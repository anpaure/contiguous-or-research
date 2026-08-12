# Macroscopic MMM cross-sector rebundling: the exact Dyck-triple charge flow
# and a finite transport basis

Date: 2026-08-01  
Lane: R, additive-constant / central-palette recursion  
Status: exact raw-defect operator, exact zero-sum child charge, an explicit
integral cross-sector flow, a two-schema local factorization theorem, exact
capacitated cut criterion, and a corrected finite-residual reduction.
Literal paired packet columns and their physical capacities are not proved.

## 0. Outcome

The four-copy recurrence obstruction does not leave the child defect bank
without structure.  At one fixed child parameter `n`, every rooted raw MMM
defect has the form

\[
  0(1u_0 0v_0)\,0(1u_1 0v_1)\,0(1u_2 0v_2),                 \tag{0.1}
\]

where the six displayed fillers are Dyck words of total semilength `n-4`.
The associated nine-turn block has three lower phases whose nonempty Dyck
components are

\[
\begin{aligned}
 A_i&=1u_i0v_i,\\
 B_i&=v_i\,10\,u_{i+1},\\
 C_i&=u_i\,1v_i0,
 \qquad i\in\mathbb Z_3.                                   \tag{0.2}
\end{aligned}
\]

Reverse-complementation gives the three upper phases.  Thus (0.1) is a
literal all-dimension construction of valid defect blocks.

There is, however, an important incidence correction.  Put

\[
 \kappa(a)=\#\{\hbox{top-level primitive factors of }a
                         \hbox{ which equal }10\}.           \tag{0.3}
\]

For a physical defect `a=(a_0,a_1,a_2)`, its degree in the canonical
labelled block family is exactly

\[
               2+\kappa(a_0)\kappa(a_1)\kappa(a_2),          \tag{0.4}
\]

not three.  Canonical skeleton phase and canonical first-return extraction
do not commute.  Consequently the tempting uniform `1/3` fractional cover
is false already at `n=5`.

The same formula exposes the correct constructive object.  If

\[
                   k(a)=\prod_{i=0}^2\kappa(a_i),
 \qquad             b(a)=1-k(a),                             \tag{0.5}
\]

then

\[
                         \sum_a b(a)=0                       \tag{0.6}
\]

on every labelled child defect bank.  The canonical `1/3` block weights
have load defect exactly `b/3`.  Hence the macroscopic correction is an
ordinary **zero-sum integral transshipment**, not four copied parent banks.

There is a dimension-independent abstract transport basis.  On ordered
triples of nonempty Dyck words use

1. contextual Tamari rotations inside one component; and
2. one top-level-peak transfer between two components.

These two move schemas connect every fixed-size Dyck-triple layer.  Since
the incidence matrix of a connected graph is totally unimodular and
saturated, the integer charge `b` has an integral routing.  In particular,
at the palette ledger there is no further congruence obstruction.

In fact the first routing is completely explicit.  If `tau` is the
cross-sector phase map in (2.2), then

\[
                   b=\sum_x({\bf e}_x-{\bf e}_{\tau x}).     \tag{0.7}
\]

Thus one unit on every directed arc `tau x -> x` exactly balances the child
count.  The two local move schemas are needed to factor these generally
nonlocal arcs into a finite prospective packet vocabulary, not to prove
existence of an abstract flow.

The exact remaining physical theorem is now finite and explicit.  For each
used abstract edge one needs a **paired unit transporter**: a signed
combination of literal block/rerouter packets whose lower boundary is
`e_v-e_u` and whose reverse-complement upper boundary is the same reflected
unit.  With capacities, existence of the required compound packet is
equivalent to Hoffman's cut inequalities.  If only a subgraph is realized,
the exact uncapped residual is the component-sum charge.  Thus a bounded
residual basis follows as soon as all but bounded total component charge is
joined by the two transporter schemas.

This theorem exactly balances the central child **count and signed palette
ledger**.  It does not by itself give a disjoint block packing, a factor
chronology, residence, deeper shadows, topology, occurrence linkage, or a
common-cap compiler.  Those are stated separately below.

