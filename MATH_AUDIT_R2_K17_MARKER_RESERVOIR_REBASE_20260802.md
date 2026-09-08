# `k=17` R2 rebase: the 96-orbit marker reservoir

**Date:** 2026-08-02  
**Status:** authenticated finite bank; host embedding remains open.  No
packing search was repeated.

## 1. Authenticated packet

The authoritative theorem is
`MATH_THEOREM_K17_MARKER_RESERVOIR_Z17_ORBIT_PACKING_20260802.md`, SHA-256
`bf072e7c74918ad729a14ba030e866de895444df85a5af02ecd2230357e40ee7`.
Its literal witness is the actual file
`scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv`
(not a `.txt` file), SHA-256
`88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403`.

All theorem-declared local hashes equal the copies under the producer root

```text
/home/amodo/or15/work/root_k17_marker_orbit_packing_20260802
```

including search audit `abbc69a34b8e92d0e8cc62f1bc9e4683e641a78bc39c7103b8938b41fc3c85c0`
and independent literal audit
`28a4d4cd6e19c4c6b77a8140c85bd1fceac11421e5eea0dd8ae0e50ea8d119ab`.

## 2. Independent replay

At the unique R2 root

```text
/home/amodo/or15/work/r2_k17_marker_orbit_replay_20260802
```

the frozen independent verifier was compiled with H100 `g++ 13.3.0`,
`-O3 -std=c++20 -DNDEBUG -Wall -Wextra -Wpedantic -Werror`, and rerun on the
frozen witness.  Its executable SHA-256 is
`9d4956c1475a270d478a9f780a8dc3edc32ee7e126842e87c562534b04ac289c`.
The regenerated audit is byte-identical to the producer audit, SHA-256
`28a4d4cd6e19c4c6b77a8140c85bd1fceac11421e5eea0dd8ae0e50ea8d119ab`.
It certifies:

* 96 base modules and `96*17=1,632` developed modules;
* 27,744 pairwise distinct typed named resources, split by ranks 5--9 as
  `1,632, 1,632, 8,160, 8,160, 8,160`;
* zero local four-window failures; and
* 6,528 occurrence-labelled buffer slots, representing 6,154 masks with
  maximum unlabelled multiplicity two.

The producer's literal verifier intentionally treated `x_mask` as the
physical witness key and ignored the ancillary `candidate` column.  A second
deterministic verifier therefore reconstructed the complete quotient graph
without running any independent-set search.  It bound every candidate ID to
its filtered-reservoir `x_mask`, obtained 330 raw modules, one rejected
module (`x_mask=12672`), 329 vertices, 1,663 edges and degree range 2--21,
and verified that all 96 bound witness vertices are independent.  Its source
SHA-256 is
`c92cd3d0fb396d2bca3df85120a273bc5ab8a117c597c71ccc52d7a93046d399`,
H100 executable SHA-256 is
`c751c653f16e035720cfd68fcbd0d59905e85a4ff00faf6c761c20e4aa0dedef`,
and replay output SHA-256 is
`a45e131a8c526432edd91f665a2413a58ad85e6e9a8c8303f38dbf6d27fe3634`.

The producer audit status string `PASS_ORBIT_SIMPLE_58` is a stale threshold
label; its numeric payload and both independent replays certify 96 modules.
There is no maximality claim.

## 3. R2 master interface

This witness is now the authoritative marker-reservoir bank for future R2
host work.  Its exact current module key is

```text
(x_mask, shift),  x_mask in the frozen 96-row witness, shift in Z/17Z.
```

The fixed data `D={0}`, `V=(1,2,3,4,5)`, `w=1`, `h=2`, rotated by `shift`,
determine the five local source masks, 17 named resources, and four labelled
buffer occurrences.  No alternative reservoir search should be substituted
for this bank.

It is not yet a serialized round-02 cut bank or an owner/q1-factor
embedding.  In particular, the 6,528 buffer occurrences have no immutable
host-position map.  Therefore the radius-three catalogue remains based on
round-02 bank SHA-256
`48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`
until a protected embedding manifest:

1. maps every one of the 1,632 module keys and all 6,528 labelled buffer
   occurrences to legal immutable host occurrences;
2. replays owner/target identities and local windows after placement; and
3. binds the resulting bank, factor, occurrence, and protected-resource
   hashes.

If that bridge changes `B0`, the primitive recut table, `A21`, all five
zero-265 rows, and the `L0/Lsucc` libraries must be regenerated.  If it is an
in-place reservation, every radius-three subset truth table must instead
carry these occurrence labels as protected resources.  Until one of those
two exact interfaces is frozen, the new reservoir does not alter the
radius-three count audit or its `NOT READY` launch verdict.

## 4. First-58 lower-q1 host extension

The factor frozen in `MATH_AUDIT_R2_K17_MARKER58_Q1_EXTENSION_20260802.md`
now binds the first 58 base orbits, after all 17 shifts and opening type 3,
to an exact spanning rank-9 degree-two factor with the complete rank-8
palette.  It contains all 986 opened five-owner/four-edge marker paths.

This closes only the owner/lower-q1 path interface.  The factor has 1,179
components and covers 13,307 of 19,448 rank-10 caps, leaving exactly 6,141
holes.  Its protected flags do not bind the omitted fifth q1 edge, the
rank-5--7 marker targets, or any source/buffer occurrence.  Consequently it
does not yet supply the protected occurrence-position bridge required in
Section 3 and does not replace the radius-three round-02 bank.

## 5. Scope

The authenticated result is exactly a quotient-orbit packing of named rank
5--9 resources with local four-window identities.  It does not bind the
6,528 occurrences physically and makes no host chronology, q1-factor,
component topology, residence, ranks 10--17, opening, exterior-window, or
compiler claim.
