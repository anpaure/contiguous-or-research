# K17 canonical PBBS cut cores and an actual 306-owner source stage

Date: 2026-09-08.
Status: exact finite census and two complete finite decisions, executed only on h100. A 306-owner path and its 308-letter depth-two factor are materialized. This is not an optimal universal word or an all-k proof. Later on September8, its one-pivot extension was ruled out by the global facet budget, and a different all-ports Johnson prefix superseded it. The census and finite construction remain valid.

## 1. Concrete result

The canonical k17 upper-middle PBBS factor has 146 cycles and 24,310 distinct rank-nine owners. The six cycles carrying every positive run of length three can be replaced by one explicit path of 306 owners such that:

- every owner in those six cycles appears exactly once;
- every strictly internal positive coordinate run has length at least three;
- the maximal depth-two source is nonempty at every position and replays the owner path exactly;
- together with the other 140 intact canonical cycles, the path retains every one of the 41,225 proper upper targets of ranks 10 through 16; and
- exactly three of the five new block seams are non-Johnson, the minimum possible on the specified safe-port bank.

The corresponding global adjacent-intersection rank-eight palette misses five targets. This count is a palette statement, not a claim that every possible lower witness has been checked.

Literal artifacts:

    scratch/badsix_relaxed_306_owner_path.word
    scratch/badsix_relaxed_308_depth2_source.word

The main remaining source task is to fuse the other 140 cycles with this path, with exact upper-witness replacement, legal residence and compatible lower compilation. Nothing here supplies that task.

## 2. Exact cut-core lemma

Let C=(T_0,...,T_(L-1)) be a cycle of owners. A cyclic witness for a target Y, starting at i and using q+1 owners, crosses exactly the cut positions

    F(i,q)={i+1,...,i+q} mod L.

A cut position j means cutting the edge entering owner T_j. Define

    K_C(Y)=intersection F(i,q)

where the intersection runs over every cyclic witness of Y in C. Then opening C once at cut j loses all its old witnesses of Y if and only if j belongs to K_C(Y).

Proof: one witness survives as a linear interval exactly when the removed edge is not among its internal edges. All witnesses are lost exactly when the cut lies in all their internal-edge sets. QED.

For a family of cycles, call Y exclusive to C if no other cycle supplies Y. Put

    L_C(j)=number of exclusive targets Y with j in K_C(Y).

If every original cycle is cut at least once and only the retained block interiors are counted, then at least

    sum_C min_j L_C(j)

distinct targets are lost. This is because exclusive target families for different cycles are disjoint; extra cuts cannot restore an old within-cycle witness. Reversing retained blocks also cannot restore a witness crossing a removed edge. New seam intervals may recreate the targets, so this is a mandatory recapture count **before new-seam witnesses**, not a lower bound on nu(k).

## 3. Complete k17 census

The original f map is reconstructed directly from each rank-eight mask A. Find its unique cyclic Dyck root u; then

    f(A)=A^c minus {u}.

The upper-middle owner cycles are the complements of cycles of f^2. No optimizer or precomputed component list is a premise.

The exact cycle-length histogram is:

| length | number of cycles |
|---:|---:|
| 17 | 6 |
| 51 | 10 |
| 85 | 44 |
| 119 | 34 |
| 153 | 24 |
| 187 | 6 |
| 221 | 1 |
| 357 | 12 |
| 459 | 2 |
| 561 | 1 |
| 765 | 5 |
| 1309 | 1 |

For each cycle start, the verifier extends interval ORs until the full set is reached. On a plateau with unchanged OR, only its shortest occurrence needs to update the cut core: each longer occurrence has a superset of the shortest occurrence's internal edges. Proper upper targets cannot reappear after the full OR. These observations prove completeness of the compact enumeration.

The rank counts reproduced across the whole factor are:

    rank:   10     11    12    13   14  15  16
    count: 19448  12376  6188  2380  680 136 17.

There are 24,157 targets supplied by exactly one cycle, partitioned by rank as

    16,388 / 6,545 / 1,207 / 17 at ranks 10 / 11 / 12 / 13.

Exactly 59 cycles have no cut preserving all their globally exclusive upper targets. All 59 already have a rank-ten obstruction at every cut. The sum of their cyclewise minimum losses is 129, of which at least 59 are rank ten. Thus a full fusion that breaks all 146 original cycles must recreate at least 129 distinct globally exclusive targets through new seams or other changes.

The height-eight mountain cycle is cycle 0, of length 17, with root Dyck word 1111111100000000. At every cut it loses exactly 1,2,3,4 globally exclusive targets at ranks 10,11,12,13, respectively: ten in total. This extends the familiar immediate-upper mountain obstruction to its exact multirank cut bill.

No one of the 146 cycles has a cut preserving every target supplied locally by that cycle. Local losses can nevertheless be harmless globally when another cycle retains a witness.

Census artifacts:

    scratch/audit_k17_pbbs_cycle_upper_cut_inventory_20260908.py
    scratch/k17_pbbs_cycle_upper_cut_inventory_20260908.json

Remote execution directory:

    /home/amodo/exact-b-k17-pbbs-inventory-20260908/

## 4. Jointly safe openings of all six short-run cycles

The exact general component classification is proved separately in

    scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md.

For the deterministic cycle numbering used by the census, the six bad cycles are

    115,116,118,122,129,138,

each of length 51. None has a globally exclusive proper upper target. That observation alone would not justify cutting all six simultaneously.

The joint census finds exactly 102 targets with no supplier outside these six cycles. All have rank ten. Their supplier graph is the cycle

    115--116--118--122--129--138--115,

with seventeen distinct targets on each graph edge. Every such target has exactly the two indicated supplier cycles.

