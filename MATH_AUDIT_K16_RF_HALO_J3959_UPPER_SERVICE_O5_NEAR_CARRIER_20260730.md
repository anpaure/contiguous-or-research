# Exact upper-service O5 census at the Hall-3 RF-halo carrier

## Forced services

Starting from the authenticated `j=3959` RF-halo carrier, this census forces
the three directed new joins

```text
ca71 -> 4a79,
4a79 -> 4e39,
6879 -> Y,       where 6879 | Y = 6f79.
```

The intact prefix `eb60,ea61,ca71` followed by `4a79,4e39,4d39` realizes the
entire nested upper chain `ca79<ea79<eb79` and `4e79`.  The third join realizes
`6f79` while retaining the lower parent prefix through `6879`.

Five cuts split the movable interval into four blocks.  All
`4! * 2^4 = 384` signed block patterns were generated; exactly 208 restore no
old cut edge and are provenance-irreducible.  All injections of the three
services into the five new joins and all 56 choices of `Y` were imposed.

The exact partial-cut census is

```text
fully pinned descriptors: 182
one-free-cut descriptors:    4
two-free-cut descriptors:    0
three-free-cut descriptors:  0
```

Expanding the four one-free-cut intervals and deduplicating gives exactly
16,680 O5 candidates.  Of these 16,678 have the exact three-flat profile and
sufficient scalar capacity.

## Result: a four-equation near-carrier

No candidate has exact maximal-envelope/middle reconstruction.  However, the
minimum structural defect is only four bad replay rows, with no empty
envelope cells.  It is achieved by four representations (two distinct cut
positions, each with two equivalent signed patterns).  The best one is

```text
pattern 163
cuts    3958,3959,4619,4935,12825
flats   5456,12869,12871
capacity 31199
empty envelope cells 0
bad replay rows      4
remaining upper holes 0f3d,6a79,6b79
```

Its exact four replay defects are

| row | carrier mask | replay | missing bit |
|---:|---:|---:|---:|
| 3958 | `6879` | `2879` | `4000` |
| 3959 | `0f39` | `0e39` | `0100` |
| 3960 | `0f33` | `0e33` | `0100` |
| 12165 | `0d3d` | `0d2d` | `0010` |

The only five new seams are

```text
3958:  6879 -> 0f39    (union 6f79)
11848: ca71 -> 4a79    (union ca79)
11849: 4a79 -> 4e39    (union 4e79)
12165: 0d3d -> 4f29
12825: 6a71 -> 4679
```

Thus the canonical upper-service braid is not merely “almost valid” by a
scalar score: it fails in two sharply localized coordinate runs.

## Sharp buffer consequence

The first bad seam lies in the depth-three sector.  Any fixed-target repair
there needs three consecutive buffer rows after `6879`: all three must carry
bit `4000`, and the last two must also carry bit `0100`.  This extends the
`4000` and `0100` runs through `0f39,0f33` to the required length four.

The second bad seam lies after the first flat, at depth two.  It needs two
consecutive buffer rows after `0d3d`, both carrying bit `0010`, to reach the
required length three.

Therefore one- or two-buffer repair is impossible for this fixed target.
The sharp next family is relocation of an existing contiguous length-three
segment and a contiguous length-two segment, in both orientations, with
their source gaps reconnected.  It must simultaneously restore the three
residual upper masks `0f3d,6a79,6b79`.

## Artifacts

```text
scratch/search_k16_j3959_upper_service_o5_20260730.cpp
SHA-256 7e301d805a5b4554254753f931107d95d5b6027b3a988c4a5636934436770152

scratch/k16_rf_halo_j3959_upper_o5_20260730/result.tsv
SHA-256 97af0b7adf5b1ce8be2b1b14bfacc690a000d213de22f20a66894a3007c78a9c

scratch/k16_rf_halo_j3959_upper_o5_20260730/run.stdout
SHA-256 7f9dff4ca200920f2362d341d2a9a4019dc0ffdf6d6f460868acd159beb4f23e

scratch/k16_rf_halo_j3959_upper_o5_20260730/best.targets
SHA-256 94ce24bb6dd4f8236f8565941d3aeea55caec0d1a3abb31b0419c8cd78282516

scratch/k16_rf_halo_j3959_upper_o5_20260730/best.targets.envelope
SHA-256 a489b9b98e8765347fbdd42332f29cd5ca0217eb7ea49a4c000ccdd32c40d202
```

The H100 executable had SHA-256
`d597ff53bee3fa1c2238031e6cf4503a222a7597a6d06832c56cd9fb4a2fdff9`.

