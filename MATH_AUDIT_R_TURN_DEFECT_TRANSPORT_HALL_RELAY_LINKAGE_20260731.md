# Audit of the turn-defect transport Hall--relay--linkage theorem

Date: 2026-07-31  
Verdict: **PASS after scope corrections**; the theorem is an exact
conditional selection theorem, not an all-`m` macro-supply theorem

Audited file:

```text
MATH_THEOREM_R_TURN_DEFECT_TRANSPORT_HALL_RELAY_LINKAGE_20260731.md
```

## 1. Static transport

The occurrence unfolding is correct under the stated unit-service
hypothesis.  If a macro has `delta(h)=1` at one old hole, services no other
old hole on that shore, and leaves every old colour covered, every negative
unit comes from a surplus occurrence: `delta(c)=-a` and terminal coverage
imply `n(c)>=a+1`.  Hence one may name one donor-to-hole defect job and keep
all ancillary signed changes in the literal macro ledger.

The capacitated Hall inequalities are then exactly max-flow/min-cut after
unfolding repeated occurrences.  They are not an integral description for
arbitrary compound macros.  The theorem correctly excludes macros servicing
several holes from this shore-flow model and checks every ancillary change
again in the ordered prefix ledger.

## 2. Compatibility and physical resources

For fixed lower and upper job sets, Hall in the compatibility graph gives a
perfect matching.  If support conflicts are contained in its line graph,
two selected matching edges cannot conflict physically.  This proves the
line-conflict lemma.

Line-conflict is sufficient, not necessary for one successful packet.  The
main theorem was corrected accordingly: its exact packet clause is a perfect
compatibility matching whose selected literal supports are disjoint; the
line-conflict property is a checkable catalogue-level certificate.

The need for this correction is witnessed already by the `2 x 2` resource
fixture.  Diagonal macros both use one capacity-one resource and off-diagonal
macros both use a second.  All job marginals and the half-vector pass, but
each integral perfect matching overloads one resource.  Thus general macro
selection is not ordinary bipartite Hall; unrestricted grouped compatibility
contains `3DM`.

## 3. Topology and order

For pairwise support-disjoint switches, deleting every old switch matching
leaves fixed path atoms with endpoint pairing `P`.  At a subset `S`, the
factor components are exactly the alternating cycles of `P` with the current
old/new seam matching `M_S`.  Consequently, an executable one-switch order
exists if and only if the exact safe subset cube contains a maximal legal
chain.  This is a tautological but complete finite-state criterion and is
strictly stronger than static Hall.

The Euler-trail projection is valid only under the separately stated
context-independent Markov hypothesis.  In the general case, component
pairing, protected support, and any required boundary linkage relation must
remain in the subset state.  Two disjoint switches which each split a cycle
but jointly restore it give the minimum two-macro obstruction to replacing
the subset chain by terminal Hamiltonicity.

For the frozen `m=5` packet, the Hamilton-safe subsets are exactly

\[
 \varnothing,\{C_1\},\{C_2\},\{C_1,C_2\},
 \{C_1,C_2,C_3\}.
\]

Thus `C1,C2<C3`, with two topology-safe orders.  The complementary defect
projection is the directed cycle

\[
 73\to146\to292\to73,
\]

whose head-to-tail Euler order is one of them.  This proves the relay model
but also shows why the Euler projection is not the whole topology state.

## 4. Terminal common-core linkage

After contracting a forced guarded bank, take a maximum matching `P` in the
source/final common augmented graph.  Berge's theorem gives the exact
criterion: the terminal graph has a perfect matching precisely when all
exposed left vertices link vertex-disjointly to distinct exposed right
vertices in the final alternating network.  Menger gives the equivalent
capacity-`r` cut condition.  No intermediate perfect matching follows or is
needed when debt is allowed until packet end.

Macro support-disjointness does not make linkage gain additive.  A valid
minimum example has left vertices `b,s1,s2`, right vertices `a,t1,t2`,
common edges `ba,bt1`, and maximum common matching `{ba}`.  Add `s1a` in one
macro and `s2t1` in another.  The added edges have disjoint endpoints and
each alone raises rank from one to two.  Together the rank remains two,
because both gains compete for `t1` and `t2` is isolated.  Hence a single
terminal global flow, or genuinely private direct-sum route modules, is
necessary.

The `m=5` common core has rank `197` on order-`210` shores and the frozen
certificate supplies thirteen disjoint augmenting paths.  This verifies the
terminal row for that one packet, not for the surrounding `C10` catalogue.

The controlled-debt normalization is also exact.  Writing

\[
 \xi=N-\nu(A)-\max\{h_-,h_+\},
\]

