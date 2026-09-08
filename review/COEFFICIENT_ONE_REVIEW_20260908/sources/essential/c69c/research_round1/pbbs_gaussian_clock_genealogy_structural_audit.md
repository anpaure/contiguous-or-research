# PBBS short clocks expose a deterministic triangle of original pruning slots

Date: 2026-09-07. Pure proof, written by the Gaussian residual subagent.
Original project files are read-only. No computation was used.
Local review record: the worktree lead and the independent recency-gate
agent fully reviewed Sections 1-5 and Appendix A; both reviews pass.
The reached-height invariance clarification also passed. The coordinator
has now accepted the theorem after separate structural and analytic
audits, both passing on 2026-09-07.

This note supplies a structural estimate for the actual full-lifetime
event. It uses the exact equality-particle renormalization and the
one-start renewal identity, rather than a fresh law at reached states.
The separate analytic transfer is in pbbs_gaussian_clock_analytic_transfer.md.

The principal conclusion is (12): a short lifetime at height comparable
to its cutoff forces a bounded sum over a FIXED triangular collection of
original inverse-pruning coordinates. The number of these coordinates
at pruning depth s is s+1. The coordinates are not newly sampled at
different dynamical visits.

## 1. Original pruning arrays and their exact law

For a Dyck root D, put D_s=partial^s D and r_s=|D_s|_up, where partial
simultaneously deletes all peaks. Write h=ht(D), so r_h=0 and r_s>0
for s<h. Fix the entire feasible profile (r_0,...,r_h).

At a level s with nonempty core D_(s+1), let

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).                         (1)

There are p_s equality particles in the cyclic word 0D_s. Label them
persistently in cyclic order, with label 0 on the edge immediately
before the original unmatched zero. The recorded particle word is
0D_(s+1). For particle j, let L_j be the positive cyclic distance from
particle j-1 to particle j, and let epsilon_j be one if their recorded
bits differ, zero otherwise. Define the original incoming-gap coordinate

    Z_(s,j)=(L_j-1-epsilon_j)/2.                         (2)

Between consecutive equality edges, physical bits alternate. Therefore
L_j=2Z_(s,j)+1+epsilon_j with Z_(s,j)>=0. Summing distances gives

    sum_j Z_(s,j)=ell_s.

Here sum epsilon_j=2 pk(D_(s+1)) and
pk(D_(s+1))=r_(s+1)-r_(s+2).

The vector Z_s is an exact encoding of the inverse-pruning fibre over
D_(s+1). The core bits and all gap distances reconstruct the original
cyclic word and its specified root uniquely. Its vector is a weak
composition of ell_s into p_s parts. Conversely, the known exact fibre
size is binom(ell_s+p_s-1,p_s-1), exactly the number of such compositions.
Injection and this finite equality prove that every composition is
admissible. This also identifies the usual terminal free-leaf occupancy
with Z_(s,0).

Consequently, conditional on the complete pruning profile, the original
vectors Z_s are independent uniform weak compositions. This follows by
reconstructing from the bottom core upward: at each level the fibre size
depends only on the profile, not the particular core word. The last
nonempty core is the uniquely determined height-one word (10)^(r_(h-1)).
Only nonempty-core levels will be queried below.

## 2. Every gap coordinate is invariant under the dynamics

Apply one physical PBBS update at a level with nonempty reduced core.
Its selected equality particle a advances one physical edge. Thus its
incoming distance L_a increases by one and its outgoing distance
L_(a+1) decreases by one. Other distances do not change.

In the recorded particle word rooted at a, the selected bit is zero,
its predecessor bit is zero, and its successor bit is one. The update
complements every other recorded bit and leaves the selected zero fixed.
Hence epsilon_a changes from zero to one and epsilon_(a+1) changes
from one to zero. All other epsilon values are unchanged. Formula (2)
therefore shows that EVERY Z_(s,j) is invariant, with persistent indices.

In particular, a later terminal occupancy query reads one of the
ORIGINAL coordinates Z_(s,j), without a time-dependent offset. This is
not a statement that the queries are independent: repeated queries of
one coordinate read the same value.

## 3. Two exact clocks

At a physical PBBS phase with selected label a, define two clocks:

