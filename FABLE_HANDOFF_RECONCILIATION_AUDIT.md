# Fable-to-handoff reconciliation audit

Date: 2026-07-22

## 1. Verdict

I audited the finalized mathematical artifacts attributable to the Claude/Fable general-case session and reconciled them against `MATHEMATICAL_HANDOFF.md`.

The short answer is:

- **The authoritative handoff contains every material theorem, correction, and retraction produced by the finalized Fable work.**
- **The handoff is internally consistent with the audited Fable results.** Later sections explicitly override the few exploratory claims that were false, overstated, or unaudited.
- **The raw Fable notebook is not itself self-consistent if read straight through.** It is a chronological research notebook: old claims remain in place under later warning labels and corrections. It must not be treated as a theorem ledger without those overrides.
- Four secondary facts are not stated explicitly in the handoff: two small finite all-long-max examples, a separately named local neighbor-exceedance lemma, an explicit closed form for a Markov-tail corollary, and a random-order corollary. None supplies the missing general theorem.
- The currently running “Quantitative Seam Alternative” task has no finalized artifact or public result yet, so it is correctly excluded from this mathematical inventory.

This file is an audit only. It does not change `MATHEMATICAL_HANDOFF.md`.

## 2. Source boundary and snapshot

### Included primary material

1. `fable_general_case/FABLE_GENERAL_CASE_WORK.md`, the direct durable notebook.
2. The finalized public assistant outputs in the productive Claude session JSONL, including all later correction/audit passes.
3. The dedicated independent audits:
   - `FABLE_PROVENANCE_AUDIT.md`
   - `FABLE_RUN_SPECTRUM_AUDIT.md`
   - `FABLE_INTERVAL_SUPPLY_AUDIT.md`
   - `FABLE_THEOREM_O_AUDIT.md`
   - `FABLE_TWO_CYCLE_AUDIT.md`
   - `fable_general_case/FABLE_SEAM_LEVEL_LAW_AUDIT.md`
4. The clean theorem notes that Fable either authored or imported and explicitly relied upon, listed in Section 8 below.
5. Finite machine outputs directly associated with the notebook, but only as finite evidence, never as general proof.

### Excluded as theorem sources

- Private/raw chain-of-thought was not treated as a mathematical source.
- In-progress tmux text was not treated as a result.
- `claude_fable_k14.log` contains only HTTP 402 failures and no mathematical output.
- Prompts and launcher scripts contain instructions, not results.
- A failed or interrupted API response was not treated as a theorem.

### Snapshot identifiers

At the final audit read:

- `MATHEMATICAL_HANDOFF.md`: SHA-256 `b62a585075c3365df8c290d9ada97944ff46d9d3a51338444c70fcf119b45c3d`.
- `fable_general_case/FABLE_GENERAL_CASE_WORK.md`: SHA-256 `11b95d8f873b7c5b83667a58a9de31f356ca1b98ba029c00a5886b8c1489954a`.
- Productive Claude session JSONL `5d106b46-3000-4132-9735-c4e3ac4b59ca.jsonl`: last audited state had 829 records and SHA-256 `cd9e35c74811870c2c821b3dea6b5b8dc100921510a5a1764c180ac203de4618`.

The provenance audit freezes the session at record 720. I also inspected finalized activity after that cutoff. It adds correction/readback work but no new theorem; therefore the mathematical ledger below remains complete.

## 3. Positive theorem inventory

The status column is the status after applying all later corrections, not the status at the first place a claim appeared.

