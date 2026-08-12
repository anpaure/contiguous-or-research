# `k=17` V2 directed-history to rank-11/rank-12 upper CEGAR contract

Date: 2026-08-02  
Lane: R2  
Status: exact fail-closed theorem and integration contract; no new solve and no
SAT/UNSAT verdict.  Executable source and audit output are not frozen until an
independent literal replay succeeds.

## 0. Result

The rank-11/rank-12 target-automaton separator can be attached to the live V2
directed-history decoder with **zero new variables**.  Every uncovered target
orbit produces a positive frontier vector in existing directed-dart variables;
identical same-batch vectors share one physical clause, and an empty vector is
a fatal catalogue obstruction.  Each nonempty clause remains valid under an
arbitrary rethreading of the quotient cycle and does not freeze the incumbent
order.

The live boundary is important.  The frozen V2 decoder binary authenticates
the static 3,904,557-clause master only.  The currently searched v499, v526 and
v537 formulas have the same variables and the same static clause prefix, but
have additional authenticated suffixes.  A promoted decoder must therefore
take both `STATIC_MASTER.cnf` and `CANDIDATE.cnf`, prove exact clause-prefix
identity, and replay the complete SAT assignment against the candidate.  It
must not pass a strengthened candidate to the old static-only binary.

This contract proves only the cyclic rank-11/rank-12 owner-union deck inside
the fixed `Z_17`-equivariant marker58 catalogue.  Rank-13--17 regression,
opening/exterior windows, lower source, compiler and regeneration remain
separate fail-closed gates.

## 1. Authenticated parent schema and live candidates

The immutable directed-history schema is

| semantic class | exact variable interval |
|---|---:|
| residual option primaries | `1..35713` |
| remaining base variables | `35714..204167` |
| directed nonloop darts | `204168..276041` |
| depth-three history variables | `276042..348971` |

There are 71,874 directed darts: 464 orientations of 232 fixed marker edges
and 71,410 orientations of 35,705 residual nonloop options.  The other eight
residual options are quotient self-loops, have no dart variables, and are
killed by eight inherited negative primary units.  A dart-only upper audit
must first authenticate those units; otherwise its catalogue would not be
complete.

The immutable reconstruction inputs are

```text
c6638107ba4d1241403f914b5893614d9660a48cde7e43bef495b5fe28ebed52
  marker58_residence_round1.cnf
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  marker58_residence_round1.map.tsv
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf       (348971 variables, 3904557 clauses)
7827cb0c8b7925d5fca73f37d0cd6cbc8567eff51f6609ecca8b6681bf29a7fb
  marker58_directed_history.map.tsv
88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
  k17_marker_orbit.witness.tsv
```

The read-only strengthened/live inventory at the time of this contract was

| candidate | clauses | SHA-256 |
|---|---:|---|
| strengthened V2 | 3,904,720 | `8edea7e353343b420aa60c4d9fa2bb78fc9536c955af4ff0d7cb5a16718402c0` |
| v499 | 3,904,741 | `05787aa7b9676da8f76f9523f48609127781656e5aeb455b7fd01b71ed8765ce` |
| v526 | 3,904,768 | `79103e9a2e4ee30b214e91e7f4bf09a77cfe14c689bd1a88b73921e58484b2c0` |
| v537 | 3,904,779 | `be93c2b1b8af993c0e5ecab17f32880e2564c9481aa2a2b1d0a660789b77691c` |

Strengthened V2 is the exact static prefix plus 162 canonical residence rows
and the reversal-symmetry unit `204168`; its independent construction-audit
SHA-256 is
`707175eea147b4d239524a2a9c4effc639666495e803ab007ba96ba4f2880a50`.

These hashes identify snapshots, not a preferred solver lane.  A first SAT
incumbent is bound to the exact candidate hash it satisfies.  No suffix may be
silently transplanted between candidates.

The frozen decoder source/binary pair is not candidate-aware.  A local draft
adds a `decode-candidate-sat` path, but its source, binary and manifest do not
yet form an independently replayed triple.  It is therefore pre-freeze input,
not authenticated evidence.

