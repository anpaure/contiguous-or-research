# Exact owner-level `Q_8` carousel, sparse-seam suspension, and the transverse-kernel boundary

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The standard four-stage `Q_8` frame carousel does have a literal
owner-level composition.  Let `P^(j)`, `j in Z_4`, be the four crossed
factors associated with

\[
 S_j=SK^j,\qquad S=(2\ 4),\qquad K=(1\ 2\ 3\ 4).
\]

Partition `Q_8=Q_4^L\times Q_4^R` into the four child-parity classes

\[
 C_0=(0,0),\quad C_1=(0,1),\quad C_2=(1,1),\quad C_3=(1,0).
\]

Every `P^(j)` sends `C_i` bijectively to `C_(i+1)`.  Therefore

\[
             R(x)=P^{(i)}(x)\qquad (x\in C_i)                 \tag{0.1}
\]

is a neighbour permutation of all 256 owners.  A direct phase calculation
shows that every `R`-component has direction word `omega omega`, with
`omega` a permutation of the eight directions.  Thus `R` is an exact
isometric `C_16`-factor.  The minimal 24-owner obstruction is avoided rather
than amortized: the larger synchronized construction never uses its
forbidden within-component mixed hub.  This statement does not assert a
new factor-wide `X/Y` decoder across the sixteen components.

The factor has an exact long-payload suspension.  Insert, after each of the
eight first-half carousel directions, a disjoint block of `L` fresh
directions, and repeat the resulting first-half word.  This gives sixteen
owner-disjoint isometric cycles of length

\[
                         16(L+1)                              \tag{0.2}
\]

on an explicit carrier of `256(L+1)` owners.  There are sixteen seam edges
per macrocycle.  At depth `q`, at most `16q` cyclic starts, or the fraction

\[
                         {q\over L+1},                        \tag{0.3}
\]

meet a seam.  In particular the requested maximum-depth bound is
`H/(L+1)=O(H/L)`.

This is a genuine local composition theorem, but not yet `CPM` or `EMSF`.
If every seam-crossing occurrence is quarantined, the two signed ledgers
summed through depth `H` cost at most

\[
                         {H(H+1)\over L+1}\,G                \tag{0.4}
\]

on carrier mass `G`.  Thus black-box seam disposal requires `L >> H^2`,
whereas `CPM/EMSF` impose `H/sqrt(m) -> infinity` and allow only `L<m`
(indeed `L<=r=o(m)` in the packet formulation).  Consequently sparse seams
alone cannot yield the required `o(W)` aggregate hole bound.

There are two different bottom-kernel conclusions, and they must not be
conflated.

1. The owner-level factor (0.1) uses the standard four shores, all in one
   phase-kernel normalizer.  It retains the inherited bottom-wire system
   and therefore cannot by itself remove the Gaussian fixed-frame deficit.
2. A catalogue of individually valid coordinate-conjugate `Q_8` cells can
   be made transverse enough that its abstract port matchings have no common
   nontrivial block system.  This is **not** a closed carousel in one common
   gauge: the conjugations also change the reference factors.  Thus it does
   not refute the bottom-block theorem for actual common-gauge finite
   substitutions.  No owner-level lift of this transverse catalogue is
   presently proved.

The exact surviving gate is therefore a kernel-changing owner splice with
a correlated multidepth seam decoder.  Such a decoder must repair almost
all seam-crossing windows; diluting them is quantitatively insufficient.

## 1. Phasewise owner splicing

We first record the exact ownership mechanism.

### Lemma 1.1 (phasewise splice)

Let

\[
                         V=C_0\dot\cup\cdots\dot\cup C_{r-1}
\]

and let `F_0,...,F_(r-1)` be permutations of `V` satisfying

\[
                         F_j(C_i)=C_{i+1}                    \tag{1.1}
\]

for every `i,j`, with indices modulo `r`.  Then

\[
                         F(x)=F_i(x)\quad(x\in C_i)          \tag{1.2}
\]

