# Audit: the codimension-\(2\lceil\log_2 b\rceil\) moment code

**Verdict (2026-09-05).** The probabilistic dual-distance argument is
valid for the internal three-rank flag system of Master I.10b/I.4, after
the statement and proof corrections listed below. It is not a
full-completed-tour support-disjointness theorem.

Let \(b\) be odd,

\[
 m=\lceil\log_2 b\rceil,\qquad Q=2^m,
 \qquad \mathbb F_Q/\mathbb F_2,                       \tag{0.1}
\]

and let \(H\) be an integer with \(H=o(b)\). For the proof below, \(b\)
is sufficiently large that

\[
                         Q\ge8,\qquad 2m\le b-1.       \tag{0.2}
\]

The second condition is necessary because the cyclic difference has a
one-dimensional kernel.

## 1. Exact collision universe

The forbidden set \(\mathcal B\) must mean collisions among the
\(q=b(b-1)\) attached flags

\[
 (s,k),\qquad s\in\mathbb Z_b,\quad1\le k<b,          \tag{1.1}
\]

at the three ranks in Master I.10b. It must not mean collisions among all
\(b^2\) cyclic starts of a completed tour.

Define

\[
 (\partial x)_j=x_j+x_{j-1},\qquad j\in\mathbb Z_b.  \tag{1.2}
\]

For the internal collision set,

\[
 \boxed{\operatorname {wt}(\partial h)\in\{2,4\}
        \quad(h\in\mathcal B).}                       \tag{1.3}
\]

The proof in the pasted text is correct after adding one missing range
restriction. In the lower-rank case, two attached positions in one packet
give

\[
                         h=\mathbf1_I+\varepsilon e_s, \tag{1.4}
\]

where \(I\) is an interval in the punctured cyclic order and
\(|I|\le b-2\). The inequality follows because the attached positions
range only over \(1,\ldots,b-1\). Thus (1.4) is not the all-one word and
has at most two cyclic components, so
\(\operatorname {wt}(\partial h)\le4\).

In the middle case, \(h\) is supported on the empty and doubled pair
indices. In the internal upper case, it is supported on the empty index
and two consecutive doubled indices; every subset of those three indices
has at most two cyclic components. In the boundary upper case it is
supported on one index. Hence the derivative always has weight at most
four. A cyclic binary derivative has even weight and vanishes only on
\(0,\mathbf1\). The first is not a collision difference; the support
descriptions above and \(b\ge5\) exclude \(\mathbf1\). This proves (1.3).

The scope is essential. For all completed cyclic starts,
\(\mathbf1\) is a lower-rank collision difference and
\(\partial\mathbf1=0\).

## 2. Deterministic moment separation

Choose distinct

\[
                  \gamma_0,\ldots,\gamma_{b-1}\in\mathbb F_Q           \tag{2.1}
\]

and define the binary linear map

\[
 \mathsf A x=
 \left(\sum_j\gamma_j(\partial x)_j,\
       \sum_j\gamma_j^3(\partial x)_j\right)\in\mathbb F_Q^2,
 \qquad\mathcal C=\ker\mathsf A.                      \tag{2.2}
\]

No binary vector \(z\) of weight two or four lies in the kernel of the
two moment sums. At weight two, the first sum would equate two distinct
\(\gamma\)'s. At weight four, write the four distinct field elements as
\(a,b,c,d\). The first sum gives \(d=a+b+c\), while characteristic two
gives

\[
 a^3+b^3+c^3+(a+b+c)^3
 =(a+b)(a+c)(b+c)\ne0.                                \tag{2.3}
\]

Combining (1.3) and (2.3) proves

\[
                         \mathcal C\cap\mathcal B=\varnothing          \tag{2.4}
\]

for every injection (2.1).

## 3. The adjoint rows and their indexing

Every \(\mathbb F_2\)-linear functional on \(\mathbb F_Q^2\), not
“field-linear functional,” has the unique form

\[
 (u,w)\longmapsto\operatorname {Tr}(\alpha u+\beta w)
 \qquad(\alpha,\beta\in\mathbb F_Q),                  \tag{3.1}
\]

