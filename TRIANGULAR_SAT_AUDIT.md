# Independent audit of the triangular SAT certificates

## Verdict

The exact claim in `TRIANGULAR_NFA_SAT.md` is supported:

\[
                         \boxed{\rho(4)=2}.
\]

The audit found no soundness, completeness, clause-count, or reversal-symmetry
error in `scratch/triangular_nfa_sat.cpp`.  The independent
interval-selector encoding in `scratch/triangular_interval_sat.cpp` is also
sound and complete for the same spanning-word problem.

The computational certificate chain was reproduced as follows.

* All seven hashes in
  `scratch/certificates/TRIANGULAR_NFA_MANIFEST.sha256` match.
* Regenerating `R=4,n=12` from the current NFA source gives, after
  decompression, a byte-for-byte identical CNF.
* The regenerated formula has exactly `6762` variables and `121548` clauses,
  with maximum referenced variable `6762`.
* A fresh build of the official `drat-trim` checker independently accepts the
  stored DRAT proof and prints `s VERIFIED`.
* The complete stored `R=4,n=13` assignment satisfies every one of the
  `131324` clauses in a freshly regenerated formula.
* Decoding that assignment reproduces `tri_r4_n13.txt` exactly.  The generic
  interval analyzer independently finds all 30 targets and all 11 alphabet
  cells.
* As a second lower-bound check, the structurally different interval-selector
  CNF for `R=4,n=12` was regenerated and Kissat 4.0.4 returned UNSAT.

Consequently, length 12 is impossible and the displayed length-13 word is a
valid spanning word.  Since `|T_4|=11`, the minimum excess is exactly two.

No source file was modified during this audit.

## 1. Problem audited

The alphabet is

\[
 \mathcal T_R=\{(0,0)\}\cup
 \{(s,y):1\le s\le R,\ 0\le y<s\}.
\]

For every triple

\[
             z=(u,r,x),\qquad 0\le u<r\le R,\quad 0\le x<r,
\]

a witnessing interval must have

\[
 \min s=u,\qquad \max s=r,\qquad \max y=x,
 \qquad\text{and contain some cell with }y=0.
\]

There are

\[
 C=1+\frac{R(R+1)}2
 \quad\text{cells and}\quad
 T=\sum_{r=1}^R r^2
 \quad\text{targets}.
\]

The definition implemented by both SAT generators agrees with the independent
analyzer `scratch/analyze_triangular_word.cpp` and with the preceding
triangular-word notes.

## 2. NFA encoding

### 2.1 Allowed cells and provider bits

Fix `z=(u,r,x)`.  A cell `(s,y)` can occur in a witness exactly when

\[
                         u\le s\le r,\qquad y\le x.
\]

Among allowed cells, the four provider bits record

\[
 s=u,\qquad s=r,\qquad y=x,\qquad y=0.
\]

If every cell of an interval is allowed and the OR of these four-bit masks is
15, then all four required extrema are attained.  Conversely, every witness
has exactly these properties.  This establishes the local equivalence used by
both encodings.

### 2.2 Automaton soundness

The states are `0,...,15,done`.  A nonzero unfinished state `m` has the
invariant:

> some nonempty allowed suffix of the processed prefix has provider OR `m`.

State zero means that no suffix is currently retained.  On an allowed cell,
the three choices abandon, restart, or extend the retained suffix.  On a
forbidden cell an unfinished search is reset.  State 15 moves to `done`, and
`done` is absorbing.

The only apparent subtlety is that an allowed cell may itself have provider
mask zero.  In that case state zero remains state zero.  Discarding such a cell
cannot remove any required provider, so it cannot create a false accepting
trajectory.  For every state `m=1,...,15`, the suffix invariant follows
inductively.

Thus reaching state 15 produces one consecutive allowed suffix whose provider
OR is 15.  It is a genuine witness.  Acceptance in state `done` merely records
that such a suffix was found earlier.  This proves soundness.

### 2.3 Automaton completeness

