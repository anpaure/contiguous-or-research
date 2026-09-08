# Exact Hall obstruction to the frozen-pair cap construction

2026-09-08. Bounded exact computation and proof-scope note by
`exact_b_induction`. Both prescribed instances are settled. A separate
certificate replay verifies the first optimum without rerunning a flow
algorithm. All mathematical execution was on h100; no heuristic frames,
random choices, or additional optimization instances were used.

## 1. Source and the two specified decisions

The source is the unchanged 146-component canonical PBBS bank in
`k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json`, with
24,310 total period positions. Its SHA-256 is

    fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3

We apply the proved reduction in
`PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md`,
which was read in full. Indexing is exactly the stored canonical cycle
and zero-based cyclic position. Put

    X_i = complement of stored lower owner,
    H = min(original height,3),
    D_i = X_i intersect ... intersect X_(i+H),
    Pin_i = (X_i minus X_(i-1)) union (X_(i+H) minus X_(i+H+1)).

The execution independently checked that the pin formula equals the
union of all indispensable-coordinate deficits in affected owner
windows, and that each original owner window has its asserted OR.

Height-one and height-two components are frozen. The H=3 bank has
22,134 positions. Every original letter there has rank6, and all 12,376
rank6 targets occur. The demand is all 9,401 targets of ranks1 through5.
An eligible position for target S satisfies Pin_i subset S subset D_i.

In each network, the layers are source, target, physical position,
original-rank6-label group, sink. The first three forward edge types
have capacity1. A group containing n_T original occurrences and e_T
editable occurrences has capacity e_T when some occurrence is an anchor,
and e_T-1 otherwise. Thus every rank6 label retains a literal occurrence.

The two prescribed results are:

| Instance | Editable positions | Sum of group capacities | Exact result |
|---|---:|---:|---:|
| Unrestricted H3 positions | 22,134 | 9,758 | Maximum assignment 8,245 |
| Canonical alternating frame | 11,009 | 7,013 | At most 7,013 assignments |

The unrestricted graph has 364,650 target-position edges. Every target
has at least one eligible position. Its failure is simultaneous and
capacitated, not an absent individual host.

For the second instance, each odd cycle of period v has editable indices
0,2,...,v-3. Everything else is an anchor. Exactly 8,380 rank6 labels
already have an anchor. The scalar capacity is 7,013, smaller than 9,401
by 2,388, so the requested stopping rule applies: no second max-flow
was run. This is an upper bound, not a claim that 7,013 is attainable
in that smaller network.

## 2. A checkable Hall certificate, not just a solver answer

For a family F of small targets, let N_T(F) denote the eligible physical
positions whose original label is T. In the unrestricted network,
every assignment of F uses at most

    sum_T min(|N_T(F)|, n_T-1)

positions. The saved Hall family has exactly 1,768 targets:

* 17 of rank 3;
* 238 of rank 4;
* 1,513 of rank 5.

Its entire eligible-neighbor set has 6,256 positions in 5,661 label
groups. Of those groups, 5,066 have only one original occurrence and
therefore zero permissible edits. The remaining usable capacities are
578 groups contributing one each and 17 groups contributing two each.
Thus the exact Hall capacity is

    578 + 2*17 = 612,

and the deficit is

    1768 - 612 = 1156.

Consequently at most

    9401 - 1156 = 8245

distinct small targets can be assigned in this network. The integral
flow supplies a feasible matching of exactly 8,245 targets to different
positions, with every group reserve respected. This independently
certifies that **8,245 is the exact network optimum**.

The complete target masks, eligible physical positions, and per-label
capacity contributions are in
`k17_capped_low_flows_20260908/unrestricted_hall_cut_certificate.json`.
Its group columns are rank6 mask, neighbor count, group capacity,
usable capacity. The matching in `unrestricted_assignment.json` has
columns target mask, cycle, cyclic position, original rank6 mask, pin
mask. It certifies a feasible assignment only; it is not asserted to
be a simultaneously owner-preserving cap.

The initial decision program also checked a residual minimum cut of
capacity 8,245. The separate replay does not use residual reachability,
Dinic's algorithm, or the submask edge generator: it tests each of the
1,768 Hall targets directly against every physical H3 position, computes
the neighbor capacities, and separately checks all 8,245 matching rows.
Both upper and lower certificates passed.

## 3. A broader exact obstruction that follows from this certificate

Keep H1/H2 frozen. There is no cap of this canonical bank that both
covers all nonempty targets and preserves every original H3 pair OR.
This is stronger than failure of the one prescribed alternating frame.

Indeed, every preserved H3 pair has rank7. Any interval of length at
least two in an H3 component therefore has rank at least7. Frozen
H1/H2 letters have ranks8 and7, respectively. Hence every target of
rank at most6 must be realized as one literal H3 letter. A rank6 target
can remain as a cap of an original rank6 letter only when the original
letter already equals that target, so at least one occurrence of each
rank6 label must remain unchanged. Moreover pair preservation implies
preservation of all longer owner windows, and therefore every cap must
contain its Pin_i. Choosing one literal witness for each distinct target
of ranks1 through5 would give a saturated assignment in the unrestricted
network. The certified maximum 8,245 contradicts the required 9,401.

The obstruction applies to this fixed source bank, with H1/H2 frozen
and every native H3 pair occurrence preserved. It does **not** prohibit
changing some rank7 pair occurrences and recovering their named targets
elsewhere. It also does not prohibit the general short-interval cap
criterion, changing H1/H2 components, changing the owner source, or
retiming witnesses. In particular this is not an obstruction to
nu(17)=B(17).

Neither instance saturated. Therefore no proposed complete capped bank
or literal full-cube word was materialized, and no numerical upper bound
for nu(17) changed. Even a future complete cyclic bank would still need
a justified linear splice before giving a B(17)-word.

## 4. Reproducibility and execution limits

Decision program:

    scratch/decide_k17_capped_low_target_two_flows_20260908.py

Independent certificate replay:

    scratch/replay_k17_cap_flow_certificates_20260908.py

Compact decision and replay reports:

    scratch/k17_capped_low_flows_20260908/two_flow_report.json
    scratch/k17_capped_low_flows_20260908/independent_certificate_replay.json

All group-capacity rows for both prescribed instances and the
unrestricted matching/Hall certificate are in the same directory.

Remote directory:

    /home/amodo/exact-b-k17-capped-low-flows-20260908/

Each execution enforced 120 CPU seconds, 150 wall seconds, and 2 GiB
address space. The decision program took 1.527 seconds; the independent
non-optimization replay took 3.450 seconds. Both exited 0. No mathematical
process remains live. These are exact finite integer checks and a
human-readable proof from their certificates, not external or formal
proof-assistant certification.

Internal independent proof review: `exact_equality_structure` read this
entire note and passed Section 3's fixed-bank obstruction. The review
explicitly retained the limitation that later component joins may
create new lower-target witnesses across seams; this certificate does
not itself control those new witnesses.
