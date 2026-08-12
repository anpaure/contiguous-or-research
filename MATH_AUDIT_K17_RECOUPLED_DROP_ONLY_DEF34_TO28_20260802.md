# K17 strict-recoupled drop-only chain: independent audit

Date: 2026-08-02  
Status: **PASS**, with one material provenance correction  
Scope: static target-chain table, complete 6/9/4 supplier projection, maximum matching/DM shore, and marginal two-phase relaxed-nine socket existence. This is not a chronology, residence, upper-shadow, occurrence-packing, compiler, or word result.

## 1. Authoritative lineage and correction

The zero-transfer parent is

```text
bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
```

and the structural transfer catalogue is

```text
30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
```

The 1,748-ticket ledger has SHA-256

```text
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
```

and names exactly 7,213 protected rows.

The strict-def84 recoupled deficiency-34 parent is reconstructed as the zero-transfer parent plus the 438 transfers

```text
drop001_def33.selected.tsv union {32928}.
```

Its SHA-256 is

```text
9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3
```

The file `/home/amodo/or15/work/def34_release_math_20260802/final.tsv`, SHA `e359e821...`, is **not** that parent: it differs in 108 rows and must not be cited as the initial table of this chain. The authoritative 9daf table is at

```text
/home/amodo/or15/work/root_k17_b268_common_parent_selector_def84_release_c490cc49_019fc35b_20260802/out/def84_force_mutable_zero_roots/final.tsv
```

This correction does not affect any state after the first drop. Reconstructing from the bf5b parent and the frozen selected sets reproduces every stored deficiency-33 through deficiency-28 table byte for byte.

## 2. Why the transfer count is free

For one catalogue edge, the zero-transfer endpoint pair has the form

```text
L = (Z < R_L),       length 2,
R = (X < M < R_R),   length 3,
```

and the selected transfer changes it to

```text
L' = (X < Z < R_L),  length 3,
R' = (M < R_R),      length 2.
```

Here the catalogue certifies the displayed strict containments. Consequently:

1. the multiset of literal targets in the two rows is identical before and after the move;
2. the pair of lengths remains `{2,3}`;
3. both roots and both owners are unchanged;
4. the inverse operation is simply to drop the transfer.

For a selected set with pairwise-disjoint endpoint rows, these involutions commute. Therefore **every subset** of the selected transfers preserves the complete 65,535-target partition and the global length histogram `(7395,16915)`. There is no equation fixing the transfer count to 438. If the two endpoints avoid the protected set, dropping the transfer also leaves all 7,213 protected rows unchanged.

This proves that the six drop-only steps below require no compensating additions.

## 3. Exact replay

The dropped transfer indices are

```text
32928, 11715, 12615, 32713, 49993, 68076.
```

The clean-room replay independently rebuilt every table, regenerated the complete supplier graph, ran Hopcroft--Karp, reconstructed the alternating DM Hall shore, and reduced the two DNF files by literal role identity.

| state | selected | table SHA-256 | supplier rank | deficiency | graph edges | zero heads | DM shore H/N | sockets `(p0,p1,both,either)` |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| def34 | 438 | `9dafc568...` | 16864 | 34 | 74982 | 20 | 51/17 | 3099/2260/1838/3521 |
| def33 | 437 | `9e5fcd90...` | 16865 | 33 | 74985 | 19 | 50/17 | 3099/2260/1838/3521 |
| def32 | 436 | `4aab8c6d...` | 16866 | 32 | 74990 | 19 | 49/17 | 3098/2259/1837/3520 |
| def31 | 435 | `0164db1e...` | 16867 | 31 | 74994 | 19 | 46/15 | 3097/2258/1836/3519 |
| def30 | 434 | `0a6f73c0...` | 16868 | 30 | 74999 | 19 | 43/13 | 3096/2257/1835/3518 |
| def29 | 433 | `df408f84...` | 16869 | 29 | 74995 | 19 | 41/12 | 3095/2256/1834/3517 |
| def28 | 432 | `18044fb4...` | 16870 | 28 | 74996 | 19 | 37/9 | 3094/2255/1833/3516 |

The corresponding graph FNV-64 values are

```text
def34 a3d6b556f77db3fa
def33 c7f210f0df68f832
def32 e593bd0dc0d61000
def31 264f5383c639c0fa
def30 90fd3cb49d2a5e02
def29 3f16dca71a4069a9
def28 e23b6734b354ecfd
```

At every state the audit also verified:

- exactly one occurrence of every nonempty target of rank at most eight;
- target-rank histogram `17,136,680,2380,6188,12376,19448,24310`;
- 7,395 length-two and 16,915 length-three chains;
- every rank-eight root and every rank-nine owner exactly once;
- unchanged owner/root row assignment;
- all 7,213 protected rows literally unchanged.

The socket tuple is only the marginal existence tuple for the exact relaxed-nine five-cell DNF in the two owner phases. It does **not** prove simultaneous occurrence packing or a common phase-valid chronology.

## 4. Exhaustive single-drop plateau at deficiency 28

Let `X` be the deficiency-28 DM Hall head shore in the final graph. For a proposed drop `e`, remove from `X` the old head that disappears, when there is one, and call the resulting set `X_e`. Recompute the exact neighbour set of `X_e` after changing the two endpoint rows.

If

```text
|X_e| - |N_e(X_e)| >= 28,
```

then Hall's theorem proves that the new graph still has deficiency at least 28. A full matching computation is unnecessary.

The frozen scan SHA is

```text
80f77baf5f20e016216060f2d26c9b9610317fba0e73b13ea864a4291806891c
```

and covers all 432 selected transfers:

- 430 are independently certified by the fixed-shore Hall inequality;
- the only two not filtered are transfers 5619 and 63200, each with fixed-shore excess 27;
- fresh complete projections for both still have deficiency 28.

Therefore no single selected-transfer drop improves the deficiency-28 state. The pair `{5619,63200}` was also replayed exactly and remains deficiency 28 (table SHA `0860d691...`); this is a calibration only, not an exhaustive pair result.

## 5. Proof-safe next neighbourhood

The next sound move is an **addition or drop-plus-add exchange**, not another isolated selected drop. The local involution theorem above makes such a state valid whenever endpoint rows are disjoint and unprotected. A proof-safe search should:

1. enumerate currently unselected structural transfers with free, unprotected endpoints;
2. use the current DM shore as a necessary Hall filter;
3. run a fresh complete projection on every survivor;
4. accept a supplier improvement only after requiring an exact common two-phase occurrence tuple (and then a common occurrence packing), rather than relying on the marginal DNF socket counts.

This expands the search beyond the exhausted drop-only radius while keeping target partition, roots, owners, protected rows, and phase semantics explicit.

## 6. Frozen audit artifacts

Remote directory:

```text
/home/amodo/or15/work/def34_release_math_20260802/independent_audit_20260802
```

Key hashes:

```text
cfc718583879545822df2d8ff84bd60bb3884545c7b51d31cac0783ce82edee4  audit source
bf64d8b1a18600906c4e992ce1aebc0a56a6c2f592a65b6898e8020bd2c0f8ef  audit binary
493652f6a32f483db6af779c5aaea09bb171d65ff938a04025ce216d00dcd9e0  independent.audit.json
0413713a606290d229456465d5a0715da7c18032c498c82af38d3cc06637b380  independent.stdout
52f0db2669e92486cb1cd09e5e77a95985aa8621f9703e5e67544f18134ba550  independent.stderr
```

