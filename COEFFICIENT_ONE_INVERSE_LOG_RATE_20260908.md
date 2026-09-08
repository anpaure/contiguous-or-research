# Explicit inverse-logarithmic PBBS construction bound

Date: 2026-09-08. Status: complete internal proof review on the same finite
PBBS inputs as the proposed coefficient-one manuscript. The new finite
geometric theorem, original-composition transfer, dyadic packing and
numerical constants have separate internal audits. This is not external
or formal certification of the inherited manuscript.

The user's new clock argument removes the small logarithmic exponent.
An explicit conservative version is

\[
\boxed{\displaystyle
 \nu(k)\le W(k)\left[1+2^{400000}
             \frac{(\log\log k)^{3/2}}{\log k}\right],
 \qquad k\ge
 k_*:=\left\lceil\exp\!\left(\exp(4194304)\right)\right\rceil.}
\tag{1}
\]

All logarithms are natural. Here4194304=2^22. The coefficient and threshold
are deliberately loose, but completely numerical. The exponent of log k
is exactly one; it does not depend on the Gaussian-envelope constant.
The same error bounds (nu(k)-B(k))/W(k) from above. Exact equality with
B(k) remains open.

## 1. The finite clock theorem

For a positive decreasing convex profile a_0,...,a_(d+1), a_0=r, assume

\[
 .99\frac r{s+1}\le a_s\le1.01\frac r{s+1},\qquad
 \ell_s=a_s-2a_{s+1}+a_{s+2},\qquad
 \pi_s=\frac{2a_{s+1}}{a_s+a_{s+2}},\quad q_s=1-\pi_s.
\]

Suppose every prefix satisfies
Z_m=product_(s<m) pi_s^(s+1)<=C_Z/(m+1). At row s query
n_s=s+1+2sum_(j<s)(s-j)W_j independent geometric entries, each with
Pr(Z=j)=pi_s q_s^j, and let V_d=sum_(s<d)W_s. Then

\[
 \mathbb E z^{V_d}\le\frac{20e^{54}C_Z}{1+d(1-z)},\qquad
 \Pr(V_d\le M)\le64e^{54}C_Z\frac{M+1}{d+1}.          \tag{2}
\]

The complete proof uses the two-type backward generating functions

\[
 x_d=1,\ y_d=t,\quad
 x_s=\frac{x_{s+1}\pi_s}{1-q_s y_{s+1}^2},\quad
 y_s=y_{s+1}x_s,\quad \mathbb E z^{V_d}=y_0/t,
 \quad z=t^2.
\]

The linear comparison U_d=U_(d+1)=1,
U_s+U_(s+2)=2U_(s+1)/pi_s has the exact Wronskian formula

\[
 \frac{U_s}{a_s}=\frac1{a_d}
 -(a_d-a_{d+1})\sum_{j=s}^{d-1}\frac1{a_j a_{j+1}},
 \qquad U_s\ge\frac{d+1}{5(s+1)}.
\]

AM-GM and backward induction on both value and slope give
y_s²<=[1+(t^-2-1)U_s]^-1. At t²=1/2, summation by parts bounds
the PGF correction above the zero-path probability by e^54. For general
z>=1/2, restart the finite backward recursion at
m=floor((1-z)(d+1)/(10z)). When this is useful, x_m<=1 and y_m<=1/sqrt2,
so both terminal weights are dominated by the prefix half-PGF. This gives
(2); it does not assume a new random profile at the restart.

[The complete geometric proof](/Users/amir.nuriyev/Documents/problem/scratch/GEOMETRIC_CLOCK_FINITE_PGF_AND_PREFIX_RESTART_INDEPENDENT_AUDIT_20260908.md)
includes small depths, zero rows and z=0,1. The audited original-profile
energy gives C_Z=2exp(2^18), uniformly over every required prefix.

## 2. Transfer to actual finite compositions

Conditioned on the original full pruning profile, row s has
P_s=2a_(s+1)+1 slots and total mass ell_s. Hence

\[
 N_s=\ell_s+P_s-1=a_s+a_{s+2},\qquad
 (P_s-1)/N_s=\pi_s.
\]

These are the original rows, not the shifted free rows used in the
different physical-candidate comparison. For n distinct slots, the exact
finite row-sum law is

\[
 \Pr(W=w)=\binom{n+w-1}{w}
       \frac{(\ell)_w(P-1)_n}{(N)_{n+w}},
\]

with falling factorials. Factoring the denominator proves

