# Exact `0xa9ce` capacity obstruction and four-cut boundary for the seed0-derived K16 carrier

Date: 2026-07-31  
Status: solver-free fixed-order theorem and exact finite three/four-cut censuses  
Scope: source-relative; no unrestricted K16 no-go

## 1. Authenticated object and lineage

The target order studied here is

```text
scratch/k16_fourfilter_insert_aug_d2_1_targets_20260731.word
SHA-256 e483dae43cce3ca3e678958daab49f4237628f9b129df4f030fd83d83ffaa452
```

It contains all `C(16,8)=12,870` rank-eight masks exactly once.  Its filename
is historical and misleading: the separately frozen lineage audit identifies
its lower half with a seed0-derived parent, not the authenticated
four-filter/repeat-free parent.  Every statement below concerns this exact
`e483...` order only.

All adjacent pairs except the seam at position `6478` are Johnson edges.  The
exception is

```text
0xb84e -> 0x89ce,
```

and the missing rank-nine edge colours are exactly `0xa9ce` and `0xb8ce`.
The complete consecutive-upper deficit is

```text
{0xa9ce, 0xa9de, 0xa9fe, 0xb8ce, 0xb8cf}.
```

## 2. Maximum-area schedule and its Hall core

The exact three-hole maximal-envelope DP has maximum schedule

```text
X = {6479,10451,12872},
Y = {0,1,2}.
```

Its selected proper-prefix area is `29,799`.  The uniform omitted-start
credit gives the safe scalar upper bound `29,808`; the exact endpoint-aware
credit is only `3+3+1=7`, so the literal number of lower cells is `29,806`.
The span histogram is

```text
1^2420  2^3971  3^6479,
```

all envelopes are nonzero, and every middle row replays exactly.

For a lower target `S` and physical lower interval `C`, let `O_C` be the OR
of the maximal envelopes in `C`, and let `M_C` contain a coordinate whenever
some middle-row occurrence of that coordinate has every possible carrier in
`C`.  The exact individual-pin condition is

```text
S subset O_C,
M_C subset S,
and S meets every envelope in C.
```

The resulting graph has `345,822` incidences.  Its only zero-host targets are

```text
0x8000 and 0x898d.
```

Maximum matching is `26,249/26,332`, so the deficiency is `83`.  The canonical
alternating Hall shore has `635` targets and `552` cells.  Its left rank
profile is `1^1 6^95 7^539`; its right length profile is `1^278 2^274`.
Thus the displayed maximum-area schedule is compiler-impossible before any
SAT or common-cap assignment.

## 3. All-schedule `0xa9ce` obstruction

The fixed schedule failure is not the main theorem.  Every universal word
inducing this target order must contain a physical interval whose OR is the
missing upper mask

```text
H = 0xa9ce.
```

The nine rank-eight facets of `H` occur at target positions

```text
2129, 6479, 7033, 7238, 7578, 9330, 9530, 10447, 12336,
```

and no two are consecutive.

### Lemma 3.1 (provider length at most seven)

An `H`-provider interval cannot have eight or more physical cells.

Indeed, delete the final three positions of such an interval.  The remaining
five-position start window contains at least two selected starts because
there are only three start holes globally.  Those two starts are consecutive
in the selected-start order.  Their deadlines are at most three positions
later, so both complete middle intervals lie inside the `H` interval.  Both
consecutive middle targets would therefore be rank-eight facets of `H`,
contrary to the authenticated isolation list above.

### Theorem 3.2 (fixed-order compiler no-go)

Run the exact capped-envelope P/Q dynamic program for each possible
`H`-provider length `1..7`.  The state consists of the two hole counts, the
exact accumulated OR queue of active middle rows, the pin phase, and the
accumulated pin OR.  At a pinned position the maximal letter is the active
middle envelope intersected with `H`.  Completed pin state zero is absorbing.

The per-length maximum selected areas are

```text
length 1: 23320
length 2: 23320
length 3: 25828
length 4: 23323
length 5,6,7: infeasible.
```

The global optimum uses

```text
X = {6479,6480,12872},
Y = {0,1,2},
J_H = [6480,6482],
```

with capped letters `0xa04e,0x884e,0x89cc`, whose OR is `0xa9ce`.
Every middle row replays, so the bound is attained in the one-pin relaxation.

Nevertheless, even the deliberately generous omitted-start credit gives

```text
25828 + 9 = 25837 < 26332.
```

Therefore no monotone three-hole P/Q schedule of this fixed target order can
simultaneously realize `0xa9ce` and all `26,332` lower targets.  This closes
the entire fixed-order compiler fibre, not merely its maximum-area schedule.

Two independent implementations reproduce the optimum.  The independent
audit also gives the endpoint-exact count `25,828+7=25,835`.

## 4. Smallest connected q1 rethread topology

The q1 holes force any edge-exchange repair to add one facet edge of
`0xa9ce` and one facet edge of `0xb8ce`.

### Three cuts

The complete three-cut census enumerates

```text
36*36 = 1296 facet-edge pairs,
18432 endpoint/cut assignments,
716 assignments with three distinct cuts,
237 distinct endpoint configurations,
4 q1-complete ledgers.
```

Exactly one q1-complete ledger reconstructs to a connected path, at cuts

```text
{2128,6404,6478}.
```

It adds seams `39cf,b8ce,a9ce`; the first is a rank-ten, non-Johnson
auxiliary seam.  Its order has SHA
`1133c5d4c7aff3a9888125c9d34b5ac29b0463bb03d8d8fc34b9c5e745124a89`.
Complete upper replay leaves `{7bce,b8cf,b9ce,b9fe}`, and the exact all-P/Q
capacity is `25830+9=25839<26332`.  Thus the unique connected three-cut q1
completion exists, but is upper-incomplete and compiler-dead.

