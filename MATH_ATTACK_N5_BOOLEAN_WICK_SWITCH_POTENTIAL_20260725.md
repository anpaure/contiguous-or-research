# Fifth-wave N: Boolean-Wick potentials and fixed-degree switch obstructions

## 0. Verdict

There is a constructive nonlinear potential, but it does not create the
missing absolute balancing theorem.

At one rank write

\[
\mu=c\mathbf1+y,\qquad
\frac1N\sum_S\mu(S)=c+\theta,\qquad
f=y-\theta\mathbf1,
\]

where \(y\) is integer-valued and \(N\theta\) is an integer. Define the
pointwise Boolean-Wick defect

\[
\boxed{
\mathfrak d_\theta(f)
=
f^2-(1-2\theta)f-\theta(1-\theta)
=
y(y-1).
}
\tag{0.1}
\]

For integer \(y\), if

\[
d(y)=\operatorname{dist}(y,\{0,1\}),
\]

then

\[
\boxed{
\mathfrak d_\theta(f)=d(y)(d(y)+1),
\qquad
d(y)=\frac{\sqrt{1+4\mathfrak d_\theta(f)}-1}{2}.
}
\tag{0.2}
\]

Thus the exact nonlinear inverse of the Boolean variance/skew defect is
precisely the free-quota corridor penalty. On an exact factor,

\[
\boxed{
\mathcal C_H(F)
=
\sum_{q\le H}\frac1{c_q}
\sum_S
\frac{
\sqrt{1+4\mathfrak d_{\theta_q}(f_q(S))}-1
}{2}
=
\sum_{q\le H}\frac1{c_q}
\sum_S\operatorname{dist}(\mu_q(S)-c_q,\{0,1\}).
}
\tag{0.3}
\]

It vanishes pointwise on every floor-balanced Boolean profile, regardless
of that profile's Johnson harmonic distribution. It therefore subtracts
the unavoidable Boolean skew without asking for near-purity in \(E_2\), or
in any other fixed \(E_j\).

This potential has a genuine exact-factor descent theorem. Given any exact
factor \(G\) with

\[
\mathcal C_H(G)<\mathcal C_H(F),
\]

some cancellation-connected union of complete \(F/G\) ownership
components is a legal integral exact-factor switch and decreases
\(\mathcal C_H\) by at least

\[
\frac{\mathcal C_H(F)-\mathcal C_H(G)}
{|\mathcal K(F,G)|}
\ge
\frac{\mathcal C_H(F)-\mathcal C_H(G)}
{\operatorname{Cat}_m}.
\tag{0.4}
\]

This is favorable deterministic macro-drift toward a known better
comparator. It is not a one-transposition Foster drift, and it neither
bounds packet size nor proves that
\(\min_F\mathcal C_{H_A}(F)=o(W)\).

The fixed-degree polynomial alternatives admit a sharp classification.
After exact Bernoulli subtraction, every scalar polynomial is divisible
by \(y(y-1)\). For \(0<\theta<1\), a genuinely cubic skew discrepancy
changes sign already at \(y=-1\) and \(y=2\). The first robust centered
correction is quartic, and it dominates the old quadratic floor defect
with an explicit constant:

\[
\boxed{
p_{4,\theta}(y)
\ge
\left(1+6\min\{\theta^2,(1-\theta)^2\}\right)y(y-1).
}
\tag{0.5}
\]

Even higher falling factorials have extra integer zeros and are blind;
odd factorials change sign. More generally, every integer-nonnegative
Bernoulli-subtracted polynomial either dominates \(y(y-1)\), or has an
extra integer zero and, at every rational interior mean
\(0<\theta<1\) on sufficiently divisible instances, permits non-Boolean
zero-potential profiles.

There are two further no-go theorems.

1. No fixed-degree polynomial wall penalty that detects \(y=2\) with
   fixed strength can remain uniformly comparable above by the
   linearly growing corridor on an expanding load range. The square-root
   inverse in (0.2) is genuinely non-polynomial.

2. Let a coercive Bernoulli-subtracted polynomial slack be combined with
   a nonnegative Johnson-spectral slack whose kernel is a fixed finite
   level set \(S\). Then

   \[
   \boxed{
   \left(
   \sqrt{\Phi_P/\kappa}
   +
   \sqrt{\mathcal S_Q/\gamma}
   \right)^2
   \ge
   N\theta(1-\theta)[1-\Xi(S)],
   }
   \tag{0.6}
   \]

   where

   \[
   \Xi(S)
   =
   \frac{4e^2\theta}{1-\theta}
   \sum_{j\in S}
   \left(\frac{j^j}{j!}\right)^2
   [8(L-1)]^j,
   \qquad
   L=\log\frac{4\sqrt n}{\theta}.
   \tag{0.7}
   \]

   At \(\theta\asymp1/m\) and fixed \(S\), \(\Xi(S)=o(1)\).
   Polynomial wall near-equality and fixed-band spectral near-equality
   therefore cannot coexist.

Finally, a coordinate-invariant polynomial potential restricted to an
intrinsic transposition cell is antipodally even in the component signs.
A cubic load potential has only pair Walsh interactions and is still a
weighted Max-Cut potential; degree four produces only pair and
four-component parity interactions. No odd/skew component bias survives.
Fair drift averages to zero on every cell, reverse switches have opposite
drift, and a minimum in a legal communicating class blocks strict descent.

The resulting theorem-level conclusion is:

> **Exact dichotomy.** The Boolean-Wick corridor is a valid nonlinear,
> overload-equivalent potential with exact legal macro-descent. Every
> fixed-degree scalar polynomial correction is either noncoercive,
> quantitatively harsher than the quadratic wall defect, or subject to the
> same fixed-kernel harmonic obstruction. None supplies automatic favorable
> transposition drift or an absolute \(o(W)\) exact-factor minimum.

## 1. Exact-factor and switch notation

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

