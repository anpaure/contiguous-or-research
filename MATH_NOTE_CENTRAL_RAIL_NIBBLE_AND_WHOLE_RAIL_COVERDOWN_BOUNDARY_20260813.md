# Central-rail nibble and whole-rail cover-down boundary

**Date:** 2026-08-13  
**Status:** exact reduction and theorem-applicability audit.  No diagonal
near-perfect matching is claimed.

## 1. Inputs now available

Let `H_cent` be the period-`r=2q+1` central rail hypergraph on the
rank-`R` owner layer.  The exact theorem gives

\[
 {\Delta_2\over D}={2\over R(k-R)},
 \qquad
 r^2{\Delta_2\over D}=O(k^{-1}).                      \tag{1.1}
\]

Every edge is a literal closed biresident rail with simple proper interval
deck.

Independently, the complementary-fibre lift gives, for every suitable
graph edge `h`, a literal period-`2q` rail `B(h)` and a common-reserve
identity

\[
 \mathcal B(S)=\mathcal B(G)\sqcup\mathcal B(h).      \tag{1.2}
\]

Thus a leave which is already a disjoint union of `s` fibres `B(h)` is
absorbed componentwise by `s` whole-rail switches.  The cover-down target
is therefore sharper than an arbitrary small owner set:

\[
 \boxed{
 V\setminus V(M)=\bigsqcup_{i=1}^{s}\mathcal B(h_i)
 \quad\text{with bounded }s.}                        \tag{1.3}
\]

## 2. Scalar compatibility

A central matching leaves

\[
 |L|\equiv W\pmod{2q+1}.                              \tag{2.1}
\]

A union of `s` period-`2q` fibres has size `2qs`, hence

\[
 2qs\equiv -s\pmod{2q+1}.                             \tag{2.2}
\]

Consequently the scalar congruence for (1.3) is

\[
 \boxed{s\equiv-W\pmod{2q+1}.}                       \tag{2.3}
\]

There is always a representative `s in {0,...,2q}`.  Thus the central
scalar obstruction can be converted to at most `2q` whole residual rails,
but this is `O(q)`, not `O(1)`.  A bounded number of fibres is possible
only if `-W mod (2q+1)` is bounded along the relevant `k`, or if additional
consecutive-period components are admitted.  Because

\[
 \gcd(2q,2q+1)=1,                                    \tag{2.4}
\]

a mixed `2q`/`2q+1` scalar equation has no divisibility obstruction, but
scalar solvability is not a disjoint rail factor.

The general-period complementary-fibre lift sharpens the scalar point.
It supplies whole residual fibres of each legal period `m>=2q` for which
the required fresh labels exist.  In particular, periods `2q+1` and
`2q+2` are consecutive, so every sufficiently large scalar `W` is a
nonnegative combination of their sizes.  This removes scalar divisibility
if those fibres participate in the **bulk** factor.  It does not imply a
bounded terminal correction: a cover-down theorem must still correlate
the selected bulk and its leave into the same fibre catalogue.

## 3. Why an ordinary central nibble does not produce (1.3)

The matching incidence system alone records only which owners are left.
It does not correlate the leave into the highly structured fibres
`B(h)`.  Even a matching leaving `o(W)` arbitrary owners gives no reason
for those owners to admit a partition into period-`2q` fibres.

The correct reserve formulation is a transversal cover-down.  Choose a
pairwise-disjoint family `R` of candidate fibre supports, reserve all
their owners from the main nibble, and demand that the main matching cover
every owner outside `R` while leaving inside `R` precisely a selectable
union of fibre blocks satisfying (2.3).  Equivalently, one needs a
matching in an augmented hypergraph whose terminal choices are the blocks
`B(h)`, not individual owner vertices.

The local whole-rail identity proves that each chosen block can be
absorbed.  It does not prove:

1. existence of a large mutually disjoint reserve family;
2. a pseudorandom nibble whose leave is supported on that family;
3. a final transversal selecting whole blocks rather than arbitrary
   subsets of their owners; or
4. preservation of socket, cap, history, and other non-interval tickets.

## 4. Exact one-bite statement

There is a uniform-in-`r` first step.  In an `r`-uniform `D`-regular
hypergraph, mark every edge independently with probability

\[
 p={\gamma\over rD},\qquad0<\gamma\le1,
\]

and retain a marked edge only if it meets no other marked edge.  Since an
edge meets at most `r(D-1)` other edges, its conditional isolation
probability is at least

\[
 (1-p)^{r(D-1)}=e^{-\gamma+o(1)}.
\]

Some outcome therefore covers at least

\[
 {\gamma e^{-\gamma}+o(1)\over r}|V|                 \tag{4.1}
\]

vertices.  For `r=Theta(sqrt(k))`, one bite covers a
`Theta(k^{-1/2})` fraction.

This does not iterate automatically.  To leave an `o(1)` fraction via
steps of this scale requires `Theta(r log(1/epsilon))` bites, together
with uniform regeneration of degrees, codegrees, and reserve loads.  The
time-zero estimate (1.1) is not such a trajectory theorem.

