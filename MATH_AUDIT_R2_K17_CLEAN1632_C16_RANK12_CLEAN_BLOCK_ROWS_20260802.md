# R2 audit: clean1632+C16 rank-12 clean-block rows

Date: 2026-08-02  
Status: exact carrier-specific separator package, independently replayed.  No
SAT solver was launched by this audit.

## Result

For the independently authenticated clean1632+C16 quotient factor, the 306
missing physical rank-12 targets are exactly 18 free `Z_17` target orbits.
For every orbit, all 17 physical target phases were developed.  Each phase
has exactly `C(12,9)=220` clean rank-nine owners.  Their induced factor
components, a persistent missing coordinate for every component, and both
literal factor incidences at every clean owner were exported.

For a target representative `Z`, let `S_Z(F)` be the set of incumbent-selected
optional quotient edge-orbit variables having a developed edge incident with
a `Z`-clean physical owner.  The frozen row is

```text
OR_{e in S_Z(F)} -x_e
```

in DIMACS notation.  The 18 rows are pairwise distinct and nonempty.  Their
width range is 217--320 and their total literal count is 5,142.  The complete
censuses are:

```text
physical factor edges                 24310
selected optional quotient orbits      1198
rank-12 missing physical targets         306
rank-12 missing target orbits              18
literal phases checked per orbit           17
clean owners checked per phase             220
component certificate rows               43503
incidence certificate rows               67320
negative-primary separator rows              18
empty supports                                0
```

The representatives, component counts per phase, and row widths are:

| representative | components | width |
|---:|---:|---:|
| 14319 | 146 | 309 |
| 15357 | 130 | 288 |
| 23547 | 138 | 274 |
| 24415 | 152 | 274 |
| 24431 | 149 | 272 |
| 24565 | 127 | 277 |
| 27615 | 145 | 308 |
| 28351 | 123 | 267 |
| 28407 | 146 | 276 |
| 28527 | 148 | 283 |
| 28599 | 151 | 299 |
| 28637 | 140 | 288 |
| 30199 | 143 | 320 |
| 31483 | 147 | 303 |
| 43775 | 125 | 217 |
| 44511 | 149 | 303 |
| 44795 | 149 | 302 |
| 46971 | 151 | 282 |

## Soundness

For every missing physical target `Z`, the factor induced on clean owners
`u subseteq Z` is a disjoint union of clean blocks.  The literal replay proves
that every exported block has a persistent coordinate in `Z` absent from all
owners of the block.  Therefore no clean block has union `Z`.

If a later degree-two factor retains all optional orbits in `S_Z(F)`, both
incumbent incidences at every clean owner remain: each is fixed or belongs to
`S_Z(F)`.  Degree two excludes any replacement incidence.  Consequently all
clean blocks and their persistent holes remain unchanged, so `Z` is still
missing.  Hence the displayed all-negative row is sound and is violated by
the incumbent.  This is the exact saturation separator; it is not claimed to
be a minimum-cardinality logical separator.

Representative-only cleanliness was not used.  The producer reconstructed
all 17 phases and required phasewise equality of optional supports and clean
component-size profiles before quotienting the row.  The independent checker
also reconstructed the 306 physical holes and proved that their canonical
representatives equal the 18 entries in the promoted `missing.tsv` ledger.

## Authenticated inputs

```text
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  marker58_residence_round1.map.tsv
a5986aaed96c5b39b6385628d8c602de3e91ce67acfe44942c76bc11528d92fb
  qa.../c16/factor.tsv
64a4689ab3f4da120f754f142706b7e260bf08b2b481a74d492f6117a9a794a0
  qa.../c16/holes.tsv
59a872b5362a9cd1b9dd586d136c234676943fe514b77ffbfedfab46146cadf6
  qa.../c16/missing.tsv
f57fa510175182b83c6e3154608c58b43962e70d91b4b62a618f5ed8eeed41ec
  qa.../c16/upper_orbits.json
be6cd5b5a1eb2778241882a32deb8565cf7adf38670cafc2ec79f9b1cb97a10a
  qa.../c16/owner_cycle.tsv
```

## Frozen package

Remote root:

```text
/home/amodo/or15/work/r2_k17_clean1632_cleanblock_rows_20260802
```

Workspace mirror:

```text
scratch/r2_k17_clean1632_cleanblock_rows_20260802
```

Principal hashes:

```text
c3f3495851ba39cea5675188ecb381301609af715775d9316c7200dab7bba551
  r2_k17_clean1632_rank12_clean_block_separator_20260802.cpp
995eee7f3c4a4ce300930067b7f46022c948802a89820a8e39a0c428efc0bc95
  audit_r2_k17_clean1632_rank12_clean_block_independent_20260802.cpp
51de7ca303483a225570f8c3ba3a28836a686a96a8cd4c0e6f6d66ef25473ce0
  clean1632_c16.clean12.rows.cnf
99230a208ed48ba8ba5033873a7223ec6a8d0f5160ec0f4fd6f11aa315d910b3
  clean1632_c16.clean12.targets.tsv
3b9e3429dbaf8a5d228ce0cbec06bb8703b87a34c670b1d8b5d642af7aa7f237
  clean1632_c16.clean12.components.tsv
385cf768cbe28406f4eebc76ce07206f90bfc3f67aea23b46dea2637dcfaf231
  clean1632_c16.clean12.incidences.tsv
7aa9bc8625359e853af7291fe39f2f4bc7d1693fbf830f3034fbfc0b9c1d7686
  clean1632_c16.clean12.audit.json
dff79094ca4222a8974a2e57447d4c534a45987e4cd17ef5bf2e711e9e1a1c68
  clean1632_c16.clean12.independent.audit.txt
a5fc4e5a835c69f2244eb7ff590b0229e01a3a4fb3262c83eb624f739bedd9bf
  R2_CLEAN1632_C16_CLEANBLOCK_FROZEN_SHA256SUMS
```

Both runs used `g++ -std=c++20 -O3 -DNDEBUG` on H100 CPU.  Producer peak RSS
was 15,872 KiB; independent replay peak RSS was 22,016 KiB.

## Scope

This is a carrier-only rank-12 lazy-cut package.  The carrier has 96 positive
residence-defect orbits and 98 missing rank-11 orbits; it is not a resident
SAT incumbent.  The audit makes no source, compiler, opening, exterior-window,
regeneration, word, or `nu(17)` claim.  Ranks 13--17 are clean only for this
calibration carrier and must still be checked on every future decoded model.
