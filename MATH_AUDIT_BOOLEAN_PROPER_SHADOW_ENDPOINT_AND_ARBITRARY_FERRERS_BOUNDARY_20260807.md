# Audit of the proper-shadow endpoint theorem and arbitrary Ferrers deletion

**Date:** 2026-08-07  
**Audited source:**  
MATH_THEOREM_BOOLEAN_PROPER_SHADOW_ENDPOINT_AND_ARBITRARY_FERRERS_BOUNDARY_20260807.md

**Verdict:** PASS.  The colex recursion, endpoint induction, affine
proper-shadow inequality, and Hall complement argument are exact.  Every
boundary deletion of the optimal scalar size is capacity-safe.  The result
has no nested-chain or literal-compiler content.

## 1. Colex recursion

Let \(D_{n,r}(q)\) be the minimum number of proper subsets, including the
empty set, below \(q\) rank-\(r\) sets.  Kruskal--Katona permits the
minimizing family to be the initial colex segment.

Write

\[
 q=\binom ar+q',
\qquad
 0\le q'\le\binom a{r-1}.
\tag{1.1}
\]

The first \(\binom ar\) colex sets are all rank-\(r\) subsets of
\([a]\).  Every remaining set contains \(a+1\), and deletion of \(a+1\)
gives the initial rank-\((r-1)\) colex family of size \(q'\) on \([a]\).
The proper subsets split disjointly according as they omit or contain
\(a+1\).  Therefore

\[
 D_{n,r}(q)
 =\sum_{s=0}^{r-1}\binom as+D_{a,r-1}(q').
\tag{1.2}
\]

This includes the cases \(q'=0\) and
\(q'=\binom a{r-1}\), so adjacent Pascal blocks meet correctly.

## 2. Endpoint induction

Fix \(\lambda\ge0\).  Induction on \(r\), applied to the second term of
(1.2), shows that the minimum inside each Pascal block occurs at one of
its two endpoints.  The remaining candidates are

\[
 G_r(a)=\sum_{s=0}^{r-1}\binom as-\lambda\binom ar,
\qquad r\le a\le n.
\tag{2.1}
\]

Pascal's identity gives

\[
 G_r(a+1)-G_r(a)
 =\sum_{s=0}^{r-2}\binom as-\lambda\binom a{r-1}.
\tag{2.2}
\]

After division by \(\binom a{r-1}\), every summand

\[
 \frac{\binom as}{\binom a{r-1}},
\qquad s<r-1,
\tag{2.3}
\]

decreases with \(a\).  Hence the differences in (2.2) change sign at most
once, from nonnegative to nonpositive.  The breakpoint sequence first
increases and then decreases, so its minimum is attained at \(a=r\) or
\(a=n\).

These endpoints are respectively

\[
 2^r-1-\lambda,
\qquad
 \sum_{s=0}^{r-1}\binom ns-\lambda\binom nr.
\tag{2.4}
\]

The base case \(r=1\) is immediate because \(D_{n,1}(q)=1\) for
\(q>0\).  Thus Theorem 2.1 passes.

## 3. Proper-shadow affine surplus

Return to the Boolean lower ideal

\[
 \mathcal L=\{S:1\le |S|<r\},
\qquad
 \Lambda=|\mathcal L|,
\qquad
 h=\Lambda-dW>0.
\tag{3.1}
\]

Removing the common empty set from (2.4), with \(\lambda=d\), gives the
two endpoint values

\[
 2^r-2-d,
\qquad
 \Lambda-dW=h.
\tag{3.2}
\]

The optimal residue bound and \(d\le r-1\) give

\[
 h\le\binom{d+1}{2}
 \le2^r-2-d.
\tag{3.3}
\]

For the second inequality, the worst case is \(d=r-1\), where it becomes

\[
 \binom r2\le2^r-r-1.
\tag{3.4}
\]

Consequently every nonempty owner family \(Q\) satisfies

\[
 |\partial_{<r}Q|-d|Q|\ge h.
\tag{3.5}
\]

The full owner shore attains equality.

## 4. Arbitrary deletion and Hall

Let \(\mathcal B\subseteq\mathcal L\) be any \(h\)-set, and match the
residual targets to \(d\) labelled copies of each rank-\(r\) owner.
Both shores have size

\[
 \Lambda-h=dW.
\tag{4.1}
\]

For a residual family \(\mathcal F\), let \(U\) be its unlabelled owner
neighbourhood.  If \(U\) is the full owner shore, then
\(|\mathcal F|\le dW=d|U|\).  Otherwise put \(Q=\mathcal O\setminus U\).
No member of \(\mathcal F\) lies in the lower shadow of \(Q\), so

\[
 \begin{aligned}
 |\mathcal F|
 &\le\Lambda-|\partial_{<r}Q|\\
 &\le\Lambda-(d|Q|+h)\\
 &=d(W-|Q|)=d|U|.
 \end{aligned}
\tag{4.2}
\]

This is Hall's condition, and integrality is ordinary bipartite matching
integrality.  Theorem 4.1 passes for an entirely arbitrary boundary
family, not merely one having the Ferrers rank profile.

It follows that every \(dW\)-subset of \(\mathcal L\) is a transversal
basis.  Every smaller set extends to one, so the capacity transversal
matroid is exactly \(U_{dW,\Lambda}\).

## 5. Scope

The Hamilton-first extraction may therefore choose its distinct
rank-profiled boundary targets inside the selected clean-packet bottoms
without reopening ordinary capacity Hall.  This genuinely closes the
capacity-only Hamilton--Ferrers intersection.

It does not say that several targets matched to one owner are comparable,
that the owner fibres form strict chains, or that those chains occur as
short intervals in one word.  The sharp flag-configuration matching,
common compiler, resident source chronology, and deeper-upper deck remain
separate.
