# K16 four-filter fixed-order capped-host no-go

## Exact scope and conclusion

Let the rank-eight carrier be

```
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452
```

It is a permutation of all `C(16,8)=12870` rank-eight masks.  Consider the
waste-three P/Q compiler architecture: a physical word has length `12873`,
three physical starts and three physical deadlines are omitted, and every
selected rank-eight row has depth at most three.

**Theorem.** No P/Q schedule for this fixed carrier can compile a universal
physical word.  In fact, requiring the mandatory upper target

```
H = 0xa9ce
```

reduces the greatest selected proper-prefix area to `25828`.  Even granting
the three omitted starts the uniform, deliberately optimistic credit `3`
each gives

```
25828 + 9 = 25837 < 26332
```

available lower cells, whereas there are `26332` nonempty masks of ranks
one through seven.

This is a solver-independent, source-relative no-go for the authenticated
fixed target order and the stated P/Q architecture.  It is not an
unrestricted K16 no-go and says nothing about a different carrier rethread.

## Why an `H` interval is mandatory

Literal interval replay of the carrier finds exactly five missing upper
masks:

```
a9ce, a9de, a9fe, b8ce, b8cf.
```

Any universal physical word must therefore contain a nonempty interval `J`
whose cellwise OR is `H=0xa9ce`.

Fix a P/Q schedule and write `E_p` for the intersection of all middle targets
active at physical position `p`.  Every middle-realizing cell is a submask of
`E_p`.  If some realization has OR `H` on `J`, then every cell on `J` is a
submask of `H`.  Replacing the realization by the maximal capped word

```
C_p = E_p & H  for p in J,
C_p = E_p      for p outside J
```

cannot lose any required middle bit.  It cannot add an illegal middle bit,
because `E_p` is a submask of every active target.  It also keeps every cell
nonzero and its OR on `J` is exactly `H`: it contains the old realization
and remains a submask of `H`.

Thus, for a fixed schedule and interval, the following three checks are
necessary and sufficient:

1. every capped cell is nonzero;
2. every rank-eight middle row literally reconstructs;
3. the capped cells on `J` have OR exactly `H`.

This maximal-cap argument is why the dynamic program below loses no physical
realization.

## The host has length at most seven

The nine rank-eight facets of `H` occur at carrier positions

```
2129, 6479, 7033, 7238, 7578, 9330, 9530, 10447, 12336.
```

They are pairwise nonadjacent.

Suppose an `H`-only physical interval has length `ell >= 8`.  A row started
in the first `ell-3` positions of the interval finishes inside it because
all depths are at most three.  There are at least five such start positions,
and only three physical starts are omitted globally, so at least two are
selected.  Consecutive selected starts correspond to consecutive middle
rows.  Each of those rows is reconstructed entirely by cells contained in
`H`, hence is a rank-eight facet of `H`.  This contradicts facet isolation.
Therefore `ell <= 7`.  Length eight was nevertheless included as a fail-safe
regression in the exact enumeration.

## Exact finite dynamic program

For each fixed host length `1,...,8`, the independent checker scans the
`12873` physical positions.  Immediately before a position, its state is

```
(number of used start holes,
 number of used deadline holes,
 accumulated OR of every active middle row,
 host phase and remaining length,
 accumulated host OR).
```

Every transition independently chooses whether the current position is a
start hole and a deadline hole.  It intersects the active targets to obtain
`E_p`, uses `E_p&H` during the host and `E_p` otherwise, updates all active
row ORs, and accepts a deadline only when the ending row exactly equals its
target.  A host may finish only with OR `H`.

For an exact state, only the history with greatest area is retained.  This
dominance is exact: all future feasibility tests and area increments depend
only on the displayed state.  The increment at position `p` is

```
p * (start_hole - deadline_hole),
```

whose sum is exactly the selected proper-prefix area.

The audited maxima by host length are

| length | maximum area | status |
|---:|---:|---|
| 1 | 23320 | realizable |
| 2 | 23320 | realizable |
| 3 | 25828 | realizable |
| 4 | 23323 | realizable |
| 5 | — | infeasible |
| 6 | — | infeasible |
| 7 | — | infeasible |
| 8 | — | infeasible |

The global maximizer is

```
start holes X = {6479,6480,12872}
deadline holes Y = {0,1,2}
host interval   = [6480,6482]
host cells      = a04e,884e,89cc
host OR         = a9ce
selected area   = 25828.
```