For each of the six cycles, intersect the safe cuts for every one of these 102 targets that it supplies. There are exactly seventeen resulting ports:

    cycle115: indices 0 mod 3;
    each other listed cycle: indices 2 mod 3.

Here indices refer to the deterministic cycle ordering obtained by starting from the least unused lower-owner mask and repeatedly applying f^2.

Choosing any one allowed cut independently in each of the six cycles preserves the whole global proper upper deck while all other cycles remain intact. Indeed, each of the 102 special targets survives in each of its two supplying bad-cycle paths; every other upper target has an intact supplier outside the bad sector. Reversal of an opened path does not change its interval-OR support.

This gives a genuinely joint safe-port bank. It does not require a union bound, probabilistic independence, or a choice-dependent witness transfer.

## 5. Exact seam decision

Each cycle has seventeen safe cuts and two orientations, giving 204 oriented block options in total. For a block P and coordinate x, let s_P(x) be its terminal positive-run length, or zero if x is absent from its last owner. Define p_Q(x) analogously at the first owner of Q.

Since every coordinate is nonconstant in every 51-owner block, no positive run can cross more than one block seam. The concatenation P,Q creates no strictly internal positive run of length one or two precisely when, for every x,

    s_P(x)+p_Q(x) is zero or at least three.

This formula covers all four endpoint-membership cases. Internal runs within each block are already valid.

To ensure a nonempty depth-two envelope at a possibly non-Johnson seam, also require the two crossing triple intersections to be nonempty:

    P[-2] intersect P[-1] intersect Q[0] is nonempty;
    P[-1] intersect Q[0] intersect Q[1] is nonempty.

The remaining triple intersections lie inside original Johnson blocks and are nonempty. Boundary single/pair intersections follow from these conditions.

### 5.1 Requiring every seam to be Johnson is impossible on this bank

Add the condition |P[-1] symmetric_difference Q[0]|=2. The resulting option graph has 204 directed arcs, all between cycles 115,116,138. The other three colors are isolated. The complete color-subset/last-option dynamic program has reachable state counts

    204,170,102,0,0,0

at one through six selected cycle colors. Hence no four-block path, and in particular no path through all six cycles, exists on this specific Johnson-safe bank.

This is a finite bank obstruction. It does not exclude other cuts with coordinated upper repair, a split cycle, an external connector block, or a non-Johnson seam.

Artifacts:

    scratch/decide_k17_pbbs_badsix_safe_johnson_path_20260908.py
    scratch/k17_pbbs_badsix_safe_johnson_path_decision_20260908.json

### 5.2 Allowing guarded non-Johnson seams succeeds

Retain the positive-run and nonempty-triple conditions and charge one for each non-Johnson seam. The exact same-state dynamic program has 3,060 allowed option arcs, 204 complete terminal states, and minimum total charge three.

An attaining path uses the following cycle/cut choices, all in their forward orientation:

    118/2, 129/8, 122/29, 116/50, 138/29, 115/0.

The literal concatenation has 306 distinct rank-nine owners. Its maximal depth-two inverse has 308 letters, minimum letter rank two, and passes all 306 literal identities

    E_i union E_(i+1) union E_(i+2) = T_i.

A separate literal interval-OR replay of this path together with the 140 intact cycles retains all 41,225 proper upper targets.

The resulting adjacent-intersection rank-eight palette of the whole mixed path/cycle family misses exactly

    21866,43860,46420,70998,92834.

These five masks are a downstream obligation. A rank-eight palette count does not rule out additional source-level short witnesses, and no lower compiler has yet been run.

Artifacts:

    scratch/decide_k17_pbbs_badsix_safe_relaxed_path_20260908.py
    scratch/k17_pbbs_badsix_safe_relaxed_path_decision_20260908.json
    scratch/badsix_relaxed_306_owner_path.word
    scratch/badsix_relaxed_308_depth2_source.word

## 6. Why the finite decisions are complete

A dynamic-programming state is (M,i): the set M of used cycle colors and the last oriented block option i. The available continuation depends only on these two objects, because each block is fixed and every seam predicate is pairwise. Thus retaining one minimum-cost predecessor for each state loses no future possibility. Initial states contain any one of the 204 options; transitions append any compatible unused color. Induction on |M| proves that the stored costs are exactly the optimum costs of every corresponding partial path. Terminal states use all six colors.

The JSON decisions include every option, compatibility edge or reconstruction source, and reachable state (with distances in the relaxed case), so this is a reproducible finite certificate rather than a timed search result. All mathematical execution was on h100.

The supplied verifier scripts should be placed in the remote directory as audit.py, decide.py, and relaxed.py, respectively. The latter two reuse the preceding exact source generator. Their recorded results are mathematical evidence only in the fixed canonical k17 setting.

## 7. What this advances

The short-residence sector was placed in one explicit depth-two-compatible block of 306 owners while retaining the global upper deck against intact outside cycles. The variable-depth arithmetic in

    scratch/PBBS_306_PREFIX_EXACT_DEADLINE_COMPILER_20260908.md

initially supplied a schedule for testing this real prefix. The later global facet-count argument in `K17_PBBS_PREFIX_ONE_PIVOT_NOGO_AND_CONSECUTIVE_START_BUDGET_20260908.md` proves that its three non-Johnson edges prevent a universal one-pivot completion, regardless of the remaining chronology. It is no longer an active one-pivot candidate.

The replacement all-ports Johnson prefix is stored separately and has its endpoint interface in `K17_PBBS_ALLPORTS_JOHNSON_PREFIX_ENDPOINT_INTERFACE_20260908.md`. Its outgoing seam into the depth-three sector, fusion of the other cycles, mandatory upper-target recapture, and complete lower common-cap compiler remain open. The old 308-letter factor is a valid small source component, not a universal word on 17 coordinates. No bound on nu(17) has changed.
