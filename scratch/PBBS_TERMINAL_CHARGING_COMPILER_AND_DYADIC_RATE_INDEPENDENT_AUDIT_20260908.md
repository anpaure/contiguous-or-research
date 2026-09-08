# Terminal charging: independent discrete, compiler, and numerical audit

2026-09-08. Pure proof and local source reads. No mathematical program,
simulation, solver, or unavailable verifier was run.

This independently audits
USER_PBBS_TERMINAL_CHARGING_CLAIM_20260908.md and the complete upstream
note PBBS_TERMINAL_PROFILE_CAPPING_AND_SHARP_MGF_INDEPENDENT_AUDIT_20260908.md.
The discrete charging, profilewise averaging, clipping, finite compiler,
floor effects, optimized exponent, and explicit dyadic corollary pass.
The bounds concern the asymptotic construction, not nu(k)=B(k).

## 1. Exact charging, including a circular interval

For each occupied edge e of a directed circle, lift the preceding period
to the line ending at e. A containing interval shorter than its circle
has a unique starting occurrence on this lift. Choose the latest start,
with deterministic tie breaking. Exactly one containing interval is
chosen at each occupied edge. Therefore, for any nonnegative edge weight,

    sum_{e in U_t} omega(e)
      =sum_{I:T(I)<=t} sum_{e in I}
                         omega(e)1{I is chosen at e}.             (1)

No stationarity or probability theorem is needed for (1).

On the existing physical good event, an eligible success Y_k with k>=1
starts strictly after the base start, no later than the sampled edge,
and contains that edge. The cutoff margin places it in the same
cutoff-t family. Hence it defeats the base interval in (1), and

    1{base is terminal}<=1{Y_1=...=Y_K=0}.                        (2)

The physical period and no-wrap guards are important here: the starts
are compared on the same lift. They hold on the stated aperture domain
because every trace has fewer than2r+1 edges, while every physical period
has at least2r+1 edges.

One must not condition the free rows on being terminal. The correct use
is the implication (2) followed by expectation under the unchanged
base-zero incidence fibre. All the good-event restrictions used before
the success vector is tested are measurable in its exposed environment.
That is the conditioning already verified in
PBBS_QUANTITATIVE_RATE_INCIDENCE_COMPILER_INDEPENDENT_AUDIT_20260908.md.

## 2. First-gap tail and the floor in K

The complete conditional vector coupling now tests only the event that
there is no renewal in1,...,K. For the exact renewal gap law this is
G>K, and its known positive integral gives

    Pr(G>K)
       <= integral_0^1 exp(-s H_K) ds
       <=1/H_K<=1/log(K+1).

For K=floor(r^(1/100)), K+1>r^(1/100), so

    Pr(G>K)<=100/log r.                                        (3)

There is no logarithmic factor from a reciprocal number of renewals.
The success-vector TV error is still a separate bad mass. No growing
finite-dimensional inclusion-exclusion estimate replaces the existing
complete-vector coupling.

## 3. Profilewise normalization and a fixed final cutoff

The full pruning profile Pi is invariant along physical PBBS components.
This includes its height and envelope Q. Its frequency under the uniform
original Dyck root is exactly W_Pi/W_r: each original root has the same
2r+1 physical rotation multiplicity. Thus the conditional, unnormalized
incidence measure

    I_t^Pi(f)=E_D[1{T<=t} sum_{j=0}^{T+1}f(D,j) | Pi]

satisfies

    u_t(Pi)=I_t^Pi(1_terminal),       0<=u_t(Pi)<=1.              (4)

This retains the actual incidence weight; the root law is not refreshed
at a reached phase.

Set H_*=floor((c+1)R), t0=floor(cR), and average t over
ceil(cR),...,floor((c+1)R). The occupied sets are nested inside each
profile class, so u_t0(Pi)<=average_t u_t(Pi). A fixed birth belongs
to the boundary strip for at most q+1 choices of t. Consequently

    average_t I_t^Pi(0<=t-T<q)
         <=2(q+1)mu_H*(Pi)/R.                                  (5)

The endpoint set has size at least R/2. This is a conditional finite
counting statement, not an average of differently normalized Palm laws.
In particular the resulting cutoff t0 is the same for every profile;
no profile-dependent aperture has been selected.

