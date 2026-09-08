# Lane R: a q1-exact strict-C8/C6 packet lowers the full bank 73 to 66

Date: 2026-07-29

## 1. Baseline and result

Fix

```text
Q73 = scratch/k16_q1_endpoint_resume1_failedlit73_20260729.json
SHA-256 fa7d6edce1a71012d317220a97e0cf8900dd14d385087ea3a6d920a64d16e513

R = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

`Q73` is a simple spanning degree-two Johnson factor with zero lower/upper
q1 holes.  Against fixed `R`, its complete two-choice failed-literal replay
has

```text
short positive runs        2240
components                    4 = 1030+2630+2921+6289
unhit two-choice motifs      510
candidate bank               970
double-failed variables       73.
```

The result of this note is an explicit physical packet of replacement radius
seven, consisting of one strict-token C8 and one vertex-disjoint C6, which
preserves both q1 supports and gives

\[
 (\Phi,\mathrm{Res},\#\mathrm{components})\colon
 (73,2240,4)\longmapsto(66,2241,2).
\]

No new failed literal is created.  The resulting factor is still infeasible
because all 66 surviving variables are double-failed.

## 2. The minimum displayed `Q73/R` packet

Among the 73 frozen failed-literal proofs, the minimum union of dependency
rows has size 17 and occurs for either pivot

```text
(47458,63810), (63570,63810).
```

The common row set consists of fifteen palette/degree rows and two motif
rows.  Its two closures are

\[
\begin{aligned}
C_A&=\{(7526,7782),(7526,15714),(15466,15714)\},\\
C_B&=\{(48210,63570),(47458,63810),(63570,63810)\}.
\end{aligned}
\]

The first edge of each closure is common to `Q73` and `R`; the other four
are blue-removal variables.  The fifteen hard rows sum to

\[
 H_A+y\le h,\qquad H_B+d\le y,
\]

where

```text
H_A = b_(7526,15714) + b_(15466,15714)
H_B = b_(47458,63810) + b_(63570,63810)
y   = r_(48450,63810)
h   = b_(15686,15698)
d   = r_(57678,61766).
```

The motifs give `H_A,H_B>=1`, while the unit box gives `d>=0,h<=1`.
Their sum is `0<=-1`.  Thus this minimum displayed failed-literal core is
itself a real-linear Farkas packet, not merely a branching artifact.

Its current physical support has 21 edges: twelve blue, seven red, and the
two common closure edges.  The exact row tags and all provider/incidence
sets are replayed in

```text
scratch/k16_failedlit73_fullbank_20260729.audit.json
SHA-256 d03193607795d42865e16277888c4ea0c3c025499fcd78c966077a131cde7c47
```

## 3. Complete closure-plus-literal C4/C6 census

Enumerate every connected physical alternating C4 or C6 containing at least
one of those 21 edges.  Both orientations are used; trades are globally
deduplicated by sorted deleted/added edge sets, then filtered by literal
lower and upper q1 replay.

The exact counts are

| radius | target incidences | distinct trades | q1-exact trades |
|---:|---:|---:|---:|
| 2 (C4) | 141 | 130 | 1 |
| 3 (C6) | 5263 | 4936 | 14 |

Two of the fifteen retained trades already have an ordinary unit
contradiction.  The remaining full-bank score histogram is

```text
68^1, 69^4, 71^7, 75^1.
```

Therefore the complete C4/C6 floor in this closure-plus-current-literal
neighborhood is 68.  The unique best C6 is

```text
delete (47395,55587), (47458,63810), (55619,63747)
add    (47395,47458), (55587,55619), (63747,63810).
```

It has zero q1 holes, residence 2241, two components of lengths `2921,9949`,
and `Phi=68`.  It removes five old failed literals and creates none.

The complete census is

```text
scratch/k16_fl73_ab_support_c4c6_failed_literal_potential_20260729.audit.json
```

This completeness is only for connected C4/C6s containing a current closure
or row literal.  A trade may change a row by inserting a previously absent
provider without touching an old literal; that larger class is not claimed
complete.

## 4. Unique strict-token C8 through the two closures

For the strict-token subclass, every connected radius-four trade induces a
derangement of four token occurrences.  Hence its token permutation has type
`4` or `2+2`:

1. type `4` is a directed four-cycle in the lower/upper compatibility graph;
2. type `2+2` is a pair of token rectangles with opposite endpoint-boundary
   vectors.

Zero boundary together with a connected 2-regular physical symmetric
difference is necessary and sufficient for one alternating C8.  Exhausting
this normal form through all six physical closure edges gives

```text
compatibility arcs       501323
global token rectangles   12303
closure rectangles            7
physical type-4 C8s            1
physical type-(2+2) C8s        0.
```

The unique strict-token C8 is

```text
delete (39394,47554), (47458,63810),
       (55714,55746), (63778,63874)

