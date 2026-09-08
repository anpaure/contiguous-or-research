# Theorem AD-v5: fail-closed all-opening Benders with executable upper, DM, and common-cap branches

Date: 2026-08-02

## 1. Scope

This theorem extends the frozen v4 interface in
`MATH_THEOREM_AD_ALL_OPENING_PRIMARY_BENDERS_AND_DM_INTERFACE_20260802.md`.
V4 remains unchanged: it proves the source projection, determinant-primary
provenance, guarded-cut rule, and downstream interface.  V5 makes the
opening selector bank, all-upper classifier, exact Hall/DM export, and SAT
common-cap publication path executable.

The result is a fail-closed recourse theorem.  It does not assert that an
authenticated resident `k=17` factor exists, and it does not emit or prove a
`k=17` universal word.

## 2. Authenticated incumbent and openings

On the marker58 determinant face there are 35,713 semantic factor primaries,
exactly 1,198 of which are selected.  After the fixed rows and selected
option developments are authenticated, the physical factor is one simple
degree-two cycle with

\[
  W=24,310
\]

rank-nine owners.  Its recourse opening set is the set of all directed cuts

\[
  \Omega=\{(\epsilon,c):\epsilon\in\{0,1\},\ 0\le c<W\},
  \qquad |\Omega|=2W=48,620.
\]

The persistent identity of an opening is its directed physical endpoint
pair.  Array positions and selector integers are incumbent-local.

For every opening, v5 evaluates the stages in this strict order:

1. exact flat source;
2. every nonwrapping upper union;
3. the exact strict-lower P/U/M graph, matching, Hall shore, and DM data;
4. common-cap SAT replay and dual exhaustive word verification.

A later stage is never used to repair or reinterpret an earlier failure.

## 3. Concrete guarded selector extension

Let `A(x)` be the complete signed cube of all 35,713 incumbent primaries.
V5 introduces a guard `g` and one selector `a_omega` for each
`omega in Omega`.  Its extension enforces

\[
  g\Longleftrightarrow A(x),
\]

all `a_omega -> g`, a Sinz at-most-one bank, and

\[
  g\Longrightarrow \bigvee_{\omega\in\Omega}a_\omega.
\]

Consequently, away from the exact incumbent cube every local selector is
false, while on the incumbent cube exactly one selector is true.  This makes
each opening cut a genuine incumbent-guarded clause rather than an
unguarded factor exclusion.

For a source obstruction with authenticated path support `G_omega`, v5 may
emit

\[
  \neg a_\omega\ \vee\ \neg G_\omega.
\]

For an upper or Hall failure without a stronger host channel, the executable
fallback is

\[
  \neg a_\omega\ \vee\ \neg g.
\]

The selector extension and guarded clauses are portable to a persistent
master only after every selector is rebased through its stable directed
endpoint key and the complete guard/selector extension is imported.

The short selected-primary clause is valid only on the authenticated
exact-1,198 marker58 face.  The complete signed 35,713-primary no-good is the
unconditional incumbent fallback.

## 4. Executable upper branch

For an opened owner chronology `T_0,...,T_(W-1)` and depth `d`, v5 computes
the unique maximal flat antecedent

\[
  P_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i.
\]

Every source interval of length at least `d+1` is exactly its nonwrapping
consecutive-owner union.  Thus an upper target is present exactly when it is
the union of some consecutive nonwrapping owner block.  V5 constructs a
compact target classifier once, reconstructs the missing-upper count for
every directed cut, and materializes an exact witness core when a requested
opening reaches the upper branch.

An upper failure is terminal for that opening.  In the absence of an exact
persistent DFA/path activation channel, only the guarded full-incumbent cube
is exported.

## 5. Executable Hall and DM branch

For each strict-lower target `S` and short occurrence-labelled cell `C`, let
`U_C` be the union of its antecedent letters and let `M_C` contain the owner
bits whose entire maximal carrier is contained in `C`.  The exact candidate
predicate is

\[
  S\subseteq U_C,\qquad M_C\subseteq S,\qquad
  S\cap P_p\ne\varnothing\quad\text{for every }p\in C.
\]

V5 enumerates this literal graph and computes a maximum matching.  If `A`
is the canonical deficient target shore, `N(A)` its exact old neighborhood,
and

\[
  \delta=|A|-|N(A)|>0,
\]

the exported DM repair schema contains:

- every target in `A`;
- every cell in the exact complement of `N(A)`;
- the exact P/U/M candidate semantics for the associated `q` variables;
- the guarded prospective row

\[
  a_\omega\Longrightarrow
  \sum_{C\notin N(A)}q_{\omega,A,C}\ge\delta.
\]

This strong row is valid in a host master only when every `q` is linked iff
the displayed exact candidate disjunction.  One-way or optimistic activation
is insufficient.  Until that equivalence is installed, the executable cut
is the guarded full-incumbent cube.  Hall remains necessary only; it is not
a simultaneous common-cap certificate.

## 6. Executable SAT common-cap and publication branch

For a source-, upper-, and Hall-passing linear owner path, `path-control`
regenerates the common-cap CNF from the authenticated owners.  Publication
requires all of the following in one invocation:

1. the owner path and SAT model are regular files with distinct canonical
   pathnames;
