# Guarded endpoint ladders and alternating splices for the K17 PBBS factor

Date: 2026-07-31  
Lane: R, K17 PBBS theory  
Status: unconditional deterministic reduction, component-neutral Catalan
ledger, and frozen-factor lower bound; the final guarded braid is not yet
proved to exist

## 0. Verdict

There are two different path objects in the K15-to-K17 four-sector lift,
and their edge counts must not be mixed.

* The **PBBS U shore** is the no-new-coordinate copy of
  \(\binom{[15]}9\).  It has 5005 states, so its desired path has exactly
  5004 Johnson edges and 5004 distinct rank-eight intersections.  This is
  the object named in the question.
* The eventual **full K17 middle path** has all
  \(\binom{17}9=24310\) owners and therefore 24309 edges.  The other three
  four-sector ledgers must extend the U-shore path without lower-colour
  collision.

The authenticated PBBS U construction has already reached a particularly
clean deterministic starting point:

```text
scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments
SHA-256 3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465
```

It is a partition of all 5005 U states into 736 literal Johnson path
components.  Its 4269 internal edges have distinct rank-eight intersections,
its internal interval bank covers **every** upper mask of ranks 10 through
15, and it has no internal positive coordinate run of length one or two.
These statements have an independent literal replay in
`scratch/k17_pbbs_u_singleton_absorbed_independent_20260731.audit.json`
(SHA-256
`8b29fb3fea8a782d543f1054720328bc92f158e7535d487eab90ac04370be88d`).

If one insists on a standalone U-shore path, its remaining problem is

\[
 \boxed{\text{join 736 protected components by 735 actual endpoint seams}.}
                                                               \tag{0.0}
\]

That standalone path is now known to have colour-simple and full-DFA
degree covers; one replay consists of a main path on 551 components and
cycles of sizes `91,43,22,9,8,8,4`.  Thus its first authenticated remaining
gate is connectivity followed by the exact full staircase, not static
pair-local endpoint matching.

An independently replayed five-seam alternating closure then reduces this
to one path plus six cycles while preserving all 735 seam colours and the
full DFA.  It proves genuine fusion mobility, but not a Hamilton path.

More importantly, a standalone U path is **not necessary** for the full
four-sector K17 carrier.  For general `r`, put

\[
 W_r=\binom{2r-1}{r},\quad N_r=\binom{2r-1}{r+1},\quad
 J_r=W_r-N_r=\operatorname{Cat}_r.                    \tag{0.0a}
\]

If the U deck has `c` path components and the A/X/Y decks form `J_r`
native Catalan macros, then their `J_r+c-1` external seams are forced to
have untagged lower colour and

\[
             (N_r-c)+(J_r+c-1)=W_r-1.                 \tag{0.0b}
\]

In the strict distributed-insertion normal form this becomes

\[
 (N_r-c)+2c+(J_r-1-c)=W_r-1.                          \tag{0.0c}
\]

At K17 and `c=737`, this is

\[
                    4268+1474+692=6434.               \tag{0.0d}
\]

Thus macro subdivision has exactly zero lower-q1 component tax and leaves
exactly one untagged colour unused.  It creates endpoint mobility, not
palette slack.  This identity and its endpoint classification are proved in
Section U8 and separately in
`MATH_LEMMA_K17_COMPONENT_NEUTRAL_U_INSERTION_LEDGER_20260731.md`.

The current partial Y-U-X certificate supplies 737 locally
`010/0110`-safe bridges with pairwise-distinct colours.  It deliberately
uses no A vertices and constructs one extra direct Y-X pair.  In the strict
internal-insertion normal form with the unique hole untagged, a final open
carrier omits one such pair; a more general carrier may retain all untagged
edges and leave a tagged hole.  Either route must still solve the global
A/X/Y order, upper collars, and full state product.  Consequently global U Hamiltonicity
has ceased to be the strategic obstruction.

A subsequent coupled attachment already gives an exact all-lower-rainbow
2-factor on all 24310 owners, but it has 989 components, 9103 upper holes,
and extensive length-two/three run debt.  Thus even full lower-factor
existence is not the missing theorem; the obstruction is the common
upper/resident connected rethread and compiler.

This note proves the exact colored-port/Hall theorem for (0.0), the exact
run-summary composition law needed by alternating switches, and a guarded
alternating-cycle fusion theorem.  It also classifies the exact endpoint
run-state types.  If, for a named catalogue, deleting `010/0110`-creating
seams destroys a previously feasible endpoint matching, the obstruction is
an ordinary guarded Hall/Tutte cut and Theorems U7.1--U7.2 give sufficient
reroot-bridge repairs.  This is a model-specific conclusion: it is false for
the static pair graph of both frozen banks above, so an UNSAT claim must name
the stronger colour/DFA/global model and its artifact.  Scalar colour count
is never the explanation; the residual untagged palette has invariant slack
exactly one.

There are also two unrelated occurrences of the number 17 in the local
literature.  The live U-shore lane starts from **17 K15 rank-eight PBBS
cycles** in `k15_dual_descent_a4_step19`.  The AD natural four-sector child
below starts from a different two-cycle K15 parent and happens to have **17
components on all 24310 K17 owners**.  The U-shore 5004 theorem concerns the
first lineage; the 1740-edge lower bound concerns only the second.

For completeness, let

\[
 {\cal V}=\binom{[17]}9,\qquad N=|{\cal V}|=24310,
\]

and let `F` be the authenticated 17-component four-sector factor from

```text
scratch/ad_k17_k15_four_sector_factor_20260731.json
```

(`SHA-256 542a40b2ba905a939e157bdb973b59d873cf22b9b7c3eb86bc15d11ff078a7f3`).
Every edge of `F` is Johnson and the map

\[
                 AB\longmapsto A\cap B                 \tag{0.1}
\]

is a bijection from `E(F)` to \(\binom{[17]}8\).  The factor nevertheless
misses 1739 adjacent rank-ten unions and 4045 arbitrary-width upper masks.

The full-factor audit additionally proves four things.

1. **Exact scale correction.**  A spanning path on \({\cal V}\) has 24309
   edges.  If it retains factor edges and replaces a set `D` of them by a
   set `S` of new seams, then

   \[
                    |D|=|S|+1.                         \tag{0.2}
   \]

   Distinct rank-eight intersections are preserved exactly when the new
   seam colours are distinct members of the deleted-colour set.  Exactly
   one deleted colour is then omitted.

2. **A new frozen-factor lower bound.**  Every path rethread of the displayed
   factor which covers every adjacent rank-ten union has

   \[
                    |S|\ge1739,\qquad |D|\ge1740.      \tag{0.3}
   \]

   This applies to an arbitrary symmetric-difference rethread, not merely a
   block reversal.  It strictly supersedes the old 61-edge unique-provider
   bound and the 49-cut staircase bound for this one frozen factor.

3. **A deterministic guarded-Hall theorem.**  After the cuts and fragment
   orientations are fixed, assign to every nonterminal fragment:

   * one distinct deleted lower colour to return; and
   * one bundle of upper targets to reproduce in its new endpoint ladder.

   Keep a directed fragment seam only when it passes, simultaneously, the
   literal Johnson test, the assigned lower-colour identity, the complete
   assigned suffix--prefix OR test, and a short-run boundary test.  Ordinary
   Hall on this *intersected guarded graph* is necessary and sufficient for
   a degree-correct path cover.  It is not enough to check the four guards
   in separate marginal graphs.

4. **An alternating-splice theorem.**  Every alternating even cycle in the
   guarded matching graph preserves all source-assigned lower colours,
   upper ladders, and run guards.  A component-transversal alternating
   \(C_{2a}\) merges `a` current components into one.  Consequently a
   guarded matching together with a component-transversal alternating-cycle
   fusion sequence gives one literal rank-nine path.  In the special
   17-component case, eight guarded \(C_6\)'s arranged as a loose spanning
   3-tree suffice.

The resulting path has 24309 distinct rank-eight intersections, every
required upper interval union, and no interior positive coordinate run of
length at most three.  The latter makes the depth-three run staircase
automatic.

The theorem is constructive and integral, but conditional on finding its
guarded cut/bundle/matching data.  No such bank is proved here for the frozen
factor.  The exact remaining theorem is therefore not “there are many
Johnson endpoint pairs.”  It is the simultaneous guarded-Hall and
alternating-connectivity assertion in Section 8.

Thus `5004` is correct for a standalone PBBS U shore, while `24309` is the separate
full-middle count.  Sections U1--U8 below solve the deterministic U-shore
and component-neutral interfaces.  Sections 1--9 record the architecture-general/full-factor
ledger and the new 1740-edge no-go for trying to rethread the frozen natural
17-cycle factor directly.

## U1. Authenticated PBBS U-shore reduction

The source is the authenticated 17-cycle PBBS occurrence system built from

```text
scratch/k15_dual_descent_a4_step19.segments.json
SHA-256 d4e2dacd881c968f431925db178d44180cec5981c04862aa2e4a4a50d14dd504
```

Choosing one occurrence of each of the 5005 rank-nine union colours gives

```text
scratch/k17_pbbs_u.fragments
SHA-256 8db7db58a697171a7440fbd1c2333c782947737079530470b482a971948e9944
```

with 761 maximal selected-edge fragments.  The source occurrence histogram
is

\[
                         1^{3630}2^{1320}3^{55}.        \tag{U1.1}
\]

Every internal edge is Johnson, all internal rank-eight intersections are
distinct PBBS owner states, and there is no internal positive run of length
one or two.

Two audited local refinements, followed by one lossless nested ladder,
produce 765 fragments with only 28 rank-ten holes.  A displayed
fragment-disjoint matching chooses one literal seam for each of those holes,
using 56 different source fragments and 28 fresh intersection colours.
Contracting those seams gives the historical 737-component bank.  Direct
replay gives

\[
\begin{array}{c|c}
\text{U states}&5005\text{ distinct}\\
\text{components}&737\\
\text{internal edges}&5005-737=4268\\
\text{internal intersection colours}&4268\text{ distinct}\\
\text{unused rank-eight colours}&\binom{15}8-4268=2167\\
\text{upper masks witnessed, ranks }10,\ldots,15&4944/4944\\
\text{internal positive runs of length }1,2&0.
\end{array}                                                \tag{U1.2}
\]

The bank contains 183 singleton and 168 length-two components.  Hence a
pattern such as `010` or `0110` can span two or three final seams even when
every two-component concatenation passes a pairwise check.  This is why the
whole-path summary in Section U5 is mandatory.

The rank-ten repair certificate is integral.  It is not an assertion that
737 arbitrary blocks may now be concatenated.  A later lossless singleton
absorption gives the current bank

```text
scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments
SHA-256 3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465
```

with 736 components, 4269 distinct internal colours, 2166 unused
rank-eight colours, complete ranks 10 through 15, and no internal `010` or
`0110`.  It needs 735 joins as a standalone U path and still leaves the
same invariant 1431-colour excess from Proposition U1.1.

### Proposition U1.1 (fragment-count colour invariant)

Let any PBBS U atlas partition the 5005 U states into `f` Johnson fragments,
and suppose its `5005-f` internal intersection colours are distinct.  A
Hamilton path obtained only by joining whole fragments needs exactly `f-1`
new seams.  It has 5004 distinct intersections if and only if those seams
use `f-1` fresh pairwise-distinct rank-eight colours.  The scalar fresh bank
has size

