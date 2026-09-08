# Exact consecutive-window designs inside the canonical tensor packet

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 \mathcal V=
 \{X\cup Y:
 X\in\tbinom{\{a,b,c,d\}}2,\ 
 Y\in\{uw,ux,vw,vx\}\}
\tag{0.1}
\]

be the canonical 24-owner local packet, and let

\[
                         \mathcal V^r
\tag{0.2}
\]

be its tensor product on \(r\) disjoint eight-coordinate blocks.

Choose \(a\) blocks in one of the canonical six-\(Q_2\) resolutions and
\(b\) blocks in one of the canonical three-\(Q_3\) resolutions. Leave the
other \(r-a-b\) local owners passive. Put

\[
                         s=2a+3b.                       \tag{0.3}
\]

If \(s\) is a power of two, then \(\mathcal V^r\) has an explicit cycle
factor such that, simultaneously for every

\[
                         1\le q\le s/2,                 \tag{0.4}
\]

the maps taking a middle owner to the intersection or union of its
\(q+1\) consecutive cycle states are injective on all of
\(\mathcal V^r\). Consequently, at every such depth,

\[
\boxed{
 \#\{\text{distinct lower literal targets}\}
 =\#\{\text{distinct upper literal targets}\}
 =24^r.}                                                \tag{0.5}
\]

The same single cycle factor works at every depth in (0.4); no
depth-by-depth choice of orders is made.

In particular, let

\[
                         Q=\sqrt m\,\omega(m)=o(m).
\tag{0.6}
\]

If the canonical packet has \(r\ge2Q\) blocks, choose a power of two
\(r_0\) with

\[
                         Q\le r_0<2Q,\qquad r_0\le r,
\tag{0.7}
\]

use \(a=r_0,b=0\), and leave the other blocks passive. Then
\(s=2r_0\) is a power of two and (0.5) holds simultaneously for every
\(q\le Q\). Thus the canonical tensor packet has an exact algebraic
owner-normalized consecutive-window design through the requested
Gaussian-growing depth.

There is a necessary normalization distinction. In one \(Q_s\), the
number of all possible literal \(q\)-face deletion patterns is

\[
                         \binom sq2^{s-q},               \tag{0.8}
\]

whereas any 2-factor supplies exactly \(2^s\) directed starts. Therefore
the fraction of all possible face patterns realized by any 2-factor is at
most

\[
\boxed{
                         {2^q\over\binom sq}.}           \tag{0.9}
\]

For \(q=o(s)\),

\[
                         {2^q\over\binom sq}
 \le\left({2q\over s}\right)^q.                         \tag{0.10}
\]

Hence no cycle factor can realize almost all possible cube faces. What the
constant-one owner problem can ask for, and what (0.5) gives exactly, is
one distinct literal target for every certified owner.

The remaining obstruction is not internal to \(\mathcal V^r\). It is the
outer owner-disjoint selection of overlapping tensor packets and coordinate
frames. The theorem below does not solve that global packing equation.

## 1. Literal face traces

An isometric constant-weight cube is specified by a fixed core and
disjoint active coordinate pairs

\[
                         E_1,\ldots,E_s.                \tag{1.1}
\]

A cube vertex chooses one endpoint from each \(E_i\). Let
\(x_0,x_1,\ldots,x_q\) be a geodesic segment whose \(q\) directions are
the distinct set \(D\subseteq[s]\).

For \(i\notin D\), the chosen endpoint of \(E_i\) is constant along the
segment. For \(i\in D\), both endpoints occur. Therefore

\[
 \bigcap_{j=0}^qx_j
 =\text{fixed core}\ \cup\
   \{\text{chosen endpoint of }E_i:i\notin D\},          \tag{1.2}
\]

and

\[
 \bigcup_{j=0}^qx_j
 =\text{fixed core}\ \cup\
   \{\text{chosen endpoint of }E_i:i\notin D\}
   \cup\bigcup_{i\in D}E_i.                             \tag{1.3}
\]

Thus, inside a known cube cell, either physical trace is equivalent to

\[
                         (D,x|_{[s]\setminus D}).        \tag{1.4}
\]

The lower trace makes every touched pair empty; the upper trace makes it
full.

For a neighbor permutation \(F\) on \(Q_s\), write

