# The p6440 compound `[2,2]` uniform-bit obstruction

**Date:** 2026-07-30

**Lane:** D, exact finite K16

**Status:** proved complete no-go in the stated atomic-cluster fibre

## 1. The branch selected

Work at the authenticated reorganized-H1 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

of length 12,873.  Its unique uncovered target is `H=0x2c6d`.

The previous theorem closed the four-site family in which the adjacent
p6439/p6440 packet, an `I0` cell, and a return cell are three clusters
separated by source-FULL open gaps.  The next smaller complete branch is the
atomic partition `[2,2]`:

1. p6439 takes one of all 16 retained unshielded `O2` values;
2. adjacent p6440 takes one of all 16 portal values;
3. `i` takes one of all 25 retained shielded `I0` rows;
4. a distinct position `t` takes an arbitrary changed nonzero value `z`;
5. the open source gap between `i` and `t` is non-FULL, while the open gap
   from p6440 to the earlier endpoint of `{i,t}` is FULL.

Thus p6439/p6440 and `i/t` are two exact compound packets, and all mixed
derivatives between the packets vanish.

The clean high-debt fallback has only 16 gate/service bases but requires two
globally arbitrary returns, whose complete reduced kernel has not been
frozen.  Its base count alone is not a valid state-space comparison.  The
`[2,2]` branch is the next branch with a complete finite reduced catalogue,
so it is the justified choice under the smaller-complete-state-space rule.

## 2. Complete geometry catalogue

The first packet has

```text
16 * 16 = 256
```

exact profiles.  Direct endpoint partition and the mixed OR-rectangle
formula agree for all 256, and the profiles are all distinct.

The complete non-FULL return corridors around the three possible `I0`
positions are

| `I0` position | alleles | complete return corridor | sites per allele |
|---:|---:|---|---:|
| 6606 | 16 | `[6587,6605] union [6607,6626]` | 39 |
| 7984 | 8 | `[7958,7983] union [7985,8013]` | 55 |
| 9726 | 1 | `[9709,9725] union [9727,9742]` | 33 |

Consequently the second packet has

```text
16*39 + 8*55 + 1*33 = 1,097
```

allele/site bases, and the exact packet-pair catalogue has

```text
256 * 1,097 = 280,832
```

geometries.  Quantifying every arbitrary nonzero changed value gives

```text
280,832 * 65,534 = 18,404,044,288
```

raw literal assignments.  This raw fibre is not sampled or truncated.

## 3. Exact OR-convolution/MITM formulation

For a target `T`, write `m(T)` for its source interval multiplicity.  Let
`P(T)` be the source-relative beta column of the first packet.  For a fixed
second-packet geometry `{i,t}`, let `ell_T` be the old multiplicity of all
source intervals affected by that packet.

After fixing the `I0` allele at `i`, partition the new affected intervals
into those not containing `t` and those containing `t`.  The former
contribute a constant `A_T`.  Group the latter by the OR `c` of all their
fixed cells and let `mu_c` be the exact multiplicity.  If `z` is the new
value at `t`, their total new multiplicity is

```text
G_T(z) = A_T + sum_c mu_c * 1[c OR z = T].       (3.1)
```

Identical contexts are aggregated only with their multiplicities retained.
The second-packet column is `ell_T-G_T(z)`.  Since the inter-packet gap is
source-FULL, the exact final multiplicity is

```text
m_final(T) = m(T) - P(T) - ell_T + G_T(z).       (3.2)
```

Hence final coverage is equivalent to the integral inequalities

```text
G_T(z) >= 1 - m(T) + P(T) + ell_T               (3.3)
```

for every target.  This is the exact OR-convolution/MITM; there is no
hole-count, fractional, independence, or joint-OR approximation.

There is an even earlier exact separator in this fibre.  Apply the first
packet and the `I0` allele, but not the return.  Every one of the 6,400 such
three-edit bases has both

```text
A = 0x286d,
B = 0x287d = A union 0x0010
```

as unit deficits.  Any new witness for either missing target after changing
only position `t` must contain `t`.

For a target `T`, let `C_t(T)` be the OR of the maximal `T`-compatible
context on both sides of `t` in that exact three-edit base.  A value `z`
creates a `T` witness through `t` if and only if

```text
T minus C_t(T) subseteq z subseteq T.            (3.4)
```

The exact catalogue proves, for every one of the 280,832 geometry rows,

```text
0x0010 subseteq B minus C_t(B).                  (3.5)
```

Thus a `B` witness forces `0x0010 subseteq z`.  But `0x0010` is not a bit of
`A`, while every `A` witness requires `z subseteq A`.  No value can witness
both targets.  Equivalently, the Boolean interval intersection in (3.4) is
empty before any final capacity test.

### Theorem 3.1

No word in the complete p6440 compound `[2,2]` fibre is universal.

### Proof

The geometry table in Section 2 exhausts every permitted second packet and
every first-packet/`I0` choice.  In any completion, the only newly changed
cell after the three-edit base is `t`, so both missing targets `A,B` require
witnesses through `t`.  Equations (3.4) and (3.5) force `z` simultaneously to
omit and contain bit `0x0010`, a contradiction.  This excludes all 65,534
changed nonzero values at once for every geometry.  Therefore none of the
18,404,044,288 raw assignments is universal.  QED.

