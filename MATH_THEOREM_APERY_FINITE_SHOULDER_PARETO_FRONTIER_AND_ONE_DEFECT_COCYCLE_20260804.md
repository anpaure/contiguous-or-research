# Finite Apéry shoulders: exact Pareto frontiers and the one-defect cocycles

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and exact reduction.  It
uses the complete min-plus Bellman recursion, rather than only monotonicity
along one critical denomination.  It proves an exact shortest-path equation
for every active prefix length, an exact recursive decomposition of every
derivative train, and explicit cocycle formulae for the uniform, short-first
affine, and long-wrap one-defect formal clocks.  It does **not** prove that
the resulting shoulder scalar is smaller than the positive formal margin.

Let

\[
 c_0=0,\qquad c_1,\ldots,c_n\ge0
\]

be internally superadditive, let `V` be its physical Bellman clock, and let

\[
 \lambda=\max_{1\le j\le n}{c_j\over j},\qquad
 W_m=m\lambda+\beta_{m\bmod g}
\]

be the formal maximum-density Apéry clock.  Put

\[
 \Delta_m=W_m-V_m\ge0.
\tag{0.1}
\]

The cited finite-shoulder theorem proves that `Delta_m=0` for all
sufficiently large `m` and that, for every original denomination,

\[
 \Delta_m=\min_{1\le j\le\min(m,n)}
 \bigl(\sigma_{m,j}+\Delta_{m-j}\bigr),
 \qquad
 \sigma_{m,j}=W_m-W_{m-j}-c_j\ge0.
\tag{0.2}
\]

The purpose of this note is to solve the combinatorial content of (0.2)
exactly at every shoulder height.

## 1. Seed deficits and the formal cocycle

For `1<=j<=n`, define the seed deficit

\[
 e_j:=W_j-c_j.
\tag{1.1}
\]

Also set `e_0=0`.

Internal superadditivity gives `V_j=c_j` on the displayed table, so

\[
                         e_j=\Delta_j\ge0.
\tag{1.2}
\]

For nonnegative `a,b`, define the formal superadditivity cocycle

\[
 \kappa_W(a,b):=W_{a+b}-W_a-W_b\ge0.
\tag{1.3}
\]

### Theorem 1.1 (seed-cocycle factorization)

For every legal Bellman edge,

\[
 \boxed{\sigma_{m,j}=e_j+\kappa_W(m-j,j).}
\tag{1.4}
\]

More generally, let

\[
 \mathbf j=(j_1,\ldots,j_p),\qquad
 1\le j_i\le n,\qquad \sum_i j_i=m
\]

be an exact-fill configuration, and put

\[
 \begin{aligned}
 \omega_W(\mathbf j)&:=W_m-\sum_iW_{j_i}\ge0,\\
 E_W(\mathbf j)&:=\sum_i e_{j_i}+\omega_W(\mathbf j).
 \end{aligned}
\tag{1.5}
\]

Then

\[
 \boxed{
 \Delta_m=\min_{\mathbf j:\,\sum j_i=m}E_W(\mathbf j).}
\tag{1.6}
\]

#### Proof

Equation (1.4) is the identity

\[
 W_m-W_{m-j}-c_j
 =(W_j-c_j)+(W_m-W_{m-j}-W_j).
\]

The cocycle is nonnegative because the formal clock is superadditive.
For a complete configuration,

\[
 W_m-\sum_i c_{j_i}
 =\sum_i(W_{j_i}-c_{j_i})+
   \left(W_m-\sum_iW_{j_i}\right)
 =E_W(\mathbf j).
\]

Taking the minimum of the left side is the same as subtracting the
maximum configuration value from `W_m`; this is `W_m-V_m=Delta_m`.
\(\square\)

Thus the shoulder is a finite constrained shortest-path problem.  The
numbers `e_j` are the literal costs of the original generators; the
cocycle is the extra cost of composing their formal states.

## 2. Exact cross-denomination recursion for the active prefix lengths

Fix an **original** critical denomination `H`, so

\[
 c_H=W_H=H\lambda=:L.
\tag{2.1}
\]

Every original critical denomination is divisible by `g`, hence

\[
 W_{m+H}=W_m+L.
\tag{2.2}
\]

For `0<=r<H`, put

