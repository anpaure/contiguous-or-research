# K=16 closure-594 radius-six theorem and expanded-14 ejection LNS (2026-07-30)

## Exact radius-six result

The closure-normalized `5/9/4` eighteen-cell fibre rooted at the authenticated
length-12,873 best-delete word has no universal member using at most six raw
cell substitutions.

This is a proof-checked UNSAT result, not a timeout:

- variables: `5356`
- clauses: `108783`
- CNF SHA-256:
  `a801100d40f5f276668d0f8f3a8f8feaaf1c2e83202c63708258934a19aa9d56`
- DRAT SHA-256:
  `b62ca8110e789dccaa22639fa09f7e026b11547f176ba372fdbf729b84bd113b`
- `drat-trim`: exit `0`, `s VERIFIED`
- checked resolution steps: `590251225`
- RAT lemmas: `0`

The local checker transcript and machine record are in
`scratch/k16_closure594_radius6_verified_20260730/`.

Closure normalization is nonexpansive in changed-cell support when applied to
both the candidate and incumbent.  Therefore the result excludes arbitrary
raw values, not merely the displayed 245-value normalized alphabet.  Any
feasible word in this fibre must change at least seven collar cells.

Radius seven timed out without a solver verdict; it is `UNKNOWN`, not a
no-go.  Larger nested radii were still running when this record was written.

## Consequence for local search

The exact theorem explains why one-cell annealing repeatedly transfers the
sole hole between masks instead of closing it.  A useful heuristic proposal
must be a coordinated repair chain rather than a random sequence of unrelated
cell mutations.

`scratch/k16_expanded14_ejection_lns_20260730.cpp` implements that proposal on
the external-ready basin.  Its support is the causal twelve positions plus
the exact outside provider `6524` and the ranked two-debt provider `668`:

```text
110,111,112,666,667,668,670,4299,4301,6522,6523,6524,6526,9958
```

For a current missing mask the search exactly enumerates every replacement in
this support capable of witnessing it.  It applies one such provider, follows
the newly-created singleton debts, and treats the entire ejection chain as one
annealing move.  It also maintains genuine witnesses for blockers `18553` and
`26745` outside finishing position zero.  Every zero-hole state is replayed
from scratch over all 65,535 nonempty masks before it is emitted.

Two independent H100-CPU runs were launched from the two authenticated
22-hole expanded-collar basins.  These are heuristic lanes; absence of a hit
has no theorem status.

## Exact parent-cube plateau

The two authenticated 22-hole expanded-collar basins differ at precisely nine
editable positions:

```text
110,112,666,667,668,670,4299,6523,6526
```

`scratch/k16_expanded14_h22_parent_cube_20260730.cpp` exhaustively replayed
all `2^9 = 512` hybrids obtained by independently choosing either parent's
value at each differing position.  Every hybrid has exactly 22 holes.  More
precisely, 21 hole labels are common to all 512 words; position `6523` merely
toggles the last hole between `38174` and `38172`.  The other eight binary
coordinates do not change the hole set at all, separately or jointly.  Thus
the saved parents span an eight-dimensional coverage-inert plateau times one
two-state hole toggle, not a descent direction.  This is exact only for that
binary parent-value cube; it does not exclude third values or edits at the
other expanded-support positions.

Machine record:
`scratch/k16_expanded14_h22_parent_cube_20260730.audit.json`, SHA-256
`ac7b418361c63077d9e45ce5e67402ac747bfe62c4db4df395eef49fa994b2c7`.
