# Independent audit: five-slot three-efficient threshold endpoint and delayed crossing

**Date:** 2026-08-04  
**Method:** independent symbolic rederivation and rational-inequality audit;
no finite search or numerical optimization.  
**Verdict:** **PASS after one strict-boundary scope repair.**

## 0. Frozen payload and dependencies

The audited theorem is

MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md

with post-repair SHA256

\[
\boxed{\texttt{1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6}}.
\]

The repair separates the exact inert conditions

\[
 y\ge2a,\qquad y>A-p
\]

from the relative interior \(y>\max\{2a,A-p\}\), and records that the
right inequality in the genuinely inert repeated-gap domain is strict.
The equality boundaries were already assigned to the threshold and overlap
faces, so no mathematical gate changed.

The exact five-pulse input and its prior independent audit have hashes

\[
\begin{array}{c|c}
\text{five-slot maximum-efficiency normal forms}
&\texttt{2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e}\\
\text{independent normal-form audit}
&\texttt{e22399cc4f64c0a338059b2ee7806d0c45c7d9b881a6f5d8f28e8a13457d33d2}.
\end{array}
\]

The endpoint-saturation theorem has SHA

\[
\texttt{7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f}.
\]

## 1. Reconstructing the five-pulse branch

Write

\[
 (c_0,\ldots,c_5)=(0,x,y,p,p+a,p+b).
\]

Internal superadditivity gives

\[
\begin{gathered}
y\ge2x,\qquad p\ge x+y,\qquad a\ge x,\\
b\ge y,\qquad b\ge a+x,\qquad p+a\ge2y.
\end{gathered}                                             \tag{1.1}
\]

Maximal efficiency of size three gives

\[
                         a\le p/3,\qquad b\le2p/3.          \tag{1.2}
\]

The residue-one simple paths modulo three are one size-four step or two
size-five steps; the residue-two paths are one size-five step or two
size-four steps.  Hence

\[
 s_1=\max\{a,2b-p\},\qquad s_2=\max\{b,2a\}.              \tag{1.3}
\]

Availability occurs late only for the two double-step witnesses.  The
exceptional capacities are \(1,2,4,5,7\), with

\[
 V_7=\max\{2p+a,p+b+y\}.                                  \tag{1.4}
\]

Comparing those five entries with the formal period-three lattice gives
exactly

\[
\begin{aligned}
 \Phi={}&\mathcal L_3(p;s_1,s_2)\\
 &+K(x)-K(s_1)
  +K(p+a)-K(p+s_1)
  +K(V_7)-K(2p+s_1)\\
 &+K(y)-K(s_2)
  +K(p+b)-K(p+s_2).
\end{aligned}                                             \tag{1.5}
\]

Thus the theorem starts from the authenticated five-pulse identity and not
from an eventual-period approximation.

## 2. Independent check of the one-period train bounds

Put \(A^2=\alpha=\pi/4\), \(v=At\), and

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-\alpha(t-j)^2}.
\]

Poisson summation gives

\[
 \Theta(t)=2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt),
\qquad
\epsilon:=4\sum_{m\ge1}e^{-4\pi m^2}<1/20000.             \tag{2.1}
\]

Directly completing the half train gives

\[
 F_A(At)=1-\Theta(t)+e^{-\alpha t^2}
              +\sum_{j\ge2}e^{-\alpha(j-t)^2}.             \tag{2.2}
\]

At \(t=0\), retain the \(j=2\) term:

\[
 C(A)>e^{-\pi}-1/20000.
\]

The theorem's rational exponential estimate gives
\(e^\pi<20000/861\), so

\[
                         C(A)>43/1000.                     \tag{2.3}
\]

For \(0\le t\le2/5\), set

\[
 H(t)=e^{-\alpha t^2}+e^{-\alpha(2-t)^2}.
\]

The derivative has the sign of

\[
 g(t)=\log\frac{2-t}{t}-\pi(1-t).
\]

