# The adjacent-cut `K17` tail: forced direct ears and the exact residual packet lift

Date: 2026-07-31  
Lane: AD  
Status: exact literal certificate for the `572` forced direct ears; exact
provider/filler ledger; exact `4/5` bounded-packet theorem; and exact relaxed
port-Hamilton/repeat-factor reduction after a clean unique-provider stage.
The fixed provider certificate is not clean and the repeat factor has not
been solved.  No `K17` word is claimed.

## 0. Result and precise boundary

For cyclic cut separation `s=1` (equivalently `s=16`), the immutable
Greene--Kleitman seed is a matching of `3640` Johnson edges on `7280`
rank-seven owners.  It has no old rank-nine turn and leaves `12168` unused
rank-seven owners.  The supported provider projection has full rank
`8736/8736`, but `572` of its lower-colour rows have only old--old providers.

Those exceptional rows have no obstruction **at the isolated direct layer**.
An independently replayed certificate chooses `572` old--old edges with

```text
572 distinct missing rank-six colours,
572 distinct fresh rank-eight unions,
1144 distinct old endpoints,
1144 distinct boundary rank-nine turns.
```

More strongly, the `1144` endpoints belong to `1144` different seed edges.
Thus the direct ears form a matching even after the seed edges are
contracted.  Charging them leaves a literal path forest `F_0` with

\[
 |V(F_0)|=7280,
 \quad |E(F_0)|=3640+572=4212,
 \quad c(F_0)=3068,                                  \tag{0.1}
\]

and exactly `6136=2*3068` exposed old ports.

A later exact full-tail audit proves that each of the two displayed
`572`-edge banks is individually unextendable even in the raw residual
q6/q8/degree b-factor.  This does not invalidate the local certificate or
classify all minimum direct banks.  Any live construction must therefore
choose the direct bank jointly with the full tail (or allow more than `572`
direct edges); the remainder of this note is an exact conditional reduction
for a clean jointly chosen core.

The shortest balanced residual packet schedule is uniquely

\[
                  x_4=2637,\qquad x_5=430.            \tag{0.2}
\]

It consists of `3067` long ears, uses all `9631` inserted owners, and has

\[
 6134\text{ endpoint--unused edges},
 \qquad 6564\text{ unused--unused edges}.             \tag{0.3}
\]

The exact remaining gate is not another ordinary Hall test.  A concrete
capacity-feasible choice of all `8164` residual providers now exists, but it
has `17` illegal saturated wedges, `1764` central rank-nine collision units,
and four owner cycles.  These defects must be removed by correlated provider
reselection or alternating packets.  Once the unique-provider core is a
clean forest, the `4/5` schedule is optional: the `4534` repeats form an
exact port-Hamilton factor on `2656+1879=4535` contracted nodes.  Conditional
on the prescribed no-new-to-new diamond topology, their tail rank-five row
is an exact guarded grouped SDR: every facet-distinct centre-local domain has
raw size `20` (an equal-facet centre has an empty list), external endpoint
guards reduce full pair lists to
`12,13,16`, or `20` before bank filtering, and `776` singleton lists have
raw size at least four after facet-distinctness checks.

## 1. Seed matching and forced direct rows

Let `F` be the `s=1` seed matching in `J(17,7)`.  Write `B` for its `7280`
old owners and `Z` for the `12168` unused owners.  For a Johnson edge `xy`
put

\[
                  L(xy)=x\cap y,\qquad Q(xy)=x\cup y. \tag{1.1}
\]

A provider for a missing rank-six colour `D` is a supported fresh edge
`xy` with `L(xy)=D`.  Call it `BB`, `BU`, or `UU` according as zero, one, or
two of its endpoints lie in `Z`.

### Lemma 1.1 (a `BB` provider is a direct ear)

In any maximum-degree-two completion containing `F`, a selected `BB` edge
is an entire length-one ear between two seed components.

#### Proof

Each endpoint of a `BB` edge already has degree one in `F`.  The new edge
raises both degrees to two, so neither endpoint can be incident with another
new edge.  If the two endpoints belonged to the same seed component, the
new edge would close a two-edge cycle; such candidates were removed from
the supported catalogue.  Hence the edge is a direct ear between distinct
seed components. \(\square\)

