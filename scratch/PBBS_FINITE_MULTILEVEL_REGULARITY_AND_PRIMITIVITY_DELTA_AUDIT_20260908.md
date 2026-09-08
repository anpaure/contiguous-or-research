# A finite multilevel regularity and primitivity bound with the proposed constants

Date: 2026-09-08. Independent pure-proof audit by exact_b_finite_frontier.
No mathematical program, word construction, or numerical search was run.

Verdict: the displayed finite probability bound passes with its stated
constants. The expectation bias is bounded from the exact finite pruning
census, not by replacing it with its limiting harmonic profile.

Let n=2r+1 be odd, let L>=0 be an integer, put d=L+3, and assume

    n>=4096d^6.

For a uniform original Dyck root let n_j=2a_j+1 be the physical
circumference after j pruning rounds. Define

    tau=n/(16d^3),
    delta_1=2(L+1)n(n+1)exp[-n/(2048d^6)],
    delta_2=Ln*2^[-n/(6d^3)],
    delta=delta_1+delta_2.                                (1)

Except on an event of probability at most delta, simultaneously:

* |n_j-n/(j+1)|<=tau for every 1<=j<=L+1;
* all first L original incoming-gap rows are primitive;
* for 0<=s<L, ell_s>=n/(2d^3) and p_s>=n/(2d);
* a_j>=r/[2(j+1)] for every 0<=j<=L+1.

No numerical threshold or hidden asymptotic qualifier is needed beyond
the displayed n>=4096d^6. As usual, a probability majorant that exceeds
one remains a valid bound.

## 1. The exact fair-bit census controls its bias uniformly in depth

Start with n independent fair bits on a labelled odd cycle. Let N_j
be its size after j equality-pruning rounds. The exact finite census is

    E N_j = n/(j+1) sum_(q=0)^j cos^(n-1)(pi q/(j+1)).    (2)

It is valid at every depth j, including after many words have reached
their one-site bottom. Formula (2), its marked-renewal derivation, and
the depth-uniform edit bound are proved in
`PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md`, Sections 2-5.

For j>=1 pair the cosine terms near zero and pi. The inequality
cos t<=exp(-t^2/2) on [0,pi/2] gives, with
c=(n-1)pi^2/[2(j+1)^2],

    0<=E N_j-n/(j+1)
       <=2n/(j+1) sum_(q>=1)exp(-c q^2)
       <=2n/(j+1) integral_0^infinity exp(-c x^2) dx
       =n sqrt(2/[pi(n-1)])
       <=2sqrt(n).                                      (3)

The sum-to-integral step uses monotonicity of the nonnegative Gaussian
integrand. The final inequality holds for every n>=3; for instance
pi>=2 and n/(n-1)<=3/2 already imply it. At j=0 the bias is exactly
zero. Thus (3) is a fully finite all-depth estimate.

From n>=4096d^6 one has sqrt(n)>=64d^3, whence

    2sqrt(n)<=n/(32d^3)=tau/2.                           (4)

This establishes the required bias allowance with precisely the proposed
constant; no approximation to the expectation has been substituted.

## 2. Bounded differences and exact root-conditioning cost

Flipping one original bit changes every N_j by at most two. For j>=1,
the first equality-pruning image changes by at most two insertions or
deletions, and further equality pruning does not increase this edit
distance. Exposing the independent input bits therefore gives

    Pr_iid(|N_j-E N_j|>u)<=2exp(-u^2/(2n)).               (5)

The event |N_j-n/(j+1)|>tau, together with (3)-(4), forces
|N_j-E N_j|>tau/2. Consequently (5) implies

    Pr_iid(|N_j-n/(j+1)|>tau)
       <=2exp[-tau^2/(8n)]
       =2exp[-n/(2048d^6)].                             (6)

The event that the fair-bit word is exactly 0D for a Dyck root D has
probability Cat_r/2^n. The central-binomial averaging bound yields

    Cat_r/2^n>=1/[n(n+1)].                              (7)

