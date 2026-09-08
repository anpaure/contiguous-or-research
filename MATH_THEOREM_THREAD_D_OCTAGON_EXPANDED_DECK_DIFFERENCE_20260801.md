# Exact expanded-source deck difference of the quaternary octagon

Date: 2026-08-01  
Lane: Thread D, terminal compiler interface for the resident octagon packet  
Status: exact all-depth family classification for the maximal and sharp
inverse words after the two exterior split hosts.  This note proves a
bounded laminar **relation** interface, not a terminal target-cell matching.

## 0. Outcome

Let `d>=2`.  Add the two split hosts of
`MATH_THEOREM_THREAD_D_OCTAGON_SPLIT_BOUNDARY_RESET_20260801.md` to the
maximal or sharp depth-`d` inverse of the resident octagon tensor.  If
`Delta_epsilon` is the set of distinct interval unions which occur in phase
`epsilon` but not in the other phase, then

\[
 (|\Delta_0^{\max}|,|\Delta_1^{\max}|)=(2d+1,2d+1),       \tag{0.1}
\]

and

\[
 (|\Delta_0^{\sharp}|,|\Delta_1^{\sharp}|)
       =(4d+1,6d-3).                                      \tag{0.2}
\]

The reported sharp census

\[
 (9,9),(13,15),(17,21),\ldots,(41,57)
\]

for `d=2,...,10` is therefore exact.

There is no hidden grid.  The maximal difference is three boundary masks
plus two nested filler rays on each shore.  The sharp difference is the
maximal one plus a bounded number of further nested rays.  However this is
only `O(1)` **family complexity**: the number of literal target masks is
linear in `d`.

The maximal ledger is balanced, but balance alone does not give native
return because every member of a directed difference is, by definition,
absent from the opposite packet phase.  The sharp ledger has the stronger
obstruction

\[
                  |\Delta_1^{\sharp}|-|\Delta_0^{\sharp}|=2d-4. \tag{0.3}
\]

Thus, for `d>=3`, a two-way one-for-one native-return scheme is impossible
even at the scalar level.  A terminal implementation must solve an actual
compiler/common-cap matching to external or unaffected duplicate cells.
Replacing the sharp inverse by the balanced maximal inverse removes the
scalar imbalance, but does not remove that matching gate.  The ray table
makes the gate laminar; it does not make it automatic.

## 1. Notation and expanded coordinates

Suppress the fixed core `K`, which is coned onto every mask below.  Put

\[
 F=\{f_0,\ldots,f_{d+1}\},\qquad
 F[i,j]=\{f_i,\ldots,f_j\}.                              \tag{1.1}
\]

Let `Q^epsilon` denote either the maximal or sharp inverse.  Its length is
`9d+23`.  In the phase-oriented split-host expansion use

\[
 \widehat Q^\epsilon=
 (a_\epsilon,a_{1-\epsilon})\mid Q^\epsilon\mid
 (a_{2-\epsilon},a_{1+\epsilon}),                       \tag{1.2}
\]

where the subscripts in (1.2) have their literal values `0,1,2` rather
than cyclic interpretation.  Thus

\[
\begin{array}{c|cc}
 &\text{left far,near}&\text{right near,far}\\ \hline
0&(a_0,a_1)&(a_2,a_1)\\
1&(a_1,a_0)&(a_1,a_2).
\end{array}                                               \tag{1.3}
\]

All interval coordinates below are zero based in the expanded word
`widehat Q`, whose length is `9d+27`.  The displayed rank is the rank after
suppressing `K`; the physical rank is larger by `|K|`.

For a word `X`, write `D(X)` for its distinct-value interval-union deck and

\[
 \Delta_\epsilon(X)=\mathcal D(X^\epsilon)-
                     \mathcal D(X^{1-\epsilon}).         \tag{1.4}
\]

## 2. The maximal inverse

### Theorem 2.1 (two rays plus three boundary masks)

The following tables are disjoint and exhaust the two directed maximal
differences.  The last column gives one canonical literal interval witness.

For phase zero:

\[
\begin{array}{c|c|c|c}
\text{name}&\text{mask}&\text{rank}&[\ell,r]\\ \hline
L_0^-&\{a_1,a_2,a_3\}\cup(F-f_0)&d+4&[1,2]\\
L_0 &\{a_1,a_2,a_3\}\cup F&d+5&[1,d+3]\\
P_{0,h}&\{z,a_1\}\cup F[1,h]&h+2&[6d+19,6d+18+h]\\
S_{0,h}&\{z,a_3\}\cup F[d+1-h,d]&h+2&[7d+20-h,7d+19]\\
R_0^-&\{a_0,a_2,a_3\}\cup(F-f_{d+1})&d+4&[8d+24,9d+25]
\end{array}                                               \tag{2.1}
\]

where `1<=h<=d-1`.  For phase one:

\[
\begin{array}{c|c|c|c}
\text{name}&\text{mask}&\text{rank}&[\ell,r]\\ \hline
L_1^-&\{a_0,a_2,a_3\}\cup(F-f_0)&d+4&[1,2]\\
P_{1,h}&\{z,a_3\}\cup F[1,h]&h+2&[2d+7,2d+6+h]\\
S_{1,h}&\{z,a_1\}\cup F[d+1-h,d]&h+2&[3d+8-h,3d+7]\\
R_1&\{a_0,a_1,a_3\}\cup F&d+5&[7d+22,9d+25]\\
R_1^-&\{a_0,a_1,a_3\}\cup(F-f_{d+1})&d+4&[8d+24,9d+25].
\end{array}                                               \tag{2.2}
\]

Consequently both directed differences have `2(d-1)+3=2d+1` values.  Their
rank multisets agree: two values at every rank `3,...,d+1`, two at rank
`d+4`, and one at rank `d+5`.

## 3. The sharp eight-address inverse

The maximal families (2.1)--(2.2) remain present after sharp thinning.  The
following are precisely the additional values.

### Theorem 3.1 (complete sharp correction table)

For phase zero the additional values are

\[
\begin{array}{c|c|c|c}
\text{name}&\text{mask}&\text{rank}&[\ell,r]\\ \hline
A_{01}^-&\{a_1\}\cup(F-\{f_0,f_1\})&d+1&[5d+18,6d+16]\\
A_{01}&\{a_1\}\cup(F-f_0)&d+2&[5d+17,6d+16]\\
A_{03}^-&\{a_3\}\cup F[0,1]&3&[7d+22,7d+22]\\
A_{03}&\{a_3\}\cup F[0,2]&4&[7d+22,7d+23]\\
S^+_{0,h}&\{z,a_3\}\cup F[d+1-h,d+1]&h+3
          &[7d+20-h,7d+20]\\
S^{0+}_{0,h}&\{z,a_3,f_0\}\cup F[d+1-h,d+1]&h+4
          &[7d+20-h,7d+21].
\end{array}                                               \tag{3.1}
\]

Here `1<=h<=d-2` in the last two rows.  Hence (3.1) contributes
`4+2(d-2)=2d` values and

\[
                         |\Delta_0^\sharp|=2d+1+2d=4d+1. \tag{3.2}
\]

For phase one the additional values are

\[
\begin{array}{c|c|c|c}
\text{name}&\text{mask}&\text{rank}&[\ell,r]\\ \hline
A_{11}^-&\{a_1\}\cup F[0,1]&3&[3d+10,3d+10]\\
A_{11}&\{a_1\}\cup F[0,2]&4&[3d+10,3d+11]\\
S^+_{1,h}&\{z,a_1\}\cup F[d+1-h,d+1]&h+3
          &[3d+8-h,3d+8]\\
S^{0+}_{1,h}&\{z,a_1,f_0\}\cup F[d+1-h,d+1]&h+4
          &[3d+8-h,3d+9]\\
A^L_{13,h}&\{a_3\}\cup F[1,h+2]&h+3&[d+5,d+5+h]\\
A^R_{13,h}&\{a_3\}\cup F[2,h+2]&h+2&[d+6,d+5+h].
\end{array}                                               \tag{3.3}
\]

The two `S` rows have `1<=h<=d-2`; the two `A_13` rows have
`1<=h<=d-1`.  Thus (3.3) contributes

\[
                 2+2(d-2)+2(d-1)=4d-4                  \tag{3.4}
\]

