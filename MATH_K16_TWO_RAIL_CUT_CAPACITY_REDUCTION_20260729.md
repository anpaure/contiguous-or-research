# Exact two-rail cut-capacity reduction for the `15 -> 16` lift

Date: 2026-07-29

Status: Sections 1--3 and the qualitative fragment-port discussion remain
valid; the numerical calibration in Sections 4--5 is superseded by the
audited correction below.  No feasibility of the remaining port,
upper-shadow, or compiler systems is asserted.

**Audited correction (2026-07-29).**  Sections 4--5 previously conflated
two different rails and two different cut models.  The rail defined in
(1.1) is the Pascal facet rail `z+(T_i intersection T_(i+1))`; the `2010`
short-run census belongs instead to the pointwise complement rail
`z+([15]\T_i)`.  Moreover, the two-boundary clauses (4.1) have exact minimum
`1575`, whereas `1230` is the minimum for the broader full-collar clauses
which also permit every internal edge of a short run.  Therefore (5.1)--
(5.2) are not a calibrated numerical theorem for the facet rail.  The exact
corrected statement and audit are
`MATH_THEOREM_K_K15_COMPLEMENT_BRAID_COLLAR_TRANSVERSAL_AND_BB_RESTORATION_GATE_20260729.md`.

## 1. Odd factor and the even middle deck

Let

\[
 k=2r-1,
 \qquad
 W={k\choose r}={k\choose r-1},
\]

and let `F` be a q1-exact Johnson factor on
`binom([k],r)`.  Orient each physical component and write its consecutive
vertices and edge colours as

\[
 T_i,\qquad X_i=T_i\cap T_{i+1}.
\]

Q1 exactness means that the `X_i` are the `W` distinct members of
`binom([k],r-1)`.  Add a new coordinate `z` and define

\[
 A_i=T_i,
 \qquad
 B_i=\{z\}\cup X_i.
\tag{1.1}
\]

Then the `A_i` and `B_i` partition the middle layer
`binom([k] union {z},r)`.  Along every source component all four canonical
rail/rung transitions are Johnson edges:

\[
 A_iA_{i+1},\qquad
 B_iB_{i+1},\qquad
 A_iB_i,\qquad
 B_iA_{i+1}.
\tag{1.2}
\]

Indeed, the first and last two assertions follow from
`X_i subset T_i,T_(i+1)`.  The two sets `X_i,X_(i+1)` are distinct facets
of `T_(i+1)`, so their intersection has rank `r-2`; hence the second edge is
also Johnson.

Thus every q1-exact odd factor canonically produces a two-rail spanning
subgraph of the even middle-layer Johnson graph.  The lift problem is to
choose a Hamilton path in this subgraph, or in a controlled enlargement of
it, with residence and shadow constraints.

## 2. Exact segment accounting

Cut the `A` rail cycles into `a` nonempty contiguous paths and the `B` rail
cycles into `b` nonempty contiguous paths.  Preserve every internal rail
edge and concatenate the resulting `a+b` pieces into one path using cross
rail Johnson seams.  Then the edge-type counts are forced:

\[
 \#AA=W-a,
 \qquad
 \#BB=W-b,
 \qquad
 \#\text{cross}=a+b-1.
\tag{2.1}
\]

This is just the edge count of a disjoint union of paths: an `A` path cover
on `W` vertices with `a` components has `W-a` edges, similarly for `B`, and
joining `a+b` pieces into one path uses `a+b-1` seams.

The identity is independent of the order and orientation of the pieces.
It is therefore a hard arithmetic constraint on every segmented two-rail
lift.

## 3. The q1 capacity theorem

The child rank-`(r-1)` targets split as

\[
 { [k]\choose r-1}
 \quad\sqcup\quad
 \bigl\{\{z\}\cup S:S\in{[k]\choose r-2}\bigr\}.
\tag{3.1}
\]

An `AA` edge or a cross edge omits `z`, while a `BB` edge has colour

\[
 B_i\cap B_{i+1}
 =\{z\}\cup(X_i\cap X_{i+1}).
\tag{3.2}
\]

Consequently **only internal `BB` edges can realize the z-containing half
of (3.1)**.

For every rank-`(r-2)` target `S`, let

\[
 \mu(S)=\#\{i:X_i\cap X_{i+1}=S\}
\tag{3.3}
\]

over all oriented factor components, and let `C_B` be the set of cut `BB`
rail edges.  Assume the old lower-q2 deck is complete, so `mu(S)>=1` for
every `S`.  Then z-containing q1 coverage survives the cuts if and only if

