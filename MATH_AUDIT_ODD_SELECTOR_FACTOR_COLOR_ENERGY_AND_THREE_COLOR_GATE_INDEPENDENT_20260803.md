# Independent audit: odd selector factor-colour energy and the three-colour gate

**Date:** 2026-08-03  
**Verdict:** **GO**, after two scope clarifications applied directly to the
source theorem.  The reduction, all counting identities, the zero set, the
factorization equivalence, and the Kempe obstruction are exact.

**Audited source:**
`MATH_THEOREM_ODD_SELECTOR_FACTOR_COLOR_ENERGY_AND_THREE_COLOR_GATE_20260803.md`  
**Audited source SHA256:**
`9a56e03152d0c5bdc69165ea651ccf257138a62d0cd25bacc0e72af946d09c1d`

The two applied clarifications are:

1. the statement now assumes `m>=3`; the sought zero-energy object is
   impossible at `m=2`, since three compressed edges cannot be distributed
   with multiplicity at most two over the unique upper colour;
2. the protected penalty in (2.8) protects an **upper colour as unique**.
   It does not pin or preserve a specified physical occurrence of that
   colour.

No other correction was needed.

## 1. Parameter and Catalan identities

For `n=2m-1`,

\[
 W={2m-1\choose m-1}={2m-1\choose m},\qquad
 U={2m-1\choose m+1}={m-1\over m+1}W.
\]

Hence

\[
 C=W-U={2W\over m+1}
   ={1\over m+1}{2m\choose m}=\operatorname{Cat}_m,
 \qquad {C\over U}={2\over m-1}.                 \tag{A1}
\]

It follows immediately that

\[
 {m\choose2}C=mU,                                  \tag{A2}
\]

which is exactly the Catalan conversion used in (3.3).

The containment graph between the rank-`m-1` and rank-`m` shores is
`m`-regular on both sides: an `(m-1)`-set has `m` one-element extensions,
and an `m`-set has `m` one-element deletions.  Thus every proper
`m`-edge-colouring is precisely a decomposition into `m` perfect matchings.

## 2. Local multigraph and compression

Fix an upper set `R` of size `m+1`.  Its middle facets are `T_x=R-x` and
its lower diamonds are `q_xy=R-{x,y}`.  At each `q_xy`, the two incidences
to `T_x,T_y` have distinct factor colours, so replacing `xy` by that
unordered colour pair produces a loopless multigraph `H_R` on `[m]`.

For a fixed factor colour `i`, each facet `T_x` has exactly one incident
edge of colour `i` among its `m` lower incidences.  There are `m+1` facets,
therefore

\[
 \deg_{H_R}(i)=\sum_{j\ne i}a^R_{ij}=m+1.          \tag{A3}
\]

The handshaking identity gives

\[
 \sum_{i<j}a^R_{ij}={m(m+1)\over2}
 ={m\choose2}+m.                                   \tag{A4}
\]

For fixed colours `i,j`, each lower row `q` has two distinct matching
neighbours.  They are adjacent `m`-sets, their intersection is `q`, and
their union is one upper set `R`.  Conversely, an edge of `H_R` carrying
the pair `ij` is exactly such a lower row.  Therefore

\[
 \mu_{ij}(R)=a^R_{ij}.                              \tag{A5}
\]

Every middle vertex has one incident compressed edge from each of the two
factor colours.  The two edges are distinct.  Parallel compressed edges
cannot occur, because adjacent middle sets have a unique rank-`m-1`
intersection.  The compressed graph is consequently a simple spanning
`2`-factor on the middle shore, with

\[
 \sum_R\mu_{ij}(R)=W.                               \tag{A6}
\]

This verifies Lemmas 1.1 and 1.2 in full.

## 3. One-pair energy and its exact zero set

For every integer `z>=0`,

\[
 f(z)={(z-1)(z-2)\over2}
 =\begin{cases}
 1,&z=0,\\
 0,&z=1,2,\\
 {z-1\choose2},&z\ge2.
 \end{cases}                                      \tag{A7}
\]

Thus `f` is a nonnegative integer and its zero set is exactly `{1,2}`.
Using (A6),

\[
 \begin{aligned}
 \Delta_{ij}
 &=\sum_R\left[{\mu_{ij}(R)\choose2}-\mu_{ij}(R)+1\right]\\
 &=\sum_R{\mu_{ij}(R)\choose2}-W+U
  =\sum_R{\mu_{ij}(R)\choose2}-C.                 \tag{A8}
 \end{aligned}
\]

Hence

\[
 \Delta_{ij}=0
 \quad\Longleftrightarrow\quad
 \mu_{ij}(R)\in\{1,2\}\ \hbox{for every }R.       \tag{A9}
\]

If (A9) holds, write `d_2` for the number of multiplicity-two upper
colours.  Since all `U` colours occur and the total multiplicity is `W`,

\[
 U+d_2=W,\qquad d_2=C.                              \tag{A10}
\]

This proves the claimed duplicate count.

## 4. Automatic regularity of the duplicate design

Let the two matchings be `t,s`.  For any coordinate `x`, each image
matching runs once through the complete middle shore, so its selected
middle sets containing `x` number `{2m-2\choose m-1}`.  In every lower row,
`t(q)\cap s(q)=q`; the lower rows containing `x` number
`{2m-2\choose m-2}`.  Inclusion-exclusion therefore gives

\[
 \#\{q:x\in t(q)\cup s(q)\}
 =2{2m-2\choose m-1}-{2m-2\choose m-2}.            \tag{A11}
\]

Under zero energy, subtract the base occurrence of every upper colour.
Exactly `{2m-2\choose m}` base upper colours contain `x`.  Since the two
adjacent binomial coefficients are equal,

