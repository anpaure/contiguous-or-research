# Gate A: one-step-lag absorption of macro erosion and degree rebinning

**Date:** 2026-08-22  
**Status:** unconditional abstract carrier-kernel theorem, followed by the
exact Gate-A specialization.  The theorem removes child-degree column
sorting as an independent obstruction.  It does not prove the remaining
ancestor-row predictable-rate regression.

The current Gate-A ledger writes the dangerous selection term at time
`j` against the *new* root degree.  Sorting surviving carriers into those
new degree buckets appears to require control of every column of the macro
transition matrices.  That is stronger than necessary.  The new test
function differs from the old one by the favorable erosion already present
in the preceding exact recursion.  Since the next scaled carrier hazard is
uniformly bounded, its covariance with this difference is only a small
multiple of that favorable erosion.  On summing the raw recursions, the
multiple is absorbed by the erosion itself.

The argument is deterministic algebra on substochastic kernels.  It has no
independence, regularity, or lower-tail hypothesis, and it remains valid
when a terminal tail becomes empty.

## 1. Carrier kernels and the exact scalar recursion

For `0<=j<J`, let `X_j` be a finite carrier-history space and let `mu_j` be
a probability measure on it.  Formally, an element of `X_j` is a path
`(x_0,...,x_j)` of current carrier states, and the parent projection deletes
the last coordinate.  Keeping the history is only a bookkeeping device: it
makes the labelled parent of every surviving carrier unique.  All kernels
and observables below may depend only on the current-state projection.  Let

\[
 K_j(x,y)\ge0,\qquad
 a_j(x)=\sum_{y\in X_{j+1}}K_j(x,y),\qquad
 \bar a_j=\mathbb E_{\mu_j}a_j>0                         \tag{1.1}
\]

be a substochastic survival kernel.  The child carrier-Palm law is

\[
 \mu_{j+1}(y)={\sum_x\mu_j(x)K_j(x,y)\over\bar a_j}.       \tag{1.2}
\]

Let `Phi_j:X_j->[0,infinity)` be a test which decreases along every
surviving transition:

\[
 \delta_j(x,y)=\Phi_j(x)-\Phi_{j+1}(y)\ge0
 \quad\hbox{whenever }K_j(x,y)>0.                           \tag{1.3}
\]

Put

\[
 A_j=\mathbb E_{\mu_j}\Phi_j,qquad
 E_j={\mathbb E_{\mu_j}\sum_yK_j(x,y)\delta_j(x,y)
             \over\bar a_j}.                               \tag{1.4}
\]

Thus `E_j` is the mean erosion under the child carrier law.  Directly from
(1.2)--(1.4),

\[
 \boxed{
 A_{j+1}=A_j+{\operatorname {Cov}_{\mu_j}(a_j,\Phi_j)
                    \over\bar a_j}-E_j.}                   \tag{1.5}
\]

This is the abstract form of the exact Gate-A Palm recursion.  Notice that
no division by `A_j` occurs.

Assume that the survival mass has the pointwise finite-bite decomposition

\[
 a_j=1-S_j+R_j,qquad
 0\le S_j\le L_j,qquad 0\le R_j\le\varepsilon_j.           \tag{1.6}
\]

The variables `S_j` and `R_j` live on `X_j`.  Since `Phi_j` is
nonnegative,

\[
 \operatorname {Cov}(R_j,\Phi_j)
 =\mathbb E(R_j\Phi_j)-\mathbb E R_j\,A_j
 \le\varepsilon_jA_j.                                      \tag{1.7}
\]

For `j>=1`, a child state has a unique labelled parent carrier in the
applications.  More generally, retain the joint parent-child law induced
by (1.2), and denote the pulled-back parent test on `X_j` by
`Phi_{j-1}^{\leftarrow}`.  Then

\[
 \Phi_j=\Phi_{j-1}^{\leftarrow}-\delta_{j-1}.                \tag{1.8}
\]

Here and below covariance involving the parent test is taken under that
joint child law; only its conditional expectation on `X_j` matters.

## 2. One-step-lag covariance absorption

### Theorem 2.1

Under (1.1)--(1.8), define `E_{-1}=0` and

\[
 B_0={[-\operatorname {Cov}_{\mu_0}(S_0,\Phi_0)]_+
              \over\bar a_0},                               \tag{2.1}
\]

while, for `j>=1`, define the ancestor-row term

\[
 B_j={[-\operatorname {Cov}_{\mu_j}
          (S_j,\Phi_{j-1}^{\leftarrow})]_+
              \over\bar a_j}.                               \tag{2.2}
\]

Also put

\[
 g_j=1+{\varepsilon_j\over\bar a_j},\qquad
 \lambda_j={L_j\over\bar a_j}.                              \tag{2.3}
\]

Then the exact one-step inequality is

