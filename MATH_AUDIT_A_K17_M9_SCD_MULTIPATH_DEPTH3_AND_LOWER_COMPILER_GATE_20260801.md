# The authenticated `m=9` SCD forest needs exactly 1,419 interior residence cuts before any depth-three compiler

Date: 2026-08-01  
Lane: A, `K17` SCD multipath lower compiler  
Status: exact authenticated finite obstruction, exact optimal cut ledger,
and exact post-cut common-`Q` formulation.  No `K17` word or physical
post-cut braid is claimed.

## 0. Verdict

The authenticated flexible-SCD object is a genuine upper/lower-exact
linear forest on

\[
 W={17\choose9}=24310
\]

middle owners, with

\[
 U={17\choose10}=19448
\]

edges and

\[
 C=W-U=4862
\]

path components.  It cannot, however, be used as `4,862` untouched
depth-three source blocks.

Exactly `1,213` of the components fail the component maximal-source
equations.  The failure is intrinsic to their interiors: there are

\[
 1076\text{ internal positive runs of length }2,
 \qquad
 660\text{ internal positive runs of length }3.       \tag{0.1}
\]

No ordering, reversal, exterior cap, or endpoint connector can repair an
internal run while retaining that component verbatim.  The exact minimum
number of additional internal cuts which makes every resulting piece
depth-three factorable is

\[
                         \boxed{1419}.                \tag{0.2}
\]

Thus the smallest retained-interior face has

\[
 P=C+1419=6281                                      \tag{0.3}
\]

pieces, not `4,862`.  It preserves

\[
 W-P=18029                                         \tag{0.4}
\]

internal rank-eight lower colours and has a raw rank-eight omission bank
of size `P`, including the one linear boundary colour.  Against the
advertised scalar defect allowance `7401`, this leaves only

\[
                         7401-P=1120                 \tag{0.5}
\]

units before any further seam/common-cap casualty is charged.

There is a positive but sharply limited result.  In the **disjoint full
piece-block relaxation**, after reserving all `18,029` internal `q1`
cells, the `6,281` omitted rank-eight targets have a perfect matching to
locally admissible cells.  There are no zero-host lower targets at any
rank `1,...,8`.  This is not a physical compiler: the separated blocks
contain `110,616` lower cells, whereas a length-`24313` word has only
`72,936`.  The exact surviving gate is therefore a joint piece
ordering/orientation, global maximal-source quotient, occurrence matching,
and one common maximal word.

The abstract connector upper multiset from
`MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md` is a
separate rank-ten row.  Its existence neither repairs (0.1) nor realizes
the physical lower common-`Q` quotient.

## 1. Authenticated input

The selected flexible-detachment assignment is

```text
scratch/ad_k17_scd_multicomponent_20260801/phase_m9.selected.tsv
SHA-256 49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de
```

The independently checked model and option-map hashes are

```text
model       75946e58bea2147d3899eae3f0f99aca9ba4ea413682c938ca59534b980a687c
option map  381dc1068aa39403d442c3d3b2d45a1c334dbc1e2b206449d5f678a6c1b6d473
```

The authenticated replay reports

```text
selected=8008 edges=19448 palettes=19448/19448
max rooted in/out/physical=1/1/2 components=4862 cycles=0
```

The independent component table used below is

```text
scratch/threadA_k17_m9_scd_lower_compiler_20260801/components.tsv
SHA-256 dc4557fb557dccb87bec15476e11b81655d17c6c6c5295b020fec95adbcb47ef
```

It contains all `24,310` owners, grouped into the `4,862` directed paths.

## 2. Exact component source criterion

Let

\[
                         O_0,O_1,\ldots,O_{n-1}       \tag{2.1}
\]

be one directed component.  At depth three define its maximal source by

\[
 K_p=\bigcap_{\max(0,p-3)\le i\le\min(n-1,p)}O_i,
 \qquad 0\le p\le n+2.                              \tag{2.2}
\]

### Theorem 2.1 (component factorability)

There is a nonempty source block `A_0,...,A_(n+2)` satisfying

\[
                  A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}=O_i
                  \qquad(0\le i<n)                  \tag{2.3}
\]

if and only if

\[
 K_p\ne\varnothing\quad(0\le p\le n+2),
 \qquad
 O_i=K_i\cup K_{i+1}\cup K_{i+2}\cup K_{i+3}.       \tag{2.4}
\]

When it exists, `K` is the unique componentwise-largest source.

#### Proof

Every source position belongs to each owner window using it, so every
feasible `A_p` is contained in `K_p`.  Hence an empty `K_p` or a coordinate
missed by the right side of (2.4) is impossible.  Conversely `A=K`
directly gives (2.3) when (2.4) holds.  \(\square\)

### Lemma 2.2 (internal short-run obstruction)