## 1. Raw defects and the six-filler block

Use the paper parameter `n>=4`; the cyclic ground has size

\[
                             q=2n+1.                          \tag{1.1}
\]

Let `D_n` denote either raw MMM turn-defect bank.  Its exact size is

\[
 D_n={q\over3}[z^{n-1}](C(z)-1)^3
    ={q\over n-1}\binom{2n-2}{n-4}.                          \tag{1.2}
\]

Here `C(z)` is the Catalan generating function.

### Lemma 1.1 (rooted six-Dyck parametrization)

A lower raw defect together with one of its three record-zero separators is
equivalent to

\[
 (p;u_0,v_0,u_1,v_1,u_2,v_2),qquad p\in\mathbb Z_q,         \tag{1.3}
\]

where all six fillers are Dyck and their total semilength is `n-4`.
Consequently

\[
 q[z^{n-4}]C(z)^6=3D_n.                                     \tag{1.4}
\]

#### Proof

The cyclic three-forest lemma writes a rooted lower defect uniquely as

\[
                         0a_0,0a_1,0a_2,                   \tag{1.5}
\]

where each `a_i` is a nonempty Dyck word.  Its unique first-return
factorization is `a_i=1u_i0v_i`.  Removing the three displayed first and
matching-return letters leaves six Dyck fillers.  Their semilength is
`(n-1)-3=n-4`.  The operation reverses uniquely.  Counting the root
coordinate and fillers gives the left side of (1.4); every unrooted defect
has exactly three record separators.  Equation (1.2), or
`C-1=zC^2`, gives the equality.  \(\square\)

Label the three skeleton positions in sector `i` by

\[
                         A_i=0,\quad B_i=1,\quad C_i=0.       \tag{1.6}
\]

Let `Q_A,Q_B,Q_C` be the corresponding three coordinate triples.  Let `H`
be the one-coordinates and `G` the zero-coordinates in the six fillers.
Then

\[
 |H|=|G|=n-4,qquad
 \Omega=H\mathbin{\dot\cup}G\mathbin{\dot\cup}
                Q_A\mathbin{\dot\cup}Q_B\mathbin{\dot\cup}Q_C. \tag{1.7}
\]

### Theorem 1.2 (literal six-filler q9 block)

The three masks

\[
             L_R=H\cup Q_R,\qquad R\in\{A,B,C\},             \tag{1.8}
\]

are lower raw defects.  Their pairwise unions

\[
             U_{RS}=H\cup Q_R\cup Q_S,qquad R\ne S,          \tag{1.9}
\]

are upper raw defects.  Thus (1.8)--(1.9) are a genuine padded nine-turn
block.

#### Proof

For the `B` phase, roots at `A_i` give the three nonempty components
`1u_i0v_i`.  For the `A` phase, roots at `C_i` give

\[
                             v_i\,10\,u_{i+1}.                \tag{1.10}
\]

For the `C` phase, roots at `B_i` give

\[
                             u_i\,1v_i0.                      \tag{1.11}
\]

Each word in (1.10)--(1.11) is a concatenation of Dyck words and contains
the displayed nonempty first-return factor, hence is a nonempty Dyck word.
The lower three-forest criterion proves (1.8).

For (1.9), complementing `U_RS` gives `G union Q_T`, where
`{R,S,T}={A,B,C}`.  Coordinate reversal turns the six complemented fillers
into their reverse-complements, which are again Dyck, and permutes the
skeleton phases.  Therefore the reverse-complement of `U_RS` is a lower
raw defect.  This is exactly the upper raw-defect criterion.  \(\square\)

The reversal in the second paragraph is essential.  Plain complementation
does not preserve the Dyck language.

## 2. The corrected canonical block operator

Let `V_n` be the labelled physical lower-defect bank.  It is convenient to
represent a state by the cyclic class

\[
                              x=[a_0,a_1,a_2],                \tag{2.1}
\]

