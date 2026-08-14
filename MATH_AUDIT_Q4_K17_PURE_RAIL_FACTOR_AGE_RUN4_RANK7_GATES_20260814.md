# Hostile audit: the q4 pure-rail age/run-four/rank-seven bridge is exact

**Date:** 2026-08-14

**Verdict:** PASS after two interface clarifications.  The literal rail
identities, cyclic wrap indexing, maximal run-four claim, rank-seven
lower-q2 identity, and five-core successor count are correct.  The audited
source now states explicitly why quotient positions give distinct marked
run-start orbits and requires the rank-seven type positions to be the
selected lower-q2 representatives.  It still makes no quotient-factor or
coloured-path feasibility claim.

## 1. Audited bundle

The pre-audit reduction had SHA-256

```text
df7e337f8f385a8b771b2552d675676e0b2af7482f536c8b5a94e37dfa2c6874.
```

The final audited source and replay are

```text
0b195aec1a3bf8f3b05c4314d2e8c8e91214fb257fbb01f03e909218bd9affbe
  MATH_REDUCTION_Q4_K17_PURE_RAIL_FACTOR_CLOSES_AGE_RUN4_AND_RANK7_GATES_20260814.md

27dc138f2744043e4368306d008f5824821e062795338db502133acc73122b10
  scratch/verify_q4_k17_pure_rail_age_run4_rank7_bridge_20260814.py

f4768658b462278f5a87bb2ea9166097d990153416faa70e6d434a7d54dca3ce
  scratch/verify_q4_k17_pure_rail_age_run4_rank7_bridge_20260814.h100.out

d132edbc6a0e17fb14906581d2229714f3c5475b2a0e1d8e271d3e91783a14b0
  scratch/verify_q4_k17_pure_rail_age_run4_rank7_bridge_20260814.h100.log
```

The exact replay line is

```text
PASS q4_pure_age_bridge periods=10,11 run4=all_positions marked_orbit_projection=12870_to_1430 rank7=L3 certified_demands=436+1144 core_states_max=30 legal_type_pairs=42
```

## 2. Edge indexing and maximal cyclic run

For a period `N in {10,11}` pure rail

\[
 O_i=C\cup\{s_i,s_{i+1},s_{i+2},s_{i+3}\},
\]

with distinct support labels, direct subtraction gives

\[
 O_i-O_{i+1}=\{s_i\},\qquad
 O_{i+1}-O_i=\{s_{i+4}\}.                         \tag{2.1}
\]

Thus the edge indexed `i` deletes `alpha_i=s_i` and inserts
`beta_i=s_(i+4)`.  At position `j`, the preceding edge is `j-1`, so

\[
 \beta_{j-1}=s_{j+3}=\alpha_{j+3}.                \tag{2.2}
\]

The coordinate `s_(j+3)` occurs in exactly

\[
 O_j,O_{j+1},O_{j+2},O_{j+3}.                     \tag{2.3}
\]

It is absent from `O_(j-1)` and `O_(j+4)`.  Distinctness of the support
labels and `N>4` make this valid even when any index crosses the cyclic
boundary.  Therefore `(2.3)` is maximal on both sides and has length
exactly four, not merely at least four.  The replay checks every edge and
every starting position separately at both periods and traverses a full
cyclic membership word from each start.

## 3. Distinct quotient run-start orbits

A marked run start is the translation orbit of a pair `(O,x)`, where `O`
is its first owner and `x` is its active coordinate.  Forgetting the mark
defines the projection

\[
 [(O,x)]\longmapsto[O].                            \tag{3.1}
\]

Consequently equality of two marked run-start orbits implies equality of
their owner orbits.  In a quotient-simple selected column the owner orbits
at its positions are distinct; the exact owner rows make them distinct
across all selected columns.  Hence all `1,430` quotient positions give
distinct run-start orbits.  Any 436 positions chosen for the
singleton-age-zero types therefore give 436 distinct required run starts.

