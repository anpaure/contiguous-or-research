# Fourth-wave A: equal and polygon-interior four-boxes

Date: 2026-07-25

## 0. Verdict

For

\[
 P(\boldsymbol\ell)=\prod_{i=1}^4[0,\ell_i],
\]

let \(g_4(\boldsymbol\ell)\) be the least length of a word of nonzero box
points whose nonempty contiguous coordinatewise maxima contain every
nonzero target, and let \(w_4(\boldsymbol\ell)\) be the box width.

This attack does **not** prove either

\[
 g_4(t,t,t,t)=w_4(t,t,t,t)+o(t^3)
\]

or a positive-proportion lower bound on the equal cube.  It does produce
four unconditional advances which sharply change the surviving problem.

1. The A3 boundary obstruction propagates into a genuine open collar of
   the strict polygon interior.  An explicit integral example is

   \[
   \boxed{
   \liminf_{n\to\infty}
   \frac{
   g_4(36n,36n,36n,105n)
   -w_4(36n,36n,36n,105n)}
   {n^3}
   \ge \frac{165579}{512}>0.}
   \tag{0.1}
   \]

   Here \(105<36+36+36\), so this is not a dominant or boundary ray.

2. On every compact subset of the strict polygon-interior cone, there is
   one literal word of length

   \[
   w_4(\boldsymbol\ell)+O(R^2)
   \]

   covering the three central ranks simultaneously.  The lower central
   rank is literal, the middle rank is supplied by adjacent pairs, and the
   upper central rank by consecutive triples.

3. That three-rank word cannot be completed by insertions while retaining
   its literal lower-central spine.  More generally, \(s\) distinct literal
   rank-\(R\) letters together with coverage of rank \(R-1\) force

   \[
   N\ge s+|P_{R-1}|.
   \tag{0.2}
   \]

   For the equal cube this gives the exact wall

   \[
   \boxed{N\ge2M_m-5m-2,}
   \qquad
   M_m=w_4(m,m,m,m).
   \tag{0.3}
   \]

   Hence any full near-width word must factor almost the entire
   lower-central layer nontrivially.

4. The equal cube admits an exact complementary-shell decomposition into
   packets whose widths telescope to \(M_m\).  The following is the
   smallest literal constructive gate isolated here.

   > **Complementary-shell packet lemma — UNPROVED.**  For the packet
   > \(\mathcal A_r\cup\mathcal B_r\) defined in Section 4, construct one
   > literal nonzero ambient word of length
   > \[
   > (r+1)^2+r^2+e_r,
   > \qquad
   > \sum_{r\le R}e_r=o(R^3).
   > \tag{PACK}
   > \]

   PACK implies

   \[
   g_4(R,R,R,R)=M_R+o(R^3).
   \]

The dual attack also reaches a stable conclusion.  Every fixed
macroscopic symmetric-rank-band certificate made from sharp
endpoint-chain intersections, arbitrary monotone coordinate-separable
potentials, arbitrary threshold-dependent cover weights, and cover
disjointness collapses on the equal cube.  The exact finite dual reduces
to a one-dimensional threshold inequality, and that inequality has
strictly negative continuum margin for every fixed band fraction
\(0<x<2\).  Mesoscopic bands \(k=o(t)\), nonseparable spatial weights, and
multi-cover motifs remain outside the proved collapse.

Thus the equal cube remains open, but the remaining positive target for
the recursive shell-fusion line is no longer an unspecified “surface
braid”: it is the literal packet lemma PACK.  A surviving endpoint dual
must leave the macroscopic
coordinate-separable rank-band class isolated in Section 5.

No web search, finite search, or computational experiment is used below.

## 1. A3 as a boundary condition: an interior collar

We first record exactly how far the A3 theorem propagates by monotonicity.
This is a boundary condition for the new attack, not its equal-cube
conclusion.

### Lemma 1.1 (lower-subbox monotonicity)

If \(Q'\) is an origin-anchored coordinate subbox of \(Q\), then

\[
 g(Q)\ge g(Q').
 \tag{1.1}
\]

#### Proof

Start with a universal word for \(Q\) and delete every letter outside
\(Q'\).  If an interval witnesses a target \(x\in Q'\), every letter in
that interval is coordinatewise at most \(x\), hence already lies in
\(Q'\).  The selected interval therefore survives as a contiguous
interval of the restricted word. \(\square\)

### Theorem 1.2 (explicit strict-interior collar)

Let \(1\le d<3\), put

\[
 \lambda=\frac d3,
\]

and take integral sequences with normalized side ratios
\((1,1,1,d)\).  Then

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_4(t,t,t,dt)-w_4(t,t,t,dt)}{t^3}
\ge
\eta(d),}
\tag{1.2}
\]

where rounding changes only \(O(t^2)\), and

\[
\boxed{
\eta(d)=
\frac{561}{512}\left(\frac d3\right)^3
-\left(1-\frac{(3-d)^3}{24}\right).}
\tag{1.3}
\]

