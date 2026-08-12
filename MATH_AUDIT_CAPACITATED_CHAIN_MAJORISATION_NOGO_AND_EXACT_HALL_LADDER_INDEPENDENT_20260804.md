# Independent audit: capacitated-chain majorisation, the Hall ladder, and the interval frontier

**Date:** 2026-08-04  
**Method:** independent symbolic proof replay; no finite search, solver, or
computer-assisted mathematical inference  
**Audited files:**

- `MATH_THEOREM_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_20260804.md`
- `MATH_AUDIT_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_SELF_20260804.md`

## Verdict

**GO after one scope correction.**

The following claims independently replay correctly.

1. Greene--Kleitman truncated-sum inequalities are necessary for a
   prescribed capacity vector, but they are not sufficient, even for a
   connected pure normal rank-symmetric rank-unimodal strongly Sperner
   poset admitting a symmetric-chain decomposition.
2. After the named time slices are fixed, the capacity problem is exactly
   a ladder of adjacent Hall matchings together with the conjugate capacity
   bounds.
3. On a nondecreasing interval of Boolean ranks, an interval-supported
   rank schedule lifts to named skipless Boolean chains by normalized
   matching.
4. The heterogeneous interval integer system is exact; for uniform
   capacity, the interval matrix is totally unimodular, its unrestricted
   dual is exact, and the monotone optimum is the stated separated-comb
   sum.
5. The triangular binomial profile has a uniform linear margin against all
   `D`-separated cuts, so the complete residual profile fits if all active
   sockets are temporarily upgraded to capacity `D`.

The correction is purely one of scope.  The one-sided interval-lift theorem
does not itself lift an arbitrary full Boolean-lattice balanced histogram
across the middle rank.  The source and self-audit have been edited to say
so.  The direct implication from a hypothetical Boolean majorisation
theorem to Furedi's floor/ceiling chain conjecture remains valid, and the
actual lower-ideal application lies entirely in the nondecreasing half.

Nothing audited here proves the true heterogeneous triangular interval
system, prescribed-puncture Hall, literal serialization, owner attachment,
or `nu(k) <= B(k)+O(1)`.

## 1. Necessary truncated-sum cuts

Let `X` be a union of `p` antichains.  Each chain `C_i` meets each
antichain at most once and has size at most `c_i`; hence

\[
 |X\cap C_i|\le \min(p,c_i).
\]

Summing and maximizing over `X` proves

\[
 a_p(P)\le\sum_i\min(p,c_i).
\]

Strong Sperner identifies `a_p(P)` with the sum of the `p` largest rank
sizes, but the Greene--Kleitman min--max theorem minimizes the truncated
objective separately for each `p`.  It does not produce one chain
partition realizing an externally prescribed vector `c`.  The example in
Section 2 witnesses this exact quantifier gap.

## 2. Counterexample replay

The poset consists of three internally disjoint four-element arms between
one bottom and one top.  Its rank sizes are

\[
                       1,3,3,3,3,1.
\]

### 2.1 Structural properties

- **Connected and pure:** every maximal chain is one whole arm together
  with the two endpoints and therefore has six elements.
- **Rank-symmetric and rank-unimodal:** immediate from the displayed rank
  sizes.
- **Normal:** bottom-to-rank-one is a complete star; each internal
  interface is a perfect matching between equal three-element ranks; and
  every nonempty subset of rank four has the singleton top as its upper
  neighborhood.  In each case
  `|N(X)|/|P_(i+1)| >= |X|/|P_i|`.
- **SCD:** one arm together with both endpoints has rank interval `[0,5]`,
  and the other two arms have rank interval `[1,4]`.

For a union of `p` antichains, every included endpoint consumes its own
antichain because it is comparable with every other element.  With `s`
endpoints included, at most `s+3(p-s)` elements occur.  It follows, with
the obvious realizing families, that

\[
 (a_1,a_2,a_3,a_4,a_5,a_6)=(3,6,9,12,13,14).
\]

