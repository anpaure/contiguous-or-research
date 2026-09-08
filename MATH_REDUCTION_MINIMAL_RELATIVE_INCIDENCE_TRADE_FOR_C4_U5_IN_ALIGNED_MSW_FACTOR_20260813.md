# The minimal relative incidence trade needed to install the seam `C_4-U_5`

**Date:** 2026-08-13  
**Status:** exact colored-edge formulation, exact lower bound through four
changed facets in the first nondegenerate finite case, and a five-facet
middle-incidence witness; a uniform symbolic lift preserving upper current
remains open

## 1. Why the correct object is a colored edge factor

Put `n=2m+1` and let `F_m` be the complete first-aligned MSW packet factor.
Every rank-`m` facet `L` occurs exactly once and lies between two consecutive
rank-`m+1` owner windows.  Write

\[
                         e_0(L)=\{A_L,B_L\}.       \tag{1.1}
\]

Thus `F_m` is equivalently a colored 2-factor on the rank-`m+1` owners:

* every facet `L` is one color used exactly once;
* every owner has degree two;
* the edge of color `L` must join two owners containing `L`.

For the first compound seam put

\[
 C=C_4,qquad U=U_5,qquad L_0=C\cap U.            \tag{1.2}
\]

The desired edge is

\[
                         e_1(L_0)=\{C,U\}.         \tag{1.3}
\]

The previous coexistence obstruction proves that `(1.3)` is not the edge
of color `L_0` in `F_m`.

### Proposition 1.1 (exact relative-trade equations)

Let `\mathcal A` be a finite set of facets containing `L_0`.  A relative
middle-incidence trade supported on `\mathcal A` is precisely a choice

\[
 e_1(L)=\{X_L,Y_L\},\qquad L\subset X_L,Y_L,
 \qquad X_L\ne Y_L,\qquad L\in\mathcal A,        \tag{1.4}
\]

such that

\[
 \sum_{L\in\mathcal A}\bigl(
  \mathbf1_{X_L=V}+\mathbf1_{Y_L=V}\bigr)
 =
 \sum_{L\in\mathcal A}\bigl(
  \mathbf1_{A_L=V}+\mathbf1_{B_L=V}\bigr)         \tag{1.5}
\]

for every owner `V`, and `(1.3)` holds.

It preserves the complete immediate-upper current if and only if additionally

\[
 \sum_{L\in\mathcal A}\mathbf1_{X_L\cup Y_L=T}
 =
 \sum_{L\in\mathcal A}\mathbf1_{A_L\cup B_L=T}   \tag{1.6}
\]

for every rank-`m+2` set `T`.

#### Proof

Each facet remains used once because its color is retained.  Equation
`(1.5)` is exactly degree preservation at every owner.  Conversely these
two properties are precisely the owner/lower exact factor equations.
The upper value of a colored edge is the union of its endpoints, giving
`(1.6)`. \(\square\)

This formulation removes row-decomposition noise.  Fusion and chronology
are later questions; the first gate is the finite integer system
`(1.3)--(1.6)`.

## 2. A three-facet search is finite and exact

Let `X_C` be either old factor neighbour of `C`, other than across `L_0`,
and similarly choose `X_U` for `U`.  A three-facet trade can only use

\[
 L_0,qquad C\cap X_C,qquad U\cap X_U.             \tag{2.1}
\]

Once `(1.3)` is imposed, owner-degree balance leaves only finitely many
pairings of the four displaced endpoints.  Testing whether the two
remaining colors contain the endpoints gives a literal constant-size
decision procedure.  The optional upper-current test is then the equality
of three union-value multisets.

The H100 standard-library/CP-SAT verifier executes exactly this decision.
For `m=8,9,10` it finds no three-facet trade, even before upper current is
required.

Likewise, enumeration of all universal inverse-triple two-row trades whose
negative rows lie in `F_m`, while freezing every selected portal row, finds
no trade installing `C_4-U_5` at `m=8,9,10`.

These are finite diagnostics, not yet an asymptotic no-go theorem.

## 3. The first exact finite minimum

At `m=7`, freeze the six positive rows used by the selected internal portal
bank.  Solve `(1.3)--(1.5)` over all rank-`m` facets.