Given a witnessing interval, stay at zero before it, restart at its first
nonzero-provider cell, and extend through its remaining cells.  Any leading
zero-provider cells may be discarded without changing the four providers.
The trajectory reaches 15 at the witness's right endpoint, then remains in
`done`.  If the witness ends at the final word position, final state 15 is
accepted directly.  Therefore every witness has an accepting trajectory.

### 2.4 CNF correspondence

Exactly-one clauses select one cell at every word position and one automaton
state for every target and time.  For the uniquely selected current state and
cell, exactly one transition implication is active, and it restricts the
uniquely selected next state to the automaton's transition relation.

Hence a satisfying assignment decodes to a word and one legal accepting path
per target.  Conversely, a spanning word plus one accepting path per target
satisfies all clauses.  Requiring every alphabet cell to occur makes the CNF
equivalent to the complete spanning-word problem, not merely target coverage.

The NFA encoding is therefore sound and complete.

## 3. Reversal symmetry

Reversing a word preserves alphabet coverage.  A witnessing interval
`[l,r]` is sent to `[n-1-r,n-1-l]`; it contains the same multiset of cells and
therefore has the same minima, maxima, and peak condition.

The final clauses prohibit precisely the endpoint pairs with

\[
                 \text{first cell index}>\text{last cell index}.
\]

For every word, either it or its reversal has first index at most last index.
Thus the restriction cannot remove the last solution.  The source emits one
clause for each ordered endpoint-value pair with `last < first`, namely
`binom(C,2)` clauses.  The implementation and the description agree.

## 4. NFA variable and clause counts

The variable count is

\[
                       nC+(n+1)T\cdot17.
\]

The clause families are:

\[
\begin{array}{c|c}
\text{family}&\text{count}\\ \hline
\text{one cell per position}&n\left(1+\binom C2\right)\\
\text{every cell occurs}&C\\
\text{one state per target/time}&T(n+1)\left(1+\binom{17}2\right)\\
\text{initial/final states}&2T\\
\text{transition implications}&Tn\,17C\\
\text{reversal orientation}&\binom C2.
\end{array}
\]

For `R=4`, `C=11` and `T=30`.  At `n=12` this gives

\[
 12\cdot11+13\cdot30\cdot17=6762
\]

variables and

\[
 12(1+55)+11+30\cdot13(1+136)+60
 +30\cdot12\cdot17\cdot11+55=121548
\]

clauses.  At `n=13` it gives `7283` variables and `131324` clauses.  The
headers, actual clause counts, and largest referenced variables all agree
with these values.

## 5. Independent interval-selector encoding

The second source uses one selector for every target and every physical
interval of length at least two.  Omitting singleton target witnesses is
safe: because every target has `u<r`, no single cell can simultaneously
attain first-coordinate minimum `u` and maximum `r`.

For a selected interval, one clause per position forces its cell to be
allowed, and four clauses force the four provider properties to occur
somewhere in the interval.  These conditions are exactly equivalent to the
target definition from Section 1.

The Sinz clauses correctly enforce at most one selected interval for each
target:

* `s_i` propagates whether an earlier selector has fired;
* a selector implies its prefix flag;
* no selector may fire after an earlier prefix flag;
* the final selector is treated by the terminal clause.

Together with the at-least-one clause, exactly one witness is selected.
This is stronger than existential selection but loses no word: choose any one
witness for each target.  Therefore the interval encoding is independently
sound and complete.

For `R=4,n=12`, it has 66 candidate intervals, 4062 variables, and 25068
clauses.  Direct enumeration of the generated DIMACS file confirms the header
counts and maximum variable.

## 6. Certificate reproduction

### 6.1 Manifest and formula identity

Running `shasum -a 256 -c TRIANGULAR_NFA_MANIFEST.sha256` from
`scratch/certificates` reports `OK` for all seven entries, including the
current generator source.

The stored CNF was decompressed and compared with a newly generated formula:

```text
new r4n12 CNF SHA-256:
89367430fbbc6a598bf6af32784e853e1d31daa7092f3202085287ab2aebf221
stored decompressed CNF SHA-256:
89367430fbbc6a598bf6af32784e853e1d31daa7092f3202085287ab2aebf221
cmp result: identical
```

