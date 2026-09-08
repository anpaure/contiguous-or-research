# Audit of the `K17` OPTIMAL28 complement-repair edge floors

Date: 2026-07-31  
Verdict: **PASS, architecture-specific scope enforced**

Audited theorem:
`MATH_THEOREM_K17_OPT28_COMPLEMENT_REPAIR_EDGE_FLOORS_AND_CAP_REBASE_20260731.md`.

## 1. Frozen input and bank split

The audit binds the owner word

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
```

and rotates it at position `21331`.  The first `4108` entries are the frozen
marked path and the remaining `20202` the complement.  Direct replay checks
that all `24310` owners are distinct rank-nine sets and that all cyclic
intersections are distinct rank-eight sets.

The independent two-bank audits agree on the exact forced row:

```text
rank profile                         9^4108 8^20203
distinct direct facets                         20203
strict D2 bad runs                              2392
replay failures                                 3568
missing bit-row incidences                      3759
upper holes 10/11/12                   1900/911/128.
```

The maximal envelope has no empty letter.  This does not mitigate the
failure: maximal replay already omits required bits, so every further cap is
contained in an invalid maximal word.  The theorem correctly reports
common-cap infeasibility before Hall rather than a Hall deficiency.

## 2. Residence interval semantics

For an internal complement run `0 1^r 0`, `r=2` or `3`, the stored interval
is the old edge segment from its entry edge through its exit edge.  If every
edge in this segment remains selected, its internal vertices already have
degree two, so the segment remains consecutive in any new two-factor,
possibly reversed.  Consecutive intersection changes its positive trace to
`1^(r-1)`, which is forbidden in a depth-two row.  Hence every repair in the
fixed marked-path/standard-zipper architecture must hit every stored
interval.

There are exactly

```text
owner length 2 intervals                     1025
owner length 3 intervals                     1367
total                                         2392.
```

Earliest-right-end greedy returns `1603` edge positions.  The script checks
that they hit every interval.  It separately records the `1603` intervals
which trigger those choices and checks that consecutive trigger intervals
are disjoint.  Thus it supplies both a cover of size `1603` and a packing of
size `1603`; interval packing--cover duality is proved directly rather than
invoked numerically.  The length-two-only calculation similarly gives
`754`, but that is not the two-bank requirement.

## 3. Rank-ten edge floor

If a consecutive interval of rank-nine Johnson owners has union `S` of rank
ten, every adjacent pair has a rank-ten union contained in `S`, hence equal
to `S`.  Therefore each missing rank-ten target needs a newly selected edge
with that target as upper label.

The frozen cycle has `17548` distinct upper labels out of `19448`, so the
missing family has size `1900`.  Its sorted-list payload agrees with the
independent shadow audit:

```text
bf8b1769b6362b27c03e3c3652cee06fad3162864bb53a50894113efa08fb2fb.
```

One new edge supplies only one upper label.  Hence `1900` new edges are
necessary.  Because edge count is fixed, at least `1900` old edges are also
deleted.  The residence and upper repairs may use the same deletions, so the
combined bound is the maximum, not the sum.

## 4. Fixed-skeleton and nonflat caveats

The interval theorem allows arbitrary interior Johnson rethreading.  The
existing residual-pairing face is smaller and is already empty: the frozen
zipper audit finds `724` bad owner runs internal to `257` immutable
components, including `227` length-three runs inside `141` individual macro
words.  Reordering or reversing those objects cannot alter their internal
zeros.

Conversely, neither lower bound is global.  The `1603` number assumes the
fixed marked bank and the standard owner/facet zipper.  The `1900` number
assumes rank-ten service comes from intervals of the rank-nine owner
chronology.  A genuinely nonflat compiler can escape those assumptions.

## 5. Common-cap scope

A marked-preserving lower-rainbow rethread fixes the **set** of `20203`
direct facets, so it fixes the scalar ledger `45332/48625`, slack `3293`.
It changes their order.  Since consecutive facets determine complement
owners and the ordered triples determine maximal envelopes, neither the cap
graph nor its permanent hosts are invariant.

The theorem therefore correctly requires this order:

1. choose and connect the repaired owner factor;
2. materialize the ordered facet row;
3. pass exact inversion and all upper-provider rows;
4. only then build the residual common-cap graph; and
5. enforce either a guarded-Hall face or all exact unary/pair/triple cuts.

No common-cap result is inferred from the positive scalar slack.

## 6. Reproduction

```text
python3 scratch/audit_k17_opt28_complement_repair_floors_20260731.py
python3 -m py_compile scratch/audit_k17_opt28_complement_repair_floors_20260731.py
```

Frozen audit bundle:

```text
scratch/audit_k17_opt28_complement_repair_floors_20260731.py
  SHA-256 8b301755ef697a0ce52f7115760a34a1ecb741974dedc507ec1dca33f7ce827a
scratch/k17_opt28_complement_repair_floors_20260731.audit.json
  SHA-256 9be467d5a1feca78ca5e361e49ab57ae3bda7bef32232aaa85c0ee8042102068
  payload 01a30120a9a0c05acaccab862e673bababe038086c0dfd79a5bfd76efe876cc7
```

The script is a linear-time audit over `2392` intervals and one rank-ten
palette; it performs no search or SAT solve.
