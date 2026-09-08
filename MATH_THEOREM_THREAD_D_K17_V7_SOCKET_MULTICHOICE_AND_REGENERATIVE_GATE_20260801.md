# The k=17 v7 socket bank: exact multi-choice regeneration interface and a two-demand catalogue obstruction

Date: 2026-08-01  
Lane: D / SCD facet sockets / child-provider and repeat cocycle  
Status: **exact finite selector equivalence and solver-free obstructions for
the stated frozen menus.  No obstruction is asserted for a prospectively
enlarged socket catalogue, and no k=17 word is claimed.**

## 1. Authoritative starting state

The current calibration is the authenticated v7 SCD socket bank, not the
former v5 bank.  It has

\[
  38\text{ resident sockets},\qquad 6258\text{ resident pieces},
  \qquad 24310\text{ rank-nine owners}.                 \tag{1.1}
\]

Its internal upper-hole counts at ranks 10 through 15 are

\[
                  1485,2454,1593,553,99,9.             \tag{1.2}
\]

The exact two-piece census has no raw zero at ranks 10--15, but its
**context-extendable** zero counts are

\[
                    100,4,0,0,0,0.                    \tag{1.3}
\]

For rank ten, an interval witness contains an adjacent owner pair whose
union is the target.  Therefore each of the 100 rank-ten rows in (1.3) is a
genuine necessary residence obstruction for an intact-piece seam path.
The four rank-eleven rows are different: a longer interval may cross more
than one seam, so they belong to the accumulated-union automaton below and
are not four additional socket demands by fiat.

Every one of the 100 rank-ten rows has one published compact L3 socket.
Their individual extra-cut sum is 213.  Exactly 99 L3 rows are child-clean;
the socket for target 75749 exports the sole unsupported child 14309, and
14309 has clean compact socket choices.  These statements are local.  The
number 213 is **not** a simultaneous cut budget until the options, guards,
facets and shared cuts are selected globally.

The noncanonical pivot-rich geodesic packet is already proved elsewhere.
Nothing below calls it a missing lemma.  This note isolates the separate
finite SCD/socket selector.

Crucially, the joint selector must sit **before** this bank is frozen.  The
old 38 sockets, their component options and guards must themselves be
prospective variables.  Section 6 proves that appending the new sockets to
the immutable v7 bank is impossible.

## 2. A complete physical column

Let \(a\) be one candidate socket, fragment rethread or joint macro.  Its
column must contain all of the following literal data.

1. The set \(F(a)\) of consumed owner occurrences (in particular the
   selected facets), and the ordered replacement owner word.
2. The left and right guard intervals, oriented boundary states and exact
   residence transition.
3. A partial component-option map \(\pi_a:c\mapsto o\), and the set
   \(D(a)\) of newly exposed old boundaries.
4. For every lower colour \(L\) and upper target \(T\), the signed
   occurrence changes
   \(\Delta^-_a(L)\) and \(\Delta^+_a(T)\).  For ranks above ten the latter
   is the complete internal interval deck of the replacement, not a
   fixed-width proxy.
5. The child multiset \(C(a)\), including each old upper occurrence
   destroyed by extraction, and the repeated-parent contribution of the
   socket.
6. The endpoint insertion/current vector, the common-cap state and every
   compiler occurrence address exported by the column.

Items 3--5 make the socket a signed physical column rather than a token
that merely says “cover its parent”.  In particular, let
\(n_T^0(y,d)\) be the exact host occurrence count after choosing the
component options and all standalone/column-induced cuts, but before
inserting replacement columns.  Then after selecting columns \(z_a\) and
ordinary path seams \(x_e\), immediate-upper support is the literal
inequality

\[
 n_T^0(y,d)+\sum_a\Delta^+_a(T)z_a
       +\sum_{e:\,\upsilon(e)=T}x_e\ \ge 1.             \tag{2.1}
\]

Equation (2.1) simultaneously records parent gain, child casualties and
ordinary providers.  A separate recursively generated “child list” is
only a sparse representation of the negative terms in (2.1).

## 3. Exact multi-choice selector

For every host component \(c\) and admissible cut option \(o\), let
\(y_{co}\in\{0,1\}\), with

