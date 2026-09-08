# The certified `m=4` Haar circuit is not a direct Dyck-context functor

Date: 2026-07-26

Method: pure mathematics.  All finite tables below are obtained directly
from the fourteen cyclic orders displayed in `NONLOCAL_HAAR_M4.md`.

## 0. Outcome

The completed negative and positive factors of the certified four-for-four
Haar trade cannot be substituted, as they stand, into an arbitrary Dyck
hole with the outer boundary paths frozen.  This remains false after

* choosing any one of the nine coordinates as the parent coordinate;
* reversing the individual wreaths; and
* applying an arbitrary common relabelling of the other eight coordinates.

The obstruction is at the **ports**, before any lower-shadow calculation.
For six choices of the parent coordinate the two Haar sides have different
port multisets.  For the remaining three choices their common port family
is not a relabelled Catalan port family.

There is nevertheless a sharp positive remnant.  For parent coordinate
`6`, the common port family differs from a Catalan port family in exactly
two complementary pairs.  On the rooted Johnson graph the correction has
the three-step vacancy route

\[
             235\longrightarrow135,\qquad
             245\longrightarrow235,\qquad
             239\longrightarrow349.                 \tag{0.1}
\]

Every arrow in (0.1) has the same endpoint signature as the elementary
port slide in the certified four-row complete-wreath associator.  The new
rooted pentagon audit shows, however, that this does **not** give a recursive
repair: the four-row associator contains two Dyck states in one path and
cannot lie in a port-transversal factor, whereas the recursively legal
pentagon fixes all ambient ports pointwise.  Thus (0.1) measures the exact
boundary defect but is not a route inside the rooted context-functor fibre.

## 1. The exact port criterion

Let `J` have size `2r` and let `z` be an additional parent coordinate.
For a wreath `C` on `J union {z}`, delete the four (in general `r`)
middle windows containing `z`.  The remaining `r+1` middle windows form a
Johnson geodesic

\[
                       R=X_0,X_1,\ldots,X_r=J\setminus R.
                                                               \tag{1.1}
\]

Its unordered complementary endpoint pair

\[
                         e_z(C)=\{R,J\setminus R\}              \tag{1.2}
\]

is the `z`-port of `C`.  If `F` is an exact local factor, put

\[
                         \mathcal E_z(F)=\{e_z(C):C\in F\}.      \tag{1.3}
\]

For a linear order `prec` on `J`, let `D_r(prec)` be the Catalan family of
Dyck `r`-subsets and put

\[
 \mathcal C_r(\prec)=
   \bigl\{\{P,J\setminus P\}:P\in D_r(\prec)\bigr\}.            \tag{1.4}
\]

### Lemma 1.1 (fixed-boundary context criterion)

An exact local factor `F` can replace the canonical MSW factor inside an
arbitrary aligned size-`r` Dyck hole, with every outside spectator and
every row boundary fixed, if and only if

\[
                         \mathcal E_z(F)=\mathcal C_r(\prec).    \tag{1.5}
\]

Two local factors give the two sides of an arbitrary-spectator context
trade only if both satisfy (1.5) for the same `z` and the same order.

#### Proof

Necessity is a boundary statement.  The canonical row indexed by
`P in D_r(prec)` enters the local slab at `P` and exits at `J minus P`.
An arbitrary outside spectator can distinguish all of these boundary
attachments.  Hence the replacing wreath assigned to `P` must have the
port `\{P,J minus P\}`.  There are `Cat_r` rows and `Cat_r` ports, so their
port family is exactly (1.4).

Conversely orient the unique wreath at every port from `P` to
`J minus P`.  The core states of all the paths partition
`binom(J,r)`, because `F` is exact.  Their adjacent unions partition
`binom(J,r+1)`: complementation in `J` and adjoining `z` identifies these
unions with the factor vertices containing `z`.  These are exactly the two
`X/Y` ownership ledgers of the slab criterion.  The endpoints agree row by
row, so adjoining an arbitrary common exterior spectator preserves both
ledgers.  This proves sufficiency. \(\square\)

