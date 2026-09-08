# PBBS repair through a square-root-over-log budget cutoff

2026-09-07. Root synthesis; pure proof, no computation.
Status: the full-history linear-gap input passed full root reading and
two independent root audits. The complete finite-cutoff consequence below
also passed its independent spectral/physical/charge audit. Coefficient
one remains open.

Let r be the Dyck semilength, h the invariant height of a newborn root,
T its lifetime INCLUDING consumption, and B=T-h its interruption budget.
Let W=(2r+1)Cat_r be the total physical edge count of the full PBBS factor.
The corresponding positive residence has T+1 owners and its full repair
trace has T+2 edges.

Define the integer

    L_r=min{L>=1 : 2^L>=r+1},
    J_r=max(1, isqrt(floor(r/(256 L_r)))).              (1)

Then J_r is of order sqrt(r/log r) and tends to infinity. ALL repair
traces with B<=J_r, without a lifetime or height cutoff, have

    occupied edge union o(W),
    maximum edge-disjoint packing o(W/sqrt(r)),
    o(W) distinct affected owners.                    (2)

There is also a finite computable H_r with H_r/sqrt(r)->infinity and
H_r=o(r) for which an explicit transversal of all these traces has
O(H_r)-per-cut total charge o(W). The positive-budget part is much
smaller: its raw total trace incidence and its individually charged
target repairs are negligible, so only B=0 requires shared repair.

This strengthens the previously proved o(r^(1/4)) budget range. It does
NOT control B>J_r, construct the complete PBBS word, or reduce the
unconditional full-cube coefficient.

## 1. The pointwise structural input

The fully audited theorem
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_positive_budget_linear_height_gap.md
proves, for EVERY complete newborn history with positive budget,

    h<=7rho+sigma<=(7/2)B,       B=2rho+sigma.          (3)

Here rho and sigma count surviving R and S updates. The proof maintains
an actual initial path after the mark, with defect delta obeying
P:delta->(delta-1)_+, R:delta->delta+1, S:delta->delta. A reached post-S
suffix FQ has a high initial path and a height-h trailing packet. Its
P-run barrier, valid for arbitrary reached F, charges at most three P
updates per defect decrease, plus one per nonterminal S. The original
first-packet bookkeeping bounds the initial P run by 5rho. Defect
decreases total exactly rho; hence h<=7rho+sigma. No fresh reached-root
law, original-core clearance imposed on reached F, or no-wrap condition
is used in this full-history theorem.

In particular, on 0<B<=J,

    h<=floor(7J/2)<=4J,
    T+2=h+B+2<=7J                 (J>=1).             (4)

We use these deliberately loose constants; no optimality is claimed.

## 2. An elementary, uniform bounded-height count

A Dyck word of semilength r and height at most m is a length-2r walk
from 0 to 0 in the path graph on levels 0,...,m. Its adjacency matrix
has operator norm 2cos(pi/(m+2)). Therefore the number of such roots is
at most

    [2cos(pi/(m+2))]^(2r)
       <=4^r exp[-pi^2 r/(m+2)^2].                    (5)

The last inequality follows from cos x<=exp(-x^2/2) on [0,pi/2].
For completeness, the path eigenvectors have j-th coordinate
sin((j+1)ell*pi/(m+2)); their eigenvalues are
2cos(ell*pi/(m+2)), 1<=ell<=m+1, giving the stated norm. A diagonal
matrix entry is at most the norm of its even power.

For sufficiently large r the maximum with 1 in (1) is inactive and
J_r^2<=r/(256L_r). Put m=floor(7J_r/2). Since m+2<=6J_r,

    pi^2 r/(m+2)^2
       >=(256pi^2/36)L_r
       >64L_r
       >=64log(r+1).                                 (6)

Here pi>3 and L_r>=log_2(r+1)>=log(r+1). Thus (3)-(6) imply

    #{D in Dyck_r : 0<B(D)<=J_r}
       <=4^r(r+1)^(-64).                              (7)

No asymptotic height limit is used. The elementary central-binomial
bound binom(2r,r)>=4^r/(2r+1) gives
Cat_r>=4^r/[(r+1)(2r+1)]. Dividing (7) yields the explicit probability

    Pr_Dyck_r(0<B<=J_r)<=2(r+1)^(-62).                (8)

