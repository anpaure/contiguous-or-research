# Uniform PBBS cutoff estimates with fully explicit constants

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.
Method: pure proof and local source reads; no mathematical execution.

Internal review: root completed an independent full-file read and checked
the energy, variation, denominator, moment, path, and complementary-depth
constants on 2026-09-08; PASS, with no numerical gap found. This is an
internal proof audit, not external certification. Frontier's independent
numerical audit of Sections 2-7 also passed on 2026-09-08, with no change
required: it independently expanded the energy debit and checked the
MGF, clock, lower-tail, and complementary-depth constants. Neither review
is external certification.

This audits Section 4, (15)-(19), of the user's quantitative proposal,
transcribed in `scratch/USER_PBBS_QUANTITATIVE_RATE_CLAIM_20260908.md`.
The two-depth argument is valid. The complementary short-query-depth
sector has the explicit proof in Section 7 below. No unavailable linked
proof or fixed-parameter limit is assumed.

## 1. Numerical statement and precise upstream inputs

Put R=sqrt(r), r>=1, let b>=1, and let H be any nonnegative integer with
H<=bR. Let T include the consuming update; a trace has T+2 edges.
The height is h. Write F_S for the original triangle sum through depth S,
using the globally defined last-row and post-extinction conventions in
`pbbs_uniform_early_triangle_incidence.md`, Section 1.

The following choices work:

\[
\begin{aligned}
 E&=2^{18},& B_*&=64\exp(2E),\\
 D_*&=2^{12}\exp(2^{19}),& J_*&=2^{38}\exp(2^{19}),\\
 A_0&=2^{80}\exp(2^{20})=16J_*^2,& b_0&=2^{-53}.
\end{aligned}                                                    \tag{1.1}
\]

In particular, with multiplicative constant C_raw=1,

\[
\begin{aligned}
 \mathbb E[(T+2)\mathbf1_{T\le H}]
    &\le \exp(A_0(b+1)^2),\\
 \Pr(T\le H,\ h<\epsilon R)
    &\le R^{-1}\exp(A_0(b+1)^2-b_0/\epsilon^2),\\
 \mathbb E[(T+2)\mathbf1_{T\le H,F_S>0}]
    &\le \exp(A_0(b+1)^2)S^2/r,
                       \qquad 1\le S\le R.
\end{aligned}                                                    \tag{1.2}
\]

The middle bound holds for every epsilon>0. These bounds are uniform for
all the stated finite r,b,H,S. They consequently apply throughout
b<=O(sqrt(log log r)) without any new limiting argument.

The numerical inputs, rather than unnamed absolute constants, are:

1. The envelope in `scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`,
   Section 3, equations (5)-(7), with C0=64 and p=64/6.
2. The coarse-profile consequences in that note, Section 4, (9)-(10).
3. The exact original-row clock recurrence and path comparison with
   coefficient 6 in
   `review/COEFFICIENT_ONE_REVIEW_20260908/sources/essential/c69c/research_round1/pbbs_quantitative_clock_polylog_short_mass.md`,
   Section 4, (14)-(17). The structural physical clock theorem supplies
   its identification with actual clocks when the circumference bounds
   checked below hold.
4. Monotonicity and convexity of the exact pruning profile. Section 3
   below expands the deterministic energy proof in
   `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_bounded_gaussian_short_incidence.md`,
   Section 2, replacing all its unspecified constants by numbers.

## 2. Absolute envelope moments and an independent geometric depth

The full original profile determines a>=1 with

\[
 \Pr(a>1+x)\le4\sum_{j\ge1}
  \exp\left[-\frac{32}{3}(x+\sqrt{\log(j+2)})^2\right]
 \le4e^{-(32/3)x^2},\qquad x\ge0.                       \tag{2.1}
\]

The last sum of powers is at most one by comparison with the integral
of x^(-32/3) from 2 to infinity. Put Q=a+sqrt(log(a+2)); then 1<=Q<=3a.
For u>=6, (2.1) gives Pr(Q>u)<=4e^(-u^2/4). Enlarging the prefactor
also covers 0<=u<6, so

\[
                   \Pr(Q>u)\le e^{12-u^2/4}.             \tag{2.2}
\]

