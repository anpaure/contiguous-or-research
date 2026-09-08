# Unrestricted fixed-bank triple caps: exact CNF and one solver result

2026-09-08. Prepared and executed by `exact_b_finite_frontier` after complete source review by the root agent, `exact_b_induction`, and `exact_equality_structure`.

**Updated status: the identical formula now has an independently accepted DRAT proof.**
See [the proof-export repair and accepted certificate](K17_UNRESTRICTED_TRIPLE_CAPS_INDEPENDENT_DRAT_CERTIFICATE_20260908.md).
This document records the original single solver call and its truncated,
rejected proof. A later identical-formula, identical-seed replay recovered
the complete proof after explicitly flushing the native C stream; there
were two cap-formula decision calls in total. No alternate instance or seed
was tried. The original failed artifact remains unchanged.

## 1. Exact scope of the instance

Use the original 146 canonical k17 PBBS cycles, with their original cuts and order, and aperture `H=min(height,3)`. The source file SHA-256 is

`fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3`.

All H=1 and H=2 components remain completely unchanged. Their fixed lower palette contains exactly 1,887 targets, all of rank seven. There are no full anchors on the H=3 components. Every H=3 position may independently shrink to any nonempty cap between its required pins and its original rank-six source letter.

The constraints preserve **every original rank-eight triple occurrence** on H=3, and require every target of ranks one through seven to have an ordinary cyclic witness in the bank. Witness intervals may overlap freely and share the same cap-coordinate variables.

The formal encoding equivalence is proved in
[the unrestricted cap CNF audit](PBBS_UNRESTRICTED_TRIPLE_CAPS_COMPLETE_CNF_AND_SPARSE_RUN_CLAUSES_20260908.md).
The exhaustive host census is in
[the triple-preserving host note](K17_TRIPLE_PRESERVING_SHORT_HOSTS_AND_CANONICAL_ANCHOR_MENU_CERTIFICATE_20260908.md), §2; its later anchor restriction is **not** used here.

This instance is strictly more general than the earlier impossible every-third-anchor frame. It still has definite limitations: it freezes H≤2, preserves all native H3 triples, keeps this fixed bank, and requires lower targets to be realized inside its cyclic components. It does not include new witnesses across later component joins, altered owners, changed native triples or arbitrary new words.

## 2. Variables and exact forward implications

There is one Boolean variable for every optional coordinate of every H3 cap. Pinned coordinates are constant true, and coordinates outside the original letter are constant false. Constants are handled by explicit bitmask tests, avoiding any ambiguity between Boolean `True` and variable number one.

For each native triple and each of its coordinates, require the coordinate to survive in at least one of the three caps. Clauses already satisfied by a pin are omitted. The source-run endpoint lemma shows every remaining clause has exactly three optional variables; the generator checks that claim directly. Cyclic wraparound triples are included.

A lower target must use one or two positions because every three-position interval already contains a preserved rank-eight triple. The exhaustive individual host criterion is

\[
\bigcup_{i\in I}\operatorname{Pin}_i\subseteq S\subseteq
\bigcup_{i\in I}D_i,\qquad |I|\in\{1,2\}.
\]

For every such host of a nonfixed target S, introduce a witness variable y. Its forward implications require:

- every optional coordinate outside S to be absent from every cap in the interval;
- every coordinate of S not already supplied by a pin to be present in at least one available cap position.

For each nonfixed target, require at least one of its witness variables. Reverse implications, exclusivity constraints and at-most-one witness constraints are unnecessary. Shared cap bits enforce consistency between overlapping chosen witnesses.

The frozen palette is computed solely from H≤2. None of the full-anchor labels or rank-six reservations from earlier failed models are retained in this formula.

## 3. Exact formula census

| Quantity | Count |
|---|---:|
| Optional cap-coordinate variables | 90,576 |
| Witness variables | 630,309 |
| Total variables | 720,885 |
| Preserved native H3 triples | 22,134 |
| Enumerated individual one/two-position hosts before fixed-target omission | 631,992 |
| Nonfixed required lower targets | 39,338 |
| Positive native-triple clauses | 61,472 |
| Witness inclusion clauses | 1,238,773 |
| Witness exclusion clauses | 1,683,816 |
| Target-coverage clauses | 39,338 |
| Total clauses | 3,023,399 |

The exact DIMACS SHA-256 is

`673d26f3dc605da62cdfa335953c1637eb1375f0fee82e85822b68ab4b8747ab`.

