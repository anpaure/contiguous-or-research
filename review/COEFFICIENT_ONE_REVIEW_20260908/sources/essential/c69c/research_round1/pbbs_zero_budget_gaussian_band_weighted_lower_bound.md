# True zero-budget Gaussian bands have nonvanishing length-weighted mass

Date: 2026-09-07. Pure proof; no computation or original-source edits.

For every fixed 0<a<b, the TRUE newborn class

    E_(r;a,b)={D in Dyck_r: T(D)=ht(D),
                         a sqrt(r)<=ht(D)<=b sqrt(r)}

has probability Theta_(a,b)(r^(-1/2)). Its length-weighted mass converges
to a strictly positive constant. Consequently, for every fixed c>0,
short complement repair intervals at cutoff H=floor(c sqrt(r)) have
total physical edge incidence Omega_c(W), even though their newborn
count is o_c(W) by the accepted Gaussian theorem.

These are incidence and energy lower bounds. They are not lower bounds
for an edge-disjoint packing, distinct damaged targets, or the optimal
cost of a construction that shares repairs.

## 1. Exact generating function and the limiting density

Use the accepted full zero-budget identity

    G_h(x)=sum_(D: ht(D)=T(D)=h) x^(|D|_up)
          =x^h/[F_(m_1)(x)F_(m_2)(x)F_(m_3)(x)],      (1)

where F_0=F_1=1, F_m=F_(m-1)-xF_(m-2), and m_1,m_2,m_3 are
balanced integers with sum 2h+1. In particular m_i/h->2/3 and

    G_h(1/4)=2/product_(i=1)^3(m_i+1)
             ~27/(4h^3).                              (2)

The positive determinant factorization is

    F_m(x)=product_(k=1)^floor(m/2)(1-4q_(m,k)x),
    q_(m,k)=cos^2(pi*k/(m+1)).                          (3)

Normalize the coefficients of G_h at x=1/4. Their size variable N_h is
h plus the sum of independent geometric variables on {0,1,...}, with
parameters q_(m_i,k). For each fixed k, its geometric variable divided
by h^2 converges to an exponential of rate

    lambda_k=9 pi^2 k^2/4.

The sum of the means of the modes k>K, divided by h^2, is O(1/K),
uniformly in h: use sin(pi*k/(m+1))>=2k/(m+1). Thus

    N_h/h^2 -> Y=sum_(i=1)^3 sum_(k>=1) E_(i,k),       (4)

where the E_(i,k) are independent exponentials of rate lambda_k.
The sum is finite almost surely. Its Laplace transform is

    E exp(-uY)=[(2sqrt(u)/3)/sinh(2sqrt(u)/3)]^3.       (5)

The value at u=0 is one, and E Y=2/9, agreeing with the geometric
mean identity sum_k q_(m,k)/(1-q_(m,k))=m(m-1)/6.

Let g denote the density of Y, extended by zero on (-infinity,0]. It is
continuous and strictly positive on (0,infinity). For positivity, split
off one exponential X and call
the remaining sum V. Every finite partial sum of V can be arbitrarily
small with positive probability, and its independent tail has arbitrarily
small mean. Hence P(V<t)>0 for every t>0. The convolution density
E[lambda_1 exp(-lambda_1(t-V))1_(V<t)] is then positive.

## 2. Uniform local limit, rather than only weak convergence

Keep the k=1 geometric mode from two of the three determinant factors.
Their parameters satisfy 1-q=Theta(h^(-2)). At Fourier argument t/h^2,
with |t|<=pi h^2, their product of characteristic-function moduli is
bounded by

    C/(1+t^2),                                        (6)

using
|1-q exp(i theta)|^2=(1-q)^2+2q(1-cos theta)
and 1-cos theta>=2theta^2/pi^2 for |theta|<=pi.
All other factors have modulus at most one. The same integrable bound
holds for the limiting characteristic function.

Pointwise convergence from (4), followed by dominated convergence in
Fourier inversion, therefore gives the UNIFORM lattice local limit

    sup_(n in Z) |h^2 P(N_h=n)-g(n/h^2)| -> 0.         (7)

The supremum follows because the Fourier L1 error bounds the inversion
error uniformly in n/h^2. In particular, (7) is uniform when r/h^2
stays in any compact subset of (0,infinity). This also proves the
continuity used above. No unproved local central limit theorem is assumed.

Since

    [x^r]G_h(x)=4^r G_h(1/4) P(N_h=r),

(2) and (7) yield, uniformly on every fixed positive Gaussian band,

    [x^r]G_h(x)
      =4^r h^(-5)[(27/4)g(r/h^2)+o(1)].               (8)

Divide by Cat_r~4^r/(sqrt(pi)r^(3/2)). Define

    kappa(u)=(27sqrt(pi)/4) u^(-5) g(u^(-2)), u>0.     (9)

It is continuous and positive, and uniformly for a<=h/sqrt(r)<=b,

    P_(Dyck_r)(T=ht=h)
       =r^(-1)[kappa(h/sqrt(r))+o(1)].                 (10)

