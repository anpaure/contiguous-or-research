# Thread D: exact reserve augmentation for the frozen K16 repair portals

**Date:** 2026-07-30  
**Status:** exact finite-column theorem; the collective interacting-edit gate remains open

## 1. Frozen state and four portals

Let (W) be the frozen length-(12873) word
`scratch/k16_12873_repaired_partial.word`, with SHA-256

```text
0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and exact hole set

\[
 H_0=\{10365,52833,52835\}.
\]

Four fixed portals are considered (positions are zero-based).  The two
three-move return portals (P_0,P_1) are the current priority; the older
two-move portals are retained as comparison rows.

1. The central portal
   \[
   (6436:18033\mapsto18017),\qquad
   (6439:10361\mapsto10365)
   \]
   covers (H_0) and leaves the ten-mask debt
   \[
   D_c=\{10361,18033,20081,20215,26745,43129,
          50801,52849,52983,59513\}.
   \]
2. The boundary portal
   \[
   (1:\mathtt{0x2829}\mapsto\mathtt{0x2839}),\qquad
   (12872:\mathtt{0xcc41}\mapsto\mathtt{0xce41})
   \]
   also covers (H_0), and leaves the eight-mask debt
   \[
   D_b=\{10349,11373,43117,44141,
          52321,52323,52327,52455\}.
   \]
3. The boundary-return portal (P_0)
   \[
   (6440:\mathtt{0xa069}\mapsto\mathtt{0x2069}),\quad
   (6441:\mathtt{0x806d}\mapsto\mathtt{0x006d}),\quad
   (12872:\mathtt{0xcc41}\mapsto\mathtt{0xce41})
   \]
   has exact portal-word SHA-256
   `d45df419f4dfbc875a160d5076f7906999bd6eb18cdf9b536da79601849316be`
   and debt
   \[
   D_0=\{43129,43133,52321,52323,52327,52455\}.
   \]
4. The central-return portal (P_1)
   \[
   (6435:\mathtt{0x0600}\mapsto\mathtt{0x8600}),\quad
   (6440:\mathtt{0xa069}\mapsto\mathtt{0x2069}),\quad
   (6441:\mathtt{0x806d}\mapsto\mathtt{0x006d})
   \]
   has exact portal-word SHA-256
   `c0c665adf013bf5d4f84099f909c42ee12d3b8ac20d31aec40d55a7757c032d4`
   and debt
   \[
   D_1=\{20065,20067,20081,20215,43129,43133\}.
   \]

Both debt sets and every multiplicity in this note are obtained by exact
contiguous-interval OR recurrence, not by a bounded-width proxy.

## 2. Strict reserve columns

Fix either portal (P), with debt (D=H(PW)).  A **strict atomic reserve
column** is a nonzero one-cell replacement (e=(p,a)), away from the two
fixed portal positions, such that

\[
 H(eW)=H_0,\qquad H(PeW)\subseteq D,
 \qquad A_e:=D\setminus H(PeW)\ne\varnothing.                 \tag{2.1}
\]

Thus the edit neither fills nor enlarges the original three-hole state before
the portal, creates no foreign post-portal hole, and prepays at least one debt
mask.  This is the literal meaning of an edit that individually preserves the
three-hole incumbent and creates a portal-surviving reserve.

For a family ({\cal E}) of such columns, the isolated-column reserve problem
is the set-cover system

\[
 \min\sum_{e\in{\cal E}}x_e,
 \qquad
 \sum_{e:d\in A_e}x_e\ge1\quad(d\in D),
 \qquad x_e\in\{0,1\}.                                      \tag{2.2}
\]

Its fractional dual is

\[
 \max\sum_{d\in D}y_d,
 \qquad
 \sum_{d\in A_e}y_d\le1\quad(e\in{\cal E}),
 \qquad y_d\ge0.                                            \tag{2.3}
\]

If one insists that different debt masks be assigned to different reserve
edits, the exact condition is ordinary Hall:

\[
 |N(X)|\ge |X|\qquad(X\subseteq D),                          \tag{2.4}
\]

where (N(X)=\{e:A_e\cap X\ne\varnothing\}).  Condition
(2.4) is sufficient but unnecessarily strong for (2.2), because one edit may
cover several debt masks.  The exact uncapacitated formulation is (2.2), not
an ordinary matching theorem.

Finally, even a cover in (2.2) is only an isolated-column candidate: two
selected edits may alter each other's witness intervals.  Every positive pair
must therefore be replayed simultaneously.  The audit does this for every
pair passing the isolated set-cover test.

## 3. Exact reduction of the raw replacement catalogue

The nominal catalogue contains every position (p) and every nonzero value
(a) that is a submask of at least one (d\in D).  There are

\[
 4479\cdot12873=57,658,167
\]

assignments for (D_c), and

\[
 1407\cdot12873=18,112,311
\]

assignments for (D_b).  The following reduction is lossless for strict
columns.

### Lemma 3.1 (unique-owner intersection)

For each cell (p), let ({\cal U}_p) be the set of targets (T) whose
baseline witness is unique and in which (p) supplies a bit not supplied by
the other cells of that witness.  Put

\[
 I_p=\bigcap_{T\in{\cal U}_p}T.
\]

Every strict reserve replacement (a) at (p) satisfies (a\subseteq I_p).

**Proof.**  The unique old witness of (T\in{\cal U}_p) is destroyed if the
essential contribution at (p) is not retained.  Any replacement witness for
(T) must contain (p), since every interval avoiding (p) is unchanged and
none witnessed (T) before.  An interval with OR (T) can contain only cell
values that are submasks of (T); hence (a\subseteq T).  Intersect over
({\cal U}_p).  ∎

The independent reconstruction finds exactly (50,170) unique targets and
(114,290) essential target-cell incidences; every one of the (12,873)
cells has at least one such incidence.  These counts agree with the frozen
exact edit ledger.

### Lemma 3.2 (post-portal side-state condition)

If replacing cell (p) by (a) creates a new witness of (d\in D) after the
portal, then for an exact left-suffix/right-prefix OR state (s) about (p),

\[
 s\vee a=d.                                                  \tag{3.1}
\]

**Proof.**  An interval newly witnessing (d) must contain the changed cell.
Removing that cell splits the interval into a suffix to its left and a prefix
to its right.  Their union is one of the enumerated exact side states (s),
and reinserting (a) gives (3.1).  ∎

Lemmas 3.1 and 3.2 give the following exact reductions.

| portal | debt-submask values | raw assignments | necessary assignments | positions |
|---|---:|---:|---:|---:|
| old central | 4,479 | 57,658,167 | 176 | 9 |
| old boundary | 1,407 | 18,112,311 | 173 | 10 |
| (P_0) | 1,471 | 18,936,183 | 262 | 12 |
| (P_1) | 2,495 | 32,118,135 | 203 | 11 |

Exact multiplicity deltas, in both (W) and (PW), are then used to test
(2.1).

## 4. Census and cuts

### Theorem 4.1 (central strict-column obstruction)

The central portal has **no strict atomic reserve column**.  In particular,

\[
 N(\{d\})=\varnothing\qquad(d\in D_c),                       \tag{4.1}
\]

so every singleton is already an exact set-cover and Hall obstruction.

### Theorem 4.2 (boundary strict-column obstruction)

The boundary portal has exactly one strict atomic reserve column:

\[
 (p,a)=(0,43117),\qquad A_e=\{43117\}.                       \tag{4.2}
\]

The old value at position (0) is (34860).  The other seven debt masks have
empty provider sets.  Thus (2.2) is infeasible, with for example the exact
singleton cut

\[
 N(\{10349\})=\varnothing.                                  \tag{4.3}
\]

There is consequently no two-column cover to replay for either portal.

### Theorem 4.3 (priority return portals have empty strict atlases)

For each of (P_0) and (P_1), **none** of the losslessly reduced candidates
is a strict atomic reserve column.  Thus

\[
 N_{P_i}(\{d\})=\varnothing
 \qquad(i\in\{0,1\},\ d\in D_i).                             \tag{4.4}
\]

In particular, the isolated-column cover number is infinite and there is no
two-column cover to replay.  The exact baseline multiplicities of the (P_0)
debts are all one.  For (P_1), the multiplicity of (20081) is two and the
other five debt multiplicities are one; the obstruction nevertheless remains
complete.

### Corollary 4.4 (minimum one-cell reserve bound)

For either fixed portal, one nonzero one-cell reserve substitution cannot
prepay the complete debt.  Hence the unrestricted one-cell-substitution
reserve number is at least two.  Within the stronger **strict atomic** model
(2.1), the reserve number is infinite: no family of individually safe columns
covers the debt.

The first sentence is unconditional for one-cell substitutions: any edit that
creates a debt witness must satisfy the submask and side-state necessities
used above.  It does not cover deletion-shifts, insertions, reorderings, or
length changes.

There is also an independent exact closure bound in the already-open portal
state.  Any one replacement covering every current debt mask must be a
nonzero submask of their common intersection.  Exhausting the exact
left-suffix/right-prefix states gives

| portal | debt size | common mask | assignments | maximum debts gained |
|---|---:|---:|---:|---:|
| old central | 10 | `0x0071` | 193,095 | 6 |
| old boundary | 8 | `0x0861` | 193,095 | 4 |
| (P_0) | 6 | `0x8861` | 399,063 | 4 |
| (P_1) | 6 | `0x0861` | 193,095 | 3 |

This proves the same radius-two lower bound even if one first applies the
portal and then allows an arbitrary single nonzero substitution, without the
pre-portal preservation requirement.  The table counts gains only, so it
cannot accidentally use the absence of new losses to strengthen the bound.

## 5. Sharp remaining gate

The census does **not** exclude a collectively safe interacting family
(E) in which some edit is unsafe or useless in isolation.  Such a family may
repair a unique target destroyed by another edit, or create a debt witness
whose interval contains several edited cells.  In that case columns do not
add: one must impose the exact conditions

\[
 H(W^E)=H_0,\qquad H(PW^E)=\varnothing                       \tag{5.1}
\]

on the simultaneous word.  This is the precise next exchange-hypergraph
gate.  The present theorem says that any positive solution must use this
genuinely interacting mechanism; there is no decomposition into individually
safe reserve payments.

## 6. Reproduction

Run

```bash
python3 scratch/audit_threadD_k16_portal_reserve_augmentation_20260730.py
```

The executable audit is
`scratch/audit_threadD_k16_portal_reserve_augmentation_20260730.py`; its JSON
certificate is
`scratch/threadD_k16_portal_reserve_augmentation_20260730.audit.json`.

The final four-portal remote run used one CPU, 19.20 seconds wall time, and
83,968 KiB maximum resident memory.
