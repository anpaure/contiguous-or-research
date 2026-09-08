# Optimal k18: initialized two-cycle construction and exact byte regeneration

Date: 2026-09-08. Independent proof and one bounded literal replay by
`exact_equality_structure`. Root read the complete checker, including
its final additional assertions, before authorizing its single execution.

**Result: PASS.** The supplied optimal 18-coordinate word is recovered
exactly from the already verified 17-coordinate word, one specified
coordinate permutation, and a uniquely identified phase of its recovered
long cycle. The actual initial recency state admits precisely 24,309
updates covering the full 17-cube, attaining the general lower bound
`lambda_17(P) >= W(17)-1`.

This is a reconstruction from the supplied 17-coordinate **literal word**.
The long cycle's phase is measured in the literal `R` recovered below.
It does not identify a phase in the user's unprovided canonical `P`, nor
regenerate either word from the unprovided quotient construction.

## 1. Inputs, definitions, and independently established prerequisites

The input is [the optimal 17-coordinate word](../answers/k17_optimal24313.word),
denoted `A`, of length 24,313 and SHA-256

`7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9`.

Its universality and exact optimality were established in
[the direct-forward and two-cycle certificate](K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md).
The supplied 18-coordinate input has length 48,623 and SHA-256

`6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5`.

It has separately passed the full-cube
[independent first-occurrence verifier](K18_OPTIMAL48623_INDEPENDENT_FIRST_OCCURRENCE_CERTIFICATE_20260908.md).
The present replay pins both hashes and establishes the construction's
internal structure independently of that full-cube census.

Masks use bits 0 through 16 for the old coordinates, and `z=131072` for
the new coordinate. Array indices in this note are zero-based unless a
table explicitly says otherwise. Recency blocks are ordered from most
recent to least recent. Updating a state by a letter means prepending
that letter, deleting its coordinates from all older blocks, and deleting
empty blocks. State prefix unions are exactly the distinct suffix ORs
of the physical history.

## 2. The endpoint replacement is legitimate

**Endpoint replacement lemma.** Suppose a word ends with consecutive
nonempty letters `P,L`. Replacing `L` by a nonempty `C` preserves the
last pair union if and only if

    L \ P ⊆ C ⊆ L ∪ P.                                  (2.1)

Under (2.1), every interval of length at least two has the same OR as
before: an affected interval contains the entire last pair, whose union
has not changed. Every unaffected singleton is also unchanged. Therefore,
if the old target `L` has a witness disjoint from the final position, a
universal word remains universal after the replacement.

The equivalence follows directly from `P ∪ C = P ∪ L`. This allows
coordinates of `P` to be added to `L`; it is more general than replacing
`L` by one of its subsets. When `P \ L` is nonempty, it is the old
second recency block, so the replacement changes those first two blocks
while preserving their union; an empty resulting block is removed.
If `P` is a subset of `L`, a replacement can instead split the old first
block and insert a second block. The universal-word argument above does
not require either recency special case.

Here the final two letters of `A` are `25249,689`. Replace its final
letter by `8881`. The checker establishes

    25249 | 689 = 25249 | 8881 = 25265,

and that the unchanged letter at index 87 is `689`. Thus the new left
word `A'` remains universal and still has optimal length 24,313.
Its exact body is saved as
[k17_optimal24313_tail8881.word](k18_optimal_initialized_structure_20260908/k17_optimal24313_tail8881.word),
with SHA-256

`275eb227c5bef8acc2b3b8e218a68c9c39bccf725d28431b2ef69ff100edfed9`.

The actual terminal state is

    P' = (8881 | 16384 | 2 | 1024 | 4 | 32768 |
          8 | 2048 | 4096 | 256 | 64 | 65536).             (2.2)

Its block-size profile is `(6,1,1,1,1,1,1,1,1,1,1,1)`.

## 3. Recovering the precise two-cycle continuation

Recover two literal cycles directly from `A`:

    Q = A[:85],             |Q| = 85,
    R = A[86:-2],           |R| = 24225.

