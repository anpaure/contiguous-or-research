# Finite geometric-clock PGF: Wronskian, nonlinear comparison, and restart

2026-09-08. Independent pure-proof audit by `exact_b_induction` of the
finite geometric theorem in
`scratch/USER_PBBS_INVERSE_LOG_CLOCK_CLAIM_20260908.md`.
No mathematical computation or unavailable verification package was used.

Verdict: the finite theorem passes, including the Wronskian lower bound,
the direction of the nonlinear comparison, and the prefix restart.
Explicit constants are

\[
 C_{\rm pgf}=20e^{54}C_Z,
 \qquad C_{\rm budget}=64e^{54}C_Z.                  \tag{0.1}
\]

The passage from finite weak compositions to this geometric theorem and
the downstream OR-word rate are separately audited by root. They are not
assumed in the proof below.

## 1. The exact theorem and branching recursion

Let a_0,...,a_(d+1) be positive, decreasing and convex, with a0=r, and

\[
 (1-\delta)\frac r{s+1}\le a_s\le
 (1+\delta)\frac r{s+1},\qquad \delta=1/100.
\]

Define ell_s=a_s-2a_(s+1)+a_(s+2)>=0,
pi_s=2a_(s+1)/(a_s+a_(s+2)), and q_s=1-pi_s. Thus 0<pi_s<=1.
Assume, for every prefix 0<=m<=d,

\[
 Z_m=\prod_{s<m}\pi_s^{s+1}\le C_Z/(m+1).
\]

The empty prefix implies C_Z>=1. Row s uses independent geometric
entries with probability pi_s q_s^j at j>=0. Its query count and mass
satisfy

\[
 n_s=s+1+2\sum_{j<s}(s-j)W_j,\qquad V_d=\sum_{s<d}W_s.
\]

For 0<=z<=1 the conclusions are

\[
 \mathbb E z^{V_d}\le\frac{C_{\rm pgf}}{1+d(1-z)},
 \qquad
 \Pr(V_d\le M)\le C_{\rm budget}\frac{M+1}{d+1}
                          \quad(M\text{ an integer }\ge0).       \tag{1.1}
\]

The d=0 case is immediate. Assume d>=1 below.

For clarity, the recursion is exact for this geometric model. A C node
produces one C and 2Z T nodes; a T node produces one C and (2Z+1) T
nodes. Starting with one T node gives n_s nodes at row s and
1+2V_d terminal T nodes. For terminal T weight 0<t<=1, write x_s,y_s
for the two backward generating functions. Independence gives

\[
 x_d=1,\quad y_d=t,\qquad
 x_s=\frac{x_{s+1}\pi_s}{1-q_s y_{s+1}^2},\quad
 y_s=y_{s+1}x_s.                                      \tag{1.2}
\]

Therefore E z^(V_d)=y0/t when z=t^2. Every value lies in [0,1], and
x_s<=x_(s+1)<=1 and y_s<=y_(s+1). Zero ell_s simply gives q_s=0;
no division by ell_s occurs.

## 2. Wronskian formula with all small-depth cases included

Set U_d=U_(d+1)=1 and solve backward

\[
                  U_s+U_{s+2}=2U_{s+1}/\pi_s.
\]

Its values are positive and U_s>=U_(s+1), by backward induction.
The sequence a_s solves the same linear equation. Hence the Wronskian
U_s a_(s+1)-U_(s+1)a_s is constant, equal at s=d to
-Delta_d, where Delta_d=a_d-a_(d+1). Telescoping ratios gives exactly

\[
 \frac{U_s}{a_s}=\frac1{a_d}
          -\Delta_d\sum_{j=s}^{d-1}\frac1{a_j a_{j+1}}.           \tag{2.1}
\]

Let m=floor(d/2). Convexity gives
Delta_d<=(a_m-a_d)/(d-m). The profile bounds imply

\[
 \Delta_d\le\frac{r}{(m+1)(d+1)}
       \left[1+\delta\frac{d+m+2}{d-m}\right]
       \le\frac{2(1+5\delta)r}{d(d+2)}.                         \tag{2.2}
\]

For even d>=2 the ratio in brackets is at most 5; for odd d it is 3,
including d=1. Also (m+1)(d+1)>=d(d+2)/2 in both parities.
Thus (2.2) has no unhandled d=1 or floor exception.

Use the full sum in (2.1), the lower profile bounds, and
sum_(j=0)^(d-1)(j+1)(j+2)=d(d+1)(d+2)/3. Then

\[
 \frac{U_s}{a_s}\ge\frac{d+1}{r}
 \left[\frac1{1+\delta}
       -\frac{2(1+5\delta)}{3(1-\delta)^2}\right]
                  \ge\frac{d+1}{4r}.                            \tag{2.3}
\]

At delta=1/100 the bracket minus 1/4 is exactly
102499/3959604>0. Multiplying by a_s>=.99r/(s+1) proves

\[
                         U_s\ge\frac{d+1}{5(s+1)}.               \tag{2.4}
\]

## 3. The nonlinear comparison is correctly oriented

Extend y_(d+1)=t and put v_s=-log y_s. Equation (1.2) gives

\[
 v_s-2v_{s+1}+v_{s+2}=g_s(v_{s+1}),
 \quad g_s(v)=\log\frac{1-q_s e^{-2v}}{\pi_s}.                   \tag{3.1}
\]

Each g_s is increasing on v>=0. Let eta=t^(-2)-1 and
w_s=(1/2)log(1+eta U_s). AM-GM and the linear equation imply

