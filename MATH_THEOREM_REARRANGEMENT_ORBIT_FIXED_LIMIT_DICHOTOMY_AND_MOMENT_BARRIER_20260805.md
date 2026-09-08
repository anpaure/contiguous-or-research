# Rearrangement-orbit fixed-limit dichotomy and the signed-moment barrier

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional compactness theorem.  Under one common
integrable envelope for the anchored negative profiles, every positive
mass surviving an `mathcal R` orbit produces a sign-reversed fixed point
as an omega-limit.  More strongly, a uniform second-moment bound gives a
possibly atomic sign-reversed measure limit, and a nonpositive
signed-first-moment invariant excludes it and forces `L1` decay.  This
does not establish that invariant for every Rayleigh iterate.

## 1. Setup

Let

\[
 H_{n+1}=\mathcal RH_n,
 \qquad p_n=(H_n)_+,
 \qquad q_n=(H_n)_-,
 \qquad C_n=C_{H_n}.
\]

Assume every `H_n` has integral zero and finite `L1` norm.  Put

\[
 A_n=\int p_n=\int q_n.
\]

The exact rearrangement identity gives

\[
 H_{n+1}=p_n-C_n,
 \qquad \int C_n=A_n.                             \tag{1.1}
\]

In particular

\[
 p_{n+1}=(p_n-C_n)_+\le p_n                       \tag{1.2}
\]

pointwise, and

\[
 A_n-A_{n+1}=\int\min\{p_n,C_n\}.                 \tag{1.3}
\]

## 2. Fixed-limit dichotomy

### Theorem 2.1

Assume there is one integrable function `E>=0` such that

\[
 C_n(t)\le E(t)\qquad(n\ge0)                      \tag{2.1}
\]

for almost every `t`.  Then either

\[
 \|H_n\|_1\longrightarrow0,                      \tag{2.2}
\]

or the orbit has an `L1` omega-limit of the form

\[
 G=p_\infty-C_\infty\ne0,                         \tag{2.3}
\]

where

1. `C_infinity` is nonnegative and nonincreasing;
2. `p_infinity C_infinity=0` almost everywhere;
3. `int p_infinity=int C_infinity>0`; and
4. `mathcal R G=G`.

Thus every nonzero compact limit is a sign-reversed separated fixed
point: its negative part is an initial nonincreasing profile and its
positive part lies beyond that profile.

### Proof

By (1.2), `p_n` decreases pointwise to a function `p_infinity`.  The
numbers `A_n` decrease to some `A_infinity>=0`; monotone convergence gives

\[
 \int p_\infty=A_\infty,
 \qquad p_n\longrightarrow p_\infty\quad\hbox{in }L^1. \tag{2.4}
\]

If `A_infinity=0`, then

\[
 \|H_n\|_1=2A_n\longrightarrow0,
\]

which is (2.2).

Suppose `A_infinity>0`.  Every `C_n` is nonnegative and nonincreasing.
Helly selection gives a subsequence, still denoted `C_n`, converging
pointwise at every continuity point to a nonnegative nonincreasing
`C_infinity`.  The common envelope (2.1) and dominated convergence give

\[
 C_n\longrightarrow C_\infty\quad\hbox{in }L^1,
 \qquad \int C_\infty=A_\infty.                  \tag{2.5}
\]

Since `A_n` converges, (1.3) implies

\[
 \int\min\{p_n,C_n\}\longrightarrow0.
\]

Equations (2.4)--(2.5), or simply the Lipschitz continuity of `min` in
its two arguments, yield

\[
 \min\{p_\infty,C_\infty\}=0\quad\hbox{a.e.}      \tag{2.6}
\]

Along this subsequence, (1.1) gives

\[
 H_{n+1}\longrightarrow G=p_\infty-C_\infty
 \quad\hbox{in }L^1.                              \tag{2.7}
\]

