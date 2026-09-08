# An exact endpoint-critical Bellman table with negative total shoulder

**Date:** 2026-08-07  
**Method:** pure mathematics; two-generator min-plus arithmetic and rational
Gaussian derivative bounds  
**Status:** unconditional counterexample.  Even when the endpoint is the
unique critical denomination, the **total** finite Apéry availability
shoulder need not be nonnegative.  The complete physical Rayleigh
functional in this example remains positive.

## 1. The table

Put \(n=30\), and define

\[
 v_j={4j\over125}\quad(0\le j\le28),
 \qquad
 v_{29}={957\over1000},
 \qquad
 v_{30}=1.
\tag{1.1}
\]

### Lemma 1.1

The table is nonnegative, nondecreasing and internally superadditive.
The endpoint \(30\) is its unique maximum-density denomination.

#### Proof

For sums at most \(28\), superadditivity is equality.  At total \(29\),

\[
 {957\over1000}>{4\cdot29\over125}.
\tag{1.2}
\]

At total \(30\), a split not using \(29\) has value \(120/125<1\),
while the split \(29+1\) has value

\[
 {957\over1000}+{4\over125}={989\over1000}<1.
\tag{1.3}
\]

These are every possible internal inequality.  The densities are

\[
 {v_j\over j}={4\over125}<{1\over30}\quad(j\le28),
 \qquad
 {v_{29}\over29}={33\over1000}<{1\over30}.
\tag{1.4}
\]

Thus only the endpoint has density \(1/30\). \(\square\)

## 2. Exact stable residue costs

Subtract the endpoint density.  The proper reduced costs are

\[
 e_j={j\over30}-v_j=
 \begin{cases}
  j/750=4j/3000,&1\le j\le28,\\
  29/3000,&j=29.
 \end{cases}
\tag{2.1}
\]

All steps of size at most \(28\) may be replaced, at the same total
cost, by unit steps.  If a residue walk uses \(k\) steps of size \(29\)
and unit length \(l\), its residue and cost are

\[
 l-k\pmod {30},
 \qquad
 {29k+4l\over3000}.
\tag{2.2}
\]

For a fixed residue \(r\), minimize first over \(l\equiv r+k\pmod{30}\)
and then over \(k\).  Before the first wrap the numerator is
\(4r+33k\), and after it the first possible value occurs at
\(k=30-r\).  Therefore

\[
 \boxed{
 d_r={1\over3000}\min\{4r,29(30-r)\}.}
\tag{2.3}
\]

The two expressions cross between \(r=26\) and \(r=27\).  Hence the
stable shifts \(s_r=r/30-d_r\) agree with the displayed values except at

