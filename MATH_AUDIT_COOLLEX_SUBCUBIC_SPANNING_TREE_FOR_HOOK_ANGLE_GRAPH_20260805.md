# Audit of the cool-lex subcubic hook-angle tree

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_COOLLEX_SUBCUBIC_SPANNING_TREE_FOR_HOOK_ANGLE_GRAPH_20260805.md`  
**Method:** recursion-tree and binary/composition dictionary audit; no search

## 1. Dictionary

A zero-rooted binary word with `q` zeros has a unique vector of the `q`
one-run lengths following those zeros.  Changing the chosen zero rotates
that vector, so binary necklaces with `q` zeros and `b` ones are exactly
cyclic weak compositions of mass `b` in `q` slots.  The transfer
`x_j+1,x_(j+1) -> x_j,x_(j+1)+1` swaps the boundary `10` to `01` once.

## 2. Recursion edges

For `r=0^s1^t gamma`, the root of child call
`C(s-1,t-i,01^i gamma)` is

\[
 r_i=0^{s-1}1^{t-i}01^i\gamma.
\]

The root-to-first-child pair and every consecutive child-root pair differ
in exactly the displayed adjacent `01/10`.  The published necklace oracle
ensures both endpoints are distinct canonical representatives whenever the
child call exists, so no quotient loop is inserted into the tree.

## 3. Tree count and degree

The recursion call tree partitions outputs among the current root and the
disjoint child calls.  Replacing the ordinary star from the current root to
the child roots by the path through those roots still uses exactly one edge
per child and connects the same child subtrees.  Induction gives a tree.

A root has at most two neighbors in its parent's sibling path and only one
edge to the first root in its own child list.  Its degree is therefore at
most three.  This count includes periodic necklaces because the published
recursion outputs necklace classes, not all rotations.

## 4. Dependency and scope

The only imported theorem is exact coverage/nonduplication of the
Sawada--Williams first-10 recurrence for fixed-density necklaces.  No
claim about the size of a Gray-code transition is imported.

The constructed plane tree does not determine the order of marked PBBS
ports on promoted components.  In particular, the audit does not use the
currently unsettled orientation/time-order calculation in the standalone
two-chip contour theorem.

## 5. Verdict

**PASS** for existence of a canonical subcubic adjacent-transfer spanning
tree, conditional only on the cited published recursion theorem.  The
parent-port contour equation and physical halo packing remain open exactly
as stated.
