# K16 append-0200 phase collar `(4,7,3)`: exact-one-change certificate

Date: 2026-07-30

## Result

Let `W` be

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

It has length `12,874` and its sole missing nonzero 16-bit contiguous OR is
`0x287d`.  Freeze every cell except the fourteen zero-based positions

```text
[0,4) union [6437,6444) union [12871,12874).
```

Allow an editable cell to take any nonzero 16-bit mask, including its
incumbent value, but require **exactly one** of the fourteen values to differ
from its incumbent.  No assignment in this fibre is universal.

This is a proof-certified finite theorem.  It is not the full `(4,7,3)`
collar theorem: change counts `2` through `14` remain outside this particular
certificate while the unbounded run is pending.  It also says nothing about
edits outside the fourteen positions, insertions, deletions, relocation,
reordering, arbitrary length-`12,874` words, or unrestricted K16.

## Exact reduction

An interval avoiding every editable position is unchanged.  Such intervals
already cover `65,492` targets.  The remaining `43` targets must be witnessed
by an interval meeting the editable set.

For each consecutive block of editable positions, the frozen pieces between
them have one of `349` exact OR bases.  For a target `t` and base `b`, a
candidate interval is possible precisely when

1. `b` is a submask of `t`;
2. every editable value in the block is a submask of `t`; and
3. their union supplies every bit of `t \ b`.

Dominance reduction leaves `1,892` exact witness terms.  A selector for each
term implies these bit conditions, and each of the 43 targets has a clause
requiring at least one selector.  Sixteen Boolean variables encode each
editable mask, a nonzero clause forbids zero, and an exact change variable is
equivalent to disagreement with the incumbent.  The frozen exact prefix
counter imposes change count one.

The resulting DIMACS instance has:

```text
2,157 variables
52,639 clauses
128,894 literals
```

The independent encoding audit reconstructed the complete unbounded DIMACS
clause multiset, checked the affected-interval decomposition, and compared
term semantics with direct full-word OR replay.  A separate finite logic
audit checked the change equivalence and cardinality counter exhaustively on
small instances (`90,114` cardinality cases).

## Solver and proof replay

Kissat `4.0.4` ran on H100 CPU core 27 with `nice 19`, a 900-second timeout,
and an 8-GiB address-space cap.  It returned exit `20` in `0.13` seconds.
The retained binary DRAT proof has SHA-256

```text
cdc0e8497db9d7ccd359ebc56b4c61229fe25a4ad2b18ffbd69011506a3cbb02.
```

`drat-trim` independently checked that proof against the hash-frozen CNF,
returned exit zero, and emitted the literal `s VERIFIED` in `0.51` seconds.
Thus the DIMACS instance is UNSAT.  By the independently audited exact
reduction, the stated exact-one-change fibre contains no universal word.

## Frozen lineage

- Positions manifest:
  `scratch/k16_append0200_phase_collar_4_7_3.positions.txt`, SHA-256
  `f18ab34ea0f6be18c038ae4c52ba62ea931671925b2d7cd9a9513a9de5692118`.
- Emitter:
  `scratch/k16_dynamic_unbounded_substitution_cnf_20260730.cpp`, SHA-256
  `5d40fc37e1b1caea5992049887204a8224589b48f91ab7b5c6d7531efdc503a1`.
- Imported frozen core:
  `scratch/k16_12873_fixed_substitution_cnf_20260730.cpp`, SHA-256
  `c660cae1f5915f23a783fc371177cbe90f0206830d2fb83be92bd0c17a964cb8`.
- Independent unbounded-encoding audit:
  `scratch/k16_append0200_collar473_unbounded_cnf_thread473_20260730.audit.json`,
  SHA-256
  `8f34817be210ccb18d6f657eeb6ade419d9c158361bf0e713b60c6e3758521e6`.
- Exact-one-change CNF, map, and statistics SHA-256:
  `3966db372e621b7916124dac655e03de01261ef84e0b84683234756f24fbbc7d`,
  `28fd52773d49c3bd54abadd3753b28b788cdb0137c9dce39b781cd0c3c821d3e`,
  and `973c65e05214127722db67696d4b6c99a78f4a23515b381a1788a22479fbc1fe`.
- Proof-check transcript:
  `scratch/k16_append0200_collar473_exact_b01_20260730/dratcheck.stdout`,
  SHA-256
  `50978de992ea05a41deafa5d605f79a6a59889a207e40d87d1dd961d09fc8653`.
- Fail-closed replay driver:
  `scratch/audit_k16_append0200_collar473_exact_b01_proof_20260730.py`,
  SHA-256
  `ccfd8e00a45c9b9b206b959bca721baa14016c90fd2c4aaff738f11d5db97b64`.
- Compact audit:
  `scratch/k16_append0200_collar473_exact_b01_20260730.audit.json`, SHA-256
  `f3fe64f87dd447bfb37d789389d8f54c175af3aab82f2ba42cfc706eaa983ea2`,
  payload
  `b1afc45f1833737ba34383069374648522a3f5371eb3a07ec85b435f94ecacc3`.

The heavy artifacts are also retained at
`/home/amodo/or15/work/root_k16_ripple_near_sat_20260730_38f933/append0200_collar473_exact_b01_root`
on H100.
