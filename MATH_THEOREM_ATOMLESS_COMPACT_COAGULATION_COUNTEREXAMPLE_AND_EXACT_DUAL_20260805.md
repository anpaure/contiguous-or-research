# Atomless compact coagulation: a strict-window counterexample and the exact dual criterion

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or search  
**Status:** unconditional.  Compact support, atomlessness, a strictly positive
continuous socket density, equality of work, and even the strict two-to-three
count window do **not** imply finite coagulation.  The exact missing hypotheses
are the configuration-price inequalities below.  For a socket support bounded
away from zero, the same criterion is a compact finite-arity transport dual.

## 1. Finite coagulations

Fix `0<b<L<infinity`.  Let `mu` be a finite measure on `[b,L]` and let
`nu` be a finite measure on `(0,b)`.  A finite coagulation is a finite positive
measure `rho` on

\[
 \mathcal C_0=
 \bigsqcup_{n\ge1}
 \{(x;y_1,\ldots,y_n):x\in[b,L],\ 0<y_i<b,
                         \ \sum_i y_i=x\}/\mathfrak S_n                 \tag{1.1}
\]

whose job marginal is `mu` and whose aggregate occurrence marginal is `nu`.
Thus

\[
 (x)_\#\rho=\mu,
 \qquad
 \int\sum_i\mathbf1_{\{y_i\in E\}}\,d\rho=\nu(E).                    \tag{1.2}
\]

The adjective finite refers to the number of sockets in almost every job
configuration.  Since its expectation is `nu(0,b)<infinity`, this is automatic
once (1.2) holds.

## 2. Two universal necessary cuts

Every coagulation satisfies

\[
 \boxed{
 \nu(0,b)\ge
 \int_{[b,L]}\left(\left\lfloor{x\over b}\right\rfloor+1\right)d\mu(x).}
                                                                         \tag{2.1}
\]

Indeed, `n` pieces strictly below `b` have sum strictly below `nb`, so a job
of size `x` needs more than `x/b` pieces.

There is also a continuum of upper-tail capacity cuts.  For every `0<t<b`,

\[
 \boxed{
 \nu((t,b))\le
 \int_{[b,L]}\left(\left\lceil{x\over t}\right\rceil-1\right)d\mu(x).}
                                                                         \tag{2.2}
\]

If a configuration contains `k` pieces strictly larger than `t`, then
`kt<x`; hence `k<=ceil(x/t)-1`.  Integration proves (2.2).  Atomlessness
makes the choice of open or closed threshold immaterial in the applications
below.

These cuts already show why total count and total work cannot characterize
coagulation.

## 3. A continuous strict-window counterexample

Set

\[
 b=1,
 \qquad L={51\over50},
 \qquad
 d\mu(x)=50\,\mathbf1_{[1,51/50]}(x)\,dx.                              \tag{3.1}
\]

Thus

\[
 \mu([1,51/50])=1,
 \qquad
 \int x\,d\mu(x)={101\over100}.                                      \tag{3.2}
\]

On `(0,1)`, define the continuous strictly positive density

\[
 g(y)={1\over10}
      +{43\over45}\,19y^{18}
      +{47\over45}\,19(1-y)^{18},
 \qquad d\nu(y)=g(y)\,dy.                                             \tag{3.3}
\]

The two beta densities in (3.3) have respective means `19/20` and `1/20`.
Consequently

\[
 \nu(0,1)={1\over10}+{43\over45}+{47\over45}
          ={21\over10},                                               \tag{3.4}
\]

and

\[
 \int_0^1y\,d\nu(y)
 ={1\over20}+{43\over45}{19\over20}
              +{47\over45}{1\over20}
 ={101\over100}.                                                       \tag{3.5}
\]

Thus the work is exactly balanced and the count ratio lies strictly in the
Rayleigh residual window

\[
        2\mu([1,51/50])<\nu(0,1)<3\mu([1,51/50]).                     \tag{3.6}
\]