This is the port-qualified form of the middle-levels path-factor normal
form.  Mere occurrence of one Dyck state somewhere in a wreath is not
enough; it must be one of the two states adjacent to `z`.

## 2. Ports of the Haar certificate

For a listed cyclic order

\[
                         q=(q_0,\ldots,q_8)
\]

with `q_k=z`, one representative of its port split is

\[
 A_z(q)=\{q_{k+2},q_{k+4},q_{k+6},q_{k+8}\},
 \qquad e_z(q)=\{A_z(q),J\setminus A_z(q)\},             \tag{2.1}
\]

with indices modulo nine.  Formula (2.1) is just the first and last core
state in (1.1).

Let `F^-` be the ten common rows plus the four negative Haar rows, and let
`F^+` be the ten common rows plus the four positive Haar rows.  Directly
from the eight displayed orders,

\[
              \mathcal E_z(F^-)=\mathcal E_z(F^+)
              \quad\Longleftrightarrow\quad z\in\{3,4,6\}.      \tag{2.2}
\]

This is also the endpoint-pair ledger independently recorded in
`CARTESIAN_CAP_FLAG_OBSTRUCTION.md`.  Therefore every
`z notin {3,4,6}` is already impossible in Lemma 1.1.  It remains to test
whether the common family at `z=3,4,6` is a relabelled Catalan family.

## 3. Two invariants of a Catalan port family

Write an order on eight coordinates as

\[
                         a_1\prec a_2\prec\cdots\prec a_8.
\]

Two elementary properties of `\mathcal C_4(\prec)` will suffice.

1. The pair `\{a_1,a_8\}` is separated by every split in the family.
   Indeed every nonempty Dyck word begins with `1` and ends with `0`.
2. Orient every split toward the side containing `a_1`, delete `a_1,a_8`,
   and regard the roots as three-subsets of the six internal coordinates.
   The six excluded triples are, writing the internal order as
   `b_1,...,b_6`,

   \[
   b_1b_5b_6, b_2b_5b_6,
   b_3b_4b_5, b_3b_4b_6, b_3b_5b_6, b_4b_5b_6.       \tag{3.1}
   \]

   In particular the excluded triples contain the complete three-graph
   on `\{b_3,b_4,b_5,b_6\}`.  The same assertion holds after orienting
   toward `a_8`, by complementation.

Both properties are invariant under relabelling.

## 4. Coordinates `3` and `4`: no universal separated pair

For `z=3`, the following seven port splits already have no coordinate pair
which is separated by all of them:

\[
\begin{array}{c|c}
2578&1469\\
2469&1578\\
4578&1269\\
4678&1259\\
1567&2489\\
2678&1459\\
1456&2789
\end{array}                                               \tag{4.1}
\]

For completeness, intersecting their separated-pair sets leaves, after
the first two rows,

\[
 \{12\}\cup(\{4,6,9\}\times\{5,7,8\});
\]

after the third row it leaves
`\{6,9\} x \{5,7,8\}`; after the fourth it leaves
`\{65,97,98\}`; after the fifth it leaves only `97`; and the seventh
deletes `97`.

For `z=4`, six rows suffice:

\[
\begin{array}{c|c}
2378&1569\\
1278&3569\\
2569&1378\\
6789&1235\\
1389&2567\\
1358&2679
\end{array}.                                               \tag{4.2}
\]

The survivor sets are successively

\[
 \{13\}\cup(\{2,7,8\}\times\{5,6,9\}),\quad
 \{7,8\}\times\{5,6,9\},\quad
 \{75,85\},\quad\{85\},\quad\varnothing.               \tag{4.3}
\]

Thus property 1 of Section 3 fails for `z=3` and `z=4`.

## 5. Coordinate `6`: a non-Catalan near miss

For `z=6`, the unique pair separated by all fourteen port splits is

\[
                              \{7,8\}.                    \tag{5.1}
\]

Orient every split toward `8` and remove the fixed coordinates `8,7`.
On the internal universe

