# Rayleigh Apéry defects: a periodic queue and an exact zeroth-mode reserve

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reduction.  After first-minimum saturation
and least-critical normalization, the formal Apéry period is at most the
Rayleigh minimum.  Its residue displacements form a cyclic subadditive
metric.  A displacement of size `Delta` therefore has average at least
`Delta/2`, not merely one exceptional residue.  In counting coordinates
this is an exact nonnegative periodic queue with a positive zeroth Fourier
mode.  The finite availability shoulder is a second nonnegative queue, and
adverse shoulder debt forces a dimension-free amount of its area.  The
remaining analytic obstruction is one centered periodized covariance; no
Boolean capacity reserve or all-price positivity is asserted.

## 0. Setup

Let

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Write `zeta` for its
unique global minimum and

\[
 M=K(0)=1-2e^{-\pi/4}>0.
\tag{0.1}
\]

Let

\[
 c_0=0,c_1,\ldots,c_N
\]

be a **nonnegative** saturated first-`zeta` internally superadditive
Bellman table:

\[
 c_j<\zeta\quad(1\le j<N),
 \qquad \zeta\le c_N<2\zeta.
\tag{0.2}
\]

Let `V` be its physical Bellman clock.  Put

\[
 \lambda=\max_{1\le j\le N}{c_j\over j},
 \qquad
 h=\min\operatorname*{argmax}_{1\le j\le N}{c_j\over j}.
\tag{0.3}
\]

Let `S` be the complete critical set, `g=gcd(S)`, and let

\[
 U_m=\lambda m+\beta_{m\bmod g}
\tag{0.4}
\]

be the formal maximum-density Apéry clock.  Thus `beta_0=0`, every
`beta_r<=0`,

\[
 V_m\le U_m,
\tag{0.5}
\]

and equality holds after a finite conductor.

Define

\[
 P=g\lambda,
 \qquad
 s_r=\lambda r+\beta_r,
 \qquad
 d_r=-\beta_r=\lambda r-s_r
 \quad(0\le r<g),
\tag{0.6}
\]

and

\[
 \Delta=\max_{0\le r<g}d_r.
\tag{0.7}
\]

The quantities `d_r` are the formal residue displacements.  The finite
availability deficits are

\[
 \delta_m=U_m-V_m\ge0.
\tag{0.8}
\]

Finally put

\[
 e_m=\lambda m-V_m=d_{m\bmod g}+\delta_m.
\tag{0.9}
\]

## 1. The formal period lies below the first-minimum threshold

### Theorem 1.1 (least-critical period cap)

With the normalization above,

\[
 \boxed{0<P\le\zeta.}
\tag{1.1}
\]

More precisely, if `h<N`, then `P<zeta`; if `h=N`, then

\[
 c_N=\zeta,\qquad g=N,\qquad P=\zeta.
\tag{1.2}
\]

### Proof

If `h<N`, then `g<=h`, so

\[
 P=g\lambda\le h\lambda=c_h<\zeta
\]

by first crossing.

Suppose `h=N`.  Saturation says

\[
 c_N=\max\{\zeta,P_N\},
\]

where `P_N` is the maximum value of a proper lower-index partition of
`N`.  If `P_N>=zeta`, choose an attaining partition
`N=j_1+...+j_t`.  Since `N` is critical,

\[
 N\lambda=c_N=P_N=\sum_i c_{j_i}
 \le\sum_i j_i\lambda=N\lambda.
\]

Equality of the sum forces `c_(j_i)=j_i lambda` for every part.  At least
one `j_i<N`, contradicting that `N` is the least critical index.  Hence
`P_N<zeta` and saturation gives `c_N=zeta`.

There is no critical index below `N`, so the complete critical set is
`{N}`.  Thus `g=N` and `P=N lambda=c_N=zeta`.  This proves (1.1)--(1.2).
\(\square\)

This cap is stronger than the raw saturated endpoint aperture
`c_N<2zeta`: the maximum-density **period value**, which is the quantity
seen by the phase train below, never exceeds `zeta`.

## 2. A maximum cyclic displacement spreads over half the period

For every displayed denomination put

\[
 a_j=\lambda j-c_j\ge0.
\tag{2.0}
\]

