# Terminal charging, profilewise clipping, and a sharp fractional moment

Date: 2026-09-08. Independent audit by `exact_b_induction`.
Method: pure finite counting, probability inequalities, and local source
reads. No mathematical computation or unavailable verifier was run.

Internal review: root completed a full independent read and passed this
audit on 2026-09-08. Root additionally proposed retaining the stronger
A_err=A0+64 error constant below, leaving explicit room for the compiler
multiplier. This is internal review, not external certification.

This audits the proposal transcribed in
`scratch/USER_PBBS_TERMINAL_CHARGING_CLAIM_20260908.md`.
Verdict: the terminal/profilewise argument and the stated sharp-MGF
constants pass. The error exponent can use the existing numerical
A=2^2097152 already at r>=2^1000000, before any later absorption of the
error into a pure power of r.

## 1. Exact profile frequencies and terminal counting

Let Pi be the full original pruning profile. It is invariant under the
physical PBBS maps, including the step-two root shift. In particular its
height h and the envelope Q are constant on each physical component.
This is the accepted invariance used explicitly in
`scratch/PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md`, Section 6.

Let W_Pi be the number of physical edge positions with profile Pi. The
physical birth dictionary gives exactly the same profile frequencies
as the uniform original Dyck root:

\[
 \Pr_D(\Pi)=W_\Pi/W_r.
\]

For every profile of positive mass, define the conditional unnormalized
incidence measure

\[
 I_t^\Pi(f)=\mathbb E_D\left[
   \mathbf1_{T\le t}\sum_{j=0}^{T+1}f(D,j)\mid\Pi\right],
 \qquad \mu_t(\Pi)=I_t^\Pi(1).
\]

Write u_t(Pi) for the occupied edge fraction inside the physical components
of that profile. Thus 0<=u_t(Pi)<=1. All cutoffs below are smaller than
the physical cycle lengths: r>=2^1000000 and
1<=c<=sqrt(log log r) imply H_*+2<=r<2r+1, where
H_*=floor((c+1)sqrt(r)). Every short trace therefore covers each of its
edges once.

At each occupied edge choose the containing trace whose start is latest
in the unwrapped backward history ending at that edge, breaking any ties
deterministically. Let terminal(D,j) indicate that the sampled base trace
was chosen. Exactly one incident trace is chosen at every occupied edge.
Hence, separately for every profile,

\[
                      u_t(\Pi)=I_t^\Pi(\mathbf1_{\rm terminal}).
                                                               \tag{1.1}
\]

For any invariant nonnegative weight omega(Pi), the weighted identity is
E_Pi[omega u_t]=I_t(omega 1_terminal). This is a finite counting identity;
it does not identify an incidence-biased root with a fresh uniform root.

## 2. Why one later success defeats terminality

Retain the exact safe base-zero fibre, the common finite deep boundaries,
the exposed no-repeat condition, the collar, and the cutoff margin from
the existing quantitative proof. The sources are

* `scratch/PBBS_QUANTITATIVE_RATE_INCIDENCE_COMPILER_INDEPENDENT_AUDIT_20260908.md`,
  Sections 1-4;
* `scratch/PBBS_QUANTITATIVE_VECTOR_RENEWAL_AND_FLUX_EXPLICIT_CONSTANTS_20260908.md`,
  Sections 1-4.

They retain the original conditional free composition rows after the
full profile, deeper rows, and sampled offset are exposed. Their complete
success-vector TV bound is 8r^(-1/100), uniformly on every feasible safe
environment.

On the physical good event, a success Y_k with 1<=k<=K gives a distinct
native birth at positive time t_k/2 after the base birth, no later than
the sampled edge. Its trace contains that edge. Under the margin t-T>=q
it belongs to the same cutoff-t family. Therefore

\[
 \mathbf1_{\rm terminal}
      \le\mathbf1_{Y_1=\cdots=Y_K=0}
                 \quad\hbox{on the physical good event}.        \tag{2.1}
\]

One does not condition the free-row law on terminality. Instead apply
the pointwise implication (2.1), and then integrate the upper bound under
the original incidence measure. The good-event restrictions are measurable
in the already exposed environment; they do not select on the remaining
success outcomes.

For the coupled renewal process, no success in 1,...,K is precisely the
event that its first gap G exceeds K. The established exact gap tail gives

\[
 \Pr(G>K)\le1/\log(K+1)\le100/\log r,
                 \qquad K=\lfloor r^{1/100}\rfloor.              \tag{2.2}
\]

The floor causes no loss: K+1>r^(1/100). Thus the reciprocal-renewal
log-log factor is absent.

## 3. Cutoff averaging is valid at each fixed profile