Here \(g'\) is strictly increasing on \((0,1)\);
\(g(1/10)>0\) and \(g(3/25)<0\).  Therefore the unique maximum of
\(H\) on the audited interval lies between those two points, and

\[
 H(t)
 <e^{-\pi/400}+e^{-2209\pi/2500}
 <397/400+1/16=211/200.                                  \tag{2.4}
\]

For the tail beginning at \(j=3\), the first term is below \(1/190\)
and every successive ratio is below \(1/100\).  Thus

\[
 \sum_{j\ge3}e^{-\alpha(j-t)^2}<1/180.                    \tag{2.5}
\]

Substitution in (2.2) yields

\[
 F_A(At)<11/200+1/180+1/20000<61/1000.                   \tag{2.6}
\]

Finally, (2.3)'s stronger precursor
\(e^\pi<20000/861<(11/5)^4\) gives
\(e^{-\pi/4}>5/11\), while \(e^{-\pi}>1/25\).  Hence

\[
 C(A)<1-2e^{-\pi/4}-e^{-\pi}
 <14/275<61/1000.                                        \tag{2.7}
\]

All constants used at the endpoint are therefore strict and uniform on
the claimed range.

## 3. Threshold endpoint \(p+b=A\)

From \(b\le2p/3\) and \(b=A-p\),

\[
 3A/5\le p<A,\qquad0<b\le2A/5.                            \tag{3.1}
\]

The first-crossing condition \(p+a<A\) gives \(a<b\), and (1.1) gives

\[
                         x\le b-a,\qquad y\le b.           \tag{3.2}
\]

For a table whose endpoint is exactly \(A\), the literal configuration
with \(q\) endpoint generators and one size-\(r\) generator gives the
termwise Bellman lower bound

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(p)+F_A(p+a).              \tag{3.3}
\]

At \(q=0\) this is equality by prefix superadditivity.  At \(q\ge1\),
both Bellman arguments lie in \([A,\infty)\), where \(K\) is increasing.
Thus (3.3) prices the actual clock and loses none of the five finite
pulses.

Reflection gives

\[
 F_A(A-v)>-F_A(v)-\epsilon.                               \tag{3.4}
\]

Every interior critical point of \(F_A\) on \([0,A/2]\) is a strict
maximum, so (3.2) gives

\[
\begin{aligned}
F_A(x)&\ge\min\{C(A),F_A(b-a)\},\\
F_A(y)&\ge\min\{C(A),F_A(b)\}.
\end{aligned}                                             \tag{3.5}
\]

Apply (3.4) to \(p=A-b\) and
\(p+a=A-(b-a)\).  With \(U=61/1000\), equations
(2.3), (2.6), and (2.7) give

\[
\begin{aligned}
\Phi
&>C(A)+2(C(A)-U)-2\epsilon\\
&>3(43/1000)-2(61/1000)-2/20000\\
&=69/10000>0.                                             \tag{3.6}
\end{aligned}
\]

The claimed threshold-endpoint margin is correct.

## 4. Endpoint saturation and the inert identities

The lower-denomination partitions of capacity five are dominated by the
two maximal two-part partitions

\[
                         3+2,\qquad4+1.
\]

Indeed,

\[
\begin{aligned}
p+2x&\le p+y,\\
2y+x&\le p+y,\\
y+3x&\le p+y,\\
5x&\le p+y,
\end{aligned}
\]

using \(y\ge2x\) and \(p\ge x+y\).  Therefore

\[
 P_5=p+\max\{y,a+x\}=p+v.                                \tag{4.1}
\]

Endpoint saturation is exactly

\[
                         b=\max\{A-p,v\}.                  \tag{4.2}
\]

Equality \(v=A-p\) belongs to the already closed threshold face.  On the
strict inert face,

\[
                         b=v>A-p.                          \tag{4.3}
\]

If \(b=y\), then \(2b-p\le a\) is \(2y\le p+a\).  If
\(b=a+x\), then

\[
 a+2x\le p
\]

follows from \(a\le p/3\) and \(x\le p/3\).  Thus

\[
                         s_1=a.                            \tag{4.4}
\]

Since \(x\le a\),

\[
 s_2=\max\{b,2a\}=\max\{y,2a\}=:w.                       \tag{4.5}
\]

Finally,

\[
 b+y\le p+a:
\]

for \(b=y\) this is \(2y\le p+a\), while for \(b=a+x\)
it is \(x+y\le p\).  Hence

\[
                         V_7=2p+a.                         \tag{4.6}
\]

Substitution in (1.5) cancels exactly the capacity-four and capacity-seven
pulses and no others:

\[
\begin{aligned}
\Phi={}&\mathcal L_3(p;a,w)
+K(x)-K(a)+K(y)-K(w)\\
&+K(p+b)-K(p+w).                                         \tag{4.7}
\end{aligned}
\]

This confirms the five-to-three pulse collapse.

## 5. The \(w=y\) delayed face

Here \(y\ge2a\), and \(a+x\le2a\), so

\[
                         b=y=w.
\]

The last two pulses in (4.7) vanish and

