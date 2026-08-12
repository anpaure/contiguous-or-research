# Exact common-tail suspension of the fourteen-row Tamari base factor

**Date:** 2026-08-06  
**Method:** pure mathematics; no finite search, solver, or computation  
**Status:** unconditional protected partial-factor theorem.  It does not
assert completion of the suspended fourteen-row bank to a full factor in the
larger dimension.

## 0. Verdict

The port-restored Tamari packet is contained in an exact noncanonical
fourteen-row factor at semilength four.  Tensoring **all fourteen rows** with
one common complement-geodesic tail gives, in every larger semilength, a
literal fourteen-row partial shortest-wreath factor.  The four-row Tamari
replacement remains a sealed support trade inside that bank: the ten common
rows are untouched and no state or adjacent-union colour leaks into them.

The old common-context metric no-go does not apply.  In the tensor order the
common deletion tail lies between the row-dependent deleted and inserted
base blocks.  For fixed linear representatives it contributes exactly

\[
                    s\,|P_0\mathbin{\triangle} Q_0|     \tag{0.1}
\]

new inversions between two base rows, where `s` is the tail semilength.
Thus the common tail itself supplies linear cyclic-order dispersion.

What does **not** follow is a full exact factor in the larger dimension.
The naive sealed product-box completion is arithmetically impossible for
generic `s`: a `5 x (s+1)` state box has `5(s+1)` vertices, while every
shortest complement path has `s+5` vertices.  A boxwise partition would
require

\[
                            s+5\mid20.                  \tag{0.2}
\]

Hence an all-dimensional completion must mix product boxes or rank sectors.

## 1. Base factors and the tail tensor

Let `J` be an eight-element base ground.  A base complement geodesic is

\[
                         P=(P_0,P_1,P_2,P_3,P_4),       \tag{1.1}
\]

where every `P_i` is a four-subset of `J`, consecutive states are Johnson
adjacent, and

\[
                              P_4=J-P_0.                \tag{1.2}
\]

Let `F^-` and `F^*` be the two exact fourteen-path factors from
`MATH_THEOREM_PORT_RESTORED_TAMARI_BASE_EXACT_FACTOR_COMPLETION_20260806.md`.
They share ten paths, and their remaining four paths are respectively the
negative and port-restored Tamari packets.  On each shore:

* the seventy base states `P_i` occur exactly once;
* the fifty-six adjacent unions `P_i union P_(i+1)` occur exactly once.

Let `E` be disjoint from `J`, with `|E|=2s`, and choose any complement
geodesic

\[
                         S=(S_0,S_1,\ldots,S_s)          \tag{1.3}
\]

in the rank-`s` layer of `E`.  Put

\[
                              r=s+4.                    \tag{1.4}
\]

Define the common-tail tensor of `P` by

\[
 \widehat P=
 (P_0+S_0,P_1+S_0,\ldots,P_4+S_0,
  P_4+S_1,\ldots,P_4+S_s).                            \tag{1.5}
\]

There are `r+1=s+5` states in (1.5).

### Lemma 1.1 (literal complement geodesic)

Every `widehat P` in (1.5) is a shortest rank-`r` Johnson path from
`P_0+S_0` to its complement in `J union E`.

#### Proof

The first four steps exchange the four base coordinates and leave `S_0`
fixed.  The final `s` steps exchange the tail coordinates and leave `P_4`
fixed.  Thus all `r` steps are Johnson edges.  The endpoints satisfy

\[
 (J\cup E)-(P_0+S_0)
   =(J-P_0)+(E-S_0)=P_4+S_s.                           \tag{1.6}
\]

Their Johnson distance is `r`, so the path is shortest.  \(\square\)

## 2. Exact partial-factor suspension

### Theorem 2.1 (fourteen-row partial factor)

For either base factor `F in {F^-,F^*}`, the family

\[
                         \widehat F_S
                         =\{\widehat P:P\in F\}        \tag{2.1}
\]

consists of fourteen pairwise state-disjoint shortest complement paths.
Their adjacent-union colours are also pairwise distinct.

Equivalently, after adjoining one omitted coordinate, `widehat F_S` is a
literal fourteen-wreath partial factor, exact on both of its central shores.

#### Proof

Split the states in (1.5) into the base part

\[
                         P_i+S_0\quad(0\le i\le4)       \tag{2.2}
\]

and the proper tail part

\[
                         P_4+S_j\quad(1\le j\le s).     \tag{2.3}
\]

All states in (2.2) are distinct because `F` partitions the seventy base
four-sets.  All states in (2.3) are distinct because the endpoints `P_4`
are distinct across the fourteen base paths and `S` is simple.  Equality
between (2.2) and (2.3) would force `S_0=S_j` on the disjoint tail ground,
which is impossible for `j>0`.  This proves state disjointness.

The adjacent unions likewise split into

\[
        (P_i\cup P_{i+1})+S_0\quad(0\le i<4)           \tag{2.4}
\]

