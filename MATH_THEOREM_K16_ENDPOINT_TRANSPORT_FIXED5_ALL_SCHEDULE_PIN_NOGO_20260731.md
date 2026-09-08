# Exact all-schedule pin obstruction for the K16 endpoint-transport target

Date: 2026-07-31  
Status: solver-free fixed-order P/Q compiler no-go  
Scope: source-relative; no unrestricted K16 claim

## 1. Authenticated target and transport

The target order is

```text
scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word
SHA-256 9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b
```

It is a permutation of all `C(16,8)=12,870` rank-eight masks.  Starting from
the seed0-derived deficiency-four order of SHA `0a3a34c4...`, it is obtained
by two exact suffix reversals:

```text
cut 6173:  add q1 colour b8ce, remove the unique 3cce seam;
cut 11009: add q1 colour 3cce, remove one of two 3cea seams.
```

The final order is q1-complete.  Exhaustive contiguous-OR replay leaves only

```text
0x3ceb  (rank 10),
0xa9fe  (rank 11)
```

as upper holes.

## 2. Fixed maximum schedule

The maximum-area three-hole P/Q schedule is

```text
X = {12870,12871,12872},
Y = {0,1,8589}.
```

Its selected proper-prefix area is `30,023`.  The frequently quoted `30,032`
is the deliberately optimistic `area+9` bound.  Exact finite-path omitted-
start credits are only `3+2+1`, so the physical lower-cell count is `30,029`.
All envelopes are nonzero and all 12,870 middle rows replay exactly.

The exact individual-host graph has

```text
358,122 incidences,
matching 26,327 / 26,332,
deficiency 5,
zero hosts {0x29cc,0x38c6,0x8000,0x898d},
canonical Hall shore 30 targets / 25 cells.
```

The shore target-rank profile is `1^1 5^1 6^6 7^22`; its cell-length profile
is `1^3 2^18 3^4`.  Thus the displayed schedule is compiler-impossible even
before common-cap selection.

## 3. All-schedule singleton theorem

The fixed-schedule Hall defect is not the decisive statement.  Every
universal physical word must contain an interval with OR `0x8000`.  Because
physical letters are nonzero and `0x8000` has only one nonzero submask, every
letter in such an interval equals `0x8000`; in particular a one-cell
`0x8000` host exists.

The exact capped-envelope event DAG ranges over every monotone schedule with
three omitted starts, three omitted deadlines and maximum row depth three,
and over every position of that one-cell host.  It gives

```text
maximum selected area                  25,776
uniform omitted-start credit               9
optimistic total capacity              25,785 < 26,332
endpoint-exact total                    25,782
```

The maximizing replay uses

```text
X={6175,12871,12872}, Y={0,1,6141}, host=[6142,6142],
```

and has no zero cell or failed middle row.  Therefore no three-hole P/Q
schedule of this fixed target order can compile all 26,332 lower masks.  This
already closes the entire fixed-order compiler fibre independently of the
upper holes.

## 4. Two independent upper-pin obstructions

The missing upper masks give two further independent no-gos.  For an upper
mask `H`, let `rho(H)` be the longest consecutive run of target rows contained
in `H`.  If an `H` provider has physical length `L`, delete its final three
cells.  Among the remaining `L-3` start positions at most three are omitted;
the other `L-6` starts index consecutive target rows whose complete middle
intervals lie in the provider.  Hence

```text
L <= rho(H) + 6.
```

The literal facet census and exact capped-provider DPs give:

| mandatory host | contained rank-8 rows | `rho` | length bound | max selected area | optimistic capacity |
|---|---:|---:|---:|---:|---:|
| `0x3ceb` | 45 | 2 | 8 | 25,740 | 25,749 |
| `0xa9fe` | 165 | 4 | 10 | 25,743 | 25,752 |

Both totals are below 26,332.  The maximizing literal replays have no empty
cell, no failed middle row and the exact named provider OR.  Endpoint-exact
totals are 25,746 and 25,749.  Either upper requirement alone therefore also
closes the fixed target order; a simultaneous two-pin DP is unnecessary.

