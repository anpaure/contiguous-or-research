# Finite asymmetric staircases attain their largest rank layers

2026-09-08. Cover-selectors finite verifier. All numerical work ran via
ssh h100. For all32 mandatory cases s=2,3,4,5, p=1,2,3,4, and u=s±1,
the allowed five-dimensional poset has an actual saturated-chain
partition whose size equals its largest rank layer. No general Sperner
theorem is inferred.

The weighted sums with position multiplicities(4,1,7,2) all EXCEED
28s^4. Therefore none of these tested finite certificates supplies
the requested strict terminal gain, even when the accepted grid-chain
inflation theorem is applied.

## 1. Exact finite object and method

All five coordinates range over{0,...,2s-1}. On the first four ordered
axes, the thresholds are s except at position p, where the threshold
is u=s+delta, delta in{-1,1}. A tuple is allowed when its four bits

    b_i=1{x_i>=threshold_i}

are nonincreasing. The fifth coordinate is unrestricted.
The number of allowed vertices is

    N=10s^5+2(2p-5)delta s^4.                       (1)

Indeed the five threshold boxes have one high prefix and one low
suffix; summing their volumes gives(1). The verifier enumerates the
tuples directly instead of using(1) as its coverage test.

The bipartite graph has one left and one right copy of each tuple.
An edge x_L--y_R is present exactly when y=x+e_i for one coordinate
and both tuples are allowed. Such an edge is an actual ambient unit
step and hence a saturated comparability in the induced poset.

A maximum matching M is computed on this graph. Its edges give a
directed graph with in-degree and out-degree at most one. Rank strictly
increases along every edge, so its components are paths. They form an
actual saturated-chain partition with N-|M| chains. Every matched
edge and every target uniqueness condition was checked explicitly.

Separately, the complete rank census counts tuples by sum_i x_i.
Each layer is an antichain. Thus equality of N-|M| with the largest
layer certifies both an optimal saturated partition and the finite
Sperner property for that particular case. A positive gap would have
been reported only as a saturated-partition gap; it would not by itself
have proved a width obstruction.

## 2. All individual counts

The following are the saturated-chain counts for u=s-1. Every entry
equals the largest rank-layer cardinality. The parenthesized values
are the ranks where that maximum is attained.

| s | p=1 | p=2 | p=3 | p=4 |
|---:|---:|---:|---:|---:|
|2|48(8)|46(9)|39(10)|27(10)|
|3|215(13,14)|207(15)|182(16)|139(16)|
|4|638(19)|615(20,21)|553(22)|449(22)|
|5|1495(24)|1450(26)|1320(27,28)|1115(28)|

For u=s+1, the four counts are the reverse of each displayed row.
The maximizing ranks are obtained by sending a listed rank j to
5(2s-1)-j at the reversed position. This was checked in every case;
it also follows from complementing all coordinate values and reversing
the order of the first four axes. The full32 rank censuses are in
ASYMMETRIC_STAIRCASE_SATURATED_CHAIN_COUNTS_20260908.json.

## 3. Exact weighted terminal comparison

Write W_p for the actual chain count at position p and put

    W=4W_1+W_2+7W_3+2W_4.

The position-weighted membership is unchanged because
sum_p w_p(2p-5)=0; it equals140s^5 for either sign. The relevant
chain-count baseline is28s^4. The exact comparison is:

| s | W for u=s-1 | W for u=s+1 | 28s^4 | Excess for minus / plus |
|---:|---:|---:|---:|---:|
|2|565|565|448|117 /117|
|3|2619|2617|2268|351 /349|
|4|7936|7930|7168|768 /762|
|5|18900|18920|17500|1400 /1420|

These are exact integer counts, not numerical approximations. In
particular there is no negative weighted gain among the tested cases.
The largest-rank-layer lower bounds already force these same weighted
counts, so a different chain partition of the SAME finite posets cannot
improve any entry in this table.

This last statement concerns these fixed finite macro posets. It does
not rule out other thresholds, other weighted positions, another finite
macro object, or a construction that changes the repair architecture.

## 4. Largest completed case: actual paths and independent replay

The largest mandatory case is s=5,p=1,u=4. It has:

    35000 allowed vertices;
    150000 unit-step edges;
    matching size33505;
    1495 saturated chains;
    largest rank layer1495, at rank24.