add    (39394,55746), (47458,47554),
       (55714,63874), (63778,63810).
```

Its deleted and added lower-token multisets are both

```text
39362, 47426, 55682, 63746,
```

and its upper-token multisets are both

```text
47586, 55778, 63842, 63906.
```

It destroys `C_B` and preserves `C_A`.  Literal replay gives zero q1 holes,
unchanged residence 2240, two components `2921+9949`, and

\[
 \Phi:73\longmapsto68.
\]

It removes exactly

```text
(36210,36274), (40214,40274), (47458,63810),
(48402,48404), (63570,63810)
```

from the failed-literal bank and adds none.  Thus it Pareto-dominates the
best C6 on residence while attaining the same failed-literal score.

The complete strict-token enumeration and materialized endpoint are

```text
scratch/k16_fl73_ab_strict_token_c8_20260729.enumeration.json
SHA-256 989de7e55e412ac6b6db55a700015f871eef2062d54e20c1561341a1d9e1cab4

scratch/k16_q1_endpoint_resume1_failedlit68_strict_c8_20260729.json
SHA-256 3c92246050699e41ac1dc2f52b3582ad6fb3e4c605320a54c4d1d232cf289bf8

scratch/k16_failedlit68_strict_c8_fullbank_20260729.audit.json
SHA-256 6c3d917b21ea153784c6aaae4ce2b71cf0c75cb02ad57157759819912c783058
```

This is complete only for strict-token connected C8s that touch one of the
six current closure edges of `C_A union C_B`.  It is not the entire
strict-token neighborhood—a strict-token C8 could avoid those closures while
altering another tagged row—and it is not the class of all q1-cover-preserving
C8s.  The positive construction does not require either broader class to be
exhausted.

## 5. The radius-seven packet and an exact `Phi=66` endpoint

Compose the strict C8 with the vertex-disjoint A-side C6

```text
delete (7478,23846), (7526,15714), (15654,32034)
add    (7478,7526), (15654,15714), (23846,32034).
```

Physical vertex-disjointness makes the two switches commute.  Complete q1
replay is nevertheless required, because vertex-disjoint packets may still
share a palette label.  The combined factor passes that replay and has

```text
replacement radius          7
lower/upper q1 holes       0/0
short positive runs       2241 = 1^134 2^907 3^1200
components                   2 = 2921+9949
unhit two-choice motifs     508
candidate bank              967
failed literals              66.
```

Relative to `Q73`, the packet removes the seven failed literals

```text
(36210,36274), (40214,40274), (40280,44376),
(40280,56656), (47458,63810), (48402,48404),
(63570,63810)
```

and creates none.  The new exact endpoint and independent full-bank replay
are

```text
scratch/k16_q1_endpoint_resume1_failedlit66_20260729.json
SHA-256 56389a8e82461ac727b92680854771f7faba785da1d55769d9d3b20e84b394f0

scratch/k16_failedlit66_fullbank_20260729.audit.json
SHA-256 f0f00af6ac12208a755b146fd40ac85a37de8951afd57e77286610e0641890a5
```

This is an independent `Phi=66` construction.  A concurrent Lane-H route
has another `Phi=66` endpoint with one physical component and a 965-variable
bank, so the present two-component endpoint is not claimed to be the unique
or globally preferred representative of the score-66 frontier.  Its value is
the explicit commuting strict-C8/C6 mechanism.

The materializer is

```text
scratch/materialize_k16_fl73_to66_c8_c6_packet_20260729.py
SHA-256 8d4cd827808ac4c901397989f54562a39b026a61516120c6bcb372b37f6d213d
```

## 6. Proved boundary

The coefficient-one/k16 construction is not completed.  The proved boundary
is exactly:

1. the current `Q73/R` minimum displayed core is a two-motif real Farkas
   packet;
2. its complete current-support C4/C6 neighborhood has floor 68;
3. its closure-touching strict-token C8 subclass contains a unique,
   residence-neutral improvement to 68;
4. a commuting q1-exact C8+C6 packet improves the stated full-bank baseline
   from 73 to 66 by an independent route;
5. the new endpoint remains solver-free infeasible because `Phi=66>0`.

No claim is made about arbitrary q1-exact C8s, deeper shadows, a resident
overlay circulation, connectivity to one physical cycle, `COMP3`, or a
literal k16 word.  All work was deterministic and local-light.  No H100 job,
SAT/CP solve, GPU task, or web query was launched under the active resource
moratorium.
