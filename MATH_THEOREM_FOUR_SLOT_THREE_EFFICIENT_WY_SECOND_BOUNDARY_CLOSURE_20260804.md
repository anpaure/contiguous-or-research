# Closure of the second `w=y` boundary by a theta slope comparison

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves the remaining
`P+u=2y` surface of the `w=y` face positive.  Combined with the first
boundary and period-monotonicity results in
`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_PULSE_NORMAL_FORMS_20260804.md`,
it closes the subcritical `w=y` effective-clock gate.  It makes no claim
about the `w=2u` face or the full Bellman problem.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  For `P>0`, define

\[
 \mathcal L_3(P;u,y)
 =\sum_{q\ge0}\bigl(K(qP)+K(qP+u)+K(qP+y)\bigr).
\tag{0.1}
\]

## 1. Statement

### Theorem 1.1

Assume

\[
 {A\over2}\le y\le {2A\over3},
 \qquad
 2y-A\le u\le {y\over2},
 \qquad
 P=2y-u.
\tag{1.1}
\]

Then

\[
                         \boxed{\mathcal L_3(P;u,y)>0.}
\tag{1.2}
\]

The endpoint `y=2A/3` is included; there the interval in (1.1) consists of
the single value `u=A/3`.

Write

\[
                         b=y-u.
\tag{1.3}
\]

Then

\[
 {y\over2}\le b\le A-y,
 \qquad
 u=y-b,
 \qquad
 P=y+b.
\tag{1.4}
\]

Thus the ordered gaps in one period are exactly

\[
                         (u,b,b).
\tag{1.5}
\]

The proof shows that the corresponding train is strictly increasing as
the repeated gap `b` increases.  Its minimum is the uniform pattern
`(y/2,y/2,y/2)`.

## 2. A compact-to-tail slope comparison

Put

\[
 h(t)=t e^{-\pi t^2/4},
 \qquad
 D(t)=h(1+t)-h(1-t)\qquad(0\le t\le1).
\tag{2.1}
\]

For `0<=t<=1`, direct differentiation of the compact branch gives

\[
                         K'(At)=2A D(t).
\tag{2.2}
\]

### Lemma 2.1

The function `D` is strictly increasing on `[2/3,1]`.

#### Proof

Since

\[
 h'(s)=e^{-\pi s^2/4}\left(1-{\pi s^2\over2}\right),
\]

one has

\[
                         D'(t)=h'(1+t)+h'(1-t).
\tag{2.3}
\]

For `2/3<=t<=1`, put `r=1-t` and `s=1+t`.  Then
`0<=r<=1/3` and `5/3<=s<=2`.

The classical bounds `333/106<pi<22/7` imply

\[
 e^{-\pi r^2/4}>e^{-\pi/36}>{9\over10},
 \qquad
 1-{\pi r^2\over2}>1-{\pi\over18}>{52\over63}.
\]

Indeed `pi/36<11/126`, and

\[
 e^{11/126}
 <1+{11/126\over1-(11/126)/2}
 ={263\over241}<{10\over9}.
\]

Hence

\[
                         h'(r)>{26\over35}.
\tag{2.4}
\]

On the other hand,

\[
 \left({\pi s^2\over2}-1\right)<{37\over7},
 \qquad
 e^{-\pi s^2/4}\le e^{-25\pi/36}<e^{-25/12}<{1\over8}.
\]

The last inequality follows from the degree-seven positive Taylor sum

\[
 \sum_{j=0}^{7}{(25/12)^j\over j!}
 = {289664104889\over36118462464}>8.
\]

Therefore

\[
                         h'(s)>-{37\over56}.
\tag{2.5}
\]

Combining (2.3)--(2.5),

\[
                         D'(t)>{26\over35}-{37\over56}
                         ={23\over280}>0.
\]

This proves the lemma. \(\square\)

### Lemma 2.2 (reflected compact slopes)

For every `0<=a<=1/3`,

\[
                         \boxed{D(1-a)>D(a).}
\tag{2.6}
\]

#### Proof

Let

\[
 S(a)=\sum_{n\in\mathbb Z}(n+a)e^{-\pi(n+a)^2/4}.
\tag{2.7}
\]

Pairing the four terms `n=0,-1,1,-2` and then the remaining two tails gives

\[
 S(a)=-R(a)+T(a),
\tag{2.8}
\]

where

\[
\begin{aligned}
 R(a)&=D(1-a)-D(a)\\
 &=h(2-a)+h(1-a)-h(a)-h(1+a),\\
 T(a)&=\sum_{k\ge2}\bigl(h(k+a)-h(k+1-a)\bigr).
\end{aligned}
\tag{2.9}
\]

The function `h` decreases on `[2,infinity)`.  Since `a<=1/3`, every
summand of `T(a)` is nonnegative, and

\[
 T(a)\ge h(2+a)-h(3-a)\ge h(7/3)-h(8/3).
\tag{2.10}
\]

The following two rational bounds are elementary:

\[
                         h(7/3)>{1\over40},
 \qquad
                         h(8/3)<{1\over80}.
\tag{2.11}
\]

For the first, `pi<22/7` gives

