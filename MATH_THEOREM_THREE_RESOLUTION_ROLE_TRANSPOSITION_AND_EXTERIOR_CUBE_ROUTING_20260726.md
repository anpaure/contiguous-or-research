# The three-resolution role transposition and exterior-cube routing theorem

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There is a genuine compound escape for **ordered compiler roles** from the
one-slab state-compatibility obstruction, but its scope is precise.

Inside one literal `Q_{R+1}` slab, the three successive resolutions

\[
                    \mathcal P_e\longrightarrow\mathcal P_i
                    \longrightarrow\mathcal P_j
                    \longrightarrow\mathcal P_e                 \tag{0.1}
\]

return the two original owner packets exactly and transpose the two ordered
active roles occupied initially by the physical directions `i,j`.  Every
successive old/new owner-transfer matrix is the balanced splitter
`(1/2)J_2`, whereas the cumulative owner-transfer matrix is `I_2`.  Thus
the correlations between the two half-packet splittings are essential; the
three matrices may not be multiplied as independent Markov kernels.

Apply this closed gadget on edges of the exterior packet cube of a parent
`Q_S`.  A gadget labelled by a physical transposition applies that
transposition to the compiler-coordinate identifications at both endpoints.
For any fixed transposition, every even set of endpoint packets can be
addressed exactly by a mod-two `T`-join.  For exterior dimension at least
two, a full assignment is reachable exactly when the product of its packet
signs is positive; otherwise one reservoir packet absorbs the sharp parity
defect.  Combining this with a fixed triangular adjacent-transposition
network gives the following result.

> **Exterior-cube order-routing theorem.**  Let a parent `Q_S` be partitioned
> into its parallel `Q_R` packets, and put `k=S-R`.  Given an arbitrary
> desired physical coordinate conjugate of one fixed compiler on every packet
> except one reservoir packet, a sequence of closed three-resolution gadgets
> realizes all the desired conjugates.  The final owner partition is exactly
> the initial partition, every intermediate resolution is integral and legal,
> and no owner is lost.

If the reservoir must also realize a prescribed rooted table, discard it.
This costs exactly `2^R` owners per `Q_S`, a fraction `2^{-k}`.  For a union
of such parents, the resulting missing-shadow charge through depth `H` is at
most

\[
                      2H E_{\rm res},\qquad
              E_{\rm res}\le 2^{-k_{\min}}G.          \tag{0.2}
\]

Consequently it is `o(W)` whenever

\[
                       H2^{-k_{\min}}=o(1)             \tag{0.3}
\]

and the preceding owner leave already has `H E_0=o(W)`.

Coordinate conjugation transports the entire compiler cycle factor, so its
rooted successor permutation, nesting, and all successor-cocycle identities
remain exact at every depth.  The theorem therefore removes the adaptive
switching obstruction for packetwise compiler-conjugate tables.

It does **not** prove that a general balanced nested flag table is
packetwise compiler-conjugate, nor does it change packet membership.  That
cross-parent grouping/selection statement remains the exact unsolved gate.

## 1. Ordered packet frames

Let `D` be a set of `R` mutually disjoint physical pair-directions, let
`E` be a disjoint set of `k` further pair-directions, and put

\[
                         S=R+k.                         \tag{1.1}
\]

Inside the coordinate cube `Q_{D\cup E}=Q_S`, use the parallel packet
partition

\[
 P_z=\{x\in Q_{D\cup E}:x|_E=z\},
       \qquad z\in\{0,1\}^E.                           \tag{1.2}
\]

Every `P_z` is a literal `Q_R` with active physical frame `D`.  There are

\[
                         P=2^k                         \tag{1.3}
\]

packets.  Their adjacency graph under changing one exterior bit is the
connected cube `Q_k`.

An **ordered frame** on a packet is a bijection from the abstract compiler
coordinates `[R]` to `D`.  Equivalently, after fixing one reference
identification, it is an element of `S_R`.

During a compound trade the ordered roles may be carried as owner metadata.
An intermediate packet may then consist of two half-packets whose carried
role identifications differ.  This is a **mixed-frame intermediate state**,
not a compiler packet, but it is still a legal owner packet because slab
legality uses only its common physical active frame.  No intermediate trace
is needed for this metadata implementation.

