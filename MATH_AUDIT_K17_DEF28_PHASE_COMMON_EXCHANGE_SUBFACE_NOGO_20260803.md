# K17 deficiency-28 phase-common exchange subface

Date: 2026-08-03  
Status: **scope-exact no-go**  
Result: no supplier-rank improvement among the one-add / one-drop-plus-one-add actions whose added transfer lies in the authenticated literal exact-common one-transfer subface.

## 1. Parent and catalogue

The parent is the independently audited deficiency-28 table

```text
18044fb4f7e4174c483e3cd8f6c4d91b0b9a9aa1a26ef45952312a310e5244c2
```

with complete supplier rank `16870/16898`, deficiency `28`, and DM Hall shore `37/9`.

New additions must use the fresh structural catalogue built on the bf5b recoupled zero-transfer parent:

```text
e51b1688e977c11fb7dee80338f4bcc7e86b83c232c416f48bd774ac6f4d9746
  fresh.complete.edges.tsv
```

It has 115,086 protected-safe structural edges. The older 93,234-edge catalogue is valid for replaying and dropping its historical selected modes, but it is not a valid prospective addition catalogue after root recoupling.

The 432 retained historical modes were rebound uniquely by endpoint pair to the fresh catalogue:

```text
b2dee4346ac11d8e563476624303b1903343e9cca55c2f9aaefbe4cf2f4ee89f
  def28.fresh.selected.tsv
```

The private footprint remains the authenticated 7,213-row bank.

## 2. Exact action universe

Two action types were enumerated.

1. `ADD(a)`: add one currently unselected fresh transfer whose two endpoints are free and unprotected.
2. `DROP_ADD(d,a)`: revert one of the 432 selected transfers, then add one unselected fresh transfer whose endpoints are free after that drop.

The transfer involution theorem proves that both action types preserve the complete 65,535-target partition, every root and owner, and the 7,395/16,915 length histogram. Endpoint and protected-row checks are literal.

The exact action counts are

| action | legal actions |
|---|---:|
| add | 85,033 |
| drop plus add | 36,761,701 |

## 3. Hall screens

The first screen uses the frozen 37/9 DM head shore. Every changed old head is removed from the witness, and the neighbour set is recomputed exactly from the changed endpoint-row menus. An action is rejected when this explicit Hall set still has deficiency at least 28.

| action | pass neighbour-cardinality Hall screen |
|---|---:|
| add | 2,503 |
| drop plus add | 1,241,637 |

A stronger exact matching-rank calculation on the same surviving old head shore leaves

| action | pass restricted-rank screen |
|---|---:|
| add | 2,502 |
| drop plus add | 1,241,150 |

The rank-screen output is frozen at

```text
18d272c6fd4678552486cce8a8366baa4acc7eb9ff616c1e6abbe329b6ff26f4
  rank37_survivors.tsv
```

## 4. Literal common-occurrence subface

The exact one-transfer occurrence audit on this same fresh parent enumerates a literal tuple

```text
(q, alpha, beta, predecessor_row, successor_row)
```

that is identical in native phase 0 and transported phase 1 for 3,171 fresh edges. Its ledger is

```text
2c399790b1af274f652d42308ecc54d16e0a3f7ef96c42d7b4dc3c21af23329a
  fresh.edge.exact_common.tsv
```

Intersecting this exact-common edge set with the Hall survivors gives:

| action | Hall survivors with exact-common added edge |
|---|---:|
| add | 0 |
| drop plus add | 322 |

This exact tuple predicate is a strong sufficient subface. It is not necessary after a batch: another retained or dropped transfer can change the available long witnesses and may create a tuple absent in the isolated one-transfer table.

## 5. Fresh complete supplier replay

All 322 surviving drop-plus-add tables were materialized exactly. Their complete 6/9/4 supplier graphs were rebuilt by an incremental algorithm that:

- reuses an old edge only when both its supplier row and head row are unchanged;
- recomputes every edge from a changed supplier;
- recomputes every incidence into a changed/new hard head;
- restores deterministic head ordering and self-exclusion;
- runs a fresh Hopcroft--Karp matching and DM-shore replay.

The first three incremental graphs were compared in full against independent `full_projection` rebuilds, including edge count, matching rank, graph FNV, and DM shore.

Verdict:

```text
PASS_K17_DEF28_COMMONFACE_SUPPLIER_REPLAY
candidates=322 improvements=0 full_validations=3
```

The final deficiency histogram is

```text
28 : 286 candidates
29 : 36 candidates
```

No candidate reaches the subsequent final-table occurrence regeneration or packing gate because none improves the supplier rank.

The replay ledger is

```text
e61358bb429ef18d76048c45c462ea6f02d79069a9f49666ebfeb48e531f7f0a
  commonface_supplier_rank37.tsv
```

## 6. Exact conclusion and remaining open scope

There is no deficiency-27 table in the declared radius `(drop <= 1, add = 1)` subface whose added edge already has a literal identical two-phase occurrence tuple on the authenticated isolated one-transfer parent.

This does **not** close all 1,241,150 Hall-surviving drop-plus-add actions. An added edge outside the isolated exact-common set may acquire a phase-common tuple from the other retained transfers. Closing that larger face requires candidate-specific supplier replay followed by candidate-specific two-phase occurrence regeneration and packing.

It also does not prove a common occurrence-labelled state, carrier chronology, residence, upper deck, compiler, or K17 word.

## 7. Frozen artifacts

Persistent H100 root:

```text
/home/amodo/or15/work/recoupled_def28_phase_exchange_20260803
```

Sources and binaries:

```text
880bb17351fa52eb293d204fe2887832dc3b798dac13d64661a45b68394c06bc  screen source
6ed1d41a68b570c9e8a294fe8c99646773b81e653180092ad37327ac82398ed8  screen binary
953019ec7bbcc505c23c14a9b966b6888be13d865a1575f8726a1ef8a5cceac0  supplier replay source
048a34da491ad812facd113731d3c744d80589386c4b70254a6ad6a270f331cf  supplier replay binary
```

