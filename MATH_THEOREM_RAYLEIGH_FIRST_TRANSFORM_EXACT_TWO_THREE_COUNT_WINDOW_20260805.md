# Rayleigh first transform has exact two-to-three socket count window

**Date:** 2026-08-05  
**Method:** pure mathematics; elementary rational interval estimates only;
no search or solver  
**Status:** unconditional.  After the first equal-level subtraction and
one-piece overlap cancellation, the separated residual has strictly
between two and three socket occurrences per job.  Thus the count ledger
permits a mixture of two- and three-socket continuations.  This is only a
count theorem; it does not supply the required configuration coupling.

## 1. Setup

Put

\[
 A={\sqrt\pi\over2},
\qquad
 K(t)=
 \begin{cases}
 1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
 -e^{-(A+t)^2},&t>A.
 \end{cases}
\]

Let `b` be the first positive zero of `K`, let `c` be its unique
minimum, and put

\[
 K_0=K(0),\qquad m=K(c).
\]

For `m<u<0`, let

\[
 \ell(u)\in(b,c),\qquad r(u)\in(c,\infty),
 \qquad K(\ell(u))=K(r(u))=u,
\]

and let `z(u)=r(u)-ell(u)`.  The first equal-level theorem proves that
`z` is strictly increasing from zero to infinity.  Write

\[
 u_b=z^{-1}(b)<0.
\]

After the first transform and cancellation of its one-piece overlap, the
remaining socket and job masses are

\[
 S_2=K_0+m-u_b,
 \qquad
 J_2=-u_b.                                      \tag{1.1}
\]

The question addressed here is the exact position of `S_2/J_2` relative
to the integers two and three.

## 2. Elementary rational certificate

We use only the following standard enclosure.  For rational `x>=0` and
an integer `N` with `x<N+2`, put

\[
 L_N(x)=\sum_{j=0}^N{x^j\over j!},
 \qquad
 U_N(x)=L_N(x)+{x^{N+1}\over(N+1)!}
                  {1\over1-x/(N+2)}.
\]

Then

\[
 L_N(x)<e^x<U_N(x),
 \qquad
 {1\over U_N(x)}<e^{-x}<{1\over L_N(x)}.       \tag{2.1}
\]

The second display follows from the first, and the first follows by
bounding the ratio of consecutive terms in the exponential tail.  Thus
every decimal endpoint used below is a terminating rational and every
inequality in the following table is an exact rational inequality after
substitution in (2.1).  Taking `N=20` is already more than sufficient.

The classical bounds `333/106<pi<355/113` first give

\[
 {4431\over5000}<A<{8863\over10000}.             \tag{2.2}
\]

Direct use of (2.1)--(2.2) gives the following deliberately coarse
certificate:

\[
\begin{array}{c|c}
\text{quantity}&\text{certified inequality}\\ \hline
K_0&0.088<K_0<0.09\\
K(0.46)&K(0.46)>0.002\\
K(0.48)&K(0.48)<-0.002\\
K'(0.772)&K'(0.772)<-0.01\\
K'(0.788)&K'(0.788)>0.006\\
K(0.78)&K(0.78)<-0.05\\
K(0.55),\ K(1.03)&K(0.55)>-0.021>-0.025>K(1.03)\\
K(0.60),\ K(1.06)&K(0.60)<-0.03<-0.023<K(1.06).
\end{array}                                                    \tag{2.3}
\]

For completeness, the only estimate on the minimum not already displayed
in the table is also immediate from the same brackets.  The derivative
signs in (2.3) put

\[
 0.772<c<0.788.
\]

On this interval,

\[
 e^{-(A-c)^2}<0.991,
 \qquad
 e^{-(A+c)^2}<0.064.
\]

Consequently

\[
 -0.055<m< -0.05.                                \tag{2.4}
\]

The right inequality follows from `m<=K(0.78)` and (2.3); the left one
follows from the preceding two upper bounds on the Gaussian summands.
Combining (2.3)--(2.4),

\[
 \boxed{0.033<K_0+m<0.04.}                       \tag{2.5}
\]

No floating-point premise is hidden here: (2.3) is a compact presentation
of finitely many rational comparisons obtained from (2.1).

## 3. Locating the level at separation `b`

The zero signs in (2.3) imply

\[
 0.46<b<0.48.                                    \tag{3.1}
\]

Let

\[
 e=\ell(u_b),\qquad R=r(u_b)=e+b.
\]

We claim

\[
 0.55<e<0.60.                                    \tag{3.2}
\]

Indeed, `K` is strictly increasing on its right inverse branch.  From
`b<0.48` and (2.3),

\[
 K(0.55)>K(1.03)>K(0.55+b).
\]

Therefore the right point at the same level as `0.55` lies to the right
of `0.55+b`; its separation exceeds `b`.  Since the equal-level
separation decreases strictly as the left endpoint moves from `b` to
`c`, this gives `e>0.55`.

Similarly, `b>0.46` and (2.3) give

\[
 K(0.60)<K(1.06)<K(0.60+b).
\]

The equal-level right endpoint belonging to `0.60` therefore lies to the
left of `0.60+b`, so its separation is smaller than `b`.  Hence
`e<0.60`, proving (3.2).

Equations (3.1)--(3.2) yield

\[
 1.01<R<1.08,
 \qquad
 1.8962<A+R<1.9663.                              \tag{3.3}
\]

In particular `R>A`, so the noncompact branch of `K` gives

\[
 -u_b=e^{-(A+R)^2}.
\]

Another direct application of (2.1), now only to the two endpoint squares
in (3.3), gives

\[
 e^{-1.8962^2}<0.03,
 \qquad
 e^{-1.9663^2}>0.02.
\]

Therefore

\[
 \boxed{0.02<-u_b<0.03.}                         \tag{3.4}
\]

## 4. Exact two-to-three count theorem

### Theorem 4.1

The first transformed, overlap-cancelled Rayleigh residual satisfies

\[
 \boxed{2J_2<S_2<3J_2.}                          \tag{4.1}
\]

Equivalently,

\[
 \boxed{K_0+m+u_b>0,\qquad K_0+m+2u_b<0.}        \tag{4.2}
\]

### Proof

Put `P=K_0+m` and `q=-u_b`.  From (2.5) and (3.4),

\[
 P-q>0.033-0.03>0,
\]

whereas

\[
 P-2q<0.04-2(0.02)=0.
\]

Both inequalities are strict.  Since (1.1) says

\[
 S_2=P+q,
 \qquad
 J_2=q,
\]

these are exactly `S_2>2J_2` and `S_2<3J_2`.  `square`

## 5. Exact consequence and exact limitation

Define

\[
 \theta={S_2\over J_2}-2\in(0,1).
\]

At the scalar count level, a fraction `1-theta` of the residual jobs must
use two sockets and a fraction `theta` must use three sockets.  Thus no
arity outside `{2,3}` is required by counts after the first transform.

This does **not** prove that the socket-size measure admits such a
two/three-configuration decomposition.  The remaining exact gate is a
joint-size coupling: construct two- and three-socket configurations with
sum equal to each job while reproducing the literal residual socket
marginal.  Configuration-price inequalities can still obstruct a pair
even when its work and count rows agree.  The theorem proves only that the
Rayleigh compact face lies in the sharp scalar arity window in which a
two/three policy is possible.

## 6. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`,
   SHA at use
   `b63058f76b1ebb4904b4b939b10f981332d7de36bba90a39d8b1a35424787ac6`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.

