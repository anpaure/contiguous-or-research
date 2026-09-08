# Exact PBBS short-repair incidence law in original coordinates

2026-09-07. Pure proof; no computation. This is a finite sampling and
overlap dictionary, not a new renewal or overlap asymptotic.

Read-only sources: task05's `pbbs_stationary_lifetime_identities.md`,
`pbbs_gaussian_age_residual_and_cut_charges.md`, and
`pbbs_zero_budget_pair_product_and_overlap_divergence.md` in worktree
c69c/research_round1; the authoritative scratch note
`PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md`.
The original-array fiber representation in Section 3 is an explicit
input from the current pruning-coordinate audit.

## 1. Birth phase and inclusive edge endpoints

Fix r>=1, n=2r+1, and the full physical complement-projected PBBS factor,
with W=n Cat_r edges. Write f for the rank-r PBBS permutation, g=f^2,
phi for the rooted quotient, and tau=phi^2. The lifetime T(D) includes
the consuming update. Thus a gap-start root D with omitted-label return
gap 2T(D)+1 gives a complement positive run with T(D)+1 owners and a
repair interval with T(D)+2 edges.

To fix the complement phase literally, let B be the physical rank-r
state at the omitted-label gap start, with root D. Put

    B_d=f^(2d)B,
    e_d : (f^(2d-1)B)^c -> (f^(2d+1)B)^c,   d in Z.       (1)

The birth on e_d has gap-start root tau^d D. The repair interval born
on e_0 contains precisely

    e_0,e_1,...,e_(T(D)+1).                               (2)

Offset j=0 is the insertion edge; offset j=T+1 is the deletion edge;
offsets 1,...,T are internal. At this cut the positive run has j owners
on the left and T+1-j on the right, including a zero side at a boundary.

Equivalently, if one starts with a complement edge A_i^c -> A_(i+2)^c,
its birth root is root(A_(i+1))=phi(root(A_i)). On all Dyck roots the
common phi shift preserves uniform measure and commutes with tau. For
a merely tau-invariant owner-root family Omega, the birth-root family
is phi(Omega); it cannot silently be replaced by Omega.

Let P be the actual physical period of (1). The prebirth owner lacks
the inserted coordinate and returns after P steps, so the coordinate
is first deleted by e_(P-1). Hence T(D)+2<=P for every birth on this
cycle. The accepted full-label property also gives P>=2r+1. A root's
tau-period may be shorter than P: repeated roots at different physical
phases are distinct births and must remain distinct in overlap counts.

Our cutoff below is T<=H. A cutoff H_res on complement residence instead
means T<=H_res-1.

## 2. Uniform retained repair-edge incidence

Let A(D) be any zero-one birth predicate and set

    mu_A=E_D[(T(D)+2)A(D)],                              (3)

where D is uniform among the Cat_r roots. There are exactly W mu_A
retained repair-edge incidences. If mu_A=0 the family is empty and its
incidence probability law is undefined. Otherwise its exact sampler is:

1. Choose D with probability (T(D)+2)A(D)/(Cat_r mu_A).
2. Choose uniformly one of its n physical spatial phases u, thereby
   fixing B and the entire deterministic trajectory (1).
3. Choose j uniformly in {0,...,T(D)+1}.

Thus every admissible triple (D,u,j) has probability 1/(W mu_A), and

    E_inc,A Psi = (1/mu_A) E_(D,u)
                       [ A(D) sum_(j=0)^(T(D)+1) Psi(D,u,j) ]. (4)

For A_H=1{T<=H} and p_t=Pr_D(T=t), in particular,

    Pr_inc,H(T=t,j=v)=p_t/mu_H,
          1<=t<=H, 0<=v<=t+1;
    Pr_inc,H(T=t)=(t+2)p_t/mu_H.                         (5)

Conditioned on the explicit offset j, the root is uniform among those
with max(1,j-1)<=T<=H. Uniform retained births and uniform retained
repair incidences are different measures.

## 3. Disintegration on the original pruning-coordinate fibers

Assume the supplied exact coordinate bijection: each root is represented
once by a feasible pruning profile R and an original array x in its
Cartesian product C_R of weak-composition fibers. Before conditioning,
given R the original array is uniform on C_R. It is this original array,
not a newly sampled array at a reached root, that determines every
T(tau^d D).

Marginalizing out the physical phase in (4) gives the exact atom law

    Pr_inc,A(R,x,j)
      = A(D(R,x)) 1{0<=j<=T(D(R,x))+1}/(Cat_r mu_A).      (6)

For a positive-mass conditioning event (R,j), x is therefore uniform
on

    {x in C_R: A(D(R,x))=1, T(D(R,x))>=j-1}.             (7)

For a positive-mass conditioning event R alone, its law is proportional
to (T(D(R,x))+2)A(D(R,x)) on C_R. Thus recording j cancels the length
factor, but it leaves a survival condition. Neither conditioning
preserves the original product independence unless separately proved.
The physical phase, when needed, is still uniform given (R,x,j).

## 4. Exact shifted overlap, with negative shifts and wrap

At a sampled e_j, let K_A(B,j) count all retained repair intervals on
its physical cycle that contain this edge. For each physical birth
residue d modulo P put T_d=T(tau^d D). With [v]_P in {0,...,P-1},

    K_A(B,j)=sum_(d mod P) A(tau^d D)
                         1{[j-d]_P<=T_d+1}.             (8)