by nondegeneracy of the absolute trace pairing. Put

\[
 f_{\alpha,\beta}(t)=\operatorname {Tr}(\alpha t+\beta t^3).           \tag{3.2}
\]

Then

\[
\begin{aligned}
 \operatorname {Tr}\bigl((\alpha,\beta)\cdot\mathsf A x\bigr)
 &=\sum_j f_{\alpha,\beta}(\gamma_j)(x_j+x_{j-1})\\
 &=\sum_j
   \bigl[f_{\alpha,\beta}(\gamma_j)
        +f_{\alpha,\beta}(\gamma_{j+1})\bigr]x_j.      \tag{3.3}
\end{aligned}
\]

Thus the pasted adjoint index is correct:

\[
 v_j=f(\gamma_j)+f(\gamma_{j+1}),                     \tag{3.4}
\]

with \(j+1\) read cyclically. The \(j+1\), rather than \(j-1\), follows
from the convention \((\partial x)_j=x_j+x_{j-1}\).

## 4. Nonconstancy and \(Q/4\) balance

As a Boolean polynomial in any binary coordinate basis of \(\mathbb F_Q\),
\(f_{\alpha,\beta}\) has degree at most two: Frobenius
\(t\mapsto t^2\) is binary linear, \(t^3=t\,t^2\) is quadratic, and trace
is binary linear.

For \((\alpha,\beta)\ne(0,0)\), \(f_{\alpha,\beta}\) is nonconstant when
\(Q\ge8\). The missing displayed calculation in the pasted proof is

\[
\begin{aligned}
 f(y+z)+f(y)+f(z)
 &=\operatorname {Tr}\bigl(\beta y^2z+\beta yz^2\bigr)\\
 &=\operatorname {Tr}\left(
   \bigl[\beta y^2+(\beta y)^{Q/2}\bigr]z\right).      \tag{4.1}
\end{aligned}
\]

Here

\[
 \operatorname {Tr}(c z^2)=\operatorname {Tr}(c^{Q/2}z)               \tag{4.2}
\]

is the adjoint-of-Frobenius identity. If \(f\) were constant, then
\(f(0)=0\) would make it identically zero. Equations (4.1) and
nondegeneracy of trace would imply

\[
             \beta y^2+\beta^{Q/2}y^{Q/2}=0
             \qquad(y\in\mathbb F_Q).                 \tag{4.3}
\]

For \(Q\ge8\), the left side is a nonzero polynomial of degree \(Q/2<Q\)
whenever \(\beta\ne0\), because the exponents \(2,Q/2\) are distinct.
It cannot vanish at all \(Q\) field elements. Hence \(\beta=0\), after
which nondegeneracy of \(t\mapsto\operatorname {Tr}(\alpha t)\) gives
\(\alpha=0\), a contradiction.

The claimed balance is the minimum-distance bound for order-two
Reed--Muller polynomials:

\[
 0\ne P,\quad\deg P\le2
 \quad\Longrightarrow\quad
 |\{x:P(x)=1\}|\ge2^{m-2}=Q/4.                        \tag{4.4}
\]