Let \(\mathfrak F_m\) be the finite set of exact middle wreath factors.
Fix \(1\le H\le m-1\). At depth \(q\), write

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
\frac W{N_q}=c_q+\theta_q,
\]

where

\[
c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
0\le\theta_q<1,\qquad
\rho_q=N_q\theta_q\in\mathbb Z.
\]

For \(F\in\mathfrak F_m\), let \(\mu_q^F(S)\) be its rank-\(r_q\)
interval load and put

\[
y_q^F(S)=\mu_q^F(S)-c_q,
\qquad
f_q^F(S)=\mu_q^F(S)-(c_q+\theta_q)
=y_q^F(S)-\theta_q.
\tag{1.1}
\]

Then

\[
\sum_Sy_q^F(S)=\rho_q,
\qquad
\sum_Sf_q^F(S)=0.
\tag{1.2}
\]

All loads and all switches below remain integral inside a single exact
factor.

There are two different switch scopes.

### 1.1 Arbitrary-comparator ownership cubes

For exact factors \(F,G\), cancel common wreaths and decompose their middle
ownership overlay into connected components

\[
\mathcal K(F,G)=\{K_1,\ldots,K_k\}.
\]

Orient every component from its \(F\)-side to its \(G\)-side and let
\(z_i\) be the corresponding wreath-incidence change. Put

\[
v_i=B_Hz_i,
\qquad
B_H=(B_1,\ldots,B_H).
\]

For every \(J\subseteq[k]\),

\[
F_J=F+\sum_{i\in J}z_i
\tag{1.3}
\]

is a genuine exact factor. Moreover,

\[
k\le |F\setminus G|\le B.
\tag{1.4}
\]

This is an exact macro-exchange cube, but it need not be one edge of the
transposition-switch communicating graph.

### 1.2 Intrinsic transposition cells

Fix a coordinate transposition \(\tau\) and take \(G=\tau F\). The
resulting ownership cube is intrinsic: every child has the same component
decomposition. If \(d_i\) is the old-minus-new load vector of component
\(i\), every cell child has the form

\[
x(\varepsilon)
=
\bar x+\frac12\sum_{i=1}^k\varepsilon_i d_i,
\qquad
\varepsilon_i\in\{-1,+1\},
\tag{1.5}
\]

where

\[
\bar x=\frac{\mu^F+\tau\mu^F}{2}.
\]

All \(2^k\) points in (1.5) are exact factors. This narrower scope is used
for the fair-cell, antipodality, and communicating-class results in
Section 7.

## 2. The Boolean-Wick identity

Fix one rank and suppress \(q\). Let

\[
\mu=c\mathbf1+y,\qquad
f=y-\theta\mathbf1,\qquad
\sum_Sy(S)=N\theta.
\]

### Lemma 2.1 — exact pointwise defect

For every integer load coordinate,

\[
\boxed{
f^2-(1-2\theta)f-\theta(1-\theta)=y(y-1).
}
\tag{2.1}
\]

The right side is nonnegative and vanishes exactly when
\(y\in\{0,1\}\).

#### Proof

Substitute \(f=y-\theta\):

\[
\begin{aligned}
f^2-(1-2\theta)f-\theta(1-\theta)
&=(y-\theta)^2-(1-2\theta)(y-\theta)
  -\theta(1-\theta)\\
&=y^2-y.
\end{aligned}
\]

For an integer \(y\), the product \(y(y-1)\) is zero at \(0,1\) and
positive everywhere else. \(\square\)

The summed identities are

\[
\boxed{
\sum_Sy(S)(y(S)-1)
=
\sum_Sf(S)^2-N\theta(1-\theta),
}
\tag{2.2}
\]

and

\[
\boxed{
\sum_Sf(S)y(S)(y(S)-1)
=
\sum_Sf(S)^3-(1-2\theta)\sum_Sf(S)^2.
}
\tag{2.3}
\]

Thus the same pointwise defect subtracts both the balanced Boolean
variance and the unavoidable centered Boolean skew exactly.

### Lemma 2.2 — exact inverse

For integer \(y\), put

\[
d(y)=\operatorname{dist}(y,\{0,1\}).
\]

Then

\[
\boxed{
y(y-1)=d(y)(d(y)+1).
}
\tag{2.4}
\]

Consequently,

\[
\boxed{
d(y)
=
\frac{\sqrt{1+4y(y-1)}-1}{2}
=
\frac{|2y-1|-1}{2}.
}
\tag{2.5}
\]

#### Proof

If \(y\le0\), write \(y=-d\); then
\(y(y-1)=d(d+1)\). If \(y\ge1\), write \(y=1+d\), and the same identity
holds. Finally

\[
1+4y(y-1)=(2y-1)^2.
\]

\(\square\)

Equation (2.5) is the constructive lesson from the higher-harmonic
obstruction: invert the pointwise Boolean identity instead of forcing the
Boolean profile into a low Johnson eigenspace.

## 3. The nonlinear corridor and exact macro-drift

For one integer load vector of total \(cN+\rho\), define

\[
D^-(y)=\sum_S(-y(S))_+,
\qquad
D^+(y)=\sum_S(y(S)-1)_+,
\tag{3.1}
\]

\[
O(y)=\max\{D^-(y),D^+(y)\},
\qquad
C(y)=D^-(y)+D^+(y).
\tag{3.2}
\]

Here \(O\) is the mobile balanced overload and

\[
C(y)=\sum_Sd(y(S)).
\tag{3.3}
\]

### Theorem 3.1 — exact skew-subtracted corridor

Let

\[
p(y)=|\{S:y(S)\ge1\}|.
\]

Then

\[
\boxed{
2O(y)=C(y)+|p(y)-\rho|.
}
\tag{3.4}
\]

In particular,

\[
\boxed{
O(y)\le C(y)\le2O(y).
}
\tag{3.5}
\]

Moreover,

