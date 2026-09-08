# Theorem: positivity on the three-slot regime-II triangle

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem, independently audited.
It proves the remaining fixed-period triangle by an endpoint reduction,
Poisson summation, and rational Gaussian bounds.

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\]

and let `K` be the kernel

\[
 K(u)=
 \begin{cases}
 1-e^{-(A-u)^2}-e^{-(A+u)^2},&0\le u\le A,\\
 -e^{-(A+u)^2},&u>A.
 \end{cases}
\]

Define

\[
 C(A)=\sum_{q\ge0}K(qA),\qquad
 F_A(u)=\sum_{q\ge0}K(qA+u).
\]

Then

\[
 \mathcal L_3(A;z,y)=C(A)+F_A(z)+F_A(y).             \tag{0.1}
\]

The goal is to prove

\[
 \boxed{\mathcal L_3(A;z,y)>0}
 \qquad
 \left(0\le z\le {y\over2},\quad0\le y\le{2A\over3}\right).
                                                               \tag{0.2}
\]

## 1. Reduction of the `z`-variable to its endpoints

For `0<=u<=A/3`, the tail formula gives

\[
 F_A(u)=1-e^{-(A-u)^2}
        -\sum_{q\ge0}e^{-(A+u+qA)^2}.                \tag{1.1}
\]

Let

\[
 \phi(v)=ve^{-v^2},\qquad
 \lambda(v)={\phi'(v)\over\phi(v)}={1\over v}-2v.
\]

The function `lambda` is strictly decreasing.  At an interior critical
point of `F_A`, put

\[
 w=A-u,qquad v_q=A+u+qA.
\]

Termwise differentiation of the Gaussian series gives

\[
 \sum_{q\ge0}\phi(v_q)=\phi(w),                     \tag{1.2}
\]

and hence

\[
\begin{aligned}
 {1\over2}F_A''(u)
 &=\sum_{q\ge0}\phi'(v_q)+\phi'(w)\\
 &\le\bigl(\lambda(A+u)+\lambda(A-u)\bigr)\phi(w)\\
 &=2A\left({1\over A^2-u^2}-2\right)\phi(w)<0.     \tag{1.3}
\end{aligned}
\]

Indeed,

\[
 A^2-u^2\ge {8A^2\over9}={2\pi\over9}>{1\over2}.
\]

Thus every interior critical point on `[0,A/3]` is a strict maximum, so
the minimum on any subinterval is attained at an endpoint.  Since
`y/2<=A/3`, (0.1) implies

\[
 \mathcal L_3(A;z,y)
 \ge \min\{J_1(y),J_2(y)\},                          \tag{1.4}
\]

where

\[
 J_1(y)=2C(A)+F_A(y),
 \qquad
 J_2(y)=C(A)+F_A(y/2)+F_A(y).                       \tag{1.5}
\]

It remains to sign these two scalar functions.

## 2. A theta lower envelope

Normalize `y=At` and write

\[
 f(t)=F_A(At),\qquad0\le t\le{2\over3}.
\]

Directly from the two branches of `K`,

\[
 f(t)=1-e^{-a(1-t)^2}-\sum_{n\ge1}e^{-a(n+t)^2}.    \tag{2.1}
\]

Introduce the full shifted Gaussian lattice

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-a(t-j)^2}.
\]

Poisson summation at `a=pi/4` gives

\[
 \Theta(t)=2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt).
                                                               \tag{2.2}
\]

Set

\[
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}.
\]

Completing (2.1) to the lattice (2.2) yields the exact identity

\[
 f(t)=1-\Theta(t)+e^{-at^2}
      +\sum_{j\ge2}e^{-a(j-t)^2}.                   \tag{2.3}
\]

Consequently, with

\[
 H(t)=e^{-at^2}+e^{-a(2-t)^2},                      \tag{2.4}
\]

one has

\[
 \boxed{f(t)\ge-1+H(t)-\varepsilon}.               \tag{2.5}
\]

At `t=0`, `f(0)=C(A)`, so (2.5) also gives

\[
 C(A)\ge e^{-\pi}-\varepsilon.                     \tag{2.6}
\]

The theta error is tiny by a purely rational estimate.  Since `pi>3`,
successive summands after the first have ratio at most `e^{-36}`.  Also
the positive Taylor series through degree eight gives

\[
 e^3>\sum_{k=0}^8{3^k\over k!}
     =20+{41\over4480}>20.
\]

Therefore

\[
 \varepsilon
 <{4e^{-12}\over1-e^{-36}}
 <{1\over20000}.                                    \tag{2.7}
\]

## 3. The two-Gaussian envelope has no interior minimum

For `0<t<=2/3`, the sign of `H'(t)` is the sign of

\[
 g(t)=\log{2-t\over t}-\pi(1-t),                   \tag{3.1}
\]

because

\[
 H'(t)=2a\left((2-t)e^{-a(2-t)^2}-te^{-at^2}\right).
\]

