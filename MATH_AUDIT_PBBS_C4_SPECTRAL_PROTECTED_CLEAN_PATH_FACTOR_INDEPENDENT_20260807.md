# Independent audit: the full clean PBBS packet bank extends to a two-factor

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_PBBS_C4_SPECTRAL_PROTECTED_CLEAN_PATH_FACTOR_20260807.md`  
**Verdict:** PASS for the stated spanning-two-factor theorem.  This audit
does not promote the result to a Hamilton cycle, a literal antecedent, a
deep-upper deck, or a lower compiler.

## 1. Exact cut

Let `G` be the `r`-regular middle-levels incidence graph and let
`P subseteq G`.  A two-factor `F` containing `P` is equivalent to an
`(r-2)`-factor `G\F` of `G\P`.  The bipartite factor cut is therefore

\[
 e_G(A,B)+(r-2)(W-|A|-|B|)\ge e_P(A,B)
\]

for every `A subseteq X`, `B subseteq Y`.  Thus equation (2.1) in the
source has the correct sign and coefficient.

For `|A|+|B|>W`, set `S=X\A`, `C=Y\B`,
`q=|A|+|B|-W`, `s=|S|`, and `c=|C|`.  Direct regular-edge counting gives

\[
 e_G(A,B)=rq+e_G(S,C),
\]

so the left side of the cut is exactly `e_G(S,C)+2q`.  After taking
`s<=c`, the smaller protected shore is `B`, of size `q+s`; hence

\[
 e_P(A,B)\le 2\min(q+s,H).
\]

All reductions through (2.6) are exact.

## 2. Elementary regimes

If `q>=H`, the term `2q` alone pays the protected cut.  If `q<H`, put
`t=H-q`.

* For `s<=t`, every vertex of `S` loses at most `q+s<=H` neighbours to
  `B`, so `e_G(S,C)>=s(r-H)>=2s` for large `r`.
* For `s>t` and `q+s<=r-2`, writing `s=t+u` gives

  \[
  e_G(S,C)\ge(t+u)(r-H-u).
  \]

  The quadratic is concave on `0<=u<=r-H-2`; both endpoint values are at
  least `2t`.  Thus its entire interval is at least `2t`.

These cases are complete and leave precisely the source's regime (3.6).

## 3. Quadratic and spectral regimes

The graph is `C4`-free because two distinct rank-`m` sets have at most one
common rank-`m+1` superset.  Consequently

\[
 \sum_y d_y^2\le rs+s(s-1)\le s(r+s).
\]

Cauchy--Schwarz over `B` yields the source's (4.2).  In the remaining
regime `s>= (1-alpha)r-1`; for `s<=kappa r^2`, with
`kappa=(1+alpha)/2`, the displayed ratio is `R<=kappa+o(1)<1`.
The resulting `Omega_alpha(r^2)` lower bound dominates `2t=O(r)`.

For `s>kappa r^2`, the incidence matrix satisfies

\[
 MM^T=rI+A(J(2m+1,m)),
\]

whose second singular value is `r-1`.  Substitution of
`W-s=c+q`, `W-c=s+q` into bipartite expander mixing gives (5.2).
With `x=q/s` and `y=q/c`,

\[
 \sqrt{(1+x)(1+y)}\le1+x+x^2/2,
\]

and `x<=alpha/(kappa r)`.  Hence the bracket in (5.2) is at least
`1-alpha/kappa-o(1)>0`.  Since `c/W>=1/3` eventually, this again gives
`e_G(S,C)=Omega_alpha(r^2)>2t`.

No cut regime is omitted.

## 4. PBBS consequence and exact scope

A resource-disjoint bank of `h` clean packets has maximum degree two and
`4h` protected incidence edges.  Taking `H=2h`,

\[
 H/r\le d(d+1)/(m+1)=\pi/4+o(1)<1.
\]

Thus the theorem applies with any fixed `alpha` strictly between `pi/4`
and one.  The former restriction `4h<=m-1` is genuinely removed for all
sufficiently large parameters.

What is proved is exactly

\[
 \text{resource-disjoint clean packet bank}
 \Longrightarrow
 \text{protected spanning two-factor}.
\]

Connectivity and all literal/compiler decorations remain separate.  In
particular, this result must not be cited as a Hamilton-extension theorem.
