# Disjoint contextual reciprocal-`C_8` layers: exact cube, edit moment, and capacity ceiling

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let `F_s` be the canonical anchored `D_s`-port factor and put

\[
                         B=C_s=\operatorname {Cat}_s.
\]

At a top-level Dyck-component boundary after semilength `a`, where
`0<=a<=s-2`, the contextual reciprocal `C_8` matching is

\[
 P1100R\longleftrightarrow P1010R,qquad
 P\in D_a,\quad R\in D_{s-a-2}.                     \tag{0.1}
\]

Its exact number of two-root rectangles is

\[
                         \boxed{M_a=C_aC_{s-a-2}.}    \tag{0.2}
\]

Thus `M_a` is asymptotic to `B/16` only at the two endpoint boundaries
`a=0,s-2`.  For fixed `a`,

\[
                         {M_a\over B}\longrightarrow
                         {C_a\over4^{a+2}}.           \tag{0.3}
\]

Choose a set `A subseteq {0,...,s-2}` of pairwise disjoint four-bit
positions; equivalently,

\[
                         |a-b|\ge2\qquad(a\ne b\in A).             \tag{0.4}
\]

Then all complete matching layers in `A` are simultaneously legal.  They
commute as exact `X/Y` factor switches.  Their root matching union consists
of Boolean orbits of size at most `2^|A|`, and size `2^|A|` really occurs
on the all-singleton root when all selected positions fit.  Distinct layers
never give the same root pair; they merge through roots on which several
blocks are eligible.

If `G_A` is the all-on factor, then

\[
 \sum_{P\in D_s}d(F_s(P),G_A(P))=4\sum_{a\in A}M_a,                \tag{0.5}
\]

and every full `X/Y` ownership component of `F_s/G_A` has at most
`2^|A|` roots.  Consequently

\[
 \boxed{
 \Xi(F_s,G_A)le
       2^{|A|+2}{\sum_{a\in A}M_a\over B}.}           \tag{0.6}
\]

For every fixed number of layers this is `O(1)=o(sqrt(s))`.  Sparse-edit
rounding therefore does **not** obstruct the simultaneous construction.

The obstruction is supply and direction.  Among all disjoint position
sets, even allowing `|A|` to grow,

\[
 \boxed{
 \limsup_{s\to\infty}{1\over B}
       \max_A\sum_{a\in A}M_a={\sqrt2\over8}.}        \tag{0.7}
\]

Only the layer `a=0` changes the rooted first-insertion boundary; every
layer `a>0` lies after a nonempty complete Dyck prefix and leaves that
boundary fixed.  Thus the layers do not add in one common first-boundary
direction.

At the complete rank-`s-1` cyclic profile, one reciprocal rectangle has an
elementary square with negative mass two.  Hence, even granting perfect
background sign at every toggle, all disjoint layers have cap descent at
most

\[
                         \left({\sqrt2\over4}+o(1)\right)B.        \tag{0.8}
\]

This is below the parent demand `delta_theta B` whenever

\[
 \delta_\theta>{\sqrt2\over4},
 \qquad\text{equivalently}\qquad
 \theta>4+2\sqrt2.                                    \tag{0.9}
\]

If the physical consumer can use at most one signed unit per rectangle,
then (0.7) is already below the minimum demand `B/4`, and the architecture
fails throughout `4<=theta<16`.

For the proposed fixed range `u=4,...,7`, the maximum raw edge densities
are respectively

\[
 {9\over64},\quad {295\over2048},\quad
 {151\over1024},\quad {2449\over16384}.               \tag{0.10}
\]

These are not `u/16`.  Even at two ideal useful units per edge, the
corresponding capacities are at most

\[
 {9\over32},\quad {295\over1024},\quad
 {151\over512},\quad {2449\over8192},                 \tag{0.11}
\]

all below `0.3B`.  Hence no fixed four-to-seven disjoint-position family
can cover the hard parent sector.  Full carrier signs can only lower these
raw bounds.

## 1. One contextual matching

Write a Dyck root as a concatenation of top-level Dyck words.  Fix `a` and
consider roots containing at the boundary after a complete prefix `P` one
of the two length-four words

\[
                         1100,qquad1010.              \tag{1.1}
\]

Both are Dyck words of semilength two.  Replacing one by the other keeps
the prefix and suffix at height zero.  Thus every eligible unordered pair
has the unique form (0.1), proving the count (0.2).

Put

\[
                         \tau_a=(2a+2\  2a+3).       \tag{1.2}
\]

The MSW concatenation law

\[
                         \rho(PQ)=(\rho(P),2a+\rho(Q))              \tag{1.3}
\]

shows that the two old omitted-coordinate orders have a common prefix,
then the two four-letter patterns

\[
 (2a+4,2a+2,2a+3,2a+1),
 \quad
 (2a+2,2a+1,2a+4,2a+3),                              \tag{1.4}
\]

and then a common tail.  Cyclically moving the common prefix behind the
tail reduces (1.4) to the standard octahedral cut table.  Therefore the
two old rows and their `tau_a`-conjugate partners own exactly the same
complete middle and adjacent-union token sets.  They form one sealed
two-root component of the full `X/Y` overlay.

