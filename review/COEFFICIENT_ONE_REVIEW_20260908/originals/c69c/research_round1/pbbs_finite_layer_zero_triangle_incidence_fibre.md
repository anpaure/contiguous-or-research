# The finite-layer zero-triangle incidence fibre

2026-09-08. Pure proof; no computation. This note conditions the BASE
birth on finitely many original triangle rows and identifies its exact
remaining fibre. Shifted partner births retain their original F_0
membership; no shifted zero-triangle gate is added.

Complete-file reviews by the worktree lead and independent recency
reader pass. The coordinator has accepted the lemma after its own
full read and independent reverse-clock and incidence audit.

## 1. Original arrays and the safe profile domain

Fix r, H=floor(c sqrt(r))<r, and the original top-row-zero family

    F_0={GOOD, T<=H, Z_(0,0)=0},
    mu_0=E[(T+2)1_(F_0)].

The incidence assertions assume mu_0>0, as holds for all sufficiently
large r at fixed c by the accepted mu_0=Theta_c(1) bound. If mu_0=0,
there is no F_0 incidence to condition; the deterministic clock identity
below remains valid.

GOOD here is the accepted PROFILE-MEASURABLE condition. Write
D_s=partial^s D, r_s=ups(D_s), h=ht(D), and

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).

Conditional on a complete feasible pruning profile, the original rows
Z_s are independent uniform weak compositions of ell_s into p_s parts.
The row labels are persistent original particle labels, and their
canonical initial selected label is zero. For a deterministic S>=1, put

    F_S=sum_(s=0)^(S-1) sum_(u=0)^s Z_(s,-u).          (1)

All indices in (1) are cyclic. In the exact fibre argument below, fix a
full profile satisfying

    h>=2S,
    p_s>2H+1 and p_s>=2(s+1)            for 0<=s<S.  (2)

Thus all queried cores are nonempty and the s+1 triangle coordinates in
row s are distinct. In particular p_s-s-1>=1. Fix also every original
row with index at least S. These rows reconstruct the ORIGINAL root D_S
uniquely. They do not determine the remaining coordinates in rows s<S.

## 2. The candidate clock uses only D_S

At any PBBS level, a C clock runs to the next selection of the physical
predecessor of the currently selected label; its length is even. A T
clock runs to the next selection of the same label; its length is odd.
Their usual numerical lengths are 2C and 2T+1, respectively.

Starting at time zero in the fixed-site process of D_S, concatenate
exactly S C clocks and then one T clock. More explicitly, let t_0=0;
the ith C clock ends at the first later selection of label -i, for
i=1,...,S. After t_S, end the final T clock at the next selection of
label -S. Set

    G_S^*=t_(S+1),       T_S^*=(G_S^*-1)/2.           (3)

Every clock is taken at its actual chronological reached phase of this
ONE original D_S trajectory. There is no reinitialization between
clocks. G_S^* is finite and odd, and is a function only of D_S, hence
only of the full profile and rows with index at least S.

The reduced height is h-S. Since each C length is at least two and the
last T length is at least 2(h-S)+1, one also has

    G_S^*>=2h+1,       T_S^*>=h.                     (4)

## 3. Both directions of the clock identity

The exact one-level partition at a node with incoming coordinate z is

    C parent -> C child followed by 2z T children,
    T parent -> C child followed by 2z+1 T children.   (5)

The children are adjacent chronological intervals in the same reduced
trajectory. Before the first spatial wrap, (5) identifies the actual
parent clocks. At z=0 it reduces to

    C -> C,                  T -> C T.              (6)

The original chronological row-s query order is 0,-1,-2,...: every
completed row-s node has one child C, which moves the selected label
at level s+1 by -1, followed only by T clocks, which leave that selected
label unchanged at their endpoints. Every level initially has label
zero. This proves the query order without using any unqueried row
coordinate or any guessed physical shift at another level.

