# R2 audit: k=17 bow-tie CEGAR banks 2--5 and the functional-Hall replay gate

Date: 2026-08-01

Status: frozen read-only audit.  No pricing, CNF build, SAT solve, proof
extraction, or other process was launched on `h100` by this lane.  The remote
payload was inspected after Lane L had completed each stage, and the small
certificates plus full DRAT proofs were copied locally without modifying the
remote directory.

## 1. Exact scope

This audit concerns the fixed k=17 ML9 factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

and the same-base split-option catalogue

```text
scratch/k17_h2_two_cut_closure_20260801/k17_two_cut.candidates.tsv
SHA256 fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6
```

Every promoted bank has 3,805 selected extra cuts, 7,612 physical pieces,
15,224 oriented states, and 7,612 selected rank-eight lower colours.  A
radius-one move in this ledger replaces the chosen split option in exactly
one already split base piece.  It does not move a cut to another base piece,
change the original 3,807-cut decomposition, change the underlying ML9
factor, or apply a C6/q4 factor circuit.

The literal zero vector is

\[
 Z=(Z_L,Z_{\rm out},Z_{\rm in},Z_{\rm coherent},Z_{10}).
\]

Here `Z10=0` means that every missing rank-ten target has at least one
relaxed seam provider in the atlas.  It does **not** say that one selected q1
factor covers all those targets.

## 2. Exact q1 problem

For every piece `p` and orientation `sigma`, let `o[p,sigma]` be its
orientation variable.  For every literal relaxed-resident atom `e`, let
`y[e]` select the seam.  The root q1 CNF encodes exactly

\[
 o_{p,0}+o_{p,1}=1,
\]

\[
 \sum_{e:t(e)=(p,\sigma)}y_e=o_{p,\sigma},\qquad
 \sum_{e:h(e)=(p,\sigma)}y_e=o_{p,\sigma},
\]

and, for every selected lower colour `c`,

\[
 \sum_{e:\ell(e)=c}y_e=1.
\]

Thus a SAT model is an orientation-consistent coloured directed cycle
cover.  The q1 CNFs audited below do not encode selected rank-ten coverage,
connectivity, or the exact all-boundary residence chronology.

## 3. Read-only promotion ledger

The predecessor of this frozen range is
`bowtie_top.bank.tsv`, SHA
`423a759cd9d180a23f221d8ebc6ea388112394bb2c7b028f12fd1668f425803b`.
Each row below is an exact one-row bank substitution.

| remote bank | bank SHA256 | predecessor row -> promoted row | relaxed atoms | missing rank10 | q1 variables / clauses |
|---|---|---|---:|---:|---:|
| `bowtie2` | `8a80469181b5fa13780131baf4be728e0d0ed4a299a0eeac82ea77dacb04106e` | `(6042,6041) -> (6044,6043)` | 228744 | 5098 | 891690 / 2416908 |
| `bowtie3` | `dac02bce9c3ac901566f9da6be50ed4021e561b1793c1d1be68705579839ba62` | `(13673,13672) -> (13676,13675)` | 228788 | 5097 | 891866 / 2417390 |
| `bowtie4` | `941995b772d4ee3b92bdff9a43ac8b4b122ce2cc1bbc73cd212033d99063788c` | `(7841,7840) -> (7854,7853)` | 228776 | 5096 | 891817 / 2417257 |
| `bowtie5` | `9f520aad9d16055a3fb8f961f6967f79a75cd69139579161d2747e236f9489e0` | `(15499,15498) -> (15509,15508)` | 228758 | 5096 | 891745 / 2417059 |

For all four banks, the literal rebuild reports

```text
RELAXED zero_colours=0
RELAXED zero_tail_pieces=0
RELAXED zero_head_pieces=0
RELAXED match_piece_TH=match_piece_TC=match_piece_CH=7612
COMMON_ORIENTATION_ZERO relaxed=0
RANK10_ZERO relaxed=0
```

These are singleton/projection statements only.  Exact q1 is UNSAT at every
stage:

| bank | q1 CNF SHA256 | solver output SHA256 | DRAT proof SHA256 | checked core clauses / lemmas / resolution steps |
|---|---|---|---|---:|
| `bowtie2` | `eaa1326c375e32c78d1069eb01a0d467a3055a8b553bd6f8e34f020bdd7b1139` | `caf9280a03c54e5031082a74a410e8e88279791c2fdc199f02b5a4da73acd1dd` | `b29ec40589405458d4aa2e7a71f9b7d986db63630b6848739738b7c751e6e760` | 19 / 17 / 42 |
| `bowtie3` | `b5a9ad714b85b35cf2271ddfe89feb96feac1e16a3f0752cc23acb240c9fb9ba` | `27e9fe81a4615addf73839a37a60b2e726117af1c7968e2b053a51857e8a6aff` | `8839a260471d8a3086ac62b6b36e32e57910a9050f6ddb939ff1a5a14dbca10d` | 130 / 38 / 700 |
| `bowtie4` | `9642a0b72b9baedfcf9c2649b07d7fab71cd2f692a96c9b42eef95c9ca7e2210` | `5444c07144db6c7b18fab0cb3d11c4950f8b8901a2d2b7f2a0d4c58f05661349` | `616866b2986a5be8132eff64542a1cb8de12ce00a5e857cf2b75d3744cbd909e` | 106 / 32 / 811 |
| `bowtie5` | `31295c96dea470e14a9c107ee3aeb9d23133dfead8239c599a9d75771d375e06` | `f58c68993712ac851e73caab8d413eff4e957b90f30390a274730a104954afa1` | `4ea772e5be743529bcaa64f50413d38151f75f4c6b535bceb65476d15b8e3bda` | 80 / 33 / 217 |

Every checker output ends in `s VERIFIED`.  The exact core/check hashes are:

| bank | core CNF SHA256 | core lemmas SHA256 | corecheck SHA256 |
|---|---|---|---|
| `bowtie2` | `1519987ce57e853aa8b560b31250a5f3dd14841c8c11f6853ddc13b944714ad3` | `128a9d752420cf551de7e6f6a6a59b87eee279e8cda03c56a74a21abdac5e6bf` | `314668a02b0aee764767578be1839ba4807b1623c7c6deef9f5f6fafc512a4ff` |
| `bowtie3` | `d036f43f82c4f122ce0def8de1eaffeaa49eade21f2620870c540d7d9de65667` | `71f3b608ed8ae5f08c04bda4f044046ecf231430cdeaf0a23be80617cbe0a29c` | `5ebb420bf25a6e3beb39df4c591917808db44969419ef79a0eaa49a7b1fab5d9` |
| `bowtie4` | `372ec92712afd177e14d277d40fcc178c3925bc8ca443556866fd68932559e72` | not retained as a separate file | `08adfab49c4d78ffbb75a7308eebe19325e996f1ac805415c9dc1f04662ce824` |
| `bowtie5` | `d4e5aad31be74d9126d493360281382591912e2cec5440c136f737ee042b8241` | not retained as a separate file | `721b7c6a8d53b440b08127886ccd80502c30c2c678f405288966abfdc1addbea` |

The absent separate lemma files at stages 4 and 5 are an artifact-retention
limitation, not a claim that no lemmas were used: their checker transcripts
report 32 and 33 core lemmas respectively.

## 4. Requested third-core pricing result

On `bowtie2`, the decoded core has central piece 3044, leaf 5099, provider
pieces 4159 and 5047, and selected lower masks 114240 and 113224.  The exact
radius-one colour-provider scan reports

```text
moves=16667
Z=0 preserving moves=13030
provider-gain moves=18
baseline degrees (114240,113224)=(4,8)
```

Its promoted bank is `bowtie3`.  The selected move is base piece 2549,
candidate `13672 -> 13675`; it leaves degree 114240 at 4, increases degree
113224 from 8 to 28, and has 228788 relaxed atoms.  Literal rebuild then
reconfirms `Z=0` and all three perfect physical projections.  The exact q1
solve is nevertheless UNSAT with the verified 130-clause core above.

This proves that the one-cut provider move breaks the named third core but
does not solve q1.  It does not prove that this move is best under any global
objective, or that all radius-one core-breaking moves are UNSAT.

## 5. Decoded successor cores

The `bowtie3` core uses orientation pieces 1188, 3371, and 5792.  It has four
seams of lower mask 120354 through pieces 472 and 4031, and 22 seams of lower
mask 119858 through providers 2686, 2771, 3370, 3413, and 5718.

The `bowtie4` core uses the same three orientation pieces.  Its 22 retained
seam variables all have lower mask 119858.

The `bowtie5` core uses orientation pieces 3829, 3954, and 3955.  Its 18
seam variables split as follows:

- ten seams of lower mask 115401, coupling the three core pieces through
  provider 4746;
- six reciprocal seams of lower mask 83657 between piece 3829 and providers
  6853, 7084, and 7441;
- the reciprocal pair of lower mask 115593 between pieces 3954 and 3955.

Audit warning: `bowtie3.core.orivars` contains spurious integer 130 parsed
from the core CNF header.  It is not present in a core clause.  The
proof-safe orientation variables are only the six variables belonging to
pieces 1188, 3371, and 5792.

## 6. Exact functional-Hall/Benders separator

Let `E` be the complete universe of legal option-labelled oriented
tail--head pairs after the master fixes orientations, and let

\[
 \Gamma_C(e)=\{c:(e,c)\text{ is a rebuilt relaxed atom}\}.
\]

The master chooses a directed pair matching `p[e]`.  Conditional colour
recourse is

