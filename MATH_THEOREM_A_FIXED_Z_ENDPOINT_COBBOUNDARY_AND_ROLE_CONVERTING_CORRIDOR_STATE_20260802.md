# Fixed-`z` endpoint coboundary and the exact role-converting corridor state

**Date:** 2026-08-02  
**Lane:** A, ambient corridor for the opened seven-ear fixed-`z` packet  
**Status:** exact relative-displacement theorem, exact fixed-rail residue
formula, and exact finite-state obstruction.  Existence of the required
endpoint-conditioned Hall/common-base certificate is not asserted.

## 0. Verdict

Delete the same exterior ear `Q_j` from the two locally completed fixed-`z`
cycles.  The two remaining protected paths

\[
        P^\varepsilon:s=y_{j+1,d}\longrightarrow r=x_{j,d},
        \qquad \varepsilon\in\{0,1\},                 \tag{0.1}
\]

have the same literal endpoint owners, frames, and exported partial socket
relations.  Fix any common accepted boundary-state choice in those
relations.  Their interiors differ at the heptagon rows, but the frozen
local ledger gives

\[
                  V(P^1)-V(P^0)=0.                    \tag{0.2}
\]

If one literal, capacity-faithful, co-oriented **spanning** ambient corridor

\[
                         C:r\longrightarrow s         \tag{0.3}
\]

is accepted by that common endpoint choice and is used with the same
physical lifts and orientations in both phases, then
`P^0C` and `P^1C` are co-oriented spanning cycles and

\[
                    V(P^1C)-V(P^0C)=0.                \tag{0.4}
\]

Thus the ambient corridor introduces no **relative** pump gate.  Its
intrinsic absolute voltage may be nonzero and must not be counted as a
relative sidecar defect.

There is also an exact absolute-residue statement on one **fixed physical
state table**, with its protected head, final tail, and closing join fixed,
on the ordered-rail face.  If `W` is the common ordered rail and
`H=Stab_A(W)` in the deck group `A`, then every rooted common-base corridor
has the same residue modulo `H`.  On the rigid singleton pivot rail at
`d>=2`, `H={0}`, so the residue is literally fixed.  If that fixed value misses the
required absolute ticket fibre, no Hall witness, reordering, or same-rail
alternating circuit inside that fixed interface can repair it.  Changing the
closing join, final tail, or state table is a distinct escape.

The exact escape is then a **state-returning non-coboundary circuit**.  Lane
K has now constructed the first such local quotient actuator in the
one-copy simple occurrence-labelled model: a twisted three-run `C6` with
completed voltage `+1` or `-1`, cap state `(0,0)`, explicit two-sided
history branch, and a private physical closure.  This is a literal local
pump, not yet an ambient corridor transition: its `3n` developed roots must
be planted and its exported history/private branch admitted.  A supplied
parallel edge, duplicated payload, or broader multigraph interface remains
outside K's minimality scope.  A numerical `C6` voltage alone is not enough.
The actuator must return the correlated rail role, fragment pairing, cap
state, both histories, private aperture, and protected-resource state.
Failure of the resulting finite product-state reachability test is the
precise obstruction within the fixed corridor table and declared actuator
catalogue; changing that table is a separate escape.

## 1. Literal endpoint-conditioned corridor interface

Use the fixed-state fragment table of
`MATH_THEOREM_A_ENDPOINT_CONDITIONED_PHASE_COMMON_CORRIDOR_MATERIALIZATION_20260802.md`.
Every state records at least

\[
 (T,\text{frame},R^+,R^-,b,\Delta,
     f_{\rm ap},{\cal P}_{\rm priv}),                  \tag{1.1}
\]

where `T` is the literal owner, `R^+,R^-` are the two directed boundary
histories, `b,Delta` are the cap-prefix/debt data, and the last two fields
record the private aperture and protected-resource bank.  If a physical
fragment has several roles, phases, or orientations, they are exclusive
states of one occurrence, not independent capacity copies.

An ambient join is admissible only when it

1. is a literal Johnson seam in the displayed frames;
2. is accepted by both endpoint-history automata;
3. satisfies the named lower-facet and immediate-cap rows;
4. avoids both protected packet banks; and
5. carries its complete physical resource set and additive displacement.

