# k=15 q1-factor to compiler audit

## Scope and terminology

This audit concerns the saved equivariant quotient selectors that already give
a physical Johnson 2-factor with both q1 rainbows complete.  Their reported
`choice_changes` values are **Hamming distances between quotient selectors**.
They are not Hall deficiencies.

The resident-centred distance is measured from the resident seed; the other
distances are measured from the joint scaffold.  They are therefore not even
one common optimization scale.  The comparison below is decided by the
intrinsic residence and shadow columns, not by the distance column.

None of the audited factors is yet a valid depth-three carrier, so the graded
lower Hall instance is not yet defined for any of them.  In particular, the
authoritative Hall deficiency 19 belongs to the older non-equivariant
carrier/compiler pairing and must not be attached to the factors below.

The deterministic source is
[`scratch/audit_k15_q1_factor_compiler_readiness.py`](scratch/audit_k15_q1_factor_compiler_readiness.py),
with full output in
[`scratch/k15_q1_factor_compiler_readiness.audit.json`](scratch/k15_q1_factor_compiler_readiness.audit.json).
The distance-80 input has SHA-256
`bc734aa673ce1efc7b72e298c5765e526daee87c948ccc9a4db947d7313cd557`.

## Exact comparison

| saved factor | quotient-choice distance | physical cycles | bad carrier runs (length 2 / 3) | exact minimum residence cuts | forced q1 holes before seams | missing carrier-gate orbits (lower q2 / lower q3 / upper) |
|---|---:|---:|---:|---:|---:|---:|
| resident-centred `d80` | **80** | 3615, 1050, 1050, 720 | **240 / 435** | **480** | **>=135** | **53 / 16 / 21 = 90** |
| resident-centred `d83` snapshot | 82 | 15 x 429 | 255 / 510 | 540 | >=150 | 52 / 19 / 20 = 91 |
| joint `d86` | 86 | 5 x 1209, 270, 120 | 510 / 615 | 780 | >=240 | 53 / 25 / 20 = 98 |
| joint `d92` | 92 | 3 x 2080, 195 | 600 / 480 | 735 | >=180 | 57 / 20 / 17 = 94 |
| joint strict Hamilton `d93` | 93 | 1 x 6435 | 570 / 480 | 720 | >=180 | 56 / 22 / 17 = 95 |
| joint `d94` | 94 | 5 x 1287 | 585 / 465 | 735 | >=180 | 57 / 21 / 17 = 95 |

There are no length-one carrier runs in any factor.  At depth three, the bad
runs are exactly the length-two and length-three runs shown above.

The residence-cut number is exact: every bad run gives a circular interval of
three or four factor edges, and a cut must stab that interval.  Circular
interval stabbing is solved exactly by fixing a point in one interval and
greedily stabbing the resulting linear intervals by right endpoints.

The former distance-82 factor's 15 length-429 cycles are rotational translates.  Hence its
765 physical residence defects are only **51 quotient defect motifs**, its 540
minimum physical cuts are 36 cuts per phase, and its forced q1 loss is 10
colours per phase.  This is precisely why repairing quotient choices is much
smaller than routing 540 independent physical paths.

The q1-hole number is a rigorous lower bound for a *cut-only* repair.  It keeps
only bad-run spans all of whose edges carry globally unique upper-q1 colours,
then exactly stabs those spans.  Every selected edge destroys a different
unique colour.  Other interactions can only increase the loss.

## Shadow profiles

The fixed-window physical holes `(lower, upper)` at q=1,2,3 are:

| factor | q1 | q2 | q3 |
|---|---:|---:|---:|
| resident d80 | (0,0) | (775,270) | **(240,45)** |
| resident d82 | (0,0) | (760,270) | (285,30) |
| joint d86 | (0,0) | (775,270) | (375,30) |
| joint d92 | (0,0) | (835,228) | (300,30) |
| strict d93 | (0,0) | (820,228) | (330,15) |
| joint d94 | (0,0) | (835,228) | (315,30) |

For the best resident-centred factor, unrestricted consecutive carrier
intervals still miss:

| rank | physical holes | orbit holes |
|---:|---:|---:|
| 4 | 60 | 4 |
| 5 | 240 | 16 |
| 6 | 775 | 53 |
| 10 | 270 | 18 |
| 11 | 45 | 3 |

All other noncentral ranks are covered by unrestricted cyclic intervals.
The lower q2/q3 and upper totals in the first table are precisely the orbit
gates consumed by the current carrier/compiler pipeline.

## Opening verdict

Opening every original component once does **not** eliminate residence for any
saved factor.  Even the one-cycle d93 Hamiltonian carrier needs 720 cuts, not
one.  The best object now needs 480 cuts, producing 480 paths.

For each factor, the deterministic exact minimum-stabbing witness was also
opened into paths.  The raw endpoint Johnson graph is connected in all six
cases, so ordinary adjacency is plentiful.  Residence-safe seams are the
problem:

| factor | paths | residence-safe seam components | isolated paths | degree-1 paths |
|---|---:|---:|---:|---:|
| resident d80 | **480** | 16 | 15 | 59 |
| resident d82 | 540 | 8 | 7 | 31 |
| joint d86 | 780 | 1 | 0 | 8 |
| joint d92 | 735 | 1 | 0 | 5 |
| strict d93 | 720 | 16 | 15 | 15 |
| joint d94 | 735 | 1 | 0 | 18 |

Thus **none of the six canonical minimum-cut witnesses can have a Hamilton
path in its residence-safe seam graph**: each has an isolated path or more
than two degree-one paths.  This is not a no-go for all minimum cut sets; cut
positions were optimized only for cardinality, not seam compatibility.  It
does show that a fixed-factor splice route must jointly optimize cuts and
seams rather than treating seams as a cheap second phase.

Thus there are two exact repair formulations:

1. **Fixed-factor seam formulation.**  Jointly choose a noncanonical cut set
   and its seams.  The cardinality floor is now 480 paths and 479 new Johnson
   seams for the resident-centred factor.  The seams must restore a
   perfect lower-q1 palette except for the permitted linear boundary colour,
   restore at least the 135 upper-q1 colours necessarily lost at cuts, create
   no new carrier run of length below four, and then meet the remaining shadow
   gates.  This is exact but is a large global path-routing model.
2. **Choice-repair formulation (recommended).**  Change the quotient selector
   itself and impose only:
   - one choice at each of the 429 lower-central orbits;
   - physical degree two;
   - complete upper-q1 coverage; and
   - no physical coordinate run of length 1, 2, or 3.

   Connectivity should remain relaxed to a cycle cover.  This is the smallest
   exact gate that removes the obstruction exhibited by the audit.  It is the
   existing `search-carrier --allow-cycle-cover --base-only` model, seeded by
   the resident-centred distance-80 factor.  Only after it succeeds should the
   exact lower-q2, lower-q3-positive-degree, and unrestricted-upper CEGAR cuts
   be enabled.  Hall is evaluated only after those carrier gates pass and a
   valid erosion envelope exists.

## Concrete recommendation

The resident-centred distance-80 factor is the unambiguous best postprocessing
seed among the saved q1 factors.  It simultaneously minimizes residence
violations (675), exact residence cuts (480), forced cut-only q1 loss (135),
and total missing carrier-gate orbits (90).  Hamiltonicity of d93 is not useful
enough to offset its substantially worse residence geometry.

The next exact search target is therefore **resident d80 -> resident,
q1-complete, degree-two, residence-clean cycle cover**, with no connectivity or
deeper-shadow constraints.  A positive result enters the exact shadow CEGAR
stage.  A negative result at a proved radius is meaningful.  Running a lower
Hall compiler before this gate passes is mathematically premature.

The corresponding repo-owned invocation is of the form

```bash
python3 scratch/graded_quotient_pipeline.py search-carrier \
  --k 15 \
  --hint scratch/k15_resident_q1factor_d80_snapshot.json \
  --allow-cycle-cover --base-only \
  --max-choice-changes R \
  --workers 8 --timeout 1800 --max-rounds 1 \
  --output scratch/k15_resident_q1factor_base_rR.json
```

Here `R` is distance from the saved distance-80 factor, not from the original
resident seed and not a Hall deficiency.