\[
                              U=\{1,2,3,4,5,9\},
\]

the fourteen rooted triples are

\[
\begin{aligned}
\mathcal R=\{&123,124,125,134,139,145,149,159,\\
             &234,235,239,245,345,359\}.                 \tag{5.2}
\end{aligned}
\]

Hence the six excluded triples are

\[
                       \mathcal H=\{129,135,249,259,349,459\}. \tag{5.3}
\]

The hypergraph (5.3) contains no complete three-graph on four vertices.
The complementary orientation has excluded family

\[
                       \{123,125,134,135,249,345\},       \tag{5.4}
\]

which also contains no such four-vertex clique.  Property 2 of Section 3
therefore fails in both orientations.  Thus
`\mathcal E_6(F^\pm)` is not a
Catalan port family under any coordinate order.

### Theorem 5.1 (direct Haar-context obstruction)

The completed `m=4` Haar factors in `NONLOCAL_HAAR_M4.md` cannot be the two
local factors in a fixed-boundary arbitrary-spectator Dyck-context trade,
for any choice of parent coordinate, orientations, or common coordinate
relabeling.

#### Proof

For `z notin {3,4,6}`, equation (2.2) violates the common-boundary
necessity in Lemma 1.1.  For `z=3,4`, Section 4 violates the first Catalan
invariant.  For `z=6`, Section 5 violates the second. \(\square\)

This is not the previously known constant-gap insertion obstruction.  It
allows an arbitrary outer Dyck spectator and examines only the exact
middle-levels `X/Y` interface.  The failure occurs before the spectator is
adjoined.

## 6. Exact distance from a Catalan port family

The `z=6` obstruction is only two port pairs wide.  Take the internal order

\[
                         (1,3,4,5,2,9),
\]

so the full order is

\[
                         (8,1,3,4,5,2,9,7).               \tag{6.1}
\]

By (3.1), its excluded triple family is

\[
                 \mathcal H_{\rm Cat}
                   =\{129,239,245,249,259,459\}.          \tag{6.2}
\]

Comparing (5.3) and (6.2),

\[
 \mathcal H\setminus\mathcal H_{\rm Cat}=\{135,349\},
 \qquad
 \mathcal H_{\rm Cat}\setminus\mathcal H=\{239,245\}.  \tag{6.3}
\]

Equivalently the current factor has the two extra rooted ports

\[
                  2389\mid1457,qquad2458\mid1379,        \tag{6.4}
\]

and lacks the required ports

\[
                  1358\mid2479,qquad3489\mid1257.        \tag{6.5}
\]

The transformation of root sets admits the collision-free token-slide
schedule

\[
       2358\to1358,qquad2458\to2358,qquad2389\to3489.   \tag{6.6}
\]

At every arrow the two roots differ by one coordinate.  The destination is
empty when the arrow is performed, and after all three arrows the root set
is exactly the Catalan family (6.1).

## 7. Why neither known associator repairs the ports

The four-row packet in
`MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md` changes its auxiliary
port pair by

\[
                    1256\mid3478
                      \longrightarrow
                    1258\mid3467.                       \tag{7.1}
\]

Thus, as an **unrooted complete-wreath** move, it performs one
Johnson-adjacent token slide on complementary port pairs.  Coordinate
relabeling turns (7.1) into any arrow of (6.6).

It cannot be used in a `D_4`-port-transversal factor.  Its distinguished
positive path contains both `1245` and `1256`, two distinct Dyck roots.
Since the paths of a port-transversal factor partition the middle states,
every Dyck state must occur as the endpoint of its own path; no path can
contain a second Dyck state internally.  This is Theorem 1.1 of
`MATH_THEOREM_ROOTED_PENTAGON_AND_PORT_OBSTRUCTION_20260726.md`.

The five-row rooted pentagon in that note has the opposite property: after
wrapping it in an arbitrary common context, every ambient initial and
terminal port is fixed **row by row**.  Hence any composition of rooted
pentagons preserves the complete ambient port assignment.  It cannot carry
out even the first nontrivial arrow of (6.6).

