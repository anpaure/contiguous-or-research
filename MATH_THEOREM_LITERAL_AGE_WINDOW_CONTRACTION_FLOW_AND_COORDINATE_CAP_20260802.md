# Literal age windows on the central contraction

Date: 2026-08-02  
Status: exact all-high flow formulation, exact coordinate-label cuts, a
balanced central matching, and unconditional literal obstructions.  This
note does not prove a common integral age flow, a Hamilton extension of the
balanced matching, a canonical-pull realization, or any contiguous-OR
bound.

## 0. Outcome

Put

\[
             k=2m+1,\qquad
 \mathcal L={ [k]\choose m},\qquad
 \mathcal O={ [k]\choose m+1},\qquad
 W=|\mathcal L|=|\mathcal O|,
\]

and let `2 <= d <= m`.  Fix a perfect central incidence matching

\[
                         M:\mathcal L\longrightarrow\mathcal O.
\]

The contraction digraph `D_M` has a useful literal refinement.  Label the
arc

\[
 q\longrightarrow q'=q-\{a\}+\{b_M(q)\},
 \qquad b_M(q)=M(q)-q,                                    \tag{0.1}
\]

by its departure `a`.  Taking length-`d` resident windows in this labelled
digraph gives an **age-window lift**.  A root- and role-exact integral
circulation in the lift is exactly a literal all-high cycle cover realizing
the prescribed target chains.  The ordinary subtour cuts are exactly what
changes that cycle cover into one Middle Levels Hamilton cycle.

This formulation exposes a coordinate cut not visible in the static SCD
selector.  If `D_x` is the number of selected departures labelled `x`, then

\[
 \boxed{
 D_x=|\{q:b_M(q)=x\}|
 \le \left\lfloor{\binom{2m}{m-1}\over d}\right\rfloor .}
                                                               \tag{0.2}
\]

The equality is cyclic coordinate balance; the inequality is the residence
run bound.  Every prescribed consecutive deck jump

\[
                         S+\{x\}\supset S                  \tag{0.3}
\]

at one fixed deck depth consumes a distinct `x`-departure.  Thus (0.2) is
an exact necessary cut on both the choice of the parity matching and the
ordering of the chain blocks.

There is no coordinate-capacity obstruction to choosing a central matching
alone.  Cyclic parenthesis matching gives a rotation-equivariant perfect
matching `M_cyc` with

\[
 |\{q:b_{M_{\rm cyc}}(q)=x\}|=
 {1\over m+1}\binom{2m}{m}=\operatorname {Cat}_m             \tag{0.4}
\]

for every coordinate.  Since `d <= m`, (0.4) satisfies (0.2), and the
central-matching extension theorem puts `M_cyc` inside a full SCD.  This is
only the balanced SCD/parity row: it does not prove that `D_(M_cyc)` is
Hamiltonian or that a target-exact age flow exists on it.

Arbitrary antichain-valid target chains nevertheless fail the literal row.
For every `m,d` in the displayed range, more than the right side of (0.2)
distinct chains of the form (0.3), with the rank-`m` maxima used as root
anchors, satisfy every static hypothesis but admit no literal cycle cover.
The smallest instance is `(k,m,d)=(5,2,2)` and needs only three nonempty
chains.  At `(7,3,3)` the same obstruction can be made using only proper
intersection targets, without rank-`m` root anchors.

There is also a target-free obstruction at the smallest parameter:

\[
 \boxed{
 \text{no depth-two resident Hamilton cycle in }J(5,2)
 \text{ has rainbow adjacent unions}.}                       \tag{0.5}
\]

Thus the corrected pull clock and the static SCD theorem meet at a genuine
integral correlation gate.  At `k=5` the fractional stationary trace exists,
while an all-high one-copy owner-rainbow Hamilton trace does not.

## 1. The labelled contraction and its age-window lift

For \(q\in\mathcal L\), the element `b_M(q)` in (0.1) is well defined.  The
outgoing arcs of `D_M` are

