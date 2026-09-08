# Finite cross-cell gadgets: exact Farkas witness and floor-covariance obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Audited conclusion

This note independently audits and strengthens
`MATH_OBSTRUCTION_FINITE_CROSS_CELL_GADGET_BLOCK_PROFILE_DUAL_20260726.md`.

The obstruction is valid with the exact quantifiers needed for the proposed
finite-gadget route.  A gadget may contain arbitrarily many transverse
status-cell decompositions, overlapping literal target cylinders, all three
big/cross/small quartet shores, and an arbitrary joint choice common to both
signs and every protected depth.  If one tensor copy of the gadget is
supported on a fixed number \(b\) of physical coordinates and different
copies have disjoint coordinate supports, then at

\[
                         q=A\sqrt m+O(1),\qquad A>0,
\tag{0.1}
\]

there is a nonnegative target weight which violates the exact multiple-choice
Farkas inequality by \(\Omega_{A,b}(W)\).  The same witness also gives the
outcome-wise floor-energy bound

\[
                         Q_q^-\ge \Omega_{A,b}(W),
 \qquad                    Q_q^+\ge \Omega_{A,b}(W).
\tag{0.2}
\]

Thus neither negative covariance nor integral semigroup saturation can
repair an independent tensor power of a fixed finite gadget.

There is one necessary scope qualification.  A *finite number of global
resolutions* need not have bounded coordinate-support components.  Two
perfect matchings can already have a connected union on all \(2m\)
coordinates.  The proved obstruction is therefore a bounded-carrier tensor
obstruction, not a no-go for every finite catalogue of global transverse
frames.

## 1. Exact configuration model

Fix \(b\ge2\), first with \(b\mid2m\), and partition the physical coordinate
set into

\[
                  n={2m\over b}
\tag{1.1}
\]

labelled blocks \(C_1,\ldots,C_n\), each of size \(b\).  Let

\[
                  \mathcal O=\binom{[2m]}m
\tag{1.2}
\]

be the middle-owner layer.  Partition \(\mathcal O\) into owner regions
\(\mathcal O_i\).  Region \(i\) has an arbitrary finite option menu
\(\mathcal L_i\).  One option may simultaneously choose several status-cell
resolutions, packet shores, affine compiler phases, and all-depth
chronology.  We assume only:

1. every physical Johnson axis used by every option has both endpoints in
   one block \(C_j\); and
2. at each signed depth \(q\), every owner emits one target occurrence.

For the lower sign put

\[
 a_{i\ell}^{-,q}(T)
 =\#\{X\in\mathcal O_i:\text{ option }\ell
                    \text{ emits }T\text{ from }X\}.
\tag{1.3}
\]

No target injectivity is assumed in (1.3).  The option columns are allowed
to couple both signs and all depths inseparably.

An independent tensor power of a fixed \(b\)-coordinate cross-cell gadget
has exactly this form: take the tensor supports as the blocks \(C_j\).  All
transversality and cylinder overlap *inside* a copy are retained.

If \(b\nmid2m\), combine the fewer than \(b\) residual coordinates with
one tensor block and condition on their finitely many local states.  The
remaining \(b\)-blocks still have cardinality \(2m/b+O(1)\); every
coefficient index below changes by \(O_b(1)\), and summing the finitely many
residual sectors restores the same \(\Omega_{A,b}(W)\) conclusion.

An owner leave \(L=o(W)\) also causes no difficulty.  Removing owners can
only decrease the left side of the one-sided Farkas inequality, while the
profile window below has \(\Theta_{A,b}(W)\) targets.  In the floor statement
one replaces \(W\) by \(W-L\); its Gaussian-depth floor is still at least
one.

## 2. The invariant survives every internal transverse resolution

For \(Y\subseteq[2m]\), define

\[
 F_b(Y)=\#\{j:C_j\subseteq Y\}.
\tag{2.1}
\]

### Lemma 2.1

If \(T\) is a lower target emitted from the middle owner \(X\), then