### Proposition 7.1 (rooted-packet port invariant)

Let `F_0,F_1,...,F_s` be path factors such that each step replaces a rooted
packet by another packet with the same initial and terminal state at every
row, possibly after wrapping it in a common one-hole context.  Then the
root-to-complement port assignment of `F_i` is independent of `i`.
Consequently no sequence of embedded rooted pentagons transforms the Haar
port family (5.2) into the Catalan family (6.2).

#### Proof

One rooted replacement leaves every affected endpoint pair fixed, and all
unaffected paths are unchanged.  The common-context operations in the
rooted context theorem add the same fixed material to corresponding
endpoints and therefore also preserve their labels.  Induction over the
sequence proves the first assertion.  Equations (6.3)--(6.6) change two
port pairs, so the second follows. \(\square\)

The correct finite successor target is therefore not port repair.  It is a
pair of already-`D_4`-port-transversal path factors with the same rooted
ports and with a nonzero deeper Haar effect while the preceding shadow
effect cancels.  Rooted pentagons are admissible generators for that new
target; the finished `m=4` Haar factors are not admissible starting states.

## 8. Scope

Theorem 5.1 rules out the finished eight-row Haar identity as a direct
context functor and rules out repairing it by a mere choice of rooting.  It
does **not** rule out

* a new port-preserving combination of rooted pentagons having Haar effect;
* a larger finite path-cover gadget;
* preparatory state-dependent component switches; or
* a different local factor with the Catalan port property.

The useful conclusion is therefore not that the Haar lane is dead.  It is
that the old finite certificate lies in the wrong rooted component.  Its
boundary defect is exactly the three-slide ledger (6.6), but recursively
legal moves cannot change that ledger.  A scalable Haar circuit must be
built natively inside the port-transversal fibre.

## 9. The rooted pentagon has the right nonzero primitive effect

There is a useful exact input for that native construction.  Number the
parent coordinate of the rooted pentagon by `7`.  For a rooted path

\[
                         X_0,Z_0,X_1,Z_1,X_2,Z_2,X_3,
\]

its seven rank-two cyclic windows are

\[
\begin{gathered}
 X_0\cap Z_2,\quad X_0\cap X_1,\quad X_1\cap X_2,
 \quad X_2\cap X_3,\\
 Z_0\cap X_3,\quad Z_0\cap Z_1,\quad Z_1\cap Z_2.
                                                               \tag{9.1}
\end{gathered}
\]

Reading (9.1) from the two five-row tables in the rooted-pentagon note gives

\[
 \boxed{
 B_2(\mathbf 1_{\mathcal P^+}-\mathbf 1_{\mathcal P^-})
   =e_{25}+e_{37}+e_{47}-e_{27}-e_{34}-e_{57}.}          \tag{9.2}
\]

Every singleton occurs once in every wreath, so the rank-one effect is
zero.  Thus the rooted pentagon is already a genuine lower-shadow
direction:

\[
                         B_3w=0,\qquad B_2w\ne0,\qquad B_1w=0. \tag{9.3}
\]

The coordinate involution

\[
                              \tau=(2\ 3)(4\ 5)            \tag{9.4}
\]

sends the three positive pairs in (9.2) to the three negative pairs and
vice versa.  Hence

\[
                              \tau B_2w=-B_2w.             \tag{9.5}
\]

In fact the positive pentagon factor is `tau` applied to the negative one,
up to row reindexing, so `tau w=-w` at every rank.  Pairing a packet with
its `tau`-copy in the **same** outer context therefore cancels the complete
trade, not merely its first unwanted shadow.

This leaves a precise port-preserving Haar target.  Embed rooted pentagons
in two or more inequivalent size-three contexts inside a size-four Dyck
factor (terminal concatenation, initial concatenation, or the outer
primitive context).  Their lifted rank-three images of (9.2) must cancel,
while their rank-two images must not.  All ambient `D_4` ports then remain
fixed by Proposition 7.1.  This is the rooted commutator version of the old
Haar suspension problem, and it avoids the port obstruction of Theorem 5.1
by construction.

