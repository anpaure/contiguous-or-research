# First-eligible (B_4) cyclic-SCD packets: an explicit context-dependent middle factor

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Result

The four-coordinate cyclic SCD seed can be packed context-dependently over
almost the entire middle layer.

Partition all but at most three of the (2m) coordinates into ordered
four-blocks.  In each four-block use the local cycle

\[
 14\longrightarrow12\longrightarrow23\longrightarrow34
 \longrightarrow14.                                      \tag{0.1}
\]

Call these four local states eligible.  For a middle set (X), choose its
first (r) eligible blocks, where

\[
 H\ll r\le m/16,qquad r	ext{ is a power of two},qquad h=2r. \tag{0.2}
\]

Varying the four local states in those selected blocks, while freezing every
other coordinate, gives a canonical packet isomorphic to (Q_{2r}=Q_h).
The packets are disjoint, and all but (e^{-Omega(m)}W) middle sets lie in
one of them.  Applying the exact Hamming (C_{2h})-factor in every packet
therefore gives an explicit owner-disjoint physical-strip factor with
exponentially small middle leave.

Moreover, if the two directions of each local block are sibling leaves in
the recursive Hamming order, then for every (qle r) both signed
consecutive-window maps are injective **inside each packet**.  Thus the local
SCD seed, the context-dependent packetization, the long physical cycles, and
all intrapacket flag equations are solved exactly.

What is not solved is the outer packet problem.  Different first-eligible
packets can emit the same physical shadow.  To obtain the radius-resolved
SCD kernel, one still must choose nested radius-eligible positions so that
the aggregate cross-packet collision/flag defect is (o(W)).  The theorem
below isolates that as the only missing identity for this explicit
construction.

## 1. The local cyclic SCD cell

On a block (B={1,2,3,4}), put

\[
 \mathcal A={14,12,23,34}.                            \tag{1.1}
\]

The order (0.1) is a physical (Q_2=C_4).  Its successive lower edge
labels are

\[
 1,2,3,4,                                               \tag{1.2}
\]

and its successive upper labels are

\[
 124,123,234,134.                                       \tag{1.3}
\]

Both lists are injective.  This is the central cycle of the exact SCD

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24.
\end{array}                                             \tag{1.4}
\]

Thus (1.2)--(1.3) are simultaneously the physical edge shadows and the
lower/upper rank-one SCD flags.

## 2. The canonical packet partition

Let

\[
 B_1<B_2<\cdots<B_b,qquad b=\lfloor m/2\rfloor,       \tag{2.1}
\]

be disjoint four-coordinate blocks; freeze the at most three remaining
coordinates as part of the outside context.

For a middle set (X), call (i) eligible when

\[
 X\cap B_i\in\mathcal A.                               \tag{2.2}
\]

If (X) has at least (r) eligible indices, let

\[
 I(X)=\{i_1<\cdots<i_r\}                                \tag{2.3}
\]

be the first (r).  Define its packet by freezing (X) outside these
blocks and allowing every local state in (mathcal A) inside them:

\[
 \mathcal P(X)=left{Y:
 Y\setminus\bigcup_{i\in I(X)}B_i
 =X\setminus\bigcup_{i\in I(X)}B_i,quad
 Y\cap B_i\in\mathcal A (i\in I(X))ight}.          \tag{2.4}
\]

### Lemma 2.1 (context stability)

For every (Yinmathcal P(X)),

\[
 I(Y)=I(X),qquad mathcal P(Y)=mathcal P(X).          \tag{2.5}
\]

Consequently the retained middle sets are partitioned into packets of size

\[
 |mathcal P|=4^r=2^{2r}.                               \tag{2.6}
\]

#### Proof

Every selected block remains in (mathcal A), so remains eligible.  Every
unselected block is frozen.  Before the last selected index there were no
additional eligible blocks, by the first-(r) rule, and this remains true.
Thus the ordered first (r) eligible indices are unchanged.  Equation
(2.4) then gives the same equivalence class. \(\square\)

Each local cycle (0.1) is a (Q_2).  Their Cartesian product identifies
every packet with

\[
 (Q_2)^r=Q_{2r}=Q_h.                                   \tag{2.7}
\]

## 3. Exponentially small middle leave

Choose a uniformly random middle set.  Equivalently, choose each coordinate
independently with probability (1/2), and condition on total size (m).
Before conditioning, the eligibility events of the (b) disjoint
four-blocks are independent and