## 4. Exact ledgers

The four positive-support classes of the three-edit bases are

```text
{286d,287d,2c6d}                         3,776 states;
{286d,287d,2c6d,846d}                   1,024 states;
{286d,287d,2c6d,846d,a46d}              1,024 states;
{286d,287d,2c6d,a46d}                     576 states.
```

Their geometry counts by `I0` position are

```text
p6606: 159,744;
p7984: 112,640;
p9726:   8,448;
total:  280,832.
```

Every row has exactly one broken inter-singleton gap.  The complete lower-
versus-upper obstruction masks are

```text
0x0410:170688, 0x0c10:1920, 0x2c10:9216,
0x8c10:28352, 0xac10:70656.
```

All contain `0x0010`, and the extracted target certificate histogram is the
single row

```text
0x287d > 0x286d @ 0x0010 : 280,832.
```

Accordingly the exact witness-pruned catalogue has zero nonempty intervals
and zero candidate values.  There is no candidate word to replay.

## 5. Independent audit

The primary C++ program reconstructs the retained atlas, checks all 256
first-packet OR rectangles, constructs every second-packet corridor, and
computes the exact three-edit target contexts for every geometry.  Its
ordered catalogue digest is `103571e39210c840`.

The independent C++ checker does not include the primary source or consume
its row enumeration.  It freezes the authenticated primitive alphabets,
reconstructs every three-edit beta by a generic first-edited/last-edited
interval partition, rediscovers all four support classes and all three
corridors, and obtains each `B` context by literal outward scanning.  It
independently proves the same `0x0010` conflict in all 280,832 rows; its
context digest is `c2456d95a147ec49`.

Both runs used one H100 CPU in the exclusive directory

```text
/home/amodo/or15/work/threadD_k16_p6440_compound22_20260730
```

under 512 MiB address-space caps, with no swap and no `/dev/shm` writes.
The primary run used 2.04 seconds and 23,552 KiB maximum RSS.  The
independent run used 2.08 seconds and 12,288 KiB maximum RSS.  A lightweight
hash-closure manifest checks both statuses, counts, hashes, resource exits,
support histograms, and the uniform certificate.

Authoritative artifacts:

```text
scratch/audit_threadD_k16_p6440_compound_return_catalogue_20260730.cpp
  SHA 687934581a7095fb5cd679a9d909a37077240aee220f4411f452f60d38861017
scratch/threadD_k16_p6440_compound22_20260730/compound22.catalogue.audit.json
  SHA b7d9faff8d79e127a25326fd74c88588f9019c4e584c846cf94895b0fcf7321f
scratch/audit_threadD_k16_p6440_compound22_pair_obstruction_independent_20260730.cpp
  SHA 96d6dd86c42b3add493e4eed75ea6044c3c7b21bfaaa8523eacf9076c98c8a52
scratch/threadD_k16_p6440_compound22_20260730/compound22.independent.audit.json
  SHA aa31ed87aff4f2bb98092ce4cee550177e2e9824df0e66f2f8b0de1c7dc58da8
scratch/audit_threadD_k16_p6440_compound22_manifest_20260730.py
  SHA 3322fdecdea9d54c45f3380916aa77114c425ffd6ffea3d18dc4f88ac0e3663a
scratch/threadD_k16_p6440_compound22_20260730/compound22.manifest.audit.json
  SHA 12d4337a71b9da69987d67cdf58917e23c3873208aefa74987d2a5f6cf2b4ecd
  payload 00666a966e39c98ca7ae0f631ffc335d1d9a5ff2f1b929bd0ec8ae1af8a613b9
scratch/threadD_k16_p6440_compound22_20260730.provenance.txt
  SHA eba6637d2979ab2a89ae9d81699a67f0cbba686d34ca0ea81ce685a61c686593
```

## 6. Exact scope boundary

This theorem is disjoint from the named active campaigns:

- it has four genuine changed sites, so it is outside radius3;
- its mandatory `I0` position is one of `6606,7984,9726`, outside both the
  frozen S13 support and collar594's 18 editable positions;
- it uses the reorganized-H1 source and mandatory p6439/p6440/`I0` service
  signature, not Thread A's H2 donor, service-5462, and R19-return signature;
- it contains no high-debt joint-service primitive.

It closes only the atomic `[2,2]` branch: the `I0`/return gap is non-FULL and
the two packets are separated by a FULL gap.  It does not close a return
interacting with the first packet (`[3,1]`), a return joining both packet
regions, two broken gaps (`[4]`), a high-debt or joint-service primitive,
two or more return cells, another portal or source basin, or unrestricted
K16.

The next clean high-debt fallback is the unique shielded minimum

```text
p9958: 0x2a01 -> 0x806d
```

with seven unit debts and 16 gate profiles, followed by a complete two-return
MITM.  Its dynamic two-return kernel must be frozen before search.

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
