# The canonical MSW second shadow fails linearly, but the complete target row has a degree-two rainbow owner realization

**Date:** 2026-08-13  
**Status:** unconditional canonical no-go; unconditional positive incidence
reduction; exact all-rank wreath completion remains open

## 1. Notation and the second-shadow row

Put

\[
 n=2m+1,\qquad
 \mathcal O={ [n]\choose m},\qquad
 \mathcal S={ [n]\choose m-1},
\]

and write

\[
 W=|\mathcal O|={2m+1\choose m},\qquad
 N=|\mathcal S|={2m+1\choose m-1}={m\over m+2}W.       \tag{1.1}
\]

An exact wreath factor is a family of

\[
 B={W\over 2m+1}=\operatorname {Cat}_m                 \tag{1.2}
\]

cyclic orders whose length-`m` cyclic windows partition `mathcal O`.
Its second shadow is the family of all length-`m-1` windows in the same
orders.  Equivalently, view each order as a Johnson cycle on its
length-`m` windows.  A length-`m-1` target `S` occurs precisely when the
cycle uses an edge whose two endpoints have intersection `S`.

In the notation of
`MATH_THEOREM_LONG_APERTURE_MSW_OWNER_FACTOR_FLAT_EROSION_AND_SECOND_SHADOW_GATE_20260813.md`,
one has `m=r-1`, and this is exactly the rank-`r-2` gate.

## 2. The specific canonical MSW factor does not pass the gate

Let `F_m^MSW` be the canonical Chung--Feller/MSW wreath factor.  The
marked-gap theorem
`MATH_THEOREM_MSW_23_FIXED_HOLE_FLOOR_20260725.md`, independently audited
in `MATH_AUDIT_FULL_CANONICAL_23_CUBE_Q1_20260725.md`, proves that for all
sufficiently large `m`, the number of rank-`m-1` targets absent from
`F_m^MSW` is at least

\[
 (m-3)\operatorname {Cat}_{m-2}-{2W\over m+2}
   =\left({1\over32}-o(1)\right)W.                  \tag{2.1}
\]

The proof is intrinsic to the MSW Dyck recursion.  Briefly, the roots
obtained by inserting `1100` or `1010` at a marked gap give disjoint pairs
of equal second-shadow occurrences.  The insertion-gap-to-order-gap map is
a permutation, so a linear subfamily of these duplicate certificates is
fixed by `(2 3)`.  The exact fixed-target occurrence ledger then converts
their duplicate excess into the lower bound (2.1) on missing targets.

Thus the second-shadow condition is not hidden inside the published MSW
factor theorem:

\[
 \boxed{F_m^{\rm MSW}\text{ is not second-shadow-surjective.}}       \tag{2.2}
\]

Direct enumeration by `msw_shadow_test.cpp` gives the following finite
cross-check.  The entries are distinct canonical length-`m-1` windows
over all `N` possible targets.

\[
\begin{array}{c|c|c}
m&\text{covered}&\text{missing}\\ \hline
2&5/5&0\\
3&21/21&0\\
4&80/84&4\\
5&298/330&32\\
6&1111/1287&176\\
7&4168/5005&837\\
8&15739/19448&3709\\
9&59771/75582&15811\\
10&228070/293930&65860
\end{array}                                                        \tag{2.3}
\]

At `m=4`, the four literal missing triples are

\[
 \{1,4,7\},\quad \{2,5,8\},\quad
 \{2,5,9\},\quad \{4,7,9\}.                       \tag{2.4}
\]

The recursively defined target

\[
 S_m=[m-3]\cup\{2m-4,2m-1\}                         \tag{2.5}
\]

is absent in the direct canonical computation for every `4<=m<=11`.
This is useful diagnostic evidence, but (2.1), rather than extrapolation
from (2.5), is the unconditional all-large-`m` no-go.

## 3. The obstruction is not universal to wreath factors

`WREATH_FIRST_SHADOW_AUDIT.md` verifies a list of fourteen cyclic orders
on `[9]` with the following exact properties:

\[
 \mu_4(A)=1\quad(A\in {[9]\choose4}),                \tag{3.1}
\]

and

\[
 \#\{S:\mu_3(S)=1\}=42,
 \qquad
 \#\{S:\mu_3(S)=2\}=42.                            \tag{3.2}
\]

In particular, all `84` triples occur.  Hence a noncanonical exact
wreath factor passes the second-shadow gate at `m=4`.  No parity,
point-margin, or universal wreath invariant can force a hole.

