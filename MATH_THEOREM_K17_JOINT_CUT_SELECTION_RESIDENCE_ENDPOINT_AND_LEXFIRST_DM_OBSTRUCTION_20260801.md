# Joint cut selection is the exact `k=17` residence/endpoint gate

**Date:** 2026-08-01  
**Status:** unconditional structural theorem and exact scoped obstruction for
the authenticated protected factor.  The theorem corrects the sequential
strategy “choose the deterministic rightmost-greedy minimum residence cut, then
match its endpoints.”  It does **not** rule out another minimum cut, a
nonminimum cut, an interior rethread, or a compound seam gadget, and it does
not construct a `k=17` word.

## 0. Authenticated input and corrected conclusion

Let `F` be the projected owner two-factor obtained from

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

It is lower-`q1` rainbow, immediate-upper complete, has seven owner cycles,
and contains the protected reset/twin-bank incidences.  Its short positive
runs have exact protected-avoiding circular transversal number

\[
                              \tau(F)=3807.                 \tag{0.1}
\]

Two audits of one deterministic rightmost-greedy optimum `D_lex` initially
appear to point in opposite directions:

* the raw endpoint atlas has `28,395` unordered seams, equivalently `56,790`
  directed atoms, and its `795` rigid singleton demands form a
  resource-conflict-free forest;
* after a deliberately relaxed **necessary** residence screen, `1,289` cut
  colours have no seam and `368` physical blocks have no outgoing or incoming
  seam.

There is no contradiction.  The `795` forest is a raw, pre-residence object.
In fact its `281` unique-lower members are incumbent cut edges, and minimum
cut edges cannot be reinserted in any resident atomic reassembly.  The
correct construction chooses the cut and the replacement seams jointly.

## 1. Canonical symmetric-difference normal form

Write an old projected edge as `e=TT'` and put

\[
 \kappa(e)=T\cap T'\in {[17]\choose8},\qquad
 \rho(e)=T\cup T'\in {[17]\choose10}.                    \tag{1.1}
\]

Because `F` is lower-rainbow, for every rank-eight colour `K` there is one
old edge `e_K` with `kappa(e_K)=K`.

Let `H` be any Johnson Hamilton path on the same rank-nine owner set and
define canonically

\[
 D=E(F)\setminus E(H),\qquad A=E(H)\setminus E(F).       \tag{1.2}
\]

Thus an old edge which is cut and then reinserted is cancelled before `D`
and `A` are recorded.

### Theorem 1.1 (exact lower-palette and degree equations)

The path `H=F-D+A` uses every old lower colour exactly once except for one
boundary colour `K_*` if and only if, for every rank-eight colour `K`,

\[
 \boxed{
 \mathbf 1_{e_K\in D}
 =\mathbf 1_{K=K_*}+|\{a\in A:\kappa(a)=K\}|}             \tag{1.3}
\]

Moreover, `H` has degree two at every internal owner and degree one at its
two endpoints if and only if

\[
 \boxed{
 \deg_A(v)-\deg_D(v)
 =-\mathbf 1_{\{v\text{ is an endpoint of }H\}}}           \tag{1.4}
\]

for every owner `v`.  In particular,

\[
 |A|=|D|-1,                                               \tag{1.5}
\]

every new seam has a distinct deleted lower colour, no uncut lower colour
can be reused, and `K_*` is deleted but is not the colour of a new seam.

#### Proof

The multiplicity of `K` in `H` is

\[
 1-\mathbf 1_{e_K\in D}+|\{a\in A:\kappa(a)=K\}|.
\]

Equating this with `1-\mathbf 1_{K=K_*}` gives (1.3).  At an owner `v`, subtracting
the old degree two from the desired path degree gives (1.4).  Summing (1.3)
over `K`, or summing (1.4) over owners and dividing by two, gives (1.5).
\(\square\)

### Theorem 1.2 (exact immediate-upper equation)

Let `m_R(F)` be the number of old edges with union `R`.  The immediate-upper
palette of `H` is complete if and only if

\[
 \boxed{
 m_R(F)-|D\cap\rho^{-1}(R)|+|A\cap\rho^{-1}(R)|\ge1}
                                                               \tag{1.6}
\]