\[
 \Pr(X\cap B_i\in\mathcal A)=\frac4{16}=rac14.       \tag{3.1}
\]

Let (Jsim\operatorname {Bin}(b,1/4)).  If (rle b/8), Chernoff gives

\[
 \Pr(J<r)\le e^{-c b}                                  \tag{3.2}
\]

for an absolute (c>0).  Also

\[
 \Pr(|X|=m)=2^{-2m}\binom{2m}m=\Theta(m^{-1/2}).       \tag{3.3}
\]

Hence conditioning costs at most a factor (O(\sqrt m)):

\[
 \Pr(J<r\mid |X|=m)
 \le O(\sqrt m)e^{-cb}=e^{-\Omega(m)}.                \tag{3.4}
\]

### Theorem 3.1 (context-dependent physical middle factor)

If (r) is a power of two and satisfies (0.2), the retained middle layer
has an exact owner-disjoint factor into physical (C_{4r}=C_{2h})'s.  Its
leave (E) satisfies

\[
 E=e^{-\Omega(m)}W.                                    \tag{3.5}
\]

#### Proof

Lemma 2.1 partitions the retained owners into (Q_h)-packets.  Since
(h=2r) is a power of two, the exact maximum-isometric Hamming factor
partitions every (Q_h) into (C_{2h})'s.  Equation (3.4) proves the leave
bound. \(\square\)

For the SCI scale one may take, for example,

\[
 r=2^{\lfloor(3/4)\log_2m\rfloor-O(1)},qquad h=2r,    \tag{3.6}
\]

so (H/h=o(1)) and (h=o(m)).

## 4. Exact intrapacket all-depth injectivity

Order the (2r) Hamming directions so that the two directions belonging to
one four-block are siblings at the bottom of the recursive direction tree.
Use the forward orientation (0.1) in every local block and no optional parent
reversals.

The dyadic balance law of the recursive Hamming factor says that any window
of (qle r) consecutive directions uses a local block at most once.
Therefore a lower (q)-shadow has, in each block,

* its original rank-two state if the block was untouched;
* one of the four distinct singleton labels (1.2) if it was touched.

The target identifies the touched blocks by local rank and recovers the
unique original local state from (1.2).  The upper proof uses local ranks two
and three and the injective list (1.3).

### Theorem 4.1 (packetwise flag injectivity)

For every packet and every (1\le q\le r), the maps

\[
 X\longmapsto\bigcap_{j=0}^{q}F^j(X),qquad
 X\longmapsto\bigcup_{j=0}^{q}F^j(X)                  \tag{4.1}
\]

are injective on all starts of all cycles in that packet.

In particular, every collision in the global factor of Theorem 3.1 is a
collision between distinct first-eligible packets.

## 5. Exact census interface to the radius kernel

Let (mathcal X) be the retained owner set, so

\[
 |mathcal X|=W-E.                                     \tag{5.1}
\]

To turn Theorem 3.1 into a radius-resolved strip kernel, it is enough to
choose nested subsets

\[
 mathcal X=mathcal X_0\supseteqmathcal X_1
 \supseteq\cdots\supseteqmathcal X_H                \tag{5.2}
\]

with

\[
 |mathcal X_q|=N_q+e_q,qquad
 sum_{q=0}^H|e_q|=o(W),                               \tag{5.3}
\]

such that the two maps (4.1), restricted to (mathcal X_q), miss only
(o(W)) targets in aggregate over (q\le H).  Packetwise injectivity is
already exact; only cross-packet collisions enter this selection.

If such subsets exist, define

\[
 \bar\rho(X)=\max\{q:X\in\mathcal X_q\}.              \tag{5.4}
\]

The forced exact radius multiplicities are

\[
 N_d-N_{d+1}quad(d<H),qquad N_H,                    \tag{5.5}
\]

and rounding them to multiples of (2h) loses at most

\[
 O(hH)\text{ owners and }O(hH^2)=o(W)\text{ flags}.   \tag{5.6}
\]

Thus no owner supply, local order, physical-cycle, internal collision, radius
census, or divisibility problem remains in this explicit construction.

## 6. The finite local recursion identity still missing

The surviving statement is a cross-packet nested-transversal identity:

> In the first-eligible (B_4) packet factor, choose the nested subsets
> (5.2) so that their lower and upper physical shadow maps have aggregate
> missing mass (o(W)) through (q\le H).

