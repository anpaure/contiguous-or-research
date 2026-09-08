# Exact CNF design for the `k=11` single-switch portal branches

## 1. Status and recommendation

This note designs exact **branches** of the length-465 problem.  None of the
branches below is WLOG for an unrestricted optimum.  Consequently:

* a SAT model, followed by an independent interval-OR check, proves
  `nu(11)=465`;
* an UNSAT certificate refutes only the selected branch; it does **not** prove
  `nu(11)>465` and does not refute `nu(k)=B(k)`.

The recommended branch is no longer the fully saturated `369+93` schedule.
A concrete, factorable `q=19` prefix is now known.  It realizes all twelve
missing rank-seven colours, six additional rank-seven bridge colours, and the
rank-eight seam `958`.  The best search order is therefore:

1. the concrete `q=19` factor-prefix branch;
2. the same `q=19` rank-six row with the factor left free;
3. the abstract `q=19` portal branch;
4. only then the much more restrictive saturated `q=369` branch.

The `q=13` branch is arithmetically smaller, but no compatible 13-vertex
factorable portal path is known.  The new `q=19` certificate is much stronger
evidence than the difference of six fixed-window cells.

## 2. Audited exact kernel to reuse

Use the exact `k11_forest_sat.cpp` formulation with only the following
structural modules enabled:

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
```

The audited inventory of this kernel is

```text
2,882,282 variables
14,352,124 clauses
298 direct targets
```

It is satisfiable exactly when a length-465 nonzero universal array exists.
It contains actual entry bits

\[
 a_{p,b}\quad(0\le p<465,\ 0\le b<11),
\]

and exact simultaneous witnesses for every target.  Thus factorability and
coordinate pin survival are inherent: there is no later factor-labeling
problem and no possibility that independently selected labels disagree.

The two central layers use the state list

```text
00 01 02 03 11 12 13 22 23 33
```

where state `alpha beta` at ordered witness index `i` denotes the physical
interval `[i+alpha,i+beta]`.  Write `z5[i,u]` and `z6[i,u]` for the existing
rank-five and rank-six state variables.  The existing permutation flags
`q5[i,S]` and `q6[i,S]` assign all 462 masks of the indicated rank to the 462
selected physical intervals.

For actual runs, the exact containment caps should also be enabled:

```text
K11_FOREST_CONTAINMENT_CAPS=1
```

They add no variables and 107,368 clauses.  The resulting common search
kernel has

```text
2,882,282 variables
14,459,492 clauses.
```

The caps are a propagation strengthening, not part of branch correctness.
The inventories below are reported both before and after adding them.

Do **not** enable coordinate-canonical rank-six-entry cuts, the old rank-six
branch cuts, minimum-component portfolios, or any seed-distance restriction.
The concrete prefix fixes decimal masks and therefore breaks the coordinate
symmetry used by those optional canonical cuts.  In particular its first
entry is the literal rank-six mask `489`, not the canonical mask `63`.

## 3. A zero-variable exact endpoint macro

The direct and rank-seven-shadow targets already have unary endpoint variables
`L_T(p),R_T(p)` with the exact meanings

\[
 L_T(p)\iff p\ge l_T,\qquad R_T(p)\iff p\le r_T.
\]

To require a target's selected witness to be a length-four window beginning
somewhere in `0,...,h`, add `L_T(h)` and, for every `0<=i<=h`, the two clauses

\[
\begin{aligned}
 \operatorname{Left}_T(i)&\Longrightarrow R_T(i+3),\\
 \operatorname{Left}_T(i)&\Longrightarrow \neg R_T(i+4),
\end{aligned}
\]

where

\[
 \operatorname{Left}_T(0)=L_T(0),\qquad
 \operatorname{Left}_T(i)=L_T(i)\land\neg L_T(i-1)\quad(i>0).
\]

For `i>0`, for example, the first implication is the clause

\[
 \neg L_T(i)\vee L_T(i-1)\vee R_T(i+3).
\]

This macro uses no new variable and exactly `2(h+1)+1` clauses.  For a
rank-seven target represented through `RankSevenShadow`, also set its
existing `active` flag true.  The base crossed-witness clauses then prove the
OR is exactly that target.

To fix one witness to `[l,r]`, add the four endpoint units

\[
 L_T(l),\quad\neg L_T(l-1),\quad R_T(r),\quad\neg R_T(r+1),
\]

omitting an out-of-range neighbor.  This is the cheapest way to put the
direct rank-eight target `958` at a prescribed seam.

## 4. The saturated `q=369` branch

### 4.1 Rank-six schedule

The requested single-switch rank-six witnesses are

\[
 R_3(1),\ldots,R_3(369),
 \quad R_4(370),\ldots,R_4(462).
\]

In zero-based ordered-witness notation, add the 462 units

\[
 z6[i,02]\quad(0\le i\le368),\qquad
 z6[i,03]\quad(369\le i\le461).                 \tag{4.1}
\]

### 4.2 Exact one-defect dichotomy

The short-band one-defect theorem has two alternatives.  They have especially
small state descriptions.

* **Triple defect.**  The rank-five schedule is

  \[
    01^{369}\,(02)^*\,(13)^*,                    \tag{4.2}
  \]

  where the second and third blocks together have length 93.  The first `13`
  identifies the omitted late triple; no `13` means that the last late triple
  is omitted.  The defect may be at `R_3(370)` if the `02` block is empty.

* **Pair defect.**  The schedule is

  \[
    (01)^*\,(12)^*\,13^{94},                     \tag{4.3}
  \]

  where the first two blocks together have length 368.  Their switch locates
  the omitted early pair.

The base monotonicity clauses already force each displayed two-state word to
have at most one switch.  A single branch bit `t` gives the complete
dichotomy with 924 guarded clauses:

```text
i =   0..367:  t -> z5[i,01];       !t -> (z5[i,01] or z5[i,12])
i =       368: t -> z5[i,01];       !t -> z5[i,13]
i = 369..461:  t -> (z5[i,02] or z5[i,13]);
                                      !t -> z5[i,13]
