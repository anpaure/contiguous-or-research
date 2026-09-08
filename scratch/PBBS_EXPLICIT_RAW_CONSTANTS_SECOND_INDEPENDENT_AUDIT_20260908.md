# Second independent audit of the explicit raw-incidence constants

Date: 2026-09-08. Pure proof; no mathematical execution.

Reviewed in full: `PBBS_QUANTITATIVE_CUTOFF_UNIFORMITY_AND_EXPLICIT_CONSTANTS_INDEPENDENT_AUDIT_20260908.md`, Sections 2--7, including its imports from the explicit envelope and coefficient-six finite path comparison. Result: PASS. No numerical change is required to

    E=2^18, B*=64 exp(2E), D*=2^12 exp(2^19),
    J*=2^38 exp(2^19), A0=2^80 exp(2^20)=16J*^2,
    b0=2^-53.

The principal checks were as follows.

1. The envelope tail implies Pr(Q>u)<=exp(12-u^2/4). Tail integration gives E exp(Q^2/8)<=exp(13). The displayed polynomial and Young inequalities give the moment bound exp(32+4t^2); Cauchy--Schwarz then gives exactly exp(22+8t^2-u^2/8) for the truncated first moment. The constants and exponents in both steps are valid.

2. The choice kappa_g=2^-24 satisfies the displayed coarse-profile margin. The small-depth case yields the weaker global h>=2^-25 R/Q with no excluded profiles.

3. In the energy proof, v_s<=8r/(s+1)^2 and a_s<=16/(s+1), with 1-a_s>=1/4, give sum a_s^2<=512. Positive variation is at most four times that sum, so total variation is less than 8192. The logarithmic discrepancy is in fact at most 1026, within the stated 2048. Weighted Cauchy--Schwarz gives the stated 4096 debit.

4. The linear telescoping debit is at most 2064. Replacing a_s a_(s+1) by a_s^2 costs at most 131072. The tail quadratic weight correction costs at most 256. Thus the half-weighted energy debit is at most 68744, plus at most one harmonic-integral discrepancy, below 2^17. Polynomial summation gives the claimed 24rd and 32rd^2 bounds. The reciprocal-denominator correction is at most (96/9)d/r<=16. These estimates rigorously fit E=2^18, and then B* follows with coefficient 128/3<64.

5. At the shorter clock depth, the separate physical-circumference and composition-prefix inequalities hold for every summed path. K0+1<=2(1+H/h); the restricted exponential sum uses z exp(z)<=exp(2z). Hence D* dominating E+24B* is sufficient for both finite probability bounds. This domination holds numerically.

6. D* times 2^26 equals J*. The independent geometric height bound, rather than the shorter clock depth alone, gives H/h<=2^25 bQ and validates that exponent. When the clock depth is below two, the global conditional-probability prefactor exceeds one, so the fallback is valid for every finite r and b.

7. The raw-incidence prefactors are absorbed by A0=16J*^2. The low-height tail coefficient is exactly (2^-25)^2/8=2^-53. If the legal clock depth is below the requested triangle depth, its indicator is bounded by 2^50(b+1)^2 S^2 Q^2/R^2. Multiplying by the global conditional bound produces the same pointwise majorant as the safe-depth calculation; no factor two is necessary. The last polynomial-prefactor logarithm is bounded by 31(b+1)^2, well inside the available 12J*^2(b+1)^2 margin.

The original finite path comparison was checked against its exact source: q_s=ell_s/(p_s+ell_s)=ell_s/(r_s+r_(s+2)+1), and coefficient six follows from the same composition-prefix law with p_s>=2(n_s+W_s). No independent-slot approximation or new reached-root distribution is introduced.

This audit certifies the constants for the three raw estimates in the reviewed note. Assembly with the separate physical-eligibility, vector-coupling, packing, and literal-word compiler proofs is still required for the final quantitative theorem. It does not prove exact equality nu(k)=B(k).
