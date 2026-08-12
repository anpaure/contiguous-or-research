# Exact seed0-def4 four-cut no-go and endpoint-upper1 two-opt frontier

Date: 2026-07-31  
Lane: R  
Status: exact solver-free finite theorems in the scopes stated below; no K16 word

## 1. Frozen deficiency-four source

The first source is

```text
scratch/threadA_k16_fourfilter_q1_twoopt_frontier_20260731/cuts_2129_10447.targets
SHA-256 0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b
```

It is the complete rank-eight deck, has q1 hole `b8ce`, and has complete
upper deficit `{a9fe,b8ce,b8cf}`.  Its maximum-area P/Q schedule has selected
area 30,098 and generalized lower-Hall deficiency four, witnessed by 29
targets and 25 cells.

## 2. Forced-seam reduction for four cuts

Consider an exchange which deletes exactly four old path edges, adds exactly
four Johnson edges, retains the two path endpoints and reconstructs one path.
If it repairs q1 then one added edge is a facet edge of `b8ce`.  There are
exactly

\[
\binom 92=36
\]

such edges.

If it also creates `a9fe`, some new witness interval for `a9fe` must cross a
new edge, because the old order has no such witness and every interval wholly
inside a retained segment survives unchanged.  Both endpoints of this edge
are rank-eight subsets of `a9fe`.  The Johnson graph induced by those
\(\binom{11}{8}=165\) vertices has

\[
\frac12\binom{11}{8}\,8\,3=1980
\]

edges.  The two distinguished edges are necessarily different, because
`a9fe & b8ce = a8ce` has rank eight.

For each of the `36*1980=71,280` distinguished pairs, choose an incident old
cut for each of its four endpoint occurrences.  Four distinct cuts expose
eight endpoint degrees; subtracting the four distinguished incidences leaves
four endpoint deficits, whose three perfect pairings are exhaustive.  This is
an exact generation of the stated four-cut class, including the case where a
one-vertex segment receives two new incident edges.

The resulting exact ledger is:

| stage | count |
|---|---:|
| distinguished edge pairs | 71,280 |
| incident-cut assignments | 1,013,760 |
| four-distinct-cut assignments | 1,002,338 |
| residual endpoint pairings | 3,007,014 |
| rows with all four added edges Johnson | 13,361 |
| deduplicated configurations | 12,022 |
| q1-complete configurations | 19 |
| connected configurations | 8 |
| distinct connected target orders | 6 |

None of the eight connected configurations covers all three required masks.
In fact, every one still misses `b8cf`.  Their complete upper deficits and
optimistic P/Q capacities are:

| cuts | added edges | upper holes | capacity |
|---|---|---|---:|
| 1209,4113,6098,6172 | `21ee-a1ec;31ce-31ec;38ce-b84e;81ee-89ce` | `7bce,a5ee,a9fe,b8cf,b9ce,b9fe,e5ee` | 19,651 |
| 2129,5338,6098,6172 | `29ce-a1ce;31ce-b18e;38ce-b84e;89ce-a98e` | `7bce,b8cf,b9ce,b9fe` | 25,751 |
| 4113,5338,6098,6172 | `31ce-b18e;38ce-b84e;81ee-89ce;a1ce-a1ec` | `7bce,a5ee,a9fe,b8cf,b9ce,b9fe,e5ee` | 24,008 |
| 2129,5338,6098,6172 | `29ce-89ce;31ce-b18e;38ce-b84e;a1ce-a98e` | `7bce,b8cf,b9ce,b9fe` | 21,879 |
| 2129,5338,6172,12518 | `29ce-a1ce;31ce-b18e;38ce-b88e;998e-a98e` | `7bce,a9fe,b8cf` | 23,863 |
| 2129,6097,6098,12518 | `29ce-89ce;89ce-89dc;998e-a98e;b84e-b88e` | `b8cf,b9ce,b9fe` | 21,886 |
| 2129,6098,6099,12518 | `29ce-89ce;998e-a98e;b05e-b84e;b84e-b88e` | `b8cf,b9ce,b9fe` | 21,886 |
| 2129,2130,6098,12518 | `29ce-89ce;998e-a98e;a98e-a996;b84e-b88e` | `b8cf,b9ce,b9fe` | 21,886 |

The last three cut representations materialize the same target order.  The
best capacity is 25,751, below the necessary 26,332.  Thus this standard
four-cut class is dead both at upper support and at scalar compiler capacity;
it cannot preserve the old 29/25 Hall shore.

This theorem does not cover a relocated non-Johnson P/Q seam, five or more
cuts, endpoint changes or value edits.

## 3. Stronger endpoint-transport source

The next source is

```text
scratch/k16_seed0_def4_endpoint_transport_upper1_targets_20260731.word
SHA-256 d310b08fddfdd49d019d9a656350377c4d2695ae972e6be8ebac8c7ae99b430f
```

