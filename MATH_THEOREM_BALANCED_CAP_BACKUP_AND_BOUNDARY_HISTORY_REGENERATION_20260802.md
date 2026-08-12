# Balanced cap backups and boundary-history tickets for regenerative heptagonal descent

**Date:** 2026-08-02  
**Status:** exact cap-reserve/cut theorem, exact finite-history interface, and
conditional packing/descent theorem.  The prospective heptagon count by itself
does not prove the host-spread hypothesis below.  No residence completion,
source factor, compiler, or universal word is claimed.

## 0. Outcome

The heptagonal circulation theorem changes the location of the missing
all-dimension argument.

For a fixed rooted defect in the central regime `r=k/2+O(1)`, the cap-exact
phasewise `C14` atlas has

\[
 N_{k,r}=(r-1)(r-2)(k-r)_4(k-r-4)=\Theta(k^7)             \tag{0.1}
\]

prospective labelled tickets, and every nonanchor central token has load
`O(k^6)`.  For fixed coprime voltage in the same regime, seven-run sockets
are even more numerous: through a fixed deleted boundary coordinate their
raw prospective multiplicity contains

\[
 {r-1\choose6}{k-r-1\choose6}(7!)^2\,\Omega(k)^7.         \tag{0.2}
\]

Neither formula is a frozen-factor neighbourhood theorem.  In particular,
nonzero holonomy obstructs the naive fixed-label cap rotor.  A usable
developed packet must carry a nontrivial cap permutation, spend and replant
duplicate cap units, or close its cap debt only in a larger terminal return.

The exact recursive atom is therefore not a bare `C14`.  It is a
**cap/history macro-ticket** carrying

\[
 \bigl(\delta^{\rm cap},\beta^{\rm cap},h,
       \{\Sigma_d(P_i)\}_{i=0}^6,
       \mathcal R_d^+,\mathcal R_d^-,\mathbb W_{q,d},
       \text{topology/opening},\text{protected resources}\bigr). \tag{0.3}
\]

This note proves:

1. terminal cap safety is exactly a family of reserve-cut inequalities;
2. every safe cap transfer is a collection of reserve-token paths and
   cycles, so “balanced backup planting” has a literal flow meaning;
3. the recursive residence socket consists of labelled forward/reverse
   absolute ear matrices and the signed old-versus-new macro relation, not
   merely the aggregate endpoint drift;
4. the audited Pascal pivot resets the positive insertion history after its
   triangular entrance guard; a full bi-history reset additionally requires
   a separately supplied literal deletion-history dual/reversed reset with
   its own entrance domain;
5. a complete physical host-spread hypothesis with `Theta(k^7)` lists and
   `O(dk^6)` conflict load gives a rigorous greedy packing and regenerative
   descent theorem.

Thus the next mathematical target is balanced duplicate-cap backup planting
**jointly with** boundary-history tickets.  Raw central packet abundance is
no longer the missing row.

## 1. Exact cap-reserve circulation

Work first with literal physical cap keys.  Let `M_F(U)` be the number of
selected row occurrences whose immediate-upper cap is `U`, and assume the
current factor is cap-complete:

\[
                         M_F(U)\ge1.                     \tag{1.1}
\]

For a terminal compound packet `Q`, let `a_Q(U)` and `b_Q(U)` be the numbers
of removed and inserted row occurrences with cap `U`.  Put

\[
 \delta_Q(U)=b_Q(U)-a_Q(U),\qquad s_F(U)=M_F(U)-1.        \tag{1.2}
\]

Equivalently, draw one directed cap-transfer arc `U -> V` for every row
replacement whose old and new caps are `U` and `V`.  For a union of packets,
let `D` be the resulting directed multigraph.  Then

\[
 \delta_D(U)=\operatorname{in}_D(U)-\operatorname{out}_D(U). \tag{1.3}
\]

### Theorem 1.1 (terminal reserve cuts)

The terminal compound is cap-support exact if and only if any, hence all, of
the following equivalent systems hold:

\[
 M_{F^Q}(U)=M_F(U)+\delta_Q(U)\ge1
             \qquad\text{for every }U,                  \tag{1.4}
\]

\[
 \operatorname{out}_D(U)-\operatorname{in}_D(U)
                    \le s_F(U)\qquad\text{for every }U,  \tag{1.5}
\]

and

\[
 \operatorname{out}_D(S)-\operatorname{in}_D(S)
                    \le s_F(S)\qquad\text{for every }S,  \tag{1.6}
\]

