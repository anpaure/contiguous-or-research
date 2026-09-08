# A bounded exact pair-frame associator which changes shallow fixed-pair type

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let two coordinate matchings differ by the four-coordinate recoupling

\[
 P_0:\quad ab\mid cd,
 \qquad
 P_1:\quad ac\mid bd,
\tag{0.1}
\]

and agree on two reservoir pairs

\[
                         uv\mid wx.
\tag{0.2}
\]

There is a bounded exact middle-support trade between their occupancy-cube
cycle factors.  Each side consists of six isometric (4)-cycles and covers
the same 24 middle sets.  The bipartite ownership overlap is connected, so
the trade is one minimal overlap component for these two factors.

Relative to the original frame (P_0), its depth-one shadow effect is

\[
\boxed{
 \begin{array}{c|cc}
 &\text{before}&\text{after}\\ \hline
 \text{lower }(m-1)\text{ type}&16\,f_0+8\,f_1&24\,f_0\\
 \text{upper }(m+1)\text{ type}&16\,f_1+8\,f_2&24\,f_1.
 \end{array}}
\tag{0.3}
\]

If an outside spectator core contains (F) full (P_0)-pairs, every
index in (0.3) is translated by (F).  Thus the operative moves are

\[
 8\text{ lower occurrences }f=F+1\longrightarrow F,
 \qquad
 8\text{ upper occurrences }f=F+2\longrightarrow F+1.
\tag{0.4}
\]

Thus the packet changes the fixed-pair type in the useful direction while
preserving exact middle ownership integrally.  It disproves any statewise
invariant asserting that local coordinate recouplings cannot move pair
type.  What remains global is packing/suspending many such frames while
retaining long blocks and coherent deeper-shadow action.

## 1. The 24-set frame

Let

\[
 \mathcal Y={\{u,w\},\{u,x\},\{v,w\},\{v,x\}\}
\]

be the four orientations of the two reservoir pairs.  Put

\[
                         \mathcal X=\binom{\{a,b,c,d\}}2.
\]

The frame support is

\[
 \boxed{
 \mathcal V=\{X\cup Y:X\in\mathcal X,\ Y\in\mathcal Y\}.}
\tag{1.1}
\]

It has (6\cdot4=24) sets, all of size four.  An arbitrary fixed outside
core and arbitrary frozen full/empty pairs may be adjoined, so the packet
embeds in every sufficiently large middle layer.

For a pair matching (P), let (Q(P_1,P_2)) denote the isometric square
obtained by choosing one element from each of the two displayed pairs and
flipping them in cyclic order.  Explicitly, for (P_0),

\[
 Q_0=(ac,bc,bd,ad),
\tag{1.2}
\]

and for (P_1),

\[
 Q_1=(ab,bc,cd,ad).
\tag{1.3}
\]

The reservoir square is

\[
                         Q_R=(uw,vw,vx,ux).
\tag{1.4}
\]

All displayed cycles are physical isometric (Q_2) cycles: consecutive
sets exchange the chosen endpoint of exactly one coordinate pair.

## 2. The two exact cycle factors

Define the (P_0)-factor

\[
\boxed{
 \mathcal F_0=
 \{Q_0\cup Y:Y\in\mathcal Y\}
 \ \dot\cup\ \{ab\cup Q_R, cd\cup Q_R\}.}
\tag{2.1}
\]

Here (Q_0\cup Y) means adjoin the fixed reservoir orientation (Y) to
every vertex of (Q_0), and (ab\cup Q_R) has the analogous meaning.
The four first cycles cover precisely the local configurations

\[
                         ac,bc,bd,ad,
\]

for every reservoir orientation; the last two cover the remaining local
configurations \(ab,cd\).  Hence \(\mathcal F_0\) partitions
\(\mathcal V\).

Similarly define

\[
\boxed{
 \mathcal F_1=
 \{Q_1\cup Y:Y\in\mathcal Y\}
 \ \dot\cup\ \{ac\cup Q_R, bd\cup Q_R\}.}
\tag{2.2}
\]

The four first cycles cover (ab,bc,cd,ad), and the two reservoir cycles
cover \(ac,bd\).  Thus \(\mathcal F_1\) also partitions \(\mathcal V\).

### Theorem 2.1 (exact associator)

Replacing the six cycles of \(\mathcal F_0\) by the six cycles of
\(\mathcal F_1\) is an exact integral middle-support trade.

#### Proof

Equations (2.1)--(2.2) are two partitions of the identical support
\(\mathcal V\).  Each member is a physical isometric cycle.  Therefore the
replacement preserves every middle vertex exactly once. \(\square\)

## 3. The ownership overlap is one component

Write (L_Y) for the (P_0) local square at reservoir orientation (Y),
and write (L_{ab},L_{cd}) for the two (P_0) reservoir squares.  Use
(R_Y,R_{ac},R_{bd}) for the corresponding (P_1) cycles.

The ownership overlap has the following edges, one for each middle set:

