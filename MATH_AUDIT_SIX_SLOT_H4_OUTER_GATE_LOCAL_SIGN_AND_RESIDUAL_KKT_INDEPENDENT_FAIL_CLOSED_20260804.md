# Independent fail-closed audit: six-slot h=4 outer gate

**Date:** 2026-08-04  
**Audited theorem:**  
MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md  
**Audited theorem SHA-256:**  
34057076744b82574ca5d93c87d29dea301c9b9a0edf9ee4232bc72e5b091315  
**Audited freeze manifest:**  
MATH_FREEZE_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.sha256  
**Manifest SHA-256:**  
c8b651c5a3d48382a9710273d38d6da6d99f419282e4c5d129486550b0638e71  

**Verdict:** **FAIL CLOSED PENDING TWO ENDPOINT-STRICTNESS
CORRECTIONS.**  The concavity chord, rational sign interval, far-end
Gaussian obstruction, continuity argument, residual identities, and full
KKT/subgradient list all pass.  However, two displayed strict inequalities
are false at equality endpoints.  Both have immediate weak-form repairs,
and no advertised gate conclusion depends on the false strictness.  This
audit is bound to the original bytes and therefore does not silently apply
those repairs.

## 1. Byte and manifest authentication

Rehashing the theorem gives exactly

\[
\texttt{34057076744b82574ca5d93c87d29dea301c9b9a0edf9ee4232bc72e5b091315}.
\]

Rehashing the manifest gives exactly

\[
\texttt{c8b651c5a3d48382a9710273d38d6da6d99f419282e4c5d129486550b0638e71}.
\]

The manifest's two entries both verify.  Thus this audit addresses the
requested frozen theorem and its frozen self-audit, not a later working
copy.

## 2. Exact corrections

### 2.1 Kernel derivative at zero

The frozen Lemma 1.1 states

\[
                         0<-K'(w)<{3\over10}
 \qquad(0\le w\le A/2).
\tag{2.1}
\]

At \(w=0\), direct differentiation gives

\[
 K'(0)
 =2A e^{-A^2}-2A e^{-A^2}=0.
\]

Equivalently, the theorem's own factorization contains

\[
                         \tanh(0)-0=0.
\]

Therefore the left strict inequality in (2.1) is false at the included
endpoint.

The exact repair is

