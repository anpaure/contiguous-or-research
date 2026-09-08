# K16 deletion-191 topology and nonduplicative novel-phase supports

Date: 2026-07-30  
Lane: AD, global optimal-length support selection  
Status: **solver-free exact artifact audit; four scoped support recommendations; feasibility UNKNOWN**

## 1. Scope and frozen inputs

The authenticated universal word is

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

The exact delete-plus-one-substitution no-go remains in force: deleting one
cell and changing at most one surviving cell never gives a universal
length-12873 word.  The present note does not repeat that exhaustive run.
Instead it audits and composes the retained low-hole provider topology:

```text
scratch/k16_multiroot_deletion_portal_rank_20260730.tsv
SHA-256 fe51c4301cab3be93900a9f848082a8fd8a7336bf1d0f9016cb512df2f9a33d2
```

with the new deletion-6440 descendant

```text
scratch/k16_delete6440_novel_h2_20260730.word
length 12873
SHA-256 a1c9ec8d4e2b22b2fa20af1d0c96a33591b273f730814e1011f7bcd159e928fe
holes {0x287d,0x546d} = {10365,21613}
```

and its complete one-cell provider atlas

```text
scratch/k16_delete6440_novel_h2_provider_atlas_20260730.audit.json
SHA-256 777e3a3ed015b8f0dc58743584b1ff9bcd80b8aa9e5c262f5721a13743a0cf6f.
```

All positions below are zero-based positions in this length-12873 word.
The active multiroot job uses support

```text
{0,3,5921,12872}.
```

None of the supports recommended here is that support.  No solver was run.

## 2. The exact deletion-root graph

Define a directed edge from deletion root `r` to deletion root `s` when one
enumerated substitution installs every hole of `r` and leaves exactly the
hole set of `s`.  Parsing the frozen 191-row table gives exactly

```text
16 directed edges from 11 source roots,
38696 full-provider replacement rows.
```

The full edge list is

```text
0     -> 1,2
1     -> 0,6441,12873
2     -> 3
3     -> 2
6440  -> 6441
6441  -> 2,6440
6959  -> 6960
6960  -> 6959
12871 -> 12872
12872 -> 12871,12873
12873 -> 12872.
```

An independent Tarjan pass over these rows reproduces exactly the five
nontrivial strongly connected components

```text
{0,1}, {2,3}, {6440,6441}, {6959,6960},
{12871,12872,12873}.
```

The component `{2,3}` is relevant to the new masks.  Its lexicographically
best exact exits both use position 2:

```text
root 2: {0x246d,0x2c6d,0x346d,0x766d}
        -> {0x146d,0x546d};
root 3: {0x146d,0x546d}
        -> {0x246d,0x346d,0x766d}.
```

This does not prove that position 2 is the unique realization of either
root edge.  It proves that position 2 is an authenticated best transition
and gives an axis absent from the active four-cell support.

## 3. Exact `0x546d/0x766d` phase fibre

The novel parent has holes

```text
H=0x287d, L=0x546d.
```

Its atlas has 52,429 provider/value pairs, no zero-debt move, and exactly
eight minimum one-debt moves.  All eight occur at position 3 and have values

```text
0x0044,0x0045,0x004c,0x004d,
0x0064,0x0065,0x006c,0x006d.
```

Each fills `L` and creates

```text
C=0x766d,
```

so the eight children all have hole set `{H,C}`.  The child manifest and
topology audit are

```text
scratch/k16_delete6440_novel_h2_children_20260730/manifest.json
SHA-256 e693420bf7b2ccab7693ed9c7ec25d464d14660ca5b7d4459975cefc04632e53

scratch/k16_delete6440_novel_h2_eight_child_topology_20260730.audit.json
SHA-256 04046a0e7eab09d31fb67a0ca5e8f348e4f09d7e9e9db65cff4bb6f8f10d1d38.
```

Literal replay confirms that each child differs from the parent only at
position 3 and has exactly the two stated holes.  For every child, the
complete provider atlas has exactly eight minimum exits, again at position
3, with values

```text
0x2044,0x2045,0x204c,0x204d,
0x2064,0x2065,0x206c,0x206d.
```

They fill `C` and recreate `L`.  All eight children have one common minimum-
transition signature, but their complete full-provider profile signatures
are pairwise distinct.  Consequently:

* contracting the eight children is exact for the displayed minimum
  `L <-> C` transition;
* contracting them for all later providers is not justified;
* putting position 3 itself in an arbitrary-value model retains all eight
  phase choices without selecting one child in advance.

## 4. Phase-uniform provider table

The following rows are read from the complete parent and eight child atlases.
`after` is the total number of holes after the best action at that position.
The child structural row is identical for all eight children; only the stated
candidate-value count can vary.

