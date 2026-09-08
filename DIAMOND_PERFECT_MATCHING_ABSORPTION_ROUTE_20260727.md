# The coloured-diamond perfect-matching route: exact audit

Date: 2026-07-27

## 0. Outcome

Put

\[
 v=2r-1,
 \qquad {\cal L}=\binom{[v]}{r-1},
 \quad {\cal M}=\binom{[v]}r,
 \quad {\cal U}=\binom{[v]}{r+1},
 \quad W=|{\cal L}|=|{\cal M}|.
\]

The four-partite diamond encoding is exact.  Its full degree and codegree
calculus is especially favourable: after a quasirandom choice of the
Catalan excess design, all degrees are \((1+o(1))r(r+1)\) and the maximum
codegree is \(O(r)\).  Consequently the ordinary fixed-uniformity nibble
gives a matching missing only \(o(W)\) vertices.  This proves an
asymptotic **near-factor inside a prescribed upper-slot catalogue**: all
but \(o(W)\) of those prescribed slots are used.  It does not yet realize
the load vector exactly.

It does not give a perfect matching.  Exactness has three additional
obstructions which a degree--codegree theorem does not see.

1.  The prescribed upper loads must satisfy an exact point lattice
    identity.
2.  Their pair degrees must dominate an exact Catalan floor.  The difference
    is the forced inventory of coordinate-swap pairs.
3.  Even after those tests, all Farkas/space cuts and the residual matching
    lattice remain to be controlled.

The alpha and octahedral trades do give genuine small absorbers, but only
for a residual which is already a disjoint union of legal diamond edges.
They are zero-marginal trades and cannot by themselves turn an arbitrary
balanced leftover into legal edges.  Thus there is currently no justified
black-box absorption theorem which upgrades the near-factor below to an
exact prescribed-load factor.  The missing statement is a tailored
cover-down theorem, not another codegree estimate.

## 1. Exact four-partite encoding

Let

\[
 w:{\cal U}\longrightarrow\mathbb Z_{\ge1},
 \qquad \sum_{A\in{\cal U}}w(A)=W.
 \tag{1.1}
\]

Create four parts of size \(W\):

\[
 P_L={\cal L},\qquad
 P_U=\{(A,s):1\le s\le w(A)\},\qquad
 P_0={\cal M}\times\{0\},\qquad
 P_1={\cal M}\times\{1\}.
\]

For a Boolean diamond \(X\subset A\), let its two intermediate sets be
\(Y=X+a\) and \(Z=X+b\), where \(A\setminus X=\{a,b\}\).  For every slot
\((A,s)\), insert the two hyperedges

\[
 \{X,(A,s),(Y,0),(Z,1)\},\qquad
 \{X,(A,s),(Z,0),(Y,1)\}.
 \tag{1.2}
\]

Call the resulting 4-partite 4-graph \({\cal H}_w\).

### Theorem 1.1 (exact equivalence)

\({\cal H}_w\) has a perfect matching if and only if there is a spanning
lower-rainbow 2-factor on \({\cal M}\) whose upper-union load vector is
exactly \(w\).

#### Proof

A perfect matching chooses one diamond at every lower vertex and every
upper slot.  Each middle set occurs once as a 0-clone and once as a 1-clone,
so orienting from the 0-clone to the 1-clone gives indegree and outdegree
one.  Conversely orient every cycle of a prescribed 2-factor and assign
the occurrences of each upper colour bijectively to its slots.  This gives
a perfect matching of (1.2).  \(\square\)

This encoding contains only genuine Boolean diamonds.  It has none of the
wildcard or completion vertices which invalidated the earlier full-band
matching proposal.

## 2. Exact degrees and codegrees

Now specialize to a simple excess family

\[
 D\subseteq{\cal U},\qquad w(A)=1+\mathbf1_D(A),\qquad |D|=C_r,
 \tag{2.1}
\]

where \(C_j=\frac1{j+1}\binom{2j}{j}\).  Write

\[
 d_D(X)=|\{A\in D:X\subset A\}|,
 \qquad
 d_D(Y)=|\{A\in D:Y\subset A\}|.
\]

### Proposition 2.1 (degrees)

The vertex degrees are

\[
\begin{aligned}
 d(X)&=r(r-1)+2d_D(X), &&X\in{\cal L},\\
 d(A,s)&=r(r+1),       &&(A,s)\in P_U,\\
 d(Y,0)=d(Y,1)&=r(r-1)+r\,d_D(Y), &&Y\in{\cal M}.
\end{aligned}
\tag{2.2}
\]

Their averages are all exactly

\[
 R:=r(r+1),
 \tag{2.3}
\]

because

\[
 \mathbb E_Xd_D(X)=r,
 \qquad
 \mathbb E_Yd_D(Y)=2.
 \tag{2.4}
\]

### Proposition 2.2 (complete pair-codegree table)

Pairs in the same part have codegree zero.  For pairs in distinct parts:

\[
\begin{array}{c|c}
\text{pair}&\text{codegree}\\ \hline
X,(A,s)&2\mathbf1_{X\subset A}\\
X,(Y,\epsilon)&(r-1+d_D(Y))\mathbf1_{X\subset Y}\\
(A,s),(Y,\epsilon)&r\mathbf1_{Y\subset A}\\
(Y,0),(Z,1)&w(Y\cup Z)\mathbf1_{|Y\cap Z|=r-1}.
\end{array}
\tag{2.5}
\]

In the last line \(Y=Z\) gives zero.  In particular, if

\[
 \max_Yd_D(Y)=o(r),
 \tag{2.6}
\]

then \(\Delta_2({\cal H}_w)=O(r)=o(R)\).  Notice that the deliberately
duplicated upper slot causes no large codegree; its codegree with a lower
vertex is exactly two.

The calculation also identifies the nonregularity correctly.  The upper
part is exactly regular.  The lower part is near-regular as soon as
\(\max_Xd_D(X)=o(r^2)\), and the middle-clone parts are near-regular as soon
as (2.6) holds.

One must not replace near-regularity by the formally cleaner condition
\(d_D(Y)=2\) for every middle set.  That condition would indeed imply
\(d_D(X)=r\) for every lower set (double-count the two intermediate sets
between \(X\) and each \(A\)), making the entire 4-graph exactly regular.
But it is already impossible at \(r=4,v=7\): after complementation it asks
for a graph on seven vertices having exactly two selected edges in every
triangle.  A monochromatic triangle in the selected/unselected two-colouring
contradicts this.  Thus a viable exact theorem must genuinely tolerate
nonregular degrees.

## 3. Exact lattice and capacity barriers

Every diamond obeys, coordinatewise,

\[
 \mathbf1_Y+\mathbf1_Z=\mathbf1_X+\mathbf1_A.
 \tag{3.1}
\]

This produces an exact lattice obstruction which survives all averaging.

### Theorem 3.1 (point identity)

If \({\cal H}_{1+\mathbf1_D}\) has a perfect matching, then

\[
 \boxed{d_D(x)=2C_{r-1}\quad(x\in[v]).}
 \tag{3.2}
\]

#### Proof

Sum (3.1) over a perfect matching and compare the known point degrees of
the complete levels.  Equivalently,

\[
 \binom{2r-2}{r}+d_D(x)
 =2\binom{2r-2}{r-1}-\binom{2r-2}{r-2},
\]

which reduces to (3.2).  \(\square\)

Thus equal part sizes and Catalan cardinality are not the complete
divisibility conditions.  A prescribed excess family which is not point
regular is impossible, however favourable the degrees and codegrees of the
ambient catalogue may appear.

There is a sharper second-order obstruction.  Let \(h_{ij}\) be the number
of selected diamonds whose two exchanged coordinates are exactly
\(\{i,j\}\).

### Theorem 3.2 (forced swap-pair inventory)

Every perfect matching must satisfy

\[
 \boxed{h_{ij}=d_D(\{i,j\})-C_{r-1}\ge0.}
 \tag{3.3}
\]

Moreover, under (3.2),

\[
 \sum_{j\ne i}h_{ij}=2C_{r-1}\quad(i\in[v]),
 \qquad
 \sum_{i<j}h_{ij}=W.
 \tag{3.4}
\]

#### Proof

For a fixed coordinate pair \(ij\), the difference between its incidence
in the two middle endpoints and in the lower and upper faces of one diamond
is \(-1\) precisely when \(ij=A\setminus X\), and is zero otherwise.
Summing gives

\[
 h_{ij}
 =\binom{2r-3}{r-3}
  +\binom{2r-3}{r-1}+d_D(\{i,j\})
  -2\binom{2r-3}{r-2}.
\]

The binomial second difference is \(-C_{r-1}\), proving (3.3).  Summing
over \(j\) and using (3.2) gives (3.4).  \(\square\)

The nonnegativity in (3.3) is a genuine **space/capacity barrier**.  It
says that a realizable excess design is not merely point regular: every
pair must occur at least \(C_{r-1}\) times.  The available slack is only
\(C_{r-1}/(r-1)\) on average, since

\[
 \mathbb E_{ij}d_D(\{i,j\})
 =\frac r{r-1}C_{r-1}.
 \tag{3.5}
\]

For a partial matching, (3.1) also forces its leftover to obey the same
coordinate lattice:

\[
 \sum_{Y\in L_0}\mathbf1_Y+\sum_{Z\in L_1}\mathbf1_Z
 =\sum_{X\in L_L}\mathbf1_X+\sum_{A_s\in L_U}\mathbf1_A.
 \tag{3.6}
\]

Equal leftover cardinalities in the four parts do not imply (3.6).

Finally, prescribed fractional feasibility is not automatic.  It is
equivalent to the Farkas inequalities

\[
 \sum_X\alpha_X+2\sum_Y\beta_Y+
 \sum_Aw(A)\gamma_A\ge0
 \tag{3.7}
\]

whenever

\[
 \alpha_X+\beta_{X+a}+\beta_{X+b}+\gamma_{X+a+b}\ge0
 \tag{3.8}
\]

for every diamond.  These are the exact global space cuts.  The point and
pair tests above are especially transparent members/consequences of this
barrier system, but they do not exhaust it.

