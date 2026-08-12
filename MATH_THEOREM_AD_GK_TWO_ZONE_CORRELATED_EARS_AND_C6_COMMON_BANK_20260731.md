# Correlated GK ears: exact common-bank accounting, the endpoint-free tax, and the C6 zero-flux interface

Date: 2026-07-31  
Lane: AD  
Status: exact all-parameter ear accounting and splice criterion; exact
`k=17` obstruction to the advertised `4024/905/252/42` intact-ear mix;
exact three-layer complement interface and conditional C6 corridor theorem.
No completed `k=17` chronology, prefix, upper tower, residence certificate,
or compiler is claimed.

## 0. Verdict

The authenticated two-cut Greene--Kleitman object is a very useful base
forest, but its proposed corrected ear ledger is not a feasible completion
of the intact forest.

The base has `5224` rank-seven paths.  A `j`-edge ear joining two old path
endpoints has `j-1` new rank-seven owners, `j` new rank-eight edge unions,
and `j+1` new rank-nine turns.  The available owner budget therefore forces

\[
 \sum_jx_j=5223,\qquad \sum_j(j-1)x_j=1535.             \tag{0.1}
\]

There are `674` missing rank-six colours with no original endpoint
superset.  In the intended edge-service architecture, such a colour can
occur only on an internal--internal edge of an ear.  A `j`-edge ear has only
`max(j-2,0)` such edges.  Consequently every intact edge-service completion
in this architecture must satisfy

\[
 \sum_{j\ge3}(j-2)x_j\ge674.                            \tag{0.2}
\]

For the advertised mix

\[
 (x_1,x_2,x_3,x_4)=(4024,905,252,42),                  \tag{0.3}
\]

the left side of (0.2) is only `252+2*42=336`.  Thus (0.3)
is solver-free impossible in the fixed intact GK forest.  The earlier
`252/42` split classified only the `294` colours all of whose rank-seven
supersets are unused; it did not service the other `380` endpoint-free
colours.

This obstruction does not destroy the two-zone architecture.  Equations
(0.1) imply, independently of the ear-length distribution,

\[
 \sum_j jx_j=6758,\qquad \sum_j(j+1)x_j=11981.          \tag{0.4}
\]

Hence longer ears can create the missing internal--internal service
positions without changing the exact rank-eight or rank-nine scalar
interface.  The right replacement is an occurrence-labelled, correlated
ear selection, followed by zero-flux C6 rerouting inside its common owner/
rank-eight bank.  Rank-nine turns and endpoint topology must remain in that
state; C6 resource equality alone does not close them.

## 1. General ear notation

Let `F` be a linear forest in a Johnson graph on an owner layer
`V subseteq binom(Omega,r)`.  For an edge `xy` put

\[
 L(xy)=x\cap y,\qquad U(xy)=x\cup y.                   \tag{1.1}
\]

When `x-y-z` is a nonbacktracking length-two subpath whose union has rank
`r+2`, put

\[
 W(x,y,z)=x\cup y\cup z.                               \tag{1.2}
\]

An oriented `j`-ear is a Johnson path

\[
 e=(x_0,x_1,\ldots,x_j)                                \tag{1.3}
\]

whose ends are endpoints of two distinct components of `F`, and whose
internal owners are outside `V(F)`.  The inward old neighbour at each end
is part of the oriented-ear data.  Define

\[
\begin{aligned}
 I(e)&=\{x_1,\ldots,x_{j-1}\},\\
 L(e)&=\{L(x_{i-1}x_i):1\le i\le j\},\\
 U(e)&=\{U(x_{i-1}x_i):1\le i\le j\},
\end{aligned}                                           \tag{1.4}
\]

and let `W(e)` be the `j-1` internal turns together with the two boundary
turns formed with the inward old neighbours.  Thus

\[
 |I(e)|=j-1,\quad |L(e)|=|U(e)|=j,\quad |W(e)|=j+1,     \tag{1.5}
\]

provided the displayed resources are individually distinct.  Distinctness
between different ears is a separate selection constraint.

## 2. Ear accounting and the endpoint-free tax

### Theorem 2.1 (length-invariant ear ledger)

Suppose `F` has `c` components and a family of `c-1` ears has exactly `I`
internal-owner occurrences (in particular, `I` distinct new owners when the
ears are owner-disjoint).  If `x_j` is the number of `j`-edge ears, then

