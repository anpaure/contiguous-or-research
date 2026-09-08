# Symmetrized convex profiles give actual fractional rectangle covers

Date: 2026-09-07. This is a fractional-cover result, not an integral word.
It complements `UNBOUNDED_RECTANGLE_OVERLAP_20260907.md` by showing that its
centered Gaussian profile is realizable on actual subsets after coordinate
symmetrization. The unresolved step is integral rounding/serialization.

## 1. Exact finite realization lemma

Let `k=2m`. Put

\[
 B_j=\binom{2m}{m+j}\quad(0\le j\le m),\qquad B_{m+1}=B_{m+2}=0.
\]

Suppose `G_0,...,G_(m+2)` is nonnegative, nonincreasing and convex,
`G_(m+1)=G_(m+2)=0`, and

\[
                         G_j\ge B_j\quad(0\le j\le m).
\]

Then there is an `S_(2m)`-invariant fractional cover of the Boolean cube by
indexed pairs

\[
 (C\times D,\ (C\times D)^c),
\]

where `C,D` are saturated chains on complementary supports. Its principal
charge is at most `G_0+2G_m`. Before the bounded correction described below,
its indexed occurrence charge is exactly `G_0`, and its total indexed
designated occurrence volume is

\[
                         G_0+2\sum_{j=1}^mG_j.          \tag{1}
\]

The distinction between indexed occurrences and ordinary fractional coverage
is relevant only for the terminal length `m+1` pair and is corrected below.

### Proof

For `1<=a<=m+1`, set

\[
                  w_a=G_{a-1}-2G_a+G_{a+1}\ge0.
\]

Twice summing the second differences gives, for `0<=j<=m`,

\[
                  G_j=\sum_{a>j}w_a(a-j),\qquad
                  G_0=\sum_aa w_a.                    \tag{2}
\]

For each `a`, choose complementary support sizes as follows. If
`a congruent to m+1 (mod 2)`, use `(m,m)`; otherwise use `(m-1,m+1)`.
On a `p`-set there is a saturated symmetric chain of length `a` whenever
`a<=p+1` and `a congruent to p+1 (mod 2)`: start at rank
`(p-a+1)/2` and add `a-1` new coordinates. Thus both shores admit chains
`C_a,D_a` of length `a`. Their product has rank center `m` and rank profile

\[
                         T_a(j)=(a-|j|)_+.
\]

Its full complement has the same profile. Give the uniform coordinate orbit
of this indexed complementary pair total weight `w_a/2`. The symmetric group
is transitive on each rank, so every rank-`m+j` target receives weight

\[
 {1\over B_j}\sum_a {w_a\over2}\,2T_a(j)=G_j/B_j\ge1.
\]

The indexed weighted principal charge is
`sum_a (w_a/2)(a+a)=sum_a a w_a=G_0`. The weighted number of indexed
rectangle occurrences is `sum_a(w_a/2)(2a^2)=sum_a w_a a^2`, which equals
the rank sum in (1), since `sum_j T_a(j)=a^2`.

It remains to correct ordinary set-cover multiplicity. For `a<=m`, choose
the symmetric chains so that at least one shore has a nonempty fixed bottom
set and a nonempty permanently omitted top complement. That shore's chain
contains no two complementary sets, so `C_a times D_a` and its full
complement are disjoint. For `a=m+1`, both shores are maximal chains on
`m` coordinates. Their rectangle and complement overlap exactly in
`emptyset,P,Q,[2m]`, where `P,Q` are the two supports. Here
`w_(m+1)=G_m`.

Under the uniform coordinate orbit, this overlap causes a shortfall
`w_(m+1)/B_0` at each middle target and `w_(m+1)/2` at each of the empty and
full targets. Add the uniform orbit of singleton complementary middle pairs
with total weight `w_(m+1)/2`; it costs `w_(m+1)` and repairs every middle
target. Add the singleton complementary pair `{emptyset},{[2m]}` with weight
`w_(m+1)/2`; it costs another `w_(m+1)` and repairs both extremes (or only
the nonempty full target if empty is outside the problem). Thus ordinary
fractional coverage has charge at most `G_0+2G_m`. Orbit stabilizers cause
no issue because the construction averages over the uniform group action;
equal orbit members may be combined by adding their weights. This proves the
lemma. \(\square\)

## 2. An exact discrete convex majorant

Fix

\[
              0<\epsilon<2e^{-1/2}-1,
              \qquad M=(1+\epsilon)B_0.
\]

The following gives a finite majorant with central charge exactly `M`.
For `0<=j<=m-1`, direct use of
`B_(j+1)/B_j=(m-j)/(m+j+1)` gives

\[
 {B_j-2B_{j+1}+B_{j+2}\over B_j}
 ={2(2(j+1)^2-m-1)\over(m+j+1)(m+j+2)}.               \tag{3}
\]

Thus the binomial tail is convex after its unique inflection. Let `J_m` be
the least `j` for which the right side of (3) is nonnegative, and define

\[
 \sigma_m=\min_{1\le j\le J_m+1}{M-B_j\over j},
 \qquad L_j=M-\sigma_mj.                               \tag{4}
\]

For all sufficiently large `m`, `L_m<0`; this hypothesis is required in the
finite construction. Let `z_m` be the least `j>=J_m+1` with
`B_j>=L_j`, and put

\[
 G_j=\begin{cases}L_j,&0\le j<z_m,\\B_j,&z_m\le j\le m,\end{cases}
 \qquad G_{m+1}=G_{m+2}=0.                             \tag{5}
\]

This sequence is nonnegative, decreasing, convex, and dominates `B`.
Indeed (4) gives domination through `J_m+1`; the definition of `z_m` gives it
until the splice; and afterward equality holds. Both pieces decrease. At the
splice, writing differences as `Delta G_j=G_(j+1)-G_j`,