* T is the interval until the next selection of that same label a.
  Its physical length is 2T(D)+1, with the established newborn-lifetime
  convention.
* C is the interval until the next selection of the physical predecessor
  label a-1. Its physical length is 2C(D).

The notation C in this note denotes this clock, not a Catalan generating
function. Selections of adjacent physical labels strictly alternate.
To see this, consider edge (a-1,a). A selection at its right endpoint
requires incoming bits 00 and changes the edge to unequal bits 10.
Until an endpoint is selected, both bits are complemented together, so
equality cannot change. Another right-endpoint selection is impossible
until the left endpoint is selected. A left-endpoint selection requires
outgoing bits 01 and changes them to 00; another such selection is
impossible until the right endpoint is selected. The full-label property
ensures eventual events in both directions. Initial predecessor bit zero
forces the first predecessor selection time to be even.

In the reduced PBBS, call the currently selected equality particle b and
its predecessor b-1. Let

    0<B_1<B_2<... 

be successive positive selection times of b-1. If the original terminal
coordinate is z, the initial particle distance is 2z+1: both recorded
endpoint bits are zero. Before a spatial wrap, particle b-1 selects the
physical label a-1 on its (2z+1)st move and the physical label a on its
(2z+2)nd move. The exact physical clock partition is therefore

    C parent: child C, then 2z child T clocks;
    T parent: child C, then 2z+1 child T clocks.         (3)

The child C runs from the starting time to B_1; the subsequent child T
clocks are the intervals [B_j,B_(j+1)]. These intervals are adjacent,
disjoint except for endpoints, and cover the parent clock exactly.
Their child roots are actual reached phases of the same reduced PBBS.

For example, writing F=partial D, Psi(F)=phi^(B_1)F, and R for the
same-label return permutation on reduced phases, (3) is equivalent to

    C(D)=C(F)+sum_(j=0)^(2z-1) T(R^j Psi(F))+z,
    T(D)=C(F)+sum_(j=0)^(2z)   T(R^j Psi(F))+z.         (4)

An empty sum is zero. The terms are generally correlated. No product law
on the reached roots R^j Psi(F) is being asserted.

We use (3) only while the entire outer physical horizon G is smaller
than the circumferences at the relevant levels. This excludes the wrap
alternative. All child clocks lie inside that same outer interval, so
the restriction automatically passes to every node in the truncated
genealogy. Taking G<2r_L+1 is sufficient for levels s<L; on a short root
the even C subintervals are strictly shorter than the possible N-1
move of one particle around to the predecessor site.

## 4. The original slot order is deterministic

Expand an outer T clock using (3), through L pruning levels for which
the preceding circumference condition holds. At every depth the nodes
are a chronological partition of the SAME physical interval [0,G].
Their left endpoints are distinct.

At depth s, a node queries the incoming gap of the currently selected
persistent particle at level s+1. A C clock at level s+1 changes that
level's selected physical label by -1. A T clock at that level ends at
the same selected physical label. Every depth-s node has exactly ONE
child C, followed only by child T clocks. Its completion therefore
changes the selected particle index at level s+1 by exactly -1.

Initially the selected persistent label is 0 at every level. It follows
that the chronological depth-s queries are exactly

    Z_(s,0), Z_(s,-1), Z_(s,-2), ...                    (5)

with indices modulo p_s. There is no dependence of this order on any
unexposed coordinate. The number of queries can depend on their values.
If fewer than p_s nodes occur, all queried coordinates are distinct.

This is stronger than bounding repetitions by a return-time argument.
It also avoids a deferred-decisions assumption about a trajectory oracle.
The necessary event derived below concerns a fixed prefix of (5).

## 5. A short outer lifetime allows only bounded total queried mass

Let n_s be the number of all clocks at depth s, m_s the number of T
clocks, and W_s the sum of their n_s queried gap coordinates. Start with
n_0=m_0=1. Formula (3) gives exact identities

    m_(s+1)=m_s+2W_s,
    n_(s+1)=n_s+m_s+2W_s.                              (6)

Thus

    n_s>=s+1,
    sum_(s=0)^(L-1) W_s=(m_L-1)/2.                   (7)

