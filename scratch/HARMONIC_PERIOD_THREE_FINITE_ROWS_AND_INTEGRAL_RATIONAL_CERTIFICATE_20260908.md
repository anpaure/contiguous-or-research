# Exact outward-rational certificates for the harmonic-period numbers

2026-09-08. Bounded numerical audit by `exact_b_induction`. All three
specified finite rows, the specified integral lower sum, and the two
coefficient comparisons pass. Only those parameters were evaluated.
This note certifies the numerical inequalities; the probabilistic
finite theorem supplying the four terms is a separate proof interface.

## 1. The three finite certificates

Set delta=1/10, z=M, Q_r=4(r+1)sqrt(r), and

    A_z = 1 + sum_(prime p<=M) log(p)/(p-1),
    rho_s = (1001/1000)(s+2)^(3/2) / [2 sqrt(pi*(9r/10))],
    y_s = (36r/10)/(s+2) - (22r/10)/(s+3) + 1,
    b_s = min(1,(A_z+M*rho_s)/log(y_s)).

For each of the following rows, the exact outward arithmetic proves

    Q_r(1+M) product_(s=0)^(L-1) b_s < (1/4)10^(-d).

| r | L | M | d | Proved upper bound on log[4*10^d*Q_r(1+M)*product b_s] |
|---:|---:|---:|---:|---:|
| 10^12 | 1,100 | 790 | 330 | < -24 |
| 10^14 | 3,500 | 2,250 | 950 | < -72 |
| 10^16 | 10,200 | 6,150 | 2,600 | < -142 |

The full certified upper bounds, each a rational with denominator
10^40, are respectively

    -24.1840237529594175045481551914158591044930
    -72.2204447174243510930589234706348645166557
    -142.4158463321439232983265775716796812694773

The required finite guards also pass in all three rows:

    delta*sqrt(r)/(L+2) >= 4,
    (18r/10)/(L+2)^3 >= 1000.

For each remaining term C exp(-E), the program proves

    E - log(4C) - d log(10) > 0.

Its three (C,E) pairs are exactly

    (4 sqrt(r), M),
    (2(L+1), (delta*sqrt(r)/(L+2)-4)^2/6),
    (Q_r L(3r+1), (36r/10)/[3(L+2)^3]).

For concise display, the following integer lower bounds are weaker
than the saved certified rational margins:

| r | Short-period margin | Depth margin | Nonprimitive-row margin |
|---:|---:|---:|---:|
| 10^12 | >13 | >485 | >56 |
| 10^14 | >43 | >11,014 | >513 |
| 10^16 | >142 | >152,829 | >5,209 |

Thus each of the four terms is strictly below (1/4)10^(-d), and their
sum is strictly below 10^(-d). This conclusion is the direct numerical
consequence of the specified four-term expression; it introduces no
new conditioning or period assumption.

## 2. Why the logarithms and square roots are rigorous

All arithmetic used in the inequalities is integer or rational. The
working scale is B=10^40. A stored lower or upper integer represents
that integer divided by B. Mathematical premises do not use binary
floating point, quadrature, or a library logarithm.

For a positive rational x, exact powers of two normalize it as
x=2^e u with 1<=u<2. With y=(u-1)/(u+1),

    log(u) = 2 sum_(j=0)^63 y^(2j+1)/(2j+1) + remainder,
    0 <= remainder <= 3^(-128),

because 0<=y<=1/3 and the positive series tail is bounded by its first
term times 1/(1-y^2). Each multiplication and division in the truncated
positive sum is rounded down for the lower enclosure and up for the
upper enclosure. The explicit remainder is added to the upper bound.
The same series encloses log(2). Multiplication by a negative exponent
e correctly interchanges its lower and upper contributions.

Pi is enclosed using Machin's identity

    pi=16 atan(1/5)-4 atan(1/239).

Each arctangent uses 64 alternating rational terms. Every individual
term is rounded outward, and the next positive term bounds the
remainder because the even-length partial sum is below the arctangent.
The negative coefficient -4 uses the opposite arctangent bound.

To obtain an upper rho_s bound, replace pi by its positive lower
enclosure and compute the ceiling of B times the resulting square root
using `isqrt` and exact integer-square comparisons. In particular, the
program verifies both the claimed ceiling and the failure of the next
smaller integer to be a valid upper bound.

A_z is rounded up, rho_s is rounded up, and log(y_s) is rounded down.
Their ratio therefore gives an upper bound for b_s, after applying the
monotone cap min(1, .). The logarithm of that upper bound is itself
rounded up. Adding these upper logarithms, log[4Q_r(1+M)], and d log(10)
proves the product inequality without forming a giant product.

For the other terms, E is retained as an exact rational. The verifier
rounds E down and both logarithms up. A positive resulting margin is
therefore a valid strict lower bound.

## 3. The integral certificate is reproduced exactly

Consider

    I = integral_(0)^(25/16) -log(251/1000+(19/50)t^(3/2)) dt.

The integrand is positive and decreasing on this interval. Use the
right endpoints t_i=(i/1000)^2 for i=1,...,1250. At those endpoints,

    q_i = 251/1000 + 19i^3/(50*1000^3),
    delta t_i = (2i-1)/10^6.

Each q_i lies strictly between zero and one. The positive logarithm
series gives

    -log(q_i) > sum_(j=1)^32 (1-q_i)^j/j.

Every cell contribution formed from that rational partial sum is
rounded down separately to a multiple of 10^(-18). The exact sum of
those 1,250 rounded cells is

    1074181933864880728 / 10^18
      = 1.074181933864880728.

This is exactly the proposed integer numerator, not merely a nearby
floating-point value. It exceeds 1073/1000 by

    147741733110091 / 125000000000000000 > 0.

The monotone right-endpoint inequality and the strictly positive
omitted logarithm terms therefore prove I>1073/1000. Every rounded
cell is saved for replay.

## 4. The two additional exact comparisons

The squared coefficient in the proposed bound is exactly

    [(1.001*1.07)/(0.7999*2*sqrt((157/50)*0.99))]^2
      = 26072521475 / 180818786826.

Its distance below (0.38)^2 is exactly

    47139178343 / 226023483532500 > 0.

Also

    (930/1069)^5 = 695688369300000 / 1396009989636349,

whose distance below 1/2 is exactly

    4633251036349 / 2792019979272698 > 0.

Both checks use rational comparisons after squaring positive quantities;
no square-root approximation is needed for these two comparisons.

## 5. Artifacts and scope of execution

Program:

    scratch/verify_harmonic_period_three_rows_and_integral_20260908.py

Complete report:

    scratch/harmonic_period_rational_certificates_20260908/rational_certificate_report.json

The 1,250 downward-rounded cell numerators:

    scratch/harmonic_period_rational_certificates_20260908/integral_1250_downward_cells.json

Remote output directory:

    /home/amodo/harmonic-period-three-rows-20260908/

One h100 execution completed all specified checks, made 30,860 calls
to the rational logarithm enclosure, and exited 0 in 1.084 seconds.
It enforced 120 CPU seconds, 150 wall seconds, and 2 GiB address space.
No parameter search or extra finite row was run, and no process remains
live. Timing is descriptive only and is not a mathematical premise.

This is an exact arithmetic certificate with a documented enclosing
method. It is not external or proof-assistant certification of the
surrounding probabilistic theorem.
