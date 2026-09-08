# K17 `b268` recoupled DM-shore gammoid and batch-exchange obstruction

**Date:** 2026-08-02  
**Status:** proof-complete matching theorem, rebased on the strict-`def84`
recoupled supplier projection.  The two one-release probes below are exact
only at complete `6/9/4` projection level.  They are not legal replacement
batches and are not socket, common-occurrence, protection, chronology, or
compiler certificates.  No solver or root radius job was launched here.

## 1. Literal parent and scope

The authoritative transfer selection and its strict pre-recoupling table are

```text
c490cc49aef575caae9f72d478ff08320f24a3625593f2465f9b94fb7d8ce979
  .../input/def84.selected.tsv

3171bf380c3a139313f1304bb1d821810cb7402c20aa99f01ab8ccdc189854f1
  .../input/def84.table.tsv
```

under

```text
scratch/k17_b268_common_parent_selector_20260802/
  root_k17_b268_common_parent_selector_def84_release_c490cc49_019fc35b_20260802/
```

After pinned-root recoupling, the table used by the present supplier theorem
is

```text
9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3
  out/def84_force_mutable_zero_roots/final.tsv
  out/def84_force_mutable_zero_roots/supplier.table.tsv
```

Its complete projection audit is

```text
b4e3f66178efbcd4129bc8a83cb8725b613a8eb09b35bb58548a2ffd90f5dff5
  out/def84_force_mutable_zero_roots/supplier.projection.audit.json
```

and reports

```text
active heads K       16898
supplier edges       74982
matching rank        16864
deficiency              34
zero heads               20
canonical Hall shore  51 / 17
graph FNV64            a3d6b556f77db3fa
```

Thus this is not the earlier pre-recoupling deficiency-84 supplier graph.
The serial theorem must be rebased on the literal recoupled graph of
deficiency 34.

All results through Section 8 concern a static bipartite supplier graph.  A
projection edge means that the complete row-pair flag predicate is nonzero.
It does not by itself select a common physical occurrence or a chronology.

## 2. The strict `51/17` shore

Let

\[
             G=(H,U;E), \qquad |H|=K=16898,
\]

be the recoupled supplier graph.  Let `Q` be the displayed maximum-deficiency
head shore and put

\[
          B=N_G(Q),\qquad |Q|=51,\quad |B|=17,
          \qquad O=H\setminus Q.
\]

The matching rank is

\[
 \nu(G)=16864=|O|+17,
 \qquad |O|=16847.                                      \tag{2.1}
\]

### Lemma 2.1 (outside saturation)

Every maximum matching saturates all `16847` heads in `O`, matches exactly
`17` heads of `Q`, and uses all suppliers in `B` on those `Q` heads.

#### Proof

Every matching uses at most `|O|` edges incident with `O` and at most
`|B|=17` edges incident with `Q`, since every neighbour of `Q` lies in `B`.
Equality (2.1) attains the sum of these two upper bounds.  Therefore each
bound is attained separately.  \(\square\)

Let `T(G)` be the transversal matroid on the head ground set `H`: a head set
is independent when it can be matched injectively into `U`.  Lemma 2.1 gives

\[
                 r_{T(G)/O}(Q)=17.                       \tag{2.2}
\]

The base contracted nullity is therefore

\[
                 |Q|-r_{T(G)/O}(Q)=51-17=34.             \tag{2.3}
\]

The exact DM component audit is frozen at

```text
scratch/def34_release_math_20260802/
  strict_def34_dm.audit.json       1b9b7a4308472cba84d3b171eea73e2d5ced33a0e46c3190557bc2c6154b2bbc
  strict_def34_dm.components.tsv   d5ecd42fde312e7a6aa656466a4d513dbe0af33d9dccf479978d3aed55e5158e
  strict_def34_dm.members.tsv      e3b948447d9ab3c271350982393ad11a73ddeb09c78852e2c45af63af96aa7f5
```

The induced `Q/B` incidence graph has `32` connected components.  Twenty
are isolated zero-head components.  Of the other twelve, ten have gap one
and two have gap two:

```text
component 12: heads {6503,6770,8188,21087}, suppliers {6448,8183}, gap 2
component 21: heads {12948,13148,19502},     suppliers {12973},      gap 2
```

Consequently the deficiency splits exactly as

\[
       34=20\text{ zero loops}+14\text{ shared-bank units}.       \tag{2.4}
\]

In particular, removing zero heads is not the whole problem.
Here `component` means a connected component of this induced canonical Hall
shore.  No full DM-poset decomposition beyond that literal ledger is used.

### Lemma 2.2 (smallest fixed-parent local oracle)

Fix one maximum matching `M` and let `M_O` be its restriction to `O`.
Then `M_O` avoids `B`.  For every `I subseteq Q`,

\[
 I\text{ is independent in }T(G)/O
 \quad\Longleftrightarrow\quad
 I\text{ is matchable into }B\text{ in }G[Q,B].          \tag{2.5}
\]

Hence on the unchanged strict parent the contracted matroid restricted to
`Q` is the direct sum of the 32 component transversal matroids.  Its exact
rank is the sum of 32 tiny bipartite matching ranks.

#### Proof

If `I` is matched into `B`, that matching is disjoint from `M_O`, so their
union saturates `O union I`.  Conversely, every edge incident with a head in
`I subseteq Q` ends in `B`; restricting any matching of `O union I` gives a
matching of `I` into `B`.  Connected components make the last rank additive.
\(\square\)

Lemma 2.2 is valid only while the graph and outside matching footprint used
in its proof survive.  A batch may change a head or supplier outside `Q`,
invalidate an edge of `M_O`, or create a cross-component alternating path.
Then the oracle in the next section is load-bearing.

## 3. Exact no-sacrifice rank after a fixed batch

Let `X` be one fully materialized candidate batch.  It produces a fixed
successor graph

\[
                  G_X=(H_X,U;E_X).
\]

Put every head whose state, activity, or supplier incidence may change into
a mutable set `C_X`; let

\[
                  O_X=H_X\setminus C_X
\]

be the heads whose matched status is required to survive.  If an allegedly
outside head changes state, it belongs in `C_X`, not in `O_X`.

### Theorem 3.1 (contracted outside-preserving rank)

Assume `O_X` is independent in the successor transversal matroid `T_X=T(G_X)`.
For every candidate mutable-head set `C subseteq C_X`, the maximum number of
heads of `C` that can be matched while all of `O_X` remain matched is

\[
 \boxed{
 r_{O_X}(C)=r_{T_X/O_X}(C)
           =\nu\bigl(G_X[O_X\cup C,U]\bigr)-|O_X|.}       \tag{3.1}
\]

If the complete active head set is `O_X union C`, its exact deficiency is

\[
 \boxed{\delta_X=|C|-r_{O_X}(C).}                         \tag{3.2}
\]

For any candidate targeting improvement `g` over deficiency `34`, (3.2)
gives the general exact threshold

\[
                    r_{O_X}(C)=|C|-34+g.                 \tag{3.3}
\]

Let `C_0` be the base active mutable-head set for the same declared outside
set `O_X`, and put

\[
 r_0=\nu\bigl(G[O_X\cup C_0,U]\bigr)-|O_X|.              \tag{3.4}
\]

If the batch preserves the total head count and `|C|=|C_0|`, it improves
deficiency by `g` exactly when

\[
                         r_{O_X}(C)=r_0+g.                \tag{3.5}
\]

In the special case that no changed head or incidence lies outside the old
shore, `O_X=O`, `C_0=Q`, and `r_0=17`.  Otherwise enlarging the mutable set
also enlarges the base local rank; the constant `17` must not be retained.

#### Proof

The rank formula for matroid contraction is

\[
 r_{T_X/O_X}(C)=r_{T_X}(O_X\cup C)-r_{T_X}(O_X).
\]