Tail integration yields E exp(Q^2/8)<=1+e^12<=e^13. For 0<=m<=6,
x^m exp(-x^2/16)<=(8m)^(m/2)<=2^17, with m=0 interpreted as one.
Also tx<=x^2/16+4t^2. Therefore

\[
 \mathbb E[Q^m e^{tQ}]\le e^{32+4t^2},\quad 0\le m\le6,
 \qquad
 \mathbb E[Qe^{tQ}\mathbf1_{Q\ge u}]
       \le e^{22+8t^2-u^2/8}.                           \tag{2.3}
\]

The second inequality is Cauchy-Schwarz applied to the first one with
m=2 and 2t, and (2.2). No independence between profile variables is used.

Take kappa_g=2^-24 and d_g=floor(kappa_g R/Q). The explicit envelope is

\[
 |r_s-r/(s+1)|\le64R
       [a+\sqrt{\log(2+R/(s+1))}].
\]

For d_g>=2 the source floor calculation gives coarse comparability
through 2d_g+1, because

\[
 3\delta_{\kappa_g}
 =192\kappa_g[1+\sqrt{\log(8/\kappa_g)}]
 <21/2^{18}<1/4.
\]

Thus r_(2d_g)>0 and h>2d_g>=kappa_g R/Q. If d_g<2, then
kappa_g R/Q<2 and h>=1. Both cases give the pointwise bound

\[
                    h\ge 2^{-25}R/Q.                    \tag{2.4}
\]

This depth is independent of b. Replacing it by the shorter clock depth
would lose an additional factor b in the exponent.

## 3. Numerical coarse-profile energy bounds

Suppose d>=2 and

\[
 \frac{3r}{4(s+1)}\le x_s=r_s\le\frac{5r}{4(s+1)},
                      \qquad 0\le s\le d+1.
\]

Set v_s=x_s-x_(s+1), a_s=v_s/x_s for 0<=s<=d, and
ell_s=v_s-v_(s+1). Convexity and comparison with floor(s/2) show

\[
 v_s\le\frac{8r}{(s+1)^2},\quad
 a_s\le\frac{16}{s+1},\quad 1-a_s\ge1/4.              \tag{3.1}
\]

For s>=2 the comparison is
v_s<=x_floor(s/2)/(s-floor(s/2))<= (15/2)r/(s+1)^2;
s=0,1 follow directly from v_s<=r. The last inequality follows from
x_(s+1)/x_s >=(3/5)(s+1)/(s+2)>=3/10.

Consequently sum a_s^2<=512. Moreover
(a_(s+1)-a_s)_+<=a_s^2/(1-a_s), so the total variation of the finite
sequence is at most 1+8*512<8192. For
H_(u,d)=sum_(s=u)^(d-1)1/(s+1), logarithmic telescoping gives

\[
 \left|\sum_{s=u}^{d-1}a_s-H_{u,d}\right|\le2048,
 \qquad
 \sum_{s=u}^{d-1}(s+1)a_s^2\ge H_{u,d}-4096.         \tag{3.2}
\]

Indeed -log(1-a)-a<=a^2/[2(1-a)]<=2a^2; the endpoint coarse-ratio
and harmonic-integral errors are each at most one. Weighted Cauchy-Schwarz
then proves the second inequality, also when its right side is negative.

The exact identity ell_s/x_s=a_s-a_(s+1)+a_sa_(s+1) has two harmonic
contributions. Replacing a_sa_(s+1) by a_s^2 in weights between zero and
s+1 costs at most 16*8192=2^17. For weights s+1, the linear telescoping
boundary costs at most 2048+16. For weights s-t on t<s<d, the same
linear bound applies, and replacing the quadratic weight s+1 by s-t
costs at most

\[
 (t+1)\sum_{s=t+1}^{d-1}a_s^2
       \le256(t+1)\sum_{s=t+1}^{\infty}(s+1)^{-2}\le256.
\]

The harmonic sum H_(t+1,d) differs from log(d/(t+1)) by at most one.
It follows, with room to spare, that both half-weighted sums

\[
 \frac12\sum_{s<d}(s+1)\frac{\ell_s}{x_s},\qquad
 \frac12\sum_{t<s<d}(s-t)\frac{\ell_s}{x_s}
\]

are at least their respective logarithms log d and log(d/(t+1)), minus
2^17. An empty tail is harmless.

