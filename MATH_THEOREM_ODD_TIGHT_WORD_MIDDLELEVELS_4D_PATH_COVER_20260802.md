# Odd tight words force a `4d`-component Middle Levels path cover

**Date:** 2026-08-02  
**Status:** unconditional consequence of covering the two equal central
layers at length `W+d`; no source factor, residence, upper-shadow theorem,
or universal construction is asserted.

## 0. Result

Let

\[
 k=2r-1,
 \qquad W=\binom{k}{r}=\binom{k}{r-1}.
\]

Suppose a nonempty subset word of length `W+d` covers every rank-`r` target
and every rank-`(r-1)` target.  Then the Middle Levels graph on those two
layers has a spanning alternating linear forest with at most

\[
 \boxed{4d}
\tag{0.1}
\]

components.

More precisely, the word itself canonically supplies an alternating core
forest with

\[
 c\le2d
\tag{0.2}
\]

components, using all `W` rank-`r` owners and `W-c` distinct coatoms.  The
remaining `c` coatoms can always be attached after at most `c` incidence
cuts, giving at most `2c<=4d` spanning paths.

For K17, `d=3`.  Thus every hypothetical length-24313 word induces:

* an owner/coatom core with at most `6` paths; and
* a full Middle Levels path cover with at most `12` paths.

This is independent of flatness, chain alignment, or any preselected
Middle Levels factor.

## 1. The forced near-rainbow core

Choose one witness interval for every rank-`r` target and order the `W`
intervals by left endpoint.  Incomparability of distinct equal-rank targets
makes their right endpoints strictly increasing as well.  Let

\[
 T_0,T_1,\ldots,T_{W-1}
\]

be the corresponding owner values.

Choose one witness interval for every rank-`(r-1)` target.  Group these
witnesses by physical left endpoint.  At most one distinct rank-`(r-1)`
target lies in one such nested chain.

The q1-rigidity theorem in
`MATH_THEOREM_K17_POSITIVE_SLACK_Q1_RIGIDITY_20260802.md` applies verbatim in
odd dimension.  All but at most `2d` coatom targets occur in clean selected-
start chains.  If `S_i` is the target in the clean chain at selected start
`i`, then

\[
 S_i=T_{i-1}\cap T_i,
\tag{1.1}
\]

so `T_(i-1),T_i` are Johnson-adjacent.  All such `S_i` are distinct.

The occurrence statement is equally rigid.  Let `J_i^max` be the maximal
lower-atlas cell beginning at this clean selected start.  The witness for
`S_i` is contained in `J_i^max`, while clean-chain containment gives

\[
 S_i\subseteq \operatorname{OR}(J_i^{\max})
 \subseteq T_{i-1}\cap T_i=S_i.
\]

Hence `OR(J_i^max)=S_i`.  Thus at least `W-2d` colours are not merely in
the abstract q1 palette: they occupy their physical maximal top ports.
Positive scalar slack can duplicate these colours lower in their chains,
but cannot move the compulsory top occurrences.

Let `E` be the set of these clean target-bearing transitions and put

\[
 g=|E|,
 \qquad c=W-g.
\tag{1.2}
\]

Then

\[
 c\le2d.
\tag{1.3}
\]

## 2. Exact core component count

For every `i in E`, insert the coatom `S_i` between its two owners:

\[
 T_{i-1}-S_i-T_i.
\tag{2.1}
\]

Because `E` is a subset of the transitions of one linear owner order, the
result is an alternating linear forest.  It uses:

\[
 W+g\quad\text{vertices},
 \qquad 2g\quad\text{edges}.
\]

Therefore its number of components is exactly

\[
 (W+g)-2g=W-g=c.
\tag{2.2}
\]

It covers every rank-`r` vertex and precisely `g=W-c` coatom vertices.  Let
`R` be the remaining coatom set; then

\[
 |R|=c.
\tag{2.3}
\]

Thus the number of missing coatoms equals the number of core paths.  This
equality is not an asymptotic count; it is Euler's formula for the forced
linear forest.

## 3. Attaching every remaining coatom

