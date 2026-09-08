# Central-trace trades for centered squares

Date: 2026-09-07. This note gives exact local identities for centered-square
traces in the Boolean lattice on `[2b]`; it does not prove the full-cube
coefficient-one conjecture.

## 1. Trace and edge-colour identities

Let `J=J(2b,b)` be the Johnson graph. An oriented geodesic

\[
 P=(T_0,T_1,\ldots,T_{\ell-1})
\]

with `ell<=b` determines a unique centered square pair. Indeed, along a
geodesic every step deletes a new coordinate and inserts a new coordinate.
The common intersection and the complement of the common union have size
`b-ell+1`, and the two ordered lists of deleted and inserted coordinates
give the two chain axes. Conversely, the middle trace of a centered square
pair is

\[
 \operatorname{Tr}(P)=
 \{T_0,\ldots,T_{\ell-1},T_0^c,\ldots,T_{\ell-1}^c\}.
\]

Multiplicity is retained in this notation. Its principal charge is
`2ell`.

For a Johnson edge `UV`, define its two lower colours by

\[
 \phi_-(UV)=\{U\cap V,(U\cup V)^c\}.                 \tag{1}
\]

The two upper colours are their complements. The rank-`b-1` occurrence
multiset of the square pair determined by `P` is exactly

\[
 \biguplus_{i=0}^{\ell-2}\phi_-(T_iT_{i+1}),         \tag{2}
\]

and its rank-`b+1` occurrence multiset is the complement of (2). Hence a
collection of square pairs with total principal charge `M` and `t`
components has exactly

\[
                         M-2t                         \tag{3}
\]

lower-rank occurrences and the same number of upper-rank occurrences.

In particular, if the edge multiset of the trace paths is unchanged, then
the adjacent-rank coverage is unchanged. Tail switches or context switches
that merely reassemble the same Johnson edges cannot repair an adjacent
hole.

## 2. Contiguous traces are diagonal subsquares

Write the square determined by a geodesic of `ell` middle vertices in the
following coordinates. There are ordered lists

\[
 X=(x_1,\ldots,x_{\ell-1}),\qquad
 Y=(y_1,\ldots,y_{\ell-1})
\]

and a fixed set `F` of size `b-ell+1` such that the geodesic is

\[
 S_i=F\cup X_{\{i+1,\ldots,\ell-1\}}\cup Y_{[i]},
 \qquad 0\le i<\ell.                                \tag{D1}
\]

One orientation of its square is

\[
 \mathcal R(P)=
 \{F\cup X_{\{i+1,\ldots,\ell-1\}}\cup Y_{[j]}:
                       0\le i,j<\ell\}.             \tag{D2}
\]

**Diagonal-block lemma.** For `0<=a<=c<ell`, the square determined by the
contiguous subgeodesic `(S_a,...,S_c)` is exactly the index block

\[
 \{F\cup X_{\{i+1,\ldots,\ell-1\}}\cup Y_{[j]}:
                       a\le i,j\le c\}              \tag{D3}
\]

of (D2), together with its complement block.

Proof. The subgeodesic has fixed set

\[
 F_{a,c}=F\cup X_{\{c+1,\ldots,\ell-1\}}\cup Y_{[a]}.
\]

At step `i -> i+1` it deletes `x_(i+1)` and inserts `y_(i+1)`. Hence its
square consists of

\[
 F_{a,c}\cup X_{\{i+1,\ldots,c\}}
              \cup Y_{\{a+1,\ldots,j\}},
 \qquad a\le i,j\le c.
\]

Substituting the definition of `F_(a,c)` gives (D3) term by term.
`square`

Thus the full square of every contiguous subpath is contained in the full
square of the ambient path. This is an all-rank statement.

There is also an intrinsic description, independent of the coordinate
lists. For `i<=j`, the target at index `(j,i)` in (D2) is `S_i intersect
S_j`, and that at `(i,j)` is `S_i union S_j`. Therefore

\[
 \mathcal R(P)=\{S_i\cap S_j,S_i\cup S_j:0\le i,j<\ell\}.  \tag{D4}
\]

This explains the all-rank containment directly: taking unions and
intersections of a subpath's vertices cannot leave the ambient pair hull.

## 3. A monotone zero-charge merge at every rank

**Merge lemma.** Let

