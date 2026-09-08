# A fourth `T2` prefix phase closes the finite `D_5` suffix actuator, but neither a component hypertree nor undilated residence survives

**Date:** 2026-08-14
**Status:** unconditional exact finite theorem at suffix semilength five in
the internal-owner alternating-circuit class.  A 41-circuit bank is pairwise
owner- and q1-colour-disjoint, preserves aggregate q2 support, and sends all
42 `D_5` suffix roots and all 372 touched lifted components to one output.
The suffix labels form a tree, but the component--trade incidence graph has
cycle rank 35 and is not a hypertree.  Both undilated q=2 residence collars
fail.  No all-semilength first-return grammar or physical common-history
planting is claimed.

## 0. Outcome

Let `D_5` be the 42 Dyck words of semilength five.  Start with the exact
post-`T2` factor at `m=11`, and use the internal-owner alternating circuits
defined in
`MATH_THEOREM_T2_DYCK_D3_D4_SPANNING_ACTUATOR_ATLAS_AND_CONTEXT_GATE_20260813.md`.
The first-return split

\[
                         X=1U0V                                      \tag{0.1}
\]

partitions `D_5` into blocks of sizes

```text
(|U|,|V|) = (0,4),(1,3),(2,2),(3,1),(4,0)
block size =    14,    5,    4,    5,   14.
```

There is an explicit split-aware label tree with

```text
26 child_D4 edges
 8 child_D3 edges
 3 child_D2 edges
 4 consecutive-split bridges
--------------------------------
41 edges on 42 suffix roots.
```

Its degree histogram is `1:7, 2:30, 3:5`.

The all-six-prefix exact minimum candidate bank is not resource-selectable.
Adding the first reset phase still is not resource-selectable.  One further
prefix phase is enough:

```text
productive minimum phases  101001010101, 101001001101
first reset phase P0        101010001101
closing reset phase P1      100011001101.
```

The selected 41 circuits use these phases respectively `12,10,10,9` times.
Their simultaneous toggle has the exact result

```text
pairwise owner disjoint                         yes
pairwise q1-colour disjoint                     yes
aggregate q2 support losses                       0
minimum surviving old q2 load                     1
negative q2-current occurrences                 346
base lifted components met                      372
output components on touched owners               1
suffix-representative output components           1
component reduction                             371
output component owner length per shore       12420.
```

Thus the finite `D_5` topology problem is solved.  The residence result is
negative:

```text
bad upper q=2 collars   181
bad lower q=2 collars   151
minimum seam gap        1 on both shores.
```

## 1. The split-aware suffix tree

The extreme blocks `(0,4)` and `(4,0)` receive the frozen 13-edge `D_4`
tree under `X -> 10X` and `X -> 1X0`.  The blocks `(1,3)` and `(3,1)` receive
the four-edge `D_3` tree in the corresponding right and wrapped contexts.
The middle `(2,2)` block is the `D_2 x D_2` square with one edge deleted.
Finally use the lexicographically first Johnson edge between each consecutive
pair of split blocks.  The four bridges are

```text
1010101010 -- 1100101010
1100101010 -- 1101001010
1101001010 -- 1101010010
1101010010 -- 1101010100.
```

The frozen builder independently checks the 41 distinct transposition edges,
connectivity on all 42 roots, the split sizes, and the degree histogram.

## 2. Exact circuit menus

For a suffix edge `A--B` and a `T2` prefix owner `P`, the admissible circuit
is a simple directed path `PA -> PB` together with a simple directed path
`PB -> PA`.  Every owner on both paths has degree two in the post-`T2`
factor.  The two paths share only their endpoints and no q1 colour.  At a
toggled row `(O,Q^-,Q^+)`, with untouched selected mate `M`, the q2 current
is

\[
                         [M\cup Q^+]-[M\cup Q^-].              \tag{2.1}
\]

Every minimum below is exact in this internal-owner class: directed
distances supply the lower bound; every shorter length and path split is
exhausted; label simplicity and `(2.1)` are checked against the complete old
load ledger.

### 2.1 All-prefix global minima

Across all six `T2` prefix channels the exact per-edge histogram is

```text
C14:1  C18:9  C20:13  C22:16  C24:2.
```

