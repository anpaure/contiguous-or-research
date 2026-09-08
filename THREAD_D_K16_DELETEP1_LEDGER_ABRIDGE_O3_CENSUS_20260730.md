# K16 delete-p1 sparse-ledger A-bridge: exact O3 census

Date: 2026-07-30

Status: exact scoped exhaustion; no length-12,873 word found; global gap remains

\[
                         12873\le \nu(16)\le12874.
\]

## 1. Frozen lineage and corrected ledger

The authenticated upper word is

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Relative to `scratch/k16_append0200_12874_onehole.word`, exactly twelve—not
fourteen—positions change:

\[
0,1,3,4,6436,6438,6439,6440,6442,12871,12872,12873. \tag{1.1}
\]

Delete zero-based position `1`.  The resulting word

```text
W = scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

has length `12873` and sole hole

\[
H=11373=0x2c6d.                                          \tag{1.2}
\]

The surviving image of (1.1) is

\[
\Lambda=\{0,2,3,6435,6437,6438,6439,6441,
           12870,12871,12872\}.                          \tag{1.3}
\]

Every deletion-plus-one-substitution basin with at most three holes is
already closed, and radius at most two around `W` is already closed.  The
family below is a genuine three-site endpoint family.  It does not invoke the
active `(4,9,4)`, `(5,9,4)`, or 44-position crossover formulas.

## 2. The debt-one gate

Put

\[
A=43117=0xa86d,\qquad g=6440,
\]

and observe in `W` that

\[
W_{6438}\vee W_{6439}=0x286d,qquad
W_{6438}\vee W_{6439}\vee W_g=A.                       \tag{2.1}
\]

The second interval is the unique `A` witness.  For every

\[
z_s=0x0440\vee s,\qquad s\subseteq0x002d,               \tag{2.2}
\]

we have

\[
W_{6438}\vee W_{6439}\vee z_s=H.                       \tag{2.3}
\]

There are exactly sixteen prescribed values in (2.2).  Direct literal replay verifies
that replacing `W_g` by any one of them leaves exactly the sole hole `A`.
Moreover every `z_s` contains bit `0x0400`, which `A` omits.  Therefore no
new `A` witness can contain the gate position.  The gate is an exact witness
transport `A -> H`, not a scalar approximation.

## 3. Sparse ledger A-bridge

Choose two sites `p<r` from `Lambda`, outside the protected interval
`[6438,6440]`, and require one final `A` witness containing both endpoints.
Because that witness avoids `g`, every fixed cell between its endpoints must
be an `A`-submask.  Extend through every adjacent compatible fixed cell and
let `F_pr` be their maximal OR, excluding `p,r`.

This exact compatibility scan leaves only

| `(p,r)` | maximal interval | `F_pr` | private targets |
|---|---|---:|---:|
| `(0,2)` | `[0,2]` | `0x2069` | 15 |
| `(0,3)` | `[0,3]` | `0x206d` | 19 |
| `(2,3)` | `[1,3]` | `0x2069` | 17 |
| `(6435,6437)` | `[6435,6439]` | `0xa86d` | 20 |
| `(12870,12871)` | `[12870,12871]` | `0` | 16 |
| `(12871,12872)` | `[12871,12872]` | `0` | 14 |

For replacement endpoint values `u,v`, the required `A` interval exists if
and only if

\[
0<u,v\subseteq A,qquad F_{pr}\vee u\vee v=A.           \tag{3.1}
\]

The maximal-context implication is exact: any smaller compatible context is
contained in `F_pr`, which remains inside `A`, so a smaller witness extends
to the displayed maximal interval.  Conversely every `A` witness containing
both endpoints supplies (3.1).

The six relaxed endpoint counts are

\[
27584,36736,27584,65025,6559,6559,                    \tag{3.2}
\]

for total `170047`.  Requiring both endpoint values to differ from their
incumbents leaves `169919` genuine pairs.  Combining them with all sixteen
gates gives exactly

\[
                         16\cdot169919=2718704          \tag{3.3}
\]

genuine three-site words.  On every adjacent endpoint support, zero rows
preserve the incumbent pair OR, so this atlas does not duplicate the earlier
adjacent pair-OR braid census.

## 4. Exact private-target criterion

Fix one support and order its edited sites as `s0<s1<s2`.  A target is
private if every old `W` witness meets at least one edited site; add the old
hole `H`.  Removing the three sites splits `W` into four fixed components,
so exact old interval multiplicities determine this private set.  Every
nonprivate target retains a disjoint old witness.

An affected interval meets a nonempty consecutive site class among

\[
\{0\},\{1\},\{2\},\{0,1\},\{1,2\},\{0,1,2\}.           \tag{4.1}
\]

For a class `E`, its OR is exactly

\[
F\vee\bigvee_{i\in E}x_i,                              \tag{4.2}
\]

where `F` ranges over the finite fixed suffix/full-gap/prefix bases for that
class.  The implementation precomputes every distinct `F`.  A candidate is
universal if and only if every private target occurs in one of the six tables
(4.2).  Thus the census is an exact literal criterion, not Hall, marginal,
or independent-provider relaxation.

The implementation independently replays:

* all sixteen gate-only words;
* sixteen stratified candidates on each of the six supports; and
* every newly retained support minimum and every putative zero.

## 5. Exact result

The `-O3 -march=native` H100-CPU run exhausts all `2718704` candidates and
finds no universal word.  Its exact global hole histogram is

```text
holes : candidates
2     : 11264
4     : 36352
5     : 24160
6     : 497648
7     : 113552
8     : 439296
9     : 32768
10    : 523264
12    : 1040400
```

The floor is two.  One retained optimum is

```text
p=0, r=2, u=0xa86d, v=0x006d, gate=0x0440,
holes {18553=0x4879, 26745=0x6879}.
```

It is materialized as

```text
scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
  threadD_k16_deletep1_ledger_abridge_o3_20260730.best.word
