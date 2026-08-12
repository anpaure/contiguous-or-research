# Inverse-circle closure of the cyclic Apéry variance conjecture

**Date:** 2026-08-05  
**Method:** pure mathematics; generalized inverses, connected-circle
sumset growth, and continuous quantile majorization; no computation,
search, or solver  
**Status:** unconditional.  Every nonnegative cyclically subadditive
Apéry defect satisfies the scale-sharp variance inequality.  Consequently
the complete formal Rayleigh phase is strictly positive at every residue
period covered by the all-period Fourier coefficient theorem.  Finite
availability shoulders remain separate.

## 1. Statement

Let

\[
 e:\mathbb Z/g\mathbb Z\longrightarrow[0,\infty),
 \qquad e(0)=0,
\]

be subadditive:

\[
 e(x+y)\le e(x)+e(y).
\tag{1.1}
\]

Put

\[
 c=e(1),\qquad
 \mu={1\over g}\sum_{r=0}^{g-1}e(r).
\]

### Theorem 1.1 (scale-sharp cyclic variance theorem)

For every such profile,

\[
 \boxed{
 \operatorname {Var}(e)
 \le {\mu(\mu+c)\over3}.}
\tag{1.2}
\]

In the physical normalization `c<=1`, this implies

\[
 \boxed{
 \operatorname {Var}(e)
 \le {\mu(\mu+1)\over3}.}
\tag{1.3}
\]

The proof converts the finite cyclic profile into a subadditive function
on the connected circle.  Connected-circle sumsets have no positive
Haar-measure stabilizer loss, so the composite-period Kneser obstruction
disappears.

## 2. Unit-generator normalization

If `c=0`, repeated use of (1.1) gives

\[
 e(r)\le r e(1)=0
 \qquad(0\le r<g),
\]

and hence `e=0`; (1.2) is immediate.

Assume `c>0` and replace `e` by `e/c`.  It is therefore enough to prove
the theorem under

\[
 \boxed{e(1)=1.}
\tag{2.1}
\]

Then

\[
 0\le e(r)\le r
 \qquad(0\le r<g).
\tag{2.2}
\]

At the end, multiplying the normalized inequality by `c^2` gives (1.2).

## 3. The superadditive lift and its inverse

Use the representative `0<=r<g` and define, for every integer
`n=qg+r`,

\[
 A(n)=qg+r-e(r)=n-e(r).
\tag{3.1}
\]

Thus

\[
 A(n+g)=A(n)+g.
\tag{3.2}
\]

### Lemma 3.1 (lift properties)

The function `A:Z->R` is nondecreasing and superadditive, and satisfies

\[
 A(n)\le n.
\tag{3.3}
\]

#### Proof

Equation (3.3) is just nonnegativity of `e`.  Away from a period seam,

\[
 A(n+1)-A(n)
 =1-e(r+1)+e(r)\ge0
\]

by `e(r+1)<=e(r)+e(1)`.  At a seam the increment is
`1+e(g-1)>=0`.  Hence `A` is nondecreasing.

For arbitrary integers `m,n`, cyclic subadditivity gives

\[
\begin{aligned}
 A(m+n)
 &=m+n-e(\overline m+\overline n)\\
 &\ge m+n-e(\overline m)-e(\overline n)\\
 &=A(m)+A(n),
\end{aligned}
\]

where bars denote residues modulo `g`.  Thus `A` is superadditive.
\(\square\)

Define the left generalized inverse

\[
 B(t)=\min\{n\in\mathbb Z:A(n)\ge t\}
 \qquad(t\in\mathbb R).
\tag{3.4}
\]

The minimum exists because `A(n)-n` is bounded and `A(n)` tends to
\(\pm\infty\) with `n`.

### Lemma 3.2 (inverse lift)

The inverse `B` is nondecreasing, satisfies

\[
 B(t+g)=B(t)+g,
\tag{3.5}
\]

and is subadditive:

\[
 \boxed{B(s+t)\le B(s)+B(t).}
\tag{3.6}
\]

Moreover `B(t)>=t`.

#### Proof

Monotonicity is immediate from (3.4), and (3.5) follows from (3.2).
By definition,

