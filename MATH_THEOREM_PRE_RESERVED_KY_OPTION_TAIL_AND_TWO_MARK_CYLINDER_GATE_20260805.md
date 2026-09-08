# Pre-reserved bottom banks: the `K_y` option tail and the exact two-mark cylinder gate

**Date:** 2026-08-05  
**Method:** exact FIFO algebra, finite-population coupling, two nested
Chernoff bounds, and factorial moments; no computation or search  
**Status:** unconditional bank-reservation and one-task option-tail theorem,
followed by an exact sufficient two-mark cylinder theorem for both
size-biased resource-load tails.  The existing one-mark owner cylinder and
the lower-forest MLD theorem do not supply the two-mark hypothesis.  Thus
this closes the random-bank part of the Bottom option-tail lemma, but it does
not make the separator-amplified Haxell completion unconditional.

## 1. The separator permits both bottom banks to be reserved first

Let `H_0` be the original copy count and suppose

\[
                         W\ge (d+1)H_0.                    \tag{1.1}
\]

Fix constants `c,beta_0,beta_1>0`, put

\[
 s=\left\lceil{cH_0\over d}\right\rceil,
 \qquad H=H_0-s,                                           \tag{1.2}
\]

and, before any upper owner SDR is chosen, reserve disjoint uniformly
random owner banks

\[
 |B_0|=M_0=\lfloor\beta _0H\rfloor,
 \qquad |B_1|=M_1=\lfloor\beta _1H\rfloor.                \tag{1.3}
\]

Write `beta=beta_0+beta_1`.

### Theorem 1.1 (pre-reservation does not recreate a balanced upper level)

Immediately before upper level `j>=2` is installed, after all levels above
`j` have been installed outside the reserved banks, the available owner
shore has size at least

\[
 \bigl(j+1+c-\beta+O_c(d^{-1})\bigr)H.                    \tag{1.4}
\]

In particular, if

\[
                         2+c-\beta=\gamma>0,               \tag{1.5}
\]

then every upper level `j>=2` retains right-to-left scalar ratio at least
`1+gamma+o(1)`.

#### Proof

The `d-j` already installed upper levels occupy `(d-j)H` owners.  Hence the
available shore is at least

\[
 W-M_0-M_1-(d-j)H.                                        \tag{1.6}
\]

Since `c` is fixed,

\[
 {H_0\over H}={1\over1-c/d+O(H_0^{-1})}
              =1+{c\over d}+O_c(d^{-2}),                  \tag{1.7}
\]

and therefore

\[
 {W\over H}\ge(d+1){H_0\over H}
               =d+1+c+O_c(d^{-1}).                        \tag{1.8}
\]

Divide (1.6) by `H` and use (1.8).  The minimum over `j>=2` is attained at
`j=2`, where (1.4) equals `1+gamma+o(1)`.  \(\square\)

This corrects the apparent reservation obstruction.  Reserving two layers
without first sacrificing copies moves the balanced bottleneck to level
two.  Reserving them after (1.2), with `c>beta-2`, leaves a fixed positive
gap there.

## 2. The exact one-task graph

Fix a prospective terminal bottom state after level two.  Put

\[
 L=T_2-\{b_2,b_1\},\qquad y_0=b_1,                         \tag{2.1}
\]

and let `Y` be its fresh coordinate set, of size

\[
                         y=q-d+1=\Theta(d^2).               \tag{2.2}
\]

For `a in Y` and an unordered pair `{a,b} in binom(Y,2)`, define owner
resources

\[
 v_a=L\cup\{y_0,a\},\qquad e_{ab}=L\cup\{a,b\}.           \tag{2.3}
\]

The maps `a -> v_a` and `{a,b} -> e_ab` are injective, and their two images
are disjoint: equality would force `y_0 in {a,b}`, contrary to freshness.
Consequently the admissible options are exactly the retained edges

\[
 \Omega(L,y_0)={\{a,b\}:v_a,v_b\in B_1, e_{ab}\in B_0\}.\tag{2.4}
\]