Nor is this secretly a network-flow system.  Fix one lower set \(X\) and
three outside coordinates \(a,b,c\).  On the three middle-degree rows
\(X+a,X+b,X+c\), the three diamond columns \(X+ab,X+bc,X+ca\) induce

\[
 \begin{pmatrix}
 1&0&1\\1&1&0\\0&1&1
 \end{pmatrix},
 \qquad |\det|=2.
 \tag{3.9}
\]

Hence the natural equality matrix is not totally unimodular.  Integrality
cannot be obtained by relabelling (3.7)--(3.8) as an ordinary flow.

### Theorem 3.3 (the full integer edge lattice)

Let \(\Lambda\) be the integer lattice generated by the incidence vectors
of all edges of \({\cal H}_w\), with every \(w(A)\ge1\).  Then a vector

\[
 z=(z_L,z_U,z_0,z_1)\in\mathbb Z^{P_L\sqcup P_U\sqcup P_0\sqcup P_1}
\]

lies in \(\Lambda\) if and only if

\[
 \sum z_L=\sum z_U=\sum z_0=\sum z_1
 \tag{3.10}
\]

and

\[
 \sum_Yz_0(Y)\mathbf1_Y+
 \sum_Yz_1(Y)\mathbf1_Y
 =\sum_Xz_L(X)\mathbf1_X+
 \sum_{(A,s)}z_U(A,s)\mathbf1_A.
 \tag{3.11}
\]

Thus (3.6), together with equality of the four part sizes, is not merely a
visible necessary congruence: it is the **entire integer lattice**.  There
are no additional hidden modular invariants.

#### Proof

It is enough to determine all characters into \(\mathbb R/\mathbb Z\)
which vanish on every edge.  Write such a character as

\[
 \alpha_X,\qquad \gamma_{A,s},\qquad \beta^0_Y,\qquad\beta^1_Y.
\]

Using two slots of the same upper set against the same diamond shows that
\(\gamma_{A,s}\) is independent of \(s\).  Comparing the two orientations
of a diamond gives

\[
 (\beta^0_Y-\beta^1_Y)=(\beta^0_Z-\beta^1_Z)
\]

whenever \(Y,Z\) are Johnson-adjacent.  The Johnson graph is connected, so
this difference is one constant.  Absorb that constant into a part
potential and write the remaining middle potential as \(\beta_Y\).  We
then have

\[
 \alpha_X+\gamma_A+\beta_{X+a}+\beta_{X+b}=0
 \tag{3.12}
\]

for every \(A=X+a+b\).

Fix an \((r-2)\)-set \(R\) and four outside points \(a,b,c,d\).  Alternate
(3.12) around the containment four-cycle with lower faces \(R+a,R+b\) and
upper faces \(R+a+b+c,R+a+b+d\).  The lower and upper potentials cancel,
leaving

\[
 \beta_{R+a+c}+\beta_{R+b+d}
 =\beta_{R+b+c}+\beta_{R+a+d}.
 \tag{3.13}
\]

Equation (3.13) forces \(\beta\) to be an additive valuation on the
uniform layer.  Indeed, for fixed distinct \(a,b\), the difference

\[
 \beta_{P+a}-\beta_{P+b}
\]

is independent of the \((r-1)\)-set \(P\) disjoint from \(a,b\): two such
\(P\)'s differing by one exchange are related by (3.13), and their Johnson
graph is connected.  Calling this difference \(c_a-c_b\), the cocycle
identity for three coordinates gives a consistent family \((c_i)\), and

\[
 \beta_Y=b+\sum_{i\in Y}c_i.
 \tag{3.14}
\]

Substitution into (3.12), followed by connectivity of the lower--upper
containment graph, shows that every annihilating character is a sum of:

* constants on the four parts whose total is zero; and
* a coordinate character, with value \(-\sum_{i\in X}c_i\) on lower and
  upper vertices and \(+\sum_{i\in Y}c_i\) on both middle-clone parts.

These are exactly the characters generated by (3.10)--(3.11).  Since
\(\mathbb R/\mathbb Z\) detects every proper quotient of a free abelian
group, the two lattices coincide.  \(\square\)

Theorem 3.3 is favourable for absorption: after the visible coordinate
balance is imposed there is no further parity class to hit.  It does **not**
say that the nonnegative edge semigroup is saturated.  Section 6 gives the
smallest possible hole.

## 4. A quasirandom Catalan design and a rigorous near-factor

The preceding obstructions can be met simultaneously.  Here is a clean
prime-order existence statement.

### Theorem 4.1 (quasirandom orbit design)

Suppose \(p=2r-1\) is prime and \(r\to\infty\).  There is a union \(D\) of
full translation orbits of \((r+1)\)-sets such that

\[
 |D|=C_r,\qquad d_D(x)=2C_{r-1}\quad(x\in\mathbb Z_p),
 \tag{4.1}
\]

and, for an absolute constant \(K\),

\[
 \max_{X\in{\cal L}}d_D(X)\le Kr,qquad
 \max_{Y\in{\cal M}}d_D(Y)\le K\frac r{\log r},
 \tag{4.2}
\]

while simultaneously