\[
 {49\pi\over36}<{30\over7}.
\]

The exponential series gives

\[
 e<1+1+{1\over2}+{1/6\over1-1/4}
 ={49\over18}<{11\over4},
\]

while `e^{2/7}<1/(1-2/7)=7/5`.  Consequently

\[
 e^{49\pi/36}<e^{30/7}
 <\left({11\over4}\right)^4{7\over5}
 ={102487\over1280}<{280\over3},
\]

which implies `h(7/3)>1/40`.

For the second, `pi>333/106` gives

\[
 {16\pi\over9}>{296\over53}.
\]

The degree-eight positive Taylor sum satisfies

\[
 \sum_{j=0}^{8}{(296/53)^j\over j!}
 ={4633837100358140947\over19611802479578715}
 >{640\over3}.
\]

Thus `e^{16pi/9}>640/3`, which is equivalent to the second inequality in
(2.11).  It follows that

\[
                         T(a)>{1\over80}.
\tag{2.12}
\]

Poisson summation gives

\[
 S(a)=16\sum_{m\ge1}m e^{-4\pi m^2}\sin(2\pi ma).
\tag{2.13}
\]

Since `pi>3`, and the degree-eight positive Taylor sum at `3` gives
`e^3>20`,

\[
 |S(a)|
 \le16\sum_{m\ge1}m e^{-4\pi m^2}
 <{16e^{-12}\over1-2e^{-36}}
 <{1\over5000}.
\tag{2.14}
\]

Equations (2.8), (2.12), and (2.14) yield

\[
 R(a)=T(a)-S(a)
 >{1\over80}-{1\over5000}
 ={123\over10000}>0.
\]

This proves (2.6). \(\square\)

### Corollary 2.3

If

\[
 0\le a\le {1\over3},
 \qquad
 1-a\le p\le1,
\]

then

\[
                         \boxed{K'(Ap)>K'(Aa).}
\tag{2.15}
\]

#### Proof

Both `1-a` and `p` lie in `[2/3,1]`.  Lemma 2.1 and Lemma 2.2 give

\[
 D(p)\ge D(1-a)>D(a).
\]

Now apply (2.2). \(\square\)

## 3. Monotonicity of the repeating-gap train

Fix `y` in `[A/2,2A/3]`, and for

\[
                         {y\over2}\le b\le A-y
\]

put

\[
 u=y-b,
 \qquad
 P=y+b,
 \qquad
 H_y(b)=\mathcal L_3(P;u,y).
\tag{3.1}
\]

### Lemma 3.1

The function `H_y` is strictly increasing on its interval.

#### Proof

The Gaussian tails permit termwise differentiation.  Since

\[
 qP+u=(q+1)y+(q-1)b,
 \qquad
 qP+y=(q+1)y+qb,
\]

one obtains

\[
\begin{aligned}
 H_y'(b)={}&-K'(u)+K'(P)+K'(P+y)\\
 &+\sum_{q\ge2}\Bigl(
 qK'(qP)+(q-1)K'(qP+u)+qK'(qP+y)
 \Bigr).
\end{aligned}
\tag{3.2}
\]

Put `a=u/A` and `p=P/A`.  The domain gives

\[
 0\le a\le {1\over3},
 \qquad
 p+a={2y\over A}\ge1,
 \qquad
 p\le1.
\]

Hence Corollary 2.3 gives

\[
                         K'(P)>K'(u).
\tag{3.3}
\]

Every remaining argument in (3.2) is at least `A`: one has
`P+y>A`, and for `q>=2`, `qP>=3A/2`.  On this Gaussian tail `K'>0`.
Therefore every term left after the strictly positive difference in (3.3)
is nonnegative, and in fact `H_y'(b)>0`. \(\square\)

## 4. Proof of Theorem 1.1

By (1.4) and Lemma 3.1,

\[
 \mathcal L_3(2y-u;u,y)
 =H_y(y-u)
 \ge H_y(y/2).
\]

At `b=y/2`, put `s=y/2`.  Then `u=s`, `P=3s`, and the three residue
classes interlace into the complete arithmetic clock:

\[
 H_y(y/2)
 =\sum_{q\ge0}\bigl(K(3qs)+K((3q+1)s)+K((3q+2)s)\bigr)
 =C(s).
\tag{4.1}
\]

The proved all-ceiling theorem gives `C(s)>0` for every `s>0`.  Therefore

\[
                         \mathcal L_3(2y-u;u,y)>0.
\]

This proves Theorem 1.1. \(\square\)

## 5. Exact scope

The theorem closes precisely the second boundary in

\[
 P_0+u=2y,
 \qquad
 {A\over2}\le y<{2A\over3},
 \qquad
 2y-A\le u\le y/2.
\]

Together with the already-proved first boundary `P_0+u=A` and strict
period monotonicity, this proves the entire subcritical effective-clock term
on the `w=y` face positive.  The compact transient `K(x)-K(u)` on that face
is separately nonnegative by the parent theorem.

No assertion is made about the `w=2u` pulse system, the remaining
large-residue normalized tail scope, arbitrary three-efficient tables, the
all-slot Bellman inequality, or `nu(k)<=B(k)+O(1)`.