Thus one task is literally a complete graph whose vertices have colour
`B_1` and whose edge-resources have colour `B_0`.

Put

\[
 p_j={M_j\over W},\qquad \mu_1=yp_1.                       \tag{2.5}
\]

From (1.8),

\[
 p_j={\beta_j+o(1)\over d+1+c},\qquad
 \mu_1=\Theta(d).                                         \tag{2.6}
\]

### Lemma 2.1 (fixed-count colours look independent on one `K_y`)

On any fixed set of `m` owner resources, the restriction of the uniform
fixed-size partition `(B_0,B_1,rest)` has total-variation distance

\[
                         O(m^2/W)                           \tag{2.7}
\]

from independent multinomial colours of probabilities `(p_0,p_1,1-p_0-p_1)`.

#### Proof

Expose the `m` colours in a fixed order.  At exposure `t`, each conditional
colour probability differs from its original density by at most `O(t/W)`.
Couple this draw to an independent multinomial draw with failure probability
`O(t/W)`, and sum over `t<m`.  \(\square\)

For one `K_y`, `m=y+binom(y,2)=O(d^4)`, while
`W=exp(Theta(d^2))`.  Thus (2.7) is `exp(-Theta(d^2))`, negligible compared
with every `exp(-Theta(d))` tail below.

### Theorem 2.2 (one-task option lower tail)

Fix `0<delta<1/4` and define

\[
 D_\delta=(1-\delta)p_0
       {\left\lfloor(1-\delta)\mu_1\right\rfloor\choose2}.\tag{2.8}
\]

There is `g=g(delta,beta_0,beta_1,c)>0` such that every fixed prospective
bottom state satisfies

\[
 \boxed{
 \Pr\bigl(|\Omega(L,y_0)|<D_\delta\bigr)\le e^{-gd}.}
                                                                    \tag{2.9}
\]

Moreover

\[
 D_\delta=(1-O(\delta))p_0p_1^2{y\choose2}=\Theta(d).      \tag{2.10}
\]

#### Proof

Work first in the independent multinomial model.  The number

\[
 X=|\{a:v_a\in B_1\}|                                    \tag{2.11}
\]

is `Bin(y,p_1)` of mean `mu_1`.  Hence

\[
 \Pr(X<(1-\delta)\mu_1)
       \le \exp(-\delta^2\mu_1/2)=e^{-\Omega(d)}.          \tag{2.12}
\]

Conditional on the selected vertex set, the edge-resource colours remain
independent, and

\[
                 |\Omega|\mid X\sim
                 \operatorname {Bin}\!\left({X\choose2},p_0\right).
                                                                    \tag{2.13}
\]

On the complement of (2.12), its conditional mean is at least
`p_0 binom(floor((1-delta)mu_1),2)=Theta(d)`.  A second Chernoff bound gives
probability `e^{-Omega(d)}` of falling below (2.8).  Transfer to the
fixed-size partition by Lemma 2.1.  Equation (2.10) follows from
`mu_1 -> infinity`.  \(\square\)

For the resource-load argument it is useful to remove a harmless source of
compound multiplicity.  A `B_1` vertex may be incident with several options
of one task.  This does not affect option supply, because the random graph
in (2.13) has a fixed bounded average degree.

### Lemma 2.3 (bounded-degree option pruning)

For every fixed `delta>0` there is a fixed integer

\[
             \Delta=\Delta(\delta,\beta_0,\beta_1,c)       \tag{2.14}
\]

and a deterministic rule which, from `Omega(L,y_0)`, selects a subgraph
`Omega^Delta(L,y_0)` of maximum degree at most `Delta`, such that

\[
 \Pr\left(
 |\Omega^\Delta(L,y_0)|
 <(1-O(\delta))p_0p_1^2{y\choose2}
 \right)\le e^{-g_\Delta d}.                              \tag{2.15}
\]

#### Proof

Condition on `X=s` in the central Chernoff range in (2.12).  The option
graph is `G(s,p_0)`, where `s=Theta(d)` and `p_0s` stays between two fixed
positive constants.  Let `m_Delta(G)` be the maximum number of edges in a
subgraph of maximum degree at most `Delta`.