\[
 d_D(\{i,j\})\ge C_{r-1}\qquad(i\ne j).
 \tag{4.3}
\]

#### Proof

The prime action is free and \(p\mid C_r\).  Select exactly \(C_r/p\)
upper-set orbits uniformly without replacement.  The sampling density is

\[
 \rho=\frac{C_r}{\binom p{r+1}}=\frac2{r-1}.
\]

Every full orbit has point degree \(r+1\), so (4.1) is deterministic.

We need two elementary orbit-intersection bounds.  Write an upper set as
the complement of an \((r-2)\)-set \(B\).  If the translates \(B+t\),
\(t\in T\), all lie in a fixed set \(S\), then

\[
 B+T\subseteq S.
\]

Cauchy--Davenport gives \(|B+T|\ge|B|+|T|-1\).  For a fixed
\(X\in{\cal L}\), the relevant \(S=X^c\) has size \(|B|+2\), so one orbit
contains at most three upper supersets of \(X\).  For a fixed
\(Y\in{\cal M}\), \(|Y^c|=|B|+1\), so one orbit contains at most two upper
supersets of \(Y\).

Thus \(d_D(X)\) and \(d_D(Y)\) are weighted hypergeometric sums with
weights at most three and two, and means \(r\) and two.  Standard exponential
moment bounds for sampling without replacement give

\[
 \Pr[d_D(X)>Kr]\le e^{-c_Kr},
 \qquad
 \Pr[d_D(Y)>Kr/\log r]\le e^{-(K/3+o(1))r}.
\]

Choose \(K\) large enough and union-bound over the \(e^{(2\log2+o(1))r}\)
sets in the two middle levels.  This proves (4.2) with positive probability.

For a fixed pair, the mean is

\[
 \rho\binom{2r-3}{r-1}
 =\frac r{r-1}C_{r-1},
\]

so its distance above the floor in (4.3) is \(C_{r-1}/(r-1)\).  An orbit
contributes at most \(p\), and the sum of its orbit weights is
\(\binom{2r-3}{r-1}\).  Bernstein's inequality therefore makes the lower
tail at (4.3) at most

\[
 \exp\{-\Omega(C_{r-1}/r^3)\}.
\]

A union bound over the \(O(r^2)\) pairs completes the proof.  \(\square\)

### Corollary 4.2 (near-perfect matching in a prescribed catalogue)

For the family \(D\) in Theorem 4.1,

\[
 d_{{\cal H}_{1+\mathbf1_D}}(z)=(1+o(1))R
 \quad\text{for every vertex }z,
 \qquad
 \Delta_2=O(r)=o(R).
 \tag{4.4}
\]

Hence the fixed-uniformity near-perfect matching theorem gives a matching in
\({\cal H}_{1+\mathbf1_D}\) covering all but \(o(W)\) vertices.

This is an unconditional asymptotic near-factor inside the exact desired
upper-slot catalogue, using all but \(o(W)\) of its slots.  It is the
strongest conclusion justified solely by the degree--codegree input; calling
it an exact prescribed-load factor would be incorrect.

## 5. Alpha and octahedral trades as absorbers

Fix an \((r-2)\)-set \(R\) and four outside coordinates
\(Q=\{1,2,3,4\}\).  Put

\[
 X_i=R+i,
 \qquad
 A_j=R+(Q\setminus\{j\}),
\]

and let \(e_{ij}\) be the diamond \((X_i,A_j)\), for \(i\ne j\).  The
integer changes preserving the lower, upper, and middle marginals are
exactly

\[
 z_{ij}=-z_{ji},\qquad \sum_{j\ne i}z_{ij}=0.
 \tag{5.1}
\]

Thus the local kernel is the circulation lattice of \(K_4\).  Its primitive
simple moves are directed triangles (alpha trades) and directed four-cycles
(octahedral trades).

### Lemma 5.1 (the alpha trade is a hypergraph trade)

For a directed triangle \(i\to j\to k\to i\), the three positive diamonds
and the three negative diamonds can be oriented so that they are two
matchings of \({\cal H}_w\) on exactly the same twelve vertices.

#### Proof

Both sides use the same three lower vertices and the same three upper slots.
On the six geometric middle vertices, the two chord matchings form one
alternating 6-cycle.  Its bipartition supplies the common set of three
0-clones and three 1-clones.  \(\square\)

The same statement holds for the four-cycle trade, with four hyperedges on
each side.

### Corollary 5.2 (edge absorbers)

If a hyperedge \(e\) lies on one side \(P\) of an alpha trade \(P\leftrightarrow
N\), then

\[
 P\setminus\{e\}
 \quad\text{matches }V(P)\setminus V(e),
 \qquad
 N\quad\text{matches }V(P).
\tag{5.2}
\]

Hence \(V(P)\setminus V(e)\) is an eight-vertex absorber for the four
vertices of \(e\).  Every hyperedge belongs to at least

\[
 \boxed{2(r-1)(r-2)}
 \tag{5.3}
\]

such alpha trades: choose the removed element \(i\in X\), the fourth
coordinate \(j\notin A\), and either member of \(A\setminus X\) as the
third vertex of the directed triangle.  Extra upper slots can only increase
this number.  A four-cycle trade similarly gives a twelve-vertex absorber
after one of its four edges is removed.

