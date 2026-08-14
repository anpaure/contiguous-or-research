# Hostile audit of the tapped marked-C6 direct-graft collar obstruction

**Date:** 2026-08-14

**Audited source:**
`MATH_REDUCTION_D5_TAPPED_MARKED_C6_DIRECT_GRAFT_COLLAR_NOGO_AND_CABLE_GATE_20260814.md`

**Verdict:** **PASS in its exact canonical-collar scope.**  Every hard
distance-two terminal triple forces the two marked-C6 clock roles `x2,y2`
into singleton Venn cells used by the prescribed direct terminal edges.
Those edges therefore violate the sufficient two-move collar guard at the
canonical phase-common `P_(i,2)--Q_(i,0)` cut under every coordinate
relabeling.  This is not an architecture-free residence no-go: a different
cut with a new mixed-collar proof, the audited owner-disjoint three-splice
package, or the separate global 226-router architecture may escape.  The
frozen census supports exactly `164` hard capacity failures and `48`
adjacent rows with no clock-cell capacity deficit; it does not claim 48
feasible protected-halo menus.

## 1. Forced-cell proof

For the hard tapped terminal, the marked-C6 formula gives

\[
\begin{aligned}
 B&=A_0=K+z+a_0,\\
 C&=Q_{1,1}=(K-x_2)+y_2+z+a_1,\\
 T&=(K-x_2)+z+a_0+a_1.
                                                               \tag{1.1}
\end{aligned}
\]

Put `H=(K-x2)+z`.  Then

\[
 T=H+a_0+a_1,
 \qquad B=H+x_2+a_0,
 \qquad C=H+y_2+a_1.                                \tag{1.2}
\]

Direct subtraction now gives the two singleton cells

\[
 B\setminus(T\cup C)=\{x_2\},
 \qquad
 C\setminus(T\cup B)=\{y_2\}.                     \tag{1.3}
\]

The terminal edge supports are equally forced:

\[
 T\mathbin\triangle B=\{x_2,a_1\},
 \qquad
 T\mathbin\triangle C=\{y_2,a_0\}.                \tag{1.4}
\]

This is a Venn-cell statement, so an arbitrary coordinate relabeling of a
fixed hard triple can rename the labels but cannot move the `x2` clock role
out of cell `010` or the `y2` role out of cell `001`.  The two cells are
singletons for every equal-rank triple with hard signature
`(1,1,2,r-2,r+2)`; no spare coordinate in the same cell is available.

## 2. Exact collar scope

The previously audited marked-C6 theorem opens a port at the unchanged
central edge

\[
                         P_{i,2}--Q_{i,0}.           \tag{2.1}
\]

The two internal support pools adjacent to this cut are
`{x1,y1}` and `{x2,y2}`.  Its sufficient q2-residence theorem requires the
first two and last two exterior Johnson supports to avoid the whole clock
set

\[
                         \{x_1,x_2,y_1,y_2\}.        \tag{2.2}
\]

In the declared rowwise direct graft, the prescribed `T--B` and `T--C`
edges are terminal exterior moves.  By `(1.4)`, one contains `x2` and the
other contains `y2`.  Hence `(2.2)` fails on the first relevant move,
independently of all choices of `x1,y1`, common-core coordinates, or spare
labels.  Enlarging the ambient ground cannot split either singleton cell.

This proves only failure of the canonical cut `(2.1)` under guard `(2.2)`.
The guard is sufficient, not a characterization of every possible mixed
collar.  The source correctly leaves open a different tapped boundary phase
with a direct calculation, a resident transition cell, and a global
multi-boundary router atlas.

## 3. Adjacent type

In the adjacent tapped model

\[
 B=A_0,
 \qquad C=A_1,
 \qquad T=K+z+f_0,                                  \tag{3.1}
\]

the terminal edge supports use active labels `a0,a1,f0`, while the four
clock roles can occupy the common/all-exterior Venn cells.  There is no
forced singleton-clock collision analogous to `(1.3)`.  This establishes
only capacity of the Venn cells to place the clocks away from the direct
terminal supports.  Protected owner/q1/q2 halos, cross-edge legality,
palette refill, and simultaneous selection remain separate.

The source consistently uses this narrow wording: all 48 adjacent rows
pass the **clock-cell capacity precheck**, not the complete menu search.

## 4. Independent 164/48 replay

The frozen full output has 212 diagnostics with kind histogram

```text
adjacent       48
distance_two 164.
```

The standalone audit does not import or rerun the randomized menu builder.
It checks every diagnostic record and proves:

1. each of the 164 hard rows has exactly two deficits, cells `010` and
   `001`;
2. each deficient cell has required clock multiplicity one, one total
   coordinate, zero available coordinates, and that coordinate is guarded;
3. each of the 48 adjacent rows has no exact collar-capacity deficit; and
4. the first hard row, row `0` / source row `1`, is already a one-row core.

The full output has an empty final menu on all 212 rows because it also
imposes the large protected radius-two halo and samples finite relabeling
menus.  That stronger emptiness is not used to claim an adjacent no-go.

For the first hard row the deficient coordinates are literally `0` in cell
`010` and `13` in cell `001`, agreeing with the symbolic `x2,y2` roles.
Across all other hard rows the coordinate names vary but the two forced
cell types do not.

## 5. Escape statements and current references

The source's positive local reference is current.  The audited theorem

```text
MATH_THEOREM_D5_OWNER_DISJOINT_THREE_SPLICE_RESIDENT_RESET_PACKAGE_20260814.md
```

proves one 36-owner closed package for each terminal metric type, with 24
new cable/router owners relative to two assumed ambient C6 cycles, exact
local `(B U C)` action, zero typed q2 occurrence current, and closed-package
residence.  It still does not prove the cut-open D5 graft, crossing collars,
q1 refill, or simultaneous rowwise planting.

The source also correctly separates a second architecture: the exact
477-token head permutation has a minimum 226-three-cycle reduction.  Full
C6 routers remove the per-row tail and hard-collar use algebraically, but
the resulting 678 serial attachments still need ordered strand cuts,
Johnson cross edges, q1 refill, typed-palette simplicity, crossing
residence, and the final `372 -> 1` traversal.

Thus the direct obstruction is neither contradicted nor made universal by
the two escapes.  It eliminates one precise rowwise collar implementation.

## 6. H100 hashes

All hashing and the standalone replay ran through `ssh h100`.

| artifact | H100 SHA-256 |
|---|---|
| reduction source | `e425ed35fa0872420c9a739424472d3b395c207408647cda73c364139c374829` |
| original 212-row search/replay | `4e9b4932036f8bf89c51fd9973e0802925cffd2e7ead9ac69f3b8e9ea15bf654` |
| original full H100 output | `fd6b96e1f5578d1c8f39382d13d4475a1ffe23e2b24f052bb2dedcd0330d2b9b` |
| standalone census audit | `4e084331cf8508454ebf5c1e3bef5e6a0262c32dbd9a484b207958e4cdac75a0` |
| standalone H100 output | `4e383403357d25fa5c7bd101c6555667523ef0f528aef4286582bef33c6a67ba` |

The reduction, this audit, and the standalone verifier/output are safe to
freeze together in the stated scope.
