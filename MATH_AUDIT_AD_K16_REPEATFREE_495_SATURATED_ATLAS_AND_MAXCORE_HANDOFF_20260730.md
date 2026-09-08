# AD audit: repeat-free 4/9/5 inventory, saturated atlas, and maximal-core handoff

Date: 2026-07-30  
Status: **exact inventory replay and complete seed5-self semantic atlas; the
maximal-core solver is fail-closed and smoke-audited, but its bounded smoke is
UNKNOWN and gives no feasibility verdict**

## 1. Exact fibre

For ordered K15 parents `X,Y`, the 4/9/5 word is

```text
Q0(4) | X[6:6436] | Q1(9)
      | (0x8000 | Y[7:6432]) | Q2(5),
```

where the eighteen cells in `Q0,Q1,Q2` are free and all indices are
zero-based with half-open slices.  Its length is

```text
4 + 6430 + 9 + 6425 + 5 = 12873.
```

The two authenticated depth-two repeat-free parents used here are

```text
seed1  93484c945194c628b761f5b9a67111365d00fc1727d7e19839f07b74fee96d49
seed5  4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6.
```

## 2. Scoped inventory theorem

### Theorem 2.1

Among the materialized local and H100 4/9/5 runs found for literal ordered
pairs from `{seed1,seed5}`, the exact incumbent ledger is:

| pair | word SHA-256 | literal coverage | holes |
|---|---|---:|---|
| `(1,1)` | `b5a4c8d8190cdbb82cade5a56e5cad5e192e9bf3e1ee82ed6eb87becd8dc4fbe` | 65,531 | `0x43ea,0x77bc,0x83c8,0xb38c` |
| `(5,5)` | `9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6` | 65,532 | `0x18e7,0x3de7,0x9e20` |
| `(1,5)` | no 4/9/5 artifact found | -- | -- |
| `(5,1)` | no 4/9/5 artifact found | -- | -- |

Thus the best authenticated existing incumbent is the seed5 self-pair, with
three holes.

#### Proof

For each saved eighteen-cell ledger, reconstruct the displayed physical word.
Maintain the set of distinct OR values of intervals ending at the current
position; after appending cell `x`, replace it by

```text
{x} union {v OR x : v was an old ending value}.
```

The union over all positions is exactly the set of literal contiguous ORs.
Independent Python and C++ replays give the table.  The seed5 cell ledger has
SHA

```text
6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

and reconstructs the already authenticated RF495 word byte-for-byte.  The
full provenance and replay are frozen in

```text
MATH_AUDIT_AD_K16_REPEATFREE_495_EXISTING_RUN_INVENTORY_20260730.md
  SHA e57a7a6d5b34206800a35cd0ee0a192e55de702536284a070583d6a3e09e84ca
scratch/ad_k16_repeatfree_495_run_inventory_20260730/literal_replay.audit.json
  SHA 58f9c065c37d29dec19101d8e936a6a68c27b1893c5444f43289278bd3448401.
```

The absence statements are filesystem-inventory statements only.  In
particular, the similarly named `XS1_YRF` artifact has geometry 5/9/4, and
the `RS1` artifact uses reversed seed1.  Neither belongs in this table.

The H100 `ktri` files `kRF495.sol` and `kS1495.sol` are empty.  Their CNF
hashes are respectively

```text
2fc9333bc069a60ad85d39a409f35725e1941b66765407cf9b3276ffeff31e7a
67b074bc2ff9232af5dfa4588b9980c5e3254f14114ee7370c430eebfd384d53.
```

Empty solution files give no SAT or UNSAT verdict.

## 3. Complete saturated seed5 atlas

Freeze the seed5 self-pair in

```text
scratch/k16_triwindow_rf495_repeatfree_frozen_atlas_20260730/.
```

Its free physical positions are

```text
0,1,2,3,
6434,6435,6436,6437,6438,6439,6440,6441,6442,
12868,12869,12870,12871,12872.
```

Let `A=seed5[6:6436]` and
`B=0x8000 | seed5[7:6432]`.  Let `C_fix` be the union of the literal interval
OR sets wholly inside `A` or wholly inside `B`, and put

```text
R = {1,...,0xffff} minus C_fix.
```

### Theorem 3.1 (exact saturated atlas)

The frozen atlas has:

```text
fixed-body covered nonzero masks        65465
residual targets |R|                       70
unlabelled semantic shapes                395
target-labelled semantic providers       6081
potential literal provider intervals     6089
semantic omitted / extra providers        0 / 0
incumbent covered nonzero masks          65532
incumbent holes             0x18e7,0x3de7,0x9e20.
```

The exact machine authority is

```text
host_atlas.audit.json
  SHA     024b67240db0a98f7c18c43e1c87a85af2d67624c50878e7aa80474f11f95194
  payload f33588e336ee019f665aeec046d79be803b1457f22acec645c6f3215109f7970
residual_witness_incidence.tsv
  SHA     a3ca5b14a5e6286cbcb96e6ca3c827979a525f697eabf6f0704c4fcde982113c.
