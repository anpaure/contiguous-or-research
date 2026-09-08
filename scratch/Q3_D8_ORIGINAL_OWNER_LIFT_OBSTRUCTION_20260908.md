# Original binary-owner lifts require charge at least 2576

2026-09-08. Pure finite argument; no enumeration, LP, MILP, or mathematical
computation was run. This is an obstruction to a specified extension
family, not a lower bound for unrestricted ternary chain-pair covers.

## 1. Exact scope and forced targets

Use the fourteen binary rows in `MASTER_HANDOFF.md`, A.7.1. Each row has
two ordered quadruples I and J. An **original-owner lift** uses this same
shore partition and, on each shore, a full ternary geodesic in which each
coordinate is incremented twice and the first increments occur in the
original order. The second increments can occur in any permitted order.
Retain any of the four intervals 0..8, 1..8, 0..7, or 1..7 on each shore.
The actual charge is the sum of the two retained shore lengths.

The complete bank considered in Sections 2--3 consists only of these
lifts of the fourteen original owners. It can mix owners and endpoint
modes arbitrarily and can use repeated rows. Arbitrary new shore
partitions or new first-increment orders are outside this family.

The binary certificate proves that every binary support of size 3, 4,
or 5 has exactly one owner among the fourteen rows. Every point of a
ternary lift has a nonzero support that is a prefix on each of its two
original shore orders. Consequently every ternary point whose nonzero
support has size 3, 4, or 5 can be covered only by lifts of its unique
binary owner. This statement uses the nonzero support, not the total
ternary rank.

For one fixed owner, write each shore in its own original order and
denote local vectors by four digits. There are four owner supports of
size 3, five of size 4, and four of size 5. They supply respectively
4*2^3 = 32, 5*2^4 = 80, and 4*2^5 = 128 forced ternary points.
Thus each owner has 240 forced points in these three support sizes.

## 2. Twelve rows are necessary for every owner

Put

    A = 2000,       B = 1100,
    T = {2210, 2120, 1220},
    U = {2111, 1211, 1121, 1112}.

Both A and B have ternary rank 2. Every member of T or U has ternary
rank 5. Members of T have nonzero support size 3, and members of U have
nonzero support size 4.

First consider the seven targets

    (A,z),  z in T union U.                           (1)

Their total nonzero support sizes are 4 or 5, so all seven must be
covered by this owner. A strict shore chain contains at most one member
of a given rank. Their seven distinct right restrictions all have rank
5, so they require seven distinct rows. Every such row contains A on
its left shore.

Now consider the five targets

    (1220,A), (1220,B), (1211,A), (1121,A), (1112,A).  (2)

Their total nonzero support sizes are respectively 4, 5, 5, 5, and 5.
They too must be covered by this owner. They are five distinct points
at the same pair of shore ranks (5,2), so they require five distinct
rows.

Each left restriction in (2) has first coordinate 1 and a positive
coordinate outside the first position. It is therefore incomparable
with A = 2000: A has a larger first coordinate and a smaller positive
later coordinate. No strict left chain can contain A and any of these
left restrictions. Thus none of the five rows serving (2) can be one
of the seven rows serving (1). Every owner requires at least

    7 + 5 = 12 rows.                                  (3)

This row-count argument itself permits arbitrary strict subchains:
it uses incomparability and equal shore ranks, not saturation or the
presence of every intermediate shore rank. First-increment orders
enter through the exclusive binary-ownership assertion in Section 1.

## 3. Endpoint costs force total charge at least 2576

The seven targets

    (z,0000),  z in T union U,

have total nonzero support sizes 3 or 4 and force seven distinct owner
rows containing the right lower endpoint. Likewise the seven targets
(0000,z) force at least seven owner rows containing the left lower
endpoint. The targets (2222,0000) and (0000,2222), both of support
size 4, force the left and right upper endpoint to appear at least
once each.

Every shore in the endpoint-mode family retains all seven ranks
1,...,7. If the owner uses n rows and E is the number of retained shore
endpoint occurrences, its exact charge is 14n + E. The preceding
requirements give n >= 12 and E >= 7+7+1+1 = 16. Hence every owner has
charge at least

    14*12 + 16 = 184.                                 (4)

These are counts of endpoint occurrences, so a row containing several
required endpoints is charged correctly: each retained endpoint adds
one to its actual shore length. Endpoint coincidences in different
rectangles do not remove their charges.

Summing over the fourteen owners proves

    total charge >= 14*184 = 2576 > 2392.              (5)

The strict improvement gate is 76545/32 = 2392+1/32. Therefore this
entire original-owner endpoint-mode lift family cannot improve c9.
The bound does not claim sharpness within the restricted family. It
does not apply to arbitrary shorter nonsaturated subchains, because
such chains do not have the baseline charge fourteen. It also does
not apply to a bank that can assign forced targets to additional rows
with new first-increment orders or new shore partitions.

## 4. Original-owner short rows plus either fixed repair cannot cover

There is an even stronger obstruction for the proposed bank consisting
of short rows plus either of the four-row repairs in
`Q3_D8_FOUR_ROW_EXTREMAL_REPAIR_AND_SHORT_GATE_20260908.md`, if all its
short rows are restricted to the fourteen original first-increment
orders and their original shore partitions.

Each short shore retains only ranks 1,...,7 and therefore omits its
zero vector. For any owner and any z in T union U, the target (z,0000)
has global ternary rank 5 and support size 3 or 4. Its unique original
owner cannot cover it with a short row because the right shore is zero.
No other original owner can cover it, by exclusive ownership.

Each repair shore has ranks 0,1,2,6,7,8. No two of those ranks sum to
5. Thus neither fixed four-row repair contains any rank-five target.
The target (z,0000) is also absent from the repair. The resulting bank
fails coverage regardless of how many original-owner short rows it
uses, not just when it uses at most 167.

For a literal example, the first binary owner is (0461,5723). Put its
left restriction equal to 2210 and its right restriction equal to
0000. In global coordinate order 0,...,7 the target is

    (2,0,0,0,2,0,1,0).

It has rank 5 and nonzero support {0,4,6}, which has that unique binary
owner. It is missed by every bank in the restricted short-row-plus-
fixed-repair family. This argument allows either the fixed-partition
132-point repair or the affine 138-point repair because they have the
same allowed shore-rank set.

The unrestricted 167-short-row construction remains open: its rows
may use other orders and other balanced partitions, and this note
does not exclude those rows.