There are 4,912 literal circuits in the complete global-minimum bank.  The
resource SDR is UNSAT.  Deletion shrinking gives the inclusion-minimal core

```text
edge 35  child_D2      (2,2)--(2,2)
edge 38  split_bridge  (1,3)--(2,2)
edge 39  split_bridge  (2,2)--(3,1).
```

All three meet the suffix `1101001010`; only the two productive endpoint
phases occur at their global minima.

### 2.2 The first reset phase is still insufficient

For `P0=101010001101`, exhaust the strict-shorter classes separately on all
41 edges and retain every circuit at the first q2-safe length.  The exact
length histogram is

```text
C18:1  C22:5  C24:15  C26:15  C28:3  C30:2.
```

Together with the 4,912 global-minimum circuits this gives 13,394 candidates.
The resource CNF remains UNSAT.  Its inclusion-minimal four-edge core is

```text
edge 22  child_D4      (0,4)--(0,4)
edge 27  child_D3      (3,1)--(3,1)
edge 33  child_D3      (3,1)--(3,1)
edge 37  split_bridge  (0,4)--(1,3).
```

The two adjacent pairs are supported at distant suffix roots but collide in
auxiliary owner/colour resources.  Hence ordinary degree-three edge colouring
of the label tree does not solve the SDR.

### 2.3 One additional reset phase closes the bank

Use `P1=100011001101`.  Iterative core extension first produced a 14-edge
core spanning every split class and then the four-edge extreme-block core

```text
edges 1,17,18,21: four child_D4 edges,
three in split (4,0) and one in split (0,4).
```

Adding the `P1` first-safe menus on the propagated cores closes the resource
CNF.  The final topology search used 20,329 candidates.  Only nine `P1`
circuits are selected, on edges

```text
3, 6, 11, 17, 18, 23, 28, 29, 33,
```

with selected `P1` lengths

```text
C26:2  C28:3  C30:3  C32:1.
```

Every selected `P1` circuit belongs to a fully enumerated first-safe class;
no retained-candidate cap is used to justify a selected row.

This is the sharp phase statement proved here:

> Relative to the frozen global-minimum plus `P0` first-safe bank, zero new
> prefix phases is impossible and the single additional phase `P1` is
> sufficient.

It is not a proof that every possible three-channel bank, or arbitrarily
long circuits confined to three channels, is impossible.

## 3. Exact aggregate q2/resource selection

Give every candidate a Boolean variable.  The base CNF imposes:

1. exactly one candidate on each of the 41 tree edges;
2. at most one use of every owner;
3. at most one use of every q1 colour;
4. for every old q2 target `T`,

   \[
                 L_T+\sum_C x_C\Delta_C(T)\ge 1.              \tag{3.1}
   \]

For positive and negative terms, `(3.1)` is converted exactly to a signed
cardinality inequality by replacing each gain literal `x` with the absent
gain literal `not x` and shifting the right-hand side by the total possible
gain.  A k-modulo-totalizer encoding was independently exhaustively checked
on signed repeated-literal test instances.

The final q2/resource CNF has

```text
candidate variables and auxiliaries   1,237,774
clauses                               3,925,056
old q2 targets constrained                3,992.
```

The selected incidence-length histogram is

```text
C18:6  C20:6  C22:11  C24:6  C26:4  C28:3  C30:4  C32:1.
```

The independent verifier does not trust `(3.1)`: it rebuilds the post-`T2`
factor and recomputes all 346 negative occurrences.  Every old target retains
load at least one.

## 4. Exact topology CEGAR

Resource disjointness, q2 safety, and a suffix-label tree do not force one
lifted output.  The first q2-safe resource model had eight output components
in the preliminary replay.

The final selector uses exact connectivity cuts.  For a rejected model and
a proper output component `S`, let

* `R_S` be the currently selected candidate variables whose removed old
  incidence crosses `S`;
* `A_S` be all menu variables having an added incidence that crosses `S`.

Every connected alternative must satisfy

\[
              \bigvee_{x\in R_S}\neg x\ \vee\
              \bigvee_{y\in A_S}y.                            \tag{4.1}
\]