The defects have an exact shortest-path meaning:

\[
 \boxed{
 e_m=\min_{j_1+\cdots+j_t=m}\sum_i a_{j_i},
 \qquad
 d_r=\min_{j_1+\cdots+j_t\equiv r\pmod g}\sum_i a_{j_i}.}
\tag{2.0a}
\]

In the second minimum the empty walk is allowed for residue zero, and
zero-cost critical steps may be inserted freely.  Indeed, subtracting the
value of any exact-fill configuration from `lambda` times its capacity
gives exactly the sum of its seed costs.  Minimizing is the Bellman
definition of `e_m`; dropping exact capacity and retaining only residue is
the Apéry definition of `d_r`.  Consequently

\[
 \delta_m=e_m-d_{m\bmod g}
\tag{2.0b}
\]

is literally the extra toll for exact finite availability over the best
residue walk.  Thus both defects below are configuration opportunity
costs, not arbitrary analytic perturbations.

The cyclic Apéry inequalities are equivalent to

\[
 d_{(r+t)\bmod g}\le d_r+d_t
 \qquad(r,t\in\mathbb Z/g\mathbb Z).
\tag{2.1}
\]

Thus `d` is a nonnegative cyclic subadditive function with `d_0=0`.

### Theorem 2.1 (cyclic half-average theorem)

Every such defect profile satisfies

\[
 \boxed{
 {1\over g}\sum_{r=0}^{g-1}d_r\ge {\Delta\over2}.}
\tag{2.2}
\]

The constant `1/2` is the exact consequence of subadditivity alone.

### Proof

Choose `a` with `d_a=Delta`.  For every residue `r`, cyclic
subadditivity gives

\[
 \Delta=d_a\le d_r+d_{a-r}.
\]

Sum over all `r`.  The map `r -> a-r` is a permutation of the cyclic
group, so

\[
 g\Delta\le
 \sum_r d_r+\sum_r d_{a-r}
 =2\sum_r d_r.
\]

Division by `2g` proves (2.2). \(\square\)

In particular, the large-displacement alternative

\[
 \Delta>\varepsilon_*\lambda
\tag{2.3}
\]

from the global Apéry stability tube implies

\[
 \boxed{
 {1\over g\lambda}\sum_r d_r>{\varepsilon_*\over2}.}
\tag{2.4}
\]

Thus a counterclock cannot hide its formal nonarithmeticity in one sparse
residue: it creates a dimension-free average phase displacement.

## 3. Counting coordinates give a literal periodic queue

For a nondecreasing clock `a=(a_m)`, define its strict counting price

\[
 F_a(x)=\#\{m\ge0:a_m<x\},\qquad x>0,
\tag{3.1}
\]

and set `F_a(0)=0`.  Gaussian endpoint null sets make the half-open
convention immaterial.  Let

\[
 L_m=\lambda m
\]

be the arithmetic clock.  Since `U_m<=L_m`,

\[
 w(x):=F_U(x)-F_L(x)\ge0.
\tag{3.2}
\]

### Theorem 3.1 (Apéry displacement queue)

The function `w` is `P`-periodic almost everywhere.  On one period,

\[
 \boxed{
 w(x)=\sum_{r=1}^{g-1}{\bf1}_{[s_r,r\lambda)}(x),
 \qquad0\le x<P,}
\tag{3.3}
\]

and hence

