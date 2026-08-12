# Exact \(m=4\) mixed-split forest closure and its cyclic repair kernel

Date: 2026-07-31  
Status: complete positive closure census for one authenticated fixed forest;
complete negative old-core-plus-ears verdict for its two closures

## 1. Authenticated input and the fixed forest

The input is

```text
scratch/even_two_rail_q3pattern_k8_20260730.PASS.json
SHA-256 9b9da8a7f821fc815eb77ed3aaa74431fb9aa387425d2c8166a80109ee4db5c3
JSON path carrier.cycle
```

Its 70 rank-four facets form a Hamilton cycle in \(J(8,4)\).  The rank-five
union loads are \(1^{42}2^{14}\), and the two occurrences of every doubled
upper colour are consecutive.  The complete \(2^{14}\) split-transversal
census has exactly one rank-three-rainbow choice.  In doubled-block order its
bits are

```text
1,0,1,0,1,0,1,0,1,0,1,0,1,0
```

where `1` retains the outgoing edge and `0` retains the incoming edge.
Deleting the opposite edge in every doubled block gives a spanning forest
\(F\subset J(8,4)\) with all 56 rank-three intersections and all 56 rank-five
unions exactly once.  It has fourteen paths, with length histogram
\(3^7 7^7\).  Thus there is no singleton or cyclic component.

## 2. Complete endpoint-closure census

All \(2^{14}=16384\) orientations of \(F\) were tested.  Path zero was fixed
only as the cyclic root, and every directed Hamilton closure satisfying the
equal-union condition (1.1) of
`MATH_AUDIT_M4_SPLIT_LEAVE_FOREST_AND_PAIR23_CLOSURE_20260731.md` was
enumerated without colour pruning.

Exactly one orientation works.  Its integer bit word is `10853`, with
reversed path indices

```text
0,2,5,6,9,11,13
```

under the raw-source canonical path ordering.  It has exactly two rooted
Hamilton closures:

```text
0,1,5,12,11,8,6,7,2,4,13,10,9,3,0
0,7,2,1,5,4,13,12,11,10,9,8,6,3,0
```

Both closures pass all three remaining gates: the fourteen incoming
`alpha` colours are distinct, the fourteen smoothed base colours are
distinct, and the smoothed bases are disjoint from the fourteen outgoing
`beta` colours.  Hence both are literal uniformly-outgoing directed repairs.
The canonical fixture is the first closure above.  Its seam cycle is

```text
142,15,23,86,102,228,180,177,184,60,92,90,27,147,
209,197,225,113,114,106,108,204,198,150,135,71,75,43,
51,178,154,216,156,30,46,45,77,201,232,226,240,120,
57,53,54,166,163,139,195,99,101,85,89,153,141,172
```

Its fourteen repairs, as
`(block,tail,head,omitted,base,alpha,beta)`, are

```text
(1,15,23,29,7,13,21)
(7,177,184,169,176,161,168)
(9,60,92,116,28,52,84)
(15,197,225,165,193,133,161)
(17,113,114,83,112,81,82)
(23,150,135,149,134,148,133)
(25,71,75,78,67,70,74)
(31,216,156,212,152,208,148)
(33,30,46,58,14,26,42)
(39,226,240,210,224,194,208)
(41,120,57,105,56,104,41)
(47,139,195,202,131,138,194)
(49,99,101,39,97,35,37)
(55,172,142,170,140,168,138)
```

Producer-independent replay reconstructs the seam blocks and insertions
from these arrays alone.  It verifies the base profile
\(0^{14}1^{28}2^{14}\), exact outgoing rank-three palette, fourteen distinct
alphas, all 56 rank-five blocks, and a 70-facet cap-two Hamilton cycle.

## 3. The repair core does not recurse as nine ears plus the old core

For the canonical closure the complete occurrence-labelled repair core has
21 edges.  Exhausting every possible degree-one choice visits 128 states;
all \(7!=5040\) maximal orders stop at depth seven.  Every peeling order
removes the same seven forced ears and reaches the same
leafless \(7\times7\times7\) kernel with 14 hyperedges.  In that kernel:

* the omitted--base projection is one simple 14-cycle;
* the base--beta projection is one simple 14-cycle;
* the omitted--beta projection is seven disjoint vertex pairs, each carried
  by two parallel hyperedges; and
* there are exactly two hypergraph perfect matchings, the two alternating
  choices around the cyclic kernel.

The producer-independent old-\(m=3\)-core test explores 449 states and finds
no forced-ear order leaving the authenticated five-by-five-by-five,
seven-edge \(m=3\) core.

The alternate closure is still farther from unitriangular: its complete core
has 28 edges and no degree-one vertex initially.  Its omitted--base and
base--beta projections are each two disjoint simple 14-cycles, its
omitted--beta projection is fourteen doubled pairs, and it has exactly four
hypergraph perfect matchings.  Its old-(m=3)-residual test fails at the
initial state.

Therefore this fixed forest proves \(m=4\) uniformly-outgoing existence but
does **not** realize the proposed recursive shape “old (m=3) core plus nine
forced ears.”  Its sharper structural residue is seven forced ears plus one
seven-token alternating cycle kernel.  This is a fixed-(F) statement only;
it neither excludes a different leaf-peelable (m=4) forest nor proves an
all-\(m\) construction.

## 4. Comparison with the varied-size flag-matching carrier

An independently frozen 56-flag inclusion matching lifts to another exact
two-sided-rainbow 14-path forest, now with component sizes

\[
21,7,7,6,5,5,4,3,2,2,2,2,2,2.
\]