The checker verifies the exact identity

    A = Q || Q[0] || R || R[:2].                         (3.1)

Let `S=reverse(R)` and `Qrev=reverse(Q)`. The supplied one-based
coordinate permutation is

    pi = (2,1,7,12,11,15,5,4,3,6,17,8,9,10,14,13,16).

Thus old coordinate `i` is mapped to coordinate `pi_i`.
The final 24,309 letters of the supplied 18-word all contain `z`.
After stripping `z` and undoing `pi`, they are exactly

    S[1428], S[1429], ..., S[1426] || Qrev,              (3.2)

where the first segment is read cyclically modulo 24,225 and has length
24,224. Equivalently, the long cycle is opened immediately after
`S[1427]=27202`, and that one initial letter is omitted from the update
sequence. A linear-time KMP lookup in `S||S` certifies that 1428 is the
unique possible start phase of this known 24,224-letter segment. No
phase search over other constructions was performed.

Let `D` be the complete rotation of `S` starting at index 1428. Then
`D[:-1]` is the long update segment and `D[-1]=S[1427]=27202`.
The complete construction is

    A' || {z} || (pi(D[:-1] || Qrev) with z added
                 to every letter).                    (3.3)

Its length is

    24313 + 1 + 24224 + 85 = 48623.

The checker builds (3.3) from `A`, the fixed replacement, the recovered
phase, and `pi`, serializes it as newline-separated decimal masks, and
asserts **byte equality** with the raw supplied 18-word. The regenerated
body is saved as
[k18_optimal48623_regenerated_from17.word](k18_optimal_initialized_structure_20260908/k18_optimal48623_regenerated_from17.word).

## 4. Why the omitted long-cycle letter costs no update

Undoing `pi` in the initializer (2.2) gives

    (27202 | 32 | 1 | 16 | 256 | 65536 |
     128 | 8 | 32768 | 4096 | 4 | 1024).                 (4.1)

This is exactly the periodic recency state of `S` immediately after its
omitted letter `S[1427]`. The checker establishes it by processing the
complete rotation `D` from the empty state. This produces the periodic
state because the union of a full period contains all 17 coordinates:
every coordinate's most recent occurrence is within that last period.

Consequently, the initial state followed by the 24,224 long updates
visits all 24,225 periodic endpoint states of `R`, once each. It exposes
the whole cyclic target family of that long cycle without spending an
update on the omitted position. The following 85 updates are the literal
linear word `Qrev`; all of its ordinary interval targets are therefore
available, regardless of earlier history.

Direct forward interval scans, independently of the recency recurrence,
give the exact target counts

    cyclic R:            130748,
    linear reverse Q:       633,
    union:               131064.                        (4.2)

The checker additionally compares the long-stage initialized prefix
family, after undoing `pi`, with the entire directly enumerated cyclic
`R` family. They are equal, including all ranks.

## 5. The seven targets supplied across the join

The last three unpermuted long-segment letters and first three short
letters are exactly

    10771, 8739, 26656 | 19106, 19076, 33444.             (5.1)

The seven targets missing from the union (4.2) and their ordinary
interval witnesses in this six-letter word are:

| Target | Rank | Local interval, one-based inclusive |
|---:|---:|:---:|
| 27298 | 7 | [3,4] |
| 27299 | 8 | [2,4] |
| 27302 | 8 | [3,5] |
| 27303 | 9 | [2,5] |
| 27315 | 9 | [1,4] |
| 27319 | 10 | [1,5] |
| 60070 | 9 | [3,6] |

The exact sorted hole list and all seven specified intervals are pinned
assertions in the checker. Each witness is also permuted, marked with
`z`, translated to its actual global indices in the 18-word, and checked
against an independent segment-tree range-OR implementation.
The full translations are recorded in
[the seven-target seam certificate](k18_optimal_initialized_structure_20260908/seven_target_initialized_join_certificate.json).

Equations (4.2) and (5.1) therefore prove that the initialized tour
contains all 131,071 nonempty old targets, including the targets supplied
only across the join. This uses actual ordinary intervals, not an
unaccounted cyclic wrap in the final word.