Thus the poset is strongly Sperner directly, without relying on normality.

### 2.2 Capacity failure despite strict scalar slack

For five bins of capacity three, the truncated sums are

\[
                       (5,10,15,15,15,15),
\]

strictly above every entry of the preceding `a_p` vector; total capacity
is `15>14` as well.

Nevertheless, a chain contains internal elements from at most one arm.
Four internal elements of one arm need at least two capacity-three chains,
so the three arms require at least six chains.  Five bins cannot suffice.

The five displayed atomic supports have the claimed column sums.  The
rank positions `1` and `4` have combined demand six, while a length-three
interval meets at most one of them.  Hence five interval rows are also
impossible.  This independently verifies both the named obstruction and
its earlier one-dimensional consecutive-support shadow.

## 3. Exact Hall-ladder equivalence

Given a chain packing, enumerate each chain from its maximum downward and
place its `q`-th element in `A_q`.  A bin of height below `q` contributes
nothing, so

\[
 |A_q|\le K_q=|\{i:c_i\ge q\}|.
\]

Consecutive elements give an inclusion injection
`A_(q+1) -> A_q`.

Conversely, orient every chosen injection toward the smaller slice index.
Every vertex outside `A_1` has one outgoing edge, injectivity gives
indegree at most one, and the slice index strictly decreases.  Therefore
the components are vertex-disjoint directed paths and hence chains.
Their conjugate length counts are exactly `|A_q|`.

If the `j`-th largest path length `ell_j` exceeded `c_j`, then at
`q=c_j+1` there would be at least `j` paths of height at least `q`, while
there are at most `j-1` capacities of that height.  This contradicts
`|A_q|<=K_q`.  Thus decreasingly sorted paths fit decreasingly sorted
bins.

For fixed slices, every interface is an ordinary bipartite matching that
must saturate `A_(q+1)`.  Hall's theorem is exact, and the matchings at
different interfaces may be chosen independently: slice monotonicity
automatically turns their union into paths.  Selection of the named slices
is intentionally outside these fixed-interface flows.

## 4. Boolean interval-support lift

For `X` in Boolean rank `s`, upward incidence counting gives

\[
 (k-s)|X|\le (s+1)|N(X)|,
\qquad
 |N(X)|\ge {C_{s+1}\over C_s}|X|.
\]

On a nondecreasing rank interval, `C_(s+1)>=C_s`, so Hall matches any
currently selected family of continuing labels to distinct containing
sets one rank higher.  After this matching, exactly
`n_(s+1)-q` labels start, and at least
`C_(s+1)-q >= n_(s+1)-q` named sets remain unused.  Induction therefore
constructs all named skipless chains.

This proof is adaptive: it chooses the named family in each new rank.  It
does not match into an arbitrary pre-frozen punctured family.  It is also
one-sided.  Across the descending half, the displayed expansion inequality
reverses, so an arbitrary full-lattice interval histogram needs an
additional correlated middle-rank gluing argument.  Neither limitation
affects the lower-ideal use in the theorem.

## 5. Exact interval formulations

### 5.1 Heterogeneous capacities

The coverage equalities

\[
 \sum_{a\le s\le b}x_{a,b}=n_s
\]

are exactly the column demands of an interval family.  The threshold rows

\[
 \sum_{b-a+1\ge q}x_{a,b}\le K_q
\]

say that the conjugate count of interval lengths is dominated by the
conjugate count of capacities.  Expanding integral `x_(a,b)` into literal
rows and applying the same sorted-conjugate argument as in the Hall ladder
assigns every interval to a capacity.  Conversely, any such assignment
obviously satisfies both systems.  This proves exactness of the integer
formulation.

For any rank-position set `S`, one bin contributes at most
`alpha_(c_i)(S)`, proving the geometric cut.  If the points of `S` are
pairwise `D`-separated and every `c_i<=D`, each positive-capacity interval
meets `S` at most once, yielding the `K_1` cut.

