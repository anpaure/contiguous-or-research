# Audit of the log-free shared-boundary packing split

Date: 2026-07-25

Theorem 6.1 appended to
`PBBS_SHARED_BOUNDARY_COLLISION_20260725.md` is valid.

Fix \(A>0\), let \(L=L(r)=o(r^{1/5})\), and split a quotient-edge-
disjoint family at duration \(a\sqrt r\), where \(a>0\) is fixed before
letting \(r\to\infty\).

For the lower-duration part, the proved sub-Gaussian packing theorem gives

\[
 \lim_{a\downarrow0}\limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}\,
 \overline\nu_{\le a\sqrt r}=0.
 \tag{1}
\]

For \(s>a\sqrt r\), the family is a subset of the normalized start set.
Moreover

\[
 \frac{L}{s}=o(r^{-3/10}),
\]

so, for every fixed \(a\), the hypotheses \(3\ell<s-2\) and
\(\ell\le c s\) required by the shared-boundary coefficient theorem hold
uniformly for all \(\ell\le L\), once \(r\) is large.  Therefore

\[
 \begin{aligned}
 |\mathcal P(s>a\sqrt r)|
 &\le C4^r
   \sum_{\ell\le L}\frac{(\ell+2)^2}{\sqrt{\ell+1}}
   \sum_{s>a\sqrt r}s^{-6}\\
 &\le C_a4^r\frac{L^{5/2}}{r^{5/2}}.
 \end{aligned}
 \tag{2}
\]

Since

\[
 B_r/\sqrt r\asymp4^r/r^2,
\]

division of (2) by the coefficient-one quotient scale gives

\[
 O_a\!\left(\frac{L^{5/2}}{\sqrt r}\right)=o(1).
 \tag{3}
\]

Thus, for fixed \(a\), the large-duration part is negligible.  Taking
\(r\to\infty\) first and then \(a\downarrow0\) in (1) proves

\[
 |\mathcal P|=o_A(B_r/\sqrt r).
\]

There is no missing spatial-phase factor: the shared-boundary coefficient
counts normalized roots, and the family in Theorem 6.1 is explicitly a
quotient-edge-disjoint family.  The fixed-\(A\) quantifier is also harmless,
since the upper limit \(A\sqrt r\) is discarded when the large-duration
sum is enlarged to infinity.

