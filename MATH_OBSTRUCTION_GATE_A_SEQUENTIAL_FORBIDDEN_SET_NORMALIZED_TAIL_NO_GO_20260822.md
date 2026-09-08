# Gate A: the positive sequential forbidden-set representation stops at the carrier mixture

**Date:** 2026-08-22  
**Status:** exact positive representation and exact non-punctured
normalized-tail no-go; no punctured tail bound is claimed

## 0. Outcome

For integer \(c\ge m-1\), the normalized cutoff test

\[
 \varphi_c(d)={(d-c)_+^m\over(d)_m}                       \tag{0.1}
\]

has an exact positive sequential representation.  Give the live root rows
a uniform random priority order.  At carrier step \(j\), forbid the top
\(c-j\) remaining live rows.  A fixed ordered \(m\)-carrier passes all
steps with probability

\[
 \prod_{j=0}^{m-1}{d-c\over d-j}
 ={(d-c)^m\over(d)_m}.                                   \tag{0.2}
\]

For fixed carrier labels and fixed priorities, this success event is
coordinatewise increasing in the retained target state.  It therefore
gives a positive-event proof of the fixed-carrier Harris inequality.

The representation does **not** compare different carrier labels.  An
exact product hypergraph at \(m=12,c=11\) has

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\varphi_{11}(d_v))<0, \tag{0.3}
\]

although the covariance is nonnegative for every fixed carrier.  The
adverse between-label term can be amplified arbitrarily by adding external
rows without changing the root degree, the forbidden-set event, or its
carrier likelihoods.

Consequently the representation does not imply cutoff-tail uniform
integrability, a carrier-label domination theorem, or
\(\Pi_c(E)=o(1)\) from \(\Pi_{12}(E)=o(1)\).  It is an exact positive
realization of the cutoff tilt, but punctured geometry is still required
at the carrier-mixture level.

## 1. The priority/forbidden-set representation

Let a target-retention state \(X\) have a finite live root star
\(\mathcal L(X)\) of size \(d\).  Fix an ordered distinct live carrier

\[
 \gamma=(F_1,\ldots,F_m).                                \tag{1.1}
\]

Assign independent continuous priorities \(\xi_F\) to all possible root
rows, independently of \(X\).  At step \(j=0,\ldots,m-1\), remove
\(F_1,\ldots,F_j\) from the current list and let \(B_j\) be the
\(c-j\) rows of largest priority among the remaining live rows.  If
\(c-j=0\), put \(B_j=\varnothing\).  Let

\[
 \mathcal A_{c,m}(X,\gamma,\xi)
 =\{F_{j+1}\notin B_j\text{ for every }0\le j<m\}.        \tag{1.2}
\]

When \(d\le c\), define this event to be false.

### Theorem 1.1 (exact positive cutoff sampler)

For integers \(c\ge m-1\) and \(d\ge m\),

\[
 \boxed{
 \Pr_\xi(\mathcal A_{c,m}\mid X,\gamma)
 =\varphi_c(d).}                                         \tag{1.3}
\]

For fixed \(\gamma,\xi\), the indicator of
\(\mathcal A_{c,m}\) is increasing under enlargement of the live root
star.

#### Proof

Suppose the first \(j\) tests have succeeded.  Their definition is
invariant under every permutation of the \(d-j\) row labels not yet used
by the carrier.  Consequently \(F_{j+1}\) is conditionally equally likely
to occupy any of the \(d-j\) remaining priority ranks.  Exactly \(c-j\)
of those ranks are forbidden, so the next conditional success probability
is

\[
 1-{c-j\over d-j}={d-c\over d-j}.                         \tag{1.4}
\]

Multiplication over \(j\) gives (1.3).

For monotonicity, suppose the event holds for a live set \(\mathcal L\)
and enlarge it without removing a carrier row.  If \(F_{j+1}\) was not
among the \(c-j\) largest-priority rows before enlargement, at least
\(c-j\) old remaining rows had larger priority.  Those witnesses remain
after enlargement.  Hence \(F_{j+1}\) cannot enter the forbidden top set.
This holds at every step.  \(\square\)