The hypothesis makes the second term `|O_X|`; transversal rank is ordinary
maximum bipartite matching rank, proving (3.1).  An independent set extends
to a basis of every matroid restriction, so the rank difference is attained
by a matching that saturates all of `O_X`, not merely by a matching of the
same cardinality which sacrifices an outside head.  Subtracting from the
number of active heads proves (3.2)--(3.3), and comparison with the base
state proves (3.5).  \(\square\)

If the batch may invalidate all known matchings of `O_X`, first test

\[
                       \nu(G_X[O_X,U])=|O_X|.             \tag{3.6}
\]

A single weighted matching can combine (3.6) and (3.1): give each edge whose
head is in `O_X` weight `|C|+1` and each edge whose head is in `C` weight one.
The optimum first maximizes outside coverage and, conditional on saturating
`O_X`, maximizes mutable coverage.

### Corollary 3.2 (exact-pair freeze)

Suppose instead that every exact edge of a declared outside matching `M_O`
must remain fixed.  Delete its matched heads and suppliers.  The exact local
rank is

\[
 \boxed{
 r_{M_O}^{\rm fix}(C)
   =\nu\bigl(G_X[C,U\setminus M_O(O_X)]\bigr).}           \tag{3.7}
\]

This is the rank of an ordinary transversal matroid on `C`.  It is a
sufficient but potentially stricter certificate than (3.1), because (3.1)
may reroute the outside heads without leaving any of them unmatched.

## 4. Alternating-path gammoid representation

Choose any successor matching `M_O` saturating `O_X`.  Form a directed graph
`D_X` on the two bipartite shores by orienting

* every edge outside `M_O` from `head` to `supplier`; and
* every edge of `M_O` from `supplier` to `head`.

Let the terminals be the supplier vertices not used by `M_O`.

### Theorem 4.1 (gammoid form)

A set `I subseteq C_X` is independent in `T_X/O_X` if and only if `D_X`
contains `|I|` pairwise vertex-disjoint directed paths from the heads in `I`
to distinct free-supplier terminals.  Therefore `T_X/O_X` is a gammoid, and
its rank is one unit-vertex-capacity linkage/max-flow computation.

#### Proof

If the paths exist, flip matched and nonmatching edges along all of them.
Vertex disjointness preserves matching degree one, every internal outside
head remains matched, and every path adds its initial head.  Conversely,
take a matching saturating `O_X union I`.  The symmetric difference with
`M_O` has degree at most two.  Its components beginning at `I` are disjoint
alternating paths ending at suppliers free under `M_O`; orienting them gives
the required linkage.  \(\square\)

Thus the correct multi-swap analogue of one augmenting path is a set of
vertex-disjoint paths in one fixed successor alternating digraph.  A
contraction of a transversal matroid need not itself have a transversal
presentation, so `gammoid` is the proof-safe general classification.  Under
the exact-pair freeze (3.7), all alternating rerouting is forbidden and the
minor collapses to a transversal matroid.

For a candidate-specific speedup, start the alternating closure at every
new/deleted head, every changed supplier, and every endpoint of an
invalidated matching edge; close under successor nonmatching arcs and
matched reverse arcs.  A component disjoint from this closure retains its
old matching and may be frozen.  Closing only inside the old `Q/B` component
is not sound.

## 5. When ordinary matroid intersection is exact

The gammoid theorem gives a positive matroid-intersection reduction under
the following strict conditions.

1. The successor supplier graph, head-state ground set, and terminal set are
   fixed before optimization.
2. The outside set is independent and contracted as in (3.1).
3. All remaining admissibility conditions on the candidate head set are the
   independent sets of one genuine matroid `A` on that same fixed ground
   set.  Examples are one-state-per-row partition constraints after every
   donor or host choice on the other side has already been fixed.
4. Occurrence or socket labels are genuinely private refinements, or a
   proved extension theorem says that common independence in `A` and the
   gammoid can always be realized by one literal table.
5. Selecting an element does not activate a supplier or compatibility edge
   which can serve another selected element; all such incidences are already
   fixed in the graph.

### Theorem 5.1 (conditional positive reduction)

