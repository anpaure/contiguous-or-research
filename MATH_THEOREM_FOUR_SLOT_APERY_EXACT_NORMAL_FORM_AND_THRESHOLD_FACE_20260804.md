# Four-slot-efficient Bellman clocks: exact Apéry normal form and threshold-face positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It enumerates the
four-state Apéry witnesses, keeps every capacity below nine exactly, and
proves the complete four-slot-efficient threshold face `T=A` positive.
For an arbitrary four-slot-efficient table it leaves only one explicit
one-variable boundary inequality, displayed in (7.6).  It does not prove
that last inequality here.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Consider a nonnegative
internally superadditive four-slot table defined by

\[
 (c_0,c_1,c_2,c_3,c_4)=(0,x,y,z,T).                 \tag{0.1}
\]

Its resulting constraints are

\[
 y\ge2x,\qquad z\ge x+y,\qquad
 T\ge x+z,\qquad T\ge2y.                           \tag{0.2}
\]

Assume throughout that

\[
                         T\ge A.                   \tag{0.2a}
\]

Suppose also that the size-four generator has maximal efficiency:

\[
 {T\over4}\ge {y\over2},\qquad
 {T\over4}\ge {z\over3}.                          \tag{0.3}
\]

Write

\[
 \alpha={T\over4},\qquad
 d_1=x-\alpha,\quad d_2=y-2\alpha,
 \quad d_3=z-3\alpha.                              \tag{0.4}
\]

Then

\[
 d_1,d_2,d_3\le0,qquad
 d_2\ge2d_1,qquad d_3\ge d_1+d_2,qquad
 d_1+d_3\le0.                                      \tag{0.5}
\]

For a period `P` and shifts define

\[
 \mathcal L_4(P;a,b,c)
 =\sum_{q\ge0}\bigl(K(qP)+K(qP+a)+K(qP+b)+K(qP+c)\bigr).
                                                               \tag{0.6}
\]

## 1. Exact enumeration of the four-state Apéry witnesses

### Theorem 1.1

The maximum reduced weights in residues `1,2,3 mod 4` are

\[
\boxed{
 \begin{aligned}
 \beta_1&=\max\{d_1,d_2+d_3,3d_3\},\\
 \beta_2&=\max\{d_2,2d_3\},\\
 \beta_3&=d_3.
 \end{aligned}}
                                                               \tag{1.1}
\]

Equivalently, put

\[
\boxed{
 \begin{aligned}
 s_1&=\alpha+\beta_1
     =\max\{x,y+z-T,3z-2T\},\\
 s_2&=2\alpha+\beta_2
     =\max\{y,2z-T\},\\
 b_1&=\max\{x,y+z-T\}.
 \end{aligned}}
                                                               \tag{1.2}
\]

Then

\[
 0\le x\le s_1\le\alpha,qquad
 0\le y\le s_2\le2\alpha,qquad z\le3\alpha.       \tag{1.3}
\]

#### Proof

Every reduced step weight is nonpositive.  If a walk repeats a residue, the
intervening closed subwalk has nonpositive weight and may be deleted without
decreasing the total weight.  Hence a maximum reduced witness may be chosen
simple.  A simple path from zero in `Z/4Z` has at most three edges.  Suppressing
the order of steps with the same multiset, the complete list of reduced
weights is

\[
\begin{array}{c|l}
1&d_1, d_2+d_3, d_1+2d_2, 3d_3\\
2&d_2, 2d_1, 2d_3, d_1+d_2+d_3\\
3&d_3, d_1+d_2, 3d_1, 2d_2+d_3.
\end{array}                                                     \tag{1.4}
\]

In residue one, `d_1+2d_2<=d_1`.  In residue two,
`d_2>=2d_1`, while `d_1+d_2+d_3<=d_2` by
`d_1+d_3<=0`.  In residue three, (0.5) gives

\[
 d_3\ge d_1+d_2\ge3d_1,qquad d_3\ge2d_2+d_3.
\]

This proves (1.1), and (1.2)--(1.3) are its translation back to physical
weights. \(\square\)

## 2. Every exceptional capacity below nine

### Theorem 2.1 (literal finite head)