\[
 A(B(s))\ge s,
 \qquad
 A(B(t))\ge t.
\]

Superadditivity of `A` gives

\[
 A(B(s)+B(t))\ge s+t,
\]

so the least integer whose `A`-value reaches `s+t` is at most
`B(s)+B(t)`.  This is (3.6).

Finally, if an integer `n<t`, then (3.3) gives `A(n)<=n<t`; such an `n`
cannot occur in the defining set (3.4).  Therefore `B(t)>=t`.
\(\square\)

Put

\[
 u(t)=B(t)-t.
\tag{3.7}
\]

Lemmas 3.1--3.2 give

\[
 \boxed{
 u(t)\ge0,
 \qquad u(t+g)=u(t),
 \qquad u(s+t)\le u(s)+u(t).}
\tag{3.8}
\]

Thus `u` is a nonnegative measurable subadditive function on the connected
circle `R/gZ`.  Notice that no primality, true-period, or zero-subgroup
assumption has entered.

## 4. The inverse is exactly the phase discrepancy

For `0<=r<=g`, put

\[
 a_r=r-e(r),
\]

where `e(g)=e(0)=0`; hence `a_0=0` and `a_g=g`.  Lemma 3.1 says

\[
 0=a_0\le a_1\le\cdots\le a_g=g.
\tag{4.1}
\]

For almost every `t` in the phase interval

\[
 a_r<t<a_{r+1},
\]

the first integer at which `A` reaches `t` is `r+1`.  Therefore

\[
 \boxed{u(t)=r+1-t.}
\tag{4.2}
\]

Repeated phase points merely make an interval empty.  Values at the
finitely many endpoints do not affect any Haar integral.  Formula (4.2)
is exactly the normalized complete-phase discrepancy from the Apéry phase
moment theorem.

Let expectation on the left below mean normalized Lebesgue measure on one
circle period, and let expectation on `e` mean the uniform residue law.
Integrating (4.2) gives

\[
\begin{aligned}
 \mathbb Eu
 &={1\over2g}\sum_{r=0}^{g-1}
 \bigl((1+e_r)^2-e_{r+1}^2\bigr)\\
 &=\boxed{{1\over2}+\mu},
\end{aligned}
\tag{4.3}
\]

and

\[
\begin{aligned}
 \mathbb Eu^2
 &={1\over3g}\sum_{r=0}^{g-1}
 \bigl((1+e_r)^3-e_{r+1}^3\bigr)\\
 &={1\over3}+\mu+\mathbb Ee^2.
\end{aligned}
\tag{4.4}
\]

The cyclic powers telescope.  Subtracting the square of (4.3) yields

\[
 \boxed{
 \operatorname {Var}(u)
 ={1\over12}+\operatorname {Var}(e).}
\tag{4.5}
\]

The lattice correction `+1` in the finite variance conjecture has now
become the exact variance `1/12` of the unit inverse sawtooth.

## 5. A connected-circle quantile theorem

We isolate the continuous statement used below.

### Theorem 5.1 (subadditive circle variance)

Let `v` be a nonnegative measurable subadditive function on a connected
circle, and suppose `v` has finite second moment.  Then

\[
 \boxed{
 \operatorname {Var}(v)
 \le { (\mathbb Ev)^2\over3}.}
\tag{5.1}
\]

#### Proof

For `z>=0`, let

\[
 C_z=\{x:v(x)\le z\}.
\]

Subadditivity gives

\[
 C_s+C_t\subseteq C_{s+t}.
\tag{5.2}
\]

Normalized Haar measure on a connected circle obeys the one-dimensional
connected Kneser inequality

\[
 m(E+F)\ge\min\{1,m(E)+m(F)\}.
\tag{5.3}
\]

For completeness, (5.3) is the compact-group Kneser theorem: if `E+F`
is not the whole circle, its stabilizer is a proper closed subgroup of a
circle, hence finite and of Haar measure zero.  Approximation by compact
subsets gives the measurable version.  In the present application all
sublevel sets are finite unions of intervals, so no measurability
qualification is needed.

Let \(q:[0,1]\to[0,\infty]\) be the increasing quantile of `v`.  From
(5.2)--(5.3), with an arbitrarily small enlargement of the two levels to
remove endpoint conventions,

