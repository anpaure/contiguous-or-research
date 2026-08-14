# The tapped marked-C6 D5 reset has a direct-graft collar obstruction

**Date:** 2026-08-14  
**Status:** exact symbolic local obstruction plus corrected architecture
reduction.  The minimal marked-C6 box realizes both D5 terminal metric types
internally, but every hard distance-two row violates its phase-common direct
graft collar.  A separate two-channel resident cable or a tapped
multi-boundary collar is genuinely required.  Simultaneous cable planting is
not proved here.

## 0. Outcome

The 18-owner marked-C6 router has a rank-seven hard terminal model

\[
 B=A_0,\qquad C=Q_{1,1},\qquad
 T=(K-x_2)+z+a_0+a_1,                                \tag{0.1}
\]

whose marked first return is the desired head transposition.  Metric
compatibility alone, however, is insufficient for a source graft.

At the hard row, write

\[
 H=T\cap B\cap C,qquad
 T=H+a_0+a_1,qquad B=H+x_2+a_0,qquad C=H+y_2+a_1. \tag{0.2}
\]

The direct terminal edges have exchange supports

\[
                    \operatorname{supp}(TB)=\{x_2,a_1\},
 \qquad             \operatorname{supp}(TC)=\{y_2,a_0\}.      \tag{0.3}
\]

In every coordinate relabelling of the hard tapped template, the singleton
cells `B-(T union C)` and `C-(T union B)` are respectively the router clock
labels `x_2` and `y_2`.  But the phase-common marked-C6 cut has internal
collar pools containing those same clock labels.  Its proved sufficient
graft condition requires the first two and last two exterior exchange
supports to avoid the whole clock set

\[
                         \{x_1,x_2,y_1,y_2\}.                   \tag{0.4}
\]

Equations `(0.3)--(0.4)` contradict one another.  Therefore no direct graft
of the tapped hard template at the prescribed `TB,TC` incidences satisfies
the phase-common collar theorem, independently of all choices of the other
clock/core labels.

The exact frozen census confirms this for every hard row:

\[
                 164/164\text{ hard rows fail},\qquad
                  48/48\text{ adjacent rows pass the clock-cell capacity
                  precheck}.                                   \tag{0.5}
\]

Thus the tapped construction removes the metric-terminal obstruction but
not the occurrence-history obstruction.  The two facts are complementary,
not contradictory.

## 1. Symbolic proof of the hard-row obstruction

In the hard tapped model, the owners from the marked-C6 formula are

\[
 A_0=K+z+a_0,qquad
 Q_{1,1}=(K-x_2)+y_2+z+a_1,                         \tag{1.1}
\]

and the displayed tail is

\[
 T=(K-x_2)+z+a_0+a_1.                              \tag{1.2}
\]

Put `H=(K-x_2)+z`.  Then `(1.1)--(1.2)` are exactly `(0.2)`.  Consequently
`x_2` and `y_2` are not freely assignable spare labels after the terminal
triple is fixed: they are the two prescribed singleton Venn cells of that
triple.

The direct edge `T--B` exchanges `a_1` for `x_2`, and `T--C` exchanges
`a_0` for `y_2`, giving `(0.3)`.  Hence any exterior collar that begins or
ends with the two prescribed terminal edges necessarily meets the internal
clock set `(0.4)`.  The two-move collar guard fails already on its first
move.  Enlarging the ambient rank or relabelling the common core cannot
alter this forced-cell identity.

This proves an obstruction to the **declared phase-common cut and its collar
criterion**.  It is not an architecture-free no-go: another tapped boundary
phase with a different exact mixed-collar proof, or a resident transition
cell absorbing the forced supports, may still work.

## 2. Why the adjacent type is different

For the adjacent tapped model

\[
             B=A_0,qquad C=A_1,qquad T=K+z+f_0,              \tag{2.1}
\]

the terminal Venn signature has enough nonforced common/exterior cells to
choose the four clock labels away from the direct terminal supports.  The
finite precheck therefore finds no corresponding capacity contradiction on
any of the 48 rows.

This is only a local feasibility statement.  It does not prove a
simultaneous resource-simple choice of all adjacent boxes or any actual
crossing q2 current.

## 3. Corrected hard-row route: the resident two-channel cable

For one hard triple, choose a common Johnson neighbour `E` of `B,C` other
than `T`.  Then both `B--E` and `C--E` are Johnson adjacencies.

1. Use `B,E` as the internal marked router sockets.
2. Use the six-owner resident cable as a prospective transition cell.  Its
   direct edge and complementary five-edge return display the two distinct
   channel arcs needed to relocate an internal socket.
3. Perform only ordinary degree-two edge splices.  If `PQ` is a
   phase-common router cut and `XY` a cut on a disjoint cable/exterior
   component, delete `PQ,XY` and insert one of the legal cross pairings
   `PX,QY` or `PY,QX`.  A serial cable needs two such splices, one at each
   end.  No owner is identified and no edge is traversed twice.

The union of two closed cycles sharing `E` is **not** the construction: it
would give `E` degree four.  Likewise, the common label `E` in a normalized
menu is not a licence to reuse that owner occurrence.  A physical package
must choose owner-disjoint copies and prove that all four added cross edges
are Johnson edges.

