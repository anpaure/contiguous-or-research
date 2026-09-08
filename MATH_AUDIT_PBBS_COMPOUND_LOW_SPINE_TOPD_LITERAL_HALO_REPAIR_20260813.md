# Audit of the compound-low-spine named top-`d` halo repair

**Date:** 2026-08-13  
**Audited source:**
`MATH_COROLLARY_PBBS_COMPOUND_LOW_SPINE_TOPD_LITERAL_HALO_REPAIR_20260813.md`  
**Audited SHA-256:**
`b10ff95ed0b1ae89a78ab2283363b9f639e1fdb98937d3f9dacdf99cd53071d7`  
**Verdict:** **PASS at the named-crossing-casualty scope.**  The original
source SHA `81d05ccc8dc2aa80e3f52cff6b1118b34edb8f1d53438b5ff5c4b6f3a58d6284`
overclaimed preservation of the complete old top-`d` compiler and called
the paired owner path a source upper witness before imposing residence.
Those scopes are corrected in the audited source.

## 1. Task profile

Let `p=d-3`.  A selected correct-rank depth-`q` occurrence is a block of
`q+1` owners and has `q` internal owner edges.  For one deleted edge there
are at most `q` cyclic starts whose block crosses it.  Therefore the union
bound

\[
                  |\mathcal D_q|\le pq\le dq
\]

is valid, including repeated target values.  Summing gives `O(d^3)` named
occurrences.  The clean-halo theorem is formulated for a multiset, so no
distinct-value assumption is hidden here.  Depth one is restored by the
two palette half-edges and is correctly excluded from the halo bank.

The scope phrase “correct-rank” is load-bearing.  The repair theorem applies
to the canonical occurrences of target rank `R-q`; it makes no claim that
an arbitrary owner interval crossing a cut has that rank.

## 2. Selection order and path forest

The fixed seam owners and facets, including all `z_h`, form an `O(d)`
endpoint path forest.  Choose the `O(d)` depth-two halo packages first,
avoiding this bank.  They use `O(d^2)=O(R)` resources and have exposure
`O(d)`.

At one fixed compound endpoint there are at most `O(d)=o(R)` forbidden
incident resources from that bank, so a fresh first whisker event exists.
After that event the clean-arm lemma sees only `O(R)` forbidden resources
in its signature layer.  Hence all long compound bridges can be routed
after the depth-two halos.  Their union is the disjoint union of one
compound path and the halo paths, not one asserted path; this is exactly a
path forest and is sufficient for the ordered halo and protected-factor
theorems.

The resulting intermediate base has size `O(dR)` and exposure `O(d)`, as
required.  Central packages of depths at least three and their arms then
pack by the frozen ordered-halo theorem.

## 3. Orientation and literal rows

For one intersection halo, the forward protected identity is

\[
             \bigcup_{h=q}^{d}P_{i+h}=S.
\]

The clean-halo theorem proves the reflected identity in the reverse owner
orientation.  Thus no global cycle-orientation compatibility is needed for
the halo paths.  The compound path retains its own declared orientation;
all halo identities survive whichever orientation that component induces.

The paired first shore has a consecutive owner path with owner union
`Z=[2R-1]\setminus S`.  This is an unconditional protected owner-path
upper witness.  If the completed factor is `d`-resident, then

\[
 \bigcup_{j=t}^{t+q-1}T_j
   =\bigcup_{p=t}^{t+q+d-1}P_p=Z,
\]

so it becomes a literal source-interval upper witness under the same
residence premise as the lower source cell.

## 4. Exact remaining scope

The polynomial protected-factor theorem is prospective.  It contains the
compound path and every named clean halo, but it need not retain old PBBS
edges or canonical occurrences which do not cross a deleted edge.
Consequently the proved conclusion is:

> every named correct-rank crossing casualty has a protected literal halo,
> and every paired complement has a protected owner-path witness.

It is **not** yet a complete top-`d` compiler theorem for the new factor.
That stronger conclusion needs a relative PBBS rethread or a new global fan
theorem, in addition to resident completion.  Deep targets, arbitrary upper
targets, fusion/opening, and the typed terminal interface remain outside
this corollary.

