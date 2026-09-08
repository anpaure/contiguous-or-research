# The 0P1 parent embedding: exact connector ages and its sole bad arrival

Date: 2026-09-09. Pure proof; no mathematical execution or construction search.

This note concerns an actual specified strict canonical-Phi factor on 2r+1 parent coordinates, of lower rank r, with residence at least three. It uses the embedding **0P1**, not the separate smaller-factor embedding 00X11. For the supplied nineteen-coordinate carrier the required factor and residence were already verified in [the literal carrier certificate](K19_OPTIMAL_LITERAL_PHI_CARRIER_PAIR_CHANGING_COMPILER_AND_QUOTIENT_CERTIFICATE_20260909.md), Section 3. The pure structural statements below are independent of the separately executed fixed-input counts, linked in Section 6.

## 1. Coordinates and the embedded factor

Assume r>=2. Prefix the parent word P by a fixed child zero u and suffix it by a fixed child one b. The last parent coordinate is called a; it is an active parent coordinate, not fixed. Thus the child state is 0P1, on 2r+3 coordinates with rank r+1. In the nineteen-coordinate application, u is child bit0, parent bit18 becomes child a=bit19, and b is child bit20.

Every prefix height within P is shifted down by one. Since the parent lower walk has final height -1, its minimum is at most -1, so the child minimum within P is at most -2. The last child one finishes at height -1 and cannot be a first global minimum. The leading zero likewise cannot be the child minimum. Therefore

    Phi_child(0P1) = 0 Phi_parent(P) 1.                 (1.1)

Every parent edge P->sigma(P) embeds as 0P1->0sigma(P)1. Parent-coordinate ages are unchanged; b is permanently present and u permanently absent. This proves the inherited history without treating a as permanently present.

## 2. Exact ages for the corrected connector

Take a port P=00D1, where D is Dyck of semilength r-1. Write D=1R. Its child image is A=000D11. Replace its outgoing edge by

    A=000D11 -> B=001D10 -> C=011D00 -> E=1110R00.
                                                               (2.1)

The three canonical insertions are the third, second, and first displayed child positions. The deletions are b, a, and the first one d of D. This is the previously proved [corrected three-step connector](Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md), Section 5.

Let alpha be the actual parent age of a at P, and gamma the actual parent age of d. They are positive integers, or may be infinite for a permanent coordinate. The deleted-coordinate ages at the three transitions are exactly

    infinity,  alpha+1,  gamma+2.                       (2.2)

In particular, the connector is residence-three legal **if and only if alpha>=2**. The first deletion is always legal; the last is always legal because gamma>=1. If alpha=1, the second deletion closes a positive run of exactly two states, so no choice of older ages for other coordinates repairs it.

At the new end E, the three newly inserted prefix coordinates have ages 1,2,3 in physical order. Every surviving D-coordinate has its parent age plus three. These are local output-age data, not an automatic continuation certificate.

## 3. Complete inverse classification at P=00D1

Name the first two parent zero positions x,y. All possible containing uppers are P+z with z either x, y, or a zero position of D. The final a is already present and cannot be z. Canonical Phi inverse removes the up-step immediately after the last global prefix minimum, with the empty prefix included.

* **z=x.** The upper is 10D1. Its prefix heights are 1,0, then the nonnegative Dyck profile, and finally 1. Its last global minimum is the height-zero return at the end of D. The following up-step is a. Hence the strict predecessor is 10D0, and its edge to P inserts a and deletes x.
* **z=y.** The upper is 01D1. Its last global minimum is -1 at x, followed by y. The inverse is P itself. This is exactly the excluded Phi self-return.
* **z is a D-zero.** The initial 00 reaches height -2. Until the flipped D-zero, heights are -2 plus the Dyck height; after that flip every remaining D-prefix height is raised by two and is at least zero. The final a ends at height +1. Thus the last global minimum is the last Dyck return of height zero before the flipped position, interpreted also as the empty D prefix. Its following up-step is a one of D, strictly before the flipped zero. Inverse Phi removes that D-one, not a. The predecessor therefore already contains a.

These cases exhaust all containing uppers and all strict predecessors. Consequently, in any specified strict parent factor,

    age_P(a)=1  iff  sigma^(-1)(00D1)=10D0.             (3.1)

Combining (2.2) and (3.1), the connector fails exactly at that named incoming edge. No inference from a mere state count or from independently chosen histories is used. There is no assertion here about how many such edges occur in the supplied factor.

### 3.1. Age two is impossible in every strict factor

In fact, in any strict canonical-Phi factor, the age of a at 00D1 belongs to

    {1} union {3,4,5,...} union {infinity}.             (3.2)

No residence assumption is needed. More locally, two strict incoming transitions suffice to prove that a, if retained on the last edge, was also retained on the preceding edge.

