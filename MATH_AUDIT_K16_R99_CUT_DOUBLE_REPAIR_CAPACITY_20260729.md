# Audit of the `k=16`, radius-99 cut-only double-repair capacity relaxation

Date: 2026-07-29  
Status: **exact necessity theorem and solver-free model census; no CP-SAT result claimed**

## 1. Verdict

The cut-only double-repair model is a sound necessary relaxation in the
frozen loopless `C_15` quotient scope.  Every degree-balanced, both-q1,
99-seam completion induces binary auxiliary variables satisfying the rows
below for its fixed cut.  The branch-uniform 14/12 consequences additionally
use the audited 147-motif-hitting cut scope required of a resident candidate.

1. activation by the cut sole-provider edges;
2. matching capacity one in every lower and upper unique-colour class;
3. the cut endpoint capacities; and
4. the dynamic demand row

\[
 \boxed{
 \sum_{a\in A_{\rm both}} y_a
 \;\ge\;
 \sum_{e\in S}(w_L(e)+w_U(e))x_e-99.
 }
 \tag{1.1}
\]

The exact unique-loss diagonals 113 in the `RETAIN_22511` branch and 111 in
the `DELETE_AND_REPLACE_22511` branch imply the uniform demands 14 and 12.
The dynamic row is stronger: for example, the delete Pareto point `(64,48)`
has demand 13.

Passing this relaxation is not sufficient for a completion.  It does not
assert that the selected auxiliary seams extend to all 99 additions, cover
the remaining q1 rows, or satisfy residence, connectivity, or voltage.

## 2. Frozen scope and census

Let `S` be the 858-edge loopless source factor.  The frozen inputs are:

```text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8

scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json
SHA-256 b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e
```

The cut projection has 147 current residence-motif rows.  A radius-99 cut
is represented by `x_e=1` for a source edge `e` that is deleted, with either
`x_22511=0` or `x_22511=1` for the two branches.

For a source edge `e`, define

\[
 w_L(e)=1
 \quad\Longleftrightarrow\quad
 e\text{ is the sole selected source provider of its lower q1 colour},
 \tag{2.1}
\]

and define `w_U(e)` analogously.  The exact source census is

\[
 \#(w_L,w_U)=
 (00:32,\ 01:151,\ 10:153,\ 11:522).
 \tag{2.2}
\]

Thus there are 675 source-unique lower colours and 673 source-unique upper
colours.  Let `p_L(c)` and `p_U(d)` denote their unique source providers.

There are 26,570 loopless off-source seams.  Let

\[
 A_{\rm both}=\{a:
 \operatorname{lower}(a)\text{ is source-unique and }
 \operatorname{upper}(a)\text{ is source-unique}\}.
 \tag{2.3}
\]

The exact census is

\[
 |A_{\rm both}|=20{,}787.
 \tag{2.4}
\]

Among these seams, 13 have the same source edge as their lower and upper
unique provider.  There are 20,504 distinct ordered source-provider pairs,
with seam multiplicity histogram

\[
 1^{20{,}221}2^{283}.
 \tag{2.5}
\]

Every one of the 675 lower colour classes, 673 upper colour classes, and 858
quotient nodes occurs in the auxiliary-seam incidence system.

## 3. Necessity theorem

Fix a radius-99 source cut `C`.  Put

\[
 L(C)=\sum_{e\in S}w_L(e)x_e,
 \qquad
 U(C)=\sum_{e\in S}w_U(e)x_e.
 \tag{3.1}
\]

These are the source-unique lower and upper colours whose sole provider is
cut.  Let `A` be the 99-edge addition set of an exact degree-balanced,
both-q1 completion.

### Theorem 3.1

There is a subset `Y` of `A intersect A_both` such that:

\[
 |Y|\ge L(C)+U(C)-99;
 \tag{3.2}
\]

the seams in `Y` have pairwise distinct lower colours and pairwise distinct
upper colours; both unique source providers of every seam in `Y` lie in
`C`; and, at every quotient node `v`,

\[
 d_Y(v)\le d_C(v).
 \tag{3.3}
\]

#### Proof

For each lost source-unique lower colour, choose one added seam that restores
it.  The chosen seams form a set `R_L` of size `L(C)`: the choice is
injective because one seam has only one lower colour.  Similarly choose a
set `R_U` of size `U(C)` for the lost upper colours.  Both are subsets of the
same 99-edge addition set, so inclusion-exclusion gives

\[
 |R_L\cap R_U|
 \ge |R_L|+|R_U|-|A|
 =L(C)+U(C)-99.
 \tag{3.4}
\]

Set `Y=R_L intersect R_U`.  Membership in the two representative sets makes
every seam in `Y` a simultaneous repair.  Injectivity of the representatives
in each palette makes `Y` a lower/upper colour matching.  Its two colours
are lost, so their unique source providers are cut.

Finally, both the source and completed factors have the same quotient
degree at every node.  All edges in this scope are loopless, hence

\[
 d_A(v)=d_C(v).
 \tag{3.5}
\]