where only arcs crossing the shore `S` are counted and
`s_F(S)=sum_(U in S)s_F(U)`.

If the packet removes and inserts the same number of rows, then

\[
             \sum_U s_{F^Q}(U)=\sum_U s_F(U).             \tag{1.7}
\]

Cap-multiset equality is the strictly stronger condition

\[
                         \delta_Q(U)=0\quad\text{for all }U. \tag{1.8}
\]

#### Proof

Equation (1.4) is the literal load update.  Substituting (1.2)--(1.3) gives
(1.5).  Summing (1.5) over `U in S` cancels the internal arcs and gives
(1.6); conversely (1.6) applied to singletons gives (1.5).  Equal numbers of
old and new rows give `sum_U delta_Q(U)=0`, which proves (1.7).  Equality of
the old and new cap multiplicity vectors is exactly (1.8).  \(\square\)

The shore form (1.6) is useful for a terminal-commit circulation, but it does
not impose a legal sequential order.  A directed cycle on all-tight caps
satisfies every terminal cut and still creates a cap hole after its first
primitive unless the cycle is committed simultaneously or the temporary
debt is stored in the lifted state.

### Theorem 1.2 (reserve-token path decomposition)

Every cap-transfer multigraph `D` decomposes into directed cycles and
directed paths whose initial vertices are precisely the positive-divergence
copies

\[
 d_D(U)=\operatorname{out}_D(U)-\operatorname{in}_D(U)>0 \tag{1.9}
\]

and whose terminal vertices are the negative-divergence copies.  The
terminal cap cuts hold exactly when the `d_D(U)` path starts at `U` can be
injected into the `s_F(U)` old reserve units there.  Each path consumes one
old reserve unit at its start and plants one new reserve unit at its end;
cycles merely circulate row occurrences.

#### Proof

At every vertex, pair as many incoming and outgoing arc ends as possible.
Following paired ends decomposes all arcs into cycles and maximal paths.
The unpaired outgoing ends are counted by the positive part of `d_D`, and
the unpaired incoming ends by its negative part.  The number of required
path starts at `U` is therefore `d_D(U)_+`.  Inequality (1.5) is exactly
`d_D(U)_+<=s_F(U)` whenever `d_D(U)>0`; vertices of nonpositive divergence
need no old reserve.  At the other endpoint the load, hence the reserve,
increases by one.  \(\square\)

This gives a precise definition.

> A **balanced duplicate-cap backup certificate** for `Q` is the path
> decomposition of Theorem 1.2 together with the literal load witness
> `s_F(U)>=d_D(U)_+` at every path start.  For occurrence-level composition,
> it additionally designates a surviving old baseline occurrence outside the
> deleted support at every net-losing cap and records the new occurrences at
> path ends as the exported replacement reserve bank.

The word “balanced” refers to (1.7): reserve units are transported, not
created.  A protected untouched baseline occurrence at every net-losing cap
is a convenient literal certificate of support preservation.  It is not a
certificate of cap-multiset equality.

### Theorem 1.3 (ordered cap-debt monoid)

For an ordered packet word `P`, let `z_P` be its final cap-load change and
let

\[
 \beta_P(U)=\max_{0\le j\le |P|}
       \left(-\sum_{i=1}^j\delta_i(U)\right)_+          \tag{1.10}
\]

be its maximum prefix demand.  Let `mathbb W_P` be its exact **signed macro**
bi-history relation: it has value infinity on illegal old/new socket pairs
and otherwise stores `Phi_after-Phi_before`, including the
whole-component-token difference.  It is not an absolute ear-cost matrix.
For `A` followed by `B`, with `B` evaluated state-relatively after `A` (or
on a disjoint/additive literal ledger), the exact product is

\[
 (z_A,\beta_A,\mathbb W_A)(z_B,\beta_B,\mathbb W_B)
 =\bigl(z_A+z_B,
        \max\{\beta_A,\beta_B-z_A\},
        \mathbb W_B\otimes\mathbb W_A\bigr).            \tag{1.11}
\]

The product is associative.  Starting reserve `s_F` protects every physical
prefix exactly when `s_F>=beta_P`.  If `P` is one simultaneous terminal
symmetric difference, its minimal cap requirement is only

\[
                         (-z_P)_+,                      \tag{1.12}
\]

and requiring safety of a merely conceptual primitive ordering can create
artificial debt.

#### Proof