\[
                             F_b(T)=F_b(X).
\tag{2.2}
\]

For the upper sign, the number of empty blocks is the same in the upper
target and its middle owner.

#### Proof

Every Johnson move exchanges two coordinates in one \(C_j\), so local rank
inside every block is constant along the owner window.  A block full in
\(X\) contains both endpoints of every internal coordinate pair and hence
has no available Johnson axis; it remains full in the lower intersection.
A block not full in \(X\) is not full in any owner in the window, and its
intersection cannot be full.  This proves (2.2).  Complementation changes
full lower blocks into empty upper blocks and proves the second assertion.
\(\square\)

The lemma does not use a fixed matching, a fixed status cell, or disjoint
literal target cylinders.  Thus cross-cell overlap inside one tensor copy
does not weaken it.

## 3. Exact profile counts and the uniform ratio

Put

\[
 h_b(z)=(1+z)^b-z^b,\qquad D_b=2^b-1.
\tag{3.1}
\]

Let \(X_{m,k}\) be the number of middle owners with \(F_b=k\), and let
\(T_{m-q,k}\) be the number of lower rank-\((m-q)\) targets with \(F_b=k\).
Then exactly

\[
\begin{aligned}
 X_{m,k}&=\binom nk[z^{m-bk}]h_b(z)^{n-k},\\
 T_{m-q,k}&=\binom nk[z^{m-q-bk}]h_b(z)^{n-k}.
\end{aligned}
\tag{3.2}
\]

Normalize the coefficients of \(h_b\) by the span-one variable

\[
 \Pr(J=j)={\binom bj\over D_b},\qquad0\le j<b.
\tag{3.3}
\]

Write

\[
 \mu_b={b(2^{b-1}-1)\over D_b},\qquad
 \sigma_b^2=\operatorname {Var}J>0,
\tag{3.4}
\]

and

\[
 a_b=b-\mu_b={b2^{b-1}\over D_b},\qquad
 v_b={2(1-2^{-b})\over b}\sigma_b^2>0.
\tag{3.5}
\]

Let \(q=A\sqrt m+O(1)\), and uniformly for \(y\) in a fixed compact set put

\[
 k={m\over b2^{b-1}}+y\sqrt m+O(1).
\tag{3.6}
\]

Then the lattice local central limit theorem gives the uniform identity

\[
 \boxed{
 \log{X_{m,k}\over T_{m-q,k}}
 ={A^2+2Aa_by\over2v_b}+o(1).}
\tag{3.7}
\]

#### Proof of (3.7)

Put \(d=n-k\).  The common binomial factor in (3.2) cancels.  The source
coefficient index has deviation

\[
\begin{aligned}
 m-bk-\mu_bd
 &=m-\mu_bn-(b-\mu_b)k\\
 &={m\over D_b}-a_bk
 =-a_by\sqrt m+O(1)
\end{aligned}
\tag{3.8}
\]

from \(\mu_bd\), while the target deviation is

\[
                         -(A+a_by)\sqrt m+O(1).
\tag{3.9}
\]

Moreover

\[
                         \sigma_b^2d=v_bm+O(\sqrt m).
\tag{3.10}
\]

The span-one local limit estimate for the two coefficients in (3.2)
therefore yields

\[
 -{a_b^2y^2\over2v_b}
 +{(A+a_by)^2\over2v_b}+o(1),
\]

which is (3.7).  Uniformity on compact \(y\)-sets is the standard uniform
form of the same lattice estimate. \(\square\)

At

\[
                         y_*=-{A\over a_b},
\tag{3.11}
\]

the limiting ratio is

\[
                         \exp\!\left(-{A^2\over2v_b}\right)<1.
\tag{3.12}
\]

Consequently there are constants \(c_{A,b}>0\) and
\(\rho_{A,b}<1\) such that, for the integer window

\[
 \mathcal K_m=\left\{k:
 \left|k-{m\over b2^{b-1}}+{A\over a_b}\sqrt m\right|
       \le c_{A,b}\sqrt m\right\},
\tag{3.13}
\]

