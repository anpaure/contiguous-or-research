# Correlated SCD segmentation: the exact sidecar--Rado completion theorem and the nonlocal ticket gate

Date: 2026-08-01  
Lane: H3 / protected SCD segmentation / stateful connector completion  
Status: exact conditional theorem and exact finite obstruction.  No sidecar,
represented safety matroid, all-`m` cut bound, or final compiler is constructed
here.

## 0. Verdict

Let

\[
 n=2m-1,
 \qquad W=\binom{2m-1}{m},
 \qquad C=\operatorname {Cat}_m=\frac{2W}{m+1}.
\]

Start with an upper-q1-exact, lower-q1-injective spanning Johnson linear
forest on the `W` rank-`m` owners.  It has exactly `C` path components.  If
`t` old edges are cut, the raw segmentation has

\[
                              P=C+t                         \tag{0.1}
\]

pieces and exactly `P` missing lower-q1 colours.

There is a sharp conditional use of an equality

\[
                         |\mathcal H|=P-b.                  \tag{0.2}
\]

Reserve `b` pieces as one protected sidecar and contract its `b-1` fixed
arcs.  There remain `P-b+1` contracted components, hence `P-b` real
connector tasks.  If each upper hole is aligned with one real destination,
the lower providers are source-private, every connector has a context-free
resident state and a sealed occurrence ticket, all arcs increase one common
potential, and one represented resource matroid passes one Rado rank test,
then the pieces extend to one resident protected Hamilton chronology.  The
`b-1` sidecar arcs, the `P-b` real connectors, and the one terminal provider
use the `P` missing lower colours exactly once.

The specialization `b=2^d` explains why the finite equality
`6281-6273=8=2^3` is arithmetically attractive.  It is **not** an SCD
invariant.  The same `k=17` all-minimum-cut atlas contains another
`6281`-piece bank with only `6055` upper holes, so its difference is `226`.
Moreover every unchanged `1419`-cut minimum SCD segmentation has an
unsupported selected rank-ten colour.  Thus the conditional theorem cannot
be applied to the current minimum face with ordinary endpoint seams.

## 1. Exact piece--hole identity

Let `F` be the original Catalan path forest and let `D` be a set of `t`
cuts.  Write `F-D` for the resulting path pieces.  Let

* `A(F)` be the number of upper masks of ranks at least `m+2` missing from
  the complete internal interval-union deck of `F`; and
* `B_F(D)` be the number of masks of ranks at least `m+2` which occur in
  `F`, have no occurrence internal to a piece of `F-D`, and were not
  already counted by `A(F)`.

Because the immediate upper colours of the original forest are pairwise
distinct and complete, every cut destroys one different rank-`m+1` colour.
Because every piece interval was already an interval of its old component,
the old and newly created hole banks are disjoint.  Therefore

\[
 \boxed{
 |\mathcal H_F(D)|=t+A(F)+B_F(D),
 \qquad
 P-|\mathcal H_F(D)|=C-A(F)-B_F(D).
 }                                                        \tag{1.1}
\]

In particular the number `t` cancels from the second difference.  The
deep cut collateral `B_F(D)`, not minimum-cardinality interval stabbing,
controls the apparent near-square.

For the canonical `k=17,d=3` segmentation,

\[
 C=4862,\quad t=1419,\quad A=1662,\quad B=3192,
\]

and hence

\[
 P-|\mathcal H|=4862-1662-3192=8.                       \tag{1.2}
\]

The hole bank includes the fifteen rank-fifteen casualties.  On the other
authenticated endpoint-degree minimum pattern the holes by rank are

\[
        1419,2398,1576,549,102,11,
\]

whose total is `6055`; thus

\[
                         6281-6055=226.                  \tag{1.3}
\]

Equations (1.2)--(1.3) occur at the same `m,d,t,P`.  Consequently neither
`P-|\mathcal H|=8` nor `P-|\mathcal H|=2^d` follows from the Catalan count,
the SCD property, or minimum residence cutting.

More exactly, the proposed `2^d` sidecar arithmetic is equivalent to the
deep-deck identity

