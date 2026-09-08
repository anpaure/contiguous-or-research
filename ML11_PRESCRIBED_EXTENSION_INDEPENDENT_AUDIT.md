# Independent audit of the prescribed `ML_11` extension certificate

## Verdict

**PASS**, for the following exact graph-theoretic statement:

> The 37-vertex alternating path in
> `k11_ml_prescribed_path_q19.txt` occurs consecutively in a Hamilton cycle
> of the rank-five/rank-six incidence graph on `[11]`.  The cycle admits a
> cut whose short arc has 93 rank-six vertices and is disjoint from the
> nineteen prescribed rank-six vertices; the complementary arc has 369
> rank-six vertices and contains all nineteen prescribed ones.

This audit does **not** certify a length-465 OR array.  The certificate says
nothing by itself about mixed-delay factorability, short-window labels,
coordinate pin survival, or the longer upper OR shadows.

## 1. Independent certificate recomputation

I wrote a separate verifier,
`scratch/ml11_prescribed_independent_check.cpp`.  It does not call or share
logic with `ml11_prescribed_extension_verify.cpp`.

From the raw integer files it recomputes:

1. the cycle has 924 entries;
2. every one of the 462 rank-five masks and every one of the 462 rank-six
   masks occurs exactly once, and no other mask occurs;
3. all 924 cyclic neighboring pairs are containment pairs differing in one
   bit;
4. the prescribed file has 37 distinct vertices and 36 valid middle-level
   edges;
5. it occurs in the cycle in direction `-1`;
6. it contains nineteen rank-six vertices;
7. the complementary-direction arc chosen immediately after the prescribed
   path contains 93 distinct rank-six vertices, 186 edges, and 187 vertices,
   and none of its vertices lies in the prescribed path;
8. the other arc consequently contains 369 rank-six vertices; and
9. the two distinct cut colours are the rank-five masks `188` and `171`.

The independent output was

```text
PASS rank5=462 rank6=462 cyclic_edges=924 path_direction=-1
prescribed_rank6=19 cut_rank6=93 cut_edges=186 cut_vertices=187
complement_rank6=369 cut_colours=188,171
```

I also decomposed the cyclic edge set by alternating edge parity.  Every
vertex has degree one in each parity class, so the displayed cycle itself
recovers two edge-disjoint perfect matchings.

The final supplied verifier independently reports

```text
PASS ML_11 Hamilton cycle vertices=924 edges=924
prescribed_vertices=37 prescribed_edges=36 cut369_rank6=369
cut93_rank6=93 cuts_outside_prefix=yes disjoint_from_prefix=yes
direction=-1 cut_colours=188,171
```

The rank-five ledger follows without a separate assumption.  The 369-upper
arc has 368 internal rank-five vertices, the 93-upper arc has 92, and their
two distinct cut endpoints supply the remaining two:

\[
                         368+92+2=462.
\]

## 2. Audit of the two-perfect-matching formulation

The formulation in `ml11_prescribed_matching_search.cpp` is sound and, for
this path-extension question, complete.

Colour the 36 prescribed path edges alternately.  Each colour class is a
matching.  The program forces the first class into a perfect matching
`M_0`.  It forces the other class into a second perfect matching `M_1` and
forbids, at every lower vertex, the edge selected by `M_0`.  Therefore
`M_0` and `M_1` are edge-disjoint.  Their union is a simple degree-two
spanning graph and hence a disjoint union of alternating even cycles.
`cycle_components` follows exactly the permutation

\[
 l\longmapsto M_0(l)\longmapsto M_1^{-1}(M_0(l)).
\]

It reports one component exactly when the union is one 924-vertex Hamilton
cycle.  `emit_cycle` then writes the alternating lower--upper traversal of
that component.

Conversely, any Hamilton cycle containing the prescribed path has two
alternating perfect-match edge classes.  Globally swapping their names if
necessary makes the first prescribed edge belong to `M_0`, so it satisfies
the program's forced colouring.  Thus the matching formulation does not
discard any possible extension merely by fixing the two colours.

The augmenting-path routine is an exact bipartite matching routine for each
chosen graph.  Randomness changes which extension is obtained, not the
validity of a returned matching.  Rebuilding with GCC and running

```text
./ml11_match k11_ml_prescribed_path_q19.txt 1 77124
```

gave

```text
trial=1 cycles=1 924
SAT trial=1
```

and reproduced `k11_ml_prescribed_cycle_q19.txt` byte for byte.  This
bytewise reproducibility is implementation-specific because `std::shuffle`
is a standard-library operation; it is not needed for the theorem because
the frozen cycle is checked directly.

## 3. Audit of the optional SAT formulation

The `MIDDLE_FORCE_PATH` branch in `middle_levels_sat.cpp` validates the
prescribed vertices and edges and adds one positive unit clause for each of
the 36 path edges.  The existing degree-exactly-two clauses force every
internal prescribed vertex to have precisely those two incident cycle
edges.  The lazy component cuts are valid cut constraints: every spanning
Hamilton cycle crosses every proper current component, while a one-component
degree-two spanning subgraph is a Hamilton cycle.  Therefore, in the default
mode with no additional shadow options, this is an exact alternative
encoding of the same extension question.