we have, uniformly in \(k\in\mathcal K_m\),

\[
                         X_{m,k}\le
                 (\rho_{A,b}+o(1))T_{m-q,k}.
\tag{3.14}
\]

## 4. The witness has positive Gaussian mass

It remains important that (3.13) is not a thin exceptional profile.  This
can be checked without any unproved saddle assertion.

For one uniformly random block subset let \(R\) be its rank and let
\(I=\mathbf1_{\{R=b\}}\).  At density one half, with \(p_b=2^{-b}\),

\[
\begin{aligned}
 \operatorname {Var}R&={b\over4},\\
 \operatorname {Var}I&=p_b(1-p_b),\\
 \operatorname {Cov}(R,I)&={bp_b\over2}.
\end{aligned}
\tag{4.1}
\]

Hence the conditional variance per block is

\[
 \tau_b^2=p_b(1-p_b)-bp_b^2
          =p_b\bigl(1-(b+1)p_b\bigr)>0.
\tag{4.2}
\]

The support points \((0,0),(1,0),(b,1)\) generate the full integer lattice,
so the bivariate lattice local central limit theorem applies.  Conditioning
the total rank to be \(m-q\), it gives

\[
\begin{aligned}
 \mathbb E(F_b\mid |T|=m-q)
   &=n2^{-b}-2^{1-b}q+O(1),\\
 \operatorname {Var}(F_b\mid |T|=m-q)
   &=n\tau_b^2+O(\sqrt m)=\Theta_b(m).
\end{aligned}
\tag{4.3}
\]

The centre in (3.13) differs from the conditional mean in (4.3) by only
\(O_{A,b}(\sqrt m)\), and the window has width
\(\Theta_{A,b}(\sqrt m)\).  Therefore

\[
 \sum_{k\in\mathcal K_m}T_{m-q,k}
       =(\eta_{A,b}+o(1))N_q,
 \qquad \eta_{A,b}>0,
\tag{4.4}
\]

where \(N_q=\binom{2m}{m-q}\).  Since

\[
                         {N_q\over W}\longrightarrow e^{-A^2},
\tag{4.5}
\]

equations (3.14) and (4.4) give a deficit of order \(W\).

## 5. Exact Farkas failure

Let

\[
 \mathcal Y_m=\{T\in\tbinom{[2m]}{m-q}:F_b(T)\in\mathcal K_m\},
 \qquad w=\mathbf1_{\mathcal Y_m}.
\tag{5.1}
\]

For every owner region \(i\) and every option \(\ell\), Lemma 2.1 gives

\[
 \langle w,a_{i\ell}^{-,q}\rangle
 \le\#\{X\in\mathcal O_i:F_b(X)\in\mathcal K_m\}.
\tag{5.2}
\]

Taking the maximum separately in every region and then summing is harmless,
because the right side of (5.2) is independent of \(\ell\).  Since the
\(\mathcal O_i\) partition the middle layer,

\[
 \sum_i\max_{\ell\in\mathcal L_i}
       \langle w,a_{i\ell}^{-,q}\rangle
 \le \sum_{k\in\mathcal K_m}X_{m,k}
 \le(\rho_{A,b}+o(1))|\mathcal Y_m|.
\tag{5.3}
\]

For the one-sided target demand \(b_T=1\),

\[
                         \langle w,b\rangle=|\mathcal Y_m|.
\tag{5.4}
\]

Thus (5.3) violates

\[
 \sum_i\max_\ell\langle w,a_{i\ell}\rangle
                         \ge\langle w,b\rangle
\tag{5.5}
\]

by

\[
 (1-\rho_{A,b}+o(1))|\mathcal Y_m|
                         =\Omega_{A,b}(W).
\tag{5.6}
\]

This is a separation from the complete fractional Minkowski sum of the
option polytopes, before any semigroup issue arises.  If the notation
\(w>0\) is intended to require strict positivity in every coordinate, add
\(\varepsilon_m>0\) to all zero coordinates, with
\(\varepsilon_m H=o(1)\).  Both support functions change by \(o(W)\), so
the linear gap (5.6) remains.

