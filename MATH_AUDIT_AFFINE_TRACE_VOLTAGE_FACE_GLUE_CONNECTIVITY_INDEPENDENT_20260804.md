# Independent audit of affine traces and voltage face glue

**Date:** 2026-08-04  
**Verdict:** **PASS after scope and collision-clarity repairs.**  The affine
trace representation, face-component quotient, complete fibre blow-up,
regular `H`-cover, component formula, and cycle-rank obstruction are all
correct.  Coincident images of different source coordinate directions do
not invalidate any claim, provided the first quotient is read—as now stated—
as the simple adjacency graph.

No search, H100 computation, solver, or finite enumeration was used.

## 1. Audited files

| role | file | SHA-256 |
|---|---|---|
| target before audit | `MATH_THEOREM_AFFINE_TRACE_VOLTAGE_FACE_GLUE_CONNECTIVITY_20260804.md` | `28c39666a1965bb3a4ea6441fd37a57ba62bb6d8d3f0845286887bda935562db` |
| target after audit | same file | `1a7e9a3b6bea7c26be7135d95d0400a255c4c789a044b8332a38bf21c550a7b3` |
| parent touch theorem | `MATH_THEOREM_TOUCH_NUMBER_BINARY_RESIDUE_AND_FACE_GLUE_GATE_20260804.md` | `a0a53ec1846d0bc613eae4a3ce00c3dc296e823ea9f3e06ad888364c90039e18` |

The hash of this audit note is reported outside the note.

## 2. Repairs applied

1. The theorem now explicitly says that `pi(E)` is a set and that
   `mathcal G` is the simple face-adjacency graph.  Several physical cube
   directions with one quotient image do not create parallel adjacency
   edges.
2. The complete blow-up proof now records why such coordinate collisions
   are harmless: any one realizing direction works, while the face-dependent
   correction lies in `A=A_1+A_2`.
3. The free `H`-action is now checked on edges as well as vertices, and the
   absence of edge inversion is explicit.  This proves the graph-cover
   property rather than merely a quotient action.
4. Parallel edges in `mathcal B` are explicitly identified as distinct
   translation orbits of simple edges of `mathcal G`, not duplicate physical
   coordinate labels.
5. The two-bit arithmetic consequence now restates the parent's necessary
   hypotheses: `M>nu_2(W_r)`, source dimension at least `M`, and
   `|U| congruent to W_r modulo 2^M`.

These are scope/interpretation repairs; no formula or conclusion was
reversed.

## 3. Affine trace representation

Inside a fixed source cell, every physical endpoint indicator is either a
constant, a source bit `x_j`, or its complement `1-x_j`.  A cell of the
second pairing fixes the integer occupancy of each of its pairs to
`rho in {0,1,2}`.

* Occupancy zero or two fixes both endpoint indicators.  After constants
  from the source-cell record are substituted, this produces affine bit
  constraints or an inconsistency.
* Occupancy one says that the two endpoint indicators are complementary,
  which is one affine equation over `F_2`.

Thus the common solution set is either empty or an affine binary subspace
`t+L`.  This derivation remains valid on a common source/second-frame pair:
the occupancy-one equation is then tautological on a singleton source pair,
whereas occupancies zero and two are incompatible.

The overlay description is also correct.  A free common pair supplies one
standard basis direction.  A free nontrivial alternating component supplies
the simultaneous flip of its singleton source-pair choices.  Distinct
overlay components have disjoint supports, so the listed direction vectors
are independent; fixed or inconsistent components contribute no freedom.

For arbitrary `t+L`, an ambient cube edge in direction `e_j` stays in the
trace exactly when `e_j in L`.  Therefore every trace path changes its
vertex by an element of

\[
 A(L)=\operatorname{span}\{e_j:e_j\in L\},
\]

and every element of this span is realized by successive legal cube edges.
The induced components are exactly the cosets of `A(L)`.  The face count
`2^(dim L-dim A(L))` follows.

## 4. Quotient fibres

For trace `i`, the face-component set is

\[
 \mathcal F_i=(t_i+L_i)/A_i.
\]

Since `A_i subseteq A=A_1+A_2`, projection modulo `A` is well-defined on
faces and maps onto

\[
 X_i=\pi(t_i)+\pi(L_i).
\]

Its kernel is exactly

\[
 (L_i\cap A)/A_i,
\]

so all fibres have the cardinality claimed in (0.6).

