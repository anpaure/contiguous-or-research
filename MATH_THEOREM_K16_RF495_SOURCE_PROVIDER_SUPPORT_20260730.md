# K16 RF495 source: exact provider equations and the tri-window support-three gate

Date: 2026-07-30  
Status: **proved solver-independent, source-relative theorem; service and universality scopes separated**

## 1. Frozen source

The authenticated repeat-free K15 parent is

```text
scratch/k15_repeatfree_seed_20260730/K15_REPEATFREE_SEED.word
SHA-256 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

and the frozen RF495 cell ledger is

```text
scratch/k16_rf495_source_atlas_20260730/rf495_best.cells
SHA-256 6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

with the exact 4/9/5 layout

```text
cells[0:4]
+ parent[6:6436]
+ cells[4:13]
+ (0x8000 | parent[7:6432])
+ cells[13:18].
```

The reconstructed length-12,873 word is

```text
scratch/k16_rf495_source_atlas_20260730/rf495_source.word
SHA-256 9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6
```

The compressed ending-OR recurrence retains at most 12 states and counts all
82,863,501 literal intervals.  Exactly 65,532 nonzero masks occur.  The three
and only three holes are

```text
h0 = 0x18e7,   h1 = 0x3de7,   h2 = 0x9e20.
```

The complete 65,536-entry interval-count vector, serialized as little-endian
unsigned 64-bit integers, has SHA-256

```text
af046e55c1d4d62f4a5e3ce22d8e11faf948d1f9540ef050f47bec1962e24200.
```

## 2. Exact one-cell provider normal form

Fix a position `p` and one of the holes `h`.  For every interval `I`
containing `p`, put

```text
c(I,p) = OR of the source cells in I other than p.
```

After replacing the source cell at `p` by a nonzero mask `v`, the interval is
an `h`-witness exactly when

```text
c(I,p) | v = h.                                                (2.1)
```

Forbidden-bit endpoint scans enumerate every context in (2.1).  After
removing Boolean-dominated contexts, every one of the 38,619 position--hole
rows has a **single** minimal required mask `m_h(p)`.  Consequently the full
provider domain is the Boolean interval

```text
v provides h at p
  iff  0 < v,  v & ~h = 0,  and  m_h(p) & ~v = 0.              (2.2)
```

The catalogue stores `m_h(p)` and a literal representative interval proving
it for every row.  Setting `v=h` gives the singleton interval `[p,p]`, so all
12,873 positions are provider sites for each individual hole.  The exact
numbers of `(position,value)` providers are

| hole | exact provider pairs |
|---|---:|
| `0x18e7` | 27,824 |
| `0x3de7` | 360,228 |
| `0x9e20` | 16,980 |

Intersecting (2.2) at a common position gives the exhaustive same-site
census:

| holes served at the same edited site | sites | site/value pairs |
|---|---:|---:|
| `0x18e7`, `0x3de7` | 363 | 893 |
| `0x18e7`, `0x9e20` | 0 | 0 |
| `0x3de7`, `0x9e20` | 0 | 0 |
| all three | 0 | 0 |

Thus no one-cell edit anywhere in the word can service all three holes.

## 3. Unrestricted service support is exactly two

The preceding all-three intersection gives the lower bound two.  It is
sharp: make the two edits

```text
p34  := 0x18e7,
p100 := 0x9e20.
```

Then the three literal witnesses are

```text
0x18e7 on [34,34],
0x3de7 on [28,35],
0x9e20 on [100,100].
```

Therefore the minimum unrestricted edit support needed merely to create the
three missing witnesses is exactly two.

This statement is **service-only**: it does not assert that the two edits
preserve all 65,532 source-covered masks.

## 4. The frozen 4/9/5 tri-window has an exact support-three gate

Let

```text
F = {0,1,2,3,
     6434,6435,6436,6437,6438,6439,6440,6441,6442,
     12868,12869,12870,12871,12872}.
```

For a proposed changed support `T` contained in `F`, every new witness for a
source hole must meet `T`.  Deduplicate all such intervals by

```text
(fixed source OR outside T, subset of T touched by the interval).
```

For one-site supports there are 111 possible triples of witness shapes.  For
the 153 two-site supports there are 7,702 possible triples.  In every case,
the three OR equations contradict each other at a single bit before any
nonzero or changed-value side condition is used.  Using the first
contradictory bit in increasing order, the exact two-site ledger is

| bit | 0 | 2 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|
| shape triples | 4,724 | 400 | 317 | 1,678 | 85 | 498 |

These entries sum to 7,702.  Hence:

> Any word differing from the RF495 source at at most two positions of `F`
> still misses at least one of `0x18e7`, `0x3de7`, `0x9e20`.

In particular, no such word is universal.  This is a literal source-relative
no-go, independent of SAT, DIMACS, stochastic search, or collateral models.

The bound is sharp for **hole service**.  Every three-element subset of `F`
can service all three holes by assigning the three holes as singleton values
to its three distinct positions.  Therefore all 816 unordered three-site
supports are service-feasible.  Equivalently, the viable ordered
provider-site tuples `(p0,p1,p2)` for `(h0,h1,h2)` are exactly the 4,896
pairwise-distinct triples in `F^3`.

This last construction does **not** prove that any three-cell assignment is
universal.  Preservation of the other 65,532 masks is the separate active
kernel/collateral problem.

## 5. Auditable artifacts

```text
scratch/audit_k16_rf495_source_provider_atlas_20260730.py
  SHA-256 5e74565312ff0938e6a9a5315c8a880a13ea8b71a0f4b51d01b4e0bfc9651611

scratch/k16_rf495_source_atlas_20260730/one_cell_provider_constraints.json
  SHA-256 0f2b5bfddbf859e80373044ed45123a836b76b0f4a2ceeefc07f6ee083bba7b8
  payload 4ed73f2ccf8b19163370acb413e35de43e266625ca1db0bb9697ef70dd460439

scratch/k16_rf495_source_atlas_20260730/rf495_source_provider_atlas.audit.json
  SHA-256 474db189e9077b5c403def65bd9da8e5d3166007e8aa16a9b448c113fc90c33d
  payload aac03de52a1930501fae2931f1e6ba9e344d9ad66ef5669e56ac9c1d2a5a31b7
```

Re-running the audit reproduces all three generated artifacts byte for byte.
The theorem does not claim an unrestricted length-12,873 K16 no-go.
