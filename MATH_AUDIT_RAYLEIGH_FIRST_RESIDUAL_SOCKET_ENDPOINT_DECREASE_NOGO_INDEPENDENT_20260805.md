# Independent audit: first Rayleigh residual socket endpoint decrease

**Date:** 2026-08-05  
**Method:** independent pure-mathematical replay; no search or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`  
**Audited source SHA-256:**
`78e017354f77b21e6ba0c53301027e25cec3ffd020872727cbe9aab8802469c7`  
**Verdict:** **GO with no correction.**  The derivative identity and the
rational endpoint certificate imply `g_2'(b-)<0`.  This kills only the
whole-law increasing-density Wang--Wang shortcut; layer or role
decompositions remain live.

## 1. Second derivative identity

At an equal-level pair put

\[
 a=K'(r)>0,\qquad q=-K'(\ell)>0.
\]

Since

\[
 {dr\over du}={1\over a},\qquad
 {d\ell\over du}=-{1\over q},
\]

one has

\[
 {da\over du}={K''(r)\over a},\qquad
 {dq\over du}={K''(\ell)\over q},\qquad
 {dt\over du}={1\over a}+{1\over q}.
\]

Differentiating `u'=aq/(a+q)` first with respect to `u` and then dividing
by `dt/du` gives exactly

\[
 u''(t)={q^3K''(r)+a^3K''(\ell)\over(a+q)^3}.
\]

All orientations and powers are correct.

## 2. Endpoint bounds

At `t=b`, write `e=ell(u(b))` and `R=r(u(b))`.  The previously certified
rational brackets

\[
 0.46<b<0.48,\quad 0.55<e<0.60,\quad1.01<R<1.08
\]

and `4431/5000<A<8863/10000` place the arguments of
`Q'(x)=2(1-2x^2)e^{-x^2}` in compact rational intervals.  The stated
coarse consequences

\[
 K''(b)>0.19,\qquad K''(e)>0,\qquad-K''(R)<0.35
\]

and

\[
 a>0.075,\qquad q<0.28
\]

are directionally consistent and have ample margin under the same finite
Taylor enclosure used in the source.  In particular,

\[
 {q\over a+q}<{56\over71}.
\]

Because `K''(e)>0`, dropping the positive `a^3K''(e)` term from the
numerator gives

\[
 -u''(b)<(-K''(R))\left({q\over a+q}\right)^3
 <0.35\left({56\over71}\right)^3<0.172.
\]

Therefore

\[
 g_2'(b-)=-K''(b)-u''(b)<-0.19+0.172<0.
\]

The strict endpoint decrease is proved.

## 3. Scope

The density starts at zero and is positive inside `(0,b)`, while it is
strictly decreasing near `b`.  Hence it cannot be used whole as a
nondecreasing role law in the same-direction monotone-density theorem of
Wang--Wang.  No conclusion follows for a decomposition into monotone
subroles, the canonical uniform-superlevel layers, unequal role laws, or a
general configuration coupling.
