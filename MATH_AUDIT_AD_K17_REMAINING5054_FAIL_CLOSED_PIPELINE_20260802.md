# Independent audit of the K17 remaining-5054 fail-closed pipeline

Date: 2026-08-02  
Audit lane: independent subagent replay, transcribed after source freeze  
Verdict: PASS for the stated pure-recut/post-SAT scope, with two explicitly
unexercised positive branches.

## 1. Frozen sources

```text
f3d623b4f150fdeb3d73725a99612e67a86931cbbd439c008a44bde77e111c28  scratch/verify_ad_k17_q1_dimacs_model_20260802.cpp
7cdd4e0a31df093e211924d74fc5e3331d24bab7b38ea6ff88fec02c413f062c  scratch/materialize_ad_k17_q1_model_chronology_20260802.cpp
ba423074976a3adfb6ae9369838f0caacf4625fa6e01045763becacc55e91379  scratch/audit_ad_k17_q1_survivor_full_guards_20260802.cpp
2204867aa416fe9c46cc47df734e7ccd48a6dc31b1ca18438e5399272f51b432  scratch/run_ad_k17_q1_survivor_full_guard_pipeline_20260802.sh
4e82d78323e2b8154aa260a78c36b741c61365f55d889e87f8a9ea0c221a1e2a  scratch/build_ad_k17_remaining5054_crossdeck_prefilter_20260802.py
e54cb26ec6a97ac13cb3861cd3f5959ce7dd1a7952bf1a3b0529fcb508741e0f  scratch/verify_ad_k17_bank_in_remaining5054_20260802.py
```

## 2. Inventory and prefilter replay

The audit independently recounted 169,426 clean banks, 164,323 persistent-core
rejections and 5,103 rebuild rows.  Removing the separately certified 49
dirty-central q1-UNSAT rows leaves exactly 5,054 rows on anchors 0 through 12,
with the displayed per-anchor profile in the theorem note.  Job IDs and bank
keys are injective.

Every one of the 5,054 rows was checked against the frozen round02 bank and
candidate catalogue: both old cuts are selected, both new cuts are unselected,
old and new cuts have the named base, the bases are distinct, and both moves
are genuine.  The independent ray-product replay agrees with maximum total
48 over ranks 11 through 17 and rankwise maxima

```text
4,6,7,9,11,11,1.
```

This was audited as a casualty **superset**, not a final-hole set.  The choice
to make no general hard rejection is correct.

## 3. Decoder and guard audit

The final materializer regenerates factor traversal in the same occurrence
order as the q1 builder, checks the complete 20,477-row candidate catalogue,
rebuilds 7,612 pieces, regenerates every relaxed seam row, and checks the full
successor permutation.  Its literal owner, Johnson, lower-q1, upper-q1 and
protected-incidence tests are sufficient for the chronology it emits.

The audit found and the final sources correct all of the following earlier
hazards:

1. Standard Kissat models wrap across many `v` lines and use one final zero;
   requiring a zero on every line was wrong.
2. Numeric stream extraction could silently ignore trailing nonnumeric data;
   model and CNF tokens are now parsed strictly.
3. Negating `LLONG_MIN` before a range test could overflow in standalone use;
   the range check now precedes negation.
4. A disconnected resident factor could previously receive the retained-deck
   partial PASS under Hamilton policy; topology is now tested before either
   positive status.
5. Protected incidences were checked only between base/current factors; the
   emitted chronology now explicitly contains every frozen protected
   incidence.
6. A conforming but unrelated 3,805-cut bank could enter the generic decoder;
   the frozen runner now proves exact membership in one unique 5,054 row
   before CNF replay.

The full guard correctly recomputes the complete physical edge difference
`A`, rather than trusting the declared two-recut support, and verifies the
maskwise cross-deck inclusion.  It correctly separates retained-old coverage
from zero actual holes at ranks 11 through 17.

Physical connectivity is the definitive topology certificate on this
non-equivariant face.  The code does not invent a voltage: it reports not
applicable unless the complete physical edge set is exactly Z17-invariant.
Only on that face does it construct the quotient multigraph and verify the
`sum gcd(17,v)` lift-count identity.

## 4. Regression and exact remaining caveat

Toy total/multiline SAT replay passes; false assignments and garbage tokens
fail.  Job 14 passes exact 5,054 membership.  The authenticated round02 UNSAT
output cannot emit a chronology.  Baseline and protected-C6 controls reproduce
the frozen component, run and upper-hole counts.

There is no authentic q1-SAT survivor in the shared 5,054 artifacts, so the
positive K17 materialization branch has no end-to-end positive regression.
There is also no invariant physical fixture exercising the numeric Z17 voltage
branch.  These are regression gaps, not proved counterexamples or logical
shortcuts.  The runner's exact scope is the frozen pure-recut face
`BASE_FACTOR == CURRENT_FACTOR`; it does not claim the same reference ledger
for a factor-changing C6/C8 move.

No q1 solve, compiler/common-cap proof, source-word construction or final
contiguous-OR theorem is contained in this audit.
