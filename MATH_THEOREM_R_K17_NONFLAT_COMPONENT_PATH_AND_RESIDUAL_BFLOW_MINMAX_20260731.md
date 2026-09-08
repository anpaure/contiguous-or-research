# The nonflat component path and residual port completion have an exact Hall--cut master

Date: 2026-07-31  
Status: exact abstract theorem and scoped `K17` reduction; six occurrence
swaps clean the marked interiors, and the complete radius-one occurrence
neighbourhood is solver-free path-infeasible; radius two/Steiner sockets
remain open and no `K17` word is claimed

## 0. Result and scope

The new nonflat phase ledger changes the correct unit of rethreading.  The
selected objects should not be opened as 108 independent A segments.  In
the original macro forest they met 106 components whose closure contained
190 macros and 3,970 owners; six closures carried 32 strict internal D2
defects.

Six explicit occurrence swaps now rebuild the same 108 required macros into
106 marked components whose closure has only 154 macros and 3,815 owners.
Every marked component has zero strict internal D2 and D3 debt.  This removes
the former six-component obstruction, but it does not make the endpoint
master feasible.  In the exact repaired one-old-`U` connector catalogue,
required singleton component 77 has no residence-clean incidence in either
orientation.  Its singleton marked-connectivity cut is literally

\[
                         x(\delta(\{77\}))\ge1
                         \quad\Longleftrightarrow\quad 0\ge1.      \tag{0.1}
\]

All six geometric incidences create one D2 run of length two and one D3 run
of length three, through owner `0x40ff` on coordinate 0 or 14, or owner
`0x5b33` on coordinate 9.  Thus the repaired fixed-endpoint,
one-owner-per-join face is infeasible before distinct-owner Hall or residual
flow.

There is a second scope boundary.  The marked closure is clean, but the raw
complementary macro words are not: among 883 nonempty unmarked components,
82 contain 320 strict internal D2 defects and no D3 defect.  Consequently a
literal global macro-phase completion must also rethread the complement.
Alternatively, a two-bank construction may use a separately audited facet
phase; marked cleanliness alone does not certify it.

This note proves the exact component-neutral contraction, fixed-order Hall
criterion, residual capacitated-Hall criterion, and complete pair-column/cut
formulation.  It also proves why the unfixed coupled problem is not ordinary
flow or two-matroid intersection: a minimal four-column parity fixture
passes every two-coordinate Hall projection but has no integral connector
pair.  On the current repaired instance these general rows are preceded by
the explicit singleton cut (0.1).

The original `106/190/3970` ledger and its six-component obstruction are
independently frozen in
`MATH_THEOREM_K17_MARKED_MACRO_COMPONENT_TWO_BANK_OBSTRUCTION_20260731.md`.
The repaired `106/154/3815` ledger and component-77 cut are frozen in
`MATH_AUDIT_K17_SIXSWAP_REPAIRED_COMPONENT_PATH_GATE_20260731.md`.

## 1. Port-forest normal form

Let (F=(T,E_F)) be a finite linear forest.  Its vertices are the literal
port colours, and its components are denoted by

\[
                         \mathcal C=\pi_0(F),\qquad c=|\mathcal C|.
\]

Put

\[
                         d_t=2-\deg_F(t).                         \tag{1.1}
\]

Thus a nontrivial path component has one unit of demand at each endpoint;
an isolated vertex has two occurrence-labelled halfports at the same colour.
Let \(H\) be the resulting multiset of halfports, with colour map
\(\tau:H\to T\) and component map \(\gamma:H\to\mathcal C\).  Then every
component contributes exactly two halfports and

\[
 |H|=\sum_{t\in T}d_t
     =2|T|-2|E_F|=2c.                              \tag{1.2}
\]

