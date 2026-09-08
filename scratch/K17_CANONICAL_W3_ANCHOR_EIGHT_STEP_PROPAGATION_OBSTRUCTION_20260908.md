# The fixed canonical width-three anchor frame is impossible

2026-09-08. Exact deterministic propagation and independent replay by `exact_b_finite_frontier`, executed only on h100. The specified canonical anchor frame cannot cover all lower targets. This is an obstruction to **one fixed periodic-bank architecture**, not to unrestricted caps, other anchor frames, later seam witnesses, or ν(17)=B(17).

The source is the [previously certified exact block menu](K17_TRIPLE_PRESERVING_SHORT_HOSTS_AND_CANONICAL_ANCHOR_MENU_CERTIFICATE_20260908.md): H≤2 components frozen, and full anchors at positions 0,3,6,... of every canonical H=3 cycle. Every allowed option combination preserves all native triples, boundary pairs, and longer native windows. There are 7,377 blocks, 2,346,272 original options, and 20,282 nonfixed target labels to cover.

## 1. Sound deterministic rules

For each block, retain its exact domain of literal cap tuples. A tuple's local outputs are its chosen letter or letters and, for a two-position block, their OR. Support of a target is counted by **distinct blocks having at least one remaining tuple containing that target**.

If a nonfixed target has only one supporting block, any covering assignment must choose a tuple containing that target at that block. Filter its domain accordingly. All previously required targets remain imposed together. An empty domain or a target with zero supporting blocks is a contradiction. This rule is a necessary deduction, not a heuristic commitment to a particular tuple.

The soundness and the distinction between block support and option/channel support were independently reviewed by `exact_b_induction` before execution.

## 2. The exact eight-step contradiction

Initially, 4,441 rank-seven labels each have only one provider block. Their mandatory preservation reduces the total option count from 2,346,272 to 1,606,918. Domains remain nonempty and every nonfixed target still has support.

Thereafter the program processes forced target labels in increasing numeric order, updating that queue after every filter. The first eight additional deductions are:

| Step | Target mask | Only supporting block | Options before | Options after |
|---:|---:|---:|---:|---:|
| 1 | 63 | 2 | 108 | 16 |
| 2 | 95 | 37 | 108 | 16 |
| 3 | 119 | 32 | 108 | 16 |
| 4 | 125 | 27 | 108 | 16 |
| 5 | 126 | 2 | 16 | 1 |
| 6 | 175 | 106 | 108 | 16 |
| 7 | 183 | 168 | 108 | 16 |
| 8 | 55 | 425 | 108 | 8 |

After step eight, target **2103** has no supporting block. It is the rank-six set `{1,2,3,5,6,12}` under the bit convention that coordinate x has bit x−1.

Its entire original provider list is:

| Block | Mandatory targets after the deductions | Remaining options containing 2103 |
|---:|---|---:|
| 425 | 55, 67639 | 0 |
| 657 | 2615 | 0 |
| 1297 | 2359 | 0 |
| 1450 | 2231 | 0 |
| 1515 | 34871 | 0 |
| 1617 | 18487 | 0 |
| 1668 | 10295 | 0 |

The rank-seven requirements in this table are each independently forced by unique original provider blocks. The last step removes the only remaining possible host of 2103. Thus no full covering selection exists in this frame.

The resulting domain count is 1,606,251, but this is not a surviving feasible domain system: target 2103 is already unsupported. Computation stopped immediately at that contradiction. Neither the preselected 1,768-target configuration-Hall check nor a channel-capacity flow was reached, and no SAT/optimization search was performed.

## 3. Independent replay and compact certificate

The producer maintains target-to-block support sets incrementally. The replay uses a different verification route:

1. Regenerate every original literal tuple from the factorized source menus.
2. Verify every initial unique rank-seven provider claim.
3. For each forced target in the trace, recompute its support by checking every original provider's current tuples, without using the producer's updated support map.
4. Regenerate the affected block's domain from its **original** tuples and the conjunction of all accumulated mandatory targets, instead of applying the producer's last incremental filter.
5. Check all final domain lists agree and that no remaining tuple in any original provider realizes 2103.
6. Independently reconstruct all 14,720 position menus from their source letters and pins and compare the decoded literal tuples.

All checks passed. The full run, including replay, took approximately 2.93 seconds under limits of 120 CPU seconds, 150 wall seconds, and 2 GiB address space.

A subsequent bounded export expands the eight trace steps into their complete original supplier rows. That compact derivation uses 30 blocks and 30 initial unique rank-seven dependencies; all dependency-uniqueness claims were checked by a fresh full-menu scan. It includes each relevant block's positions, original letters, pins and complete factorized cap menus, so no hidden rejected option is needed to interpret the trace. This export did not make further covering choices or search for another obstruction.

Artifacts:

- [Full propagation certificate](k17_anchor_propagation_20260908/anchor_support_propagation_certificate.json).
- [Compact supplier-by-supplier derivation](k17_anchor_propagation_20260908/anchor_compact_supplier_derivation.json).
- [Producer and independent replay](propagate_k17_canonical_w3_anchor_menus_20260908.py).
- [Compact derivation exporter](extract_k17_anchor_propagation_derivation_20260908.py).
- [Original exact option menu](k17_triple_anchor_menus_20260908/canonical_w3_anchor_factorized_menus.json), SHA-256 `bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642`.

Remote artifacts are in `/home/amodo/exact-b-k17-anchor-propagation-20260908/`. The larger partial residual domain-index file is retained there; it is not required to replay the contradiction from the source menu and compact derivation.

The earlier census that every target had an individual host was correct. The contradiction establishes that those individual hosts cannot all be realized together in this one canonical anchor frame.