Nevertheless no coagulation exists.  Put `t=51/100`.  Since
`(51/100)^19<1/1000`, (3.3) gives

\[
\begin{aligned}
 \nu((t,1))
 &={1\over10}(1-t)
   +{43\over45}(1-t^{19})
   +{47\over45}(1-t)^{19}\\
 &>{49\over1000}+{43\over45}{999\over1000}
   ={45162\over45000}>1.                                             \tag{3.7}
\end{aligned}
\]

But two sockets larger than `51/100` have sum strictly larger than
`51/50`, whereas every job is at most `51/50`.  Hence every job can contain
at most one such socket, and (2.2) gives

\[
                  \nu((51/100,1))\le\mu([1,51/50])=1,                 \tag{3.8}
\]

contradicting (3.7).

The same obstruction has an explicit continuous covering-price witness.
By continuity of the tail in (3.7), choose

\[
              {51\over100}<s<1
              \quad\text{with}\quad \nu((s,1))>1.                     \tag{3.9}
\]

Choose a continuous function \(w:(0,1)\to[0,1]\) which vanishes on
\((0,s]\), equals one above \(s+\varepsilon\), and has
\(\int w\,d\nu>1\); this is possible for sufficiently small positive
\(\varepsilon\).  Put \(L=51/50\), and choose

\[
 C\ge\max\left\{{1\over s},{1\over2s-L}\right\},
 \qquad
                         a(y)=Cy-w(y).                              \tag{3.10}
\]

Then \(a\) is continuous and nonnegative.  In any cover of a job \(x\le L\),
let \(k\) be the number of pieces on which \(w\) is positive.  If \(k\le1\),

\[
                         \sum_i a(y_i)\ge Cx-1.                       \tag{3.11}
\]

If \(k\ge2\), those \(k\) pieces are all larger than \(s\), and

\[
\begin{aligned}
 \sum_i a(y_i)-(Cx-1)
 &\ge C(ks-x)-k+1\\
 &\ge C(ks-L)-k+1\ge0.                                                \tag{3.12}
\end{aligned}
\]

The final expression is increasing in \(k\) because \(Cs\ge1\), and at
\(k=2\) it is nonnegative by (3.10).  Hence \(a^\star(x)\ge Cx-1\) on
the whole job support.  Work equality now gives

\[
 \int a^\star\,d\mu\ge C{101\over100}-1
 >
 C{101\over100}-\int w\,d\nu
 =\int a\,d\nu.                                                        \tag{3.13}
\]

Thus the continuous price inequality of Theorem 4.1 fails explicitly; the
tail obstruction is not hidden only in a discontinuous indicator cut.

Therefore the hypotheses

* compact atomless jobs;
* a continuous socket density bounded below by a positive constant;
* exact equality of first moments; and
* strict socket/job count ratio between two and three

are jointly insufficient.

## 4. The exact generic price theorem

For a nonnegative bounded continuous socket price `a` on `(0,b)`, define
its covering closure

\[
 a^\star(x)=
 \inf\left\{
       \sum_{i=1}^na(y_i):
       n\ge1,\ 0<y_i<b,\ \sum_i y_i\ge x
     \right\}.                                                            \tag{4.1}
\]

### Theorem 4.1 (compact-job coagulation iff all covering prices pass)

Let `mu` be any finite measure on `[b,L]`, and let `nu` be any finite measure
on `(0,b)`, with

\[
                 \int x\,d\mu(x)=\int y\,d\nu(y)<\infty.              \tag{4.2}
\]

Then a finite exact coagulation exists if and only if

\[
 \boxed{
 \int a^\star(x)\,d\mu(x)
 \le
 \int a(y)\,d\nu(y)}                                                  \tag{4.3}
\]

for every nonnegative bounded continuous `a`.

No atomlessness or density assumption is needed for this equivalence.

### Proof

Necessity is configurationwise: an exact configuration is one of the covers
admitted in (4.1), so `a^star(x)<=sum_i a(y_i)`.  Integrating gives (4.3).

