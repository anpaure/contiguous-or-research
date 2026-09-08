# Independent audit of the partial-completion forest result

## Verdict

The two advertised completion certificates are valid.

```text
k=11: nonzero length 478,  coverage 2047/2047
k=14: nonzero length 3677, coverage 16383/16383
```

Consequently the proved bounds

```text
nu(11) <= 478,  N(11) <= 479,
nu(14) <= 3677, N(14) <= 3678
```

are correct.  I recomputed the missing sets from the partial words using both
exhaustive interval enumeration and an independently compiled suffix-OR
recurrence; I did not take the generator's reported counts as evidence.  I
also recompiled the generator, reproduced all six current `*_best` data files
byte for byte, and reran both independent full-word verifiers.  The new logs
are byte-identical to the stored logs.

The linear-forest lemma and auxiliary-bridge mechanism are sound.  They are
sufficient constructions, not characterizations or optimality results.  Two
documentation qualifications are recorded below: the bridge statement should
say that its two base vertices are distinct (implicit when the two targets are
distinct), and an older file named `k14_pinnable_factor_verification.txt`
certifies an earlier 16,093-mask factor rather than the current 16,123-mask
factor.  Neither point affects either completed certificate.

## 1. Mathematical construction

Let `F` be the masks still missing in a lower rank and `G` those still missing
in the next rank.  Put one physical vertex, labelled by its mask, into the
completion for every member of `F`.  Add any number of labelled auxiliary
vertices.  If one selects edges subject to

```text
maximum degree <= 2, and no cycle,
```

then the selected graph is a disjoint union of paths and isolated vertices.
Writing each path in path order and concatenating the components preserves
every selected edge as an adjacent pair.  Therefore every lower target is a
singleton, every upper target assigned to an edge is the OR of an adjacent
pair, and any remaining upper target can be appended literally.  Joins
between components can create extra OR values, but cannot invalidate an old
witness.  This proves the stated length

```text
|F| + number of auxiliary vertices + number of literal upper targets.
```

The shared bridge is also exact.  If distinct base vertices `P,Q` and a
nonzero label `X` obey

```text
P | X = U,
X | Q = V,
```

then the path `P,X,Q` represents both upper targets using one auxiliary
position.  In the unique-contained-base situation, set

```text
X = (U & ~P) | (V & ~Q).
```

It works exactly when this `X` is contained in both `U` and `V`: it already
contains the missing part of each target, while containment prevents an
outside bit from contaminating either OR.

The word "distinct" should be explicit in the abstract bridge lemma if base
vertices are counted only once.  For distinct targets it follows anyway: if
`P=Q`, the two displayed OR equations imply `U=V`.  The implementation also
rejects a repeated base because the second edge would close a cycle.  All six
base vertices used by the three `k=14` bridges are distinct.

## 2. Source audit

Audited source:

```text
bd5af38640511da6a740ac5eca5966801bec14be486e04823cce9ce512432eae  partial_completion_forest.cpp
```

### Post-audit diagnostic delta

The source changed once after the first audit snapshot.  Removing current
lines 332--340 produces SHA-256

```text
67694d6e139d01088453da3b223820aa15c69fecfef658edc773cd0f5fadc137
```

exactly, so the complete delta from the previously audited source is the one
new loop after `write_word` that prints one `shared_auxiliary=...` diagnostic
line per selected bridge.  The loop only copies two matching indices, computes
the already-used auxiliary label, and reads labels for `cout`.  It executes
after coverage validation and after both certificate files have been written;
it changes no graph, matching, word, or output file.

I freshly compiled SHA `bd5af386...` and reran both instances.  All six
generated missing/completion/completed files remain byte-identical to the
stored `*_best` files and retain the hashes listed below.  The only observable
change is that the `k=14` standard-output log now explicitly prints the three
bridges with auxiliary labels 288, 8196, and 48; `k=11` has no such line.
Thus the source delta has no construction or certificate semantics.

The source compiled cleanly as C++20 with `-O3 -Wall -Wextra -pedantic`.
Within the intended range `k<20`, its relevant operations are sound:

1. `covered_masks` maintains exactly the distinct ORs of suffixes ending at
   the current position, so its union over positions is precisely the set of
   all interval ORs.
2. Missing masks are divided into the requested two adjacent ranks, and any
   other missing rank causes rejection.