\[
                         A(F)+B_F(D)=C-2^d.             \tag{1.4}
\]

It is (1.4), together with endpoint service, that an asymptotic SCD theorem
would have to produce.  A bound on `t` alone has no bearing on (1.4).

## 2. Configuration and sidecar data

The theorem must keep segmentation and physical repair prospective.  For
each old path component `K`, let `\mathfrak C_K` be a finite catalogue of
local configurations.  A configuration records all residence cuts,
protected guard boundaries, exposed atomic paths, and the literal state at
each exposed end.  A prepared macro consumes a declared owner-disjoint set
of exposed atoms and replaces them by one internally certified ordered
block.  Unconsumed atoms remain blocks.  Exactly one configuration is
chosen on each old component, and selected macros together with unconsumed
atoms partition all `W` owners once.

Assume the chosen configuration has `P` active directed path blocks before
the sidecar, and that these blocks partition all `W` owners exactly once.
It is **lower-clean** when its internal Johnson edges have pairwise distinct
lower colours.  In that case their complement is a missing lower bank
`\mathcal A` of cardinality `P`.  If a macro creates an internal repeat,
the corresponding edge release must be part of the configuration before
the theorem applies; an aggregate lower count is insufficient.

Fix \(1\le b\le P\) active blocks and `b-1` directed Johnson joins between
them.
Call the resulting path `S` a **sealed protected sidecar** when:

1. its `b` blocks and `b-1` joins are internally source-valid and resident;
2. its joins use `b-1` different colours of `\mathcal A`;
3. it contains every prescribed protected packet/bank assigned to it and
   preserves all of their literal owner, immediate-palette, collar and
   occurrence resources;
4. its two exterior ends export fixed boundary states, so no run-age choice
   inside `S` depends on its eventual neighbours; and
5. after installing `S`, the complete internal upper leave is a named bank
   `\mathcal H` of size `P-b`.  Every target already serviced by `S` is
   removed before `\mathcal H` is defined.

Contract `S` to a root component `K_*`.  Together with the other `P-b`
blocks it gives a component set

\[
                  \mathcal K,
                  \qquad |\mathcal K|=P-b+1.            \tag{2.1}
\]

Fix one physical orientation and one exported sealed boundary-state sheet
for every member of `\mathcal K` as part of this outer configuration choice.
Every atom in which `K` occurs as a source or destination uses that same
orientation and state sheet.  If orientations are not fixed in advance,
Theorem 3.1 has a nested existential: one common orientation sheet must make
the Rado inequalities true.  Independent incoming and outgoing orientation
choices are not allowed.

The sidecar leaves `P-b+1` unused lower colours.  Assume these are the exact
residual missing-lower bank and assign them bijectively as

\[
                       K\longmapsto a_K
                       \qquad(K\in\mathcal K).           \tag{2.2}
\]

These are the **source-private lower tokens**.

Fix a bijection

\[
 \theta:\mathcal K\setminus\{K_*\}\longrightarrow\mathcal H. \tag{2.3}
\]

Thus each nonroot destination carries one named upper-hole task.

## 3. Sealed connector atoms and the one Rado row

For `K in \mathcal K`, let `h_K,b_K` denote its first and last owner.  Put

\[
 \mathcal D=(\mathcal K\setminus\{K_*\})\cup\{\bot\}.   \tag{3.1}
\]

A real connector atom with source `K` and destination `J` is the literal
packet

\[
                         e=(K,J,a_K,\omega),             \tag{3.2}
\]

where:

* `b_K` and `h_J` are joined by exactly one declared inter-block Johnson
  edge, with \(b_K\cap h_J=a_K\); it consumes exactly that one residual
  lower token and no additional owner or missing-lower resource;
* the packet is compatible with the exported states of both components;
* `\omega` is a physical interval occurrence with union `\theta(J)`; and
* every owner, palette, guard, compiler and occurrence resource consumed by
  the packet is listed literally.

For destination `\bot`, the atom `(K,\bot,a_K)` has no physical outgoing
join and designates the unique terminal source.  Let `\mathcal E_J` be the
menu for destination `J`, including `\mathcal E_\bot`.

