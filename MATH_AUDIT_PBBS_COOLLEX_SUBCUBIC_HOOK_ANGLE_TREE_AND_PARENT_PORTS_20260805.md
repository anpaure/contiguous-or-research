# Audit: cool-lex subcubic hook-angle tree and promoted ports

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_COOLLEX_SUBCUBIC_HOOK_ANGLE_TREE_AND_PARENT_PORTS_20260805.md`  
**Method:** symbolic reconstruction from the fixed-content necklace recursion; no
finite search  
**Verdict:** **PASS**, with the scope stated in the theorem.  In particular,
this audit does not promote contour compatibility or halo separation to proved
statements.

## 1. Necklace encoding

For a cyclic weak composition `x=(x_0,...,x_(q-1))` of `b`, the word

\[
0,1^{x_0}0,1^{x_1}\cdots0,1^{x_{q-1}}
\]

has exactly `q` zeros and `b` ones.  Rotation of the composition is rotation
of the word, and cutting after each zero recovers the composition.  Therefore
the map is a bijection on necklace classes.

Moving one chip between adjacent banks changes the separating local word from
`10` to `01`, or conversely.  Thus the adjacent-transfer graph is exactly the
cyclic adjacent-swap graph on these fixed-content necklaces.

## 2. Sibling edge identity

At a recursion node `w=0^s 1^t gamma`, set

\[
w_i=0^{s-1}1^{t-i}0,1^i\gamma,
\qquad w_t=w.
\]

For consecutive indices, put

\[
P=0^{s-1}1^{t-i},\qquad R=1^{i-1}\gamma.
\]

Then, literally,

\[
w_i=P01R,
\qquad
w_{i-1}=P10R.
\]

Hence every sibling-path edge is one allowed adjacent transfer.  This check
uses only the recursion roots, not the generally non-adjacent transitions of
the emitted cool-lex Gray order.

## 3. Tree and degree audit

Assume recursively that every child call has already produced a tree on its
own disjoint recursion class.  Contract those child trees.  The newly added
edges form the path

\[
w_t-w_{t-1}-\cdots-w_j.
\]

It joins the contracted child vertices and the parent exactly once and creates
no cycle.  Undoing the contractions proves connectedness and acyclicity.
Induction from the terminal calls proves that the graph spans every necklace
in the recursion class, and hence the initial call spans the full fixed-content
necklace set.

A vertex has at most two incident edges in the sibling path of its parent
call.  In its own call it is the first vertex `w_t`, so it gains at most one
edge to its first child root.  These are the only possible incidences.
Therefore

\[
\Delta(T)\le 3.
\]

## 4. Promoted-port audit

For a sibling edge

\[
P01R\longleftrightarrow P10R,
\]

deleting the moving `1` gives the common lower word `P0R`.  Promotion at that
rooted cut inserts two empty vacancy slots, giving

\[
P000R.
\]

The data consisting of the promoted word together with the marked inserted
pair reconstructs `P0R`, the cut, and therefore the two rooted children.
Consequently rooted tree edges have distinct **marked** promoted occurrences.
This does not assert that their unmarked parent necklace classes are distinct.

## 5. Scope audit

The proof establishes only:

1. a spanning adjacent-transfer tree;
2. maximum degree three on the child tree;
3. the rooted promoted-port rule `01/10 -> 000`;
4. injectivity after retaining the inserted-pair mark.

It does **not** establish that the directed order of the marked ports on an
assembled parent spine equals the plane-tree contour order.  It also does not
establish disjoint physical halos, compatibility with the named two-rail
block, coverage of non-hook sectors, or any post-q2 compiler gate.  The
orientation warning is essential: reflecting a rooted port exchanges the two
child shores as well as reversing the parent port.

## 6. Final verdict

The theorem is proof-safe exactly as scoped.  The remaining hook problem is no
longer child-side connectivity or degree; it is the simultaneous directed
contour/parent-port-order identity together with physical halo packing.
