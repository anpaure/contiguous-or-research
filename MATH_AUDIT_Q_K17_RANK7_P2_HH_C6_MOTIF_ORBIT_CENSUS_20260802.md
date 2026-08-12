# K17 rank-seven `P2--H--H` suffix-`C6` motif census

**Date:** 2026-08-02  
**Status:** exact protected structural orbit census, plus a scoped independent
execution of an older common-phase row-shadow pricer.  This is a local
harvest result, not a simultaneous packing, reset, chronology, residence,
upper, compiler, or word construction.

## 1. Rebase

The support-three suffix circuit is

\[
(S_0,R_0)+(B_1,S_1,R_1)+(B_2,S_2,R_2)
\longmapsto
(S_1,R_0)+(B_1,S_2,R_1)+(B_2,S_0,R_2),
\]

where, for a rank-six core `C` and three distinct spokes `a,b,c`,

\[
S_0=C+a,\quad S_1=C+b,\quad S_2=C+c,
\]

and the roots are the three pairwise unions.  The authenticated example is

```text
P2,H,H rows = 16269,16267,16271.
```

Its new P2 role has `3,899` phase-0 and `3,584` phase-1 exact hyperarcs.

The authoritative structural enumeration contains

```text
rank-seven phase-union-zero demands             623
structural suffix-C6 columns                    364
bottom-legal columns                            180
protected row-clean columns                     118
demands with a protected column                 116
demands with no protected column                507
```

The authoritative catalogue and audit are

```text
scratch/k17_rank7_p2_hh_c6_audit_20260802/
  structural_candidates.tsv
SHA-256 cb93bfc7b785eff4e9d6d01bc6ec6f46e3e2025879b3b1abeff85ba9757fefe0

  structural.audit.json
SHA-256 77d3ada0ea96b95044830c216d62e4826a16c027212563773cf048975d608e48
```

## 2. Canonical local orbit theorem

For one protected column, take the ordered target tuple

```text
S0,R0,B1,S1,R1,B2,S2,R2.
```

The multiset of the seventeen coordinate-membership words is a complete
orbit invariant under coordinate relabelling.  The `118` protected columns
occupy exactly four such orbits:

| bottom profile `(|B1|,|B2|,|B1 intersect B2|)` | columns | demands |
|---|---:|---:|
| `(5,6,5)` | `112` | `110` |
| `(4,6,4)` | `4` | `4` |
| `(6,5,5)` | `1` | `1` |
| `(3,6,3)` | `1` | `1` |

Thus the new suffix circuit is not a sporadic target geometry.  It lies in
the dominant `(5,6,5)` orbit, which contains `112/118` protected columns
and reaches `110/116` structurally supported demands.

To retain both authenticated owner phases, append the two owner sets of
each of the three physical rows.  The resulting ordered fourteen-set tuple
has `60` complete coordinate orbits.  A coarser profile records the bottom
triple above and whether each of the six owner markers is the missing third
spoke (`I`) or an exterior coordinate (`E`).  There are `16` such profiles.
The authenticated circuit has profile

```text
(5,6,5) | EEEEEE,
```

which is again dominant: `64` protected columns on `63` demands.

Therefore the finite-family statement is two-level:

- target geometry is a tiny **four-orbit** family;
- phase-labelled owner boundaries refine it to `16` coarse profiles and
  `60` complete orbits.

## 3. Scoped common-phase pricing replay

Before the authoritative `118`-column catalogue was frozen, an older
`111`-column catalogue filtered to H rows common to both phase tables was
priced against all `2,129,483` dynamic modes and all `17` fixed-soft modes
in each phase, excluding modes entering either rebuilt H destination.  On
that older input the independent execution gives

```text
phase-0-positive columns                          17
phase-1-positive columns                          19
positive in both phases                           13
distinct demands supported in both                12 / 623
```

Only `11` of those `13` columns belong to the newer authoritative protected
set; they support `10` demands.  The other two fail the newer protected-row
criterion.  All eleven intersections use the dominant `(5,6,5)` target
geometry.  Nine have profile `EEEEEE`; the other two have `EEEEII` and
`EEIEEE`.  Two repair the same P2 demand, row `16269`, hence eleven columns
but ten demands.

Frozen scoped-pricing outputs:

```text
rank7_c6_common_phase.tsv
  SHA-256 d9623d361347297be11aafa3b192733e5fd690a50daa1ed5a7caf753edbb7500
rank7_c6_common_phase.audit.txt
  SHA-256 74f6d5d245cee4b83656f3c5b92c3e2e63568a3826fed6ea22827ae64c796c88
```

This replay is complete only for the older `111`-column input.  It is not an
exhaustive price of the authoritative `118` columns; that catalogue belongs
to the separate full-column task.  It also retains only one canonical
witness per phase and makes no simultaneous endpoint-packing claim.

## 4. Interpretation

The authenticated rank-seven suffix `C6` is the first non-H-specific
role-moving motif.  Its algebra is genuinely reusable: four local coordinate
orbits contain every protected structural instance in this table.  The
scoped pricing replay authenticates at least ten protected demands in both
phases, but does not settle the remaining authoritative columns.

It is nevertheless a harvest module, not the full rank-seven route.  The
fixed one-shot structural family reaches only `116/623` demands.  More
strongly, the separate fixed-root SCC theorem leaves `162` bad P2 roles as
singleton SCCs even after bottom constraints are deleted.  Consequently an
architecture that repairs each bad role by moving that role's own rank-seven
label must recouple rank-eight roots, cross into a larger P2/H host family,
or plant a new root bank.  This is not an absolute fixed-root socket no-go:
moving other H middles can create a new endpoint DNF for an unchanged P2
label.  The complete regenerated occurrence catalogue is therefore still
load-bearing.

## 5. Independent orbit artifacts

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  analyze_k17_rank7_p2_hh_c6_motif_orbits_20260802.cpp
  SHA-256 fb8c1372cf42e1e5b424d5799a08e28f85954218628f28977bf27e384479e0e0

  rank7_c6_motif_candidates.tsv
  SHA-256 13ebc407fbb1edb05906744d2e6f12b5da8699210980513a35f3c60de46b6bf5

  rank7_c6_motif_groups.tsv
  SHA-256 b22fee495e978c9c3576d330c7a9fb3c6ea9822611bd4cd27917f21841255938

  rank7_c6_motif.audit.json
  SHA-256 5861b1b05292020266f4c5508fb961a8c7a0303269f80ad9eb2f2aca9e1cbc44
```