for every rank-ten target `R`.

#### Proof

Only the deleted old adjacencies and added new adjacencies change the
adjacent-union multiset.  Formula (1.6) is its literal multiplicity.
\(\square\)

## 2. Residence forces cut/endpoint correlation

For an old maximal positive coordinate run of length at most three, let its
**closed collar** be the entering gap, every internal gap, and the leaving
gap.  Let `P` be the protected old gap set.  Here `C` denotes the
pre-cancellation set of old edges cut to form atomic blocks; `D` retains the
canonical symmetric-difference meaning from (1.2).

Any resident interior-preserving candidate satisfies

\[
 C\cap P=\varnothing,\qquad C\cap I\ne\varnothing
       \quad\text{for every old short-run collar }I.          \tag{2.1}
\]

These rows are necessary, but new seams can create new short runs, so they
are not sufficient.

### Lemma 2.1 (private-run incumbent exclusion)

If `C` is an inclusion-minimal transversal of the short-run collars, then
no edge of `C` can be reinserted as a seam in a resident
interior-preserving reassembly.  Consequently its canonical deleted set is
`D=C`.

#### Proof

For each `e in C`, inclusion minimality gives a private collar `I_e` with
`I_e intersection C={e}`.  Every other old adjacency in `I_e` remains inside
one of the cut path blocks.  Reusing the incumbent endpoint pair `e`
therefore restores the complete old word

\[
                         0\,1^j\,0\qquad(1\le j\le3),         \tag{2.2}
\]

or its reversal.  This is an internal forbidden run, independently of the
orientations of the two blocks.  Hence `e` cannot be a new resident seam.
Every old edge outside `C` remains internal to a retained block, while every
edge in `C` remains absent, so canonical cancellation gives `D=C`.
\(\square\)

Every cardinality-minimum transversal is inclusion-minimal.  Consequently
an exact minimum-cut endpoint atlas must discard all incumbent seams before
any Hall claim is made.  This private-collar conclusion is not asserted for
redundant extra cuts, which need not have private collars.

## 3. Exact joint cut-selection theorem

For an inclusion-minimal protected cut set `C` satisfying (2.1), let `B(C)`
be the path blocks of `F-C`, let `K(C)={kappa(e):e in C}`, and give every block its two
orientations.  A directed seam atom joins the last owner of one oriented
block to the first owner of a distinct oriented block by a nonold Johnson
edge `a` satisfying `kappa(a) in K(C)`.  Lemma 2.1 identifies `C` with the
canonical `D` in (1.2).

For each coordinate, summarize an oriented block by the finite automaton for
the language

\[
 \mathcal L_4=\{w:\text{no factor }0\,1^j\,0
                         \text{ occurs for }1\le j\le3\}.      \tag{3.1}
\]

The product of the seventeen summaries is associative and is exact; an
all-one block may transport an unfinished run across more than one seam,
which is why pairwise seam tests are not sufficient.

### Theorem 3.1 (joint cut, endpoint, palette, and residence criterion)

There is an atomic Hamilton owner path obtained from an inclusion-minimal
cut transversal which is interior-preserving, positive-run-resident, retains
every protected old edge, is lower-`q1` exact modulo one named boundary
colour, and is immediate-upper complete if and only if there exist,
**jointly**,

1. an inclusion-minimal protected cut set `C` satisfying (2.1);
2. one orientation of every block of `B(C)`;
3. a set `A` of nonold directed endpoint seams;
4. two path endpoints and one omitted colour `K_*`;

such that:

* the literal lower and owner-degree equations (1.3)--(1.4) hold;
* `F-D+A` is connected and acyclic;
* every immediate-upper row (1.6) holds; and
* the block order induced by `F-D+A` has an accepting product in all
  seventeen copies of the automaton (3.1).

#### Proof

Given a path, take its pre-cancellation cut set `C`.  Lemma 2.1 identifies
it with canonical `D`; protection, (2.1), Theorems 1.1--1.2, graphic
connectivity, and automaton acceptance are all necessary.

