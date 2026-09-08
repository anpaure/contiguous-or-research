# Recurrent shifted cones in the original arrays under actual short incidence

2026-09-08. Root pure-proof deduction; no computation.
Status: full independent root-helper and task03 audits PASS. These are
ORIGINAL-INDEX array events, not yet physical shifted births or eligible
virtual intervals.

## 1. Setting and the precise accepted inputs

Let D be a Dyck root of semilength r, with pruning sizes r_s, height h,
and original inverse-pruning rows Z_s. Put

    H=floor(c sqrt(r)), c>0 fixed,
    F0={GOOD,T<=H,Z_(0,0)=0},
    mu0=E_D[(T+2)1_F0]=Theta_c(1).

The actual incidence law first weights the original uniform Dyck law by
(T+2)1_F0/mu0, then chooses j uniformly in {0,...,T+1}. The row labels
are persistent original labels, not positions in a newly rooted state.
Write

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2),
    F_S=sum_(s=0)^(S-1) sum_(u=0)^s Z_(s,-u).

The following previously proved inputs are used explicitly.

1. [Finite-layer incidence fibre](../../c69c/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md): on a profile with h>=2S, p_s>2H+1 and p_s>=2(s+1) for s<S, fix the entire profile, all original rows of index at least S, and j. Conditional on F_S=0 and a feasible environment, rows s<S are independent uniform weak compositions of ell_s into p_s-s-1 free coordinates, their s+1 base-triangle coordinates being zero. No lifetime constraint on a free coordinate remains.
2. [Actual safe-depth and zero-triangle bounds](PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md), Section6: the preceding profile domain and F_S=0 have actual incidence probability at least 1-C_c S^2/r-C_c exp(-b_c r/S^2), for deterministic 1<=S<=sqrt(r), by restricting to the stated safe-depth event.
3. [Original one-depth concentration](PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md), Section2: for every s and x>=0,

       P_D(|r_s-r/(s+1)|>(4+x)sqrt(r))<=2exp(-x^2/6).

The first input was fully read by root and passed a separate full clock,
measurability, composition, and incidence audit. The other inputs are
already accepted. The deduction below requires no new dynamic law.

## 2. Fixed original free coordinates have a stable product limit

Fix S>=1 and finitely many distinct nonbase coordinates in each row
s<S. On the actual incidence law, all of their values jointly converge
in total variation to independent random variables G_(s,i) with

    P(G_(s,i)=a)=(1-q_s)q_s^a, a=0,1,...,
    q_s=1/(s+2)^2.                                  (1)

Coordinates in the base triangle have limiting value zero. The free
product limit is also stable relative to the exposed environment: the
mean, over feasible environments, of the conditional total-variation
distance from the fixed law (1) tends to zero.

Proof. The marginal root density under incidence is at most C_c sqrt(r).
Input3 therefore implies, for every fixed finite set of depths,

    r_s/r -> 1/(s+1)

in actual incidence probability. For example take deviations r^(3/4):
the original failure probability is exp(-Omega(sqrt(r))), and the extra
sqrt(r) factor is harmless. Thus uniformly on a set of incidence
probability tending to one, for each fixed s<S,

    p_s/r -> 2/(s+2),
    ell_s/r -> 2/[(s+1)(s+2)(s+3)],
    ell_s/(ell_s+p_s-s-1) -> 1/(s+2)^2.              (2)

The safety and zero-triangle exception in Input2 is o(1) for fixed S.
Now use the EXACT conditional fibre, not an unconditioned product law.
Put P=p_s-s-1 and ell=ell_s. For m fixed distinct free coordinates with
specified values a_1,...,a_m, whose sum is a, stars and bars gives

    P(Z_1=a_1,...,Z_m=a_m | environment,F_S=0)
      = binom(ell-a+P-m-1,P-m-1)/binom(ell+P-1,P-1). (3)

For all sufficiently large r the displayed parameters are positive;
the probability is zero if a>ell. Along every sequence satisfying (2),
the ratio (3) tends to (1-q_s)^m q_s^a. Its limiting masses sum to one,
so pointwise convergence on this countable state space implies total-
variation convergence: first restrict to a finite set with limiting
mass close to one, then bound the complementary mass in both laws.
This reasoning is uniform on shrinking typical-profile sets, or else
a violating parameter sequence would contradict the same limit.
Conditional row independence proves the assertion for all queried rows.
The atypical and infeasible-environment masses are o(1). This proves
the mean conditional TV assertion and its unconditional consequence.

The exposed environment itself need NOT have its original unweighted
law. In particular (1) is not an independent model for a reached root.

The new [initial-P-run estimate](../../../contextual/c69c/research_round1/pbbs_initial_p_run_incidence_divergence.md)
has a useful compatibility consequence. For any deterministic
m_r=o(r^(1/4)), adding the restriction p0>m_r does not change the
UNCONDITIONAL finite-coordinate limit (1). Its complement has actual
incidence probability at most C_c(m_r+1)^2/sqrt(r)=o(1); intersecting
any event changes its probability by at most this amount, and
conditioning divides by a probability tending to one. Thus finite
free-gap randomness persists even on long-initial-P bases. This does
not assign an unchanged conditional law at each individual environment
after the extra restriction, or itself prove a physical misalignment.

## 3. Shifted array cones and their exact limiting joint law

For an integer d>=0 define the depth-S ORIGINAL-INDEX cone event

    Q_S^(r)(d)=1{Z_(s,-d-u)=0 for 0<=s<S, 0<=u<=s}. (4)

