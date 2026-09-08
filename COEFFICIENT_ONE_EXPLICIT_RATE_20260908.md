# Explicit logarithmic rate for the PBBS construction

Date: 2026-09-08. The quantitative argument was supplied by the user.
The numerical constants below were extracted and checked internally by
Codex and its mathematical subagents. This is a proposed-proof extension
on the manuscript's finite PBBS inputs; it is not external or formal
certification of those inherited structural lemmas.

All logarithms are natural. Write W(k)=binomial(k,floor(k/2)).

## 1. Completely numerical conclusions

Set

\[
 A=2^{2097152},\qquad \gamma=2^{-2097160},\qquad
 k_0=\left\lceil\exp\!\left(\exp(2^{2097165})\right)\right\rceil.
\]

Then the finite PBBS inputs imply

\[
 \boxed{\nu(k)\le W(k)\left(1+(\log k)^{-\gamma}\right)
          \quad(k\ge k_0).} \tag{1}
\]

Thus the multiplier in the large-dimension error term is explicitly
**C=1**. A version valid in every integer dimension k>=2 is

\[
 \boxed{0\le\nu(k)-B(k)
       \le\frac{2^{60}W(k)}{(\log k)^{\,2^{-2097160}}}.} \tag{2}
\]

These constants are deliberately very conservative. They quantify the
asymptotic convergence; they do not give a useful numerical improvement
at k=17. The recorded finite bounds remain

\[
                  24313\le\nu(17)\le25745.
\]

## 2. Explicit analytic inputs

Put R=sqrt(r), x=log r, y=loglog r. All growing-scale statements below
hold for r>=2^1000000 and 1<=c<=sqrt(y). Use

\[
 K=\lfloor r^{1/100}\rfloor,\quad
 S=\lfloor r^{1/50}\rfloor,\quad
 L=\lfloor r^{2/5}\rfloor,\quad
 q=\lceil Rr^{-1/100}\rceil.
\]

The uniform raw-incidence proof gives

\[
 A_0=2^{80}\exp(2^{20}),\qquad b_0=2^{-53},
\]

and, for H<=bR, b>=1,

\[
\begin{aligned}
 \mu_H:=\mathbb E[(T+2)\mathbf1_{T\le H}]
      &\le e^{A_0(b+1)^2},\\
 \Pr(T\le H,h<\epsilon R)
      &\le R^{-1}e^{A_0(b+1)^2-b_0/\epsilon^2},\\
 \mathbb E[(T+2)\mathbf1_{T\le H,F_S>0}]
      &\le e^{A_0(b+1)^2}S^2/r \quad(1\le S\le R).
\end{aligned} \tag{3}
\]

These are finite uniform estimates, not substitutions into a fixed-b
big-O. The proof uses geometric depth floor(2^-24 R/Q), independent
of b, to obtain h>=2^-25 R/Q. A second depth
floor(2^-24 R/((b+1)Q)) makes the actual composition queries legal.
The full original profile has Pr(Q>u)<=exp(12-u^2/4). Explicit energy
loss 2^18 and the coefficient-six path majorant lead to
J=2^38 exp(2^19), with A_0=16J^2. The complementary sector where the
query depth is shorter than S is included in (3).

The complete numerical derivation, including every constant, is
[the uniform-cutoff proof](scratch/PBBS_QUANTITATIVE_CUTOFF_UNIFORMITY_AND_EXPLICIT_CONSTANTS_INDEPENDENT_AUDIT_20260908.md).

The exact shifted-triangle success vector can be represented by rowwise
sampling without replacement. Matching every success intersection proves
equality of the full binary-vector law on its safe exposed fibre. Coupling
the auxiliary rows to independent Bernoulli rows yields, at these scales,

\[
 d_{TV}(Y_1,\ldots,Y_K;\text{renewal vector})
       \le8r^{-1/100}. \tag{4}
\]

The renewal masses are u_n=1/(n+1). For the number R_K of renewals through
K, including zero, the explicit first-gap tail and reciprocal summation
give

\[
 \mathbb E[R_K^{-1}]
     \le\frac{600(1+\log\log r)}{\log r}. \tag{5}
\]

The stationary unnormalized peak flux obeys

\[
                         M_L\le11000000r^{-3/20}. \tag{6}
\]

