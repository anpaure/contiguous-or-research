# Thread D: occurrence296+C6 pure-hex master

Date: 2026-07-31  
Status: **encoding/build PASS; complete static forest-first pure-C6 face exact UNSAT; no K17 word claim**

## 1. Frozen scope

This master is rebased on the frozen occurrence296+C6 local minimum and the
complete boundary-correct marked-safe C6 catalogue.  It does not reuse the old
base's applicability or orientation bits.  The exact input catalogue contains
`28,121` columns from `45,024` applicable identities.

Two faces are represented:

1. `cycle`: retain the complete composed degree-two factor and require a
   single component;
2. `forest`: freeze protected incidences and both endpoints of every
   selected-touched lower colour, then leave a fresh asymmetric residual
   `b`-flow downstream.

Neither face includes the final common-cap compiler or literal K17 word
verification.

## 2. Exact structural system

For every selected C6 column the three removed and three added incidences are
literal.  The master installs every nontrivial removed-incidence and
added-incidence clique as an **unguarded** structural constraint.  Since each
column has zero signed degree at every owner and lower colour, these binary
incidence bounds are equivalent to a simple degree-two factor.

The initial guarded obligations are all `296` inherited forest hazards and
the independently proved floor `sum y_h >= 66`.  The build has

```text
selection variables                 28,121
initial guarded obligations             297
total variables                     28,418
constraints                         44,097
serialized proto bytes           1,908,351
```

Assumption cores are sufficient only relative to this complete hashed
unguarded structural system.  They are not standalone CNF/DRAT certificates
and are not deletion-minimal without replay.

## 3. Residence and topology separation

In forest mode, marked interiors are scanned at physical-token threshold
three and complementary owner interiors at threshold four.  Every path
endpoint and every marked/complement transition exports its exact bounded
collar.  Those collars are explicitly labelled
`EXPORTED_OBLIGATIONS_NOT_ENFORCED`; a forest PASS is therefore only a
skeleton PASS pending residual chronology and literal zipper replay.

A proper frozen zero-socket cycle is rejected.  If the frozen graph is the
full spanning factor, or in cycle mode once one component remains, the master
constructs the exact physical zipper row and scans it at threshold three,
including both marked/facet boundaries.  Each bad run yields a local
final-incidence no-good from the factor edges determining its extended token
window.  The frozen baseline regression is

```text
physical-Z strict runs 503 = 230 motifs of 6 incidences
                           + 273 motifs of 8 incidences.
```

## 4. Exact rank-ten composition

The linear closing colour `6394` is omitted.  Every other rank-ten provider
is reconstructed from the two final endpoints of its lower colour.  Lazy
rows use exact endpoint-pair AND variables, so two C6 columns changing
opposite endpoints retain their quadratic cross term.  Isolated signed gains
are not summed.  The baseline regression has exactly `1,585` rank-ten holes.

Forest mode uses these loads diagnostically by default because the residual
`b`-flow may change released endpoints.  Cycle mode makes them hard.

## 5. Bounded forest-first run

The independently audited source was executed once on one H100 CPU under a
2 GiB address-space cap.  It completed normally in three CEGAR rounds:

| round | exact solver status | columns | new exact cuts | diagnostic rank-ten holes |
|---:|---|---:|---:|---:|
| 0 | FEASIBLE | 197 | 364 internal R3 + 3 zero-socket cycles | 1,724 |
| 1 | FEASIBLE | 208 | 371 internal R3 | 1,725 |
| 2 | INFEASIBLE | -- | -- | -- |

The round-two proof took `0.089855` seconds after the two 90-second candidate
rounds.  It is an exact **scoped UNSAT for the complete static marked-safe
pure-C6 forest master**, with rank ten diagnostic rather than hard.  The
sufficient obligation core has all `1,035` guards:

```text
forest hazards             296
certified floor              1
internal residence motifs  735
zero-socket cycles           3
```

The full-cycle face is a restriction of this forest-first face: any legal
one-cycle selection can be frozen and completed by choosing its own released
incidences again, and its exact physical zipper passes every deferred collar.
Consequently this forest UNSAT also excludes every static cycle-preserving
selection from the same `28,121`-column catalogue.  A separate cycle solve is
unnecessary and was not launched.

There are no hard rank-ten rows in that core.  Therefore the contradiction is
already hazard/resource/residence/topology, and cannot be attributed to the
ten holes lacking isolated one-column providers.  The raw union printed on
the guarded rows has `440` old component labels, but this is not yet a safe
arity-two promotion scope: assumption replay/minimization and structural
factor-graph closure are required by Section 6.

Bounded deletion minimization then replayed the full `1,035` assumptions
exactly UNSAT and contracted them to the following exact sufficient core:

```text
guard 111: hazard 111, unique C6 provider column 25925, component 943;
guard 588: one complementary internal-R3 final-edge motif,
           components 943 and 1715;
guard 763: one complementary internal-R3 final-edge motif,
           components 601, 943 and 1715.
```

The three-guard final replay is exact UNSAT.  Removing each singleton was
`UNKNOWN` under its one-second bound, so this is deliberately labelled
`SUFFICIENT_CORE_MINIMIZED_WITH_RETAINED_UNRESOLVED`, not deletion-minimal.
The minimizer used 13.53 seconds and 223,132 KiB peak RSS.  Its first two
pre-solver launches failed at library/protobuf initialization and are recorded
as `ABORTED_NOT_UNSAT`; neither contributed a proof.

The later final-expression audit supplies the missing deletion witnesses and
therefore upgrades the **mathematical three-row core** to deletion-minimal,
without reinterpreting the bounded minimizer's status:

```text
omit guard111: choose no column; motif sums (588,763)=(5,4);
omit guard588: choose {25925}; guard763 sum=5;
omit guard763: choose {25925,26083}; guard588 sum=5.
```

All three selections obey the exact removed/added incidence capacities.  Thus
every row is necessary although the one-second CP tests were inconclusive.

The forced column `25925` is cycle-preserving and hits hazards
`111,192,193`.  Its isolated boundary-correct rank-ten ledger gains no
currently missing target and deletes the unique providers of targets
`108460` and `112584`, for net hole change `+2`.  Rank ten was not a hard row
in the contradiction, but any compound replacement for this core must retain
the complete endpoint-labelled ledger: an unlabelled “two losses” scalar is
not composable because opposite-endpoint changes have cross terms.

The minimized-core result is
`scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.core.minimized.json`,
SHA-256 `449b57349a84a3138983b13c49bf4e6ac97ba4e506bbc3b0f66e71df3249c9ca`,
payload `d5bf70eb6038d5ea72e77f7515b652e8d9b7df85580bbb1433e8b6fdfed28727`.
The proof-safe minimizer source has SHA-256
`0f9937ab2a5ed074c9d01653394622e37bc67e09b6d93a43ec1c0506c775b417`.

Independent proto replay also explains why the original all-guard core could
not define a local escalation: its floor guard contains all `28,121` column
variables, so its structural factor-graph closure is global.  The final proto
has `29,232` variables and `45,281` rows: `28,121` columns, `1,035` guards,
`76` touch auxiliaries, `43,800` incidence cliques, `446` touch-definition
rows, and `1,035` guarded obligations.  Local promotion must therefore use
the replayed three-row core, not the raw all-guard core.

The run used 198.05 seconds wall time and 357,776 KiB peak RSS, exited zero,
and emitted no selection because the terminal status is INFEASIBLE.
`TIMEOUT`, `CPU_LIMIT`, and other resource exits would have been `UNKNOWN`,
never UNSAT.

Frozen run artifacts:

- result:
  `scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.result.json`,
  SHA-256 `85f059f7d8d271c41179b76f63f7e43f224fde7c9276813a445203bfb3ce4ed1`,
  payload `ac4f12fccf48975d4927ff5a63be8a39d6016be1e7d4d13e3ab94592a93abd17`;
- final model:
  `scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.final.model.pb`,
  SHA-256 `711fded03cf8829bbd145c1786acdaadf9bf7bb3678bf94fa3942213bb177a06`;
- final guard map:
  `scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.guards.json`,
  SHA-256 `94e7a7c473ee3f06535953e977f59870025fa6dfe0070e524cfe8d9cdd5a7649`;
- stdout/resource/exit SHAs begin `ea35a957/b960d17b/9a271f2a`.

## 6. Arity-two escalation rule

The minimized core has an exact conditional-return, or holonomy, normal form.
Condition on the unique hazard provider `h=25925`.

* Guard `588` has all six final-incidence literals true.  Among the complete
  marked-safe C6 catalogue, the only compatible column that can falsify one is
  `a=26083`, by removing incidence `(112392,128776)`.
* Guard `763` initially has sum five because nonbaseline incidence
  `(112392,112394)` is absent.
* The forced primary `a=26083` adds exactly that incidence.  Guard `763` then
  has sum six.
* None of its remaining true baseline literals has a remover in the complete
  marked-safe catalogue compatible with `h`; the added literals cannot be
  removed by a base-relative C6 column.

Thus the conditional service system has primary-bank size one, return-bank
size zero, no direct joint service, no exact service edge, and two-obligation
Rado rank one.  This is stronger than a two-column search failure: once `a`
is selected, the second six-literal clause is monotonically locked.  It gives
a hand-checkable local explanation of the full pure-C6 UNSAT.