The H100 replay exhausts all rank-nine owners on `Z_17`.  It finds `1,430`
owner orbits and `12,870=9*1,430` marked owner-coordinate orbits, and checks
that `(3.1)` is well-defined for every literal marked pair.  This is a
projection from 12,870 marked orbits to 1,430 owner orbits; the needed
injection is its contrapositive restricted to starts whose owner orbits are
distinct.

After translation development, each selected quotient start produces its
17 literal translates.  Thus the factor has one exact run-four start at
each of its 24,310 physical owner occurrences.

## 4. Rank seven is literally `L^(3)`

Three consecutive owners intersect in

\[
 O_i\cap O_{i+1}\cap O_{i+2}
   =C\cup\{s_{i+2},s_{i+3}\}=L_i^{(3)},            \tag{4.1}
\]

which has rank `5+2=7`.  The action of `Z_17` on rank-seven sets is free,
so there are

\[
 \binom{17}{7}/17=1,144                            \tag{4.2}
\]

target orbits.  A lower-q2 cover supplies at least one position over every
target.  Selecting one occurrence per target gives 1,144 pairwise distinct
positions, because one position has only one `L_i^(3)` value.  Their
developments contain every literal rank-seven set.

This supply statement must be coupled to chronology: the 1,144 certified
rank-seven types must be assigned exactly to those selected positions.
The pre-audit master listed lower-q2 coverage and type assignment as
separate rows without stating this selector.  The final source adds the
selector explicitly and preserves the correct scope: its prescribed type
positions may still fail to admit a cyclic core-refresh path.

If every lower-q2 load is in `{1,2}`, total load 1,430 forces exactly
`858` targets of load one and `286` of load two.  The replay verifies this
count and all 1,144 literal orbit keys.

## 5. Five-core successor count

At one position write the labelled core state as the ordered partition
`K=(K_0,K_1,K_2)`.  At the next position, a core label can enter age one
only by surviving from `K_0`, and it can enter age two only by surviving
from `K_1`.  No core label may enter age three, since that class is the
forced active singleton.  Hence a successor with sizes
`(k'_0,k'_1,k'_2)` is exactly a choice

\[
 K'_1\subseteq K_0,\quad |K'_1|=k'_1,
 \qquad
 K'_2\subseteq K_1,\quad |K'_2|=k'_2,              \tag{5.1}
\]

followed by the forced complement

\[
 K'_0=C-(K'_1\cup K'_2).                           \tag{5.2}
\]

The size identity `k'_0+k'_1+k'_2=5` makes `(5.2)` automatically have the
required size.  Therefore existence is equivalent to

\[
 k'_1\le k_0,\qquad k'_2\le k_1,                  \tag{5.3}
\]

and the exact number for a fixed labelled old state is

\[
 \binom{k_0}{k'_1}\binom{k_1}{k'_2}.               \tag{5.4}
\]

There is no omitted multinomial factor: after `(5.1)`, every remaining
core label is forced into `K'_0`.  The replay enumerates every labelled
partition of the five-core for all nine certified types and all 81 ordered
type pairs.  It obtains maximum state-menu size 30 and exactly 42 legal
type pairs, with `(5.4)` holding for every old labelled state.

## 6. Scope boundary

The audited bridge removes the two frozen **supply** obstructions:

* every quotient owner position offers a distinct exact run-four start;
* every rank-seven orbit can be offered by a lower-q2 position.

It does not prove that a mixed period-10/11 quotient factor satisfying all
owner/q1/q2 rows exists.  Nor does it prove that the selected rank-seven
positions and remaining certified types admit the required coloured cyclic
core path, ranks-two-through-six suffix transversal, safe component fusion,
upper continuation, or terminal cap.  These limitations are stated in the
final reduction.

All compilation, exhaustive replay, and hashing were performed through SSH
on H100.  The local Mac was used only for reading, editing, transfer, and
Git.