The Bellman clock is exactly

\[
\begin{array}{c|ccccccccc}
m&0&1&2&3&4&5&6&7&8\\ \hline
V_m&0&x&y&z&T&T+b_1&T+s_2&T+z&2T.
\end{array}                                                     \tag{2.1}
\]

At capacity nine the last Apéry witness arrives:

\[
                         V_9=2T+s_1.              \tag{2.2}
\]

Thereafter the clock is periodic in value:

\[
\boxed{
 V_{4q}=qT,quad
 V_{4q+1}=qT+s_1\ (q\ge2),quad
 V_{4q+2}=qT+s_2\ (q\ge1),quad
 V_{4q+3}=qT+z\ (q\ge0).
}                                                               \tag{2.3}
\]

Consequently

\[
\boxed{
\begin{aligned}
 \Phi(x,y,z,T):=\sum_{m\ge0}K(V_m)
 ={}&\mathcal L_4(T;s_1,s_2,z)\\
 &+K(x)-K(s_1)+K(y)-K(s_2)\\
 &+K(T+b_1)-K(T+s_1).
\end{aligned}}                                                  \tag{2.4}
\]

#### Proof

Internal superadditivity gives `V_m=c_m` for `m<=4`.  At capacity five,
every partition is dominated by either `4+1` or `3+2`, giving
`T+b_1`.  The residue-two Apéry paths have ordinary capacities two and
six, so capacity six gives `T+s_2`.  In residue three the direct step is
already optimal by (1.1), giving `T+z` at capacity seven.  Capacity eight
is `2T`.  The only simple witness not yet physically available is the
three-step path `3+3+3`, of capacity nine; it supplies `3z`, and hence
(2.2).  Padding by size-four generators proves (2.3).  Substitution into
the four shifted lattices gives (2.4), without suppressing any finite
capacity. \(\square\)

## 3. Period monotonicity and the three boundary faces

### Lemma 3.1

For fixed `x,y,z`, the Bellman functional is nondecreasing in `T` on the
four-slot-efficient range.

#### Proof

Increasing `T` can only increase every Bellman maximum.  Capacities below
four are fixed.  At every capacity `m>=4`, one size-four generator gives
`V_m>=T>=A`; hence all changed arguments lie in the increasing Gaussian
tail of `K`.  The result follows term by term. \(\square\)

Since `z>=x+y>=3x`, the inequality `4z/3>=x+z` always holds.  Thus the
least admissible endpoint in this regime is

\[
                         T_0=\max\{A,2y,4z/3\}.     \tag{3.1}
\]

If `T_0=2y`, the table lies on the already-proved two-efficient face.
If `T_0=A`, it is the threshold face proved below.  If `T_0=4z/3`, it
reduces to the one-variable gate in Section 7.

## 4. Three elementary Gaussian train facts

For `0<=u<=A`, write

\[
 F(u)=\sum_{q\ge0}K(qA+u),\qquad C(A)=F(0).          \tag{4.1}
\]

### Lemma 4.1

One has

\[
\boxed{
 C(A)>{1\over25},qquad
 F(u)>{1\over25}\quad(0\le u\le A/4),qquad
 F(u)>0\quad(0\le u\le A/2).
}                                                               \tag{4.2}
\]

Moreover

\[
                         F(u)<{1\over20}
 \qquad(A/4\le u\le A/2).                         \tag{4.3}
\]

#### Proof

Put `M=1-2e^{-pi/4}`.  The proved rational bounds

\[
 M>{3\over35},\qquad e^{-\pi}<{7\over160},qquad
 \sum_{n\ge3}e^{-\pi n^2/4}<{1\over800}            \tag{4.4}
\]

give

\[
 C(A)=M-\sum_{n\ge2}e^{-\pi n^2/4}
 >{3\over35}-{7\over160}-{1\over800}
 ={57\over1400}>{1\over25}.                        \tag{4.5}
\]

At the quarter shift,

\[
 F(A/4)=1-e^{-9\pi/64}
 -\sum_{n\ge1}e^{-\pi(n+1/4)^2/4}.                 \tag{4.6}
\]

The exact rational exponential bounds

