# Self-audit: middle-levels half projection and balanced-collar depuncturing

**Date:** 2026-08-05  
**Method:** independent symbolic proof audit; no computation or search  
**Audited theorem:**
`MATH_THEOREM_MIDDLE_LEVELS_HALF_PROJECTION_AND_BALANCED_COLLAR_DEPUNCTURING_20260805.md`

## 1. Parameter audit

For `k=2r`,

\[
 W={2r\choose r},\qquad
 U={2r\choose r+1}={r\over r+1}W,
 \qquad C=W-U={W\over r+1}=\operatorname {Cat}_r.
\]

Hence a spanning `C`-component forest on the `W` owners has exactly `U`
edges.  A balanced bank of `b=C-1` collars with `s=h+1` bridge owners per
collar deletes `bs` owners and `bs` nonrepeated stem colours, leaving

\[
 |V_0|=W-bs,qquad |\mathcal U_0|=U-bs=|V_0|-C.
\]

The counts in the theorem are consistent.

## 2. Middle-levels sector audit

On `Omega dot union {z}`, the rank-`r/r+1` sectors are

\[
 A={\Omega\choose r},\quad
 B=z+{\Omega\choose r-1},\quad
 C_+={\Omega\choose r+1},\quad
 D=z+{\Omega\choose r}.
\]

Containment allows exactly `A-C_+`, `B-D`, and the vertical matching
`X-(z+X)`.  In particular a `C_+` vertex has no non-`A` neighbour.  This
validates the key projection premise.

For a Hamilton cycle `H`, every `R in C_+` has two distinct `A` neighbours,
which are distinct rank-`r` facets of `R`.  Their Johnson edge has union
exactly `R`; distinct `R` give distinct physical edges because the union
recovers `R`.

At `X in A`, the unique vertical edge is either selected or not, so its
projected degree is respectively one or two.  A projected cycle would
saturate both cycle incidences at every one of its `A` and `C_+` vertices,
making it a connected component of `H`.  Since `B,D` are nonempty, this is
impossible.  Thus the projection is a spanning forest.  Its edge count is
`U=W-C`, forcing exactly `C` components and `2C` degree-one vertices.  By
the degree formula, those are exactly the selected vertical edges.  Theorem
2.1 is GO.

The opposite-half statement is dual: each `z+L in B` has two `D` neighbours
`z+X,z+Y`; after deleting `z`, `X cap Y=L`.  It gives a separate
lower-exact forest, not simultaneous two-palette exactness.  The theorem
states this limitation explicitly.

## 3. Depuncturing audit

One balanced collar has vertices

\[
 P,M_0,\ldots,M_h,N.
\]

Its nonrepeated stem has `s=h+1` edges:

\[
 M_0M_1,\ldots,M_{h-1}M_h,M_hN.
\]

They use exactly the `s` distinct colours
`U_1,...,U_h,U_*`.  The omitted left seam `PM_0` repeats `U_1`.

If the stem is an initial component segment, deleting the `s` owners
`M_0,...,M_h` deletes exactly those `s` edges and leaves `N` as the new
initial endpoint.  It does not split or delete the component.  Distinct
stem components therefore leave the component count unchanged.  Exact
upper bijectivity removes precisely `mathcal U_B`.

Conversely attaching the stem backwards at the exposed endpoint `N` adds
`s` new vertices and `s` edges to one path, creates no cycle, and restores
precisely `mathcal U_B`.  The two operations are literal inverses.  Adding
the `C-1` left seams follows the assumed component-level spanning path and
therefore produces one owner Hamilton path.  Each such seam contributes
only the declared second copy of `U_1`.  Theorem 4.1 is GO.

The defect corollary correctly requires two extra hypotheses: the stem
colours themselves are present, and no outside edge also uses one.  Under
those hypotheses deleting/restoring the stems cannot change any defect on
the complementary palette.

## 4. Endpoint-role audit

An oriented `C`-path forest has exactly `C` omitted head roles (initial
endpoints) and `C` omitted tail roles (terminal endpoints).  The active
role banks both have size `W-C=U`, exactly the size of the upper palette.

A matching saturating upper, active-tail, and active-head parts gives
indegree/outdegree at most one and uses every permitted role exactly once.
It is therefore `C` source-to-terminal paths plus possible directed cycles.
After adding the `C-1` formal collar arcs, exactly one source and one sink
remain.  The augmented graph is one spanning path plus possible directed
cycles.  Acyclicity is thus necessary and sufficient.  A common strict
potential makes it automatic.  Theorem 5.1 is GO.

## 5. Scope audit

The result proves:

* unconditional **unprotected, upper-only** Catalan forest existence;
* exact deletion/restoration equivalence for a supplied balanced collar
  bank; and
* a sufficient protected middle-levels target.

It does not prove:

* that the upper and lower exact half-projections coincide;
* that a Hamilton cycle contains the prescribed Catalan-scale stem bank;
* residence, deeper upper witnesses, or named lower flags; or
* the full punctured protected theorem.

The theorem file states all four exclusions.  Overall audit verdict:

\[
                         \boxed{\text{GO WITH STATED SCOPE}}.
\]