For (6), the explicit regular-profile event fails with probability at
most (4L+6)r^-200. On it, d_L<=5r/L^2 and the canonical zero-triangle
probability is at most 250000 L^-7/8, by an Abel sum starting at depth
1024. The exceptional contribution is bounded without a normalizer.
See [the complete vector, renewal and flux proof](scratch/PBBS_QUANTITATIVE_VECTOR_RENEWAL_AND_FLUX_EXPLICIT_CONSTANTS_20260908.md).

## 3. The actual occupied-edge bound

Use the unnormalized physical incidence measure

\[
 \mathfrak I_t(f)=\mathbb E_D\left[
  \mathbf1_{T\le t}\sum_{j=0}^{T+1}f(D,j)\right].
\]

Let U_t be the occupied-edge union and K_t(e) the number of traces in
the same cutoff family covering e. Exactly

\[
                     |U_t|/W_r=\mathfrak I_t(1/K_t). \tag{7}
\]

On the safe base-zero fibre through L, the lifetime is a function of
the exposed depth-L core alone. Thus its shortness and offset tests
introduce no further weighting on the upper free composition rows.
The collar and no-repeat tests are measurable in the exposed environment.
Consequently (4)-(5) integrate with multiplier mu_t, not its reciprocal.

Let H_* =floor((c+1)R), and E_c=exp(A_0(c+2)^2). The finite stationary
identities hold for this growing finite K. They give the following raw
errors, before a cutoff-margin strip:

| Event or comparison | Upper bound |
|---|---:|
| Positive base triangle | E_c r^-1/5 |
| First K boundaries extend beyond L | 44000000(c+3)r^-1/25 |
| Boundary starts after the sampled edge | 11000000r^-7/50 |
| Extra endpoint time exceeds q | 22000000(c+3)r^-13/100 |
| Extra-slot collar | 384 E_c r^-1/100 |
| Success-vector comparison | 8 E_c r^-1/100 |

The collar constant comes from the exact Abel inequality
sum_(u=S)^(L-1) ell_u/r_(u+1)<=192/S. Profile failure costs at most
(H_*+2)(4L+6)r^-200. Non-GOOD restoration costs at most 2/(2r+2)^9;
positive top gaps are already included in the base-triangle row.
Using c+3<=E_c, their sum is at most 2^28 E_c r^-1/100.

All successful remaining candidates are distinct native births whose
traces contain the sampled edge and whose lifetimes are at most T+q.
They are therefore in the SAME family if t-T>=q. This leaves the strip
I_t(0<=t-T<q).

Average t over the integers from ceil(cR) through floor((c+1)R).
A fixed birth belongs to the strip for at most q+1 such cutoffs, so its
average raw cost is at most 8 E_c r^-1/100. No normalized Palm laws are
averaged. Together with (5), y>=1 and r^-1/100<=y/log r, this proves
that at least one such actual cutoff satisfies

\[
 \boxed{|U_t|/W_r\le 2^{40} e^{A_0(c+2)^2}
                         \frac{\log\log r}{\log r}.} \tag{8}
\]

The coarse multiplier 2^40 exceeds the sum of the displayed constants.
[The physical-incidence and compiler audit](scratch/PBBS_QUANTITATIVE_RATE_INCIDENCE_COMPILER_INDEPENDENT_AUDIT_20260908.md)
checks the conditional fibre, stationary measure, finite margins, and
same-family cutoff calculation in detail.

## 4. Packing and a literal word

Let P_t(r) be the largest edge-disjoint family of traces with T<=t.
Split at height epsilon R. Equation (3) bounds the number of low-height
births; each other packed trace uses at least epsilon R distinct edges.
Thus

\[
 \frac{RP_t(r)}{W_r}
  \le E_c e^{-b_0/\epsilon^2}+\frac{|U_t|}{\epsilon W_r}.
\]

Take epsilon^2=b_0/(2y), so epsilon^-1=2^27 sqrt(y). Equation (8) gives

\[
          RP_t(r)/W_r\le2^{68} E_c y^{3/2}/\log r. \tag{9}
\]

The finite compiler with H=t+1, including its exterior word, is

\[
 \nu(2r+1)\le W_r+2H\operatorname{Cat}_r
          +2(5H-1)P_t(r)+2L_r(r-H).
\]

