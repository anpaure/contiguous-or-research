# K16 length-12874 proof-aware annealing and stabilizer crossover

## Authenticated starting basins

Two literal length-12874 words have one uncovered nonzero mask:

| word | SHA-256 | missing mask | singleton masks | doubleton masks |
|---|---|---:|---:|---:|
| `scratch/k16_ripple_insert12874_onehole.word` | `5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db` | `0x287d` | 50,170 | 8,188 |
| `scratch/k16_append0200_12874_onehole.word` | `aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18` | `0x287d` | 50,170 | 8,187 |

The count of 50,170 singleton masks is the exact reason an unrestricted
single-cell annealer is poorly conditioned: most useful coverage is protected
by one physical interval, so a mutation which installs the missing mask very
often deletes another mask's last witness.

For the first basin, the exact one-cell census proves that every substitution
which installs `0x287d` leaves at least two collateral holes.  For the softer
`append0200` basin the exact floor is one.  There are exactly sixteen minimum
portals, all at zero-based position 6440, with new values

```
0x2004, 0x2005, 0x200c, 0x200d,
0x2024, 0x2025, 0x202c, 0x202d,
0x2044, 0x2045, 0x204c, 0x204d,
0x2064, 0x2065, 0x206c, 0x206d.
```

Each portal repairs `0x287d` and leaves only `0xa879` uncovered.  An independent
complete one-cell census from each of those sixteen states again has collateral
floor one; every minimum move is at position 6440 and returns the debt to
`0x287d`.  Thus these states form a closed one-cell shuttle, not a completion.
The literal words and census are

```
scratch/k16_append0200_portal_p6440_v*_onehole.word
scratch/k16_append0200_16portal_radius2_census_20260730.audit.json
```

This is scoped: a simultaneous two-or-more-cell edit can still cross the
shuttle.

## Exact parallel-tempering lane

`scratch/k16_incremental_replica_exchange_20260730.cpp` maintains exact
interval-OR multiplicities and evaluates a substitution from the two monotone
OR chains adjacent to its position.  It uses

* service-biased proposals aimed at a currently missing mask;
* compound two-through-seven-step debt cascades, accepted or rejected only
  after exact nonlinear replay;
* singleton and doubleton witness counts as a reserve potential; and
* parallel tempering to exchange states between low- and high-temperature
  replicas.

Two H100-CPU runs produced the following independently replayed snapshots:

| snapshot | SHA-256 | hole | singleton | doubleton |
|---|---|---:|---:|---:|
| `scratch/k16_12874_anneal_rex3_snapshot_20260730.word` | `771ca5868b0a81b7d0f246b51495a63495a5face0a4ffcd412eb23bdc5681456` | `0x287d` | **50,059** | 8,381 |
| `scratch/k16_12874_anneal_rex4_snapshot_20260730.word` | `5b64bb3bb0464519858d4a53909024e6c2ec983af4bbbcc85bb7c931248a0e60` | `0xa879` | **50,058** | 8,374 |

Both remain one-hole words.  The improvement from 50,170 to 50,058 singleton
masks is nevertheless real: annealing is thickening the unique-witness
firewall while remaining on the one-hole level set.  No universal word is
claimed here.

## Stabilizer crossover lane

`scratch/search_k16_stabilizer_onecut_crossover_20260730.cpp` samples coordinate
permutations in the setwise stabilizer of the current hole.  Such a permutation
maps a one-hole word to another equivalent one-hole word.  It then exactly
scans, in `O(n k^2)` per permutation,

1. every one-cut child `A[0:c] + B[c:n]` in both orientations; and
2. optional imported-block children
   `A[0:l] + B[l:r] + A[r:n]` for every right boundary.

Internal prefix/suffix/middle interval counts are updated incrementally and all
cross-boundary interval ORs are replayed exactly.  Early H100 runs reduce an
arbitrary hole-filling crossover from thousands of collateral holes to four;
examples include the exact quartets

```
{0x207d, 0x227d, 0x247d, 0x267d}
{0x286d, 0x2c6d, 0xa86d, 0xac6d}
```

but no zero-hole child has yet been found.  These four-hole children are useful
large-neighbourhood seeds because their changes are coherent witness bundles,
unlike independent bit flips.

## Current conclusion

Simulated annealing is applicable, but the certified local geometry says that
the elementary move must be a balanced compound exchange.  A missing-count-only
single-cell annealer sees a strict one-hole local minimum and a two-state debt
shuttle.  Parallel tempering with a thin-witness reserve and stabilizer-based
genetic crossover are the currently justified annealing mechanisms.

