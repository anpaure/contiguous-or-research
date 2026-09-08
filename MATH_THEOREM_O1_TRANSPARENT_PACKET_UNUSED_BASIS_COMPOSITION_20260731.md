# Transparent packets over one unused compiler basis: a lean `B+O(1)` interface

Date: 2026-07-31  
Status: exact composition and conditional regenerative implication.  The
uniform packet-abundance and Pascal list-expansion hypotheses remain open.
No unconditional `nu(k)<=B(k)+O(1)` claim is made.

## 0. Outcome

Three exact interfaces remove the need to export a global upper-witness bank
or one complete common-cap augmenting path with every packet.

1. **Upper transparency.**  Old and new word fragments have the same
   coordinate entry/exit times, and every old internal union value reappears
   internally in the new fragment.
2. **Topology/residence transparency.**  The two fragments have the same
   typed boundary state; every local phase is residence-safe, and one common
   connector makes every allowed subset state a physical forest/path state.
3. **Compiler transparency.**  Fix one trace-guarded compiler matching
   `M_0`.  Every packet deletes one distinct cell from the unused-cell bank
   `B=C-cells(M_0)` and preserves all incidence guards used by `M_0`.

Under these conditions compatible packets compose literally.  Crossing
upper intervals are unchanged, internal old values are recreated locally,
the physical state remains legal by the common boundary certificate, and
the same compiler matching `M_0` survives every packet selection.

The only global selection rows left are therefore:

* disjoint/boundary-compatible physical packet supports; and
* distinct representatives in the unused-cell bank `B`.

This is strictly leaner than attaching arbitrary protected-witness and
common-cap path tickets to every C6 option.

## 1. Packet data

Fix a baseline physical word or owner chronology `A`.  A task `i` has a
position interval `J_i` and a list of options `a in P_i`.  Its old fragment
is `X_i=A[J_i]`; option `a` replaces it by an equal-length fragment
`Y_(i,a)`.

Assume the packet intervals are position-disjoint after the declared
conflict relation is enforced.  For a fragment `X`, let

\[
 \Sigma(X)=\left(
   (\bigcup_{t\le j}X_t)_j,
   (\bigcup_{t\ge j}X_t)_j
             \right),
 \qquad
 \mathcal U(X)=\{\bigcup_{t=p}^qX_t:p\le q\}.        \tag{1.1}
\]

Equivalently, `Sigma(X)=Sigma(Y)` iff every coordinate has the same first
and last occurrence position in `X` and `Y`.

Fix also one target-saturating matching `M_0` in a trace-guarded compiler
graph `H=(L,C;E)`, and put

\[
                         B=C-\operatorname{cells}(M_0).           \tag{1.2}
\]

The set `B` is a basis of the dual transversal matroid `M_H^*`.

An option `(i,a)` is **fully transparent over `(A,M_0)`** when:

1. `Sigma(X_i)=Sigma(Y_(i,a))`;
2. `mathcal U(X_i) subseteq mathcal U(Y_(i,a))`;
3. its internal coordinate runs are legal, and its boundary run state agrees
   with that of `X_i`;
4. it has the same typed physical boundary as `X_i`, and belongs to one
   declared common-connector forest cube;
5. it names a cell `b_(i,a) in B` which is deleted by this option; and
6. every selected incidence of `M_0` remains present and individually
   trace-guarded after the local replacement.

For a reversible cube replace the inclusion in item 2 by equality.  If
lower intersection shadows must also be transparent rather than recompiled,
apply items 1--2 to the coordinatewise complements as well.

## 2. Exact composition theorem

### Theorem 2.1 (transparent unused-basis composition)

Choose one fully transparent option from each of some task set `S`.  Suppose

1. their packet intervals/supports are mutually compatible in the declared
   common-connector forest cube; and
2. the cells `b_(i,a_i)`, `i in S`, are distinct.

Then all chosen options may be applied simultaneously, with the following
properties.

* Every interval-union value present in `A` is still present.
* Every coordinate run crossing a packet boundary is unchanged, and every
  internal run is legal.
* The resulting physical support has the declared topology.
* The original matching `M_0` still saturates every compiler target.
* Its maximal common cap is exact.

#### Proof

Apply the packets sequentially.  Equality of `Sigma` preserves every
interval crossing the current packet at the same address.  Internal
dominance recreates every old value wholly inside it.  Disjointness keeps
later packet addresses fixed, so induction preserves the complete old upper
support.

The first/last occurrence characterization of `Sigma`, together with item 3
of full transparency, preserves all boundary-crossing coordinate runs and
certifies the internal ones.  The common-connector cube gives the physical
topology for every subset state.

Every deleted cell lies in `B`, hence is unused by `M_0`; distinctness is
the natural deletion capacity row.  Item 6 says no used incidence or its
trace guard is changed.  Therefore the literal same matching `M_0` survives.
The trace-guarded compiler theorem promotes every saturating matching in
this bank—and in particular `M_0`—to an exact maximal common cap. \(\square\)

The theorem is one-way because coverage is one-way.  Extra upper values and
overcoverage are harmless.

## 3. Selection reductions

For task `i`, retain only its fully transparent options and join it to the
unused cell `b_(i,a)`.  If several options use the same unused cell they are
different realizations of one compiler representative.

### Corollary 3.1 (unused-bank Hall row)

If the task-to-unused-cell graph has a task-saturating matching and the
corresponding physical options can be chosen mutually compatible, then all
tasks compose by Theorem 2.1.