\[
\begin{aligned}
 \sum_jx_j&=c-1,\\
 \sum_j(j-1)x_j&=I,\\
 \sum_jjx_j&=c-1+I,\\
 \sum_j(j+1)x_j&=2(c-1)+I.                             \tag{2.1}
\end{aligned}
\]

In particular the total numbers of new edge and turn **occurrences** depend
only on `(c,I)`, not on the ear-length distribution.  They become counts of
distinct resource colours only after the injectivity rows of Theorem 3.1.

#### Proof

The first equation is the number of joins.  Sum the first identity in
(1.5) to obtain the second.  Adding the first equation once and twice to
the second gives the last two equations. `square`

### Theorem 2.2 (endpoint-free service inequality)

Let `S` be a set of lower edge colours absent from `F`, and suppose no
member of `S` is contained in an original endpoint of `F`.  If the selected
ears cover every member of `S`, then

\[
 \sum_{j\ge3}(j-2)x_j\ge |S|.                          \tag{2.2}
\]

Equivalently, if `b=sum_(j>=2)x_j` is the number of non-direct ears, then

\[
 b\le I-|S|,\qquad x_1\ge(c-1)-(I-|S|).               \tag{2.3}
\]

#### Proof

If an edge has lower colour `s`, both of its owner endpoints contain `s`.
For `s in S` neither endpoint can be an original endpoint of `F`; the edge
must therefore lie between two internal ear owners.  A `j`-edge ear has
exactly `max(j-2,0)` internal--internal edge positions, and one position has
only one lower colour.  This proves (2.2).  Moreover

\[
 \sum_{j\ge3}(j-2)x_j
   =\sum_j(j-1)x_j-\sum_{j\ge2}x_j=I-b,
\]

which gives (2.3). `square`

For the authenticated `k=17` forest,

\[
 c=5224,\qquad I=1535,\qquad |S|=674.                  \tag{2.4}
\]

Thus every intact edge-service completion in this architecture has at most
`861` non-direct ears and at least

\[
                         x_1\ge4362                    \tag{2.5}
\]

direct ears.  The scalar extremal example

\[
 (x_1,x_2,x_3)=(4362,187,674)                          \tag{2.6}
\]

satisfies the counts, but is not a local construction: exact freshness
enumeration finds only `266` of the `674` rows with a clean three-ear,
another `128` first with a clean four-ear, and `280` unresolved even at
length four.  Longer ears, ears serving multiple rows, or cuts exposing
base internals are therefore mandatory.

### Theorem 2.3 (cut-and-reroute endpoint bound)

Cut `s` old base edges, exposing at most `2s` new endpoint slots, and let
the reroute use `x_j` new `j`-edge ears.  With `S` as in Theorem 2.2,

\[
 \sum_{j\ge3}(j-2)x_j+2s\ge |S|.                      \tag{2.7}
\]

In particular, if the displayed short-ear pattern retains its `336`
internal--internal positions and every extra component is rejoined by an
extra direct ear, then

\[
                         s\ge {674-336\over2}=169.      \tag{2.8}
\]

#### Proof

An `S`-coloured edge either is internal--internal in a new ear or touches a
newly exposed old endpoint: by definition it cannot touch an original
endpoint.  The first class has the capacity in Theorem 2.2.  Each cut
exposes at most two new endpoints, and endpoint capacity permits at most one
new incident ear edge at each.  This proves (2.7), and (2.8) follows.
`square`

For `s` pairwise vertex-disjoint internal cuts the scalar lower/common-bank
ledger telescopes exactly.  The retained base has `10152-s` distinct
geometric rank-six colours, so the ear system must introduce `2224+s`
missing colours.  It has `6758+s` new edges, leaving

\[
                    (6758+s)-(2224+s)=4534             \tag{2.9}
\]

repeated geometric colours and therefore the same rank-five payload demand
as before.  Such cuts destroy exactly `2s` old turns, while the `s` extra
direct joins create `2s` boundary turns.  This is only a scalar telescope:
the actual lost and gained colour sets must still match.  No matching of
the `380` potentially exposable rows to cut endpoints is asserted here.

## 3. Exact literal splice criterion

### Theorem 3.1 (rainbow ear-splice theorem)

Let `F` have `c` nontrivial path components and assume its `U`- and
`W`-occurrence maps are injective.  A family `E` of `c-1`
oriented ears turns `F` into one literal owner path with the asserted lower,
upper and turn resources if and only if all of the following hold.

