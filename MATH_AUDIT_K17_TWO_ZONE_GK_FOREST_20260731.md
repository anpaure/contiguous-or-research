# Audit of the proposed `k=17` two-zone Greene--Kleitman construction

Date: 2026-07-31  
Verdict: **GO** for the complete scalar ledger, Boolean-diamond counts, and
the explicit two-cut Greene--Kleitman forest.  **NO-GO** both for the
proposed direct/two-edge completion and for the first 294-colour short-ear
repair.  Arbitrary-length ears on the immutable seed are also ruled out;
only a cut/rethread or changed-seed completion remains open.  No
length-24313 word is certified.

## 1. Independently verified claims

A dependency-free reconstruction over all `binom(17,6)=12376` rank-six
sets verifies the following exactly.

1. The distinct-pivot contributions for `a=0,...,6` are

   \[
       8,232,1744,4384,3124,624,36,
   \]

   both by direct pivot enumeration and independently by the stated
   reflection-principle sum.  Their total is `10152`.
2. Whenever the two pivots differ, the rotated pivot is strictly larger in
   the ordinary coordinate order.  The sum-of-elements potential therefore
   orients every edge increasingly.
3. Each of the two upward pivot maps is injective.  The projected graph has
   `15376` vertices, maximum degree two, and exactly `5224` components; every
   component is a path.
4. The `10152` edge unions all have rank eight and are pairwise distinct.
5. The `4928` degree-two turns all have rank nine and are pairwise distinct.
6. The path-size histogram is

   ```text
   vertices in path : 2    3    4   5  6  7  8
   number of paths  : 2184 1716 876 349 83 15 1.
   ```

7. A canonical rank-five/rank-eight containment has exactly `120` distinct
   oriented Boolean-diamond realizations and `54` guard letters on either
   side, but those letters induce only `9` distinct rank-nine owner colours.
8. Every displayed prefix/tail/ear scalar identity is correct.
9. The un-ordered prefix block inventory exists by two explicit Hall
   inequalities and the Erdős--Ko--Rado bound; only its rainbow ordering is
   open.
10. The GK forest is all-width rainbow inside its components.  For widths
    `2,...,8`, every consecutive union has rank `6+width` and is globally
    distinct.  The protected-bank counts are respectively
    `10152,4928,1888,564,116,17,1` at ranks `8,...,14`.

This also repairs one presentational ambiguity in the proposal: with
`C=(S-{a,b})+g`, the exact common intersection is `R cap T=C` of rank four.
No rank-five intersection assertion is used.

## 2. The original ear schedule is impossible

Let `E_0` be the 10,448 degree-one vertices of the GK forest.  A direct join
has two endpoints in `E_0`; each edge of a two-edge join has one endpoint in
`E_0` and one new intermediate rank-seven vertex.  Consequently the
rank-six intersection colour of every such new edge has at least one
rank-seven superset in `E_0`.

Among the 2,224 missing rank-six colours, exact enumeration gives

```text
missing colours with no original endpoint superset     674
missing colours whose all 11 rank-seven supersets
are unused by the GK forest                            294.
```

Thus the displayed `3688` direct plus `1535` two-edge ears cannot introduce
all missing rank-six colours.  Cutting old GK edges can expose internal
vertices and may repair 380 of the 674, but it cannot repair the 294 colours
whose every superset is unused.

Every one of the 674 no-endpoint colours must occur on an
internal--internal edge of an ear in any completion retaining every GK edge.
Exact enumeration against the authenticated rank-eight and rank-nine
palettes gives:

```text
all 674 no-endpoint colours:
  locally clean three-edge ear                         266
  no three-edge but a clean four-edge ear              128
  neither within four edges                            280

the 294 all-unused subfamily:
  locally clean three-edge ear                         252
  requiring a clean four-edge ear                       42.
```

Here “locally clean” means that the ear joins two old path endpoints, uses
fresh internal rank-seven vertices, and all of its new rank-eight edge
unions and rank-nine turns avoid the GK palettes.  Thus 280 colours require
longer ears, shared multi-colour ears, or cuts/reroutes.

In particular, the previously advertised repair

\[
 (x_1,x_2,x_3,x_4)=(4024,905,252,42)                  \tag{2.1}
\]

is also impossible.  It has only

\[
 252+2(42)=336<674                                    \tag{2.2}
\]

internal--internal edges.  For a no-cut schedule, if `x_j` counts `j`-edge
ears, the exact necessary capacity conditions are

\[
 \sum_jx_j=5223,\qquad
 \sum_j(j-1)x_j=1535,\qquad
 \sum_{j\ge3}(j-2)x_j\ge674.                          \tag{2.3}
\]

These conditions are arithmetically consistent, for example with
`(x_1,x_2,x_3)=(4362,187,674)`, but they are not sufficient.  A separate
greatest-supported-edge/wedge peel closes the entire immutable-forest
branch for arbitrary ear lengths: the induced missing-rank-six versus
fresh-rank-eight provider graph has matching rank `1780/2224`, with `416`
zero rows and an explicit Dulmage--Mendelsohn witness of `584` demands
against `140` providers.  Every locally clean long ear survives the peel,
so a globally rank-eight-rainbow completion would yield the impossible
`2224`-matching.  This result has been independently reconstructed from
scratch.  Therefore a successful use of this GK seed must cut/rethread old
edges or change the seed; merely lengthening ears cannot work.

