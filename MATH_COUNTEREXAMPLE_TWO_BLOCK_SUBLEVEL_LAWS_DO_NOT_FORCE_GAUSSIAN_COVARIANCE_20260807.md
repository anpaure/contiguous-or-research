# The two-block order and sublevel-sumset laws do not force Gaussian covariance

**Date:** 2026-08-07  
**Status:** unconditional pure mathematics.  This is an exact
counterexample to the abstract implication from the pointwise order and
the distributional two-block sumset inequality to the signed Gaussian
covariance.  It is not a counterexample to the stronger pointwise
half-line inverse laws, nor to the physical endpoint-critical theorem.

Put

\[
 a={\pi\over4},\qquad f(x)=e^{-ax^2},
\]

\[
 B(z)=f(1-z)+f(1+z),\qquad
 H_2(z)=\sum_{\ell\ge2}f(\ell+z).
\]

For a nonnegative function \(U_i\) on \((0,1)\), write

\[
 A_i(t)=\{z:U_i(z)\le t\},\qquad F_i(t)=|A_i(t)|.
\]

## Theorem

The conditions

\[
 0\le U_1\le U_0
\tag{1}
\]

and

\[
 F_0(s)+F_0(t)\le F_0(s+t)+F_1(s+t)
\tag{2}
\]

whenever both input sublevel sets have positive measure do not imply

\[
 \int_0^1\{U_0B'+U_1H_2'\}\,dz\ge0.
\tag{3}
\]

In fact, take

\[
 E=\left({19\over20},1\right),\qquad
 U_0=U_1={\bf1}_E.
\tag{4}
\]

Then (1)--(2) hold, while the integral in (3) is strictly negative.

### Proof

The order (1) is immediate.  The two sublevel distributions coincide
and equal

\[
 F_0(t)=F_1(t)=
 \begin{cases}
 0,&t<0,\\
 19/20,&0\le t<1,\\
 1,&t\ge1.
 \end{cases}
\tag{5}
\]

If both input sublevel sets have positive measure, then \(s,t\ge0\).
If \(s+t<1\), necessarily \(s,t<1\), and both sides of (2) equal
\(19/10\).  If \(s+t\ge1\), the right side equals \(2\), while the
left side is at most \(2\).  Hence (2) holds in every case.

It remains to sign the covariance.  Differentiation gives

\[
 B'(z)=2a\{(1-z)e^{-a(1-z)^2}-(1+z)e^{-a(1+z)^2}\},
\tag{6}
\]

and

\[
 H_2'(z)=-2a\sum_{\ell\ge2}(\ell+z)e^{-a(\ell+z)^2}<0.
\tag{7}
\]

The inequality \(B'(z)<0\) is equivalent to

\[
 h(z):=\log{1+z\over1-z}-\pi z>0.
\tag{8}
\]

At \(z=19/20\),

\[
 \log39>3>{19\pi\over20}.
\tag{9}
\]

Here \(e<3\) gives \(e^3<27<39\), while \(\pi<22/7\) gives
\(19\pi/20<209/70<3\).  Moreover

\[
 h'(z)={2\over1-z^2}-\pi
 \ge {800\over39}-\pi>0
\tag{10}
\]

on \([19/20,1)\).  Thus \(B'<0\) throughout \(E\), and (7) shows
\(B'+H_2'<0\) there.  Therefore

\[
 \int_0^1\{U_0B'+U_1H_2'\}\,dz
 =\int_{19/20}^1(B'+H_2')\,dz<0.
\]

This proves the theorem. \(\square\)

## Exact implication for the endpoint programme

The distributional inequality (2) forgets the locations of the
sublevel sets, whereas the Gaussian derivative changes sign.  It
therefore cannot by itself prove the two-block covariance target.

Any valid positive theorem must retain additional geometry, for example
the pointwise half-line laws

\[
 U_0(x+y)\le U_0(x)+U_0(y),\qquad
 U_1(x+y-1)\le U_0(x)+U_0(y),
\]

or the stronger fact that \(U_0,U_1\) are literal staircase inverse
profiles arising from one Bellman table.  The counterexample (4) fails
the first pointwise law when two points below \(19/20\) have sum above
\(19/20\), so it makes no claim against that stronger target.
