# Unequal thresholds in the fixed fourteen-row cover

Date: 2026-09-07. No improved full-cube coefficient was obtained.
All computations below ran explicitly through `ssh h100`.

The test retains the fourteen ordered `4+4` binary prefix rows in master
A.7.1, but chooses a possibly different threshold `c_i in {1,...,q-1}`
on each coordinate of `[q]^8`, where `[q]={0,...,q-1}`. For an ordered
shore `(i_1,...,i_4)`, its actual staircase consists of points whose four
bits `1[x_(i_j)>=c_(i_j)]` are nonincreasing. The binary-cover certificate
therefore guarantees that the fourteen products of these staircases cover
the entire grid, for every threshold vector.

For each shore, form the directed graph of allowed unit coordinate increases.
An integral matching between two copies of this vertex set partitions it
into ascending paths: each matched edge is a successor link, and coordinate
rank forbids directed cycles. Its path count is `V-|matching|`, where `V`
is the staircase's number of points. The code also constructs a vertex
cover of the bipartite graph of size `|matching|`, checks every edge against
that cover, and checks the literal path partition. Equality with this cover
certifies that the path count is minimum among **unit-step path partitions**.
No rank-polynomial or fractional-cover inference is used.

Pairing all left and right paths in one row gives principal charge

\[
                         V_L w_R+V_R w_L,
\]

where `w` is the certified path count. Summing this over the fourteen rows
gives a literal integral chain-pair cover. The existing q-ary amplification
theorem converts charge `M` to asymptotic coefficient `(M/q^7) beta_9`.
Beating the current construction by this method would require
`M/q^7<35/32`.

The complete threshold-vector enumerations gave:

| Grid alphabet q | Shore types | Threshold vectors | Minimum M | Unique minimizer |
|---:|---:|---:|---:|---|
| 4 | 81 | 6,561 | 17,920 | every threshold is 2 |
| 6 | 625 | 390,625 | 306,180 | every threshold is 3 |

Both normalized minima are exactly `35/32`. Independent literal membership
enumeration of the selected path products checked all 65,536 and 1,679,616
grid points, respectively. The executable is
`binary8_unequal_thresholds_20260907.py`. Certified logs and full chosen path
data are in `/home/amodo/or-research-20260907-QiqXT3/` on h100, under
`binary8_threshold_q4_certified.*` and `binary8_threshold_q6_certified.*`.

Scope is deliberately narrow: these are finite negative results for the
fixed fourteen-row template, two specified grids, and independent products
of unit-step shore-path partitions. Arbitrary strict chain partitions can
use jumps and are not excluded. Neither other alphabets, other row banks,
coordinated cross-row decompositions, nor unrestricted OR words are ruled
out. This test supplies no lower bound on `nu` and no new asymptotic theorem.
