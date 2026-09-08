# Equivariant same-parity induction from tap-decorated orbit flows

**Date:** 2026-08-03  
**Status:** unconditional quotient/lifting and induction theorems, followed
by a conditional finite-state target.  No all-dimensional orbit schema,
transition arrow, or new bound on `nu(k)` is asserted to exist.

## 0. Verdict

Write

\[
                         k_m=2m+1.
\]

The persistent induction is the same-parity step

\[
             g_m\longrightarrow g_{m+1},
             \qquad k_m\longrightarrow k_m+2,          \tag{0.1}
\]

with two terminal branches at every odd state:

\[
       g_m\longrightarrow\text{terminal at }2m+1,
       \qquad
       g_m\longrightarrow\text{terminal at }2m+2.       \tag{0.2}
\]

The correct quotient object is not a vector of defect counts.  It is a
finite **tap-decorated orbit quiver** of complete states and complete
certificate arrows, marked by the stabilizer/transporter data of the
symmetry action groupoid.  Its objects retain the complete persistent
boundary state, its arrows retain the materialized child shared by the
successor and odd terminal, rooted chronology, physical assignment,
continuation holonomy, and authenticated successor, and its inner flow
quotients retain every addressed capacity.  The even terminal may be a
separate complete extension of the same source state.

There are two different flow requirements.

* The regenerative branch must have full flow.  A bounded deficit is legal
  only when the exact unserved objects form a bounded typed sidecar which is
  exported and **replaced**, rather than accumulated, at the next step.
* The odd and even terminal branches need only uniformly bounded flow or
  matching deficiency, provided a literal repair theorem turns the actual
  omitted family into uniformly bounded terminal charge.  Terminal charge
  is paid once and is not exported.

A useful equivariant strengthening is available.  On a free cyclic bulk,
every exact orbit-flow or orbit-matching deficiency is a multiple of the
orbit order.  Hence a dimension-independent deficiency bound becomes exact
full saturation once the free orbit order exceeds that bound.  This does
not apply to fixed seams, roots, openings, compensation paths, short
orbits, or any other nonfree resource; those objects must be isolated in
the finite boundary/sidecar state.

The fresh-pair action supplies a natural growing common group for one
same-parity arrow.  If `k=2r-1`, rotate the `k` old coordinates by `C_k` and
fix the two fresh coordinates.  An old subset of rank `r+a` has period at
least `k/|2a+1|`; an addressed object with an equivariant projection to that
subset has at least the same period.  Thus every exact-period stratum in an
`O(sqrt(k))` old-rank band has growing modulus.  Uniform bounded defects
therefore vanish without global freeness, provided different period strata
are capacity-separated and each stratum is itself period-pure.

This common action is local to one arrow.  On the child it fixes the fresh
pair and is not the full `C_(k+2)` rotation needed as the old-coordinate
action of the next arrow.  Iteration still requires an authenticated rolling
change-of-group/reframing interface.

Under a uniform finite marked quotient with a nonempty recurrent core,
full regenerative flow and bounded odd/even tap charge lift to one literal
infinite odd spine with an adjacent-even tap at every level.  The uniform
bounded-charge reset-spine theorem then gives `nu(k) <= B(k)+O(1)`.

The present note proves that implication and identifies an exact conditional
finite-state schema and proof target.  It does not construct the state or its
open arrows.

## 1. Complete states and tap-decorated arrows

Let `X_m` be a finite family of literal auxiliary states on `2m+1`
coordinates.  A state contains every persistent datum needed to authenticate
the next step.  In the current regenerative language this includes the
complete product boundary

\[
 \Xi=\bigl(
   \text{owner/facet/palette};\Delta,b;
   \mathcal R_d^+,\mathcal R_d^-;
   \text{reserve},J,\text{opening},\nu,\star,
   \text{private};\mathsf W,\mathsf S,\mathsf C;
   \mathsf R_{\rm res}
   \bigr),                                             \tag{1.1}
\]

together with protected topology, voltage, named provider and boundary
addresses, the structural frame/coset, every exported exception, the
root/common-basis datum used by successor authentication, and the
parent-authentication datum.  Purely terminal compiler and repair choices
need not be exported when phase decoupling has been proved.

For a terminal certificate `C`, retain the exact charge

\[
                  \tau(C)=c(C)+R(\mathcal H(C)),       \tag{1.2}
\]

where `H(C)` is the literal omitted family after the final replay.  A bound
on a matching deficiency is not yet a bound on (1.2) unless a repair
theorem controls this actual family.

Fix `C >= 0`.  An **odd-decorated arrow** from `x in X_m` to
`y in X_(m+1)` is a complete record

\[
                         a:x\longrightarrow y          \tag{1.3}
\]

which contains one literal certificate jointly realizing the odd successor
`x -> y` and the odd terminal at `2m+1`, with terminal charge at most `C`.
Every materialized-child, structural-host, root/common-basis/cap,
occurrence, supplier, chronology, and successor-authentication choice shared
by these two assertions is quantified inside the arrow.

An **even tap** on `x` is a separate complete certificate terminalizing the
same literal state at `2m+2`, again with charge at most `C`.  It may use a
different terminal materialization, compiler, and physical assignment,
because these data are not exported.  If an even choice also affects the
persistent child, it is not terminal-only and must instead be bundled into
the arrow.

