# Thread D: exact all-cut joint-history to COMP3 bridge

Date: 2026-07-30

## Result

`scratch/threadD_k16_joint_history_comp3_bridge_20260730.py` is a fail-closed
postprocessor for a `PASS_COMPILER_SHADOWS` artifact emitted by
`scratch/solve_even_two_rail_joint_history_kissat_20260730.py`.

It does not use a source carrier, edit radius, seam hint, or source-relative
constraint.  It independently rebuilds the complete transition catalogue,
replays the selected quotient circuit from root zero, checks every mathematical
field of the materialized carrier, and recomputes the cyclic q2/q3 and
arbitrary-width upper audit.

For a physical Hamilton cycle of length `W`, the postprocessor accounts for
all `2W` compiler chronologies: every deleted edge and both orientations.  The
only atlas-level rejection is an exact necessary upper-survival obstruction.
Lower fixed-window losses are recorded but are not used to reject a state.

## Exact upper cut theorem

Fix a cyclic middle chronology `T_0,...,T_{W-1}` and an upper target `S`.
For every start `a` at which a cyclic interval can attain `S`, let `b(a)` be
the first endpoint for which

```
T_a union T_{a+1} union ... union T_{b(a)} = S.
```

Every later endpoint with the same union crosses a superset of the cyclic
edges crossed by `[a,b(a)]`.  Therefore the set of cut edges destroying every
`S` witness is exactly

```
intersection_a edges([a,b(a)]).
```

A cut survives the complete upper bank iff it is outside this intersection
for every upper target.  Reversing the chronology does not alter the family of
cyclic vertex blocks, so the result is orientation-independent.  The code
computes first endpoints from coordinate occurrence lists and represents edge
sets as exact Python-integer bitsets.

This is a necessary-and-sufficient upper filter.  It does not presume a fixed
q-edge upper witness.

## Exact boundary and compiler gate

For each surviving oriented cut, the bridge constructs the literal linear
COMP3 geometry.  It enumerates candidate incidences cell-first.  A lower target
is rejected if it has no candidate cell.  Every target whose complete
candidate set lies in boundary cells is placed in one bipartite boundary SDR;
the exact Hopcroft--Karp deficiency is checked before CP-SAT.  This includes,
but is not limited to, a q1 colour lost at the cut.

The fixed-state compiler then runs with:

- exactly one CP-SAT worker;
- an explicit per-state time limit and a total portfolio time limit;
- a mandatory finite external `RLIMIT_AS`, checked against the declared cap;
- the literal source requirement `{z}=32768`;
- the complete boundary-only SDR in the same source-bit model;
- lazy exact rows for every remaining lower target.

The output word path must be fresh.  A decoded word is accepted only after a
second verifier, independent of the COMP3 audit routine, checks:

1. exact `D^3 A = T`;
2. the complete rank-eight middle deck and Johnson chronology;
3. every source letter is a nonempty 16-bit mask;
4. an actual source letter equals `32768`;
5. every lower mask occurs in a source interval of length at most three;
6. every upper mask occurs in an arbitrary-width middle interval;
7. all 65,535 nonempty masks occur as source-word interval unions.

No word is written before all seven checks pass.

## Deterministic state accounting

The atlas records all upper-safe and upper-unsafe cut edges.  Compiler states
are ordered by increasing cut edge, then `forward`, `reverse`.  A bounded run
that does not visit the complete state list returns
`UNKNOWN_INCOMPLETE_STATE_PORTFOLIO`; an UNKNOWN fixed-state solve is never
converted into UNSAT.  A checkpoint containing every attempted state is
written after each state.

## Regression

`scratch/test_threadD_k16_joint_history_comp3_bridge_20260730.py` is a
laptop-light four-test suite.  On the retained fresh K10 carrier it proves:

- the producer selection rematerializes exactly and a one-bit carrier tamper
  is rejected;
- the upper intersection formula agrees target-for-target with literal replay
  for all 252 cut edges and both orientations (504 paths);
- 72 cut edges are upper-safe and 180 are upper-obstructed;
- every cut/orientation state is represented exactly once in the atlas;
- the retained 254-letter word passes the independent 1,023-mask replay at
  cut edge 251, forward orientation.

Run:

```sh
python3 scratch/test_threadD_k16_joint_history_comp3_bridge_20260730.py
```

The K16 audit stage is solver-free:

```sh
python3 scratch/threadD_k16_joint_history_comp3_bridge_20260730.py audit \
  --candidate BRANCH_PASS.json --expected-k 16 \
  --atlas WORK/all_cut_atlas.json --output WORK/audit.json
```

The portfolio must be launched on the H100 CPU under an outer cap.  A typical
single-process shape is:

```sh
prlimit --as=2147483648 --cpu=3600 -- \
  env PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_k16_joint_history_comp3_bridge_20260730.py run \
  --candidate BRANCH_PASS.json --work WORK \
  --output WORK/result.json --output-word WORK/k16.word \
  --per-state-seconds 300 --total-seconds 3300 --max-states 64 \
  --workers 1 --batch 64 --max-address-space-bytes 2147483648
```

The portfolio caller should invoke this bridge immediately when a branch emits
`PASS_COMPILER_SHADOWS`.  A nonzero exit status means rejection, scoped UNSAT,
or UNKNOWN according to the persisted result; it is never a word certificate.