\[
 x_r=W_r,\qquad \delta_{r,q}=\Delta_{r+qH}\quad(q\ge0).
\tag{2.3}
\]

The critical edge gives

\[
 \delta_{r,0}\ge\delta_{r,1}\ge\cdots\ge0,
\tag{2.4}
\]

and the sequence is eventually zero.

For a denomination `j`, define

\[
 r_j=[r-j]_H\in\{0,\ldots,H-1\},\qquad
 \ell_{rj}={j-r+r_j\over H}.
\tag{2.5}
\]

Then `ell_(rj)` is a nonnegative integer and

\[
 r+qH-j=r_j+(q-\ell_{rj})H.
\tag{2.6}
\]

The edge is physically available exactly when `q>=ell_(rj)`.  Its slack
does not depend on `q`; write

\[
 \begin{aligned}
 s_{rj}
 &:=e_j+\kappa_W(r_j+(q-\ell_{rj})H,j)\\
 &=x_r-x_{r_j}+\ell_{rj}L-c_j\ge0.
 \end{aligned}
\tag{2.7}
\]

The first line is independent of the displayed admissible `q`, because
adding `H` to the first cocycle argument adds `L` to both formal terms and
therefore cancels.

### Theorem 2.1 (critical-coordinate min-plus equation)

For every `r,q` with `r+qH>=1`,

\[
 \boxed{
 \delta_{r,q}=
 \min_{\substack{1\le j\le n\\q\ge\ell_{rj}}}
 \bigl(s_{rj}+\delta_{r_j,q-\ell_{rj}}\bigr).}
\tag{2.8}
\]

For real `t`, extend the active-prefix length by

\[
 N_r(t)=
 \begin{cases}
  +\infty,&t<0,\\
  \#\{q\ge0:\delta_{r,q}>t\},&t\ge0.
 \end{cases}
\tag{2.9}
\]

At nonnegative height `N_0(t)=0`, because every multiple of `H` is
filled exactly by critical generators.

For every `1<=r<H` and `t>=0`, one has the exact tropical Bellman equation

\[
 \boxed{
 N_r(t)=\min_{1\le j\le n}
 \left(\ell_{rj}+N_{r_j}(t-s_{rj})\right).}
\tag{2.10}
\]

Equivalently,

\[
 \boxed{
 N_r(t)=\min\left\{q\ge0:
 \begin{array}{l}
 \text{there is an exact-fill configuration }\mathbf j\\[-2pt]
 \text{of }r+qH\text{ with }E_W(\mathbf j)\le t
 \end{array}\right\}.}
\tag{2.11}
\]

#### Proof

Substitute (2.6)--(2.7) into the full slack recursion (0.2).  This gives
(2.8), including precisely the availability condition `q>=ell_(rj)`.

Fix one `j` and one height `t`.  Before `q=ell_(rj)` the edge is absent,
so it imposes no restriction.  From that index onward, the term supplied
by this edge exceeds `t` exactly when

\[
 \delta_{r_j,q-\ell_{rj}}>t-s_{rj}.
\]

If `t<s_(rj)`, this is automatic and our convention makes the permitted
prefix infinite.  If `t>=s_(rj)`, its permitted indices are exactly the
first

\[
 \ell_{rj}+N_{r_j}(t-s_{rj})
\]

indices.  Equation (2.8) exceeds `t` precisely when **every** Bellman edge
exceeds `t`.  Intersecting these prefixes takes their minimum and proves
(2.10).  The residue-zero base state is separate because `Delta_0=0` is
not produced by a Bellman edge.

Finally, monotonicity (2.4) gives

\[
 N_r(t)=\min\{q:\delta_{r,q}\le t\}.
\]

Insert the configuration formula (1.6) to obtain (2.11). \(\square\)

The old monotonicity theorem said only that each active set is a prefix.
Equation (2.10) says exactly how all those prefixes are coupled across
different residues and different heights.

### Corollary 2.2 (attaining-edge decomposition of a derivative train)

Let

\[
 J_{L,N}(y)=\sum_{q=0}^{N-1}K'(y+qL).
\]

If `j` attains the minimum in (2.10), then necessarily `t>=s_(rj)` and

\[
 \boxed{
 \begin{aligned}
 J_{L,N_r(t)}(x_r-t)
 ={}&J_{L,\ell_{rj}}(x_r-t)\\
 &+J_{L,N_{r_j}(t-s_{rj})}
 \bigl(x_{r_j}-(t-s_{rj})+c_j\bigr).
 \end{aligned}}
\tag{2.12}
\]

