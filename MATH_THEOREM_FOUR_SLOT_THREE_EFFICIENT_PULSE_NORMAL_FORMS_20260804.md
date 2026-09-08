# Four-slot three-efficient clocks: exact pulse normal forms and closed normalized faces

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction with positive subfaces.
It preserves every finite transient in the three-slot-efficient `n=4`
regime.  Complete positivity of the regime is not proved here.

Let

\[
 (c_0,c_1,c_2,c_3,c_4)=(0,x,y,z,T)
\]

be internally superadditive, and suppose `z/3` is a maximal efficiency.
Put

\[
 u=T-z,qquad w=\max\{y,2u\},qquad
 v=\max\{y,u+x\}.
\tag{0.1}
\]

The exact four-slot normal form gives

\[
 x\le u\le z/3,qquad y\le w\le2z/3,qquad
 v\le w,qquad u+y\le z,
\tag{0.2}
\]

and its comparison with the effective three-slot table `(0,u,w,z)` is

\[
\begin{aligned}
 \mathcal B_4={}&\mathcal L_3(z;u,w)\\
 &+K(x)-K(u)+K(y)-K(w)+K(z+v)-K(z+w),
\end{aligned}
\tag{0.3}
\]

where

\[
 \mathcal L_3(P;a,b)=
 \sum_{q\ge0}\bigl(K(qP)+K(qP+a)+K(qP+b)\bigr).
\tag{0.4}
\]

All three terms in the second line of (0.3) are retained below.

## 1. A monotonic interval for the kernel

### Lemma 1.1

The kernel `K` is decreasing on `[0,2A/3]`.

#### Proof

Put `a=pi/4`, `x=At`, and `h(s)=s exp(-as^2)`.  For `0<=t<1`,

\[
 K'(At)=2A\bigl(h(1+t)-h(1-t)\bigr).
\]

Moreover

\[
 \log{h(1-t)\over h(1+t)}
 =\pi t-2\operatorname{arctanh}t=:f(t).
\tag{1.1}
\]

The function `f` is concave on `[0,2/3]`, because

\[
 f''(t)=-{4t\over(1-t^2)^2}\le0.
\]

Its endpoint values satisfy `f(0)=0` and

\[
 f(2/3)={2\pi\over3}-\log5>0:
\]

indeed `pi>3` and `e^2>5`.  A concave function lies above its endpoint
chord, so `f(t)>=0` throughout.  Hence `h(1-t)>=h(1+t)` and `K'(At)<=0`.
\(\square\)

Let `sigma` again denote socket measure minus job measure.  Then

\[
 K(a)-K(b)=\sigma([a,b))\qquad(0\le a\le b).
\tag{1.2}
\]

Intervals below are occurrence-labelled: if two intervals overlap, their
`sigma` masses are added with multiplicity.

### Proposition 1.2 (all normalized periods are already closed)

If `z>=A`, then the four-slot Bellman functional is strictly positive,
without any additional restriction on `u`.

#### Proof

The first displayed threshold crossing occurs at capacity at most three.
Delete every later denomination by the first-crossing theorem.  The
resulting prefix has grid size at most three and is strictly positive by the
complete three-slot Bellman theorem.  First-crossing deletion can only
lower the functional, so the original four-slot table is strictly positive
as well. \(\square\)

## 2. The face `w=y`

### Theorem 2.1 (one-transient face)

If `w=y`, then automatically `v=y`, and