For completeness, write
\(P(x',x_m)=P_0(x')+x_mP_1(x')\). If \(P_1=0\), induction on \(m\)
and duplication of the two slices gives (4.4). If \(P_1\ne0\), then
\(\deg P_1\le1\); on every \(x'\) with \(P_1(x')=1\), the two slice
values differ and contribute exactly one one. Induction applied to
\(P_1\) again gives (4.4). Applying the same argument to \(1+f\), which
is nonzero because \(f\) is nonconstant, shows

\[
 |\{t:f(t)=0\}|\ge Q/4,\qquad
 |\{t:f(t)=1\}|\ge Q/4.                               \tag{4.5}
\]

## 5. Sampling without replacement

Choose the ordered injection (2.1) uniformly without replacement. Fix a
nonzero coefficient pair and its \(f\). Put \(L=Q/8\), an integer because
\(Q\ge8\). Also \(L\le b\), since \(Q<2b\).

Before draw \(r<L\), both value classes in (4.5) retain at least

\[
                         Q/4-r\ge Q/8                 \tag{5.1}
\]

unused elements. Therefore, for either prescribed next bit, the opposite
class contains at least \(Q/8\) of the at most \(Q\) remaining elements.
The conditional probability of the prescribed bit is at most \(7/8\).
Consequently every prescribed full value sequence has probability at most

\[
 (7/8)^{Q/8}\le e^{-c b},\qquad
 c={1\over8}\log{8\over7}>0.                          \tag{5.2}
\]

The word \(v\) in (3.4) records exactly the cyclic transitions of

\[
                  f(\gamma_0),\ldots,f(\gamma_{b-1}). \tag{5.3}
\]

The number of binary cyclic sequences with at most \(H\) transitions is at
most

\[
                         2\sum_{j=0}^{H}{b\choose j}. \tag{5.4}
\]

Indeed choose the initial bit and a set of transition edges; ignoring the
even-parity consistency restriction only enlarges the count. Since
\(H=o(b)\),

\[
 \log\left(\sum_{j=0}^{H}{b\choose j}\right)=o(b).    \tag{5.5}
\]

There are \(Q^2-1<4b^2\) nonzero coefficient pairs. Equations
(5.2)--(5.5) give

\[
\Pr\left(\exists(\alpha,\beta)\ne(0,0):
          \operatorname {wt}v_{\alpha,\beta}\le H\right)
\le
 2Q^2\left(\sum_{j=0}^{H}{b\choose j}\right)
 (7/8)^{Q/8}
=o(1).                                                \tag{5.6}
\]

Thus an ordered injection exists for which every nonzero adjoint row has
weight greater than \(H\).

## 6. Rank, size, and exact balance

If \(\mathsf A\) did not have full binary rank \(2m\), a nonzero binary
functional on \(\mathbb F_Q^2\) would annihilate its image. By (3.1), its
adjoint row would be zero, contradicting (5.6). Hence

\[
 \operatorname {rank}_{\mathbb F_2}\mathsf A=2m,\qquad
 |\mathcal C|=2^{b-2m}={2^b\over Q^2}
 \ge {2^b\over4b^2}.                                  \tag{6.1}
\]

Moreover the nonzero adjoint rows are exactly the nonzero words of
\(\mathcal C^\perp\), so

\[
                         d(\mathcal C^\perp)>H.        \tag{6.2}
\]

If the projection of \(\mathcal C\) onto a coordinate set
\(J\subseteq[b]\), \(|J|\le H\), were not surjective, a nonzero functional
on \(\mathbb F_2^J\) annihilating its image would extend by zero to a
nonzero word of \(\mathcal C^\perp\) of weight at most \(H\). Thus every
such projection is onto. All fibers of a surjective linear map have equal
size, and translating gives exact \(H\)-wise balance in every coset.

## 7. Edge cases and exact usefulness

1. The proof is genuinely characteristic two: both (2.3) and the binary
   transition interpretation use it.
2. The \(Q\ge8\) restriction is real. At \(Q=4\),
   \(\operatorname {Tr}_{\mathbb F_4/\mathbb F_2}(t^3)\) is identically
   zero, so nonconstancy fails for \((\alpha,\beta)=(0,1)\).
3. Full rank is impossible unless \(2m\le b-1\), since
   \(\partial\mathbf1=0\). “Sufficiently large” must retain this
   requirement.
4. The code always contains \(\mathbf1\). This is harmless for the
   internal flag collision set, where \(\mathbf1\notin\mathcal B\), but
   prevents interpreting the result as disjointness of all completed
   rank-\((b-1)\) supports: antipodal completed tours have exactly \(2b\)
   common lower targets.
5. Therefore the valid conclusion is: every coset is jointly disjoint on
   the three **attached internal flag** target families, has size (6.1),
   and has exact \(H\)-wise state balance. The result strengthens the local
   bank used in Master I.4--I.5 by a factor of order \(b\). It does not
   perform the remaining cross-pairing all-band tour selection.
