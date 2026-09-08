# Canonical k17 mountain C6: complete upper transport, but no free opening

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: exact finite computer-assisted result for one analytically specified
surgery on the original canonical k17 PBBS factor. Every mathematical
execution was on `ssh h100`. The result does not supply a universal word,
reduce the number of components, or prove an all-rank transport theorem for
arbitrary C6 contexts or all dimensions.

## 1. Concrete theorem

Apply the clean C6 from
`MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`
to the original canonical rank-eight `f^2` factor in dimension 17. At the
lower-owner level, remove the three undirected edges

```text
(510,255), (894,383), (766,639)
```

and insert

```text
(510,383), (894,639), (766,255).
```

These are the published template with

\[
 C=\{1,\ldots,6\},\quad(a_0,a_1,a_2)=(7,8,9),\quad c=0,
\]

\[
 P_i=C\cup\{a_i,a_{i+1}\},\qquad Q_i=C\cup\{a_i,c\}.
\]

Complement the owners to obtain the rank-nine carrier.

The operation changes exactly the original cycles numbered 0 and 1 in the
canonical census, whose lengths are 17 and 221. It replaces them by two
cycles of lengths 135 and 103. Every one of the 238 owners is retained
once, and all owner degrees remain two.

For these affected owners, the **entire set of cyclic proper upper targets
is identical before and after the surgery**. The exact lost and gained
target families are both empty, at every rank. The shared local support has
the following complete census:

| upper rank | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| targets | 238 | 238 | 238 | 238 | 238 | 136 | 17 |

Thus 1,343 distinct proper upper targets have complete literal transport
certificates. Each new cycle also covers the full set by a whole-cycle
union. This is local support equality, not recovery from unaffected
components.

The global adjacent-intersection rank-eight **multiset** is unchanged, and
the new affected cycles have no positive coordinate run shorter than seven.
In particular the surgery creates no depth-three residence defect. It is
disjoint from the six 51-cycles used for the already constructed 306-owner
shallow prefix.

The topology remains a two-cycle topology. Although the rigid 17-cycle is
no longer a component, no net fusion has been achieved.

## 2. Exact source and transport certificate

The verifier starts from each rank-eight mask `A`, finds its unique cyclic
Dyck root `u`, and computes

\[
                        f(A)=A^c\setminus\{u\}.
\]

It decomposes the original `f^2` permutation into its canonical cycles.
It does not assume the published move's old edges are present: it checks
all three memberships, deletes them, inserts the three new edges, verifies
degree two everywhere, and traverses the resulting undirected components.
Orientation choices in that traversal cannot affect interval-OR support.

For each original and new affected cycle it considers every cyclic start
and successively ORs the following owners until the full set appears.
Every proper target in that cycle appears during this scan. Stopping at the
full set is safe because adding letters cannot remove coordinates.

Repeated unchanged OR values need only their shortest witness. For support
enumeration they add no target; for the cut-core calculation below, every
longer occurrence has a superset of that shortest occurrence's cut edges,
so discarding it does not change the intersection defining a cut core.

The exact output records:

* both original affected lower-owner cycles and both new cycles;
* the complete edge replacement;
* for every one of the 1,343 common targets, a literal old occurrence and a
  literal new occurrence, each specified by cycle, start, and width;
* the exact empty lost/gained target families;
* all relevant rank counts and positive-run histograms; and
* the targetwise cut cores and complete cut-loss lists for both new cycles.

The corresponding artifacts are

```text
scratch/audit_k17_canonical_rigid_clean_c6_20260908.py
scratch/k17_canonical_rigid_clean_c6_20260908.json
```

In the JSON, `complete_local_upper_transport` is the full target-to-
occurrence map. `affected_old_lower_cycles` and `new_lower_cycles` contain
the literal cycle bodies. This supplies actual PBBS exterior contexts,
rather than an arbitrary-context assertion based only on q1/q2 identities.

## 3. Lower-palette and residence checks

The original complementary owner factor has every rank-eight
adjacent-intersection target exactly once. Indeed, if the lower owner is
`A`, then `A union f^2(A)` is the rank-nine complement of `f(A)`; hence

\[
                      A^c\cap f^2(A)^c=f(A).
\]

