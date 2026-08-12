# The `k=16` even-equivariant interface: exact reconciliation and quotient factor model

Date: 2026-07-29  
Status: exact audit and exact finite reduction. No `k=16` word is claimed.

## 1. Verdict on the retained factors

The local three-switch artifact

```text
scratch/k16_seed0_bresident_c6packet.components.json
```

has eight physical components of lengths

```text
6225,45,35,35,35,20,20,20.
```

It is **not** rotation invariant. Its 6435 edges occupy 432 rotation
classes with multiplicities

```text
15^426, 12^3, 3^3.
```

Consequently it cannot literally be the `B` part of an equivariant `(c,t)`
deck. This is a statewise obstruction, not a failure of a chosen indexing.

There is, however, an exact repair. Apply all fifteen rotations of any one
of the thirty certified `C6` switches in

```text
scratch/seed0.upperq1.dualresident.c6switches.json.
```

The resulting factor is rotation invariant, still has eight physical
components with the same length multiset, covers all 5005 rank-six colours,
and has no positive run shorter than four. Its quotient has four cycles:

| quotient length | voltage mod 15 | physical lifts |
|---:|---:|---:|
| 415 | 2 | 1 |
| 7 | 12 | 3 |
| 4 | 9 | 3 |
| 3 | 13 | 1 |

Thus symmetrizing the switch solves equivariance without sacrificing the
proved `B`-residence or `q1` coverage.

It does **not** yet give a `(c,t)` carrier. In a `(c,t)` chronology, every
quotient `B` path is a one-run of the fixed-coordinate word `t`. The quotient
3-cycle can only become a three-vertex `B` path after opening, and that run is
repeated fifteen times in the physical lift. Depth-three residence requires
length at least four. One global linear cut can hide at most one physical
copy, not the other fourteen. Therefore this particular symmetric
eight-component factor still needs one further quotient-level merge or
rethreading.

The same factor is not bi-resident: its complement shore has 1125 short
runs (`360` of length two and `765` of length three). So it is a solved
resident `B` rail, not a completed two-rail lift.

## 2. Why the `k=14` six-piece braid is not a `(c,t)` example

The optimal `k=14` middle path has length 3432 and the even-equivariant period
would be `3432/13=264`. Its closing endpoints have symmetric difference eight,
so it is not a cyclic Johnson deck. More decisively, no coordinate trace is
264-periodic. The mismatch counts range from 1062 to 1770; even the new
coordinate has 1062 mismatches.

This agrees with the literal six-piece schedule

```text
A1, B2(reversed), A3, B1, A2(reversed), B3
```

whose new-coordinate runs have lengths `3,966,747` and gaps `270,1027`
(with the two boundary gaps joined cyclically). The six-piece braid is a
genuinely non-equivariant construction. It is evidence for a braid fallback,
not evidence that `(c,t)` already contains the known even optima.

## 3. The direct 858-vertex quotient graph

Let `A` be the 429 orbits of old rank-eight owners and `B` the 429 orbits of
old rank-seven owners. Use one binary variable for every `C15`-orbit of a
Johnson edge in the rank-eight layer of `[16]`.

The exact graph census is:

| edge type | edge orbits | quotient loops | meaning |
|:---|---:|---:|:---|
| `AA` | 12012 | 14 | old rank-8 Johnson edge |
| `BB` | 12012 | 14 | old rank-7 Johnson edge |
| `AB` | 3432 | 0 | containment rung `B subset A` |
| **total** | **27456** | **28** | |

For a non-loop edge variable, selection contributes one to the degree of
each endpoint orbit. A quotient loop contributes two to its single endpoint.
The central factor equations are therefore

\[
 \sum_{e\ni v,\ e\text{ non-loop}}x_e
 +2\sum_{e\text{ loop at }v}x_e=2
 \qquad(v\in A\sqcup B).
\]

These 858 equations are the exact rotation-equivariant 2-factor condition.
Unlike `(c,t)`, they do not prescribe a single quotient Hamilton chronology.

## 4. Exact simultaneous `q1` rows

There are four independent palettes:

1. lower without `z`: rank-seven old targets, from `AA` intersections and
   `AB` lower endpoints;
2. lower with `z`: rank-six old targets, from `BB` intersections;
3. upper without `z`: rank-nine old targets, from `AA` unions;
4. upper with `z`: rank-eight old targets, from `BB` unions and `AB` upper
   endpoints.

For every target orbit `O`, impose the corresponding cover inequality

\[
                        \sum_{e:\operatorname{col}(e)=O}x_e\ge1.
\]

The row sizes are exact:

| palette | target orbits | candidate edge-orbit counts |
|:---|---:|:---|
| lower no-`z` | 429 | `28 AA + 8 AB = 36` each |
| lower with `z` | 335 | `36 BB` for 333 rows; `12 BB` for 2 rows |
| upper no-`z` | 335 | `36 AA` for 333 rows; `12 AA` for 2 rows |
| upper with `z` | 429 | `28 BB + 8 AB = 36` each |

Thus the static core has 27,456 binary variables, 858 weighted degree rows,
and 1,528 cover rows. This is smaller and less rigid than a fixed-position
`(c,t)` model.

## 5. The size-five exceptional target orbits

At old ranks six and nine there are 335 target orbits, not 333. Exactly two
at each rank have size five:

```text
rank 6: 3171 = {0,1,5,6,10,11}
        5285 = {0,2,5,7,10,12}

rank 9: 7399, 11627
```

The rank-nine rows are the complement orbits of the displayed rank-six rows.
For a target orbit `O` of size `s_O`, one selected equivariant seam orbit
gives uniform physical load

\[
                       \frac{15}{s_O}
\]

to every target in `O`. Hence generic loads are integral multiples of one,
whereas the exceptional loads are integral multiples of three. The cover row
is still `sum x_e >= 1`, but an exceptional row has only twelve candidate
edge orbits and its first witness already creates ten unavoidable excess
physical occurrences.

In the `(c,t)` specialization with `R` one-runs of `t`, each hard palette has
`429-R` seam orbits. It must cover 335 target orbits, so

\[
                              R\le94.
\]

At equality, each hard palette has physical excess `20`: each of its two
size-five target orbits consumes one seam orbit of fifteen occurrences to
cover five targets, forcing excess ten. Thus the two hard palettes together
have forced excess `40`. The weaker raw occurrence count gives `R<=95` and is
wrong by exactly these exceptional orbits.

## 6. Voltage and residence are exact post-core constraints

Give every quotient edge its phase label. A selected quotient cycle with
voltage `v` lifts to `gcd(15,v)` physical cycles. Component control can be
handled by ordinary lazy subtour/merge cuts; a coprime nonzero voltage gives
one physical lift, but coefficient-one compilation does not require every
quotient component to have this property.

Residence is also finite and local after lifting. For every coordinate, a
forbidden run is a selected path with trace `0 1^ell 0` for `ell=1,2,3`;
bi-residence adds `1 0^ell 1`. Such a witnessed motif yields the sound clause

\[
                       \sum_{e\in P}x_e\le |P|-1.
\]

The rotation-closed `C6` calculation above proves that quotient alternating
switches can improve component topology while preserving `q1` and one-shore
residence. What remains open is simultaneous two-shore residence, deeper
shadows, a safe opening/braid, and exact `COMP_3`.

For the distinguished coordinate alone there is a compact exact eager
encoding.  Put

\[
 y_v=\sum_{e\ni v,\ e\text{ cross-shore}}x_e.
\]

The degree-two equations make `y_v` the number of shore changes at `v`.
Impose `y_v<=1`; this excludes a shore run of length one.  For each selected
same-shore edge `uv`, impose

\[
 x_{uv}+y_u+y_v\le2,
\]

excluding length two.  Finally introduce, for every oriented same-shore
incidence `(v,vu)`, the product flag

\[
 p_{v,vu}=x_{vu}\wedge y_u
\]

and impose

\[
 \sum_{vu\text{ same-shore}}p_{v,vu}\le1
 \qquad\text{for every }v.
\]

If a shore run has length three, its middle vertex has two selected
same-shore neighbours which are both boundary vertices, violating the last
row. Conversely every violation of one of these three systems displays a
run of length one, two, or three. Hence these constraints are necessary and
sufficient for the top coordinate and its complement on every
non-monochromatic quotient component to have cyclic run length at least
four.  A monochromatic component additionally needs the voltage-length test
stated below.  The encoding uses only 858 boundary variables and 47,992
oriented **non-loop** same-shore incidence product variables, rather than
enumerating roughly 1.3 million same-shore two-paths.

The CP-SAT implementation uses the projection-equivalent lower definition

\[
 p_{v,vu}\ge x_{vu}+y_u-1,
 \qquad y_v+\sum_{vu}p_{v,vu}\le1.
\]

When either input is zero the auxiliary may be chosen zero, so the omitted
upper directions do not change the projected feasible set; when both inputs
are one the displayed lower row forces the flag.  The second row combines
the length-two and length-three exclusions.  The connected unit-voltage
model has `82,314` variables and `28,989` constraints before these rows, and
`131,164` variables and `78,725` constraints after them.

This local characterization is exact on every non-monochromatic quotient
cycle, hence in particular on a connected factor containing both shores.  A
disconnected monochromatic component has no boundary vertex; its whole lifted
cycle is one shore run and must still be checked by voltage lifting.  The
independent replay below performs that check rather than silently treating a
boundary-free component as resident.

