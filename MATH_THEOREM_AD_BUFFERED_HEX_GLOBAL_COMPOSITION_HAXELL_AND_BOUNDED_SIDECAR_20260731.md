# Buffered hex packets: exact global composition, Haxell selection, and the bounded sidecar clause

Date: 2026-07-31  
Lane: AD  
Status: exact sufficient composition and selection theorem, with sharp
counterexamples to weaker pairwise formulations.  The theorem is
conditional on a fully witnessed packet bank.  No all-`k` packet-supply
theorem, and hence no unconditional `nu(k)=B(k)+O(1)`, is claimed.

## 0. Verdict

The slogan

> pairwise nonconflicting buffered hexes compose globally

is false unless “nonconflicting” includes more than disjoint geometric
supports.  There are two irreducibly global obstructions:

* three pairwise safe connectors can form a component cycle; and
* three pairwise cap-feasible packets can compete for only two compiler
  cells.

There is, however, a clean corrected theorem.  First fix one decorated
off-state and either a prescribed path/backbone slot for every packet or a
triangular rooted-basis order.  Put a complete local common-cap witness,
all protected resource tickets, and the full affected-occurrence halo into
each packet option.  Declare two options conflicting whenever any of these
certified resources overlap or their boundary signatures disagree.  Then
**every independent transversal is a literal global composition**.

At that point Haxell's independent-transversal theorem applies with no
further Hall or cycle row:

\[
              |\mathcal L_i|\ge \max\{1,2\Delta(\Gamma)\}
              \quad\text{for every packet list }i                  \tag{0.1}
\]

guarantees one globally composable choice from every list.  The topology
normalization and integral cap witnesses must precede (0.1); Haxell cannot
supply them after the fact.

A bounded exceptional set is harmless only when every exceptional slot has
a literal neutral bypass, its current missing targets enter the current
terminal repair, and only auxiliary recurrence obligations enter a
regenerated bounded sidecar.  Merely deleting `O(1)` packet slots can break
the physical path and is not a valid additive-constant argument.

## 1. Decorated off-state and fully witnessed packets

Fix a literal decorated state `X_0` consisting of:

1. an ordered owner chronology and a directed path forest;
2. all exported lower/upper/payload occurrence maps through the protected
   depth;
3. residence boundary data (prefix/suffix run lengths clipped at the
   required thresholds);
4. typed endpoint and voltage/socket labels; and
5. one integral common-cap matching `M_0`.

A **buffered packet option** `p` replaces a literal off-fragment `A(p)` by
an on-fragment `B(p)`.  Its certificate contains:

* its typed input/output ports and exact boundary words;
* its internal owner/edge support;
* every affected occurrence at every protected rank;
* its exact signed loss/gain vector, with a named ticket for each consumed
  occurrence;
* its residence prefix/suffix state;
* its local quotient connectivity relation and endpoint action;
* a local integral cap matching on named target and cell tickets; and
* its exported sidecar state.

For a protected fixed window width `d`, the affected-occurrence halo is the
`d`-closure of the edited letters, with each crossing window assigned to
one packet or one declared interface.  For residence it also contains the
threshold-clipped run data on both sides.  For an all-depth shadow row the
halo means the **full set of affected occurrences**, unless a separate
trace identity proves that longer windows are invariant.  Constant edit
support alone does not make an all-depth halo constant.  Cyclic wrap or
opening occurrences and the clipped run state at the final socket are part
of this halo.

## 2. Four smallest counterexamples to naive pairwise composition

### 2.1 Graphic obstruction

Take three old path components `C_1,C_2,C_3`, each with two private ports,
and three resource-private connectors `12,23,31`.  Every connector is
locally a path.  Every pair forms a forest.  All three form a cycle.

Thus no graph whose edges mean only pairwise resource collision can encode
graphic independence of arbitrary component links.

### 2.2 Common-cap Hall obstruction

Let three support-disjoint packets each require one distinct compiler cell
from the same menu `{a,b}`.  Every pair has an integral cap matching, but the
triple violates Hall:

\[
                              3>2.                     \tag{2.1}
\]

Pairwise existential cap compatibility therefore does not compose.  A
packet must carry private/preallocated cap tickets, or the selected bank
must still pass one global Hall test.

### 2.3 Crossing-window obstruction

