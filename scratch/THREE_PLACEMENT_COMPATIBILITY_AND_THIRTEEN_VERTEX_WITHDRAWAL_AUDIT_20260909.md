# Three-placement compatibility and thirteen-vertex withdrawal: independent audit

Date: 2026-09-09. Status: pure-proof PASS with the explicit guards below. No mathematical execution.

Reviewed in full the pasted submission at `/Users/amir.nuriyev/.codex/attachments/3f53a597-1ae3-4d12-bd60-ac5bfd049c51/pasted-text.txt`. Its first part proposes a bounded-obstruction theorem for overlapping target placements, an exact forbidden-pair/triple formulation, and a local withdrawal reduction. Its later numerical and optimality assertions require separate raw artifacts and verification; they are not certified by this proof audit.

## 1. Model and maximal common caps

Let E_i be nonempty envelopes at positions of a finite cycle. A cell is a nonempty consecutive cyclic window of length less than q. For the principal application q=3, its length is one or two. A placement e=(S,J) prescribes the nonempty target S as the OR on J. A placement matching has distinct target labels and distinct physical cells.

For a placement family P define

    C_i(P)=E_i intersect intersection_(S,J in P, i in J) S.

The empty target intersection contributes the whole alphabet. Simultaneous realizability by nonempty letters A_i subset E_i, preserving every q-window OR, is equivalent to all of:

1. Every C_i is nonempty.
2. Every q-window has the same OR under C as under E.
3. For every (S,J) in P, the OR of C on J is S.

Every realizing A is contained in C positionwise. Enlarging A to C cannot introduce a coordinate outside a prescribed S on its cell, or outside the original envelope OR on a protected window. Thus every equality and nonemptiness persists under enlargement. Conversely C itself is a realizing assignment if the three checks pass.

This exact maximal-cap principle is already proved in [the earlier short-target cap note](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md), Section 4. The new deduction reviewed here is the size bound on a failing subfamily and its local withdrawal consequence; the cap principle itself is not new.

## 2. Three placements suffice, and two do not

For q=3, each position belongs to at most three distinct eligible cells: its singleton and the pairs immediately to its left and right. Suppose the maximal caps fail a check.

* If C_i is empty, retain all placements whose cells contain i. There are at most three, and their same cap remains empty.
* If a coordinate x in a protected triple's original OR is lost, then at every position of that triple whose envelope contains x, some selected placement excludes x. Retain one such placement per position. At most three suffice to lose x on the same protected triple.
* If x in a prescribed target S is lost from its cell J, retain that placement. At every position of J whose envelope contains x, retain a placement excluding x. There are at most two such positions, so at most three placements suffice. A selected excluding placement cannot be the retained target placement itself, because x belongs to S. If x occurs in no envelope on J, the target placement alone already fails.

No prescribed cap union gains a coordinate outside its target. These failures exhaust the criterion in Section 1. Feasibility is hereditary under deleting placements, because the caps only enlarge. Therefore a matching family is feasible if and only if every subfamily of at most three placements is feasible.

The proposed sharpness example passes. On a four-position cycle with all envelopes {a,b,c,d}, prescribe {a},{b},{c} on three consecutive singleton cells. Any two prescriptions leave a full-envelope position in every protected triple, but all three make their common triple lose d. This has distinct targets and distinct cells and proves that pairwise feasibility alone is insufficient.

## 3. General q and cyclic small periods

For q>=2, at a fixed position there are at most

    1+2+...+(q−1)=q(q−1)/2

short cells. Thus an empty-cap certificate has at most that size. A missing protected-window coordinate needs at most q placements, and a missing prescribed-target coordinate needs its own placement plus at most q-1 suppressing placements. Consequently

    h_q=max(q,q(q−1)/2)

is a valid obstruction bound. This proves the submitted generalization, without asserting its sharpness for every q.

The clean conventional domain is cycle length M>=q, with cells indexed by cyclic start and length, so all cells are proper position intervals. Small periods can also be handled without increasing the bounds: define a cell by its physical start and length, use its set of visited positions for all ORs and caps, and deduplicate repeated positions when counting witnesses. For length ell, a fixed position is contained in at most min(ell,M) physical starts, which is at most ell. A protected q-window or a short cell visits at most q or q-1 distinct positions. Thus the same proof works even when a window wraps through the same position more than once. If instead coincident cells are identified as position sets, there are fewer cells and the bounds remain valid.

What is not allowed is silently introducing arbitrarily many copies of the same physical cell while retaining the one-placement-per-cell count. Multiple components cause no problem: protected windows and cells stay within their component, and the argument applies there.

## 4. Exact binary formulation

Enumerate individually feasible placements. Require exactly one selected placement for every requested target and at most one per physical cell. Add the inequality sum_(e in F) x_e <= |F|-1 for every infeasible pair or triple F. At an integral selection, these matching constraints and the theorem in Section 2 are necessary and sufficient for a simultaneous refinement. The realizing letters are the maximal common caps.

Because individual infeasibility was removed from the candidate list, no missing singleton constraint is hidden. When a proposed integral matching fails, the preceding proof extracts a forbidden selected subfamily of size two or three, whose inequality cannot exclude a valid matching. An exact separation loop need not enumerate all such constraints in advance.

