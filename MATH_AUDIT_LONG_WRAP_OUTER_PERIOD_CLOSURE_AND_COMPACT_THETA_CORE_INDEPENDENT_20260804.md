# Independent audit: long-wrap outer-period closure and normalized theta core

**Date:** 2026-08-04

**Audited source:**
`MATH_THEOREM_LONG_WRAP_OUTER_PERIOD_CLOSURE_AND_COMPACT_THETA_CORE_20260804.md`

**Original source SHA-256:**
`7d1f940220874fe2d0e218b3a5076e75fb612cc048200b19b05638d665c56cfa`

**Corrected source SHA-256:**
`c60b69aadd89815605be134162ade2c2355008ae9f34ee39d45bb3c5cef139b3`

**Method:** independent symbolic replay and exact rational arithmetic.  No
floating-point sign decision, parameter search, or remote computation was
used.

## 1. Verdict and required corrections

**GO after repair.**  The two asserted positive period regions are valid:

\[
 {A\over2}\le P\le {4A\over5},
 \qquad
 {11A\over12}\le P<A.
\]

The remaining KKT locus is correctly confined to

\[
 {4\over5}<P/A<{11\over12},
 \qquad 0<a/A<{1-P/A\over2}.
\]

The original source required four corrections.

1. Its advertised sharpened inequality

   \[
                          -h'(\rho)>-{39\over1000}
   \]

   is false at `rho=3/4`.  The valid coarser bound `>-1/10` is sufficient.
2. The claimed degree-24 certificate was not displayed in a reproducible
   form.  It has been replaced by explicit rational `S_N,E_N` enclosures,
   including the exact margin

   \[
                          U(4/5)<-{47\over15000}<-{1\over500}.
   \]
3. Numerous display equations in the latter half of the file lacked their
   closing delimiter.  These formatting failures are repaired.
4. Stationarity plus nonnegative second derivative is necessary, not by
   itself sufficient, for an interior local minimum.  The source now says
   that the unique possible local-minimum root necessarily satisfies the
   displayed KKT conditions rather than being characterized by them.

The phrase “compact band” was also narrowed to “bounded band whose closure
is compact”; the surviving KKT locus has not itself been proved closed.

## 2. Exact exponential enclosure

For rational `t>0`, define

\[
 S_N(t)=\sum_{k=0}^N{t^k\over k!},
 \qquad
 E_N(t)=S_N(t)+{t^{N+1}\over(N+1)!}
                       {1\over1-t/(N+2)}.
\]

When `t<N+2`, positivity of the exponential series gives

\[
                         S_N(t)<e^t<E_N(t).
\]

The upper bound follows because every ratio after the first omitted term
is at most `t/(N+2)`.  Every comparison below is therefore a finite rational
inequality.

The following complete arithmetic ledger was replayed by clearing positive
denominators:

| use | exact rational comparison |
|---|---|
| origin first term | `S_6(157/100)>24/5` |
| lower-period tail ratio | `(19/7) S_4(5/16)>11/3` |
| first endpoint at `3/5` | `S_6(9/5)>16/3` |
| second endpoint at `4/5` | `S_8(314/125)>12` |
| upper tail ratio | `S_8(8949/5000)>52/9` |
| derivative at `6/5` | `E_8(198/175)<25/8` |
| rejected `-39/1000` bound | `E_4(99/224)<5/3` |
| first weighted-tail term | `(19/7)^5 S_4(15/16)>2438/7` |
| weighted-tail ratio | `(19/7)^3 S_4(2/3)>(200/9)(71/55)^2` |
| `h(6/5)` | `S_6(1413/1250)>300/97` |
| `h(4/5)` | `E_6(88/175)<4000/2419` |
| `h(2)` | `S_12(333/106)>4000/173` |
| `h(14/5)` | `S_14(16317/2650)>1400/3` |
| first omitted endpoint ratio | `S_7(4)>360/7` |
| later endpoint ratios | `S_8(5)>1100/9` |
| derivative at `13/12` | `S_3(169/192)>(851/1008)(49/18)` |
| upper bound for `e^3` | `E_8(3)<201/10` |
| upper bound for `e^(1/7)` | `E_3(1/7)<7/6` |

The auxiliary estimate `e>19/7` is itself exact because

\[
                         e>S_5(1)={163\over60}>{19\over7}.
\]

This ledger replaces the opaque signed-Taylor assertion completely.

## 3. Audit of Lemma 1.1

At `x=0`, cancellation of the `q=0` term gives

\[
 T_\rho(0)=\sum_{q\ge1}h(1+q\rho)-h(1-\rho).
\]

The first-positive/adverse ratio is exactly