More generally, before fixing `M_0`, the exact row is the dual-Rado system

\[
 r_{M_H^*}\!\left(\bigcup_{i\in J}L_i\right)\ge|J|
 \qquad(J\subseteq I).                              \tag{3.1}
\]

After fixing `M_0`, ordinary Hall into `B` is a sufficient specialization.

### Corollary 3.2 (bounded-task greedy reset)

Suppose there are at most `H=O(1)` tasks, every list has at least
`alpha m^2` fully transparent options, and a fixed option conflicts with at
most `beta mD_m` options in any other list, including unused-cell collisions.
If

\[
                         \alpha m^2>(H-1)\beta mD_m,              \tag{3.2}
\]

then a compatible choice exists by greedy selection.  In particular this
holds eventually whenever `D_m=o(m)`.

### Corollary 3.3 (dispersed reservoir reset)

Suppose instead that the full option atlas has lists of order
`alpha m^2` and directed per-list row energy at most

\[
                              K D_m m^3.                           \tag{3.3}
\]

The sparse average-load extraction at density
`Theta(1/(D_m m))`, followed by per-list pruning and Haxell, supplies a
compatible unprescribed reservoir of order

\[
                              \Omega(W/D_m).                       \tag{3.4}
\]

This corollary constructs a reservoir.  Serving a prescribed leave still
requires a spread eligible task-to-anchor matching or planting the leave
jointly with the bulk.

### Theorem 3.4 (density-matched full reset; conditional)

Suppose a provisional child has `Theta(W)` elementary local failures, but
they are partitioned into

\[
                              H_m\le\gamma W/D_m                  \tag{3.5}
\]

compound collar tasks, each repaired by one macro changing `O(D_m)` seams.
Assume every task has at least `alpha m^2` fully transparent options and,
on the **actual prescribed task lists**, every list has average external
conflict at most

\[
                              K D_m m.                             \tag{3.6}
\]

Then all compound tasks have a simultaneous compatible repair for every
sufficiently large `m` whenever `D_m=o(m)`.

#### Proof

Apply per-list Markov pruning: delete options of degree greater than
`2K D_m m`, retaining at least half of each list.  The induced conflict
graph has maximum degree at most `2K D_m m` and every part has size at least
`alpha m^2/2`.  Haxell applies once

\[
                {\alpha m^2\over2}\ge4K D_m m,
\]

which holds eventually for `D_m=o(m)`.  The number of task parts does not
enter Haxell's inequality.  Theorem 2.1 composes the selected macros.
\(\square\)

The count (3.5) is the density match behind the buffered-hexagon proposal.
A canonical lift may need `Omega(W)` changed physical seams; this does not
contradict the theorem because `W/D_m` macros, each changing `Theta(D_m)`
seams, have total seam capacity `Theta(W)`.  Raw six-seam C6s without
buffering do not have this capacity.

For the natural deadline scale `D_m=d(k)=Theta(sqrt(m))`, both the number of
required macros and the compatible-reservoir scale are `Theta(W/sqrt(m))`.
What remains unproved is not the numerical supply but the prescribed-list
row (3.6), full transparency of each macro, and the compiler unused-prefix
condition.

## 4. Regenerative `O(1)` implication

Let `Phi` count every carried occurrence-labelled defect, including
topology and minimum-run debt.  Assume one bounded reachable sublevel
`Phi<=E` with a finite base state and, in every sufficiently large odd
step, a prospective Pascal lift satisfying:

1. at most four child tasks per carried token plus three absolute newborn
   lower tasks;
2. only an absolute number of structural seams;
3. fully transparent option lists satisfying Corollary 3.2;
4. a trace-guarded matching `M_0` whose unused bank satisfies the Hall row;
   and
5. after the selected packets are applied, the exported state again has
   `Phi<=E`, while odd/even terminal words have bounded repair complexity.

### Theorem 4.1

These hypotheses imply

\[
                              \boxed{\nu(k)\le B(k)+O(1)}.         \tag{4.1}
\]

#### Proof

The exposure row bounds the number of tasks by `4E+O(1)`.  The ECO seam and
compound-collar theorem keeps the selector at this task granularity.
Corollary 3.2 and Theorem 2.1 construct a legal successor for all sufficiently
large dimensions; hypothesis 5 keeps the induction inside the same bounded
sublevel.  The bounded-defect odd-spine theorem compiles odd and even
terminal words and pays each bounded terminal repair only in its own
dimension.  Finitely many initial dimensions change only the final absolute
constant. \(\square\)

## 5. Exact remaining construction theorem

The proved implication isolates one concrete positive target.

> **Prospective transparent unused-basis packet theorem.**  Construct a
> protected Pascal braid and one trace-guarded compiler matching `M_0` such
> that every reachable task has `Omega(m^2)` resident packet options with
> matching coordinate entry/exit times, internal upper dominance, a common
> topology boundary, and deletion representatives expanding into the unused
> basis of `M_0`; the selected successor must regenerate the same bounded
> sidecar state.

The automatic common-basis avoidance theorem protects any bounded packet
scaffold from puncturing, and the arbitrary-common-basis theorem supplies a
`P-o(P)` physical body around it.  Neither theorem supplies the exact bulk
Hall/Rado row into `B`, the transparent packet lists, or the bounded
regeneration.  Those are the remaining mathematical obligations.
