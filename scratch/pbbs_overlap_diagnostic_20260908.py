"""Bounded physical PBBS diagnostic. Execute ONLY via ssh h100.

Uniform independent subsets, fixed base phase, and literal full return
intervals. Finite statistics are exploratory, never asymptotic certificates.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import json
import math
import pathlib
import signal
import socket
import time
import resource

assert socket.gethostname().lower() == "arboghast", "Execute only on verified ssh h100 host"
allowed = sorted(os.sched_getaffinity(0))
os.sched_setaffinity(0, allowed[:2])
resource.setrlimit(resource.RLIMIT_CPU, (140, 145))
resource.setrlimit(resource.RLIMIT_AS, (3 * 1024**3, 3 * 1024**3))
import numpy as np

START = time.monotonic()
DEADLINE = START + 120
TRIALS = 4096
BATCH = 128
SEED = 202609080117
rng = np.random.default_rng(SEED)
out_path = pathlib.Path(__file__).with_name("results.json")
result = {"seed": SEED, "planned_trials_per_r": TRIALS,
          "batch": BATCH, "wall_cap_seconds": 120,
          "physical_horizon": "0,...,6Hmax+5 inclusive",
          "base_phase": "B=Hmax+1, physical time 2B",
          "runs": [], "status": "running"}


def save():
    result["wall_seconds"] = time.monotonic() - START
    out_path.write_text(json.dumps(result, indent=2) + "\n")


def summarize(records, trials):
    if not records:
        return {"retained": 0}
    a = np.asarray(records, dtype=np.float64)
    weights, counts = a[:, 0], a[:, 1]
    total = weights.sum()
    order = np.argsort(counts)
    cdf = np.cumsum(weights[order]) / total
    quantiles = {
        str(q): int(counts[order[np.searchsorted(cdf, q)]])
        for q in [0.1, 0.5, 0.9]
    }
    occupied = float(np.sum(weights / counts) / trials)
    # Include the zero contributions of rejected newborn trials.
    second = float(np.sum((weights / counts)**2) / trials)
    se = math.sqrt(max(0.0, second - occupied**2) / trials)
    return {"retained": len(records),
            "incidence_effective_n": float(total**2 / (weights @ weights)),
            "mu_hat": float(total / trials),
            "occupied_fraction_hat": occupied,
            "occupied_fraction_standard_error": se,
            "incidence_mean_K": float(weights @ counts / total),
            "incidence_K_quantiles": quantiles,
            "incidence_probability_K_le_2": float(weights[counts <= 2].sum() / total),
            "incidence_probability_K_le_5": float(weights[counts <= 5].sum() / total),
            "min_K": int(counts.min()), "max_K": int(counts.max())}


for r in [32, 64, 128, 256]:
    n = 2*r + 1
    cuts = {str(c): int(math.floor(c*math.sqrt(r))) for c in [2, 3, 4]}
    hmax = max(cuts.values())
    assert hmax < r
    bbase = hmax + 1
    tbase = 2*bbase
    tlen = 6*hmax + 6
    nbirth = 2*hmax + 3
    accum = {c: {"all": [], "top_zero": []} for c in cuts}
    done = 0
    run_start = time.monotonic()
    while done < TRIALS and time.monotonic() < DEADLINE:
        batch = min(BATCH, TRIALS-done)
        row = np.arange(batch)
        template = np.arange(n) < r
        bits = rng.permuted(np.broadcast_to(template, (batch,n)), axis=1)
        labels = np.empty((batch, tlen), dtype=np.int32)
        topzero = np.empty((batch, nbirth), dtype=np.bool_)
        for t in range(tlen):
            prefix = np.cumsum(bits.astype(np.int16)*2-1, axis=1, dtype=np.int32)
            lam = np.argmin(prefix, axis=1)
            labels[:, t] = lam
            assert not np.any(bits[row, lam])
            assert not np.any(bits[row, (lam-1) % n])
            if t % 2 == 0 and t//2 < nbirth:
                topzero[:, t//2] = ~bits[row, (lam-2) % n]
            bits = ~bits
            bits[row, lam] = False

        # Return times are found among ALL integer physical phases.
        last = np.full((batch, n), tlen+1000, dtype=np.int32)
        lifetime = np.full((batch, nbirth), hmax+1, dtype=np.int32)
        for t in range(tlen-1, -1, -1):
            lam = labels[:, t]
            nxt = last[row, lam]
            finite = nxt < tlen
            assert np.all((nxt[finite]-t) % 2 == 1)
            if t % 2 == 0 and t//2 < nbirth:
                short = finite & (nxt-t <= 2*hmax+1)
                lifetime[short, t//2] = (nxt[short]-t-1)//2
            last[row, lam] = t

        for i in range(batch):
            tb = int(lifetime[i, bbase])
            if tb > hmax:
                continue
            j = int(rng.integers(0, tb+2))
            edge = bbase + j
            weight = tb + 2
            for c, cutoff in cuts.items():
                if tb > cutoff:
                    continue
                births = np.arange(edge-cutoff-1, edge+1)
                assert births[0] >= 0 and births[-1] < nbirth
                lt = lifetime[i, births]
                hit = (lt <= cutoff) & (births+lt+1 >= edge)
                k = int(np.count_nonzero(hit))
                assert k >= 1
                accum[c]["all"].append((weight, k))
                if topzero[i, bbase]:
                    k0 = int(np.count_nonzero(hit & topzero[i, births]))
                    assert 1 <= k0 <= k
                    accum[c]["top_zero"].append((weight, k0))
        done += batch

    run = {"r": r, "n": n, "trials": done,
           "complete_fixed_trial_batch": done == TRIALS,
           "wall_seconds": time.monotonic()-run_start,
           "cutoffs": {c: {"H": cutoff,
                           "all": summarize(accum[c]["all"], done),
                           "top_zero": summarize(accum[c]["top_zero"], done)}
                       for c, cutoff in cuts.items()} if done else {}}
    result["runs"].append(run)
    save()
    print(json.dumps(run), flush=True)
    if done != TRIALS:
        break

result["status"] = ("complete" if len(result["runs"]) == 4 and
                    all(x["complete_fixed_trial_batch"] for x in result["runs"])
                    else "wall_cap_partial")
save()
print(json.dumps({"status": result["status"], "results": str(out_path),
                  "wall_seconds": result["wall_seconds"]}), flush=True)
