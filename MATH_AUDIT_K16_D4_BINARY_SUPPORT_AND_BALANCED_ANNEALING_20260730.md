# K16 D4 binary support audit and balanced-cycle annealing lane

Date: 2026-07-30

## 1. The denominator-four support does not contain a binary C=105 seed

The exact fractional direct-cycle primal of value `207/2` has 174 nonzero
physical seams.  On the frozen length-eight K16 catalogue those seams form a
port permutation with eight directed cycles.  Their lengths are

```text
15, 15, 15, 18, 18, 18, 30, 45.
```

Any binary endpoint-balanced subset of this support is a union of whole
cycles.  There are exactly three subsets of cardinality 105, all of cycle
type

```text
45 + 30 + 15 + 15.
```

Each services exactly 75 of the 93 frozen q<=3 defects, leaving 18.  Hence
there is no binary balanced/service C=105 selection inside the 174-seam D4
support.  This is solver-free enumeration of `2^8` cycle subsets, not a
timed-solver verdict.

Canonical replay:

```text
scratch/audit_k16_d4_binary_c105_support_20260730.py
  SHA-256 d89060fb66789e2bd78ce0f2365b39c4e8ebc8882217c3c87f397ece319e94e6

scratch/k16_d4_binary_c105_support_20260730.audit.json
  SHA-256 938dad01b74604e0fddd6e0ce62d6892e8a80fbbffd9876bab1ba5ebee33b381
```

The canonical audit was run on the H100 CPU host under a 512 MiB / 60 CPU-s
cap.  It records all cycles, all three C=105 subsets, their covered targets,
and an empty feasible-mask list.

## 2. Fractional branch bases do round to exact balanced cycle packs

For a fractional capacity-one circulation `x`, add a dummy diagonal edge of
mass

```text
1 - sum_v x(u,v)
```

at every active port.  Endpoint balance makes the augmented matrix doubly
stochastic.  Randomized Birkhoff--von Neumann decomposition therefore emits
integral permutations.  Removing dummy fixed points leaves a binary
endpoint-balanced, capacity-one seam-cycle pack.

Applied to the exported C=105 branch LP bases, this produces many integral
components with exactly 105 physical seams.  The first C++ scans gave:

```text
D4 whole-cycle seed                         18 missing targets
best generic LP-rounded seed                11 missing, weight 44, slack 0
best targeted slack-2 LP-rounded seed       15 missing, weight 46, slack 2
best targeted slack-3 LP-rounded seed       19 missing, weight 41, slack 3
```

The weighted deficit is the correct continuation coordinate.  For every
balanced C=105 state,

```text
repeat_weight - missing_weight + direct_slack = 3.
```

Thus the visually attractive 11-hole state is actually a slack-zero state
with eleven missing weight-four targets.  It is farther in direct-dual mass
than the 19-hole slack-three state.

## 3. Exact annealing state and move

The annealer never edits the raw word.  Its state is a permutation of all
12,870 ports:

* a dummy fixed point means that the source transition is not cut;
* a nonfixed edge is one selected physical seam.

Consequently endpoint balance and port capacity are hard invariants.  An
annealing move is an alternating circuit in the tail/head bipartite
matching.  Dummy diagonal edges are included, so an alternating circuit can
both deactivate old ports and activate new ones.  Hot replicas may leave the
requested cardinality temporarily, but only states at the requested count and
direct-slack face can replace the incumbent or be written to disk.

The current engine additionally has:

1. randomized Birkhoff seed generation from multiple LP bases;
2. missing-target provider-forced alternating BFS;
3. explicit selected-cycle ruin moves;
4. unused-port physical-cycle recreate moves;
5. a missing-weight-primary objective and independent slack-2/slack-3 lanes;
6. parallel tempering, with circuits as long as 1,024 seams observed in
   smoke tests.

Code:

```text
scratch/k16_balanced_cycle_anneal_20260730.cpp
```

Every emitted service-pass candidate must be replayed by the independent
fail-closed checker

```text
scratch/replay_k16_floor105_candidate_20260730.py
```

