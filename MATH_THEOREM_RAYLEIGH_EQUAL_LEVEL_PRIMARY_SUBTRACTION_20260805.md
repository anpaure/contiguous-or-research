# Rayleigh equal-level primary subtraction and the transformed coagulation gate

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reduction on the separated-residual face.
The signed-tail kernel supplies one canonical, state-dependent first socket
for every residual job.  The remaining jobs and sockets have explicit
densities and equal work.  A coagulation of that transformed pair lifts
literally to a coagulation of the original Rayleigh pair.  The transformed
pair is not solved here.

## 0. Setup and outcome

Put

\[
 A={\sqrt\pi\over2},\qquad p=e^{-A^2},
\]

and let

\[
 j(x)=2(A+x)e^{-(A+x)^2}\quad(x>0),
\qquad
 s(y)=2(A-y)e^{-(A-y)^2}\quad(0<y<A).
\]

The signed-tail kernel is

\[
 K(t)=
 \begin{cases}
 1-e^{-(A-t)^2}-e^{-(A+t)^2},&0\le t\le A,\\
 -e^{-(A+t)^2},&t>A.
 \end{cases}                                      \tag{0.1}
\]

It satisfies

\[
 K'(t)=j(t)-s(t)\quad(0<t<A),
 \qquad K'(t)=j(t)\quad(t>A),                       \tag{0.2}
\]

and has a unique zero `y_* in (0,A)` and a unique minimum at
`c in (y_*,A)`.  Write

\[
 K_0=K(0)=1-2p>0,\qquad m=K(c)<0.                  \tag{0.3}
\]

After matching the common one-piece density `min(j,s)`, the remaining
socket and job measures are exactly

\[
 \nu_{\rm res}(dy)=-K'(y){\bf1}_{(0,c)}(y)\,dy,
 \qquad
 \mu_{\rm res}(dx)=K'(x){\bf1}_{(c,\infty)}(x)\,dx. \tag{0.4}
\]

This note gives a canonical first subtraction for (0.4).  Let
`ell(u) in (y_*,c)` and `r(u) in (c,infinity)` be the two inverse branches
of `K` at level `u in (m,0)`.  Pair the job `r(u)` with the socket
`ell(u)`.  Their difference

\[
                         z(u)=r(u)-\ell(u)           \tag{0.5}
\]

is the transformed job.  The unused socket bank is simply the initial
branch `(0,y_*)` of (0.4).

The key point is that both paired marginals are literally Lebesgue measure
`du` on `(m,0)`.  No independent-renewal assumption or guessed coupling is
used.

## 1. The equal-level coupling is exact

### Lemma 1.1 (inverse branches)

The maps `ell` and `r` are well defined and continuous on `(m,0)`, with

\[
 \ell(u)<c<r(u),\qquad K(\ell(u))=K(r(u))=u.        \tag{1.1}
\]

Moreover

\[
 \ell'(u)={1\over K'(\ell(u))}<0,
 \qquad
 r'(u)={1\over K'(r(u))}>0,                         \tag{1.2}
\]

so `z` is strictly increasing from zero to infinity.

#### Proof

The one-minimum theorem says that `K` decreases strictly from zero to `m`
on `(y_*,c)` and increases strictly from `m` to zero on `(c,infinity)`.
This gives the two inverse branches and (1.2).  Consequently

\[
 z'(u)={1\over K'(r(u))}-{1\over K'(\ell(u))}>0.
\]

As `u downarrow m`, both inverse branches tend to `c`, so `z(u)->0`.
As `u upward 0`, `ell(u)->y_*` and `r(u)->infinity`, so
`z(u)->infinity`.  `square`

### Theorem 1.2 (one exact primary socket per residual job)

The measure

\[
                         du\quad(m<u<0)              \tag{1.3}
\]

under the map `u -> r(u)` is `mu_res`, while under
`u -> ell(u)` it is the restriction of `nu_res` to `(y_*,c)`.

#### Proof

On the right branch, `du=K'(x)dx`; on the left branch, orientation is
reversed and `du=K'(y)dy`, so positive Lebesgue measure in increasing
`u` pushes forward as `-K'(y)dy`.  Equations (0.4) give the assertion.
`square`

Thus every residual job receives one genuine socket, and every socket in
the negative-level branch is used once.

## 2. The transformed pair

Define

\[
 \widetilde\mu=z_\#(du|_{(m,0)}),
 \qquad
 \widetilde\nu(dy)=-K'(y){\bf1}_{(0,y_*)}(y)\,dy.   \tag{2.1}
\]

### Proposition 2.1 (explicit transformed density)

The transformed job measure is atomless on `(0,infinity)`.  At
`w=z(u)`, put

\[
 a(u)=K'(r(u))>0,
 \qquad b(u)=-K'(\ell(u))>0.
\]

Then

\[
 {d\widetilde\mu\over dw}(z(u))
 ={a(u)b(u)\over a(u)+b(u)}.                        \tag{2.2}
\]

Its total mass and the unused-socket mass are

\[
 \widetilde\mu(0,\infty)=-m,
 \qquad
 \widetilde\nu(0,y_*)=K_0.                         \tag{2.3}
\]

They have exactly equal first moments:

\[
 \int_0^\infty w\,d\widetilde\mu(w)
 =\int_0^{y_*}y\,d\widetilde\nu(y).                \tag{2.4}
\]

#### Proof

Equation (2.2) is change of variables, since

\[
 z'(u)={1\over a(u)}+{1\over b(u)}.
\]

The mass identities follow from the lengths of the level intervals:
`(m,0)` has length `-m`, while

\[
 \int_0^{y_*}-K'(y)dy=K(0)-K(y_*)=K_0.
\]