A **tap-decorated step** is an odd-decorated arrow together with an even tap
on its source.  This is exactly the quantifier pattern of one odd-spine
level; it does not require the two terminal branches to share terminal-only
choices.

Denote the complete arrow set by `A_m^C`, with source and target maps

\[
                 s:A_m^C\to X_m,
                 \qquad t:A_m^C\to X_{m+1}.           \tag{1.4}
\]

The definition deliberately moves every persistent shared existential into
the odd-decorated arrow.  Separate transition and odd-terminal flow
positives do not define an arrow unless their shared choices coexist.  The
even tap is joined only on the complete literal source state, unless an
extra common choice has explicitly been declared persistent.

## 2. Exact orbit-flow lemmas

### Theorem 2.1 (orbit circulation with balances and quotas)

Let a finite group `Gamma` act on a finite directed multigraph, preserving
tails, heads, parallel-arc identities, integral lower and upper capacities
`ell_a,u_a`, and an integral vertex balance `b_v`.  For every arc orbit `O`
and vertex orbit `K`, put

\[
 L_O=\sum_{a\in O}\ell_a,
 \qquad U_O=\sum_{a\in O}u_a,
 \qquad B_K=\sum_{v\in K}b_v.                         \tag{2.1}
\]

There is a full-network flow satisfying

\[
 \ell_a\le f_a\le u_a,
 \qquad
 \sum_{a:\,\operatorname{tail}(a)=v}f_a
 -\sum_{a:\,\operatorname{head}(a)=v}f_a=b_v        \tag{2.2}
\]

if and only if the orbit totals satisfy

\[
 \begin{aligned}
 L_O\le z_O\le U_O,\qquad
 &\sum_{O:\,\operatorname{tail}(O)=K}z_O
 -\sum_{O:\,\operatorname{head}(O)=K}z_O=B_K
 \quad(K\text{ every vertex orbit}).                 \tag{2.3}
 \end{aligned}
\]

Whenever (2.3) is feasible, the full network has an integral feasible flow.

#### Proof

Projection sends a full flow to

\[
                           z_O=\sum_{a\in O}f_a.       \tag{2.4}
\]

Summing (2.2) over a vertex orbit gives (2.3).  Conversely, from a quotient
solution define

\[
                           f_a={z_O\over |O|}
                           \qquad(a\in O).             \tag{2.5}
\]

The head and tail projections from an arc orbit to a vertex orbit are
equivariant surjections.  Every fibre therefore has the same size.  After
dividing the corresponding equation in (2.3) by `|K|`, (2.5) satisfies the
balance equation at every literal vertex.  Loops cancel on both sides.
The capacity bounds follow because capacities are constant on an orbit.

Thus the full rational flow polytope is nonempty.  Its constraint matrix is
a directed incidence matrix with bound rows and is totally unimodular, so
integral data give an integral feasible flow.  \(\square\)

Source, sink, demand, and exact successor-output quotas are represented by
ordinary capacity-faithful arcs with lower and upper bounds.  These quotas
must be invariant under the chosen residual stabilizer and occur as complete
arc orbits; an individually pinned quota requires first reducing the group.
Under that condition Theorem 2.1 includes the exact suffix-flow theorem and
also permits a successor bank to be required, not merely bounded above.

### Theorem 2.2 (orbit transportation and exact deficiency)

Let `H=(L,R;E)` be a capacity-faithful bipartite graph preserved by
`Gamma`.  Write its shore orbits as `L_i,R_j`, with sizes `l_i,r_j`, and
put `ij` in the orbit support graph exactly when `E(L_i,R_j)` is nonempty.
Then

\[
 \nu(H)=\max\left\{
  \sum_{ij}z_{ij}:
  z_{ij}\ge0,
  \sum_jz_{ij}\le l_i,
  \sum_iz_{ij}\le r_j
  \right\}.                                          \tag{2.6}
\]

In particular, `H` has a matching saturating `L` exactly when

\[
       \sum_{i\in I}l_i
       \le\sum_{j\in N(I)}r_j
       \qquad(I\text{ every set of left orbit indices}), \tag{2.7}
\]

and its exact deficiency is

\[
 |L|-\nu(H)=
 \max_I\left(
   \sum_{i\in I}l_i-
   \sum_{j\in N(I)}r_j
          \right)_+.                                  \tag{2.8}
\]

#### Proof

Every supported orbit block is biregular.  Spread `z_ij` uniformly over
the edges in that block.  Equations (2.6) give a fractional matching of the
same value in `H`, and bipartite-matching integrality gives a literal
matching.  The reverse inequality follows by projecting any matching to its
block counts.  Weighted Hall duality gives (2.7)--(2.8).  \(\square\)

Every physical capacity must be represented before applying either theorem.
An unaddressed target-value quotient, duplicated state copy, or hidden
edge-specific shared resource violates the hypotheses.

### Lemma 2.3 (arrow-orbit tail surjectivity)

Suppose one finite group `Gamma` acts on both shores and on `A_m^C`, and
the maps in (1.4) are equivariant.  For an arrow `a:x -> y`, let

\[
 H_a=\operatorname{Stab}(a),\quad
 H_x=\operatorname{Stab}(x),\quad
 H_y=\operatorname{Stab}(y).                          \tag{2.9}
\]

