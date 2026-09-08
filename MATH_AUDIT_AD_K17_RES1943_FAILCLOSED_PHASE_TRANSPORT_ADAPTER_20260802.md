# Audit: K17 res1943 fail-closed owner-phase transport adapter

**Date:** 2026-08-02  
**Status:** both guard branches exercised; static round047 transport succeeds,
but exhaustive source projection fails in both transported phases.

## 1. Early refusal is literal fail-closed

Before opening the universal incidence map or carrier assignment, the adapter
strictly parses the target table and requires

\[
  \texttt{matching}=\texttt{hard\_heads},\qquad
  \texttt{deficiency}=0,\qquad
  \texttt{zero\_hard\_heads}=0
\]

together with the positive projection status.  The G21 calibration has
matching `16841/16898`, deficiency 57, and 45 zero heads.  With deliberately
nonexistent carrier paths it returns `REFUSED_PROJECTION_NOT_CLOSED`, records
`carrier_files_opened=false`, and creates neither phase tables nor an incidence
diff.  This independently checks guard ordering.

## 2. Authenticated positive input and carrier

The later round047 table has hashes

```text
target table       95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
projection audit   2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a
Hall file          88088c986ade02910cff46fb5bf9b1bdfef76a34331a3e99983f9d92ed9aae87
```

and independently replays with matching `16898/16898`, deficiency zero, and
zero isolated hard heads.  The res1943 model SHA is
`4570796ee9a5d084deb3f1e7522a35836c877b0c94797dd85636f61c9a251c2c`
and the universal map SHA is
`80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a`.

The adapter reconstructs 48,620 selected edges on 48,620 vertices, one
component, and cycle rank one.  The root degree histogram is `(1,24308,1)`,
all 24,310 owners have degree two, and peeling leaves an even cycle with 3,182
vertices, or 1,591 roots.  Hence exactly two perfect owner phases exist and
22,719 off-cycle phase edges are forced.

## 3. Static transport passes independently

The adapter changes 13,472 owners in phase zero and 13,692 in phase one; the
phases differ on 1,591 roots.  Chain IDs, roots, lengths, targets, target
partition, and target/root FNV remain fixed.  A separately compiled static
verifier accepts each table with:

```text
rows / selected owner matching  24310 / 24310
all rank <= 8 targets           65535, exactly once
length histogram (1,2,3)        (0,7395,16915)
minimum long lower bound         16915, attained
```

## 4. Complete post-transport projection fails

A separately compiled exhaustive verifier enumerates every long menu and all
nine strict two-transition interval menus, with short roles acting as address
reset sockets.  It verifies long monotonicity and computes exact maximum
matchings and Hall shores:

```text
phase 0: matching 16836/16898, deficiency 62, zero 48,
         Hall heads/neighbors 82/20, graph FNV64 8957edf54ad1cdf5
phase 1: matching 16832/16898, deficiency 66, zero 51,
         Hall heads/neighbors 89/23, graph FNV64 59863cd695edca59
```

Thus static payload transport is valid, but projection perfection is not
carrier-phase invariant.  The smallest missing coupling is the owner-dependent
supplier incidence between the payload table and selected carrier phase.

## 5. Fail-closed boundary

Both transported projections are negative.  Consequently no same-role state
balance, occurrence-labelled source chronology, residence, deeper upper, DM,
common cap, compiler, or word is in scope.

Frozen bundle:

```text
scratch/ad_k17_res1943_failclosed_phase_adapter_20260802/
```