The source compiled cleanly against the repository's build-only CaDiCaL
stub, and the forced-path front end reported

```text
forced_path_vertices=37 forced_path_edges=36
```

The stub deliberately cannot solve, so this was only a syntax/front-end
test.  No SAT claim relies on it: the explicit cycle is the complete
certificate.

## 4. Caveats and non-bugs

- `NO CERTIFICATE` from a bounded randomized matching search is not an
  impossibility result.  Only a returned and independently checked cycle is
  evidence of existence.
- The matching search is intentionally hard-coded to the `k=11`, 37-vertex
  instance.  It is not a general middle-level theorem implementation.
- The matching search and `MIDDLE_FORCE_PATH` reader do not reject trailing
  noninteger text.  The supplied path is a clean all-integer file and its
  parsed length and every edge are checked, so this is input-format hygiene,
  not a defect in the present certificate.  The standalone verifier's final
  parser does reject noninteger input.
- The optional SAT source may impose strictly stronger conditions when one
  of its shadow/run modes is requested.  Only its default forced-path branch
  is equivalent to the bare extension problem audited here.
- A middle-level Hamilton completion is only the central combinatorial
  ledger.  It neither constructs entries `A_i` nor verifies any contiguous
  subarray OR coverage.

## 5. Frozen hashes audited

```text
fe4b03bc40bae4c6cf0435f2b30c610c453c02c3288c319a9b0361952c707a41  k11_ml_prescribed_path_q19.txt
15afd3798debafdc08dcec42e7c3d0e79c44f54d3f4d29ca4d6f27b41905c0d2  k11_ml_prescribed_cycle_q19.txt
600d5e2adff0393c7d1da659b8a3d4491310e466e374cad9f15c57cf02eb0a88  ml11_prescribed_matching_search.cpp
75b5a76258489eae53dd74a7abbaeabbc4312a31e5936ed8f09563e2f6e7186a  ml11_prescribed_extension_verify.cpp
a3ce24742f0f51ddd94564cf3e5c01b37a16bb3175cf7c389e5e177689a878f2  middle_levels_sat.cpp
d9dd9a4906ac5d96366fd1f7da7725b3b84e03f2c265be67f1e3d7905036c765  scratch/ml11_prescribed_independent_check.cpp
```

Subject to the exact scope above, the audit result is **PASS**.

## 6. Addendum: optional mixed-run scoring mode

The generator was subsequently extended with an optional `SHORT_COUNT`
argument and a strict noninteger-rejecting path parser.  The matching and
cycle-generation logic is unchanged.  In the unscored mode, seed `77124`
still returns the primary certificate on trial one, byte for byte.

The scoring implementation is correct for the following narrowly defined
quantity.  It orients the rank-six row so that the prescribed nineteen-mask
path prefix comes first, then applies the mixed-delay criterion to every
internal coordinate one-run.  If a run begins at zero-based index `first`,
the test

```cpp
first <= short_count ? 3 : 4
```

is intentional rather than an off-by-one error: in one-based notation a run
starting at `q+1` still needs only length three, while starts at `q+2` or
later need length four.  Runs touching either linear boundary are correctly
exempted.  Scores are ordered lexicographically by total length deficit and
then number of violating runs.

An independent reimplementation gives the primary cycle score
`239/154`.  For 5,000 trials with seed `77125` and `SHORT_COUNT=19`, the
updated program reports

```text
score trial=602 deficit=239 violations=152
score trial=849 deficit=210 violations=136
BEST trials=5000 deficit=210 violations=136
```

and reproduces `k11_ml_prescribed_cycle_q19_runbest210.txt` byte for byte.
That new file independently passes the complete Hamilton-cycle, prescribed
path, and `369/93` cut audit.  Its independently recomputed values are

```text
rank5=462 rank6=462 cyclic_edges=924 path_direction=-1
prescribed_rank6=19 cut_rank6=93 complement_rank6=369
q19_deficit=210 q19_violations=136 cut_colours=436,433
```

The scoring mode prints the best valid Hamilton cycle found even when its
deficit is positive, and then exits with status `1`; this is deliberate and
must not be mistaken for an invalid certificate or an UNSAT result.

Most importantly, `210/136` is a heuristic central-row score, not a distance
to an OR array.  It tests existence of some factor for the mixed central
schedule only.  It does not enforce compatibility with the already chosen
22 factor entries of the certified prefix, the fixed-boundary continuation
conditions, lower labels and pins, or upper-shadow coverage.  A positive
deficit has no proved edit-distance interpretation.

The added artifacts audited here have hashes

```text
600d5e2adff0393c7d1da659b8a3d4491310e466e374cad9f15c57cf02eb0a88  ml11_prescribed_matching_search.cpp
e42c4fa8f2a658a9d0c74e34a47d83e1218bea643ead242f6ca4beff07ac0020  k11_ml_prescribed_cycle_q19_runbest210.txt
d9dd9a4906ac5d96366fd1f7da7725b3b84e03f2c265be67f1e3d7905036c765  scratch/ml11_prescribed_independent_check.cpp
```

The addendum verdict is **PASS**, subject to these scoring-scope caveats.
