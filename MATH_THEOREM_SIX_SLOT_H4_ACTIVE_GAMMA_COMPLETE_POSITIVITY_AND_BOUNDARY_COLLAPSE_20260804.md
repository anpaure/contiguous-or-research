# Six-slot `h=4`: complete positivity of the active-`Gamma` rectangle and boundary collapse

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It proves that
the literal correlated rectangle gate is uniformly positive on the whole
active side of its one-dimensional `Gamma` switch, including the switch
itself.  Combined with upper-band convexity, every remaining possible
minimum of the gate is therefore on the inactive side and on the explicit
boundary/nonsmooth list.  It does not sign those remaining boundary
strata, so complete six-slot `h=4` positivity is not claimed.  No search
or sampled computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0),
\tag{0.1}
\]

and write `F=F_A`.  The literal rectangle gate is

\[
\boxed{
\begin{aligned}
 \mathfrak R(\delta,P,u)={}&C(\tau)+F_\tau(P)+F_\tau(P+u)\\
 &+\min\{C(\tau),F_\tau(u)\}-\Gamma(\delta),
 \qquad \tau=A+\delta,
\end{aligned}}
\tag{0.2}
\]

on

\[
 {2\tau\over3}\le P\le A,
 \qquad
 0\le u\le\min\{A-P,P/4\},
\tag{0.3}
\]

where

\[
 v={A-\delta\over2},
 \qquad
 L={57\over1400},
 \qquad
 \Gamma(\delta)={1\over20000}+(F(v)-L)_+.
\tag{0.4}
\]

The preceding correlated theorem gives

\[
                 0<\Gamma(\delta)<{3147\over700000}.
\tag{0.5}
\]

We call `F(v)>=L` the closed active side; equality is the `Gamma` switch.

## 1. The active side is a narrow literal rectangle

### Lemma 1.1 (one-third anchor)

\[
                         \boxed{F(A/3)<{29\over750}<L.}
\tag{1.1}
\]

#### Proof

For `0<=w<=A`, the period-`A` train is

\[
 F(w)=1-e^{-(A-w)^2}-\sum_{n\ge1}e^{-(nA+w)^2}.
\tag{1.2}
\]

At `w=A/3`, retaining the first three adverse Gaussians gives

\[
 F(A/3)
 <1-e^{-\pi/9}-e^{-4\pi/9}-e^{-49\pi/36}.
\tag{1.3}
\]

Let

\[
 U_{24}(x)=\sum_{j=0}^{23}{x^j\over j!}
 +{x^{24}\over24!\,(1-x/25)}
\tag{1.4}
\]

for `0<x<25`, so `e^x<U_24(x)`.  The rational comparisons

\[
 U_{24}(22/63)<{1000\over703},
 \qquad
 U_{24}(88/63)<{200\over49},
 \qquad
 U_{24}(539/126)<75
\tag{1.5}
\]

are direct positive-integer cross multiplications.  Since `pi<22/7`,
they imply

\[
 e^{-\pi/9}>{703\over1000},
 \qquad
 e^{-4\pi/9}>{49\over200},
 \qquad
 e^{-49\pi/36}>{1\over75}.
\tag{1.6}
\]

Consequently

\[
 F(A/3)
 <1-{703\over1000}-{49\over200}-{1\over75}
 ={29\over750}<{57\over1400}.
\]

This proves (1.1). \(\square\)

### Corollary 1.2 (active localization)

On the closed active side `F(v)>=L`,

\[
 \boxed{
 v<{A\over3},
 \qquad
 \delta>{A\over3},
 \qquad
 \tau>{4A\over3},
 \qquad
 P>{8A\over9},
 \qquad
 0\le u<{A\over9}.}
\tag{1.7}
\]

#### Proof

The authenticated half-band theorem makes `F` strictly decreasing on
`[A/4,A/2]`.  Since `v` lies in that interval, Lemma 1.1 and `F(v)>=L`
give `v<A/3`.  The identities

\[
 \delta=A-2v,
 \qquad
 \tau=A+\delta
\]

