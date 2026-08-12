# Algebraic audit: Apéry fundamental-period collapse and one-kink comb reserve

**Date:** 2026-08-05  
**Method:** pure mathematics; independent hand replay of every group,
carry, density, phase-enumeration, and reserve identity; no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_RAYLEIGH_APERY_FUNDAMENTAL_PERIOD_COLLAPSE_AND_ONE_KINK_COMB_RESERVE_20260805.md`  
**Verdict:** **SELF-GO.**  The reduction is exact.  It closes critical-period
boundaries and the full one-kink family, but not primitive multi-kink
profiles or finite shoulders.

## 1. Critical-residue collapse

If `d_a=0`, repeated cyclic subadditivity makes every element of
`<a>` zero.  Since `-a` is in the same subgroup,

\[
 d_{r+a}\le d_r,
 \qquad
 d_r\le d_{r+a}+d_{-a}=d_{r+a}.
\]

Thus equality holds.  The subgroup `<a>` is the multiples of
`g_0=gcd(a,g)`, so the quotient defect is well-defined.  The physical
clock identity is termwise:

\[
 \lambda m-d_{m\bmod g}
 =\lambda m-\widetilde d_{m\bmod g_0}.
\]

There is therefore no factor `g/g_0` in the full infinite functional.
The phase enumeration gives the same conclusion because `(q,k)` maps
bijectively to `n=q(g/g_0)+k`.

## 2. Ordinary superadditivity of the ramp

For `f(r)=(r-h)_+`, take `i+j<=g`.

* If neither index exceeds `h`, the right side is zero.
* If exactly one does, adding the other nonnegative index can only increase
  the positive part.
* If both do, `f(i+j)=i+j-h` while
  `f(i)+f(j)=i+j-2h`.

Hence `f(i+j)>=f(i)+f(j)`.

## 3. Carry superadditivity of the ramp

For `x=i+j>=g`, the required inequality is

\[
 g-h+(x-g-h)_+\ge(i-h)_++(j-h)_+.
\]

If at most one index exceeds `h`, the right side is at most `g-h`.
If both do, it is `x-2h`.  For `x<=g+h`, the left side is `g-h` and the
claim is exactly `x<=g+h`; for `x>=g+h`, the left side also equals
`x-2h`.  Every equality face and the endpoint case are covered.

## 4. Density and primitiveness

For `h<r<=g`,

\[
 {s_r\over r}=\eta{r-h\over r},
 \qquad
 {P\over g}=\eta{g-h\over g}.
\]

Their difference has the sign of `h(g-r)`.  Thus every proper density is
strictly below the endpoint density exactly when `h>0`.  Cyclic
superadditivity then makes the displayed shifts their own exact Apéry
shifts; no unlisted walk can improve them.

## 5. Phase multiset and no off-by-one

The zero phases are `r=0,1,...,h`, exactly `h+1` copies.  The positive
phases are

\[
 \eta,2\eta,\ldots,(q-1)\eta,
\]

exactly `q-1` copies.  Total count is

\[
 (h+1)+(q-1)=h+q=g.
\]

One zero plus the positive phases gives every residue of the `eta`-mesh in
one `P=q eta` period.  Reindexing `n=aq+j` proves

\[
 \sum_{j=0}^{q-1}F_{q\eta}(j\eta)=C(\eta).
\]

The remaining `h` zeros give `hC(P)`, not `(h+1)C(P)`.  Therefore

\[
 \Phi=C(\eta)+hC(P).
\]

The all-mesh theorem applies to both positive meshes and gives the strict
reserve `(h+1)c_*`.

## 6. Boundary calibrations

* `q=1`: `eta=P`, `h=g-1`; all `g` phases are zero and
  `Phi=gC(P)`, agreeing with the endpoint-only theorem.
* `q=g`: `h=0`, phases are the full arithmetic residue grid and
  `Phi=C(P/g)`.  Every defect is zero, so fundamental-period collapse gives
  the same answer.
* `1<q<g`: the endpoint is uniquely maximum-density, so these are genuine
  primitive clocks even though their functional is comb-decomposable.

## 7. Scope

The theorem does not establish that every extreme point of the cyclic
subadditive cone is a ramp.  It does not decompose a sum of kinks, because
`K` is nonlinear and separate positive comb decompositions cannot simply be
added at the level of shifts.  It also does not pair the finite shoulder.
The exact remaining formal class is primitive and multi-kink, as stated.