with its actual ground labels retained.  Cyclically changing the record
separator rotates the triple and gives the same physical state.

For `a_i=1u_i0v_i`, define

\[
 \sigma(x)=[u_i1v_i0]_{i\in\mathbb Z_3},qquad
 \tau(x)=[v_i10u_{i+1}]_{i\in\mathbb Z_3}.                   \tag{2.2}
\]

The map `sigma` is a permutation: its inverse uses the unique last-return
decomposition.  The map `tau` is not generally a permutation.

Index the canonical labelled block family by `x in V_n` and put

\[
                         B_x=\{x,\sigma x,\tau x\}.           \tag{2.3}
\]

Parallel labelled copies of one geometric six-set are retained.  This is
the honest output of quotienting the three record separators; it is not a
claim that the physical incidence graph is regular.

### Lemma 2.1 (exact indegree of the cross-sector phase)

For a nonempty Dyck word `a`, let `kappa(a)` be (0.3).  Then

\[
                  |\tau^{-1}(y)|=\prod_{i=0}^2\kappa(y_i).   \tag{2.4}
\]

Consequently the exact degree of `y` in the labelled family (2.3) is

\[
                     \deg(y)=2+\prod_i\kappa(y_i).           \tag{2.5}
\]

#### Proof

There is one incidence `y in B_y`.  There is one incidence arising from
the unique `sigma^{-1}y`.  To solve `tau(x)=y`, one must, independently in
each component `y_i`, choose the displayed top-level primitive factor `10`
in a decomposition

\[
                           y_i=v_i\,10\,u_{i+1}.              \tag{2.6}
\]

Conversely every such triple of choices recovers one `x`.  This proves
(2.4)--(2.5).  \(\square\)

### Proposition 2.2 (the first exact obstruction and why it is useful)

At `n=5`, there are eleven states of cyclic component type

\[
              P=(1100,10,10),\qquad \deg(P)=2,               \tag{2.7}
\]

and eleven of type

\[
              R=(1010,10,10),\qquad \deg(R)=4.               \tag{2.8}
\]

Every canonical labelled block contains one `P` and two `R` states.
Therefore the canonical family alone has no fractional perfect cover.

#### Proof

The six fillers have total semilength one.  Its unique peak lies in a
`u`-slot or a `v`-slot; applying (0.2) gives exactly one primitive state and
two split states.  Cyclic labels give eleven of each type.  Equations
(2.5), (2.7), and (2.8) follow because `kappa(1100)=0` and
`kappa(1010)=2`.

Give weight `-2` to every `P` row and `+1` to every `R` row.  Every block
column has total dual weight zero, while the all-one right side has weight
`-11`.  Farkas' lemma excludes a fractional perfect cover.  \(\square\)

Proposition 2.2 is not the end of the lane.  It identifies the first
mandatory noncanonical transporter: the contextual

\[
                              1100\longleftrightarrow1010     \tag{2.9}
\]

Tamari transfer.  The audited crossed rerouter is a service-level example
of precisely this kind of second packet, although no claim is made here
that it has the full paired boundary required in Section 5.

## 3. Exact child charge

For a vector of block weights `w`, the lower load operator is

\[
 (A^-_nw)(y)=w_y+w_{\sigma^{-1}y}
                    +\sum_{x:\tau x=y}w_x.                   \tag{3.1}
\]

The upper operator `A^+_n` is its conjugate under reverse-complementation,
with the induced permutation of block labels.  In particular its degree
profile is the reflected copy of (2.5).

### Theorem 3.1 (zero-sum scaled divergence)

Put

\[
               k(y)=\prod_i\kappa(y_i),qquad b(y)=1-k(y).   \tag{3.2}
\]

Then

\[
 A^-_n{\bf1}=3{\bf1}-b,qquad
                         \sum_{y\in V_n}b(y)=0.              \tag{3.3}
\]

The corresponding upper charge is the reverse-complement of `b`.
Equivalently, uniform canonical block weight `1/3` misses the desired
unit load by exactly `b/3`.

#### Proof

