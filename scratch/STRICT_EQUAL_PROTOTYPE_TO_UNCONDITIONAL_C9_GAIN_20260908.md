# A strict equal-length prototype would improve c9 unconditionally

2026-09-08. Pure conditional construction; no computation. Root and independent
direct-route full audits passed. The antecedent is an actual finite chain
certificate, not a rank bound. No certificate satisfying it is asserted.

## 1. Precise sufficient antecedent

Put alpha=35/32. Suppose a fixed literal prototype and the proved grid
inflation give, on every nine-fold equal product of length a in a fixed
integer progression, a complete paired-chain cover with principal
charge

    kappa a^8,              0<kappa<alpha,           (1)

and compiler overhead O(a^7). All targets have witnesses internal to
the paired gadgets, all child chains are retained, and membership is
charged with its indexed multiplicity. The successful finite weighted
gate in `GRID_CHAIN_INFLATION_FOR_ASYMMETRIC_STAIRCASE_20260908.md`
would supply exactly this antecedent; its pair count is O(a^7), so the
accepted A.24 row compiler supplies the required overhead.

Then a deterministic construction has asymptotic coefficient strictly
below c9. It does not need a limiting joint law for the active ninth
radius or an explicit excursion/resolvent formula.

## 2. Padding and contraction for arbitrary nine lengths

Sort the actual lengths as r<=a_1<=...<=a_8 and let A be the least
allowed prototype length not below a_8. Pad EVERY factor to A by
repeating its last member, including the shortest ninth factor. Apply
the inflated prototype in these formal indices, map each chain to its
actual sets, and remove consecutive repetitions inside its image.
The index map is monotone and surjective. These image chains cover
the full actual product, remain nonempty and strict, and have no larger
individual length. Keep all indexed chains even when some coincide.

Thus the candidate principal charge is at most kappa A^8, with the
same O(A^7) upper overhead. The actual volume is r product_i a_i;
there is no change to its denominator. Use this candidate only when
it is cheaper than the existing A.7 staircase/line construction.

For fixed prototype modulus, rounding A changes the unrounded degree-
eight charge by O((1+a_8)^7). It is lower order in the existing fixed-
number-of-input-factors transfer, exactly as A.7's even rounding.
The continuum normalized candidate and old bounds are consequently

    F_new=min(F_old, kappa a_8^8/(r product_i a_i)),
    F_old=min(alpha a_8^7/(product_i a_i),
                                      1/a_7+1/a_8).             (2)

The unweighted minimum remains continuous even at zero lengths after
multiplying by actual volume. The old line upper bound still dominates
F_new, so the original reciprocal-integrability and fixed-factor
Riemann-limit argument applies without a new singular estimate.

In particular the candidate-to-staircase ratio is exactly

    (kappa/alpha)(a_8/r).                           (3)

At limiting equal charged radii A, it is cheaper whenever r/A>kappa/alpha.
This comparison uses a crude formal membership upper bound; no saving
from deduplicating different image chains is needed.

## 3. Uniform positive mass of nine comparable current radii

Use the same nine independent three-dimensional Brownian paths and
minimum-radius mesh updates as A.7.5. Let their allocated times be
t_1,...,t_9; at the terminal step their sum is one. Fix eta>0 and the
event

    E_eta={sup_(0<=t<=1) |B_i(t)-9t e_1|<=eta
                                         for every i=1,...,9}. (4)

Its probability p_eta is strictly positive, independently of the mesh
size M; an elementary proof is in Section 5 below.

On this event, the radius at local time t differs from 9t by at most
eta. If the next update chooses i, the minimum rule gives

    9t_i-eta <= |B_i(t_i)| <= |B_j(t_j)| <=9t_j+eta

for every j. Immediately after advancing its clock by 1/M, its excess
over every other clock is at most 2eta/9+1/M. Induction from equal zero
clocks therefore bounds the entire clock spread by that quantity at
every step. At the terminal time, every clock is within that spread of
1/9. Hence every CURRENT terminal radius lies in

    [1-3eta-9/M, 1+3eta+9/M].                       (5)

For M sufficiently large this is contained in [l,u], where
l=1-4eta and u=1+4eta. This includes the currently active shortest slot;
the argument does not substitute historical maxima for current radii.

## 4. A strictly positive expected saving

Choose eta>0 so small that l>0 and

    theta=kappa u/(alpha l)<1,
    alpha (u/l)^8<2.                               (6)

This is possible because kappa<alpha<2. On E_eta and for all sufficiently
large M, the staircase term in (2) is smaller than the line term:
the former is at most alpha u^7/l^8, while the latter is at least 2/u.
Equation (3) then bounds the candidate by theta times the old bound.
Also the old staircase bound is at least alpha/a_8>=alpha/u. Therefore

    F_old-F_new >= d:=(1-theta)alpha/u>0
                         on E_eta,                (7)

and F_old-F_new>=0 everywhere. Thus, under the same Brownian coupling,

    E F_new <= E F_old-p_eta d                     (8)

for every sufficiently large mesh size M. There is no interchange of
an unproved joint limiting distribution in this inequality.

The fixed-M deterministic product-SCD transfer of A.7 multiplies these
expectations by sqrt(pi/8). The old coefficients converge to c9.
Choose one sufficiently large but FIXED M so that its old coefficient
is less than c9+sqrt(pi/8)p_eta d/2. For this M, (8) and the existing
all-dimension passage give

    limsup_(k->infinity) nu(k)/W(k)
       <=c9-sqrt(pi/8)p_eta d/2<c9.                 (9)

The right-hand improvement need not be practically large. It is a
strict unconditional consequence of the explicit finite antecedent (1).

## 5. Elementary positivity of the Brownian tube

Here is a direct proof of p_eta>0 without a drift-change theorem. Set
b=eta/(4 sqrt(3)), and partition [0,1] into N equal intervals of length
h=1/N, with N sufficiently large. At each grid time require each
coordinate's error from 9t e_1 to lie in [-b,b]. Conditional on any
such current error, the Gaussian next increment has probability at
least 1/4 per coordinate of returning its error to [-b,b], uniformly
for all sufficiently small h: the worst interval is displaced from a
half-line boundary by only 9h=o(sqrt(h)), and its opposite boundary is
at distance 2b from that boundary. This also follows directly by
integrating the Gaussian density over [9h,b] and using symmetry.

The three coordinates are independent, so the endpoint event has
probability at least 1/64. The reflection bound gives probability at
most 12 exp(-2b^2/h) that any coordinate's Brownian increment exceeds
2b in absolute value anywhere inside this interval. Choose h so small
that this bound is less than 1/128 and 9h<=b. The endpoint-and-path
event then has conditional probability at least 1/128.

On it, the error inside the interval is at most b+2b+9h<=4b in every
coordinate, hence at most eta in Euclidean norm. Independent future
increments and induction over the N intervals show that one Brownian
path follows the tube with probability at least (1/128)^N. Independence
of the nine paths gives p_eta>=(1/128)^(9N)>0. Only positivity is used.

The active-ratio resolvent law may give a much better quantitative mass,
but no such identity is necessary for (9). The current unresolved work
is entirely the actual chain/prototype antecedent (1); a favorable
rank polynomial alone does not establish it.
