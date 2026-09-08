# Independent audit: pair-cell two-adic selector obstruction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PAIR_CELL_TWO_ADIC_SELECTOR_OBSTRUCTION_20260804.md`

## 1. Cell-size and valuation audit

Fixing the zero/one/two occupancy of every physical pair leaves one binary
choice for each singleton pair and no choice for any other pair.  A
dimension-`m` cell therefore has exactly `2^m` owners.

Legendre's formula gives

\[
 \nu_2\binom{2r}{r}
 =2r-s_2(2r)-2r+2s_2(r)=s_2(r),
\]

because binary left shift does not change digit sum.  Therefore a disjoint
union of cells all divisible by `2^M` cannot equal the middle layer when
`M>s_2(r)`.  This argument is independent of the number and geometry of
the pairing frames.

## 2. Fractional-gap audit

For every admissible `m`, at least one dimension-`m` pair cell exists.  The
full symmetric group is transitive on middle owners and preserves the
occurrence-labelled family of such cells, so the owner incidence degree is
a positive constant.  Uniform reciprocal incidence weight is therefore a
fractional exact cover.

An integral exact cover would use `W_r/2^m` cells.  This number is not an
integer for `m>s_2(r)`.  Thus the claimed fractional-integral gap is exact;
it is not merely a failure of one rounding algorithm.

For the `r=2` literal example, each of the six owners lies in exactly two
of the three good square cells.  The three independent owner-row types are
the edge equations of a triangle, whose only real solution is the all-half
vector.  Hence the example is a valid actual pair-cell obstruction even at
the coarse threshold boundary `M=s_2(r)`.  Its nonintegrality is not
independent of cardinality, however: every available cell has size four,
and four does not divide six.  The example proves that the bound stated
only in terms of the minimum threshold `M` is not sufficient, not that an
extra incidence obstruction survives every exact-size congruence.

## 3. Two-frame theorem audit

Every element belongs to one block on each shore, so its exact-cover row is
`x_A+y_B=1`.  On a connected bipartite intersection component these rows
force one constant value on the first shore and its complement on the
second.  Bad blocks on opposite shores force inconsistent values, and this
is the only obstruction.

For pairings, changing the selected endpoint of a singleton pair is a token
move along the corresponding matching edge.  Alternating such moves across
the two matchings gives the exclusion process on `P union Q`.  Token count
in each graph component is invariant, and the token graph of a connected
graph is connected at every fixed token count (the empty and full cases are
singletons).  Hence the stated component classification is correct.

For three partitions, fixing the selected `R`-blocks covers exactly
`U_S`.  Any full `P`- or `Q`-block meeting `U_S` is then unusable, not merely
its intersection with `U_S`; this is why such vertices are marked
forbidden.  Removing `U_S` leaves two honest restricted partitions, so the
two-frame theorem applies with no loss.  Conversely its selected residual
blocks are disjoint from `U_S` by construction.  The deletion-component
criterion is therefore necessary and sufficient.

## 4. Cut-residue audit

Whole good-cell sizes vanish modulo `2^M`, leaving (5.1).  If every proper
block size also had valuation at least `s_2(r)+1`, then the complete owner
count would be divisible by `2^{s_2(r)+1}`, contradicting its exact
valuation `s_2(r)`.  Thus at least one proper selected block must carry the
low two-adic residue.

This does not lower-bound the number of cuts or force selected proper blocks
to have different lengths.  One suitably sized proper block could satisfy
the modular row, and the two-adic valuation condition alone does not
exclude a compatible common block size whose valuation is at most
`s_2(r)`.  Odd-part divisibility and feasible block counts may still rule
out a particular common size.  What (5.2) categorically excludes is a
library in which every block size is divisible by `2^{s_2(r)+1}`.
Geometry, residence, Hall, and holonomy remain separate constraints.

## 5. Corrections required by the audit

The core theorems were sound, but the prose required four proof-scope
corrections, now applied to the theorem note:

* the `r=2` example was retitled as an obstruction at the coarse threshold
  boundary, where `M=s_2(r)`, and its stronger modulo-four explanation was
  made explicit rather than attributing the failure uniquely to incidence;
* the token-component characterization was supplied with the missing
  connectivity argument for fixed-cardinality exclusion configurations;
* the claim that cuts force variable lengths was removed, since the modular
  calculation only forces at least one low-valuation selected block; and
* the switch-tree conclusion was restricted to switch-only operations on a
  fixed edge union at `M>s_2(r)`, where vertex degrees and hence owner
  multiplicities are invariant.

The note also now distinguishes its exact intersection-component theorem
from any separately defined successor-Hall statement.

## 6. Scope verdict

**PASS after the scope corrections recorded in this audit.**  The note
proves:

* whole good cells cannot partition the middle layer once their minimum
  dimension exceeds `s_2(r)`;
* the symmetric all-pairings whole-cell hypergraph can have a fractional
  exact cover while having no integral one;
* the exact two-frame whole-block selector criterion;
* the exact three-frame reduction to a third-shore component separator;
  and
* a necessary modular condition on any cut-block replacement.

It does **not** prove:

* nonexistence of a cut-and-splice resident factor;
* macro Hall or collar holonomy for a proposed path partition;
* a lower bound larger than one on the number of proper blocks;
* that proper blocks must have variable lengths, or that a uniform length
  of valuation at most `s_2(r)` is impossible;
* any upper-palette or compiler statement; or
* `nu(k)=B(k)+O(1)`.

The contextual assertions about a particular syndrome threshold,
three-frame cover theorem, resident-cube theorem, macro Hall theorem, or
collar holonomy are inputs from outside the two audited files.  This audit
checks the deductions made from those stated inputs; it does not certify
the external results themselves.

The proof-safe consequence is that the seam-free exact-cover route is
closed negatively in the asymptotic residence regime.  Within the proposed
pair-cell route, future selector work must use at least one residue-carrying
proper block and must separately establish safe seams; arithmetic alone
does not prescribe the block-length distribution.

A two-edge switch preserves every vertex degree in the fixed edge union,
not just its support.  Accordingly, at `M>s_2(r)`, a switch-only
Hamiltonization cannot start from a spanning vertex-disjoint family of
whole good cells, and switches cannot turn an overlapping or incomplete
fixed family into an owner partition.  This does not obstruct switch trees
after the owner-selection row has been solved using proper blocks, nor a
broader algorithm that changes the selected blocks in addition to
performing switches.
