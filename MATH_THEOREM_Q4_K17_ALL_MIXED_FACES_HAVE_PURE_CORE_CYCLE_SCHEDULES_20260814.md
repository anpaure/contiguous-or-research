# Every mixed q4 k17 face has a factor-independent pure-core cycle schedule

**Date:** 2026-08-14

**Status:** explicit finite theorem.  All fourteen mixed period-10/11 faces
admit closed cycles in the exact 72-state labelled five-core automaton whose
aggregate nine type counts are the frozen 1,430-position census.  Literal
cycle multisets are frozen and independently replayed.  This does not assign
the cycles to quotient factor columns and does not solve the rank-seven pin
coupling.

## 0. Result

Index the mixed faces by `0<=t<=13`:

\[
       a_t=143-11t,\qquad b_t=10t,
       \qquad 10a_t+11b_t=1430.                    \tag{0.1}
\]

Here `a_t` is the required number of period-ten cycles and `b_t` the number
of period-eleven cycles.  For every `t`, there is a multiset consisting of
exactly `a_t` closed length-ten state cycles and `b_t` closed length-eleven
state cycles whose aggregate type vector is

\[
 (139,297,8,20,20,140,127,237,442).                \tag{0.2}
\]

Thus the factor-independent type/core scheduling gate is feasible on every
mixed face, including the pure period-ten face `t=0` and pure period-eleven
face `t=13`.

## 1. Literal state graph

The nine type IDs, five-core profiles, frozen multiplicities, and labelled
state counts are

| id | type | core profile | count in `(0.2)` | labelled states |
|---:|---|---|---:|---:|
| 0 | `(1,5,2,1)` | `(0,4,1)` | 139 | 5 |
| 1 | `(1,6,1,1)` | `(0,5,0)` | 297 | 1 |
| 2 | `(2,5,1,1)` | `(1,4,0)` | 8 | 5 |
| 3 | `(3,3,2,1)` | `(2,2,1)` | 20 | 30 |
| 4 | `(3,4,1,1)` | `(2,3,0)` | 20 | 10 |
| 5 | `(4,3,1,1)` | `(3,2,0)` | 140 | 10 |
| 6 | `(5,1,2,1)` | `(4,0,1)` | 127 | 5 |
| 7 | `(5,2,1,1)` | `(4,1,0)` | 237 | 5 |
| 8 | `(6,1,1,1)` | `(5,0,0)` | 442 | 1 |

Their state counts sum to `72`.  A labelled state is an ordered partition
`K=(K_0,K_1,K_2)` of the abstract five-core with the displayed profile.
There is an arc `K->K'` exactly when

\[
                         K'_1\subseteq K_0,
              \qquad     K'_2\subseteq K_1.        \tag{1.1}
\]

The literal directed graph has `793` arcs.  A cycle certificate lists state
IDs; every consecutive pair and the final-to-first wrap must be an arc of
`(1.1)`.

## 2. Exact face census and decompositions

The independent replay obtains:

| `t` | period-10 cycles | period-11 cycles | all cycles | distinct certified words |
|---:|---:|---:|---:|---:|
| 0 | 143 | 0 | 143 | 28 |
| 1 | 132 | 10 | 142 | 31 |
| 2 | 121 | 20 | 141 | 15 |
| 3 | 110 | 30 | 140 | 20 |
| 4 | 99 | 40 | 139 | 15 |
| 5 | 88 | 50 | 138 | 15 |
| 6 | 77 | 60 | 137 | 27 |
| 7 | 66 | 70 | 136 | 16 |
| 8 | 55 | 80 | 135 | 16 |
| 9 | 44 | 90 | 134 | 21 |
| 10 | 33 | 100 | 133 | 18 |
| 11 | 22 | 110 | 132 | 22 |
| 12 | 11 | 120 | 131 | 32 |
| 13 | 0 | 130 | 130 | 18 |

The output certificates contain the complete compressed multiset
`(period,state word,multiplicity)` on every row.  For example, the `t=0`
certificate begins with

```text
2 * (0,61,10,62,9,61,10,65,6,70),
3 * (0,61,47,54,47,54,47,54,47,70),
```

both of period ten.  The `t=13` certificate begins with

```text
2 * (0,61,10,62,9,61,10,62,9,61,70),
2 * (0,61,50,11,38,24,20,32,30,17,70),
```

both of period eleven.  State IDs are resolved literally by the 72-row
catalogue embedded in the same certificate.  These displayed rows are only
examples; the committed JSON gives every word and multiplicity.

The search used a direct finite satisfaction model with one state variable
at every position, exact cyclic transition tables, and global type counts
`(0.2)`.  The theorem does not rely on solver optimality: the independent
replay reconstructs the graph without importing the search code and checks
every exported edge, wrap, multiplicity, period total, and type count.

## 3. What this solves

Given only a mixed face `(a_t,b_t)`, the theorem supplies the correct number
of abstract period-ten and period-eleven core/type cycles.  Relabelling the
abstract five-core by any bijection to a candidate rail core preserves
`(1.1)`.  Therefore there is no factor-independent obstruction from the
frozen type census or the exact core-refresh automaton on any mixed face.

In particular, the two extreme faces are positive:

```text
t=0:  143 closed period-10 cycles;
t=13: 130 closed period-11 cycles.
```