The negative superlevel sets of the nonincreasing initial profile
`C_infinity` are initial intervals, so its anchored component profile is
itself.  By (2.6), the positive part `p_infinity` is disjoint from it.
Therefore

\[
 \mathcal RG=p_\infty-C_\infty=G.
\]

Both masses equal the positive number `A_infinity`, so `G` is nonzero.
This proves the theorem. `square`

## 3. The signed-first-moment barrier

### Theorem 3.1

In addition to the hypotheses of Theorem 2.1, assume

\[
 \int_0^\infty t\bigl(p_0(t)+E(t)\bigr)dt<\infty. \tag{3.1}
\]

If every orbit point satisfies

\[
 \boxed{\int_0^\infty tH_n(t)dt\le0,}             \tag{3.2}
\]

then

\[
 \boxed{\|H_n\|_1\longrightarrow0.}              \tag{3.3}
\]

### Proof

If (3.3) failed, Theorem 2.1 would give a nonzero fixed omega-limit
`G=p_infinity-C_infinity`.  Because `C_infinity` is nonzero,
nonincreasing, and disjoint from the equal-mass `p_infinity`, its support
must end at a finite point `tau`: if it stayed positive at every finite
point, disjointness would force `p_infinity=0`.

Consequently `p_infinity` is supported in `[tau,infinity)`, while
`C_infinity` is supported in `[0,tau]` and has positive mass strictly
before `tau`.  Hence

\[
 \int t p_\infty(t)dt
 \ge \tau A_\infty
 >\int t C_\infty(t)dt,                           \tag{3.4}
\]

so

\[
 \int tG(t)dt>0.                                  \tag{3.5}
\]

On the other hand `p_n<=p_0`, `C_n<=E`, and (3.1) permit dominated
convergence with the weight `t` in (2.7).  Thus the signed first moments
of `H_{n+1}` on this subsequence converge to the positive quantity
(3.5), contradicting (3.2).  Therefore only (3.3) is possible. `square`

The exact moment-drift identity shows that the moments in (3.2) are
nondecreasing.  Hence it is enough to prove that their supremum is at
most zero; equivalently, that the total accumulated translation drift is
at most the magnitude of the original negative signed moment.

## 4. Envelope-free `L1` decay from second moments

The common pointwise envelope in Theorem 2.1 is convenient but is not
needed merely to force `L1` decay.  The key is that rearrangement itself
controls every positive moment of the profiles.

### Lemma 4.1 (profile moments decrease)

For every `alpha>=0` for which the displayed moments are finite,

\[
 \int_0^\infty t^\alpha C_n(t)dt
 \le \int_0^\infty t^\alpha q_n(t)dt.             \tag{4.1}
\]

For `n>=1`, one also has `q_n<=C_(n-1)`, and therefore

\[
 \boxed{
 \int t^\alpha C_n
 \le\int t^\alpha C_{n-1}.}                       \tag{4.2}
\]

### Proof

At negative depth `s`, write the components as
`(a_(s,j),a_(s,j)+ell_(s,j))`.  Then

\[
 \int_0^{\ell_{s,j}}t^\alpha dt
 \le
 \int_{a_{s,j}}^{a_{s,j}+\ell_{s,j}}t^\alpha dt.
\]

Integrating in `s` and summing proves (4.1).  Equation (1.1) gives

\[
 q_n=(C_{n-1}-p_{n-1})_+\le C_{n-1},
\]

which combines with (4.1) to give (4.2). `square`

### Theorem 4.2 (measure-compact signed-moment barrier)

Assume

\[
 \int_0^\infty t^2\bigl(p_0(t)+C_0(t)\bigr)dt<\infty. \tag{4.3}
\]

If

\[
 \boxed{\int_0^\infty tH_n(t)dt\le0
 \qquad(n\ge0),}                                  \tag{4.4}
\]

then

\[
 \boxed{\|H_n\|_1\longrightarrow0.}              \tag{4.5}
\]

No uniform component bound, pointwise envelope, or Lipschitz estimate is
needed for this `L1` conclusion.

