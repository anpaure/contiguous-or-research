# All 1,430 fixed actual19 ports have verified local two-order connectors

Date: 2026-09-09. Status: **one deterministic mixed-bank run completed**.

On the same verified nineteen-coordinate carrier, the deterministic rule

    parent a-age >=2:  000D11 -> 001D10 -> 011D00  -> 1110R00;
    parent a-age  =1:  000D11 -> 001D10 -> 0110R10 -> 1110R00;
    D=1R

passed at **every one of the 1,430 fixed ports** `P=00D1`, with D Dyck of
semilength 8. It retained the original route at 1,371 ports and swapped
the last two deletions at exactly the 59 previously identified failures.
All mixed lower and consumed-upper banks were injective and mutually
disjoint. The endpoint and the ages of its surviving coordinates agree
between the two routes.

This certifies a complete local connector bank with the original supplied
incoming histories. It does not construct a spanning 21-coordinate factor, restore
the histories after global gluing, or prove full-cube coverage.

## 1. Exact local proof and fixed finite task

The all-r construction is proved in
[the two-order connector theorem](TWO_ORDER_CANONICAL_PHI_CONNECTOR_AND_COMPLETE_0P1_PORT_BANK_20260909.md).
The first route deletes b,a,d; the second deletes b,d,a, where d is the
first D-coordinate. Their exact deletion ages are respectively

    infinity, alpha+1, gamma+2;
    infinity, gamma+1, alpha+2.

At a strict incoming boundary only one present coordinate can have age 1.
If alpha=1, then gamma>=2, so the second route is legal. At the actual
bad ports the stronger saved predecessor identity 10D0 also proves that
d was already present before the port. The new run independently checks
this against the raw carrier.

The [review plan](ACTUAL19_MIXED_CORRECTED21_CONNECTOR_BANK_REVIEW_PLAN_20260909.md)
fixed this rule before execution. No alternative parent, permutation,
cut, matching, optimization, or search was permitted or performed. The
prior 59-bad list was pinned, but no successful new route was assumed.

## 2. Inputs, review and bounded execution

Source:
[audit_actual19_mixed_corrected21_connector_bank_20260909.py](audit_actual19_mixed_corrected21_connector_bank_20260909.py),
SHA-256 `a696a4cff29f93675f987a23f7b9db726642d6d3c9f9161d2cbc83ddd991902d`.

Sole carrier input:
[k19_optimal92381.word](../answers/k19_optimal92381.word), SHA-256
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.

The earlier diagnostic source, report and complete bad-port list were
also pinned and copied. The new source does not import or execute the
earlier checker. It reconstructs every middle owner and history from
the raw literal and independently compares all prior bad records,
branch counts and the full age histogram.

Root and the induction agent completed full independent source/plan
reviews before authorization. The finite-frontier agent also reread the
complete source and the all-r pure proof. Exactly one execution ran on
h100 (`arboghast`), with hard limits 30 CPU seconds, 45 wall seconds,
1 GiB address space and 128 MiB per output file, plus external
`timeout 45s`. It exited 0, using **0.553959171 CPU seconds** and
**0.5544336368329823 wall seconds**. No retry occurred.

## 3. What was replayed

The checker verified the raw SHA and exact period-plus-three identity,
complete rank-9/rank-10 decks, physical union/intersection phase, all
canonical outgoing Phi edges, strict Johnson transitions, and residence
three throughout the parent. It also checked canonical-Phi commutation
of the fixed physical child embedding `(P<<1)|(1<<20)` on every parent
state.

The Dyck family was independently generated and found in the complete
deck. Exact cyclic ages were computed from an absent-state anchor and
independently replayed backwards at every port. Every strict inverse
incidence at every port was checked. The chosen route was then replayed
after its last three actual embedded parent states, verifying all
deletions at threshold three and every canonical child upper.

| Check | Actual result |
|---|---:|
| Complete fixed port family | 1,430 |
| Unchanged original routes | 1,371 |
| Swapped routes on the prior bad list | 59 |
| Locally legal selected routes | 1,430 |
| Size of each of four lower banks | 1,430 |
| Size of each of three consumed-upper banks | 1,430 |

The four lower banks are disjoint, including the old/new choice in the
third state. The three upper banks are also disjoint. The three new
lower banks have b=0, so they lie outside the embedded parent inventory.
Both routes have the same final mask and prefix-coordinate ages 1, 2, 3;
every surviving D-coordinate gains three states of residence. The final
a-deletion on every swapped route has exact age 3.

## 4. Complete artifacts and scope

- [Final report](actual19_mixed_corrected21_connector_bank_20260909/output/actual19_mixed_corrected21_connector_bank_certificate.json).
- [Every selected connector and history](actual19_mixed_corrected21_connector_bank_20260909/output/all_mixed_connector_ports.json).
- [All unchanged routes](actual19_mixed_corrected21_connector_bank_20260909/output/all_unchanged_original_routes.json).
- [All 59 corrected routes](actual19_mixed_corrected21_connector_bank_20260909/output/all_swapped_bad_port_routes.json).
- [Run log](actual19_mixed_corrected21_connector_bank_20260909/run.log),
  [exact command](actual19_mixed_corrected21_connector_bank_20260909/exact_command.txt),
  [provenance](actual19_mixed_corrected21_connector_bank_20260909/PROVENANCE.md),
  and [remote artifact hashes](actual19_mixed_corrected21_connector_bank_20260909/SHA256SUMS).

The complete report has SHA-256
`a624b70497760bc114e1b8ad9efb1c50107a16a8b33ecbbe5b1e59b1aece621e`.
All 12 remote artifacts were copied locally and passed their stored
SHA-256 manifest. The exact command and provenance are also retained.

The original 1,371/59 diagnostic remains correct for its single route.
This separate result removes its local exceptions by changing the
deletion order. Its inherited histories are still the original parent
histories; global reconnection must supply compatible boundary ages.
Unused child states, residual matching, global connectivity, upper-rank
targets and literal lower compilation remain separate requirements.
