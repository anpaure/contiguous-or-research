# R2 clean-block upper integration for the `k=17` compact-Horn-v3 + rank-11 master

Date: 2026-08-02  
Status: exact fail-closed integration theorem, independently replayed
carrier-1819 rank-12 calibration, and independently replayed unsolved sibling
CNF. No solver was launched.

## 1. Rebased interface

The static combined parent remains

```text
p cnf 366131 2037474
CNF SHA256 8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8
map SHA256 73a8f94f2a0249c29ba599bd832a3d173d5e00ed773b3e610761e610600ca5dd
```

The combined map reuses, byte for byte, the 71,874 directed-arc rows from the
V2 history map.  Their projection SHA256 is
`76c9ddc87df06f48dcd93c516ae3f4e9c98a98938128f516e4cde1f1feff8e55`.
R2 does not allocate a second dart or voltage frame: the post-SAT decoder uses
that shared map to reconstruct the selected orientation, quotient voltage and
physical development.  The clean-block clause itself is orientation-free and
uses only optional primaries `1..35713`.

It contains the compact Horn-v3 residence module, the frozen union-562
residence bank, and the exact eager rank-11 `S/Q` module. The authoritative
next residence suffix is not the provisional union-604 cited by the general
clean-block note. This task uses the independently authenticated canonical
596-row bank

```text
/home/amodo/or15/work/qa_k17_clean_floor1700_independent_20260802_quotientaudit/
cumulative.blocks.cnf
SHA256 d96d7ad6e39d3208b300221a280496090816c4f2654e931606ebdcb4a7434e50
```

It consists of 596 distinct pure-negative rows with arity histogram
`1:51, 2:24, 3:274, 4:247`; it contains the static union-562 exactly and adds
34 rows. It also contains the older union-421 plus 175 rows.

Rank 11 remains eager and verify-only. A post-SAT rank-11 miss contradicts an
already replayed 55-`Q` hard row and is a fatal decoder inconsistency; R2 emits
no rank-11 lazy clause.  The 728 eager coverage rows have one-based parent
clause ordinals `2036747..2037474`.

R2 does not duplicate P2's compact-rank12 derivation. Its upper contribution
is a post-SAT semantic separator in the existing optional-primary variables.

## 2. All-phase clean-block separator

Fix a physical rank-12 target `Z`. A rank-nine owner `u` is `Z`-clean when
`u subset Z`. Delete all dirty owners from an incumbent degree-two factor
`F`; the remaining components are maximal clean blocks. The target is covered
if and only if one block has union `Z`.

When `Z` is missing, each block `B` therefore has a persistent hole

\[
       h_B in Z - \bigcup_{u in B}u.                    \tag{2.1}
\]

Let

\[
 S_Z(F)=\{p:\ p\hbox{ is a selected optional quotient edge orbit and some
 developed edge of }p\hbox{ is incident with a }Z\hbox{-clean owner}\}. \tag{2.2}
\]

The learned row is

\[
                 \bigvee_{p in S_Z(F)} \neg p.          \tag{2.3}
\]

It is serialized by sorting positive primary IDs increasingly and then
negating them:

```text
-p1 -p2 ... -pt 0
```

### Theorem 2.1 (soundness)

Every factor retaining all primaries in `S_Z(F)` still misses `Z`, and the
incumbent falsifies (2.3).

#### Proof

At every clean owner, each incumbent incident edge is either fixed or belongs
to `S_Z(F)`. Retaining all of `S_Z(F)` therefore retains both incidences.
Degree two forbids any replacement incidence, so every clean-clean edge and
every clean-dirty boundary edge is unchanged. Hence every maximal clean block
and its persistent hole (2.1) survives. No clean block can have union `Z`.
All variables in (2.3) are selected by the incumbent, so all negative literals
are false there. `square`

For rank 12 there are exactly `binom(12,9)=220` clean physical owners, giving
the structural bound `|S_Z(F)|<=440`. An empty support is a scoped catalogue
obstruction and must be handled as an empty-clause verdict, not silently
discarded.