For m=3,4, one summation by parts in ell_s=v_s-v_(s+1), dropping its
nonpositive final term and using (3.1), gives explicitly

\[
 \sum_{s<d}(s+1)^3\ell_s\le24rd,\qquad
 \sum_{s<d}(s+1)^4\ell_s\le32rd^2.                    \tag{3.3}
\]

Now let q_s=ell_s/(x_s+x_(s+2)+1). Since

\[
 \frac{\ell_s}{2x_s}-\frac{\ell_s}{4x_s^2}
   \le q_s\le\frac{\ell_s}{x_s},
\]

the total weighted lower-bound correction is at most
(4/(9r^2))*24rd<=16 for d<=r. Therefore E=2^18 safely gives

\[
 \Phi=\sum_{s<d}(s+1)q_s\ge\log d-E,\qquad
 A_t=\sum_{t<s<d}(s-t)q_s\ge\log\frac d{t+1}-E.       \tag{3.4}
\]

Combining q_s<=(4/3)(s+1)ell_s/r with (3.3)-(3.4) proves

\[
 B_d=\sum_{s<d}(s+1)q_se^{-2A_s}\le64e^{2E}=B_*.
                                                                    \tag{3.5}
\]

The same summation truncated at any 1<=S<=d gives

\[
 \sum_{s<S}(s+1)q_se^{-2A_s}\le B_* S^2/d^2.          \tag{3.6}
\]

## 4. Legal clock depth and numerical finite path bound

Put kappa=2^-24 and

\[
                  d=\left\lfloor\frac{\kappa R}{(b+1)Q}\right\rfloor.
\]

When d>=2, d<=d_g, so the preceding profile bounds hold through 2d+1
and h>2d. For s<d,

\[
 p_s=2r_{s+1}+1\ge r/d\ge (b+1)QR/\kappa.
\]

For a short clock take K0=ceil(H/h). Every path of total queried mass
at most K0 obeys
n_s+W_s<=3(K0+1)(s+1)<=3H/2+6d.
Hence p_s>2H+1 and p_s>=2(n_s+W_s): indeed
(b+1)/kappa>3b+12kappa, for every b>=1.
These verify separately the physical circumference condition and the
finite composition-prefix comparison. They hold for every summed path.

The exact coefficient-6 path majorant and (3.4)-(3.5) give

\[
 \Pr(T\le H\mid\text{profile})
  \le\frac1d\exp[E+6B_*(K0+1)]
  \le\frac1d\exp[D_*(1+H/h)].                        \tag{4.1}
\]

For F_S>0 and S<=d, the restricted exponential sum is
Q0[exp(theta B_d)-exp(theta(B_d-B_early))], theta=6(K0+1).
Using (3.6), x<=e^x for x>=0, and the same choice D_*, it gives

\[
 \Pr(T\le H,F_S>0\mid\text{profile})
   \le\frac{S^2}{d^3}\exp[D_*(1+H/h)].               \tag{4.2}
\]

For both inequalities D_*=2^12 exp(2^19) dominates E+24B_*.
The equivalence between early original triangle positivity and a positive
queried row uses the exact first-positive-row argument in the source
early-triangle lemma. Outside S<=d it is not asserted.

## 5. Global conditional probability and raw incidence

By (2.4), H/h<=2^25 bQ. On d>=2, the floor bound gives
1/d<=2^25(b+1)Q/R. Thus (4.1) implies

\[
 \Pr(T\le H\mid\text{profile})
  \le\frac{2^{25}(b+1)Q}{R}\exp[J_*(b+1)Q].          \tag{5.1}
\]

On d<2, kappa R/((b+1)Q)<2, so the prefactor in (5.1) already exceeds
one. Equation (5.1) is therefore global, including every small rank and
the short-query-depth sector.

Multiply by H+2<=(b+2)R, then apply (2.3) with m=1 and
t=J_*(b+1). The logarithm of the resulting bound is at most

\[
 25\log2+\log(b+1)+\log(b+2)+32+4J_*^2(b+1)^2
                   \le A_0(b+1)^2.
\]

For the last inequality use b+1>=2, b+2<=2(b+1), log x<=x^2,
and J_*^2>=16. This proves the first inequality of (1.2).

## 6. Low height and the explicit lower-tail exponent

