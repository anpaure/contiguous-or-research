# Actual19 supplies 1,371 corrected21 connector histories, with 59 exceptions

Date: 2026-09-09. Status: **one fixed diagnostic completed and fully replayed**.

For the supplied optimal19 carrier, exactly **1,371 of the 1,430** fixed
ports `P=00D1`, with D a Dyck word of semilength 8, supply residence-three
incoming histories for the corrected connector

    000D11 -> 001D10 -> 011D00 -> 1110R_tail00,
    D=1R_tail.

The remaining **59** ports have active-parent-coordinate age exactly 1.
Their actual predecessors are all exactly `10D0`, as predicted by the
inverse-Phi criterion. At each such port the connector's second deletion
closes a run of length 2, so this fixed connector is not residence-three
legal with that supplied history. The original parent factor itself still
has residence at least three: the too-early deletion occurs only in the
proposed continuation.

This resolves a fixed incoming-history test. It does not splice the
connectors into a spanning21 factor or assert simultaneous matching,
output-age compatibility, all-rank coverage, or optimality at dimension21.

## 1. Inputs, review and execution

The only mathematical input was
[the verified optimal19 literal](../answers/k19_optimal92381.word), SHA-256
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
The checker is
[audit_actual19_embedded_corrected21_connector_ages_20260909.py](audit_actual19_embedded_corrected21_connector_ages_20260909.py),
SHA-256 `27388f115066d5f6270a8d8957bc3503d81ddf231aa5e65d989afeef0663a6dd`.

Root and the structure agent independently read the full source and
[review plan](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGE_DIAGNOSTIC_REVIEW_PLAN_20260909.md)
before authorizing the single run. The finite-frontier agent also reread
the complete source. This is internal independent review, not an external
review claim.

Exactly one execution ran on h100, hostname `arboghast`, with 30 CPU
seconds, 45 wall seconds, 1 GiB address space, and 128 MiB per output file;
an external `timeout 45s` supplied the additional wall guard. The run
exited 0, using **0.542291545 CPU seconds** and
**0.5424529858864844 wall seconds**. No retry, alternate parent, relabeling,
phase choice, cut, matching, or search occurred.

## 2. Exact finite checks

The checker independently reconstructed the first 92,378 literal letters
as one cyclic period and verified that the remaining three repeat its
prefix. Cyclic triple and four-letter unions gave the complete, distinct
rank9 and rank10 decks, with the exact union/intersection phase. Every
parent edge was a strict Johnson edge with canonical outgoing Phi, and
both delayed-deletion exclusions for residence three passed.

For each parent state P the child embedding was exactly

    embed(P) = (P << 1) | (1 << 20).

Thus child coordinate0 is fixed absent, coordinate20 is fixed present,
and parent coordinate18 becomes active child coordinate19. The checker
verified canonical-Phi preservation on all 92,378 embedded states.

The fixed Dyck family was generated recursively and also independently
identified by scanning the complete parent middle deck. These inventories
agreed, and their count agreed with the exact Catalan formula. Neither
1,430 nor a zero-exception outcome was an assumed success criterion.

Exact cyclic ages were computed from a zero-anchored pass and independently
replayed backwards to the preceding absent state at every port. Every
strict inverse incidence at every port was also checked: `10D0` is the
unique candidate predecessor omitting the active final parent coordinate.

For every proposed connector, the checker replayed its three actual Phi
steps after the final three supplied parent states. If the parent ages
at the port are alpha for its final coordinate and eta for its first
D-coordinate, the exact deletion ages are

    infinity, alpha+1, eta+2.

The finite history independently supplied ages
`3, min(alpha,3)+1, min(eta,3)+2`, sufficient to certify exactly the same
threshold-three outcome. This replay passed for every good and bad port.
The four lower banks and three outgoing-upper banks were injective and
disjoint across the fixed family. This incidence fact is separate from
compatibility with the remaining parent factor.

## 3. Observed result and complete evidence

| Quantity | Verified value |
|---|---:|
| Fixed ports | 1,430 |
| Residence-three legal connectors | 1,371 |
| Bad age-one ports | 59 |
| Ports with active-coordinate age 2 | 0 |
| Smallest active-coordinate age among good ports | 3 |
| Largest active-coordinate age | 54 |

All 59 bad records identify the exact parent position, D, predecessor,
last three parent states, proposed child states, and failed second-edge
age. The full histogram and complete good/bad partition are retained in
the evidence directory:

- [Complete diagnostic certificate](actual19_embedded_corrected21_connector_ages_20260909/output/actual19_corrected21_connector_age_certificate.json).
- [Every fixed port](actual19_embedded_corrected21_connector_ages_20260909/output/all_fixed_connector_ports.json).
- [All 1,371 good connectors](actual19_embedded_corrected21_connector_ages_20260909/output/all_good_connectors.json).
- [Exact list of 59 bad ports](actual19_embedded_corrected21_connector_ages_20260909/output/all_bad_age_one_ports.json).
- [Run log](actual19_embedded_corrected21_connector_ages_20260909/run.log),
  [provenance](actual19_embedded_corrected21_connector_ages_20260909/PROVENANCE.md),
  and [remote artifact hashes](actual19_embedded_corrected21_connector_ages_20260909/SHA256SUMS).

The complete report has SHA-256
`fe798b2a6dbc55c4307ed252f91ca4b53c02b88dd442e3c10d8eba90360aeecc`.
All ten copied remote files passed their stored SHA-256 manifest locally.

The pure connector and input-age criterion are proved in
[the corrected-root-socket audit](Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md),
Section5. The new numerical result is the exact fixed-parent split into
1,371 supplied histories and 59 failures; no global completion is inferred.