Fourteen Johnson endpoint connectors make this forest Hamiltonian.  Because
the internal forest already contains every lower and upper colour once, the
connector repetitions preserve complete support; the final load profiles are
\(1^{43}2^{12}3\) below and \(1^{44}2^{10}3^2\) above.  This is a genuine
positive physical-lift fixture, but it does not satisfy the block-coherent
split-leave gate.

The complete equal-union port graph of that fixed forest has 34 directed
arcs, no bidirectional pair, and the port `0x95` is isolated.  Its maximum
matching size is 13, with zero perfect matchings.  Equivalently, all
\(2^{14}\) path orientations have zero degree-feasible endpoint state and
zero rooted equal-union Hamilton closure.  Only eight of the fourteen
published Johnson connectors are legal in either equal-union direction.

Thus the new carrier is useful as a counterexample and recursive diagnostic:
abstract flag matching plus a physical Hamilton connector cycle does not
imply a uniformly outgoing repair.  The missing invariant is already the
local equal-union/block-coherence condition, before alpha or base-colour
tests.  This fixed-forest no-go does not diminish its complete-coverage
certificate or exclude a different reclosure after changing forest edges.

## 5. Frozen artifacts and reproduction

```text
scratch/build_catalan_m4_mixed_split_fixed_forest_closure_20260731.py
  SHA-256 15689d2bcecd42803ea1fe92c7ed7e9386057001fa88a220f8f6820fab7d36e4

scratch/catalan_m4_mixed_split_fixed_forest_closure_20260731.PASS.json
  SHA-256 e8eb60cf8401296d73fa7d39739fb85d70e7f921ecd9661548e2a768cb44f899

scratch/catalan_m4_mixed_split_fixed_forest_closure_alt_20260731.PASS.json
  SHA-256 5cf286ca9f11583abaa270e5dd9460c69ede94a0ffc9c533aa84f2ec9ed55600

scratch/verify_catalan_directed_repair_m4_result_20260731.py
  SHA-256 c51710a3b95fd7d5682d529324781f068493612665bc9acf0cedbd8d72ac02cd

scratch/catalan_m4_mixed_split_fixed_forest_closure_20260731.audit.json
  SHA-256 6999f539e5223848d26bf5e487c75497aced09a2b82351e4e2ac32383ba0df4b
  canonical payload 500191a998017d35b0d60981805e6d75cd7c9f62f425963c8ca8d08a893188aa

scratch/catalan_m4_mixed_split_fixed_forest_closure_alt_20260731.audit.json
  SHA-256 5370c94922fc6df2ee1416227f9afc640d6d899b6e6ae0c94b5aa7516f6ad51c

scratch/audit_catalan_m4_mixed_split_closure_kernels_20260731.py
  SHA-256 4e878a3276eeff39cc9d9e3ae62ea3b54a210944846afac5d6ae3873bef0af4f

scratch/catalan_m4_mixed_split_closure_kernels_20260731.audit.json
  SHA-256 f5b76d28a9efc11e0f4d7100c50f21f0d583530fdc3b4221671e96f87a314f15
  canonical payload 5458d897f06eec2f37925541de875c0b5fd60b79e84dfb73b05f1b3bb46654ed

scratch/audit_catalan_m4_repair_core_cycle_structure_20260731.py
  SHA-256 f4f6ced6da40c1d15665eee7f519c19b2912b22faeadd7e00fb525a416345e32

scratch/catalan_m4_repair_core_cycle_structure_20260731.audit.json
  SHA-256 982ee40e39d2d1d2c33c7a3bba425e9c9107ded868208670a6058f25f39ca118
  canonical payload 3d7d6c79b5dea6e6b9255c176894f0bfea6730df8cfdcba38ec8d2fc5ef2273f

scratch/audit_catalan_m4_flag_connector_lift_independent_20260731.py
  SHA-256 7c825136a55e3f0cf12a3b996a9dea32980ff9ecd1262bfd04af1cc979c78a19

scratch/catalan_m4_flag_connector_lift_independent_20260731.audit.json
  SHA-256 a505dbe4e0d93eca2631b0949ddfe8d650bd71bbaedada2ea135f1d770781174
  canonical payload 3f2eeede08f432d06df74482d599ad3eb07bd65566130227269bbc8c966e1186

scratch/audit_catalan_m4_flagforest_split_leave_closure_20260731.py
  SHA-256 f6cd1c688fc6113aa04addf8e724852a59c01eb0aa9d48202e0eb1ce5d564592

scratch/catalan_m4_flagforest_split_leave_closure_20260731.audit.json
  SHA-256 750c98a950e294621a2d8c514782197b471bbe6a4ccb93de9bade7b992e9eb8e
  canonical payload 70379674183049c0d2f14761cf82f0bef1afd93a5ab90352fe36ad3a60d8a33d
```

Run

```text
python3 scratch/build_catalan_m4_mixed_split_fixed_forest_closure_20260731.py
python3 scratch/build_catalan_m4_mixed_split_fixed_forest_closure_20260731.py --closure-index 1
python3 scratch/verify_catalan_directed_repair_m4_result_20260731.py --input CANDIDATE --output AUDIT
python3 scratch/audit_catalan_m4_mixed_split_closure_kernels_20260731.py
python3 scratch/audit_catalan_m4_repair_core_cycle_structure_20260731.py \
  --input scratch/catalan_m4_mixed_split_fixed_forest_closure_20260731.PASS.json \
  --output CORE_AUDIT
python3 scratch/audit_catalan_m4_flag_connector_lift_independent_20260731.py \
  --output FLAG_AUDIT
python3 scratch/audit_catalan_m4_flagforest_split_leave_closure_20260731.py \
  --output FLAG_CLOSURE_AUDIT
```
