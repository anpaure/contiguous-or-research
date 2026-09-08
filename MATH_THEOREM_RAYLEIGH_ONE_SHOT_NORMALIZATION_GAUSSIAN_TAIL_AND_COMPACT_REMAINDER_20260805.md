# Rayleigh one-shot normalization, Gaussian-tail coagulation, and the compact remainder

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reduction.  One common-density cancellation,
one equal-level primary subtraction, and one further common-density
cancellation turn the Rayleigh pair into a strictly separated pair whose
socket density is positive at its upper endpoint and whose job density has
a Gaussian tail.  All sufficiently high job bands of that pair admit an
explicit equal-piece coagulation inside the socket bank.  The only
remaining continuum gate is therefore compactly supported.  No repeated
equal-level policy or compact completion is claimed.

## 1. The first transformed pair

Let `K` be the Rayleigh signed-tail kernel, let `b` be its unique zero and
`c` its unique minimum, and let

\[
 z(u)=r(u)-\ell(u),\qquad m<u<0,
\]

be the first equal-level remainder map.  Write `u(t)=z^{-1}(t)`.  The first
transformed job density is

\[
                         f_1(t)=u'(t)>0
 \qquad(t>0),                                      \tag{1.1}
\]

and its socket density is

\[
                         g_1(t)=-K'(t)>0
 \qquad(0<t<b).                                    \tag{1.2}
\]

The one-well regeneration theorem proves the strict overlap domination

\[
                         g_1(t)>f_1(t)
 \qquad(0<t<b).                                    \tag{1.3}
\]

Cancel `f_1(t)dt` as one-piece configurations throughout the overlap.  The
remaining pair is

\[
 \nu_2(dt)=g_2(t){\bf1}_{(0,b)}(t)dt,
 \qquad
 g_2(t)=-K'(t)-u'(t),                              \tag{1.4}
\]

and

\[
 \mu_2(dt)=f_2(t){\bf1}_{(b,\infty)}(t)dt,
 \qquad
 f_2(t)=u'(t).                                     \tag{1.5}
\]

They have equal first moments.  Their supports are strictly separated, and

\[
                         g_2(b-)>0.                \tag{1.6}
\]

Indeed, (1.6) is the endpoint form of the strict inequality (1.3):

\[
 g_2(b-)=-K'(b)-u'(b)>0.                           \tag{1.7}
\]

This is a one-shot normalization.  It must not be confused with applying
the equal-level rule a second time; that repeated policy has a separate
prefix-Hall obstruction.

## 2. A general terminal-density tail lemma

### Lemma 2.1 (Gaussian tail fits below a positive terminal socket density)

Let `C>0`.  Suppose a socket measure has density `g` on `(0,C)` and

\[
                         \liminf_{y\uparrow C}g(y)>0.          \tag{2.1}
\]

Suppose a job measure on `(C,infinity)` has density `f` satisfying, for
some constants `B,gamma>0` and finite `d`,

\[
                         f(x)\le B(1+x)^d e^{-\gamma x^2}
 \quad\text{for all sufficiently large }x.         \tag{2.2}
\]

For `n>=2`, split every job in `((n-1)C,nC)` into `n+1` equal pieces.
There is a finite `N_0` such that the aggregate piece-occurrence density of
all bands `n>=N_0` is pointwise at most `g`.

#### Proof

For one band the piece density is

\[
 (n+1)^2 f((n+1)y)
 {\bf1}_{((n-1)C/(n+1),\,nC/(n+1))}(y).            \tag{2.3}
\]

Put `delta=C-y`, `L=C/delta`, and `m=n+1`.  Exactly as in the Rayleigh
band calculation, an active term satisfies

\[
                         L<m<2L.                   \tag{2.4}
\]

It also satisfies

\[
                         my>(m-2)C.                \tag{2.5}
\]

For all large active `m`, (2.2) therefore bounds (2.3) by

\[
                         B_1 m^{d+2}e^{-\gamma_1m^2}            \tag{2.6}
\]

