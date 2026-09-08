# Height-adaptive construction: uniform finite thresholds from dimension 29

2026-09-08. **[R], conditional on the retained finite PBBS support,
matching-corridor, particle-reduction and original pruning-fibre inputs.**
The new signature recursion and analytic estimates passed independent
internal proof review. A new exact rational calculation reproduced all
four threshold certificates and checked the finite bridge against the
previously reproduced census. Internal reviews are not external or
proof-assistant certification of the dependency chain.

The resulting sufficient thresholds apply to **every subsequent integer
dimension**, of either parity:

| Starting dimension | Upper bound | Excess above width |
|---:|---:|---:|
| 29 | nu(k) < 1.01 W(k) | less than 1% |
| 327 | nu(k) < 1.001 W(k) | less than 0.1% |
| 1,483 | nu(k) < 1.0001 W(k) | less than 0.01% |
| 6,849 | nu(k) < 1.00001 W(k) | less than 0.001% |

Here W(k)=binom(k,floor(k/2)). These are sufficient thresholds, not
claims that each is the smallest possible starting dimension. Since
W(k)<=B(k)<=nu(k), each row also bounds nu(k)-B(k) by its displayed
fraction of W(k), and hence of B(k). It does not establish equality.

The advance over [the exact census through 101](HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md)
is the decreasing analytic envelope that continues beyond the finite
table. The new time-and-rotation recursion is equivalent to the already
audited denominator formula and provides an alternative exact census
algorithm. No new asymptotic exponent or shorter literal word is claimed.

## Exact time-and-rotation recursion

For a deficit-one state A on n sites, let

    Gamma(A)={(t,u): f_n^t(A)=rho_n^u(A)}.

There is no nontrivial rotational stabilizer. Commutation of f and rho
therefore gives unique Q>=1 and 0<=U<n with

    Gamma(A)={(jQ,jU+kn): j,k integers},
    F(A)=Qn/gcd(n,U).

For child circumference p, child signature (Q,U), and parent incoming-row
least period d|p, the necessary-and-sufficient one-level return criterion
is

    m=(t-pu)/n is an integer, d|m, and (t,-m) belongs to Gamma(child).

Writing t=jQ leaves precisely d|jU and p|j(Q+nU). Consequently, put

    K=lcm(p/gcd(p,Q+nU), d/gcd(d,U)),
    m=(-KU) mod p,
    Q'=KQ,
    U'=((KQ-nm)/p) mod n.

This is the exact minimal parent signature. Start at the one-site core
with (Q,U)=(1,0). Every full period is odd, so f and f^2 have the same
periods. A primitive top row gives the exact identity
F(parent)=lcm(np,F(child)).

For a p-slot row of mass ell and proposed least period d|p, let e=p/d.
The count is zero unless e divides ell. Otherwise m=ell/e and the number
of **ordered** rows is

    C(p,ell;d)=sum_(j|gcd(d,m)) mobius(j)
                            *binom((d+m)/j-1,d/j-1).

This includes the mass-zero case and is equivalent to the previous
divisor-subtraction count. The original rooted fibre is a Cartesian
product of row sets. Multiplying the row counts, then multiplying by n
and dividing by the exact period, gives the cycle count for a signature.
The partition census and its root/state multiplicities are unchanged.

[The complete signature and fibre audit](scratch/PBBS_EXACT_SYMMETRY_SIGNATURE_RECURSION_AND_NONPRIMITIVE_TOP_GF_AUDIT_20260908.md)
proves minimality, signs, oddness, the primitive equality and all degenerate
row cases. The new submission's reported 918,219-profile implementation
was not supplied or rerun; the existing independently implemented
1,295,970-profile census through 101 supplies the finite data used here.

## A decreasing envelope with explicit constants

Write n=2r+1, Cat_r=binom(2r,r)/(r+1), and

\[
J_r=\frac{3r+49}{3r(r+2)(r+3)}+\frac{43}{72\operatorname{Cat}_r},
\qquad
E_r=2\sqrt{\frac{2J_r}{2r+1}}
 +86(r+1)\sqrt r\left(\frac{25}{36}\right)^r.
\]

For the unchanged height-adaptive word N_r, the proved bound is

\[
\frac{N_r-W(2r+1)}{W(2r+1)}\le E_r\qquad(r\ge1).
\]

The exact collar identity averages (2h-1)/v over uniformly sampled
physical middle states. Every canonical Dyck root has n distinct physical
rotations, so the rotation-invariant quantities below have exactly the
same law under a uniform root. Reflection gives E(h^2)<=2n.

If d=r-(number of Dyck peaks), then p=2d+1 is the particle count and

    Pr(d=j)=binom(r,j)binom(r,j+1)/(r Cat_r), 0<=j<r.

For j>=1,

    1/(2j+1)^2 <= 1/[4(j+1)(j+2)]
                  +5/[3(j+1)(j+2)(j+3)].

The cleared numerator is (j-1)(56j+43). At j=0 the required correction
is 43/72, with probability 1/Cat_r. Vandermonde summation gives

    E[1/((d+1)(d+2))] <=4/[r(r+2)],
    E[1/((d+1)(d+2)(d+3))] <=8/[r(r+2)(r+3)].