## 10. The three natural size-four embeddings do not cancel

The preceding commutator target can be tested exactly for the three
one-node contexts

\[
                         x10,\qquad10x,\qquad1x0.        \tag{10.1}
\]

The answer for one copy in each context is negative.  The obstruction is an
exposed target in the two-external-coordinate arm after the three physical
coordinate injections are taken into account.

Decompose the rank-two effect (9.2) according to the seven positional
windows in (9.1).  On the six local coordinates put

\[
\begin{aligned}
 A={}&e_{15}+e_{35}-e_{24}-e_{14},\\
 B={}&e_{14}+e_{25}+e_{36}-e_{15}-e_{26}-e_{34},\\
 C={}&e_{24}+e_{26}-e_{35}-e_{36},\\
 D={}&e_3+e_4-e_2-e_5.                                  \tag{10.2}
\end{aligned}
\]

Here `A` and `C` are the two boundary-window effects, `B` is the sum of
the three core--core effects, and `D` is the sum of the two
parent-containing effects after deleting their common parent coordinate.
In particular

\[
                         A+B+C+7D=B_2w,                  \tag{10.2a}
\]

where `7D` means adjoining coordinate `7` to every singleton in `D`.

Let `a` be the selected coordinate of the added `10`, let `b` be its
unselected coordinate, and let `c` be the odd-graph parent coordinate.
If `xT` denotes adjoining every coordinate of the external set `T` to
every target in `x`, then the three lifted rank-three effects are

\[
\begin{aligned}
 \Delta_R&=aB+bC+cA+bcD &&(x10),\\
 \Delta_L&=aA+bB+cC+acD &&(10x),\\
 \Delta_J&=aA+bC+cB+abD &&(1x0).                       \tag{10.3}
\end{aligned}
\]

### Lemma 10.1 (context-effect table)

Equations (10.3) hold literally, target by target.

#### Proof

For `x10`, the rooted path is

\[
 S_0a,S_1a,S_2a,S_3a,\overline{S_0}b.
\]

The first boundary target acquires `c`, the three core--core targets
acquire `a`, the opposite boundary target acquires `b`, and each of the
two parent-containing targets acquires `bc`.  This is the first line of
(10.3).

The path for `10x` first exchanges `a` for `b` and then runs the old local
path with `b` fixed.  The corresponding four positional classes acquire,
respectively, `a,b,c,ac`, proving the second line.

For `1x0`, reverse the local flip order between the two outer flips.  The
core states after the initial state are

\[
 ab([6]\setminus Y_2),\quad
 ab([6]\setminus Y_1),\quad
 ab([6]\setminus Y_0).
\]

The four positional classes consequently acquire `a,c,b,ab`.  The middle
core term is the intersection `Y_0 intersect Y_1 intersect Y_2`; direct
use of the pentagon tables gives the same signed pair effect as the omitted
middle core--core term, namely `e_{34}-e_{25}`.  Thus the total single-`c`
class is exactly `B`, proving the third line. \(\square\)

### Theorem 10.2 (natural three-context obstruction)

Choose either orientation of the rooted pentagon independently in each of
the three contexts (10.1).  If every context is used nontrivially once,
their lifted rank-three effects cannot sum to zero.

#### Proof

Use the natural positions `1,...,8` and parent `9`.  The three injections
of the six local coordinates and their external triples are

\[
\begin{array}{c|c|c}
 x10&i\mapsto i&(a,b,c)=(7,8,9)\\
 10x&i\mapsto i+2&(a,b,c)=(1,2,9)\\
 1x0&i\mapsto i+1&(a,b,c)=(1,8,9).
\end{array}                                               \tag{10.4}
\]

In the right-concatenation copy, the `bcD` term contains

\[
                         +e_{389}+e_{489}-e_{289}-e_{589}. \tag{10.5}
\]

The only targets containing `9` in the left copy but not `1` come from its
`cC` term and are