### Four cuts

For four cuts, after the two forced missing-colour edges, the four remaining
degree deficits have exactly three pairings.  The exhaustive census checks

```text
1296 facet-edge pairs,
18432 endpoint/cut assignments,
17714 four-distinct-cut assignments,
53142 remaining-endpoint pairings,
316 distinct q1 edge configurations.
```

Only four configurations preserve every q1 colour.  Exactly two reconstruct
to one connected Johnson path.  Their complete all-P/Q maximum scalar
capacities are respectively

```text
25837 and 24468,
```

both below `26,332`.  Each also retains upper holes

```text
{0x7bce,0xa9fe,0xb8cf,0xb9ce,0xb9fe}.
```

Thus no exact four-cut exchange in the enumerated all-q1/Johnson class can
reach the lower compiler gate.  A four-cut exchange with a non-q1 auxiliary
edge, five cuts, or a different carrier parent is not covered by this census.

## 5. Current frontier

The independently frozen seed0-derived reversal lead with target SHA
`0a3a34c4...` is already stronger than continuing this dead `e483...` order:
it has scalar capacity `30,107` and Hall deficiency four.  Two endpoint
reroots from it give the q1-complete order SHA `9142910f...`, with only upper
holes `{3ceb,a9fe}` and fixed-schedule Hall deficiency five.  The exact
all-schedule pin theorem closes that fixed order too: forcing either missing
upper target leaves optimistic capacity at most `25752<26332`.  A further
target-order braid is necessary.  None of these theorems closes the authentic
four-filter parent, another target order, or K16 equality globally.

## 6. Frozen artifacts

```text
scratch/threadD_k16_fourfilter_aug_d2_1_pq_hall_20260731.audit.json
  SHA e4c7e021a1e5582312ac0abb0d5d9806fdb0ca647db02983c792b555ff54fa5e
  payload 34c8c1bf9c06cd5282d3f99ee1394d447ded4ec6a15ef4f28400ab1bd7f2039a

MATH_THEOREM_K16_FOURFILTER_A9CE_CAPPED_PQ_FIXED_ORDER_NOGO_20260731.md
  SHA 6545738cb9b01f5a4daa8c1ab445a7536436c3dbe0ec9573b244aa0cc9bcb349
scratch/audit_k16_fourfilter_insert_aug_d2_1_static_hall_20260731.py
  SHA c22e77fb991a87716336f72e932f5bf2fb00c695beb2875b1ef4a963b14620a6
scratch/k16_fourfilter_insert_aug_d2_1_static_hall_20260731.audit.json
  SHA 25fe15941a06715e58eccc39e120294e63df4f143ae9bc400036158afc87cb4f
  payload 225c29c505107a1c5547d2c868cecb10bff07f747de10d6c9ca8ed00739cb0e4

scratch/audit_k16_fourfilter_a9ce_capacity_dp_20260731.py
  SHA 477fa465b3f6253f23311f7523db8da9408fa8218a04f99149f6075191a3cf78
scratch/k16_fourfilter_a9ce_capacity_dp_20260731.audit.json
  SHA 8140f6b6adec5a25d8050bc6d9d86854ebca503a3fdffed69eb5fe128dac4dfa
  payload 39a658bf1ae49024a455b224ace17c1af7683975c88b2ee7f337b47782a07230

scratch/audit_j3959_outer_context_k16_fourfilter_a9ce_capped_pq_dp_20260731.py
  SHA 1a1477530d82b43bfb42f14432bbc35617273475a61003b5b3474609df15f4f4
scratch/j3959_outer_context_k16_fourfilter_a9ce_capped_pq_dp_20260731/audit.json
  SHA ba31465e86e1896d3596891182c0868259337606b70d20eea2a89b2e617fbd1a
  payload c7ac8ccd70641ee2f0b40487039142faa673b0f49a19d82c46d9bd2e4e05f870

scratch/threadD_k16_fourfilter_q1_threecut_20260731.py
  SHA 3e78f7deb01b2a3128258586195f6dba046598a37114c5afa998c69e6771e584
scratch/threadD_k16_fourfilter_q1_threecut_20260731/census.audit.json
  SHA 0fd1f704d94311fd8fae42d56019252b1046af3894ffbd373b086611423f3cbd
  payload 9632099e860837a2f34c35b6a8805f0fdaff79aece23665944fb9ca58ea134fb

scratch/audit_k16_fourfilter_q1_fourcut_20260731.py
  SHA 4a49b0e1a9c24b8faa86387c1504da63620da35c5dcd7adfaaab06588f7af18c
scratch/k16_fourfilter_q1_fourcut_20260731/census.audit.json
  SHA 8625b481d53c77226dc9b8037271e8d25e4c9a6dd76bc65ad4bf7d2f3ec6e3ee
  payload ffbbd7857dbc3d442472eb5daefe3e5798fe3ebfde630bc154af8afa9597bfa9

scratch/audit_j3959_outer_context_k16_fourfilter_q1_fourcut_independent_20260731.py
  SHA 647ecdd807982253e52e0070667711f3523a72beb3e813d5c2e6d9f57eb7d0a8
scratch/j3959_outer_context_k16_fourfilter_q1_fourcut_independent_20260731/audit.json
  SHA 602d4535b63363b6086f2afa6bb78888ffe3e9b7be68b0ab27335203067b6f28
  payload 4350d0b68ce31bf0ecd8ac6d38d3da86b68b1739a6def40a47b5d643f8d2878f
```