Then `H_a <= H_x,H_y`, and every representative of the state orbit
`Gamma x` is the tail of exactly

\[
                         [H_x:H_a]                    \tag{2.10}
\]

arrows in the arrow orbit `Gamma a`.  In particular, every nonempty arrow
orbit projects surjectively onto its source-state orbit.

#### Proof

The arrow orbit has size `[Gamma:H_a]`, the source orbit has size
`[Gamma:H_x]`, and the equivariant source projection has constant-size
fibres.  Their ratio is (2.10).  \(\square\)

This elementary lemma is the weakest outer induction principle.  A full
transportation flow on the complete state-transition graph is stronger: by
Theorem 2.2 it gives a one-copy matching saturating every active source
state.

## 3. The finite marked quotient state

A finite quotient at each fixed `m` is automatic and proves nothing about
induction.  The required object is one finite graded alphabet `Q`, independent
of `m`, together with finitely many marked arrow templates.  When the
deadline is a fixed function of the level, the external clock is `(m,d_m)`
and is not copied into the finite state.  If its update is not determined by
the level, the required finite residue/update type belongs in `q`; an
arbitrary unbounded deadline register cannot be hidden in the clock.

One explicit proof-safe state schema is

\[
              q=(\theta,\overline\Xi,\lambda,\varepsilon). \tag{3.1}
\]

Its coordinates have the following meanings.

1. `theta` is a finite framed residual-schema type.  From `(m,theta)` it
   generates, after all compensation, anchor, reservation, and terminal
   choices which precede a gate have been fixed, the complete addressed
   node-split networks and occurrence graphs.  It records vertex and arc
   orbit types, parallel arcs, source and terminal arcs, orbit support, and
   exact orbit-capacity laws.
2. `bar Xi` is a finite **compositional congruence** class of the complete
   persistent state (1.1), including topology, voltage, history, source,
   witness, compiler, residence, and protected-address data.  Equality of
   two quotient labels must have the fibre-product lifting property needed
   to concatenate literal representatives.
3. `lambda` is the finite frame, stabilizer, transporter, and continuation-
   holonomy type.  It records the common interface action on parent and
   child and the authenticated successor conjugacy.  A quotient loop with
   nontrivial address voltage is accepting only when that voltage lies in
   the declared conjugacy.  For a rolling fresh-pair construction it also
   records the change-of-group certificate which turns the output carrying
   the old `C_k` action into a next-action-admissible state for `C_(k+2)`.
4. `varepsilon` is the complete relative-orbit/transporter type of the
   bounded exported exception carrier.  A literal representative still
   carries every actual address, flag, history, and future deletion-guard
   datum needed to replay those exceptions; the finite symbol records their
   full isomorphism type relative to the frame.  Its support is bounded by
   one absolute constant and the transition replaces it rather than
   adjoining a new copy.  If these relative types are not drawn from a
   finite alphabet, (3.1) is not a finite state.

For every object or arrow template, the number of literal vertex and arc
orbits is uniformly bounded, and their multiplicities and capacities are
fixed functions of the external clock.  This is a finite **symbolic** state:
large orbit multiplicities are generated from `m`, not stored as an
unbounded word.

Each object type also carries a finite level-generation schema for its
possibly separate even-terminal extension, including its pinned terminal
network, omitted-family construction, and repair-charge rule.

The Markov condition is load-bearing.  If two literal states have the same
type `q`, every future arrow/tap schema obtained after fixing their declared
frames must be equivariantly isomorphic, or an authenticated transporter
must identify them.  If a future deletion guard distinguishes two fibres,
they are different states.

An arrow type `e:q -> q'` additionally retains finite level-generation
schemas for:

* the source, target, and arrow stabilizer types and their inclusions;
* one common-child type and every choice shared by the successor and odd
  terminal;
* finite orbit templates for the state-expanded regenerative and odd-
  terminal networks, with exact orbit-sum capacities;
* the rooted carrier/Euler chronology and complete continuation holonomy;
* an integral-output rule proving that at least one integral lift has an
  authenticated target of type `q'`; and
* generation of the literal odd omitted family and its repair-charge label.

The finite alphabet stores these schemas, not an unbounded literal word,
chronology, or omitted family.  At level `m` the schema generates the exact
literal objects, which remain part of the certificate.

An integral maximum flow need not be invariant and need not realize a
chosen vector of orbit totals.  Therefore the integral-output rule cannot
be replaced by the assertion that the fractional orbit flow is symmetric.

## 4. When an arrow or even-tap template is open

Fix a representative arrow template only after its common child,
compensation linkage, cap/guard state, reservations, rooted chronology, and
candidate successor frame have been fixed.  Quotient its residual networks
by the stabilizer of this fully pinned template, not by an ambient parent
group which moves one of those objects.

Let `D_reg` be the total persistent demand in a capacity-faithful
state-expanded regenerative network.  Its necessary flow row is

\[
                         F_{\rm orb}^{\rm reg}=D_{\rm reg}. \tag{4.1}
\]

The network includes exact output quotas for the successor state.  If the
regenerative gate is factored into router, suffix, compiler, and ray pieces,
the proof must either reserve disjoint resources between those pieces or
put them in one common network.  Separate marginal optima are not additive
when they compete for one physical capacity.