The atom is **state sealed** when its legality is independent of the
incoming state before its source component and of the outgoing state after
its destination component.  It is **ticket sealed** when the occurrence
`\omega` lies in a fixed local packet word.  A longer occurrence counts as
sealed only when its entire ordered multi-block segment is one compound
packet contracted before this Rado stage; a symbolic token for an as-yet
unordered interval is not enough.
The words “state” and “ticket” cannot be omitted from these hypotheses.

Assume all real component arcs lie in one fixed DAG; equivalently, it is
enough to have one potential `\phi` with

\[
                         \phi(K)<\phi(J)                 \tag{3.3}
\]

for every real candidate `(K,J,a_K,\omega)`.

Assume every forced physical connector has been placed inside the sidecar.
Finally assume there is a represented matroid `N` on the residual atom
ground, after contracting the sidecar payload and deleting every atom which
conflicts with its protected resources, which represents exactly:

* distinct source components;
* the source-private lower tokens;
* owner and endpoint capacity; and
* simultaneous protected-packet, palette, sealed-state and sealed-ticket
  compatibility.

This is one load-bearing hypothesis.  Separate pairwise Hall tests do not
manufacture `N`.

The usual prescribed-bank variant contracts an additional independent atom
bank and deletes its already-used destination classes before applying the
same rank condition.  It is omitted from the notation below.

Every forced physical inter-block connector is assumed to be one of the
sidecar joins.  If another real connector is prescribed, first contract it,
delete its used source, destination and lower token, and recompute
\(\mathcal K,\mathcal D\) and all menus.  Contracting it only inside `N`
while retaining its old destination task would double-fill that destination.

### Theorem 3.1 (sidecar-contracted protected Rado completion)

Within the declared configuration, sidecar, potential and represented
atom atlas, a protected resident Hamilton chronology exists if and only if

\[
 r_N\!\left(\bigcup_{J\in Y}\mathcal E_J\right)\ge |Y|
                 \qquad(Y\subseteq\mathcal D).          \tag{3.4}
\]

The resulting chronology:

1. uses every owner once and contains the `b` sidecar blocks consecutively;
2. has exactly `b-1+(P-b)=P-1` physical inter-block joins;
3. covers every target in `\mathcal H` by its aligned sealed ticket;
4. uses `P-1` different members of the missing lower bank on physical
   joins and leaves exactly the `\bot`-provider unused; and
5. preserves every payload resource represented in `N`.

#### Proof

Rado's theorem applied to (3.4) selects one independent atom from every
destination menu.  There are `|\mathcal D|=P-b+1` selected atoms.  Source
independence and (2.2) therefore use every source component and every
remaining lower token exactly once.

Every nonroot component is a real destination once, while `K_*` has no
incoming arc.  Every source has one selected atom, but the unique source
selected for `\bot` has no physical outgoing arc.  Hence every other source
has outdegree one.  The common potential excludes directed cycles.  Starting
from any component and repeatedly following its unique predecessor must
therefore terminate at the only indegree-zero component `K_*`.  The real
arcs form one rooted directed tree; because every outdegree is at most one,
it is one Hamilton path on `\mathcal K`.

Expand the sidecar and every contracted block.  Internal certification and
state sealing give residence and source validity.  Equation (2.3) and the
sealed tickets give the whole named upper leave.  The sidecar joins use
`b-1` missing lower colours and the real Rado joins use `P-b`; these are
different by represented independence.  The only unused member is the
`\bot`-provider.  All protected conclusions follow from contraction and
`N`-independence.

Conversely, a chronology in this declared atlas selects one atom from every
destination menu and uses compatible resources and distinct sources.  It is
an independent transversal of `N`, so Rado necessity gives (3.4). `square`

### Corollary 3.2 (the `2^d` sidecar specialization)

If

\[
                         |\mathcal H|=P-2^d,             \tag{3.5}
\]

