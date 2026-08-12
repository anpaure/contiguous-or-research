# Exact-`d` macro-Euler ports: global overlap, endpoint aperture, Hoffman expansion, and the `c=0` gate

**Date:** 2026-08-02  
**Lane:** ROOT, regenerative pull--cell / protected Catalan--pivot host  
**Status:** unconditional fixed-state globalization and private-core lemmas;
an exact macro-Euler reduction; an exact Hoffman characterization on the
complete-state rectangle face; and a literal obstruction outside that face.
The ambient Boolean/Catalan existence hypotheses isolated in Section 5 are
**unproved**.  No all-dimensional host or new value of `nu(k)` is claimed.

## 0. Outcome

This note attacks `OPEN-2` and the endpoint part of `OPEN-3` in
`RQPHR_c`.

There is one useful correction to the previous global-overlap warning.
Suppose one literal block state has already been fixed for every component.
If every consecutive pair is glued by equality of its complete ordered
`d`-rail, then all source letters at every nonadjacent identified address
agree automatically, even when intervening components have length less than
`d`.  The reason is transitivity through the chain of interval overlaps.
What pairwise port Hall fails to supply is precisely the **common state
section**: the same component realization at its incoming and outgoing
ports.  It also fails to control capacity-one addresses and propagated
aggregate histories.

Both remaining rows have exact sufficient treatments.

1. Every exact-`d` ordering has an explicit exclusive source core in each
   block.  Putting every capacity-one interval pin inside that core makes
   global address injectivity automatic.  An internal block of depth-row
   length `ell` has core length `max(ell-d,0)`; hence a short internal
   component has no such private pin capacity.
2. Once the complete seam token contains the ordered source rail, rooted
   free-port type, and propagated aggregate-history state, a component
   realization is a directed **macro-arc**.  An exact-`d` component order is
   an Euler trail using one macro-arc of every component colour.  A virtual
   closing arc and one terminal-only aperture state force the prescribed
   pivot-first orientation and the condition `o subset T_terminal`.

On the face where every remaining component has a literal Cartesian
complete-state menu `A_K x H_K`, the existence of the required connected
one-copy selector is exactly the protected-skeleton Hoffman system

\[
 \#\{K:A_K\subseteq X\}-
 \#\{K:H_K\cap X\ne\varnothing\}
 \leq \eta_R(X)\qquad(X\subseteq V_*).               \tag{0.1}
\]

This is a quantitative, integral criterion.  Cutting the resulting Euler
circuit at the virtual arc gives the desired exact-`d` order with the
aperture component last.

Cartesianity is load-bearing.  One literal depth-one component with the two
orientations `u->v` and `v->u` has a balanced half--half circulation and
full tail/head projections, but has no integral balanced choice.  Ordinary
Hall and a fixed-sink strict-gammoid rank see only the two projections and
cannot distinguish this relation from the full rectangle, which contains
loops.  Thus the minimal general state is the pairing-resolved transition
relation, not one unpaired gammoid.

The resulting `c=0` certificate is explicit: one pivot nonowner, full
`d`-overlap, terminal aperture containment, nonpositive Hoffman deficit, a
connected protected skeleton, zero quotient-address Hall deficit, complete
aggregate-history acceptance, and empty terminal casualty family.  The
unproved ambient assertion is that the protected Catalan component atlas
contains such rectangles and a skeleton while also realizing the
co-located reset.  The corrected stationary pull clock does not prove that
assertion.

Every owner-level rectangle used internally has one further one-copy
requirement.  If the union of its `d` boundary source letters already equals
its rank-`r` owner, the state is saturated and forces that owner in two
consecutive depth cells.  Hence internal completed rectangles must use
unsaturated states.  The currently available empty/proper-depth hinge
rectangles are saturated and do not instantiate the required Hoffman table
except at an open boundary or beside the unique nonowner.

## 1. Fixed-state full overlap really is globally literal

Let component `i` have positive depth-row length `ell_i`.  Its literal
source block

\[
                    A^i=(A^i_0,\ldots,A^i_{\ell_i+d-1})           \tag{1.1}
\]

has source interval

\[
 I_i=[a_i,a_i+\ell_i+d-1],\qquad
 a_1=0,\quad a_{i+1}=a_i+\ell_i.                    \tag{1.2}
\]