Consequently every \(d<3\) sufficiently close to \(3\) has positive cubic
excess.

#### Proof

At the middle rank of

\[
 [0,t]^3\times[0,dt],
\]

projection onto the first three coordinates retains precisely the lattice
points whose normalized coordinate sum lies between

\[
 a=\frac{3-d}{2}
 \quad\text{and}\quad
 3-a.
\]

For \(1\le d\le3\), the two omitted regions are opposite tetrahedra of
volume \(a^3/6\).  Hence

\[
 w_4(t,t,t,dt)
 =
 \left(1-\frac{(3-d)^3}{24}\right)t^3+O(t^2).
 \tag{1.4}
\]

The full box contains the boundary subbox

\[
 [0,\lambda t]^3\times[0,dt],
 \qquad d=3\lambda.
\]

The A3 shoulder theorem, applied with shoulder parameter
\(x=\lambda/2\), gives

\[
 g_4(\lambda t,\lambda t,\lambda t,3\lambda t)
 \ge
 \left(1+\frac{49}{512}\right)\lambda^3t^3+O(t^2).
 \tag{1.5}
\]

Combine (1.1), (1.4), and (1.5). \(\square\)

For the integral ray in (0.1), use the boundary subbox

\[
 [0,35n]^3\times[0,105n]
 \subset
 [0,36n]^3\times[0,105n].
\]

The A3 lower coefficient is

\[
 \frac{561}{512}\,35^3.
\]

The full-box width coefficient is

\[
 36^3-\frac{3^3}{24}=36^3-\frac98.
\]

Their difference is exactly

\[
 \frac{561\cdot35^3}{512}
 -36^3+\frac98
 =\frac{165579}{512},
\]

which proves (0.1).

This argument cannot reach the equal cube.  A single boundary subbox inside
\([0,t]^4\) has normalized short-side sum at most one.  If its three short
sides are \(a,b,c\) and \(a+b+c\le1\), then \(abc\le1/27\).  Moreover the
A3 boundary functional satisfies, for \(0\le x\le\min(a,b,c)\),

\[
 \Gamma(x)
 \le \frac{abc}{3}+\frac{abc}{24}
 =\frac38abc,
\]

because \(x/(a+b+c)\le1/3\) and \(x^3\le abc\).
Thus this single-subbox certificate is at most

\[
 \frac{11}{8}abc\le\frac{11}{216},
\]

far below the equal-cube width coefficient \(2/3\).  Summing several such
certificates would require a new disjoint-resource theorem; monotonicity
alone gives only their maximum.

## 2. A one-word three-central-rank atlas

The next theorem works uniformly on compact subsets of the strict polygon
interior (and exactly whenever its displayed integer hypothesis holds).
It is a positive literal construction, not a shadow or fractional trail.

For a graded box \(P\), write \(P_j\) for its rank-\(j\) layer.

### Lemma 2.1 (vertex-edge-wedge word)

Let \(G\) be a finite simple graph of maximum degree \(\Delta\).  Let

\[
 b=\#\{v:\deg_G(v)\ne2\},
 \qquad c=c(G).
\]

There is one vertex word which contains

1. every vertex as a literal letter;
2. the endpoints of every edge as an adjacent pair; and
3. for every wedge \(u-v-w\), with \(u\ne w\), one of
   \(u,v,w\) or \(w,v,u\) as a consecutive triple,

and whose length is at most

\[
\boxed{
 |E(G)|
 +\left(\frac{\Delta}{2}
       +3\binom{\Delta}{2}\right)b
 +2c.}
\tag{2.1}
\]

#### Proof

Let \(X=\{v:\deg v\ne2\}\).  Suppress the maximal degree-two threads.
Every noncycle thread has two incidences with \(X\), so there are at most
\(\Delta b/2\) such threads.  Write each thread once as its complete vertex
sequence.  Every component consisting entirely of degree-two vertices is
a cycle; write its cyclic sequence and repeat its first two vertices.
Append isolated vertices when necessary.  The total cost so far is at most

\[
 |E(G)|+\frac{\Delta b}{2}+2c.
\]

This covers every edge and every wedge centered at a degree-two vertex.
For each \(x\in X\) and each unordered pair of distinct neighbors
\(\{u,w\}\), append the triple \(u,x,w\).  The added cost is at most

\[
 3b\binom{\Delta}{2}.
\]

Concatenating the blocks creates only additional irrelevant maxima.
This proves (2.1). \(\square\)

### Theorem 2.2 (three-layer atlas)

Let

\[
 P=\prod_{i=1}^4[0,\ell_i],
 \qquad
 S=\sum_i\ell_i,
 \qquad
 r=\left\lfloor\frac S2\right\rfloor,
\]

and assume

\[
 \max_i\ell_i<r.
 \tag{2.2}
\]

If every side is \(O(R)\), there is one literal range-maximum word of
length

\[
\boxed{w_4(\boldsymbol\ell)+O(R^2)}
\tag{2.3}
\]

covering every target in

\[
 P_{r-1}\cup P_r\cup P_{r+1}.
\]

