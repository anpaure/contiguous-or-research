# The asymmetric hook repair must use the retained bulk

2026-09-08. Pure constructive analysis; no computation. Independent
direct-route and root full-file audits passed. This closes one particular chain-repair strategy,
not the actual asymmetric width gate or the infinitesimal rank gain.

## 1. Exact bulk and remainder geometry at position three

Use Q_3 from `ASYMMETRIC_SHORT_AXIS_RANK_FIRST_VARIATION_20260908.md`.
All five coordinates have indices 0,...,2s-1. The third staircase
coordinate has cut u=s-Delta, with 1<=Delta<s; the other three have
cut s. Write y for the fifth, absorbed coordinate. The four threshold
bits must be nonincreasing.

The original balanced four-axis hook partition has chains indexed by
j_2,j_3,j_4 in {0,...,s-1}. Their initial and final points are

    (0,j_2,j_3,j_4),
    (2s-1-j_2,2s-1-j_3,2s-1-j_4,2s-1),

and their lengths are 8s-3-2(j_2+j_3+j_4). The endpoint formula follows
by induction in A.20: each later j is at most s-1, so truncating that
many terminal points remains on the previous last-coordinate segment.

Every old chain with j_3<u remains entirely inside the asymmetric
staircase. Call these the retained bulk chains. After multiplying each
by [2s] in y and taking the complete product SCD, their count is exactly

    2s*u*s^2=2s^4-2Delta*s^3.                      (1)

Indeed each retained four-axis chain has length at least
2s+3+2Delta>2s. The product SCD therefore has exactly 2s children.

The points outside this retained bulk have the following DISJOINT
description. All intervals below contain their integer endpoints:

    R_1:
      s<=x_1<=2s-1,       s<=x_2<=s+Delta-1,
      u<=x_3<=2s-1,       0<=x_4,y<=2s-1;

    R_2:
      s<=x_1<=2s-1,       s+Delta<=x_2<=2s-1,
      u<=x_3<=s-1,        s<=x_4<=2s-1,
                              0<=y<=2s-1.          (2)

For an explicit derivation, adjoining a length-N coordinate with cut
u to a chain E of length L whose last h members are above the previous
cut gives the hook {i>=L-h or z<u}. Its outer hooks j<min(h,u) leave,
when h>u, precisely [L-h,L-u) x [u,N). At coordinate three, h=s,
so this remainder consists of the last-coordinate segment x_2 in
[s,s+Delta), with x_3>=u; the first two-axis hook endpoints make x_1
range independently over [s,2s). The following fourth coordinate is
unrestricted because these third-coordinate values are high, giving
R_1. The surviving third-coordinate hooks have last-high count
s+Delta. At coordinate four, their excess-high rectangle has
x_3 in [u,s), x_4>=s, and x_2=2s-1-j_3 with j_3<u. This gives R_2.
The same outer hooks supply exactly the retained original bulk above.

## 2. The two principal remainders are incomparable

Let R_1^+ be the part of R_1 with x_3>=s. For every point v in R_1^+
and w in R_2,

    v_2<w_2,                    v_3>w_3.           (3)

They are therefore incomparable regardless of the other coordinates.
Thus no chain can meet both R_1^+ and R_2. This statement holds in the
FULL asymmetric poset, even if a proposed joining chain is permitted
to pass through extra bulk points.

These pieces are ordinary boxes. Their side lengths, respectively,
are permutations of

    (s,Delta,s,2s,2s),
    (s,s-Delta,Delta,s,2s).                        (4)

Each has a standard product SCD attaining its maximum rank. At first
order in epsilon=Delta/s, their widths are

    width(R_1^+)=(5/3)Delta*s^3
                              +O(Delta^2*s^2+s^3),
    width(R_2)=(23/24)Delta*s^3
                              +O(Delta^2*s^2+s^3). (5)

Here the thin [Delta] factor contributes Delta times the central
density of the remaining four-box product at first order. For side
lengths (1,1,2,2), that density is
(27-2*8-2+1)/6=5/3. For (1,1,1,2), it is
[(5/2)^3-3(3/2)^3+2(1/2)^3]/6=23/24.
The finite bounded-composition formula gives the stated O(s^3)
rounding error, uniformly in 0<=Delta<=s/2; varying the other side
s-Delta gives the O(Delta^2*s^2) term. Equivalently take s to infinity
first at fixed epsilon, and then epsilon to zero.

The residual strip R_1 minus R_1^+ has two side lengths Delta and
has a line partition with at most 2Delta^2*s^2 chains. Product SCDs
of R_1 and R_2 give a matching upper bound to first order. Together
with the incomparable antichains in (3)-(5), this proves

    width(R_1 union R_2)
       =(21/8)Delta*s^3+O(Delta^2*s^2+s^3).        (6)

Thus grouping the original hook remainders into actual boxes improves
their separate indexed treatment, but cannot eliminate their principal
charge by joining the two regions to each other.

## 3. Exact consequence for a frozen-bulk strategy

Suppose a construction retains all chains counted in (1) as separate
completed chains, then covers the remaining points by additional
chains. The additional chains may contain repeated bulk points, but
the retained chains are not extended, reconnected, or replaced.
Equations (1) and (6) make its least possible total chain count

    2s^4+(5/8)Delta*s^3+O(Delta^2*s^2+s^3).        (7)

The upper direction is constructive: keep the bulk product SCD and
partition the two boxes in (2). The lower direction follows because
any added family must cover the residual antichain in Section 2.
For sufficiently small fixed epsilon>0 and then large s, (7) exceeds
the old balanced count 2s^4.

By contrast, the largest-rank calculation at this position gives
2s^4-(5/6)epsilon*s^4+O(epsilon^(4/3)s^4) in the continuum limit.
The gap does not prove a non-rank antichain obstruction for the whole
poset: the residual antichain need not be compatible with a maximal
bulk antichain. It proves that attaining the favorable derivative
requires changing the retained bulk chains, for example attaching
remainders to their ends or rerouting their internal connections.
Merely taking better SCDs of, or joining, the two separate remainders
cannot suffice.
