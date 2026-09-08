# The standard MMM defect matches the nine-turn atom only at the base

Date: 2026-07-31  
Status: exact block characterization; complete physical MMM census at
grounds 9 and 11; one-glue census at ground 13; no asymptotic packing theorem

## 0. Verdict

The commuting nine-turn packet is the exact repair atom for the standard
project-`m=5` defect, but the match does not persist literally under the
standard MMM recursion.

On `ML(9)`, one of the two labelled MMM Hamilton endpoints has holes

```text
lower: 73,146,292
upper: 219,365,438,
```

which are exactly one common-core three-partition block.  This is the root
repaired by the three translated `C10` switches.

Already on `ML(11)`, every labelled MMM gluing-tree Hamilton endpoint has
22 holes on each shore.  Among all 112 endpoints, only six admit seven
pairwise-disjoint padded nine-turn blocks.  Each of those six has exactly
one such packing, and the remaining lower and upper holes are **not nested**.
Consequently they cannot be repaired by the padded unit macro either.

Thus the natural MMM debt is not a disjoint union of the new blocks, even
up to one nested unit remainder.  This is a finite shape obstruction, not an
asymptotic obstruction: the best endpoints still put 21 of 22 holes on each
shore into seven blocks.  A uniformly bounded residual gadget basis could
therefore keep the regenerative route alive.

The next dimension confirms that this is not only congruence.  The canonical
`ML(13)` endpoint has 117 holes per shore and 274 admissible blocks, but one
lower and two upper holes occur in no block.  Exact branch-and-bound rules out
38 disjoint blocks, so this endpoint leaves at least six holes per shore
after block packing.  Replacing one canonical gluing label by any other label
which keeps the auxiliary graph a tree gives 56 Hamilton endpoints.  Every
one has an uncovered lower and an uncovered upper hole.  The best exchange
improves the block catalogue to 275 and leaves only one uncovered hole on
each shore, but still has no 38-block packing.

The exact lesson is:

> The padded nine-turn cube is a real dimension-uniform actuator, but it is
> not a closed basis for the defect emitted by the stateless MMM recursion.
> An induction must either carry deliberately normalized three-partition
> debt or add at least one further bounded residual gadget type.

## 1. Exact block characterization

Use project parameter `n`, so the middle-level graph has ground size
`2n+1`, shores of ranks `n,n+1`, and turn palettes of ranks `n-1,n+2`.
Padding the `ML(9)` packet uses a common set `H` of size `n-4` and three
pairwise-disjoint triples `Q_0,Q_1,Q_2`.  Its holes are

\[
 L_i=H\cup Q_i,
 \qquad
 U_{ij}=H\cup Q_i\cup Q_j\quad(0\le i<j\le2).       \tag{1.1}
\]

### Lemma 1.1 (intrinsic recognition)

Three lower holes `L_0,L_1,L_2` and three upper holes form a padded
nine-turn block if and only if

\[
 |L_0\cap L_1\cap L_2|=n-4,
 \qquad
 L_i\cap L_j=L_0\cap L_1\cap L_2                  \tag{1.2}
\]

for every `i!=j`, and the upper holes are exactly

\[
                    \{L_0\cup L_1,L_0\cup L_2,L_1\cup L_2\}.       \tag{1.3}
\]

#### Proof

Equation (1.1) immediately implies (1.2)--(1.3).  Conversely put
`H=L_0 intersect L_1 intersect L_2` and `Q_i=L_i minus H`.  Every lower
hole has rank `n-1`, so every `Q_i` has size three.  The pairwise intersection
equalities say that the three `Q_i` are disjoint.  Equation (1.3) is then
exactly (1.1). \(\square\)

Thus the candidate block hypergraph is canonical: enumerate triples of
lower defects satisfying (1.2), and retain the triple precisely when all
three pairwise unions lie in the upper defect set.  No knowledge of the
switch catalogue is required for this test.

### Corollary 1.2 (first block-Hall checks)

A complete decomposition into padded packets requires:

1. equal defect cardinality divisible by three;
2. every lower and upper hole to lie in some candidate block; and
3. a matching of size one third of the defect in the six-uniform block
   hypergraph, where blocks conflict on either shore.

Failure of item 2 is already a singleton Hall obstruction.  Item 3 is the
exact global block-packing condition.

## 2. Complete `ML(9)` census

The full labelled MMM auxiliary multigraph at `n=4` has two Hamilton
gluing-tree endpoints.  Their turn defects have size three on each shore.
Exactly one endpoint has one candidate block, namely

\[
 (73,146,292)\longleftrightarrow(219,365,438).       \tag{2.1}
\]

The other endpoint has upper holes `(221,365,438)`, so the pairwise-union
condition fails.  Hence the positive base is genuine but is already a choice
inside the MMM gluing family, not a formal property of every gluing tree.

