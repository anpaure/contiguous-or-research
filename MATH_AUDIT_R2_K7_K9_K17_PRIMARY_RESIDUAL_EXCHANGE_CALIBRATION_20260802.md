# K7/K9 calibration and the K17 primary-residual exchange interface

**Date:** 2026-08-02  
**Status:** exact finite calibration at K7 and K9, plus a fail-closed K17 extraction specification. The K9 audit is a bounded exhaustive one-move/circuit census, not a broad search. No K17 feasibility, residence, source, compiler, opening, or word claim is made.

## 1. Theorems rebased

The current local closed-shore theorem is

```text
MATH_THEOREM_ODD_Q1_RESIDUAL_CLOSED_SHORE_ENDPOINT_CRITERION_20260802.md
SHA-256 efbc4bc95e03794e1a2eb2bf07b1caeb9ee4a368677ab3a6dd1f74abaccdb3ad
```

For a fixed primary selector, its residual maximum flow is deficient by

\[
 \max_Y\left(2I_A(Y)+J_A(Y)-\sum_{T\in Y}c_T\right)_+.
\]

The Markov boundary is

```text
scratch/MATH_THEOREM_ODD_Q1_INCIDENCE_MARKOV_CIRCUITS_AND_C6_OBSTRUCTION_20260802.md
SHA-256 76ac68ed45f0449a8537dc2d76f133638fbf41e622e3e6a80f3bcfa3fe8ee759
```

Root--owner fixed-margin circuits preserve every primary Benders row. A same-upper diamond replacement can change root support and owner endpoints. A dual owner--upper circuit preserves upper and owner degrees but transports primary roots. Its exact row delta is the old closed-shore root weight minus the new root weight. Chordless circuits, not C6 alone, generate the unrestricted root--owner fixed-margin fibre; completeness in the dual primary fibre separately requires every legal dual alternating circuit.

## 2. Authenticated K7 calibration

The deficient primary selector is frozen at

```text
/home/amodo/or15/work/root_k7_q1_owner_degree_audit_20260802
source SHA-256 df65e847a96d34ceac517fc72f9a15002e4494cb4b16d3cbc1bdc1f6f1c91825
output SHA-256 925b5fbd8bd33d37e1f2e797c44f2ebd7177419f3601357c68bbbb9ac7a80336
```

It has 21 primary edges, 14 residual roots, residual flow `25/28`, and a minimum closed shore

```text
I=4, J=10, c(Y)=15, deficiency=3
Benders lhs=22, rhs=19
```

The actuator package is

```text
/home/amodo/or15/work/root_k7_q1_benders_actuators_20260802
```

| census | exact result |
|---|---:|
| legal same-upper replacements | 73 |
| replacements improving the incumbent row | 49 |
| row gain one / two | 38 / 11 |
| resulting flow 24 / 25 / 26 | 6 / 23 / 20 |
| alternating dual C6 | 13 |
| root-injective forest dual C6 | 4 |
| incumbent-row-improving dual C6 | 2 |
| flow-improving dual C6 | 0 |

The literal same-upper move at upper mask `93`, root `84 -> 76`, changes owner edge `85--92` to `77--92`, gains two on the incumbent row, and raises the global flow only to `26/28`. The two improving dual C6 moves leave flow at `25/28`.

```text
same-upper source 619da84f0c156909dbde72652f1d3fd4e577b46f8cfd0d9899a246a68a35a2a0
same-upper output fd41b6f734ab48319518b5b3d067fdc229c3a7047fbd626b59d942a4b2bb0b56
dual-C6 source     5460703a8a420cd4fd506b4b7cb8f43e663a8063cf3ae1410a4477e98ab5fc2f
dual-C6 output     8a548fb439d0fae538c03ab007f665e54074b43008002f11c9cf8e581dd1070a
```

Thus improvement of one returned shore is not an exact proxy for improvement of the reoptimized residual flow.

## 3. Exact bounded K9 calibration

### 3.1 Input and factor development

The authoritative quotient certificate is

```text
scratch/k9_sigma_factor_calibration_20260729.certificate.json
SHA-256 a7e2127394009806a3e2564a6910c510cbb2d82df8fe1a01dc6aab566c0475bb
```

The independent audit already records 14 quotient choices, 126 middle owners, complete 84-element upper-q1 palette, four physical components of lengths `9,39,39,39`, and cyclic depth-two residence.

The new O3 C++ audit develops every quotient choice through all nine rotations and independently verifies:

