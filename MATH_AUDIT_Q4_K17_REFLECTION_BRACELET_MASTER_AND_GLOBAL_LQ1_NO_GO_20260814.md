# Hostile audit: q4 k17 reflection bracelet master and lower-q1 boundary

**Date:** 2026-08-14
**Verdict:** PASS for the exact strong owner-only reduction and the
globally lifted lower-`q1` obstruction.  The finite owner master remains
search-UNKNOWN.

## 1. Frozen source

```text
MATH_REDUCTION_Q4_K17_REFLECTION_BRACELET_OWNER_FACTOR_MASTER_20260814.md
SHA-256 1b0e7a661b206816eee3513221c6a22380526576377d17e9bf5106d2335314b8
```

## 2. Positive reduction audit

An affine reflection of `Z_17` has one fixed point and eight transposition
pairs.  Counting invariant rank-nine sets and dividing the 17 physical
representatives per necklace gives exactly `{8 choose 4}=70` fixed owner
necklaces.  The other 1,360 owner necklaces form 680 reflected pairs, so
the bracelet quotient has exactly 750 rows.

For a strong palindromic rail, reflection acts on support positions by
`i -> 9-i` and on four-window starts by `i -> 6-i`.  The only fixed starts
are 3 and 8.  Quotient simplicity excludes accidental coincidence of any
other paired starts, so each strong self column covers exactly two fixed
and eight nonfixed owner rows.  This forces 35 self columns and 54 disjoint
reflected column-pairs.  Row-by-row reflection then proves the stated
750-row exact-cover equivalence; translation development is free and gives
143 quotient columns, 2,431 rails, and all 24,310 physical owners.

The fixed starts project to two four-subsets of eight reflection-pairs
meeting in the two core pairs.  Their graph is the 36-regular
intersection-two graph on 70 vertices, with 1,260 edges.  The H100 catalogue
independently confirms that all 1,260 edges have quotient-simple strong
lifts, with the frozen degree range 76 through 128.

## 3. Typed obstruction audit

The rank-eight layer likewise has 70 fixed bracelets.  In a globally
lifted self rail the invariant odd core contains the reflection's unique
fixed ground label, so the disjoint ten-support is fixed-point-free.  Its
dihedral involution is therefore either a support edge-axis or the
half-turn; a support vertex-axis would fix two forbidden support labels.

For q4, a support edge-axis `j -> a-j` with odd `a` acts on owner starts by
`i -> a-3-i`, a vertex-axis with two fixed owners and zero fixed owner
edges.  The half-turn has zero fixed owners and zero fixed edges.
Immediate-lower tickets are the owner-cycle edges, so a globally lifted
self column covers no fixed rank-eight lower bracelet.  A nonself reflected
pair covers any fixed lower bracelet twice.  Exact lower-`q1` coverage is
therefore impossible in the globally lifted reflection face.

This obstruction does not apply to quotient-twisted self columns with
owner-dependent translating lifts, nor does it invalidate the owner-only
master.

## 4. Search and scope audit

The monolithic CP-SAT run and five fixed-perfect-matching faces all ended
UNKNOWN at their stated caps.  No SAT, UNSAT, or factor claim follows.
Likewise, the strong palindromic catalogue is not proved to classify every
quotient-self rail: quotient equality permits owner-dependent translations,
so a common affine lift needs an additional constant-lift or unique-cycle
lemma.  The source states both limitations explicitly.

The H100 source/output hashes in the audited reduction match the replayed
artifacts.  All enumeration, solving, replay, and hashing ran through SSH
on H100; the local Mac was used only for reading, editing, transfer, and
Git.