This statement is strictly about the age-state schedule.  It neither
selects quotient columns nor identifies a schedule cycle with a physical
rail.

## 4. The remaining rank-seven-pin coupling

Let `mathcal Q_N` be the selected quotient factor columns of period `N`,
and let `mathcal S_N` be the certified schedule-cycle copies of the same
period.  Their cardinalities agree by `(0.1)`.  For a schedule position put

\[
 r(s_i)=1 \quad\Longleftrightarrow\quad c_0(s_i)+c_1(s_i)=7.   \tag{4.1}
\]

Exactly the types with IDs

\[
                         1,2,4,5,7,8              \tag{4.2}
\]

have `r=1`, and their frozen counts sum to

\[
                297+8+20+140+237+442=1144.        \tag{4.3}
\]

Equivalently, the marked profiles are exactly the six profiles with
`k_2=0`.  The unmarked profiles have IDs `0,3,6`, all have `k_2=1`, and
their counts sum to

\[
                         139+20+127=286.           \tag{4.4}
\]

For a factor column `Q`, write

\[
                         q_Q(j)=[L_{Q,j}^{(3)}]     \tag{4.5}

for its rank-seven orbit at position `j`.  The unresolved pin problem must
choose, separately for each period:

1. a bijection between the copies in `mathcal S_N` and `mathcal Q_N`; and
2. one directed cyclic phase for every matched pair,

so that the `1,144` positions with `r=1` hit every rank-seven orbit exactly
once.  With assignment variables `y_(S,Q,delta)`, the exact orbit row is

\[
 \sum_{S,Q,\delta} y_{S,Q,\delta}
     \sum_{i\in\mathbb Z_N} r(S_i)
       \mathbf 1[q_Q(i+\delta)=A]=1
 \qquad(A\in{\mathbb Z_{17}\choose7}/\mathbb Z_{17}).          \tag{4.6}
\]

The `y` variables also have the usual one-use rows for every schedule copy
and every selected factor column.  Only directed rotations are automatic;
reversal is not assumed because `(1.1)` is directed.

Under the intended lower-q2 load range `{1,2}`, the 1,430 positions over
1,144 rank-seven orbits have the forced histogram

\[
                         858\times1,\qquad286\times2.            \tag{4.7}
\]

Equations `(4.3)` and `(4.4)` make the pin rule completely sharp:

* every singleton `L^(3)` orbit must occur at a `k_2=0` schedule position;
* the two occurrences of every doubled `L^(3)` orbit must receive one
  `k_2=0` position and one `k_2=1` position.

Indeed `(4.6)` chooses one marked occurrence per orbit, and the `286`
unmarked positions are exactly the extra occurrences of the `286` doubled
orbits.  This `286=286` identity is necessary but still does not construct
the period-compatible cycle/phase matching.

A fixed bijection from the abstract five-core to the literal core of `Q`
can be chosen after a match and preserves all refresh arcs.  It has no
effect on `(4.5)`, though it will matter for the remaining rank-two through
rank-six suffix payloads.

Lower-q2 coverage guarantees that each orbit `A` occurs somewhere among
the factor positions, and `(4.3)` gives the right number of pinned type
positions.  Neither fact implies the cycle/phase assignment `(4.5)`.
Therefore the rank-seven pin remains a separate finite coupling gate and is
not claimed by this theorem.

## 5. H100 certificates

All computation, compilation, replay, and hashing ran through SSH on H100.
The local Mac was used only for reading, editing, transfer, and Git.

The search source is

```text
scratch/search_q4_k17_pure_core_cycle_schedule_20260814.py
SHA-256 1ecda43db50ac7bcd73b23af570614b051b053b7d4f8f80d0b2798f101513574
```

The five exact certificate batches are

```text
scratch/search_q4_k17_pure_core_cycle_schedule_faces0_13_20260814.h100.out
scratch/search_q4_k17_pure_core_cycle_schedule_faces1_3_20260814.h100.out
scratch/search_q4_k17_pure_core_cycle_schedule_faces4_6_20260814.h100.out
scratch/search_q4_k17_pure_core_cycle_schedule_faces7_9_20260814.h100.out
scratch/search_q4_k17_pure_core_cycle_schedule_faces10_12_20260814.h100.out
```

Their SHA-256 values, recorded again by the independent replay, are

```text
fb06c2cb1d8660748fa40ab9d851488671eee8f05063e5881501e33ad844d08d  faces0_13
786c3a29b997df057d6910bcb4799d5f466cb541403f4621920c0094efb1e001  faces1_3
07bdeb13fff103f9a05c72bdd637648861ff910816c6b739b24728036d60481c  faces4_6
9b74fa3b21bc3cb5684bbd186bb0ce471741fe8e499845f8face62e49f9e3cff  faces7_9
04f64f5c03c9374c38b37d2f33b167f80c68cb6b7b117d772da0b560dbae3493  faces10_12
```

Independent replay:

```text
scratch/replay_q4_k17_pure_core_cycle_schedule_20260814.py
SHA-256 110db60c388936bd2fcde22128ff1662a59d093436738995615b6ff327f9d4f5

scratch/replay_q4_k17_pure_core_cycle_schedule_20260814.h100.out
SHA-256 ea1b3e0847f7afa32a6749349d485a2d861f9d99e80754032e63c97245464b7a
```