for constants `B_1,gamma_1>0` depending only on `B,gamma,d,C`.
Summing over the active integers gives

\[
 R_{\ge N}(y)
 \le B_2(1+L^{d+2})e^{-\gamma_1L^2/2}.             \tag{2.7}
\]

If any band `n>=N` is active, then

\[
                         \delta<{2C\over N+1}.     \tag{2.8}
\]

Thus for all large `N` its entire demand is supported in a terminal
neighborhood on which `g>=q>0` by (2.1), while the right side of (2.7)
tends uniformly to zero as `L> (N+1)/2` tends to infinity.  Choose `N_0`
so that (2.7) is below `q`.  Outside that terminal neighborhood the demand
is zero.  This proves pointwise domination. `square`

Every band kernel in the lemma is literal: a job `x` is replaced by
`n+1` copies of `x/(n+1)<C`.  Work is preserved band by band.

## 3. Gaussian tail of the transformed job

### Lemma 3.1

The density `f_2=u'` in (1.5) satisfies a Gaussian upper bound of the form
(2.2).

#### Proof

At `t=z(u)`, put

\[
 a=K'(r(u))>0,
 \qquad q=-K'(\ell(u))>0.
\]

Then

\[
                         u'(t)={aq\over a+q}\le a. \tag{3.1}
\]

For all large `t`, `r(u)>A`, so `a=j(r(u))`.  Also

\[
                         r(u)=t+\ell(u)>t,
\]

and the Rayleigh density `j` is decreasing.  Hence

\[
 u'(t)\le j(r(u))\le j(t)
 =2(A+t)e^{-(A+t)^2}le2(A+t)e^{-t^2}.             \tag{3.2}
\]

This is (2.2), for example with `d=1` and `gamma=1`. `square`

## 4. Compact-remainder theorem

### Theorem 4.1

The pair `(mu_2,nu_2)` in (1.4)--(1.5) has a finite threshold `N_0` such
that all jobs above `(N_0-1)b` possess an explicit exact equal-piece
coagulation using a submeasure of `nu_2`.

After removing those jobs and sockets, one obtains positive measures

\[
                         \mu_{\rm cmp},\nu_{\rm cmp}           \tag{4.1}
\]

with equal first moments and supports

\[
 \operatorname {supp}\mu_{\rm cmp}
 \subseteq[b,(N_0-1)b],
 \qquad
 \operatorname {supp}\nu_{\rm cmp}
 \subseteq[0,b].                                   \tag{4.2}
\]

Any finite coagulation of this compact pair lifts, by reattaching the
cancelled one-piece sockets and the first equal-level primary socket, to a
finite coagulation of the original Rayleigh job/socket measures.

#### Proof

Equation (1.7) gives the terminal-density hypothesis (2.1) with `C=b`, and
Lemma 3.1 gives the Gaussian-tail hypothesis.  Lemma 2.1 therefore supplies
the pointwise dominated equal-piece tail kernel.  Removing its job and
socket marginals preserves positivity.  Equal splitting preserves work
band by band, so the remaining first moments agree and (4.2) holds.

A coagulation of the compact remainder, combined with the explicit tail
kernel, coagulates `(mu_2,nu_2)`.  Add back the transformed common
one-piece density.  Then append the first equal-level socket to each first
transformed job, as in the primary lifting theorem, and finally restore the
original common one-piece density.  Every operation adds only finitely many
pieces, so the final configurations are finite. `square`

## 5. Exact frontier

The anonymous continuum problem no longer needs an unbounded-state
construction.  It is enough to coagulate the one compact pair (4.1).
Equivalently, one may solve its closed configuration-price inequalities or
its uniform-layer packet transport.

This is not yet automatic.  Equal work, strict count slack, compact support,
and atomless densities do not imply configuration feasibility for arbitrary
measures.  The remaining Rayleigh-specific theorem is a compact packet
coupling, not another tail estimate and not an iteration of the equal-level
policy.