For either terminal parity `pi`, after its final word/order, cap state,
reference matching, and complete damage set have been fixed, let

\[
 \delta_\pi=D_\pi-F_{\rm orb}^\pi.                   \tag{4.2}
\]

More generally one may use the exact residual-gate vector

\[
 (\delta_{\rm rt},\delta_{\rm suf},\delta_{\rm comp},
      \delta_{\rm ray},e_{\rm other})_\pi,            \tag{4.3}
\]

provided every gate is formed in the same pinned terminal state and every
cross-gate reservation is explicit.  The terminal requirement is a literal
repair inequality

\[
 \tau_\pi
 =c_\pi+R(\mathcal H_\pi)
 \le C_\pi,                                           \tag{4.4}
\]

where `H_pi` is the omitted family produced by that same selected integral
lift.  A bound on (4.2) or (4.3) implies (4.4) only through a stated repair
theorem.

### Theorem 4.1 (open-arrow lift)

An arrow template produces a literal odd-decorated arrow if there exists
**one** integral physical witness `Pi_odd` satisfying all of the following
simultaneously:

1. the persistent network satisfies the full quotient row (4.1), or its
   exact unserved identities are exported as `varepsilon'` with
   `|varepsilon'|<=C_s`;
2. in the sidecar case, the full augmented network, including input and
   output sidecar quotas, is saturated and the target type records
   `varepsilon'`;
3. the odd terminal produced by `Pi_odd` satisfies (4.4);
4. every choice shared by the transition and odd terminal is encoded in one
   joint state-expanded network, or a proved rectangular/disjointness lemma
   shows that their integral lifts combine into this same `Pi_odd`;
5. the packets selected by `Pi_odd` have the declared rooted chronology and
   their full
   continuation holonomy lies in the authenticated successor conjugacy; and
6. the literal output of `Pi_odd` lands in the declared active target type.

The joint quotient program must contain every invariant lower bound,
balance, source/terminal arc, and successor-output quota.  If chronology is
not itself encoded in the state-expanded network, clause 5 is a condition on
the same selected lift, not a separate existential assertion.

#### Proof

Theorems 2.1--2.2 supply an integral lift of the joint capacity-faithful
program.  The hypothesis chooses a lift `Pi_odd` which simultaneously meets
all nonnetwork rows; no marginal lift is substituted for it.  Clauses 1--2
close every persistent obligation, including the carried sidecar.  Clauses
3--4 give the odd terminal on the same co-instantiated child.  Clause 5
serializes the unordered physical selection and authenticates its complete
boundary action.  Clause 6 supplies the literal next state.  These data are
exactly an odd-decorated arrow as defined in Section 1.  \(\square\)

### Theorem 4.2 (even-tap lift)

A complete source state has an even tap of charge at most `C_even` if one
separate integral physical witness `Pi_even`, formed after all of its
terminal-only choices are fixed, satisfies the exact even occurrence,
supplier, compiler, chronology, damage, omitted-family, and repair rows,
including (4.4).  Quotient flow or matching may produce `Pi_even` through
Theorems 2.1--2.2 only when those rows are encoded in one capacity-faithful
state-expanded program or joined by a proved rectangular/disjointness
lemma.

The witness `Pi_even` need not equal `Pi_odd`.  The two witnesses meet on the
complete literal source state and on every datum declared persistent; their
terminal-only extensions may differ.

Bounded persistent deficiency without clause 2 is not a weak version of
regeneration.  If the input sidecar has size at most `C_s`, the output
sidecar must again have size at most `C_s`; the old and new defects are not
united.

## 5. Tap-decorated orbit-quiver induction

For every level `m`, let `Q_m^*` be a nonempty collection of active complete
literal state **orbits**, each labelled by one of the finitely many object
types and even-open in the sense that **every literal representative** has
an even tap from Theorem 4.2.  It is enough to exhibit one invariant
even-tap certificate orbit with an equivariant, hence surjective, source
projection onto the state orbit.  An active arrow is an
odd-open template from Theorem 4.1 whose source orbit is in `Q_m^*` and
whose target orbit is in `Q_(m+1)^*`.  Assume, at every level, that the
complete active arrow relation is invariant under one common finite
interface action on the two shores, as in Lemma 2.3.  A type representing
several unrelated literal orbits must verify the following rows for each
orbit separately.

The minimal top-level hypothesis is simply one selected infinite path
through these active literal relations.  Neither left-totality nor a
simultaneous matching of all states is logically necessary.  The next
theorem gives two stronger finite-quotient mechanisms which produce such a
path.

### Theorem 5.1 (same-parity quotient induction)

Assume one absolute terminal-charge bound `C_tap` and, for every
`m >= m_0`, either of the following outer rows.

1. **Left-total support:** every active object orbit has a nonempty active
   arrow orbit leaving it; or
2. **Full state transportation:** in the complete active state-transition
   graph, with current object-orbit sizes `a_i(m)` and next object-orbit
   sizes `b_j(m+1)`, the finite transportation system

   \[
      z_{ij}\ge0,\qquad
      \sum_jz_{ij}=a_i(m),\qquad
      \sum_iz_{ij}\le b_j(m+1)                       \tag{5.1}
   \]

   is feasible on the active arrow support.

Then every literal active state at level `m_0` lies on an infinite
compatible odd spine