The first identity is (2.5).  For the second, mark one top-level primitive
factor equal to `10` in a nonempty Dyck word.  The unmarked prefix and
suffix are arbitrary Dyck words, so its generating function is

\[
                           C(z)\,z\,C(z)=zC(z)^2=C(z)-1.      \tag{3.4}
\]

Thus the generating function for a triple weighted by
`prod_i kappa(a_i)` is `(C-1)^3`, exactly the unweighted generating
function for triples of nonempty Dyck words.  The cyclic label and
three-root quotient are identical on both counts.  Therefore

\[
                   \sum_y k(y)=|V_n|=D_n,                    \tag{3.5}
\]

which is (3.3).  Reverse-complementation preserves top-level atomic-factor
counts after reversal and gives the upper statement.  \(\square\)

### Corollary 3.2 (canonical macroscopic cross-sector flow)

The charge has the exact integral decomposition

\[
                         b=\sum_{x\in V_n}
                              ({\bf e}_x-{\bf e}_{\tau x}).   \tag{3.6}
\]

Equivalently, orient one unit of flow from `tau x` to `x` for every state
`x`.  The resulting divergence is `b`.  Under reverse-complementation the
same formula gives the upper flow.

#### Proof

The coefficient of `e_y` on the right side is one minus the number of
preimages of `y` under `tau`.  Lemma 2.1 identifies that number as `k(y)`.
This is exactly `b(y)`.  \(\square\)

This is the smallest macroscopic rebundling promised in the title.  It is
sourcewise explicit and uses the whole child bank; it is not obtained by
copying parent defects.  Its arcs are signed palette transports, not yet
literal disjoint factor packets.

At `n=5`, this flow is especially transparent.  Each of the eleven cyclic
contexts contains one Tamari pair

\[
                   (1100,10,10)\longleftrightarrow
                   (1010,10,10),                             \tag{3.7}
\]

with charges `+1` and `-1`.  Orienting all eleven pairs from the split word
to the primitive word is an exact charge routing.  The base obstruction of
Proposition 2.2 is therefore not a scalar deficit; it asks for this first
noncanonical paired transporter.

Equation (3.3) is the desired count reconciliation.  The whole child bank,
including the macroscopic birth sector missed by a four-copy lift, carries
zero total charge internally.  No bounded correction to the scalar count
is needed; the charge must be transported between child states.

An exact common fractional cover based on canonical labels plus signed
corrections `z` would satisfy

\[
 A^-_nz=b,qquad A^+_nz=b^+,qquad {\bf1}+z\ge0,qquad
                     w={{\bf1}+z\over3}.                     \tag{3.8}
\]

More generally, noncanonical packet columns may be added to the left side.
The inequality in (3.8), the equality of the lower and upper correction,
and physical packet capacities are substantive; zero total charge alone
does not imply them.

In scaled block coordinates, a nonnegative fractional packing requires

\[
                         0\le {\bf1}+z\le3.                  \tag{3.9}
\]

Once all vertex loads equal three, the upper bound follows from
nonnegativity, but it is useful to display it.  A literal integral block
selection requires the much stronger coordinatewise condition

\[
                         {\bf1}+z\in\{0,3\}^{\mathcal B}.    \tag{3.10}
\]

Neither (3.9) nor (3.10) follows from an abstract signed flow.

## 4. A two-schema local factorization graph

Let `T_N` be the set of ordered triples of nonempty Dyck words whose total
semilength is `N=n-1`.  For a fixed record separator `p`, these triples are
exactly the raw defects rooted at `p`.  Define an undirected graph `Gamma_N`
on this rooted layer by the following two contextual move schemas.

* **(R), a Tamari rotation.**  Inside one component, under arbitrary Dyck
  prefix and suffix contexts, replace

  \[
                     (1u0)(1v0)\longleftrightarrow1(1u0)v0. \tag{4.1}
  \]

  This is the usual binary-tree rotation; either side has the same
  semilength.

