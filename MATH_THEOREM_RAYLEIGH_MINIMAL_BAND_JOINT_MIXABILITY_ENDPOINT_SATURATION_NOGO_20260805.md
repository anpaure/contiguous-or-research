# Rayleigh residual coagulation: minimal-band joint-mixability endpoint saturation

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional scoped no-go and exact extra-piece support reduction.
The natural application of the Wang--Wang monotone-density joint-mixability
theorem to the separated Rayleigh residual pair fails on every sufficiently
high minimum-piece band.  The failure is not a mean mismatch: the
Wang--Wang support inequality forces every socket marginal to reach the
physical endpoint, while the residual socket density vanishes there.  One
additional socket per job removes this support obstruction exactly.  The
result does not disprove the residual coagulation or construct the required
extra-piece marginal decomposition.

## 1. The separated residual pair

Put

\[
 A={\sqrt\pi\over2},\qquad p=e^{-A^2},
\]

and

\[
 j(x)=2(A+x)e^{-(A+x)^2},\qquad
 s(y)=2(A-y)e^{-(A-y)^2}.
\]

Let `c in (0,A)` be the unique positive crossing `j(c)=s(c)`.  After
matching the common density as one-piece jobs, the remaining socket and job
measures are

\[
 \nu_{\rm res}(dy)=(s(y)-j(y)){\bf1}_{(0,c)}(y)\,dy,
\tag{1.1}
\]

and

\[
 \mu_{\rm res}(dx)
 =(j(x)-s(x)){\bf1}_{(c,A)}(x)\,dx
  +j(x){\bf1}_{[A,\infty)}(x)\,dx.
\tag{1.2}
\]

The crossing has the form `c=A theta`, where

\[
 {\operatorname {arctanh}\theta\over\theta}={\pi\over2}.
\tag{1.3}
\]

In particular `theta>1/2`.  Indeed,

\[
 {\operatorname {arctanh}(1/2)\over1/2}=\log 3<{\pi\over2};
\]

the left side of (1.3) is strictly increasing.  Hence

\[
                         2c>A.                    \tag{1.4}
\]

For every integer `n>=3`, define the minimum-piece band

\[
 I_n=((n-1)c,nc),\qquad
 w_n=\mu_{\rm res}(I_n)=\int_{(n-1)c}^{nc}j(x)\,dx>0.
\tag{1.5}
\]

By (1.4), `I_n` lies above `A`.  Its normalized job density is therefore
strictly decreasing on its full support:

\[
 f_n(x)={j(x){\bf1}_{I_n}(x)\over w_n}.
\tag{1.6}
\]

Every `x in I_n` needs at least `n` residual sockets because each socket is
strictly smaller than `c`.

## 2. The Wang--Wang support row on one band

The monotone-density joint-mixability theorem says that distributions with
monotone densities in one common direction on bounded supports are jointly
mixable whenever their mean/support inequality holds.  For distributions
with supports `[a_i,b_i]`, lengths `l_i=b_i-a_i`, and finite means `m_i`,
that inequality is

\[
 \sum_i a_i+\max_i l_i
 \le \sum_i m_i
 \le \sum_i b_i-\max_i l_i.
\tag{2.1}
\]

Apply it to

\[
                       (Y_1,\ldots,Y_m,-X_n),       \tag{2.2}
\]

where `X_n` has density (1.6), each socket `Y_i` is supported on
`[a_i,b_i] subseteq [0,c]`, and the desired center is zero.  Since `f_n` is
decreasing, the density of `-X_n` is increasing.  Thus the increasing form
of the Wang--Wang theorem requires the socket densities to be increasing
as well.

The support of `-X_n` is

\[
                       [-nc,-(n-1)c]               \tag{2.3}
\]

and has length `c`.  Every socket support has length at most `c`, so the
maximum length in (2.1) is exactly `c`.  Since the joint center is zero,
(2.1) becomes

\[
 \boxed{
    \sum_{i=1}^m a_i\le(n-1)c,
    \qquad
    \sum_{i=1}^m b_i\ge nc.}
\tag{2.4}
\]

The remaining scalar condition is the necessary mean identity

\[
                         \sum_i \mathbb E Y_i
                         =\mathbb E X_n.            \tag{2.5}
\]

Thus (2.4)--(2.5) are the exact Wang--Wang rows for this band.

## 3. Exact-`n` endpoint saturation

### Theorem 3.1 (minimal-band Wang--Wang no-go)

There do not exist, for every `n>=3`, `n` increasing-density socket
probability laws `G_(n,1),...,G_(n,n)` on subintervals of `[0,c]` such
that

1. `(G_(n,1),...,G_(n,n),-F_n)` is certified jointly mixable by the
   Wang--Wang monotone-density theorem; and
2. the positive-mass socket occurrence measure

   \[
       w_n\sum_{i=1}^n G_{n,i}                     \tag{3.1}
   \]

   is dominated by `nu_res`.

Consequently the standard decomposition which assigns the whole
minimum-piece band `I_n` to exactly `n` monotone socket roles cannot be a
coagulation of the separated Rayleigh pair.

#### Proof