\[
 D_q(x)=\{\operatorname{dir}(x,Fx),\ldots,
          \operatorname{dir}(F^{q-1}x,F^qx)\},          \tag{1.5}
\]

and define the encoded shadow

\[
                         \Sigma_q(x)
 =(D_q(x),x|_{[s]\setminus D_q(x)}).                    \tag{1.6}
\]

By (1.2)--(1.4), injectivity of \(\Sigma_q\) is exactly injectivity of
both physical lower and upper traces inside the cell.

## 2. The recursive nonlinear factor

For powers of two \(s\), define a neighbor permutation \(F_s\) recursively.
Let \(F_1\) toggle the sole coordinate. If \(s=2h\), write
\(x=(u,v)\in Q_h^L\times Q_h^R\), and put

\[
 F_{2h}(u,v)=
 \begin{cases}
  (F_hu,v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_hv),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                            \tag{2.1}
\]

Every move toggles one bit, so it reverses total parity. Hence

\[
\boxed{
 F_{2h}^{\,2t}(u,v)=(F_h^tu,F_h^tv)}                    \tag{2.2}
\]

for every \(t\). The order of the two moves in each pair depends on the
initial parity, but their product does not.

### Lemma 2.1 (cycle structure)

For \(s\ge2\), every cycle of \(F_s\) has length \(2s\), is isometric, and
has direction word

\[
                         \pi\pi                         \tag{2.3}
\]

for a permutation \(\pi\) of the \(s\) directions.

#### Proof

Induct on \(s\). By (2.2), an \(F_{2h}\)-orbit returns after \(4h\)
steps. It cannot return at an odd time because exactly one half has just
moved, and it cannot return at a smaller even time because one of the
two \(F_h\)-orbits would return before its length \(2h\).

During the first \(2h\) moves, the recursion makes \(h\) moves in each
half. By induction, those are all \(h\) directions of that half exactly
once. During the next \(2h\) moves the same direction sequence repeats,
because every parent direction word has period \(h\). Thus the child word
is \(\pi\pi\).

Every cyclic block of at most \(2h\) directions in \(\pi\pi\) has no
repetition. The cube distance between the endpoints of such a path equals
its length, proving isometry. \(\square\)

Thus \(F_s\) is an explicit 2-factor of \(Q_s\) into isometric
\(2s\)-cycles.

### Theorem 2.2 (simultaneous shadow injectivity)

For every power of two \(s\), both the forward and reverse encoded shadow
maps are injective on \(Q_s\) for every

\[
                         q\le s/2.                      \tag{2.4}
\]

#### Proof

Induct on \(s=2h\). The case \(s=2,q=1\) is the four-cycle.

First let \(q=2t\le h\). A \(2t\)-window contains exactly \(t\) moves in
each half. By (2.2), its encoded trace splits as

\[
                         \Sigma_t(u)\times\Sigma_t(v).  \tag{2.5}
\]

Since \(t\le h/2\), the induction hypothesis recovers \(u\) and \(v\).

Now let \(q=2t+1\le h\). One half contributes \(t+1\) directions and the
other contributes \(t\). The cardinalities of the two direction
projections reveal which half moved first. Since \(h\) is even whenever
\(h>1\),

\[
                         t+1\le h/2.                    \tag{2.6}
\]

The trace therefore splits into one depth-\((t+1)\) parent trace and one
depth-\(t\) parent trace, both injective by induction. This again recovers
\((u,v)\).

Reversing every orbit leaves the same two-step recursion, with the order
inside each pair reversed. The identical argument proves reverse
injectivity. \(\square\)

Theorem 2.2 is stronger than a depthwise design: one algebraic successor
permutation works simultaneously through half the cube dimension.

## 3. The six-\(Q_2\) local resolutions are face-separated

Use the original local matching

\[
                         ab\mid cd\mid uv\mid wx.        \tag{3.1}
\]

One canonical six-\(Q_2\) partition consists of

\[
 \{Q_0\cup Y:Y\in\{uw,ux,vw,vx\}\}
 \ \dot\cup\
 \{ab\cup Q_R,\ cd\cup Q_R\},                           \tag{3.2}
\]

where \(Q_0\) flips the special pairs \(ab,cd\) and \(Q_R\) flips the
reservoir pairs \(uv,wx\).

