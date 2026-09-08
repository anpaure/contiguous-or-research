# Chain-splitting surgery for ordered orthogonal decompositions

This note asks whether the `d=B(k)-W(k)` extra endpoint slots can be obtained
by splitting chains in a pair of orthogonal symmetric-chain decompositions
(SCDs), where

\[
 W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

The answer is not an automatic yes.  What *is* available is an exact
cycle-transversal theorem.  It identifies precisely what the `d` splits must
do, gives packing lower bounds that can disprove a proposed seed pair, and
separates cycle breaking from triangular support and pin survival.

No all-`k` bounded-splitting theorem is claimed here.

## 1. Splits and chain gaps

Let `P` be the punctured Boolean lattice.  Let

\[
 \mathcal L=\{L_1,\ldots,L_W\},\qquad
 \mathcal R=\{R_1,\ldots,R_W\}
\]

be orthogonal SCDs.  Thus every two chains, one from each family, meet in at
most one mask.

If

\[
 C=(C_a\subset C_{a+1}\subset\cdots\subset C_b),
 \qquad |C_t|=t,
\]

then a **gap** of `C` is one of the `b-a` positions between `C_t` and
`C_{t+1}`.  Cutting at a gap replaces `C` by its two nonempty contiguous
pieces.  Several cuts replace it by the corresponding consecutive rank
blocks.

One cut increases the number of chains by exactly one.  Therefore `d` cuts in
each family produce `W+d` chains in each endpoint decomposition.  Splitting
preserves all of the following automatically:

* the partition of the masks;
* the chain property;
* orthogonality between the two families.

It does **not** automatically preserve symmetry, nor is symmetry needed after
the surgery.

For two masks `X subset Y` in one chain, write

\[
 G_C(X,Y)
\]

for the set of chain gaps between them.  They remain in the same piece after a
cut set `K` exactly when

\[
 K\cap G_C(X,Y)=\varnothing. \tag{1.1}
\]

This elementary observation is the basis of the exact obstruction below.

## 2. Alternating precedence cycles

The incidence graph has the chains of `mathcal L` and `mathcal R` as its two
vertex classes and one rank-labelled edge for every mask.  It is simple by
orthogonality.

First consider only the desired order of the right pieces: as rank increases
inside a left piece, the indices of the incident right pieces must increase.

### Definition 1 (right alternating cycle certificate)

A right alternating cycle certificate of length `t` consists cyclically of

\[
 R_1,L_1,R_2,L_2,\ldots,R_t,L_t,R_1
\]

and masks

\[
 x_i\in L_i\cap R_i,\qquad
 y_i\in L_i\cap R_{i+1},qquad |x_i|<|y_i|, \tag{2.1}
\]

where indices are modulo `t`.  Repeated original chains are allowed; this is
important because two different pieces of one original chain may occur in a
cycle after surgery.

The certificate forces

\[
 R_1<R_2<\cdots<R_t<R_1 \tag{2.2}
\]

provided that the two masks displayed at every occurrence of a chain have not
been separated by a cut.

Its **cut support** is

\[
 \operatorname{supp}(\Gamma)=
 \bigcup_{i=1}^t G_{L_i}(x_i,y_i)
 \;\cup\!
 \bigcup_{i=1}^t G_{R_i}(y_{i-1},x_i). \tag{2.3}
\]

The notation in the second union means all gaps between the two masks,
regardless of which has smaller rank.

There is a left alternating cycle certificate obtained by interchanging the
two families and reversing the required rank direction: along a right piece,
left indices must decrease as rank increases.  Let `mathfrak C_R` and
`mathfrak C_L` denote the two families of certificates.

### Theorem 2 (exact cycle-transversal theorem)

Let `K_L,K_R` be gap cuts in the two SCDs, and put `K=K_L union K_R`.
After splitting at these gaps, both required local chain orders exist if and
only if

\[
 K\cap\operatorname{supp}(\Gamma)\ne\varnothing
 \quad\hbox{for every }\Gamma\in
 \mathfrak C_L\cup\mathfrak C_R. \tag{2.4}
\]

Consequently, the minimum total number of cuts needed to obtain the two local
orders is exactly the transversal number of the hypergraph whose vertices are
chain gaps and whose hyperedges are the supports (2.3).  The constraint of at
most `d` cuts in each family is the corresponding two-coloured transversal
problem.

#### Proof

Suppose a certificate `Gamma` is not hit.  Equation (1.1) says that `x_i,y_i`
remain together in one left piece, and `y_{i-1},x_i` remain together in one
right piece.  Hence the refined pieces still force every comparison in (2.2),
which is impossible in a linear order.  The same argument applies to left
certificates.

Conversely, suppose the refined right-precedence digraph has a directed cycle.
For every arc choose the left piece and the two masks that generate it.  At
each right vertex of the directed cycle, the incoming and outgoing masks lie
in the same refined right piece.  Projecting all pieces back to their original
chains gives a certificate of the form (2.1), and none of the gap intervals in
(2.3) was cut.  Thus it is an unhit certificate.  The identical projection
argument works for a directed cycle in the refined left-precedence digraph.

If all certificates are hit, both refined precedence digraphs are acyclic, so
topological orders give the two desired local orders.  QED.

### Corollary 3 (cycle-packing obstruction)

If `q` alternating cycle certificates have pairwise disjoint cut supports,
then every ordering surgery uses at least `q` cuts.  In particular, a
`W+d`-piece surgery is impossible if there are more than `2d` such
support-disjoint certificates.  A packing supported entirely on gaps from one
family gives the sharper obstruction `q>d` for that family.

The same conclusion follows from any fractional packing of certificates: the
fractional packing number is a lower bound for the integral cut number.

This gives a concrete way to disprove bounded repair of a proposed orthogonal
pair without searching over all orders.

## 3. A positive one-sided splitting lemma

There is a useful simpler sufficient condition when cuts are assigned to the
family that generates the offending comparisons.

For every unsplit left chain, list the right chains it meets in increasing
rank order.  Put an arc between each two consecutive names.  A cut in that
left chain deletes exactly the corresponding occurrence of an arc.  Parallel
occurrences are retained separately.

### Lemma 4 (generator-side feedback surgery)

If at most `d` left-chain gaps can be cut so that the resulting right
precedence digraph is acyclic, and at most `d` right-chain gaps can be cut so
that the resulting left precedence digraph is acyclic, then the two refined
chain families admit the required local orders.

#### Proof

Topologically order the original right-chain names after the left cuts.  If a
right chain was itself split, put all of its pieces consecutively at the
location of that name.  Orthogonality implies that one left piece meets at
most one piece of any original right chain, so this refinement creates no new
comparison inside the block of pieces.  It therefore remains a valid right
order.  Apply the symmetric argument to order the left pieces.  QED.

Lemma 4 is only sufficient, whereas Theorem 2 is exact: a cut in a target-side
chain can also open a directed cycle by cloning one of its vertices.

## 4. The adjacent-middle feedback invariant

For `k=2m`, identify every chain of an SCD with its unique middle `m`-set.  Let
`F_-` be the partial-permutation digraph defined by rank-`m-1` masks:

\[
 X\longrightarrow Y
 \quad\Longleftrightarrow\quad
 X\cap Y\hbox{ lies in left chain }X
 \hbox{ and right chain }Y. \tag{4.1}
\]

Let `F_+` be defined by rank-`m+1` masks and consecutive unions.  Before any
splitting, the middle-chain precedence object is the occurrence-labelled
directed multigraph

\[
 P_{\rm mid}=F_-^{\rm rev}\uplus F_+. \tag{4.2}
\]

The disjoint-union symbol matters.  One direction `X->Y` may be generated
once by a lower mask and once by an upper mask.  It disappears only after both
labelled occurrences have been separated from their middle pieces.

As proved in `ORDERED_OSCD.md`, each of `F_-` and `F_+` has indegree and
outdegree at most one, and

\[
 |E(F_-)|=|E(F_+)|=W-\operatorname{Cat}_m. \tag{4.3}
\]

A cut immediately below or above the middle member separates exactly one
adjacent mask from its middle piece.  Cuts at all other ranks do not alter
`P_mid`.

### Theorem 5 (central feedback lower bound)

Let

\[
 \operatorname{wfas}(P_{\rm mid})
\]

be the minimum number of labelled arc occurrences whose deletion makes the
underlying digraph of `P_mid` acyclic.  Equivalently, give every directed pair
weight equal to its multiplicity in (4.2), and take a minimum-weight feedback
arc set.  Any
chain-splitting surgery that makes the adjacent-middle ranks orderable uses at
least

\[
 \operatorname{wfas}(P_{\rm mid}) \tag{4.4}
\]

central cuts across the two decompositions.  Hence a `d`-per-side surgery
requires

\[
 \boxed{\operatorname{wfas}(P_{\rm mid})\le 2d.} \tag{4.5}
\]

Conversely, if a feedback occurrence set `Q` can be assigned, occurrence by
occurrence, to one of its two endpoint-chain central gaps so that at most `d`
assigned cuts lie in each decomposition, then those cuts make the remaining
adjacent-middle precedence graph acyclic.

#### Proof

After surgery, let `Q` be the labelled adjacent-rank incidences that no longer lie in a
piece containing their original middle member.  Every member of `Q` requires
at least one cut at one of its two central gaps, and one central gap is
incident with only one such adjacent mask.  Therefore

\[
 |Q|\le\hbox{number of central cuts}.
\]

If the underlying digraph supported by `P_mid-Q` contained a directed cycle,
at least one labelled occurrence of every comparison on that cycle would
remain attached to its middle piece, so the cycle would survive.  Thus `Q` is
a feedback occurrence set, proving (4.4) and (4.5).

For the converse, cut one chosen endpoint gap for every labelled occurrence
in `Q`.  That occurrence leaves the middle-piece incidence graph, and the
underlying graph supported by the remaining occurrences is acyclic.  QED.

The standard Greene--Kleitman/complement pair has the explicit directed
`2m`-cycle proved in `ORDERED_OSCD.md`, so it has positive central feedback
cost for every `m>=2`.  The theorem deliberately makes no unsupported claim
about the exact size of that feedback cost.

### Why abstract orthogonality is insufficient

The local axioms alone permit arbitrarily large feedback cost.  For each
`j`, take four formal middle vertices `a_j,b_j,c_j,d_j` and put

\[
 F_+^{(j)}=\{a_j\to b_j,\ c_j\to d_j\},
\]

\[
 F_-^{(j)}=\{c_j\to b_j,\ a_j\to d_j\}.
\]

Then

\[
 (F_-^{(j)})^{\rm rev}\cup F_+^{(j)}
\]

is the directed four-cycle

\[
 a_j\to b_j\to c_j\to d_j\to a_j.
\]

The disjoint union of `q` gadgets obeys all partial-permutation degree
conditions but has weighted feedback arc number `q`.  This formal gadget is not claimed
to extend to a Boolean SCD pair.  It proves a precise logical point: a bounded
splitting theorem must exploit additional Boolean/SCD structure, not merely
orthogonality and the correct layer counts.

## 5. The arithmetic boundary cost

Even after all precedence cycles are broken, pure middle-matched chains may
have too few lower cells.  In the fixed-central geometry with middle intervals

\[
 [i,i+d],\qquad 1\le i\le W,
\]

the pure `W`-chain lower band has

\[
 dW-\binom{d+1}{2} \tag{5.1}
\]

cells.  All physical intervals of lengths at most `d` in `W+d` positions
number

\[
 dW+\binom{d+1}{2}. \tag{5.2}
\]

The two boundary triangles therefore contain exactly

\[
 d(d+1) \tag{5.3}
\]

cells.  If

\[
 L=\sum_{s=1}^{m-1}\binom{2m}{s},\qquad
 \sigma=dW+\binom{d+1}{2}-L,
\]

then at least

\[
 \max\{0,d(d+1)-\sigma\} \tag{5.4}
\]

lower masks must use a boundary endpoint piece.

This proves that some slack pieces must be nonempty when (5.4) is positive.
It does **not** say that one distinct cut is needed for every such mask: one
split chain piece may contain several boundary masks.  Cycle-transversal
bounds and cell-count bounds measure different resources and should not be
conflated.

## 6. Exact triangular scheduling after the cuts

Acyclic local precedence is still weaker than triangular support.  The latter
also has an exact criterion that is useful after a proposed surgery.

Let the refined incidence graph have `n` left pieces and `n` right pieces,
including any isolated empty padding pieces.  Let `P_L,P_R` be the two acyclic
local precedence digraphs.

Fix a linear extension `beta` of `P_R`, where `beta(R)` is the position of a
right piece.  Give every left piece the deadline

\[
 d_\beta(L)=\min\{\beta(R):L\cap R\ne\varnothing\}. \tag{6.1}
\]

An isolated left padding piece may be assigned deadline `n`.  Define its
effective deadline

\[
 \widehat d_\beta(L)=
 \min\{d_\beta(X):L\preceq_{P_L}X\}, \tag{6.2}
\]

where `X=L` is allowed.

### Theorem 6 (precedence-with-deadlines criterion)

For the fixed right order `beta`, there is a linear extension `alpha` of
`P_L` such that every occupied cell is triangular,

\[
 \alpha(L)\le\beta(R)\qquad(L\cap R\ne\varnothing), \tag{6.3}
\]

if and only if

\[
 \boxed{
 \left|\{L:\widehat d_\beta(L)\le q\}\right|\le q
 \quad\hbox{for every }1\le q\le n.} \tag{6.4}
\]

Consequently, an ordered triangular layout exists after the splits if and only
if `P_R` has some linear extension `beta` satisfying (6.4).

#### Proof

Condition (6.3) is equivalent to

\[
 \alpha(L)\le d_\beta(L)
\]

for every left piece.  If `widehat d_beta(L)<=q`, some descendant `X` of `L`
has deadline at most `q`.  Every feasible topological order places `L` before
`X`, hence within its first `q` positions.  This proves necessity of (6.4).

For sufficiency, order the left pieces by nondecreasing effective deadline,
breaking equal effective deadlines by a topological order of `P_L`.  If
`L precedes X` in `P_L`, the descendant set used in (6.2) for `L` contains
the descendant set for `X`, so

\[
 \widehat d_\beta(L)\le\widehat d_\beta(X).
\]

The resulting order is therefore a linear extension.  By (6.4), every piece
with effective deadline `q` occurs by position `q`; since
`widehat d_beta(L)<=d_beta(L)`, all original deadlines are met.  QED.

Without left precedence, (6.4) reduces to the transparent prefix-neighborhood
condition

\[
 |N(\{R:\beta(R)\le q\})|\le q \quad(1\le q\le n). \tag{6.5}
\]

Thus triangular support is a genuine global scheduling constraint, not a
consequence of cycle breaking.

## 7. What an all-`k` bounded-splitting theorem must prove

Since `d=B(k)-W(k)=\Theta(\sqrt{k})`, a successful surgery theorem must establish
far more than the existence of an orthogonal SCD pair.  For one explicit pair
it must provide:

1. a two-coloured transversal of **all** alternating cycle supports using at
   most `d` gaps from each family;
2. equivalently at the central three ranks, a feedback arc set satisfying
   (4.5) and the per-family assignment constraint;
3. linear extensions satisfying the deadline inequalities (6.4);
4. the lower directed-bandwidth bound `d` in the fixed-central part;
5. coordinatewise pin survival after the interval cells are assigned.

The exact positive target suggested by this note is therefore:

> **Bounded orthogonal splitting conjecture.**  There is a specifically
> chosen orthogonal SCD pair of the `k`-cube and at most `B(k)-W(k)` cuts in
> each family whose refined incidence graph passes the cycle-transversal,
> triangular-scheduling, band, and pin-survival conditions.

The standard/complement pair is not known to satisfy the required transversal
bound, and its explicit mixed central cycle shows that zero surgery is
impossible.  Before investing in an ordering or pinning argument for any seed
pair, the mathematically cheapest decisive test is now clear: prove a small
cycle-support transversal, or prove a support-disjoint cycle packing larger
than the available `2d` budget.