| ID | Fable claim | Final status | Handoff location | Reconciliation |
|---|---|---|---|---|
| P1 | Theorem A: subcritical fixed-dimensional aggregation reduces the target to a suitable capped-box bound | Proved, with its stated fixed-parameter hypotheses | Section 125, items 495-497 | Integrated faithfully; no unconditional construction is inferred |
| P2 | Lemma B: fan-capped avoidance, `|S_h| <= sum min(w_i,h)+hD` | Proved | Section 122, items 485-487 | Integrated |
| P3 | Lemma B' / Mirsky refinement for a selected covered family | Proved | Section 122, items 485-487 | Integrated with the fan-capped theorem |
| P4 | C1/C2/C4 consequences inside the named nested, side-batched, and anti-mixing architectures | Proved only under those architecture hypotheses | Section 122, especially items 486-487 | Correctly scoped; not promoted to an unrestricted theorem |
| P5 | Theorem E: every required window contains a complete long run / universal peak-window phenomenon | Proved | Section 127, items 500-504 | Integrated |
| P6 | Corridor-packing consequence / Theorem K | Proved | Sections 127 and 131, items 502-504 and 516-519 | Integrated; handoff retains the constant-four gate as open |
| P7 | Local neighbor-exceedance observation used inside the old Theorem J argument | Proved as a local statement only | Implicit in Section 131's audit of the surviving local facts | Mathematically compatible, but not separately named in the handoff |
| P8 | Theorem I: corrected run-spectrum/capped-sum inequality | Proved in corrected form | Section 131, items 516-519 | Integrated; all invalid concentration consequences are separately retracted |
| P9 | Theorem L: uniform interval service, in the corrected combined-min form | Proved; not wholly superseded | Section 139, item 543 | Integrated with the audit-corrected scope |
| P10 | Theorem L' and Corollary S: two-sided service refinement and forced plateau-spectrum consequence | Proved with the boundary/removal qualifications | Section 139, item 543 | Integrated |
| P11 | Theorem M: assignment-free clipped window-cost/area law | Proved in corrected clipped form | Sections 137 and 139, items 535-537 and 543 | Integrated; obsolete clustering language is not retained |
| P12 | Theorem N / MASTER: assignment-free service inequality and weighted supply/count law | Proved | Section 137, items 535-537 | Integrated |
| P13 | Lemma G: free positions and caps | Proved | Section 139, item 543; used by Section 133 | Integrated |
| P14 | Labeled ride-capacity theorem built on Lemma G | Proved | Section 133, items 523-525 | Integrated |
| P15 | Gap-service theorem | Proved | Section 134 | Integrated |
| P16 | First-dangerous global service theorem | Proved | Section 135, items 529-531 | Integrated |
| P17 | Theorem O: threshold extension for each fixed `c` in its audited range | Proved after independent audit | Section 139, item 544 | Integrated; this overrides the notebook's stale “conjectural” label |
| P18 | Scalar survivor continuum obtained after combining the audited inequalities | Proved only as a scalar-feasibility statement | Section 139, item 546 | Integrated; handoff does not confuse scalar survival with realizable orders |
| P19 | Proposition Q: adjacent directed plateaux cannot have the same line letter | Proved | Section 139, item 547 | Integrated |
| P20 | Corrected restricted two-cycle theorem: one contiguous chain of mutually adjacent, sufficiently long plateaux is impossible in the cheap regime | Proved in this restricted form | Section 139, item 547 | Integrated; broader Theorem P is rejected |
| P21 | Theorem R: Markov tail for the window minima `q_i` | Proved | Sections 137 and 139; acknowledged again in Section 142, item 564 | Integrated in substance; exact closed form is not printed explicitly |
| P22 | Boundary-reservoir profile under explicit vanishing-seam hypotheses | Proved | Section 142, items 560-561 | Integrated, with hypotheses |
| P23 | Saturated-atom cross-line obstruction | Proved | Section 142, item 562 | Integrated |
| P24 | General boundary-seam inequality beyond atomic profiles | Proved | Section 143, items 565-567 | Integrated |
| P25 | Mixed-profile cross-line obstruction | Proved | Section 145, items 571-574 | Integrated |
| P26 | Positive-seam/cross-line coupling and static balanced survivor analysis | Proved in its stated static/profile sense | Section 148, items 583-587 | Integrated; not promoted to an ordering theorem |
| P27 | From the failed seam-level attempt: the local rising-end lemma and the high-level capacity lemma | Proved local lemmas | Section 152, item 602 | Integrated; the attempted global implication is explicitly rejected |

## 4. Finite computation inventory

These observations are useful evidence but are not general theorems.

| Artifact/result | Audited meaning | Handoff status |
|---|---|---|
| `test_fan_capped.py` | Falsification/sanity testing for Lemma B | No theorem depends on the script; proof is mathematical |
| `all_long_max_search.py` and `alm_a45.log` | Exact small search found all-long-max orders for `a=2,3`; the `a=4` run is inconclusive | Small examples are not explicitly recorded in the handoff |
| Early windmill examples | Motivation and finite geometry, not proof of a general classification | Correctly excluded from the theorem ledger |
| Live Quantitative Seam Alternative task | In progress; no finalized markdown result exists | Correctly absent |

The all-long-max examples are the clearest literal omission from the handoff, but they are only finite examples and do not change any bound or open gate.

## 5. Retractions and superseded claims

