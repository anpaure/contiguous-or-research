# Gate A: finite-bite carrier hazard evolves by conflict-boundary conductance

**Date:** 2026-08-22  
**Status:** unconditional finite-hypergraph theorem.  It replaces the
`Z-Q` subtraction in the ancestor-row analysis by a local hazard-boundary
formula.  It does not prove the stopped punctured conductance regression.

Let `H` be a finite simple hypergraph and let its conflict graph have one
vertex for each row of `H`, with loops suppressed.  It is convenient to use
closed conflict neighbourhoods

\[
 \Gamma(F)=\{G\in E(H):G\cap F\ne\varnothing\},\qquad
 \Delta_C=\max_F|\Gamma(F)|.                                \tag{1.1}
\]

Fix an ordered carrier `gamma=(v;F_1,...,F_m)` with distinct carrier rows
and `v in F_1 cap ... cap F_m`.  Different roots and different orderings
are distinct labelled carrier objects.
Put

\[
 B_\gamma=\bigcup_{i=1}^m\Gamma(F_i),\qquad
 D_\gamma=E(H)-B_\gamma,\qquad h_\gamma=|B_\gamma|.          \tag{1.2}
\]

Thus `h_gamma` is exactly the carrier-killing singleton hazard and
`D_gamma` is its avoidance set.  Define the ordered conflict-boundary
conductance numerator

\[
 T_\gamma=
 \sum_{K\in D_\gamma}|\Gamma(K)\cap B_\gamma|
 =\sum_{R\in B_\gamma}|\Gamma(R)\cap D_\gamma|.             \tag{1.3}
\]

The equality uses symmetry of intersection.  Notice the deterministic
bounds

\[
 h_\gamma\le m\Delta_C,qquad
 0\le T_\gamma\le h_\gamma\Delta_C.                        \tag{1.4}
\]

Mark every row independently with probability `p`, accept precisely the
isolated marked rows, delete all targets in accepted rows, and call the
induced residual `H_p`.  Let `A_gamma` be the event that every carrier row
survives.  On this event let

\[
 h_\gamma(H_p)=\left|\bigcup_i\Gamma_{H_p}(F_i)\right|.      \tag{1.5}
\]

## 1. Exact tangent

### Theorem 1.1

At `p=0`,

\[
 \boxed{
 {d\over dp}\Pr(A_\gamma)\bigg|_{p=0}=-h_\gamma,\qquad
 {d\over dp}\mathbb E[h_\gamma(H_p)\mid A_\gamma]
       \bigg|_{p=0}=-T_\gamma.}                             \tag{1.6}
\]

#### Proof

With no marks the carrier survives and its hazard is `h_gamma`.  With one
marked row `K`, the mark is isolated.  If `K in B_gamma`, the carrier dies.
If `K in D_gamma`, the carrier survives and precisely the rows in
`B_gamma cap Gamma(K)` disappear from its hazard.  Hence, for

\[
 N_\gamma(p)=\mathbb E[\mathbf1_{A_\gamma}h_\gamma(H_p)],
 \qquad a_\gamma(p)=\Pr(A_\gamma),                           \tag{1.7}
\]

the empty- and singleton-mark coefficients give

\[
 a_\gamma'(0)=-h_\gamma,qquad
 N_\gamma'(0)=-h_\gamma^2-T_\gamma.                         \tag{1.8}
\]

Differentiate `N_gamma/a_gamma` at zero.  The two `h_gamma^2` terms cancel,
leaving `-T_gamma`.  \(\square\)

Thus the first-order child hazard is controlled by the edge boundary of
the *small conflict union* `B_gamma`, not by subtracting two quantities of
order `Z=|E(H)|`.

## 2. Uniform finite-bite formula

For an integer `s>=1`, set

\[
                         C_s={s^2\over2}+s.                  \tag{2.1}
\]

The elementary carrier-survival expansion says that a fixed family of at
most `s` rows, whose closed conflict-union has size `c`, survives with
probability

\[
                         1-pc+u,\qquad
                         0\le u\le C_s(p\Delta_C)^2.         \tag{2.2}
\]

Indeed, no mark in the conflict union is sufficient.  The quadratic Taylor
remainder of `(1-p)^c` costs at most `s^2(p Delta_C)^2/2`; any additional
survival requires a marked union row and a second marked conflict
neighbour, costing at most `s(p Delta_C)^2`.

### Theorem 2.1

Put `theta=p Delta_C` and assume `m theta<=1/4`.  Then