is a permutation.  If all selected edges are edges of the same ambient
graph, then `F` is a factor of that graph.

#### Proof

For fixed `i`, the restriction `F_i:C_i -> C_(i+1)` is an injection between
finite sets and is onto by (1.1).  The four restrictions in (1.2) have
disjoint domains and disjoint images, and their images partition `V`.
Their union is therefore a bijection.  The edge assertion is immediate.
\(\square\)

For a `Q_8` owner `x=(u,v)`, write

\[
 p_L=|u|\pmod2,\qquad p_R=|v|\pmod2.
\]

At total even parity every crossed shore changes one right coordinate, and
at total odd parity it changes one left coordinate.  Independently of `j`,

\[
 (0,0)\to(0,1)\to(1,1)\to(1,0)\to(0,0).             \tag{1.3}
\]

Every `P^(j)` is already a permutation, so each arrow is a bijection of
the corresponding 64-owner classes.  Lemma 1.1 proves exact ownership of
(0.1).  Notice that this argument does not choose independent shores of
the connected two-factor overlay; it chooses one entire phase restriction
from each factor.

## 2. Exact isometry

Use zero-based parent direction labels in `Z_4`.  The standard parent
direction at phase `c` is `d(c)=c`, and

\[
                         S_j(i)=-(i+j)\pmod4.                 \tag{2.1}
\]

For the common-phase `Q_4` quotient, translation in direction `i` changes
phase `a` by

\[
                         a\longmapsto a+(-1)^{a+i}.           \tag{2.2}
\]

Start an `R`-orbit in `C_0`, and let its two parent phases be the even
values `c,c'`.  The first four stages are