The original pruning profile remains the profile at every reached phase.
Indeed equality-particle renormalization preserves cyclic particle order
and count, and identifies the recorded word after an update with the
PBBS update of the peak-deleted word. Thus partial commutes with phi;
iterating gives partial^j phi^t D=phi^t partial^j D (with the appropriate
reduced map on the right). At each level its rank is unchanged by that
reduced dynamics, so every r_j is invariant. Height is the first pruning
depth at which the word becomes empty. Consequently every REACHED
depth-L root has height exactly h-L, not merely the original root D_L.

Every depth-L T interval therefore has physical length at least
2(h-L)+1, by the proved height-gap theorem. These intervals are disjoint
within the outer interval, so

    m_L <= G/[2(h-L)+1].                               (8)

All node intervals have positive integer lengths, hence n_s<=G. Suppose

    G=2T(D)+1<=2H+1,
    h>L,
    p_s>G for 0<=s<L.                                  (9)

Then the first n_s entries in (5) have not wrapped and, by n_s>=s+1,
nonnegativity gives

    sum_(s=0)^(L-1) sum_(j=0)^s Z_(s,-j)
      <= sum_(s=0)^(L-1) W_s
      <= ( G/[2(h-L)+1]-1 )/2.                       (10)

Every coordinate on the left side is an original fibre coordinate with
a predetermined index. In particular, for fixed a,c>0, if

    h>=a sqrt(r),   T(D)<=c sqrt(r),

then for every fixed L and sufficiently large r satisfying (9),

    sum_(s=0)^(L-1) sum_(j=0)^s Z_(s,-j) <= K_(a,c),  (11)

where any fixed integer K_(a,c)>c/(2a) suffices. The exact constant is
unimportant; it is independent of r and L in the iterated-limit use.

Thus the structural conclusion is

    {h>=a sqrt(r), T<=c sqrt(r), regular first L levels}
       is contained in
    {sum of the fixed triangular coordinates <=K_(a,c)}. (12)

The number of levels L may first be fixed, r sent to infinity, and only
then L sent to infinity. No estimate for a growing number of pruning
levels is necessary.

## 6. Exact probabilistic transfer target

For a uniform composition of ell into p parts, any fixed finite list of
distinct coordinates converges to independent geometric variables when
ell,p tend to infinity with a fixed positive ratio. The limiting positive
probability is q=ell/(ell+p), and P(Z=k)=(1-q)q^k. This follows directly
from the ratio of the two stars-and-bars counts after fixing those
coordinates.

If the standard fixed-depth Catalan fringe law is supplied in the form

    r_s/r -> 1/(s+1) in probability,
          for every fixed s,                           (13)

then (1) gives

    ell_s/p_s -> 1/[(s+1)(s+3)],
    q_s -> 1/(s+2)^2.                                  (14)

Conditional-profile independence from Section 1 makes the finitely many
triangular coordinates asymptotically independent across all fixed
levels. No reached-state independence is used. Let S_L be their sum.
For each fixed L,

    limsup P(S_L<=K)
      <= exp{K-(1-e^(-1)) sum_(s=0)^(L-1)
                                   (s+1)/(s+2)^2}.    (15)

Indeed 1{S_L<=K}<=exp(K-S_L), and a geometric variable
satisfies E exp(-Z)<=1-(1-e^(-1))P(Z>0).
The sum in (15) diverges as log L. Consequently (12)-(15) give

    P(h>=a sqrt(r), T<=c sqrt(r)) -> 0                 (16)

for every fixed a,c>0, using (13) as proved in Appendix A. Letting a
decrease to zero and applying the Dyck-height small-ball estimate proved
in pbbs_gaussian_clock_analytic_transfer.md gives

    P(T<=c sqrt(r)) -> 0 for every fixed c>0.          (17)

The coordinator's independent structural and analytic audits passed.
Appendix A below gives a direct proof of the profile input (13). The strongest new
structural input is the deterministic implication (12), not an averaged
entry kernel or a reset of the residual lifetime law.

## 7. A literal one-level clock check

The existing symbolic family from
pbbs_original_node_charge_counterexample.md is useful here. Put A=10 and

    D_b=111000 1 A^b 0,       b>=3.

It has height three, semilength b+4, and lifetime T=6, so its physical
horizon 13 is below its outer circumference 2b+9. Its core is

    F=partial D_b=110010,
    partial F=10.

