# Five-slot Bellman clocks reduce to two pulse-free repeated-gap lattices

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that every
five-slot Bellman table outside two explicit pulse-free three-coset families
has strictly positive functional.  It does not prove the two remaining
inequalities and therefore does not prove the all-grid Bellman inequality or
an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 \mathcal L_3(P;u,v)
 =\sum_{q\ge0}\bigl(K(qP)+K(qP+u)+K(qP+v)\bigr).
\tag{0.1}
\]

The two remaining scalar families are

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta)
\tag{0.2}
\]

on

\[
 0\le a\le\beta,
 \qquad
 2a+2\beta<A<2a+3\beta,
\tag{0.3}
\]

and

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\tag{0.4}
\]

on

\[
 0<a<{A\over4},
 \qquad
 \max\{3a,A-2a\}<p<A-a.
\tag{0.5}
\]

The cyclic gap triples are respectively

\[
 (a,\beta,\beta)
 \qquad\hbox{and}\qquad
 (a,a,p-2a).
\tag{0.6}
\]

Thus both gates are pulse-free three-coset trains with two equal gaps; the
singleton gap lies on opposite sides of the repeated gap in the two
families.

## Theorem 1 (complete five-slot reduction)

If

\[
 \mathcal R(a,\beta)>0
 \quad\hbox{throughout (0.3)}
\tag{1.1}
\]

and

\[
 \mathcal P(p,a)>0
 \quad\hbox{throughout (0.5)},
\tag{1.2}
\]

then every nonnegative internally superadditive Bellman table with grid
size at most five and displayed endpoint at least `A` has strictly positive
functional.

Equivalently, any nonpositive five-slot table forces at least one failure of
(1.1) or (1.2).  No finite Ap\'ery head, active threshold face, endpoint
pulse, or other efficiency class remains.

### Proof

Assign a five-slot table to its least maximum-density denomination among
the sizes `2,3,4,5`.  This loses nothing: if size one is maximally efficient,
then internal superadditivity gives `c_2>=2c_1`, so size two is maximally
efficient as well.  The exact maximum-efficiency normal forms therefore
split the table into the four possible sizes `h=2,3,4,5`.  If this rule
assigns `h=5`, then no smaller positive size is a maximizer, so size five is
also the global least maximizer required by the endpoint-normalization
theorem.

1. The complete `h=2` theorem proves that branch strictly positive,
   including its small-period wedge and both finite pulses.
2. Least-critical endpoint normalization forces every genuine `h=5` table
   onto `c_5=A`.  The endpoint-period train theorem then proves that branch
   positive with margin `1/400`.
3. Monotone endpoint normalization splits `h=4` into the active face
   `T=A` and the two inert faces `T=P+x`, `T=y+z`.  The active face is
   positive with margin `199/2310000`.  The complementary-pair reduction,
   compact Gaussian slope bound, and ceiling-train concavity prove both
   inert faces positive.  Hence the complete `h=4` branch is positive.
4. In `h=3`, every active endpoint `c_5=A` is positive with margin
   `69/10000`.  On the strict inert endpoint, the exact five-pulse identity
   collapses to two faces.  The `w=y` face has lower bound
   `mathcal R(a,beta)`.  On the `w=2a` face, the remaining three-pulse
   function is strictly concave in its endpoint increment.  Its threshold
   endpoint is already positive, while its other endpoint is exactly
   `mathcal P(p,a)`.  Therefore (1.1)--(1.2) close the last branch.

The four cases exhaust the least-maximizer partition.  Conversely, every
reduction was monotone in the proof-safe direction: if an original table
were nonpositive, its surviving scalar lower bound would be nonpositive.
This proves the theorem. \(\square\)

## 2. Exact one-dimensional form of the second gate

There is already a smaller sufficient analytic form for (1.2).  Write

\[
 r=1-{p\over A},
 \qquad
 s=r-{a\over A},
 \qquad
 h(x)=x e^{-\pi x^2/4}.
\tag{2.1}
\]

Then

\[
 0<r<{2\over5},
 \qquad
 0<s<{r\over2},
 \qquad
 s\ge {4r-1\over3}.
\tag{2.2}
\]

Retaining the complete `q=1,2` period-derivative blocks gives

\[
\begin{aligned}
 B(r,s)={}&h(2-r)-h(r)+h(2-s)-h(s)+h(2+r-2s)\\
 &+2h(3-2r)+2h(3-r-s)+2h(3-2s),
\end{aligned}
\tag{2.3}
\]

and

\[
 {1\over2A}{\partial\over\partial p}\mathcal P(p,a)>B(r,s).
\tag{2.4}
\]

For fixed `r`, the function `s -> B(r,s)` is strictly convex.  Hence its
unique clipped minimum `Psi(r)` is a one-dimensional sufficient gate:

\[
 \Psi(r)\ge0\quad(0<r<2/5)
 \quad\Longrightarrow\quad
 \mathcal P(p,a)>0.
\tag{2.5}
\]

The implication uses the already-positive lower-period boundary.  The sign
in (2.5) is not asserted here.

## 3. Scope

This theorem closes the structural classification of the first unresolved
finite Bellman grid.  It leaves two analytic inequalities, not a finite
case search.  It does not establish five-slot positivity, the universal
clock inequality, `nu(k)<=B(k)+O(1)`, or `nu(k)=B(k)`.
