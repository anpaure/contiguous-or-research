# Endpoint-planted coatom tensors: four exact schedules and the fixed-slot Hall gate

Date: 2026-08-01  
Status: exact row-1 local correction and exact task/slot quantifier theorem  
Scope: the mixed coatom tensor and its owner-private placement face; not a
proof of `nu(k)<=B(k)+O(1)`

## 0. Outcome

The zero-owner-defect coatom tensor remains valid, but the original-owner
planting in Section 8.5 of
`MATH_THEOREM_INDEPENDENT_ECO_COATOM_SCREEN_TENSOR_AND_FOUR_DUPLICATE_GATE_20260801.md`
needs one correction if the immediate lower palette is part of the packet
interface.

Write the residence depth as `D`, put `n=D+2`, and write

\[
 F=F_0\sqcup\{p\},\qquad
 F_0=\{g_0,\ldots,g_D\},\qquad K=G-F_0.                 \tag{0.1}
\]

The published first-block order

\[
 C_p,C_{g_0},\ldots,C_{g_D}                              \tag{0.2}
\]

with transition zero lower preserves the owner, OR-deck, topology and
residence rows, but it does **not** preserve the immediate lower-colour
counter.  None of the eight transition-zero-lower simple screen schedules
passes that row.

There is a zero-cost repair.  Use

\[
 C_p,C_{g_1},\ldots,C_{g_D},C_{g_0}                      \tag{0.3}
\]

in the first block, leave the other eleven coatom orders standard, and make
transition zero an upper screen.  Exactly four screen schedules then pass
all of the following simultaneously:

* literal simple Johnson topology and equal owner set;
* the original all-six endpoint pair;
* pointwise equal prefix/suffix OR chains;
* equal internal interval-OR support;
* all-depth residence and equal clipped boundary state; and
* equal immediate intersection and union counters.

The four upper-screen index sets are

\[
\begin{split}
 &\{0,2,4,6,8,10\},\\
 &\{0,2,3,4,6,8,10\},\\
 &\{0,2,4,5,6,8,10\},\\
 &\{0,2,3,4,5,6,8,10\}.                                \tag{0.4}
\end{split}
\]

Thus the fully immediate-palette-valid planting factor is `4`, not `8`.
The old factor `8` remains a count of distinct owner/upper/residence slots
when the immediate lower row is omitted.

There is a second, independent quantifier correction.  Quadratically many
active relabellings are quadratically many **candidate-dependent planted
slots**.  A fixed incumbent owner slot admits at most one of them.  The
right global condition is therefore Hall on actually prepared private
owner-halo slots, not Hall on formal `(c,d)` labels.

## 1. Why the lower-screen endpoint rotation loses lower `q1`

The active endpoints of row 1 are

\[
 V_0=\infty ab,\qquad V_{11}=eab.                         \tag{1.1}
\]

At transition zero the old and new departing intersections are respectively

\[
                         I^0=\infty b,\qquad I^1=\infty a.\tag{1.2}
\]

Suppose the first coatom block starts at `C_p`, so its first owner is the
literal old endpoint `G union V_0`.  If transition zero is lower and the
simple block ends at `C_q`, then `q in F_0`; it cannot end at `C_p` without
repeating its first owner.  The two immediate intersection colours incident
with the lower screen are

\[
 K\cup I^\epsilon\cup(F-\{q\}),\qquad
 K\cup I^\epsilon\cup(F-\{g_0\}).                         \tag{1.3}
\]

For the unrotated block the first value in (1.3) has missing filler `p`.
The common active screen-palette identity matches that value at the other
occurrence of `I^epsilon`.  Replacing `p` by `q` leaves a new filler-profile
class.  Since \(I^0\ne I^1\), the two new rank-`r-1` values cannot cancel
between phases.  Hence lower-counter equality would force `q=p`, which is
incompatible with a simple block beginning at `C_p`.