The ordered-Hall construction, or equivalently the
out-partition/in-partition/graphic common-base construction, is called
**literal** only after all shared owner, facet, history, cap-token, and
private-resource rows have been retained or proved redundant.  Per-join
legality is not capacity faithfulness.

### Theorem 1.1 (phase-common endpoint materialization)

Suppose a literal rooted corridor certificate materializes (0.3), spans
every residual fragment once, accepts the cyclic endpoint state in both
history polarities, and realizes the prescribed facet/cap ledger.  Use the
same physical corridor in the two phases.  Then expanding the contracted
root by `P^epsilon` gives one simple co-oriented spanning cycle for each
`epsilon`.  Every encoded history and immediate-cap row is exact, and the
two phases have the same encoded lower/immediate-upper occurrence-token
ledger.  This implies global literal cap-value coverage only when the
token-to-cap projection and demand rows were chosen to certify it.
Moreover (0.4) holds.

#### Proof

The rooted ordered-Hall certificate gives one directed spanning path from
the exit `r` of the protected root back to its entrance `s`; expanding the
root therefore gives one cycle.  Literal state composition verifies every
new seam in both history polarities, while internal fragment acceptance
verifies all other runs.  Capacity faithfulness gives the claimed facet,
cap, and private-resource rows.

In the signed fragment ledger every ambient fragment, every ambient join,
and both endpoint seams occur with the same physical lift and orientation
in the two phases.  They cancel term by term.  What remains is precisely
`V(P^1)-V(P^0)`, which is zero by (0.2).  \(\square\)

The hypotheses concerning physical lift and orientation are load-bearing.
Two projected corridors with the same owner sequence need not have the same
voltage, and reversing a retained fragment contributes its signed fragment
term.

## 2. Fixed-rail endpoint formula

Let `W` be one ordered rail carried by every candidate corridor join and
let

\[
                         H=Stab_A(W).                  \tag{2.1}
\]

For a tail occurrence `u` and a head occurrence `v`, let `ell_u,r_v in A`
be their phases relative to the fixed representatives.  Lane K's exact
same-rail formula is

\[
             \delta(u,v)=\ell_u-r_v+h_{uv},
             \qquad h_{uv}\in H.                     \tag{2.2}
\]

Fix a rooted common-base table with final tail `z` and initial head `p`.
Every rooted corridor base `Q` uses every tail other than `z` and every head
other than `p` exactly once.

### Theorem 2.1 (endpoint-conditioned fixed residue on one table)

For every rooted common base `Q`,

\[
 \sum_{e\in Q}\delta(e)
 \equiv
 \sum_{u\ne z}\ell_u-\sum_{v\ne p}r_v
 \pmod H.                                             \tag{2.3}
\]

Consequently, for this fixed `p,z,e_*` and occurrence table, every complete
absolute ticket residue has the same image in `A/H`, equivalently lies in
the fixed coset

\[
 \kappa+\delta(e_*)+
 \sum_{u\ne z}\ell_u-\sum_{v\ne p}r_v+H,             \tag{2.4}
\]

where `kappa` is the fixed fragment sum and `e_*` is the fixed closing join.
When `H={0}`, (2.4) is one literal residue independent of the Hall witness,
the order among the same fixed occurrences, and the graphic-tree
realization.  Changing `z`, `p`, `e_*`, or the physical occurrence table can
change the omitted phase terms or `delta(e_*)` and is not covered.

#### Proof

Sum (2.2) over `Q`.  The out- and in-partition base rows use the displayed
tail and head sets exactly once.  The sum of the `h_uv` terms lies in `H`,
giving (2.3).  Adding the fixed fragment and closing-join terms gives (2.4).
\(\square\)

No assertion that every element of the coset (2.4) is realized is made.

For the singleton pivot rail at `d>=2`, K's stabilizer theorem gives
`H={0}`.
Therefore two possibly different same-rail rooted corridor bases on the
same occurrence sets have exactly equal displacement.  This relaxes
identical-corridor retention at the voltage row only.  It does not make the
two choices simultaneously compatible in their history, cap, resource, or
topology rows.

## 3. Coboundary and zero-circuit characterizations

The fixed-rail formula is a special case of a general exact test.  Give
every directed candidate join `e:u->v` a label `sigma(e) in A`; traversing
an edge backwards has label `-sigma(e)`.