\[
\boxed{
C(y)
=
\sum_S
\frac{
\sqrt{1+4\mathfrak d_\theta(f(S))}-1
}{2}.
}
\tag{3.6}
\]

#### Proof

On the set \(y\ge1\),

\[
\sum_{y(S)\ge1}y(S)=p(y)+D^+(y).
\]

On the complementary set the total is \(-D^-(y)\). Conservation gives

\[
\rho=p(y)+D^+(y)-D^-(y),
\]

so

\[
D^-(y)-D^+(y)=p(y)-\rho.
\]

Now use

\[
2\max(a,b)=a+b+|a-b|
\]

and Lemma 2.2. \(\square\)

Define the weighted exact-factor potential

\[
\boxed{
\mathcal C_H(F)
=
\sum_{q=1}^{H}\frac{C(y_q^F)}{c_q}.
}
\tag{3.7}
\]

The scalar function

\[
\chi(t)=\operatorname{dist}(t,\{0,1\})
\]

has forward differences

\[
\chi(t+1)-\chi(t)
=
\begin{cases}
-1,&t\le-1,\\
0,&t=0,\\
1,&t\ge1.
\end{cases}
\tag{3.8}
\]

They are nondecreasing, so \(\chi\) is discrete convex.

### Definition 3.2 — atomic and cancellation-connected packets

For an \(F/G\) ownership cube, let

\[
\Delta_F(J)
=
\mathcal C_H(F_J)-\mathcal C_H(F).
\tag{3.9}
\]

For a nontrivial cut \(J=I\mathbin{\dot\cup}L\), put

\[
\eta_F(I,L)
=
\Delta_F(J)-\Delta_F(I)-\Delta_F(L).
\tag{3.10}
\]

A nonempty packet \(J\) is \(\mathcal C_H\)-atomic at \(F\) if it is a
singleton, or

\[
\eta_F(I,J\setminus I)<0
\tag{3.11}
\]

for every nonempty proper \(I\subset J\).

Form the sign-cancellation graph on the ownership components by joining
\(K_i,K_j\) when their load effects have opposite nonzero signs in at
least one retained coordinate. A packet is cancellation-connected when
it induces a connected subgraph.

### Theorem 3.3 — favorable legal macro-drift

Let \(F,G\in\mathfrak F_m\), and suppose

\[
g=\mathcal C_H(F)-\mathcal C_H(G)>0.
\]

Then:

1. some \(\mathcal C_H\)-atomic legal packet \(J\subseteq\mathcal K(F,G)\)
   satisfies

   \[
   \boxed{
   \mathcal C_H(F)-\mathcal C_H(F_J)
   \ge\frac g{|\mathcal K(F,G)|}
   \ge\frac gB;
   }
   \tag{3.12}
   \]

2. some cancellation-connected legal packet satisfies the same bound;
3. fixing a global minimizer \(G^*\), repeated such switches toward
   \(G^*\) reach a global minimizer in at most
   \(|\mathcal K(F,G^*)|\le B\) strict moves.

Every endpoint is an integral exact factor.

#### Proof

Start with \(J_0=\mathcal K(F,G)\), for which
\(\Delta_F(J_0)=-g\). Whenever a current packet \(J\) is not atomic,
choose a cut \(J=I\mathbin{\dot\cup}L\) with \(\eta_F(I,L)\ge0\) and
replace \(J\) by \(I,L\). Since

\[
\Delta_F(J)\ge\Delta_F(I)+\Delta_F(L),
\]

the terminal atomic leaves \(P_1,\ldots,P_t\) satisfy

\[
\sum_{\nu=1}^t\Delta_F(P_\nu)\le-g.
\]

As \(t\le|\mathcal K(F,G)|\), one leaf proves (3.12).

For the connected version, decompose the sign-cancellation graph into
components \(J_1,\ldots,J_t\). Effects from distinct graph components are
coordinatewise sign-compatible. For a discrete-convex scalar function,
same-sign increments are superadditive:

\[
\chi(x+a+b)-\chi(x)
\ge
[\chi(x+a)-\chi(x)]
+[\chi(x+b)-\chi(x)]
\tag{3.13}
\]

when \(a,b\ge0\), and likewise when \(a,b\le0\). Summing coordinatewise
gives

\[
\Delta_F(J_0)\ge\sum_{\nu=1}^t\Delta_F(J_\nu).
\]

One graph component therefore has change at most
\(-g/t\le-g/|\mathcal K(F,G)|\).

After switching a packet toward a fixed \(G^*\), all unswitched original
ownership components remain available in the new overlay with \(G^*\).
Every strict move removes at least one such component. The process reaches
\(G^*\), or another factor with the same minimum value, in at most the
original number of components. Legality follows from (1.3). \(\square\)

By (3.5),

\[
\min_F\mathcal C_{H_A}(F)=o(W)
\]

is equivalent to the fixed-window unlabelled overload target. Theorem 3.3
proves descent to that global minimum, not an upper bound on its value.

## 4. Complete scalar polynomial classification

Let \(P\in\mathbb R[t]\). Define its Bernoulli chord defect

\[
\boxed{
p_P(t)
=
P(t)-(1-t)P(0)-tP(1).
}
\tag{4.1}
\]

If \(y_1,\ldots,y_N\in\mathbb Z\) and
\(\sum_i y_i=N\theta\), then

\[
\boxed{
\sum_iP(y_i)
-N[(1-\theta)P(0)+\theta P(1)]
=
\sum_i p_P(y_i).
}
\tag{4.2}
\]

Affine changes in \(P\) therefore change (4.2) by zero.

### Theorem 4.1 — divisibility and dichotomy

There is a unique polynomial \(R_P\) such that

\[
\boxed{
p_P(t)=t(t-1)R_P(t).
}
\tag{4.3}
\]

Furthermore:

1. \(p_P(k)\ge0\) for every integer \(k\) if and only if
   \(R_P(k)\ge0\) for every
   \(k\in\mathbb Z\setminus\{0,1\}\).

