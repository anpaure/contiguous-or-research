# Three affine diamonds separate the shores and restore fractional room

2026-09-08. Pure orbit/complement audit, a bounded literal catalogue
check, and one exact fractional LP. The enlarged endpoint family
has fractional optimum 219428/93, below the improvement gate. No
integral cover is claimed.

Direct_route's scope audit supplied the affine direction-subspace
correction and the endpoint-mode clarification below; both are
incorporated. They do not change the literal matrices or exact LP.

## 1. The two chains and their critical translation orbits

On an affine four-point shore H, write a full word as

    C: a,p1,q1,p2,q2,p3,q3,b,
    D: a,q1,p1,q2,p2,q3,p3,b,                         (1)

with p_i != q_i for every i. Each coordinate appears twice in each
word. The swaps commute distinct coordinate increments, so D is
also a valid full geodesic. The chains have identical states at
ranks 0,1,3,5,7,8 and different states at ranks 2,4,6.

Write H0=H+a for any a in H; this is the linear direction subspace
of the affine shore. The choice of a does not affect H0.

Place the second chain on H+v, and develop the row under all eight
coordinate translations. Its physical orbit has size eight. A
nonzero translation preserving the shores cannot preserve their
rank-one unit vectors. A translation swapping shores would have
to be v, again by the shared rank-one states, and would then require
C=D, which is false.

For the short row, the critical rank pairs are

    rank7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1),
    rank9: (2,7),(3,6),(4,5),(5,4),(6,3),(7,2).

They represent six distinct target translation orbits at each
rank. A within-shore translation preserves each ordered rank pair,
and an odd-rank target has no nonzero translation stabilizer.
A shore-swapping translation can only compare opposite rank pairs.
Writing it as v+h, its condition on the common odd shore state
forces h=0: a vector invariant under nonzero h has even coordinate
sum. With h=0 the unequal even states prevent equality. Hence the
eight-row short orbit has 48 distinct targets at each critical rank.

The required defect ranks meet the edges

    {1,6},{2,5},{3,4},{2,7},{3,6},{4,5}.

They form the path 1-6-3-4-5-2-7. Its unique minimum vertex cover
is {2,4,6}. Thus (1) realizes the minimum three state differences
needed to break the elementary partner-swap critical collisions.

## 2. Diamond multigraph and complement closure

The three unordered edges {p_i,q_i} form a loopless multigraph with
degree

    deg(j)=2-1_{j=a}-1_{j=b}.                        (2)

If a=b, this is a triangle on the other three coordinates. If a
differs from b, it is either a Hamilton path from a to b or the
edge ab together with a doubled edge on the other two coordinates.

Let h=a+b, which lies in H0. For the full row, or the row with both
shores cropped to ranks 1,...,7, global complementation preserves
the translation orbit exactly when it either preserves or exchanges
the two shore words after translation by h. In the shore-preserving case the exact
conditions are

    (p3,q3)=(q1+h,p1+h),
    q2=p2+h.                                        (3)

The last equation means that the middle edge is an h-pair. These
conditions make each chain individually complement-symmetric under
h. For h nonzero, the shore-exchanging case would require a middle
coordinate to equal itself plus h and is impossible.

For h=0, the preserving case contradicts p2!=q2. The exchanging
case would require the first and third edges to be identical, which
is impossible for the triangle. Thus a=b never gives a complement-
closed translation orbit.

When a differs from b, write the other axes as c,d, so h=c+d. A
Hamilton graph must have cd in the middle and the other two edges
in path order or reverse path order. The doubled-edge graph must
have edge order cd,ab,cd. Their orientations must obey (3).

For a=b, the shared rank-three state has three ones. Exactly one
of C_4,D_4 is all ones, and the shared rank-five state has all four
coordinates positive. Thus the translation orbit hits both the
rank-seven A orbit and its rank-nine reflection. Adding its distinct
complement orbit repeats A at rank seven and its reflection at rank
nine. The translation-only distinctness theorem in Section 1 does
not imply complement-closure distinctness.

These closure claims are not asserted for arbitrary independent
endpoint modes. Value complementation exchanges the one-sided
intervals 1..8 and 0..7, while fixing 0..8 and 1..7. In particular,
the asymmetric endpoint truncations in the LP need not inherit the
underlying full pair's complement closure. The LP in Section 5
requires no bank symmetry or complement-closure assumption.

