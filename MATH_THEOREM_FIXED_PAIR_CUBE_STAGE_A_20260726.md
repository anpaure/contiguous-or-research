# Fixed-pair cube Stage A: the exact low-dimensional tail and a dyadic isometric cycle factor

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Verdict

Let a \(2m\)-element ground set be partitioned into \(m\) fixed coordinate
pairs. Its rank-\(m\) sets partition exactly into orientation cubes \(Q_d\),
where \(d\) is the number of split pairs. If \(h=h(m)\) satisfies

\[
 h=2^r\ge 2,\qquad h=o(m),                              \tag{0.1}
\]

then every cube of dimension \(d\ge h\) admits an explicit vertex factor
into isometric cycles of length \(2h\), while the total number of vertices
in cubes with \(d<h\) obeys

\[
 \le \exp\bigl(-(\log 2-o(1))m\bigr)\binom{2m}{m}
 =o\!\left(\binom{2m}{m}\right).                       \tag{0.2}
\]

Thus the fixed-pair Stage-A statement is true. In particular, one may take
a power of two with

\[
 \sqrt{m\log m}\ll h\ll m;                             \tag{0.3}
\]

for example

\[
 h=2^{\lceil(3/4)\log _2m\rceil}.                       \tag{0.4}
\]

The power-of-two hypothesis is exact: a vertex partition of \(Q_h\) into
cycles of length \(2h\) requires \(2h\mid 2^h\), hence \(h\) must be a
power of two. The construction below gives one spanning \(2\)-factor,
that is, one vertex-parallel class of disjoint cycles. It must not be
confused with either an arbitrary edge decomposition or a resolution of
all cube edges into several such factors.

No lower- or upper-shadow balance is asserted here. Consequently this
Stage-A theorem alone does not prove MWB or the constant-one conjecture.

## 1. The exact fixed-pair cube partition

Let

\[
 X=P_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_m,
 \qquad P_i=\{a_i,b_i\}.
\]

For \(S\in\binom Xm\), define its full, empty, and split pair sets by

\[
 F(S)=\{i:P_i\subseteq S\},\quad
 E(S)=\{i:P_i\cap S=\varnothing\},\quad
 I(S)=\{i:|P_i\cap S|=1\}.                             \tag{1.1}
\]

Put \(d(S)=|I(S)|\). Since

\[
 2|F(S)|+d(S)=m,
 \qquad |F(S)|+|E(S)|+d(S)=m,
\]

we have

\[
 |F(S)|=|E(S)|={m-d(S)\over2},\qquad d(S)\equiv m\pmod2. \tag{1.2}
\]

Fix disjoint pair-index sets \(I,F\subseteq[m]\) with

\[
 |I|=d,\qquad |F|={m-d\over2}.
\]

Let

\[
 \mathcal Q(I,F)=
 \left\{
   \bigcup_{i\in F}P_i\ \cup\ \{z_i:i\in I,\ z_i\in P_i\}
 \right\}.                                             \tag{1.3}
\]

The remaining pair indices are empty. Choosing \(a_i\) or \(b_i\) for
each \(i\in I\) identifies (1.3) with \(\mathbb F_2^d\). Two members are
adjacent in \(J(2m,m)\) exactly when one such choice is flipped. Moreover,
if two orientation words differ in \(t\) coordinates, the corresponding
sets differ by \(t\) deletions and \(t\) insertions, so their Johnson
distance is \(t\). Hence every \(\mathcal Q(I,F)\) is an isometrically
embedded \(Q_d\).

Every middle set has a unique pair \((I,F)\), so these cubes partition the
vertices, although they are not the connected components of the Johnson
graph. There are exactly

\[
 C_{m,d}=\binom md\binom{m-d}{(m-d)/2}                  \tag{1.4}
\]

such \(d\)-cubes, and their total vertex mass is

\[
 M_{m,d}
 =2^d\binom md\binom{m-d}{(m-d)/2}
 ={2^dm!\over d!((m-d)/2)!^2},                         \tag{1.5}
\]

when \(d\equiv m\pmod2\), and is zero otherwise. Thus

