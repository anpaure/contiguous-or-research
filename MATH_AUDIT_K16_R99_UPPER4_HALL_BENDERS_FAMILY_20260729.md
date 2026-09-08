# The fixed-6c98 upper-four core is a reusable Hall/Benders family cut

Date: 2026-07-29  
Status: solver-free theorem and exhaustive one-swap family replay; no `k=16`
word is claimed.

## 1. Exact four-row obstruction

For the radius-99 delete cut with digest

```text
6c98aa96b824b580be70fb9bab617e80fef233b4bf11b33a7a83adce5d9c39b4
```

the deletion-minimal exact-degree/q1 core consists of four upper-q1 colours:

```text
(1,1883)  source provider  4742
(1,1907)  source provider 22511
(1,3255)  source provider 23229
(1,5939)  source provider 24034.
```

Under this cut the only degree-usable replacement providers are

```text
(1,1883):  4737,4740,18552,18555,21385
(1,1907): 18171,18172
(1,3255): 21408,21411
(1,5939): 22529,22530.
```

Every one meets the three-node bottleneck

```text
B={576,611,617}.
```

The deleted source edges supply only three incidences on `B`: edge `18158`
supplies one and edge `22511` supplies two.  Distinct upper colours require
distinct replacement seams, so demand four exceeds capacity three.

This fixed-cut statement is only the visible specialization of a global
projected row.  Put

```text
P = {576,611,617}
    union
    {97,208,403,485,502,521,541,546,581,600,606,615,619,
     620,623,667,751,757,758,759,761,832,852}.
```

The second set has zero cut capacity at 6c98.  Direct catalogue replay checks
that `P` meets all 140 loopless off-source providers of the four colours, not
merely the eleven providers usable at 6c98.

## 2. Projected inequality

Let `x_h` be the cut bit of selected source edge `h`.  Every exact-degree,
both-q1 completion satisfies

```text
sum_h |ends(h) intersect P| x_h
    >= x_4742+x_22511+x_23229+x_24034.               (2.1)
```

Indeed, the right side counts lost source-unique upper colours.  They require
distinct added seams, every such seam consumes at least one endpoint incidence
in `P`, and exact degree restoration makes the available added incidence on
`P` equal the source-cut incidence on `P`.

The exact left support contains the 49 selected source edges incident with
`P`, with coefficient one or two according to endpoint incidence.  After
moving the four right literals left and cancelling, the normalized master row
has 52 nonzero signed coefficients.  The complete ordered lists are frozen in

```text
scratch/k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.audit.json
```

At 6c98, (2.1) reads `3 >= 4`; its normalized margin is `-1`.  This is a
solver-free proof of fixed-cut infeasibility and a globally valid generalized
Benders row, not a SAT-transcript no-good.

## 3. It excludes a family, not only 6c98

Every branch-preserving one-swap cut

```text
C' = C - {removed} + {added},
removed in C\{22511}, added in source\C
```

was enumerated.  The replay invokes no solver.  Its cumulative census is

| stage | cuts |
|---|---:|
| all one-swaps | 74,382 |
| violate (2.1) | 67,685 |
| also hit all 147 residence motifs | 858 |
| also satisfy delete-branch Pareto rows | 858 |
| also satisfy every current static portal, grouped-Hall, and joint-cover row | 65 |
| also retain the explicit 35-edge two-palette/endpoint master witness | **11** |

The eleven full current-master witnesses are the swaps

```text
(289,259)       (1298,4479)    (1298,13573)
(5952,4296)     (5952,7191)    (10233,25579)
(14383,14400)   (15465,16767)  (16084,17362)
(22963,22977)   (25152,25170).
```

Thus (2.1) removes at least eleven distinct cuts that otherwise satisfy the
current delete master with the same explicit `y` witness.  It is materially
stronger than the incumbent no-good `sum_{e in C}x_e<=98`.

This does **not** assert that any of the eleven cuts has an exact seam
completion.  It proves the opposite via (2.1).  Nor does it exclude the whole
delete branch.  Its value is that the obstruction is now projected to the
cut master and reused before any exact-add subproblem is built.

## 4. Reproduction

The structural certificate and the family replay are respectively

```text
python3 scratch/audit_k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.py
python3 scratch/audit_k16_r99_upper4_benders_family_20260729.py
```

The second command deterministically writes

```text
scratch/k16_r99_upper4_benders_one_swap_family_20260729.audit.json
```

with payload SHA-256

```text
012bf688e5d486b206e9bb6f348bfe042a95550e7415098f4c91e72fdf1406cd
```

and records zero solver invocations.