\[
 \boxed{
 \mathbb E[h_\gamma(H_p)\mid A_\gamma]
 =h_\gamma-pT_\gamma+\mathcal E_\gamma,\qquad
 |\mathcal E_\gamma|\le C_m^*h_\gamma\theta^2,}             \tag{2.3}
\]

where one may take

\[
                         C_m^*=2(C_{m+1}+C_m+m).              \tag{2.4}
\]

#### Proof

A row `R in B_gamma` belongs to the child hazard exactly when the carrier
rows and `R` all survive.  The distinct-row family has size at most `m+1`
and conflict-union

\[
 |B_\gamma\cup\Gamma(R)|
 =h_\gamma+|\Gamma(R)-B_\gamma|.                            \tag{2.5}
\]

Sum (2.2) over `R in B_gamma` and use (1.3):

\[
 N_\gamma(p)
 =h_\gamma-p(h_\gamma^2+T_\gamma)+U_\gamma,qquad
 0\le U_\gamma\le C_{m+1}h_\gamma\theta^2.                 \tag{2.6}
\]

Applying (2.2) to the carrier itself gives

\[
 a_\gamma(p)=1-ph_\gamma+u_\gamma,qquad
 0\le u_\gamma\le C_m\theta^2.                              \tag{2.7}
\]

Subtract `a_gamma(p)(h_gamma-pT_gamma)` from (2.6).  The difference is

\[
 U_\gamma-u_\gamma(h_\gamma-pT_\gamma)
                  -p^2h_\gamma T_\gamma.                    \tag{2.8}
\]

By (1.4), `pT_gamma<=h_gamma theta` and

\[
 p^2h_\gamma T_\gamma
 \le h_\gamma(ph_\gamma)(p\Delta_C)
 \le m h_\gamma\theta^2.                                   \tag{2.9}
\]

Also `a_gamma>=1-ph_gamma>=3/4`.  Equations (2.6)--(2.9), with a harmless
enlargement from `4/3` to `2`, prove (2.3)--(2.4).  \(\square\)

The error in (2.3) is relative to the local hazard `h_gamma=O_m(Delta_C)`.
Reconstructing the same statement from the avoidance count
`Q=Z-h_gamma` would leave a crude `Z theta^2` error, which is useless at
the punctured scale.  Formula (2.6) is the cancellation that removes it.

## 3. A whole old carrier bucket

Let `C` be any nonempty finite family of ordered `m`-carriers in the same
deterministic `H`.  Choose `gamma` uniformly from `C`, perform the bite,
and then condition jointly on its survival.  Write

\[
 \mu=\mathbb E_\mathcal C h_\gamma,qquad
 \tau=\mathbb E_\mathcal C T_\gamma,qquad
 V=\operatorname {Var}_\mathcal C h_\gamma.                 \tag{3.1}
\]

### Theorem 3.1

If `m theta<=1/4`, then

\[
 \boxed{
 \mathbb E[h_\gamma(H_p)\mid\gamma\in\mathcal C,
                                  A_\gamma]
 =\mu-p(\tau+V)+\mathcal E_\mathcal C,\qquad
 |\mathcal E_\mathcal C|\le C_m^{\rm fam}\mu\theta^2,}     \tag{3.2}
\]

where, for example,

\[
 C_m^{\rm fam}=2\{C_{m+1}+2C_m+m(m+1)\}.                   \tag{3.3}
\]

#### Proof

Average (2.6)--(2.7) over `C`.  The numerator and denominator are

\[
 N=\mu-p\mathbb E h_\gamma^2-p\tau+U,qquad
 a=1-p\mu+u,                                                \tag{3.4}
\]

where `0<=U<=C_{m+1}mu theta^2` and `0<=u<=C_m theta^2`.
Because `E h^2=mu^2+V`, the candidate in (3.2) is
`M=mu-p(tau+V)`.  A direct subtraction gives

\[
                         N-aM=U-p^2\mu(\tau+V)-uM.           \tag{3.5}
\]

Now `tau<=mu Delta_C`, `V<=E h^2<=m Delta_C mu`, and
`p mu<=m theta`.  Also `|M|<=2mu` under the assumed smallness.  Hence the
absolute value of (3.5) is at most

\[
 \{C_{m+1}+2C_m+m(m+1)\}\mu\theta^2.                       \tag{3.6}
\]

Finally `a>=1-pmu>=3/4`; enlarging `4/3` to `2` proves (3.2)--(3.3).
\(\square\)