\[
 \Phi=\mathcal L_3(p;a,y)+K(x)-K(a)
\ge\mathcal L_3(p;a,y),                                  \tag{5.1}
\]

because \(x\le a<A/3\) and \(K\) decreases on this interval.

The exact inert conditions are

\[
 y\ge2a,\qquad y>A-p,\qquad y\le(p+a)/2<A/2.              \tag{5.2}
\]

The equality \(y=2a\) is the overlap with \(w=2a\); equality
\(y=A-p\) is the threshold face.

On the strict interval \(y>A-p\),

\[
 G_p(y)=1-e^{-(A-y)^2}
        -\sum_{q\ge0}e^{-(A+y+qp)^2}.                     \tag{5.3}
\]

At an interior critical point, with
\(\varphi(t)=te^{-t^2}\),

\[
 \sum_{q\ge0}\varphi(A+y+qp)=\varphi(A-y).                \tag{5.4}
\]

The logarithmic derivative

\[
 \lambda(t)=1/t-2t
\]

is strictly decreasing.  Therefore

\[
 \frac12G_p''(y)
\le
 2A\left(\frac1{A^2-y^2}-2\right)\varphi(A-y)<0,           \tag{5.5}
\]

because \(y<A/2\) and
\(A^2-y^2>3\pi/16>1/2\).  Every interior critical point is
a strict maximum, so the minimum on the closure is at one of

\[
 y=A-p,\qquad y=2a,\qquad2y=p+a.                          \tag{5.6}
\]

The first is the positive threshold face and the second is the overlap
face.  On the new upper boundary put

\[
 \beta=(p-a)/2.
\]

Then

\[
 p=a+2\beta,\qquad y=a+\beta,
\]

and the gaps are \((a,\beta,\beta)\).  The projected domain is

\[
 0\le a\le\beta,\qquad
 2a+2\beta<A<2a+3\beta                                   \tag{5.7}
\]

on the genuinely inert face.  Adding the already positive endpoint
equality gives the closed gate

\[
 0\le a\le\beta,\qquad
 2a+2\beta<A\le2a+3\beta.                                \tag{5.8}
\]

Thus the only new \(w=y\) object is exactly

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta).                       \tag{5.9}
\]

## 6. The \(w=2a\) delayed face

Here \(y\le2a\), and

\[
 a\le b=\max\{y,a+x\}\le2a.                              \tag{6.1}
\]

First crossing and strict inertness give

\[
 a<A-p<b.                                                \tag{6.2}
\]

Also \(p\ge3a\).  Conversely, every point in

\[
 p<A,\qquad p\ge3a,\qquad a<A-p<b\le2a                  \tag{6.3}
\]

is realized in the projected \((p,a,b)\)-domain by taking
\(x=0,y=b\).  Thus (6.3) is exact, not merely a relaxation.

For completeness, \(K\) is decreasing on \([0,2A/3]\).  Put
\(z=t/A\).  The sign assertion is equivalent to

\[
 \log\frac{1+z}{1-z}<\pi z\qquad(0<z\le2/3).
\]

The difference is concave, vanishes at zero, and is positive at \(2/3\)
because \(2\pi/3>\log5\).  Hence the inequality holds throughout.

Now

\[
 x\le b-a\le a,\qquad y\le b\le2a<2A/3.
\]

Applying monotonicity only to those two finite pulses in (4.7) gives

\[
\begin{aligned}
\Phi\ge\mathcal H(p,a,b)
:={}&\mathcal L_3(p;a,2a)\\
&+K(b-a)-K(a)+K(b)-K(2a)\\
&+K(p+b)-K(p+2a).                                       \tag{6.4}
\end{aligned}
\]

The final tail difference is untouched; it is generally negative.

At \(p=3a\), the allowable new range is \(A/5<a<A/4\).
At \(b=2a\), all three pulse differences vanish and
\(\mathcal H=C(a)>0\).  At \(b=A-3a\), the endpoint is \(A\)
and Section 3 applies.

## 7. Scope verdict

The theorem correctly proves:

1. strict positivity, with margin \(69/10000\), of the saturated
   \(c_5=A\) face in the five-slot size-three-efficient branch;
2. exact collapse of the inert five-pulse clock to (4.7);
3. reduction of the \(w=y\) face to the repeated-gap scalar
   \(\mathcal R\); and
4. reduction of the \(w=2a\) face to \(\mathcal H\), with the adverse
   tail retained.

It does not sign \(\mathcal R\) or \(\mathcal H\), and therefore does not
prove complete five-slot positivity.  No pulse, overlap boundary, or
strict inert chamber remains unaccounted for.

