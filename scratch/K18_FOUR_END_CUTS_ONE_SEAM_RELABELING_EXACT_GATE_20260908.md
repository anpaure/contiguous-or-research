# The exact four-end-cut, one-seam relabeling gate in dimension 18

2026-09-08. Prepared by `exact_b_finite_frontier`. **Complete finite result: every one of the ten oriented tails has a directed precedence cycle. The specified family is impossible.** The one reviewed h100 run finished in 0.3203 seconds. No embedding search was needed and no new word is claimed.

The base is the independently verified universal 17-coordinate word A of length 24,313, SHA-256 `7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9`. Its optimality is recorded in [the direct-forward certificate](K17_OPTIMAL24313_DIRECT_FORWARD_AND_TWO_CYCLE_SEAM_CERTIFICATE_20260908.md). This note concerns one precisely specified construction family for the next dimension; it is not an unrestricted exact-induction claim.

## The family and its exact budget

For a=0,...,4, take B=A[a:m-(4-a)] using zero-based half-open indexing, and also consider its reversal. Each of these ten oriented tails has length m-4=24,309.

The left word is A or its reversal, with a nonempty pair-preserving cap on its last letter. If its final two letters are P,l, a cap C is permitted when

    l minus P subseteq C subseteq l,

and an earlier literal copy of l is present. Replacing l by C preserves the final pair, so every old interval of length at least two has unchanged OR. The earlier copy preserves the only possibly lost one-letter target. Therefore every permitted left word remains universal.

Allow an arbitrary permutation pi of the 17 old coordinates on this capped left word. The candidate word is

    pi(capped left) || {z} || (B_1 union {z}) || ... || (B_l union {z}).

Its exact length is 24,313+1+24,309=48,623, equal to the established endpoint lower bound B(18). A full literal coverage certificate would therefore establish equality at k=18. A negative gate decision would exclude only the stated family.

## The complete finite criterion

The following proof is independently developed in [the one-seam theorem](EXACT_ONE_SEAM_LIFT_PRECEDENCE_AND_ENDPOINT_CAP_THEOREM_20260908.md).

For every nonempty target D missing from ordinary intervals of B, let T(D) be the OR of the longest initial prefix of B whose letters are all contained in D. Empty prefixes are allowed. The tagged target D union {z} is repaired at the seam exactly when an old-coordinate suffix union C of the relabeled left word satisfies

    D minus T(D) subseteq C subseteq D.

Let E_1,...,E_q be the most-recent-first recency blocks of the left word: the differences between consecutive distinct suffix unions, including the empty suffix initially. Make a directed graph on the 17 coordinates with every arc

    x -> y for x in D minus T(D), y outside D,

over every defect D. A relative coordinate relabeling repairs every defect if and only if the coordinates can be assigned to ordered blocks F_1,...,F_q, of sizes |E_1|,...,|E_q|, with every graph arc strictly increasing the block index. This is an equivalence: the suffix ending after the latest required coordinate contains every required coordinate and no excluded coordinate precisely when the strict inequalities hold.

The full old target, if missing, imposes no arcs and is repaired by the full suffix. Every genuine nonempty defect has nonempty D minus T(D), since otherwise an internal prefix already realizes D. Hence the graph's initial minimal vertices equal the intersection of all defects, with the empty intersection interpreted as the full coordinate set.

## Complete decision for the measured profile shape

The checker derives every valid endpoint cap and its actual suffix-recency blocks from the literal input; it does not assume the endpoint data. It verifies that the distinct resulting profiles are

    (s,7-s,1,1,1,1,1,1,1,1,1,1), s=1,...,5.

All caps with the same profile are equivalent under unrestricted relative relabeling: any ordered block assignment of that shape is the image of any one representative. Thus it is enough to retain one literal representative per shape, while recording all valid caps and duplicate backups.

For any one of these profiles, first reject directed cycles. In a directed acyclic graph, enumerate each s-element subset of the initial minimal vertices as the first block. Remove the whole block simultaneously. A second block of size 7-s exists if and only if at least 7-s vertices are now minimal. Any such subset can be selected, because all later blocks are singletons and every induced subgraph of a directed acyclic graph has a topological ordering. Thus no enumeration of the second-block choices is needed. If every first-block choice fails the count test, the prescribed profile is impossible. This is a complete finite decision, not a heuristic permutation search.

## Reproducible checker and certificate scope

Source: [decide_k18_four_end_cuts_one_seam_relative_relabeling_20260908.py](decide_k18_four_end_cuts_one_seam_relative_relabeling_20260908.py).

The single completed run was restricted to `ssh h100`, hostname `arboghast`, with limits of 60 CPU seconds, 90 wall seconds, and 1 GiB address space. Root and `exact_b_induction` independently read the full source before execution. The separate endpoint audit by `exact_equality_structure` also confirmed the cap data. The checker first verifies the exact input SHA and directly scans all ordinary interval ORs of the base. It derives the endpoint-cap representatives with explicit earlier duplicate positions and pair-union equalities.

Before the ten decisions, it includes a positive control: B=A[:-1] must satisfy the graph constraints under A's actual unchanged recency partition. Every control defect also receives a directly accumulated suffix-plus-prefix seam projection witness. This checks the graph direction and strict-block interpretation against the already proved standard trimmed lift.

