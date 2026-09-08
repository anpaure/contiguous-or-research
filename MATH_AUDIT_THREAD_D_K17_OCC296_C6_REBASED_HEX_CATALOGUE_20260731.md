# Thread D: boundary-correct occurrence296+C6 incidence-hex catalogue

Date: 2026-07-31  
Status: **PASS exact catalogue and independent replay; no compatible packing or K17 claim**

## 1. Frozen fibre and scope

The catalogue is rebuilt on the frozen occurrence296+C6 one-cycle factor,
not inherited from the earlier OPTIMAL28 factor.  Its literal owner cycle has
SHA-256

```text
a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49.
```

The occurrence flow and residual assignment have SHA-256 values

```text
079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f
6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4.
```

The generator scans all

\[
 {17\choose7}{10\choose3}=2,333,760
\]

ambient incidence-hex identities.  It does not filter through the old set of
44,917 applicable identities.  A column is retained exactly when one of its
two incidence phases is present, the opposite phase is absent, and its three
moving owners avoid the 4,108 marked owners.  A marked fixed-other endpoint is
allowed: its incidence is unchanged, so the 134 marked packet signatures are
preserved literally.

## 2. Exact forest hazard theorem

Independent H2 reconstruction gives 296 strict internal residence collars in
the unmarked occurrence-macro forest, on 157 components, with weighted debt
478.  Greedy interval scheduling in each forest path gives an exact packing of
197 pairwise edge-disjoint support intervals.  Since an incidence hex removes
three old incidences, every pure-hex cover obeys

\[
                         |\mathcal H|\ge\lceil197/3\rceil=66.       \tag{2.1}
\]

All 296 rows have at least one column.  These rows must not be confused with
the final-cycle complement defects `230/94`, or the nonflat-row defects
`503/503`; those are different ledgers.

## 3. Complete rebased column and topology census

The final factor has 45,024 applicable identities and 28,121 marked-safe
columns.  Of these, 2,100 hit at least one of the 296 forest hazards, 8,252
have a positive isolated rank-ten gain, and 9,879 are active in at least one
of those two senses.  The remaining columns are retained because they may be
return or topology helpers.

Applying one column gives the exact owner-factor topology profile

| topology | columns |
|---|---:|
| one cycle | 13,875 |
| two cycles | 10,620 |
| three cycles | 3,626 |

Thus a cycle-preserving master and a forest-first asymmetric master are
genuinely different faces of the same complete catalogue.

The old-to-new marked-safe identity transition is

| class | identities |
|---|---:|
| common, same orientation | 15,452 |
| common, reversed orientation | 111 |
| old only | 12,370 |
| new only | 12,558 |

Among the old 5,433 hazard-active identities, 3,476 remain applicable with
the same orientation, none reverse, and 1,957 cease to be marked-safe
applicable.  This proves that reusing the old catalogue would be incomplete
and partly invalid.

## 4. Exact incidence resources

Every exported column contains its three removed and three added
colour-owner incidences and its three source-edge rethreads.  The complete
resource tables contain

| resource family | rows | nontrivial conflict cliques |
|---|---:|---:|
| removed incidence | 35,744 | 25,575 |
| added incidence | 63,825 | 18,225 |

At most one chosen column may use a row of either family.  These constraints
are exact for simultaneous incidence compatibility.  Each individual column
has zero signed degree at every owner and every lower colour.

## 5. Boundary-correct rank-ten ledger

The physical zipper is linear.  Its omitted closing edge has lower colour

\[
 c_\partial=6394,
 \qquad \partial c=\{7418,71930\},
 \qquad 7418\cup71930=72954.                           \tag{5.1}
\]

The target 72954 has one other physical provider.  This is why a cyclic audit
has the same 1,585-hole count despite being wrong columnwise.  The corrected
catalogue removes the closing occurrence from the baseline load and declares
all four rethreads of colour 6394 unexposed in their isolated rank-ten delta.

After this correction there are 1,585 rank-ten holes.  Ten have no
**single-column** provider; the maximum isolated support is 14.  This is not a
compound obstruction.  If two compatible columns change opposite endpoints
of one colour, the final edge has an endpoint-pair cross term, so isolated
column deltas do not add.  Any master must reconstruct both final endpoints
of every touched colour before enforcing rank-ten coverage.

## 6. Independent verification and exact boundary

The independent verifier:

1. reconstructs the occurrence forest and marked packet through the frozen
   H2 code;
2. rebuilds all 296 collars and the 197-interval packing;
3. rescans all 2,333,760 ambient identities;
4. checks all 28,121 persisted columns, their phase/orientation, packet
   preservation, source-edge rethreads, and one-column topology;
5. rebuilds both resource-clique tables; and
6. recomputes every rank-ten provider row after omitting (5.1).

It returns

```text
PASS_INDEPENDENT_BOUNDARY_AWARE_OCC296_C6_HEX_CATALOGUE_REPLAY.
```

This proves an exact input atlas for the next compatible pure-hex or
split/merge master.  It proves neither that 66 compatible columns exist nor
that the ten unsupported isolated holes cannot be produced by endpoint-pair
cross terms.  Residence, rank 11/12 accumulated-union coverage, common-cap
matching, and literal compilation remain downstream gates.  Promotion to an
arity-two packet is justified only after an exact pure-hex conflict/core
identifies the responsible hazard/resource components.

## 7. Frozen artifacts

- Generator:
  `scratch/audit_threadD_k17_occ296_c6_rebased_hex_catalogue_20260731.py`  
  SHA-256 `866c26824cfc281c0701c099c92100b1a962ae410f0385dd2fdb5c79349589d8`.
- Boundary-correct catalogue:
  `scratch/threadD_k17_occ296_c6_rebased_hex_catalogue_20260731.boundary_correct.audit.json`  
  SHA-256 `b478ed869714760321826e8010cdd328b2a30904e2e8cecfc9203f5eb4cf5a39`;  
  payload `a8c0c306eed583b6b831a4deba456a79241a75a20183a21ea17281e09037379a`.
- Independent verifier:
  `scratch/verify_threadD_k17_occ296_c6_rebased_hex_catalogue_20260731.py`  
  SHA-256 `13b5ff08a88faf78a229188505a3a8383f6c3ba23e828709b0ffb819551b4757`.
- Independent audit:
  `scratch/threadD_k17_occ296_c6_rebased_hex_catalogue_20260731.boundary_correct.independent.audit.json`  
  SHA-256 `2b16a9b405dd36c8902d2c561bd81a458fcd05e99282b373a712dc4d613ee2e4`;  
  payload `c4582b5273ada12857dfa7f61d1fa2a45e142aefb027b617f03a75cd79a2a634`.

The generator used 13.23 seconds wall time and 967,676 KiB RSS; the independent
replay used 7.19 seconds and 401,136 KiB RSS.  Both ran as one H100 CPU process
under a 2 GiB address-space cap.