\[
                         +e_{469}+e_{489}-e_{579}-e_{589}. \tag{10.6}
\]

The targets containing `9` in the outer-primitive copy but not `1` or `8`
come from its `cB` term and are

\[
 +e_{259}+e_{369}+e_{479}-e_{269}-e_{379}-e_{459}.       \tag{10.7}
\]

The remaining left and outer-primitive terms either omit `9` or contain
`1`.  Therefore target `389` occurs only in the right-concatenation copy.
Choosing the opposite orientation merely changes its coefficient from
`+1` to `-1`; it cannot make it zero.  Hence the sum of three nontrivial
copies is never rank-three invisible. \(\square\)

Thus the three canonical embeddings do not supply the desired rooted Haar
commutator.  A successful construction needs either repeated packets in
one context with different local relabellings whose `D` arms cancel, or a
larger rooted packet whose two-parent arm is zero internally.  This is an
exact support obstruction, not a quantitative shortage.

## 11. The unique-looking three-cycle cancellation also kills the Haar term

There is a second natural way to use three pentagons: keep all three in one
context and relabel the six local coordinates by the order-three
permutation

\[
                              g=(1\ 2\ 3)(4\ 6\ 5).       \tag{11.1}
\]

This does cancel the unwanted rank-three effect.  Unfortunately it cancels
the rank-two effect as well.

The edge orbits of `g` are

\[
\begin{gathered}
 \{12,23,13\},\quad\{46,56,45\},\\
 \{14,26,35\},\quad\{15,24,36\},\quad\{16,25,34\}.     \tag{11.2}
\end{gathered}
\]

### Lemma 11.1

For each of the signed edge functions `A,B,C` in (10.2), the coefficient
sum on every orbit in (11.2) is zero.  For `D`, the coefficient sum on each
vertex orbit `\{1,2,3\}`, `\{4,6,5\}` is zero.  Consequently, in any one
fixed outer context,

\[
                     (1+g+g^2)\Delta_3=0.              \tag{11.3}
\]

#### Proof

For `A`, its four nonzero edges pair as

\[
 (14)^-\leftrightarrow(35)^+,qquad
 (15)^+\leftrightarrow(24)^-.
\]

For `C` the same two orbits contain `26^+` against `35^-` and `24^+`
against `36^-`.  For `B`, its three cancellations are

\[
 14^+\leftrightarrow26^-,\qquad
 36^+\leftrightarrow15^-,\qquad
 25^+\leftrightarrow34^-.
\]

Finally `D=+3+4-2-5` has one positive and one negative vertex in each of
the two vertex orbits.  Orbit summation proves (11.3). \(\square\)

To inspect the next shadow, retain the positional decomposition used in
the proof of Lemma 10.1.  Besides `A,C`, its signed local pieces are

\[
\begin{aligned}
 B_0&=+24+25+14-15-35-34,\\
 B_1&=+34-25,\\
 B_2&=+35+36+25-34-24-26,\\
 D_0&=2e_4+e_2-2e_5-e_3,\\
 D_1&=2e_3+e_5-2e_2-e_4.                               \tag{11.4}
\end{aligned}
\]

The two triple-intersection pieces are `E_0=D_0` and `E_1=D_1` after
cancelling equal terms.

### Theorem 11.2 (three-cycle silence through rank two)

For the terminal-concatenation lift of the rooted pentagon,

\[
                         (1+g+g^2)\Delta_3=0,
 \qquad                  (1+g+g^2)\Delta_2=0.           \tag{11.5}
\]

The same holds, after the corresponding external relabelling, in either
of the other two one-node contexts.

#### Proof

The first equality is Lemma 11.1.  In (11.4), `B_0` cancels separately on
the first three cross-edge orbits in (11.2), `B_1` cancels on
`\{16,25,34\}`, and `B_2` cancels on the same three cross-edge orbits.
The vertex sums of `D_0,D_1` vanish separately on both vertex orbits.
The terminal-context rank-two formula consists only of
`A,C,B_0,B_2,D_0,D_1,E_0,E_1` with fixed external coordinates adjoined.
Every orbit sum is therefore zero.  Coordinate conjugacy gives the other
contexts. \(\square\)

