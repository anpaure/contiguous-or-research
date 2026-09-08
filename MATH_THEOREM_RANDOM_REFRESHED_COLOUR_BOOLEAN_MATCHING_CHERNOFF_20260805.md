# Randomly refreshed colours close the Boolean one-step Chernoff gate

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional one-interface theorem.  Uniform fixed-count
refreshes on the old and dummy shores, followed by a uniform perfect
matching of the augmented Boolean interface, give the required owner-wise
Chernoff concentration for each shore and for their complete colour sum.
Thus, for this refreshed-colour route, the remaining obstruction is not
one-step matching concentration but the physical right to refresh
persistent configuration colours between consecutive interfaces.  The
alternative deterministic-colour matching problem is not claimed solved.

## 1. Setup

Let `n=2r`, let `q<r`, and put

\[
 L=\binom{[n]}q,\qquad R=\binom{[n]}{q+1},
 \qquad m=|L|,\qquad N=|R|,\qquad h=N-m.
\tag{1.1}
\]

The square augmented interface `J_q` consists of the Boolean inclusion
graph `L--R` together with `N-m` labelled universal left dummies.  Let
`M` be a uniformly random perfect matching of `J_q`, and let

\[
 I=\{T\in R:T\hbox{ is matched to an old vertex of }L\}.
\tag{1.2}
\]

Write `mathcal D` for the `h` labelled dummies.  Independently of `M`,
choose two mutually independent uniform labelled partitions

\[
 L=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_c,
 \qquad |A_j|=m_j,
 \qquad \sum_jm_j=m.
\tag{1.3}
\]

and

\[
 \mathcal D=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_c,
 \qquad |B_j|=h_j,
 \qquad \sum_jh_j=h.
\tag{1.4}
\]

For `U subset [n]`, `|U|=v>=q+1`, define

\[
 X_{j,U}=|\{S\in A_j:M(S)\in\tbinom U{q+1}\}|.
\tag{1.5}
\]

For the dummy contribution and the complete colour contribution, put

\[
 Z_{j,U}=|\{d\in B_j:M(d)\in\tbinom U{q+1}\}|,
 \qquad
 W_{j,U}=X_{j,U}+Z_{j,U}.
\tag{1.6}
\]

Write

\[
 p_j={m_j\over m},\qquad
 \mu_U={m\over N}\binom v{q+1},\qquad
 \mu_{j,U}=p_j\mu_U={m_j\over N}\binom v{q+1}.
\tag{1.7}
\]

Also write

\[
 s_j={h_j\over h},\qquad
 \nu_U={h\over N}\binom v{q+1},\qquad
 \nu_{j,U}=s_j\nu_U={h_j\over N}\binom v{q+1},
\tag{1.8}
\]

and

\[
 \theta_{j,U}=\mu_{j,U}+\nu_{j,U}
 =\mathbb E W_{j,U}.
\tag{1.9}
\]

## 2. Exact conditional factorization

### Lemma 2.1

Conditioned on `M`, put

\[
 P_U=M^{-1}\!\left(I\cap\binom U{q+1}\right),
 \qquad Y_U=|P_U|=\left|I\cap\binom U{q+1}\right|.
\tag{2.1}
\]

Then

\[
 X_{j,U}=|A_j\cap P_U|
\tag{2.2}
\]

has the hypergeometric law with population size `m`, marked population
`Y_U`, and sample size `m_j`.  In particular,

\[
 \mathbb E[X_{j,U}\mid M]=p_jY_U.
\tag{2.3}
\]

#### Proof

The old part of `M` is a bijection from `L` to `I`, so (2.1)--(2.2) are
literal.  Conditional on `M`, the set `P_U` is fixed, while `A_j` is a
uniform `m_j`-subset of `L` because the colouring was chosen independently
and uniformly.  This is exactly the stated hypergeometric law. `square`

### Lemma 2.2 (two-shore conditional factorization)

Put

\[
 K_U=\binom v{q+1},
 \qquad
 Q_U=M^{-1}\!\left(\binom U{q+1}\setminus I\right),
 \qquad
 |Q_U|=K_U-Y_U.
\tag{2.4}
\]

Conditioned on `M`, `Z_(j,U)=|B_j\cap Q_U|` is hypergeometric with mean

\[
                         s_j(K_U-Y_U).
\tag{2.5}
\]

Moreover `X_(j,U)` and `Z_(j,U)` are conditionally independent, and

\[
 \mathbb E[W_{j,U}\mid M]
 =p_jY_U+s_j(K_U-Y_U).
\tag{2.6}
\]

#### Proof

The dummy part of `M` is a bijection from `mathcal D` to `R\setminus I`.
The partition of `mathcal D` is independent of both `M` and the partition
of `L`, so the same argument as Lemma 2.1 gives (2.5) and conditional
independence.  Summing the two conditional means gives (2.6). `square`

## 3. Two-stage Chernoff concentration