\[
 \binom{15}8-(5005-f)=1430+f,                         \tag{U1.3}
\]

so every successful path leaves exactly

\[
                         (1430+f)-(f-1)=1431          \tag{U1.4}
\]

rank-eight colours unused.

#### Proof

A forest of `f` path components on 5005 vertices has `5005-f` edges.  A
spanning path has 5004 edges, hence needs `f-1` joins.  Since the internal
colours are already distinct, the complete deck is distinct precisely when
the new colours are fresh and mutually distinct.  Equations (U1.3)--(U1.4)
are subtraction.  QED.

For the current frozen bank, `f=736`: 2166 colours are available and 735
are needed.  The excess 1431 is invariant and proves that only correlated
port/colour/state placement, not scalar colour capacity, can obstruct the
standalone join.

### Proposition U1.2 (fixed 763-fragment zero-provider obstruction)

The alternative frozen atlas

```text
scratch/k17_pbbs_u_johnson_repaired.fragments
SHA-256 987fe296bef58dfcdb7b85657130fc2c3a8e5061580d5eeef7adcc816194c889
```

cannot be made upper-complete by any ordering or orientation of its 763
fixed fragments.  Its internal bank misses the rank-ten target `0x23df`,
and its occurrence-labelled endpoint catalogue contains zero seams with
union `0x23df`.

#### Proof

Any new witness not internal to one fixed fragment crosses a selected
fragment seam.  Every state in a witness for a rank-ten target is a rank-nine
facet of that target.  The first two distinct consecutive facets at a
crossed seam have union equal to the rank-ten target itself.  Therefore an
endpoint seam of union `0x23df` is necessary.  The frozen catalogue has none.
QED.

This no-go is atlas-specific.  The lossless nested ladder and 28-seam
contraction change the fragment endpoints and lead to the positive
upper-complete bank (U1.2).

### Proposition U1.3 (historical two-dead-port preconditioned bank)

The later lossless endpoint preconditioning

```text
scratch/k17_pbbs_u_deadport_absorbed_20260731.fragments
SHA-256 0bcd678828c8d258b6976aa2831a250dd3650c395bf9d3864df1415ee5961a6b
```

retains all numerical properties in (U1.2).  Its independently replayed
locally guarded endpoint graph has 7013 edges, is connected on all 737
macrocomponents, has minimum component degree two, and has exactly two dead
physical ports:

\[
             (599,\text{side }1,0x69ae),\qquad
             (734,\text{side }0,0x09fe).              \tag{U1.5}
\]

Here an endpoint edge was retained only when it was Johnson, used a colour
outside the internal palette, and its two three-cell collars introduced no
`010` or `0110`.

In any whole-macro Hamilton path drawn from this guarded graph, the two dead
ports in (U1.5) must be the two external path ports.  Nevertheless the
displayed graph data do not prove a Hamilton path.

#### Proof

An internal macrocomponent uses both physical ports.  A port of degree zero
cannot be joined, so its macro must be a global endpoint and the dead port
must face outward.  The two dead ports lie on different macros and exhaust
the two global endpoints.  Connectedness and minimum degree two are not a
Hamilton criterion.  For example, every graph with a Hamilton path must
satisfy the necessary deletion inequality

\[
                         c(G-S)\le |S|+1               \tag{U1.6}
\]

for every vertex set `S`, since deleting `S` from one path leaves at most
`|S|+1` path pieces.  The audit does not certify (U1.6), orientations,
pairwise seam-colour distinctness, or multi-seam run safety.  QED.

The historical bank does have an independently replayed oriented degree
cover with 736 locally pair-safe seams when colour uniqueness and global
DFA consistency are omitted.  Hence it has no static pair-local Hall
obstruction; (U1.6), colour simplicity, connectivity, and full state replay
remain separate.

### Proposition U1.4 (current 736-bank degree-cover status)

For the current `3b1a...` bank, exact replay supplies both a colour-simple
degree cover and a colour-simple full-DFA degree cover.  The latter has one
directed path on 551 components and seven directed cycles of sizes

\[
                         91,43,22,9,8,8,4.            \tag{U1.7}
\]

It uses 735 distinct seam colours and has no pair-safe failure.  This proves
degree feasibility, not connectivity or the full four-sector chronology.
An independent decoder/replayer is frozen at
`scratch/threadD_k17_pbbs_u_singleton_degree_replay_20260731/independent.audit.json`
(SHA-256
`2c5c5727386fa3b0044bc6085648922dfa0321544cf3cdad12850991dd6a73fb`).

The current bank, rather than (U1.5), is the preferred input to Theorems
U2--U8.

## U2. Exact colored two-port object

Let \({\cal Q}=\{Q_1,\ldots,Q_f\}\) be any protected U-fragment bank, with
the current 736-bank as the principal case.  Each nonsingleton has two physical
endpoint occurrences.  Fix temporarily:

1. one of the two orientations of each `Q_i`;
2. a start component `a` and terminal component `t`.

Write `l_i,r_i` for the resulting first and last rank-nine masks.  Let
`C_0` be the set of intersection colours already used internally and put

\[
                         C_{\rm fresh}=\binom{[15]}8\setminus C_0. \tag{U2.1}
\]

A directed port seam `i -> j` is **colour-legal** when

\[
 i\ne j,\qquad |r_i\triangle l_j|=2,\qquad
 c(i,j):=r_i\cap l_j\in C_{\rm fresh}.                \tag{U2.2}
\]

This is an occurrence-labelled test.  Reversing a component changes its
physical `l_i,r_i`; a set pair occurring at nonendpoint positions is not a
port.

### Theorem U2.1 (exact colored-port characterization)

For the fixed orientations and endpoints, a path through all `f` components
with 5004 distinct rank-eight intersections is equivalent to a set `M` of
`f-1` directed seams such that:

\[
\begin{aligned}
 &\deg_M^+(i)=1 &&(i\ne t),&\quad \deg_M^+(t)&=0,\\
 &\deg_M^-(j)=1 &&(j\ne a),&\quad \deg_M^-(a)&=0,       \tag{U2.3}\\
 &c(e)\ne c(e') &&& (e\ne e'),
\end{aligned}
\]

and the directed component graph has no cycle.

#### Proof

The degree and acyclicity conditions say exactly that the component graph is
one directed `a`--`t` Hamilton path.  Every selected edge passes (U2.2), so
the physical concatenation is Johnson.  Proposition U1.1 makes colour
distinctness equivalent to the last line of (U2.3).  Conversely every
desired concatenation supplies exactly these seams.  QED.

Thus the uncoloured endpoint bipartite graph is not the exact object.  Each
seam simultaneously consumes one exit, one entry, and one fresh colour.

### Corollary U2.2 (exact macro cut inequalities)

Under the port-degree and colour conditions in (U2.3), the selected seams
form one Hamilton component if and only if every nonempty proper fragment
set `A` has a selected crossing seam:

\[
        x(\delta^+(A))+x(\delta^-(A))\ge1
        \qquad(\varnothing\ne A\subsetneq[f]).        \tag{U2.4}
\]

#### Proof

The degree equations give one directed path plus directed cycles.  A cycle
component has no selected edge crossing its vertex set, violating (U2.4).
Conversely every disconnected component outside the distinguished path is
such a cycle and gives the same violation.  QED.

### Lemma U2.3 (rainbow paths have no singleton positive run)

Every Johnson path with pairwise-distinct intersection colours has no
interior positive coordinate run of length one.  Hence every desired PBBS U
path has \(\rho_1=0\).

#### Proof

If coordinate `x` occurs only in the interior state `V_i`, then both
neighbours omit `x`.  Johnson adjacency forces

\[
       V_{i-1}\cap V_i=V_i\setminus\{x\}
          =V_i\cap V_{i+1},                           \tag{U2.5}
\]

repeating one rank-eight intersection colour.  QED.

## U3. Ordinary Hall after a source-colour assignment

There is a fully elementary way to turn the three-resource object into an
ordinary Hall problem.  Choose an injection

\[
          \gamma:[f]\setminus\{t\}\longrightarrow C_{\rm fresh}. \tag{U3.1}
\]

Retain the directed port edge `i -> j` only when it is colour-legal and

\[
                              c(i,j)=\gamma(i).         \tag{U3.2}
\]

One may intersect this graph with any additional endpoint guard, including
a protected upper ladder condition or a run-transition condition.  Call the
result \(G_\gamma\), with shores

\[
       L=[f]\setminus\{t\},\qquad R=[f]\setminus\{a\}. \tag{U3.3}
\]

### Theorem U3.1 (source-coloured endpoint Hall)

The graph \(G_\gamma\) has a degree-correct path cover if and only if

\[
                      |N_{G_\gamma}(X)|\ge|X|
                      \quad(X\subseteq L).             \tag{U3.4}
\]

Every matching given by (U3.4) already uses fresh pairwise-distinct lower
colours.  Its directed component graph is one `a`--`t` path plus cycles.

#### Proof

This is Hall's theorem on the equal shores (U3.3).  Source colours are
distinct by (U3.1), and (U3.2) forces every selected physical seam to return
its source colour.  The degree description gives one path plus cycles.
QED.

Condition (U3.4) is an exact Hall theorem for a *chosen* colour injection,
not a claim that a suitable \(\gamma\) exists.  Separate Hall checks on
endpoints and colours are invalid.  On two sources and two entries, the
endpoint graph can support only the diagonal matching while a proposed
colour assignment supports only the off-diagonal one; both marginals
saturate and their common graph is empty.

Without preassigning \(\gamma\), the exact degree problem is a rainbow
matching problem.  For each source `i`, make a graph \({\cal H}_i\) on the
vertex set `R dot-union C_fresh`, with edge `{j,c(i,j)}` for every guarded
seam `i -> j`.  A rainbow choice of one disjoint edge from each
\({\cal H}_i\) is exactly a degree-correct colour-simple cover.  The standard
Aharoni--Haxell rainbow-matching condition

\[
 \nu\!\left(\bigcup_{i\in X}{\cal H}_i\right)>2(|X|-1)
 \qquad(\varnothing\ne X\subseteq L)                  \tag{U3.5}
\]

is a rigorous sufficient condition.  We do not need (U3.5) for the proved
ordinary-Hall theorem, and do not assert it for the PBBS bank.

There is a second elementary Hall form which does not preassign the colours.
Let `D` be a directed subgraph of the actual colour-legal port graph for the
fixed orientations.  Say that `D` is:

* **order-acyclic** when its directed component graph has no directed cycle;
* **colour-proper for matchings** when, for every fresh colour `c`, the
  bipartite graph formed by the arcs of colour `c` has matching number at
  most one.

The second condition is equivalent to saying that every nonempty colour
class is a star (with a common exit or a common entry).  It implies that no
matching can select a repeated colour.

### Theorem U3.2 (acyclic colour-proper Hall theorem)

Fix orientations and endpoints `a,t`.  If `D` is order-acyclic and
colour-proper for matchings, then `D` contains a colour-simple Hamilton path
from `a` to `t` if and only if

\[
                         |N_D(X)|\ge |X|
       \qquad(X\subseteq [f]\setminus\{t\}),          \tag{U3.6}
\]