3. For each upper target, every candidate direct edge consists of two missing
   lower masks contained in that target whose OR equals the target.
4. `choose_forest` adds a candidate only when both degrees stay at most two
   and its endpoints are currently disconnected.  Thus it preserves
   acyclicity and the degree bound.  Its rollback is balanced.
5. The singleton-upper matching adds `base-X-base` bridge paths.  The
   compatibility test is exactly `X subset U` and `X subset V`, and the same
   degree/cycle tests are applied to both bridge edges.
6. `linearize_forest` is complete for the graph produced: every nontrivial
   acyclic degree-two component has endpoints, and isolated vertices are also
   visited.
7. The source finally recomputes coverage of the concatenated word before it
   writes a successful certificate.

I found no implementation bug affecting the two instances.

The program is deliberately not a complete optimizer.  In particular, it
requires every upper target with a candidate lower-pair edge to be embedded
as an edge; if no simultaneous forest exists it aborts instead of falling
back to a literal.  It also does not search tradeoffs in which literalizing
one such target permits more auxiliary bridges elsewhere.  Thus its success
proves the emitted upper bound, but failure would prove nothing and success
does not prove shortest completion.  `PARTIAL_COMPLETION_FOREST.md` correctly
labels the method sufficient and makes no `k=14` optimality claim.

Fresh runs on the two base factors regenerated the current missing,
completion, and combined files byte for byte.  Their summaries were

```text
k=11: partial=465, lower=12, upper=1,
      direct=0, bridges=0, literals=1,
      completion=13, completed=478.

k=14: partial=3434, lower=238, upper=22,
      direct=14, bridges=3, literals=2,
      completion=243, completed=3677.
```

## 3. Independent `k=11` recomputation

The first 465 entries of `k11_completed_best.txt` are, as a sequence, exactly
`k11_upper549_natural_array.txt`; its final 13 entries are exactly
`k11_completion_best.txt`.

I independently enumerated all `465*466/2 = 108345` intervals of the partial
word and separately ran the distinct-suffix recurrence.  The two coverage
bitsets agree.  They contain 2,034 of the 2,047 nonzero masks, with exactly

```text
rank 7 (12 masks):
251 493 607 941 956 1267 1468 1694 1763 1884 1946 1990

rank 8 (1 mask):
958
```

missing.  The independently emitted sorted `(mask,rank)` stream is byte-equal
to `k11_missing_best.txt`.

The 13-entry completion consists of the twelve missing rank-seven masks and
958, each literally.  It therefore covers all thirteen omissions internally,
without relying on a seam-crossing interval.  The combined 478-entry word
contains only values in `[1,2047]` and both full verifiers report all 2,047
nonzero masks.

The claimed optimality of length 13 for an **isolated completion gadget** is
also correct.  Twelve same-rank targets are an antichain.  If a 12-position
word covered all twelve, chosen witnesses for them would be pairwise
nonnested.  Their twelve left endpoints and twelve right endpoints would each
have to be all positions `1,...,12`; after sorting, every witness would be the
corresponding singleton.  Hence the entries would be precisely the twelve
rank-seven omissions.  Only 956 is contained in 958, so no interval of those
entries can OR to 958.  A thirteenth entry is necessary.

This does **not** prove that every suffix appended to the fixed 465-entry
prefix needs 13 new positions, because a shorter repair might use witnesses
crossing the old/new seam.  The main result explicitly states this caveat.

## 4. Independent `k=14` recomputation

The first 3,434 entries of `k14_completed_best.txt` are, as a sequence,
exactly `k14_pinnable_factor_missing260.txt`; its final 243 entries are exactly
`k14_completion_best.txt`.

Exhaustive enumeration of all `3434*3435/2 = 5897895` intervals and the
independent suffix recurrence produce the same coverage bitset.  The partial
word covers 16,123 of 16,383 nonzero masks.  Its exact omissions are

```text
238 masks of rank 9,
 22 masks of rank 10,
260 masks total.
```

The independently generated sorted missing stream is byte-equal to
`k14_missing_best.txt`.  Recomputing containment and pair-OR possibilities
for the 22 upper targets gives

```text
14 targets with at least one lower-lower OR edge (33 candidate edges total),
 7 targets containing exactly one missing lower mask,
 1 target containing no missing lower mask.
```

The 243 completion entries have the following exact composition:

```text
238 rank-nine lower targets,
  3 rank-two auxiliary labels (288, 8196, 48),
  2 rank-ten literal targets (15346, 8015).
```

Independent enumeration of the completion alone shows that all 260 original
omissions occur internally with shortest witnesses

```text
238 rank-nine targets at length 1,
  2 rank-ten targets at length 1,
 20 rank-ten targets at length 2.
```

The three asserted bridge triples occur consecutively (possibly reversed) at
one-based starts 40, 61, and 152 in the completion:

```text
6093, 8196, 13283
7420,  288, 15302
13423,  48, 13725
```

and direct arithmetic gives

```text
7420  | 288  = 7676,   15302 | 288  = 15334,
13283 | 8196 = 13287,  6093  | 8196 = 14285,
13423 | 48   = 13439,  13725 | 48   = 13757.
```

Thus 14 upper masks use direct lower-lower edges, six use the three bridge
vertices, and two are literal.  Relative to appending all 260 omissions, the
14 direct edges save 14 positions and the three shared bridges save three
more, giving

```text
260 - 14 - 3 = 243.
```

The complete 3,677-entry word has `3677*3678/2 = 6762003` intervals.  Fresh
exhaustive enumeration covers every one of the 16,383 required nonzero masks;
the suffix recurrence independently gives the same result.

For artifact clarity, `k14_completion.txt` and `k14_completed.txt` are the
earlier valid 246-entry completion and 3,680-entry combined word.  Independent
exhaustive and suffix checks also pass for that word.  The `*_best` files are
the improved bridge version and are the ones supporting length 3,677.

## 5. Verifier-log and hash audit

I freshly compiled the two verifier sources.  `verify_or_array.cpp` directly
enumerates every physical interval; `verify_or_suffix.cpp` uses the distinct
suffix-OR recurrence.  These are genuinely different coverage algorithms.
All four new outputs were byte-identical to the stored logs, including the
following SHA-256 values:

```text
f7d6936c7b619cdb184a2e230621600b542c3bfbabe075f8dc772cf3aea71936  k11_completed_best_exhaustive.log
e73ca5095eb735ff2059366fb573b223f8c3884bc48b1465094a540a251574c3  k11_completed_best_suffix.log
180074fdc468b4fde2bb6ca5c346c420ab3186ccc9ccd1d327857c1e32e36828  k14_completed_best_exhaustive.log
74d4f71ba91f72c76ddf76378ae1652b3b1384e7964ad15bc2636e19f83d3450  k14_completed_best_suffix.log
```

The principal data hashes also recompute as

```text
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd  k11_upper549_natural_array.txt
e4aefd4c6c229218726965d4f43d213125504d3a7f013edc8e2d3c8325a9afea  k11_missing_best.txt
4fe62fe733265ab099d2630f6a4a73c842635f4db07c4699953e0d3d0f796a2f  k11_completion_best.txt
6ac47bbb36a6b416164cd1730a450106fadddd0cd2eee2d429fe5ea4d31ae439  k11_completed_best.txt

4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad  k14_pinnable_factor_missing260.txt
152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab  k14_missing_best.txt
06f4b5a06f411a896df9d471b4e2f60d97eea537b4c81710f5e1c62117d68b19  k14_completion_best.txt
d5fc5c13685ca0e2eb182de0d245e93368453d0aaeaf6e2f5cfdff219a59c83c  k14_completed_best.txt
```

There is one stale but nonfatal artifact-name trap:
`k14_pinnable_factor_verification.txt` reports `covered=16093`, and its hash is

```text
90b78d7c28fcbe56b4fdabf2336d847b44ec55e9d865469b1946b02a06e499cc
```

so it belongs to an earlier 290-omission factor, not the current
`k14_pinnable_factor_missing260.txt`.  It should not be cited as the verifier
for the current partial word.  This does not weaken the result: I recomputed
the current 260-mask missing set independently, and both stored completed-word
logs are current and reproduce exactly.

## 6. Final audit conclusion

The new forest-completion contribution is a certified improvement, not an
exact solution of either unresolved dimension:

```text
465 <= nu(11) <= 478,
3434 <= nu(14) <= 3677.
```

The files prove the upper endpoints.  No claim here shows that 478 or 3,677
is shortest, and no generator failure would be a lower-bound certificate.
With those scope limits, the mathematical proof, implementation, artifact
counts, hashes, and universality claims all pass independent audit.
