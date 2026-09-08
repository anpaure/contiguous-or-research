# Paired-endpoint run diagnostic provenance

Executed once by `exact_b_induction` on 2026-09-09, after root's full
proof/code review and the independent source review in
`scratch/PAIRED_ENDPOINT_RUN_CHECKER_INDEPENDENT_PREEXECUTION_AUDIT_20260909.md`
by `exact_equality_structure`. Root explicitly authorized one execution.
There was no retry, scope change, construction search or word edit.

Remote directory: `/home/amodo/exact-b-paired-run-20260909/` on h100,
execution hostname `arboghast`.

The mathematical process was exactly:

```sh
python3 /home/amodo/exact-b-paired-run-20260909/verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py --k17 /home/amodo/exact-b-paired-run-20260909/k17_optimal24313.word --k18 /home/amodo/exact-b-paired-run-20260909/k18_optimal48623.word --out /home/amodo/exact-b-paired-run-20260909/certificate
```

Its stdout/stderr were redirected to the copied `execution.log`.
The program enforced 30 CPU seconds, 45 wall seconds and 1 GiB address
space. It exited successfully and reported3.6019246596843004seconds.
The code, exact report and log were copied back without modification.
No process remains live.

SHA-256 values, obtained from the remote files after completion:

```text
ba675de0908439ff68aa8da3ae9dd9ad7a5061beec900ac41f24a46f753c3f37  verify_paired_endpoint_run_theorem_and_exact_literals_20260909.py
2fdc338e54cff94664ffd07058eb7714fc8aa8f2e8bd424b497b7af930da3a67  paired_endpoint_run_diagnostic.json
b56031a03ba936fc66b5c868a0d56edc386f313ffc878137c1bbbfd2c153234b  execution.log
```

The input hashes were enforced inside the program:

```text
7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9  k17_optimal24313.word
6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5  k18_optimal48623.word
```

All137256 nonempty words over the seven nonempty three-coordinate letters
through length six passed in both endpoint orientations. The run performed
1647072 family/orientation checks,227130 shared-endpoint checks, and
454260 direct literal shared-witness replays. Counts by length were
7,49,343,2401,16807,117649.

The actual17/18 input phase checked only per-coordinate tag runs, literal
rank histograms and necessary universal-word inequalities. Full-cube
coverage was inherited from the earlier hash-pinned certificates and was
NOT recomputed in this diagnostic.

Reading the report's individual coordinate rows gives:

* Dimension17, all17 coordinates: exits2231–2232 and entrances2231–2232.
* Dimension18, old coordinates0–16: exits4462–4463 and entrances4462–4464.
* Dimension18, the new coordinate17: exits0 and entrances1. Therefore the
  ranges over all18 coordinates are exits0–4463 and entrances1–4464.

The exact literal-rank histograms, from the same report, are:

```text
k17: rank1:17, rank2:136, rank3:680, rank4:2381,
     rank5:6189, rank6:14910.
k18: rank1:18, rank2:153, rank3:816, rank4:3061,
     rank5:8568, rank6:21099, rank7:14908.
```

The same run checked1427 and4859 paired-run lower bounds; the4856 rank-nine
run-start floor versus the earlier4835; minimum53479 unmarked positions
when rank-nine literals are absent; and the97239 lower bound for at most
one exit. The proof is primary; these finite checks are diagnostic.
