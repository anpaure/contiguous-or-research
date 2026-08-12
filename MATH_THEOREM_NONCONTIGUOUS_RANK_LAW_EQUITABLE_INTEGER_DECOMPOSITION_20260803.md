# Noncontiguous rank laws have an exact equitable integer decomposition

**Date:** 2026-08-03  
**Status:** unconditional integral rank-pattern theorem and exact reduction
of the remaining named-target gate.  No computation is used.  This theorem
does **not** produce an integral named Boolean-chain factor.

## 0. Outcome

Let `H=(A,B;E)` be a bipartite graph, let `W,d` be positive integers, and
let

\[
                         n=(n_e:e\in E)\in\mathbb Z_{\ge0}^{E}
\tag{0.1}
\]

satisfy

\[
 n(\delta(v))\le W\quad(v\in A\cup B),
 \qquad n(E)\le dW .
\tag{0.2}
\]

Then the multiset containing `n_e` copies of every edge `e` can be
partitioned into `W` matchings

\[
                         M_1,\ldots,M_W                         
\tag{0.3}
\]

whose sizes differ by at most one.  In particular,

\[
 |M_i|\le d,
 \qquad
 \sum_{i=1}^{W}{\bf1}_{\{e\in M_i\}}=n_e .
\tag{0.4}
\]

Thus every integral point of the `W`-dilate of the cardinality-capped
bipartite matching polytope decomposes into exactly `W` integral points,
and the decomposition can be made equitable.  This is an integer-
decomposition property stronger than the fractional convex decomposition
used in
`MATH_THEOREM_NONCONTIGUOUS_COLLAR_RESIDUAL_RANK_MATCHING_POLYTOPE_20260803.md`.

Apply this to its rank graph: residual rank edges form a path and collar
rank edges are isolated.  If

\[
 n_s=Wq_s\in\mathbb Z,
\quad n_s+n_{s+1}\le W\quad(s,s+1\text{ residual}),
\quad \sum_s n_s\le dW,
\tag{0.5}
\]

then there are exactly `W` rank patterns `R_i` such that

* `|R_i|<=d`;
* no `R_i` contains adjacent residual ranks;
* collar ranks may occur in arbitrary noncontiguous combinations; and
* rank `s` occurs in exactly `n_s` patterns.

Moreover every pattern has size either

\[
 \left\lfloor{\sum_sn_s\over W}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil{\sum_sn_s\over W}\right\rceil .
\tag{0.6}
\]

For the optimal triangular inventory, take

\[
 n_s={2r\choose s}-b_s,
\tag{0.7}
\]

where the integer `b_s` are the Ferrers boundary multiplicities.  Whenever
the hypotheses of the noncontiguous-collar theorem hold, (0.5) holds and
the entire collar--residual rank inventory rounds **exactly**, with no
`o(W)` error and no load imbalance.

What remains is an occurrence-labelled transversal problem.  One must
choose which `b_s` named targets go to the literal boundary chains and then
assign every other named target to the scheduled owner/rank positions so
that the positions belonging to one owner form one inclusion flag.  The
rank theorem proves none of that correlation.  Section 3 gives its exact
configuration-hypergraph formulation and explains why ordinary bipartite
integrality has already been fully used.

## 1. Equitable edge colouring

### Lemma 1.1 (balanced proper edge colouring)

Let `G` be a bipartite multigraph with maximum degree at most `W`.  Its
edges have a proper `W`-colouring in which all colour-class sizes differ by
at most one.

### Proof

By Koenig's line-colouring theorem, `G` has a proper edge colouring with
`Delta(G)<=W` colours.  Add empty colours until there are exactly `W`.

Suppose two colour classes `E_i,E_j` satisfy

\[
                         |E_i|\ge |E_j|+2.               
\tag{1.1}
\]

The subgraph induced by these two colours has maximum degree at most two.
Every component is an alternating path, an even alternating cycle, or an
isolated edge.  On each component the difference

\[
             \#\{i\hbox{-edges}\}-\#\{j\hbox{-edges}\}
\]