## 3. Full endpoints create one forced repeated critical orbit

The full row adds rank-seven cells (0,7) and (7,0). Since C_7=D_7,
they belong to the same target translation orbit. That orbit has
multiplicity two in the developed full row. It is distinct from
all six interior orbits: coordinate translations preserve or swap
the two shore ranks, and {0,7} differs from each interior pair.
The same argument applies to rank-nine endpoint cells (1,8),(8,1).

The rank-seven endpoint orbit is the E orbit whose canonical twos
are H0 minus {0}; its rank-nine counterpart is its reflection. Indeed,
if the last axis is b in H, normalizing its one-valued coordinate
translates the three two-valued coordinates to (H+b) minus {0}.
Thus
a full eight-row orbit has seven distinct critical orbits and eight
orbit-occurrences, with exactly this one forced repetition.

For example, on H=0123 with v=4,

    C=00223311,       D=02032131,

obey (3) with h=1. The full eight-row orbit covers every axis and
coaxis target because C begins with a doubled coordinate, its
complement symmetry handles the upper end, and all eight coordinate
translations are present. Hence it covers all 34 extremal targets.

One such full orbit plus twenty short eight-row orbits would have
168 physical rows and charge 2384. Its full endpoint repetition
already consumes the single extra critical orbit-occurrence.
This is only a budget identity, not a construction.

In fact the individually complement-closed diamond subfamily still
contains no rank-seven class-C targets. Forward Hamilton order has
critical multiset 2F+3D+E; reverse Hamilton and the doubled-edge
case have A+3B+2D. Thus an eventual construction cannot rely only
on these individually closed diamond orbits.

## 4. Complete small normalized catalogue

Normalize H=0123, v=4 and the first axis to zero. The 105 canonical
full C words are taken modulo permutations of 1,2,3. Exactly 68
satisfy the three unequal-pair conditions in (1):

    48 Hamilton paths, 12 edge-plus-double graphs, 8 triangles.

There are ten individually complement-closed normalized pairs,
four of which give the full extremal repair described above.
All 68 pairs were checked literally for shared odd/different even
states, eight physical translated rows, six distinct short critical
orbits, and the unique extra full endpoint orbit.

All sixteen ordered endpoint-mode pairs were retained for these
unequal shores. This gives 68*16=1088 columns. Keeping ordered modes
is safe even when some physical columns coincide after swapping
shores; no row type is omitted.

## 5. Exact enlarged-family fractional gate

Add the 1088 affine-diamond endpoint columns to the complete 2100
translation-copy endpoint columns from
`Q3_D8_COPY_PROFILE_AND_ALL_TRANSVERSAL_EXACT_GATES_20260908.md`.
The enlarged family has 3188 columns and the sixty exact AGL target
orbits. Every target orbit is eligible.

One LP returned matching unscaled rational primal and dual
certificates, each with nineteen nonzero entries. Every column
inequality and every target-demand inequality was checked exactly.
The fractional optimum is

    K = 219428/93 = 2359.440860215...,

with headroom

    76545/32 - K = 96989/2976.                       (4)

The positive margin applies to the entire mixed endpoint family in
this section. It does not establish that the smaller complement-
closed exact-critical bank discussed in Section 3 is feasible.
No integer search or physical cover replay ran.

## 6. Runtime and files

One h100 process used a five-second outer cap, a three-second LP
limit, two-CPU affinity, and a 1 GiB address-space limit. Times were

    normalized catalogue/structural checks: 0.0846189996227622 s;
    single LP: 0.09046965464949608 s;
    complete process: 0.6675871596671641 s.

Files:

* `q3_d8_affine_three_diamond_fractional_gate_20260908.py`;
* `Q3_D8_AFFINE_THREE_DIAMOND_FRACTIONAL_SUMMARY_20260908.jsonl`;
* `Q3_D8_AFFINE_THREE_DIAMOND_FRACTIONAL_CERTIFICATE_20260908.json`.

The certificate preserves all physical chain words and endpoint
modes, pair structure metadata, the full integer incidence matrix,
target orbit metadata, and both exact rational certificates.
