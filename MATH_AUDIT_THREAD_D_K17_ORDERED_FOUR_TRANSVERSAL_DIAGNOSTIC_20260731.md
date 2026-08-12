# Thread D audit: ordered-four-transversal diagnostics on the K17 seam banks

Date: 2026-07-31

Status: exact fail-closed checker and two exact **partial-bank** replays.  No
complete Catalan linear matching, K17 carrier, or all-dimensional theorem is
claimed.

## 1. Exact interface

For an even ground set of size `2m`, a literal atom is the ordered quadruple

```text
(lower, upper, tail, head) = (L, U, T, H),
```

with ranks `m-1,m+1,m,m` and

```text
T intersection H = L,       T union H = U.
```

The checker verifies all of the following literally.

1. Every atom has the displayed ranks and identities.
2. The lower and upper maps are permutations of their full shores.
3. The tail and head maps are injective.
4. The directed middle graph is acyclic.  Independently, it computes the
   undirected degree excess and graphic cycle rank.

These are exactly the ordered-four-transversal conditions of
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`.
Exit status zero is reserved for a declared-complete literal certificate
passing all four conditions.  A partial bank always exits with status three,
even when every represented atom is legal.

The direct atom schema is

```json
{
  "schema": "threadD-ordered-four-transversal-atoms-v1",
  "ground_size": 4,
  "declared_complete": false,
  "atoms": [
    {"lower": 0, "upper": 0, "tail": 0, "head": 0}
  ]
}
```

where the displayed zero row is only a schema illustration and would fail
the rank checks.  The second adapter reconstructs retained source arcs and
selected seams from a component file plus a persisted candidate.  It also
checks that the candidate cut set is exactly the two canonical source cuts
per selected seam.

The reusable producer hook

```text
audit_middle_levels_path_cover(old_ground_size, all_middle_states,
                               directed_edges, sample_limit)
```

accepts a directed Johnson path/cycle cover on the rank-`m` B rail of
`ML(2m-1)`.  For each edge it records the A-position intersection and upper
turn union.  At each state with a unique predecessor and successor it records
the lower triple-intersection turn.  A producer can therefore attach exact
turn multiplicity histograms to every persisted incumbent without rerunning
a solver.

## 2. Why the present K17 replay is partial

Put the current 17 old coordinates inside an 18-coordinate ground set, with
the new coordinate `infinity` omitted from every stored mask.  Then `m=9`.
The stored PBBS component file consists only of rank-nine old-only states,
so every reconstructed edge is a same-B-rail atom.  It does not contain the
infinity rail or the cross-rail atoms of a complete 18-coordinate diamond
matching.

Accordingly, the adapter can exactly measure:

* old-only lower and upper palette multiplicities;
* ordered tail/head collisions;
* middle degrees and cycles;

but it cannot decide whether the absent rails admit a compatible completion.
For a complete replay each selected atom on those rails must export its typed
lower label, typed upper label, oriented physical tail, and oriented physical
head.  This is also why the diagnostic does not infer a middle-levels
decoration: an arbitrary Catalan linear matching need not be resolvable on
one middle-levels Hamilton cycle.

## 3. Persisted `allcegar5` bank

The exact inputs are

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
scratch/k17_fragment_seam_setcover_allcegar5_20260731.result.json
```

The reconstructed bank has 23,665 legal atoms.  Its exact restricted ledger
is

```text
tail duplicate excess                     0
head duplicate excess                     0
middle degree excess above two             0
graphic cycle rank                         2
directed cyclic SCCs                       2 (16 vertices total)

full lower missing                    21,191
full lower duplicate excess             1,098
full upper missing                    24,310
full upper duplicate excess             4,217
```

The full-shore figures split canonically.  Exactly 19,448 missing lower masks
and all 24,310 missing upper masks contain `infinity`, hence belong to absent
sectors.  The genuine represented-rail lower leave is therefore

```text
21,191 - 19,448 = 1,743,
```

