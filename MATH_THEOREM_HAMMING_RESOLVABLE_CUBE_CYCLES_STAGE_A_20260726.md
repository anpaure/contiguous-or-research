# A resolvable \(C_{2h}\)-decomposition of \(Q_h\) and fixed-pair Stage A

Date: 2026-07-26

Method: pure mathematics.

## 0. Outcome

Let \(h=2^t\ge2\).  The \(h\)-cube has an explicit resolvable edge
decomposition into isometric cycles of length \(2h\):

\[
 E(Q_h)=\mathop{\dot\bigcup}_{a\in A}E(\mathcal F_a),
 \qquad |A|=\frac h2,
\tag{0.1}
\]

where every \(\mathcal F_a\) is a spanning \(2\)-factor consisting of

\[
 \frac{2^h}{2h}
\tag{0.2}
\]

vertex-disjoint \(C_{2h}\)'s.  Every cycle has transition-direction word

\[
 1,2,\ldots,h,\ 1,2,\ldots,h.
\tag{0.3}
\]

The proof is a Hamming-syndrome construction.  Its extra ingredient beyond
the vertex-tiling argument is a parity functional which takes value one on
every coordinate syndrome.  A codimension-two syndrome subspace then
resolves all cube edges.

Embedding one resolution class in every sufficiently large orientation
cube of a fixed coordinate-pair decomposition partitions all middle sets
except those having fewer than \(h\) split pairs.  If

\[
 \sqrt{m\log m}\ll h\ll m,
\tag{0.4}
\]

that exceptional family is in fact exponentially small relative to
\(\binom{2m}{m}\), and hence \(o(W)\).

## 1. The standard isometric cycle

Let

\[
 V=\mathbb F_2^h
\]

with standard basis \(e_1,\ldots,e_h\), and put

\[
 p_0=0,\qquad p_i=e_1+\cdots+e_i\quad(1\le i\le h).
\tag{1.1}
\]

The standard cycle has ordered vertex list

\[
 p_0,p_1,\ldots,p_{h-1},
 p_h+p_0,p_h+p_1,\ldots,p_h+p_{h-1},p_0.
\tag{1.2}
\]

Since \(p_h=\mathbf1\), its direction word is (0.3).  Every arc of at
most \(h\) edges uses distinct coordinate directions.  Its endpoints
therefore have Hamming distance equal to the arc length.  Thus (1.2) is an
isometric \(C_{2h}\).

Write \(P\) for its \(2h\)-element vertex set.

## 2. An alternating syndrome enumeration

Let

\[
 U=\mathbb F_2^t,\qquad
 Q=U\oplus\langle v\rangle\cong\mathbb F_2^{t+1}.
\tag{2.1}
\]

Choose a nonzero functional

\[
 \lambda:U\longrightarrow\mathbb F_2.
\tag{2.2}
\]

The two fibers of \(\lambda\) both have size \(h/2\).  We may therefore
enumerate \(U\) as

\[
 u_0,u_1,\ldots,u_{h-1},
\qquad
 u_0=0,\qquad
 \lambda(u_i)=i\pmod2.
\tag{2.3}
\]

Define a linear syndrome map \(\phi:V\to Q\) on the coordinate basis by

\[
 \begin{aligned}
 c_i:=\phi(e_i)&=u_i+u_{i-1} &&(1\le i<h),\\
 c_h:=\phi(e_h)&=v+u_{h-1}.
 \end{aligned}
\tag{2.4}
\]

Telescoping gives

\[
 \phi(p_i)=u_i\quad(0\le i<h),
\qquad
 \phi(\mathbf1)=\phi(p_h)=v.
\tag{2.5}
\]

Consequently

\[
 \phi(\mathbf1+p_i)=v+u_i,
\tag{2.6}
\]

so \(\phi\) maps \(P\) bijectively onto all of \(Q\).

Let

\[
 K=\ker\phi.
\tag{2.7}
\]

Then

\[
 |K|=2^{h-(t+1)}=\frac{2^h}{2h},
\tag{2.8}
\]

and the cycles

\[
 \{P+k:k\in K\}
\tag{2.9}
\]

