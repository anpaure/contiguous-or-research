# Fixed actual19 histories for corrected21 connectors: review plan

Date: 2026-09-09. Original pre-execution review plan. The single reviewed
run has since completed; see the
[1,371-good /59-bad certificate](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGES_1371_GOOD_59_BAD_CERTIFICATE_20260909.md).
The remainder preserves the scope approved before execution.

The sole mathematical input is `answers/k19_optimal92381.word`, with SHA-256
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
The proposed checker is
`scratch/audit_actual19_embedded_corrected21_connector_ages_20260909.py`.
It will run only after parent and independent source review, on h100, once,
with limits 30 CPU seconds, 45 wall seconds, 1 GiB address space and
128 MiB per output file. There is no alternative parent, cut, rotation,
matching, optimization, or retry in this task.

## 1. Exact fixed family and embedding

Read the first 92,378 letters as C, verify the literal is C followed by its
first three letters, and reconstruct the cyclic triples R_i and fours U_i.
Recheck both complete middle decks, their phase relation, canonical outgoing
Phi, strict Johnson transitions, and both delayed-deletion exclusions for
residence three. Full-cube optimality is already independently verified;
this diagnostic does not repeat that much larger assertion.

Use child coordinates 0 through 20, in that physical order, and embed each
parent lower state by

    embed(P) = (P << 1) | (1 << 20).

The child begins with fixed u=0 and ends with fixed b=1. Its a-coordinate19
is active parent coordinate18. For every parent lower state P, the first
global minimum in the child is the shifted parent first global minimum:
its height is at most -2, whereas the initial child zero has height -1
and the final child height is -1. Hence Phi(embed(P))=embed(Phi(P)).
The source checks this equality throughout the actual parent cycle.
All old coordinate run lengths are preserved, while b is constantly one
along the embedded periodic incoming history.

The fixed ports are exactly P=00D1, where D is a Dyck word of semilength 8.
The checker generates all D recursively and independently scans the full
middle deck for this exact physical shape. Their equality and the derived
Catalan count are required. The quoted number 1,430 is only a comparison
field; a zero bad count is never assumed.

## 2. Connector and exact age criterion

For D=1R_tail, the four child states are

    000D11 -> 001D10 -> 011D00 -> 1110R_tail00.

The additions are coordinates 2, 1, 0. The deletions are b=20, a=19, and
the first D-bit 3. At the initial port let the exact parent ages of a
and the first D-bit be alpha and eta. The exact deletion ages are

    infinity, alpha+1, eta+2.

Thus the supplied connector is residence-three legal if and only if
alpha>=2. Its third deletion is always legal because eta>=1. All other
closed runs lie in the supplied parent history. The checker independently
replays the last three embedded parent states followed by all three new
states; these finite histories suffice for each threshold-three decision.
It checks the actual child Phi and distinct rank-10 states at every step.
The outgoing sources and all four banks are injective across D, but this
does not settle matching conflicts with the remaining parent copy.

Exact parent ages are computed by one cyclic pass beginning at an absent
state, then independently replayed backwards to an absent state at each
port. Complete good and bad records retain the physical indices, masks,
ages, parent history, and all connector states.

## 3. Exact bad-predecessor diagnostic

At P=00D1, a bad age-one arrival must come from 10D0. This can be proved
without the input word: any incoming upper has the form P+z. For the
first parent zero, that upper is 10D1 and inverse Phi deletes the final a,
giving 10D0. For the second zero, inverse Phi returns P, a forbidden self
edge. For any D-zero, the last minimum lies before that flipped D-zero;
the inverse deletes a D-one, retaining a. These exhaust the absent bits.

The checker verifies both directions against each actual predecessor and
also enumerates all its strict inverse incidences to check that 10D0 is
the sole candidate omitting a. This is a fixed finite identity check,
not a search for alternate incoming histories.

## 4. Output and interpretation

The complete certificate reports the derived port count, exact a-age
histogram, number of good connectors, and complete bad-port list. All
records are written to separate JSON files together with the pinned raw
input and source snapshot. A resource interruption before the final
certificate is incomplete and must not be reported as PASS.

PASS means that this fixed conditional age-supply diagnostic completed.
It does not mean every port passed: that assertion has a separate Boolean
field derived from the exact bad list. No spanning 21-coordinate factor, compatibility
of simultaneous parent cuts, output-age gluing, lower-target compiler,
or optimal 21-coordinate word is claimed.

The connector's pure proof is recorded in
[the two-step root-socket audit](Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md),
Section 5. The stronger all-k gluing questions remain separate.
