# Independent audit of the `K17` OPTIMAL28 one-cycle shadow/common-cap cuts

Date: 2026-07-31  
Verdict: **valid with the fixed-carrier scope stated in the theorem**

Audited theorem:

```text
MATH_THEOREM_R_K17_OPT28_ONECYCLE_DEEP_SHADOW_AND_COMMON_CAP_CUTS_20260731.md
```

## 1. Independent literal replay

The lightweight audit

```text
scratch/audit_r_k17_opt28_onecycle_deep_common_cuts_20260731.py
```

does not optimize a path or residual flow.  It authenticates the frozen
inputs, reads the materialized owner cycle, reconstructs the marked owner
set from the original macro/packet data, and then rebuilds the zipper and
all reported cuts.

It verifies independently:

```text
rank-nine owners                                  24310/24310 distinct
rank-eight adjacent intersections                 24310/24310 distinct
marked cyclic run                                  4108 owners
complement cyclic run                             20202 owners
direct facet rail                                 20203 distinct rows
Z length / rank profile                    24311 / 9^4108 8^20203
adjacent Z unions of rank below nine                          0
scalar lower-only reserve                                  3293.
```

These counts agree with the separate connected-factor and nonflat-zipper
materializers.  The connected quotient is therefore a proved input, not an
assumption of the new cut theorem.

## 2. Inversion certificate

The maximal-envelope reconstruction gives:

```text
nonempty envelope positions                       24313/24313
strict Z runs of length 1 / 2                       1025 / 1367
failed D2 rows                                             3568
zero-host row-bit obligations                              3759
zero-host bits in marked / facet shores                 0 / 3759.
```

The first witness replays literally:

\[
 Z_{4127}=\mathtt{0x0348f},\qquad
 (E_{4127},E_{4128},E_{4129})
 =(\mathtt{0x02487},\mathtt{0x03087},\mathtt{0x03087}),
\]

and

\[
 E_{4127}\cup E_{4128}\cup E_{4129}
 =\mathtt{0x03487},
\]

which omits bit `3`.  Since every realizing physical letter is contained
in its maximal envelope, this single row proves that the fixed `Z` is not a
second derivative.  Common-cap Hall is therefore logically downstream and
must not be run on this row.

The independent component scan sharpens the escape scope.  The frozen
complement has `724` strict internal owner runs (`320` of length two and
`404` of length three) in `257` fixed components.  Facetization shortens
them to forbidden internal runs without touching a seam.  Hence changing
only residual pairs, component order, or component orientation cannot
repair inversion.  The live class needs genuine component variants,
partial-macro rethreading, or compound actuators.  This is compatible with,
and stronger than, the one-row certificate above.

## 3. Upper-provider replay

All linear `Z` intervals were accumulated until their union first became
the full `17`-set.  The audit examined `618182` intervals and obtained

| rank | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| holes | 1900 | 911 | 128 | 0 | 0 | 0 | 0 | 0 |

This agrees exactly with the independent zipper audit.  The first missing
masks are `0x007bf`, `0x007ff`, and `0x03efe` at ranks ten, eleven, and
twelve.

The audit also records the fixed-depth owner-window table.  It is not used
as a substitute for physical interval coverage.  In particular, four-owner
rank-twelve windows miss `187` targets, while arbitrary physical `Z`
intervals miss only `128`.  This difference confirms that a fixed-width
proxy would be unsound.

## 4. Proof audit of the partition cuts

For an upper target `Y`, in a simple spanning owner path/cycle using every
rank-nine owner once, the selected owner intervals contained in `Y` are
exactly the connected components of the selected factor induced on

\[
 V_Y=\{T:T\subseteq Y\}.
\]

If one component has union `Y`, every partition whose blocks have proper
union must split that component, and a connected graph has a selected edge
across the partition.  If no component has union `Y`, the partition into
actual components has proper union in every block and no crossing edge.
This proves both necessity and sufficiency of the partition family.

The proof is only for an **integral** selected path or factor.  It is an
exact lazy separator at an integral incumbent, not a claim that these cuts
describe the fractional convex hull.  The dual lower-intersection statement
has the same scope.  Physical upper compilation remains governed by the
mixed-rank `Z` interval rows.

## 5. Audit of the combined short-cell cut

The direct facet bank contains

\[
 d_8=20203
\]

distinct lower targets.  Thus the residual lower family has

\[
 65535-20203=45332
\]

members.  The uncovered long-upper family has

\[
 |H^+|=1900+911+128=2939.
\]

The two families are rank-disjoint, so they require `48271` distinct short
cells if no upper provider is repaired.  Since the word has `48625`
singleton/pair cells, the exact remaining scalar reserve is

\[
 48625-48271=354.
\]

Equivalently,

\[
 a+|H^+|=4108+2939=7047\le7401.
\]

This is a necessary count only.  Here auxiliary loss means distinct short
intervals made unavailable without discharging a charged target.  It
neither supplies candidate cells nor proves Hall or cap compatibility.
Repairing one upper target returns one unit only if the direct-facet count,
all other upper holes, and auxiliary loss stay fixed.

## 6. Audit of the common-cap master

After `Z` and all provider positions are fixed, assume the fixed prepins are
already jointly cap-compatible and their occupied cells are removed from
the unused-cell set or included in its capacity rows.  The rank-three
obstruction theorem then depends only on the fact that variable cells are
singletons or adjacent pairs; it does not depend on target rank.  It
therefore remains valid when the short-target family is enlarged by the
upper masks in `H^+`.

The exact integral system is:

1. one candidate per short target;
2. at most one target per short cell; and
3. one exclusion inequality for every minimal empty-position, row-bit,
   prepin-bit, or selected-anchor-bit obstruction.

At most three short cells meet a position, and a selected pair anchor needs
at most two other cells to block both of its positions.  Hence every
minimal obstruction has size at most three.  Conversely, every failed
maximal-cap equation contains one of these minimal obstructions.  The
system is therefore necessary and sufficient after `D2` inversion.

Ordinary Hall alone is not sufficient.  A guarded permanent-bit/host
subgraph can reduce the exact system to Hall, but no such guarded subgraph
is asserted for this artifact.

If socket or provider positions remain variable, the rank-three conclusion
does not apply unchanged; the outer model can contain rank-four
obstructions.

## 7. Scope corrections

The following implications are **unsupported** and are not made in the
audited theorem:

* scalar slack `3293` implies a common cap;
* owner/lower-`q1` connectivity implies residence or physical upper
  coverage;
* the old `39cc3abe...` cycle's numerical no-gos transfer to this cycle;
* fixed-depth owner shadows equal arbitrary physical interval shadows; or
* failure of this one zipper obstructs regenerated component variants,
  partial-macro rethreads, compound actuators, or a nonflat compiler.

Another residual pairing of the **same fixed component words** is excluded,
but only by the separate `724`-run internal-component theorem; it is not a
consequence of the one saved ordering alone.

The precise proved boundary is: the displayed quotient and lower palette
are complete, but its canonical marked/facet zipper fails an explicit
row-bit cut and `2939` long-upper provider rows.  Ranks `13` through `17`
have providers in this noninvertible row; every repair must preserve or
re-audit them.  After inversion and provider rows are repaired, the exact
remaining gate is the matching-plus-rank-three common-cap system.
No `K17` word and no claim about `nu(17)` follows.
