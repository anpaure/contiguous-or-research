# Independent audit of the entrance/exit capacity theorem

Date: 2026-09-08. Reviewer: Codex subagent exact_equality_structure.

Source reviewed in full:

    scratch/EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md

Verdict: the stated necessary-condition theorem and its induction
obstruction are valid. This was a proof review, not an independent replay
of the numerical table. No new equality construction is supplied.

1. At a fixed cut c, every crossing old projection is L_i union R_j.
   Adjoining P_(c+1) to L_i leaves this union unchanged. The modified left
   states form one nested chain with minimum C_c=P_c union P_(c+1), so at
   most [r-|C_c|+1]_+ such states can have rank at most r. For each left
   state, the right states give a nested union chain with at most one
   distinct rank-r output. This proves the fixed-cut bound. Neither
   disjointness nor unit rank increments are needed.

2. A selected tagged-target witness either starts at a tagged position or
   starts untagged and crosses an entrance. The former class has at most
   h_z distinct targets because a fixed start supplies a chain of old
   projections. Charging the latter to its first entrance is well-defined
   and the fixed-cut lemma bounds each charge class. The classes exhaust
   the witnesses, proving the entrance inequality. Applying exactly the
   same argument to the reversed physical word proves the exit inequality.

3. At a tag-transition cut the untagged neighboring letter is nonempty and
   remains nonempty after projection, so |C_c|>=1. Therefore the per-cut
   capacity is at most r. This is where nonzero physical letters are used.

4. Deleting every tagged letter preserves all targets disjoint from z:
   their original witnesses contain no tagged letter. The surviving
   subsequence is universal in the old dimension and has at least B(k)
   letters. Hence h_z<=N-B(k), exactly as used in the bound.

5. For old dimension 2r, the binomial identity

       W(2r+1)=2 W(2r)-Cat_r

   gives the claimed exact gap Cat_r+d_(2r)-d_(2r+1). The O(sqrt(r))
   correction is negligible compared with Cat_r, so the exponential
   entrance/exit lower bound follows from the existing Catalan estimate.

6. A tagged run lacks an entrance exactly when it meets the first physical
   position, and lacks an exit exactly when it meets the last. The maximum
   of those two endpoint indicators gives the stated run correction.

The claim that a fixed or polynomial number of tagged intervals cannot
support exact induction in every odd dimension follows. The theorem does
not preclude a construction with exponentially many interleaved tagged
runs, does not compare finite upper bounds from such a construction, and
does not prove nu(k)>B(k).
