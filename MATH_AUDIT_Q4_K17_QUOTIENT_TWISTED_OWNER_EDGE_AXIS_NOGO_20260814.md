# Hostile audit of the q4 k17 quotient-twisted owner edge-axis no-go

**Date:** 2026-08-14
**Verdict:** **PASS** for the stated dihedral edge-axis class.  The theorem
does not classify nondihedral quotient-self columns.

**Audited source:**
`MATH_OBSTRUCTION_Q4_K17_NO_QUOTIENT_TWISTED_OWNER_EDGE_AXIS_PERIOD10_COLUMN_20260814.md`

## 1. Normalization audit

A five-subset of `Z_17` has no nontrivial translation stabilizer, so one
canonical core per translation orbit gives exactly `6188/17=364` cores.
Rotating start indices conjugates `i -> a-i` to `i -> a-2k-i`; every odd
`a` can therefore be normalized to `1`.  Odd axes have no fixed vertices
and fix the two cycle edges `(0,1)` and `(5,6)`.

For that normalized action, the adjacent owner pairs depend exactly on
the five-label words `s0..s4` and `s5..s9`.  The equality of canonical
owner representatives in the boundary equation is equivalent to allowing
an arbitrary translating lift for that pair.  Requiring the two words to
be disjoint is exactly support-label simplicity.  Hence the boundary-pair
enumeration is complete for the theorem's class; it does not assume a
common reflection centre.

## 2. Independent count audit

The search and hostile replay are separate implementations.  Both rebuild
the canonical core list and owner necklaces.  They agree on

```text
188160 boundary words,
2115072 disjoint boundary pairs,
173440 owner-nonsimple pairs,
1941632 quotient-simple pairs.
```

The replay directly asserts the already-forced `(0,1)` and `(5,6)` owner
relations, then records the three remaining relation bits.  The only
patterns are

```text
000:1940480, 001:384, 010:384, 100:384.
```

These sum to `1941632`; `111` is absent.  Thus no quotient-simple candidate
has the normalized edge-axis action.

The primary search also ran the more restrictive seed in which the two
combinatorial fixed owner edges were required to be fixed lower
bracelets.  That catalogue was empty as well, but the theorem correctly
uses the stronger owner-only no-go and does not depend on lower-edge
alignment.

## 3. Scope audit

The proof allows a different translation in every owner relation.  It is
strictly stronger than the frozen global-lift obstruction on this action
class.  Conversely, it assumes the induced owner permutation is a
dihedral edge axis.  With row-dependent translations a quotient-self
column could induce a nondihedral involution, so the source correctly
leaves the full quotient-self fixed-row signature classification open.

The consequence for the joint reflection master is correspondingly
scoped: the hoped-for edge-axis `(0 fixed owner,2 fixed lower)` family is
impossible, but no universal lower-ticket obstruction is claimed.

## 4. H100 provenance

All substantive enumeration, replay, compilation, and hashes ran on H100
host `arboghast`; the Mac was used only for reading, editing, transfer, and
Git.

Binding SHA-256 values:

```text
4974a23ec14e3088a50f09908f1a6d2281f4173fa6585659f9c4533b401bcf84  source note
3ca0f39cfb4bf0111a77057ed17c8f07692cd2e77a9cba8aa6465d3b70743c78  primary enumeration
f6a7ed39a8f1dbd520167b3ac3b602d7dfe925027aaa4914be7212ca11bb14d4  primary H100 output
bfd78b519efb4772e7a0562f7581a93be0f0ba95f82de26c3e8b3d86e6566d1e  independent replay
9c4de299e8f71374b16630c2cba458341ba4d71104aa5c082682d85aff3470b9  independent H100 output
```
