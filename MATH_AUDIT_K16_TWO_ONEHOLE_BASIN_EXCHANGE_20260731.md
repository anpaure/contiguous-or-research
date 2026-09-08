# K16: two distinct 12873 one-hole basins have the same middle defect

## Verdict

The two authenticated length-12873 words

- `scratch/k16_upper12874_best_delete.word` (`a72cc9e0...`), and
- `scratch/k16_vv_th495_deletep1_onehole_20260731.word` (`e4a7ad4e...`)

are physically different compiler fillings, but they induce **exactly the same
first-middle chronology**.  In particular, the V/V word does not supply a new
`0xc279 -> 0x2c6d` carrier-level exchange.

Both words miss only

```text
H = 0x2c6d
```

and both have the same repeated first-middle label

```text
D = 0xc279
```

at the same two deadline groups `(11726,11728)` and `(12826,12828)`.

## Exact comparison

For both words, the selected first-middle rows have

```text
(stalls, jumps, flats, ghosts) = (0,0,3,1)
groups = 12870
distinct labels = 12869
start holes = {6432,12869,12871}
deadline holes = {0,2,3}
span histogram = 0^1 1^2 2^6436 3^6431.
```

The complete ordered list of all 12870 tuples

```text
(latest start, deadline, middle label)
```

is identical between the two words.

Their length-12874 controls also have identical first-middle chronologies.  In
each control, the unique witness for `H` is `[1,4]`, whose cells are

```text
0x2800, 0x2069, 0x0065, 0x0424.
```

Deleting physical position 1 removes `0x2800`; the residual context is
`0x246d`, missing precisely bit `0x0800`.  Thus the two one-hole states arise
through the same exact deletion circuit.

## Literal exchange circuit

An exhaustive common-provider audit gives:

- old hole `0x2c6d`;
- minimum possible debt after one arbitrary cell replacement: 1;
- exactly 16 minimum-debt replacements;
- every one acts at position 6440, changing `0x806d` to one of the 16 values
  in the `0x0440..0x046d` family;
- every one installs `0x2c6d` and loses only `0xa86d`.

For a representative edit `p6440 := 0x0440`, the exhaustive reverse audit
again has minimum debt 1 and exactly 16 replacements, all at position 6440;
they restore `0xa86d` and lose `0x2c6d`.

Hence both basins contain the same exact minimal one-cell circuit

```text
0x2c6d <-> 0xa86d.
```

This is not yet the desired `0xc279 -> 0x2c6d` exchange: a universal optimum
must also collapse one of the two `0xc279` deadline groups, which necessarily
requires a wider rethreading/edit in this chronology.

## What is genuinely different

The words differ at 192 physical positions and in the witness multiplicities
of 415 targets.  Their unique-witness sets are:

```text
common                 50033
delete-p1 only           137
V/V only                 179
```

Their one-hole provider menus also differ (`27064` versus `26438` candidate
assignments), so they are genuinely different lower/compiler basins.
Nevertheless, the best literal exchange is identical.  Around the two
`0xc279` witnesses, the only private-target difference is that `0xc219` is
private at position 12828 in the delete-p1 basin but not in the V/V basin.
This may matter to a wider multi-cell search, but it does not change the
middle deadline defect.

## Scope

This audit does **not** show that every possible K16 length-12873 word has this
defect.  It shows that these two apparently different candidates share one
middle carrier chronology.  The new repeat-free K15 seed should therefore be
judged by whether its lifted K16 carrier changes this chronology—not merely by
whether its compiler cells differ.

Machine replay:

- `scratch/audit_k16_two_onehole_basin_exchange_20260731.py`
- `scratch/k16_two_onehole_basin_exchange_20260731.audit.json`