\[
                         \sum_o y_{co}=1.               \tag{3.1}
\]

For every column \(a\), let \(z_a\in\{0,1\}\).  The local target rows and
component implications are

\[
 \sum_{a:\operatorname{parent}(a)=T}z_a\ge1
       \quad(T\in Z_{10}),
 \qquad z_a\le y_{c,\pi_a(c)}.                          \tag{3.2}
\]

Here \(Z_{10}\) is the current 100-row zero set.  A future joint column may
serve two parents and then appears in both rows of (3.2).

Let \(\operatorname{supp}(a)\) be the union of the selected facet owner
occurrences and every physical owner occurrence in the two guard words.
Physical occurrence resources have capacity one:

\[
                 \sum_{a:u\in\operatorname{supp}(a)}z_a\le1
                 \qquad\text{for every occurrence }u.  \tag{3.3}
\]

The same form applies to any private lower occurrence, endpoint ticket or
compiler address.  Moreover, if boundary \(b\) lies strictly inside a
selected guard interval of \(a\), then

\[
                              z_a+d_b\le1.               \tag{3.4}
\]

Extra cuts are exact union variables.  Let \({\cal A}_b\) include every
socket, rethread, component-option or explicit standalone-cut cause that
creates boundary \(b\), and let \(w_\alpha\) denote its actual selector
(respectively a \(z\)-, \(y\)- or standalone-column variable).  Then

\[
 d_b\ge w_\alpha\quad(\alpha\in{\cal A}_b),
 \qquad d_b\le\sum_{\alpha\in{\cal A}_b}w_\alpha.     \tag{3.5}
\]

Thus \(d_b\) is the OR of the selected causes and cannot turn on for free.
The cut budget is the cardinality of this union, not the sum of the
per-column cut counts.  Equations (2.1)--(3.5), together
with the lower rows below, are the exact correlated child-provider layer.

After applying the chosen cuts and columns, let \({\cal P}(y,z,d)\) be the
literal resulting resident pieces.  Choose one orientation per piece and
one directed seam \(x_e\) between successive pieces.  With source and sink
indicators \(s_p,t_p\), impose

\[
 \deg^-(p)+s_p=1,
 \quad \deg^+(p)+t_p=1,
 \quad \sum_p s_p=\sum_p t_p=1,                         \tag{3.6}
\]

and the graphic rows

\[
                 \sum_{e\in E(S)}x_e\le |S|-1
                 \qquad(\varnothing\ne S\subseteq{\cal P}). \tag{3.7}
\]

Together with \(\sum_e x_e=|{\cal P}|-1\), the degree and graphic rows are
exactly one
directed Hamilton path on the pieces.  Every chosen seam must pass the
literal capped run automata for all 17 coordinates.

### Theorem 3.1 (finite selector equivalence)

Fix a collision-complete finite catalogue whose columns include their
complete data from Section 2 and whose typed capacity/general-feasibility
rows record every higher-order interaction.  Such an integral solution
exists if and only if a resident compiler-ready Hamilton path is obtainable
from that catalogue, provided the solution records the literal decomposition
used to materialize each selected column.  Pairwise binary no-goods alone
do not imply collision-completeness.  No uniqueness or bijection between
encodings and paths is claimed.

#### Proof

Given a physical path with a catalogue decomposition, read off its component options, selected local
rethreads, cuts, piece orientations and seams.  Resource disjointness and
all signed incidence equations hold by literal counting; (3.7) holds
because a path has no cycle.

Conversely, (3.1)--(3.5) make the selected replacements simultaneously
embeddable in one owner deck.  Materialize them and cut at the selected
union of boundaries.  The degree and graphic rows concatenate every resulting
piece exactly once into one path.  The residence automata validate every
new boundary.  The lower, upper and compiler rows then give the claimed
literal palettes and common-cap source word.  No projection or rounding is
used.  \(\square\)

The theorem is dimension-uniform but conditional on catalogue supply.  It
does not say that the present two-option catalogue is complete.

## 4. Exact lower-repeat and immediate-upper cocycles

The exact prospective lower count is

