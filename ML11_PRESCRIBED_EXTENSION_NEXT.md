# The prescribed `ML_11` path-extension gate is SAT

## 1. Exact result

Let `H` be the 37-vertex alternating path obtained from the nineteen
rank-six triple masks in `k11_partial_switch_prefix_q19.txt` by inserting the
eighteen consecutive rank-five intersections.  Explicitly, `H` is stored in
`k11_ml_prescribed_path_q19.txt`.

There is a Hamilton cycle of the eleven-dimensional middle-levels graph
`ML_11` which contains `H` as a consecutive oriented subpath.

A complete certificate is stored in
`k11_ml_prescribed_cycle_q19.txt`.  It contains all 924 vertices of ranks five
and six exactly once, in cyclic order.  Direct independent verification gives

```text
PASS ML_11 Hamilton cycle vertices=924 edges=924 prescribed_vertices=37
prescribed_edges=36 cut369_rank6=369 cut93_rank6=93
cuts_outside_prefix=yes disjoint_from_prefix=yes direction=-1
cut_colours=188,171
```

Thus the precise graph-theoretic gate in Section 9 of
`K11_PORTAL_EMBEDDING_MATH_NEXT.md` is closed positively.

This is **not** a length-465 OR array.  In particular, the certificate by
itself imposes neither the mixed-delay coordinate-run conditions nor the
lower pinning and upper-shadow conditions.

## 2. Alternating-perfect-matching construction

The completion has a smaller formulation than a general Hamilton-cycle SAT
instance.

Colour the 36 edges of the prescribed alternating path alternately red and
blue.  Each colour is a matching: at every internal path vertex the two path
edges have opposite colours.  Complete the red forced matching to a perfect
matching `M_0` of the rank-five/rank-six incidence graph.  Complete the blue
forced matching to a perfect matching `M_1`, forbidding every edge of `M_0`.

The simple graph

\[
                 M_0\mathbin\cup M_1
\]

has degree two at every vertex.  It is therefore a disjoint union of even
cycles.  If it has one component, it is the desired Hamilton cycle, and all
prescribed edges remain present.

`ml11_prescribed_matching_search.cpp` implements exactly this construction.
It uses randomized augmenting paths only to choose the two perfect matchings;
the output certificate is checked independently and does not rely on any
probabilistic assertion.  With seed `77124`, the first pair of completed
matchings already has one component of size 924:

```text
trial=1 cycles=1 924
SAT trial=1
```

The result is deterministic for this compiler/source/seed combination; a
fresh rerun reproduced the certificate byte for byte.

## 3. Why the required `369/93` cut exists outside the prefix

The prescribed path contains nineteen rank-six vertices.  Deleting its
interior from the Hamilton cycle leaves one complementary cyclic arc with
443 rank-six vertices.

Starting immediately after the last prescribed vertex in the completion
direction, take the next 93 rank-six vertices.  This gives the lower-facing
path `Q`, and it is disjoint from the prescribed block.  The complementary
rank-six arc `P` has 369 vertices and contains the whole prescribed block.
The two rank-five vertices at the cuts are, for the displayed certificate,

\[
                         188,\qquad171.
\]

Both lie outside the prescribed path.  The 368 internal rank-five colours of
`P`, the 92 internal colours of `Q`, and these two cut colours are exactly all
462 rank-five masks, because they are precisely the rank-five vertices of the
Hamilton cycle.

This proves the full `368+92+2=462` rank-five ledger required by the cut-cycle
construction.

## 4. Independent verifier

`ml11_prescribed_extension_verify.cpp` checks from the raw files that:

1. the path has 37 vertices and the cycle has 924 vertices;
2. the cycle is exactly the union of the rank-five and rank-six layers;
3. every cyclic neighboring pair is an inclusion edge differing in one bit;
4. the prescribed path occurs consecutively, in one of the two orientations;
5. the selected 93-rank-six cut arc avoids all nineteen prescribed rank-six
   vertices; and
6. both cut colours are distinct rank-five vertices outside the prescribed
   path.

Reproduction:

```bash
g++ -O3 -std=c++20 ml11_prescribed_matching_search.cpp -o ml11_match
g++ -O3 -std=c++20 ml11_prescribed_extension_verify.cpp -o ml11_verify

./ml11_match k11_ml_prescribed_path_q19.txt 1 77124 \
  > reproduced_cycle.txt
cmp reproduced_cycle.txt k11_ml_prescribed_cycle_q19.txt
./ml11_verify k11_ml_prescribed_path_q19.txt \
  k11_ml_prescribed_cycle_q19.txt
```

An independent exact alternative is also available.  When
`MIDDLE_FORCE_PATH` names the alternating-path file,
`middle_levels_sat.cpp` adds the 36 corresponding unit edge clauses to its
degree-two 2-factor encoding.  Its existing lazy component cuts then demand
one Hamilton cycle.  The perfect-matching certificate makes running that
larger encoding unnecessary for existence, but the branch is useful for
adding future shadow or run constraints.

## 5. Certificate hashes

The frozen primary files have SHA-256 hashes:

```text
fe4b03bc40bae4c6cf0435f2b30c610c453c02c3288c319a9b0361952c707a41  k11_ml_prescribed_path_q19.txt
15afd3798debafdc08dcec42e7c3d0e79c44f54d3f4d29ca4d6f27b41905c0d2  k11_ml_prescribed_cycle_q19.txt
600d5e2adff0393c7d1da659b8a3d4491310e466e374cad9f15c57cf02eb0a88  ml11_prescribed_matching_search.cpp
```

The verifier and the optional SAT source should be rehashed after any later
audit edits.

An independent implementation audit is recorded in
`ML11_PRESCRIBED_EXTENSION_INDEPENDENT_AUDIT.md`, SHA-256

```text
86bd033bf29af424b62171ce01396ebabccaa1ddeaaba9c4a46fda5050849a85
```

It independently recomputes the complete cycle, path, cut, matching, and
bounded-score certificates rather than trusting the constructor's checks.

## 6. Exact scope

The new certificate proves:

\[
\boxed{\text{the explicit 37-vertex path extends to an `ML_11` Hamilton cycle}.}
\]

It does not prove that this particular completion can be ordered and cut so
that its rank-six row is mixed-delay factorable.  It also does not certify
all lower short-window ORs, coordinate pins, or longer upper unions.  Those
are the remaining OR-specific gates and must be tested or constructed on top
of this now-complete central ledger.

## 7. Exhaustive mixed-delay cut audit of this cycle

The Hamilton certificate does not accidentally solve the factorability gate.
`ml11_mixed_cut_analyze.cpp` exhaustively checks both cyclic orientations and
every placement of a 93-rank-six `Q` arc which avoids all nineteen prescribed
rank-six vertices.  There are exactly

\[
                      2(443-93+1)=702
\]

such oriented cuts.

For each cut it writes the rank-six target row as the 369 vertices of `P`
followed by the 93 vertices of `Q`, and applies the exact one-switch run
criterion with short-count 369.  A run contributes `required-length` to the
reported deficit.  The result is

```text
valid_q_arcs=702 factorable=0
best deficit=111 violations=98 start_mask=374 direction=-1
best_P_first=374 best_P_last=1212 best_Q_first=1268 best_Q_last=822
```

There are precisely two schedules whose `P` row begins with the prescribed
nineteen vertices, one in each orientation:

```text
prefix_at_P_start direction=-1 reversed=0 deficit=112 violations=97
prefix_at_P_start direction=1  reversed=1 deficit=119 violations=100
```

Thus the orientation retaining the certified prefix order is close to the
best cut of this particular cycle, but is not factorable.  Merely moving the
369/93 cut cannot repair it.

For completeness, treating the same rank-six order as the original `q=19`
switch gives

```text
q19_prefix_order deficit=239 violations=154
fixed_boundary_containment=0 fixed_boundary_initial_runs=0
D_first=252,1244,1238,1254
```

So it also fails both exact boundary tests imposed by the fixed factor tail
`4,32,514`.  This is a negative statement only about the displayed arbitrary
perfect-matching completion.  It is not an obstruction to another Hamilton
cycle containing the same prescribed path; future matching/SAT searches may
add the mixed-run and boundary constraints directly.