Under conditions 1--5, an admissible batch matching `k` mutable heads while
preserving all outside heads exists if and only if `A` and `T_X/O_X` have a
common independent set of size `k`.  Ordinary weighted matroid intersection
is exact for additive batch costs.

This is the largest proof-safe positive statement.  If a batch merely
selects replacement head states in a fixed graph, use it.  If selecting the
batch itself creates the external suppliers and cross-head incidences, the
graph is not fixed and Theorem 5.1 does not apply.

## 6. Why the action family is not one matroid

There are three separate obstructions.

### 6.1 Heredity before atomization

If `release` and `compensation` are separate action elements and validity
requires equal numbers or implications pairing them, a valid two-action set
can have invalid singletons.  The family is then not hereditary and cannot
be the independent sets of any matroid.  Any matroidal attempt must first
atomize a complete balanced swap as one column.

### 6.2 Minimal augmentation obstruction after atomization

Even atomic row-disjoint transfer swaps are not a matroid.  Let donors be
`x1,x2`, hosts be `y1,y2`, and let three otherwise harmless atomic columns be

\[
 a=(x_1,y_1),\qquad b=(x_1,y_2),\qquad c=(x_2,y_1).       \tag{6.1}
\]

The row-disjoint sets include `I={a}` and `J={b,c}`.  But neither
`I+b` nor `I+c` is row-disjoint.  Since `|I|<|J|`, the matroid augmentation
axiom fails.  This is the smallest possible obstruction: two ground elements
cannot witness augmentation failure in a hereditary family.

The structural transfer family is instead the intersection of two partition
matroids, one for donor rows and one for host rows.  Adding the supplier
gammoid creates a three-matroid problem, not ordinary two-matroid
intersection.

### 6.3 Exact 3-dimensional-matching obstruction

The need for three constraints is not cosmetic.  Given a 3-dimensional
matching instance with triples `e=(x,y,z)`, create one atomic swap for each
triple.  Give it donor resource `x`, host resource `y`, and a replacement
head whose sole newly available supplier has identity `z`.  Make every old
head removed by a swap a private zero head and isolate the entire gadget
from the frozen outside matching.  A size-`k` rank-improving row-disjoint
batch exists exactly when the triples contain a size-`k` 3-dimensional
matching.

Thus a generic polynomial reduction of this batch selector to ordinary
two-matroid intersection with polynomial rank oracles would solve
3-dimensional matching.  Unless `P=NP`, no such generic reduction exists.
Branching/Benders or a more specialized exact integer oracle is required.

### 6.4 Supplier gain is not a rank function on actions

Even without row conflicts, grouping edge activations by actions destroys
matroid rank.  Start with the sole edge `h1-s1`, of rank one.  Let action
`a` add `h2-s1` and action `b` add `h1-s2`.  Relative rank gains are

\[
 f(\varnothing)=f(\{a\})=f(\{b\})=0,
 \qquad f(\{a,b\})=1.                                  \tag{6.2}
\]

Hence

\[
 f(\{a\})+f(\{b\})<f(\{a,b\})+f(\varnothing),
\]

violating submodularity.  No matroid or gammoid on the action ground set has
this rank function.  The two actions jointly create the alternating path
`h2-s1-h1-s2`; neither creates an augmentation alone.  This is precisely the
selection-dependent-graph phenomenon in batch supplier repair.

## 7. Two exact projection diagnostics

The fixed-parent release ledger is

```text
scratch/def34_release_math_20260802/def34.release_oracle.tsv
SHA-256 789a4002bc1c19f3f840243bee7ed5d624c6ff1209ee59a9b3b79bb1b461823f
```

These probes remove one selected transfer, leaving `437`, and replay the
complete projection.  The directory has no common manifest binding all
inputs.  The old `b268` catalogue is not a prospective recoupled catalogue.
Accordingly, the probes are diagnostics of the fixed table only; they are
not asserted legal next swaps.

### 7.1 Release `32928`: genuine projection gain

Releasing transfer `32928` restores

```text
row 13007: LLR -> LR supplier
row 13925: MR  -> LMR head
```

