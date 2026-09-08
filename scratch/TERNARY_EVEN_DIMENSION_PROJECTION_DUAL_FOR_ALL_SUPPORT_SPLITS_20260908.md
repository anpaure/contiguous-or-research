# The ternary projection dual is valid for every support split

2026-09-08. Author: appendix_a. Pure proof; no mathematical computation
or new search. Root independently rederived and passed the general
proof. Direct-route full-file analytical audit passed, including all
support splits, empty shores, and the fractional-optimum corollary.

## 1. Unrestricted row theorem

Let d=2m with m>=1. For x in {0,1,2}^d, define

    y(x) = (1/m)*#{a : sum_(i!=a) x_i=d-1}.          (1)

Let C,D be any nonempty strict coordinatewise chains on complementary
supports of sizes r and s, where r+s=d. Empty support parts are
permitted; a chain on an empty support then has one state. There is
no saturation, endpoint, equal-length, or balance requirement. Then

    sum_(x in C x D) y(x) <= |C|+|D|.               (2)

The total target weight is

    sum_x y(x) = 6*[t^(d-1)](1+t+t^2)^(d-1)
               = 6 W_3(d-1),                       (3)

where W_3(d-1) denotes that central ternary rank size. Thus (1) is
a cost dual for integral or fractional chain-pair covers allowing
arbitrary support splits. The proof below fills the gap left by the
balanced-only incidence argument in Section 4B of
`Q3_D8_MIXED_ENDPOINT_EXACT_FRACTIONAL_MARGIN_20260908.md`.

## 2. A graph with three possible edge diagonals

Extend C and D to full saturated chains in their respective cubes.
This is possible by filling the coordinate increments between
successive comparable states, and before and after their endpoints.
The original chains are subsets of these extensions. No extension
states are charged or selected until explicitly added below.

Exchange shores if necessary so r<=s, hence r<=m. Write the extended
states as C_i, 0<=i<=2r, and D_j, 0<=j<=2s, indexed by total rank.
Let a_i be the number of ones in C_i. Reverse the right rank index:
write b_k for the number of ones in D_(d-k). Its legal indices are

    2r-d <= k <= d.

Both a and b change by exactly plus or minus one between consecutive
legal indices, because each saturated ternary step either opens a
coordinate from zero to one or closes it from one to two.

Make a bipartite graph with left rank vertices i and right reversed-rank
vertices k. The selected vertices encode the original chain members.
Give the edge (i,k) weight y(C_i,D_(d-k)); edges of zero weight may
be omitted. The row's weight is precisely the total edge weight in
the subgraph induced by its selected vertices, and its charge is
the number of those vertices.

If a target has rank d-1, its y-value is n_0/m; at rank d it is
n_1/m; at rank d+1 it is n_2/m. Other ranks have zero weight. Thus
an edge is possible only when |i-k|<=1. Put H_i=a_i+b_i wherever
both sides' indices are legal. The edge weights are

    (i,i):       H_i/m,
    (i,k), |i-k|=1: (d+1-a_i-b_k)/(2m).             (4)

For the second formula, at either outer rank the relevant number
of zeros or twos is (d+1-n_1)/2. Every outer edge has weight at most
one: a rank d-1 target has at most m zeros, and a rank d+1 target
has at most m twos. All edge weights are nonnegative.

The common legal index interval is

    I={0,...,2r}.

Every selected vertex outside I is a right vertex. Only k=-1 and
k=2r+1 can have a neighboring left vertex, and each has at most
one such neighbor. All other exterior right vertices have degree
zero. Removing any exterior vertex therefore removes weight at
most one and removes charge one. This cannot decrease the quantity

    selected edge weight minus selected vertex count.              (5)

It suffices to prove that (5) is nonpositive for selections inside I.

## 3. Fill missing vertices without decreasing weight minus charge

Call an index full when both of its vertices are selected. If there
is no full index, there is at most one selected vertex at each index,
and every possible edge joins consecutive indices. The selected
graph is a subgraph of a path. Each edge weighs at most one, so its
total weight is at most its number of vertices. This proves the
desired inequality in that case.

Suppose now that some index is full. Grow a contiguous interval of
full indices outward from it, one index at a time. At each step a
neighboring index j is already full and |i-j|=1.