To prove this, suppose the predecessor S retains a. By the complete classification, the incoming upper is B=P+z with z a D-zero, and S=B-v where v is the D-one removed by inverse Phi. The initial 00 and final a are unchanged, so S=00D'1, where D' has equal numbers of zeros and ones. The global minimum of B is -2, and v is the up-step immediately after its LAST attainment. Before v all B-heights are at least -2. At v the B-height is -1, and changing that up-step to a down-step lowers this and every later height by two. Since B never returns to -2 after that last minimum, all resulting heights are at least -3, with equality at v. Therefore S has global minimum exactly -3. Its initial 00 reaches only -2, and its balanced middle word D' has minimum exactly -1.

If a were freshly inserted into S, some containing upper S+t would have inverse Phi delete its final coordinate a. Its last global minimum would then be immediately before a. That prefix has height zero, since the upper ends at height +1 and a is an up-step. Thus every prefix of S+t would have to be nonnegative. If t is not the first initial zero, its first prefix is already negative. If t is that first zero, the upper is 10D'1: its middle word still dips to height -1. Both cases are impossible. Hence every strict predecessor of S already contains a, and the age at P is at least three.

For empty D (r=1), the retained-a branch does not exist and the sole strict arrival has age one, so the age exclusion also holds at that boundary. The nonempty-D connector itself retains its earlier r>=2 assumption.

Consequently the connector test may equivalently be stated as age(a)>=3 on every actual strict parent factor. Its necessary and sufficient numerical deletion-age test remains alpha+1>=3; equation (3.2) explains why equality alpha=2 never occurs at this family of ports. Root proposed this strengthening after the fixed diagnostic observed no age-two ports; the induction agent independently checked the complete two-step proof above.

## 4. Bank disjointness and used uppers

Choose any subset of ports that pass the exact test. Let its size be h, and let M=binom(2r+1,r) be the complete parent lower inventory. Every embedded state has child u=0 and b=1. All three new lower banks B,C,E have b=0, so none belongs to the embedded inventory. Within the new banks their prefixes 001,011,111 distinguish them, and each map from D is injective. The last bank recovers D from E=1110R00 by restoring the deleted first one.

The consumed uppers at A,B,C are

    001D11,  011D10,  111D00.                          (4.1)

The first is the old embedded outgoing upper of A, reused rather than counted twice. The other two have b=0 and are outside the complete embedded upper inventory, which has b=1. They are mutually distinct and injectively indexed by D. Thus no selected connectors collide with each other or with the retained embedded factor, in lower states or consumed upper states.

Removing the selected h outgoing edges and adding the 3h connector edges gives M+3h used lowers and M+2h consumed uppers/assigned edges. It produces h directed paths, plus any original components without selected cuts. The missing incoming heads are exactly 0sigma(00D1)1 for the selected ports; the free outgoing ends are the corresponding E. This is a path bank with inherited boundary histories, not a complete factor.

All selected ports' original histories certify the local age calculation. Once the old cycles are cut, any eventual new incoming connection at a path head must re-establish sufficient capped parent ages and mature b. Those ages cannot be independently assigned for free merely because the old history supplied them before cutting.

## 5. Immediate closing and scope

The free outgoing upper of E is 1110R01: all its old nonempty prefixes are strictly positive, so Phi adds final b. Every missing incoming head has its first two child bits zero. Indeed the first is the fixed u, and the second is the first parent bit, which is zero throughout the containing upper Phi(00D1)=01D1. A rank-(r+1) facet of 1110R01 can delete only one of its first two ones, so it cannot equal any such missing head. Hence the listed paths cannot be closed by directly matching only these free ends to these missing heads.

The result is an exact, testable source-age gate on the supplied nineteen-coordinate factor, with a disjoint connector bank for the passing ports. It does not replace the incoming bad edges, complete a residual matching, supply all unused child states, preserve all-rank interval targets, or prove a twenty-one-coordinate universal word. It is distinct from the 00X11 construction, in which both a and b are permanent and no alpha>=2 test is needed.

Root proposed this actual-parent embedding and the named bad-edge criterion. The induction agent independently checked the complete inverse classification, the exact age equivalence, and the bank accounting. No new finite counts or execution results are claimed in this note.

## 6. Separate fixed-input result and review status

The finite-frontier agent's one bounded h100 diagnostic is recorded in [the 1,371-good / 59-bad certificate](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGES_1371_GOOD_59_BAD_CERTIFICATE_20260909.md). It tested all 1,430 fixed ports of the supplied nineteen-coordinate factor, finding 1,371 legal connectors, 59 age-one failures, and no age-two port. These are counts for that fixed carrier, not general enumerative claims. Section 3.1 independently proves the age-two exclusion for every strict factor.

The induction agent fully read the executed checker and review plan after this run, and passed its complete port inventory, inverse lists, exact cyclic ages, independent finite-history replay, and bank checks. This was a retrospective source audit, not a claimed pre-execution review or a new execution. The certificate's named source and raw-input hashes fix the actual run. No global child completion follows from these checks.
