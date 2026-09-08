# BTK symmetric chains give an exact two-colour Catalan forest

**Date:** 2026-08-13  
**Status:** unconditional all-parameter theorem; degree-two pathization is
the remaining local gate

## 1. The two turn rows

Fix `r>=2`, put `n=2r-1`, and write

\[
 \mathcal L={ [n]\choose r-1},\qquad
 \mathcal M={ [n]\choose r},\qquad
 \mathcal U={ [n]\choose r+1}.                       \tag{1.1}
\]

Then

\[
 |\mathcal L|=|\mathcal M|=:W={2r-1\choose r},
 \qquad
 |\mathcal U|=:U={2r-1\choose r+1},                 \tag{1.2}
\]

and

\[
 W-U={2W\over r+1}=\operatorname {Cat}_r.           \tag{1.3}
\]

For a Johnson edge `AB` on `mathcal M`, call

\[
 \ell(AB)=A\cap B\in\mathcal L,
 \qquad
 u(AB)=A\cup B\in\mathcal U                         \tag{1.4}
\]

its lower and upper colours.

The aim of this note is to choose exactly `U` Johnson edges, one of every
upper colour and with pairwise distinct lower colours, while keeping them
acyclic.

## 2. Greene--Kleitman chains

Use the standard Greene--Kleitman/BTK symmetric chain decomposition of
`B_n`.  In its parenthesis description, scan a binary membership word from
left to right and match every `1` with the rightmost earlier unmatched `0`.
The matched positions are fixed within one chain.  The unmatched positions
consist of some `1`s followed by some `0`s, and moving upward in the chain
flips the unmatched zeros from left to right.

For a chain `C`, let

\[
 p(C)=\text{the rank of its bottom element}.          \tag{2.1}
\]

Equivalently, `p(C)` is the number of matched `01` pairs.  The chain runs
from rank `p(C)` through rank `n-p(C)`.

Every chain containing a rank-`r+1` element has

\[
 p(C)\le r-2                                             \tag{2.2}
\]

and contains unique consecutive elements

\[
 L_C\subset A_C\subset U_C,
 \qquad
 (|L_C|,|A_C|,|U_C|)=(r-1,r,r+1).                    \tag{2.3}
\]

There are unique coordinates `x_C,y_C` such that

\[
 A_C=L_C\cup\{x_C\},qquad
 U_C=L_C\cup\{x_C,y_C\}.                            \tag{2.4}
\]

Define the other rank-`r` intermediate set

\[
 B_C=L_C\cup\{y_C\}.                                \tag{2.5}
\]

Thus `A_CB_C` is a Johnson edge with

\[
 \ell(A_CB_C)=L_C,qquad u(A_CB_C)=U_C.              \tag{2.6}
\]

## 3. The exact forest theorem

### Theorem 3.1 (BTK two-colour Catalan forest)

Let

\[
 F_{\rm BTK}=\{A_CB_C:C\text{ contains rank }r+1\}. \tag{3.1}
\]

Then all of the following hold.

1. The upper-colour map is a bijection

   \[
   u:E(F_{\rm BTK})\longrightarrow\mathcal U.        \tag{3.2}
   \]

2. The lower-colour map is injective:

   \[
   |\{\ell(e):e\in E(F_{\rm BTK})\}|=U.             \tag{3.3}
   \]

3. `F_BTK` is a forest on the full vertex set `mathcal M`.
4. It has exactly

   \[
   c(F_{\rm BTK})=W-U=\operatorname {Cat}_r          \tag{3.4}
   \]

   components, counting isolated rank-`r` owners.

#### Proof

Every member of `mathcal U` lies in a unique symmetric chain, and that
chain necessarily satisfies (2.2).  Hence the sets `U_C` in (2.3)
enumerate `mathcal U` exactly.  Formula (2.6) proves (3.2).

The corresponding `L_C` lie in those same distinct chains.  A symmetric
chain contains only one element at rank `r-1`, so the `L_C` are pairwise
distinct.  This proves (3.3).

It remains to prove acyclicity.  Orient every selected edge as

\[
 A_C\longrightarrow B_C.                            \tag{3.5}
\]

Let `p=p(C)`.  At state `L_C`, the coordinates `x_C,y_C` in (2.4) are the
first two unmatched zeros in the Greene--Kleitman bracketing.  Passing to
`B_C` flips `y_C` while leaving `x_C` zero.  The two consecutive unmatched
positions `x_C<y_C` therefore become one new matched `01` pair; all old
pairs remain unchanged.  Consequently, if `C(B_C)` denotes the unique
symmetric chain containing `B_C`, then

\[
 p(C(B_C))=p(C)+1.                                   \tag{3.6}
\]

Thus the chain-bottom potential strictly increases along every directed
edge.

Moreover, a rank-`r` owner `A` can occur as the tail `A_C` only for its
own unique symmetric chain.  Hence every vertex has outdegree at most one
in (3.5).  If the underlying undirected graph contained a cycle, its cycle
edges would have total outdegree equal to the number of cycle vertices.
Since each vertex contributes at most one, every cycle vertex would have
exactly one outgoing cycle edge, producing a directed cycle.  This
contradicts the strict potential increase (3.6).  Hence `F_BTK` is a
forest.

Finally, it has `W` vertices and, by (3.2), `U` edges.  Euler's identity
for a forest gives (3.4). `square`

## 4. Exact finite structure

The construction is fully explicit.  Direct generation of the recursive
BTK chains verifies Theorem 3.1 for `2<=r<=9` and gives the following
useful census.

