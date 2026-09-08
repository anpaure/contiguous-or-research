# Hostile audit: the resident C8 is an internal three-state reset, but 164 D5 rows force terminal connectors

**Date:** 2026-08-14
**Scope:** hostile audit of
`MATH_REDUCTION_D5_ROW_RESET_TO_PRESCRIBED_TERMINAL_RESIDENT_C8_QUOTIENT_20260814.md`
**Verdict:** **PASS** in the stated **closed internal** scope.  With the four
displayed heptagonal backups it
satisfies the internal parts of clauses 1--4 of the conditional D5 reset
gate.  It does not satisfy the exposed-terminal quantifiers or prove the
212-copy prescribed coinstantiation.  An exact D5 replay shows that 164 of
the 212 reset rows cannot be obtained by literal coordinate relabelling of
the two marked C8 sockets.

## 1. Clause-by-clause verdict

The conditional reset gate in
`MATH_THEOREM_T2_D5_RESIDENCE_DILATION_SUCCESSOR_TAG_NOGO_AND_THREE_STATE_RESET_GATE_20260814.md`
requires one fixed-bank three-terminal cell.  The complementary-square C8,
the four fixed backups, and a formal untouched spectator have the following
status.

| D5 clause | closed internal quotient | prescribed D5 substitution |
|---|---|---|
| 1. same owner, immediate-lower, and immediate-upper bank | **PASS** | conditional on disjoint terminal grafts |
| 2. both states and all exposed collars are q2-biresident | internal cycles **PASS** | exposed collars **UNPROVED** |
| 3. swap the two head ports, fix the tail, inverse in the same bank | **PASS** as a marked first-return quotient plus formal identity spectator | physical tail wire and terminal identification **UNPROVED** |
| 4. old-to-new q2 support is monotone | upper row **PASS**; lower row **PASS after the four backups** | graft-crossing lower and upper windows **UNPROVED** |

Thus “abstract row reset closed” is correct.  “D5 reset cell constructed”
would not be correct.  The marked owners are saturated interior vertices of
the closed C8 bank, and the spectator is only a direct-sum identity port
until an actual fixed resident path is cut and grafted.  Those are exactly
the terminal qualifications retained in the reduction note.

## 2. Exact internal action and resources

The old first-return map on all four incoming sockets is the identity and
the switched map is

\[
                              i\longmapsto i+1\pmod 4.
\]

Suppressing the unmarked sockets gives identity and the transposition on
`{R_0,R_2}`.  Adjoining a disjoint identity socket `a` therefore gives the
abstract action

\[
                              1_a\times(R_0\ R_2).
\]

The matching toggle is involutive, so the inverse uses the same bank.

Independent replay also confirms that the old four cycles and the switched
merged cycle have exactly the same owner, immediate-lower, and
immediate-upper palettes.  Each palette has `8m-8` values, every value has
load one, and the owner-current theorem supplies zero upper/union current at
every width.  The four heptagonal backups are unchanged in the two states,
so adjoining them preserves all three equal-bank statements.

## 3. Lower-q2 current and the uniqueness proof

Only two triple-owner windows on each side of a switched incidence change.
With the notation of the reduction, their signed contribution is

\[
 \sum_i\bigl([A_i^+]-[A_i^-]
              +[B_{i+1}]-[B_i]\bigr)
 =\sum_i([A_i^+]-[A_i^-]).
\]

The eight `A` values are distinct: the active adjacent pair determines the
index up to the shift between `A_i^+` and `A_{i+1}^-`, and in that remaining
case the missing core labels are the distinct `t_i,t_{i+1}`.

The claimed support census is also correct, but the prose proof should make
one finite endpoint classification explicit.  A triple intersection with
no `a` or `Z`, with all but one `C` coordinate, can occur only in the last
three/closure neighbourhood of one complementary path.  The candidates
there are

\[
\begin{aligned}
 G_{i,n-3}\cap S_i\cap R_i
   &=(C-t_i)+q_i+q_{i+2},\\
 S_i\cap R_i\cap U_i&=A_i^-,\\
 R_i\cap U_i\cap F_{i,1}&=B_i,
\end{aligned}
\]

and after switching the last two become `A_i^+` and `B_{i+1}`.  All other
forward or return windows either contain a neutral coordinate in their
intersection or miss at least two core coordinates.  The nonadjacent active
pair in the first displayed candidate separates it from every `A`; the
missing core label separates `A` from `B` and separates the shifted `A`
values.  This proves that each `A_i^-` has old load one and switched load
zero, and dually each `A_i^+` is a singleton birth.

The independent H100 audit checked this formula, uniqueness, and exact
support loss for all 399 admissible pairs with `13<=m<=50`, not merely the
one-`q`-per-`m` schedule used by the reduction's 63-case replay.

