# Independent audit: inverse-circle closure of cyclic Apéry variance

**Date:** 2026-08-05  
**Audited source:** `MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`  
**Audited source SHA-256:** `31c6844cb1b630abdc6ebc859a9b963387b1442747a2c9527f51eee508b8dc62`  
**Method:** independent proof reconstruction from the definitions; no finite search or solver  
**Verdict:** **GO**.  The scale-sharp inequality

\[
 \operatorname{Var}(e)\le \frac{\mu(\mu+e(1))}{3}
\]

is correct.  The only changes I recommend are two local exposition
clarifications in the continuous-quantile proof; neither changes the
argument or statement.

## 1. Lift and generalized inverse

After scaling to \(e(1)=1\), repeated subadditivity gives
\(0\le e(r)\le r\) for \(0\le r<g\).  For

\[
 A(qg+r)=qg+r-e(r)
\]

one has

\[
 A(n+1)-A(n)=
 \begin{cases}
 1-e(r+1)+e(r),&r<g-1,\\
 1+e(g-1),&r=g-1,
 \end{cases}
\]

so \(A\) is nondecreasing.  For arbitrary positive or negative integers
\(m,n\), cyclic subadditivity gives

\[
 A(m+n)=m+n-e(\bar m+\bar n)
 \ge A(m)+A(n).
\]

Thus the use of negative lifts and period carries introduces no hidden
exception.  Also \(A(n)\le n\), \(A(n+g)=A(n)+g\), and \(A(n)-n\) is
bounded.

For

\[
 B(t)=\min\{n\in\mathbb Z:A(n)\ge t\},
\]

the minimum exists, and translating the defining set proves
\(B(t+g)=B(t)+g\).  Since

\[
 A(B(s)+B(t))\ge A(B(s))+A(B(t))\ge s+t,
\]

one gets \(B(s+t)\le B(s)+B(t)\).  Finally, \(A(n)\le n\) excludes every
\(n<t\) from the defining set, so \(B(t)\ge t\).  Therefore

\[
 u(t)=B(t)-t
\]

is a finite, nonnegative, measurable, \(g\)-periodic subadditive
function.  The passage to \(\mathbb R/g\mathbb Z\) is legitimate because
the inequality holds for all real lifts and \(u\) is periodic.

## 2. Exact phase law and moments

Put \(a_r=r-e(r)\), with \(a_g=g\).  Monotonicity of \(A\) gives

\[
 0=a_0\le a_1\le\cdots\le a_g=g.
\]

For \(a_r<t<a_{r+1}\), all earlier integer indices have \(A<t\), while
\(A(r+1)=a_{r+1}>t\), hence

\[
 B(t)=r+1,\qquad u(t)=r+1-t.
\]

Plateaux merely create empty intervals, and endpoints form a null set.
Direct integration gives

\[
 \frac1g\int_0^g u
 =\frac1{2g}\sum_r\big((1+e_r)^2-e_{r+1}^2\big)
 =\frac12+\mu,
\]

and

\[
 \frac1g\int_0^g u^2
 =\frac1{3g}\sum_r\big((1+e_r)^3-e_{r+1}^3\big)
 =\frac13+\mu+\mathbb E e^2.
\]

The cyclic power terms telescope exactly, so

\[
 \operatorname{Var}(u)=\frac1{12}+\operatorname{Var}(e).
\]

No distinct-phase assumption is being used.

## 3. Connected-circle quantile inequality

Let \(v\ge0\) be measurable and subadditive on a connected circle, and
write

\[
 C_z=\{x:v(x)\le z\},\qquad F(z)=m(C_z).
\]

Then \(C_s+C_t\subseteq C_{s+t}\).  The connected-circle sumset
inequality

\[
 m(E+F)\ge\min(1,m(E)+m(F))
\]

therefore yields

\[
 F(s+t)\ge\min(1,F(s)+F(t)).
\]