Equivalently, orient/recouple the local (B_4) seeds by bounded
eight-coordinate rectangle associators so that every physical target is
assigned to one compatible packet start, with only (o(W)) aggregate
failures, while the assignments are nested in (q).

This is now a finite local recursion problem over the explicit alphabet

\[
 {14,12,23,34}                                      \tag{6.1}
\]

and the bounded rectangle associator.  A tensor solution of that identity
would prove the radius-resolved kernel and SCI.  Random independent packet
orientations are not enough: they retain the critical-load Poisson hole
fraction at shallow depths.  No proof of the cross-packet identity is given
here.

## 7. Every band target has a packet-local candidate, up to exponential error

Although simultaneous selection remains open, there is no outer **support**
deficit.  The first-eligible rule supplies a packet-local geodesic candidate
for almost every physical target.

For a lower target (S) and a four-block (B_i), call its local state

* type (A) when (S\cap B_i\in\mathcal A);
* type (L) when (|S\cap B_i|=1).

Read the blocks from left to right, retaining only types (A,L), and stop
after the first (r) retained blocks.  Say that (S) is lower-good at depth
(q) if this prefix contains at least (q) type-(L) blocks.

For each singleton (s\subset B_i), the local list (1.2) has a unique
oriented edge start (x_s\in\mathcal A) whose intersection with its
successor is (s).  On (q) chosen type-(L) blocks replace (s) by
(x_s), leaving every other block unchanged.  The resulting set (X) has
size (m), and the chosen (q) blocks lie among its first (r) eligible
blocks.  Moving once in each of them gives a geodesic (q)-path with

\[
 \bigcap_{j=0}^{q}X_j=S.                               \tag{7.1}
\]

Complete its (q) distinct cube directions to an ordering of all (h=2r)
packet directions and repeat that order.  This embeds the path in a physical
(C_{2h}) from the full strip catalogue.

For an upper target (T), use types (A) and

\[
 U:\quad |T\cap B_i|=3.                                \tag{7.2}
\]

The injective upper list (1.3) gives a unique local start contained in each
triple.  Replacing (q) triples by those starts produces a middle owner and
a geodesic path whose union is (T).

### Theorem 7.1 (exponentially complete candidate support)

Uniformly for (1\le q\le H=o(r)), all but

\[
 e^{-\Omega(r)}N_q                                    \tag{7.3}
\]

targets in each signed depth-(q) layer occur as a consecutive shadow of a
physical (C_{2h}) lying wholly in one retained first-eligible packet.
Consequently the aggregate candidate-support leave through (H) is (o(W)).

#### Proof

Work first under independent (1/2)-bits.  In a block,

\[
 \Pr(A)=\frac14,qquad \Pr(L)=\frac14                 \tag{7.4}
\]

for the lower problem, while (Pr(A)=Pr(U)=1/4) for the upper problem.
Conditional on a block being in the relevant two-type union, its two types
are equiprobable.  Hence among the first (r) union blocks, the number of
liftable (L)'s (or (U)'s) is binomial (operatorname {Bin}(r,1/2)).
Since (q=o(r)), Chernoff gives probability (e^{-\Omega(r)}) that it is
less than (q).  Having fewer than (r) union blocks at all has probability
(e^{-\Omega(m)}).

Conditioning the total set size to be (m-q) or (m+q) costs the reciprocal
of

\[
 2^{-2m}N_q
 =m^{-1/2}\exp\!\left(-O(q^2/m)\right).              \tag{7.5}
\]

For (q\le H=O(\sqrt{m\log m})), this reciprocal is polynomial in (m),
which is absorbed by (e^{-\Omega(r)}).  The explicit lifting above then
gives (7.1) and its upper analogue.  Finally

\[
 H e^{-\Omega(r)}W=o(W).
\]

\(\square\)

Thus the remaining cross-packet theorem is not a question of whether a
target has a compatible physical strip.  It is the integral simultaneous
choice problem: select only (W/(2h)+o(W/h)) whole strips so that these
abundant candidates are used with near-unit middle ownership and nested
all-depth coverage.

## 8. RETRACTED: side-size imbalance is not a coverage obstruction