\[
 \sum_{\substack{0\le d\le m\\d\equiv m\ (2)}}M_{m,d}
 =\binom{2m}{m}=:W_m.                                  \tag{1.6}
\]

As an exact check on (1.5), consecutive admissible dimensions satisfy

\[
 {M_{m,d+2}\over M_{m,d}}
 ={(m-d)^2\over(d+1)(d+2)}.                            \tag{1.7}
\]

## 2. A finite low-dimensional tail bound

For \(2\le h\le m/2\), put

\[
 L_{m,h}=\sum_{\substack{0\le d<h\\d\equiv m\ (2)}}M_{m,d}. \tag{2.1}
\]

### Proposition 2.1

For every \(2\le h\le m/2\),

\[
 \boxed{
 {L_{m,h}\over W_m}
 \le (2m+1)h\,2^{-m}
       \left({em\over h-1}\right)^{h-1}.}              \tag{2.2}
\]

Consequently

\[
 L_{m,h}\le
 \exp\bigl(-(\log2-o(1))m\bigr)W_m=o(W_m)               \tag{2.3}
\]

for every integer sequence \(2\le h=h(m)=o(m)\), for all sufficiently
large \(m\).

#### Proof

The middle binomial coefficient in (1.5) is at most \(2^{m-d}\).
Therefore

\[
 L_{m,h}\le 2^m\sum_{d=0}^{h-1}\binom md.              \tag{2.4}
\]

The binomial coefficients are increasing for \(d<m/2\), and the standard
factorial estimate gives

\[
 \sum_{d=0}^{h-1}\binom md
 \le h\binom m{h-1}
 \le h\left({em\over h-1}\right)^{h-1}.                \tag{2.5}
\]

Since the central coefficient is the largest coefficient of
\((1+x)^{2m}\),

\[
 W_m=\binom{2m}{m}\ge {4^m\over2m+1}.                  \tag{2.6}
\]

Equations (2.4)--(2.6) prove (2.2). If \(x=(h-1)/m=o(1)\), the logarithm
of its right-hand side is

\[
 -m\log2+mx\bigl(1+\log(1/x)\bigr)+o(m)
 =-(\log2-o(1))m,                                      \tag{2.7}
\]

because \(x\log(1/x)\to0\). This proves (2.3). \(\square\)

The lower condition \(h\gg\sqrt{m\log m}\) plays no role in this tail
estimate; only \(h=o(m)\) is needed.

## 3. Maximal isometric cycles in a cube

Write an edge of \(Q_h\) by the coordinate which it flips.

### Lemma 3.1 (direction-word characterization)

A simple \(2h\)-cycle in \(Q_h\) is isometric if and only if, cyclically,
its edge-direction word is

\[
 \pi_1,\ldots,\pi_h,\pi_1,\ldots,\pi_h                 \tag{3.1}
\]

for a permutation \(\pi\) of \([h]\).

#### Proof

If the cycle is isometric, the endpoints of every length-\(h\) arc have
cube distance \(h\). Hence the \(h\) directions on that arc are distinct
and therefore form a permutation of \([h]\). Comparing two consecutive
length-\(h\) arcs shows that the newly entering direction equals the
departing one. Thus the direction word has period \(h\), proving (3.1).

Conversely, every cyclic block of at most \(h\) symbols in (3.1) has no
repetition. Its endpoint difference therefore has Hamming weight equal to
the block length. The shorter arc between any two cycle vertices has
length at most \(h\), so cycle distance and cube distance agree. \(\square\)

In particular, the word

\[
 1,2,\ldots,h,1,2,\ldots,h                              \tag{3.2}
\]

defines an isometric \(2h\)-cycle for every \(h\ge2\). The issue is not
the existence of one cycle, but whether its translates can partition all
vertices.

## 4. The explicit dyadic vertex factor

### Theorem 4.1 (sharp vertex-factor theorem)

For an integer \(h\ge2\), \(Q_h\) has a vertex partition into isometric
cycles of length \(2h\) if and only if \(h\) is a power of two.

#### Necessity

