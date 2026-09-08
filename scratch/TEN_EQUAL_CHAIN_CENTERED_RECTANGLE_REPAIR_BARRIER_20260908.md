# A centered-rectangle obstruction for one ten-factor microbox

2026-09-08. Pure proof with a bounded exact-arithmetic check on h100. This is a lower bound for the complete centered product-SCD terminal-rectangle ledger, not for unrestricted OR words or overlapping covers.

## 1. Statement and scope

Start from ten coordinate chains, each of length s. Refine their product by complete centered product SCDs, permitting every subsequent pair or group choice to depend on the current child tuple. Retain every child, stop at two chains per leaf, and let

    P = sum over terminal rectangles (a+b)

be the principal charge. Then, uniformly over all such refinements,

    liminf_(s -> infinity) P/s^9 >= 23771/22680
                                   = 1.0481040564373898... .

In particular this class cannot repair a single [s]^10 microbox with principal coefficient below 1.02244. Two separately repaired microboxes have total coefficient at least

    23771/11340 = 2.0962081128747796...,

which exceeds the proposed total patch allowance 2.04489.

The class includes the entire adaptive recursion in recursive_scd_coalescent_20260905_f6b82.py and Section 3 of GENERAL_D_BLOCK_AND_RECURSIVE_SCD_LIMITS_20260905_f6b82.md. It does not include overlapping staircase covers, moving-center refinements, or leading-order sharing of positions between terminal rectangles or the two microboxes.

## 2. An exact finite rank dual

Write

    N_s(q) = [x^q](1+x+...+x^(s-1))^10,
    n=10(s-1),       q_*=4s-4,       R=2s-1,

and set N_s(-1)=0. The exact finite lower bound is

    P >= 2s [N_s(q_*)-N_s(q_*-1)] + 2N_s(q_*-1).       (1)

To prove it, complete every terminal rectangle (a,b) by one final product SCD. Its child lengths are

    |a-b|+1, |a-b|+3, ..., a+b-1.

All children of the completed full product have odd length because n is even. For one terminal rectangle,

    a+b >= (R+1) 1{a child of length R occurs}
             + 2 #{children of length greater than R}.          (2)

If R is a child length, the right side equals a+b. If R lies below all children, the right side is 2min(a,b), which is at most a+b. If R lies above all children, it is zero. These cases are exhaustive.

Every complete centered refinement gives a centered SCD of the original full product after the final merges. Its chain-length inventory is determined solely by the rank polynomial. A chain of length R starts at rank

    (n-R+1)/2=4s-4=q_*,

so the number of such chains is N_s(q_*)-N_s(q_*-1). Chains longer than R start at smaller ranks; their total number telescopes to N_s(q_*-1). Summing (2) proves (1). Thus the bound is independent of the adaptive policy and does not require a uniform convergence theorem for a Bellman recursion.

## 3. Exact asymptotic coefficient

Inclusion-exclusion gives

    N_s(q)=sum_(j=0)^10 (-1)^j C(10,j) C(q-js+9,9),

where a term is zero if q-js<0. Its consecutive difference is

    N_s(q)-N_s(q-1)
      =sum_(j=0)^10 (-1)^j C(10,j) C(q-js+8,8).

At q=q_*=4s-4, division by s^9 and s^8 respectively gives the leading coefficients

    f_10(4)  = [sum_(j=0)^3 (-1)^j C(10,j)(4-j)^9]/9!
              =44117/181440,

    f'_10(4) = [sum_(j=0)^3 (-1)^j C(10,j)(4-j)^8]/8!
              =809/2880.

The same f_10(4) is obtained from N_s(q_*-1)/s^9. These are finite polynomial asymptotics, with error O(1/s) after normalization. Dividing (1) by s^9 therefore proves

    liminf P/s^9 >= 2f'_10(4)+2f_10(4)=23771/22680.

Equivalently, f_10 is the density of the sum of ten independent Uniform[0,1] variables. The general squared-interval dual from Appendix A.6 would give, at threshold a>0,

    gamma_d >= a f'_d((d-a)/2)+2f_d((d-a)/2).

The proof above is its exact finite specialization d=10,a=2 and avoids interval-endpoint conventions entirely.

## 4. Computational check and implication

One Python Fraction calculation was run exclusively through ssh h100. It verified the two displayed rational coefficients, their sum, and its strict comparison with 1.02244. No dynamic programme, Monte Carlo calculation, or solver search was run: the analytic lower bound already excludes the requested coefficient throughout the specified recursion class.

This rules out patching the two omitted binary macrocells independently by optimizing only complete centered recursive SCDs. It leaves open a cover that repairs them jointly, shares leading-order positions with existing rows, or uses a different overlapping or noncentered microbox construction.