### Proof

As in Theorem 2.1, `p_n` decreases pointwise and in `L1` to a function
`p_infinity` of mass `A_infinity`.  Suppose for contradiction that
`A_infinity>0`.

Regard `C_n(t)dt` as finite measures.  Lemma 4.1 with `alpha=2` gives a
uniform second-moment bound, hence tightness and uniform integrability of
their first moments.  Along a subsequence they converge weakly to a
measure `mu` of total mass `A_infinity`, and their first moments converge
to that of `mu`.

On every compact interval bounded away from zero, monotonicity and the
mass bound give a common `L-infinity` bound for `C_n`.  Helly selection
therefore identifies the restriction of `mu` to `(0,infinity)` as

\[
 c_\infty(t)dt,
\]

where `c_infinity` is nonnegative and nonincreasing.  The only possible
singular part is an atom at the origin:

\[
 \mu=\alpha\delta_0+c_\infty(t)dt.                \tag{4.6}
\]

The overlap in (1.3) tends to zero.  Local dominated convergence away
from zero consequently gives

\[
 p_\infty(t)c_\infty(t)=0
 \quad\hbox{for almost every }t>0.                 \tag{4.7}
\]

If `c_infinity` is nonzero, let `tau` be the endpoint of its support.
It must be finite: otherwise monotonicity makes `c_infinity` positive
almost everywhere on `(0,infinity)`, and (4.7) would contradict the
positive mass of `p_infinity`.  Equation (4.7) then puts `p_infinity` in
`[tau,infinity)`.  If `c_infinity=0`, take `tau=0`; all of `mu` is then
the origin atom.

In either case, equality of the two total masses gives the strict
barycentre inequality

\[
 \int_0^\infty t p_\infty(t)dt
 >\int_{[0,\infty)}t\,d\mu(t).                    \tag{4.8}
\]

Indeed, the left mass is an `L1` function supported at or to the right of
`tau`, while the continuous part of `mu` lies strictly to its left and
the atom in (4.6) lies at zero.

Finally, `p_n<=p_0`, the second-moment bounds, and weak convergence imply

\[
 \int tH_{n+1}(t)dt
 =\int t p_n(t)dt-\int t C_n(t)dt
 \longrightarrow
 \int t p_\infty(t)dt-\int t\,d\mu(t)>0.
\]

This contradicts (4.4).  Therefore `A_infinity=0`, and
`||H_n||_1=2A_n` tends to zero. `square`

## 5. Rayleigh consequence

For the Rayleigh orbit, the original kernel and its first iterate have
positive-prefix/negative-tail sign order and therefore strictly negative
signed first moment.  The Rayleigh profile has moments of every order, so
Lemma 4.1 automatically propagates the compactness input (4.3).
Theorems 4.1--4.2 reduce `L1` decay to the single scalar invariant

\[
 \boxed{\sup_n\int_0^\infty tK_n(t)dt\le0.}       \tag{5.1}
\]

To upgrade that conclusion to the unit-block box norm still requires a
local regularity row, such as a common Lipschitz bound plus a common
Gaussian envelope.  Thus the full analytic orbit lemma is reduced to two
sharply separated invariants:

1. the scalar barrier (5.1), which already forces `L1` decay; and
2. a local `L1`-to-box compactness row, for example one common Lipschitz
   bound and one common Gaussian envelope for the complete kernels.

Under these two rows, the unit-block box convergence required by the
all-price theorem follows.

This is weaker than proving quantitative overlap at every step: arbitrarily
small intermediate overlap is allowed.  What must be excluded is exactly
escape to the sign-reversed fixed-point face.

Neither (5.1) nor the all-iterate local-regularity row is asserted here.  In
particular, this theorem does not prove the Rayleigh configuration
inequality or `nu(k)<=B(k)+O(1)` by itself.

## 6. Frozen dependency

`MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`,
SHA-256 at use:
`d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b`.
