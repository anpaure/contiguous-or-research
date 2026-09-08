# Exact depth-two collision reduction to disjoint bowties

Date: 2026-07-25

Method: deterministic incidence counting.

## 0. Outcome

For any exact wreath factor, every depth-two cyclic interval is the
intersection of two adjacent depth-one cyclic intervals.  Depth-two
collision pairs which reuse either depth-one parent are controlled exactly
by the depth-one pair moment.  Consequently, for the canonical MSW factor,
whose depth-one pair moment is now `O(W)`, the only unresolved depth-two
collisions are genuine four-parent bowties.

## 1. The extension graph at one depth-two target

Put `n=2m+1`.  Let `F` be any exact middle wreath factor, and let
`mu_1(T)` and `mu_2(S)` be its depth-one and depth-two cyclic-interval
loads.

A pointed depth-two occurrence of an `(m-2)`-set `S` in one cyclic order
has exactly two adjacent length-`m-1` extensions in that order.  Write them

\[
 T^-(e)=S\cup\{a\},\qquad T^+(e)=S\cup\{b\},
 \qquad a\ne b.
\tag{1.1}
\]

Thus the occurrence `e` may be regarded as an edge between two vertices
of the complete graph on the `m+3` rank-`m-1` supersets of `S`.

Every pointed depth-one occurrence belongs to exactly two pointed
depth-two occurrences in the same cyclic order, one on each side.  Hence,
if `d(T)` is the total number of incidences of all pointed depth-two
occurrences with the depth-one target `T`, then

\[
 \boxed{d(T)=2\mu_1(T).}
\tag{1.2}
\]

## 2. Reused-parent collisions

Let `P_2^{\rm meet}` count unordered pairs of distinct pointed depth-two
occurrences which have the same target `S` and whose two extension edges
share at least one depth-one parent.

### Theorem 2.1

For every exact wreath factor,

\[
 \boxed{
 P_2^{\rm meet}
 \le2\sum_T\binom{\mu_1(T)}2
 =2P_1.}
\tag{2.1}
\]

where

\[
 P_1=\sum_T\binom{\mu_1(T)}2.
\]

#### Proof

Charge a reused-parent collision pair to any common depth-one parent `T`.
The `mu_1(T)` pointed occurrences of `T` each have two adjacent
depth-two children, and those two child targets are distinct.  Two
colliding depth-two occurrences cannot use the same pointed occurrence of
`T`, since its left and right children are different.  For a fixed pair
of distinct pointed occurrences of `T`, their two two-element child
families have at most two common targets.  Hence at most two collision
pairs are charged to that occurrence pair.  This gives
`2 binom(mu_1(T),2)` for fixed `T`; summing proves (2.1).  A collision
which shares both parents may be charged twice, which is harmless.
\(\square\)

## 3. The exact remaining bowtie

Let `P_2^{\rm bow}` count collision pairs whose two extension edges are
vertex-disjoint.  Then tautologically

\[
 \boxed{P_2\le2P_1+P_2^{\rm bow}.}
\tag{3.1}
\]

For one bowtie there are four distinct coordinates outside `S`, say
`a,b,c,d`, and the two pointed middle owners are

\[
 X=S\cup\{a,b\},\qquad Y=S\cup\{c,d\}.
\tag{3.2}
\]

Their local cyclic deletion pairs are exactly `{a,b}` and `{c,d}`.
Equivalently, a bowtie is a pair of distance-two middle owners whose
intersection is `S`, with disjoint local deleted pairs equal to their two
respective differences.

For the canonical MSW factor, the clean-corridor renewal theorem gives
`P_1=O(W)`.  Therefore

\[
 \boxed{P_2=O(W)+P_2^{\rm bow}.}
\tag{3.3}
\]

This is a strict depth-two reduction: parallel extension pairs and all
wedges are already paid for.  A linear depth-two energy theorem now needs
only an `O(W)` count of genuine four-parent bowties in the canonical MSW
cyclic flag system.

The same incidence argument applies dually to the upper-core description,
but complementation of cyclic intervals already identifies the lower and
upper depth-two load ledgers in odd dimension.

## 4. The exact endpoint-fan hypergraph

There is a useful target-local description at every depth.  Fix an
`(m-q)`-set `R`.  If `R=I_pi(j,m-q)` in one row, write the `q` coordinates
immediately before it as `p_1,...,p_q` (ordered outwards) and those
immediately after it as `s_1,...,s_q`.  The `q+1` middle intervals of this
row which contain `R` have complements over `R`

\[
 Q_i=\{p_1,\ldots,p_i\}\cup
     \{s_1,\ldots,s_{q-i}\},
 \qquad0\le i\le q.                                             \tag{4.0}
\]