Deleting excess incident edges at every vertex gives the deterministic
bound

\[
 m_\Delta(G)\ge e(G)-\sum_v(d_G(v)-\Delta)_+.              \tag{2.16}
\]

The degree of one vertex is binomial of bounded mean.  Choose the fixed
`Delta` so large that the expected sum on the right of (2.16) is at most
`delta/4` times `E e(G)`, uniformly over the compact range of possible
values of `p_0s`.  Hence

\[
                         \mathbb Em_\Delta(G)
       \ge(1-\delta/3)\mathbb Ee(G).                       \tag{2.17}
\]

Assign every potential edge to its lower endpoint in a fixed vertex order
and expose the resulting `s` independent edge blocks.  Replacing one block
changes only edges incident with one vertex.  A degree-`Delta` subgraph uses
at most `Delta` of those edges, so `m_Delta` changes by at most `Delta`.
McDiarmid's inequality now gives an `exp(-Omega(s))=exp(-Omega(d))`
lower tail at every fixed linear deviation from (2.17).  Combine this with
the two Chernoff bounds in Theorem 2.2 and the finite-population coupling.
Choose the lexicographically first maximum degree-`Delta` subgraph to make
the rule deterministic.  \(\square\)

From now on the option class of a task means this pruned class.  Its size is
still `(1-o_delta(1))bar D=Theta(d)`, every `B_0` resource occurs at most
once in one task class, and every `B_1` resource occurs at most `Delta`
times in one task class.

The theorem is pointwise in the prospective state.  Consequently, for any
deterministic weighted family of prospective states, independent of the
bank draw, the expected bad weight is at most `e^{-gd}` times its total
weight.  It does not assert that an upper SDR selected *after seeing the
banks* samples those states without bias; that quantifier is handled below
by an explicit marked-cylinder hypothesis.

## 3. The two exact load environments

The resource loads depend on how the upper SDR chooses its marked terminal
states.  A prospective state can be encoded by

\[
                         \alpha=(T,b_2,b_1),                \tag{3.1}
\]

where `T` is a rank-`r` level-two owner and `b_2,b_1` are ordered distinct
members of `T`.  Let `X_alpha` indicate that this marked state is selected.
Selected states have distinct first coordinates `T`.

Put

\[
 \vartheta={ (1+\epsilon)H\over W(r)_2},\qquad \epsilon=o(1).\tag{3.2}
\]

The exact probabilistic input needed below is the following bank-conditioned
two-mark cylinder:

\[
 \boxed{
 \mathbb E\!\left[\prod_{a=1}^mX_{\alpha_a}\mid B_0,B_1\right]
 \le\vartheta^m}                                           \tag{C2}
\]

for every compatible collection of marked states with distinct owners.
Only values `m=O(d)` are needed.

We now compute exactly the deterministic bank statistics to which (C2)
is applied.  Put

\[
                         q_0=k-r.                           \tag{3.3}
\]

### Type zero

Fix `U in B_0`.  For `z notin U`, put

