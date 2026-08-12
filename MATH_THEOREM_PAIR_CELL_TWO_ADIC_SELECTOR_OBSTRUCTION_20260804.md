# The two-adic obstruction to a whole-pair-cell selector

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical obstruction and exact two-frame
selector theorem.  The obstruction applies to any number of pairing
frames.  It shows that the seam-free whole-cell selector cannot solve the
residence problem whenever the required cell dimension satisfies
`M>s_2(r)`, as it eventually does under Corollary 2.2's growth assumptions.
It does not rule out selectors which cut cells into resident paths and
splice those paths.

## 1. Pair cells and their sizes

Throughout, `r>=1` and all cell-dimension thresholds are nonnegative
integers.

Let `P` be a perfect pairing of `[2r]`.  For an `r`-set `T`, record, for
each pair of `P`, whether `T` contains zero, one, or two of its endpoints.
The owners with one fixed record form a **pair cell**.  If the record has
exactly `m` singleton pairs, then the choices of one endpoint in those
singleton pairs are independent.  Thus the cell has exactly

\[
                              2^m                                      \tag{1.1}
\]

owners and is an induced `m`-cube under the usual single-pair flip
adjacency.  In particular, a cell good at threshold `M` has cardinality
divisible by `2^M`.

Write

\[
                  W_r=\binom{2r}{r}
\]

for the number of middle owners, and let `s_2(r)` denote the number of ones
in the binary expansion of `r`.

### Lemma 1.1 (exact middle-layer valuation)

\[
                         \nu_2(W_r)=s_2(r).                         \tag{1.2}
\]

#### Proof

Legendre's identity gives

\[
                 \nu_2(n!)=n-s_2(n).
\]

Since `s_2(2r)=s_2(r)`,

\[
\begin{aligned}
 \nu_2\binom{2r}{r}
 &=2r-s_2(2r)-2(r-s_2(r))\\
 &=s_2(r).
\end{aligned}
\]

\(\square\)

## 2. The obstruction

### Theorem 2.1 (whole-cell selector obstruction)

Take any family of perfect-pairing frames on `[2r]`, finite or infinite.
If the middle layer is partitioned into whole pair cells, all of dimension
at least `M`, then

\[
                            M\le s_2(r).                            \tag{2.1}
\]

Consequently, no such partition exists when `M>s_2(r)`.  Since
`s_2(r)<=floor(log_2 r)+1`, it certainly cannot exist whenever

\[
                         M>\lfloor\log_2 r\rfloor+1.             \tag{2.2}
\]

#### Proof

Every selected cell has size divisible by `2^M`, by (1.1).  Hence their
disjoint union has size divisible by `2^M`.  The union is the full middle
layer, whose size has two-adic valuation `s_2(r)` by Lemma 1.1.  Therefore
`M<=s_2(r)`. \(\square\)

This theorem applies in particular to the seam-free exact-cover equations

\[
 x_C\in\{0,1\},\qquad
 \sum_{C\ni T}x_C=1\quad\left(T\in\binom{[2r]}r\right),            \tag{2.3}
\]

when every available column `C` is a good cell of dimension at least `M`.
Summing all equations in (2.3) gives

\[
             \sum_C 2^{\dim C}x_C=W_r,                            \tag{2.4}
\]

and reduction modulo `2^M` is already a contradiction whenever
`M>s_2(r)`, in particular under (2.2).

### Corollary 2.2 (the current residence threshold is beyond the obstruction)

Let `D=D(r)` tend to infinity faster than `log r`, and let `h(D)` be any
local-cube threshold with `h(D)>=D`.  For all sufficiently large `r`, a
cover of the owner layer by cells of dimension at least `h(D)` cannot be
made disjoint by selecting whole cells.

In particular this applies to the explicit syndrome-quotient threshold,
where `h(D)` is the least power of two at least `4D`, and to the OR-word
regime `D=Theta(sqrt(r))`.

The conclusion is independent of how much frame redundancy is available.
Adding all perfect pairings does not remove the obstruction.

### Proposition 2.3 (a literal three-frame obstruction at the coarse threshold boundary)

The coarse threshold test `M<=s_2(r)` from Theorem 2.1 is necessary for a
selector at a prescribed good threshold, but passing that test is not
sufficient for a given available family.  There are three actual pair-cell
frames which cover every owner twice by good cells but have no whole-cell
exact cover.

#### Proof

Take `r=2` on the ground set `{1,2,3,4}` and use the three perfect
pairings

\[
 12|34,\qquad 13|24,\qquad 14|23.                              \tag{2.5}
\]

Set `M=1`.  In each frame there is one good dimension-two cell: the four
two-subsets transversal to that pairing.  The two matching edges themselves
are the two bad dimension-zero cells.  Every two-subset is a matching edge
in exactly one of (2.5), so it belongs to the good cell in each of the other
two frames.

Let `x_i` indicate selection of the good cell in frame `i`.  The three
types of owner rows are

\[
       x_2+x_3=1,\qquad x_1+x_3=1,\qquad x_1+x_2=1.             \tag{2.6}
\]