The incidence graph between the complete rank-`(r-1)` and rank-`r` layers
is `r`-regular on two equal shores.  It has a perfect matching.  Restrict
one such matching to `R`.  This gives an injection

\[
 \mu:R\longrightarrow\binom{[k]}r,
 \qquad S\subset\mu(S),
\tag{3.1}
\]

whose chosen owner vertices are distinct.

Start with the core forest and regard every `S in R` as an isolated vertex.
For each `S`, inspect the current degree of `mu(S)`.

* If that degree is zero or one, add the incidence edge
  `S--mu(S)`.
* If that degree is two, first delete either one of its two current
  incidence edges, and then add `S--mu(S)`.

The selected owners are distinct, so no owner receives two new leaves.
Every operation preserves maximum degree two.  Deleting an edge from a
forest and adjoining an isolated vertex by one edge also preserves
acyclicity.  Every vertex on both shores is now present.

Initially, after the `c` unused coatoms are added as isolated vertices,
there are `2c` components.  An attachment at an endpoint decreases the
component count by one.  An attachment at an internal owner first increases
it by one through the cut and then decreases it by one through the leaf
attachment.  Consequently the final component count is at most

\[
 2c\le4d.
\tag{3.2}
\]

Every component is a path (possibly a singleton), proving (0.1).

## 4. Exact leaf-only no-extra-cut criterion

The factor `2` in (3.2) is needed only when a remaining coatom is forced to
an internal owner.  Let the `c` core path components be

\[
 P_1,\ldots,P_c
\]

and expose the two free degree slots at its owner endpoints.  For a
singleton-owner component these are two occurrence-labelled slots at the
same owner.  Let `E` be the resulting set of `2c` endpoint slots.  Form a
bipartite graph `H` from the remaining coatoms `R` to `E`, with

\[
 S\sim e
 \quad\Longleftrightarrow\quad
 S\subset T(e),
\tag{4.1}
\]

where `T(e)` is the owner carrying the slot.

### Proposition 4.1 (leaf-only endpoint-slot Hall gate)

The core extends, using no deleted core incidence, by attaching **every**
member of `R` as a degree-one leaf at an old owner endpoint if and only if
`H` has a matching saturating `R`.  Such a leaf-only extension has the same
`c` components.

#### Proof

A matching saturating `R` attaches every unused coatom as a leaf to a
different free endpoint slot.  Degrees remain at most two and no two old
components are joined, so the result has exactly `c` spanning paths.

Conversely, in a leaf-only extension every member of `R` uses exactly one
free endpoint slot, and distinct coatoms consume distinct degree slots.
These attachments give a matching saturating `R` in `H`.  \(\square\)

The leaf-only qualifier is necessary.  A general no-cut cover with the same
component count may use one remaining coatom with degree two to merge two
old paths and leave another remaining coatom isolated.  It need not
saturate `R` in the endpoint-slot matching.

The exact unrestricted no-cut gate is still bounded.  Contract every old
core path to one vertex and retain the `c` vertices of `R`.  Select exactly
`c` legal endpoint incidences such that:

1. every owner endpoint slot has load at most one;
2. every coatom in `R` has degree at most two;
3. no physical owner--coatom edge is selected twice; and
4. the selected contracted multigraph is acyclic.

Starting from `2c` isolated contracted vertices, these `c` forest edges
leave exactly `c` components; expanding the old paths gives precisely a
same-`c`, no-core-cut spanning path cover.  Thus ordinary Hall solves the
useful leaf-only face, while the fully general face is a small
degree-two/graphic selection problem.  At K17 it has at most six coatom
vertices, six core vertices, and twelve endpoint slots.

## 5. Scope and consequence

The theorem is a necessary structural consequence, not a construction of
the word that induced it.  In particular, it does not show that an arbitrary
`12`-path Middle Levels cover has:

* depth-`d` literal source factorization;
* coordinate residence;
* immediate or deeper upper-shadow coverage;
* the correct start/deadline staircase; or
* a common lower compiler.

It does show that a Catalan-scale or `3807`-component central owner/coatom
topology cannot be intrinsic to an optimal odd-dimensional word.  Any such
word already carries a six-component K17 core, and the remaining central
completion is bounded by six named coatoms plus at most six incidence cuts.