The all-`m` existence question remains open; the rest of this note gives
two unconditional reductions which locate its genuinely chronological
part.

## 4. A rainbow linear forest from a saturating cycle

Form the adjacent-layer incidence graph

\[
 \mathcal B=(\mathcal S,\mathcal O;E),
 \qquad S A\in E\Longleftrightarrow S\subset A.       \tag{4.1}
\]

It is `(m+2,m)`-biregular: every `S` has `m+2` parents, and every owner
has `m` facets.

The saturating-cycle theorem of Gregor--Mička--Mütze, applied to the two
levels `m-1,m` of `B_n`, gives a simple alternating cycle

\[
 S_0\subset A_0\supset S_1\subset A_1\supset\cdots
 \supset S_{N-1}\subset A_{N-1}\supset S_0,          \tag{4.2}
\]

where the `S_i` are all members of `mathcal S` and the `A_i` are `N`
distinct owners.

### Theorem 4.1 (one-path rainbow forest)

For every `m>=2`, there is a graph `P_*` on `mathcal O` such that

1. `P_*` consists of one path with `N` edges and `N+1` vertices, together
   with `W-N-1` isolated owners;
2. the `N` path edges have pairwise distinct intersection colours and use
   every member of `mathcal S` exactly once; and
3. consequently `P_*` is a degree-two rainbow forest with exactly

   \[
   W-N={2W\over m+2}=\operatorname {Cat}_{m+1}       \tag{4.3}
   \]

   components.

#### Proof

Suppress the lower vertices in (4.2).  Consecutive owners `A_(i-1),A_i`
are distinct and both contain `S_i`, so

\[
 A_{i-1}\cap A_i=S_i.                               \tag{4.4}
\]

The suppression is therefore a simple Johnson cycle on the `N` used
owners, with every intersection colour exactly once.

There are `W-N>0` unused owners.  Choose one of them, say `U`, and choose
any facet `S_j subset U`.  The colour `S_j` occurs on the unique cycle
edge `A_(j-1)A_j`.  Delete that edge and add `U A_(j-1)`.  Since both
endpoints contain `S_j`, the new edge still has colour `S_j`.  It attaches
the formerly unused vertex `U` to one endpoint of the opened cycle.
The result is one path on `N+1` vertices with all `N` colours exactly
once.  Declare every other unused owner isolated.  This proves all claims.
`square`

Thus the rainbow-linear-forest problem is not an additional conjecture;
it is a direct consequence of the published saturating-cycle theorem.

### Theorem 4.2 (two-SDR rainbow owner graph)

There is a graph `P` on vertex set `mathcal O` such that

1. `Delta(P)<=2`;
2. `P` has exactly one edge of every intersection colour
   `S in mathcal S`;
3. consequently `P` is a disjoint union of paths, isolated vertices, and
   cycles; and
4. the number of path components, counting an isolated vertex as a path,
   is exactly

   \[
   W-N={2W\over m+2}=\operatorname {Cat}_{m+1}.       \tag{4.5}
   \]

#### Proof

By Koenig's line-colouring theorem, the bipartite graph `mathcal B` has a
proper edge-colouring with its maximum degree `m+2`.  At a left vertex
`S`, all `m+2` colours occur exactly once.  Therefore each colour class is
a matching which saturates all of `mathcal S`.

Choose two colour classes `M_0,M_1`.  For every `S`, let

\[
 A_j(S)\in\mathcal O
 \quad\text{be its mate in }M_j,qquad j=0,1.         \tag{4.6}
\]

The two owners are distinct, both contain `S`, and hence

\[
 A_0(S)\cap A_1(S)=S.                               \tag{4.7}
\]

Put the edge `A_0(S)A_1(S)` in `P`.  Each `M_j` is a matching, so every
owner occurs at most once in each phase; hence `Delta(P)<=2`.  Formula
(4.4) gives every colour exactly once.

Finally, `P` has `W` vertices and `N` edges.  In a graph of maximum degree
two, a path component contributes one to `|V|-|E|`, while a cycle
contributes zero.  Thus the number of path/isolate components is
`W-N`, proving (4.5). `square`

Relative to the desired number `B` of wreaths, the open-component count is

\[
 {W-N\over B}={2(2m+1)\over m+2}<4.                 \tag{4.8}
\]