Restored supplier `13007` supplies former zero head `13914` with flag mask
`136`; the new head `13925` has degree four.  A successor maximum matching
contains

```text
S13007 -> H13914  mask 136
S13887 -> H13925  mask 2
```

The full projection changes as follows:

```text
rank/heads      16864/16898 -> 16865/16898
deficiency                34 -> 33
zero heads                20 -> 19
maximum shore          51/17 -> 50/17
```

The table and audit hashes are

```text
9e5fcd90a90c4020ce50e18f5df597b2c5c3e51b45c2deef5cf31d32962a24f0
  release32928.table.tsv
651032d331a42a1ca522c96381afe0616ef7baa727f1926b7627ec818731444c
  release32928.projection.audit.json
```

Thus this probe has contracted rank gain one at projection level.

### 7.2 Release `63200`: local zero repair, outside displacement

Releasing transfer `63200` restores supplier `19283`, which supplies former
zero head `6352` with mask `263168`, and activates new head `10618` of degree
two.  Nevertheless the full projection remains at rank `16864` and
deficiency `34`; the new maximum shore is `52/18` and the zero count is `19`.

The decisive outside matching change is

```text
base:
  S10617 -> H10352
  S10618 -> H3564
  S10621 -> H10584
  S10642 -> H3584

release63200:
  S10617 -> H3564
  S10618 -> H10584
  S10621 -> H3584
  H10352 unmatched, S10642 free
```

Head `10352` is outside the old `51`-head shore.  Other literal changes
include `S19072 -> H19283` disappearing, new `S19283 -> H6352`, and the
reroute through new head `10618`.  Therefore the local zero repair displaces
one outside match and produces no net rank gain.

The matching and audit hashes are

```text
636f65b6fb0fc679cfa2b940131328d823668acecdff0f2eac8678097d3b237a
  release63200.matching.tsv
b842ff410563e89ab8cfdd16c4af923f7c2b0d305fcfd9413aa1ec3aee1f434a
  release63200.projection.audit.json
```

This is a literal counterexample to all of the following proposed oracles:

* count newly nonzero heads;
* count new neighbours of the old `Q` only;
* add deficiencies of old DM components without alternating closure; or
* preserve only the cardinality of the old `Q/B` matching.

The contraction/gammoid oracle (3.1) detects the outside displacement.

## 8. Exact selected-parent Hall/Benders oracle

For a fixed fully regenerated batch and occurrence selection, let `d_h` be
the active-head bit, put `K_X=sum_h d_h`, and let `p_{hu}` be the exact active
supplier incidence.
For a separated head set `Y`, define

\[
                 n_u^Y=\bigvee_{h\in Y}p_{hu}.             \tag{8.1}
\]

Then the exact supplier rank is

\[
 r_{\rm sup}
   =\min_{Y}\left(K_X-\sum_{h\in Y}d_h+\sum_u n_u^Y\right). \tag{8.2}
\]

Equivalently, maximizing `Theta` under the lazy rows

\[
 \Theta\le K_X-\sum_{h\in Y}d_h+\sum_u n_u^Y            \tag{8.3}
\]

is an exact rank epigraph.  To impose outside preservation, also require
`O_X` independent, or use the lexicographic weighted matching of Section 3.
The violated `Y` comes from one maximum matching and alternating reachability.

This is the smallest universal exact oracle when the batch changes the graph:
the integer master chooses atomic actions and exact parent/occurrence
activations; one polynomial matching separator evaluates (8.2).  A stale
fixed-shore additive score is only a filter.

## 9. Common occurrence support

The current selected-mode occurrence audit is frozen at

```text
.../out/def84_force_mutable_zero_roots/selected_mode_occurrences/
  common.audit.json          b6ff2745c4b3611812cd747609a7babb864420b668fed39753f381b5c5e16774
  common.occurrences.tsv     8e57c62ef6cc198715b71b30e05ef6cf6d5d88fa49f666f1b08d4c3fa9cc1b80
  common.packing.audit.json  c731ca82f49139e63f17ca471aa297e19a98797c3c03d97296021e6ee858fec2
```

