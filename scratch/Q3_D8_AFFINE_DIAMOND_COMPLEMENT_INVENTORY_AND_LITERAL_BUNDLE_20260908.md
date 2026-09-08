# Admissible complement-closed diamond bundles hit three C orbits each

2026-09-08. One bounded h100 structural inventory, no LP or integer
search, followed by a pure normalization check of the supplied
literal example. There are admissible C-covering bundles. Their
uniform three-C count obstructs one specific exact-critical ledger.

The classification now has a pure proof in
`Q3_D8_PURE_DIAMOND_CLASSIFICATION_AND_WITNESS_LEDGER_20260908.md`.
Ternary_lift independently audited its Sections 1--4: PASS. In
particular, the proof obtains exactly the same admissible U/V/W
families, counts 336/336/504, and witness capacities without using
this inventory as a premise.

## 1. Complete physical catalogue

Use the affine three-diamond pair family from
`Q3_D8_AFFINE_THREE_DIAMOND_AUDIT_AND_EXACT_GATE_20260908.md`, with
both shores cropped to ranks 1,...,7. The partner word swaps steps
(2,3), (4,5), and (6,7), each on distinct coordinate axes.

For a fixed linear shore H and v outside H, normalize the common
first axis to zero by a coordinate translation. Of the 630 full
words with that first axis, 408 satisfy the diamond conditions.
Exchanging the two chain words gives the same translation orbit,
so there are 204 physical translation-orbit representatives.
All these orbits have eight physical rows.

Global complement reversal, followed by translation of the last
axis to zero, is an involution on those representatives. It has
thirty fixed representatives and 87 two-element pairs. Developing
the seven H choices and four v choices gives

    5712 physical translation8 orbits,
    840 complement-closed size8 bundles,
    2436 generic complement-closed size16 bundles.    (1)

The normalization accounts only for actual coordinate translations
and exchanging the two shores, not for an extra linear-group
identification. These are counts of physical orbit families.

## 2. Critical repetition screen and result

Every individual translation8 orbit has six distinct rank-seven
target translation orbits. A size16 complement bundle must have
twelve distinct critical orbits to avoid intrinsic repetition.
The target orbits at ranks seven and nine all have size eight.

The complete catalogue gives:

| Bundle size | Generated | Admissible | Rejected |
| ---: | ---: | ---: | ---: |
| 8 physical rows | 840 | 840 | 0 |
| 16 physical rows | 2436 | 336 | 2100 |

The same pass/fail result was checked independently on rank nine.
The size8 bundles contain no class-C critical target. Before
screening, the size16 bundles split as follows:

| Distinct C target orbits | Number of size16 bundles |
| ---: | ---: |
| 0 | 1428 |
| 2 | 672 |
| 3 | 336 |

Exactly the 336 three-C bundles pass the repetition screen. Thus
every admissible generic bundle contains three C targets, and
every admissible size8 bundle contains zero.

The union of all admissible bundles covers all 127 rank-seven
target translation orbits, all 127 rank-nine orbits, and all 28 C
orbits. There is no individual critical eligibility obstruction.

## 3. A literal positive sixteen-row bundle

On H=0123 with v=4, take

    C=01023231,
    D=00132321.                                      (2)

Their cropped row is C^circ x (D^circ+4). Develop it by all eight
coordinate translations and add its global value complement. The
two translation orbits are different, giving sixteen physical
rows of total charge 224.

The six original rank-seven target orbits and the six complemented
rank-nine target orbits can be distinguished canonically without
computation. Translate each target by the xor of its odd set of
one-valued coordinates. Use these descriptors:

* D(L;T): L is the three-point line of ones and T is the two-set
  of twos, neither containing zero.
* B(L;t): L is the three-point complement of the five ones, and
  t is its two-valued point.
* C(L;t): L is the line of ones; the twos are zero and t.
* F(T): the unique one is zero and T is the nonline three-set of
  twos.

The complete canonical list is:

| Source shore ranks | Original rank-seven descriptor |
| --- | --- |
| (1,6) | D(356;47) |
| (2,5) | B(167;1) |
| (3,4) | D(246;37) |
| (4,3) | D(347;26) |
| (5,2) | C(123;4) |
| (6,1) | D(257;46) |

| Original shore ranks before value complement | Complemented rank-nine descriptor |
| --- | --- |
| (2,7) | D(145;67) |
| (3,6) | C(347;1) |
| (4,5) | B(347;4) |
| (5,4) | B(246;4) |
| (6,3) | C(246;1) |
| (7,2) | F(467) |

All twelve descriptors differ. The bundle's critical class
multiset is therefore

    3C + 5D + 3B + F.                               (3)

This independently verifies one useful C-covering bundle. It is
not a cover of the whole cube.

## 4. The diamond-only full8 plus twenty-short8 ledger is impossible

Consider the proposed charge-2384 bank consisting of one of the
individually complement-closed full eight-row extremal orbits and
twenty eight-row units of short affine diamond orbits, with the
entire short bank complement-closed. Its critical occurrence count
is 128 translation-orbit units against 127 demanded units.

The full orbit's endpoint target orbit already has multiplicity
two, and is distinct from all six interior orbits. This consumes
the only permitted excess. Every short complement bundle must
therefore pass the repetition screen, and every C target must be
covered exactly once.

The full orbit and every admissible self size8 bundle contain zero
C targets. Every admissible generic size16 bundle contains exactly
three. If g generic bundles were selected, exact C coverage would
require

    3g=28,

which is impossible. This conclusion concerns the diamond-only
complement-closed exact-critical ledger, not the mixed endpoint
family of the positive fractional LP. Additional copied rows,
different endpoint compositions, or an asymmetric bank are outside
this divisibility argument.

## 5. Files, checks, and runtime

One process ran only on h100, under a five-second outer cap,
two-CPU affinity, and a 1 GiB address-space limit. Runtime was
0.2541169277392328 seconds. No optimizer or new integer search ran.

Files:

* `q3_d8_affine_diamond_complement_structural_catalogue_20260908.py`;
* `Q3_D8_AFFINE_DIAMOND_COMPLEMENT_STRUCTURAL_SUMMARY_20260908.json`;
* `Q3_D8_AFFINE_DIAMOND_COMPLEMENT_STRUCTURAL_CATALOGUE_20260908.json`.

Every generated record stores its literal shore words, partition,
translation, eight- or sixteen-row size, critical orbit incidence
with multiplicities, all covered target translation orbits, C
count, and screen result. The certificate includes all 3276
complement bundles, including the rejected ones.
