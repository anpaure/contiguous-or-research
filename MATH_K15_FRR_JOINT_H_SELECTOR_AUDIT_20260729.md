# K15 FRR: joint cut-set and selector audit

Date: 2026-07-29  
Status: exact restricted model validated, then superseded by a static
41-versus-60 obstruction.

## 0. Scope and verdict

The model chooses the cut support `H` and every replacement pair together.
It is exact in the following class:

* the source is the saved two-component K15 facet factor;
* the 45-vertex component is frozen;
* the 6,390-vertex component is repaired equivariantly under `Z_15`;
* every changed upper-colour orbit retains exactly one edge orbit.

It is not an unrestricted turn-selector theorem and is not a no-go for
`nu(16)` if UNSAT.

The base CNF has:

| item | count |
|---|---:|
| cut variables `x_q` | 426 |
| non-old replacement variables `y_(q,p)` | 11,502 |
| primary variables | 11,928 |
| total variables | 69,640 |
| clauses | 186,029 |
| literals | 1,670,033 |
| collar rows | 95 |
| cut-spacing rows | 1,278 |
| distinct endpoint rows | 429 |
| distinct lower-coverage rows | 332 |

This is small enough for one low-priority, 1 GB Kissat lane.  It is also
the exact implementation of the useful part of the proposed surgery-flow
idea: the support is no longer frozen before endpoint circulation is known.

## 1. Exact constraints

For each quotient upper orbit `q`, `x_q=0` retains the old edge orbit and
`x_q=1` chooses one of its 27 non-old pair orbits:

```
sum_p y_(q,p) = x_q.
```

The static CNF enforces:

1. all 95 old length-three-run collars are hit;
2. two chosen cut residues have cyclic separation at least four;
3. every physical rank-seven vertex has degree exactly two after the
   frozen small-component contribution is subtracted;
4. every physical rank-six colour not supplied by the small component has
   at least one retained-old or replacement provider;
5. upper q1 coverage, which is automatic because each upper orbit selects
   exactly one edge orbit.

Every SAT factor is reconstructed physically.  A bordered positive run of
length at most three, or a component shorter than four, contributes the
universal path clause saying that at least one of its selected edges must be
absent next time.  These cuts do not assume that a particular current
factor is otherwise fixed.

## 2. Off-by-one and exceptional-orbit audit

The independent audit
`scratch/audit_k15_frr_joint_h_exactness_20260729.py` proves mechanically:

* the spacing loop emits exactly the 1,278 unordered pairs at cyclic
  distances one, two, or three, each once;
* the primary count is exactly `426*(1+27)=11,928`;
* rank seven and rank eight each consist of 429 free size-15 orbits;
* rank six consists of 333 size-15 orbits and two exceptional size-5
  orbits;
* one exceptional rank-six orbit is already covered by the frozen small
  component;
* on the other, one equivariant provider hits a physical colour three
  times.  Its signed literal therefore occurs three times in the raw row.
  The row is an OR-coverage clause, so this multiplicity is intentionally
  idempotent rather than an erroneous exact-cardinality coefficient;
* all physical rotations of each rank-six row have identical signed
  expressions before global deduplication.

Thus the non-free rank-six action is handled physically, not by applying a
false free-orbit quotient.

## 3. Regression and all-depth materialization

With collar/spacing constraints omitted and all `x_q=0` pinned, the model
is SAT and reconstructs the source exactly:

* two components;
* complete lower and upper q1 palettes;
* 1,425 positive length-three violations;
* 95 distinct joint-model path clauses.

The final materializer also performs the canonical compiler all-depth
audit.  On the source it records rank-seven vertices once; lower rank
`7-q` uses fixed intersections of `q+1` consecutive vertices; upper
coverage extends every cyclic start until the full set and records every
strictly new union.  It finds zero holes in every rank.  The nonzero
load-one census is:

| rank | load-one targets |
|---:|---:|
| 4 | 90 |
| 5 | 900 |
| 6 | 3,630 |
| 7 | 6,435 |
| 8 | 6,435 |
| 9 | 3,675 |
| 10 | 1,095 |
| 11 | 30 |