There is also an exact-factor implementation.  At each arrow one conjugates
the complete current factor by the physical transposition of the old and new
frozen coordinates.  This gives an exact compiler factor, successor, and
rooted cocycle at every intermediate state.  It rewrites flags covariantly;
it does not transport a fixed owner-attached table verbatim.  The two
implementations have the same closed role holonomy.

We use the following natural role-transport rule under a slab trade.  If
the old partition freezes `c`, the new partition freezes the active
coordinate `d`, and hence `c` becomes active, then `c` inherits the ordered
role vacated by `d`; every other active coordinate keeps its role.  This
rule is the specified ownerwise connection used below.  It is deterministic
once the old ordered frame has been fixed; no uniqueness among all possible
metadata transports is claimed.

## 2. The smallest nontrivial closed compound

Fix one exterior direction `e\in E` and an edge `zz^e` of the packet cube.
The union of its endpoint packets is the slab

\[
 \mathcal S_z=P_z\cup P_{z^e}\cong Q_{D\cup\{e\}},     \tag{2.1}
\]

with every other exterior coordinate fixed.  For `c\in D\cup\{e\}` let

\[
 \mathcal P_c=\{P^c_0,P^c_1\},\qquad
 P^c_a=\{x\in\mathcal S_z:x_c=a\}.                    \tag{2.2}
\]

Thus `\mathcal P_e` is the original pair of packets.

Choose distinct `i,j\in D` and perform (0.1).

### Theorem 2.1 (exact three-resolution holonomy)

The compound (0.1) has the following properties.

1. For consecutive distinct frozen coordinates `c,d`,

   \[
                |P^c_a\cap P^d_b|=2^{R-1}
                \qquad(a,b\in\{0,1\}).                \tag{2.3}
   \]

   Hence every normalized one-step owner-transfer matrix is

   \[
                         {1\over2}
                  \begin{pmatrix}1&1\\1&1\end{pmatrix}.          \tag{2.4}
   \]

2. The cumulative initial/final transfer matrix is

   \[
              |P^e_a\cap P^e_b|=2^R\mathbf1_{a=b},     \tag{2.5}
   \]

   so the two original owner packets return exactly.

3. Under ordered role transport, the physical directions `i,j` exchange
   their roles and every direction in `D\setminus\{i,j\}` keeps its role.
   The same transposition occurs in both endpoint packets.

4. Under this vacated-role connection and without an extra port relabelling,
   three resolutions are minimal for a nonidentity closed role holonomy.

#### Proof

Equation (2.3) fixes two distinct coordinates of `Q_{R+1}` and leaves
`R-1` coordinates free.  Equation (2.5) is immediate because the initial
and final partitions are literally the same partition.

Let the initial roles occupied by `i,j` be `\alpha,\beta`.  In the first
trade, `e` enters the active frame and inherits role `\alpha` from `i`.
In the second, `i` enters and inherits role `\beta` from `j`.  In the
third, `j` enters and inherits role `\alpha` from `e`.  Thus the final
role occupants are

\[
                        \alpha:j,\qquad \beta:i,       \tag{2.6}
\]

as claimed.  This argument does not use the value of `x_e`, so the two
endpoint packets receive the same transposition.

The two endpoint packets need not start with the same ordered
identification.  If their initial identifications are `\rho_0,\rho_1`, the
ownerwise calculation gives final identifications `\tau\rho_0,\tau\rho_1`,
where `\tau=(ij)`.  The intermediate `i`- and `j`-facets can then be
mixed-frame packets, as allowed in Section 1; their physical active frame is
still common and every slab resolution remains literal.

One resolution cannot return to the original frozen coordinate.  A
two-resolution return has the form

\[
                        \mathcal P_e\to\mathcal P_i
                        \to\mathcal P_e.
\]

The role of `i` moves to `e` and then back to `i`, so its holonomy is the
identity.  Hence (0.1) is smallest. `\square`

For an individual owner `x`, the successive packet labels are exactly

