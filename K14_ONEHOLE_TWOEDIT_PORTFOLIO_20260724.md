# Exact two-edit anchor stars for the 208 one-hole `k=14` suffix roots

## Purpose

The certified word is a 3,434-entry prefix followed by a 242-entry suffix.
Exactly 208 single deletions of that suffix leave a 241-entry suffix covering
259 of the prefix's 260 missing targets.  A successful two-value repair of any
one root proves

```text
nu(14) <= 3675.
```

The saving then propagates through the current trimmed lifts by respectively
`1,2,4,8,16,32` entries in dimensions 14 through 19.

This portfolio is not one of the live unrestricted append-241 solves.  It is a
small exact candidate subfamily built around the certified suffix.

## Deterministic manifest

Run

```bash
python3 scratch/build_k14_onehole_twoedit_manifest.py \
  k14_pinnable_factor_missing260.txt k14_missing_260.txt \
  k14_append_242.txt scratch/k14_onehole_twoedit_portfolio_20260724
```

The builder independently recomputes the old suffix-OR chain and all internal
and crossing witnesses needed for the 260-hole family.  It requires exactly
208 one-hole deletion roots.  In every root, replacing suffix position 3 by
the unique hole leaves exactly one residual hole; position 3 is therefore a
common phase anchor.

For every root the full manifest pairs anchor 3 with each of the other 240
positions.  It contains

```text
208 * 240 = 49,920
```

position architectures.  The two replacement values are not restricted by
the manifest.  Each CNF case gives both positions arbitrary nonzero 14-bit
values.  The default split has eight roots and 1,920 cases per full shard,
with a final 1,920-case shard because 208 is divisible by eight.

The recommended first shard is `shard_00.tsv`, containing deletion roots
`3,4,5,6,7,8,9,10` and every pair `(3,q)`, `q != 3`.

## Exact provider CNF

For one root and selected positions `p<q`, every old target with a witness
avoiding both positions survives.  Only the fixed 260-hole family needs to be
examined, because every other target already has an unchanged witness wholly
inside the 3,434-entry prefix.

For an endangered target, every replacement-dependent interval is of one of
three types:

1. it contains `p` but not `q`, with OR `base OR x`;
2. it contains `q` but not `p`, with OR `base OR y`;
3. it contains both, with OR `base OR x OR y`.

The distinct bases are computed exactly from the left/right OR chains, with
the ten certified old suffix ORs included in the crossing types.  A base not
contained in the target is impossible.  Otherwise its need is
`target & ~base`; superset needs of the same type are dominated and deleted.

Use one exactly-selected manifest case, 28 shared value bits for `x,y`, and a
provider selector for every remaining `(case,target,type,need)`.  A provider
implies its case and the exact bit conditions:

```text
p-only: x subset target and need subset x
q-only: y subset target and need subset y
both:   x subset target, y subset target, need subset (x OR y).
```

The case implies a provider disjunction for every endangered target.  This is
sound and complete for the listed architectures.  The construction is the
14-bit, branch-specific-root analogue of the already audited provider CNF in
`scratch/k13_exact_pair_neighborhood_cnf.cpp`.

## Measured first-shard size

An exact read-only profile of the 1,920 first-shard cases found:

```text
endangered-target incidences: 6,056
undominated providers:        12,176
maximum providers in a case:  12
individually impossible cases: 0
```

Before any optional phase variables, the direct selector/provider encoding
therefore needs approximately 16,043 variables:

```text
28 value bits + 1,920 case selectors + 1,919 sequential auxiliaries
              + 12,176 provider selectors.
```

Even the simple per-provider encoding has fewer than 0.6 million clauses and
should remain below roughly 20 MiB DIMACS.  The generator must print its exact
inventory; these figures are sizing bounds, not substitutes for that output.

## Certification semantics

The frozen implementation and independent pre-launch audit are recorded in
`K14_ONEHOLE_TWOEDIT_PRELAUNCH_AUDIT_20260724.md`.

Search mode is candidate-first.  A SAT model is accepted only after:

1. reconstructing the selected deletion and both arbitrary values;
2. checking exactly 3,675 nonzero 14-bit entries;
3. direct quadratic interval-OR enumeration; and
4. independent `verify_or_array 14` and `verify_or_suffix 14` passes.

An UNSAT result closes only the cases in that immutable shard.  It becomes a
certificate only when the exact manifest, CNF, map, DRAT/LRAT trace, solver
log, and hashes are retained and an independent proof checker reports
success.  Closing all 26 shards excludes this anchor-star family, not all
241-entry completions of the fixed prefix.  The live 52-branch unrestricted
append encoding remains the exhaustive fixed-prefix decision problem.

## Preliminary one-edit screen

For orientation only, an exact provider feasibility profile over all
`208*241=50,128` one-position branches found repair-family sizes

```text
2: 43,056 cases; 3: 6,448 cases; 4: 624 cases
```

and no feasible arbitrary nonzero replacement value.  This should be promoted
only after its profiler is independently implemented and audited; it is not
used to prune the two-edit CNF.