These prove E(p^-2)<=J_r. The complete derivations, including the exact
second Vandermonde numerator, are retained in
[the independent moment and envelope audit](scratch/PBBS_NARAYANA_RECIPROCAL_MOMENT_AND_UNIFORM_ENVELOPE_AUDIT_20260908.md).

The nonprimitive top row is bounded by an original-root count, without
concentration. For child semilength d>=1, child peaks k and row mass ell,
the parent size is r=d+k+ell. An e-fold repeated row has generating
function (1-x^e)^(-p/e), with odd e>=3. At fixed 0<x<1 it is bounded by
(1-x^3)^(-p/3). The Narayana polynomial satisfies

    N_d(x) <= sqrt(x)(1+sqrt(x))^(2d)/d.

At x=9/25 and A=51/50, exact rational inequalities give

    A^3(1-x^3)>1,
    B=A^2*x*(1+sqrt(x))^2=374544/390625<1.

Union over at most p repetition factors and sum over children. If b_r
counts roots with nonprimitive top row, the positive generating function
is bounded by

    sum_r b_r*x^r <=3sqrt(x)*A*B/(1-B)
                  =85957848/2010125<43.

Thus b_r<=43(25/9)^r. The elementary Catalan lower bound yields bad-row
probability at most 86(r+1)sqrt(r)(25/36)^r. This is an evaluation of a
positive generating function, not a coefficientwise comparison of the
individual repetition series.

On primitive rows v>=np, and Cauchy–Schwarz gives

    E[(2h-1)/v; primitive] <= (2/n) E(h/p)
                           <=2sqrt(2J_r/n).

On other states (2h-1)/v<1. Adding their probability proves the envelope.
No independence of height and particle count, or of fixed-size gap
coordinates, is used. The previous concentration and divisor-probability
estimates are unnecessary for this envelope.

Finally, J_r is a sum of decreasing positive terms:

    J_r=1/[r(r+2)]+40/[3r(r+2)(r+3)]+43/(72Cat_r).

For the envelope's second term, the squared successive ratio is

    (25/36)^2*(r+2)^2/[r(r+1)] <=125/144<1  (r>=4).

Both terms of E_r strictly decrease for r>=4.

## The exact finite-to-infinite bridge

One new h100 calculation, bounded by 30 CPU seconds, 45 wall seconds and
512 MiB, completed in about 0.084 seconds. It used integer arithmetic,
fractions and upward integer-square-root bounds on a 10^-60 grid:

| r | Certified rounded-up upper bound for E_r | Target |
|---:|---:|---:|
| 45 | 0.009271845429338486 | <0.01 |
| 163 | 0.000991315300369260 | <0.001 |
| 741 | 0.000099868373195185 | <0.0001 |
| 3,424 | 0.000009998021412266 | <0.00001 |

The script also hash-checked the existing exact census and verified all
31 inequalities 125C_r<W_r for r=14,...,44. The unique largest ratio
in that band is at r=16, dimension 33:

    C_33/W(33)=4479616/583401555<1/125<1/100.

Therefore the finite census handles odd dimensions 29 through 89; the
decreasing envelope, beginning at r=45, handles every odd dimension from
91 onward. The exact lift doubles both word length and width, supplying
all even dimensions as well. This proves the one-percent guarantee for
every k>=29. The other three envelope rows give starting dimensions
327, 1483 and 6849 in the same way.

At dimension 29 the exact native construction has

    W(29)=77,558,760,
    N_14=78,019,684,
    N_14-W(29)=460,924.

The existing dimension-97 row was also checked: its relative excess is
below 0.00001 at dimensions 97 and 98. That isolated stronger pair does
not make 97 a uniform threshold; the native ratios are not monotone.

[The numeric certificate](scratch/SYMMETRY_DESCENT_UNIFORM_THRESHOLD_EXACT_NUMERIC_CERTIFICATE_20260908.md)
links the [reproducible script](scratch/verify_symmetry_descent_uniform_threshold_numbers_20260908.py)
and [full exact report](scratch/symmetry_descent_thresholds_20260908/symmetry_descent_threshold_numeric_certificate.json).
The report SHA-256 is
`acd7d2c2cfc8c067198c3e227c4011de09d32a28df79c41289c0da6fb337ebb4`.
All mathematical execution was on h100. No enormous literal word was
generated, and no finite table was extrapolated without a proof.

## Relation to exact equality

The strongest recorded eventual stretched-exponential rate remains
[the harmonic-period bound](HEIGHT_ADAPTIVE_HARMONIC_PERIOD_RATE_20260908.md).
After this threshold audit, the user supplied a separate optimal word:
[nu(17)=B(17)=24,313 is now verified](K17_OPTIMAL24313_VERIFIED_20260908.md).
That finite breakthrough is independent of this conditional envelope.
The submission's references to older 17-dimensional upper bounds are
historical; current neighboring bounds are tracked separately in
[the finite comparison](FINITE_BOUNDS_K18_K19_K20_20260908.md).

The construction-specific exponential additive-overhead barrier also
remains valid. These uniform approximation guarantees do not make the
unchanged construction attain B(k), and do not resolve nu(k)=B(k).