If the next index i is already full, nothing is added. If it has
exactly one selected vertex, add its missing mate. For example,
adding the right mate adds the central edge and its edge to the
already selected left vertex at j. Their combined weight is

    H_i/m + (d+1-a_j-b_i)/(2m)
      = (d+1+H_i+a_i-a_j)/(2m)
      >= (d+H_i)/(2m) >=1.                         (6)

Here a_i-a_j is plus or minus one and d=2m. If the missing mate
is left, the identical calculation uses b_i-b_j instead. The new
vertex costs one, so (5) cannot decrease. Any additional edges to
other previously selected vertices only improve this conclusion.

If index i is empty, add both its vertices. They add their central
edge and both outer edges to the full index j. The total new weight
from these three edges is

    H_i/m + (2d+2-H_i-H_j)/(2m)
      = (2d+2+H_i-H_j)/(2m) >=2.                   (7)

Indeed each of a and b changes by plus or minus one, so
H_i-H_j>=-2. The two new vertices cost two. Again (5) cannot
decrease, including when other new edges are present.

Continue to the two ends of I. These additions use actual states
of the two saturated extensions, so they are legal enlarged chain
selections. They produce the full common interval. It remains to
bound its weight by its vertex count.

## 4. The full-interval weight telescopes

For any full interval of L consecutive common indices, the two
outer edge weights between i and i+1 sum to

    (2d+2-H_i-H_(i+1))/(2m).

Adding all central edges and these adjacent pairs cancels every
interior height. If alpha and beta are the endpoint indices, the
total weight is exactly

    ((2m+1)/m)*(L-1) + (H_alpha+H_beta)/(2m).        (8)

The height bounds on a ternary path give

    a_i <= min(i,2r-i),
    b_i <= min(d-i,d-2r+i).

Consequently throughout I,

    H_i <= d-2*|i-r|.

Since beta-alpha=L-1, the triangle inequality yields

    H_alpha+H_beta <= 2d-2*(L-1)
                    =4m+2-2L.                     (9)

Substitution into (8) gives weight at most 2L, exactly the number
of selected vertices in a full interval. This includes L=1 and
r=0; when both endpoint indices coincide their height is counted
twice in (8).

Thus (5) is nonpositive after filling, and hence was nonpositive
before filling and before removing exterior vertices. This proves
(2) for arbitrary original strict chains. Finally, for each deleted
coordinate its own value has three choices and the other d-1 values
have total rank d-1. Summing the d deletion tests and dividing by
m proves (3).

## 5. Exact unrestricted fractional optimum in dimension eight

For d=8, the central seven-coordinate rank has size

    [t^7](1+t+t^2)^7 = 1+42+210+140=393.

The unrestricted dual total is therefore 6*393=2358. The nineteen-term
rational primal in Section 3 of
`Q3_D8_MIXED_ENDPOINT_EXACT_FRACTIONAL_MARGIN_20260908.md`
already gives a fractional balanced cover of that same charge.
Its forty-five histogram constraints were checked exactly, and
uniform coordinate-permutation averaging of each actual row makes
it a cover of every individual target. Those balanced rows belong
to the unrestricted family as well. Hence

    inf fractional charge over ALL strict ternary-eight
    chain-pair rows with arbitrary support splits =2358.            (10)

No new computation of the primal is needed: its saved exact
certificate supplies the upper bound, and the pure theorem above
supplies the unrestricted lower bound. This does not round that
fractional cover into an integral template.

For an actual cover with multiplicity load(x), the strengthened
inequality is

    total charge >=2358 + sum_x y(x)*(load(x)-1).     (11)

Thus unbalanced repair rows cannot evade projection penalties from
already forced repetitions. In particular, the U16 bundle's excess
twenty-eight gives charge at least2386 even when every other row has
an arbitrary split. Retaining also the copied palindrome P4 gives
at least2392. These bounds use the exact repeated target orbits
proved in Section 5 of
`Q3_D8_U_STRIPS_PALINDROME_2384_AVAILABILITY_AND_CORNER_OBSTRUCTION_20260908.md`.

Any further repeated-load penalty, such as its additional sixteen
from E_H and its reflection, also obeys (11) once that repetition is
established. Its separate geometric assumptions for forcing those
targets remain necessary; unrestricted dual validity does not by
itself extend a saturated-corner argument to arbitrary nonsaturated
repair rows.

The result settles the proposed unbalanced-row dual-gain route:
there is no strict row exceeding its charge under y. Integral charge
2358 or an improving integral charge at most2392 is not constructed
or excluded by this theorem alone.