Indeed, if all current crossing removals remain and no new crossing incidence
is selected, no lower-factor edge crosses `S`.  The fixed complemented return
half and endpoint verticals cannot cross `S`, because `S` is a component of
the current complete lift.  Thus `(4.1)` is necessary, not a heuristic
whole-model block.

Incremental CaDiCaL rejected seven models.  Their touched/suffix output counts
were

```text
4/2, 7/3, 8/6, 4/2, 3/2, 3/2, 2/2.
```

Thirty-one exact cuts then produced the eighth model with `1/1`.  Direct
traversal of the complete lifted factor gives 372 touched base components,
one output, reduction 371, and 12,420 owners per shore.

## 5. Tree versus hypertree

The 41 suffix-label edges are a tree.  This does not lift to a component
hypertree.  Let the 41 actuator supports be hyperedges on their touched base
components.  The bipartite component--trade incidence graph has

```text
component vertices   372
trade vertices         41
incidence edges        447
connected components     1
cycle rank              35 = 447-(372+41)+1.
```

Therefore the selected component hypergraph is connected but not a hypertree.
The one-output conclusion rests on the exact endpoint traversal in Section 4,
not on the sufficient hypertree theorem.

## 6. Common-history and residence diagnostics

The individual upper common-intersection ranks have histogram

```text
5:1  6:5  7:7  8:22  9:6,
```

while the lower ranks have histogram

```text
0:2  1:1  2:6  3:14  4:10  5:5  6:3.
```

Every lower palette has a nonzero loss current, between 6 and 14 occurrences;
two circuits have lower common-intersection rank zero.  Thus even the
algebraic common-core test is not uniform on the lower shore.  A physical
common-history lift would additionally require occurrence-disjoint,
cut-separated source fragments, which are not supplied here.

The complete simultaneous output has 181 bad upper and 151 bad lower q=2
collars.  Both minimum seam gaps equal one.  Consequently

\[
 \boxed{\text{the finite D5 actuator is q2-support-safe and topologically
 spanning, but not undilated two-shore resident.}}             \tag{6.1}
\]

## 7. Frozen certificate and provenance

The principal H100 artifacts are:

```text
menu bundle
  scratch/t2_suffix_d5_reset_menu_bundle_20260814.h100.out
  SHA256 9c22615cd3058688f048f4e4062d007edadb10ab415c15ee89ed10d21b1bed8d

selector
  scratch/solve_t2_suffix_d5_topology_cegar_20260814.h100.out
  SHA256 94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32

independent full-factor verifier
  scratch/verify_t2_suffix_d5_topology_cegar_selection_20260814.h100.out
  SHA256 ff5475083d3d836b5f107c5821c45918676b4a6df81bffc48ac1af8600e6a068

hostile menu/core audit
  scratch/audit_t2_suffix_d5_reset_spanning_bank_20260814.h100.out
  SHA256 1da6977f8e978c71fb90bcfb3bc54aa223f0d894850751200c3c425593c16942

signed-cardinality encoding audit
  scratch/verify_t2_suffix_d5_signed_cardinality_encoding_20260814.h100.out
  SHA256 38d036714801352a29cb3951aec659bbf6d9305ec29c893c5fd2b82320965855
```

All enumeration, compilation, SAT solving, traversal, hashing, and audit runs
were executed via SSH on H100.  The local Mac was used only to read/edit
sources, transfer frozen artifacts, and operate Git.

## 8. Exact remaining gate

This theorem settles the finite `D_5` reset-template SDR and topology problem.
It does not yet give the desired induction.  The remaining gate is

\[
 \boxed{\begin{array}{c}
 \text{derive a split-size finite-state reset grammar valid for every}
 \ D_s,\text{ with uniform phase and length bounds;}\\
 \text{then plant its selected circuits in occurrence-disjoint,
 cut-separated, residence-dilated two-turn histories.}
 \end{array}}                                                   \tag{8.1}
\]

The walking sequence of Hall cores shows why copying aligned child atlases is
not itself such a grammar: auxiliary resources couple distant first-return
blocks.  The fourth phase repairs `D_5`, but no recurrence proving that the
number of states stays bounded at `D_6,D_7,...` is present.