## 3. Complete `ML(11)` census

At `n=5` the full labelled auxiliary multigraph has 13 gluing labels on six
plane-tree components.  Exhausting its labelled spanning trees and retaining
the literal physical Hamilton outcomes gives 112 endpoints.  Every endpoint
has 22 lower and 22 upper turn holes.

The exact distribution by candidate-block count is:

```text
blocks       9 10 11 12 13 14 15 16 17 18 19
endpoints    1  3  5  9 20 23 10 22  9  1  9
```

Only six of the nine endpoints with 19 candidates contain seven disjoint
blocks.  Each has a unique seven-block packing.  The six residual pairs are

```text
(594,1451)  three times,
(658,1387)  three times.
```

Neither lower mask is contained in its paired upper mask:

```text
594 & ~1451 = 592,
658 & ~1387 = 656.
```

### Theorem 3.1 (`ML(11)` block-basis failure)

No labelled MMM gluing-tree Hamilton endpoint on `ML(11)` has its complete
turn defect expressible as padded nine-turn blocks plus at most one padded
unit macro.

#### Proof

Twenty-two is not divisible by three, so a representation by full blocks
alone is impossible.  A representation by seven blocks and one unit macro
would give a seven-block packing whose residual pair is nested.  The complete
112-endpoint census above finds only six seven-block packings, and every
residual pair is explicitly nonnested.  Proposition 5.3 of the translated-
packet theorem requires nesting for a padded unit macro. \(\square\)

This is the first dimension after the positive `ML(9)` base.  In particular,
allowing a different or nonstandard labelled MMM gluing tree does not repair
the mismatch.

## 4. `ML(13)` and the one-glue neighbourhood

At `n=6`, take the lexicographically first potential-decreasing MMM label at
every nonstar component.  Its physical Hamilton endpoint has 117 holes per
shore and 274 candidate blocks.  The intrinsic isolated holes are

```text
lower: 713
upper: 4843,5483.
```

Therefore an exact 39-block decomposition is impossible.  A deterministic
exact branch-and-bound over the block hypergraph also rules out 38 disjoint
blocks (12,465 decision states), so this fixture leaves at least six holes
per shore.

Now replace one of the 13 canonical labels by one of the other 27 labels,
retaining only selections which are auxiliary spanning trees and literal
physical Hamilton factors.  There are exactly 56 distinct endpoints.  Every
one has at least one lower and one upper hole in no candidate block.  The
best exchange is label `25 -> 17`; it has 275 candidate blocks and isolated
holes

```text
lower: 713
upper: 4843.
```

Although `713 subset 4843`, exact branch-and-bound still rules out 38
disjoint full blocks (18,378 decision states).  Thus one unit macro plus 38
full blocks is unavailable in this best one-glue fixture as well.

These are finite statements about the specified MMM catalogue.  They do not
exclude a different middle-level factor, two or more nonstandard glues, a
richer alternating-circuit packet, or a stateful recursion whose debt is
created in block-normal form.

## 5. Consequence for the general construction

The new local atom solves the **actuation** problem but not the **debt-shape**
problem.  The exact regenerative interface must now export one of the
following stronger states.

1. A bounded list of three-partition blocks plus a bounded residual debt in
   a separately guarded finite gadget basis.
2. An arbitrary bounded defect bank together with the unit-macro containment
   Hall graph and a mechanism which combines units without losing the
   matching-floor invariant.
3. A recursion which creates its palette debt directly as reserved private
   blocks, rather than repairing the stateless MMM endpoint after the fact.

The `ML(11)` result favours option 1: seven packets remove 21 of 22 defects
on each shore, so only a one-pair residual **shape** is missing.  The fact
that this residual is nonnested proves that the additional gadget cannot be
only Proposition 5.3's padded unit switch.

What remains open asymptotically is whether the block hypergraph of the
standard recursion always has a packing leaving `O(1)` holes.  The present
census refutes exact closure and the one-unit extension, but does not refute
bounded regeneration.

## 6. Reproducibility and scope

The independent audit is

```text
scratch/audit_standard_mmm_q9_block_match_ml11_20260731.py
```

It reconstructs the physical MMM base factor and every labelled gluing tree
from the defining Dyck-word formulas, recomputes both turn palettes, applies
Lemma 1.1 literally, and performs the stated finite packing searches without
a SAT solver.  Its JSON output is

```text
scratch/standard_mmm_q9_block_match_ml11_20260731.audit.json.
```

The exhaustive quantifier is the full labelled MMM gluing-tree family at
`n=4,5` and the complete one-label tree neighbourhood of the canonical
`n=6` endpoint.  No assertion is made about every Middle Levels factor or
about an unrestricted multi-circuit rethread.