Conversely, (1.4) and the graphic rows make `F-D+A` one spanning path.
Equation (1.3) gives the claimed lower palette, (1.6) gives the upper
palette, and the product automaton gives positive-run residence.  Since `C`
avoids the protected edges, every protected old edge remains inside a
retained block.  A typed reset phase or rooted predecessor state requires
additional orientation/state pins; undirected retention alone does not
supply it.
\(\square\)

The automaton here controls internal positive runs of the owner chronology.
Clipped source collars, signed/dual residence, and literal `D^3` replay are
not silently included.  Rank ten is edge-additive; ranks eleven and higher
instead require the complete ordered suffix/full-block/prefix occurrence
universe, equivalently an accumulated-union block automaton.  The terminal
common-cap compiler adds one occurrence-labelled matching after physical
replay.  None of those rows follows from Theorem 3.1.

## 4. A cutwise DM lower bound for ordinary seams

For a fixed `D`, let `E_rel(D)` be the directed atoms surviving the relaxed
necessary two-block residence predicate: when neither incident block is
all-one in a coordinate, the joined suffix/prefix run must already have
length at least four; if either block is all-one, impose no condition.
Every seam of an exact resident atomic reassembly lies in `E_rel(D)`.

Project `E_rel(D)` onto the three bipartite graphs

\[
 T\!H(D),\qquad T\!K(D),\qquad K\!H(D),                    \tag{4.1}
\]

between physical tail blocks, head blocks, and deleted colours.  Write their
matching numbers as `nu_TH(D),nu_TK(D),nu_KH(D)` and put `C=|D|`.

### Theorem 4.1 (external-service lower bound)

Suppose at least `C-1-b` of the required linear join slots are ordinary
seam triples in `E_rel(D)`, while the remaining `b` triple slots are supplied
outside that atlas.  Then

\[
 \boxed{
 b\ge\delta_{\rm lin}(D):=
 \max_{Q\in\{TH,TK,KH\}}(C-1-\nu_Q(D))_+.}               \tag{4.2}
\]

For a cyclic reassembly the corresponding bound is

\[
 \boxed{
 b\ge\delta_{\rm cyc}(D):=
 \max_{Q\in\{TH,TK,KH\}}(C-\nu_Q(D))_+.}                 \tag{4.3}
\]

Equivalently, an all-ordinary linear solution requires every Hall
deficiency in each projection to be at most one; an all-ordinary cyclic
solution requires zero deficiency.

#### Proof

The ordinary seams of a path induce matchings of size at least `C-1-b` in
all three projections: a selected ordinary seam uses one tail, one head,
and one deleted colour.  No projection can contain a matching larger than
its matching number.  Rearranging gives (4.2); the cyclic proof is the same
with `C` selected joins.  \(\square\)

This is a necessary projection theorem, not a three-dimensional matching
sufficiency claim.  The number `b` counts missing ordinary triple slots, not
physical gadgets: one compound gadget may discharge several such slots.
Even when (4.2) vanishes,
orientation sharing, graphic connectivity, upper coverage, and the exact
automata remain.

## 5. Reconciliation of the two deterministic emitted-cut audits

Both audits use the same deterministic rightmost-greedy protected-gap-
avoiding minimum cut, denoted `D_lex` in the retained artifacts.

### Stage 1: raw resources

There are

\[
 28,395\text{ unordered endpoint pairs}
 =56,790\text{ directed atoms}.                            \tag{5.1}
\]

Every raw two-shore projection has a perfect matching.  The `560`
unique restorers of cut-killed rank-ten colours and the `281` raw
degree-one lower-colour seams have union size

\[
                         560+281-46=795.                      \tag{5.2}
\]

That union has no endpoint, lower-colour, block-degree, or graphic conflict.
This is a true **raw** statement.

### Stage 2: canonical cancellation and private collars

Exactly `3,807` of the unordered pairs are incumbent old edges.  Lemma 2.1
removes them, leaving

\[
 24,588\text{ unordered nonincumbent pairs}
 =49,176\text{ directed atoms}.                            \tag{5.3}
\]

Already `282` cut colours have no nonincumbent pair.  All `281` unique-lower
members of (5.2) are incumbent-only, so the raw `795` forest cannot be
contracted as a resident forced forest.  The `46` overlaps in (5.2) are
also sole raw restorers of `46` killed rank-ten colours, proving that those
upper rows require nonordinary service on this cut.

