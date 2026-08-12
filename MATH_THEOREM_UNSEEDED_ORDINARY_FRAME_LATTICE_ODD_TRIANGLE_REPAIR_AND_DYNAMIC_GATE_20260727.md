# Unseeded ordinary frames: lattice saturation, exact odd-triangle repair, and the dynamic rounding gate

Date: 2026-07-27

Scope: coefficient-one program; pure mathematics only. No computation,
search, solver, web input, or fixed-uniformity matching theorem is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 M=m+H,\qquad
 N=\binom{2m}{M}=\binom{2m}{m-H},
\tag{0.1}
\]

where \(H\) is the least integer for which

\[
 \lambda_H:=\frac WN\ge M.
\tag{0.2}
\]

In the intended regime,

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \rho:=\frac{MN}{W}=1-o(1),\qquad
 W-MN=o(W).
\tag{0.3}
\]

Throughout, \(m\) is sufficiently large. In particular
\[
 2\le H\le m-1,\qquad m\ge2H,\qquad 2H<M,
\tag{0.3a}
\]
which are the ranges used by the exchange, triangle, and cyclic-interval
arguments below.

For a top \(U\in\binom{[2m]}M\) and a directed cyclic order
\(\pi\) on \(U\), let

\[
 e(U,\pi)=\{U\}\mathbin{\dot\cup}{\cal O}(U,\pi),
\tag{0.4}
\]

where \({\cal O}(U,\pi)\) is the set of the \(M\) cyclic
\(m\)-windows. Thus an ordinary frame has one top and \(M\) owners.

Write

\[
 D=(M-1)!,\qquad
 F=m!H!,\qquad
 D_O=\binom mH F=\rho D,
\tag{0.5}
\]

and

\[
 \tau=\frac DF=\frac{\binom MH}{M}.
\tag{0.6}
\]

Here \(D\) is the directed top degree, \(D_O\) is the directed owner
degree, and \(F\) is the number of directed frames on a prescribed
compatible top which contain a prescribed owner.

The following statements are proved in this note.

1. Let \(A\) be the full top-plus-owner incidence matrix of ordinary
   frames. Over every field \(K\), its left kernel consists exactly of

   \[
   \begin{aligned}
    \beta_X&=b_0+\sum_{c\in X}b_c,\\
    \alpha_U&=-Mb_0-m\sum_{c\in U}b_c.
   \end{aligned}
   \tag{0.7}
   \]

   The parameters have one redundancy, so

   \[
    \operatorname{rank}_K A=N+W-2m
   \tag{0.8}
   \]

   in every characteristic. Every nonzero Smith invariant of \(A\)
   is therefore one. Equivalently,

   \[
   \boxed{
    \operatorname{im}_{\mathbb Z}A
    =
    \left\{(t,y):
      \sum_{X\ni c}y_X
      =m\sum_{U\ni c}t_U\quad\text{for every }c
    \right\}.}
   \tag{0.9}
   \]

   Thus the full ordinary-frame lattice is saturated. There is no hidden
   parity or other congruence obstruction arising from the determinant-two
   triangle.

2. The owner-only column lattice is also exact:

   \[
   \boxed{
   \operatorname{im}_{\mathbb Z}A_O
   =
   \left\{y\in\mathbb Z^{\binom{[2m]}m}:
     M\mid\sum_Xy_X,\quad
     m\mid\sum_{X\ni c}y_X\ \forall c
   \right\}.}
   \tag{0.10}
   \]

   In particular the exact all-top target has a balanced \(0\)-\(1\)
   owner leave satisfying every lattice condition and a signed integral
   frame representation. Positivity, not lattice membership, is the
   remaining issue.

3. The lower containment relaxation has exact Hall slack. For every
   top family \({\cal S}\),

   \[
    \left|\bigcup_{U\in{\cal S}}\binom Um\right|
    \ge\lambda_H|{\cal S}|
    \ge M|{\cal S}|.
   \tag{0.11}
   \]

   Hence one can integrally assign \(M\) distinct contained owners to
   every top. The sole missing condition in this relaxation is that the
   \(M\) owners assigned to one top must be the complete cyclic-window
   deck of one order.

4. The displayed determinant-two triangle is exactly repairable after
   the three full catalogues are restored. With notation defined in
   Section 4, the exact number of ordered choices of one pairwise
   owner-disjoint frame on each of the three tops is

   \[
    \boxed{D^3-3F^2D+3GF^2-G^3>0,}
   \tag{0.12}
   \]

   where

   \[
    G=H!^2(m-H+1)!.
   \tag{0.13}
   \]

   Thus the restricted three-column LP/IP gap is not an unseeded
   obstruction. Its half-vector also has top loads \(1/2\), not an
   integral resolution right-hand side.

5. More generally, every \(q\) distinct tops admit pairwise
   owner-disjoint ordinary frames whenever

   \[
    H(q-1)<\tau.
   \tag{0.14}
   \]

   Therefore every genuinely deficient full-catalogue top set has size
   at least

   \[
   \boxed{
    q_0=\left\lceil\frac{\tau}{H}\right\rceil+1
    =\left\lceil\frac{\binom MH}{MH}\right\rceil+1,}
   \tag{0.15}
   \]

   and

   \[
    \log q_0
    =\left(\frac12+o(1)\right)
      \sqrt m\,(\log m)^{3/2}.
   \tag{0.16}
   \]

   Hence no family of fewer than \(q_0\) tops is itself a
   full-catalogue packing obstruction. The literal selected-column
   triangle remains a valid odd inequality, but its three complete
   top catalogues are jointly saturable.