1. Every ear joins endpoints of two distinct base components.
2. Every original endpoint and every internal owner is used at most once.
3. The component multigraph induced by the ears is connected.
4. Every edge and every internal or boundary triple represented in `W(e)`
   is Johnson-legal and has the declared rank.
5. The required lower colours are covered by `union_e L(e)`.
6. Occurrences are injective inside every ear,
   `|U(e)|=j` and `|W(e)|=j+1`; moreover the sets `U(F),U(e)` are pairwise
   disjoint, and the sets `W(F),W(e)` are pairwise disjoint.

Under rows 1--3 the component multigraph is automatically a path: it has
`c` vertices and `c-1` edges, is connected, and has maximum degree two.
The two unused original endpoints are the endpoints of the final path.

#### Proof

Rows 1--2 splice literal paths without repeating an owner.  The component
multigraph has maximum degree two because each base component has two
endpoints.  Row 3 and `|E|=c-1` make it a tree, hence a path.  Concatenating
the oriented base paths and ears gives the literal chronology.  Its new
edges and new length-two subpaths are exactly (1.4)--(1.5), proving rows
4--6 sufficient for a rank-eight/rank-nine-injective splice.  Conversely,
cutting any such final path at the selected ear edges recovers rows 1--3,
and its occurrence trace gives rows 4--6. `square`

This theorem requires only coverage, not injectivity, of lower colours.
That distinction is essential here: the `6758` new ear edges service only
`2224` rank-six colours missing from the base.  Rank-eight unions and
rank-nine turns, by contrast, must be fresh for the advertised two-zone
partition.

### Lemma 3.2 (rank-five payload Hall projection)

Under the proposal's designated rank-five payload regime, let `m_D` be the
multiplicity of a geometric rank-six intersection `D` in the final owner
path.  **Assume** one occurrence is assigned the rank-six lower target `D`
and every other occurrence is required to carry a distinct rank-five
target.  (A genuinely nonflat compiler could instead use a smaller subset
and lies outside this lemma.)  Fix an
allowed internal-tail bank `B_5` after reserving the `1652` prefix and two
boundary rank-five targets.  The allowed choices below `D` are

\[
 B_5\cap\partial_5D,
 \qquad \partial_5D={S\in{\Omega\choose5}:S\subset D}.  \tag{3.1}
\]

Ignoring the compatibility of neighbouring source letters, such a distinct
payload assignment exists if and only if

\[
 \sum_{D\in X}(m_D-1)
       \le \left|B_5\cap\bigcup_{D\in X}\partial_5D\right| \tag{3.2}
\]

for every family `X` of geometric rank-six colours.

For every matched pair `S=D-g` and every oriented pair of owners, with
distinct `x,y` outside `D`,

\[
                         A=D+x,\qquad B=D+y,            \tag{3.3}
\]

there are exactly `5*4=20` witnesses in the canonical
rank-four-intersection subfamily.  Namely, for ordered distinct `a,b in S`,
put

\[
                 R=D-b+x,\qquad T=D-a+y.               \tag{3.4}
\]

Then

\[
R\cup S=A,\qquad S\cup T=B,\qquad R\cup S\cup T=D+x+y. \tag{3.5}
\]

and `R\cap T=D-\{a,b\}` has rank four.  Allowing `a=b` would give five
additional rank-five-intersection realizations; those are not counted here.

#### Proof

The payload problem is a bipartite `b`-matching from one demand node of
capacity `m_D-1` for every `D` to the allowed rank-five sets in `B_5` below
it.  The capacitated Hall theorem is exactly (3.2).  Equation (3.5) follows
by direct substitution.  Conversely, because `|R|=6` and
`R\cup S=D+x`, the set `R` must contain `g,x` and omit a unique `b in S`,
so `R=D-b+x`; similarly `T=D-a+y`.  The intersection has rank four exactly
when `a!=b`.  Since `S` has five elements, the twenty ordered distinct
choices of `a,b` exhaust the canonical subfamily. `square`

For `k=17`,

\[
 \sum_D(m_D-1)=16910-12376=4534.                       \tag{3.6}
\]