For sufficiency, first allow trimming.  Let `mathcal F_mu` be the set of
finite available-capacity measures `B` on `(0,b)` for which there is a
kernel with job marginal `mu`, aggregate used marginal `lambda<=B`, and

\[
                         \sum_i y_i\ge x                              \tag{4.4}
\]

in every configuration.  The set `mathcal F_mu` is convex and upward closed.
It is also narrowly closed.

To verify closedness, suppose `B_n->B` narrowly and choose witnesses
`rho_n`.  Narrow convergence gives both a uniform mass bound and uniform
tightness of the \((B_n)\)'s in the open socket space.  Their expected piece
counts are uniformly bounded:

\[
 \int N\,d\rho_n=\lambda_n(0,b)\le\sup_n B_n(0,b)<\infty.             \tag{4.5}
\]

Thus configurations with `N>R` have mass `O(1/R)`.  Given
\(\varepsilon>0\),
choose a compact \(K\Subset(0,b)\) with
\(\sup_nB_n((0,b)\setminus K)<\varepsilon\).  The mass of configurations
having some piece outside \(K\) is at most
\(\lambda_n((0,b)\setminus K)\le B_n((0,b)\setminus K)\).  For fixed \(R\),
the configurations with \(N\le R\), all pieces in \(K\), and job coordinate
in \([b,L]\) form a compact set.  Hence the configuration measures are tight
on the actual disjoint-union configuration space.  Pass to a weak limit
`rho`.  The cover inequality (4.4) is closed.  For every nonnegative
compactly supported continuous `f`, the
configuration functional `sum_i f(y_i)` is nonnegative lower semicontinuous,
so Portmanteau gives

\[
 \int\sum_i f(y_i)\,d\rho
 \le\liminf_n\int\sum_i f(y_i)\,d\rho_n
 \le\int f\,dB.                                                          \tag{4.6}
\]

The positive-piece marginal of `rho` is therefore at most `B`.  This proves
`B in mathcal F_mu`.

If `nu` were outside `mathcal F_mu`, separation from this closed convex
upward set would give a bounded continuous price `a` such that

\[
            \int a\,d\nu
        <   \inf_{B\in\mathcal F_\mu}\int a\,dB.                        \tag{4.7}
\]

Upward closure forces `a>=0`.  The right side separates independently over
jobs and equals

\[
             \int a^\star(x)\,d\mu(x).                                \tag{4.8}
\]

For completeness, (4.8) has no hidden infinite-arity assumption.  Restrict
first to pieces in `[1/M,b-1/M]`.  After redundant pieces are removed, a
cover of a job in `[b,L]` uses a uniformly bounded number of such pieces.
Compact measurable selection gives the restricted pointwise infimum.  As
`M` increases these infima decrease to (4.1), while repetitions of one fixed
interior socket give a bounded common dominator because the job support is
compact.  Dominated convergence proves (4.8).

Equations (4.7)--(4.8) contradict (4.3), so a covering kernel with used
marginal `lambda<=nu` exists.  Finally, exact work balance gives

\[
\begin{aligned}
0
&\le
 \int\left(\sum_i y_i-x\right)d\rho
 +\int y\,d(\nu-\lambda)\\
&=\int y\,d\nu-\int x\,d\mu=0.                                      \tag{4.9}
\end{aligned}
\]

Both nonnegative terms vanish.  Hence every cover is exact, and the positive
measure `nu-lambda` has zero integral against the strictly positive function
`y`; therefore `lambda=nu`.  Its expected piece count is finite, so almost
every configuration is finite.  This is the required coagulation. `square`

### Theorem 4.2 (generic interval-flow equivalence)

Put

\[
                         G(t)=\mu((t,\infty)),\qquad t\ge0.             \tag{4.10}
\]

A finite exact coagulation exists if and only if there is a finite measure
eta on

\[
              \mathcal E=\{(a,y):a\ge0,\ 0<y<b\}                       \tag{4.11}
\]

whose length marginal is nu and whose interval occupation is

