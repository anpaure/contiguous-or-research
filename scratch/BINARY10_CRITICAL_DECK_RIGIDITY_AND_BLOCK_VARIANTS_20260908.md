# Critical-deck rigidity and exact block-row variant constraints

2026-09-08. Pure theory; no computation or solver. Root and independent
direct-route full-file audits passed. All targets are the designated prefix unions of a
balanced 5+5 row; full complements are not silently added to coverage.

## 1. A rigidity theorem for every 42-row balanced bank

One row is an ordered partition (L,R) of ten coordinates into shores
of length five. Its targets are L_[i] union R_[j], 0<=i,j<=5. Within
the row these 36 targets are distinct. In ranks 4,5,6 it contributes
5,6,5 targets. Thus 42 rows contribute exactly

    210,252,210 = binom(10,4),binom(10,5),binom(10,6)

occurrences in those ranks. A full cover must be an exact deck in all
three ranks.

Fix a coordinate at position q in its shore, 1<=q<=5. It occurs in
5-q,6-q,6-q row targets at ranks 4,5,6 respectively: count the possible
prefix lengths i>=q with 0<=k-i<=5. Across the full cube the corresponding
coordinate incidences are 84,126,126. Therefore, for every coordinate a,

    delta_4(a)=delta_5(a)=delta_6(a),                (1)

where delta_k is the bank's multiplicity-weighted rank-k incidence
minus the full rank-k deck incidence. The difference of 42 between the
first two row-bank counts cancels 126-84 exactly.

Consequently, a bank with only ONE missing cube target cannot have
that target in a critical rank. If its sole critical hole is A, that
rank has exactly one excess occurrence at some B!=A, while the other
critical ranks are exact. Equation (1) would give 1_B-1_A=0, impossible.
This statement permits the sole hole to be in a noncritical rank; it
does not assert that such a bank exists.

More generally, suppose all critical ranks except rank k are exact,
and rank k has exactly two distinct holes H_1,H_2. Its two excess
occurrences, allowing multiplicity at the same target, must have the
same incidence sum as H_1,H_2. If |H_1 intersection H_2|=k-1, this is
impossible. Indeed every coordinate in their intersection must lie in
both excess sets, every coordinate outside their union in neither,
and the two remaining coordinates must be split one to each. The
only two k-sets are then H_1,H_2 themselves, which are absent. Thus
two adjacent rank-six holes cannot be repaired by a different two-set
incidence trade while the other critical decks remain exact. Holes
whose difference has at least two exchanges can admit such trades;
the stated obstruction is specifically the one-exchange case.

## 2. Simultaneous shore reversal cannot pair an exact bank

Reversing both shore orders maps the complement of every row target
to a target of the reversed row. But both rows still contain the
SAME two central targets L and R: neither full shore set changes.
Hence a row and its simultaneous reversal repeat at least two rank-five
targets. No exact 42-row bank can contain such a pair, and in particular
it cannot be closed under simultaneous reversal. Swapping shore names
does not remove the duplication.

For a block row on one oriented middle-levels Hamilton cycle, its
right shore is the uniquely assigned first rank-five target U_(s-1).
The reversed row has the same right shore. If it were another forward
block of that same cycle, its first U would force the same start index,
but its first S removes the opposite endpoint of the right ordering
and hence is different. The central-rank argument above is stronger:
changing the cycle or orientation does not rescue an exact paired bank.

## 3. Block notation and the three z-present decks

Use a valid consecutive block from
`MU9_TO_BINARY10_CONSECUTIVE_BLOCK_OBSTRUCTION_20260908.md`. Let Q be
the nine nonpivot coordinates, let p be its number of assigned S
targets, and put m=5-p. Its row is

    L=(a_1,...,a_(p-1),z,c_1,...,c_m),
    R=(k_1,...,k_m,d_(p-1),...,d_1,b).

Write A={a_1,...,a_(p-1)}, K={k_1,...,k_m}, and C={c_1,...,c_m}.
Only the orders of K and C are free, giving (m!)^2 variants. Denote
the fixed first and last assigned no-z five-sets by R_0=R as a set
and U_end. Let S_end be the final assigned no-z four-set. Then

    S_end=A union K,
    Q minus R_0=A union C,
    U_end=A union K union {R_(m+1)}.                (2)

For h=0,...,m define the four-set

    P_h=A union {c_1,...,c_h}
            union {k_1,...,k_(m-h)}.               (3)

These form a geodesic path in the Johnson graph on four-subsets of Q,
from the FIXED S_end to the FIXED Q minus R_0. At its hth step, for
h=0,...,m-1, it removes k_(m-h) and inserts c_(h+1).

After deleting z, the z-present rank-4, rank-5, rank-6 decks of this
row are exactly, respectively,

    P_h intersection P_(h+1),       0<=h<m;         (4)
    P_h,                           0<=h<=m;        (5)
    P_h union P_(h+1),              0<=h<m,
          together with U_end.                     (6)

To verify this directly, a z-containing prefix has left length p+h.
At total rank four, the right prefix length is m-1-h; at rank five it
is m-h; at rank six it is m+1-h. The first two give (4)-(5). For rank
six, h=0 gives the fixed set U_end, and h=1,...,m give the unions in
(6). This also handles m=0: no triples, one four-set, and only U_end
as a five-set. The core ranks in (4)-(6) are 3,4,5.