### Theorem 3.1 (closed-walk criterion modulo a stabilizer)

For a connected candidate graph `G`, the following are equivalent.

1. Every signed closed walk has label in `H`.
2. There is a potential `phi:V(G)->A/H` such that

   \[
                 \sigma(u\to v)=\phi(v)-\phi(u)
                 \quad\text{in }A/H.                 \tag{3.1}
   \]

Under either condition every `r`-to-`s` corridor has residue
`phi(s)-phi(r)` modulo `H`.

#### Proof

Condition 2 telescopes on every closed walk.  Conversely, fix a root and
define `phi(v)` as the signed label of any root-to-`v` walk modulo `H`.
Condition 1 makes this path-independent, and a one-edge extension gives
(3.1).  Telescoping on an `r`-to-`s` walk proves the last claim. \(\square\)

There is a matching-specific version.  On the matching-covered part of the
tail/head split graph, all perfect matchings have the same displacement
modulo `H` if and only if every matching-alternating circuit has signed
displacement in `H`.  Equivalently, on each elementary component there are
potentials `alpha,beta` with

\[
                    \sigma(u,v)=\alpha(u)+\beta(v)
                    \quad\text{in }A/H.               \tag{3.2}
\]

Indeed, symmetric differences of perfect matchings are disjoint unions of
alternating circuits; conversely the alternating circuits generate the
matching-covered cycle space.  Equation (3.2) follows by propagation on a
spanning tree, and its sum over a perfect matching is independent of the
pairing.

With additional order, graphic, and physical-resource restrictions, the
full-graph circuit test remains sufficient.  It is a converse only on an
exchange-connected valid-base face in which the tested circuits are literal
feasible base exchanges.  An algebraic circuit using a forbidden shared
resource is not a physical corridor move.

### Corollary 3.2 (what K's same-rail theorem supplies)

If every alternating circuit of the corridor catalogue stays in one ordered
rail `W`, K's theorem puts its label in `H=Stab_A(W)`.  Hence the
matching-projection residue is fixed modulo `H`; under
the same-tail/head and common-rail hypotheses of Section 2 its value is
(2.4).  For a rigid rail it is fixed exactly.  A role-converting edge lies
outside this corollary.  In K's one-copy simple occurrence-labelled model,
a role-converting `C6` is the first simple support not already forced to have
zero holonomy.  K's twisted three-run theorem now realizes that support with
voltage `+/-1`; its admission to this corridor is addressed below and is not
implied by the circuit calculation.

## 4. Exact role-converting pump state

Let `S` be the finite set of **Markov-complete literal configurations**.
Every state `c` contains the complete current physical corridor/factor edge
set, its ordered fragment decomposition, its full signed facet/cap occupancy
and debt ledger, and every geometric datum needed to validate the next
actuator.  It has a boundary-package projection `bnd(c)=xi`, where

\[
 \xi=(\text{rail/role},\text{fragment pairing/topology},
      \Delta,b,R^+,R^-,f_{\rm ap},{\cal P}_{\rm priv},
      \text{resource-availability state}).             \tag{4.1}
\]

An accepted role-converting actuator is a directed transition

\[
                    a:c\xrightarrow{\eta}c'           \tag{4.2}
\]

only when one literal chronology simultaneously certifies its displacement
`eta in A`, cap state, two histories, private aperture, protected resources,
and topology action.  Resource-incompatible transitions are absent.  A
smaller summary such as only (4.1) may replace the literal configuration
only after a separate composition/congruence lemma proves it Markov-complete;
equal unproved summaries can conceal noncomposable geometries.

Fix the endpoint package `xi_0` and the required exact residue `t in A`.
Let `C_0` be the set of literal fixed-interface corridors supplied by
Section 1.  Each `C in C_0` determines an initial configuration `c_C` and an
exact residue `rho(C) in A`.  Theorem 2.1 proves only

\[
                       \rho(C)\in\bar\rho+H,           \tag{4.3}
\]

where `bar rho` is any representative of the fixed coset (2.4), not that
the whole coset is realized.  Let `S_acc(xi_0)` be the literal one-cycle
configurations whose boundary package is `xi_0`, whose complete owner,
facet, cap, history, and protected-resource ledger equals every exact target
row, and whose at-most-capacity rows are legal.

