# Independent audit of the canonical-Phi plateau age theorem

Date: 2026-09-09. Status: PASS, pure proof review; no mathematical execution.

Reviewed source: [Canonical Phi: exact backward age obligations and a forced-age plateau](CANONICAL_PHI_BACKWARD_AGE_OBLIGATIONS_AND_INITIAL_PLATEAU_THEOREM_20260909.md), Sections 1–8. This review is by the induction agent, independently of the structure agent's derivation. It is internal proof review, not external certification.

## 1. Backward obligations

The strict predecessor list in Section 1 is complete: the s+1 uppers containing a lower Q have distinct Phi preimages, exactly one of which is Q. The remaining s are precisely its strict predecessors. The individual and universal survival recurrences in Section 2 have the stated meanings, and do not by themselves impose residence.

The nested obligation transition in Section 3 is exact. Requiring R_1 to survive the next reverse edge checks every obligation due at that edge. An old obligation lasting t+1 more reverse edges becomes one lasting t; the forward-deleted coordinate d creates an obligation lasting q−1 reverse edges, so it is added to every new R'_t. Thus R'_t=R_(t+1) union {d}, with R_q empty. The stated actual-age test at a finite left boundary discharges precisely the remaining obligations.

The one-step condition is an admissibility condition for that reverse edge; feasibility of a whole finite path still includes all later obligation tests and its left boundary. The source explicitly supplies those requirements. In the finite backward-state graph, reachability of a cycle is equivalent to an infinite backward walk; every individual obligation expires within q−1 steps. This does not impose a one-copy factor, a consistent successor across repeated visits, or any right continuation. Those limitations are correctly retained.

## 2. Suffix-minimum lemma

Let h be the height immediately before x. For a suffix dominating 1^m D 00, every height after x and before the final two sites is greater than h. At the penultimate site a the height is at least h+m−1. If m>=2 this too is greater than h. The final upper height is +1, whereas the global minimum is at most zero because the empty prefix is included. Consequently, for m>=2 the last global minimum lies at or before the prefix immediately before x, and its following up-step lies at or before x.

For m=1 only a can be an additional last minimum. Equality with h requires no zero-to-one additions earlier in this suffix, including a. If b were zero, the final height +1 would force h=2, contradicting global minimality. Thus the exceptional inverse deletion is b, with b=1 and h=0. This proves exactly the source's exception; empty D causes no change.

## 3. Forced ages, including the q-th coordinate

At reverse depth t, earlier proven inverse removals affect only x_1,...,x_(t−1). All terminal ones from x_t onward therefore remain in the incoming upper, which dominates 1^(j+2−t) D 00 on that suffix. The preceding lemma restricts its inverse removal to x_t, an earlier plateau position, an initial zero, or the exceptional final b.

Removing the newly adjoined upper coordinate is the excluded self-return. Any other alternative is a fresh forward insertion. An initial zero or b is absent from the terminal Q_j and must therefore be deleted again before that terminal state. Starting at reverse depth t, this closes a positive run of at most t−1 states, strictly below q when t<=q. A newly inserted earlier plateau coordinate must likewise be deleted before its already established later fresh insertion; its positive run is also shorter than q. Hence the only permissible inverse removal is x_t.

This proves exact terminal ages t for t=1,...,min(q,j+1). Every other terminal coordinate survives all m reverse transitions and thus has age at least m+1. The argument uses only the source's displayed-history hypothesis: at least m incoming transitions, and residence for runs born and closed in them. No global factor or extension is assumed.

In applications of the complete menu in Section 6, carry this history-length hypothesis, or an actual valid past and its boundary-age certificate. A shorter displayed history with unspecified earlier ages is not by itself a certificate. Under the stated hypothesis the menu is exact, including p=q−1, p>=q, q=1, and the case where it is empty.

## 4. Explicit head choices and scope

For q>=3, j=q−2 and nonempty D=1R, canonical Phi adds the last initial zero. Deleting the first D-one therefore sends

    0^(q−2) 1^(q−1) D 00  ->  0^(q−3) 1^q 0 R 00.

That D-one has age at least q by the theorem, and the displayed suffix R recovers D from the head, proving injectivity. For q=2, j=0, Phi instead adds b, giving 1D00 -> 10R01 after deleting the first D-one. These are strict age-legal single edges conditional on the admitted incoming history. The assumptions r>=q−1 and D nonempty ensure that the chosen deletion exists; no omitted small-parameter construction is implied.

The q=3 specialization agrees with the separately reviewed exhaustive two-step calculation in [the corrected root-socket note](Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md): ages 1 and 2 exclude 110D00 and permit the indicated 1110R00 head.

The source correctly stops at a local age interface and an injective single-edge allocation. It does not prove that those heads are free, that incoming histories coexist, that a residual matching exists, or that all-rank targets are preserved. It does not undo the [all-root first-entrance obstruction](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md). No substantive correction was required.
