# Audit: K17 drop-12 irreducible bilateral-source triple oracle

**Date:** 2026-08-03

**Verdict:** mathematical core PASS; Q-computation gate NO-GO pending an
immutable authoritative theorem and a fail-closed Task3 implementation
freeze.

## Scope

This audit concerns only triples containing at least one member of the
authenticated rank-16,878 source bank of size 468, ledger SHA
`21ab1c4f987c54d835306394c86a7aef0b96ead2caeaf31153b9513889a91050`.
To avoid collision with the separate rank-stagnant S47 bank, this audit
calls that source bank **H468**.

S47 is outside the support-two theorem. Its corrected unary common-option
zero proves only that a feasible S47 pair must use the partner host
(support at least one). It does not inherit the H468-specific
94-prefix -> 70 -> zero argument.

Task3 owns the broad B/G1/G2 join. This audit did not launch or duplicate it.

## Authority failure

The delegation named an authoritative theorem digest beginning
`85e946e1`. During independent read-only audits, the local file
`MATH_THEOREM_K17_DROP12_IRREDUCIBLE_BILATERAL_SOURCE_TRIPLE_ORACLE_20260803.md`
changed repeatedly without either auditor editing it. Observed states
included:

    66757d84...  532 lines
    30c08e08...  536 lines
    feddb58e...  560 lines
    e6f301de...  575 lines

None matches the announced prefix. Therefore no Q run can be authenticated
against the current moving file. The exact authoritative bytes must be
restored, or one final digest must be explicitly promoted and frozen in the
Task3 pre-run manifest.

## Mathematical core that passed

For an H468 source option in a feasible triple:

1. support zero projects to the unary child and contradicts exact unary zero;
2. support one projects to a directed source-rescue pair prefix;
3. losslessness of the complete pair screen places that prefix among the 94;
4. every feasible extension passes the lossless 10,536,324-to-70 upper; and
5. the complete exact 70-row replay is zero.

Hence any remaining H468-source option uses both helper hosts. This argument
does not assume that the two-mode prefix itself has a complete pair packing.

For each phase, classifying a source ticket by helper-host footprint gives
the exact donor-aware partition

    B, G1_f, G1_g, G2.

The ordered phase-class joins whose helper-support union is `{f,g}` are
exactly:

    (B,G2)       (G2,B)
    (G1_f,G1_g)  (G1_g,G1_f)
    (G1_f,G2)    (G2,G1_f)
    (G1_g,G2)    (G2,G1_g)
    (G2,G2)

Thus there are nine joins. Inclusion-exclusion gives exactly 21 source
selected-host patterns and 645 full three-role host-incidence matrices:

    7^2 - 2*4^2 + 2^2 = 21
    61^2 - 2*46^2 + 34^2 = 645.

These are finite covers, not counts of physical triples or positives.

## Frozen structural census

The structural census bundle
`scratch/audit_k17_drop12_irreducible_triple_domain_20260803` has manifest
SHA
`1f30719a9646804629d813b450eefc5dbc28dc5f8a6bdba3edd3271de8212c17`.
Its independent counters agree:

    exactly one H468 source       2,929,210,805,021
    exactly two H468 sources         10,776,672,353
    exactly three H468 sources           11,531,253
    unique H468-containing total  2,939,999,008,627

    source-labelled, helpers unordered  2,950,798,743,486
    source-labelled, helpers ordered    5,901,597,486,972

This is a structural endpoint domain only; it is not |Q| and must not be
scanned.

## Required output-sensitive staging

The first trusted Task3 run must be candidate-driven:

1. emit `B_raw(e,phase,key,ticket,casualties)` with empty helper support;
2. emit `G1_raw(e,phase,key,f,ticket,casualties)`, immediately excluding
   `d_f`;
3. emit `G2(e,phase,key,f,g,orientation,ticket,casualties)` with both
   predecessor/successor orientations and complete provenance;
4. let the phase-0/phase-1 join determine the unordered helper pair
   `{f,g}`;
5. only then reject any option whose full two-phase footprint meets
   `{d_f,d_g}` and emit the final pair-keyed B/G1/G2 and support-two ledgers.

Testing both named donors before the helper pair is known is either
ill-defined or reintroduces the forbidden helper-pair scan.

Every posting and final option must retain:

- source-bank tag `H468`;
- source and helper edge IDs, all hosts and donors;
- phase, role, B/G1/G2 class, and declared key;
- predecessor/successor orientation;
- exact state payload, root, owner, rows, flags, and full footprint;
- casualty set and complete producer/input provenance.

Helper ordering may be quotiented only after preserving G2 orientation.
Sorted physical triples may be deduplicated only after retaining every
viable H468 source label.

## Unaudited optimization

A changing theorem draft introduced a quotient into exactly 32 H468 source
transition classes. That optimization is not part of the audited core. It
must be omitted from the first trusted run unless a SHA-bound 468-to-32
census and an independent proof show that the class key includes every
argument to `incoming_possible`, `outgoing_possible`, and
`common_five_cell`.

## GO conditions

Q computation may start only after:

1. one immutable authoritative theorem digest is restored or promoted;
2. Task3 source implements the raw/final staging above;
3. an independent source audit verifies losslessness and every posting field;
4. the pre-run manifest binds theorem, all inputs, sources, build command,
   binary, run command, and target ledgers;
5. the post-run manifest binds outputs, audits, and transcripts.

Occurrence positives, if any, still require complete helper menus, exact
three-option packing, simultaneous materialization, protected-row replay,
and a fresh supplier maximum matching. No marginal supplier credit may be
inherited.