\[
 \Pr_{\rm comp}(W=w)
 \le\Pr_{\rm geom}(W=w)(1-w/N)^{-n}
 \le\Pr_{\rm geom}(W=w)e^{2nw/N},\quad w\le N/2.
\]

Use R=sqrt(r), h>=2^-25 R/Q, and
d=floor(2^-40 R/((b+1)Q)), H<=bR, M=ceil(H/h).
On paths of mass at most M, the total likelihood exponent is at most
4M(M+1)(d+1)²/r<=9*2^-28<1. All slot, circumference and horizon
conditions hold. The physical event T<=H forces V_d<=M. Applying (2)
therefore gives the global bounds

\[
 \Pr(T\le H\mid\Pi)
 \le2^{73}e^{2^{18}+55}\frac{(b+1)^2Q^2}{R},\qquad
 \mu_H(\Pi)\le2^{74}e^{2^{18}+55}(b+1)^3Q^2.          \tag{3}
\]

When d<2 the displayed probability bound exceeds one, so the same
conclusion follows without interpreting an unsafe genealogy.
[The complete finite transfer audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVERSE_LOG_ORIGINAL_COMPOSITION_TRANSFER_INDEPENDENT_AUDIT_20260908.md)
checks every guard and the exact consuming-update convention.

## 3. Occupied support, actual trace lengths, and the literal word

Set K_mu=2^100 exp(2^18+64), a larger valid constant in (3), and
D0=2^33 K_mu exp(32). The audited Gaussian profile satisfies
E Q²,E Q³<=exp32 and omega=1+R/(h+2)<=2^26 Q. Latest-start charging,
the finite first-gap comparison and profilewise cutoff averaging give
both weighted and unweighted relative occupied support at most

\[
 D_0\frac{(c+2)^3}{\log r}
 +\exp((A_0+64)(c+2)^2)r^{-1/400},
 \qquad A_0=2^{80}e^{2^{20}}.                         \tag{4}
\]

Use the weighted bound only for traces of lifetime at most R. For the
remaining dyadic bands, divide occupied support by the actual lower
trace length 2^(j-1)R. The final band ends at min(2^j,c)R, so every
cutoff stays inside the proved range. Summing the bands gives

\[
 \frac{RP_{\lfloor cR\rfloor}}{W_r}
 \le2^9D_0\frac{1+c^2}{\log r}
 +3\exp((A_0+64)(c+2)^2)r^{-1/400}.                  \tag{5}
\]

In the literal compiler take H=floor(cR)+1. Its cycle openings, repair
cost and sharp finite exterior estimate yield

\[
\begin{aligned}
 \frac{\nu(2r+1)}{W_r}\le1
 &+\frac{c+1}{R}+2^{15}D_0\frac{c^3}{\log r}\\
 &+e^{(A_0+65)(c+2)^2}r^{-1/400}
 +48(1+c^2)e^{-c^2}.
\end{aligned}                                                    \tag{6}
\]

This retains the large exceptional-error coefficient explicitly. It is
valid for r>=2^1000000 and1<=c<=sqrt(loglog r), on the inherited finite
PBBS inputs. There is no new assumption of independence of physical
success indicators.

## 4. Numerical balance and both parities

For y=loglog r>=2^22-1, one has A0+65<exp(2^21) and
log(7200y)<=y/4. Consequently the exceptional term in (6) is at most
r^-1/800. It and the cycle term are each at most exp(-y).
Choose c²=y-.5log y. Then both principal terms have order
y^(3/2)exp(-y), with an odd-dimensional coefficient at most2^16D0.

For either k=2r+1 or2r+2, k>=k_* implies y>=2^22-1. The trimmed
one-coordinate lift doubles both width and word length in the even
case; converting log r to log k costs at most two. Thus the coefficient
is at most2^17D0=2^150 exp(2^18+96)<2^400000, proving (1).

[The full numerical synthesis](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVERSE_LOG_DYADIC_COMPILER_AND_EXPLICIT_NUMBERS_20260908.md)
and [its separate full-file audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVERSE_LOG_DYADIC_AND_NUMERICAL_CONSTANTS_SECOND_AUDIT_20260908.md)
give each floor, dyadic constant and threshold comparison. These proofs
were reviewed internally; the user's unavailable numerical checker was
not represented as reproduced.

The deterministic construction still enumerates the finite admissible
apertures and retains a shortest compiled word. The numerical threshold
does not make this an efficient construction for small dimensions.
The later height-adaptive finite word gives24313<=nu(17)<=24957;
that improvement is independent of this asymptotic deduction.
