# K16 fixed-75 C106: three-target cycle-slack obstruction and conditioned floor 107

Date: 2026-07-30  
Lane: L, fixed-`F75` residual cycle packets  
Status: **proved for integral selections containing the authenticated `F75`; no global C106 conclusion**

## 0. Verdict

No balanced capacity-one count-106 selection in the frozen K16 seam catalogue
can contain the authenticated fixed block `F75` and service all 93 frozen
targets. Equivalently, `F75` has no 31-seam C106 completion in any of the
`4^5=1024` five-lock normal-form signatures.

The decisive obstruction uses only the three residual price-four targets

```text
T = {46811, 56173, 60854}.
```

In the exact clean graph, every directed closed walk touching one specified
member of `T` has direct slack at least three, while no directed closed walk
of total slack at most five touches two distinct members of `T`. An integral
balanced circulation of total slack at most five therefore cannot service all
three targets.

Thus the source-relative count floor on this fixed face is

```text
C >= 107, conditioned on retaining F75.
```

This is not an unrestricted K16 floor 107 and says nothing about a count-106
selection that replaces or recombines `F75`.

## 1. Frozen face and the 1024 signatures

The raw ledger and direct certificate are

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
SHA256 a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2
```

The fixed-block audit is

```text
scratch/l_k16_d4_cycle_blocks_20260730.audit.json
SHA256 b9dca4325deac03fa8575ad755db2cf54b777f1dd8811009d2e35f25e5eaa7a8
```

`F75` is a tight balanced capacity-one union of three `C15` blocks and one
`C30` block. It occupies 75 ports and services 60 targets exactly once. The
33 residual targets have price profile

```text
1^15 2^15 4^3
```

and the three price-four residual targets are exactly `T`.

The authenticated fixed-face atlas is

```text
scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json
SHA256 a08a6d8f42b9e9e70b0e7278edfd5492032eb7733a3710c53e821101597a7125
```

For every hypothetical integral C106 completion, the five-lock normal form
chooses at each lock either one unit of total direct slack or one of three
residual price-one targets to repeat. Hence:

- all repeats occur among the fifteen residual price-one targets;
- every target already serviced by `F75` retains multiplicity one;
- every member of `T` has residual demand exactly one;
- total direct slack is an integer between zero and five.

The atlas counts by total slack are

```text
0:243, 1:405, 2:270, 3:90, 4:15, 5:1.
```

## 2. Exact clean-graph lemma

Let `X` be the residual circulation of a hypothetical fixed-`F75` C106
selection. Every selected residual seam lies in the following clean graph.

1. Its endpoints avoid all 75 `F75` ports, because those ports are already
   saturated at incoming and outgoing capacity one.
2. It hits no `F75`-serviced target, because the exact normal form permits
   repeats only at selected residual price-one targets.
3. Its direct slack is at most five, because all seam slacks are nonnegative
   integers and the whole residual circulation has total slack at most five.

Raw replay leaves exactly 205,694 arcs, with slack histogram

```text
slack 0: 38,935
slack 1: 32,280
slack 2: 73,713
slack 3: 29,468
slack 4: 29,817
slack 5:  1,481
```

The deletions remove 2,550 fixed-port arcs, 3,273 fixed-target-hit arcs, and
87 arcs of slack above five. This proves that every directed cycle of `X` is
wholly contained in the displayed clean graph. No heuristic support
restriction is used.

## 3. Exact marked closed-walk census

The clean graph has exactly 180 seams hitting `T`, sixty for each target.
Every such seam hits exactly one member of `T`. Their slack profile is

```text
46811: 51 tight, 9 slack-one
56173: 54 tight, 6 slack-one
60854: 53 tight, 7 slack-one.
```

For a clean directed path, record a three-bit mask saying which members of
`T` it touches. The verifier runs exact Dijkstra on the expanded state graph

```text
(port, T-mask), 12870 * 8 = 102960 states.
```

For every marked provider seam `e:u->v`, and for every exact path mask, it
computes the minimum slack of a return path from `v` to `u`. Adding `e`
prices a closed walk with the union mask. There are 150 distinct provider
heads, 180 marked provider occurrences, and 1,440 persisted provider/return
mask prices.

The exhaustive cost table, truncated at budget five, is

| `T` mask | marked targets | minimum closed-walk slack |
|---|---|---:|
| `001` | `46811` | 3 |
| `010` | `56173` | 3 |
| `100` | `60854` | 3 |
| `011` | first pair | greater than 5 |
| `101` | second pair | greater than 5 |
| `110` | third pair | greater than 5 |
| `111` | all three | greater than 5 |

The stored integer `6` is a fail-closed sentinel meaning “no walk of cost at
most five”; it is not an assertion that the unrestricted exact minimum is
six.

Completeness is elementary. Any directed closed walk touching `T` contains a
marked provider occurrence `e`. Cutting the walk just after `e` leaves a
directed return path from `head(e)` to `tail(e)`, with exactly one of the eight
recorded union masks. Conversely, adjoining any recorded return path to its
marked seam gives a directed closed walk. Thus the 180-by-8 table loses no
closed walk of slack at most five.

The three singleton lower bounds are attained by explicit cost-three closed
walks:

```text
46811: 117908,192438,66749,207530,209317
56173: 147007,173135,95845,207729,208837
60854: 88808,177906,146769,207327,208895
```

The audit replays endpoint balance, target mask, and total slack for each
witness. For every pair and for the triple it separately checks all 180
marked occurrences and all eight return masks, including every superset mask,
and freezes zero survivors at cost at most five.

## 4. Circulation obstruction

Every nonnegative integral balanced directed flow decomposes into directed
closed walks. This remains true after relaxing packet count, residual port
capacity, binarity to arbitrary nonnegative integer multiplicities, and all
service rows except the three rows in `T`.

Suppose such a circulation has total slack at most five and services all
three members of `T`.

- No one closed walk can contain two distinct members of `T`, by the exact
  pair census.
- Therefore at least three marked closed walks are needed.
- Each marked closed walk has slack at least three, by the singleton census.

Their total slack is at least nine, contradicting the budget five. Hence no
such integral circulation exists.

## 5. Fixed-face floor theorem

**Theorem 5.1.** There is no integral balanced capacity-one count-106
selection in the frozen K16 seam catalogue which contains `F75` and services
all 93 frozen targets.

**Proof.** Subtracting the balanced `F75` block leaves a balanced residual
circulation. Section 1 places the candidate in one of the 1,024 exact
normal-form signatures, so it has total slack at most five, zero residual
demand on fixed targets, and demand one on every member of `T`. Section 2
puts all its cycles in the exact clean graph. Section 4 then gives a
contradiction. QED.

The theorem proves the fixed-face source-relative floor `C>=107`. It does not
construct a count-107 packet.

## 6. Structural corner refinements

The broad theorem subsumes the earlier corner searches, but their literal
cycle structure remains useful for construction at count 107.

### 6.1 All-repeat corner: 243 signatures

At total slack zero, the clean tight graph has 38,935 arcs and 12,816 SCCs.
Its entire cyclic core consists of exactly

```text
5 C3 + C45,
```

with 60 cycle-eligible arcs. Every component is replayed as a literal directed
simple cycle. None of the six cycle columns services any member of `T`.
Consequently all 243 exact all-repeat signature faces are infeasible even
after relaxing residual capacity, binarity, and count to nonnegative
fractional cycle coefficients. Independently, 31 is not a subset sum of
`3,3,3,3,3,45`.

### 6.2 One-slack layer: 405 signatures

There are exactly fifteen slack-one seams with a tight return path. They are
chords of the unique tight `C45`; every chord plus its unique simple tight
return segment is a length-29 portal macro. The only disjoint all-tight
fillers are subsets of the five `C3` blocks, giving exact attainable packet
counts

```text
29,32,35,38,41,44,
```

never 31. The full tight-plus-portal cyclic core has 75 arcs, and all 75 have
zero incidence on `T`. Thus all 405 one-slack signatures fail by two
independent structural obstructions.

## 7. Reproduction and hashes

### 7.1 All-1024 integral floor-107 replay

```text
python3 scratch/audit_l_k16_fixed75_c106_price4_closed_walk_floor107_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json \
  --d4-audit scratch/l_k16_d4_cycle_blocks_20260730.audit.json \
  --atlas scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json \
  --output NEW_FIXED75_C106_FLOOR107_AUDIT.json
