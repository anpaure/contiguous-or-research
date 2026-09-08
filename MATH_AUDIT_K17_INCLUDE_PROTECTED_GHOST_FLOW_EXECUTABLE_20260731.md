# Executable audit for the K17 include-protected ghost flow

Date: 2026-07-31

## 1. Scope

The executable

`scratch/threadD_audit_k17_include_protected_ghost_flow_20260731.py`

implements exactly the contracted flow of Theorem 2.1 in
`MATH_THEOREM_K17_INCLUDE_PROTECTED_RESIDUAL_BFLOW_20260731.md` for a fixed
persisted seam candidate.  It does **not** invoke the older balanced-factor
flow.

The forced physical bank is the set-OR of the selected seam edges and the
selected protected source edges.  Consequently:

1. a selected seam/source-colour conflict with a selected protected edge is
   rejected at the local bank gate;
2. the old source edge of an unprotected seam colour is not frozen and is
   automatically ejected from every completion branch.

The source factor, candidate payload, component hash, canonical seam cuts,
protected tails, witness references, owner degrees, and colour multiplicities
are replayed before any flow is run.

For the fully coupled face, `--require-banked-q1` additionally replays one
exported old-edge or selected-seam designation for every one of the
\(\binom{17}{10}=19{,}448\) rank-ten targets.  An old designation must be a
literal source-edge union and its tail must occur in the protected bank; a
seam designation must be selected and have the advertised union.  Thus a
later ejection cannot silently destroy the eager \(q_1\) certificate.

## 2. Exact branch model

For an allowed omitted lower colour (z), the executable removes the fixed
bank colours and (z) from the real right shore, adds one demand-two boundary
dummy, and solves the integral network

\[
s\longrightarrow V\longrightarrow
  \bigl((\mathcal C\setminus(C_K\cup\{z\}))\cup\{\partial\}\bigr)
  \longrightarrow t.
\]

The owner capacities are (2-\deg_K(v)); every real colour and the dummy have
demand two; every incidence has capacity one.  The executable verifies the
total-demand identity before accepting the backend result.

On failure it persists the exact minimum-cut sets (X,Y), whether
\(\partial\in Y\), all three terms in

\[
d_K(X)\le 2|Y|+|D_z\cap(X\times(L_z\setminus Y))|,
\]

and independently checks that the Hall surplus equals both the max-flow
deficit and the replayed cut-capacity deficit.

On saturation it persists the two boundary owners, all selected residual
incidences, all projected Johnson edges, and the exact path/cycle
decomposition.  A branch with cycles is labelled `ONE_PATH_PLUS_CYCLES`, not
as a Hamilton-path certificate.  A cycle already contained in the forced bank
is reported before flow as a genuine topology obstruction requiring at least
one bank-edge release from that cycle.

Direction, residence, arbitrary-width upper coverage, and the compiler remain
outside this executable.

## 3. Exact directed-topology lift

The separate executable

`scratch/threadD_audit_k17_include_protected_hamilton_recourse_20260731.py`

implements the exact directed topology lift for one explicitly chosen omitted
colour.  It first invokes the same fail-closed bank reconstruction with the
full banked-\(q_1\) requirement.  It then introduces both orientations of
every residual Johnson edge, one boundary dummy, and one `AddCircuit` row on
the \(24{,}310\) owners plus that dummy.  Every bank arc is fixed true, every
nonomitted lower colour is selected exactly once, and the omitted colour is
absent.  Since there are no self-loops, a satisfying circuit is exactly a
directed Hamilton path through all physical owners.

The emitted path is replayed without the solver: owner uniqueness, Johnson
adjacency, fixed directed bank containment, exact nonomitted lower colours,
unprotected old-source ejections, and every arbitrary-width linear upper
interval union are recomputed.  A resource-limited CP-SAT result is labelled
`UNKNOWN_RESOURCE_LIMIT_OR_SEARCH_INCOMPLETE`; only a completed branch may be
called SAT or scoped UNSAT.  Residence and the lower compiler below rank eight
remain downstream gates.

