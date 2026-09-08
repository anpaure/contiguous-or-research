# Final GO cross-audit: `1053/20000` Apéry price and period-26 positivity

**Date:** 2026-08-04  
**Verdict:** **GO after finite-certificate hardening.**  The exact
`18/1000000` compact-price margin survives, the residual margins are
exactly `68/1000000` and `302/1000000`, and the period-twenty-six theorem
follows within its stated honest exact-first-carry scope.

## 0. Audited object

Input:

- `MATH_THEOREM_APERY_GLOBAL_1053_OVER_20000_AND_PERIOD26_COMPLETE_POSITIVITY_20260804.md`,
  SHA-256
  `c18c2744a87be8b41c42e956b9a750338c0abe5f6fb72b2cf669923644af39c5`.

Audited successor:

- same filename, SHA-256
  `97182d953e89773b6b2c193348ccf9ae3c94c8d7267ddd9731c1a7dd0168e229`.

The successor adds explicit rational Taylor degrees and tail ratios; it
does not change the claimed price or either chamber margin.

The independent exact-rational verifier is
`scratch/audit_apery_global_1053_period26_exact_20260804.py`, SHA-256
`7afc32f0c68ef35fce9a3ef35ffce52a9a6ef6a6e96fce18ae6d1abdcbcdf150`.
It uses only Python integer/Fraction arithmetic and exits with
`exact rational audit: PASS`.

## 1. Jacobi identity and differentiation

On `0<=x<=2/13<1/5`, the frozen Jacobi dependency gives

\[
 f(x)=1-\Theta(x)+e^{-\pi x^2/4}
      +\sum_{j\ge2}e^{-\pi(j-x)^2/4},
 \qquad |\Theta(x)-2|<1/20000.
\]

The Gaussian series and its first two derivatives converge uniformly on
this compact interval, so termwise differentiation is legitimate.  For

\[
 Q(t)=(\pi^2t^2/4-\pi/2)e^{-\pi t^2/4},
\]

one obtains

\[
 J''(x)=Q(x)+\sum_{j\ge2}Q(j-x),
 \qquad
 Q'(t)={\pi^2t\over8}(6-\pi t^2)e^{-\pi t^2/4}.
\]

Thus `Q` increases on `[0,2/13]` and is positive and decreasing from
`24/13` onward.

## 2. Exact concavity certificate

Write `pi_-=333/106`, `pi_+=355/113`, and let `P_n,U_n` be the lower and
upper positive Taylor bounds defined in the corrected theorem.

At the negative endpoint,

\[
 {\pi_-/2-\pi_-^2/169\over U_1(\pi_+/169)}>7/5
\]

by exact cross multiplication.  The coefficient
`pi/2-pi^2/169` increases throughout the rational `pi` bracket, so this
proves `Q(2/13)<-7/5`, and monotonicity gives `Q(x)<-7/5` on the whole
interval.

For positive `Q`, exact rational checks give

\[
 {\pi_+^2t^2/4-\pi_+/2\over P_n(\pi_-t^2/4)}<c
\]

for `(t,n,c)` equal to

\[
 (24/13,5,1/2),\quad (37/13,8,1/25),\quad
 (50/13,7,1/200).
\]

For `t>=50/13`, the ratio `Q(t+1)/Q(t)` is below `1/2`: its rational
coefficient ratio is below `2`, and its exponential ratio is below `1/4`
because the relevant degree-one Taylor polynomial already exceeds `4`.
Consequently

\[
 \sum_{k\ge0}Q(50/13+k)<{1/200\over1-1/2}=1/100.
\]

It follows that

\[
 \sum_{j\ge3}Q(j-x)<1/25+1/100=1/20
\]

and therefore

\[
 J''(x)<-7/5+1/2+1/20=-17/20<-1/2.
\]

Every direction of the Gaussian reciprocal inequalities was checked:
upper Gaussian bounds use `P_n(pi_- c)`, while lower Gaussian bounds use
`U_n(pi_+ c)`.

## 3. Value and derivative at `1/8`

The four upper Gaussian certificates use degrees `2,14,20,22` at the
lower rational exponents

\[
 333/27136, 74925/27136, 176157/27136, 320013/27136.
\]

The first omitted term has lower exponent `506493/27136`.  Degree 18,
together with a successor ratio below `1/100`, proves both the unweighted
tail bound