2. If \(p_P\not\equiv0\) is integer-nonnegative, it has even degree and
   positive leading coefficient.

3. The exact comparison constant

   \[
   \boxed{
   \kappa(P)
   =
   \min_{k\in\mathbb Z\setminus\{0,1\}}R_P(k)
   }
   \tag{4.4}
   \]

   is attained and satisfies

   \[
   p_P(k)\ge\kappa(P)k(k-1)
   \qquad(k\in\mathbb Z).
   \tag{4.5}
   \]

4. If \(\kappa(P)>0\), the potential is merely a stronger certificate
   than the quadratic Boolean defect. If \(\kappa(P)=0\), there is an
   extra integer zero \(k\notin\{0,1\}\). For every rational
   \(0<\theta<1\), along sufficiently divisible fixed-sum instances,
   non-Boolean zero-potential load vectors exist.

#### Proof

Equation (4.1) vanishes at \(0\) and \(1\), proving the unique
factorization (4.3). Since \(k(k-1)>0\) at every other integer, the first
claim follows.

A nonzero polynomial nonnegative on both integer tails must have even
degree and positive leading coefficient. Consequently \(R_P\) is either a
nonnegative constant or tends to \(+\infty\) on both tails; the minimum in
(4.4) is attained. This proves (4.5).

If \(\kappa(P)=0\), attainment gives an extra integer root \(k\). Fix
rational \(0<\theta<1\). If \(k\ge2\), mix loads \(0,k\) in proportions
\(1-\theta/k,\theta/k\). If \(k\le-1\), mix loads \(k,1\) in proportions
\((1-\theta)/(1-k)\) and \((\theta-k)/(1-k)\). In both cases the mean is
\(\theta\), every summand in (4.2) is zero, and the vector is not Boolean.
The rational proportions become integral for sufficiently divisible
\(N\). At the endpoint densities, an additional root on the appropriate
opposite side is needed for the same conclusion.
\(\square\)

For an actual rank with loads \(\mu\ge0\), only roots
\(-c\le k\le B-c\) are feasible. The all-integer theorem is the robust
statement; the same pointwise comparison dichotomy holds after restricting
the minimum in (4.4) to the actual feasible interval. The zero-profile
mixture conclusion additionally requires the fixed mean to lie in the
convex hull of feasible zero loads.

### 4.1 Centered moments

Assume \(0\le\theta\le1\). For \(r\ge2\), put

\[
p_{r,\theta}(t)
=
(t-\theta)^r
-(1-t)(-\theta)^r
-t(1-\theta)^r.
\tag{4.6}
\]

This subtracts the centered Bernoulli \(r\)-th moment exactly.

For \(r=2\),

\[
\boxed{p_{2,\theta}(t)=t(t-1).}
\tag{4.7}
\]

For \(r=3\),

\[
\boxed{
p_{3,\theta}(t)
=
t(t-1)(t+1-3\theta).
}
\tag{4.8}
\]

Hence

\[
p_{3,\theta}(-1)=-6\theta,
\qquad
p_{3,\theta}(2)=6(1-\theta).
\tag{4.9}
\]

These two displayed witnesses have strict opposite signs when
\(0<\theta<1\). At an endpoint density, the genuine cubic remains
sign-indefinite on the two integer tails, but one of these nearest
witnesses becomes zero.

No affine correction or added multiple of \(t(t-1)\) can make a genuine
cubic nonnegative on both integer tails: after exact Bernoulli subtraction
it still has the form

\[
t(t-1)(at+b),\qquad a\ne0,
\]

whose quotient has opposite tail signs.

Fixed total mass does not rescue (4.8). For rational \(0<\theta<1\) and
sufficiently divisible \(N\), a load vector on \(\{-1,1\}\) with mean
\(\theta\) has total cubic discrepancy

\[
-3N\theta(1-\theta),
\]

whereas a vector on \(\{0,2\}\) with the same mean has discrepancy

\[
+3N\theta(1-\theta).
\tag{4.10}
\]

For \(r=4\),

\[
\boxed{
p_{4,\theta}(t)
=
t(t-1)
\left[
t^2+(1-4\theta)t+1-4\theta+6\theta^2
\right].
}
\tag{4.11}
\]

The quotient is a convex quadratic whose vertex lies in
\([-1/2,3/2]\). Its minimum on
\(\mathbb Z\setminus\{0,1\}\) occurs at \(-1\) or \(2\), where its values
are

\[
1+6\theta^2,
\qquad
1+6(1-\theta)^2.
\]

Therefore

\[
\boxed{
p_{4,\theta}(k)
\ge
\left(1+6\min\{\theta^2,(1-\theta)^2\}\right)k(k-1)
}
\tag{4.12}
\]

for every integer \(k\). The first robust centered-moment correction is
thus only a stronger quadratic wall penalty.

### 4.2 Falling factorials

For \(d\ge2\), the falling factorial

\[
(t)_d=t(t-1)\cdots(t-d+1)
\]

already has zero Bernoulli chord.

- If \(d\) is odd, \((t)_d\) is negative on the negative integer tail.
- If \(d\ge4\) is even, it is integer-nonnegative but vanishes at
  \(2,\ldots,d-1\), so it is blind to non-Boolean loads.
- The factorial square
  \([t(t-1)]^2\) is nonnegative and obeys

  \[
  [t(t-1)]^2\ge2t(t-1)
  \]

  on the integers, with equality among non-Boolean integers at
  \(-1,2\) (and trivially also at \(0,1\)). It again only strengthens the
  quadratic defect.

This recovers, from the Boolean-Wick viewpoint, the collapse of the
normalized factorial hierarchy to its quadratic member.

## 5. Why a faithful polynomial cannot replace the corridor

The preceding classification is qualitative. The next theorem permits
the polynomial coefficients to depend on the size of the feasible load
range and still proves a quantitative obstruction.

### Theorem 5.1 — fixed-degree bounded-slope no-go