The independent audit checks the complete eight-pattern face and obtains
zero lower-counter passes for every `0<=D<=12`.

## 2. The repaired upper-rooted planting

### Theorem 2.1

For every `D>=0` and every target rank for which the coatom tensor is
defined, the first-block order (0.3), standard orders in the other blocks,
and any schedule in (0.4) give a pair of simple rank-`r` Johnson paths with
all six rows listed in Section 0.

#### Proof

Every two distinct coatoms are Johnson adjacent.  The final first-block
owner in (0.3) omits `g_0`.  At transition zero the upper screen omits
exactly `g_0,p` and adds the entering active coordinate.  Thus the left
Johnson step deletes `p` and adds that active coordinate.  The step from
the screen to the standard first owner of block one adds `p` and deletes
the departing active coordinate.  All later steps are the already proved
mixed-screen tensor steps.

The first owner omits `p`, so it is `G union V_0`; the standard final block
ends at `C_p`, so the last owner is `G union V_11`.  Reordering a block does
not change its owner set.  Each schedule in (0.4) belongs to the finite
sixteen-pattern simple common-screen table, hence the two phases have the
same distinct physical owner set.

The first block and its order are common to the two phases.  Prefix and
suffix unions therefore change in the same positions.  At the upper screen,
the active prefix advances through `V_1` and the active suffix begins at
`V_0`; the contracted row-1 prefix and suffix identities apply.  Inside one
coatom block a singleton sees its coatom and every interval of length at
least two fills `F`, independently of the coatom permutation.  The standard
lower/upper-screen decomposition therefore proves the same internal
interval-OR support in the two phases.

Residence is symbolic in `D`.  Coordinate `p` is absent in the first owner
and at the transition-zero upper screen; the intervening positive run has
length `n-1=D+1`.  Coordinate `g_0` is absent in the last first-block owner,
the upper screen, and the first next-block owner, so these consecutive zeros
create no short positive run.  For `1<=i<=D`, the run between its zero in
the first order and its zero at position `i` of the next standard block has
length

\[
                         (n-1-i)+1+i=n.                    \tag{2.1}
\]

All subsequent filler gaps have the original lower bound `n-1`, and every
active run contains a whole length-`n` block.  The two endpoint blocks are
common, so the clipped boundary states agree.

It remains only the six-coordinate immediate-palette row.  Exhausting the
sixteen simple common-screen schedules gives exactly (0.4).  This is a
finite active identity independent of `D`; filler profiles merely tensor
it with common sets.  The audit checks it literally for `0<=D<=12`.
\(\square\)

## 3. Exact active-label count and fixed-slot uniqueness

Fix the endpoint masks, `K`, and `F`.  Equivalently in the planted notation,
fix `G,F_0,p`.  The endpoints determine

\[
 e=R-L,\qquad \infty=L-R,\qquad
 \{a,b\}=(L\cap R)-G.                                    \tag{3.1}
\]

Swapping `a,b` interchanges the old and new active words, so it does not
give a second reversible packet.  Put

\[
 {\cal R}=\Omega-\bigl(G\cup\{p,e,\infty,a,b\}\bigr),
 \qquad q=|{\cal R}|=|\Omega|-r-2.                       \tag{3.2}
\]

The roles `c,d` are ordered and distinct.  Hence one fixed screen schedule
has exactly

\[
                              q(q-1)                       \tag{3.3}
\]

formal active relabellings, and the corrected four-schedule atlas has

\[
                              4q(q-1)                      \tag{3.4}
\]

formal endpoint-compatible tensors.

### Proposition 3.1 (owner injectivity)

A literal incumbent owner slot determines `(c,d)` and its screen schedule.
Distinct active pairs differ in at least `3(D+2)` block owners.

#### Proof

For an active triple `V`, the planted block-owner set is

\[
 \{G\cup V\}\ \cup\
 \{(G-\{g\})\cup V\cup\{p\}:g\in F_0\}.                 \tag{3.5}
\]