6. The full catalogue has a stronger static diagonal estimate than its
   maximum codegree. For every owner \(X\) and every frame \(g\not\ni X\),
   the number \(A_X(g)\) of \(X\)-frames externally meeting \(g\) satisfies

   \[
    \boxed{A_X(g)\le\frac{11D_O}{m^2}}
   \tag{0.17}
   \]

   for all sufficiently large \(m\). If

   \[
    \nu_0=\frac1{(M+1)D},
   \tag{0.18}
   \]

   then, simultaneously for every integer \(\ell\ge2\),

   \[
   \boxed{
    \nu_0\sum_{g\not\ni X}A_X(g)^\ell
    \le
    \left(\frac{11}{m^2}\right)^{\ell-1}D_O^\ell.}
   \tag{0.19}
   \]

   This includes, rather than cancels, repeated hits coming from odd
   triangles. The external-edge and off-centre compensation-coin
   exponential remainder is \(O(\theta^2/m^2)\) for
   \(0\le\theta\le c\log m\). Central deaths are cemetery events and
   are not included in that small remainder.

7. A precise trajectory-specific propagation statement, called OLDP in
   Section 7, would imply an integral matching of

   \[
    (1-m^{-1/20}-o(1))N=N-o(N)
   \tag{0.20}
   \]

   ordinary frames. Its cumulative stopped logarithmic error is only

   \[
    m^{-9/10+o(1)}.
   \tag{0.21}
   \]

   OLDP is **not proved here**. It cannot be replaced by a deterministic
   assertion for every edge-deletion residual: concentrated pair-star
   residuals in the current file set refute such heredity.

Consequently this note does not prove the unseeded near-resolution or
coefficient one. It does prove that the determinant-two minor, all
congruence conditions, the ordinary containment Hall system, and every
sub-\(q_0\) top family are not the obstruction. Any negative example must be
a genuinely global nonnegative packing obstruction. The shortest positive
route is the trajectory-specific OLDP propagation of (0.17)--(0.19), not
an invocation of Pippenger--Spencer from the single number \(2/m^2\).

## 1. Directed columns versus simple supports

The degree formulas in (0.5) use directed cyclic orders modulo rotation.
Reversal gives

\[
 e(U,\pi)=e(U,\pi^{\mathrm{rev}}).
\tag{1.1}
\]

For \(2\le H<m\), the family of cyclic \(H\)-intervals determines the
underlying undirected cycle, so reversal is exactly a twofold duplication.
Thus the simple support catalogue has half the displayed degrees.

More explicitly, in the simple catalogue

\[
 D^{\rm simp}=D/2,\quad F^{\rm simp}=F/2,\quad
 D_O^{\rm simp}=D_O/2,\quad G^{\rm simp}=G/2.
\tag{1.1a}
\]

The directed triangle count (4.6) is eight times the corresponding
simple-support count, every \(A_X(g)\) is halved after duplicate
representations are removed, and the dominating initial clock
\(\nu_0\) doubles. All normalized inequalities are unchanged.

This convention changes none of the conclusions below. Duplicate columns
do not alter the column lattice, left kernel, Smith invariants, or matching
feasibility. In the simple catalogue one merely gives every support the
fractional weight \(2/D\), instead of giving each directed representation
weight \(1/D\).

The uniform directed fractional point is

\[
 x_{U,\pi}=\frac1D.
\tag{1.2}
\]

Every top has load one and every owner has load

\[
 \frac{D_O}{D}=\rho\le1.
\tag{1.3}
\]

Its total weight is \(N\), which is optimal for the fractional packing LP
because every column uses one top. This is a top-perfect fractional point;
it is not a perfect fractional cover of all \(N+W\) vertices.

## 2. Exact left kernel and saturated full lattice

Let \(A\) have one row for each top and one row for each owner, and one
column for each directed frame. We determine its left kernel over an
arbitrary field \(K\).

### Lemma 2.1 (adjacent-swap exchange identity)

Suppose \((\alpha_U,\beta_X)\) lies in \(\ker_K A^T\). For distinct labels
\(a,b\), and every two \((m-1)\)-sets \(L,R\subseteq[2m]\setminus\{a,b\}\)
satisfying

\[
 |L\cap R|=m-H,
\tag{2.1}
\]

one has

\[
 \beta_{L+a}-\beta_{L+b}
 =
 \beta_{R+a}-\beta_{R+b}.
\tag{2.2}
\]

#### Proof

The kernel equation says that, on a fixed top \(U\),

\[
 \sum_{X\in{\cal O}(U,\pi)}\beta_X
\tag{2.3}
\]

is independent of the directed cyclic order \(\pi\).

Put \(a,b\) in adjacent cyclic positions and interchange them. Exactly
two cyclic \(H\)-intervals change as sets: the interval ending at the first
position and the interval beginning at the second. Equivalently, exactly
two complementary \(m\)-windows change. Their four forms are

\[
 L+a,\quad L+b,\quad R+a,\quad R+b,
\tag{2.4}
\]

with the two changes oppositely oriented. Equality of (2.3) before and
after the swap gives (2.2).

Conversely, every pair \(L,R\) satisfying (2.1) is realizable in this way.
Indeed

\[
 |R\setminus L|=|L\setminus R|=H-1.
\]

After positions \(0,1\) occupied by \(a,b\), put, in order,

\[
 R\setminus L,\qquad L\cap R,\qquad L\setminus R
\tag{2.5}
\]

in cyclic position blocks of respective lengths \(H-1,m-H,H-1\). The
two boundary \(H\)-intervals then give precisely the four windows in
(2.4). This proves the lemma. \(\square\)

### Lemma 2.2 (context independence)

For fixed distinct \(a,b\), the difference

\[
 g_{ab}(L)=\beta_{L+a}-\beta_{L+b}
\tag{2.6}
\]

is independent of the \((m-1)\)-set
\(L\subseteq[2m]\setminus\{a,b\}\).

#### Proof

Consider the graph on the \((m-1)\)-subsets of

\[
 \Omega=[2m]\setminus\{a,b\},
\]

joining two sets when their Johnson distance is \(H-1\). Lemma 2.1 says
that \(g_{ab}\) is constant on every edge. We show that this graph is
connected.

