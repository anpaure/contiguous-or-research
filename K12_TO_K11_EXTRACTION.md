# Exact `k=12 -> k=11` extraction audit

This note separates full-word dimension maps from the useful central-row
extraction.  The source certificates are `k12_optimal_nonzero.txt` (926
entries) and `k12_central_path_full.txt` (the 924 rank-six central windows).

## 1. Full-word maps

If `phi:2^X -> 2^Y` is a surjective join homomorphism, applying `phi`
entrywise preserves every interval-OR witness.  Zero images may be deleted,
and consecutive equal nonzero images may be run-compressed.

Every surjective join map from a 12-atom Boolean cube to an 11-atom cube has,
after relabeling, the following form: eleven source atoms map to the eleven
target singletons and the remaining atom maps to an arbitrary mask `B`.
Indeed, a representation of a target singleton as a union forces one source
atom to have exactly that singleton as its image.

`scan_k12_join_quotients.cpp` exhausts all `12*2^11` such maps.  Automatic
zero deletion and run compression give a best length of 774, attained by
mapping source coordinate 11 to the full 11-bit mask.  Ten independent greedy
deletion orders reduce this to 585, still worse than the verified 508 upper
bound.  The previously audited literal restriction (keep only entries avoiding
one coordinate) has raw best length 641 and deletion-pruned best 583.  Thus no
ordinary quotient or restriction extracts a competitive full `k=11` word.

## 2. Section-shadow theorem

Let `Q` be a rank-`r` row on `Y union {z}`.  Form

* `Q^0`, the subsequence of terms avoiding `z`, and
* `Q^1`, the subsequence of terms containing `z`, with `z` erased.

Every consecutive-union witness whose target avoids `z` lies wholly in one
zero run, so it remains consecutive in `Q^0`.  Dually, every
consecutive-intersection witness whose target contains `z` lies wholly in one
one run, so after erasing `z` it remains a witness in `Q^1`.

If `Q` enumerates the complete rank-`r` layer in dimension `2r`, each section
has `binom(2r-1,r)` terms and enumerates its corresponding layer exactly once.
For the exact `k=12` row and `z=11`, the zero section therefore enumerates all
462 rank-six masks on eleven coordinates and inherits **all upper union
shadows through rank 11**.

## 3. Block-reconnection lemma

Split `Q^0` at every non-Johnson jump.  Each piece is a Johnson path.  Reorder
and independently reverse these pieces, joining them only when the two exposed
endpoints form a Johnson edge.  The result is again a Hamilton Johnson path.
Moreover every inherited upper-shadow witness survives: it was contained in
one original zero run, hence in one piece, and reversal preserves its union.

For coordinate 11 the zero section has 25 maximal pieces of lengths

```text
60,14,5,13,7,20,13,10,4,7,3,33,7,12,19,9,29,33,10,27,38,5,13,68,3.
```

Their oriented endpoint graph has a Hamilton ordering.  With zero-based piece
indices one certified ordering is

```text
21+ 4- 22+ 10+ 1+ 16+ 2- 14+ 9- 19+ 11+ 13- 24- 12-
7- 17+ 3- 20+ 5+ 0- 18+ 6+ 15+ 23- 8-
```

`repair_k12_section_blocks.cpp` constructs it.  The resulting path is
`k11_from_k12_upper_complete_path.txt`; its independent score is recorded in
`k11_from_k12_upper_complete_path.analysis`.

It has all 462 central vertices, all 461 Johnson adjacencies, and complete
ranks 7--11.  It misses only 3 rank-three, 18 rank-four, and 23 rank-five
lower shadows, and its delay-three run deficit is 92.  It is not yet a factor
or a universal OR word.

## 4. Sparse hybrid with the lower-complete seed

Take the union of the edges in the new upper-complete path and
`k11_lower956_upper549.txt`.  `analyze_path_union.cpp` certifies:

```text
real edges                         555   (versus 6930 in J(11,6))
shared by both paths               367
unique to upper-complete path       94
unique to lower-complete seed       94
connected components                 1
degree range                       2..4
distinct rank-5 intersection colors 461/462
distinct rank-7 union colors        330/330
```

Thus this 555-edge graph already contains support for both central colour
requirements.  It is an exact, mathematically derived search reduction, not a
heuristic edge sample.  A solution found inside it is a valid fixed-row
solution; UNSAT only rules out this sparse union.

The existing solver searches its canonical branch without source changes:

```sh
RECOMBINE_OUTPUT=k11_k12_sparse.path \
RECOMBINE_MIN_DISTANCE=18 \
RECOMBINE_PHASE_REPAIRS=k11_k12_sparse_phase.txt \
./recombine_paths_sat 11 6 \
  k11_from_k12_upper_complete_path.txt \
  k11_lower956_upper549.txt ordinc
```

The phase file safely inserts ten of the twelve missing rank-seven colours
while displacing only duplicated seed colours; it changes no clauses.

In a sparse graph the canonical omitted-colour/endpoint normalization is not
WLOG.  `recombine_paths_sat.cpp` now accepts `RECOMBINE_NO_CANONICAL=1` for an
exhaustive search of the entire 555-edge union:

```sh
RECOMBINE_NO_CANONICAL=1 \
RECOMBINE_OUTPUT=k11_k12_sparse_exhaustive.path \
RECOMBINE_MIN_DISTANCE=18 \
RECOMBINE_PHASE_REPAIRS=k11_k12_sparse_phase.txt \
./recombine_paths_sat 11 6 \
  k11_from_k12_upper_complete_path.txt \
  k11_lower956_upper549.txt ordinc
```

`ordinc` enforces a connected ordered Hamilton path, distinct rank-five edge
colours with an endpoint-accessible omitted colour, all rank-seven colours,
and lazily adds exactly the missing rank-3/rank-4/rank-8/rank-9 and forbidden
run constraints.  If it emits a path, the usual exact factor-label SAT and
independent OR verifiers are still required.

## 5. Why the literal inverse lift fails

A standard odd-to-even braid in coordinate `z` has a section-convex incidence
word: one block of 462 zeroes and one block of 462 ones.  After erasing `z`,
the one block is the adjacent-intersection row of the zero block plus its
omitted colour (with the appropriate orientation and endpoint seam).

The exact `k=12` path has no such coordinate.  Coordinate 11, by far the
closest, has 50 section transitions (26 zero runs and 25 one runs); the other
coordinates have 158--169 transitions.  Hence the exact `k=12` solution is
not the direct odd-to-even lift of any `k=11` row.  The block extraction above
is the strongest certified inverse information currently obtained from it.