\[
 \boxed{
 q(x+y)\le q(x)+q(y)
 \qquad(x,y\ge0,\ x+y\le1).}
\tag{5.4}

Put

\[
 S(x)=\int_0^xq(t)\,dt.
\]

For `0<x<1`, apply (5.4) to the decomposition
`x=y+(x-y)` and integrate with `y` from `0` to `x`:

\[
 xq(x)\le2S(x).
\tag{5.5}
\]

Consequently

\[
 {d\over dx}{S(x)\over x^2}
 ={xq(x)-2S(x)\over x^3}\le0
\]

for almost every `x`.  If \(m=\mathbb Ev=S(1)\), then

\[
 \boxed{S(x)\ge m x^2.}
\tag{5.6}
\]

The increasing linear function

\[
 \ell(x)=2mx
\]

has the same total integral as `q`, and its prefix integral is exactly
`mx^2`.  Hence (5.6) says that `q` is majorized by `ell`.

Here is a direct square-moment verification, avoiding any convention about
the word “majorized.”  Put

\[
 H(x)=\int_0^x(q(t)-\ell(t))\,dt.
\]

Then `H>=0`, `H(0)=H(1)=0`, and `q+ell` is nondecreasing.  Stieltjes
integration by parts gives

\[
\begin{aligned}
 \int_0^1(q^2-\ell^2)
 &=\int_0^1(q-\ell)(q+\ell)\\
 &=-\int_{[0,1]}H\,d(q+\ell)\le0.
\end{aligned}
\]

Therefore

\[
 \mathbb Ev^2=\int_0^1q^2
 \le\int_0^1(2mx)^2dx={4m^2\over3}.
\]

Subtracting `m^2` proves (5.1).  \(\square\)

In the inverse-circle application, `u` is bounded because it is periodic
and piecewise affine with finitely many jumps, so all displayed Stieltjes
integrals are finite.  For the abstract formulation of Theorem 5.1, the
same calculation may equivalently be applied first to bounded quantile
truncations and then passed to the limit by monotone convergence.

## 6. Completion of the finite cyclic theorem

Apply Theorem 5.1 to the inverse-circle profile `u`.  Equations
(4.3)--(4.5) give

\[
 {1\over12}+\operatorname {Var}(e)
 =\operatorname {Var}(u)
 \le {({1\over2}+\mu)^2\over3}
 ={1\over12}+{\mu(\mu+1)\over3}.
\]

Cancel `1/12`:

\[
 \boxed{
 \operatorname {Var}(e)
 \le {\mu(\mu+1)\over3}}
\tag{6.1}
\]

under the normalization `e(1)=1`.

For the original profile with `c=e(1)>0`, apply (6.1) to `e/c` and
multiply by `c^2`:

\[
 \operatorname {Var}(e)
 \le c^2{(\mu/c)(\mu/c+1)\over3}
 ={\mu(\mu+c)\over3}.
\]

Together with the zero case from Section 2, this proves Theorem 1.1.

## 7. Rayleigh consequence and exact scope

The general Apéry phase-moment/Fourier theorem gives the strict lower
bound

\[
 \Phi(U)
 >M\left(
 {1\over2}+\mu
 -\sqrt{{1\over4}+3\operatorname {Var}(e)}
 \right).
\]

Theorem 1.1 and `c<=1` imply

\[
 {1\over4}+3\operatorname {Var}(e)
 \le\left({1\over2}+\mu\right)^2.
\]

The coefficient estimate in the cited Fourier theorem is strict, so the
complete formal phase is strictly positive even in the equality case.
Thus prime periods, composite periods, nontrivial Kneser stabilizers, and
correlated coset residuals are all closed at the formal periodic level.

This theorem does **not** address the finite availability shoulder.  That
queue is nonperiodic and is outside the inverse-circle moment identity.

## 8. Dependencies

1. the connected compact-group Kneser inequality on the circle;
2. `MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md` for the downstream Fourier consequence (the moment identities
   themselves were reproved in Section 4);
3. `MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_ALL_APERY_PERIOD_FOURIER_POSITIVITY_20260805.md` for the strict all-period coefficient estimate.
