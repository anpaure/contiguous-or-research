# Machine-checked certificate: the `k=15` resident seed cannot be repaired in 67 choices

Date: 2026-07-29

## Certified statement

Let `F_0` be the strict equivariant residence-clean selector stored in

`scratch/fixtures/k15_residence_hint_explicit_v1.json`.

It misses exactly 67 upper-`q=1` quotient colours.  In the strict `k=15`
quotient choice catalogue, there is **no degree-two selector covering every
upper-`q=1` colour at Hamming distance 67 from `F_0`**.

Consequently every degree-two upper-`q=1`-complete selector in this catalogue
has Hamming distance at least

\[
                              68.
\]

This is now backed by a deterministic CNF generator and an independently
checked DRAT proof, not merely a CP-SAT status.

The statement does not impose connectivity, voltage, residence after the
repair, or any deeper shadow condition.  Omitting those conditions makes the
certified lower bound stronger.

## Why distance 67 has a complete finite action model

One changed lower-orbit choice introduces at most one previously missing
upper-`q=1` colour.  Therefore a repair at distance 67 must satisfy all of the
following:

1. it chooses exactly one replacement action for each of the 67 missing
   colours;
2. every removed old colour remains represented, so an old colour of initial
   load `ell` is removed at most `ell-1` times;
3. a lower orbit is changed at most once;
4. the sum of endpoint-degree changes is zero at every central orbit vertex.

Enumerating every one-end and two-end replacement satisfying the first two
local requirements gives exactly 1646 actions.  This is the complete
radius-67 action set, not a local-search sample.

For an action `a`, let `delta_a(v)` be its endpoint-degree change at central
orbit vertex `v`.  If `x_a` is its Boolean selector, degree preservation is

\[
                 \sum_a \delta_a(v)x_a=0.
\]

## A strictly relaxed UNSAT core

The proof deliberately uses fewer constraints than the full action model:

- all 1646 action variables are retained;
- only 65 of the 67 target equalities are retained (the equalities for masks
  `1951` and `3451` are omitted, leaving those actions optional);
- only 343 of the 429 endpoint-degree equalities are retained;
- every lower-orbit at-most-one constraint is omitted;
- only two old-colour capacities are retained:

  - mask `6999`, initial load 2, removal capacity 1;
  - mask `7597`, initial load 2, removal capacity 1.

The complete lists are recorded in
`scratch/k15_radius67_colour_greedy_iis.json` and copied into the CNF
metadata.  Since constraints were deleted while all action variables were
kept, this is a relaxation of the full radius-67 problem.  UNSAT of the
relaxation proves UNSAT of the full model.

The two colour masks are, in zero-based coordinate notation,

\[
\begin{aligned}
6999 &= \{0,1,2,4,6,8,9,11,12\},\\
7597 &= \{0,2,3,5,7,8,10,11,12\}.
\end{aligned}
\]

## Independent CNF encoding

`scratch/generate_k15_radius67_core_cnf.py` rebuilds the catalogue and the
1646 actions from the seed.  It encodes:

- retained target sums with an exact-one sequential counter;
- the two retained removal capacities with at-most counters;
- every retained signed degree equality exactly.

For the last item, if `P_v` and `N_v` are respectively the positive and
negative action literals at vertex `v`, then

\[
 \sum_{a\in P_v}x_a=\sum_{a\in N_v}x_a
 \iff
 \sum_{a\in P_v}x_a+\sum_{a\in N_v}(1-x_a)=|N_v|.
\]

The right-hand side is an ordinary exact-cardinality constraint, avoiding
any reliance on one-directional totalizer outputs.

The resulting formula has

\[
               28{,}998\text{ variables},\qquad
               56{,}979\text{ clauses}.
\]

Clause breakdown:

| family | clauses |
|---|---:|
| 65 target exact-one constraints | 4,590 |
| two old-colour capacities | 76 |
| 343 degree equalities | 52,313 |

## Proof and independent verification

Kissat 4.0.4 returned `UNSATISFIABLE` and emitted an ASCII DRAT proof.
`drat-trim` then independently reported:

```text
c parsing input formula with 28998 variables and 56979 clauses
c detected empty clause; start verification via backward checking
c 9427 of 56979 clauses in core
c 2986 of 31946 lemmas in core using 437593 resolution steps
c 0 RAT lemmas in core; 785 redundant literals in core lemmas
s VERIFIED
c verification time: 0.436 seconds
```

Authoritative artifact hashes:

| artifact | SHA-256 |
|---|---|
| `scratch/k15_radius67_core.cnf` | `e8b0b9690de36bfd5b7fde2efe7e84cb0402c6a23836fbd0f3b2f372afceedd9` |
| `scratch/k15_radius67_core.drat` | `8e7f821502672259ad8a314c6fde3540b9949d5d8e42f0fcae7dbd853eec7ed6` |
| `scratch/k15_radius67_colour_greedy_iis.json` | `acf167155dc70518de7e3060620a5f29a18c434b0cc29cca6af788ad1438e1b5` |

The deterministic bundle checker is
`scratch/verify_k15_radius67_drat_bundle.py`.  From the remote repository
directory containing `drat-trim`, run:

```bash
python3 verify_k15_radius67_drat_bundle.py
```

It first regenerates the CNF byte-for-byte from the seed and action catalogue,
checks the stored hashes, and only then invokes `drat-trim`.  The verified
output is:

```json
{"clauses": 56979, "cnf_sha256": "e8b0b9690de36bfd5b7fde2efe7e84cb0402c6a23836fbd0f3b2f372afceedd9", "proof_sha256": "8e7f821502672259ad8a314c6fde3540b9949d5d8e42f0fcae7dbd853eec7ed6", "status": "VERIFIED", "variables": 28998}
```

## Interpretation and boundary of the result

This closes the evidentiary gap in the earlier radius audit: **67 changes are
formally impossible**, even before imposing most carrier requirements.

It does not show that radius 68 is feasible.  It also does not lower the
current Hall deficiency of the best fully formed non-equivariant `k=15`
carrier.  Its immediate algorithmic consequence is narrower but useful:
searches centred on the residence-clean quotient seed should not allocate any
time to radius 67; radius 68 is the first mathematically admissible shell.