This is stronger than agreement of the DIMACS header: the certified proof is
being checked against exactly the formula emitted by the audited source.

### 6.2 DRAT verification

A fresh checkout of the official `marijnheule/drat-trim` repository at commit

```text
2e3b2dc0ecf938addbd779d42877b6ed69d9a985
```

was built locally and run on the regenerated CNF and decompressed stored proof.
It returned exit code zero and:

```text
c parsing input formula with 6762 variables and 121548 clauses
c finished parsing
c detected empty clause; start verification via backward checking
c 49435 of 121548 clauses in core
c 85347 of 165099 lemmas in core using 3138468 resolution steps
c 25555 RAT lemmas in core; 14293 redundant literals in core lemmas
s VERIFIED
c verification time: 8.949 seconds
```

Thus the DRAT file is a valid refutation of the regenerated NFA CNF.  The
preserved `tri_r4_n12_proof.log` alone contains only the solver status and is
not a certificate; the independently checked DRAT file is the relevant
evidence.

As a separate corroboration, Kissat 4.0.4 solved the regenerated
interval-selector formula for `R=4,n=12` as UNSAT in 14.62 seconds.  This
second run is not needed for the theorem, but it checks the conclusion through
a different exact encoding.

### 6.3 Satisfying model and explicit word

The stored `R=4,n=13` model contains exactly 7283 assigned literals, one for
each variable, with no duplicate variable and no omission.  A generic DIMACS
assignment checker evaluated all 131324 clauses in a freshly regenerated CNF:

```text
clauses=131324 unsatisfied=0 referenced_unassigned_vars=0
```

The audited decoder reproduces `tri_r4_n13.txt` byte for byte.  Independently,
the exhaustive interval analyzer reports:

```text
SUMMARY missing=0 alphabet_valid=1 span=1 distinct_cells=11/11
```

The word is therefore a valid upper-bound certificate independently of the SAT
model and independently of the automaton proof.

## 7. Small-instance cross-checks

Fresh NFA and interval-selector formulas agree on the neighboring exact case:

\[
\begin{array}{c|c|c|c}
R&n&\text{NFA result}&\text{interval-selector result}\\ \hline
3&7&\mathrm{UNSAT}&\mathrm{UNSAT}\\
3&8&\mathrm{SAT}&\mathrm{SAT}\\
4&12&\text{certified }\mathrm{UNSAT}&\mathrm{UNSAT}\\
4&13&\mathrm{SAT}&\mathrm{SAT}.
\end{array}
\]

The `R=3,n=8` NFA model decodes to a word for which the independent analyzer
reports all 14 targets and all 7 cells.  A fresh `R=4,n=13` NFA solve also
returns SAT and decodes to a fully spanning word; the independently generated
interval-selector model does likewise.  These small checks exercise both
directions of both encodings without relying only on the stored `R=4` proof.

## 8. Scope and caveats

1. The theorem proves the exact auxiliary value `rho(4)=2`; it does not by
   itself solve an additional instance of the original universal-subarray-OR
   problem.
2. Both command-line programs assume meaningful nonnegative parameters and do
   not validate `R` and `n`.  The audited certificate calls use `R>=3,n>=7`, so
   this has no bearing on them.
3. Each `decode` routine is an extractor, not a SAT-model checker: it trusts the
   `s SATISFIABLE` marker and records positive literals.  The stored model was
   therefore checked separately against the entire CNF as described above.
4. `scratch/analyze_triangular_word.cpp` has an unconditional x86-specific
   target pragma and does not compile unchanged on Apple Silicon.  For this
   audit only, its input stream was compiled after filtering that single pragma;
   its analysis logic was not changed.  The two SAT generators already guard
   their x86 target pragmas correctly.
5. The older ledger in `TRIANGULAR_MIN_REPEATS_AUDIT.md` predates this proof and
   says that `rho(4)` minimality is unknown.  That statement is now stale.  The
   checked DRAT certificate justifies replacing it by `rho(4)=2` wherever the
   current theorem ledger is maintained.

Subject to these scope notes, no unsupported exact claim remains in
`TRIANGULAR_NFA_SAT.md`.