Thus the most economical three-copy symmetry is too symmetric: it erases
the desired Haar residue together with the preceding shadow.  Combined
with Theorem 10.2, this leaves no three-pentagon construction among the two
canonical patterns (one in each context, or one `C_3` orbit in one
context).  Mixed context-dependent relabellings, or at least four rooted
packets, remain open.

## 12. Fixed-context rooted pentagons can never produce Haar

The preceding three-cycle is not an accidental over-cancellation.  In a
fixed outer context, **every** linear combination of coordinate-relabelled
rooted pentagons that cancels at the lifted middle rank also cancels at the
next rank.  Thus increasing the number of pentagons inside one context
cannot solve the Haar problem.

Let `h` be an arbitrary element of the real group algebra of the six local
coordinates.  It represents any signed multiset of relabelled rooted
pentagon trades in one fixed context: the coefficient sign records the
orientation of each pentagon.  The external coordinates are held fixed.

### Theorem 12.1 (fixed-context Haar no-go)

For any of the three one-node contexts in (10.1), let `Delta_3` and
`Delta_2` be the lifted rank-three and rank-two effects of a rooted
pentagon.  Then

\[
                         h\Delta_3=0
             \quad\Longrightarrow\quad
                         h\Delta_2=0.                  \tag{12.1}
\]

Consequently no number of coordinate-relabelled rooted pentagon packets
confined to one fixed context can yield a nonzero Haar residue one rank
below a cancelled lifted middle effect.

#### Proof

First consider the terminal context `x10`.  By (10.3),

\[
                       h\Delta_3
                 =a(hB)+b(hC)+c(hA)+bc(hD).            \tag{12.2}
\]

The four displayed terms have four different intersections with the
external coordinate set `\{a,b,c\}`, namely `\{a\}`, `\{b\}`, `\{c\}`,
and `\{b,c\}`.  Their target supports are therefore disjoint.  Hence

\[
 h\Delta_3=0
       \quad\Longrightarrow\quad
 hA=hB=hC=hD=0.                                        \tag{12.3}
\]

The positional pieces in (11.4) satisfy the exact identities

\[
       B_0=B+C,\qquad B_1=-(A+B+C),\qquad B_2=A+B.      \tag{12.4}
\]

Let `deg` be the edge-to-vertex incidence map,
`deg(e_{ij})=e_i+e_j`.  Directly from (10.2) and (11.4),

\[
 \deg A=-D_0,\qquad \deg C=-D_1,\qquad
 D=D_0+D_1,\qquad E_0=D_0,\quad E_1=D_1.               \tag{12.5}
\]

The incidence map is equivariant under coordinate relabelling.  Thus
(12.3)--(12.5) imply

\[
 hB_0=hB_1=hB_2=hD_0=hD_1=hE_0=hE_1=0.                \tag{12.6}
\]

The targetwise positional expansion used in Lemma 10.1 expresses the
terminal-context rank-two effect entirely through

\[
        A,C,B_0,B_1,B_2,D_0,D_1,E_0,E_1
\]

with fixed external coordinates adjoined.  Equation (12.6), together
with `hA=hC=0`, therefore gives `h Delta_2=0`.

For `10x` and `1x0`, the four rank-three sections in (10.3) again have
pairwise distinct external-coordinate intersections.  They consequently
give the same implication (12.3), with `A,B,C` permuted.  The local
identities (12.4)--(12.5) are unchanged, so the rank-two conclusion follows
identically. \(\square\)

Theorem 12.1 leaves only genuinely mixed-context cancellation (where the
external sections of different embeddings can overlap after their
physical coordinate injections) or a larger primitive rooted packet whose
two-parent arm vanishes internally.  In particular, the phrase “at least
four rooted packets” at the end of Section 11 is insufficient by itself:
arbitrarily many packets still fail if they remain in one context.
