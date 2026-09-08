# The first overlapping two-seed \(Q_2\) completion gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

There is a natural first common carrier for two coordinate-overlapping
pair-frame associators:

\[
 \mathcal U=
 \left\{X\cup Y:
 X\in\binom{[6]}3,\quad
 Y\in\{uw,ux,vw,vx\}\right\}.
\tag{0.1}
\]

It has \(20\cdot4=80\) middle owners.  On the six special coordinates the
four perfect matchings

\[
\begin{aligned}
 M_{00}&=12\mid34\mid56,\\
 M_{10}&=13\mid24\mid56,\\
 M_{01}&=12\mid35\mid46,\\
 M_{11}&=13\mid25\mid46
\end{aligned}
\tag{0.2}
\]

form a genuine square in the matching-switch graph.  Consecutive
recouplings overlap in coordinates and propagate their unchanged pair.

Every matching \(M\) and every distinguished edge \(r\in M\) have an
explicit exact factor \(\mathscr D(M;r)\) of \(\mathcal U\) into twenty
physical \(Q_2\)'s.  Thus four distinct exact common-support corners
exist.  Moreover, if adjacent matchings \(M,M'\) share \(r\), then

\[
                 \mathscr D(M;r)\longleftrightarrow
                 \mathscr D(M';r)
\tag{0.3}
\]

is exactly two disjoint copies of the certified \(24\)-owner pair-frame
associator, together with an identical complement.

The first nontrivial obstruction to using four *canonical* corner factors
is exact:

\[
\boxed{\text{No choice of the four distinguished edges makes all four
edges of (0.2) canonical associator trades.}}
\tag{0.4}
\]

At each matching state, the two incident square edges preserve two
different matching pairs.  But a \(Q_2\)-factor of the central all-split
\(Q_3\) fixes exactly one coordinate pair.  Canonicality of an incident
trade forces that fixed pair to be the pair preserved on that edge.
The two requirements at one corner are incompatible.

This canonical obstruction is sharp.  A noncanonical joint retile of the
same \(80\)-owner carrier exists explicitly.  There are four factors
\(\mathscr F_{00},\mathscr F_{10},\mathscr F_{01},\mathscr F_{11}\)
with lower pair-type ledgers

\[
\begin{array}{c|c}
\text{corner}&\text{lower base-type ledger}\\ \hline
00&32f_0+48f_1\\
10&48f_0+32f_1\\
01&48f_0+32f_1\\
11&64f_0+16f_1.
\end{array}
\tag{0.5}
\]

Hence each Boolean bit has the identical, background-independent signed
drift

\[
                         16(e_0-e_1),
\tag{0.6}
\]

including on the two upper edges of the square.  The upper excess ledger
has the same table shifted from \(f_0,f_1\) to \(f_1,f_2\).

All four factors possess one common \(\mathbb Z_4\) owner colouring.
Consequently they have a common-support phase-compatible suspension to
twenty physical \(C_{2h}\)'s for every \(h\ge2\).  This is a literal
two-seed, nonproduct, long-cycle associator.  It escapes the forced-axis
obstruction by using different central \(Q_3\) face axes in different
parts of the final corner.

The action-ceiling audit also sharpens.  In the fully product-transversal
tensor of the original \(24\)-owner atoms, one touched new-shore block
erases a Bernoulli contribution of mean \(1/3\).  Hence the unsuspended
tensor has exact mean death \(q/3\) per start, whereas the uniform
rank-\((m-q)\) pair-type law requires \(q/2+O_A(1)\).  The canonical
product tensor therefore already has the wrong birth--death drift, even
before its \(\Theta(W)\) certified collar is charged.  The more general
rowwise bound

\[
                 \mathsf W_1(\nu_q,V)\le {2tq\over h}W
\tag{0.7}
\]

remains correct and is the appropriate statewise ceiling for arbitrary
radius-\(t\) pair-geodesic Hamming rows.

## 1. A square of genuinely overlapping matching switches

Two perfect matchings of six labelled points are adjacent when they agree
on one edge and differ by a four-coordinate recoupling on the other four
points.  The four states in (0.2) have shared edges

\[
\begin{array}{c|c}
\text{matching-square edge}&\text{shared pair}\\ \hline
00-10&56\\
00-01&12\\
10-11&13\\
01-11&46.
\end{array}
\tag{1.1}
\]

For example,

\[
 12\mid34\mid56
 \longleftrightarrow
 13\mid24\mid56
\tag{1.2}
\]

recouples the first four coordinates, while

\[
 13\mid24\mid56
 \longleftrightarrow
 13\mid25\mid46
\tag{1.3}
\]

recouples \(24\mid56\) to \(25\mid46\).  The second operation therefore
uses an edge produced or retained after the first; it is not a
coordinate-disjoint Boolean tensor.

At every corner the two incident shared pairs are distinct:

\[
\begin{array}{c|c}
00&56,\ 12\\
10&56,\ 13\\
01&12,\ 46\\
11&13,\ 46.
\end{array}
\tag{1.4}
\]

This elementary observation becomes the exact factor obstruction in
Section 4.

## 2. The \(80\)-owner common carrier

Let the two unchanged reservoir pairs be

\[
                         R_1=\{u,v\},\qquad R_2=\{w,x\},
\tag{2.1}
\]

and let

\[
                         Q_R=(uw,vw,vx,ux).
\tag{2.2}
\]

The carrier \(\mathcal U\) in (0.1) consists of a special three-set and
one selected endpoint from each reservoir pair.  Every owner has rank
five.  Relative to any matching \(M=\{r,p,q\}\) of the six special
coordinates, a special three-set has one of exactly two forms:

1. it splits all three pairs \(r,p,q\); or
2. it splits one pair, fills one pair, and empties one pair.

There are respectively

\[
                         2^3=8,\qquad 3\cdot2\cdot2=12
\tag{2.3}
\]

special sets of the two kinds.

## 3. Twenty-square factors

Fix \(M=\{r,p,q\}\) and distinguish \(r\).

* For every reservoir orientation \(Y\), and for each of the two
  orientations of \(r\), fix those choices and vary independently the
  selected endpoints in \(p\) and \(q\).  This is one physical \(Q_2\).
  These choices give \(4\cdot2=8\) cells and cover all owners whose
  special part splits every \(M\)-pair.
* For each of the twelve special sets \(X\) of the second kind, take the
  reservoir square \(X\cup Q_R\).

Denote the resulting family by \(\mathscr D(M;r)\).

### Theorem 3.1 (exact common-support factor)

\(\mathscr D(M;r)\) is a partition of \(\mathcal U\) into twenty
pairwise vertex-disjoint physical \(Q_2\)'s.

#### Proof

The eight all-split special sets are partitioned into two faces of their
orientation cube \(Q_3\), according to the chosen endpoint of \(r\).
For each of four fixed reservoir orientations this gives two disjoint
\(Q_2\)'s, hence eight cells.  The other twelve special sets are
disjoint, and the reservoir square over each contains its four possible
reservoir orientations.  The two special classes are disjoint and
exhaust \(\binom{[6]}3\).  Therefore the twenty cells cover

\[
                         8\cdot4+12\cdot4=80
\]

owners exactly once.  Every displayed cell varies two swaps on disjoint
coordinate pairs, so it is a physical Johnson \(Q_2\). \(\square\)

Consequently any choices

\[
 \mathscr D(M_{00};r_{00}),\quad
 \mathscr D(M_{10};r_{10}),\quad
 \mathscr D(M_{01};r_{01}),\quad
 \mathscr D(M_{11};r_{11})
\tag{3.1}
\]

with \(r_{ij}\in M_{ij}\) give four distinct exact factors on one common
owner support.  This proves weak four-corner exactness without any
additive double coverage.

## 4. Exact canonical edge criterion

Let adjacent matchings \(M,M'\) share the pair \(r\).  They induce two
different matchings on the complementary four-set.

### Theorem 4.1 (one edge is two literal associators)

The trade

\[
                         \mathscr D(M;r)
 \longleftrightarrow    \mathscr D(M';r)
\tag{4.1}
\]

is the disjoint union of two copies of the certified \(24\)-owner
pair-frame associator, indexed by the two orientations of \(r\), plus
identical cells off that support.

#### Proof

First restrict to owners for which \(r\) is split.  Fixing one of its two
orientations leaves a rank-two special set on the complementary
four-set, together with the two split reservoir pairs.  This is exactly
the \(24\)-owner carrier

\[
                   \binom{[4]}2\square Q_R.
\tag{4.2}
\]

In \(\mathscr D(M;r)\), the four configurations splitting both
complementary \(M\)-pairs form their local square at every fixed
reservoir orientation, while the two full/empty configurations use
reservoir squares.  This is the old canonical shore.  Replacing the
complementary matching by that of \(M'\) gives exactly the new canonical
shore.  The two orientations of \(r\) give two disjoint copies.

If \(r\) is full or empty, the complementary special set has rank one or
three.  Relative to either complementary matching it has exactly one
split pair, and \(\mathscr D(M;r)\) and \(\mathscr D(M';r)\) both use the
same reservoir square at that fixed special set.  Thus the complement of
the two active copies is identical. \(\square\)

The converse is visible on the central sector.

### Lemma 4.2 (the distinguished edge is forced)

Suppose \(M,M'\) share \(r\), and an edge of a four-corner construction
using factors of the form \(\mathscr D(M;a)\) and
\(\mathscr D(M';b)\) is required to be precisely the canonical
pair-frame trade on the \(r\)-split slab, with the complement unchanged.
Then

\[
                              a=b=r.
\tag{4.3}
\]

#### Proof

Consider the eight special sets splitting all three \(M\)-pairs.  They
form the orientation cube \(Q_3\).  The old canonical associator on the
\(r\)-split slab fixes the orientation of \(r\) and uses the two faces
which vary the other two pair directions.  But the all-split part of
\(\mathscr D(M;a)\) is, by definition, the two-face factor fixing \(a\).
The two face factors of \(Q_3\) are equal only when their fixed
coordinate is equal.  Hence \(a=r\).  The same argument on the new shore
gives \(b=r\). \(\square\)

### Theorem 4.3 (no canonical four-edge square)

There is no choice \(r_{ij}\in M_{ij}\) for which every edge of the
matching square (0.2) is a canonical pair-frame associator trade between
the corresponding factors \(\mathscr D(M_{ij};r_{ij})\).

#### Proof

At corner \(00\), canonicality of the edge \(00-10\) forces
\(r_{00}=56\) by Lemma 4.2, while canonicality of \(00-01\) forces
\(r_{00}=12\).  These pairs are distinct.  This is already a
contradiction.  The same incompatibility appears at every corner by
(1.4). \(\square\)

This obstruction is stronger than failure of the matching flips to
commute as fixed coordinate operations.  The matching states themselves
do form the square (0.2); what fails is a common completed \(Q_2\)-factor
at its vertices which realizes every square edge by the known signed
atom.

## 5. The forced re-axis toll

The obstruction has a concrete signed interpretation.  Measure lower
full-pair type relative to the base matching

\[
                         M_{00}=12\mid34\mid56.
\tag{5.1}
\]

For \(\mathscr D(M_{00};r)\), every one-split special state contains one
full base pair.  Its twelve reservoir squares contribute

\[
                         12\cdot4=48
\tag{5.2}
\]

type-one lower edges, while the all-split faces contribute none.

Take the path \(00\to10\to11\).  The first canonical edge uses
\(r=56\).  The two local associator copies remove \(2\cdot8=16\)
type-one occurrences:

\[
\begin{array}{c|c}
\text{factor}&\text{base type-one lower edges}\\ \hline
\mathscr D(M_{00};56)&48\\
\mathscr D(M_{10};56)&32.
\end{array}
\tag{5.3}
\]

The second canonical edge must instead fix the shared pair \(13\).
Changing the central \(Q_3\) face axis gives

\[
                         \mathscr D(M_{10};13):40
\tag{5.4}
\]

base type-one edges.  Indeed the twelve vertical special states
contribute \(32\).  In the all-split \(M_{10}\)-cube, fixing \(13\) and
varying \(24,56\) gives two base-pair intersections per reservoir
orientation, hence eight more.  The re-axis step restores eight of the
sixteen deaths before the second seed is applied.

Finally

\[
                         \mathscr D(M_{11};13):32.
\tag{5.5}
\]

For \(M_{11}=13\mid25\mid46\), whose union with \(M_{00}\) is one
alternating six-cycle, six of the twelve one-split special sets contain
a base full pair, contributing \(24\).  In the all-split cube, each of
the two active directions leaves the other two new pairs; exactly one of
their four endpoint choices is a base pair.  This contributes two edges
per reservoir orientation, hence eight.  Thus the second canonical edge
removes only the eight occurrences paid back by re-axis:

\[
                         48\longrightarrow32
                         \longrightarrow40
                         \longrightarrow32.
\tag{5.6}
\]

The net base-type action is one \(16\)-occurrence layer, not two
independent layers.  This calculation is an illustration of Theorem 4.3,
not a universal invariant for arbitrary \(Q_2\)-tilings of
\(\mathcal U\).

## 6A. An explicit noncanonical two-seed square

We now retile the central sector and attain two independent signed layers.
Let

\[
                         \mathscr F_{00}
 =\{X\cup Q_R:X\in\binom{[6]}3\}.
\tag{6.1}
\]

This is the all-vertical factor of twenty reservoir squares.  Put

\[
 \mathscr F_{10}=\mathscr D(M_{10};56),
 \qquad
 \mathscr F_{01}=\mathscr D(M_{01};12).
\tag{6.2}
\]

To define the final corner, use at every fixed reservoir orientation
\(Y\) the following four special \(Q_2\)'s, in the displayed cyclic
orders:

\[
\begin{aligned}
 S_1&=(125,235,345,145),\\
 S_2&=(126,246,346,136),\\
 S_3&=(134,146,156,135),\\
 S_4&=(234,245,256,236).
\end{aligned}
\tag{6.3}
\]

Every consecutive pair differs by one coordinate swap, and the two
directions of each row are disjoint:

\[
\begin{array}{c|c}
S_1&13,\ 24\\
S_2&14,\ 23\\
S_3&36,\ 45\\
S_4&35,\ 46.
\end{array}
\tag{6.4}
\]

The sixteen special sets in (6.3) are distinct.  The four missing
three-sets are

\[
                         123,\quad124,\quad356,\quad456.
\tag{6.5}
\]

Define

\[
 \mathscr F_{11}
 =
 \{S_j\cup Y:1\le j\le4,\ Y\in\{uw,ux,vw,vx\}\}
 \mathbin{\dot\cup}
 \{X\cup Q_R:X\in\{123,124,356,456\}\}.
\tag{6.6}
\]

### Theorem 6.1 (literal four-corner completion)

Every \(\mathscr F_{\epsilon_1\epsilon_2}\) is a partition of the
identical \(80\)-owner support \(\mathcal U\) into twenty physical
\(Q_2\)'s.

#### Proof

Exactness of the first three factors follows from Theorem 3.1 and the
definition of the all-vertical factor.  In (6.6), the four special
squares partition sixteen special three-sets at each of the four fixed
reservoir orientations, giving sixteen disjoint \(Q_2\)'s and covering
sixty-four owners.  The four reservoir squares over (6.5) cover the
remaining sixteen owners.  Equation (6.4) proves physical
geodesicity. \(\square\)

The retile can be read as an exact buffer allocation.  The first two
death families are

\[
\begin{aligned}
\mathcal A&=\{125,126,345,346\},\\
\mathcal B&=\{134,234,156,256\},
\end{aligned}
\tag{6.7}
\]

while the all-split buffer is

\[
\mathcal T=\{135,136,145,146,235,236,245,246\}.
\tag{6.8}
\]

Every square in (6.3) contains two members of
\(\mathcal A\cup\mathcal B\) and two members of \(\mathcal T\), and the
four buffer pairs partition \(\mathcal T\).  The choices deliberately use
different face axes:

\[
\begin{array}{c|c}
S_1&\{235,145\}\\
S_2&\{246,136\}\\
S_3&\{146,135\}\\
S_4&\{245,236\}.
\end{array}
\tag{6.9}
\]

This is exactly how the construction evades Theorem 4.3.

## 6B. Exact two-sided signed ledger

Continue to measure type in the five-pair base frame

\[
                         12\mid34\mid56\mid uv\mid wx.
\tag{6.10}
\]

Every lower edge has type zero or one.  In the all-vertical factor,
twelve special sets contain one base full pair and eight are all-split,
so

\[
                         \mathscr F_{00}^-:
                         32f_0+48f_1.
\tag{6.11}
\]

The count for \(\mathscr F_{10}\) is (5.3), and symmetry gives the same
count for \(\mathscr F_{01}\):

\[
                         \mathscr F_{10}^-=
                         \mathscr F_{01}^-:
                         48f_0+32f_1.
\tag{6.12}
\]

Every edge of every special square in (6.3) has type zero.  For example,
the four special intersections of \(S_1\) are

\[
                         25,\quad35,\quad45,\quad15,
\]

none a base pair; the other rows have the same property.  The four
vertical special sets in (6.5) each contain one base full pair and
contribute four type-one edges.  Hence

\[
                         \mathscr F_{11}^-:
                         64f_0+16f_1.
\tag{6.13}
\]

Equations (6.11)--(6.13) prove the affine Boolean identity

\[
 \boxed{
 L^-_{\epsilon_1,\epsilon_2}
 =32f_0+48f_1+
   16(\epsilon_1+\epsilon_2)(f_0-f_1).}
\tag{6.14}
\]

Thus both seed differences are identical on both parallel edges; there is
no interaction term in the aggregate lower type ledger.

The upper statement is equally exact.  The complement of an upper
rank-six edge is a lower rank-four edge.  In a universe of five base
pairs, a rank-four set with \(f\) full pairs has \(f+1\) empty pairs.
Therefore an upper edge has \(f+1\) full pairs precisely when its
complementary lower edge has \(f\) full pairs.  Complement preserves the
aggregate lower counts of every factor above:

* \(\mathscr F_{00},\mathscr F_{10},\mathscr F_{01}\) are
  complement-stable as factor families;
* the complement of \(\mathscr F_{11}\) again consists of four
  zero-type special squares and the same four vertical special states in
  complementary pairs.

Consequently

\[
 \boxed{
 L^+_{\epsilon_1,\epsilon_2}
 =32f_1+48f_2+
   16(\epsilon_1+\epsilon_2)(f_1-f_2).}
\tag{6.15}
\]

The two seed bits therefore have matched useful lower and upper drift.

## 6C. One common phase colouring and all-length suspension

Order the reservoir orientations as

\[
                         y_0=uw,\quad y_1=vw,\quad
                         y_2=vx,\quad y_3=ux.
\tag{6.16}
\]

Define \(g:\binom{[6]}3\to\mathbb Z_4\) by

\[
\begin{array}{c|rrrrrrrr}
X&125&235&345&145&126&236&346&146\\ \hline
g(X)&0&3&2&1&0&1&2&3
\end{array}
\tag{6.17}
\]

\[
\begin{array}{c|rrrrrrrr}
X&246&136&134&156&135&234&245&256\\ \hline
g(X)&1&3&0&2&1&0&3&2
\end{array}
\tag{6.18}
\]

and set

\[
                         g(123)=g(124)=g(356)=g(456)=0.
\tag{6.19}
\]

Finally colour every owner by

\[
                         c(X\cup y_k)=g(X)+k\pmod4.
\tag{6.20}
\]

### Lemma 6.2 (simultaneous phase compatibility)

The restriction of \(c\) to every \(Q_2\) cell in every one of the four
factors is \(0,1,2,3\) in a cyclic order, up to an overall rotation and
reversal.

#### Proof

On a vertical reservoir square, (6.20) is

\[
                         g(X),g(X)+1,g(X)+2,g(X)+3.
\]

The special squares needed by \(\mathscr F_{10}\) are

\[
\begin{aligned}
(125,235,345,145)&:(0,3,2,1),\\
(126,236,346,146)&:(0,1,2,3).
\end{aligned}
\]

Those needed by \(\mathscr F_{01}\) are

\[
\begin{aligned}
(134,145,156,136)&:(0,1,2,3),\\
(234,245,256,236)&:(0,3,2,1).
\end{aligned}
\]

The four final-corner rows (6.3) have colour sequences

\[
                         (0,3,2,1),\quad(0,1,2,3),
                         \quad(0,3,2,1),\quad(0,3,2,1).
\]

Adding the fixed reservoir offset \(k\) only rotates the colours.
This checks every nonvertical cell; the remaining cells are vertical.
\(\square\)

Adjoin \(h-2\) split coordinate pairs.  Apply the standard coloured-square
suspension to every cell: a square with directions \(\alpha,\beta\) is
replaced by the physical \(C_{2h}\) with direction word

\[
 \alpha,\beta,e_1,\ldots,e_{h-2},
 \alpha,\beta,e_1,\ldots,e_{h-2}.
\tag{6.21}
\]

The tail-orientation fibre above a base owner depends only on its colour.
Lemma 6.2 therefore implies:

### Theorem 6.3 (common-support all-length two-seed associator)

For every \(h\ge2\), the four factors
\(\mathscr F_{00},\mathscr F_{10},\mathscr F_{01},\mathscr F_{11}\)
lift to four exact factors of one identical lifted owner support, each
consisting of twenty pairwise disjoint physical isometric
\(C_{2h}\)'s.  Every Boolean edge is a literal completed-factor trade.

This theorem proves long-cycle realizability of the local two-seed menu.
It does not assert that its four full-depth labelled carrier vectors are
affine, only the exact depth-one type ledgers (6.14)--(6.15).

## 6D. Near-spanning packing and tensorization

The local square has positive fixed density and tensorizes on
coordinate-disjoint copies.  Reserve

\[
                         B=\lfloor m/10\rfloor
\tag{6.22}
\]

disjoint ten-coordinate blocks for copies of \(\mathcal U\), and reserve
\(P=\lfloor m/2\rfloor\) disjoint spectator pairs in the remaining
ordinary coordinates.  Before conditioning on total rank, a ten-block is
eligible with probability

\[
                         {|\mathcal U|\over2^{10}}
                         ={80\over1024}={5\over64},
\tag{6.23}
\]

and a spectator pair is split with probability \(1/2\).

For a middle owner, choose its first \(r\) eligible ten-blocks and its
first \(s\) split spectator pairs, and freeze the exterior.  Both lists
are stable under variation in

\[
                         \mathcal U^r\square Q_s.
\tag{6.24}
\]

Exactly as in the first-eligible packet proof, the distinct sets (6.24)
partition every owner having enough eligible blocks and split pairs.

### Theorem 6.4 (macroscopic two-seed tensor)

Assume

\[
                         r\le {5B\over128},
 \qquad                   s\le {P\over4},
 \qquad                   h=2r+s=2^a.
\tag{6.25}
\]

Then a family of

\[
 G\ge W\left\{1-
 2(m+1)\left[
 e^{-5B/512}+e^{-P/16}\right]\right\}
\tag{6.26}
\]

middle owners is partitioned into canonical packets
\(\mathcal U^r\square Q_s\).  Every packet has \(4^r=2^{2r}\) exact
factor resolutions.  Each resolution partitions it into \(20^r\)
physical \(Q_h\)'s and hence into \(C_{2h}\)'s.  Every global resolution
has exactly

\[
                              {G\over2h}
\tag{6.27}
\]

long-cycle components.

#### Proof

The eligible-block count has mean \(5B/64\), and the first condition in
(6.25) is its half-mean threshold.  Chernoff gives
\(e^{-5B/512}\).  The split-pair half-mean tail is \(e^{-P/16}\).
Conditioning fair independent bits on total rank \(m\) costs at most the
factor \(2(m+1)\), proving (6.26).

Selector stability proves the packet partition.  At each of the \(r\)
local factors choose one of the four exact corners.  Products give

\[
 \mathcal U^r\square Q_s
 =\mathop{\dot\bigcup}_{20^r\text{ cells}}Q_{2r+s}.
\]

The power-of-two Hamming syndrome factor partitions each \(Q_h\) into
physical \(C_{2h}\)'s.  Counting owners gives (6.27). \(\square\)

Thus \(r=\Theta(\sqrt m)\) overlapping two-seed gadgets are available to
\(1-e^{-\Omega(m)}\) of all middle owners, with literal integrality and
one-copy ownership.  In the unsuspended case \(s=0\), a
product-transversal shallow window which touches \(q\) distinct gadgets
and selects corner \(11\) has aggregate mean death

\[
                              {2q\over5},
\tag{6.28}
\]

because (6.14) removes \(32/80=2/5\) of one type unit per touched gadget.
This improves the one-seed tensor's \(q/3\), but it is still below the
uniform target displacement \(q/2+O_A(1)\).  Equation (6.28) is an exact
aggregate statement for a product-transversal phase schedule; arbitrary
state-dependent phase and corner selections require the complete
occurrence-resolved carrier, not only its mean.

The exact visibility deficit is now one-dimensional.  Conditional on the
infinity bit, the source and depth-\(q\) target centres differ by

\[
 \Delta_{\varepsilon,q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}
 ={q\over2}+O_A(1).
\tag{6.29}
\]

One fully visible corner-\(11\) gadget contributes \(2/5\) of one type
unit.  Therefore the mean-sharp visible-gadget count is

\[
 \boxed{
 L^*_{\varepsilon,q}
 ={5\over2}\Delta_{\varepsilon,q}
 ={5q\over4}+O_A(1).}
\tag{6.30}
\]

A direction order which touches at most \(q\) distinct gadgets in a
\(q\)-window is short by \(q/4+O_A(1)\) gadget exposures, equivalently by
\(q/10+O_A(1)\) pair-type units.  In the symmetric product CLT this gives
the limiting total-variation gap

\[
                         2\Phi(A/5)-1.
\tag{6.31}
\]

Thus the local completion theorem changes the global gate sharply.  The
old demand was \(3q/2\) fresh one-seed exposures.  The nonproduct square
reduces it to \(5q/4\) completed gadget exposures.  A literal schedule
must make a second gadget simultaneously visible on one quarter of the
physical deletion phases, or must add another local retile which removes
half of the sixteen survivor-high occurrences left by corner \(11\).

## 6. Self-audit of the long-cycle action ceiling

Let a pair-geodesic \(C_{2h}\) row have direction word

\[
                         \pi_1\cdots\pi_h
                         \pi_1\cdots\pi_h
\tag{6.1}
\]

in a frame \(P'\) at matching-switch distance at most \(t\) from a base
frame \(P\).  At most \(2t\) of the active \(P'\)-pairs are absent from
\(P\).  For a lower cyclic \(q\)-window, only one of those bad directions
can break a base full pair.  Every bad direction occurs twice and belongs
to \(q\) cyclic windows.  Hence one row contributes at most

\[
                         2q(2t)=4qt
\tag{6.2}
\]

units of owner-to-target pair-type transport.  A factor on \(W\) owners
has \(W/(2h)\) rows, giving exactly the normalization

\[
                 \boxed{\mathsf W_1(\nu_q,V)
                         \le {2tq\over h}W.}
\tag{6.3}
\]

No independence is used.  The conclusion remains valid when different
rows choose different radius-\(t\) frames.  It also remains valid after
overlapping recouplings if the final row still has one pair-geodesic
Hamming frame.  It does **not** cover a new row with sequential
nontrivial frame monodromy and no single final pairing \(P'\).

The odd distinguished-coordinate model changes neither normalization nor
Gaussian scale when the constructed rows freeze the infinity bit.  If a
future row actively flips infinity, that direction must be added to the
bad-direction count.

At \(q=A\sqrt m+o(\sqrt m)\), the audited truncated-Lipschitz Gaussian
test gives

\[
 {H_q\over W}
 \ge {c_A\over R_A}
      -{2A\over R_A}{t\over h}-o(1).
\tag{6.4}
\]

Thus \(t/h=\Omega_A(1)\) is necessary for \(o(W)\) holes within this
scope.

## 7. Exact drift of the canonical product tensor

The general ceiling (6.3) is not tight for the canonical product factor.
On one local \(24\)-owner block the source type enumerator is

\[
                              M(z)=16+8z.
\tag{7.1}
\]

If a depth window touches the block on the new shore, its lower type
enumerator is \(24\).  Hence one touched block erases one Bernoulli
contribution of mean \(1/3\).

In a fully product-transversal tensor, assume the shallow direction order
touches \(q\) distinct associator blocks.  Then the exact source and
output enumerators differ by

\[
                         M(z)^t
 \quad\longrightarrow\quad
                         24^q M(z)^{t-q}.
\tag{7.2}
\]

After normalizing by \(24^t\), the mean pair-type death is exactly

\[
                              {q\over3}
\tag{7.3}
\]

per start.  By contrast a uniform rank-\(m\) source and uniform
rank-\((m-q)\) target in a fixed pair frame have mean full-pair
difference

\[
 {m(m-1)-(m-q)(m-q-1)\over2(2m-1)}
 ={q(2m-q-1)\over2(2m-1)}
 ={q\over2}+O_A(1)
\tag{7.4}
\]

when \(q=O_A(\sqrt m)\).

Thus the all-new canonical product tensor does not itself produce the
uniform target pair-type law: it supplies only two thirds of the required
mean death.  With \(s\) spectator directions and
\(h=2t+s\), an evenly phase-transversal order which never touches one
associator block twice in a \(q\)-window has mean death

\[
                              {2tq\over3h}.
\tag{7.5}
\]

This exact product calculation is stronger than (6.3) for that specific
factor.  It is not a universal obstruction to state-dependent shore
selection, biased phases, or arbitrary radius-\(t\) frame mixtures; those
remain governed by (6.3) and the full histogram, not only its mean.

## 8. Collar implication: corrected scope

A \(C_{2h}\)-factor has \(W/(2h)\) rows.  The standard certified
linearization deletes an \(H\)-collar at every cut, costing

\[
                              O(HW/h).
\tag{8.1}
\]

With \(t=O(H)=O(\sqrt m)\), this *particular collar-deletion
implementation* has the familiar tradeoff:

* \(h=O(t)\) retains possible matching action but certifies only a
  \(\Theta(W)\) collar bound;
* \(h/H\to\infty\) certifies an \(o(W)\) collar but gives \(t/h\to0\),
  and (6.4) leaves \(\Omega_A(W)\) holes.

This is not a universal seam lower bound.  Aligned or overlapping slab
collars might have a smaller union, and a future fused braid might use its
cross-seam windows rather than discard them.  Likewise the serial estimate
\(O(LHW/h)\) is the cost of literal independent slab collars, not a lower
bound on every \(L\)-layer construction.

## 9. Precise surviving gate

The following are proved.

1. The first coordinate-overlapping matching square exists explicitly.
2. Its natural \(80\)-owner carrier has four distinct exact \(Q_2\)
   factors on one common support.
3. Every individual matching-square edge can be realized by two literal
   certified associators plus an unchanged complement.
4. No four factors in the natural \(\mathscr D(M;r)\) family realize all
   four canonical edges simultaneously.
5. The obstruction is the forced face axis of the central all-split
   \(Q_3\), and its signed re-axis toll is explicit.
6. The noncanonical factors (6.1)--(6.6) escape that obstruction and
   realize the affine two-bit lower and upper ledgers
   \(48,32,32,16\).
7. The explicit colouring (6.17)--(6.20) gives one common-support
   all-length suspension into twenty \(C_{2h}\)'s at every length.
8. The rowwise Wasserstein ceiling and its normalization pass audit.
9. The canonical product tensor has exact drift \(q/3\), not the required
   \(q/2+O_A(1)\).

Not ruled out:

* an occurrence-resolved proof that the complete all-depth labelled
  carrier differences of the four suspended factors span the required
  Gaussian birth--death operator;
* a positive-density global packing in which many such two-seed gadgets
  remain independently selectable after long-cycle fusion;
* an \(o(W)\)-collar realization which does not dilute the local
  \(2/5\) two-bit depth-one action; or
* a monodromic braid not contained in one pair-geodesic Hamming frame.

The finite two-seed completion gate is therefore positive.  The next gate
is quantitative and global: tensor or pack the suspended \(80\)-owner
square so that its two bits are visible with the required frequency at
every Gaussian depth, while retaining one-copy ownership, cross-context
separation, and \(o(W)\) total collar charge.