For the fixed `438` selected donor roles it reports

```text
phase-0 positive roles                         244
phase-1 positive roles                         216
marginal positive-role intersection            188
roles with one literal tuple common to phases  116
marginal-both roles without a common tuple       72
exact common tuples                             129
maximum row-disjoint common packing             113
```

In this particular audit, `exact common tuple` means literal equality of

```text
(short_row,q,alpha,beta,pred_row,succ_row)
```

between the two phase menus.  This is a deliberately strong cross-phase
identity condition.  Marginal positivity in both phases is necessary for a
paired two-phase realization, but it is not sufficient: the two selected
tickets must also satisfy every declared shared state, flag, physical-row,
and resource equation.

Literal tuple equality is not a universal requirement.  Unless the model
declares that the two phases must use the same physical occurrence, an exact
joint state may select a compatible pair `(g0,g1)` with `g0 != g1`.  The
`116` literal-intersection roles and their rank-`113` row-disjoint packing
are therefore a stronger fixed-overlay calibration, not the general common-
support ground set.  Conversely, the `188` marginal-both roles are only a
necessary optimistic bank, not a feasible paired-ticket certificate.

These facts do not license retaining the fixed `438` modes in a batch.  A
release or replacement changes short/head states and can change every
occurrence menu using those physical rows.  For each prospective batch `X`:

1. materialize its complete successor table;
2. regenerate both phase occurrence menus;
3. select one phase-0 and one phase-1 ticket where required, linked by every
   declared common-state/flag/resource equation;
4. require literal tuple equality only for roles whose semantics explicitly
   identify the physical occurrence across phases;
5. enforce all row and resource capacities on the resulting paired-ticket
   selection `Lambda=(Lambda_0,Lambda_1)`; and
6. construct `G_{X,Lambda}` using only incidences guarded by those selected
   tickets before applying (3.1) or (8.2).

For a fixed pair `(X,Lambda)`, supplier rank is still the contracted
transversal/gammoid rank.  Jointly choosing `X` and `Lambda` is generally an
occurrence hypermatching: each phase ticket consumes a short role plus
predecessor and successor physical rows, and the paired tickets also obey
cross-phase equations before supplier and structural resources are even
added.  It is not automatically a second matroid.  Only a regenerated
private-ticket or otherwise proved matroidal subbank may be used in Theorem
5.1.

The current selected-mode literal-common packing is therefore a useful
strong support calibration, not a necessary general condition and not a
prospective batch oracle.  It also proves no
chronology: row-disjoint equal tuples need not form one state-balanced cycle.

## 10. Exact algorithm and stopping condition

For an atomic batch candidate:

```text
materialize the successor from one literal recoupled parent
validate structural row-disjointness and all protected footprints
regenerate both occurrence catalogues and compatible paired tickets
use literal tuple intersection only where cross-phase identity is declared
select paired occurrence/resource variables and build their guarded graph
put every changed head or incidence endpoint in the mutable closure
verify the outside heads remain independent
compute r_O(C) by one matching/alternating-path gammoid oracle
accept the claimed gain only if the exact rank and every nonmatching gate pass
```

A sufficient continuation theorem is now taut but sharp: if every reachable
positive-deficiency state admits a structurally and occurrence-valid batch
whose exact contracted rank gain is at least one, repeated acceptance reaches
deficiency zero in at most the current deficiency many accepted batches.
Neither the strict `51/17` decomposition nor the two release probes prove
that hypothesis.

## 11. What this theorem does not prove

It proves the exact fixed-successor gammoid, the outside-contraction rank
formula, the conditional positive matroid-intersection reduction, and the
general nonmatroid/three-constraint obstruction for selecting batches.

It does not prove that either diagnostic release is a legal next move.  In
particular, the probes leave `437` selected transfers and have no replay here
of a compensating addition, protected `7,213`-row preservation, socket floors,
prospective recoupled transfer catalogue, common occurrence packing, residual
outer completion, chronology, residence, upper deck, compiler, or word.

Projection closure remains strictly weaker than common-occurrence and
chronology closure.