Such a partition has \(2^h/(2h)\) cycles. Hence \(2h\mid2^h\), or
\(h\mid2^{h-1}\). Thus \(h\) has no odd prime divisor and is a power of
two. This argument already applies without the isometry assumption.

#### Sufficiency and explicit construction

Let \(h=2^r\), \(r\ge1\), identify \(V(Q_h)\) with \(\mathbb F_2^h\), and
let \(e_1,\ldots,e_h\) be its standard basis. Define

\[
 p_0=0,\qquad
 p_{j+1}=p_j+e_{1+(j\bmod h)}\quad(0\le j<2h).          \tag{4.1}
\]

Then \(p_{2h}=p_0\), and

\[
 C=(p_0,p_1,\ldots,p_{2h-1})                            \tag{4.2}
\]

is the isometric cycle with word (3.2).

Let \(G=\mathbb F_2^r\), list its elements explicitly as

\[
 g_j=\text{the length-\(r\) binary expansion of }j,
 \qquad 0\le j<h,                                      \tag{4.3}
\]

and embed \(G\) as \(G\times\{0\}\) in
\(\Sigma=\mathbb F_2^{r+1}\). Put \(t=(0,\ldots,0,1)\). Define the linear
map

\[
 \phi:\mathbb F_2^h\longrightarrow\Sigma               \tag{4.4}
\]

on basis vectors by

\[
 \phi(e_j)=(g_j+g_{j-1},0)\quad(1\le j<h),
 \qquad
 \phi(e_h)=(g_{h-1},1)=t+(g_{h-1},0).                  \tag{4.5}
\]

The recurrence gives \(p_{h+j}=p_h+p_j\). Thus, for \(0\le j<h\),
telescoping gives

\[
 \phi(p_j)=(g_j,0),\qquad
 \phi(p_{h+j})=t+(g_j,0).                               \tag{4.6}
\]

Thus \(\phi\) maps the \(2h=2^{r+1}\) vertices of \(C\) bijectively onto
all of \(\Sigma\). In particular, \(\phi\) is onto. Let

\[
 K=\ker\phi,\qquad
 |K|=2^{h-r-1}={2^h\over2h}.                            \tag{4.7}
\]

For every \(k\in K\), translate the cycle by \(k\):

\[
 C_k=(k+p_0,k+p_1,\ldots,k+p_{2h-1}).                   \tag{4.8}
\]

These cycles partition \(\mathbb F_2^h\). Indeed, for each
\(x\in\mathbb F_2^h\), bijectivity of \(\phi|_{V(C)}\) gives a unique
\(p_j\) with \(\phi(p_j)=\phi(x)\); then \(k=x+p_j\in K\), so
\(x=k+p_j\). The representation is unique by the same argument. Every
\(C_k\) is isometric because translation preserves cube distance. This
proves the theorem. \(\square\)

The exceptional value \(h=1\) has no simple \(2\)-cycle in the simple
graph \(Q_1\); traversing its sole edge twice is not a cycle under the
standard convention.

### Corollary 4.2 (fixed active dimension inside every larger cube)

Let \(s\ge h\ge2\). Then \(Q_s\) has a vertex partition into isometric
\(2h\)-cycles if and only if \(h\) is a power of two.

#### Proof

Necessity follows from \(2h\mid2^s\). For sufficiency, fix any \(h\) of
the \(s\) coordinates. Fixing all other \(s-h\) coordinates partitions
\(Q_s\) into \(2^{s-h}\) isometric \(h\)-faces. Apply Theorem 4.1 in each
face. \(\square\)

This corollary is the form needed for Stage A. It does **not** assert a
natural-length \(2s\)-cycle factor in an arbitrary \(Q_s\); that stronger
claim is false whenever \(s\) is not a power of two.

## 5. Completion of Stage A

Fix a power of two \(h\ge2\). In every orientation cube \(Q_d\) with
\(d\ge h\), choose, deterministically, the first \(h\) split-pair
coordinates. Fixing the other \(d-h\) orientations partitions \(Q_d\)
into \(h\)-faces. Apply (4.8) in every face.

The result is a vertex-disjoint family of isometric \(2h\)-cycles covering
exactly