\[
 \boxed{
 s_{27}={871\over1000},
 \qquad
 s_{28}={457\over500}.}
\tag{2.4}

At residue \(29\), both descriptions give \(s_{29}=957/1000\).

The stable walk to residue \(28\) is \(29+29=30+28\).  Thus it first
becomes available in block one.  The stable walk to residue \(27\) is
\(29+29+29=2\cdot30+27\), and it first becomes available in block two.
No cheaper exact fill exists one block earlier by (2.2).  Consequently
the only nonzero normalized availability chains are

\[
 \boxed{
 \eta_{27,0}=\eta_{27,1}={7\over1000},
 \qquad
 \eta_{28,0}={18\over1000}.}
\tag{2.5}

All later entries, and all other residue chains, have zero deficit.

## 3. Exact shoulder

Let

\[
 A={\sqrt\pi\over2},qquad
 \kappa(y)=K(Ay).
\tag{3.1}
\]

Equations (2.4)--(2.5) give the entire finite shoulder:

\[
\boxed{
\begin{aligned}
 \mathcal H={}&
 \kappa(108/125)-\kappa(871/1000)\\
 &+\kappa(233/125)-\kappa(1871/1000)\\
 &+\kappa(112/125)-\kappa(457/500).
\end{aligned}}
\tag{3.2}
\]

The middle line is strictly negative because \(\kappa\) is strictly
increasing on \([1,\infty)\).  It remains to compare the two compact
lines.

For \(0\le y\le1\), with \(a=\pi/4\),

\[
 \kappa'(y)=2a\left(
 (1+y)e^{-a(1+y)^2}-(1-y)e^{-a(1-y)^2}
 \right).
\tag{3.3}
\]

### Lemma 3.1 (rational derivative bounds)

On the interval \([108/125,457/500]\), the derivative \(\kappa'\) is
strictly increasing.  Moreover

\[
 \boxed{
 \kappa'(108/125)>-{21\over1000},
 \qquad
 \kappa'(112/125)>{1\over100}.}
\tag{3.4}
\]

#### Proof

Differentiating (3.3),

\[
 {\kappa''(y)\over2a}
 =\bigl(1-2a(1+y)^2\bigr)e^{-a(1+y)^2}
  +\bigl(1-2a(1-y)^2\bigr)e^{-a(1-y)^2}.
\tag{3.5}
\]

Throughout the displayed interval, the second summand is greater than
\(9/10\).  Writing \(t=a(1+y)^2>27/10\), the absolute value of the
negative first summand is
\((2t-1)e^{-t}<1/3\); the latter function is decreasing for
\(t>3/2\).  Hence \(\kappa''>0\).

For the first endpoint, elementary Taylor bounds give

\[
 {17\over125}e^{-a(17/125)^2}<{1341\over10000},
 \qquad
 {233\over125}e^{-a(233/125)^2}>{121\over1000}.
\tag{3.6}
\]

Using \(2a=\pi/2<11/7\), (3.3) is therefore greater than

\[
 -{11\over7}{131\over10000}>-{21\over1000}.
\tag{3.7}
\]

At the second endpoint, the corresponding bounds are

\[
 {237\over125}e^{-a(237/125)^2}>{9\over80},
 \qquad
 {13\over125}e^{-a(13/125)^2}<{129\over1250}.
\tag{3.8}
\]

Their difference exceeds \(93/10000\).  Since \(2a=\pi/2>3/2\),

\[
 \kappa'(112/125)>{279\over20000}>{1\over100}.
\tag{3.9}
\]

All exponential comparisons in (3.6) and (3.8) follow from the
alternating Taylor bounds for (e^{-x}), using
(31415/10000<\pi<355/113). \(\square\)

### Theorem 3.2 (negative total shoulder)

For the table (1.1),

\[
 \boxed{\mathcal H<-{33\over10^6}<0.}
\tag{3.10}
\]

#### Proof

By monotonicity of \(\kappa'\) and (3.4),

\[
 \kappa(108/125)-\kappa(871/1000)
 <{7\over1000}{21\over1000}
 ={147\over10^6},
\tag{3.11}
\]

while

\[
 \kappa(112/125)-\kappa(457/500)
 <-{18\over1000}{1\over100}
 =-{180\over10^6}.
\tag{3.12}
\]

The middle line of (3.2) is negative, so (3.10) follows. \(\square\)

## 4. Consequence

The conjectural shortcut

\[
 \text{endpoint uniquely critical}
 \quad\Longrightarrow\quad
 \mathcal H\ge0
\tag{4.1}
\]

is false.  Any endpoint-critical proof must combine the signed shoulder
with the positive formal reserve, or use the exact direct-theta plus
missing-tail identity.  Residuewise shoulder signs are not the only
problem: their **total** can be negative.

This example is not a counterexample to the physical Rayleigh/Bellman
inequality.  Its formal reserve is much larger than the shoulder debt.
No nonpositive complete clock is claimed.

## 5. Dependencies

1. the exact max-plus/min-plus endpoint reduction;
2. the elementary Rayleigh kernel formula;
3. no enumeration, solver, or numerical sign check.