\[
 \begin{aligned}
 \deg_{\mathcal D_{ij}}(x)
 &=2{2m-2\choose m-1}
   -{2m-2\choose m-2}-{2m-2\choose m}\\
 &={2\over m}{2m-2\choose m-1}
  =2\operatorname{Cat}_{m-1}.                      \tag{A12}
 \end{aligned}
\]

The multiplicity-two colour set is a set, not a multiset, so it is a
simple Catalan design of size `C` and the asserted coordinate degree.
There is no additional current-balancing hypothesis hidden here.

## 5. Protected-bank term

The protected objective is

\[
 \Delta^{\mathcal P}_{ij}
 =\Delta_{ij}+\sum_{R\in\mathcal P}{\mu_{ij}(R)\choose2}.    \tag{A13}
\]

Every term is nonnegative.  If (A13) vanishes, then (A9) holds and, for
each protected colour, the binomial penalty vanishes.  Positivity from
(A9) then forces `mu_ij(R)=1` on `P`.  Conversely, cap-two surjectivity
with every protected colour unique makes every term zero.  Hence

\[
 \Delta^{\mathcal P}_{ij}=0
 \Longleftrightarrow
 \bigl(\Delta_{ij}=0\ \hbox{and}\
       \mathcal D_{ij}\cap\mathcal P=\varnothing\bigr).      \tag{A14}
\]

This formula is exact for an upper-colour uniqueness bank.  It records the
multiplicity produced by the actual selector, but it does not distinguish
which physical occurrence supplies the unique protected colour.  A theorem
requiring a named protected row or edge needs additional occurrence-level
variables.

## 6. Total energy and the local equality case

For one `R`, let `z` be the number of zero multiplicities.  From (A4),

\[
 \sum_{i<j}{a^R_{ij}\choose2}
 \ge\sum_{a^R_{ij}>0}(a^R_{ij}-1)
 =m+z\ge m.                                         \tag{A15}
\]

Equality in the first inequality occurs exactly when every positive
multiplicity is `1` or `2`; equality throughout also forces `z=0`.
The excess `m` in (A4) is then realized by exactly `m` doubled pairs.
Equation (A3) says that, after removing the base `K_m`, those doubled
pairs have degree two at every factor colour.  Since they are distinct
pairs and `m>=3`, they form a simple spanning `2`-factor `Z_R`.  Thus

\[
 \sum_{i<j}{a^R_{ij}\choose2}=m
 \Longleftrightarrow H_R=K_m+Z_R.                  \tag{A16}
\]

Summing (A8) over factor pairs and applying (A2) yields

\[
 \sum_{i<j}\Delta_{ij}
 =\sum_R\left(\sum_{i<j}{a^R_{ij}\choose2}-m\right)\ge0.    \tag{A17}
\]

If the total is zero, every local summand is zero; equivalently every
`H_R` has form (A16).  Then every factor pair has multiplicity `1` or `2`
at every upper colour, so all `{m\choose2}` factor pairs are simultaneous
cap-two upper-surjective selectors.  The best-pair average bound follows
because the individual energies are nonnegative integers.

## 7. One-factorization equivalence and topology

Two edge-disjoint incidence bijections are two edge-disjoint perfect
matchings of the `m`-regular bipartite containment graph.  Deleting them
leaves an `(m-2)`-regular bipartite graph.  Konig's line-colouring theorem
decomposes the residual graph into `m-2` perfect matchings, extending the
pair to a one-factorization.  Conversely, any two colour classes of a
one-factorization are edge-disjoint incidence bijections.  Combining this
with (A9) proves the equivalence in (0.8), and combining it with (A14)
proves its protected-colour version.

The compressed graph is a `2`-factor.  Orient an edge from its endpoint
whose incidence has colour `i` to its endpoint whose incidence has colour
`j`.  Every middle vertex then has indegree and outdegree one, so each
component is a directed cycle.  Thus `c_ij=1` is exactly the projected
single-cycle owner/q1 condition.  Since all terms are nonnegative,

\[
 \Xi^{\mathcal P}_{ij}
 =\Delta^{\mathcal P}_{ij}+c_{ij}-1                 \tag{A18}
\]

vanishes exactly for a connected selector with protected upper colours
unique.  As the theorem states, (A18) does not price a safe linear opening,
residence, deeper upper windows, or the lower compiler.

## 8. Kempe rigidity

The subgraph `F_i union F_j` is a disjoint union of alternating cycles.
Swapping `i,j` on one such cycle leaves the unordered edge set
`F_i union F_j` unchanged.  At every lower row, the unordered pair of
middle neighbours is therefore unchanged.  Compression, all upper
multiplicities, the duplicate set, pair energy, and component count are
unchanged.

More generally, every proper recolouring involving only `i,j` on a fixed
two-colour subgraph is a collection of these component swaps.  Therefore
any move that changes the fixed pair selector while remaining a
one-factorization must exchange incidence edges with at least one third
factor colour.  This proves the stated three-colour gate.  It does not
prove that the available Boolean `C6` trades reach zero energy.

## 9. Final audited boundary

The theorem proves an exact owner/q1 reduction:

\[
 \boxed{
 \text{cap-two occurrence selector exists}
 \Longleftrightarrow
 \min_{\mathcal F}\min_{i<j}\Delta_{ij}=0.}
\]

It also gives the correct protected-colour and projected-topology
objectives and a rigorous obstruction to same-pair Kempe descent.

It does **not** prove that a zero-energy factor pair exists for every
`m`, that it can be made connected, that named physical occurrences can be
protected, or that the common-cap/all-width/residence/compiler gates can
be met.  Those remain separate existence problems.
