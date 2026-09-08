# Audit of existing repeat-free-parent K16 4/9/5 tri-window runs

**Date:** 2026-07-30  
**Lane:** AD, independent replay/inventory  
**Status:** exact literal replay of every materialized 4/9/5 incumbent found for
the ordered parent pairs in `{seed1,seed5}`; no search-optimality claim

## 1. Exact scope

The physical layout audited here is

```text
Q0(4) | X[6:6436] | Q1(9) | (0x8000 | Y[7:6432]) | Q2(5),
```

of total length 12,873.  The authenticated repeat-free parents are

```text
seed1  93484c945194c628b761f5b9a67111365d00fc1727d7e19839f07b74fee96d49
seed5  4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

where `K15_REPEATFREE_SEED.word` is byte-identical to `k15seed_5.word`.

This is a read-only inventory of the local repository and the surviving H100
`/dev/shm` namespace on 2026-07-30.  It proves the literal hole counts of the
saved incumbents.  It does **not** prove that no deleted historical run once
existed, nor that either heuristic incumbent is optimal in its fibre.

## 2. H100 run inventory

Exactly the following materialized 4/9/5 implicit-search incumbents were found
with both parents in `{seed1,seed5}`.

### 2.1 Ordered pair `(seed5,seed5)`

The base run

```text
/dev/shm/tri_implicit_RF_495
```

and all sixteen seeded continuations

```text
/dev/shm/tri_implicit_RF_495_seed3901 ... seed3908
/dev/shm/tri_implicit_RF_495_joint6901 ... joint6908
```

have the same saved cell ledger, SHA-256

```text
6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c.
```

The base log SHA is

```text
4399aa303a7418ae602ee563187def7cc12e7c317cab66573bff5d3548d55d6e.
```

Its last improving record says `score=3`; every continuation starts from and
retains that same score-three ledger.  The logs end in periodic `STATUS`
records, not a proof-producing terminal verdict.

### 2.2 Ordered pair `(seed1,seed1)`

The one found implicit run is

```text
/dev/shm/tri_implicit_S1_495.
```

Its cell-ledger SHA is

```text
29175fe18e5da68c61fd78196840c21f84661dc9788d8a44e092adb503fc9833,
```

and its log SHA is

```text
9179d0d2c210d135d4301ef4e401b3465facfcbae14419fd90d13414b49360ec.
```

The last improving record says `score=4`; again the log ends in `STATUS`, not
an optimality or infeasibility certificate.

### 2.3 Cross pairs

No materialized **4/9/5** run was found for `(seed1,seed5)` or
`(seed5,seed1)`.  The similarly named H100 artefact

```text
/dev/shm/tri_implicit_XS1_YRF
```

is not a counterexample to this statement: its associated variable map has
free positions

```text
0..4, 6435..6443, 12869..12872,
```

so its partition is exactly **5/9/4**.  No `XRF_YS1` run directory or
catalogue entry was found.  `tri_implicit_RS1_495` uses the reversed seed1
word of SHA

```text
bb02c9cdf498a0e6af3a88be63ede29716fbc3644aa3275fa9375faaf58d9662,
```

and is therefore a distinct oriented parent, not the literal ordered pair
requested here.

## 3. The H100 `ktri` artefacts carry no solver verdict

The two relevant fixed CNFs are:

| pair | CNF SHA-256 | emit SHA-256 | map SHA-256 |
|---|---|---|---|
| `(5,5)` `kRF495` | `2fc9333bc069a60ad85d39a409f35725e1941b66765407cf9b3276ffeff31e7a` | `69434db5bbaf63118deef6cec8fbc0374a83c1bd198183c573cd696068e62bf6` | `1c8f7c1e5a010adaf63f0c681d54f4150002f9d2d6f5cf19443606e961b69e00` |
| `(1,1)` `kS1495` | `67b074bc2ff9232af5dfa4588b9980c5e3254f14114ee7370c430eebfd384d53` | `c0f6c218936880cf9c921ee52285951731447142900f7162fe72924fd4d223a6` | `1c8f7c1e5a010adaf63f0c681d54f4150002f9d2d6f5cf19443606e961b69e00` |

Both corresponding `.sol` files have size zero and SHA
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The independent `/dev/shm/tri_dimacs_S1_495` CaDiCaL output and error files
are also empty.  Hence none of these files is SAT, UNSAT, DRAT, or LRAT
evidence.

## 4. Independent literal replay theorem

### Theorem 4.1

Reconstructing the complete physical words from the authenticated parents
and the saved eighteen cell values, then directly enumerating contiguous ORs
without consulting the tri-window shape catalogue, gives:

| pair | physical-word SHA-256 | covered | exact holes |
|---|---|---:|---|
| `(seed1,seed1)` | `b5a4c8d8190cdbb82cade5a56e5cad5e192e9bf3e1ee82ed6eb87becd8dc4fbe` | 65,531 | `0x43ea,0x77bc,0x83c8,0xb38c` |
| `(seed5,seed5)` | `9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6` | 65,532 | `0x18e7,0x3de7,0x9e20` |

Thus the best authenticated literal incumbent among the existing requested
4/9/5 runs is the `(seed5,seed5)` RF495 word, with exactly three holes.

### Proof

The verifier constructs

```text
cells[0:4]
+ X[6:6436]
+ cells[4:13]
+ [0x8000 | y : y in Y[7:6432]]
+ cells[13:18].
```

For every left endpoint it extends the right endpoint, marks the current OR,
and stops only after the OR becomes `0xffff`.  It then lists every unmarked
nonzero 16-bit mask.  A structurally separate C++ verifier performs the same
literal enumeration on the emitted words and returns the same counts and
hole lists.  In particular, the seed5 word is byte-identical to the already
published RF495 three-hole word.  This proves the displayed statements. QED.

## 5. Frozen replay artefacts

```text
scratch/audit_ad_k16_repeatfree_495_run_inventory_20260730.py
  SHA 5fa4c8b597c084ef9a8131eb7fc355c2cddd87bd01592006b8f29325cef928f9

scratch/ad_k16_repeatfree_495_run_inventory_20260730/literal_replay.audit.json
  SHA 58f9c065c37d29dec19101d8e936a6a68c27b1893c5444f43289278bd3448401

scratch/ad_k16_repeatfree_495_run_inventory_20260730/seed1_self_495.word
  SHA b5a4c8d8190cdbb82cade5a56e5cad5e192e9bf3e1ee82ed6eb87becd8dc4fbe

scratch/ad_k16_repeatfree_495_run_inventory_20260730/seed1_self_495.cpp_replay.txt
  SHA 6b3803c4123e2973f9136fe63538ee97f5f5a6a4900ea39a4d36f590d0d49356

scratch/ad_k16_repeatfree_495_run_inventory_20260730/seed5_self_495.word
  SHA 9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6

scratch/ad_k16_repeatfree_495_run_inventory_20260730/seed5_self_495.cpp_replay.txt
  SHA b7a495342c3105db52d8a9eb40ac7a0dea2605107ff4fda28fd88401f27972a3
```

The theorem authenticates literal coverage only.  It does not promote the
three-hole RF495 incumbent to a universal word, and it does not infer an
UNSAT result from any empty solver-output file.