give the next two inequalities.  Finally (0.3) gives

\[
 P\ge{2\tau\over3}>{8A\over9},
 \qquad
 u\le A-P<{A\over9}.
\]

This proves (1.7). \(\square\)

## 2. Three narrow-band train bounds

### Lemma 2.1 (ceiling bound)

If `tau>4A/3`, then

\[
                         \boxed{C(\tau)>{73\over1000}.}
\tag{2.1}
\]

#### Proof

The ceiling train is increasing in its period, so it is enough to bound
`C(4A/3)`.  The authenticated compact Gaussian bound gives

\[
 1-2e^{-\pi/4}>{881\over10000}.
\tag{2.2}
\]

At period `4A/3`, the first adverse tail is `e^{-49\pi/36}`.  The lower
bound `\pi>333/106` gives

\[
 {49\pi\over36}>{427\over100},
\]

and the finite positive Taylor polynomial satisfies

\[
                 \sum_{j=0}^{12}{(427/100)^j\over j!}>70.
\tag{2.3}
\]

Thus the first tail is smaller than `1/70`.  Every successive exponent
gap is at least `2\pi`.  Moreover `\pi>157/50`,

\[
 e^2>\sum_{j=0}^{5}{2^j\over j!}>{29\over4},
\]

and

\[
 e^{2\pi}>e^{6+7/25}
 >\left({29\over4}\right)^3
  \left(1+{7\over25}+{1\over2}{49\over625}\right)>500.
\tag{2.4}
\]

Hence the complete tail is smaller than

\[
 {1/70\over1-1/500}<{1\over69}.
\]

It follows that

\[
 C(\tau)>C(4A/3)
 >{881\over10000}-{1\over69}>{73\over1000}.
\]

This proves (2.1). \(\square\)

### Lemma 2.2 (upper rectangle shifts)

If

\[
 \tau\ge{4A\over3},
 \qquad
 {8A\over9}\le w\le A,
\]

then

\[
                         \boxed{F_\tau(w)>-{13\over250}.}
\tag{2.5}
\]

#### Proof

Write `w=At`.  On `8/9<=t<1`, the ratio of the positive to the adverse
term in `K'(At)/(2A)` is

\[
 {1+t\over1-t}e^{-\pi t}.
\tag{2.6}
\]

Its logarithmic derivative is

\[
 {2\over1-t^2}-\pi
 \ge {162\over17}-{22\over7}>0.
\]

At `t=8/9`, it exceeds one because

\[
 e^{8\pi/9}<e^{14/5}<17;
\tag{2.7}
\]

the last inequality follows directly from the degree-24 Taylor majorant
`U_24(14/5)<17`.  Therefore `K` is increasing on `[8A/9,A]`.

At the left endpoint,

\[
 K(8A/9)=1-e^{-\pi/324}-e^{-289\pi/324}.
\tag{2.8}
\]

Since `157/50<\pi<22/7`, put `x=\pi/324`.  Then

\[
 {157\over16200}<x<{1\over100},
\]

so

\[
 1-e^{-x}>x-{x^2\over2}
 >{199\over200}{157\over16200}>{6\over625}.
\tag{2.9}
\]

Also

\[
 {289\pi\over324}>{14\over5},
 \qquad
 \sum_{j=0}^{8}{(14/5)^j\over j!}>{1000\over61},
\]

and hence

\[
                         e^{-289\pi/324}<{61\over1000}.
\tag{2.10}
\]

It remains to bound the period tail.  Its first argument is at least
`29A/9`, and the gap between successive squared arguments is at least
`70\pi/27`.  The estimates

\[
 {841\pi\over324}>8+{3\over20},
 \qquad
 {70\pi\over27}>8+{19\over135},
\tag{2.11}
\]

together with `e^2>29/4` give

\[
 e^{841\pi/324}
 >\left({29\over4}\right)^4{23\over20}>3000,
\]

and

\[
 e^{70\pi/27}
 >\left({29\over4}\right)^4{154\over135}>3000.
\tag{2.12}
\]

