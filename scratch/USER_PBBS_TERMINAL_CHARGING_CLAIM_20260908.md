# User's terminal-charging rate proposal — review transcription

2026-09-08. Structured transcription of the user's latest proof for internal
review. The original chat is authoritative. The linked sandbox proof and
verifier packages have not been supplied as accessible local files.

Use the same exact finite PBBS inputs and the quantitative sampling law
already audited in COEFFICIENT_ONE_EXPLICIT_RATE_20260908.md. Set R=sqrt(r),
W_r=binomial(2r+1,r), profile Pi with invariant height h and envelope Q.

## 1. Deterministic terminal charging

In any family of directed circular intervals shorter than their circles,
assign each occupied edge e to its containing interval with latest start
measured backwards from e (deterministic ties). For invariant or arbitrary
nonnegative edge weight omega,

    sum_(e in U_t) omega(e)
      =sum_(I:T(I)<=t) sum_(e in I) omega(e)*1_terminal(I,e).

Every successful eligible candidate Y_k with k>=1 starts strictly after
the sampled base start, no later than sampled e, and covers e. It prevents
the base incidence being terminal. Thus, outside the same physical errors
and cutoff strip, terminal<=1{Y_1=...=Y_K=0}.

The complete-vector coupling compares to renewal masses u_n=1/(n+1).
For its first gap G,

    Pr(G>K)=integral_0^1 product_(j=1..K)(1-s/j)ds
             <=1/H_K<=1/log(K+1).

At K=floor(r^1/100), this is <=100/log r. No reciprocal renewal count is
used, removing its loglog factor.

## 2. Profile-invariant weights

Set omega=1+R/(h+2). Every trace has at least h+2 distinct edges, hence

    R P_t/W_r <=(1/W_r)sum_(e in U_t) omega(e).

The existing geometric height bound h>=c_h R/Q gives omega<=C Q.
Thus there is no epsilon-height split or epsilon inverse loss.

The existing numerical profile bound is Pr(Q>x)<=exp(12-x^2/4) and
h>=2^-25 R/Q, so root notes omega<=2^26 Q. The conditional raw estimate,
with J=2^38 exp(2^19) and t_max=floor((c+1)R), is

    mu_max(Pi)=E[(T+2)1_(T<=t_max)|Pi]
       <=2^26(c+2)^2 Q exp(J(c+2)Q).

Keep this profile visible rather than averaging immediately.

## 3. Profilewise averaging and clipping

Let u_t(Pi) be the occupied fraction within the physical factor having
profile Pi. It is between0 and1. Use the same L=r^2/5,S=r^1/50,K=r^1/100
(floored), q=ceil(Rr^-1/100), and cutoff set ceil(cR)..floor((c+1)R).
At each fixed profile, the cutoff strip0<=t-T<q holds for any birth at
mostq+1 times. Monotonicity gives

    u_floor(cR)(Pi)<=average_t u_t(Pi)
       <=C mu_max(Pi)/log r+ebar(Pi).

The error ebar is nonnegative. The preceding raw error estimate implies

    E[omega*ebar]<=exp(C(c+2)^2) r^-1/400.

For justification split ONLY the error at Q=r^1/800. Below it, multiply
the previous r^-1/200 raw bound by C Q; above it the Gaussian tail is
superpolynomial. Conditional upper free rows retain their original law.

Now use u<=1 BEFORE averaging:

    R P_floor(cR)/W_r
       <=C E[Q min{1,C(c+2)^2 Q exp(J(c+2)Q)/log r}]
                       +exp(C(c+2)^2) r^-1/400.

## 4. Fractional moment

For0<p<=1, min(1,z)<=z^p. If Pr(Q>x)<=C0 exp(-a0 x^2), then uniformly
v in[1,2],u>=0,

    E[Q^v exp(uQ)]<=C(1+u)^3 exp(u^2/(4a0)).

Proof by tail integration using x^(v-1)<=1+x, x^v<=x+x^2, completing
the square. With v=1+p,u=Jp(c+2), choose A>=max(2,J^2/(4a0)) large
enough for errors. Then uniformly1<=c<=sqrt(loglog r),0<p<=1,

    R P_floor(cR)/W_r
      <=C(c+2)^(2p+3) exp(Ap^2(c+2)^2)/(log r)^p
                         +exp(A(c+2)^2)r^-1/400.

For fixed c and p1 this gives P_floor(cR)=O_c(W_r/(R log r)). For
0<c<1 monotonicity from c1 suffices. This is at the prescribed cutoff.

## 5. Compiler and optimized exponent

Use H=floor(cR)+1 in the exact compiler

    nu(2r+1)<=W_r+2H Cat_r+2(5H-1)P_(H-1)+2L_r(r-H).

After the exterior estimate and absorbing polynomially small errors,

    nu/W<=1+C r^-1/1000
      +C(c+2)^6 exp(Ap^2(c+2)^2)/(log r)^p+Ce^-c^2/8.

This is claimed for sufficiently large r uniformly over the above p,c.
The threshold here depends on A; it must not silently be asserted at
the earlier r0=2^1000000.

Set y=loglog r,p*=1/sqrt(8A),c=2sqrt(p*y)-2. Since A>=2, p*<=1/4;
eventually c admissible. Repair exponent is -p*y/2; exterior exponent
is -p*y/2+sqrt(p*y)-1/2. Polynomial factor is absorbed into exp(Csqrt y).
Thus gamma*=p*/2=1/(4sqrt(2A)), and

    nu(k)/W(k)<=1+C(log k)^-gamma* exp(Csqrt(loglog k)),

in both parities by the exact doubling lift. Every fixed gamma<gamma*
therefore gives O_gamma((log k)^-gamma). Old common-A balancing yields
1/(8A+1), so new order is A^-1/2 versus A^-1. Exact equality is not proved.

## Root's optional completely numerical corollary to audit

The explicit sharp MGF can use constant2^26 and a0=1/4: after square
completion, full-line Gaussian moments bound the integral by
16+36u+8u^2+32u^3<=64(1+u)^3;64e^12<2^26.
This gives the packing main prefactor2^88 J^3, exponentJ^2p^2(c+2)^2.
After compilation use2^92 J^3, whose logarithm is below2^21.
The previously certified A=2^2097152 dominates J^2 and the weighted raw
error exponent after numerical constants are absorbed.

For a dyadic pure-power corollary, take

    p=1/(4sqrt A)=2^-1048578,
    gamma_new=p/4=2^-1048580,
    k_new=ceil exp(exp(2^1048616)).

For k>=k_new, r>=sqrt k and y>=2^39 sqrt A, so z=p*y>=2^37.
Choose c=2sqrt z-2. Then Ap^2=1/16, repair exponent=-3z/4 and tail
exponent=-z/2+sqrt z-1/2. The logarithm of the main constant is<2^21;
log(constant*64z^3)-z/2<-log4 at z>=2^37. The tail with its floor
constant2048 is also below(1/4)e^-z/4. Cycle/weighted errors are below
another quarter. Conversion log r>=0.5log k costs2^gamma<=5/4.
Thus candidate C1 corollary is nu(k)<=W(k)(1+(log k)^-gamma_new)
for k>=k_new. This remains a draft until the weighted error and threshold
calculations receive independent review.