All letters of the word lie in \(P_{r-1}\).  Rank \(r-1\) is covered by
singletons, rank \(r\) by adjacent pairs, and rank \(r+1\) by consecutive
triples.

The \(O(R^2)\) constant is uniform when the normalized side vector ranges
over a compact subset of the strict polygon-interior cone

\[
 \max_i\ell_i<\sum_{j\ne i}\ell_j.
\]

#### Proof

Make \(P_{r-1}\) the vertex set of a graph.  For each
\(z\in P_r\), let \(p<q\) be its first two positive coordinates and insert

\[
 e_z=\{z-e_p,z-e_q\}.
 \tag{2.4}
\]

Condition (2.2) ensures that a rank-\(r\) point cannot be supported on one
coordinate, so the edge is defined.  It is simple, and distinct targets
give distinct edges because

\[
 (z-e_p)\vee(z-e_q)=z.
 \tag{2.5}
\]

Thus

\[
 |E(G)|=|P_r|=w_4(\boldsymbol\ell).
 \tag{2.6}
\]

Every vertex has degree at most four.  Outside

\[
 \mathcal B=
 \{v:v_1\in\{0,\ell_1\}
       \text{ or }v_2\in\{0,\ell_2\}\},
 \tag{2.7}
\]

the two edges selected from \(v+e_1\) and \(v+e_2\) are incident with
\(v\), while edges selected from \(v+e_3\) and \(v+e_4\) are not.
Therefore every vertex outside \(\mathcal B\) has degree exactly two.
Fixing \((v_3,v_4)\), the induced graph outside \(\mathcal B\) is one
possibly empty coordinate-\(\{1,2\}\) path.  Consequently

\[
 b=O(R^2),
 \qquad
 c(G)=O(R^2).
 \tag{2.8}
\]

Apply Lemma 2.1.  Singleton letters cover \(P_{r-1}\), and (2.5) shows
that the adjacent pairs cover \(P_r\).

It remains to check rank \(r+1\).  For \(y\in P_{r+1}\), let \(a<b\) be
its first two positive coordinates and put

\[
 z_a=y-e_a,
 \qquad
 z_b=y-e_b,
 \qquad
 v=y-e_a-e_b.
\]

If \(y\) has at least three positive coordinates, both \(z_a,z_b\) have
at least two.  If \(y\) has exactly two, a failure would make one of
\(z_a,z_b\) a rank-\(r\) point supported on one coordinate, contradicting
(2.2).  The selected edge \(e_{z_a}\) contains \(v\), as does
\(e_{z_b}\).  They are distinct and form a wedge centered at \(v\).
The corresponding consecutive triple has maximum

\[
 z_a\vee z_b=y.
\]

This proves the theorem. \(\square\)

### Equal-cube constant

For \(P=[0,m]^4\), put \(M_m=|P_{2m}|\).  The exceptional set satisfies

\[
 |\mathcal B|
 \le
 2\left[
 \binom{2m+1}{2}+\binom{m+1}{2}
 \right]
 =5m^2+3m.
\]

Also

\[
 c(G)\le(m+1)^2+|\mathcal B|.
\]

Since \(\Delta=4\), Lemma 2.1 yields the explicit bound

\[
\boxed{
 L\le M_m+112m^2+70m+2.}
\tag{2.9}
\]

The constant is deliberately crude; the surface order is the point.

## 3. The literal-spine wall

The preceding atlas is not a viable immutable spine for a full near-width
word.

### Theorem 3.1 (singleton-spine barrier)

Let a range-maximum word in a graded product box contain \(s\) distinct
rank-\(R\) targets as literal letters and cover every target in rank
\(R-1\).  Then

\[
\boxed{N\ge s+|P_{R-1}|.}
\tag{3.1}
\]

#### Proof

Choose one witnessing interval for every rank-\((R-1)\) target.  None can
contain a rank-\(R\) literal position, because its maximum would then have
rank at least \(R\).

Two distinct equal-rank targets cannot have selected witnesses with the
same left endpoint.  Such intervals are nested by their right endpoints,
so their maxima are comparable; equal rank would force them to be equal.
The \(|P_{R-1}|\) witnesses therefore have distinct left endpoints, all
outside the \(s\) counted literal positions.  Hence

\[
 N-s\ge|P_{R-1}|.
\]

\(\square\)

### Corollary 3.2 (exact equal-cube wall)

For the equal cube,

\[
 |P_{2m-1}|=M_m-(m+1),
 \qquad
 |P_{2m-2}|=M_m-(4m+1).
 \tag{3.2}
\]

Every word which retains all rank-\((2m-1)\) points literally and also
covers rank \(2m-2\) satisfies

\[
\boxed{N\ge2M_m-5m-2.}
\tag{3.3}
\]

Thus the direct-line word, every Euler-trail two-layer word, and the
three-layer atlas cannot be completed to coefficient one merely by
insertion, reordering, or seam repair while retaining their literal
lower-central letters.