## 2. Candidate-aware decoder precondition

For candidate `F_i`, the decoder performs these operations before upper
separation.

1. Reconstruct the marker58 option/dart/history schema from the immutable base
   CNF, base map, directed map and witness.
2. Parse `STATIC_MASTER.cnf` and `F_i` strictly.  Require 348,971 variables in
   both and at least 3,904,557 clauses in `F_i`.
3. Compare the first 3,904,557 clause vectors exactly.  The static file must
   end there.  Parse and retain every candidate suffix clause through EOF.
4. Count terminal-status lines and require exactly one recognized line, equal
   to `s SATISFIABLE`, plus exactly one signed assignment for every variable
   `1..348971`.  Reject missing, duplicate, contradictory and out-of-range
   assignments, every second terminal status (even an identical SAT line), and
   every unrecognized `s ...` line.
5. Replay every clause of `F_i` under that assignment.
6. Replay protected markers, all rank-eight facets, owner degrees, all
   rank-ten caps, dart/primary equivalence, indegree/outdegree one, all history
   equations, quotient components, component voltages, the physical lift and
   literal positive residence.

Hashing and parsing must be from one immutable snapshot (or must be protected
by before/after identity checks); separately reopening a mutable input is not
an authenticated binding.  Any failure above is a verifier failure, not a
CEGAR row.

Only a decoder output with one quotient component, nonzero voltage and no
positive run of length one, two or three is eligible for upper separation.
Running the upper scan earlier is allowed for diagnostics, but it cannot make
the incumbent acceptable.

## 3. Exact voltage and coordinate frame

Let `rho` be the one-bit left rotation of a 17-bit mask.  For a mask `S`, let
`rep(S)` be its minimum integer rotation and let `g(S)` be the unique fibre
satisfying

\[
                         S=\rho^{g(S)}\operatorname{rep}(S).
\]

For an exported dart `a:u->v` of voltage `delta_a`, the physical lift is

\[
 (u,g)\longrightarrow(v,g+\delta_a),\qquad
 \rho^gR_u\longrightarrow\rho^{g+\delta_a}R_v.          \tag{3.1}
\]

Thus the successor of physical owner `S=rho^g R_u` is reconstructed as

\[
                         S'=\rho^{g+\delta_a}R_v.         \tag{3.2}
\]

The directed map is authoritative.  In particular, the reverse row is not a
bare endpoint swap.  The independent V2 identities are

\[
 \delta_{\bar a}=-\delta_a,\qquad
 d_{\bar a}=b_a,\qquad b_{\bar a}=d_a                 \pmod {17},             \tag{3.3}
\]

where `d` is the deletion in the tail frame and `b` is the insertion in the
head frame.  Every row used by the separator is checked literally through

\[
 S\setminus S'=\{g+d_a\},\qquad
 S'\setminus S=\{g+\delta_a+b_a\}.                       \tag{3.4}
\]

For a physical target `W`, use its unique canonical representative

\[
                       Z=\min_{h\in Z_{17}}\rho^hW.       \tag{3.5}
\]

Every proper nonempty mask has orbit 17.  Rotating an entire physical witness
changes all fibres by the same gauge but changes neither its quotient dart IDs
nor its voltage differences.  Consequently one cut for `Z` is valid for all
17 physical targets in its orbit.  Darts are never rotated independently.

A selected quotient cycle of total voltage `V != 0 mod 17` develops to one
24,310-owner physical cycle.  Voltage zero develops to 17 cycles.  The upper
cuts themselves enforce neither connectivity nor nonzero voltage.

## 4. Complete target automata

Enumerate canonical target masks in increasing integer order.  The exact
census is 728 rank-11 targets and 364 rank-12 targets.

For target `Z`, a transient state is `(S,U)`, where `S` is the current physical
rank-nine owner, `U` is the owner union accumulated so far, and

\[
             S\subseteq U\subsetneq Z,\qquad |S|=9.      \tag{4.1}
\]