```

#### Proof

First replay all intervals wholly inside the two fixed bodies, using the
ending-OR recurrence from Theorem 2.1.  This gives `C_fix` and the displayed
70-mask complement.

For each residual target `T`, scan every physical interval meeting at least
one free cell.  Treat free cells as unassigned and let `F` be the OR of its
fixed cells and `Q` its ordered set of free positions.  Stop a rightward scan
only when `F` gains a bit outside `T`; monotonicity makes all later endpoints
impossible.  Retain precisely `F subseteq T`, then collapse literal intervals
by the target-labelled semantic key `(T,F,Q)`.

This no-cutoff scan gives 6,089 literal rows and 6,081 distinct keys.  Direct
comparison with every witness in the frozen `model.map.json`, separately for
each `T`, has empty set difference in both directions.  Every stored
representative interval independently reconstructs its recorded `F,Q`.
Finally, literal replay of the assembled incumbent gives the three displayed
holes.  No solver assignment or cutoff-completeness assumption enters this
proof.

## 4. Exact same-Q quotient

There are exactly

```text
C(5,2) + C(10,2) + C(6,2) = 10+45+15 = 70
```

nonempty contiguous free-position sets `Q` in windows of sizes 4,9,5.

### Theorem 4.1 (unique greatest fixed OR)

For every residual target `T` and every one of these seventy `Q`, the raw
provider class with fixed `(T,Q)` has a unique greatest fixed OR.  Replacing
the class by that row is exact.  Hence the reduced atlas has exactly

```text
70 * 70 = 4900
```

rows; 1,181 of the 6,081 raw rows are dominated.

#### Proof

For a fixed `Q`, legal shore extensions form monotone prefix/suffix OR chains.
If `Q` has two shores, take the union of the greatest legal state on each
shore.  It is still a submask of `T` and contains every other legal fixed OR.
After equal `(F,Q)` plateaux are collapsed, the greatest row is unique.

All rows in one class impose the same cell caps `x_p subseteq T` for
`p in Q`.  Increasing `F` only decreases the demanded variable bits
`T minus F`; therefore the greatest row dominates every smaller row.
Conversely it is itself one of the raw physical rows.  The frozen certificate
lists every class, its raw size, all dominated witness IDs, and a class digest:

```text
residual_maximal_provider_incidence.tsv
  SHA 1be45c403964377ac1406a4d210f0cd66115c78a533109c55705afc64bf7741c.
```

Independent replay finds 70 classes for every target, 4,900 total rows, and
zero dominance-certificate failures.

## 5. Maximal-core theorem and executable handoff

Choose one provider `(T,F_T,Q_T)` for each residual target and define, for
every free cell `p`,

```text
K_p = intersection {T : p in Q_T},
```

with empty intersection `0xffff`.

### Theorem 5.1 (integral maximal-core criterion)

The selected providers have simultaneous nonzero literal cell values if and
only if

```text
K_p != 0                                             for every used p,
F_T OR (OR_{p in Q_T} K_p) = T                      for every residual T.
```

When these conditions hold, `x_p=K_p` is a literal integral realization.

#### Proof

Any realizing value at `p` is a submask of every selected target incident
with `p`, hence a submask of `K_p`.  Nonzeroness and the displayed OR
equalities are therefore necessary.  Conversely assigning `K_p` satisfies
all target caps, is nonzero by hypothesis, and gives every selected target by
the second equality.

The full-domain executable implementing this criterion is

```text
scratch/search_ad_k16_rf495_maximal_core_provider_20260730.cpp
  SHA a60bd838cc10ab9d025d3d18b8c70c22d07967ab4c7f177432c6039292adb110.
```

It accepts the 6,081-row raw incidence, independently reconstructs the exact
4,900-row same-Q quotient, starts with all 4,900 choices, and has no seed4
hole-pair root, displacement budget, or S4 frontier assertion.

The independent verifier is

```text
scratch/audit_ad_k16_rf495_frozen_atlas_and_provider_solver_20260730.py
  SHA e7c9ab52b81816d973dbf576343e13a59f90d5afb1ceec9abdf6eb0fec1163c2.
```

It computes the real input hashes rather than trusting the strings echoed by
the solver.  For a future SAT report it reconstructs the eighteen maximal
cores, checks every selected literal representative, and replays all 65,535
nonzero masks.  For a future UNSAT report it checks the complete custom
branch proof: each branch must list every currently viable provider, each
leaf must have an empty target domain, and each memo reference must point to
an earlier byte-identical semantic state.

The current one-node smoke has status `UNKNOWN`; it proves only that parsing,
dominance reduction, and the full root domain agree:

```text
maximal_core_smoke.report.json
  SHA f3ce406f2dce4f945fcd405f9c944de0316c89823a2edd8fcc4841eea9c5869f
independent audit
  SHA     e20adfaf63d3abe4edc80188e4c86716ac5fe04d4471ce7cb67f67aec7542706
  payload 0b1cb1e6ec16806241a012963435fbb3d433fd26d7c48b0a534d4812a92825c8.
```

`UNKNOWN` is not a feasibility verdict.

## 6. Exact boundary

This work supplies the requested genuinely repeat-free perfect-parent basin
and a complete target-labelled solver handoff.  It does not prove that the
three-hole incumbent is optimal in its 4/9/5 fibre, does not exclude absent
mixed-pair runs, and does not solve the maximal-core choice system.  No K16
bound changes.