These are the proposal's `4534` internal rank-five payloads.  Two reserved
boundary rank-five targets give the advertised total `4536` only if their
two boundary occurrence rows also literalize; equivalently they are two
extra demand nodes in the joint Hall system.  Lemma 3.2 is an exact
**tail-payload projection for fixed `B_5`**, but not by itself a global
common-cap or chronology theorem.  If the prefix/boundary allocation is not
fixed first, `B_5` must be selected jointly with those rows.  Choices (3.4)
for adjacent transitions share source letters, so their simultaneous
literalization is an occurrence-labelled path CSP.  Hall alone does not
solve either joint problem.

### Lemma 3.3 (product-chain all-width protected bank)

In one two-cut product-chain component write its consecutive owners as

\[
                      L_a=(A_{a+1},B_{r-a}),            \tag{3.7}
\]

with `L_(a-1)` the next owner.  The union of `w` consecutive owners is

\[
 L_a\cup\cdots\cup L_{a-w+1}
       =(A_{a+1},B_{r-a+w-1}),                         \tag{3.8}
\]

and has rank `r+w`.  Across the complete product SCD these unions are
globally injective for each fixed `w`.

#### Proof

Nestedness of the two segment chains gives (3.8).  Its first-shore rank
recovers `a`; unique membership in each segment-chain decomposition then
recovers both chains and the window. `square`

For the authenticated GK forest, widths `2,...,8` therefore give protected
rank-`8,...,14` banks of exact sizes

\[
                 10152,4928,1888,564,116,17,1.          \tag{3.9}
\]

Concatenating intact components, with arbitrary reversals, preserves every
one of these internal windows.  The only obligations not inherited from an
intact GK component are windows containing a new ear edge or owner, including
both internal-ear and boundary-crossing windows.  Conversely, cutting an old
component removes only windows crossing a cut; at width `w` there are at most
`w-1` per cut.
Thus the `s\ge169` route has a bounded but nonzero protected-halo ledger and
cannot be certified from the scalar cut count alone.

## 4. The exact three-layer complement interface

The authenticated base has

\[
\begin{array}{c|r}
\text{base path components}&5224\\
\text{base rank-seven owners}&15376\\
\text{base rank-six edges / distinct rank-eight unions}&10152\\
\text{base internal distinct rank-nine turns}&4928.
\end{array}                                             \tag{4.1}
\]

There are `19448` rank-seven owners and `24310` rank-eight and rank-nine
sets in the ambient layers.

### Theorem 4.1 (two-zone complement identity)

For any ear family satisfying (0.1), assume its internal owners, rank-eight
unions and rank-nine turns are occurrence-injective and fresh against the
base.  Then the following three residual bank sizes are forced:

\[
\begin{array}{c|c|c|c}
\text{resource}&\text{base}&\text{ears}&\text{complement}\\\hline
\text{rank-seven owners}&15376&1535&2537\\
\text{rank-eight unions}&10152&6758&7400\\
\text{rank-nine turns}&4928&11981&7401.
\end{array}                                             \tag{4.2}
\]

Then a prefix can complete these three layers exactly if
and only if its `2536` separator owners plus the one seam owner, its `7400`
adjacent-pair unions, and its `7401` three-letter windows are exactly the
three set complements in (4.2).  The last family consists of `7399` windows
wholly in `P` and the two three-letter windows crossing `P|T`; it is not a
four-window prefix row.

#### Proof

The owner complement is
`19448-15376-1535=2537`.  The other two identities follow from Theorem 2.1:
`24310-10152-6758=7400` and
`24310-4928-11981=7401`.  Because every relevant family is injective,
having the displayed cardinality and being disjoint from the tail is
equivalent to being its full complement. `square`

This is the exact **common-bank interface**.  It is stronger than three
separate scalar equations: the tail selection fixes the actual three
complements that the prefix must realize.  It is not a maximal-common-cap
compiler assignment, a residence statement, or an upper-rank interval
certificate.

The rank-nine row is deliberately mixed-width.  Its `7401` prefix starts
use three letters, whereas its `16909` tail starts use four letters.  Thus

\[
 7399+2+16909=24310,                                   \tag{4.3}
\]

and no uniform four-window claim is being made.

## 5. Relation to the C6/common-cap machinery

Represent a selected Johnson transition by its geometric atom

\[
                 a=(L,U;\{s_0,s_1\}),                  \tag{5.1}
\]