Thus consecutive blocks have full `d`-overlap.  Assume that one fixed
literal state has been chosen for every component and that

\[
              A^i_{\ell_i+t}=A^{i+1}_t
                    \qquad(0\leq t<d).               \tag{1.3}
\]

### Lemma 1.1 (nonadjacent letter consistency is transitive)

Under (1.2)--(1.3), all local letters mapped to one global source address
are equal.  Hence the quotient is one well-defined source word.  This
remains true when one or more intervening `ell_i` are less than `d`.

If every cap constraint is a conjunction of translated block-local
constraints, the same quotient satisfies every such cap constraint.
Nonlocal cap or history predicates must instead be included in the
aggregate state of Section 2.

#### Proof

Both starts and ends of the intervals `I_i` strictly increase.  If a global
address `x` belongs to `I_i cap I_j` with `i<j`, then it belongs to every
`I_q`, `i<=q<=j`.  Moreover

\[
 I_q\cap I_{q+1}=[a_{q+1},a_{q+1}+d-1].              \tag{1.4}
\]

Equation (1.3) identifies the two letters at `x` across every adjacent
pair in this chain.  Transitivity identifies the letters supplied by
blocks `i` and `j`.  A translated local cap accepts that same fixed letter,
which proves the cap statement. \(\square\)

The fixed-state qualification is essential.  A state-forgetting pairwise
port graph may use one realization of a middle component on its incoming
edge and a different realization on its outgoing edge.  Lemma 1.1 says
nothing about such an inconsistent section.

### Lemma 1.2 (exclusive source cores)

For an order of at least two blocks define

\[
\begin{aligned}
 J_1&=[a_1,a_1+\ell_1-1],\\
 J_i&=[a_i+d,a_i+\ell_i-1] &&(1<i<s),\\
 J_s&=[a_s+d,a_s+\ell_s+d-1].                        \tag{1.5}
\end{aligned}
\]

An interval with lower endpoint larger than its upper endpoint is empty.
Then `J_i` is exactly the part displayed in (1.5) which is contained in no
other block.  In particular,

\[
 |J_1|=\ell_1,\qquad |J_s|=\ell_s,\qquad
 |J_i|=\max(\ell_i-d,0)\quad(1<i<s).                 \tag{1.6}
\]

If every capacity-one pin assigned to block `i` is an interval wholly
inside `J_i`, and pins are distinct inside each block, then all selected
pin addresses are globally distinct.  A core of length `q` contains
exactly

\[
                         q(q+1)/2                    \tag{1.7}
\]

nonempty interval addresses.

#### Proof

The previous block ends at `a_i+d-1` and the next block begins at
`a_i+ell_i`.  Because all starts and ends are increasing, no block earlier
than `i-1` reaches farther right and no block later than `i+1` begins
farther left.  This proves (1.5)--(1.6).  Intervals contained in disjoint
cores cannot be the same global interval.  Finally, a linearly ordered
`q`-set has `q(q+1)/2` nonempty intervals. \(\square\)

The numerical bound (1.7) is only an address-capacity screen.  It does not
assert that those intervals have the target OR values required by the
compiler.

### Theorem 1.3 (exact quotient-address Hall deficit)

Fix the component order and its global quotient.  Let `T` be the remaining
capacity-one compiler tasks after the protected pivot bank has been fixed.
For each task `t`, let `Gamma_t` be the set of all target-correct global
interval addresses obtained by translating its allowed local occurrences
and then deleting protected or otherwise unavailable addresses.  Repeated
local occurrences with the same global image are deduplicated.  Put

\[
 \Delta_{\rm pin}=
   \max_{Y\subseteq {\cal T}}
       \left(|Y|-\left|\bigcup_{t\in Y}\Gamma_t\right|\right).  \tag{1.8}
\]

The minimum number of unmatched tasks is exactly `Delta_pin`.  In
particular, a globally address-injective pin selection exists if and only if

\[
                         \Delta_{\rm pin}=0.           \tag{1.9}
\]

Assigning every task to a block, restricting its candidates to that block's
exclusive core, and finding an injective selection inside each block is a
sufficient decomposed certificate for (1.9).

#### Proof

Form the bipartite graph from tasks to their distinct global interval
addresses.  The deficient form of Hall's theorem says that the maximum
matching leaves