The formula and mappings were streamed to disk, without retaining all three million clauses as Python objects. Formula generation took approximately 7.42 seconds.

## 4. The one approved solver call

The solver was PySAT's **CaDiCaL195**, configured once with seed zero and proof logging. It made one public `solve()` call. The result was `False` (UNSAT).

The returned statistics were:

- 1,130 conflicts;
- 1,565,640 decisions;
- 45,446,192 propagations;
- 93 internal CaDiCaL restarts.

Those 93 internal algorithmic restarts occurred inside the single solver call; they are not additional invocations, seeds, configurations or resumed attempts. The script made zero external solver restarts.

The worker, including formula loading, took approximately 6.94 wall seconds. Total generation, solving and report time was approximately 14.71 wall seconds and 14.68 aggregate CPU seconds.

The run enforced a total 120-second CPU budget, a total 150-second wall budget, driver/worker address-space soft limits of 512 MiB and 3,584 MiB, and a 1 GiB worker single-file limit. It asserted the exact source hash and the h100 hostname `arboghast`. A worker timeout or file/memory/CPU exhaustion would have produced INCONCLUSIVE without another solve. No limit was reached.

The raw binary DRAT stream is **1,448,580 bytes**. The script saves it without asserting that its contents constitute an independently accepted proof.

## 5. Proof status and retained artifacts

Read-only discovery initially found no DRAT/LRAT checker on PATH or in the inspected common executable/source directories. This task did not install a checker. The root agent subsequently built the official `drat-trim` separately and checked the saved binary proof. It reported `ERROR: no conflict` after reading the artifact. That failure is retained rather than treated as successful certification.

The capture path copied the Python temporary file before deleting the solver. Its `prfile.flush()` call flushes the Python file object, and does not itself establish that CaDiCaL's separate C stdio buffer has been flushed. A read-only inspection of the installed Python binding also found that `Cadical195.get_proof()` merely seeks, reads and decodes that temporary file; substituting that method alone is not a demonstrated fix. A missing buffered tail is a hypothesis under investigation, not a verified explanation of the failed check.

The root agent subsequently parsed the binary artifact and found that its last complete operation ends at byte 1,448,577, followed by three bytes of an incomplete operation; there are 111,611 complete operations and no empty-clause addition. Thus the saved stream is demonstrably truncated. This identifies a defect in the proof artifact, without by itself proving why the capture lost data or establishing the UNSAT conclusion. A separate candidate formed from the complete prefix plus a final empty-clause addition is being externally checked; it is not accepted merely because the solver said UNSAT.

That prefix-plus-empty candidate subsequently failed with `conflict claimed,
but not detected`. The accepted proof came from the separate corrected
capture described in the linked repair record, not from that candidate.

The original formula and raw proof have not been edited or regenerated.
The accepted recaptured proof is a separate artifact and passed the
independent checker before the status was promoted.

The original artifact alone did not certify UNSAT. The later complete
proof and successful independent check are linked at the top of this note.
The extracted core uses 420 original clauses and 215 RUP lemmas. The
subsequently supplied optimal 17-dimensional word changes the chronology
and is outside this fixed-bank obstruction; exact nu(17)=24,313 is now
independently verified.

Local files:

- [Reviewed generator/worker/replay script](decide_k17_unrestricted_triple_caps_cadical195_20260908.py).
- [Formula metadata](k17_unrestricted_triple_caps_20260908/formula_metadata.json).
- [Solver result](k17_unrestricted_triple_caps_20260908/solver_result.json).
- [Run decision report](k17_unrestricted_triple_caps_20260908/decision_report.json).
- [Raw binary DRAT stream](k17_unrestricted_triple_caps_20260908/solver_raw_proof.drat.bin).
- [Archive containing exact DIMACS, both mappings and solver artifacts](k17_unrestricted_triple_caps_20260908/exact_cnf_mappings_and_solver_artifacts.tar.gz).

The archive retains the unmodified files `unrestricted_triple_caps.cnf`, `cap_bits.jsonl`, and `witness_selectors.jsonl`. Mapping rows are respectively

`[variable, cycle, position, coordinate_bit_mask]`

and

`[variable, target_mask, cycle, cyclic_start, interval_length]`.

All original uncompressed artifacts are also retained at

`h100:/home/amodo/exact-b-k17-unrestricted-triple-caps-20260908/`.

The script contains a SAT extraction path and independent complete cyclic-target/range-OR replay, but those paths were not executed because the solver returned UNSAT. No SAT bank or new linear word is claimed. No solver process remains running.