The same proof applies without change to every target rank `10..16`, with
width at most `min(1198,2 binom(s,9))`.  Rank 10 is already hard in the carrier
base and rank 11 is already hard in the eager `S/Q` module.  R2 uses the rank-12
instance here and leaves P2's compact rank-12 derivation untouched.  A future
post-SAT decoder may use the same clean-block routine for ranks 13--16; rank 17
is automatic only after the one-physical-chronology gate.  No monotone
lower-rank-to-higher-rank implication is assumed.

The authenticated floor-1751 rank-13 calibration has one missing orbit and a
749-primary clean-block row.  It confirms the generic interface but no literal
floor-1751 row artifact is imported into this child; the 62-row suffix below is
exactly 34 residence rows plus the 28 carrier1819 rank-12 rows.

## 3. The phase condition is mandatory

For a quotient owner representative `u`, occurrence `(u,g)` is clean exactly
when

\[
                         rho^g u subset Z.               \tag{3.1}
\]

Cleanliness cannot be tested on `u` alone. The R2 producer and independent
checker both inspect the literal 24,310-edge physical development and all 17
rotations of every canonical missing target. For each orbit they require:

1. all 17 physical targets occur in the literal missing-target ledger;
2. each phase has exactly 220 clean owners;
3. every clean owner has its exact two physical incumbent incidences;
4. every maximal clean component has an explicit persistent hole;
5. the selected optional-primary support is identical in all 17 phases; and
6. the sorted component-size profile is identical in all 17 phases.

Only after these checks is one canonical row retained for the free target
orbit. No representative-only quotient test is used. Canonicalization is only
output deduplication after literal phase equality.

## 4. Fail-closed post-SAT transaction

For a live combined-master incumbent, the decoder/separator transaction is:

1. authenticate the combined CNF/map, canonical-596 bank, complete SAT model,
   factor export and every earlier semantic row;
2. replay the assignment against the exact candidate formula;
3. verify marker resources, degree two, protected edges, exact rank-8 facets,
   all rank-10 caps, compact-Horn residence, quotient topology, nonzero voltage
   and the physical development;
