# Exact stationary PBBS lifetime and residual-life identities

Date: 2026-09-07. Pure proof; no computation or enumeration.

The main result is a finite stationary marked-Dyck permutation and its exact
return-section identities. Uniform newborn lifetime has mean r, even after
conditioning on height. Uniformly sampling an existing up-step gives a
different, length-biased law. None of these identities assumes Q6, independent
renewal increments, mixing, or a local central limit theorem.

## 1. Sources, prior overlap, and conventions

Read-only sources inspected:

- PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Sections 1, 3, 4, 8, 9;
- MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md,
  Sections 1 and 2;
- PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md, including the full-label
  consequence of componentwise homomesy;
- MATH_THEOREM_PBBS_ST_EXACT_ADDITIVE_RENEWAL_AND_TWO_TIME_CENSUS_20260726.md,
  Section 1;
- MATH_THEOREM_PBBS_ST_EXACT_RENEWAL_THRESHOLD_AND_TWO_POINT_KERNEL_20260726.md;
- PBBS_TWO_DIMENSIONAL_RENEWAL_LOCAL_CLT_GATE_20260725.md.

The run-length shift and occupation census are already explicit in the
exact run-spectrum source. The identities below reorganize them into a
marked-Dyck stationary object. No novelty claim is made for the general
finite renewal/occupation counting principle.

Fix r>=1 and n=2r+1. Let f be the PBBS permutation on rank-r subsets,
g=f^2, phi its rooted-Dyck quotient, and tau=phi^2. Write D=P1R0S for the
first-maximum factorization. Then

    tau(D)=S 1_new P 0 R.                                  (1)

The old first-maximum up-step is consumed, the new divider is planted,
and the other up-steps keep their coordinate identities.

T(D) counts the subsequent g updates from immediately after planting in
(1) through the consuming update. It equals the number of rank-r owner
states in that positive coordinate run. In particular a mountain of
height r has T=r. This is the convention used in the corrected conservation
identity in pbbs_q6_independent_audit.md.

## 2. Why there are no permanent coordinates here

The PBBS-specific input used in this section is the already audited
full-label property: on any f component of length L, each coordinate
occurs L/n>0 times in its omitted-label word. It is stated in the
residence-reduction source, Section 1, and independently used in the
run-spectrum source's componentwise homomesy census.

Consecutive occurrences of a label have odd cyclic separation. If L is
odd, the step-two cycle visits the whole f component, so every coordinate
is inserted and deleted on that g cycle. If L is even, occurrences of
each coordinate alternate between the two parities. Their positive total
number is consequently even, and both parities contain occurrences.
Again each of the two g cycles has an insertion and deletion of every
coordinate. Thus no coordinate is permanently present or permanently
absent on any g component. The same holds after complementation.

This hypothesis cannot be omitted for a general Johnson cycle. A permanent
core contributes occupation but no births. On a rank-r cycle with a
permanent core of size c, counting only born runs gives mean lifetime
r-c, not r. The permanent-core examples in short_trade_core_obstruction.md
therefore do not obey the PBBS mean identity.

## 3. A finite stationary marked-Dyck permutation

Let Omega be any nonempty tau-invariant set of semilength-r Dyck roots.
Examples include one tau orbit, all roots of one specified height, all
roots, or a union remaining after deletion of complete short tau cycles.
An arbitrary noninvariant class, such as the primitive roots, is not an
admissible conditioning class for the claims below.

Define the finite state space

    M_Omega={(D,j): D in Omega, j is an up-step position of D}.

It has r|Omega| states. Under (1), transport a retained marked up-step
with its block. If the mark is the consumed first-maximum up-step, reset
the mark to the newly planted divider. This defines a permutation F of
M_Omega: tau is a permutation of Omega, and at each update the retained
up-steps map bijectively to retained up-steps, while the consumed step
maps bijectively to the new one.

Let B_Omega be the image under F of the first-maximum marked states.
This birth section has exactly one marked state above each D, hence
|B_Omega|=|Omega|. Its marked position above D is the new divider planted
by the transition from tau^(-1)D.