\[
 \pi_s\sqrt{(1+\eta U_s)(1+\eta U_{s+2})}
       \le\pi_s+\eta U_{s+1}.
\]

Equivalently,
w_s-2w_(s+1)+w_(s+2)<=g_s(w_(s+1)). Both terminal values and terminal
backward slopes agree for v and w. Suppose at an induction stage that
v_(s+1)>=w_(s+1) and
v_(s+1)-v_(s+2)>=w_(s+1)-w_(s+2). Equation (3.1), the subsolution
inequality and monotonicity of g_s give the same inequality for the next
backward slope, and then for v_s itself. This proves

\[
                y_s^2\le\frac1{1+(t^{-2}-1)U_s}.                 \tag{3.2}
\]

The induction compares both value and slope; a one-variable maximum
principle with the opposite sign has not been substituted.

## 4. The half-PGF correction is less than e^54

Unwinding (3.1), or summing its discrete second differences, gives

\[
 \mathbb E 2^{-V_d}=Z_d
      \prod_{s<d}(1-q_s y_{s+1}^2)^{-(s+1)},
                       \qquad t^2=1/2.                         \tag{4.1}
\]

Equations (2.4)-(3.2) give y_(s+1)^2<=5(s+2)/(d+1). For 0<=u<1,
-log(1-u)<=u/(1-u). Since y<=1 and
q_s/pi_s=ell_s/(2a_(s+1)), the logarithm of the correction product is
at most

\[
 \frac{5}{2(1-\delta)r(d+1)}
                  \sum_{s<d}(s+1)(s+2)^2\ell_s.                \tag{4.2}
\]

Here is the finite convexity bound used in that sum. Put
v_s=a_s-a_(s+1). The same half-index comparison as in (2.2) gives
v_s<=3r/(s+1)^2 for every s>=1 in range; v0<=r. Summation by parts,
dropping its nonpositive last term, gives

\[
 \sum_{s<d}(s+2)^3\ell_s
  \le8r+\sum_{s=1}^{d-1}
     [3(s+1)^2+3(s+1)+1]\frac{3r}{(s+1)^2}
  \le21r(d+1).                                                  \tag{4.3}
\]

Indeed each interior summand is at most (9+9/2+3/4)r<15r.
Replacing (s+1)(s+2)^2 by (s+2)^3 in (4.2) therefore bounds the
correction logarithm by 105/1.98<54. Consequently

\[
                   \mathbb E2^{-V_d}\le e^{54}C_Z/(d+1).         \tag{4.4}
\]

The same argument applies to every prefix m, since its profile bounds
and its Z_m hypothesis are part of the assumptions.

## 5. Prefix restart: both terminal weights are controlled

Let z=t^2>=1/2, eta=(1-z)/z, and A=eta(d+1). If A>=10, choose
m=floor(A/10). Then 1<=m<=d, m+1<=A/5, and (2.4)-(3.2) give
y_m^2<=1/2. Also x_m<=1 by (1.2).

Now regard the first m levels as a deterministic bivariate PGF evaluated
at terminal values (x_m,y_m). The backward maps in (1.2) are increasing
in both nonnegative terminal arguments. Replace them by
(1,1/sqrt(2)). Its output is
(1/sqrt(2)) E[2^(-V_m)]. Dividing the original output by
t>=1/sqrt(2) therefore proves

\[
 \mathbb E z^{V_d}\le\mathbb E2^{-V_m}
        \le\frac{e^{54}C_Z}{m+1}
        \le\frac{10e^{54}C_Z}{A}.                              \tag{5.1}
\]

This is monotonicity of finite generating functions, not conditioning
on a random clock boundary or restarting at a purported fresh profile.

Since 1+d(1-z)<=1+A<=2A, (5.1) gives the first part of (1.1) with
C_pgf=20e^54 C_Z. If A<10, then 1+d(1-z)<11 and the trivial PGF
bound one suffices with that same constant. If z<=1/2, use monotonicity
and (4.4), noting 1+d(1-z)<=d+1. The endpoints z=0 and z=1 follow
as well; logarithms of t=0 were never needed.

## 6. The lower-budget bound and a numerical prefix constant

For integer M>=1 put z=M/(M+1). On V_d<=M, z^(V_d)>=z^M, and
z^(-M)<=e<3. The PGF bound consequently gives

\[
 \Pr(V_d\le M)\le
  3C_{\rm pgf}\frac{M+1}{d+M+1}
  \le64e^{54}C_Z\frac{M+1}{d+1}.
\]

For M=0 the exact zero-path probability is Z_d and the same conclusion
holds. This proves (0.1)-(1.1).

For the physical application, the previously audited explicit profile
energy supplies C_Z=2e^(2^18). The physical query depth satisfies d<=r,
as required by that finite energy bound. Its finite q with denominator
a_s+a_(s+2)+1 is no larger than the present geometric q. Hence
Z_m<=exp(-Phi_m)<=e^(2^18)/m<=2e^(2^18)/(m+1) for m>=2;
the prefixes m=0,1 follow from Z_m<=1. One applies the same energy
bound at each prefix, whose profile still satisfies its hypotheses.

Thus admissible fully numerical choices are

\[
 C_{\rm pgf}=40e^{2^{18}+54},\qquad
 C_{\rm budget}=128e^{2^{18}+54}.                              \tag{6.1}
\]

This records an actual prefix-uniform input rather than inferring one
from a bound at the final depth alone.
