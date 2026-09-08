# Exact symmetry-signature recursion and the nonprimitive top-row generating function

2026-09-08. Independent pure-proof audit by `exact_b_induction` of
`SYMMETRY_DESCENT_UNIFORM_THRESHOLDS_USER_CLAIMS_20260908.md`.
No mathematical execution or census rerun was performed. Verdict:
the exact (Q,U) recursion, its minimality and odd periods, the ordered
row Möbius count, and the bound b_r<=43(25/9)^r all **PASS**.

This audit uses the already proved one-level translated-return
equivalence and original rooted inverse-pruning bijection. It does
not by itself certify the separate four numerical envelope values
or their finite-to-infinite thresholds.

## 1. Why a unique signature exists

Let A be a rank-r physical word on n=2r+1 sites. Use positive physical
rotation rho^u and the canonical PBBS map f. These maps commute.
Define

    Gamma(A)={(t,u) in Z^2: f^t(A)=rho^u(A)}.

This is a subgroup of Z^2. Its projection to the time coordinate
contains the positive full period, so it is QZ for a unique Q>=1.
For a given admissible time, the translation is unique modulo n:
a nontrivial rotational stabilizer would force a repetition length
dividing both n and r, while gcd(n,r)=1. Choose the unique U with
0<=U<n and (Q,U) in Gamma. Then

    Gamma(A)={(jQ,jU+kn): j,k in Z}.                     (1.1)

The full labelled period is therefore

    F=Q*n/gcd(n,U).                                     (1.2)

For the one-site zero word, the correct base signature is (1,0).
Its full period is1 and every integer translation fixes it.

## 2. Derivation and minimality of the parent recursion

Consider a parent of circumference n, child circumference p, and
original gap-row least period d|p. Suppose the child's exact signature
is (Q,U). The one-level theorem proved in
`PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md`
states that a parent translated return (t,u) is equivalent to

    m=(t-pu)/n integral,
    d divides m,
    (t,-m) in Gamma(child).                             (2.1)

The sign is important: positive physical parent rotation u corresponds
to child rotation -m on persistent particle labels.

By(1.1), t=jQ and m=-jU modulo p. Since d divides p, the row condition
is exactly d|jU. The requirement that u be integral is

    p divides j(Q+nU).

These are the ONLY restrictions on j. For an integer c and positive
integer b, b|jc exactly when b/gcd(b,c) divides j. Thus the least
positive admissible j is

    K=lcm(p/gcd(p,Q+nU), d/gcd(d,U)).                    (2.2)

Set m to the least nonnegative representative of -KU modulo p and
define

    Q'=KQ,
    U'=((KQ-nm)/p) modulo n, with 0<=U'<n.              (2.3)

The numerator is divisible by p by construction. Replacing m by
m+lp changes its quotient by -ln, so U' is independent of the
representative. The least-time argument proves that(2.3) is the
EXACT parent signature, not just one return pair or an upper bound.
It remains valid for U=0, d=1, and p=1, with the ordinary gcd
convention gcd(b,0)=b.

The earlier denominator criterion describes the same subgroup:

    (n_j/d_(j-1))*(u/n_0-t*sigma_j) integral for all j.

The recursion simply eliminates the hierarchy one level at a time
using its necessary-and-sufficient step(2.1). Therefore its full
period agrees with

    lcm_j den(e_(j-1)*sigma_j).

No row-phase or root-rotation information beyond the least row period
is missing. The one-level equivalence already accounts for the actual
translation of the recorded child state.

## 3. Oddness and the primitive-row equality

Assume the child full period F_child is odd. The integer

    t=lcm(F_child,np)

is odd and is a parent physical return: put u=0, m=t/n. Since np|t,
m is a multiple of p and hence of d; the child translation -m is
trivial modulo p, and the child returns after t. The one-site base
has odd period, so induction proves that every parent full period
is odd. Its f² period is the same number.

If the parent row is primitive, d=p. Any parent physical return
with u=0 must have p|m=t/n and must restore the child without a
nontrivial translation. Hence both np and F_child divide t.
Conversely their lcm is a return by the preceding paragraph. Thus

    F_parent=lcm(np,F_child)                            (3.1)

exactly in the primitive-row case. No such equality is assumed for
nonprimitive rows.

For the submitted example, n=11, p=3 and child signature(1,1):

* d=1 gives K=1, m=2, Q'=1, U'=(-7 modulo11)=4, hence F=11.
* d=3 gives K=3, m=0, Q'=3, U'=1, hence F=33.

A constant row(1,1,1) has d=1, and the other least-period-three rows
with the same total mass provide the primitive case. The example is
consistent with the actual parent size because r=d_child+k_child+ell
=1+1+3=5.

## 4. Möbius counts are counts of ordered rows

Take p slots, total mass ell, and a proposed least cyclic period d|p.
Put e=p/d. A row with this least period is an ordered block of d
entries repeated e times. Therefore e must divide ell; otherwise
the count is zero. When it does, put m=ell/e.

The ordered base block has length d and mass m and must have no
proper period. If it is itself a j-fold repetition, then j divides
both d and m, and its shorter block count is

    binom((d+m)/j-1,d/j-1).