\[
 e(q,a):q\longrightarrow M(q)-\{a\}
        =q-\{a\}+\{b_M(q)\},\qquad a\in q.                  \tag{1.1}
\]

Write

\[
 \alpha(e(q,a))=a,\qquad
 \beta(e(q,a))=b_M(q),\qquad
 \omega(e(q,a))=M(q).                                      \tag{1.2}
\]

Thus `D_M` is `m`-regular in both directions, the arrival label is constant
on each outgoing star, and the owner colour is the matched upper vertex.

### 1.1 Resident windows

Let

\[
             \mathbf q=(q_0,q_1,\ldots,q_{d-1})             \tag{1.3}
\]

be a directed walk of length `d-1` in `D_M`, and put

\[
                         a_t=q_t-q_{t+1}
                 \qquad(0\le t\le d-2).                    \tag{1.4}
\]

Call (1.3) an age-window state when the `a_t` are distinct members of
`q_0`.  It carries the all-high flag

\[
                         f(\mathbf q)=(q_0;a_0,\ldots,a_{d-2}) \tag{1.5}
\]

and its depth-`j` intersection deck is

\[
 I_j(\mathbf q)=\bigcap_{t=0}^{j}q_t
       =q_0-\{a_0,\ldots,a_{j-1}\},
       \qquad 0\le j\le d-1.                               \tag{1.6}
\]

For `j=0`, the set in (1.6) is the root `q_0`.

Two states

\[
 \mathbf q=(q_0,\ldots,q_{d-1}),\qquad
 \mathbf q'=(q'_0,\ldots,q'_{d-1})
\]

form an arc of the age-window lift `A_d(M)` when

\[
 q'_t=q_{t+1}\quad(0\le t\le d-2)                           \tag{1.7}
\]

and, writing `a_(d-1)=q_(d-1)-q'_(d-1)`,

\[
                  a_{d-1}\in q_0-\{a_0,\ldots,a_{d-2}\}.    \tag{1.8}
\]

Condition (1.8) is exactly the new-oldest-letter condition in the literal
shift law.  In particular, (1.7)--(1.8) imply

