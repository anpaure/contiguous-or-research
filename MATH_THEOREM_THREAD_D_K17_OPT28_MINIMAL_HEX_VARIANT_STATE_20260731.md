# K17 OPTIMAL28: minimal palette-preserving component variants and the exported RSB state

Date: 2026-07-31  
Status: exact local-column theorem and complete K17 minimum-support catalogue;
no residence repair or K17 word is claimed

## 1. Fixed obstruction, refined by literal location

Keep the authenticated `4108`-owner marked packet fixed.  In the `4871`
nonmarked fixed macro components there are exactly `724` strict owner runs of
length below four, supported on `257` components:

\[
  320\text{ runs of length }2,
  \qquad 404\text{ runs of length }3.
\]

Their literal anatomy is sharper than this scalar ledger.

* `227` length-three runs are on old coordinates `0,...,14`, lie strictly
  inside `141` individual macros, and survive every existing macro-port split.
* `497` runs cross a macro join and use one of the two new coordinates.  Their
  profile is
  \[
  X:(160\text{ of length }2, 80\text{ of length }3),\qquad
  Y:(160\text{ of length }2, 97\text{ of length }3).
  \]
* No support interval contains a component boundary edge.  The nearest
  support is one owner edge inside a component; `637` of the `724` rows are
  more than two edges from either component endpoint.

Thus changing component order, reversal, or exterior connectors cannot touch
any of the `724` rows.  Among bad components, `107` contain one macro and
`150` contain between two and sixteen macros.  The complete macro-count and
run-count histograms are in the audit payload.

For a strict run beginning at owner position `s` and having length `ell`, its
support is the owner-edge interval

\[
                  I=[s-1,s+\ell-1].                 \tag{1.1}
\]

At least one edge of `I` must change.  Interval duality gives an exact
arbitrary-adjacency transversal and disjoint packing of size `452`.  If split
sites are restricted by physical provenance, the `227` strict-macro rows need
`155` interior macro sites, while the `497` tag rows need `305` existing
macro-join sites.  The latter two figures are separate restricted optima and
are not additive lower bounds for a mixed actuator.

## 2. The smallest exact palette-preserving rethread

Let `Gamma_r` be the bipartite inclusion graph between rank-`r-1` colours and
rank-`r` owners.  A lower-rainbow Johnson factor is equivalently a subgraph of
`Gamma_r` having degree two at every owner and every colour.

### Lemma 2.1 (no four-cycle)

`Gamma_r` has no four-cycle.

#### Proof

If two distinct rank-`r-1` sets `c,d` lie in a rank-`r` set, their union is
the unique rank-`r` set `c union d`.  They therefore cannot have two distinct
common rank-`r` neighbours.  \(\square\)

### Theorem 2.2 (minimum literal rethread is an incidence hexagon)

Every nonzero finite palette-preserving factor change has support at least
six in the incidence variables.  Equality holds precisely on a hexagon

\[
 K+a, K+b, K+c
 \quad\leftrightarrow\quad
 K+ab, K+bc, K+ca,                                  \tag{2.1}
\]

where `|K|=r-2` and `a,b,c` are distinct labels outside `K`.  If one of the
two alternating phases of this hexagon is selected, replacing it by the
other phase preserves every owner degree and every lower-colour degree
exactly.

#### Proof

The signed difference of two degree-two factors is an integral circulation
in the bipartite incidence graph and decomposes into even alternating
cycles.  Lemma 2.1 excludes support four.  A six-cycle has three colour and
three owner vertices.  Intersecting its three colour vertices gives a common
rank-`r-2` core `K`, and the remaining labels give (2.1).  Alternating the
cycle changes three selected incidences to the other three and has zero
degree at all six vertices.  \(\square\)

This is the smallest literal component-split/rethread primitive.  For each
of its three colours, one selected endpoint is replaced while the other
endpoint stays fixed.  Hence it may split, merge, or reroute factor
components, but it never loses or duplicates an owner or lower colour.  If
its three owners avoid the marked owner packet, the packet remains literally
intact; a boundary colour may change its complementary endpoint without
changing the marked endpoint.

The hexagons are the complete **minimum-support layer**, not a claimed
generating set for every rethread.  More generally, the signed difference of
two equal-degree factors decomposes conformally into simple alternating
circuits.  Some longer circuits may be primitive in the allowed resource
subgraph and need not decompose into legal hexagons.  If a local split exports
nonzero degree current, the corresponding normal form additionally contains
alternating trails ending at the exported socket occurrences.  The exact
all-support catalogue is therefore simple alternating circuits plus
boundary-current trails; Section 3 freezes its first, smallest layer.

## 3. Complete K17 minimum-support catalogue

The deterministic audit enumerates every alternating incidence hexagon of
the frozen OPTIMAL28 factor and then applies the two exact filters above.

```text
all alternating incidence hexagons                         44,917
hexagons whose three owners avoid the marked packet         27,933
such hexagons touching at least one immutable run             5,433
```