\[
\begin{array}{c|ccc|c}
 &e^{-9\pi/64}&e^{-25\pi/64}&e^{-81\pi/64}
 &\displaystyle\sum_{n\ge3}e^{-\pi(n+1/4)^2/4}\\ \hline
\text{upper}&129/200&47/160&19/1000&1/1000\\
\text{lower}&641/1000&7/24&37/2000&0
\end{array}                                                     \tag{4.7}
\]

imply

\[
                         {1\over25}<F(A/4)<{1\over20}.          \tag{4.8}
\]

All inequalities in (4.4) and (4.7) are rational certificates: use
`333/106<pi<22/7`, the positive Taylor polynomial for a lower exponential
bound, and the Taylor polynomial plus its geometric remainder for an
upper bound.  For the two tails, successive ratios are bounded by
`1/100`; cross-multiplication gives the displayed fractions.

The critical-point calculation in the proved two-slot theorem says that
every interior critical point of `F` on `[0,A/2]` is a strict local
maximum.  Hence a minimum on `[0,A/4]` occurs at `0` or `A/4`, proving the
middle assertion of (4.2).

At the half shift, Poisson summation gives

\[
 F(A/2)=2\sum_{m\ge1}(-1)^{m+1}e^{-4\pi m^2}>0,     \tag{4.9}
\]

by the alternating-series test.  The same critical-point statement on
`[0,A/2]` now proves the last assertion of (4.2).

It remains to prove the uniform upper bound.  Put
`h(t)=t e^{-(\pi/4)t^2}`.  Differentiation gives

\[
 {1\over2A}{d\over du}F(u)
 =\sum_{n\ge1}h(n+u/A)-h(1-u/A).                   \tag{4.10}
\]

On `1/4<=u/A<=3/8`, the right side is negative because

\[
 h(1-u/A)>9/20,qquad
 \sum_{n\ge1}h(n+u/A)<17/40.                       \tag{4.11}
\]

On `3/8<=u/A<=1/2`, it is negative because

\[
 h(1-u/A)>2/5,qquad
 \sum_{n\ge1}h(n+u/A)<7/20.                        \tag{4.12}
\]

For (4.11)--(4.12), use that `h` decreases after `1`, retain the first
tail term, and bound the rest by

\[
 h(v)+\int_v^\infty h(t)\,dt
 =h(v)+{2\over\pi}e^{-(\pi/4)v^2};                 \tag{4.13}
\]

the four displayed comparisons again follow from the same rational
Taylor bounds.  Thus `F` decreases on `[A/4,A/2]`, and (4.3) follows from
(4.8). \(\square\)

### Lemma 4.2 (reflected train bound)

For

\[
                         0\le u\le3A/4
\]

one has

\[
                         F(u)>-{1001\over20000}.     \tag{4.14}
\]

#### Proof

There is nothing to prove for `u<=A/2` by Lemma 4.1.  Put `t=u/A` in
`[1/2,3/4]`.  Direct completion to the integer Gaussian lattice gives

\[
 F(At)+F(A(1-t))
 =-4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt).        \tag{4.15}
\]

The already-proved theta estimate bounds the absolute value of the right
side by `1/20000`.  Since `A(1-t)` lies in `[A/4,A/2]`, (4.3) gives
(4.14). \(\square\)

## 5. The delayed residue-one correction

### Lemma 5.1

On the threshold face `T=A`,

\[
 K(A+b_1)-K(A+s_1)>-{101\over4000}.                 \tag{5.1}
\]

#### Proof

Here `0<=b_1<=s_1<=A/4`.  Since `K` increases on the tail, the left side
is minimized after replacing `b_1` by zero and `s_1` by `A/4`.  Therefore

\[
\begin{aligned}
 K(A+b_1)-K(A+s_1)
 &\ge K(A)-K(5A/4)\\
 &=-e^{-\pi}+e^{-81\pi/64}\\
 &>-{7\over160}+{37\over2000}
  =-{101\over4000},
\end{aligned}                                                     \tag{5.2}
\]

using (4.4) and (4.7). \(\square\)

## 6. Complete positivity on the threshold face