\[
 \boxed{
 0\le-K'(w)<{3\over10}\quad(0\le w\le A/2),}
\tag{2.2}
\]

with strict positivity for \(0<w\le A/2\).

### 2.2 Diagonal displacement

The frozen equation (1.3) states, for \(0\le s\le t\le A/2\),

\[
 F(s)-F(t)
 <\min\left\{{3(t-s)\over10},{61\over1000}\right\}.
\tag{2.3}
\]

At \(s=t\), equation (2.3) reads \(0<0\), which is false.

The exact repair is

\[
\boxed{
 F(s)-F(t)\le {3(t-s)\over10},
 \qquad
 F(s)-F(t)<{61\over1000}.}
\tag{2.4}
\]

Equivalently, the displayed minimum bound may be written non-strictly;
it is strict whenever \(s<t\).

### 2.3 Downstream effect

No final sign claim needs either false endpoint strictness.

* In the active envelope, the reflection estimate is strict, so the
  envelope remains strictly above its stated minorant even when
  \(\delta=0\) makes the displacement loss zero.
* In the inactive envelope, the first cap loss is strictly below
  \(\eta\), while the moving loss is at most \(D\).  The preceding
  reflection inequality is strict, so the stated strict envelope bound
  survives a zero displacement.
* The singleton and half-period bounds also inherit strictness from
  reflection.
* At \(w=0\), the later residual assertion

  \[
  R_\tau(w)-T_\tau(w)>0
  \]

  remains strict because

  \[
  R_\tau(0)-T_\tau(0)
  =\sum_{q\ge2}(q-1)K'(q\tau)>0.
  \]

Thus a corrected successor theorem can retain every advertised gate
conclusion, but the frozen theorem itself requires correction.

## 3. Concavity chord and local sign interval

The authenticated endpoints are

\[
 C(A)>C_0={5503\over125000},
 \qquad
 C(6A/5)>{63\over1000}.
\]

Their certified difference is

\[
 {63\over1000}-{5503\over125000}
 ={2372\over125000}>0.
\]

For \(0\le\delta\le A/5\), concavity with
\(t=5\delta/A\) gives

\[
 C(A+\delta)>
 C_0+{5\delta\over A}{2372\over125000}.
\]

Since \(A<8/9\),

\[
 {5\over A}{2372\over125000}
 >{45\over8}{2372\over125000}
 ={5337\over50000}.
\]

The chord coefficient in the frozen theorem is exact.

The switching point also checks:

\[
 {3\delta_0\over10}
 ={3\over10}{1061\over18750}
 ={2122\over125000}
 =\eta.
\]

Before the switch, the repaired common minorant is

\[
 {9897\over1000000}
 -{2163\over50000}\delta.
\]

Using \(\delta_0<3/50\) gives

\[
 {9897\over1000000}
 -{2163\over50000}{3\over50}
 ={36507\over5000000}>0.
\]

After the switch, the minorant is

\[
 {43849\over1000000}
 -{32163\over50000}\delta,
\]

whose exact zero is

\[
 {43849/1000000\over32163/50000}
 ={43849\over643260}=\delta_*.
\]

Direct cross multiplication verifies

\[
 0<\delta_0<{3\over50}<\delta_*<{7\over100}<{A\over5},
\]

and \(7/100<61/300\), so neither the displacement cap nor the chord range
is crossed.  The independent strict reflection and ceiling inequalities
make both gates strictly positive at \(\delta_*\), even though the final
linear minorant vanishes there.

**Concavity/sign-interval verdict:** **PASS after the endpoint weak-form
repairs in Section 2.**

## 4. Far-end exponential audit

At \(\delta=A/2\), one has \(\tau=3A/2\) and \(B_\delta=0\).
The test choices in the frozen proof give

\[
\begin{aligned}
 \mathfrak G_{XY}(A/2)
 \le{}&C(\tau)+2F_\tau(A/2)+F_\tau(A)\\
 &+F_\tau(2A/3)+F_\tau(3A/4),
\end{aligned}
\tag{4.1}
\]

and

\[
 \mathfrak G_Z(A/2)
 \le C(3A/4)+2F_\tau(2A/3)+2F_\tau(A/2).
\tag{4.2}
\]

### 4.1 Constant and exponent ledger for XY

The five surviving compact constants in (4.1) are correct.  The retained
negative Gaussians are exactly

\[
\begin{gathered}
 2e^{-\pi/4},\quad
 2e^{-\pi/16},\quad
 2e^{-9\pi/16},\quad
 e^{-\pi},\\
 e^{-\pi/36},\quad
 e^{-25\pi/36},\quad
 e^{-\pi/64},\quad
 e^{-49\pi/64}.
\end{gathered}
\]

Using the theorem's lower bounds, their numerator ledger over denominator
\(10000\) is

\[
 9118+16432+3412+432+9163+1127+9520+901
 =50105.
\]

Therefore

\[
                         \mathfrak G_{XY}(A/2)
 <5-{50105\over10000}
 =-{21\over2000}.
\]

### 4.2 Constant and exponent ledger for Z

The train \(C(3A/4)\) has two compact constants.  Its first genuinely
tail-only term is

\[
                         -e^{-25\pi/16},
\]

which the theorem correctly retains.  Together with the other two trains,
the negative ledger is exactly

\[
\begin{gathered}
 2e^{-\pi/4},\quad e^{-\pi/64},\quad e^{-49\pi/64},
 \quad e^{-25\pi/16},\\
 2e^{-\pi/16},\quad2e^{-9\pi/16},
 \quad2e^{-\pi/36},\quad2e^{-25\pi/36}.
\end{gathered}
\]

The rational numerator sum is

\[
 9118+9520+901+73+16432+3412+18326+2254
 =60036.
\]

Hence

\[
                         \mathfrak G_Z(A/2)
 <6-{60036\over10000}
 =-{9\over2500}.
\]

### 4.3 Rational exponential certificates

For the seven new Gaussian rows, \(\pi<22/7\) gives the exact rational
exponent majorants

\[
 {11\over224},\ {539\over224},\
 {11\over56},\ {99\over56},\
 {11\over126},\ {275\over126},\
 {275\over56}.
\]

Every value is positive and smaller than \(26\).  Therefore

\[
 U_{24}(x)=\sum_{n=0}^{24}{x^n\over n!}
 +{x^{25}\over25!}{1\over1-x/26}
\]

is a valid rational upper bound for \(e^x\).  Clearing its positive
denominator verifies respectively

\[
\begin{aligned}
U_{24}(11/224)&<{125\over119},&
U_{24}(539/224)&<{10000\over901},\\
U_{24}(11/56)&<{1250\over1027},&
U_{24}(99/56)&<{5000\over853},\\
U_{24}(11/126)&<{10000\over9163},&
U_{24}(275/126)&<{10000\over1127},\\
U_{24}(275/56)&<{10000\over73}.
\end{aligned}
\]

These are exactly the reciprocals needed for the lower Gaussian bounds.
The previously authenticated \(e^{-\pi/4}\) and \(e^{-\pi}\) rows have
the correct directions as well.

**Far-end obstruction verdict:** **PASS.**

## 5. Continuity audit

The inactive envelope already has a fixed compact domain.  Writing

\[
 b=tB_\delta,\qquad w=t\tau/2,\qquad0\le t\le1,
\]

puts the active and singleton envelopes on fixed compact unit intervals.
Their objectives are jointly continuous through \(\delta=A/2\).
The minimum of a continuous function over a fixed compact set is
continuous.  Thus both gates are continuous.

Strict positivity at \(\delta_*\) and strict negativity at \(A/2\)
therefore force a zero in \((\delta_*,A/2)\) and a negative one-sided
neighborhood of the far endpoint.  This is a statement about the relaxed
gates only.

**Continuity verdict:** **PASS.**

## 6. Residual identities and complete inner KKT list

The termwise identities are

\[
 T_\tau(w)=K'(w)+\sum_{q\ge1}K'(q\tau+w),
\qquad
 R_\tau(w)=\sum_{q\ge1}qK'(q\tau+w),
\]

and hence

\[
 R_\tau(w)-T_\tau(w)
 =-K'(w)+\sum_{q\ge1}(q-1)K'(q\tau+w).
\]

Every term of \(R_\tau\) is positive.  Thus
\(T_\tau(w)=0\Rightarrow R_\tau(w)>0\).  On the half band the corrected
kernel sign, together with the strictly positive \(q\ge2\) sum, gives
\(R_\tau-T_\tau>0\), including at \(w=0\).

For a complementary pair with
\(T_\tau(r)=T_\tau(s)=t\),

\[
\begin{aligned}
 &[R_\tau(r)-T_\tau(r)]
 +[R_\tau(s)-T_\tau(s)]+3t\\
 &\qquad=R_\tau(r)+R_\tau(s)+t
 =R_\tau(r)+R_\tau(s)+T_\tau(r).
\end{aligned}
\]

The subtraction ledger is exact, and the theorem correctly refrains from
assigning a sign when a paired shift lies above \(A/2\).

The exhaustive inner candidate types are:

* \(\mathcal H\): \(b=0\), \(b=B_\delta\), or
  \(T_\tau(b+\delta)=T_\tau(A-b)\);
* \(\mathcal I\): \(b=0\), \(b=A/3\), the clip switch
  \(b+\delta=A/2\), the cap switch
  \(F_\tau(m_\delta(b))=C(\tau)\), the constant-low equation
  \(T_\tau(A-b)=0\), or the moving equation
  \(T_\tau(b+\delta)=T_\tau(A-b)\);
* \(\mathcal S\): \(w=0\), \(w=\tau/2\), or
  \(T_\tau(w)=0\) with \(A/2\le w\le\tau/2\).

There is no omitted smooth branch or inner kink.

## 7. Outer derivatives and nonsmooth conditions

Replaying the envelope theorem gives exactly:

\[
\mathcal H'
=R_\tau(0)+R_\tau(b+\delta)+T_\tau(b+\delta)
 +R_\tau(A-b)
\]

for an interior or fixed-zero active minimizer, and

\[
\begin{aligned}
\mathcal H'
={}&R_\tau(0)
+R_\tau(\tau/3)+{1\over3}T_\tau(\tau/3)\\
&+R_\tau(2\tau/3)+{2\over3}T_\tau(2\tau/3)
\end{aligned}
\]

at \(b=B_\delta\).

The three smooth inactive branches have derivatives

\[
\begin{array}{c|c}
0&R_\tau(A-b)+R_\tau(0)\\
A/2&R_\tau(A-b)+R_\tau(A/2)\\
b+\delta&R_\tau(A-b)+R_\tau(b+\delta)+T_\tau(b+\delta).
\end{array}
\]

The singleton derivatives are \(R_\tau(w)\) at an interior critical
minimizer, \(R_\tau(0)\) at zero, and

\[
R_\tau(\tau/2)+{1\over2}T_\tau(\tau/2)
\]

at the moving endpoint.  Finally,

\[
 {d\over d\delta}C(\tau/2)
 ={1\over2}\sum_{q\ge1}qK'(q\tau/2).
\]

Thus the two smooth outer equations in the theorem are exact.

At a branch tie, clip, cap switch, or changing active minimizer, a
one-dimensional local minimum must satisfy

\[
                         \partial_-\mathfrak G\le0
                         \le\partial_+\mathfrak G.
\]

The orientation is correct.  This actual one-sided condition is stronger
than merely placing zero in the convex hull of active branch derivatives.
The outer endpoints, inner-domain endpoints, and gate-zero equation are
separately listed.  A gate zero is correctly not required to be
outer-stationary.

**KKT/subgradient verdict:** **PASS and exhaustive.**

## 8. Final scope verdict

The frozen theorem's substantive conclusions are repairable without
changing their constants:

1. both relaxed gates are positive through \(\delta_*\);
2. both relaxed gates are negative at the formal far endpoint;
3. every residual smooth or nonsmooth candidate lies in the stated KKT
   locus;
4. this does not prove positivity or negativity of a physical table.

Nevertheless, the requested policy is fail-closed on any correction.
Equations (1.2) and (1.3) of the frozen theorem contain false strict
endpoint statements.  Therefore the byte-bound verdict is:

\[
\boxed{\textbf{FAIL CLOSED PENDING THE TWO WEAK-ENDPOINT CORRECTIONS}.}
\]