\[
        \max_{Y\subseteq {\cal T}}(|Y|-|N(Y)|)
\]

left vertices unmatched.  Here `N(Y)=union_(t in Y) Gamma_t`, which proves
(1.8)--(1.9).  Exclusive cores of different blocks are disjoint by Lemma
1.2, so componentwise injections unite to a global injection. \(\square\)

## 2. Complete seam tokens and the macro-Euler equivalence

Fix a rooted Catalan forest `Q_0`.  Let `K_*` be its protected pivot/reset
component.  A **complete seam token** is a state in a finite set `V` which
records at least:

1. the ordered literal `d`-source rail;
2. the typed rooted free-port certificate needed for the next owner
   transition; and
3. the exact aggregate prefix state which must propagate through the seam.

The third coordinate may be the product of the clipped owner-residence
automata, common-cap state, exported reset state, and any other prefix
predicate being claimed.  The transition system must be exact: accepting
the terminal aggregate state is equivalent to accepting the corresponding
global predicate.  Merely recording separate component summaries without
their input-to-output action is not sufficient.

Every oriented literal realization `e` of a component `K` induces a
directed macro-arc

\[
                       e:t^-(e)\longrightarrow t^+(e),           \tag{2.1}
\]

coloured by `K`.  Equality of two consecutive tokens means literal rail
equality, a legal rooted free-port seam, and equality of the propagated
aggregate state.  If a seam relation is not naturally equality-labelled,
use one token copy for each accepted seam certificate; this is the usual
state expansion and changes no existence question.

Fix one pivot realization

\[
                         p:\alpha\longrightarrow\beta.           \tag{2.2}
\]

It will be the first block.  Fix an omitted lower root `o`.  A terminal
realization is **aperture typed** when its final owner `T^+` satisfies

\[
                              o\subseteq T^+.          \tag{2.3}
\]

For one such realization `r_o`, replace its ordinary output token by a
terminal-only copy `tau`.  No other selected component arc is allowed to
meet `tau`.  Add the virtual closing arc

\[
                            c:\tau\longrightarrow\beta.          \tag{2.4}
\]

The arc `c` is a proof device and contributes no source position or target.

### Theorem 2.1 (rooted aperture macro-Euler equivalence)

Choose one macro-arc from every component other than `K_*`, including the
fixed terminal arc `r_o`.  Assume `r_o` is the only selected arc entering
`tau` and `c` is the only selected arc leaving `tau`.  The chosen blocks
have an exact-`d` order after `p`, propagate every state encoded in `V`, and
end at the aperture-typed owner of `r_o` if and only if the selected
macro-arcs together with `c`

1. have zero total boundary, and
2. have connected underlying undirected support after isolated states are
   deleted.

Here `partial(u->v)=1_v-1_u`.  The resulting owner endpoint obeys the
phase-specific aperture condition (2.3).

#### Proof

An accepted order after `p` is a directed trail from `beta` to `tau` using
every selected component arc once, with `r_o` last.  Adding `c` makes its
arc multiset balanced and connected.

Conversely, a weakly connected balanced directed multigraph has an Euler
circuit.  At `tau` the unique incoming and outgoing arcs are `r_o` and `c`,
so they are consecutive in every Euler circuit.  Cut the circuit immediately
after `c`.  The result starts at `beta`, ends at `tau`, uses every component
arc exactly once, and has `r_o` last.  Prepending `p` gives the claimed
component order.  Equality of adjacent complete tokens propagates the
aggregate state, while Lemma 1.1 gives the unique literal source quotient.
Finally (2.3) is exactly the endpoint aperture for the chosen rooted phase.
\(\square\)

### Corollary 2.2 (whole-state reversal)

Suppose the complete token system has an involution `iota` under which

\[
          (u\longrightarrow v)^{\rm rev}
             =\iota(v)\longrightarrow\iota(u),        \tag{2.5}
\]

and all occurrence addresses, aggregate states, pins, and the reset token
are reversed simultaneously.  Then reversing a certificate from Theorem
2.1 gives a certificate for the opposite rooted phase.  The terminal
condition `o subset T^+` becomes the initial condition `o subset T^-`, as
required by the endpoint-aperture theorem.

#### Proof

Reverse the Euler trail and every literal block.  Equation (2.5) preserves
token equality and reverses all addresses in the one global word.  The two
endpoint containments are interchanged. \(\square\)