More generally, if \(N=M_m+o(M_m)\), Theorem 3.1 and (3.2) imply that only
\(o(M_m)\) distinct rank-\((2m-1)\) targets may occur literally.  Almost
the entire lower-central layer must itself be represented as nontrivial
factor maxima.

This is an architecture-specific obstruction.  It does not lower-bound an
unrestricted word which already factors that layer.

## 4. The exact complementary-shell packet reduction

The singleton wall suggests recursing through target packets rather than
retaining one literal central spine.

Let

\[
 S_r=[0,r]^2
\]

and split it into

\[
 H_r=
 \{(0,j):0\le j\le r\}
 \cup
 \{(i,r):1\le i\le r\},
 \tag{4.1}
\]

and

\[
 I_r=
 \{1,\ldots,r\}\times\{0,\ldots,r-1\}
 =(1,0)+S_{r-1}.
 \tag{4.2}
\]

The set \(H_r\) is the saturated chain

\[
 (0,0)<(0,1)<\cdots<(0,r)<(1,r)<\cdots<(r,r)
\]

of edge height \(2r\), and

\[
 S_r=H_r\mathbin{\dot\cup}I_r.
\]

Define disjoint target packets

\[
 \mathcal A_r=S_r\times H_r,
 \qquad
 \mathcal B_r=H_r\times I_r.
 \tag{4.3}
\]

Then

\[
\boxed{
 S_r\times S_r
 =
 \mathcal A_r
 \mathbin{\dot\cup}
 \mathcal B_r
 \mathbin{\dot\cup}
 (I_r\times I_r).}
\tag{4.4}
\]

### Lemma 4.1 (iterated packet peel)

Put

\[
 \tau_r=(R-r,0,R-r,0).
\]

Then

\[
\boxed{
 [0,R]^4
 =
 \{\tau_0\}
 \mathbin{\dot\cup}
 \bigdotcup_{r=1}^R
 \tau_r(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r).}
\tag{4.5}
\]

#### Proof

Equation (4.4) is the expansion

\[
 (H_r\dot\cup I_r)\times(H_r\dot\cup I_r),
\]

with the first two terms grouped according to whether the second factor
lies in \(H_r\), or instead lies in \(I_r\) while the first lies in
\(H_r\).  Moreover,

\[
 \tau_r+(I_r\times I_r)
 =
 \tau_{r-1}+(S_{r-1}\times S_{r-1}).
\]

Iterate down to \(r=0\). \(\square\)

### Lemma 4.2 (exact packet width ledger)

The two packets have aligned middle layers and

\[
\boxed{
 w(\mathcal A_r)=(r+1)^2,
 \qquad
 w(\mathcal B_r)=r^2.}
\tag{4.6}
\]

Consequently

\[
\boxed{
 M_R
 =
 1+\sum_{r=1}^R\bigl((r+1)^2+r^2\bigr).}
\tag{4.7}
\]

#### Proof

Since \(H_r\cong[0,2r]\),

\[
 \mathcal A_r\cong[0,r]^2\times[0,2r],
\]

whose width is \((r+1)^2\).  Also

\[
 \mathcal B_r
 \cong
 [0,2r]\times[0,r-1]^2
\]

after a rank-one translation, so its width is \(r^2\).  The abstract
middle rank of \(\mathcal B_r\) becomes ambient local rank \(2r\), the
same as that of \(\mathcal A_r\).  Translation by \(\tau_r\) moves both
to global rank \(2R\).  The terminal \(\tau_0=(R,0,R,0)\) also has rank
\(2R\).  Thus (4.5) partitions the global middle layer and proves (4.7).
\(\square\)

### Theorem 4.3 (PACK implies the equal-cube estimate)

For each \(r\), suppose one nonzero ambient \([0,r]^4\) word covers every
nonzero target in

\[
 \mathcal A_r\cup\mathcal B_r
\]

and has length

\[
 (r+1)^2+r^2+e_r.
 \tag{4.8}
\]

If

\[
 \sum_{r\le R}e_r=o(R^3),
 \tag{4.9}
\]

then

\[
\boxed{
 g_4(R,R,R,R)\le M_R+o(R^3).}
\tag{4.10}
\]

In particular, the pointwise condition \(e_r=o(r^2)\) suffices.

#### Proof

Translate the \(r\)-packet word by \(\tau_r\) and concatenate the translated
blocks.  Translation commutes with coordinatewise maximum, and no
insertion is made inside a packet block, so every internal selected witness
survives.

The local packet word omits its local zero.  For \(1\le r<R\), that zero
translates to the nonzero parent target \(\tau_r\), so append it once.  For
\(r=R\), it is the excluded global zero and must not be appended.  Finally
append the terminal target \(\tau_0\).  There are \(R\) appended singleton
origins in total.

The packet baseline widths sum to \(M_R-1\), so the resulting length is

\[
 (M_R-1)+\sum_{r=1}^Re_r+R
 =
 M_R+\sum_{r=1}^Re_r+R-1.
\]

