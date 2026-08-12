# Self-audit: mixed-screen two-fan ambient antecedent

**Date:** 2026-08-04  
**Method:** symbolic proof audit only; no computation, search, or solver  
**Verdict:** `RETRACTED / DO NOT CITE`.  Independent review found that the
`Cd/Ic` values are not the actual aligned `a/b` birail targets and that the
first native-overlap proof needs an additional core pin in the `d=2` case.
The corrected construction is being rebased on `Ibc/Ica`.

## 1. Binary-dilation audit

For one positive owner run `[alpha,beta]`, a source occurrence at `p`
affects `[p-d,p]`.  Exact support inside the run is therefore equivalent to
`p in [alpha+d,beta]`.  The first and last positions are forced, and gaps
at most `d+1` are necessary and sufficient.  Lemma 1.1 is exact.

The run criterion alone does not force nonempty source letters.  Here the
fixed nonempty packet core `K` belongs to every owner and screen, hence to
every internal maximal-erosion envelope.  All displayed ray/native
addresses are internal.  The nonempty-letter row is therefore separately
satisfied rather than inferred from residence.

## 2. Local owner traces

At `Cd` the adjacent screen types are lower/upper.  Their active parts are
respectively `{e,c}` and `{e,c,d,infinity}` in both phases.  Hence
`K,e,c` cross both screens, while `d` begins its positive run at the block.

At `Ic` the adjacent screen types are upper/lower, with active parts
`{e,c,d,infinity}` and `{infinity,c}`.  Hence `K,infinity,c` cross both
screens, while `e` ends its positive run at the block.

The proposed common-core and pivot pins lie in the eroded positive runs.
The two blocks begin `d+3` owner positions apart.  Shared-core pin gaps are
at most `d`, and each internal filler has consecutive forced occurrences
between its two block zeros.  Thus the two pin systems coexist.

## 3. Ray-value audit

For `1<=i<=d`, a zero at owner `i` forces filler occurrences at relative
positions `i-1` and `i+d+1` and forbids positions `i,...,i+d`.

- `[j,d-1]` therefore contains exactly fillers `f_(j+1),...,f_d`.
- `[d+2,d+j+1]` contains exactly fillers `f_1,...,f_j`.

The stable-core pins lie at `d-1,d+1,d+2`; the middle pin is outside both
ray banks and ensures every native overlap contains the stable core even at
`d=2`.
The `Cd` pivot lies only on the right ray; the `Ic` pivot lies only on the
left ray.  The guard traces force their block-side occurrences at `d` and
`d+1`; the sparse next occurrences may be placed at `2d+2`.  Hence guards
and nonblock active coordinates are excluded.  The four displayed ray
identities follow exactly.

## 4. Native-diamond audit

Owner and q1-union identities are tautological unions of depth-`d` source
windows.  For the overlap `p_i`, the forced filler positions supply every
filler except `f_i,f_(i+1)`.  Direct interval containment shows that each
stable-core pin pair and each of the two pivot pin pairs meets every
`p_i`.  Nothing outside the block can occur in any block owner window.
Thus `OR(p_i)=O_i intersect O_(i+1)`.

Address families have different lengths (`<d`, `d`, `d+1`, `d+2`) inside
one block, and the two block starts differ.  The resulting `2(d-1)` records
are occurrence-distinct.

## 5. Scope exclusions

The proof does not infer polarized cap acceptance from Boolean containment,
does not infer a background matching from disjoint local records, does not
construct the global Hamilton carrier, and does not prove a recursive
whole-host regeneration theorem.  These remain named premises, so the
local theorem makes no all-`k` upper-bound claim.