\[
 \boxed{
 A_{j+1}\le g_jA_j+B_j+\lambda_jE_{j-1}-E_j.}              \tag{2.4}
\]

If

\[
                         \lambda_j\le g_j\qquad(1\le j<J), \tag{2.5}
\]

then every internal erosion term cancels after iteration, and

\[
 \boxed{
 A_J\le
 \left(\prod_{j=0}^{J-1}g_j\right)A_0
 +\sum_{j=0}^{J-1}
    \left(\prod_{k=j+1}^{J-1}g_k\right)B_j.}                \tag{2.6}
\]

In particular, if `B_j<=beta_j A_j`, then the same proof with
`g_j` replaced by `g_j+beta_j` gives

\[
 \boxed{
 A_J\le A_0\prod_{j=0}^{J-1}(g_j+\beta_j)
 \le A_0\exp\sum_{j=0}^{J-1}
       \left(\beta_j+{\varepsilon_j\over\bar a_j}\right).} \tag{2.7}
\]

The conclusions include the case `A_j=0`; no logarithm or positive-tail
denominator is needed.  They do require the explicitly assumed positive
carrier survival mass `bar a_j>0`.  An empty test tail and an empty carrier
population are different cases.

#### Proof

For `j>=1`, (1.8) gives

\[
 -\operatorname {Cov}(S_j,\Phi_j)
 =-\operatorname {Cov}(S_j,\Phi_{j-1}^{\leftarrow})
   +\operatorname {Cov}(S_j,\delta_{j-1}).                  \tag{2.8}
\]

Both variables in the last covariance are nonnegative, and
`S_j<=L_j`.  Therefore

\[
 \operatorname {Cov}(S_j,\delta_{j-1})
 \le\mathbb E(S_j\delta_{j-1})
 \le L_j\mathbb E_{\mu_j}\delta_{j-1}=L_jE_{j-1}.          \tag{2.9}
\]

For `j=0` use the definition of `B_0` directly; no lag term occurs.  Insert
`a_j=1-S_j+R_j` into (1.5), and use (1.7)--(2.2) and (2.9).  This proves
(2.4).

To iterate, multiply (2.4) by

\[
                         G_{j+1,J}=\prod_{k=j+1}^{J-1}g_k
\]

and sum over `j`.  The coefficient of an internal `E_i`, `0<=i<J-1`, is

\[
 G_{i+2,J}\lambda_{i+1}-G_{i+1,J}
 =G_{i+2,J}(\lambda_{i+1}-g_{i+1})\le0.                    \tag{2.10}
\]

The final coefficient is `-1`.  Discarding these nonpositive terms proves
(2.6).  If `B_j<=beta_jA_j`, absorb it into the coefficient of `A_j` in
(2.4); (2.5) remains true because `g_j+beta_j>=g_j`.  Iteration and
`1+x<=e^x` prove (2.7).  \(\square\)

### Corollary 2.2 (the small-bite condition is automatic)

If `L_j<=1/3`, then `a_j>=1-L_j`, so

\[
 \lambda_j\le{L_j\over1-L_j}\le{1\over2}<1\le g_j.         \tag{2.11}
\]

Thus the absorption condition (2.5) requires no extra punctured estimate.

## 3. Exact Gate-A specialization

Take `X_j` to be the alive ordered `m`-carrier histories after bite `j`, and
let `K_j` be the literal survival subkernel while the process is active.
A stopped chain is represented by freezing every history once the stopping
test fires; its later kernels have `a=1`, `S=R=delta=0`.  The transition on
which the test first fires retains its literal degree erosion before
freezing.  Killing all stopped histories, or conditioning on nonstopping,
would not satisfy (1.6) and is not being asserted here.
For a fixed terminal threshold `c>=m-1`, set

\[
 \Phi_j(H,\gamma)=\varphi_c(d_H(v)),\qquad
 \varphi_c(d)={(d-c)_+^m\over(d)_m},                         \tag{3.1}
\]

with value zero below degree `m`.  On the positive real branch,

\[
 {d\over dx}\log\varphi_c(x)
 ={m\over x-c}-\sum_{i=0}^{m-1}{1\over x-i}\ge0,             \tag{3.1a}
\]

because `c>=m-1` makes every denominator `x-i` at least `x-c`.
Thus `varphi_c` is nondecreasing.  Induced deletion only lowers degrees,
so (1.3) holds.  Equations (1.4)--(1.5) are exactly the scalar Palm
recursion, and `E_j` is exactly its favorable erosion term after division
by carrier survival mass.

For an isolated-row bite with predictable marking probability `p_j(H)`,
put

\[
 h_j(H,\gamma)=\left|\bigcup_{F\in\gamma}\Gamma_H(F)\right|,
 \qquad S_j=p_j(H)h_j(H,\gamma).                             \tag{3.2}
\]

If

