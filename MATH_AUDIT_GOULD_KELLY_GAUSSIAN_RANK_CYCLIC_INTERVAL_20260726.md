# Gould--Kelly does not give the Gaussian-rank cyclic-interval factor

Date: 2026-07-26

## 0. Verdict

Let

\[
 v=2m,\qquad r=m-a\sqrt m+O(1),\qquad s=v-r,
 \qquad b=s-r=v-2r,
\]

where \(a>0\) is fixed (the same conclusions hold whenever
\(b\to\infty\) and \(b=o(m)\)).  Let \(\mathcal H_r\) be the simple
\(v\)-uniform hypergraph whose vertices are the \(r\)-sets of \([v]\),
and whose edges are the \(v\) length-\(r\) intervals of an unoriented
cyclic order.

Theorem 1.4 of Gould--Kelly, *Advancing the R\"odl Nibble: New bounds on
matchings and the list chromatic index of hypergraphs*,
[arXiv:2511.11375](https://arxiv.org/abs/2511.11375), does **not** prove
an almost-perfect matching in \(\mathcal H_r\).

There are two separate reasons.

1.  The obstruction is already quantitative, even if one grants a
    uniform-in-(v) version of their theorem.  The exact distance-one
    pair codegree gives

    \[
       B\le \sqrt{D/C_2}=(1+o(1)){m\over\sqrt2},
    \]

    and the full-edge codegree \(C_v=1\) sharpens this to

    \[
       B\le D^{1/(v-1)}=(e^{-1}+o(1))m.
    \]

    Their leftover is

    \[
       |V(\mathcal H_r)|B^{-1+\gamma}(\log D)^A.
    \]

    Since \(A\) is a positive integer, even the formally best case
    \(A=1\) has

    \[
       B^{-1+\gamma}\log D
       \ge (1+o(1)){2e\log m}\,B^\gamma\longrightarrow\infty.
    \]

    Thus the published conclusion is vacuous here; better intermediate
    codegree estimates cannot repair it.

2.  Independently, the theorem is quantified as

    \[
       1/D\ll1/A\ll\gamma\ll1/k,
       \qquad k+1=v=2m.
    \]

    It is a fixed-uniformity theorem.  No uniform threshold in growing
    \(k\) is stated, so the fact that \(D\) is factorial does not justify
    a diagonal application.  In fact the proof contains powers such as
    \((\log D)^{6k}\), making the nonuniformity material rather than
    cosmetic.

The remainder of this note gives the exact pair sequence, a rigorous
all-\(j\) upper envelope, and the potentially dangerous periodic-boundary
calculation.

## 1. Degree and simplicity

For \(2\le r<v/2\), the \(v\) length-\(r\) intervals of a cyclic order
determine that order up to reversal.  Indeed, among those intervals,
Johnson-distance one occurs exactly for consecutive starts, so the
induced Johnson graph recovers the coordinate cycle.  Hence

\[
   |E(\mathcal H_r)|={(v-1)!\over2}.
\]

There are (v) intervals in every edge.  Double counting incidences gives
the exact vertex degree

\[
 \boxed{D={r!s!\over2}.}                                      \tag{1.1}
\]

In the Gaussian regime, Stirling gives

\[
 \log D=(2+o(1))m\log m,
 \qquad
 D^{1/(v-1)}=(e^{-1}+o(1))m.                         \tag{1.2}
\]

## 2. Exact pair-codegree sequence

Let (X,Y\in\binom{[v]}r) be distinct, and write

\[
 t=|X\setminus Y|=|Y\setminus X|.
\]

### Proposition 2.1

For (1\le t<r),

\[
 \boxed{
   \operatorname{codeg}(X,Y)
     =(t!)^2(r-t)!(s-t)!,
   \qquad
   {\operatorname{codeg}(X,Y)\over D}
     ={2\over\binom rt\binom st}.}                 \tag{2.1}
\]

For the disjoint case \(t=r\),

\[
 \boxed{
   \operatorname{codeg}(X,Y)
      ={(r!)^2(b+1)!\over2},
   \qquad
   {\operatorname{codeg}(X,Y)\over D}
      ={b+1\over\binom sr}.}                        \tag{2.2}
\]

#### Proof

When \(t<r\), the four nonempty atoms

\[
 X\setminus Y,\quad X\cap Y,\quad Y\setminus X,
 \quad [v]\setminus(X\cup Y)
\]

must occur in one of the two opposite cyclic block orders.  Counting
directed cyclic orders gives twice the product of their factorials;
quotienting by reversal proves (2.1).

When (X,Y) are disjoint, anchor the start of the (X)-block.  After
ordering (X), the remaining linear segment consists of the (Y)-block
and the \(b\) outside points, giving \((b+1)!\) orders, and \(Y\) has
(r!) internal orders.  Quotienting by reversal proves (2.2).  \(\square\)

The sequence

\[
 q_t:=\binom rt\binom st
\]

is unimodal because

\[
 {q_{t+1}\over q_t}={(r-t)(s-t)\over(t+1)^2}.
\]

Moreover the disjoint value in (2.2) is (r^2/2) times the
\(t=r-1\) value in (2.1).  Consequently

\[
 {C_2\over D}
 =\max\left\{{2\over rs},{b+1\over\binom sr}\right\}.          \tag{2.3}
\]

For \(b=2a\sqrt m+O(1)\),

\[
 {b+1\over\binom sr}
 ={b+1\over\binom sb}
 \le (b+1)(b/s)^b
 =\exp[-\Theta(\sqrt m\log m)],
\]

so the first term wins and

\[
 \boxed{{C_2\over D}={2\over rs}=(2+o(1))m^{-2}.}              \tag{2.4}
\]

This normalized obstruction cannot be removed by regular sparsification.
Every cyclic-interval edge contains exactly (v) Johnson-distance-one
pairs, while (J(v,r)) has

\[
 {1\over2}\binom vr rs
\]

edges.  Hence any (D'\)-regular subhypergraph made from cyclic-interval
edges has average distance-one pair codegree \(2D'/(rs)\), and therefore

\[
 \Delta_2/D'\ge2/(rs).                                      \tag{2.5}
\]

## 3. A rigorous upper envelope for every (j)

Let \(C_j=C_j(\mathcal H_r)\) be the maximum codegree of \(j\) distinct
vertices.  Define

\[
 p_t={2\over\binom rt\binom st}\quad(1\le t<r),
 \qquad
 p_r={b+1\over\binom sr},
 \qquad
 d_j=\min\{r,\lfloor j/2\rfloor\}.
\]

### Proposition 3.1 (full-sequence envelope)

For every (2\le j\le v),

\[
 \boxed{
 {C_j\over D}
 \le \max_{d_j\le t\le r}p_t
 =\begin{cases}
   \max\{p_{d_j},p_r\},&d_j<r,\\
   p_r,&d_j=r.
  \end{cases}}                                               \tag{3.1}
\]

Also \(C_v=1\) exactly.

#### Proof

Suppose (j) prescribed (r)-sets occur in one cyclic order, and let
(P\subset\mathbb Z_v) be their (j) distinct start positions.  A ball
of radius \(d-1\) in the cycle has at most \(2d-1\) vertices, so two
positions in (P) have cyclic distance at least \(\lfloor j/2\rfloor\).
For \(r<v/2\), two length-\(r\) intervals whose starts have cyclic distance
(u\le v/2) have Johnson distance \(\min\{u,r\}\).  Thus the prescribed
family contains a fixed pair at Johnson distance at least \(d_j\).  Its
codegree bounds the codegree of the entire family.

The displayed ratio for \(q_{t+1}/q_t\) shows that \(q_t\) is unimodal.
Therefore the largest \(p_t\) on \([d_j,r-1]\) is attained at \(d_j\) or
\(r-1\), and \(p_r=(r^2/2)p_{r-1}\).  This proves (3.1).  Finally, a full
(v)-set of vertices contained in an edge is that edge itself, and the
hypergraph is simple, so \(C_v=1\).  \(\square\)

This envelope is deliberately one-sided: it is sufficient to audit every
possible (j)-configuration, but it is not asserted to be the exact
maximum for intermediate (j).  Determining all those exact maxima is
unnecessary for the negative Gould--Kelly conclusion, because \(C_2\) and
\(C_v\) already force the bottleneck.

## 4. Periodic boundary configurations

The only way the boundary graph of selected starts can close up before all
(v) starts are used is through \(\gcd(v,r)\).  This case does not evade
the preceding envelope, and its codegree can be computed exactly.

Put

\[
 g=\gcd(v,r),\qquad L=v/g,\qquad h=r/g.
\]

Fix a cyclic order \(\pi=(x_0,\ldots,x_{v-1})\), and take the \(L\)
intervals whose starts form one orbit under addition by (r):

\[
 \mathcal U_g=\{I_\pi(ir,r):i\in\mathbb Z_L\}.
\]

For the present Gaussian regime, (2\le h<L-2) for all sufficiently
large (m).

### Proposition 4.1 (periodic-orbit codegree)

\[
 \boxed{\operatorname{codeg}(\mathcal U_g)=(g!)^L.}             \tag{4.1}
\]

#### Proof

The orbit starts are exactly one congruence class modulo (g).  They cut
the coordinate cycle into \(L\) chunks \(B_0,\ldots,B_{L-1}\), each of
size (g), and \(\mathcal U_g\) is the family of all unions of (h)
consecutive chunks.  Since (2\le h<L-2), maximum intersections recover
the cyclic adjacency of these (L) windows, and consecutive differences
recover each chunk.  Thus every realizing coordinate cycle concatenates
the recovered chunks in the one recovered unoriented cyclic order.  The
elements inside each chunk may be ordered arbitrarily, giving exactly
\((g!)^L\) cycles.  \(\square\)

Here \(g\mid(v-2r)=b\), so \(g\le b=O(\sqrt m)\).  Stirling applied to
(1.1) and (4.1) yields

\[
 \log\left({D\over(g!)^L}\right)^{1/(L-1)}
   =g\log(m/g)+O(g).                                      \tag{4.2}
\]

For \(g=1\), this is the full edge and the root is
\((e^{-1}+o(1))m\).  For every \(g\ge2\) with \(g=O(\sqrt m)\), the root
is much larger than a constant multiple of (m).  Thus periodic closure
does not create a hidden bottleneck below the already visible
full-edge/distance-one scale.  Proposition 3.1 remains valid without any
aperiodicity assumption.

## 5. Substitution into Gould--Kelly

In Gould--Kelly's notation the uniformity is \(k+1=v=2m\).  Their
allowable matching parameter satisfies

\[
 B\le\min\left\{
   \sqrt{D/D_2},
   \min_{4\le j\le v}(D/D_j)^{1/(j-1)},
   1/\varepsilon
 \right\}.                                                   \tag{5.1}
\]

Exact regularity lets us take an arbitrarily small positive
\(\varepsilon\), so that term is harmless.  But (2.4) and \(C_v=1\)
give, for every valid choice of the upper bounds \(D_j\ge C_j\),

\[
 \boxed{
 B\le\min\left\{(1+o(1)){m\over\sqrt2},
                  (e^{-1}+o(1))m\right\}
       =(e^{-1}+o(1))m.}                                  \tag{5.2}
\]

The theorem concludes that at most

\[
 |V(\mathcal H_r)|B^{-1+\gamma}(\log D)^A                \tag{5.3}
\]

vertices are uncovered.  Since (A\) is an integer and (A\ge1),
(1.2) and (5.2) imply

\[
 B^{-1+\gamma}(\log D)^A
 \ge B^{-1+\gamma}\log D
 \ge(2e+o(1))B^\gamma\log m\longrightarrow\infty.       \tag{5.4}
\]

Thus (5.3) is larger than the entire vertex set.  This is not a failure
to estimate \(C_j\) sharply: even replacing all intermediate codegrees by
their theoretically best possible values cannot alter (5.2)--(5.4).

## 6. Why factorial degree does not diagonalize the hierarchy

The hierarchy in Theorem 1.4 means: first fix (k), then choose
\(\gamma\) sufficiently small in terms of (k), then (A) sufficiently
large in terms of \(\gamma,k\), and only then take (D) sufficiently
large.  It supplies no function \(D_0(k,A,\gamma)\) for which one has
checked

\[
 {r!s!\over2}\ge D_0(2m-1,A_m,\gamma_m).
\]

Therefore “(D) is factorial” is not a logical diagonal argument.  The
proof's explicit appearances of \((\log D)^{6k}\) also show why extracting
uniform dependence is substantive.  More importantly, even a hypothetical
uniform extraction would still be defeated by (5.4).

## 7. Precise conditional that would be useful

A tailored growing-uniformity theorem could close this one-rank matching
problem if it used the cyclic boundary geometry and returned a leftover of
the form

\[
 |V(\mathcal H_r)|\,B^{-1+o(1)}(\log D)^{o(1)},
 \qquad B=\Theta(m),                                      \tag{7.1}
\]

with the final (o(1)) strong enough that
\((\log D)^{o(1)}=m^{o(1)}\).  Then (7.1) would be \(o(|V|)\).
Gould--Kelly's published \((\log D)^A\), with \(A\ge1\) and fixed
uniformity quantified first, is not such a theorem.

Hence the rank-(r) cyclic-interval almost-factor remains an
object-specific growing-uniformity matching theorem, not a black-box
consequence of arXiv:2511.11375.
