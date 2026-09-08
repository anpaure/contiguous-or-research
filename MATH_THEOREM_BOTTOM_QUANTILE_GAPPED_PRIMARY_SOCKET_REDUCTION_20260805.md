# Bottom-quantile primary sockets: a gapped non-equal-level continuation

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reduction.  For any separated atomless
job/socket pair with strict socket-count slack, one can assign one
bottom-quantile socket to every job so that all remainders are uniformly
bounded away from zero.  This is the simplest continuation that avoids the
origin prefix-Hall failure of repeated equal-level subtraction.  It does
not by itself coagulate the remaining pair.

## 1. General theorem

Let `alpha` be a finite atomless socket measure supported on `(0,b)` and
`beta` a finite atomless job measure supported on `(b,infinity)`.  Assume

\[
 \int y\,d\alpha(y)=\int x\,d\beta(x),             \tag{1.1}
\]

and put

\[
 S=\alpha(0,b),\qquad J=\beta(b,\infty).
\]

Assume `S>J>0`, and assume the cumulative function of `alpha` is strictly
increasing on `(0,b)`.

### Theorem 1.1 (bottom-quantile gap reduction)

There is a unique `q in (0,b)` such that

\[
 \alpha(0,q)=J.                                    \tag{1.2}
\]

Let

\[
 \kappa=\alpha|_{(0,q)},
 \qquad
 \lambda=\alpha|_{(q,b)}.                          \tag{1.3}
\]

Choose any coupling `pi` of the equal-mass measures `beta` and `kappa`,
and push it forward under

\[
 (x,y)\longmapsto x-y
\]

to obtain a remainder-job measure `gamma`.  Then

\[
 \boxed{\operatorname {supp}\gamma\subseteq[b-q,\infty),} \tag{1.4}
\]

and the remaining pair `(gamma,lambda)` has equal work:

\[
 \boxed{
 \int z\,d\gamma(z)=\int y\,d\lambda(y).}          \tag{1.5}
\]

Its masses are

\[
 \gamma(0,\infty)=J,
 \qquad
 \lambda(0,b)=S-J.                                \tag{1.6}
\]

Finally, every coagulation of `(gamma,lambda)` lifts to a coagulation of
`(beta,alpha)` by appending the coupled primary socket `y` to the
configuration of `x-y`.

### Proof

Existence and uniqueness of `q` follow from atomlessness, strict increase,
and `0<J<S`.  Both marginals of `pi` have mass `J`.  Since
`x>b` and `y<q`, every remainder satisfies

\[
 x-y>b-q>0,
\]

which proves (1.4).  Moreover

\[
\begin{aligned}
 \int z\,d\gamma(z)
 &=\int(x-y)\,d\pi(x,y)\\
 &=\int x\,d\beta(x)-\int y\,d\kappa(y)\\
 &=\int y\,d\alpha(y)-\int y\,d\kappa(y)\\
 &=\int y\,d\lambda(y),
\end{aligned}
\]

which is (1.5).  The count identities are immediate.  Disintegrating
`pi` over the remainder together with `(x,y)` and appending `y` to any
remainder configuration gives total `(x-y)+y=x`; its aggregate appended
socket marginal is `kappa`, while the remainder kernel uses `lambda`.
Thus the lifted marginals are exactly `beta` and `alpha`. `square`

### Corollary 1.2 (the exact count scalar)

The reduced pair passes the unavoidable one-socket-per-positive-job count
row exactly when

\[
 \boxed{S\ge2J.}                                   \tag{1.7}
\]

If `S<2J`, this particular one-primary-socket reduction cannot be
completed: all remainder jobs are positive by (1.4), but the remaining
socket mass `S-J` is smaller than their mass `J`.

This is a no-go only for the bottom-quantile **one-socket** policy.  A
policy assigning two sockets at once to some jobs is not covered.

## 2. Application after the first Rayleigh equal-level transform

Let `widetilde K` be the first transformed Rayleigh kernel.  It is strictly
decreasing on `(0,b)`, strictly increasing on `(b,infinity)`, and has

\[
 \widetilde K(0)=K_0+m>0,
 \qquad
 \widetilde K(b)=u(b)<0.                            \tag{2.1}
\]

After cancelling its common one-piece overlap, the separated socket and
job measures are

\[
 \alpha(dy)=-\widetilde K'(y)\mathbf1_{(0,b)}dy,
 \qquad
 \beta(dx)=\widetilde K'(x)\mathbf1_{(b,\infty)}dx. \tag{2.2}
\]

Their masses are

\[
 S=\widetilde K(0)-\widetilde K(b)
   =K_0+m-u(b),
 \qquad
 J=-\widetilde K(b)=-u(b).                         \tag{2.3}
\]

Hence the strict socket-count slack is

\[
 S-J=K_0+m>0.                                      \tag{2.4}
\]

Theorem 1.1 therefore supplies a non-equal-level primary coupling whose
remainders have a strict positive gap.  Its reduced count gate is the
single scalar

\[
 \boxed{
 \Gamma:=S-2J=K_0+m+u(b).}                         \tag{2.5}
\]

If `Gamma>=0`, the reduced pair has at least one socket occurrence per
positive remainder job.  If `Gamma<0`, some jobs must receive at least two
new sockets in the next macro-step; one-primary-socket continuation is
count-impossible.

No sign of `Gamma` is claimed here.  More importantly, even
`Gamma>=0` would settle only the count row of the gapped remainder pair,
not its complete configuration inequalities.

## 3. Relation to the repeated equal-level no-go

The repeated equal-level rule pairs sockets and jobs adjacent to the cusp
minimum.  Its new remainder density is positive at zero, while its unused
socket density vanishes there.  The bottom-quantile rule does the opposite:
it reserves the entire upper socket tail and uses only a lower quantile,
forcing every remainder to be at least `b-q>0`.

Thus the origin prefix obstruction is avoidable; the price is the explicit
count scalar (2.5) and a new compact/gapped configuration problem.  This is
an exact branch reduction, not a complete Rayleigh coagulation.

## 4. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_PRIMARY_SUBTRACTION_20260805.md`,
   SHA at use:
   `b63058f76b1ebb4904b4b939b10f981332d7de36bba90a39d8b1a35424787ac6`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA at use:
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.