2. their hashes are unchanged across the replay;
3. the SAT assignment is total;
4. every regenerated DIMACS clause is satisfied;
5. every selected provider has exact P/U/M semantics;
6. the decoded letters have the exact owner derivative;
7. a start-organized interval-OR scan covers all `2^k-1` nonempty masks;
8. an independently organized frontier scan covers the same universe.

Only after these checks does v5 install a word by a no-replace atomic path.
Existing output paths and canonical-path input/output aliases are rejected.

The independent common-cap verifier reconstructs the CNF byte-for-byte,
binds the CNF/model/word hashes, replays every clause and provider, rebuilds
the derivative, and repeats both exhaustive scans.

## 7. Fail-closed UNSAT boundary and terminal logic

The `UNSAT_PROOF` worklist token is intentionally nonauthoritative.  V5 maps
every such token to `COMMONCAP_UNKNOWN`; the diagnostic shell receipt does
not pin the CNF, proof, checker, and checker result through sealed
descriptors.  Therefore it cannot emit a common-cap cut, close an opening,
or authorize a global no-good.  The recorded field
`commoncap_unsat_verified` remains zero.

No authenticated `k=17` opening passed source and Hall in this freeze, so
the `UNSAT_PROOF -> COMMONCAP_UNKNOWN` worklist path was not dynamically
reached by a production factor replay.  Its status here is an implemented,
fail-closed code-path theorem and source audit, not an accepted UNSAT proof
or an executed UNSAT certificate control.

A global incumbent no-good is emitted only if every one of the 48,620
openings has a definitive terminal failure and no opening is pending or
unknown.  Any `DEEP_PENDING`, `COMMONCAP_UNKNOWN`, or unverified UNSAT claim
blocks that conclusion.  A word is reported only through the verified SAT
publication branch above.

## 8. Executed controls

### 8.1 `k=13` Hall-deficient control

The authenticated cycle has 3,432 directed openings, all source-passing.
The independent verifier reconstructs every compact upper count.  At root
`127 -> 4191`, the upper deck is complete, the exact lower graph has 4,095
targets and 5,154 cells, and the maximum matching is 3,984.  The canonical
shore has sizes 453 and 342, hence deficiency 111; the complement contains
4,812 exact DM `q` cells.  This executes the upper/Hall/DM branch, but it has
no determinant-primary or common-cap claim.

### 8.2 authenticated `k=15` SAT control

The linear path has complete upper deck, 16,383 strict-lower targets, 19,311
cells, 137,238 exact candidate incidences, and a perfect matching.  The exact
common-cap instance has 169,440 variables and 621,905 clauses.  Its total
model is replayed, the emitted word has the exact derivative, and both
exhaustive scans cover all 32,767 nonempty masks.  This executes the SAT and
publication branch; it is a linear chronology control, not cyclic residence
and not a `k=17` result.

### 8.3 `k=17` all-opening negative controls

For final2397, all 48,620 openings fail the source stage; the minimum
residual short-run count is 2,395 and the bounded source core has two runs,
eight edges, and six primaries.  V5 emits 48,620 guarded opening clauses,
the exact selector extension, and the global incumbent no-goods, but no word.

For clean1581, all 48,620 openings also fail the source stage; the minimum
residual is 1,579 and the source core is `[2,6,5]`.  This is a stronger
authenticated factor calibration but is explicitly nonresident.

Both controls use `sparse-control`; neither replays a complete combined-
master CNF.  No `k=17` opening reaches upper, Hall, or common-cap.  The
upper/Hall/DM and SAT publication branches are calibrated separately by the
`k=13` and `k=15` controls; the nonauthoritative UNSAT token path is not
dynamically calibrated.

## 9. Frozen implementation

The authoritative package is
`scratch/ad_k17_all_opening_benders_v5_20260802/`, whose `SHA256SUMS` has
SHA-256

```text
e118cf2d32b0a8422d2328e6b08ef7e3fb66bc7478cde4174f8b96e0022b5116
```

The principal v5 sources are:

```text
e85b9aa0b54a0856aa7d8171a1f535528ac988c0de4bed94594e5c610469ed9a  build_ad_k17_all_opening_benders_v5_20260802.cpp
1ff83d792a02d134698bbff7335d655fcbaac81f10096e2e90053c88e9c651d4  verify_ad_k17_all_opening_benders_v5_20260802.cpp
8f662a22c90d006833f2c98e1c7e7eeac9843255dd938097b0410c85647627b9  verify_ad_benders_v5_cycle_hall_control_20260802.cpp
7372d11f99e04a554b3c3838f0f87f4f2d62c1e136e727f3e7c2a819dfe0ccae  verify_ad_benders_v5_commoncap_sat_control_20260802.cpp
0bde69820a62277cf381bb1c076cba187e4cf0d5bb00def860caa88cdc73cc64  verify_ad_commoncap_unsat_receipt_v5_20260802.sh
```

The last script is deliberately labelled nonterminal and is not trusted by
the production executable.

## 10. Exact conclusion

V5 closes the executable mechanics requested by the v4 interface: every
opening is enumerated, local failures are guarded by concrete selectors,
upper and exact Hall/DM witnesses can be materialized, and a SAT common-cap
path can publish only after dual exhaustive verification.  It remains
fail-closed for unverified UNSAT claims and for incomplete resident search.

As of this freeze, no authenticated source-ready resident `k=17` model is
available, no `k=17` word has been emitted, and no conclusion about
`nu(17)=B(17)` follows.
