# Self-audit: compact two-step family global compensation

**Date:** 2026-08-05  
**Method:** independent line-by-line symbolic audit; no computation, search,
or solver  
**Verdict:** PASS within the stated family and asymptotic scope.

## 1. Bellman normalization

Dividing the displayed table by `lambda_H` gives rewards

\[
 0\ (j<H),\qquad H,\qquad H+1,qquad 2H.
\]

Every plateau generator `H+1+s` is equivalent, for value and capacity,
to one `H+1` generator plus `s` zero-value units.  Therefore exact-fill
defect is distance down to `<H,H+1>`.  The normal form

\[
                         pH+b,\qquad0\le b\le p
\]

gives distance `(r-q)_+` at `m=qH+r`.  This checks Theorem 1.1.

## 2. Shoulder indexing

The defect is nonzero exactly on `q<r<H`.  Setting `s=r-q` gives

\[
 0\le q\le H-2,
 \qquad
 1\le s\le H-q-1,
\]

and

\[
 V_{qH+r}=q(H+1)\lambda_H=qL'_H,
 \qquad
 U_{qH+r}=qL'_H+s\lambda_H.
\]

Hence the triangular formula includes every changed index once and only
once.

## 3. Limit and domination

For fixed `q`, `s/H` is the Riemann coordinate, while

\[
 s\lambda_H=(s/H)L_H,
 \qquad
 L_H,L'_H\to\zeta.
\]

The missing final interval caused by the upper limit `H-q-1` has length
`O(q/H)` for fixed `q` and vanishes.  For large `q`, both row arguments
are at least `q zeta/2`; on the outer branch `|K(x)|=exp(-(A+x)^2)`.
The displayed Gaussian majorant is summable and independent of `H` after
discarding finitely many small `H`.  Dominated convergence is therefore
legitimate.

The second term in the limiting row sum tiles `[0,infinity)`:

\[
 \sum_{q\ge0}\int_0^1K((q+x)\zeta),dx
 ={1\over\zeta}\int_0^\infty K(u),du.
\]

The signed-tail identity gives this integral as `E X-E Y=E(A-R)=0`.
Thus the limit is exactly the arithmetic comb `C(zeta)`, not merely a
positive lower bound.

## 4. Scope audit

The proof establishes eventual positivity in the one explicit table
family.  It does not provide an effective threshold in `H`, classify all
compact Bellman tables, or show that every adverse layer has a literal
partner.  The theorem correctly retains those exclusions.