The old image set `I` is Strong Rayleigh under the uniform perfect
matching of `J_q`.  Consequently `Y_U` has mean `mu_U` and the usual
Bernoulli Chernoff bounds.  Hypergeometric variables have the same
Chernoff--Bernstein bounds as sampling without replacement.

### Theorem 3.1 (refreshed-colour owner concentration)

There is an absolute constant `c_0>0` such that, for every
`0<delta<=1`,

\[
 \boxed{
 \Pr\{|X_{j,U}-\mu_{j,U}|\ge\delta\mu_{j,U}\}
 \le 4\exp(-c_0\delta^2\mu_{j,U}).}
\tag{3.1}
\]

One may take `c_0=1/24`.

#### Proof

Put `p=p_j`, `mu=mu_U`, and `X=X_(j,U)`.  If `p=0` the assertion is
trivial, so assume `p>0`.  Define the good occupancy event

\[
 \mathcal G=\{|Y_U-\mu|<\delta\mu/3\}.
\tag{3.2}
\]

 Strong-Rayleigh Chernoff concentration gives

\[
 \Pr(\mathcal G^c)
 \le2\exp(-\delta^2\mu/20)
 \le2\exp(-\delta^2p\mu/20).
\tag{3.3}
\]

Indeed, at threshold `delta mu/3`, the Bernstein upper-tail denominator is
at most `2mu(1+1/9)=20mu/9`, while the lower-tail denominator is `2mu`.

On `mathcal G`, equation (2.3) gives

\[
 |pY_U-p\mu|<\delta p\mu/3.
\tag{3.4}
\]

Thus the event in (3.1), together with `mathcal G`, implies

\[
 |X-pY_U|>{2\delta p\mu\over3}.
\tag{3.5}
\]

For `delta<=1`, on `mathcal G` one has `Y_U<=4mu/3`.  The two-sided
hypergeometric Bernstein inequality, conditional on `M`, therefore gives

\[
 \Pr\left(
 |X-pY_U|>{2\delta p\mu\over3}\mid M
 \right)
 \le
 2\exp(-\delta^2p\mu/24).
\tag{3.6}
\]

The deliberately loose constant `1/24` follows by substituting the
threshold from (3.5) into

\[
 2\exp\left(-{t^2\over2(pY_U+t/3)}\right)
\]

and using `p<=1`, `Y_U<=4mu/3`, and `delta<=1`.  Combining (3.3) and
(3.6), and weakening `1/20` to `1/24`, proves (3.1). `square`

### Corollary 3.2 (simultaneous subexponential family)

Let `mathcal T` be any family of colour/owner tests with

\[
 |\mathcal T|\le e^{Cr}.
\tag{3.7}
\]

If every test has

\[
 \delta_{j,U}^2\mu_{j,U}
 \ge48(Cr+\log4),
\tag{3.8}
\]

then, with positive probability, all tests satisfy their relative-error
bounds simultaneously.

#### Proof

Apply Theorem 3.1 and the union bound.  The total failure probability is at
most

\[
 4\exp\!\left(Cr-{1\over24}
     \min_{(j,U)\in\mathcal T}
     \delta_{j,U}^2\mu_{j,U}\right)<1.
\]

`square`

### Theorem 3.3 (complete old-plus-dummy colour concentration)

There is an absolute constant `c_1>0` such that, for every
`0<delta<=1`,

\[
 \boxed{
 \Pr\{|W_{j,U}-\theta_{j,U}|\ge\delta\theta_{j,U}\}
 \le4\exp(-c_1\delta^2\theta_{j,U}).}
\tag{3.9}
\]

One may take `c_1=1/36`.

#### Proof

Suppress `j,U` and put

\[
 p=p_j,\quad s=s_j,\quad K=K_U,\quad
 \mu=\mu_U,\quad\nu=\nu_U=K-\mu,
 \quad\theta=p\mu+s\nu.
\tag{3.10}
\]

If `theta=0`, both colour classes are empty and the assertion is trivial.
Conditioned on `M`, Lemma 2.2 gives conditional mean

\[
 \theta_Y=pY_U+s(K-Y_U)
 =\theta+(p-s)(Y_U-\mu).
\tag{3.11}
\]

The old image `I` is Strong Rayleigh, and its complement is Strong
Rayleigh as well.  Consequently the common deviation
`Y_U-mu=-(K-Y_U-nu)` has a two-sided Bernstein bound with variance proxy

\[
                         \rho=\min(\mu,\nu).
\tag{3.12}
\]

Put `d=|p-s|`.  If `d=0`, then `theta_Y=theta` identically.  If `d>0`,
define

\[
 \mathcal H=
 \left\{|Y_U-\mu|<{\delta\theta\over3d}\right\}.
\tag{3.13}
\]

The elementary inequality

\[
                         \theta\ge d^2\rho
\tag{3.14}
\]

