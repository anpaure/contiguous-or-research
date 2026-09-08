# Cohort-stable multinomial Laplace induction for Boolean interfaces

**Date:** 2026-08-05  
**Method:** pure mathematics; no search, solver, or H100 computation  
**Status:** unconditional probabilistic theorem for an unconditioned chain
of uniform augmented Boolean matchings and past-measurable uniform
transition refinements.  It closes the newborn-versus-persistent
**concentration** bridge.  It does not prove that all literal future roles
are physically interchangeable, or that protected conditioning preserves
the required matching law.

## 1. Multinomial Laplace domination

Let `Omega` be a finite set of size `m`.  A random labelled partition

\[
 \Omega=C_1\mathbin{\dot\cup}\cdots
             \mathbin{\dot\cup}C_s,
 \qquad |C_i|=m_i,
 \qquad p_i={m_i\over m},                        \tag{1.1}
\]

has **multinomial Laplace domination**, abbreviated `MLD`, if for every
deterministic `B subset Omega` and every real vector
`theta=(theta_1,...,theta_s)`,

\[
 \boxed{
 \mathbb E\exp\!\left(\sum_i\theta_i|C_i\cap B|\right)
 \le
 \left(\sum_i p_i e^{\theta_i}\right)^{|B|}.}   \tag{1.2}
\]

The right side is the Laplace transform obtained by colouring the points
of `B` independently with probabilities `(p_i)`.  Thus MLD says that the
actual fixed-size cohort partition is no more dispersed than the
corresponding independent multinomial experiment.

A one-class partition is MLD with equality.  A uniform labelled partition
with fixed class sizes is MLD by Lemma 2.1 below.

## 2. Uniform refinements preserve MLD

### Lemma 2.1 (fixed-population sampling bound)

Let a population of size `M` contain `n_j` objects of weight
`w_j>0`, with `sum_j n_j=M`.  If `Y` objects are sampled uniformly without
replacement, then

\[
 \mathbb E\prod_{x\text{ sampled}}w_x
 \le
 \left({\sum_jn_jw_j\over M}\right)^Y.          \tag{2.1}
\]

#### Proof

The left side is

\[
 {e_Y(w_1,\ldots,w_M)\over\binom MY},
\]

where the weights are repeated according to their multiplicities.
Maclaurin's inequality for elementary symmetric means gives (2.1).
`square`

### Theorem 2.2 (cohortwise transition refinement)

Suppose `(C_i)_(i<=s)` is MLD.  For every `i`, fix nonnegative integers
`n_(ij)` with row sum `m_i`.  Conditional on `(C_i)`, independently choose
a uniform labelled refinement

\[
 C_i=C_{i1}\mathbin{\dot\cup}\cdots
               \mathbin{\dot\cup}C_{it},
 \qquad |C_{ij}|=n_{ij},                         \tag{2.2}
\]

and forget the old labels:

\[
 D_j=\bigcup_iC_{ij}.                            \tag{2.3}
\]

Then `(D_j)_(j<=t)` is MLD with proportions

\[
 p'_j={1\over m}\sum_i n_{ij}.                  \tag{2.4}
\]

Zeros in `(n_(ij))` are allowed.

#### Proof

Fix `B` and `(theta_j)`, and put `Y_i=|C_i cap B|`.  Conditional on
`(C_i)`, the `Y_i` points of `B cap C_i` see a multivariate
hypergeometric sample from a population containing `n_(ij)` copies of
weight `e^(theta_j)`.  Lemma 2.1 gives

\[
 \mathbb E\!\left[
 e^{\sum_j\theta_j|D_j\cap B|}\mid(C_i)
 \right]
 \le\prod_i a_i^{Y_i},
 \qquad
 a_i={1\over m_i}\sum_jn_{ij}e^{\theta_j}.      \tag{2.5}
\]

Use MLD for the old partition with real parameters `log a_i`:

\[
 \mathbb E\prod_i a_i^{Y_i}
 \le\left(\sum_i p_i a_i\right)^{|B|}
 =\left(\sum_jp'_je^{\theta_j}\right)^{|B|}.   \tag{2.6}
\]

This is exactly MLD for `(D_j)`. `square`

This theorem strictly extends exact uniform transition refresh.  The
input need not be a globally uniform partition; it may contain arbitrarily
many nonexchangeable birth cohorts, provided their joint law has MLD.

## 3. The old-image Bernoulli transform

Consider the augmented Boolean interface

\[
 L=\binom{[n]}q,
 \qquad
 R=\binom{[n]}{q+1},
 \qquad
 m=|L|,
 \qquad
 N=|R|,                                          \tag{3.1}
\]

with `N-m` universal dummies.  Let `M` be a uniformly random perfect
matching, independent of the input cohort partition on `L`.  Let

\[
 I=\{T\in R:T\text{ is matched to an old vertex}\},
 \qquad D=R\setminus I.                          \tag{3.2}
\]

The old-image theorem says that `I` is Strong Rayleigh and has uniform
one-point marginal

\[
 \lambda={m\over N}={q+1\over n-q},
 \qquad \delta=1-\lambda.                        \tag{3.3}
\]

### Lemma 3.1 (all-real Bernoulli Laplace bound)

For every deterministic `B subset R` and every real `tau`,

\[
 \boxed{
 \mathbb E e^{\tau|I\cap B|}
 \le(\delta+\lambda e^\tau)^{|B|}.}             \tag{3.4}
\]

#### Proof

Specialize the real-stable generating polynomial of `I` by setting every
variable in `B` equal to `z` and every other variable to one.  The
resulting univariate probability generating polynomial has only real
nonpositive zeros.  It therefore factors as the generating polynomial of
a sum of independent Bernoulli variables with parameters
`rho_1,...,rho_|B|`.  Their sum is

\[
 \sum_j\rho_j=\mathbb E|I\cap B|=\lambda|B|.
\]

For `a=e^tau-1>-1`, concavity of `x -> log(1+ax)` gives

\[
 \prod_j(1+a\rho_j)
 \le(1+a\lambda)^{|B|},
\]

which is (3.4).  This argument works for positive and negative `tau`.
`square`

## 4. Boolean transport adds a newborn cohort without weakening MLD

### Theorem 4.1 (cohort-stable Boolean transport)

Let

\[
 L=C_1\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}C_s
\]

be an MLD partition, independent of `M`, with proportions `p_i`.  Transport
the old cohorts and add the newborn cohort:

\[
 C'_i=M(C_i)\quad(1\le i\le s),
 \qquad
 C'_0=D.                                         \tag{4.1}
\]

Then `(C'_0,C'_1,...,C'_s)` is MLD on `R`, with proportions

\[
 p'_0=\delta,
 \qquad
 p'_i=\lambda p_i.                               \tag{4.2}
\]

#### Proof

Fix `B subset R` and real parameters `theta_0,...,theta_s`.  Conditional
on `M`, put

\[
 P_B=\{S\in L:M(S)\in B\},
 \qquad Y=|P_B|=|I\cap B|.                       \tag{4.3}
\]

The old partition is independent of `M`, so its MLD inequality applies to
the now deterministic set `P_B`:

\[
 \mathbb E\!\left[
 e^{\sum_{i>=1}\theta_i|C'_i\cap B|}\mid M
 \right]
 \le a^Y,
 \qquad a=\sum_{i>=1}p_i e^{\theta_i}.           \tag{4.4}
\]

Since `|D cap B|=|B|-Y`, including the newborn weight gives

\[
 \mathbb E e^{\sum_{i>=0}\theta_i|C'_i\cap B|}
 \le e^{\theta_0|B|}
      \mathbb E e^{(\log a-\theta_0)Y}.          \tag{4.5}
\]

The parameter in the last expectation may have either sign.  Lemma 3.1
applies and yields

\[
\begin{aligned}
 e^{\theta_0|B|}
 \left(\delta+\lambda a e^{-\theta_0}\right)^{|B|}
 &=\left(
   \delta e^{\theta_0}
   +\sum_{i>=1}\lambda p_i e^{\theta_i}
   \right)^{|B|}.
\end{aligned}                                    \tag{4.6}
\]

This is exactly the MLD inequality with the proportions in (4.2).
`square`

No uniformity of the newborn set is asserted or needed.  Its Strong-
Rayleigh complement relation to `I` is precisely what makes the two-cohort
Laplace transform close.

## 5. Arbitrarily many births and sparse state transitions

### Theorem 5.1 (serial cohort-stable induction)

Start with the one-class partition of a complete Boolean rank.  Repeat any
finite sequence of the following operations:

1. a cohortwise uniform transition refinement with integer counts fixed in
   advance (or determined only by deterministic class-size data, not by
   realised cohort positions), followed by arbitrary merging of output
   labels;
2. an independent uniform augmented Boolean perfect matching, transporting
   every old class and adding the dummy image as one new class.

At every time, the complete current partition is MLD.

#### Proof

The initial partition is MLD.  Theorem 2.2 preserves MLD under every
transition refinement and merge.  Theorem 4.1 preserves it under every
Boolean transport and newborn insertion.  Induction proves the claim.
`square`

The number of cohorts never enters the inequality.  In particular the
theorem applies through `O(sqrt(r))` ranks even if one retains every birth
rank, every residence age, and every unfinished future-role state as a
separate label.

## 6. Exact Chernoff consequence

Let `J` be any union of current labels and set

\[
 C_J=\bigcup_{j\in J}C_j,
 \qquad p_J={|C_J|\over|\Omega|}.
\]

In the MLD inequality set `theta_j=theta` on `J` and zero elsewhere.
Then, for every deterministic `B subset Omega` and every real `theta`,

\[
 \boxed{
 \mathbb E e^{\theta|C_J\cap B|}
 \le(1-p_J+p_Je^\theta)^{|B|}.}                 \tag{6.1}
\]

Thus `|C_J cap B|` has the exact binomial benchmark

\[
 \mu=p_J|B|                                      \tag{6.2}
\]

and the standard Chernoff--Bernstein bounds

\[
 \Pr(X\ge\mu+t)
 \le\exp\!\left(-{t^2\over2(\mu+t/3)}\right),
 \qquad
 \Pr(X\le\mu-t)
 \le\exp\!\left(-{t^2\over2\mu}\right).       \tag{6.3}
\]

For Boolean owner tests take

\[
 B=\binom Uq.
\]

Consequently every cohort union, state union, or future-role aggregate
has concentration about its exact uniform benchmark, simultaneously at
every rank after a union bound.  If the total number of tests over all
`O(sqrt(r))` ranks is at most `e^(Cr)`, the usual condition

\[
 \delta_T^2\mu_T\ge 4(Cr+\log 2+\omega(1))      \tag{6.4}
\]

for the Bernstein-scale version makes all tests pass with positive
probability.  The additional `O(sqrt(r))` birth cohorts cost no factor in
the exponent and no additive accumulation term.

This is stronger than a geometric-error recurrence: at every rank the
entire cohort partition satisfies the same one-shot binomial Laplace bound.

## 7. Whole future roles after an uncoloured path cover

The theorem supports the following proof order.  Sample the uncoloured
Boolean interfaces independently.  Carry only physically forced cohort or
automaton labels through the matchings.  Whenever a cohort has a fixed
menu of still-unperformed whole future roles, assign those roles by a
uniform fixed-size refinement inside that cohort.  Theorem 2.2 preserves
MLD, so every union of assigned roles has the owner-wise Chernoff bound
(6.3).

This post-colouring interpretation is legitimate only when all members of
the refined cohort have the same literal eligibility menu and assigning a
role does not modify the already exposed path.  If eligibility depends on
the realised individual path, named target, socket, or protected
occurrence, merely splitting into eligibility classes is **not** covered:
that geometry-dependent split need not be MLD.  It needs a separate proof
that the eligibility partition is itself produced by an MLD-preserving
operation.  In particular, refining to singletons destroys the useful
randomization and generally fails (1.2).

## 8. Exact remaining boundary

The theorem removes the following proposed obstruction:

\[
 \boxed{\text{newborn cohorts do not destroy Chernoff concentration and
 do not accumulate an }O(\sqrt r)\text{ error.}}
\]

It does **not** remove these physical or integral gates:

1. **Protected conditioning.**  The next interface matching is required to
   be an independent uniform matching of the full augmented Boolean
   graph.  Conditioning on prescribed edges, sockets, or endpoints may
   destroy the uniform old-image marginals used in Lemma 3.1.
2. **Eligibility.**  Transition counts must be fixed independently of
   realised positions before the next matching, and refinements must be
   uniform among literally interchangeable objects.
3. **Exact target-once assignment.**  MLD gives simultaneous spread
   inequalities; it does not itself solve the later Rado/interval-chain
   matching or common-cap compiler.
4. **Small means.**  A cohort or role whose relevant owner mean is only
   `O(r)` may not beat an `e^(Theta(r))` union without additional exact or
   deterministic handling.

Within these boundaries, the formerly open cohort-stable coloured Boolean
concentration theorem is complete.

### Proposition 8.1 (geometry-adaptive splitting can destroy MLD)

The eligibility warning is necessary.  Start from the one-class partition
of `Omega`, fix a nonempty proper set `B subset Omega`, and split
deterministically into

\[
 D_1=B,
 \qquad D_2=\Omega\setminus B.                  \tag{8.1}
\]

For the test set `B` itself and any `theta>0`, the left side of MLD is

\[
 e^{\theta|B|},
\]

whereas the proposed independent benchmark is

\[
 \left({|B|\over|\Omega|}e^\theta
       +1-{|B|\over|\Omega|}\right)^{|B|}
 <e^{\theta|B|}.                                 \tag{8.2}
\]

Thus an eligibility class chosen from realised geometry need not satisfy
even the first MLD inequality.  Uniform refinement among a predeclared
interchangeable cohort is substantive, not cosmetic.

## 9. Dependencies

1. `MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`.
2. `MATH_THEOREM_UNIFORM_PARTITION_TRANSITION_REFRESH_AND_BIRTH_GATE_20260805.md`.
3. The elementary Maclaurin inequality for symmetric means.
