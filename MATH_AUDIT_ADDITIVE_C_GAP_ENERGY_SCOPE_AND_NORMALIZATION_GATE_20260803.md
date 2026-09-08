# Audit: additive-constant gap energy and the normalization gate

**Date:** 2026-08-03  
**Verdict:** **GO**, after the small proof-safety edits recorded below.  
**Scope:** pure mathematical audit; no computation or finite search.

Audited source:

`MATH_THEOREM_ADDITIVE_C_GAP_ENERGY_SCOPE_AND_NORMALIZATION_GATE_20260803.md`

## 1. Exact replacement of `d` by `e=d+C`

The one-run proof depends only on the chosen erosion depth.  With
`E=e+1`, a run of owner length `L` has marker span `L-E`; for a marker
gap `g<=E`,

\[
 \sum_{q=1}^{e}(g-q)_+=\binom g2.
\]

Therefore

\[
 \sum_{q=1}^{e}H_q(L)
 =e\left(L-\frac E2\right)-\sum_g\binom g2
\]

is exact.  Summing over separated run hulls gives

\[
 U=e\left(L_{\rm tot}-\frac{RE}{2}\right),\qquad
 G=P-R,\qquad S=L_{\rm tot}-RE,
\]

and Cauchy gives

\[
 J\ge\frac12\left(\frac{S^2}{P-R}-S\right).
\]

The `S=0` case was made explicit in the theorem: then `P=R` and `J=0`,
so no zero denominator is used.  No cyclic or Johnson hypothesis is used
in this local calculation.  The noncyclic extension is consequently
valid under the stated separated-hull and signature-domination
hypotheses.

For a complete resident cyclic carrier,
`L_tot=rW`, `R=W`, and the linear cut adds exactly at most
`binom(E,2)` short boundary cells.  Thus the finite inversion

\[
 P\ge W+\frac{S_e^2}{S_e+2K_e}
\]

is the original theorem with `d` replaced by `e`, with no hidden use of
minimality of `d`.

## 2. Density constant and sparse rails

For fixed `C`,

\[
 \frac{e^2}{k}\to\frac\pi8,qquad
 \frac{eW-\Lambda}{W}=\epsilon_k+C,qquad
 \frac{S_e}{kW}=\frac12+o(1),
\]

and the parity ledger gives

\[
 \frac{K_e}{kW}
 =\frac{4-\pi}{16}+\frac{\epsilon_k+C}{2}+o(1).
\]

Inverting and dividing by `rW`, using `r/k->1/2`, yields exactly

\[
 \frac{P}{rW}\ge
 \frac4{8-\pi+8(\epsilon_k+C)}-o(1).
\]

Minimality of `d` gives the exact bounds

\[
 -\frac{\binom{d+1}{2}}W\le\epsilon_k
 <1-\frac{\binom d2}W,
\]

so monotonicity of the displayed density function gives the uniform
constant `4/(16-pi+8C)`.

Replacing `d` by `e` in the exact/canonical rail census gives

\[
 \frac{P}{rW}\le\frac he(1+o(1)).
\]

Hence bounded defect forces `h=Omega_C(e)=Omega(d)`, and every fixed
number of sparse rails fails for every fixed `C`.  This implication is
correct only on the stated resident erosion-factor face, as the theorem
emphasizes.

## 3. Full erosion tail

Full depth-`e` erosion has cyclic cell ranks at least `r-e`.  Granting
all `binom(E,2)` boundary cells arbitrary values therefore still omits

\[
 \left[\sum_{s=1}^{r-e-1}\binom ks-\binom E2\right]_+.
\]

Since `e/sqrt(k)->sqrt(pi/8)`, the standardized cutoff tends to
`-sqrt(pi/2)`.  Also `Lambda/2^k->1/2` and the polynomial boundary is
negligible.  Dividing by `Lambda` gives

\[
 2\Phi(-\sqrt{\pi/2})=0.210\ldots .
\]

Thus the Gaussian-tail claim and its normalization are correct.

## 4. Add-one-letter counterexample and scope

If `A` is a flat depth-`d` factor with owner row `T=D^dA`, appending any
nonempty letter preserves universality.  For the first `W-1` entries of
the new depth-`d+1` row,

\[
 D^{d+1}A^+=DT,
\]

and adjacent distinct rank-`r` Johnson owners have union rank `r+1`.
Thus the appended word itself is not a flat rank-`r` depth-`d+1` factor.
This correctly refutes only the naive automatic normalization; it does
not refute a different extraction or transformation theorem.

The theorem therefore does **not** prove an architecture-free statement
about every universal word of length `B(k)+C`.  Its extension to all such
words still requires the explicitly stated resident-row normalization
theorem.  This caveat is essential and is correctly retained.

## 5. Edits and lineage

The audit made four proof-safety edits:

1. stated the degenerate `S=0` convention;
2. replaced `epsilon_k<1+o(1)` by its exact minimality bounds;
3. wrote the Gaussian-tail ratio to `Lambda` explicitly and corrected a
   stale equation reference;
4. scoped the append-one-letter identity to its first `W-1` entries.

The malformed and strictly weaker draft
`MATH_THEOREM_FIXED_ADDITIVE_SLACK_FLAT_CARRIER_DENSITY_BARRIER_20260803.md`
was fully subsumed and had no repository citations, so it was removed.

## Final proof-safe conclusion

\[
\boxed{
\begin{array}{c}
\text{Fixed additive slack does not remove the positive-density or}\
\text{full-erosion barriers on the resident fixed-depth carrier face;}\\
\text{promoting this to arbitrary }B(k)+C\text{ words remains an open}\
\text{normalization theorem.}
\end{array}}
\]