| position | parent best action | every child best action | child candidate count |
|---:|---|---|---:|
| 2 | fill `H`; after 5; debts `{0xa46d,0xa879,0xa87d,0xe879}` | fill **both** `H,C`; after 4; same debts | 735 |
| 3 | fill `L`, debt `{C}`; after 2 | fill `C`, debt `{L}`; after 2 | 257 |
| 4 | fill `L`; after 4; debts `{0x542d,0x562d,0x56ad}` | fill `C`; after 5; debts `{0x542d,L,0x562d,0x56ad}` | 516--544 |
| 528 | fill `L`; after 11 | fill `C`; after 4; debts `{0x0462,0x146b,0x546b}` | 528 |
| 5934 | fill `H`; after 5; debts `{0x1060,0x306d,0x307d,0x327d}` | identical structural row | 192 |
| 6438 | fill `H`; after 5; debts `{0x286d,0x2c6d,0xa86d,0xac6d}` | identical structural row | 272 |
| 6441 | fill `L`; after 4 | fill `C`; after 6 | 129 |

The two remote `H` ports at 5934 and 6438 have disjoint best-debt sets.  The
two child `C` ports at 4 and 528 also have disjoint best-debt sets.  Finally,
the child joint-provider debt set at position 2 is disjoint from the union of
the displayed best-debt sets at 4, 528, 5934 and 6438.  These are exact set
equalities, not an independence assumption.  They make the added positions
nonredundant at the one-cell ledger level, but they do not imply that their
simultaneous interval deltas add.

## 5. Ranked nonduplicative supports

Call a support **one-step role-complete for this phase fibre** when it contains

1. position 2, the authenticated `{2,3}` deletion-SCC axis and child joint
   `H,C` provider;
2. position 3, the exact `L/C` phase axis;
3. one direct `L/C` port from `{4,528}`; and
4. one phase-stable `H` port from `{5934,6438}`.

This definition is local to the frozen atlases.  It is not a completeness or
WLOG theorem for arbitrary length-12873 words.

Subject first to minimum support size and then to a broad parent-phase
provider domain, the recommended supports are:

| rank | name | support | editable blocks | reason |
|---:|---|---|---|---|
| 1 | remote four | `{2,3,4,5934}` | `[2,4]`, `{5934}` | smallest role-complete support; position 5934 has 129 parent provider values versus 17 at 6438 |
| 2 | central four | `{2,3,4,6438}` | `[2,4]`, `{6438}` | same roles, but uses the central `H/A` collateral geometry |
| 3 | child-expanded five | `{2,3,4,528,5934}` | `[2,4]`, `{528}`, `{5934}` | adds the strongest child-specific `C` port, with debt support disjoint from position 4 |
| 4 | dual six | `{2,3,4,528,5934,6438}` | `[2,4]`, `{528}`, `{5934}`, `{6438}` | adds both disjoint `C` and disjoint `H` alternatives |

The first two are especially compact: positions 2--4 form one consecutive
block, so the deletion-SCC and phase axes are allowed to interact literally
inside the same interval geometry, while the `H` service position is one
remote block.  This is the smallest exact-role fallback to the active support
`{0,3,5921,12872}`, which contains the phase switch and three `H` portals but
omits position 2 and the direct position-4 `L/C` port.

The ordering is a deterministic support-design recommendation, not a claim
that rank 1 dominates rank 2 in the full nonlinear interval-OR model.  Any of
these supports must still be compiled with arbitrary values jointly and a
SAT candidate must be replayed on all 65,535 masks.

## 6. Reproducible audit and boundaries

The light audit script independently:

* checks every pinned hash;
* parses all 191 root rows, reconstructs the 16-edge graph, and recomputes its
  strongly connected components;
* replays the parent and all eight child words to obtain their exact holes;
* checks that every child differs from the parent only at position 3;
* checks all sixteen forward/reverse minimum phase moves;
* reads each complete provider atlas and proves the table's phase-uniform
  profiles and collateral-set disjointness; and
* rejects the active four-cell support from the recommended list.

Artifacts:

```text
scratch/audit_ad_k16_deletion191_novel_phase_supports_20260730.py
SHA-256 76ede13badc5ad3230398b3c72316fb3825942c16e49fdcbb2395bdd8a57c06d

scratch/ad_k16_deletion191_novel_phase_supports_20260730.audit.json
SHA-256 7dbec1f8ba999b6711c5215ff8cfc763d5fea71e7b8a36e78446e939d87fb34d
payload 6e2e7f538a60bd3f8e2ed531402ad27490b7e47d82352ec58f2b7da0bba72f77.
```

Exact proved boundary:

* the graph, phase transitions, per-position one-cell profiles and support
  role checks above are proved for the frozen artifacts;
* no support here has been solved;
* no support is proved WLOG;
* no UNSAT or universal length-12873 word is claimed;
* finite LNS timeouts and provider rankings remain heuristic outside the
  exact rows explicitly audited here.