This is genuine absorption, but its scope must not be overstated.

* It absorbs a four-set of vertices only when those vertices already form a
  legal diamond hyperedge.
* A union of such zero-marginal trades preserves (3.6); it cannot repair a
  leftover which violates the coordinate lattice.
* Removing several edges from trade sides absorbs their union only when
  those removed edges form a matching.

Therefore alpha/octahedral charts are excellent **switchers and edge
absorbers**, but they are not a universal absorber for an arbitrary balanced
four-partite residual.

There is also a quantitative warning.  The catalogue has
\(\Theta(Wr^2)\) hyperedges and \(\Theta(Wr^4)\) alpha charts, while a
vertex-disjoint absorber bank contains only \(O(W)\) charts.  A uniformly
spread bank therefore samples only an \(O(r^{-4})\) fraction of the charts,
whereas one edge belongs to only \(\Theta(r^2)\) charts.  A universal
edge-by-edge bank cannot follow merely from random thinning; a structured
template or a cover-down theorem is necessary.

## 6. Semigroup holes and the first non-edge absorber

The full lattice theorem does not imply that a small admissible leftover can
itself be partitioned into diamond edges.

### Proposition 6.1 (a one-cell semigroup hole)

Fix an \((r-2)\)-set \(I\) and four distinct outside points \(a,b,c,d\).
Consider the leftover consisting of

\[
 X=I+a\in P_L,\qquad
 A=I+b+c+d\in P_U,\qquad
 Y=I+a+b\in P_0,\qquad
 Z=I+c+d\in P_1.
 \tag{6.1}
\]

It satisfies the part equations and

\[
 \mathbf1_Y+\mathbf1_Z=\mathbf1_X+\mathbf1_A,
\]

so its incidence vector lies in the full edge lattice by Theorem 3.3.  But
it is not one hyperedge: \(X\not\subset A\), equivalently \(Y,Z\) are not
Johnson-adjacent.  Since there is only one vertex in each part, it has no
edge partition.

Thus the proposed statement

\[
 \text{``every sufficiently small coordinate-balanced leftover is
 edge-decomposable''}
\]

is false already at size one.

The obstruction is a genuine Farkas/Hall space cut.  For any family
\({\cal S}\subseteq P_L\), every fractional or integral cover must satisfy

\[
 \sum_{X\in{\cal S}}\ell_L(X)
 \le
 \sum_{(A,s):A\in N({\cal S})}\ell_U(A,s),
 \tag{6.2}
\]

where \(N({\cal S})=\{A:\exists X\in{\cal S},\ X\subset A\}\).  This is
obtained from (3.7) by assigning potential \(-1\) to \({\cal S}\), potential
\(+1\) to its upper neighbourhood, and zero elsewhere.  The leftover (6.1)
violates (6.2) with \({\cal S}=\{X\}\).  Dually, every family of 0-clones
must satisfy the Johnson-neighbourhood Hall inequality against the available
1-clones.  Neither projection family follows from the coordinate lattice.

More generally, the complete fractional space-barrier theorem for a
leftover vector \(\ell\ge0\) is

\[
 \boxed{
 \ell\in\operatorname{cone}\{\mathbf1_e:e\in E({\cal H}_w)\}
 \iff
 \langle\pi,\ell\rangle\ge0
 \text{ for every }\pi\text{ with }
 \sum_{v\in e}\pi_v\ge0\ (e\in E).}
 \tag{6.3a}
\]

The containment and Johnson Hall cuts are explicit subfamilies of (6.3a).
Theorem 3.3 characterizes the lineality/equality part of this dual exactly;
the remaining one-sided potentials are genuine space barriers and cannot be
recovered from lattice arithmetic.

There is nevertheless an exact absorber for this minimal hole.

### Proposition 6.2 (one-edge diagonal absorber)

For the target (6.1), let the reservoir be the four vertices of the legal
oriented diamond

\[
 e_-=\{I+c,\ I+a+b+c,\ (I+b+c,0),\ (I+a+c,1)\}.
 \tag{6.3}
\]

The reservoir alone is matched by \(e_-\).  After adjoining the target,
the same eight vertices are matched by

\[
\begin{aligned}
 e_1&=\{I+a, I+a+b+c, (I+a+b,0), (I+a+c,1)\},\\
 e_2&=\{I+c, I+b+c+d, (I+b+c,0), (I+c+d,1)\}.
\end{aligned}
\tag{6.4}
\]

Hence every coordinate-balanced one-cell leftover with
\(|X\setminus A|=1\) has a one-edge absorber, after relabelling the four
outside coordinates.

This move is an augmenting two-path in the diamond hypergraph.  It is not a
zero-marginal alpha trade: its two sides have sizes one and two.  It is the
first genuinely useful cover-down gadget beyond edge absorption.

### Corollary 6.3 (balanced trades alone cannot cover down)

No absorber for the target (6.1) can be obtained solely by composing alpha
and octahedral trades and then deleting edges from one side.