### Stage 3: necessary residence correlation

The relaxed necessary residence atlas contains `13,174` directed atoms and
has

\[
\begin{array}{c|r}
\text{zero cut colours}&1289\\
\text{dead outgoing physical blocks}&368\\
\text{dead incoming physical blocks}&368\\
\nu_{TK}=\nu_{KH}&2518\\
\nu_{TH}&3364.
\end{array}                                                \tag{5.4}
\]

The `1,289` zero-colour vertices themselves form a Hall/DM witness and
exactly exhaust the `TK` and `KH` deficiencies.  The tail--head deficiency
is `443`: its `368` singleton-dead blocks account for 368 units, while 75
further units are genuinely nonsingleton Hall correlation.

By Theorem 4.1,

\[
 \delta_{\rm lin}(D_{\rm lex})
 =\max(3806-2518,3806-3364)=1288,                        \tag{5.5}
\]

and

\[
 \delta_{\rm cyc}(D_{\rm lex})=1289.                    \tag{5.6}
\]

Thus one linear boundary omission saves at most one unit: the fixed
deterministic rightmost-greedy emitted minimum decomposition still has at
least `1,288` deficient
ordinary join obligations before exact automata, deeper shadows, or the
compiler are considered.  This is not a lower bound of `1,288` physical
gadgets.

## 6. Three scoped faces and the support-two closure

The following exact results concern different hosts or different resource
projections and therefore must not be merged into one invariant.

### 6.1 The canonical SCD `6281` face

The right-end-greedy minimum split of the authenticated SCD forest uses
`1419` cuts and produces `6281` maximal-source-factorable resident pieces.
Its complete oriented two-piece graph has `10,022,670` legal arcs.  Of the
`1419` cut-killed rank-ten colours, `1097` have a provider and `322` have
none.  If a longer interval had one of those rank-ten unions, every crossed
pair of distinct rank-nine owners would already have that same union.
Hence the `322` rows rule out upper completion of these fixed pieces under
every order and orientation.

The separate integrated seam atlas also requires a seam intersection to be
one of the currently missing lower colours.  It has `720` rank-ten zeros:

\[
                         720=322+398.                         \tag{6.1}
\]

The extra `398` targets have resident pair providers only by reusing an
already consumed lower colour.  Thus `322` is the pure fixed-piece
source/upper obstruction, while `720` belongs to the stricter exact-lower
atomic face.  Neither count applies to a different minimum split, extra
cuts, an interior rethread, or the protected twin-bank factor below.

The later SCD split audit confirms this scope constructively.  All `322`
canonical rows occur in the one-split union, and one common `192`-extra-cut
rebuild has zero upper-only rank-ten support rows.  A coupled minimum-cut
segmentation has only `19` upper-only zeros, and an `18`-extra-cut common
rebuild gives `6299` pieces with zero upper-only rank-ten support rows.  The
lower-compatible relaxed rank-ten rows remain far from closed: the latter
two segmentations have `605` and `581` zeros respectively.  These are support
theorems only: no common degree assignment, one-path topology, all-width
chronology, exact global residence, or compiler is supplied.

### 6.2 The protected-factor lex face

For the protected seven-component factor, Sections 4--5 prove only that the
fixed `D_lex` atomic face has `1289` zero lower-colour rows and the projection
defects (5.4).  The exact minimum-cut exchange walk reaches `984` zero rows,
so `1289` is demonstrably not invariant among minimum transversals.

### 6.3 Exact support-two union theorem

Starting from the same lex partition, the extra-cut audit enumerates all
`20,477` unprotected noncut internal gaps; every resulting two-subpiece
option passes its local physical viability screen.  Unary options leave
exactly `110` of the `1289` old zero-colour demands unsupported.  The
complete union atlas of

\[
 3,194,008\text{ cut-pair supports and }
 3,435,988\text{ pair--colour incidences}                    \tag{6.2}
\]

supports all `2025=1289+368+368` old singleton demands and every prospective
new-cut colour:

```text
empty_joint_demands = 0
empty_joint_colours = 0
closure_joint_dead  = 0
```

