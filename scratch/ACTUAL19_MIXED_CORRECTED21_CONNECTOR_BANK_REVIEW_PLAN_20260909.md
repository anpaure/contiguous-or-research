# One deterministic mixed connector bank on the fixed actual19 carrier

Date: 2026-09-09. Original pre-execution review plan. The single reviewed
run has now completed; see the
[complete 1,430-port local-bank certificate](ACTUAL19_TWO_ORDER_COMPLETE1430_LOCAL_CONNECTOR_BANK_CERTIFICATE_20260909.md).
The remainder preserves the originally reviewed scope.

The checker is
[audit_actual19_mixed_corrected21_connector_bank_20260909.py](audit_actual19_mixed_corrected21_connector_bank_20260909.py).
It will use the same fixed parent and the same complete physical family
`P=00D1`, D Dyck of semilength 8, as the completed
[1,371-good /59-bad diagnostic](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGES_1371_GOOD_59_BAD_CERTIFICATE_20260909.md).
There is exactly one route choice, determined by the independently
recomputed parent age alpha of its final coordinate:

    alpha>=2: 000D11 -> 001D10 -> 011D00  -> 1110R00;
    alpha=1:  000D11 -> 001D10 -> 0110R10 -> 1110R00;
    D=1R.

No optimization, alternative parent, relabeling, cyclic phase, cut, or
matching choice is part of this diagnostic. Parent and independent full
source review are required before one possible h100 execution. Proposed
limits remain 30 CPU seconds, 45 wall seconds, 1 GiB address space and
128 MiB per output file, with external `timeout 45s`. No retry is proposed.

## 1. Fixed inputs and their role

The only carrier is `answers/k19_optimal92381.word`, SHA-256
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.

Three existing artifacts are separately pinned and copied into the output:

| Artifact | SHA-256 |
|---|---|
| Prior diagnostic source | `27388f115066d5f6270a8d8957bc3503d81ddf231aa5e65d989afeef0663a6dd` |
| Prior complete report | `fe798b2a6dbc55c4307ed252f91ca4b53c02b88dd442e3c10d8eba90360aeecc` |
| Prior complete 59-bad-port JSON | `d177285f9e8fad4f6db5e45cb9a0b82cec6775b65f6303c143304a1add11f151` |

Their local paths are respectively the original checker in `scratch/`,
and `output/actual19_corrected21_connector_age_certificate.json` and
`output/all_bad_age_one_ports.json` within
`scratch/actual19_embedded_corrected21_connector_ages_20260909/`.

The prior source is never imported or executed. Its hash only fixes the
provenance of the earlier results. The new source reconstructs the actual
middle cycle, exact ages, fixed port family, and every history from the
raw literal. It compares the independently reconstructed port partition,
histogram and all named bad records with the earlier pinned artifacts.

The carrier raw is 598,636 bytes; the prior report is 3,697 bytes; the prior
source is 16,141 bytes; the complete bad list is 56,995 bytes. The existing
26,956,277-byte full named-carrier table and 1.7 MiB incoming-circuit table
are unnecessary inputs for this rule.

## 2. Why the bad branch is legal

Let d be the first D-coordinate. At a bad port alpha=1, the previous
parent state is exactly 10D0. It already contains d, so its parent age
gamma at 00D1 is at least 2. The new route deletes b,d,a in that order;
its exact deletion ages are

    infinity, gamma+1, alpha+2 = 3.

Thus all three deletions meet residence three. The intermediate state
`0110R10` has first global minimum -1 at the first coordinate, so its
outgoing canonical Phi inserts that coordinate. Both routes end at
exactly the same `1110R00`. Their inserted prefix coordinates have ages
1,2,3 at that end; every other surviving D-coordinate has its original
age plus 3. This does not certify any continuation from the end.

The source independently replays the last three actual embedded parent
states followed by the selected three transitions. This finite history
supplies enough ages to verify every threshold-three deletion, including
the exact age-3 final deletion on the swapped route. It also checks every
actual child Phi edge, the literal bit patterns and the common endpoint.

## 3. Mixed-bank collision check

The initial and second lower banks start 000 and 001; the final bank
starts 111. Both possible intermediate banks start 011, but the old branch
has a=0 and the swapped branch has a=1. Each branch retains an injective
encoding of D. Hence the two branches cannot collide with one another,
and the four lower banks are pairwise disjoint.

The consumed upper banks start 001, 011, 111. Within the third upper bank,
the same a-coordinate distinguishes the branches. The checker verifies
all actual masks, rather than relying only on this explanation. Every
new lower and the latter two consumed uppers have b=0, outside the old
embedded inventories, which have b=1.

All incoming histories used here are the original parent histories.
Cutting and reconnecting the parent later can change those histories;
the resulting global boundary obligations are not certified here.

## 4. Complete retained outputs and precise meaning of PASS

Save every chosen four-state connector, three-state incoming history,
deletion order, exact and replayed deletion ages, and its original parent
position. Separate the unchanged original routes and the swapped routes.
The report will include the independently derived branch counts and all
mixed-bank cardinalities, with source/input/provenance hashes and limits.

PASS requires every fixed port's selected route to pass all local edge
and age checks and the complete mixed banks to be injective. The counts
1,371 and 59 are prior comparisons, not success assumptions. A resource
interruption without the final certificate is incomplete.

This is a local connector-bank certificate. It is not a repaired parent
matching, a spanning 21-coordinate factor, an upper-target preservation
assertion, or a universal 21-coordinate word. Source preparation does not
authorize execution.

The all-r pure proof is
[the two-order connector theorem](TWO_ORDER_CANONICAL_PHI_CONNECTOR_AND_COMPLETE_0P1_PORT_BANK_20260909.md).
It shows that the two exact age conditions cover every strict incoming
boundary with mature b. The finite-frontier agent independently read and
passed that complete proof before any execution of this derivative.