Put R=sqrt(r), d=c+2, and H_*=floor((c+1)R). Let Hset contain the integers
ceil(cR),...,floor((c+1)R), and set t0=floor(cR). Its size is at least R/2.

For a fixed profile, let e_t(Pi) be the actual conditional raw incidence
mass of the union of physical bad events, plus the bounded conditional
TV defect. Include the cutoff-margin strip among the physical bad events.
This definition is deliberate: a conditional Markov majorant may be much
larger and is not substituted for the actual mass. The two terms obey

\[
                       0\le e_t(\Pi)\le2\mu_{H_*}(\Pi)
                                           \le2(H_*+2).          \tag{3.1}
\]

Equations (1.1)-(2.2), conditional on the same profile, yield

\[
 u_t(\Pi)\le\frac{100\mu_{H_*}(\Pi)}{\log r}+e_t(\Pi).
\]

For a fixed original birth of lifetime T, the strip 0<=t-T<q occurs
for at most q+1 choices of t. Counting those choices before averaging
over roots proves, separately at every Pi,

\[
 \mathop{\rm av}_{t\in Hset} I_t^\Pi(0\le t-T<q)
       \le\frac{2(q+1)}R\mu_{H_*}(\Pi).                         \tag{3.2}
\]

Define ebar(Pi)=average_t e_t(Pi). Because occupied sets are nested,
u_t0(Pi)<=average_t u_t(Pi). Consequently

\[
 u_{t0}(\Pi)\le
    \min\left\{1,\frac{100\mu_{H_*}(\Pi)}{\log r}
                         +\overline e(\Pi)\right\}.             \tag{3.3}
\]

No profile-dependent cutoff is selected. The desired cutoff t0 is fixed,
and its monotonicity allows the profilewise average. No Markov or stationary
clock estimate is asserted after a nonstationary conditioning: the old
unconditional flux estimates are used only to bound E ebar below.

## 4. The profile weight controls a packing without a height split

Set omega=1+R/(h+2). Every trace has T+2>=h+2 distinct edges, all of the
same invariant profile. Its total omega weight is therefore at least R.
For any edge-disjoint packing, summing these weights and then enlarging
to the entire occupied set gives

\[
 \frac{R P_{t0}(r)}{W_r}\le\mathbb E_\Pi[\omega(\Pi)u_{t0}(\Pi)].
                                                               \tag{4.1}
\]

The previously proved geometric envelope bound h>=2^-25 R/Q gives
omega<=2^26 Q. The existing global conditional probability estimate,
with b=c+1, gives the explicit conditional raw bound

\[
 \mu_{H_*}(\Pi)
       \le2^{26}d^2Q\exp(JdQ),
 \qquad J=2^{38}\exp(2^{19}).                                  \tag{4.2}
\]

The original uniform profile law, not the Palm law, is the expectation
in (4.1). Its incidence bias remains visible in the factor (4.2).

## 5. Numerical weighted-error bound at the original threshold

Let A0=2^80 exp(2^20), E_c=exp(A0 d^2), and r>=r0=2^1000000.
The explicit error table in `COEFFICIENT_ONE_EXPLICIT_RATE_20260908.md`,
Section 3, sums to at most 2^28 E_c r^(-1/100) before the strip.
Its averaged strip is at most 8E_c r^(-1/100). Thus the actual masses
defined in Section 3 satisfy

\[
 \mathbb E\overline e\le2^{29}E_c r^{-1/100},\qquad
 \overline e\le2(H_*+2)\le4dR.                                \tag{5.1}
\]

Put M=r^(1/800). Below this envelope cutoff, omega<=2^26 M, so

\[
 \mathbb E[\omega\overline e\mathbf1_{Q\le M}]
        \le2^{55}E_c r^{-7/800}.                              \tag{5.2}
\]

The previous explicit envelope audit proves
Pr(Q>x)<=exp(12-x^2/4) and
E[Q 1_(Q>M)]<=exp(22-M^2/8). Therefore (5.1) gives

\[
 \mathbb E[\omega\overline e\mathbf1_{Q>M}]
        \le2^{80}dR\exp(-r^{1/400}/8)
        \le2^{80}r\exp(-r^{1/400}/8).                         \tag{5.3}
\]

Here d<=R on the stated c,r domain. For a wholly numerical check, write
x=log r>=500000. The cubic term of the exponential series implies
e^(x/400)>=32x, because x^2>=32*6*400^3. Thus the last expression in
(5.3) is at most 2^80 r^-3<=r^-2.

Set A_err=A0+64. The bound (5.2) is at most half of
exp(A_err d^2)r^(-1/400), since 2^55<=exp(64d^2)/2 for d>=3;
the same half-bound holds for r^-2 at r>=r0. Hence

