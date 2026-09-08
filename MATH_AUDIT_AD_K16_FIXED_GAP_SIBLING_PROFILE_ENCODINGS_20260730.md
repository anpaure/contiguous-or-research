# Exact sibling-profile encodings for the K16 fixed-gap shortening gate

Date: 2026-07-30

Status: exact model construction and solver-free census for the two remaining
fixed-gap profiles.  No SAT or UNSAT verdict is asserted.

## 1. Frozen input and exact scope

The only physical input is the authenticated universal word

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
length 12874
```

Its fixed-gap collar architecture is

\[
                  A_5\mid G_1\mid B_9\mid G_2\mid C_4.       \tag{1.1}
\]

The already-live `(4,9,4)` instance is not changed or regenerated here.  The
new emitter covers exactly the two siblings `(5,8,4)` and `(5,9,3)`.  It has
no objective, edit budget, recycled-colour condition, or bounded-window
assumption.

The two supporting imported files are pinned as follows.

```text
scratch/solve_ad_k16_12874_append_template_exact_20260730.py
SHA-256 820bc726f4a9edafb69081e36f24712a0dfe2196ea33271bc661d690056b0cfb

scratch/build_ad_k16_12874_append_template_cnf_20260730.py
SHA-256 2a2ffca7a27511e32ab4539e8ad0e34417ccba2da805bc00f406bf5ca0af7be0
```

The new scripts are

```text
scratch/build_ad_k16_12873_sibling_phase_fusion_cnf_20260730.py
SHA-256 8dafa82e9b7fed4cd3e308aef58253aa16ef56234629497708fb8e254dad6a67

scratch/decode_verify_ad_k16_12873_sibling_phase_fusion_cnf_20260730.py
SHA-256 555e1bcf9eec8b025706c557e698b3b23bd768823259a9c153fd951bc30329f9
```

The decoder also pins the pre-existing DIMACS/replay helper

```text
scratch/decode_verify_ad_k16_12873_phase_fusion_cnf_20260730.py
SHA-256 f0b70293b9cdc9b0ed8280d1eaaf8592bf3b03006b76513f0bcd9397b6a27c6e
```

## 2. Canonical shortened representatives

All positions below are zero based.

For `(5,8,4)`, delete source position `6444`, whose frozen value is `50209`.
The canonical serialization of the resulting length-`12873` representative
has SHA-256

```text
073c54f3129b05a0fa5a63890d69962ccc1a70d29f93444182fc9e8f1bf3645e
```

and the arbitrary nonzero positions are exactly

\[
 [0,5),\qquad[6436,6444),\qquad[12869,12873).            \tag{2.1}
\]

For `(5,9,3)`, delete source position `12873`, whose frozen value is `52833`.
The canonical serialization of the resulting length-`12873` representative
has SHA-256

```text
f59a5c3cf55d77352903e2db10157586e17d882da286753ab11b10652cacd579
```

and the arbitrary nonzero positions are exactly

\[
 [0,5),\qquad[6436,6445),\qquad[12870,12873).            \tag{2.2}
\]

Deleting a different old slot inside the same shortened block does not
enlarge the class: after deletion every surviving block cell is arbitrary,
so both choices parameterize the complete set of ordered words of the new
block length.  The canonical deletions above merely give unambiguous frozen
representatives and hashes.

## 3. Exact interval-pattern theorem

Let `w` be either canonical representative and let

\[
                  p_0<p_1<\cdots<p_{16}                 \tag{3.1}
\]

be its editable positions.  A *fixed run* is a maximal interval avoiding all
`p_i`.

### Theorem 3.1 (interval catalogue equivalence)

The emitted CNF is satisfiable if and only if some assignment of nonzero
16-bit masks to the seventeen editable cells makes the resulting literal
length-`12873` word universal.

#### Proof

Every literal interval is of exactly one of two types.

1. It avoids every `p_i`.  It then lies in one fixed run, and its OR is
   replayed directly in the fixed-run coverage pass.
2. It meets editable cells.  The editable indices it meets form one
   consecutive index interval `[i,j]`.  The literal interval consists of a
   suffix of the fixed run immediately before `p_i`, all editable cells
   `p_i,...,p_j`, every complete intervening fixed gap, and a prefix of the
   fixed run immediately after `p_j`.

For the second type, let `f` be the OR of the chosen fixed suffix, complete
fixed gaps, and chosen fixed prefix.  Duplicate triples `(i,j,f)` are safely
identified because they impose the same condition on every editable
assignment and yield the same interval OR.

Fix a target mask `T`.  The pattern `(i,j,f)` yields `T` exactly when

\[
 f\subseteq T,                                           \tag{3.2}
\]

every editable bit outside `T` is zero in every cell `p_i,...,p_j`, and for
each bit in `T\setminus f`, at least one of those editable cells contains the
bit.  These are precisely the implications guarded by the pattern's witness
variable.  A disjunction over all legal pattern witnesses is imposed for
each target not already covered inside a fixed run.  Each editable cell also
receives the disjunction of its sixteen bit variables, enforcing that the
literal cell is nonzero.

Thus every satisfying assignment chooses, for every residual target, an
actual contiguous interval whose OR is that target.  Conversely, a universal
assignment supplies an actual interval for each residual target; its unique
`[i,j]` and its fixed OR `f` select a legal witness satisfying all guarded
clauses.  Fixed-run targets need no variable witness.  This proves both
directions. \(\square\)

This proof uses literal intervals in one word.  It does not pass through a
rankwise marginal, owner Hall relaxation, or fractional synchronization.

## 4. Solver-free exact censuses

The emitter's `--census-only` path reconstructs the canonical deletion,
verifies its hash, replays fixed runs, and enumerates the deduplicated triples
of Theorem 3.1 without allocating a SAT solver or writing a CNF.

For `(5,8,4)` the exact census is

```text
editable cells                         17
cell-bit variables                    272
deduplicated interval patterns        451
residual targets                       57
witness variables                    4235
total variables                      4507
nonzero-cell clauses                    17
target witness-disjunction clauses     57
positive-bit witness clauses        31393
zero-bit exclusion clauses          97545
total clauses                       129012
maximum fixed-run suffix states         11
census payload SHA-256 ca67c044db450067f1f6533908d84fcfec42e4f39a8a27e954814e17c24614e2
```

The clause arithmetic is exact:

\[
              17+57+31393+97545=129012.                 \tag{4.1}
\]

For `(5,9,3)` the exact census is

```text
editable cells                         17
cell-bit variables                    272
deduplicated interval patterns        462
residual targets                       57
witness variables                    4555
total variables                      4827
nonzero-cell clauses                    17
target witness-disjunction clauses     57
positive-bit witness clauses        33880
zero-bit exclusion clauses         115923
total clauses                       149877
maximum fixed-run suffix states         11
census payload SHA-256 5354e7d99793f30236f2474704aac924c99b61b77c95004102a3c91cc98f4083
```

Here

\[
              17+57+33880+115923=149877.                \tag{4.2}
\]

The seventeen nonzero clauses and the residual-target disjunctions are
included in both totals.  Witness-variable ranges in the emitted map are
recomputed independently by the decoder.

## 5. Equisatisfiable all-profile closure/maximal-context compression

The separate compact emitter uses the independently frozen reduction

```text
THREAD_K_K16_CLOSURE_NORMALIZED_THREE_PROFILE_COMPRESSION_20260730.md