Each of the five distinct trimmed tails is scanned once, by advancing the right endpoint from every left endpoint until either the full old set or the end of the word. Reversal has exactly the same internal target family, so its coverage census is reused. For each of the ten orientations, the report contains the complete defect list, rank counts, compatible prefix data, graph masks, and either a directed-cycle witness or every necessary first-block count test for all five profiles.

If an embedding succeeds, the checker constructs an explicit coordinate permutation and actual 48,623-letter word. It enumerates all ordinary interval ORs using compressed ending-suffix states, then independently replays one nonwrapping interval for every one of the 262,143 nonempty targets with a segment tree. Only this literal verification can produce the output status `SAT_LITERAL_VERIFIED`.

No root handoff, existing optimal word, or previous construction is modified by this checker.

## Exact result and short obstruction certificates

Full machine-readable report: [one_seam_relative_relabeling_decision.json](k18_four_end_cuts_one_seam_20260908/one_seam_relative_relabeling_decision.json). It contains every defect, its exact longest compatible prefix, every graph arc, and a generating defect for each displayed cycle edge.

The original standard trimmed lift is a positive control: A[:-1] has the single defect 26,291. A suffix of the original left A of length four already has OR 26,291; its union with the tail's first-letter prefix 8,834 is still 26,291. Its unchanged recency profile is `(5,2,1,1,1,1,1,1,1,1,1,1)`. The exact graph constraint and this direct literal seam projection both pass.

The forward left word has last letter 689, preceding letter 25,249, and required cap coordinate mask 16. Its 16 nonempty permitted caps yield sizes 1 through 5. The reversed word has last letter 8,834, preceding letter 10,913, and required mask 2. Its eight caps yield sizes 1 through 4. All 24 caps have an explicit earlier duplicate backup in the report, and together yield exactly the five profile shapes above.

Every four-letter-trim case fails earlier, at the unrestricted graph test. The following cycles use **zero-based coordinate indices**, matching the script: coordinate i is mask `1<<i`. For a cycle `(v_0,...,v_j=v_0)`, the listed defects generate its edges in that order.

| Prefix cut | Suffix cut | Tail orientation | Defect count | Directed cycle | Generating defects |
|---:|---:|---|---:|---|---|
| 0 | 4 | forward | 9 | 0→2→0 | 26275, 26278 |
| 0 | 4 | reverse | 9 | 5→7→5 | 25122, 1666 |
| 1 | 3 | forward | 10 | 0→2→0 | 26275, 26278 |
| 1 | 3 | reverse | 10 | 0→3→14→0 | 10915, 76475, 25122 |
| 2 | 2 | forward | 11 | 2→4→2 | 26279, 26291 |
| 2 | 2 | reverse | 11 | 1→3→1 | 10915, 76473 |
| 3 | 1 | forward | 12 | 1→4→1 | 10915, 2705 |
| 3 | 1 | reverse | 12 | 1→3→1 | 10915, 76441 |
| 4 | 0 | forward | 15 | 0→1→4→0 | 2705, 10915, 76304 |
| 4 | 0 | reverse | 15 | 0→1→2→0 | 2705, 10915, 109212 |

For example, the forward prefix A[:-4] misses 26,275 and 26,278. For both targets the longest compatible prefix has union 8,834. Target 26,275 requires coordinate 0 in the suffix while excluding coordinate 2; target 26,278 requires coordinate 2 while excluding coordinate 0. The two required strict recency inequalities contradict each other. The other rows have the same two- or three-inequality form, with all exact data retained in the report.

The five defect rank censuses, unchanged by reversal, are:

| Prefix cut | Counts by target rank |
|---:|---|
| 0 | rank4:1, rank5:1, rank8:3, rank9:4 |
| 1 | rank5:1, rank7:1, rank8:3, rank9:4, rank10:1 |
| 2 | rank6:1, rank7:2, rank8:3, rank9:4, rank10:1 |
| 3 | rank5:1, rank6:1, rank7:2, rank8:3, rank9:4, rank10:1 |
| 4 | rank5:2, rank6:1, rank7:2, rank8:4, rank9:4, rank10:2 |

Thus the negative result is stronger than failure of the five cap profiles: **none of these ten fixed marked tails can be completed by any universal left word on the old coordinates using a single pure singleton bridge.** Every left word's suffix unions form an ordered chain, so every such completion would have to satisfy the same contradictory strict precedence cycle. Allowing arbitrary left length, different left letter contents, or a different recency profile does not remove this fixed-tail contradiction.

This does not rule out changing the marked tail beyond these five trims and their reversals, inserting a different bridge, using multiple seams, or constructing an optimal 18-coordinate word another way. At the time this gate finished, the verified bounds were 48,623≤nu(18)≤48,626. A subsequently supplied literal word independently attains 48,623; see [the independent first-occurrence certificate](K18_OPTIMAL48623_INDEPENDENT_FIRST_OCCURRENCE_CERTIFICATE_20260908.md). The narrow fixed-tail obstruction and the new optimum are consistent.

Remote report directory: `/home/amodo/exact-b-k18-four-end-cuts-one-seam-20260908/`. The execution command was `python3 /home/amodo/decide_k18_four_end_cuts_one_seam_relative_relabeling_20260908.py`. An earlier shell invocation using the unavailable name `python` exited 127 before the script started; it ran no mathematical code. The subsequent `python3` invocation was the sole actual run, with no restart or variation.