\[
 \sum_{j\ge5}e^{-\pi(j-1/8)^2/4}<10^{-6}
\]

and, using the displayed `39/8` factor, the weighted derivative-tail bound
below `10^{-6}`.  Summing the four term bounds and the tail gives exactly

\[
 987810+63240+1520+10+1=1052581
\]

over denominator one million.  Hence

\[
                         J(1/8)<1.052581.
\]

The lower Gaussian brackets are independently certified by
`U_1,U_8,U_12,U_15` at the upper rational exponents.  Substitution into the
square bracket `B` in the derivative formula gives

\[
 -{4713\over8000000}<B<-{1961\over4000000}<0.
\]

Since `pi/2<355/226`,

\[
 J'(1/8)>{355\over226}\left(-{4713\over8000000}\right)
 =-{334623\over361600000}>-1/1000,
\]

while the upper bracket proves `J'(1/8)<0`.  For orientation only, a
high-precision recomputation gives approximately
`J'(1/8)=-0.0008706709`; this decimal is not used in the proof.

## 4. Tangent envelope and the fail-closed price margin

The strict concavity bound yields

\[
 J(x)\le J(1/8)+J'(1/8)(x-1/8)-{1\over4}(x-1/8)^2.
\]

For any real `y`, the maximum of `ay-y^2/4` is `a^2`.  Since
`|J'(1/8)|<1/1000`, its contribution is below `1/1000000`.  Therefore

\[
 J(x)<{1052582\over1000000},
\]

and the theta error gives

\[
 f(x)<{1052582\over1000000}-1+{1\over20000}
 ={52632\over1000000}
 \qquad(0\le x\le2/13).
\]

The critical price comparison is exact:

\[
 {1053\over20000}-{52632\over1000000}
 ={18\over1000000}>0.
\]

Thus the requested `18e-6` margin survives without rounding.

On `[2/13,1/2]`, the frozen period-26 dependency supplies both
`f'(x)<0` and `f(2/13)<523/10000`.  Hence

\[
 f(x)\le f(2/13)<0.0523<0.05265={1053\over20000}.
\]

This verifies the extension to the entire compact half interval; no
concavity claim is extrapolated past `2/13`.

## 5. Exact three-row repricing

In each frozen residual slack functional, only
`R_1,R_2,R_3` equal the old global price `G=533/10000`; rows four onward
use their separate anchors.  Replace exactly those three entries by
`G_*=1053/20000`.  Each changed slack remains nonnegative because it is

\[
 f(X_i)-L+G_*-f(Y_i),
\]

with the frozen compact floor and the newly proved global upper price.
Every theta, middle-train, late-pair, and rows-four-through-seven term is
unchanged.

The exact gain is

\[
 3(G-G_*)=3(1066-1053)/20000
 ={1950\over1000000}.
\]

Substitution into the frozen identities gives

\[
 E(s)={-1882+1950\over1000000}+\mathcal S_6^*
 ={68\over1000000}+\mathcal S_6^*,
\]

and

\[
 E(s)={-1648+1950\over1000000}+\mathcal S_7^*
 ={302\over1000000}+\mathcal S_7^*.
\]

Both new slack functionals are nonnegative.  The `68e-6` and `302e-6`
margins are therefore literal strict residual margins, not rounded
estimates.

## 6. Final scope verdict

The authenticated period-26 reduction already closes all chambers except
`R_6,R_7`.  The preceding positive identities close those two, and the
frozen comparison `Phi(W)>=E(s)` proves `Phi(W)>0`.

Accordingly:

- **GO:** global compact price `1053/20000` on `[0,1/2]`;
- **GO:** exact repricing of only the first three rows;
- **GO:** residual margins `68/1000000` and `302/1000000`;
- **GO:** complete period-26 positivity for honest exact-first-carry
  formal cyclic Apéry clocks;
- **NO CLAIM:** overshoot, later first crossing, physical shoulders,
  arbitrary periods, or an OR-word construction.

## 7. Frozen dependencies

- `MATH_THEOREM_APERY_PERIOD26_SHARP_DEPTH_AND_TWO_RESIDUAL_THRESHOLD_CHAMBERS_20260804.md`,
  SHA-256
  `15777eb5978671af4ce685f9760fc1c2a1cef25e424cafe7deda8bc004cdee2f`;
- `MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md`,
  SHA-256
  `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a`.
