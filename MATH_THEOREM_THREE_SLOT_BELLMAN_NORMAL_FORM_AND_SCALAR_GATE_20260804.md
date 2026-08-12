# Three-slot Bellman clocks: exact normal form and a scalar Gaussian gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  Every three-slot
Bellman table is strictly positive.  The proof uses exact max-plus normal
forms, a scalar theta estimate, and a separately audited fixed-period
triangle theorem.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Consider a three-slot
internally superadditive table

\[
 (c_0,c_1,c_2,c_3)=(0,x,y,T),                       \tag{0.1}
\]

so that

\[
 0\le x,\qquad y\ge2x,\qquad T\ge x+y,
 \qquad T\ge A.                                      \tag{0.2}
\]

Its unbounded-knapsack Bellman clock is

\[
 V_m=\max_{1\le j\le3}(c_j+V_{m-j}),
 \qquad V_0=0.                                       \tag{0.3}
\]

This note classifies `V` exactly and reduces the only critical part of one
regime to a single explicit Gaussian inequality.

## 1. Exact two-regime normal form

For a period `P` and shifts, write

\[
 \mathcal L_2(P;z)=
 \sum_{q\ge0}\bigl(K(qP)+K(qP+z)\bigr),             \tag{1.1}
\]

and

\[
 \mathcal L_3(P;z,y)=
 \sum_{q\ge0}
 \bigl(K(qP)+K(qP+z)+K(qP+y)\bigr).                 \tag{1.2}
\]

### Theorem 1.1 (three-slot Bellman normal form)

There are two cases.

### (I) The two-slot generator has maximal efficiency

If

\[
 2T\le3y,                                            \tag{1.3}
\]

put `z=T-y`.  Then `x<=z<=y/2`, and

\[
 V_{2q}=qy,
 \qquad
 V_{2q+1}=
 \begin{cases}
 x,&q=0,\\
 qy+z,&q\ge1.
 \end{cases}                                         \tag{1.4}
\]

Consequently

\[
 \boxed{
 \sum_{m\ge0}K(V_m)
 =\mathcal L_2(y;z)+K(x)-K(z).
 }                                                     \tag{1.5}
\]

### (II) The three-slot generator has maximal efficiency

If

\[
 3y\le2T,                                            \tag{1.6}
\]

put

\[
 z=\max\{x,2y-T\}.                                   \tag{1.7}
\]

Then `0<=x<=z<=T/3`, and

\[
\begin{aligned}
 V_{3q}&=qT,\\
 V_{3q+1}&=
 \begin{cases}
 x,&q=0,\\
 qT+z,&q\ge1,
 \end{cases}\\
 V_{3q+2}&=qT+y.
\end{aligned}                                        \tag{1.8}
\]

Consequently

\[
 \boxed{
 \sum_{m\ge0}K(V_m)
 =\mathcal L_3(T;z,y)+K(x)-K(z).
 }                                                     \tag{1.9}
\]

At equality `2T=3y`, the two descriptions agree.

#### Proof

First suppose (1.3).  Two one-slot generators may be replaced by one
two-slot generator because `y>=2x`.  Two three-slot generators may be
replaced by three two-slot generators because `3y>=2T`.  If one residual
one-slot and one residual three-slot generator both remain, replace them by
two two-slot generators, using

\[
 x+T\le (T-y)+T\le2y.
\]

Thus an optimal configuration contains only two-slot generators, together
with at most one residual generator of odd size.  At capacity `2q` its
value is `qy`.  At capacity `2q+1`, the residual choice is either one
one-slot generator, giving `qy+x`, or, for `q>=1`, one three-slot generator
and `q-1` two-slot generators, giving `qy+T-y`.  Since `T-y>=x`, (1.4)
follows.  Equivalently, direct substitution in (0.3) verifies the induction:
`z+x<=y` and `2T<=3y` control the even row, while the size-two and
size-three predecessors attain the odd row.

Now suppose (1.6).  Replace pairs of one-slot generators by a two-slot
generator and triples of two-slot generators by two three-slot generators.
After those replacements, the only residue representatives are:

* no residue, giving `qT` at capacity `3q`;
* one two-slot generator, giving `qT+y` at capacity `3q+2`;
* either one one-slot generator or two two-slot generators in place of one
  three-slot generator, giving respectively `qT+x` and
  `qT+2y-T` at capacity `3q+1`.

The efficiency inequalities show that no discarded representative is
better.  For a direct recurrence check, the needed inequalities are