Within one fixed family the variance term in (3.2) is a nonnegative
decrement: survival preferentially removes high-hazard carriers.  Its size
may nevertheless vary arbitrarily between old degree buckets, so it is not
globally favorable for a regression comparison.  On a fixed root shore put

\[
 B_d=\{v:d_H(v)=d\},                                       \tag{3.7a}
\]

For a nonempty bucket with `d>=m`, take `C_d` to be all labelled ordered
carriers rooted in `B_d`.  Every
root in this bucket has exactly `(d)_m` carriers, so the uniform law on
`C_d` is the carrier-Palm law obtained by choosing the root uniformly from
`B_d` and then its ordered carrier uniformly.  Equation (3.2) is the exact
finite-bite **ancestor-row hazard evolution** needed after the one-step-lag
erosion-absorption theorem.  Its complete decrement profile is

\[
 \boxed{\kappa_d=\tau_d+V_d,qquad
 \tau_d=\mathbb E_{\mathcal C_d}T_\gamma,\qquad
 V_d=\operatorname {Var}_{\mathcal C_d}h_\gamma.}          \tag{3.7}
\]

Both `tau_d` and `V_d`, and especially their sum, must be retained in the
degree-regression ledger.

This is a literal necessity, not only cautious bookkeeping.  On ground set
`{0,1,2,3,4}`, take the nine rows

\[
 04,01,134,13,234,02,013,024,034                         \tag{3.7b}
\]

and let `m=2`.  For the unique degree-four root `1`, direct enumeration of
its `(4)_2` labelled carriers gives

\[
 (\mu_4,\tau_4,V_4)=\left({53\over6},1,{5\over36}\right),  \tag{3.7c}
\]

whereas the unique degree-six root `0` gives

\[
 (\mu_6,\tau_6,V_6)=\left({44\over5},1,{4\over25}\right).  \tag{3.7d}
\]

Thus `tau_d` is constant while
`kappa_6=29/25>41/36=kappa_4`; the variance profile alone creates a
harmful contribution to the downward ancestor regression.

### 3.2 Exact two-blocker exposure form

The two quantities in (3.7) have a closed rootwise formula.  Fix a root `v` of
degree `d>=m`.  For rows `R,K`, put

\[
 a_R(v)=|\{F\ni v:F\cap R\ne\varnothing\}|,
 \qquad
 a_{R\cup K}(v)=|\{F\ni v:F\cap(R\cup K)\ne\varnothing\}|, \tag{3.8}
\]

and

\[
 P_R^0={(d-a_R(v))_m\over(d)_m},\qquad
 P_{RK}^0={(d-a_{R\cup K}(v))_m\over(d)_m}.                 \tag{3.9}
\]

Choose the ordered carrier uniformly from the star of `v`.  The event
`R notin B_gamma` has probability `P_R^0`, while simultaneous avoidance
of `R,K` has probability `P_RK^0`.  Therefore

\[
 \boxed{
 \overline T_m(v)=\mathbb E[T_\gamma\mid v]
 =\sum_{\substack{R,K\in E(H)\\R\cap K\ne\varnothing}}
       (P_K^0-P_{RK}^0).}                                   \tag{3.10}
\]

Indeed the summand is exactly the probability that the carrier hits `R`
but avoids `K`, which is the indicator defining the oriented boundary in
(1.3).  The same two-blocker data give

\[
 \boxed{
 \mathbb E[h_\gamma^2\mid v]
 =\sum_{R,K\in E(H)}(1-P_R^0-P_K^0+P_{RK}^0),}              \tag{3.11}
\]

because the summand is the probability that the carrier hits both rows.
Together with

\[
 \mathbb E[h_\gamma\mid v]=\sum_R(1-P_R^0),                 \tag{3.12}
\]

(3.10)--(3.12) express the complete bucket decrement
`tau+Var(h)` in (3.2) through one-root, two-blocker avoidance counts.  No
enumeration of child degree columns is present.

## 4. Conflict-matrix compression

Let `A` be the closed conflict matrix on `E(H)`:

\[
 A_{R,K}=\mathbf1_{\{R\cap K\ne\varnothing\}},\qquad
 C=A\mathbf1,\qquad \overline C={\mathbf1^TC\over Z}.       \tag{4.1}
\]

For a carrier `gamma`, let `c_gamma` be the zero-one vector of its `m`
carrier rows and let `b_gamma` be the zero-one vector of `B_gamma`.  Then