agreeing with the independent partial-factor audit.  On the upper old-only
shore, all 19,448 labels occur, with 4,217 repeated incidences.  Thus this
incumbent has already solved old-only upper surjectivity, but not the integral
upper injectivity required by the four-transversal.  Its 1,098 lower repeats
include retained-source/seam correlations and are intentionally stronger
than the 37 repeats among the selected seams alone.

The ML trace parameters and multiplicities are

```text
(m,Q,P,Cat_m) = (9,24310,19448,4862)
A positions:   0^1743 1^21482 2^1072 3^13
upper turns:   1^15665 2^3377 3^378 4^28
lower turns:   0^4442 1^8746 2^4660 3^1431 4^160 5^9
```

Thus the upper turn map is surjective, while the lower turn map on the 23,044
defined internal positions is not.  The directed bank has 647 underlying
components, not one ML Hamilton cycle.  Alternating occurrence SDR is
therefore marked `NOT_APPLICABLE`, rather than inferred from upper support.

## 4. Persisted exact-active-2649 bank

The second candidate is

```text
scratch/k17_fragment_exactactive2649_distinct_20260731.result.json
```

It reconstructs 23,107 legal atoms and has

```text
tail duplicate excess                     0
head duplicate excess                     0
middle degree excess above two             0
graphic cycle rank                         1
directed cyclic SCCs                       1

full lower missing                    22,535
full lower duplicate excess             1,884
full upper missing                    24,310
full upper duplicate excess             3,659
```

After subtracting the absent infinity-containing lower shore, the old-only
lower leave is 3,087.  The 1,884 lower repeats are exactly the already-known
retained-source correlations: 1,142 selected protected-source conflicts plus
742 unprotected ejection obligations.  The seam colours themselves are
distinct; the four-transversal ledger correctly detects that this does not
make the combined retained-old-plus-seam bank injective.  Again, every
old-only upper label occurs, but with 3,659 repeats.  The one graphic cycle
is the independently reported forced cycle.

Its corresponding trace multiplicities are

```text
A positions:   0^3087 1^19339 2^1884
upper turns:   1^16087 2^3071 3^283 4^6 5^1
lower turns:   0^4929 1^8556 2^4543 3^1277 4^137 5^5 6^1
```

Upper turn support is again complete, lower turn support is not, and the
1,204-component bank is not an ML Hamilton cycle.  Its alternating-SDR status
is again exactly `NOT_APPLICABLE`.

These identities are a useful integral-obstruction signature.  In both
incumbents the ordered tail/head maps and the degree-two condition are already
exact; what remains inside the represented rail is joint palette
injectivization plus cycle removal.  Releasing an unprotected source edge can
change these numbers, so they are incumbent diagnostics rather than no-go
theorems.

## 5. Reproduction and scope

Run the tiny exact tests with

```text
python3 scratch/test_threadD_ordered_four_transversal_20260731.py
```

They cover a complete `m=2` forest certificate, a complete three-palette
certificate rejected solely for its directed cycle, a partial certificate
which is never promoted to PASS, and the callable ML hook on the unique
three-state B-rail cycle of `ML(3)`.

The two K17 audits are reproduced by

```text
python3 scratch/threadD_audit_ordered_four_transversal_20260731.py \
  --components scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components \
  --candidate scratch/k17_fragment_seam_setcover_allcegar5_20260731.result.json \
  --ground-size 18 \
  --output scratch/threadD_k17_allcegar5_ordered_four_transversal_20260731.audit.json

python3 scratch/threadD_audit_ordered_four_transversal_20260731.py \
  --components scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components \
  --candidate scratch/k17_fragment_exactactive2649_distinct_20260731.result.json \
  --ground-size 18 \
  --output scratch/threadD_k17_exactactive2649_ordered_four_transversal_20260731.audit.json
```

Both commands deliberately return status three.  They report turn-map
multiplicities, but do not pretend that surjection is an alternating-occurrence
SDR.  The latter requires one materialized middle-levels Hamilton cycle and
its rail-indexed occurrence order.  They do not use the retracted fixed-size
matching bound, and they do not assert that an arbitrary linear diamond
matching is middle-levels-resolvable.
