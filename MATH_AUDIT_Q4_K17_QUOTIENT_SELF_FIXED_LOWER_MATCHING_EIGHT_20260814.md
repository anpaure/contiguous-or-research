# Hostile audit of the q4 k17 fixed-lower quotient-self matching-eight theorem

**Date:** 2026-08-14  
**Verdict:** **PASS** for the owner-simple, immediate-lower-simple period-ten
q4 class and the literal reflected-pair master stated in the source.  The
result does not obstruct a symmetry-broken owner factor or arbitrary
post-factor transports.

**Audited source:**
`MATH_OBSTRUCTION_Q4_K17_QUOTIENT_SELF_FIXED_LOWER_CATALOGUE_HAS_MATCHING_EIGHT_20260814.md`

## 1. Normalization audit

A fixed rank-eight translation necklace has a representative preserved by
an affine reflection.  Translating its centre to zero makes it four of the
eight nonzero `{+a,-a}` pairs, giving exactly 70 literal masks.  Any fixed
lower occurrence can be rotated to `L_0`; its five-core is a five-subset of
that eight-set, and its other three elements are precisely the active
support positions `1,2,3`.  Thus the 70-by-56 unreduced task list is
complete.

Multiplication by a nonzero residue commutes with negation and conjugates
translations to translations.  It preserves every property tested by the
theorem.  Modulo `+-1` it acts as the regular cyclic group of order eight
on the eight reflection pairs.  Burnside on weight-four subsets gives
`(70+2+2+6)/8=10`; the independently reconstructed orbit sizes are
`2,4,8,8,8,8,8,8,8,8`.  One representative per orbit therefore reduces
3,920 tasks to 560 without discarding a typed column.

## 2. Enumeration audit

After positions `0,...,4` are fixed, owner self-reflection forces the
reflected necklaces of both incident owners to occur among the ten owner
windows.  For any chosen physical target windows, a tail satisfies both
requirements exactly when its four position-membership classes have the
same sizes as the corresponding four label-membership classes.  The
primary enumerator assigns all bijections within those classes and
deduplicates literal tails.  This is an exact constraint join, not a
sampling or a dihedral ansatz.

The full reconstructed column is then tested directly.  The status counts

```text
3627836 owner-nonsimple
  11864 lower-nonsimple
69000100 owner-simple but not owner-self
       8 owner-self
```

sum to all `72,639,808` completed orders.  Lower-nonsimple orders are
correctly excluded from the theorem's admissible class because a repeated
positive lower ticket cannot occur in an exact lower ledger.  The primary
deduplication key is the unordered owner deck together with the unordered
lower deck; consequently the reported four are distinct owner/lower typed
columns, not a claim about all physical rails.

## 3. Independent witness and closure replay

The audit wrapper does not call the primary classifier.  It reconstructs
the owner and lower decks from every retained `(core,order)`, recomputes
their reflection permutations and rowwise translating lifts, and confirms
for all four representatives

```text
2 fixed owners, 2 fixed lowers,
nondihedral owner action,
non-reflection-closed lower deck,
nonconstant owner translation lift.
```

It independently rebuilds the ten multiplier orbits, develops all four
typed representatives by `Z_17^*`, and obtains 16 typed columns over eight
owner decks.  Every owner deck has exactly two lower-deck realizations and
the two are literal reflections.  Hence selecting both repeats the same
ten-owner deck.

The two fixed-row graphs are independently built on the complete 70-row
universes.  Each is eight disjoint edges plus 54 isolated vertices, so its
maximum matching is visibly and computationally eight.  The wrapper also
re-enumerates the complete frozen strong-self catalogue.  None of the eight
owner decks is among its 136,456 decks, none of the eight fixed-owner edges
is among its 1,260 distance-two edges, and none is in the sample-zero
35-edge matching.  The source therefore correctly calls the columns new
owner-master variables while stating that they do not augment the frozen
sample-zero face.

The wrapper normalizes fixed owner bracelets to four-subsets of the eight
reflection pairs and finds intersection size three on all eight new edges.
They are Johnson-distance-one edges, so their absence from the strong
distance-two graph is structural.  Removing their sixteen endpoints leaves
54 vertices and 756 strong edges.  Exact matching returns size 27 and emits
the stated 27-edge certificate; its union with the eight new edges is
directly checked to be a 35-edge perfect matching.  The positive new-face
proposition is therefore supported independently of the lower no-go.

## 4. Consequence audit

In the stated literal reflection architecture every nonself column is
selected with its reflected mate.  A fixed lower bracelet occurring in one
member occurs again in the mate, so such a pair contributes even fixed-row
load and cannot alone realize target load one.  Owner-self, lower-simple
columns with any fixed lower occurrence are exactly the complete catalogue
above.  Owner exactness permits at most one of the two lower realizations
above each owner deck, and their lower-edge graph reaches only 16 fixed
rows.  Thus at least 54 of the 70 target parities remain wrong.  This proves
the scoped joint reflection-master no-go.

A unit mixed C4 lower-ledger move toggles two rows, so 54 wrong parities
require at least 27 such moves.  With only the frozen strong-self family,
all 70 are wrong and the corresponding bound is 35.  The source correctly
does not extend this counting bound to larger atoms with more than two
lower-row toggles.

The theorem deliberately leaves open:

* symmetry-breaking selection not organized in literal reflected pairs;
* a non-reflection owner factor;
* mixed-C4 transport after the owner factor; and
* larger lower-ledger atoms.

No stronger no-go is inferred from the finite catalogue.

## 5. H100 provenance

All substantive enumeration, witness replay, strong-catalogue comparison,
matching, compilation, and hashing ran on H100.  The Mac was used only for
reading, editing, transfer, and Git.

Binding SHA-256 values:

```text
911702a6e5e70700fd8d8abc9c85061d0b8643c94cdbf3497e3c1e3552c17b38  source note
9502baaa308c3aaea04c2bbc2488ca94b9e03a13ff73092c56d2d3c3d7c533d0  primary enumerator
396a9abf338d4d5f9abdb4a2adb3d9bc2f652ffb6bf376d71e7f832fe5f5375b  primary H100 output
ab2bace023a9ede13238d03588a0e2661c98fa873180ee3ab79722f4955fda04  primary H100 timing
c9d27c4a99ed2eabe47759f14fa0bd3838333a51146baabbb7f9efa843b4321e  independent audit/closure replay
324bf271234eefede36081908c38e73e72272925e2a6b4df656cae1189fc5426  independent H100 output
b4afd2e4640be3af7cb6ebb821c010da131dd13a714caf6cae8dccefcb34a04c  independent H100 timing
```
