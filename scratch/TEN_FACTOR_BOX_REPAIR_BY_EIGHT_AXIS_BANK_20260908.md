# A cheaper ten-factor box repair from the verified eight-axis bank

2026-09-08. Pure analytic construction, no computation. Root derivation
and independent appendix-a full audit passed, including uniform finite
errors and the additional accumulator. This improves a local repair ledger. It does
not construct a binary-ten near-cover or improve the unconditional c9.

## 1. Construction and exact limiting charge

Consider one actual product box [s]^10 of ten disjoint-support chains.
Keep eight factors of length s. Partition the product of the remaining
two factors by its complete symmetric chain decomposition, whose lengths
are

    r_j=2s-1-2j,             0<=j<s.

Their sum is s^2. For each such ninth chain use the fourteen-row
eight-axis staircase bank and its exact sacrificial-chain absorption
from SACRIFICIAL_ACCUMULATOR_EXACT_ABSORPTION_20260908.md. If s is odd,
pad the eight principal chains to the next even length by repeated
members, paying only lower-order terms. Its limiting principal charge
per volume, with eight equal lengths a and ninth length r, is

    F(a,r)=alpha/(2a) [1+E min(1,aT/r)],
    alpha=35/32,            T=1+U_1+U_2+U_3,

where the U_i are independent Uniform[0,1]. This formula is an exact
asymptotic deterministic inventory of the bank, not an assumption about
random chain lengths. All indexed chain occurrences remain charged.

Summing its complete paired-rectangle charge over the displayed SCD
therefore gives

    P_10(s) <= (gamma_10+o(1))s^9,
    gamma_10 = alpha/2 [1+E min(1,T/R)],             (1)

where R has density r/2 on [0,2], independently of T. Indeed
sum_j (r_j/s^2) f(r_j/s) tends to integral_0^2 (r/2)f(r)dr;
this is the size-weighted chain-length inventory of [s]^2.

All finite rounding and bridge corrections are lower order. With half
length u, let V=5u^4 and R_0=u^3. The exact raw component charge is
14V[r_j R_0+sum_L min(r_j,L)], with indexed staircase lengths
L=8u-3-2(j_2+j_3+j_4). The min function is 1-Lipschitz, so its
three-dimensional grid average differs from its continuum average by
O(1), uniformly for 1<=r_j<=2s. The resulting component error is
O(s^7). The complete A.24 bridge overhead is also O(s^7) per component.
Summing over s components gives O(s^8). Odd-s padding has that same
order. Tiny r_j introduce no singularity in these finite inventories.

## 2. Elementary exact integral

Only 1<T<R<2 contributes to the deficit from min(1,T/R)=1. On [1,2],
the density of T is (t-1)^2/2. Consequently

    E(1-T/R)_+
      = integral_1^2 [(t-1)^2/2]
                    integral_t^2 [(1-t/r)r/2] dr dt
      = (1/8) integral_0^1 u^2(1-u)^2 du
      = 1/240.

Substituting into (1) proves

    gamma_10=(35/32)(1-1/480)=16765/15360.           (2)

This is strictly below the earlier 5+5 product-SCD coefficient 115/96.
The saving is 1635/15360=109/1024 in the s^9 coefficient.
The bound remains above the centered-rectangle lower coefficient
23771/22680, so it does not contradict that restricted-class barrier.

## 3. Conditional binary-ten transfer and scope

For a literal m-row balanced binary-ten bank with b missing patterns,
repair each missing [s]^10 macrocell by the construction above. Absorb
the eleventh accumulator into one shore of every indexed rectangle.
An actual product SCD with a chain of length r multiplies membership by
r and increases the chain count by at most r, so the principal repair
charge is at most r P_10(s). The same volume normalization and complete
Euler bridge accounting as in
BINARY10_PARTIAL_MACRO_COVER_REPAIR_LEDGER_20260908.md give

    coefficient <= [12m + b(16765/15360)] beta_11/512.             (3)

There is no extra complement saving: the macrocell convention and pivot
folding are exactly those of the existing ledger. All target witnesses
remain internal to their paired-chain gadgets.

Thus a 42-row bank with one hole would have a slightly better conditional
coefficient than the previous one-hole theorem. No such bank is supplied.
Two separately repaired holes still cost 33530/15360>2.18, whereas the
available repair allowance is 2.0448919776.... This construction does
not pass the two-hole improvement gate.

The inequality concerns a reusable local full-box cover. It makes no
claim that arbitrary holes can share its charge or that the record has
changed.
