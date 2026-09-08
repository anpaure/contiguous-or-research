# Independent audit of the `k=17` marker58 directed-history master

Date: 2026-08-02  
Status: **PASS for the exact loopless directed-cycle-cover and cyclic positive-residence extension of the frozen round-one face stated below.**  The frozen base already contains two incumbent component cuts and 316 residence blockers.  The formula does not yet enforce one quotient Hamilton cycle, nonzero component voltage, a literal opening/collar, ranks `11+`, source placement, or compiler feasibility.  No SAT or UNSAT conclusion is made.

## 1. Frozen object and verdict

The audited builder is

```text
82a20aeec38a0ebce6467c2558a1b604a32fbed26b2818d7d2575a82af75dc4a
  scratch/build_k17_marker58_directed_history_master_20260802.cpp
```

It was applied to the authenticated inputs

```text
c6638107ba4d1241403f914b5893614d9660a48cde7e43bef495b5fe28ebed52
  marker58_residence_round1.cnf
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  marker58_residence_round1.map.tsv
88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
  k17_marker_orbit.witness.tsv
```

with `base_count=58` and `open_edge=3`.  The generated main formula and map are

```text
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
7827cb0c8b7925d5fca73f37d0cd6cbc8567eff51f6609ecca8b6681bf29a7fb
  marker58_directed_history.map.tsv
```

under

```text
/home/amodo/or15/work/root_k17_directed_history_master_20260802
```

An independent implementation reconstructed every fixed edge and directed
arc, checked all seventeen physical developments of every arc, and compared
all `3,904,557` clauses in order.  It returned

```text
PASS_AD_K17_DIRECTED_HISTORY_MASTER_INDEPENDENT_AUDIT
```

with frozen artifacts

```text
abb3e3ee576f159d1e594936f4d696433ce3ad830470f394518859ca431f6b04
  scratch/audit_ad_k17_directed_history_master_20260802.cpp
058ea27da915f591b7214256d7b1e4ca22a21b8c94a36eb7a125b3f0b8f74970
  scratch/ad_k17_directed_history_independent_audit_20260802/
    directed_history.independent.audit.json
0149d13f0f58ce0d9f8dd49c85afbe884c782db6197f7dc800fc7b62a04e7ff3
  scratch/ad_k17_directed_history_independent_audit_20260802/audit.stdout
```

The builder itself does not hash-bind its three inputs: it checks the map and
witness semantically but checks only the base CNF header before copying its
body.  The verdict above is therefore tied to the displayed hashes, not to an
arbitrary file passed under the same filename.

## 2. Exact rotation convention

Let `rho` be cyclic coordinate rotation on `Z_17`.  Write a stored physical
directed edge as

\[
 A_{\rm phys}=\rho^s\bar A\longrightarrow
 B_{\rm phys}=\rho^t\bar B,
 \qquad \delta=t-s\pmod {17},                         \tag{2.1}
\]

where `bar A,bar B` are the canonical owner representatives.  Rotating both
ends by `-s` gives

\[
             \bar A\longrightarrow\rho^\delta\bar B.  \tag{2.2}
\]

Thus a physical coordinate with source-frame label `j` has target-frame
label

\[
                         j-\delta\pmod {17}.             \tag{2.3}
\]

If the inserted coordinate has label `q` in the source frame, its target
label is `q-delta`.  Consequently the implementation lines

```text
inserted_at_target = inserted_source_frame - delta
shifted            = value - delta
```

have the correct sign.  Reversing the edge swaps its physical endpoints and
produces `-delta`, the reversed deletion, and the reversed insertion.

The independent audit checks (2.1)--(2.3) for every one of the seventeen
developed copies of all `71,874` directed arcs.  In particular this is not a
representative-only or sample check.

## 3. Fixed-marker reconstruction

For each of the first fifty-eight frozen bases `x`, the builder reconstructs

\[
 U=\{0\}\cup x\cup\{1,2,3,4,5\},                       \tag{3.1}
\]

the same five-cycle used by the independently audited marker58 quotient
builder, opens it at edge three, and takes its four consecutive path edges.
This gives `58*4=232` fixed quotient edges.