\[
 \boxed{
 \overline w:={1\over P}\int_0^P w(x)\,dx
 ={1\over P}\sum_{r=0}^{g-1}d_r
 \ge {\Delta\over2\lambda}.}
\tag{3.4}

### Proof

For `m=qg+r`, equations (0.4) and (0.6) give

\[
 U_m=qP+s_r,
 \qquad
 L_m=qP+r\lambda.
\]

The standard walk consisting of `r` copies of denomination one has value
`r c_1`; hence `s_r>=r c_1>=0`.  Also `s_r=r lambda-d_r<=r lambda<P`
for `0<r<g`.  Thus both points really do lie in the same half-open
`P`-block; this is where nonnegativity of the original Bellman table is
used.

Moving one counting point from `L_m` leftward to `U_m` adds exactly the
indicator of the interval between those two points.  Both endpoints lie
in the same `P`-block.  Summing inside one block gives (3.3), and every
later block is its translate by `P`.  Integrating (3.3) gives

\[
 \int_0^P w=\sum_r(r\lambda-s_r)=\sum_r d_r.
\]

Equation (3.4) now follows from Theorem 2.1 and `P=g lambda`. \(\square\)

The graph of `w` is a queue: a residue enters at its displaced point
`s_r` and exits at its arithmetic point `r lambda`.  It is nonnegative
because every Apéry point moves only to the left.

## 4. Exact phase decomposition of the formal functional

Let

\[
 \sigma(dx)=-K'(x)\,dx.
\tag{4.1}
\]

This is the signed socket-minus-job deviation measure, and

\[
 \sigma((x,\infty))=K(x),
 \qquad
 \sigma((0,\infty))=K(0)=M.
\tag{4.2}
\]

Define the periodized density

\[
 Q_P(x)=\sum_{q=0}^{\infty}-K'(qP+x),
 \qquad0<x<P.
\tag{4.3}
\]

The Gaussian tail gives absolute local convergence and

\[
 \int_0^P Q_P(x)\,dx=M.
\tag{4.4}
\]

### Theorem 4.1 (zeroth-mode reserve identity)

For every formal Apéry clock above,

\[
 \boxed{
 \Phi(U)
 =C(\lambda)+\int_0^P w(x)Q_P(x)\,dx.}
\tag{4.5}
\]

Equivalently,

\[
 \boxed{
 \Phi(U)
 =C(\lambda)+M\overline w
  +\int_0^P\bigl(w(x)-\overline w\bigr)Q_P(x)\,dx.}
\tag{4.6}
\]

Consequently, in the large-displacement branch (2.3), the zeroth mode
contributes the strict positive amount

\[
 \boxed{M\overline w>{M\varepsilon_*\over2}.}
\tag{4.7}
\]

### Proof

For every `m`, tail integration gives

\[
 K(U_m)-K(L_m)=\sigma([U_m,L_m)).
\]

Sum over `m` and use the nonnegative interval multiplicity `w`:

\[
 \Phi(U)-C(\lambda)=\int_0^\infty w(x)\,d\sigma(x).
\]

Periodicity of `w` and the Gaussian summability of `K'` turn the last
integral into the right side of (4.5).  Subtracting and adding the mean of
`w`, then using (4.4), proves (4.6).  Equation (4.7) is (3.4) and (2.3).
\(\square\)

The all-mesh arithmetic-comb theorem gives

\[
 C(\lambda)>c_*={377\over108000}.
\tag{4.8}
\]

Therefore formal-clock positivity is reduced to the centered covariance

\[
 \mathcal C_P(w)
 :=\int_0^P(w-\overline w)Q_P.
\tag{4.9}
\]

For example, the inequality

\[
 \mathcal C_P(w)\ge-M\overline w
\tag{4.10}
\]

for every Apéry queue with `P<=zeta` would imply
`Phi(U)>=C(lambda)>0`.  In the large-displacement branch it is enough to
prove the strictly weaker bound

\[
 \mathcal C_P(w)>-c_*-M\overline w.
\tag{4.11}
\]

Thus the nonarithmetic formal obstruction is no longer an unstructured
list of residues: it is one nonnegative queue with a protected positive
mean, tested against one fixed periodized density on a compact period
`P<=zeta`.

## 5. The finite shoulder is a second queue

Define

\[
 z(x)=F_V(x)-F_U(x).
\tag{5.1}
\]

Since `V_m<=U_m`, this is nonnegative, has finite support in the counting
index, and

\[
 \boxed{
 z(x)=\sum_{m\ge0}{\bf1}_{[V_m,U_m)}(x),
 \qquad
 \int_0^\infty z(x)\,dx=\sum_m\delta_m.}
\tag{5.2}
\]

Moreover

\[
 \boxed{
 \Phi(V)=\Phi(U)+\int_0^\infty z(x)\,d\sigma(x).}
\tag{5.3}
\]

Let

\[
 \mathscr S^-=
 \sum_m\bigl(K(U_m)-K(V_m)\bigr)_+
\tag{5.4}
\]

be the adverse shoulder debt used in the global stability dichotomy.

### Theorem 5.1 (debt forces literal shoulder area)

One has

\[
 \boxed{
 \mathscr S^-
 \le \lVert K'\rVert_\infty\sum_m\delta_m.}
\tag{5.5}
\]

Consequently the adverse-debt alternative

\[
 \mathscr S^-\ge {c_*\over2}
\tag{5.6}
\]

forces

\[
 \boxed{
 \int_0^\infty z(x)\,dx
 =\sum_m\delta_m
 \ge{c_*\over2\lVert K'\rVert_\infty}
 >{c_*\over2}.}
\tag{5.7}
\]

### Proof

The mean-value bound on each interval `[V_m,U_m]` gives the first
inequality in (5.5).  For `Q(x)=2x exp(-x^2)`, one has

\[
 0\le Q(x)\le\sqrt{2/e}<1.
\]

On the compact branch, `K'` is the difference of two numbers in this
interval; on the outer branch it is one such number.  Hence
`||K'||_infty<1`.  Equations (5.2), (5.5), and (5.6) give (5.7).
\(\square\)

Thus a shoulder counterclock must contain a dimension-free amount of
literal interval displacement.  This is stronger than merely counting
adverse cells, but its signed pairing in (5.3) can still be negative.

## 6. Formal and shoulder defects share one subadditive geometry

### Theorem 6.1 (total-defect spreading)

The complete defect `e_m=lambda m-V_m` is nonnegative and subadditive:

\[
 \boxed{e_{i+j}\le e_i+e_j.}
\tag{6.1}
\]

It agrees eventually with the cyclic defect `d_(m mod g)`.  For every
`m>=2`,

\[
 \boxed{
 (m-1)e_m\le2\sum_{i=1}^{m-1}e_i.}
\tag{6.2}
\]

Equivalently, if

\[
 A(t)=\#\{m\ge1:e_m>t\},
\]

then every `m` with `e_m>t` satisfies

\[
 \boxed{
 m-1\le2\#\{1\le i<m:e_i>t/2\}
 \le2A(t/2).}
\tag{6.3}
\]

### Proof

Nonnegativity follows from maximum density.  Superadditivity of `V` gives

\[
 e_{i+j}=\lambda(i+j)-V_{i+j}
 \le\lambda i+\lambda j-V_i-V_j=e_i+e_j.
\]

Eventual equality `V=U` gives eventual agreement with `d`.

Apply (6.1) to every split `m=i+(m-i)` and sum over
`1<=i<m`.  The right side counts every `e_i`, `1<=i<m`, twice, proving
(6.2).  If `e_m>t`, then for every split at least one of
`e_i,e_(m-i)` exceeds `t/2`; otherwise (6.1) would give `e_m<=t`.
The two reflected active-index sets cover all `m-1` splits, which proves
(6.3). \(\square\)

So neither a periodic displacement nor a finite shoulder can be an
isolated high-index defect.  The total geometry is one subadditive
multiscale queue.

## 7. Exact consequence and boundary

Combine the independently audited global stability tube with Theorems
2.1 and 5.1.  Every nonpositive saturated first-minimum Bellman clock must
have at least one of the following two quantitative structures:

1. a periodic Apéry queue with

   \[
   \overline w>{\varepsilon_*\over2},
   \qquad
   M\overline w>{M\varepsilon_*\over2};
   \]

2. a finite shoulder queue with

   \[
   \int z>{c_*\over2}.
   \]

Both are exact dimension-free resources in counting coordinates.  The
first has a genuinely positive zeroth-mode contribution; the second is a
literal displacement area but may be adversely located.

This theorem does **not** complete either conversion requested by the
all-price programme.  Analytic positivity still requires controlling the
centered covariance (4.9) jointly with the signed finite-shoulder pairing
(5.3).  Boolean reserve requires a further occurrence-faithful theorem
turning one of these analytic queues into actual socket capacity.  Neither
follows from queue area alone.  What is removed is the possibility that a
counterclock escapes through one exceptional Apéry residue or through an
area-free finite shoulder.

## 8. Dependencies

1. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
2. `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md`;
3. `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md`;
4. `MATH_COROLLARY_RAYLEIGH_GLOBAL_APERY_STABILITY_TUBE_20260805.md`;
5. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`.