Here Cat_r=W_r/(2r+1), 2H<=r+1, and the fully finite exterior estimate is
2L_r(r-H)/W_r<=1024 exp(-(H-1)^2/(8r)). The constant 1024 follows
from the original chain-pair formula and an explicit Gaussian-sum bound;
it introduces no asymptotic threshold. Hence

\[
 \frac{\nu(2r+1)}{W_r}
 \le1+\frac{c+2}{\sqrt r}
 +10(c+2)2^{68} e^{A_0(c+2)^2}\frac{y^{3/2}}{\log r}
 +1024e^{-c^2/8}.
\]

The polynomial prefactor is at most exp(128(c+2)^2). Since
log 2>=2/3 and log 2<=1,

\[
 \log(2^{2097152})\ge(2/3)2097152
       >2^{20}+81\ge\log(2A_0).
\]

Thus A=2^2097152 exceeds A_0+128, proving the explicit two-parameter bound

\[
 \boxed{\frac{\nu(2r+1)}{W_r}\le
  1+\frac{c+2}{\sqrt r}
   +e^{A(c+2)^2}\frac{(\log\log r)^{3/2}}{\log r}
   +1024e^{-c^2/8}.} \tag{10}
\]

Its stated domain is r>=2^1000000 and 1<=c<=sqrt(loglog r).
All length, distinct-slot, nonwrapping and epsilon margins hold there.
The proof constructs a deterministic word: compile every admissible
integer aperture and retain the shortest. The existence of a suitable
cutoff in (8) does not require knowing it in advance.

## 5. Fully numerical exponent and threshold

Suppose y>=4096A and choose c=sqrt(y/(16A)). It is admissible and c>=2.
Then exp(A(c+2)^2)<=exp(y/4). With gamma=1/(256A), the three excesses
in (10) are each at most one quarter of exp(-gamma y):

- The tail is 1024 exp(-2gamma y); gamma y>=16>log4096.
- The middle term is y^(3/2)exp(-3y/4); log y<=y/4 for y>=16 suffices.
- The cycle term is at most 2sqrt(y)exp(-exp(y)/2), which is smaller
  than the same quarter for y>=16.

For k>=k_0 from section 1, the odd source 2r+1 is k or k-1, and
r>=sqrt(k). Consequently y>=8192A-log2>=4096A. The trimmed lift from
2r+1 to 2r+2 has exactly twice the word length, while W(2r+2)=2W_r.
It introduces no relative error. Finally

\[
 \tfrac34(\log r)^{-\gamma}
   \le\tfrac34\,2^\gamma(\log k)^{-\gamma}
   \le\tfrac{15}{16}(\log k)^{-\gamma}
   <(\log k)^{-\gamma}.
\]

This proves (1) in both parities, with C=1 and the stated k_0.

## 6. Extending the numerical inequality to all k>=2

The previously proved uniform finite construction gives
nu(k)+1<=4*2^k/sqrt(k+1), while
W(k)>=2^k/sqrt(2(k+1)). Therefore nu(k)/W(k)<4sqrt(2)<6 for every k.
For 2<=k<k_0, the ceiling in k_0 gives

\[
 \log\log k<8192A+1,\qquad
 (\log k)^\gamma<e^{32+\gamma}<3^{33}.
\]

Hence (nu(k)/W(k)-1)(log k)^gamma<5*3^33<2^60. For k>=k_0, (1)
is stronger. Since B(k)>=W(k) and B(k)<=nu(k), equation (2) follows.
The uniform finite construction is proved in
[the earlier finite-completion audit](scratch/USER_FINITE_CYLINDER_COMPLETION_WITHOUT_DIMENSION_FLOOR_20260908.md).

## 7. Scope and subsequent proposals

This supplies explicit constants for the user's first quantitative rate.
It removes the unspecified convergence rate in the earlier proposed
coefficient-one manuscript, conditional on the same finite structural
inputs. The quantitative estimates received root and independent internal
reviews; their proof notes are linked above. The user's unavailable
sandbox verifier packages were not run or claimed as independent evidence.

The later recency-state splice and terminal-incidence/profile-capping
proposal are separate deductions. They do not enter the proof of (1)-(2).
The terminal-incidence refinement has since passed internal review and
gives the stronger numerical result in
[the terminal-rate proof](COEFFICIENT_ONE_TERMINAL_RATE_20260908.md).
Neither rate proves nu(k)=B(k), and no 24313-letter word on 17 coordinates
is supplied here.
