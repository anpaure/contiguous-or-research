# An exact freeze-variation formula and a final-ten-percent obstruction

2026-09-08. Pure analysis; no computation. Root read the complete note and
passed the generator, quartic bound, exit moments, Hölder bound, final-ten-
percent inequality, and stated-ledger scope checks.
This concerns the equal-principal continuum charge of the specified
fourteen-row absorption bank. It is not a lower bound for unrestricted
OR words or an exclusion of other adapted terminal controls.

Use `SACRIFICIAL_ACCUMULATOR_EXACT_ABSORPTION_20260908.md` and master A.7.
Put alpha=35/32 and beta=sqrt(pi/8). With eight equal principal lengths
a>0 and sacrificial radius r>=0, the exact limiting absorption ledger is

    F(a,r)=alpha/(2a) [1+E min(1,aT/r)],
    T=1+U_1+U_2+U_3,                                (1)

where the U_i are independent uniform[0,1] variables. At r=0 the minimum
is interpreted as one. In particular F(a,r)=alpha/a for r<=a.

## 1. Exact annular-occupation criterion

The density of T is

    f_T(t)=(1/2) sum_(j=0)^3 (-1)^j binom(3,j)
                                      (t-1-j)_+^2. (2)

It is supported on [1,4]. Let a be fixed, |x|=r, and let
R_u=|x+B_u| for standard three-dimensional Brownian motion B.
For the Bessel generator L=(1/2)d^2/dr^2+(1/r)d/dr,

    L_r F(a,r)=-alpha f_T(r/a)/(4a^2 r).            (3)

To verify (3), the function min(1,l/r) is harmonic on each side of
r=l; its radial derivative has jump -1/l there. Its distributional
Bessel generator is -delta_l/(2l). Integrating against the density
f_T(l/a)/a and multiplying by alpha/(2a) gives (3). The averaged
function is C^2, constant near zero, and has bounded generator for
fixed a, so the ordinary stopped Itô formula and bounded convergence
give the exact identity

    F(a,r)-E F(a,R_delta)
      = alpha/(4a^2) integral_0^delta
                       E[f_T(R_u/a)/R_u] du.        (4)

The integrand is defined as zero at R_u=0. Thus the continuation discount
is precisely a weighted occupation of the annulus a<R_u<4a. It is not
a new growth advantage for the frozen principal radii.

For a deterministic freeze time theta in (0,1), let a=A_theta be the
balanced principal frontier and let the retained sacrificial vector x
have |x|<=a. Conditional on the freeze information, let the remaining
variance delta=1-theta be an independent Gaussian continuation of that
slot. A.7 gives

    A_theta^(-2) distributed as S_9/theta,

where S_9 is the sum of nine independent unit-ball exit times in dimension
three. No law for |x| conditional on a is needed. The resulting charge
C_theta=beta E F(a,R_delta) satisfies

    C_theta = c9 theta^(-1/2)
      - (alpha beta/4) E[
          a^(-2) integral_0^delta f_T(R_u/a)/R_u du]. (5)

Consequently this policy improves c9 if and only if its expected weighted
annular occupation exceeds

    4 E sqrt(S_9) [theta^(-1/2)-1].                 (6)

Equation (6) compares the actual continuation gain with the loss from
freezing the principal frontier early. Supermartingale monotonicity
alone supplies no such comparison.

## 2. A uniform fourth-order discount bound

For every t>=1, the positive convolution formula for U_1+U_2+U_3 gives

    E(t-T)_+ <= (t-1)^4/24.

For example its density at y>=0 is at most y^2/2: integrate over the
nonnegative simplex and omit the upper bounds U_i<=1. A further integral
against (t-1-y) proves the displayed bound. It is valid also when t>2,
not just on the first piece of the stop-loss polynomial.

It follows from (1) that, for r>=0,

    0 <= alpha/a-F(a,r)
       <= alpha (r-a)_+^4/(48a^5).                 (7)

If the initial vector satisfies |x|<=a, the triangle inequality gives
(|x+B_delta|-a)_+<=|B_delta|. Since E|B_delta|^4=15delta^2,

    0 <= alpha/a-E F(a,R_delta)
       <= (5alpha/16) delta^2 a^(-5).              (8)

This bound is uniform over the sacrificial starting radius and direction.
It therefore does not require convergence or identification of the active
minimum's joint law in the minimum-clock limit.

## 3. Explicit exclusion for theta>=9/10

Averaging (8) and using the frontier law yields

    C_theta/c9 >= theta^(-1/2)
       - (5/16) [E S_9^(5/2)/E sqrt(S_9)]
                    delta^2 theta^(-5/2).          (9)

The exit transform x/sinh(x), with x=sqrt(2s), gives

    E tau=1/3, E tau^2=7/45, E tau^3=31/315.

Independence therefore gives

    E S_9=3, E S_9^2=47/5, E S_9^3=3229/105.

Cauchy--Schwarz and Hölder imply respectively

    E S_9^(5/2) <= sqrt(151763/525) <18,
    E sqrt(S_9) >= sqrt(135/47) >3/2.               (10)

Hence the moment ratio in (9) is strictly below 12. If theta>=9/10,

    theta^(-5/2) <= (10/9)^(5/2) <4/3.

For 0<delta<=1/10, (9) consequently gives

    C_theta/c9 > theta^(-1/2)-5delta^2
                  >1+delta/2-5delta^2 >=1.         (11)

The second inequality is strict because (1-delta)^(-1/2)>1+delta/2.
Thus freezing the eight principals during the final ten percent and
dumping all remaining variance into the sacrificed slot does NOT improve
this continuum absorption ledger. This is an analytic result independent
of the finite-mesh diagnostic in the preceding note.

More locally, the two-sided bounds F<=alpha/a and (9) prove

    C_(1-delta) = c9 [1+delta/2+O(delta^2)]
                                  as delta decreases to zero, (12)

uniformly over all admissible active-minimum laws at the deterministic
freeze time. The initial variation is unfavorable even though the fixed-
principal continuation charge is a supermartingale.

## 4. Terminal-bank and policy scope

The existing line alternative cannot defeat this comparison at eight equal
principal lengths. If r<=a, its normalized charge is 2/a, above F(a,r).
If r>=a, exact absorption into a principal line gives 1/a+1/r. For
1<=t=r/a<=5/2, this is at least 7/(5a)>alpha/a>=F(a,r). For t>=5/2,

    aF(a,r) <= alpha/2+5alpha/(4t) <1+1/t,

using E min(1,T/t)<=E T/t=5/(2t). Thus the line fallback is everywhere
more expensive on the limiting state geometry in this note.

Statements (9)-(12) concern a deterministic freeze time, the eight equal
principal frontier furnished by A.7, and this specified terminal bank.
They do not exclude earlier freezes theta<9/10, adapted state-dependent
stopping, retaining genuinely unequal principal radii, finer contracted
unequal-staircase compilers, or another control policy. Such a proposed
improvement must still supply a legal all-child construction and the
fixed-factor compiler limits. No improved asymptotic coefficient is
claimed here.
