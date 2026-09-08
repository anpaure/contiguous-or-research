# Audit of the per-chain `Q_6 -> Q_8` lift no-go theorem

## Verdict

`PER_CHAIN_OSCD_LIFT_NO_GO.md` passes audit.

The decisive conclusion does not depend on trusting a SAT solver.  For each
of the `24` good `Q_6` seeds, an independently reconstructed relaxed
candidate graph has maximum matching `55/56` and a displayed three-to-two
Hall witness.  Since the relaxation drops both shared-mode consistency and
cross-chain orthogonality, this proves that no per-chain lift assignment can
have injective central unions.  It retains only the necessary pointwise
condition that the two successors differ; otherwise their union has rank
four rather than the required upper rank five.

The local lift-fork lemma correctly explains every displayed witness.  The
SAT formulation is exact and agrees with the Hall result, but its UNSAT
output is diagnostic rather than the primary certificate.

## 1. Lift convention

For `C=(x_0,...,x_t)`, mode zero gives

\[
 (x_0,\ldots,x_t,x_tz),\qquad
 (x_0z,\ldots,x_{t-1}z),
\]

and mode one gives

\[
 (x_0,x_0z,\ldots,x_tz),\qquad
 (x_1,\ldots,x_t).
\]

Each nonempty child is saturated.  If `C` starts in rank `r` and ends in
rank `n-r`, the long child starts/ends in complementary ranks of `Q_(n+1)`,
and the short child does likewise.  The children partition the low and high
copies of `C`.  Hence independent modes on different chains always produce
an SCD.

A `Q_6` SCD has `20` chains.  Its first lift has `35` chains, so a pair has
`2(20+35)=110` mode variables over two stages, as stated.

## 2. SAT-width claims

For one lift, descendants of a fixed cross-pair of original chains depend
only on their two mode bits.  Deleting every bad truth-table row by a binary
clause is therefore necessary and sufficient for almost orthogonality.
This proves the 2-SAT claim without assuming a special endpoint pattern.

For two lifts, one original parent has at most two first-stage children.
A cross-pair of parents therefore uses at most two parent bits and four
child bits.  Enumerating its complete local truth table gives clauses of
width at most six for final orthogonality.

A rank-three `Q_8` mask has one fixed `Q_6` parent chain.  Its successor in
one decomposition is determined by the parent's first bit and the active
child's second bit.  Two decompositions use at most four bits; an equal-union
event for two lower masks uses at most eight.  This verifies the width-eight
collision claim.

The encoder materializes exactly these truth tables.  Random assignments
were independently reconstructed into full `Q_7,Q_8` SCDs and compared
against both the orthogonality-only and union-only CNFs.  No discrepancy was
found.  More importantly, the union-only UNSAT conclusion follows from the
independent Hall verifier below.

## 3. Exhaustiveness of local successor candidates

Fix a rank-three mask `S` of `Q_8`.

1. Its restriction to the first six coordinates belongs to a unique
   original `Q_6` chain.
2. For either first-stage mode, its restriction to `Q_7` belongs to one
   uniquely determined child role.
3. Either second-stage mode on that active child determines its final chain
   and rank-four successor.

Thus four local cases exhaust the possible successor in one decomposition.
Taking the Cartesian product for `D,E` exhausts all possible successor
unions.  Modes on inactive chains cannot affect this mask.

The candidate graph deliberately allows these local cases to be selected
independently for different `S`.  Every genuine global assignment is
therefore a subcase of the graph.  A Hall obstruction in this graph is a
valid no-go theorem even before orthogonality is imposed.

## 4. Audit of the lift-fork lemma

Let `x<y` be an original chain edge.

* If `x` is nonbottom, its copies `x+p` and `x+q` keep successors `y+p` and
  `y+q` after two arbitrary lifts.  A mode-one split can remove only the
  bottom low copy; it cannot remove the edge at a nonbottom `x`.  The high
  copy is also nonterminal because `y` exists.