where neighbours lie in \([f]\setminus\{a\}\).

#### Proof

Necessity is ordinary Hall.  Conversely Hall supplies a matching saturating
the two equal shores.  Its directed component graph has the prescribed
indegrees and outdegrees, hence consists of one `a`--`t` path and directed
cycles.  Every selected arc lies in the acyclic digraph `D`, so no directed
cycle exists; the cover is the one spanning path.  If two selected seams
had the same colour, they would be two disjoint edges in that colour class,
contradicting matching number at most one.  QED.

This is the cleanest genuinely Hall-type sufficient theorem for the final
736-macro standalone join.  The nontrivial construction task is to prune the physical
port graph to such a `D` without destroying (U3.6) or the staircase.

## U4. Upper ladders become monotone after service contraction

For both the historical 737-bank and current 736-bank, every upper target already has a witness wholly
inside one component.  Reorienting a component reverses its witness but does
not change its union.  Joining components adds cross-component intervals
and deletes no internal interval.  Therefore:

### Theorem U4.1 (internal upper-bank protection)

Every ordering and orientation of the current 736 components which uses actual
endpoint seams preserves all upper masks of ranks 10 through 15.

#### Proof

Every certified witness lies in one component and hence remains a contiguous
interval after the components are concatenated.  OR is invariant under
reversal.  QED.

This theorem is stronger than a seam-capacity estimate: the final 735 standalone seams
have **no upper service obligation at all**.  The endpoint ladder packing
was needed in the preceding 28-seam contraction and is already supplied by
the explicit fragment-disjoint certificate.  For another atlas without an
internal complete bank, the guarded bundle condition in Sections 3 and 5
below is the correct replacement.

For completeness, the preceding upper-service contraction has its own exact
packing theorem.  Let `T` be a set of upper debts, and for each `U in T` let
\({\cal H}_U\) be the 3-uniform hypergraph of candidate service seams, where
one hyperedge records its two occurrence-labelled fragment ports and its
fresh lower colour.  A rainbow family of pairwise disjoint hyperedges, one
from every \({\cal H}_U\), gives upper-service seams without port or
lower-colour collision.  To contract them into protected *path*
macrocomponents, the selected seam graph on source fragments must also be a
forest; port disjointness alone can leave a closed fragment cycle.

### Proposition U4.2 (service-seam packing criteria)

Either of the following conditions is sufficient for such a service bank.

1. For every nonempty `S subseteq T`,

   \[
       \nu\!\left(\bigcup_{U\in S}{\cal H}_U\right)
                      >3(|S|-1).                      \tag{U4.1}
   \]

2. Put

   \[
      D=\max_{U\in T,\,r}
          |\{e\in{\cal H}_U:r\in e\}|.               \tag{U4.2}
   \]

   If \(|{\cal H}_U|>3D(|T|-1)\) for every `U`, then a greedy service
   bank exists.

#### Proof

Condition (1) is the 3-uniform Aharoni--Haxell rainbow-matching theorem.
For (2), after at most `|T|-1` choices, at most `3(|T|-1)` resources are
occupied.  Each resource blocks at most `D` candidates for the next target,
so fewer than `3D(|T|-1)` of its candidates are blocked.  A disjoint one
remains.  QED.

The displayed 28-seam PBBS certificate supplies the stronger conclusion
directly: it uses 56 distinct source fragments, so its fragment graph is a
matching and hence a forest.  No claim that its raw catalogue satisfies
either stronger sufficient inequality is needed.

## U5. Exact short-run summary monoid

Connectivity and colour simplicity are not enough.  The final order must
pass the depth-three monotone-deadline staircase.

For a finite rank-nine word `Q` and coordinate `x`, record:

1. whether every state of `Q` contains `x`;
2. the lengths of its initial and terminal positive `x`-runs, capped at 4;
3. for `j=1,2,3`, the latest local start of an **interior** positive
   `x`-run of length at most `j`, with value 0 when none exists.

Together with `|Q|`, call the resulting finite record \(\Sigma_3(Q)\).

### Theorem U5.1 (exact concatenation law)

There is a deterministic associative product `star` on these records such
that

\[
                         \Sigma_3(QR)=\Sigma_3(Q)\star\Sigma_3(R). \tag{U5.1}
\]

In particular, \(\Sigma_3\) of a component concatenation is determined by
the component order, orientations, and no other information.

#### Proof

Internal runs of `Q` remain at their old starts.  Internal runs of `R` have
their starts shifted by `|Q|`.  The only other possible run is formed from
the terminal run of `Q` and the initial run of `R`:

* if both endpoint bits are one, concatenate the two runs;
* if exactly one is one, that boundary run closes or opens at the seam;
* if both are zero, no positive run crosses the seam.

The all-one flags decide whether the resulting run touches the global left
or right boundary and hence whether it is interior.  Its length, when at
most three, is known exactly from the capped prefix/suffix lengths; values
at least four are all equivalent for a depth-three frontier.  Taking the
maximum of the old, shifted, and new boundary-run starts gives the three new
frontiers.  The new prefix/suffix lengths and all-one flag follow from the
same four cases.  This constructs the product.  Associativity follows
because both parenthesizations equal the literal run record of `QRS`.  QED.

For a complete **full K17 carrier** `P`, taking the maximum over coordinates
in its record gives exactly the canonical frontiers
\(\rho_1(P),\rho_2(P),\rho_3(P)\).  The canonical K17 staircase condition is

\[
                    \rho_1(P)+\rho_2(P)+\rho_3(P)\le7401. \tag{U5.2}
\]

By Lemma U2.3, lower-rainbow simplicity already forces \(\rho_1=0\).
The bank (U1.2) has no internal run of length two.  If the selected seams
also create none, then its U-block contribution has \(\rho_2=0\), and the
remaining local condition concerns length-three starts.

If the U path is embedded as one contiguous block beginning at global
position `b`, every internal length-three start in it is at most
\(b+5002\).  Hence the simple placement condition

\[
                              b\le2399                    \tag{U5.3}
\]

puts all of its internal length-three starts by position 7401.  The two
external sector seams and every other sector still contribute their own run
frontiers and must be composed with \(\Sigma_3\).  Thus a U-shore path alone
exports an exact staircase summary; it does not, by itself, certify the full
four-sector chronology.

This is the correct weakening of a minimum-run-four demand.  The scoped
`0x31ef` obstruction for `scratch/k17_pbbs_u_repaired.fragments` proves that
one forced seam creates a length-two run.  It refutes the stronger
minimum-run-three requirement for that fixed atlas, but it does **not**
refute (U5.2): a forced short run can be harmless if placed sufficiently
early.

For arbitrary omitted starts, compose \(\Sigma_3\) with the complete
24310-state chronology, compute its adjusted frontiers \(\rho^\alpha\), and
apply the exact global condition

\[
 \min_{0\le\alpha_1\le\alpha_2\le\alpha_3\le24310}
       \operatorname{Loss}(\alpha,\rho^\alpha)\le7401,
 \qquad \rho^\alpha\le\alpha,                         \tag{U5.4}
\]

together with chain alignment when upper transfer through the compiler is
required.  Envelope nonemptiness and the later lower Hall/common-cap
compiler remain separate.

### Corollary U5.2 (finite short-chain audit)

When every macrocomponent internally avoids `010` and `0110`, a proposed
macro path avoids them globally if and only if every selected one-seam and
two-seam chain avoids them, together with the possible three-seam `0110`
chains whose relevant middle pieces are singletons.

#### Proof

The forbidden words have cell lengths three and four.  A length-three word
crosses at most two component seams.  A length-four word crosses at most
three, and crossing all three forces its two internal component pieces to
be singletons.  Every other occurrence is internal to a macro or belongs to
one of the listed chains.  QED.

### Corollary U5.3 (switch-safe chronology certificate)

An alternating component splice is staircase-safe precisely when the
`star`-product of its newly ordered macrocomponents, together with their
absolute prefix length, respects (U5.2).  Carrying \(\Sigma_3\) on every
contracted macrocomponent makes this check deterministic at every fusion
step.

Unlike Johnson, colour, and internal-upper guards, staircase safety is not
automatically source-local: an alternating switch changes absolute run
positions.  Every positive switch claim must therefore carry either its
exact \(\Sigma_3\) product or the stronger fail-closed condition that it
creates no interior run of length at most three.

## U6. Alternating-cycle fusion theorem for a protected U bank

Let `M` be a colour-simple degree-correct matching obtained from Theorem
U3.1 (or from an exact rainbow matching).  It gives one directed path and
some directed cycles on the protected components.  For matched arcs

\[
                         i_h\to j_h\quad(0\le h<a),     \tag{U6.1}
\]

suppose all cyclic cross arcs

\[
                         i_h\to j_{h+1}\quad(h\bmod a) \tag{U6.2}
\]

are actual Johnson port seams and preserve the source-colour assignment.
Then (U6.1)--(U6.2) is an alternating \(C_{2a}\) in the source-coloured
endpoint graph.

### Theorem U6.1 (colored PBBS component splice)

If the arcs (U6.1) lie in `a` distinct current directed components, toggling
to (U6.2):

1. preserves all endpoint degrees and all 5004 lower-colour distinctness;
2. preserves every upper interval target in the internal protected bank;
3. merges the `a` components into one; and
4. preserves the K17 staircase exactly when the new global order passes the
   summary test (U5.2).

#### Proof

The alternating cycle uses every displayed source and head once.  The
source-colour rule returns the same distinct fresh colour at each source.
Theorem U4.1 protects upper witnesses.  Cutting the old arcs turns the
touched components into directed paths, and the cyclic cross-connection
concatenates them into one component; when one is the distinguished path,
the result is again a path with the same global endpoints.  The final clause
is Theorem U5.1.  QED.

There is an explicit globally palette-neutral six-cycle which calibrates
the unassigned rainbow formulation.  Let `K` be a 7-set and let
\(a_0,a_1,a_2,c\) be distinct and outside `K`, with indices modulo three.
Put

\[
\begin{aligned}
 R_i&=K\cup\{a_i\},\\
 U_i&=K\cup\{a_i,a_{i+1},c\},\\
 P_i&=K\cup\{a_i,a_{i+1}\},\\
 Q_i&=K\cup\{a_i,c\}.
\end{aligned}                                          \tag{U6.8}
\]

### Lemma U6.1A (explicit lower/upper-neutral C6)

The switch

\[
                    \{P_iQ_i:i\in\mathbb Z_3\}
       \longleftrightarrow
                    \{P_iQ_{i+1}:i\in\mathbb Z_3\}   \tag{U6.9}
\]

preserves the multisets of lower rank-eight colours and upper rank-ten
colours, and preserves every displayed owner degree.  If its three old
edges lie in three distinct current cycles in the component-transversal
orientation, it merges those cycles into one.

#### Proof

For the old edges,

\[
 P_i\cap Q_i=R_i,\qquad P_i\cup Q_i=U_i.              \tag{U6.10}
\]

For the new edges,

\[
 P_i\cap Q_{i+1}=R_{i+1},\qquad
 P_i\cup Q_{i+1}=U_i.                                \tag{U6.11}
\]

Thus both colour multisets are merely permuted.  Each `P_i` and `Q_i` loses
and gains one edge.  The component conclusion is the three-path
cut-and-cyclic-reconnect trace from Theorem U6.1.  QED.