All1495 paths were reconstructed and saved, covering all35000 tuples.
The independent replay uses only those paths and the four thresholds,
not the sparse graph or matching routine. It decodes every vertex,
checks the monotone threshold bits, checks every step is exactly one
positive coordinate increment, rejects every repeated vertex, and
independently enumerates all allowed five-tuples to check complete
coverage. It also recounts the ranks. All checks PASS.

An alternating-reachability construction additionally produced a
bipartite vertex cover of size33505 and checked every graph edge meets
it. This equals the matching size, independently certifying optimality.
The rank-layer lower bound already certifies the optimal path count.

The durable path certificate is
ASYMMETRIC_STAIRCASE_LARGEST_CHAIN_PARTITION_20260908.json. A vertex
is encoded in base2s with the first coordinate most significant; the
file records the thresholds, exact case, and explicit list of paths.

## 5. Scope, runtime, and files

The mandatory32-case progress report was saved after2.7165 seconds.
The bounded initial run ended during the optional s=6 stage before
that stage completed or its paths were exported. NO s=6 result is
claimed. A separate recovery limited to2 seconds recomputed only the
largest completed mandatory case, formed the weighted table, and
completed the independent path/tuple and matching-cover replay in
0.3624 seconds. The initial internal limit was18 seconds; both stages
were pinned to at most two CPUs and capped at3GiB.

Local durable files, all in this scratch directory:

- verify_asymmetric_staircase_saturated_chains_20260908.py
- ASYMMETRIC_STAIRCASE_SATURATED_CHAIN_COUNTS_20260908.json
- ASYMMETRIC_STAIRCASE_LARGEST_CHAIN_PARTITION_20260908.json

The remote directory is
/tmp/asymmetric_staircase_matching_20260908_cover_selectors/.
The recovery command was

    ssh h100 'timeout 2s python3 /tmp/asymmetric_staircase_matching_20260908_cover_selectors/verify_asymmetric_staircase_saturated_chains_20260908.py /tmp/asymmetric_staircase_matching_20260908_cover_selectors --recover'

The accepted grid-chain inflation lemma would turn a strict finite
weighted decrease into an asymptotic construction. It does not turn
the positive excesses above into a gain. This experiment supplies
actual finite chain certificates and a precise negative comparison
for the requested perturbations, without a general nonexistence claim.

## 6. Position census for every coordinate of the literal template

A separate tiny inventory on h100 read the unchanged fourteen rows in
MASTER_HANDOFF.md, Appendix A.7.1. For each coordinate, n_p counts the
rows where that coordinate appears in position p of its own ordered
four-coordinate shore. The result is:

| Coordinate | (n_1,n_2,n_3,n_4) | n_4-n_1 | Central gradient -(2/3)(n_4-n_1) |
|---:|:---:|---:|---:|
|0|(4,1,7,2)|-2|4/3|
|1|(3,5,2,4)|1|-2/3|
|2|(3,4,4,3)|0|0|
|3|(4,3,3,4)|0|0|
|4|(3,6,0,5)|2|-4/3|
|5|(4,2,5,3)|-1|2/3|
|6|(3,4,4,3)|0|0|
|7|(4,3,3,4)|0|0|

Every coordinate satisfies the exact critical-rank constraints
sum_p n_p=14 and sum_p p*n_p=35; the program checks both independently
for each of the eight rows of this census. The gradient column applies
the formula from ASYMMETRIC_SHORT_AXIS_RANK_FIRST_VARIATION_20260908.md;
it is not an estimate of the largest-rank-layer count.

The maximum absolute imbalance is 2, attained by coordinates 0 and 4
with opposite signs. Thus coordinate 0 already maximizes this particular
first-variation magnitude within the literal template. No coordinate
attains the general upper bound 3. This census alone makes no claim
about optimal finite thresholds or chain counts for other coordinates.

The durable source and complete row-by-row census are
inventory_eight_bit_template_positions_20260908.py and
EIGHT_BIT_TEMPLATE_POSITION_COUNTS_20260908.json. The source asserts
that it runs on the authorized h100 host, arboghast. The exact command
was:

    ssh h100 'timeout 5s python3 - /tmp/asymmetric_template_positions_20260908_cover_selectors.json' < scratch/inventory_eight_bit_template_positions_20260908.py > scratch/EIGHT_BIT_TEMPLATE_POSITION_COUNTS_20260908.json

No matching or search was added for this census.
