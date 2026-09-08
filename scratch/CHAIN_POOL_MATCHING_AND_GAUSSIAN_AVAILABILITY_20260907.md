# Near-width common-root chains: global availability without dilution

Date: 2026-09-07. Pure proof; no computation.

This is a composition of the audited growing-prefix central matching,
marked-target zero-hit theorem, and cyclic-rail-chain geometry. It is
NOT a simultaneous routing theorem. Source proofs are listed below;
this research note does not replace the self-contained master handoff.

## 1. Parameters and literal word family

Let the ground size be 2b, W=binom(2b,b), and, for sufficiently large b,

    d=L=floor(log log b),
    h=d floor(sqrt(b)/d),
    a=Lh, ell=a+1, H=floor(h sqrt(L)).

Use the chain of L cells, with d cyclic rails of length h in each cell,
from `CHAIN_OF_CYCLIC_RAIL_CELLS.md`. Its distinct folded middle support,
principal word charge, and common caps have sizes

    r=(L+1)+Ld(h-1),
    M=2d(Lh+1),
    |F|=|G|=b-a.

All root permutations preserve that middle support. There are d full
geodesics of side ell; their states are prefixes in at most 2d+2
whole-ground ordered groups. Moreover

    M-2r=2(d-1)(L+1),
    t=d, g<=2d+2, a=b^(1/2+o(1)), r=b^(1/2+o(1)),
    t log log b=o(log b), 2a<b,
    sqrt(b)<<H<<a, H<=b-ell.

The accepted growing-prefix matching theorem therefore supplies a
near-perfect matching of these folded supports. After choosing a
uniform representing embedding for each selected support, any choice
of its route permutations has the same middle footprint.

For m selected macros, m<=W/(2r). Their guarded derivative words cost

    m[M+2Hd+(d-1)]+(m-1)
      <= W[1+O(1/h+H/(Lh)+1/(Lh))]
       = W+o(W).

The (m-1) term is for guards BETWEEN macros; the (d-1) term is for
guards between routes inside a macro. Patch the o(W) unmatched middle
sets using isolated set-valued letters and guards, still at o(W) cost.
The master Appendix A.4 repair of ranks outside the H-band also costs
o(W), since H/sqrt(b)~sqrt(L)->infinity. Keep that repair fixed in every
subsequent routing choice. Its incidental band targets are part of the
fixed exterior, not ignored.

Thus this is a FAMILY of literal words of length W+o(W), all realizing
the entire middle rank and the ranks outside the H-band. No member is
yet proved universal or even density-one.

## 2. Exact inventory and its Gaussian asymptotic

For 1<=q<=H, let Ncross_q count pairs of levels (s,s+q) with nonroot
endpoints in different cells. Endpoint reconstruction in the geometry
proof gives, at either signed rank b+/-q,

    Selected_q = 2d(Lh+1-q)
      -1_{h divides q} 2(d-1)(L-q/h+1),
    Pool_q = Selected_q+2d(d-1)Ncross_q,
    Flexible_q = 2d Ncross_q.

Here Selected_q is the distinct support of EVERY single routing;
Pool_q is its union over all routing choices. Flexible_q is the portion
of a single routing's support that can change with the phases.

For q<=h, Ncross_q=(L-1)(q-1). For h<=q<=H=o(Lh), every nonroot
level pair is cross-cell, and there are only O(L) pairs with at least
one root endpoint. Consequently, uniformly for q/sqrt(b) in a fixed
compact subset of (0,infinity),

    Selected_q/M -> 1,
    Flexible_q/M -> min(c,1),
    Pool_q/(2r) = (d min(c,1)+o(d)),
    c=q/sqrt(b).

The errors are uniform across q=h; its root-pair correction is O(dL),
which is o(M). At each fixed Gaussian depth the flexible selected mass
is therefore a positive fraction of principal charge. This avoids the
vanishing q/h flexible fraction of the earlier broadened-arm box.