## 6. Exact floor-energy consequence and both signs

Let \(Z(T)\) be the integral lower load of any selected outcome and put

\[
                         c_q=\left\lfloor{W\over N_q}\right\rfloor.
\tag{6.1}
\]

At Gaussian depth, \(c_q\ge1\).  Equation (5.3), now applied to the
selected columns, gives

\[
 \sum_{T\in\mathcal Y_m}Z(T)
        \le(\rho_{A,b}+o(1))|\mathcal Y_m|.
\tag{6.2}
\]

Therefore

\[
 \sum_{T\in\mathcal Y_m}(c_q-Z(T))_+
 \ge(c_q-\rho_{A,b}-o(1))|\mathcal Y_m|.
\tag{6.3}
\]

For every integer \(z\ge0\),

\[
 (z-c_q)(z-c_q-1)\ge2(c_q-z)_+.
\tag{6.4}
\]

Hence the exact floor-corrected energy satisfies

\[
\begin{aligned}
 Q_q^-(Z)
 &=\sum_T(Z(T)-c_q)(Z(T)-c_q-1)\\
 &\ge2(c_q-\rho_{A,b}-o(1))|\mathcal Y_m|
   =\Omega_{A,b}(W).
\end{aligned}
\tag{6.5}
\]

Thus no probability law on the integral options can have expected
floor-energy \(o(W)\): every outcome already has the lower bound (6.5).
This is stronger than failure to find a particular negative covariance.

Complementing owners and targets preserves every internal Johnson axis and
turns full lower blocks into empty upper blocks.  The identical proof gives

\[
                         Q_q^+(Z)=\Omega_{A,b}(W).
\tag{6.6}
\]

The two witnesses may be placed in the common all-sign, all-depth weight
array one at a time.  Consequently the simultaneous requirement fails on
each sign separately at the single protected depth \(q=A\sqrt m+O(1)\).

## 7. Consequence for the two-sign quartet transports

The big/cross/small shore gadget may move lower profiles on
\(13/32+o(1)\) owner density and upper profiles on the same density.  If a
fixed finite number of quartets is assembled into one transverse gadget,
all of its shore axes nevertheless remain inside the union of those
quartets.  Regard that whole union as one \(b\)-block.  Lemma 2.1 then
applies unchanged.

Thus overlapping literal cylinders and the exact two-sign local transports
do not repair an independent tensor of this finite object.  They can only
be useful as generators in a construction whose selected axes join
different tensor copies on a growing scale.

## 8. Sharp proved boundary

The no-go is controlled by the coordinate union graph, not by the number of
options.  Let \(\Gamma\) have the physical coordinates as vertices and all
Johnson pairs appearing in any option as edges.  If the atlas is a tensor
of copies of one fixed gadget, every component of \(\Gamma\) lies in a
fixed \(b\)-set, and Sections 1--7 apply.

By contrast, define two perfect matchings on the cyclically ordered
coordinates by

\[
\begin{aligned}
 M_0&=\{\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\},\\
 M_1&=\{\{2,3\},\{4,5\},\ldots,\{2m,1\}\}.
\end{aligned}
\tag{8.1}
\]

Their union is a single \(2m\)-cycle.  Hence a catalogue with only two
global transverse frames can already have an unbounded support component;
finiteness of the catalogue alone supplies no block-profile witness.

The exact surviving constructive statement is therefore:

> build a common all-depth selection system whose available-axis union has
> growing components, whose *selected* Gaussian-depth windows cross every
> bounded terminal partition on \(\Omega_A(W)\) occurrences, and then prove
> the weighted Farkas inequalities and semigroup absorption on that growing
> system.

No coefficient-one conclusion follows here.  What is closed is the route
of tensoring a fixed bounded-carrier cross-cell gadget, even if that gadget
has perfect local negative covariance.