All states `(S,S)` are reachable from an unconditional source.  For every
catalogue dart whose source representative is `rep(S)`, reconstruct `S'` by
(3.2).  If `S'` is contained in `Z`, add the transition

\[
 (S,U)\longrightarrow
 \begin{cases}
   (S',U\cup S'),&U\cup S'\subsetneq Z,\\
   \text{sink},&U\cup S'=Z,
 \end{cases}                                             \tag{4.2}
\]

gated by the single existing dart variable `y_a`.

For rank 11, `|U|` is 9 or 10.  There are 55 start-owner states, 110
rank-ten-union states, source and sink: 167 nodes.  Every covered rank-11
target has an exact three-owner/two-dart subwitness.

For rank 12, `|U|` is 9, 10 or 11.  There are

\[
 {12\choose9}+{12\choose10}{10\choose9}
       +{12\choose11}{11\choose9}=1540                 \tag{4.3}
\]

transient states, plus source and sink.  Every covered target has a first-hit
witness of four through 56 owners, hence three through 55 darts.  The complete
automaton may contain cycles.  No four-owner-only restriction, incumbent
neighbourhood, provider cap or truncated path catalogue is proof-safe.

State numbering for replay is deterministic and zero-based: source is state 0;
transient states follow, sorted first by `U` and then by `S` (both as unsigned
17-bit integers); sink is the last state.  A changed state order is a changed
schema and gets a different schema hash.

The reachable-set digest uses a fixed-length bit vector in that state order:
state `j` is bit `(j mod 8)` of byte `floor(j/8)`, least-significant bit first,
and unused high bits of the last byte are zero.  SHA-256 is taken over those
raw bytes.  The canonical target-catalogue digest is over the UTF-8 stream
`rank<TAB>unsigned_mask<LF>` in rank-then-mask order, where both integers are
unsigned base-10 with no leading zeros.  Target ordinals are zero-based in that
order.

For a retained witness, initialize the FIFO queue with start states in state-ID
order and scan each state's conditional transitions in
`(dart_variable,target_state_id)` order.  The first predecessor assigned to a
state is immutable.  This tie rule does not change reachability, but makes the
exported witness byte-reproducible.

## 5. Zero-auxiliary DIMACS row

Let `y*` be the incumbent.  Starting from all unconditional source entries,
compute the exact set `R_Z` reachable through transitions whose dart literal
is true in `y*`.  If the sink is reachable, retain one predecessor path as the
literal witness for `Z` and emit no row.

If the sink is not reachable, form

\[
 H_Z(R_Z)=\{a:\text{a catalogue transition labelled }a
                    \text{ leaves }R_Z\}.                \tag{5.1}
\]

The exact DIMACS clause is

```text
a1 a2 ... at 0
```

where `a1<...<at` are the sorted distinct dart IDs in `H_Z(R_Z)`.  Required
checks are:

* every literal is positive and lies in `204168..276041`;
* every ID occurs exactly once in the authenticated directed map;
* reverse darts remain different literals;
* all conditional edges leaving `R_Z` are represented;
* no unconditional source edge leaves `R_Z`;
* every emitted literal is false in the incumbent; and
* repeated physical lifts and repeated automaton edges bearing the same dart
  ID are deduplicated.

No option primary, history bit, target bit, position bit, automaton-state bit
or flow bit is introduced.  Therefore

\[
 V_{i+1}=348971,\qquad C_{i+1}=C_i+N_i,                 \tag{5.2}
\]

where

\[
 N_i=N_i^{11/12}+N_i^{deep}.                            \tag{5.3}
\]

Here `N_i^(11/12)` is the number of novel frontier vectors and
`N_i^deep` is zero or one according as the rank-13--17 literal replay passes or
emits the factor no-good (8.1).  The two types cannot collide: frontier rows
are positive dart literals and (8.1) is a negative-primary row.  Thus the sum
in (5.3) is exact.

Every future source-to-sink path has a first edge leaving `R_Z`, and the gate
of that edge belongs to (5.1); hence the row is valid.  A true incumbent
frontier literal would make its head reachable, so the incumbent falsifies
the row.  This is the complete first-exit proof.

