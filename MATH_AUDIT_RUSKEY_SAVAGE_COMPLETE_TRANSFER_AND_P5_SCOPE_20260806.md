# Audit of the Ruskey--Savage complete-transfer path and P5 router scope

**Date:** 2026-08-06  
**Method:** direct comparison with the definitions and Theorem 1 of
Ruskey--Savage (1996), followed by a literal replay of the five-vertex
path decomposition; no computation or search  
**Verdict:** the two abstract graph theorems are correct.  Their proposed
application to the adjacent-necklace odd bulk was invalid because the
physical graph is a cyclic nearest-neighbour subgraph, followed by a
rotational quotient and a hub-colour constraint.  Both source files have
been corrected to abstract complete-transfer scope.

## 1. Ruskey--Savage theorem actually used

Ruskey and Savage encode a multiset combination as

\[
 x=(x_0,\ldots,x_t),\qquad
 0\le x_i\le n_i,qquad \sum_i x_i=k.
\]

They define `x,y` to be adjacent when there are arbitrary indices `p,q`
such that

\[
 x_p=y_p+1,
 \qquad x_q=y_q-1,
 \qquad x_i=y_i\quad(i\ne p,q).
\]

Their Theorem 1 states that for every nondecreasing capacity vector there
is an **extreme** Gray code.  “Extreme” is defined to start at the right
lexicographic extreme and end at the left lexicographic extreme.  For the
equal capacity vector `(2,...,2)`, the hypotheses apply and the adjacency
is exactly the complete-transfer graph

\[
 \{x\in\{0,1,2\}^n:\sum_i x_i=R\}
\]

with an arbitrary unit move `p to q`.  Therefore the Hamilton-path claim
in the first audited file is valid.  Reversal exposes the other extreme
endpoint, and coordinate permutations preserve the graph because all
capacities are equal.

Alternating edges of this path give a matching of size `floor(N/2)`.  The
central coefficient

\[
 [z^n](1+z+z^2)^n
 =\sum_j{n\choose2j}{2j\choose j}
\]

is odd because every `j>=1` summand is even.  Thus the abstract central
complete-transfer graph has a near-perfect matching with one extreme
socket.  These portions of the argument pass unchanged.

## 2. Fatal physical adjacency mismatch

The adjacent-necklace capacity-two theorem has a different edge set.  Its
coordinates are cyclic macro positions, and a legal horizontal move
transfers one unit only between adjacent positions:

\[
                         q=p+/-1\pmod n.
\]

Ruskey--Savage permit arbitrary `p,q`.  For example, at `n>=4`, the move

\[
 (1,1,0,0,\ldots)\longleftrightarrow
 (0,1,1,0,\ldots)
\]

is a Ruskey--Savage edge but is not a physical move when coordinates zero
and two are nonadjacent.  Hence the physical cyclic graph is only a
spanning subgraph of the graph covered by their theorem.  A Hamilton path
in the supergraph gives no Hamilton path or near-perfect matching in the
subgraph.

Two further constraints are also absent from the Gray theorem:

1. after fixing a background necklace, physical states are quotiented by
   its cyclic stabilizer, so a labelled Hamilton path need not project
   injectively and some projected edges may be loops;
2. selected physical horizontal edges are constrained by the partition
   matroid of unpointed hub colours, while an arbitrary Gray matching may
   repeat a hub colour.

Therefore the Gray path supplies none of the macroscopic same-shore wrap
current proved necessary by the rooted-path imbalance theorem.  The
dyadic/circulation blossom gate remains open.

## 3. P5 decomposition replay

Inside any genuine Hamilton path

\[
                         v_0,v_1,\ldots,v_{N-1},
\]

the block

\[
 v_{5f},v_{5f+1},v_{5f+2},v_{5f+3},v_{5f+4}
\]

does give the abstract two-port router

\[
 s_f=v_{5f+2},
 \quad p_f^0=v_{5f+1},\quad t_f^0=v_{5f},
 \quad p_f^1=v_{5f+3},\quad t_f^1=v_{5f+4}.
\]

After choosing one length-two branch, the other two vertices are matched
by their path edge.  The suffix beginning at `v_(5q)` is matched by
alternating edges and leaves at most its final vertex.  Thus the P5
decomposition is exact in the abstract complete-transfer graph.

It does **not** yet give a physical receiver router.  In addition to the
three graph-lifting rows above, one must identify every external gain claim
with a literal occurrence at `s_f`, verify both possible terminal types at
`t_f^0,t_f^1`, and export the residual extreme socket in the regenerative
state.  Until then, the phrases “gain route” and “sink” are abstract path
roles, not authenticated typed-cap occurrences.

## 4. Corrected scope

The two corrected files prove:

1. complete-transfer capacity-two layers are Hamilton-path traceable;
2. their central layers have one-socket near-perfect matchings; and
3. any such Hamilton path contains arbitrarily many disjoint abstract P5
   routers together with a matching of the unused vertices.

They do not prove:

1. the cyclic nearest-neighbour odd-sector matching;
2. rotational descent;
3. hub-rainbow selection;
4. a typed source/sink occurrence interface; or
5. removal of the odd circulation-blossom gate.