Fix \(d\ge2\), \(U\ge2d\), and \(C\ge0\). Let \(p\) be any real
polynomial of degree at most \(d\) such that

\[
p(0)=p(1)=0
\]

and, for every integer \(2\le t\le U\),

\[
0\le p(t)\le C(t-1).
\tag{5.1}
\]

Then

\[
\boxed{
p(2)
\le
\frac{
4(d-1)(2^{d-1}-1)
}{
U-2
}\,C.
}
\tag{5.2}
\]

Consequently, if \(p(2)\ge\kappa>0\), every corridor comparison constant
in (5.1) satisfies

\[
\boxed{
C
\ge
\frac{\kappa(U-2)}
{4(d-1)(2^{d-1}-1)}.
}
\tag{5.3}
\]

No fixed-degree polynomial can both detect the first surplus wall with
uniform strength and remain uniformly comparable above by the linearly
growing corridor as \(U\to\infty\).

#### Proof

Write

\[
p(t)=t(t-1)R(t),
\qquad
\deg R\le d-2.
\]

Put

\[
L_0=\left\lfloor\frac{U-2}{d-1}\right\rfloor
\ge\frac{U-2}{2(d-1)}
\]

and choose the \(d-1\) nodes

\[
x_j=2+jL_0,\qquad 1\le j\le d-1.
\]

All lie in \([2,U]\), and (5.1) gives

\[
0\le R(x_j)=\frac{p(x_j)}{x_j(x_j-1)}
\le\frac C{x_j}
\le\frac C{L_0}.
\tag{5.4}
\]

Lagrange interpolation of the degree-\((d-2)\) polynomial \(R\) at these
nodes yields

\[
R(2)=\sum_{j=1}^{d-1}R(x_j)\ell_j(2),
\]

with

\[
|\ell_j(2)|
=
\prod_{h\ne j}\frac{h}{|j-h|}
=
\binom{d-1}{j}.
\tag{5.5}
\]

Hence

\[
R(2)
\le
\frac C{L_0}\sum_{j=1}^{d-1}\binom{d-1}{j}
=
\frac{(2^{d-1}-1)C}{L_0}.
\]

Since \(p(2)=2R(2)\), the lower bound for \(L_0\) proves (5.2), and
(5.3) follows. \(\square\)

The algebraic square root in (2.5) is therefore not cosmetic. It is what
turns the quadratic Boolean defect into a bounded-slope, overload-faithful
potential.

## 6. Quantitative harmonic two-slack obstruction

This section imports the audited higher-harmonic stability theorem and
derives the precise no-go for polynomial wall potentials combined with
fixed-kernel spectral gates.

Let

\[
\Omega_{n,k}=\binom{[n]}k,\qquad
\frac13\le\frac kn\le\frac23,\qquad
N=|\Omega_{n,k}|.
\]

Let \(c\in\mathbb Z_{\ge0}\), let \(0<\theta<1\) with
\(N\theta\in\mathbb Z\), and let
\(x:\Omega_{n,k}\to\mathbb Z_{\ge0}\) have mean \(c+\theta\). Put

\[
y=x-c,\qquad
f=y-\theta\mathbf1.
\]

For a scalar polynomial \(P\), define its exact rank-\(c\) Bernoulli
defect

\[
\Delta_{P,c}(z)
=
P(c+z)-P(c)-z[P(c+1)-P(c)]
\tag{6.1}
\]

and

\[
\Phi_P(x)=\sum_S\Delta_{P,c}(y(S)).
\tag{6.2}
\]

Assume the substantive coercivity condition

\[
\boxed{
\Delta_{P,c}(z)\ge\kappa z(z-1)
\qquad(z\ge-c,\ z\in\mathbb Z)
}
\tag{6.3}
\]

for some \(\kappa>0\).

Choose the \(N\theta\) largest entries of \(y\), let
\(\mathcal B\) be their index set, and put

\[
b=\mathbf1_{\mathcal B},
\qquad
g=b-\theta\mathbf1.
\]

### Lemma 6.1 — exact polynomial-to-Boolean rounding

\[
\boxed{
\|f-g\|_{2,\mathrm{count}}^2
=
\|y-b\|_2^2
\le
\sum_Sy(S)(y(S)-1)
\le
\frac{\Phi_P(x)}{\kappa}.
}
\tag{6.4}
\]

#### Proof

The last inequality is (6.3). For the first,

\[
\|y-b\|_2^2-\sum_Sy(S)(y(S)-1)
=
2\sum_{S\notin\mathcal B}y(S).
\]

The last sum is nonpositive. Otherwise some unselected integer entry is
at least one; every selected entry is then at least one, so the selected
sum is at least \(N\theta\), contradicting the total sum
\(N\theta\) together with a positive unselected sum. \(\square\)

Let

\[
S\subseteq\{1,\ldots,\min(k,n-k)\}
\]

be a finite nonempty set of positive Johnson levels and put

\[
V_S=\bigoplus_{j\in S}E_j.
\]

Define

\[
L=\log\frac{4\sqrt n}{\theta}
\]

and

\[
\boxed{
\Xi(S)
=
\frac{4e^2\theta}{1-\theta}
\sum_{j\in S}
\left(\frac{j^j}{j!}\right)^2
[8(L-1)]^j.
}
\tag{6.5}
\]

Assume the finite-size hypotheses of the fixed-level theorem for every
\(j\in S\), and \(L\ge2\). Then

\[
\boxed{
\operatorname{dist}_{2,\mathrm{count}}^2(g,V_S)
\ge
N\theta(1-\theta)[1-\Xi(S)].
}
\tag{6.6}
\]

Let \(Q\) be a nonnegative Johnson-spectral operator. Assume

\[
Q|_{E_j}=0\quad(j\in S),
\qquad
Q|_{V_S^\perp\cap E_0^\perp}\ge\gamma I
\tag{6.7}
\]

for some \(\gamma>0\), and put

