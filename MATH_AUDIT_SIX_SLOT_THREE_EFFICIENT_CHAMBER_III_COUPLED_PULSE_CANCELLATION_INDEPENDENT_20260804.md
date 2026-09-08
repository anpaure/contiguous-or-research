# Independent audit: six-slot `h=3` chamber-III coupled pulse cancellation

**Date:** 2026-08-04  
**Method:** pure calculus and rational exponential estimates only; no
numerical search or enumeration.  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_III_COUPLED_PULSE_CANCELLATION_20260804.md`  
**Audited source SHA-256:**
`4e53e83f9912b3e8ec42eacf9dff1065d71d649be5cc8f4400f0223cbba8b811`

## Verdict

**PASS as an exact reduction.**  The two individually adverse finite
pulses have a jointly nonnegative sum.  The remaining prethreshold
repeated-gap train is not signed.

## 1. Coordinate and domain audit

With

\[
 c=2b-p,\qquad\beta=p-b,
\]

one has `p=c+2\beta`, `b=c+\beta`, and the chamber inequalities give

\[
 0\le a\le c\le p/3,
 \qquad
 2c+3\beta=p+b<A.
\]

Thus `c<=beta`, `A/2<=p<2A/3`, and
`c<2A-3p`.  The two finite differences combine exactly as

\[
 Q(a)-Q(c),
 \qquad
 Q(z)=K(p+z)+K(2p+z).
\]

No term has been dropped in this recombination.

## 2. Auxiliary `h` inequality

For `h(s)=s exp(-pi s^2/4)`, direct differentiation gives

\[
 h''(s)={\pi\over2}s\left({\pi s^2\over2}-3\right)
 e^{-\pi s^2/4}.
\]

Therefore

\[
 f(r)=h(r)-h(2-r)-h(5/2-r)
\]

is strictly concave on `[1/5,1/2]`: the first second derivative is
negative and the other two are positive because their arguments are at
least `3/2>sqrt(6/pi)`.

The two endpoint identities in the source are exact.  Their rational
certificates also check:

- `(331/45)(54853/24576)>16`, giving the stated `r=1/2` bound;
- `(331/45)(25673/15625)>12` and
  `20(12/5)=48`, giving the stated `r=1/5` bound.

Hence both endpoint values are positive, and strict concavity places the
whole graph above their chord.  The claimed inequality for `h` follows.

## 3. Coupled derivative

For `0<=z<=c`, `p+z<A` is compact while `2p+z>=A` is in the tail.  Put

\[
 t=p/A,\qquad\zeta=z/A,\qquad r=1-t-\zeta.
\]

The domain gives

\[
 1/2\le t<2/3,
 \qquad
 0\le\zeta\le\min\{t/3,2-3t\},
\]

and therefore

\[
 1/5\le r\le1/2.
\]

Differentiating the compact and tail kernels gives exactly

\[
 {Q'(z)\over2A}=h(2-r)-h(r)+h(2+t-r).
\]

Since `t>=1/2` and `h` is decreasing on `[2,\infty)`,

\[
 h(2+t-r)\le h(5/2-r).
\]

The auxiliary inequality then makes `Q'(z)<0`.  Because `a<=c`, this
proves `Q(a)-Q(c)>=0`, with equality exactly at `a=c`.

## 4. Residual domain and scope

Projecting away `a` leaves exactly

\[
 c\ge0,
 \quad c\le\beta,
 \quad A/2\le c+2\beta,
 \quad2c+3\beta<A.
\]

These inequalities also imply `c+2\beta<A`, so no omitted original
period constraint is needed.  The source proves only that chamber III is
bounded below by the pulse-free train on this domain.  It does not prove
that train positive or close any other chamber.