partition \(V\).  Indeed, equality \(p+k=p'+k'\) implies
\(\phi(p)=\phi(p')\), hence \(p=p'\) by (2.5)--(2.6), and then \(k=k'\).
The cardinalities in (2.8) finish the proof.

Thus (2.9) is one spanning resolution class.  We next resolve all edges.

## 3. The parity functional and the resolution subspace

Extend \(\lambda\) to a functional \(\Lambda:Q\to\mathbb F_2\) by

\[
 \Lambda(u+\varepsilon v)=\lambda(u),
\tag{3.1}
\]

and let

\[
 M(u+\varepsilon v)=\varepsilon.
\tag{3.2}
\]

By (2.3)--(2.4),

\[
 \Lambda(c_i)=1\qquad(1\le i\le h).
\tag{3.3}
\]

In particular,

\[
 \Lambda(\phi(x))=\sum_{i=1}^h x_i,
\tag{3.4}
\]

so the syndrome code \(K\) is even.  Also

\[
 \Lambda(v)=0,\qquad M(v)=1.
\tag{3.5}
\]

Put

\[
 A=\ker\Lambda\cap\ker M
   =\{u\in U:\lambda(u)=0\}.
\tag{3.6}
\]

Then

\[
 \dim A=t-1,\qquad |A|=\frac h2.
\tag{3.7}
\]

For every coordinate direction \(i\), (3.3) and (3.5) imply

\[
 Q=A\oplus\langle c_i,v\rangle.
\tag{3.8}
\]

Indeed, the images of \(c_i,v\) under \((\Lambda,M)\) are respectively
\((1,M(c_i))\) and \((0,1)\), so they form a basis of \(Q/A\).

For each \(a\in A\), choose any \(z_a\in V\) with

\[
 \phi(z_a)=a,
\tag{3.9}
\]

and define the translated factor

\[
 \mathcal F_a=\{P+k+z_a:k\in K\}.
\tag{3.10}
\]

Every \(\mathcal F_a\) is a vertex partition into isometric
\(C_{2h}\)'s, being a translate of (2.9).

## 4. Exact edge resolution

### Theorem 4.1 (resolvable Hamming-cycle decomposition)

The \(h/2\) factors in (3.10) are pairwise edge-disjoint and together
cover every edge of \(Q_h\).

#### Proof

Fix direction \(i<h\).  In the quotient \(Q\), the base factor
\(\mathcal F_0\) uses the two \(c_i\)-edges

\[
 \{u_{i-1},u_i\},\qquad
 \{v+u_{i-1},v+u_i\}.
\tag{4.1}
\]

Their four endpoints form the affine plane

\[
 u_{i-1}+\langle c_i,v\rangle.
\tag{4.2}
\]

For \(i=h\), the two quotient edges are

\[
 \{u_{h-1},v\},\qquad
 \{v+u_{h-1},0\},
\tag{4.3}
\]

and their endpoints again form an affine plane parallel to
\(\langle c_h,v\rangle\).

Translation by \(z_a\) translates these quotient planes by \(a\).
Equation (3.8) says that

\[
 \{a+q_i+\langle c_i,v\rangle:a\in A\}
\tag{4.4}
\]

partitions \(Q\), for the appropriate base point \(q_i\).  Each plane in
(4.4) contains exactly two edges in direction \(c_i\).  Hence, as
\(a\) ranges over \(A\), the quotient edges selected in direction \(c_i\)
are precisely all \(h=|Q|/2\) such edges, once each.

Finally, every quotient \(c_i\)-edge has exactly \(|K|\) lifts to
direction-\(i\) edges of \(V\), and each factor in (3.10) contains all
those lifts over its two selected quotient edges.  Thus the factors
partition all direction-\(i\) edges of \(Q_h\).  This holds independently
for every \(i=1,\ldots,h\), proving the theorem. \(\square\)

The construction therefore has two simultaneous resolutions:

* inside one factor, \(K\) indexes the vertex-disjoint cycles;
* across factors, \(A\) indexes the edge-resolution classes.

The count is exact:

\[
 \frac h2\cdot\frac{2^h}{2h}\cdot2h
 =h2^{h-1}=|E(Q_h)|.
\tag{4.5}
\]

## 5. Signed transition words

Let the two coordinates in active pair \(i\) be

\[
 P_i=\{a_i,b_i\},
\]

and encode orientation \(0\) by choosing \(a_i\), orientation \(1\) by
choosing \(b_i\).  If a cycle starts at orientation
\(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_h)\), its signed
transition word is

\[
 \begin{array}{rcl}
 i=1,\ldots,h:
 &P_i^{\varepsilon_i}&\longrightarrow P_i^{1-\varepsilon_i},\\[1mm]
 i=1,\ldots,h:
 &P_i^{1-\varepsilon_i}&\longrightarrow P_i^{\varepsilon_i}.
 \end{array}
\tag{5.1}
\]

Here \(P_i^0=a_i\) and \(P_i^1=b_i\).  Thus every active pair is flipped
once in the first half and once, in the reverse signed direction but the
same coordinate order, in the second half.  Translation changes only
\(\varepsilon\), not the unsigned direction word (0.3).

More generally a coordinate permutation \(\pi\) changes (0.3) to

\[
 \pi(1),\ldots,\pi(h),\ \pi(1),\ldots,\pi(h).
\tag{5.2}
\]

## 6. Embedding in fixed-pair middle occupancy cubes

Fix a perfect matching of a \(2m\)-element ground set:

\[
 \mathcal P=\{P_1,\ldots,P_m\},\qquad |P_i|=2.
\tag{6.1}
\]

For a middle set \(X\in\binom{[2m]}m\), call a pair full, empty, or split
according as \(X\) contains two, zero, or one of its elements.  If

\[
 f(X),e(X),d(X)
\]

are the three counts, then

\[
 f(X)=e(X),\qquad 2f(X)+d(X)=m.
\tag{6.2}
\]

Fix the full-pair set, the empty-pair set, and the set \(D\) of split
pairs, with \(|D|=d\).  Choosing one endpoint in each split pair identifies
the resulting middle-set stratum with

\[
 Q_d.
\tag{6.3}
\]

If \(d\ge h\), choose and order \(h\) of its split-pair directions, fix the
remaining \(d-h\) orientations, and apply one resolution class
\(\mathcal F_a\) in every resulting \(Q_h\)-fiber.  The fibers are
disjoint, and each \(\mathcal F_a\) is a vertex partition.  Hence the whole
stratum partitions into partial pair-flip \(C_{2h}\)'s.

Every cube edge is a Johnson exchange inside one fixed coordinate pair.
Every arc of at most \(h\) transitions in a cycle uses distinct pairs, so
the embedded cycles remain isometric Johnson cycles.  Full pairs, empty
pairs, and inactive split orientations form the fixed exterior core.

Thus:

### Theorem 6.1 (exact fixed-pair Stage A)

For every power of two \(h\), every middle occupancy stratum with at least
\(h\) split pairs has an explicit vertex partition into isometric
\(C_{2h}\) partial pair-flip cycles, all with transition word (5.1).

## 7. The low-split exceptional mass

The number of middle sets with exactly \(d\) split pairs is

\[
 A_d=
 \begin{cases}
 \displaystyle
 \binom md
 \binom{m-d}{(m-d)/2}2^d,&m-d\text{ even},\\[3mm]
 0,&m-d\text{ odd}.
 \end{cases}
\tag{7.1}
\]

Indeed, choose the split-pair indices and their orientations, then choose
half of the remaining pairs to be full and the other half empty.

Using

\[
 \binom{m-d}{(m-d)/2}\le2^{m-d},
\tag{7.2}
\]

we obtain

\[
 \sum_{d<h}A_d
 \le 2^m\sum_{d<h}\binom md.
\tag{7.3}
\]

Let \(\alpha=h/m\).  If \(h=o(m)\), then \(\alpha\to0\), and the entropy
bound gives

\[
 \sum_{d<h}\binom md
 \le \exp\!\big(mH(\alpha)+o(m)\big)
 =\exp(o(m)),
\tag{7.4}
\]

where

\[
 H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)=o(1).
\]

