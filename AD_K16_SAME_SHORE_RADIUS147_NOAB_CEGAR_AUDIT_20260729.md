# Adversarial audit: k=16 radius-147 fixed-AB same-shore CEGAR

Date: 2026-07-29

Verdict: **the radius-147 cut normal form, the 80 fixed AB edges, all variable
counts, and the degree/q1 semantics check exactly.**  The reported round-zero
`INFEASIBLE` status is nevertheless solver-transcript evidence only: the
payload contains no independently checkable UNSAT proof or universal
structural cut.  A small solver-free obstruction can be extracted for the
single retained same-shore transversal hint, but it does not apply to all
variable radius-147 cut choices.

Replayable files:

- `scratch/audit_ad_k16_same_shore_radius147_noab_cegar_20260729.py`
- `scratch/ad_k16_same_shore_radius147_noab_cegar_20260729.audit.json`

No CP-SAT solve was launched for this audit.

## 1. Proven radius-147 normal form

The source is again the top-resident Hamilton scaffold, SHA-256
`f76ab4e5...`, not the promoted lower-q1-two-hole carrier.  Its 226 old
residence motifs contain a certified family of 147 pairwise edge-disjoint
motifs.  Their sizes and union are:

| Packed motif size | Number |
|---:|---:|
| 2 | 20 |
| 3 | 72 |
| 4 | 55 |
| **Union edges** | **476** |

Every repair must delete at least one current edge from every packed motif.
Because the packed motifs are edge-disjoint, every repair deletes at least
147 current edge orbits.  At removal radius exactly 147, equality forces:

1. exactly one deletion in each packed motif; and
2. no deletion outside their 476-edge union.

This is the exact solver-free reason for the 476 cut variables and the 147
equalities.  It does not depend on CP-SAT, degree completion, or q1.

The retained same-shore transversal is an explicit feasible witness for the
pure motif system: it contains 147 edges, chooses exactly one from every
packed motif, and hits all 226 old motifs.  Its split is 87 AA plus 60 BB.

## 2. Fixed-cross scope is an added restriction

The complete quotient catalogue contains

```text
AA 12012, AB 3432, BB 12012; loops: 14 AA + 14 BB.
```

The source factor contains

```text
AA 389, AB 80, BB 389; loops: 0.
```

Its 80 AB edges have 160 distinct endpoints.  The packed 476-edge union
contains 233 AA, 36 AB, and 207 BB edges.  The model creates all 476 cut
variables but fixes the 36 AB cut variables to zero.  The other 44 selected
AB edges lie outside the packing union and are constants.  New AB edges are
excluded.  Hence all 80 source AB edge orbits are fixed selected exactly,
leaving 440 effective same-shore cut choices.

This fixed-AB condition is **not** a consequence of the radius-147 normal
form.  The existence of one same-shore minimum transversal proves only that
the no-AB face is nonempty at the motif level; it does not prove that every
minimum transversal avoids AB edges.  The negative result therefore belongs
to the explicitly restricted no-AB branch.

The model also forbids every new quotient loop.  That too is a restriction,
not a consequence of the packing theorem.

## 3. The 23,218 seam variables

The seam set is exactly every quotient edge orbit satisfying all three
conditions:

1. not selected in the source;
2. shore AA or BB, not AB; and
3. not a quotient loop.

The independently reconstructed count is

```text
AA 11609 + BB 11609 = 23218.
```

Equivalently, start with 24,024 same-shore catalogue edges, remove 28 loops
and the 778 selected same-shore source edges.  No allowed seam is omitted
inside the stated nonloop fixed-AB domain.

## 4. Degree and q1 constraints are exact

The source has quotient degree two at all 858 quotient vertices.  For every
vertex the model imposes

```text
removed incidence = added incidence.
```

An undirected nonloop contributes at each endpoint; a cut loop would be
listed twice at its one quotient endpoint.  Thus the equations make
`source - cuts + seams` degree two exactly.  Summing all 858 equations gives
twice the number of cuts equals twice the number of seams.  Since the packed
equalities force 147 cuts, they also force 147 seams without a separate
cardinality constraint.

The detailed motif catalogue and the coarse degree/q1 catalogue have exact
edge-ID alignment across all 27,456 orbits: representatives, quotient
endpoints, lower and upper rows, loop flags, and shore types all agree.

For each of all 764 lower and 764 upper quotient q1 rows the expression

```text
source multiplicity - cut providers + seam providers >= 1
```

is literally the resulting provider multiplicity.  It is not a proxy,
capacity bound, or compressed sufficient condition.  Therefore the model
enforces both current q1 decks exactly within its edge domain.

All 226 old residence motifs are hard constraints in round zero.

## 5. Relaxation direction and exact implication

Relative to a general radius-147 rethread, the model is restrictive because
it fixes all 80 AB edges, forbids every new AB edge, and forbids new loops.

Within that restricted domain it is a relaxation of the desired exact
Hamilton-resident factor:

- quotient connectivity and lift voltage are only postchecked;
- round zero cuts only the 226 old motifs;
- residence motifs created by chosen seams would be discovered and added
  lazily after a feasible incumbent.

The solver reports the round-zero relaxation itself infeasible, before any
incumbent or lazy cut.  Therefore, if the transcript is trusted, it excludes
every exact resident Hamilton factor inside the fixed-AB, nonloop-same-shore,
radius-147 face: an exact solution would also satisfy this weaker base model.

It does **not** exclude variable-cross, AB-replacement, loop-seam, or
radius-above-147 rethreads.

## 6. Solver-free structural search

There is no motif-only contradiction: the retained 147-edge same-shore hint
meets all pure cut and old-motif constraints.

For that one fixed hint, however, a solver-free degree/q1 obstruction exists.
The cuts create deficits at 290 quotient nodes, with histogram
`1:286, 2:4`.  They destroy 104 lower and 118 upper current q1 rows.  Nine of
those rows have no allowed seam provider whose two endpoints both have
positive deficit: four lower and five upper.

An explicit row is lower q1 row `2765`:

- selected edge 7714 is its sole source provider and the hint deletes it;
- it has 27 allowed off-source AA nonloop seam providers;
- every one of those 27 edges has an endpoint of deficit zero.

At a deficit-zero endpoint the degree equation is a sum of nonnegative seam
variables equal to zero, forcing every incident candidate off.  Hence row
2765 cannot be restored for this fixed hint.  The audit JSON lists all 27
providers and hashes the full nine-row obstruction family.

This certificate must not be promoted to the joint CEGAR model: another
one-per-packed-motif cut choice changes the deficit nodes and need not delete
edge 7714.  I found no universal cut or dual certificate for all 440 effective
cut variables.

## 7. Transcript and provenance

The retained result has one round:

```text
status INFEASIBLE
motif cuts before solve 226
branches 160567
conflicts 12640
wall time 3.036135964 s
```

Its canonical `payload_sha256` recomputes exactly as
`e34945e92e4805917add5c41e4a8b0761da5fc460c976a86257df3b4ad8c7bbd`.
Its embedded source SHA and motif-audit SHA also match current bytes.

The result does not embed the model-script SHA, catalogue/module SHA or
catalogue digest, OR-Tools version, host/full command arguments, or a proof
log.  The follow-up audit JSON records the current generator/module hashes,
but historical model provenance and the universal UNSAT lower bound remain
solver-transcript scope.