## 7. A deterministic top-bi-resident warm factor

The complementary centered-PBBS factor itself has no cross edges.  In the
canonical sorted edge-orbit catalogue, apply the square switch

```text
remove 8195, 24348
add    8216, 13450.
```

This is not a heuristic CP-SAT incumbent.  The compact certificate is

```text
scratch/k16_qfactor_topresident_square_warm_20260729.json
```

and the independent replay, which rebuilds the PBBS map and all 27,456 edge
orbits without importing the search implementation, is

```text
scratch/audit_k16_qfactor_topresident_square_warm_20260729.py.
```

It proves the following exact census:

| quantity | value |
|:---|---:|
| selected edge orbits | 858 |
| cross-edge orbits | 2 |
| lower / upper `q1` orbit support | 764 / 764 |
| quotient / physical components | 117 / 155 |
| minimum positive top run | 15 |
| minimum zero top run | 15 |
| all-coordinate short positive runs | `1^15, 2^105, 3^930` |

The positive and zero top-run histograms are identical:

```text
15^5, 21^15, 45^9, 75^21, 105^23, 135^11, 165^1.
```

Thus this factor is an exact `q1`-complete warm start satisfying the eager
top-and-complement-top residence rows.  It is **not** Hamilton and it is
**not** resident on all old coordinates.  Those nonclaims are material: its
purpose is to seed connectivity/unit-voltage search without beginning from a
top-nonresident factor.

It selects four quotient loops (`7,15435,15450,27455`).  Their physical
lifts have long top runs, so they do not invalidate the literal residence
audit.  The connected `AddCircuit` model excludes every quotient loop and
must therefore change at least these four selected bits; “warm start” does
not mean that every circuit-model row is already satisfied.

## 8. A `q1`-complete top-bi-resident physical Hamilton cycle

A nearest-factor solve from the mixed ten-component seed produced a
loopless top-bi-resident factor with two quotient cycles.  They have 778 and
80 edges, voltages 2 and 9, and therefore lift to one component of length
11,670 and three components of length 400.  Exhaustive enumeration of all
two-edge splices between these two cycles gave the following census:

| splice filter | survivors |
|:---|---:|
| catalogue-realizable degree-preserving splices | 1,304 |
| both `q1` palettes remain complete | 30 |
| top and complement-top residence remain valid | 24 |
| quotient voltage is a unit modulo 15 | 22 |

The first canonical survivor is the square switch

```text
remove 22568, 25126
add    22572, 24966.
```

Its certificate and solver-free replay output are

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
scratch/k16_qfactor_q1_topresident_hamilton_20260729.audit.json.
```

Rebuilding the 27,456-edge catalogue and lifting the selected 858 edge
orbits proves:

| quantity | value |
|:---|---:|
| lower / upper `q1` orbit support | 764 / 764 |
| quotient components | 1 |
| quotient voltage | 11 |
| physical components / length | 1 / 12,870 |
| selected cross-edge orbits | 80 |
| minimum positive / zero top run | 4 / 4 |

Thus one physical Hamilton cycle now simultaneously satisfies exact lower
and upper `q1` coverage and the eager top-and-complement-top residence
system.  This is still not the final resident Gray cycle: the other fifteen
coordinates have short positive-run census

```text
1^330, 2^1620, 3^1440.
```

The canonical catalogue digest is
`e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

## 9. Reproduction

Run

```bash
python3 scratch/audit_k16_ct_and_quotient_factor_20260729.py
```

to produce

```text
scratch/k16_ct_and_quotient_factor_20260729.audit.json
```

The audit is deterministic and performs no search.

Replay the warm factor independently with

```bash
python3 scratch/audit_k16_qfactor_topresident_square_warm_20260729.py
```

which writes

```text
scratch/k16_qfactor_topresident_square_warm_20260729.audit.json.
```

The retained hashes are

```text
e186c4bb77071dc1dd3ce3c895f368664a208fc94c6fc1e960ceb2c1c7f73256  certificate
4a687b9c99d11f327ac6b769f365ba2d86fd753370d3af92c3464c709b676650  independent replay
eaf46d967f4db1dbe440e49dc1c06a23f7a79450d39dc5aa2827c42cb876a67e  replay output
```

Replay the top-bi-resident Hamilton factor with

```bash
python3 scratch/k16_even_necklace_q1_factor_20260729.py audit \
  scratch/k16_qfactor_q1_topresident_hamilton_20260729.json \
  --output scratch/k16_qfactor_q1_topresident_hamilton_20260729.audit.json
```

The retained hashes are

```text
f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5  certificate
f51c1cba8d540fda4cf148b68b7bbc71a3c04407f4182cfba641fa255bce1624  replay output
```