\[
 \boxed{
 \mathcal B_4=\mathcal L_3(z;u,y)+\sigma([x,u)).
 }
\tag{2.1}

The effective residues have ordered cyclic gaps:

\[
 u\le y-u\le z-y.
\tag{2.2}

#### Proof

The condition `w=y` says `y>=2u`.  Since `x<=u`,
`u+x<=2u<=y`, so (0.1) gives `v=y`.  Substitution in (0.3) leaves only
`K(x)-K(u)`, which is (2.1) by (1.2).

The first inequality in (2.2) is `y>=2u`.  The second is
`z+u>=2y`, which is the original constraint `T>=2y`. \(\square\)

### Theorem 2.2 (normalized moderate-residue closure)

On the `w=y` face, if

\[
                         z\ge A,qquad u\le {2A\over3},
\tag{2.3}
\]

then

\[
                         \boxed{\mathcal B_4>0}.
\tag{2.4}

#### Proof

The effective table `(0,u,y,z)` is internally superadditive.  It lies in
regime II of the proved three-slot theorem: `3y<=2z`, and

\[
 \max\{u,2y-z\}=u
\]

because `z+u>=2y`.  Its Bellman sum is exactly
`mathcal L_3(z;u,y)`, and it is strictly positive since `z>=A`.

By Lemma 1.1, `x<=u<=2A/3` gives `K(x)-K(u)>=0`.  Now apply (2.1).
\(\square\)

The unresolved subcritical effective clock has the exact domain

\[
 {3A\over4}\le z<A,qquad
 A-z\le u\le z/3,qquad
 2u\le y\le{z+u\over2}.
\tag{2.5}

Here the transient in (2.1) is nonnegative because `u<A/3`.  Thus only
`mathcal L_3(z;u,y)` remains.

The ordered-gap structure has an exact uniform-lattice comparison.  Put

\[
\begin{aligned}
 P_1&=\sum_{q\ge0}[qz+u,qz+z/3),\\
 P_2&=\sum_{q\ge0}[qz+y,qz+2z/3),
\end{aligned}
\tag{2.6}

where the sums denote occurrence-labelled interval families.  Then

\[
 \boxed{
 \mathcal L_3(z;u,y)
 =C(z/3)+\sigma(P_1)+\sigma(P_2).
 }
\tag{2.7}

Indeed, split `C(z/3)` into its three residue classes modulo `z` and use
(1.2).  Relation (2.2) implies `u<=z/3` and `y<=2z/3`, so both intervals
have the displayed orientation.  Equation (2.7), on (2.5), is the exact
subcritical analytic gate for this face.

This gate admits one further exact dimension reduction.

### Theorem 2.3 (strict period monotonicity)

Fix `u,y` satisfying the ordered-gap constraints, and put

\[
 \Psi(P)=\mathcal L_3(P;u,y).
\]

On every feasible interval

\[
 {3A\over4}\le P\le A,\qquad
 u\le P/3,\qquad y\le2P/3,\qquad P+u\ge A,
\tag{2.8}
\]

one has

\[
                         \boxed{\Psi'(P)>0}.
\tag{2.9}

#### Proof

All terms with period index `q>=2` lie in the increasing Gaussian tail,
so their derivatives are positive.  Both shifted `q=1` terms also lie in
the tail.  Only the bare term `K(P)` can have negative derivative.

Normalize `p=P/A` and write `h(s)=s exp(-pi*s^2/4)`.  Since
`u/A<=p/3`, `y/A<=2p/3`, and `h` decreases at these tail arguments, the
total `q=1` derivative, divided by `2A`, is at least

\[
 R(p):=-h(1-p)+h(1+p)+h(1+4p/3)+h(1+5p/3).
\tag{2.10}

We prove `R(p)>0` on `[3/4,1]`.  First,

\[
\begin{aligned}
 R''(p)={}&-h''(1-p)+h''(1+p)\\
 &+{16\over9}h''(1+4p/3)+{25\over9}h''(1+5p/3)>1.
\end{aligned}
\tag{2.11}

The first term is nonnegative.  The function `h''` has only one maximum
on each of the positive-argument intervals below, so its minimum is at an
endpoint.  Exact rational bounds give

\[
 h''(x)>{2\over5}\quad(7/4\le x\le2),
\]

\[
 h''(x)>{1\over4}\quad(2\le x\le7/3),
 \qquad
 h''(x)>{1\over10}\quad(9/4\le x\le8/3).
\tag{2.12}

Thus the right side of (2.11) exceeds

\[
 {2\over5}+{16\over9}{1\over4}
 +{25\over9}{1\over10}={101\over90}>1.
\tag{2.13}

Here is a compact exact certificate.  Put

\[
 \rho=e^{-\pi/64}.
\]

The classical rational bounds `333/106<pi<22/7` and elementary Taylor
bounds give

\[
                         {119\over125}<\rho<{497\over522}.
\tag{2.14}

For the lower bound, use

\[
 e^{11/224}<1+{11\over224}
 +{(11/224)^2/2\over1-(11/224)/3}<{125\over119}.
\]

For the upper bound, the degree-three positive Taylor polynomial at
`333/(106*64)` is larger than `522/497`.  Substitution in the endpoint
formulas for `h''` proves (2.12) by rational cross-multiplication; for the
two nonintegral exponents use `rho^(784/9)>rho^88` and
`rho^(1024/9)>rho^114`.

At `p=3/4`, the arguments are quarter-integral, and

\[
 R(3/4)=-{\rho\over4}+{7\rho^{49}\over4}
 +2\rho^{64}+{9\rho^{81}\over4}>{9\over200}.
\tag{2.15}

Also

\[
\begin{aligned}
 R'(3/4)={}&(1-\pi/32)\rho+(1-49\pi/32)\rho^{49}\\
 &+{4\over3}(1-2\pi)\rho^{64}
 +{5\over3}(1-81\pi/32)\rho^{81}>-{1\over100}.
\end{aligned}
\tag{2.16}

Both inequalities follow from (2.14), using its lower bound for positive
terms, its upper bound for negative terms, and `pi<22/7`.  Strong
convexity now gives

\[
 R(p)>{9\over200}-{1\over20000}
 ={899\over20000}>0.
\tag{2.17}

Thus the `q=1` derivative is positive; every later derivative is positive
as well.  This proves (2.9). \(\square\)

### Corollary 2.4 (two boundary surfaces)

For fixed feasible `u,y`, define

\[
 P_0=\max\{A,2y\}-u.
\tag{2.18}

Then every feasible `z` satisfies `z>=P_0`, and

\[
 \boxed{
 \mathcal L_3(z;u,y)\ge\mathcal L_3(P_0;u,y).
 }
\tag{2.19}

#### Proof

The constraints `z+u>=A` and `z+u>=2y` give `z>=P_0`.  Since `y>=2u`,
the number `2y-u` also dominates `3u`, `3y/2`, and `u+y`; if `A-u` is
larger, then `A>2y>=4u` gives the same domination.  Thus every period in
`[P_0,z]` remains feasible and at least `3A/4`.  Apply Theorem 2.3.
\(\square\)

Consequently the whole subcritical `w=y` gate reduces to

\[
 P_0+u=A\quad(2y\le A),
 \qquad
 P_0+u=2y\quad(2y\ge A).
\tag{2.20}

No interior period remains.

## 3. The face `w=2u`

### Theorem 3.1 (three-pulse transient)

If `w=2u`, then

\[
 \boxed{
 \mathcal B_4=\mathcal L_3(z;u,2u)
 +\sigma([x,u))+\sigma([y,2u))
 +\sigma([z+v,z+2u)).
 }
\tag{3.1}

#### Proof

This is (0.3), with each difference rewritten using (1.2).  The interval
orientations follow from `x<=u`, `y<=2u`, and `v<=2u`. \(\square\)

The effective clock itself has an exact comparison with the uniform
three-step lattice.  Define

\[
\begin{aligned}
 Q_1&=\sum_{q\ge0}[qz+u,qz+z/3),\\
 Q_2&=\sum_{q\ge0}[qz+2u,qz+2z/3).
\end{aligned}
\tag{3.2}

Since `z>=3u`,

\[
 \boxed{
 \mathcal L_3(z;u,2u)
 =C(z/3)+\sigma(Q_1)+\sigma(Q_2).
 }
\tag{3.3}

Thus the entire `w=2u` face is one arithmetic ceiling margin plus five
explicit occurrence-labelled pulse families.  No abstract effective-clock
deficiency remains.

There is one immediate positive normalized subface.

### Corollary 3.2

If

\[
 z\ge A,qquad u\le A/3,qquad v=2u,
\tag{3.4}

then `mathcal B_4>0`.

#### Proof

The effective table `(0,u,2u,z)` is a normalized regime-II three-slot
table, so `mathcal L_3(z;u,2u)>0`.  The last pulse in (3.1) is empty.
The first two pulses are nonnegative by Lemma 1.1 because their endpoints
lie in `[0,2A/3]`. \(\square\)

Condition `v=2u` includes either boundary `y=2u` or `x=u`.

## 4. Exact remaining frontier

The three-slot-efficient four-slot regime has been reduced to two explicit
objects:

1. on `w=y`, the two boundary surfaces (2.20);
2. on `w=2u`, the five occurrence-labelled pulses in (3.1)--(3.3), outside
   the normalized subface (3.4).

By Proposition 1.2, both objects may be restricted to `z<A`.

Every exceptional Bellman value appears in these formulas.  In particular,
the negative tail pulse `[z+v,z+2u)` is not discarded.  This note does not
sign the remaining pulse systems, prove the complete three-efficient
regime, prove the four-state Apéry regime, or prove the universal Bellman
inequality.
