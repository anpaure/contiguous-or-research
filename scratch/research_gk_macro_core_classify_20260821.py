#!/usr/bin/env python3
"""Classify recurrent prefixes from the one-reset length-b GK macro graph.

Research-only; run on H100.
"""

from collections import Counter, defaultdict
import argparse
import importlib.util
from itertools import permutations
from pathlib import Path


def load_module():
    path = Path(__file__).with_name("research_gk_length_b_macro_reset_core_20260821.py")
    spec = importlib.util.spec_from_file_location("macro_core", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def gap_signature(prefix: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(prefix[i + 1] - prefix[i] for i in range(len(prefix) - 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    module = load_module()
    data = module.build(args.b, True)
    states = data["core_states"]
    by_runs: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    signatures: Counter[tuple[int, ...]] = Counter()
    for state in states:
        prefix = state[:-1]
        runs = module.interval_runs(prefix)
        by_runs[len(runs)].append(state)
        signatures[gap_signature(prefix)] += 1
    print("B", args.b, "CORE", len(states))
    print("SIGNATURES")
    for sig, count in sorted(signatures.items(), key=lambda z: (len(z[0]), z[0])):
        print(count, sig)
    for run_count in sorted(by_runs):
        print("RUN_COUNT", run_count, "N", len(by_runs[run_count]))
        for state in sorted(by_runs[run_count]):
            print(state, module.interval_runs(state[:-1]))

    # Test whether the {-1,-3} mod (2b-1) signature is generic for every
    # length-b strong macro, or is forced only by recurrence.
    b = args.b
    n = 2 * b
    add_cache = {}

    def aa(q):
        source = frozenset(q)
        if source not in add_cache:
            add_cache[source] = module.additions(n, source)
        return add_cache[source]

    def strong_step(q):
        add = aa(q)
        if not add:
            return None
        nxt = q[1:] + (add[0],)
        nxt_add = aa(nxt)
        common = min(len(nxt_add), max(0, len(add) - 1))
        if len(add) == 1 or (
            common > 0 and nxt_add[:common] == add[1 : 1 + common]
        ):
            return nxt
        return None

    mod = 2 * b - 1
    macro_count = 0
    good_signature = 0
    violation_hist = Counter()
    valid_starts = {}
    for q0 in permutations(range(n), b):
        q = q0
        forced = []
        for _ in range(b - 1):
            add = aa(q)
            if not add:
                q = None
                break
            forced.append(add[0])
            q = strong_step(q)
            if q is None:
                break
        if q is None:
            continue
        macro_count += 1
        valid_starts[q0] = tuple(forced)
        gaps = tuple((forced[i + 1] - forced[i]) % mod for i in range(b - 2))
        bad = sum(gap not in (mod - 1, mod - 3) for gap in gaps)
        many_skip = sum(gap == mod - 3 for gap in gaps) > 1
        if bad == 0 and not many_skip:
            good_signature += 1
        else:
            violation_hist[(bad, many_skip)] += 1
    print(
        "ALL_MACRO_SIGNATURE",
        b,
        "MACROS",
        macro_count,
        "GOOD",
        good_signature,
        "VIOLATIONS",
        sorted(violation_hist.items()),
    )

    def badness(prefix):
        gaps = [
            (prefix[i + 1] - prefix[i]) % mod for i in range(len(prefix) - 1)
        ]
        skips = sum(gap == mod - 3 for gap in gaps)
        return sum(gap not in (mod - 1, mod - 3) for gap in gaps) + max(
            0, skips - 1
        )

    delta_hist = Counter()
    nondecreasing_bad = []
    for q0, forced in valid_starts.items():
        old = badness(q0[:-1])
        for sentinel in range(n):
            if sentinel in forced:
                continue
            nxt = forced + (sentinel,)
            if nxt not in valid_starts:
                continue
            new = badness(forced)
            delta_hist[(old, new)] += 1
            if old > 0 and new >= old and len(nondecreasing_bad) < 20:
                nondecreasing_bad.append((q0, forced, sentinel, old, new))
    print(
        "BADNESS_TRANSITIONS",
        b,
        sorted(delta_hist.items()),
        "NONDECREASING_BAD_EXAMPLES",
        nondecreasing_bad,
    )


if __name__ == "__main__":
    main()