> **Audit correction (2026-07-26).** The claim formerly labelled
> Theorem 8.1 is false as a coverage statement. A selected window is an
> edge of the lower/upper context graph, but the selected windows need not
> form a matching in that graph. Several windows may repeat one lower
> target while covering different upper targets, or conversely. Therefore
> unequal shore cardinalities do **not** imply that their absolute
> difference remains uncovered. An occurrence-capacity or degree theorem
> would be needed in addition, and none is proved here.
>
> The enumeration below is retained only as an audit of context-shore
> sizes. Formula (8.3) is **not** a lower bound on missing targets, and all
> purported consequences in Section 9 are retracted.

The candidate theorem does not mean that an order choice inside the fixed
four-block partition can solve the band.  There is an exact component
invariant, and at (q=\Theta(\sqrt m)) it has a linear two-sided deficit.

Assume for clarity that (2m=4b).  For a target (S), record in each
four-block its local rank.  On an odd-rank block give a singleton (s) and
the triple appearing opposite it in (1.2)--(1.3) the same label.  Thus the
local edge bijection is

\[
 1\leftrightarrow124,quad
 2\leftrightarrow123,quad
 3\leftrightarrow234,quad
 4\leftrightarrow134.                                  \tag{8.1}
\]

Consider any (q)-window which uses (q) distinct four-blocks once each.
Its lower and upper targets have identical

* sets of local-rank (0,2,4) blocks;
* exact local states in every rank-two block;
* set (J) of odd-rank blocks;
* label vector in ([4]^J).

It changes exactly (q) positions of (J) from rank one to rank three.
Fix all the displayed invariant data, put (s=|J|), and let (k) be the
number of rank-three blocks in the lower layer.  The targets in this
component are indexed by

\[
 \binom{J}{k}\quad\text{below},qquad
 \binom{J}{k+q}\quad\text{above},                     \tag{8.2}
\]

and every admissible window gives an inclusion (K\subset K') between
these two levels.

### Invalid former claim 8.1 (not a coverage deficiency)

The following expression records context-shore size differences, but it is
**not** a lower bound on the number of uncovered targets:

\[
 \boxed{
 D_{m,q}^{(4)}=
 \sum_{\mathfrak c}
 \left|\binom{s(\mathfrak c)}{k(\mathfrak c)}
       -\binom{s(\mathfrak c)}{k(\mathfrak c)+q}\right|,} \tag{8.3}
\]

where (mathfrak c) ranges over the fixed context data above, with the
corresponding multiplicity from its rank-two local states and odd labels.

For every fixed (c>0), if (q=\lfloor c\sqrt m\rfloor), then

\[
 D_{m,q}^{(4)}\ge(\delta_4(c)+o(1))W                 \tag{8.4}
\]

for some (delta_4(c)>0).

#### Audit of the former proof

Inside one context, a selected window is an edge of the inclusion graph
between the two levels in (8.2). The formerly asserted next step was that
at least the absolute difference of the two shore sizes is uncovered.
That inference would require selected windows to be a matching on target
vertices. They are not: an edge cover may reuse a target on the smaller
shore while covering several targets on the larger shore. Thus (8.3) does
not follow as a missing-target bound.

For (8.4), choose a uniform lower target of rank (m-q=2b-q).  Let (n_j)
be its number of blocks of local rank (j).  The rank identity is

\[
 n_1-n_3=q+2(n_4-n_0).                                \tag{8.5}
\]

The conditioned block census has the usual multivariate local central-limit
law.  Uniformly for (q=c\sqrt m+O(1)), a positive constant fraction of all
lower targets satisfy

\[
 s=n_1+n_3=(1+o(1))\frac m4,qquad
 n_4-n_0=-\frac q4+O(\varepsilon\sqrt m),             \tag{8.6}
\]

where (\varepsilon>0) is fixed sufficiently small.  (Equivalently, use
independent Bernoulli bits with
(p=1/2-q/(2m)), apply the multivariate de Moivre--Laplace theorem to the
five block ranks, and condition their total.)

Equations (8.5)--(8.6) give

\[
 k=\frac s2-\frac q4+O(\varepsilon\sqrt m),qquad
 k+q=\frac s2+\frac{3q}4+O(\varepsilon\sqrt m).       \tag{8.7}
\]

Stirling's formula in the central binomial window yields

\[
 \frac{\binom{s}{k+q}}{\binom{s}{k}}
 =\exp(-4c^2+O(\varepsilon)+o(1)).                    \tag{8.8}
\]

Choose (\varepsilon) so the right side is bounded away from one. On a
positive-mass family of contexts, (8.3) is therefore a fixed positive
fraction of the lower side. This proves only the shore-size statement
(8.4), not a coverage deficit. \(\square\)

The harmless remainder when (4\nmid2m) changes only (O(1)) coordinates
and does not affect (8.4).

### No coverage consequence

The explicit first-eligible factor still solves the middle layer and every
intrapacket geometry, but this cardinality calculation does not decide
whether direction orders confined to a fixed four-block partition can
satisfy SCI. That question requires an occurrence-capacity theorem for the
context graph.

## 9. RETRACTED: no transition-density lower bound follows

> Every asserted lower bound in this section depended on the invalid
> coverage interpretation of (8.3). The definitions and elementary
> incidence count (9.5) are harmless, but Theorem 9.1, Corollary 9.2, and
> the claimed \(\Omega(W/\sqrt m)\) bound are unsupported and must not be
> used.

The following invalid argument is retained only so its dependency is
visible. Fix the four-block partition. For a physical strip (C)
and a starting position (t), call its signed depth-(q) window **native** if
its (q) successive middle moves change (q) distinct four-blocks, once each,
through the local four-cycle (1.1).  Every native window obeys all the
context invariants in Section 8.  Let

\[
 B_q(\mathcal F)=
 \#\{(C,t):C\in\mathcal F,\text{ the depth-}(q)
                 \text{ window at }t\text{ is not native}\}.             \tag{9.1}
\]

