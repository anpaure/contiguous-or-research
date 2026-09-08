# K16 c5960 carrier: exact upper/Hall/provider-component audit

## Verdict

The carrier in
`scratch/root_k16_collar_c5960_20260730/candidate.targets` is **not a
materializable optimal witness**.

It satisfies exact middle ownership, but it has two independent failures:

1. its rank-8 chronology misses 18 arbitrary-upper targets; and
2. its exact depth-3 lower compiler incidence graph has Hall deficiency 427.

The already-frozen 20-target split-pair collar signature is fully saturated
(matching 20/20).  Thus this carrier is an explicit counterexample to using
that local signature as a global compiler gate for a wholly rethreaded
chronology.

## Independent replay

The independent auditor is
`scratch/audit_k16_c5960_provider_components_20260730.py`, SHA-256
`95188fab992c224b4c40147fdf5c2b47121f1fe2ea975b5d578912c2c4d26fe5`.

Its frozen output is
`scratch/root_k16_collar_c5960_20260730/provider_components.audit.json`,
SHA-256
`acde1fbcf20090dbecb0f633e920611133056fe4128c83b92f3b58cfa4bf82d0`,
payload SHA-256
`08891162c18db1beca2d3a02be8143ce94a6cb91d0fd327a9747feeeda58c760`.

The source carrier has SHA-256
`c94fced40186400703799f62edd561b0eb2e16018efad0f63df300b6834c0cf3`.

The replay obtains:

- 12,873 rank-8 targets, 12,870 distinct: no middle hole;
- arbitrary-upper holes: 18, with rank histogram `9:8, 10:7, 11:3`;
- 26,332 lower targets and 26,552 proper-prefix physical cells;
- 352,285 lower incidences;
- maximum lower matching 25,905;
- exact lower Hall deficiency `26332-25905=427`;
- canonical Hall shore: 4,139 left targets versus 3,712 cells.

The 18 upper holes are

```
077d 2f65 3379 3779 6f65 a27d a2f9 a3f9 a3fd
ae65 b27d ca7c ca7e cb78 cb7c cb7e cf78 ea7e
```

## Exact lower deficiency decomposition

The canonical lower Hall shore splits into 305 connected components:

- 298 isolated zero-provider rank-7 targets, each of deficiency one;
- six nontrivial deficiency-one components of sizes
  `24/23, 9/8, 7/6, 5/4, 4/3, 3/2` (left/right);
- one giant component of size `3789/3666`, deficiency 123, component SHA-256
  `f1bd591860b1734c0618c16c13b87e68b5df4ac35d0b3a9f7ee8c7466295c49c`.

The six small nontrivial components are recorded exactly in the JSON.  Their
left sets are:

```
4816 481e 4836 483e 4856 4876 4896 4897 489e 48b6 48d6
491e 4996 5816 5817 581e 5856 5896 c816 c81e c836 c856 c896 d816

a41c a41d a43c a45c a49c a51c ac1c b41c e41c

c780 c781 c782 c784 c788 d780 e780

2645 264d 2655 26c5 a645

b0a4 b0a6 b0ac b2a4

e80c e84c e90c
```

Of the 298 candidate zero-provider targets, 297 had at least one provider in
the exact229 comparison carrier.  The sole exception is `4879`, already an
isolated zero of that comparison basin.  The JSON records every destroyed old
provider cell for all 297 targets.

The arithmetic is exact:

```
298 isolated + 6 small + 123 giant = 427.
```

## Why the failure is so large

The three adjacent flats occur at positions `1811, 12368, 12370`.  Therefore
the forced-depth histogram is

```
d=3: 1812, d=2: 10557, d=1: 2, d=0: 502.
```

In particular, 502 terminal middle rows generate no proper-prefix cell at all,
and the first flat removes the depth-3 row from most of the chronology.  The
comparison exact229 carrier has flats `6320, 12869, 12871`, 32,063 physical
prefix cells, and Hall deficiency 25.  The c5960 chronology has only 26,552
prefix cells, merely 220 more than the 26,332 lower targets.  Its enormous
provider loss is therefore not visible in an upper-shadow hole count.

## Why 18 upper holes and Hall deficiency 427 do not conflict

They are counts in different incidence systems.

- The 18 upper holes ask whether unions of consecutive rank-8 carrier targets
  hit every rank above eight.  No distinctness assignment is involved.
- The Hall deficiency asks whether every lower target can be assigned to a
  **distinct physical proper-prefix erosion cell**.  It depends on flat
  placement, envelopes, mandatory bits, and competition between targets for
  the same cell.

Good upper coverage is therefore not a proxy for a compilable lower side.

## Minimal sound strengthened gate

For a candidate whose chronology is wholly rethreaded, the minimal sound gate
is:

1. materialize the forced offsets and maximal envelopes;
2. build every proper-prefix cell's exact lower-target signature;
3. run maximum matching on all 26,332 lower targets; and
4. separately replay arbitrary-upper coverage.

For a genuinely local edit of a fixed carrier this can be compressed: take
the complete alternating closure of every lost or gained provider incidence
and match only that dynamic closure while retaining the unchanged matching
outside it.  A frozen 20-target shore is sound only when the edit cannot create
new deficient components outside that closure.  Here every target position
changes, the dynamic closure is the 4,139-by-3,712 Hall shore above, and the
full matching is the correct gate.

## Scope

This refutes only the c5960 carrier and the use of the old local signature as
a global gate.  It does not refute the 18-cell perfect-parent collar family,
the general `nu(16)=12873` conjecture, or another chronology with better flat
placement and a Hall-complete lower incidence graph.
