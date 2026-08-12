# Independent audit of the cool-lex subcubic hook tree

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_COOLLEX_SUBCUBIC_SPANNING_TREE_FOR_HOOK_ANGLE_GRAPH_20260805.md`  
**Method:** direct recurrence, quotient-edge, tree-count, and degree audit;
no finite search

## 1. Imported statement and dictionary

The only external input needed is the Sawada--Williams fixed-density
necklace recursion: the valid calls of `C(s,t,gamma)` partition the
necklace classes and output every class exactly once.  Nothing about the
size of successive transitions in their Gray listing is used.

The binary/composition dictionary is exact.  Rooting at a zero records the
lengths of the following one-runs, and changing the root rotates that weak
composition.  Moving one chip between adjacent slots changes exactly one
boundary `10` to `01` (or conversely), so it is an edge of the hook-angle
graph.

## 2. Sibling-root edges

For a call root

\[
 r=0^s1^t\gamma,
\]

the stated child roots are

\[
 r_i=0^{s-1}1^{t-i}0,1^i\gamma.
\]

The pair `r,r_(t-1)` differs at the displayed `01/10`.  Directly from the
root formula, each consecutive pair is

\[
\begin{aligned}
r_i&=0^{s-1}1^{t-i}\,01\,1^{i-1}\gamma,\\
r_{i-1}&=0^{s-1}1^{t-i}\,10\,1^{i-1}\gamma,
\end{aligned}
\]

and hence also differs at one displayed adjacent `01/10`.  Thus the
sibling-root path uses strict adjacent-swap edges, even though this need
not be true of arbitrary consecutive outputs in the published Gray order.

Because valid recursive calls output distinct necklace classes, none of
these edges becomes a loop after quotienting by rotation.

## 3. Tree induction and degree

Let the valid child calls have disjoint output sets `V_i`.  Inductively
their internal trees contribute

\[
 \sum_i(|V_i|-1)
\]

edges.  The sibling-root path contributes one edge per child, hence the
union has

\[
 \sum_i(|V_i|-1)+\#\{i\}=\sum_i|V_i|
\]

edges on `1+sum_i |V_i|` vertices.  It is connected, hence a tree.

A recursive-call root receives at most two edges from the sibling path in
its parent call and at most one edge from its own root to its first child.
No other recursive path contains it.  Therefore the maximum degree is at
most three.  The recursive child order supplies a canonical plane order.

The audited theorem originally had two display errors: an extraneous
leading `1` in the edge-count equation, and the indices `i+1` mislabeled as
`i-1` in its first version of the consecutive-root display.  Both have
been corrected in the theorem file.  Direct substitution in the root
formula proves the corrected display above, so neither error changes the
construction or the conclusion.

## 4. Scope boundary

The proof establishes only the child-side adjacent-transfer tree and its
bounded degree.  It does not identify the plane-tree contour order with
the cyclic order of marked `00` ports on promoted PBBS parents.  It also
does not prove simultaneous q2-halo separation.  Those are independent
physical/order gates and remain open.

## 5. Verdict

**PASS after the one displayed edge-count typo was corrected.**

The unconditional mathematical conclusion is:

> Every hook-angle graph has a canonical plane spanning tree of maximum
> degree at most three whose edges are legal adjacent chip transfers.

No claim about the promoted-port contour product, global packing, or
`nu(k)<=B(k)+O(1)` follows from this theorem alone.