Call these `q+1` sets the **fan** of the occurrence.  Let
`G_R^(q)` be the `q`-uniform hypergraph on `[n] setminus R` obtained by
taking the union of all occurrence fans over `R`.

#### Lemma 4.1 (fan simplicity)

For every exact middle factor, `G_R^(q)` is simple and

\[
 \boxed{|E(G_R^{(q)})|=(q+1)\mu_q(R).}                          \tag{4.0a}
\]

#### Proof

The sets within one fan are distinct.  If the same `q`-set `Q` occurred
in fans from two different rows, then the middle set `R union Q` would be
a middle interval of both rows, contradicting exact middle ownership.
Thus all fan edges are distinct, and every occurrence contributes exactly
`q+1` of them. \(\square\)

At `q=2`, the full fan hypergraph `G_R^(2)` is an ordinary simple graph
with `3 mu_2(R)` edges.  Each occurrence also has one distinguished
**mixed** fan edge `{p_1,s_1}`.  Let `B_R` be the graph of these mixed
edges.  Then

\[
 |E(B_R)|=\mu_2(R),
 \qquad
 \boxed{
 B_R=\bigl\{\{a,b\}:\epsilon(R\cup\{a,b\})=\{a,b\}\bigr\},}   \tag{4.0b}
\]

where `epsilon(X)` is the endpoint pair of the middle interval `X` in
its unique owner row.  The parent edge attached to a depth-two occurrence
in Section 1 is exactly this mixed edge.  Hence a genuine bowtie is
exactly a pair of vertex-disjoint edges of `B_R`.

The other two fan edges remove two consecutive coordinates from the same
end; they belong to the full simplicity ledger (4.0a) but not to the
bowtie graph.  Thus the single endpoint map really does encode the new
depth-two collision species.  At general depth, the entire fan (4.0) is
the complement sequence along a length-`q` segment of the wreath's
Johnson cycle.

This fan formulation supplies simplicity for free, but it does not bound
the number of disjoint edge pairs.  That global count is exactly the
canonical renewal problem addressed by the centered path criteria.

## 5. General-depth parent-edge recurrence

Nothing in the parent charge used the special value two.  With our depth
convention, a pointed depth-`q` interval is the intersection of two
adjacent depth-`(q-1)` intervals.  Each pointed
depth-`(q-1)` occurrence has two distinct depth-`q` children.

Let `P_q^{bow}` count pairs of equal depth-`q` targets whose two unordered
parent pairs are vertex-disjoint.  Then for every `q>=2`,

\[
 \boxed{P_q\le2P_{q-1}+P_q^{bow}.}
\tag{5.1}
\]

The proof is verbatim Theorem 2.1, rank by rank.  Thus the entire
collision hierarchy separates into inherited parent collisions and new
four-parent bowties.  Iterating gives

\[
 P_q\le2^{q-1}P_1+
       \sum_{j=2}^{q}2^{q-j}P_j^{bow}.
\tag{5.2}
\]

Formula (5.2) is an exact ledger, not by itself a useful Gaussian-window
bound: the factor `2^(q-j)` must be removed by additional canonical
noncrossing/renewal structure.  It nevertheless identifies bowties as the
only genuinely new collision species at every depth.

There is a second reason not to iterate (5.2) as a raw pair bound.  The
centered energy consumed by prime-cycle smoothing is

\[
 \boxed{
 E_q=\|\mu_q-\lambda_q\mathbf1\|_2^2
    =2P_q-(\lambda_q-1)W.}                                     \tag{5.3}
\]

Once `lambda_q` grows, the subtracted term is the unavoidable collision
baseline and `P_q=O(W)` is false even for balanced loads.  A uniform
all-depth theorem must therefore control (5.3), or equivalently the
floor-corrected balanced pair excess, rather than `P_q` itself.  A bound
`E_q=O(q^aW)` feeds the nonuniform prime-cycle ledger only when `a<1`;
constant-factor loss per depth is fatal.

For the actual MWB endgame, the fixed-window diagonalization gives a
different valid target: for every fixed `A`, prove

\[
                         E_q\le C_AW
 \qquad(1\le q\le A\sqrt m),                                   \tag{5.4}
\]

with no uniformity in `A` required.  Since `lambda_q<=exp(A^2+o(1))` in
this window, the stronger raw estimate `P_q<=C'_AW` is at least
arithmetically compatible there.  It is not compatible with a single
absolute constant on a growing window such as
`q<=sqrt(m log log m)`, where `lambda_q` itself grows like `log m`.

The same warning appears in the direct Catalan renewal.  Treating the `q`
elementary pivot corridors as independent channels gives critical row sum
`q K(1/4)^2=q/4`, already one at `q=4`.  Uniformity therefore requires a
synchronized outer-shell theorem (for instance a single removable shell,
or a bundled `K^(2q)` transition), not a channel union bound.