Conditional on that event, D is uniform. Equality pruning of 0D has
N_j=2a_j+1=n_j. Union-bound (6) over the L+1 tested depths and divide
by the lower bound (7). This proves

    Pr_D(exists 1<=j<=L+1: |n_j-n/(j+1)|>tau)
       <=delta_1.                                      (8)

No independence across depths is asserted or needed.

## 3. Deterministic row and semilength bounds on the regular event

Assume the complement of the event in (8), and set n_0=n exactly.
For 0<=s<L,

    ell_s=(n_s-2n_(s+1)+n_(s+2))/2,
    p_s=n_(s+1).

The centered second difference in ell_s is

    n/[(s+1)(s+2)(s+3)]>=n/d^3.

The total error after division by two is at most 2tau. Therefore

    ell_s>=n/d^3-2tau=7n/(8d^3)>=n/(2d^3).               (9)

Similarly,

    p_s>=n/(s+2)-tau>=n/d-tau>=n/(2d).                  (10)

The domain implies n>=4d. It follows from (10) that

    p_s-1>=n/(2d)-1>=n/(4d)>=n/(4d^3).

Together with (9), this gives the useful integer-size parameter

    m_s=min(ell_s,p_s-1)>=n/(4d^3).                     (11)

In particular all tested cores are nonempty and the p_s are odd and
greater than one; a zero row or a one-part row cannot be hidden in
this regular sector.

For the requested semilength bound, put u=j+1<=L+2<d. Regularity gives

    a_j=(n_j-1)/2 >=(n/u-tau-1)/2.

This is at least (n-1)/(4u)=r/(2u), because

    2u tau+2u <= n/(8d^2)+2d <= n/8+n/2 < n+1.          (12)

Here u<=d and n>=4d were used. The case j=0 is immediate from a_0=r.
Thus a_j>=r/[2(j+1)] on the entire claimed range.

## 4. Exact composition repetition count gives the second error term

Condition on any full original pruning profile in the regular sector.
The original row s is uniform among weak compositions of ell_s into
p_s odd parts, by the exact original inverse-pruning law. Let

    D_s=binom(ell_s+p_s-1,p_s-1).

A nonprimitive cyclic row is a j-fold repetition for a divisor j>=3
of p_s. If j does not divide ell_s, it is impossible. Otherwise the
number D_(s,j) of repeated rows is

    D_(s,j)=binom(ell_s/j+p_s/j-1,p_s/j-1).

Concatenating j independently chosen short compositions injects
D_(s,j)^j possibilities into the D_s full compositions. Hence

    D_(s,j)/D_s <= D_s^(-(j-1)/j)<=D_s^(-2/3).

There are at most p_s choices of j, so

    Pr(row s nonprimitive | profile)<=p_s D_s^(-2/3).    (13)

With m_s from (11), monotonicity of binomial coefficients and the
one-from-each-pair injection give

    D_s>=binom(2m_s,m_s)>=2^m_s.

Since p_s<=n, (11)-(13) imply

    Pr(row s nonprimitive | profile)
       <=n*2^[-n/(6d^3)].                              (14)

Union-bound over the first L rows and then integrate over the regular
full profiles. The bound is uniform, so the resulting probability is
at most delta_2. The same conclusion is immediate when L=0, whose
primitive-row event is empty. No primitive-conditioned profile law or
independence between these row-failure events is used.

Combining this estimate with (8) proves (1) and all the stated finite
consequences. The row law and its physical interpretation are linked in
`PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`,
Section 5.

## 5. Audit scope

The exact constants 4096, 2048, 16, and 6 all survive the finite proof.
No repair to the proposed delta expression is required. This note supplies
the original-profile probability estimate and deterministic regular-sector
inequalities. The further use of this event in a period average, a divisor
sum, or a universal-word error formula is a separate deduction; it is not
assumed in proving this probability bound.