Every nonzero target belongs to exactly one translated packet or is one of
the appended origins, by (4.5).  This proves (4.10).  The final assertion
is weighted Cesàro summation. \(\square\)

The condition (4.8) is asymptotically sharp: the aligned packet middle
layers form an antichain of size

\[
 (r+1)^2+r^2.
\]

It is essential that PACK asks for **one literal word for the union**.
Servicing \(\mathcal A_r\) and \(\mathcal B_r\) separately cannot work.
Indeed, A3 gives quadratic excess on

\[
 \mathcal A_r\cong[0,r]^2\times[0,2r].
\]

For \(\mathcal B_r\), the boundary subbox

\[
 [0,2r-2]\times[0,r-1]^2
\]

already has the same width \(r^2\) and quadratic A3 excess.  Thus separate
payment incurs \(\Omega(r^2)\) extra length.  The packet lemma must fuse
the two complementary orientations at leading order.

## 5. What the endpoint dual can and cannot do at equality

The A3 proof uses two orthogonal endpoint-chain partitions, a linear
transverse potential, and competition for coordinate covers.  On the equal
cube, every fixed macroscopic symmetric-band extension of that mechanism
within the precise separable class below collapses.

### 5.1 Collapse of all linear coordinate-potential band duals

Let

\[
 X_t=[0,t]^4,
 \qquad
 W_t=w(X_t)=\frac23t^3+O(t^2),
\]

and retain the symmetric band

\[
 2t-k\le |x|\le2t+k,
 \qquad \frac kt\to x\in[0,2).
\]

Let \(f_4\) be the density of the sum of four independent uniform
\([0,1]\) variables, and set

\[
 f(v)=f_4(2-v).
\]

For \(0\le v\le1\),

\[
 f(v)=\frac23-v^2+\frac12v^3.
 \tag{5.1}
\]

Define

\[
 \mathcal A(x)=2\int_0^x f(v)\,dv,
 \tag{5.2}
\]

\[
 \mathcal F(x)=
 2\int_0^x
 \left(2f(v)-\frac23\right)_+\,dv,
 \tag{5.3}
\]

and

\[
 U(x)=
 \frac23+\left(\frac x2-1\right)f(x).
 \tag{5.4}
\]

Here, to leading order:

* \(\mathcal A(x)t^4\) is the band population and also the cover capacity
  in any one coordinate direction;
* \(\mathcal F(x)t^4\) is the sharp adjacent-layer cover demand in one
  endpoint partition when the chain count is \(W_t+o(t^3)\); and
* \(U(x)t^4\) is the budget for one unit linear coordinate potential.

### Proposition 5.1 (the A3-style linear numerator is negative)

For every fixed \(x\in(0,2)\) and every nonzero common left/right choice
of nonnegative coordinate-type weights, the direct A3-style weighted
cover-minus-linear-potential numerator is strictly negative at leading
order.

#### Proof

First use the same coordinate weights on both endpoint partitions.
Normalize them as

\[
 c_i\ge0,\qquad
 \max_i c_i=1,\qquad
 s=\sum_i c_i\in[1,4].
\]

Put \(a_i=1-c_i\).  If \(e_i\) is the number of used covers in coordinate
\(i\), then

\[
 \sum_i c_i e_i
 =
 \sum_i e_i-\sum_i a_i e_i.
\]

The total-cover lower bound and the linear-potential upper bound therefore
force, in one endpoint partition,

\[
 \sum_i c_i e_i
 \ge
 \bigl(\mathcal F(x)-(4-s)U(x)\bigr)t^4+o(t^4).
 \tag{5.5}
\]

For two orthogonal endpoint partitions, the weighted capacity is
\(s\mathcal A(x)t^4+o(t^4)\).  Thus the leading violation margin is

\[
 G_s(x)=
 2\mathcal F(x)-2(4-s)U(x)-s\mathcal A(x).
 \tag{5.6}
\]

Let \(x_0\in(0,1)\) be the unique solution of \(f(x_0)=1/3\).
For \(0\le x\le x_0\),

\[
 \mathcal F(x)=2\mathcal A(x)-\frac{4x}{3},
\]

and

\[
 G_s(x)
 =(4-s)h(x)-\frac{8x}{3},
 \tag{5.7}
\]

where

\[
 h(x)=\mathcal A(x)-2U(x)
 =\frac{2x}{3}-2x^2+\frac{4x^3}{3}-\frac{x^4}{4}.
 \tag{5.8}
\]

Since

\[
 h(x)
 =
 \frac{2x}{3}
 -x^2\left(2-\frac{4x}{3}+\frac{x^2}{4}\right)
 \le\frac{2x}{3},
\]

we get

\[
 G_s(x)\le-\frac{2sx}{3}<0
 \qquad(x>0).
 \tag{5.9}
\]

For \(x\ge x_0\), the positive-part integral \(\mathcal F\) is constant,
while

\[
 \mathcal A'(x)=2f(x)>0,
\]

and

\[
 U'(x)
 =\frac12f(x)+\left(\frac x2-1\right)f'(x)>0.
\]

