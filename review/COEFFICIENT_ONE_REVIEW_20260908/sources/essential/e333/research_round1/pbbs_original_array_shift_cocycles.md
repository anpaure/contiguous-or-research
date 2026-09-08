# PBBS shifted short returns in the original pruning coordinates

Date: 2026-09-07. Pure finite proof; no computation.

Read-only sources: worktree c69c, research_round1,
`pbbs_gaussian_clock_genealogy_structural_audit.md`,
`pbbs_zero_budget_pair_product_and_overlap_divergence.md`, and
`pbbs_stationary_lifetime_identities.md`; and the original
`/Users/amir.nuriyev/Documents/problem/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`,
Sections 8-9 and 14. The source lifetime convention is retained:
the physical omitted-label return gap at root D is 2T(D)+1, and
tau=phi^2. This note concerns original coordinates and finite events,
not an asymptotic cluster or incidence-weight assertion.

## 1. Persistent indices and the correct translated arrays

Fix one root D of positive semilength r and height h. Put

    D_s=partial^s D,    r_s=|D_s|_up,    n_s=2r_s+1,
    p_s=n_(s+1),       0<=s<h.

At level s, the equality particles are labelled cyclically modulo p_s,
with original label zero on the edge immediately before the unmatched
zero of 0D_s. Let Z_(s,j) be the original incoming-gap coordinate from
the structural source, for nonempty-core levels 0<=s<h-1. If a bottom
array is desired, its single coordinate is deterministically
Z_(h-1,0)=r_(h-1). These coordinates are invariant under physical PBBS
updates when particle labels are persistent.

On the ORIGINAL fixed-site cyclic word w_s=0D_s, number sites
0,...,n_s-1, and let lambda_s(t) be its omitted site at every integer
time t, before that time's update. Negative times use the inverse of
the finite PBBS permutation on the SAME original labelled orbit; no
new root is sampled. Thus lambda_s(0)=0. All levels use the same
signed physical time t. Equality-particle renormalization
identifies the selected particle at level s with the omitted site of
the fixed-site process at level s+1. Write

    kappa_s(t)=lambda_(s+1)(t)  modulo p_s.             (1)

**Exact shift identity.** If Z^t denotes the canonical pruning arrays
of the new root phi^t D, whose particle labels are reset to start at
its current distinguished particle, then

    Z^t_(s,j)=Z_(s,kappa_s(t)+j),                      (2)

with indices modulo p_s. In particular, for the root tau^d D use
t=2d at EVERY pruning level, for every integer d, positive or negative.

Indeed the newly distinguished particle has old label kappa_s(t).
Persistent cyclic order makes its new successor j equal to old label
kappa_s(t)+j, and gap-coordinate invariance gives (2). The physical
formula omitted site = particle edge position +1 does not add a one
to this PARTICLE-indexed shift. Renormalization advances one step at
every level per physical update; there is no level-dependent time
rescaling. Identity (2) permits arbitrary previous spatial wraps.
The forward identities also hold at each negative-time transition of
the same bi-infinite orbit, so invertibility gives (2) at all integer
times.

For an explicit quotient cocycle at a nonempty reduced core
(0<=s<h-1), let delta(F) be the position of the
first maximum-reaching up-step of F. If F=P1R0S is its first-maximum,
first-return factorization, put omega(F)=|S|+1. The original skew-product
identities give, for all integers t,d,

    kappa_s(t)=sum_(v=0)^(t-1) delta(phi^v D_(s+1))
                                                   modulo p_s,
    kappa_s(2d)=-sum_(v=0)^(d-1) omega(tau^v D_(s+1))
                                                   modulo p_s. (3)

Every sum from 0 to t-1 is SIGNED: it is the ordinary sum over
0<=v<t when t>=0, and minus the sum over t<=v<0 when t<0.
Use the same convention with d in the second identity. Thus (3)
telescopes the original voltage increments in either time direction.
For example kappa_s(-1)=-delta(phi^(-1)D_(s+1)), while
kappa_s(-2)=+omega(tau^(-1)D_(s+1)), each modulo p_s.

Equivalently the even-time shift theta_s(d)=kappa_s(2d) obeys

    theta_s(0)=0,
    theta_s(d+1)=theta_s(d)-omega(tau^d D_(s+1)) mod p_s.

The increment identity holds for every integer d.

For the optional bottom slot, kappa_(h-1) is identically zero modulo
one, as is lambda_h; no value of delta at an empty core is invoked.

These are deterministic cocycles of the ORIGINAL reduced process, not
a new probability law at its visited roots. Generally theta_s(d) is
not -d. For example D_(s+1)=(10)^k has delta=1 at every step, hence
theta_s(d)=2d modulo 2k+1. Different pruning depths generally have
different shifts.

## 2. A bottom-up recursion entirely from the original data

The preceding cocycle can also be evaluated without using a reached-root
oracle. For s<h-1 let b_(s+1,j) be bit j of the original word 0D_(s+1),
and put

    epsilon_(s,j)=1{b_(s+1,j-1) != b_(s+1,j)},
    L_(s,j)=2Z_(s,j)+1+epsilon_(s,j),
    C_s(0)=0,
    C_s(j)=sum_(k=1)^j L_(s,k),       1<=j<p_s.        (4)

These are fixed original constants. The arrays and pruning profile
reconstruct the original reduced words by the source's inverse-pruning
bijection, so (4) uses no additional random information.

Define the signed visit count at every integer time by

    M_(s+1,j)(t)= #{0<=u<t: lambda_(s+1)(u)=j},   t>=0,
                 -#{t<=u<0: lambda_(s+1)(u)=j},   t<0. (5)