\[
                       x_e,\quad x_i,\quad x_j,\quad x_e.           \tag{2.7}
\]

This is the exact half-packet trace through the gadget.  Formula (2.7)
also explains why multiplying the three matrices (2.4) gives the wrong
cumulative answer: the same owner bits are retained and reused at the later
seams.

### Proposition 2.1A (complete owner-history tensor)

For `a,b,c,d\in\{0,1\}`,

\[
 \left|P_a^e\cap P_b^i\cap P_c^j\cap P_d^e\right|
       =2^{R-2}\mathbf1_{\{d=a\}}.                 \tag{2.7a}
\]

When `d=a`, the conditions fix the three distinct coordinates `e,i,j`
of `Q_{R+1}` and leave `R-2` coordinates free.  When `d\ne a`, the two
conditions on `e` are inconsistent.  Thus the endpoint identity matrix is
carried by correlations in the full history tensor, not by the product of
the three coarse splitter matrices.

### Proposition 2.1B (exact-factor lift at every state)

Let `\mathcal F` be any exact canonically oriented cycle factor subordinate
to `\mathcal P_e`, and let `s_{uv}` be the physical coordinate
transposition exchanging axes `u,v`.  Define

\[
 \mathcal F_1=s_{ei}\mathcal F s_{ei}^{-1},\qquad
 \mathcal F_2=s_{ij}\mathcal F_1s_{ij}^{-1},\qquad
 \mathcal F_3=s_{je}\mathcal F_2s_{je}^{-1}.        \tag{2.7b}
\]

Then `\mathcal F_t` is an exact factor subordinate to the `t`th
packetization in (0.1), and

\[
                    s_{je}s_{ij}s_{ei}=s_{ij}.      \tag{2.7c}
\]

Hence the terminal factor is the active-coordinate conjugate
`s_{ij}\mathcal F s_{ij}^{-1}` on the original packets.  Indeed, a
coordinate permutation maps every literal isometric cycle bijectively to a
literal isometric cycle and maps the two facets of one resolution to those
of the next.  Identity (2.7c) fixes `e` and interchanges `i,j`.

### Corollary 2.2 (a general single-slab loop)

A loop

\[
 \mathcal P_e\to\mathcal P_{i_1}\to\cdots
       \to\mathcal P_{i_t}\to\mathcal P_e             \tag{2.8}
\]

transports the ordered roles by one permutation of
`\{i_1,\ldots,i_t\}` and applies that same permutation to both endpoint
packets.  In particular no bit-blind closed loop in one slab can apply a
nontrivial role permutation to only one of its two original facets.

#### Proof

At every step the newly active coordinate inherits the role of the newly
frozen coordinate.  This rule depends only on the frozen-coordinate walk,
not on the value of the packet bit. `\square`

### Theorem 2.3 (path-independent owner-transfer matrix)

Let the same parent `Q_S` have an initial parallel `Q_R` foliation with
active frame `D` and a final parallel `Q_R` foliation with active frame
`D'`.  Put

\[
                    a=|D\setminus D'|=|D'\setminus D|.             \tag{2.9}
\]

After grouping packets by their common frozen word on
`[S]\setminus(D\cup D')`, the normalized initial/final owner-transfer
matrix is a direct sum of blocks

\[
                              2^{-a}J_{2^a}.            \tag{2.10}
\]

This matrix depends only on `D,D'`, not on the sequence of slab trades.
In particular, if `D=D'`, the final physical packet partition is exactly the
initial one; if `D\ne D'`, every initial packet is split equally among
`2^a` final packets.

More generally, for any two literal coordinate packets `P,Q` with active
frames `D,D'`, respectively,

