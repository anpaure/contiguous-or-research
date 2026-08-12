# Finite Apéry shoulders: critical-chain monotonicity and an exact layer-cake scalar

**Date:** 2026-08-04
**Status:** unconditional pure-mathematical theorem and sharp reduction.  It
rewrites the complete formal-cyclic-versus-physical Bellman correction as
one exact derivative-prefix scalar.  It gives a sufficient monotonicity
criterion under which a positive formal clock survives physical
availability, and proves that critical-chain monotonicity alone cannot imply
that criterion.  It does not prove universal Bellman positivity or
`nu(k) <= B(k) + O(1)`.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel

\[
 K(x)=
 \begin{cases}
  1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
  -e^{-(A+x)^2},&x>A.
 \end{cases}
\tag{0.1}
\]

The two formulas and their first derivatives agree at `A`, so `K` is
continuously differentiable on `[0,infinity)`.

Let

\[
 c_0=0,\qquad c_1,\ldots,c_n\ge0
\tag{0.2}
\]

be a finite internally superadditive table, and let

\[
 V_0=0,\qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j})
\tag{0.3}
\]

be its physical Bellman clock.  Define

\[
 \lambda=\max_{1\le j\le n}{c_j\over j}>0,
 \qquad
 S=\{j:c_j=j\lambda\},
 \qquad
 g=\gcd(S).
\tag{0.4}
\]

For `d_j=c_j-j lambda`, let `beta_r`, `0<=r<g`, be the maximum reduced
weight of a residue walk from zero to `r` in the usual Apéry digraph.  The
formal cyclic clock is

\[
 W_m=m\lambda+\beta_{m\bmod g}.
\tag{0.5}
\]

The all-slot Apéry theorem gives

\[
 0\le V_m\le W_m,
 \qquad
 V_m=W_m\quad(m\ge T),
 \qquad T=n(n-1).
\tag{0.6}
\]

Hence the full discrepancy is the finite shoulder

\[
 \mathcal H(V,W)
 =\sum_{m\ge0}\bigl(K(V_m)-K(W_m)\bigr).
\tag{0.7}
\]

## 1. Exact min-plus deficit dynamics

Define the Apéry deficit

\[
 \Delta_m=W_m-V_m\ge0
\tag{1.1}
\]

and, for `1<=j<=min(m,n)`, the literal edge slack

\[
 \sigma_{m,j}=W_m-W_{m-j}-c_j.
\tag{1.2}
\]

### Theorem 1.1 (supersolution and exact slack recursion)

Every edge slack is nonnegative, and

\[
 \boxed{
 \Delta_m=
 \min_{1\le j\le\min(m,n)}
 \bigl(\sigma_{m,j}+\Delta_{m-j}\bigr).}
\tag{1.3}
\]

#### Proof

Write `r=m mod g`.  An attaining reduced walk for
`beta_(m-j mod g)`, followed by the original denomination `j`, is a
reduced walk to `r` of weight

\[
 \beta_{(m-j)\bmod g}+d_j.
\]

Maximality of `beta_r` therefore gives

\[
 \beta_r\ge\beta_{(m-j)\bmod g}+d_j.
\]

After restoring `lambda` times the capacities, this is exactly

\[
 W_m\ge W_{m-j}+c_j,
\]

so `sigma_(m,j)>=0`.  Substituting
`V_(m-j)=W_(m-j)-Delta_(m-j)` into the Bellman recurrence gives

\[
 \begin{aligned}
 V_m
 &=\max_j\bigl(c_j+W_{m-j}-\Delta_{m-j}\bigr)\\
 &=W_m-\min_j\bigl(\sigma_{m,j}+\Delta_{m-j}\bigr),
 \end{aligned}
\]

which is (1.3). \(\square\)

Equation (1.3) is the exact coupling omitted by a bare comparison
`V<=W`: the shoulder deficits are not free variables.

## 2. Critical denominations split the shoulder into monotone chains

Fix any critical denomination `h in S` and put

\[
                         L=c_h=h\lambda.
\tag{2.1}
\]

Because `g` divides every member of `S`, it divides `h`; hence

\[
                         W_{m+h}=W_m+L.
\tag{2.2}
\]

