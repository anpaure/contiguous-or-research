# Five-slot size-four-efficient clocks: closure of the active threshold face

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves strict
positivity on the genuinely active endpoint face `T=A` of the five-slot
size-four-efficient branch.  No finite search or numerical optimization is
used.

Put

\[
A={\sqrt\pi\over2},
\qquad
F(v)=F_A(v)=\sum_{q\ge0}K(qA+v),
\qquad
C=F(0).
\tag{0.1}
\]

Consider an internally superadditive table

\[
                       (0,x,y,z,P,A)
\tag{0.2}
\]

on the threshold face of the size-four-efficient regime.  Thus

\[
\begin{gathered}
0\le x\le P/4,
\qquad2x\le y\le P/2,
\qquad x+y\le z\le3P/4,\\
P\ge x+z,
\qquad P\ge2y,
\qquad A\ge P+x,
\qquad A\ge y+z,
\qquad {4A\over5}\le P<A.
\end{gathered}
\tag{0.3}
\]

The endpoint-period Bellman lower bound is

\[
\Phi(x,y,z,P,A)
\ge
\mathscr B_A(x,y,z,P)
:=C+F(x)+F(y)+F(z)+F(P).
\tag{0.4}
\]

## 1. Frozen train facts

We use the already proved exact train estimates

\[
C>{57\over1400},
\tag{1.1}
\]

\[
F(t)<{1593\over22000}
\qquad(0\le t\le A/4),
\tag{1.2}
\]

\[
F(t)>{1\over25}quad(0\le t\le A/4),
\qquad
F(t)>0\quad(0\le t\le A/2),
\tag{1.3}
\]

and

\[
F(A/4)<{293\over6000}.
\tag{1.4}
\]

Every interior critical point of `F` on `[0,A/2]` is a strict local
maximum, and `F` is strictly decreasing on `[A/4,A/2]`.  Finally, Poisson
reflection gives

\[
                         F(t)+F(A-t)>-{1\over20000}
                         \qquad(0\le t\le A).
\tag{1.5}
\]

All constants in (1.1)--(1.5) have rational Taylor/theta certificates in
the audited four-slot threshold theorems.  In particular, (1.4) is the
unrounded rational estimate obtained directly from their displayed
quarter-shift bounds.

## 2. The small reflected pair

Write

\[
                         u=A-P.
\tag{2.1}
\]

Then (0.3) gives

\[
                         0<u\le A/5,
                         \qquad0\le x\le u.
\tag{2.2}

Because every interior critical point on `[0,u]` is a strict maximum, the
minimum of `F` on that interval occurs at an endpoint.  Hence

\[
                         F(x)\ge\min\{C,F(u)\}.
\tag{2.3}

Reflection at `u`, together with (1.1)--(1.2), now gives the uniform bound

\[
\begin{aligned}
C+F(x)+F(P)
&>C+\min\{C,F(u)\}-F(u)-{1\over20000}\\
&>2{57\over1400}-{1593\over22000}-{1\over20000}\\
&={13813\over1540000}>0.
\end{aligned}
\tag{2.4}

For completeness, the second line is valid in both cases.  If `F(u)>=C`,
the preceding expression is `2C-F(u)` before the reflection error.  If
`F(u)<C`, it is `C`, which is larger than the displayed common lower
bound.

## 3. The second reflected pair

If `z<=A/2`, then (1.3) gives both `F(y)>0` and `F(z)>0`; equation (2.4)
already proves `mathscr B_A>0`.

It remains to take `z>A/2` and put

\[
                         v=A-z.
\tag{3.1}

The constraints `y+z<=A` and `z<=3P/4`, with `P=A-u`, give

\[
 y\le v<{A\over2},
 \qquad
 v\ge A-{3P\over4}
   ={A\over4}+{3u\over4}
   \ge {A\over4}.
\tag{3.2}

Reflection gives

\[
                         F(y)+F(z)
                         >F(y)-F(v)-{1\over20000}.
\tag{3.3}

If `y>=A/4`, then `A/4<=y<=v<A/2`; monotonic decrease of `F` gives
`F(y)>=F(v)`.  Combining (2.4) and (3.3) is strictly positive.

If instead `y<A/4`, equations (1.3)--(1.4) and the same monotonic decrease
from `A/4` to `v` give

\[
                         F(y)-F(v)
                         >{1\over25}-{293\over6000}.
\tag{3.4}

Combining the two reflected pairs, and charging both theta errors, yields
the exact worst-case margin

\[
\begin{aligned}
\mathscr B_A
&>2{57\over1400}-{1593\over22000}
  +{1\over25}-{293\over6000}-{1\over10000}\\
&={199\over2310000}>0.
\end{aligned}
\tag{3.5}

## 4. Main theorem

### Theorem 4.1

Every five-slot size-four-efficient table on the endpoint threshold face
`T=A` has strictly positive Bellman functional.  In fact,

\[
                         \boxed{
\Phi(x,y,z,P,A)>{199\over2310000}.}
\tag{4.1}

#### Proof

The endpoint-period comparison (0.4) reduces the claim to positivity of
`mathscr B_A`.  Sections 2--3 exhaust `z<=A/2` and `z>A/2`; equation (3.5)
is the smaller of the displayed uniform margins. \(\square\)

### Corollary 4.2

After monotone endpoint normalization

\[
T_*=\max\{A,P+x,y+z\},
\]

a nonpositive five-slot size-four-efficient table can survive only on one
of the two Bellman-inert faces

\[
                         T_*=P+x
                         \qquad\hbox{or}\qquad
                         T_*=y+z.
\tag{4.2}

Equivalently, only the two subcritical four-denomination clocks whose first
threshold composite is `4+1` or `2+3` remain.

## 5. Scope

This theorem closes the active threshold face, not the two inert composite
faces.  It therefore does not yet prove the complete five-slot
size-four-efficient branch, the full five-slot Bellman inequality, or any
OR-word upper bound.