The independent extraction finds exactly `572` missing colours whose every
supported provider is `BB`.

### Theorem 1.2 (private exceptional matching)

There is a simultaneous selection of one provider for each of the `572`
exceptional colours such that:

1. its rank-eight unions are pairwise distinct and avoid `Q(F)`;
2. its `1144` old endpoints are pairwise distinct;
3. its two boundary rank-nine turns per direct ear are pairwise distinct;
4. its `1144` endpoints belong to `1144` distinct seed components.

Consequently the quotient direct-edge graph is a matching of size `572`.
After adjoining it to `F`, the component census is

\[
           572\text{ two-dimer paths}+2496\text{ single dimers},          \tag{1.2}
\]

so it has `3068` components, no cycle, and `6136` exposed ports.

#### Proof

The frozen table names the lower colour, upper union, two old endpoints and
two boundary turns of every selected direct ear.  Direct replay verifies
all four injectivity assertions.  Mapping each endpoint to its seed mate
gives quotient-degree histogram `1^1144`; hence no seed component occurs
twice.  A matching of `572` edges decreases the number of components from
`3640` to `3068` and cannot create a cycle. \(\square\)

This is stronger than a vertex-disjoint `BB` selection.  Component privacy
is what makes the contracted residual topology literal.

## 2. Why `4/5` is the canonical bounded-length schedule

After the direct ears are charged, `3068` path components must be joined by
`3067` residual ears.  They must collectively contain `9631` unused internal
owners.

If every residual ear had length at most four, it would contain at most
three internal owners, for a total at most

\[
                         3(3067)=9201<9631.            \tag{2.1}
\]

Thus maximum length at least five is unavoidable.  Restricting to the two
consecutive lengths four and five gives

\[
 x_4+x_5=3067,
 \qquad 3x_4+4x_5=9631,                              \tag{2.2}
\]

whose unique solution is (0.2).  Hence (0.2) attains the smallest possible
maximum ear length.

This is a **balanced sufficient subclass**, not a resource-preserving WLOG
normalization of every possible completion.  No claim is made that a
completion using other lengths can always be converted to (0.2).

Every length-four packet has owner pattern

\[
                         B-U-U-U-B,                   \tag{2.3}
\]

and every length-five packet has pattern

\[
                         B-U-U-U-U-B.                 \tag{2.4}
\]

Therefore the packet edges and turns have the exact ledger

\[
\begin{array}{c|r}
\text{residual ears}&3067\\
\text{internal owners}&3(2637)+4(430)=9631\\
\text{residual edges}&4(2637)+5(430)=12698\\
BU\text{ edges}&2(3067)=6134\\
UU\text{ edges}&2(2637)+3(430)=6564\\
\text{residual turns}&5(2637)+6(430)=15765.
\end{array}                                           \tag{2.5}
\]

Together with the `572` direct edges and their `1144` turns, this gives the
required `13270` new edges and `16909` tail turns.

## 3. Exact residual packet theorem

Contract each component of `F_0` only for the topology row; all literal old
owners and endpoint labels remain part of a packet.

### Theorem 3.1 (residual `4/5` packet lift)

A completion in the schedule (0.2) exists if and only if there are `2637`
oriented length-four packets and `430` oriented length-five packets with all
of the following properties.

1. Every packet is a simple Johnson path of the form (2.3) or (2.4) between
   exposed endpoints of two distinct current components.
2. Packet internal-owner sets are pairwise disjoint; their union has size
   `9631` and lies in `Z`.
3. The packet endpoints use `6134` distinct exposed ports of `F_0`, leaving
   exactly two old ports as the global path endpoints.
4. The `12698` packet edges have the type counts (2.5), and designated
   occurrences among them cover each of the `8164` remaining missing
   rank-six colours.
5. Every residual rank-eight union is distinct and avoids the `4212`
   rank-eight colours already used by `F_0`.
6. Every one of the `15765` packet boundary/internal turns has rank nine;
   these turns are pairwise distinct and avoid the `1144` direct-core turns.
7. The `3067` packet links are graphic-independent on the `3068` contracted
   components of `F_0`.

Under these conditions the union is one literal path.  Conversely, every
literal completion in the schedule (0.2) uniquely supplies these rows.