and

\[
        P_4+(S_{j-1}\cup S_j)\quad(1\le j\le s).       \tag{2.5}
\]

The colours in (2.4) are distinct because `F` partitions the fifty-six
base rank-five colours.  The colours in (2.5) are distinct because the
`P_4` are distinct and the adjacent unions of a shortest complement
geodesic are distinct.  A colour in (2.4) has base/tail ranks `(5,s)`,
whereas a colour in (2.5) has ranks `(4,s+1)`.  Thus the two families cannot
meet.  \(\square\)

### Corollary 2.2 (the lifted Tamari trade is sealed)

The two partial factors `widehat F^-_S` and `widehat F^*_S` have ten common
rows.  Replacing the four negative tensor rows by the four port-restored
tensor rows preserves exactly the aggregate state support and the aggregate
adjacent-union support.  No state or colour of a common row changes.

#### Proof

The base Tamari packet has identical aggregate state and adjacent-union
ledgers on its two shores and fixes every terminal state `P_4` row by row.
Tensoring its base segments by `S_0` preserves the two ledger equalities.
The junction and proper tail segments depend only on the fixed `P_4` and on
`S`, so they agree literally row by row.  Theorem 2.1 makes both packets
disjoint from the ten common tensor rows.  \(\square\)

## 3. Exact correction to the common-context distance claim

Write the exchange word of `P` as deletion order

\[
                         D_P=(d_1,d_2,d_3,d_4)          \tag{3.1}
\]

and insertion order

\[
                         I_P=(i_1,i_2,i_3,i_4).         \tag{3.2}
\]

Similarly write the tail orders as `D_S` and `I_S`, each of length `s`.
The cyclic coordinate order reconstructed from (1.5), with its omitted
coordinate displayed last, is

\[
                         (D_P,D_S,I_P,I_S,\infty).      \tag{3.3}

### Theorem 3.1 (linear cut-crossing dispersion)

For two base paths `P,Q`, compare the fixed linear representatives (3.3).
Then

\[
 \boxed{
 d_{\rm inv}(\widehat P,\widehat Q)
 =d_{\rm inv}((D_P,I_P,\infty),(D_Q,I_Q,\infty))
  +s\,|P_0\mathbin{\triangle} Q_0|.}                 \tag{3.4}
\]

#### Proof

Old-old inversions are exactly those of the two displayed base orders.
The internal orders of `D_S,I_S` agree in both rows, as do their mutual
order and their order relative to `infty`.  Every label of `I_S` follows
all base labels in both rows and contributes nothing new.

A label of `D_S` follows precisely the four labels of `P_0` in the first
row and precisely the four labels of `Q_0` in the second.  Its relative
order flips with exactly the labels in `P_0 triangle Q_0`.  There are `s`
labels in `D_S`, proving (3.4).  \(\square\)

Thus a common context is not generally distance-neutral.  It is neutral
only when the two insertion cuts have the same old labels on one side.
The former `e_s=0` specialization in
`CATALAN_SEAM_ABSORPTION_OBSTRUCTION.md` is therefore inapplicable to this
tensor.  The conditional metric lower bound in that note remains valid.

## 4. Why the obvious product completion does not follow

Fix one base path `P` and one tail path `S`.  Their central product box is

\[
             \mathcal B(P,S)=
             \{P_i+S_j:0\le i\le4,\ 0\le j\le s\},   \tag{4.1}
\]

with

\[
                         |\mathcal B(P,S)|=5(s+1).      \tag{4.2}

### Proposition 4.1 (sealed-box divisibility obstruction)

If `mathcal B(P,S)` were partitioned into shortest rank-`r` complement
paths without using states outside this box, then

\[
                              s+5\mid20.                \tag{4.3}

In particular no such sealed-box factorization exists for `s>15`.

#### Proof

Every shortest rank-`r=s+4` complement path has `r+1=s+5` states.  A
partition of (4.2) therefore requires

\[
                              s+5\mid5(s+1).            \tag{4.4}

But

\[
                         5(s+1)=5(s+5)-20,              \tag{4.5}

so (4.4) is equivalent to (4.3).  \(\square\)

This is a no-go only for independent completion of every fixed product
box.  It does not obstruct a global noncanonical completion whose paths
move between boxes or between base-rank sectors.

## 5. Remaining host theorem

The base-host existence and the protected partial suspension are now exact.
The remaining statement is:

> **Cross-box Tamari completion.**  Extend the fourteen-row partial factor
> `widehat F^-_S` (equivalently `widehat F^*_S`) to a full exact
> shortest-wreath factor on `2r+1` coordinates while keeping the four-row
> sealed trade and its protected tail rails.

A proof cannot be a Cartesian product of independent base/tail path boxes
for all sufficiently large `r`, by Proposition 4.1.  It must use an SCD or
matching construction with genuine cross-box flow.