Every reconstructed fixed edge is checked against the stored map row for

* its rank-eight facet orbit;
* both rank-nine owner orbits;
* its rank-ten cap orbit;
* its signed `Z_17` voltage; and
* literal ranks `8,9,9,10`.

The complete fixed stream is consumed exactly once.  A wrong witness prefix,
opening type, fixed-row order, or marker convention therefore fails before
formula generation.

## 4. Orientation rows are exact on the authenticated base

There are `35,713` residual options, of which eight are quotient loops.  The
new master forces all eight loop primaries false.  For every other residual
edge `e`, with primary `x_e` and the two directed literals `a_e,bar a_e`, it
emits the exact equivalence

\[
               a_e+\bar a_e=x_e.                         \tag{4.1}
\]

For each fixed edge it emits

\[
               a_e+\bar a_e=1.                           \tag{4.2}
\]

At each of the `1,430` owner orbits it emits one outgoing ALO and one incoming
ALO.  There are no separate outgoing/incoming AMOs.  They are nevertheless
logically redundant on this exact base:

1. residual facet exactness chooses exactly `1,198` residual edges;
2. every selected nonloop edge contributes two owner incidences;
3. the residual owner capacities sum to

   \[
                         2\cdot1198=2396;                 \tag{4.3}
   \]

4. the authenticated base owner rows impose those capacities as upper
   bounds.

Hence every base owner bound is tight and every owner has undirected degree
two after the `232` fixed edges are included.  Equations (4.1)--(4.2) orient
each incident edge exactly once.  Outdegree at least one and indegree at
least one then force one of each.

Thus the output is exactly a **loopless directed quotient cycle-cover** on
the frozen round-one strengthened face.  That face is the resource base plus
two incumbent component cuts and 316 residence blockers; it is not the raw
resource face.  The 316 blockers are redundant after the complete history
layer is added, while the two component cuts remain genuine inherited
restrictions.  The output is not yet a one-cycle/Hamilton formula.
Forcing the eight loops false is valid for the desired quotient-Hamilton
face, because a selected quotient loop consumes both degrees of its owner;
it does exclude some disconnected equivariant factors.

## 5. Exact last-three-insertion history

At an owner `v`, let

\[
 H_0(v),H_1(v),H_2(v)\in\mathbb Z_{17}                  \tag{5.1}
\]

be the last, second-last, and third-last insertion labels, expressed in the
canonical frame of `v`.  The formula uses a seventeen-way exact-one encoding
for each of these three values.

For a selected dart `a:u->v` of voltage `delta_a`, deletion label `p_a` in
the source frame, and insertion label `q_a` in the target frame, the emitted
clauses imply

\[
\begin{aligned}
 H_0(v)&=q_a,\\
 H_1(v)&=H_0(u)-\delta_a,\\
 H_2(v)&=H_1(u)-\delta_a,                                \tag{5.2}\\
 p_a&\notin\{H_0(u),H_1(u),H_2(u)\}.
\end{aligned}
\]

The propagation clauses are syntactically one-way implications.  They are
semantic equalities because the source slot is exact-one, the selected
incoming dart forces one target value, and the target slot is exact-one.
The incoming/outgoing proof in Section 4 supplies the unique selected
incoming dart.

No membership clause is missing.  `H_0` is forced to an actual insertion;
older slots are propagated actual insertion labels; and (5.2) prevents any
of them from being deleted while it remains in the three-slot history.

### Theorem 5.1 — exact residence projection

On the loopless directed quotient cycle-cover face, (5.1)--(5.2) are
equivalent to cyclic positive depth-three residence on every developed
physical component.

#### Proof

Write the directed projected owner transitions as `T_i->T_(i+1)`, with
insertion `q_i` and deletion `p_i`.  Equations (5.2) give, in the current
frame,

\[
             H(T_i)=(q_{i-1},q_{i-2},q_{i-3}).            \tag{5.3}
\]

The coordinate-frame changes telescope by (2.3).  The deletion row is
therefore exactly

\[
                 p_i\notin\{q_{i-1},q_{i-2},q_{i-3}\}.   \tag{5.4}
\]