#### Proof

Rows 1--3 give maximum owner degree two.  A contracted component has two
exposed ports, so the packet quotient also has maximum degree two.  It has
`3068` vertices and `3067` edges.  Row 7 makes it a forest; a forest with
`v-1` edges is connected, hence this quotient is one path.  Expanding its
components and packets gives a literal owner path, while rows 4--6 give the
declared lower service and fresh rank-eight/rank-nine palettes.

Conversely, cut a completed path at its `F_0` edges.  The remaining pieces
are its oriented residual ears.  Their lengths, owners, ports, resource
occurrences and contracted links give rows 1--7. \(\square\)

In an edge/wedge model, degrees and a graphic cut do not by themselves
enforce the internal-size histogram `3^2637 4^430`.  One must either select
materialized packet columns or add an exact component-length state.  This is
the first model-size distinction that the ordinary provider projection
misses.

## 4. Provider/filler wedge identities

Of the `12698` residual edges, `8164` are designated providers and `4534`
are repeat/decorated filler occurrences.  Let

* `p` be the number of provider `BU` edges;
* `A,B,C` be the numbers of internal `PP,PF,FF` wedges, respectively.

The remaining edge types are forced:

\[
\begin{aligned}
 P_{UU}&=8164-p,\\
 F_{BU}&=6134-p,\\
 F_{UU}&=6564-(8164-p)=p-1600.
\end{aligned}                                         \tag{4.1}
\]

Nonnegativity alone gives

\[
                         1600\le p\le6134.             \tag{4.2}
\]

The authenticated supported catalogue is sharper: `3640` demand rows are
`UU`-only, `1001` are `BU`-only, and `3523` allow both types.  Hence every
physical supported selection satisfies

\[
                         \boxed{1600\le p\le4524}.      \tag{4.2a}
\]

Counting provider and filler incidences at the `9631` internal owners gives

\[
\begin{aligned}
 A+B+C&=9631,\\
 2A+B&=16328-p,\\
 B+2C&=2934+p,\\
 p&=6697-A+C.
\end{aligned}                                         \tag{4.3}
\]

In particular

\[
                  2173\le A-C\le5097,                 \tag{4.4}
\]

so every physical supported residual lift has at least `2173` more
provider--provider than
filler--filler internal wedges.  The full `16909` tail turn events partition
exactly as

\[
\begin{array}{c|c}
\text{pure-provider turns}&7841+C\\
\text{mixed turns}&B\\
\text{pure-filler turns}&A-563.
\end{array}                                           \tag{4.5}
\]

Here the first row includes the `1144` charged direct-core turns and the
`p` residual provider boundary turns.

#### Proof

Equation (4.1) subtracts provider counts from the fixed `BU/UU` capacities.
A provider `BU` edge has one internal incidence and a provider `UU` edge has
two, giving `16328-p=2A+B`.  The analogous filler count is
`2934+p=B+2C`.  Eliminating `p`, and then using the supported type bound
(4.2a), proves (4.3)--(4.4).  Provider boundary turns
plus central `PP` turns number `1144+p+A=7841+C`; filler boundary turns plus
central `FF` turns number `6134-p+C=A-563`. \(\square\)

### Remark 4.1 (a formal unfiltered ledger face)

If one ignores the authenticated provider-type catalogue and formally sets
`p=6134`, all residual `BU` edges are providers and all `4534` fillers are
`UU`.  For some integer `t=C`,

\[
                    (A,B,C)=(563+t,9068-2t,t).         \tag{4.6}
\]

Within the `2637` core strings of length two and `430` core strings of
length three, let `R` be the number of filler runs.  Then

\[
 R=4534-t,
 \qquad 2052\le R\le3497,
 \qquad \boxed{1037\le t\le2482}.                    \tag{4.7}
\]

#### Proof

For binary strings, the number of filler runs equals the number of filler
edges minus the number of adjacent `FF` pairs.  At most one run fits in a
length-two string and at most two in a length-three string, giving
`R<=2637+2(430)=3497`.  To minimize runs, fill all `430` length-three
strings and then `1622` length-two strings, giving `R>=430+1622=2052`.
Substitute `t=4534-R`. \(\square\)