\[
 \boxed{
 \int_{\mathcal E}\mathbf1_{\{a\le t<a+y\}}\,d\eta(a,y)=G(t)
 \quad\text{for a.e. }t\ge0.}                                         \tag{4.12}
\]

#### Proof

Given a coagulation, order each finite socket list and place the sockets
consecutively on \([0,x)\).  A job of size \(x\) then contributes
\(\mathbf1_{\{t<x\}}\) to occupation, proving (4.12), while every socket
contributes one interval of its own length.

Conversely, let \(\sigma_0,\sigma_1\) be the start and end marginals of
\(\eta\).  For compactly supported \(C^1\) test functions, integration by
parts gives

\[
 \int f\,d(\sigma_1-\sigma_0)
 =\int f'(t)G(t)\,dt
 =\int f\,d\mu-\mu([b,L])f(0).                                        \tag{4.13}
\]

If \(\mu([b,L])=0\), then (4.12), positivity, and the positive interval
lengths force \(\eta=0\), and the assertion is trivial.  Otherwise the
interval measure is a directed flow with source
\(\mu([b,L])\delta_0\) and sink \(\mu\).  Disintegrate at every positive
endpoint and pair the continuing part of incoming flow with outgoing flow.
Iteration from zero produces directed paths.  Any unused residual interval
flow has equal start and end marginals, so its occupation density has zero
distributional derivative.  Finite total interval work forces that constant
occupation density to be zero, and positive interval lengths force the
residual flow itself to vanish.

Finally \(\eta(\mathcal E)=\nu(0,b)<\infty\).  Dividing by the source mass
shows that the mean number of intervals per path is finite; hence paths are
finite almost surely.  Their terminal marginal is \(\mu\), their
length-occurrence marginal is \(\nu\), and the sum of the consecutive
lengths is the terminal position. \(\square\)

### Corollary 4.3 (an explicit renewal sufficient condition)

Let

\[
                         \overline\nu(u)=\nu((u,b)),\qquad u\ge0.       \tag{4.14}
\]

If there is a probability measure \(q\) on \([0,\infty)\) such that

\[
 \boxed{
 G(t)=\int_{[0,t]}\overline\nu(t-a)\,dq(a)
 \quad\text{for a.e. }t\ge0,}                                         \tag{4.15}
\]

then a finite exact coagulation exists.

Indeed, take \(\eta(da,dy)=q(da)\nu(dy)\).  Its length marginal is \(\nu\),
and Fubini identifies its occupation density with the right side of (4.15).
Theorem 4.2 applies.  This product renewal condition is only sufficient;
general solutions may require the start and length to be dependent.

## 5. The compact gapped finite-arity dual

The post-primary Rayleigh reduction has socket support bounded away from
zero.  In that setting the preceding criterion has a simpler signed form.

Let `S` be a nonempty compact subset of `[q,b]` with `q>0`, and let `J` be a
nonempty compact subset of `(0,infinity)`.  Assume explicitly that every
`x in J` has a representation as a finite sum of members of `S` (equivalently,
one may first replace the job support by its intersection with the
representable semigroup).  Put

\[
 N=\left\lfloor{\max J\over q}\right\rfloor.                           \tag{5.1}
\]

For `phi in C(S)`, define

\[
 m_\phi(x)=
 \min\left\{
       \sum_{i=1}^n\phi(y_i):
       1\le n\le N,\ y_i\in S,\ \sum_i y_i=x
     \right\}.                                                         \tag{5.2}
\]

### Theorem 5.1 (finite-arity exact transport dual)

For finite measures `gamma` on `J` and `lambda` on `S`, an exact finite
coagulation exists if and only if

\[
 \boxed{
       \int_S\phi\,d\lambda
       \ge
       \int_Jm_\phi\,d\gamma
       \qquad(\phi\in C(S)).}                                          \tag{5.3}
\]

### Proof

