# R2 k17 joined geometry--colour pairs: fail-closed replay contract

Date: 2026-08-02  
Status: verifier contract and compiled literal replay are frozen; no joined
pair is accepted by this note until its promoted artifacts pass the contract.
No pair enumeration or SAT search is performed here.

## 1. Input normalization and exact two-recut binding

The upstream D/A projection may contain several raw seam witnesses for one
unordered bank.  Before replay it must be normalized to one row per bank with
one of the exact headers

```text
pair_id geometry_base geometry_old_cut geometry_new_cut supplier_base supplier_old_cut supplier_new_cut activation_lower
pair_id geometry_base geometry_old_cut geometry_new_cut supplier_base supplier_old_cut supplier_new_cut activation_lower expected_local_clean
```

(The serialized file is tab separated.)  The normalization file and the
upstream catalogue from which it was derived are both hash-retained.  The
literal verifier rejects duplicate ids, duplicate unordered banks, a shared
base, an identity recut, a cut which is not an option of the named base, or an
old cut which is not the cut selected by the frozen round02 bank.

For a row `(g,s,q)`, the verifier constructs, rather than reads, the four
assignments

```text
D0,  Dg = D0-gold+gnew,  Ds = D0-sold+snew,
Dgs = D0-{gold,sold}+{gnew,snew}.
```

This makes it impossible for an upstream bank file to hide a third change.
Any bank later passed to the q1 builder must independently parse to `Dgs`
exactly and have its SHA-256 bound in the q1 manifest.

The current promoted normalization is

```text
source:
  scratch/r2_k17_round02_geometry_visible_supplier_join_20260802.tsv
  SHA-256 2d2f8d8d89decf178af5b2337cf2959110538c330330096fbe582dd26dbc6a76
normalized:
  scratch/r2_k17_round02_geometry_visible_supplier_join_promoted53.normalized.tsv
  SHA-256 8c2cdd3c7de0f1010c03d1708022d8ffb95395040baefec4ecbdd2e868aaadc1
all-row normalization:
  scratch/r2_k17_round02_geometry_visible_supplier_join_all70.normalized.tsv
  SHA-256 152efb45df6169e63b31468c1744d4f7541792dec69790958991d2bb5be7572f
```

An exact header-aware projection of the source rows whose `disposition` is
`PROMOTE_LOCAL_CLEAN` is byte-identical to the normalized file.  It has 53
rows, 53 distinct `join_id` values (retained as `pair_id`), and 53 distinct
role-ordered mover/supplier banks.  No rejected source row is present and no
source comment or hash is embedded in the data TSV.

The nine-column file is byte-identical to the corresponding projection of
all 70 frozen source rows.  It has 70 distinct ids and role-ordered banks,
with the exact expected partition `53 clean + 17 dirty`.  In this mode the
verifier rebuilds `Dgs` and its `Score` for every row, requires

```text
(Score.bad()==0) == expected_local_clean,
```

and emits `zero_lower`, `zero_out`, `zero_in`,
`zero_common_orientation`, and `zero_rank10` even for rejected rows.  The
palette-multiplicity, raw-geometry, surviving activation and final fan-rank
stages run only on the 53 rows which are both expected and replayed clean.
The original eight-column 53-row q1-promotion manifest is unchanged.

## 2. Palette activation is tested after both cuts

Let `q=activation_lower`.  The geometry--supplier interpretation is accepted
only if all four literal multiplicity statements hold:

```text
mult_D0(q)=0, mult_Dg(q)=0, mult_Ds(q)=1, mult_Dgs(q)=1,
```

and the new cut of `s` has lower mask exactly `q`.  Moreover all 7,612 cut
colours of `Dgs` must be simple.  A boolean selected-colour bit alone is not
enough, because it would conceal duplicate cuts.

The geometry child is rebuilt physically and must expose a *new* raw resident
noncore seam of colour `q` at one of the invariant owner sockets

```text
S=115442,  T=115186.
```

“New” is tested against the frozen baseline atlas by the stable tuple

```text
(socket, direction, other_base, other_side, other_orientation,
 other_owner, lower, upper),
```

not by a mutable physical-piece number.  Finally `Dgs` is rebuilt from
scratch and must contain a selected seam of colour `q`, either the same
occurrence or a literal replacement occurrence.  Thus an intact unary
counterpart which disappears when its base is also recut is not credited
unless a replacement state actually survives in the joint atlas.

## 3. Five zero-265 rows and exact breaker rank

On `Dgs`, the complete literal relaxed atlas is rebuilt.  Acceptance requires

```text
zero_lower = zero_out = zero_in = zero_common_orientation = zero_rank10 = 0.
```

The last row is only raw rank-ten provider availability; it is not selected
rank-ten coverage.

