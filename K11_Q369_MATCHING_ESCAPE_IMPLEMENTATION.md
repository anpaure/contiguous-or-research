# q369 matching-plateau escape

## Scope

This change strengthens only the heuristic optimization of a perfect matching
between the 1,023 lower masks and legal residual short intervals in
`k11_q369_hall_search.cpp`.  It does **not** enlarge or relax the structural
search space.  In two-component mode every accepted row still has:

- a 369-vertex and a 93-vertex rainbow Johnson path;
- the audited endpoint-color condition;
- at least 323 distinct bulk rank-four triple intersections; and
- every other condition checked by `rainbow_johnson_path(row, true)`.

A positive optimized matching score is only an upper bound for that row.  A
zero score remains an exact constructive factor certificate.  In particular,
the retained conflict-38 row has a verified UNSAT exact lower-factor CNF, so
no optimizer can legitimately reach zero on that fixed row; its value is as a
better source of row-search heat and as a calibration of the old matching
heuristic.

## Exact graded score

For a selected perfect matching `m`, define

```text
c_m(p,b) = number of matched lower intervals covering p whose target omits b.
```

For each required pin obligation `R`, let `P_R` be its possible envelope
positions (and, for a nonempty factor-position obligation, its possible bits).
The old binary test says that `R` fails exactly when

```text
min_{(p,b) in P_R} c_m(p,b) > 0.
```

The implementation now compares matchings lexicographically by:

1. the number of failed obligations;
2. the sum of the displayed minima over failed obligations (`pressure`);
3. the old position/central/target failure breakdown; and
4. minus the number of surviving zero-count pin choices (`slack`).

The first coordinate is exactly the former pin score.  `pressure=0` if and
only if the pin score is zero.  Pressure and slack therefore add a search
gradient but cannot manufacture a false certificate.

Every failed obligation is also treated as a conflict hyperedge.  A chosen
target/interval edge receives blame for each candidate pin of the failed
obligation that it blocks.  This identifies the matching variables that can
actually repair the current failure instead of heating only its physical row
positions.

## Matching moves

The old optimizer chose a uniformly random target and followed a blind
alternating path of depth at most 12 that had to finish at an unused interval.
The revised optimizer:

- starts 85% of paths from conflict-hypergraph implicated targets;
- permits depth 32;
- accepts a closed alternating cycle as well as an ejection path ending at an
  unused interval; and
- keeps the best of the cheap and refined valid matchings as a monotone
  two-member portfolio.

An ejection path or alternating cycle changes only legal target/interval
edges, keeps every lower target matched, and repeats no interval.  Before a
score is returned, the code explicitly checks all 1,023 chosen intervals are
distinct and legal.  Thus these moves preserve the exact Hall-perfect
matching invariant.

The path search exposes three tuning variables:

```text
Q369_MATCHING_TRIALS          default 1024
Q369_MATCHING_REFINE_TRIALS   default 4096
Q369_MATCHING_REFINE_MARGIN   default 12
```

## Lightweight regression

The current source compiles warning-free with

```bash
g++ -O3 -std=c++20 -pthread -Wall -Wextra -Wpedantic \
  k11_q369_hall_search.cpp -o q369_hall_search
```

ASan+UBSan evaluation at 1,024 matching trials is clean.  No path search was
run locally.  Deterministic matching-only evaluations gave:

| row | trials | conflict | pressure | central | target | D3 | upper holes |
|---|---:|---:|---:|---:|---:|---:|---:|
| `q369_two_conflict42_d3_329.txt` | old evaluator | 42 | n/a | 2 | 40 | 329 | 44 |
| same row | 4,096 | 25 | 25 | 0 | 25 | 329 | 44 |
| same row | 16,384 | 24 | 24 | 0 | 24 | 329 | 44 |
| `q369_two_conflict38_d3_328.txt` | 4,096 | 24 | 24 | 1 | 23 | 328 | 46 |
| same row | 16,384 | 17 | 17 | 0 | 17 | 328 | 46 |
| same row | 65,536 | **13** | **13** | **0** | **13** | 328 | 46 |

The 13 surviving failures are all matched-target pins.  This shows that the
nominal 38/42 plateau was substantially a matching-optimization artifact,
while the fixed-row UNSAT proof shows that some positive obstruction remains.

## Remote build and launch

Rose is currently saturated.  Do not launch until `q369_c45retain` has
finished and cores 4 and 5 have been rechecked as free.  The agreed target is
`/root/q369_refined_match_search`, tmux session `q369_refined_rose`.

After that preflight, copy the source and the conflict-38 and conflict-42 rows,
then build:

```bash
ssh -p 27423 root@157.157.221.29 \
  'mkdir -p /root/q369_refined_match_search'
scp -P 27423 \
  k11_q369_hall_search.cpp \
  scratch/certificates/k11_q369_global_factor/hall_zero/q369_two_conflict38_d3_328.txt \
  scratch/certificates/k11_q369_global_factor/hall_zero/q369_two_conflict42_d3_329.txt \
  root@157.157.221.29:/root/q369_refined_match_search/
ssh -p 27423 root@157.157.221.29
mkdir -p /root/q369_refined_match_search
cd /root/q369_refined_match_search
g++ -O3 -std=c++20 -pthread -Wall -Wextra -Wpedantic \
  k11_q369_hall_search.cpp -o q369_hall_search
./q369_hall_search --explain-two q369_two_conflict38_d3_328.txt 65536
```

The scoped two-core launch is:

```bash
tmux new-session -d -s q369_refined_rose \
  "cd /root/q369_refined_match_search && \
   Q369_MATCHING_TRIALS=4096 \
   Q369_MATCHING_REFINE_TRIALS=65536 \
   Q369_MATCHING_REFINE_MARGIN=20 \
   taskset -c 4,5 nice -n 10 ./q369_hall_search \
     --two-component 86400 2 q369_refined_runbest.txt \
     q369_two_conflict38_d3_328.txt \
     q369_two_conflict42_d3_329.txt \
     >q369_refined.stdout 2>q369_refined.log"
```

Monitor without touching the certificate jobs:

```bash
tmux capture-pane -pt q369_refined_rose -S -80
tail -40 /root/q369_refined_match_search/q369_refined.log
```