#### Proof

An attaining edge gives

\[
 N_r(t)=\ell_{rj}+N_{r_j}(t-s_{rj}).
\]

The right side is finite, so `t>=s_(rj)`.  Equation (2.7) rearranges to

\[
 x_r-t+\ell_{rj}L
 =x_{r_j}-(t-s_{rj})+c_j.
\]

Split the derivative train after its first `ell_(rj)` terms. \(\square\)

Thus an active derivative train is never free: after a finite boundary
prefix it is a literal right translate, by one available value `c_j`, of
an active train at another residue and a lower slack budget.

## 3. Exact Pareto-frontier form of the shoulder scalar

Since `H<=n`, for `0<=r<H` one has

\[
 \delta_{r,0}=\Delta_r=e_r.
\tag{3.1}
\]

The critical-chain layer-cake theorem and (2.11) therefore give the exact
identity

\[
 \boxed{
 \mathfrak S_H(V\mid W)
 =\sum_{r=1}^{H-1}\int_0^{e_r}
 J_{L,N_r(t)}(x_r-t)\,dt,}
\tag{3.2}
\]

where every `N_r(t)` is the least critical-period lift admitting a
configuration of Pareto cost at most `t`, as in (2.11).  There are no
remaining free shoulder variables.  In particular,

\[
 \Phi(V)>0
 \quad\Longleftrightarrow\quad
 \sum_{r=1}^{H-1}\int_0^{e_r}
 J_{L,N_r(t)}(x_r-t)\,dt<\Phi(W).
\tag{3.3}
\]

Only finitely many frontiers occur: `Delta_m=0` beyond the Apéry
conductor, so each `N_r` is a finite step function with values bounded by
that conductor.

## 4. The three simple formal clocks

The Pareto cost (1.5) becomes especially rigid on the three formal
geometries whose relevant pure-periodic branches are already known to be
positive in the cited scopes.

### 4.1 Uniform arithmetic clock

If

\[
                         W_m=\alpha m,
\tag{4.1}
\]

then

\[
 \boxed{
 \kappa_W(a,b)=0,\qquad
 \omega_W(\mathbf j)=0,\qquad
 E_W(\mathbf j)=\sum_i e_{j_i}.}
\tag{4.2}
\]

Hence

\[
 \boxed{
 N_r(t)=\min\left\{q:\exists\mathbf j,
 \sum_i j_i=r+qH,\quad \sum_i e_{j_i}\le t\right\},
 \qquad x_r=\alpha r.}
\tag{4.3}
\]

Thus a uniform formal shoulder is exactly a bicriteria coin problem:
ordinary capacity is minimized in units of `H`, while the second resource
is the additive seed deficit.

### 4.2 Short-first affine clock

Let

\[
 W_m=\alpha m-\beta\left\lceil{m\over g}\right\rceil,
 \qquad \beta>0.
\tag{4.4}
\]

For residues `u,v in {0,...,g-1}`, put

\[
 \epsilon_-(u,v)=
 \begin{cases}
 1,&u>0,\ v>0,\ u+v\le g,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{4.5}
\]

Then

\[
 \boxed{
 \kappa_W(a,b)=\beta\epsilon_-(\bar a,\bar b).}
\tag{4.6}
\]

For a configuration of total capacity `m`, define

\[
 C_-(\mathbf j)
 :=\sum_i\left\lceil{j_i\over g}\right\rceil
   -\left\lceil{m\over g}\right\rceil
 \in\mathbb Z_{\ge0}.
\tag{4.7}
\]

Then

\[
 \boxed{
 \omega_W(\mathbf j)=\beta C_-(\mathbf j),\qquad
 E_W(\mathbf j)=\sum_i e_{j_i}+\beta C_-(\mathbf j).}
\tag{4.8}
\]

Consequently (2.11) is the explicit frontier

\[
 \boxed{
 N_r(t)=\min\left\{q:\exists\mathbf j,
 \sum_i j_i=r+qH,\quad
 \sum_i e_{j_i}+\beta C_-(\mathbf j)\le t\right\},}
\tag{4.9}
\]

with

