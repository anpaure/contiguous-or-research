# `k=17`: full rooted-flag arc supply and the compact joint master

**Date:** 2026-08-02  
**Status:** unconditional arc-supply theorem and exact finite formulation.
The solver verdict for the full joint formulation is pending.  This note does
not assert a `k=17` word.

## 1. Setting

Use the nine certified rank-eight-rooted types

\[
(a,b,c)\in\{(1,5,2),(1,6,1),(2,5,1),(3,3,2),(3,4,1),
(4,3,1),(5,1,2),(5,2,1),(6,1,1)\}.
\]

A full flag at a root `Q` is a partition

\[
                 Q=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2,
                 \qquad (|C_0|,|C_1|,|C_2|)=(a,b,c).
\]

For a physical Johnson turn

\[
 Q'=Q-\{\alpha\}+\{\beta\},
\]

the exact age criterion is

\[
 \alpha\in C_2,\qquad C'_1\subseteq C_0,
 \qquad C'_2\subseteq C_1.                         \tag{1.1}
\]

The owner colour is forced to be `Q union Q'`.

## 2. Exact local supply

### Theorem 2.1

Fix a source flag of type `s=(a,b,c)` and a destination type
`t=(a',b',c')`.  For each physical turn whose deleted coordinate belongs to
`C_2`, the number of destination flags of type `t` satisfying (1.1) is

\[
                    {a\choose b'}{b\choose c'}.     \tag{2.1}
\]

Consequently, before quotient self-turns are removed, the exact outgoing
degree of a source flag of type `s` is

\[
  9c\sum_t {a\choose b_t}{b\choose c_t}.             \tag{2.2}
\]

#### Proof

For a fixed turn, choose `C'_1` as any `b'`-subset of `C_0` and `C'_2` as
any `c'`-subset of `C_1`.  They are disjoint.  The remaining elements of
`Q'` form `C'_0`, and their number is

\[
 8-b'-c'=a'.
\]

This constructs every compatible destination exactly once.  There are `c`
choices of the departing coordinate and nine choices of the new coordinate,
which proves (2.2).  \(\square\)

There is a dual exact formula.  Fix a destination type `(a',b',c')`.  For
one incoming physical turn the newborn is a fixed element of `C'_0`.  For a
source type `(a,b,c)`, put

\[
 x=a-b',\qquad y=b-c'.
\]

The remaining `a'-1` elements of `C'_0` supply the extra source-age-zero and
source-age-one elements.  Thus the number of source flags is

\[
 {a'-1\choose x}{a'-1-x\choose y}.                  \tag{2.3}
\]

Summing (2.3) over source types and multiplying by the number of nonself
turns whose newborn lies in `C'_0` gives the incoming degree.

### Corollary 2.2 (no full-menu zero roots)

The complete `k=17` quotient contains only sixteen self turns among its
`1430*72` physical directed Johnson turns.  After deleting all self turns,
every one of the `2,722,720` rooted full flags still has positive outgoing
and incoming degree.  More sharply,

\[
             \min_f d^+(f)=168,
             \qquad \min_f d^-(f)=8.                \tag{2.4}
\]

The complete compatible flag-arc count is

\[
                    1,415,274,112.                   \tag{2.5}
\]

The per-type audit is:

| type | flags | one-turn outgoing sum | one-turn incoming sum | out range | in range |
|---:|---:|---:|---:|---:|---:|
| 0 | 240240 | 15 | 1 | 240--270 | 8--9 |
| 1 | 80080 | 21 | 1 | 168--189 | 8--9 |
| 2 | 240240 | 35 | 3 | 280--315 | 48--54 |
| 3 | 800800 | 33 | 6 | 528--594 | 150--162 |
| 4 | 400400 | 52 | 6 | 416--468 | 150--162 |
| 5 | 400400 | 69 | 14 | 552--621 | 476--504 |
| 6 | 240240 | 31 | 32 | 496--558 | 1376--1440 |
| 7 | 240240 | 78 | 32 | 624--702 | 1376--1440 |
| 8 | 80080 | 63 | 72 | 504--567 | 3744--3888 |

Therefore the 761 zero-out roots in the old frozen static table are not a
local scarcity theorem.  They are caused by making the static selection
before the chronology.  This conclusion is still only local: positive
degree does not imply the simultaneous lower palettes, owner rainbow, or a
Hamilton cycle.

The independent complete-menu replay is

```text
scratch/audit_k17_full_flag_arc_supply_20260802.cpp
```

and on the H100 CPU reports

```text
PASS flags=2722720 compatible_arcs=1415274112
min_out=168 min_in=8 self=16
```

## 3. Exact compact joint formulation

The generator

```text
scratch/build_k17_rank8_joint_flag_cycle_master_20260802.cpp
```

uses age-membership bits rather than the 1.415-billion compatible flag arcs.
It imposes simultaneously:

1. one full flag at each of the 1,430 rank-eight roots;
2. exact certified type multiplicities;
3. exact suffix palettes at ranks two through seven;
4. one selected directed arc into and out of every root;
5. the literal implications (1.1) on every selected arc; and
6. every rank-nine owner colour exactly once.

Type cardinalities use balanced binary adders.  The exact full model has

```text
variables    1,733,388
clauses     11,155,006
arcs           102,944
suffix vars    403,260
```

The rank-seven staged relaxation has

```text
variables      652,158
clauses      6,152,416
```

### 3.1 Exact two-matching factorization

The directed-root geometry has a smaller equivalent form.  Let `I` be the
9-regular quotient incidence multigraph between rank-eight roots and
rank-nine owners.  Choose two disjoint perfect matchings `D,H` in `I`.
Orient every selected `D` incidence from its root into its owner and every
selected `H` incidence from its owner into its root.

This gives a directed root cycle cover: at every root there is one incoming
and one outgoing selected incidence, and at every owner one root enters and
one root leaves.  Disjointness forbids the one-root loop.  Conversely, a
directed root cycle-cover arc

\[
                       Q\longrightarrow Q',
                       \qquad T=Q\cup Q'
\]

selects `(Q,T)` in `D` and `(Q',T)` in `H`.  These operations are inverse.
The quotient voltage is the difference of the two incidence phases.

For an owner `T`, condition every age implication on the conjunction of its
selected `D` and `H` incidences.  In the common physical gauge those
implications are exactly (1.1), so this factorization loses no literal
information and introduces no relaxation.

It reduces the geometry from 102,944 directed-arc variables to 25,740
oriented-incidence variables.  With the same binary counters, the resulting
masters have

```text
                    variables     clauses
rank-7 staged         316,172    5,388,956
full ranks 2..7     1,397,402   10,391,546
```

The companion incidence decoder independently reconstructs the ordered
turn at every owner rather than trusting the factorization:

```text
scratch/decode_verify_k17_rank8_joint_flag_incidence_20260802.cpp
```

An optional restricted mode retains only the connected sixteen-arc support
of the authenticated integral type circulation.  It is a sufficient search
subclass, not a necessary condition.

The independent decoder

```text
scratch/decode_verify_k17_rank8_joint_flag_cycle_20260802.cpp
```

reconstructs every selected flag and transition, replays the exact lower
palettes and owner colours, decomposes the selected permutation, computes
component voltages, and emits valid outgoing subtour clauses.  A terminal
PASS requires one quotient cycle with nonzero voltage.

## 4. Remaining scope

Even a PASS of this master proves only the joint lower/owner gate.  It does
not establish strict-upper or arbitrary-width witnesses, a physical safe
opening, or the final compiler, and therefore is not by itself a proof that
`nu(17)=24313`.