If a coordinate has an internal positive owner run `[a,b)` of length at
most three, then it occurs in no maximal-source position belonging to that
run.  Consequently every owner in that run fails reconstruction in (2.4).

#### Proof

For the coordinate to belong to `K_p`, the full owner-index interval
`[p-3,p]` occurring in (2.2) must lie inside `[a,b)`.  This requires

\[
                         a+3\le p\le b-1,            \tag{2.5}
\]

which is impossible when `b-a<=3`.  Since the run is internal, neither
global clipping convention can restore it.  \(\square\)

This proves that such a defect survives every permutation or reversal of
the other components.  It can be removed only by an interior cut or an
interior rethread which changes the retained component.

## 3. Exact finite component audit

The independent replay of (2.2)--(2.4) gives:

| quantity | exact value |
|:--|--:|
| components | `4,862` |
| components failing (2.4) | `1,213` |
| empty `K_p` positions | `0` |
| owner rows failing reconstruction | `3,863` |
| internal length-two runs | `1,076` |
| internal length-three runs | `660` |

The sum `2(1076)+3(660)=4132` counts failed coordinate incidences;
overlap among them explains why only `3,863` owner rows fail.

Thus the requested untouched `4,862`-block compiler face is exactly
infeasible before target Hall, common cap, or upper-shadow matching is
considered.

## 4. The minimum interior residence cut is 1,419

Represent a bad run `[a,b)` by the closed interval `[a,b]` of
inter-owner cut positions.  Cutting at any `c in [a,b]` makes that positive
run touch a new piece endpoint (or splits it into two clipped runs).

### Theorem 4.1 (interval-stabbing normal form)

For a fixed component, a cut set eliminates every internal positive run
of length at most three if and only if it stabs every associated interval
`[a,b]`.  The minimum number of cuts is obtained by sorting the intervals
by their right endpoints and repeatedly choosing the first uncovered
right endpoint.

#### Proof

The first statement is the definition of clipping at a new component
boundary.  For the second, let `[a,b]` be the first interval in
right-endpoint order.  Every stabbing set has a point `c in [a,b]`.
Replacing `c` by `b` cannot uncover any later interval that `c` hit: every
later interval has right endpoint at least `b`, and if its left endpoint
is at most `c`, then, because it also met `c<=b`, its left endpoint is at
most `b`.  Induction proves greedy optimality.  \(\square\)

Applied independently to all authenticated components, the cut counts are

| cuts in one old component | number of components |
|--:|--:|
|0|3,649|
|1|1,037|
|2|149|
|3|24|
|4|3|

Their weighted sum is `1,419`.  Direct reconstruction verifies that all
`6,281` resulting pieces have nonempty maximal sources, reconstruct every
owner, and have no internal positive run shorter than four.

The rank-eight ledger follows without another search.  Every retained
piece edge has its old distinct lower intersection colour.  A forest on
`W` owners split into `P` pieces has `W-P` retained edges, so it supplies
exactly `18,029` distinct rank-eight colours and omits exactly `P=6,281`.

## 5. Exact fixed-chronology generalized compiler

The following is the correct model after a physical ordering, orientation,
and depth-three schedule have been fixed.  It must not be replaced by a
rankwise Hall matching.

Let `J` be the physical source positions and let `E_p` be the intersection
of every prescribed middle-owner row using position `p`, together with all
fixed cap/guard rows.  Let `C` be the physical intervals of lengths at most
three.  Some cells are already fixed to the retained internal rank-eight
colours.  Let `R` be the remaining lower targets: every rank `1,...,7`
target plus the `P` omitted rank-eight targets.

Choose binary occurrence variables

\[
 z_{S,I}\in\{0,1\}\qquad(S\in R,\ I\in C)           \tag{5.1}
\]

with

\[
 \sum_I z_{S,I}=1\quad(S\in R),
 \qquad
 \sum_S z_{S,I}\le1\quad(I\in C).                  \tag{5.2}
\]

For one choice `z`, put

\[
 K_p(z)=E_p\cap
       \bigcap_{(S,I):\ z_{S,I}=1,\ p\in I}S.        \tag{5.3}
\]

### Theorem 5.1 (exact matching/common-`Q` criterion)

The fixed physical atlas admits one nonempty source word realizing every
middle row, every fixed internal lower cell, and every target in `R` if and
only if there is a `z` satisfying (5.2) such that

1. `K_p(z)` is nonempty and contains every mandatory bit at `p`;
2. the unions of `K_p(z)` reconstruct every prescribed middle/fixed row;
3. for every selected occurrence,

   \[
                    \bigcup_{p\in I}K_p(z)=S.        \tag{5.4}
   \]

#### Proof