\[
\mathcal S_Q(f)=\langle f,Qf\rangle.
\tag{6.8}
\]

### Theorem 6.2 — polynomial wall plus spectral-kernel no-go

If \(\Xi(S)<1\), then

\[
\boxed{
\left(
\sqrt{\frac{\Phi_P(x)}{\kappa}}
+
\sqrt{\frac{\mathcal S_Q(f)}{\gamma}}
\right)^2
\ge
N\theta(1-\theta)[1-\Xi(S)].
}
\tag{6.9}
\]

Consequently,

\[
\boxed{
\frac{\Phi_P(x)}{\kappa}
+
\frac{\mathcal S_Q(f)}{\gamma}
\ge
\frac12N\theta(1-\theta)[1-\Xi(S)].
}
\tag{6.10}
\]

#### Proof

The higher-harmonic projection theorem gives

\[
\sum_{j\in S}\|P_jg\|_2^2
\le
4e^2N\theta^2
\sum_{j\in S}
\left(\frac{j^j}{j!}\right)^2
[8(L-1)]^j.
\]

Since \(\|g\|_2^2=N\theta(1-\theta)\), this is (6.6). The spectral gap
in (6.7) gives

\[
\operatorname{dist}_2^2(f,V_S)
\le\frac{\mathcal S_Q(f)}{\gamma}.
\]

By the triangle inequality and Lemma 6.1,

\[
\begin{aligned}
\sqrt{N\theta(1-\theta)[1-\Xi(S)]}
&\le\operatorname{dist}_2(g,V_S)\\
&\le\|g-f\|_2+\operatorname{dist}_2(f,V_S)\\
&\le
\sqrt{\Phi_P/\kappa}
+
\sqrt{\mathcal S_Q/\gamma}.
\end{aligned}
\]

This proves (6.9). Equation (6.10) follows from
\((a+b)^2\le2(a^2+b^2)\). \(\square\)

At \(n=2m+1\), \(\theta\asymp1/m\), and fixed nonempty \(S\),

\[
\Xi(S)=O_S\left(\frac{\log^{\max S}m}{m}\right)=o(1).
\tag{6.11}
\]

Thus simultaneous slacks

\[
\Phi_P=o(N\theta),
\qquad
\mathcal S_Q=o(\gamma N\theta)
\]

are impossible.

For exact-factor early ranks \(1\le q\le K=\lfloor m^{1/3}\rfloor\),
\(c_q=1\) and

\[
\sum_{q\le K}N_q\theta_q(1-\theta_q)
=
\left(\frac13+o(1)\right)W.
\]

If the same fixed \(S\), coercivity constants, and normalized spectral
gaps apply rankwise, summing (6.10) gives

\[
\boxed{
\sum_{q\le K}
\left(
\frac{\Phi_{P,q}}{\kappa_q}
+
\frac{\mathcal S_{Q,q}}{\gamma_q}
\right)
\ge
\left(\frac16-o(1)\right)W.
}
\tag{6.12}
\]

This is the fixed-degree analogue of the exhausted near-equality gate.

### 6.1 Operator-polynomial corollary

Let \(A_J\) be a Johnson-scheme operator with distinct level eigenvalues
\(\lambda_j\), and let \(R_m\) be a nonzero polynomial of degree \(d\)
such that

\[
R_m(\lambda_j)\ge0.
\]

Then \(Q=R_m(A_J)\) has a zero set on at most \(d\) Johnson levels. Discard
an \(E_0\) root, if present, because \(f\perp E_0\), and call the remaining
positive root set \(S\). Exact equality forces \(f\) into \(V_S\).
Approximate equality invokes Theorem 6.2 only after defining

\[
\gamma_m
=
\min_{R_m(\lambda_j)>0}R_m(\lambda_j)
\tag{6.13}
\]

and proving a slack of order \(o(\gamma_mN\theta)\).

If the root indices are fixed and bounded, (6.11) applies. A fixed-degree
operator polynomial may instead place its finitely many roots at
\(m\)-dependent high levels; no fixed-low-band conclusion then follows.
If the positive root set is empty, take \(V_S=\{0\}\) and
\(\Xi(S)=0\); the proof of (6.9)--(6.10) is then immediate with the same
spectral-gap normalization.

### 6.2 Four meanings of degree

The following notions must not be conflated.

1. The scalar load degree of
   \(\sum_SP(\mu(S))\) gives no Johnson cutoff. On a Boolean profile
   \(b\),

   \[
   P(c+b)=P(c)+[P(c+1)-P(c)]b
   \]

   pointwise, regardless of \(\deg P\). More exactly,

   \[
   P(c+b)-[(1-\theta)P(c)+\theta P(c+1)]
   =
   [P(c+1)-P(c)](b-\theta).
   \tag{6.14}
   \]

   Every nonconstant one-site polynomial feature therefore has exactly
   the same Johnson spectrum as the Boolean indicator, up to scale.

2. The degree of an operator polynomial \(R(A_J)\) bounds only the number
   of root levels, not their indices or the outside spectral gap.

3. The multilinear degree of
   \(S\mapsto f(S)\) in the membership coordinates
   \(\mathbf1_{\{i\in S\}}\) genuinely bounds its Johnson support.

4. The interaction arity of a multi-site polynomial does not by itself
   bound Johnson degree unless its interaction kernel also has bounded
   coordinate degree.

Theorem 6.2 requires a separately proved spectral-kernel statement. Scalar
polynomial degree alone does not supply it.

## 7. Exact intrinsic-cell switch calculus

Let \(\Phi\) be a coordinate-invariant separable polynomial potential

\[
\Phi(F)
=
\sum_{q\le H}w_q\sum_Sp_q(\mu_q^F(S)),
\qquad
w_q>0.
\tag{7.1}
\]

Fix an intrinsic \(\tau\)-cell as in (1.5).

### 7.1 Chosen packets and factorial differences