The source `P_i` changes lower colour from `R_i` to `R_{i+1}`.  Hence
(U6.9) is **not** a switch inside a fixed source-colour graph `G_gamma`
from Theorem U3.1/U6.1.  It is legal only in the unassigned
rainbow-matching space, or after a simultaneous reassignment of the source
colours.

Eight component-transversal copies could merge 17 cycles to one before a
final opening.  This is only a topology statement.  A PBBS realization of
the required eight copies is unproved, and (U6.9) alone does not preserve
arbitrary-width interval witnesses or the run staircase; those must pass
Theorems U4.1 and U5.1 on the common physical order.

For the current `3b1a...` bank, a separate exact audit finds no rooted
closure of supports two, three, or four through the displayed four-cycle,
but finds one support-five toggle which is simultaneously rainbow and
full-DFA safe.  It changes the degree cover from path551 plus seven cycles
to path279 plus cycles of sizes

\[
                         367,43,22,9,8,8.              \tag{U6.12}
\]

This is an authenticated instance of the unassigned guarded-switch
principle, not an existence theorem for a complete fusion bank.  Its audit
is `scratch/k17_pbbs_u_singleton_absorption_c6_girth5_20260731.audit.json`
(SHA-256
`0470ff016bbadf7a44d3a692a13f690c080bcf48f5616bdf7bc235ca8f6f6319`).

### Lemma U6.1B (whole-macro two-opt)

In a current U-macro path, reverse one contiguous block of whole
macrocomponents and replace its two boundary seams.  The move preserves all
component-internal edges, their lower colours, and every internally
protected upper witness.  It is a valid lower-rainbow Johnson move if and
only if its two new boundary pairs are Johnson and their intersection
colours are distinct and absent from the retained palette; they may reuse
the two colours of the deleted boundary seams.

Its `010/0110` status and exact staircase are preserved if and only if the
new one/two/three-seam chains pass Corollary U5.2 and the final summary
passes Theorem U5.1.

#### Proof

Reversal preserves every undirected internal adjacency and every internal
interval union.  It also reverses the coordinate words; `010` and `0110`
are palindromes.  Only the two old boundary edges are deleted and only the
two displayed new ones are inserted, giving the stated Johnson and colour
criterion.  Every newly possible short factor meets a changed boundary, so
Corollary U5.2 is exhaustive.  The exact frontier claim is the summary
identity (U5.1).  QED.

### Corollary U6.2 (deterministic PBBS U-path theorem)

The authenticated 736-component bank yields the required 5005-state U path
provided there exist:

1. orientations and global endpoints;
2. either a source-colour injection satisfying Hall (U3.4), or an exact
   colour-simple degree cover;
3. a sequence of component-transversal alternating cycles reducing its
   path-plus-cycles cover to one path; and
4. a final U-block summary which, after composition with the other three
   sector summaries and both external seams, satisfies (U5.2) or (U5.4).

The output then has literal Johnson seams, 5004 distinct rank-eight
intersections, every U-shore upper interval union, and an exact exported
short-run summary for the full staircase.

All four clauses refer to one physical component order.  Within the
standalone U-path subproblem, its open content is the existence of the
coloured connected chronology; upper coverage and scalar colour supply are
already certified.  The full K17 compiler and the distributed alternative
of Section U8 remain separate.

### Theorem U6.3 (prefix-ideal Hall plus staircase)

There is a checkable strengthening which makes the Hall theorem itself
control the U contribution to the staircase.  Fix orientations and endpoints `a,t`, and
let `D` be an order-acyclic, colour-proper directed port bank as in Theorem
U3.2.  Suppose there are nested component sets

\[
                B_2\subseteq B_3,
                \qquad a\in B_2,                      \tag{U6.3}
\]

such that:

1. each `B_j`, `j=2,3`, is an initial ideal of `D`:

   \[
                   E_D(V\setminus B_j,B_j)=\varnothing; \tag{U6.4}
   \]

2. fix the literal left and right exterior sentinel words which meet the U
   block.  The exact depth-three trace automaton certifies that, in the
   composition `left sentinel | U path | right sentinel` for every directed
   component path allowed by `D`, every interior positive run of length at
   most `j` whose start lies in the U block starts in a component of `B_j`,
   for `j=2,3`; runs which start in the exterior are included in the
   certified exterior frontier.  Equivalently, both external seams may be
   required to satisfy the stronger fail-closed boundary guard; and
3. with `n_i=|Q_i|` and

   \[
                          L_j=\sum_{i\in B_j}n_i,       \tag{U6.5}
   \]

   if the U block starts at global position `b` and the already certified
   exterior frontier is `(0,eta_2,eta_3)`, one has

   \[
      \max\{\eta_2,b+L_2-1\}
       +\max\{\eta_3,b+L_3-1\}\le7401.               \tag{U6.6}
   \]

If the Hall inequalities (U3.6) hold, then `D` contains a literal U-shore
Hamilton path satisfying Johnson legality, 5004 distinct rank-eight
intersections, and complete U-shore upper interval coverage.  After the
stated exterior composition, the full chronology satisfies the canonical
K17 staircase.

#### Proof

Theorem U3.2 supplies a colour-simple Hamilton path.  Once this path leaves
`B_j`, (U6.4) forbids its return.  Since it starts in `B_2` and must visit
every vertex, it must exhaust each nested `B_j` before leaving it.  Thus
`B_j` occupies the first exactly `L_j` physical states of the concatenated
word.

By Lemma U2.3, \(\rho_1=0\).  By (2), including the right external seam,
every final interior run of length at most `j` which starts in the U block
starts among those states, so its global start is bounded by

\[
                         b+L_j-1\qquad(j=2,3).         \tag{U6.7}
\]

Runs starting outside U are bounded by the literal exterior certificate.
Taking the maximum with those exterior frontiers and applying (U6.6) gives
the staircase condition (U5.2).  The
Johnson and colour conclusions are Theorem U3.2 and Proposition U1.1; the
upper conclusion is Theorem U4.1.  QED.

Condition (2) is not a pairwise-seam heuristic, and the right sentinel
cannot be replaced by a scalar pre-existing frontier: a terminal U run can
become interior only after the following sector is attached.  For depth
three it is a
finite regular-language check: forbidden newly late starts have one of the
forms `010`, `0110`, or `01110`, each of length at most five, and may cross
several singleton macrocomponents.  The summary product in Theorem U5.1 (or
the equivalent five-cell automaton on the DAG) checks it fail-closed.

For a U block placed first with no exterior short-run debt, the coarser
budget \(L_2+L_3\le7401\) implies (U6.6).
The exact fixed-atlas `0x31ef` seam merely forces one length-two event; this
theorem says it must be routed inside `B_2`.  It is not a staircase
obstruction unless the resulting nested-prefix cost violates (U6.6).

## U7. Endpoint run-state matching and reroot bridge conditions

This section formalizes the reported structural phenomenon: a pure Johnson
endpoint matching can exist while a more strongly guarded matching fails
after boundary-state constraints are imposed.  For any *named* static
pair-filtered graph, such a failure is exactly a Hall/Tutte obstruction and
the reroot criteria below are rigorous sufficient repairs.

It is not, however, the current frozen-bank verdict.  On `0bcd...`, an exact
replay selects 736 Johnson seams satisfying the literal pair-local
`010/0110` predicate when colours, global DFA consistency, and subtour cuts
are omitted.  On the later `3b1a...` bank, even colour-simple and full-DFA
degree covers are replayed.  Therefore any cited UNSAT must identify a
different atlas or an additional colour/global-state/connectivity model;
it may not be described as failure of the static graph in (U7.5) or
(U7.6).  The distinction is essential because patterns can span several
seams.

### U7.1 Exact endpoint state types

For one coordinate, avoidance of `010` and `0110` has the four live states

\[
              {\mathsf S}=\{\epsilon,0,01,011\},       \tag{U7.1}
\]

meaning the longest current suffix which is a prefix of a forbidden word.
The transition table is

\[
\begin{array}{c|cc}
 &0&1\\\hline
\epsilon&0&\epsilon\\
0&0&01\\
01&\bot&011\\
011&\bot&\epsilon.
\end{array}                                            \tag{U7.2}
\]

For an oriented macro `Q` and coordinate `x`, composition along its
membership word gives a partial map

\[
                   \Theta_{Q,x}:{\mathsf S}\longrightarrow
                         {\mathsf S}\cup\{\bot\}.      \tag{U7.3}
\]

The 15-tuple \(\Theta_Q=(\Theta_{Q,x})_{x\in[15]}\), together with the two
physical endpoint masks, is its exact boundary run-state type.  A sequence
of macros avoids both forbidden words exactly when the product of these
partial maps is defined on the all-\(\epsilon\) initial vector.  This is the
same finite monoid as Theorem U5.1 with the length-three frontier suppressed.

The number 15 is specific to the pure U shore, where the two new tag bits
are constantly zero.  For the integrated four-sector braid the exact type
is the full 17-tuple, including `x,y`, unless their residence has already
been proved separately by the macro grammar.

### Lemma U7.0 (coordinate reset port)

If the first three membership bits of an entry macro are `111` in coordinate
`x`, then those three cells accept every incoming live state in
\({\mathsf S}\) and leave state \(\epsilon\).  Thus such an entry is a
universal `x`-reset port.  By contrast, prefix `00` sends every *surviving*
state to `0` but kills incoming states `01` and `011`, so it is not a
universal port.

#### Proof

Apply the `1` column of (U7.2) three times:

\[
 \epsilon\mapsto\epsilon,\qquad
 0\mapsto01\mapsto011\mapsto\epsilon,\qquad
 01\mapsto011\mapsto\epsilon\mapsto\epsilon,\qquad
 011\mapsto\epsilon\mapsto\epsilon\mapsto\epsilon.
\]

The `00` statement follows from the `0` column.  QED.

Rerooting can therefore improve the state Hall graph by exposing reset
prefixes for the coordinates active in a deficient exit type.  Merely
increasing untyped endpoint degree need not do so.

For an oriented internally clean macro `Q`, let `w_x(Q)` be its membership
word in coordinate `x`, let

\[
 s_x(Q)=\delta(\epsilon,w_x(Q)),\qquad
 D(Q)=\{x:s_x(Q)\ne\epsilon\},                       \tag{U7.3a}
\]

and, when `|Q|>=3`, put

\[
                         C_3(Q)=Q_0\cap Q_1\cap Q_2. \tag{U7.3b}
\]

For a shorter entry macro take \(C_3(Q)=\varnothing\); it can receive a reset
edge only from a macro with empty danger set.

### Theorem U7.0A (acyclic reset-Hall theorem)

Fix exactly one orientation/reroot of each physical macro, each internally
avoiding `010` and `0110`, and use those oriented macros as the vertices.
Fix initial and terminal macros `a,t`.  Form a directed seam graph
`D_reset` using only actual normal-form Johnson seams with legal lower
colours, and retain `P -> Q` only when

\[
                         D(P)\subseteq C_3(Q).         \tag{U7.3c}
\]

Assume `D_reset` is acyclic.  If the exit--entry bipartite graph obtained by
deleting exit `t` and entry `a` satisfies

\[
                         |N(S)|\ge |S|                \tag{U7.3d}
\]