holds: if `p>=s`, then `d^2<=p` and
`theta>=p mu>=d^2 rho`; the case `s>=p` is symmetric.  Apply the
Bernstein bound with `t=delta theta/(3d)`.  If `t<=3rho`, then

\[
 {t^2\over2(\rho+t/3)}
 \ge {t^2\over4\rho}
 \ge {\delta^2\theta\over36}.
\tag{3.15}
\]

If `t>3rho`, the same exponent is at least

\[
 {3t\over4}
 ={\delta\theta\over4d}
 \ge {\delta^2\theta\over4}.
\tag{3.16}
\]

Therefore in both cases

\[
 \Pr(\mathcal H^c)
 \le2\exp(-\delta^2\theta/36).
\tag{3.17}
\]

On `mathcal H`, `|theta_Y-theta|<delta theta/3` and
`theta_Y<=4theta/3`.  Conditional on `M`, the two hypergeometric variables
in Lemma 2.2 are independent; their union is negatively associated and has
mean `theta_Y`.  Its Bernstein bound at threshold `2delta theta/3` gives

\[
 \Pr\left(
 |W_{j,U}-\theta_Y|>{2\delta\theta\over3}\mid M
 \right)
 \le2\exp(-\delta^2\theta/7).
\tag{3.18}
\]

Combine (3.17)--(3.18) and weaken `1/7` to `1/36`.  When `d=0`, omit
`mathcal H`; equation (3.18) alone is stronger. `square`

### Corollary 3.4 (simultaneous complete-colour tests)

For a family `mathcal T` of at most `e^(Cr)` complete colour/owner tests,
if

\[
 \delta_{j,U}^2\theta_{j,U}
 \ge72(Cr+\log4)
 \qquad((j,U)\in\mathcal T),
\tag{3.19}
\]

then with positive probability every test meets its relative-error bound.

#### Proof

The union bound in Corollary 3.2 applies with `1/36` in place of `1/24`.
`square`

## 4. Why this is stronger than the deterministic-colour formulation

For a deterministic colour class `A subset L`, concentration of

\[
 |\{S\in A:M(S)\in\tbinom U{q+1}\}|
\]

is an assignment-within-the-image problem.  The Strong-Rayleigh law of
`I` alone does not determine it.  Lemma 2.1 removes that obstruction
exactly: after uniform independent refreshment, conditioning on the whole
matching turns the remaining statistic into an ordinary hypergeometric
intersection.  Lemma 2.2 and Theorem 3.3 do the same simultaneously for
the independently refreshed start-dummy shore.

No edge-coordinate negative-association assertion is used.  In
particular, the positive correlations on conditional `K_(2,2)` faces of
the perfect-matching polytope do not affect the proof.

## 5. Exact remaining multi-step gate

The theorem closes one interface whenever its colour partition may be
sampled afresh, independently of that interface matching.  It does not
by itself justify such refreshment for a persistent physical chain.

A sufficient multi-step statement is therefore the following.  The
wording includes the quantifiers needed by the probabilistic proof; mere
permission to rename a few compatible histories is not enough.

> **Serial uniform colour-refresh lemma.**  Conditional on every protected
> choice made before a Boolean interface, there is a randomized physical
> relabelling kernel for the complete *unperformed future-role data* on the
> current old vertices and labelled start dummies such that: (i) for the
> required, past-measurable fixed class sizes, its outputs on the two shores
> are mutually independent and exactly uniform among all labelled
> partitions of those sizes; (ii) the next matching can be sampled
> uniformly from `J_q`, independently of both partitions, without violating
> the protected state; (iii) every reassigned future continuation remains
> literally legal; (iv) all already realized targets, residence prefixes,
> named boundaries, sockets, and compiler tickets remain fixed; and (v)
> after the interface the same assertion is available at the next level.

Under that lemma, choose both refreshed shore partitions and the uniform
interface matching conditionally and independently at every level.
Theorems 3.1 and 3.3 supply the new one-step colour errors.  Full refresh
eliminates inherited colour--position correlation; equivalently, if the
prior coloured-flow bookkeeping is retained, the exact Boolean factor
`(v-q)/(n-q)<=1/2` contracts its inherited owner error.  A union bound over
all levels and tests, followed by the geometric-error argument in the
coloured Boolean flow theorem, gives the spread top-to-chain lift covered
by that theorem.

Thus, within the refreshed-colour strategy, the surviving obstruction has
changed from

\[
 \text{arbitrary deterministic-colour matching concentration}
\]

to the narrower physical question

\[
 \boxed{\text{can unfinished future roles be refreshed without changing
 the protected past?}}
\]

This theorem makes no claim that the serial uniform refresh exists.  In
particular, a refresh restricted by type-dependent eligibility or by
future named targets is not covered unless it induces the exact uniform
partition and independence asserted above.

## 6. Dependencies

1. `MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`;
2. `MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`;
3. the standard Chernoff bound for negatively associated Bernoulli
   variables and the standard hypergeometric Bernstein bound.