Indeed, every alpha/octahedral move replaces one matching by another on the
same vertex set.  A composition still has identical covered vertex sets on
its two sides.  If edges are then deleted from one side to expose a target,
that target is exactly the disjoint union of the deleted legal edges.  The
target (6.1) has no such edge partition.  Thus a nonzero augmenting gadget
such as (6.3)--(6.4), not merely a richer supply of zero-marginal trades, is
logically necessary.

For a general coordinate-balanced one-cell leftover, put

\[
 t=|X\setminus A|.
\]

Then \(X\cap A=Y\cap Z\), \(X\cup A=Y\cup Z\), and inside the interval
\([X\cap A,X\cup A]\) the two pairs are complementary bipartitions of a
\((2t+2)\)-set.  A bounded local absorber cannot handle all such targets.

There is an explicit growing absorber whenever the target is coherent on
one middle side.

### Theorem 6.4 (coherent ladder absorber)

Suppose, after possibly exchanging the two clone parts, that

\[
 Y=X+h,\qquad Z=A-h
 \tag{6.5}
\]

for some \(h\in A\setminus X\).  Equivalently, \(X\subset Y\).  Then the
target \(\{X,A,(Y,0),(Z,1)\}\) has an absorber with exactly \(t\) reservoir
edges and \(t+1\) absorbing edges, where \(t=|X\setminus A|\).

#### Construction

Choose \(g\in(A\setminus X)\setminus\{h\}\) and put

\[
 L_t=A\setminus\{h,g\}.
\]

Then \(|X\setminus L_t|=|L_t\setminus X|=t\).  Write these two difference
sets as \(\{p_1,\ldots,p_t\}\) and \(\{q_1,\ldots,q_t\}\), and define the
monotone exchange path

\[
 L_0=X,\qquad
 L_i=L_{i-1}-p_i+q_i,\qquad
 U_i=L_{i-1}\cup L_i\cup\{h\}.
 \tag{6.6}
\]

For each \(i\), the two diamonds \((L_{i-1},U_i)\) and \((L_i,U_i)\)
share the middle set

\[
 K_i=L_{i-1}+q_i=L_i+p_i.
\]

Use as reservoir the \(t\) oriented edges

\[
 (L_i,U_i; (L_i+h,0),(K_i,1)),\qquad 1\le i\le t.
 \tag{6.7}
\]

After the target arrives, replace them by the \(t\) edges

\[
 (L_{i-1},U_i; (L_{i-1}+h,0),(K_i,1)),\qquad1\le i\le t,
 \tag{6.8}
\]

and the final edge

\[
 (L_t,A; (L_t+h,0),(L_t+g,1)).
 \tag{6.9}
\]

The common \(K_i\)-vertices cancel term by term.  The 0-clone chain
telescopes: its first new vertex is \(L_0+h=Y\), and its final reservoir
vertex \(L_t+h\) is consumed by (6.9).  The other endpoint of (6.9) is
\(L_t+g=A-h=Z\).  The monotone form of (6.6) makes all lower, upper, and
middle vertices on each side distinct, so both displayed families are
matchings.  This proves the theorem.  \(\square\)

Theorem 6.4 contains Proposition 6.2 as the case \(t=1\).  The natural next
idea would be to braid two coherent ladders when the elements of
\(X\setminus A\) are split between \(Y\) and \(Z\).  The following theorem
shows that such a braid is necessarily quadratic, not linear.

### Theorem 6.5 (exact mixed swap-inventory lower bound)

For a coordinate-balanced one-cell target, put \(I=X\cap A=Y\cap Z\) and
partition the active coordinates into

\[
\begin{array}{c|c|c|c}
P=(X\cap Y)\setminus I&
Q=(X\cap Z)\setminus I&
R=(A\cap Y)\setminus I&
S=(A\cap Z)\setminus I .
\end{array}
\tag{6.10}
\]

Write

\[
 |P|=p,\qquad |Q|=q,\qquad |R|=q+1,\qquad |S|=p+1,
\tag{6.11}
\]

so \(t=p+q\).  If an absorber has a reservoir matching \(M_-\) of \(m\)
edges and an absorbing matching \(M_+\) of \(m+1\) edges, then

\[
\boxed{m\ge 2pq+p+q.}
\tag{6.12}
\]

In particular, when \(p,q=\Theta(t)\), every absorber has
\(\Omega(t^2)\) edges.  No \(O(t)\)-edge universal braid exists.

#### Proof

For a four-part vertex vector \(V\), define its pair-incidence defect

\[
\Delta_{ij}(V)
=d_{M_0,V}(ij)+d_{M_1,V}(ij)
 -d_{L,V}(ij)-d_{U,V}(ij).
\tag{6.13}
\]

For one legal diamond edge this defect is \(-1\) on its exchanged
coordinate pair and zero on every other pair.  If \(h^\pm_{ij}\) is the
swap-pair inventory of \(M_\pm\), the absorber identity

\[
\mathbf1_{V(M_+)}
=\mathbf1_{\rm target}+\mathbf1_{V(M_-)}
\]

therefore gives

\[
h^+_{ij}-h^-_{ij}=-\Delta_{ij}({\rm target}).
\tag{6.14}
\]

For the four-type partition (6.10), direct substitution gives