\[
 S_z(U)=|\{a\in U:U-a+z\in B_1\}|.                        \tag{3.4}

The number of marked prospective incidences whose `B_0` resource is `U`
and whose two endpoint resources lie in `B_1` is exactly

\[
 \boxed{
 N_0(U)=(q_0-1)\sum_{z\notin U}{S_z(U)\choose2}.}          \tag{3.5}

Indeed, choose `b_1=z`, choose the two elements `{a,b}=U-L`, and then
choose `b_2` in the `q_0-1` points outside `U union {z}`.  The two endpoint
owners are `U-b+z` and `U-a+z`.

Conditioned on `U in B_0`, its mean is

\[
 \bar N_0=(1+o(1))q_0(q_0-1){r\choose2}p_1^2.              \tag{3.6}

### Type one

Fix `V in B_1`.  For `z notin V`, put

\[
 A_z(V)=|\{a\in V:V-a+z\in B_0\}|,
 \qquad
 C_z(V)=|\{a\in V:V-a+z\in B_1\}|.                       \tag{3.7}

The number of marked prospective option incidences using `V` as one
endpoint and having the other two resources in the correct banks is
exactly

\[
 \boxed{
 N_1(V)=(q_0-1)\sum_{z\notin V}A_z(V)C_z(V).}              \tag{3.8}

To see this, choose the fresh other endpoint label `z`, the deleted mark
`b_1=a` counted by `A_z`, the replaced owner element counted by `C_z`, and
then `b_2` in `q_0-1` ways.  The two counts in (3.7) are disjoint because
the banks are disjoint, so their product never uses the same element twice.
Its conditional mean is

\[
 \bar N_1=(1+o(1))q_0(q_0-1)r(r-1)p_0p_1.                 \tag{3.9}

Define the natural load means

\[
 \rho_j=\vartheta\bar N_j.                                \tag{3.10}

Then

\[
 \rho_0=(1+o(1)){H\over W}{q_0(q_0-1)p_1^2\over2},
 \qquad
 \rho_1=(1+o(1)){H\over W}q_0(q_0-1)p_0p_1,              \tag{3.11}
\]

and both are `Theta(d)`.  If

\[
 \bar D=p_0p_1^2{y\choose2},                              \tag{3.12}
\]

then, up to `1+o(1)` factors,

\[
                         \rho_0={\bar D\over\beta_0},
 \qquad                  \rho_1={2\bar D\over\beta_1}.   \tag{3.13}

These are exactly the load scales asserted by double counting in the
separator-amplified theorem.

## 4. Uniform banks have exponentially small environment tails

We use one elementary quadratic-block estimate.

### Lemma 4.1 (quadratic multinomial blocks)

Let `g,n=Theta(d^2)`.  Independently in each of `g` blocks, colour `n`
points with probabilities `Theta(1/d)`, with all remaining probability put
in a null colour.  Let `Z` be either

\[
 \sum_{h=1}^g{X_h\choose2}
 \quad\hbox{or}\quad
 \sum_{h=1}^gX_hY_h,                                      \tag{4.1}
\]

where the two counts in the second expression are disjoint colour counts.
There are constants `eta_0,c_0>0` such that

\[
 \boxed{
 \mathbb E\bigl[Z\,1_{\{Z>(1+\eta_0)\mathbb EZ\}}\bigr]
       \le \mathbb EZ\,e^{-c_0d}.}                        \tag{4.2}
\]

The same statement holds for a uniform fixed-size colour partition of an
ambient population of size `exp(Theta(d^2))`.

#### Proof

Every nonnull block count has mean `Theta(d)`.  Truncate all block counts
at `K d^(3/2)`.  A binomial Chernoff bound and a union bound over
`Theta(d^2)` blocks show that the discarded contribution is at most
`EZ exp(-Omega(d^(3/2)log d))`.

On the truncated event, changing one of the `Theta(d^4)` point colours
changes either statistic by at most `O(d^(3/2))`.  The mean of either
statistic is `Theta(d^4)`.  McDiarmid's inequality at any fixed relative
deviation therefore has exponent

\[
 {\Theta(d^8)\over\Theta(d^4)O(d^3)}=\Theta(d).            \tag{4.3}
\]

The same bound at dyadic larger deviations, together with the polynomial
maximum `Z=O(d^6)`, gives the size-biased form (4.2).  Finally use the
sequential coupling of Lemma 2.1 on the `Theta(d^4)` resources involved;
its error is `exp(-Theta(d^2))`, even after multiplication by the polynomial
maximum.  \(\square\)

Apply Lemma 4.1 to (3.5) and (3.8).  We obtain, for `j=0,1`,

\[
 \boxed{
 \mathbb E\bigl[N_j(R)1_{\{N_j(R)>(1+\eta_0)\bar N_j\}}
       \mid R\in B_j\bigr]
       \le \bar N_j e^{-c_0d}.}                           \tag{4.4}
\]

No all-resource union bound is needed.

## 5. The two-mark cylinder gives both size-biased load tails

Let `w_(alpha,j)(R)` be the number of retained options of state `alpha`
which contain `R in B_j`.  Lemma 2.3 gives

\[
 0\le w_{\alpha,0}(R)\le1,
 \qquad0\le w_{\alpha,1}(R)\le\Delta.                    \tag{5.1}
\]

Put `Delta_0=1, Delta_1=Delta`.  The actual resource load is

\[
                         \ell_j(R)=\sum_\alpha
                                  w_{\alpha,j}(R)X_\alpha. \tag{5.2}
\]

The sums `N_j(R)` in Section 3 count all unpruned option incidences, so

\[
                         \sum_\alpha w_{\alpha,j}(R)
                                  \le N_j(R).              \tag{5.3}
\]

For `t>=0`, expand the product

\[
 e^{t\ell_j}=\prod_\alpha
       \left(1+(e^{tw_{\alpha,j}}-1)X_\alpha\right).       \tag{5.4}
\]

Condition (C2), followed by `1+x<=e^x` and convexity on
`[0,Delta_j]`, gives

\[
 \begin{aligned}
 \mathbb E[e^{t\ell_j(R)}\mid B_0,B_1]
 &\le \exp\left(\vartheta\sum_\alpha
                    (e^{tw_{\alpha,j}}-1)\right)\\
 &\le \boxed{
 \exp\left({\vartheta N_j(R)\over\Delta_j}
                    (e^{t\Delta_j}-1)\right).}
                                                               \tag{5.5}
 \end{aligned}
\]

The same expansion with one distinguished factor gives

\[
 \mathbb E[\ell_j e^{t\ell_j}\mid B_0,B_1]
 \le \vartheta e^{t\Delta_j}N_j
    \exp\left({\vartheta N_j\over\Delta_j}
                    (e^{t\Delta_j}-1)\right).              \tag{5.6}
\]

Thus, on

\[
 N_j(R)\le(1+\eta_0)\bar N_j,                              \tag{5.7}

the load has the Laplace bound of `Delta_j` times a Poisson variable of
mean `(1+eta_0)rho_j/Delta_j`.  Since `Delta_j` is a fixed constant, its
constant-factor upper and size-biased tails are `exp(-Omega(rho_j))`.

### Theorem 5.1 (bottom resource-load tails)

Assume (C2).  There are fixed constants `eta_1,g_1>0`, depending only on
the bank-density constants, such that

\[
 \boxed{
 \mathbb E\left[
   \ell_j(R)1_{\{\ell_j(R)>(1+\eta_1)\rho_j\}}
       \mid R\in B_j\right]
       \le \rho_j e^{-g_1d}}
 \qquad(j=0,1).                                            \tag{5.8}
\]

Consequently, if `B_*` denotes the total option-resource incidence mass on
resources above these thresholds, then

\[
 \boxed{
                         \mathbb EB_*\le C H\bar D e^{-g_1d}.}
                                                                    \tag{5.9}
\]

#### Proof

Split according to (5.7).  On its complement, (5.5) at first order and
(4.4) give

\[
 \mathbb E[\ell_j(R)1_{(5.7)^c}\mid R\in B_j]
 \le\vartheta\bar N_j e^{-c_0d}=\rho_j e^{-c_0d}.         \tag{5.10}

On (5.7), choose `eta_1>eta_0` with a fixed gap large enough for the fixed
`Delta_j`.  Apply exponential Markov to (5.6).  Optimization is the usual
Poisson Chernoff calculation after replacing `t` by `tDelta_j`, and gives
`rho_j exp(-Omega(rho_j/Delta_j))=rho_j exp(-Omega(d))`.
This proves (5.8).

Sum (5.8) over owner resources.  Since
`|B_0|rho_0=(1+o(1))H bar D` and
`|B_1|rho_1=(2+o(1))H bar D`, equation (5.9) follows.  \(\square\)

The same argument with `m=1` in (C2) and Lemma 2.3 gives

\[
 \mathbb E|\{\hbox{selected low-option tasks}\}|
                         \le He^{-gd}.                     \tag{5.11}
\]

Indeed, sum the conditional selection marginal `<=vartheta` over all bad
marked states and then average over the banks; the total nominal marked
state mass is `vartheta W(r)_2=(1+o(1))H`.

Combining (5.9)--(5.11) with Corollary 4.1 of
`MATH_THEOREM_SEPARATOR_AMPLIFIED_BOTTOM_INDEPENDENT_TRANSVERSAL_20260805.md`
loses only `O(H exp(-g'd))=o(H/d)` tasks, provided the constants satisfy
the deterministic Haxell margin.  Asymptotically that margin is

\[
 (1-\eta)\bar D
   >2(1+\eta)\left({\bar D\over\beta_0}
                     +{4\bar D\over\beta_1}\right),       \tag{5.12}
\]

which is available by taking fixed `beta_0,beta_1` sufficiently large and
then taking `c>beta_0+beta_1-2`.

## 6. Why the current MLD and cylinder theorems do not close (C2)

There are two separate scope gaps.

### 6.1 Lower-forest MLD is linear and on the wrong random object

The current MLD theorem controls, for a deterministic owner/target family
`A`, Laplace transforms of the linear counts `|Q cap A|` of lower-chain
configuration labels.  It does not state that the residual owner bank is a
uniform role partition, and it does not control the cubic event

\[
                 1_{\{e_{ab}\in B_0\}}
                 1_{\{v_a\in B_1\}}
                 1_{\{v_b\in B_1\}}.                      \tag{6.1}
\]

Pre-reserving the banks supplies the missing bank randomness directly, so
MLD is unnecessary for Theorem 2.2.  It still says nothing about the upper
SDR's marked-state law after that reservation.

### 6.2 The proved owner cylinder has only one mark

The existing slack-level cylinder controls occurrence pairs `(T,b_2)` at
scale

\[
                         {1+o(1)\over dr}.                  \tag{6.2}

Condition (C2) controls triples `(T,b_2,b_1)` at the smaller scale

\[
                         {1+o(1)\over d(r)_2}.              \tag{6.3}

The implication is false without a new assertion about the second mark.
For example, start with any law satisfying the one-mark cylinder and set

\[
                         b_1=f(T,b_2)                       \tag{6.4}

deterministically, where `f(T,b_2)` is one chosen member of `T-{b_2}`.
The law of `(T,b_2)` and every one-mark cylinder is unchanged, but a
prescribed supported triple has probability of order `1/(dr)`, a factor
`r-1` larger than (6.3).

There is also a direct post-upper obstruction to deriving Theorem 2.2 from
the one-mark cylinder.  After any upper state has been fixed, choose `B_1`
and then choose `B_0` to avoid all edge-resources `e_ab` induced by its
selected `B_1` vertices.  Only `O(d^2)` edge-resources are forbidden inside
an owner universe of exponential size, so the required bank cardinality is
unchanged, while that task has `Omega=empty`.  The upper occurrence law,
including every cylinder in (6.2), is untouched.  Thus the role banks must
be selected before, and coupled probabilistically to, the upper SDR.

## 7. The exact remaining theorem

The Bottom option-tail lemma is reduced to the following single owner-side
statement.

> **Pre-reserved two-mark spread SDR.**  After the separator sacrifice and
> the uniform reservation of `B_0,B_1`, install levels `j>=2` in their
> complement from a distribution satisfying the bank-conditioned marked
> cylinder (C2), up to order `O(d)`, while preserving the already required
> owner, freshness, and terminal hull constraints.

Theorem 1.1 shows that this process has fixed scalar slack at every upper
level.  Theorems 2.2 and 5.1 then supply, respectively, the exponential low
option-degree tail and both exponential size-biased resource-load tails.
No bottom Hall-cut or comparator theorem remains after (C2).

What is not proof-safe is to cite the present one-mark cylinder or lower
MLD as if either implied (C2).  A possible route is to choose `b_1`
uniformly after `(T,b_2)` under a symmetry-preserving upper SDR law; then
the one-mark cylinder multiplies by `(r-1)^(-m)` and gives (C2) immediately.
The FIFO/lower-chain construction does not currently prove that this
uniform second-mark refinement is physically available.