### Theorem 6.1

Every four-slot-efficient table with

\[
                         T=A
\]

has strictly positive Bellman sum.  In fact,

\[
                         \Phi(x,y,z,A)>{47\over10000}.           \tag{6.1}
\]

#### Proof

Now `alpha=A/4`, so (1.3) gives

\[
 0\le s_1\le A/4,qquad0\le s_2\le A/2,qquad
 0\le z\le3A/4.                                      \tag{6.2}
\]

Also `x<=s_1` and `y<=s_2`.  The kernel decreases on `[0,A/2]`, so

\[
 K(x)-K(s_1)\ge0,qquad K(y)-K(s_2)\ge0.             \tag{6.3}
\]

Apply the exact formula (2.4), Lemmas 4.1--4.2, and Lemma 5.1:

\[
\begin{aligned}
 \Phi(x,y,z,A)
 &\ge C(A)+F(s_1)+F(s_2)+F(z)-{101\over4000}\\
 &>{1\over25}+{1\over25}+0
   -{1001\over20000}-{505\over20000}\\
 &= {94\over20000}={47\over10000}.
\end{aligned}                                                     \tag{6.4}
\]

This prices the capacity-five transient explicitly; no eventual-period
argument has hidden it. \(\square\)

## 7. The only remaining boundary in the four-efficient regime

Assume a table is already truncated at its first crossing, so `x,y,z<A`.
By Lemma 3.1 it is enough to take `T=T_0` from (3.1).

* If `T_0=A`, Theorem 6.1 applies.
* If `T_0=2y`, the complete two-efficient four-slot theorem applies.
* It remains only that `T_0=4z/3>A`.

In the last case put

\[
                         \alpha={z\over3}\in(A/4,A/3).           \tag{7.1}
\]

For a positive step `a`, write

\[
                         C(a):=\sum_{m\ge0}K(ma).                \tag{7.1a}
\]

Then the Apéry shifts collapse to the exact ceiling shifts

\[
                         s_1=\alpha,qquad s_2=2\alpha,qquad z=3\alpha.
                                                               \tag{7.2}
\]

Indeed the candidate `3z-2T` equals `alpha`, while all other residue-one
candidates are at most `alpha`; similarly `2z-T=2alpha` dominates residue
two.  Formula (2.4) becomes

\[
\begin{aligned}
 \Phi={}&C(\alpha)
 +K(x)-K(\alpha)+K(y)-K(2\alpha)\\
 &+K(4\alpha+b_1)-K(5\alpha).                     \tag{7.3}
\end{aligned}

The first two corrections are nonnegative.  For the second one, the
needed monotonicity of `K` on `[0,2A/3]` follows from

\[
 \log{1+t\over1-t}<\pi t\qquad(0<t\le2/3),          \tag{7.4}
\]

which is the logarithmic form of `K'(At)<0`; its left-minus-right side
has no positive maximum and is negative at `t=2/3` because
`log 5<2pi/3`.  Indeed `e^2>1+2+2=5`, while `pi>3`, so
`log 5<2<2pi/3`.

Since `b_1>=0`, (7.3) is bounded below by the one-variable function

\[
\boxed{
 J(\alpha):=C(\alpha)+K(4\alpha)-K(5\alpha),
 \qquad A/4\le\alpha\le A/3.
}                                                               \tag{7.5}
\]

Thus the single explicit inequality

\[
\boxed{
                         J(\alpha)>0
 \quad(A/4\le\alpha\le A/3)
}                                                               \tag{7.6}
\]

would complete the entire four-slot-efficient regime.  No two- or
three-variable Apéry optimization remains.

## 8. Exact scope

This theorem proves:

1. the complete four-state simple-path Apéry enumeration;
2. the literal Bellman head through capacity eight and the capacity-nine
   stabilization;
3. a single exact functional formula with three finite corrections;
4. complete positivity on the full threshold face `T=A`;
5. reduction of every remaining four-efficient table to (7.6), after the
   already-proved two-efficient boundary is removed.

It does **not** prove (7.6), the three-efficient four-slot regime, the
universal Bellman inequality, or `nu(k)<=B(k)+O(1)`.
