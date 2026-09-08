# Independent audit: MSW endpoint-augmented Hamiltonization equivalence

**Date:** 2026-08-05  
**Method:** line-by-line comparison with the primary Mütze--Nummenpalo--Walczak
paper *Sparse Kneser graphs are Hamiltonian*; no finite search or solver  
**Audited input:**
`MATH_THEOREM_MSW_ENDPOINT_AUGMENTED_HAMILTONIZATION_EQUIVALENCE_20260805.md`,
SHA-256
`790e0d8e253bb6fbb4ae0d69a62b7e71bb7aa550779bb570e4b0d5fe9721e444`

## Verdict

**GO, with one non-load-bearing wording correction.**

The main claims are supported by the primary construction:

1. the MNW cycle factor uses exactly the MSW paths closed by one selected
   complement edge per path;
2. every MNW flipping cycle is wholly contained in the bipartite graph
   `G_r`;
3. hence symmetric difference leaves every selected closure edge untouched
   and cannot introduce an unselected complement edge;
4. complementing the `2r` coordinates turns the resulting Hamilton cycle
   into a Hamilton cycle of the displayed endpoint-augmented containment
   graph `A_r`;
5. MNW Theorem 12 then gives the asserted middle-levels lift, and one global
   complement makes the `z`-free half literally the original MSW path
   family;
6. suppressing the intervening rank-`(r+1)` vertices gives exactly
   `F_z(H)=P_r`, and the edge-union colours partition the entire
   rank-`(r+1)` layer.

No correction to Theorems 3.3, 3.4, Corollary 4.1, or the `r=1,2` boundary
is required.

## 1. Primary graph definitions

MNW Section 2.2 defines

* `B_r^0` as the length-`2r`, weight-`r` bitstrings;
* `B_r^1` as the length-`2r`, weight-`(r+1)` bitstrings;
* `G_r` as their Hamming-distance-one incidence graph;
* `G_r^+` as `G_r` plus **all** edges `{x,bar(x)}` with
  `x in B_r^0`.

Thus `G_r^+` contains the full complement matching, whereas the graph used
in the audited theorem contains only the selected Catalan submatching

\[
 M_r=\{\{x,\bar x\}:x\in D_r\}.
\]

This distinction is handled correctly in the audited proof: it does not
infer the result merely from Hamiltonicity of `G_r^+`; it proves that the
particular MNW Hamilton cycle lies in the smaller graph `G_r+M_r`.

## 2. Factor and flipping-cycle support

MNW Section 2.3 defines, for every `x in D_r`, a path

\[
 P(x)=(x_0,\ldots,x_{2r})\subseteq G_r,
 \qquad x_0=x,\quad x_{2r}=\bar x,
\]

and Lemma 5 states that these paths are mutually vertex-disjoint and cover
all vertices of `G_r`.  The cycle factor is then

\[
 C_r=\{P(x)+\{x,\bar x\}:x\in D_r\}.
\]

MNW Section 3 defines a flipping cycle to be a cycle **in `G_r`** whose
path edges alternate with cross-path edges.  The Hamilton cycle is obtained
by symmetric difference of `C_r` with a conflict-free family of these
flipping cycles.

It follows literally that:

* no selected closure edge `{x,bar(x)}` is toggled;
* no unselected complement edge can be inserted;
* the resulting Hamilton cycle is a subgraph of `G_r+M_r`.

This verifies the load-bearing support claim in Theorem 3.4.

## 3. Complement to the augmented containment graph

Bitwise complement on the first `2r` coordinates sends

\[
 B_r^1\longleftrightarrow {\Omega\choose r-1},
 \qquad
 B_r^0\longleftrightarrow {\Omega\choose r},
\]

and sends Hamming-distance-one incidence to containment.  It preserves each
unordered closure edge `{x,bar(x)}` setwise.  Therefore

\[
 \overline{G_r+M_r}\cong
 \left({\Omega\choose r-1}\longleftrightarrow
       {\Omega\choose r}\right)+M_r=A_r.
\]

So the imported MNW Hamilton cycle proves Hamiltonicity of `A_r`, not only
of the full odd graph.

## 4. Exact Theorem 12 half tracking

MNW Theorem 12 defines its middle-levels model `M_r` as the disjoint union
of

\[
 G_r0\quad\text{and}\quad \overline{G_r}1
\]

plus vertical matching edges `{x0,x1}` for `x in B_r^0`.
For `r>=3`, it removes the retained closure edges from the MNW Hamilton
cycle, obtaining a path family `Q in G_r`, and uses

\[
 Q0\quad\text{and}\quad\overline{P_r}1
\]

with the two endpoint vertical edges for every `x in D_r`.

Consequently the `z=1` half is the fixed complemented MSW path family and
the `z=0` half is the rethreaded family.  Complementing all `2r+1`
coordinates is an automorphism of the middle-levels graph and sends

\[
 \overline{P(x)}1\longmapsto P(x)0.
\]

Hence the resulting `z`-free half is literally the original `P_r`, not
merely an isomorphic path factor or one having the same run spectrum.

## 5. Projection and upper-colour partition

Every `P(x)` starts and ends at weight `r` and has `2r` hypercube edges,
alternating through exactly `r` weight-`(r+1)` vertices.  Suppressing these
vertices gives an `r`-edge Johnson path from `x` to `bar(x)`.

By MNW Lemma 5 the paths partition **all vertices** of `G_r`.  In
particular, their intermediate vertices partition `B_r^1`.  Each such
intermediate vertex is the union of its two adjacent rank-`r` vertices.
Therefore the Johnson edge-union map is a bijection onto
`binom(Omega,r+1)`.  This proves both

\[
 F_z(H)=P_r
\]

and the asserted global disjointness/completeness of the upper colours.

## 6. Small ranks

* For `r=1`, `A_1` consists of one rank-zero vertex, two rank-one vertices,
  the two containment edges, and the selected endpoint edge: it is a
  triangle.
* For `r=2`, `G_2^+` is the Petersen graph.  The graph `G_2+M_2`, and hence
  `A_2`, is a spanning subgraph of it.  A Hamilton cycle in that subgraph
  would also be a Hamilton cycle in the Petersen graph, so none exists.

Thus the theorem's range `r>=3`, with the stated isolated `r=2` exception,
is exact.

## 7. Exact wording correction

Section 2 of the audited theorem currently says that the odd-graph closure
edge "in the middle-levels lift ... is the pair of vertical endpoint
edges."  This should not be read as a literal edge identity.  Under MNW
Theorem 12, one closure edge is **replaced by the entire chain**

\[
 x0\;--\;x1\;--\;\overline{P(x)}1\;--\;\bar x1\;--\;\bar x0,
\]

which contains two vertical endpoint edges and the full opposite-half
path.  The later contraction argument uses the correct chain, so this is
only a wording correction and does not affect any theorem.

## Final status

\[
 \boxed{\text{PASS / GO: the endpoint-augmented Hamiltonization and exact
 half-projection claims are supported by MNW.}}
\]

The audit closes only the protected MSW stem/upper-`q1` gate stated in the
input theorem.  It does not add claims about deeper upper shadows,
nonprotected coordinate residence, prescribed formal seams, or the later
common-cap compiler.