| ID | Original exploratory claim | Final status | Handoff location | Reconciliation |
|---|---|---|---|---|
| R1 | The corrected run-spectrum inequality forces pointwise concentration | Retracted | Section 131, items 516-519 | Explicitly rejected |
| R2 | The run lengths form a forced `(4/3)a` staircase/windmill distribution | Retracted | Section 131 | Explicitly rejected |
| R3 | Theorem J globally forces the old staircase geometry | Retracted; only a local neighbor fact survives | Section 131 | Explicitly rejected |
| R4 | Ride partition / transportation claims derived from that concentration | Retracted | Section 131 | Explicitly rejected |
| R5 | Theorem L is wholly superseded by first-dangerous service | False historical label | Section 139, item 543 | Corrected: L retains an independently useful parameter range |
| R6 | Theorem M may choose the “first complete plateau” with no clipping issue | Retracted/corrected | Sections 137 and 139 | Handoff uses the clipped form |
| R7 | Theorem O remains conjectural | Stale notebook label | Section 139, item 544 | Independent audit proves fixed-`c` theorem; handoff is correct |
| R8 | Lemma R: equality seams create no new run | False | Section 139, item 547 | Explicit countermechanism recorded; only cost-one correction is viable |
| R9 | Theorem P: arbitrary pure two-cycle dense chains die | Not proved | Section 139, item 547 | Handoff keeps only the restricted contiguous all-long theorem |
| R10 | P': all two-letter stretches die | Not certified | Sections 139 and 142, item 564 | Explicitly rejected for constant, span, and maxima-count gaps |
| R11 | P'': near-rotation / letter recurrence follows | Conjectural | Sections 139 and 142, item 564 | Explicitly rejected as a theorem |
| R12 | Windmill v3 criticality closes the scalar survivor | Heuristic | Section 142, item 564 | Explicitly classified as heuristic |
| R13 | The Markov tail alone yields a boundary reservoir with average cost `4a/3` | Unsupported gloss | Sections 139 and 142 | Handoff requires added spatial/seam hypotheses |
| R14 | A scalar survivor profile is itself a realizable order | False inference | Sections 142-148 | Handoff distinguishes scalar feasibility from physical ordering constraints |
| R15 | A first seam-level law proves the needed cross-line mass | Failed | Section 152, items 600-603 | Failure and precise gap are recorded |
| R16 | Pascal/windmill-style local pictures alone settle the general case | Unsupported | Sections 139-152 | Never promoted in the handoff |
| R17 | Random-order intuition supplies an unrestricted deterministic theorem | False inference | Section 122 and later audits | Handoff preserves the probabilistic statement only in its own scope |
| R18 | The two-cycle pattern is completely resolved | Stale notebook wording | Section 139, item 547 | Handoff records only the restricted theorem |
| R19 | Complete scalar inequalities through Theorem O already contradict all profiles | False | Section 139, item 546 | Handoff explicitly exhibits the survivor continuum |
| R20 | The failed seam argument supplied the Quantitative Seam Alternative | False | Section 152, item 603 | The alternative is stated as the next open target |

## 6. Open and conditional Fable claims

| Claim | Current status | Handoff treatment |
|---|---|---|
| Conjecture D / universal cheap cover | Open; later replaced as the main route by sharper dichotomies, but not disproved | Its role is absorbed into Sections 122-127 and the later constant-four gate |
| Constant-four corridor transition gate | Open | Section 127, item 504, and Section 131 |
| Unrestricted all-long-max classification | Open; only `a=2,3` finite examples | Not used as a theorem |
| General two-/three-letter recurrence and near-rotation forcing | Open/unsupported in the proposed form | Rejected in Sections 139 and 142 |
| Realization of the scalar survivor continuum | Open as an order problem | Sections 142-148 add obstructions but do not claim full closure |
| Quantitative Seam Alternative | Open and currently being investigated | Section 152, item 603 |
| General asymptotic constant-one construction | Open | Nothing in the Fable work changes the proved `sqrt(2)+o(1)` upper constant in the current handoff |

## 7. Exact substantive items not explicit in the handoff

The audit found no missing material theorem. It found four secondary facts that could be added for completeness:

1. **Finite all-long-max examples.** Exact searches find examples at `a=2` and `a=3`; the `a=4` log is inconclusive. This is evidence, not a theorem.
2. **Separately named local neighbor-exceedance lemma.** The handoff records that the global Theorem J inference fails and preserves the valid local ingredients in prose, but does not isolate this local observation under its own lemma number.
3. **Closed form of the Markov-tail corollary.** From the weighted-supply law,
   `#{i : q_i >= beta a} >= ((4-3 beta)/(2-beta)) a^2 - o(a^2)`
   in the audited parameter range. The handoff contains the ingredients and acknowledges the result, but not this exact displayed formula.
4. **Random-order corollary.** Combining the fixed-`c` service result at, for example, `c=6/5` with the run inequality yields `D=Omega(a^2)` with high probability for a random order. The handoff retains an earlier probabilistic `Omega(a^2/log a)` statement in Section 122, but not this sharper corollary.

None of these four items changes the general deterministic frontier, the exact finite-`k` ledger, or the missing seam theorem.

## 8. Related clean notes and their handoff destinations

The following are not contradictions or competing theories. They are cleaned-up theorem modules and subsequent strengthening layers:

| Note/audit family | Handoff destination |
|---|---|
| `SUBQUADRATIC_PRODUCT_AGGREGATION.md` and audit | Section 125 |
| `FAN_CAPPED_AVOIDANCE.md` and audit | Section 122 |
| `UNIVERSAL_CAPPED_RUN_COVER.md` and audit | Section 127 |
| `LABELED_RIDE_CAPACITY.md` and audit | Section 133 |
| `BRAID_GAP_SERVICE.md` and audit | Section 134 |
| `FIRST_DANGEROUS_GLOBAL_SERVICE.md` and audit | Sections 135 and 139 |
| `BOUNDARY_RESERVOIR_PROFILE.md` | Section 142, items 560-561 |
| `SATURATED_ATOM_CROSSLINE.md` | Section 142, item 562 |
| `GENERAL_BOUNDARY_RESERVOIR.md` | Section 143 |
| `MIXED_PROFILE_CROSSLINE.md` | Section 145 |
| `POSITIVE_SEAM_CROSSLINE_COUPLING.md` | Section 148 |
| `fable_general_case/FABLE_SEAM_LEVEL_LAW_AUDIT.md` | Section 152 |

There is no contradiction between the scalar survivor in Section 139 and the later obstructions. Section 139 says the scalar inequalities alone permit a continuum. Sections 142-145 exclude portions of that continuum after adding physical boundary/cross-line hypotheses. Section 148 still exhibits a static balanced positive-seam survivor, but explicitly does not claim that the profile is realizable by an order.

## 9. Residual inconsistencies inside the raw Fable notebook

These are notebook-history problems, not handoff inconsistencies:

1. The top ledger and Section 12.1 still call Theorem O conjectural/open, despite the later independent audit proving the fixed-`c` version.
2. An older heading calls Theorem L “SUPERSEDED”; the later authoritative correction restores it in the range where it remains stronger or unique.
3. Section 12.1 contains an incorrect displayed polynomial in one profile calculation. The corrected polynomial is
   `2c^2 - (23/3)c + 20/3`,
   with roots `4/3` and `5/2`; the qualitative conclusion used later survives.
4. P, P', P'', near-rotation, and windmill-v3 prose remains in the notebook, but is surrounded by explicit “false,” “not certified,” or “heuristic” warnings.
5. Early Theorem M language about first-complete selection and clustering is stale relative to the corrected clipped theorem.
6. Section 11.4's suggestion that “2-cycles are resolved” is too broad; only the restricted all-long contiguous theorem is certified.
7. `FABLE_PROVENANCE_AUDIT.md` ends at session record 720, while the productive session later reached record 829. The later finalized outputs add correction/readback activity but no new theorem.

Therefore a model should read the notebook chronologically only for discovery. For citation and continuation, it should use `MATHEMATICAL_HANDOFF.md` plus the dedicated audit files.

## 10. Final reconciliation

The mathematical work is self-consistent after applying provenance order:

1. clean theorem note or finalized notebook claim;
2. independent audit/correction, when present;
3. `MATHEMATICAL_HANDOFF.md` as the authoritative integrated ledger.

On that ordering, no proved Fable theorem contradicts the handoff, and no material proved theorem is absent. The principal unresolved mathematical bottleneck remains exactly the one the handoff states: convert the surviving scalar/profile mass into a quantitative, position-sensitive seam/cross-line obstruction strong enough to force quadratic excess, or else construct a genuine surviving order. The current Fable continuation is aimed at that Quantitative Seam Alternative, but it has not yet finalized a result.