values, proving `|Delta_1^sharp|=2d+1+4d-4=6d-3`.

All families in (3.1) and (3.3) are inclusion chains in their parameter.
The only imbalance is the long two-ray `A_13` bank replacing the two-cell
`A_01` chain.  After matching their top-rank endpoints, the unmatched rank
ledger is

\[
\begin{array}{c|ccc}
\text{displayed rank}&3&4,\ldots,d&d+1\\ \hline
\text{phase-one surplus}&1&2\text{ at each rank}&1.
\end{array}                                               \tag{3.5}
\]

For `d>=3` its total is `1+2(d-3)+1=2d-4`.  At `d=2` the two displayed
endpoint ranks coincide with the two matched top endpoints, and the surplus
is empty, again giving `2d-4=0`.

## 4. Proof of the classifications

The fixed split hosts have the same untyped interval deck in both
orientations.  Hence an exclusive value must contain at least one tensor
source cell.  Insert the maximal erosion definition

\[
 E_p^\epsilon=
 \bigcap_{\max(0,p-d)\le i\le\min(8d+22,p)}T_i^\epsilon \tag{4.1}
\]

and sweep the right endpoint for each fixed left endpoint.  Until the next
active-label occurrence, only a consecutive filler interval grows.  Once
both phase-exclusive active labels have appeared, the active union is
phase-common and no later interval can be exclusive.

There are exactly five surviving endpoint corridors.  The two exterior
corridors give the three boundary rows of (2.1) or (2.2).  The two interior
single-screen corridors give `P_epsilon,h` and `S_epsilon,h`; their filler
endpoints advance by one, yielding `1<=h<=d-1`.  Every other interval either
has a phase-common union before reaching a corridor, or saturates to a
phase-common active union after leaving it.  This proves (2.1)--(2.2),
including exhaustiveness.

For the sharp word replace every nonexceptional erosion letter by
`E_p^0 cap E_p^1`.  Only the eight exceptional addresses remain
phase-specific.  Repeating the same endpoint sweep leaves the maximal five
corridors plus:

* two terminal intervals on each of the `a_1` and `a_3` singleton traces;
* two suffix extensions through `f_(d+1)` and then `f_0`; and
* in phase one, the two possible starts of the long `a_3` filler corridor.

Writing those successive filler unions gives exactly (3.1) and (3.3).
Leaving any displayed endpoint corridor adds the next missing active label
and makes the union phase-common, proving exhaustiveness.  The counts and
ranks follow directly.

## 5. Compiler consequence

Theorems 2.1 and 3.1 compress the arbitrary-width interval comparison to a
constant list of laminar family types.  In particular there is no analogue
of the unrestricted donor-grid obstruction in this local expanded packet.

This does **not** collapse the terminal compiler to `O(1)` cells.  A chain
of `d-1` distinct masks still requires `d-1` distinct occurrences in an
injective target-cell assignment.  Moreover none of the masks in
`Delta_epsilon` occurs internally in the opposite expanded phase.  Thus:

1. the maximal inverse has no scalar or rank-profile imbalance, but still
   needs an exact matching to native external duplicates or common-cap
   compiler cells;
2. the sharp inverse has the additional `2d-4` obstruction (3.5) on the
   phase-one-to-phase-zero return leg; and
3. any claimed regenerative reset must exhibit the matching.  The bounded
   ray table alone is not a reset certificate.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_octagon_expanded_deck_difference_20260801.py
```

The audit reconstructs both expanded source words, computes their complete
distinct interval decks, and checks equality with every mask, rank and
zero-based witness in (2.1)--(3.3) for `2<=d<=12`.  It reports

```text
PASS_THREADD_OCTAGON_EXPANDED_DECK_DIFFERENCE
payload_sha256=dc66f1d5e0680036f54e677c2ef851536e3eec7479324494ee1a62276a0050c7
```

The frozen payload is

```text
scratch/threadD_octagon_expanded_deck_difference_20260801.audit.json
```

The finite replay is an audit of the displayed all-`d` endpoint sweep, not
a substitute for its proof.  Ambient deadline, owner, prescribed-cap and
target-cell Hall legality remain outside this note.
