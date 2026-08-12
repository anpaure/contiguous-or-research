# K17 fixed10/occurrence-pinned root-subset descent reaches deficiency 21

**Date:** 2026-08-03  
**Status:** exact finite materialization-and-replay audit on one SHA-pinned
face. This is not a chronology, residence, upper, compiler, word, or
`nu(17)=B(17)` claim.

## 1. Frozen face and protocol

Every run binds the same data:

- bf5 private-bank parent `bf5b946f...`;
- `7,213` protected rows / ticket file `d02e01d0...`;
- fresh `115,086`-edge catalogue `57bc1ac6...`;
- fixed ten-mode deficiency-40 selection `e47ceaaf...`;
- the authenticated two-phase occurrence face with 23 union BASE_LMR rows,
  SHA `c92f4e30...`;
- the 27 named direct-low root actions, SHA `763a88af...`.

For each tested action subset, the audit performs two actual computations:

1. solve one joint augmented presentation matching with all chosen actions,
   the protected bank, ten modes, and 23 occurrence rows pinned;
2. materialize the resulting table and replay the complete `6/9/4` supplier
   projection from that table.

There is no addition of singleton SCC credits. The joint presentation must
saturate `29,256/29,256` before its supplier score is counted.

The materializer source has SHA `5ee28d1f...`; the independent complete
supplier projector source has SHA `7a10575d...`.

## 2. All-27 incumbent and complete one-drop census

The all-27 joint table has complete supplier score

```text
edges       74,932
zero heads      21
matching    16,876 / 16,898
deficiency      22
Hall shore    23 / 1
```

All 27 subsets obtained by dropping one action were then rematerialized and
replayed. Their exact deficiency distribution is

```text
deficiency 21:  3 subsets
deficiency 22: 14 subsets
deficiency 23:  9 subsets
deficiency 24:  1 subset
```

The three strict improvements are:

| dropped action | physical row | deficiency | zero heads |
|---:|---:|---:|---:|
| 12 | 12,948 | 21 | 19 |
| 15 | 13,641 | 21 | 20 |
| 16 | 14,155 | 21 | 20 |

Thus the simultaneous all-27 choice is not even locally optimal on this
fixed face.

## 3. Frozen representative

The representative drops action 12 and retains the other 26. Its augmented
presentation again saturates exactly `29,256/29,256`; all 26 direct-low
actions are satisfied. Protected-row and occurrence-row changes are both
zero in the compressed and final tables.

Its materialized carrier hashes are

```text
compressed  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
final       fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
```

The complete supplier replay is

```text
edges       74,935
zero heads      19
matching    16,877 / 16,898
deficiency      21
Hall shore    23 / 2
graph FNV64  f80fe0c9b65f2471
```

Compared with all 27, removing one action adds three supplier edges and one
matching rank. This is a coupled rematerialization effect, not a removable
singleton credit.

## 4. Exact local census and tied beam

From the drop-12 representative, every one of the remaining 26 actions was
dropped in turn, with a fresh joint completion and complete supplier replay.
The distribution is

```text
deficiency 21: 12 subsets
deficiency 22: 12 subsets
deficiency 23:  2 subsets
```

Re-adding action 12 returns the all-27 deficiency-22 table. Consequently,
the all-except-12 subset is an exact single-toggle local optimum for this
deterministic completion-and-replay protocol.

The two other first-level ties were also expanded. Across 52 replays from
the all-except-15 and all-except-16 seeds (51 distinct two-drop subsets), the
distribution is

```text
deficiency 21: 22 evaluations
deficiency 22: 27 evaluations
deficiency 23:  3 evaluations
```

No tied branch reaches deficiency below 21. Across the three best
first-level seeds, 75 distinct two-drop subsets were covered; none strictly
improves the first-level value.

## 5. Exact scope of the conclusion

What is proved on this face:

- deficiency 22 is not locally optimal in the named 27-action subset cube;
- deficiency 21 is attained by three one-drop subsets;
- the representative all-except-12 subset has no improving Hamming-distance
  one neighbor under the frozen deterministic joint completion protocol;
- expanding all three tied one-drop seeds gives no strict second-drop
  improvement.

What is not proved:

- global optimality of deficiency 21 over all `2^27` subsets;
- optimality over every possible augmented completion of one subset;
- optimality on another occurrence packing, mode selection, or parent;
- any complete K17 word or upper bound.

The exact frozen artifact directory is

```text
scratch/k17_b268_common_parent_selector_20260802/
  root_action27_joint_incumbent_20260803/
  frozen_def21_subset_descent_20260803/
```

Its `SHA256SUMS` has SHA

```text
c1f696934bf93518c236d11d1fee570ec24b2b4b2a9a9e24de01e13526bab0c0
```

The heavy computations ran CPU-only on H100 under

```text
/home/amodo/or15/work/root_k17_bf5_def40_occ27_019fc35b_20260803
```