SHA-256 452055e47d7f7c331dfab6cbfef5a88ced2ed9bdfa6cb817a920640628d8b525.
```

Independent suffix-state and start-by-start replays both give precisely that
two-hole set; this does not assert that every minimum row has the same two
holes.  The run used one CPU, `6552` KiB maximum RSS, no swap, and
`0.33` seconds wall time.  Program exit `1` is the declared exhausted-negative
exit, not a resource failure.

The independent checker replays lineage, domains, counts, the saved minimum,
and both literal coverage calculations.  It does not independently repeat all
`2718704` rows; exhaustion rests on the audited C++ six-class implementation.

## 6. Scope and next braid

This proves:

> No word obtained from the frozen delete-p1 root by one of the sixteen
> prescribed exact
> debt-one gates and two genuine surviving-ledger endpoint edits, with a final
> `A` witness containing both endpoints, is universal.

It does not exclude:

* an `A` witness using only one repair endpoint;
* repair sites outside the surviving image `Lambda` of the 12-change ledger;
* a three-cell packet not passing through the sixteen prescribed debt-one
  gates;
* the full one-site-provider-plus-two-repair or two-site-provider-plus-one-
  repair radius-three branches; or
* an unrelated length-12,873 word.

The next clean invariant family is the adjacent triple-OR braid

\[
(x,y,z)\mapsto(u,v,w),\qquad u\vee v\vee w=x\vee y\vee z,
\]

which changes two adjacent pair ORs simultaneously and is not reducible to
the exhausted adjacent pair-OR catalogue.  This note neither freezes nor
claims a census of that larger family.

## 7. Reproducible artifacts

```text
C++ source
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730.cpp
  SHA-256 22cd69fa05f6ac63ce461b51a38651d774d340774863fb49f73f602d72cd52da

H100 binary
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
    threadD_k16_deletep1_ledger_abridge_o3_20260730
  SHA-256 5e9994002d8ebd01f3f2e276d429677bc76629e1fac2bc1705c0b8a8ea91b778

raw exhaustive audit
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
    threadD_k16_deletep1_ledger_abridge_o3_20260730.raw.audit.json
  SHA-256 13efc9fc7518a22f12e1d34be2bb4cd60ddb5cbd49d943cd7ca269a782c6f629

resource transcript
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
    threadD_k16_deletep1_ledger_abridge_o3_20260730.resource.txt
  SHA-256 e49a0d355a77c7385795e6481cac84a0c44c05c2f5d4e58afd9de3ebb219f7fc

build provenance (compiler version and exact compile/run commands)
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
    threadD_k16_deletep1_ledger_abridge_o3_20260730.build.txt
  SHA-256 a74c1191310822f0f9a783e71956f5e52b368d25318a6d3699fdffe47ea9c34f

independent checker
  scratch/audit_threadD_k16_deletep1_ledger_abridge_o3_20260730.py
  SHA-256 c4ad7b11312d04365bfbd0f6596f54edae94c4fef603ff054f45a4174e45364a

independent audit
  scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730.audit.json
  SHA-256 5ea50a9319eccba3c80c0961feba72c78da4b382b7e8fe28ff817c25bb6daf68
  payload d4a24b73c236146bfab0b58827d01197c4a7194b2bb608758d176664f6c2c8b1
```