```

The preferred seam-`958` route specializes to the triple-defect branch and
keeps the defect away from `R_3(370)`.  It can be encoded without `t` using
only 462 clauses:

```text
z5[i,01]                       for i = 0..368
z5[369,02]
z5[i,02] or z5[i,13]          for i = 370..461
```

### 4.3 Why these clauses really imply short-band saturation

This does not require a separate quadratic all-different encoding.  The
physical short band has

\[
 465+464+463=1392
\]

cells.  Equations (4.1)--(4.3) select 369 distinct rank-six cells and 462
distinct rank-five cells.  The exact base formula represents all 561 masks of
ranks one through four by intervals of length at most three.  Different masks
cannot use the same physical interval, and intervals of different OR-ranks
cannot coincide.  Since

\[
 369+462+561=1392,
\]

every short cell is used exactly once.  Its OR-values are therefore precisely
all masks of ranks one through five plus 369 distinct rank-six masks.  This
proves both all-distinctness and exhaustion; no additional selector matrix is
needed.

### 4.4 Portal constraints

For each of the twelve named rank-seven masks

```text
251 493 607 941 956 1267 1468 1694 1763 1884 1946 1990
```

set its existing rank-seven `active` flag and apply the endpoint macro of
Section 3 with `h=367`.  This requires it to occur as one of the internal
portals `R_4(1),...,R_4(368)`.  Fix the direct target `958` to the seam
`[368,371]`, i.e. `R_4(369)`, with four endpoint units.

All other targets remain in the exact base formula.  In particular this does
not assume that any witness from the old thirteen-hole factor survives.

The preferred triple-defect branch adds no variables and 9,784 clauses:

```text
rank-six schedule                 462
rank-five triple-defect schedule  462
12 portal endpoint restrictions 8,856
958 seam endpoint units             4
                                  -----
                                  9,784
```

Its inventories are therefore

```text
raw:               2,882,282 variables / 14,361,908 clauses
with exact caps:   2,882,282 variables / 14,469,276 clauses
```

Keeping both one-defect alternatives uses one new variable and 10,246 branch
clauses, giving `2,882,283 / 14,362,370` before caps.  This broader saturated
branch is still not the unrestricted problem.

## 5. The weaker `q=13` partial-switch branch

The monotone schedule

\[
 R_3(1),\ldots,R_3(13),
 \quad R_4(14),\ldots,R_4(462)                  \tag{5.1}
\]

is encoded by

\[
 z6[i,02]\ (0\le i\le12),\qquad
 z6[i,03]\ (13\le i\le461),                   \tag{5.2}
\]

again 462 units.  It makes no assertion about global short-band saturation
or the rank-five schedule.

The clean preferred subbranch puts the twelve named rank-seven values in
the internal portals `R_4(1),...,R_4(12)` and fixes `958` at the seam
`R_4(13)`.  Apply the rank-seven endpoint macro with `h=11` and fix `958` to
`[12,15]`.  The complete delta is only 778 clauses and no variables:

```text
rank-six schedule               462
12 internal portal restrictions 312
958 seam endpoint units           4
                                ---
                                778
