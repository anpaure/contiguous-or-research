# Independent audit of full upper preservation by the all-r short-sector path

Date: 2026-09-08.

Reviewed:

- `PBBS_GLOBAL_CORRIDOR_HEIGHT_AND_SHORT_SECTOR_FULL_UPPER_PRESERVATION_20260908.md`;
- `PBBS_ALL_R_SHORT_SECTOR_FIRST_UPPER_RANKS_PRESERVED_20260908.md`;
- the imported corridor in `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Section 21;
- the explicit q2 height construction in `MATH_ATTACK_Y12_DIRECT_ALL_DEPTH_PBBS_DYCK_GATE_20260725.md`, Section 4, and its occurrence theorem in `MATH_THEOREM_PBBS_MAX_HEIGHT_Q1_SECTION_IS_Q2_COMPLETE_20260805.md`;
- the explicit invariant sector in `PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md`.

Result: PASS by independent pure proof. No new mathematical computation was run and no earlier bounded computation is a premise of this audit. The result is full upper-target support for the specified mixed path/cycle family, not a single optimal word and not nu(k)=B(k).

## 1. The corridor-height kernel is valid

Let S have rank r-q on n=2r+1 positions. Repeated reverse cancellation of adjacent 01 pairs leaves 2q+1 unmatched zeros. Each finally unmatched zero is present throughout the cancellation. It is therefore a permanent barrier: two symbols in different intervening open arcs can never become adjacent across it and cancel. Every symbol in an open arc between successive surviving zeros must eventually cancel inside that arc, since no other final survivor lies there. Thus every such arc has equally many zeros and ones.

Choose q consecutive reverse-unmatched marks C_0,...,C_(q-1) and flip them to ones. In the resulting rank-r set B, the cyclic interval from C_0 through C_(q-1) consists of the q flipped marks and q-1 balanced intervening arcs. Its increment is exactly q. There are q+1 unchosen surviving marks outside this interval, so this is an interval of fewer than n positions, not a multiply wrapped walk.

For any rank-r set B, normalize its cyclic binary word to 0D, where D is Dyck, and let H be the height of D. An interval inside D has increment at most H, because it is a difference of prefix heights in [0,H]. An interval crossing the distinguished zero has increment -h_start-1+h_end<=H-1. The full circle has increment -1. Conversely a prefix ending at a maximum of D attains H. Therefore H is exactly the maximum cyclic interval increment, and the displayed interval proves ht(B)>=q.

This applies to the actual initial state B_0 in the established global-maximum corridor: that state is S together with precisely q consecutive reverse-unmatched zeros. The existing corridor theorem supplies the literal canonical g=f^2 edges and the exact q+1-state intersection S. The new height calculation thus applies to an actual witness, not an arbitrary completion of S.

For q>=3, B_0 has height at least three and cannot be in the removed sector, whose roots all have height two. The sector is explicitly invariant under f, hence under the finite permutation g. Its complement is therefore invariant as well. Every state and edge of the corridor remains in an untouched component. No additional theorem asserting height conservation for every PBBS state is needed for this conclusion.

The boundary q=r is covered: S is empty, B_0 has height at least r, and the exact corridor intersection is empty, yielding the full upper target after complementation.

## 2. The q2 height-three backup is a valid import

For |S|=r-2 and r>=3, forward cancellation gives five Dyck blocks D_i between unmatched zeros. At least one block is nonempty, so their maximum height H is at least one. Choose a tallest block and the down-step u immediately after its rightmost maximum. Changing u to an up-step makes that block a nonnegative ballot path of final height two and maximum H+1.

The explicit construction adds the unmatched zero immediately before the chosen block as another one. In the normalized root of the resulting rank-r state A, the central primitive is

    1 D_i^up 0 D_(i+1) 0 D_(i+2) 0.

Its maximum is exactly H+2: the changed step u first reaches that level, and the following block baselines cannot exceed it. Every exterior primitive has height at most H. This is the construction stated and proved in the imported Y12 Section 4; its distinguished-deletion identities give

    g^(-1)A intersect A intersect gA = S.

Thus A has height at least three and this whole witness lies outside the invariant removed sector. Ties among tallest original blocks cause no problem: the new central primitive is strictly taller than every exterior primitive.

## 3. Immediate-upper q1 recaptures check in every phase

Put M=r-2. Use the explicit lower-owner parity sets A_b,B_b,C_b from the first-upper-ranks note and f^3=rho. For b>0, the cut edge has tail f^(t_b)A_b, with t_b=4n-2b-2. Reducing t_b modulo three gives the deleted colors

    phase 0: A_b minus {2b+1},
    phase 1: B_b minus {2r-1},
    phase 2: C_b minus {0}.

These follow directly by intersecting A_b with C_b, B_b with rho A_b, and C_b with rho B_b, respectively.

In phase zero the following seam exists and its unrotated color is A_b intersect A_(b+1)=A_b minus {2b+1}. The final nonzero block is always phase two, so the claimed following seam is never missing in this case.

In phase one with b>=2, the preceding seam is at time t_b+2. The identities

    A_(b-1) intersect A_b = A_b minus {2b},
    rho(A_b minus {2b}) = B_b minus {2r-1}

prove exact recapture after restoring the common rotation. For b=1, the proposed edge in block zero has the correct color because A_1 minus {2}=A_0 minus {1}. Its color has cyclic zero-gap types two and three, while the color cut from block zero has one zero gap of length four. These patterns cannot coincide under rotation; hence the particular backup edge is not the removed edge.

For phase two define

    K_b=evens[2,2b] union odds[2b+3,2r-3] union {2r}.

The coordinate map on rooted defect-one states is

    g(x,y,z,u)=(z,x,y,u+2(x+y+2)) modulo n.

For b>=2, expansion of the root (b-1,M-b,1,1) gives exactly K_b union {2b+1}; its image is (1,b-1,M-b,2r-1), which expands to K_b union {1}. All three coordinates are positive since 2<=b<=M-1. This is a canonical edge in an untouched interior component, including the possible equal-coordinate interior case.

For b=1 and r>=5, the root (r-4,1,1,4) expands to K_1 union {2r-2}; its image (1,r-4,1,1) expands to K_1 union {4}. Again all triple coordinates are positive. The exceptional r=4 case has K_1={2,5,8}, of spatial period three. Since its component has length 27 and f^3=rho, rotations by three and six supply two further distinct occurrences of the same edge color in that component. One cut cannot remove all three occurrences. At r=3 there is no nonzero block.

Finally, the block-zero cut has color K_0=odds[1,2r-3]. The states K_0 union {2r} and K_0 union {2r-1} belong to the height-one all-unit component and are related by its g action, a spatial rotation by two. Their edge is untouched.

These cases exhaust every deleted q1 edge. All uncut old q1 edges remain present, proving full immediate-upper support after complementing the lower colors.

## 4. General conclusion and its boundary

The all-r explicit path retains every bad-sector owner exactly once. Immediate-upper targets have the q1 recaptures above. Every next-upper target has the height-at-least-three q2 witness. Every higher target has the actual height-at-least-q corridor witness, entirely outside the removed sector. These cases cover all ranks r+1 through 2r+1 for every r>=3.

Therefore the explicit short-sector path, together with every other canonical component left intact, preserves the complete upper target support. The argument supplies a genuine all-r replacement for the earlier bounded r<=8 upper census.

It does not prove that the remaining cycles can be cut and fused while preserving that support, that their lower source caps can be assigned simultaneously, or that the final source can attain B(k). Those remain separate construction requirements. The already completed k17 475/849 surgeries also require their own transport certificates; they are not automatic consequences of this all-r short-sector theorem.