Call the first four cells special-active and the last two
reservoir-active.

### Lemma 3.1

For every \(d\in\{0,1,2\}\), the physical lower \(d\)-face traces of
distinct cells in (3.2) are disjoint. The same is true of upper traces.

#### Proof

At \(d=0\), this is exactly the fact that (3.2) partitions
\(\mathcal V\).

Suppose \(d>0\). A lower trace from a special-active cell contains
\(2-d\) special coordinates and the fixed two-coordinate reservoir
orientation \(Y\). A lower trace from a reservoir-active cell contains
the fixed special pair \(ab\) or \(cd\) and \(2-d\) reservoir
coordinates. Thus the two cell types are distinguished by their special
and reservoir cardinalities. Within the first type, the retained
reservoir orientation identifies \(Y\); within the second, the retained
special pair identifies the cell.

For an upper trace, special-active cells have \(2+d\) special and two
reservoir coordinates, whereas reservoir-active cells have two special
and \(2+d\) reservoir coordinates. The same fixed data identify the cell.
\(\square\)

The recoupled six-\(Q_2\) resolution has the identical proof after
replacing the two special active pairs and the two fixed special pairs.

## 4. The three-\(Q_3\) local resolutions are face-separated

Consider the three cells

\[
\begin{array}{c|c|c|c}
\text{cell}&\text{fixed special point}&
 \text{active special pair}&\text{active reservoir pairs}\\ \hline
A_1&a&bc&uv,\ wx\\
A_2&d&ab&uv,\ wx\\
A_3&c&bd&uv,\ wx .
\end{array}                                             \tag{4.1}
\]

Their special two-set vertex supports are

\[
 \{ab,ac\},\qquad \{ad,bd\},\qquad \{bc,cd\},           \tag{4.2}
\]

which partition \(\binom{\{a,b,c,d\}}2\). Tensoring each special support
with all four reservoir orientations gives a partition of \(\mathcal V\)
into three \(Q_3\)'s.

### Lemma 4.1

For every local direction set, the physical lower face traces of distinct
cells in (4.1) are disjoint. The same is true of upper face traces.

#### Proof

Let \(d_S\in\{0,1\}\) indicate whether the active special direction is
touched. The special part of a lower trace has size \(2-d_S\), so the
physical target determines \(d_S\).

If \(d_S=0\), its special two-set lies in exactly one of the three
disjoint supports in (4.2), identifying the cell. If \(d_S=1\), its
special trace is the fixed singleton

\[
                         a,\quad d,\quad c,              \tag{4.3}
\]

again identifying the cell.

For upper traces, the case \(d_S=0\) is still (4.2). When \(d_S=1\), the
special trace is respectively

\[
                         abc,\quad abd,\quad bcd,        \tag{4.4}
\]

which are distinct. Reservoir directions are common to all three cells
and cannot undo this identification. \(\square\)

The second three-\(Q_3\) resolution has the same proof, with the analogous
partition of the six special two-sets and three distinct fixed
singletons/triples.

## 5. Tensor face separation

Choose \(a\) local \(Q_2\) resolutions and \(b\) local \(Q_3\)
resolutions. Each product cell is a physical \(Q_s\), where
\(s=2a+3b\). The number of product cells, including passive local owner
labels, is

\[
                         M=24^{\,r-a-b}6^a3^b.          \tag{5.1}
\]

The vertex count is

\[
 M2^s
 =24^{\,r-a-b}6^a3^b2^{2a+3b}
 =24^r.                                                \tag{5.2}
\]

Thus these product cells partition the whole tensor packet.

### Theorem 5.1 (packet-wide simultaneous literal injectivity)

If \(s\) is a power of two, apply the factor \(F_s\) of Section 2 inside
every product cell. Then, for every \(q\le s/2\), the physical lower and
upper consecutive-window maps are injective on all \(24^r\) owners.

#### Proof

Within one cell, Theorem 2.2 and (1.2)--(1.6) give physical trace
injectivity.

Suppose two physical traces from possibly different product cells are
equal. Restrict the common target to each eight-coordinate tensor block.
Lemmas 3.1 and 4.1 identify the local active cell whenever that block is
active. A passive block is unchanged and its local owner is read directly
from the target. Therefore the common target identifies the entire
product cell.