\[
                    g_{m_0}\to g_{m_0+1}\to\cdots,   \tag{5.2}
\]

and every `g_m` has literal odd and adjacent-even terminal certificates of
charge at most `C_tap`.  Consequently the bounded-charge reset-spine theorem
gives an absolute constant `C_*`, with `C_* >= C_tap`, such that

\[
                         \nu(k)\le B(k)+C_*           \tag{5.3}
\]

for all `k`; `C_*` absorbs the finite initial range once.

#### Proof

Under row 1, Lemma 2.3 transports one displayed active arrow to every
literal representative of its source orbit.  Its target lies in the next
active collection.  Recursive choice produces (5.2).

Under row 2, Theorem 2.2 gives a literal matching saturating every active
source state.  In particular the active relation is left-total, so the
previous argument applies.  Every selected odd-open arrow supplies the
joint successor/odd-terminal certificate, and every active source state is
even-open.  Thus both terminal branches have the same uniform charge bound.
The reset-spine implication gives (5.3).  \(\square\)

Full state transportation is stronger than needed for one spine.  It is
useful when a simultaneous one-copy successor assignment or a reversible
state ensemble is required.

A stationary finite quotient graph need not have a literal periodic lift.
Its infinite path is sufficient.  To assert a literal return, the product
of its transporter/holonomy labels must meet the authenticated return
relation.

## 6. Bounded-to-full promotion on a free bulk

### Theorem 6.1 (free-orbit rigidity)

Suppose a cyclic group `C_mu` acts freely on every addressed left and right
vertex orbit of an invariant bipartite gate.  Its exact matching deficiency
is a nonnegative multiple of `mu`.

For the flow statement, fix one invariant node-split source--sink network.
The source and sink are bookkeeping fixed points, while the full demand is
the total capacity of complete free source-port arc orbits.  Require free
action on every port, sink-terminal, internal addressed vertex, and every
finite-capacity arc orbit, including source, terminal, and node-split arcs.
Every nonzero lower bound, finite upper bound, balance, and exact quota in
the maximized bulk program must have orbit total divisible by `mu`; all
nonfree quota arcs are excluded into the boundary state.  Then both the full
demand and maximum flow value are multiples of `mu`, so the exact flow
deficiency is a nonnegative multiple of `mu`.

Consequently, a nonnegative sum of such deficiencies which is strictly less
than `mu` is zero term by term.

#### Proof

Divide every orbit size and orbit capacity by `mu`.  The transportation and
network-flow quotient programs become integral programs on the free-orbit
quotient.  Their optimal values, and hence the differences from the full
shore or source capacities, are multiples of `mu`.  A nonnegative multiple
of `mu` below `mu` is zero.  \(\square\)

### Corollary 6.2 (bounded-to-full same-parity induction)

Assume the finite marked quotient of Section 3 has a nonempty **candidate
core** of complete state orbits.  At every level and from every candidate
source orbit, choose at least one candidate arrow template into the next
candidate core.  The source state also has a candidate even-tap template.
That even template is required for every literal representative, or is one
invariant certificate orbit with surjective source projection.
Suppose one common cyclic interface group of order `mu_m` preserves each
fully pinned parent/child candidate and:

1. either the complete augmented persistent bulk is one capacity-faithful
   free-orbit program with exact deficiency at most one absolute `D`, or it
   has a proved resource-disjoint product decomposition into free-orbit
   gates whose nonnegative deficiencies sum to at most `D`;
2. every displayed free-bulk gate satisfies Theorem 6.1 and
   `mu_m -> infinity`;
3. every nonfree boundary/sidecar factor is saturated exactly and fully
   replaced, and either is capacity-disjoint from the free bulk or is fixed
   first, after which its consumed capacities are deleted and the residual
   bulk is still invariant and free; a coupled program containing nonfree
   capacity is allowed only under a separate theorem proving its claimed
   divisibility;
4. one joint physical lift satisfies the rooted chronology, holonomy,
   integral-output, and odd-repair rows of Theorem 4.1; and
5. a possibly separate lift satisfies the even-tap rows of Theorem 4.2,
   with uniform charge.

Then for all sufficiently large `m`, every persistent free-bulk gate is
fully saturated.  The arrows are open, Theorem 5.1 produces the odd spine
and both taps, and (5.3) follows.

#### Proof

For `mu_m>D`, Theorem 6.1 forces the joint bulk deficiency, or every
nonnegative deficiency in the disjoint factorization, to be zero.  Clause 3
closes the remaining persistent boundary exactly.  Clauses 4--5 make each
chosen candidate arrow odd-open and each source orbit even-open.  Hence the
candidate core becomes left-total in the sense of Theorem 5.1.  Apply that
theorem.  \(\square\)

The group in Corollary 6.2 must act on **both** levels and on the complete
arrow template.  Independently using `C_(2m+1)` on the parent and
`C_(2m+3)` on the child does not define such an action.  One needs a common
fresh-pair/interface stabilizer.  An action-groupoid or biset can replace the
common group only after a separate orbit-fibre and divisibility theorem has
been proved for it; Theorems 2.1--2.2 do not supply that extension.  The
surviving modulus is the order of the actual residual stabilizer, not the
ambient coordinate-rotation order.