## 3. Band counts and weighted limits

Riemann summation of (10) proves

    sqrt(r) P(E_(r;a,b)) -> K_(a,b),
    K_(a,b)=integral_a^b kappa(u) du>0.                (11)

In particular this proves both sides of the claimed Theta(r^(-1/2))
estimate. More generally, for each fixed integer j>=0,

    r^((1-j)/2) E[(T+2)^j 1_(E_(r;a,b))]
       -> integral_a^b u^j kappa(u) du.                (12)

The +2 affects no leading constant in a positive Gaussian band.
For j=1 the limit is a strictly positive finite constant; for j=2 the
unscaled moment has order sqrt(r).

## 4. Actual short-run incidence and rank energy

Fix c>0 and choose any 0<a<b<c. Put H=floor(c sqrt(r)). Every root
in E_(r;a,b) has T+1<=H for sufficiently large r. Therefore

    liminf E[(T+2)1_(T+1<=H)]
       >= integral_a^b u kappa(u)du>0,                 (13)

and

    liminf r^(-1/2) E[(T+2)^2 1_(T+1<=H)]
       >= integral_a^b u^2 kappa(u)du>0.               (14)

The exact rank-energy weight has the additional lower bound

    liminf E(H-T)_+
       >= integral_a^b(c-u)kappa(u)du>0.               (15)

Indeed (10) applies uniformly to the band and
(H-h)/sqrt(r)->c-u. The same positive lower bound holds with (H-T-1)_+;
the subtraction of one changes the band contribution by O(r^(-1/2)).

Let W=(2r+1)Cat_r and let I_H denote the full physical family of
complement residence intervals with T+1<=H. Each gap start contributes
one such interval, of T+2 edges. The exact identities are

    sum_(I in I_H)|I|=W E[(T+2)1_(T+1<=H)],
    E_H(P_r)=W E(H-T)_+.                              (16)

Consequently (13)-(15) prove

    sum_(I in I_H)|I|=Omega_c(W),
    E_H(P_r)=Omega_c(W),
    sum_(I in I_H)|I|^2=Omega_c(W sqrt(r)).             (17)

The quadratic raw run charge ell(ell+1)/2, with ell=T+1, likewise has
total Omega_c(W sqrt(r)); its band limit constant is one half of the
integral in (14). Already the zero-budget band alone supplies all of
these lower bounds.

The accepted global zero-budget upper bound
P(T=ht)=O(r^(-1/2)) also shows that its cutoff-H length-weighted mass
is O_c(1). Thus the contribution of the zero-budget class itself to the
first quantity in (17) is Theta_c(W), rather than only Omega_c(W).

## 5. Scope for a repair ledger

These estimates coexist with the accepted full newborn rarity
P(T+1<=H)=o_c(1). In fact (11) gives the complementary lower bound

    P(T+1<=H)=Omega_c(r^(-1/2)).                       (18)

Thus it is impossible to strengthen the TRUE unweighted short-run count
to o_c(W/H) at a fixed Gaussian cutoff. This says nothing comparable
about the maximum edge-disjoint subfamily.

There is also an immediate monotonic consequence for larger cutoffs.
If H_r/sqrt(r)->infinity, a single fixed band E_(r;a,b) still lies below
H_r for all large r. Therefore

    |I_(H_r)|>=c_(a,b) W/sqrt(r),
    H_r |I_(H_r)|/W -> infinity.                        (19)

This uses inclusion of one fixed band, not a new rate or limit theorem
with growing c. In particular, the RAW census requirement (9.1) in
MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md
is impossible: its left side includes this fixed band and is at least
Omega(4^r/r^2), whereas (9.1) asks for o(4^r/(r^2 sqrt(log r))).
This rejects that stronger raw-count sufficient route only. The
residence-packing criterion and a construction that shares repairs
remain undecided by the lower bound.

The raw sum of repair-interval lengths is not o(W). A ledger charging
every run separately at a fixed positive cost per interval edge therefore
has an Omega(W) charge. A quadratic raw per-run ledger has an
Omega(W sqrt(r)) charge. An H-per-run charge also has an Omega_c(W)
contribution from (11). These facts rule out those raw sums being
negligible; they do not prove that every legal repair must pay those sums.

Intervals can overlap, one cut can hit several intervals, and targets
can be represented more than once. Accordingly (17) proves neither a
packing lower bound nor a distinct-target-loss lower bound. To obtain
an o(W) repair contribution one needs an argument that shares, clusters,
discounts, or otherwise avoids the separate raw incidence charges.

Sources: the accepted exact product in
research_round1/pbbs_original_forest_product.md, Section 5; its positive
geometric factorization as used in pbbs_zero_budget_uniform_bound.md;
and the exact physical dictionary in
pbbs_gaussian_age_residual_and_cut_charges.md, Sections 1 and 5.

## Appendix. An elementary certificate for the positive weighted lower bound