* If at least two members lie below `x`, then after the first split the old
  low copy of `x` is still nonbottom under either mode.  Its old successor
  `y` therefore survives the second split.
* A singleton `{x}` first becomes `(x,x+p)`.  The next lift puts `x+p` after
  `x` in mode zero and `x+q` after `x` in mode one.

For a lift fork, the first item fixes the successor unions at `S+p,S+q` as
`V+p,V+q`.  The second and third items restrict the union at `A` to those
same two values.  Hence three lower masks have only two upper candidates.
All rank calculations agree: after lifting `Q_(2m)` twice, `S+p,S+q,A`
have rank `m`, the lower central rank, and `V+p,V+q` have rank `m+2`, the
upper central rank.

The depth hypotheses in the definition are necessary for this proof.  In
particular, merely requiring `A` to be nonbottom would not ensure that its
old successor survives two successive mode-one splits.  The main note
correctly requires two members below it.

## 5. Independent finite verification

`scratch/verify_per_chain_q6_q8_hall.py` independently reimplements:

* both one-chain lift modes;
* almost orthogonality;
* central successor maps and union injectivity;
* generation of the `84` good `Q_4` pairs and the `24` global-mode good
  `Q_6` seeds;
* all local per-chain successor cases;
* bipartite maximum matching and alternating-tree Hall witnesses;
* direct detection of the lift-fork configuration.

For every seed it checks:

\[
 |L_H|=3,\qquad |N(L_H)|=2,
\]

the three candidate-set sizes are `1,1,2`, and the full candidate matching
has size exactly `55`.  It also checks that the Hall witness is induced by a
literal lift fork in the underlying `Q_6` pair.

The final output is

```text
verified 84 good Q4 pairs are fork-free
verified 24 Q6 seeds; maximum candidate matching 55/56 each
```

The seed table printed by the verifier agrees row-for-row with Section 5 of
the main note.

## 6. SAT cross-check

For each seed, the exact encoder reports

```text
orthogonality only: SAT, 110 variables, 776 clauses
union only:         UNSAT, 110 variables, 2661 clauses
both:               UNSAT, 110 variables, 3325 clauses
```

The equality of clause counts across the `24` seeds is consistent with the
uniform fork structure and their symmetry-related local catalogs.  No
solver proof trace is required for the theorem because the independently
checked Hall witness is a short mathematical UNSAT certificate.

## 7. Reproduction

Run:

```bash
python3 scratch/verify_per_chain_q6_q8_hall.py
python3 scratch/per_chain_oscd_lift_q6_q8_sat.py --seed -1 --only-orthogonality
python3 scratch/per_chain_oscd_lift_q6_q8_sat.py --seed -1 --only-union
python3 scratch/per_chain_oscd_lift_q6_q8_sat.py --seed -1
```

The Hall verifier takes well under one second on the audited machine.  The
three SAT passes together take under twenty seconds.

SHA-256:

```text
b4425d84d587c32048165c5040567db789316d4db8dc9af665634443f758840e  PER_CHAIN_OSCD_LIFT_NO_GO.md
0fdaf8939166b3697958901b7b7c65d5ef0b2b9b058cf102f0a058ae45d5c0b0  scratch/per_chain_oscd_lift_q6_q8_sat.py
97ee5f407a607b8f4e24228cae748c44694a10e8d3c8351d6050712e26eb8a49  scratch/verify_per_chain_q6_q8_hall.py
```

## 8. Guardrails

The result rules out only the `24` `Q_6` seeds generated by the stated
global-mode history and only lifts that retain fixed parent chains while
choosing their two standard modes independently.

It does **not** prove:

* that every union-perfect OSCD pair on `Q_6` contains a lift fork;
* that fork-freeness is sufficient for a successful lift;
* that nonlocal chain splicing cannot work;
* the general orthogonal two-SDR lemma.

The correct strategic conclusion is narrower and decisive: the current
`24` seeds cannot be repaired by per-chain mode freedom, because their
failure occurs already in a relaxed three-to-two Hall neighborhood.
