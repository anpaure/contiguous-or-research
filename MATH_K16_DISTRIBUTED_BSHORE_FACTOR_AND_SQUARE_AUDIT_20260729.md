# A resident q1-complete `k=16` B shore and the remaining square-circulation gate

Date: 2026-07-29

## 1. Status

This note does **not** prove `nu(16)=12873`.  It proves a new one-sided
factor theorem needed by a distributed odd-to-even braid, and gives two exact
obstructions to the most direct ways of using that factor.

The strict shared-tail construction is excluded by Theorem 7.1 of
`MATH_ODD_EVEN_SHARED_TAIL_LIFT_20260727.md`: if consecutive central cells
are distinct equicardinal sets, every source letter in the strict appended
sector is nonempty after projection, so the singleton new coordinate is
missing.

The surviving architecture must distribute the new coordinate.  Its exact
last gate is still a feasible unrestricted `COMP_3` selector containing a
source cell equal to `{z}`.  A marked internal four-cell B run is a convenient
staged sufficient channel for that selector.  It is not asserted to be a
globally necessary or sufficient condition: truncated boundary source cells
are genuine alternatives, and every marked ear still requires a full
compiler audit.

## 2. One-sided fixed-`M_0` factor theorem

Let `X=[15]`.  There exists a spanning Johnson 2-factor `F` on
`binom(X,8)` with the following properties.

1. Every rank-nine set occurs as the union of an edge of `F`.
2. In every cyclic component of `F`, every nonconstant coordinate zero-run
   has length at least four.
3. Consequently the complemented factor

   \[
   \bar F=\{X\setminus U:U\in F\}
   \tag{2.1}
   \]

   is a spanning Johnson 2-factor on `binom(X,7)`, every positive coordinate
   run in `bar F` has length at least four, and every rank-six set occurs as
   an edge intersection.

The physical component lengths of `bar F` are

\[
6045,135,45,35,35,35,20,20,20,15,15,15.
\tag{2.2}
\]

Its rank-six edge-colour loads are

\[
1^{3720}2^{1155}3^{115}4^{15}.
\tag{2.3}
\]

The minimum positive run is exactly four.

### Proof certificate

The factor lies in the same-`v`-excluded fixed-`M_0` equivariant face.  The
reduced formula consists of:

- one selected quotient edge at each of 429 lower orbits;
- one selected quotient edge at each of 429 middle orbits;
- all 335 upper-q1 orbit-cover clauses;
- the 761,235 audited dual zero-gap clauses.

The final formula has 2,999 variables and 780,398 clauses, SHA-256

`3a1823c2757ec9cd7ddf1625cb32b261a71240d97cdcf7694db8463bd2d52459`.

The fail-closed audit checks every clause under the returned assignment,
decodes exactly 429 quotient choices, verifies both quotient-shore
injections, expands to all 6,435 physical middle states, reconstructs every
cycle, and literally enumerates all parent unions, complemented B
intersections, and cyclic B coordinate runs.  It returns the counts in
(2.2)--(2.3) with no missing q1 target and no short B run.

Stable artifacts are:

- `scratch/seed0.upperq1.dualresident.candidate.json`, SHA-256
  `4d9371522665ac1134381bec80c744b9dfd587aa1908419229a52a5b158e4e5f`;
- `scratch/seed0.upperq1.dualresident.components.json`, SHA-256
  `ea45990f5516dd6085d54ecad16eea222f30ae957c58968cfaf284f41aa09c7c`;
- `scratch/seed0.upperq1.dualresident.audit.json`, SHA-256
  `13dcc0b4e26ec504009be995e6be2a4fc5f662f969bcb0f5851dfa8c0f963960`.

The builders/auditor are
`scratch/build_k15_fixed_m0_upper_q1_base_20260729.py` and
`scratch/audit_k15_fixed_m0_upperq1_dualresident_20260729.py`.

This is a one-sided theorem.  The parent rank-eight factor has 1,110 short
positive runs (minimum two), lower-q2 has 26 missing quotient orbits, and
deeper rows are not protected.  None of those properties is silently
claimed.

## 3. Exact cut-only obstruction for the new factor

Only BB edges can realize the child lower-q1 targets containing `z`.  If a
BB edge of rank-six colour `S` is cut and no BB edge of colour `S` remains,
then no mixed AB seam can restore `z+S`; at most two such colours can be
assigned to the two global compiler boundaries.

Call a B component **sealed** when every one of its edge colours has global
load one.  The factor (2.1) has exactly three sealed components, namely the
three components of length 15 in (2.2).

### Proposition 3.1

No construction which opens every component of (2.1) and reconnects the
pieces using only mixed AB seams can preserve all but at most two B lower-q1
colours.

### Proof

Opening a cyclic component deletes at least one of its BB edges.  In a
sealed component the deleted colour has no second BB occurrence.  Mixed AB
seams have z-free intersections, so they cannot restore it.  The three
sealed components therefore force three distinct z-bearing rank-seven
holes, but the exact compiler has only two rank-seven boundary channels.
This contradicts the required hole bound.  `square`

The exact cut/ear CP-SAT replay is independently unnecessary for this proof,
but agrees: it is infeasible in 1.02 seconds.  Its report is
`scratch/seed0.upperq1.dualresident.cutear.json`, SHA-256
`5d947db2ed8f937f8ad8ed5c452e8732be8bc06578d5c5a6417757836fda42ca`.