Let `F_i=t_i+ell_i+A_i`.  A cube edge in direction `e_j` joins `F_1` and
`F_2` precisely when there are `a_i in A_i` with

\[
 t_1+ell_1+a_1+t_2+ell_2+a_2=e_j.
\]

Projection proves necessity of

\[
 \varphi_1(F_1)+\varphi_2(F_2)\in\pi(E).
\]

Conversely, choose any physical direction realizing that membership.  The
remaining difference belongs to `A_1+A_2`, so it decomposes as `a_1+a_2`
and yields literal adjacent vertices in the chosen faces.  If either face is
replaced by another face in the same quotient fibre, its representative
changes by an element of `L_i cap A`; the same decomposition argument still
works.  Every base adjacency therefore expands to a complete bipartite
graph between the two face fibres.

This proves the “twin” assertion even when distinct `e_j` have equal
quotient image.  Their multiplicity is irrelevant to adjacency existence.

Projection cannot join different base components.  Conversely, every
nontrivial connected base component expands to a connected graph because
each base edge is complete bipartite.  An isolated base vertex may expand
to several isolated twins; this does not affect the claimed whole-graph
equivalence because a connected bipartite `mathcal G` with both shores
nonempty has an edge.  Hence face glue is connected exactly when
`mathcal G` is connected.

## 5. The regular voltage cover

The subgroup

\[
 H=\pi(L_1)\cap\pi(L_2)
\]

translates both affine shores.  It acts freely on vertices.  If `xy` is an
edge, simultaneous translation by `h` preserves it because

\[
 (x+h)+(y+h)=x+y
\]

in characteristic two.  The shore labels are preserved, so no edge can be
inverted.  An edge stabilizer fixes its initial vertex and is therefore
trivial.

For each quotient edge orbit and each vertex above its initial quotient
endpoint, translating one representative edge gives exactly one incident
lift.  Thus `mathcal G -> mathcal B` is a regular graph cover with deck group
`H`, not merely a free quotient action.

Coordinate-direction collisions still cause no problem.  They were already
collapsed in the simple graph `mathcal G`.  If two distinct simple edges of
`mathcal G` have the same pair of vertex orbits but are not `H`-translates,
they yield parallel edge orbits in `mathcal B`; these are legitimate and may
form two-edge cycles.

Choosing one lifted representative `s(v)` of every base vertex gives the
standard voltage rule

\[
 (u,h)\longmapsto(v,h+\omega(\bar e)).
\]

Changing the section adds a coboundary and leaves closed-walk voltages
unchanged as a subgroup.

## 6. Component and cycle-rank formulas

Fix one connected base component and a base vertex `v_0`.  A lifted closed
walk from `(v_0,h)` ends at `(v_0,h+omega(W))`.  Hence two points above
`v_0` are connected exactly when their labels differ by an element of the
closed-walk voltage subgroup `Omega`.  Base connectedness makes every lift
component meet every vertex fibre.  The number of lift components is

\[
 [H:\Omega].
\]

Summing this index over disconnected base components proves (3.3), including
isolated base vertices (`Omega=0`) and `H=0`.

For connected `mathcal B`, a spanning tree has
`|E|-|V|+1` non-tree edges.  Their fundamental closed walks generate all
closed-walk voltages, also in a multigraph with parallel edges.  If the lift
is connected, these voltages span the binary vector space `H`, giving

\[
 \dim H\le |E(\mathcal B)|-|V(\mathcal B)|+1.
\]

In particular a tree base can work only for `H=0`.  The obstruction is
necessary, not sufficient by itself; the theorem states the stronger exact
condition `Omega=H`.

## 7. Exact two-touch scope

Each affine trace decomposes into its connected face components.  Contracting
those connected faces in the induced cube graph on
`T_1 dotcup T_2=C-U` produces exactly the face-glue graph.  Therefore

\[
 C-U\text{ connected}
 \iff\text{face glue connected}
 \iff\mathcal B\text{ connected and }\Omega=H.
\]

Under the separately restated arithmetic hypotheses, the parent theorem
also supplies the necessary two-bit residue condition.  Neither arithmetic
nor voltage connectedness constructs a Hamilton interval: connected face
glue may lack a Hamilton face chain or compatible physical ports.

Accordingly, the theorem does not establish a globally disjoint two-touch
dicut, a Hamilton path through either shore, residence collars, macro Hall,
a palette, or a compiler.  Coordinate multiplicity may matter to those later
port/chronology questions, but it does not alter the audited connectivity
criterion.

