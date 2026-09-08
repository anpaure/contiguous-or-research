# `k=17` paired_escape003: complete mixed star/octahedral-`C8` pair census

Date: 2026-08-02  
Status: exact finite no-go for one physical star `C8` plus one physical
octahedral `C8`, including compatible overlapping supports, on the frozen
`paired_escape003` carrier.

## 1. Source carrier

The independently replayed source is

```text
scratch/h3_k17_paired_escape003_independent_20260802/
  paired_escape003.factor.tsv
```

It has one physical component, every rank-eight facet exactly once, every
rank-nine owner at degree two, every rank-ten cap, and all `3,944` protected
facets.  Its positive short-run vector is

```text
(length 1,length 2,length 3) = (0,2261,1870),
```

for total `4131`, and its rank-11--13 cyclic upper-hole vector is

```text
(1887,442,34).
```

## 2. Complete mixed construction

The star family uses a rank-seven core and the octahedral family a rank-six
core.  Every active directed phase is generated modulo cyclic rooting.
After rejecting any support containing a protected facet, the carrier has

```text
37,213 star phases,
36,329 octahedral phases.
```

Of these, respectively `10,370` and `11,135` would individually add an
incidence already selected at one of their facets.  Such a phase cannot
participate in a disjoint pair, but it is retained for the overlapping join:
the other phase may remove that incidence.

### Disjoint supports

For individually simple disjoint phases, every cap-complete pair is found by
the necessary cap-debt index.  A debt-free star tests every octahedron.  A
star with debt is joined through its rarest zero-load cap to every
octahedron that adds that cap, after which the full two-circuit cap delta is
checked.  This gives

```text
4,775,258 indexed disjoint candidates,
50,847 cap-compatible disjoint pairs.
```

### Overlapping supports

Every star is joined with every octahedron sharing at least one physical
facet.  This complete shared-facet join has `1,031,645` distinct pairs.

The two incidence updates are composed simultaneously, not sequentially:
at each shared facet, first take the union of the requested removals, then
the union of the requested additions.  The resulting two-element incidence
set is required to exist literally, and the global rank-nine owner-degree
delta is required to be zero.  Thus individually duplicate phases are
accepted exactly when their collision is repaired by the partner.  There are

```text
281,571 degree-compatible overlapping pairs.
```

## 3. Exact final gates

Across the disjoint and overlapping joins:

| final gate | count |
|---|---:|
| preserve every rank-ten cap | 50,983 |
| also leave one physical component | 16,320 |
| residence-improving | 0 |

Of the `16,320` connected rows, `51` have a genuinely shared facet and
`16,269` are disjoint.  Every retained row is rebuilt as a literal incidence
factor and its complete physical owner cycle is traversed.

No retained pair decreases total positive short-run count or residence
deficit.  The best residence level is only a tie in run count: exactly `102`
pairs have `delta short-count = 0`, and all `102` have
`delta residence-deficit = +3`.  Hence there is no neutral-or-better
residence witness even after allowing a full mixed two-circuit trade.

## 4. Independent replay

A separate verifier reconstructs each star and octahedron from its literal
core/petal key, composes shared-facet updates by incidence-set algebra,
checks the rank-nine degree delta and complete cap multiplicity delta, and
rebuilds the full owner cycle.  It replays all `16,320` rows and all `51`
overlapping-support rows exactly.

## 5. Scope

This closes the complete one-star-plus-one-octahedron physical `C8` face on
the authenticated `paired_escape003` factor, including:

* all facet-disjoint pairs capable of repairing one another's cap debt;
* every pair sharing one or more physical facets;
* overlapping pairs whose individual duplicate incidence is repaired by the
  partner;
* exact protection, facet, owner-degree, cap, connectivity, and positive
  residence replay.

It excludes three circuits, longer alternating circuits, temporary
multi-step paths outside this final face, source positions, lower compiler,
and any global impossibility claim.  Since no residence-improving pair
exists, no rank-11--13 deck was promoted as a joint residence witness.

## 6. Frozen artifacts

```text
bd3993d6b4a49a87bc880352d397cbf498d0d42494a33d68aa05ba611fa9d511  scratch/search_k17_physical_mixed_star_oct_c8_pairs_20260802.cpp
336d31b58b582223e82f0f78ac86bab0cebabfa562f89278fa596b645563988e  scratch/verify_k17_physical_mixed_star_oct_c8_pairs_20260802.cpp
2cb2e653818bb4c98cd5335a388445d8b086ce97a1fe1b43e3c58bebfc00d486  scratch/h3_k17_paired_escape003_independent_20260802/paired_escape003.factor.tsv
978262c90f7557d524b816243bd771c3eda124e26053a9c9605ba00fe4ca736d  scratch/k17_paired_escape003_physical_mixed_c8_pairs_20260802/pc8_mixed_escape003.audit.json
9347991c9533f8f34b375992f648db1d3a7262f1fd792675af0b02b7887931ed  scratch/k17_paired_escape003_physical_mixed_c8_pairs_20260802/pc8_mixed_escape003.connected.tsv
4b54bc7423dbc166375eea68cb5755ac1d9dde68533927703063f0c30c324339  scratch/k17_paired_escape003_physical_mixed_c8_pairs_20260802/pc8_mixed_escape003.delta123.tsv
39819dde493910b0b9a292625e4a8fcaec3965c07ad3602c88a94c7555bf1709  scratch/k17_paired_escape003_physical_mixed_c8_pairs_20260802/pc8_mixed_escape003.independent.audit.json
```

Remote O3 CPU roots:

```text
/home/amodo/or15/work/pc8_mixed_escape003_20260802
/home/amodo/or15/work/pc8_mixed_escape003_verify_20260802
```