Since `Y` is a subset of `A`, (3.3) follows.  This proves the theorem and the
dynamic row (1.1).  No product-variable argument is used.  QED.

The theorem only counts source-unique losses.  A nonunique q1 row may also
be lost when all of its source providers are cut; such losses can only add
requirements and do not weaken the theorem.

## 4. Exact binary extended formulation

Use binary variables

\[
 x_e\quad(e\in S),
 \qquad
 y_a\quad(a\in A_{\rm both}).
 \tag{4.1}
\]

Here `y` selects a possible representative matching.  It is not asserted to
equal the set of all simultaneous repairs.

The cut rows are

\[
 \sum_{e\in S}x_e=99,
 \qquad
 x_{22511}=b,
 \qquad
 \sum_{e\in M}x_e\ge1
 \quad\text{for each of the 147 motifs }M.
 \tag{4.2}
\]

Activation and matching can be compressed into one gated row per unique
colour:

\[
 \sum_{a:\operatorname{lower}(a)=c}y_a
 \le x_{p_L(c)},
 \tag{4.3}
\]

\[
 \sum_{a:\operatorname{upper}(a)=d}y_a
 \le x_{p_U(d)}.
 \tag{4.4}
\]

When the unique provider is retained, the right side is zero and all such
`y` variables are inactive.  When it is cut, the right side is one and the
row imposes the palette matching capacity.

The endpoint rows are

\[
 \sum_{a\ni v}y_a
 \le
 \sum_{e\in S:\,e\ni v}x_e
 \qquad(v=0,\ldots,857),
 \tag{4.5}
\]

and the final row is (1.1).

### Model census

The compressed model has

\[
 \boxed{21{,}645\text{ Boolean variables and }2{,}356\text{ constraints}.}
 \tag{4.6}
\]

The variables are 858 cut variables and 20,787 matching-selector variables.
The constraints split as follows:

\[
\begin{array}{l|r}
\text{row family}&\text{count}\\ \hline
\text{cut cardinality}&1\\
\text{locked branch}&1\\
\text{motif hitting}&147\\
\text{gated lower colours}&675\\
\text{gated upper colours}&673\\
\text{endpoint capacities}&858\\
\text{dynamic demand}&1\\ \hline
\text{total}&2356
\end{array}
\tag{4.7}
\]

The equivalent expanded encoding has 41,561 deduplicated individual
activation rows, 675 lower matching rows, and 673 upper matching rows.  With
the other rows unchanged, it has 43,917 constraints.  The 13 seams whose two
activation literals are the same account for the difference between 41,561
and twice 20,787.

## 5. What the 14/12 maximum test proves

For a fixed cut `C`, let `nu(C)` be the maximum size of a binary `y` satisfying
(4.3)--(4.5), and let

\[
 D(C)=L(C)+U(C)-99.
 \tag{5.1}
\]

Every exact completion of `C` satisfies

\[
 \nu(C)\ge D(C).
 \tag{5.2}
\]

The exact Pareto audit proves `D(C)>=14` throughout the retain branch and
`D(C)>=12` throughout the delete branch.  Therefore a proved branch-wide
upper bound

\[
 \max_C\nu(C)<14
 \quad\text{or}\quad
 \max_C\nu(C)<12
 \tag{5.3}
\]

is an exact no-go for a current-motif-hitting resident candidate in the
corresponding branch.

The converse does not hold.  A maximum at or above the uniform threshold
may occur at a cut whose own demand is larger.  Thus `max nu >= 14/12` does
not by itself certify even capacity feasibility of the maximizing cut.

For a mathematically validated partial hint, either impose (1.1), or
maximize the cut-dependent margin

\[
 \nu(C)-D(C).
 \tag{5.4}
\]

A returned cut with nonnegative verified margin passes this necessary
relaxation and may be used as a cut-side hint.  It is still not a factor or a
q1 completion.  A negative incumbent is not a no-go: only a proved optimal
negative margin, a proved upper bound below the uniform threshold, or proven
infeasibility of (1.1)--(4.5) supplies a certificate.  `FEASIBLE`, `UNKNOWN`,
or a time-limited incumbent below threshold does not.

## 6. Full-add rows and indicator semantics

In a full model with binary addition variables `z_a`, the following global
row is valid without products:

\[
 \boxed{
 \sum_{a\in A_{\rm both}}z_a
 \ge
 \sum_{e\in S}(w_L(e)+w_U(e))x_e-99.
 }
 \tag{6.1}
\]

The genuinely simultaneous repairs form a subset of `A_both`; counting
other selected `A_both` seams only enlarges the left side.  Define

\[
 E_L^+=\{a:\ a\text{ is off-source loopless and }
                 \operatorname{lower}(a)\text{ is source-unique}\},
 \tag{6.2}
\]

and define `E_U^+` analogously for the upper palette.  Then

\[
 z(E_L^+)\ge L(C),
 \qquad
 z(E_U^+)\ge U(C)
 \tag{6.3}
\]