One may retain (5) in the averaged error, as the upstream note does.
Alternatively it is at most6r^(-1/100)mu_H*(Pi), and hence at most
6mu_H*(Pi)/log r at the stated numerical threshold. In the second
version the main constant in (3) can be enlarged from100 to128.
Both versions give the same stated numerical prefactors.

Use u<=1 before integrating over Pi. If
u<=a+e with a,e>=0, then u<=min(1,a)+e. For0<p<=1,
min(1,a)<=a^p. These are pointwise inequalities in the original
profile law. Clipping a previously averaged exponential would not
justify the improved quadratic dependence on p.

## 4. Packing and the weighted-error guard

Take omega=1+R/(h+2). A packed trace has T+2>=h+2 distinct edges of
one invariant profile. Its total omega-weight is at least R.
For any edge-disjoint packing,

    R P_t0/W_r<=E_Pi[omega u_t0(Pi)].                            (6)

The established geometric height estimate gives omega<=2^26 Q.
There is no small-height deletion or inverse height-cutoff cost.

The error function must be defined using actual conditional bad-incidence
masses and a bounded conditional coupling defect. Those terms satisfy,
for example,

    ebar(Pi)<=2(H_*+2).

A profilewise Markov majorant may be much larger and must not be
substituted for this bounded error function when controlling its high-Q
tail. The upstream note uses exactly the bounded definition.

The split at Q=r^(1/800) is then justified. Below it, the old mean raw
error is multiplied by at most2^26r^(1/800). Above it, the Gaussian
envelope tail controls the deterministic bound2(H_*+2).
The explicit upstream derivation gives the strengthened exponent

    A_err=A0+64,   A0=2^80 exp(2^20),

with

    E[omega ebar]<=exp(A_err(c+2)^2)r^(-1/400)                  (7)

already for r>=r0=2^1000000. Its polynomial raw-error debit and Gaussian
tail bounds were independently checked. Importantly, (7) does not yet
absorb the growing exponential into a pure power of r.

## 5. Sharp fractional moment and the finite packing inequality

The global conditional raw bound and sharp moment are

    mu_H*(Pi)<=2^26 d^2 Q exp(JdQ),   d=c+2,
    E[Q^v exp(uQ)]<=2^26(1+u)^3 exp(u^2),
       1<=v<=2, u>=0,
    J=2^38 exp(2^19).

The sharp moment follows by tail integration with
Pr(Q>x)<=exp(12-x^2/4), completing the square, and integrating on
the full real line. The resulting polynomial is
16+36u+8u^2+32u^3<=64(1+u)^3;64exp(12)<2^26.
Thus its quadratic coefficient really is one, with no unstated
multiplicative loss inside u^2.

Combining the pointwise clipping with (6) uses v=1+p and u=Jpd.
Since (128*2^26)^p<=2^33 and
(1+Jpd)^3<=8J^3d^3, the numerical packing bound is

    R P_floor(cR)/W_r
      <=2^88 J^3 d^(2p+3)
             exp(J^2 p^2 d^2)/(log r)^p
           +exp(A_err d^2)r^(-1/400).                         (8)

This is at the prescribed cutoff, uniformly for
r>=r0,1<=c<=sqrt(loglog r),0<p<=1.
The cases0<c<1 inherit an O_c bound from c=1 by monotonicity.

## 6. Literal compiler and the two floor effects

Put t0=floor(cR), H=t0+1. The accepted finite compiler gives

    nu(2r+1)
      <=W_r+2H Cat_r+2(5H-1)P_t0+2L_r(r-H).

Its relative cycle charge is at most(c+1)/R. Its packing multiplier
in terms of R P_t0/W_r is at most10(c+2). Thus the main prefactor in
(8) becomes2^92 J^3, and its polynomial degree2p+4 is at most six.
For the error,10d<=exp(d^2), so its exponent becomes at most
A0+65, strictly below the common A below.

The finite exterior constant1024 was proved in the previous independent
compiler audit. Here its cutoff is t0=floor(cR), so retain the floor:

    1024exp(-t0^2/(8r))
      <=1024exp(-c^2/8+c/(4R))
      <=2048exp(-c^2/8).                                      (9)

The last inequality uses c/R<=1 on the stated domain. The constant
1024 without this correction cannot simply be copied from the earlier
cutoff selected at t>=ceil(cR).

Consequently, with

    A=2^2097152 >= J^2, A0+65,
    C_main=2^92 J^3,    log C_main<2^21,