* **(S), a sector peak transfer.**  If a donor component remains nonempty,
  move one top-level factor `10` from the donor to the end of another
  component:

  \[
              (a_i10,a_j)\longleftrightarrow(a_i,a_j10).     \tag{4.2}
  \]

  The third component is unchanged.  Any ordered pair of sectors is
  allowed.

Both are finite schemas: dimension enters only through the Dyck contexts.

### Theorem 4.1 (connectivity)

For every `N>=3`, the graph `Gamma_N` is connected.

#### Proof

The rotation graph on Dyck words of a fixed semilength is connected.  A
self-contained induction proves this: if the first-return factorization is
`1u0v`, repeatedly use (4.1) to move every top-level factor of `v` under the
initial return; recursively normalize `u` and the moved factor.  Thus every
word reaches a fixed comb, and reversing moves joins any two words.

In particular a component of semilength `s` can be changed to `(10)^s`.
If `s>=2`, one terminal `10` may then be transferred by (4.2), leaving a
nonempty donor.  Repeating transfers changes any positive size composition
of `N` into `(N-2,1,1)`.  Finally use (4.1) independently in the three
components to reach one fixed canonical triple.  Every state reaches that
triple, proving connectivity.  \(\square\)

### Corollary 4.2 (unconditional abstract integral balancing)

Let `widehat Gamma_n` be the labelled physical graph obtained by taking the
rooted copy of `Gamma_N` at every `p in Z_q` and identifying the three rooted
representations of each physical defect.  For `n>=5`, `widehat Gamma_n` is
connected.  For `n=4`, the charge `b` is identically zero.  Consequently,
for every `n>=4` there is an integer flow `f` on the oriented edges of the
physical graph such that

\[
                            \partial f=b.                     \tag{4.3}
\]

#### Proof

Each rooted `p`-layer is connected by Theorem 4.1.  Two layers meet whenever
one physical defect has record separators at both coordinates.  For
`n>=5`, there are defects having a separator gap of `3` and defects having
a separator gap of `5`: choose the intervening component semilength `1` or
`2` and split the remaining semilength positively between the other two
components.  Hence the layer-intersection graph contains the translations
`p mapsto p+3` and `p mapsto p+5`.  Since `gcd(3,5)=1`, these translations
generate `Z_q`, so the physical quotient is connected.  At `n=4`, every
component has semilength one and `k=1`, hence `b=0`.

For `n>=5`, Theorem 3.1 gives total charge zero on the connected physical
graph.  Choose a spanning tree, root it, and orient it toward the root.  On
the edge above a vertex set `S` put the integer flow
`sum_(v in S)b(v)`, with its sign deciding direction.  Its divergence is
`b`.  This is the standard integral tree-flow construction.  \(\square\)

This is already the smallest macroscopic count-balancing theorem: child
defects are routed across Dyck-component triples by two contextual move
schemas.  It is not an assertion that each abstract edge is a literal
factor trade.

Corollary 3.2 gives an even shorter nonlocal routing on the `tau`-arcs.
The role of `widehat Gamma_n` is to reduce those nonlocal arcs to two finite
contextual move schemas.  A literal occurrence-labelled lift may remember
an absolute chosen root in addition to the physical mask; then a reroot
slide is an additional packet datum.  Connectivity here is for the physical
palette quotient obtained by identifying the three record roots.

## 5. The exact paired-transporter theorem

Let `P_n` be a catalogue of literal or relational packet columns.  A signed
packet relation `r` has a lower boundary `partial^- r`, an upper boundary
`partial^+ r`, and a complete resource support.  Negative coefficients
mean removal from a declared baseline; hence they are legal only within the
available support capacity.

### Definition 5.1 (paired unit transporter)

For an oriented abstract edge `e=(u,v)` of `Gamma_N`, a paired unit
transporter is a signed packet relation `r_e` satisfying

\[
 \partial^-r_e={\bf e}_v-{\bf e}_u,qquad
 \partial^+r_e={\bf e}_{\iota v}-{\bf e}_{\iota u},          \tag{5.1}
\]