Independent literal replay has zero capped cells, zero middle failures, and
exact host OR `a9ce`.  Its actual omitted-start credit is only
`3+3+1=7`, hence its actual physical lower-cell count is `25835`; the theorem
uses the larger schedule-independent upper bound `25828+9`.

Finally, every physical proper-prefix interval has one literal OR, so
distinct lower targets inject into distinct such intervals.  The strict
capacity inequality `25837<26332` is therefore decisive before a lower Hall
or common-cap solve.

## Fixed maximizing-schedule Hall cross-check

For the original area-maximizing schedule

```
X={6479,10451,12872}, Y={0,1,2}, selected area=29799,
```

the exact physical-cell count is `29799+7=29806`, not `29799+9`, because the
omitted terminal start `12872` has only its singleton interval.

For a physical lower cell `J`, let `U(J)` be the OR of its maximal envelopes
and let `M(J)` be the union of all middle bits whose entire host set lies in
`J`.  A lower mask `S` is individually realizable on `J` exactly when

```
S subset U(J),
M(J) subset S,
E_p & S != 0 for every p in J.
```

The full graph has `26332` targets, `29806` physical cells and `345822`
incidences.  Its only zero-degree targets are `8000` and `898d`.  Maximum
matching size is `26249`, and the canonical alternating Hall shore has

```
|L|=635, |N(L)|=552, deficiency=83.
```

The left-shore rank histogram is `1:1, 6:95, 7:539`; the right shore has
`278` singleton and `274` length-two cells.  A separately indexed Thread D
audit agrees exactly after translating cell ids to physical `(start,length)`
pairs.

This Hall obstruction is schedule-specific and is superseded, for the fixed
carrier order, by the all-schedule `a9ce` capped-capacity theorem above.  Its
full catalogues are retained as a regression and as local information for
future rethreads.

## Authenticated artifacts

- `scratch/audit_j3959_outer_context_k16_fourfilter_a9ce_capped_pq_dp_20260731.py`
  - SHA-256 `1a1477530d82b43bfb42f14432bbc35617273475a61003b5b3474609df15f4f4`
- `scratch/j3959_outer_context_k16_fourfilter_a9ce_capped_pq_dp_20260731/audit.json`
  - SHA-256 `ba31465e86e1896d3596891182c0868259337606b70d20eea2a89b2e617fbd1a`
  - payload SHA-256 `c7ac8ccd70641ee2f0b40487039142faa673b0f49a19d82c46d9bd2e4e05f870`
- `scratch/j3959_outer_context_k16_fourfilter_a9ce_capped_pq_dp_20260731/maximal_length3_capped.word`
  - SHA-256 `10dd1395bea724ee65a792fe4a0b80710b6866f960c12d5e57dfe5475f7bd2bd`
- `scratch/audit_k16_fourfilter_insert_aug_d2_1_static_hall_20260731.py`
  - SHA-256 `c22e77fb991a87716336f72e932f5bf2fb00c695beb2875b1ef4a963b14620a6`
- `scratch/k16_fourfilter_insert_aug_d2_1_static_hall_20260731.audit.json`
  - SHA-256 `25fe15941a06715e58eccc39e120294e63df4f143ae9bc400036158afc87cb4f`
  - payload SHA-256 `225c29c505107a1c5547d2c868cecb10bff07f747de10d6c9ca8ed00739cb0e4`
- full Hall edge catalogue
  - `scratch/k16_fourfilter_insert_aug_d2_1_static_hall_20260731.edges.tsv`
  - SHA-256 `dc7e27d7e05bd6ff83273e24cf9acd1509abdb3a4db8f9c741fbcf2a52c7cc64`
- canonical Hall left/right catalogues
  - SHA-256 `f926129204587f751ad117dc3e4ecc54712b5b556b904cf3fa73af2a75975c8c`
  - SHA-256 `9f757404bf3ee78bec1f6ba91d48d19afec328947ab5e9bd3671eb61dbb9f620`
- full zero-host obstruction catalogue
  - `scratch/k16_fourfilter_insert_aug_d2_1_static_hall_20260731.zero_obstructions.tsv`
  - SHA-256 `da05301fee3c7d79c4bb6fd00044639cdc964ca385d4242a90ff9ef0f0295ed0`

