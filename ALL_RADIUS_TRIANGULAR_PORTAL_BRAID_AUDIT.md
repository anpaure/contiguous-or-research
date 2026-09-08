# Independent audit of the all-radius selective triangular braid

## Verdict

**PASS.**  The proposed recursion is a valid unconditional construction.  It
gives

\[
g_\triangle(R)\le \frac78R^2+O(R),\qquad
\rho(R)\le \frac38R^2+O(R).
\]

No hidden fixed-row, canonical-provider, or computational assumption is used.

## Proof audit

The four target classes are exhaustive and each proposed interval has exactly
the required extrema.

1. For `x=0`, two or more consecutive peaks in the alternating peak block
   supply the target and both peak types.
2. For `r=R`, starting at `E_(R,x)` in the decreasing outer arm prevents a
   height larger than `x`; the subsequent peak block supplies `[u,R]` and a
   type-0 peak.
3. For `u=0`, `r<R`, and `x>0`, the lifted diagonal begins
   `P_1,E_(2,1),...,E_(R-1,R-2)`.  Since `x<r`, its prefix through
   `E_(x+1,x)` cannot increase the first-coordinate maximum past `r`.
4. In the remaining case, subtracting one from all three parameters produces
   a valid target at radius `R-2`.  The typed-witness hypotheses give exactly
   heights zero and one when the old height is zero, and give exactly heights
   zero and `x+1` otherwise.  Because the selective lift is letterwise, the
   lifted witness remains contiguous.

Spanning is also complete: the scaffold supplies row `R` and every peak;
interior cells of height at least two are unique lifts of lower nonpeaks; and
every height-one cell is the lift of a type-1 occurrence of the corresponding
positive lower peak.  The construction restores a type-1 occurrence of each
positive peak using odd scaffold peaks and the even supplements.  Hence the
inductive braidability invariant is preserved.

The recurrence is exact (the displayed inequality may be strengthened to an
equality for this constructor):

\[
n_R=n_{R-2}+3R+1+\lfloor R/2\rfloor.
\]

It solves to

\[
n_{2t}=\frac{7t^2+9t+2}{2},\qquad
n_{2t+1}=\frac{7t^2+15t+4}{2}.
\]

Subtracting `|T_R|=1+R(R+1)/2` gives exactly the two claimed excess formulas
and therefore the constants `7/8` and `3/8`.

## Independent computation

[`scratch/verify_all_radius_triangular_portal_braid.py`](scratch/verify_all_radius_triangular_portal_braid.py)
reimplements the recursion and exhaustively checks radii `0..50`.  It checks
the alphabet, exact closed-form length, diagonal prefix, a type-1 occurrence
of every positive peak, every target, and—stronger than the supplied untyped
verifier—the existence for every target of a witness satisfying the typed
inductive conditions.  It passes.

## Scope

This materially improves the local triangular construction, but it does not
by itself improve the currently proved global `sqrt(2)` constant.  The claims
about removing duplicated ladders or supplements are correctly presented as
next targets, not as proved constructions.