\[
 n_L^-(y,d,z,x)=n_L^{-,0}(y,d)
   +\sum_a\Delta_a^-(L)z_a
   +\sum_{e:\,\lambda(e)=L}x_e.                        \tag{4.0}
\]

Here \(n_L^{-,0}(y,d)\), like its upper analogue in (2.1), is recomputed
after the selected component options and cuts.  The compiler imposes its
required occurrence degree on (4.0); a fixed-host constant is not sound.

The fixed v7 pieces have 18,052 internal edges but only 17,974 distinct
rank-eight intersections.  Their multiplicity histogram is

\[
                   1^{17897}2^{76}3^1,                  \tag{4.1}
\]

so the internal lower repeat excess is 78.  With 6257 seams, an intact-piece
path can contain at most

\[
                         17974+6257=24231               \tag{4.2}
\]

of the 24,310 lower colours.  Thus it has at least 79 lower holes.  A path
with the ideal single forced boundary hole must release at least one
occurrence from each doubled colour and two from the tripled colour:

\[
 \sum_{e\in E_L^{\rm int}}d_e\ge m_L-1,
 \qquad \sum_L(m_L-1)=78.                               \tag{4.3}
\]

Socket extraction cuts may discharge rows of (4.3), but only their literal
intersection colours count.  The 78 and 213 ledgers cannot be subtracted or
added scalarly.

The fixed pieces have 17,963 distinct immediate-upper colours and 89
internal repeat units, hence 1485 rank-ten holes.  If an intact-piece path
were rank-ten complete, exactly 1485 of its 6257 seams would be first
providers and 4772 seam occurrences would be repeats.  Together with the
89 internal repeats this gives the forced total

\[
                         4772+89=4861.                  \tag{4.4}
\]

Prospective cuts and sockets change all three summands in (4.4), so the
master must recompute them from the signed columns.

More generally, let \({\cal H}\) and \({\cal L}\) be the lower missing and
repeat-excess multisets after all selections, \({\cal R}\) the upper
rank-ten repeat-excess multiset, and \(T^-,T^+\) the endpoint owners.  Every
upper-complete owner path obeys

\[
 |{\cal H}|=|{\cal L}|+1,
 \qquad
 d_{\cal R}(q)=2860+d_{\cal H}(q)-d_{\cal L}(q)
 -\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}.             \tag{4.5}
\]

This is the exact child-provider/repeat cocycle.  Cardinality alone is not
enough.

## 5. Ranks 11--15 and common history

For each target \(T\) of rank 10 through 15, scan the final owner path with
state \(A\subseteq T\):

\[
 A\longmapsto
 \begin{cases}
 A\cup X,&X\subseteq T,\\
 \varnothing,&X\not\subseteq T.
 \end{cases}                                             \tag{5.1}
\]

The target is covered exactly when state \(T\) is reached.  Indeed every
witness lies in a maximal consecutive block of owners contained in \(T\),
and that block's union is \(T\).  Thus (5.1) is necessary and sufficient
for arbitrary-width upper coverage.  It uses the same selected chronology
for every rank; independent per-rank seam providers are insufficient.

The terminal compiler is likewise occurrence-labelled.  Every lower cell
selected by its matching must be admissible under one common maximal cap
\(Q\).  A symmetric or equivariant aggregate matching cannot replace this
row.

## 6. A sharp obstruction in the currently published option menu

The file
`scratch/k17_socket_v7_extendable_zero100_compact_sockets_20260801.tsv`
contains exactly two choices for each of the 100 demands: one L3 and one L4
socket.  This complete **frozen two-choice menu** is not jointly selectable.

### Theorem 6.1 (two-target resource obstruction)

Within that menu, targets 8060 and 15996 cannot both be served.

#### Proof

Both choices for 8060 contain facet owner 7804 and require option 6 on
component 22.  Both choices for 15996 contain the same facet owner 7804 and
require option 3 on component 22.  Hence every one of the four cross-choice
pairs violates both the owner-capacity row (3.3) and the component-option
row (3.2).  \(\square\)

The independent audit finds 25 target pairs for which all four L3/L4
cross-choice pairs have an already visible facet, component-option or
equal-guard conflict.  One pair suffices for Theorem 6.1.  These are
catalogue obstructions, not impossibility results for new nonnested sockets
or joint multi-target macros.  The weakest repair of the displayed pair is
one of:

1. a new 8060 option that avoids the 7804/component-22 spine;
2. a new 15996 option that avoids that spine; or
3. one joint column that uses owner 7804 once and serves both parents with
   a complete combined guard/child ledger.

### Corollary 6.1 (exact menu-broadening floor)

The 25-edge target no-good graph has minimum vertex-cover number 19.
Consequently at least 19 target menus must acquire a new option (counting a
joint multi-target column in every demand menu it serves) before the frozen
two-choice menu can become selectable.

Indeed, the graph is the disjoint union of 13 copies of (K_2), one
(K_4) on `22206,32391,73395,73635`, the four-edge tree with centre
`82931` and branch `82931-73586-67451`, and the path
`69342-73434-73688`.  Their cover numbers are respectively
(13,3,2,1).  In the stricter all-L3 architecture, the exact conflict
graph has 100 edges and an explicit matching of size 37, so at least 37 of
those frozen L3 columns must be replaced.  Both bounds are menu-relative.

There is a second, easily confused menu issue.  The generation-three clean
L3 and L4 sockets for child 14309 use right state 1510, segment 755 and
component 248.  Those resources are already the left guard of frozen v7
socket 69605.  Therefore a builder that hard-wires the first
generation-three child row aborts, but this is not an atlas no-go.  Two
compatible clean alternatives are already literal:

* the generation-three L5 row uses right state 1596, segment 798 and
  component 260 and costs seven extra cuts;
* the round-one external L3 row uses guards
  `(state,segment,component)=(1439,719,234)` and `(785,392,132)` and costs
  only two extra cuts, but it shares facet occurrence `(557,0)`, owner
  10213, with its parent-75749 L3 socket;

Neither has a physical conflict with the frozen 38 rows in the independent
audit, but only the generation-three L5 is also conflict-free against the
chosen parent-75749 L3 row.  Thus the two-cut L3 is not a regenerative
parent--child closure.  The child row must be a genuine menu variable, not
the first row in a file; for the displayed parent and frozen bank the L5 is
the currently certified compatible choice.

### Theorem 6.2 (frozen-bank append obstruction)

Even after choosing a compatible child row, the 100 sockets cannot be
bolted onto the immutable 38-socket bank.

#### Proof

The independent physical conflict audit tests component options, full
half-open guard overlaps, facets inside guards, extra cuts splitting guards
and facet occurrence capacity.  With the compatible generation-three L5
child installed, only 21 of the 200 candidate rows remain individually
viable.  They serve only 13 targets; 87 targets have no viable choice.
The exact prepared builder, which also propagates its component guard
domains, retains only 17 rows over 12 targets and reports 88 locally dead
targets before search.  Either certificate already contradicts (3.2) for
the fixed bank.  \(\square\)

The one-target discrepancy, 87 versus 88, is expected: the first audit is
the physical conflict projection, while the builder additionally propagates
the selected component/guard domains.  Neither result is a no-go for the
prospective model in which the old 38 sockets may be changed or removed.

## 7. Why ordinary Hall or matroid intersection does not finish the gate

Even the facet-only selector is a multi-resource hypergraph set-packing
problem: one socket column meets several owner-capacity rows.  Guards,
child balance, lower repeats and the graphic path row add further
independent resource systems.  The four-way obstruction of Theorem 6.1 is
already a two-part colourful compatibility failure; the full selector is a
multiple-choice hypergraph matching coupled to a graphic matroid and shared
history automata.  Its matrix is not a directed network matrix, and no TU
or ordinary Rado theorem follows.

A useful exact separation hierarchy is nevertheless available:

1. reject incompatible component assignments and resource cliques;
2. separate child-balance and lower-repeat Hall rows (2.1),(4.3);
3. separate directed cycle cuts (3.7);
4. replay residence and add forbidden transition cores;
5. separate the accumulated-union automata (5.1);
6. invoke the occurrence-labelled common-cap compiler.

Every negative certificate then has a precise scope.  Theorem 6.1 closes
the present nested L3/L4 menu, while Theorem 6.2 closes append-only repair of
the frozen v7 bank.  Neither closes the prospective regenerative master.