where `iota` is the literal reverse-complement identification of the two
raw defect shores.  All other declared palette rows vanish.  A **guarded**
transporter additionally has zero boundary on owner, q1, residence,
deeper-shadow, topology, occurrence, and compiler rows named in its state.

The reflected upper equation in (5.1) is essential.  A lower-only Tamari
relation does not solve the simultaneous block problem.

### Theorem 5.2 (integral macroscopic rebundling)

Assume:

1. paired unit transporters are available for every edge of one connected
   spanning subgraph of `Gamma_N`;
2. the tree flow from Corollary 4.2 can be installed with the stated signs
   without exceeding any negative block or physical resource capacity.

Then the canonical child charge is exactly cancelled on both shores by an
integer compound relation.  Equivalently, the corrected scaled incidence
ledger is `3` at every raw defect row.

If every transporter is guarded, every named guard row is unchanged.

#### Proof

Take the integer flow `f` of Corollary 4.2 and form

\[
                              R=\sum_e f_e r_e.               \tag{5.2}
\]

Linearity and (5.1) give

\[
                  \partial^-R=b,qquad \partial^+R=b^+.      \tag{5.3}
\]

Adding this to the all-one canonical scaled ledger changes
`3-b` to `3` on both shores.  Hypothesis 2 makes the signed relation a legal
nonnegative replacement rather than only an identity in the Grothendieck
group.  Vanishing of additional guard boundaries is also preserved under
the sum.  \(\square\)

Theorem 5.2 is an exact theorem, but its hypotheses are not currently
proved for the physical MMM/Pascal factor.  It isolates two prospective
packet schemas rather than an unbounded collection of child-specific
repairs.

### Theorem 5.3 (capacitated min-max form)

Suppose a paired transporter on directed edge `e` can be used at most
`c_e` times, and suppose packet supports are serializable so these are the
only capacity constraints.  Then an exact charge routing exists if and
only if, for every vertex set `S subseteq T_N`,

\[
 \sum_{v\in S}b(v)
       \le \sum_{e\in\delta^-(S)}c_e,qquad
 -\sum_{v\in S}b(v)
       \le \sum_{e\in\delta^+(S)}c_e.                        \tag{5.4}
\]

For symmetric undirected capacity these are the two orientations of the
same cut condition.

For the present charge, every cut demand has the intrinsic form

\[
                  b(S)=|S|-|\{x:\tau x\in S\}|
                       =|S|-|\tau^{-1}(S)|.                  \tag{5.5}
\]

Thus a violated transporter cut is literally a shortage of sources whose
cross-sector phase enters `S`; it is not an unidentified global syndrome.

#### Proof

Add a supersource to positive-demand vertices and a supersink from
negative-demand vertices, with the usual capacities `|b(v)|`.  A saturating
flow is equivalent to a transporter flow with divergence `b`.  Max-flow
min-cut gives precisely (5.4).  Integrality follows from integral
capacities.  \(\square\)

If two packet menus share owners, colours, or cap cells, their conflicts
are not represented by scalar `c_e`; one must split the corresponding
resource into a capacity-one node or use the full packet-selection matrix.
Thus (5.4) is exact only under its stated serializability hypothesis.

## 6. Finite residual basis and exact cut obstruction

Let `Gamma'_N` be the subgraph of abstract moves for which a paired
transporter has actually been certified.  Ignore capacities temporarily.
For a connected component `K` put

\[
                             \beta(K)=\sum_{v\in K}b(v).      \tag{6.1}
\]

### Theorem 6.1 (component residual formula)

The charge `b` is exactly routable on `Gamma'_N` if and only if

\[
                              \beta(K)=0                     \tag{6.2}
\]

for every connected component `K`.  If signed residual charge is allowed,
the minimum possible residual `l_1` norm is

\[
                              \sum_K|\beta(K)|,               \tag{6.3}
\]

and the total positive residual equals half of (6.3).

#### Proof