Switching any collection of the `M_a` disjoint pairs is consequently a
literal anchored exact factor operation.  In each changed rooted row the
two consecutive Johnson exchanges are reversed.  Its deletion half makes
one adjacent transposition and its insertion half makes one, so

\[
                              d(P)=2.                 \tag{1.5}
\]

## 2. Commutation of disjoint positions

For an eligible root `x`, let `r_a x` toggle its block at position `a`.
On the binary root word this is exactly the coordinate action of `tau_a`.
For a selected position set `A`, define

\[
 E_A(x)=\{a\in A:x\text{ has }1100\text{ or }1010
                     \text{ rooted at }a\}.           \tag{2.1}
\]

If (0.4) holds, toggling one selected block changes no bit in any other
selected block.  It also leaves a complete Dyck prefix of the same length
before every later block.  Therefore

\[
 E_A(r_ax)=E_A(x),qquad r_ar_bx=r_br_ax.              \tag{2.2}
\]

Let

\[
                         h_x=\prod_{a\in E_A(x)}\tau_a.             \tag{2.3}
\]

### Theorem 2.1 (simultaneous exact factor)

The all-on family has the row formula

\[
                         \boxed{G_A(x)=h_xF_s(h_xx).}              \tag{2.4}
\]

It is an anchored exact factor.  The matching layers may be applied in
any order.

#### Proof

Proceed by induction over the selected positions.  Suppose a set of
earlier layers has been applied.  For an `a`-matched root pair `x,r_ax`,
eligibility at every earlier disjoint position is identical on the two
roots.  Hence their current rows are obtained from the corresponding
canonical pair by one common coordinate conjugation `h` whose support is
disjoint from `tau_a`.

The canonical pair is the sealed reciprocal rectangle of Section 1.
Conjugating its complete token equality by `h` gives another literal
reciprocal rectangle in the current factor.  Switching all such disjoint
pairs preserves both complete ownership ledgers and every root/complement
port.  Since `h tau_a=tau_a h`, the updated row formula is (2.4), independent
of the order of application.  This proves both exactness and commutation.
\(\square\)

The maximum possible number of pairwise disjoint positions is

\[
                         \boxed{|A|\le\lfloor s/2\rfloor.}         \tag{2.5}
\]

## 3. Root merging, full components, and `Xi`

For `a!=b`, the matchings at `a` and `b` have no common edge: their two
roots differ on different four-bit supports.  They can have common
vertices.  The all-singleton root

\[
                              (10)^s                 \tag{3.1}
\]

is eligible at every position, so it witnesses simultaneous incidence
with every selected layer.  On an orbit with `e=|E_A(x)|`, the partial
involutions freely flip `e` disjoint blocks.  The root matching component
is therefore a Boolean cube of size `2^e`.

Every sequential switch in Theorem 2.1 moves ownership only among rows of
this root cube.  Consequently no token edge in the direct full overlay of
`F_s,G_A` leaves the cube.  The direct full components may refine it, but
they cannot be larger.  Thus

\[
                              b_K\le2^{|A|}.           \tag{3.2}
\]

The local exchange intervals belonging to disjoint four-bit positions are
disjoint in the concatenated MSW phase order.  Hence their two adjacent
inversions per rooted row add without cross inversions:

\[
                         d(F_s(x),G_A(x))=2|E_A(x)|.  \tag{3.3}
\]

Double-counting eligible roots gives

\[
\begin{aligned}
 D_{\rm tot}
   &=2\sum_x|E_A(x)|\\
   &=2\sum_{a\in A}2M_a
     =4\sum_{a\in A}M_a.                             \tag{3.4}
\end{aligned}
\]

Now

\[
 B\Xi=\sum_Kb_KD_K
       \le2^{|A|}\sum_KD_K
       =2^{|A|}D_{\rm tot},                           \tag{3.5}
\]

which proves (0.6).  Notice the distinction from a same-pair serial bank:
the positions in `A` produce different matchings and Boolean root merging.
For fixed `|A|`, however, that merging remains bounded and does not threaten
the little-`o(sqrt(s))` sparse threshold.

## 4. Exact Catalan packing ceiling

Put

\[
                         w_{s,a}={C_aC_{s-a-2}\over C_s}.           \tag{4.1}
\]

For fixed `a`, the Catalan ratio gives (0.3).  The weights are symmetric,

\[
                         w_{s,a}=w_{s,s-a-2},          \tag{4.2}
\]

and decrease strictly from either endpoint toward the centre.  Indeed, if
`b=s-a-2`, then

\[
 {w_{s,a+1}\over w_{s,a}}
 ={(2a+1)(b+1)\over(a+2)(2b-1)}<1
 \quad\Longleftrightarrow\quad b>a+1.                \tag{4.3}
\]

Near the left endpoint, the limiting weights are

\[
                         v_a={C_a\over4^{a+2}}.        \tag{4.4}
\]