The `5,433` active columns cover every one of the `724` rows and every one of
the `257` bad components.  No row has a local supply obstruction: row degree
ranges from `2` to `34`.  By row class:

```text
strict macro-interior, length 3       227 rows, degree 2..20
macro-join, length 2                  320 rows, degree 2..22
macro-join, length 3                  177 rows, degree 5..34
```

One hexagon touches at most five current bad rows and at most three current
components.  The exact column profiles are

```text
number of hit rows:       1^2947 2^2115 3^263 4^103 5^5
number of hit components: 1^4998 2^417  3^18
```

There are `3932` join-only columns, `1307` strict-interior-only columns, and
`194` columns coupling the two defect classes.  The active-label/core tag
profiles are

```text
(core tags, active tags) = (0,1)^1537 (1,0)^1859
                            (1,1)^1214 (2,0)^823.
```

These counts prove that the `106`-variant scalar floor is not blocked by
local incidence supply: every one of those `106` components has between `5`
and `225` active columns.  There are `115` columns meeting two floor
components and `2` meeting three.  They do **not** prove a compatible selection:
hexagons can conflict, can create new short runs, can spoil upper witnesses,
and can violate common-cap cells.  Within the one-layer baseline-hex model,
every old bad row must be hit, so the maximum row coverage five gives the
weak bound `ceil(724/5)=145`.  The interval certificate is sharper: every
repair deletes at least `452` distinct old owner adjacencies, whereas one hex
deletes only three.  Hence a compatible pure-hex repair needs at least

\[
                         \lceil452/3\rceil=151
\]

columns.  This is scoped to the pure minimum-support hex face; a longer
circuit pays its literal number of deleted old adjacencies.

## 4. Exact local signature and all-dimension state

An active column has the following lossless signature.

\[
 \Sigma=(K; a,b,c;\epsilon;
          \{(c_i,w_i^\mathrm{fixed},w_i^-,w_i^+)\}_{i=1}^3;
          R;\mathcal C).                                \tag{4.1}
\]

Here `epsilon` is the selected phase, `w_i^- -> w_i^+` is the changed
endpoint of colour `c_i`, `w_i^fixed` is its unchanged other endpoint, `R`
is the set of immutable rows hit, and `C` is the set of current components
meeting those rows.  The first two fields determine the six incidence
variables; the three endpoint quadruples determine the component
split/rethread exactly.  Owner and lower-palette resource deltas are
identically zero and need no aggregate ledger.

For residence depth `d` and protected shadow depth `H`, extend (4.1) by the
following correlated physical data:

1. the length-`d` coordinate trace collars on both sides of the six sockets;
2. the exact target-labelled prefix/suffix accumulated-union transfers (or
   an explicit bank of every endangered old witness and gained new witness);
3. the signed socket/boundary current for trail atoms; and
4. either the compiler/common-cap collar relative to one already fixed and
   transported cap/matching, or the full exact global rank-three common-cap
   recourse relation.

All old owner and lower-colour data outside the six incidences are unchanged,
and residence is decided by a bounded collar automaton.  Arbitrary-width
upper service is not a bounded collar property: exact prefix/suffix union
chains remain target-labelled.  Likewise, a five-row common-cap collar is
exact only when transporting a previously fixed compiler; before a compiler
exists one must retain the full common-cap boundary relation or solve global
recourse.  Thus (4.1) is the smallest incidence signature, while the exact
RSB extension is the product signature in
`MATH_THEOREM_THREAD_D_ALLK_COMPONENT_VARIANT_RSB_SIGNATURE_20260731.md`.
Its port and residence arity is bounded, but its upper and cap banks may grow
with the dimension.

The exact master must still impose binary incidence bounds

\[
  0\le x_e^0-\sum_{h:e\in h^-}y_h+
                    \sum_{h:e\in h^+}y_h\le1,           \tag{4.2}
\]

followed by component connectivity, the residence collar automaton, complete
upper-witness replay, and common-cap recourse.  Equation (4.2) is necessary
even though each individual column is degree-neutral: it prevents two
columns from removing or adding the same incidence.

## 5. Reproducibility and scope

Generator/audit:

`scratch/audit_threadD_k17_opt28_hex_variant_catalogue_20260731.py`

SHA-256: `0a9daacc04c7754e70d674f862d66d03d13842fe6153bf520ac6fcfd2ad99cd0`

Payload:

`scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json`

SHA-256: `9ac6416078d73676ca63d483cf30540806ef14f588f77bf8301d0ca5b919a87e`

Payload SHA-256:
`ba0fce17bfe13d491cbb2cf229d3f070e75def80b50de854d89af226e5d24923`

The payload contains all `724` support rows, all exact transversal points,
and all `5,433` columns with their six incidences, three source-edge
rethreads, hit rows, and hit components.  It is a catalogue and theorem-level
reduction only.  It makes no K17 completion claim.
