# Separator-amplified bottom completion by an independent transversal

**Date:** 2026-08-05  
**Method:** exact FIFO algebra, resource-load cleanup, and Haxell's
independent-transversal theorem; no computation or finite search  
**Status:** unconditional deterministic completion theorem, followed by a
precise scalar-tail input.  This removes the conditional choice of a first
bottom matching from the separator-funded construction.  It does not by
itself prove that the recursively produced owner reservoir has the stated
option-degree and resource-load tails.

## 1. Why a larger fixed separator spend is useful

Use the notation of
`MATH_THEOREM_SEPARATOR_FUNDED_SLACK_BOTTOM_TWO_STAGE_MATCHING_20260805.md`.
There are initially `H_0` punctured copies and at least `(d+1)H_0` middle
owners.  For the asymptotic estimates in Section 5 we additionally use the
coefficient-one saturation supplied by the global ledger,

\[
                  H_0=(1+o(1)){W\over d+1}.                \tag{1.1}
\]

The deterministic statements in Sections 2--4 do not need this saturation.
Discard

\[
                 s=\left\lceil {cH_0\over d}\right\rceil,
                 \qquad H=H_0-s,                             \tag{1.2}
\]

where `c` is an absolute constant to be chosen below.  After levels
`2,...,d` have been installed, the residual bottom bank has size at least

\[
                 2H+(d+1)s=(2+c+o(1))H.                    \tag{1.3}
\]

Choose disjoint banks

\[
                 B_0,B_1\subseteq A_2,
                 \qquad |B_j|=\beta_jH,                    \tag{1.4}
\]

where `beta_0,beta_1` are fixed constants and

\[
                 \beta_0+\beta_1<2+c.                     \tag{1.5}
\]

The point of allowing `c` to be a sufficiently large *fixed* constant is
that the remaining bottom problem admits a deterministic independent-
transversal solution.  No random-Sperner or all-cut theorem is needed.

## 2. The three-owner option of one task

For a retained task `i`, put

\[
                 L_i=T_2^i-\{b_2^i,b_1^i\}.                \tag{2.1}
\]

For an unordered fresh pair `{a,b}`, define

\[
\begin{aligned}
 U_0(i;a,b)&=L_i\cup\{a,b\},\\
 U_a(i;a,b)&=L_i\cup\{a,b_1^i\},\\
 U_b(i;a,b)&=L_i\cup\{b,b_1^i\}.                          \tag{2.2}
\end{aligned}
\]

Call `{a,b}` an **admissible option** when

\[
                 U_0(i;a,b)\in B_0,
                 \qquad U_a(i;a,b),U_b(i;a,b)\in B_1.      \tag{2.3}
\]

The owner `U_0` is the level-zero owner.  Either orientation of the pair
then gives a legal level-one owner: choosing `x_2=a,x_1=b` uses `U_a`, and
choosing `x_2=b,x_1=a` uses `U_b`.

Freshness makes the three owners in (2.2) distinct.  Moreover, for fixed
`i`, the owner `U_0` determines the unordered pair `{a,b}`.  Hence no two
options of one task have the same `B_0` resource.

Let `Omega_i` be the set of admissible options of task `i`.

## 3. The option conflict graph

Make a graph `J` whose vertices are all pairs `(i,omega)` with
`omega in Omega_i`.  Put no edges inside one task class.  Join options of
different tasks when they share at least one of their three owner
resources in (2.2).

For a resource `U in B_0 union B_1`, let

\[
 \ell(U)=|\{(i,\omega):U\hbox{ occurs in }\omega\}|.        \tag{3.1}
\]

If every `B_0` resource has load at most `R_0` and every `B_1` resource has
load at most `R_1`, then

\[
                 \Delta(J)\le R_0+2R_1-3.                 \tag{3.2}
\]

Indeed, one option uses one `B_0` resource and two `B_1` resources, and
every conflicting option is counted at one of those resources.

### Theorem 3.1 (deterministic bottom completion)

Suppose

\[
 \min_i|\Omega_i|\ge 2(R_0+2R_1).                          \tag{3.3}
\]

Then all retained tasks have pairwise owner-disjoint legal bottom pairs
`(T_0,T_1)`.

#### Proof

Haxell's independent-transversal theorem says that a graph of maximum
degree `Delta`, whose vertex partition has every class of size at least
`2Delta`, has an independent transversal.  Equations (3.2)--(3.3) apply it
to the partition `(Omega_i)`.  Let `omega_i={a_i,b_i}` be the selected
option of task `i`.

Independence makes all selected `U_0` resources distinct and makes the two
element sets

\[
                 \{U_a(i;\omega_i),U_b(i;\omega_i)\}       \tag{3.4}
\]

pairwise disjoint over different tasks.  Choose either endpoint in (3.4)
as `T_1^i`, and orient `{a_i,b_i}` accordingly.  The chosen `T_1` owners
are pairwise distinct.  The banks `B_0,B_1` are disjoint, so no selected
`T_0` equals a selected `T_1`.  Formula (2.2) is exactly the backward FIFO
identity, proving the assertion.  \(\square\)