\[
 R_0(\rho)={1+\rho\over1-\rho}e^{-\pi\rho}.
\]

### The interval `1/2<=rho<=3/5`

Its logarithmic derivative is

\[
                         {2\over1-\rho^2}-\pi.
\]

This is negative because its maximum is `25/8-pi<0`.  Hence

\[
 R_0(\rho)\le3e^{-\pi/2}<{5\over8},
\]

using the first row of the ledger.

For every successive positive term, `z>=1+rho` gives

\[
 {h(z+\rho)\over h(z)}
 \le {11\over8}e^{-7\pi/16}<{3\over8}.
\]

Thus the whole positive train is less than `8/5` times its first term,
and `(8/5)(5/8)=1` proves the strict sign.

### The interval `3/5<=rho<=4/5`

The logarithmic derivative of `R_0` is increasing, so `log R_0` is convex
and its maximum on the interval occurs at an endpoint.  The exact endpoint
bounds are

\[
 4e^{-3\pi/5}<{3\over4},
 \qquad
 9e^{-4\pi/5}<{3\over4}.
\]

Also

\[
 1+{\rho\over z}\le{13\over9},
 \qquad
 2z\rho+\rho^2\ge{57\over25},
\]

so the successive ratio is less than `1/4`.  The entire train is less than
`4/3` times its first term, and `(4/3)(3/4)=1`.  Lemma 1.1 is therefore
strictly correct on the whole interval.

## 4. Audit and repair of Lemma 3.1

At the right compact endpoint,

\[
 U(\rho)=T_\rho(1-\rho)
 =h(2-\rho)-h(\rho)+\sum_{n\ge0}h(2+n\rho),
\]

and termwise differentiation gives

\[
 U'(\rho)=-h'(2-\rho)-h'(\rho)
              +\sum_{n\ge1}n h'(2+n\rho).
\]

### The two compact derivative terms

On `[6/5,5/4]`, `h''<0`, so `-h'` is increasing.  At the left endpoint,

\[
 -h'(6/5)=e^{-9\pi/25}\left({18\pi\over25}-1\right)
 >{8\over25}{5\over4}={2\over5}.
\]

The Gaussian bound uses `E_8(198/175)<25/8`; the polynomial bound uses
`pi>157/50>25/8` in the equivalent linear inequality.

Likewise `-h'` is increasing on `[3/4,4/5]`.  At `3/4`,

\[
 h'(3/4)<{64\over91}{1\over8}={8\over91}<{1\over10}.
\]

Thus `-h'(rho)>-1/10`.

The rejected `-39/1000` claim really is false, not merely unaudited.
Indeed `pi<22/7` gives

\[
 1-{9\pi\over32}>{13\over112},
 \qquad {9\pi\over64}<{99\over224},
\]

while `E_4(99/224)<5/3`.  Hence

\[
 h'(3/4)>{13\over112}{3\over5}
 ={39\over560}>{39\over1000}.
\]

### Weighted Gaussian tail

Put

\[
 H(z)=-h'(z)=e^{-\pi z^2/4}left({\pi z^2\over2}-1\right),
 \qquad a_n=nH(2+n\rho).
\]

The function `H` decreases beyond `11/4`.  The first term satisfies

\[
 a_1\le H(11/4)<{1\over32}.
\]

For `z>=11/4`, `rho<=4/5`, and `n>=1`, the polynomial ratio obeys

\[
 {n+1\over n}
 {\pi(z+\rho)^2/2-1\over\pi z^2/2-1}
 <{20\over9}\left({71\over55}\right)^2.
\]

The exponent gap is at least `75pi/64>11/3`.  The corresponding ledger row
therefore gives

\[
                         {a_{n+1}\over a_n}<{1\over10}.
\]

Consequently

\[
 -\sum_{n\ge1}n h'(2+n\rho)
 <{1/32\over1-1/10}={5\over144}<{1\over20}.
\]

Combining the three strict estimates yields `U'>1/4`.

### Exact endpoint margin

The rational exponential ledger gives

\[
 \begin{aligned}
 h(6/5)&<{97\over250},&
 h(4/5)&>{2419\over5000},\\
 h(2)&<{173\over2000},&
 h(14/5)&<{3\over500}.
 \end{aligned}
\]

The first omitted tail ratio, from `14/5` to `18/5`, is below `1/40`;
all later ratios are below `1/100`.  Hence

\[
                         \sum_{n\ge2}h(2+4n/5)<{1\over6000}.
\]

Substitution gives the exact rational upper bound