The permutation `f` supplies every rank-eight mask once. The clean-C6
identities preserve the old lower-owner adjacent-union multiset, and the
verifier independently compares the full affected counters after
complementation. Thus no rank-eight adjacency label is lost or duplicated.

The old and new positive-run histograms on the affected complementary
cycles are:

| run length | old occurrences | new occurrences |
|---:|---:|---:|
| 7 | 0 | 1 |
| 8 | 204 | 205 |
| 9 | 17 | 15 |
| 21 | 17 | 15 |
| 22 | 0 | 1 |
| 23 | 0 | 1 |

All other lengths have zero occurrences. These counts come from actual
maximal coordinate runs in the resulting cyclic owner sequences. They show
that the gadget is safe for the depth-three sector, independently of the
published q2 palette claim.

## 4. Exact opening obstruction after the surgery

Neither resulting cycle has a cut preserving all its globally exclusive
proper upper targets, even when its companion and all other original
cycles remain intact.

For the 135-cycle, the globally exclusive target counts are 135 each at
ranks 10, 11, and 12, and 17 at rank 13. For the 103-cycle they are 103
each at ranks 10, 11, and 12. Each cycle's minimum forced exclusive loss
over all cuts is exactly six. In particular every cut already loses a
rank-ten target, and no safe-port bank is obtained.

These statements use complete targetwise cores. For a cyclic occurrence
with start `i` and width `q+1`, its fatal cuts are the `q` internal edges.
Intersect these sets over all occurrences of a target. A cut loses that
target exactly when it lies in the intersection. A target is globally
exclusive to the current cycle exactly when neither the companion nor an
unaffected cycle supplies it. The verifier performs both tests explicitly.

The surgery nevertheless reduces the scalar minimum recapture bill. The
two old cycles have minimum exclusive losses 10 and 6. The two new ones
have minima 6 and 6. Since the union of affected upper supports is unchanged,
global exclusivity for every unaffected cycle is unchanged. Therefore the
sum of cyclewise minimum forced losses in the complete factor decreases
exactly from **129 to 125**. The number of cycles with no globally safe cut
remains 59.

This number is a mandatory target-recapture count before new seam witnesses
are included. It is not a word-length improvement or a lower bound on
`nu(17)`.

## 5. Composition with the 306-owner stage

The six bad cycles used in
`K17_PBBS_UPPER_CUT_CORES_AND_306_OWNER_SOURCE_STAGE_20260908.md` have
indices 115,116,118,122,129,138, disjoint from the two affected cycles here.
The 306-owner path retains the old global upper deck by relying on the
union of the remaining cycles' supports. The present surgery leaves the
support union of cycles 0 and 1 exactly unchanged, so that reliance remains
valid. Conversely the C6 support equality itself uses no outside backup.

Consequently the two modifications can coexist without a new proper-upper
defect. This surgery also leaves the prefix stage's five rank-eight
adjacency deficits unchanged, since its own rank-eight multiset is
preserved. Both output cycles remain suitable intact blocks for the
depth-three sector by their minimum positive residence seven.

The 125 count in Section 4 pertains to the all-cycle factor after this C6
alone. It is not automatically the recapture bill of the later mixed
path/cycle stage, whose backup occurrences and already opened components
must be evaluated in their actual form.

To turn this into a single source, one still needs actual fusion seams
with the exact run and nonempty-envelope tests, literal replacements of
the upper targets lost when cycles are cut, and the full lower common-cap
assignment. The surgery does not establish any of those global facts.

## 6. Reproduction and scope

The remote execution directory is

```text
/home/amodo/exact-b-k17-rigid-c6-20260908/
```

Copy the verifier there as `audit.py`, then execute on h100:

```sh
python3 audit.py
```

It writes `rigid_c6.json`. The original canonical cut inventory used for
the 129-to-125 comparison is

```text
/home/amodo/exact-b-k17-pbbs-inventory-20260908/inventory.json
```

No search over alternative C6 moves, arbitrary contexts, or seam paths was
performed. The tested edges were fixed by the published analytic template.
All-rank local support equality is proved here only for its actual
canonical k17 context. The general template theorem still guarantees only
its previously proved q1/q2 identities until a dimension-uniform
all-width transport argument is supplied.