The representability assumption is essential for the displayed minimum in
(5.2) to be finite on the whole job support.  No additional scalar
hypotheses are needed: the two tests \(\phi(y)=y\) and \(-y\) enforce exact
work, while the tests \(\phi=1\) and \(-1\) enforce the feasible lower and
upper aggregate occurrence-count bounds.  The job mass is already fixed by
the prescribed job marginal `gamma`.

The exact configuration space is the finite disjoint union, for
`1<=n<=N`, of the compact fibres

\[
 \{(x;y_1,\ldots,y_n):x\in J,\ y_i\in S,\ \sum_i y_i=x\}/\mathfrak S_n.
                                                                            \tag{5.4}
\]

Measures on (5.4) with fixed job marginal `gamma` form a compact convex set.
The aggregate occurrence-marginal map is continuous, because
`sum_i phi(y_i)` is continuous and `n<=N`.  Its image is therefore compact
and convex.  Separation of `lambda` from that image gives a continuous
`phi`; minimizing the separating functional over the fixed job marginal
separates pointwise over `x` and gives exactly `int m_phi dgamma`.  This is
(5.3).  The reverse direction is immediate by integration over any
configuration measure. `square`

Thus the compact gapped problem is literally a finite-arity multi-marginal
transport problem.  Compactness removes every analytic closure issue, but it
does not make the inequalities (5.3) automatic.

## 6. Consequence for the Rayleigh compact remainder

The pre-primary Rayleigh compact remainder `(mu_c,nu_c)` has precisely the
qualitative properties refuted by Section 3: compact separated supports,
atomless densities, equal work, and

\[
                   2\mu_c(\mathbb R)<\nu_c(\mathbb R)
                                      <3\mu_c(\mathbb R).               \tag{6.1}
\]

Therefore no generic atomless compact-coagulation theorem based only on
those rows can close the Rayleigh problem.  Its special densities must be
used to prove the full family (4.3), or an explicit kernel must be built.

After the bottom-quantile primary socket is removed, the remaining pair
`(gamma,lambda)` has socket support in `[q,b]` and uniform finite arity.
Theorem 5.1 applies directly (on its representable job support).  Hence its
exact unresolved row is the signed finite-arity family (5.3), not tightness,
tail control, atomlessness, or scalar count.

There is a preliminary pointwise gate which the choice of primary coupling
must respect.  With the actual atomless socket interval \((q,b)\), the set of
representable positive remainder sizes is exactly

\[
 \boxed{
 \mathcal R(q,b)=\bigcup_{n\ge1}(nq,nb).}                              \tag{6.2}
\]

Necessity is immediate from summing \(n\) values in \((q,b)\); sufficiency
follows by using \(n\) equal values \(z/n\).  Thus a primary coupling
\((x,y)\) is unusable whenever \(x-y\notin\mathcal R(q,b)\).  If
\(q<b/2\), these intervals overlap and
\(\mathcal R(q,b)=(q,\infty)\).  At \(q=b/2\), the single additional point
\(b\) is absent.  If \(q>b/2\), finitely many genuine gaps remain between
successive intervals.  An arbitrary bottom-primary coupling does not
automatically avoid them.

The threshold cuts (2.2), specialized to the Rayleigh measures, provide a
first concrete analytic audit family:

\[
 \nu_c((t,b))
 \le
 \int\left(\left\lceil{x\over t}\right\rceil-1\right)d\mu_c(x)
 \qquad(0<t<b).                                                            \tag{6.3}
\]

Satisfying the pointwise gate (6.2) and all threshold cuts (6.3) would still
be only necessary.  Theorem 4.1 identifies the complete target: every
covering-closed price must pass.

## 7. Scope

This note proves:

1. a rigorous counterexample to the proposed generic compact theorem,
   even with strict two-to-three count slack;
2. exact necessary count and tail-capacity cuts;
3. a necessary-and-sufficient generic covering-price theorem;
4. an exact interval-flow formulation and a concrete renewal sufficient
   condition; and
5. a compact finite-arity signed dual for the gapped remainder.

It does **not** prove the Rayleigh price inequalities, construct its compact
kernel, or imply an integral/literal SCD rounding.