\[
\Delta_{ij}=
\begin{cases}
+1,&ij\in P\times R\text{ or }ij\in Q\times S,\\
-1,&ij\in P\times Q\text{ or }ij\in R\times S,\\
0,&\text{otherwise}.
\end{cases}
\tag{6.15}
\]

Thus \(M_-\) must contain at least one swapped edge for every pair in
\(P\times R\) and \(Q\times S\).  These pairs are distinct, and one
diamond edge has only one swap pair.  Consequently

\[
 m\ge |P||R|+|Q||S|
 =p(q+1)+q(p+1)=2pq+p+q.
\]

The positive side similarly needs at least

\[
 |P||Q|+|R||S|
 =2pq+p+q+1
\]

edges, exactly one more.  \(\square\)

The coherent cases are exactly \(p=0\) or \(q=0\).  There (6.12) reduces to
\(m\ge t\), and Theorem 6.4 attains equality.  Hence the coherent ladder is
optimal, not merely convenient.  The earlier containment-path argument
only gave \(m\ge\lceil t/2\rceil\); the pair inventory is the sharp
obstruction.

For a typical mixed target with \(p,q=\Theta(r)\), one target consumes
\(\Theta(r^2)\) reservoir edges.  Therefore an edge-disjoint absorber bank
of size \(O(W)\) can handle at most \(O(W/r^2)\) such targets.  An
unspecified \(o(W)\) nibble leave is quantitatively insufficient for this
completion scheme unless the cover-down first correlates/re-pairs the
leftover into mostly coherent cells.

The same argument gives the correct aggregate currency, without first
pairing a many-cell leftover into singleton targets.

### Corollary 6.6 (aggregate pair-defect barrier)

Let \(\ell\) contain \(s\) vertices in each of the four parts and satisfy
the coordinate lattice.  If an absorber uses \(m\) reservoir edges, then

\[
\boxed{
m\ge
\sum_{i<j}\bigl(\Delta_{ij}(\ell)\bigr)_+ .}
\tag{6.16}
\]

Indeed, (6.14) holds with the aggregate defect, so every positive unit of
\(\Delta_{ij}\) requires a negative-side edge with swap pair \(ij\).
Moreover

\[
\sum_{i<j}\Delta_{ij}(\ell)=-s,
\tag{6.17}
\]

because the four ranks contribute

\[
2\binom r2-\binom{r-1}2-\binom{r+1}2=-1
\]

per cell.  Hence the corresponding lower bound for the absorbing side is
exactly the right-hand side of (6.16) plus \(s\).

This identifies the statistic which a viable cover-down must control:
not the raw number of leftover vertices, but the positive \(L^1\) mass of
their pair defect.  Different cells can cancel each other's mixed defects,
so correlated re-pairing can still beat the singleton-by-singleton
\(\Theta(r^2)\) cost.  A random or unstructured leave gives no such
cancellation for free.

There is an equivalent quota formulation for a partial matching in the full
prescribed catalogue.  Put

\[
h^*_{ij}=d_D(\{i,j\})-C_{r-1},
\]

the forced final swap inventory from Theorem 3.2, and let \(h^M_{ij}\) be
the inventory already used by a partial matching \(M\).  The uncovered
vertex set has

\[
\boxed{\Delta_{ij}(\text{leave})=h^M_{ij}-h^*_{ij}.}
\tag{6.18}
\]

Consequently a completion which leaves every edge of \(M\) untouched is
possible only if

\[
h^M_{ij}\le h^*_{ij}\qquad(i<j).
\tag{6.19}
\]

This condition is automatic for an initial segment of an actual perfect
matching, but not for a generic nibble.  Corollary 4.2 therefore cannot be
fed blindly into absorption: the nibble must respect all
\(\binom v2=\Theta(r^2)\) swap quotas, or the absorber must explicitly undo
the overused pairs.  Formula (6.16) is exactly the minimum number of such
undoing edges.

### Proposition 6.7 (exact coherent re-pairing normal form)

For a four-part leftover \(({\cal L}',{\cal U}',{\cal M}'_0,{\cal M}'_1)\),
form two edge-coloured bipartite graphs:

\[
\begin{aligned}
B_0&:\quad X\in{\cal L}'\ --\ Y\in{\cal M}'_0
       &&\text{when }X\subset Y,\quad\text{colour }Y\setminus X,\\
B_1&:\quad A\in{\cal U}'\ --\ Z\in{\cal M}'_1
       &&\text{when }Z\subset A,\quad\text{colour }A\setminus Z.
\end{aligned}
\tag{6.20}
\]

The leftover can be partitioned into coherent cells of the orientation
\(Y=X+h,\ Z=A-h\) if and only if \(B_0\) and \(B_1\) have perfect matchings
with identical colour histograms.

Indeed, pair equal-coloured edges \(X--(X+h)\) and
\((Z+h)--Z\) to obtain one coherent cell; the converse reads these two
incidences from every cell.  Clone-reversed coherent cells give the analogous
pair \({\cal L}'--{\cal M}'_1\) and
\({\cal U}'--{\cal M}'_0\).  Thus deterministic re-pairing is a
**coupled coloured-perfect-matching problem**, not a consequence of the
pair-defect inequalities alone.

