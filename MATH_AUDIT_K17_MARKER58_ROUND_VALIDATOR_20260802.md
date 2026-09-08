# K17 marker58 quotient/residence round validator (2026-08-02)

## Scope

This package validates a SAT assignment for any current marker58 quotient
CEGAR round.  It does **not** run a solver and makes no ranks-11--17,
antecedent/compiler, or universal-word claim.

The validator is fail-closed.  It accepts decoder exit 0 (connected,
nonzero-voltage lift) or 10 (authenticated factor needing a topology cut),
then always audits residence.  Every other decoder/extractor inconsistency is
fatal.

## Sources

- `scratch/decode_verify_k17_marker58_upper_q1_quotient_model_20260802.cpp`
  (`8ea0416b010868b371539e3149562f72bd7cf8cfe1cd7981bc8ada816043e61b`)
- `scratch/extract_k17_marker58_quotient_residence_blockers_20260802.cpp`
  (`a489e9286a571fe50cc6d187443e4b60b115250d6b0dd070ec15604a6a038f86`)
- `scratch/validate_k17_marker58_quotient_cegar_round_h100_20260802.sh`
  (`2f4d043bb180a025e691e1c16a1be6fe2e741089119783679758379ea1613fd0`)
- `scratch/run_k17_marker58_upper_q1_quotient_cegar_h100_20260802.sh`
  (`0bc6b6b635470379d80f2eed18598ace65a202864035b52ab3ac4494b22ac498`)

The last runner is prepared only; it was not launched in this audit.

## Exact checks

For a full solver assignment the decoder replays every DIMACS clause.  For a
sparse positive-primary model it rejects negative/auxiliary partial input,
sets absent primaries false, synthesizes the exact sequential-counter
auxiliaries, and then replays every DIMACS clause.  It independently checks:

1. all 1,430 quotient edges and 24,310 developed physical edges;
2. the exact rank-8 palette, rank-9 degree two, and all 19,448 rank-10 caps;
3. quotient components and their signed voltages;
4. literal physical components by BFS;
5. the predicted lift-component count against physical BFS.

The residence extractor then traverses **every** physical degree-two
component.  Constant coordinate traces on one component are legal and are
recorded.  For every positive coordinate run of length two or three it emits
the negation of the selected nonfixed quotient options on the entering,
internal, and leaving edges.  Repeated variables in one short segment are
deduplicated.  Identical clauses may aggregate multiple run types, and their
physical occurrence count is required to be divisible by 17.  A length-one
run is rejected because it contradicts the exact rank-8 facet palette.  An
all-fixed short run is a terminal obstruction for this protected target
class.

These blocker clauses remain necessary when the current factor is
disconnected: retaining their selected quotient variables retains all 17
translated short runs.  In any eventual connected Z17-equivariant cycle a
single linear cut cannot absorb all 17 translated closures.

The shell wrapper stages outputs in a fresh directory, hashes all inputs
before and after validation, independently checks that every emitted primary
blocking clause is falsified by the current model, and publishes an output
manifest atomically.

## H100 no-solver regression

Root:

`/home/amodo/or15/work/root_k17_marker58_round_validator_regression_20260802_quotientaudit`

No SAT solver was launched.

| input | expected result | observed |
|---|---:|---:|
| original disconnected c68b model vs base CNF | authenticated nonterminal | exit 10; 2 component cuts; 318 residence blocks |
| connected double-fusion model vs base CNF | topology pass, residence nonterminal | exit 10; 0 component cuts; 316 residence blocks |
| same connected model vs frozen round-1 CNF | old model rejected | exit 1; `assignment falsifies CNF clause` |

The disconnected physical factor was traversed as 19 components with size
histogram `42:17, 442:1, 23154:1`; it produced 5,406 short physical runs and
318 quotient blockers.  The connected factor reproduced the previously
frozen residence-clause SHA exactly:

`9948bd6152774219b93adf7f5476929ad6e1a8a4338b9ddd38504ce47eaf3e51`.

## Repeated-CEGAR output contract

For an authenticated SAT assignment the wrapper publishes:

- `next_component_cuts.tsv` for the next quotient build;
- `next_primary_blocks.cnf`, the deduplicated union of the current exact
  zero-voltage assignment block and all residence blocks;
- the reconstructed `factor.tsv`;
- decoder and residence audits, occurrence ledger, stable input hashes, and
  `SHA256SUMS`.

Return codes are 0 only for q1/topology/cyclic-residence pass, 10 for another
CEGAR round, 20 for an all-fixed protected residence obstruction, and 1 for a
validation failure.