scratch/audit_k16_12873_three_profile_closure_model_20260730.py
SHA-256 29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2

scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
recorded payload d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47
```

The artifact producer hashes its in-memory object before JSON converts
integer histogram keys to strings.  Therefore hashing the parsed JSON body
gives the separately pinned value
`31fce742afdf9af4a8cfc6ded18a8d8bccd6493603010b4e4400d8e19a752e0c`,
not the recorded payload.  The compact emitter checks the authoritative byte
hash, the recorded payload field, and this parsed-body hash; it does not
incorrectly claim that the two payload conventions coincide.

Let `R` be the common 57-target repair family and define, for a nonzero cell
value `v`,

\[
 \operatorname{cl}(v)=\bigcap\{T\in R:v\subseteq T\}.    \tag{5.1}
\]

The two complete separator ORs are `0x7fff` and `0xffff`, and no member of
`R` contains either.  Hence an `R`-witness cannot cross from one collar into
another: such an interval would contain the complete intervening separator.
The compact catalogue may therefore enumerate the three collars locally
without losing a literal witness.

When the containing family is empty the cell is dead for every `R`-witness
and may be replaced by the fixed sentinel `0x0001`.  Otherwise replacing `v`
by `cl(v)` preserves every chosen witness containing that cell: the value
only grows, but remains a subset of the witness target.  Performing these
replacements simultaneously therefore normalizes every feasible assignment
into the 245 nonzero fixed points of (5.1).  Targets outside `R` retain fixed
gap witnesses.  This proves equisatisfiability, but does not preserve Hamming
distance from the incumbent.

For a fixed target and local variable interval, the admissible left suffix
ORs and right prefix ORs are nested chains.  Their largest values contained
in the target are simultaneously physically realizable, and their union
contains every other admissible context.  Hence retaining only this unique
maximal context is also iff-exact.  The compact implementation covers all
three profiles, including the timed-out raw `(4,9,4)` branch, while the raw
sibling implementation in Sections 1--4 remains unchanged.  The scripts are

```text
scratch/build_ad_k16_12873_sibling_phase_fusion_compact_cnf_20260730.py
SHA-256 b9aed39ba84d338b28677d65af7c56073fb620d9e24efc4b938fc86e447b43e4