This is a quotient statement.  It does not justify selectively reversing
one packet against a frozen exterior.

## 3. Exact Hoffman expansion on the rectangle face

Let `I` be the component colours other than the fixed pivot.  Reserve
literal arcs `R` from pairwise distinct colours, including `r_o`.  Let

\[
                         P=\{c\}\cup R,
             \qquad \eta_R=\partial P.               \tag{3.1}
\]

Fix a state set `V_*` containing `beta,tau` and every endpoint of `P`.
Assume the underlying support of `P` contains a spanning tree of `V_*`.
No member of `R` other than `r_o` is incident with `tau`.
For every unreserved component `K`, assume its literal complete-state
transition relation contains a nonempty Cartesian rectangle

\[
                         A_K\times H_K\subseteq V_*\times V_*.   \tag{3.2}
\]

Every cross-pair in (3.2) must be one actual component realization with
the same owner/payload/upper/compiler declarations.  The rectangles avoid
`tau`, so its terminal-only incidence remains unique.

For \(X\subseteq V_*\) put

\[
 \ell_A(X)=|\{K:A_K\subseteq X\}|,
 \qquad
 r_H(X)=|\{K:H_K\cap X\ne\varnothing\}|.             \tag{3.3}
\]

### Theorem 3.1 (protected rectangular macro-port criterion)

Under the preceding hypotheses, one can select one literal macro-arc from
every unreserved component so that Theorem 2.1 applies if and only if

\[
                 \ell_A(X)-r_H(X)\leq\eta_R(X)
                         \qquad(X\subseteq V_*).       \tag{3.4}
\]

The `if and only if` is for the fixed rectangle system (3.2) and fixed
boundary `P`.  For arbitrary component relations merely **containing** the
rectangles, (3.4) is a sufficient condition.

#### Proof

Every selected free arc contributes one tail and one head.  The fixed bank
`P` is balanced after the free choice exactly when the aggregate free-tail
count `p` and free-head count `q` obey

\[
                              p-q=\eta_R.              \tag{3.5}
\]

Every component whose whole tail list lies in `X` must put its tail in
`X`, while at most `r_H(X)` components can put a head in `X`.  Thus (3.5)
implies (3.4).

Conversely, the possible aggregate tail vectors form the integral
polymatroid base

\[
       \sum_K \operatorname{conv}\{\mathbf1_v:v\in A_K\},       \tag{3.6}
\]

and the head vectors form the analogous base for the lists `H_K`.
Edmonds' integral polymatroid-intersection criterion turns their translated
intersection by `eta_R` exactly into (3.4).  Hence there is an integral
common count vector.  Two bipartite `b`-matchings choose one tail and one
head for every component with those counts.  Cartesianity pairs the choices
belonging to the same component into literal arcs.  Their boundary is
`-eta_R`, so adjoining `P` is balanced.  The reserved bank already spans
`V_*`, hence the full support is connected.  Theorem 2.1 applies.
\(\square\)

Define the exact rectangular deficit

\[
 \Delta_R=\max_{X\subseteq V_*}
     \bigl(\ell_A(X)-r_H(X)-\eta_R(X)\bigr).           \tag{3.7}
\]

Thus `Delta_R<=0` is the quantitative one-copy expansion condition.  It is
evaluated after the protected pivot, terminal aperture arc, every reserved
skeleton arc, and every literal guard deletion have been imposed.

### Corollary 3.2 (exact connected characterization on a pure rectangle atlas)

Suppose every component menu is itself a complete-state rectangle.  An
aperture-typed pivot-first exact-`d` order exists if and only if there are a
used state set `V_*` and reserved distinct-component arcs `R`, including the
terminal arc, such that `P={c} union R` contains a spanning tree and the
residual rectangles, after intersection with `V_*` on both shores, are
nonempty and satisfy (3.4).

#### Proof

Sufficiency is Theorem 3.1.  For necessity, take an accepted macro trail,
add `c`, and extract a spanning tree from its connected support.  Put in
`R` the selected component arcs of that tree and also `r_o` if it was not
already selected for the tree.  The remaining actual selector proves every
residual inequality (3.4) by the necessary half of Theorem 3.1. \(\square\)