Equivalently, \(B_0\) is a uniform \(c\)-subset of the live rows.  After
each successful carrier choice, retire the lowest-priority member of the
current blocker set.  Thus \(|B_j|=c-j\), and at every step exactly
\(d-c\) of the \(d-j\) remaining rows are allowed.

### Corollary 1.2 (the exact cutoff state law)

Let targets be retained independently.  On the joint factorial Palm
space, a state-carrier pair has unnormalized mass

\[
 \Pr(X)\mathbf1_{\{\gamma\text{ live in }X\}}.            \tag{1.5}
\]

Its state marginal is tilted by \((d)_m\), and conditional on the state
the carrier is uniform.  Adjoin independent priorities and condition on
\(\mathcal A_{c,m}\).  The new state marginal is tilted by

\[
 (d)_m\varphi_c(d)=(d-c)_+^m,                             \tag{1.6}
\]

while the carrier remains uniform conditional on the state.  Thus at
\(m=12\) its first-pair marginal is exactly the cutoff pair law
\(\Pi_c\).

#### Proof

Equation (1.3) multiplies every state-carrier atom having degree \(d\) by
the same factor \(\varphi_c(d)\).  This proves both assertions.  \(\square\)

For a fixed carrier, the live-row set is an increasing function of the
remaining target indicators.  Therefore
\(\mathcal A_{c,m}\) and every increasing carrier hazard are increasing
events/functions for fixed priorities.  Harris's inequality and averaging
over the priorities give

\[
 \operatorname {Cov}\!\left(
 h_\gamma,\varphi_c(d_v)\mid\gamma\text{ retained}\right)
 \ge0.                                                    \tag{1.7}
\]

This is useful, but it is still a fixed-carrier statement.

## 2. The carrier-mixture term survives unchanged

Let \(\pi\) be the survival-weighted carrier-label law, and put

\[
 H_\gamma=\mathbb E[h_\gamma\mid\gamma\text{ retained}],
 \qquad
 P_\gamma=\Pr(\mathcal A_{c,m}\mid\gamma\text{ retained})
          =\mathbb E[\varphi_c(d_v)\mid\gamma\text{ retained}]. \tag{2.1}
\]

The law of total covariance is

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\mathbf1_{\mathcal A})
 =\mathbb E_\pi
   \operatorname {Cov}(h_\gamma,\mathbf1_{\mathcal A}\mid\gamma)
  +\operatorname {Cov}_\pi(H_\gamma,P_\gamma).}           \tag{2.2}
\]

The first term is nonnegative by (1.7).  The forbidden-set construction
does not constrain the sign of the second term.  More generally, for a
carrier-label statistic \(K_\gamma\), conditioning on success gives

\[
 \mathbb E_\pi K_\gamma-\mathbb E_{\tau_c}K_\gamma
 =-{\operatorname {Cov}_\pi(K_\gamma,P_\gamma)
       \over\mathbb E_\pi P_\gamma}.                      \tag{2.3}
\]

Thus the rare-tail denominator and the labelwise Simpson covariance are
exactly the same objects as before the representation.

## 3. Exact normalized-tail counterexample

Retain every target independently with probability \(1/2\).  Use distinct
targets

\[
 v,a,b,\quad s_i,t_i,u_i\ (1\le i\le12),\quad
 x_{ij}\ (1\le i\le12,\ 1\le j\le M).
\]

The root-star rows are

\[
 A_i=\{v,a,s_i,t_i\},\qquad
 B_i=\{v,b,u_i\}\qquad(1\le i\le12),                      \tag{3.1}
\]

and the external rows are

\[
 X_{ij}=\{u_i,x_{ij}\}.                                   \tag{3.2}
\]

Choose an ordered twelve-carrier from the root star.  Let \(k\) be its
number of \(B\)-rows.  After cancelling a common factor \(12!\), the
survival-weighted type law is

\[
 w_k={\binom{12}k^2\over2^{b_k}},\qquad
 b_k=1+\mathbf1_{\{k>0\}}+\mathbf1_{\{k<12\}}
          +k+2(12-k),                                    \tag{3.3}
\]

\[
 Q=\sum_{k=0}^{12}w_k={125800033\over67108864},\qquad
 \pi_k={w_k\over Q}.                                      \tag{3.4}
\]