scratch/decode_verify_ad_k16_12873_sibling_phase_fusion_compact_cnf_20260730.py
SHA-256 08c7f87a6e538141f06eda0277afc33e179848ca656408383435cefdfb313d7a
```

The closure domain has SHA-256
`26f2f21ff9a9a9ad0ab1855a0ab84e5c9ea376f94d61bfdf40865699dce31cb3`.
Its exact bit CNF has 257 clauses and 932 literals per cell, including the
nonzero clause.  The common repair-target list has SHA-256
`f70994a9fb5488fca17c69a9e06873a50d01757d3184e081a2b7c41381040c10`.

The exact compact censuses are:

| profile | local forms | witness vars | total vars | positive | negative | domain clauses | target rows | total clauses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `(4,9,4)` | 65 | 3705 | 3977 | 28292 | 91840 | 4369 | 57 | 124558 |
| `(5,8,4)` | 61 | 3477 | 3749 | 26442 | 78400 | 4369 | 57 | 109268 |
| `(5,9,3)` | 66 | 3762 | 4034 | 28695 | 94080 | 4369 | 57 | 127201 |

The maximal-context ledger hashes are respectively

```text
(4,9,4) df4a5d7ff7b0a9e7a42ac5c398c5acbc46eb790eaa56db94bb478fec4fff8f1a
(5,8,4) 39c869fa2defe5dc039972a2552b1f081dd65092c06d4b553abb14c306459bea
(5,9,3) 3d0087f1781a33da76e7016e126c5a2ac62daaa63844b4c13fde2a3bebfc72c5
```

The solver-free compact census payload hashes, which also pin all imported
source and audit hashes, are

```text
(4,9,4) 6308ab8a292d2a7b8b3fe3a02dce59fdcad5866f55a18ec130340786dad4c858
(5,8,4) 59dfa2688e32561ce5921f421c364c39ad7a5df9ffd111fa7a9592a4c7b55b48
(5,9,3) 2c3601c54cb2cf6bc317f7800da175c8c668943cf761e9db82ff14be98e7f144
```

Thus the compact model removes 762 variables and 21,146 clauses from the
raw `(4,9,4)` model, 758 variables and 19,744 clauses from the
raw `(5,8,4)` model, and 793 variables and 22,676 clauses from the raw
`(5,9,3)` model, without changing any feasible profile family.

An independent adversarial source audit of the final emitter/decoder snapshot
reproduced all three counts and ledger hashes and found no remaining semantic
or provenance defect.

## 6. Fail-closed generation and positive verification

Actual CNF generation is host-gated to H100 CPU.  It refuses changed source
or helper hashes and refuses to overwrite either output.  The map records
the source, canonical deletion, derived-word hash, exact positions, imported
hashes, emitter hash, complete census, bit-variable rows, target witness
ranges, CNF hash, and a stable payload hash.

The decoder requires the operator to freeze the generated CNF hash, map
hash, and map-payload hash explicitly.  It then:

1. checks the source, emitter, helper, CNF, map, and payload hashes;
2. reconstructs the canonical deletion and both its word hash and census;
3. verifies all profile constants, consecutive bit-variable rows, and every
   target witness range;
4. rejects non-SAT, contradictory, out-of-range, or incomplete assignments;
5. parses the complete DIMACS file and checks every clause under the model;
6. decodes all seventeen nonzero masks into the literal word; and
7. independently replays every interval-ending OR and requires no missing
   mask among `1,...,65535`.

Consequently a decoder `PASS_LITERAL_UNIVERSAL_LENGTH12873` result is a
literal positive certificate.  It would combine with the authenticated
lower bound to prove `nu(16)=12873`.

For an UNSAT conclusion, the CNF must additionally have a complete checked
DRAT/LRAT proof.  A timeout, killed process, incomplete proof trace, or
presolve message without checked proof remains `UNKNOWN`.

Both raw and compact emitters reject aliased CNF/map output paths.  Both
decoders reject aliased candidate/audit output paths and explicitly re-hash
their imported semantic helpers.

## 7. Exact remaining boundary

No solver was run and no CNF/map artifact was generated in this audit.  The
two sibling profile models are now executable, but their feasibility is
open.  Even proof-checked UNSAT for both siblings, together with the
`(4,9,4)` branch, would close only the fixed-gap one-block-shortening class of
(1.1), not arbitrary length-`12873` words.