This is the strongest generic integral Hall/Hoffman face currently
justified.  A strict gammoid may be used inside the definition of one
complete token or to choose disjoint compiler routes, but it does not erase
the tail--head pairing in a component transition.

## 3A. Support-first Rado--erosion route: the ports can be born afterwards

The literal-rail macro model is not the only sufficient route.  The newest
protected-support Rado theorem and maximal-erosion theorem permit the owner
chronology to be chosen first.  One then marks the Catalan forest inside
that chronology and constructs the source antecedent globally.

Let

\[
                         T=(T_0,\ldots,T_{W-1})        \tag{3A.1}
\]

be a Hamilton path on the middle owners, with distinct transition roots and
one fixed rooted matching phase `M_0`.  Let `S` be its occurrence-labelled
incidence support, which is an incidence matching in this phase; let
`F subseteq S` be the protected pivot/witness forest.  Assume the
phase-specific omitted root `o` lies in the required endpoint owner and the
complete propagated owner-history state of `T` is accepting.  Write
`delta_F(S)` for the protected graphic-Rado deficiency

\[
 \delta_F(S)=\max_{{\cal A}\subseteq {\cal R}}
       \bigl(|{\cal A}|-|E({\cal A})|+\kappa_F({\cal A})\bigr), \tag{3A.2}
\]

where `R` is the residual immediate-upper task shore.  Thus
`delta_F(S)=0` is exactly the existence of an upper-exact rooted Catalan
forest `Q_0` with `F subseteq Q_0 subseteq S`.

Adjoin the unique controlled nonowner at the declared outer pivot boundary
to obtain a depth-row word `T_tilde` of length `W+1`.  Let `J` be its source
address set.  In one combined prescribed-window instance, include the
post-insertion depth windows, every selected old crossing window, one chosen
interval for every required upper target, and all fixed literal pivot/collar
rows.  Compiler pins already fixed in the protected bank may also be
included.  The remaining compiler tasks are matched after the maximal word
is constructed, using the target-correct candidate sets in Theorem 1.3.
With lower point-pins `P_j`, caps `C_j`, and prescribed row values `R_H`,
put

\[
 E_j=C_j\cap\bigcap_{H\ni j}R_H                       \tag{3A.3}
\]

and define the nonnegative erosion defect

\[
\begin{aligned}
 \Delta_{\rm er}={}&
   \sum_{j\in J}{\bf1}_{E_j=\varnothing}
   +\sum_{j\in J}|P_j\setminus E_j|\\
  &+\sum_{H}
       \left|R_H\setminus\bigcup_{j\in H}E_j\right|. \tag{3A.4}
\end{aligned}
\]

By the arbitrary-window maximal-erosion theorem,
`Delta_er=0` is exactly the existence of one nonempty source word satisfying
all those union equations, pins, and caps; the pointwise maximal witness is
`A_j=E_j`.

### Theorem 3A.1 (support-first birth of globally guarded exact-`d` ports)

Assume

\[
                 \delta_F(S)=0,\qquad
                 \Delta_{\rm er}=0,\qquad
                 \Delta_{\rm pin}=0.                 \tag{3A.5}
\]

Then one may select an upper-exact rooted Catalan forest `Q_0` containing
`F` such that:

1. its `C=Cat_m` path components occur in the order inherited from `T`, and
   the `C-1` edges of `S-Q_0` are exactly their directed connector path;
2. the maximal word `A=(E_j)` has source length `W+d+1=B+1` and realizes
   every prescribed window row;
3. restricting `A` to the source interval of each component gives literal
   component blocks whose consecutive intersections are the same ordered
   `d` letters; hence all exact-`d` ports and all nonadjacent source
   identifications are globally consistent; and
4. the endpoint aperture, propagated owner history, selected upper
   occurrences, and globally injective compiler pins all hold in that one
   word.

Thus a support satisfying (3A.5), the co-located reset `Hhat->J=o`, empty
terminal casualty, and quotient regeneration is a quantitative
support-first `RQPHR_0` certificate.  Existence of such supports in all
dimensions is **unproved**.

#### Proof

The protected Rado theorem applied to (3A.2) selects `Q_0`.  The rooted
support of the full owner path `S` is itself a path.  Therefore a subset
`Q_0` of `U` edges has `W-U=C` path components, and the complementary
`W-1-U=C-1` path edges join those components in their inherited order.