Stripping the fixed core/filler data from the twelve blocks recovers the
active triple set.  Among its two free labels, `c` is the unique one which
occurs in a triple containing `infinity`; `d` is the other.  More
quantitatively, changing `c` removes the three triples

\[
             \infty bc,\quad\infty ca,\quad\infty ec,     \tag{3.6}
\]

while fixing `c` and changing `d` removes

\[
                       ead,\quad ebd,\quad ecd.            \tag{3.7}
\]

Each active triple owns `n=D+2` distinct coatom owners, proving the distance
claim and injectivity.

In an ordered slot, a screen's filler deficit records lower versus upper at
each transition and hence recovers the schedule.  Even after forgetting
order, the four schedules in (0.4) have distinct screen-owner fingerprints,
as the audit checks.  Thus a fixed owner slot contains one reversible tensor
or none after the external guards are imposed. \(\square\)

This is the task/menu quantifier which the raw local count does not supply.
For a fixed active all-six atom, varying `F_0`, `p`, and the old eight screen
patterns produced

\[
                         8P{r-3\choose D+1}.               \tag{3.8}
\]

distinct parameterized planted slots.  The choices are recoverable from
their block owners, so (3.8) is not multiplicity inside one incumbent slot.
After requiring the immediate palettes and using Theorem 2.1, the corrected
count is

\[
                         4P{r-3\choose D+1}.               \tag{3.9}
\]

If the fresh-`p` pool and active-label reservoir are disjoint, (3.9) may be
multiplied by `q(q-1)`.  If they are the same pool, one must instead sum the
available `q_p(q_p-1)` over `p`; multiplying independent marginal counts
would overcount collisions.

## 4. The exact private planted-slot Hall theorem

Let `T` be a finite bank of occurrence-labelled repair tasks.  Let `S` be a
bank of **actually prepared atomic slots**.  A slot includes its ordered
owner word, boundary owners, full affected-occurrence halo, palette and
topology tickets, and every compiler resource used by its U5 certificate.
Assume distinct slots have disjoint interiors and disjoint full halos, with
any shared boundary capacity written explicitly.

By Proposition 3.1, each slot has at most one coatom tensor label.  Define a
bipartite graph

\[
                         \Gamma=(T,S;E)                    \tag{4.1}
\]

by joining task `tau` to slot `s` exactly when that unique tensor repairs
`tau` and every literal owner, palette, residence, topology and U5 guard
passes.

### Theorem 4.1 (atomic-slot Hall criterion)

Under the private-halo hypothesis, all tasks can be repaired simultaneously
if and only if

\[
                 |N_\Gamma(X)|\ge |X|
                 \qquad\text{for every }X\subseteq T.      \tag{4.2}
\]

With integral slot capacities `b(s)`, replace the left side by
\(\sum_{s\in N(X)}b(s)\).

#### Proof

Necessity is Hall's cut.  Conversely, (4.2) gives a task-saturating matching.
Each matched edge names one literal guarded tensor in one prepared slot.
Owner equality preserves that slot's owner bank, and the private full halos
make all chosen switches commute.  Therefore the matching materializes all
repairs.  The capacitated statement follows by cloning slots. \(\square\)

Private atomicity is essential.  If candidates carry overlapping multi-owner
halos, candidate identities are hyperedges, not unit Hall representatives.
The exact feasibility system is then

\[
 \sum_{q\in A_\tau}x_q=1,
 \qquad
 \sum_{q:h\in H(q)}x_q\le1,
 \qquad x_q\in\{0,1\}.                                  \tag{4.3}
\]

Ordinary Hall on the formal candidate labels is not sufficient for (4.3).
For example, two tasks may each have two labelled candidates while all four
candidate halos contain one capacity-one owner.  Candidate-count Hall passes,
but no pair is compatible.  Thus a quadratic formal `(c,d)` atlas becomes a
quadratic usable menu only after a private planted-slot theorem, or after a
stronger exact hypergraph/matroid certificate for the actual owner halos.