In the two-letter word `({1},{2})`, edit the first letter to `{1,3}` and the
second to `{2,3}`.  The letter supports are disjoint, but both edits change
the same crossing interval from `{1,2}` to `{1,2,3}`.  Summing two local
ledgers double-counts this one occurrence.  Expanded halos or explicit
interface ownership are necessary.

### 2.4 Missing common off-state

The state-dependent moves `e->f` and `f->g` may each be legal, while they
are neither simultaneous replacements of one base nor order-independent.
A common off-state, or a declared dependency DAG with exact boundary-state
transport, is necessary.

These examples are minimal in the relevant sense: two packets cannot form
a genuinely higher-order graphic cycle or a `3>2` Hall shore.

## 3. Exact composition theorem

Let `P` be a selected family of buffered packet options.

### Theorem 3.1 (buffered global composition)

Assume the following rows.

**B0 (common state or dependency order).**  Every off-fragment `A(p)` is a
subfragment of the same decorated state `X_0`.  Alternatively, the packets
are supplied in a DAG order and every packet input signature is exactly the
joint cumulative output signature produced by all its predecessors.

**B1 (complete support separation).**  Internal supports and unglued ports
are disjoint.  Affected-occurrence halos are disjoint except at named
interfaces, and each interface occurrence has one declared owner.  The
length-`d-1` boundary words, residence states, and typed port signatures
agree at every identified interface.  The owner's ledger at an interface is
evaluated from the exact simultaneous boundary words of every incident
packet; it is not a sum of unary ledgers.

**B2 (literal local legality).**  Every replacement is a literal Johnson/
compiler fragment with the declared degree, owner, palette, voltage, run,
and internal/interface occurrence ledgers.

**B3 (graphic row).**  Delete the off-fragments and contract every untouched
path fragment of `X_0`.  Each packet transfer graph is acyclic, and the
union quotient is a forest.  For a final path the quotient is connected,
has maximum degree at most two, and has the declared two endpoints.

It is enough instead to preassign every packet to a consecutive slot of one
fixed oriented component order.  Another exact sufficient certificate is a
rooted exchange matrix which is block triangular in a prescribed order and
has every diagonal block nonsingular, **together with** the global
maximum-degree-two, port-capacity, declared-endpoint and required
root-deletion/component rows.  Triangularity certifies the rooted graphic
basis, not the path-degree rows.

**B4 (global resource tickets).**  Retained-base gains, packet gains, and
interface gains are occurrence-injective in every exported palette.  Every
loss is restored, charged to a distinct preallocated spare ticket, or placed
in the declared current terminal exception set.  Only auxiliary recurrence
state, not a currently missing target, may be exported to the sidecar.

**B5 (integral common cap).**  The off-state matching `M_0` is unchanged
outside packet domains.  The union of replaced target and cell domains is
`M_0`-closed: every off-state edge incident with a replaced cell has its
target in a replaced target domain.  Every packet carries an integral local
matching covering exactly the targets whose `M_0` assignments it replaces;
the target domains and cell ranges of these matchings are disjoint and the
matchings agree with pinned interface assignments.  Equivalently, one
explicit global integral Hall matching may replace this private-domain
condition.

Then all replacements in `P` can be applied simultaneously.  The result is
a literal forest/path with the declared endpoints; every protected
occurrence ledger is the disjoint sum of the local/interface ledgers; every
protected loss is restored or explicitly exceptional; and the restriction
of `M_0` outside replaced domains, united with the local matchings, is one
integral common-cap assignment.

#### Proof

B0 and B1 make the replacements commute, or make their prescribed order
well-defined.  Every changed occurrence belongs to one local halo or one
owned interface, whose ledger is evaluated on the simultaneous boundary
state, so B2 gives literal legality and makes the resulting signed resource
ledger exact.  After contracting untouched fragments, a physical cycle
exists exactly when the packet quotient has a cycle; B3 therefore gives the
declared forest/path.  Under the matrix alternative, triangularity gives

\[
          \det X=\prod_i\det X[A_i,B_i]\ne0,           \tag{3.1}
\]

so the selected exchange is a rooted graphic basis; the separately retained
degree/port/endpoint rows make it the declared path.  B4 proves palette
capacity and loss coverage.  Finally, restrict `M_0` by deleting its edges
incident with every replaced target or cell domain.  B5 has disjoint local
matching domains and ranges, pinned consistently at interfaces, so the
union of this restriction with the local integral matchings is again an
integral matching covering the required target domains. \(\square\)