\[
 -\sigma_m\le B_{z_m}-L_{z_m-1}
 \le B_{z_m}-B_{z_m-1}\le B_{z_m+1}-B_{z_m},           \tag{6}
\]

where the first inequality is the crossing, the second uses the previous
noncrossing, and the last uses tail convexity. Hence differences do
not decrease. The final two differences are also increasing because
`B_(m-1)=2m`, `B_m=1`, `B_(m+1)=0`. The finite lemma therefore produces an
actual fractional coordinate cover of charge at most
`(1+epsilon)W(2m)+2`, since `G_m=B_m=1`.

## 3. Fixed-error Gaussian limit and side scale

Let `m` tend to infinity with `epsilon` fixed. Uniformly for `t` in compact
sets,

\[
 {B_{\lfloor t\sqrt{2m}\rfloor}\over B_0}\longrightarrow e^{-2t^2},
 \qquad {J_m\over\sqrt{2m}}\longrightarrow{1\over2}.  \tag{7}
\]

Consequently

\[
 {\sigma_m\sqrt{2m}\over B_0}\longrightarrow
 \min_{0<t\le1/2}{1+\epsilon-e^{-2t^2}\over t}.       \tag{8}
\]

The minimizer is the unique `a in (0,1/2)` satisfying

\[
              (1+4a^2)e^{-2a^2}=1+\epsilon,
\]

and the minimum is `lambda_a=4ae^(-2a^2)`. The splice position divided by
`sqrt(2m)` tends to the unique second intersection `z_a>1/2` of

\[
             1+\epsilon-\lambda_at=e^{-2t^2}.          \tag{9}
\]

Thus the normalized discrete profile converges to

\[
 g_a(t)=\max\{1+\epsilon-\lambda_a|t|,e^{-2t^2}\}.
\]

The binomial tails give uniform integrability, so (1) and a Riemann sum yield

\[
 {V\over2^{2m}}\longrightarrow
 \sqrt{2/\pi}\int_{-\infty}^{\infty}g_a(t)\,dt.       \tag{10}
\]

As `epsilon` subsequently tends to zero, `epsilon=2a^2+O(a^4)`,
`z_a~1/(4a)`, and (10) is asymptotic to

\[
                         {1\over2\sqrt{\pi\epsilon}}. \tag{11}
\]

This is the sharp centered rank-profile constant from the overlap note, now
as an actual-coordinate fractional cover.

Although (5) has tiny positive weights at longer lengths, its principal
charge is concentrated on `a=O(sqrt(m/epsilon))`. Precisely, for any cutoff
`L`, telescoping gives

\[
 \sum_{a>L}a w_a=(L+1)(G_L-G_{L+1})+G_{L+1}.           \tag{12}
\]

After `L=R sqrt(2m)` beyond the splice, the right side divided by `B_0`
tends to `(1+4R^2)e^{-2R^2}`. Choosing `R` a sufficiently large constant
multiple of `epsilon^(-1/2)` makes this negligible. Hence all but a
vanishing fraction of the charge uses square side lengths
`O(sqrt(k/epsilon))`, exactly the scale forced by the finite lower bound.

## 4. Macroscopic calibration

Fractional coefficient one itself has a simpler exact construction with
macroscopic sides. Use only the disjoint centered square pair of length `m`
from the `(m-1,m+1)` split and give its uniform coordinate orbit total weight

\[
                         z={B_0m\over2(m^2-1)}.         \tag{13}
\]

At offset `0<=j<m` it has `2(m-j)` distinct targets. The required weight,
relative to the central requirement, is

\[
 Q_j={B_j/B_0\over1-j/m},\qquad Q_0=1,\quad
 Q_1={m^2\over m^2-1}.
\]

For `1<=j<=m-2`,

\[
 {Q_{j+1}\over Q_j}={ (m-j)^2\over m^2-(j+1)^2}<1,
\]

because numerator minus denominator is `1-2j(m-j-1)<0`. Thus (13) covers
every nonempty proper rank; add the full target separately. Its principal
charge is

\[
                  2mz={B_0m^2\over m^2-1}=B_0+o(B_0). \tag{14}
\]

This is exactly optimal among fractional centered square covers with side at
most `m`. Indeed a side-`ell` pair supplies `2(ell-1)` rank-`m+1`
occurrences at cost `2ell`, so its incidence per unit cost is at most
`(m-1)/m`. Covering all `B_1=B_0m/(m+1)` targets forces the lower bound
in (14).

The average multiplicity of (13) is asymptotic to `sqrt(m/pi)`. Its relative
charge error is of order `m^(-2)`, outside the joint regime
`epsilon*m -> infinity` used in Section 3. Hence it does not contradict the
mesoscopic lower scale there. The added content of the tangent construction
is a sharp overlap law while keeping almost all charged sides at
`O(sqrt(k/epsilon))`, not the first fractional coefficient-one family.

For the larger model allowing unequal side lengths and moving rank centers,
`EXACT_SATURATED_PAIR_FRACTIONAL_OPTIMUM_20260907.md` subsequently gives
the exact fractional optimum `W(2m)*(1+1/(m(m+1)))`, attained by two
coordinate orbits. This does not change the restricted optimality assertion
above or perform integral rounding.

## 5. Boundary of the result

This proves fractional coverage of each actual subset, not merely aggregate
rank domination. It does not round the orbit weights to a finite integral
cover of comparable charge. The companion
`CENTERED_SQUARE_BAND_COMPILER_20260907.md` proves that sufficiently long
integral squares can be serialized with negligible overhead; hence
serialization is no longer the missing step for such a rounding. The
hyperedges here have growing size and large structured intersections, so a
fixed-uniformity matching theorem does not perform the required integral
selection.
