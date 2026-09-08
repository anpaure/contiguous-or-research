# K16 endpoint-transport upper-pin capacity no-go

## 1. Frozen scope and verdict

The authenticated rank-eight target order is

`scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word`

with SHA-256

`9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b`.

It is a permutation of all `C(16,8)=12870` rank-eight masks.  Its exact
missing upper intervals are

```text
H10 = 0x3ceb  (rank 10),
H11 = 0xa9fe  (rank 11).
```

The verdict is

> **Fixed-order P/Q capacity no-go.**  Every depth-three, three-start-hole,
> three-deadline-hole physical realization must provide both `H10` and
> `H11`.  Already either requirement separately reduces the optimistic
> scalar lower capacity below `26332`.  Therefore the fixed target order has
> no generalized waste-three P/Q compiler lift.

This is a source-relative fixed-order theorem.  It does not exclude another
carrier order and is not an unrestricted K16 no-go.

## 2. Maximal capped-envelope reduction

Fix a P/Q schedule.  Let `E_p` be the intersection of all active rank-eight
rows at physical position `p`; every legal physical cell `C_p` satisfies
`C_p subseteq E_p`.

If an interval `J` provides a missing upper mask `H`, then every `C_p` in
`J` is a subset of `H`.  Replace the cells of `J` by

```text
C'_p = E_p intersection H.
```

This only enlarges the old cells, remains inside every active middle row,
and remains inside `H`.  Thus it preserves exact middle replay and still has
OR exactly `H`.  Consequently a schedule and provider interval are feasible
if and only if their maximal capped envelope has

1. no zero cell;
2. exact OR for every middle row at its deadline; and
3. exact provider OR `H`.

These three conditions are the complete state transition tested by the
audit DP.  A state records the numbers of used start/deadline holes, the ORs
accumulated by the at most three active middle rows, the provider phase, and
the accumulated provider OR.  States with identical data have identical
continuations, so retaining the largest accumulated selected area is exact.

## 3. Finite provider-length theorem

For a mask `H`, write `r(H)` for the longest consecutive run in the frozen
target order of rank-eight masks contained in `H`.

Consider an `H`-provider of physical length `ell`.  Every selected start in
the first `ell-3` provider positions has its complete depth-at-most-three
middle interval inside the provider.  Hence its rank-eight target is
contained in `H`.  At most three of those positions are omitted starts, and
selected starts from a contiguous physical block index consecutive middle
targets.  Therefore

```text
ell - 6 <= r(H),
```

so `ell <= r(H)+6`.

The literal target census gives:

| mask | contained rank-eight rows | expected | longest run | provider bound |
|---|---:|---:|---:|---:|
| `0x3ceb` | 45 | `C(10,8)=45` | 2 | 8 |
| `0xa9fe` | 165 | `C(11,8)=165` | 4 | 10 |

For `0x3ceb`, all longest runs are pairs; for `0xa9fe`, a longest run is
positions `11029..11032`.  The audit JSON records the complete position and
run catalogues.

## 4. Exact all-schedule DP results

The DP enumerates every provider location and every monotone three-hole P/Q
schedule for each permitted provider length.  `--` means infeasible even
before the scalar capacity gate.

| provider length | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| max selected area, `0x3ceb` | 25740 | 25740 | 25740 | 25740 | 25740 | -- | -- | -- | | |
| max selected area, `0xa9fe` | 25740 | 25740 | 25740 | 25174 | 25738 | 25743 | 22066 | -- | -- | -- |

The three omitted starts can contribute at most three physical lower cells
each.  Granting the uniform optimistic credit `+9` therefore gives

```text
0x3ceb: 25740 + 9 = 25749 < 26332  (deficit 583),
0xa9fe: 25743 + 9 = 25752 < 26332  (deficit 580).
```

Thus each mandatory upper provider separately kills every fixed-order
schedule.  No simultaneous two-pin DP is needed for the conclusion.

The literal maximizing replays have no zero cells, no failed middle row, and
the exact named provider OR.  Boundary-aware omitted-start credit is only
six in each global maximizing replay, yielding exact totals `25746` and
`25749`; the theorem deliberately uses the weaker uniform `+9` bound.

## 5. Reproducible artifacts

| artifact | SHA-256 |
|---|---|
| `scratch/audit_endpoint_transport_upperpin_capacity_20260731.py` | `9f4a5db10a55ce0834c672b0f8ba6a4d28cec4cf4ae7d6263ac9527bb04bc1df` |
| `scratch/endpoint_transport_upperpin_capacity_20260731.audit.json` | `18e2dc5a7e20f6e0f79a4681517536fab9b4ed26e414a53976a42a7c2c2f6017` |
| audit payload | `e275ffa8373413c0a7cf85e193edbce69efa27084c4faea6eedafdc535427842` |

The implementation is independent of the production upper-pin DP.  It
reconstructs all active-row intersections itself, performs the complete
bounded provider census, and separately rebuilds and replays each maximizing
capped word from its sparse P/Q event certificate.