### Theorem 3.1 (finite minimum at `m=7`)

There is no relative middle-incidence trade changing at most four facet
colors.  There is one changing exactly five.

One five-facet witness is the following.  The common labels `0,6,7,8,9,14`
are suppressed where convenient:

\[
\begin{array}{c|c|c}
L&\text{old extra pair}&\text{new extra pair}\\ \hline
\{0,3,6,7,8,9,14\}&\{4,5\}&\{5,11\}\\
\{0,4,6,7,8,9,14\}&\{5,12\}&\{3,12\}\\
\{0,5,6,7,8,9,14\}&\{3,12\}&\{3,4\}\\
\{0,6,7,8,9,11,14\}&\{3,10\}&\{10,12\}\\
\{0,6,7,8,9,12,14\}&\{10,11\}&\{5,10\}.
                                                        \tag{3.1}
\end{array}
\]

Here “extra pair” means the two labels separately added to the displayed
facet to obtain its two endpoint owners.

#### Proof

Direct substitution in `(3.1)` shows that the last new edge is
`C_4-U_5`.  Counting every owner endpoint in the two columns proves
`(1.5)`.  None of the five colors belongs to a frozen selected portal row.

For the lower bound, the CP-SAT model has one Boolean variable for every
legal owner pair on every facet, freezes the selected portal colors,
imposes one selected pair per facet, all owner degree equations `(1.5)`,
and `(1.3)`.  Adding

\[
 \sum_L\mathbf1_{e_1(L)\ne e_0(L)}\le t
\tag{3.2}
\]

returns certified
`INFEASIBLE` at `t=3,4` and `OPTIMAL` with five changes at `t=5`.
The frozen JSON certificates and independent replay script bind this finite
claim. \(\square\)

The trade `(3.1)` is important structurally: the missing seam does not
require an extensive factor reconstruction at the middle ranks.  A small
colored circuit exists.  But `(3.1)` is tied to `m=7`; simply adjoining a
common tail does not reproduce the first-aligned packet edges for larger
`m`.

## 4. Upper current is the remaining sharp local obstruction

The five-facet witness `(3.1)` does not satisfy `(1.6)`.  More generally:

* the finite search proves no upper-exact trade with at most
  `5,6,8,12` changed facets at `m=7`;
* the unrestricted `m=7` upper-exact feasibility search remains
  computationally unresolved in the allotted run;
* at the smaller `m=6` diagnostic, an upper-exact solution exists with
  27 changed facets, although optimality was not proved;
* no universal two-row inverse-triple trade installs the seam in the tested
  `m=8,9,10` factors.

Therefore the first remaining local theorem is not merely another
middle-rank alternating cycle.  It is one of:

1. a uniform bounded-support colored trade satisfying `(1.3)--(1.6)`;
2. a middle-incidence trade plus a separate bounded upper-current absorber;
3. a proof that upper coverage inequalities, rather than exact upper
   tickets, allow the five-facet-type trade without loss.

Only after this local current problem is solved does one re-audit row
chronology, residence, and fusion.

## 5. Reproducibility and scope

The exact search files are:

* `scratch/search_minimal_colored_edge_trade_compound_seam_20260813.py`;
* `scratch/cpsat_relative_incidence_trade_compound_seam_20260813.py`;
* `scratch/search_relative_inverse_trade_for_compound_seam_20260813.py`.

All SAT and enumeration ran on `h100`.  The local Mac was used only for
lightweight proof and file inspection.

Frozen H100 results include:

* `scratch/h100_results/cpsat_relative_compound_seam_m7_middle_cert_c3_20260813.json`;
* `scratch/h100_results/cpsat_relative_compound_seam_m7_middle_cert_c4_20260813.json`;
* `scratch/h100_results/cpsat_relative_compound_seam_m7_middle_cert_c5_20260813.json`;
* `scratch/h100_results/cpsat_relative_compound_seam_m6_upper_exact_20260813.json`;
* `scratch/h100_results/relative_inverse_trade_compound_seam_m8_m10_20260813.json`.

This note does not assert a uniform lift of `(3.1)`, nor does it convert a
colored factor trade into a legal protected cyclic rethread.  It isolates
the smallest exact algebraic gate and shows that the middle-incidence part
is locally solvable.
