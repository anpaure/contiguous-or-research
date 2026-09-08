# Literal nineteen-coordinate carrier: exact phase and bounded diagnostic

2026-09-09. Pure derivation and pre-execution plan by
`exact_equality_structure`. The subsequently authorized single run
completed PASS; the exact result is linked in Section 4.
Root and frontier separately audit complete coverage of the supplied
literal words. This diagnostic reconstructs only the specified literal19
carrier and its low-rank compiler; it does not reproduce an unprovided
compact generator or search history.

## 1. Input and requested scope

The supplied word is `answers/k19_optimal92381.word`, copied from the
identically named Downloads file. Root supplies the pinned SHA-256 to
the checker's required `--word-sha` argument before execution.

Root has now supplied that pinned literal hash:

    1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414.

The directly existing canonical input is

    /home/amodo/exact-b-k19-height-adaptive-20260908/height_adaptive_canonical_cycles.json

Its bounded header/hash read established the retained schema
`cycle,height,length,lower_owners` and SHA-256

    5e44113db3152b216af7761766f69a7b389db54b5c1f5dce9ac227ba6e6e71cd.

The checker is
`scratch/reconstruct_k19_optimal_literal_carrier_and_lower_compiler_20260909.py`.
It permits exactly one deterministic run on h100 (`arboghast`), with
60 CPU seconds, 90 wall seconds, 2 GiB address space, and 1 GiB per
output file. It performs no search, trial switch, relabeling, word edit,
or fresh canonical factor construction. Any failed required architecture
check is saved as `failure_report.json` and stops the run without retry.

## 2. Correct envelope phase, derived from the literal

Suppose the literal has the verified form A=C followed by its first
three letters, with |C|=92378. Define cyclically

    R_i=C_i union C_(i+1) union C_(i+2),
    U_i=C_i union ... union C_(i+3),
    E_i=U_(i-3) intersect ... intersect U_i.               (2.1)

If all R_i have rank nine, all U_i have rank ten, and the U_i are
distinct, then

    U_(i-1) intersect U_i=R_i.                            (2.2)

Indeed R_i is contained in both upper sets, and distinct rank-ten
sets cannot have a rank-ten intersection.

Every one of the four factors defining E_i contains C_i. Thus C_i is
contained in E_i. Also each of E_i,E_(i+1),E_(i+2) is contained in both
U_(i-1) and U_i. Consequently

    R_i subseteq E_i union E_(i+1) union E_(i+2)
        subseteq U_(i-1) intersect U_i=R_i.

Hence the EXACT phase is

    OR(E_i,E_(i+1),E_(i+2))=R_i.                         (2.3)

There is no phase shift under convention (2.1). Likewise four successive
E letters have union R_i union R_(i+1)=U_i. The checker tests these
identities on actual masks, including every wraparound window.

The apparent indexing concern only arises if an external carrier uses
a different definition of R_i or U_i. This reconstruction defines both
from the literal, so it does not assume that an unprovided generator's
index zero or orientation agrees with (2.1).

If (2.3) holds, entrywise lowering E to C preserves every triple and
therefore every longer cyclic interval. Pair preservation is NOT assumed.
The checker records every pair changed by the caps and explicitly
reconstructs all literal/pair targets of ranks one through eight.

## 3. The named matching and exact diagnostic outputs

The checker verifies that R and U are bijections onto the complete
rank-nine and rank-ten layers. It records

    outgoing(R_i)=U_i,
    incoming(R_i)=U_(i-1),
    successor(R_i)=R_(i+1).

For each rank-nine mask R, it calculates the canonical unmatched zero
as the FIRST minimum of its linear ones-minus-zeros prefix walk in
positive coordinate order. Adding that zero is the fixed matching Phi.
The exact matching identification is proved in
`scratch/PBBS_PHI_LEXICAL_MATCHING_AND_PUBLISHED_HAMILTON_RESIDENCE_AUDIT_20260909.md`,
Section 3. No canonical cycle reconstruction is needed for this check.

Agreement of the actual outgoing matching with Phi is a DIAGNOSTIC,
not a required premise. A valid word may change both canonical matchings.
Any disagreement is retained with all violating positions, and the
low-rank, quotient, and canonical-comparison checks continue. Both the
incoming and outgoing changed counts are reported.

It then checks both delayed-deletion exclusions on the actual successor
cycle. The envelope ranks, literal ranks, pair ranks, and individual
triple-deficit pins are reported without assuming pair preservation.

Every target of rank at most eight must be a literal or pair, because
every triple has rank nine. All such masks are enumerated and their
actual ordinary witnesses inside A=C+C[:3] are replayed directly. This
gives the COMPLETE low-rank literal/pair sets, their overlap, and all
pair-only targets. Complete higher-rank coverage remains the separate
full-word verification, not an implication from these rank counts alone.

The existing canonical19 factor is compared on the SAME named lower
labels. The checker decomposes the difference of the two incoming
matchings into alternating circuits; it does not try those circuits as
surgeries. This comparison is additional provenance, not a hypothesis
for the literal word's validity.

Finally it derives the 4862 physical rotation orbits of all rank-nine
masks. Every named field is checked for rotation equivariance before a
representative row is claimed to determine that field. The complete
named carrier is saved regardless, so a non-equivariant literal cap is
not silently represented by one representative. These recovered rows
are data extracted from the supplied word, not a supplied compact
construction certificate.

## 4. Current status

Root and frontier read the source fully. After the explicit adjustment
making actual Phi agreement diagnostic rather than a premise, root
authorized one h100 run. It completed PASS in 2.659485 seconds. Complete
results and provenance are recorded at
`scratch/K19_OPTIMAL_LITERAL_PHI_CARRIER_PAIR_CHANGING_COMPILER_AND_QUOTIENT_CERTIFICATE_20260909.md`.
There was no retry or expanded scope. The cursor/run-credit proof completed
before this new task remains saved separately at
`scratch/EXACT_TWO_PROJECTION_CURSOR_GLUING_AND_COMPOSABLE_RUN_CREDIT_20260909.md`.