\[
 \boxed{\mathbb E[\omega\overline e]
           \le\exp(A_{\rm err}(c+2)^2)r^{-1/400},
       \qquad A_{\rm err}=A_0+64.}                           \tag{5.4}
\]

The existing A=2^2097152 satisfies A>A0+128, so it also bounds this
weighted error with explicit room for later multipliers. Equation (5.4)
is valid at r0 itself. It does not claim that the factor exp(A_err d^2)
can be absorbed into r^(-1/1000) at r0; that later step needs the larger
threshold already identified in the user transcription.

## 6. Sharp MGF with no constant loss in the quadratic exponent

For 1<=v<=2 and u>=0, tail integration and
x^(v-1)<=1+x, x^v<=x+x^2 give

\[
 \mathbb E[Q^v e^{uQ}]
  \le e^{12}\int_0^\infty
        [2+(2+u)x+ux^2]e^{-x^2/4+ux}\,dx.
\]

Complete the square as -x^2/4+ux=u^2-(x-2u)^2/4 and put z=x-2u.
Use x<=2u+|z| and x^2<=8u^2+2z^2, then enlarge to the full real line.
The Gaussian integrals obey

\[
 I_0=2\sqrt\pi<4,\qquad I_1=4,\qquad I_2=4\sqrt\pi<8.
\]

The resulting polynomial is at most
16+36u+8u^2+32u^3<=64(1+u)^3. Since 64e^12<2^26,

\[
 \boxed{\mathbb E[Q^v e^{uQ}]
        \le2^{26}(1+u)^3e^{u^2},
             \quad1\le v\le2,\ u\ge0.}                        \tag{6.1}
\]

The quadratic coefficient is exactly 1=1/(4a0) for a0=1/4.
For the numerical prefactor one may use e<3 and 3^3<2^5, giving
e^12<2^20. No asymptotic MGF or unknown absolute constant is used.

## 7. Clip before averaging, then use the fractional moment

For z,e>=0, min(1,z+e)<=min(1,z)+e. For 0<p<=1,
min(1,z)<=z^p. Apply both pointwise to (3.3), then (4.1)-(4.2).
The main term is at most

\[
 \frac{2^{26}(100\cdot2^{26})^p d^{2p}}{(\log r)^p}
                  \mathbb E[Q^{1+p}e^{JpdQ}].
\]

Equation (6.1) applies because 1+p belongs to [1,2]. Using
(100*2^26)^p<=2^33 and (1+Jpd)^3<=(2Jd)^3 gives

\[
 \boxed{\frac{R P_{\lfloor cR\rfloor}(r)}{W_r}
   \le2^{88}J^3(c+2)^{2p+3}
        \frac{e^{J^2p^2(c+2)^2}}{(\log r)^p}
          +e^{A_{\rm err}(c+2)^2}r^{-1/400}.}                  \tag{7.1}
\]

All estimates are uniform for r>=r0, 1<=c<=sqrt(log log r), 0<p<=1.
The same A=2^2097152 dominates both J^2 and A_err. Thus replacing the
two exponents by A yields the proposed common-A inequality.

The compiler's packing factor is at most 10(c+2), so its main numerical
prefactor can be 2^92 J^3 and its polynomial can be (c+2)^6. Indeed
2p+4<=6 and 10<16. Its logarithm is

\[
 \log(2^{92}J^3)=206\log2+3\cdot2^{19}<2^{21}.
\]

For the error term, 10(c+2)<=exp((c+2)^2) for c>=1. The compiler error
therefore has exponent at most (A0+65)(c+2)^2, which is still smaller
than A(c+2)^2. Thus retaining the common A after compilation uses the
proved numerical gap and does not silently discard the multiplier.

The subsequent optimized p,c choice and the proposed final k-threshold
are separately audited by the structure agent. This note certifies the
profilewise, weighted-error, and sharp-MGF inputs, rather than silently
assuming their conclusion from the previous reciprocal-renewal proof.

## 8. Boundaries of the conclusion

The terminal assignment is to the SAME all-short cutoff family; the
averaged cutoff strip is explicitly charged. The full-profile invariant
is needed to use the original Q tail after clipping. Error masses are
actual conditional incidence masses, not conditional versions of global
Markov estimates. The free rows retain the original base-zero fibre law;
terminality is never imposed as extra conditioning.

With those conditions, no cross-profile sampling, unstated normalizer,
or exchange of a fixed-parameter limit with a growing parameter remains
in this argument. It gives a quantitative construction bound, not exact
equality nu(k)=B(k).