Prefixes of `AB` either lie in `A`, giving demand `beta_A`, or consist of
all of `A` followed by a prefix of `B`, giving demand `beta_B-z_A`.
Taking their coordinatewise maximum proves (1.11); min-plus composition of
signed state-transition relations is associative because the intermediate
potential cancels.  The load after a prefix `j` is
`1+s_F+z_(P,<=j)`, which proves the acceptance statements.  \(\square\)

For regeneration, terminal nonnegativity is not enough: the exported vector

\[
                         s_{F^P}=s_F+z_P                \tag{1.13}
\]

must lie in the declared recursive reserve class.  The strongest convenient
face is `z_P=0`; the authenticated `k=17` heptagon instead transports three
reserve units and must export their new locations.

If consumed and planted reserve units have recursive types, write `ell(u)`
for the consumed demand of type `u`, `a(v)` for the planted capacity of type
`v`, and let `Gamma` be the allowed type-transport graph.  An integral typed
assignment exists exactly when the capacitated Hall cuts

\[
 \sum_{u\in S}\ell(u)
       \le\sum_{v\in N_\Gamma(S)}a(v)
                         \qquad\text{for every type set }S       \tag{1.14}
\]

hold.  This Hall row applies only when backup clones genuinely have socket
menus and capacities.  For fixed passive backup occurrences, the
authoritative test remains (1.4) plus the untouched-occurrence check; adding
an invented matching layer would be stronger than the physical problem.

### Orbit qualification

Equations (1.1)--(1.9) are unconditional on literal physical caps.  They may
be compressed to one unweighted row per cap orbit only when those cap orbits
are free.  With a stabilizer, one must retain stabilizer-coset multiplicities
or work physically.  For ground size `2r-1`, rank-`(r+1)` cap orbits can have
nontrivial stabilizer when `gcd(2r-1,r+1)>1`; an unqualified one-unit-per-orbit
statement is therefore false in general.  The relevant `Z_17` cap action is
free.

## 2. Holonomy forces a cap permutation or a reserve bank

Assume in this section that the involved owner, facet, and cap orbits are
free.  Without freeness, use the literal physical development or retain the
appropriate stabilizer-coset multiplicities; the following unweighted
quotient statements must not be applied verbatim.

For a quotient `t`-row packet with phase increments `a_i`, put

\[
                         h=\sum_i a_i\pmod k.             \tag{2.1}
\]

The developed moving graph has `gcd(k,h)` circuits.  Exact cap-multiset
transport requires a row permutation `pi` and shifts `q_i` satisfying

\[
                         V_i=\rho^{q_i}U_{\pi(i)}.        \tag{2.2}
\]

Under the naive sequential fixed-label rule, (2.2) forces

\[
                         z_0=\rho^h z_0.                 \tag{2.3}
\]

On a free coordinate orbit, a nonzero coprime `h` violates (2.3).  Thus the
phasewise fixed-`z` heptagon supplies a uniform cap-multiset-exact subclass,
but a coprime-voltage development must instead use a nontrivial matching in
(2.2), a reserve certificate from Theorem 1.2, or a larger compound return.

The authenticated `2,822 -> 2,754` `k=17` `C14` has

\[
                         h=5\pmod {17}.                  \tag{2.4}
\]

It changes 51 net-lost and 51 net-gained physical cap values, hence three of
each in the free quotient.  The three old canonical cap-orbit representatives

\[
                         13783,\ 27447,\ 28075          \tag{2.5}
\]

have load two, and the three new canonical cap-orbit representatives

\[
                         13727,\ 28331,\ 43755          \tag{2.6}
\]

finish at load two.  Therefore it transports exactly three quotient reserve
units, or 51 literal units.  It is cap-support exact and one-cycle, but not
cap-multiset exact.  This is the finite model for balanced backup transport;
it is not a proof that such a reserve bank is available in every dimension
or at every reachable factor.

## 3. Exact boundary-history tickets

Fix residence depth `d`.  A retained path may later be used in either
orientation, so its recursive signature must be label-sensitive and
bidirectional.  Write

\[
 \Sigma_d(P)=\bigl(\mathbb A_P^+,\mathbb A_{P^\dagger}^+,
                    \mathbb A_P^-,\mathbb A_{P^\dagger}^-,
                    \partial P,\ell_d(P),K^+(P),K^-(P)\bigr). \tag{3.1}
\]

Here `mathbb A` is the ordinary nonnegative absolute tropical event-cost
matrix (infinity for an illegal pair), `partial P` stores the endpoint
frames and connector labels, `ell_d` is the length capped at the
largest value relevant to depth `d`, namely
`ell_d(P)=min{|P|,d+1}`, and `K^+`, `K^-` are the full coordinate bitsets
recording coordinates
constant-present or constant-absent on the path.  Those core sets are needed
for whole-component tokens if a compound move temporarily splits the factor.