If a coordinate is inserted at transition `i-l` and next deleted at `i`,
its positive owner run has length `l`.  Equation (5.4) forbids precisely
`l=1,2,3` and allows `l>=4`.  Conversely every positive run of length at
most three violates the corresponding term of (5.4).  The cyclic history
relations include each component's closing dart, so there is no untyped
history reset.  Finally, a coordinate which is constant one on a whole
physical component has run length equal to that component's circumference.
Every nontrivial Johnson component has an insertion on each transition; the
history rule forces the next deletion of that inserted coordinate at least
four transitions later.  Hence every accepted physical component has
circumference at least four, and the constant-one case is legal as well.
This proves the equivalence.  QED.

The theorem is one-sided.  It does not constrain deletion-to-next-insertion
gaps, negative runs, or arbitrary pairs of equal flip labels.

## 6. Exact dimensions and clause decomposition

The input map has

```text
fixed edges                 232
residual options          35,713
residual quotient loops        8
nonloop edges             35,937
directed arcs             71,874
```

The history block has

\[
               1430\cdot3\cdot17=72,930                 \tag{6.1}
\]

variables.  Starting from the `204,167`-variable base gives

\[
 204167+71874+72930=348971.                               \tag{6.2}
\]

The independently replayed added-clause ledger is

| row family | clauses |
|---|---:|
| loop bans and orientation links | 143,292 |
| owner incoming/outgoing ALO | 2,860 |
| history ALO | 4,290 |
| history pairwise AMO | 583,440 |
| insertion/deletion/transport, `38` per arc | 2,731,212 |
| **total added** | **3,465,094** |

The active build uses the `439,463`-clause round-one base, hence

\[
                  439463+3465094=3904557.                \tag{6.3}
\]

The same source can also be applied to the `439,145`-clause no-cut base; that
different scoped build has `3,904,239` clauses.  These two totals must not be
conflated.

## 7. Relation to the proposed Hamilton/path-age master

The builder closes the eager residence row but implements only part of the
larger proposal.

* It has no quotient order/root constraints and therefore permits several
  directed quotient cycles.
* It has no component voltage potentials or total-voltage row.
* It does not select a literal physical opening seam or a collar.

This omission is deliberate and scope-safe.  The history equations are
cyclic on every selected quotient component.  If later cuts force one
quotient cycle and its voltage is nonzero, the physical lift is one
`24,310`-owner cycle and Theorem 5.1 gives exact positive residence.  Since
`17` is prime, nonzero total voltage is sufficient at that point.

A quotient gauge edge is an orbit of seventeen physical edges, not one
literal opening.  One must not delete its history equation as though it were
a single linear seam.  A future rooted potential layer may use one quotient
edge to expose the total voltage, while retaining the history transition on
that edge.  A genuine physical collar requires its own phase-specific
transducer.

The present history encoding is also not proved variable-minimal.  A
five-state or threshold-age encoding uses fewer state variables; the chosen
last-three-insertion encoding has especially direct transition clauses and
matches the exact insertion-to-next-deletion theorem.

## 8. Canonical blocker bank and remaining gates

The authoritative cumulative blocker bank is the canonical `421`-row file

```text
8caaf19d74b161146e312a99e6e25d46d8e2e67b9e20785a4382bd066dc28106
  scratch/r2_k17_residence_master_round1_20260802/
    c10_escape_from3553/floor3502_b198_freeze/
    cumulative_round4.canonical.blocks.cnf
```

The provisional raw-text union `585` is rejected.  Every canonical blocker
is logically implied by the complete history layer, so the `421` rows are
valid redundant strengthening/regression rows, not a missing semantic part
of this formula.

An exploratory proofless Kissat process was still active when this audit was
frozen.  Its running state is no evidence of feasibility or infeasibility.
Any SAT output must still be decoded for quotient components, component
voltages, literal physical topology, and direct cyclic runs.  Any UNSAT line
without a checked proof is only a solver result.  Ranks `11--17`, a literal
opening/source chronology, maximal erosion, and terminal compiler/common-cap
feasibility all remain outside the formula.