Equation (2.4) shows that h<epsilon R implies Q>2^-25/epsilon.
Apply the truncated estimate (2.3) to (5.1). It gives

\[
 \Pr(T\le H,h<\epsilon R)
 \le\frac{2^{25}(b+1)}R
   \exp\left[22+8J_*^2(b+1)^2-\frac{2^{-53}}{\epsilon^2}\right].
\]

The prefactor and constant 22 are absorbed by A_0=16J_*^2 as above.
This proves the second inequality of (1.2), with b0=2^-53. The proof
does not discard low heights before applying the original-row clock.

## 7. The early triangle, including d<S or d<2

First suppose d>=max(S,2). Equation (4.2), its floor bound, and (2.4)
give

\[
 \Pr(T\le H,F_S>0\mid\text{profile})
 \le \frac{2^{75}(b+1)^3S^2Q^3}{R^3}
                         e^{J_*(b+1)Q}.             \tag{7.1}
\]

On the complementary sector, d<max(S,2) implies
kappa R/((b+1)Q)<max(S,2)<=2S. Consequently

\[
 \mathbf1_{d<\max(S,2)}
      \le \frac{2^{50}(b+1)^2 S^2 Q^2}{R^2}.
\]

Multiply this indicator by the GLOBAL bound (5.1) and drop F_S. The
result is exactly the right side of (7.1). Thus (7.1) controls both
disjoint profile sectors, without a factor two and without assigning an
unsafe physical meaning to repeated triangle slots.

Average using (2.3) with m=3 and multiply by H+2<=(b+2)R. The coefficient
of S^2/r is at most

\[
 2^{75}(b+1)^3(b+2)e^{32+4J_*^2(b+1)^2}
                    \le e^{A_0(b+1)^2}.
\]

For example its logarithm beyond the quadratic MGF term is at most
76+4log(b+1)+32 <=31(b+1)^2, using log2<=1 and b+1>=2;
12J_*^2>=31. This proves the last inequality of (1.2).

## 8. Raw-incidence error (23): scope and finite exponent ledger

The physical conditioning and exact shifted-vector law are independently
audited by the other agents; this section checks the unnormalized mass
and scales. The explicit vector/flux constants are in
`scratch/PBBS_QUANTITATIVE_VECTOR_RENEWAL_AND_FLUX_EXPLICIT_CONSTANTS_20260908.md`.
They hold for r>=2^1000000 and give M_L<=11000000 r^(-3/20), with
K=floor(r^(1/100)), S=floor(r^(1/50)), L=floor(r^(2/5)).

Let the largest cutoff be H<=bR and q=ceil(R r^(-1/100)). Exact stationary
flux and offset counting, with no normalization by mu_H, give:

| Bad event | Raw-incidence upper bound before numerical constants |
|---|---|
| Positive base triangle F_L | exp(A0(b+1)^2) r^(-1/5) |
| Initial boundary t_K>=L | (b+2) r^(-1/25) |
| Initial boundary after sampled edge | r^(-7/50) |
| Added endpoint duration Delta_K>q | (b+2) r^(-13/100) |
| Extra-slot collar failure | exp(A0(b+1)^2) r^(-1/100) |
| Finite-vector comparison error | exp(A0(b+1)^2) r^(-1/100) |

The first line is (1.2), not a fixed-b normalized assertion. The next
three lines follow respectively from
2(H+2)K M_L/L, K M_L, and 2(H+2)K M_L/q.
The collar source gives the finite Abel bound 192K/S before multiplication
by mu_H. The vector audit gives 8r^(-1/100). Profile-regularity failures
have raw mass at most (H+2) times their original-root probability; the
explicit concentration is far smaller than these powers.

Thus all these errors have the claimed form
exp(C(b+1)^2)r^(-1/200), uniformly for 1<=b<=O(sqrt(log log r)).
Their actual numerical prefactors, and the separate non-GOOD restoration,
must be included in the final synthesis; no hidden normalizer or random
root resampling occurs in this ledger. The rate statement follows from
the independent physical-conditioning audit together with these uniform
finite bounds, not from the older fixed-depth limit theorem.

The only constants imported without rederiving their underlying structural
theorems are explicit 64, 32/3, and the exact coefficient 6 listed in
Section 1. No unnamed absolute constant has been assigned a numerical
value in the derivation of A0, b0, or (1.2).