The scalar extremes in (4.7) are realizable as binary strings.  The physical
shift-one catalogue has `p<=4524`, so this formal face is **not** a supported
completion and is retained only as an algebra check.

## 5. Authenticated capacity checkpoint and its exact defects

After charging the `572` direct ears, an exact capacity model selects one
edge for every remaining missing rank-six colour with distinct rank-eight
unions, old-port capacity one, unused-owner capacity two, and globally
injective boundary rank-nine turns.  Its residual selected-edge census is

\[
              BU=3065,\qquad UU=5099.                 \tag{5.1}
\]

Together with the direct core it has

\[
\begin{array}{c|r}
\text{distinct forced boundary turns}&4209\\
\text{unused degree zero/one/two}&4416/2241/5511\\
\text{old ports still unused}&3071.
\end{array}                                           \tag{5.2}
\]

Thus the exact repeat-degree deficit is

\[
\begin{array}{c|r}
\text{new zero-degree unused owners to select}&1879\\
\text{repeat }BU\text{ edges}&3069\\
\text{repeat }UU\text{ edges}&1465\\
\text{repeat edges total}&4534.
\end{array}                                           \tag{5.3}
\]

The incidence identity is

\[
 2241+2(1879)=5999=3069+2(1465).                      \tag{5.4}
\]

This closes the provider rank-eight/vertex-capacity marginal.  It does not
close the physical unique-provider core.  Literal replay finds

\[
\begin{array}{c|r}
\text{degree-two provider centres}&5511\\
\text{illegal provider wedges}&17\\
\text{compatible central-turn occurrences}&5494\\
\text{distinct compatible central colours}&3991\\
\text{central duplicate units}&1503\\
\text{central colours colliding with the boundary bank}&261\\
\text{total central collision units}&1764.
\end{array}                                           \tag{5.5}
\]

There is also a topology defect not recorded by the capacity solver.  The
fixed base+direct+provider graph has

\[
 |V|=15032,\quad |E|=12376,\quad c=2660,              \tag{5.6}
\]

and exactly four cyclic components, each of cycle excess one.  These cycles
are saturated, so adding repeat edges cannot open them.

### Lemma 5.1 (fixed-checkpoint repair obligations)

Any completion descended from this exact provider edge set must first
change provider incidences so as to:

1. hit at least one incident provider edge at each of the `17` illegal
   centres;
2. change at least `1764` rank-nine turn occurrences in total, counted with
   multiplicity, unless a changed chronology removes those occurrences; and
3. break each of the four selected owner cycles.

These obligations may be discharged by the same correlated exchanges; they
are not asserted to be additive lower bounds on the number of packets.

#### Proof

A saturated degree-two illegal centre cannot receive a filler edge, so one
of its selected incident edges must change.  If a colour occurs `m` times
among the central events and the protected boundary bank, at least `m-1`
of those occurrences must change to make the row injective; summing gives
`1764`.  Finally, adding edges cannot destroy an existing cycle. \(\square\)

For the restricted actuator class of disjoint, physical vertex-supported
`3<->3` C6 toggles whose symmetric difference is one simple six-owner cycle
and which leave every off-support turn unchanged, one toggle changes at
most six owner-turn occurrences.  Therefore this particular checkpoint
needs at least

\[
                         \left\lceil1764/6\right\rceil=294             \tag{5.7}
\]

such toggles.  This is a support lower bound for that actuator class only;
longer rethreads or a fresh global provider selection are not covered.

## 6. Exact contracted port-Hamilton factor

Abandon the `4/5` packet lengths after the unique-provider stage.  Suppose
the base, direct ears and `8164` unique-provider edges have instead been
chosen so that they form a clean acyclic maximum-degree-two graph `K` with
the same vertex and edge counts as (5.6), and define `V(K)` to be its
nonisolated support.  Then

\[
                         c(K)=15032-12376=2656.         \tag{6.1}
\]

Every component of `K` is a path, so it has two ports.  Choose `1879`
currently zero-degree unused owners and regard each as a singleton node
with two ports.  The contracted repeat problem has

\[
                         2656+1879=4535                 \tag{6.2}
\]

nodes and must select `4534` edges.

