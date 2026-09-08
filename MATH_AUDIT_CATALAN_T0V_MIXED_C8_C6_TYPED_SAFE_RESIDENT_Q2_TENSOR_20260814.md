# Hostile audit of the mixed `C8+C6` Catalan `T0V` tensor

**Date:** 2026-08-14  
**Verdict:** **PASS**, with the source's explicit scope: literal typed support
through `q2`, six-to-one lifted topology, and an internal phase-clock collar
through three owner blocks.  The span-four backup and contracted thirteen-
port realization remain open and are not smuggled into the theorem.

**Audited source:**
`MATH_THEOREM_CATALAN_T0V_MIXED_C8_C6_TYPED_SAFE_RESIDENT_Q2_TENSOR_AND_Q3_GATE_20260814.md`

## 1. Literal packet and resource audit

The four old `C8` incidences and three old `C6` incidences occur in the
canonical semilength-six factor.  Their seven complementary incidences do
not.  The circuits have disjoint owner sets and share exactly one colour,

```text
100011010111.
```

They share no incidence.  Toggling both therefore preserves every owner
degree and every colour degree.  Direct replay of final colour endpoints
and final owner colours gives

```text
owner current       0
upper-q1 current    0
lower-q2 current    0
lower-q1 current    4 positive / 4 negative
upper-q2 current    3 positive / 3 negative.
```

The four negative lower loads and three negative upper loads are all two.
This checks the central claim that the mixed packet, unlike the frozen
two-`C6` relay, is lower-typed-safe.

The target-directed atlas contains fourteen `C8` creators.  None is safe on
both lower `q1` and upper `q2`.  Of 11,418 owner-disjoint target-directed
`C8+C6` pairs, exactly one is safe on all five typed decks.  Its literal
data agree with Section 1 of the source.

## 2. The endpoint seam is necessary and correctly included

The most likely tensoring error was to copy the semilength-six current
without noticing that

```text
C = 000011010111
```

is a path endpoint only when the suffix is empty.  For nonempty `V`, its
untouched suffix-side colour is present.  Full-factor replay gives exactly
the additional current

```text
+000011110111[g(V)] - 100011010111[g(V)].
```

Thus a nonempty suffix has four, not three, positive and negative upper-q2
rows per packet.  The source states this distinction correctly.

The exact `Gamma` inverse test verifies the two advertised providers of the
negative seam row.  If `k(V)` is the coordinate raised by `g` and `ell(V)`
the coordinate lowered by the following `h`, the inverse pairs are

```text
(1,12+k(V)), (11,12+ell(V)).
```

They are distinct.  Exhaustive H100 replays through suffix semilength three
list loads two or three and recover these pairs exactly.  The proof is
symbolic: the fixed prefix-height substitution plus the defining touching-
step ordinals verifies all four conditions of the exact inverse theorem.

Because `g^{-1}=h'`, the seam suffix signature is injective.  Fixed prefix
bits distinguish seam rows from body rows.  No cross-`V` or seam/body
collision is hidden.

## 3. Full tensor and topology audit

For `m=6,7,8,9`, the independent tensor verifier reconstructs the complete
canonical factor, toggles every Dyck-suffix packet, and recomputes all five
occurrence decks.  Every run has:

* zero owner, upper-`q1`, and lower-`q2` current;
* four lower gains and four lower losses per suffix;
* three upper gains/losses for the empty suffix and four per nonempty
  suffix;
* zero support casualties; and
* pairwise-disjoint owner, colour and incidence packet supports.

The fixed odd lift is rebuilt independently.  Both projected rank shores
have exactly

```text
Cat_m - 5 Cat_(m-6)
```

components.  The endpoint trace identifies the six root prefixes printed
in the theorem and one affected closure component.  Hence the claim is a
six-to-one component merge, not merely a numerical decrement that could
hide one merge and one split.

## 4. Phase-clock and residence scope

The union of old and new owner adjacencies is bipartite in every complete
tensor replay.  The base endpoint trace forces the root-sign vector

```text
(-,+,-,+,-,+)
```

up to global reversal.  Exhausting all old component directions against
the two physically legal new directions gives:

```text
two-block signature loss       0
span <= 3 stratified loss      0
span 4 stratified loss         1.
```

The unique lost base union is `110111001111`, witnessed by the four owners
printed in the source.  There is no new interval of any span with that
union.  Clock-depth replays for `h=2,...,8` give losses

```text
5,7,9,11,13,15,17,
```

which are exactly `2h+1`.  The source's endpoint-offset proof explains the
entire sequence and does not infer an all-width theorem from finite data.

The positive residence statement is correspondingly limited to internal
intervals meeting at most three owner blocks.  This covers the owner,
`q1`, and immediate-upper `q2` rows in scope.  It does not cover a
z-present return, the final lifted closure, or the span-four row.

## 5. `C6`-only obstruction audit

The exact model has one Boolean variable for each of the 826 initially
alternating unoriented native `C6` supports.  Owner packing enforces
simultaneous owner-disjointness.  Shared colours are allowed: every
potential owner-colour incidence is modeled after all selected toggles,
and a Boolean pair variable identifies the literal final two endpoints of
each colour.  Therefore lower-`q1` support is checked on the final factor,
not by an invalid additive approximation when colours are shared.

With creation of `T0` and preservation of every old lower-`q1`, upper-`q2`
and lower-`q2` value imposed, CP-SAT returns `INFEASIBLE`.  The theorem
correctly limits the no-go to owner-disjoint simultaneous banks of initially
alternating native `C6`s.

## 6. Thirteen-port scope audit

The source does not claim that the native thirteen-port theorem survives
six-root contraction.  It records the missing data explicitly:

* one global sign bit per contracted block;
* the forced six-role relative sign vector;
* literal survival of a complete source block at the chosen terminal role;
* the multiway common-history test;
* transitive history consistency and separated starts; and
* quotient connectivity.

This is the correct gate.  An untouched reverse owner-path stem is not
silently identified with a canonical tight-source port, and the native
`13>12` pigeonhole margin is not reused after adding packet exclusions.

## 7. Reproducibility

All substantive runs and all hashes were performed on H100.  The frozen
outputs are:

```text
scratch/search_msw_t0_c8_c6_typed_safe_20260814.h100.out
scratch/solve_msw_t0_typed_safe_c6_bank_shared_colours_20260814.h100.out
scratch/audit_msw_t0v_mixed_c8_c6_tensor_20260814.h100.out
scratch/audit_msw_t0v_mixed_seam_providers_20260814.h100.out
scratch/audit_msw_t0_mixed_c8_c6_phase_clock_20260814.h100.out.
```

The final H100 SHA-256 digests are:

| artifact | SHA-256 |
|---|---|
| theorem | `f3ea40b7ae77a35bd0b764ac27b17336b665fe0d66818c293d442ed1a770e7bd` |
| target `C8+C6` atlas verifier | `321bef8aeb125e1bc22ce83b8759de932ea86b31cc3a9b48e9753509994b9c5e` |
| atlas output | `1d6af9108653ae9025bdbd355d68493cf6e9e0902865614838706f7d6585615e` |
| exact shared-colour `C6` no-go verifier | `295f840e491d321ee079facd4e882e8c10e73c64e8b56b523e8d28e39349d6ab` |
| no-go output | `82427e37dce436c24e27be35a386f2c7eee9a31d5f207f40ade215f9fbc8a90e` |
| full tensor verifier | `108713915f26cf46efb71740f9b1c391d0beed244a9069a109df298baff0e09c` |
| full tensor output | `c92fa7235e085654e310426cbdcded0be061b9b109495adb870ed8525e48cad9` |
| seam-provider verifier | `44b0a0391aee5fef46c5f778b7afef5afd4a8c702b2a24d594efb4a7a945c025` |
| seam-provider output | `38b6bb887d3663c0bbcf641840486c0c408f9edfbd70e0f17042eaff9f70eac4` |
| phase-clock verifier | `307c6131c8c1ecc9732606aba873a5f0268cc24bc6dd6fed307860fb224bf1fe` |
| phase-clock output | `2da24a5ce8ca6d718870ed218eb2671f81a53d6a01dea8d35590dc9abedd4ab0` |

The audit file's own digest is reported externally to avoid a
self-referential hash.
