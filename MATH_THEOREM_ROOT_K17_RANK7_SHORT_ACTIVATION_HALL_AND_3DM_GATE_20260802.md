# Rank-seven short activation: exact Hall branches and the 3DM gate

**Date:** 2026-08-02  
**Status:** unconditional structural theorem for the compressed-normal
three-level recoupling model.  It proves that the static outer model is a
bipartite b-matching, while the pair-specific rank-seven-short condition is
not another flow in general.  It gives an exact fixed-mode Hall oracle and
proof-safe mode cuts.  It does not decide the special K17 containment
instance, construct typed sockets, or produce a word.

## 1. The integral outer model

Let

\[
 L=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Use containment-supported variables

\[
 a_{\ell m}\ (L\to M),\qquad
 b_{\ell r}\ (L\to R),\qquad
 c_{mr}\ (M\to R)
\]

and impose

\[
\begin{aligned}
 \sum_m a_{\ell m}+\sum_r b_{\ell r}&=1 &&(\ell\in L),\\
 \sum_r c_{mr}&=1 &&(m\in M),\\
 \sum_\ell b_{\ell r}+\sum_m c_{mr}&=1 &&(r\in R),\\
 \sum_\ell a_{\ell m}&\le1 &&(m\in M).
\end{aligned}                                                   \tag{1.1}
\]

This is the bipartite b-matching on left shore
`L dotcup M_out` and right shore `M_in dotcup R`.  Consequently its matrix
is totally unimodular.  Every integral solution is a compressed-normal
chain partition with

\[
 16915\ (L-M-R),\qquad 4862\ (L-R),\qquad 2533\ (M-R).          \tag{1.2}
\]

The adjective compressed-normal is load-bearing: chains with two members
of `L` are outside this face.

## 2. Pair-specific short activation

Let `p_mr` be one exactly when the short chain `m-r` passes a declared
marginal socket test.  A middle `m` is short precisely when it has no low
predecessor.  Hence the exact integer implication is

\[
 \boxed{
   \sum_{r:p_{mr}=0}c_{mr}\le \sum_\ell a_{\ell m}
 }
 \qquad(m\in M).                                             \tag{2.1}
\]

The individual rows

\[
 c_{mr}\le p_{mr}+\sum_\ell a_{\ell m}                       \tag{2.2}
\]

are integer-equivalent to (2.1), but (2.1) is fractionally stronger because
`sum_r c_mr=1`.

Direct short chains `ell-r` behave differently.  If a complete,
context-independent audit proves such a pair impossible, deleting the arc
`b_lr` merely deletes an edge of the b-matching and preserves total
unimodularity.  A zero from one frozen chronology is not a
context-independent audit after global recoupling.

## 3. Smallest fractional obstruction

Take one low vertex `ell`, two middles `m1,m2`, two roots `r1,r2`, all
`L-M` and `M-R` edges, and no `L-R` edge.  Declare the diagonal `M-R`
edges bad and the off-diagonal edges good.  Write

\[
 a_i=a_{\ell m_i},\qquad c_{ij}=c_{m_i r_j}.
\]

The base rows say

\[
 a_1+a_2=1,
\]

and make `c` a doubly stochastic `2 by 2` matrix.  The activation rows are

\[
 c_{11}\le a_1,\qquad c_{22}\le a_2.                         \tag{3.1}
\]

Every feasible point can be written

\[
 c_{11}=c_{22}=t,\quad c_{12}=c_{21}=1-t,\quad
 a_1=s,\quad a_2=1-s,
\]

where

\[
 0\le t\le s\le1-t.                                         \tag{3.2}
\]

Thus `(t,s)=(1/2,1/2)` is a fractional vertex.  The six active rows in
variable order `(a1,a2,c11,c12,c21,c22)` have determinant of absolute value
two.  Therefore (1.1)+(2.1) is not a network matrix or a totally unimodular
formulation.

## 4. General feasibility is NP-complete

The loss of integrality is not only an artefact of the formulation.

### Theorem 4.1 (activation matching contains exact 3DM)

For arbitrary three-level bipartite graphs, deciding whether (1.1) and
(2.1) have an integral solution is NP-complete.  This remains true with

1. no direct `L-R` arcs;
2. exactly one bad `M-R` arc incident with each middle; and
3. good `M-R` arcs forming disjoint complete group-to-private-root graphs.

#### Proof

Reduce from exact three-dimensional matching.  Let

\[
 X,Y,Z,\qquad |X|=|Y|=|Z|=n,
\]

and let `T subseteq X times Y times Z` be the triple family.  Assume every
`y` occurs in at least one triple; otherwise the instance is immediately
negative.  For each triple `tau=(x,y,z)` create a middle `m_tau`.  Put

\[
 L=X.
\]

Join `x` to `m_tau` exactly when `tau` has first coordinate `x`.

For a fixed `y`, let `g_y` be the number of triples with second coordinate
`y`, and create `g_y-1` private roots

\[
 p_{y,1},\ldots,p_{y,g_y-1}.
\]

The root shore is

\[
 R=Z\ \mathbin{\dot\cup}\
   \{p_{y,j}:y\in Y,\ 1\le j<g_y\}.
\]

Hence

\[
 |R|=n+\sum_y(g_y-1)=|T|=|M|.
\]

Join every `m_tau`, with `tau=(x,y,z)`, to

* its single shared root `z`; declare this edge bad;
* all `g_y-1` private roots in the `y`-group; declare these edges good.

There are no `L-R` arcs.

In any feasible matching, all `g_y-1` private roots of a `y`-group must be
filled by distinct middles of that group.  Exactly one middle of each group
therefore remains and must use its bad shared-`Z` edge.  Equation (2.1)
forces every such middle to receive a low predecessor.  There are exactly
`n` selected middles and exactly `n` low vertices.  Root saturation says
their triples use every `z` exactly once, and low saturation says they use
every `x` exactly once.  By construction they already use every `y` exactly
once.  They form an exact three-dimensional matching.

Conversely, from an exact 3DM choose its one triple in every `y`-group,
match that middle to its `z` root and its `x` predecessor, and match the
remaining group middles bijectively to the private roots.  All rows hold.
This is a polynomial reduction, while verification is polynomial.  QED.

Consequently there is no general reduction of the pair-specific activation
layer to ordinary matching, matroid intersection, gammoid intersection, or
submodular flow with polynomial separation oracles unless `P=NP`.  This is
a statement about arbitrary presentations, not a hardness theorem for the
special Boolean-containment K17 instance.

## 5. Exact Hall oracle after fixing the short middles

Let

\[
 S=\{m\in M:m\text{ is short}\},\qquad |S|=2533,
\]

and put `T=M setminus S`.  Form a bipartite graph `G_S` with

\[
 \text{left shore }L\mathbin{\dot\cup}M,
 \qquad
 \text{right shore }T\mathbin{\dot\cup}R.
\]

Its edges are

* `ell-m` for `m in T` when `ell subset m`;
* `ell-r` when `ell subset r`;
* `m-r` when `m subset r` and either `m in T` or `p_mr=1`.

Both shores have size

\[
 |L|+|M|=21777+19448=41225
 =16915+24310=|T|+|R|.
\]

### Theorem 5.1 (fixed-short Hall equivalence)

There is a compressed-normal chain recoupling with short-middle set exactly
`S` satisfying every marginal rank-seven short condition if and only if
`G_S` has a perfect matching.  Equivalently,

\[
 |N_{G_S}(A)|\ge |A|
 \qquad(A\subseteq L\mathbin{\dot\cup}M).             \tag{5.1}
\]

#### Proof

An outer solution matches every low and rank-seven target to its next
receiver.  Long middles `T` are required receivers and short middles `S`
are omitted.  A short middle may use only a good root edge; a long middle
may use any root edge.  This is exactly a perfect matching in `G_S`.
The converse reads the three chain types from such a matching.  Hall's
theorem gives (5.1).  QED.

Thus the exact global marginal problem has the min--max form

\[
 \boxed{
   \min_{S\subseteq M,\ |S|=2533}
   \max_{A\subseteq L\dot\cup M}
   \bigl(|A|-|N_{G_S}(A)|\bigr)_+ .
 }                                                           \tag{5.2}
\]

It is feasible exactly when (5.2) is zero.

Enumerating `S` gives an exact
`binom(|M|,2533) poly(|E|)` algorithm.  This is an XP-style exact branch,
not a useful FPT claim for K17.  There is, however, an FPT parameterization
by the number `q` of middles having both good and bad root options: branch
on the short/long mode of those `q` middles.  All-good middles may remain
unfixed, and all-bad middles are forced long.  Every branch is an ordinary
b-matching, giving running time `2^q poly(|E|)`.

## 6. Proof-safe mode--Hall cuts

Write

\[
 t_m=1_{m\in T}=1-1_{m\in S}.
\]

For a fixed left set `A`, put

\[
 A_L=A\cap L,\qquad A_M=A\cap M,
\]

and define the always-visible root bank

\[
 R_A^0=N_R(A_L)\ \cup\
       \bigcup_{m\in A_M}\{r:m\subset r,\ p_{mr}=1\}.        \tag{6.1}
\]

For `m in A_M`, let

\[
 B_m=\{r:m\subset r,\ p_{mr}=0\}\setminus R_A^0.
\]

Then the exact neighbour count under mode vector `t` is

\[
 f_A(t)=
 |N_M(A_L)\cap T|
 +\left|R_A^0\cup\bigcup_{m\in A_M\cap T}B_m\right|.        \tag{6.2}
\]

Every feasible mode vector satisfies the universal Hall row

\[
                         f_A(t)\ge |A|.                     \tag{6.3}
\]

The function in (6.2) is a monotone coverage function, hence submodular.
Its superlevel constraint is not a matroid rank inequality in general;
Theorem 4.1 explains why a polynomial family of ordinary flow cuts cannot
be expected for arbitrary inputs.

For a proof-safe MILP/Benders implementation, introduce occurrence-specific
root-neighbour variables `u_(A,r)` and enforce the exact OR

\[
 u_{A,r}=\bigvee_{m\in A_M:\ r\in B_m}t_m
 \qquad(r\notin R_A^0).                                    \tag{6.4}
\]

Then add

\[
 \sum_{m\in N_M(A_L)}t_m
 +|R_A^0|+
 \sum_{r\notin R_A^0}u_{A,r}
 \ge |A|.                                                   \tag{6.5}
\]

The OR must be bidirectional; allowing unsupported `u_(A,r)=1` makes the
cut unsound.  A deficient Hall shore returned at a fixed mode branch gives
one new globally valid row (6.4)--(6.5).  The weaker proof-safe fallback is
the exact-mode no-good

\[
                     \sum_{m\in S}1_{m\text{ short}}\le2532. \tag{6.6}
\]

Equation (6.6) is valid only because every mode vector has exactly 2533
short middles.

## 7. Boundary to literal sockets

The indicator `p_mr` records only marginal existence for the short pair.
Exact common-state selection still chooses a typed record

\[
                 (\text{short},\text{pred port},
                    \text{succ port},\text{state/address}).
\]

After fixing the complete shared state and one injective endpoint map, the
opposite endpoint choices and the residual long--long transitions combine
into one bipartite perfect matching.  Before that branch, the typed layer
contains arbitrary three-dimensional matching and is genuinely
hypergraphic.  A Hall cut from one state/endpoint branch must therefore be
conditioned on all outer, state, and endpoint literals used to build that
branch; transporting it as a naked root-bank cut is unsound.

Scope exclusions: a complete K17 global-union socket catalogue, supplier
Hall, connected topology, residence, upper shadows, source/compiler closure,
and a length-24313 word.