\[
 x+y\le T,
 \qquad z+y\le T,
 \qquad z+x\le y.
\]

The first is (0.2).  The other two follow separately from
`z=x` and `z=2y-T`, using `y>=2x`, `T>=x+y`, and `3y<=2T`.
They verify all three predecessors in each residue class of (0.3).
Conditions (0.2) and (1.6) also give

\[
 x\le {y\over2}\le {T\over3},
 \qquad
 2y-T\le {T\over3},
\]

which proves the asserted range of `z`.  This proves (1.8), and summing the
two normal forms gives (1.5) and (1.9). \(\square\)

## 2. The critical part of regime I is one-dimensional

Define

\[
 \mathcal H(P):=\mathcal L_2(P;A-P),
 \qquad {2A\over3}\le P\le A.                       \tag{2.1}
\]

Its endpoint values are arithmetic-clock margins:

\[
 \mathcal H(2A/3)=\sum_{m\ge0}K(mA/3)>0,
 \qquad
 \mathcal H(A)=2\sum_{m\ge0}K(mA)>0.                \tag{2.2}
\]

### Theorem 2.1 (scalar reduction in the subcritical-period branch)

In regime I, assume `y<A`.  Then

\[
 {2A\over3}\le y<A,
 \qquad
 A-y\le z\le {y\over2},                             \tag{2.3}
\]

and

\[
 \boxed{
 \sum_{m\ge0}K(V_m)
 \ge \min\{\mathcal H(y),\ C(y/2)\},
 }                                                     \tag{2.4}
\]

where `C(a)=sum_(m>=0)K(ma)>0` is the proved ceiling margin.
Consequently the one-variable inequality

\[
 \boxed{
 \mathcal H(P)\ge0
 \qquad(2A/3\le P\le A)
 }                                                     \tag{2.5}
\]

would close all of regime I with `y<A`.

#### Proof

Since `T>=A` and `T<=3y/2`, (2.3) follows from `z=T-y`.  Also
`0<=x<=z<=y/2<A/2`.

The kernel is strictly decreasing on `[0,A/2]`.  Indeed, with
`t=u/A<=1/2` and `phi(v)=v exp(-v^2)`,

\[
 \log{\phi(A+u)\over\phi(A-u)}
 =2\operatorname{arctanh}(t)-\pi t<0,                \tag{2.6}
\]

because

\[
 \operatorname{arctanh}(t)
 \le {t\over1-t^2}\le {4t\over3}
 \quad\hbox{and}\quad {8\over3}<\pi.
\]

Thus `K(x)>=K(z)`, so the transient correction in (1.5) is nonnegative.

It remains to minimize `mathcal L_2(y;z)` on the interval in (2.3).  For
`z>=A-y`, all terms with positive period index lie in the Gaussian tail,
and

\[
 F_y(z):=\sum_{q\ge0}K(qy+z)
 =1-e^{-(A-z)^2}
  -\sum_{q\ge0}e^{-(A+z+qy)^2}.                      \tag{2.7}
\]

At an interior critical point, the logarithmic-derivative argument from
the two-slot theorem gives

\[
 {1\over2}F_y''(z)
 \le2A\left({1\over A^2-z^2}-2\right)
       (A-z)e^{-(A-z)^2}<0,                          \tag{2.8}
\]

because `z<=y/2<A/2`.  Hence every interior critical point is a strict
maximum, and the minimum is at an endpoint.  At the two endpoints,

\[
 \mathcal L_2(y;A-y)=\mathcal H(y),
 \qquad
 \mathcal L_2(y;y/2)=C(y/2).
\]

Together with the nonnegative transient correction, this proves (2.4).
\(\square\)

## 3. The scalar theta gate is positive

### Theorem 3.1

For every

\[
                         {2A\over3}\le P\le A,
\]

one has

\[
                         \boxed{\mathcal H(P)>0}.                 \tag{3.1}
\]

Consequently every regime-I table with `y<A` has a strictly positive
Bellman sum.

#### Proof

Put

\[
                         t={P\over A}\in[2/3,1],
 \qquad a=A-P.
\]

Only the four values `0,P,a,A` in the two residue classes are at most
`A`.  Expanding their four kernel values and writing the remaining terms
as Gaussian tails gives

