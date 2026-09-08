# R2 audit: strict17 full-q1 calibration for the compound oracle

**Date:** 2026-08-02  
**Mode:** read-only remote hash and literal report inspection; no search or
solver was launched.

**Superseded calibration:** `strict17` is retained as the authenticated
predecessor/plateau state.  The current base is the residence-2018
bridge--quench endpoint recorded in
`MATH_AUDIT_R2_K17_FULLQ1_BRIDGE_QUENCH2018_CALIBRATION_20260802.md`.

## Authenticated files inspected

All paths are below

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
```

```text
5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa  fullq1_strict17.best.model
47deb8628c43290608f320c59debbd48c1a8920c381f78d79ec3faef4dc19ab6  fullq1_strict17.extended.model
07910032872f507b1f093b97d58a752ebd17ab6080154e15d26541d6b63f69e0  fullq1_strict17.audit.json
914be37333d831dd503344684a72a8f213a5062d1a3deef15377f2fac1f7d658  fullq1_strict17.passive.audit.json
14b0d6e09eb6b72ea0d4dbf741dc1815421910323d0df731c4a46131afd78f74  fullq1_strict18.audit.json
5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa  fullq1_strict18.best.model
```

## Replayed-report facts used by the theorem

`fullq1_strict17.passive.audit.json` reports one connected augmented
lollipop, opened rank-ten holes zero in both licensed orientations, and

```text
orientation 0: short histogram (1280,745), total 2025
orientation 1: short histogram (1281,744), total 2025
deeper holes ranks 11,12,13: (1521,279,4) in both orientations
```

Its auxiliary ordinary-component total is `2023`; this is not the literal
opened objective and is not used as such.

`fullq1_strict18.audit.json` reports

```text
guard_safe_catalogue=14119
lossless_residence_improving=0
initial_opened_q1_holes=[0,0]
final_opened_q1_holes=[0,0]
pair_candidates=0
pairs_tested=0
```

The local frozen source

```text
scratch/k17_h1_fullq1_res2169_compound_20260802/
  search_k17_fullq1_strict_batch_residence_20260802.cpp
```

constructs `pair_candidates` only from connected moves with a nonempty q1
gain set and at most two q1 losses.  Consequently the zero pair count at a
full-q1 incumbent is a prefilter outcome, not an exhaustive root-disjoint
pair certificate.

## Scope

This note authenticates the byte hashes and the contents of the cited frozen
reports and checks the pair-prefilter interpretation against the local source.
It does not independently regenerate the factor, re-run the complete model
checker, launch a solver, or certify a residence-improving compound packet.
