# The varied-size \(m=4\) flag forest: exact rainbow reclosure and cap-two obstruction

Date: 2026-07-31  
Status: finite solver-free theorem for one authenticated \(m=4\) forest

## Theorem

Let \(\sigma\) be the literal rank-three/rank-five inclusion matching frozen
in
`scratch/audit_catalan_m4_flag_connector_lift_independent_20260731.py`,
and let \(F=\psi(\sigma)\) be its unique physical Johnson lift.

Then:

1. \(F\) is a spanning fourteen-path forest in \(J(8,4)\), with component
   orders

   \[
   21,7,7,6,5,5,4,3,2,2,2,2,2,2.
   \]

2. The supplied fourteen connectors close \(F\) into a Hamilton cycle.
   The forest edges already use every rank-three intersection and every
   rank-five union exactly once, so the cycle has complete immediate lower
   and upper coverage even though the supplied connector colours repeat.

3. Among all Johnson perfect matchings of the 28 path endpoints, exactly
   39,330 exist, and exactly 16,080 contract to one cycle on the fourteen
   path components. Of these connected closures:

   | connector condition | closures |
   |---|---:|
   | lower rainbow | 7,776 |
   | upper rainbow | 7,318 |
   | both shores rainbow | 3,865 |

   Thus this same fixed forest has Hamilton closures whose complete lower
   and upper load profiles are both \(1^{42}2^{14}\).

4. No endpoint closure of this fixed forest is upper cap-two coherent, and
   hence none is uniformly outgoing. The obstruction is local: endpoint
   `0x95` has exactly four legal endpoint neighbours,

       0x87, 0x8d, 0x93, 0xb1,

   but for each of the four connector edges the unique forest edge having
   the same upper colour shares no physical rank-four endpoint with it.
   Every endpoint perfect matching must use one edge incident with `0x95`,
   so the cap-two gate fails before any global cycle condition.

Consequently a perfect inclusion matching whose lift is a spanning path
forest can admit many two-shore-rainbow Hamilton closures while admitting no
cap-two closure. This is an explicit physical counterexample to the
implication

\[
\text{common-transversal path forest + rainbow endpoint cycle}
\Longrightarrow
\text{uniformly outgoing repair}.
\]

It is not a counterexample to existence of a different uniformly outgoing
\(m=4\) forest: the separate item-2139 \(3^7 7^7\) fixture is positive.

## Proof

The independent literal replay enumerates all 56 flags, checks every
rank-three and rank-five colour exactly once, enumerates the unique Johnson
edge between each flag, and reconstructs the fourteen paths. It also checks
the supplied endpoint matching and Hamilton cycle directly.

The exhaustive reclosure audit builds all 74 Johnson edges between endpoints
of different components. Two independent exact enumerators are used:

* a smallest-domain DFS over endpoint perfect matchings, with 130,834 search
  nodes; and
* a component-traversal DFS, with 745,478 search nodes.

They agree on every total and on the full quotient-cycle partition
histogram. Each connected matching is classified by injectivity of its
intersection and union colours. A literal Hamilton cycle is reconstructed
for the simultaneous-rainbow class and replays the two
\(1^{42}2^{14}\) profiles.

For the negative assertion, the audit lists all four endpoint edges incident
with `0x95`, finds the unique same-upper edge of \(F\), and checks endpoint
disjointness in every row. This is a one-vertex obstruction, so it proves
zero cap-two closures without relying on the exhaustive count.

The abstract implications used here are proved in
`MATH_THEOREM_CATALAN_PATH_FOREST_CONNECTOR_AND_SMOOTHING_LEDGER_20260731.md`:
an endpoint component cycle closes a path forest to a Hamilton cycle;
connector repetitions do not affect coverage; two-shore injectivity gives
the two floor profiles; and cap-two additionally requires literal adjacency
to the unique same-upper forest edge.

## Reproduction and hashes

    baseline independent note
      MATH_AUDIT_CATALAN_M4_FLAG_CONNECTOR_PHYSICAL_LIFT_INDEPENDENT_20260731.md
    baseline replay
      scratch/audit_catalan_m4_flag_connector_lift_independent_20260731.py
      SHA 7c825136a55e3f0cf12a3b996a9dea32980ff9ecd1262bfd04af1cc979c78a19
    baseline JSON
      scratch/catalan_m4_flag_connector_lift_independent_20260731.audit.json
      SHA a505dbe4e0d93eca2631b0949ddfe8d650bd71bbaedada2ea135f1d770781174
      payload 3f2eeede08f432d06df74482d599ad3eb07bd65566130227269bbc8c966e1186

    exhaustive reclosure replay
      scratch/audit_catalan_m4_fixedforest_connector_census_20260731.py
      SHA 6ae9b5f1e7856b6ff9a1ed755d18883b5c0627406dd2f2306f9d1aa2efd23f45
    reclosure JSON
      scratch/catalan_m4_fixedforest_connector_census_20260731.audit.json
      SHA e2c40dee905397d7bfe526f0f886f15b9992c9d0105ad09390a120d3ce7adcba
      payload 437bd9f7deb71c42a91108be488cb6f60687a9903ef0cfa0dc6123839b1fea75

## Scope

This is complete only for the frozen varied-size \(m=4\) forest. It proves
neither an all-\(m\) construction nor a no-go for other \(m=4\) forests.