### Invalid former Theorem 9.1

The formerly asserted inequality was

\[
 \boxed{
 M_q^-(\mathcal F)+M_q^+(\mathcal F)
 \ge D_{m,q}^{(4)}-2B_q(\mathcal F).}                  \tag{9.2}
\]

Consequently, for every compact interval
(0<a<b<\infty) there is (\delta=\delta(a,b)>0) such that,
uniformly for

\[
 a\sqrt m\le q\le b\sqrt m,
\]

\[
 M_q^-+M_q^+\ge (\delta-o(1))W-2B_q.                 \tag{9.3}
\]

#### Retraction

The first sentence of the old proof invoked the false coverage
interpretation of (8.3). Native windows may cover both unequal shores by
reusing targets on the smaller shore. Hence neither (9.2) nor (9.3) is
proved.

The only valid elementary count in this section is the following. For each
strip (C), suppose
one marks a set (E_{\rm rec}(C)) of transition positions such that every
depth-(q) window avoiding the marked positions is native.  Put

\[
 \mathcal T(\mathcal F)=\sum_{C\in\mathcal F}|E_{\rm rec}(C)|.            \tag{9.4}
\]

Since a marked transition lies in exactly (q) cyclic depth-(q) windows,

\[
 B_q(\mathcal F)\le q\,\mathcal T(\mathcal F).        \tag{9.5}
\]

Here a transition must be marked not only when it directly mixes two fixed
blocks, but also whenever its removal is needed to ensure that an unmarked
(q)-window uses distinct blocks.  Thus (9.5) applies to arbitrary local
associators once all of their affected transition sites are marked.

### Invalid former Corollary 9.2

Assume

\[
 |\mathcal F|=\frac{W}{2h}+o(W/h)                    \tag{9.6}
\]

and the aggregate signed shadow leave on
(a\sqrt m\le q\le b\sqrt m) is (o(W)).  Then

\[
 \boxed{
 \mathcal T(\mathcal F)=\Omega\!\left(\frac{W}{\sqrt m}\right),
 \qquad
 \frac{\mathcal T(\mathcal F)}{|\mathcal F|}
   =\Omega\!\left(\frac{h}{\sqrt m}\right).}         \tag{9.7}
\]

#### Retraction

The summation below used invalid inequality (9.3):

\[
 \sum_q(M_q^-+M_q^+)
 \ge \Theta(W\sqrt m)-O\!\left(\mathcal T
                      \sum_{q\asymp\sqrt m}q\right)
 =\Theta(W\sqrt m)-O(m\mathcal T).                  \tag{9.8}
\]

It yields no conclusion about (\mathcal T).

No lower bound on affected sites per strip is presently established by
this argument. Dense recoupling remains a valid construction option, but
is not known to be necessary.

## 10. Corrected occurrence-capacity theorem

The missing ingredient in Sections 8--9 is the global budget of window
occurrences.  Once that budget is included, a coarser fixed-block invariant
does give a valid obstruction.