for every set of exits `S`, then it contains one macro-Hamilton path from
`a` to `t`.  If its selected seam colours are pairwise distinct (for
example by a source-colour injection), the path is lower-rainbow; and its
full membership word avoids `010` and `0110` at every coordinate.

#### Proof

Hall gives a matching saturating every nonterminal exit and every
noninitial entry.  The directed cover has the unique source `a`, unique
sink `t`, and otherwise indegree and outdegree one.  Acyclicity excludes
cycle components, so all macros lie on the one `a`--`t` path.

For residence, induct along that path.  At the exit of `P`, the actual DFA
state equals the canonical state `s_x(P)`.  If it is \(\epsilon\), the next
macro follows its canonical clean trace.  Otherwise \(x\in D(P)\), so
(U7.3c) says that the first three membership bits of `Q` are `111`.
By Lemma U7.0 those bits accept every live state and reset it to \(\epsilon\);
the canonical trace is also at \(\epsilon\) there.  The actual and canonical
states then agree through the rest of `Q`.  Induction proves that no
forbidden transition occurs.  Colour simplicity is the separate stated
hypothesis.  QED.

This is a genuinely global sufficient theorem, unlike a pair-collar check.
A reroot of `Q` at position `i` has the exact reset core

\[
                C_i=Q_i\cap Q_{i+1}\cap Q_{i+2},     \tag{U7.3e}
\]

together with its rerooted danger set, physical endpoints, and available
colour.  It is admitted by this strong reset-Hall theorem precisely when
\(D(P)\subseteq C_i\) and the literal Johnson/colour tests also pass.  Other
state-specific DFA-safe edges can exist without a universal three-cell
reset.  These
occurrence-labelled profiles are therefore the correct reroot objects.  If
a reroot deletes old endpoint edges, the retained graph must be recomputed;
edge-additive monotonicity cannot be assumed.

For a single proposed boundary `A|B`, the locally forbidden cases at one
coordinate are exactly

\[
       01|0,\quad0|10,quad011|0,quad01|10,quad0|110. \tag{U7.4}
\]

These are the two nontrivial splits of `010` and the three nontrivial splits
of `0110`.  Thus the last three membership bits at an exit and first three
at an entry classify all one-boundary conflicts.  They do not classify a
whole macro path: `0|1|0` and `0|1|1|0` are the minimal conflicts spanning
two and three seams.

### U7.2 Exact local matching cuts

Delete two proposed global ports.  Let \(G_{\rm pair}\) be the undirected
graph on the remaining physical ports whose edges are actual fresh-colour
Johnson seams passing (U7.4).  Ignoring colour repetition and macro
connectivity, a locally pair-clean saturation exists if and only if

\[
                     o(G_{\rm pair}-S)\le |S|
                     \qquad(S\subseteq V(G_{\rm pair})), \tag{U7.5}
\]

where `o` counts odd components.

#### Proof

This is Tutte's perfect-matching theorem applied to the occurrence-labelled
port graph.  QED.

After fixing an orientation of every macro, the same relaxation becomes a
bipartite exit--entry graph `B_pair`.  It is feasible if and only if

\[
                    |N_{B_{\rm pair}}(X)|\ge |X|
                    \qquad(X\subseteq L),             \tag{U7.6}
\]

by Hall.  Thus, whenever this static model is infeasible, it has an
odd-component barrier in the free-port formulation or a deficient shore in
every fixed-orientation formulation.  Connectedness and minimum component
degree do not exclude either certificate.  No such static barrier is
asserted here for `0bcd...` or `3b1a...`.

The run-state types can themselves yield a smaller Hall theorem.  Partition
the two shores into types \(L_\alpha,R_\beta\) using (U7.3).  Suppose, as an
additional hypothesis, that every allowed type block
\(B[L_\alpha,R_\beta]\) is complete bipartite.  Then a perfect endpoint
matching exists whenever the type quotient satisfies

\[
       \sum_{\alpha\in A}|L_\alpha|
          \le\sum_{\beta\in N(A)}|R_\beta|
       \qquad(A\text{ a set of exit types}).          \tag{U7.7}
\]

Indeed Hall on the complete blow-up is exactly (U7.7).  For PBBS the
Johnson and fresh-colour tests make the type blocks sparse, so completeness
is an **unproved expansion hypothesis**, not a consequence of the state
classification.

### Theorem U7.1 (Hall repair by reroot bridges)

Let `B_0=(L,R;E_0)` be a retained pair-clean oriented endpoint graph after
some reroots, and let `E_+` be additional pair-clean endpoint edges created
by a further reroot bank.  Put

\[
                 \delta(X)=(|X|-|N_{B_0}(X)|)_+.      \tag{U7.8}
\]

If, for every \(X\subseteq L\), the bipartite graph

\[
                 E_+[X,R\setminus N_{B_0}(X)]         \tag{U7.9}
\]

has a matching of size at least \(\delta(X)\), then `B_0+E_+` has a perfect
matching.

#### Proof

The matching in (U7.9) supplies at least \(\delta(X)\) distinct new
neighbours outside \(N_{B_0}(X)\).  Hence

\[
 |N_{B_0+E_+}(X)|\ge |N_{B_0}(X)|+\delta(X)\ge|X|.
\]

Hall applies for every `X`.  QED.

This theorem is preserved under further edge-additive reroots.  A reroot
which changes a physical endpoint can delete old edges; then `B_0` must mean
the actually retained graph, and no monotonicity may be assumed.

### Theorem U7.2 (Tutte repair by odd-component bridges)

Let `G_0` be a retained undirected pair-clean port graph and `E_+` a set of
new pair-clean reroot edges.  For each vertex set `S`, form a graph
\(J_S\) whose vertices are the odd components of `G_0-S`, joining two when
an edge of `E_+` surviving deletion of `S` joins those components.  If

\[
         \nu(J_S)\ge
         \left\lceil\frac{(o(G_0-S)-|S|)_+}{2}\right\rceil
         \qquad(S\subseteq V(G_0)),                   \tag{U7.10}
\]

then `G_0+E_+` has a perfect matching.

#### Proof

A matching of size `m` in `J_S` pairs `2m` distinct odd components of
`G_0-S`.  First add only those `m` bridge edges.  Each paired union is even,
so this intermediate graph has exactly `o(G_0-S)-2m` odd components.
Adding the remaining edges of `E_+` cannot increase the odd-component
count: an added edge merges two components, and the parity cases
odd--odd, odd--even, even--even change that count by `-2,0,0`, respectively.
With `m` as in (U7.10), therefore

\[
                         o((G_0+E_+)-S)\le|S|.
\]

Tutte's theorem applies.  QED.

The converse lower bound is also useful: any perfect matching in an
augmented graph must either match an odd component to a vertex of `S` or
pair it across a new intercomponent edge.  Hence a barrier with excess
\(q-|S|\) requires at least \((q-|S|)/2\) matching-disjoint bridge edges
unless other reroot changes destroy the old component decomposition.

### U7.3 Correct reroot scale and the remaining lemma

The live protected U forest and the full AD natural factor have different
scales.

* In the standalone U lane, the upper-service seams and one further
  singleton absorption have already been contracted; 735 final joins remain.
  The current colour-plus-DFA degree equations are feasible, so its next
  verified obstruction is connectivity, not static Hall.  For any future
  deficient catalogue, maximum fixed-orientation Hall deficiency (U7.8)
  and worst free-port Tutte excess (U7.5) are useful **alternative**
  potentials; they are not numerically equivalent without a reduction.
  In the distributed Catalan braid of Section U8, these standalone joins
  are not required at all.
* In the separate full-factor lane, 1739 adjacent upper colours are absent.
  Corollary 2.2 forces at least 1739 new provider seams and 1740 deleted old
  edges.  Any reroot theorem for that architecture must select the upper
  service bank and the boundary-state bridges **jointly at that scale**;
  an `O(1)` postprocessing theorem cannot suffice.

The smallest useful positive statement is now the following.

> **Run-state service-bridge lemma (`RSSB`, unproved).**  One can choose the
> mandatory occurrence-labelled upper-service reroots so that, after their
> path-forest contraction, their exact profiles
> `(entry,exit,C_i,D_i,colour)` create an edge-additive acyclic reset graph;
> every Hall-deficient set `X` receives the \(\delta(X)\)
> matching-disjoint reset bridges in (U7.9) (or every Tutte barrier receives
> (U7.10)); and the bridges admit a source-injective fresh-colour assignment
> while retaining the complete internal upper bank.

Under `RSSB`, Theorem U7.1 supplies Hall, Theorem U7.0A supplies one globally
`010/0110`-free macro path, and the source injection supplies the rainbow
untagged palette.  Thus `RSSB` is a genuine sufficient common theorem, not
only a diagnostic expansion inequality.

For a U-only reroot family, `RSSB` can be applied to the current
736-component protected forest when its retained graph actually has a
barrier.  In the distributed braid it instead applies to the component-to-
macro port assignment in Section U8.  For the full natural factor, its
service family has at least 1739 members.  The theorem is deliberately a
common selection statement: separate upper-provider Hall and run-state Hall
do not imply it.

Once `RSSB` gives a degree matching, Theorems U3.2/U6.1 still require
colour-simple connectivity and the exact length-two/three staircase.  A
static Hall certificate therefore never replaces the later chronology and
compiler gates.

## U8. Catalan component neutrality in the full four-sector braid

The preceding U-only path theorems are sufficient interfaces, but the full
K17 braid has a strictly more flexible exact ledger.

Let `r>=2`, let the old ground set have size `2r-1`, and add coordinates
`x,y`.  Put

\[
 W_r=\binom{2r-1}{r},\qquad
 N_r=\binom{2r-1}{r+1},\qquad
 J_r=W_r-N_r.                                      \tag{U8.1}
\]

Since

\[
 \frac{N_r}{W_r}=\frac{r-1}{r+1},\qquad
 W_r=\frac12\binom{2r}{r},
\]

one has the exact Catalan identity

\[
                         J_r=\frac1{r+1}\binom{2r}{r}
                            =\operatorname{Cat}_r.    \tag{U8.2}
\]

### Theorem U8.1 (full component-neutral lower ledger)

Suppose the U sector is partitioned into `c` nonempty lower-rainbow Johnson
paths.  Suppose the A, X, and Y sectors are each partitioned into `J_r`
nonempty lower-rainbow paths and grouped into `J_r` legal native Y-A-X
macros.  If the resulting `J_r+c` components are joined into one globally
lower-q1-rainbow path, then every external component seam is forced to have
untagged lower colour and the four tag counts are

\[
\begin{array}{c|c}
xy&W_r-J_r=N_r,\\
x&(W_r-J_r)+J_r=W_r,\\
y&(W_r-J_r)+J_r=W_r,\\
00&(N_r-c)+(J_r+c-1)=W_r-1.
\end{array}                                           \tag{U8.3}
\]

Hence `c` cancels exactly.  The tagged families are complete, while the
untagged family has exactly one hole.

#### Proof

Each of the J paths in a sector contributes one fewer internal edge than
vertex, so the A-A, X-X, and Y-Y internal counts are `W_r-J_r=N_r`.
The J Y-A and A-X sockets raise the y- and x-tag counts to `W_r`.
Thus the xy, x, and y slot counts already equal their entire colour-family
sizes `N_r,W_r,W_r`; another external seam of one of those tags would force
a repeat.  Every external seam is therefore untagged.  The U interiors
contribute `N_r-c` such edges, and joining `J_r+c` components into one path
contributes `J_r+c-1`.  Their sum is `N_r+J_r-1=W_r-1`.  QED.