the following finite bound holds on the previous domain:

    nu(2r+1)/W_r
       <=1+(c+1)/R
          +C_main(c+2)^6 exp(Ap^2(c+2)^2)/(log r)^p
          +exp(A(c+2)^2)r^(-1/400)
          +2048exp(-c^2/8).                                  (10)

The tiny polynomial error in the user's later simplified display
requires an A-dependent increase in r. Formula (10) avoids hiding that
threshold.

## 7. The optimized exponent is correct

For a general asymptotic choice (c+2)^2=beta*y, y=loglog r, the repair
and tail exponents are respectively

    p-Ap^2 beta,       beta/8,

up to the explicitly retained square-root and polynomial losses.
Balancing gives

    beta=8p/(1+8Ap^2),     gamma(p)=p/(1+8Ap^2).

Its maximum occurs at p*=1/sqrt(8A), which is <=1/4 when A>=2.
Then beta=4p* and

    gamma*=p*/2=1/(4sqrt(2A)).

Equivalently take c=2sqrt(p*y)-2 at p=p*. The main exponential is
exp(-py/2), while the exterior exponential is
exp(-py/2+sqrt(py)-1/2). This proves the stated

    O((log k)^(-gamma*) exp(C sqrt(loglog k)))

excess, including both parities. Every fixed smaller exponent gives
a pure logarithmic power. The displayed argument does not remove
the square-root correction at the boundary exponent itself.

## 8. Fully numerical dyadic C=1 corollary

Use the deliberately nonoptimal dyadic choices

    sqrt A=2^1048576,
    p=1/(4sqrt A)=2^-1048578,
    gamma=p/4=2^-1048580,
    k0=ceil(exp(exp(2^1048616))).

For k>=k0 let 2r+1 be k if k is odd and k-1 if k is even.
Then r>=sqrt(k), so

    y=loglog r>=2^1048616-log2
                    >=2^39 sqrt A,
    z=py>=2^37.

In particular r>=r0. Set c=2sqrt(z)-2. It satisfies
1<=c<=sqrt(y), and Ap^2=1/16. All finite aperture and compiler guards
from (10) therefore hold.

The main term in (10) is exactly bounded by

    64 C_main z^3 exp(-3z/4).

For z>=2^37, log C_main<2^21,3log z<=3sqrt(z)<=z/8, and
2^21+log64<=z/8. Its ratio to exp(-z/4) is therefore at most
exp(-z/4)<1/8.

The exterior term is

    2048exp(-z/2+sqrt(z)-1/2).

Since sqrt(z)<=z/8, its ratio to exp(-z/4) is at most
2048exp(-z/8-1/2)<1/8.

The weighted error has

    A(c+2)^2=sqrt(A)*y<=y^2.

For y>=4000, exp(y)>=y^3/6 implies
y^2<=(3/2000)exp(y). Thus the error is at most

    exp(-exp(y)/1000)=r^(-1/1000).

Since exp(y)/1000>=y>=z here, its ratio to exp(-z/4) is at most
exp(-3z/4)<1/8. This absorption is made at the new A-dependent
threshold, not at r0.

Finally the cycle term is at most2sqrt(z)/R. For y>=16,
R=exp(exp(y)/2)>=exp(2y), z<=y, and log y<=y/4.
Its ratio to exp(-z/4) is less than1/8 as well.

The four excess terms together are consequently at most

    (1/2)(log r)^(-gamma).

The trimmed one-coordinate lift doubles both length and middle width
exactly. Moreover log r>=(log k)/2 and2^gamma<=5/4. The total excess
in either parity is at most(5/8)(log k)^(-gamma), proving in particular

    nu(k)<=W(k)[1+(log k)^(-2^-1048580)]
       for k>=ceil(exp(exp(2^1048616))).                       (11)

All logarithms here are natural. The intentionally huge threshold is an
explicit proof bound; no useful finite estimate for k=17 follows from it.
The proof uses no numerical evaluation of these large real numbers.

## 9. Audit scope

The terminal assignment is a new, useful replacement for the reciprocal
renewal count in this construction. Keeping the original profile visible
and clipping before its expectation also removes the earlier height-split
loss. The inherited PBBS structural and literal compiler theorems remain
the premises recorded in the linked sources; no unavailable verifier
output is used as a proof premise.

This independent audit finds no further discrete, conditioning, floor,
compiler, parity, or numerical-threshold gap. It does not promote internal
review to external or formal verification, and it does not settle the
separate exact-equality objective.
