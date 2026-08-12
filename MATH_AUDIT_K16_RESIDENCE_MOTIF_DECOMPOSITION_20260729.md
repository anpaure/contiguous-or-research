# k=16 residence-motif decomposition and exact rethread frontier

Date: 2026-07-29

## Certified scaffold

The source
`scratch/k16_qfactor_q1_topresident_hamilton_20260729.json` selects 858
edge orbits of the 858-vertex rotational quotient.  Independent audits give:

- one quotient cycle, voltage 11 modulo 15;
- one physical Hamilton cycle of length 12,870;
- all 764 lower and all 764 upper q1 colour orbits covered;
- top-coordinate 1-runs and 0-runs of length at least four;
- 3,390 old-coordinate short runs: 330 of length one, 1,620 of length
  two, and 1,440 of length three.
- 88 quotient q2 holes and 122 upper-shadow orbit holes.

Rotation acts freely on the old coordinates of each short-run witness.  The
3,390 physical witnesses therefore collapse to 226 quotient motif orbits:

| physical run length | quotient motif edges | quotient motifs | physical copies |
|---:|---:|---:|---:|
| 1 | 2 | 22 | 330 |
| 2 | 3 | 108 | 1,620 |
| 3 | 4 | 96 | 1,440 |

Each motif is exactly the entering edge, its internal edges, and the exiting
edge of the short coordinate run.

## Elementary `147` min-max theorem

Write the selected quotient Hamilton cycle as

\[
e_0,e_1,\ldots,e_{857}.
\]

Every residence motif is a set of two, three, or four consecutive cyclic
edges.  Their union covers 558 cycle edges, leaving 300 edges in no motif.
Cutting the cycle at any uncovered edge turns all motifs into ordinary
intervals on a line.

Apply the earliest-finish greedy algorithm.  Whenever the first remaining
interval ends at position \(p\), put \(p\) in the transversal and put that
interval in the packing, then delete all intervals meeting \(p\).  This
constructs simultaneously:

- 147 pairwise edge-disjoint residence motifs; and
- 147 selected quotient edges meeting all 226 motifs.

The packing is an integral LP-dual certificate: assign dual weight one to
each packed motif and zero to every other motif.  Since the packed motifs are
edge-disjoint, every edge constraint has dual load at most one, and the dual
value is 147.  The 147-edge transversal is a primal solution of the same
value.  Hence

\[
\boxed{\nu(\mathcal H)=\tau(\mathcal H)=147.}
\]

The solver-free greedy packing used by the audit has size histogram
\(2^{20}3^{72}4^{55}\) and union size 476.  An independent CP packing has
histogram \(2^{19}3^{70}4^{58}\) and union size 480.  These are different
maximum packings and must not be conflated.

The structural artifact
`scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json`
contains all 147 greedy packed edge sets, their quotient-cycle positions, and
the unique transversal edge assigned to each.  Any 147-edge transversal must
meet every packed motif exactly once and cannot remove an edge outside the
chosen packed union.

## Local components

The motif-intersection hypergraph has 112 components.  No component has more
than seven motifs or fourteen selected edges.

| component transversal number | number of components |
|---:|---:|
| 1 | 85 |
| 2 | 21 |
| 3 | 4 |
| 4 | 2 |

The total is \(85+2\cdot21+3\cdot4+4\cdot2=147\).  Fifty-eight components
are isolated single motifs.  Selected quotient-edge motif degrees are

\[
0^{300},\quad1^{384},\quad2^{154},\quad3^{20}.
\]

Thus the residence obstruction is locally decomposable.  The difficulty is
not selecting motif cuts; it is completing those cuts to a new factor while
retaining the two colour decks.

## Exact q1 coupling

The scaffold's selected-provider multiplicities are

| palette | multiplicity 1 | multiplicity 2 | multiplicity 3 | excess |
|---|---:|---:|---:|---:|
| lower q1 | 680 | 74 | 10 | 94 |
| upper q1 | 674 | 86 | 4 | 94 |

Only 36 of 858 selected edges are individually redundant in both palettes,
and 186 of the 226 motifs contain no such edge.  Exact CP-SAT diagnostics
prove:

1. no motif transversal can retain at least one *current* provider of every
   lower and upper colour;
