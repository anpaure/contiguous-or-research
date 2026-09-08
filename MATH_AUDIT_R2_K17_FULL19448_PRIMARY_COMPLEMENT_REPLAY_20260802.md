# R2 audit: K17 full-19,448 primary selector and literal complement

**Date:** 2026-08-02  
**Status:** PASS for the deterministic ordinary primary selector and its
literal opened/cyclic complements in both licensed orientations. This is a
rank-ten residual-flow audit only.

## 1. Frozen package

H100 root:

~~~text
/home/amodo/or15/work/r2_k17_full19448_primary_complement_audit_20260802
~~~

Immutable physical-factor inputs from the independent semantic decoder:

| input | SHA-256 |
|---|---|
| orientation 0 | a5a6b2833a6eea217dd91d5768687a8cba09b5ede5284f4bb7d972fa2f5c363b |
| orientation 1 | f8ed5a1bd6e2cd0fa3ec8ec01889937d43453c81caf0bee87e8d3c88d0f09357 |

Independent verifier package:

| artifact | SHA-256 |
|---|---|
| source | 80b91e6fdf86adb981b0f830495d9575f92f26513d5f4cba985bf4c2d9fd626f |
| O3 binary | 4ab97a82e50673d3a715f5cd1e16c8b13b853fb3d2ecfd2a64abe6e584f5306c |
| audit JSON | 976c52ca38964477e933a9df9fdcee98f8e8369511133c2b1e535bcc4cc9f97e |
| empty stderr | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| exit file | 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa |
| manifest | 3b662eeed25f3fec2697cbf6a49b46ae5fb2784eb89e215bc947552d89b5b873 |

Every entry in MANIFEST.sha256 passes sha256sum -c. The verifier ran on one
H100 CPU and launched no search or SAT solver.

## 2. Literal checks

For each orientation the verifier independently:

1. parsed all 24,310 physical factor rows;
2. checked rank 9/9 endpoints, rank-eight intersections and rank-ten unions;
3. checked cyclic adjacency and all 24,310 rank-nine owners exactly once;
4. checked the edge-class census: 24,308 ordinary, one internal D seam and
   one physical D closing seam;
5. reconstructed the complete ordinary provider histogram;
6. selected the first ordinary occurrence of each rank-ten target;
7. contracted the resulting primary forest with an independent disjoint-set
   implementation;
8. checked that the complete complement is one quotient cycle and that
   deleting the physical closing seam leaves one quotient path.

## 3. Exact result

Both orientations give:

~~~text
ordinary occurrences                  24,308
ordinary distinct rank-ten targets    19,448
ordinary multiplicity range              1..5
singleton targets                     15,128
duplicated targets                     4,320
D-superset targets                        36
D-superset provider occurrences           37
D-superset multiplicity range             1..2

primary occurrences                   19,448
primary forest components              4,862
opened residual occurrences            4,861
opened residual quotient          one path
opened residual flow                    9,722
cyclic residual occurrences            4,862
cyclic residual quotient          one cycle
cyclic residual flow                    9,724
~~~

The independently decoded seam colours are:

| orientation | internal | closing |
|---:|---:|---:|
| 0 | 41215 | 66047 |
| 1 | 73983 | 33279 |

The same ordinary histogram appears in both orientations. Therefore neither
the internal nor closing seam is needed as a primary rank-ten provider.

## 4. Retained fail-closed correction

Verifier version 0 inherited the q1-zero checkpoint's second seam pair
98559/8703. It passed every geometry, palette and complement check, then
failed deliberately at the final semantic seam assertion:

~~~text
FAIL_R2_K17_FULL19448_PRIMARY_COMPLEMENT orientation1 seam colours
~~~

The failure package is retained under MANIFEST.v0.sha256, SHA-256
50f8142e9e15296ae5f55d649b032ff871ce27c7336e164fc5716bef421b4ffb.
The corrected verifier accepts only the final-topology pair 73983/33279.

## 5. Exact scope

This audit gives a literal full residual complement and hence a witness for
every closed-shore inequality at immediate rank ten. It does not certify
positive residence, ranks 11--17, source, compiler, exterior windows,
opening collateral beyond the encoded owner path, regeneration, a word, or
\(\nu(17)=24313\).