## 4. Exact path-deck completion problem

Suppose 126 consecutive S positions have been partitioned into 42
valid blocks. Then sum p=126 and sum m=84. The no-z four- and five-
decks are automatically exact. Completing ALL three z-present critical
decks is equivalent to choosing one path (3) per block such that:

* the path vertices partition all 126 four-sets of Q;
* the 84 edge intersections give all 84 triples exactly once;
* the 84 edge unions partition the five-sets outside the 42 fixed
  distinct U_end targets.

This is an equivalence for these three decks only. Full-cube coverage
still needs all other ranks, and the no-z six-deck must also pass its
separate boundary test.

There are immediate variant-free necessary conditions. The 42 starts
S_end and the 42 terminal sets Q minus R_0 must not collide, except
for the same row when m=0 (p=5), where the path is a singleton. Thus
S_end(i)=Q minus R_0(j) with i!=j forbids exact variants. For i=j the
equality holds precisely when m=0, since K and C are disjoint.

Every edge union must avoid EVERY fixed U_end. Every available triple
for a block with m>=1 has the form A union B, with B a subset of
K union C of size m-1. Every available four-set has the same form
with |B|=m, and every nonfixed five-set with |B|=m+1. All these individual
sets are attainable by suitable orders. Missing targets from the union
of the corresponding availability families therefore forbid a deck;
the path correlations remain additional conditions.

## 5. Forced coordinate-swap multiplicities before ordering

Let E_end be the MULTISET consisting of both endpoints of each path,
counting the endpoint twice for a singleton path. For a coordinate set
X, let e_X count endpoint occurrences containing X, and let u_X count
the fixed U_end sets containing X.

If the three decks in Section 4 are exact, then for each coordinate a,

    e_a=14+u_a.                                    (7)

For each unordered pair {a,b}, the number h_ab of path steps which
exchange a and b is forced to be

    h_ab=e_{a,b}-u_{a,b}.                          (8)

Proof: a path system has vertex-degree sum equal to twice its vertex
sum minus its endpoint multiset, with a singleton contributing zero
degree and two endpoint copies. For an edge with four-set ends V,W,
one-coordinate incidence satisfies
1_V+1_W=1_(V intersection W)+1_(V union W). For pair incidence, subtract
one from the right precisely when the pair is the two exchanged
coordinates. Therefore exact decks give

    2 binom(8,3)-e_a
           =binom(8,2)+binom(8,4)-u_a,
    2 binom(7,2)-e_ab
           =binom(7,1)+binom(7,3)-u_ab-h_ab,

which are (7)-(8).

In terms of the fixed boundary sets, if s_X counts S_end sets and
r_X counts R_0 sets, then

    e_a=s_a+42-r_a,
    e_ab=s_ab+42-r_a-r_b+r_ab.                     (9)

Thus all 36 desired swap multiplicities in (8) are known before any
row orders are selected. They must be nonnegative integers.

Within one block, each K coordinate is removed once and each C
coordinate inserted once. Its swaps form a perfect matching between
K and C. Conversely any such matching, in any order, gives one of
the (m!)^2 paths in (3). Hence a necessary earlier assignment stage is
to choose these per-block perfect matchings whose total unordered-pair
multiplicities are exactly (8). Only then need the swap orders be chosen
to meet the vertex, intersection, and union decks.

For example h_ab cannot exceed the number of blocks with a in K,b in C
or a in C,b in K. For ANY coordinate subset X, put k_i=|K_i intersection
X|, c_i=|C_i intersection X| and m_i=|K_i|. The fixed desired cut total
h(delta X)=sum_(a in X,b outside X) h_ab must satisfy

    sum_i |k_i-c_i| <= h(delta X)
        <= sum_i min(k_i+c_i,2m_i-k_i-c_i).          (10)

The lower bound is the unavoidable imbalance in each matching. For the
upper bound, at most min(k_i,m_i-c_i) edges can go from K inside X to
C outside, and at most min(m_i-k_i,c_i) in the other direction. Their
sum is the displayed minimum. These are exact necessary matching
conditions, not sufficient conditions for the full variant problem.

## 6. A one-hole no-z six-deck forces another critical defect

Let v_a be the multiplicity count of coordinate a in the retained
no-z rank-six occurrences. No assumption that this deck is exact is
needed here. The original no-z U targets form 42 paths of five-sets,
whose endpoints are R_0 and U_end. Consecutive intersections are all
assigned S targets except the 42 S_end sets; their unions are precisely
the retained no-z six-targets. Taking coordinate incidences gives

    2*70-r_a-u_a = (56-s_a)+v_a,
    r_a+u_a-s_a =84-v_a.                           (11)

But exactness of all three z-present decks, by (7) and (9), requires
r_a+u_a-s_a=28. Thus it forces

    v_a=56 for every coordinate a.                 (12)

If the no-z six-deck has exactly one missing target H and one excess
occurrence D, its incidence vector is 56+1_D-1_H, which cannot obey
(12) for distinct sets. Hence such a bank necessarily has at least one
additional z-present critical-rank defect. The claim does not rule out
a bank with more holes or a structured repair for them.

The general rigidity theorem in Section 1 also applies outside the
consecutive-block construction. The path formulation in Sections 3-6
applies to any valid block on any oriented middle-levels Hamilton cycle;
it uses no special feature of the previously screened cyclic mu(9)
certificate and no output from a solver.