The equality with `Cat_(m+1)` in (4.3) and (4.5) is exact, not
asymptotic.  It is
the adjacent-layer Catalan difference and suggests a recursive path-factor
interface: the rainbow owner graph has exactly the number of open
components occurring at the next Catalan order.

Thus target coverage and owner degree two can be achieved simultaneously
with fewer than four open paths per desired wreath, on average.  What is
not supplied by Theorem 4.2 is the cyclic-window chronology or even a
Johnson-adjacent closure of the path endpoints.

## 5. An acyclic rainbow realization

There is a complementary certificate which enforces acyclicity but not
the degree bound.

For `S in mathcal S`, let `E_S` be the edge set of the clique on its
`m+2` parents.  Every edge in `E_S` is a Johnson edge of colour `S`.

### Theorem 5.1 (Rado/dragon rainbow forest)

One can select one edge `e_S in E_S` for every `S in mathcal S` so that

\[
 \{e_S:S\in\mathcal S\}                             \tag{5.1}
\]

is a forest on `mathcal O`.

#### Proof

Apply Rado's independent-transversal theorem to the graphic matroid on
the complete graph with vertex set `mathcal O`.  It is enough to prove
that for every `X subseteq mathcal S`, the graph

\[
 G_X=\left(\Gamma(X),\bigcup_{S\in X}E_S\right)      \tag{5.2}
\]

has graphic rank at least `|X|`.

Let its nonempty connected components have colour sets
`X_1,...,X_c` and owner sets `V_1,...,V_c`.  The whole parent clique of a
colour lies in one component, so `V_j=Gamma(X_j)`.  Double-counting the
incidences from `X_j` to its upper shadow gives

\[
 (m+2)|X_j|\le m|V_j|.                              \tag{5.3}
\]

In particular, since `X_j` is nonempty,

\[
 |V_j|\ge |X_j|+1.                                  \tag{5.4}
\]

Therefore

\[
 \operatorname {rk}(G_X)
 =\sum_{j=1}^c(|V_j|-1)
 \ge\sum_{j=1}^c|X_j|=|X|.                         \tag{5.5}
\]

Rado's theorem now gives the claimed rainbow forest. `square`

This forest again has `N` edges and hence exactly `W-N` components.  It
need not have maximum degree two.

## 6. The exact remaining synthesis gate

The three positive certificates now have the following exact status:

\[
\begin{array}{c|c|c}
\text{certificate}&\text{all colours once}&\text{owner structure}\\ \hline
\text{saturating-cycle path}&\text{yes}&
  \text{one path plus }\operatorname {Cat}_{m+1}-1\text{ isolates}\\
\text{two-SDR graph}&\text{yes}&\Delta\le2,\text{ paths and cycles}\\
\text{Rado graph}&\text{yes}&\text{forest, degree unbounded}.
\end{array}                                                        \tag{6.1}
\]

Thus target coverage, acyclicity, and the degree-two owner constraint can
all be met simultaneously.  Even this is not yet a wreath factor.  Starting
from Theorem 4.1, the full completion must use the
`Cat_(m+1)-1` isolated owners, cut/rethread the long path, and produce `B`
cycles of length `2m+1`, each a literal wreath (equivalently, every
coordinate has one cyclic run of `m` ones in the lower-window order).

This gives the proof order

\[
 \boxed{
 \text{saturating rainbow path}
 \longrightarrow
 \text{Catalan-isolate chronological rethreading}
 \longrightarrow
 \text{wreath factor}.}                              \tag{6.2}
\]

The first object in (6.2) is unconditional.  The remaining arrow is not an
owner-capacity, Hall, degree, or cycle-avoidance problem.  It is the
genuinely chronological rethreading gate.

## 7. Exact conclusion

The answer for the cyclic orders of the **specific canonical MSW factor**
is negative, with linear rather than bounded defect.  The answer for
arbitrary exact wreath factors is positive at `m=4` and has no separate
target-capacity or degree-two obstruction for any `m`.

What remains unproved is an all-`m` theorem combining the unconditional
rainbow path with minimum-odd-cycle chronology.  Any claimed resolution of the
long-aperture second-shadow gate must therefore supply one of:

1. an all-`m` shadow-covering exact wreath factor;
2. a rethreading theorem which turns the saturating path and its
   `Cat_(m+1)-1` isolates into wreath cycles; or
3. a different owner chronology whose long-cell unions cover the same
   upper row.

The canonical MSW orders themselves cannot be used for this purpose.
