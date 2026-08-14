# Hostile audit of q4 k17 rank-seven mark necklaces and isolated schedules

**Date:** 2026-08-14
**Verdict:** **PASS after scope correction.**  The projected run criterion
is an iff only for unmarked type-ID allocation.  Literal boundary-state
compatibility and the six marked-type counts are supplied for the canonical
mask family by the separate fourteen-face certificates, not by the integer
criterion alone.

**Audited source:**
`MATH_THEOREM_Q4_K17_RANK7_MARK_NECKLACES_AND_ISOLATED_FACE_SCHEDULES_20260814.md`

## 1. Full binary-word audit

The analyser independently constructs the 72 labelled ordered partitions
and all 793 refresh arcs.  For each of all `2^10` and `2^11` directed
binary words it restricts each position to the correct marked/unmarked
state bank, propagates exact labelled successors, and checks the cyclic
wrap.  Retaining one path per tail is sound because the start is fixed
during each propagation and closure depends only on that tail and start.
It reports every word feasible.  Quotienting only by directed rotations
gives the standard counts 108 and 188; reversal is not used.

The state-count convention is consistent: types `0,3,6` contribute
`5+30+5=40` unmarked states, and the other types contribute 32 marked
states.

## 2. Run-language and integer-gate audit

For unmarked profiles, the refresh inclusions permit exactly

```text
0->6, 3->3, 3->6.
```

Type 6 has no unmarked successor; type 0 can only be followed by 6; type 3
can continue as 3 or terminate as 6.  This gives the run list in `(2.1)`.
An all-unmarked directed cycle can only use the `3->3` loop.

For nonconstant cycles let `x` length-two runs be `06`, `z` be `36`, and
let `q` long runs end in 6.  The residual singleton counts are exactly

```text
u0=139-x,
u6=127-x-z-q,
u3=a-266+2x+z+q.
```

The bounds in `(2.3)` are precisely nonnegativity of the selected run
numbers and these singleton counts.  Using
`h+a+2b+S=286`, the remaining number of type-3 positions simplifies to
20 automatically, with `h` of them in all-unmarked cycles.  Thus `h<=20`
and `(2.3)` are necessary and sufficient for the projected unmarked
type-ID allocation.

They are not sufficient for a compatible labelled-state lift across
marked boundaries or for the six marked-type counts.  The source now says
this explicitly.  This correction is essential; the independent canonical
certificates establish the stronger result only for their displayed mask
multisets.

The quick cuts are also sound.  Every unmarked-to-unmarked arc ends at a
type-3 or type-6 position, giving at most `20+127=147` such arcs.  Every
internal edge of a long run is sourced at a type-3 position, so the long-run
excess is at most `20-h`.

## 3. Fourteen-face certificate audit

For face `t`, the canonical construction has `143-t` cycles, puts two
unmarked positions on each, and puts one extra position on the first `2t`
cycles.  The total is `2(143-t)+2t=286`.  The cyclic gaps are `(3,7)` or
`(3,8)` for two-position masks and `(3,3,4)` or `(3,3,5)` for three-position
masks, so the claimed distance-three condition is literal.

The independent replay does not import the search code.  It reconstructs
all states/arcs, regenerates the canonical masks, verifies each state word,
cyclic wrap, mark bit, period count, mask hash, state-word hash, and the
complete nine-type vector on every face.  The certificate covers all 14
faces and 1,430 positions per face.

## 4. Pure-period-ten exact-cover audit

At `t=0` all 143 canonical masks are the same directed mask `{0,3}`.  A
solution of `(4.3)` chooses one phase on each physical rail, forbids
unmarked singleton-load positions, and covers every doubled orbit once.
There are 286 chosen positions and 286 doubled-orbit rows, so this is
exactly the desired marked/unmarked split.  A coefficient two correctly
rejects an option containing both occurrences of one doubled orbit.

The arbitrary bijection of certified state cycles to rails is valid:
permuting whole cycles and rotating each directed cycle preserve every
refresh arc and the global type census.  A separate bijection from the
abstract five-core to each rail core preserves the labelled transition
relation.  Because every binary mask is identical at `t=0`, the orbit
exact cover does not need to remember which literal state word was assigned
to which rail.  This proves both directions of Theorem 4.1 at the stated
rank-seven scope.

The argument does not settle later rank-two through rank-six payloads; the
source leaves those separate.

## 5. Generic 2-SAT audit

One Boolean per doubled orbit chooses exactly one of its two occurrences.
For every same-rail pair at cyclic distance one or two, the clause forbids
choosing both.  These clauses are necessary and sufficient for cyclic
three-separation.  With 286 isolated singleton runs, the projected run
criterion is automatically feasible (`a=286`, all other run variables
zero).

The source correctly does not promote raw 2-SAT feasibility to a full
nine-type schedule: a generic mask multiset still needs a canonical-mask
matching or a residual exact-census labelled-state refinement.

## 6. H100 provenance

All substantive enumeration, solving, replay, and hashing ran on H100;
the Mac was used only for reading, editing, transfer, and Git operations.
The committed source/output hashes listed in the theorem match the
replayed artifacts.

Binding theorem SHA-256:

```text
ae2c001768f69cae4a6822854d3a7dff3cffd796caca4eaaf4e01f4d4ba691b4
```

The six verifier/certificate hashes are reproduced verbatim in Section 7
of the theorem and were independently matched on H100 during this audit.