\[
 b_\gamma=\mathbf1_{\{Ac_\gamma>0\}},\qquad
                         0\le b_\gamma\le Ac_\gamma         \tag{4.2}
\]

coordinatewise.

### Theorem 4.1 (common contraction plus three-walk energy)

Define

\[
 J_\gamma=\sum_{R\in B_\gamma}(C_R-\overline C),\qquad
 W_\gamma=c_\gamma^TA^3c_\gamma.                            \tag{4.3}
\]

Then

\[
 \boxed{
 \overline C h_\gamma+J_\gamma-W_\gamma
 \le T_\gamma
 \le\overline C h_\gamma+J_\gamma.}                        \tag{4.4}
\]

Consequently Theorem 2.1 implies

\[
 \boxed{
 \mathbb E[h_\gamma(H_p)\mid A_\gamma]
 \le(1-p\overline C)h_\gamma
       +p(W_\gamma-J_\gamma)
       +C_m^*h_\gamma\theta^2.}                             \tag{4.5}
\]

#### Proof

The oriented cut identity is

\[
 T_\gamma=b_\gamma^TA(\mathbf1-b_\gamma)
 =\overline C h_\gamma+J_\gamma-b_\gamma^TAb_\gamma.       \tag{4.6}
\]

The last quadratic form is nonnegative.  Since `A` has nonnegative
entries, (4.2) also gives

\[
 b_\gamma^TAb_\gamma
 \le(Ac_\gamma)^TA(Ac_\gamma)
 =c_\gamma^TA^3c_\gamma=W_\gamma.                          \tag{4.7}
\]

This proves (4.4); insert its lower bound into (2.3) to obtain (4.5).
\(\square\)

Both error profiles in (4.5) have exact rootwise averages.  With the
notation (3.8)--(3.9),

\[
 \boxed{
 \mathbb E[J_\gamma\mid v]
 =\sum_R(1-P_R^0)(C_R-\overline C).}                        \tag{4.8}
\]

Uniform ordered sampling without replacement from the root star also gives

\[
\boxed{
\begin{aligned}
 \mathbb E[W_\gamma\mid v]
 ={}&{m\over d}\sum_{F\ni v}(A^3)_{F,F}\\
 &+{m(m-1)\over(d)_2}
   \sum_{\substack{F,G\ni v\\F\ne G}}(A^3)_{F,G}.
\end{aligned}}                                             \tag{4.9}
\]

Thus the common term `p overline C h` in (4.5) is a scalar contraction and
cannot by itself create a degree inversion.  The exact structural profiles
left after that contraction are the centered conflict-degree exposure
(4.8), the length-three conflict-walk energy (4.9), and the bucket variance
`V_d` in (3.7).  This is a finite, fixed-order interface; no maximum-degree
cap alone bounds these profiles.

## 5. Punctured scale and the remaining theorem

In the stopped punctured range, `Delta_C=O(rz)`,
`p=O(epsilon/(rz))`, and hence `theta=O(epsilon)`.  On a child fibre where
the next bite rate has one common value `p_+`, take `Delta` to be a common
parent/child conflict-degree bound and put `theta_+=p_+Delta`.  Multiplying
(2.3) by this constant gives an error

\[
                         O_m(p_+h_\gamma\theta^2)
                         =O_m(\theta_+\theta^2).             \tag{5.1}
\]

The established microbite schedule makes the sum of such quadratic terms
negligible.  Thus the previous `Z theta^2` obstruction is absent.

In the literal random-clock process, however, `p_+=p_+(H_p)` is generally
child-state-dependent.  Equation (5.1) cannot then be obtained by pulling
`p_+` through the conditional expectation.  One must prove the weighted
version or retain the predictable-rate and global-size mixing explicitly.

What remains is not a generic graph theorem.  It is a punctured-specific,
stopped state-Palm estimate showing that the weighted decrement profile
corresponding to `kappa_d=tau_d+V_d` does not acquire enough degree
variation to spend the Gate-A logarithmic budget.  Even on a constant-rate
fibre the relevant term is `p p_+ kappa_d`, not merely `p p_+ tau_d`.
The ingredients in (3.7), equivalently (3.10)--(3.12) and the profiles
(4.8)--(4.9), are bounded-order rooted objects to which the existing
boundary-codegree and polymer expansion can be applied.  The literal live
gate additionally retains predictable-rate and global-size mixing.  This
note does not perform that stopped comparison and does not claim Gate A
closed.
