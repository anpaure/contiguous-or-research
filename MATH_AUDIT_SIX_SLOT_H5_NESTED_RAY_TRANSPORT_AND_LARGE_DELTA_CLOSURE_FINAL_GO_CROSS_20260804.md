# Final cross-audit: six-slot `h=5` nested-ray large-excess closure

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the two-fifths Gaussian anchor,
the complete reflected physical polytope, all three compact rays, all six
period gains, the endpoint interval, and the exact rational margin.  No
search, solver, sampled computation, or numerical optimization was used.

**Audited theorem:**
`MATH_THEOREM_SIX_SLOT_H5_NESTED_RAY_TRANSPORT_AND_LARGE_DELTA_CLOSURE_20260804.md`,
SHA256
`34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a`.

## 0. Verdict

**FINAL GO.**  The theorem proves strict positivity for every canonical
inert size-five-efficient six-slot table with

\[
                         A/15\le\delta<A/5.
\]

The three-ray inequalities, gain monotonicities, Gaussian anchor, endpoint
quantifiers, and final margin are valid on all three endpoint faces and
their intersections.  No face or exterior chamber is omitted.

One line in Lemma 2.3 is terse: `y<=m` alone would give only a weak compact
difference.  The full frozen physical rows imply the stronger inequality

\[
                         m-y\ge{A-5\delta\over10}>0,
\]

which supplies the advertised strictness.  This is an implication of the
stated hypotheses, not an extra assumption or a repair to the theorem.

## 1. Two-fifths anchor

For `w=2A/5`, the compact term and first three positive-period adverse
terms have exponents

\[
 {9\pi\over100},\quad {49\pi\over100},\quad
 {36\pi\over25},\quad {289\pi\over100}.
\]

The four strict lower Gaussian prices sum to

\[
 {7535+2143+107+1\over10000}={9786\over10000}.
\]

Dropping all later negative terms is a strict upper bound, hence

\[
                         F(2A/5)<{214\over10000}
 ={107\over5000}<{11\over500}.
\]

For the lower bound, the four displayed adverse upper prices sum, together
with the complete omitted tail, to

\[
 {151\over200}+{43\over200}+{11\over1000}
 +{3\over25000}+{1\over1000000}
 ={981121\over1000000}.
\]

The omitted-tail estimate has the correct scale.  Its first exponent is
`121pi/25>40293/2650`, so the first term is below `1/2000000`.  The smallest
successive exponent gap is `49pi/20>16317/2120`, giving ratio below
`1/1000`; therefore the complete tail is below `1/1000000`.

It follows that

\[
 F(2A/5)>{18879\over1000000}>{1\over100}.
\]

All four upper- and lower-price exponent comparisons use the displayed
positive Taylor majorants in the correct direction.  Every exponent is
below 25 where `U_24` is invoked.

## 2. Physical-ray consequences

The exact reflected predecessor gives

\[
 0\le u\le{A-5\delta\over6},
 \quad x\le u+\delta,
 \quad y\le{2(A-u)\over5},
\]

\[
 v\ge{A+4u\over5},
 \quad m\ge{2A+3u\over5},
 \quad v\ge x+u,
 \quad m\ge y+u.
\]

For `0<delta<A/5`, these imply every simplified row used in the theorem:

\[
 0\le u\le A/6,\qquad x\le v,\qquad y\le m,
 \qquad v\ge A/5,\qquad m\ge2A/5,
\]

\[
                         0\le x\le A/5,qquad
                         0\le y\le2A/5.
\]

For the `x` bound, explicitly,

\[
 x\le u+\delta\le{A+\delta\over6}<A/5.
\]

The endpoint row `A-2m<=delta` also gives

\[
 m-y\ge{A-\delta\over2}-{2A\over5}
 ={A-5\delta\over10}>0.
\]

This strict separation is valid on every endpoint face; it is not lost at a
face intersection or at `u=0` in the compact closure.

## 3. Compact transport rays

The exact compact part is

\[
 T_5=C-F(u)+F(x)-F(v)+F(y)-F(m).
\]

For the first ray, `u<=A/6<A/2`, so the frozen global price and ceiling
floor give

\[
 C-F(u)>L-G
 ={44024-53300\over1000000}
 =-{9276\over1000000}.
\]

For the second ray:

- if `x>=4A/25` and `v<=A/2`, then `x<=v` and strict-threshold
  monotonicity gives `F(x)>=F(v)`;
- if `v>A/2`, reflection and half-band positivity give
  `F(v)<epsilon<F(x)`;