Indices are cyclic at their row. For each fixed finite collection of
d's and S, the relevant indices are distinct as ordinary integer
indices modulo p_s for all sufficiently large typical profiles. On
exceptional roots without these rows define the indicator to be zero;
Input2 makes that convention asymptotically irrelevant. The base d=0
cone has probability tending to one under actual F0 incidence.

Fix 0=d_0<d_1<...<d_k and write g_j=d_j-d_(j-1). The limiting joint
probability of all their cones is

    lim_(r->infinity) P_inc(Q_S^(r)(d_j)=1 for j=0,...,k)
      = product_(j=1)^k u_(g_j,S),                  (5)

where

    u_(g,S)=product_(s=0)^(S-1)
             [ (s+1)(s+3)/(s+2)^2 ]^min(g,s+1).    (6)

Indeed, in row s each cone uses an integer interval of s+1 coordinates.
Adding these equal-length intervals in increasing d order adds exactly
min(g_j,s+1) NEW coordinates at its jth addition. The base interval is
already forced to zero. All newly requested coordinates are free, so
(1) gives (5)-(6), including coincidences between cones. Neither cones
nor their indicators have been declared independent.

For g<=S the product telescopes exactly to

    u_(g,S)=1/(g+1) * [(S+2)/(S+1)]^g.              (7)

One quick verification divides the product for g by the product for
g-1. The ratio is the tail product over s>=g-1, namely
g(S+2)/[(g+1)(S+1)]. Multiplying these ratios for g=1,... gives (7).
For g>S the product is the same as for g=S. In particular

    lim_(S->infinity) u_(g,S)=1/(g+1)               (8)

for every fixed positive g.

## 4. The infinite-array cone process is a recurrent renewal process

Construct independent G_(s,i) on all free original integer coordinates,
with law (1), and set the base cone coordinates to zero. Let Q_S(d)
be the corresponding event (4), and Q_infinity(d)=inf_S Q_S(d).
For every fixed finite collection of d's, monotone convergence and
(5)-(8) give

    P(Q_infinity(d_j)=1 for j=0,...,k)
      =product_(j=1)^k 1/(g_j+1).                  (9)

These are the joint indicators of a proper recurrent renewal process
started at zero. For completeness, put u_n=1/(n+1) and

    U(z)=sum_(n>=0)u_n z^n=-log(1-z)/z,
    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt.

For n>=1 the coefficient

    f_n=-integral_0^1 (-1)^n binom(t,n)dt

is nonnegative: binom(t,n) has sign (-1)^(n-1) for 0<t<1. Also f_0=0
and F(1-)=1, so the f_n form a probability distribution on positive
finite integers. The renewal process with iid increments of this law
has mass sequence u_n, because 1/(1-F)=U. Regeneration gives exactly
(9). Finite inclusion-exclusion determines the law of every finite
binary indicator vector from these joint probabilities. Hence it is
the law of Q_infinity. Almost surely its number R_L of renewals in
{0,...,L} tends to infinity: every fixed finite number of its positive,
almost surely finite increments has a finite sum.

The auxiliary construction also bounds finite-depth errors. For S>=L,
the probability that any Q_S(d) differs from Q_infinity(d), 1<=d<=L,
is at most

    sum_(d=1)^L [u_(d,S)-1/(d+1)] <= C L/(S+1).     (10)

Use (7) and e^x-1<=C x for 0<=x<=1. This is a bound in the limiting
independent ORIGINAL array model; it does not assert a growing-r
uniform approximation to that model.

## 5. Actual incidence has many array cones in an iterated limit

For fixed L, use S=L in (4). Section2 gives convergence of the finite
indicator vector under actual F0 incidence to (Q_L(d))_(d=0)^L.
In the auxiliary coupling Q_L(d)>=Q_infinity(d), coordinatewise.
Consequently, for every fixed integer M>=0,

    limsup_(r->infinity)
      P_inc(sum_(d=0)^L Q_L^(r)(d)<=M)
        <=P(R_L<=M).

Let L tend to infinity. We obtain the unconditional actual-incidence
ARRAY conclusion

    lim_(L->infinity) limsup_(r->infinity)
      P_inc(sum_(d=0)^L Q_L^(r)(d)<=M)=0.            (11)

A diagonal choice gives some L_r tending to infinity arbitrarily
slowly, with L_r=o(sqrt(r)), for which the cone count diverges in
actual incidence probability. No quantitative rate in r is claimed.
For the diagonal, apply (11) successively with M=1,2,... and errors
tending to zero, taking each r threshold after the fixed-L limit; it
may also be increased to enforce any prescribed diverging upper bound
on L_r. The particular finite diagonals can be chosen increasing.

## 6. The missing physical interface is not part of this theorem

An array index d in (4) has NOT been identified with physical birth d.
At a physical time t, the queried initial label at level s is determined
by the reached selection cocycle at that level. These labels need not
all equal -d, and may depend on the free rows whose zeros appear in (4).

Even if the starting labels aligned, finite-depth zero clocks alone
do not show that their deeper C^S T remainder meets T<=H or that their
repair interval covers the sampled offset j. Those are separate clock
transport and endpoint assertions. The recent long initial P-run lemma
does not supply them by itself; bounded-gap one-neighbor amplification
also warns against a uniform deterministic endpoint comparison.

Thus (11) is NOT k0 divergence, occupied support o(W), a physical
packing theorem, or coefficient one. It supplies the recurrent random
array structure under the correct short-incidence law. To use it, one
must map enough of these cone events to distinct eligible ORIGINAL F0
partner labels through exact physical dynamics. No shifted cone test
has been added to the definition of the target partner family F0.