There is a variable-uniformity theorem of Grable whose applicability
condition is worth separating from its conclusion.  It asks

\[
 \Delta_2=o\!\left({D\over r\log W}\right).           \tag{4.2}
\]

For the central hypergraph this condition **does hold**, because

\[
 {r\Delta_2\log W\over D}
 ={2(2q+1)\log W\over R(k-R)}
 =\Theta(k^{-1/2}).                                   \tag{4.3}
\]

However, the resulting quoted leave fraction is

\[
 \left({r\Delta_2\log W\over D}\right)^{
          1/(2r-1+o(1))}.                             \tag{4.4}
\]

Here the base is `Theta(k^{-1/2})` but the exponent is
`Theta(k^{-1/2})`, so

\[
 \log(\text{fraction})
 =-\Theta\!\left({\log k\over\sqrt k}\right)=o(1),
\]

and (4.4) tends to one.  Thus Grable verifies that the time-zero
collision condition is genuinely in his growing-rank regime, but his
quantitative conclusion does not yield an `o(W)` leave here.

## 5. Audit of Vu's higher-codegree theorem

Vu's theorem can exploit a hierarchy

\[
 D=D_1,D_2,\ldots,D_s
\]

of upper bounds on codegrees.  In a convenient modern restatement, if
`x` satisfies

\[
 x^2\le {D_j\over D_{j+1}}quad(1\le j<s),
 \qquad
 x^{r-s+1}\le {D_{s-1}\over D_s},                    \tag{5.1}
\]

then, under the theorem's hierarchy, the leave is of order

\[
 {W\log^A W\over x}.                                 \tag{5.2}
\]

Using only the pair codegree means taking `s=2`, so

\[
 x\le(D/D_2)^{1/(r-1)}
 =\left({R(k-R)\over2}\right)^{1/(2q)}
 =1+O\!\left({\log k\over\sqrt k}\right).            \tag{5.3}
\]

This is quantitatively vacuous: it does not give an `o(W)` leave.

Higher codegrees could change this conclusion only after proving exact
upper bounds `D_j` with sufficiently large consecutive ratios throughout
a growing range of `j`.  The pair formula alone supplies no such bounds,
because the trivial monotonicity estimate `D_j<=D_2` makes the ratios in
(5.1) equal to one.  The central rail geometry suggests that clustered
consecutive windows are the extremal configurations, but a complete
labelled Venn-profile optimization has not yet been proved.  Moreover,
Vu's stated hierarchy still fixes the uniformity before the degree limit.

There is also an exact obstruction to using the entire sequence blindly.
Every unrooted rail support occurs with its two directed orientations, so
the maximum full-edge multiplicity is

\[
 D_r=2.
\]

Any `r-1` owners from one support determine that support.  Indeed, their
intersection is the core `C`: no toggle label belongs to all `r-1`
remaining `q`-windows.  After deleting `C`, every toggle label has degree
`q` in the full window family; in the `r-1` subfamily, the `q` labels of
the missing window have degree `q-1` and the other `q+1` labels have
degree `q`.  Hence both the toggle set and the missing window are
recovered.  Finally, in the full family the graph joining two windows
when their intersection has size `q-1` is a cycle.  Its two directions
recover exactly the two directed cyclic orders modulo rotation.  Thus
the same two and only two parameterized orientations contain the given
`r-1` owners, giving

\[
 D_{r-1}=2.                                           \tag{5.4}
\]

Thus choosing `s=r` in (5.1) forces `x^2<=D_{r-1}/D_r=1`.  One must stop
before this flat terminal tail, but then the terminal power
`x^{r-s+1}` becomes large.  This tradeoff is exactly why a full optimized
codegree calculation, rather than the slogan that higher codegrees help,
is necessary.

Thus invoking "higher codegrees help" without the full central
`D_j` calculation and a diagonal threshold audit is not proof-safe.

## 6. Precise remaining theorem

The positive route is reduced to the following concrete statement.

> **Central-to-fibre cover-down theorem.**  There is a pairwise-disjoint
> reserved family of legal period-`2q` fibres and a matching of central
> period-`2q+1` rails such that every uncovered owner belongs to the
> reserve and the uncovered reserve owners are a disjoint union of a
> bounded number of complete fibres, with all compulsory ticket rows
> retained.

The whole-rail graph absorber proves the final switching step once this
theorem is available.  Neither classical fixed-rank Pippenger, Vu's
pair-only specialization, nor the current first-bite calculation proves
the cover-down statement.

The immediate rigorous subproblems are therefore:

1. compute the full central rail codegree sequence, including labelled
   Venn types, and test Vu/Gould--Kelly bottlenecks;
2. construct a large disjoint period-`2q` reserve with uniform incidence
   from outside owners;
3. prove a reserve-aware diagonal nibble or an exact transversal
   cover-down; and
4. solve the residue (2.3) with bounded, rather than merely `O(q)`,
   terminal components.