Thus the new factor needs either a BB rethreading which restores at least one
sealed colour, or a different SAT point with at most two sealed components.

An isolated two-edge repair which directly joins one of the original sealed
components is also excluded for this factor.  Across the three sealed cycles
and every edge of every other component there are 825 two-edge switches
whose two replacement pairs are Johnson edges.  Exactly 120 preserve every
B lower-q1 colour, but none of those 120 both directly joins an original
sealed component and preserves depth-three residence at the two new seams.
Since the source cycles are already resident, the two seam-collar test is
necessary and sufficient for one isolated two-edge switch.  This census does
not exclude interacting switches, packets whose colour losses compensate,
or restoration by a new BB edge away from the original sealed component.

The census is
`scratch/search_k16_bshore_q1_resident_twoedge_switches_20260729.py`; its
report is `scratch/seed0.upperq1.dualresident.bbswitches.json`, SHA-256
`0b9e7a96a17057ec4bd615e434a8f9a6e8e18b73fccb408e078e2b2c5e6a254f`.

## 4. Exact square catalogue against the solved `k=15` A path

Let

\[
A=D^3(\texttt{answers/k15.word}).
\]

For an AA edge `X0-X1` and a B edge `R0-R1`, the colour-aware square
conditions are

\[
R_0=X_0\cap X_1,
\qquad
X_0=R_0\cup R_1.
\tag{4.1}
\]

Replacing those two rail edges by

\[
X_1-(z+R_0),
\qquad
X_0-(z+R_1)
\tag{4.2}
\]

restores the removed AA-lower colour `R0` and removed BB-upper colour
`z+X0` identically.  The only q1 costs are the removed AA-upper and BB-lower
colours.  This is Lemma 2.1 of
`MATH_K16_DUAL_RAIL_SQUARE_SWITCH_REDUCTION_20260729.md`.

Exhausting (4.1) for the factor in Section 2 and the fixed A path gives:

\[
\begin{array}{c|r}
\text{all literal squares}&3614\\
\text{two-collar resident squares}&345\\
\text{both non-restored colours duplicated}&690\\
\text{collar resident and both colours duplicated}&90.
\end{array}
\tag{4.3}
\]

All 90 fully safe squares meet the 6045-cycle.  More sharply:

- the 45-cycle has no square satisfying (4.1);
- the 135-cycle and 45-cycle have no collar-safe square;
- every component except the 6045-cycle has no square which is both
  collar-safe and strictly q1-safe.

Therefore a packet of one independent square per B component cannot fuse
this SAT point to the fixed A path.  This is a scoped no-go: interacting
square packets, BB switches, another A chronology, or another SAT factor
remain possible.

The literal enumerator is
`scratch/audit_k16_dualrail_square_catalogue_20260729.py`.  Its report is
`scratch/seed0.upperq1.dualresident.square_catalogue.json`, SHA-256
`d07c6149a09d637d188652f69eaf2cd65172dbc1568ad2e4e5ba3b10c761fb07`.

## 5. PBBS calibration and its sharper opening obstruction

The centered PBBS factor on rank-seven sets, reordered by the square of the
PBBS permutation, has:

\[
73\text{ components},qquad
1^{3630}2^{1320}3^{55}\text{ q1 loads},
\tag{5.1}
\]

complete 5005/5005 rank-six support, and 945 short positive runs:

\[
90\text{ of length }2,qquad855\text{ of length }3.
\tag{5.2}
\]

Exactly twenty PBBS components are sealed: component 0 of length 15,
component 1 of length 165, components 2--6 of length 135, and components

\[
7,8,9,10,11,13,14,15,17,18,20,25,26
\]

of length 105.  Opening all PBBS cycles with mixed seams therefore costs at
least twenty unique B q1 colours, independent of residence.  Hence PBBS is a
correct q1-complete starting factor but requires genuine BB circulation; a
cut-only repair cannot approach the two-hole compiler bound.

The exact census/model is
`scratch/k16_pbbs_bshore_residence_cut_model_20260729.py`.  Its report is
`scratch/pbbs_bshore_residence_cut_b2.json`, SHA-256
`d0e51d64f31b900ef1314ca04372a70ff48a50b42cb7b91e53f8ec48157ecafb`.

## 6. Smallest surviving theorem gate

The distributed B-shore problem is now the following exact finite statement.

> **B-shore square/circulation gate.**  Construct a rank-seven Johnson path
> cover on `binom([15],7)` whose positive coordinate runs are depth-three
> resident.  Couple it to a resident A chronology by colour-aware squares and
> any needed BB switches so that the child middle graph is one path.  After
> all AA, AB and BB surgery, the **total** residual lower-q1 family must fit
> the two compiler boundary cells.  The resulting chronology must also pass
> all upper-shadow ledgers and unrestricted `COMP_3`, including an actual
> selector cell `e_p={z}`.  A marked four-state B ear may be imposed as a
> sufficient staged singleton channel, but is not substituted for the
> compiler condition.

For the present SAT factor, Proposition 3.1 rules out cut-only opening; the
two-edge census rules out an isolated two-edge switch directly joining an
original sealed component; and the square census rules out an independently
safe one-square-per-component repair.  Coordinated multi-switch and
colour-compensating packets remain open.  For PBBS, at least eighteen of its
twenty sealed opening losses must be restored by BB circulation before the
two-boundary theorem can apply.

No `k=16` word is claimed until the final middle chronology, complete upper
support, common compiler, and literal 65,535-target replay all pass.