Their unique real solution is `x_1=x_2=x_3=1/2`, so there is no binary
solution.  This is a literal pair-cell instance, not an abstract partial
factor gadget. \(\square\)

Here `s_2(2)=1=M`, so the coarse reduction modulo `2^M` does not rule out a
partition.  However, every available cell in this example has dimension
two and size four, so the stronger reduction modulo four already rules out
an integral cover of the six owners.  The triangle equations display the
same fractional-integral failure explicitly.  Thus this literal example
shows that the necessary inequality involving only the minimum threshold
`M` is not sufficient; it does not isolate an incidence obstruction
independent of the exact available cell sizes.

## 3. A genuine fractional-integral gap

The obstruction is not a failure of fractional owner supply.

Fix an admissible dimension `m`, meaning

\[
                  0\le m\le r,\qquad m\equiv r\pmod2.
\]

Let `H_m` be the occurrence-labelled hypergraph whose vertices are the
middle owners and whose edges are all dimension-`m` pair cells in all
perfect pairings.  Every edge has size `2^m`.

### Theorem 3.1 (regular fractional cover, no integral cover)

The hypergraph `H_m` has a fractional exact cover.  If `m>s_2(r)`, it has
no integral exact cover.

#### Proof

Admissibility gives an actual cell: choose `m` singleton pairs,
`(r-m)/2` full pairs, and `(r-m)/2` empty pairs in any fixed pairing.
The symmetric group on `[2r]` acts transitively on the middle owners and
preserves the occurrence-labelled family of dimension-`m` cells.  Hence
every owner lies in the same positive number `a_m` of edges of `H_m`.
Assigning weight `1/a_m` to every edge gives total incident weight one at
every owner, so it is a fractional exact cover.

An integral exact cover would partition `W_r` vertices into sets of size
`2^m`; hence `2^m` would divide `W_r`.  Lemma 1.1 rules this out for
`m>s_2(r)`. \(\square\)

Thus even the maximally symmetric all-pairings host has an exact fractional
owner factor but no whole-cell integral factor in the relevant dimension.
Ordinary regularity, fractional Hall, or a putative total-unimodularity
argument on the whole-cell incidence matrix cannot close the selector.

## 4. Exact two-frame selector theorem

There is also a complete characterization for two fixed frames.  This
isolates the obstruction before the genuinely three-partite exact-cover
problem appears.

Let `P,Q` be two partitions of a finite universe `V`; in the application
they are the pair-cell partitions induced by two perfect pairings.  Mark
some blocks on each shore as available.  Form the bipartite intersection
graph `Gamma(P,Q)`: its vertices are the blocks of `P` and `Q`, with an edge
`AB` when `A cap B` is nonempty.

### Theorem 4.1 (two-partition exact selector)

There is an exact cover of `V` by available whole blocks from `P union Q`
if and only if no connected component of `Gamma(P,Q)` contains both

* an unavailable block of `P`, and
* an unavailable block of `Q`.

#### Proof

Give every `P`-block a variable `x_A` and every `Q`-block a variable `y_B`.
For an element in `A cap B`, exact coverage is

\[
                              x_A+y_B=1.                         \tag{4.1}
\]

Unavailable variables are fixed to zero.  Along a connected component of
the bipartite intersection graph, (4.1) forces all `P` variables to one
common value `c` and all `Q` variables to `1-c`.  An unavailable `P` block
forces `c=0`, while an unavailable `Q` block forces `c=1`.  These demands
are compatible exactly under the stated condition.  If neither shore is
forced, choose either `c=0` or `c=1`.  Every resulting variable is binary
and (4.1) covers every element exactly once. \(\square\)

For pair-cell partitions, the connected components have a concrete token
interpretation.  The multigraph `P union Q` on `[2r]` is a disjoint union
of alternating even cycles.  Moving within one `P`- or `Q`-cell toggles a
singleton pair, which is exactly a legal exclusion-process move of one
token along an edge of `P union Q`.  More explicitly, two owners are in
the same component of `Gamma(P,Q)` exactly when they can be joined by a
sequence in which consecutive owners lie in one common `P`- or `Q`-cell;
within such a cell, the differing singleton choices can be toggled one at
a time.  Thus this equivalence relation is the configuration graph for
indistinguishable exclusion tokens moving on `P union Q`.

Token number in every connected component of `P union Q` is invariant.
Conversely, the fixed-`k` token graph of any connected finite graph is
connected.  One quick proof is to pass to a spanning tree and induct on
the number of vertices, using a leaf: configurations with the same leaf
occupancy connect by induction after deleting the leaf, while different
leaf occupancies can first create a vacancy at its neighbour and move the
leaf token.  Applying this independently on the components of `P union Q`
proves that two middle owners lie in the same component of
`Gamma(P,Q)` precisely when they have the same number of chosen
coordinates in every connected component of `P union Q`.

In particular, if `P union Q` is one alternating cycle, then
`Gamma(P,Q)` is connected.  If the good threshold exceeds `r mod 2`, each
shore has an unavailable cell: a pairing has a cell of minimum dimension
`r mod 2`, obtained by taking whole pairs and, when `r` is odd, one
singleton pair.  Theorem 4.1 then rules out a whole-cell selector using
those two frames.

