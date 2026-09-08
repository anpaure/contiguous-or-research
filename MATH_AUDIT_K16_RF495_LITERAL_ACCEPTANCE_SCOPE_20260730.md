# K16 repeat-free collar: literal acceptance, not flat-middle acceptance

For the frozen repeat-free odd-to-even `4/9/5` collar, a SAT assignment must
be accepted exactly when the resulting nonzero word has length `12,873` and
its contiguous ORs cover all `65,535` nonempty masks.  Requiring `D^3 A` to
be an exact enumeration of the rank-eight layer is an unsound additional
restriction for this fibre.

The marked fixed body has the form `0x8000 | seed5[7:6432]`.  Its ordinary
rank-eight child deliveries arise from three-cell old-coordinate windows
(`D^2` of the parent) together with the top bit, not from a globally flat
four-cell `D^3` row.  Handoff item 2002a records one fixed child jump in every
valid repeat-free marked body.  Thus the architecture-free equality
inventory permits a universal word with stalls/jumps/flats summing to three;
flatness is not part of the definition or lower-bound equality theorem.

The authenticated incumbent demonstrates the distinction directly.  Its
`D^3` row has length `12,870`, only `12,868` distinct masks, and rank
histogram

```
rank 8:  6,433
rank 9:  6,436
rank 10:     1
```

while its literal deficit is only the three masks `0x18e7`, `0x3de7`, and
`0x9e20`.  The exact provider CNF and maximal-core formulation correctly
target literal interval coverage and do not require a flat derivative row.

In fact, flatness is impossible throughout this frozen fibre.  The marked
fixed body has `6425` cells and therefore `6422` internal four-cell windows.
For every such window,

```
D^3(0x8000 | seed5) = 0x8000 | D^3(seed5).
```

The parent value has rank eight and does not contain the new top bit, so all
`6422` immutable child values have rank nine.  No assignment to the eighteen
collar cells can change them.

Accordingly:

1. a candidate passing literal all-mask replay at length `12,873` proves
   `nu(16)=12,873`, regardless of its derivative histogram;
2. RF495 must never pass `--require-middle-row`, because that option is a
   hard rejection gate.  With the option absent, the generic verifier still
   records `middle_row_exact` and every row-rank histogram diagnostically; and
3. UNSAT claims remain scoped to the literal provider/CNF model actually
   solved, not to a strengthened flat-carrier subfamily.

## Acceptance-path audit

The current H100 wrapper
`scratch/run_k16_rf495_provider_minconflicts_h100_20260730.sh` invokes the
generic verifier with `--k 16` and no middle-row flag.  Its staged remote copy
has the same SHA-256.  The min-conflicts engine
`scratch/search_k16_provider_choice_minconflicts_20260730.cpp` calls its
literal `exhaustive_verify` before emitting a successful word.  The separate
maximal-core verifier
`scratch/audit_ad_k16_rf495_frozen_atlas_and_provider_solver_20260730.py`
reconstructs the eighteen cells and rejects SAT unless literal replay covers
all 65,535 masks.  Neither path tests derivative flatness.

The DIMACS decoder, monotone CEGAR controller, and implicit tri-window search
were checked separately.  They respectively label a decoded word universal
only when literal replay has no missing masks, emit
`PASS_LITERAL_65535_OF_65535` only when the independent literal auditor has an
empty missing set, and replay the assembled word before writing
`VERIFIED_UNIVERSAL`.  None computes a middle condition for acceptance.

The generic flag remains legitimate for separately scoped K11/K15
flat-certificate workflows; deleting it globally would be a different and
incorrect change.  The exact audit is frozen in
`scratch/k16_rf495_literal_acceptance_scope_20260730.audit.json`.

The zero-ghost deadline and endpoint-rook pruning used by a separate RF495
search is not a disguised flatness gate.  It explicitly accounts for the one
immutable child jump, asks the twenty-three mutable starts to supply the
remaining twenty-one rank-eight labels, and leaves two mutable failures.  It
is a proved necessary presolve inside the literal fibre; terminal acceptance
still depends only on nonzero length and literal all-mask replay.
