# Independent audit: six-slot prethreshold half-period reduction and closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The two-variable repeated-gap gate is reduced
correctly to the half-period function, and the new two-compact train theorem
proves that function strictly positive.  The derivative identities, all
inequality directions, the rational Gaussian certificates, the endpoint
split, and the chamber-II/chamber-III substitutions have been checked
independently.  This closes only the shared repeated-gap residual; it does
not close the other chamber-II residuals or complete six-slot positivity.

## 1. Exact binding

Reduction theorem:

`MATH_THEOREM_SIX_SLOT_PRETHRESHOLD_REPEATED_GAP_HALF_PERIOD_REDUCTION_20260804.md`

SHA-256:

`c7479855908547c4d18ccc139d0df6880bb73905f93b7b9ba26683a841636286`

Closure theorem:

`MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md`

SHA-256:

`c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a`

The dependency hashes printed in the two notes agree with the current
workspace bytes.

## 2. Chamber domains and the fixed-sum change of variables

The chamber-II repeated-gap endpoint is

\[
 \mathcal L_3\!\left(P;a,{P+a\over2}\right)
\]

under

\[
 {A\over2}\le P<{2A\over3},\qquad
 0\le a\le {P\over3},\qquad 3P+a\le2A.
\]

For chamber III, putting `P=c+2 beta` and `a=c` sends

\[
 c\le\beta,quad {A\over2}\le c+2\beta,quad
 2c+3\beta<A
\]

to precisely the same domain, since

\[
 c\le {c+2\beta\over3},qquad
 3P+a=2(2c+3\beta)<2A.
\]

Now set

\[
 y={P+a\over2},\qquad b={P-a\over2}.
\]

Then `P=y+b`, `a=y-b`, and the four independent constraints become

\[
 b\le y,\quad b\ge {y\over2},\quad
 b\ge {A\over2}-y,\quad b\le A-2y.
\]

Feasibility gives `A/4 <= y <= 2A/5`, so the displayed domain (1.4) in
the reduction theorem is exact.  It includes the single closure point
`(P,a)=(2A/3,0)`; the theorem explicitly treats the threshold equality
face by continuity, while the physical chamber retains `P<2A/3`.

With

\[
 p={P\over A},\qquad u={a\over A},\qquad
 r={3p+u\over2},
\]

one obtains

\[
 {1\over2}\le p\le {2\over3},\quad
 0\le u\le {p\over3},\quad 3p+u\le2.
\]

The maximum possible `u` is `1/5`, attained where
`p/3=2-3p`, namely at `p=3/5`.

## 3. Exact derivative and favorable-row audit

For fixed `y`, differentiating

\[
 H_y(b)=F_{y+b}(0)+F_{y+b}(y-b)+F_{y+b}(y)
\]

gives exactly