There is also an exact cut-and-reroute ledger.  Cutting `c` pairwise
vertex-disjoint *internal* GK edges changes the seed to `5224+c` components,
`10152-c` edges and `4928-2c` turns.  If the old 294-colour short-ear counts
are retained, increasing the direct-ear count from `4024` to `4024+c`
produces `6758+c` new edges and `11981+2c` new turns, so the final rank-eight
and rank-nine counts still telescope exactly.  Endpoint capacity alone then
requires `336+2c>=674`, hence `c>=169`.  A bipartite matching assigns the
other 380 no-endpoint colours to 380 distinct internal rank-seven supersets,
so the cut route passes its first vertex-assignment Hall test.  Compatible
cut edges and globally rainbow rerouting are not proved.  A separately
frozen certificate now exposes all 380 non-all-unused no-endpoint colours
using 312 vertex-disjoint cuts (90 endpoint--internal and 222
internal--internal), and its scalar ledger replays exactly.  This closes
only exposure: palette-safe simultaneous ear selection on the cut forest is
still open.  In fact, the fixed certificate's chosen colour-to-port
assignment already fails its next physical-neighbour Hall row: matching rank
`368/380`, with a `77>65` DM witness.  This is not a no-go for another
assignment or cut set; it proves that cuts, assignments and physical partners
must be optimized jointly.

## 3. Corrected prefix and upper interfaces

The prefix inventory lemma prevents repeated *low targets*; it does not by
itself prevent two different low blocks from having the same rank-eight
union.  Write the prefix as `q_0,...,q_7400` and put

\[
 C_i=q_i\cup q_{i+1}\qquad(0\le i<7400).
\]

Zero slack requires the `C_i` to be distinct rank-eight sets.  For
`0<=i<7399`, the owner is

\[
 q_i\cup q_{i+1}\cup q_{i+2}=C_i\cup C_{i+1}.
\]

Consequently the exact internal prefix gate is a vertex-simple path in
`J(17,8)` with distinct rank-nine edge-union colours.  At every rank-seven
separator `q_{i+1}`, one additionally has the forced identity
`q_{i+1}=C_i cap C_{i+1}`.  Two cross-seam triples supply the remaining two
prefix owner colours.  This occurrence-labelled doubly-rainbow path is
strictly stronger than the unordered block inventory.

Coverage above rank nine is independent.  For example, the six rank-six
letters

```text
012345, 123456, 234567, 345678, 456789, 056789
```

have distinct rank-seven pair unions, distinct rank-eight triple unions and
distinct rank-nine quadruple unions, but their two rank-ten five-letter
unions coincide.  Thus ranks `10,...,16` need a separate witness condition.
The all-width GK bank in item 10 is useful protected supply, not a proof that
an eventual ear completion remains upper-complete.

## 4. What has not been verified

The audit does **not** establish any of the following.

* The cut/rethreaded components can be connected under their altered
  component and palette ledger while satisfying all rank-six, rank-eight
  and rank-nine rainbow constraints.
* The `2537` low prefix blocks and `2536` rank-seven separators admit the
  required alternating ordering.
* The complete chronology covers ranks `10,...,17`.
* A universal word of length `24313` exists.

The exact one-pivot owner row is mixed-width, not a uniform length-four row.
Starts `0,...,7400` have length-three rank-nine owners, while starts
`7401,...,24309` have length-four owners.  Thus the proposal must provide
`7401` prefix triple owners and `16909` tail quadruple owners, totalling
`binom(17,9)=24310`.  This is a correct ledger, not yet a proof those owner
windows are all distinct rank-nine sets.

## 5. Reproducibility

The source is

```text
scratch/audit_k17_two_zone_gk_forest_20260731.py
```

and emits

```text
scratch/k17_two_zone_gk_forest_20260731.audit.json.
```

The canonical payload hash is

```text
c5eab693949d301bbb41888d98e628a83d063f15289e2f6d6134e24469e08bca
```

The arbitrary-length immutable-seed no-go and its independent
reconstruction are respectively

```text
MATH_THEOREM_H2_K17_GK_RAINBOW_EAR_ENDPOINT_HALL_OBSTRUCTION_20260731.md
  SHA b32243b40b27f73b9ec8b72620353162e9f6cebfec02ba60866e820f15169e3c
MATH_AUDIT_INDEPENDENT_K17_GK_SUPPORTED_EAR_HALL_20260731.md
  SHA b60387c8422e205cf558b484d7916a81ad0c944d342a76c3ab1258829f9a3828
```

The frozen 312-cut exposure certificate (not a tail completion) is

```text
MATH_AUDIT_K17_GK_MIN_VERTEX_DISJOINT_CUT_ROUTE_20260731.md
  SHA ba2f82d304df49dd60e3b3110cb9930aa3122269cc0ec0c86ebc73d14f57ab56
scratch/k17_gk_cut312_certificate_30e0812da947f999_20260731.json
  SHA 30e0812da947f999a5c6d91ca52c323c7ca25302c127daf3434262faed9e9474
scratch/audit_k17_gk_cut312_certificate_20260731.py
  SHA 36f518cbeec5c4de7d8f18494aacca1c6d358c961a6151f0ef281407227dd19a
```