An incidence column has coordinate sum zero in every component, proving
necessity.  Within one component, the integral spanning-tree construction
routes every integer vector of total zero; hence the incidence lattice is
exactly the saturated zero-sum lattice.  Leave one signed amount
`beta(K)` at an arbitrary vertex of each component to attain (6.3).  No
smaller `l_1` norm can have the prescribed component sums.  Since the total
sum over all components is zero, positive and negative residual masses are
equal.  \(\square\)

This gives the promised finite residual formulation.

* If the certified packet schemas join all states, the central ledger has
  zero residual.
* If they leave several components but `sum_K |beta(K)|=O(1)`, the residual
  has bounded signed mass and can be handed to a finite terminal gadget
  basis.
* If a component has unbounded `|beta(K)|`, (6.1) is the sharp cut
  obstruction and identifies which additional contextual transporter must
  cross it.

Under capacities, replace (6.2) by the Hoffman cuts (5.4).  Under physical
resource conflicts, use the corresponding expanded cut/Rado matrix.  This
is a constructive pricing rule: a violated cut asks for a packet column
crossing that named Dyck-state cut with the correct reflected upper
boundary.

## 7. Integral packing after charge balance

Charge balance is not hypergraph matching integrality.  One useful
downstream sufficient criterion is nevertheless exact.

### Proposition 7.1 (phase-cocycle rounding, conditional)

Suppose a corrected labelled block subfamily is degree three at every
defect on both shores and admits a block coloring

\[
                            \chi:\mathcal B\to\mathbb F_3    \tag{7.1}
\]

such that the three blocks incident with every defect have colors
`{0,1,2}`.  Then every color class is an exact disjoint block cover.

If the three incidences at vertex `v` have local phase labels
`r=0,1,2`, the rainbow condition is equivalent to

\[
                 \chi_B=\psi_v+\epsilon_v r_{vB},qquad
                 \epsilon_v\in\{+1,-1\}.                    \tag{7.2}
\]

For fixed signs, (7.2) is solvable if and only if the induced one-cochain
has zero voltage on every alternating incidence cycle.  On the upper shore
the phase label is reflected, `r \mapsto 2-r`, up to an affine root offset.

#### Proof

At every defect, each color occurs on exactly one incident block.  Hence a
fixed color covers it exactly once, and no two selected blocks intersect.
Every permutation of `F_3` is affine with slope `+1` or `-1`, proving
(7.2).  With the signs fixed, (7.2) is a potential equation on a bipartite
incidence graph; a potential exists exactly when every cycle sum vanishes.
\(\square\)

This criterion is sufficient, not necessary, and cannot be applied to the
uncorrected canonical family because Proposition 2.2 excludes even its
fractional cover at `n=5`.

## 8. Exact proved/conditional boundary

The unconditional advances are:

1. the six-filler construction (1.8)--(1.9) gives genuine lower and upper
   raw defect blocks in every dimension;
2. their exact canonical incidence operator is (3.1), with degree (2.5);
3. the child imbalance is the explicit integer charge
   `b=1-prod kappa`, and it has total zero exactly;
4. two contextual Dyck move schemas connect the whole fixed-size state
   layer;
5. therefore the child count admits an exact integral abstract flow, and
   every remaining ledger obstruction is an explicit transporter cut.

The first necessary noncanonical column is already visible at `n=5`:
`1100` and `1010` carry opposite unit charge.  Thus the crossed/Tamari
transporter is not an optional refinement; it is the minimal missing
rebundling type.

The unproved physical statement is:

> **Paired crossed-Tamari packet lemma.**  Contextual instances of (4.1)
> and (4.2), or a connected spanning subbank of them, have serializable
> literal compound packets satisfying the simultaneous boundary (5.1),
> with sufficient capacity and the required protected guard rows.

Proving that lemma and (5.4) would balance the central raw child defect
exactly.  A bounded violation of (6.2)/(5.4) would instead give a finite
residual basis.  Neither conclusion alone proves a physical
`B(k)+O(1)` word: residence, deeper shadows, owner topology, occurrence
matching, and common-cap compilation must still be carried by the packet
state.