FORWARD DIRECTION. Suppose an upper-array completion satisfies F_S=0
and T(D)<=H. Its outer physical horizon G=2T(D)+1 is at most 2H+1,
strictly below all the circumferences required by (2). Starting from
one T node, (6) gives the exact depth-s clock word

    C^s T,

by induction for 0<=s<=S. At depth s<S this word queries precisely
0,-1,...,-s, all zero by (1). Consequently its depth-S word is the
candidate word in (3), with the same initial root and the same successive
physical phases. Its total duration is unchanged by partitioning:

    G=G_S^*,       T(D)=T_S^*.                       (7)

In particular, if the fixed deeper environment has G_S^*>2H+1, NO
upper-array completion with F_S=0 can have T<=H. This conclusion does
not require first defining an untruncated parent genealogy for a long
completion.

CONVERSE DIRECTION. Suppose G_S^*<=2H+1 and take ANY upper-array
completion whose triangle coordinates are all zero. Start with the
candidate depth-S chronological word C^S T and group it as

    C^(S-1) (C T).

Each initial singleton C lifts through (6) to a parent C, and the final
pair C T lifts to a parent T. At row S-1, the successive queried
original labels are 0,-1,...,-(S-1), all zero. The phase of each group
is its actual left endpoint in the same reduced trajectory; completion
of a group changes that reduced selected label by exactly -1.

These lifts are actual clocks: their entire candidate horizon is at most
2H+1, strictly below p_(S-1), and a fortiori below the parent
circumference. Thus neither a full-lap same-site return nor the
same-particle lap to the predecessor can precede the specified hit.
For the even C intervals, their lengths are also strictly smaller than
the odd total G_S^*, so the possible circumference-minus-one alternative
is excluded. This is the one-level no-wrap justification for using (6)
in reverse, not an assumption that a long parent has the same clock.

We have obtained the actual parent word C^(S-1)T with the SAME total
duration. Repeat this grouping at rows S-2,...,0. At every row s the
needed labels are exactly 0,-1,...,-s, and (2) supplies the same horizon
bound. The final result is the actual outer T clock of duration G_S^*.
Therefore T(D)=T_S^*<=H for every such completion.

Combining both directions, for every offset j>=0 and every upper
completion on the profile domain (2), one has the exact event identity

    {T<=H, F_S=0, j<=T+1}
      ={all Z_(s,-u)=0 for 0<=u<=s<S}
         intersect {G_S^*<=2H+1, j<=(G_S^*+1)/2}.     (8)

The second event is measurable from the fixed deeper environment.
The inclusive survival endpoint is T_S^*+1=(G_S^*+1)/2.

## 4. Exact incidence mass and the product of free fibres

Sample the ACTUAL F_0 repair-incidence law: choose a root with weight
(T+2)1_(F_0), then choose j uniformly from 0,...,T+1. After marginalizing
the uniform physical deck, every allowed pair (D,j) has the constant
probability

    1/(Cat_r mu_0).                                  (9)

The lifetime weight cancels exactly against the offset choice. We do
not assign the original unweighted law to the remaining environment.

Fix an environment E=(R,y,j), where R is the entire profile satisfying
(2), y comprises ALL original rows with index at least S, and j>=0.
Call it feasible if R is GOOD and

    G_S^*(y)<=2H+1,       j<=(G_S^*(y)+1)/2.          (10)

On F_S=0 the top-row condition Z_(0,0)=0 is automatic. Formula (8)
shows that (10) is the complete remaining base-lifetime and survival
test. Every choice of the unforced coordinates is then admissible.
In row s<S, there are exactly

    q_s^free=p_s-s-1

unforced coordinates, and their sum is ell_s. Its number of completions
is therefore

    M_s=binom(ell_s+p_s-s-2,p_s-s-2).                 (11)

This includes ell_s=0. Since the original inverse-array encoding is
bijective, the number of upper completions of a feasible E is exactly
the product of these M_s. Consequently its joint mass under the
ORIGINAL F_0 incidence law is

    P_inc,0(E=(R,y,j), F_S=0)
      =1_(E feasible)/(Cat_r mu_0) product_(s<S) M_s.  (12)