Because `Delta_er=0`, the maximal-erosion theorem gives the one source word
`A_j=E_j` satisfying every row in the combined window family.  Its depth row
has length `W+1`, so `A` has length `W+d+1`.  If one component occupies
depth indices `[b,b+ell-1]`, restrict `A` to

\[
                         [b,b+\ell+d-1].              \tag{3A.6}
\]

Its consecutive `(d+1)`-unions are exactly that component's depth cells.
For consecutive components the two intervals (3A.6) overlap in
`[b+ell,b+ell+d-1]`, the same `d` letters of the already fixed global word.
This proves literal full overlap and all nonadjacent consistency without a
separate component antecedent choice.  The prescribed-window rows carry the
declared histories and upper occurrences, while `Delta_pin=0` and Theorem
1.3 choose distinct physical interval addresses.  The endpoint containment
was assumed in the rooted phase. \(\square\)

### Corollary 3A.2 (five quantitative zero-defect rows)

On the support-first face, the central `c=0` construction reduces to the
simultaneous zero conditions

\[
 \boxed{
   \Delta_R\le0,\qquad
   \delta_F(S)=0,\qquad
   \Delta_{\rm er}=0,\qquad
   \Delta_{\rm pin}=0,\qquad
   H=\varnothing.}                                   \tag{3A.7}
\]

Here `Delta_R` and its protected skeleton construct one connected rooted
owner chronology from a completed owner/history rectangle table;
`delta_F` marks the upper-exact Catalan forest inside it; `Delta_er` births
the common source antecedent and every fixed/selected interval row;
`Delta_pin`, evaluated in that maximal word, selects distinct global
compiler addresses; and `H=empty` is zero terminal
repair.  The co-located aperture reset and quotient successor remain typed
boundary requirements, not numerical consequences of (3A.7).

Every internal owner-packet menu counted by `Delta_R` must also be
**one-copy unsaturated**: no allowed boundary `d`-state may already have
union equal to the role's owner.  This is part of being a literal completed
table, not a sixth marginal cut.  The proved saturated-state lemma shows
that the existing empty/proper-depth hinge rectangles fail it internally.
Full-depth hinges with unsaturated tails, or another new completed
construction, remain possible; their all-dimensional supply is
**unproved**.

Every implication in this corollary is proved.  The joint existence of one
canonical table/support satisfying all five rows and the typed reset is
**unproved**.  In particular, the Rado and erosion theorems do not prove the
Hoffman row, and the corrected pull clock proves none of the common-table
requirements.

## 4. Why projected Hall or one unpaired gammoid is not enough

Take depth `d=1` and two disjoint nonempty source letters `U,V`.  A
one-cell component with owner

\[
                              T=U\cup V               \tag{4.1}
\]

has the two reversal realizations

\[
                         e_+:U\longrightarrow V,
                    \qquad e_-:V\longrightarrow U.   \tag{4.2}
\]

Let the required aggregate boundary be zero; equivalently, let the pivot
suffix and desired terminal token both be `U`.  The endpoint owner `T` may
be chosen to contain the omitted root `o`, so the owner-aperture row itself
passes.

### Proposition 4.1 (minimal literal correlation obstruction)

Weighting each arc in (4.2) by `1/2` gives an exact fractional one-copy
balanced circulation.  The tail projection and head projection are both
`{U,V}`, so every projected one-role Hall test and the unpaired fixed-sink
rank-one test pass.  There is no integral balanced choice and hence no
exact-`d` return trail from `U` to `U` using this component once.

The Cartesian hull `{U,V} x {U,V}` does have an integral solution, namely
a loop.  Those loops are not literal realizations of (4.1): the blocks
`(U,U)` and `(V,V)` have owners `U` and `V`, not `T`.

#### Proof

The two boundaries in (4.2) are negatives, so their half--half average is
zero.  Each integral choice has nonzero boundary.  Projection forgets
which tail is paired with which head and therefore identifies (4.2) with
its Cartesian hull. \(\square\)

This is also the smallest possible obstruction: one state has only loops,
and one role is the first point at which a fractional one-copy equation can
mix two opposite nonloop transitions.