```text
126 distinct rank-four roots
degree two at all 126 rank-five owners
84/84 rank-six upper colours
upper multiplicities 1^45 2^36 3^3
physical components 9,39,39,39
```

It then chooses a deterministic lexicographic one-provider-per-upper primary subforest, with a bounded cycle repair if needed. The frozen selector has 84 edges and 42 induced forest components. Its 42 unused roots have exact residual flow `84/84`; the factor complement itself is also a literal completion witness.

### 3.2 Worst single-move seed

All 1,176 same-upper proposals from the base selector were enumerated. Exactly 297 retain root injectivity, owner degree at most two, and a linear forest. Their reoptimized residual flows are

```text
82^10 83^96 84^191.
```

The deterministic worst seed is

```text
primary index 8, upper 175
old root 135, owners 143--167
new root 139, owners 143--171
```

It has flow `82/84`. Its returned minimum-cut owner shore has

```text
I=22, J=12, c(Y)=54, deficiency=2.
```

### 3.3 Exact move comparison on that seed

| move class | alternating/proposed | legal | incumbent-row improving | global-flow improving | improving-row but flow down / flat / up |
|---|---:|---:|---:|---:|---:|
| same-upper diamond | 1,176 | 296 | 184 | 14 | 23 / 147 / 14 |
| dual owner--upper C6 | 55 | 5 | 3 | 0 | 1 / 2 / 0 |
| dual owner--upper C8 | 102 | 14 | 4 | 0 | 4 / 0 / 0 |

In particular, the incumbent-row score can strictly improve while another shore becomes more deficient. Every candidate was subjected to a fresh exact max-flow and the returned max-flow deficiency was checked against the closed-shore formula.

### 3.4 Frozen package

```text
local  scratch/r2_k9_primary_residual_exchange_oracle_20260802
H100   /home/amodo/or15/work/r2_k9_primary_residual_exchange_oracle_20260802
```

Principal hashes:

```text
source                 1c21163bc6851145af88a65a125cda6d99ca0db4d8a0f342ac998069056c171e
H100 binary            b368e77b9243cd3c063019ad7902303f82c96f950b7907b4eb187378f6faa805
audit JSON             25f683c45bc4f738d2771a15d804ea18a2af28ea7956085324d3e53d883dffaa
move catalogue         97f589642a2b339f0ed4a9afaebc73b24f99e89d81ddbe20a0e46117fdba4803
base primary selector  69d44389a2f7574bbd6a9c4f12598dff8e4f693c8c18e46268a6e3df396ffc40
deficient seed         3475d940551ddd7805a11642cc3efc866b940d057c74d7b2b249136f7dc6f9f2
```

A second execution on idle core 20 is byte-identical for the JSON, 316-line catalogue, and both 85-line selector TSVs. The verifier checks the catalogue line/kind census and rejects duplicate `(kind,key)` rows. Resource use was 0.05 wall seconds and 3,584 KiB maximum RSS. Compile and run stderr are empty.

## 4. Exact frozen K17 71-row snapshot

The relevant theorem and stage are

```text
MATH_THEOREM_K17_H1_ORDINARY_EXCURSION_BENDERS_MASTER_20260802.md
living aggregate; the exact 71-hole inputs are frozen by the four hashes below

/home/amodo/or15/work/root_k17_h1_global_outer_20260802/
  exact_q1_stage/round4.root_chain50m.s2026080204.model
    SHA-256 24296cdf3b600c4018c109d8de9d352b05913e2cd08b5c7074675fdfc9c63df4
  exact_q1_stage/round4.map.tsv
    SHA-256 d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63
  exact_q1_anneal71_stage_20260802/seed.extended.model
    SHA-256 0debc7f6aabfb30b9f69e13da39e3ca355f29206d7dec3e5592cc5544f7c4f63
  exact_q1_anneal71_stage_20260802/seed.q1.cuts.cnfpart
    SHA-256 5c4b9a9a3cb6fe2a0d4a17b02475a6aa092456dc356db8ab1edab085a1825b0f
```

The historical 50M snapshot explicitly requested for this calibration gives

```text
required non-D rank-ten targets 19,412
covered                         19,341
missing                         71
missing-row literals            3,195
```

The connected factor model has 218,790 incidence variables. The complete map adds 875,088 ordinary pair variables, for 1,093,878 variables total. Its guarded C6 walk tested 50,000,000 proposals and promoted coverage `19,175 -> 19,341`; the frozen audit SHA is `4b064bec979fcf75da0a9d3e07ab21aefa21d5c4ad04b63bb8a28a6efa2d4a6c`.