At a current cell vertex, flipping component \(i\) has integral effect
\(\delta_i\). A packet \(J\) has effect

\[
z_J=\sum_{i\in J}\delta_i.
\]

For every legal packet,

\[
\boxed{
\Phi(F_J)-\Phi(F)
=
\sum_{q,S}w_q
\left[
p_q(\mu_q(S)+z_{J,q}(S))-p_q(\mu_q(S))
\right].
}
\tag{7.2}
\]

If \(\deg p_q\le D_q\), Newton's exact finite-difference identity gives

\[
\boxed{
p_q(x+z)-p_q(x)
=
\sum_{r=1}^{D_q}\binom zr\Delta^rp_q(x),
}
\tag{7.3}
\]

with generalized binomial coefficients for negative \(z\).

If

\[
p_q(t)=\sum_{r=0}^{D_q}A_{q,r}(t)_r,
\]

then equivalently

\[
\boxed{
\Phi(F_J)-\Phi(F)
=
\sum_{q,S}w_q
\sum_rA_{q,r}\sum_{s=1}^r
\binom rs
(\mu_q(S))_{r-s}(z_{J,q}(S))_s.
}
\tag{7.4}
\]

No infinitesimal approximation occurs.

For disjoint packets \(I,L\), their exact interaction is

\[
\boxed{
\eta_F(I,L)
=
\sum_{q,S}w_q
\sum_{r,s\ge1}
\binom{z_{I,q}(S)}r
\binom{z_{L,q}(S)}s
\Delta^{r+s}p_q(\mu_q(S)).
}
\tag{7.5}
\]

The atomic splitting proof of Theorem 3.3 therefore remains valid for
every polynomial, convex or not, inside any genuine ownership cube.
Discrete convexity is needed only for the stronger
cancellation-connected conclusion.

### 7.2 Antipodal cancellation

Let

\[
V(\varepsilon)=\Phi(F_\varepsilon)
\]

on the intrinsic cell. Relabelling by \(\tau\) sends
\(F_\varepsilon\) to \(F_{-\varepsilon}\). Coordinate invariance of
\(\Phi\) gives

\[
\boxed{V(-\varepsilon)=V(\varepsilon).}
\tag{7.6}
\]

### Theorem 7.1 — only even component interactions survive

If \(\max_q\deg p_q\le D\), the Walsh expansion

\[
V(\varepsilon)
=
\sum_{A\subseteq[k]}\widehat V(A)\varepsilon_A
\]

satisfies

\[
\boxed{
\widehat V(A)=0
\quad\text{when }|A|\text{ is odd or }|A|>D.
}
\tag{7.7}
\]

From the all-plus vertex, flipping a packet \(I\) changes the potential by

\[
\boxed{
\Delta_I\Phi
=
-2\sum_{\substack{A\ne\varnothing,\ |A|\ {\rm even}\\
                   |A\cap I|\ {\rm odd}}}
\widehat V(A).
}
\tag{7.8}
\]

In particular,

\[
\Delta_I\Phi=\Delta_{I^c}\Phi.
\tag{7.9}
\]

#### Proof

Equation (7.6) changes every Walsh character by
\((-1)^{|A|}\), proving the odd-set cancellation. Since each load
coordinate is affine in \(\varepsilon\), a scalar polynomial of degree
\(D\) has multilinear Walsh degree at most \(D\). Evaluating the expansion
at the all-plus sign and the sign flipped on \(I\) proves (7.8).
For even \(A\),

\[
|A\cap I^c|\equiv |A\cap I|\pmod2,
\]

which proves (7.9). \(\square\)

### Corollary 7.2 — cubic skew remains a pair cut

For \(\deg p_q\le3\), only pair coefficients survive, and

\[
\boxed{
\widehat V(\{i,j\})
=
\frac14
\sum_{q,S}w_q
p_q''(\bar x_q(S))
d_{i,q}(S)d_{j,q}(S).
}
\tag{7.10}
\]

Consequently,

\[
\boxed{
\Delta_I\Phi
=
-\frac12
\sum_{\substack{i\in I\\j\notin I}}
\sum_{q,S}w_q
p_q''(\bar x_q(S))
d_{i,q}(S)d_{j,q}(S).
}
\tag{7.11}
\]

Thus a cubic load correction changes the state-dependent edge weights but
does not create an oriented skew drift. It remains a weighted Max-Cut
problem. Degree four adds only even pair and four-component parity
interactions.

The exact fair value for degree at most three is

\[
\boxed{
K_\tau\Phi
=
\sum_{q,S}w_q
\left[
p_q(\bar x_q(S))
+
\frac18p_q''(\bar x_q(S))
\sum_i d_{i,q}(S)^2
\right].
}
\tag{7.11a}
\]

The cubic Rademacher moment vanishes; its effect survives only through the
state-dependent second derivative in this even expression.

### 7.3 Fair drift and the class-minimum obstruction

Uniform fair resampling of the cell gives its constant mean

\[
K_\tau\Phi(F)
=
2^{-k}\sum_{\varepsilon}V(\varepsilon).
\]

Hence

