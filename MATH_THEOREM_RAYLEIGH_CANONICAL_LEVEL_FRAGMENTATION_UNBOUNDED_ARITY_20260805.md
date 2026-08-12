# Canonical Rayleigh level fragmentation has necessarily unbounded arity

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional scoped no-go and exact reduction.  The canonical
negative-level intervals cannot be split into only one or two pieces with
the positive-lobe length marginal.  In fact no uniform arity bound is
possible.  After the maximal diagonal one-piece cancellation, this proposal
is exactly the already isolated first-transformed residual fragmentation
problem, whose scalar count lies strictly between two and three pieces per
remaining job.

## 1. The two length measures

Let `K` be the Rayleigh signed-tail kernel, let `b` be its first positive
zero, let `c` be its unique minimum, and put `m=K(c)<0`.  At negative level
`u in (m,0)`, write

\[
 K(\ell(u))=K(r(u))=u,
 \qquad \ell(u)<c<r(u),
\]

and

\[
 z(u)=r(u)-\ell(u).
\]

The inverse-branch theorem gives a strictly increasing bijection

\[
 z:(m,0)\longrightarrow(0,\infty).
\]

Define the canonical level-length measure

\[
 \beta=z_\#(du|_{(m,0)}).
\]

On the positive lobe put `p=K_+` and

\[
 \alpha(dy)=-p'(y)\,dy=-K'(y){\bf1}_{(0,b)}(y)\,dy.
\]

Thus

\[
 \operatorname{supp}\alpha\subseteq[0,b],
 \qquad
 \operatorname{supp}\beta=[0,\infty).
\]

Their first moments agree.  Indeed, layer cake gives

\[
 \int y\,d\alpha(y)=\int_0^b p(t)\,dt,
\]

while the negative superlevel intervals give

\[
 \int z\,d\beta(z)=\int_0^\infty K_-(t)\,dt,
\]

and `integral K=0` identifies the two quantities.

The masses are

\[
 \alpha(0,\infty)=K(0),
 \qquad
 \beta(0,\infty)=-m,
\]

and the authenticated count theorem gives `1<K(0)/(-m)<2`.

## 2. The support obstruction

### Theorem 2.1

In every finite fragmentation of a `beta`-job of length `z` into pieces
whose aggregate marginal is `alpha`, its number `N(z)` of pieces satisfies

\[
 \boxed{N(z)\ge \left\lceil {z\over b}\right\rceil.}
\]

Consequently:

1. no fragmentation supported on one- and two-piece configurations exists;
2. no fragmentation with any fixed uniform arity bound exists;
3. every successful fragmentation has positive occurrence mass at
   arbitrarily large arities.

### Proof

Every positive `alpha`-piece has length at most `b`.  If a job of length
`z` is partitioned into `N` such pieces, then `z<=Nb`, proving the displayed
bound.

For every finite `L`, strict surjectivity of `z:(m,0)->(0,infinity)` gives

\[
 \beta((L,\infty))>0.
\]

In particular, jobs of length greater than `2b` have positive `beta`-mass
and require at least three pieces.  More generally, jobs of length greater
than `Nb` have positive mass and require at least `N+1` pieces.  This proves
all three assertions. `square`

The fact that the **average** piece count lies between one and two is not in
conflict with the theorem.  Rare long jobs use three, four, and arbitrarily
many pieces; their excess count must be offset by a sufficiently large bank
of one-piece jobs.

## 3. Maximal diagonal cancellation recovers the known residual

The transformed job measure `beta` has density `u'(t)` at length `t`, where
`u=z^{-1}`.  The one-well theorem proves

\[
 0<u'(t)<-K'(t)\qquad(0<t<b).
\]

Hence the whole submeasure

\[
 u'(t){\bf1}_{(0,b)}(t)\,dt
\]

may be cancelled as literal one-piece configurations between `beta` and
`alpha`.  The uncancelled measures are exactly

\[
 \beta_2(dt)=u'(t){\bf1}_{(b,\infty)}(t)\,dt
\]

and

\[
 \alpha_2(dy)=\bigl(-K'(y)-u'(y)\bigr)
                   {\bf1}_{(0,b)}(y)\,dy.
\]

These are the job and socket measures of the authenticated
first-transform overlap-cancelled residual.  If their masses are denoted by
`J_2` and `S_2`, respectively, the exact count theorem states

\[
 \boxed{2J_2<S_2<3J_2.}
\]

Thus the canonical level-fragmentation proposal does not reduce the open
configuration gate to a one/two-piece coupling.  Its natural maximal
one-piece cancellation returns verbatim to the known two/three average-count
residual, while the unbounded support still forces unbounded arity before the
separate Gaussian-tail removal.

This is a scoped statement.  It does not rule out a state-dependent
unbounded-arity fragmentation of `beta` into `alpha`, nor the already proved
tail removal followed by a compact configuration coupling.

## 4. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`.
4. `MATH_THEOREM_RAYLEIGH_DEVIATION_LORENZ_AND_RESIDUAL_INTERVAL_CORE_20260805.md`.
