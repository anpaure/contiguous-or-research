# Exact beta-threshold comparisons and the elementary composition lower bound

Date: 2026-09-08. Status: the four requested rational comparisons pass;
the composition inequality has the direct proof below.

This is an audit of the displayed finite expressions. It does not itself
establish their proposed connection to an OR-word bound, prove monotonicity
over every dimension, or verify the separately reported 24,715-letter word,
whose body was not supplied to this task. No construction search was run.

## 1. Four exact rational comparisons

For odd n define

    W=binom(n,(n-1)/2),
    beta_n=4n(n+1)(242/243)^n+n(99/100)^n,
    R(n)=(2^(n+2)+2W)/(n^2 W)+beta_n.

One bounded h100 process formed these expressions with exact integers and
reduced rational arithmetic at n=5641,5643,6253,6255. For a threshold 1/q,
it checked the exact integer sign of q times the reduced numerator minus
the reduced denominator. No floating-point approximation was used.

It also obtained the following rational enclosures. Each listed decimal
is an exact lower endpoint; the upper endpoint is the lower endpoint plus
10^-24 and is strict.

| n | Exact rational lower endpoint for R(n) | Certified comparison |
|---:|---:|:---|
| 5641 | 0.010065906889287253783526 | R(n)>1/100 |
| 5643 | 0.009990393077418169965223 | R(n)<1/100 |
| 6253 | 0.001000477920417412307465 | R(n)>1/1000 |
| 6255 | 0.000992967613437660795735 | R(n)<1/1000 |

Consequently the requested comparisons hold, with strict inequalities on
both sides:

    R(5641)>0.01>R(5643),
    R(6253)>0.001>R(6255).

The certificate retains the complete exact reduced numerator and denominator
of each R(n), the exact comparison sign, and both enclosure endpoints as
integer numerators over 10^24. These are reproducible rational checks,
not printed quadrature values or assumed numerical thresholds.

## 2. Composition count: a proof requiring no enumeration

Let p and ell be integers satisfying

    p>=9n/22,   ell>=n/33,
    D=binom(p+ell-1,p-1),

on the claimed domain of odd n>=5. Put q=ceil(n/33). Since n>=3,

    9n/22-1-n/33=25n/66-1>=0.

Therefore p-1>=n/33. The integer p-1 must then be at least q, and the
integer ell is also at least q. Binomial coefficients binom(a+b,a) are
nondecreasing in each of the nonnegative integers a,b, so

    D=binom((p-1)+ell,p-1)>=binom(2q,q)>=2^q>=2^(n/33).

For the middle inequality, partition a set of 2q elements into q pairs.
Choosing exactly one member of each pair gives 2^q distinct q-subsets.
This proves the composition inequality exactly. In fact the proof works
for every integer n>=3 under the stated p,ell bounds; the requested odd
n>=5 domain is contained in it.

## 3. Artifacts, limits, and scope

The exact checker is

    scratch/check_pbbs_beta_rational_thresholds_20260908.py.

The complete rational certificate is

    scratch/pbbs_beta_rational_threshold_certificate_20260908.json.

The only mathematical process ran on h100, with output under

    /home/amodo/exact-b-pbbs-beta-thresholds-20260908/.

It had limits of 30 CPU seconds, 45 wall seconds, and 512 MiB address space,
and returned PASS. The integer-to-decimal conversion limit was explicitly
lifted only to retain the full rational certificate; arithmetic stayed exact.

No other dimensions were enumerated, no word construction or deletion was
attempted, and no optimality or all-dimension threshold claim follows merely
from these four adjacent comparisons. Those broader deductions belong to
the separately audited general proof.