\[
 \begin{aligned}
 U(4/5)
 &<{97\over250}-{2419\over5000}+{173\over2000}
       +{3\over500}+{1\over6000}\\
 &=-{47\over15000}<-{1\over500}.
 \end{aligned}
\]

Since `U` is increasing, `U(rho)<0` throughout `[3/4,4/5]`.

## 5. Audit of Lemma 4.1

Let `r=1-rho<=1/12` and `0<=x<=r`.  Retaining the first two positive
train rows gives

\[
 T_\rho(x)>D(x)+h(2-r+x)-h(r-x),
 \qquad D(x)=h(1+x)-h(1-x).
\]

On `[11/12,13/12]`, `h''<0`, so `h'` is decreasing.  At the right
endpoint,

\[
 -h'(13/12)
 <{851\over1008}{1\over S_3(169/192)}
 <{18\over49}<{1\over2}.
\]

Therefore `D(x)>=-x`.  Also

\[
 h(2-r+x)\ge h(2)=2e^{-\pi},
 \qquad h(r-x)\le r-x,
\]

and consequently

\[
                         T_\rho(x)>2e^{-\pi}-r.
\]

The exact upper exponential bounds

\[
 e^\pi<e^{22/7}=e^3e^{1/7}
 <{201\over10}{7\over6}={1407\over60}<24
\]

show `2e^(-pi)>1/12>=r`.  Hence `F_P'(w)>0` on the claimed complete
interval.

## 6. Convexity, chord, and domain audit

The imported theorem gives strict convexity of `w -> F_P'(w)` on
`[0,A-P]`.  Therefore

\[
 G_P(a)=F_P'(a)+2F_P'(2a)
\]

has

\[
                         G_P''(a)=F_P'''(a)+8F_P'''(2a)>0.
\]

A convex function lies below the chord joining its endpoint values, so
negative endpoint values imply negativity throughout.

The domain split is exact:

\[
 {P\over3}={A-P\over2}
 \quad\Longleftrightarrow\quad
                         P={3A\over5}.
\]

For `P/A in [1/2,3/5]`, the endpoint is `a=P/3`; both shifts `P/3,2P/3`
lie in the proved density-tie wedge and

\[
 Q_P(P/3)=C(P/3)
\]

by residue-class splitting.

For `P/A in [3/5,3/4]`,

\[
                         {P\over3}\le A-P\le{2P\over3},
\]

so the shift theorem signs `F_P'(A-P)`.  Lemma 1.1 signs `F_P'(0)`;
convexity signs the full interval.  For `P/A in [3/4,4/5]`, Lemma 3.1
replaces the right-endpoint sign.  Thus the two subranges meet without a
gap at `3/4` and close at `4/5`.

For `P/A>=11/12`, admissibility gives `0<=a<=2a<=A-P`, so Lemma 4.1
signs both terms of `Q_P'`.  The removed ranges and the surviving interval
are therefore exactly those claimed.

## 7. Normalized KKT residual

With `P=A rho` and `a=A x`,

\[
 {F_P'(Ax)\over2A}=T_\rho(x).
\]

Hence tangential stationarity and nonnegative curvature become

\[
 T_\rho(x)+2T_\rho(2x)=0,
 \qquad
 T_\rho'(x)+4T_\rho'(2x)\ge0.
\]

These are necessary conditions for an interior local minimum.  Strict
convexity of `Q_P'` proves there is at most one such root for each `rho`; it
does not make the two displayed conditions sufficient, which is why the
source wording was corrected.

The inward chamber derivative gives

\[
                         T_\rho(x)\le0\le T_\rho(2x).
\]

For the free period derivative,

\[
 {\partial\over\partial P}
 \{C(P)+F_P(a)+F_P(2a)\}
 =\sum_{q\ge1}q\{K'(qP)+K'(qP+a)+K'(qP+2a)\}.
\]

Since

\[
 \kappa(u)={K'(Au)\over2A}
 =\begin{cases}
 h(1+u)-h(1-u),&0\le u\le1,\\
 h(1+u),&u\ge1,
 \end{cases}
\]

normalization changes the period equation only by a positive constant.
Thus the residual `mathcal R(rho,x)=0` in the source is exact.

The remaining parameter set is bounded and has compact closure, but the
KKT locus itself has not been proved closed or continuous.  No compactness
argument is used in the present theorem.

## 8. Exact scope

The corrected theorem proves the two outer period regions positive and
reduces the rest to the displayed bounded KKT locus.  It does not sign that
locus and therefore does not prove complete Chamber II, Chamber I,
six-slot positivity, arbitrary-grid Bellman positivity, or an OR-word upper
bound.

All four imported dependency hashes in the source were checked against the
workspace and agree with the frozen values quoted there.