\[
\begin{array}{c|c|c}
\text{local configuration}&P_0\text{ owner}&P_1\text{ owner}\\ \hline
ad,bc&L_Y&R_Y\\
ac&L_Y&R_{ac}\\
bd&L_Y&R_{bd}\\
ab&L_{ab}&R_Y\\
cd&L_{cd}&R_Y.
\end{array}
\tag{3.1}
\]

The first row gives two parallel edges (L_YR_Y) for each (Y).
Moreover, (R_{ac}) and (R_{bd}) are each adjacent to every (L_Y),
while (L_{ab}) and (L_{cd}) are each adjacent to every (R_Y).

### Proposition 3.1

The overlap graph of \((\mathcal F_0,\mathcal F_1)\) is connected.

#### Proof

Every two vertices (L_Y,L_{Y'}) are joined through (R_{ac}).  Every
(R_Y) is adjacent to (L_Y), and (L_{ab},L_{cd}) are adjacent to all
(R_Y).  Hence every left and right cycle lies in one component.
\(\square\)

Consequently the six-for-six exchange is not an artificial union of
smaller ownership trades: it is precisely the component switch supplied
by the overlap lemma.

## 4. Exact depth-one type action

Measure full-pair type with respect to the original matching

\[
                         P_0=ab\mid cd\mid uv\mid wx.
\]

For an edge of an isometric cycle, its lower decoration is the
intersection of its two middle endpoints, and its upper decoration is
their union.

### 4.1 The lower shadows

In a cycle (Q_0\cup Y), one special (P_0)-pair is emptied by an edge,
the other remains split, and both reservoir pairs remain split.  Thus all
four lower shadows have type (f=0).  There are four such cycles, giving
16 occurrences of type zero.

In (ab\cup Q_R) or (cd\cup Q_R), one special pair remains full, the
other special pair is empty, one reservoir pair is emptied, and the other
is split.  All four lower shadows have type (f=1).  The two cycles give
8 such occurrences.  Therefore

\[
                         \mathcal F_0^-:16f_0+8f_1.
\tag{4.1}
\]

For (Q_1\cup Y), a lower edge contains only one of the four special
coordinates, so it contains no full (P_0)-pair.  For (ac\cup Q_R) and
(bd\cup Q_R), the fixed local two-set splits both (P_0)-pairs, while
one reservoir pair is emptied.  Again there is no full pair.  Hence

\[
                         \mathcal F_1^-:24f_0.
\tag{4.2}
\]

### 4.2 The upper shadows

An edge of (Q_0\cup Y) fills one special (P_0)-pair and leaves the
other special pair and both reservoir pairs split, so it has type (f=1).
The four cycles give 16 such occurrences.

An edge of (ab\cup Q_R) or (cd\cup Q_R) retains one full special pair
and fills one reservoir pair, so it has type (f=2).  Thus

\[
                         \mathcal F_0^+:16f_1+8f_2.
\tag{4.3}
\]

An edge of (Q_1\cup Y) contains three special coordinates, hence exactly
one full (P_0)-pair.  An edge of (ac\cup Q_R) or (bd\cup Q_R) splits
both special (P_0)-pairs but fills one reservoir pair.  Both cases have
type (f=1), and therefore

\[
                         \mathcal F_1^+:24f_1.
\tag{4.4}
\]

Equations (4.1)--(4.4) prove (0.3).

Adjoining a spectator core with (F) full (P_0)-pairs adds (F) to
every type and proves (0.4).

## 5. Minimality in the two-reservoir (Q_2) frame

The six local two-subsets split under (P_0) into one four-vertex
orientation square plus two singleton full/empty strata; under (P_1)
the same is true with a different square and different singletons.  A
singleton local stratum cannot support a nontrivial pair-flip cycle without
reservoir directions.  An isometric four-cycle requires two independent
directions, so two unchanged reservoir pairs are necessary in this
literal (Q_2)-cycle model.

Once the two reservoir pairs are supplied, every one of the 24 middle
vertices must occur in the exact support exchange.  A four-cycle contains
four vertices, so each side needs at least six cycles.  The constructions
(2.1)--(2.2) attain this bound.  Thus the packet is smallest within the
natural two-reservoir, isometric-(Q_2), full-frame model.

This does not claim absolute minimality among arbitrary nonisometric walks,
repeated-vertex blocks, or packets using additional coordinate systems.

## 6. A bounded suspension to physical \(C_{2h}\)'s

The four-cycle packet is not confined to depth one.  It has a
phase-compatible colouring which suspends it to a six-for-six trade of
isometric \(C_{2h}\)'s for every \(h\ge2\), without increasing the number
of rows.

Put the reservoir orientations in the cyclic order

\[
 y_0=uw,\qquad y_1=vw,\qquad y_2=vx,\qquad y_3=ux.
\tag{6.1}
\]

Give every physical square an oriented vertex enumeration and a colour in
\(\mathbb Z_4\) as follows.

* On the left big square \(L_k=Q_0\cup y_k\), a vertex in position \(i\)
  of \(Q_0=(ac,bc,bd,ad)\) has colour \(i+k\).
* On the right big square \(R_k=Q_1\cup y_k\), a vertex in position \(i\)
  of \(Q_1=(ab,bc,cd,ad)\) has colour \(i+k\).
* On \(L_{ab}\) and \(R_{ac}\), the vertex over \(y_k\) has colour \(k\).
* On \(L_{cd}\) and \(R_{bd}\), the vertex over \(y_k\) has colour
  \(k+2\).

All colours are modulo four.  The last four rules merely rotate the
oriented reservoir square, so every coloured object is still the same
physical isometric square.

### Lemma 6.1 (phase compatibility)

Every middle vertex has the same colour in its left and right owner.

#### Proof

For the six possible local two-sets the colours on the two sides are

\[
\begin{array}{c|cccccc}
X&ac&bc&bd&ad&ab&cd\\ \hline
\text{left colour}&k&k+1&k+2&k+3&k&k+2\\
\text{right colour}&k&k+1&k+2&k+3&k&k+2.
\end{array}
\tag{6.2}
\]

Here \(k\) is determined by the reservoir orientation \(y_k\).  Thus the
two entries agree in every case. \(\square\)

Now adjoin \(h-2\) new coordinate pairs

\[
                         C_1,\ldots,C_{h-2}.
\tag{6.3}
\]

For an oriented coloured square
 \(Z=(z_0,z_1,z_2,z_3)\), choose a base orientation \(0\) of the new
pairs and let \(e_1,\ldots,e_{h-2}\) be their flip directions.  Replace
\(Z\) by the cycle with direction word

\[
 \alpha,\beta,e_1,\ldots,e_{h-2},
 \alpha,\beta,e_1,\ldots,e_{h-2},
\tag{6.4}
\]

where \(\alpha,\beta\) are the two alternating directions of \(Z\).
Equivalently, the first half runs

\[
 z_0@0, z_1@0, z_2@0,
 z_2@e_1,\ldots,z_2@\mathbf1,
\tag{6.5}
\]

and the second half runs

\[
 z_3@\mathbf1, z_0@\mathbf1,
 z_0@(\mathbf1+e_1),\ldots,z_0@0.
\tag{6.6}
\]

The notation \(z@\eta\) means the local four-set \(z\), together with
the orientation \(\eta\in\mathbb F_2^{h-2}\) of the new pairs.  The final
entry in (6.6) is the initial vertex and is not counted twice.

### Theorem 6.2 (bounded long-cycle associator)

For every \(h\ge2\), the six coloured squares on each side of the local
associator lift by (6.4) to six pairwise vertex-disjoint isometric
\(C_{2h}\)'s.  The two six-cycle families cover exactly the same
\(12h\) middle sets, and their ownership overlap is connected.

#### Proof

Every direction in (6.4) occurs once in each half.  No direction repeats
on an arc of at most \(h\) edges, so the resulting cycle is isometric and
has length \(2h\).

The six base squares on either side are vertex-disjoint.  Their lifts are
therefore vertex-disjoint as well.  The set of new-pair orientations used
above a local vertex depends only on its colour: colour \(1\) occurs at
the state \(0\), colour \(3\) at \(\mathbf1\), colour \(2\) along the
forward prefix chain, and colour \(0\) along the complementary return
chain (including the endpoints).  By Lemma 6.1 every local vertex has the
same colour in its two owners.  Hence it is lifted through precisely the
same new-pair orientations on the two sides.  The two unions of lifted
vertices are identical.  Each side has six cycles of length \(2h\), so
the common support has size \(12h\).

Finally, every local vertex of the original 24-set frame occurs at least
once in its lifted colour fibre.  Thus every edge of the connected base
ownership overlap from Proposition 3.1 survives in the lifted overlap.
The latter is therefore connected. \(\square\)

This proves that the pair-frame move is already a bounded exact
all-length associator.  What it does not by itself prove is a global
packing theorem or simultaneous control of all shadows of the suspended
cycles.

## 7. Consequences and remaining lift

The pair-frame associator proves a local fact which the one-native-matching
capacity obstruction cannot see:

\[
 \boxed{
 \text{a bounded exact component switch can change fixed-pair type.}}
\]

It is therefore a genuine candidate absorber for the conjugate-pairing
catalog.  Its limitations are equally precise.

1. The bounded packet suspends to every physical length \(2h\), but its
   full multidepth shadow action still has to be allocated globally.
2. A coefficient-one construction needs a vertex-disjoint packing of many
   frames inside a long-block factor.
3. The suspension preserves the connected ownership exchange exactly;
   the remaining issue is controlling every depth \(q<h\) after packing.
4. The packet changes lower and upper type in matched directions, but a
   global allocation must choose where each direction is needed.

The next theorem is consequently a suspension/packing statement, not a
search for the local associator: the bounded local associator already
exists explicitly.
