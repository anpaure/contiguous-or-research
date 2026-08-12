# Centered child profiles: the post-collar constant mode is parent-determined

Date: 2026-07-27

## 0. Exact algebraic result

Let \({\cal H}_t\) be any current induced \(r\)-uniform catalogue, let
\(S\) be an active physical profile of size \(k<r\), and write
\(d_t(S)\) for its current codegree.  Then

\[
\boxed{
 \sum_{a\notin S}d_t(S\cup\{a\})=(r-k)d_t(S).}
\tag{0.1}
\]

The sum includes inactive resources with codegree zero.  The same identity
holds at time zero.

Put

\[
 p_{S,a}=\frac{d_0(S\cup\{a\})}{(r-k)d_0(S)},
 \qquad \sum_ap_{S,a}=1,
\tag{0.2}
\]

and use the natural survival-normalized link ratios

\[
 X_S(t)=\frac{d_t(S)}{d_0(S)u_t^{r-k}},
 \qquad
 X_{S,a}(t)=
 \frac{d_t(S\cup\{a\})}
      {d_0(S\cup\{a\})u_t^{r-k-1}}.
\tag{0.3}
\]

Then

\[
\boxed{
 \sum_ap_{S,a}X_{S,a}(t)=u_tX_S(t).}
\tag{0.4}
\]

Thus the constant child mode which has aggregate \(\ell^1\)-kernel one is
known exactly from the parent.  It is not an independent profile boundary.

Define the centered child variance

\[
 V_S(t)=
 \sum_ap_{S,a}\bigl(X_{S,a}(t)-u_tX_S(t)\bigr)^2.
\tag{0.5}
\]

Equivalently,

\[
\boxed{
 V_S=\sum_ap_{S,a}X_{S,a}^2-u_t^2X_S^2.}
\tag{0.6}
\]

This note proves only these identities and the covariance spectrum below.
It does not yet prove a stopped supermartingale estimate for \(V_S\).

## 1. Proof of the incidence identity

Every current catalogue edge containing \(S\) has exactly \(r-k\)
resources outside \(S\).  In the left side of (0.1), that edge is counted
once for each of those resources.  This proves (0.1).  Applying it at time
zero proves that the coefficients in (0.2) sum to one.  Substitute (0.3)
into the left side of (0.4), use (0.1), and cancel \((r-k)d_0(S)\); the
remaining power of \(u_t\) is exactly one.  Expanding the square in (0.5)
and using (0.4) proves (0.6).

No independence, pseudorandomness, or catalogue-specific geometry enters.

## 2. The categorical covariance operator

For a probability vector \(p=(p_a)\), let

\[
 C_p=\operatorname{diag}(p)-pp^{\mathsf T}.
\tag{2.1}
\]

Then

\[
 x^{\mathsf T}C_px
 =\sum_ap_ax_a^2-\left(\sum_ap_ax_a\right)^2
 =\operatorname{Var}_p(x_a).
\tag{2.2}
\]

Consequently

\[
 C_p\succeq0,
 \qquad C_p{\bf1}=0,
 \qquad
 \boxed{\|C_p\|_{2\to2}\le\max_ap_a.}
\tag{2.3}
\]

The last inequality follows by dropping the nonnegative square in (2.2):

\[
 x^{\mathsf T}C_px\le\sum_ap_ax_a^2
 \le(\max_ap_a)\|x\|_2^2.
\]

If there are \(b\) equiprobable children, then

\[
 C_p=\frac1bI-\frac1{b^2}J,
\tag{2.4}
\]

so its spectrum is \(0\) on constants and \(1/b\) with multiplicity
\(b-1\).

## 3. Exact regular-block plus gap spectrum

The post-collar consecutive spine has \(b=m-k\) regular continuations and
one omitted/gap sector.  Write their probability weights as

\[
 p_1=\cdots=p_b=a=\frac\alpha b,
 \qquad p_\star=\beta,
 \qquad \alpha+\beta=1.
\tag{3.1}
\]

On the \((b-1)\)-dimensional regular-block subspace orthogonal to constants,
\(C_p\) has eigenvalue \(a\).  On the span of the normalized regular constant
and the gap coordinate its matrix is

\[
 a\beta
 \begin{pmatrix}
 1&-\sqrt b\\
 -\sqrt b&b
 \end{pmatrix},
\tag{3.2}
\]

with eigenvalues

\[
 0,qquad a\beta(b+1).
\tag{3.3}
\]

For the exact spine ratios,

\[
 \alpha=1-\frac1{r-k},
 \qquad
 \beta=\frac1{r-k},
 \qquad
 a=\frac1b\left(1-\frac1{r-k}\right).
\tag{3.4}
\]

Hence, for \(b\ge2\),

\[
\boxed{
 \|C_p\|_{2\to2}
 =\max\{a,a\beta(b+1)\}
 =O(1/b).}
\tag{3.5}
\]

The scalar \(\ell^1\) child kernel is \(\alpha=1-o(1)\), but after the
parent-determined constant mode is removed, the Hilbert kernel is
\(O(1/(m-k))\).

## 4. Exact remaining dynamic question

To turn (3.5) into the missing stopped theorem one must prove that, after
the physical-union compensation and equality resolution, the predictable
jump covariance of the centered vector

\[
 \bigl(X_{S,a}-uX_S\bigr)_a
\]

is governed by \(C_p\), without a new coherent error of order one.  A child
profile crossing while the parent remains below threshold then has weighted
cost in \(V_S\), and the \(O(1/(m-k))\) spectrum is the contraction which the
positive scalar energy lacks.

This is the precise Hilbert-space gate.  The identities (0.1)--(0.6) show
that any remaining order-one mode must come from the compensated jump
geometry, not from static child mass.