For a heptagon with retained paths `P_0,...,P_6`, compose the signatures in
the old step-one order

\[
                         0,1,2,3,4,5,6                  \tag{3.2}
\]

and the new step-two order

\[
                         0,2,4,6,1,3,5,                \tag{3.3}
\]

including the literal old and new connector morphisms.  This gives separate
absolute composites `mathbb A_(q,d)^old` and `mathbb A_(q,d)^new`.  On an
actual old socket `omega` and declared new socket `omega'`, define the signed
macro relation

\[
 \mathbb W_{q,d}(\omega,\omega')=
   C_{q,d}^{\rm new}(\omega')-C_{q,d}^{\rm old}(\omega), \tag{3.3a}
\]

when both absolute composites and the declared connector transport are
legal, and infinity otherwise.  Both `C` values include their respective
whole-component-token contributions.  The Boolean support of `mathbb W`
gives feasibility; its finite entry is the exact killed/born drift for that
particular paired socket.  There is no socket-independent scalar `c_d(q)` in
general, and the new absolute composite alone can never certify a negative
drift.

### Theorem 3.1 (fixed-fragment history criterion)

On a fixed retained-fragment table, a heptagonal macro-ticket is
history-accepting exactly when:

1. its signed paired relation `mathbb W_(q,d)` has a finite entry on the
   actual old positive/zero histories and the declared new histories or
   reset state;
2. that entry uses the required endpoint frames and connector labels;
3. every constant-core whole-component token passes; and
4. that selected signed-relation entry has negative terminal drift in the
   declared potential.

For a closed co-oriented replay, subtracting the two aggregate transfer
composites gives the exact endpoint drift `B_2(H)-B_1(H)`.  That aggregate
drift is not by itself a recursive socket: a later connector may reverse a
path or test a particular insertion/deletion label, in which case the full
signature (3.1) is necessary.

#### Proof

The capped-age automaton is Markov-sufficient for event-bearing short runs.
All runs internal to one retained path occur on both sides and cancel.  The
connector compositions determine every changed boundary run.  Forward and
reverse morphisms cover every permitted path orientation, and the core sets
cover precisely the constant-coordinate components not represented by an
event pair.  Subtracting the old absolute composite from the new one on the
paired actual sockets gives exactly the signed potential drift in (3.3a).
Therefore the four displayed conditions are respectively
necessary and sufficient for a legal labelled socket pair, its literal
transport, the whole-component guard, and the negative exact ledger.
\(\square\)

### Proposition 3.2 (local same-cap backup menu)

Fix a cap `U` of size `n` and two internally biresident retained collars.
After transporting all labels into one endpoint frame, let `I^+` and `D^+`
be the recent-insertion and forthcoming-deletion collars, and let `I^-` and
`D^-` be their deletion-history duals.  Assume the endpoint separation

\[
 I^+\cup D^+\subseteq U,
 \qquad (I^-\cup D^-)\cap U=\varnothing,               \tag{3.4}
\]

and the old positive and negative cross-collar inequalities.  Put

\[
                         W=U\setminus(I^+\cup D^+).      \tag{3.5}
\]

Then the exact number of oriented same-cap connectors

\[
                         U-\alpha\longrightarrow U-\beta
\]

carrying those collars is

\[
                         |W|(|W|-1).                     \tag{3.6}
\]

If `n>=2d+1`, this is at least

\[
                         (n-2d)(n-2d-1).                \tag{3.7}
\]

If endpoint separation (3.4) or either old cross-collar inequality fails,
no endpoint choice repairs that failure with one connector.

#### Proof

Internal biresidence makes every recent/future positive label present at the
corresponding endpoint and every dual negative label absent, which gives
(3.4).  Both missing endpoint roles must avoid the positive collars, so they
are precisely an ordered pair of distinct elements of `W`.  This gives
(3.6).  The two positive collars contain at most `2d` labels, giving (3.7).
The failed endpoint or cross-collar tests depend only on the retained ears
and cannot be changed by choosing the two roles.  \(\square\)

Thus, once compatible collars and a cap are fixed, local backup connectors
are `Theta(k^2)` in the central regime for `d=O(sqrt(k))`.  This does not put
their owners and facet into one degree-two factor or give the required path
permutation.  The remaining row is joint factor/topology embedding.

## 4. Protected Pascal and pull-ear composition

A proof-safe protected Pascal state at depth `d` must export at least

\[
 \mathfrak S_d=\bigl(
   p_*\to g,\ w,\ Q_*,\ (J,o_J),\ e_{\rm open},
       (A_*,\nu_*),\
   \mathcal R_d^+,\mathcal R_d^-,\
   s_F,\ h,\sigma,\text{ frame},\
   \text{protected correction and upper resources}\bigr). \tag{4.1}
\]

The first entries are the persistent one-aperture port, literal rail,
deficient predecessor support, and the missing value `J` together with the
address-distinct exterior occurrence `o_J` intended to discharge it;
`e_open` is the literal opened-edge identity and `(A_*,nu_*)` records the
active-star address and count.  The local one-aperture port/debt relay keeps
the debt count equal to one under its own suspension.  Turning that relay
into the conditional one-position `B+1` bridge additionally requires
`e_open` to be the aperture transition so that `J` is the endpoint colour,
the literal occurrence `o_J`, and one-star consolidation.  The theorem
does not construct the ambient source or common compiler.

The reserve coordinate in (4.1) means membership in a declared admissible
reserve class, not merely its total mass or the number of caps with positive
slack.  Two vectors with the same total reserve can have different reachable
typed backups and different future cap cuts.

For the directed positive history, a depth-`d` pivot with deletion labels
`a_1,...,a_d` has exact input domain

\[
 \mathcal D_A=\left\{(h_1,\ldots,h_d):
    a_t\notin\{h_1,\ldots,h_{d-t+1}\}\ (1\le t\le d)\right\}, \tag{4.2}
\]

and constant output

\[
                         (\mu,\rho_{d-1},\ldots,\rho_1). \tag{4.3}
\]

The frozen pivot audit proves only this positive insertion-history reset.  A
full bi-history recurrence must separately supply a literal deletion-history
dual or reversed reset with its own triangular entrance domain; it is not a
consequence of (4.2)--(4.3).  For growing depth there is no
transition-equivariant section from the depth-`d` state to depth `d+1`.  A
recurrence must export the new oldest insertion/deletion labels, retain the
longer bi-history relation, or install depth-`(d+1)` certified positive and
separately supplied dual resets with their complete entrance domains.  Merely
remembering a constant output is insufficient.

### Theorem 4.1 (macro-ticket accepting return)

Let `q_1,...,q_L` be a materialized macro-ticket path from a protected state
`mathfrak S_d`.  Its terminal commit returns to the same regenerative class
and strictly decreases the integer potential `Phi` if and only if the union
passes all of the following declared rows:

1. literal factor, facet, owner, and protected-row exactness;
2. the cap cuts (1.4), the prefix product (1.11) when intermediate factors
   are physical, and membership of the exported reserve vector in its
   declared recursive class;
3. the component/opening calculation and required quotient voltage;
4. the composed positive and zero bi-history relations of Theorem 3.1 on the
   selected paired old/new socket;
5. the aperture/exterior-discharge and deeper-upper coordinates included in
   `mathfrak S_d`; and
6. total signed macro weight from `mathbb W` at most `-1`.

If the complete finite builder materializes every legal transition and every
passing terminal commit inside the declared support/debt bound, then exactly
one of the following holds: such a negative accepting path exists, or a
Bellman--Ford/Farkas vertex potential makes every materialized accepting
return nonnegative.

#### Proof

Items 1--5 are precisely the literal terminal state equality, and item 6 is
the desired descent.  Sufficiency and necessity follow by replaying the
union, not by adding primitive deltas.  For the alternative, layer the finite
state graph by macro-step count, add a zero-cost analytic reset from every
accepting state to the root, and apply the no-negative-cycle potential
theorem.  Completeness of the materialized builder is essential for the
claim about all paths in the declared envelope.  \(\square\)

### Corollary 4.2 (exact completed-ticket circulation)

Expand every materialized macro-ticket into one arc for each literal choice
of input/output bi-history and backup/return sockets, including its connector
morphism and a Markov-sufficient exact cost.  Let `x_a` be its zero-one
selection variable, `partial a(U)=-delta_a(U)` its cap demand, and `c_a` its
exact signed macro weight `C_new-C_old` on that paired socket, including the
whole-component difference.  The occurrence-resource universe contains every old/new
row, owner, facet, backup, collar, and protected occurrence whose sharing can
change the union replay.  For prescribed private tasks, the terminal
selection is exactly the integer system

\[
\begin{aligned}
 &\sum_{a\in\mathcal A_t}x_a=1
      &&\text{for every task }t,\\
 &\sum_{a:\operatorname{head}(a)=\omega}x_a
      =\sum_{a:\operatorname{tail}(a)=\omega}x_a
      &&\text{for every internal history state }\omega,\\
 &\sum_a x_a\,\partial a(U)\le s_F(U)
      &&\text{for every physical cap }U,\\
 &\sum_{a:q\in\operatorname{supp}(a)}x_a
      \le\operatorname{cap}(q)
      &&\text{for every occurrence resource }q,\\
 &\sum_a c_ax_a\le-1,
\end{aligned}                                                   \tag{4.4}
\]

together with the declared connected/root-reachable support, component
permutation, opening, and voltage rows.  Open recursion replaces conservation
at its two boundary histories by one unit of source/sink imbalance.  Exact
cap-multiset return replaces the cap inequality by zero cap drift.  If every
physical prefix must be cap-safe, the ordered reserve vector or the prefix
coordinate `beta` from (1.11) must also be included in the state.

This formulation is necessary and sufficient for the fully materialized
literal catalogue; it is not an ordinary network-flow integrality theorem.
The task, cap, resource, topology, and connectedness rows can destroy total
unimodularity.  An LP dual certifies only the relaxation.  Expanding every
bounded resource coordinate into the layered state graph recovers the exact
integral Bellman--Ford alternative of Theorem 4.1.

### Pull-ear specialization

A heptagon may be treated as one relation-labelled macro-ear.  It does not
automatically satisfy the graphic prepared-tree axioms.  If a family of such
ears separately satisfies exact forest semantics, protected/exterior return,
hereditary palette transparency, and prepared additive collar weights, then
the two-pull minimum-spanning-tree exchange theorem applies.  If some
spanning tree has full residence potential zero, every minimum-weight tree
has full potential zero, and repeated improving two-pull exchanges reach
some such minimum tree with peak component debt one.  They need not reach a
prespecified zero tree.

Without a common history dart graph or context-independent collars, scalar
edge weights need not add.  The correct exact object is then the relation-
labelled dynamic program or the lifted graph of Theorem 4.1.  Ordinary pull
graph connectivity cannot replace history acceptance.

## 5. The balanced cap/history host-spread hypothesis

The remaining expansion row can now be stated without referring to raw
circuit degree.

Fix constants `c,C,a>0`, a macro-return bound `L`, and `H` private defect
tasks.  For each task `i`, let `mathcal A_i` be an atlas of **physically
exposed** rooted macro-tickets, already filtered by Theorem 4.1.  Call these
atlases `BCHS(k,d;c,C,a,L)` if the private anchor skeletons and their
mandatory protected banks are already pairwise compatible/disjoint and:

1. `|mathcal A_i|>=c k^7` for every `i`;
2. each ticket uses at most `aLd` nonanchor resources, counting literal
   central rows, cap-reserve occurrences, forward/reverse history collars,
   capped lengths and whole-component/constant-core tokens, topology ports,
   and protected upper tickets when present; alternatively every evaluated
   component is longer than `d`, so the core correction vanishes;
3. each such resource occurs in at most `Ck^6` tickets of any other rooted
   atlas; and
4. resource-disjoint tickets are prepared: their full collars do not create
   unrecorded cross terms, they return the same protected Pascal state, and
   each has total signed macro weight at most `-1` for its declared task.

The word “physically exposed” is load-bearing.  The prospective counts
(0.1)--(0.2) do not establish item 1 for a frozen factor.

The `O(k^6)` nonanchor-load theorem belongs to the fixed-`z`, phasewise
cap-exact atlas in (0.1).  It must not be transferred automatically to the
larger twisted-geodesic atlas in (0.2): fixing a moving-geodesic token can
still leave `Theta(k^7)` labelled twisted completions.  A twisted proof needs
a private skeleton or a separately extracted one-degree-load subatlas.

### Theorem 5.1 (greedy balanced-ticket packing)

If

\[
             (H-1)aLCd < ck,                             \tag{5.1}
\]

then one can choose one ticket from each `mathcal A_i` so that the chosen
tickets are pairwise resource-disjoint.  Their sequential or simultaneous
prepared commit preserves every returned state coordinate and performs all
`H` declared negative repairs.

#### Proof

After `j` tickets have been chosen, they occupy at most `jaLd` resources.
By item 3, those resources exclude at most

\[
                         jaLCd\,k^6                       \tag{5.2}
\]

tickets from the next atlas.  For `j<=H-1`, (5.1) makes (5.2) strictly less
than `ck^7`, so at least one ticket remains.  Induction chooses all `H`.
Prepared disjointness gives the terminal replay assertion.  \(\square\)

In asymptotic shorthand, bounded-length tickets pack whenever
`HLd=o(k)`.  For fixed `H,L` and `d=Theta(sqrt(k))`, this inequality holds.

### Theorem 5.2 (regenerative descent)

Let `Phi` be a nonnegative integer on a class of protected Pascal states.
Assume that at every reachable state with `Phi>0`, `BCHS` supplies a ticket
or prepared batch whose commit returns to the class and lowers `Phi` by at
least one.  Then repeated commits reach `Phi=0` in at most `Phi(F_0)`
rounds.  A single-ticket round uses at most `L` macro-steps; a prepared batch
of at most `H` such tickets uses at most `HL`.  Every round preserves the
declared cap, history, aperture, topology, and protected-upper coordinates.

#### Proof

The returned state lies in the same class, so the hypothesis reapplies.
The nonnegative integer decreases strictly at every round.  \(\square\)

This is a concrete sufficient form of lifted terminal cycle expansion.  It
is not necessary that every primitive improve: all debts may be carried
inside one length-`L` accepted ticket, or the declared length-`HL` batch.

## 6. Why the host-spread row is genuinely additional

Four exact obstructions prevent the central count from proving Theorem 5.2.

1. **Tight cap cycle.**  On the one-copy arc face of a directed cap cycle of
   length `m` with `s_F=0` everywhere, the only nonempty terminally safe
   subcirculation is the whole cycle.  The tight `C4` therefore has no
   three-arc cap-only
   bypass, and cycles of growing length rule out a uniform bound from cap
   completeness or bounded degree.  A shorter ear exists exactly when the
   cap-transfer graph has a return path or reachable reserve source of the
   corresponding bounded distance; the full lifted ear must additionally
   pass history and topology.
2. **History boundary.**  A pivot may export the correct rail and cap while
   the next edge deletes its just-inserted `mu`, creating a length-one run.
   Cap containment cannot replace (4.2) or the bi-history relation.
3. **Pascal aperture.**  Two strict central one-copy closing ports with a
   common rail cannot cross nondegenerately.  The smallest escape uses one
   rank-defect-one predecessor support and one explicit exterior discharge.
   This occurrence credit is separate from immediate-upper cap reserve.
4. **Canonical pull face.**  In the complete labelled `ML(11)` MMM
   gluing-tree family, the upper-`q1`-exact accepting endpoints have minimum
   positive residence debt 154.  No path returning to that face can improve
   such a minimizer, irrespective of its temporary debt or length.

Accordingly no uniform theorem follows from `Theta(k^7)` prospective supply,
the `O(k^6)` central-token load, ordinary pull-graph connectivity, or cap
slack alone.  The precise extra hypothesis is positive-density **joint**
physical exposure of reserve-balanced, boundary-history-accepting tickets
with the same one-degree load bound.

## 7. Frozen `k=17` calibration and scope

For `k=17,r=9`, the rooted fixed-`z` atlas has exactly 376,320 labelled
tickets, and its maximum audited nonanchor central-token load is 47,040.
The twisted voltage-one census has 476 seven-run owner anchors, 196 through a
fixed boundary coordinate.  These are exact central/socket calibrations; no
completed cap/history fibre count is inferred from them.

The dominant endpoint is

```text
scratch/r2_k17_residence_master_round1_20260802/final2754/
  after_c14_2754_single/final2754.factor.tsv
```

It has positive residence 2,754, one physical cycle, complete central and
immediate palettes, and deep-upper hole counts

\[
                 (H_{11},H_{12},H_{13})=(1853,357,0),     \tag{7.1}
\]

with ranks 13 and above complete.  Exact current blocker extraction gives
162 current rows.  Against the canonical 445-row bank, 142 overlap and 20
are novel, producing the deterministic locally canonicalized 465-row union.
The endpoint therefore remains positive-residence and `NEED_CEGAR`; it is
not called resident or a word.  Its complete one-endpoint-retaining directed
`C6/C8` census has 43 and 23 cap-safe one-component candidates,
respectively, and zero positive-short-run improvements.  This closes only
that declared short single face, not long or compound packets.

The final `C14` replay additionally gives

\[
 (\Delta S_+,\Delta D_+,\Delta S_0,\Delta D_0)
                         =(-4,-6,-4,-6)                   \tag{7.2}
\]

per coordinate, holonomy five, one developed moving circuit, and the
three-reserve-unit cap transport of Section 2.  This proves coexistence of
cap-support-preserving one-cycle topology and exact negative terminal
residence drift at one authenticated state.  It does not prove a recursive
bi-history or protected Pascal-state return, positive-density host spread,
or regeneration after the next commit.

Principal frozen inputs and audits are

```text
MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md
MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md
MATH_THEOREM_K_CAP_BACKUP_HISTORY_TICKET_MONOID_AND_HEPTAGON_HOST_GATE_20260802.md
MATH_THEOREM_K_HEPTAGON_CAP_HOLONOMY_BACKUP_AND_HISTORY_TICKET_INTERFACE_20260802.md
MATH_THEOREM_A_EQUIVARIANT_DIRECTED_HISTORY_EAR_SEMIGROUPOID_AND_PULL_TRANSPORT_20260802.md
MATH_THEOREM_A_MIDDLE_LEVELS_PULL_EAR_GAP_MONOID_AND_PREPARED_TREE_DESCENT_20260802.md
MATH_AUDIT_K17_PHASE_FREE_HISTORY_AND_PASCAL_PIVOT_RESET_20260802.md
MATH_THEOREM_K_PASCAL_PORT_RANK_APERTURE_AND_ONE_CREDIT_REGENERATIVE_CHAIN_20260802.md
MATH_AUDIT_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md
scratch/k17_upper_decorated_longrun_circuit_20260802/longrun2754.audit.json
scratch/k17_upper_decorated_longrun_circuit_20260802/heptagon_atlas_k17_r9.audit.json
scratch/audit_heptagonal_cap_circulation_atlas_20260802.cpp
scratch/audit_k17_endpoint_circuit_longrun_20260802.cpp
scratch/p_k17_physical_deadline_master_20260802/final2822_history_lns/final2822.factor.tsv
scratch/audit_k17_final2754_cegar_rebase_20260802.cpp
scratch/k17_final2754_cegar_rebase_20260802.audit.json
scratch/k17_final2754_cegar_rebase_20260802.novel20.cnf
scratch/k17_final2754_cegar_rebase_20260802.cumulative465.cnf
```

The principal SHA-256 bindings are

```text
fac9ad6c29f39a89c9cdce4e88f231e5f73725535e6e1aea47aeb3f43aaaddc7  final2754.factor.tsv
f6bc3755af3a83940e83d34da644bc0ba174a2b7fbcc534b5cd71a31a34b5c83  final2822.factor.tsv
edc937949e741382fbf53cb80f1d32aa9c7d7f008f60894682ecac0b1e7747a7  round000.model
e151ccd9327d66430e7c0c08f601b49c8e4f7c632871f68ca2c3d604b5b63c15  cumulative445.blocks.cnf
50ac7888a76995a0646fe450bee8acf4c95dfcd5400c7addedede8a799b1994a  final2754.current.blocks.cnf
3b07ed4f2147b65dab3f39eb9fdcfd9cab770f806fc58ea2a4396f142d966948  round000.audit.json
47feac9f900322af7aa05396fc4ee00ba6ebb734d5d467e897e8a940348df177  audit_k17_endpoint_circuit_longrun_20260802.cpp
46dda4f08412ecd06b58885d50c65e4b7227b7d5952a2acb3184af0c17a92ec3  longrun2754.audit.json
31aa36f6fc4a2be2dfaf03819dd81cbd5df0bd626949f6641a6a78fb81f38eea  longrun2754.trace.tsv
092ffad06b367b8e6c21f8a913fdd6529a1415b28aa69d8d4811a83664473e44  longrun2754.moving_cycles.tsv
ca47063d711133e68745d92a8af7d6b4bfe110f559e5e808a394df0f106679b5  k17_final2754_cegar_rebase_20260802.audit.json
cb43cd2a1a89b910a6e3afd0d0d4eac209ea1d13db4f83c3de1a6c606c7c7629  k17_final2754_cegar_rebase_20260802.novel20.cnf
87a9334aa6819c89b758736fb6e97948d31e124cd7468a79fc30ae6a3845fd69  k17_final2754_cegar_rebase_20260802.cumulative465.cnf
```

The theorem makes no inference about an upper/source antecedent, a linear
opening, a common source/compiler state, or a universal word.  Deeper upper
resources are preserved only when explicitly included in the macro-ticket
state.  No heavy enumeration is used in this integration.