Profiles outside (2) are outside this formula's stated domain. For a
nonfeasible environment within (2), the joint mass is zero, so there
is no conditional fibre law to assign.

For every positive-mass feasible environment, (9)-(12) prove that,
conditional on E and F_S=0, the original rows s<S are independent;
in row s its triangle entries are fixed at zero, and its remaining
entries are a uniform weak composition of ell_s into p_s-s-1 parts.
No residual lifetime weighting, mixture, or constraint on the free
entries remains. The distribution of E itself is still the actual
incidence distribution in (12).

## 5. The safe zero-triangle restriction has asymptotically full mass

This section uses the accepted quantitative original-profile envelope
and uniform early-triangle estimate. Put R=sqrt(r). Their inputs are:

* A profile-measurable a>=1 satisfies
  P(a>t)<=C exp(-b t^2), with an adjustment of C for bounded t.
* A=a+sqrt(log(a+2))<=3a and L=floor(kappa_c R/A).
* If L>=2, the profile has h>2L and satisfies all physical/query safety
  inequalities in (2) for S<=L.
* Uniformly in the original profile,

      E[(T+2)1{T<=H} | profile]<=C_c A exp(C_c A).

* mu_0 is bounded above and below by positive constants depending on c.
* For deterministic 1<=S<=R,

      E[(T+2)1{T<=H,F_S>0}]<=C_c S^2/r.              (13)

These are original-profile and original-incidence statements. In
particular the same a has a uniform subGaussian upper tail under the
ACTUAL F_0 incidence law. Indeed, using A<=3a, the raw bound and the
positive lower bound on mu_0 give

    P_inc,0(a>t)
      <=C_c E[a exp(C_c a)1{a>t}]
      <=C_c (E[a^2 exp(2C_c a)])^(1/2) P(a>t)^(1/2)
      <=C_c exp(-b_c t^2).                           (14)

The exponential moment is finite by the original subGaussian tail;
the constants are uniform in r. Bounded t is again absorbed into C_c.

Set M=max(S,2). If L<M, then A>kappa_c R/M, hence
a>kappa_c R/(3M)>=kappa_c R/(6S). Formula (14) yields, for every
deterministic 1<=S<=R,

    P_inc,0(L<max(S,2))<=C_c exp(-b_c r/S^2).         (15)

Dividing (13) by mu_0 gives

    P_inc,0(F_S>0)<=C_c S^2/r.                       (16)

Thus the actual F_0 incidence law assigns probability at least

    1-C_c S^2/r-C_c exp(-b_c r/S^2)                  (17)

to the base event {F_S=0, L>=max(S,2)}. In particular this probability
tends to one for every deterministic S=o(sqrt(r)). On this event the
profile domain (2) holds, so Sections 2-4 apply without a new law at a
reached root.

## 6. Scope and conditioning guard

The exact product in Section 4 is a BASE conditioning statement. A
shifted partner contributes precisely when it belongs to the original
family F_0 and its repair interval covers the sampled edge. No partner
is required to satisfy a shifted F_S=0 event. Its test must still be
evaluated through the original arrays and the exact physical cocycles.

Likewise the exact uniform compositions are not additionally conditioned
on a maximum-gap event. Such an event can be proved to have high
probability under this law or its complement bounded separately; adding
it as a conditioning restriction changes the exact product fibre. The
profile-only nature of GOOD and of the safety conditions is essential
to the formula as written.

This lemma does not prove that many shifted labels pass their virtual
lifetime cutoff, and gives no occupied-support or packing conclusion.

Sources: pbbs_gaussian_clock_genealogy_structural_audit.md, especially
its exact clock partition and deterministic original-slot query order;
the original incidence-window constant-atom identity;
pbbs_uniform_early_triangle_incidence.md; and the accepted bounded
Gaussian short-incidence envelope and top-row-zero reduction.
