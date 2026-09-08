# Thread D: corrected Lane-I exact A29 Benders row

Date: 2026-07-28

## 1. Frozen parent and quarantine

The fourth parent is read literally from

```text
scratch/k15_transposition_parent_winner.json
```

Its stored transposition `[1,12]` is **zero-based**, hence it exchanges
one-based coordinates `(2,13)`.  The corrected payload metadata is

```json
"tau_zero_based": [1, 12],
"tau_one_based": [2, 13]
```

The previous payload with SHA-256 beginning `d17b69e4` used bits `(0,11)`.
It and its descendants are quarantined in
`scratch/threadD_quarantine_wrong_tau_0_11/` and must never be used.

The freeze audit decodes the complete fourth path in both corrected payloads
and compares all 6,435 masks with the frozen winner.  It passes, with fourth
parent start/end masks `9901/7779`.  The corrected four-parent payload has
SHA-256

```text
cd754db2437b572a5d64642a362f4a662f7d93acaff5cd0cc075795df4d85287
```

## 2. Exact Lane-I interior states

For depth `h=0,1,2`, a centered state has `6+h` vertices and `5+h` selected
normal arcs.  Write these vertices as `Y_0,...,Y_{5+h}` and put

\[
 Q_i=Y_{i-3}\cap Y_{i-2}\cap Y_{i-1}\cap Y_i
 \qquad(3\le i\le5+h).
\]

The represented compiler cell uses `Q_4,...,Q_{4+h}`.  Lane-I's exact
mandatory identity gives

\[
 E=\bigcup_{i=4}^{4+h}Q_i,
 \qquad
 M=E\setminus(Q_3\cap Q_{5+h}).
\]

The native precomputer tests the fixed shore `A29` by the interval-zeta
formula, including row-intersection inclusion--exclusion.  It emits only
positive states.  For a positive state `gamma`, its model variable is

\[
 z_\gamma=
 \bigwedge_{e\in\gamma}x_e
 \wedge L_{v_0}\wedge R_{v_*},
\]

where `L_v` means the first state vertex is not at path position 0 or 1 and
`R_v` means the last state vertex is not at either final position.  These
guards leave exactly the six left and six right starts at each depth for the
endpoint circuit.

## 3. Exact nine-vertex endpoint circuit

The carrier is one `AddCircuit` through a dummy vertex.  Normal arc variables
are `x_uv`; dummy arcs choose the source and sink.  Vertex positions and their
inverse satisfy

\[
 x_{uv}=1\Longrightarrow \pi_v=\pi_u+1,
\]

with the dummy source/sink implications fixing positions `0` and `W-1`.
The inverse position variables expose the first nine vertices and the last
nine in reverse order.

For either nine-vertex collar, define

\[
 q_{p,a}=\bigwedge_{j=\max(0,p-3)}^p y_{j,a}
 \qquad(0\le p\le8).
\]

For boundary start `b=0,...,5` and depth `h=0,1,2`, let

\[
 e_{b,h,a}=\bigvee_{p=b}^{b+h}q_{p,a},
\]

\[
 m_{b,h,a}=
 \begin{cases}
 e_{b,h,a}\wedge\neg q_{b+h+1,a},&b+h<3,\\
 e_{b,h,a}\wedge\neg(q_{b-1,a}\wedge q_{b+h+1,a}),&b+h\ge3.
 \end{cases}
\]

Each of the 36 boundary claim variables selects one target from `A29` and is
allowed to be one only if the target satisfies `M subset T subset E` and
meets every cell row.  No scalar boundary credit appears anywhere.

## 4. Reusable exact/lazy row

The emitted row is

\[
 \boxed{
   \sum_{\gamma\in\Gamma^+}z_\gamma
   +\sum_{b,h}(c^-_{b,h}+c^+_{b,h})\ge L.
 }
\]

For `A29`, the requested Hall threshold is `L=1524`.

The row is exact after existential projection of its auxiliaries.  Every
positive interior cell has one selected centered state, and every interior
state selected by the path is forced to its exact indicator value.  A
boundary claim implies a literal fitting target.  Conversely, each genuinely
hit boundary cell can select such a target.  Therefore the row is feasible
exactly when `|N(A29)|>=L`.

`scratch/threadD_A29_laneI_cpsat.py` exposes this as

