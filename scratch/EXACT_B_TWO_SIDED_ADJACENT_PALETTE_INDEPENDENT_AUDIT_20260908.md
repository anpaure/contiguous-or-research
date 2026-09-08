# Independent audit of the two-sided adjacent-palette requirement

Date: 2026-09-08.
Reviewer: Codex subagent exact_b_finite_frontier.
Status: PASS, elementary proofs checked; no computation rerun.

Reviewed files:

- scratch/EXACT_B_TWO_SIDED_ADJACENT_PALETTE_REQUIREMENT_20260908.md;
- MASTER_HANDOFF.md Section 3.12 for the credited lower-side argument;
- scratch/K17_PBBS_UPPER_CUT_CORES_AND_306_OWNER_SOURCE_STAGE_20260908.md for the canonical cut census; and
- scratch/PBBS_CANONICAL_MOUNTAIN_C6_ALL_UPPER_TRANSPORT_20260908.md, especially Section 4, for the post-C6 global-exclusivity scope.

## 1. Endpoint ordering and charge

Distinct same-rank target witnesses cannot contain each other; equal starts or equal ends would force containment. Thus both selected endpoint sequences are strictly increasing and each misses exactly t physical positions.

All interval unions from one left endpoint form a chain, as do those ending at one fixed right endpoint. Hence an endpoint of either specified type can be charged by at most one distinct target of a fixed rank. Charging a missing palette target to one unselected endpoint in a chosen witness therefore gives at most 2t targets. A physical position counted once as an unselected start and once as an unselected end correctly contributes two endpoint types to this bound.

## 2. Upper counterpart

For an adjacent-upper witness [a_j,b_i], j=i yields exactly the selected owner and j>i gives an interval contained in that owner. Thus its rank r+1 forces j<i.

It then contains both J_j and J_(j+1): its left endpoint precedes both selected starts, and b_i>=b_(j+1). The two distinct rank-r owner sets have a union of size at least r+1, contained in the rank-(r+1) witnessed set. Consequently the union equals that target.

This proves the new upper inequality. It uses only one selected witness per middle target and endpoint monotonicity. Critical-witness uniqueness, fixed window lengths, a maximal source, and Johnson adjacency are unnecessary.

## 3. Lower counterpart and odd efficiency

For a rank-(r-1) witness with selected endpoints, j<=i would make it contain J_j. Thus j>i; it lies inside J_i and J_(i+1). Their intersection has size at most r-1 and contains the witnessed rank-(r-1) target, so equality follows. This is correctly credited to the master rather than presented as new.

In the odd middle-layer case with the adjacent lower rank covered, each Johnson step contributes one lower color and each non-Johnson step contributes none. Therefore b+e_minus=W-1-|P_minus|, and the upper bound 2t-1 follows directly. For k17,t=3 the combined non-Johnson/repetition allowance is five. The statement is not meant to infer a rank-zero coverage condition in the degenerate k=1 nonzero-target problem.

## 4. Exact recapture inference

After opening the specified owner cycles into retained blocks, any rank-ten target absent from every internal adjacent union can enter P_plus only at a new seam. Each seam has one union value, so it contributes at most one distinct required rank-ten color. The upper inequality permits at most six rank-ten targets outside the final P_plus for a length-W+3 universal word. Thus |H|-6 distinct missing colors must be recreated as seam colors.

The canonical census supplies 59 distinct losses, one from each of 59 cycles with no globally safe rank-ten cut. The exclusive target families for different cycles are disjoint. A target lost from all old interval witnesses is certainly absent from all old internal adjacent witnesses. Also, on distinct same-rank owners any rank-ten union of a longer owner interval already equals the union of its first two owners. There is no overlooked wider-owner witness which can evade this rank-ten counting argument.

The resulting lower requirement of 53 recaptured seam colors is valid for the specified all-cycle assembly. It counts required colors and does not charge extra physical letters or bound unrestricted nu(17).

## 5. Mountain replacement and scope