Moreover `sigma_(m+h,h)=0`.  Applying (1.3) with the denomination `h`
gives

\[
                         \boxed{\Delta_{m+h}\le\Delta_m.}
\tag{2.3}
\]

For `0<=r<h`, define

\[
 x_r=W_r,
 \qquad
 \delta_{r,q}=\Delta_{r+qh}\quad(q\ge0).
\tag{2.4}
\]

Then

\[
 \boxed{
 \begin{aligned}
 W_{r+qh}&=x_r+qL,\\
 V_{r+qh}&=x_r+qL-\delta_{r,q},\\
 \delta_{r,0}&\ge\delta_{r,1}\ge\cdots\ge0,
 \end{aligned}}
\tag{2.5}
\]

and every deficit chain is eventually zero by (0.6).  In particular the
physical points on one critical chain have gaps

\[
 V_{r+(q+1)h}-V_{r+qh}
 =L+\delta_{r,q}-\delta_{r,q+1}\ge L.
\tag{2.6}
\]

Thus physical availability transforms every formal arithmetic chain by
moving a finite initial prefix to the left and weakly increasing its
successive gaps.  This is the exact monotone-majorization content supplied
by a critical denomination.

## 3. Layer-cake formula for the complete finite shoulder

For `N>=0`, define the derivative-prefix train

\[
 J_{L,N}(y)=\sum_{q=0}^{N-1}K'(y+qL),
 \qquad J_{L,0}=0.
\tag{3.1}
\]

For `0<=t<delta_(r,0)`, put

\[
 N_r(t)=\#\{q\ge0:\delta_{r,q}>t\}.
\tag{3.2}
\]

Since each deficit chain is nonincreasing and eventually zero, its active
indices at height `t` are exactly

\[
                         0,1,\ldots,N_r(t)-1.
\tag{3.3}
\]

### Theorem 3.1 (exact critical-chain layer cake)

The finite shoulder has the exact representation

\[
 \boxed{
 \mathcal H(V,W)
 =-\sum_{r=0}^{h-1}
   \int_0^{\delta_{r,0}}
   J_{L,N_r(t)}(x_r-t)\,dt.}
\tag{3.4}
\]

#### Proof

For `x>=delta>=0`, the fundamental theorem of calculus gives

\[
 K(x-\delta)-K(x)
 =-\int_0^\delta K'(x-t)\,dt.
\tag{3.5}
\]

Partition the indices `m` uniquely as `m=r+qh`, use (2.5), and apply
(3.5):

\[
 \mathcal H(V,W)
 =-\sum_{r=0}^{h-1}\sum_{q\ge0}
   \int_0^{\delta_{r,q}}
   K'(x_r+qL-t)\,dt.
\tag{3.6}
\]

Only finitely many deficits are nonzero, so the sums and integrals may be
reordered without a convergence argument.  At fixed `r,t`, (3.3) turns
the active summand into

\[
 \sum_{q=0}^{N_r(t)-1}K'(x_r-t+qL)
 =J_{L,N_r(t)}(x_r-t).
\]

This proves (3.4). \(\square\)

## 4. The exact scalar that a finite shoulder must pay

Define the adverse shoulder debt and compensating shoulder credit by

\[
 \begin{aligned}
 \mathfrak D_h(V\mid W)
 &=\sum_{r=0}^{h-1}\int_0^{\delta_{r,0}}
   \bigl[J_{L,N_r(t)}(x_r-t)\bigr]_+\,dt,\\
 \mathfrak C_h(V\mid W)
 &=\sum_{r=0}^{h-1}\int_0^{\delta_{r,0}}
   \bigl[-J_{L,N_r(t)}(x_r-t)\bigr]_+\,dt.
 \end{aligned}
\tag{4.1}
\]

Then Theorem 3.1 says

\[
 \boxed{
 \mathcal H(V,W)=\mathfrak C_h(V\mid W)-\mathfrak D_h(V\mid W).}
\tag{4.2}
\]

Equivalently, the **net shoulder debt**

\[
 \boxed{
 \mathfrak S_h(V\mid W)
 :=\mathfrak D_h(V\mid W)-\mathfrak C_h(V\mid W)
 =-\mathcal H(V,W)}
\tag{4.3}
\]