## 5. Exact repair boundary

The suffix transport itself is not unique.  After the first reroot, the
q1-completing second reroots `fixed_3`, `fixed_4`, and `fixed_6` owe only
`0xa9fe`; `fixed_5` owes `0x3ceb,0xa9fe`; and `fixed_7` owes
`0x2dcf,0xa9fe`.  Thus `0x3ceb` is not an invariant debt, while `0xa9fe` is
common to the audited q1-completing endpoint family.

For `fixed_5`, the terminal target is `0x38ea`, which is not a submask of
`0xa9fe`.  A further suffix reversal preserves all intervals internal to its
two pieces, and every genuinely new interval crosses the new seam and hence
contains the old terminal target.  Therefore one additional suffix reversal
cannot create an `0xa9fe` interval.  At least two more suffix reroots, or a
genuinely different interior/changed-value rethread, are necessary in this
transport topology.

Any successor search must protect more than q1 and scalar area: it must
recompute the full lower Hall graph and explicitly eliminate or host the
`0x8000` obstruction.  Upper completion alone cannot rescue the frozen order.

## 6. Frozen artifacts

```text
scratch/endpoint_transport_auth_20260731/audit_endpoint_transport_fixed5.py
  SHA 9866cd1da5f092e31381077a8cc424022fff0a7109ea9f72d153a5dcc63d7b25
scratch/endpoint_transport_auth_20260731/endpoint_transport_fixed5.audit.json
  SHA 48714159aa7405e10ce10af7bab2ce8ed25487ebd9ddf6ece7be93c4391a7d75
  payload 50204724f6ee794ff77c46f7f66890a8f43bfd5cbd145f3c5ebaeeb4c41012a3

scratch/ad_k16_fourfilter_endpoint_transport_maxpq_hall_20260731.audit.json
  SHA 807fa0c274aed16ae99cb3269da1c16a19749f9e55f6887df9cb60344ddd5bd1
  payload b134dd2efa74f9939694156fc7ef62d486c950febc1967cf27ffcd8d1dee945b

scratch/audit_k16_fourfilter_endpoint_host_dp_bundle_20260731.py
  SHA bb20209727ec93f65b4cec296c07246750e3532b9fc33f2dfd2ad37590db2f5c
scratch/k16_fourfilter_endpoint_host_dp_bundle_20260731.audit.json
  SHA 40560ed400eab4d27820366e21f0d13f23a866c78f44f579bbc1af07bddd705d
  payload f50ad74dc7398c4a6cdfadbbef9182da3c376a6b3ed3e9200b221ce517f70d4b

MATH_AUDIT_K16_ENDPOINT_TRANSPORT_UPPERPIN_CAPACITY_NOGO_20260731.md
  SHA 90f5163c286dff750cbab74ef8184faa91d6bb5b7e177ccb10cb6ced8aa60b0a
scratch/audit_endpoint_transport_upperpin_capacity_20260731.py
  SHA 9f4a5db10a55ce0834c672b0f8ba6a4d28cec4cf4ae7d6263ac9527bb04bc1df
scratch/endpoint_transport_upperpin_capacity_20260731.audit.json
  SHA 18e2dc5a7e20f6e0f79a4681517536fab9b4ed26e414a53976a42a7c2c2f6017
  payload e275ffa8373413c0a7cf85e193edbce69efa27084c4faea6eedafdc535427842

scratch/audit_k16_fourfilter_endpoint_transport_seam_algebra_20260731.py
  SHA 99753eaf2179255790b98a1f2456bc9cc036b1b133041c42485de98883fee02a
scratch/k16_fourfilter_endpoint_transport_seam_algebra_20260731.audit.json
  SHA a611aab1c3be6e3df9ab8c03b8db44bce83cd1307bda505e8afdee46a130e914
  payload fbfeda969a9669aa65138f331317fedb8aaa94561cb860160df7bd1e585a8c1d
```

The theorem is exact only for the authenticated target order and the
three-hole monotone P/Q compiler architecture.  It does not exclude other
target orders, other equality architectures, or unrestricted K16 equality.