## 3. Why the marked theorem applies at every fixed Gaussian depth

A lower target in the verified all-depth pool is an intersection of
two ordered central endpoints, or the corresponding intersection in
the complementary orientation. In the merged ordered groups it is a
prefix set (reverse orders for the complementary orientation), lying
between a common core of size b-a and a common union of size b+a.

For a source role T0 of rank b-q, conditioning a uniform permutation
on T0 mapping to a fixed target T gives the SAME marked allocation bound

    Pr(S subset F_marked)
       <= g^u / [binom(b-q,d0) binom(b+q,e0)],
    d0<=a-q, e0<=a+q, q<=u=d0+e0<=2a.

The accepted extent-count and geodesic argument then give

    kappa_q(1/log b) <= exp[-(1/2-o(1))q log b].

Nothing in this argument requires q<=h. That restriction belonged to
the box's old short-depth pool census, not to the marked-kernel proof.
The chain supplies its complete pool census for all q<=H<a.

All marks here are DISTINCT target roles, not multiplicities of paths
or phase realizations. Source role weights are fixed before sampling;
representing embeddings are uniform; the central nibble ignores marks.
These are the hypotheses needed for its equivariant ban-deficit bound.

Let N_q=binom(2b,b-q). The exact normalized possible-supplier degree is

    Gamma_pool(q)=(W/N_q)Pool_q/(2r).

The central-binomial ratio and Section 2 yield

    Gamma_pool(q)=(e^(c^2) min(c,1)+o(1))d -> infinity.

The already audited adaptive zero-hit theorem now proves that a fixed
target in this rank belongs to at least one selected macro's possible
pool with probability 1-o(1), uniformly on every fixed Gaussian annulus.
Its many-supplier version gives order d distinct selected macro suppliers
with probability 1-o(1). Neither assertion chooses their route phases.

## 4. Whole-cube possible-pool density

Fix 0<epsilon<C. The preceding bound is uniform on
epsilon<=abs(q)/sqrt(b)<=C, so the expected number of unavailable targets
there is o(4^b). Ranks with abs(q)<epsilon sqrt(b) contain at most
O(epsilon)4^b+O(W) targets. The ranks with abs(q)>C sqrt(b) contain at
most 2 exp(-C^2)4^b targets by the elementary binomial tail bound.

Take b->infinity, then epsilon->0 and C->infinity. This gives expected
possible-pool deficit o(4^b), and Markov yields deficit o(4^b) with high
probability, jointly with near-perfect central matching. This uses one
fixed parameter sequence and one process, not a different process for
each target or annulus.

Accordingly, there exist near-width common-middle word families whose
UNION of possible target supports has density 1-o(1), and whose phase
choices affect a macroscopic target mass at every fixed Gaussian depth.
The required next theorem is that ONE compatible phase choice has
density 1-o(1). Only then can the master density-amplification reduction
be applied. An o(4^b) possible deficit is not an o(W) patch list.

## 5. Sources and audit scope

- Root `scratch/GROWING_PREFIX_GRID_KERNEL_AND_MATCHING_20260907.md`.
- `7796/problem/research_round1/CHAIN_OF_CYCLIC_RAIL_CELLS.md` under
  `/Users/amir.nuriyev/.codex/worktrees/`.
- `ae28/problem/research_round1/ROUND4_OFFCENTRAL_MARKED_POOL_KERNEL.md`.
- `ae28/problem/research_round1/ROUND4_HIGH_VALENCE_POOL_ZERO_HIT.md`.

The source geometry, central matching, marked kernel and finite zero-hit
proofs passed full root and independent audits. The chain-specific
all-depth role transfer and min(c,1) asymptotic were also independently
checked by their two task owners. A separate independent root-agent audit
PASSED this entire written composition and the source phase/DP sections,
including guards, the all-depth marked role transfer and the annulus
limit for one fixed process. Full coefficient one and exact equality
remain open; no new full-cube upper coefficient is claimed here.