The companion mountain note does more than retain a local palette. It states that both new components have a globally exclusive rank-ten loss at every cut, tested against their companion and all unaffected cycles. Their combined full upper support equals that of the two old components. Hence exclusivity for every unaffected component is unchanged, and the total count of 59 unsafe components remains valid. This justifies retaining the 53-color condition after that particular C6 replacement.

One useful explicit reading: 53 is the total new-seam requirement relative to the selected all-cycle starting factor. If some prefix seams have already been fixed, their successful recaptures count toward that total. The note does not establish 53 additional Q seams after the 306-owner prefix stage unless those existing credits are separately subtracted. Arbitrary rethreadings require their own starting cut-bank accounting, as the root note correctly states.

Every seam whose union has rank ten is Johnson at rank nine and simultaneously supplies one rank-eight intersection color. The coupling of these two palettes is therefore real. Neither endpoint bound asserts a compatible spanning chronology, preserves more distant ranks, or solves the lower common cap.

No mathematical defect remains in the reviewed statement or proof. No code was executed for this audit.

## 6. Audit of the sharper consecutive-start upper theorem

The subsequently proposed upper J bound is valid. Assume owner intervals [i,r_i], nondecreasing h_i=r_i-i, and that the word ends at r_(W-1). Let J count every strict depth increase, including a possible increase at the final owner.

If an adjacent-upper witness ends at r_i, its start at most i-1 makes it contain two consecutive owners, so their union equals its value; its start at least i puts it inside owner i and prevents upper rank. A witness ending before r_0 lies inside the first owner. If its endpoint b lies in r_i<b<r_(i+1), then a<=i-1 again contains consecutive owners and a>=i+1 lies inside owner i+1. Only a=i is exceptional. For a fixed gap these [i,b] intervals are nested, so the gap contributes at most one distinct rank-(m+1) color. A gap exists exactly at a strict depth increase. Thus the number of adjacent-upper colors absent from consecutive-owner unions is at most J.

Unlike the lower J+2 theorem, this upper bound requires no exclusion of a final depth jump. It still requires that the physical word have no tail beyond the final owner deadline.

For the depth-two/depth-three k17 one-pivot schedule, the sole exceptional upper cell is [305,308], which contains the whole owner P_305. Every exceptional rank-ten color must be one of the eight rank-ten supersets of P_305.

## 7. Audit of the stronger 59-new-edge requirement

A reference cycle with a globally exclusive rank-ten loss at every possible cut has the following property: every one of its edges carries a globally unique rank-ten adjacent-union color. Indeed, if cutting edge e loses rank-ten target S, every old adjacent witness of S must be e itself. If another edge supplied S it would survive that cut. Every longer rank-ten owner witness contains a rank-ten adjacent witness, since its distinct rank-nine first two owners already union to all of S.

Any linear spanning owner path must omit at least one undirected edge of each reference cycle; including every edge would retain a closed cycle inside a path. From the 59 unsafe cycles choose one omitted edge each. Their 59 globally unique colors are distinct and absent from every retained reference edge. Therefore each color requires either a new owner edge or an exceptional physical upper witness.

The root's updated finite diagnostic checks both the original exclusive-target lists and the post-mountain-C6 lists. None of the eight possible upper-pivot colors is exclusive to any of the59 unsafe cycles. The only exclusive one is103767, supplied by safe cycle69. The existing old-prefix Johnson seams likewise have zero credit against these59 private families. Consequently all59 colors require new owner edges relative to the reference factor. The argument permits arbitrary rethreading of Q; rethreading can supply the needed new edges but cannot evade the count under the stated fixed-prefix/schedule hypotheses.

Moreover, a rank-ten P/Q seam also contains P_305 and hence is one of those same eight supersets. It cannot earn one of the59 required private colors either. For that fixed old prefix, the59 recaptures therefore lie strictly inside Q, not at P/Q.

This last conclusion concerns the OLD non-Johnson prefix with P_305=103765 and the specified one-pivot schedule. The old one-pivot prefix is separately impossible by its lower facet budget. If a replacement prefix changes its endpoint or new seam colors, its credit check must be updated. These counts remain source-relative necessary conditions and do not prove a lower bound on unrestricted nu(17).
