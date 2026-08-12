# AD24: variance-throughput obstruction to uniform LVMR

Date: 2026-07-25

Pure mathematics only.  No computation, solver, search, or web input is
used.

## 0. Verdict

The low-variance mean-reversion implication in
`MATH_ATTACK_AD22_DEPENDENT_VERTICAL_PHASE_ROUNDING_20260725.md` is
algebraically correct, but its uniform hypothesis is impossible at the
claimed variance scale.

The obstruction is elementary and exact.  If an integral row change
\(z\in\mathbb Z^N\) satisfies

\[
 \mathbb Ez=-\kappa g+e,
 \qquad
 \mathbb E\|z\|_2^2\le C,                                  \tag{0.1}
\]

then

\[
 \boxed{
 {\|e\|_2^2\over\kappa^2}
 \ge {\bigl(\|g\|_1-C/\kappa\bigr)_+^2\over N}.}            \tag{0.2}
\]

At the calibrated middle row there is a literal one-order-per-top state
with

\[
 \|g\|_1\ge\gamma W                                       \tag{0.3}
\]

for an absolute \(\gamma>0\).  It is obtained by one independent uniform
cyclic order in every top and then retaining one realization; the middle
loads are asymptotically Poisson with mean one.

Since

\[
 p=N_H=(1+o(1)){W\over m},\qquad
 \kappa\ge {c\over p},\qquad M\sim m,                       \tag{0.4}
\]

every uniform variance bound \(C_m=o(M)\) gives

\[
 {C_m\over\kappa}le {C_mp\over c}=o(W).                    \tag{0.5}
\]

Putting \(N=W\) in (0.2) therefore forces

\[
 \boxed{{\|e\|_2^2\over\kappa^2}\ge(\gamma^2-o(1))W.}      \tag{0.6}
\]

This contradicts the required uniform bias budget \(o(W)\).  In
particular:

* the rowwise hypothesis \(\mathrm{LVMR}(c,C,\varepsilon)\) with fixed
  \(C\) and \(\sum_j\beta_j=o(W)\) is false;
* the simultaneous hypothesis with total variance \(C_m=o(M)\) and
  \(\beta(m)=o(W)\) is false; and
* the row-dependent variant \(C_j=o(m/Q)\) is also false uniformly over
  all states.

The conditional descent theorems remain valid implications.  A viable
replacement must either restrict the kernel to a near-balanced domain,
allow variance \(\Omega(M)\) at Poisson-like states, reduce the drift rate
there, or first construct a near-balanced starting state by a separate
global theorem.

## 1. The exact integral throughput lemma

### Theorem 1.1 (variance-throughput inequality)

Let \(z\) be an integrable random vector in \(\mathbb Z^N\).  If (0.1)
holds with \(\kappa>0\), then (0.2) holds.

#### Proof

For every integer \(a\),

\[
 |a|\le a^2.
\]

Coordinatewise summation gives

\[
 \|z\|_1\le\|z\|_2^2.                                     \tag{1.1}
\]

Jensen's inequality and (0.1) now give

\[
 \|\mathbb Ez\|_1
 \le\mathbb E\|z\|_1
 \le\mathbb E\|z\|_2^2
 \le C.                                                     \tag{1.2}
\]

Since \(\mathbb Ez=-\kappa g+e\), the reverse triangle inequality yields

\[
 \|e\|_1
 \ge\kappa\|g\|_1-C.                                      \tag{1.3}
\]

Finally \(\|e\|_1\le\sqrt N\|e\|_2\).  Taking the positive part in
(1.3), squaring, and dividing by \(N\kappa^2\) proves (0.2).
\(\square\)

The unbiased specialization is particularly transparent:

\[
 e=0
 \quad\Longrightarrow\quad
 \mathbb E\|z\|_2^2\ge\kappa\|g\|_1.                      \tag{1.4}
\]

Thus an integral kernel cannot generate a diffuse drift without paying
for its total \(\ell_1\) throughput in squared jump size.  Rare large
exchanges do not evade (1.4).

## 2. Existence of the required hard integral state

Use the calibrated first crossing

\[
 H=\min\{h:\lambda_h\ge m+h\},\qquad M=m+H,
 \qquad p=N_H,qquad S=Mp.                                 \tag{2.1}
\]

Choose independently and uniformly one directed cyclic order in every
top \(U\in\binom{[2m]}M\).  This is a valid integral one-order-per-top
configuration, and cutting each full promotion cycle gives one literal
path per top.

Fix a middle owner \(X\).  The number of tops containing it is

\[
 a=\binom mH.                                               \tag{2.2}
\]

Inside one containing top, a uniformly random cyclic order contains \(X\)
as a cyclic \(m\)-interval with probability

\[
 \rho={M\over\binom Mm}.                                   \tag{2.3}
\]

The middle load \(Z_X\) therefore has the exact binomial law

\[
 Z_X\sim\operatorname{Bin}(a,\rho),qquad
 a\rho={S\over W}=:\mu.                                    \tag{2.4}
\]

At the first crossing,

\[
 \mu=1-o(1),\qquad \rho=o(1).                              \tag{2.5}
\]

Consequently

\[
 \Pr(Z_X=0)=(1-\rho)^a
 =\exp(-\mu+O(\mu\rho))longrightarrow e^{-1}.             \tag{2.6}
\]