This does **not** say that two total extra cuts cure the lex face.  It says
that each singleton row has at least one, possibly different, unary or
two-cut support column in an incompatible union of menus.  It selects no
common cut bank, orientations, endpoint-disjoint seams, deleted-colour SDR,
degrees, topology, upper witnesses, exact residence product, or compiler.
In particular, the simultaneous-extra-cut lower bounds in the minimum-cut
exchange note are unaffected.

The separate dense SAT witness is subject to the same qualification when
read on its own: its unary columns are evaluated against intact base blocks,
some of which are destroyed by other selected splits.  It is prospective
support, not a seam matching.  The next subsection records the distinct
literal rebuild of its selected cut set.

### 6.4 Literal dense-refinement projection theorem

The selected `3805` extra cuts have now been rebuilt literally, independently
of the prospective support assignments.  They produce `7612` physical
pieces and `7612` distinct selected lower colours.  The relaxed necessary
residence atlas has `243,424` atoms, no zero physical piece or lower colour,
and perfect physical projections

\[
              \nu_{TH}=\nu_{TC}=\nu_{CH}=7612.               \tag{6.3}
\]

There are `187` dead oriented states on each endpoint shore, but every
unoriented physical piece retains the opposite orientation in that one role.
For exactly `187` pieces, however, incoming seams exist only in one
orientation and outgoing seams only in the opposite orientation.  Neither
orientation supports both roles.  The exact common-orientation q1 CNF is
therefore UNSAT by unit propagation.  Thus the literal rebuild closes the
old unoriented singleton and pairwise-projection obstruction but fails the
strictly stronger shared-orientation row.

The same rebuilt bank has `5094` rank-ten casualties.  Raw atoms support all
of them, whereas the relaxed necessary-residence atlas has exactly `78`
rank-ten zero-provider rows.  Any globally resident atomic chronology uses
only atoms in that relaxed atlas, and a rank-ten interval crossing a seam has
the same union on a crossed adjacent owner pair.  Hence this particular
`7612`-piece refinement is upper-incomplete under every atomic ordering.

This updates, but does not invalidate, the prospective warning above: the
literal lower/endpoint projections pass; simultaneous persistence is now
proved for this selected bank.  The prospective SAT assignments themselves
are not a seam matching, and the fixed bank is independently killed by the
`187` shared-orientation units and the `78` upper rows.

A subsequent literal cut-choice descent, still a live incumbent rather than
a terminal bank, preserves zero q1 piece/colour rows and all three perfect
unoriented projections while reducing the two exact counts to `94` and `28`.
Its combined singleton objective is therefore `122`, down from `265`.  This
does not supply common orientation, upper completion, or functional Hall; it
does prove directly that neither defect count is invariant under cut choice.

The next independently replayed cut-choice bank closes both local families:
common-orientation zeros and relaxed rank-ten zeros are each `0`, while all
three relaxed physical q1 projections remain perfect.  Bank/audit SHA prefixes
are `5b4fe2d1`/`199ab886`.

The relaxed seam atlas is an undirected physical-socket graph.  Exact q1 is
not merely nonisolation: it is a coloured perfect matching which uses every
socket and every selected lower colour exactly once; rank-ten targets label
the same edges.  Pure refinement preserves all old socket edges, supplies a
canonical edge for each new socket pair, and therefore cannot create a new
singleton zero.  It also extends any already feasible coloured matching by
those canonical edges.

For the fixed zero/zero bank the coloured matching is nevertheless UNSAT.
The verified 14-clause/five-lemma core has two degree-two colours and four
directed seams; after simultaneous-reversal quotient, both required colour
edges meet the same physical socket of the central piece.  Colour exactness
requires both and socket degree one forbids both.  This rejects only bank
`5b4fe2d1...` and supplies the next cut-CEGAR target; it is not a protected-
factor or word no-go.

The first CEGAR step is also exact.  All `240` substitutions confined to the
three visible core pieces fail; `20` retain every local zero row and remain
q1-UNSAT.  A global one-cut replacement on base piece `1268` breaks the first
bow tie while preserving zero/zero singleton support, but exposes a second
verified `15`-clause/`7`-lemma core.  Thus cut CEGAR is effective and the
obstruction stays constant-size, but termination is not proved.