It is enough to join every ordinary Johnson-neighbour pair. Write

\[
 A=S\cup\{x\},\qquad A'=S\cup\{y\},\qquad |S|=m-2.
\]

Choose

\[
 R_0\subset S,\quad |R_0|=H-1,
\]

and

\[
 Q\subseteq\Omega\setminus(S\cup\{x,y\}),\quad |Q|=H-2.
\]

These choices exist for \(2\le H\le m-1\). Put

\[
 B=(S\setminus R_0)\cup\{x,y\}\cup Q.
\tag{2.7}
\]

Then \(|B|=m-1\), and both \(A\) and \(A'\) are at Johnson distance
\(H-1\) from \(B\). Hence the distance-\((H-1)\) graph contains a
two-edge path between every Johnson-neighbour pair. The ordinary Johnson
graph is connected, proving the claim. \(\square\)

### Theorem 2.3 (field-uniform left kernel)

For every field \(K\), every vector in \(\ker_K A^T\) has the form

\[
 \beta_X=b_0+\sum_{c\in X}b_c,
 \qquad
 \alpha_U=-Mb_0-m\sum_{c\in U}b_c.
\tag{2.8}
\]

The parameterization has exactly the one-dimensional kernel

\[
 b_c=t\quad(c\in[2m]),\qquad b_0=-mt.
\tag{2.9}
\]

Consequently

\[
 \dim_K\ker A^T=2m,\qquad
 \operatorname{rank}_K A=N+W-2m.
\tag{2.10}
\]

#### Proof

By Lemma 2.2 write \(g_{ab}\) for the context-independent difference.
Choose an \((m-1)\)-set avoiding three prescribed labels \(a,b,c\). Then

\[
 g_{ab}+g_{bc}=g_{ac}.
\tag{2.11}
\]

Fix a reference label \(r\) and put \(b_a=g_{ar}\). Equation (2.11)
gives

\[
 g_{ab}=b_a-b_b.
\tag{2.12}
\]

Therefore

\[
 X\longmapsto\beta_X-\sum_{c\in X}b_c
\]

is unchanged by every Johnson one-swap. The rank-\(m\) Johnson graph is
connected, so it is a constant \(b_0\). This proves the first equation
in (2.8).

Every frame has \(M\) owners, and every coordinate of its top occurs in
exactly \(m\) of those owners. Hence

\[
 \sum_{X\in{\cal O}(U,\pi)}\beta_X
 =Mb_0+m\sum_{c\in U}b_c.
\tag{2.13}
\]

The column kernel equation gives the formula for \(\alpha_U\).

If all \(\beta_X\) vanish, exchanging one coordinate between two
\(m\)-sets shows that all \(b_c\)'s are equal to a common \(t\), and then
\(b_0=-mt\). Thus (2.9) is the exact parameter kernel. There are
\(2m+1\) parameters and one redundancy, proving (2.10).

No division was used. In particular the proof remains valid in
characteristic two and in characteristics dividing \(m\) or \(M\). The
independent type relation

\[
 \beta_X=1,\qquad \alpha_U=-M
\]

is the parameter \(b_0=1,b_c=0\); it is not silently obtained by dividing
by \(m\). \(\square\)

### Theorem 2.4 (saturated full column lattice)

The integer column lattice of \(A\) is exactly the set in (0.9).

#### Proof

Let the nonzero Smith invariants of \(A\) be

\[
 s_1\mid s_2\mid\cdots\mid s_r.
\]

Theorem 2.3 gives the same rank \(r=N+W-2m\) over \(\mathbb Q\) and over
every \(\mathbb F_p\). If a prime \(p\) divided some \(s_i\), the rank
would drop modulo \(p\). Hence every \(s_i=1\), and

\[
 \operatorname{im}_{\mathbb Z}A
 =\operatorname{span}_{\mathbb Q}(A)\cap
  \mathbb Z^{\mathcal U\sqcup\mathcal X}.
\tag{2.14}
\]

Every column satisfies, for each coordinate \(c\),

\[
 \sum_{X\ni c}y_X
 =m\sum_{U\ni c}t_U.
\tag{2.15}
\]

The \(2m\) equations (2.15) are independent over \(\mathbb Q\). Their
common kernel has codimension \(2m\), which equals the codimension of the
column span by Theorem 2.3. They therefore describe the rational column
span exactly. Intersect with the integer lattice in (2.14).

Summing (2.15) over \(c\) also gives

\[
 \sum_Xy_X=M\sum_Ut_U,
\tag{2.16}
\]

so no separate total equation is needed over the integers. \(\square\)

## 3. Owner-only lattice, a balanced signed target, and ordinary Hall

Let \(A_O\) be the owner-row block of \(A\).

### Corollary 3.1 (owner-only lattice)

Equation (0.10) holds.

#### Proof

Necessity is columnwise: every frame has \(M\) owners, and every coordinate
of its top appears in \(m\) of them.

Conversely, suppose \(y\) obeys the divisibilities in (0.10). Put

\[
 k=\frac1M\sum_Xy_X,\qquad
 z_c=\frac1m\sum_{X\ni c}y_X.
\tag{3.1}
\]

Then

\[
 \sum_cz_c=Mk.
\tag{3.2}
\]

The integer vectors

\[
 (1,{\bf1}_U),\qquad U\in\binom{[2m]}M,
\tag{3.3}
\]

generate every integer pair \((k,z)\) satisfying (3.2). Indeed,
differences of two \(M\)-sets differing by \(i\leftrightarrow j\) generate
\((0,e_i-e_j)\), and one fixed \(M\)-set supplies the total coordinate.
Thus choose integer top totals \(t_U\) satisfying

\[
 \sum_Ut_U=k,\qquad
 \sum_{U\ni c}t_U=z_c.
\tag{3.4}
\]

The pair \((t,y)\) now satisfies (2.15), so Theorem 2.4 gives an integer
frame vector mapping to it. Its owner image is \(y\). \(\square\)

Put

\[
 d_0=W-MN.
\tag{3.5}
\]

### Corollary 3.2 (an exact balanced \(0\)-\(1\) leave is in the signed image)

There is a \(0\)-\(1\) owner vector \(y\) with total mass \(MN\), and top
vector \(t_U=1\) for every top, such that
\((t,y)\in\operatorname{im}_{\mathbb Z}A\).

#### Proof

The integer \(d_0\) is even. Indeed \(W\) is even and

\[
 \frac{MN}{2}=m\binom{2m-1}{M-1}\in\mathbb Z.
\tag{3.6}
\]

Choose \(d_0/2\) complementary owner pairs \(\{X,X^c\}\) and let
\({\cal L}\) be their union. Every coordinate occurs in exactly
\(d_0/2\) members of \({\cal L}\). Put

\[
 y_X={\bf1}_{X\notin{\cal L}}.
\tag{3.7}
\]

Then

\[
 \sum_Xy_X=W-d_0=MN
\]

and, for every coordinate \(c\),

\[
 \sum_{X\ni c}y_X
 =\frac{W-d_0}{2}
 =\frac{MN}{2}
 =m\binom{2m-1}{M-1}
 =m\sum_{U\ni c}1.
\tag{3.8}
\]

Apply Theorem 2.4. \(\square\)

The resulting frame coefficients may be negative or larger than one.
Corollary 3.2 is a lattice theorem, not a matching theorem.

### Theorem 3.3 (exact Hall theorem after forgetting cyclic grouping)

For every top family
\({\cal S}\subseteq\binom{[2m]}M\),

\[
 \left|\Gamma({\cal S})\right|
 :=
 \left|\bigcup_{U\in{\cal S}}\binom Um\right|
 \ge\lambda_H|{\cal S}|
 \ge M|{\cal S}|.
\tag{3.9}
\]

Consequently there is an integral assignment of \(M\) distinct owners to
every top, with no owner assigned twice.

#### Proof

Every top is incident with \(\binom MH\) owners, and every owner is
contained in exactly \(\binom mH\) tops. Double counting the incidences
from \({\cal S}\) into its neighbourhood gives

\[
 \binom MH|{\cal S}|
 \le\binom mH|\Gamma({\cal S})|.
\tag{3.10}
\]

The identity

\[
 \frac{\binom MH}{\binom mH}
 =\frac WN=\lambda_H
\tag{3.11}
\]

proves (3.9). Replace each top by \(M\) identical clones. A clone set
supported on \({\cal S}\) has size at most \(M|{\cal S}|\), so (3.9) is
Hall's condition for the cloned bipartite graph. An integral matching
assigns the required owners.

If \(0<|{\cal S}|<N\), the first inequality in (3.9) is strict. Equality
would force every top containing an owner in \(\Gamma({\cal S})\) to lie in
\({\cal S}\), making \({\cal S}\) a union of components of the rank-\(M\)/
rank-\(m\) containment graph. That graph is connected because adjacent
rank-\(M\) sets share an \(m\)-subset and the rank-\(M\) Johnson graph is
connected. \(\square\)

The theorem identifies the exact obstruction left after Hall: at each top,
the assigned \(M\) owners must form one cyclic promotion deck. Ordinary
containment capacity itself is not deficient.

## 4. The determinant-two triangle has zero unseeded loss

Choose pairwise disjoint sets

\[
 |C|=m-H,\qquad |A_1|=|A_2|=|A_3|=H,
\tag{4.1}
\]

which is possible when \(m\ge2H\). Put

\[
 X_i=C\cup A_i
\tag{4.2}
\]

and

\[
 U_{12}=C\cup A_1\cup A_2,\quad
 U_{23}=C\cup A_2\cup A_3,\quad
 U_{31}=C\cup A_3\cup A_1.
\tag{4.3}
\]

Choosing on \(U_{ij}\) an order in which \(A_i,A_j\) are \(H\)-blocks
gives the owner-row minor

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad |\det|=2.
\tag{4.4}
\]

