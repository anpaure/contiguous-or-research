# R2 independent audit: round-02 visible-pair q1 proofs and fail-closed scope

Date: 2026-08-02  
Status: **PASS** for the 65 realizable distinct-base unions of the twelve
certified visible socket escapes.  The formulas audited here are
`RELAXED_Q1_ONLY`; no selected-rank-ten or connectivity clauses are used in
the UNSAT conclusion.

## 1. Exact face

The twelve escape moves give 66 formal unordered pairs.  The pair
`e08,e11` is not a simultaneous bank because both replace base 2251 cut
`12065` by different alternatives.  The exact partition is therefore

```text
formal pairs                         66
INCOMPATIBLE_SAME_BASE                1
realizable distinct-base banks       65
```

The canonical 66-row literal replay is

```text
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.tsv
  SHA-256 7b2edd1557f4fe94e6c88acdc362ffb18b88cd21f8bf6e03eb3699f5c89556b7
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.audit.json
  SHA-256 fe5fb127e9d405574f9e1b7da7f2cc7fcdb98794ce0a881e6497819099123b70
```

Root solver jobs compact away the incompatible formal face 62 and use job
ids `0..64`.  Thus root jobs 62--64 correspond to canonical formal faces
63--65.  Ledgers must be joined by the two complete move tuples, not by the
numeric pair field alone.

Every realizable bank has 3,805 rows, differs from the frozen round-02 bank
in exactly the stated two rows, and passes the literal simultaneous rebuild:

```text
zero_lower=zero_tail=zero_head=zero_coherent_orientation=zero_rank10=0.
```

This is a final-bank replay.  It does not union unary supports whose intact
counterpart block may disappear after the other recut.

## 2. Formula and proof authentication

Canonical remote root:

```text
/home/amodo/or15/work/root_k17_round02_two_escape_q1_20260801/tests
```

Frozen ledgers:

```text
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.q1_summary.tsv
  SHA-256 b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.drat_summary.tsv
  SHA-256 006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3
```

An independent hash pass recomputed all 65 bank hashes, all 65 exact CNF
hashes and all 65 retained-proof hashes from the remote files.  All 195
matched the two frozen ledgers; there were no missing, duplicate or extra
job ids.  The CNF dimensions range from

```text
891538 variables / 2416486 clauses
to
892259 variables / 2418469 clauses.
```

The retained proof family was then checked a second time, serially and
read-only, by

```text
/home/amodo/or15/drat-trim/drat-trim
  SHA-256 92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a
```

against each exact `pairNN.q1.cnf/pairNN.q1.drat` pair.  The result was

```text
checked=65  VERIFIED=65  failures=0
```

Backward cores range from 20 to 187 original clauses and from 10 to 86
lemmas.  This second pass did not regenerate formulas or proofs and did not
run a pricing/search loop.

Consequently every realizable union of two moves from the visible
twelve-row menu has no relaxed orientation-consistent q1 coloured cycle
cover.  This is the exact theorem frozen in
`MATH_THEOREM_THREAD_D_K17_ROUND02_VISIBLE_SOCKET_ESCAPE_PAIR_NOGO_20260801.md`.

## 3. Socket-role rank, topology and rank ten

The old `114930` fan is genuinely broken in every one of the 65 banks.  The
occurrence-labelled resource ledger is

```text
scratch/threadD_k17_mask114930_core_20260801/socket_escape_pairs.resource.tsv
  SHA-256 fa0ff09575729642913f9d0579f31a28e7493adbdce01a2415abf21a9a002b78
scratch/threadD_k17_mask114930_core_20260801/socket_escape_pairs.resource.audit.json
  SHA-256 da3fdd6d6ffacd198e91890c2993551f68a6f47d57eec47e1f0fb7852885e574
```

For the 34 compatible cross-side pairs it gives two new arms with distinct
colours and distinct outside physical socket occurrences.  For each of the
31 same-side pairs, either member's new arm pairs with a surviving old
`114930` arm at the opposite socket.  Hence the old two-socket resource
rank is two for every realizable bank.  This destroys only the old local
fan; the verified successor cores explain why complete q1 remains UNSAT.

Because all 65 q1-only formulas are UNSAT, there is no selected seam cover.
The fail-closed values are therefore

```text
component_topology = N/A_Q1_UNSAT
selected_rank10    = N/A_Q1_UNSAT
```

The raw `zero_rank10=0` row proves only that every missing internal rank-ten
target has a candidate provider.  It does not prove that one common q1
selection covers those targets.  Likewise no component count exists before
a q1 model is selected.  A future SAT branch must stream-check the CNF model,
replay one orientation/in/out/colour use per physical piece, decompose the
selected successor permutation, and recompute selected rank-ten
multiplicities.  The reusable semantic checker is

```text
scratch/verify_r2_k17_relaxed_q1_functional_hall_model_20260801.cpp
```

## 4. Fail-closed acceptance contract

A promoted case is accepted only after all applicable rows below pass.

1. Reconstruct the normalized bank from round-02 and require exactly two
   compatible move tuples; formal face 62 is `INCOMPATIBLE`, not UNSAT.
2. Rebuild the full occurrence-labelled atlas and require all five literal
   zero rows, exact piece/colour dimensions and the three physical
   projection matchings.
3. Bind the exact map-producing builder, bank SHA, formula mode and CNF SHA.
   `Q1_PLUS_R10` must never be substituted for `Q1_ONLY` in a q1 theorem.
4. For UNSAT, require a nonempty retained proof and an independent checker
   ending in `s VERIFIED`; solver stdout alone is `SOLVER_UNSAT`, not a
   certificate.
5. For SAT, require a complete clause-checked and semantically replayed
   model before computing socket rank, topology or selected upper rows.
6. Recompute physical socket roles from owner occurrences and ordered paths.
   Mutable piece numbers and owner-mask quotients are insufficient.
7. Mark topology and selected-rank-ten `N/A` on the UNSAT branch rather than
   silently claiming them.

This contract is fail-closed: absent maps, hashes, model/proof, checker
success, or literal rebuild data yields `UNRESOLVED`.

## 5. Sharp scope

The audit closes only the compatible pair menu drawn from the twelve
individually visible clean socket escapes.  It does not cover arbitrary
Hamming-two recuts, a visible arm plus a neutral rerouter, dirty-prefix
compensation, central-role pairs, palette--geometry cross activation, added
cuts, C6/C8 rethreads, exact assembled residence, ranks 11--17, component
joining, exterior windows, opening, or the terminal compiler.
