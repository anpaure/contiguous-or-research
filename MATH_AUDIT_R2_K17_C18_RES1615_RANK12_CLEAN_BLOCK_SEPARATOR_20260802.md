# R2 audit: exact rank-12 clean-block separator for the promoted C18 carrier

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_c18_res1615_cleanblock_rows_20260802`

The independently replayed input factor has SHA-256 `5c8e864807c641109b6f430a21064c219417c912000a0d2c9a8cc6317e67c955`.  Its physical deep-hole and missing-orbit ledgers have SHA-256 `fe41c1fc0b2f18e5b9ade2247f722fabcc62b77808f5b47975a9bdb74fd44e4f` and `10a3b03466d2417b3be85b5ff5964d27d781386f098f474ee700c27521858b7c`.  The quotient option map has SHA-256 `7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3`.

For each missing rank-12 target `Z`, the producer reconstructs all 220 rank-9 owners contained in `Z`, the incumbent factor induced on them, every induced component, and an explicit coordinate of `Z` missing from that component's owner union.  It then takes every selected optional quotient orbit incident to a clean owner in every one of the 17 physical phases.  Retaining all these incidences saturates the clean owners under the exact degree-two master and preserves every persistent-hole component.  Therefore target coverage requires the sound primary no-good

```text
OR_{e in S_Z} (not x_e).
```

The producer and a separately written semantic replay agree exactly:

- 238 physical rank-12 holes forming 14 complete `Z_17` orbits;
- 14 distinct, nonempty negative-primary rows, width 217 through 307 and total width 3,920;
- all 17 phases and 220 clean owners per phase;
- 33,660 component rows carrying explicit persistent-hole coordinates;
- 52,360 literal incidence rows;
- equal support and clean-component size profile across all phases of each orbit.

Artifact hashes:

- rows `b1dbd3e5d7bd278fe6b5a2e3fcccb670b3a93bfad0ffcfc9a2e144393c638c09`;
- targets `7770bc2ab4c1ada763909084f0b4110d23ad0065eda5bad585a85ec372ab84b0`;
- components/persistent holes `dc0b1e2198cce9ce2a5f2f18df0ab1df3d86f2361df9cd49e1e47b11f98dfbfe`;
- incidences `73321ec6bb7f086e14bdcc8a85b6d784a5d814a22ca0d256dff3ceaceb1c1db6`;
- producer audit `8c9ce961656d57ca74e53cfd43b118fcc9016e4824398d9f0d8f3ffe0b78891f`;
- independent replay `9c31adebc4d8fb870ffcd2414c60f1b9e1af171ecf9e8a7e3b4e96ab718fbbfb`;
- frozen manifest `1719a538667c384bde990e6147054a499964391c2d13979d3b34aeae8824c4a5`.

This is a carrier-specific lazy-cut package.  The carrier still has 1,615 short positive runs.  No residence, SAT, source, compiler, opening, exterior-window, regeneration, or word claim is made; no solver was launched.