belongs to `{-1,0,1}`.  Equation (1.1) implies that some component has
difference `+1`.  Interchange colours `i,j` on that component.  Properness
is preserved, while `|E_i|` decreases by one and `|E_j|` increases by one.
Consequently

\[
                         \sum_{h=1}^{W}|E_h|^2
\]

strictly decreases.  Repeat.  The nonnegative integer potential forces
termination, and at termination no two class sizes differ by two.  Hence
they differ by at most one.  `square`

Parallel edges cause no difficulty.  A proper colouring gives them
different colours; a two-edge parallel component is an even alternating
cycle and has colour difference zero.

## 2. Exact rank-pattern decomposition

Replace every edge `e` of `H` by `n_e` parallel copies, producing a
bipartite multigraph `G_n`.  The degree of `v` is exactly
`n(delta(v))`, so (0.2) gives `Delta(G_n)<=W`.  Apply Lemma 1.1.  Every
colour class is a matching in `H`, counted with the available edge
multiplicities, and the classes partition the multiset (0.1).

Put `N=n(E)`.  Equitability says that every class has size
`floor(N/W)` or `ceil(N/W)`.  Since `N<=dW`, the latter is at most `d`.
This proves (0.3)--(0.4).

For the noncontiguous collar graph, a matching is exactly a rank set with
no adjacent residual ranks and unrestricted collar part.  Give its edge
`e_s` multiplicity `n_s`.  Its path-vertex degrees are
`n_s+n_(s+1)`, its isolated-edge endpoint degrees are `n_s`, and its total
edge count is `sum_s n_s`.  Thus (0.5) is exactly (0.2), and the colour
classes give the claimed patterns.

For (0.7), `Wq_s=binom(2r,s)-b_s` is integral.  The adjacent and total
rows are precisely the corresponding inequalities in the audited
fractional theorem, multiplied by `W`.  Therefore its optimal inventory
has an exact equitable integral pattern schedule.

Two useful boundary cases become transparent.

1. If the owner bank carries exactly `dW` targets after the triangular
   boundary removal, then **every** pattern has size exactly `d`.
2. If it carries `N<dW` targets, the only pattern sizes are
   `floor(N/W)` and `ceil(N/W)`; the number of larger patterns is exactly

   \[
                         N-W\left\lfloor{N\over W}\right\rfloor .
   \tag{2.1}
   \]

Hence neither a fractional owner load nor a collar/residual covariance is
needed to balance the scalar capacity.  All remaining nonintegrality is
label-level.

## 3. The exact named-target gate after rank rounding

Fix one equitable pattern schedule

\[
                         \mathcal R=(R_1,\ldots,R_W).
\tag{3.1}
\]

Let `O=binom([2r],r)` be the owner set.  Temporarily fix, for each rank
`s`, the named boundary family `B_s subset binom([2r],s)` of cardinality
`b_s`; put

\[
                         L_s={ [2r]\choose s}\setminus B_s .
\tag{3.2}
\]

Build the configuration hypergraph `K(mathcal R,B)` with three kinds of
vertices:

* one pattern vertex `p_i` for each `i in [W]`;
* one owner vertex `o_T` for each `T in O`; and
* every residual named target `S in L_s`.

For every bijective owner choice locally represented by a pair `(i,T)` and
every ordering `pi` of the coordinates of `T`, put in one configuration
edge

\[
 \{p_i,o_T\}\cup
 \{\text{the first }s\text{ coordinates of }\pi:s\in R_i\}.
\tag{3.3}
\]

### Proposition 3.1 (configuration matching equivalence)

For fixed `mathcal R` and fixed boundary families `B_s`, the owner bank has
an exact named-target flag realization if and only if
`K(mathcal R,B)` has a matching of size `W` covering every pattern vertex,
every owner vertex, and every target vertex in (3.2).

### Proof

A realization assigns every pattern to one distinct owner and chooses one
owner ordering.  Its scheduled prefixes are pairwise distinct and exhaust
the residual targets exactly when the corresponding `W` configuration
edges are disjoint and cover the three shores.  This is precisely the
stated matching.  Reading a covering matching backwards gives the owner
assignment and orderings.  `square`