\[
 \sum_c z_{e,c}=p_e,\qquad
 \sum_e z_{e,c}=d_c,
\]

where `d[c]=1` for each of the 7,612 selected colours.  For every
`X subset E`, exact Hall recourse is

\[
 p(X)\le d(\Gamma_C(X)).
\]

Equivalently, with `M` the recourse matching value and `n=7612`, the
maximum-closure/Benders family is

\[
 \boxed{M+p(X)-d(\Gamma_C(X))\le 7612.}
\]

The exact separator is the min-cut network

```text
source -> oriented pair e     capacity p[e]
e -> selected colour c        capacity 7613 for every rebuilt atom
selected colour c -> sink     capacity d[c]
```

The source-side pair set of a deficient cut is the violated Hall shore.
This is an exact recourse separator only for the complete rebuilt atlas and
the fixed master orientations/pair choices.  On an incumbent-only atlas it
is merely an incumbent-guarded cut.

The analogous TH, TC, and CH projection cuts are necessary diagnostics, not
a characterization of the unconditioned three-resource problem.  The
verified bow-tie cores are explicit counterexamples: all three projections
are perfect while exact q1 is UNSAT.

## 7. Future SAT replay verifier

The source

```text
scratch/verify_r2_k17_relaxed_q1_functional_hall_model_20260801.cpp
SHA256 ff9ca5af2cf96a0b8afe5ab890b4ba6cbf38ff4c2c9f0a255734d8ab18009ee0
```

It imports the canonical factor/cut/state and relaxed-predicate implementation
from `scratch/search_r2_k17_literal_cut_rank10_singletons_20260801.cpp`, SHA
`0dc111142836215496a2f920606c7e0c0b99099f4b14805c39eb9c28ef50de9e`.
Both source hashes are therefore part of any future replay manifest.

is syntax-checked with C++20 and is ready for a future complete Kissat SAT
model.  It performs all of the following before returning PASS:

1. independently checks 48,620 distinct factor incidences, degree two on
   both 24,310-vertex shores, seven alternating cycles, shore permutations,
   and all 26 protected gaps;
2. checks 3,805 distinct selected split options, no protected split, 7,612
   pieces, 15,224 oriented states, and 7,612 selected lower colours;
3. rebuilds the complete relaxed atom atlas from literal owner paths;
4. requires exact tuple/order bijections with the seam and orientation maps,
   and disjoint semantic variable ranges;
5. requires one complete `s SATISFIABLE` assignment and streams every DIMACS
   clause, including auxiliary sequential-counter variables;
6. verifies one common orientation, one incoming seam, one outgoing seam,
   and one seam per selected colour, both per piece and per oriented state;
7. emits the selected seam certificate and successor-cycle decomposition;
8. runs exact maximum matching and Hall-shore extraction on all three pair
   projections and on the three recourses conditioned respectively on TC,
   CH, and TH choices;
9. on the fixed TH face, emits alternating-residual SCC/DM blocks and marks
   selected colour edges forced when they lie on no alternating cycle;
10. recomputes actual internal-plus-selected-seam rank-ten holes, asserting
    zero only when invoked with `REQUIRE_R10`.

Its command line is

```text
verify FACTOR.tsv CANDIDATES.tsv BANK.tsv Q1.cnf SAT.model \
       Q1.orientations.tsv Q1.seams.tsv OUTPUT_PREFIX [REQUIRE_R10]
```

No SAT model existed within the frozen `bowtie2`--`bowtie5` range, so no
positive replay result is claimed here.

## 8. Frozen artifacts and environment

The local bundle is

```text
scratch/r2_k17_bowtie_cegar_readonly_20260801/
```

It contains all four normalized banks, literal rebuild transcripts, solver
transcripts, full DRAT proofs, extracted core CNFs, checker transcripts,
retained lemma/core-variable files, and the available pricing transcripts
and sources.  The H100 environment reported:

```text
host arboghast
AMD EPYC 9354P 32-Core Embedded Processor, 64 logical CPUs
g++ 13.3.0
Kissat 4.0.4
```

Full q1 CNFs and seam maps remain in the read-only Lane L remote directory;
their hashes are frozen in this note.  All four orientation maps have SHA
`daff17d99359a33cb55a6cb0dc495eff3181b7782edd990f860d6c24a16f0645`.

`bowtie6` appeared after the assigned range.  It is explicitly outside this
audit and is not silently incorporated.

## 9. Nonclaims

This audit does not establish any of the following:

- q1 feasibility for a promoted bank;
- a connected Hamilton component or opening/joining topology;
- exact cyclic residence rather than the encoded relaxed two-block test;
- selected rank-ten completion from `RANK10_ZERO=0`;
- ranks 11--17 or all-width exterior cross-windows;
- terminal/common compiler compatibility;
- rooted `ae88` attachment compatibility;
- regeneration or `nu(17)=24313`.