Let \(\mathcal U\) be the pure-owner deck.  A pure owner \(u\) is installed
by choosing two distinct incident port colours (t,t'\subset u); physically
this is the two-edge path (t-u-t').  In the parent-induced odd-diamond
factor one has

\[
                         |\mathcal U|=c.                         \tag{1.3}
\]

Equations (1.2)--(1.3) are the exact zero-slack ledger: every pure owner must
use two incidences and every halfport must be consumed once.

For the authenticated current `K17` macro forest,

\[
 |T|=6435,\qquad |E_F|=1430,\qquad
 c=|\mathcal U|=5005.                              \tag{1.4}
\]

## 2. Marked-path contraction is component-neutral

Let \(\mathcal M\subseteq\mathcal C\) be a marked component bank of size
(m\).  A **typed marked chain** consists of

* an order (C_1,\ldots,C_m) of the marked components;
* one orientation of every (C_i);
* distinct owners (u_1,\ldots,u_{m-1}\); and
* for every (i<m), the exit halfport of (C_i) and entry halfport of
  (C_{i+1}), both incident with (u_i),

such that the literal depth-two/depth-three seam transducer accepts every
join.  Any fixed common-cap or palette guard may also be included in the
definition of an accepted join.

### Theorem 2.1 (neutral contraction and two-bank contiguity)

Installing a typed marked chain consumes (m-1) pure owners and (2m-2)
halfports, and it replaces the (m) marked components by one path
supercomponent (C_\star).  The residual instance has

\[
 c'=c-m+1,qquad |\mathcal U'|=c-m+1,qquad |H'|=2(c-m+1).       \tag{2.1}
\]

Hence the contraction is exactly capacity-neutral.

If the residual completion is connected, the final quotient is one cycle
and the marked components occur consecutively on that cycle.  Deleting one
of the two marked--unmarked interface incidences opens a linear order in
which the marked bank and its complement are each contiguous and exactly
one interface remains.

#### Proof

Every installed owner joins two previously distinct consecutive marked
components, so (m-1) joins turn them into one path and consume exactly
(2m-2) of their (2m) halfports.  Thus two halfports remain on
(C_\star).  The component and owner counts in (2.1) both decrease by
(m-1), and (1.2) gives the residual halfport count.

After all degrees are completed, every component vertex and every pure
owner vertex has degree two in the contracted bipartite multigraph.
Connectedness therefore makes it one cycle.  No residual edge can enter the
interior of (C_\star), whose internal halfports have already been spent;
the cycle enters and leaves only at its two ends.  Hence the marked path is
one cyclic interval, and its complement is the other.  Opening one of the
two crossing incidences leaves the other as the unique linear interface.
\(\square\)

For a balanced post-split forest whose clean marked bank again has
(m=106), (2.1) specializes to

\[
 105\text{ marked connectors},\qquad
 c'=|\mathcal U'|=4900,\qquad |H'|=9800.             \tag{2.2}
\]

Thus a clean nonflat bank would spend no owner or port slack.  The frozen
forest does not satisfy the theorem's internal-cleanliness premise; the six
required splits must also preserve the balanced component/owner identity.

## 3. The two exact Hall rows after an order is fixed

Fix an oriented marked-component order.  It has gaps
(g_1,\ldots,g_{m-1}).  Let (L(g_i)\subseteq\mathcal U) be the owners
which contain both literal endpoint colours and whose connector passes all
declared seam, palette, and fixed-cap guards.

### Theorem 3.1 (rainbow gap Hall)

The fixed marked order can be labelled by distinct pure owners if and only
if

\[
 \boxed{\left|\bigcup_{g\in I}L(g)\right|\ge |I|
        \quad\text{for every }I\subseteq\{g_1,\ldots,g_{m-1}\}.} \tag{3.1}
\]

#### Proof

This is Hall's theorem in the bipartite graph between the gaps and the pure
owners.  A saturating matching is exactly a distinct-owner labelling of all
marked joins.  \(\square\)

Now fix one such labelled chain \(P\).  Let \(G_P\) be the residual simple
incidence graph between the unused owners \(\mathcal U_P\) and the port
colours (T), and let (d_t^P) be the residual demand.  Initially ignore
pair-specific residence or cap restrictions, or assume they are
**Cartesian**: any two distinct individually allowed incidences of one owner
form an allowed connector.

### Theorem 3.2 (residual capacitated Hall)

Assume

\[
                         \sum_t d_t^P=2|\mathcal U_P|.             \tag{3.2}
\]

There is an integral residual incidence completion if and only if, for every
(A\subseteq\mathcal U_P),

\[
 \boxed{
 2|A|\le\sum_{t\in T}
       \min\bigl(d_t^P,|N_{G_P}(t)\cap A|\bigr).}                 \tag{3.3}
\]

#### Proof

Use a source--owner--port--sink network.  Source--owner capacities are two,
owner--port capacities are one, and port--sink capacities are (d_t^P).
For a fixed owner set (A), minimizing the cut placement of one port (t)
costs the smaller of (d_t^P) and (|N(t)\cap A|).  Hence (3.3) is exactly
the max-flow/min-cut condition for saturating every source--owner arc.
Integral capacities give an integral flow.  The unit owner--port capacities
forbid using the same port colour twice at one owner.  \(\square\)

Define the residual Hall deficiency of a labelled chain by

\[
 \delta(P)=\max_{A\subseteq\mathcal U_P}
 \left(2|A|-\sum_t
       \min(d_t^P,|N_{G_P}(t)\cap A|)\right).                    \tag{3.4}
\]

The empty set shows (delta(P)\ge0).  Thus, on a Cartesian residual face,
the exact coupled degree min--max is

\[
 \boxed{\min_{P\in\mathfrak P_{\mathcal M}}\delta(P)=0,}        \tag{3.5}
\]

where \(\mathfrak P_{\mathcal M}\) is the set of typed, distinctly labelled
marked chains.  Formula (3.5) is necessary and sufficient for a marked path
plus a residual **degree** completion.  It says explicitly why one may not
optimize the marked path and residual flow independently.

## 4. Connectivity and pair-specific guards

Degree Hall does not imply a single cycle.  For fixed \(P\), let
\(\mathcal B(P)\) be the integral residual degree completions and let
\(\Pi(P)\) be the component partition after contracting the marked chain.
For \(B\in\mathcal B(P)\) and a union \(W\) of components, write
\(\partial_BW\) for the chosen pure-owner connectors with exactly one port
in (W).  Then

\[
 \boxed{
 P\text{ has a connected residual completion}
 \iff
 \max_{B\in\mathcal B(P)}
 \min_{\varnothing\ne W\subsetneq\Pi(P)}|\partial_BW|\ge1.}     \tag{4.1}
\]

This is an exact max--min criterion, not a relaxation: the inner minimum is
positive precisely when the contracted completion is connected.  Because
all contracted degrees are even, a positive cut actually has size at least
two.

For the fully literal model, retain occurrence-labelled halfports.  For
each unused owner \(u\), let \(\mathcal A_u(P)\) be its allowed unordered
pairs ({h,h'}) of distinct residual halfports.  The pair is included only
when

1. \(\tau(h),\tau(h')\subset u\) and \(\tau(h)\ne\tau(h')\);
2. the two-ended depth-two/depth-three seam transducer accepts it;
3. its lower/upper provider column is legal; and
4. its physical collar is compatible with the declared common cap, when a
   cap has been fixed.

With Boolean columns (z_{u,{h,h'}}), the exact residual master is

\[
\begin{aligned}
 \sum_{a\in\mathcal A_u(P)}z_{u,a}&=1
                    &&(u\in\mathcal U_P),\\
 \sum_{u,a\ni h}z_{u,a}&=1
                    &&(h\in H_P),                                  \tag{4.2}\\
 \sum_{u,a:\,a\text{ crosses }W}z_{u,a}&\ge1
                    &&(\varnothing\ne W\subsetneq\Pi(P)).
\end{aligned}
\]

### Theorem 4.1 (exact pair-column criterion)

For a fixed typed marked chain (P), (4.2) is feasible if and only if that
chain extends to a literal connected pure-owner completion satisfying all
pair guards used to define the column families.

#### Proof

The first row uses every remaining owner exactly once.  The second uses
every remaining halfport exactly once.  Thus every quotient vertex has
degree two.  The third row is exactly connectedness after the fixed forest
and marked chain are contracted.  Expanding each chosen column to its two
physical incidences gives the desired completion.  Conversely every literal
completion selects one such column for every owner and satisfies all three
rows.  \(\square\)

The same formulation can choose the marked chain rather than receive it as
input.  In the full column family require

\[
 \sum_{u,a:\,\gamma(a)\subseteq\mathcal M}z_{u,a}=m-1             \tag{4.3}
\]

and, for every nonempty proper \(\mathcal S\subsetneq\mathcal M\),

\[
 \sum_{u,a:\,a\text{ crosses }(\mathcal S,\mathcal M\setminus\mathcal S)}
 z_{u,a}\ge1.                                                       \tag{4.4}
\]

The internal marked connector graph is then a connected graph on (m)
vertices with (m-1) edges.  It is a tree; the global degree-two rows make
its maximum degree at most two, so it is a path.  Equations (4.2)--(4.4) are
therefore a lossless exact simultaneous marked-path/residual-completion
master.  They also force exactly two marked--unmarked connector columns.

## 5. Matroid boundary and the minimal Hall obstruction

If an orientation and component order are fixed, Theorem 3.1 is an
intersection of two partition matroids, hence ordinary bipartite matching.
The residual Cartesian degree row is likewise a bipartite `b`-matching.
The unfixed problem is different.

There is an exact natural matroid description after fixing one orientation
of every marked component but before fixing their order.  On the ground set
of legal directed, owner-labelled component arcs, let

* (M_{\rm out}) be the partition matroid of capacity one per tail;
* (M_{\rm in}) be the partition matroid of capacity one per head;
* (M_U) be the partition matroid of capacity one per owner label; and
* (M_G) be the graphic matroid of the underlying undirected component
  edge.

A set of (m-1) arcs independent in all four matroids is exactly a
distinct-owner directed Hamilton path on the marked components.  Indeed
graphic independence with (m-1) edges makes the underlying graph a tree,
and the in/out caps make its maximum degree at most two and orient every
internal vertex with one entering and one leaving arc.  Conversely every
such path is independent in all four matroids.  This is an exact criterion,
but it is a four-matroid intersection, not the polynomial two-matroid
intersection covered by Edmonds' min--max theorem.  If component orientation
is also variable, consistent use of its two physical halfports is an
additional state/partition row; the pair-column master (4.2)--(4.4) is the
lossless formulation.

An oriented connector column simultaneously consumes

* one outgoing component slot;
* one incoming component slot; and
* one pure-owner label.

Thus even before connectivity it is a three-resource matching.  The four
columns

\[
 (g_1,c_1,u_1),\quad(g_1,c_2,u_2),\quad
 (g_2,c_1,u_2),\quad(g_2,c_2,u_1)                  \tag{5.1}
\]

give the minimal parity obstruction.  Every two-coordinate projection is
the complete (K_{2,2}), and assigning weight (1/2) to all four columns
satisfies every marginal quota.  Nevertheless no two columns are disjoint
in all three coordinates, so no integral two-gap connector exists.

Consequently, in the natural connector-column formulation:

1. separate Hall tests on component adjacency, owner labels, and endpoint
   ports are not sufficient;
2. the displayed resource rows are three partition constraints, so no
   ordinary two-matroid/Edmonds criterion follows from them;
3. global connectivity adds a further graphic/subtour row; and
4. a solver-free Edmonds rank criterion requires an additional
   private/aligned hypothesis which collapses one of the three resources.

This does not prove that no specially represented matroid formulation could
exist for the Boolean-containment instance.  It proves that marginal Hall
and the natural two-resource projection are insufficient.  The obstruction
disappears after a complete oriented component order and
its endpoint ports are fixed: only the gap and owner coordinates remain,
and (3.1) is then exact.

There is also a topology obstruction beyond Hall.  Two disjoint groups can
each possess a perfect residual degree flow, so (3.3) holds, while no allowed
connector crosses the group cut.  Equation (4.1), or equivalently the last
row of (4.2), detects this and ordinary Hall does not.

## 6. The currently isolated finite obstructions

### 6.1 The frozen whole-component bank fails before Hall

The exact closure census is

\[
 106\text{ marked components},\quad190\text{ macros},\quad3970\text{ owners}.
\]

Six components contain 32 strict internal D2 length-two runs in optional
macros.  Component reversal preserves these runs, and a `U` connector can
touch only the two external halfports.  Therefore every pair-column family
for the unmodified whole-component bank is rejected by the internal
residence predicate before (3.1), (3.3), or (4.2) is tested.  This is a
pre-Hall obstruction, not a deficient-set certificate.

In every bad component the unique required macro is an endpoint edge.  One
local forest split per bad component separates it from the bad optional
tail.  Thus six component-local splits are necessary within this escape
class.  They are not sufficient: the changed macro incidences must be
rebalanced so that (1.3) remains true, and the resulting instance must still
pass the marked path, residual Hall, topology, palette, and common-cap rows.

### 6.2 Endpoint-only splicing has an actual Hall witness

The old endpoint-only splice graph has only 70 arcs and 50 isolated marked
states.  In its bipartite path-cover graph, a Hamilton path may leave only
one outgoing copy and one incoming copy unmatched.  Taking the 50 isolated
outgoing copies gives

\[
                         |N(S)|=0<49=|S|-1.                         \tag{6.1}
\]

Thus endpoint-only splicing fails by a singleton-union Hall deficiency of
at least 49; this is stronger than merely saying that a search found no
path.

The detached whole-required-macro residence graph is different: the frozen
root census has 3,146 directed arcs, minimum outdegree five, and an explicit
108-macro Hamilton path.  Those facts remove the old singleton obstruction
but do not repair the 32 optional-tail runs forced by component closure and
do not certify a **post-split, distinctly U-labelled** component path.
At that stage candidate owner lists for the six-socket exchange had not been
frozen.  Section 6.3 supersedes that branch with the later six-occurrence
forest repair and its new exact endpoint obstruction.

### 6.3 The six-swap repair reaches a new singleton-cut obstruction

The cumulative six-occurrence witness changes the macro forest itself.  Its
marked closure has 106 components, 154 macros and 3,815 owner tokens, with
zero internal D2/D3 debt.  Its fixed-endpoint catalogue has 412 geometric
directed arcs and 312 residence-clean arcs using 140 pure-owner labels.
Nevertheless required singleton component 77, global forest component 1269,
has no clean incident arc in either orientation.  It is macro 18, with
rank-eight ports 0x40fe,0x5933 and a 111-owner word.

The only possible geometric owners are 0x40ff and 0x5b33.  In both directions
they create respectively a D2 run of length two and derivative D3 run of
length three, on coordinate 0, 14, or 9.  Hence the component cut in (4.4)
for the singleton marked set is empty.  This is a literal
connectivity-support obstruction:

\[
                   \sum_{a\text{ crosses }\{77\}}z_a=0<1.       \tag{6.2}
\]

The unconditioned owner-to-port flow still passes 10010/10010.  It checks
only the case before choosing 105 marked owners or consuming their 210
halfports; it cannot repair (6.2) and says nothing about the conditioned
Hall inequalities.  Moreover, if the raw unmarked macro words are retained
as the complementary physical phase, 82 unmarked components contain 320
strict internal D2 defects.  Thus both a component-77 socket and a clean
complement chronology are required in that literal two-bank architecture.

### 6.4 Occurrence choice is an outer exact configuration variable

Let \(\Omega\) be any finite declared family of occurrence transversals.
For \(\tau\in\Omega\), rebuild literally the macro forest \(F_\tau\),
its marked bank \(\mathcal M_\tau\), and its oriented residence-clean,
owner-labelled connector set \(A_\tau\).  States which split a forced
packet or have an internally bad marked component are deleted.

Fix one orientation \(o(C)\) of each marked component.  On
\(A_\tau(o)\), use the out-partition, in-partition, owner-label partition
and underlying graphic matroids from Section 5, and put

\[
 r_\tau(o)=\max\{|I|:I\subseteq A_\tau(o)
   \text{ is independent in all four matroids}\}.               \tag{6.3}
\]

Then the exact marked-path deficiency of the occurrence state is

\[
 p(\tau)=|\mathcal M_\tau|-1-\max_o r_\tau(o).                \tag{6.4}
\]

Thus a distinctly labelled clean marked Hamilton path exists in the
declared occurrence family if and only if

\[
                         \min_{\tau\in\Omega}p(\tau)=0.        \tag{6.5}
\]

This is the precise way occurrence choice enters the matroid layer.  It is
not a perturbation of a fixed flow: changing \(\tau\) may change the
forest components, marked closure, endpoint ports, allowed owner labels,
internal words and residual demands simultaneously.

For a fast exact presolve, let \(w(\tau)\) be the number of weak
components of the unoriented clean connector projection, let
\(\ell(\tau)\) be its number of degree-one marked vertices, and let
\(\nu(B_\tau)\) be the maximum matching in the tail--head projection.
Every marked Hamilton path requires

\[
 w(\tau)=1,\qquad \ell(\tau)\le2,qquad
 \nu(B_\tau)\ge |\mathcal M_\tau|-1.                          \tag{6.6}
\]

Moreover, if one freezes \(\tau\) and augments its connector graph by
new socket adjacencies, their number is at least

\[
 \max\left\{
   w(\tau)-1,\ 
   \left\lceil\frac{\ell(\tau)-2}{2}\right\rceil,\ 
   |\mathcal M_\tau|-1-\nu(B_\tau)
 \right\}.                                                       \tag{6.7}
\]

Indeed one new edge merges at most two weak components, touches at most two
forced leaves, and increases a matching by at most one.

The complete radius-one census about the six-swap residence-zero state now
closes this occurrence face without path SAT:

```text
all one-coordinate neighbours                         1430
internally residence-clean                            1411
with no isolated marked component                      122
with connected clean connector projection                0
satisfying the path degree necessity                     0
minimum forced leaves                                    21
```

The best weak-component shapes are \([102,2,2]\) for 106 marked
components and \([103,2,2]\) for 107.  Hence every radius-one state fails
the first condition in (6.6), and (6.7) gives a fixed-state socket-edge
floor of at least ten from \(\ell\ge21\).  This is not a ten-occurrence-
move floor: one further occurrence exchange can alter many connector edges
at once.  Exactly twelve radius-one states attain the three-component
frontier, so only those twelve need be extended in the radius-two
occurrence search.

For the closure-minimizing seventh move

```text
21006: (0,1121) -> (0,4318),
```

the marked closure is 153 macros/3,800 owner tokens and its clean projection
has shape \([102,2,2]\) with 22 forced leaves.  The two islands are the
global component pairs \(\{1856,2820\}\) and \(\{2435,2440\}\),
whose sole internal owner labels are respectively 28053 and 11993.  The
tail--head projection has matching number 103, with Hall witness

\[
 S=\{47,52,66,73,75,78,92,97\},\qquad
 N(S)=\{15,31,51,56,84\}.                              \tag{6.9}
\]

Thus (6.7) specializes to

\[
 \max\{3-1,\lceil(22-2)/2\rceil,105-103\}=10.        \tag{6.10}
\]

Equality in (6.10) is rigid: ten new adjacency units must form a matching
which touches exactly 20 of the 22 forced leaves, the other two becoming the
global path endpoints, and at least two units must join the two small
islands to the large component.  Any unit incident with a degree-at-least-two
vertex or any repeated forced leaf raises the socket-edge requirement to at
least eleven.

This move must be pinned literally when reproducing the witness.  The current
census ordering no longer places it in row zero, although the frozen
premaster flow below authenticates the stated move and ledger.

For any occurrence state passing (6.5), the residual degree criterion is
still Theorem 3.2 with the state- and path-dependent demands and unused
owners.  In exact min--max form, on a Cartesian residual face it is

\[
 \min_{\tau\in\Omega} 
 \min_{P\in\mathcal H_\tau}
 \max_{A\subseteq\mathcal U_\tau\setminus L(P)}
 \left(
 2|A|-
 \sum_T\min\{d_T^\tau-\eta_T(P),|N_\tau(T)\cap A|\}
 \right)=0,                                                       \tag{6.11}
\]

where \(\mathcal H_\tau\) is the set of distinctly labelled clean marked
Hamilton paths whose port current obeys \(0\le\eta_T(P)\le d_T^\tau\),
\(L(P)\) is its owner-label set, and \(\eta(P)\) its port current; a
minimum over an empty \(\mathcal H_\tau\) is infinity.
Pair-specific guards and one-cycle connectivity still require the literal
pair columns and quotient cuts of Section 4.

More explicitly, let \(\mathcal B(\tau,P)\) be the integral
occurrence-labelled pair-column completions satisfying the owner and
halfport equations after \((\tau,P)\), and let
\(\Pi(\tau,P)\) be the contracted fixed-component partition.  With the
maximum of an empty family defined as minus infinity, the exact connected
completion criterion is

\[
 \max_{\tau\in\Omega}\ 
 \max_{P\in\mathcal H_\tau}\ 
 \max_{z\in\mathcal B(\tau,P)}
 \min_{\varnothing\ne W\subsetneq\Pi(\tau,P)}
 \sum_{(u,a):,a\text{ crosses }W}z_{u,a}\ge2.                 \tag{6.12}
\]

The inner cut sum is even under the degree equations, so two is exactly the
positive-cut threshold.  Formula (6.12) is the requested occurrence/path/
flow min--max.  Its quantifiers are existential, but the column family and
component partition are functions of \(\tau\); replacing them by one
unconditioned flow before choosing \(\tau\) is invalid.

## 7. Common-cap and provider scope

Fixing a physical cap (Q) gives a rigorous sufficient specialization:
delete every marked-gap or residual pair column which is not literally
realized by (Q), and solve (3.1) and (4.2) in the remaining graph.  If the
component interiors are also (Q)-realized, the resulting completion uses
one common cap by construction.  This is the correct Cartesian/guarded
route from marginal Hall to compatible Hall.

If (Q) is not fixed, cap choice and connector choice must be solved
together.  Bounded span or separate provider counts do not make this
automatic.  The lossless recursive state must retain at least

\[
 \bigl(\text{run boundary signatures},\ H,\ \mathcal A_u,\
        \Pi(F),\ \mu^{\rm int}_{\rm upper},\
        \text{literal cap/provider relation}\bigr).               \tag{7.1}
\]

Here \(\mu^{\rm int}_{\rm upper}\) is the full internal upper-target load
vector.  Retaining only the deleted globally-unique providers is not
lossless: all occurrences of a nonunique upper target can also be deleted.
Deeper shadows and the final common-cap compiler remain terminal conditions
even after the owner/lower component master closes.

## 8. Precise remaining theorem

Choose an occurrence state beyond the closed radius-one family, or add a
literal multi-owner/Steiner socket catalogue, preserving the balanced
edge/component and lower-colour ledgers.  The smallest occurrence search is
radius two from the twelve three-component frontier states.  Then construct
one solution of (4.2)--(4.4) such that:

1. its marked internal columns contain all 108 required clean macros but no
   strict internal D2/D3 violation;
2. every marked and residual join passes the literal D2/D3 run transducer;
3. all columns preserve the occurrence-labelled lower palette;
4. the complementary physical phase itself has no internal D2/D3 violation;
5. one of the two bank-crossing incidences is a legal linear opening; and
6. all columns lie in one nonempty common-cap fibre.

By Theorems 2.1, 4.1 and (6.5)--(6.12), this is necessary and sufficient
inside the stated augmented nonflat architecture.  Radius one is now
solver-free closed: all 122 nonisolating states remain disconnected and
have at least 21 forced leaves.  A fixed such state needs at least ten new
socket adjacencies by (6.7), whereas an occurrence move may change the
connector graph globally.  Only after a radius-two occurrence state or a
multi-owner C6/C10/Steiner packet passes the path rows do conditioned Hall,
quotient connectivity, complementary residence, deeper service and the
common cap become live.  The problem is neither a scalar phase debt nor an
ordinary marginal Hall check.

## 9. Frozen finite dependencies

The corrected whole-component obstruction is independently replayed by

```text
MATH_THEOREM_K17_MARKED_MACRO_COMPONENT_TWO_BANK_OBSTRUCTION_20260731.md
SHA-256 65819b0a7ef73a48729d14b7e20e944072cf7fc8ca1c732c21cd7361f5a9886a

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.audit.json
SHA-256 c4a7e2477186247bdbdace01967426a1cf55db8bcacc99296b679c681451e259

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.independent.json
SHA-256 b668fbc5e75a9ccd25c3571a9c4938f2a6167b0e66ca18d8c35c096afe90bdec
```

The detached 108-block phase path remains a valid, weaker positive input:

```text
MATH_THEOREM_K17_SINGLE_OWNER_PHASE_PATH_20260731.md
SHA-256 fa447d416822281d9893be6283bf8d357b80b4c2c4959880a34ea64418f89ac8

scratch/k17_nonflat_phase_path_20260731.json
SHA-256 68f203728da4c476262ad07eaac8ed0be65f8435ac598bce29e7ad275031f853
```

The repaired fixed-endpoint obstruction is replayed by

```text
scratch/k17_sixswap_repaired_macro_forest_20260731.flow.json
SHA-256 004c782c5b7af630f3d30b704eed4a90c2431db7895cd7217d463216b7f9a283

scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
SHA-256 14b90b013dab73649b9b65097f14def799c2c4bbdb6fe8c0f60d362d8f7bf262

scratch/k17_sixswap_repaired_component_flow_gate_20260731.audit.json
SHA-256 90fbffaf6fc35c159ce81b4730f1d37b503bec49617bdda77cd2f435d92f14d6
payload 8fb977c1bb10ad904f4dcd2a904d92c7c3d5f2f9243d62822898bb13ec024a73
```

An independent materialization additionally records the raw complementary
bank's 82 dirty components and 320 internal D2 defects:

```text
scratch/materialize_r_k17_sixswap_macro_flow_20260731.py
SHA-256 a05bbee22b61c78452156855ff978a70bc7f7b5dc0e4acf07a31e54ebd2d7d53

scratch/r_k17_sixswap_macro_flow_20260731.json
SHA-256 305dc5197a2b17481b018f04ac86bdda5acea409d244ab2dbc332fede8045df0
payload 84116113b9d970df6effc05cbf5bd19a97f9216bbec8cdf3c94c68b8c38823e8
```

The exact radius-one occurrence theorem is recorded by

```text
scratch/census_k17_two_bank_single_occurrence_swaps_20260731.py
SHA-256 0b2fa2802fb5562d453b8122864cbe0fe0c2c91aadd24d1b00afa3ccf0ce812d

scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 e9797343a3d6e841195b01b3541814562f8af8c6645f0d8e4795e2f0a9fa1d83

scratch/k17_sevenswap_premaster_macro_forest_20260731.flow.json
SHA-256 56f6701224913c1b3c09cedd1483595ef627d1bc946a87af43a8e73098dda0dc
payload 153644883597d6bd2f37f9f6271f7423f4db5302c304a83801bf66116566c5d7
```