All displayed bounds (6)-(8) are asserted for sufficiently large r;
the finite fallback in (1) only defines the cutoff at small dimensions.

## 3. Exact physical normalization and raw positive charges

The full physical dictionary assigns exactly 2r+1 births to each Dyck
root. Hence the number N_+(r) of positive-budget physical births in (8)
satisfies

    N_+(r)<=2W(r+1)^(-62).                            (9)

Each of their full traces has at most 7J_r edges by (4). Their total
trace incidence, and therefore their occupied edge union, is at most

    7J_r N_+(r)<=14J_r W(r+1)^(-62)=o(W).             (10)

In particular N_+(r)=o(W/sqrt(r)). Cutting the birth edge of every such
run is a literal physical transversal, regardless of any overlap.
Even charging O(r^p) per positive run is o(W) for every fixed p<62;
only the much smaller powers needed below are claimed for the compiler.

For the target ledger, any legal horizon 1<=H<r and a retained run of
residence length ell=T+1<=H has intended-occurrence capacity
binom(H+ell+1,2)=O(H^2). Charging each intended failure caused by this
positive class to one erased run, and appending its literal target once
per charged occurrence, costs at most

    O(H^2 N_+(r))=o(W),                               (11)

uniformly in that legal range. This is only the contribution of these
runs: other runs can cause additional failures. No equality between
actual holes and failed designated witnesses is asserted.

## 4. Add the all-height zero-budget sharing theorem

The accepted theorem PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md
in this directory gives occupied edge support o(W) and maximum
edge-disjoint packing nu_0(r)=o(W/sqrt(r)) for ALL B=0 traces. Add the
positive family of Section 3. Its support adds o(W) by (10), and any
disjoint packing adds at most N_+(r)=o(W/sqrt(r)) members. This proves
the first two claims in (2).

For the owner claim, a run born at edge e_s has owners
X_(s+1),...,X_(s+T+1), and its trace contains e_s,...,e_(s+T+1).
Map an affected owner X_i to its preceding edge e_(i-1). This is a
global injection on physical owner positions into the occupied edge
union. Hence there are o(W) distinct affected owners as well. This
does not bound owner-coordinate incidences or actual target deficits.

For a common cutoff, compute the finite zero-budget packing number
nu_0(r) and take c_r to be the largest positive integer satisfying

    c^4 r nu_0(r)^2<=W^2,          c^8<=r,             (12)

with fallback c_r=1 if the finite set is empty. Put

    H_r=isqrt(c_r^2 r).

Exactly as in the zero-budget theorem, every fixed c is eventually
admissible, c_r->infinity, H_r/sqrt(r)->infinity,
H_r<=r^(5/8)=o(r), and H_r nu_0(r)=o(W).

Open each physical cycle and take a zero-budget interval transversal,
then add all N_+(r) positive birth edges. The total cut count is at most

    nu_0(r)+Cat_r+N_+(r).                             (13)

The H_r-weighted first term is o(W); the cycle-opening charge is
H_r Cat_r/W=H_r/(2r+1)=o(1); and the positive charge is o(W) by
(9) and H_r<r. This proves the final transversal assertion. In fact all
positive runs in this class eventually satisfy T+1<=H_r, since
T+1<=7J_r=O(sqrt(r/log r)) while H_r/sqrt(r)->infinity.

Raw total incidence of the combined class need NOT be o(W): the
zero-budget subfamily still has its established order-W lower bound.
The word cost is small there because the repairs share physical cuts.

## 5. Precise remaining sector

The unresolved runs now have B>J_r. Among those short enough to affect
the selected Gaussian band, the remaining condition is

    T+1<=H_r,              B>J_r=Theta(sqrt(r/log r)).  (14)

They have at least ceil((J_r+1)/2) surviving interruption events.
Neither (3) nor the spectral bound controls their packing or weighted
target failures. The gap between this threshold and budgets of order
sqrt(r) remains substantive. The full coefficient-one conjecture and
exact equality remain open.