The restricted three-column half-vector is feasible and has objective
\(3/2\), while an integral matching among those three columns has size one.
However its top loads are all \(1/2\). Moreover the top-row restriction of
the same three columns is the \(3\times3\) identity, so (4.4) does not
produce torsion in the full matrix.

The full catalogues repair the packing loss exactly.

### Theorem 4.1 (exact three-top repair count)

Let

\[
 G=H!^2(m-H+1)!.
\tag{4.5}
\]

The number of ordered triples of frames, one on each top in (4.3), whose
owner decks are pairwise disjoint is

\[
 D^3-3F^2D+3GF^2-G^3.
\tag{4.6}
\]

For all sufficiently large \(m\), this number is positive.

#### Proof

The pairwise top intersections are

\[
 U_{12}\cap U_{23}=X_2,\quad
 U_{23}\cap U_{31}=X_3,\quad
 U_{31}\cap U_{12}=X_1.
\tag{4.7}
\]

They have size \(m\). Thus frames on two different displayed tops can
share an owner only at the corresponding \(X_i\).

For each of the three possible pair collisions, both relevant frames must
contain the corresponding \(X_i\), giving \(F^2D\) triples. For the
intersection of two collision events, one frame must contain its two
incident owners. Those owners are at Johnson distance \(H\), and the
number of orders on their unique common top containing both is \(G\). The
other two frames each have \(F\) choices, giving \(GF^2\). If all three
collisions occur, each top frame must contain its two incident owners,
giving \(G^3\). Inclusion-exclusion proves (4.6).

Alternatively, the union bound gives

\[
 \Pr(\text{some collision})
 \le3\left(\frac FD\right)^2
 =\frac3{\tau^2}.
\tag{4.8}
\]