\[
\begin{aligned}
 \mathcal H(P)=3-2e^{-A^2}-e^{-4A^2}
 &-\bigl(e^{-A^2(t-1)^2}+e^{-A^2(t+1)^2}
          +e^{-A^2t^2}+e^{-A^2(t-2)^2}\bigr)\\
 &-R(t),                                                    \tag{3.2}
\end{aligned}
\]

where

\[
 R(t)=\sum_{q\ge2}e^{-A^2(1+qt)^2}
      +\sum_{n\ge1}e^{-A^2(2+nt)^2}.                         \tag{3.3}
\]

The four terms in parentheses are four terms of the full integer Gaussian
lattice

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-A^2(t-j)^2}.
\]

Since `A^2=pi/4`, Poisson summation gives

\[
 \Theta(t)=2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt)
 \le2+\varepsilon,
 \qquad
 \varepsilon:=4\sum_{m\ge1}e^{-4\pi m^2}.                  \tag{3.4}
\]

Write `M=1-2e^{-pi/4}`.  Equations (3.2)--(3.4) imply

\[
 \mathcal H(P)\ge M-e^{-\pi}-\varepsilon-R(t).              \tag{3.5}
\]

It remains only to record uniform elementary bounds.  The rational
Gaussian estimate already used for the ceiling theorem gives

\[
 M>{3\over35},\qquad e^{-\pi}<{1\over20},
 \qquad M-e^{-\pi}>{1\over28}.                              \tag{3.6}
\]

Also `pi>3` and `e^3>20` give

\[
 \varepsilon
 <{4e^{-12}\over1-e^{-36}}<{1\over20000}.                   \tag{3.7}
\]

Every summand in (3.3) decreases with `t`, so take `t=2/3`.
Successive terms in its first series have ratio at most
`e^{-8pi/9}`, and successive terms in its second series have ratio at most
`e^{-pi}`.  The elementary Taylor bounds

\[
 e^4>50,\qquad e^{8/3}>{100\over7},\qquad e^3>20
\]

therefore give

\[
\begin{aligned}
 R(t)
 &\le {e^{-49\pi/36}\over1-e^{-8\pi/9}}
      +{e^{-16\pi/9}\over1-e^{-\pi}}\\
 &<{1/50\over1-1/14}
      +{49/10000\over1-1/20}
  <{1\over46}+{1\over190}
  <{1\over36}.                                             \tag{3.8}
\end{aligned}
\]

For completeness, all three exponential inequalities in the preceding
line follow by truncating the positive Taylor series: through degree eight
for `e^3`, through degree seven for `e^4`, and through degree seven for
`e^(8/3)`.  No decimal estimate is used.

Finally (3.5)--(3.8) yield

\[
 \mathcal H(P)>{1\over28}-{1\over20000}-{1\over36}>0.
\]

The last assertion follows from Theorem 2.1. \(\square\)

### Theorem 3.2 (complete regime-I positivity)

Every three-slot table satisfying

\[
                            2T\le3y
\]

has a strictly positive Bellman sum.

#### Proof

The case `y<A` is Theorems 2.1 and 3.1.  Suppose `y>=A`.  Formula (1.5)
and `z>=x` give

\[
\begin{aligned}
 \sum_{m\ge0}K(V_m)
 &=C(y)+K(x)-\sum_{q\ge1}e^{-(A+qy+z)^2}\\
 &\ge C(y)+K(x)-\sum_{q\ge1}e^{-(A+qy+x)^2}\\
 &=\mathcal L_2(y;x).                                  \tag{3.9}
\end{aligned}
\]

The table `(0,x,y)` is internally superadditive because `2x<=y`, and its
endpoint satisfies `y>=A`.  The two-slot theorem therefore says that the
last expression is strictly positive. \(\square\)

## 4. Regime II reduces to one compact triangle

### Theorem 4.1 (period monotonicity and boundary closure)

In regime II, fix `x,y` and vary `T` over its admissible range.  The
Bellman sum is nondecreasing in `T`.  Its least admissible period is

\[
 T_0=\max\{A,3y/2\}.                                  \tag{4.1}
\]

If `y>=2A/3`, the Bellman sum is strictly positive.  If `y<=2A/3`, it is
enough to prove

\[
 \boxed{
 \mathcal L_3(A;z,y)>0,
 \qquad
 z=\max\{x,2y-A\},
 }                                                     \tag{4.2}
\]

on the compact triangle

\[
 0\le x\le y/2,
 \qquad 0\le y\le2A/3.                               \tag{4.3}
\]

#### Proof

