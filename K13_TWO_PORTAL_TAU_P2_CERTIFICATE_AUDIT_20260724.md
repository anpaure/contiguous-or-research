# Certified no-go for the `tau(i)=i+2` coherent two-portal tier

Date: 2026-07-24

## Theorem certified

Let `B` be the exact 926-entry nonzero `k=12` word and let `O` be either
orientation of `B`.  For each

```text
2 <= cut <= 923
```

delete `O[cut-1],O[cut],O[cut+1]`.  Let `L` and `R` be the retained entries
before and after the cut.  Put

```text
tau(i) = i+2 mod 12
```

on the old bit coordinates.  For every old-bit permutation `pi`, the word

```text
(4096 | pi(L)) || 4096 || B || 4096 || (4096 | pi(tau(R)))
```

fails to cover at least one nonzero 13-bit target.

This formally excludes

```text
2 * 922 * 12! = 883,278,950,400
```

additional parameter assignments.  Together with the previously certified
identity-relative-map tier, two fixed relative maps and

```text
1,766,557,900,800
```

parameter assignments in the adjacent-three-deletion center lane are now
formally excluded.

## Why this map was selected

A bounded Purple-only profile pass completed all eleven nonidentity rotations
and three reflections before temporary full-tier CNFs approached the root-disk
guardrail.  The temporary CNFs were stopped and deleted without touching any
unrelated process.  Among those fourteen completed maps, rotations by `+2`
and `-2` tied for the smallest exact rank-impossible provider count.

For `tau(i)=i+2`, the two oriented profiles have:

| orientation | structural states | holes | providers | rank-impossible hole obligations |
|---|---:|---:|---:|---:|
| forward | 922 | 494,705 | 868,163 | 122,452 |
| reversed | 922 | 499,701 | 878,530 | 123,098 |
| total | 1,844 | 994,406 | 1,746,693 | 245,550 |

The compact retained profile ledgers are:

```text
scratch/k13_two_portal_nonidentity_profile_forward.tsv
  bef71f2030e6a9b6545cc199a07bbb6cc3e0dc0e7221d0e2d0c72120d6b9b8dd
scratch/k13_two_portal_nonidentity_profile_reverse.tsv
  4dc5d3109e0ffac09842801e0aab3b95b38b5cd31d5722cca93591d964cd0a12
```

No unprofiled map is claimed to be worse; the profile was only a bounded
choice rule for the next exact tier.

## Search and certificate partition

The 922 states were partitioned into fifteen immutable 64-state-or-smaller
shards and searched in both orientations on free allowed Purple CPUs 5 and
11.  All thirty search blocks returned no candidate.

The same thirty formulas were regenerated in certification mode.  Every
Kissat UNSAT result was checked immediately by `drat-trim` and received an
explicit

```text
s VERIFIED
```

before its marker was written.  To respect Purple's root-disk limit, each
verified CNF, map, and DRAT was then gzip-compressed before proceeding to the
next shard.  At most one uncompressed shard per worker was live.

There are exactly thirty `UNSAT_VERIFIED` markers, thirty check logs containing
`s VERIFIED`, and no `SAT_VERIFIED` marker.  The compressed certificate
directory occupies 183 MiB at

```text
/root/k13_two_portal_design_20260724/cert_center_tau_p2
```

## Independent replay

`scratch/audit_k13_two_portal_fixed_tau_certificates.py` independently:

1. verifies that the fifteen shards partition exactly the 922 requested
   `(cut-1,cut,cut+1,cut,+1,2)` states;
2. checks both orientations and absence of SAT markers;
3. decompresses one certificate block at a time;
4. regenerates its CNF, map, and stats byte-for-byte;
5. freshly reruns `drat-trim` on its CNF/proof pair; and
6. hashes every immutable input and certificate artifact into one JSON ledger.

The audit completed successfully and wrote the ledger only after all thirty
fresh proof checks passed.  Its terminal result is

```text
PASS tau=1,2 shards=15 states_per_orientation=922 certificates=30 \
assignments=883278950400 \
ledger_sha256=9c5e006a54a94b02dfe78fb6ab0c811cdb912731f9a07f481e1fba49213850d5
```

The compact locally preserved ledger is

```text
scratch/k13_two_portal_tau_p2_certificate_ledger.json
```

with SHA-256

```text
9c5e006a54a94b02dfe78fb6ab0c811cdb912731f9a07f481e1fba49213850d5
```

## Reproducibility hashes

```text
exact CNF generator
  8a7675bba778e4c24e11501829b238caedf09eb4554819e2e0b627797949e179
fixed-tau manifest builder
  a97b216b598ca6b4e28899704b196c30d676846e1bd375f16b1f03be1a66e1e5
compression-capable block runner
  baf1b29fa937f87262f5afa3274121c8ff7f0a418165a56baf9299f2802b1d7c
marker-checking portfolio wrapper
  5821a2b63225869461780b6b592300753c6e89b0f1031ccafbea4dd2e98acbe8
independent fixed-tau certificate auditor
  387e3697bf489738f2690e8bc33797cb54c6cb25952de33025a4102dba722e54
```

## Durable preservation status

The full 183 MiB compressed certificate set was copied byte-for-byte from
Purple to

```text
scratch/certificates/k13_two_portal_20260724/cert_center_tau_p2
```

The lightweight verifier
`scratch/verify_k13_two_portal_certificate_copy_hashes.py` checked all 150
ledgered CNF, map, proof, stats, and original-check artifacts in that copy and
returned

```text
PASS certificates=30 hashed_artifacts=150 \
ledger_sha256=9c5e006a54a94b02dfe78fb6ab0c811cdb912731f9a07f481e1fba49213850d5
```

The source directory had already passed full CNF regeneration and thirty
fresh DRAT checks on RunPod.  After the copied bytes were verified against
that audit ledger, the two explicitly named identity and `tau=+2` source
directories were removed from Purple, recovering 222 MiB.  The local copy is
now the durable full-certificate source; the compact ledger alone is not being
treated as a substitute for the proofs.

## Scope

This result excludes one nonidentity relative map in the center lane.  The
other 22 nonidentity dihedral maps and the entire endpoint-plus-seam lane
remain open.  No finite upper or lower bound changes.