2. minimizing current provider losses over all transversals gives 180 lost
   colour classes (88 lower and 92 upper) with 148 deleted edges;
3. at the exact 147-edge radius, the minimum is 181 lost classes (87 lower
   and 94 upper).

If AB deletions are forbidden, a 147-edge transversal still exists, but its
best possible provider loss is 182 classes (87 lower and 95 upper).

These are deletion-only statements.  A rethread adds as many new edges as it
deletes, and those additions can restore the missing colours.  The theorem is
that residence cuts and palette restoration cannot be performed
sequentially; they must be chosen jointly.

## Fixed-cross shore decomposition

The scaffold contains 389 AA, 80 AB, and 389 BB selected edge orbits.  The
80 AB edges form a matching: 80 distinct A boundary vertices and 80 distinct
B boundary vertices.

If the AB pattern is fixed, each shore is a residual f-factor problem on 429
vertices:

- residual degree one at its 80 boundary vertices;
- residual degree two at its 349 interior vertices;
- exactly 389 selected same-shore edges.

The fixed AB matching supplies 80 distinct lower-no-top colours and 80
distinct upper-top colours.  Consequently:

- AA must cover the remaining 349 lower-no-top colours and all 335
  upper-no-top colours;
- BB must cover all 335 lower-top colours and the remaining 349 upper-top
  colours.

Each shore therefore covers 684 required colour classes with 389 edges,
again with 94 incidence units of slack.

There are 175 motifs wholly inside one shore and 51 meeting one fixed AB
boundary.  No short motif contains two AB edges, as top biresidence separates
cross boundaries by at least four vertices.  Pure-shore interval packings
force at least 60 AA removals and at least 60 BB removals.  The remaining 27
minimum-radius removals allocate the boundary motifs between the shores.

A size-147 transversal with no AB deletion exists.  Nevertheless, the exact
joint cut-and-seam model with

- one deletion from each of the 147 packed motifs;
- all 226 original motifs hit;
- every AB edge fixed;
- quotient degree two;
- both q1 palettes complete;

is **INFEASIBLE**.  This remains infeasible even after dropping top
biresidence.  Lower q1 alone is feasible and upper q1 alone is feasible; the
incompatibility is specifically their simultaneous realization on the same
radius-147 residual f-factors.

Therefore:

\[
\boxed{\text{every radius-147 rethread must change at least one AB edge.}}
\]

Both the scaffold and every quotient 2-factor have an even number of AB
edges, since \(2|A|=2E_{AA}+E_{AB}\).  Hence the AB-set symmetric difference
is even: the first live case changes at least two AB variables.  This gives a
sound redundant Benders row for the unrestricted radius-147 search.

Equivalently, retaining the entire top-boundary pattern costs at least radius
148.

## Exact next models

Two complementary models are implemented.

1. `scratch/search_k16_residence_radius147_packing_rethread_20260729.py`
   keeps the full edge catalogue, enforces AddCircuit, unit voltage, both q1
   palettes, top biresidence, the 147 packing equalities, and exact CEGAR cuts
   for every newly-created residence motif.  This is the correct radius-147
   lane because it permits the now-necessary AB changes.
2. `scratch/search_k16_residence_radius147_shore_cegar_20260729.py` fixes the
   AB matching and solves the two residual shore f-factors, with component,
   voltage, and new-motif cuts added lazily.  Radius 147 is certified
   infeasible; radius 148 is the first live fixed-cross case.

The first unrestricted radius-147 AddCircuit solve with the 226 seed motif
cuts returned `UNKNOWN` after 600 seconds; this is not evidence of
infeasibility.  The packing model is stronger: it fixes 382 selected edges,
limits deletions to a 476-edge packed union, and restricts additions to
12,320 admissible nonloop edges on 586 possible deficit vertices.

The mathematically justified next move is therefore parallel but sharply
bounded:

- run the packing-strengthened radius-147 model allowing AB changes;
- run the radius-148 fixed-cross shore model;
- after the first feasible factor, add newly-created residence motifs before
  spending effort on q2 and deeper shadows.

This is not a local phase/voltage repair.  At least 147 quotient edge orbits,
or 2,205 physical edge occurrences, must change, and the two q1 decks force a
topology-changing rethread at the minimum radius.
