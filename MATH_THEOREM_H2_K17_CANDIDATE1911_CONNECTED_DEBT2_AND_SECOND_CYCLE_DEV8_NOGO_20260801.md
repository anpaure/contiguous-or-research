# K17 dev5 candidate 1911: connected debt-two factor and dev8 second-cycle gate

Date: 2026-08-01  
Lane: H2 independent replay  
Status: **central factor GO; one-side simple second-cycle lengths 3--8 NO-GO. No K17 word claim.**

## 1. Connected factor

The frozen factor

```text
scratch/k17_complement_dual_shell_dev5_20260801/
  seed17931.minimum_debt_assignment_cycle.factor.tsv
SHA-256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

independently replays as follows.

```text
D/H incidence matchings:       1430 / 1430, perfect and edge-disjoint
changed from seed:              D 0 rows, H 8 owner rows
quotient owner factor:          one 1430-cycle
voltage:                        9 mod 17
physical lift:                  one 24310-cycle, all owners distinct
rank-8 edge palette:            1430 / 1430
upper rank-10 turn palette:     1144 / 1144
lower rank-7 turn palette:      1142 / 1144
lower holes:                    0x00e0f, 0x01547
```

The lower load histogram is `1^874 2^249 3^18 4^1`; the upper histogram is
`1^878 2^247 3^18 4^1`.

This is not resident: literal physical replay has 1,173 positive runs of
length two and 3,179 of length three (`4352` short runs total).  Thus the
result solves central topology, rank-eight and upper-q1, but not physical
residence or the full compiler.

Independent artifacts:

```text
scratch/audit_h2_k17_candidate1911_connected_factor_20260801.py
SHA-256 1def852a7baa644a5da1a52f92ac63f4ab08e7e0cbb405872261608658aa8c69

scratch/h2_k17_candidate1911_connected_factor_20260801.audit.json
SHA-256 906eca150fed88d5f5562de4e22f2a38143ec7c3666a24858b20ee036097d822
```

## 2. Exact bounded second-cycle class

Starting from this connected factor, dev8 enumerates one additional simple
assignment cycle

* on `D` alone or `H` alone;
* of length `3` through `8` selected matching rows; and
* containing direct new providers for both missing lower targets.

The last condition loses no solution in this class: a final factor covering
an absent lower target must contain a changed owner incidence whose new lower
turn is that target.  Anchoring every provider of the first hole, following
the displaced-owner matching permutation, retaining all parallel phase
incidences, and closing every simple cycle therefore enumerates the class
completely.

The exact census is:

| side/length | targeted | connected, nonzero voltage | minimum total holes |
|---|---:|---:|---:|
| H5 | 1 | 0 | -- |
| H7 | 21 | 2 | 7 |
| H8 | 130 | 0 | -- |
| D6 | 1 | 0 | -- |
| D7 | 16 | 5 | 2 |
| D8 | 68 | 0 | -- |

All other side/length rows have zero targeted cycles.  There are zero
connected nonzero-voltage candidates with both palettes complete.

The best residual is D-side length seven, candidate 29:

```text
voltage:      3 mod 17
upper hole:   0x0355f
lower hole:   0x0062f
total debt:   2
```

Thus the bounded move can transport the debt but does not reduce it.

## 3. Frozen computation

Remote source:

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/
  dual_splice_dev8_20260801
```

Local frozen bundle:

```text
scratch/h2_k17_candidate1911_second_cycle_dev8_20260801/
```

Key hashes:

| artifact | SHA-256 |
|---|---|
| source | `0d42d483b2fc8def4c1263b1d2bb3a45bf90520c57d81df220fa6cdf5c487704` |
| H100 binary | `45c6808c4023c0815ab5d6a1e05df13df79331e66af6ca4833ab8d7fc6c54e77` |
| source factor | `c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587` |
| second-cycle TSV | `3a575bbf28e5afe54e229b8c27af5133f223e49049c6ebe2b8dd6419ddf9c98e` |
| second-cycle summary | `2e0501b905b12149fa25ea76f0879dbefaa1d554f9b140059b29ac838cfbb3b9` |
| run audit | `2a0279f1bda1718cf3a5d594edf82f0f80391228ba08ada4426cb70276b342c4` |
| minimum-debt factor | `aed64bc32992d65f77c4a0bcbcf9189f88d3d835295df517e8ca29f46595fb8a` |

The H100 process exited `0`.  The independent verifier replayed all 237
emitted edge-disjoint cycles from literal incidence IDs and reproduced every
component, voltage and palette row:

```text
scratch/audit_h2_k17_candidate1911_second_cycle_dev8_20260801.py
scratch/h2_k17_candidate1911_second_cycle_dev8_20260801.audit.json
```

## 4. Scope

The no-go covers exactly one simple cycle on one matching shore through
length eight.  Mixed `D/H` changes, two assignment cycles, nonsimple
alternating circuits, and length at least nine remain open.  Residence,
ranks at least eleven, source/deep-shadow witnesses, opening, common cap and
compiler constraints are separate.  Neither this bounded no-go nor the
positive central factor proves or refutes global K17 equality.
