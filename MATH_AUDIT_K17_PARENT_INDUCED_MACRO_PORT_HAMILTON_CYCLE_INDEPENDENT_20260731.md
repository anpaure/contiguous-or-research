# Independent audit: the parent-induced `K17` macro-port Hamilton cycle

Date: 2026-07-31  
Status: **PASS**, exact source-relative literal theorem

## Frozen inputs

```text
MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md
SHA-256 d02245596dd9f5097881e901243c850c89216f777eafaae4a06502c0dfe7309e

scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6

scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

Independent replay:

```text
scratch/independent_audit_k17_parent_induced_macro_port_cycle_20260731.py
SHA-256 56a929ea4fb355b75a56675faca7610daa4e5694e90566cd4ff6d66ccc3c179c

scratch/k17_parent_induced_macro_port_cycle_20260731.independent_audit.json
SHA-256 c0f509b7a2547a84fd9bae439deb49f5ffa21247b71e372167c4bde4d26c70cf
```

The independent replay imports no constructor code.  It reads the final cycle
and parent component file, explicitly builds the relevant Boolean layers, and
was replayed twice with byte-identical JSON output.

## Literal theorem audit

Let `W` be the cyclic list in the `.cycle` file.  Direct enumeration gives

```text
|W|                                      24310 = binom(17,9)
distinct W entries                      24310
rank of every entry                     9
cyclic Johnson adjacencies              24310/24310
distinct consecutive intersections      24310 = binom(17,8)
```

Moreover, the owner set is literally all of `binom([17],9)` and the
intersection set is literally all of `binom([17],8)`, not merely two sets of
the correct cardinalities.  Thus the promoted Hamilton/lower-`q1` statement is
**GO**.

## Independent downstream census

The cyclic lower-window replay gives

| lower depth | window width | target rank | distinct | total | missing |
|---:|---:|---:|---:|---:|---:|
| `q2` | 3 | 7 | 17,825 | 19,448 | 1,623 |
| `q3` | 4 | 6 | 11,363 | 12,376 | 1,013 |

All width-three intersections have rank seven.  At width four the occurrence
rank profile is `rank6: 23247, rank7: 1063`.

The cyclic upper-interval replay gives

| rank | distinct | total | missing |
|---:|---:|---:|---:|
| 10 | 17,557 | 19,448 | 1,891 |
| 11 | 11,466 | 12,376 | 910 |
| 12 | 6,060 | 6,188 | 128 |
| 13 | 2,377 | 2,380 | 3 |
| 14 | 680 | 680 | 0 |
| 15 | 136 | 136 | 0 |
| 16 | 17 | 17 | 0 |
| 17 | 1 | 1 | 0 |

The three missing rank-thirteen masks are `0x0ef7b`, `0x0efdb`, and
`0x16fdb`.  The maximum first-full interval width is `283`.  Exact hashes of
all larger missing sets are frozen in the independent JSON.

The cyclic positive-run census has no length-one run and has exactly

```text
length 2: 1063
length 3: 1829
total short: 2892
```

The best one-edge opening neutralizes only three of them; edge `142` is the
first maximizing edge, leaving `2889`.  There are `155` maximizing edges, so
the theorem's edge `142` is a deterministic first-max choice rather than a
unique optimum.

## Construction provenance audit

The authenticated parent contains two cyclic rank-eight components of lengths
`6390` and `45`, together enumerating `binom([15],8)`.  Their consecutive
rank-seven intersections enumerate `binom([15],7)`.  Consecutive rank-six
intersection colours have multiplicity profile

```text
1^3630 2^1320 3^55,
```

and the parent rank-nine unions have profile

```text
1^3675 2^1230 3^100.
```

Keeping the first authenticated occurrence of each rank-six colour deletes
`1405` edges from the large parent component and `25` from the small one,
giving the claimed `1430` oriented residual paths.

The final literal cycle has the exact top-bit sector partition

```text
00: 5005  = every old rank-nine U owner
01: 6435  = every old rank-eight parent owner tagged on one shore
10: 6435  = every old rank-eight parent owner tagged on the other shore
11: 6435  = every old rank-seven parent edge colour tagged on both shores.
```

This independently confirms the advertised parent-induced `A/X/Y/U` owner
provenance.  The primary constructor was also rerun and regenerated the same
cycle byte for byte; its fixed-seed integral port completion is therefore
reproducible.

## Exact scope and caveat

The certificate is a literal Hamilton cycle of rank-nine owners with a perfect
rank-eight edge-colour palette.  It does **not** give a universal `K17` word:
the displayed upper holes, lower `q2/q3` holes, `2892` short residence runs,
and the common-cap compiler remain open.

The port completion is undirected at macro level: the final cycle traverses
`751` residual macros in their designated `X -> Y` direction and `679` in the
reverse direction.  Hence it does not prove a uniform outgoing-orientation
strengthening of the macro theorem.  This orientation caveat does not affect
the literal Hamilton/lower-`q1` certificate, which is checked directly.

This audit verifies the finite literal certificate and its parent provenance.
It does not independently prove the main theorem's later dimension-uniform
sufficient rule; nor does it replace the separate all-occurrence-transversal
residence audit.