Hence \(G_s\) is strictly decreasing and remains negative.  At \(x=0\)
every leading quantity vanishes. \(\square\)

Negativity of this particular lower-bound numerator alone would not
exclude a stronger weighted demand hidden by the potential estimate.
The exact finite relaxation and the required side/coordinate
symmetrizations are handled next.

### 5.2 Exact reduction for monotone separable potentials

Retain the finite symmetric band with lower and upper ranks

\[
 L=2t-k,\qquad U=2t+k.
\]

Let \(M_j=|(X_t)_j|\), \(W=W_t\), and \(b=M_L=M_U\).  Define

\[
 F_{t,k}
 =
 \sum_{j=L}^{U-1}[M_j+M_{j+1}-W]_+.
 \tag{5.10}
\]

For a fixed coordinate and threshold \(0\le q<t\), let \(A_q\) be the
number of band covers crossing

\[
 q\longrightarrow q+1.
\]

Put

\[
 \Delta_q
 =
 \#\{x\in(X_t)_U:x_i>q\}
 -\#\{x\in(X_t)_L:x_i>q\},
\]

and

\[
 u_q=\Delta_q+(W-b).
 \tag{5.11}
\]

### Theorem 5.2 (exact positivity criterion for the threshold LP)

Within the relaxation consisting of arbitrary monotone
coordinate-separable potentials, arbitrary threshold-dependent coordinate
cover weights, the aggregate forced-cover constraints, and cover
disjointness, a strict certificate exists if and only if
\(\mathcal G_{t,k}>0\), where

\[
\boxed{
 \mathcal G_{t,k}
 =
 2F_{t,k}
 -4\sum_{q=0}^{t-1}\min\{A_q,2u_q\}.}
\tag{5.12}
\]

When \(\mathcal G_{t,k}>0\), its value is an explicitly attained separating
margin.  When \(\mathcal G_{t,k}\le0\), the aggregate real relaxation is
feasible; this does not assert the existence of actual endpoint-chain
partitions.

#### Proof

For coordinate \(i\), every monotone one-coordinate potential is a
nonnegative combination of the step potentials

\[
 \psi_{i,q}(z)=\mathbf1_{\{z_i>q\}}.
\]

It increments exactly on a coordinate-\(i\) cover crossing
\(q\to q+1\).  If \(e_{i,q}\) counts a selected set of the covers forced
in one endpoint partition, telescoping \(\psi_{i,q}\) gives

\[
 0\le e_{i,q}\le u_q,
 \qquad
 \sum_{i,q}e_{i,q}\ge F_{t,k}.
 \tag{5.12a}
\]

Indeed, the top and bottom chains contribute \(\Delta_q\); the
\(W-b\) chains not ending on the top boundary contribute at most one
additional unit each, while internal minima only subtract.

Let atoms be \(a=(i,q)\), with \(u_a=u_q\) and \(A_a=A_q\), and put

\[
 \mathcal P=
 \left\{
 e:0\le e_a\le u_a,\quad\sum_a e_a\ge F_{t,k}
 \right\}.
 \tag{5.12b}
\]

The left and right forced-cover sets are disjoint, so

\[
 e_a^L+e_a^R\le A_a.
 \tag{5.12c}
\]

The two-side aggregate relaxation is feasible exactly when

\[
 F_{t,k}
 \le
 \sum_a\min\{u_a,A_a/2\}
 =
 4\sum_q\min\{u_q,A_q/2\}.
 \tag{5.12d}
\]

For necessity, average \(e^L,e^R\).  Conversely, a vector bounded by
\(\min(u_a,A_a/2)\) may be used on both sides.

For completeness, define

\[
 m(c)=\min_{e\in\mathcal P}\langle c,e\rangle.
\]

With side-specific nonnegative weights, the separating margin is

\[
 \Phi(c^L,c^R)
 =
 m(c^L)+m(c^R)
 -\sum_aA_a\max(c_a^L,c_a^R).
 \tag{5.12e}
\]

If \(\bar c=(c^L+c^R)/2\), concavity of \(m\) and
\(\bar c_a\le\max(c_a^L,c_a^R)\) show

\[
 \Phi(\bar c,\bar c)\ge\Phi(c^L,c^R).
\]

Averaging over coordinate permutations similarly removes coordinate
asymmetry.  If one side is written in complemented coordinates, first
reindex its threshold by \(q\mapsto t-1-q\).

Finally, (5.12d) fails exactly when \(\mathcal G_{t,k}>0\).  In that case
the symmetric bang-bang weights

\[
 c_q=
 \begin{cases}
  1,&A_q<2u_q,\\
  0,&A_q\ge2u_q.
 \end{cases}
\]

attain the displayed separating value. \(\square\)

For \(k/t\to x\), let \(g=f_3\) be the density of the sum of three
independent uniform variables and define

\[
 A_x(y)=
 \int_{2-x-y}^{2+x-y}g(s)\,ds,
 \tag{5.13}
\]

