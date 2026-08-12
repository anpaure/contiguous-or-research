# Independent audit: odd adjacent-depth capacity-`D` absorber

**Date:** 2026-08-05  
**Method:** pure symbolic audit; no computation, search, or solver  
**Audited source:** `MATH_THEOREM_ODD_ADJACENT_DEPTH_CAPACITY_D_ABSORBER_20260805.md`  
**Verdict:** **GO after one proof-strengthening patch.**  The theorem is a
correct conditional odd-dimensional analogue of the adjacent-depth residual
lower theorem.  It does not prove an unconditional word, a boundary bank, or
protected serialization.

## 1. Tail and multiplicity audit

In `B_(2r-1)`, a symmetric chain born at rank `a<=r-1` has multiplicity

\[
 H_a={2r-1\choose a}-{2r-1\choose a-1}
\]

and meets both ranks `r-1` and `r`.  With old bottom `t=r-D`, a chain born
at `t+g` consumes `D-g` lower-collar vertices and has capacity `g`.  Hence

\[
 M_g=H_{t+g}\ (1\le g<D),\qquad
 K_q=\sum_{g=q}^{D-1}H_{t+g}=W-C_{t+q-1},
\]

so `K_D=0`.  After changing the bottom to `b=t-1`, births `b+g`,
`1<=g<=D`, give

\[
 K_q^+=\sum_{g=q}^{D}H_{b+g}=W-C_{b+q-1},
\]

and therefore

\[
 K_q^+-K_q=C_{t+q-1}-C_{t+q-2}=H_{t+q-1}.
\]

At `q=D`, this is the genuine capacity-`D` bank

\[
 H_{r-1}=C_{r-1}-C_{r-2}={2W\over r+1}.
\]

There is no capacity-`D+1` SCD birth.  These indices and multiplicities are
exact.

## 2. Terminal deletion and basic-rounding audit

Because `K_D=0`, every configuration in a feasible old LP has zero
length-`D` tail.  The last aggregate row is therefore identically zero on
the feasible support, so the active aggregate rank is at most `D-1`; an
extreme point leaves at most `D-1` split whole jobs.

Moving the bottom from `t` to `b=t-1` deletes the terminal rank-`t-1`
cell of every old residual job.  The surviving residual ranks are exactly
`1,...,t-2`, and every exceptional descendant can be cut into pieces of
length at most `D`.  Thus capacity `D`, rather than the nonexistent
capacity `D+1`, is sufficient.  The safe count

\[
 h=D\left\lceil {L_{\max}\over D}\right\rceil<r
\]

is valid because `L_max<=r-D-2` (and is zero when no descendant survives).
The conjugate-tail inequalities subtract `h` at every threshold
`q<=D`, exactly as required for `h` reserved capacity-`D` occurrences.

## 3. Named-lift audit

For capacity `g`, the socket start rank is `u_g=b+g`.  A fragment top has
rank at most `b-1`, so its minimum containment degree is attained at rank
`b-1` and equals

\[
 d_g={2r-b\choose g+1}.
\]

The deterministic configuration/capacity marking is made before the
Boolean path geometry is exposed, so it is a permitted cohort refinement
and preserves MLD.  The MLD--Hölder pointwise load theorem is
dimension-general for `u<=floor(n/2)` and applies here for every
`u_g<=r-1`.  Its slack condition is precisely

\[
 {\Delta_g^2d_g\over C_{u_g}H_{u_g}}\ge A_0(2r-1).
\]

At the last start rank, the incidence graph between ranks `r-1` and `r`
of `B_(2r-1)` is `r`-regular with equal shores.  A perfect matching
therefore extends all distinct rank-`r-1` collar occurrences to distinct
rank-`r` owners.  No extra top-rank birth or socket is being assumed.

## 4. Uniform reserve audit

The original corollary had the correct asymptotic conclusion but compressed
the only uniform-in-`q` estimate into the phrase “only improves.”  The
source has been patched to expose the proof.  With

\[
 a_g=r-u_g=D+1-g,
\]

one has uniformly for `D=Theta(sqrt(r))`

\[
 C_{u_g}=\Theta(W),\qquad H_{u_g}=\Theta(a_gW/r),
\qquad d_{g+1}/d_g={r+D-g\over g+2}.
\]

The unrounded reserve size is

\[
 X_g=\Theta\!\left(W\sqrt{a_g/d_g}\right),
\]

successive terms have ratio `O(r^(-1/4))`, and `a_gd_g` is increasing.
Consequently

\[
 {X_q\over H_{u_q}}=O(r^{-1/4}),\qquad
 \sum_{g=q}^{D}\Delta_g=o(H_{u_q})
\]

uniformly in `q`.  Ceiling errors contribute only `O(D)`, negligible
against `H_(r-1)=2W/(r+1)`.  This proves the reserve inequalities; it is
not merely a first-row estimate.

## 5. Exact implication boundary

Taking `D=d(2r-1)` changes physical length from `W+D=B(2r-1)` to
`W+D+1=B(2r-1)+1`.  What has been proved is only:

\[
 \mathrm{FC}^{\rm odd}_D
 +\text{literal priced boundary bank}
 +\text{protected joint serialization}
 \Longrightarrow
 \nu(2r-1)\le B(2r-1)+1.
\]

The source correctly excludes all three invalid upgrades:

1. it does not infer suffix occurrences from abstract SCD occurrences;
2. it does not absorb the separately priced endpoint/Ferrers bank; and
3. it does not claim owner connectivity, residence, arbitrary-width upper
   coverage, or common-cap compatibility.

Accordingly, the odd residual lower absorber itself is proof-safe, while
the all-price configuration inequality and protected serializer remain
the live global gates.