```

Hence this branch has

```text
raw:               2,882,282 variables / 14,352,902 clauses
with exact caps:   2,882,282 variables / 14,460,270 clauses.
```

If all thirteen targets may be permuted over all thirteen portal cells, use
169 flags `y[i,T]`.  For each target require at least one flag.  A flag implies
exact equality of its four-entry OR with the target: one positive occurrence
clause for each target bit and four negative entry clauses for each absent
bit.  Exact equality itself prevents two distinct targets from using one
cell; with thirteen targets and thirteen cells every cell is automatically
used.  This broader version adds 169 variables and 4,323 clauses, for
`2,882,451 / 14,356,447` before caps.

The `q=13` branch is far weaker and more plausible than saturation, but its
allocated CNF is not dramatically smaller: the exact all-target kernel still
dominates the inventory.  More importantly, the twelve independently listed
Johnson edges were never shown to concatenate into one factorable 13-vertex
path.  The next section removes that local uncertainty.

## 6. The verified `q=19` portal prefix

### 6.1 Exact local certificate

The following nineteen distinct rank-six triples form a factorable path:

```text
P =
489 429 940 828 860 1876 1862 1734 1731 1251
243 123 95 543 670 1690 1434 1436 444
```

Their eighteen consecutive unions are

```text
U =
493 941 956 892 1884 1878 1990 1735 1763
1267 251 127 607 671 1694 1946 1438 1468
```

Every `P_i` has rank six, every `U_i` has rank seven, all values in each row
are distinct, and `P_i OR P_(i+1)=U_i`.  The row `U` contains all twelve named
rank-seven omissions and the six additional bridge colours

```text
892 1878 1735 127 671 1438.
```

An explicit sparse factor, extended through the rank-eight seam, is

```text
A[1..22] =
489 425 424 300 780 788 836 1604 1602 1218 195
99 83 27 30 538 154 1176 408 4 32 514.
```

Direct recomputation gives

```text
R3(i) = P_i                      for i = 1..19
R4(i) = U_i                      for i = 1..18
R4(19) = 958
A20 OR A21 OR A22 = 550          (rank 4).
```

The last rank-four overlap leaves room for an unknown `A23` to make the first
lower-facing central witness `R4(20)` a rank-six mask.  This is local
feasibility, not proof that the prefix extends to 465 entries.

### 6.2 Abstract `q=19` branch

Use the central schedule

\[
 R_3(1),\ldots,R_3(19),
 \quad R_4(20),\ldots,R_4(462),                 \tag{6.1}
\]

encoded by the 462 units

\[
 z6[i,02]\ (0\le i\le18),\qquad
 z6[i,03]\ (19\le i\le461).                   \tag{6.2}
\]

Require the twelve named rank-seven targets to have length-four witnesses
starting in `0,...,17`, and fix `958` to `[18,21]`.  This adds 922 clauses and
no variables:

```text
rank-six schedule               462
12 portal endpoint restrictions 456
958 seam endpoint units           4
                                ---
                                922