## 4. Quantifier and resource statuses

The command accepts explicit omitted colours, an explicit colour file, an
ascending `--scan-until-pass`, or `--scan-all-allowed`.  `--max-branches` is a
resource cap.  Exhaustion under that cap is labelled
`INCOMPLETE_RESOURCE_CAPPED_NO_PASS`, never UNSAT.  The global status
`INFEASIBLE_ALL_ALLOWED_OMITTED_COLOURS` is emitted only after every allowed
colour branch has an optimal failed max-flow certificate.

With `--branch-dir`, each complete branch certificate is written separately
and bound into the main audit by both file SHA-256 and stable payload SHA-256.

## 5. Regressions

The dependency-free test

`scratch/test_threadD_k17_include_protected_ghost_flow_20260731.py`

substitutes a tiny exact Edmonds--Karp backend.  It checks a passing boundary
path, an infeasible branch whose replayed Hall surplus is two, and a forced
cycle.  It prints

`PASS tiny contracted flow, exact min-cut, and forced-cycle regression`.

The solver-free directed replay test

`scratch/test_threadD_k17_include_protected_hamilton_recourse_20260731.py`

checks an exact three-owner path, fixed-bank retention, the omitted-colour
ledger, one unprotected ejection, arbitrary-width upper coverage, and rejection
of the reversed path.  It prints

`PASS tiny directed path, fixed-bank, lower-colour, and upper replay regression`.

The older unguarded active2649 candidate was replayed only through the local
bank gate.  The frozen audit is

`scratch/threadD_k17_ghostflow_old2649_local_gate.audit.json`.

It certifies:

* 2,908 selected seams and 11,793 selected protected source tails;
* 14,701 distinct physical bank edges after reason-OR;
* zero repeated seam colours but 1,142 selected seam/protected-source colour
  conflicts;
* one forced bank cycle of length nine;
* status `INFEASIBLE_LOCAL_BANK_GATE`, with no flow branch attempted.

This is only a regression against the known rejected candidate.  It says
nothing about the subsequently guarded active2649 run.

## 6. Frozen hashes

At this audit:

* contracted-flow executable SHA-256:
  `6bc120526a5c366d9a8f775109fbd9357c8430ba7b1adbf4e9d1a0803f0e48b3`;
* tiny test SHA-256:
  `d166acd05afe90973a6b1156999520a68e5e4c4fc32e94580dde6f0c55314ce8`;
* directed-Hamilton executable SHA-256:
  `37350ea88c331dd27c7a81e87c9dc1368a319d43d82bcbfc56124589c53e10be`;
* directed replay test SHA-256:
  `46b8eaf038009aa788f4738f8fa865f139d68450741263fa327d491216cfe47b`;
* old-active2649 directed local-gate audit SHA-256:
  `19aba38cf51201dfc58d58e0a0d7539775eff598e7cbba10b10ca214bd869b4c`;
  payload SHA-256
  `52e20c941df43342881c54182134ff4892bcbafea95df5cbc6971c741548f2f4`;
* old-active2649 local-gate audit SHA-256:
  `9b549b1a2c19ce9b9792ee64f88150f04425f05ea00058c7c0e2a5ef243ae029`;
* old-active2649 local-gate payload SHA-256:
  `8fe34c493641bc4ac246788ff0c8276049c0b7d5b019a515ed2859401401ff30`.

The production invocation on H100 is of the form

```sh
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_audit_k17_include_protected_ghost_flow_20260731.py \
  --components SOURCE.components \
  --candidate GUARDED.candidate.json \
  --require-banked-q1 \
  --scan-until-pass \
  --branch-dir BRANCH_CERTIFICATES \
  --output AUDIT.json
```

No result is inferred if OR-Tools is unavailable; that case is explicitly
`UNKNOWN_BACKEND_UNAVAILABLE`.
