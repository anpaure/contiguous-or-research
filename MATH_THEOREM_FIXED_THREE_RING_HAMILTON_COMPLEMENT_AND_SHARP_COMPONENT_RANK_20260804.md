# Fixed three-ring Hamilton complements and the sharp component-rank boundary

**Date:** 2026-08-04  
**Status:** unconditional exact reduction and component theorem for the
six transport hexagons in
`MATH_THEOREM_OPEN_HEX_PAIR_TRANSPORT_AND_FIXED_RING_PLANTING_20260804.md`.
It proves that a phase-clean Hamilton target for the opposite eighteen-edge
phase automatically gives a protected completion with at most thirteen
components.  It also characterizes exactly when the six fixed hexagons are
a strict component hypertree and gives the exact additional circuit rank
needed otherwise.  It does **not** prove the remaining phase-clean rooted
Hamilton extension.

No computation or search is used.

## 0. The two eighteen-edge phases

Specialize the open-hex transport theorem to `c=3`.  Index its six
incidence hexagons by

\[
        J=\{(i,e):i\in\mathbb Z_3,\ e\in\{0,1\}\}.
\]

For `j in J`, let `O_j` be its old three-edge perfect matching and `N_j`
its opposite three-edge perfect matching.  Thus

\[
 O_j=\{I_iU_{i,e},\;Y_{i,e}A_{i,e},\;W_{i,e}C_{i,e}\},
\tag{0.1}
\]

and

\[
 N_j=\{I_iY_{i,e},\;A_{i,e}W_{i,e},\;C_{i,e}U_{i,e}\}.
\tag{0.2}
\]

Put

\[
                  D=\dot\bigcup_{j\in J}O_j,
       \qquad     N=\dot\bigcup_{j\in J}N_j.
\tag{0.3}
\]

The unions in (0.3) are edge-disjoint.  Hexagons belonging to the two
roles at one ring root share that root but no edge; all other vertices are
private.  Consequently

\[
 |D|=|N|=18,
 \qquad D\cap N=\varnothing,
 \qquad d_D(v)=d_N(v)\quad\text{for every }v.
\tag{0.4}
\]

At a ring root both degrees in (0.4) are two; at every other used vertex
they are one.

Call a Hamilton cycle `H` **phase-clean** when

\[
                         N\subseteq H,
             \qquad     D\cap H=\varnothing.
\tag{0.5}
\]

The avoidance clause is essential.  Merely containing `N` does not permit
the set-theoretic replacement `N -> D` when an old edge is already present.

## 1. Exact Hamilton-complement equivalence

### Theorem 1.1 (phase-clean complement equivalence)

The following are equivalent.

1. There is a phase-clean Hamilton cycle `H`.
2. There is a spanning two-factor `F_0` such that

   \[
        D\subseteq F_0,\qquad N\cap F_0=\varnothing,
   \tag{1.1}
   \]

   and simultaneously toggling the six transport hexagons gives a
   Hamilton cycle.

Under the equivalence the two objects determine one another by

\[
       F_0=(H\setminus N)\cup D,
       \qquad
       H=(F_0\setminus D)\cup N.
\tag{1.2}
\]

#### Proof

Assume first that `H` satisfies (0.5).  Equations (0.4) give, at every
vertex,

\[
 d_{(H-N)\cup D}(v)=2-d_N(v)+d_D(v)=2.
\]

The edge sets are disjoint by (0.5), so this is a simple spanning
two-factor satisfying (1.1).  Reversing the replacement recovers `H`.

Conversely, if `F_0` satisfies (1.1), the same degree calculation shows
that the second graph in (1.2) is a spanning two-factor.  By hypothesis it
is Hamiltonian; (1.1) says precisely that it contains `N` and avoids `D`.
\(\square\)

Thus the bounded-component question is not another unrestricted
two-factor-extension problem.  Its exact remaining positive premise is

\[
 \boxed{\text{a Hamilton cycle of }ML_m\text{ containing }N
        \text{ and avoiding }D.}
\tag{1.3}
\]

This is a rooted, phase-labelled Hamilton extension statement for one
fixed path forest of eighteen edges.