### Theorem 6.1 (repeat port-Hamilton equivalence in the fresh decorated subclass)

Fix a clean unique-provider forest `K`.  In the subclass in which repeat
edges have fresh/injective rank-eight and rank-nine resources and are
literalized by the deletion code below, a completion on the current
`BU=3069,UU=1465` face exists if and only if there are a set `Z_0` of `1879`
zero-degree unused owners and a set `R` of `4534` fresh Johnson edges such
that:

1. every port of `K` has `R`-degree one except two declared global ports,
   which have degree zero;
2. every `z in Z_0` has `R`-degree two and every other zero-degree unused
   owner has degree zero;
3. `R` has exactly `3069` `BU` and `1465` `UU` edges;
4. its rank-eight unions are pairwise distinct and avoid the `12376`
   base/direct/unique-provider bank;
5. the `3069+2241+1879=7189` new boundary/internal rank-nine turns have rank
   nine, are pairwise distinct, and avoid the `9720` clean-core turns;
6. all lower-repeat payloads admit the deletion-label assignment in
   Theorem 6.2 below; and
7. `K union R` is acyclic.

Then `K union R` is one literal path on `16911` owners.  Conversely every
completion in this fixed decorated subclass supplies rows 1--7.

#### Proof

After adding `Z_0`, there are `16911` owners.  The graph has
`12376+4534=16910` edges and maximum degree two, with exactly two degree-one
owners by rows 1--2.  Row 7 makes it a forest; a forest with `v-1` edges is
connected, hence it is one path.  Rows 3--6 give the declared resource and
compiler semantics.  Necessity follows by deleting the repeat edges from
any path in this subclass. \(\square\)

Thus no prescribed ear-length histogram or owner-level subtour family is
needed.  On the contracted `4535`-node graph, degree two plus graphic
independence is exactly the Hamilton-path row.

### Theorem 6.2 (deletion-label SDR on a fixed repeat factor)

For `e=vw in R`, put `C_e=v intersect w`, a rank-six set.  Choose a deletion
label `g_e in C_e` and the rank-five source

\[
                         A_e=C_e-\{g_e\}.              \tag{6.3}
\]

Let `B_5` be an allowed tail rank-five bank.  It may be prescribed in
advance, or it may be the bank output by this tail and passed to the prefix
as a complement constraint.  The repeat factor has a valid literal deletion
assignment if and only if:

1. `A_e in B_5` for every repeat edge and the map `e -> A_e` is injective
   (bijective when `|B_5|=4534`);
2. at every internal carrier owner `v` incident with a repeat edge, the two
   incident lower facets are distinct and the two incident source letters
   have union exactly `v`.  The two global path endpoints use their separately
   specified outer boundary sources; in Theorem 6.1 no repeat edge is incident
   with either endpoint.

Writing the incident lower facets as

\[
 C_e=v-\{x\},\qquad C_f=v-\{y\},\qquad x\ne y,         \tag{6.4}
\]

Facet distinctness is automatic for two unique edges in the rainbow core.  If two
incident facets coincide, both source letters lie in the same proper facet
of `v`, so no deletion assignment exists.  For distinct facets, if only `e`
is a repeat, the union row is equivalent to `g_e != y`.  If both are repeats,
it is equivalent to

\[
                 g_e\ne y,\qquad g_f\ne x,
                 \qquad g_e\ne g_f.                  \tag{6.5}
\]

#### Proof

Distinctness gives the required tail bank, and when `|B_5|=|R|` it gives
exactly `B_5`.  For (6.5), a coordinate can be absent from both source
letters only if a deletion label equals the opposite missing coordinate or
the two deletion labels coincide.  Excluding precisely those cases makes
their union `v`; the one-repeat case is the same calculation with the other
facet unshrunk.  Equality of the two facets makes the union a subset of that
facet and proves the rejection row. \(\square\)

For a fixed physical path, Theorem 6.2 is a finite conflict-SDR: each repeat
edge has at most six label options; equal rank-five targets conflict
globally, and adjacent repeat edges have the local forbidden pairs (6.5).
Equivalently, decompose the repeat edges into maximal consecutive runs,
enumerate every locally legal label word on each run, and choose one word
per run with disjoint target sets.  This run-hypergraph formulation absorbs
all local union constraints before the global SDR.  Ordinary rank-five Hall
without the run state is insufficient.