where `L` is its **geometric** lower edge colour, `U` its upper edge union,
and `{s_0,s_1}` is its unlabelled owner-slot pair.  A suspended C6 has two
three-atom phases with the same multisets of these geometric resources.
The `H/T` role labelling of the owner slots and the rank-five source payload
of Lemma 3.2 are additional coordinates; neither is automatically preserved
by the geometric C6 identity.  Sockets `42` and `57` in the strict atlas are
explicit role-displacement counterexamples.

### Lemma 5.1 (C6 zero-flux rethread)

Suppose two ear realizations differ only by replacing one complete C6 phase
by the opposite phase, with all exterior slot incidences fixed, **and** the
terminal orientation has the same labelled `H/T` slot multiset as the old
phase.  Then the replacement has zero signed displacement on

1. lower edge-colour service;
2. rank-eight edge unions; and
3. labelled rank-seven owner slots.

Every turn not incident with one of the exchanged slots is unchanged.
Thus only the local rank-nine turn multiset and the decoded endpoint/root
state can change.  If the source-payload coordinate is also required to
have zero signed displacement, the exact lower target multiset is preserved
as well.

#### Proof

The geometric C6 identity proves equality of the first two coordinates and
of the unlabelled owner multiset.  The explicit role-closure hypothesis
upgrades the last equality to labelled slots, proving the first three
assertions.  A turn is determined by two consecutive atoms at one labelled
occurrence slot.  If neither incidence is exchanged, the ordered pair is
unchanged.  Contracting the unchanged exterior fragments leaves precisely
the local endpoint/root action. `square`

### Theorem 5.2 (private correlated C6 completion)

Fix an ear-spliced state satisfying the owner, lower-service and rank-eight
rows of Theorems 3.1 and 4.1.  Let `P` be a phase-disjoint bank of
**role-closed** C6 rethreads whose labelled slot supports and rooted
cross-dependencies are private.  For `p in P`, let `delta_9(p)` be its signed
rank-nine turn vector and `g(p)` its decoded endpoint action.

If a subbank `A subseteq P` satisfies

\[
 \sum_{p\in A}\delta_9(p)=\Delta_9,\qquad
 \prod_{p\in A}g(p)=g_*                              \tag{5.2}
\]

in a legal dependency order, every selected packet is individually rooted
legal, the collective rooted fundamental minor is nonsingular (equivalently
the quotient replacement is acyclic with the declared roots), and every
carried role, source-payload, anchor and protected-cap guard closes, then
activating `A` realizes the prescribed turn repair `Delta_9` and endpoint
correction `g_*` without changing the owner, geometric-rank-six-service or
rank-eight banks, and without changing the literal lower palette when the
payload displacement is zero.

In the particularly checkable single-gain case, suppose each packet is
endpoint-neutral and replaces one designated **consumable occurrence** of
an excess turn by one missing turn.  Require capacity one on those loss
occurrences (or, equivalently, that every sacrificed colour retains its
required residual load).  If the resulting bipartite graph
`missing turn -- (private packet,loss occurrence)` satisfies Hall, a
matching saturating the missing turns gives such a completion.

#### Proof

Lemma 5.1 makes the first three resource coordinates identically zero and
makes signed turn displacements additive on a private bank.  Rooted
privacy gives the stated legal composition order, while endpoint actions
compose as permutations.  This proves the first assertion.  In the
single-gain case, the expanded Hall matching chooses pairwise private
packets with distinct gained targets and capacity-feasible sacrificed
occurrences, so their sum is the required repair. `square`

### Lemma 5.3 (serial C6 telescope)

Let `P_1,...,P_t` be legal C6 path fragments with distinct exterior ports
such that the output labelled port of `P_i` is the input labelled port of
`P_(i+1)`, with compatible in/out roles.  Suppose two fragments intersect
only when consecutive and then exactly in that prescribed common port;
consecutive port signatures cancel.  Require every cross-junction protected
window to be legal and fresh against the retained base and every other new
window, in addition to internal rank-eight/all-width freshness.
Then their concatenation is one legal serial ear with only the input of
`P_1` and output of `P_t` exposed.  Its signed resource vector is the sum of
the fragment vectors and its endpoint action is the ordered product of the
fragment actions.

#### Proof

Identify each consecutive output/input port.  The local incidence equations
cancel at every identified port, leaving degree one only at the two exterior
ports and degree two elsewhere.  The exact intersection hypothesis forbids
a nonconsecutive repeat or closed cycle, so the union is a path.  Resource
incidence is additive, while endpoint decoders compose under concatenation.
The internal and cross-junction palette hypotheses give the claimed fresh
union windows. `square`