## 2. Thirteen components are automatic from a Hamilton complement

For a two-factor `F_0` containing `D`, form the **occurrence incidence
multigraph** `B(F_0)` as follows.

* Its left vertices are the components of `F_0`.
* Its right vertices are the six transport hexagons.
* For each of the three old edges of a hexagon, add one incidence edge to
  the component of `F_0` containing that old edge.

Parallel incidences are retained.  They record that two old edges of one
hexagon lie on the same factor component; suppressing them would erase the
strictness obstruction.

### Lemma 2.1 (component barriers)

If a collection of the six hexagons is toggled, no resulting factor
component can use old material from two different connected components of
`B(F_0)`.

#### Proof

Outside the displayed hexagons every edge stays fixed.  A toggle reconnects
only the path pieces belonging to factor components incident with its own
right vertex.  Induction over any toggle order therefore preserves each
connected component of `B(F_0)` as a closed block. \(\square\)

### Theorem 2.2 (sharp thirteen-component bound)

If the equivalent conditions of Theorem 1.1 hold, then

\[
                    \boxed{|\operatorname{Comp}(F_0)|\le13.}
\tag{2.1}
\]

More exactly, `B(F_0)` is connected and its cyclomatic number is

\[
 \boxed{
   \beta(B(F_0))
      =|E|-|V|+1
      =18-(6+|\operatorname{Comp}(F_0)|)+1
      =13-|\operatorname{Comp}(F_0)|.}
\tag{2.2}
\]

#### Proof

All six toggles produce the one-component factor `H`.  Lemma 2.1 therefore
forces `B(F_0)` to be connected; in particular, no component of `F_0` is
disjoint from `D`.  The multigraph has exactly eighteen incidence edges,
six right vertices, and one left vertex per component of `F_0`.  Every
connected multigraph has at least one fewer edge than vertices, giving

\[
 18\ge6+|\operatorname{Comp}(F_0)|-1.
\]

This is (2.1), and the connected cyclomatic identity gives (2.2).
\(\square\)

There is also a direct surgery proof of the scalar bound.  Replacing one
three-edge phase of an alternating hexagon changes the component count of
a two-factor by at most two: if its three old edges meet `t` old cycles,
deleting them produces three path pieces in those cycles, and the new
matching reconnects those three pieces into between one and three cycles.
Starting from the Hamilton target and reversing six hexagons therefore
creates at most `1+6*2=13` cycles.  Formula (2.2) is stronger because it
records the exact lost strict rank.

### Corollary 2.3 (strictness is the equality case)

The six fixed transport hexagons form the strict component hypertree of the
open-hex theorem if and only if

\[
                         |\operatorname{Comp}(F_0)|=13.
\tag{2.3}
\]

#### Proof

By (2.2), equality in (2.3) is equivalent to `B(F_0)` being a tree.  A tree
has no parallel pair, so the three old edges of each hexagon lie on three
distinct factor components.  Leaf-order contraction is therefore strict
at every step, exactly as in the transport-hypertree theorem.

Conversely, a strict component hypertree is a tree with six right vertices
of degree three.  It has eighteen edges, hence thirteen left vertices.
\(\square\)

This exposes an important optimization reversal:

\[
 \boxed{
  \text{inside the Hamilton-complement fibre, minimizing components is
  not a route to strictness; strictness asks for the maximum value }13.}
\tag{2.4}
\]

A phase-clean Hamilton target with fewer than thirteen inverse components
still solves the topology problem—the six simultaneous toggles return the
Hamilton cycle—but its fixed incidence multigraph has cycles, so the
leaf-order strict-hypertree certificate is unavailable.

## 3. Exact extra-circuit rank when the fixed six are a forest

The following statement applies to an arbitrary two-factor completion
`F` containing `D`, without assuming a Hamilton target.

Let `B_6=B(F)`.  Include as isolated left vertices every factor component
not meeting `D`.  Suppose first that `B_6` is a forest, and let

\[
                         q=|\operatorname{Comp}(B_6)|.
\tag{3.1}
\]

