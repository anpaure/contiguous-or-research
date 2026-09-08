# Exact cyclic width in nine coordinates: mu(9)=126

2026-09-07. Self-contained finite certificate. No external word file,
solver output, or unproved construction hypothesis is needed below.

Let mu(k) be the minimum number of nonempty set-valued letters in a cyclic
word whose interval unions, with lengths from one through one period,
include every nonempty subset of a k-element ground set.

## Construction

Represent subsets of {0,...,8} by their nine-bit masks and let

    rho(x) = ((x << 1) & 511) | (x >> 8).

Take the fourteen-letter seed

    S = (1,18,130,258,264,72,96,36,33,48,24,272,144,192).

For 0<=i<14 and 0<=t<9, define

    A_(14t+i) = rho^(5t)(S_i).                         (1)

This is a nonzero cyclic word of length126. Because gcd(5,9)=1, shifting
a witness by fourteen positions generates every coordinate rotation of
its target. All indices below are zero-based and cyclic modulo126.

## Complete orbit certificate

For a mask T put c(T)=min_{0<=j<9}rho^j(T). In each table row, the listed
witness pairs (start,length) correspond in order to the representatives.
Taking the OR of the indicated letters in (1) gives a mask with that
canonical representative. Every witness starts within the first seed.

| Rank | Canonical representatives | Corresponding (start,length) |
|---|---|---|
| 1 | 1 | (0,1) |
| 2 | 3,5,9,17 | (6,1),(3,1),(1,1),(4,1) |
| 3 | 7,11,13,19,21,25,35,37,41,73 | (9,2),(2,2),(5,2),(0,2),(3,2),(6,2),(8,2),(7,2),(4,2),(1,2) |
| 4 | 15,23,27,29,39,43,45,51,53,57,75,77,83,85 | (12,3),(13,3),(5,3),(11,3),(9,3),(2,3),(4,3),(10,3),(7,3),(8,3),(1,3),(0,3),(6,3),(3,3) |
| 5 | 31,47,55,59,61,79,87,91,93,103,107,109,117,171 | (11,4),(12,4),(9,4),(10,4),(7,4),(0,4),(2,4),(4,4),(13,4),(8,4),(1,4),(5,4),(6,4),(3,4) |
| 6 | 63,95,111,119,123,125,175,183,187,219 | (9,5),(12,5),(0,5),(8,5),(7,5),(5,5),(2,5),(3,5),(1,5),(4,5) |
| 7 | 127,191,223,239 | (8,6),(1,6),(0,6),(2,6) |
| 8 | 255 | (0,7) |
| 9 | 511 | (0,8) |

These finite OR and rotation identities can be checked directly from (1).
For example, start1 and length2 give18|130=146, whose orbit representative
is73; start4 and length5 give264|72|96|36|33=365, with representative219.
These are precisely the two nontrivial periodic orbits needed here.

The representatives in the table are distinct canonical masks. All their
rotation orbits have size9 except73 and219, whose sizes are3, and511,
whose size is1. The numbers of different supplied targets by rank are
therefore

    9,36,84,126,126,84,36,9,1,

respectively. These equal binom(9,s) for s=1,...,9. Thus the table supplies
every nonempty target, not just one named family per rank. This proves
mu(9)<=126.

## Optimality

At a fixed cyclic start, interval unions are nested as their length grows.
They therefore contain at most one DISTINCT target of a fixed cardinality.
A universal cyclic word must realize all binom(9,4)=126 rank-four targets,
so it needs at least126 starts. Consequently

    mu(9)=126=W(9).                                    (2)

## Constructive origin: one safe orbit erasure

The parent seed is obtained by changing the initial1 in S to3. At that
position of the developed parent cycle, the neighboring masks are6 and18.
The removed mask2 is contained in both neighbors, since6&3&18=2.
Perform this erasure at every fourteenth position. Those positions are
pairwise nonadjacent. Every interval of length at least two containing an
erased bit also contains an unmodified neighbor which retains that bit;
hence all such interval unions are unchanged.

The only potentially lost one-letter pair belongs to the rotation orbit
of3. That orbit still occurs at unmodified positions: rho^5(48)=3, and48
is an unmodified seed letter. The nine new singleton letters supply all
nine coordinates. The table above directly certifies the final word, so
its proof does not depend on trusting the parent search or this explanation.

## Verification provenance and scope

The tree/history search ran ONLY on H100 and found this candidate after
6,215,169 DFS nodes. A separate literal verifier checked all511 targets,
both middle decks, the maximal pair envelope and the developed pin.
A third, root-owned H100 check used a different latest-start suffix-union
recurrence, then replayed a witness for every target. It independently
returned all511 targets and the59 orbit witnesses displayed above.

The SHA256 of the original one-line candidate bytes (including its newline) is
`b7914d1d4abf3ea25602a5eb5a13b23aee9ae955298eddb71e91ec454c9214ab`.
The readable nine-line copy in `answers/cyclic_k09_width126.word` has the
same mask sequence but different formatting; this is not its byte hash.
The hash is provenance only; the seed, table and lower-bound proof make
this file self-contained without its preimage or any verification script.

This is an exact CYCLIC result. It does not improve the already known
linear value nu(9)=128, establish a general odd-dimensional construction,
prove nu(k)=B(k), or change the full-cube asymptotic coefficient.