This is the natural variable-length/shared-colour replacement for (0.3): a
long serial ear amortizes its two base endpoints over many
internal--internal rank-six service edges.  The current finite catalogue
contains locally clean on-fragments only; it has no planted off phases or
authenticated boundary signatures with which to instantiate Lemma 5.3.
Moreover every role-closed full C6 fragment has even endpoint action
(identity or a 3-cycle on its local support).  A serial word of these
fragments can realize only an even decoded endpoint action; an odd target
requires a parity-changing non-C6 actuator.

The theorem is a reusable correlated-completion mechanism, not an existence
proof for this GK fixture.  The strict direct-chain atlas independently
shows why the guard hypothesis cannot be omitted: raw C6 banks can be large
while terminal nativity, role alignment and rooted closure leave no usable
two-shore bank.  Conversely that strict-side no-go does not apply directly
to the new GK owner host; a GK-specific C6 column atlas must be built after
the ear state is chosen.

For a completely static two-zone partition, pair every **role- and
payload-closed** tail C6 packet with a prefix rethread whose complete signed
`(rank7,rank8,rank9)` vector is `(0,0,-delta_9)`.  Such a pair has zero flux
on all three rows of (4.2).  A private rooted-compatible bank of these paired corridors can be
activated without changing the common-bank interface provided all
cross-junction protected-window and cap guards also pass.  Existence of a
positive-density paired bank with those guards is the precise all-parameter
socket theorem still missing.

## 6. Compact exact intact-forest master and current boundary

The exact intact-forest master has one Boolean variable per oriented ear
column.  A column records

* two old component endpoints and `j-1` internal rank-seven owners;
* its `j` lower edge colours and `j` rank-eight unions;
* its `j+1` rank-nine turns; and
* its component-pair edge and endpoint orientation.

The rows are:

1. exactly `5223` ears and exactly `1535` internal owners;
2. endpoint and internal-owner capacity one;
3. all `2224` missing rank-six colours covered;
4. rank-eight and rank-nine capacity one, avoiding the base palettes;
5. connected component graph (then automatically one path); and
6. the actual prefix complement rows of Theorem 4.1.

The first valid separation order is (2.2), then local candidate existence,
then owner/rank-eight/rank-nine packing, then graphic cuts, and only then the
prefix, long upper intervals, residence and compiler.  The frozen source
does not contain the complete long-ear column catalogue, so no SAT/UNSAT
claim is made for this master.

The first local exact profile is

\[
\begin{array}{c|r}
\text{missing rank-six colours}&2224\\
\text{no original endpoint superset}&674\\
\text{all rank-seven supersets unused}&294\\
\text{clean three-ear among the 674}&266\\
\text{additional clean four-ear}&128\\
\text{unresolved through length four}&280.
\end{array}                                             \tag{6.1}
\]

The `294` all-unused subfamily splits `252+42` at lengths three/four.  That
subfamily split is valid, but it cannot be promoted to the global ear mix
(0.3).

## 7. Reproducibility and scope

The authenticated inputs are

```text
PROPOSED_K17_TWO_ZONE_GK_EAR_CONSTRUCTION_20260731.md
MATH_AUDIT_K17_TWO_ZONE_GK_FOREST_20260731.md
scratch/audit_k17_two_zone_gk_forest_20260731.py
scratch/k17_two_zone_gk_forest_20260731.audit.json
scratch/audit_ad_gk_two_zone_correlated_ears_20260731.py
scratch/ad_gk_two_zone_correlated_ears_20260731.audit.json
```

The companion AD audit authenticates hashes, independently replays all
scalar identities and the endpoint-free inequality, and records the exact
scope.  The proposed mix (0.3) remains useful only as a corrected count for
the `294` all-unused local rows; it is refuted as a global intact-forest
schedule.

The older `threadD_k17_two_zone_ear_provider_gate` and uniform-prefix-scope
artifacts were built against superseded core SHA `c30899b8...`.  Their
`674/294` empty-provider counts survive in the new reconstruction, but their
short-ear feasibility and uniform-four-window language are not used here.

Nothing here proves a length-`24313` word.  In particular, rank-ten through
rank-seventeen interval coverage, residence, literal low-cell allocation,
the prefix alternating path, and the generalized compiler remain separate
gates.