In the native class the Catalan macro count is itself forced.  If A, X, and
Y are each partitioned into the same `b` path count and grouped into `b`
legal Y-A-X macros, and every xy-tagged colour occurs exactly once on an
A-A edge, then `W_r-b=N_r`, hence `b=J_r=Cat_r`.  With this value the
X-X plus A-X and Y-Y plus Y-A slot counts are each `W_r`.

### Corollary U8.2 (strict distributed insertion ledger)

If every U path is inserted in a distinct internal gap of a linear Catalan macro
order, then

\[
 1\le c\le\min\{N_r,J_r-1\},
\]

and the untagged ledger splits as

\[
                 (N_r-c)+2c+(J_r-1-c)=W_r-1.          \tag{U8.4}
\]

For K17, `r=8`, `W_8=6435`, `N_8=5005`, and `J_8=1430`.  Thus

\[
                 (5005-c)+2c+(1429-c)=6434.           \tag{U8.5}
\]

At `c=737` the terms are `4268+1474+692`; at `c=736` they are
`4269+1472+693`.  A standalone U Hamilton path is therefore not
count-necessary.

The word "insert" is topological.  Keeping a fixed direct seam
`Y(T)-X(T)` and replacing it by `Y(T)-U-X(T)` repeats the colour `T` at
both new seams.  A rainbow insertion requires global endpoint re-pairing or
rerooting.

### Proposition U8.3 (exact untagged endpoint and palette types)

For old projections `T,T'` of rank `r` and `V,V'` of rank `r+1`, the
untagged Johnson seams are exactly