The same promotion may be applied to the outer active state graph if its
complete addressed state orbits are free under a common `C_(mu_m)`.  A
uniformly bounded outer matching deficiency then becomes zero for large
`m`, giving row 2 of Theorem 5.1.  Without this divisibility, bounded outer
deficiency is not enough.

### 6.3 Fresh-pair common-period growth

The arithmetic in this subsection folds the pure core of
`MATH_THEOREM_FRESH_PAIR_COMMON_STABILIZER_GROWTH_20260803.md`, frozen for
this audit at SHA-256
`2ebf63c7d25dbc95aa51fe79e46a9798f31bc8343b9b45479e0e90f3a733b22d`.
The regenerative interface below is stated more strongly than that note's
Corollary 6.1: persistent exceptions are replaced in the successor, whereas
only terminal-only exceptions may be paid once.

Let

\[
                         k=2r-1,
\]

let `C_k` rotate the `k` old coordinates, and let it fix two labelled fresh
coordinates `u,v`.  This is one common action on the parent and child of a
single `k -> k+2` arrow.

### Lemma 6.3 (old-subset period)

If `S subseteq [k]` has rank `s=r+a`, then its `C_k`-orbit order satisfies

\[
 |C_kS|
 \ge {k\over\gcd(k,s)}
 = {k\over\gcd(k,2a+1)}
 \ge {k\over|2a+1|}.                                 \tag{6.1}
\]

The denominator never vanishes.  In particular, the ranks `r-1,r` are
free, and every old rank with `|s-r|<=D` has period at least

\[
                         {k\over2D+1}.                \tag{6.2}
\]

#### Proof

If the stabilizer of `S` has order `h`, its action on `[k]` is free and `S`
is a union of `h`-element coordinate orbits.  Hence `h` divides both `k` and
`s`, so `|C_kS|=k/h>=k/gcd(k,s)`.  Since
`2s-k=2a+1`, Euclid gives `gcd(k,s)=gcd(k,2a+1)`.
Equation (6.2) follows from `|2a+1|<=2D+1`.  \(\square\)

On the child ground `[k] union {u,v}`, the two middle ranks are `r` and
`r+1`.  Their old-rank offsets, as the fresh occupancy varies, are

\[
 \{0,-1,-2\},\qquad \{1,0,-1\}.                     \tag{6.3}
\]

Thus every fresh-occupancy sector in both child middle shores has period at
least `k/3`.  If only one fixed fresh coordinate is added for the adjacent
even tap, its central-rank sectors have offsets `0,-1` and are free.

### Lemma 6.4 (addressed inheritance and residual subgroup)

Let an addressed object `omega` have a literal equivariant old-subset
projection

\[
                 S(g\omega)=gS(\omega)\qquad(g\in C_k). \tag{6.4}
\]

Then

\[
 \operatorname{Stab}_{C_k}(\omega)
 \subseteq \operatorname{Stab}_{C_k}(S(\omega)),
 \qquad
 |C_kS(\omega)|\mid |C_k\omega|.                    \tag{6.5}
\]

More generally, let `H_k <= C_k` be the actual residual subgroup stabilizing
the fully pinned materialized arrow: child, compensation linkage,
root/common-basis/cap, guards, reservations, protected pins and signature,
chronology constraints, and successor quotas.  If `h_k=|H_k|`, then

\[
 |H_k\omega|
 \ge {h_k\over\gcd(k,r+a)}
 \ge {h_k\over|2a+1|}.                               \tag{6.6}
\]

#### Proof

Equivariance gives the stabilizer inclusion.  In a cyclic group, subgroup
inclusion implies the orbit divisibility in (6.5).  For (6.6),
`Stab_(H_k)(omega)` is contained in
`H_k intersect Stab_(C_k)(S(omega))`, whose order is at most
`gcd(k,r+a)`.  Apply orbit--stabilizer and Lemma 6.3.  \(\square\)

Adding literal address data therefore cannot shorten an orbit.  Forgetting
or coalescing the old label, using a shared capacity without a unique
address, or choosing a nonequivariant canonical representative is a
coarsening, not address enrichment, and receives no such bound.

### Lemma 6.5 (exact-period defect divisibility)

Fix an exact orbit order `q` under the cyclic residual group `H_k`.  Suppose
a complete gate is `H_k`-invariant: its shore or vertex sets, incidence
relation, arcs, capacities, balances, lower and upper bounds, and quotas are
transported equivariantly and occur in complete `H_k`-orbits.  Suppose
a capacity-faithful matching gate has both addressed shores, and every
capacity gadget not already represented by a shore vertex, in
exact-period-`q` orbits.
Suppose a node-split flow gate has every port, supplier sink, internal
addressed vertex, source/terminal arc, node-split arc, and other finite
physical capacity in exact-period-`q` orbits; its source and supersink may be
fixed bookkeeping vertices.  All lower bounds and quotas occur in complete
invariant orbits.

Then the matching deficiency and flow corank are nonnegative multiples of
`q`.

#### Proof

Every exact-period-`q` object has the same stabilizer: the unique subgroup
of `H_k` of order `h_k/q`.  After quotienting by that kernel, `C_q` acts
freely on every addressed shore or finite-capacity object.  Apply Theorem
6.1.  \(\square\)

### Theorem 6.6 (central-band period-stratified promotion)