Theorem 3.1 applies with a `2^d`-piece sidecar, provided all of its other
hypotheses are proved.  The sidecar contracts `2^d-1` arcs, leaving
`P-2^d+1=|\mathcal H|+1` components, one real destination per hole and one
terminal atom.

The count is sharp for this **one sealed ticket per real connector** model.
If `|\mathcal H|>P-b`, there are too few real connectors.  If
`|\mathcal H|<P-b`, neutral/repeat upper tasks must be added or some
connectors must be permitted to carry no new target.  Neither case is an
obstruction to a broader chronology model.

## 4. Why the present minimum SCD face does not satisfy the theorem

The protected `k=17` q1 factor gives the general warning.  Its
lexicographically first minimum `3807`-cut segmentation has `56,790` raw
Boolean seam triples and perfect matchings in every two-shore projection.
After a necessary relaxed residence screen, `1289` deleted colours have no
candidate, `368` blocks have no outgoing candidate, and `368` have no
incoming candidate.  Thus an arbitrary minimum transversal cannot be frozen
before boundary-age matching.  That audit leaves other minimum or
nonminimum transversals open.

The SCD statement is stronger on its minimum face.  Here the cardinality
equality at the canonical `k=17` cut is only the zeroth Rado row.  For the
fixed earliest-right `6281` pieces, `322` deleted rank-ten colours have no
locally resident direct endpoint seam.  More strongly, over the complete
`8894`-pattern minimum-cut atlas, every global `1419`-cut choice contains at
least fourteen selected rank-ten colours with no extendable one-seam
provider.  For any alignment that assigns such a colour to a real
destination, its menu is empty and the singleton case of (3.4) fails.

The authenticated thirty-socket repair shows why the variables cannot be
frozen in stages.  Its static child list closes, but after materializing the
final `6252` intact pieces there are seven raw rank-ten zero rows and `53`
internal lower repeat units.  At least one release from every repeated
lower-colour pair and new exposure for the zero rows must remain prospective
in the same configuration/atom master.  A protected sidecar may be part of
that repair, but no such sidecar is presently certified.

Thus the surviving alternatives are precisely:

* a nonminimum correlated cut set;
* resident facet/socket macros or an interior rethread which internally
  supplies the zero rank-ten colours;
* prospective releases eliminating every lower repeat; and
* after those changes, a sealed atlas satisfying (3.4).

## 5. Why arbitrary-width tickets are not seam local

For oriented blocks `B_i`, write `G(B_i)` for the union of the whole block,
and `S_a(B_i),P_b(B_i)` for suffix and prefix unions.  Every interval crossing
from block `i` to block `j` has the exact form

\[
 S_a(B_i)\cup G(B_{i+1})\cup\cdots\cup G(B_{j-1})
                   \cup P_b(B_j).                       \tag{5.1}
\]

Hence a rank-`m+1` hole is seam local: every adjacent pair inside a witness
already has that same union.  A deeper target need not be local.  On the
frozen `k=17` pieces there is a rank-fourteen witness using sixteen owners
and crossing two cuts, and another using ten owners and crossing three.
Changing one intermediate block or its orientation can destroy (5.1) while
leaving both endpoint seams unchanged.

The residence state has the same nonlocality.  A coordinate constant on an
entire block carries its incoming run age to the next seam, so legality of
the outgoing seam is not a function of the adjacent pair alone.

Therefore an arbitrary-width occurrence or a run transition may enter the
Rado matroid only after **sealing** makes it context free.  Without sealing,
the exact object is a state-expanded Hamilton-path master with activated
multi-seam occurrence variables.  It is not a Rado transversal on ordinary
seam atoms.

There is already a sharp matroid obstruction before these history rows are
added.  Linear forests do not form a matroid: on vertices `1,...,5`, put

\[
 A=\{12,23,34\},
 \qquad B=\{25,12,13,34\}.                              \tag{5.2}
\]

Both are linear forests and `|A|<|B|`, but `A+25` has degree three at vertex
`2`, while `A+13` contains a triangle.  Thus no member of `B-A` augments
`A`.  Source/head/lower-colour synchronization also contains the standard
three-resource matching obstruction.  Indeed the four atoms