Assume first that (m) is even and partition the (2m) coordinates into
(b=m/2) fixed four-blocks.  For every target (S), put

\[
 Z(S)=\#\{i:|S\cap B_i|=4\}
      -\#\{i:|S\cap B_i|=0\}.                         \tag{10.1}
\]

Every native window from (9.1) preserves (Z): an active local four-cycle
has lower rank one and upper rank three, while every untouched block has
the same restriction on both signs. More generally, define the exact
escape count

\[
 B_q^Z=\#\{(C,t):Z(L^C_{t,q})\ne Z(U^C_{t,q})\}.       \tag{10.2a}
\]

A window can be non-native in the older label sense and still preserve
(Z); such a window supplies no escape from the invariant and is not counted
by (B_q^Z). Let

\[
 L_z=\#\{S\in\tbinom{[2m]}{m-q}:Z(S)=z\},\qquad
 U_z=\#\{S\in\tbinom{[2m]}{m+q}:Z(S)=z\},              \tag{10.2}
\]

and

\[
 D^Z_{m,q}=\sum_z|L_z-U_z|.                            \tag{10.3}
\]

Thus

\[
 \sum_zL_z=\sum_zU_z=N_q,qquad
 \sum_z\max(L_z,U_z)=N_q+\frac12D^Z_{m,q}.            \tag{10.4}
\]

### Theorem 10.1 (valid edge-cover capacity bound)

Let (\mathcal F) be a family of owner-disjoint physical (C_{2h})'s,
fix (1\le q<h), and let

\[
 R=2h|\mathcal F|\le W                                      \tag{10.5}
\]

be its number of directed middle starts. Then

\[
 \boxed{
 M_q^-(\mathcal F)+M_q^+(\mathcal F)
 \ge N_q+\frac12D^Z_{m,q}-R-B_q^Z.}                  \tag{10.6}
\]

In particular, the right side may be replaced by
(N_q+D^Z_{m,q}/2-W-B_q^Z).

#### Proof

For every (z), let (e_z) be the number of (Z)-preserving occurrences in
class (z). Then

\[
                         \sum_ze_z=R-B_q^Z.            \tag{10.7}
\]

Using only those occurrences, at most (e_z) distinct lower targets and at
most (e_z) distinct upper targets can be covered in class (z).  Hence the
native missing count there is at least

\[
 (L_z-e_z)_+ +(U_z-e_z)_+
 \ge \max(L_z,U_z)-e_z.                               \tag{10.8}
\]

Restoring one (Z)-breaking occurrence can remove at most one lower and one
upper hole.  Summing (10.8), using (10.4)--(10.7), and subtracting
(2B_q^Z) gives

\[
 N_q+\frac12D^Z_{m,q}-(R-B_q^Z)-2B_q^Z,
\]

which is (10.6). \(\square\)

This is the precise correction to the false shore-size argument: the
absolute context imbalance matters only after it is compared with the
finite occurrence budget (R).

### Theorem 10.2 (Gaussian evaluation of the invariant)

Let (q=\lfloor c\sqrt m\rfloor) for fixed (c>0), and write (\Phi) for the
standard normal distribution function.  Then

\[
 \boxed{
 \frac{D^Z_{m,q}}{2N_q}
 \longrightarrow
 \tau(c):=2\Phi(\sqrt2c)-1.}                          \tag{10.9}
\]

Moreover,

\[
                         \frac{N_q}{W}\longrightarrow e^{-c^2}. \tag{10.10}
\]

#### Proof

Under independent fair bits in one four-block, let (Y) be the local rank
and let

\[
 V=\mathbf1_{\{Y=4\}}-\mathbf1_{\{Y=0\}}.
\]

At (p=1/2),

\[
 \mathbb EY=2,quad \operatorname {Var}Y=1,quad
 \mathbb EV=0,quad \operatorname {Var}V=\frac18,quad
 \operatorname {Cov}(Y,V)=\frac14.                  \tag{10.11}
\]

A uniform lower target is the product measure conditioned on

\[
                         \sum_{i=1}^bY_i=2b-q.         \tag{10.12}
\]

The bivariate lattice local central-limit theorem, or equivalently
exponential tilting followed by conditional de Moivre--Laplace, gives the
uniform lattice approximation