\[
 P=(T_0,\ldots,T_{p-1}),\qquad
 Q=(U_0,\ldots,U_{q-1})
\]

be oriented middle traces of two centered square pairs. Suppose

\[
 T_{p-1}\sim U_0,\qquad
 d_J(T_0,U_{q-1})=p+q-1,\qquad p+q\le b.             \tag{4}
\]

Then their concatenation

\[
 P*Q=(T_0,\ldots,T_{p-1},U_0,\ldots,U_{q-1})
\]

is a geodesic and determines one centered square pair of side `p+q`.
Replacing the two old square pairs by this one:

1. preserves the complete middle-trace multiset;
2. contains both old square pairs and therefore preserves every old target
   at every rank;
3. adds, in the adjacent ranks, precisely the two lower occurrences

\[
 T_{p-1}\cap U_0,\qquad (T_{p-1}\cup U_0)^c,         \tag{5}
\]

   and their two upper complements;
4. leaves the principal charge unchanged:
   `2p+2q=2(p+q)`.

Proof. Condition (4) says that a path of `p+q-1` Johnson edges has endpoint
distance `p+q-1`, so the concatenation is geodesic. Its vertex list,
together with its complementary list, is exactly the concatenation of the
two old trace lists (as a multiset).
The diagonal-block lemma, with blocks `[0,p-1]^2` and
`[p,p+q-1]^2`, embeds both old square pairs in the new one. Formula (2)
shows that only the joining edge and its complementary edge are added in
the adjacent ranks. The charge identity is immediate. `square`

Thus if either target in (5) is currently a lower-rank hole, the merge
strictly decreases the lower deficit without creating a new deficit and at
zero principal cost. The analogous statement holds in the upper rank. The
smallest instance merges two side-one square pairs based at adjacent
antipodal vertex pairs into one side-two pair.

For independently compiled band blocks, this merge also removes one
component-overhead payment and loses no designated band target.
It does not assert preservation of unintended cross-block witnesses in an
arbitrary pre-existing word. The preserved certificate is the full family
of targets belonging to the old squares, which can then be recompiled.

### Exact gain at every rank

Use `d` for rank offset, to distinguish it from the second path length.
A side-`m` square pair has exactly

\[
                         2(m-|d|)_+                  \tag{G1}
\]

targets of rank `b+d`. Because `p+q<=b`, the fixed cap of the merged
square is nonempty. Consequently its orientation and complement families
are disjoint, and the index map in (D2) is injective. The two old diagonal
blocks are disjoint as well. Hence the number of genuinely new rank-`b+d`
targets is exactly

\[
 \boxed{2\left[(p+q-|d|)_+-(p-|d|)_+-(q-|d|)_+\right].}       \tag{G2}
\]

If `p<=q` and `r=|d|`, half of (G2) is

\[
 \begin{cases}
 r,&0\le r<p,\\
 p,&p\le r<q,\\
 p+q-r,&q\le r<p+q,\\
 0,&r\ge p+q.
 \end{cases}                                         \tag{G3}
\]

There is no new middle target, there are exactly two new targets in each
adjacent rank, and the total gain over all ranks is `4pq`, the size of the
two off-diagonal rectangles and their complements.

These gains are relative to the two replaced squares. Some added targets
may already have witnesses in other squares of a larger cover; global
distinct coverage is nondecreasing but its strict gain can be smaller.

### Overlapping coalescence also saves principal charge

Suppose instead that the two oriented paths have an identical terminal/
initial overlap of `r>=1` vertices, and that their union in this order is a
geodesic of side `ell=p+q-r<=b`. In its coordinates the old paths occupy
index intervals `[0,p-1]` and `[p-r,ell-1]`. Their squares are the two
diagonal blocks on these intervals, whose intersection is the diagonal
`r`-square. Coalescing them preserves every old target and saves exactly
`2r` units of principal charge. At rank `b+d` the new target count is

\[
 2\big[(p+q-r-|d|)_+-(p-|d|)_+-(q-|d|)_+
                              +(r-|d|)_+\big].       \tag{G4}
\]

Summing over ranks gives `4(p-r)(q-r)` additional targets. The case of one
path contained in the other gives zero new targets and simply deletes a
redundant square. For independently compiled `H`-band blocks, assuming
`H<min(p,q)`, coalescence saves exactly `2r+2H` letters in the length
ledger, with no designated target loss.