```

The inventories are

```text
raw:               2,882,282 variables / 14,353,046 clauses
with exact caps:   2,882,282 variables / 14,460,414 clauses.
```

### 6.3 Fixed rank-six-row branch (recommended first)

In addition to (6.2), set the nineteen existing permutation literals

\[
 q6[i,P_{i+1}]\qquad(0\le i<19).                \tag{6.3}
\]

The eighteen named and bridge portals are then logical consequences of
`P_i union P_(i+1)=U_i`; no rank-seven endpoint restriction is needed.  Fix
the direct target `958` to `[18,21]` with four units.  This branch adds only

```text
462 schedule units + 19 row units + 4 seam units = 485 clauses.
```

It has

```text
raw:               2,882,282 variables / 14,352,609 clauses
with exact caps:   2,882,282 variables / 14,459,977 clauses.
```

This is the best first exact run: it preserves factor freedom while anchoring
the difficult portal path to a verified, globally coherent local object.

### 6.4 Fixed factor-prefix branch (strongest phase branch)

Instead of (6.3), fix the first 22 entries to the displayed `A` word with
`22*11=242` signed unit clauses.  Together with the 462 schedule units, all
nineteen rank-six triples, all eighteen rank-seven portals, and the `958`
seam follow automatically.  The branch delta is 704 clauses, giving

```text
raw:               2,882,282 variables / 14,352,828 clauses
with exact caps:   2,882,282 variables / 14,460,196 clauses.
```

Although narrower than Section 6.3, this is the best branch for rapidly
testing whether the certified local factor can be continued at all.

## 7. All remaining targets are still encoded

No branch above may reuse the claim that the old fixed-delay factor covered
all but thirteen masks.  Deformation can destroy arbitrary old witnesses.
The formulas above retain the exact all-target machinery:

* ranks one and two use direct exact endpoint witnesses;
* ranks three and four use the audited compact rank-five adjacent-shadow
  encoding plus its six exact exception slots;
* ranks five and six are exact permutations of their 462-element layers;
* every rank-seven mask uses the audited crossed-rank-six encoding or one of
  its six exact exception slots;
* ranks eight through eleven use direct exact endpoint witnesses.

Thus every SAT assignment is already an actual universal 465-entry word.
It must still be decoded and checked by both the exhaustive interval verifier
and the independent distinct-suffix-OR recurrence.

## 8. Is the portal formulation actually smaller?

Relative to the raw unrestricted `exact_or_sat.cpp` formulation reported in
the handoff (`8,098,440` variables and `21,305,534` clauses), reusing the
forest theorems is a major reduction: the branch formulas have about 2.88
million variables and 14.35 million clauses.

Relative to the best exact forest formulation, however, the answer is **no**.
The low-risk implementation merely fixes existing state and endpoint
variables.  It has essentially the same allocated inventory, with hundreds
or thousands of additional clauses.  Its advantage is semantic search-space
reduction and much stronger propagation, not DIMACS size.

A purpose-built generator may omit the twelve already forced rank-seven
target modules and the direct `958` module.  This saves approximately

```text
12 * 1,396  rank-seven endpoint variables
6 * 12      rank-seven exception-column variables
5,115       direct-958 variables
-----------------------------------------------
21,939 variables,
```

putting a fixed-row/fixed-prefix `q=19` formula near 2.860 million variables.
Eliminating the now-unit rank-six state variables saves at most another 4,620
variables.  Clause savings are roughly 0.1 million.  These are useful but not
dramatic (well under two percent).  They are not worth risking a new encoding
before the simple unit-clause branches have been tested and proof-audited.

## 9. Adversarial scope audit

1. **Saturation is an extra hypothesis.**  UNSAT for Section 4 says nothing
   about a different monotone-band schedule.
2. **A partial switch is also extra.**  Neither `q=13` nor `q=19` is WLOG.
3. **The concrete prefix is very narrow.**  Its UNSAT would only show that
   this particular factorable path does not extend.
4. **The named targets are not canonical.**  They were omissions of another
   factor.  That is why every other target remains encoded from scratch.
5. **No fake pins are introduced.**  All portal and central constraints are
   imposed on the common entry variables `a[p,b]`; simultaneous pin survival
   is automatic.
6. **Optional symmetry cuts can become unsound for the branch.**  Once decimal
   masks or entries are fixed, coordinate permutations need not preserve the
   branch.  Use the exact kernel listed in Section 2 and no coordinate-
   canonical extras.
7. **No UNSAT promotion.**  Only a checked SAT word settles `k=11` from these
   branches.  A proof-producing UNSAT run is still valuable, but its theorem
   statement must name the exact branch it refutes.

## 10. Implementation order

The production source should not be changed until this design is audited.
After audit, add one mutually exclusive environment mode with the following
values:

```text
q19_factor_prefix
q19_fixed_row
q19_abstract
q13_seam958
q369_triple_seam958
q369_dichotomy
```

The first implementation should be `q19_factor_prefix`, followed by
`q19_fixed_row`.  Both need only unit clauses against already allocated
variables and therefore have the smallest possible implementation risk.