\[
 |P\cap Q|\in\{0,2^{|D\cap D'|}\},                    \tag{2.11}
\]

with the nonzero case occurring exactly when their frozen assignments agree
on every coordinate frozen by both.

#### Proof

Fix the common frozen word outside `D\cup D'`.  An initial packet is then
indexed by its frozen word on `D'\setminus D`, while a final packet is
indexed by its frozen word on `D\setminus D'`.  Every pair of such words is
compatible, and their intersection leaves precisely the coordinates
`D\cap D'` free.  Its size is

\[
                         2^{|D\cap D'|}=2^{R-a}.
\]

Division by the packet size `2^R` gives (2.10).  The same compatibility
argument proves (2.11). `\square`

Thus no compound history can turn a genuine splitter into whole-packet
permutation transport.  The positive holonomy in Theorem 2.1 concerns
ordered compiler roles carried by half-packets; its literal owner-transfer
matrix remains the identity.

### Proposition 2.4 (the first four-resolution history tensor)

For distinct `i,j,k\in D`, the closed walk

\[
 \mathcal P_e\to\mathcal P_i\to\mathcal P_j
       \to\mathcal P_k\to\mathcal P_e                 \tag{2.12}
\]

has cumulative endpoint matrix `I_2` and ordered-role holonomy

\[
                              (i\ k\ j).                \tag{2.13}
\]

If `a_t` is the packet bit at the `t`th state of (2.12), its complete owner
history tensor is

\[
 \#\{x:x_e=a_0,x_i=a_1,x_j=a_2,x_k=a_3,x_e=a_4\}
       =2^{R-3}\mathbf1_{a_4=a_0}.                     \tag{2.14}
\]

#### Proof

The four specified coordinates are independent in `Q_{R+1}` and leave
`R-3` free coordinates; the first and last constraints address the same
coordinate.  This proves (2.14) and the endpoint claim.  Vacated-role
transport leaves the old roles of `i,j,k` occupied finally by `k,i,j`,
respectively, which is (2.13). `\square`

## 3. Exact trace effect and the rooted cocycle

Let `\mathcal C` be any exact cycle factor of the abstract `Q_R`.  Write
its directed successor as `F`, and write its abstract nested deletion and
addition flags as `\Delta_q(y),\Gamma_q(y)`.  Thus

\[
                    F^qy=y-\Delta_q(y)+\Gamma_q(y).    \tag{3.1}
\]

An ordered identification `\rho:[R]\to D` induces a physical cube
isomorphism `\widehat\rho` and hence the conjugate factor

\[
 F_\rho=\widehat\rho F\widehat\rho^{-1}.              \tag{3.2}
\]

Its rooted flags are exactly

\[
\begin{aligned}
 D_{q,\rho}(X)
   &=\widehat\rho\bigl(\Delta_q(\widehat\rho^{-1}X)\bigr),\\
 A_{q,\rho}(X)
   &=\widehat\rho\bigl(\Gamma_q(\widehat\rho^{-1}X)\bigr).
\end{aligned}                                          \tag{3.3}
\]

Here `\widehat\rho` permutes whole physical pair axes and fixes the frozen
core.

### Proposition 3.1 (all-depth cocycle preservation)

After a three-resolution role transposition `\tau=(ij)`, installing the
transported compiler changes `\rho` to `\tau\rho`.  Its exact trace table
is given by (3.3) with `\tau\rho`, and

\[
 F_{\tau\rho}^qX
   =X-D_{q,\tau\rho}(X)+A_{q,\tau\rho}(X)              \tag{3.4}
\]

for every depth for which the abstract compiler trace is defined.  In
particular its first-step map is a permutation, its flags are nested, and
all rooted successor-cocycle identities hold exactly.

#### Proof

Conjugate (3.1) by the cube isomorphism `\widehat{\tau\rho}`. `\square`

For a packet `P`, sign `\epsilon`, and depth `q`, let
`L_{P,q}^{\epsilon,\rho}(T)` be the number of rooted compiler occurrences
ending at the literal target `T`.  The same conjugation gives the exact
target-vector action

\[
 L_{P,q}^{\epsilon,\tau\rho}(T)
   =L_{P,q}^{\epsilon,\rho}(\widehat\tau^{-1}T).        \tag{3.5}
\]

Thus choosing the transported compiler conjugate changes the packet's
physical target image by a literal coordinate permutation, not by a
fractional averaging.  In particular
all within-packet trace multiplicities, including injectivity, are preserved.

This proposition is a construction of new cocycle-compatible flags, not a
repair of a fixed incompatible table.  A preassigned table survives the
gadget only if it equals the transported table (3.3).  In particular no
owner-preserving compound can repair a nonbijective preassigned first-step
map.

### Proposition 3.2 (literal rooted-table path erasure)

Attach to every physical owner `X` a preassigned literal rooted flag
`\mathcal T(X)`.  A sequence of slab re-resolutions changes only the packet
partition: it changes neither `X` nor `\mathcal T(X)`.  Consequently two
networks with the same final packet partition have exactly the same final
packetwise rooted tables.  A closed network has no literal trace effect at
all.

The role holonomy of Theorem 2.1 can matter only when the compiler
identification, and hence the rooted table itself, is selected jointly with
the final network.  It cannot route a fixed flag from one root to another or
turn a fixed non-compiler table into a compiler table.

#### Proof

A slab re-resolution replaces one partition of a fixed owner set by another
partition of that same set.  It contains no map `X\mapsto X'` and performs
no operation on an owner label.  Induction over the resolutions proves the
claim. `\square`

At depth one the obstruction is already complete: the two signed targets
`T_1(X)=X-D_1(X)` and `U_1(X)=X+A_1(X)` uniquely determine

\[
                 S(X)=T_1(X)\cup\bigl(U_1(X)\setminus X\bigr).    \tag{3.6}
\]

Hence a compound which literally preserves both preassigned depth-one
targets preserves the successor map itself.  No higher-layer associator can
repair its bijectivity while retaining those targets.  Moreover, if a
retained set `\mathcal G` is to carry an exact factor with the same two
depth-one targets, necessarily

\[
                              S(\mathcal G)=\mathcal G.             \tag{3.7}
\]

Thus `\mathcal G` must be a union of complete old successor cycles.  The
reservoir deletion in Theorem 6.1 is valid because its hypothesis is
stronger: every retained packet already carries a complete compiler factor.
Lower flags alone would not determine `S`; both signs are essential here.

## 4. Mod-two routing on the exterior cube

We first isolate the elementary graph fact used by the recursion.

### Lemma 4.1 (exact `T`-join in a connected graph)

Let `G_0=(V,E_0)` be connected.  For every even set `A\subseteq V`, there
is an edge set `J\subseteq E_0` whose set of odd-degree vertices is exactly
`A`.  One may choose `J` inside a fixed spanning tree, and then

\[
                            |J|\le |V|-1.              \tag{4.1}
\]

#### Proof

Root a spanning tree.  Include the edge joining a nonroot vertex `v` to its
parent precisely when the subtree rooted at `v` contains an odd number of
vertices of `A`.  At every nonroot vertex, the parity of its incident chosen
edges is its indicator in `A`.  The same then holds at the root because
`|A|` is even. `\square`

Fix a physical transposition `\tau=(ij)` of two active directions.  Run the
three-resolution gadget labelled `\tau` on every edge of a `T`-join `J` in
the exterior packet cube.  A packet at `v` receives `\tau^{\deg_J(v)}`.
Therefore it receives `\tau` exactly for `v\in A`.

The gadgets may be run sequentially.  If parallel bookkeeping is desired,
first group edges by their exterior direction.  Edges in one direction are
owner-disjoint, so one `T`-join requires at most `3k` partial resolution
layers.

## 5. Arbitrary compiler-conjugate routing with one reservoir

We need one elementary universal-word fact.  There is a fixed sequence

\[
                     \tau_1,\ldots,\tau_L,\qquad
                     L={R\choose2},                    \tag{5.1}
\]

of adjacent transpositions of the fixed physical labels in `D` such that
every element `\sigma\in S_R` has a representation

\[
                     \sigma=\tau_1^{a_1}\cdots
                              \tau_L^{a_L},\qquad
                     a_t\in\{0,1\}.                    \tag{5.2}
\]

To see this without any group-theoretic black box, take the triangular
insertion-sort comparator sequence

\[
 (1,2); (2,3),(1,2); \ldots;\
 (R-1,R),(R-2,R-1),\ldots,(1,2).                       \tag{5.3}
\]

It sorts every permutation when each comparator is used exactly when its two
current entries are inverted.  Reverse the sorting decisions and the
comparator order.  Starting from the identity, this realizes the original
permutation as a subword.  Relabelling the reversed sequence gives (5.1)--
(5.2).

### Theorem 5.1 (exterior-cube compiler-conjugate routing)

Let the parallel packets (1.2) fill one `Q_S`, and choose a reservoir vertex
`v_*\in Q_k`.  Prescribe an arbitrary desired ordered identification
`\rho_v` on every packet `P_v` with `v\ne v_*`.  Then closed
three-resolution gadgets produce these identifications exactly, with the
following ledger.

1. Every intermediate packetization is integral and owner-exact.
2. The final packetization is literally (1.2).
3. Every nonreservoir packet has its prescribed ordered identification.
4. The reservoir has some valid ordered identification, not prescribed in
   advance.
5. At most

   \[
                      L(2^k-1)                         \tag{5.4}
   \]

   three-resolution edge gadgets are used, hence at most

   \[
                      3L(2^k-1)                        \tag{5.5}
   \]

   individual slab re-resolutions.
6. The construction can be scheduled in at most `3kL` partial owner-
   disjoint layers.

#### Proof

Measure every desired ordered frame relative to one reference frame.  Use
(5.2) to choose bits `a_t(v)` for every `v\ne v_*`.  At time `t`, put

\[
 A_t^0=\{v\ne v_*:a_t(v)=1\}.                          \tag{5.6}
\]

If `|A_t^0|` is odd, add `v_*`; otherwise do not.  The resulting `A_t` is
even.  By Lemma 4.1 choose a `T`-join `J_t` in the exterior cube with odd
boundary `A_t`.  Process the time indices in the descending order
`t=L,L-1,\ldots,1`, running the `\tau_t` gadget on all edges of `J_t`.

For a fixed `t`, a packet receives `\tau_t` once modulo two exactly when it
lies in `A_t`.  The physical transposition `\tau_t` is the same on every
selected edge, so repeated incidences cancel before the next transposition
time.  Because role transport left-multiplies the ordered identification,
the descending time order gives exactly
`\tau_1^{a_1}\cdots\tau_L^{a_L}` from (5.2) at every nonreservoir packet.
The reservoir receives the
product determined by the parity corrections and is still a valid ordered
frame.

Lemma 4.1 gives at most `2^k-1` edge gadgets per time, proving (5.4)--(5.5).
Grouping selected cube edges by their `k` directions proves the partial-layer
bound.  Each edge gadget returns its two original packets by Theorem 2.1, so
the owner and final-partition claims follow. `\square`

### Proposition 5.2 (the exact parity obstruction for the edge-loop model)

Start with the same reference ordered frame on all `2^k` packets.  Any
network generated by closed single-edge loops has

\[
                 \prod_{v\in Q_k}\operatorname{sgn}(\rho_v)=+1.   \tag{5.7}
\]

Therefore a prescription containing an odd number of odd coordinate
conjugates cannot be realized on all packets by this generator set.  The
smallest example is two packets with a transposition prescribed on only one.

#### Proof

By Corollary 2.2, one closed edge loop applies one common permutation
`\pi` to its two endpoint frames.  It multiplies the product in (5.7) by
`\operatorname{sgn}(\pi)^2=1`.  Induct over the loops. `\square`

This proposition proves that the one-reservoir formulation of Theorem 5.1
is not merely a defect of the `T`-join proof.  It does not claim an
obstruction against a larger primitive which is not generated by closed
single-edge slab loops.

### Theorem 5.3 (sharper noncommutative tree recursion)

The conclusion of Theorem 5.1 can be obtained with at most

\[
                         (R-1)(2^k-1)                  \tag{5.8}
\]

three-resolution edge gadgets, hence at most

\[
                         3(R-1)(2^k-1)                 \tag{5.9}
\]

individual slab re-resolutions.  This recursion does not assume that the
desired packet permutations commute.

#### Proof

Choose a spanning tree of `Q_k` rooted at the reservoir `v_*`.  Process its
nonroot vertices in postorder.  When `v` is processed, all its child edges
have already acted.  Let `g_v` be its current ordered-frame permutation and
let `\rho_v` be its prescribed permutation.  Put

\[
                              h_v=\rho_vg_v^{-1}.       \tag{5.10}
\]

Write `h_v` as a product of at most `R-1` transpositions, using its disjoint
cycle decomposition.  On the edge from `v` to its parent, run the
three-resolution loop once for each of these transpositions, in the order
which left-multiplies by `h_v`.  It sends the frame at `v` to
`h_vg_v=\rho_v` and applies the same collateral multiplier to its parent.

No later operation touches `v`: its child edges and its unique parent edge
have all been completed.  Induction toward the root fixes every nonroot
packet exactly, while the root absorbs all collateral in some unrestricted
valid frame.  A spanning tree has `2^k-1` edges, proving (5.8)--(5.9).
`\square`

For a partial-layer ledger, choose a depth-`k` rooted cube tree.  Process
depths from the leaves upward and group edges at one depth by their exterior
direction.  Each group is owner-disjoint.  Padding shorter permutation
words by identity steps gives at most

\[
                              3k^2(R-1)                \tag{5.11}
\]

partial resolution layers.  This scheduling bound is not charged to the
contiguous word because the entire network is offline.

### Theorem 5.4 (exact parity characterization)

Assume `k\ge2`.  Starting from one common reference identification, a full
assignment `(\rho_v)_{v\in Q_k}\in S_R^{2^k}` is realizable by closed
single-edge loops if and only if

\[
                 \prod_{v\in Q_k}\operatorname{sgn}(\rho_v)=+1. \tag{5.12}
\]

Thus the reservoir in Theorems 5.1 and 5.3 is needed only when the desired
assignment has odd total parity.

When (5.12) holds, the construction uses at most

\[
                         (R-1)(2^k+3)                 \tag{5.12a}
\]

three-resolution edge gadgets, hence at most three times this many bare
slab re-resolutions.  It can be scheduled in at most
`3k^2(R-1)+12(R-1)` partial layers.

#### Proof

Necessity is Proposition 5.2.  For sufficiency, choose a root `r` with two
distinct neighbors `u,v` and run the postorder construction of Theorem 5.3.
It fixes every nonroot label and leaves some label `g_r` at the root.  By
(5.12),

\[
                         \delta=\rho_rg_r^{-1}\in A_R.           \tag{5.13}
\]

Let `E_{xy}(a)` denote the edge operation which left-multiplies the labels
at `x,y` by `a`.  The four operations

\[
 E_{ru}(a),\quad E_{rv}(b),\quad
 E_{ru}(a^{-1}),\quad E_{rv}(b^{-1})                 \tag{5.14}
\]

restore the labels at `u,v` and left-multiply the root by
`b^{-1}a^{-1}ba`.  Taking `a,b` to be two transpositions sharing one point
produces a 3-cycle.  Every even permutation is a product of at most `R-1`
3-cycles: take an even transposition decomposition of length at most
`R-1`, pair its terms, use a single 3-cycle for two transpositions sharing
a point, and use the identity

\[
                     (ab)(cd)=(acb)(acd)              \tag{5.15}
\]

for a disjoint pair.  Repeating (5.14) therefore localizes `\delta` at the
root without altering any other packet.  This finishes the assignment.
Each 3-cycle costs four transposition-labelled edge loops.  Combining this
with (5.8)--(5.11) gives (5.12a) and the stated layer bound.  For `R=2`,
`A_R` is trivial and the same conclusion is immediate. `\square`

## 6. Rooted-table and missing-shadow theorem

Consider a disjoint union of parent product cells

\[
                   \mathcal Q=\biguplus_{\alpha}Q_{S_\alpha},
                   \qquad S_\alpha\ge R,               \tag{6.1}
\]

with total owner mass `G`.  Partition each parent into parallel `Q_R`
packets.  Put

\[
                         k_{\min}=\min_\alpha(S_\alpha-R).          \tag{6.2}
\]

Suppose that on every packet except possibly one designated packet per
parent, a prescribed rooted flag table is a physical coordinate conjugate
of one fixed exact diverse compiler.  No common conjugate is assumed between
packets.

### Theorem 6.1 (conditional HRS order-routing theorem)

All prescribed nonreservoir rooted tables in (6.1) can be realized
simultaneously by a legal compound slab network followed by the exact
compiler factors.  Their first-step maps are permutations within packets,
and all all-depth nesting and successor-cocycle identities are exact.

If the reservoir packets are discarded, their total owner mass is exactly

\[
 E_{\rm res}=\sum_\alpha 2^R
             =\sum_\alpha 2^{-\left(S_\alpha-R\right)}2^{S_\alpha}
             \le 2^{-k_{\min}}G.                       \tag{6.3}
\]

Relative to any complete balanced rooted table agreeing with the prescribed
tables on the nonreservoir packets, the total number of missing signed
targets through depth `H` is at most

\[
                         2H E_{\rm res}.                \tag{6.4}
\]

#### Proof

Apply Theorem 5.3 independently in every parent.  Proposition 3.1 gives the
rooted claims.  There is one reservoir `Q_R`, of size `2^R`, in each parent,
which proves (6.3).

At a fixed sign and depth, every discarded owner carries exactly one target
occurrence.  Charge each target missing from the retained realization to one
discarded occurrence of that target in the complete balanced table.  There
are at most `E_{\rm res}` such targets.  Sum over two signs and `H` depths to
obtain (6.4). `\square`

If the desired conjugates in every parent have even total parity, Theorem
5.4 realizes also the designated packet and one may take
`E_{\rm res}=0`.  For an odd-parity parent, one uncontrolled packet is
unavoidable within the closed single-edge-loop generator, although a larger
primitive could in principle change this invariant.

If, in addition, an earlier packetization discarded `E_0` owners from the
same complete balanced rooted table used in Theorem 6.1, and all current
prescribed packet tables agree with its restriction, then the combined
charge is

\[
                         2H(E_0+E_{\rm res}).           \tag{6.5}
\]

Thus the exact coefficient-one scale follows from

\[
                 HE_0=o(W),\qquad
                 H2^{-k_{\min}}G=o(W).                 \tag{6.6}
\]

In the near-spanning regime `G=(1-o(1))W`, the second condition is precisely
`2^{k_{\min}}/H\to\infty`.

No intermediate resolution is serialized in the final contiguous-OR word.
Hence the compound network adds zero word interfaces.  After the final
compiler is installed, the usual component ledger remains

\[
                       {G-E_{\rm res}\over2R}
\]

components and `O(HG/R)` final linearization cost.  This is `o(W)` whenever
`H=o(R)`.

## 7. Exact proved/conditional boundary

Proved unconditionally:

1. under the stated vacated-role connection, the smallest nontrivial closed
   compound is the three-resolution role transposition (0.1);
2. its three one-step transfer matrices are `(1/2)J_2`, but its cumulative
   owner-transfer matrix is `I_2`;
3. its exact owner path is (2.7), and it applies the same role transposition
   to both endpoint packets;
4. mod-two `T`-joins route any fixed physical transposition to any even
   packet set;
5. arbitrary compiler-coordinate conjugates are routable on all but one
   packet of every parent `Q_S`;
6. the sharp operation, partial-layer, reservoir, component, and
   missing-shadow ledgers are (5.8)--(6.6); and
7. transported compiler tables preserve the rooted successor cocycle at
   every depth.

The result is conditional only at the point where it is connected to the
global coefficient-one problem: the prescribed balanced flags must already
be grouped into the parent packets and, packet by packet, must be coordinate
conjugates of the diverse compiler.  The compound network supplies neither
that grouping nor the balanced selection of conjugates.  It also cannot
repair a preassigned noncocycle table.

Thus the bare-slab fixed-layer obstruction is not a universal adaptive
no-go for ordered compiler roles.  It is escaped at three resolutions for
such roles, with negligible reservoir loss once `2^{S-R}\gg H`.  The
remaining gate exposed by this lane is a cross-parent integral selection
statement:
choose the packet frames and compiler conjugates so that the final rooted
tables have aggregate missing-shadow defect `o(W)` simultaneously through
`H`, while retaining parent codimension `S-R\gg\log_2 H`.
