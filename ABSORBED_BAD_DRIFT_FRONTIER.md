# Sharp absorbed benefit, bad-hull mass, and the drift frontier

## 1. Exact absorbed excess at a fixed successor level

Work at the bottom dangerous threshold.  For an absorbed seam let `t` be
the normalized positive level of its successor line.  Absorption gives

\[
 p\le1+t,\qquad s\le2-t,
\]

and always `p,s>=1`, `z>=0`, `p+s+z<=4`.  Its excess over the average
service cost is

\[
 \Delta_A=ps+z\min(p,s)-{4\over3}(p+z).
\]

Direct optimization gives the exact envelope

\[
g(t)=\max\Delta_A=
\begin{cases}
 {2\over3}-{t\over3}-t^2,&0\le t\le{1\over3},\\
 {1\over3}+{2t\over3}-t^2,&{1\over3}\le t\le{1\over2},\\
 {4\over3}-{4t\over3}-t^2,&{1\over2}\le t\le{2\over3},\\
 {2\over3}-t,&{2\over3}\le t\le1.
\end{cases}                                             \tag{1.1}
\]

The maximizing configurations are, successively,

\[
(p,s,z)=(1+t,2-t,0),\quad(1+t,2-t,1),quad
(2-t,2-t,2t),\quad(1,2-t,0).                            \tag{1.2}
\]

The function `g` is nonincreasing.  In particular,

\[
                 \Delta_A\le {2\over3}-{t\over3}.       \tag{1.3}
\]

If `A` is total absorbed mass, same-line uniqueness gives one successor
measure per direction dominated by `dt`; their combined density is at most
three.  Therefore the bathtub principle gives the sharp count-only bound

\[
 \int\Delta_A\,d\rho_A
 \le3\int_0^{A/3}g(t)\,dt
 \le{2A\over3}-{A^2\over18}.                             \tag{1.4}
\]

At a fixed threshold `1<=c<4/3`, the simpler pointwise bound is

\[
 \Delta_A\le a(c):=c\left({5\over3}-c\right),            \tag{1.5}
\]

with equality at `(p,s,z)=(c,3-c,0)`.

## 2. Direction-labelled bad-hull bound

Let `B` be normalized bad-seam count and put `u_j=2-p_j`.  Every bad edge
satisfies

\[
                         z_j>u_j+u_{j+1}.                 \tag{2.1}
\]

Count both endpoint plateaux of every bad edge with multiplicity.  A
dangerous plateau with `u<=x` lies on an absolute coordinate level at most
`x`.  Across three directions and two signs there are at most `6x a+O(1)`
such lines, and an endpoint occurs in at most two bad edges.  Hence the
normalized endpoint-incidence distribution `eta` obeys

\[
                         \eta([0,x])\le12x,
 \qquad \|\eta\|=2B.                                    \tag{2.2}
\]

The bathtub minimum of its `u`-moment is `B^2/6`.  Since (2.1) charges this
moment to the total gap budget `delta`,

\[
 \boxed{B\le\sqrt{6\delta}.}                             \tag{2.3}
\]

The normalized word mass in bad records consequently satisfies

\[
 \boxed{b\le2\sqrt{6\delta}+\delta+o(1).}                \tag{2.4}
\]

This halves both constants in the previous unlabelled estimate.

## 3. The saturated scalar survivor fails stationarity

At `delta=0`, every nonabsorbed record has `z=0` and the self-closed service
margin is at least `4/3`.  In the range `3/2<A<2`, (1.4) is explicitly

\[
 G(A)=3\int_0^{A/3}g(t)\,dt
 =-{7\over12}+{4A\over3}-{2A^2\over9}-{A^3\over27}.       \tag{3.1}
\]

The scalar boundary uses

\[
 f={A+3\over2},\qquad N=f-A={3-A\over2},qquad
 G(A)={4N\over3}.                                         \tag{3.2}
\]

Its unique solution in `(3/2,2)` is

\[
 A_*=1.70817256009\ldots,
\]

the root of

\[
                 4A^3+24A^2-216A+279=0.                  \tag{3.3}
\]

Equality in the bathtub bound fills every direction on
`[0,A_*/3]`.  From the maximizers (1.2), its absorbed predecessor/successor
length drift is

\[
 \int_{\rho_A}(s-p)
 =3\int_0^{1/2}(1-2t)\,dt={3\over4}.                      \tag{3.4}
\]

But the remaining mass is only

\[
 N={3-A_*\over2}=0.64591371995\ldots<{3\over4},           \tag{3.5}
\]

and every seam has `|s-p|<=1`.  It cannot cancel (3.4).  This contradicts
the exact equality of predecessor and successor length marginals.  Hence the
fully saturated scalar extremizer is not a coherent seam process.

## 4. Exact remaining target

The drift argument above uses equality in all bathtub and service bounds.
It does not exclude ledgers with larger absorbed mass or slack benefit.
The remaining analytic problem is a Pareto inequality that bounds

\[
 \int\Delta_A
\]

jointly with

\[
 \left|\int_{ho_A}(s-p)\right|,
\]

then charges the compensating drift to nonabsorbed and bad records using
their self-closed service margins.  No scalar line-count inequality can
replace this common-marginal coupling.