This is valid without a cutoff and counts each physical birth once.
It is a deterministic function of the original state; there are no
independently renewed roots in (8).

If A implies T<=H and H+2<=P, the H+2 possible earlier birth residues
have the unique lifted representatives j-H-1,...,j. Therefore

    K_A(D,j)=sum_(d=j-H-1)^j A(tau^d D)
                                    1{T_d>=j-d-1}.      (9)

For H=o(r), the accepted lower bound P>=2r+1 makes (9) applicable to
every physical component for all sufficiently large r. Otherwise use
(8), or replace H in the age-window bound by min(H,P-2).

Negative d are genuinely earlier births. For d=-a their lifetime must
be at least j+a-1. Positive d can contribute only when d<=j and still
must satisfy T_d>=j-d-1. At the left endpoint d=j-H-1, an overlapping
retained interval has T_d=H and e_j is its deletion edge. At d=j, e_j
is its insertion edge. The sampled base birth d=0 always contributes.

In particular, a shifted event T_d<=H alone does not guarantee overlap:
the later retained interval may already have ended. The zero-budget
fixed-height argument avoids this issue because all its lengths agree.

Every finite joint law follows by inserting products of these original-
trajectory indicators in (4). For example the probability that fixed
physical birth residues d_1,...,d_s all supply retained intervals at
the sampled edge is exactly

    (1/mu_A) E_(D,u) [ A(D) sum_(j=0)^(T(D)+1)
        product_l A(tau^(d_l)D)
                    1{[j-d_l]_P<=T(tau^(d_l)D)+1} ].     (10)

The physical-period convention in (10) is essential when a root orbit
has a shorter period. No factorization of (10) is asserted.

For an integer budget threshold bcut>=0, take

    A_(H,bcut)(D)=1{T(D)<=H, T(D)-h(D)>bcut},             (11)

where height h is tau-invariant. Formula (9) specializes to

    K_(H,bcut)(D,j)=sum_(d=j-H-1)^j
      1{max(h(D)+bcut+1,j-d-1,1)<=T(tau^d D)<=H}.        (12)

Its sampling measure is (4) or (6) with predicate (11); the offset j
and budget threshold bcut are separate parameters.

## 5. The exact occupied-edge target and low-budget deletion

Write K_A(e) for the same congestion at physical edge e. Counting
incidences in the two orders gives

    E_edge K_A=mu_A,
    Pr_inc,A(sampled edge=e)=K_A(e)/(W mu_A),
    #{e:K_A(e)>0}/W=mu_A E_inc,A[1/K_A].                 (13)

On the incidence law, 1<=K_A<=r+2, the upper bound following from the
full repair family, whose congestion is exactly r+2 at every edge.

The target for negligible occupied support is the PRODUCT in (13).
If mu_A=O(1), divergence of K_A in incidence probability would suffice.
For all Gaussian-short runs, the current short-birth bound alone gives
only mu_H=o(H), which may diverge. Then one needs
E_inc,H[1/K_H]=o(1/mu_H), or an equivalent product estimate. Full-family
sampling illustrates the issue: mu=r+2 and K=r+2 diverge while every
edge is occupied. No new overlap-divergence result is proved here.

Put B=T-h. The separate all-lifetime low-budget inputs have DIFFERENT
forms for zero and positive budgets:

    #{edges in some B=0 repair interval}/W=o(1),
    Z_+=E[(T+2)1{0<B<=bcut_r}]=o(1).                   (14)

Zero-budget RAW incidence E[(T+2)1{B=0}] is Theta(1), so it must not be
included in the second estimate. The accepted authoritative note
`PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md` supplies (14) for
its explicit bcut_r=J_r of order sqrt(r/log r), without a lifetime
cutoff. Only the first line uses sharing among repair intervals.

Let mu_H be the all-short normalizer, mu_+ the normalizer for
A_+=1{T<=H,B>0}, and mu_res the normalizer for (11). Set

    delta_+=mu_+-mu_res <= Z_+,
    delta_H=mu_H-mu_res
           =E[(T+2)1{T<=H,B=0}]+delta_+.               (15)

Whenever the corresponding laws are defined, conditioning gives the
exact identities

    TV(P_inc,+,P_inc,res)=delta_+/mu_+,
    TV(P_inc,H,P_inc,res)=delta_H/mu_H.                 (16)

Thus positive-short and residual incidence laws are asymptotically
close when mu_+ is bounded below. All-short and residual incidence laws
are close only under the additional relative-mass condition
delta_H=o(mu_H); a lower bound on mu_H alone is insufficient because
the removed zero-budget raw mass need not vanish.

For OCCUPIED support no such relative-mass condition is needed. Every
edge lost on passing from all-short to residual is in a zero-budget
repair interval or in one with 0<B<=bcut_r. By (14),

    0 <= #{e:K_H(e)>0}/W-#{e:K_res(e)>0}/W
      <= #{edges in some B=0 interval}/W+Z_+=o(1).       (17)

If mu_H tends to zero, the occupied all-short fraction already tends
to zero by (13), since it is at most mu_H. Closeness of any sampling
laws alone does not identify their congestion observables. The remaining
overlap target is still mu_res E_inc,res[1/K_res]=o(1), with the empty
residual family interpreted as having zero occupied support.
