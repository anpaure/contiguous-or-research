# K16 carrier-3 Hall-22 checkpoint (2026-07-30)

Carrier 3 is the strongest authenticated optimal-length K16 carrier currently
known.  It is not yet a full word, but it reduces the exact lower-compiler Hall
deficiency from 92 to 22.

## Independent support audit

- target chronology length: 12,873;
- all (\binom{16}{8}=12{,}870) rank-8 targets occur;
- flat positions (zero-based): 5769, 12869, 12871;
- maximal-envelope replay: exact, with no zero envelopes;
- physical short cells: 31,512;
- all 26,333 strict upper targets occur.

Target SHA-256:
`6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0`.

## Independent Hall audits

Both the Python Hopcroft-Karp audit and an independently implemented native
C++ replay agree:

- lower targets: 26,332;
- cells: 31,512;
- incidences: 350,892;
- maximum matching: 26,310;
- deficiency: **22**;
- canonical alternating witness: (519-497=22).

The exact 22 unmatched rank-7 masks and all 519 witness targets are included
in the checkpoint package.

## Provenance and scope

The chronology arose from move kind 3, pattern 4, cuts
`5725,6388,12826`.  This large nonlocal move also relocates the first flat to
5769; it is exactly the kind of structure missed by the fixed-flat local
catalogues.

This is an authenticated repair checkpoint, not yet a proof of
(\nu(16)=12873).  A descendant must reach Hall deficiency zero, then pass
COMP3 and an exhaustive literal replay of all 65,535 nonempty masks.

Files are under `scratch/k16_carrier3_hall22_checkpoint_20260730/`.