## 8. Reusable regenerative statement

### Theorem 8.1 (regenerative column certificate)

Let a family of hosts in arbitrary dimension carry finite column catalogues
as in Section 2.  Suppose every initial demand has a chosen parent column,
every exported child is paid by an ordinary provider or another chosen
column, all columns are resource-disjoint and option-compatible, (4.5)
holds with the required lower/compiler degree vector, and the selected
pieces satisfy (3.6)--(3.7), residence, (5.1) and one common cap.  Then the
materialized chronology is a resident, all-upper-exact, compiler-ready
Hamilton owner path.

#### Proof

The exact cut-OR, component-option and occurrence-capacity rows first
materialize one owner-disjoint family of literal replacement words.  The
degree, edge-count and graphic rows concatenate all resulting pieces into
one directed path, and the run automata certify every internal and external
boundary.  Paying a child means paying its *signed occurrence unit* in
(2.1), rather than merely naming another socket; hence all rank-ten rows
hold after the simultaneous materialization.  Recurrence (5.1) then checks
every longer upper interval in that same path.  Finally (4.0), (4.5) and the
occurrence-labelled common-cap matching certify the lower/compiler cells.
All hypotheses concern finite literal incidences or automaton states, so no
unconstructed chronology is assumed.  \(\square\)

A decreasing-potential child DAG is a sufficient sparse implementation of
the signed-payment hypothesis: direct ordinary providers are the sinks, and
processing socket casualties from smaller to larger potential proves (2.1)
inductively.  It is not necessary, and a list of individually clean children
is not enough unless the simultaneous cut/option materialization preserves
their advertised providers.

There is a checkable positive supply condition on a prepared face.  Fix the
component states, a common protected-provider bank and a topology face on
which every compatible option union is graphic-safe.  If the collision graph
(G) captures every remaining incompatibility and every demand menu obeys

[
                 |{cal P}_U|gemax{1,2Delta(G)},
]

then Haxell's independent-transversal theorem selects one compatible option
per demand.  Combined with the signed occurrence, residence and common-cap
rows of Theorem 8.1, this gives a regenerative certificate.  The fixed-face
and collision-completeness hypotheses are essential; the inequality is not
a theorem about the raw socket menus alone.

This is a noncircular regeneration lemma: its hypotheses are finite
incidence, automaton and matching rows and its conclusion is a literal
chronology.  The still-missing all-dimensional theorem is **supply** of such
columns with bounded live child/resource debt.  The v7 data prove local
socket supply but, by Theorem 6.1, the published nested option menu lacks
the required correlation.

## 9. Artifacts and scope

The solver-free menu and cocycle audit is

* `scratch/audit_threadD_k17_v7_socket_multichoice_20260801.py`;
* `scratch/threadD_k17_v7_socket_multichoice_20260801.audit.json`.

The independent child/resource referee audit is

* `scratch/audit_threadD_k17_v7_socket_multichoice_gate_20260801.py`;
* `scratch/threadD_k17_v7_socket_multichoice_gate_20260801.audit.json`.

The full physical frozen-bank scope audit and the exact prepared builder
diagnostic are

* `scratch/audit_threadD_k17_v7_socket_selector_scope_20260801.py`;
* `scratch/threadD_k17_v7_socket_selector_scope_20260801.audit.json`;
* `scratch/build_k17_v7_extendable100_socket_selector_cnf_20260801.cpp`;
* `scratch/k17_v7_fixed38_extendable100_socket_selector_20260801.builder.out`.

The independent vertex-cover/Haxell audit is

* `scratch/audit_r_k17_v7_tau19_haxell_20260801.py`;
* `scratch/r_k17_v7_tau19_haxell_20260801.audit.json`.

Together they replay (1.1)--(1.3), the 100/200 menu, the 213 and 99/1
ledgers, both kinds of child compatibility, Theorem 6.1, all 25 pairwise
menu no-goods, the exact 87/88 frozen-bank distinction and the fixed-piece
lower/upper multiplicities.  They do not claim that all
possible sockets have been enumerated, solve the enlarged selector, or
prove `nu(17)=B(17)`.