### Theorem 6.1 (exact next integral theorem)

The next construction theorem is the feasibility of one **joint integral
cut/seam selector**.  Its variables must simultaneously choose

1. either one minimum collar-transversal path in every old component, or a
   priced lex-plus-extra-cut refinement;
2. the literal induced subpieces and one orientation/state for each;
3. occurrence-labelled seam atoms, including atoms activated by two chosen
   split options;
4. one source, one sink, and one named boundary lower colour;

and must impose on those same variables:

* exactly one service for every selected deleted lower colour except the
  boundary colour, including self-closure of every newly cut colour;
* tail/head capacity and owner degree equations;
* a connected acyclic contracted path;
* the rank-ten multiplicity rows and the complete ordered interval-witness
  rows at ranks eleven and higher;
* protected typed-state pins and the exact seventeen-coordinate residence
  product; and, only after literal physical replay,
* one terminal common-cap compiler matching.

For the inclusion-minimal branch, Theorem 3.1 supplies the exact criterion.
The priced extra-cut branch requires its general pre-cancellation extension:
the cut set may be redundant, selected old cut edges may be reused as seams,
and Lemma 2.1/private-collar cancellation cannot be invoked automatically.

The support-two census closes singleton nonemptiness only in its lex-rooted
union projection, and the selected literal rebuild closes all three
unoriented pairwise lower/endpoint projections.  A positive theorem must
still construct the full integral selector.  Cut choice has produced a bank
with neither shared-orientation singleton contradictions nor rank-ten
zero-provider rows, but its exact tail/head/colour matching is bow-tie UNSAT.
The next CEGAR step must change one core colour/socket incidence and rerun the
exact matching.  A global negative theorem must produce a Hall/DM/Benders
inequality valid across cut choices.

## 7. Sharp scope of the inclusion-minimal atomic theorem

The exact parameter for the inclusion-minimal-transversal, atomic,
fixed-interior face is not “the endpoint rank after the deterministic emitted
minimum cut.”  It is

\[
 \tau_{\rm join}^{\rm atom,min}(F)=
 \min\{|C|:\ C\text{ is inclusion-minimal, satisfies (2.1), and the full
 atomic joint master of Theorem 3.1 is feasible}\}.          \tag{7.1}
\]

The minimum of the empty feasible family is `+infinity`.

The present results prove

\[
             \tau_{\rm join}^{\rm atom,min}(F)\ge3807,\qquad
             D_{\rm lex}\text{ is infeasible in the atomic master}. \tag{7.2}
\]

They do **not** prove that every 3,807-cut choice fails.  To close the whole
minimum-cut face one must prove

\[
 \min_{C:\ |C|=3807,\ C\text{ satisfies (2.1)}}
       \delta_{\rm lin}(C)>0                              \tag{7.3}
\]

as one sufficient projection obstruction, or give a stronger obstruction
to the exact master.  Conversely, finding a cut with zero projected
deficiency would only open the remaining
orientation/graphic/upper/automaton rows; it would not finish them.

The proof-safe live alternatives are:

* jointly select a different minimum cut and its endpoint seams;
* pay for a nonminimum cut whose endpoint state is better;
* rethread interiors rather than keeping the cut blocks atomic; or
* use compound seam gadgets which jointly discharge the normalized
  deficient obligations from Theorem 4.1.

The parameter `tau_join^atom,min` is face-specific.  It says nothing about a
collar-redundant/priced atomic refinement, an interior rethread, or a compound
gadget which does not preserve the old block interiors.

## 8. Frozen evidence