Using the increasing generalized quantile
\(q(x)=\inf\{z:F(z)\ge x\}\), and approaching the two quantile levels
from above if necessary, gives

\[
 q(x+y)\le q(x)+q(y),\qquad x,y\ge0,\quad x+y\le1.
\]

This checks the atom and endpoint conventions.  In particular, applying
the inequality to \((y,x-y)\) and integrating \(0\le y\le x\) gives

\[
 xq(x)\le 2\int_0^xq(t)\,dt.
\]

This is the intended reading of the source's phrase “integrate (5.4)
with \(y\) from \(0\) to \(x\).”  Writing \(S(x)=\int_0^xq\), it follows
that \(S(x)/x^2\) is nonincreasing.  Hence, if \(m=S(1)\),

\[
 S(x)\ge mx^2.
\]

There is no hidden endpoint regularity problem in the Stieltjes step.
Indeed the same quantile inequality with two probabilities just above
\(1/2\) shows that \(q(1)<\infty\); alternatively finite second moment
allows truncation and passage to the limit.  Thus \(q+2mx\) is a bounded
nondecreasing function.  With

\[
 H(x)=\int_0^x(q(t)-2mt)\,dt,
\]

one has \(H\ge0\), \(H(0)=H(1)=0\), and Stieltjes integration by parts
is valid:

\[
 \int_0^1(q^2-(2mx)^2)\,dx
 =-\int_{[0,1]}H\,d(q+2mx)\le0.
\]

Consequently

\[
 \mathbb E v^2\le\frac{4m^2}{3},\qquad
 \operatorname{Var}(v)\le\frac{m^2}{3}.
\]

For the inverse profile \(u\), all sublevel sets are finite unions of
intervals, so even the mild general measurable-sumset technicalities are
absent in the actual application.

## 4. Scale restoration

Applying the circle inequality to \(u\) gives

\[
 \frac1{12}+\operatorname{Var}(e)
 \le \frac{(\frac12+\mu)^2}{3}
 =\frac1{12}+\frac{\mu(\mu+1)}3
\]

under \(e(1)=1\).  For \(c=e(1)>0\), apply this to \(e/c\) and multiply
by \(c^2\):

\[
 \operatorname{Var}(e)\le\frac{\mu(\mu+c)}3.
\]

If \(c=0\), repeated subadditivity forces \(e(r)=0\) for every residue,
so the zero case is complete.  If the physical normalization gives
\(c\le1\), monotonicity in the second factor yields

\[
 \operatorname{Var}(e)\le\frac{\mu(\mu+1)}3.
\]

## 5. Downstream Rayleigh implication

The cited formal-phase theorem supplies

\[
 \Phi(U)>M\left(\frac12+\mu-
 \sqrt{\frac14+3\operatorname{Var}(e)}\right).
\]

The just-proved physical inequality implies

\[
 \frac14+3\operatorname{Var}(e)
 \le\left(\frac12+\mu\right)^2.
\]

Both sides inside the final comparison are nonnegative.  Therefore the
parenthesis is nonnegative, and the strict Fourier estimate makes
\(\Phi(U)>0\), including the equality case.  This conclusion has exactly
the scope stated in the source: the complete formal periodic phase.  It
does not settle the separate nonperiodic finite-availability shoulder.

## 6. Counterexample audit and final verdict

The potentially dangerous cases all survive the proof:

1. period seams and negative integer lifts are covered by cyclic
   subadditivity and the exact lift identity;
2. repeated phase points create only zero-length integration intervals;
3. composite periods create no loss after passage to the connected
   circle, because every proper closed subgroup has zero Haar measure;
4. atoms in the value distribution are handled by upper approximation
   in the quantile levels;
5. an unbounded-quantile endpoint cannot occur for a finite-valued
   measurable subadditive circle profile, and in any event the inverse
   profile is bounded and piecewise affine.

No counterexample or missing hypothesis remains.  Verdict: **GO**.