```

```text
driver
  scratch/audit_l_k16_fixed75_c106_price4_closed_walk_floor107_20260730.py
  SHA256 8e2da3e326666255f21fbe2312b3c9e6ce97f22d96893147fc29175f20e3f1b5

frozen v2 audit
  scratch/l_k16_fixed75_c106_price4_closed_walk_floor107_v2_20260730.audit.json
  SHA256 58915e7da037ebba28e230dcd71e3084d1c4aacbfec80c5fc024128943550d7f
  payload 6451cab631029429efb2548cd63ccbd3ec3417f6bf5aa0d383946aed413399b9
```

The replay uses only the Python standard library and completed locally in
about two seconds.

### 7.2 All-repeat cycle columns

```text
driver
  scratch/audit_l_k16_fixed75_c106_r0_cycle_columns_20260730.py
  SHA256 86f1a53e421d1121bae401db1951c926f1b72c9e3d90342e791631d4d18bf0a1

audit
  scratch/l_k16_fixed75_c106_r0_cycle_columns_20260730.audit.json
  SHA256 1161f4ddb730ca371d2bc224ed97f315420b580f3bdb875e6021176a97fd4dc0
  payload a35efec6613f9b45ad255913c63ce6ac616ea15a2d3f39d649e8304657e7dd11
```

An independent raw SCC replay agrees:

```text
scratch/l_k16_fixed75_c106_s0_tight_scc_20260730.audit.json
SHA256 d0a08038b98523a580321b34771449db8f4ed3a635bd3a985cbbc9fe2abe3331
payload fe69ce1f0f7539328485965802b5827598a83e1c53002884bd48be18d249d88b
```

### 7.3 One-slack portal macros

```text
driver
  scratch/audit_l_k16_fixed75_c106_s1_portal_cycle_columns_20260730.py
  SHA256 a3862bb3fa013371f251731cafc33c770cd4acce8a3c9bb875fb7098a51bfd37

standalone v2 audit
  scratch/l_k16_fixed75_c106_s1_portal_cycle_columns_v2_20260730.audit.json
  SHA256 559f18c9b4d091b43e8c059b0cbaa1cb46d46f3d66fad04fc0fea7441746e590
  payload 62d23edaeef9e138466c85c7ec10bec41d79b8b5303d135abede1e36ab2f4bc7
```

The v2 replay has no CP/SAT dependency. An aggregate CP result exists only as
a negative control and is not read by the frozen standalone run.

## 8. Audit boundary

The all-1024 theorem is integral. It does not claim infeasibility of an
unbranched fractional C106 model or of fractional flows that use a small
coefficient on a seam of slack above five. The all-repeat refinement is
fractional only after conditioning on one exact target-multiplicity signature
face, which justifies deleting fixed-target hits.

No q1, separation, reverse-edge, residence, survivor, deeper-shadow,
all-depth, or compiler rows are used. Their omission strengthens the no-go on
the fixed face. No candidate exists, so no canonical full-candidate replay is
needed or modified.