### Theorem 6.3 (raw Boolean diamonds and the exact guarded grouped SDR)

Assume the contracted repeat topology has the following prescribed diamond
form: each of the `1879` new unused centres is incident with two **distinct**
repeat edges, no repeat edge joins two new centres, each pair edge's non-new
endpoint is a `K`-port incident with exactly one unique-core edge, and every
other repeat edge is isolated between two such unique-core ports.  This
topology is not yet constructed.  Conditional on it, the `4534` repeat edges
partition into

\[
 1879\text{ ordered two-edge groups}+776\text{ singleton groups},          \tag{6.6}
\]

because `2(1879)+776=4534`.

If the two centre facets coincide, the pair list is empty by Theorem 6.2.
Otherwise, for a two-edge group at centre `v`, write

\[
 C_e=S\cup\{y\},\qquad C_f=S\cup\{x\},
 \qquad |S|=5.                                         \tag{6.7}
\]

At the new centre alone, the locally legal deletion pairs are exactly

\[
                     (g_e,g_f)\in S^2,qquad g_e\ne g_f,                 \tag{6.8}
\]

so every centre has a raw `5*4=20` Boolean-diamond domain.  This is not yet
the full pair-group list: each repeat edge also meets a unique-core edge at
its other endpoint.

If the repeat and unique facets coincide at either external endpoint, the
pair list is empty by Theorem 6.2.  Otherwise that endpoint supplies one
forbidden deletion coordinate.  After the centre restrictions are imposed,
let `F_e,F_f` be the resulting additional guard sets inside `S`; each is
either empty or a singleton.  Before a prescribed-bank filter, the exact
guarded label list is

\[
 \mathcal O_v=\{(g_e,g_f):g_e\in S\setminus F_e,
       g_f\in S\setminus F_f, g_e\ne g_f\}.            \tag{6.8a}
\]

Its size is `20` if both guards are empty, `16` if exactly one is active,
`12` if the same guard is active on both sides, and `13` if two distinct
guards are active.  If `B_5` is prescribed, retain only options for which
both resulting rank-five targets lie in `B_5`; this can reduce the list
further.

A singleton repeat is adjacent to unique edges at both ends.  Equal facets
at either end give an empty list.  Otherwise its two endpoint guards leave
at least four deletion labels before prescribed-bank filtering.

After the topology and all guards are fixed, tail rank-five literalization
is exactly the following grouped SDR: choose one two-target option from each
guarded pair list and one target from each guarded singleton list so that all
`4534` chosen rank-five targets are distinct.

#### Proof

At a new centre, (6.5) says `g_e,g_f` both lie in the common five-set `S`
and are unequal, giving the raw twenty choices.  The one-repeat calculation
at each far endpoint gives its additional unary guard, hence (6.8a).  For
allowed-set sizes `5,5`, `4,5`, `4,4` with equal excluded coordinates, and
`4,4` with distinct excluded coordinates, subtracting the allowed diagonal
gives respectively `20,16,12,13`.  The singleton bound is `6-2=4` after two
distinct-facet guards.  The groups partition the repeat edges by hypothesis,
so all local union constraints have now been compiled into their guarded
option lists.  The only remaining tail rank-five condition is global target
injectivity, which is precisely the grouped SDR. \(\square\)

For a group family `X`, let `N(X)` be the union of all targets appearing in
any option of a group in `X`, and let

\[
                   d(X)=2|X_{\rm pair}|+|X_{\rm single}|.                \tag{6.9}
\]

Every grouped SDR satisfies the necessary inequalities

\[
                             |N(X)|\ge d(X).             \tag{6.10}
\]

They are not sufficient.  Two pair groups on four targets with option
families

\[
                 \{\{a,b\},\{c,d\}\},
 \qquad          \{\{a,c\},\{b,d\}\}                 \tag{6.11}
\]

satisfy (6.10), but every option from the first intersects every option from
the second.  Thus union-cardinality inequalities do not characterize an
arbitrary grouped-choice system.  No embedding of (6.11) into the restricted
physical Boolean-diamond lists is asserted here; for that special family,
ordinary projected Hall might conceivably be strengthened by additional
structure.

