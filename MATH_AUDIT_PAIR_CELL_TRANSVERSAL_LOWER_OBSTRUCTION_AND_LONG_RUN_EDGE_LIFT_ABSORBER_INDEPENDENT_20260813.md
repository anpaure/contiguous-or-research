# Independent audit: pair-cell transversal obstruction and edge lift

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_PAIR_CELL_TRANSVERSAL_LOWER_OBSTRUCTION_AND_LONG_RUN_EDGE_LIFT_ABSORBER_20260813.md`  
**Source SHA-256:**
`7dd84b2dbd830f0a52b772a02467e15b92f5c52cc8f99e3f63a8d0a4dcafb852`  
**Verdict:** **PASS.**  No mathematical flaw was found.  No source edit was made.

## Checks

1. **Inaccessible lower family.**  An internal pair-cell edge flips one
   singleton pair and therefore has an empty pair in its intersection.
   Conversely, if a rank-`p` facet is empty on `P_i`, adjoining either
   endpoint of `P_i` produces the two owners of one internal edge.  If a
   rank-`p` facet has no empty pair, it cannot contain the sentinel and must
   take exactly one endpoint of every pair.  Thus the inaccessible family is
   exactly the `2^p` transversal facets.  Since the whole rank-`p` lower row
   has size `W`, the accessible count `W-2^p` and Corollary 1.2 follow.

2. **Lifted owners and lower row.**  `D_t=L_{x_t}\cup L_{x_{t+1}}` has one
   doubled pair, namely the transition direction.  That doubled pair and
   all remaining singleton choices recover the unoriented cube edge, so
   distinct Hamilton-cycle edges give distinct owners.  Consecutive
   transition directions differ.  Direct pairwise inspection then gives
   `D_{t-1}\cap D_t=L_{x_t}` and one Johnson exchange.  Hence every
   transversal facet occurs exactly once.

3. **One-unit residence loss.**  Between successive direction-`i`
   transitions at edge distance `g`, the newly selected endpoint is present
   in `g+1` consecutive lifted owners, whereas its mate is absent in the
   `g-1` strict interior owners.  The roles reverse at the next gap.  Thus
   input transition separation at least `q+1` gives positive runs at least
   `q+2` and zero runs at least `q`.  Constant absence of the sentinel causes
   no finite short positive or zero run.

4. **Optimality and localization.**  A closed degree-at-most-two bank on
   `n` distinct owners has at most `n` edges, so covering `2^p` distinct
   transversal lower colours needs at least `2^p` owners.  The lift attains
   this.  Every lifted owner has sentinel absent, one prescribed doubled
   pair, and all other pairs singleton, so the affected bank is contained in
   exactly the stated `p` dimension-`p-1` cells.  The theorem correctly
   leaves their complement-factor rethread open.

5. **Upper turns.**  The union at `L_{x_t}` doubles precisely the two
   consecutive transition pairs and fixes every other pair according to
   `x_t`.  It therefore determines, and is determined by, the unordered
   direction pair together with the ambient two-face.  Equality of two upper
   values is exactly repetition of that turn-face datum.  The source makes
   only the resulting conditional simplicity statement and does not claim
   turn-injectivity.

The scope is consequently accurate: this is an exact lower-palette repair
component and localization theorem, not yet a completion of the disrupted
top cells or a globally upper-simple factor.
