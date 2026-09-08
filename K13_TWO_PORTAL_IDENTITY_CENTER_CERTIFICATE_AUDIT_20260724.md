# Certified no-go for the first coherent two-portal `k=13` tier

Date: 2026-07-24

## Theorem certified

Let `B` be the supplied exact 926-entry nonzero `k=12` word.  For either
orientation `O` of `B`, choose an integer

```text
2 <= cut <= 923
```

and delete the three adjacent oriented entries

```text
O[cut-1], O[cut], O[cut+1].
```

Let `L` and `R` be the retained entries before and after `cut`, respectively,
and let `pi` be any permutation of the twelve old bit coordinates.  No word

```text
(4096 | pi(L)) || 4096 || B || 4096 || (4096 | pi(R))
```

covers all 8,191 nonzero 13-bit masks.

The theorem covers exactly

```text
2 * 922 * 12! = 883,278,950,400
```

parameter assignments.  It is the identity-relative-map first tier of the
larger coherent two-portal family in
`K13_TWO_PORTAL_COHERENT_SEAM_PORTFOLIO_20260724.md`.

## Certificate partition

The 922 structural states were partitioned into fifteen immutable shards:

* fourteen shards of 64 states;
* one shard of 26 states.

The same exact partition was solved in both lifted orientations.  Thus there
are thirty CNFs and thirty DRAT proofs.  Every proof was accepted by
`drat-trim` with an explicit

```text
s VERIFIED
```

and no SAT marker or candidate word occurred.

The largest generated block had 40,911 clauses.  The full retained
certificate directory occupies 39 MiB on Purple RunPod at

```text
/root/k13_two_portal_design_20260724/cert_center_identity_v2
```

No search, CNF generation, or proof checking was run on the user's machine.

## Independent replay audit

`scratch/audit_k13_two_portal_identity_certificates.py` independently:

1. verifies that the state shards contain every row
   `(cut-1,cut,cut+1,cut,+1,0)` for `cut=2,...,923`, exactly once;
2. checks fifteen certificates in each orientation and no SAT marker;
3. checks every CNF header against its recorded variable/clause statistics;
4. regenerates every CNF, map, and stats file byte-for-byte from the immutable
   base and shard;
5. reruns `drat-trim` freshly on all thirty CNF/proof pairs; and
6. hashes every base, shard, CNF, map, stats, proof, and original check log into
   one compact JSON ledger.

Its RunPod output is

```text
PASS shards=15 states_per_orientation=922 certificates=30 \
assignments=883278950400 \
ledger_sha256=56f8a913fe4b086599af9f68bacfc3e789fad5057e2b62ad676efd9238f7cb0f
```

The compact ledger is
`scratch/k13_two_portal_identity_center_certificate_ledger.json`.

## Relevant hashes

```text
certificate ledger
  56f8a913fe4b086599af9f68bacfc3e789fad5057e2b62ad676efd9238f7cb0f
independent certificate auditor
  e32642e5a2a4fc980444e0d8f7e604f7b09fcb7088335287518277979c27cafc
exact CNF generator
  8a7675bba778e4c24e11501829b238caedf09eb4554819e2e0b627797949e179
independent reduction audit
  53ad98ea576d3d5bf564bd3950b8546de050e39e8ea29aa43754162b09bdb917
```

The production wrapper was corrected before the certified run so that
`SAT=exit 0`, a marker-backed UNSAT block is `exit 1`, and any setup failure
without the corresponding marker stops the portfolio.  The final wrapper
hashes used for this identity-tier run were

```text
scratch/run_k13_two_portal_block.sh
  8310a24626724b56ec70689ea1d3f6e40e5369fb6a82a1bdbbb104212b81e0d4
scratch/run_k13_two_portal_portfolio.sh
  5821a2b63225869461780b6b592300753c6e89b0f1031ccafbea4dd2e98acbe8
```

The block runner was later extended only with post-verification gzip support
for the larger `tau=+2` certificates; that successor and its hash are recorded
in `K13_TWO_PORTAL_TAU_P2_CERTIFICATE_AUDIT_20260724.md`.

The complete identity-tier certificate directory is now preserved at

```text
scratch/certificates/k13_two_portal_20260724/cert_center_identity_v2
```

and its 150 ledgered immutable artifacts were rehashed after transfer:

```text
PASS certificates=30 hashed_artifacts=150 \
ledger_sha256=56f8a913fe4b086599af9f68bacfc3e789fad5057e2b62ad676efd9238f7cb0f
```

The verified Purple source directory was removed only after this byte-level
copy check, together with the corresponding `tau=+2` source, to recover root
disk space.

## Scope

This formally excludes only the adjacent-three-deletion, identity-relative-
map tier.  The nonidentity dihedral relative maps and the endpoint-plus-seam
structural lane remain available.  The certified finite-`k` bounds do not
change.
