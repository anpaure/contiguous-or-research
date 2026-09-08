# Independent audit of the sparse-marking Turan spread pivot bank

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_SPARSE_MARKING_TURAN_SPREAD_PIVOT_BANK_20260805.md`  
**Method:** independent symbolic replay; pure mathematics only  
**Verdict:** **INDEPENDENT-GO at the stated owner-only scope**, after one
minor general-theorem correction: the marking parameter must satisfy
`gamma/(s Delta) <= 1`.  The theorem now states the equivalent eventual
assumption `s Delta >= gamma`.  This condition is automatic in the pivot
application and does not change any application or constant.

## 1. Probability space and event intersection

In an `s`-uniform `Delta`-regular simple hypergraph,

\[
                         |E|={N\Delta\over s}.
\]

Deleting a vertex set `F` removes at most `|F|Delta` edges.  With
`q=gamma/(s Delta)`, now explicitly assumed to lie in `[0,1]`,

\[
 \mu=\mathbb E X=q|E(H_F)|
 \ge {\gamma N\over s^2}
       \left(1-{s|F|\over N}\right).
\]

The hypotheses imply `mu -> infinity`, so the displayed lower Chernoff
event has probability `1-o(1)`.

Every intersecting unordered edge pair is counted at least once in

\[
                         \sum_v {d(v)\choose2}
                         \le {N\Delta^2\over2}.
\]

Thus `E Y <= gamma^2 N/(2s^2)`.  Markov gives the stated collision event
with probability at least `epsilon/(1+epsilon)`.  Independence between
this event and the Chernoff/spread events is neither asserted nor needed:
if `G` is the collision event and `H` is the intersection of all
`1-o(1)` events, then

\[
             \Pr(G\cap H)\ge\Pr(G)-\Pr(H^c)>0
\]

eventually.  Hence the proof really does produce one common marking.

## 2. Simultaneous spread bound

For a test set `A`, put

\[
 Z_A=\sum_e |e\cap A|\xi_e.
\]

The retained degrees are at most `Delta`, so

\[
 \sum_e|e\cap A|\le\Delta|A|,
 \qquad
 \sum_e|e\cap A|^2\le s\Delta|A|.
\]

It follows that

\[
 \mathbb E Z_A\le {\gamma|A|\over s},
 \qquad
 \sum_e\operatorname {Var}(|e\cap A|\xi_e)
       \le\gamma|A|.
\]

At excess `epsilon gamma |A|/s`, Bernstein's denominator is
`O_(epsilon,gamma)(|A|)`, because the summand bound `s` contributes
`s * epsilon gamma |A|/s = O(|A|)`.  The exponent is therefore

\[
                    \Omega_{\epsilon,\gamma}(|A|/s^2).
\]

The ratio condition

\[
 {L/s^2\over1+\log|\mathcal A|}\longrightarrow\infty
\]

is stronger than the exact union-bound requirement.  It proves all star
bounds in the same outcome as the edge and collision bounds.  Since the
Turan matching is a subset of the marked edges, and any later exact-size
submatching is a further subset, the spread inequality is inherited
without another probabilistic step.

## 3. Turan coefficient and forbidden-set error

For the marked intersection graph,

\[
 \alpha(G)\ge {X^2\over X+2Y}.
\]

The right side is increasing in `X` and decreasing in `Y`.  Writing
`eta=s|F|/N=o(1)` and inserting the good-event bounds gives

\[
 |M|\ge
 { (1-\epsilon)^2\gamma(1-\eta)^2
  \over
   (1-\epsilon)(1-\eta)+(1+\epsilon)\gamma}
 {N\over s^2}.
\]

This is exactly the theorem's coefficient plus an `o(1)` caused by the
forbidden-set loss.  No codegree estimate and no growing-uniformity nibble
is hidden here.

For a completely explicit even-parity margin, take `gamma=5` and
`epsilon=1/100`.  The limiting coefficient is

\[
 {5(99/100)^2\over99/100+5(101/100)}
 ={9801\over12080}>{11\over14}>{\pi\over4},
\]

using `pi<22/7`.  Thus the asymptotic gap used to absorb the forbidden
`o(1)` term is strict, not merely numerical rounding.

## 4. Pivot hypergraph regularity and simplicity

Fix a rank-`r` endpoint.  An oriented length-`h` pivot geodesic starting
there is determined by an ordered `h`-tuple of deleted coordinates and an
ordered `h`-tuple of inserted coordinates, hence by

\[
                         (r)_h(k-r)_h
\]

choices.  The displayed owner set induces a path in the Johnson graph:
nonconsecutive owners have Johnson distance at least two.  It therefore
has exactly two orientations, reversal being the only duplicate.  Hence

\[
 |E(H_{\rm piv})|={W(r)_h(k-r)_h\over2},
 \qquad
 \Delta={s(r)_h(k-r)_h\over2}.
\]

This also verifies that the collapsed owner-set hypergraph is simple and
regular.  In the central application `h=Theta(sqrt r)<min(r,k-r)` and
`s Delta >= gamma` is automatic.

## 5. Star threshold and simultaneous union bound

For `|S|=a`,

\[
                         |\mathcal O(S)|={k-a\choose r-a}.
\]

This decreases with `a` in the stated range, so at
`a=r-h-1` its minimum is

\[
                         L_*={k-r+h+1\choose h+1}.
\]

When `k=2r+O(1)` and `h=Theta(sqrt r)`, the elementary bounds on binomial
coefficients give

\[
 \log L_*=\Theta(h\log(r/h))
           =\Theta(\sqrt r\log r).
\]

Thus `L_*/s^2` grows superpolynomially and, in particular,

\[
                  {L_*/s^2\over1+\log(2^k)}\to\infty.
\]

The theorem's all-star union bound is valid.  A prescribed
`F=o(W/s)` gives exactly the required `s|F|/W=o(1)`.  For polynomial-size
`F`, its intersection with even the minimum star is negligible, which
justifies the uniform multiplicative form in the final corollary.

## 6. Exact Catalan counts in both parities

At bridge depth `h=d(k)+1`, `s=d(k)+2` and

\[
                         {s^2\over r}\to{\pi\over4}
\]

for both `k=2r` and `k=2r-1`.  The explicit coefficient above is greater
than `pi/4`, so in the even case the matching eventually has strictly more
than

\[
                         {W\over r+1}
\]

edges.  It therefore contains an exact submatching of size
`W/(r+1)-1`.  In the odd case the target is only

\[
                         {W\over2r-1}-1,
\]

corresponding to normalized constant `pi/8`; the same matching has ample
margin.  Passing to either exact-size submatching preserves every spread
bound.

## 7. Exact GO scope

The theorem unconditionally closes the **owner-side spread-bank** row:
after any prescribed `o(W/s)` owner deletion, there is an exact
parity-appropriate Catalan number of pairwise owner-disjoint pivot
geodesics, and their owner union occupies only `O(1/s)` of every tested low
containment star.

It does **not** prove any of the following:

1. disjointness of the bridges' natural suffix-target decks;
2. compatibility of the bridges' flags or endpoint states;
3. a named lower-chain factor on the deterministic complement;
4. arbitrary-width upper completeness of that factor; or
5. `nu(k)<=B(k)+O(1)` or coefficient-zero equality.

The single correction made during this audit affects only the abstract
general lemma outside its application.  All pivot-bank conclusions and
all constants survive unchanged.