### Proposition 6.8 (strict pair margin does not imply coherent re-pairing)

For all sufficiently large \(r\), there are polynomial-size leftovers which

1. satisfy the full coordinate lattice;
2. have \(\Delta_{ij}<0\) for every coordinate pair; but
3. have a lower vertex isolated from both lower--middle incidence graphs,
   and hence admit no coherent re-pairing of either orientation.

#### Construction

Start with the mixed target having \(p=q=1\), so its positive pair defect is
supported on four pairs.  For every coordinate pair \(ij\), adjoin two
pairwise vertex-disjoint legal diamond cells with swap pair \(ij\).  Choose
their lower faces greedily so that both middle endpoints omit at least one
of the two coordinates of the original lower target \(X\).  This is always
possible: after the swap pair and one forbidden coordinate are excluded,
there remain \(\binom{2r-4}{r-1}\) lower faces, while only polynomially many
vertices have previously been forbidden.

Every added legal cell contributes \(-1\) to \(\Delta_{ij}\) and zero to all
other pair defects.  Two copies on every pair make the aggregate defect
strictly negative, including on the four initially positive pairs.  All
cells are coordinate-balanced, so their union satisfies the lattice.  But
no middle vertex in either clone contains the distinguished \(X\), making
\(X\) isolated in both possible coherent incidence graphs.  \(\square\)

This counterexample does not say that the random five-part nibble leave has
bad incidence expansion.  It says that **quota margin alone cannot prove
the deterministic re-pairing theorem**; Hall expansion of the actual
residual incidence graphs must be maintained as a separate invariant.

### The labelled-quota correction

In the augmented five-part hypergraph, a coherent ladder is not by itself
an absorber for one leftover quota slot.  If its target cell has defect
\(\Delta\), its two matching sides have swap inventories satisfying

\[
h^+-h^-=-\Delta.
\tag{6.21}
\]

For a non-edge coherent cell, \(-\Delta\) has several positive entries and
also negative entries; it is not one standard basis vector corresponding to
one labelled quota slot.  Hence the old quota vertices used by the reservoir
cannot all be retained while one new quota vertex is added.

For a whole leave, the unused quota multiplicity is

\[
k_{ij}=h^*_{ij}-h^M_{ij}=-\Delta_{ij}(\mathrm{leave})\ge0.
\tag{6.22}
\]

Coherent ladders may therefore be used only in **coupled bundles** whose
negative swap requirements cancel and whose aggregate net inventory is
exactly \(k\).  Equivalently, one needs a quota-exchange network which frees
the old labelled slots used by the reservoir ladders and reassigns the new
positive-side slots.  Merely partitioning the four original parts into
coherent cells and absorbing each cell independently is insufficient in the
five-part model.

## 7. Why no black-box exact theorem applies yet

The input (4.4) is sufficient for a nibble because the hypergraph uniformity
is the fixed number four.  It is not sufficient for an exact matching.
Near-regularity and \(\Delta_2=o(R)\) do not exclude parity, lattice, or
space barriers, even in very dense multipartite examples.  In the present
geometry those barriers have the concrete forms (3.2), (3.3), (3.6), and
(3.7)--(3.8).

The orbit design of Theorem 4.1 clears the point identity and the visible
pair-capacity floor.  What has **not** been proved is either of the following
stronger assertions.

1.  A robust fractional theorem: all Farkas cuts have uniform slack after a
    small reservoir is removed.
2.  A cover-down theorem: every sufficiently small residual satisfying the
    full edge lattice can be converted, inside the reservoir, into a
    matching of legal diamonds.

Only after the cover-down produces a residual matching do the local alpha
absorbers of Section 5 complete it edge by edge.  Consequently the correct
conditional exact statement is:

> **Conditional completion theorem.**  If a reservoir in
> \({\cal H}_{1+\mathbf1_D}\) has the cover-down property that every small
> lattice-admissible leftover can, after adjoining reserved vertices, be
> transformed into a disjoint family of legal residual edges, and it
> contains disjoint alpha absorbers for those residual edges, then the
> near-perfect matching of Corollary 4.2 extends to a perfect matching.

The second clause is locally abundant by (5.3).  The first clause is the
real unproved theorem.

## 8. Final verdict

The diamond route has now been separated into a proved and an unproved
part.

\[
\boxed{
\begin{array}{c}
\text{quasirandom Catalan excess design}\\
+\ \text{degree/codegree nibble}
\end{array}}
\quad\Longrightarrow\quad
\boxed{\text{near-factor in the prescribed catalogue, with }o(W)\text{ leave}.}
\]

The exact upgrade requires

\[
\boxed{
\text{robust Farkas/space control}
+\text{ lattice-respecting reservoir transformers}
+\text{ alpha absorption}.}
\]

No divisibility obstruction remains for the prime cyclic designs, and the
visible pair capacities have exponential margin over concentration error.
But the cover-down is not supplied by any result proved in the current
files.  Thus the robust perfect-matching/absorption route is mathematically
live, and it already proves the asymptotic near-factor, but it does **not**
yet prove an exact prescribed-load q1 factor.
