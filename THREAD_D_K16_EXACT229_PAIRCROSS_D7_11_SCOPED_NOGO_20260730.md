# Exact229 distance-7--11 pair-cross cycle no-go

Date: 2026-07-30

Status: **proved scoped no-go**.  The chronology, Hall shore, source, and
completed H100 run are hash-frozen below.  This theorem closes one interacting
token-cycle class; it is not a no-go for jointly legal close collars.

## Frozen instance

The input chronology is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974
```

It has length 12,873, exact maximal-envelope reconstruction, no zero envelope,
and no arbitrary-width upper hole.  The exact generalized-COMP3 Hall audit is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.hall.k.audit.json
SHA 85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0
```

Its frozen alternating shore has

\[
             |U|=212,\qquad |N(U)|=187,\qquad \delta(U)=25.       \tag{1}
\]

Hence every compiler-feasible chronology must increase this fixed
neighbourhood by at least 25 cells.  Passing this one cut would still not
prove full Hall feasibility.

## Exact interaction identity

For a row replacement at position \(p\), every potentially changed COMP3
cell start lies in

\[
                         I_p=[p-5,p+6].                           \tag{2}
\]

The exact reconstruction neighbourhood is smaller,
\([p-3,p+3]\).  Thus individually legal replacements at positions separated
by at least seven remain jointly reconstruction-exact, while their Hall
profiles can interact at distances 7 through 11.

For an admitted directed replacement arc \(e\), let \(w(e)\) be its exact
change in \(|N(U)|\).  For two arcs put

\[
 \kappa(e,f)=\Delta_U(e,f)-w(e)-w(f).                             \tag{3}
\]

If all support positions have mutual distance at least seven, no cell start
belongs to three intervals (2): three ordered positions span at least 14,
whereas two intervals meet only when their centres differ by at most 11.
Cellwise inclusion--exclusion therefore gives the exact, not approximate,
identity

\[
 \Delta_U(C)=\sum_{e\in C}w(e)+
     \sum_{\substack{e<f\\7\le |p_e-p_f|\le11}}\kappa(e,f).       \tag{4}
\]

For at most eight support positions there are at most seven nonzero pair
slots.  This proves the safe DFS bound

\[
 s+(8-u)M_1+(7-a)M_2,                                            \tag{5}
\]

where \(u\) arcs and \(a\) interacting pairs have already been charged,
\(M_1=\max(0,\max w)=4\), and
\(M_2=\max(0,\max\kappa)\).  The closing arc is included in \(8-u\).

An independent source audit checked (2)--(5), old-token semantics for cycle
replacements, atlas indexing, canonical root rotation, and the harmless
contraction of equal-mask no-op arcs:

```text
scratch/threadD_k16_exact229_paircross_independent_source_audit_20260730.md
SHA f50ff01795663e8a3792adf8e0808a795fe3788244702e3c1b42d10c50130c39
```

## Complete scoped census

The quantified class is one directed token cycle on two through eight
positions, pairwise separated by at least seven.  Every constituent arc must
be individually legal on the frozen chronology.  The least support position
is the canonical root; inverse orientation is retained.

The exact catalogues are

```text
tested ordered replacements       165,701,250
locally legal arcs                     165,666
interacting position pairs              64,320
pair-correction entries             11,538,425
nonzero pair corrections                   840
correction histogram       -2:12, -1:711, 0:11,537,585, +1:117
```

Thus the interaction is genuine but sparse, and its maximum favourable
cross-term is only +1.  The threshold-safe DFS returned

```text
DFS states                         37,565,341
safe bound prunes                  33,025,594
closures reached after pruning         19,558
maximum reached closure current             6
closures with current at least 25            0
```

The 19,558 closures are the closures reached after the sound bound (5), not
all low-current legal cycles.  Since every pruned continuation has certified
upper bound below 25 and every reached closure has current at most 6, no cycle
in the quantified class can satisfy the necessary cut (1).  No full Hall call
is warranted.

The production source and completed result are

```text
scratch/threadD_k16_exact229_hall_paircross_cycle_census_20260730.cpp
  SHA 4982cee3f006575cc6efce57a906efd7913586cbb7f92a48b19a84d577c407eb

scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730/result.json
  SHA dccac35377f1891d4ea656235f575facd150d772952ba2124e28195a99fdc930

scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730/cycles.tsv
  SHA be4fdf107cb575cb528632aa8970e09574ca68ad7d55d5ab44559a350322760c
```

The positive-arc table is byte-identical to the independently audited
wide-12 table (SHA
`8d45283cf170713af419ed2cc86d206d32e5200c5098c64353633eea73486268`).
All staged hashes verify.  The run used one H100 CPU, no GPU, a 2 GiB address
space cap, 188.84 seconds wall time, 188.42 seconds user CPU, 21,000 KiB
maximum RSS, and no swap; it exited zero.  Timeout or resource failure would
have been `UNKNOWN`, but neither occurred.

A separate artifact/closure auditor verified all staged hashes, the checkpoint
transitions, the pair histogram, and every one of the 19,558 persisted closure
rows.  It independently recovered maximum score 6, no qualified row, and the
score histogram

```text
-3:5, -2:121, -1:688, 0:16268, 1:966,
2:911, 3:483, 4:91, 5:12, 6:13.
```

Its uniquely named source and certificate are

```text
scratch/audit_threadD_k16_exact229_paircross_d7_11_result_20260730.py
  SHA 37e344e348852f2b5c9a0e2ed47af343e67444ba4216e04703ff9c7fc4539a62
scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730/
  threadD_paircross_d7_11_solverfree_independent.audit.json
  SHA 59ff14424692c96628f030114b78652a3fed8e72f010b34993067bffc89f075d
```

An independent atlas-free C++ replay then applied every logged cycle to the
literal chronology, recomputed every affected shore cell and exact local
geometry equation, and found zero score mismatches and zero geometry
mismatches.  Its result is

```text
scratch/threadD_k16_exact229_hall_paircross_d7_11_20260730/
  independent_literal_replay/independent_literal_closure_replay.audit.json
  SHA 239ca016f4623002d98d1cf1b5e5d7601e173fa33c7e54dba3f040ac5d8eda78
```

That replay used one capped H100 CPU for 2.42 seconds and 6,268 KiB RSS.  It
does not rebuild the 11,538,425-entry atlas; mathematical completeness and
atlas indexing are the subject of the independently frozen source audit
above.  The full independent report is
`THREAD_D_K16_EXACT229_PAIRCROSS_D7_11_RESULT_AUDIT_20260730.md`, SHA
`35a95bbb35496a886a924964ede8beba81de58e8bfecb13a634e39aecba76d93`.

## Sharp surviving branch

This theorem does **not** cover:

- support positions at distance at most six;
- a close cluster whose replacements are legal only jointly, although one or
  more constituent arcs is illegal on the incumbent;
- multiple disjoint token cycles;
- cycles on more than eight positions; or
- block rethreads and other non-token topologies.

The next genuinely distinct repair class is therefore a jointly replayed
close collar (distance at most six), treated as one composite column before
any separated assembly.  Repeating individually legal wide or pair-cross
cycles cannot address that gate.