In (1.8), the physical first value `x` is fixed.  The arguments `qT` and
`qT+y` increase with `T`.  If `z=x`, so do `qT+z`.  If
`z=2y-T`, then

\[
 qT+z=(q-1)T+2y,
\]

which is constant for `q=1` and increasing for `q>=2`.  All these
positive-period arguments lie in `[A,infinity)`, where `K` is increasing.
This proves period monotonicity.  Since `x<=y/2`, the constraint
`T>=x+y` is weaker than `T>=3y/2`, proving (4.1).

Suppose first that `y>=2A/3`.  At `T_0=3y/2`, put `s=y/2`.  Then `z=s`,
the three residue classes interlace into the arithmetic clock of step `s`,
and (1.9) becomes

\[
 \sum_{m\ge0}K(V_m)=C(s)+K(x)-K(s).                  \tag{4.4}
\]

If `s<=A/2`, then `K(x)>=K(s)` because `0<=x<=s` and `K` decreases on
`[0,A/2]`, so (4.4) is at least `C(s)>0`.

Now let `s>=A/2`.  If `x<=A/2`, then for every `m>=2`, both `ms` and
`mA/2` lie in the increasing Gaussian tail and `ms>=mA/2`.  Therefore

\[
\begin{aligned}
 C(s)+K(x)-K(s)
 &=K(0)+K(x)+\sum_{m\ge2}K(ms)\\
 &\ge C(A/2)+K(x)-K(A/2)\\
 &\ge C(A/2)>0.
\end{aligned}                                        \tag{4.5}
\]

If instead `x>=A/2`, then `s>=x`, and the same tail comparison gives

\[
 K(0)+K(x)+\sum_{m\ge2}K(ms)
 \ge\sum_{m\ge0}K(mx)=C(x)>0.                       \tag{4.6}
\]

This closes `y>=2A/3`.

Finally take `y<=2A/3`.  Then `T_0=A`, and

\[
 0\le x\le z\le A/3.
\]

The kernel decreases on this interval, so the transient correction
`K(x)-K(z)` in (1.9) is nonnegative.  Dropping it leaves exactly (4.2).
\(\square\)

### Corollary 4.2 (two one-variable boundary functions)

Put

\[
 F(u)=\sum_{q\ge0}K(qA+u).
\]

The compact triangle (4.2)--(4.3) follows from the two one-variable
inequalities

\[
 \boxed{
 2C(A)+F(y)>0,
 \qquad
 C(A)+F(y/2)+F(y)>0
 \quad(0\le y\le2A/3).
 }                                                     \tag{4.7}
\]

#### Proof

For fixed `y`, every allowed `z` lies in `[0,y/2]`, which is contained in
`[0,A/3]`.  On this interval the critical-point calculation (2.8) applies
to `F`: every interior critical point is a strict maximum.  Hence

\[
 F(z)\ge\min\{F(0),F(y/2)\}.                         \tag{4.8}
\]

Since `F(0)=C(A)` and

\[
 \mathcal L_3(A;z,y)=C(A)+F(z)+F(y),
\]

substitution of the two endpoints in (4.8) gives exactly (4.7).
\(\square\)

### Theorem 4.3 (three-slot positivity)

Every internally superadditive table

\[
 (c_0,c_1,c_2,c_3)=(0,x,y,T),
 \qquad T\ge A,
\]

has a strictly positive Bellman sum.

#### Proof

Theorem 3.2 closes regime I.  In regime II, Theorem 4.1 closes
`y>=2A/3` and reduces the remaining case to (4.2)--(4.3).  Corollary 4.2
reduces that triangle to the two functions in (4.7).

The independently audited theta-completion theorem
`MATH_CANDIDATE_PROOF_THREE_SLOT_REGIME_II_TRIANGLE_20260804.md` proves

\[
 2C(A)+F(y)>{397\over20000},
 \qquad
 C(A)+F(y/2)+F(y)>{117\over20000}                  \tag{4.9}
\]

uniformly for `0<=y<=2A/3`.  Its proof completes each shifted Gaussian
row to the full Jacobi lattice, reduces the remainder to a two-Gaussian
envelope with no interior minimum, and verifies the endpoint margins by
rational Taylor bounds.  Hence the compact triangle is positive, and all
of regime II is closed. \(\square\)

Thus a finite Bellman counterexample, if one exists, must have grid size
at least four.  This theorem does not prove the all-clock inequality or
`nu(k)<=B(k)+O(1)`.
