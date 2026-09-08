# K17 fully occurrence-pinned root escape: deficiency 40 to 39

**Date:** 2026-08-03  
**Status:** exact authenticated parent construction and complete supplier
projection.  This crosses the fixed-root deficiency-40 barrier on one literal
two-phase occurrence face.  It is not yet a chronology, residence proof,
upper-shadow proof, compiler, K17 word, or proof that `nu(17)=24313`.

## 1. Starting face

The starting compressed parent is

```text
bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
```

with the 1,748-ticket protected bank

```text
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1.
```

The fixed common-state supplier face had exact optimum deficiency 40: its
ten-mode witness has selected-file SHA

```text
e47ceaafaf441afc1f7475b24741b8bf37af0ea7f7479c57421c4ab2dfb72938.
```

The active-set occurrence oracle produced one explicit phase-common packing:

```text
phase 0 incidence  30c47b6a7d8ca02afe2025e6eb10b40b9c11e304f828838e723a05f1f1aa9672
phase 1 incidence  82efeb5eef295e4582512b6585cea938aea66cc6576c693721f8ff8b9d347d3c
union LMR rows       c92f4e30e1fb406acf243a47356139a0197b27f4242c4afa75a2372a07a39b31
incidence audit      2be9f9cdf671a683d217ac9cf8fda49313fd85d751e2408bfca4e2c9c8c95783
priced active set    ba37d799f3498563f173f617c9a31d464c073312cdeb9fcfbd5019ae8cb7d030
```

It contains exactly ten tickets per phase, one per selected mode.  Each phase
uses twenty distinct physical BASE_LMR rows; seventeen are shared between
the phases, so their coalesced union has twenty-three rows.  The two tickets
for each mode have the same declared `(q,alpha,beta)` state, while their
physical predecessor/successor rows may differ.  All twenty-three rows are
unprotected and are disjoint from the ten selected modes' twenty endpoint
rows.

The root/action and fixed-shore manifests are bound by

```text
4d2b43a4b75ce422478c652f20d3c3fb7351686bc13b6693cef43dc346f24092
763a88afb8df562de83a7134cc284b3a25f209664f29e68ec2390b803845d1aa.
```

## 2. Exact action

Use direct-low root action 0:

```text
row=130, root_mask=1935, current_bottom=13
```

with action-file SHA

```text
7878538b3fd61d6e2897e92c77d3aca2219f1875d364c658c95232290bf4519c.
```

The materializer source has SHA

```text
5ee28d1ffbae91878b44625480b822f3436ff77bf7c40b6bb2e11ca5f8773528.
```

It pins, in one common presentation:

1. all 7,213 protected physical rows;
2. the ten selected modes' pre-transfer presentations;
3. the coalesced twenty-three BASE_LMR occurrence rows from both phases;
4. the named direct-low root action.

The residual augmented presentation has exact size

```text
29256 / 29256.
```

The completion changes four rows of the compressed parent.  Reapplying the
ten LLR overlays changes twenty additional endpoint rows.  Every protected
row and every occurrence-pinned row is byte-identical between the completed
compressed table and final overlaid table.  The target partition remains
exact: all 65,535 nonempty masks of ranks at most eight occur once, the root
and owner banks remain bijective, and the length histogram remains
`7395/16915`.

The output hashes are

```text
8bc9cade99e578e1f881fd74c1849db8eeda696bb124c3888e7172768e84c94f
  completed compressed table
88f0a5fc4f2a98db59450e95b06e1a4123caaeaaba40ec80db92ec74fbdde79d
  final ten-mode table
c7e3a8d08c2c3e2b9bf6b3804e07a4afd43960101ca66c8d96c673b74ccd0f07
  materialization audit
```

## 3. Complete supplier replay

The complete 6/9/4 supplier projection on the final table gives

```text
edges          74573
matching       16859 / 16898
deficiency     39
zero heads     32
Hall shore     47 / 8
graph FNV64    ff2b1e3cfadd6f49
```

The exact projection artifacts have hashes

```text
0f5b301ddaf74440506b79bdc4db1a069c0282810bea560dceda1954613d97f3
  supplier.projection.audit.json
3a93cf7a059f746938fb9b779a85fc6b45429fa57e8b778fe960b0ef433a5f7e
  supplier.matching.tsv
613218ae38a51fa4c9ea7aae3aececbc1f3d212443692d5ab04f684e62c5ffde
  supplier.hall.tsv
```

Therefore the exact fixed-root/common-state optimum 40 is not a global
barrier.  One authenticated root/common-basis exchange remains feasible
after literal two-phase occurrence pinning and improves the complete supplier
rank by one.

An independent run using action 1 at row 146 also materialized a fully pinned
parent of deficiency 39.  Its separately frozen hashes should be cited from
its own audit bundle; it is corroboration, not an input to the action-0 proof.

## 4. Allowed-edge census

On this chosen occurrence face, an independent alternating-SCC audit starts
from one exact residual perfect matching with 84,984 expanded nodes and
4,870,309 directed residual arcs.  All 27 named singleton root actions are
allowed.  Across them, all 5,635 legal direct-low-to-root edges are allowed;
none is already in the matching, and every endpoint pair lies in the same
alternating SCC.  This is consistent with the two independent materialized
actions.  The SCC result is face-specific and does not imply that several
actions compose.

## 5. Exact consequence and next gate

The proved implication is

```text
fixed ten-mode structural face
  + one common declared-state ticket per mode per phase
  + one exact direct-root exchange
  -> a literal occurrence-pinned parent of supplier deficiency 39.
```

The next Benders iteration must treat `88f0a5fc...` as a new parent:

1. regenerate its exhaustive structural mode catalogue;
2. regenerate both phase occurrence menus and compound row-state DNFs;
3. compute its new maximum matching and Hall shore;
4. select the next root/mode/occurrence exchange against target deficiency 38.

The old `bf5b946f...` mode IDs, occurrence menus, and Hall cuts are lineage
data only after this parent change.  Reusing them as if their incidences were
unchanged would invalidate the proof.

## 6. Evidence locations

Local mirror:

```text
scratch/root_k17_occurrence_pinned_singleton_action0_20260803/
```

Persistent H100 root:

```text
/home/amodo/or15/work/root_k17_occurrence_pinned_singleton_action0_20260803/
```

This audit closes only the common-basis/selected-mode/two-phase-occurrence and
complete supplier-projection gate for one transition from deficiency 40 to
39.  Chronology, residence, arbitrary-width upper coverage, outer-state
circulation, common-cap compilation, and the final length-24,313 word remain
open.