The quotient vertices in B3 are the untouched fragments of
`X_0-\bigcup_p A(p)`, not merely the original component names.  Internal
cuts can split an original component; contracting only original labels is
unsound.

For a cyclic or voltage output, replace the forest clause by the exact
one-cycle and unit-voltage closure condition, then open at a certified
socket.  Pairwise nonconflict does not imply that condition either.

## 4. When a conflict graph is complete

Fix a topological skeleton before selecting packets.  The most useful case
is an oriented path/backbone with slots `i in I`; every option in list
`L_i` has the same typed boundary ports and the same local connectivity
relation for slot `i`.  For the conflict-graph selector below, B0 uses a
common off-state.  A dependency DAG is admissible only after its cumulative
boundary states have been compiled into the option lists so that every
remaining compatibility predicate is unary or pairwise; an uncompiled
multi-parent state is not represented by an ordinary conflict graph.  Every
remaining interface is binary; a higher-arity simultaneous interface must
first be compiled into one joint super-slot.

Construct a graph `Gamma` on the disjoint union of the lists.  Do not put
edges within one list.  Put an edge between options in different lists if
any row B0--B5 would fail for that pair: support or halo overlap, interface
disagreement, repeated owner/palette/cell/loss ticket, cap-domain conflict,
or a forbidden dependency.  Because topology was fixed by the skeleton,
it is not a hidden higher-order predicate.

### Lemma 4.1 (full independent transversals are globally composable)

If every option is individually certified for B0--B5 relative to its slot,
then every independent transversal containing exactly one option from every
active list, under the common-state or compiled-DAG hypothesis above,
satisfies Theorem 3.1.

#### Proof

Independence gives every pairwise separation and agreement row by the
definition of `Gamma`.  The fixed skeleton supplies B3 for every full
choice.  In the compiled-DAG alternative, every selected cumulative input
state is the certified one by construction.  Private cap witnesses make B5
a direct sum after deleting the replaced part of `M_0`, not an
existential pairwise condition.  Hence all rows of Theorem 3.1 hold.
\(\square\)

This is the exact point at which “pairwise nonconflict implies global
composition” becomes true.  Without a fixed/triangular topology and private
cap witnesses, Lemma 4.1 is refuted by Sections 2.1--2.2.

## 5. Haxell independent-transversal selector

Let

\[
                         \Delta=\Delta(\Gamma)          \tag{5.1}
\]

be the maximum degree in the **complete** conflict graph of Section 4.

### Theorem 5.1 (buffered Haxell selector)

If

\[
              |\mathcal L_i|\ge\max\{1,2\Delta\}       \tag{5.2}
\]

for every slot `i`, then there is a choice of one packet from every list
whose simultaneous activation satisfies Theorem 3.1.

#### Proof

When `Delta>0`, Haxell's independent-transversal theorem gives an
independent transversal of a vertex-partitioned graph whenever every part
has size at least twice the maximum degree.  When `Delta=0`, nonemptiness is
both necessary and sufficient.  Apply this to `Gamma` and the parts `L_i`.
Lemma 4.1 turns the resulting full transversal into the literal composition.
\(\square\)

The global degree in (5.2) counts every conflict kind in B0--B5.  A degree
computed only from geometric support, or only from palette collision, is
not valid.  Likewise, a large provider list before cap tickets and topology
slots are fixed does not meet the theorem's hypothesis.

For the adjacent-cut `K17` normal form, one possible skeleton is an order of
the `3068` charged direct-core components.  A list at a gap then consists of
fully witnessed length-four or length-five ears between the prescribed
oriented ports.  The list option must already contain its internal owners,
all lower services/filler payloads, q8/h9 occurrences, run boundary state,
and common-cap tickets.  Neither the `8164/8164` provider matching nor the
local supported-wedge fixed point supplies these lists.  Their sizes and the
complete conflict degree remain unproved.

## 6. Bounded exceptional sidecar

A failed list condition at `O(1)` slots is not by itself harmless.  Omitting
one connector can split the chronology.  The following clause is sufficient.

### Definition 6.1 (neutral exceptional bypass)