There are two rigorous absorber interfaces.

1. **Direct option selection.**  Make a conflict graph whose vertices are
   group options and whose edges mean a shared rank-five target.  Any
   independent transversal is the desired SDR.  Haxell supplies one if each
   group list has size at least `max(1,2 Delta)`, where `Delta` is the global
   conflict degree.  The raw
   centre size `20` and singleton bound `4` do not by themselves prove that
   inequality; full pair lists may have sizes `12,13,16,20`, or less after a
   prescribed-bank filter.
2. **Alternating-path/cycle cleanup.**  First choose a perfect/injective matching
   from individual repeat occurrences to target labels **after** filtering
   facet equalities, all unary centre/external endpoint guards, and bank
   membership.  Only then is a pair centre bad precisely when its two matched
   deletion labels coincide.  An alternating cycle, or an alternating path
   ending at an unused target when the target universe has slack, is a valid
   absorber when toggling it repairs the named bad centre and creates no new
   bad centre.  An unused-target path must be a correctly oriented alternating
   reassignment path whose toggle preserves saturation of every repeat
   occurrence.  If every bad centre has a nonempty list of such absorbers of
   size at least twice their complete support-conflict degree, Haxell selects
   disjoint linkages and all toggles compose.  Linkage vertices are
   part-labelled copies `(centre,linkage)`; copies of the same physical
   linkage in different lists conflict through their common support.

The second formulation preserves the physical path because it changes only
deletion labels.  It is the clean serial-absorber target after the repeat
port-Hamilton factor is fixed.

There is a useful explicit load corollary for the direct option formulation.
For a target `T` and a group `i`, let `rho(T,i)` be the number of options in
all groups other than `i` that contain `T`, and put

\[
                         \rho=\max_{T,i}\rho(T,i).       \tag{6.12}
\]

Every option contains at most two targets, so its conflict degree is at most
`2 rho`.  Hence the guarded grouped SDR exists whenever every group list has
size at least

\[
                         \max\{1,4\rho\}.               \tag{6.13}
\]

This follows directly from the independent-transversal theorem.  It is only
a sufficient condition.  In particular the raw singleton lower bound four
would require `rho<=1`; no such load bound has been proved for the K17
factor.

## 7. What C6 and diamonds can and cannot do

On the bounded `4/5` face, after fixing its two boundary `BU` edges, a length-four packet has a
two-edge `UU` core.  Replacing that core by another two-edge path with the
same collars is a Johnson-diamond move.  A length-five packet has a
three-edge `UU` core, the natural location for one phase of an incidence
`C6`.

This is an interface description, not an automatic construction.

* A diamond is usable only after its owner transition and repeated-lower
  payload are fixed; adjacent diamonds can share literal source letters.
* A `C6` has zero lower/upper marginal displacement only when the opposite
  physical phase is native.  Labelled head/tail roles, rank-five payload,
  rank-nine turns and the quotient graphic state are additional rows.
* Serial `C6` telescoping gives one packet only when consecutive ports are
  identified exactly, nonconsecutive interiors are disjoint, every
  cross-junction rank-eight/rank-nine occurrence is fresh, and the composed
  endpoint action is the declared one.

More generally, at the unique-provider stage a role-closed C6 is useful only
when its two phases preserve the lower/q8 provider banks and the required
owner-degree vector while changing the central-turn or graphic state.  Such
a degree-neutral toggle leaves the repeat deficit (5.3) unchanged and may
simultaneously break a provider cycle and remove turn collisions.  If it
changes owner degrees, the repeat f-factor must be recomputed jointly.

Thus a closed diamond/hex is an exchange actuator **inside** Theorems 3.1 or
6.1.  It cannot be applied after freezing only a lower-to-upper provider
matching.  The current supported-edge catalogue proves on-edge and
local-wedge availability, but it contains no complete bank of native
opposite phases with these packet guards.  After topology is fixed, the
deletion-label alternating cycles of Theorem 6.3 are a separate absorber
language: they alter source labels only and therefore preserve the owner
path automatically.

## 8. Smallest exact residual master

The live relaxed master is naturally separated into three exact stages.