The two starts now lie in the same \(Q_s\) cell, where Theorem 2.2 says
they are equal. This proves global injectivity. The upper proof is
identical. \(\square\)

Because the same \(F_s\) is used at every depth, Theorem 5.1 proves (0.5)
simultaneously, not merely after choosing a separate factor for each
\(q\).

## 6. Quantitative Gaussian-depth choice

Let \(Q=\sqrt m\,\omega(m)=o(m)\), and suppose the canonical tensor packet
contains at least \(2Q\) disjoint local blocks. Choose the least power of
two \(r_0\ge Q\). Then

\[
                         Q\le r_0<2Q.                  \tag{6.1}
\]

Activate \(r_0\) blocks using their six-\(Q_2\) resolution and leave all
other local owners passive. The active cube dimension is

\[
                         s=2r_0,                        \tag{6.2}
\]

which is a power of two, and

\[
                         Q\le s/2.                      \tag{6.3}
\]

Theorem 5.1 therefore gives, uniformly for \(1\le q\le Q\),

\[
 \kappa_q^-=\kappa_q^+=0                               \tag{6.4}
\]

inside the packet, where \(\kappa_q^\pm\) denotes owner collision excess.
In particular,

\[
 \sum_{q\le Q}(\kappa_q^-+\kappa_q^+)=0.                \tag{6.5}
\]

If one uses a radius-thinned subset of owners, restricting an injective map
remains injective. Hence no new local collision term appears after imposing
a Catalan/SCD radius census.

The active consecutive-window gadget uses \(8r_0=O(Q)=o(m)\) ground
coordinates. The complete tensor packet uses \(8r\) coordinates, including
its passive labels, and embeds in the middle layer whenever \(r\le m/4\);
an outside core of size \(m-4r\) then restores the global middle rank.

## 7. Sharp obstruction under the all-face interpretation

Fix one product \(Q_s\) cell. A literal lower \(q\)-face is determined by

1. its \(q\)-set of touched directions, and
2. one orientation on every untouched direction.

Thus there are exactly

\[
                         \binom sq2^{s-q}               \tag{7.1}
\]

possible lower deletion patterns, and the same number of upper patterns.
A spanning 2-factor has one forward \(q\)-window at each of its \(2^s\)
vertices. It can therefore realize at most \(2^s\) such patterns. This
proves (0.9).

For the face-separated tensor partition, patterns belonging to different
product cells are physically distinct by Lemmas 3.1 and 4.1. Hence the
ratio (0.9) is not merely an upper bound caused by possible cross-cell
collisions. The factor of Theorem 5.1 attains its numerator exactly:

\[
 \frac{\#\{\text{realized physical patterns}\}}
      {\#\{\text{all physically admissible cell patterns}\}}
 =\frac{M2^s}{M\binom sq2^{s-q}}
 =\frac{2^q}{\binom sq}.                               \tag{7.2}
\]

Using \(\binom sq\ge(s/q)^q\) proves (0.10).

Therefore:

* if “almost all deletion patterns” means all admissible cube faces, the
  answer is no, with the exact obstruction (7.2);
* if it means one distinct literal deletion target for almost every
  certified middle owner, the answer is yes, and Theorem 5.1 gives every
  owner with zero defect.

The second normalization is the one compatible with coefficient one.

## 8. What remains global

The tensor-packet problem itself is solved by Theorem 5.1. Three interfaces
remain outside its scope.

1. Different embedded packets and different coordinate frames can share
   middle owners. Selecting an owner-disjoint packet atlas is an integral
   packing problem.
2. Physical lower targets from different packets can collide after packet
   tags are forgotten. Local face separation controls cells inside one
   packet, not cross-packet incidence.
3. A cube-cycle factor is an even-lattice consecutive-face object. A
   literal odd contiguous-OR or wreath compiler additionally needs the
   audited crossing-collar interface.

Thus there is no algebraic consecutive-window obstruction internal to
\(\mathcal V^r\) at \(q\le\sqrt m\,\omega\). The exact remaining
constant-one gate is the mixed-frame, owner-disjoint outer atlas, not
sectorwise quotas and not the local \(Q_2/Q_3\) direction orders.