\[
 (s_1,h_1,a),\ (s_1,h_2,b),\ (s_2,h_1,b),\ (s_2,h_2,a) \tag{5.3}
\]

have perfect matchings in every two-shore projection.  The two perfect
source--head matchings use colours `a,a` and `b,b`, respectively, so there
is no selection with distinct sources, heads and colours.  The represented
matroid in Theorem 3.1 is consequently a genuine structural assumption, not
notation for the raw connector system.

## 6. Asymptotic capacity

Suppose a correlated segmentation theorem gives

\[
                         t\le A_0dC.                    \tag{6.1}
\]

Then

\[
 P=C+t\le(1+A_0d)C,
 \qquad
 \frac PW\le\frac{2(1+A_0d)}{m+1}=O(d/m).              \tag{6.2}
\]

Thus the number of piece ends, real connector tasks and selected Rado atoms
is `O(Cd)=o(W)` whenever `d=o(m)`.

Let every sidecar piece use at most `L_m` owners.  A `2^d`-piece sidecar has
owner support at most

\[
                              2^dL_m.                   \tag{6.3}
\]

For `d=O(\sqrt m)` and polynomial `L_m`, (6.3) is `o(W)`.  If all remaining
connectors use native exposed endpoints and `O(1)` additional owner support,
the formal protected-owner charge is

\[
 O(Cd)+O(2^dL_m)+B_{\rm fixed}=o(W),                    \tag{6.4}
\]

where the bounded reset/Ferrers bank contributes only `B_fixed=O(d)`.

By contrast, installing a private width-`d` collar at every one of the
`Theta(P)` connector tasks costs

\[
                         O(dP)=O(d^2W/m).                \tag{6.5}
\]

At `d=Theta(\sqrt m)`, (6.5) may be a positive fraction of `W`.  The
asymptotic route therefore needs the cut choice to expose already compatible
boundary ages, a shared/regenerative collar module, or an `O(1)`-support
sealed connector.  The scalar near-square alone does not provide that row.

## 7. Exact remaining gates

The conditional route is complete once all of the following are supplied
for one jointly chosen nonminimum configuration:

1. `t=O(dC)` and a lower-clean owner partition;
2. a resident protected `2^d`-piece sidecar (or an arbitrary `b`-sidecar
   matching the actual value `P-|\mathcal H|`);
3. one hole-to-destination alignment with nonempty sealed menus;
4. source-private lower tokens and one common increasing potential;
5. a proof that the complete payload compatibility system is a represented
   matroid `N`;
6. the Rado inequalities (3.4); and
7. the terminal lower/common-source compiler on the resulting chronology.

No currently frozen SCD theorem supplies items 2--6.  In particular the
lower/root/head/graphic correlation is not closed by a disjoint
second-facet projection.

## 8. Relation to the frozen record

The finite inputs and obstructions used above are recorded in:

* `MATH_AUDIT_THREAD_A_K17_SCD_RESIDENT_PIECES_ALLINTERVAL_UPPER_GATE_20260801.md`;
* `MATH_AUDIT_A_K17_M9_MINCUT_FACET_RAIL_AND_COMPOUND_FRAGMENTATION_GATE_20260801.md`;
* `MATH_THEOREM_K17_H2_MINCUT_BLOCK_ENDPOINT_THREE_RESOURCE_NOGO_20260801.md`;
* `MATH_THEOREM_K17_SCD_COMPACT_SOCKET_BANK_AND_UPPER_CASUALTY_LEDGER_20260801.md`;
* `MATH_THEOREM_THREAD_D_K17_SOCKET30_POSTBANK_GLOBAL_SELECTOR_AND_LOWER_CUT_20260801.md`;
* `MATH_THEOREM_GUARD_INTERVAL_TRANSVERSAL_AND_Q1_CREDIT_LEDGER_20260801.md`; and
* `MATH_THEOREM_H3_NONLEXICAL_PROTECTED_RADO_FOREST_AND_TRANSPARENT_CONNECTOR_GATE_20260801.md`.