With `m=n`, the second inequality in (2.4) says

\[
                         \sum_{i=1}^n b_i\ge nc.
\]

But every `b_i<=c`.  Hence

\[
                         b_1=\cdots=b_n=c.          \tag{3.2}
\]

We use the following elementary terminal-mass fact.  If `G` is a
probability law with a nondecreasing density on `[a,c]`, then, for every
`0<epsilon<c`,

\[
                         G((c-\epsilon,c))
                         \ge {\epsilon\over c}.     \tag{3.3}
\]

If `a>=c-epsilon`, the left side is one.  Otherwise, monotonicity says that
the average density on the final interval is at least the average density
on `[a,c]`; hence it is at least `1/(c-a)>=1/c`, proving (3.3).

Equations (3.1)--(3.3) force

\[
 \nu_{\rm res}((c-\epsilon,c))
 \ge {n w_n\over c}\epsilon.                      \tag{3.4}
\]

On the other hand, the density `s-j` is continuous at `c` and vanishes
there.  Therefore

\[
 \nu_{\rm res}((c-\epsilon,c))=o(\epsilon)
 \qquad(\epsilon\downarrow0),                      \tag{3.5}
\]

contradicting (3.4), because `w_n>0`.  This proves the theorem. `square`

### Remark 3.2 (the physical boundary version)

The same endpoint pressure is visible without mixability theory.  A job
`x>nc-epsilon` represented by exactly `n` sockets below `c` must use all
`n` sockets in `(c-epsilon,c)`.  Thus the linear job mass at the top of a
band competes with only `o(epsilon)` socket mass at the physical endpoint.
Theorem 3.1 is stronger for the proposed bandwise Wang--Wang construction:
its support row forces endpoint saturation for the entire normalized band,
not merely for a shrinking top slice.

## 4. One extra socket removes the support obstruction

### Proposition 4.1 (exact `n+1` support rows)

For a decreasing job law on `I_n` and `m=n+1` increasing socket marginals
on supports `[a_i,b_i] subseteq[0,c]`, the Wang--Wang mean/support
condition is exactly

\[
 \boxed{
   \sum_{i=1}^{n+1}a_i\le(n-1)c,
   \qquad
   \sum_{i=1}^{n+1}b_i\ge nc,
   \qquad
   \sum_{i=1}^{n+1}\mathbb EY_i=\mathbb EX_n.}
\tag{4.1}
\]

In endpoint-deficit form, its nontrivial support row is

\[
                 \boxed{
                 \sum_{i=1}^{n+1}(c-b_i)\le c.}
\tag{4.2}
\]

These rows are nonempty for every `n>=3`.

#### Proof

The derivation of (4.1) is exactly (2.4)--(2.5), now with `m=n+1`.
Equation (4.2) is its upper-support inequality rewritten.

For nonemptiness, put

\[
                         \beta_n={nc\over n+1}
\tag{4.3}
\]

and take all supports `[0,beta_n]`.  Both support inequalities hold, the
upper one with equality.  A nondecreasing probability density on
`[0,beta_n]` can have any mean in `[beta_n/2,beta_n)`; uniforms give the
left endpoint and elementary increasing beta densities approach the right
endpoint.

Because `f_n` is strictly decreasing on an interval of length `c`,

\[
 (n-1)c<\mathbb EX_n<\left(n-{1\over2}\right)c.
\tag{4.4}
\]

For `n>=2`,

\[
 {\beta_n\over2}
 ={nc\over2(n+1)}
 <{\mathbb EX_n\over n+1}
 <{(n-1/2)c\over n+1}
 <\beta_n.                                         \tag{4.5}
\]

Choose all `n+1` socket laws to have the middle mean in (4.5).  This
satisfies (4.1), proving support/mean feasibility. `square`

The proposition is deliberately only a local feasibility result.  To
construct a residual coagulation, the socket role laws for all bands must
also satisfy the barycentric identity

\[
 \sum_{n\ge3}w_n\sum_{i=1}^{n+1}G_{n,i}
 +\text{(the roles assigned to the remaining job bank)}
 =\nu_{\rm res}.                                   \tag{4.6}
\]

No theorem above proves (4.6).

## 5. Exact scope

The result proves:

1. the normalized high residual bands are legitimate decreasing-density
   Wang--Wang marginals;
2. exact minimum-piece banding forces every increasing socket role to the
   vanishing endpoint and is impossible;
3. one extra role changes that rigid equality to the finite deficit budget
   (4.2), and every individual band then passes the support and mean tests.

It does **not** prove that every job requires an extra piece, that the
global cardinality slack is insufficient, or that no finer subdivision of
the job bands can work.  In fact all one-denomination ceiling prices for
the full Rayleigh pair are already known to pass strictly.  The unresolved
extra-piece route is exactly the measure-valued decomposition (4.6), plus
the separate low residual band `(c,2c)` where the density changes
monotonicity at `A`.

The primary external input is Bin Wang and Ruodu Wang, *Joint Mixability*,
Mathematics of Operations Research 41 (2016), Theorem 3.2; its displayed
mean inequality is also necessary for every joint mix.