\[
\begin{array}{c|c|c|c}
 j&\text{child}&\text{direction}&\text{new phase pair}\\ \hline
0&R&R(-c)&(c,c'+1)\\
1&L&L(-c'-2)&(c+1,c'+1)\\
2&R&R(1-c)&(c+1,c'+2)\\
3&L&L(-c'-1)&(c+2,c'+2).
\end{array}                                                \tag{2.3}
\]

The next four directions are

\[
             R(-c-2),\quad L(-c'),\quad
             R(-c-1),\quad L(1-c').                         \tag{2.4}
\]

Consequently the four right labels are

\[
                         -c,1-c,2-c,3-c,
\]

and the four left labels are

\[
                         -c'-2,-c'-1,-c',1-c'.
\]

Each list is all of `Z_4`.  The first eight moves therefore use every one
of the eight directions exactly once and carry the owner to its complement.
Complementation adds `1111` inside each parent, which belongs to the parent
phase kernel, so the two phases and the shore rule repeat.  The next eight
moves repeat the same permutation of directions and return to the start.
No earlier return is possible: a nonempty proper interval of at most eight
moves has no repeated direction, and the displacement after eight moves is
the all-one vector.  Hence every component is an isometric `C_16`.

Since the 256 owners are partitioned, there are exactly sixteen components.
In particular all lower and upper depth-one traces on each component are
injective.  This is why the conclusion does not contradict the 24-owner
mixed-hub theorem: the phasewise path through the 256-owner support is not
a 2-factor of one minimal quartet union at a mixed hub.

## 3. Two-sided ports really close

For the standard crossed shore `P^(j)`, let `Xi_j^+` and `Xi_j^-` be its
same-owner successor and predecessor frames relative to the aligned shore.
The two-sided primitive proves

\[
                         \Xi_j^- = \Xi_{j+1}^+.               \tag{3.1}
\]

An `R`-edge entering a state of `C_j` belongs to `P^(j-1)`; the edge leaving
that state belongs to `P^(j)`.  Their relative incoming and outgoing frame
labels are `Xi_(j-1)^-` and `Xi_j^+`, which agree by (3.1).  Thus a payload
inserted at this interface may use that common fixed frame.  Four stages
return the frame label, while an `R` first half makes two complete turns of
the four-stage carousel.

This equality is used only as a port certificate.  Exact ownership came
from Lemma 1.1 and exact isometry came from (2.3)--(2.4); neither conclusion
is inferred from formal frame equality alone.

## 4. Long-payload macrocycles

Fix `L>=1`.  For the eight first-half positions choose mutually disjoint
fresh direction blocks

\[
                         D_0,\ldots,D_7,qquad |D_t|=L,
\]

with ordered words `rho_t`.  If the first-half word of an `R`-component is
`w_0...w_7`, form

\[
 w_0\rho_0\,w_1\rho_1\cdots w_7\rho_7                 \tag{4.1}
\]

and repeat (4.1).  Its first copy uses every one of the `8+8L` directions
exactly once.  Its second copy repeats them, so it is an isometric cycle of
length `2(8+8L)=16(L+1)`.

Lift all sixteen `R`-cycles from a common all-zero payload state.  Distinct
lifted cycles have disjoint projections to the sixteen disjoint base
cycles; hence their owner supports are disjoint.  Their union is an exact
factor of the declared carrier

\[
                         \mathcal S_L,qquad
                         |\mathcal S_L|=16\cdot16(L+1)
                                             =256(L+1).       \tag{4.2}
\]

This is an exact packet carrier, not a factorization of the full
`Q_(8+8L)`.  Packing translates or contextual copies of `S_L` on almost all
ambient middle owners is an additional theorem.

Raw doubled-permutation isometry holds for every `L`.  A stronger literal
payload assertion needs a phase condition.  If one wants to inherit the
original parity-indexed pair-frame ledger with no separate reset, take `L`
even: the seam at position `t(L+1)` then has the original parity `t`.  For
odd `L`, an explicit phase-reset/port certificate is required.  In either
case an arbitrary word `rho_t` proves isometry only, not the payload's
literal lower/upper decoder.

## 5. Seam arithmetic and the `CPM/EMSF` boundary

There are sixteen occurrences of a base direction on one macrocycle and
`16L` payload edges.  Call the base-direction occurrences seams.  One edge
belongs to exactly `q` directed cyclic windows of `q` transitions.  Thus at
depth `q<=L`,

\[
 \#\{\text{starts meeting a seam}\}\le16q,
 \qquad
 {\#\text{ exceptional starts}\over16(L+1)}
      \le {q\over L+1}.                                  \tag{5.1}
\]

The same statement holds in the reverse orientation.  Every nonexceptional
window lies wholly inside one payload run.  If that payload carries an
already verified fixed-frame literal decoder, adjoining frozen base and
exterior coordinates preserves the certificate.  An arbitrary direction
order is not, by itself, a literal `X/Y` decoder.

For the simultaneous signed ledger, each exceptional start can lose one
lower and one upper target.  Therefore one macrocycle has at most

\[
 2\sum_{q=1}^H16q=16H(H+1)                              \tag{5.2}
\]

uncertified signed occurrences.  A carrier family of owner mass `G` has
`G/[16(L+1)]` macrocycles, so

\[
 \sum_{q=1}^H(E_q^-+E_q^+)
       \le {H(H+1)\over L+1}\,G.                         \tag{5.3}
\]

The maximum-depth or run/component toll is only `O(GH/L)`, but the
all-depth target toll is `O(GH^2/L)`.

In `EMSF`, `H/sqrt(m)->infinity` and every strip has half-length below `m`.
In `CPM`, the payload scale is at most the packet radius `r=o(m)`.  Hence

\[
                         {H^2\over L}\ge {H^2\over m}\to\infty,
                                                                  \tag{5.4}
\]

so (5.3) cannot be made `o(G)` by choosing longer legal payloads.  This is
not a lower bound on the actual target holes—other packets could cover the
same targets—but it is a rigorous no-go for the black-box strategy that
discards every seam collar.

To feed `EMSF`, one must instead prove at least one of the following.

1. A literal correlated seam decoder/collision-capture rule that reduces
   the aggregate uncaptured charge from `Theta(H^2)` to `O(H)` per
   macrocycle; then `H/L->0` would suffice.
2. A global colored packet matching that covers almost every exceptional
   seam target from other owner-disjoint packets.

Even after the first item, `CPM` still requires owner-disjoint packing with
leave `o(W)` and simultaneous target holes `o(W)`.

## 6. The standard carousel retains its bottom kernel

Let

\[
 H=\langle e_1+e_3,e_2+e_4\rangle,
 \qquad K_8=H_L\oplus H_R.                              \tag{6.1}
\]

Every standard reflection `S_j=SK^j` belongs to the parent wire
normalizer, and every shore `P^(j)` has direction field constant on cosets
of `K_8`.  The selector in (0.1) depends only on the two child parities,
which are themselves constant on `K_8`-cosets.  Thus the spliced direction
field is also constant on those cosets.  Its accumulated frame labels
normalize the four bottom wires

\[
 L\{1,3\},\quad L\{2,4\},\quad
 R\{1,3\},\quad R\{2,4\}.                              \tag{6.2}
\]

Fresh payloads placed in frames compatible with (6.2) do not alter this
fact.  Therefore the owner theorem and sparse suspension close the local
composition gate but do not escape the known fixed-pair Gaussian deficit.
If only seam collars leave this category, then at
`q=floor(A sqrt(m))` their exceptional mass is `o(W)` when `H/L->0`, while
the fixed-frame pair-type deficit remains `Omega_A(W)`.  Consequently a
standard-kernel carousel alone cannot satisfy the target condition of
either `CPM` or `EMSF`.

The common matching is visible directly on every completed macrocycle.
Writing its first-half word as

\[
 \pi=(w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7),
\]

the antipodal offset is `4(L+1)`.  It pairs `w_t` with `w_(t+4)` and the
`a`-th payload direction in `D_t` with the `a`-th direction in `D_(t+4)`.
The first pairs are exactly the standard `Q_8` bottom wires.  Hence all
sixteen macrocycles share one enlarged positional antipodal matching.  If,
as assumed in the preceding paragraph, every payload frame is compatible
with the common phase kernel, its direction field normalizes this matching
and the suspension is genuinely imprimitive.  The positional fact alone
does not impose a group-theoretic invariant on an arbitrary payload
decoder.

### Proposition 6.1 (common-gauge finite-carousel invariant)

Let a finite owner substitution be assembled from standard `Q_8` cells,
kernel-compatible coordinate conjugacies, tensor placements, serial
composition, and arbitrary componentwise or owner-dependent shore choices.
Assume every interface is expressed relative to one literal reference
factor and one common phase decoder with kernel

\[
                         K_b=H^{\oplus b}.
\]

Then every accumulated frame label lies in `N(K_b)` and preserves the
weight-two bottom-wire system recovered from `K_b`.

#### Proof

Every standard cell normalizes `H` on its active `Q_4` child.  A coordinate
conjugacy compatible with the same literal decoder must preserve its coset
fibres; equivalently it normalizes `K_b`.  Tensor placement takes direct
sums of these kernels.  The normalizer is closed under products, and an
owner-dependent selector chooses, at each owner separately, one element of
the same normalizer.  Therefore every accumulated statewise label is in
`N(K_b)`.  The weight-two elements of `K_b` recover exactly the bottom
two-point blocks, so those blocks are preserved.  \(\square\)

This proposition is the rigorous finite-carousel obstruction.  It does
not cover a new interface which itself transports one phase decoder to a
different kernel; constructing exactly that interface is the open escape.

## 7. A transverse abstract port catalogue destroys every port-only block

The preceding invariant is architectural, not a theorem about all finite
port carousels.  On direction labels `{0,...,7}`, define

\[
\begin{aligned}
B_0&=(01)(23)(45)(67),\\
B_1&=(12)(34)(56)(70),\\
B_2&=(03)(24)(15)(67),\\
B_3&=B_1,\qquad B_4=B_0.
\end{aligned}                                               \tag{7.1}
\]

The unions `B_0\cup B_1` and `B_1\cup B_2` are respectively the
Hamilton cycles

\[
 0,1,2,3,4,5,6,7,0
 \quad\text{and}\quad
 0,3,4,2,1,5,6,7,0,                                    \tag{7.2}
\]

and the remaining consecutive unions are their reversals.  The ordered
port pair of every standard two-sided `Q_8` cell is also a pair of perfect
matchings with Hamilton union.  All such ordered pairs form one
`S_8`-conjugacy class.  Hence each pair `(B_j,B_(j+1))` is the exact ordered
port pair of an individually valid coordinate-conjugate `Q_8` cell.  The
abstract permutations at consecutive ports agree.  This last equality is
not yet a common-gauge owner interface; Section 8 gives the missing gauge
equation.

The antipodal bottom matchings of the two Hamilton cycles in (7.2) are

\[
 W_0=04|15|26|37,
 \qquad
 W_1=01|35|46|27.                                      \tag{7.3}
\]

Their union is the Hamilton cycle

\[
                         0,4,6,2,7,3,5,1,0.             \tag{7.4}
\]

If `K(W)=span{e_u+e_v:uv in W}`, a vector in `K(W_0) intersect K(W_1)`
has support that is a union of edges of both matchings.  Connectedness of
(7.4) forces its support to be empty or all eight labels.  Therefore

\[
                         K(W_0)\cap K(W_1)
                         =\{0,\mathbf1^8\}.             \tag{7.5}
\]

There is no hidden larger block system.  The regular dihedral group
`<B_0,B_1>` has five two-point systems

\[
\begin{gathered}
01|23|45|67,\quad07|12|34|56,\quad04|15|26|37,\\
03|12|47|56,\quad05|14|23|67,
\end{gathered}
\]

and three four-point systems

\[
0145|2367,\qquad0347|1256,\qquad0246|1357.
\]

The matching `B_2` destroys the five two-point systems on the witnesses

\[
 01\mapsto35,\quad07\mapsto36,\quad04\mapsto23,
 \quad12\mapsto45,\quad05\mapsto13,
\]

and sends the displayed first shores of the four-point systems to

\[
                         1235,\qquad0236,\qquad2347,
\]

respectively.  Thus

\[
                         \langle B_0,B_1,B_2\rangle
                         \text{ is primitive}.         \tag{7.6}
\]

This refutes only a universal invariant deduced from the abstract port
permutations.  It does not refute the bottom-block invariant for actual
owner-spliced common-reference carousels.

## 8. Why the transverse atlas is not yet an owner carousel

The phasewise construction of Sections 1--2 needs one common ordered
partition `(C_0,C_1,C_2,C_3)` advanced by every shore.  For a conjugate
two-child `Q_8` cell, its two port matchings cross the cell's left/right
four-coordinate bipartition.  A common child-parity phase partition would
therefore require all `B_j` to cross one common `4+4` bipartition.

The unique Hamilton bipartitions (up to complement) are

\[
 A_0=\{0,2,4,6\}\quad(j=0,3),
 \qquad
 A_1=\{0,1,4,6\}\quad(j=1,2).                         \tag{8.1}
\]

They are unequal even up to complement.  Equivalently, the union of the
three port matchings contains the triangle

\[
                         2\mathbin{-}3\mathbin{-}4
                         \mathbin{-}2,                 \tag{8.2}
\]

using `23 in B_0`, `34 in B_1`, and `24 in B_2`.  Thus their union is not
bipartite.  In particular the proof of Lemma 1.1 cannot be transported to
these independently conjugated cells.

There is a more fundamental gauge defect.  If `g_j` is the conjugation used
for cell `j`, its reference factor is

\[
                         P_{0,j}=g_jP_0g_j^{-1}.
\]

The two relative-frame equations at a proposed interface are

\[
\begin{aligned}
 \delta^-_{P_{1,j}}(x)&=B_{j+1}\delta^-_{P_{0,j}}(x),\\
 \delta^+_{P_{1,j+1}}(x)&=B_{j+1}\delta^+_{P_{0,j+1}}(x).
\end{aligned}                                               \tag{8.3}
\]

Cancelling the common abstract involution shows that literal closure still
requires an owner-port identification carrying

\[
             \delta^-_{P_{0,j}}(x)
             \quad\hbox{to}\quad
             \delta^+_{P_{0,j+1}}(x).                       \tag{8.4}
\]

Independent coordinate conjugacy supplies no such identification, because
the field \(g_j\delta_0(g_j^{-1}x)\) uses a different owner and phase gauge
from the next cell.  Thus equality of consecutive `B` labels alone neither
identifies actual owner ports nor proves one predecessor and successor at
every owner.

The two formal kernels in (7.3) differ by one alternating eight-cycle.  Exactly
three quartet 2-switches are necessary and sufficient to pass between
them; an explicit shortest chain is

\[
\begin{aligned}
04|15|26|37
&\longrightarrow01|45|26|37\\
&\longrightarrow01|46|25|37\\
&\longrightarrow01|35|46|27.
\end{aligned}                                               \tag{8.5}
\]

Sufficiency is displayed.  For necessity, the union of the initial and
target matchings has one alternating component, whereas equality has four;
one 2-switch increases the number of target-common components by at most
one.

Implementing any step of (8.5) by the minimal 24-owner two-sided
associator does not solve the owner splice.  Every genuine mixed hub repeats
either its lower intersection or its upper union, so this route cannot
supply a two-sided trace-injective compiler.  Long inert payloads can
separate such mixed collars but cannot make the repeated literal trace
disappear.  The stronger graph/strip failure is proved below for the
explicit Hamilton rail.

### 8.1 Sharp long-rail test for the minimal-quartet route

The preceding last sentence has an exact growing-support realization.
Take disjoint payload pairs `r_i={x_i,y_i}`, `1<=i<=L`, and an isometric
orientation cycle

\[
 Y_0,Y_1,\ldots,Y_{2L}=Y_0
\]

with direction word `(r_1,...,r_L)^2`.  On four further coordinates put

\[
 A=ac,\quad B=bd,\quad C=ab,\quad D=cd,
 \quad U=bc,\quad V=ad.                                  \tag{8.6}
\]

Let `T_L` consist of

\[
 A\cup Y_t,C\cup Y_t\quad(0\le t\le L),
\]

\[
 B\cup Y_t,D\cup Y_t\quad(L\le t\le2L),
\]

and `U,V` over each of `Y_0,Y_L`.  Then

\[
                         |T_L|=4L+8.                         \tag{8.7}
\]

The separated factor has the two cycles

\[
 AY_0\cdots AY_L,\ UY_L,\ BY_L\cdots BY_0,\ VY_0,
\]

\[
 CY_0\cdots CY_L,\ VY_L,\ DY_L\cdots DY_0,\ UY_0.
\]

Their direction words are

\[
 (r_1,\ldots,r_L,ab,cd)^2,
 \qquad
 (r_1,\ldots,r_L,bd,ac)^2,                            \tag{8.8}
\]

so both are literal isometric `C_(2(L+2))` cycles and partition `T_L`.

There is also one exact Hamilton replacement on all of `T_L`:

\[
\begin{aligned}
 AY_0\cdots AY_L,&\ UY_L,\ DY_L\cdots DY_0,\ UY_0,\\
 CY_0\cdots CY_L,&\ VY_L,\ BY_L\cdots BY_0,\ VY_0.
\end{aligned}                                               \tag{8.9}
\]

It has one predecessor and successor at every owner.  Its four rail sectors
have the formal quartet-frame sequence

\[
 ab|cd,\quad ac|bd,\quad ac|bd,\quad ab|cd.             \tag{8.10}
\]

Equation (8.10) is only the minimal-quartet analogue of the transverse
`Q_8` catalogue; because of (8.3)--(8.4), it is not an owner realization of
the `B_j` cells.

For `1<=q<=L`, exactly `4(L-q+1)` starts have their `q` edges wholly within
one rail.  Hence exactly

\[
                         4q+4                              \tag{8.11}
\]

starts meet collars, the exact fraction `(q+1)/(L+2)`.

Nevertheless (8.9) is not an isometric strip.  At the first mixed collar,

\[
 (A\cup Y_L)\cap(U\cup Y_L)
 =(U\cup Y_L)\cap(D\cup Y_L)=Y_L\cup\{c\},              \tag{8.12}
\]

while at the second,

\[
 (C\cup Y_L)\cup(V\cup Y_L)
 =(V\cup Y_L)\cup(B\cup Y_L)=Y_L\cup\{a,b,d\}.          \tag{8.13}
\]

All other depth-one traces are distinct: rail traces and collar traces have
different special-coordinate cardinalities, the clean `Y_0` collars have
four distinct singleton/triple traces, and \(Y_0\ne Y_L\).  Thus there is
exactly one repeated lower and one repeated upper depth-one trace.

For `2<=q<=L`, exactly `q-1` windows containing both edges of the `A-U-D`
collar have lower intersection one rank too large.  Exactly `q-1` windows
containing both edges of `C-V-B` have upper union one rank too small.  The
clean collars are locally geodesic.  Thus payload length can make the
collars sparse, but cannot make the Hamilton replacement a legal compiler
strip.

More generally, every closed rail carousel whose only cross-sector
connectors are these minimal mixed hubs has at least two sector transitions.
The mixed-hub trace table charges at least one lower or upper repetition to
each transition; distinct payload contexts make the charges additive.
The construction (8.9) attains the lower bound two.  This is a sharp no-go
for the minimal-collar architecture, not for arbitrary larger collars.

If one cuts or quarantines the bad collars, their all-depth occurrence bill
is `Theta(H^2)` per carrier and `Theta(H^2W/L)` at positive owner density.
The `O(H/L)` one-depth fraction therefore does not certify `EMSF`.  At
depth one, `K` owner-disjoint such carriers in any completion to all `W`
owners have combined collision excess at least `2K`, giving the capacity
bound

\[
 M_1^-+M_1^+\ge
 \bigl[2K-2(W-N_1)\bigr]_+,
 \qquad W-N_1={W\over m+1}.                            \tag{8.14}
\]

Exact depth-one coverage would force `L=Omega(m)` at positive density.
However `CPM` permits `o(W)` holes, so (8.14) alone does **not** contradict
`CPM` when `L->infinity`.  The unconditional obstruction is instead that
(8.9) is not an isometric compiler option at all.

## 9. Exact proved/conditional boundary

The following statements are proved.

1. The standard four-stage carousel has the exact owner factor (0.1).
2. Every component is an isometric `C_16`, with literal two-sided port
   closure.
3. Its long-payload carrier has exact size `256(L+1)`, seam fraction at
   most `q/(L+1)` at depth `q`, and aggregate quarantine charge (5.3).
4. The standard owner factor retains its common bottom kernel.
5. A transverse catalogue has no common nontrivial block at the level of
   its abstract port permutations, but its independently conjugated cells
   use different reference gauges and do not form an owner carousel.
6. The common phase splice cannot apply to that catalogue because its
   natural Hamilton bipartitions differ.  The minimal-quartet long-rail
   implementation has the sharp two-sided collision (8.12)--(8.13).
7. Every actual finite carousel built with one literal reference factor,
   one common phase decoder, and the known `Q_8`-generated interfaces
   preserves the corresponding bottom-wire system statewise.  Products,
   tensors, and owner-dependent choices stay in its normalizer.

What remains conditional is exactly the following.

**Remaining lemma (9.1).**  Construct a common-gauge owner transition
between genuinely different phase kernels whose completed components are
literal isometric strips and whose uncaptured seam windows have total
signed charge \(o(W)\) through all \(q\le H\).

For compatibility with the existing endgame, (9.1) must then be packed
owner-disjointly on `W-o(W)` owners.  A proof of the corresponding colored
packet selection is `CPM`; its output is an `EMSF`, and `EMSF` implies the
constant-one contiguous-OR upper bound.  Neither implication may be
invoked from the local carousel alone.
