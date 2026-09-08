# K16 bad2 detached-cycle pass 1: exact Hall core and local edit audit

Date: 2026-07-30  
Lane: AD independent audit  
Status: **PASS exact lower graph, matching deficiency 34, DM shore 249/215; one support-seven shore improvement; no Hall-zero claim**

## 1. Authenticated chronology

The audited chronology is

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/out7/pass_1.targets
SHA-256 aea7a05a8837298205e9f35f39c7e6b99b8e7ef00fe46dcab9a8ab831e018e34
```

Independent replay gives:

```text
length                    12873
forced flats              6320,12869,12871
lower-cell capacity       32063
maximal-envelope errors   0
empty maximal envelopes   0
upper holes               0
```

Thus the chronology is an exact middle carrier and is arbitrary-upper
complete.  It is not a complete compiler: the lower candidate graph below is
deficient.

## 2. Exact lower graph and Hall theorem

For every proper-prefix cell `(start,length)` with

```text
1 <= length <= forced_depth[start],
```

the auditor recomputes its maximal allowed mask, complete-carrier mandatory
mask, and every rank-at-most-seven target satisfying the exact nonempty-letter
cell law.  This gives

```text
left targets        26332
right cells         32063
incidences         347809
maximum matching    26298
deficiency             34
```

The independently recomputed matching agrees in cardinality with the frozen
matching.  Every one of the frozen `26,298` matching pairs was separately
checked for incidence, and both endpoint projections are injective.

Alternating reachability from all unmatched left vertices gives the canonical
Hall witness

```text
|X| = 249,   |N(X)| = 215,   |X|-|N(X)| = 34.
```

The complete lists of all 249 targets and all 215 right cells are frozen in
the JSON artifact in Section 6.  Every right-cell row records its interval,
allowed mask, mandatory mask, full shore-neighbour list, and connected
component root.

## 3. DM component decomposition and zero targets

The induced bipartite graph on the witness decomposes into 33 connected
deficient components.  Their shape histogram `(left/right/deficiency)` is

```text
19 x  1/0/d1
 1 x  3/2/d1
 2 x  4/3/d1
 1 x  5/4/d1
 2 x  7/6/d1
 1 x 10/8/d2
 1 x 15/14/d1
 1 x 18/17/d1
 1 x 21/20/d1
 1 x 23/22/d1
 1 x 34/33/d1
 1 x 35/34/d1
 1 x 44/43/d1.
```

The nineteen isolated `1/0` components are exactly the zero-degree targets:

```text
2665 28e9 29a9 4339 4378 4879 48e9 4e70 5439 5670
583c 5c70 6989 6a29 6a38 6a70 6b21 6c70 8000.
```

There are eighteen rank-seven zeros and the singleton `8000`.  Every zero is
inside the canonical Hall witness.  The unique deficit-two component has root
`4331` and shape `10/8`; its left side is

```text
4331 4370 4371 4372 4374 4770 4b70 6370 c331 c370.
```

This decomposition is stronger than merely listing deterministic unmatched
roots: it identifies exactly which new right vertices can reduce the fixed
shore deficit.

## 4. Smallest authenticated neighbour-adding edit in the saved trio

Among the three saved middle-exact, upper-complete detached-cycle outputs, the
smallest pairwise change is `pass_1 -> pass_2`.  It is one occurrence-labelled
support-seven cycle on positions

```text
784,785,1986,2498,5384,5385,6148.
```

In that order, the old values are

```text
4771,4739,5639,5671,5678,5479,4778
```

and the new values are the old values at positions

```text
785,6148,5385,784,1986,2498,5384,
```

namely

```text
4739,4778,5479,4771,5639,5671,5678.
```

Both endpoints have exact middle replay and zero upper holes.  On the *fixed
pass-1 shore*, the edit changes only six incidences:

| kind | target | cell | interval | allowed | mandatory |
|---|---:|---:|---:|---:|---:|
| gain | `4268` | 2364 | `[788,789)` | `4268` | `0060` |
| gain | `4331` | 7499 | `[2499,2502)` | `4731` | `0331` |
| gain | `4378` | 2360 | `[786,789)` | `4378` | `0178` |
| gain | `5670` | 18449 | `[6149,6152)` | `5670` | `1270` |
| loss | `4370` | 18449 | `[6149,6152)` | old `4770` | old `0370` |
| loss | `4770` | 18449 | `[6149,6152)` | old `4770` | old `0370` |

Cells `2364`, `7499`, and `2360` are genuinely new right vertices for the
pass-1 shore.  Cell `18449` is retargeted, not new.  Consequently the maximum
matching on the fixed 249-target shore rises exactly

```text
215 -> 218,
```

and its deficit falls `34 -> 31`.  However the full pass-2 graph has
deficiency `35`: the edit transports more deficit outside the old shore.  It
is therefore a precise local neighbour-adding gadget, not a global
improvement.  “Smallest” here means smallest among the three authenticated
saved outputs; no general support-at-most-six no-go is claimed.

## 5. Correct scope of the 57,216 loss-robust outer collars

The outer-collar roles

```text
0665, 2665, 8000
```

lie in three distinct pass-1 deficient components:

```text
0665 : root 0665, shape 7/6;
2665 : isolated 1/0;
8000 : isolated 1/0.
```

Thus three distinct new right vertices for those roles would, **conditional
on retaining all 215 old pass-1 shore cells**, reduce this shore's deficiency
from 34 to 31.

The qualifier “57,216 loss-robust collars” cannot be imported here.  That
loss audit was performed against the old `j3959` nine-target shore, not this
249/215 shore.  It does not prove that a collar retains these 215 cells or
avoids creating a new DM shore elsewhere.  A pass-1-labelled touched-cell
replay is required before any collar can be credited with even the
conditional three-unit gain.

## 6. Frozen artifacts

Independent audit source:

```text
scratch/audit_ad_k16_bad2_pass1_hall_core_20260730.py
SHA-256 3b59a29cc94312b3fd0f6902c7dd29a623214bd0de038a1d4b36799721c7e51b
```

Complete machine-readable witness, cells, components, and edit ledger:

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/
  pass1_hall_core.ad.audit.json
SHA-256 62f5be68bc6239839c84c7e34e521779f15ee84a5c7ae566a0e726cfe3ec71d1
payload d3b9c6fdeccdd5f8fdd099170f27fee94a1e4d55f6d185f6f76c81b436afec81
```

Frozen upstream Hall file, read but not trusted as a derivation:

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/hall_1.json
SHA-256 d231de3e8ebc8073ee4e2a00ec71ff90084786cbe587a1f429c05f915ce69a2e
```

## 7. Exact boundary

Proved:

- the full pass-1 lower incidence graph and maximum matching;
- the canonical 249/215 Hall shore and all 33 connected DM components;
- all nineteen zero-degree targets;
- every shore candidate cell and its exact cell masks;
- the support-seven pass-1-to-pass-2 local shore gain; and
- the three-component placement of the outer-collar roles.

Not proved:

- a support-at-most-six local-edit obstruction around pass 1;
- retention of the pass-1 shore by any outer collar;
- a common global letter assignment after such an edit or collar; or
- a length-12,873 universal word.