\[
 \theta_j=\sup_Hp_j(H)\Delta_C(H),                           \tag{3.3}
\]

the finite-bite carrier lemma gives (1.6) with

\[
 L_j=m\theta_j,qquad
 \varepsilon_j=C_m\theta_j^2.                               \tag{3.4}
\]

Hence `m theta_j<=1/3` implies (2.5), and the already proved density-clock
bound `sum_j theta_j^2=o(1)` makes the product of the `g_j` equal
`1+o(1)`.

For `j>=1`, the only new linear term in (2.6) is

\[
 \boxed{
 B_j={[-\operatorname {Cov}_{\mu_j}
  (p_j(H_j)h_j(H_j,\gamma_j),
   \varphi_c(d_{H_{j-1}}(v)))]_+
 \over\mathbb E_{\mu_j}a_j}.}                              \tag{3.5}
\]

At `j=0` one retains (2.1).  In the punctured process it vanishes at the
fully symmetric initial catalogue because the root degree, and hence
`varphi_c(d)`, is constant; the abstract theorem does not assume this.

It is indexed by the **ancestor degree**, before the preceding erosion.
Conditioning on that degree turns (3.5) into a row statistic of the macro
transition matrix.  No child-degree column ratio occurs.

More explicitly, if

\[
 q_j^{\leftarrow}(d)=
 \mathbb E_{\mu_j}[p_j(H_j)h_j(H_j,\gamma_j)
                  \mid d_{H_{j-1}}(v)=d],                   \tag{3.6}
\]

then the pairwise identity for covariance gives

\[
 B_j\le {A_{j-1}^{\leftarrow}\over\bar a_j}
          \mathfrak J_{c,j-1}^{\leftarrow}
                 (q_j^{\leftarrow}),                        \tag{3.7}
\]

where `A_{j-1}^{leftarrow}=E_{mu_j} varphi_c(d_{H_{j-1}}(v))`
and `mathfrak J^{leftarrow}` is computed under the ancestor-degree
marginal of `mu_j`.  If `A_{j-1}^{leftarrow}=0`, the product
`A_{j-1}^{leftarrow} mathfrak J^{leftarrow}` means the unnormalized
nonnegative two-copy sum and is zero.  Formula (3.7) is merely the exact
two-copy covariance expansion; it introduces no approximation.

For a deterministic parent state and a constant-rate unconditioned bite,
the child-Palm mean avoidance conditioned on an old degree bucket `B_d` is
exactly

\[
 {\mathbb E X_1(B_d;H_p)\over\mathbb E X_0(B_d;H_p)},        \tag{3.8}
\]

the row ratio already bounded by the avoidance-extension theorem.  If, on
the child fibre in question, the next rate and edge count have common
values `p_*` and `Z_*`, respectively, then (3.6) is literally

\[
 q_j^{\leftarrow}(d)=p_*\left\{Z_*-{
 \mathbb E X_1(B_d;H_p)\over\mathbb E X_0(B_d;H_p)}\right\}. \tag{3.9}
\]

Thus constants are covariance-inert and the avoidance theorem addresses
the correct row object in this fibrewise situation.  Without common
`p_*` and `Z_*`, (3.8) is only the avoidance component: the weighted
global-size term must be retained.  What remains in the literal
random-clock process is precisely this predictable-rate, global-size, and
stopped state-Palm version.

## 4. Consequence for the Gate-A ledger

The macro child-degree matrices remain valid exact bookkeeping, but their
columns need not be controlled.  Equations (2.4)--(2.7) show that:

1. all covariance created solely by replacing the ancestor degree with the
   realized child degree is at most `L_j E_{j-1}`;
2. this is absorbed by the `-E_{j-1}` term in the preceding raw Palm
   recursion;
3. finite-bite remainders retain their already summable quadratic budget;
4. the rebinning absorption itself remains valid when a terminal tail is
   empty and introduces no division by that tail mass; and
5. the live Gate-A input is the ancestor-row predictable-rate regression
   (3.5)--(3.7), not a columnwise erosion-rebinning theorem.

This is a strict reduction, not a proof of Gate A.  In particular,
per-state row regression still does not by itself control Simpson mixing
under the stopped state-Palm law.  Nor may (2.6), which discards the
remaining favorable erosion, be used by itself to compare the terminal
tail with the much smaller uniform-slice tail.  The aggregate
actual/reference erosion and realized-center comparison remains necessary;
the theorem says only that *degree sorting inside the next selection
covariance* does not require a separate columnwise estimate.  The next
analytic targets are the weighted ancestor-row profile (3.6) and that
aggregate reference comparison.

The companion checker verifies the finite-history algebra (1.5), (2.4),
and (2.6), including complete erosion of a test tail.  It does not simulate
a stopping rule or certify the punctured interfaces (3.5)--(3.9); those
are proved symbolically above.