Put

\[
 \varphi(d)={(d-11)_+^{12}\over(d)_{12}}.                 \tag{3.5}
\]

For \(1\le k\le11\), conditional on the carrier, the extra root degree is

\[
 Y_k\ \buildrel d\over=\ 
 \operatorname {Bin}(k,1/4)+\operatorname {Bin}(12-k,1/2). \tag{3.6}
\]

At \(k=0\), it is zero with probability \(1/2\), while with probability
\(1/2\) it has the law \(\operatorname {Bin}(12,1/2)\).  At \(k=12\),
the analogous mixture uses \(\operatorname {Bin}(12,1/4)\).  Define

\[
 P_k=\mathbb E\varphi(12+Y_k),\qquad
 \mu_k=\mathbb E(12+Y_k).                                \tag{3.7}
\]

Every live root row meets the carrier through \(v\).  The external row
\(X_{ij}\) meets it exactly when \(B_i\) was selected, and its remaining
indicator is independent of \(d_v\).  Hence

\[
 H_k=\mu_k+{kM\over2},                                    \tag{3.8}
\]

and the fixed-carrier covariance is

\[
 C_k=\operatorname {Cov}(d_v,\varphi(d_v)\mid k)\ge0.     \tag{3.9}
\]

Exact rational collection gives

\[
 \mathbb E_\pi P_k
 ={60887760922742269\over82272825462856089600}>0,         \tag{3.10}
\]

\[
 \boxed{
 \operatorname {Cov}_\pi(k,P_k)
 =-{103531504816623590706626628809
 \over499782312714715254340487007436800}<0,}              \tag{3.11}
\]

\[
 \mathbb E_\pi C_k
 ={124405554636853845816229
 \over88991421844934028731351040}>0,                     \tag{3.12}
\]

\[
 \operatorname {Cov}_\pi(\mu_k,P_k)
 ={580109326576358854794581638963
 \over11195123804809621697226908966584320}>0.             \tag{3.13}
\]

Substitution of (3.8) into (2.2) gives

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\varphi(d_v))
 ={1449136804042488899522598372725
   -103531504816623590706626628809\,M
 \over999564625429430508680974014873600}.}                 \tag{3.14}
\]

At \(M=13\), this is

\[
 {5908152554165649057718189
 \over57209513818076379846667468800}>0,                  \tag{3.15}
\]

whereas at \(M=14\), it is

\[
 -{304263390241370370174430601
 \over999564625429430508680974014873600}<0.               \tag{3.16}
\]

For every fixed carrier, (3.9) remains nonnegative for all \(M\).
Meanwhile (3.11) and (3.14) show that the adverse between-label term tends
linearly to \(-\infty\) as external multiplicity grows.  The external
rows change neither \(d_v\), \(\varphi(d_v)\), \(P_k\), nor the
forbidden-set event.

## 4. Consequence for the punctured Gate-A residual

The priority representation is a clean positive sampler for the exact
integer cutoff law.  It proves:

1. the cutoff tilt can be realized without an alternating Newton series;
2. its success event is increasing for every fixed carrier; and
3. fixed-carrier product association is favorable.

It does not prove:

1. \(P_\gamma\) is comparable across carrier labels;
2. a rare carrier family under \(\pi_{12}\) remains rare under the
   \(P_\gamma\)-tilt;
3. kernel-weighted uniform integrability; or
4. a favorable sign for the between-carrier covariance.

The counterexample is not punctured, so it does not refute a
punctured-specific theorem.  It does prove that the sequential
forbidden-set mechanism alone cannot upgrade G.19's
\(\Pi_{12}\{\tau\ne0\}=o(1)\) to the cutoff law.  The next valid theorem
must combine this positive sampler with punctured boundary geometry—for
example, a switching or cluster estimate comparing the success
probabilities \(P_\gamma\) across the overlap cells while retaining the
signed kernel.

## 5. Checker

The exact script

scratch/verify_gate_a_sequential_forbidden_set_normalized_tail_no_go_20260822.py

verifies the sequential probability formula, evaluates every type
distribution with rational arithmetic, checks each fixed-carrier
covariance is nonnegative, and certifies (3.10)--(3.16).