If `H_Z(R_Z)` is empty, the immutable catalogue has no provider for `Z`.
Return `SCOPED_EMPTY_FRONTIER_OBSTRUCTION` and retain the complete
reachable-shore certificate.  The current V2 DIMACS reader rejects an empty
clause, so this status is not yet a proof-checked CNF-UNSAT verdict and must not
be reported as one.  It may be promoted either after two independent complete
shore replays, explicitly as a catalogue-semantic obstruction, or after a
versioned reader appends the standard empty DIMACS row `0` and the resulting
formula receives a checked proof.

## 6. Canonicalization, deduplication and append transaction

The canonical identity of an upper row is its sorted literal vector.  No
subsumption is performed.  In particular, never project a dart to its
undirected primary: the opposite orientation is a different transition and a
different Boolean literal.

For parent indexing, sort signed literals numerically and remove repeated
copies; a clause containing both `x` and `-x` is tagged tautological and cannot
equal a non-tautological upper row.  This normalization is used only for exact
logical-row identity, never to rewrite the authenticated parent stream.

Within a target, repeated labels are removed.  Within a batch, identical rows
from different targets are written once and every target points to the same
row ID.  Before appending, canonicalize and index every clause of the candidate
parent, not only the retained upper-row bank.  If a missing target regenerates
any parent row, fail closed: a model that really satisfies its parent cannot
falsify a clause already in that parent.  Exact parent-chain replay separately
proves that every retained earlier upper row is present.

Use the byte string

```text
a1 a2 ... at 0\n
```

as the clause serialization and SHA-256 input.  Empty-frontier serialization,
if enabled by a new schema, is exactly `0\n`.

For every target, record at least

```text
iteration
rank
canonical_target_mask
target_ordinal
incumbent_model_sha256
reachable_state_count
reachable_bitset_sha256
raw_frontier_transition_count
unique_frontier_literal_count
canonical_clause_sha256
emitted_row_id                         (one-based, or 0 when not emitted)
disposition = covered | novel | same_batch_duplicate |
              scoped_empty_obstruction |
              fatal_parent_duplicate | verifier_failure
```

The batch manifest also records the static-master, parent-CNF, base-map,
directed-map, witness, decoder, separator-schema, model, target-catalogue,
rows, provenance and child-CNF hashes.

`PREFIX.upper.r11r12.rows.cnf` and `PREFIX.upper.deep.rows.cnf` are typed,
**headerless** provenance streams.  The former has `N_i^(11/12)` rows and the
latter has `N_i^deep` rows.  Their exact-vector union, sorted numerically and
deduplicated, is `PREFIX.upper.rows.cnf` with `N_i` rows; that combined stream
is the tail actually appended.  None of these fragments is itself a solver
input.  `CHILD.cnf` is the only full formula and has the header in (5.2).

The append transaction is:

1. require fresh, nonaliasing temporary and final paths, then open and
   authenticate one immutable parent snapshot;
2. sort all novel signed literal vectors in ordinary numeric lexicographic
   order, assign one-based global row IDs after the previous maximum ID, and
   write a temporary child whose header is `p cnf 348971 C_i+N_i`;
3. copy the parent clause body unchanged and append the novel canonical rows;
4. flush and close successfully;
5. independently parse the child, compare its first `C_i` clause vectors to
   the parent, compare its last `N_i` rows to the canonical bank, require EOF,
   and verify the header arithmetic; and
6. publish the child and manifest with a same-filesystem atomic no-clobber
   operation only after all hashes agree.

The parent cannot be a raw byte prefix because its header changes.  Exact
clause-vector prefix equality, parent hash, unchanged body hash and exact tail
replay together are the binding.

The raw body hash begins at the first byte after the unique `p cnf` header's
line feed and ends at EOF.  Inputs with a second header, an unterminated final
clause, a literal outside the declared variable range or non-comment trailing
tokens are rejected.  The authenticated parent body must end in LF; a missing
separator newline is rejected rather than repaired.  Output flush and close
failures are fatal, and an output path may not alias any authenticated input
path.

