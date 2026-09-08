# Independent fail-closed audit: `h=4` rectangle upper convexity and KKT pruning

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_H4_RECTANGLE_UPPER_CONVEXITY_AND_KKT_PRUNING_20260804.md`  
**Audited SHA256:**
`07bc659e3a1eb6b0dbdab562559d2968de2af6c685d688e0ab6874b598594ff1`

## Verdict

**FAIL CLOSED as written, on one endpoint-strictness statement only.**
The curvature estimate, the complete tail ratio, branch-`C` elimination,
branch-`U` signed stationarity and period residual, and the finite KKT scope
are otherwise correct.  Replacing the false strict endpoint assertion by
the weak endpoint inequality (or assigning the endpoint to the first
ratio case) repairs the proof without changing any constant or conclusion.

## 1. Exact failing line

In Lemma 1.3 put `t=tau/A`.  The second ratio case states

\[
6/5\le t\le3/2\quad\Longrightarrow\quad r^2>9\pi/4.
\]

At the admitted endpoint

\[
t=6/5,qquad q=1,qquad w=2\tau/3,
\]

the first tail argument is

\[
r=A+\tau+w=A+{5\tau\over3}=3A,
\]

and therefore

\[
r^2=9A^2={9\pi\over4},
\]

not strictly larger.

Either of the following exact repairs is sufficient:

1. use `1<=t<=6/5` and `6/5<t<=3/2`; or
2. retain the closed second interval and write
   `r^2>=9pi/4>2997/424`.

The latter still gives the strict rational estimate needed in (1.9),
because `pi>333/106` implies

\[
{9\pi\over4}>{2997\over424}.
\]

## 2. Curvature signs and constants

For `h(r)=r exp(-r^2)`, direct differentiation gives

\[
h'(r)=(1-2r^2)e^{-r^2},\qquad
h''(r)=2r(2r^2-3)e^{-r^2}.
\]

Thus the reflected second-derivative identity

\[
{1\over2}F_\tau''(w)=h'(A-w)+h'(A+w)
+\sum_{q\ge1}h'(A+q\tau+w)
\]

has the correct signs and multiplicities.

On the upper band, `0<=A-w<=A/3`, so `h'` decreases there and

\[
h'(A-w)\ge h'(A/3)>{3\over4}.
\]

For `A+w>=5A/3`, the adverse magnitude
`(2r^2-1)exp(-r^2)` decreases, and the certified endpoint bound gives

\[
h'(A+w)>-{2\over5}.
\]

Both rational cross-products are correct:

\[
{52\over63}{115\over126}={5980\over7938}>{3\over4},
\]

\[
{212\over63}{23\over200}={4876\over12600}<{2\over5}.
\]

## 3. Complete period tail

The first tail argument is at least `8A/3`, and every tail derivative is
negative.  Its first adverse magnitude is strictly below

\[
{641\over63\cdot260}.
\]

The two polynomial ratio bounds are correct:

\[
{49\over25}{32\over29}<{11\over5},\qquad
{100\over49}{2997\over2785}<{11\over5}.
\]

After either endpoint repair above, they cover the whole range
`A<=tau<=3A/2`.  The exponent gap is at least `19pi/12>19/4`, and the
positive exponential series gives `exp(19/4)>110`.  Hence every adverse
magnitude ratio is below `1/50`, and

\[
{641\over63\cdot260}{1\over1-1/50}<{1\over25}.
\]

Consequently the intended curvature conclusion is unchanged:

\[
{1\over2}F_\tau''(w)>{3\over4}-{2\over5}-{1\over25}
={31\over100},
\]

so `F_tau''(w)>31/50` on the complete upper band.

## 4. KKT pruning

At a smooth interior branch-`C` point,

\[
2\tau/3<P<P+u<A,
\]

and stationarity requires `T_tau(P)=T_tau(P+u)=0`.  Strict increase of
`T_tau` on that band forbids two distinct zeros, so branch `C` is removed.

On branch `U`, the two shift equations imply

\[
T_\tau(P)=T_\tau(u)=-T_\tau(P+u).
\]

Since `P+u>P` within the strict-convexity band,

\[
T_\tau(P)=T_\tau(u)<0<T_\tau(P+u).
\]

Also

\[
R_\tau(w)=\sum_{q\ge1}qK'(q\tau+w)>0
\]

for every rectangle shift.  The inactive `Gamma` side therefore cannot
satisfy the outer stationarity equation.  On the active side the remaining
equation is exactly

\[
R_\tau(0)+R_\tau(u)+R_\tau(P)+R_\tau(P+u)
=-{1\over2}T_A((A-\delta)/2).
\]

The signs and multiplicities are correct.

## 5. Scope

The theorem removes only smooth branch-`C` interiors and inactive-`Gamma`
branch-`U` interiors.  It retains boundary strata, low and `Gamma` switches,
and the active residual system.  Its finite KKT scope is therefore stated
correctly and does not claim full `h=4` positivity.

## Final disposition

Do not promote the audited SHA as exact theorem text.  After the one-line
endpoint repair, no further mathematical defect was found in the claimed
pruning result.