An additional alternating circuit is **strict of arity `s`** when its old
phase meets `s` distinct current component blocks and its toggle merges
those `s` blocks without splitting.  In the component-incidence graph it
is one new right vertex of degree `s`.

### Theorem 3.1 (sharp residual hypertree rank)

Any additional strict circuit bank extending the fixed six to a component
hypertree must supply exactly

\[
                              \boxed{q-1}
\tag{3.2}

units of component rank, where an arity-`s` circuit supplies `s-1` units.
Conversely, any available strict circuits whose incidence edges connect the
`q` blocks without a cycle and whose ranks sum to `q-1` extend `B_6` to a
tree.

#### Proof

Contract every component of the forest `B_6`.  The problem becomes joining
`q` supervertices by new right nodes.  Adding an arity-`s` right node and
its `s` incidences to a forest lowers the number of connected blocks by
`s-1` exactly when it creates no cycle.  A tree has one block, so the total
rank is necessarily and sufficiently `q-1`. \(\square\)

For the present fixed six, foresthood gives

\[
 q=|V(B_6)|-|E(B_6)|
   =|\operatorname{Comp}(F)|+6-18
   =|\operatorname{Comp}(F)|-12.
\tag{3.3}
\]

Hence the exact residual component rank is

\[
                   \boxed{|\operatorname{Comp}(F)|-13.}
\tag{3.4}

If only additional strict ternary hexagons are allowed, (3.2) requires `q`
odd and exactly

\[
                         {q-1\over2}
       ={ |\operatorname{Comp}(F)|-13\over2}
\tag{3.5}
\]

hexagons.  If `q` is even, then in a catalogue consisting of strict
ternary hexagons and rank-one binary connectors, one binary connector plus
`(q-2)/2` ternary hexagons is the smallest bank by circuit count, provided
those circuit types are physically available.  These scalar counts do not
assert the required Boolean occurrences; Theorem 3.1 says exactly what an
occurrence catalogue must realize.

### Proposition 3.2 (a cyclic fixed bank cannot be repaired by addition)

If `B_6` contains a cycle, no bank obtained merely by adjoining more
circuit nodes can be a component hypertree.  At least one fixed transport
hexagon on every right-node feedback set must be replaced, or a non-strict
Hamilton certificate must be used instead.

In particular, in the Hamilton-complement situation the number

\[
                         13-|\operatorname{Comp}(F_0)|
\tag{3.6}

is exactly the cycle-space dimension of the obstruction.  Deleting one
degree-three hexagon node lowers this dimension by at most two, so at least

\[
 \left\lceil{13-|\operatorname{Comp}(F_0)|\over2}\right\rceil
\tag{3.7}
\]

fixed hexagons would have to be replaced in the worst scalar sense.  The
exact replacement number is the minimum feedback set restricted to the six
right nodes.

#### Proof

Adjoining vertices and edges never destroys a pre-existing graph cycle.
The rank bound follows because removing a degree-three right vertex removes
three edges and one vertex, decreasing cyclomatic number by at most two.
\(\square\)

## 4. Consequence for the topology programme

### Proposition 4.1 (the arbitrary-completion route is sharply false)

For every `m>=104`, the same old bank `D` has a spanning two-factor
completion with at least fifteen components.  More generally it has a
completion with at least

\[
                    1+\left\lfloor{m-20\over6}\right\rfloor
\tag{4.1}

components.

#### Proof

Use the common core `B` from the transport construction.  Outside `B`, the
bank `D` uses only the six labels

\[
                    b,a_0,a_1,a_2,z_0,z_1.
\]

Put

\[
                         t=\left\lfloor{m-20\over6}\right\rfloor.
\]

The complement of `B` has `m+1` labels, so after excluding those six labels
there are `m-5` spares.  Since `3t<=m-5`, choose `t` disjoint triples of
spare labels.  On core `B`, each triple supports one incidence hexagon.
The resulting `t` hexagons are vertex-disjoint: their lower vertices are
`B+x` and their upper vertices are `B+x+y`, and the active triples are
disjoint.  They are also disjoint from `D`.  The root and source/target
owners of `D` use one of the six excluded external labels; its remaining
vertices omit one of the private core labels `d_(i,e)`, whereas every new
hexagon vertex contains all of `B`.

Protect all six edges of every new hexagon together with `D`.  This bank is
2-bounded and has

\[
                         18+6t\le m-2
\]

edges.  The small protected-factor theorem extends it to a spanning
two-factor.  Every protected hexagon is already degree-saturated and hence
is an isolated six-cycle component.  The vertices used by `D` lie outside
those cycles, so at least one further factor component exists.  This proves
(4.1).  For `m>=104`, `t>=14`. \(\square\)

Thus even the very special Boolean geometry of `D`, together with the exact
small protected-factor theorem, does not control the topology of an
arbitrary completion.  Proposition 4.1 does not rule out a different good
completion; it proves that the completion and topology objective must be
chosen jointly.

### Theorem 4.2 (exact canonical-pull test and strictness no-go)

Let `C_m` be the canonical GMN Middle-Levels cycle factor and `H_m` its
connected labelled pull auxiliary multigraph.  Suppose the six physical
transport hexagons can be chosen as six canonical pull occurrences whose
old phases are exactly `D`, and suppose their six auxiliary labels form a
graphic forest `A` in `H_m`.

Then there is a phase-clean Hamilton cycle for `N`.  More precisely, extend
`A` to a labelled spanning tree `T` of `H_m`, toggle every label in `T-A`,
and call the resulting factor `F_0`.  Then

\[
  D\subseteq F_0,qquad N\cap F_0=\varnothing,qquad
  |\operatorname{Comp}(F_0)|=7,
\tag{4.2a}
\]

and toggling the six labels in `A` gives a Hamilton cycle `H` satisfying

\[
                         N\subseteq H,qquad D\cap H=\varnothing.
\tag{4.2b}
\]

However, these six occurrences can never be the strict ternary
component-hypertree of the open-hex theorem relative to `F_0`.  Every
canonical pull label is binary at component level: two of its old factor
edges lie in one canonical component and the third lies in the other.
After the `T-A` contractions those two old edges still lie in one component.
Thus every right node of `B(F_0)` has a parallel incidence pair, and

\[
                         |\operatorname{Comp}(F_0)|=7<13.
\tag{4.2c}
\]

#### Proof

The canonical prescribed-pull theorem extends the graphic forest `A` to a
labelled spanning tree `T`.  Canonical pull hexagons are edge-disjoint and
tree-compatible.  Toggling `T-A` therefore contracts every component edge
of the tree except the six edges of `A`; deleting six edges from a tree
leaves exactly seven components.  Edge-disjointness leaves every old phase
in `A` present and every opposite phase absent, proving (4.2a).

Toggling the remaining labels completes the spanning pull tree, so the
result is the canonical Hamilton cycle.  The six old phases are removed and
the six new phases inserted, which is precisely (4.2b).

For a nonloop canonical label, its three old incidences have the `2+1`
distribution on the two distinct canonical factor components represented
by the endpoints of its auxiliary edge.  The contractions indexed by
`T-A` can merge components but cannot split the pair of old incidences
which began together.  Moreover the endpoints of an edge of `A` remain in
different `T-A` components, since the unique path between them in the tree
`T` uses that deleted edge.  Hence each selected pull meets exactly two of
the seven current components, with one occurrence counted twice.  This
gives a parallel incidence pair at each right node and rules out a strict
ternary hypertree. \(\square\)

Theorem 4.2 resolves the proposed standard-pull strategy at the topology
level:

\[
 \boxed{
  \text{canonical forest embedding }\Longrightarrow
  \text{phase-clean Hamilton target and a seven-component inverse,}
 }
\tag{4.2d}
\]

but

\[
 \boxed{
  \text{canonical forest embedding }\not\Longrightarrow
  \text{the strict thirteen-component ternary hypertree.}
 }
\tag{4.2e}
\]

The latter is no longer needed once (4.2b) is known directly.  The only
unproved row in this strategy is now local and literal: realize the six
common-core transport hexagons as six canonical pull occurrences with old
phases `D`, and verify that their auxiliary labels form a forest.  The
generic fact that every Boolean incidence hexagon is isomorphic to a pull
hexagon does not prove this simultaneous occurrence statement; one global
parenthesis order and the canonical old-edge provenance must work for all
six roles.

For the fixed three-ring, the old request

\[
 \text{find a thirteen-component completion and separately prove a strict
 hypertree}
\]

can be replaced by the single rooted target

\[
 \boxed{
  \text{find a Hamilton cycle containing the opposite phase }N
  \text{ and avoiding the old phase }D.}
\tag{4.3}
\]

Theorem 2.2 then supplies the bounded component count automatically.  If
the inverse completion has thirteen components, the desired strict
hypertree is automatic.  If it has fewer, strictness is unnecessary because
the terminal Hamilton cycle is already certified directly.

This does not prove (4.3).  The small protected-factor theorem applies to
`N` once `18<=m-2`, but gives an arbitrary two-factor rather than a
Hamilton factor.  Hamilton-laceability without a protected-path theorem
also does not imply (4.3).  The finite protected-Hamilton counterexample in
`ML_3` shows why that logical step cannot be made formally, although it
does not refute this special bank in the asymptotic range.

The Boolean-specific next target is therefore precise:

> **Three-ring phase-clean rooted extension.**  For all sufficiently large
> `m`, the eighteen-edge path forest `N` in (0.2) lies in a Hamilton cycle
> of `ML_m` avoiding `D`.

Equivalently, in a canonical pull factor, plant the six opposite phases as
a phase-cover forest and prove that the residual contracted pull quotient
is connected.  That is a joint factor/ring choice; it is not implied by
minimizing the component count of an arbitrary protected completion.

## 5. Self-audit

1. `D` and `N` each have eighteen edges.  At the three shared roots each
   has degree two; at every other used vertex each has degree one.  Thus the
   degree replacement in Theorem 1.1 is exact.
2. The phase-clean avoidance condition is stated explicitly.  Without it,
   set union could fail to restore degree two.
3. `B(F_0)` retains parallel incidences.  Hence its eighteen-edge count and
   cyclomatic identity do not silently assume that a hexagon is strict.
4. Connectivity of `B(F_0)` follows only under the terminal-Hamilton
   hypothesis; no arbitrary protected completion is claimed connected.
5. The equality `13` is `1+6(3-1)`, the exact maximum component reduction
   of six ternary switches.
6. Strictness is characterized, not assumed: a connected eighteen-edge
   incidence multigraph on six right and thirteen left vertices is a tree,
   which excludes repeated component incidences automatically.
7. The extra-circuit theorem assumes the fixed incidence graph is already
   a forest.  Proposition 3.2 records the sharp obstruction when it is not.
8. Proposition 4.1 uses complete protected hexagons, so each one is forced
   to remain an isolated factor component; it is a bad-completion witness,
   not a no-good-completion theorem.
9. Theorem 4.2 uses the canonical fact that a nonloop pull auxiliary label
   joins two distinct factor components and has a `2+1` old-edge
   distribution.  It does not apply to a genuinely ternary ECO label.
10. No Hamilton extension, upper-palette, residence, arbitrary-width deck,
   or common-cap claim is inferred from the component theorem.

## 6. Dependencies

| role | file |
|---|---|
| fixed six transport hexagons and old/new phases | `MATH_THEOREM_OPEN_HEX_PAIR_TRANSPORT_AND_FIXED_RING_PLANTING_20260804.md` |
| strict component-hypertree toggle criterion | `MATH_THEOREM_OPEN_HEX_PAIR_TRANSPORT_AND_FIXED_RING_PLANTING_20260804.md` |
| canonical phase-cover / residual pull quotient | `MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md` |
| canonical prescribed-pull forest extension and `2+1` old phase | `MATH_THEOREM_R_CANONICAL_MUTZE_PULL_COATOM_AND_RESIDENT_COLLAR_EMBEDDING_20260801.md` |
| small protected two-factor extension | `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md` |
| protected Hamilton extension scope warning | `MATH_THEOREM_O1_PROTECTED_Q1_HAMILTON_EXTENSION_CUT_20260801.md` |