\[
\begin{array}{c|c|c|c|c}
r&U&\text{used owners}&\text{isolates}&
  \text{nonisolated components}\\ \hline
2&1&2&1&1\\
3&5&8&2&3\\
4&21&30&5&9\\
5&84&112&14&28\\
6&330&420&42&90\\
7&1287&1584&132&297\\
8&5005&6006&429&1001\\
9&19448&22880&1430&3432
\end{array}                                                        \tag{4.1}
\]

The isolate count is `Cat_(r-1)`.  The nonisolated component count is the
Catalan-triangle difference

\[
 {2r-2\choose r-2}-{2r-2\choose r-3},               \tag{4.2}
\]

and their sum is `Cat_r`, as required by (3.4).  These refined identities
follow directly by sorting the SCD chains by bottom rank; they are not
needed for Theorem 3.1.

The selected forest is generally not linear.  Its maximum degree in the
same census is `r-1`, already attained twice.  Thus Theorem 3.1 solves
simultaneously:

* every upper target exactly once;
* injective lower colours;
* the exact Catalan component count; and
* acyclicity;

but not the owner-degree-two condition required for a Johnson path cover.

## 5. The pathization gate

Before addressing degree reduction, the BTK forest has an exact Catalan
root structure.

### Theorem 5.1 (one short-chain sink per component)

Orient `F_BTK` as in (3.5).  Every connected component contains exactly
one rank-`r` owner belonging to a short symmetric chain whose bottom rank
is `r-1`.  These owners are precisely the sinks of the orientation.
Moreover, the rank-`r-1` bottom of that short chain is not used as a lower
colour in (3.3), and this gives a bijection

\[
 \{\text{components of }F_{\rm BTK}\}
 \longleftrightarrow
 \{\text{short central chains}\}
 \longleftrightarrow
 \mathcal L\setminus\ell(E(F_{\rm BTK})).           \tag{5.1}
\]

#### Proof

Every long chain with bottom rank at most `r-2` contributes exactly the
one edge whose tail is its rank-`r` member.  Hence its middle owner has
outdegree one.  A short chain with bottom rank `r-1` has no rank-`r+1`
member and contributes no edge, so its middle owner has outdegree zero.

By (3.6), every oriented edge raises the chain-bottom potential by one.
Starting from any vertex and following its unique outgoing edges therefore
terminates at a short-chain owner.  In one undirected tree component two
different sinks would force, on the unique path between them, a vertex
with two outgoing path edges; this is impossible because outdegree is at
most one.  Thus the sink is unique.

The used lower colours in (3.3) are exactly the rank-`r-1` members of the
long chains.  Their complement consists exactly of the bottom members of
the short chains.  This proves the three-way bijection. `square`

For an unused lower colour `L`, all its `r+1` rank-`r` parents lie in
BTK forest components.  Direct computation through `r=9` gives the
stronger pattern that these parents lie in pairwise distinct components.
After deleting the parent in the sink component itself, this defines a
loopless directed graph on the `Cat_r` components with outdegree exactly
`r`.  Its underlying and directed graphs are connected in all tested
cases.

The all-`r` distinct-component and strong-connectivity statements are not
proved here.  Their exact target is:

> identify the sink reached from `L+x` directly in the Dyck/ballot word of
> `L`, and show that the resulting moves generate the Catalan state space.

This contracted unused-colour graph is the natural endpoint-completion
quotient.  It is not regular in indegree and therefore is not literally the
undirected associahedron rotation graph.

The remaining local degree problem is now precise.

### Conjecture 5.2 (BTK pathization)

There is a reassignment

\[
 U\longmapsto L(U)\subset U,qquad
 |U\setminus L(U)|=2,                               \tag{5.2}
\]

such that

1. the `L(U)` are pairwise distinct; and
2. the Johnson edges joining the two rank-`r` intermediates between
   `L(U)` and `U` form a linear forest.

Any such forest has `W` vertices, `U` edges, and therefore exactly
`Cat_r` components.  Lifting each edge through its lower colour gives an
alternating path cover with both turn rows exact on the retained edges.
The `Cat_r` omitted lower colours are then exactly the number of endpoint
bridges needed to complete a Middle Levels Hamilton cycle.

The conjecture has exact SAT witnesses for

\[
 r=4,5,6,7.                                         \tag{5.3}
\]

The encoding has one variable for every pair `L subset U` at distance two,
requires one variable per `U`, at most one per `L`, and owner degree at
most two.  Cycle clauses are then added lazily.  In all four cases, the
first degree-feasible solution has only a small family of cycles, and one
round of cycle clauses produces a forest:

\[
\begin{array}{c|c|c|c}
r&\text{selected edges}&\text{forest components}&
  \text{cycle-cut rounds}\\ \hline
4&21&14&1\\
5&84&42&1\\
6&330&132&1\\
7&1287&429&1.
\end{array}                                                        \tag{5.4}
\]

These finite certificates refute small determinant, parity, and local
capacity obstructions.  They do not constitute an all-`r` proof.

## 6. Consequence for the second-shadow program

Before Theorem 3.1, it was possible that simultaneous lower/upper colour
selection itself had an integral lattice obstruction.  That possibility is
now eliminated for every `r` by an explicit positive construction.

The remaining hierarchy is

\[
 \boxed{
 \text{BTK exact two-colour forest}
 \longrightarrow
 \text{degree-two pathization}
 \longrightarrow
 \text{Catalan endpoint completion}
 \longrightarrow
 \text{double-turn chronology}.}                    \tag{6.1}
\]

The first arrow is the only unresolved incidence-level step.  All later
steps must preserve both named turn rows in the same owner state.