\[
 x_r=\alpha r-\beta\left\lceil{r\over g}\right\rceil.
\tag{4.10}
\]

Writing `j_i=q_i g+rho_i`, `0<=rho_i<g`, and letting `p_+` be the number
of positive residues, one has `C_-=0` precisely when either `p_+=0` or

\[
                         \sum_i\rho_i>(p_+-1)g.
\tag{4.11}
\]

Thus every frontier below height `beta` uses only this zero-coalescence
face.

### 4.3 Long-wrap one-defect clock

Let

\[
 W_m=am+\eta\left\lfloor{m\over g}\right\rfloor,
 \qquad \eta>0.
\tag{4.12}
\]

Then

\[
 \boxed{
 \kappa_W(a,b)
 =\eta\,\mathbf1_{\{\bar a+\bar b\ge g\}}.}
\tag{4.13}
\]

For a configuration of total capacity `m`, define

\[
 C_+(\mathbf j)
 :=\left\lfloor{m\over g}\right\rfloor
   -\sum_i\left\lfloor{j_i\over g}\right\rfloor
 \in\mathbb Z_{\ge0}.
\tag{4.14}
\]

Then

\[
 \boxed{
 \omega_W(\mathbf j)=\eta C_+(\mathbf j),\qquad
 E_W(\mathbf j)=\sum_i e_{j_i}+\eta C_+(\mathbf j).}
\tag{4.15}
\]

Hence

\[
 \boxed{
 N_r(t)=\min\left\{q:\exists\mathbf j,
 \sum_i j_i=r+qH,\quad
 \sum_i e_{j_i}+\eta C_+(\mathbf j)\le t\right\},}
\tag{4.16}
\]

with

\[
 x_r=ar+\eta\left\lfloor{r\over g}\right\rfloor.
\tag{4.17}
\]

In the same residue notation, `C_+=0` precisely when

\[
                         \sum_i\rho_i<g.
\tag{4.18}
\]

Thus every frontier below height `eta` is carry-free.

More generally, (4.8) and (4.15) give the exact budget bounds

\[
 C_-(\mathbf j)\le\left\lfloor{t\over\beta}\right\rfloor,
 \qquad
 C_+(\mathbf j)\le\left\lfloor{t\over\eta}\right\rfloor
\tag{4.19}
\]

for every configuration that can terminate an active prefix at height
`t`.

#### Proof of the cocycle formulae

The uniform identities are immediate.  For (4.4), linear terms cancel and

\[
 \kappa_W(a,b)=\beta\left(
 \left\lceil{a\over g}\right\rceil+
 \left\lceil{b\over g}\right\rceil-
 \left\lceil{a+b\over g}\right\rceil\right).
\]

The parenthesis is zero or one, and its residue classification is exactly
(4.5).  Summing over all parts proves (4.7)--(4.8).  If the positive
residues have total `R`, then

\[
 C_-=p_+-\left\lceil{R\over g}\right\rceil,
\]

which proves (4.11).

For (4.12), linear terms again cancel and

\[
 \kappa_W(a,b)=\eta\left(
 \left\lfloor{a+b\over g}\right\rfloor-
 \left\lfloor{a\over g}\right\rfloor-
 \left\lfloor{b\over g}\right\rfloor\right).
\]

This is (4.13).  For a full configuration it equals
`eta floor(R/g)`, proving (4.14)--(4.15) and (4.18).  The budget bounds
follow because all seed deficits are nonnegative. \(\square\)

The two one-defect clocks therefore have opposite but completely explicit
residue obstructions: the affine clock charges a failed coalescence of
positive residues, while the long-wrap clock charges a genuine residue
carry.

## 5. Cross-denomination defect spreading

The frontier equation also rules out an isolated high shoulder defect.
Suppose that the formal cocycle obeys

\[
                         0\le\kappa_W(a,b)\le\theta
\tag{5.1}
\]

for all `a,b`.  In the three cases above one may take respectively

\[
                         \theta=0,\qquad\beta,\qquad\eta.
\tag{5.2}
\]

### Theorem 5.1 (no isolated defect above one cocycle quantum)

For every `i,j>=0`,

\[
 \boxed{
 \Delta_{i+j}\le\Delta_i+\Delta_j+\kappa_W(i,j)
 \le\Delta_i+\Delta_j+\theta.}
\tag{5.3}
\]