The passive physical chronology has 93 rank-ten holes, then `1547,288,7` holes at ranks 11,12,13, and 5,574 short positive runs. Its audit SHA is `ae9d9d7771dd1f11bdaf905bc5af96d4104d178333c6ab2cc9d2f084c3dae6e3`. The 71 missing necessary non-D ordinary-provider rows and the 93 physical linear holes are different censuses and must not be conflated. Later descendants in the living h1 aggregate are outside this frozen calibration.

## 5. Fail-closed K17 selector extraction

For each ordinary rank-eight root `q` other than `M,D`, read its two selected incidence variables from the model and form the literal diamond

\[
 e_q=(q,\ T_q\cup H_q,\ T_q,\ H_q).
\]

This gives exactly 24,308 ordinary factor edges. Bucket them by their rank-ten union. A complete primary extraction is allowed only if every one of the 19,448 upper buckets is nonempty. Then introduce `s_(R,e)` and require

```text
one selected provider in every upper bucket R;
every primary root at most once;
primary owner degree at most two;
primary graph a linear forest;
all protected/boundary rows.
```

When providers are restricted to the incumbent ordinary factor, root injectivity and degree at most two are inherited, and the selector is a subgraph of the two ordinary paths. The unselected factor edges give a residual completion automatically. Consequently a zero-hole factor plus an internal one-provider extraction is a positive calibration, not a nontrivial residual-flow search.

The frozen 71-row snapshot does **not** admit this complete extraction: its 71 non-D buckets are empty. Therefore the total-capacity identity of the closed-shore theorem is not authorized on a fictitious 19,448-edge primary selector. Rank-ten hole closure must be the first lexicographic gate, or be modeled jointly with explicit unmet-upper variables.

After all buckets are nonempty and one complete selector is fixed, first fix
the selected `D`-neighbour boundary state, then use

```text
A = all rank-eight roots except M,D and the 19,448 primary roots;
|A| = 4,860;
b_T = 2 - 1[T=B] - fixed selected D-neighbour deficit occurrences at T;
c_T = b_T - primary_degree(T).
```

The residual network then has 4,860 root nodes, 24,310 owner nodes, 43,740 containment arcs, and target flow 9,720, plus source/root and owner/sink arcs. A failed exact flow returns an owner shore and the exact primary Benders row of the closed-shore theorem. If the `D` incidences remain variable instead, they must occur explicitly in owner capacities and every Benders row; a fixed `b_T` is then unsound.

## 6. K17 move catalogue and exact finite audit specification

The first finite K17 audit should be one O3 C++ CPU executable, not a SAT search:

1. authenticate the map/model/cut hashes above;
2. reconstruct all selected incidences, 24,308 ordinary diamonds, the two ordinary paths, and all upper-provider buckets;
3. report ordinary and exceptional-D provider multiplicities separately;
4. fail closed if asked for a complete primary selector while any bucket is empty;
5. after a zero-hole descendant is supplied, freeze a deterministic primary TSV and replay the residual flow/closed-shore equality;
6. enumerate same-upper alternatives. A rank-ten upper has 45 rank-eight roots, hence at most 44 alternatives to one selected diamond, before collision/degree/forest/protection guards;
7. enumerate incumbent-alternating dual owner--upper C6/C8 circuits, decode their new roots, and apply the same guards;
8. for every legal candidate, reoptimize the residual max flow. The incumbent-shore delta is recorded only as a lower-cost filter, never as the global verdict;
9. export the candidate delta, fresh flow, fresh minimum shore, and exact selector hashes.

Full enumeration has at most `19,448*44 = 855,712` raw same-upper proposals before guards. Warm-started integral-flow sensitivity can make this practical, but accepting a move still requires an exact terminal flow or a proved global sensitivity certificate.

The full-factor q1 hole repair uses a different circuit space: root--owner C6/C8 toggles change upper multiplicities, after which the primary provider must be reselected. Dual owner--upper circuits preserve an already complete primary upper palette and cannot manufacture one of the frozen snapshot's empty upper buckets by themselves.

## 7. Scope

The K7 and K9 results prove only that a single incumbent closed-shore gradient is not a globally improving oracle. They do not disprove submodularity of some other extended value function, and they do not prove that C6/C8 circuits suffice at K17. The K17 71-row object is a connected q1 scaffold with substantial residence and deeper-upper defects. No source, compiler, opening, residence, deeper-upper completion, word, or value of `nu(17)` follows.
