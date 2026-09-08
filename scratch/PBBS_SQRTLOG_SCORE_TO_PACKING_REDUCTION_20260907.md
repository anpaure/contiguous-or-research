# Quantitative score-to-packing target after the square-root-log bound

2026-09-07. Root conditional synthesis. No computation. The implication
below is proved; its low-score hypothesis is NOT proved.

## 1. Accepted inputs and notation

Set n=2r+1 and W=n Cat_r. A PBBS newborn has height h, lifetime T
including the consuming update, and budget B=T-h. Its full physical
repair trace has T+2 edges. Fix c>0 and H=floor(c sqrt(r)).

Use the accepted integer cutoff J_r=Theta(sqrt(r/log r)) from
PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md. The family of ALL
births with B<=J_r, without any lifetime cutoff, has maximum
edge-disjoint trace packing o(W/sqrt r).

Let A={T<=H, B>J_r} be the residual family, mu=E[(T+2)1_A], and
U_A its occupied-edge union. The new accepted root theorem
PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md gives

    mu<=mu_H=O_c(sqrt(log(r+1))).                       (1)

Task08's exact original-coordinate environment E consists of the
full pruning profile, deeper original arrays and the sampled repair
edge offset. For every nonzero level-zero label i, U_i(E) is the union
of its admissible integer incoming-gap intervals for births in A
that cover the sampled edge. Condition the base gap to a feasible
value z; the remaining p-1 gaps are a uniform composition of ell-z.
Set q_z=(ell-z)/(ell-z+p-1) and

    Lambda_*(E)=min_{feasible z}
                  sum_{i!=0} Pr_{Geom(q_z)}(Z in U_i(E)).

The reference geometric law has mass (1-q_z)q_z^a at a>=0. No
independence of the actual conditioned slots is assumed. For a
threshold lambda define the RAW low-score incidence

    nu_low(lambda)=mu Pr_inc(GOOD and Lambda_*<lambda).

If mu=0, set nu_low=0 and all conclusions are immediate. Otherwise
Pr_inc is the actual lifetime-weighted incidence law, not uniform
newborn sampling. The accepted finite comparison gives

    |U_A|/W <= nu_bad+nu_low(lambda)
                 +mu/(1+lambda/2)+80mu exp(-lambda/8), (2)
    nu_bad<=2/(n+1)^9.

This is task08's pbbs_deeper_visit_score_reciprocal_decomposition.md,
Section7, with the finite pointwise density proof in
pbbs_queried_slot_constant_density_bound.md. Root and independent
readers have checked these inputs completely.

## 2. An explicit sufficient unresolved estimate

Put lambda_r=(log(r+1))^(3/2). Equations (1)-(2) imply, unconditionally,

    |U_A|/W <=nu_low(lambda_r)+O_c(1/log(r+1))+o(r^-1). (3)

The remaining sufficient hypothesis is

    nu_low((log(r+1))^(3/2))
                    =o(1/sqrt(log(r+1)))              (LS_c)

for each FIXED c>0. If LS_c holds, (3) gives

    |U_A|=o(W/sqrt(log r)).                            (4)

Every trace in A has integer B>=J_r+1, so its length is at least
J_r+3. An edge-disjoint subfamily has total length at most |U_A|.
Consequently its maximum packing P_A obeys

    P_A<=|U_A|/(J_r+3)=o(W/sqrt r).                    (5)

Split any packing of ALL T<=H births into B<=J_r and B>J_r. The
first part is bounded by the accepted all-lifetime low-budget theorem,
and the second by (5). Thus LS_c implies

    P_r(c):=maximum packing of ALL traces with T<=floor(c sqrt r)
                  =o(W/sqrt r).                      (6)

The zero-budget family is handled by its proved shared packing,
not by incorrectly declaring its raw incidence negligible.

More generally lambda_r=log(r+1) f_r with f_r->infinity works in
place of log^(3/2), if the same low-score rate is supplied at that
threshold. Merely nu_low=o(1) is insufficient for this packing
argument: dividing an unspecified o(W) support by J_r loses a
factor sqrt(log r).

## 3. What a conditional diagonalization really supplies

Suppose LS_c is proved separately for every positive integer c.
Write a_r(c)=sqrt(r)P_r(c)/W. By (6), a_r(c)->0 for every fixed c.
Choose increasing thresholds R_m>=m^4 such that for r>=R_m,

    a_r(m)<=m^-3.

Let c_r be the largest m with R_m<=r, and set H_r=floor(c_r sqrt r).
Then c_r->infinity, H_r=o(r), and

    H_r P_r(c_r)/W <=c_r a_r(c_r)<=c_r^-2 ->0.         (7)

The separate numerical cycle-opening factor also vanishes:

    H_r Cat_r/W=H_r/n ->0.                            (8)

These are precisely packing and two charge-factor conclusions.
Without effective fixed-c rates, this is an existence diagonal,
not an automatically effective choice of R_m. It does not on its
own verify a complete compiler, every target repair, or the full
coefficient-one theorem. In particular LS_c itself remains open.

## 4. Research interpretation

The accepted short-clock calculation now controls the workload to
sqrt(log r). The unresolved task in this route is a weighted
trajectory assertion: environments with too little distinct-label
overlap must carry o(1/sqrt(log r)) raw incidence at the displayed
threshold. Finite-slot laws and an upper multiplicity bound for one
particle do not establish that assertion. No numerical probability
of success or completion percentage follows from this reduction.