## 4. The four backups are a valid internal repair

For each lost target, put

\[
 K_i=A_i^- -c_0,
 \qquad
 \sigma_i=(c_0,a,q_{i+2},q_{i+3},z_0,z_1,z_2).
\]

The cyclic length-three windows of `sigma_i`, added to `K_i`, form a
seven-owner Johnson cycle.  Consecutive owner windows overlap in two labels
and have union four; three consecutive windows meet in one label.  The
window whose common label is `c_0` therefore contributes `K_i+c_0=A_i^-`
once.

Across all four backups the owner/lower/upper palettes have sizes
`28,28,28`, are simple, and are disjoint from both states of the main C8
bank.  Their nonconstant owner, lower, and upper run/gap pairs are
respectively `(3,4)`, `(2,5)`, and `(4,3)`, so they meet the q2 internal
residence requirement.  Because the same cycles occur in both states, all
their q2 targets have zero signed current.  Adding them changes the four
lost loads from zero to one and leaves no old support value absent after the
switch.

This closes the **internal** lower-q2 defect.  It does not cover any new
triple window created when a marked socket or spectator is cut and joined to
an exterior D5 path.

## 5. Exact prescribed-terminal counterexample

The C8 marked owners are adjacent:

\[
 d_J(R_0,R_2)=1.
\]

Indeed all four `R_i` form the four triples of the same four-element active
set, so every pair of C8 incoming sockets has Johnson distance one.  A
coordinate relabelling preserves Johnson distance.

The frozen D5 selection and frozen proper three-colouring give the following
literal geometry on the 212 nontrivial reset rows.  Each tuple records

\[
 (d_J(a,b),d_J(a,c),d_J(b,c),|a\cap b\cap c|,
                                  |a\cup b\cup c|).
\]

```text
(1,1,1,10,13)   48 rows
(1,1,2, 9,13)  164 rows
```

Consequently 164 rows are direct counterexamples to identification of the
old/new D5 heads with `R_0,R_2` by a coordinate relabelling.  They
necessarily require nontrivial connector paths (or a different local
router).  In the remaining 48 rows the three terminals form a top-type
Johnson triangle: after a common-rank lift, the two heads can match
`R_0,R_2` and the tail has the incidence type of a third owner over their
common facet.  This is incidence compatibility only; it does not construct
a disjoint fixed spectator wire or certify its terminal collars.

The 212-copy row is therefore genuinely stronger than 212 independent
abstract copies.  It requires simultaneous connector selection, occurrence
splitting at the three multiplicity-four external roles, common
owner/lower/upper resource simplicity, and every crossing residence/current
test.  The low-exposure host theorem applies only after that one closed bank
has been built.

## 6. Repairs applied before freeze

The reduction was rebound only after the following changes were applied.

1. The literal backspace/control character formerly in `(2.6)` was replaced
   by `\mathcal B_i=\bigl(...)`.
2. The H100 paragraph now says that the 63 cases use the schedule
   `q=max(5,floor(sqrt(m))+1)`, one admissible `q` for each `18<=m<=80`.
   This pins the sampled scope without implying exhaustion of all admissible
   `q` at those `m`.
3. The support proof now uses the full `A_i^\pm` signature rather than rank
   alone and includes the three-candidate endpoint classification from
   Section 3 above.

## 7. H100 certificate

The independent verifier is
`scratch/audit_d5_c8_prescribed_terminal_reduction_independent_20260814.py`.
It rebuilt the C8 and backups for every admissible `(m,q)` with
`13<=m<=50`, rebuilt all 477 frozen D5 rows, and checked the exact 48/164
terminal histogram.  Compilation, replay, and hashing were performed only
on H100.

```text
audited reduction SHA-256
07084bd86c85b09ca281c7f9d284954f76d8416d17f83d188fde9ee8f54d5dd0

independent verifier SHA-256
93ff61c9422e56ac70ccd07ce8372bd3e178401d6110d899592c13db1f8b1021

independent output SHA-256
cd0f8875c6486d8194a8125f25e01679d55fc0e0a439ebb14a2e4b9a835fd068

frozen D5 selection SHA-256
94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32

frozen D5 state certificate SHA-256
05552624784b67253b9f7d07b3e37c63cb25254d9b80872835952c38ba9605c1
```

The audited reduction's own current verifier and output hashes are,
respectively,

```text
bf4662fc1e921014907408df1a82e471ce93bbb415d86235287cec112c2b7bd1
9e1fe95b14eef108fd0a0ca2e2ff1522885e8f5e1206990717f30fb36131c001
```

The sharp remaining gate is not another abstract odd-action gadget.  It is
the simultaneous prescribed-terminal connector bank, forced to be
nontrivial on at least the 164 distance-two head pairs, together with the
crossing collar/current audit.