\[
 \frac{Z+q/4}{\sqrt{m/32}}
 \ \Longrightarrow\ N(0,1)                           \tag{10.13}
\]

in the sense that the conditional law is total-variation close to the
corresponding discretized normal law. Indeed, the conditional variance per
block is

\[
 \operatorname {Var}V-
 \frac{\operatorname {Cov}(Y,V)^2}{\operatorname {Var}Y}
 =\frac1{16},                                         \tag{10.14}
\]

and there are (b=m/2) blocks.  Complementation maps an upper target to a
lower target and sends (Z) to (-Z), so the upper law has mean (+q/4) and
the same asymptotic variance.  The total-variation distance between
(N(-\sqrt2c,1)) and (N(+\sqrt2c,1)) is
(2\Phi(\sqrt2c)-1).  Since total variation equals
(D^Z_{m,q}/(2N_q)), this proves (10.9).

Finally the central-binomial local limit gives

\[
 \log\frac W{N_q}=\frac{q^2}{m}+o(1)=c^2+o(1),
\]

which is (10.10). \(\square\)

When (m) is odd, use ((m-1)/2) four-blocks and one residual two-block,
and let (Z) ignore the residual block. Conditional on its rank
(j\in\{0,1,2\}), the four-block total in (10.12) changes by only (O(1)).
The same conditional lattice CLT, followed by the three-term mixture over
(j), has the identical limiting means, variance, and total-variation
constant. A transition confined to the residual pair does not change (Z).
Thus Theorems 10.1--10.2 and their corollaries hold for odd (m) as well,
with the same asymptotic constants.

Define

\[
 \gamma(c)=e^{-c^2}(1+\tau(c))-1
           =2e^{-c^2}\Phi(\sqrt2c)-1.                \tag{10.15}
\]

Since

\[
                         \gamma(0)=0,qquad
 \gamma'(0)=\frac2{\sqrt\pi}>0,                      \tag{10.16}
\]

there is an absolute (c_0>0) such that (\gamma(c)>0) for every
(0<c<c_0).

### Corollary 10.3 (corrected phase-density necessity)

Fix (c\in(0,c_0)), let (q=\lfloor c\sqrt m\rfloor), and assume
(q<h). If

\[
 R=W-o(W),\qquad M_q^-+M_q^+=o(W),                   \tag{10.17}
\]

then

\[
                         B_q^Z\ge(\gamma(c)-o(1))W.   \tag{10.18}
\]

If transition sets (E_{\rm rec}(C)) are marked so that every
(Z)-breaking depth-(q) window contains a mark, then the same cyclic
incidence count as (9.5) gives (B_q^Z\le q\mathcal T), and

\[
 \boxed{
 \mathcal T=\Omega\!\left(\frac W{\sqrt m}\right).}  \tag{10.19}
\]

When (|\mathcal F|=W/(2h)+o(W/h)), this is

\[
 \boxed{
 \frac{\mathcal T}{|\mathcal F|}
 =\Omega\!\left(\frac h{\sqrt m}\right)}             \tag{10.20}
\]

marked transition sites per strip on average.

Unlike the retracted argument, Corollary 10.3 uses an actual occurrence
capacity: a (Z)-preserving component with shores (L_z,U_z) needs at least
(\max(L_z,U_z)) window occurrences to cover both shores.  The excess over
the global budget (W) is positive at sufficiently small Gaussian depth,
which is exactly what forces (10.18).

## 11. A stronger bounded-Lipschitz transport requirement

Counting merely whether (Z) changes loses its magnitude.  The full
occurrence ledger forces Gaussian-scale transport.

Put

\[
 \sigma_m=\sqrt{m/32},\qquad
 \psi(x)=\max(-1,\min(1,x)),\qquad
 f_m(z)=\psi(z/\sigma_m).                              \tag{11.1}
\]

Thus (|f_m|\le1) and (f_m) is (1/\sigma_m)-Lipschitz.  For a standard
normal (G), define

\[
 \Delta(c)=
 \mathbb E\psi(G+\sqrt2c)-
 \mathbb E\psi(G-\sqrt2c)>0.                          \tag{11.2}
\]

The strict inequality follows because (\psi) is nonconstant and
increasing.  Moreover

\[
 \Delta(0)=0,qquad
 \Delta'(0)=2\sqrt2\,\Pr(|G|<1)>0.                    \tag{11.3}
\]

### Lemma 11.1 (multiset replacement cost)