subtracts only the forced isolated-hole floor, so `xi>=0`.  Along either
legal `m=5` chain, ranks `207,208,209,210` and hole floors `3,2,1,0` give
`xi=0` at every accepting prefix; the atomic source/final replacement has
linkage width thirteen.  This distinguishes live correlation debt from the
larger common-core replacement linkage.

The K17 arithmetic independently checks the same state:

* source: `4134=3826+308`;
* serial `3836`: `4130=3822+308`, with six common-core augmentations;
* serial `919`: `4131=3824+307`, with four common-core augmentations.

Thus `3836` is an excess-neutral transition and `919` is a strict
correlation-debt descent.  Each is a bounded-service state arc (four or two
lower holes, with the upper shore neutral), not a unit/unit shore-Hall macro.
Neither is a complete controlled packet; no
ordered chain, final topology, or uniform replacement for width `308` is
certified.

## 5. Transparent gluing versus debt-carrying repair

The fixed-decoration hexagon criterion agrees exactly with
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`:
selected local turn-colour multisets must agree separately on both shores,
and the retained-fragment boundary mark types must alternate after
reconnection.  Such a move carries one fixed decoration and cannot transport
a selected palette defect.

The ordinary hexagon repairing the first `ML(7)` gap-Hall counterexample is
therefore a repair move which permits a new decoration, not a transparent
move for the failed frozen decoration.  The census `31` alternating, `16`
Hamilton, `10` decorable, `6` common-decoration toggles is used with exactly
this scope.

It follows that recursive composition has two phases unless a full linkage
state is carried: first an ordered defect-moving packet with terminal debt
discharge; then a fixed-decoration prepared private/aligned gluing tree.  On
the latter face, the quoted graphic--gammoid rank inequality is the exact
selection criterion.  Pairwise transparent moves for different decorations
have no Helly implication.

## 6. Orbit scope and final boundary

A nonempty translation-invariant shift bank on one complete orbit is a
balanced regular bipartite graph, and any fixed shift is a perfect matching.
This settles only the orbit pairing row.  Donor capacities, physical
supports, the safe topology chain, and terminal linkage remain independent.
Different orbits may be solved separately only when those resources and
routes are orbit-private.

The synchronized \(m=5\) downstream certificate proves complete all-depth
flag support and 46 support-preserving cuts, but also proves an immutable
whole-path residence obstruction: 31 internal one-runs have length two.
Thus an interior rethread is an independent obligation, not a missing Hall
consequence.  Item 2188 now fulfills that obligation at the central
immediate-palette level: its independently replayed 119-partner rethread
is a 42-path forest with no internal positive run below three.  It still
owes 21 deeper targets and a connector chronology.  Item 2190 further
proves that endpoint-only joining of those fixed path bodies is impossible,
by two forced edge-disjoint residence collars.  Hence the remaining
\(m=5\) move must change an interior socket jointly with the connector; the
uniform all-\(m\) rethread/connector supply theorem remains open.

The Pascal determinant split independently rules out scalar two-full-parent
composition.  Exact contraction must remember both residual acyclicity and
the absence of an `H -> T` path.  Hence boundary-deficient rails and a
pairing/reachability state are algebraically necessary.  This agrees with,
but does not prove the supply of, the safe-subset and terminal-linkage states
used here.  Packet cardinality may grow; only each circuit's ports and the
live boundary/debt state are required to be bounded.

Therefore the final theorem proves:

> supplied occurrence Hall flows + a support-disjoint compatibility
> matching + a safe relay chain + one terminal guarded linkage imply an
> exact ordered repair packet.

It does **not** prove that PBBS/MMM supplies this bank for every `m`, that a
generic grouped bank is Hall-integral, or that the resulting physical lift
satisfies future residence, deeper shadows, sockets, voltage, or the literal
compiler.

The state-expanded Theorem 6.5 has accordingly been broadened to allow
q1-neutral progress arcs and an exact acyclic used-resource/stage
coordinate.  In a residence/all-depth application its Markov state must
include the fully composed coordinate-run monoid, the last required owner
tail and all-depth target debt, and the marked linear cut.  A pairwise seam
filter is only a sufficient subface when no short all-one fragment can relay
a run across two seams.

The independent finite replay

```text
python3 scratch/audit_r_catalan_prepared_private_palette_gate_20260731.py
python3 scratch/audit_r_turn_defect_transport_controlled_debt_20260731.py
```

passes the `m=4` no-common-decoration fixture, the unmodified standard
`m=5` palette obstruction, the literal three-`C10` packet, its common
prepared gap factorization, the corrected `2 x 2` resource and `3 x 3`
linkage counterexamples, the ML(7) `31/16/10/6` scope, and the exact m5/K17
debt arithmetic.  This audit uses no K16/K17 SAT result.