\[
\begin{array}{c|c|c}
\text{seam}&\text{criterion}&\text{lower colour}\\\hline
Y(T)-X(T')&T=T'&T,\\
Y(T)-U(V),\ X(T)-U(V)&T\subset V&T,\\
U(V)-U(V')&|V\cap V'|=r&V\cap V'.
\end{array}                                           \tag{U8.6}
\]

An A-U seam is impossible; X-X and Y-Y seams have tagged colours.  A U
component can consequently mediate a macro orientation change while
retaining tag `00`.

The U interiors use `N_r-c` untagged colours, so the residual palette has

\[
                         W_r-(N_r-c)=J_r+c             \tag{U8.7}
\]

members.  The external seam quota is `J_r+c-1`: every completion uses all
but one residual colour.  Cutting an internal U edge of colour `a` and
retaining all old external seams therefore allows the one new seam to use
only `a` or the former hole `h`; the hole respectively stays `h` or moves
to `a`.  More generally, `s` cuts give an exact basis exchange on
`{a_1,...,a_s,h}`.  Subdivision creates mobility but no slack.

### U8.4 Endpoint-type existence theorem and frozen scope

After orientations and two global terminal ports are fixed, pure endpoint
selection is a perfect matching on the remaining physical ports, hence is
governed by Tutte in the free-port model and Hall in the exit-entry model.
The exact local types are the endpoint masks, the partial maps (U7.3), and
the residual colour.  Theorem U7.0A gives a genuinely global sufficient
version: prune to an acyclic reset graph, inject the colours by source, and
verify Hall.  Theorems U7.1--U7.2 describe how reroot profiles can repair a
deficient guarded graph.

The frozen partial certificate

```text
scratch/k17_pbbs_u_yux_bridge_matching_20260731.audit.json
SHA-256 ce666738203f9c5c45a180314507c0c85dcf504d1194caf90cb481412611dc74
```

constructs 737 locally `010/0110`-safe Y-U-X bridges with 1474 distinct
untagged colours, and a 693-edge direct Y-X complement.  It is intentionally
a complete 6435-colour *local* cover; the open path ledger (U8.5) omits one
of those direct pairs.  Its own scope is exact: it consumes no A vertices
and proves neither the global A/X/Y chronology nor full boundary residence.

A later changed A attachment closes the full lower degree/palette factor:

```text
scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.audit.json
SHA-256 f9daf5e8ac7cb47d4b148789fcddcbd0d1a53030f6a9e0d173a892ed78063350
payload 520c709b458a772e9bb1e7727b558b72a3d1b1c8fafb0b95672dfc5d5dec9323
```

It is an exact all-lower-rainbow 24310-edge 2-factor on all owners, with
989 components.  This is a genuine completion of the component-neutral
lower ledger, but it has 9103 upper holes and many cyclic runs of lengths
two and three.  Opening/rethreading it to one 24309-edge path while repairing
upper and residence remains open.

Thus the component count is now removed from the K17 obstruction.  The
sharp remaining distributed-braid statement is an occurrence-labelled
choice of the `J_r+c-1` external seams, orientations, and unique omitted
colour which simultaneously satisfies the reset/full-DFA chronology,
protected upper witnesses, and the later common-cap compiler.  The
independent 1739-service floor below belongs to the separate AD full-factor
architecture and is not altered by (U8.3).

## 1. Edge colours and the open double-rainbow target

For a Johnson edge `e=AB` in \(J(17,9)\), put

\[
        \lambda(e)=A\cap B\in\binom{[17]}8,
        \qquad
        \upsilon(e)=A\cup B\in\binom{[17]}{10}.       \tag{1.1}
\]

For a word of rank-nine states

\[
                         P=(P_0,\ldots,P_{N-1}),       \tag{1.2}
\]

write \({\cal D}^+(P)\) for all interval unions of rank strictly larger
than nine:

\[
 {\cal D}^+(P)=
 \left\{\bigcup_{j=a}^{b}P_j:
             0\le a\le b<N,
             \left|\bigcup_{j=a}^{b}P_j\right|>9
 \right\}.                                            \tag{1.3}
\]

Call `P` an **open doubly-rainbow universal rank-nine path** when:

1. it lists every member of \({\cal V}\) exactly once;
2. every consecutive pair is a strict Johnson edge;
3. its 24309 values \(\lambda(P_iP_{i+1})\) are distinct; and
4. every set in

   \[
                 {\cal U}^+=\bigcup_{q=1}^{8}
                    \binom{[17]}{9+q}                 \tag{1.4}
   \]

   belongs to \({\cal D}^+(P)\).

The word “open” matters.  A lower-perfect *cycle* has 24310 edges and can
use every rank-eight colour.  Opening it into a path necessarily loses one
edge and therefore one rank-eight colour.  The lower compiler must treat
that one boundary colour separately.  Calling a 24309-edge path exactly
rainbow on all 24310 lower colours would be a counting error.

## 2. Exact symmetric-difference ledger

The next lemma does not assume that the new seams came from a prescribed
fragment catalogue.

### Theorem 2.1 (cut, colour-return, and adjacent-upper ledger)

Let `F` be a spanning 2-factor on `N` vertices whose lower-edge colours are
all distinct.  Let `P` be a spanning path on the same vertices, and put

\[
             D=E(F)\setminus E(P),\qquad
             S=E(P)\setminus E(F).                    \tag{2.1}
\]

Then:

1. \(|D|=|S|+1\).
2. The lower colours of `P` are all distinct if and only if

   \[
       \lambda(S)\subseteq\lambda(D)
       \quad\hbox{and}\quad
       |\lambda(S)|=|S|.                               \tag{2.2}
   \]

   In that case exactly one member of \(\lambda(D)\) does not occur on
   `P`.
3. For a rank-ten colour `U`, let \(m_F(U),m_D(U),m_S(U)\) be its
   multiplicities on `F`, `D`, and `S`.  The adjacent upper palette of `P`
   is complete if and only if

   \[
                 m_F(U)-m_D(U)+m_S(U)\ge1
                 \quad(U\in\tbinom{[17]}{10}).         \tag{2.3}
   \]

   In particular, with

   \[
       H_1(D)=\{U:m_F(U)-m_D(U)=0\},                   \tag{2.4}
   \]

   one necessarily has

   \[
                         |S|\ge |H_1(D)|.              \tag{2.5}
   \]

#### Proof

The factor has `N` edges and the path has `N-1`, proving (1).  Every
retained factor edge has a lower colour outside \(\lambda(D)\), and these
retained colours are distinct.  A new edge can avoid collision precisely
when its colour belongs to \(\lambda(D)\), and the new edges avoid one
another precisely when their colours are distinct.  There are `|D|`
deleted colours and `|D|-1` new edges, which proves (2).

The upper multiplicity on the final path is literally
\(m_F-m_D+m_S\), proving (3).  Every member of \(H_1(D)\) needs a new
seam whose union is that member.  One seam has only one adjacent union, so
different members need different seams.  This proves (2.5).  QED.

### Corollary 2.2 (the 1740-edge K17 floor)

For the frozen 17-cycle factor,

\[
                 |H_1(\varnothing)|=1739.             \tag{2.6}
\]

Deleting edges cannot create an old occurrence of a missing colour, so
\(H_1(\varnothing)\subseteq H_1(D)\).  Hence every adjacent-upper-complete
spanning path satisfies

\[
                 |S|\ge1739,\qquad |D|\ge1740.        \tag{2.7}
\]

This is independent of residence, deeper upper targets, and the compiler.
It rules out every repair made from a bounded number of local cycle joins.
An “alternating switch” can evade the language of prechosen fragment seams,
but not the bound: its positive support is exactly `S` in (2.1).

### Corollary 2.3 (one rank-ten debt per physical seam)

For any cut set `D`, a proposed endpoint-ladder packing must assign the
members of \(H_1(D)\) injectively to physical new seam edges.  Longer
intervals do not weaken this conclusion.  If a rank-ten target is the union
of a longer Johnson interval, some adjacent pair of distinct rank-nine
facets inside that interval already has the same union.

#### Proof

All states of the interval are rank-nine subsets of the rank-ten target.
At the first genuine transition, two distinct rank-nine facets occur; their
union is the whole rank-ten target.  QED.

## 3. Exact all-upper fragment ledger

Let `D` meet every component of `F`.  Cutting `D` gives `s=|D|` path
fragments.  Fix an orientation of each and denote them

\[
                         Q_1,\ldots,Q_s.               \tag{3.1}
\]

For a fragment `Q`, let \(\operatorname{pre}_v(Q)\) and
\(\operatorname{suf}_u(Q)\) be its first `v` and last `u` states.  Put

\[
 \mathcal L(Q,R)=
 \left\{
   \bigcup\operatorname{suf}_u(Q)\ \cup\
   \bigcup\operatorname{pre}_v(R):
       1\le u\le|Q|, 1\le v\le|R|
 \right\}.                                             \tag{3.2}
\]

This definition uses a literal oriented endpoint pair.  It does not declare
`Q|R` legal; legality additionally requires that the last state of `Q` and
the first state of `R` form a Johnson edge.

Let the **internal bank** be

\[
       K(D)=\bigcup_{i=1}^{s}
       \left\{
          \bigcup_{j=a}^{b}(Q_i)_j:0\le a\le b<|Q_i|
       \right\}.                                      \tag{3.3}
\]

It is independent of the orientation of each fragment.  Define the upper
debt after cutting by

\[
                         H_*(D)={\cal U}^+\setminus K(D). \tag{3.4}
\]

### Theorem 3.1 (complete fragment-deck identity)

If a permutation \(\pi\) concatenates the oriented fragments into one
word, then its complete interval-union deck is the union of:

1. the internal bank `K(D)`; and
2. for every \(a<b\), all values

   \[
   \bigcup\operatorname{suf}_u(Q_{\pi(a)})
   \ \cup\!!
   \bigcup_{a<j<b}\ \bigcup Q_{\pi(j)}
   \ \cup
   \bigcup\operatorname{pre}_v(Q_{\pi(b)}),          \tag{3.5}
   \]

   over all nonempty suffix and prefix lengths.

Consequently the concatenation is upper-universal if and only if every
member of `H_*(D)` occurs in the cross-fragment bank (3.5).

#### Proof

Every interval either lies in one fragment or has a unique first fragment,
last fragment, nonempty suffix of the first, every intervening fragment in
full, and nonempty prefix of the last.  These are exactly (3.3) and (3.5).
QED.

### Corollary 3.2 (one-seam bundle sufficient condition)

Suppose the debt set has a partition

\[
                H_*(D)=\mathcal B_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}\mathcal B_{s-1}, \tag{3.6}
\]

and the `j`-th physical seam of a concatenation `Q|R` satisfies

\[
                         \mathcal B_j\subseteq\mathcal L(Q,R). \tag{3.7}
\]

Then the concatenation is upper-universal.

This is sufficient, not necessary: (3.5) also permits multi-seam intervals.
Its advantage is locality.  A whole nested defect ray may be put in one
bundle and serviced by one endpoint ladder.  For protected geodesic PBBS
rays, the reciprocal-key and keyed-ear criteria give exact endpoint tests
for such service.

## 4. Short-run staircase as a literal seam guard

Fix a coordinate `x`.  A positive run in a cycle or path is a maximal
consecutive string of states containing `x`.  A cyclic positive run `R` has
an **incident edge set** consisting of its internal edges and its two
boundary edges.

Call `D` a **3-run transversal** when it meets the incident edge set of
every cyclic positive run of length at most three in `F`.  After cutting,
every surviving piece of such a run touches at least one new fragment
boundary.  This is the exact consequence needed below; cutting an internal
run edge need not delete all positive cells of the run.

For an oriented fragment `Q`, let

\[
 a_x(Q)=\text{length of its initial positive }x\text{-run},
 \qquad
 b_x(Q)=\text{length of its terminal positive }x\text{-run}, \tag{4.1}
\]

with value zero when the corresponding endpoint omits `x`.  For a proposed
physical seam `Q|R`, define

\[
 g_x(Q,R)=
 \begin{cases}
 b_x(Q)+a_x(R),&b_x(Q)>0, a_x(R)>0,\\
 b_x(Q),&b_x(Q)>0, a_x(R)=0,\\
 a_x(R),&b_x(Q)=0, a_x(R)>0,\\
 0,&b_x(Q)=a_x(R)=0.
 \end{cases}                                           \tag{4.2}
\]

Call the seam **strongly 3-safe** when

\[
                         g_x(Q,R)\in\{0\}\cup[4,\infty)
                         \quad(x\in[17]).              \tag{4.3}
\]

The test is deliberately fail-closed.  A run which continues through a
whole neighbouring fragment can sometimes make a seam with
\(g_x<4\) globally safe; (4.3) does not try to exploit that nonlocal rescue.

### Theorem 4.1 (run-transversal plus seam-guard theorem)

Assume `D` is a 3-run transversal.  If every internal physical seam of a
fragment concatenation is strongly 3-safe, then every interior positive
coordinate run of the final path has length at least four.  Short runs are
possible only at the two global path ends.

Consequently the exact depth-three monotone-deadline staircase has

\[
                         \rho_1=\rho_2=\rho_3=0,        \tag{4.4}
\]

so short-run staircase control consumes none of the K17 budget
\(\Delta_{17}=7401\).

#### Proof

Consider a final interior run of length at most three.  If it avoids every
new seam, both of its bounding zero transitions and all its internal edges
are retained old edges.  It is therefore an old cyclic short run whose
entire incident edge set missed `D`, contradicting transversality.  Hence it
touches a new seam.  If it crosses that seam, its two portions have the
length in the first case of (4.2); if it ends or begins there, its incident
portion has the length in the second or third case.  Strong 3-safety
excludes lengths one through three.  A run touching a global endpoint is
the only case not tested at an internal seam.

The exact monotone-deadline theorem obtains \(\rho_j\) from interior runs
of length at most `j`.  There are none for `j=1,2,3`; boundary runs are
automatic.  This proves (4.4).  QED.

### Remark 4.2 (exact weaker alternative)

Strong 3-safety is only a convenient local sufficient condition.  For a
fixed proposed order one may instead concatenate the 17 coordinate traces,
compute the exact arbitrary-start quantities \(\rho^\alpha\), and require
the exact schedule inequalities

\[
 \tau\ge\rho^\alpha,qquad \tau\le\alpha,qquad
 g_{i+1}\le h_i,\qquad
 \operatorname{Loss}(\alpha,\tau)\le7401.             \tag{4.5}
\]

This admits some short runs.  It is an exact final-order test, not an
edge-local Hall guard.

## 5. The guarded endpoint-ladder graph

Fix the following data.

1. A cut set `D` meeting every factor component, and orientations of its
   `s=|D|` fragments \(Q_1,\ldots,Q_s\).
2. A proposed first fragment `a` and last fragment `t`.
3. Distinct return colours

   \[
       c_i\in\lambda(D)\quad(i\ne t),                 \tag{5.1}
   \]

   using all but one member of \(\lambda(D)\).
4. A partition

   \[
               H_*(D)=\mathbin{\dot\bigcup}_{i\ne t}\mathcal B_i. \tag{5.2}
   \]

   Every adjacent rank-ten debt in \(H_1(D)\) must be assigned to a
   different source `i`, because a physical seam has only one adjacent
   union.

Let `r_i` be the last state of \(Q_i\), and `l_j` the first state of
\(Q_j\).  Define a directed edge

\[
                              i\longrightarrow j       \tag{5.3}
\]

to be **guarded admissible** when all of the following literal tests pass.

* **J (Johnson):** \(|r_i\triangle l_j|=2\).
* **L (lower return):** \(r_i\cap l_j=c_i\).
* **U (upper ladder):**

  \[
                         \mathcal B_i\subseteq
                         \mathcal L(Q_i,Q_j).          \tag{5.4}
  \]

  In particular, if \(\mathcal B_i\) contains an assigned adjacent
  rank-ten debt `U`, then \(r_i\cup l_j=U\).
* **R (run):** the seam is strongly 3-safe.

Let `G` be the bipartite graph with left shore

\[
                           L=[s]\setminus\{t\}          \tag{5.5}
\]

and right shore

\[
                           R=[s]\setminus\{a\},         \tag{5.6}
\]

containing exactly the guarded admissible edges (5.3).

This definition is the formal prohibition against arbitrary fragment
seams.  A set-theoretically plausible suffix/prefix pair is absent unless
its actual endpoint states pass `J`; a Johnson pair is absent unless it
also passes `L`, `U`, and `R` on the same occurrence-labelled endpoints.

### Theorem 5.1 (endpoint-ladder Hall theorem)

There exists a degree-correct directed cover of all fragments consisting
of one directed path from `a` to `t` and zero or more directed cycles, using
only guarded admissible seams, if and only if

\[
                  |N_G(X)|\ge|X|
                  \qquad(X\subseteq L).               \tag{5.7}
\]

Every such cover has all of the following properties.

1. Every physical seam is Johnson.
2. Its new lower colours are exactly the distinct values
   \(\{c_i:i\ne t\}\), hence the complete retained-plus-new lower deck
   consists of 24309 distinct rank-eight colours.
3. Every member of `H_*(D)` occurs in a one-seam upper ladder.
4. Under the strong run version, every component of the cover has no short
   positive run except possibly at the designated path ends.

#### Proof

The shores in (5.5)--(5.6) both have size `s-1`.  Hall's theorem gives a
perfect matching exactly under (5.7).  Direct each matched pair from its
left index to its right index.  Every fragment except `t` has one outgoing
seam and every fragment except `a` has one incoming seam.  A finite directed
graph with these degrees is one directed `a`--`t` path plus directed cycles.

Properties (1)--(3), and property (4) under the strong run guard, are
sourcewise consequences of the definitions.  The
lower colours are distinct and return all but one deleted factor colour, so
Theorem 2.1 applies.  The bundles partition `H_*(D)`, so Corollary 3.2
applies.  The run assertion is Theorem 4.1.  QED.

An exact weaker DFA guard cannot be inserted into `G` merely by labelling
each edge with an input and output state.  The selected incoming and
outgoing states of every fragment must be globally consistent with one
orientation choice, and a cycle must close in state space.  Such a model is
a lifted state-consistent matching/flow followed by literal replay, not
ordinary Hall on the fragment indices.  Theorem 5.1 and Theorem 7.1 below
use the strong state-independent guard; any DFA replacement must state and
prove that lifted consistency separately.

### Warning 5.2 (marginal Hall is not compatible Hall)

Condition (5.7) must be checked after intersecting all four guards.  Hall in
the Johnson graph, Hall in a lower-colour provider graph, Hall in an upper
ladder graph, and Hall in a run-safe graph do not imply Hall in their
intersection.  Already on two sources and two targets, the first two graphs
may support only the diagonal perfect matching while the latter two support
only the off-diagonal matching.  Every marginal saturates; the common graph
is empty.

Thus the endpoint theorem is a common-occurrence theorem, not four scalar
capacity statements.

## 6. Alternating switches are safe inside the guarded graph

Let `M` be a perfect matching of `G`.  Write `M(i)=j` when the selected seam
is `i -> j`.  Suppose distinct sources \(i_0,\ldots,i_{a-1}\) have distinct
matched heads

\[
                         j_h=M(i_h),                  \tag{6.1}
\]

and suppose every cyclic cross edge

\[
                         i_h\longrightarrow j_{h+1}
                         \quad(h\bmod a)              \tag{6.2}
\]

also belongs to `G`.  Replacing the `a` edges (6.1) by the `a` edges (6.2)
is an alternating \(C_{2a}\) switch.

### Theorem 6.1 (guard preservation and component law)

The switch in (6.1)--(6.2):

1. produces another perfect matching of `G`;
2. preserves every assigned lower return colour and upper ladder bundle,
   and preserves the run condition under the strong state-independent
   guard; and
3. if the removed arcs lie in `a` distinct components of the directed
   path-plus-cycles cover, merges those `a` components into one, reducing
   the component count by `a-1`.

If one touched component is the `a`--`t` path, the merged component is again
the unique `a`--`t` path.  If all touched components are cycles, their merge
is one cycle.

#### Proof

The old and new edge sets meet every selected source and head once, proving
(1).  Every guard in Section 5 is attached to a source and is required of
*every* edge of `G` leaving that source.  Therefore replacing its head does
not change the colour \(c_i\) or bundle \(\mathcal B_i\), and the new edge
has already passed the physical and run tests.  This proves (2).

Cut each removed directed arc.  A touched cycle becomes one directed path
from its old head to its old tail.  The cyclic reconnection (6.2) concatenates
the `a` resulting paths into one cycle.  If one touched component was the
distinguished path, cutting one of its arcs leaves a prefix and suffix; the
same cyclic reconnection inserts every other cut component between them,
leaving one path with the original global endpoints.  This proves (3).
QED.

For the optional exact finite-state staircase, conclusion (2) additionally
requires the switch to conserve the expanded boundary states, or else the
new whole-order summary must be replayed.  Pairwise seam safety alone is not
closed under a switch through singleton fragments.

The case `a=2` is a guarded alternating \(C_4\) rectangle and merges two
components.  The case `a=3` is a guarded alternating \(C_6\) and merges
three components.  These are switches in the occurrence-labelled endpoint
graph; a formal set rectangle not present in `G` is not a legal switch.

### Corollary 6.2 (loose connector forest)

Suppose a perfect matching supplied by Theorem 5.1 has `c` directed
components and there is a sequence of guarded alternating switches such
that each switch meets distinct current components and the component count
falls to one.  Then the final matching gives one literal spanning path and
retains every conclusion of Theorem 5.1.

A convenient static sufficient certificate is a support-disjoint loose
hyperforest of component-transversal switches, ordered from its root.  In
particular, when `c=17`, a loose spanning 3-tree has

\[
                         \frac{17-1}{2}=8              \tag{6.3}
\]

hyperedges.  Eight guarded \(C_6\)'s therefore fuse all 17 components into
one.  If parity or support prevents such a 3-tree, one guarded \(C_4\) or
another even-support connector changes the component parity.

## 7. The deterministic K17 conversion theorem

### Theorem 7.1 (guarded PBBS endpoint-ladder conversion)

For the frozen 17-cycle factor `F`, suppose there exist:

1. a cut set `D` with \(|D|=s\ge1740\), meeting every factor component and
   every cyclic positive run of length at most three;
2. orientations of the resulting `s` fragments and choices of first/last
   fragments `a,t`;
3. a bijective lower-return assignment (5.1), omitting one deleted colour;
4. a partition (5.2) of the exact internal-bank debt `H_*(D)` into
   one-seam ladder bundles, with the adjacent rank-ten debts assigned to
   distinct sources;
5. the guarded Hall inequalities (5.7); and
6. a guarded alternating-switch fusion sequence from one Hall matching to
   one component.

Then concatenating the fragments in the final matching order gives an open
doubly-rainbow universal rank-nine path.  It has:

\[
 \begin{array}{ll}
 \text{vertices:}&24310\text{ distinct rank-nine sets},\\
 \text{edges:}&24309\text{ strict Johnson seams/internal edges},\\
 \text{lower deck:}&24309\text{ distinct rank-eight intersections},\\
 \text{upper deck:}&{\cal U}^+\text{ in the literal interval-union deck},\\
 \text{residence:}&\text{no interior positive run of length }1,2,3.
 \end{array}                                             \tag{7.1}
\]

In particular its depth-three short-run staircase is feasible with zero
run loss.  The conclusion is one physical path; the rankwise witnesses are
not selected independently.

#### Proof

The final matching is one directed path by Theorem 6.1 and hypothesis (6).
It uses every fragment once and every retained factor edge once, hence every
rank-nine owner once.  Johnson legality is guard `J`.  The lower statement
is Theorem 2.1 plus guard `L`.  The upper statement is Theorem 3.1 plus
guard `U` and the bundle partition.  The residence and staircase statements
are Theorem 4.1.  QED.

### Scope of Theorem 7.1

The theorem is fully proved, but its six hypotheses are construction data,
not properties already known for the PBBS factor.  In particular:

* the old PBBS all-depth support theorem does not imply that it survives a
  chosen 1740-edge cut set;
* many Johnson endpoint pairs do not imply the lower-return identities;
* separate endpoint, colour, ladder and residence margins do not imply
  guarded Hall; and
* Hall gives a path cover, not a connected path, until the alternating
  connector condition is supplied.

## 8. Exact remaining endpoint-ladder theorem for the AD full factor

For the separate AD full factor `542a...`, the sharp checkable target exposed
by Sections 1--7 is the following.

> **AD-K17 guarded endpoint-ladder packing (`AD-K17-GELP`, unproved).**  The
> frozen factor admits data (1)--(5) of Theorem 7.1 for which one Hall
> matching lies in the guarded alternating-switch component of a connected
> matching.

Equivalently, one may replace the final phrase by an explicit loose
connector forest.  This is strictly stronger than ordinary Hall but much
smaller than an unconstrained word search: all variables are occurrence-
labelled factor cuts, oriented fragments, and actual endpoint seams.  It is
not the remaining theorem for the distributed Catalan architecture of
Section U8.

The following necessary conditions should be applied before any search or
claimed construction.

1. `s >= 1740` by Corollary 2.2.
2. Every q1 debt has a distinct seam source.
3. Every new seam returns a distinct deleted rank-eight colour; no new
   colour outside the deleted set is allowed.
4. The cut set hits every old short run not tolerated by the exact
   staircase.
5. Every target whose complete old witness family is cut belongs to an
   actual new ladder bundle.
6. The intersected guarded graph, not its four marginals, satisfies Hall.
7. Its matching exchange space contains a component-fusing sequence.

Failure of (6) has an ordinary Hall witness \(X\subseteq L\) with
\(|N_G(X)|<|X|\).  Failure of (7) has a matching-component obstruction:
the selected matching lies in a guarded alternating component containing no
connected cover.  These are the two exact certificates requested by the
endpoint-ladder formulation.

## 9. The 5004-shore specialization

The four-sector construction uses a selected index shore `I` of size 5005.
If one asks only for a path through those 5005 selected objects, the
endpoint-Hall and alternating-component lemmas apply with

\[
                            N_I=5005,\qquad N_I-1=5004. \tag{9.1}
\]

The full-factor deleted-colour return identity does **not** apply to this
shore.  If its fixed internal fragment bank uses `5005-f` distinct colours,
each of its `f-1` seams may use any fresh colour outside that bank and the
previous seams.  The available fresh count is `1430+f`, as proved in
Proposition U1.1.

Thus 5004 distinct intersection colours are the correct requirement for
that **subshore path**.  But a path through `I` is not by itself a spanning
path through \(\binom{[17]}9\).  To use it inside the four-sector carrier one
must additionally prove:

1. its endpoints splice legally to the `X,Y,A` sectors;
2. its 5004 lower colours do not collide with the 19305 other path-edge
   colours; and
3. the combined 24309-edge lower deck omits exactly one rank-eight colour.

The number 5004 therefore cannot replace 24309 in Theorem 7.1.  It is a
valid smaller ladder subproblem and nothing more.  Section U8 shows a second
possibility: keep the U shore disconnected and distribute its components
among the Catalan macros.  That architecture realizes the full untagged
ledger directly and does not require a 5004-edge standalone U path.

## 10. Independent audit and proved/open boundary

The theorem package received an independent adversarial audit.  That audit
forced five scope corrections now incorporated above:

1. the static pair-clean graph of `0bcd...` is SAT, not UNSAT;
2. the current U bank has 736 rather than 737 components and already has a
   colour-plus-DFA degree cover;
3. the explicit C6 is globally palette-neutral but not neutral under a
   fixed source-colour assignment;
4. a service hypermatching also needs a fragment-forest condition before
   contraction into path macros; and
5. ordinary Hall supports only the strong state-independent run guard,
   whereas a weaker DFA model needs global state consistency.  The acyclic
   reset-Hall theorem supplies one sound global alternative.

The decisive identities have independent derivations.  The Catalan ledger
follows both from the four tag counts and from the strict insertion
decomposition.  The edge-count/lower-return statement follows both from
edge cardinality and from retained/deleted/added palettes.  The 1740 floor
follows both from (2.3) targetwise and from injection of the 1739 old q1
holes into new seams.  The all-upper theorem is a literal partition of
intervals by first and last fragment.

This mathematical lane ran no new finite SAT or stochastic search and used
no web query.  It does cite existing exact finite artifacts; those inputs
must not be confused with the unconditional theorems.  The principal ledger
is:

```text
source PBBS factor
  scratch/k15_dual_descent_a4_step19.segments.json
  d4e2dacd881c968f431925db178d44180cec5981c04862aa2e4a4a50d14dd504

historical upper-complete 737-bank
  scratch/k17_pbbs_u_upper_complete_20260731.fragments
  f7ea82ae64a396da5db80836af55c16f3ebc8b96e8e354384423b4b96df944c8

current upper-complete 736-bank
  scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments
  3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465
  independent audit
  8b29fb3fea8a782d543f1054720328bc92f158e7535d487eab90ac04370be88d
  colour/DFA degree-cover audit
  b5546718ea4bc927825fe801f09efdb1ad7bf468bc01291fc99d2057de0d1e4f
  independent degree-cover replay
  2c5c5727386fa3b0044bc6085648922dfa0321544cf3cdad12850991dd6a73fb
  first rainbow/full-DFA component-reducing switch
  0470ff016bbadf7a44d3a692a13f690c080bcf48f5616bdf7bc235ca8f6f6319

historical 0bcd pair-local SAT replay
  scratch/k17_pbbs_u_0bcd_pairsafe_degree_sat_20260731.audit.json
  2f55f4bcdca7634384004652e3c496d5687c29c66819992f0d7a017e90653e71

partial distributed Y-U-X bridge cover
  scratch/k17_pbbs_u_yux_bridge_matching_20260731.audit.json
  ce666738203f9c5c45a180314507c0c85dcf504d1194caf90cb481412611dc74
  matching table
  e602f2f3abc91909bec42bdde02422001d9c78f354207c7fd69b0288d99c4148

exact distributed lower-rainbow 2-factor
  scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.audit.json
  f9daf5e8ac7cb47d4b148789fcddcbd0d1a53030f6a9e0d173a892ed78063350
  payload 520c709b458a772e9bb1e7727b558b72a3d1b1c8fafb0b95672dfc5d5dec9323

separate AD full factor
  scratch/ad_k17_k15_four_sector_factor_20260731.json
  542a40b2ba905a939e157bdb973b59d873cf22b9b7c3eb86bc15d11ff078a7f3
```

The exact proved/conditional boundary is

\[
\boxed{
\begin{array}{c}
J_r=W_r-N_r=\operatorname{Cat}_r,
\quad (N_r-c)+(J_r+c-1)=W_r-1;\\[1mm]
\text{component count is neutral, but endpoint type and colour pressure are
not};\\[1mm]
\text{acyclic reset-Hall plus colour injection gives a globally resident
macro path};\\[1mm]
\text{AD-K17-GELP gives a full lower/upper/zero-run path, and every such AD
repair}\
\text{uses at least 1739 new and deletes at least 1740 old edges};\\[1mm]
\text{the distributed lower factor exists, but its upper/resident connected
rethread and compiler remain open.}
\end{array}}
\]

Thus the sharp new theorem is not a Hamiltonization statement.  Catalan
subdivision removes the component-count charge exactly; the minimal missing
existence theorem is a common occurrence-labelled selection of upper-service
reroot profiles whose reset/colour graph satisfies Hall (or Tutte after
forgetting orientation) while preserving the protected upper bank and the
one-hole lower palette.  In the separate AD architecture this common
selection must operate at the forced 1739-service scale.