\[
 D_x(y)=
 \int_y^1
 [g(2+x-z)-g(2-x-z)]\,dz,
\]

\[
 u_x(y)=D_x(y)+\frac23-f(x).
 \tag{5.14}
\]

Then the normalized margin is

\[
\boxed{
 \mathcal G_{\rm sep}(x)
 =
 2\mathcal F(x)
 -4\int_0^1
 \min\{A_x(y),2u_x(y)\}\,dy.}
\tag{5.15}
\]

The continuum sign can in fact be settled exactly.

### Theorem 5.3 (macroscopic separable-potential collapse)

For every fixed \(0<x<2\),

\[
\boxed{\mathcal G_{\rm sep}(x)<0.}
\tag{5.16}
\]

At \(x=0\), equality holds.  Consequently no fixed macroscopic symmetric
band gives a strict certificate within the complete monotone
coordinate-separable threshold class of Theorem 5.2.

#### Proof

Extend \(g=f_3\) by zero outside \([0,3]\), and abbreviate

\[
 a_x(y)=A_x(y).
\]

For \(0\le x\le1\), put

\[
 L_x=\int_{1-x}^{1}g(s)\,ds
 =\frac{1-(1-x)^3}{6}.
 \tag{5.17}
\]

Since \(\partial_y a_x=\partial_yD_x\) and \(D_x(1)=0\), direct boundary
evaluation gives

\[
 u_x(y)=a_x(y)-2L_x.
 \tag{5.18}
\]

Explicitly,

\[
 a_x(1)-2L_x=\frac23-f(x),
\]

so (5.18) follows from (5.14).

Integrating the three quadratic pieces of \(g\) gives

\[
\begin{aligned}
 a_x(y)={}&
 x(1+2y-2y^2)-\frac23x^3\\
 &+\frac12(x-y)_+^3
 +\frac12(x+y-1)_+^3.
\end{aligned}
\tag{5.19}
\]

Therefore

\[
\begin{aligned}
 d_x(y)
 &:=
 a_x(y)-2u_x(y)\\
 &=
 x(1-2y+2y^2)-2x^2+\frac43x^3\\
 &\quad-\frac12(x-y)_+^3
       -\frac12(x+y-1)_+^3.
\end{aligned}
\tag{5.20}
\]

Let \(x_0\in(0,1)\) be defined by \(f(x_0)=1/3\).  If
\(0<x\le x_0\), then

\[
 (d_x(y))_+
 <
 x(1-2y+2y^2),
\]

because \(-2x^2+4x^3/3<0\) and the two cubic positive-part terms in
(5.20) are subtracted.  Hence

\[
 \int_0^1(d_x(y))_+\,dy<\frac{2x}{3}.
 \tag{5.21}
\]

Also

\[
 \int_0^1a_x(y)\,dy=\mathcal A(x),
\]

and, in this range,

\[
 \frac{\mathcal F(x)}2
 =\mathcal A(x)-\frac{2x}{3}.
\]

Since

\[
 \min\{a_x,2u_x\}=a_x-(d_x)_+,
\]

equation (5.21) yields

\[
 \int_0^1\min\{a_x(y),2u_x(y)\}\,dy
 >
 \frac{\mathcal F(x)}2.
 \tag{5.22}
\]

For \(x\ge x_0\), the function \(\mathcal F(x)\) is constant.  Both
\(a_x(y)\) and \(u_x(y)\) are pointwise nondecreasing.  For
\(x_0\le x\le1\),

\[
 \partial_xu_x(y)
 =
 g(2-x-y)+g(2+x-y)-2g(1-x)\ge0.
 \tag{5.23}
\]

Indeed, reflect the second argument through \(3/2\).  Both resulting
arguments lie in \([1-x,2-x]\subset[0,3/2]\), where the symmetric
unimodal density \(g\) is at least \(g(1-x)\); here \(x_0>1/2\).
For \(1\le x<2\),

\[
 u_x(y)=a_x(y)-\frac13,
\]

because \(a_x(1)=1-f(x)\).  Widening the integration interval makes
\(a_x(y)\) nondecreasing.
Thus the left side of (5.22) is nondecreasing, while its right side is
constant, so the strict inequality persists.  Substitution in (5.15)
proves (5.16). \(\square\)

For \(k/t\to x\in(0,2)\),

\[
 \mathcal G_{t,k}
 =
 t^4\mathcal G_{\rm sep}(x)+o(t^4)<0.
\]

Fixed-dimensional inclusion-exclusion gives \(O(t^2)\) errors in each
rank or threshold count and hence \(o(t^4)\) after the \(O(t)\) summation,
which justifies this passage to the continuum.

This completes the collapse for every fixed macroscopic symmetric band.
It does **not** settle mesoscopic bands \(k=o(t)\): small total cover scale
alone does not control the coefficient converting a ledger into word
excess.  Nonseparable spatial weights, cross-threshold correlations,
nonlinear multi-coordinate potentials, and multi-cover motifs also remain
outside Theorem 5.2.

## 6. Best current full word and exact implication scope