This deliberately asks for pairwise disjoint *two-choice* endpoint sets.
It is stronger than the pseudoforest orientation criterion, but the fixed
separator amplification pays for that strength.

## 4. Exceptional-resource cleanup

The uniform bounds in Theorem 3.1 are not needed on the initial option
system.  Fix nominal numbers `D,R_0,R_1` satisfying

\[
                 (1-2\eta)D
                 \ge 2\bigl((1+\eta)R_0+2(1+\eta)R_1\bigr) \tag{4.1}
\]

for some fixed `eta>0`.

Declare a task low when `|Omega_i|<(1-eta)D`.  Declare a resource of type
`j` high when its load exceeds `(1+eta)R_j`.  Let `B_*` be the total number
of option--resource incidences meeting a high resource, counting all three
positions of an option.

Delete every low task.  Also delete every remaining task for which more
than `eta D` of its options touch a high resource.  The number of tasks
deleted in the second step is at most

\[
                 {B_*\over\eta D}.                         \tag{4.2}
\]

Every surviving task has at least `(1-2eta)D` options avoiding high
resources, while their resource loads are at most the thresholds in
(4.1).  Theorem 3.1 therefore gives the following exact statement.

### Corollary 4.1 (two-tail independent-transversal certificate)

The bottom band can be completed after deleting at most

\[
 |\{i:|\Omega_i|<(1-\eta)D\}|+{B_*\over\eta D}             \tag{4.3}
\]

additional tasks.

Only one-dimensional option-degree and size-biased resource-load tails
occur in (4.3).  There is no conditional matching choice and no Hall-cut
family.

## 5. Constants in the product-residual model

Write

\[
                  \theta={(d+1)H\over W}.                  \tag{5.1}
\]

The saturated regime (1.1) has `theta=1+o(1)`.  More generally, the
calculations below remain valid whenever `theta=Omega(1)`, with constants
depending on its lower bound.  The bottom-bank densities are

\[
                 p_j={\beta_j\theta+o(1)\over d+1}.        \tag{5.2}
\]

One task has `Theta(d^4)` raw fresh unordered pairs.  Requiring the one
`B_0` and two `B_1` hits in (2.3) gives

\[
                 D=\Theta(\beta_0\beta_1^2\theta^3d).     \tag{5.3}
\]

Double counting gives the natural resource-load scales

\[
                 R_0\sim {D\over\beta_0},
                 \qquad R_1\sim {2D\over\beta_1}.          \tag{5.4}
\]

Thus the asymptotic form of (4.1) is

\[
                 {1\over\beta_0}+{4\over\beta_1}< {1\over2},
                                                                    \tag{5.5}
\]

with a fixed margin to absorb `eta` and tail thresholds.  For example,
`beta_0=beta_1=20` gives left side `1/4`, leaving a factor-two reserve.
Taking any fixed `c>38` then satisfies (1.5).

Under product thinning, the lower tail for one `|Omega_i|` and the
size-biased upper tails for the loads (3.1) are `exp(-Omega(d))`.  If the
recursive occurrence process supplies the corresponding factorial-moment
bounds, (4.3) becomes

\[
                 O(H e^{-\gamma d})=o(H/d).                \tag{5.6}
\]

The deterministic theorem is independent of how those scalar tails are
proved.

## 6. Budget consequence

The preliminary loss is `cH_0/d+O(1)` copies and the cleanup loss is
`o(H_0/d)`.  Each copy consumes `d+1` owner slots and carries `O(d)` lower
payload occurrences.  Hence the unmatched owner-capacity/payload count is

\[
                 O(H_0)=O(W/d),                            \tag{6.1}
\]

with a fixed constant depending only on `c`.  This is the existing
separator scale.  In an additive-constant construction, any fixed larger
choice of `c` remains harmless **at the scalar owner-capacity level**
because one extra word position creates `Theta(W)` additional
short-interval capacity, whereas (6.1) is `o(W)`.

The physical compiler must still identify actual separator cells with the
lost named payload targets.  Equation (6.1) is neither a word-length bound
nor, by itself, that occurrence-level repair.

## 7. What this closes and what remains

Compared with the preceding separator-funded theorem, the new result
removes its only adaptive quantifier:

\[
 \text{choose a first matching preserving the second tails}.        \tag{7.1}
\]

It is replaced by the static conditions in (4.3).  Once the option-degree
and resource-load tails hold, Haxell supplies both bottom levels at once.

The remaining owner-side input is therefore only:

> **Bottom option-tail lemma.**  After the slack upper levels have been
> installed, choose the amplified residual bank split so that the admissible
> option counts and all three resource loads satisfy (4.3) with
> `o(H/d)` loss.

This is a scalar factorial-moment problem.  It is strictly weaker than the
former independent random-Sperner theorem, weaker than all-cut spread, and
does not require controlling a selected matching's exported bicycles.