Any residence-clean q1 candidate is labelled full `PASS` only if this
canonical all-depth replay also has zero holes.  Otherwise it is retained
under the narrower status
`PASS_Q1_RESIDENCE_ALL_DEPTH_INCOMPLETE`.

## 4. Superseding static obstruction

The first joint base solution used 89 cut orbits and had 1,710 physical
short-run violations, collapsing to 114 new equivariant path clauses.  The
next candidates remained statically exact and produced fresh sound cuts;
the early minimum was 1,500 violations at 86 cut orbits.  This is evidence
that joint support selection is a genuinely larger *unfiltered* lane than
all 31 fixed frontier banks.  It did not establish convergence.

Every round was appended to `work/rounds.jsonl` before the next solve, so
component counts, cut counts, violations, fresh clauses, and solve time
survive disconnects and restarts.  The lane stopped after 1,575 sound cuts
when one round reached its 120-second cap; its status is `UNKNOWN_TIMEOUT`,
not UNSAT.

It is now redundant.  A separate endpoint-seam formulation enumerates all
2,000 residence-compatible equivariant seam descriptors in advance.  The
following were independently checked against this joint-y model:

* 1,918 descriptors map to one of the 11,502 non-old joint-y edge orbits;
* 82 descriptors re-add an old edge orbit;
* no compatible old readdition owner occurs in any bad-run collar, so a
  nominal cut cannot fake collar repair;
* self endpoint-type seam loops cannot be matching orbits because the
  physical endpoint orbit has odd size 15;
* every descriptor lifts to 15 distinct physical edges;
* duplicate descriptors for the same physical edge orbit are harmless and
  mutually excluded by endpoint/upper equations;
* the sheet-five gauge rotates back to the canonical quotient endpoint,
  including the voltage-four wrap at owner 425;
* the capped trace condition is necessary and sufficient locally once cut
  residues have cyclic separation at least four.

The exact endpoint+upper+spacing system has maximum cut cardinality 41.
Independently, hitting all 95 source collars subject to the same spacing has
minimum cardinality 60.  Thus no residence-clean candidate in this joint-H
source-relative class exists:

\[
             \max |H|_{\rm compatible}=41<60=
             \min |H|_{\rm collar}.
\]

Two independently generated decision CNFs certify the two strict sides:

| decision | vars | clauses | Kissat | CaDiCaL |
|---|---:|---:|---|---|
| compatible endpoint/upper solution with `|H|>=42` | 170,382 | 348,120 | UNSAT, 0.62s | UNSAT, 1.22s |
| spaced collar transversal with `|H|<=59` | 25,501 | 51,889 | UNSAT, 0.05s | UNSAT, 0.03s |

The maximum-41 witness was physically rebuilt.  It has components
`2130+2130+2130+45`, perfect upper q1, and exactly 1,305 positive length-three
runs.  Those are precisely `15*87`, where 87 is its number of unhit quotient
collars.  Hence the compatible seams introduce zero new short runs; the
remaining violations are exactly the deliberately omitted old collars.

This closes only the `Z_15`-equivariant, small-component-frozen, spaced
source-relative FRR class.  It does not close unrestricted `RTR(7,4)` or
the full `nu(16)` problem.

## 5. Files

* `scratch/solve_k15_frr_joint_h_selector_cegar_20260729.py`
* `scratch/audit_k15_frr_joint_h_exactness_20260729.py`
* `scratch/k15_frr_joint_h_count_20260729.json`
* `scratch/k15_frr_joint_h_exactness_audit_20260729.json`
* `scratch/k15_frr_joint_h_pinold_result_20260729.json`
* `scratch/audit_k15_frr_static_max41_independent_20260729.py`
* `scratch/k15_frr_static_max41_independent_20260729.audit.json`
* `scratch/k15_frr_static_41_vs_60_backend_crosscheck_20260729.json`
* `scratch/k15_frr_joint_h_superseded_result_20260729.json`
* `scratch/k15_frr_joint_h_superseded_rounds_20260729.jsonl`
