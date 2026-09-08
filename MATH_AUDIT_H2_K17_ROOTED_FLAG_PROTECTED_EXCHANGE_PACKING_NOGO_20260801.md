# H2 audit: fixed rooted-flag protected exchange-packing no-go

Date: 2026-08-01

## Exact scope

This note concerns only the following restricted model built from the frozen
213,670 componentwise two-row exchange catalogue.

1. A selected exchange changes exactly its two rooted rows.
2. Selected exchanges are root-disjoint.
3. To service a dead owner, a service atom selects one exchange that repairs
   that owner in the frozen background and freezes every other rooted row
   incident with that owner.

The third condition makes each isolated witness composable, but it is a strict
restriction.  Consequently the no-go below is **not** an UNSAT theorem for the
direct final-row-option model, overlapping exchanges, the full rooted-flag
fibre, or K17.

## Independent proof verification

The exact remote source was copied from
`/home/amodo/or15/work/h2_k17_rooted_flag_owner_cover_20260801`.
Its SHA-256 is

`8a0f66a9b174d814b2da8207ff7dc58093b44669b73646bd9162cd661e7b3c1f`.

Two proof-producing Kissat runs were independently checked with local
`drat-trim`:

| face | variables | clauses | CNF SHA-256 | DRAT SHA-256 | verdict |
|---|---:|---:|---|---|---|
| changed roots at most 173 | 810,996 | 3,171,053 | `8f95cc5f06c7328a316ec8e76a800a3d435d1d2480935b60b7dcc5ffe8738ad9` | `5729df145174ac58bf2bca8ca39fd32b8aabd534f8a12537ce994762aafaed2a` | VERIFIED UNSAT |
| no changed-root cap | 563,779 | 2,675,363 | `211198669f146941a63c6d2f40c06de069c4d34edadd018d82dc56deb971cb50` | `3789f30a36d3f20101b66bb38b78fce0600252adbab0207b637a763c973f1272` | VERIFIED UNSAT |

Both solver runs terminate during propagation with zero decisions and zero
conflicts.  Each proof trims to 1,790 input clauses plus seven proof lemmas,
using 1,800 resolution steps and no RAT lemma.  Rechecking the trimmed 1,790
clauses with the original proof also returns `s VERIFIED`.  Thus the cap 173 is
irrelevant inside this protected model.

## A compact four-owner obstruction

The automatic DRAT core contains five owner service clauses, for owner orbit
indices

`0, 2, 8, 14, 163`

with respective clause sizes

`304, 227, 200, 116, 199`.

The core consists otherwise of 312 service-to-column implications, 312
column-to-changed-root implications, and 1,161 protection guards.  Owner 163 is
not necessary.  An independent literal projection gives the following smaller
minimal obstruction:

| owner id | canonical owner | incident root-orbit ids | distinct changed-root-pair options |
|---:|---:|---|---:|
| 0 | `0x001ff` | `0,1,2,3,4,5,6,7` | 100 |
| 2 | `0x0037f` | `1,2,8,15,16,17,18,19,20` | 34 |
| 8 | `0x003fd` | `0,7,14,20,25,29,32,34,35` | 30 |
| 14 | `0x005f7` | `5,13,40,46,51,55,58,61,62` | 98 |

For owner `u`, let `R_u` be its incident root set and let `p(s)` be the two
changed roots of service column `s`.  Protection says that every other
selected column avoids `R_u \ p(s)`.  Two different selected columns must also
have disjoint changed-root pairs.  These are pairwise conditions.

Now quotient optimistically by remembering only `p(s)` and even allowing two
owners to share a changed-root pair without first checking that their literal
replacement column is the same.  Exact bitset enumeration of the four menus
above gives:

1. every proper three-owner subfamily is compatible;
2. every compatible four-owner tuple forces owners 0 and 8 to share a pair;
3. the only pair that can be shared is `{7,42}`.

Return to literal columns.  On pair `{7,42}`, owner 0 is serviced only by
catalogue columns `{2058,2060,2072}`, whereas owner 8 is serviced only by
column `{2061}`.  Their intersection is empty.  Distinct literal columns on
the same two roots cannot both be selected by root-disjointness, while no one
literal column services both owners.  This contradicts simultaneous service
of owners `0,2,8,14`.

This is a four-partite typed Hall/packing obstruction: it is minimal with
respect to its four owner service clauses, although not claimed minimal in raw
CNF clause count.

## Audit artifacts

- Independent auditor:
  `scratch/audit_h2_k17_rooted_flag_protected_packing_core_20260801.py`
  (SHA-256
  `f3c944d3fcc5c84c4fc2b78fdb30c1a828e702e05560d419a4abc35cb5994b2f`).
- Uncapped audit JSON:
  `scratch/h2_k17_rooted_flag_protected_packing_audit_20260801/packing_all.independent_core_audit.json`
  (SHA-256
  `8083e2215533577232be807e35044f3fc8d5fc711666a8220fe41d28a95fe44a`).
- Cap-173 audit JSON:
  `scratch/h2_k17_rooted_flag_protected_packing_audit_20260801/packing173.independent_core_audit.json`
  (SHA-256
  `0517ca146ef34cee419b1185c14453792bad36cb370917526ea8a423a1462ca5`).
- Uncapped map SHA-256:
  `144dc717cd13ccbeb4f35064ba04a00c2d512c8c08a224e4a9f2796b6f196509`.
- Cap-173 map SHA-256:
  `276264b057b3d20a1500c96e5569ee457584e630fbe5d3b70ffbba8b8c21b862`.

The direct row-option optimizer must therefore recompute owner support from
the final selected row flags.  It must not promote these isolated service
masks to globally composable coverage clauses.