**Stage A: jointly chosen direct bank and clean unique-provider forest.**
Choose the exceptional direct incidences and all `8164` residual providers
with one lower service per row, q8 capacity one, old/unused owner capacities,
boundary and central h9 capacity one, compatible wedges at every degree-two
unused owner, and graphic independence after adjoining the base.  The two
displayed direct banks are raw full-factor UNSAT, while the fixed capacity
checkpoint has defects (5.5)--(5.6); neither is a feasible Stage-A output.

**Stage B: repeat port-Hamilton factor.**  Given a clean Stage-A forest,
select `1879` zero-degree owners and `4534` repeat edges with the exact
degrees, q8/h9 rows and graphic condition of Theorem 6.1.

**Stage C: grouped deletion SDR.**  On a topology with the diamond
decomposition (6.6), reject every equal-facet join, compile the raw twenty
centre pairs with their two external endpoint guards and any prescribed-bank
filter, and select one surviving pair option at every new centre.  Select one
surviving label at every singleton repeat, with global target capacity one.
Use direct grouped selection or alternating-cycle absorbers as in Theorem
6.3.

An exact monolithic model may combine these stages.  Separating them is
sound only when Stage A exports its literal degrees/palettes and Stage B
exports its final adjacency groups to Stage C.

The older bounded-length sufficient face instead has one Boolean per fully
materialized oriented length-four or length-five packet.  Its rows are:

1. select exactly `2637` and `430` packets of the two lengths;
2. capacity one on exposed `F_0` ports and internal owners, with exactly two
   unconsumed old ports;
3. cover all `8164` remaining lower colours by designated packet edges;
4. capacity one on every residual rank-eight and rank-nine colour, avoiding
   the charged `4212/1144` banks;
5. impose the exact packet-length counts; and
6. add lazy graphic cycle cuts on the `3068`-vertex component quotient.

Once packet simplicity is built into each column, no owner-level subtour
system is needed: the quotient graphic row is exact by Theorem 3.1.

The residual marginal projection has `8164` rows, `11906` rank-eight
resources and `242771` incidences, with matching rank `8164`.  This is a
necessary positive check only.  It supplies none of rows 1--2, 4--6.

## 9. Common-bank scope

The adjacent-cut tail still has the exact first-three-layer complement
sizes

\[
\begin{aligned}
 12168-9631&=2537,\\
 24310-(3640+13270)&=7400,\\
 24310-16909&=7401.
\end{aligned}                                         \tag{9.1}
\]

Their **actual sets** depend on the provider repair and repeat factor.  A
clean unique-provider core fixes `3640+572+8164=12376` tail rank-eight
colours and `4209+5511=9720` tail turns; the repeat factor supplies the other
`4534/7189`.  The prefix, higher upper shadows, residence, and common-cap
compiler must therefore be co-designed with or after the tail selection.

Unlike the half-rotation seed, the adjacent-cut seed inherits only a
`3640`-element width-two bank and no internal width-three turns.  All
`16909` tail turns, and every higher window crossing or lying in a long ear,
must be regenerated.  The theorem does not assert an all-width bank.

## 10. Frozen evidence

The independent replay used here is

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
scratch/independent_k17_gk_shift1_exceptional_bb_replay_20260731.audit.json
scratch/independent_k17_gk_shift1_exceptional_bb_solver_20260731.audit.json
scratch/audit_ad_k17_gk_shift1_forced_direct_residual_20260731.py
scratch/ad_k17_gk_shift1_forced_direct_residual_20260731.audit.json
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json
scratch/audit_ad_k17_gk_shift1_residual_cap_topology_20260731.py
scratch/ad_k17_gk_shift1_residual_cap_topology_20260731.audit.json
scratch/audit_ad_k17_boolean_diamond_guarded_sdr_20260731.py
scratch/ad_k17_boolean_diamond_guarded_sdr_20260731.audit.json
```

The first AD audit is dependency-free and independently reconstructs the
seed components, the direct-ear quotient matching, and all arithmetic
identities in Sections 2 and 4.  The second independently finds the four
saturated provider cycles and authenticates the exact port-Hamilton deficit.
The third enumerates the guarded Boolean-diamond list sizes and equal-facet
obstruction.  None repairs the provider core or solves the repeat factor.