This formulation specifies feasibility; it neither proves that a full feasible selection exists nor makes its global search easy. Coverage of targets not prescribed in the selection must come from separately retained witnesses or protected-window consequences. The old exact cap and cap-bit/SAT formulations already specified compatibility without a letter search; the bounded-order forbidden-family characterization is an additional useful form of that criterion.

## 5. Locality of a new insertion

Let P be an already feasible matching and e=(S,J) individually feasible, where S is not already prescribed. Extend the cyclic cell J by two positions on each side and call the resulting position set R. For a singleton it has at most five positions, and for a pair at most six.

For any retained subfamily of P, a newly failing cap check after adding e has a witness entirely among e and old cells meeting R:

* Only caps on J change. An empty-cap failure is therefore at J, and all its suppressing placements meet J.
* A newly damaged protected triple meets J; the entire triple lies in R. Each selected suppressor meets that triple and hence R.
* A newly damaged old prescribed cell K must meet J; because K has length at most two, it is contained in R. Its suppressors meet K. A failure of the new target itself involves only cells meeting J.

The old retained family is feasible by heredity, so the witness necessarily includes e. This proves the required locality after arbitrary withdrawals as well as before them.

The precise statement is about a needed witness or an inclusion-minimal new obstruction. It is too strong literally to say that an irrelevant placement can never occur in any incompatible triple: one can append an irrelevant placement to an already incompatible pair. Such redundant triples do not affect the reduction.

A proper cyclic interval of t<=6 positions meets t singleton cells and t+1 pair cells, so at most thirteen old cells are relevant. If R fills a small cycle, it meets only M singleton and M physical pair cells, at most twelve when M<=6. The indexed M=1 or M=2 conventions likewise give fewer than thirteen. Thus wraparound and repeated neighborhood positions cannot enlarge the claimed bound. The bound counts relevant old placements, not coordinates or arbitrary copies of cells.

## 6. Exact minimum-cost withdrawal, including an occupied cell

Give old placements finite nonnegative withdrawal costs. Let N be the old placements whose cells meet R, so |N|<=13. Form a forced set F containing:

1. Any old placement occupying the proposed physical cell J.
2. Every p in N for which {e,p} fails simultaneous cap feasibility.

The first condition is an explicit matching constraint. Under the submission's distinct-target hypotheses, a full feasibility test of both prescriptions on the identical cell already rejects the pair, since one cell cannot have two different ORs. Nevertheless this conflict should be forced explicitly rather than passed into a theorem stated only for families with distinct cells. A test of only nonempty caps and protected windows would not suffice. If a broader variant allowed equal target labels, cell occupancy would still be a matching conflict even when the cap assignment happened to be feasible.

On vertices N minus F, add edge pp' exactly when {e,p,p'} is infeasible. Old-only subfamilies are feasible, and pairs with e remaining here are feasible, so these edges are exactly the relevant unresolved triple constraints. Every feasible withdrawal set must contain F and meet every edge. Conversely, removing F and a vertex cover eliminates every local size-at-most-three obstruction; Section 5 supplies a local witness for any hypothetical remaining failure. The resulting family is therefore feasible.

Because all costs are nonnegative, an optimum need not withdraw any irrelevant old placement. Its exact cost is

    sum_(p in F) cost(p) + minimum_weight_vertex_cover(N minus F).

Withdrawing all local vertices is always feasible: e is individually feasible and no remaining obstruction has a local witness. Thus this is a finite optimum under the stated hypotheses. At most 2^13 old-vertex subsets are needed for brute-force selection, although cap tests still have their usual dependence on alphabet representation.

The hypotheses are essential to this form: the old family must be feasible; e must be individually feasible; its target must not already be prescribed elsewhere; and withdrawal costs must be nonnegative. If the target were already prescribed, its old representative might lie outside R and would need separate forced removal before claiming a thirteen-vertex bound. The cost counts withdrawn placements, not necessarily targets lost from the actual word.

## 7. Finite claims and status boundaries

The pasted text contains both an earlier claimed 352,862 / 705,724 upper pair and a later claimed optimal 352,719 / 705,435 pair, together with sandbox links and claimed Hall, constructor and execution counts. The pasted proof alone contains none of the raw words or graph certificates. This audit does not certify its zero Hall deficiency, five-cycle or one-cycle reconstruction, numerical test counts, or finite word coverage.

During this audit, actual raw words were supplied separately and dedicated literal checkers were prepared. The induction agent fully reviewed the upper and optimal forward sources and the corresponding root suffix/range/lift sources before their proposed executions. Those checks and any resulting numerical conclusions have separate reports. In particular the now-supplied optimal filenames are not, by themselves, evidence of optimality; complete literal verification and the retained endpoint lower bound are needed.

The endpoint lower-bound argument and periodic-core lift in the second half are retained results, already reviewed independently in [the earlier 19/20 audit](K19_K20_ENDPOINT_PERIODIC_LIFT_AND_TURNOVER_AUDIT_20260909.md). Their stated use is mathematically valid conditional on the claimed universal core and safe ordinary opening. The new local compatibility theorem does not establish either input, an optimal opening, or an all-dimensional construction.

The compatibility and withdrawal proofs pass with the explicit cell-occupancy, cyclic-indexing and locality qualifications above. This is internal independent proof review, not external or formal certification. No mathematical execution was performed for this audit.