are valid aggregate q1 rows.  For a stronger full-model witness formulation,
retain `y` and add

\[
 y_a\le z_a.
 \tag{6.4}
\]

Together with the gated colour rows and (1.1), this says that the selected
additions contain a sufficiently large representative matching.  No lower
AND inequality is needed because `y` is existentially selected.

If exact product indicators are useful, introduce separate variables

\[
 t_a=
 z_a\land x_{p_L(\operatorname{lower}(a))}
 \land x_{p_U(\operatorname{upper}(a))}.
 \tag{6.5}
\]

These require the usual full AND linearization, with the repeated cut literal
deduplicated when the two unique source providers coincide.  The exact
`t` variables must not inherit the colour-matching rows (4.3)--(4.4): an
actual completion may contain several qualifying additions with the same
lost colour.  The matching rows belong to the existential representative
selector `y`.  Exact `t` variables can instead support the valid count

\[
 \sum_a t_a\ge L(C)+U(C)-99.
 \tag{6.6}
\]

## 7. LP-dual Benders cuts

The binary `y` system is an extended formulation, not an `x`-only Benders
cut.  For a fixed cut, relax `y` to be nonnegative real and maximize
`sum y` under (4.3)--(4.5).  Its dual has nonnegative variables

\[
 \alpha_c,\quad\beta_d,\quad\gamma_v
 \tag{7.1}
\]

where `c` ranges over source-unique lower colours, `d` ranges over
source-unique upper colours, and `v` ranges over quotient nodes.  They
satisfy

\[
 \alpha_{\operatorname{lower}(a)}
 +\beta_{\operatorname{upper}(a)}
 +\gamma_{u(a)}
 +\gamma_{v(a)}
 \ge1
 \qquad(a\in A_{\rm both}).
 \tag{7.2}
\]

Here `u(a),v(a)` are the two quotient endpoints of `a`.  Every fixed set of
dual-feasible coefficients gives the following valid inequality for the
`x`-projection of true completions:

\[
\boxed{
 \sum_{e\in S}(w_L(e)+w_U(e))x_e-99
 \le
 \sum_c\alpha_c x_{p_L(c)}
 +\sum_d\beta_d x_{p_U(d)}
 +\sum_v\gamma_v\sum_{e\in S:\,e\ni v}x_e.
}
\tag{7.3}
\]

If the optimal LP upper bound at an incumbent cut is smaller than its
demand, an optimal dual solution supplies a separating LP-capacity Benders
cut, equivalently a weighted generalized-Hall cut, of the form (7.3).

The four-resource binary packing problem need not be integral.  Therefore
an integer `y` failure for which the LP passes does not automatically yield
an exact certificate from the LP dual.  Such a failure requires the binary
extended formulation, a logic-based Benders/no-good cut, or a separately
proved combinatorial Hall inequality.

## 8. Logical boundary

The result assumes:

- the frozen 858-edge source and exact radius-99 cut scope;
- loopless quotient source and addition seams;
- exactly 99 additions;
- both-q1 coverage; and
- exact nodewise degree restoration.

If quotient loops are admitted, all endpoint degrees must use incidence
multiplicity two.  If non-equivariant edits or another seam universe are
admitted, the scope and census must be rebuilt.

Feasibility of (4.2)--(4.5) and (1.1) proves none of the following:

- extension of `y` to a 99-edge endpoint-restoring factor;
- coverage of every remaining or newly lost q1 row;
- connectivity or unit voltage; or
- dynamic top/complement-top residence.

It is only a necessary cut-side capacity relaxation.

## 9. Dedicated solver-free artifacts

The dedicated census/theorem replay is:

```text
scratch/audit_k16_r99_cut_double_capacity_relaxation_20260729.py
SHA-256 a1260befc97839c814033782f3c2c8444618286a619d113cbeadb57dc76dac9f

scratch/k16_r99_cut_double_capacity_relaxation_20260729.audit.json
SHA-256 659dd23c41b1911167471ec92ba010ab98cab9d7051c54f23124da3dd4cd70aa
```

The audit reconstructs the catalogue and every stated row census without
calling SAT, CP-SAT, ILP, or a remote solver.  Its status is `PASS`.

The corresponding model builder/optional solver is:

```text
scratch/solve_k16_r99_cut_double_capacity_relaxation_20260729.py
SHA-256 936b5274aec0884448c31f35d3f403d1cdf40a57d5e0d1bd68639c832abb1ece
```

This note certifies the formulation and solver-free audit only.  It records
no build artifact, objective value, feasible cut, optimality claim,
infeasibility claim, or other CP-SAT result.

The corrected independent unique-loss Pareto program used for the 113/111
diagonals is:

```text
scratch/audit_k16_r99_unique_provider_pareto_20260729.py
SHA-256 558901cdc213a11b78f8616877a56e7a52d9019e0f59294656a39ab5362e854d
```

It enforces `required_edge_ids`, including the delete-branch requirement in
component 5.  The earlier omission does not alter the exact frontiers or the
113/111 diagonal bounds, but the corrected scope is the one used here.