\[
                         f(\mathbf q)\longrightarrow f(\mathbf q')
\]

literally.

### 1.2 Prescribed chains and the exact flow

Let `U` be a set of `W` roles.  For each role `u`, prescribe targets
`P_(u,j)` at some depths

\[
                         J(u)\subseteq\{0,1,\ldots,d-1\},
 \qquad |P_{u,j}|=m-j,                                      \tag{1.9}
\]

nested in increasing depth.  A candidate is a pair

\[
 \xi=(u,\mathbf q)
 \quad\text{such that}\quad
 I_j(\mathbf q)=P_{u,j}\quad(j\in J(u)).                    \tag{1.10}
\]

If the role template has a successor relation `E_U`, retain an age-window
arc `xi -> eta` only when their roles also form an edge of `E_U`.

Give every candidate a binary variable `x_xi` and every retained arc a
binary variable `z_(xi,eta)`.  The exact cycle-cover system is

\[
\begin{aligned}
 &\sum_{\xi:\operatorname{role}(\xi)=u}x_\xi=1
       &&(u\in U),\\
 &\sum_{\xi:\operatorname{root}(\xi)=q}x_\xi=1
       &&(q\in\mathcal L),\\
 &\sum_{\eta:\xi\to\eta}z_{\xi,\eta}=x_\xi,
 \qquad
   \sum_{\eta:\eta\to\xi}z_{\eta,\xi}=x_\xi
       &&(\xi).                                             \tag{1.11}
\end{aligned}
\]

If targets are occurrence-selected rather than already tied to roles, add
the usual exact target rows from OFHT.  They do not change the transition
part of (1.11).

### Theorem 1.1 (exact contraction age flow)

The zero-one solutions of (1.11) are in bijection with literal all-high
depth-`d` cycle covers which

* use every role once;
* use every lower root once;
* use every upper owner once through `M`; and
* realize every prescribed chain at its tagged deck depths.

The solution is one connected Middle Levels Hamilton cycle if and only if,
in addition, it satisfies

\[
 \sum_{\substack{\xi:\operatorname{root}(\xi)\in A\\
                  \eta:\operatorname{root}(\eta)\notin A}}
 z_{\xi,\eta}\ge1
 \quad
 (\varnothing\ne A\subsetneq\mathcal L).                  \tag{1.12}
\]

#### Proof

The first two rows of (1.11) select `W` candidates with distinct roles and
distinct roots.  The last row gives each selected candidate one predecessor
and one successor, so the selected age-window arcs form directed cycles.
The overlap equation (1.7) projects each component to a directed cycle in
`D_M`, and root exactness makes the projected cycles a cycle cover of
\(\mathcal L\).  Equations (1.6) and (1.10) give the target chains, while
(1.8) is precisely the literal age shift.

At a projected turn out of `q`, the upper vertex is `M(q)`.  Since every
root occurs once and `M` is bijective, every upper owner occurs once.  Thus
the alternating lift of a projected component is

\[
 q_0,M(q_0),q_1,M(q_1),\ldots .                             \tag{1.13}
\]

Conversely, the consecutive length-`d-1` windows of any literal cycle cover
give the candidates and arcs of (1.11).  Finally, the degree-one equations
make the projected arcs a permutation of \(\mathcal L\); the standard cuts
(1.12) say exactly that this permutation has one orbit.  Its alternating
lift (1.13) is then a Hamilton cycle of the Middle Levels graph.  \(\square\)

Theorem 1.1 is the fixed-`M`, all-high specialization of the exact OFHT
cycle-hypergraph.  Searching over parity matchings or canonical pull forests
means taking a union of systems (1.11), with the corresponding matching or
graphic constraints added.  The cuts below hold in every member of that
union.

## 2. Coordinate conservation and residence capacity

For a root-exact cycle cover, let `D_x` be the number of projected arcs
whose departure label is `x`, and put

\[
                         B_x(M)=|\{q:b_M(q)=x\}|.             \tag{2.1}
\]

### Lemma 2.1 (exact label law)

Every solution of (1.11) satisfies

\[
                         D_x=B_x(M)                           \tag{2.2}
\]

for every coordinate `x`.

#### Proof

On one projected cyclic component, sum the change of the indicator of `x`
over all turns.  The sum is zero.  Its positive terms are precisely arrivals
labelled `x`, and its negative terms are precisely departures labelled `x`.
Every root `q` is used once, and its arrival label is `b_M(q)`.  Summing over
the components gives (2.2).  \(\square\)

### Lemma 2.2 (residence run cap)

Every solution of (1.11) satisfies

\[
 D_x\le
 U_{m,d}:=\left\lfloor{\binom{2m}{m-1}\over d}\right\rfloor . \tag{2.3}
\]

#### Proof

Along each projected component, read the cyclic zero-one incidence word of
coordinate `x`.  Literal depth-`d` residence says that every positive run
has length at least `d`.  Unless the word is identically one, every positive
run has exactly one departure; an identically-one component has no
`x`-departure.  Therefore the number of `x`-departures on a component is at
most the number of its positive positions divided by `d`.

Across a root-exact cycle cover, the total number of positive positions is
the number of rank-`m` sets containing `x`, namely

\[
                              \binom{2m}{m-1}.
\]

Sum the componentwise bounds and use
`sum floor(t_i/d) <= floor(sum t_i/d)` to obtain (2.3).  \(\square\)

Combining Lemmas 2.1--2.2 proves (0.2).

At maximal depth the cap fixes the matching histogram completely.

### Corollary 2.3 (maximal-depth Catalan rigidity)

If `d=m`, every feasible central matching satisfies

\[
                         B_x(M)=\operatorname {Cat}_m
                         \qquad(x\in[k]).                    \tag{2.4}
\]

#### Proof

The cap is

\[
 {1\over m}\binom{2m}{m-1}
 ={1\over m+1}\binom{2m}{m}=\operatorname {Cat}_m.
\]

Also
\(\sum_x B_x(M)=W=(2m+1)\operatorname {Cat}_m\).  Hence all `2m+1`
upper bounds must be equalities.  \(\square\)

## 3. A balanced central matching and its exact scope

Identify the coordinates with the cyclic group `Z_(2m+1)`.  Encode an
`m`-set by a cyclic binary word, with `1` on the set and `0` off it.  Cyclic
parenthesis reduction repeatedly cancels adjacent `10` pairs.  Since the
word has one more zero than one, exactly one zero remains unmatched; denote
its coordinate by `c(q)`.

Define

\[
                         M_{\rm cyc}(q)=q+\{c(q)\}.            \tag{3.1}
\]

### Theorem 3.1 (balanced cyclic central matching)

The map (3.1) is a perfect incidence matching from \(\mathcal L\) to
\(\mathcal O\), is rotation equivariant, and satisfies

\[
                         B_x(M_{\rm cyc})=\operatorname {Cat}_m
                         \qquad(x\in[k]).                    \tag{3.2}
\]

Consequently it extends to a full SCD and satisfies every coordinate upper
cap (2.3) for `d <= m`.

#### Proof

Cut the cyclic word at its unique unmatched zero.  The remaining `2m`
symbols are completely parenthesis matched.  After the unmatched zero is
changed to one, those matched pairs remain and the changed coordinate is
the unique unmatched one.  Thus the inverse operation on a rank-`m+1` word
changes its unique unmatched one back to zero.  Hence (3.1) is a bijection,
and it is an incidence matching by construction.

Cyclic parenthesis matching has no distinguished origin, so rotating a word
rotates its unmatched coordinate.  Therefore `M_cyc` is rotation
equivariant.  Rotation acts transitively on coordinate labels, and hence all
the integers `B_x(M_cyc)` are equal.  Their sum is `W`, while

\[
 {W\over2m+1}
 ={1\over m+1}\binom{2m}{m}=\operatorname {Cat}_m.
\]

This proves (3.2).  The central-matching extension theorem puts every
perfect central matching inside a full SCD.  Finally,

\[
 \operatorname {Cat}_m={1\over m}\binom{2m}{m-1}
 \le {1\over d}\binom{2m}{m-1},
\]

so (2.3) holds.  \(\square\)

Theorem 3.1 is a positive theorem only for the coordinate-capacity row.  If
the prescribed chain family forces `H_(x,j)` jumps labelled `x` at a fixed
depth `j`, then `M_cyc` has enough label supply whenever

\[
                         H_{x,j}\le\operatorname {Cat}_m.     \tag{3.3}
\]

Neither (3.3) nor all the caps together select heads, balance the de Bruijn
rails, solve the age-window flow, or prove that `D_(M_cyc)` has one Hamilton
cycle.  Ordinary bipartite matching integrality cannot simply be applied
after the label quotas are appended: the same central edge must satisfy its
lower endpoint, upper endpoint, and added-coordinate row.  The exact object
is a coloured perfect matching, followed by (1.11).

### 3.1 The exact capacitated departure network

There is, however, one useful network-flow face after `M_cyc` and a
chain-to-root assignment have been fixed.  At a fixed deck offset
`j in {0,...,d-2}`, let

\[
                         A_j(q)\subseteq q                     \tag{3.4}
\]

be the departure labels still allowed at root `q`.  A prescribed consecutive
deck jump makes `A_j(q)` a singleton; an unprescribed position may retain a
larger list.  Some roots may already have fixed labels.  Delete those roots,
let `f_x` be the number fixed to `x`, and put

\[
                         c_x=\operatorname {Cat}_m-f_x.       \tag{3.5}
\]

Assume `c_x>=0` and that the remaining capacities sum to the number of
remaining roots.

Make a directed network with arcs

\[
 s\longrightarrow q\longrightarrow x\longrightarrow t,      \tag{3.6}
\]

where `q -> x` is present exactly when `x in A_j(q)`.  Give `s -> q`
capacity one, `q -> x` capacity one, and `x -> t` lower and upper capacity
`c_x`.  Arbitrary integral costs may be put on the middle arcs.

### Theorem 3.2 (fixed-depth capacitated Hall theorem)

The fixed departures extend at deck offset `j` to one allowed departure at
every root and exactly `Cat_m` departures of every coordinate if and only if

\[
 |R|\le \sum_{x\in N_j(R)}c_x
 \qquad
 (R\subseteq\mathcal L_{\rm free}),                          \tag{3.7}
\]

where

\[
                         N_j(R)=\bigcup_{q\in R}A_j(q).        \tag{3.8}
\]

Whenever it is feasible, (3.6) has an integral minimum-cost solution.

#### Proof

Replace coordinate `x` by `c_x` identical copies.  The desired extension is
a matching saturating the free-root shore.  Hall's theorem is exactly
(3.7).  Equivalently, (3.7) is the family of finite `s-t` cut inequalities
in (3.6).  The node-arc matrix is totally unimodular, so integral capacities
give an integral feasible flow and an integral minimum-cost optimum.
\(\square\)

In the completely unforced face, take `A_j(q)=q`.  The fractional flow

\[
                         y_{q,x}={1\over m}\mathbf1_{\{x\in q\}} \tag{3.9}
\]

has every root row equal to one and every coordinate column equal to

\[
 {1\over m}\binom{2m}{m-1}=\operatorname {Cat}_m.            \tag{3.10}
\]

Thus Theorem 3.2 rounds it to a balanced integral departure assignment.
This proves all Hall cuts (3.7) in the unforced Boolean face, not merely the
singleton coordinate totals.

For a concrete Ferrers chain factor assigned to roots, take one copy of
(3.6) at every marked deck offset.  The block-diagonal collection is a
time-expanded, totally unimodular relaxation.  It exactly tests every
fixed-depth coordinate row, including all higher-order Hall cuts (3.7).
It is not the full age problem: the chosen labels at different offsets must
belong to one ordered resident window, and the resulting first departures
must send the roots bijectively to heads in `D_(M_cyc)`.  Those linking rows
are absent from (3.6).

There is a clean regular face on which every cut (3.7) is automatic.

### Corollary 3.3 (rotation-regular departure rounding)

Let `rho` be cyclic coordinate rotation.  If every list is nonempty and

\[
                         A_j(\rho q)=\rho A_j(q)               \tag{3.11}
\]

for every root, then there is an integral choice

\[
                         a_j(q)\in A_j(q)                     \tag{3.12}
\]

which uses every coordinate exactly `Cat_m` times.

#### Proof

The rotation action on rank-`m` sets is free.  Indeed, if a rotation of
order `e` fixes an `m`-set, that set is a union of `e`-element coordinate
orbits, so `e` divides both `m` and `2m+1`; hence `e=1`.  Every root orbit
therefore has length `2m+1`.

For one orbit, choose a representative `q` and one label `a in A_j(q)`.
At `rho^t q`, choose `rho^t a`.  Equation (3.11) makes every choice legal,
and along this root orbit each coordinate is chosen exactly once.  The
number of root orbits is

\[
                         {W\over2m+1}=\operatorname {Cat}_m.
\]

Taking the union over the orbits proves the result.  \(\square\)

Thus a **concrete rotation-equivariant** Ferrers chain/root factor clears
all fixed-depth Hall cuts integrally.  The corrected pull clock gives only
a rotation-symmetric fractional average; it does not by itself produce the
concrete equivariant lists required by Corollary 3.3.

### 3.2 The first non-network row

If `y_(q,a)` selects the first departure at `q`, its head is forced to be

\[
                         h(q,a)=M_{\rm cyc}(q)-\{a\}.          \tag{3.13}
\]

A projected cycle cover requires the additional equations

\[
 \sum_{q,a:h(q,a)=h}y_{q,a}=1
 \qquad(h\in\mathcal L).                                    \tag{3.14}
\]

Columns `y_(q,a)` now meet a tail row, a departure-colour row, and a head
row.  This is the first higher-order coupling: (3.7) for every time layer
does not imply (3.14), and (3.14) still does not impose the window overlap
or subtour cuts.

The failure is already concrete at the smallest parameter.  For `m=d=2`,
Theorem 3.1 gives exactly two arrivals of each coordinate, and Theorem 3.2
gives an integral departure assignment with exactly two departures of each
coordinate.  Hence every singleton capacity row and every unconstrained
Hall cut (3.7) is feasible.  Theorem 5.1 below nevertheless proves that no
choice satisfying the head, residence, rainbow-owner, and one-cycle rows
exists.  Thus Boolean symmetry plus bipartite-flow integrality stops
strictly before the desired common factor.

### 3.3 Why the time layers do not form one TU system

Assume here that `m>=3` and `d>=3`, so that two proper deck depths exist and
the set `S` below is nonempty.  The first two proper deck depths already
contain a determinant-two minor.
Choose

\[
 S\in{[k]\choose m-2},\qquad b\notin S,\qquad T=S+\{b\},     \tag{3.15}
\]

then choose `a notin T`, `c in S`, and
`x notin T union {a}`.  Put

\[
 q=S+\{a,b\},\qquad q'=T+\{x\},\qquad
 S'=T-\{c\},\qquad T'=S+\{a\}.                              \tag{3.16}
\]

The following three all-high local flags exist:

* a flag at `q'` whose first two proper decks are `T,S`;
* a flag at `q` whose first two proper decks are `T,S'`; and
* a flag at `q` whose first two proper decks are `T',S`.

On the target rows `S,T` and the root row `q`, their columns are

\[
 \begin{array}{c|ccc}
       &f_1&f_2&f_3\\ \hline
 S     &1&0&1\\
 T     &1&1&0\\
 q     &0&1&1
 \end{array}                                                \tag{3.17}
\]

and the determinant is two.  Hence the separate network matrices at the
two depths do not remain totally unimodular after arbitrary rooted-chain
columns are identified.  This minor does not disprove the complete SCD
selector, whose global integral solution is known; it proves that a positive
Ferrers argument needs an additional path-splice, laminar, or absorber
hypothesis.  Boolean marginal symmetry alone is not such a hypothesis.

In particular, the coordinate-capacity row is not the non-TU row: its exact
matrix is the network (3.6).  Non-TU first appears here when two depths are
identified as one rooted window column; the head equations (3.14) add a
second, independent three-resource coupling.

This is the first **exhibited** loss of network total unimodularity.  At
`d=2` the displayed two-depth minor is unavailable; the note makes no claim
that it identifies an absolute first non-TU row there.  Head bijection,
resident-window overlap and the later subtour cuts remain separate coupling
rows and are not used in determinant (3.17).

## 4. Prescribed deck jumps force the coordinate cut

For a prescribed family, fix a deck depth `j` with `0 <= j <= d-2` and a
coordinate `x`.  Let `H_(x,j)` be the number of roles for which both
depths `j,j+1` are prescribed and

\[
                         P_{u,j}=P_{u,j+1}+\{x\}.              \tag{4.1}
\]

### Lemma 4.1 (fixed-depth jump cut)

Every literal cycle cover realizing the family satisfies

\[
                         H_{x,j}\le B_x(M)\le U_{m,d}.        \tag{4.2}
\]

#### Proof

Equations (1.6) and (4.1) force the departure at offset `j` of that role to
be `x`.  Distinct roles occupy distinct cycle positions.  On every directed
cycle, shifting all positions by the same offset `j` is a bijection, so
these forced departures are distinct.  Thus `H_(x,j) <= D_x`.  Apply
Lemmas 2.1--2.2.  \(\square\)

The fixed-depth qualification is necessary.  One physical departure occurs
in several overlapping age windows at different offsets, so jumps at
different depths cannot simply be added.

### Theorem 4.2 (antichain-valid coordinate overload)

For every `m>=2` and `2<=d<=m`, there is a family of prescribed target
chains satisfying all static hypotheses of the antichain-top SCD theorem
but admitting no literal cycle cover for any choice of central matching,
SCD, pull forest, or block order.

#### Proof

Fix a coordinate `x` and put

\[
                         N=U_{m,d}+1.                         \tag{4.3}
\]

There are `binom(2m,m-1)` distinct `(m-1)`-sets not containing `x`, and
`N` is no larger than this number.  Choose distinct such sets
`S_1,...,S_N`.  Prescribe `N` chains

\[
                         \mathcal C_t:\quad
                         S_t\subset S_t+\{x\},                \tag{4.4}
\]

tagged at deck depths one and zero respectively, and leave the remaining
`W-N` roles empty.

All named sets are pairwise distinct.  The maxima `S_t+{x}` are distinct
rank-`m` sets and hence form an antichain.  Therefore the static theorem
does assign the roles to distinct SCD chains and owners.  In a literal
serialization, however, (4.4) gives `H_(x,0)=N`, contrary to Lemma 4.1.
The contradiction precedes owner rainbow and connectedness.  \(\square\)

The parameter-minimal instance has

\[
                         (k,m,d)=(5,2,2),\qquad U_{2,2}=2.
\]

Taking `x=1` and

\[
 \{2\}\subset\{1,2\},\qquad
 \{3\}\subset\{1,3\},\qquad
 \{4\}\subset\{1,4\}                                    \tag{4.5}
\]

already contradicts the cap.  This is the smallest nonvacuous all-high
parameter pair because `2<=d<=m`.

There is also a proper-target-only version, so the obstruction is not an
artifact of naming the root.

### Corollary 4.3 (smallest proper-target overload)

At `(k,m,d)=(7,3,3)`, the six chains

\[
                         \{y\}\subset\{1,y\},
                         \qquad y=2,\ldots,7,                 \tag{4.6}
\]

tagged at depths two and one satisfy all static antichain hypotheses but
admit no literal cycle cover.

More generally, the same construction works for every `m>=3` and
`3<=d<=m` using `U_(m,d)+1` distinct sets

\[
                         S\in{[2m+1]-\{x\}\choose m-2}
\]

and chains `S subset S+{x}` at depths two and one.

#### Proof

For the displayed instance, coordinate `1` lies in
`binom(6,2)=15` roots, so depth-three residence allows at most five
departures of `1`.  Every chain in (4.6) forces a different departure of
`1` at offset one, giving six.

In general there are enough distinct `S` because

\[
 {\binom{2m}{m-2}\over\binom{2m}{m-1}}
 ={m-1\over m+2}>{1\over d}
 \qquad(m\ge3,\ d\ge3).                                    \tag{4.7}
\]

Thus `binom(2m,m-2) >= U_(m,d)+1`, and Lemma 4.1 applies with `j=1`.
All named targets are distinct and the rank-`m-1` maxima form an
antichain.  \(\square\)

## 5. The smallest carrier obstruction needs no targets

The preceding overloads disprove arbitrary prescribed-chain
serialization.  At the smallest parameter, even the unprescribed
owner-rainbow carrier fails.

### Theorem 5.1 (no resident rainbow `J(5,2)` Hamilton cycle)

There is no depth-two resident Hamilton cycle

\[
                         q_0,q_1,\ldots,q_9,q_0
\]

of `J(5,2)` for which the ten adjacent unions `q_i union q_(i+1)` are
pairwise distinct.

#### Proof

Let `a_i` be the coordinate departing from `q_i`.  Depth-two residence
forces `a_(i+1)` to be the other member of `q_i`, so

\[
                         q_i=\{a_i,a_{i+1}\}.                 \tag{5.1}
\]

Since the `q_i` are all ten vertices of `J(5,2)`, the adjacent pairs in the
cyclic word `a_0...a_9` are exactly the ten edges of `K_5`.  Pairwise
distinct adjacent unions say that

\[
                         T_i=\{a_i,a_{i+1},a_{i+2}\}          \tag{5.2}
\]

are the ten triples of the five-point set.

The ten distance-two pairs

\[
                         \{a_i,a_{i+2}\}                     \tag{5.3}
\]

are also exactly the edges of `K_5`.  Indeed, a fixed edge belongs to three
triples.  Its unique adjacent occurrence in (5.1) accounts for the two
consecutive triple windows on either side of that occurrence.  Its third
triple occurrence is therefore the unique distance-two occurrence (5.3).

Put

\[
                         E_j=a_{2j},\qquad O_j=a_{2j+1}
                         \quad(j\in\mathbb Z_5).              \tag{5.4}
\]

The pairs (5.3) split into two edge-disjoint five-edge closed trails

\[
 E_0E_1\cdots E_4E_0,
 \qquad
 O_0O_1\cdots O_4O_0.                                      \tag{5.5}
\]

Every edge in the two trails is distinct.  A connected simple Eulerian
graph with five edges cannot contain two cycles, since two simple cycles
use at least six edges.  Hence each trail in (5.5) is a five-cycle.  They
partition `E(K_5)`, so they are complementary Hamilton cycles.

Relabel the coordinates by `Z_5` so that `E_j=j`.  The complementary
five-cycle uses the step-two edges, and its directed traversal has the form

\[
                         O_j=c+2j
                         \quad\hbox{or}\quad
                         O_j=c-2j                             \tag{5.6}
\]

for some `c in Z_5`.  Either affine map in (5.6) has a fixed point: solve
`j=c+2j` or `j=c-2j` modulo five.  Thus `E_j=O_j` for some `j`, contradicting

\[
                         q_{2j}=\{E_j,O_j\}
\]

being a two-set.  \(\square\)

Distinct adjacent unions are exactly the upper-owner row of a Middle Levels
Hamilton cycle.  Therefore Theorem 5.1 proves (0.5).  It does not rule out
mixed age types or a fractional stationary trace.

## 6. Combination with the corrected pull clock and OFHT

The three previously proved objects now have a common exact interface.

1. The antichain-top SCD theorem solves the role, static target-chain, root,
   and free-owner resources.  It does not solve the arc variables in
   (1.11).
2. The corrected pull-clock theorem gives a rational stationary circulation
   with the required rank marginals after owner and stabilizer averaging.
   It may repeat owners and components and is not confined to one fixed
   contraction `D_M`.
3. OFHT says that the common integral choice is a resource-exact circulation
   in the literal compatibility digraph.  Theorem 1.1 identifies that
   circulation explicitly with the resident age-window lift on the all-high
   face.

Theorem 3.1 removes the bare coordinate-capacity objection to selecting an
SCD central matching.  Theorems 4.2 and 5.1 show why this does not round the
fractional clock: coordinate-labelled chain demands can exceed every
resident cap, and even a target-free balanced count need not admit a
resident owner-rainbow Hamilton order.

For a positive canonical Ferrers theorem, the first exact checks are now:

\[
 H_{x,j}\le B_x(M)\le U_{m,d}
 \qquad(x\in[k],\ 0\le j\le d-2),                           \tag{6.1}
\]

followed by feasibility of (1.11) and then the subtour cuts (1.12).  If a
coordinate-symmetric concrete chain factor has
`H_(x,j) <= Cat_m`, the balanced matching `M_cyc` clears (6.1), but a
fractional symmetric average of chain factors does not supply such a
concrete factor.  That is the precise common-rounding row still open.

No statement here supplies residence for the mixed pull blocks, complete
upper shadows, protected interfaces, a compiler, or any additive constant.