\[
 W_m-L_{m,h}                                             \tag{5.1}
\]

middle vertices. It contains exactly

\[
 N_{m,h}={W_m-L_{m,h}\over2h}                            \tag{5.2}
\]

cycles. Under (0.3),

\[
 N_{m,h}=(1+o(1)){W_m\over2h}
          =o\!\left({W_m\over\sqrt{m\log m}}\right).    \tag{5.3}
\]

Each cycle is isometric not only in its \(h\)-face but also in the host
\(Q_d\) and in \(J(2m,m)\), because all three metrics agree on that face.

## 6. Vertex factor, edge decomposition, and resolution

The terminology has three different ledgers.

1. **One cycle.** The word (3.2) gives one isometric \(C_{2h}\).

2. **A vertex-cycle factor.** The family \(\{C_k:k\in K\}\) has
   \(2^h/(2h)\) cycles, partitions \(V(Q_h)\), and selects exactly \(2^h\)
   cube edges. Equivalently, it is one spanning \(2\)-regular subgraph,
   and is the kind of vertex-parallel class used inside a resolvable edge
   decomposition.

3. **An edge decomposition.** The full cube has

   \[
   |E(Q_h)|=h2^{h-1}.                                   \tag{6.1}
   \]

   Decomposing all edges into \(2h\)-cycles would require \(2^{h-2}\)
   cycles. Resolving such an edge decomposition into vertex factors would
   require \(h/2\) resolution classes, with every vertex appearing once in
   each class.

For \(h>2\), the factor in Theorem 4.1 uses only the fraction \(2/h\) of
all cube edges. Therefore a theorem giving an edge decomposition does not
by itself identify a chosen vertex factor, and the single kernel-translate
factor proved here does not by itself decompose all edges. No such
conflation is used in Stage A.

## 7. Optional odd-ground-set variant

If the intended ground set is \(X\mathbin{\dot\cup}\{\infty\}\), with
only the \(2m\) points of \(X\) paired, apply the same argument separately
according to

\[
 \varepsilon=\mathbf1_{\{\infty\in S\}}
\]

for \(S\in\binom{X\cup\{\infty\}}m\). The exact number of \(d\)-cubes in
the \(\varepsilon\)-slice is

\[
 C^{(\varepsilon)}_{m,d}
 =\binom md
  \binom{m-d}{(m-\varepsilon-d)/2},                    \tag{7.1}
\]

provided \(d\equiv m-\varepsilon\pmod2\), and is zero otherwise. Each cube
again has \(2^d\) vertices. For each \(d\), exactly one value of
\(\varepsilon\) is admissible. Hence the low-\(d\) mass \(L'_{m,h}\) obeys

\[
 {L'_{m,h}\over\binom{2m+1}{m}}
 \le (m+1)h\,2^{-m}
       \left({em\over h-1}\right)^{h-1}=o(1)            \tag{7.2}
\]

whenever \(2\le h=o(m)\). If in addition \(h\) is a power of two, the
same cycle factor therefore covers all but
\(o\bigl(\binom{2m+1}{m}\bigr)\) vertices in this variant as well.
Indeed, its low-\(d\) numerator is bounded by the right side of (2.4),
whereas

\[
 \binom{2m+1}{m}
 ={2m+1\over m+1}\binom{2m}{m}
 \ge {4^m\over m+1};
\]

these two inequalities give (7.2).

The main theorem above uses the exact hypothesis \(X=[2m]\) and
\(W_m=\binom{2m}{m}\); equation (7.2) records the separate convention with
an unpaired point.

## 8. Exact proved boundary

The following are unconditional:

* the cube partition (1.3)--(1.6);
* the finite tail estimate (2.2);
* the sharp power-of-two classification in Theorem 4.1;
* the explicit kernel-translate factor (4.4)--(4.8);
* the near-spanning Stage-A factor (5.1)--(5.3).

What remains outside this theorem is every multidepth ownership assertion:
consecutive cycle windows need not balance, inject into, or cover the
rank-\(m\pm q\) targets. In particular, a middle vertex factor is not an
exact wreath factor and is not a proof of coefficient one.
