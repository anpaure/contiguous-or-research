# Independent audit: rank-separated named-target equitable matroid intersection

**Date:** 2026-08-03  
**Audited theorem:**
MATH_THEOREM_RANK_SEPARATED_NAMED_TARGET_EQUITABLE_MATROID_INTERSECTION_20260803.md  
**Method:** independent line-by-line matroid and counting audit. No
computation or finite search is used.

## 0. Verdict

**GO after proof-safe clarifications.**

The Boolean containment rank bound, truncated-matroid fractional vector,
dummy-layer construction, partition-capacity argument, and Edmonds
intersection saturation are all correct. In particular, equality at total
rank forces every real rank component to attain its prescribed size; this
is not merely aggregate saturation.

The theorem was patched only to spell out the two separate truncation
inequalities, omit the dummy token when it does not exist, and verify every
subset inequality and total rank of the owner partition matroid.

The scope is exact: the result assigns distinct named targets at each rank
to containing owners with equitable total loads, but does not make the
different-rank targets at one owner nested.

## 1. Containment transversal rank audit

Fix \(s<r\). In the containment graph, every rank-\(r\) owner has
\(\binom rs\) rank-\(s\) neighbours, and every rank-\(s\) target belongs
to \(\binom{k-s}{r-s}\) owners. Therefore, for any owner family \(X\),
\[
 \binom rs|X|
 \le\binom{k-s}{r-s}|\partial_sX|.
\]
The identity
\[
 \binom rs\binom kr
 =\binom ks\binom{k-s}{r-s}
\]
gives
\[
 |\partial_sX|\ge p_s|X|,
 \qquad
 p_s=\frac{\binom ks}{W}.
\]

The standard rank formula for the transversal matroid on the owner shore is
\[
 r_{M_s}(A)
 =\min_{X\subseteq A}\bigl(|A-X|+|\partial_sX|\bigr).
\]
If \(p_s\le1\), every term is at least
\[
 |A|-(1-p_s)|X|\ge p_s|A|.
\]
If \(p_s>1\), the shadow bound gives
\(|\partial_sX|\ge|X|\), so every term is at least \(|A|\); the choice
\(X=\varnothing\) gives equality. Hence
\[
 r_{M_s}(A)\ge\min\{1,p_s\}|A|.
\]

This verifies Lemma 1.1's rank estimate.

## 2. Truncation-polytope audit

The demand assumption gives
\[
 \frac{n_s}{W}\le
 \min\left\{1,\frac{\binom ks}{W}\right\}
 =\min\{1,p_s\}.
\]
Thus, for every \(A\subseteq\mathcal O\),
\[
 x^s(A)=\frac{n_s}{W}|A|\le r_{M_s}(A).
\]
Separately, \(|A|\le W\) gives
\[
 x^s(A)\le n_s.
\]
The rank function of the rank-\(n_s\) truncation is
\[
 r_{M_s'}(A)=\min\{r_{M_s}(A),n_s\},
\]
so \(x^s(A)\le r_{M_s'}(A)\) for every \(A\). Nonnegativity completes the
independence-polytope description. Moreover
\(x^s(\mathcal O)=n_s\), so the vector lies on the base face of the
truncation.

## 3. Dummy layer and partition matroid audit

Write \(N=qW+h\), \(0\le h<W\).

If \(h=0\), then \(c=q\), \(D=0\), and no dummy elements are present. If
\(h>0\), then \(c=q+1\) and
\[
 D=cW-N=W-h,
\]
so \(1\le D<W\). The constant dummy vector \(D/W\) belongs to the
independence polytope of \(U_{D,W}\): for any dummy subset \(A\),
\[
 \frac DW|A|\le |A|,
 \qquad
 \frac DW|A|\le D.
\]

At each owner, the total fractional load is
\[
 \sum_s\frac{n_s}{W}+\frac DW=c.
\]
Every token weight lies in \([0,1]\). Hence every subset of an owner part
has weight at most both its cardinality and \(c\), exactly the partition-
matroid rank inequalities.

If there are \(t\) real rank components, \(N\le tW\) implies
\(c=\lceil N/W\rceil\le t\). Thus every owner part contains at least \(c\)
available ground elements (and one additional dummy token when \(h>0\)),
so the owner partition matroid has total rank exactly \(cW\).

The direct sum of the real truncations and the optional dummy matroid also
has total rank
\[
 \sum_sn_s+D=N+D=cW.
\]

## 4. Edmonds-intersection saturation audit

The fractional vector belongs to both matroid independence polytopes and
has total weight \(cW\). Edmonds' two-matroid intersection theorem says
their intersection is the convex hull of common independent sets.
Therefore a common integral independent set has cardinality at least
\(cW\).

Neither matroid has rank above \(cW\), so the integral set has cardinality
exactly \(cW\).

For the owner partition matroid, \(W\) parts each have capacity \(c\).
Total equality forces every owner part to contain exactly \(c\) selected
tokens.

For the direct sum,
\[
 |I|=\sum_s|I_s|+|I_\star|
 \le\sum_sn_s+D=cW.
\]
Equality of the sum with the sum of component ranks forces
\[
 |I_s|=n_s\quad\text{for every real rank }s,
 \qquad
 |I_\star|=D.
\]
Thus every prescribed rank component is saturated individually.

An integral dummy independent set uses \(D\) distinct owner tokens.
Those \(D=W-h\) owners have \(c-1=q\) real tokens; the remaining \(h\)
owners have \(c=q+1\) real tokens. This is exactly the claimed equitable
histogram.

Finally, independence of \(I_s\) in the original transversal matroid gives
an injection from its \(n_s\) selected owners to \(n_s\) distinct contained
rank-\(s\) targets. Taking the unused targets as the boundary proves the
adaptive-boundary statement.

## 5. Scope audit

The direct sum deliberately treats the ranks independently. It enforces
one target per owner/rank port and balances the number of occupied ports,
but it has no constraint of the form
\[
 \phi_s(T)\subset\phi_t(T)\qquad(s<t).
\]
It also does not impose the nonadjacent residual-rank pattern law.

Therefore it cannot be cited as a named flag factor, Ferrers chronology,
upper carrier, common-cap construction, or all-\(k\) upper bound. The
theorem's final section states exactly this boundary.

## 6. Proof-safe conclusion

The verified implication is
\[
\boxed{
\begin{array}{c}
\text{rank-separated Boolean containment demands}\\
\Downarrow\\
\text{exact named-target injections and equitable owner loads}.
\end{array}}
\]
The unproved next implication is the correlated ownerwise flag
intersection with the nonadjacent rank patterns.