Let a multiset of (R) occurrences take values in a target set of size
(N), and suppose it covers all but (M) targets.  For every (|f|\le1),
provided (R\ge N-M),

\[
 \left|\sum_{\rm occurrences}f-sum_{\rm targets}f\right|
 \le R-N+2M.                                         \tag{11.4}
\]

#### Proof

Delete the (M) missing targets from the once-each target list, at cost at
most (M).  The remaining list has (N-M) entries.  The occurrence multiset
is obtained by adding (R-N+M) repetitions, at cost at most that number.
The sum is (R-N+2M). \(\square\)

### Theorem 11.2 (Gaussian (Z)-transport lower bound)

There is an absolute (c_1>0) such that the following holds.  Fix
(c\in(0,c_1)), put (q=\lfloor c\sqrt m\rfloor<h), and let
(\mathcal F) be an owner-disjoint physical strip family with

\[
 R=2h|\mathcal F|=W-o(W),\qquad
 M_q^-+M_q^+=o(W).                                   \tag{11.5}
\]

Then its directed starts satisfy

\[
 \boxed{
 \sum_{(C,t)}
 \left|Z(U^C_{t,q})-Z(L^C_{t,q})\right|
 =\Omega(W\sqrt m).}                                 \tag{11.6}
\]

#### Proof

The lattice CLT in Theorem 10.2 and bounded convergence give

\[
 \sum_{U\in\binom{[2m]}{m+q}}f_m(Z(U))
 -\sum_{L\in\binom{[2m]}{m-q}}f_m(Z(L))
 =(\Delta(c)+o(1))N_q.                               \tag{11.7}
\]

Apply Lemma 11.1 separately to the lower and upper occurrence multisets.
Writing (M_q=M_q^-+M_q^+), their (f_m)-sum difference is at least

\[
 (\Delta(c)+o(1))N_q-2(R-N_q)-2M_q.                  \tag{11.8}
\]

Since (R\le W) and (N_q/W\to e^{-c^2}), the right side divided by (W)
is at least

\[
 \kappa(c)+o(1),\qquad
 \kappa(c):=e^{-c^2}\Delta(c)-2(1-e^{-c^2}).         \tag{11.9}
\]

Equations (11.3) and (\frac d{dc}(1-e^{-c^2})|_{c=0}=0) show that
(\kappa(c)>0) for every sufficiently small fixed (c>0).  Finally,

\[
 \begin{aligned}
 \kappa(c)W+o(W)
 &\le\left|\sum_{(C,t)}
       \big(f_m(Z(U^C_{t,q}))-f_m(Z(L^C_{t,q}))\big)\right|\\
 &\le\frac1{\sigma_m}\sum_{(C,t)}
       |Z(U^C_{t,q})-Z(L^C_{t,q})|,
 \end{aligned}                                       \tag{11.10}
\]

which proves (11.6). \(\square\)

### Corollary 11.3 (paired-direction requirement)

Suppose every strip lies in a tensor of active rank-two four-block cells.
For a start (C,t), let (d_{C,t,q}) be the number of local cells for which
both active directions occur in its (q)-window.  Then

\[
 Z(U^C_{t,q})-Z(L^C_{t,q})=2d_{C,t,q},                \tag{11.11}
\]

and every (o(W))-hole factor must satisfy

\[
 \boxed{
 \sum_{(C,t)}d_{C,t,q}=\Omega(W\sqrt m),\qquad
 \frac1R\sum_{(C,t)}d_{C,t,q}=\Omega(\sqrt m).}      \tag{11.12}
\]

Thus a typical Gaussian window must complete a constant-order fraction of
its (q=\Theta(\sqrt m)) directions into local pairs.

For comparison, if the (h=2r) directions are uniformly permuted relative
to the (r) local pairs, the expected number completed by one (q)-window is

\[
 r\frac{q(q-1)}{h(h-1)}
 =\frac{q(q-1)}{2(h-1)}
 =\Theta(m/h)=o(\sqrt m)                              \tag{11.13}
\]

whenever (\sqrt m\ll h=o(m)).  Hence random affine dispersion, although
it makes almost every window change (Z) at least once, is quantitatively
insufficient.  The required cycle factor must be **pair-clustered**:
local direction partners must co-occur in typical Gaussian windows at
rate (\Theta(q)), while the packet-wide two-sided trace maps remain
injective.