is the exact scalar lost when the formal clock is replaced by the physical
clock:

\[
 \boxed{\Phi(V)=\Phi(W)-\mathfrak S_h(V\mid W).}
\tag{4.4}
\]

Consequently, whenever `Phi(W)>0`,

\[
 \boxed{
 \Phi(V)\le0
 \quad\Longleftrightarrow\quad
 \mathfrak S_h(V\mid W)\ge\Phi(W)}
\tag{4.5}
\]

or, without subtracting the favorable terms,

\[
 \boxed{
 \Phi(V)\le0
 \quad\Longrightarrow\quad
 \mathfrak D_h(V\mid W)
 \ge\Phi(W)+\mathfrak C_h(V\mid W)
 \ge\Phi(W).}
\tag{4.6}
\]

This is stronger than counting adverse cells: it prices their exact
location, depth, and prefix multiplicity.

### Corollary 4.1 (prefix-slope transport criterion)

If

\[
 J_{L,N_r(t)}(x_r-t)\le0
\tag{4.7}
\]

for every `r` and almost every `0<t<delta_(r,0)`, then

\[
 \mathcal H(V,W)\ge0,
 \qquad
 \Phi(V)\ge\Phi(W).
\tag{4.8}
\]

Thus a positive formal cyclic clock automatically survives any physical
shoulder whose active derivative prefixes all have nonpositive slope.

More generally, no termwise sign theorem is needed: the exact necessary
and sufficient target is simply

\[
                         \mathfrak S_h(V\mid W)<\Phi(W).
\tag{4.9}
\]

## 5. Why critical-chain monotonicity alone cannot close the shoulder

The prefix-slope hypothesis (4.7) does not follow solely from (2.5).
Indeed, suppose a formal chain begins at some

\[
                         x>\zeta,
\]

where `zeta` is the unique global minimizer of `K`.  Consider the abstract
deficit profile

\[
 \delta_0=x-\zeta,
 \qquad
 \delta_q=0\quad(q\ge1).
\tag{5.1}
\]

It is nonnegative, nonincreasing, eventually zero, and it weakly expands
the formal arithmetic gaps exactly as in (2.6).  Nevertheless its shoulder
contribution is

\[
 K(\zeta)-K(x)<0.
\tag{5.2}
\]

This example is deliberately **not** asserted to arise from a Bellman
table.  It proves the sharp logical boundary: no argument using only
`V<=W`, eventual equality, and critical-chain monotonicity can establish
`mathcal H>=0`.  A complete proof must exploit the full cross-denomination
slack recursion (1.3), or an equivalent constraint strong enough to bound
the net scalar (4.3).

## 6. Consequence for the all-grid Apéry programme

The uniform cyclic clock, the short-first affine clock, and the
exact-first-carry one-defect long-wrap clock are now positive in their
proved scopes.  Therefore any original physical clock lying over one of
those positive formal branches can fail positivity only by satisfying the
exact threshold

\[
 \boxed{
 \mathfrak S_h(V\mid W)\ge\Phi(W)>0.}
\tag{6.1}
\]

For those branches, the finite-shoulder problem is no longer an
unstructured comparison of two finite arrays.  It is the following scalar
question:

> Show that every deficit solution of the exact min-plus system (1.3)
> arising from a first-crossing table satisfies
> `mathfrak S_h(V|W)<Phi(W)`.

The theorem does not solve that inequality.  It removes all free shoulder
degrees of freedom except the min-plus slack system and identifies the
exact quantity that system must control.  Endpoint-critical clocks,
threshold-overshoot or delayed-carry clocks outside the cited formal
positivity theorems, and multidefect formal clocks remain separate gates.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| physical Bellman clock, maximum-density Apéry reduction, conductor | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| cyclic Apéry table and exact formal clock | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| all-grid minimal-counterexample trichotomy and finite shoulder | `MATH_THEOREM_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_20260804.md` | `8ed0ae35fe1a3bbd52824bca67240155868ed1e3a268b1f582aba944e081b4b2` |
| one-defect classification and affine exclusion | `MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md` | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| all-period exact-first-carry long-wrap closure | `MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md` | `24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd` |
