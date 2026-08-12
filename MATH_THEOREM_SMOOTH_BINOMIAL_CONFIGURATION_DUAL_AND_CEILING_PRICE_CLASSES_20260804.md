# Smooth binomial configuration dual: exact closure and Gaussian ceiling-price certificates

**Date:** 2026-08-04
**Status:** unconditional pure-mathematical reduction and positive price-class theorem.  The full configuration-dual inequality for every nonnegative price vector remains open.  This note proves the exact authoritative dual closure, identifies the signed Gaussian tail kernel, proves the globally concave subcase, and proves a strictly positive margin for every fixed reciprocal ceiling price.  Consequently any separator must be a genuinely nonconcave, non-fixed-reciprocal covering price.

## 0. Setup

Work in `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad W=C_r,\qquad
 t=r-d,\qquad H_s=C_s-C_{s-1},
\]

where `d=d(2r)` is the coefficient-one depth.  Thus

\[
 {d\over\sqrt r}\longrightarrow A:={\sqrt\pi\over2}.
\tag{0.1}
\]

The residual jobs of length `ell` and the sockets of capacity `u` have
multiplicities

\[
 n_\ell=H_{t-\ell},\qquad
 m_u=H_{t+u}+1\quad(1\le u\le d).
\tag{0.2}
\]

Deleting the empty set changes one job by one cell.  This is an `O(1)`
correction and is suppressed in the asymptotic statements below.

For a nonnegative socket price vector
`theta=(theta_1,...,theta_d)`, the physical configuration cost of a job is

\[
 \psi_\theta(\ell)=
 \min\left\{\sum_{u=1}^d\theta_up_u:
 p_u\in\mathbb Z_{\ge0},\quad
 \sum_{u=1}^d up_u\ge\ell\right\}.
\tag{0.3}
\]

The inequality is `>=`, not equality: a capacity-`u` socket can receive a
shorter chunk.  Equivalently one may trim the last selected capacity.
The configuration-dual gate is

\[
 \boxed{
 \sum_\ell n_\ell\psi_\theta(\ell)
 \le \sum_{u=1}^d m_u\theta_u
 \quad(\theta\ge0).
 }
\tag{0.4}
\]

## 1. Exact covering closure

### Lemma 1.1

For every `theta`, the function `psi_theta` is nonnegative,
nondecreasing, subadditive, and satisfies `psi_theta(0)=0`.  Replacing
`theta_u` by `psi_theta(u)` leaves `psi_theta` unchanged and can only
decrease the right side of (0.4).

Conversely, if a function `psi` on the nonnegative integers is
nonnegative, nondecreasing and subadditive, then, for every `ell<=d`, it
is the covering closure of its restriction `theta_u=psi(u)`.

#### Proof

Monotonicity follows because every cover of a larger integer covers a
smaller one.  Concatenating covers proves subadditivity.  A one-socket
cover gives `psi_theta(u)<=theta_u`; hence replacing `theta` by its closure
does not increase the supply price.  Idempotence follows by substituting
optimal covers into one another.

For the converse, every cover of `ell` has

\[
 \sum_i\psi(u_i)\ge\psi\!\left(\sum_i u_i\right)
 \ge\psi(\ell),
\]

while the one-part cover `u=ell` attains `psi(ell)`. \(\square\)

Thus the physical price class is a covering/subadditive closure.  If the
constraint in (0.3) were incorrectly replaced by equality, residue
oscillations such as a free even denomination and a costly odd
denomination would appear.  Those are not authoritative physical prices:
trimming restores monotonicity.

## 2. Exact signed-tail form

Put `Delta psi(q)=psi(q)-psi(q-1)`.  The job and socket tails telescope to

\[
 N_q:=\sum_{\ell\ge q}n_\ell=C_{t-q}+O(1),
\tag{2.1}
\]

and

\[
 M_q:=\sum_{u\ge q}m_u=
 \begin{cases}
 W-C_{t+q-1}+d-q+1,&1\le q\le d,\\
 0,&q>d.
 \end{cases}
\tag{2.2}
\]

Therefore summation by parts gives the exact residual form

\[
 \boxed{
 \sum_um_u\psi(u)-\sum_\ell n_\ell\psi(\ell)
 =\sum_{q\ge1}K_{r,q}\,\Delta\psi(q)+O(\psi(t)),
 }
\tag{2.3}
\]

where the final `O(psi(t))` is only the punctured-empty-chain convention,
and

\[
 K_{r,q}=M_q-N_q.
\tag{2.4}
\]

Without the puncture convention (2.3) is exact with no error.  Formula
(2.3) is the sharp remaining price problem: `Delta psi(q)>=0`, but it need
not decrease.

## 3. Gaussian kernel and its single crossing

The Gaussian row and socket measures are

\[
 d\nu(x)=2(A+x)e^{-(A+x)^2}\,dx\quad(x>0),
\]

and

\[
 d\mu(y)=2(A-y)e^{-(A-y)^2}\,dy\quad(0<y<A).
\]

Their signed tail kernel is

\[
 K(y)=
 \begin{cases}
 1-e^{-(A-y)^2}-e^{-(A+y)^2},&0\le y\le A,\\
 -e^{-(A+y)^2},&y>A.
 \end{cases}
\tag{3.1}
\]

It satisfies

\[
 \int_0^\infty K(y)\,dy=0.
\tag{3.2}
\]

Indeed (3.2) is exactly equality of total job and socket volume in the
coefficient-one scaling limit.

### Lemma 3.1 (one crossing)

There is a unique `y_* in (0,A)` such that `K>0` before `y_*` and `K<0`
after `y_*`.

#### Proof

On `[0,A]`, write

\[
 S(y)=e^{-(A-y)^2}+e^{-(A+y)^2}
 =2e^{-A^2-y^2}\cosh(2Ay).
\]

Then `K=1-S` and

\[
 {d\over dy}\log S(y)=2\bigl(A\tanh(2Ay)-y\bigr).
\]

The function in parentheses is strictly concave on `(0,infinity)`, has
derivative `2A^2-1=pi/2-1>0` at zero, and is negative at `A`.  Hence `S`
first increases and then decreases.  Also

\[
 S(0)=2e^{-\pi/4}<1,
 \qquad S(A)=1+e^{-\pi}>1.
\]

Thus `S` crosses one on its increasing branch and remains above one
through `A`.  Beyond `A`, (3.1) is strictly negative. \(\square\)

### Corollary 3.2 (globally concave price profiles pass)

Let `phi:[0,infinity)->[0,infinity)` be nondecreasing, concave, with
`phi(0)=0` and at most linear growth.  Then

\[
 \boxed{\int\phi\,d\nu\le\int\phi\,d\mu.}
\tag{3.3}
\]

#### Proof

Stieltjes layer cake gives

\[
 \int\phi\,d\mu-\int\phi\,d\nu
 =\int_0^\infty K(y)\,d\phi(y).
\]

The a.e. derivative of a concave `phi` is nonincreasing.  Subtract its
value at the crossing `y_*`: on the positive part of `K` the resulting
factor is nonnegative, and on the negative part both factors are
nonpositive.  The constant part integrates to zero by (3.2). \(\square\)

This corollary is a real certificate, but it does not close (0.4).  A
finite-capacity covering closure typically acquires renewal jumps at
multiples of the largest efficient denomination and need not be globally
concave.

## 4. Fixed reciprocal ceiling prices

For a fixed positive integer `q`, define the continuum ceiling price

\[
 \phi_q(x)=\left\lceil {qx\over A}\right\rceil
 \quad(x>0),\qquad \phi_q(0)=0.
\tag{4.1}
\]

It is the covering closure generated by price
`theta(y)=ceil(qy/A)` on capacities `0<y<=A`.

### Theorem 4.1 (strict ceiling margin)

For every fixed `q>=1`,

\[
 \boxed{
 \int\phi_q\,d\mu-\int\phi_q\,d\nu
 ={1\over2}-e^{-\pi/4}
 -2q\sum_{m\ge1}e^{-4\pi q^2m^2}>0.
 }
\tag{4.2}
\]

Consequently, if `a_r` is any integer with
`a_r/sqrt(r)->A/q` and the discrete price is

\[
 \psi_r(\ell)=\left\lceil {\ell\over a_r}\right\rceil,
\tag{4.3}
\]

then (0.4) holds with a positive `Theta_q(W)` margin for all sufficiently
large `r`.

#### Proof

For a nonnegative random variable `X`,

\[
 \mathbb E\left\lceil {X\over a}\right\rceil
 =\sum_{j\ge0}\Pr(X>ja).
\]

Take `a=A/q` and use the two tails in (3.1).  Since `A=qa`, direct
collection gives

\[
 D_q:=\int\phi_q\,d\mu-\int\phi_q\,d\nu
 =q-e^{-A^2}-\sum_{j\ge1}e^{-(ja)^2}.
\tag{4.4}
\]

Poisson summation for the Gaussian gives

\[
 a\sum_{j\ge1}e^{-(ja)^2}
 =A\left(1+2\sum_{m\ge1}e^{-\pi^2m^2/a^2}\right)-{a\over2}.
\]

Substitute `A/a=q` and `A^2=pi/4` to obtain (4.2).  Positivity follows,
for example, from

\[
 2q\sum_{m\ge1}e^{-4\pi q^2m^2}
 \le {2q e^{-4\pi q^2}\over1-e^{-12\pi q^2}}
 <{1\over2}-e^{-\pi/4}.
\]

Finally the local central-binomial limit and Gaussian tail domination
send the discrete normalized cost difference to `D_q`; the puncture and
rounding of `a_r` contribute `o(W)`. \(\square\)

The case `q=1` is the constant socket price: every job pays its minimum
number `ceil(ell/d)` of sockets.  Thus Theorem 4.1 recovers, and sharpens
to an explicit theta-function margin, the minimum-piece count inequality.

### Corollary 4.2

Every fixed nonnegative linear combination of

* the linear volume price `ell`, and
* the reciprocal ceiling prices `ceil(q ell/d)` for fixed `q`,

passes the asymptotic configuration dual.  The linear part has the exact
finite vacancy margin; every nonzero ceiling part has a linear-in-`W`
margin.

## 5. Exact surviving price frontier

The full inequality (0.4) is not proved here.  The remaining price class
is sharply localized:

1. equality-denomination residue oscillations are artifacts of replacing
   physical covering by exact summation and are excluded by Lemma 1.1;
2. every globally concave macroscopic profile passes by Corollary 3.2;
3. every fixed reciprocal ceiling/MIR renewal ray passes with strict margin
   by Theorem 4.1;
4. linear volume pricing passes exactly by the scalar ledger.

Thus any asymptotic separator must be a genuinely nonconcave covering
closure outside the conic classes proved above; it cannot be a fixed finite
combination of the standard linear and reciprocal ceiling rays.  The
present theorem does not decide whether such a separator could have one
fixed macroscopic mixed-denomination shape or would have to change its
renewal pattern with `r`.  Controlling or finding that remaining class is
the exact unresolved smooth-histogram configuration problem.

Even a complete proof of (0.4) would establish only a fractional
fragmentation of the actual binomial job histogram into the socket
histogram.  It would not by itself give an integral chain cutting, literal
containment between two SCDs, or the upper/residence/common-cap chronology.