Upper outputs use a noncolliding namespace:
`PREFIX.upper.r11r12.rows.cnf`, `PREFIX.upper.r11r12.targets.tsv`,
`PREFIX.upper.r11r12.witnesses.tsv` and
`PREFIX.upper.r11r12.audit.json`, together with
`PREFIX.upper.deep.rows.cnf` and the combined `PREFIX.upper.rows.cnf`.  The
existing V2
`PREFIX.cuts.cnf/.cuts.tsv` names remain reserved for topology/voltage cuts.

## 7. Optional static auxiliary encoding

The live lazy contract has an empty upper-auxiliary interval.  For comparison
only, a complete static path-column encoding may allocate fresh variables
starting at `V_parent+1`.  For each target, take every **simple** source-to-sink
state path in the complete finite automaton; removing a repeated-state closed
subwalk proves that these columns preserve reachability even for rank 12.
Sort columns by
`(rank,target,path_length,ordered_state_IDs,ordered_transition_IDs)` and let
`z_(Z,P)` denote the AND of the deduplicated dart support `A(P)`.  Emit

```text
-z a 0                         for every a in A(P)
 z -a1 -a2 ... -ak 0
 z1 z2 ... zs 0                for every target Z
```

These rows say `z <-> AND(A(P))` and `OR_P z_(Z,P)`.  They are exact only for a
complete provider catalogue.  They require a new variable schema and a decoder
that expects the enlarged assignment.

If `Q` path variables are allocated, the exact header arithmetic is

\[
 V'=V_{parent}+Q,\qquad
 C'=C_{parent}+\sum_P(|A(P)|+1)+1092,                    \tag{7.1}
\]

where the last term is one coverage clause for each of the 728+364 targets;
an empty provider family for a target contributes the standard empty clause.

A bare recursive reachability-bit encoding is not an exact substitute for
rank 12: cyclic automaton SCCs can support each other without being reachable
from the source.  Such an eager encoding needs bounded time layers or genuine
flow machinery.  It is not part of V2.

## 8. Literal upper replay and all-width fallback

On the one physical owner cycle, replay coverage independently of the
automata:

* scan all 24,310 cyclic triples for rank 11;
* for rank 12, start at every owner and accumulate widths four through 56,
  stopping as soon as the union rank exceeds 12; and
* canonicalize every hit and compare the resulting 728/364 bitsets with
  automaton sink reachability target by target.

Any disagreement is a verifier failure and emits no row.

Ranks 13--17 must also be scanned before acceptance.  For each rank `r`, visit
all 24,310 starts in physical-cycle order and grow the cyclic interval one
owner at a time.  Record a target whenever the union first has rank `r`; for
`r<17`, stop that start as soon as the monotone union rank exceeds `r`.  For
`r=17`, stop on the first full-set union, or fail after one complete 24,310
owner lap.  Retain the lexicographically first `(start,width)` witness for each
canonical target.  Until complete compact separators for these ranks are
installed, a regression uses the exact
orientation-free factor no-good

\[
                       \bigvee_{p\in X^*}\neg p,          \tag{8.1}
\]

where `X*` is the incumbent set of 1,198 selected residual primaries.  Facet
exactness makes this exclude exactly that undirected factor; its two coherent
orientations have the same cyclic interval deck.  This fallback does not pin
any other factor's chronology.

The deep-row provenance records every missing rank-13--17 target, the sorted
1,198-primary support, incumbent model and factor hashes, exact signed row
serialization, canonical row SHA-256 and its global emitted row ID.  Multiple
deep holes share this one factor no-good.

Thus an R2 upper-clean status means rank 11 and 12 passed the complete
automata and ranks 13--17 passed literal replay.  It does not mean that a
future physical opening preserves every cyclic witness.

## 9. Iterative solve/decode/separate proof

For iteration `i`:

1. authenticate `F_i`, its complete parent/cut chain and every immutable map;
2. accept only a complete SAT assignment and replay every clause of `F_i`;
3. replay marker/resources, exact directed degree, histories, quotient
   topology, voltage and the developed physical cycle;