The centered middle vector in LVMR is

\[
 g_X=Z_X-\mu.                                               \tag{2.7}
\]

Every zero load contributes \(\mu\) to \(\|g\|_1\).  Hence

\[
 \mathbb E\|g\|_1
 \ge W\mu(1-\rho)^a
 =(e^{-1}+o(1))W.                                          \tag{2.8}
\]

Some integral realization therefore satisfies (0.3), for example with
any fixed \(\gamma<e^{-1}\) and all sufficiently large \(m\).

This state need not be an owner near-transversal.  That is precisely why
it refutes the published uniform hypothesis: LVMR is quantified over
every integral one-order-per-top configuration, not only over states
already known to have \(o(W)\) owner holes.

## 3. Failure of rowwise uniform LVMR

Apply Theorem 1.1 at the middle row of the state in Section 2.  Here the
row dimension is

\[
 N=W.                                                       \tag{3.1}
\]

Under the rowwise hypothesis,

\[
 \kappa\ge {c\over p},\qquad
 \mathbb E\|z\|_2^2\le C                                  \tag{3.2}
\]

with fixed \(c,C>0\).  Therefore

\[
 {C\over\kappa}\le {Cp\over c}=O(W/m)=o(W).                \tag{3.3}
\]

Equations (0.2)--(0.3) give

\[
 {\|e\|_2^2\over\kappa^2}
 \ge {\bigl(\gamma W-o(W)\bigr)^2\over W}
 =\bigl(\gamma^2-o(1)\bigr)W.                              \tag{3.4}
\]

But LVMR requires a deterministic \(\beta_j(m)\) dominating this quantity
at every state and

\[
 \sum_j\beta_j(m)=o(W).                                    \tag{3.5}
\]

The middle term alone violates (3.5).  Thus the stated rowwise LVMR
hypothesis is false for every ordering of the hard rows.

The order of the stages does not rescue it.  A stage-\(j\) current state is
any one-order-per-top configuration together with the requirement that its
legal exchanges freeze the earlier row loads; the definition places no
restriction on what those already-frozen values are.  The configuration
from Section 2 is therefore among the states covered by the uniform
quantifier when the middle row is processed.

## 4. Failure of simultaneous low-variance mean reversion

In the simultaneous theorem, suppose

\[
 \mathbb E\sum_j\|z_j\|_2^2\le C_m=o(M).                   \tag{4.1}
\]

The middle component alone then satisfies the premise of Theorem 1.1 with
\(C=C_m\).  Since \(p=(1+o(1))W/m\) and \(M\sim m\),

\[
 {C_m\over\kappa_m}
 \le {C_mp\over c}=o(W).                                   \tag{4.2}
\]

Thus

\[
 {\|e_m\|_2^2\over\kappa_m^2}
 \ge(\gamma^2-o(1))W.                                      \tag{4.3}
\]

The theorem defines

\[
 \kappa_*:=\min_j\kappa_j\le\kappa_m
\]

and requires

\[
 \sum_j{\|e_j\|_2^2\over\kappa_j\kappa_*}\le\beta(m).
\]

For the middle summand,

\[
 {\|e_m\|_2^2\over\kappa_m\kappa_*}
 \ge {\|e_m\|_2^2\over\kappa_m^2}
 \ge(\gamma^2-o(1))W.                                      \tag{4.4}
\]

Hence \(\beta(m)=o(W)\) is impossible.  The same argument applies to any
uniform row-dependent bound \(C_j=o(M)\), including the advertised
\(C_j=o(m/Q)\) sufficient scale.

## 5. Exact scope and repair options

Theorems 5.1 and 5.2 of the source report are conditional-expectation
arguments.  Their algebra, constants, floor potential, and literal
implication are not invalidated.  What fails is the existence of their
uniform hypotheses.

The throughput inequality identifies the necessary repairs exactly.

1. **Large-state variance.**  With negligible bias, (1.4) and (0.3) force

   \[
    C\ge\kappa\|g\|_1
      \ge {c\gamma W\over p}
      =(c\gamma+o(1))m=\Omega(M).                           \tag{5.1}
   \]

   The independent heat-bath variance \(\Theta(M)\) is therefore of the
   correct unavoidable order at this state.

2. **Restricted domain.**  A low-variance kernel may still exist after a
   separate construction has already made \(\|g\|_1=o(W)\).  The descent
   theorem would then have to be restated only on that invariant
   near-balanced domain, and a starting state in the domain must be proved.

3. **State-dependent drift.**  One may lower \(\kappa\) at far-off states
   so that \(\kappa\|g\|_1\) fits the available variance.  This abandons
   the uniform lower bound \(\kappa\ge c/p\), and the terminal-energy proof
   must be re-audited with the resulting drift schedule.

4. **Macroscopic bias.**  A bias can cancel the infeasible diffuse drift,
   but (0.2) proves that its normalized squared cost is \(\Omega(W)\),
   exactly too large for coefficient one.

Thus uniform low variance cannot be the missing global packet theorem.  It
can only be a cleanup mechanism after a separate near-balancing result, or
it must pay the same \(\Theta(M)\) variance as whole-packet heat-bath
resampling on Poisson-like states.