\[
\boxed{
2^{-k}\sum_{F'\ {\rm in\ the\ cell}}
[K_\tau\Phi(F')-\Phi(F')]=0.
}
\tag{7.12}
\]

If fair drift is nonpositive at every cell vertex, it is identically zero.
If \(\Phi\) is nonconstant on the cell, a cell minimum has positive fair
drift and a cell maximum has negative fair drift.

Every chosen legal packet is reversible, so

\[
\Phi(G)-\Phi(F)=-(\Phi(F)-\Phi(G)).
\tag{7.13}
\]

### Theorem 7.3 — no automatic universal Lyapunov drift

Let \(\mathscr C\) be a communicating class of the intrinsic
transposition-switch graph, and let \(F_*\) minimize \(\Phi\) on
\(\mathscr C\). Then:

1. every chosen legal transposition packet from \(F_*\) has nonnegative
   drift;
2. every fair transposition cell through \(F_*\) has nonnegative fair
   drift;
3. a strict favorable-drift theorem outside a target set \(\mathcal T\)
   is possible only if every relevant communicating-class minimum already
   lies in \(\mathcal T\).

The same conclusion follows from stationary averaging on a finite closed
class.

#### Proof

Every permitted endpoint remains in \(\mathscr C\), so minimality proves
the first two statements. For the third, a minimum outside
\(\mathcal T\) is an immediate counterexample to strict descent.
Equivalently, every stationary law \(\pi\) satisfies

\[
\sum_F\pi(F)[K\Phi(F)-\Phi(F)]=0.
\]

\(\square\)

Affine Bernoulli subtraction cannot change any drift, because every exact
factor has the same total load \(W\) at each rank. Non-affine skew
subtraction may alter the even pair/hyperedge weights, but it cannot defeat
(7.6), reversibility, zero stationary mean, or the class-minimum
obstruction.

The arbitrary-comparator macro-drift theorem and Theorem 7.3 concern
different move graphs. The former must not be used to claim that one
intrinsic transposition class reaches an arbitrary global comparator.

## 8. Synthesis: the exact dichotomy

The fifth-wave conclusion separates four logically different jobs.

### 8.1 Pointwise Boolean subtraction

The polynomial

\[
\mathfrak d_\theta(f)
=
f^2-(1-2\theta)f-\theta(1-\theta)
\]

is the minimal polynomial of the two Boolean values
\(-\theta,1-\theta\). Every one-site polynomial identity modulo the
Boolean fibre is a multiple of it. Its nonlinear inverse is the corridor.

### 8.2 Boolean rounding

A scalar potential supports Boolean rounding only if its Bernoulli chord
defect is coercive, as in (6.3). Every robust integer-nonnegative
polynomial either dominates the quadratic defect or is blind at an extra
integer load. The cubic skew discrepancy is not coercive.

### 8.3 Harmonic placement

Scalar load degree has no control over Johnson degree. If a separate
operator gate forces the rounded Boolean profile into a fixed finite
harmonic kernel, Theorem 6.2 gives an \(\Omega(N\theta)\) combined slack.
The higher-harmonic theorem therefore blocks every such conjunction.

### 8.4 Exact switches

The nonlinear corridor has exact favorable macro-drift toward a known
better exact comparator. Intrinsic transposition drift is governed by even
component interactions and by communicating-class minima. No scalar
potential manufactures a low class or a low global minimum.

The routes left open are:

1. an absolute theorem
   \(\min_F\mathcal C_{H_A}(F)=o(W)\);
2. a wreath-specific small cancellation-connected packet theorem together
   with an absolute bound on the minimum;
3. nonlinear multi-site or rank-coupled interactions whose equality set
   is not a fixed Johnson band;
4. spectral kernels at genuinely growing or mesoscopic degrees, with the
   correct vanishing-gap normalization;
5. a theorem that every intrinsic switch class contains a low-corridor
   factor;
6. non-Boolean component-vector methods; and
7. direct literal contiguous-OR constructions.

None is proved here.

## 9. Independent audit of the decisive steps

The argument was independently audited along three mathematical tracks.

1. **Scalar algebra.** The Bernoulli chord subtraction, divisibility by
   \(t(t-1)\), the cubic signs at \(-1,2\) for \(0<\theta<1\), quartic
   quotient, and factorial zero sets were checked independently. In
   particular, the constant in (4.12) is the minimum of the quotient at
   exactly \(-1\) and \(2\).

2. **Harmonic constants.** The counting/probability conversion in
   \(\Xi(S)\), the exact integer rounding constant one, the triangle
   inequality in (6.9), and the factor \(1/2\) in (6.10) were audited
   independently. Polynomial load degree was explicitly separated from
   Johnson harmonic degree.

3. **Switch scope.** The factorial finite-difference formula, antipodal
   Walsh parity, the \(1/4\) pair coefficient in (7.10), reversibility,
   and zero stationary drift were checked inside genuine integral
   transposition cells. The arbitrary \(F/G\) macro-cube was kept separate
   from the intrinsic transposition communicating graph.

4. **New interpolation bound.** In Theorem 5.1 the interpolation nodes
   number exactly \(d-1\), matching
   \(\deg R\le d-2\). Their Lagrange weights at \(2\) have absolute values
   \(\binom{d-1}{j}\), whose sum is \(2^{d-1}-1\). The floor loss in
   \(L_0\) accounts for the factor \(4(d-1)\) in (5.2).

No finite or computational search, fractional-factor substitute, or web
input is used.

## 10. Exact implication scope

Unconditionally proved here:

1. the Boolean-Wick identity and exact corridor inverse (2.1)--(2.5);
2. overload equivalence and legal comparator-relative macro-drift
   (3.4)--(3.12);
3. complete scalar Bernoulli-polynomial classification (4.1)--(4.5);
4. cubic impossibility, exact quartic domination, and factorial blindness;
5. the fixed-degree bounded-slope no-go (5.2)--(5.3);
6. the quantitative polynomial-wall/spectral-kernel obstruction
   (6.9)--(6.12);
7. exact factorial switch formulas and antipodal even-Walsh structure
   (7.2)--(7.11); and
8. the intrinsic communicating-class drift obstruction (7.12)--(7.13).

Not proved:

1. \(\min_F\mathcal C_{H_A}(F)=o(W)\);
2. a bounded or \(o(B)\)-size improving macro-packet;
3. favorable strict transposition drift from every high-corridor factor;
4. a low minimum in every intrinsic switch class;
5. any growing-degree harmonic-kernel theorem beyond the stated
   \(\Xi(S)\) range;
6. MWB, labelled common-owner synchronization, or the contiguous-OR width
   conjecture.

The constructive nonlinear potential is therefore real, but its global
selection theorem remains exactly the old positive-fibre bottleneck.