An exceptional slot has a **neutral bypass** if a literal bounded-cost
fragment preserves its typed boundary connectivity, voltage and all
nonexceptional protected resources, while exporting a bounded list of
current missing targets to the current terminal-repair family and exporting
only bounded auxiliary port/ticket/recurrence obligations to the sidecar.
It is itself a fixed fully witnessed packet option: it satisfies B0--B3 and
the complete halo/interface rows; every current resource or cap failure is
charged to the current terminal repair; and its conflicts with ordinary
options are included before the ordinary lists and `Delta` are computed.

Thus topology remains on the fixed skeleton even when the ordinary packet
list is not selected.

### Theorem 6.2 (bounded-sidecar packet theorem)

Suppose, uniformly for all dimensions `k>=k_0` terminalized along one
infinite odd recursion spine:

1. at most `s` exceptional slots use fixed neutral bypasses, every ordinary
   list is pruned against their conflicts, and the complete conflict graph
   and its `Delta` are recomputed; the fixed bypass family is itself jointly
   B0--B3/interface compatible (equivalently, all bypass--bypass conflicts
   are absent, with every higher-arity interface compiled as one super-slot);
2. every nonexceptional slot is then filled by Theorem 5.1;
3. before terminal repair, the literal odd/even words have lengths at most
   `B(k)+c_o` and `B(k)+c_e`, respectively;
4. the odd/even terminal exception families have repair complexity at most
   `r_o,r_e`, include every current missing target and current cap obligation
   exported by a bypass, and yield one fresh integral common-cap matching for
   the repaired terminal chronology;
   and
5. every exported **auxiliary recurrence** exception lies in a fixed bounded
   invariant sidecar family and the next transition regenerates a member of
   that family.

Here `s,c_o,c_e,r_o,r_e` and every bound defining the sidecar family are
absolute constants independent of `k`.

Then

\[
             \nu(k)\le B(k)+C\quad(k\ge k_0\text{ on the covered spine}),
 \qquad C=\max\{c_o+r_o,c_e+r_e\}.                    \tag{6.1}
\]

If each exceptional slot creates at most `gamma_o` or `gamma_e` terminal
holes and there are fixed additional debts `b_o,b_e`, one may use the
literal-listing bound

\[
 C=\max\{c_o+\gamma_o s+b_o,
          c_e+\gamma_e s+b_e\}.                       \tag{6.2}
\]

The parameters `gamma_o,gamma_e,b_o,b_e` in (6.2) are also absolute and
uniform in `k`.

#### Proof

Theorems 3.1 and 5.1 produce a literal terminal chronology of the length in
row 3.  Neutral bypasses retain its topology.  Every target missing in the
current dimension belongs to the terminal exception family and is repaired
now; this costs `r_o` or `r_e`.  Only auxiliary recurrence obligations are
carried, and hypothesis 5 regenerates them in a bounded state at the next
step.  Applying the bounded-cost odd-spine theorem separately to the
covered odd and even terminalizations gives (6.1).  Literal listing gives
(6.2).  Finitely many dimensions below `k_0`, or outside the covered spine,
require separate certificates. \(\square\)

Only one compatible infinite path in the finite/bounded sidecar transition
graph is needed.  Left-totality from every sidecar state is stronger than
necessary.  Conversely, a bounded number of unhosted carrier rows without
neutral bypasses or a regenerative transition is not a sidecar theorem.

The common-cap matching must be freshly integral for each terminal
chronology by B5.  Carrying an old cap assignment through a changed
chronology is not allowed.

## 7. Weakest live all-`k` gate

The corrected route to `B(k)+O(1)` is therefore:

1. choose a path/backbone, or a triangular rooted exchange order together
   with the retained degree/port/endpoint/root rows, so topology is automatic
   for every local option;
2. build complete buffered packet lists including cap witnesses and full
   affected-occurrence halos;
3. prove the global conflict bound and (5.2), outside at most a bounded
   bypassable set;
4. prove that the bounded sidecar regenerates along one infinite odd spine;
   and
5. terminally append only the bounded exception family.

This is weaker than a zero-defect recursive theorem and stronger than local
hex abundance.  The first unproved quantitative assertion is now explicit:
a uniform fully witnessed list-size-to-conflict-degree inequality after the
topology skeleton and cap tickets are fixed.