\[
 |C_B\cap\{i:X_i\cap X_{i+1}=S\}|\le\mu(S)-1
 \qquad\text{for every }S.
\tag{3.4}
\]

Summing (3.4) gives the sharp scalar consequence

\[
 b=|C_B|
 \le
 \sum_S(\mu(S)-1)
 =W-{k\choose r-2}
 ={2W\over r+1}.
\tag{3.5}
\]

Here one cuts at least one edge on every original `B` cycle, so the number
of resulting `B` pieces equals `|C_B|`.  Conversely, (3.4), not merely
(3.5), is exactly the q1 condition: each colour retains at least one
surviving `BB` witness.

For `k=15,r=8`,

\[
 W=6435,
 \qquad
 {15\choose6}=5005,
 \qquad
 b\le6435-5005=1430.
\tag{3.6}

## 4. Residence hazards are a cut transversal

Fix the target depth `d`.  Consider the cyclic binary incidence word of an
old coordinate `x` along a `B` rail component.  A maximal positive run of
length `ell<=d` has two incident rail edges: the edge immediately before
the run and the edge immediately after it.  If neither edge is cut, the run
remains internal to one preserved `B` piece in every segmented braid and is
therefore an internal positive run of length at most `d` in the final path.
This violates depth-`d` residence.

Hence every such short run gives the necessary two-element clause

\[
 \text{cut(left boundary)}
 \quad\vee\quad
 \text{cut(right boundary)}.
\tag{4.1}
\]

Let `tau_B` be the minimum size of a cut set hitting all clauses (4.1), also
including at least one cut per physical `B` cycle.  Every segmented resident
lift satisfies

\[
 \tau_B\le b\le {2W\over r+1}.
\tag{4.2}
\]

This is only the first residence gate.  Hitting (4.1) moves every short run
to a fragment boundary; it does not automatically extend it.  The cross
seam incident with that boundary must continue `x` far enough into the
neighbouring `A` fragment, or the boundary must become one of the two global
ends.

The continuation condition is nevertheless local.  For every oriented
fragment endpoint and coordinate, record its terminal 0-run and 1-run
lengths, capped at `d+1`.  Two oriented endpoints are residence-compatible
exactly when, coordinate by coordinate, either

1. their membership bits agree and the two terminal run lengths sum to at
   least `d+1`; or
2. their bits differ and each newly internal terminal run already has
   length at least `d+1`.

At the two global ends the outward terminal run is exempt.  Thus, after the
cut set is chosen, residence is an exact finite port-compatibility problem
on the fragments; no full-word scan is needed inside the search.

## 5. The narrow `k=16` window

For the retained protected `k=15` factor, the current independent hazard
census reports `2010` clauses (4.1) and minimum transversal

\[
 \tau_B=1230.
\tag{5.1}
\]

Combining (3.6) and (5.1) leaves the exact scalar window

\[
 \boxed{1230\le b\le1430.}
\tag{5.2}
\]

The lift is therefore not an unconstrained Hamilton search on `12870`
vertices.  It is a capacitated cut problem with at most `200` cuts of scalar
slack, followed by a port matching/order problem.  The proof-safe first
stage is:

* choose `C_B` satisfying every hazard clause (4.1);
* impose every per-colour capacity (3.4), not only `b<=1430`; and
* expose the resulting oriented fragment endpoints for the exact residence
  compatibility relation of Section 4.

The reported value (5.1) must remain tied to its finite audit artifact.  It
is evidence about the retained `k=15` factor, not a general theorem about
all q1-exact factors.

## 6. Remaining exact gates

Passing (3.4), (4.1), and the port compatibility relation is necessary but
does not yet prove `nu(16)=12873`.  A complete lift must additionally check:

1. every old rank-`(r-1)` child q1 colour survives an `AA` or cross seam;
2. every higher union target survives inside a rail piece or is restored by
   a cross-piece interval;
3. the final middle chronology has a feasible exact `COMP_3(T)` antecedent,
   including its boundary residuals; and
4. literal enumeration of the resulting `12873` source word covers all
   `65535` nonempty masks.

These gates are naturally lazy: the cut/port master is small relative to
the full chronology, and each failed shadow or compiler audit supplies a
sound CEGAR cut.  A positive literal word plus the proved deadline lower
bound would establish

\[
 \nu(16)=12873.
\]

No such word is claimed here.