### 5.2 Uniform capacity and TU

With all capacities equal to `D`, the position-by-interval incidence
matrix has consecutive ones in every column and is totally unimodular.
For integral `n`, the equality-form covering polyhedron has an integral
optimum.  The primal

\[
 \min\{\mathbf1^Tx:Ax=n,\ x\ge0\}
\]

is feasible because singletons are allowed.  Its exact dual is

\[
 \max\{n^Ty:A^Ty\le\mathbf1\},
\]

with `y` unrestricted because the primal rows are equalities.  This is
precisely formula (2.18).

### 5.3 Closed monotone formula

For nondecreasing integer `n_s`, every horizontal Ferrers layer is a
suffix.  Cutting a suffix of length `L_y` into pieces of length at most
`D` uses `ceil(L_y/D)` intervals, and

\[
 \sum_y\left\lceil {L_y\over D}\right\rceil
 =\sum_{j\ge0}n_{m-jD}.
\]

The positions `m,m-D,m-2D,...` are pairwise too far apart for one interval
of length at most `D` to contain two.  Their unit weights are a feasible
dual and give the matching lower bound.  Thus the formula for
`kappa_D(n)` is exact.

## 6. Gaussian separated-cut margin

Monotonicity of the lower-half binomial coefficients makes the highest
`D`-spaced comb extremal.  With

\[
 a=\pi/4,
 \qquad D=\sqrt{\pi k/8}+O(1),
\]

its normalized `j`-th term tends to `exp(-a(j+1)^2)`.  The product formula
for binomial ratios and `log(1-u)<=-u` provide a uniform
`exp(-c j^2)` majorant, so dominated convergence is justified.

The active-socket density tends to `1-exp(-a)`.  Hence the limiting margin
is

\[
 \Delta=1-2e^{-a}-\sum_{j\ge2}e^{-aj^2}.
\]

It is positive using exactly the elementary estimates in the source:

\[
 2e^{-a}<0.946,
 \qquad e^{-4a}<0.05,
 \qquad
 \sum_{j\ge3}e^{-aj^2}
 <{7\over2400},
\]

whose sum is below one.  Therefore a fixed `delta>0` works for all large
`k`.  Deleting triangular boundary targets can only decrease the left side
of these necessary separated cuts.

For the complete nondecreasing residual binomial histogram, the monotone
formula identifies `kappa_D` with the top `D`-spaced comb, so

\[
                  \kappa_D\le K_1-\delta W.
\]

This conclusion upgrades every active socket to capacity `D`.  It proves
that the **number** of active sockets is ample.  It does not assign the
intervals to the true heterogeneous capacities, does not make an arbitrary
boundary-deleted profile monotone, and does not prove the nested threshold
rows of the heterogeneous integer system.

## 7. Uniform-chain frontier and corrected scope

Let `N=2^k`, let `W` be Boolean width, and give the `W` bins the balanced
floor/ceiling capacities summing to `N`.  For `p` below the smaller
capacity, the truncated sum is `pW` and dominates the `p` largest Boolean
ranks; above it, the truncated sum is `N`.  Thus a hypothetical theorem
making these cuts sufficient in the Boolean lattice would yield a chain
partition saturating every balanced capacity, exactly the floor/ceiling
uniform-chain conclusion.

This implication is direct and valid.  It should not be conflated with
Theorem 2.2: the latter only names interval schedules on a nondecreasing
rank interval.  The source and self-audit now state this distinction.

## 8. Final proof boundary

The audited chain is

\[
 \text{heterogeneous interval integer solution}
 \Longrightarrow
 \text{adaptively named Boolean lower flags}
\]

when the retained names are co-chosen.  For fixed named punctures, the
exact replacement is the ordered Hall ladder.  The separated Gaussian
margin only proves the relaxed all-capacities-equal-`D` face.

Therefore the theorem is safe to use as a reduction and a no-go result,
but not as a solution of the atomic-to-named lower lift or of the global
OR-word construction.