```python
carrier = add_carrier_circuit(model, payload, fixed_parent, counts)
cut = add_lane_i_cut(model, payload, carrier, patterns, threshold, counts)
```

Thus an outer Benders loop may solve the carrier first, discover the shore,
call `add_lane_i_cut`, and solve the same model again.  CP-SAT has no mutable
lazy-callback API; this solve/audit/add/resolve loop is the usable lazy form.
Adding the row initially is the exact static form.

The row is a Hall constraint, not a replacement for the host compiler's
factorability/residence constraints.  The standalone fixed-H29 regression is
factorable; a variable host model must continue to impose its existing
factorability gate separately.

## 5. Corrected four-parent audit

The parents are H29, H30, H31, and frozen `tau_zero(1,12)H29`.  The corrected
union and centered catalogue are

```text
vertices                         6,435
normal arcs                     18,753
tested depth 0/1/2       1,055,060 / 2,911,849 / 8,041,656
positive depth 0/1/2       46,787 /   258,723 / 1,305,135
positive total               1,610,645
pattern bytes                56,574,104
```

H100 native precomputation took 1.53 seconds and 33,792 KB maximum RSS.

The variable exact model has 1,670,294 variables and 3,285,016 high-level
constraints.  The fixed-H29 regression adds 6,436 fixing constraints, giving
1,670,294 variables and 3,291,452 constraints.  On H100 with
`PYTHONPATH=/dev/shm/orlib`:

```text
threshold 1495: OPTIMAL (feasible), build 33.35 s, solve 20.56 s
threshold 1496: INFEASIBLE,         build 26.01 s, solve 20.41 s
threshold 1524: INFEASIBLE,         build 27.23 s, solve 16.91 s
peak measured RSS: 3,884,724 KB
```

This pins the solver-side value to exactly 1495.  The independent native
regression also matches all 1,495 authoritative DM witness-cell indices and
finds all 18 left plus all 18 right boundary indicators equal to zero.

## 6. Corrected five-parent audit

The fifth parent is `scratch/k15_trans1113_balanced_hall31.json`.  The exact
catalogue is

```text
normal arcs                     22,451
tested depth 0/1/2       2,815,548 / 9,476,360 / 31,907,490
positive depth 0/1/2      144,989 /   916,304 /  5,325,300
positive total               6,386,593
pattern bytes               225,092,292
model variables              6,449,940
model constraints           12,840,610
```

H100 native precomputation took 4.56 seconds and 34,304 KB maximum RSS.  A
construction-only exact model build took 112.47 seconds and 6,257,576 KB
maximum RSS.  No five-parent solve was run, so no feasibility claim is made.

## 7. Artifacts and hashes

```text
scratch/threadD_A29_successor_zeta.cpp
scratch/threadD_A29_laneI_cpsat.py
scratch/threadD_A29_audit_provenance.py
scratch/threadD_A29_4parent_laneI_payload.json
scratch/threadD_A29_4parent_laneI_patterns.bin
scratch/threadD_A29_5parent_laneI_payload.json
scratch/threadD_A29_5parent_laneI_patterns.bin
scratch/threadD_A29_4parent_fixedH29_t1495.json
scratch/threadD_A29_4parent_fixedH29_t1496.json
scratch/threadD_A29_4parent_fixedH29_t1524.json
scratch/threadD_A29_5parent_laneI_build.json
scratch/threadD_A29_provenance_audit.json
```

Freeze hashes from the provenance audit:

```text
four-parent payload  cd754db2437b572a5d64642a362f4a662f7d93acaff5cd0cc075795df4d85287
four-parent patterns e90601e7a08feb493e6c5c6fdad319257f4b5eaf2ab46aa11d82632a496c68ff
five-parent payload  0018ed51e146992a26df4394651738a548abb8f38054f75c193e08b92ab28019
five-parent patterns f16ad6b1aeb0c2fca96902c3d1b04444399229c3267fab99342f9300108ced7c
```

Run `python3 scratch/threadD_A29_audit_provenance.py` before using any
descendant.  It checks metadata, complete binary length, edge counts, hashes,
and equality of every decoded fourth-parent mask with the frozen winner.
The CP-SAT builder additionally hashes the supplied payload and pattern file
against `scratch/threadD_A29_laneI_benders_manifest.json` and validates every
record's arc chain, preventing an order-dependent arc-ID catalogue from being
paired with a different graph having the same coarse counts.