More generally, arbitrary complete-state colour classes already contain
directed Hamilton cycle.  Given a digraph `D` on `V`, make one role `K_v`
for each vertex `v` and give it the arcs `v->w` of `D`.  A balanced
connected one-copy selector has one outgoing and one incoming arc at every
vertex and is therefore a directed Hamilton cycle.  Thus no theorem based
only on marginal Hall or one unpaired linkage rank can solve the general
correlated transition problem.  A pairing-resolved relation, a literal
rectangle subatlas, or a stronger structured fusion theorem is necessary.

## 5. Quantitative (c=0) certificate and the exact remaining hypothesis

The following clauses are a finite sufficient certificate.  Their
existence in the ambient Boolean/Catalan host is **not proved** here.

* **`HYP-1` (protected rooted input; unproved ambient existence).**  There
  is a rooted upper-exact Catalan forest `Q_0` containing the protected
  pivot/reset component, with the phase-specific omitted root `o`.
  Equivalently on the support-first face, there is a rooted owner-path
  incidence support `S` with protected forest `F` and
  `delta_F(S)=0` as in (3A.2).
* **`HYP-2` (one-credit literal atlas; unproved ambient existence).**  The
  pivot component has exactly one controlled nonowner depth cell, all other
  components have none, and all macro transitions use full literal
  `d`-overlap.  Every required upper witness is component-internal or is
  encoded in the exact aggregate transition state.  On the support-first
  face this clause is supplied instead by `Delta_er=0`, which constructs one
  global antecedent and births the component blocks by restriction.
* **`HYP-3` (rectangular expansion; unproved ambient existence, exact
  finite test once supplied).**  There are `V_*`, a terminal aperture arc
  `r_o`, and a protected distinct-component skeleton `R` satisfying
  (2.3), terminal isolation, and `Delta_R<=0` in (3.7).
  On the support-first face the same completed-hinge criterion is applied
  at the owner-packet level to construct the rooted chronology `T`; after
  `delta_F(S)=0` marks `Q_0`, its component connector order is inherited
  from `T` and no second component-level skeleton is required.  Every
  internal owner-level packet is one-copy unsaturated; the known saturated
  empty/proper-depth hinge menus are not substituted.
* **`HYP-4` (address and compiler closure; unproved ambient existence).**
  On the selected global quotient, the exact address deficit (1.8) is zero,
  and all pivot and boundary pins are included in the protected address
  bank before the candidate sets are formed.  A sufficient decomposed
  subcase assigns every remaining pin injectively to a target-correct
  interval wholly inside its exclusive core (1.5).  For an internal
  component with `q_K=max(ell_K-d,0)`, the necessary private-core screen is
  `|Pi(K)|<=q_K(q_K+1)/2`.
* **`HYP-5` (co-located reset and propagated acceptance; unproved ambient
  existence).**  The pivot nonowner realizes the incoming token `Hhat`, the
  owner-preserving rethread exports `J=o`, the aperture-typed terminal owner
  contains `o`, and the terminal aggregate state accepts every residence,
  cap, compiler, and exported-history coordinate read by the successor.
  No second reset or deficient overlap is used.
* **`HYP-6` (zero terminal casualty and regeneration; unproved ambient
  existence).**  The terminal family
  `H=H_up union H_comp union H_ray union H_ap` is empty, and the accepted
  exported state lies in the next reversal-quotient class, including the
  required even terminal child.

### Theorem 5.1 (finite (c=0) gate)

If `HYP-1`--`HYP-6` hold at one transition, then that transition satisfies
`RQPHR_0(m,d)`.  Its final source length is

\[
                              B+1,                    \tag{5.1}
\]

its charged carried sidecar is the singleton `{J}`, and it needs no
terminal repair.  If compatible certificates satisfying these clauses
exist on one infinite odd spine with the declared even terminal children,
then the already proved regenerative-spine implication gives

\[
                              \nu(k)\le B(k)+1.        \tag{5.2}
\]

This last infinite-spine existence is **unproved**.

#### Proof

On the direct literal-component face, Theorem 3.1 and Theorem 2.1 give a
pivot-first component order using every component once, with exact
full-`d` overlap, propagated aggregate acceptance, and the endpoint
aperture; Lemma 1.1 supplies the unique global literal word.  On the
support-first face, Theorem 3A.1 instead marks `Q_0` in the completed owner
chronology and births all component blocks from its maximal antecedent.
In both cases Theorem 1.3 and `HYP-4` supply address injectivity.
The upper atlas and compiler clauses close the remaining claimed rows.