The strongest certified complete literal word in the audited portfolio is
the three-short-side SCD connector:

\[
 B_m=(m+1)^3
 +m\bigl((m+1)^2-\Psi(m)\bigr)-1,
\]

where

\[
 \Psi(m)=
 \left\lceil\frac m2\right\rceil
 \left(\left\lfloor\frac m2\right\rfloor+1\right).
\]

Its exact parity forms are

\[
 B_m=
 \begin{cases}
 \dfrac74m^3+\dfrac92m^2+4m,
     &m\ \text{even},\\[2mm]
 \dfrac74m^3+\dfrac92m^2+\dfrac{15}{4}m,
     &m\ \text{odd}.
 \end{cases}
 \tag{6.1}
\]

The exact equal-cube width is

\[
 M_m=
 \frac{2m^3+6m^2+7m+3}{3}.
 \tag{6.2}
\]

Therefore

\[
 B_m-M_m=\frac{13}{12}m^3+O(m^2),
\qquad
 \frac{B_m}{M_m}\longrightarrow\frac{21}{8}.
 \tag{6.3}
\]

The connector is sharp only in the architecture assigning a separate
internal rectangle word to every three-short-side symmetric chain.  It is
not a lower bound on unrestricted \(g_4\).

A normalization warning is necessary.  The previously recorded
“\(7/4\)” selective triangular ledger means

\[
 \frac74M_m+O(m^2)=\frac76m^3+O(m^2);
\]

it is a tail-shadow/provider ledger, not a complete max-word.  It is not
the same as the literal full-word bound
\((7/4)m^3+O(m^2)\).

The strongest near-width complete-band word covers

\[
 \bigl||x|-2m\bigr|\le D
\]

with length

\[
 M_m+D(11m^2+13m+3).
 \tag{6.4}
\]

Thus every \(D=o(m)\) band has a width-plus-\(o(m^3)\) word.  At linear
depth, its canonical fixed-delay peak padding is already
\(\Theta(m^3)\); this is architecture-specific.

## 7. Adversarial audit and final ledger

### Independently checked points

1. **A3 scope.**  Section 1 uses A3 only on a genuine boundary subbox and
   invokes a separately proved monotonicity lemma.  It does not relabel
   the equal cube as a boundary box.

2. **Three-layer word.**  The graph construction gives one physical vertex
   word.  Pair and wedge occurrences are consecutive inside that same
   word; no separate rankwise trails are being added after the fact.

3. **Wedge distinctness.**  The two selected edges below a rank-\(r+1\)
   target are distinct and share the stated rank-\((r-1)\) vertex.
   Condition (2.2) rules out a one-supported intermediate central target.

4. **Singleton barrier.**  The lower-rank selected intervals have distinct
   left endpoints, and none may contain any counted higher-rank literal
   position.  Repeated copies cannot reduce the lower bound.

5. **Packet origins.**  There are \(R\) appended singleton origins, while
   the packet widths sum to \(M_R-1\).  The final length is therefore
   \(M_R+\sum e_r+R-1\), not \(M_R+\sum e_r+R\).

6. **Packet scope.**  PACK requires one literal word for
   \(\mathcal A_r\cup\mathcal B_r\).  Separate factors, a fractional
   endpoint assignment, or separate words at different depths do not
   satisfy it.

7. **Linear dual.**  The potential budget, coordinate capacity,
   polynomial \(h(x)\), and negativity of the direct A3-style numerator
   were reconstructed independently.

8. **Separable LP.**  The finite positivity criterion was checked through
   both its primal feasibility condition and its concave weight
   symmetrization.  The continuum inequality (5.16) was then independently
   derived from the explicit \(f_3\) density.  The result is restricted to
   fixed macroscopic symmetric bands; mesoscopic and nonseparable spatial
   duals are not declared dead.

### Unconditional theorem ledger

This report proves:

* the strict-interior collar lower bound (1.2), including (0.1);
* the graph word lemma and the three-central-rank atlas;
* the singleton-spine barrier and exact equal-cube wall;
* the complementary-shell peel, aligned packet widths, and the implication
  PACK \(\Rightarrow g_4(R,R,R,R)=M_R+o(R^3)\);
* the exact threshold LP positivity criterion; and
* collapse of every fixed macroscopic symmetric-band endpoint dual using
  monotone coordinate-separable potentials and threshold-dependent cover
  weights.

### Explicitly unproved

1. **PACK**, the one-word near-combined-width complementary-shell packet.
2. The equal-cube estimate itself.
3. A collapse theorem or positive certificate for mesoscopic,
   nonseparable-spatial, or multi-cover endpoint duals.
4. Any uniform full-box theorem on compact subsets separated from the A3
   collar.

The construction and obstruction attacks meet at the same structural
point.  Separate dominant pieces have A3 excess; fusing them has enough
quadratic raw seam capacity, but the chronology must simultaneously
realize upper joins, lower pins, and two orthogonal endpoint systems.
No current theorem proves that this can or cannot be done.