Any feasible source letter at `p` is contained in every row using `p`,
hence in (5.3).  Thus the three displayed conditions are necessary.  If a
feasible word exists for the same selected occurrences, enlarging it
positionwise to `K(z)` cannot create an outside bit in any selected or
fixed row, while it can only restore missing positive bits.  Therefore its
maximal enlargement satisfies the same exact rows.  Conversely the word
`K(z)` is a literal source when conditions 1--3 hold.  \(\square\)

The ordinary Hall inequalities for (5.2) are necessary but not sufficient:
the selected occurrences also intersect in the same position caps (5.3).
This is precisely the common-`Q` coupling.

## 6. What the separated-piece relaxation proves—and does not prove

For one factorable piece with maximal source `K`, define the run-boundary
mandatory core

\[
 F_p=(K_p\setminus K_{p-1})\cup(K_p\setminus K_{p+1}),             \tag{6.1}
\]

omitting nonexistent endpoint terms.  For an interval `I` of length at
most three put

\[
                         F(I)=\bigcup_{p\in I}F_p,
 \qquad                  K(I)=\bigcup_{p\in I}K_p.    \tag{6.2}
\]

A necessary independent-occurrence condition is

\[
                         F(I)\subseteq S\subseteq K(I).            \tag{6.3}
\]

The finite audit forms the disjoint union of all `6,281` full piece
sources, reserves the unique length-three internal `q1` cell for every
retained edge, and tests (6.3) on all other cells.

It finds:

* zero zero-host targets in every rank `1,...,8`;
* minimum host counts by rank

  \[
  8514,4428,2124,906,335,96,19,1;                   \tag{6.4}
  \]

* after restricting to the `6,281` omitted rank-eight targets and removing
  all `18,029` fixed internal `q1` cells: zero zero-host targets, minimum
  degree `2`, and maximum matching `6,281/6,281`.

This closes the easiest residual rank-eight Hall cut positively.  It is
still only a relaxation.  The separated source length is

\[
 \sum_j(n_j+3)=W+3P=43153,                           \tag{6.5}
\]

whereas an optimal `K17` word has length `W+3=24313`.  Hence a physical
integration must remove or identify

\[
                         3(P-1)=18840               \tag{6.6}
\]

source positions.  Likewise the separated lower-cell atlas has

\[
 \sum_j(3(n_j+3)-3)=3W+6P=110616                   \tag{6.7}
\]

cells, versus

\[
                         3(W+3)-3=72936              \tag{6.8}
\]

physical cells.  Its excess is `37,680=6(P-1)`.  Thus the matching in this
section cannot be read as a physical Hall certificate.

## 7. Sharp remaining finite gate

Orient and order the `P=6,281` pieces, concatenate their owner lists into

\[
                         T_0,\ldots,T_{W-1},          \tag{7.1}
\]

and form the **global**, not piecewise, maximal envelope

\[
 E_p=\bigcap_{\max(0,p-3)\le i\le\min(W-1,p)}T_i.
                                                               \tag{7.2}
\]

The exact next problem is to choose the order/orientations and the rank-ten
connector realization so that:

1. every `E_p` is nonempty and

   \[
                    T_i=E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3};          \tag{7.3}
   \]

2. all required arbitrary-width upper witnesses survive or are supplied by
   the connector palette;
3. the occurrence matching (5.2) is feasible on the resulting **physical**
   `72,936`-cell atlas; and
4. the same selection passes the maximal common-`Q` equalities (5.3)--(5.4).

Conditions (7.2)--(7.3) are a finite run-summary/order problem.  They are
not implied by the fact that every individual piece is factorable.  Short
pieces may transmit a coordinate state across more than one seam, so a
pairwise seam graph alone is not an exact model; the last three owners (or
the equivalent depth-three run summary) must be part of the state.

The connector-cocycle compression prescribes the correct abstract rank-ten
repeat multiset.  Physical endpoint realization and the four conditions
above remain coupled.  This is the smallest surviving face after the exact
`1,419`-cut obstruction.

## 8. Audit artifacts

```text
scratch/audit_threadA_k17_m9_scd_multipath_compiler_20260801.py
  SHA-256 fa7a2e76ab0fa5fc8d9c7c0af23daaac1d3cf3dbd4d96c39f0d4978833e61bab

scratch/threadA_k17_m9_scd_lower_compiler_20260801/support_v2.audit.json
  SHA-256 83ba59c77897d81ff760d53d79fcc8888d2c5c60c30a9fdcff5548ea143cedd3

scratch/threadA_k17_m9_scd_lower_compiler_20260801/support_v2.stderr
  SHA-256 b245499e6f55a98a65175f9362947815708ba07fd20add083986e2221fa84000
```

The support audit ran on one H100 CPU core under a `1 GiB` address-space
cap and `600 s` wall timeout.  It completed in `3.46 s` with peak RSS
`27,136 KiB`.  No SAT solver was used.

