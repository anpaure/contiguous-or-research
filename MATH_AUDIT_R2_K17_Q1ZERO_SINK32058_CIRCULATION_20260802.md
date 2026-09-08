# R2 audit: K17 sink-32058 circulation and q1-zero promotion

**Date:** 2026-08-02  
**Status:** read-only authentication of the promoted central-q1 factor and
literal support-seven circulation. No search or solver was launched by R2.
The audit excludes residence, deeper-upper rows, source, compiler, opening,
exterior windows, and a word.

## 1. Authenticated trajectory

All artifacts below are under

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802
```

The independently certified three-hole checkpoint is

```text
model       weighted3.independent.model
model SHA   b2b5d2c6dfa14552b4b80c2c0d69920096dc9e4b9bbc3f5c35a3360df90a416c
audit SHA   9be8b2b04c3163343eff2c7a87b1455eafc0612c393bec89172197dc1be23ba4
extended    77110b603c31bb48fa00385229f515b0c216e060ac729b04c3dce5552183695c
q1 cut      9dbe83fda5b5aed71e70309844982d7cac2f59f7fe77f3e35d951b6bae694bb7
coverage    19,409 / 19,412
missing     32058, 103907, 109870
```

The independently certified one-hole checkpoint is

```text
model       transport3_2.best.model
model SHA   be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213
literal-v2  000bbc75702f9ac78bfcae6625c3846a897831371d7c42e9ed9a32ae95c06e3b
replay      d48cc6fc8db79ca7824db22ad2251b90c1082eddcc7694bfe238a504d1903c26
extended    7e9ff1a6702de4cb6712e3155c4fbba92bfec89a1963a8ceba56fc79da48c92d
q1 cut      f8e989dba147cb17f43dd540e005cf6ab45317cf1678f8458975ea05f484cace
coverage    19,411 / 19,412
missing     32058
```

The literal one-hole audit reports 48,620 selected incidences, one component,
all 16,261 guards true, and an exact 45-literal missing row. Files named
`onehole.independent.*` at the root are zero-byte abandoned placeholders and
are not evidence; the authenticated replay is the `transport3_2` package
above.

## 2. Exact final circuit

The debt-two audit is

```text
debt2_1_cap2m.audit.json
SHA-256 1065dd9ecf422a806acc361162f73606d25b15b08d1e83777a783a3d131b54ad

debt2_1_cap2m.debt2_cycles.tsv
SHA-256 3c5a86ac5dda09536a352ef53ad3cf7ae44bad424a591a88938344de08c26032
```

Its exact census at the one-hole input is

```text
guard-safe C6 plus star-C8 rows      14,503
catalogue including chosen debt row  14,504
loss-safe residual arcs            129,227
forced 32058 installs              20
debt-two return paths              11
root-simple                         11
guard-safe                          11
connected positive                   6
best score / support                 1 / 7
```

The selected row has `forced_arc=83588`, gain `32058`, an empty loss field,
and `connected=1`. Its literal support is

```text
roots      29978,30002,54578,50483,50455,54550,21790
old vars   53759,53841,100178,91285,91208,100072,36593
new vars   53760,53846,100171,91279,91213,100073,36592
```

The authenticated incidence map decodes these as

| root | fixed owner | old owner | new owner | old q1 | new q1 |
|---:|---:|---:|---:|---:|---:|
| 29978 | 32026 | 29982 | 30010 | 32030 | 32058 |
| 30002 | 30006 | 30010 | 62770 | 30014 | 62774 |
| 54578 | 54586 | 62770 | 54579 | 62778 | 54587 |
| 50483 | 50995 | 54579 | 50487 | 55091 | 50999 |
| 50455 | 50583 | 50487 | 54551 | 50615 | 54679 |
| 54550 | 56598 | 54551 | 54558 | 56599 | 56606 |
| 21790 | 21822 | 54558 | 29982 | 54590 | 30014 |

The new owner in each row is the old owner in the next row, cyclically.
Hence this is a literal alternating C14, not merely an additive packet
signature. The seven roots and seven owner-cycle vertices are distinct. All
13 distinct colours in the table are necessary non-`D` colours; the search
replay's empty loss field implies that each of the six uncancelled old
colours had at least two input providers.

## 3. Promoted q1-zero package

The independently replayed output is

```text
model       q1zero.independent.model
model SHA   b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
audit SHA   ef9859055fd91d3179ee4e9f22b18124b4227d674f4d3fb2f4e141b60be13a8e
extended    f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90
manifest    af1867c516c069c417ba0a8e51bf98b0dbb3a5faed04f7063693c6b3bb61edff
```

The component/guard replay gives one component and 16,261 satisfied guards.
The exact pair extension reports 1,093,878 variables. The independent q1
cut output has SHA-256
`f9333055d70af89c45d08c7272eb779e92055cee9e09e135390faacf27c2d573`
and says

```text
PASS_K17_H1_EXACT_Q1_CUT
required=19412 covered=19412 missing=0 cut_literals=0
```

The empty emitted q1 cut file has the SHA-256 of an empty file. A read-only
`sha256sum -c q1zero.manifest.sha256` replay returned `OK` for all 18 listed
source, binary, model, audit, extension, q1-cut, and circuit-table artifacts.

## 4. Oracle interpretation

The finite move is accepted by the global loss-safe rows, not by a local
single-target score: every final promised multiplicity is at least one. The
one-debt and bounded C6/star-C8 failures were scoped plateaus; allowing two
temporary singleton debts exposed the C14. Intermediate debt is irrelevant
to the final simultaneous circuit toggle.

After q1 completion, select one actual factor provider for each of the
19,412 non-`D` colours. The unselected ordinary factor edges are a literal
residual completion with

```text
unused roots       4,896
target flow         9,792
closed-shore defect     0
```

This follows from the complement identity and does not require a new solver.
A residual max-flow/min-cut replay is now a fail-closed consistency check.
It is not evidence for the 36 excluded `D` targets or any later gate.

## 5. Resource and scope audit

R2 performed only read-only H100 inspection and manifest verification. No
remote directory, source, model, proof, or solver process was created. The
preflight observed the filesystem at 97% use with 34 GiB free; an unrelated
proof-producing CaDiCaL on CPU 55 was already active and was not touched.

The result closes only central necessary non-`D` rank-ten q1 coverage plus
the frozen guards and connected factor. It makes no residence, physical
all-width upper, ranks 11--17, source, compiler, opening, exterior-window,
regeneration, or word claim.
