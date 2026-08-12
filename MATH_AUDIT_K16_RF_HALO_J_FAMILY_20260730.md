# K16 cross-reflection RF-halo one-parameter family

Date: 2026-07-30

Status: **PASS_EXHAUSTIVE_TWO_EXACT_CARRIERS_UPPER5**.  This is a positive
carrier reduction and a complete theorem for the stated 5,722-member family;
it is not yet a universal K16 word.

## Family

Let `P=D^3 answers/k15.word`, let `S` be the repeat-free K15 carrier, and let
`R` be carrier3 with the entire 6,390-vertex large K15 component removed.  For
every `j=3,...,5724`, enumerate

```text
U_j = P[3:j] + S[3876:4544] + reverse(P[j:5725]) + R.
```

The RF segment begins

```text
P2,P1,P0,P6389,P6388,...
```

and ends `...,P5728,P5727,P5726,P5725`.  Thus every member preserves all
three parent-motif edges carrying the 22-cell Pascal diagonal.  Only two
local seams depend on `j`.

All 5,722 candidates have the exact `G=0` target multiset, capacity 32,176,
and all three required parent edges.  Every candidate was independently
checked for maximal-envelope reconstruction and all upper masks.

## Exact survivors

Exactly two values of `j` give a structurally exact generalized carrier:

| `j` | flats | upper holes | exact Hall deficiency |
|---:|:---|:---|---:|
| 990 | `6433,12869,12871` | `4e79,6f79,ca79,ea79,eb79` | 4 |
| 3959 | `6433,12869,12871` | `4e79,6f79,ca79,ea79,eb79` | **3** |

The five upper holes are two nested chains:

```text
4e79 < 6f79,
ca79 < ea79 < eb79.
```

The `j=3959` Hall witness is a 9-versus-6 shore.  Its three missing units are
the two unique K15 lower providers `0x2665` and `0x8000`, together with the
one-unit star excess based at `0x0665`.  Thus carrier3's Hall-22 obstruction
has been reduced to a three-unit seam/collar defect while retaining exact
middle geometry.

## Frozen artifacts

```text
scratch/k16_rf_halo_j_family_20260730/
  summary.tsv              SHA 22f380a55920d3b94795859f2b5a676b5826573dad53bb0ce35e8f91e31f66f2
  rank0_j990.targets       SHA 1ff3a096f4d139fa933acc3a749646092a4fd056d4a887974b1731863d4a232f
  rank1_j3959.targets      SHA edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
  j990.hall.txt            SHA 5983dccc877806c858f1e83ac5d7d94782394bc8c0e32a881548d03ccbc08a10
  j3959.hall.txt           SHA 1200d9abf5b7ebe2068b27941a92f7da80afef3470896414bdf6d3894ee3158c
  audit.json               SHA 004c1514e24845f2ede6ce0210b219f9a5f4ad9bb74b2da2a7e02adc34e233d3
```

Audit payload:

```text
b19ad28a079a13fa27057f93074db2c2cb69fece5e3dbc66017a6a36fda0cdcb
```

Independent audit source:

```text
scratch/audit_k16_rf_halo_j_family_20260730.py
SHA 320c5c45e1ef44ae73a7775a5151515e961d28ff9810ebf84661ceefa359dbe5
```

## Disposition

Use `j=3959` as the active seed.  The remaining move must preserve the local
K15 provider triple at the `j=3959` seam, create a private top singleton, and
install two seam grids serving the two nested upper chains.  Generic saved
circuits and the RF495 fibre are already closed and should not be revisited.
