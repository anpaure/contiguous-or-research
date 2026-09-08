# Independent audit of exact-theta endpoint descent for the repeated-gap gates

**Date:** 2026-08-04  
**Verdict:** **GO as an exact reduction.**  The reflection identity, both
gate inequalities, and the corrected threshold-period obstruction are
sound.  Neither gate is thereby proved positive.

## Exact bindings

Primary theorem:

`MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md`

SHA-256:

`0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff`

Boundary obstruction:

`MATH_OBSTRUCTION_FIVE_SLOT_LONG_SINGLETON_ENDPOINT_DESCENT_BOUNDARY_20260804.md`

SHA-256:

`92c0e145cdd9adbb309a77b71e6b089c48b4289dc5aa5604100c8284c26dc328`

## 1. Exact reflection identity

For `w=At`, the half-train completion is

\[
 F(At)=1-\Theta(t)+e^{-\pi t^2/4}
       +\sum_{j\ge2}e^{-\pi(j-t)^2/4}.
\]

At `1-t`, periodic reflection gives `Theta(1-t)=Theta(t)`.  The two
positive Gaussian banks in the two completions combine to

\[
 e^{-\pi t^2/4}
 +\sum_{j\ge1}e^{-\pi(j-t)^2/4}
 +\sum_{j\ge1}e^{-\pi(j+t)^2/4}
 =\Theta(t).
\]

Hence

\[
 F(w)+F(A-w)=2-\Theta(w/A)=\rho(w)
\]

exactly, including `w=0,A`.

Poisson summation with Gaussian parameter `pi/4` gives

\[
 \Theta(t)=2+4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt),
\]

so

\[
 \rho(w)=-4\sum_{m\ge1}e^{-4\pi m^2}
              \cos(2\pi mw/A).
\]

The correct global bound is `|rho(w)|<=epsilon`; equality occurs at
`w=0` (and `A`).  This weak inequality is now stated correctly in the
source.

## 2. Short-singleton gate

With `y=a+beta`, `v=A-2y`, and `u=v+a`, the original domain is equivalent
to

\[
 0<v<A/3,qquad0\le a\le(A-v)/4,qquad2a+3v<A.
\]

Indeed `v>0` is `2y<A`, `2a+3v<A` is `A<3y-a`, and the weak upper bound
on `a` is exactly `a<=beta`.

The clock begins

\[
 0,a,y,2y-a,2y,3y-a.
\]

Its first five entries are below `A` and its sixth above `A`.  The
threshold-period endpoint-descent bound is

\[
 R\ge C+F(a)+F(y)+F(2y-a)+F(2y).
\]

Since `2y-a=A-(v+a)`, `2y=A-v`, and `y=(A-v)/2`, exact reflection gives
precisely

\[
 R\ge C+F(a)+F((A-v)/2)-F(v)-F(v+a)
       +\rho(v)+\rho(v+a)=\widetilde Q_R.
\]

The direction is weak `>=`, as correctly stated.

## 3. Long-singleton gate

For `t=A-p-a`, the unresolved domain is exactly

\[
 0<t<a<A/4,qquad4a+t<A.
\]

The equivalences are `t>0 <=> p<A-a`, `t<a <=> p>A-2a`, and
`4a+t<A <=> p>3a`.  The clock

\[
 0,a,2a,p,p+a,p+2a
\]

again has five entries below `A` followed by one above it.  Endpoint
descent and the identities `p=A-(a+t)`, `p+a=A-t` give

\[
 P\ge C+F(a)+F(2a)-F(t)-F(a+t)
       +\rho(t)+\rho(a+t)=\widetilde Q_P.
\]

No uniform reflection error and no no-interior-minimum comparison is used.

## 4. Boundary obstruction and exact scope

At the common limiting uniform clock

\[
 a=\beta=A/4,qquad p=3A/4,
\]

the actual train is `C(A/4)>0`.  The first five-point descent retaining
its true composite period `E=5A/4` is exact and gives this same positive
arithmetic clock.

Only the second monotone relaxation `F_E -> F_A` is obstructed.  Its
threshold-period train is

\[
 S=C+F(A/4)+F(A/2)+F(3A/4)+F(A).
\]

Reflection gives

\[
 S=\rho(0)+\rho(A/4)+{1\over2}\rho(A/2).
\]

The coefficient of `e^{-4 pi m^2}` is

\[
 -4-4\cos(\pi m/2)-2(-1)^m,
\]

equal to `-2` for odd `m`, `-2` for `m=2 mod 4`, and `-10` for
`m=0 mod 4`.  Thus `S<0` exactly as the obstruction file claims.

The corrected conclusion is therefore narrow: a full-domain proof cannot
uniformly replace the true endpoint period by `A`.  It may retain the
true composite period `E`, retain the original period-three phase, or use
a boundary-stable interpolation.  This is not an obstruction to composite
endpoint descent itself and not a counterexample to either repeated-gap
gate.

## 5. Frontier

The exact-theta formulas strictly strengthen the earlier coarse
`-2 epsilon` quadrilateral bounds but do not sign the remaining domains.
The long-singleton gate is separately closed for `0<a<=A/8`; its
large-`a` range and the full short-singleton gate remain open.  Hence
complete five-slot Bellman positivity is still not proved.
