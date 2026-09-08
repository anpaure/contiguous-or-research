# Audit of Claude's quotient-CEGAR artifacts at k=9 and k=11

Date: 2026-07-28

Source directory audited: `/Users/amir.nuriyev/Downloads/opusproblem/work`

This is a certificate audit, not a rerun of either search. No SAT, CP-SAT,
Kissat, exhaustive search, GPU job, or other heavy computation was run. The
checks below are direct, solver-free evaluations of the saved selections and
literal words. The independent checker is
`scratch/audit_claude_quotient_cegar_k9_k11.py`; its complete machine-readable
output is `scratch/audit_claude_quotient_cegar_k9_k11.json`.

## 1. Verdict

There are two distinct claims, with different audit outcomes.

1. **Positive mathematical certificates: proved.** The files
   `k09_equi_new.word` and `k11_equi_new.word` are valid literal contiguous-OR
   words of lengths 128=B(9) and 465=B(11), respectively. Thus they are
   unconditional alternative certificates of ν(9)=128 and ν(11)=465, using
   the already-proved monotone-deadline lower bound. The saved final quotient
   selections also reconstruct exactly the claimed physical middle cycles,
   and their cuts are exactly the middle rows of the saved words.

2. **End-to-end search reproduction: not frozen.** The artifact directory does
   not retain a complete solver transcript. In particular, it has no final
   DIMACS files, SAT/CP-SAT models, complete lazy-cut ledger, solver binary or
   version hash, dependency lock, or source-hash manifest. There is a short
   k=9 progress log but no corresponding k=11 log. Therefore the positive
   outputs are independently verifiable, but the historical search cannot be
   reproduced byte for byte from the retained evidence alone.

The quotient pipeline is sound for a positive candidate because it rebuilds
and directly audits the physical cycle before returning `PASS`. It is not a
complete formulation even of its nominal equivariant/rainbow geometry: one
lazy lower-q2 template omits valid same-insertion paths. It is also not a
without-loss-of-generality formulation of all optimal words. Consequently a
positive `PASS` is sound, whereas an `UNSAT` result excludes at most the still
narrower accumulated-template submodel and proves no geometric no-go.

## 2. Frozen hashes

The decisive artifacts have the following SHA-256 hashes.

| Artifact | SHA-256 |
|---|---|
| `equi.py` | `aa450955ce91283bfc34f6365d355aa24d98c8121cdbc814de2dc707e4b5ba64` |
| `equicegar.py` | `99a3072fa6c3de6080cf85e6fa2cfcc289e7a8faa703da5b1374488ec834221d` |
| `equi2.py` | `d939b89386a313ff306c659f18813c582e3f0cb822c731b44aab7f16776093ff` |
| `cpsat.py` | `aa4e56dbf7b8773fff65f6432857ec8d5123434de8ea0f207b828de55df7aeaf` |
| `cutcompile.py` | `ae61b7a333a450a4dc13216349e0ab2ddbb2104e5685be3b698ce12816a58a13` |
| `gates.py` | `7d237cc60748e786b84f0235b07b5b2e7b658990f6ca3c69132073aea16f7b63` |
| `lib.py` | `a744bfcedd5786b73a6cbc54d62e9b056f188084a768fbcaf3459726b6b72845` |
| `k9_cegar.log` | `2e25584dc4d205b83ba7528ec5d271351d23c0764bd4c00fb574c3bd2efe955d` |
| `equi2_k9_rnd12.json` | `81b11db074ee29ed0d9ea537d49ac01bde7f212b106bc3a6c7871a5d5be878ad` |
| `k09_equi_new.word` | `0f282a2c5bb61c0ea48d49c5966eafba3ceb8a30cc40150a92764c1321c21b7c` |
| `equi2_k11_rnd34.json` | `05832de6a2aa7191dc99dc7133b67b852539278a930cf717bb12ed9a301616e7` |
| `k11_equi_new.word` | `0dee7330a1c912f3b568dd0a669fbc823cf79e68b76f32ef37bb7afed6ebe77a` |
| `k11_carrier.txt` | `b19825b5965067506cea862fb64ea03eb42f9eeda683c61bffccc69857a3007f` |
| `k11_pass_tuples.json` | `48a0fb50b8e8ef89c5055bb4dedc321a3877faa805334ffa451e5be3129582ec` |
| late `LEDGER.md` | `427d0eaa1c2dd65a4afd8246c5bb26c57e834fc9622294acabcab274665d19c3` |
| late `compile15.py` | `b288dc1d23898ee9a7bd4e18fd25d8ff8651cc130dd8c3ccc3ec9fa7e22bad8b` |
| late `carrier.cpp` | `63af840ff141b5ded1ca477e9694eed590c3184ab46a3a163ab43767d4c98542` |
| late `strictdfs.py` | `625e924041bff140cb469450116db8b128279bdcf770a16ec223ce1b7da13dff` |
| repository `verify_word.py` | `7beea259577d243b8952634a39baef2c38d3dd5adb33649de1314b9975163b79` |
| independent audit script | `0bcc97c4bcc3bd07e80d6a2a40e87df26b7f5335093acd34bffae191e550f242` |
| independent audit JSON | `7914ceb5ffca62292be2be4286686d2915878383a70ccc0a70821cb4621d2e75` |