## 5. Exact same-parity template lift and its boundary debt

The planted template has an exact algebraic lift through both possible
depth transitions.  It is not, however, boundary-state neutral in the
depth-jump branch.

### Theorem 5.1 (no-jump cone)

If the required residence depth stays \(D\), add the new coordinate \(z\)
to \(G\) and \(K\), leaving \(F_0,F\) and every coatom order unchanged.
Every child owner and screen is exactly its parent value union \(\{z\}\).
Consequently:

* both immediate colour counters are the cones of the parent counters;
* every prefix, suffix and internal interval OR is the cone of its parent;
* every old-coordinate trace and boundary profile is unchanged; and
* \(z\) is present throughout the fragment and has zero exterior demand.

#### Proof

Every formula for a block owner or screen contains \(K\).  Replacing \(K\)
by \(K\cup\{z\}\) therefore cones every displayed set.  Intersection,
union, adjacency, owner equality and every old-coordinate trace commute
with this common coning. \(\square\)

### Theorem 5.2 (depth-jump insertion)

If the required residence depth grows from \(D\) to \(D+1\), put

\[
 G'=G\cup\{z\},\qquad F'_0=F_0\cup\{z\},\qquad
 K'=K,\qquad F'=F\cup\{z\}.                              \tag{5.1}
\]

Use the special first-block missing-label order

\[
                 p,g_1,\ldots,g_D,z,g_0                  \tag{5.2}
\]

and the standard order

\[
                 g_0,g_1,\ldots,g_D,z,p                  \tag{5.3}
\]

in every other block.  This is uniform insertion immediately before the
last old coatom, at zero-based index \(n-1\) in every parent block of length
\(n=D+2\).

Let \(\iota(W)=W\cup\{z\}\) after the harmless coordinate-index insertion.
Every old screen becomes \(\iota(S)\).  If a parent block on active triple
\(V\) is

\[
                         L_0,\ldots,L_{n-1},              \tag{5.4}
\]

then its child block is

\[
 \iota(L_0),\ldots,\iota(L_{n-2}),
 N_V,\iota(L_{n-1}),
 \qquad N_V=K\cup V\cup F.                               \tag{5.5}
\]

The twelve \(N_V\) are new, pairwise distinct owners and are the only child
owners not containing \(z\).  The child tensor is again simple, owner-exact
between phases, upper-transparent, immediate-palette-exact, and internally
resident at depth \(D+1\).

#### Proof

Equation (5.5) follows by writing the new coatom missing \(z\); every old
coatom and every screen contains \(z\).  The fresh owner lies between two
coned old coatoms and is Johnson adjacent to each.  The active owner set is
common to both phases, so the twelve fresh owners are common and distinct.

At each insertion, a parent seam \(LR\) is replaced by

\[
                         \iota(L),N_V,\iota(R).            \tag{5.6}
\]

On immediate intersections this removes \(\iota(L\cap R)\) and adds the two
mapped old owners \(L,R\).  On immediate unions it replaces one copy of
\(\iota(L\cup R)\) by two copies.  The parent block-owner set is common to
the two phases, so these twelve corrections have the same counter in both
phases.  Every unsplit seam is simply coned.  Hence both immediate counters
remain equal.

An interval not containing \(z\) can contain only one fresh owner, since
all fresh owners are separated by coned owners or screens.  Every interval
containing \(z\) contracts across the inserted \(N_V\) values to a parent
interval with the same OR before coning.  Therefore the child internal
support has the exact decomposition

\[
 {\cal I}_\vee(\text{child})
  =\{\iota(U):U\in{\cal I}_\vee(\text{parent})\}
    \sqcup\{N_V:V\in{\cal V}\}.                           \tag{5.7}
\]

