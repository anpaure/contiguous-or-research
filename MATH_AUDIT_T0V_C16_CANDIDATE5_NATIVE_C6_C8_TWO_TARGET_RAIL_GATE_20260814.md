# Hostile audit of the candidate-5 native `C6/C8` two-target rail gate

**Date:** 2026-08-14
**Verdict:** **PASS** for the literal finite scopes in the source.  The
result is an exact one-/two-cycle obstruction and a marked-collar
reduction, not a construction of that collar.

**Audited source:**
`MATH_OBSTRUCTION_T0V_C16_CANDIDATE5_NATIVE_C6_C8_TWO_TARGET_RAIL_GATE_20260814.md`

## 1. Rank and rail audit

The two literal values have ranks `12,12`, intersection rank `11`, and
symmetric-difference rank `2`; current-factor owners have rank `9`.  The
source therefore uses `|H|=R+2`, not the invalid `R+1` ansatz.  In the
normal form, every middle owner deletes two elements of `H`, consecutive
deletion pairs meet once, and their triple intersection is empty.  This
proves Johnson adjacency and middle union `H`.  Each endpoint performs one
exchange and adds the appropriate external coordinate.

The independent literal witness replay checks:

* five distinct rank-nine owners;
* four Johnson adjacencies;
* four distinct rank-ten upper colours; and
* first/last four-owner unions equal to `A/B` exactly.

The exhaustive complement-pair enumeration finds `721710` rails.  Its
missing-incidence histogram sums to that total.  In particular the minimum
is three, attained `404` times, and `404+8406=8810` rails are within the
native `C8` insertion budget.

## 2. Native completion audit

For every three-missing rail the verifier independently chooses the old
selected mate at each affected colour, requires distinct owners, equality
of old/new owner sets, degree two on the alternating support, and one
connected component.  No `C6` survives.

For `C8`, four missing incidences are checked directly.  A three-missing
rail is extended by every possible fourth Johnson exchange before the
same mate/degree/connectedness replay.  No `C8` survives.  These tests are
rail-completion tests; the later atlas is the stronger parameter-free
check.

The target-start construction enumerates every absent incidence whose
upper colour is contained in `A` or `B`, follows every simple alternating
cycle of the requested size, and deduplicates by full support.  Its `1936`
start arcs produce exactly `382` `C6` and `1495` `C8` supports.  Full path
and upper-`q3` replay finds zero single-cycle dual creators.

## 3. Two-cycle current audit

The typed signature records the complete signed Counters for owner,
upper/lower `q1`, and upper/lower `q2`.  For cycles with disjoint owner and
colour banks, affected local deck cells are disjoint, so simultaneous
current is the sum of the two signatures.  Inverse-signature lookup is
therefore necessary and sufficient for zero typed current.  It returns
zero pairs in each of `C6+C6`, `C6+C8`, and `C8+C8`.

Target relevance does not omit a possible disjoint two-cycle repair.  A
new provider must use a newly inserted target-contained incidence.  A
cycle with none cannot change the target-local provider graph.  If only
one member were target-relevant, that member would already be a single
dual creator, which the exhaustive atlas excludes.

Because the inverse-signature banks are empty, phase, component action,
and residence are correctly reported as unreached gates.  The source does
not infer a phase obstruction from the absence of typed-current pairs.

## 4. Scope audit

The theorem is deliberately limited to the current candidate-5 `m=9`
factor and to native `C6/C8` single cycles or commuting owner-and-colour-
disjoint pairs.  Its conclusion does not cover overlapping sequential
switches, `C10` or longer cycles, triples, or cut-open packets.  Section 4
of the source lists the extra obligations for a marked collar and does not
claim they have been met.

## 5. H100 provenance

Enumeration, replay, compilation, and SHA-256 hashing were executed only
on H100 host `arboghast`.  The Mac was used only for reading, editing, and
Git operations.

Binding SHA-256 values:

```text
ba19b6dec78151aa66438b41a11ee3dd5a6928fd3b414527bf3b785050a716f9  source note
7efb5446fe84003e6d9d20b79eb64c735c621698e2f18b8050d9336e77b968a4  exhaustive search/verifier
e68597a12bebff83bb52f8573c1728782a90b155097b0f5431f46ec1a6270d66  compact hostile assertion replay
a829b2dc36560dcd984e2d12d2b158882eaad269d3cd4be142c4406f229f69d8  compact H100 output
```