The hashes of every retained intermediate `equi2_k*_rnd*.json` and
`cpsat_k11_rnd*.json` are recorded in the machine-readable audit JSON. The
repository verifier is byte-identical to the verifier in Claude's downloaded
`contiguous-or-research` checkout.

For comparison, the repository's already-authoritative witnesses are:

| Existing repository word | SHA-256 |
|---|---|
| `answers/k09.word` | `c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221` |
| `answers/k11.word` | `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850` |

Both differ from Claude's new words. Thus the new files are alternative
witnesses, not copies of the current answers.

`k11_pass_tuples.json` is a late explicit-tuple normalization of the final
k=11 selector. Its 42 triples `(lower representative mask,a,b)` agree exactly
with the expansion of all 42 indices in `equi2_k11_rnd34.json`. This removes
the dependence of the undirected selection on a choice-table index, although
the file does not retain the direction bits.

## 2A. Provenance baseline: the symmetric middle-level cycle

The canonical symmetric-cycle baseline is not an undocumented heuristic.
Merino, Mička, and Mütze prove that for every shift s coprime to 2n+1 there is
a symmetric star-transposition ordering, and give an O(n)-time-per-object,
O(n)-space generator in [*On a combinatorial generation problem of Knuth*,
arXiv:2007.07164](https://arxiv.org/abs/2007.07164). Their paper states that
the implementation is available from the [Combinatorial Object
Server](https://www.combos.org/). After omitting the alternating first bit,
this is exactly the symmetric Hamilton-cycle/necklace formulation used by
the quotient comparison here.

For k=15, the canonical shift-1 cycle has strict quotient voltage 1 and its
Johnson projection is q1-lower-perfect. It is nevertheless only a baseline,
not a carrier satisfying the extra contiguous-OR gates. Its exact gate census
is:

| Gate | Defect count |
|---|---:|
| cyclic residence runs of length 2 | 1,500 |
| cyclic residence runs of length 3 | 480 |
| upper q=1 missing | 550 |
| lower q=2 missing | 550 |
| lower q=3 missing | 528 |
| all upper ranks missing | 1,338 |

Thus symmetry, voltage one, Hamiltonicity, and perfect q1 lower colours do not
imply residence or deeper two-sided support. The fresh k=9 and k=11 quotient
outputs are stronger precisely because their direct physical audits have zero
defects in all of those required categories. This comparison does not claim
that the k=15 baseline can be repaired by the present CEGAR templates.

The theorem proof and H100 replay are separately documented in
`MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`. The frozen
stdout `scratch/audit_knuth_symmetric_middle_k15.out` has SHA-256
`42a91af7ad1635ee23109d37a3439a70dfe1df2db24aca7cb0a29f86fed49e65`
and records executed checker SHA-256
`8df79082426895cd3c7739971e9a09e5ad6137d3c3a46536fb10e331ab7c8880`.
The working checker was subsequently extended and has a different hash, so
the stdout's embedded source hash is the correct provenance for that run.

## 3. Exact k=9 certificate

### Theorem 3.1

Let A be the 128-entry sequence in `k09_equi_new.word`. Every nonempty subset
of [9] occurs as the bitwise OR of a contiguous interval of A. Moreover, D²A
is a permutation of the 126 rank-five masks. Consequently ν(9)=128.

### Proof

Direct interval enumeration found all 2⁹−1=511 nonzero masks. Every letter is
a nonzero 9-bit mask. The derivative rows are:

| Row | Length | Exact audited structure |
|---|---:|---|
| D⁰A | 128 | 128 distinct entries; ranks 1⁹, 2³⁶, 3⁸³ |
| D¹A | 127 | 127 distinct entries; ranks 3¹, 4¹²⁶ |
| D²A | 126 | 126 distinct rank-five masks |

The union of the first two rows contains each of the 255 masks of ranks one
through four exactly once. In particular every lower target is realized by an
interval of width at most d=2. The final row is exactly the complete rank-five
layer. The established lower bound gives B(9)=126+2=128, proving equality. ∎

### Proposition 3.2: quotient provenance

With the enumeration in the frozen `equi2.py`, the 14 selected choice indices
in `equi2_k9_rnd12.json` choose exactly one of the ten edge choices over each
of the 14 rank-four rotation orbits. Their nine-sheet lift has these exact
properties:

- It has 126 edges and every rank-five mask has degree two.
- It is one 126-vertex physical cycle.
- Its 126 edge intersections are exactly the rank-four masks, each once.
- The saved direction bits orient it as one directed cycle. Under left
  rotation, its directed quotient voltage is 4 modulo 9, hence coprime to 9.
- Its minimum cyclic coordinate residence is three, exactly the required d+1.
- Every upper mask and every depth-two lower trace occurs.

The deterministic cycle order used by `cutcompile.py` has 54 cuts passing the
linear residence and upper-shadow gates. Cut index 2 is the first such cut,
and the resulting path is exactly D²A. The saved word is entrywise below the
maximal linear erosion of that path and satisfies every lower compiler target.
This verifies the complete relation from frozen quotient selection, to
physical cycle, to cut-2 path, to A without invoking a solver.

The upper rank-six quotient loads are not capped by two: their histogram is
1⁷ 2² 3¹. Thus this carrier is valid for coverage, but it does not solve any
separate ansatz requiring upper load at most two.

## 4. Exact k=11 certificate

### Theorem 4.1

Let A be the 465-entry sequence in `k11_equi_new.word`. Every nonempty subset
of [11] occurs as the OR of a contiguous interval of A, and D³A is a
permutation of all 462 rank-six masks. Consequently ν(11)=465.

### Proof

Direct interval enumeration found all 2¹¹−1=2047 nonzero masks. Every letter
is a nonzero 11-bit mask. The derivative profile is:

| Row | Length | Distinct entries | Rank census |
|---|---:|---:|---|
| D⁰A | 465 | 236 | 1⁴⁴, 2¹⁷⁴, 3²⁴¹, 4², 5⁴ |
| D¹A | 464 | 368 | 2⁷, 3²⁹, 4⁴²⁴, 5², 6² |
| D²A | 463 | 463 | 4¹, 5⁴⁶⁰, 6² |
| D³A | 462 | 462 | 6⁴⁶² |

Every target of ranks one through five has a realizing interval of width at
most d=3. The row D³A is exactly the complete rank-six layer. The established
lower bound gives B(11)=462+3=465, proving equality. ∎

### Proposition 4.2: quotient provenance

With the frozen `equi2.py` enumeration, `equi2_k11_rnd34.json` selects 42 of
630 choice orbits, exactly one over each rank-five rotation orbit. Its
eleven-sheet lift has these exact properties:

- It is one directed 462-cycle through every rank-six mask.
- Every step is a Johnson step and the 462 edge intersections are precisely
  the rank-five masks, each once.
- The directed quotient voltage is 2 modulo 11.
- The minimum cyclic coordinate residence is four, exactly the required d+1.
- There are no depth-two or depth-three lower holes and no upper hole at any
  rank.

The deterministic `cutcompile.py` order has 242 cuts passing the path
residence and upper gates. Cut 0 is the first, and its path equals D³A exactly.
The word lies below its maximal erosion and every lower target has an interval
of width at most three. The current frozen compiler instance for this cut has
26,337 variables and 151,148 clauses: 1,407 letter-bit variables and 24,930
target-window selectors. These counts were obtained by constructing, but not
solving, the CNF.

The upper rank-seven quotient loads have histogram 1¹⁹ 2¹⁰ 3¹. Again,
coverage is exact but a separate upper-load-two condition fails once.

### Correction concerning `k11_carrier.txt`

`k11_carrier.txt` is not the carrier of `equi2_k11_rnd34.json`. It is exactly
D³ of the repository's older `answers/k11.word`; its cyclic order is different
from the new quotient selection. It independently has no cyclic residence,
upper, or depth-two/depth-three lower defect, but it supplies no provenance for
`k11_equi_new.word`. The scripts `q11.py` and `extract_k11.py` load the old
answer through the absolute `lib.ANS` path and analyze this old carrier. They
should not be cited as verifiers of the new CEGAR result.

## 5. Exact quotient model in `equi2.py`

Let k=2r−1. Let L be the rotation orbits of rank-(r−1) masks and M the
rotation orbits of rank-r masks. For k=9 and k=11 all these orbits are free. At
k=9 this follows because a period-three binary word has weight divisible by
three, whereas the relevant weights are four and five; at prime k=11 every
nonconstant orbit is free.

For each lower representative L and unordered pair {a,b} outside L, a choice
is the full rotation orbit of the Johnson edge L∪{a} -- L∪{b}. There are 140
choices at k=9 and 630 at k=11.

The SAT variables are:

- c_i: select choice orbit i;
- d_i: orient all physical rotations of choice i coherently;
- A_(V,x,j): at quotient middle representative V, coordinate x has propagated
  age j in {1,...,d}.

The eager clauses impose:

1. exactly one c_i over every lower orbit;
2. weighted degree at most two at every middle orbit, counting a quotient
   self-loop twice;
3. no two selected incidences both enter, or both leave, a middle orbit;
4. insertion, age propagation, and prohibition of deletion at ages at most d;
5. coverage of every rank-(r+1) upper orbit.

Exactly |M| choices are selected, so the total weighted degree is 2|M|. The
degree caps therefore force degree exactly two at every middle orbit. The
eager CNFs, before lazy clauses, have these frozen-source counts:

| k | lower/middle orbits | choices | variables | clauses |
|---:|---:|---:|---:|---:|
| 9 | 14/14 | 140 | 980 | 9,268 |
| 11 | 42/42 | 630 | 4,536 | 64,784 |

The CEGAR loop adds:

- positive quotient-component cut clauses;
- a no-good for a selected factor whose physical lift has multiple cycles;
- OR-of-AND clauses for a missing lower depth-two or depth-three orbit;
- OR-of-AND clauses for missing upper depth two;
- a selection no-good when a directly checked missing upper orbit has no
  implemented local cover clause.

Every OR-of-AND group that the builder emits is a sound sufficient motif: an
auxiliary selector implies every choice in one physical motif, and at least
one selector is required. The reverse implications are unnecessary. In a
selected two-factor, the emitted motif edges are consecutive at their shared
vertices, and reversal does not change their intersection or union. Likewise,
physical connectedness, cyclic residence, and cyclic interval support depend
only on the selected undirected factor, so a selection-level no-good does not
incorrectly discard a different useful orientation of the same factor.

The motif catalogue is not complete. In `cover_lower_q2`, the loop explicitly
rejects `q2 == p`, thereby omitting valid triples whose two outer vertices add
the same coordinate to the central vertex. This omission affects both passing
factors:

- At k=9, canonical lower target 37 is covered by nine rotated triples, all of
  same-insertion type. One is `(S,u,v,w)=(81,241,213,117)`, using selected
  choices 62 and 137 and common outer-added coordinate 5. The builder emits
  180 groups for target 37, but none is contained in the final selection.
- At k=11, canonical lower target 201 is covered by eleven rotated triples,
  again all same-insertion. One is `(562,1590,1650,630)`, using selected
  choices 396 and 505 and common outer-added coordinate 2. The builder emits
  420 groups, but none is contained in the final selection.

These direct finite counterexamples disprove template completeness. Had
either clause been accumulated, it would have rejected the corresponding
valid final factor. This cannot create a false positive because every SAT
endpoint is rebuilt and audited physically; it can create false restricted
`UNSAT` or search exhaustion. Therefore even an exhaustive SAT result for an
accumulated CEGAR formula is not exhaustive for the nominal
equivariant/rainbow geometry.

The final code independently checks quotient connectivity, the number of
physical cycles, residence, every upper rank, and lower depths two through d.
Therefore a reported positive candidate does not rely solely on the eager
automaton or lazy-clause generator. The solver-free audit repeated those
physical checks without importing `equi2.py`.

### Exact scope

The model deliberately assumes cyclic coordinate equivariance, one complete
edge orbit over each lower orbit, a perfect lower rank-(r−1) rainbow, a
two-regular middle factor with one equivariant orientation bit per edge orbit,
and the particular erosion-to-word compiler used after a safe cut. These are
sufficient conditions, not proved normal forms for arbitrary optimal words.
Moreover, the accumulated motif clauses may be strictly narrower than those
conditions. Thus no geometric or global impossibility theorem may be inferred
from an `UNSAT` result in this model.

## 6. Exact compiler model in `gates.py`

Fix a linear middle chronology T=(T_0,...,T_(W−1)) and depth d. Its maximal
erosion P has length W+d, with P_i equal to the intersection of those T_j for
which max(0,i−d)≤j≤min(i,W−1).

The compiler has a Boolean variable for coordinate x in P_i in word letter
A_i. It enforces:

1. A_i is nonempty for every i;
2. every bit of T_j appears in A_j OR ... OR A_(j+d);
3. for every target S below the middle rank, some interval of width at most d
   has OR exactly S.

Because A_i is a subset of P_i, condition 2 is equivalent to D^d A=T: the
erosion forbids every extra bit. For a target-window selector, the clauses
require every bit of S somewhere in the window and forbid every bit outside S
in every letter of that window. Hence condition 3 is also exact, not a
marginal or Hall relaxation. Middle targets are the entries of T, and any
upper interval of T lifts to the corresponding enlarged interval of A.
Therefore path residence, path upper coverage, and a satisfying compiler
assignment imply a literal universal word. Both saved words were nevertheless
checked directly over all intervals.

The final-cut compiler counts are:

| k | variables | clauses | letter-bit variables | selectors |
|---:|---:|---:|---:|---:|
| 9 | 3,283 | 13,721 | 390 | 2,893 |
| 11 | 26,337 | 151,148 | 1,407 | 24,930 |

## 7. What the retained logs do and do not prove

### k=9

`k9_cegar.log` is internally consistent with the source and saved snapshots.
It records 13 SAT rounds, quotient component cuts, one three-cycle voltage
split, depth-two holes in rounds 7 and 9, and the hole-free round-12 `PASS`.
The saved round-7, round-9, and round-12 JSONs independently reconstruct as
single physical cycles with lower depth-two missing-orbit lists `[73]`, `[11]`,
and `[]`, exactly as recorded.

The log is not a proof trace. It does not contain the generated CNFs, models,
the 15 concrete lazy clauses, a solver version/hash, or the compiler run.

### k=11

There is no k=11 CEGAR log. The retained rounds 1, 17, 27, 31, and 34 are
semantically valid snapshots, and their recorded hole lists agree with direct
reconstruction. Round 34 is the exact positive certificate. The missing
round-by-round cut ledger, solver output, and command line prevent historical
search replay.

A late-added `LEDGER.md` says the architecture was validated end to end at
k=9 and k=11 and reports approximately 12 minutes and 35 rounds for k=11.
The architecture claim is supported by the independent certificate chain in
Sections 3--6: the final selector, cut, compiler semantics, and literal word
all agree. The timing and exact round history are not independently auditable:
round 34 is consistent with a 35-round zero-based run, but no k=11 log,
solver transcript, final accumulated CNF, or lazy ledger survives.

The same ledger gives node counts and timings for `strictdfs.py`, again
without saved run logs or output certificates. Those performance statements
are historical notes, not reproduction evidence. The current recursive
`carrier.cpp` has balanced path/visited/colour undo on code inspection, but it
has no saved k=9/k=11 pass artifact and is not part of either certificate
chain audited here.

### Portability and determinism

Both `equi2.py` and `gates.py` hardcode `/opt/homebrew/bin/kissat`. `lib.py`
hardcodes an absolute answer directory under Claude's downloaded checkout. No
solver version or Python dependency file is present. The compiler invocation
has no recorded seed, and `cutcompile.py` stops after at most eight
gate-passing cuts. Even after making the paths portable, a different solver
build may return another valid assignment and therefore another valid literal
word. This does not weaken the saved positive words, but it defeats a
byte-identical regeneration claim.

The source directory changed during this audit: `k11_pass_tuples.json`,
`LEDGER.md`, `compile15.py`, `carrier.cpp`, and several exploratory scripts
appeared after the first inventory. Consequently a directory-wide claim must
name a cutoff or ship a hash manifest. All claims in this report refer to the
specific hashes in Section 2; later same-name replacements require a new
audit.

The repository `verify_word.py` correctly asserts nonzero in-range letters,
universal interval coverage, and optimal length. It computes and prints the
central-layer exactness flag but does not assert that flag. The new independent
audit explicitly asserts the central row, Johnson adjacency, quotient
provenance, and compiler semantics, so this verifier omission does not affect
the conclusions here.

## 8. CP-SAT branch

`cpsat.py` is a separate model. It removes five quotient self-loop choices at
k=11, leaving 625 choices and 1,250 directed arcs, and uses `AddCircuit`, one
choice per lower orbit, a coprime-voltage constraint, a residence automaton,
upper-depth-one coverage, and lazy deeper support cuts.

### Selector-ID incompatibility

Bare integer selector IDs from `cpsat.py` are incompatible with
`cutcompile.py`. The former deletes quotient self-loop choices before assigning
IDs, while the latter imports `equi2.Carrier`, whose choice table retains them.
The exact divergences are:

| k | `equi2` choices | CP-SAT choices | skipped loops | first divergent ID |
|---:|---:|---:|---:|---:|
| 9 | 140 | 135 | 5 | 3 |
| 11 | 630 | 625 | 5 | 4 |
| 15 | 12,012 | 11,998 | 14 | 6 |

This is a real file-interface failure, not a theoretical warning. Correctly
decoding `cpsat_k11_rnd0.json` gives a connected 462-vertex 2-regular graph.
Decoding its 42 IDs through `equi2` as the original `cutcompile.py` would do
instead gives 418 vertices and 462 distinct edges, degree histogram
`{1:143,2:154,3:33,4:66,5:22}`, largest component 363, and all 42 choice
tuples wrong. The independent verifier branches explicitly between the two
catalogues and therefore does not make this error.

The durable serialization is an explicit tuple `(lower representative,a,b)`,
plus direction data and a digest of the ordered choice table. The new
`k11_pass_tuples.json` supplies the explicit undirected tuples for the final
`equi2` factor, but not directions. The late `compile15.py` rebuilds CP-SAT's
no-self-loop enumeration for integer inputs and accepts tuple inputs; it is a
repair path for future artifacts, not evidence for the historical k=9/k=11
solver runs.

All nine saved files `cpsat_k11_rnd0.json` through `rnd8.json` reconstruct,
under that distinct no-self-loop enumeration, as genuine 462-cycles with
degree two, exact lower rank-five colours, and no residence defect. Their
saved hole counts agree with direct checks. None is a complete candidate:

| Round | upper holes | lower q=2 holes | lower q=3 holes |
|---:|---:|---:|---:|
| 0 | 0 | 5 | 0 |
| 1 | 0 | 0 | 1 |
| 2 | 1 | 5 | 0 |
| 3 | 1 | 2 | 0 |
| 4 | 0 | 1 | 0 |
| 5 | 1 | 3 | 0 |
| 6 | 0 | 4 | 0 |
| 7 | 0 | 1 | 1 |
| 8 | 1 | 2 | 0 |

The JSON files omit the chosen directed arcs, and there is no final `PASS` or
CP-SAT log. The local environment also lacks the OR-Tools dependency needed to
import the model. These files are exact regression states for their saved
undirected selections, but the CP-SAT line remains incomplete and should be
classified as exploratory rather than as a certificate.

## 9. Reuse boundary in the current repository

### Reusable now

- `verify_word.py` already verifies either new literal word unchanged. The
  independent audit adds stronger central-row and provenance assertions.
- The current repository already proves both exact finite values with
  different words, so importing the new words is not needed to establish
  ν(9) or ν(11).
- The final `equi2` JSONs plus the frozen source hashes are compact exact
  witnesses of two equivariant, lower-rainbow, resident middle cycles. They are
  mathematically reusable from the current external path as alternate carrier
  data. They are not yet a durable self-contained repository asset because the
  source JSONs and words have not been vendored here.
- The exact compiler formulation in `gates.py` is reusable after replacing
  hardcoded paths by arguments. It enforces literal simultaneous lower
  coverage, not merely rankwise marginals.
- `scratch/audit_claude_quotient_cegar_k9_k11.py` is a solver-free verifier for
  all retained `equi2` and CP-SAT snapshots, both final words, their quotient
  directions and voltages, deterministic cut indices, and the old/new
  `k11_carrier.txt` distinction.

### Reusable only after hardening

- `equi2.py`, `cutcompile.py`, and `gates.py` need configurable solver paths,
  explicit source/schema hashes in output JSON, dependency/version capture,
  retained CNF/model hashes, and a complete lazy-clause transcript for a
  publication-grade reproduction package.
- Choice indices should be supplemented by explicit choice tuples or the full
  physical cycle. At present k=9 still depends on the frozen choice table;
  k=11 now has explicit undirected tuples but no tuple-keyed directions.
- `cutcompile.py` should call an independent verifier and record the cut,
  compiler CNF hash, solver status/model hash, and final word hash.

### Not a proved reusable theorem

- Neither quotient search is WLOG for arbitrary optimal contiguous-OR words.
- The lower-q2 lazy template is incomplete even within the equivariant/rainbow
  geometry, by the same-insertion counterexamples in Section 5.
- The final carriers do not satisfy upper-load cap two.
- The CP-SAT snapshots do not pass all gates.
- The search logs cannot support a solver-performance or deterministic-rerun
  claim.
- `k11_carrier.txt`, `q11.py`, and `extract_k11.py` concern the older repository
  answer, not the new CEGAR selection.

## 10. Reproduction command for the audited positive artifacts

The complete solver-free replay is:

```sh
python3 scratch/audit_claude_quotient_cegar_k9_k11.py --source /Users/amir.nuriyev/Downloads/opusproblem/work --output scratch/audit_claude_quotient_cegar_k9_k11.json
```

It finished with `status: PASS`. This command only parses small saved files
and performs direct finite certificate checks; it launches no solver and no
search. Its scope is deliberately stated in the output as
`solver-free certificate replay; no claim of search-transcript reproducibility`.

## 11. Sharp proved/heuristic boundary

The exact finite conclusions and the explicit carrier-to-word provenance are
proved. The eager constraints and every emitted lazy motif are sound
sufficient restrictions, and direct endpoint audits protect every positive
`PASS`. The lazy motif family is not complete, even for the nominal
equivariant/rainbow geometry. What remains heuristic or undocumented is the
historical process by which the solvers found the candidates, any negative or
exhaustion claim, the performance claims without logs, and byte-for-byte rerun
reproducibility. No negative theorem follows from these artifacts.