Since \(\tau\to\infty\), (4.6) is positive. \(\square\)

At the exact uniform fractional point (1.2), the triangle inequality for
the three displayed columns has left side \(3/D=o(1)\), not \(3/2\).
Thus abundance of determinant-two minors alone gives no fractional loss at
the resolution point.

### Theorem 4.2 (robust repair against an exterior owner set)

Let \({\cal B}\) be any occupied owner family and put

\[
 b_U=\left|{\cal B}\cap\binom Um\right|.
\tag{4.9}
\]

The three tops in (4.3) have disjoint replacement frames avoiding
\({\cal B}\) whenever

\[
 b_U+2<\tau
\tag{4.10}
\]

on each of them.

#### Proof

On a fixed triangle top \(U\), each forbidden contained owner deletes
exactly \(F\) of the \(D\) frames. Also forbid the two possible common
owners in (4.7). At least

\[
 D-(b_U+2)F>0
\tag{4.11}
\]

frames remain. Choose one independently on each top. Any owner common to
two chosen frames would have to be one of the three owners in (4.7), all of
which were forbidden. \(\square\)

The number of tops for which (4.10) can fail is at most

\[
 \frac{|{\cal B}|\binom mH}{\tau-2}
 =\rho|{\cal B}|\frac\tau{\tau-2}.
\tag{4.12}
\]

For the packet-bank scale

\[
 |{\cal B}|\le\frac{3MW}{P_H},\qquad
 P_H=(256/3+o(1))MH^3,
\tag{4.13}
\]

the ratio of (4.12) to \(N\) is at most

\[
 \frac{3M^2}{P_H}\frac\tau{\tau-2}
 =\left(\frac9{256}+o(1)\right)\frac{M}{H^3}
 =o(1).
\tag{4.14}
\]

Thus the explicit triangle remains locally repairable away from \(o(N)\)
packet-damaged tops. This does not prove simultaneous global repair.

## 5. Every small top family is resolvable

The previous theorem is a three-top instance of a general greedy result.

### Lemma 5.1 (distinct-top deck intersection)

Let \(U\ne V\) be two rank-\(M\) tops and put

\[
 d=|U\setminus V|=|V\setminus U|.
\]

For every frame \(e(U,\pi)\),

\[
 \left|{\cal O}(U,\pi)\cap\binom Vm\right|
 \le(H-d+1)_+\le H.
\tag{5.1}
\]

#### Proof

Write the owners of the frame as \(U\setminus B_i\), where the \(B_i\)'s
are the cyclic \(H\)-intervals of \(\pi\). The owner \(U\setminus B_i\)
is contained in \(V\) exactly when

\[
 U\setminus V\subseteq B_i.
\tag{5.2}
\]

If no cyclic \(H\)-interval contains the fixed \(d\)-set \(U\setminus V\),
the count is zero. Otherwise unwrap one containing interval. The span of
\(d\) distinct cyclic positions is at least \(d-1\), so at most
\(H-d+1\) starts of an \(H\)-interval contain them. Since \(H<M/2\) in
the present regime, there is no second wrapped representation. \(\square\)

### Theorem 5.2 (sub-\(q_0\) top resolution)

Let \(U_1,\ldots,U_q\) be distinct tops. They admit pairwise
owner-disjoint frames whenever

\[
 H(q-1)<\tau.
\tag{5.3}
\]

More precisely, the greedy construction works in a displayed ordering if

\[
 \sum_{i<j}(H-d(U_i,U_j)+1)_+<\tau
\tag{5.4}
\]

for every \(j\).

#### Proof

Suppose frames have been chosen on \(U_1,\ldots,U_{j-1}\). By Lemma 5.1,
the frame on \(U_i\) has at most
\((H-d(U_i,U_j)+1)_+\) owners contained in \(U_j\). Each such owner lies
in exactly \(F\) of the \(D\) frames on \(U_j\). Therefore the number of
frames on \(U_j\) meeting an earlier frame is at most

\[
 F\sum_{i<j}(H-d(U_i,U_j)+1)_+.
\tag{5.5}
\]

Under (5.4) this is less than \(F\tau=D\), so an available frame exists.
The uniform bound (5.3) follows from (5.1). \(\square\)

With an exterior owner set \({\cal B}\), the same proof works under

\[
 b_{U_j}+
 \sum_{i<j}(H-d(U_i,U_j)+1)_+<\tau.
\tag{5.6}
\]

Every top family of size at most \(\lceil\tau/H\rceil\) satisfies (5.3).
Therefore a deficient full-catalogue top family has size at least \(q_0\)
from (0.15).

Finally, Stirling's formula in the range \(H=o(M)\) gives

\[
 \log\binom MH
 =H\log\frac MH+H+O\left(\frac{H^2}{M}+\log H\right).
\tag{5.7}
\]

Together with \(H=(1+o(1))\sqrt{m\log m}\), this proves (0.16).

The theorem rules out bounded and sub-\(q_0\) obstructions. Since
\(q_0=N^{o(1)}=o(N)\), it does not rule out many interacting large
obstruction blocks and therefore does not itself imply a near-resolution.

## 6. Static external-link diagonals

For owners \(X,Y\), write

\[
 p(X,Y)=\frac{d(X,Y)}{D_O}.
\tag{6.1}
\]

The exact pair-codegree table is

\[
 p(X,Y)=
 \begin{cases}
  2\binom md^{-2},&1\le d=d_J(X,Y)<H,\\[2mm]
  (m-H+1)\binom mH^{-2},&d=H,\\[2mm]
  0,&d>H.
 \end{cases}
\tag{6.2}
\]

Let \(g=e(V,\pi)\) be a physical frame and \(X\notin g\). Define

\[
 A_X(g)=
 \left|
 \left\{f:X\in f,
       (f\setminus\{X\})\cap g\ne\varnothing
 \right\}
 \right|.
\tag{6.3}
\]