Moreover,

\[
 g'(t)=\pi-{2\over t(2-t)},
 \qquad
 g''(t)={4(1-t)\over t^2(2-t)^2}>0.                \tag{3.2}
\]

Thus `g'` is strictly increasing, while

\[
 \lim_{t\downarrow0}g(t)=+\infty,
 \qquad
 g(2/3)=\log2-\pi/3<0.                              \tag{3.3}
\]

The last inequality follows already from `log 2<1<pi/3`.  Hence `g`
crosses zero once, from positive to negative.  The function `H` first
increases and then decreases, and in particular has no interior minimum on
`[0,2/3]`.  Therefore, for every `0<=b<=2/3`,

\[
 H(t)\ge\min\{H(0),H(b)\}
 \qquad(0\le t\le b).                               \tag{3.4}
\]

## 4. Rational Gaussian bounds at the three endpoints

Put

\[
 p=e^{-\pi/36}.
\]

The classical bound `pi<22/7` gives `pi/36<11/126`.  For
`u=11/126`, bounding the Taylor tail geometrically from its quadratic term
gives

\[
 e^u
 <1+u+{u^2/2\over1-u/3}
 ={100921\over92484}
 <{250\over229}.                                    \tag{4.1}
\]

The last comparison is the integer inequality

\[
 250\cdot92484-229\cdot100921=10091>0.
\]

Thus

\[
 p>{229\over250}=:q.                                \tag{4.2}
\]

The following consequences use only integer arithmetic:

\[
\begin{gathered}
 q^4>{879\over1250}>{7\over10},\\
 q^8>{247\over500},
 \qquad q^{16}>{61\over250}>{6\over25},\\
 q^{25}>{11\over100},
 \qquad q^{36}>{1\over25}.                         \tag{4.3}
\end{gathered}
\]

For transparency, the first comparison follows from

\[
 229^4=2750058481>2746875000
       ={879\over1250}\,250^4.
\]

Squaring gives

\[
 (879/1250)^2>{247\over500},
 \qquad
 (247/500)^2>{61\over250}.
\]

Then

\[
 {61\over250}{247\over500}{229\over250}
 ={3450343\over31250000}>{11\over100},
\]

and

\[
 \left({61\over250}\right)^2{7\over10}
 ={26047\over625000}>{1\over25},
\]

which proves the last two inequalities in (4.3).

The special values of `H` are

\[
\begin{aligned}
 H(0)&=1+p^{36},\\
 H(1/3)&=p+p^{25},\\
 H(2/3)&=p^4+p^{16}.
\end{aligned}                                       \tag{4.4}
\]

Equations (3.4) and (4.2)--(4.4) imply the two uniform bounds

\[
 H(t)>{47\over50}
 \qquad(0\le t\le2/3),                              \tag{4.5}
\]

and

\[
 H(t/2)>{513\over500}
 \qquad(0\le t\le2/3).                             \tag{4.6}
\]

Indeed, for (4.5) the two possible endpoint values are bounded below by

\[
 H(0)>1+{1\over25},
 \qquad
 H(2/3)>{7\over10}+{6\over25}={47\over50},
\]

while for (4.6) they are bounded below by

\[
 H(0)>1+{1\over25},
 \qquad
 H(1/3)>{229\over250}+{11\over100}={513\over500}.
\]

## 5. Positivity of both endpoint rows

Let `t=y/A`.  From (2.6), (2.7), and (4.3),

\[
 C(A)>{1\over25}-\varepsilon.                      \tag{5.1}
\]

Using (2.5) and (4.5),

\[
\begin{aligned}
 J_1(y)
 &=2C(A)+f(t)\\
 &>{2\over25}-2\varepsilon-1+{47\over50}-\varepsilon\\
 &={1\over50}-3\varepsilon
  >{397\over20000}>0.                              \tag{5.2}
\end{aligned}
\]

Likewise, (2.5), (4.5), and (4.6) give

\[
\begin{aligned}
 J_2(y)
 &=C(A)+f(t/2)+f(t)\\
 &>{1\over25}-\varepsilon
   +{513\over500}-1-\varepsilon
   +{47\over50}-1-\varepsilon\\
 &={3\over500}-3\varepsilon
  >{117\over20000}>0.                              \tag{5.3}
\end{aligned}
\]

Combining (1.4), (5.2), and (5.3) proves (0.2), with the explicit uniform
margin

\[
 \boxed{
 \mathcal L_3(A;z,y)>{117\over20000}
 }
\]

throughout the full compact triangle.

## 6. Exact scope

This note proves only the remaining fixed-period analytic row for the
three-slot regime-II Bellman normal form.  Together with the already proved
period monotonicity and boundary closure in the source theorem, it closes
the `n=3` Bellman positivity theorem.  It does not prove positivity for
tables with `n>=4`, the universal all-clock inequality, a coagulation
kernel construction, or any palette/compiler conclusion.