Every marked orbit hits B_Omega. Otherwise its mark would survive forever
without being consumed. Lifting the finite rooted orbit to the finitely
many physical spatial phases would give a permanent coordinate on a g
component, contrary to Section 2.

The F orbit from one birth-section visit to its next visit follows one
physical marked coordinate until consumption, then resets it. Its return
time is exactly T(tau^(-1)D). Since tau permutes Omega, uniform sampling
of B_Omega gives the same lifetime distribution as uniform D in Omega.
The uniform measure on M_Omega is stationary, but successive return times
need not be independent.

## 4. Exact mean lifetime, including height conditioning

Each state of M_Omega lies in exactly one excursion from the birth section
to its next visit, with the initial birth state included and the terminal
birth state excluded. Consequently

    sum_(D in Omega) T(D)=r|Omega|,
    E_Omega[T]=r.                                         (2)

Equivalently, the lift to n|Omega| physical states has one birth per edge
and r occupied-coordinate incidences per vertex. With no permanent
coordinates, every incidence belongs to exactly one born run, giving
the same count.

Height is tau-invariant, so in every nonempty height stratum

    E[T | height=h]=r.                                    (3)

Let P_count, R_count, S_count count the nonconsuming P,R,S updates in a
born run. The correct endpoint convention gives

    T=h+2 R_count+S_count.

Thus the exact conditional mean interruption budget is

    E[2 R_count+S_count | height=h]=r-h.                   (4)

This is an expectation identity. It does not imply concentration of T or
of the interruption budget.

## 5. Uniform existing marks: age, residual life, and length bias

Choose D uniformly in Omega and then choose one of its r up-steps
uniformly. This is the stationary uniform measure on M_Omega. Let A>=0
be the age of the current physical mark since its birth, and let R>=1
be the number of future updates through its consumption. Let L=A+R be
the total lifetime of its current run.

Write p_l=P_birth(T=l), with birth law uniform over Omega as in (2).
Each excursion of length l contains exactly one state with (A,R)=(a,b)
for each a>=0,b>=1 satisfying a+b=l. Therefore

    P_stat(A=a,R=b)=p_(a+b)/r.                            (5)

This gives the exact formulas

    P_stat(L=l)=l p_l/r,
    P_stat(R=b)=P_birth(T>=b)/r,
    P_stat(R>=b)=E_birth[(T-b+1)_+]/r,                    (6)
    P_stat(R<=H)=E_birth[min(T,H)]/r <= H/r.               (7)

In particular a uniformly chosen existing up-step has only O(r^(-1/2))
probability of being consumed in the next O(sqrt(r)) updates. This is
fully compatible with a positive fraction of newborn runs having such
short lifetimes: existing marks are sampled with length bias.

The moments are also exact:

    E_stat[R]=(E_birth[T^2]+r)/(2r),
    E_stat[A]=(E_birth[T^2]-r)/(2r).                       (8)

For a concrete unmarked-root statistic, let B_H(D) be the number of the
currently present up-steps that are consumed in the next H updates. Then

    E_D[B_H(D)]=E_birth[min(T,H)] <= H.                    (9)

This supplies a valid finite marked-Dyck transfer target. If
F_H=P_stat(R<=H), F_0=0, then the newborn distribution is recovered exactly
by discrete differences:

    P_birth(T=H)=r(2F_H-F_(H-1)-F_(H+1)),                 (10)
    P_birth(T<=H)=1-r(F_(H+1)-F_H).

Thus approximating the residual distribution coarsely is insufficient
for a sharp newborn count; the differences in (10) are amplified by r.

## 6. Return gaps, complement projection, and repair-edge lengths

On an f component write A_i=f^i(A_0) and lambda_i for its omitted label.
The exact recurrence is

    A_(i+2)=A_i minus {lambda_(i+1)} union {lambda_i}.