The proposition remains only a reduction.  The edge-colouring proof in
Sections 1--2 acts on rank copies and forgets both containment and
prefix nesting.  Ordinary rank-by-rank bipartite matching also does not
solve (3.3): it can assign one target to each selected owner/rank port, but
assignments at different ranks of one owner need not be comparable.  The
explicit `k=5` rank-simple example in
`MATH_THEOREM_EQUITABLE_RANK_SIMPLE_IDEAL_SDR_AND_MTF_CHAINIZATION_GATES_20260803.md`
exhibits exactly this failure for a fixed owner assignment.

There is a sharper Boolean obstruction to assigning the abstract pattern
colours to owners arbitrarily.

### Proposition 3.2 (coordinate-halfspace owner-label obstruction)

Fix a demanded rank `s<r` for which `n_s<=W/2`.  Let `I_s` be the set of
the `n_s` patterns containing rank `s`.  There is a bijection between the
pattern labels and the rank-`r` owners for which at least

\[
                         {2r-1\choose s-1}-b_s
\tag{3.4}
\]

of the nonboundary rank-`s` targets have no compatible active owner.

In the central residual band of the noncontiguous-collar theorem this can
be `Theta(W)`, despite the exact rank inventory and perfectly equitable
pattern sizes.

### Proof

Fix a coordinate `x`.  Exactly

\[
 {2r-1\choose r}={W\over2}
\tag{3.5}
\]

rank-`r` owners avoid `x`.  Since `n_s<=W/2`, choose `n_s` such owners and
map the pattern labels in `I_s` bijectively onto them.  Extend this to an
arbitrary bijection of all pattern labels with all owners.

Every active owner at rank `s` now avoids `x`.  Therefore none contains a
rank-`s` target containing `x`.  There are `binom(2r-1,s-1)` such targets;
the literal boundary family can remove at most `b_s` of them.  All the
others are isolated from the active rank-`s` ports, proving (3.4).
`square`

The proposition is not a no-go for a jointly selected owner labelling.  It
is an exact warning about the quantifiers: first balancing abstract rank
patterns and then applying an arbitrary owner permutation can create a
linear named-target defect.  At minimum the final construction must make
every active-owner shore pass the ordinary Boolean inclusion Hall cuts;
after that, the cross-rank prefix nesting is still additional.

Thus the next integral theorem is not an integer-decomposition theorem for
the rank polytope.  That theorem is now proved.  It is one of the following
equivalent Boolean-specific tasks:

1. find the boundary families and an equitable schedule for which the
   configuration hypergraph (3.3) has a perfect matching;
2. prove a switching/absorption theorem that turns the rank-separated
   assignments into ownerwise flags; or
3. construct an ordered Hall ladder whose path-length histogram is exactly
   the equitable histogram (0.6).

Any `o(W)` version may leave `o(W)` configuration vertices or targets, but
it still implies the unit-scale chain-deletion conclusion
`gamma_d(2r)=o(W)` from
`MATH_THEOREM_DENSE_FERRERS_UNIT_SCALE_CHAIN_DELETION_BARRIER_20260803.md`.
Consequently the proved rank decomposition must not be cited as a named-
target rounding or as an `O(1)` construction.

## 4. Precise gain over the fractional theorem

The previous noncontiguous-collar theorem supplied a probability law on
rank patterns.  In principle, clearing denominators and rounding its
weights could have introduced one error for every pattern in a large
convex decomposition.  The present theorem proves that no such error is
necessary:

\[
 \boxed{
 \begin{array}{c}
 \text{exact collar rank counts;}\\
 \text{exact residual rank counts;}\\
 \text{exact no-adjacent residual constraint;}\\
 \text{exact owner count }W;\\
 \text{optimal equitable owner loads.}
 \end{array}}
\tag{4.1}
\]

All five assertions hold simultaneously and integrally.  The only missing
lower-side correlation is which named Boolean sets occupy those positions
on one common family of owner flags (together with the literal Ferrers
boundary selection).
