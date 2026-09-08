# Independent source review of the unrestricted triple-cap decision

2026-09-08. Read-only audit by `exact_b_induction` of the full script
`decide_k17_unrestricted_triple_caps_cadical195_20260908.py`, against
`PBBS_UNRESTRICTED_TRIPLE_CAPS_COMPLETE_CNF_AND_SPARSE_RUN_CLAUSES_20260908.md`,
also read in full. No generation, solver call, or mathematical execution
was performed by this reviewer. Verdict: **PASS**, with one suggested
explicit assertion noted below; no mathematical encoding defect found.

## 1. The exact architecture is preserved

The script reconstructs the H=min(height,3) source from the canonical
owners. Only optional coordinates at H3 positions receive cap variables.
Pins are constants true and coordinates outside the source are false.
Every cap variable is shared by all triples and all candidate witnesses
that use that physical position. No anchors, literal-rank6 reserves,
or old matching restrictions appear in this formula.

The frozen lower palette is computed from the actual H1/H2 words by
monotone cyclic OR scans. The rank cutoff is safe: after exceeding seven
the OR can never decrease. Its asserted1,887 distinct labels are all
rank seven. The remaining39,338 required targets are exactly the
nonempty rank-at-most-seven targets not in that palette.

## 2. Triple preservation and complete witness enumeration

For every cyclic H3 triple, the script processes each coordinate of its
original rank-eight OR. A pin present at any of the three positions
satisfies the clause. Otherwise it requires the available optional
variables and asserts that exactly three remain, as guaranteed by the
proved sparse-run equivalence. Thus neither a needed supply clause nor
a wraparound triple is omitted.

For every H3 cyclic start, intervals of lengths one and two are both
enumerated. Their pin union and source union are accumulated correctly.
Enumerating every submask of source union minus pin union lists every
eligible target exactly for that interval. The asserted631,992 host
incidences agree with the complete earlier host census, including
hosts of already fixed labels; those fixed-label selectors are simply
unnecessary and are not generated.

A selector implies both halves of exact equality: every optional source
coordinate outside the target is excluded from all positions of the
host, and every target coordinate is supplied at one of them. Positive
requirements already satisfied by a pin are correctly removed. Pins
can never be excluded because host eligibility includes all of them.
Each required target receives a nonempty OR of its selectors.

Reverse occurrence-to-selector implications and at-most-one restrictions
are correctly absent. Different overlapping witnesses remain allowed;
their compatibility is decided by the same shared cap bits and the
global triple clauses.

## 3. SAT extraction and independent literal checks

The model is decoded only into original physical cap coordinates;
retaining all pins makes every new letter nonempty. The script checks
subset containment and every literal native triple again. H1/H2 words
are copied unchanged.

The cyclic suffix scan processes a doubled period and retains only
suffix starts that give length at most that period. Collecting the
last v consecutive endpoint phases covers every possible cyclic
endpoint, hence all cyclic intervals of length at most v. Retaining
the latest start for an equal suffix OR is safe: it has the same OR
and remains eligible for at least as long as any earlier equal suffix.

The resulting distinct-target dictionary is required to have exactly
131,071 entries, each between1 and131,071. A separate range-OR segment
tree replays every saved interval. Thus a reported successful bank is
certified from its literal letters, not merely trusted from the solver
or its selectors. It is correctly labelled a cyclic BANK, not a
length-B(17) linear word.

Suggested hardening sent to the author before execution: add explicit
range checks in the independent replay itself, namely
0<=start<=end<2v and end-start+1<=v. These inequalities already follow
from the audited recurrence; checking them again makes cyclic witness
admissibility explicit in the independent replay layer.

The final source was inspected again after the author's changes: this
explicit per-cycle interval assertion is now present. The added source
SHA check, h100-host guard, worker proof-file size limit, and driver
memory-exhaustion handling also preserve the reviewed mathematical
encoding and result distinctions.

## 4. One-decision resource and result handling

The driver refuses an existing output directory, preventing silent
reuse of a previous model or solver result. One worker loads the
streamed DIMACS and makes exactly one CaDiCaL195 decision call with
seed zero. There is no solver restart loop.

The worker has its own hard CPU and address-space limits. Its budget
deducts generation CPU and reserves time for validation. After the
child exits, the driver tightens its own lifetime CPU limit using the
actual child CPU usage. Its global wall alarm and bounded worker wait
kill a still-running worker and record INCONCLUSIVE. A resource-killed
worker without a complete decision is not called UNSAT.

An UNSAT response is deliberately reported as solver-reported and
independently unchecked; retaining a native DRAT stream is not claimed
to verify that proof. A failed or incomplete solver/model validation
does not produce the successful-bank status. The scope distinguishes
an exact CNF equivalence, an unfinished bounded decision, an unchecked
solver assertion, and an independently validated positive literal
construction.

No execution outcome is asserted by this source-review note. This is
internal independent review, not external or proof-assistant
certification.