The exact local resource scope is small before transitive clique closure:

```text
principal core component labels          {601,943,1715}
forced/primary columns                    {25925,26083}
their owner-component labels              {601,943,1715,3661,3734}
one-hop resource halo columns             {25925,26082,26083,26134}
strict helper columns                     {26082,26134}
```

Helper `26082` conflicts with `h` on removed incidence
`(108424,108488)`; helper `26134` conflicts with `a` on removed incidence
`(124680,124682)`.  The full resource-clique transitive closure contains
`28,041/28,121` C6 columns and is deliberately not used as a local promotion
scope.  The certified compound target is instead the principal three-label
core plus the explicit one-hop halo above.

The exact solver-free signature is
`scratch/threadD_k17_occ296_c6_core3_rado_signature_20260731.audit.json`,
SHA-256 `d3f50520c9ee47b8a7572c885d72a871fdf1751ce7fcb9cdf02a2c12b5c463aa`,
payload `94e1b52a49ace3814c5ec2bbc264ece764ad43ed2cbcc56f6e62a57ad018a42a`.
Its generator has SHA-256
`932620861cf33a272ef60652944b365c8cc489343d757f59d8c86b937b56a93c`
and ran for 19.92 seconds at 185,884 KiB peak RSS.  Earlier fail-closed
attempts emitted no certificate and are not used.

Independent literal replay returned
`PASS_INDEPENDENT_CORE3_RADO_SIGNATURE_REPLAY` in
`scratch/threadD_k17_occ296_c6_core3_rado_signature_independent_20260731.audit.json`,
SHA-256 `eff0314f7d31105329cbd6ff6ee1b20d9747ccfeb948f14aaac511fa6c12a9cf`,
payload `3b21c7b827b1cce49a90c7bb13095f92353530e5221e8eb0e70cb4310d8b03eb`.
It independently checks motif arithmetic, resource compatibility, rank-ten
endpoint deltas, helper conflicts and deletion witnesses; catalogue-wide
uniqueness remains pinned to the exhaustive source audit rather than being
re-enumerated a third time.

This lock certifies where arity-two promotion begins; it does not itself
construct a split/merge packet.  A valid promoted packet must service guard
`588` without activating guard `763`, or atomically export a new falsifier for
the latter, while preserving the complete incidence and provider ledgers.

Arity-two split/merge packets are promoted only after a replayed pure-hex
obstruction.  Starting from the guarded core variables, take closure in the
factor graph of all unguarded incidence cliques, touch definitions, and
endpoint-pair AND definitions.  Only provenance components in this closure
are principal promotion components.  An outside helper is admitted only
through an explicitly enumerated resource/socket halo.

Each promoted packet must retain the lossless signature

```text
inputs and oriented output forest;
owner, lower-colour, removed-incidence, added-incidence resources;
signed socket current and endpoint pairing;
serviced core rows and required/forbidden guards;
internal R3 defects plus both endpoint collars;
endpoint-labelled rank-ten transitions;
rank-eleven/twelve accumulated-union transfer.
```

Rado's theorem applies only if the complete guarded installability relation
has actually been represented as vertex-disjoint paths in a fixed unit
network.  Otherwise selection remains an integral resource-conflict master;
pairwise compatibility is not silently called a matroid.

## 7. Frozen build artifacts

- Source: `scratch/threadD_solve_k17_occ296_c6_pure_hex_master_20260731.py`,
  SHA-256 `3adc26bf1885b74cd62faa838f49ae423807106eb5518c847b5460d9287d09c6`.
- Build result: `scratch/threadD_k17_occ296_c6_pure_hex_master_20260731.build.json`,
  SHA-256 `872cf786390f1162acbf673cd915b7e318de6a4fcc064d935ec527959d9f3a52`.
- Guard map: `scratch/threadD_k17_occ296_c6_pure_hex_master_20260731.guards.json`,
  SHA-256 `f336656eea210ee6dea34cd1baab5287539e83805c90e7f7e26b5897a4683b78`.
- Model proto: `scratch/threadD_k17_occ296_c6_pure_hex_master_20260731.model.pb`,
  SHA-256 `967ff87277c99381d80544e0bc92d0a02beea24f3ddc5455c79109d75c54aedd`.
- Build resource log:
  `scratch/threadD_k17_occ296_c6_pure_hex_master_20260731.resource.txt`,
  SHA-256 `ad53a0863585c923238f47792440bfe6862ceb1cb48569d16a8c7531f2951c33`.

The build used 14.58 seconds and 191,016 KiB peak RSS.  Independent source
audit returned PASS for the declared scope.  No feasibility statement follows
from a build-only PASS.