This is a sufficient local simplification rule, not an existence theorem
for an efficient global sequence of coalescences. Branching paths that
merely share a middle target need not lie in one geodesic, and do not
satisfy this lemma.

The exact global capacity condition following from (3) is

\[
 M-2t\ge \binom{2b}{b-1}.                            \tag{6}
\]

If `M=(1+epsilon)W`, where `W=binom(2b,b)`, then any three-rank cover by
square pairs must have

\[
 t\le {W\over2}\left(\epsilon+{1\over b+1}\right). \tag{7}
\]

Every successful merge is optimal for this occurrence ledger: decreasing
`t` by one creates exactly the two new lower occurrence slots predicted by
(3).

## 4. Minimal fixed-component trades

If `b>=3` and the number of components is required to remain fixed, the
absolute smallest nontrivial trade uses three antipodal middle-vertex
pairs. Take a middle set `A` with Johnson neighbours `B,C` belonging to
distinct antipodal pairs. Replace the two
square pairs

\[
              (A,B)\quad\hbox{and}\quad(C)
\]

by

\[
              (A,C)\quad\hbox{and}\quad(B).          \tag{8}
\]

Here a one-vertex path denotes a side-one square pair. Both sides have the
same central multiset, two components, and charge six. The trade replaces
the two lower colours `phi_-(AB)` by `phi_-(AC)`, and similarly in the upper
rank. Two antipodal vertex pairs cannot support a nontrivial trade with a
fixed component count, so this three-vertex pivot is minimal.

If every component in the trade is required to have side at least two, the
smallest trade has four antipodal vertex pairs and two side-two squares on
each side. A particularly useful instance is an alternating four-cycle.

Let `S` have size `b-2`; choose distinct `a,b',c,d` outside `S`, and put

\[
\begin{aligned}
 A&=S\cup\{a,c\},& B&=S\cup\{b',c\},\\
 C&=S\cup\{a,d\},& D&=S\cup\{b',d\}.
\end{aligned}                                        \tag{9}
\]

Replace the side-two square pairs based on Johnson edges `AB,CD` by those
based on `AC,BD`. Both sides have middle trace multiset

\[
 \{A,B,C,D,A^c,B^c,C^c,D^c\}
\]

and charge eight. The old intersection/union colours are

\[
\begin{array}{c|c}
 \text{intersections}&S+c,\ S+d\\
 \text{unions}&S+a+b'+c,\ S+a+b'+d,
\end{array}
\]

whereas the new ones are

\[
\begin{array}{c|c}
 \text{intersections}&S+a,\ S+b'\\
 \text{unions}&S+a+c+d,\ S+b'+c+d.
\end{array}                                          \tag{10}
\]

Together with the complementary colours from (1), this replaces four
lower occurrences by four different lower occurrences, and likewise in
the upper rank. Therefore it repairs adjacent holes at zero charge whenever
every removed colour has another occurrence in the ambient cover and at
least one inserted colour is a hole.

More abstractly, collections of side-two squares are matchings only when
their central traces are disjoint. In that restricted case two
decompositions of the same central multiset are two perfect matchings on
the same folded Johnson vertices; their symmetric difference is a disjoint
union of alternating even cycles, and a four-cycle is the smallest trade.
Without the side-two/no-singleton restriction, preserving the central
multiset preserves the path vertices, not their edge degrees. The
three-vertex pivot (8) shows why arbitrary trades must not be described as
cycle-space relations.

## 5. Exact obstruction to purely local rewiring

For any central-preserving recomposition, adjacent support changes only
through changed Johnson edges by (1). In particular:

* an edge-preserving switch has exactly zero adjacent effect;
* a same-component-count trade has the same number of adjacent occurrences
  before and after, so it can increase distinct coverage only by consuming
  redundant old occurrences;
* the merge lemma is the only elementary move above that increases the
  adjacent occurrence budget: it changes the number of path components.

Thus a search over context switches should track edge colours and component
count, not merely new path decompositions. A switch that changes neither is
provably irrelevant to adjacent-rank repair.

Finite literal checks of (D3), (D4), (G2), and (G4) are in
`scripts/check_all_rank_square_merges_20260907.py`; the arguments above,
not those checks, prove the claims in all dimensions.