The original level-zero gap array, indexed as in (2), is

    (Z_(0,0),...,Z_(0,6))=(0,0,0,0,0,0,b-1).

This follows by listing the seven equality edges: the only enlarged
interparticle gap is from the up-equality edge at the start of 1 A^b 0
to its final down-equality edge. Its distance is 2b, and its epsilon is
one. In particular the FIRST query is the original terminal z=0,
although a different original slot contains arbitrarily large mass.

In the reduced phase F, the next-predecessor clock is C(F)=4, and its
endpoint is Psi(F)=101100. The literal lifetimes are T(F)=5 and
T(Psi(F))=2. Thus the one-level partition gives

    C(D_b)=4,
    T(D_b)=C(F)+T(Psi(F))=4+2=6.

The reached child is explicitly Psi(F), not a fresh copy of F. The
second original level-zero slot is not resampled. This example checks
the local clock identity only: its reduced circumference is seven, so
the stronger sufficient global no-wrap condition in (9) is not met.
It is not a Gaussian profile example.

## Appendix A. A direct fixed-depth pruning-profile law

Here C(z)=sum Cat_r z^r is the ordinary Catalan series for plane trees
with edges counted by z. A fringe subtree at a vertex consists of that
vertex and all its descendants. Fix one plane-tree shape A with k edges,
and let N_A(D) count its fringe occurrences, including the root if it
matches. The generating function of contexts with one subtree hole is

    1/(1-zC(z)^2).

Indeed every ancestor of the hole has a distinguished child edge and
arbitrary ordered lists of children on both sides, giving zC^2 per
ancestor. Therefore

    sum_D N_A(D) z^(|D|_up)=z^k/(1-zC^2).             (A1)

Since zC^2=C-1 and
1/(2-C)=(1+(1-4z)^(-1/2))/2, for r>k the coefficient
in (A1) is (1/2) binom(2(r-k),r-k). Thus

    E N_A(D)/r -> 4^(-k)/2.                            (A2)

For fixed shapes A,B of sizes k,l, ordered pairs of disjoint fringe
occurrences have generating function

    z^(k+l) 2z^2 C^3/(1-zC^2)^3.                     (A3)

To obtain (A3), use a context above their lowest common ancestor, the
two distinguished child branches below it in either order, the three
intervening child lists, and independent contexts in the two branches.
The leading singular term of (A3) at z=1/4 is

    4^(-k-l) (1-4z)^(-3/2)/8.

Dividing coefficients by Cat_r gives

    E[ordered disjoint pair count]/r^2
       ->4^(-k-l)/4.                                  (A4)

The overlapping pairs contribute O(r): if one fixed-shape occurrence
contains the other, it has only a bounded number of possible descendant
occurrences. Equations (A2)-(A4) prove convergence in probability of
N_A(D)/r to 4^(-k)/2, jointly for every finite list of shapes.

To pass from finite lists to an arbitrary bounded fringe indicator,
truncate by fringe size. The expected number of fringe occurrences of
size exactly k<r is

    Cat_k (1/2) binom(2(r-k),r-k)/Cat_r.

After dividing by r, the usual central-binomial bounds give a summand
at most

    C sqrt(r)/[(k+1)^(3/2)(r-k+1)^(1/2)].

For M<k<=r/2 their sum is O(M^(-1/2)); for r/2<k<r it is
O(r^(-1/2)). The root occurrence k=r contributes 1/r. Therefore the
expected fraction of vertices with fringe size above M is at most

    C M^(-1/2)+O(r^(-1/2)).                            (A5)

Markov's inequality, finite-shape convergence, and then M->infinity
prove the fringe law for every bounded indicator. The limiting fringe
tree has probability 4^(-k)/2 for each shape with k edges; the masses
sum to C(1/4)/2=1.

A nonroot edge survives s simultaneous leaf-pruning rounds exactly
when its child vertex has a fringe subtree of height at least s. The
root changes the vertex count by at most one. Under the limiting fringe
law, for s>=1,

    P(fringe height>=s)
      =1-C_(s-1)(1/4)/2
      =1/(s+1).

The s=0 case is immediate. This proves (13), jointly for every fixed
finite number of depths, without a growing-depth concentration theorem
or a dynamical mixing assertion.