This counts external events which delete at least one noncentral resource
of the \(X\)-link.

### Lemma 6.1 (five distance-one deck neighbours)

For every \(X\) and \(g\), at most five owners in \({\cal O}(g)\) are at
Johnson distance one from \(X\).

#### Proof

Write

\[
 Y_i=V\setminus B_i,
\]

where the \(B_i\)'s are the cyclic \(H\)-intervals of \(\pi\). Put

\[
 a=|X\setminus V|,\qquad
 R=V\setminus(X\cap V),\qquad |R|=H+a.
\]

One has

\[
 d_J(X,Y_i)=a+|X\cap B_i|.
\tag{6.4}
\]

If this distance is one, then \(a\le1\).

If \(a=0\), the interval \(B_i\) contains \(H-1\) points of the fixed
\(H\)-set \(R\). Any two such intervals intersect in at least \(H-2\)
positions. Because \(2H<M\), their cyclic starts differ by at most two,
so there are at most five possible starts.

If \(a=1\), the interval \(B_i\) is an \(H\)-subset of the fixed
\((H+1)\)-set \(R\). Any two such intervals intersect in at least \(H-1\)
positions, so their starts differ by at most one; there are at most three.
The uniform bound five follows. \(\square\)

### Theorem 6.2 (uniform external-link bound)

For every owner \(X\) and every frame \(g\not\ni X\),

\[
 A_X(g)\le\frac{11D_O}{m^2}
\tag{6.5}
\]

for all sufficiently large \(m\).

#### Proof

By Lemma 6.1 and (6.2),

\[
\begin{aligned}
 \sum_{Y\in{\cal O}(g)}p(X,Y)
 &\le \frac{10}{m^2}
  +2MH\binom m2^{-2}
  +M(m-H+1)\binom mH^{-2}\\
 &=\frac{10+o(1)}{m^2}.
\end{aligned}
\tag{6.6}
\]

The second term is \(O(H/m^3)=o(m^{-2})\), and the third is smaller.

An \(X\)-frame may meet \(g\) through an owner \(Y\in{\cal O}(g)\),
which is counted by the corresponding pair codegree. It may also have
the same top \(V\) as \(g\). The latter is possible only if \(X\subset V\)
and contributes at most \(F\) frames. Put

\[
 q=\frac FD=\frac{M}{\binom MH}=m^{-\omega(1)}.
\tag{6.7}
\]

Then \(F=qD=o(D_O/m^2)\). Combining this with (6.6) proves (6.5).
\(\square\)

For a top \(U\ne V\), the analogous external-link count is at most
\(HF=HqD=m^{-\omega(1)}D\), by Lemma 5.1.

### Theorem 6.3 (all-order initial diagonal)

Let

\[
 \nu_0=\frac1{(M+1)D}.
\]

For every owner \(X\) and every integer \(\ell\ge2\), equation (0.19)
holds. Consequently, uniformly for \(0\le\theta\le c\log m\),

\[
\boxed{
 \nu_0\sum_{g\not\ni X}
 \left[
  \exp\left(\theta\frac{A_X(g)}{D_O}\right)
  -1-\theta\frac{A_X(g)}{D_O}
 \right]
 \le C\frac{\theta^2}{m^2}.}
\tag{6.8}
\]

#### Proof

Double count ordered pairs \((f,g)\), where \(f\) is an \(X\)-frame and
\(g\) externally meets \(f\setminus\{X\}\). There are \(D_O\) choices
of \(f\). Its top has degree \(D\), and its \(M-1\) noncentral owners each
have degree \(D_O\). Hence

\[
 \sum_{g\not\ni X}A_X(g)
 \le D_O\bigl[D+(M-1)D_O\bigr].
\tag{6.9}
\]

Since \(D_O\le D\), multiplication by \(\nu_0\) gives

\[
 \nu_0\sum_gA_X(g)\le D_O.
\tag{6.10}
\]

Using the fixed uniform bound (6.5),

\[
 \nu_0\sum_gA_X(g)^\ell
 \le
 \left(\frac{11D_O}{m^2}\right)^{\ell-1}
 \nu_0\sum_gA_X(g),
\]

which proves (0.19). Sum the exponential series. Because
\(11\theta/m^2=o(1)\) in the stated range, the sum is bounded by
\(C\theta^2/m^2\). \(\square\)

The fixed constant \(11\), rather than an \((11+o(1))\) base, is important
when \(\ell\) grows.

At the exact degree-balanced reference clock
\(\nu_0=1/((M+1)D)\), an owner has off-centre coin rate

\[
 \chi_0=\frac{1-\rho}{M+1}.
\tag{6.11}
\]

For \(Y\ne X\), put \(P_X(Y)=d(X,Y)\). Since

\[
 \sum_{Y\ne X}p(X,Y)=M-1,\qquad
 \max_{Y\ne X}p(X,Y)=\frac2{m^2},
\tag{6.12}
\]

the off-centre coin analogue of (6.8) is

\[
 O\left((1-\rho)\frac{\theta^2}{m^2}\right).
\tag{6.13}
\]

For the predictable envelope \(e^{2\eta}D\) used in Section 7, the
actual initial edge rate is at most \(\nu_0\), and the factor
\(1-\rho\) in (6.13) is replaced by

\[
 1-\rho e^{-2\eta}=O(\eta+1-\rho).
\tag{6.13a}
\]

This is still \(o(1)\) and preserves the \(m^{-2}\) diagonal scale.

The coin at \(X\), and every selected edge containing \(X\), kills the
entire \(X\)-link. Those central events are stopping or cemetery hazards;
they are not small Taylor remainders and are not included in (6.13).

There is also an exact framewise pair ledger. For every frame \(f\),

\[
\boxed{
 \frac1D\sum_{\{v,w\}\subset f}d(v,w)
 =Mq+\rho\left(\frac2m+o(m^{-1})\right)
 =\frac{2\rho}{m}+o(m^{-1}).}
\tag{6.14}
\]