Divisor Möbius inversion consequently gives the exact least-period
count

    C(p,ell;d)=sum_(j|gcd(d,m)) mu(j)
                              binom((d+m)/j-1,d/j-1).   (4.1)

There is no division by d or p: positions in the original incoming-gap
row are ordered and anchored at the root. Formula(4.1) is equivalent
to the previously audited increasing-divisor subtraction for chi.

For ell=0, gcd(d,0)=d and every binomial term is1, giving one row
when d=1 and none otherwise. For p=1 the unique row always has
least period1. Both degeneracies are correctly included.

The original inverse-pruning bijection identifies fixed-profile Dyck
roots with the Cartesian product of these ordered row sets. Thus a
least-period signature has root count product C. Every root has
n distinct physical rotations, and the signature is invariant along
the PBBS orbit. Its common exact full period is F. Consequently
n*product C/F is an integer and is the exact cycle count, as proved
in the earlier signature-multiplicity audit. The stated collar sum
therefore uses the correct root and physical-state factors.

## 5. Exact generating function for an overcount of bad top rows

Let b_r count normalized Dyck roots of semilength r whose top original
gap row is nonprimitive. Such a row has child semilength d>=1, since
the one-slot child for d=0 is always primitive. Write k for the
child's number of peaks and ell for the parent row mass. The exact
inverse-pruning size relation is

    r=d+k+ell,    p=2d+1.                               (5.1)

For a fixed e>1 dividing p, an e-fold repeated row is specified by
p/e ordered nonnegative entries. Its row-mass generating function is

    (1-x^e)^(-p/e).

This counts rows whose period divides p/e, not only those with least
period p/e. Taking the union over all such e therefore overcounts
every nonprimitive row, which is the correct direction for an upper
bound. Because p is odd, e>=3. For 0<x<1,

    (1-x^e)^(-p/e) <= (1-x^3)^(-p/3).                  (5.2)

Indeed the reciprocal base on the left is no larger and its positive
exponent is no larger. There are at most p possible repetition
factors. No independence of reached rows or dynamical states is
used; these are original inverse-pruning fibres.

The peak enumerator for child semilength d is

    N_d(x)=sum_(k=1)^d [binom(d,k)binom(d,k-1)/d] x^k.

Put y=sqrt(x). The displayed sum is y/d times a sum of nonnegative
products binom(d,k)y^k * binom(d,k-1)y^(k-1). It is at most y/d
times the product of the two full binomial sums. Therefore

    N_d(x) <= sqrt(x)/d * (1+sqrt(x))^(2d).              (5.3)

Choose x=9/25 and A=51/50. The exact comparison is

    A^3(1-x^3)-1
      =22844296/1953125000 >0.                          (5.4)

Thus the common row bound in(5.2) is at most A^p. Combining the
rooted fibre count, the parent-size factor x^d, the peak factor
N_d(x), and the union bound over repetition factors gives

    sum_r b_r x^r
      <=sum_(d>=1) x^d N_d(x)(2d+1)A^(2d+1)
      <=3 sqrt(x) A sum_(d>=1) B^d,

where (2d+1)/d<=3 and

    B=A^2 x(1+sqrt(x))^2=374544/390625<1.               (5.5)

The geometric majorant proves convergence, so these positive-series
rearrangements are legitimate. Its exact value is

    3 sqrt(x) A B/(1-B)=85957848/2010125<43,            (5.6)

because

    43*2010125-85957848=477527>0.

Every coefficient is nonnegative. Hence b_r x^r is at most this
finite sum, and

    b_r <43(25/9)^r,

which in particular proves the claimed non-strict upper bound.
The cases with no nonprimitive top row, including r=0 and r=1,
are harmless; the sum over d starts at1 for exactly that reason.

## 6. Probability and collar interfaces

Using the retained elementary Catalan bound

    Cat_r>=4^r/[2(r+1)sqrt(r)],  r>=1,

the exact original-root probability satisfies

    Pr_r(nonprimitive top)
      <=86(r+1)sqrt(r)(25/36)^r.                        (6.1)

Uniform physical middle states give the same probability because
every root has exactly n rotations. No extra factor n belongs in
(6.1).

On a primitive top row the exact period is at least np. On every
state, v>=n and h<=r, so (2h-1)/v<1. Thus the proposed collar
argument may bound the bad contribution by(6.1), and the good
contribution by

    (2/n) E(h/p)
       <=(2/n) sqrt(E h^2 * E p^(-2)).                 (6.2)

Cauchy–Schwarz requires no independence between h and p. With the
separately supplied inequalities E h^2<=2n and E p^(-2)<=J_r,
(6.2) is exactly 2 sqrt(2J_r/n). This verifies the way the new bad-row
bound enters the proposed envelope, while leaving the separate J_r
derivation and finite numerical thresholds to their own audit.

## 7. Scope

The exact signature recurrence is an alternative exact algorithm for
the already proved physical period, now with its minimality justified.
The generating-function proof supplies a uniform exponential bound
on the bad top-row probability. Neither part by itself constructs a
shorter k=17 word or proves nu(k)=B(k).

No reported row, partition, or physical-state test count was rerun or
adopted as an execution result in this note. All identities above were
checked symbolically from the finite source lemmas. This is internal
independent mathematical review, not external or proof-assistant
certification.