### Theorem 4.2 (exact three-partition deletion-component reduction)

Let `P,Q,R` be three partitions of a finite universe `V`, with specified
available blocks.  An exact cover by available blocks exists if and only if
there is a subfamily `S` of available `R`-blocks with the following
property.

Put

\[
                         U_S=\bigcup_{C\in S}C.                  \tag{4.2}
\]

On the residual universe `V minus U_S`, form the bipartite intersection
graph of the restricted `P`- and `Q`-blocks.  A nonempty residual `P`- or
`Q`-block is declared forbidden when its original block was unavailable or
when its original block meets `U_S`.  Then no connected component of the
residual intersection graph may contain a forbidden block on both shores.

#### Proof

Suppose an exact cover is given and let `S` be its selected `R`-blocks.
No selected `P`- or `Q`-block can meet `U_S`, because that would double
cover an element.  After removing `U_S`, the selected `P`- and `Q`-blocks
give an exact cover of the residual universe.  Theorem 4.1 applied to the
restricted partitions gives the stated component condition.

Conversely, choose `S` satisfying that condition.  Apply Theorem 4.1 on
the residual universe, treating every unavailable block and every block
meeting `U_S` as unavailable.  This gives an exact residual cover by full
`P`- and `Q`-blocks disjoint from `U_S`.  Adding `S` gives an exact cover of
`V`, since the blocks in `S` are pairwise disjoint as members of the
partition `R`. \(\square\)

Thus the exact three-frame whole-cell selector is a **component-separator
problem**: selected cells of one frame must delete owner edges so that no
residual two-frame component is forced to choose both shores.  This is a
condition involving intersection connectivity, not merely owner
multiplicity.  Any comparison with a separately defined successor-Hall
condition requires that condition's own hypotheses and is not part of this
theorem.  In the high-dimensional whole-cell regime Theorem 2.1 shows that
no separator choice can satisfy the full exact-cover equations; after
cells are cut into paths, the all-whole-cell divisibility contradiction no
longer applies.  The cuts must instead satisfy the residue condition in
Section 5, and an analogous macro-level separator problem remains
meaningful.

## 5. What every successful cut-and-splice selector must carry

Suppose a successful owner partition uses some whole good cells and some
proper blocks cut from good-cell chronologies.  If the proper blocks have
sizes `b_1,...,b_t`, then

\[
                  \sum_{j=1}^t b_j\equiv W_r\pmod {2^M}.       \tag{5.1}
\]

Indeed, all whole-cell contributions vanish modulo `2^M`.  In particular,
when `M>s_2(r)`, at least one selected proper block has

\[
                       \nu_2(b_j)\le s_2(r).                    \tag{5.2}
\]

More generally, no block library in which every allowable block size is
divisible by `2^{s_2(r)+1}` can partition the middle layer.

This is the exact arithmetic role of the cuts: they must carry the
middle-layer residue which whole cubes cannot carry.  This conclusion does
not by itself force the proper blocks to have different lengths.  It
categorically rules out any library whose block sizes are all divisible by
`2^{s_2(r)+1}`.  In particular, for a uniform power-of-two length `2^q`,
the two-adic count rules it out when `q>=s_2(r)+1` but not when
`q<=s_2(r)`.  For arbitrary uniform lengths, odd-part divisibility and the
feasible number of blocks can impose additional restrictions not captured
by (5.2).  A macro-resident Hall theorem may still be applied after cuts,
subject to its separate geometric hypotheses.

## 6. Revised selector frontier

The three-frame cover theorem and the resident-cube theorem together give
every owner at least one local resident whole-cell chronology.  At a
threshold `M>s_2(r)`, Theorem 2.1 proves that those chronologies cannot
simply be selected whole.

Therefore, within the pair-cell chronology route, a successful selector
must have the form

\[
 \boxed{\text{cut good-cell cycles into residue-carrying resident paths}
        +\text{ prove macro Hall/holonomy for their seams}.}
\]

More generally, the theorem forces any solution at this threshold to
abandon an all-whole-cell owner partition; it does not force every possible
construction to arise by cutting these particular chronologies.  It does
not disprove a resident spanning factor: cutting a cell changes the
arithmetic, and macro-Hall or switch-tree tools may still apply once their
separate hypotheses have been met.

There is one further exact consequence for the switch-tree route.  A
two-edge switch preserves the degree of every owner, hence both vertex
support and vertex multiplicities in the switched edge union.  Therefore a
switch-only tree which starts from whole good-cell cycles and merely merges
2-factor components presupposes that those cycles already form a spanning,
vertex-disjoint family, equivalently a whole-cell owner partition.  Such a
start is ruled out by Theorem 2.1 when `M>s_2(r)`.  Switch-tree
Hamiltonization can still be used after a cut-and-splice selector has
produced a spanning resident factor.  The theorem also does not address a
procedure which changes the selected blocks, rather than using switches
alone; it says only that edge switches cannot repair owner multiplicities
or holes in a fixed initial whole-cell family.