Indeed the \(M\) top-owner pairs each have codegree \(F=qD\), while the
exact normalized owner-pair mass inside one cyclic frame is
\(2/m+o(m^{-1})\) relative to \(D_O\).

## 7. The exact dynamic gate

This section states the trajectory assertion which would finish the
unseeded near-resolution. It is deliberately marked unproved.

Set \(x(t)=e^{-t/(M+1)}\). Put

\[
 \eta=m^{-1/10},\qquad
 \widehat\Delta_t=e^{2\eta}D x(t)^M.
\tag{7.1}
\]

Run the compensated continuous greedy process against this predictable
degree envelope. At time \(t\), an active frame rings at rate

\[
 \nu_t=\frac1{(M+1)\widehat\Delta_t}.
\tag{7.2}
\]

As long as \(d_t(y)\le\widehat\Delta_t\), an active vertex \(y\) has an
independent compensation coin of rate

\[
 \chi_t(y)=
 \frac{\widehat\Delta_t-d_t(y)}
 {(M+1)\widehat\Delta_t}.
\tag{7.3}
\]

Thus its total central deletion hazard is exactly

\[
 \nu_td_t(y)+\chi_t(y)=\frac1{M+1}.
\tag{7.4}
\]

When an edge rings, add it to the matching and delete all its vertices.
A coin deletes only its vertex. In either case all incident edges are
deleted. A vertex is quarantined immediately if the decreasing envelope
would cross below its current degree. It is also quarantined if it becomes
isolated or if its stopped logarithmic degree exits

\[
 \left|
 \log d_t(v)-\log d_v(0)-M\log x(t)
 \right|\le\eta.
\tag{7.4a}
\]

Thus the logarithm below is always defined and every surviving degree lies
below the predictable envelope. The unproved OLDP assertion includes the
statement that this incidence-weighted quarantine and every deletion
cascade it creates have total size \(o(N)\) tops and \(o(W)\) owners.

Put

\[
 z=m^{-1/20},\qquad
 T=(M+1)\log(1/z).
\tag{7.5}
\]

For an active vertex \(v\) and an active frame \(g\not\ni v\), define

\[
 A_{v,t}(g)=
 \left|\{f:v\in f,\ (f\setminus\{v\})\cap g\ne\varnothing\}\right|,
\tag{7.6}
\]

and

\[
 P_{v,t}(y)=d_t(v,y).
\tag{7.7}
\]

### Unproved Lemma OLDP (ordinary-link diagonal propagation)

There is an adaptive, incidence-weighted quarantine with total size
\(o(N)\) tops and \(o(W)\) owners, including all cascaded losses, such that
with probability \(1-o(1)\), uniformly for \(t\le T\), every surviving
nonexceptional incidence satisfies

\[
 \max_{g\not\ni v}\frac{A_{v,t}(g)}{d_t(v)},
 \quad
 \max_{y\ne v}\frac{P_{v,t}(y)}{d_t(v)}
 \le
 \epsilon(t):=\frac{m^{o(1)}}{m^2x(t)^2},
\tag{7.8}
\]

\[
 \nu_t\sum_{g\not\ni v}
 \left(\frac{A_{v,t}(g)}{d_t(v)}\right)^2
 +
 \sum_{y\ne v}\chi_t(y)
 \left(\frac{P_{v,t}(y)}{d_t(v)}\right)^2
 \le\epsilon(t),
\tag{7.9}
\]

and every active frame \(f\) satisfies, outside discarded incidence mass,

\[
 \frac1{\widehat\Delta_t}
 \sum_{\{y,w\}\subset f}d_t(y,w)
 \le
 \gamma(t):=\frac{m^{o(1)}}{mx(t)^2}.
\tag{7.10}
\]

The quarantine clause must be weighted: exceptional cardinality without
control of the incident active catalogue does not prevent a cascade.

### Proposition 7.1 (OLDP implies the unseeded near-resolution)

If OLDP holds, then the process produces an integral matching of at least

\[
 (1-z-o(1))N=N-o(N)
\tag{7.11}
\]

ordinary frames. Its owner leave is \(o(W)\).

#### Proof

Fix a nonexceptional active vertex \(v\) and stop at its central death.
Let

\[
 Z_v(t)=\log d_t(v)-\log d_v(0)-M\log x(t).
\tag{7.12}
\]

An external edge \(g\) changes the logarithm by

\[
 \log\left(1-\frac{A_{v,t}(g)}{d_t(v)}\right),
\tag{7.13}
\]

and an off-centre coin at \(y\) changes it by

\[
 \log\left(1-\frac{P_{v,t}(y)}{d_t(v)}\right).
\tag{7.14}
\]

For every candidate frame through \(v\), the exact total hazard of each
of its \(M\) other vertices is \(1/(M+1)\) by (7.4). Two corrections are
needed before these \(M\) marginal hazards equal the stopped external
log-degree drift.

First, an edge containing both \(v\) and a neighbour \(y\) is included in
the marginal hazard of \(y\), but it centrally kills \(v\) and is a
stopping event. Averaged over candidate frames, this centred-link term is
at most \(\gamma(t)/(M+1)\) by (7.10). Second, a common external edge
which hits two or more neighbours is overcounted by the separate marginal
hazards. The exact inequality

\[
 (s-1)_+\le\binom s2
\tag{7.15}
\]

and (7.10) bound this second discrepancy by another
\(\gamma(t)/(M+1)\). Hence the total drift discrepancy is at most

\[
 \frac{2\gamma(t)}{M+1}.
\tag{7.16}
\]

Equations (7.8)--(7.9) bound the Taylor remainders and predictable
quadratic variation. Central edge and central coin deaths are stopping
events, not terms in this expansion.

The integrated bounds are