Let the persistent bulk of one fully pinned arrow be a capacity-faithful
direct sum of invariant exact-period gates covered by Lemma 6.5, or by a
separately stated exact `q`-divisibility theorem.  Gates of different
periods share no finite physical capacity.  Gates within one fixed period
may be combined in one joint program only when the compound remains an
invariant capacity-faithful bipartite-matching gate or directed node-split
flow gate covered by Lemma 6.5 and remains `q`-pure.  Any other joint integer
or hypergraph program requires its own exact `q`-divisibility theorem;
common period alone is not enough.

Suppose every nonbookkeeping addressed object has an equivariant projection
whose old rank lies in `|s-r|<=D(k)`, and every period-stratum deficiency is
at most one absolute `C`.  Put

\[
                 \mu_k={h_k\over2D(k)+1}.             \tag{6.7}
\]

If `mu_k>C`, every period stratum saturates exactly.  In particular this
holds eventually when `h_k/(2D(k)+1) -> infinity`; under the full fresh-pair
action `h_k=k`, any band `D(k)=O(sqrt(k))` has
`mu_k=Omega(sqrt(k))`.

#### Proof

Lemma 6.4 gives `q>=mu_k` in every displayed stratum.  Lemma 6.5, or the
separately stipulated divisibility theorem, makes its deficiency a
nonnegative multiple of `q`.  A multiple of `q` bounded by `C<mu_k<=q` is
zero.  Capacity separation lets the literal integral solutions coexist.
\(\square\)

The conclusion is simultaneous over all rank and period strata; their
number need not be bounded.  This is not a finite-state theorem.  Even one
free middle-rank period contains exponentially many literal subset orbits.
A fixed symbolic generator and finite congruence with exact support and
capacity laws remain separate hypotheses of Section 3.

### Corollary 6.7 (fresh-pair promotion of a selected arrow)

Fix either one compatible selected quotient path or a recurrent left-total
candidate core.  For every sufficiently large odd `k`, assume every
candidate arrow used by that path or core satisfies all of the following.

1. After every **pre-gate** persistent choice shared by the successor and
   odd terminal has been fixed, the complete parent/child gate instance is
   invariant under the residual subgroup `H_k` of the common fresh-pair
   action.  The later integral lift may break symmetry, but its literal
   output must satisfy clause 6.
2. Every persistent matching/flow bulk gate has the exact-period direct-sum
   representation of Theorem 6.6.  A capacity-faithful claim-to-port router
   and its suffix network occur in the same period summand or in explicitly
   disjoint summands whose exact composition theorem is supplied.  A coupled
   summand is itself a gate covered by Lemma 6.5, or has a separate exact
   `q`-divisibility theorem.
3. Every bulk object has the equivariant central-band projection of Lemma
   6.4, and every period-stratum deficiency is at most one uniform `C`, with
   `h_k/(2D(k)+1) -> infinity`.
4. Every persistent object outside the period-pure bulk is either saturated
   exactly or exported as the bounded typed sidecar and **replaced**, not
   accumulated, in the authenticated successor.  After fixing it and
   deleting its consumed capacities, the residual period strata remain
   invariant and capacity-disjoint.
5. Every terminal-only exceptional object has a uniform literal repair or
   target-bypass charge.
6. The same selected integral lift satisfies co-instantiation, rooted
   chronology, continuation holonomy, and literal output authentication.
   Its target is next-action-admissible: after the declared reframe it has
   the fully pinned `C_(k+2)` candidate action required by the next arrow.
7. The remaining open-arrow rows of Theorem 4.1 and the even-tap rows of
   Theorem 4.2 hold.

Then every persistent period-pure matching/flow gate is exact for all
sufficiently large `k`.  The chosen candidate arrows are odd-open, their
source states are even-open, and the selected path or recurrent core yields
the same-parity spine and both taps.

#### Proof

Theorem 6.6 closes every period-pure bulk gate.  Clause 4 closes every
persistent exception without accumulation, clause 5 prices only terminal
exceptions, and clauses 6--7 supply the remaining joint-arrow and tap data.
If a selected path was supplied, it is already the compatible reset spine.
Otherwise the candidate core becomes left-total, and Theorem 5.1 supplies
the path.  \(\square\)

The old-coordinate `C_k` action fixes the fresh pair and is not the full
child rotation `C_(k+2)`.  Clause 6 is therefore an additional regenerative
change-of-group theorem, not a consequence of period growth.  Likewise,
Theorem 6.6 is an inner-gate promotion.  It applies to outer state
transportation only if the complete outer relation has its own
capacity-faithful same-period decomposition and uniform per-period defect
bound.  Growing state-orbit sizes or bounded aggregate outer deficiency do
not suffice.

## 7. Why this is a finite proof target

For a fixed arrow type, the quotient graphs and networks have bounded size.
Full or `C`-bounded suffix flow is equivalent to the finite family of
quotient cut inequalities

\[
            \operatorname{cap}_{m,e}(U)
              \ge D_{m,e}-C                           \tag{7.1}
\]

over quotient source--sink cuts `U`.  Full orbit transportation is
equivalent to the finite weighted Hall family

\[
       \sum_{i\in I}a_i(m)
       \le\sum_{j\in N(I)}b_j(m+1)                   \tag{7.2}
\]

over subsets of the finite object-orbit index set.  With the convention
`out-in=B`, lower/output quotas use Hoffman's equally finite circulation
conditions

