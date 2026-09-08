# Self-audit: positive-density typed wedge baseline stability

**Date:** 2026-08-04  
**Method:** exact counting replay; no computation or search  
**Target:**
`MATH_THEOREM_POSITIVE_DENSITY_TYPED_WEDGE_BASELINE_STABILITY_20260804.md`  
**Target SHA-256:**
`52bed2d46dee3ceab88193da699745822eb11d4841d8d7ff45ca052c389f0379`  
**Verdict:** **GO under the stated completion-stable typed-baseline and
dynamic-loss cover.**

## Checks

1. A bad source has dynamic loss at least `M_*-K_p`; summing these losses
   gives the exact casualty quotient in (1.1).  Static wedges outside the
   typed baseline are correctly uncharged.
2. Every baseline wedge carries one distinguished typed owner side.  One
   unavailable side belongs to at most `m-1` full wedges, so owner-side
   deletion loses at most `(m-1)r_i` baseline certificates.  The sharper
   `C(r_i,2)` row is valid only on the separately stated dual-side typed
   face.
3. Summing the owner-star loss gives `(m-1)I`; terminal and hidden dynamic
   sets add at most `J`.  Overlap only improves the bound.
4. For `p=O(sqrt(m))`, the active cycle-alignment threshold is
   `K_p=O(m^(3/2))=o(m^2)`.  A baseline floor `alpha m^2` therefore leaves
   denominator at least `alpha m^2/2` eventually.
5. `I<=Am` and `J<=Dm^2` make the numerator at most
   `(A+D)m^2`, yielding the stated constant
   `floor(2(A+D)/alpha)`.
6. Retaining fewer sources only lowers the active-cycle threshold.  The
   baseline menus already exclude individual conflicts with `P_*`; selected
   lower turns and owner values are globally distinct, so those individual
   degree checks compose.  The scalar protected-factor edge budget remains
   separate and explicit.
7. Completion/orientation-stable typed sides and joint nonendpoint privacy
   are hypotheses.  Prospective algebraic multiplicity before choosing a
   host cannot be substituted for the literal baseline.
8. Owner-area min-cost rounding and q1 propagation control only dynamic
   background loss.  They do not manufacture the positive-density typed
   baseline or prove regeneration.

## Conclusion

The theorem is sound.  Its gain is that the all-k cap route no longer needs
an almost-full typed wedge atlas: any fixed positive-density atlas has
quadratic slack over the `O(m^(3/2))` active-cycle threshold, and aggregate
dynamic loss `O(m^2)` can spoil only constantly many source menus.