The positive lower bounds in (17)-(18) also follow without a local limit
theorem, if explicit constants for every prescribed band are not needed.
Choose 0<a<b<min(c,1/2). Separate one largest-parameter geometric G
from the normalized size in Section 1, writing N_h=h+G+R with G and R
independent. For all sufficiently large h,

    E R<=h^2,       1-q=Theta(h^(-2)),

where q is the parameter of G. For a sqrt(r)<=h<=b sqrt(r), Markov's
inequality gives P(R<=r/2)>=1-2b^2>1/2. For large r, on that event,
0<=r-h-R<=r. Consequently

    P(N_h=r)
      >= (1/2)(1-q)q^r
      >= c_1 h^(-2) exp[-c_2 r/h^2]
      >= c_(a,b) h^(-2).

Multiply by G_h(1/4)=Theta(h^(-3)) and 4^r. Summing the resulting
coefficient lower bound over this positive Gaussian band gives
P(E_(r;a,b))>=c'_(a,b)/sqrt(r). Multiplication by h, h^2, or H-h
gives the positive first-moment, second-moment, and rank-energy lower
bounds used in (17). The exact constants for arbitrary fixed bands remain
those obtained by the uniform local limit above.

## Appendix B. Global zero-budget moments and their exact constants

The accepted uniform coefficient bound supplies both tails missing from
the fixed-band local limit. This appendix and all constants below passed
an independent analytic audit on 2026-09-07. Put chi=1{T=ht} and

    nu_r=sqrt(r) sum_h P(T=ht=h) delta_(h/sqrt(r)).

Equation (10) gives vague convergence of nu_r on (0,infinity) to
kappa(u)du. For an absolute C the uniform-bound note gives, for h>=2,

    P(T=ht=h) <= C r^(3/2) (h+1)^(-5)
                   exp[-(r-h)/(2(h+1)^2)].             (B1)

For r>1 the h=1 class is empty. If h<=a sqrt(r), then h<=r/2 for
sufficiently large r. For each j=0,1,2, Riemann summation in (B1) gives

    limsup_r integral_(0,a] u^j dnu_r
      <= C_j integral_0^a u^(j-5) exp[-1/(4u^2)]du
      ->0 as a decreases to zero.                      (B2)

For the high tail, drop the exponential and sum the power. This yields

    limsup_r integral_(b,infinity) u^j dnu_r
      <= C'_j b^(j-4) ->0 as b increases to infinity.  (B3)

Thus vague convergence extends to the total mass and the first two
moments. With y=u^(-2), equation (9) gives

    integral_0^infinity u^j kappa(u)du
      =(27 sqrt(pi)/8) E[Y^(1-j/2)],  j=0,1,2.         (B4)

Since EY=2/9, the count constant is 3sqrt(pi)/4. The +2 in repair
lengths has no effect on these leading limits: its error terms are
controlled by the already bounded lower moments. Consequently

    sqrt(r) P(T=ht) -> 3sqrt(pi)/4,
    E[(T+2)chi] -> (27sqrt(pi)/8) E[sqrt(Y)],
    r^(-1/2) E[(T+2)^2 chi] -> 27sqrt(pi)/8.            (B5)

The middle constant has a closed form. The fractional-moment identity
and the Laplace transform (5), with x=2sqrt(s)/3, give

    E[sqrt(Y)]
      =(1/(2sqrt(pi))) integral_0^infinity
          [1-E exp(-sY)] s^(-3/2) ds
      =(2/(3sqrt(pi))) I,
    I=integral_0^infinity [x^(-2)-x csch(x)^3]dx.       (B6)

These nonnegative integrals are legitimate by Tonelli; finiteness also
follows from E sqrt(Y)<=sqrt(EY). Put f(x)=csch(x), so f''=f+2f^3.
Integrating with lower cutoff epsilon gives exactly

    I_(epsilon,infinity)
      =1/epsilon+[epsilon f'(epsilon)-f(epsilon)]/2
        +(1/2) integral_epsilon^infinity x f(x)dx.

The expansion epsilon f'(epsilon)-f(epsilon)
=-2/epsilon+O(epsilon^3) cancels the boundary singularity. Hence

    I=(1/2) integral_0^infinity x csch(x)dx
      =sum_(n>=0) (2n+1)^(-2)=pi^2/8,
    E[sqrt(Y)]=pi^(3/2)/12.                            (B7)

The global zero-budget first repair-incidence limit is therefore

    E[(T+2)chi] -> 9pi^2/32.                           (B8)

In particular the complete zero-budget root count is asymptotic to
(3/4)4^r/r^2. On the full physical factor, its birth count is asymptotic
to (3sqrt(pi)/4)W/sqrt(r), its total full repair-edge incidence to
(9pi^2/32)W, and its quadratic repair-edge incidence to
(27sqrt(pi)/8)W sqrt(r). Replacing T+2 by T+1 gives the same first
constant for complement owner-coordinate incidence.

These remain raw incidence statements. The separate renewal-clustering
proof establishes sharing and small support; it is not a consequence
of the moment limits alone. All statements here concern T=ht only.