It is q1-complete and its sole upper hole is `a9fe`.  For any reversal cutting
after positions \(a<b\), the new seams are

\[
T_aT_b,\qquad T_{a+1}T_{b+1}.
\]

If the reversal creates `a9fe`, at least one of those seams has both endpoints
among the 165 `a9fe`-contained occurrences.  Enumerating the two possible seam
roles gives 25,421 distinct cut pairs.  Exact adjacent-q1 multiplicity replay
and literal all-width upper replay give:

| stage | count |
|---|---:|
| contained positions | 165 |
| candidate cut pairs | 25,421 |
| q1-safe reversals | 343 |
| reversals creating `a9fe` | 26 |
| reversals preserving every upper target | 11 |

The 11 full-upper descendants have capacities

```text
cuts 505,7775      24741
cuts 2216,7587     18253
cuts 2841,7775     25751
cuts 2841,8328     28199
cuts 2843,7586     25751
cuts 2843,7775     17974
cuts 2843,8582     22907
cuts 3908,7775     20656
cuts 5448,12704    29868
cuts 7775,11744    27784
cuts 7775,12704    25419
```

Only the reversals with cuts `(2841,8328)`, `(5448,12704)` and
`(7775,11744)` pass the necessary scalar threshold.  Exact generalized Hall
at each descendant's maximum-area schedule gives respective deficiencies

\[
4,\quad75,\quad1625.
\]

## 4. New authoritative full-upper lead

The best descendant cuts after positions 2,841 and 8,328 and reverses the
inclusive block

\[
T[2842\ldots8328].
\]

Its removed boundary colours are `097f,897e`; its inserted colours are
`897f,897e`.  The target order is

```text
scratch/r_k16_endpoint_upper1_twoopt_20260731/full_upper_3_cuts_2841_8328.targets
SHA-256 ffd939890f90d30ab992507a92a7ca18315e335f705dc9ef7513ca7d2ebdd584
```

It contains every rank-eight mask once, is q1-complete and is complete at
every upper rank.  Its exact maximum-area P/Q schedule is

\[
X=\{8333,12871,12872\},\qquad Y=\{0,1,5885\},
\]

with selected area 28,190 and optimistic capacity 28,199.  The exact lower
graph has 366,212 incidences and maximum matching 26,328/26,332.  Its
canonical Hall shore is exactly four isolated zero-host targets,

\[
\{\mathtt{29cc},\mathtt{38c6},\mathtt{38ca},\mathtt{898d}\},
\]

so the witness is `4/0`.  In particular, this move removes the previous
nontrivial 30/25 shore but does not yet compile.

The Hall statement is exact for this maximum-area schedule.  Other P/Q
schedules of the same target order, compound rethreads and value edits remain
open.  A perfect marginal matching would still require common capped-envelope
and literal word replay.

## 5. Artifacts

Four-cut class:

- `scratch/audit_r_k16_seed0_def4_fourcut_rethread_20260731.cpp`
  - SHA-256 `0025015605094e7137d0a294bf890f43bf4f3ddaa8faba30ca4b0f9339ce1afc`
- `scratch/audit_r_k16_seed0_def4_fourcut_rethread_independent_20260731.py`
  - SHA-256 `cb90197d92f307ea0202260af032a7ed03aed4102bb33ff3ea50c63d477959d4`
- `scratch/r_k16_seed0_def4_fourcut_rethread_20260731/independent.audit.json`
  - SHA-256 `2358d3f47418ac55f53f66648b0df9985f27ee3db4eef9d1ffeb0560805d65a7`
  - payload SHA-256 `dbf4e936320da442c6c35ca4c6acca063f74c702066b1385f38af259f192238f`

Endpoint-upper1 frontier:

- `scratch/audit_r_k16_endpoint_upper1_twoopt_20260731.cpp`
  - SHA-256 `fdff9fc9010c926e58e5e6c8a614ebe7998caaccc11b9660c31c64de6f9f40be`
- `scratch/audit_r_k16_endpoint_upper1_twoopt_independent_20260731.py`
  - SHA-256 `6d8fd55f7e63105b565b722d769b3677744e63adaa433c981cb5647c55404397`
- `scratch/r_k16_endpoint_upper1_twoopt_20260731/independent.audit.json`
  - SHA-256 `752b301d8637ed92e0377fc4193e8c8aaac6a5d192e590ed527bfda89bfd2e2b`
  - payload SHA-256 `7c79295640b85c3bd7040dea633166d00e70476dcfd3201f2d7ad58bca0aa024`
- best fixed-schedule Hall audit
  - `scratch/r_k16_endpoint_upper1_twoopt_20260731/full_upper_3_cuts_2841_8328.hall.json`
  - SHA-256 `fcd65a9635ab83558aa7b2068a361192b6617afa252fbf527e3980e4b574586a`
  - payload SHA-256 `9640c379811c410bcffbb02ac423289c6b975949a5ede7867cc37bb080afdeae`