\[
\begin{aligned}
 H_y'(b)={}&-K'(y-b)+K'(y+b)+K'(2y+b)\\
 &+\sum_{q\ge2}\bigl(qK'(q(y+b))
 +(q-1)K'(q(y+b)+y-b)\\
 &\hspace{39mm}+qK'(q(y+b)+y)\bigr).
\end{aligned}
\]

All `q>=3` arguments are strictly beyond `A`, their coefficients are
positive, and the tail derivative `K'` is positive.  Dropping them
therefore gives a strict **lower** bound.  The complete `q=2` row and the
three compact terms yield exactly the function `J(p,u)` in (2.4).

For `0<=u<=1/5`,

\[
 {h(1+u)\over h(1-u)}
 ={1+u\over1-u}e^{-\pi u}<1,
\]

so `-D(u)>=0`.  The proof that `D` increases on `[3/4,1]` also checks:
`h'(1-x)>4/5` and `-h'(1+x)<4/5` on that strip.  Consequently

\[
 D(r)\ge D(3p/2).
\]

Every retained `h` argument is at least two, where `h` decreases.
Replacing `u` by

\[
 u_*(p)=\min\{p/3,2-3p\}
\]

therefore again points in the lower-bound direction and gives exactly
`G_-` and `G_+`.

## 4. Convex strips and reproducible rational certificate

The identity

\[
 h''(x)={\pi\over2}x
 \left({\pi x^2\over2}-3\right)e^{-\pi x^2/4}
\]

implies

\[
 D''(x)=h''(1+x)-h''(1-x)>0
 \qquad(1/2\le x\le1).
\]

Every other term in `G_-` and `G_+` has argument at least two; affine
composition, including `h(3-p)`, preserves the positive second derivative.
Thus both strip functions are strictly convex.

The interval tables (3.5) and (3.9) are reproducible using rational
arithmetic alone as follows.  For rational `x`, put

\[
 z_x^-={157x^2\over200},\qquad
 z_x^+={11x^2\over14},
\]

and

\[
 E_-(z)=\sum_{j=0}^{41}{(-z)^j\over j!},\qquad
 E_+(z)=\sum_{j=0}^{40}{(-z)^j\over j!}.
\]

Then

\[
 xE_-(z_x^+)<h(x)<xE_+(z_x^-).
\]

For `h'(x)=g(z)=e^{-z}(1-2z)`, use that

\[
 g'(z)=e^{-z}(2z-3).
\]

None of the rational `z` intervals occurring in the two tables meets
`3/2`; evaluate `g` at the appropriate rational endpoint and multiply
`E_-` or `E_+` according to the sign of `1-2z`.  Clearing positive
factorial denominators gives every displayed interval.  This supplies
an exact endpoint recipe rather than a floating-point check.

Combining those intervals gives, at `p=23/40`,

\[
 G_-(23/40)>{15\over1000},
\]

and the sharper derivative enclosure

\[
 -{11\over300}<G_-'(23/40)<{101\over6000}.
\]

Hence `|G_-'(23/40)|<1/20`.  The tangent inequality and
`|p-23/40|<=3/40` prove `G_->1/160` on the whole first strip.

At `p=3/5`, direct interval aggregation gives

\[
 G_+(3/5)>{17\over1000},\qquad
 G_+'(3/5)>{1381\over2000}>{1\over2}.
\]

Convexity makes `G_+` increasing from that endpoint.  Therefore the
claimed strict sign `H_y'(b)>0` is proved on the full physical domain and
extends continuously to its threshold face.

## 5. Boundary split and the theta expression

The lower endpoint for `b` is `y/2` when `y>=A/3`.  With `s=y/2`, the
three residue classes are `0,s,2s` modulo `3s`, so

\[
 H_y(y/2)=C(s)>0.
\]

When `y<=A/3`, the lower endpoint is `A/2-y`, hence `P=A/2` and

\[
 u={2y\over A}-{1\over2}\in[0,1/6].
\]

This gives exactly the function `mathcal B` in (4.3).  Its endpoint
identities also check by residue splitting:

\[
 \mathcal B(0)=C(A/4)+C(A/2),\qquad
 \mathcal B(1/6)=C(A/6).
\]

Finally, `F_{A/2}(w)=f(w)+f(A/2+w)`.  Applying

\[
 f(w)+f(A-w)=\rho(w)
\]

to the two shifted terms yields every sign and argument in formula (4.8):

\[
\begin{aligned}
 \mathcal B(u)={}&f(0)+f(A/2)
 +f(Au)-f(A(1/2-u))\\
 &+f(A(1/4+u/2))-f(A(1/4-u/2))\\
 &+\rho(A(1/2-u))+\rho(A(1/4-u/2)).
\end{aligned}
\]

No interior sign is inferred at the reduction stage.

## 6. Independent audit of the half-period closure

Let `w=Ax`.  Rows zero and one of `F_{A/2}` are compact on
`0<=x<=1/3`; every later row is a tail row (with matching derivative at
the threshold endpoint).  Direct expansion gives

\[
 {F_{A/2}'(Ax)\over2A}
 =\sum_{q\ge0}h(1+x+q/2)-h(1-x)-h(1/2-x)=T(x).
\]

The displayed formula for `h'''` is correct.  On `[2/3,4/3]`, its
quadratic factor is positive, so `h''` increases there.  Hence

\[
 h''(1+x)-h''(1-x)\ge0.
\]

The `q>=1` second derivatives are positive because their arguments are
at least `3/2`, while `h''(1/2-x)<0`.  Thus `T''(x)>0` exactly as claimed.

At zero, the ratio estimate for the half-spaced tail gives

\[
 T(0)<h(3/2)+{4\over3}h(2)-h(1/2).
\]

After division by `h(1/2)`, the required inequality is

\[
 3e^{-\pi/2}+{16\over3}e^{-15\pi/16}<1.
\]

The two terms are respectively smaller than `2/3` and `1/3` by the
stated positive-series rational bounds, so `T(0)<0`.

At `x=1/3`, separating the first two terms and geometrically bounding the
tail from `7/3` gives

\[
 T(1/3)<h(4/3)+h(11/6)+{5\over4}h(7/3)
          -h(2/3)-h(1/6).
\]

The exact ratios are

\[
 {h(11/6)\over h(1/6)}=11e^{-5\pi/6}<1
\]

and

\[
 {h(4/3)+(5/4)h(7/3)\over h(2/3)}
 =2e^{-\pi/3}+{35\over8}e^{-5\pi/4}<1.
\]

All inequalities are strict.  The elementary claim `e^{15/4}>20` used
in the last estimate follows already from the positive exponential series
through degree eight at `3`, so it carries no numerical-search premise.

A convex function lies below its endpoint chord.  Since both endpoint
values are negative, `T(x)<0` throughout `[0,1/3]`.  Therefore

\[
 F_{A/2}'(w)<0\qquad(0\le w\le A/3).
\]

Both moving arguments of `mathcal B` lie in this interval, and so

\[
 \mathcal B'(u)=A F_{A/2}'(Au)
 +{A\over2}F_{A/2}'(A(1/4+u/2))<0.
\]

Since `mathcal B(1/6)=C(A/6)>0`, strict decrease proves
`mathcal B(u)>0` everywhere on `[0,1/6]`.

## 7. Exact conclusion and scope

The shared residual is now closed:

\[
 \mathcal L_3\!\left(P;a,{P+a\over2}\right)>0
\]

on the full prethreshold chamber-II domain, and therefore also for the
chamber-III substitution `P=c+2 beta`, `a=c`.

This result does **not** sign the chamber-II lower endpoint
`mathcal L_3(p;a,2a)` or its stationary compact strip.  It does not close
chamber I, complete six-slot positivity, the all-grid Bellman inequality,
or any OR-word construction.
