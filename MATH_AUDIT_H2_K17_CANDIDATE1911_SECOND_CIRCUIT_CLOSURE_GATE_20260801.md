# K17 connected candidate 1911: exact second-circuit closure gate

Date: 2026-08-01  
Lane: H2 independent connector audit  
Status: **exact provider/closure theorem and one-side simple-circuit no-go
through length six; longer and mixed circuits remain open.**

## 1. Frozen input and exact base state

The connected factor is

```text
scratch/h2_k17_dev5_candidate1911.factor.tsv
SHA-256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

Its generating summary is

```text
scratch/h2_k17_dev5_candidate1911.source.json
SHA-256 d719fb01468188d827659d523677414cfb7b9244d5af567c42a87137bf19110b
```

Independent reconstruction of all 2,860 matching rows gives one quotient
cycle of length 1,430, voltage `9 mod 17`, all 1,144 rank-10 turn colours,
and exactly two missing rank-7 turn colours:

\[
                       E=0x00e0f,\qquad F=0x01547.                 \tag{1.1}
\]

The first H-side assignment circuit has eight owners.  The two holes are
literally the two unique old lower turns it deleted:

```text
owner 7711: old H 3829 -> new H 3826, 0x00e0f -> 0x00787
owner 7511: old H 3567 -> new H 3569, 0x01547 -> 0x01457
```

Thus a second circuit need not guess the debt provenance.

## 2. Assignment-digraph normal form

Fix one side `M` in `{D,H}` and hold the opposite matching fixed.  For each
owner `u` and each legal new incidence `e=(u,f)`, let `v` be the unique owner
whose current `M` edge occupies facet `f`.  Write

\[
                              u\xrightarrow[e]{}v.                 \tag{2.1}
\]

This is an arc of the assignment digraph.  A simple directed circuit

\[
 u_0\to u_1\to\cdots\to u_{t-1}\to u_0                         \tag{2.2}
\]

is exactly a one-side perfect-matching exchange: owner `u_i` receives the
old `M` facet of `u_{i+1}` through the stated incidence.  Conversely every
simple one-side matching circuit has this form.  New incidences equal to an
edge of the fixed opposite matching are forbidden.

A length-`t` circuit changes exactly `t` matching-owner rows and `t` facet
rows.  On the H side its changed successor tails are the `D^{-1}` images of
those facets; on the D side its `t` changed D rows are themselves the labelled
successor-tail support.  Rank-8 facet coverage remains exact automatically:
D is unchanged in the first case and remains facet-perfect in the second.

For an arc `e` define the literal resource increments

\[
\begin{aligned}
 \Delta_7(e)&=[L_{new}(u)]-[L_{old}(u)],\\
 \Delta_{10}(e)&=[U_{new}(f)]-[U_{old}(f)],\\
 \delta_s(e)&=s(e)-s(M(u))\pmod {17}.
\end{aligned}                                                     \tag{2.3}
\]

For a circuit `C`, exact palette preservation and repair are

\[
 \mu_r(T)+\sum_{e\in C}\Delta_r(e)(T)\ge1
 \quad(r=7,10;\ \hbox{every }T),                                  \tag{2.4}
\]

with positive gain on both targets in (1.1).  Exact retention of voltage
nine is

\[
 \sum_{e\in C}\delta_s(e)=0\pmod {17},                            \tag{2.5}
\]

on either side: an H circuit subtracts this sum from the factor voltage and
a D circuit adds it.  Finally, connectivity is not a scalar circuit row;
the decoded permutation `H'^{-1}D'` must be traversed and have one 1,430-
owner component.

Equations (2.1)--(2.5), opposite-edge exclusion, and literal traversal are
the exact support/resource balance law for the second circuit.

## 3. Provider census

Relative to candidate 1911, the assignment digraph has exactly

```text
                 providers of E     providers of F
H side                 10                  10
D side                 10                  10
```

These are provider *arcs*, not independently selectable turns.  Selecting
one forces its displaced owner into the same directed closure.  Hence the
correct small search is a circuit containing at least one E-provider and
one F-provider, rather than a Cartesian product of twenty local choices.

## 4. Unique smallest closure circuits

An exact DFS of simple assignment circuits, rooted at every E-provider and
limited only by length at most six, visits `190,529` H-side and `187,697`
D-side closure states.  It finds precisely two target-containing circuits
in total.  Every alleged circuit in this scope can be cyclically rooted at
one of the enumerated E-provider arcs, and the DFS rejects only a repeated
owner or the stated length cap, proving completeness.

### H side: unique C10

The unique H circuit has five selected matching edges and owner sequence

```text
7711 -> 7455 -> 13599 -> 14965 -> 7503 -> 7711
```

with new incidence IDs

```text
3830, 3517, 7957, 9158, 3559.
```

It gains `E` at `7711` and `F` at `14965`.  Its shift-change sum is `10`,
so the new total voltage is `9-10=16 mod 17`, not nine.  It also

```text
splits topology into components 348+640+442,
loses upper colours 0x01d9f,0x01f1f,0x0355f,0x0753d,
and leaves new lower holes 0x00b87,0x0151d.
```

### D side: unique C12

The unique D circuit has six selected matching edges and owner sequence

```text
7455 -> 3759 -> 7503 -> 5967 -> 11931 -> 7959 -> 7455
```

with new incidence IDs

```text
3510, 1047, 3562, 2296, 6790, 4145.
```

It gains `E` at `7455` and `F` at `7503`.  Its shift-change sum is `8`, so
the new total voltage is `9+8=0 mod 17`.  It also

```text
splits topology into components 427+568+384+51,
loses upper colours 0x0175f,0x01f4f,0x01f97,
and leaves the new lower hole 0x00b87.
```

There is no other simple one-side circuit of length at most six containing
providers for both debts.  In particular none can retain connectivity,
voltage nine, and the full upper/lower immediate palettes.

## 5. Exact surviving gate

The second-circuit repair is therefore reduced to one of the following
strictly larger classes:

1. a simple H-only or D-only assignment circuit of length at least seven;
2. two one-side circuits whose voltage and palette deltas cancel jointly;
3. a genuinely mixed D/H exchange, audited by the same signed resources;
4. reselecting the first circuit rather than repairing candidate 1911.

For any extension, the eager filters should be applied in this order:

1. directed matching closure and opposite-edge exclusion;
2. gain both `E,F` and enforce the full signed inequalities (2.4);
3. enforce zero net shift change (2.5);
4. traverse `H'^{-1}D'` for one component;
5. only then invoke residence or deeper-shadow replay.

This note makes no residence, higher-shadow, source, common-cap, compiler,
or K17 construction claim.

## 6. Audit artifacts

```text
scratch/audit_h2_k17_candidate1911_two_lower_circuit_interface_20260801.py
scratch/h2_k17_candidate1911_two_lower_circuit_interface_20260801.audit.json
```

The JSON includes all forty provider arcs, both unique shortest circuits,
their literal signed palette changes, voltage, and component decompositions.