\[
\begin{aligned}
 \int_0^T\epsilon(t)\,dt
 &\le
 \frac{m^{o(1)}(M+1)}{m^2}
 \int_z^1x^{-3}\,dx
 =m^{-9/10+o(1)},\\
 \int_0^T\frac{2\gamma(t)}{M+1}\,dt
 &\le
 \frac{2m^{o(1)}}m
 \int_z^1x^{-3}\,dx
 =m^{-9/10+o(1)}.
\end{aligned}
\tag{7.17}
\]

Consequently the stopped martingale inequality, with
the displayed \(\eta=m^{-1/10}\), gives

\[
 d_t(U)=(1+O(\eta))Dx(t)^M,\qquad
 d_t(X)=(1+O(\eta))D_Ox(t)^M
\tag{7.18}
\]

outside an incidence-weighted exceptional family. The one-vertex tail is
\(\exp[-m^{7/10+o(1)}]\). It is not enough for a union bound over all
\(W\) owners, but weighted expectation and Markov quarantine give the
allowed \(o(W)\) owner incidence and \(o(N)\) top loss; this weighted
conclusion is part of OLDP's quarantine assertion.

Between quarantine interventions every top dies at total rate
\(1/(M+1)\). Equations (7.1), (7.3), and (7.18) make its
compensation-coin rate \(O(\eta/(M+1))\).
Therefore the number of roots lost to coins is

\[
 O(\eta\log m)N=o(N).
\tag{7.19}
\]

The surviving roots at \(T\) number \((z+o(1))N\), and quarantine loses
another \(o(N)\). Every remaining root death is caused by a selected
physical frame, and selected frames are pairwise vertex-disjoint. This
proves (7.11).

For completeness, between quarantine interventions the active-root count
has transition \(s\mapsto s-1\) at total rate \(s/(M+1)\), by (7.4).
It is therefore the standard linear pure-death chain; equivalently, at a
fixed time its unquarantined survivor count has the binomial law with
survival probability \(x(t)\). Chernoff's inequality gives
\(S_T=zN+o(N)\), and the charged \(o(N)\) root quarantine preserves this
estimate.

Finally,

\[
 W-M|{\cal M}|
 =(W-MN)+M(z+o(1))N=o(W),
\tag{7.20}
\]

using (0.3) and \(z=o(1)\). \(\square\)

The proof of Proposition 7.1 is conditional only in the explicitly named
OLDP propagation and its adaptive weighted-quarantine clause. Equations
(7.17) show that the numerical ledger has large room once OLDP is known.

## 8. Exact role of the determinant-two triangle in the dynamic problem

Let \(e_{12},e_{23},e_{31}\) be the three literal columns producing
(4.4), and retain the owner notation \(X_1,X_2,X_3\). Take

\[
 v=X_1,\qquad g=e_{23}.
\]

The \(X_1\)-link contains both \(e_{12}\) and \(e_{31}\). The frame
\(e_{23}\) meets these two link edges at the distinct owners \(X_2\) and
\(X_3\). Therefore

\[
 A_{X_1}(e_{23})\ge2.
\tag{8.1}
\]

The triangle contributes at least the strictly positive term

\[
 \nu_0
 \left[
  \exp\left(2\theta/D_O\right)-1-2\theta/D_O
 \right]
\tag{8.2}
\]

to the exponential remainder (6.8). It is neither canceled nor treated
by total unimodularity. It is simply small in the full factorial
catalogue, and Theorem 6.3 counts it at every order.

If an adversarial residual collapses this link to the two displayed
columns, then \(A/d=1\). The pair-star constructions in

MATH_AUDIT_ORDINARY_FRAME_PAIR_COLUMN_FINITE_CUTOFF_AND_PAIR_STAR_20260727.md

and

MATH_THEOREM_PROMOTION_FRAME_HIGHER_CODEGREES_FINITE_TOWER_AND_DOMINO_TWIN_WALL_20260727.md

make this failure quantitative for arbitrary edge-deletion
subcatalogues, even after polylogarithmic physical histories. Those
constructions do not show that the compensated random trajectory reaches
such a state with appreciable probability. They prove exactly that OLDP
must be trajectory-specific and cannot be inferred deterministically from
the initial \(2/m^2\) codegree or from monotonicity under deletion.

## 9. Audited implication boundary

Proved unconditionally:

1. the exact left kernel over every field, including characteristic two;
2. full Smith saturation and the lattice formula (0.9);
3. the exact owner-only lattice (0.10);
4. a balanced \(0\)-\(1\) leave with a signed integral all-top frame
   representation;
5. the exact cloned-containment Hall theorem;
6. the exact unseeded repair count for the determinant-two triangle;
7. robust local triangle repair away from the explicitly bounded damaged
   top set;
8. resolution of every top family below the threshold (0.15);
9. the static external-link bound (0.17);
10. the all-order diagonal (0.19), with central deaths correctly stopped;
    and
11. the exact framewise pair ledger (6.14).

Not proved:

1. OLDP, including its process-hereditary estimates (7.8)--(7.10);
2. adaptive incidence-weighted quarantine without a loss cascade;
3. an integral matching of \(N-o(N)\) ordinary frames;
4. resilience after the full conveyor bank beyond the already proved
   \(o(N)\) local-damage estimate; or
5. coefficient one.

The determinant-two triangle is therefore fully accounted for. It proves
non-TU of a restricted owner minor, but it supplies neither torsion, an
integral top-right-hand-side hole, a three-top packing loss in the full
catalogue, nor a full-catalogue obstruction on those three tops.
Conversely, exact
fractional feasibility, maximum codegree \(2/m^2\), and static all-order
diagonals do not by themselves prove the dynamic propagation. Any correct
positive proof must establish OLDP or an equally strong trajectory-specific
replacement; any correct negative proof must exhibit a global
nonnegative-packing obstruction on at least \(q_0\) interacting tops.
