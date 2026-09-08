# Audit of the filtered seam-catalogue phase argument

## Finding

The target-filtered invocation of the working producer

```
scratch/catalogue_k16_state2_directed_seam_hosts_expanded_20260730.cpp
```

has seven process arguments:

```
seamcat targets out.tsv depth dl dr target
```

The pre-patch parser accepted `argc==7`, and read `argv[6]` as the target,
but selected fixed `depth,dl,dr` only under `argc==6`.  Thus an `argc==7`
invocation silently used depths `{2,3}` and all four direction pairs.
Wrappers which invoked that form once for each of `pp,pm,mp,mm` therefore
repeated the same full eight-phase filtered scan four times.  Their filenames
did not certify their advertised phase.

## Repair

The phase-selection guard is now

```cpp
const bool fixed_phase = argc == 6 || argc == 7;
```

and all three phase vectors use `fixed_phase`.  The target remains
`argv[6]` exactly when `argc==7`.

Patched source SHA-256:

```
f5d0991c4ad77c2838419e5c0d92f4411c0b7629dbfc7958733358f44ed347e3
```

To prevent later target-list extensions from changing this lineage, the
exact patched source audited below is frozen as

```
scratch/catalogue_k16_state2_directed_seam_hosts_expanded_argc7_fixed_frozen_20260730.cpp
```

## Regression audit

The light regression

```
scratch/audit_a_k16_seamcat_argc7_phase_parser_20260730.py
```

compiled the patched source and ran all eight requests

\[
 d\in\{2,3\},\qquad (d_l,d_r)\in\{-1,+1\}^2
\]

on frozen carrier `C1` with target filter `0x1879`.  Every emitted row had
exactly the requested triple `(d,dl,dr)`, and the producer's only nonzero
summary slot was the requested direction pair.  The eight emitted-row counts
were

\[
 73,54,40,73,21,6,4,21
\]

in lexicographic `(d,dl,dr)` order.  This is a parser regression, not a
construction census.

## Effect on the surplus-transfer theorem

The frozen C1 forward three-cut audit is unaffected.  It imports the
pre-existing *full* atlas

```
scratch/k16_state2_directed_seam_expanded_20260730/all.tsv
SHA 3d7c7e7ab7a211735690ad438162cf5114441b4c71a2a53437048e4cce138d7c
```

then explicitly selects `dl=dr=+1` and each recorded depth in Python, maps
the endpoints into `C1`, and independently reruns the constant-depth seam
and host-family tests.  Its `61` depth-two and `18` depth-three arcs therefore
do not depend on the broken `argc==7` path.

Conversely, `scratch/k16_c1_directed_stage2_roots_20260730.tsv` and any
other phase-labelled file produced by the pre-patch seven-argument wrapper
are quarantined.  No theorem or count in the surplus-transfer report uses
that file.  Such files must be regenerated before any phase-specific claim
is made from them.

## Artifacts

At freeze time the regression artifacts are:

```
scratch/audit_a_k16_seamcat_argc7_phase_parser_20260730.py
scratch/a_k16_seamcat_argc7_phase_parser_20260730.audit.json
```

Their SHA-256 values are respectively

```
d5b11ae61201d4d5eac1961e280846e9c1446527cfb7641ba55a8a068717fe9d
a2b22adbf440d5e15f9563cc957d5dc1ccd13d7e981eaaca75ef0490c00a170f
```

The JSON has status `PASS_ARGC7_RESPECTS_REQUESTED_PHASE` and payload SHA-256

```
3756902c92fa8d3e33c0191e3cb0a6258a1dfaefa7486fa5ecb144e8ed99e90d
```

No old phase-labelled construction count is preserved merely from its
filename.