```text
MATH_THEOREM_K17_3807_CUT_REJOIN_COLORED_FUNCTIONAL_HALL_20260801.md
  SHA256 b6ead68d850d7227da2cc4e0e0c246c97880a4d93962794e6313e32cc3d9976f

scratch/audit_k17_h2_cut_rejoin_endpoint_expansion_20260801.cpp
  SHA256 eed8f3867ee557d8211d4880fd1fd019f02543913432757d5d06c158b2612622

scratch/k17_h2_cut_rejoin_endpoint_expansion_20260801.out
  SHA256 b36c8f5526bca9038b8bf74af493ffd4bb7434c1f69697be861d8d9e979ecdf2

MATH_THEOREM_K17_H2_MINCUT_BLOCK_ENDPOINT_THREE_RESOURCE_NOGO_20260801.md
  SHA256 d858bef2a9d12e931162db69106b76ff32cac8c32b689bf58113abd40b797f93

scratch/audit_k17_h2_contracted_endpoint_hall_20260801.cpp
  SHA256 28b2349ef9a0a7de8d5623e16ed5900b45f7852fe0b14ec5f779d94cf9778498

scratch/k17_h2_contracted_endpoint_hall_20260801.out
  SHA256 1161654663b7f935feaadbfda60e3255bbcb4d2696c884331bb8b486f04a2245

MATH_AUDIT_H2_K17_M9_SCD_MULTIBLOCK_MAXSOURCE_AND_UPPER_NOGO_20260801.md
  SHA256 7ced8389379e75a7d1f208fe7a99f201479dd93a3f3cf315cf1a725925be21d5

MATH_THEOREM_K17_SCD_6281_INTEGRATED_SEAM_HALL_NOGO_20260801.md
  SHA256 3ee7dceba8b4f062f28724b94ee0a3b02f9a6d31d1b92523436671e28ff687a9

MATH_AUDIT_K17_SCD_EXTRA_SPLIT_RANK10_SUPPORT_CLOSURE_20260801.md
  SHA256 45d6499e3dac256a4eb077f1c576c6c0867de34b765f9a7c81274342f5ea9d58

MATH_AUDIT_K17_EXTRA_CUT_SINGLETON_SUPPORT_CLOSURE_SAT_20260801.md
  SHA256 587b236f8fb21e3041fda41ae11256dc766db3b994a4cf28858bb114d35fb6c5

/home/amodo/or15/work/laneL_k17_two_cut_master_20260801/run.out
  SHA256 4a0dedf3f89cf1da2ed2edc443630f3ff19517bf31c39f2b8de15abf38dacf68

scratch/k17_selected_extra_cut_literal_refinement_20260801.audit.out
  SHA256 ab5898b3b819e0e7257687d02418c66e41ccb3cfc204610c59b25abac94a5929

scratch/k17_dense_refinement_common_orientation_20260801.audit.out
  SHA256 660586ce63c1a2f2ca693f0ad9df76b44e31109e09e08f366942633aff3e5ae8

scratch/k17_dense_refinement_persistent122_bank_20260801.tsv
  SHA256 f9f7997bcdb1d65281a2877c437f23d3451849d3d725ede4fa9103be6e271d4d

scratch/k17_dense_refinement_persistent122_20260801.audit.out
  SHA256 e7bc80e4c0b50176f69576887ca8c608b874e5cf77559afe333487bf35150c01

scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
  SHA256 5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f

scratch/k17_dense_refinement_zerozero_search_audit_20260801.out
  SHA256 199ab8864d35586dd7e7c97f5131562165c63bdeb47d36b0d23e45f2b8695cef

scratch/k17_dense_zero265_q1_core_20260801.cnf
  SHA256 428296575b753910f48c76a0e74c726592da0509f32f4f226206f6812ba18aca

scratch/k17_dense_zero265_q1_dratcheck_20260801.out
  SHA256 6c8c891a1dddab4832c3a3d55efc021ddc8e8a7f9c935c505d9aea6cd1515880

scratch/k17_dense_bowtie1_repair_bank_20260801.tsv
  SHA256 423a759cd9d180a23f221d8ebc6ea388112394bb2c7b028f12fd1668f425803b

scratch/k17_dense_bowtie1_second_corecheck_20260801.out
  SHA256 1d97d08835771aceaddb27d570075f69424d28a22f19816f177b4a9fb402f65f
```

The dense-refinement theorem note is a living search ledger and is therefore
not assigned a frozen file hash here.  The literal audit outputs and incumbent
bank/core artifacts above are immutable evidence for the stated `187/78`,
`94/28`, zero/zero, and two successive q1-UNSAT cores.

The raw audit and the relaxed audit were both compiled with C++20 `-O3` and
run on H100 CPU.  No local heavy computation was used for this synthesis.