It satisfies M_(s+1,j)(0)=0 and
M_(s+1,j)(t+1)-M_(s+1,j)(t)=1{lambda_(s+1)(t)=j}
for EVERY integer t. The complete omitted-site sequences satisfy the
following recursion, also for every integer t:

    lambda_(h-1)(t)=t modulo n_(h-1),

    lambda_s(t)=C_s(lambda_(s+1)(t))
                 +M_(s+1,lambda_(s+1)(t))(t)
                 modulo n_s,             s=h-2,...,0. (6)

To prove this, the initial edge position of particle j at level s is
x_(s,j)(0)=-1+C_s(j). It moves forward once precisely when the reduced
omitted site equals j. At negative times the inverse update undoes that
same move. Telescoping the particle-position increments with (5) gives

    x_(s,j)(t)=-1+C_s(j)+M_(s+1,j)(t) modulo n_s.

The original renormalization identity is
lambda_s(t)=x_(s,lambda_(s+1)(t))(t)+1, proving (6).
For t>0 the count excludes update t; for t<0 the inverse sum includes
update t with a minus sign. Both conventions put the particle at its
position BEFORE update t. At the bottom, D_(h-1)=(10)^(r_(h-1)); its
rooted shape is fixed by phi and its voltage is one in both time
directions, proving lambda_(h-1)(t)=t modulo n_(h-1) for all integer t.
Formula (6) is valid through all spatial wraps and needs no resetting
of the original arrays at a negative-time phase.

Thus the original profile and arrays determine every shift and every
finite return predicate, by integer counts and residues alone. This is
a mathematical recursion, not a computational experiment.

## 3. Exact full-return and predecessor-count predicates

At any integer physical starting phase t_0 define

    g_D(t_0)=min{u>=1: lambda_0(t_0+u)=lambda_0(t_0)}.

The full-label property ensures a finite return, and the accepted
phase convention gives the exact identity

    2T(phi^(t_0)D)+1=g_D(t_0).                         (7)

Consequently, with G=2H+1,

    T(tau^dD)<=H
      iff some 1<=u<=G has lambda_0(2d+u)=lambda_0(2d). (8)

Together with (4)-(6), this is an original-array characterization for
every integer d and every finite H>=0, including negative birth shifts
and windows allowing spatial wraps.

There is a more economical exact predicate when G<n_0. Suppose h>=2,
put t_0=2d, a=lambda_1(t_0), and z=Z_(0,a). Then

    T(tau^dD)<=H
      iff #{1<=u<=G: lambda_1(t_0+u)=a-1 mod n_1}
                      >=2z+2.                        (9)

At t_0 the selected particle a and its predecessor both record zero,
so their incoming separation is 2z+1. If ell=lambda_0(t_0), their
lifted edge positions are ell-1 and ell-2z-2. The predecessor's k-th
selection strictly after t_0 therefore omits ell-2z-2+k. Its first
omission of ell is precisely its (2z+2)-nd such selection. No overtaking
forces this predecessor to be the first distinct particle to reach
ell again. A return by particle a after a full spatial lap takes at
least n_0 further selections, excluded by G<n_0. This proves (9).

The upper endpoint u=G is included: its omitted site is recorded before
that update. No condition G<n_1 is needed for (9); reduced dynamics can
wrap during the counting window. If h=1, T(D)=r and the short event is
empty when G<n_0. The natural one-slot convention z=r makes the
right side of (9) false as well, but the distinct-predecessor proof is
then replaced by this direct boundary case.

For any finite collection of shifts, conjoin the predicates (8), or
(9) in its stated range. All of them use the SAME original arrays
and sequences, giving an exact joint finite event without independence
or an original-to-reached reset. The collection may contain both
positive and negative shifts.

## 4. The correctly translated triangular obstruction

Assume h>L and p_s>G for 0<=s<L, where G=2H+1. Apply the accepted clock
genealogy to the root tau^dD for any integer d. Its chronological
queries at depth s, expressed in original indices, are exactly

    Z_(s,kappa_s(2d)), Z_(s,kappa_s(2d)-1), ... .      (10)

The minus one per chronological node comes from completion of that
node's unique child C clock. It is a genealogy index advance, distinct
from the two-step time cocycle in (3).

In detail, start v_0=u_0=1, let v_s count all depth-s clocks, u_s count
their T clocks, and let W_s be the sum of the first v_s queried entries
in (10). The exact source recursion remains

    u_(s+1)=u_s+2W_s,
    v_(s+1)=v_s+u_s+2W_s.

Hence v_s>=s+1 and sum_(s<L) W_s=(u_L-1)/2. The pruning profile is
invariant at every reached phase. Each depth-L T clock therefore has
physical length at least 2(h-L)+1. On the shifted short event its
whole interval has length at most G, so the source's disjoint-clock
bound yields

    sum_(s=0)^(L-1) sum_(j=0)^s
       Z_(s,kappa_s(2d)-j)
          <= [G/(2(h-L)+1)-1]/2.                     (11)

This is a NECESSARY consequence, not an equivalent full-return test.
The exact test is (8) or (9). The no-wrap hypothesis p_s>G applies
only to the new window beginning at 2d; there is no restriction on
how much the process wrapped before that time.

The shifts in (11) depend on original deeper pruning data. They cannot
be replaced by a common deterministic -d without an additional proof.
Different shifted triangles can query the same original slots; such
repeated queries read the same values. Conditioning on another short
event or choosing d from the observed trajectory does not supply a
fresh composition law.

These formulae isolate the exact finite dependence that a later cluster
argument would need to analyze. They make no claim about a growing-lag
limit, independent returns, stationary incidence weights, or packing.
An independent audit checked (2)-(3), the recurrence (6), and both the
threshold and phase endpoints in (9). The signed negative-time
extension, including the inverse-step evaluation points and the
empty-core convention, also passed an independent sign audit.