The old obstruction is the two-socket, one-colour fan at colour `114930`.
For an arm `a`, retain its lower colour, central socket, outside physical
piece, outside endpoint occurrence, direction, and demanded path
orientation.  Two arms on opposite central sockets are resource compatible
exactly when

1. their lower colours differ; and
2. their outside pieces differ, or, if the outside piece is shared, one arm
   uses it as a head and the other as a tail under the same path orientation
   and at different endpoint occurrences.

Condition 2 simultaneously enforces the one-in/one-out capacity and the
common-orientation variable.  Merely checking two different endpoint masks
would not be sufficient.  A resident direct `S--T` seam also has rank two.

The joined geometry--supplier row is accepted when the recomputed final-bank
rank is two.  The separately required surviving `q` arm authenticates the
advertised activation, but it need not be causal for the final breaker: a
different arm pair or a direct `S--T` seam may supply rank two.  The output
field `witness_uses_activation` records whether the preferred displayed
rank-two witness uses `q`; it is provenance, not an acceptance condition.
This is an occurrence-level certificate breaker, not a global q1 theorem.

The executable source is

```text
scratch/verify_r2_k17_round02_joined_pair_literal_20260802.cpp
SHA-256 6aa9ef066f28022f4beb5f7fa416de3332915f884dd5fef487b6c9d5ceab0e4e
```

It compiles cleanly apart from inherited unused-function warnings.  Its
library dependencies at freeze time are

```text
scratch/audit_threadD_k17_round02_dualfan_socket_escape_20260801.cpp
  eb6458f1e3a205d1fee5495db5cc59950d8293156fc2944581b39fa32c27d7e7
scratch/search_r2_k17_literal_cut_rank10_singletons_20260801.cpp
  0dc111142836215496a2f920606c7e0c0b99099f4b14805c39eb9c28ef50de9e
```

## 4. Exact q1 promotion branch

Passing the literal replay is necessary, not sufficient.  A promoted bank
then has exactly one of the following two certificate states.

### SAT

Retain the bank, CNF, orientation map, seam map, and complete solver model.
The independent model verifier must

1. hash-bind the bank and CNF;
2. check every CNF clause against the complete model;
3. rebuild the literal atom atlas and prove a bijection with the seam map;
4. check exactly one common orientation, outgoing seam, incoming seam and
   selected lower colour per physical piece/colour;
5. decompose the selected successor permutation; and
6. report selected rank-ten holes (and require zero only when the promoted
   claim includes selected rank ten).

The reusable checker is

```text
scratch/verify_r2_k17_relaxed_q1_functional_hall_model_20260801.cpp
SHA-256 ff9ca5af2cf96a0b8afe5ab890b4ba6cbf38ff4c2c9f0a255734d8ab18009ee0
```

Its map convention matches the CNF exporter in
`audit_k17_selected_extra_cut_literal_refinement_20260801.cpp` (SHA-256
`4e4440d8...`): two positive orientation variables per piece followed by seam
variables.  It must **not** be applied without adaptation to
`build_r2_k17_zero_bank_functional_rank10_cnf_20260801.cpp` (SHA-256
`21fb3195...`), which uses seam variables first and one signed orientation
variable per piece.

### UNSAT

Retain a nonempty proof and a manifest binding

```text
pair_id, bank_sha256, builder_sha256, formula_mode,
cnf_sha256, proof_sha256, checker_sha256.
```

An independent invocation of the retained checker on that exact CNF/proof
pair must end in `s VERIFIED`.  Solver stdout alone has state
`SOLVER_UNSAT`, not `VERIFIED_UNSAT`.  Topology and selected rank ten are
`N/A_Q1_UNSAT` on this branch.

Formula mode is load-bearing.  `RELAXED_Q1_ONLY` and `Q1_PLUS_RANK10` are
different claims and may not share an unlabeled proof ledger.

## 5. Fail-closed status lattice

For each promoted bank the only terminal statuses are

```text
REJECT_LITERAL
LITERAL_PASS_Q1_UNRESOLVED
VERIFIED_Q1_SAT
VERIFIED_Q1_SAT_SELECTED_R10
VERIFIED_Q1_UNSAT
```

Any missing or mismatched source hash, bank hash, formula hash, map, complete
model, proof, checker result, or literal row yields `UNRESOLVED`; it is never
silently inherited from the geometry or supplier projection.

## 6. Scope

This contract verifies only D/A-promoted joined pairs.  It neither proves
that the upstream 67 geometry movers or 154 raw seams are complete nor
enumerates their supplier join.  It asserts no global residence, ranks
11--17, component joining before a selected q1 model, exterior window,
opening, regeneration, or compiler statement.