### Theorem 4.1 (exact pump reachability)

A role-converting pump word closes the corridor ticket if and only if the
product automaton on `S x A` has an accepted path

\[
       (c_C,\rho(C))\leadsto(c',t)                     \tag{4.4}
\]

for some `C in C_0` and `c' in S_acc(xi_0)`.  In particular, one `C6`
suffices exactly when it is an accepted one-step transition from some `c_C`
to such a `c'`, of label `t-rho(C)`.

#### Proof

Every literal actuator word determines the successive complete configurations,
the sum of its displacement labels, its resource use, and its topology
action, hence gives a path in the product automaton.  Exact closure requires
return to the named boundary package, the target group coordinate, one-cycle
topology, and legal resources, yielding (4.4).

Conversely, expand every transition of an accepting product path by its
certified literal actuator.  Package equality composes the cap and history
relations, membership in `S_acc(xi_0)` proves every final exact-demand and
capacity row, the group coordinate gives the target residue, and the
topology coordinate gives one cycle.
\(\square\)

Projecting (4.4) to `A/H` gives a useful obstruction, but is not sufficient
for exact closure when `H` is nontrivial.  If only same-rail actuators are
allowed, the quotient coordinate cannot change.  Therefore
`t+H!=bar rho+H` forces a non-coboundary actuator or a different corridor
table.  Equality of the cosets does not prove that the required element of
`H` is physically reachable.

For the rigid pivot rail at `d>=2`, `H={0}` and every nonempty fixed-interface
corridor family has one exact residue `rho_0`.  On that face:

* if `rho_0=t`, no pump is needed;
* if `rho_0!=t`, no same-rail corridor reordering can help; and
* within the fixed table, endpoints, closing join, and declared actuator
  catalogue, unreachability of (4.4) proves the existing catalogue
  insufficient.  Any successful extension must use a non-coboundary
  transition; it may require either a new such transition or a new
  zero-holonomy state/bridge making an existing one composable.

Globally, changing the closing join or physical corridor table, or using a
different non-same-rail actuator family, can escape this scoped obstruction.

The label `eta` alone is not the state.  The full correlated tuple demanded
by K,

\[
 (\eta;\Delta,b;R^+,R^-;f_{\rm ap};{\cal P}_{\rm priv}),             \tag{4.5}
\]

must be augmented by the fragment-pairing/topology action and literal
resource compatibility.

### Corollary 4.2 (exact interface to K's twisted `C6`)

Let `n=2r-1`, put `h=d+1`, and assume `r>=3h+1`.  K's twisted three-run
construction supplies the two literal nonmixed records

\[
 \Sigma_+=(0,0,{\cal R}^+,f_+,+1),\qquad
 \Sigma_-=(0,0,{\cal R}^-,f_-,-1).                   \tag{4.6}
\]

Each record has a simple `3n`-root development, simple immediate lower and
upper occurrences, and internally accepted depth-`d` history.  Let
`K_epsilon` be the path obtained by deleting the private pump closure
`f_epsilon`.  Its complete protected bank contains all `3n` roots, all
`3n-1` retained lower occurrences, all `3n-1` retained upper occurrences,
the omitted lower/upper pair on `f_epsilon`, and every cap/history/private
occurrence in (4.6).

Choose a literal embedding `iota` of this bank **before** constructing the
spanning corridor.  In the fixed fragment table, `K_epsilon` is one
protected fragment and its roots are not also offered as singleton ambient
fragments.  Let `e_amb` denote the ambient fixed closing join, distinct from
`f_epsilon`.  Then the K branch is admitted into one spanning host if and
only if the augmented table has a literal ordered-Hall/common-base
certificate satisfying all of the following.

1. The complete bank of `K_epsilon` and every ambient fragment/resource are
   capacity-compatible; any replaced ambient occurrences are credited in
   the same signed exact ledger.
2. The two exported ends of `R^epsilon` compose literally with the two
   selected ambient fusion seams.  Marginal acceptance at the two ends is
   insufficient.
3. The complete final owner/lower/upper/cap/history/protected ledger equals
   its target.  In particular `(z,b)=(0,0)` compares the forward/reverse
   pump branches internally; it does not make arbitrary fusion seams
   palette-safe.
4. Expanding all fragments gives one co-oriented spanning cycle.
5. With `kappa_(epsilon,iota)` the complete fixed-fragment sum, including
   the opened pump path, the exact group row is

   \[
       \kappa_{\epsilon,\iota}+\delta(e_{\rm amb})
          +\sum_{e\in Q}\delta(e)=t,                 \tag{4.7}
   \]

   where `Q` is the selected rooted corridor base.

Equivalently, a two-cycle fusion formulation must quantify a literal fusion
choice `F` and include in its new-minus-old ledger the removed ambient
closure, the removed pump closure `f_epsilon`, every new seam, every
orientation change, and every affected lower/upper/history/cap occurrence.
Its displacement is then a function of `(C,epsilon,iota,F)`, not merely of
the sign `epsilon`.

#### Proof

The twisted three-run theorem supplies every internal assertion and the
correlated records (4.6).  After reserving `K_epsilon` as one fragment,
Theorem 1.1 applied to the augmented table gives necessity and sufficiency
of items 1--4.  Its additive ledger is exactly (4.7).  Conversely, any
literal host containing this opened pump path contracts to the stated
augmented-table certificate. \(\square\)

Thus K has closed the local unit-pump construction.  The remaining pump row
in this lane is precisely ambient reservation/fusion and endpoint-history
admission, not the existence of a `+/-1` voltage value.

This reservation is genuinely global.  The developed pump cycle has `3n`
Johnson edges and `6n` incidence edges; its private opening has `3n-1`
Johnson edges and `6n-2` incidence edges.  For `n=2r-1` this is far beyond the `r-2` edge budget of
the small protected-factor theorem.  That theorem therefore cannot plant
the pump as a protected sidecar; a global phase-split host/fusion theorem is
needed.  This is a limitation of the available extension theorem, not a
nonexistence claim for the ambient host.

### Example 4.3 (smallest numerical-pump false positive)

Take `A=Z_3`, `H={0}`, fixed corridor residue `rho_0=1`, and target `t=0`.
Suppose the only role-converting candidate has numerical label `2`, but maps
`xi_0` to a different package `xi_1`, with no accepted return from `xi_1` to
`xi_0`.  Numerically `1+2=0`, and the separate cap, history, topology, and
voltage projections may all be nonempty.  Nevertheless (4.4) is unreachable,
so no ticket exists.  The missing object is a return state/actuator, not an
additional marginal voltage value.

## 5. What is closed and what remains

Combining Theorem 1.1 with the literal ordered-Hall/common-base theorem
closes, conditionally on one corridor certificate,

1. one co-oriented spanning component in both fixed-`z` phases;
2. the exact encoded positive and negative boundary histories;
3. the named lower-facet and immediate-cap rows;
4. zero old/new relative sidecar displacement; and
5. a fixed absolute corridor residue modulo the rail stabilizer on one fixed
   endpoint/closing-join table, and an exact value on the rigid `d>=2`
   pivot rail.

It does **not** prove that the required ordered-Hall/common-base certificate
exists in the Boolean residual host.  Nor does it prove global cap
completeness unless those cap-demand rows are included in the literal state
table, deeper upper witnesses, source/envelope transport, the terminal
common compiler, Pascal regeneration, or ambient planting of the
child-native unit-voltage seed.

The last phrase is now local rather than algebraic: K supplies the literal
`+/-1` twisted-`C6` seed.  What remains is to reserve/fuse its developed
support and admit one of its exact exported history/private-edge records in
the ambient host.

The remaining ambient theorem is therefore sharply separated.  First find
one literal endpoint-conditioned corridor satisfying the resource and cap
rows.  On a same-rail face its residue is fixed modulo the rail stabilizer by
(2.4), and is exact on the rigid `d>=2` pivot rail.  A coset mismatch (or an
exact mismatch on that rigid face) is when K's role-converting `C6` work
becomes relevant.  Corollary 4.2 gives the exact admission test for K's
now-explicit `+/-1` branches.  When `H` is nontrivial and the cosets agree,
exact `A`-reachability still remains open.  In every case a proposed actuator
must pass the full product-state test (4.4), not only its voltage marginal.