4. require exact depth-three positive residence;
5. run the literal upper scan and the complete target automata;
6. emit all novel rank-11/rank-12 frontier rows and any deeper-rank factor
   no-good, with exact-vector deduplication;
7. construct and independently replay `F_(i+1)`; and
8. solve only that authenticated child.

Every appended frontier row is valid by the first-exit lemma and every deeper
no-good excludes an upper-defective factor.  Hence no desired solution is
removed.  Every nonfatal separable integral incumbent falsifies at least one
retained new row, so the solve/cut process is finite over the fixed catalogue;
verifier failure and scoped empty-frontier obstruction terminate outside that
loop.

SAT of an intermediate formula is not an acceptance result.  Positive
acceptance requires one quotient cycle, nonzero voltage, exact physical
residence and literal rank-11--17 coverage, together with one replayable
witness per target.  UNSAT requires both a checked DRAT/LRAT proof against the
exact final CNF hash and independent regeneration of every appended semantic
row.  The proof checks the final formula; row regeneration proves the
strengthening was valid.

The currently live Kissat v526/v537 runs were launched without proof output.
Their exit code 20, if obtained, is only an exploratory UNSAT report and cannot
meet this contract.  A promoted SAT result still needs no proof, but it needs
the complete model and every semantic replay above.

For a terminal solver run, the manifest records solver binary and command,
input CNF, raw output, wrapper exit status, model or proof, checker binary and
checker output hashes.  SAT requires the solver's SAT exit convention plus the
complete replayed assignment.  UNSAT requires the solver's UNSAT exit
convention, a nonempty proof artifact and the independent checker's verified
exit/status, all bound to the same CNF hash.

## 10. Current Pareto calibration

The two requested nonresident controls are distinct and are bound to their
terminal models:

| control | terminal model SHA-256 | factor SHA-256 | short positive runs | physical holes `(r11,r12,r13+)` |
|---|---|---|---:|---:|
| residence-first `final2023` | `cc24d613ed5fa995a923a19d278424a3d2931c8ff3b61c6439ccbb6a3aa58149` | `273d650ca2341e3058e957a94f2fbc3bed6d6ac0b48f4642d6db86e73a0b4df5` | 2023 | `(1734,323,0)` |
| deep-first `final2057` | `948f14048c699005147d764247ffdb3d0c20668ebae5977cc18559ec4ff2abe6` | `da3fe5db3ba5fe61b1c854356e2c352a299307783eb15f7da2a51bddc5731659` | 2057 | `(1683,323,0)` |

The corresponding target-orbit holes are `(102,19)` and `(99,19)`.  Both
controls retain all 24,310 rank-eight resources, all 19,448 rank-ten caps,
all 3,944 protected edges, one quotient component and one physical component.
Their canonical voltages are respectively 5 and 16.  Neither satisfies the
directed-history residence formula, so neither is a SAT control for the new
decoder path and neither supplies live upper rows.  They calibrate only the
literal target census and the Pareto tradeoff.

Their scores in the canonical 554-row negative residence bank are respectively
116 and 120.  That bank has SHA-256
`b71c8c0b12700a28e058b9d17ef07f959495057aeae7868020d31dae66291771`.

The deep-first binding is specifically
`deep_primary2057_single/round001.model`, not the similarly named parent
model.

## 11. Promotion and scope

No executable separator, modified V2 decoder, generated row bank or audit JSON
is frozen by this document.  Promotion requires two independently implemented
replayers, not merely two executions of one binary, from authenticated inputs
that agree on target catalogues, reachable-state digests, canonical rows,
child clause stream and hashes.  Until then the code is pre-freeze even if it
compiles.

The exact scope is the fixed marker58 `Z_17` quotient catalogue, cyclic
rank-11/rank-12 owner-union witnesses and the fail-closed rank-13--17 replay
gate.  It does not prove a seam/opening, exterior cross-windows, lower source,
root/lower/head correlation, common-cap matching, terminal compiler,
regeneration, a contiguous-OR word or the final extremal value.