Consequently, for every `m>=2`,

\[
 \boxed{
 (m-1)\Delta_m
 \le2\sum_{i=1}^{m-1}\Delta_i+\Omega_m,}
 \qquad
 \Omega_m:=\sum_{i=1}^{m-1}\kappa_W(i,m-i)
 =(m-1)W_m-2\sum_{i=1}^{m-1}W_i,
\tag{5.4}
\]

and therefore

\[
 \boxed{
 (m-1)(\Delta_m-\theta)_+
 \le2\sum_{i=1}^{m-1}\Delta_i.}
\tag{5.5}
\]

For `u>=0`, let

\[
 \begin{aligned}
 A(u)&=\#\{m\ge1:\Delta_m>u\},\\
 A_{<m}(u)&=\#\{1\le i<m:\Delta_i>u\}.
 \end{aligned}
\tag{5.6}
\]

If `Delta_m>t+theta`, then

\[
 \boxed{m-1\le2A_{<m}(t/2)\le2A(t/2).}
\tag{5.7}
\]

In particular, if `N_r(t+theta)>0`, then

\[
 \boxed{
 r+\bigl(N_r(t+\theta)-1\bigr)H
 \le2A(t/2)+1.}
\tag{5.8}
\]

#### Proof

Concatenate optimal physical configurations of capacities `i` and `j`.
This gives `V_(i+j)>=V_i+V_j`.  Subtract from the formal identity defining
`kappa_W(i,j)` to obtain (5.3).

Apply (5.3) to every split `m=i+(m-i)` and sum over
`1<=i<=m-1`:

\[
 (m-1)\Delta_m
 \le2\sum_{i=1}^{m-1}\Delta_i+
 \sum_{i=1}^{m-1}\kappa_W(i,m-i).
\]

The cocycle sum telescopes to the displayed formula for `Omega_m`, proving
(5.4).  Since `Omega_m<=(m-1)theta`, (5.5) follows.

If `Delta_m>t+theta`, then (5.3) shows that for every split at least one
of `Delta_i,Delta_(m-i)` exceeds `t/2`.  Hence the two sets

\[
 \{i:1\le i<m,\ \Delta_i>t/2\},
 \qquad
 \{m-i:1\le i<m,\ \Delta_i>t/2\}
\]

cover all `m-1` split indices and have total cardinality at most
`2A_(<m)(t/2)`.  This proves (5.7).  The largest active member of the
`r`-chain at height `t+theta` is

\[
 r+(N_r(t+\theta)-1)H,
\]

so (5.8) follows. \(\square\)

For a uniform formal clock, `theta=0`: every adverse high-index defect at
height `t` forces at least `(m-1)/2` earlier active indices at half that
height.  For either one-defect clock, the same assertion holds above its
single cocycle quantum.  This is a genuine cross-denomination restriction
that is absent from critical-chain monotonicity.

## 6. Exact remaining scalar gate

Equations (2.10), (2.12), (3.2), and (4.2)/(4.8)/(4.15) remove the free
geometry from the uniform, affine, and long-wrap shoulders:

* every active length is a least-cost Pareto frontier;
* every active train recursively splits into a finite boundary train and
  a translated predecessor train;
* in the one-defect cases, every residue coalescence/carry has one fixed
  price; and
* an isolated high defect is impossible above that price.

These statements do not by themselves sign (3.2).  The obstruction is
analytic and real: `K'` is negative before the unique minimizer of `K` and
positive after it, and translation by `c_j` in (2.12) does not have one
global sign.  A complete finite-shoulder proof must now establish, for the
corresponding Pareto frontiers,

\[
 \boxed{
 \sum_{r=1}^{H-1}\int_0^{e_r}
 J_{L,N_r(t)}(x_r-t)\,dt<\Phi(W).}
\tag{6.1}
\]

The theorem proves that no proposed counterexample may choose the
functions `N_r` independently.  Any future analytic charging argument can
and should use the exact recursion (2.10), or equivalently the explicit
uniform/one-defect path budgets of Section 4.

## 7. Frozen dependencies

| role | file |
|---|---|
| physical Bellman clock and displayed-table identity | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` |
| exact formal cyclic Apéry clock | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` |
| critical-chain layer cake and shoulder scalar | `MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md` |
| one-defect classification | `MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md` |
