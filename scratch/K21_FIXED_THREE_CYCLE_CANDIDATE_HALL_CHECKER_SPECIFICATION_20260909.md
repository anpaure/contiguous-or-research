# Fixed three-cycle candidate graph: proof-purpose specification

Date: 2026-09-09. This is the specification prepared before source review
and execution. The subsequently completed one-run result is recorded in
[the independent numerical certificate](K21_FIXED_THREE_CYCLE_PHYSICAL_CANDIDATE_HALL_DEFICIENCY_462_VERIFIED_20260909.md).

The question is whether the supplied21 literal certifies the claimed
weighted candidate graph with 1,997,177 edges, maximum flow 695,397 and
Hall deficiency 462. Those three numbers are comparison fields, never
input assertions or premises of the checker.

## Fixed input and phase

The only input is the already full-cube-verified literal of length353,297,
raw SHA256
`0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7`.
The source extracts exactly three periods of lengths352,548,105,63,
each followed by a verified copy of its first three letters. It verifies
that exactly572 remaining letters form the repair suffix. The suffix and
cross-component seams are NOT vertices of this candidate graph.

For each cyclic component C, use

    R_i=OR(C_i,C_(i+1),C_(i+2)),
    U_i=OR(C_i,...,C_(i+3)),
    E_i=AND(U_(i-3),...,U_i).

The checker verifies the complete distinct rank10 and rank11 decks,
U_i=Phi(R_i), consecutive owner union/intersection identities, C_i subset
E_i, and exact triple/four-window identities for E. It separately checks
rotation equivariance of successor, U, and E. No assumption of rotation
equivariance of the actual capped letters is needed.

## Exact individual candidate menus

For a cell I consisting of one or two consecutive positions, put

    V_I=OR_(i in I) E_i,
    K_I=OR_j [R_j minus OR_(i in {j,j+1,j+2} minus I)E_i].

Only starts j=-2,...,|I|-1 relative to the cell start can contribute.
The computation uses these exact deficits, rather than assuming a
simplified pin formula. A nonempty target S of rank at most9 is in the
menu exactly when

    K_I subset S subset V_I,
    E_i intersect S is nonempty for each i in I.

Necessity: a preserved triple cannot obtain a missing coordinate outside
I, and no cap can supply a coordinate outside V_I. Nonempty resulting
letters must each meet S. Sufficiency: cap E_i to E_i intersect S inside
I and leave every other letter full. Each target coordinate keeps all
its available appearances; any omitted coordinate has an outside witness
in every affected triple by the deficit condition. Every accepted menu
item is also directly replayed against every affected triple by the code.

This is the general deficit argument already recorded in
[the exact short-target cap theorem](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md).
Any rank-at-most9 interval in a globally triple-preserving cap of these
cycles has length one or two: a longer interval contains a frozen rank10
triple. Thus these are ALL individual candidate hosts for that fixed bank.
Menus do not assert simultaneous compatibility of overlapping caps.

## Orbit graph and why its Hall cut has physical meaning

Every rank10 state has a full21 rotation orbit; the checker verifies this
and the equivariance identities literally. One representative R_i therefore
indexes one single-cell orbit and one ordered pair-cell orbit, each of
size21. Equal maximal letters at different positions are still distinct
physical cells.

All nonempty targets of ranks1 through9 are partitioned into their exact
rotation orbits, whose actual sizes are21,7,3. Each target orbit has demand
equal to its size. A target orbit is adjacent to a cell orbit exactly when
some member occurs in the representative cell's exhaustive menu. Rotation
equivariance ensures that this includes EVERY physical incidence, and
that an orbit in the neighborhood of a rotation-invariant target family
contributes all21 physical cells.

The graph is

    source -> target orbit (capacity its actual size),
    target orbit -> candidate cell orbit (capacity total demand+1),
    cell orbit -> sink (capacity21).

The source runs Dinic once on this fixed graph. Its optimum equals the
maximum matching size of the expanded PHYSICAL candidate graph. Indeed,
an orbit-pair incidence is biregular under rotation. An orbit flow amount
f can be distributed uniformly over all its physical incidence edges;
each target in that orbit receives f/|target orbit| and each cell receives
f/21. This gives a feasible fractional physical matching of the same
value. Bipartite matching integrality supplies an integral matching of
at least that value. Conversely every physical matching aggregates to
a feasible orbit flow, proving equality.

A feasible candidate matching is still only a relaxation of simultaneous
cap assignment: distinct cells may overlap. However a deficient Hall
family gives an unconditional obstruction within this fixed cyclic bank:
each physical single/pair cell realizes only one target in any actual cap.
A family of targets larger than its COMPLETE physical cell neighborhood
cannot be covered. This statement requires no symmetry of the chosen caps.

The result is not a lower bound for unrestricted OR words or for other
middle carriers, and it ignores the supplied repair suffix and linear
seam opportunities.

## Independent certificate replay inside the one run

The program saves the full orbit mappings and complete deduplicated graph,
every positive flow edge, and the residual-cut target/cell sets. A separate
replay phase rereads the graph, flow, and cut files. It checks:

1. Every positive flow edge belongs to the saved complete graph; there
   are no duplicate records, negative values, or out-of-range endpoints.
2. Reconstructed source/target and cell/sink flows obey all capacities;
   their sums agree, so this is a feasible flow of the asserted value.
3. For EVERY cell orbit, the entire local menu is regenerated from the
   native triple deficits. Its incidence with the Hall target family
   equals the saved graph and the claimed neighbor set.
4. The identity

       total demand - feasible flow
          = Hall target weight - 21*(full neighbor count)

   holds exactly and is nonnegative. A feasible flow and this matching
   Hall upper bound certify the maximum value independently of Dinic's
   residual-capacity or conservation implementation.

The complete physical Hall target list and all physical neighbor cells
are also exported. No deficiency is certified from a sampled neighborhood.

## Prepared sources, limits and execution boundary

* [C++ graph and certificate checker](certify_k21_fixed_three_cycle_candidate_hall_20260909.cpp).
* [SHA/resource/provenance runner](run_k21_fixed_three_cycle_candidate_hall_20260909.py).

The original plan required complete root review before execution and one
h100 C++17 optimized build with its command and binary hash recorded.
The specified runtime was one h100/arboghast job, with CPU120 seconds total
(driver5 plus mathematical child115), wall150 seconds, address space2GiB,
and individual file size512MiB. The wrapper executes a copied, hashed
binary on an immutable SHA-checked input snapshot and a fresh output
directory. It kills a timed-out child and does not restart it.

Only a completed independent replay earns PASS. Resource exhaustion or
an interface mismatch remains inconclusive/error, without another seed,
different graph, cut change, or automatic retry.