There is one nonowner and every connector has overlap `d`, so the exact
charge identity is

\[
              \chi=\sum_Kg_K+\sum_e(d-o_e)=1.         \tag{5.3}
\]

Thus the source length is `B+1`.  `HYP-5` co-locates the one-in/one-out
reset with that sole credit.  `HYP-6` makes the terminal repair family
empty, hence `c=0`.  These are exactly the six clauses of `RQPHR_0` in
their complete-state realization.  The infinite-spine conclusion is the
conditional regenerative pull--cell theorem. \(\square\)

The substantive remaining assertion is now smaller than an unstructured
``global replay exists'': construct one protected complete-transition atlas
whose literal rectangle deficit (3.7) is nonpositive after a spanning
skeleton is reserved, while the pivot realizes the co-located reset and the
quotient-address Hall deficit and common-cap casualty are both zero.  The stationary
pull clock supplies only an average over tables and states; it supplies no
such common atlas.  The Catalan cycle-cover plus safe-pull alternative may
replace `HYP-3` only if the safe switches are globally address-closed or
hereditarily literal, preserve the complete aggregate state, and contain a
protected compatible spanning incidence tree.  Existing Ore/LKK expansion
does not prove that supply.

## 6. Independent audit of the decisive step

The companion audit

`scratch/audit_root_exact_d_macro_euler_aperture_hoffman_20260802.py`

is deliberately independent of the proofs above.  It checks:

1. exhaustive small full-overlap interval systems, including short
   intermediates, for nonadjacent letter consistency and the exclusive-core
   formula, together with exhaustive small quotient-address Hall systems;
2. birth of literal full-`d` component ports by restricting one global
   source word, and the saturated-state owner-repeat implication;
3. the sign and sufficiency of (3.4) by brute-force one-copy selection on
   small rectangle systems;
4. the Euler-circuit cut at the terminal-only aperture state by exhaustive
   arc-order enumeration; and
5. Proposition 4.1, including the false loop choices introduced by the
   Cartesian hull.

The audit result and SHA are recorded separately after execution.  The
finite audit is a regression for the exact reductions, not evidence that
`HYP-1`--`HYP-6` exist in all dimensions.

## 7. Scope ledger

**Proved in this note:** Lemmas 1.1--1.2, Theorem 1.3, Theorem 2.1,
Corollary 2.2, Theorem 3.1, Corollary 3.2, Proposition 4.1, and the
conditional implication Theorem 5.1.

**Explicitly unproved:** every ambient existence clause `HYP-1`--`HYP-6`,
nonpositive deficit for a canonical Catalan atlas, supply of the protected
skeleton, the owner-preserving aperture rethread, zero compiler casualty,
and existence of a compatible infinite spine.

The note does not prove a K17 word, an all-dimensional compiler, a generic
strict-gammoid rounding theorem, `nu(k)=B(k)+1`, or `nu(k)=B(k)`.

The proved external inputs used are the phase-specific endpoint-aperture
theorem and one-credit identity in
`MATH_THEOREM_ROOT_REGENERATIVE_PULL_CELL_ENDPOINT_APERTURE_GLOBAL_OVERLAP_AND_SINGLE_CREDIT_REDUCTION_20260802.md`,
the integral rectangular one-copy criterion in
`MATH_THEOREM_A_INTEGRAL_COLOURED_ROTOR_ONECOPY_MINMAX_AND_RAINBOW_FUSION_20260802.md`,
the protected graphic-Rado criterion in
`MATH_THEOREM_K_PROTECTED_ROOTED_SUPPORT_RADO_AND_CYCLE_SLACK_20260802.md`,
the arbitrary-window maximal-erosion closure in
`MATH_THEOREM_K_GLOBAL_MAXIMAL_EROSION_LIFT_AND_COARSENED_HISTORY_GATE_20260802.md`,
the saturated-state one-copy obstruction in
`MATH_THEOREM_A_PROTECTED_ROTOR_FUSION_CURVATURE_AND_SATURATED_HINGE_OBSTRUCTIONS_20260802.md`,
and the protected safe-switch composition theorem only for the optional
factor-first paragraph.  The corrected pull clock is cited only to delimit
scope; no integral conclusion is imported from it.
