# Independent audit of the complete short-singleton repeated-gap closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The theorem proves `R(a,beta)>0` throughout its full
honest domain.  The proof uses neither the retracted reverse monotonicity
statement nor any finite search.

## Exact binding

Audited theorem:

`MATH_THEOREM_FIVE_SLOT_SHORT_SINGLETON_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md`

SHA-256:

`8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992`

### Byte-level rebind

The previously audited source had SHA-256

`dfe0b02d66a3e895fe78e04bd8ca8b48224de8b4b08617c1c9bb13b482f7d659`.

The current source differs in exactly one formatting byte in (4.9): the
old literal text was

```text
F_A(v)<{61\over1000}quad(0\le v\le2A/5)
```

and the current text is

```text
F_A(v)<{61\over1000}\quad(0\le v\le2A/5).
```

This was checked exactly by deleting that single backslash from the
current byte stream: its SHA-256 becomes the old bound hash `dfe0b02d...`.
No mathematical token, inequality, domain, proof step, or scope statement
otherwise changed.  The audit below therefore applies verbatim to the
current source.

## 1. Coordinates and exact domain

Put

\[
 y=a+\beta,\qquad b=\beta=y-a,
 \qquad u=a/A,qquad p=(2y-a)/A=(y+b)/A.
\]

Then

\[
 a\ge0\iff u\ge0,
 \qquad
 a\le\beta\iff p\ge3u,
\]

\[
 2a+2\beta<A\iff p+u<1,
 \qquad
 A<2a+3\beta\iff3p+u>2.
\]

Existence of such a nonnegative `u` implies `3/5<p<1`, and

\[
 0\le u\le\min\{p/3,1-p\}.
\]

The second upper inequality is strict in the honest domain; adjoining it
with equality only enlarges the closure used for the lower estimate.  The
switch of the two upper bounds occurs at `p=3/4`, exactly as stated.

For fixed `y`,

\[
 H_y(b)=\mathcal L_3(y+b;y-b,y)
\]

is precisely the original train.

## 2. Derivative and retained blocks

Termwise differentiation at fixed `y` gives

\[
\begin{aligned}
H_y'(b)={}&-K'(y-b)+K'(y+b)+K'(2y+b)\\
&+\sum_{q\ge2}\{qK'(q(y+b))
 +(q-1)K'(q(y+b)+y-b)\\
&\hspace{35mm}+qK'(q(y+b)+y)\}.
\end{aligned}
\]

The `q=0,1` normalized arguments are `u`, `p`, and `(3p+u)/2`.
The complete `q=2` arguments are `2p`, `2p+u`, and `(5p+u)/2`, with
coefficients `2,1,2`.  Since `3p+u>2`, the shifted `q=1` argument is on
the Gaussian tail; every `q>=2` argument is there as well.  Every omitted
`q>=3` term has positive coefficient and positive tail derivative.
Therefore

\[
 {H_y'(b)\over2A}>
 D(p)-D(u)+h(1+(3p+u)/2)+2h(1+2p)
 +h(1+2p+u)+2h(1+(5p+u)/2).
\]

The domain gives `u<=1/4`; monotonic decrease of `K` there gives
`D(u)<=0`.  It is consequently sufficient to sign the displayed `J(p,u)`.

All three `u`-dependent `h` arguments exceed the maximum point of `h`, so
`J` decreases in `u`.  Its closure minimum is at

\[
 u_*(p)=p/3\quad(3/5\le p\le3/4),
 \qquad
 u_*(p)=1-p\quad(3/4\le p\le1),
\]

which yields exactly the two functions `J_-` and `J_+` in the theorem.

## 3. Convexity and derivative orientation

For `p` in either strip, `1+p>sqrt(6/pi)` and `1-p<=2/5`, so

\[
 D''(p)=h''(1+p)-h''(1-p)>0.
\]

Every other affine argument in `J_-` and `J_+` is at least two, where
`h''>0`; the positive squares of the affine slopes preserve the sign.
Thus both functions are strictly convex.

The auxiliary enclosure for `rho=e^{-pi/64}` is exact.  From
`pi<22/7`, the exponential-tail bound

\[
 e^{11/224}<1+{11\over224}
 +{(11/224)^2/2\over1-(11/224)/3}
 ={311033\over296128}<{125\over119}
\]

gives `119/125<rho`.  From `pi>333/106`, the degree-three positive
Taylor polynomial at `333/6784` is

\[
 {655851065159\over624435396608}>{522\over497},
\]

giving `rho<497/522`.

Independent exact cross-multiplication verifies all three displayed
rational certificates (3.7)--(3.9).  Their respective positive rational
margins are approximately `0.0277`, `0.0494`, and `0.0196`; the signs are
those stated in the theorem.

Using `3<pi<22/7`, certificate (3.7) upper-bounds the sole positive
`h'(1/4)` term and lower-bounds all five negative magnitudes, proving
`J_-'(3/4)<0`.  Certificate (3.8) makes the reverse safe estimates and
proves `J_+'(3/4)>0`.  Strict convexity then makes `J_-` decrease toward
`3/4` and `J_+` increase away from it.  Both attain their common minimum
there.

Multiplication of that common value by `4/rho` gives exactly

\[
 -1+7\rho^{48}+9\rho^{80}+20\rho^{99}
 +11\rho^{120}+24\rho^{143}.
\]

Certificate (3.9), `rho>119/125`, and the final positive term make this
strictly positive.  Hence `J>0` and therefore `H_y'(b)>0` throughout the
honest quadrilateral.

## 4. Lower boundaries

The original domain in `(y,b)` is

\[
 A/3<y<A/2,qquad
 b\ge y/2,qquad b>A-2y,qquad b\le y.
\]

For `y>2A/5`, the included lower boundary is `b=y/2`; at `y=2A/5`
it is approached from above.  Writing `s=y/2` gives the exact interlacing

\[
 H_y(y/2)=\sum_{q\ge0}\{K(3qs)+K((3q+1)s)+K((3q+2)s)\}=C(s)>0.
\]

For `A/3<y<=2A/5`, approach `b=A-2y` and set

\[
 v=A-2y,qquad a=3y-A.
\]

Then `0<=a<=v<=A/3` and `2a+3v=A`.  The compact reduction and continuity
give

\[
 H_y(A-2y)\ge C+F_A(a)-F_A(v)-2\varepsilon.
\]

The correctly oriented endpoint-minimum statement is

\[
 F_A(a)\ge\min\{C,F_A(v)\}.
\]

If `F_A(v)<=C`, the train is at least `C-2 epsilon>0`.  If
`F_A(v)>C`, the audited bounds `C>43/1000`, `F_A(v)<61/1000`, and
`2 epsilon<1/10000` give

\[
 H_y(A-2y)>86/1000-61/1000-1/10000
 ={249\over10000}>0.
\]

There is no reversed endpoint-minimum use.

## 5. Conclusion and updated frontier

For each fixed `y`, strict increase in `b` and positivity of the relevant
lower boundary prove `R(a,beta)>0` everywhere on its honest domain.

Thus the full short-singleton gate is closed.  Together with the audited
small-`a` long-singleton theorem, the only remaining five-slot analytic
region is

\[
 A/8<a<A/4,qquad
 \max\{3a,A-2a\}<p<A-a
\]

for the long-singleton train `P(p,a)`.  Complete five-slot positivity is
not yet proved.