4. replay eager rank 11; a miss is fatal and emits no row;
5. obtain rank-12 misses from the shared literal decoder (and, when present,
   cross-check P2's exact compact module) and independently confirm each by the
   all-phase clean-block scan;
6. export every clean component, one persistent hole, and both incidences of
   every clean owner;
7. form (2.3), requiring a nonempty support unless returning an explicit scoped
   empty-support obstruction;
8. normalize each logical identity by sorting signed literals numerically,
   deduplicate against both the batch and the complete parent, and perform no
   subsumption or dart projection;
9. append only novel rows, retain the existing 366,131 variables, and replay
   exact parent clause-vector prefix plus exact canonical tail before allowing
   the next solve.

If P2's exact rank-12 module is already a hard part of a later parent, a
rank-12 miss after full model replay is fatal and no R2 row is emitted.  For
the present v3+rank11 parent, missing rank-12 targets are separable.

The combined parent was copied to a fresh sibling.  Its 562 embedded residence
rows are an exact subset of canonical596, so only 34 residence rows are novel.
Those 34 and the 28 calibrated clean-block rows were normalized, globally
sorted lexicographically as signed vectors, and deduplicated into one 62-row
tail.  The exact child is

```text
p cnf 366131 2037536
/home/amodo/or15/work/r2_k17_v3_rank11_cleanblock596_child_20260802/
  marker58_compact_horn_v3_rank11_bank596_clean12.cnf
SHA256 c8511f6e166c1d44369f22cd55aeb1497232975e7c16732f2545f53a77cc051a
```

The child preserves the parent body as an exact byte prefix and exact
2,037,474-clause vector prefix.  Its tail SHA256 is
`fd338a4582e894015c7d65370e3409d713f3ffe467fed9e3fc159f773aa49521`.
An independent implementation replayed the complete child through exact EOF,
verified `596 intersect parent = 562`, recovered the 34-row set difference,
matched the 28 proof rows after signed normalization, and checked that the
62-row byte suffix is globally sorted and duplicate-free.  This is a frozen
**unsolved** child: neither SAT nor UNSAT follows from its construction.

## 5. Exact carrier-1819 clean-block calibration

Inputs:

```text
round000.model
  SHA256 11c0f52825193ca809cabbcba7bbc2b7a3c508e3af1346b7f66f793dbc5b512b
final1819.factor.tsv
  SHA256 03df8fee975817414402399284d20ad7c52058ea8b5c6b8f9bf5f653ef1768b1
final1819.owner_cycle.tsv
  SHA256 eb54fd57b8f1533598df54d42aab115b08f93ddfaa40fdf11afdf87d65a09b34
final1819.deep_upper.audit.json
  SHA256 eb80010fef9a0acaed81fa9e6f1101a2f879932a449dbd69e79587a4dbd3c512
```

The carrier has 1,819 short positive runs (`0,969,850` at lengths `1,2,3`) and
is not a v3 SAT incumbent. Its cyclic upper holes are 1,717 rank-11 targets and
476 rank-12 targets, i.e. 101 and 28 free target orbits. Ranks 13--17 are
complete for this carrier.

The all-phase rank-12 result is:

```text
physical targets audited                 476
canonical target orbits                   28
physical phases per orbit                 17
clean owners per target                   220
component certificate rows            67,473
component count range per target       121..151
clean-owner incidence rows            104,720
distinct negative-primary rows             28
empty supports                              0
support width range                    217..308
support literal sum                       7,983
representative-only logic used             false
```

All 17 phase supports and component-size profiles agree within every orbit.
No two canonical missing targets share a full support vector.

## 6. Comparison with the supplementary dart frontiers

The previous R2 target-automaton calibration remains independently valid but
is no longer the primary integration contract:

| bank | literals | sign/type | width range | total literals |
|---|---:|---|---:|---:|
| clean-block | 28 | negative optional primaries | 217--308 | 7,983 |
| automaton frontier | 28 | positive directed darts | 3,225--4,562 | 108,985 |

Both banks address the same sorted 28-target stream, SHA256
`0ce7394af4197d71ae1e06114aea120ece75f64809447fd7d5a3d7b39a492cf2`.
Their clauses are not literal subsets of one another: they use disjoint
variable intervals and opposite semantic directions. The dart row is a
first-exit condition in a directed target automaton. The clean-block row is an
orientation-free saturation certificate saying that at least one selected
optional incidence orbit must be dropped. Both are sound on the exact base,
but only the clean-block rows are designated for the next R2 integration.

The unsolved dart child with SHA256
`b64b537f4674b3ed6866865ae616db9c2a2daef7b9210a7ebb4c95d80495d3b5`
is retained only as a comparison artifact and must not be promoted as the
primary child.

## 7. Frozen source and audit artifacts

CPU-only `g++ -O3 -std=c++20` runs were performed under

```text
/home/amodo/or15/work/r2_k17_v3_rank11_upper_separator_20260802
```

Producer:

```text
scratch/r2_k17_v3_rank11_upper_integration_20260802/
r2_k17_carrier1819_rank12_clean_block_separator_20260802.cpp
  SHA256 d078692535f9c1e88d89b7f005be45a3368850f3a9ff862ec909d253e210018c
carrier1819.clean12.rows.cnf
  SHA256 5b39a2678cb7512f8e10ccfd6e855a410b3f2493f5bcbdec17f1f04c22e8fa18
carrier1819.clean12.targets.tsv
  SHA256 77dabb4e1f991f37ab5bd7fc158a7e392c13145b1c0d7bef49baf5f6622d6f6f
carrier1819.clean12.components.tsv
  SHA256 38681209d16c343d838996bbcc2da776daee64fe0990e036fa40069fdb8b9e7f
carrier1819.clean12.incidences.tsv
  SHA256 0fdda522017de86c7e014b8858e656f6738816cd5b8ac67a7961e81af0ecf5c9
carrier1819.clean12.audit.json
  SHA256 5fbc1d30bf0983a993d962dbdac90728a4d3876803095f69615cff40cb478801
```

The independent checker uses the separately authenticated clean-block parser
source `036d9f248c83fee3d7236049d262a3ed0fde9cf2a4c4e7c3a309f54782ef360f`
as its base-map/factor reader, then independently reconstructs every support,
component partition, persistent hole and incidence row:

```text
audit_r2_k17_carrier1819_rank12_clean_block_independent_20260802.cpp
  SHA256 7958cec56e2edf18cfb893c94fb4ba6a5716f0595aaa36544a182d6e694f0d65
carrier1819.clean12.independent.audit.txt
  SHA256 a95b7b7b4da26fcabf0320f24c960ddff500041d9bb98269148267b29ae5b121
```

Both implementations return the same 28 rows, phase supports, 67,473
components, 104,720 incidences, and width census.

A third, independently written full-development audit under
`/home/amodo/or15/work/r2_k17_v3_rank11_cleanblock_independent_20260802`
starts from the physical factor rather than the producer package. It regenerated
the rank-12 row bank byte-for-byte and independently exported its own target,
component and incidence projections:

```text
scratch/r2_k17_v3_rank11_rank12_lazy_20260802/
audit_r2_k17_carrier1819_clean_block_separator_independent_20260802.cpp
  SHA256 fea6d8f9b0fff9d15af5548814906c4efb7c30bb5e1659f6026d430bd6eca5d7
remote audit.out
  SHA256 2c68e0080597d32d0265fb05be759e358c85e23b26baa5b2003d8959df598741
regenerated rank12 rows
  SHA256 5b39a2678cb7512f8e10ccfd6e855a410b3f2493f5bcbdec17f1f04c22e8fa18
targets projection
  SHA256 173cdcb171a10006bd6ba1fe707ce7ec6d6bb5f8560debbf9a025f6a087c6a65
components projection
  SHA256 981be869a586a417227d13584a075f3a331cd7c2680168de7360d140d54cee3d
incidences projection
  SHA256 29917d2485435dadc60f05b20982a0b275f4efda9b83387513e9bc1c81fbc33e
```

The projections use a different serialization from the R2 proof package, so
their whole-file hashes differ; the regenerated canonical CNF row stream is
identical.

The fail-closed child builder and a separately written whole-child checker are
frozen at

```text
scratch/r2_k17_v3_rank11_rank12_lazy_20260802/
build_r2_k17_v3_rank11_cleanblock596_child_20260802.cpp
  SHA256 4489a3067d885d5b5661007d179c4f1e38b4c04b76c4a2d97f25a50ad6349c40
child596/canonical596.novel34.rows.cnf
  SHA256 a4e843fe72150448e3fb257300d9dd0d0f3826763946480153c8a283b7a8ae89
child596/clean12.canonical28.rows.cnf
  SHA256 ee636df51e363c3d8ca9d299c059ef8d82091a005e5385f56b132a54789b20a3
child596/combined62.rows.cnf
  SHA256 fd338a4582e894015c7d65370e3409d713f3ffe467fed9e3fc159f773aa49521
child596/build.audit.json
  SHA256 598e52beb61d52e46392eea4c9b67248c48b8790405f19fb7531e8d444bb9e65
child596/audit_r2_k17_v3_rank11_cleanblock596_child_independent_20260802.cpp
  SHA256 6aaa80591d0a4e82446f98e6cccecf7f24d8ce2a62546ca743246dd4f1b64182
child596/independent.audit.json
  SHA256 bf59b87647a9feff9b6b5a44bd4d45859549ed8a12b65f6662c398ceabfebd40
```

The initial independent-checker execution failed before issuing a verdict
because it incorrectly required `eofbit` after an `istreambuf_iterator` read.
The checker was corrected to require absence of `badbit`, rebuilt, and run
fresh; the hashes above bind the corrected source and PASS audit.  No CNF or
row bank changed during that correction.

## 8. Scope

This theorem freezes a carrier-only upper separator, a fail-closed live
interface, and an unsolved propagation sibling. It does not make carrier-1819
resident or SAT, and the child is not a resident-factor witness. It does not
prove a lower source realization, root/lower/head correlation, compiler,
seam/opening, exterior cross-windows, regeneration, a contiguous-OR word, or
the final extremal value.