On the other hand,

\[
 W=\binom{2m}m\ge\frac{4^m}{2m+1}.
\tag{7.5}
\]

Combining (7.3)--(7.5),

\[
 \frac{\sum_{d<h}A_d}{W}
 \le
 (2m+1)\exp\!\big(-m\log2+o(m)\big)
 =o(1).
\tag{7.6}
\]

This is exponentially stronger than required and uses only \(h=o(m)\).
In particular it applies throughout (0.4):

\[
 \boxed{\sum_{d<h}A_d=o(W).}
\tag{7.7}
\]

If a target shadow depth \(H\) satisfies

\[
 H=\Theta(\sqrt{m\log m}),\qquad H\ll h,
\tag{7.8}
\]

then the number of good cycles is at most \(W/(2h)\), so copying or padding
\(O(H)\) states per cycle costs

\[
 O\!\left(\frac{HW}{h}\right)=o(W).
\tag{7.9}
\]

Repairing every exceptional middle set literally costs \(o(W)\) at unit
cost.  If \(O(H)\) copies per exceptional set are required, choose \(h\)
with enough room to make

\[
 H\sum_{d<h}A_d=o(W),
\tag{7.10}
\]

which follows automatically from the exponential estimate (7.6) for every
subexponential \(H\), in particular for (7.8).

## 8. Scope

Proved here:

1. the full resolvable edge decomposition of \(Q_h\) into isometric
   \(C_{2h}\)'s for every \(h=2^t\ge2\);
2. a vertex partition in every resolution class;
3. the exact unsigned and signed transition-direction words;
4. the embedding into all occupancy cubes of dimension \(d\ge h\); and
5. the exponentially small \(d<h\) exceptional mass whenever \(h=o(m)\).

This completes fixed-pair Stage A, including its resolution structure.
It does not solve Stage B: one fixed coordinate pairing has the previously
recorded type-capacity obstruction for deep lower and upper shadows.