The independently audited rank-seven search proves that, for every one of
the three choices of the normalized endpoint `E`, cable and router interiors
can be selected so that they share only that normalized boundary owner and
their lower-q1, upper-q1, lower-q2 and upper-q2 decks are otherwise
disjoint.  This was a useful menu witness but was not itself the physical
owner-disjoint splice.

A subsequent H100 search has now found one literal owner-disjoint package:
an 18-owner router, one six-owner cable, and two ambient exterior six-cycles
are joined by three ordinary two-edge splices.  It has 36 distinct owners,
simple lower/upper q1 palettes, 36 distinct values on each q2 row, zero q2
occurrence current, and residence minima `(3,3)` and `(4,2)`.  The old
components of lengths `6,12,18` become one component of length `36`; after
hiding the auxiliary port, the external action is the required head
transposition.  That positive local package supersedes the merely normalized
shared-`E` menu.  Its literal formula and H100 provenance are frozen in
`MATH_THEOREM_D5_OWNER_DISJOINT_THREE_SPLICE_RESIDENT_RESET_PACKAGE_20260814.md`.
That theorem settles the closed local splice atom, including every mixed
window at its three ordinary splices.  It does not settle the later cut-open
graft to the actual D5 neighbors, q1 refill, or global traversal.

## 4. Exact global compilation gate

The hard D5 route has a finite resource-selection row, but is not merely a
package-selection problem.  The positive 36-owner splice witness first asks
for a relabelled copy at each hard occurrence.  For each of the 164 rows,
select

\[
                   (E,\text{cable phase},\text{router phase},
                         \text{clock/core relabelling})                \tag{4.1}
\]

so that:

1. the three-splice package has degree two at every owner;
2. its owner, lower-q1 and upper-q1 resources are simple, except for the
   declared boundary occurrences;
3. its complete lower/upper q2 occurrence currents are support-monotone;
4. every owner and immediate-upper run across a graft meets the depth-two
   residence bound; and
5. packages are mutually resource-compatible and compatible with the
   frozen D5 factor; and
6. cut-open in/out darts reconnect to the literal D5 strands, refill every
   removed q1 incidence, and suppress to the required global component
   traversal.

The 48 adjacent rows may use the tapped direct model or the same cable
interface.  In the **rowwise terminal architecture**, all 212 rows still
require one simultaneous selector as the first resource row, followed by
the cut-open boundary compilation and global traversal.  The count `212`
is fixed for the finite D5 reset;
hence any successfully selected joint bank has `O(1)` edges, is
`2^{o(m)}`, and has `o(m)` exposure after a common-core lift.  It then falls
inside the subexponential low-exposure coinstantiation theorem for all
sufficiently large ambient ranks.  The missing statements are the literal
resource-compatible selector, the physical boundary compiler, the complete
q1 refill and the final topology audit (plus finitely many small ambient
bases), not the asymptotic residual two-factor extension.

There is a distinct global architecture.  The complete 477-token D5 head
permutation has a minimum factorization into 226 three-cycles.  Using full
C6 routers removes the fixed-tail and per-row hard-collar requirements
algebraically, but instead requires 678 ordered serial attachments on the
logical head strands, with Johnson cross collars, exact q1 refill, mutually
simple typed palettes, crossing residence and a final `372 -> 1` traversal.
The present direct-graft obstruction chooses neither architecture; it only
rules out the canonical rowwise tapped collar.

## 5. Scope

The following facts are now exact.

* Minimal marked-C6 router topology: solved.
* Both D5 terminal metric signatures inside the router: solved individually.
* Direct hard-terminal graft using the current phase-common collar: ruled
  out on every hard row.
* Resource-compatible resident cable/router interiors: solved individually.
* One physical owner-disjoint crossing package with zero q2 current and
  q2 residence: solved by a separate audited and frozen local theorem.
* Simultaneous 212-row planting in the rowwise architecture: open.
* The alternative minimum 226-router global atlas: algebraically reduced,
  with its physical strand/collar/palette compiler open.

No all-width exterior transparency or all-semilength suffix grammar is
claimed.

## 6. H100 provenance for the 164/48 census

The census `(0.5)` is bound to the following exact H100 replay.  Its output
records the `48/164` row-kind histogram, `164` collar-infeasible rows, and a
provably smallest one-row hard core at row `0` / source row `1`.  The two
forced deficient cells are `010` at coordinate `0` and `001` at coordinate
`13`, exactly the `x_2,y_2` obstruction in `(0.2)--(0.4)`.

```text
4e9b4932036f8bf89c51fd9973e0802925cffd2e7ead9ac69f3b8e9ea15bf654
  scratch/solve_d5_tapped_c6_212_coinstantiation_20260814.py
fd6b96e1f5578d1c8f39382d13d4475a1ffe23e2b24f052bb2dedcd0330d2b9b
  scratch/solve_d5_tapped_c6_212_coinstantiation_full_20260814.h100.out
```

This binds the finite census only.  The symbolic proof in Section 1 is the
reason the one-row core applies to every hard row and to every coordinate
relabeling of the declared phase-common collar.