If consecutive occurrences of a label have f gap 2t+1, the label's rank-r
positive g run has length t. The paired complement-projected positive
run has length t+1. The dictionary for one gap start is therefore

    f return gap                  2T+1,
    rank-r positive g lifetime    T,
    complement positive lifetime  T+1,
    repair interval edge count    T+2.                    (11)

The last count includes insertion and deletion edges. A projected
residence cutoff H means T+1<=H, equivalently T<=H-1. It does not mean
T<=H, and it does not cut off repair intervals at H edges.

For a phi-invariant Omega, including all roots of a given height, the
complement newborn lifetime law is distributionally T+1 under the same
uniform root law. Its mean is r+1, and its stationary existing-coordinate
law is obtained from (5)-(8) by replacing T by T+1 and r by r+1. For
example,

    P_comp(R=b)=P_birth(T+1>=b)/(r+1).                    (12)

For an arbitrary merely tau-invariant Omega, the same comparison uses
the T law on phi(Omega): on the complement edge at A_i the incoming label
is lambda_(i+1), whose gap starts at f(A_i). This phase shift must not be
silently dropped. Both Omega and phi(Omega) still have mean T=r.

The edge-incidence analogue of length bias weights a gap-start run by
T+2. Its normalizer is r+2, agreeing with the exact r+2 repair-interval
congestion at each projected transition in the residence-reduction file.
This is a congestion count, not an edge-disjoint packing estimate.

## 7. Connection to the existing exact renewal formulas

For D_j=tau^jD define

    a_j=delta(D_j), c_j=d(D_j), c_hat_j=d(phi D_j).

The existing additive-renewal identity is

    a_(j+1)-a_j=c_j-c_hat_j,
    sum_(j=0)^(t-1)c_j-a_t=sum_(j=0)^(t-1)c_hat_j-a_0.

Its first return index is precisely the rank-r newborn lifetime:

    T(D)=min{t>=1: sum_(j=0)^(t-1)c_hat_j in a_0+n Z_(>=0)}.  (13)

Indeed the corresponding omitted-label gap is 2t+1, and (11) identifies
the rank-r lifetime as t. Nonnegative winding follows because a_t<n
and the positive increment sum makes a congruent multiple larger than
-n; it must therefore be a nonnegative multiple of n.

The exact ST_A one-point indicator is consequently 1{T<=H-1}, and the
two-point statistic uses this indicator at D and tau^jD in the same
deterministic sequence. The stationary construction above supplies neither
independence nor a mixing estimate for those indicators.

The two-dimensional-renewal local-CLT note already retracts the proposed
diffusion assumption for the natural PBBS record state: its transfer is
triangular. Nothing in (2)-(13) reinstates that application. Uniform
stationarity and a return-section interpretation do not imply a local
central limit theorem.

## 8. A precise second-moment test for a short newborn tail

For any class Omega as above, fix H<r and write

    p=P_birth(T<=H),       V=Var_birth(T).

Then

    V >= [p/(1-p)](r-H)^2,
    p <= V/[V+(r-H)^2].                                 (14)

For p=0 this is immediate, and p=1 is incompatible with E[T]=r>H.
Otherwise put a=E[T|T<=H]<=H. The other conditional mean is
(r-pa)/(1-p). Dropping the two nonnegative conditional variances gives

    V >= p(a-r)^2 + (1-p)((r-pa)/(1-p)-r)^2
       = [p/(1-p)](r-a)^2,

which proves (14). Thus any positive lower bound on the fraction of
newborn lifetimes at a sublinear cutoff forces variance of order r^2.
Conversely, a separately proved V=o(r^2) estimate would imply a vanishing
newborn fraction at every H=o(r). No such variance estimate is supplied
here; the identity for E_stat[R] in (8) is another exact formulation of
that missing moment control.

## 9. What remains unknown

The exact mean r, even at fixed height, and the residual identities are
rigorous. They do not determine P_birth(T<=H) at Gaussian or larger
sublinear scales: rare very long excursions can carry a substantial part
of the mean. Nor do one-point counts alone control the overlap packing
nu_H. The remaining dynamic problem is the distribution of the return
time (13), together with the correlations of its short-return indicators.