which checks count, distinct seam IDs, endpoint equality, port capacity,
all 93 services, direct accounting, physical materialization, source-cut
separation, q1 and deeper signed rows, residence, and full shadow coverage.

## 4. The live source-relative target is now C=106

The later five-lock automaton exhausts all 1,776 C=105 branches in the full
frozen seam catalogue.  It proves that this source carrier cannot be repaired
with 105 seams.  This is a source-relative theorem, not a lower bound over all
K16 carriers.  Two independently checked artifacts are

```text
scratch/threadB_k16_floor106_authenticated_20260730.audit.json
  SHA-256 e9db884cd069ebbf3218848832aecc469939836ba42cb134d64392ed866d0feb

scratch/k16_floor106_root_independent_replay_20260730.audit.json
  SHA-256 93ae9e2e3a39b8a0530ff9c876eb033dcd4174123c50d0919c681a6eb107ea99
```

At C=106 each of five lock groups either pays one slack unit (`S`) or repeats
one of three weight-one targets (`0`, `1`, `2`).  The 243 no-slack signatures
were all tested as continuous capacity-one circulations on the exact
1,930-arc tight cyclic graph.  All 243 are infeasible, so this is a complete
S0 fractional no-go in that graph, not merely a test of `00000`:

```text
scratch/k16_floor106_s0_capacity_lp_census_20260730.audit.json
  SHA-256 bf8fd90ee3417925c200204983676c3594c88921d8b19bbcded4adcf53a24345
```

The 781 positive-slack signatures are being censused before any further long
anneal.  In particular, the R2 group relaxation is feasible but its leading
fixed signature `1SS01` is infeasible: mixing signatures must not be confused
with a viable integer-search face.

## 5. Exact branch scoring and global-escape ruin moves

The broad C=106 S1 calibration reached 16 missing services of weighted mass
34, but still violated the five-lock normal form by 20.  In the SSSSS face an
exact rational capacity-one point exists on 662 seams and decomposes into 94
directed cycle columns.  Exact binary optimization over just those columns
has optimum 21 missing targets of weighted mass 46:

```text
scratch/k16_floor106_s5_capacity_exact_20260730.audit.json
  SHA-256 7f9780503ca106052044dc0b13604666509602e80f9bf7df6b091bbaa62c806e

scratch/k16_c106_s5_cycle_columns_20260730.audit.json
  SHA-256 42a8eb143172f1d5392e3d39cc08896b666451dc7120d7b2a3ecb7980154759c
```

The support, its active-vertex induced expansion, and its one-endpoint
incident expansion are all exact-binary infeasible.  A successful SSSSS
repair therefore needs a new cycle with a genuine outside-to-outside arc.
The C++ engine now:

1. accepts an explicit five-character `--lock-signature` and scores exact
   per-target multiplicities;
2. refuses `SERVICE_PASS` until service, slack and signature are all exact;
3. marks the 662-support/571-port region;
4. adds an outside directed cycle and removes selected whole cycles of the
   same total length and slack in one balanced capacity-preserving move.

A ten-second H100 smoke test produced the first such exact-face escape state:
C=106, slack five, balanced endpoints, capacity one, and the outside two-cycle
`[109326,199546]`.  It has 30 service holes of weighted mass 69, so it is a
move-invariant test, not progress toward a witness.  Independent replay:

```text
scratch/k16_c106_s5_global_escape_smoke_replay_20260730.audit.json
  SHA-256 e46f42c3737ddc0c8de8340458d46b6acf2b4c4da48b6bd2ece245eca789fa81
```

The next justified stochastic run is a short, branch-specific run warm-started
from the first genuinely feasible signature in the 781-signature census.  A
blind long S1/S5 anneal is not warranted.

## Scope

The D4 statement concerns only its 174-seam support.  The stronger C=105 floor
concerns the full frozen source-relative catalogue, but does not rule out a
different K16 carrier.  The S0 census concerns the tight cyclic graph, while
the SSSSS no-goes concern the named column expansions.  Likewise an annealing
plateau is evidence about one stochastic lane, never an UNSAT theorem.  Only
a C=106 candidate passing an updated independent physical replay and the
final compiler is a K16 repair witness.