- if `x<4A/25`, then `F(x)>L`, while `v>=A/5` gives
  `F(v)<V_5` either by monotonicity when `v<=A/2` or by reflection when
  `v>A/2`.

Therefore

\[
 F(x)-F(v)>L-V_5
 ={44024-49730\over1000000}
 =-{5706\over1000000}.
\]

For the third ray:

- if `y>=4A/25` and `m<=A/2`, then the strict separation derived above and
  strict decrease give `F(y)>F(m)`;
- if `m>A/2`, reflection gives `F(m)<epsilon`, while either monotonicity
  from `y<=2A/5` or the quarter floor gives `F(y)>1/100>epsilon`;
- if `y<4A/25` and `m<=A/2`, then `F(y)>L` and
  `F(m)<=F(2A/5)<11/500<L`; reflection handles `m>A/2`.

Thus `F(y)-F(m)>0` in every chamber.  Adding the three rays yields

\[
                         T_5>-{14982\over1000000}.
\]

## 4. Six period gains

For `q>=1`, the `q`-th summand of
`D_delta(w)=F_(A+delta)(w)-F_A(w)` is

\[
 e^{-(A+qA+w)^2}-e^{-(A+q(A+\delta)+w)^2}.
\]

Its derivative in `w` is

\[
 2\{h(A+q(A+\delta)+w)-h(A+qA+w)\},
 \qquad h(s)=s e^{-s^2}.
\]

Both arguments are at least `2A`, where `h` is strictly decreasing, so
`D_delta(w)` is decreasing on `[0,A]`.  Every summand increases with
`delta`, hence so does `D_delta(w)` and the sum `mathcal P_5(delta)`.

The six gain arguments are

\[
                         0,x,y,A-m,A-v,A-u.
\]

The physical rows give respectively the upper grid bounds

\[
                         0,A/5,2A/5,3A/5,4A/5,A.
\]

Since `D_delta` decreases in its argument, the total gain is at least

\[
                         \mathcal P_5(\delta)
 =\sum_{j=0}^5D_\delta(jA/5).
\]

The exact reflected decomposition contains three theta terms, each strictly
larger than `-epsilon`.  Hence

\[
 \Phi>\mathcal P_5(\delta)
 -{14982+150\over1000000}
 =\mathcal P_5(\delta)-{15132\over1000000}.
\]

## 5. Endpoint gain at `delta=A/15`

Monotonicity in `delta` reduces the entire large-excess interval to its
left endpoint.  For the `q=1` term at `w=jA/5`, its right endpoint is

\[
                         At_j,\qquad t_j={31+3j\over15}.
\]

Since `h(s)=s e^{-s^2}` decreases beyond `2A`, integration over the length
`A/15` interval gives

\[
 D_{A/15}(jA/5)
 >{\pi\over30}t_j e^{-\pi t_j^2/4}.
\]

Retaining only `q=1` is valid because every later gain summand is positive.
The six strict Gaussian lower bounds in the theorem have weighted sum

\[
                         \sum_{j=0}^5t_jb_j
 ={55799\over375000}.
\]

Using `pi>333/106` gives

\[
 \mathcal P_5(A/15)
 >{333\over3180}{55799\over375000}
 ={2064563\over132500000}.
\]

The adverse constant has the same denominator:

\[
 {15132\over1000000}
 ={2004990\over132500000}.
\]

Their exact difference is

\[
 {2064563-2004990\over132500000}
 ={59573\over132500000}>0.
\]

Thus the margin is strict at `delta=A/15` and only increases for larger
`delta`.

## 6. Endpoint and chamber scope

The reflected predecessor parameterizes every canonical inert `h=5` table
by

\[
                         0<\delta<A/5
\]

and includes all three saturated endpoint faces `X,Y,Z` and all their
intersections.  The proof above uses only inequalities valid on their common
physical polytope and therefore closes every such face whenever
`delta>=A/15`.

The threshold face `delta=0` is already positive by the frozen predecessor
chain.  The upper endpoint `delta=A/5` is a formal boundary and is excluded
from the physical inert stratum.  Therefore the exact unresolved canonical
inert size-five-efficient six-slot region is

\[
                         \boxed{0<\delta<A/15}.
\]

No assertion is made here about other least-efficiency branches, larger
generator tables, arbitrary Bellman grids, or OR-word construction.

## 7. Frozen dependency verification

All three direct dependencies exist at exactly their declared SHA256 values:

| role | SHA256 |
|---|---|
| reflected `h=5` physical polytope and gate | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| global compact price, threshold monotonicity, one-fifth anchor | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| threshold floor, half-band positivity, reflection | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |

The audited theorem remains unchanged at SHA256
`34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a`.