\[
 \sum_K B_K=0,
 \qquad
 B(S)\le U(\delta^+(S))-L(\delta^-(S))               \tag{7.3}
\]

for every quotient vertex subset `S`; the complementary subset supplies the
reverse inequality.

Thus, if the quotient topology/support is eventually fixed or periodic, all
periods have a finite common multiple, and all orbit multiplicities and
capacities are eventually polynomial or quasipolynomial functions of one
controlled external clock, the all-dimensional flow row reduces to finitely
many algebraic inequalities, one finite family for each residue class.  A
second clock such as an independently varying deadline needs its own finite
admissible-domain theorem, and the finite initial range remains separate.
This is a finite symbolic proof programme; it is not a license to infer
literal networks or state congruence from their counts.

The genuinely new construction target is therefore:

> Find one fixed finite marked quotient alphabet, prove its complete-state
> congruence and exact level-dependent capacity laws, and exhibit a nonempty
> selected infinite quotient path, or a recurrent left-total core, whose
> odd-decorated arrows satisfy full regenerative quotient flow and bounded
> odd terminal repair, and whose source states all admit bounded even taps.

If the free-bulk hypotheses are available, it is enough to prove one
uniform deficiency bound below the growing residual orbit modulus; exact
bulk saturation then follows automatically.

## 8. Sharp caveats and obstructions

1. **Finite at each level is tautological.**  The number of orbit types,
   their incidence templates, and the state congruence must be uniform in
   `m`.
2. **Use the residual stabilizer.**  Compensation deletion, a root, seam,
   opening, pin, or reserved cell can destroy the parent action.  Quotienting
   by a group which moves the fixed residual state is invalid.
3. **Integral does not mean equivariant.**  The quotient theorems return
   some integral physical lift, usually symmetry-breaking.  An invariant
   integral flow on a unit arc orbit requires `z_O in |O| Z`.  An invariant
   one-out arrow orbit requires `H_a=H_x`; invariant one-in-one-out also
   requires `H_a=H_y`.  No invariant lift is needed for Theorem 5.1, but its
   literal output type must be exported.
4. **Bounded outer deficiency need not compose.**  Let
   `X_m={0,1}`.  On even `m` retain only `0 -> 0`; on odd `m` retain only
   `1 -> 1`.  Every layer has matching deficiency one, yet no path has two
   edges.  One needs full row saturation or an explicitly closed recurrent
   core.
5. **Marginal flows do not co-instantiate.**  If transition and odd tap
   share a capacity or selector, they belong to one joint state-expanded
   network unless a rectangular/disjointness theorem factors them.
6. **Flow does not create chronology.**  A matching is an unordered
   packing.  Rooted carrier order, continuation-state composition, and
   accepted holonomy remain arrow data.  A quotient cycle with unauthenticated
   address voltage is not a return.
7. **Orbit labels are not physical capacities.**  Parallel arcs, node-split
   rows, occurrence addresses, and every edge-specific shared resource must
   survive the quotient.  Otherwise Theorems 2.1--2.2 do not apply.
8. **Primitive option selection may be nonnetworkal.**  Three-role parity
   coupling, donor deletion, and mutual support can make the preselection a
   hypergraph-packing problem.  Orbit flow begins only after exact compound
   columns or capacity-faithful gadgets have been materialized.
9. **History is not erased by symmetry.**  Orbit matching may choose a new
   oldest history label relationally, but that literal label or its
   authenticated lift orbit must be exported.  Forgetting it is not a
   congruence when future deletion guards distinguish the fibres.  A small
   orbit catalogue does not make a growing history register physically
   bounded; a guarded reset/replacement theorem is still required.
10. **Terminal deficiency is not terminal charge.**  The omitted family,
    final word, compiler damage, and repair word must be fixed before (1.2)
    is bounded.

## 9. Exact remaining hypothesis

The orbit-quotient principle turns the same-parity problem into a finite
state problem only after the following statement is proved.

> **Tap-decorated finite-orbit reset lemma (UNPROVED).**  There are a fixed
> finite marked quotient alphabet `Q`, exact level-dependent orbit-capacity
> laws, and one uniform terminal-charge bound, together with either a
> selected infinite quotient path or a nonempty recurrent left-total core.
> Every selected step has an open odd-decorated arrow to the next level,
> using one common materialized child for the successor and odd terminal,
> full augmented regenerative flow, authenticated rooted chronology and
> continuation holonomy, and exact replacement of its bounded exception
> carrier.  Every selected source state also has a possibly separate even
> terminal certificate of bounded literal repair charge.

The lemma is sufficient by Theorem 5.1.  Current results do not prove:

* a uniform finite congruence for the growing history/witness/compiler
  state;
* a residual common interface subgroup with
  `h_k/(2D(k)+1) -> infinity` and bounded orbit-schema complexity;
* one-child capacity-faithful compound columns before quotienting;
* either full persistent flow or a capacity-separated `q`-pure gate
  decomposition with a uniform per-period defect bound to which Theorem 6.6
  applies;
* an authenticated literal output type after the symmetry-breaking integral
  lift; or
* a recurrent active core with both terminal parities.

Accordingly, this note proves a new exact conditional induction and a
finite symbolic target, but no unconditional `B(k)+O(1)` theorem.