This proves upper support and also makes the prefix/suffix transport
literal.  For residence, every old filler insertion contains all old filler
coordinates, so it can only lengthen their positive runs.  Coordinate \(z\)
is absent once in every block and present at every screen; consecutive
zeros are separated by at least \(D+2\) positives.  Active coordinates
still occupy a whole block. \(\square\)

The exact boundary profiles reveal the remaining regeneration issue.  Write
\((\lambda_x,\rho_x)\) for the leading and trailing positive-run lengths.
At parent depth \(D\), the old filler profiles are

\[
\begin{array}{c|c}
 x&(\lambda_x,\rho_x)\\ \hline
 g_0&(D+1,D+1)\\
 g_i,\ 1\le i\le D&(i,D+1-i)\\
 p&(0,0).
\end{array}                                                \tag{5.8}
\]

After the jump they are

\[
\begin{array}{c|c}
 x&(\lambda'_x,\rho'_x)\\ \hline
 g_0&(D+2,D+2)\\
 g_i,\ 1\le i\le D&(i,D+2-i)\\
 p&(0,0)\\
 z&(D+1,1).
\end{array}                                                \tag{5.9}
\]

Measure exterior demand against threshold \(D+1\) in the parent and
\(D+2\) in the child, assigning demand zero when the boundary bit is zero.
Then:

* every old \(g_i\) with \(1\le i\le D\) gains exactly one unit of left
  demand;
* every old filler right demand is unchanged;
* \(g_0\) and \(p\) acquire no old-coordinate demand; and
* fresh \(z\) has left demand \(1\) and right demand \(D+1\).

Thus the proposed insertion cones all old screens and owners and preserves
all internal rows, but it does change old filler exterior demand.  A
same-parity regeneration theorem must co-lift the left exterior so that it
supplies these \(D\) units, or carry a boundary state which records them.
The local tensor alone does not give bounded-state regeneration across a
depth jump.

## 6. Exact scope

Theorem 2.1 repairs the endpoint planting and Proposition 3.1 settles its
fixed-slot quantifier.  They do not construct the required family of
prepared slots in a Pascal child, prove U5 for those slots, or regenerate
the family under `k -> k+2`.  Those remain the three global gates.  In
particular, this note does not turn a local quadratic relabelling count into
an additive-constant theorem.

The finite active audit is row-1-specific.  Relabelled cyclic copies are
available, but no multiplicative row factor is included in (3.3)--(3.9).

## 7. Independent audit

Run

```bash
python3 scratch/audit_coatom_endpoint_planting_fixed_slot_hall_20260801.py
```

It reconstructs the active connector without importing repository code or
JSON, exhausts all `2^11` screen choices to recover the sixteen simple
common-screen patterns, and checks every `0<=D<=12`.  In every depth, all
eight transition-zero-upper schedules pass U1--U4 and exactly the four in
(0.4) also pass both immediate counters.  The superseded lower-screen
rotation has zero lower-counter passes among its eight patterns.  A separate
four-label calibration verifies `q(q-1)` distinct active owner sets and
minimum active-triple loss three.  It also checks both same-parity lifts for
all four valid schedules and both phases.  In the jump branch it materializes
the twelve fresh owners, verifies the exact seam-counter and interval-support
transfer, and records every boundary profile in (5.8)--(5.9).

Artifacts:

```text
scratch/audit_coatom_endpoint_planting_fixed_slot_hall_20260801.py
  370d3735262ccc9110ac38b3890f5927db0a1a433dffa4fe1be5d232b41e90a9
scratch/coatom_endpoint_planting_fixed_slot_hall_20260801.audit.json
  fab9bd2eeb3e68917951e41218f22c040ea1dbba57f92602605bf65fa0d3307d
canonical payload
  8f5886485a59097b7904b38e2add9880ea21cb266b4d3be7bb559e69552d619c
```