The original separated residual measures have equal work.  Theorem 1.2
uses work `integral ell(u)du` from the socket side and pairs it with the
same occurrence parameter on the job side.  Subtracting that common
quantity leaves

\[
 \int_m^0(r(u)-\ell(u))du
 =\int_0^{y_*}y(-K'(y))dy,
\]

which is (2.4).  `square`

### Lemma 2.2 (strict count slack survives)

For the Rayleigh value `A=sqrt(pi)/2`,

\[
                         K_0>-m.                    \tag{2.5}
\]

#### Proof

Write `c=A theta`.  The minimum equation is

\[
 \operatorname {arctanh}\theta={\pi\over2}\theta.
\]

At `theta=17/20`, the left side is
`(1/2)log(37/3)`, which is smaller than
`17pi/40`; hence `theta>17/20`.  (For example,
`log(37/3)<13/5` and `17pi/40>527/400>13/10`.)
At the minimum, `j(c)=s(c)`, and therefore

\[
 m=1-{2\over1+\theta}e^{-A^2(1-\theta)^2}.
\]

Using the strict inequalities `theta>17/20` and
`p=e^{-pi/4}<17/37` gives

\[
 p+{e^{-A^2(1-\theta)^2}\over1+\theta}
 <{17\over37}+{20\over37}=1.
\]

This rearranges to `1-2p>-m`, which is (2.5).  For the elementary bound
`p<17/37`, use `pi/4>39/50` and

\[
 e^{39/50}>1+{39\over50}+{1\over2}\left({39\over50}\right)^2
 +{1\over6}\left({39\over50}\right)^3
 +{1\over24}\left({39\over50}\right)^4>{37\over17}.
\]
`square`

The count inequality is necessary for the transformed pair because every
positive transformed job still needs at least one further socket.  Here it
holds with strict room.

### Proposition 2.3 (exact transformed signed-tail recurrence)

Let `u(t)=z^(-1)(t)` and put `b=y_*`.  The signed-tail kernel of the
transformed pair is

\[
 \widetilde K(t)=
 \begin{cases}
 K(t)+u(t),&0\le t<b,\\
 u(t),&t\ge b.
 \end{cases}                                      \tag{2.6}
\]

In particular,

\[
 \widetilde K(0)=K_0+m>0,
 \qquad \widetilde K(\infty)=0,
 \qquad \int_0^\infty\widetilde K(t)\,dt=0.       \tag{2.7}
\]

#### Proof

For `t<b`, the unused-socket tail is

\[
 \int_t^b-K'(y)dy=K(t),
\]

while strict increase of `z` gives transformed-job tail
`integral_(u(t))^0du=-u(t)`.  Their difference is `K(t)+u(t)`.
For `t>=b` the socket tail is zero, so the signed tail is `u(t)`.
The endpoint statements follow from `u(0)=m`, `u(infinity)=0`, and
Lemma 2.2.  Its integral is the difference of the two first moments, which
vanishes by (2.4).  `square`

The pointwise inequality

\[
                         -K'(t)\ge u'(t)
                         \qquad(0<t<b)               \tag{2.8}
\]

would make the first branch of `widetilde K` nonincreasing and hence put
the transformed pair back on the same one-valley face.  This stronger
inequality is not proved here; neither is it implied merely by the
corresponding cumulative prefix inequality.

## 3. Exact lifting theorem

### Theorem 3.1 (transformed coagulation implies Rayleigh coagulation)

Suppose there is a finite-configuration coagulation kernel for the pair
`(widetilde mu,widetilde nu)` in (2.1).  Then there is a finite-configuration
coagulation kernel for the original Rayleigh pair `(mu,nu)`.

#### Proof

The map `z:(m,0)->(0,infinity)` is a bijection by Lemma 1.1.  Disintegrate
the transformed kernel over its job value `w`, set `u=z^(-1)(w)`, and
append the one additional socket `ell(u)` to every transformed
configuration.  Its new total is

\[
 w+\ell(u)=z(u)+\ell(u)=r(u).
\]

The job marginal is therefore `r_#du=mu_res`, and the aggregate socket
marginal is

\[
 \widetilde\nu+\ell_\#du
 =\nu_{\rm res}|_{(0,y_*)}
  +\nu_{\rm res}|_{(y_*,c)}
 =\nu_{\rm res}.
\]

Finally add the common one-piece configurations of density
`min(j,s)` on `(0,A)`.  They restore the cancelled parts of both original
marginals.  Every configuration remains finite, proving the theorem.
`square`

## 4. Exact frontier

The reduction is genuinely state dependent: the first socket is the
deterministic function `ell(K(x))` of the current residual job `x`.
It therefore lies outside the start-independent renewal face already
proved impossible.

What is now explicit is

\[
 \boxed{
 (\mu,\nu)
 \longleftarrow
 (\mu_{\rm res},\nu_{\rm res})
 \longleftarrow
 (\widetilde\mu,\widetilde\nu),
 }
\]

where the second arrow appends one actual equal-level socket and the final
pair has the harmonic-mean job density (2.2), socket support `(0,y_*)`,
equal work, and strict count slack.

The remaining analytic question is whether the transformed pair admits a
finite coagulation.  In particular, this note does **not** assert that the
equal-level transformation is closed under iteration, that its transformed
signed-tail kernel again has one minimum, or that the process terminates.
No discrete, named, chronological, or OR-word conclusion is claimed.

## 5. Dependencies

1. `MATH_THEOREM_RAYLEIGH_JOB_SOCKET_COAGULATION_EXACT_REDUCTION_20260804.md`;
2. `MATH_THEOREM_RAYLEIGH_INTERVAL_FLOW_DUAL_CLOSEDNESS_AND_RENEWAL_OBSTRUCTION_20260804.md`;
3. `MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md`.