They decrease in `a`.  In each pair `{2j,2j+1}`, an independent position
set chooses at most one index, and its weight is at most `v_(2j)`.  Hence
the maximum limiting contribution from one endpoint is

\[
\begin{aligned}
 \sum_{j\ge0}v_{2j}
 &= {1\over16}\sum_{j\ge0}{C_{2j}\over16^j}\\
 &= {1\over32}\left(C(1/4)+C(-1/4)\right)
  ={\sqrt2\over16}.                                  \tag{4.5}
\end{aligned}

The complete Catalan convolution is

\[
                         \sum_{a=0}^{s-2}C_aC_{s-a-2}=C_{s-1}.    \tag{4.6}
\]

After division by `C_s`, its mass tends to `1/4`; the fixed left and right
endpoint tails tend jointly to this whole mass as their widths tend to
infinity.  Thus the central remainder is negligible.  Applying (4.5) at
both endpoints proves the upper bound (0.7).  Conversely, choose even
offsets inward from both endpoints and change parity across one unused
central gap if necessary.  This attains both endpoint sums, proving equality
in (0.7).

For fixed `u`, the largest weights are taken alternately from the two
endpoints, subject to the one-position gap.  For `u=4,5,6,7` their limiting
sums are

\[
\begin{aligned}
 u=4:&\quad2(v_0+v_2)={9\over64},\\
 u=5:&\quad2(v_0+v_2)+v_4={295\over2048},\\
 u=6:&\quad2(v_0+v_2+v_4)={151\over1024},\\
 u=7:&\quad2(v_0+v_2+v_4)+v_6={2449\over16384},      \tag{4.7}
\end{aligned}
\]

where

\[
 v_0={1\over16},\quad v_2={1\over128},\quad
 v_4={7\over2048},\quad v_6={33\over16384}.
\]

This proves (0.10).

## 5. Boundary and full-carrier signs

At `a=0`, the rectangle is at the first two canonical cuts.  Choosing all
its components has the exact rooted first-insertion and first-deletion
transfer

\[
                         \Delta I=\Delta D
                         =C_{s-2}(e_3-e_2).           \tag{5.1}
\]

If `a>0`, the root has a nonempty complete Dyck prefix `P`.  The canonical
first return, and hence the first insertion/deletion segment, lies inside
`P`; the contextual rectangle begins only after that segment.  Therefore

\[
                         \boxed{\Delta I_a=\Delta D_a=0
                                  \quad(a>0)}          \tag{5.2}
\]

for the rooted first boundary.  Dually, only the terminal contextual layer
can affect the opposite last boundary.  Thus internal contextual conjugates
cannot provide four to seven copies of (5.1).

For the complete cyclic rank-`s-1` profile, every contextual rectangle has
the elementary-square form

\[
 e_{K\cup\{x,u\}}-e_{K\cup\{y,u\}}
 -e_{K\cup\{x,v\}}+e_{K\cup\{y,v\}},                \tag{5.3}
\]

where `{x,y}={2a+2,2a+3}` and the other seam pair and core are recovered
from the complete prefix/suffix context.  Its positive and negative masses
are both two.  Different values of `a` use different coordinate pairs and
different physical cores.  Equation (5.3) supplies no common cap sign after
backgrounds, collars, or target collisions are included.

Sequentially exposing the layers gives a background-independent upper
bound: one rectangle can lower a cap hinge by at most its negative mass
two.  Hence

\[
                         G\le2\sum_{a\in A}M_a.       \tag{5.4}
\]

Equations (0.7)--(0.9) follow.  If a specified physical carrier can use
only one of the two negative corners, replace the factor two in (5.4) by
one; then the maximum possible normalized supply is `sqrt(2)/8<1/4`.

## 6. Exact boundary and redirect

The disjoint-position construction is a genuine exact positive theorem:
all layers commute, all `X/Y` ledgers remain literal, full components have
bounded size for fixed layer count, and `Xi=O(1)`.

It does **not** realize the proposed repeated-leaf supply.  Its exact
defects are:

1. only two endpoint positions have `C_(s-2)` rectangles; interior counts
   are `C_aC_(s-a-2)`;
2. different layers never repeat one root pair and instead merge into
   Boolean root cubes;
3. only the first layer has the signed rooted first-boundary direction
   (5.1);
4. even perfect two-corner cap use has the hard-sector ceiling (0.9).

The next constructive statement must therefore abandon at least one of
the restrictions in this report: use overlapping/state-adaptive positions,
obtain more than two useful physical units from a larger coordinated atom,
or prove a different full-carrier hinge which does not pay the parent
plateau independently through these contextual squares.  Merely taking
four to seven disjoint adjacent-block conjugates is not sufficient.

The Catalan convolution (4.6) makes the first alternative exact: using
**all** contextual positions has raw edge count

\[
                         C_{s-1}=\left({1\over4}+o(1)\right)C_s,
\]

whereas disjoint positions retain only `sqrt(2)/8`.  Recovering the missing
mass necessarily uses adjacent, overlapping blocks such as the three-
singleton word `101010`; those layer switches are not covered by the
commuting theorem and must be recomputed state-adaptively.