Thus the complete period tail is smaller than

\[
 {1/3000\over1-1/3000}={1\over2999}<{1\over2500}.
\]

Combining monotonicity of `K` with (2.8)--(2.12),

\[
 F_\tau(w)
 >{6\over625}-{61\over1000}-{1\over2500}
 =-{259\over5000}>-{13\over250}.
\]

This proves (2.5). \(\square\)

### Lemma 2.3 (low rectangle shift)

On the closed active side,

\[
 \boxed{
 \min\{C(\tau),F_\tau(u)\}>L={57\over1400}.}
\tag{2.13}
\]

#### Proof

Lemma 2.1 gives `C(tau)>73/1000>L`.  By Corollary 1.2,
`0<=u<A/9<A/4`.  Increasing the period moves every negative tail away,
so

\[
                         F_\tau(u)>F_A(u).
\]

The authenticated quarter-band floor gives `F_A(u)>L` on
`[0,A/4]`.  This proves (2.13). \(\square\)

## 3. Complete active-side positivity

### Theorem 3.1

On the entire closed active side `F(v)>=L`,

\[
 \boxed{
 \mathfrak R(\delta,P,u)>{3653\over700000}>0.}
\tag{3.1}
\]

#### Proof

Corollary 1.2 puts both `P` and `P+u` in `[8A/9,A]` and puts the period
above `4A/3`.  Lemmas 2.1--2.3 and (0.5) therefore give

\[
\begin{aligned}
 \mathfrak R
 &>{73\over1000}+{57\over1400}
   -2{13\over250}-{3147\over700000}\\
 &={3653\over700000}>0.
\end{aligned}
\]

This proves (3.1). \(\square\)

## 4. KKT consequence

The corrected upper-convexity theorem proves:

1. the constant-low branch has no smooth interior stationary point;
2. every moving-low smooth interior stationary point must have active
   `Gamma`;
3. every inactive-`Gamma` moving-low interior point fails the positive
   outer-period equation.

Theorem 3.1 now removes the whole active side, not merely its smooth
stationary points.  In particular the `Gamma` switch is strictly
positive.

### Corollary 4.1 (boundary collapse)

Every nonpositive global minimum of the correlated rectangle gate, if
one exists, lies on the inactive side `F(v)<L` and on at least one of the
following strata:

\[
\begin{gathered}
 \delta=\delta_*,
 \qquad
 P={2\tau\over3},
 \qquad
 P=A,\\
 u=0,
 \qquad
 u=A-P,
 \qquad
 u=P/4,\\
 P={4A\over5},
 \qquad
 F_\tau(u)=C(\tau).
\end{gathered}
\tag{4.1}
\]

At intersections, the appropriate one-sided conditions apply.  There is
no remaining smooth interior KKT locus and no remaining `Gamma`-switch
locus.

The far endpoint is excluded by the earlier uniform far-end theorem.
The initial endpoint `delta=delta_*` is retained because the earlier
local theorem proves positivity of physical tables there, not by itself
positivity of this stronger sufficient gate.

## 5. Exact scope

This theorem proves:

1. an explicit one-third anchor `F(A/3)<29/750`;
2. exact localization of active `Gamma` to
   `tau>4A/3`, `P>8A/9`, `u<A/9`;
3. a uniform active-side rectangle margin `3653/700000`;
4. removal of the complete smooth interior and `Gamma`-switch loci;
5. reduction of the residual gate to the finite inactive boundary list
   (4.1).

It does not sign those boundary strata and therefore does not yet prove
complete six-slot `h=4` positivity.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| corrected literal rectangle gate | `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| corrected upper-convexity/KKT pruning | `MATH_THEOREM_SIX_SLOT_H4_RECTANGLE_UPPER_CONVEXITY_AND_KKT_PRUNING_20260804.md` | `6f8daaba40de9d40c17d429fa4925d4d985d3374fa00d89a5d05651b2529aa11` |
| quarter floor and compact Gaussian prices | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