## 6. Exact initialized optimum and full 18-coordinate coverage

For a complete initial recency state `P`, let `lambda_17(P)` be the
least number of nonempty updates whose states, including the initial
state, expose every nonempty target. Every state has at most one
prefix of rank eight, so at least `W(17)=24310` states are necessary:

    lambda_17(P) >= 24309.                              (6.1)

The construction uses 24,309 updates and satisfies full coverage by
Sections 4–5. Hence

    lambda_17(P') = 24309 = W(17)-1.                     (6.2)

The replay also directly visits all 24,310 initialized states, checks
each state against physical last-occurrence timestamps, and verifies
that the rank-eight prefixes form a bijection onto all 24,310 rank-eight
targets. Independently, the rank-nine prefixes also form a bijection
onto all 24,310 old rank-nine targets.

The singleton bridge realizes `z` itself and marks every suffix target
of `A'`, giving the initial prefix deck with `z`. Each later initialized
prefix is the projection of a real suffix interval ending at a marked
letter. Thus every old target with `z` added is realized. All unmarked
targets remain in universal `A'`. This is the forward direction of the
separately audited
[exact initialized-extension identity](INITIALIZED_RECENCY_EXTENSION_INTERLEAVING_AND_K18_LOWER_BOUND_AUDIT_20260908.md),
`Ext_z(A')=1+lambda_17(P')`.

For an independent physical check, the replay stores one actual
18-coordinate interval witness for each of the 131,071 nonempty old
targets with `z` added and verifies every one by range OR. It separately
checks the bridge singleton. No abstract recency output is accepted as
a witness without this literal replay.

An additional full-word pass finds exactly 48,620 distinct rank-nine
suffix targets, all with multiplicity one. Precisely the first three
endpoints, indices `0,1,2`, lack a rank-nine suffix target. Thus the
actual critical rank saturates the endpoint budget exactly.

The independently proved lower bound `B(18)=48623` and this word give
`nu(18)=B(18)=48623`. The initialized number in (6.2) is not the ordinary
17-coordinate word length, which remains `nu(17)=24313`.

## 7. Execution, artifacts, and scope

The reviewed checker is
[reconstruct_k18_optimal_initialized_two_cycle_structure_20260908.py](reconstruct_k18_optimal_initialized_two_cycle_structure_20260908.py).
One execution on `h100`, hostname `arboghast`, completed with **PASS** in
1.221 seconds under 30 CPU seconds, 45 wall seconds, and 1 GiB address
space. There were no retries, construction searches, or local
mathematical executions. The unique phase lookup was linear-time matching
against the already specified long cycle.

The complete local bundle is
[k18_optimal_initialized_structure_20260908](k18_optimal_initialized_structure_20260908/),
including:

* [Full certificate](k18_optimal_initialized_structure_20260908/optimal18_initialized_structure_certificate.json).
* [All initialized recency states](k18_optimal_initialized_structure_20260908/initialized_recency_states.jsonl).
* [All 131,071 marked target witnesses](k18_optimal_initialized_structure_20260908/initialized_targets_actual18_witnesses.jsonl).
* Regenerated 18-word, modified 17-word, actual and unpermuted update
  sequences, recovered `Q` and `R`, and the seven-target seam certificate.

The remote bundle is
`/home/amodo/exact-b-k18-optimal-structure-20260908/artifacts/`.

The earlier negative one-seam test covered ten specific oriented
four-end trims of `A`, with arbitrary universal left words; its directed
cycles ruled those tails out regardless of the initializer's profile.
The present continuation instead opens a rotated **reversed recovered
long cycle** and appends the reversed short cycle, so it is outside that
tail family. Its enlarged endpoint is also outside the earlier subset-cap
family. Changing the initializer profile alone would not have bypassed
the stronger negative test for those ten fixed tails.

This proves the actual construction and the initialized optimum at its
specified state. It does not establish suitable initialized tours or
exact optimal words in all dimensions.
