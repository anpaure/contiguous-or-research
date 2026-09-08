# Audit: receiver bicycle counterexample and common bicircular selector

**Date:** 2026-08-05  
**Audited files:**

* `MATH_COUNTEREXAMPLE_INVISIBLE_BICYCLE_ESCAPE_AND_PSEUDOFOREST_TREE_DISCOUNT_20260805.md`
* `MATH_THEOREM_TWO_SHORE_RECEIVER_BICIRCULAR_MATROID_PARITY_AND_FIXED_FAN_OBSTRUCTION_20260805.md`

**Method:** independent symbolic replay; no computation  
**Verdict:** PASS with the stated fixed-active-anchor scope.  The
counterexample refutes the unrestricted escape lemma, not every possible
joint choice of parent matching and anchors.

## 1. Sector and parent-criticality replay

Each of the nine coordinate pairs is in local state `12` or `21`, so every
displayed state has mass `9*3=27`, which is odd.  The coordinate length is
eighteen, hence the ordinary sector is bipartite.

The move `12 <-> 21` transfers one unit across the internal boundary of a
coordinate pair and stays in the critical residue alphabet.  Deleting that
boundary merges residues

\[
                         (4+1)+(4+2)\equiv5\pmod6.
\]

Thus the deleted-cut colour is a critical parent state.  This is why the
mass-one edge `10 <-> 01` would have been invalid for this purpose: its
merged residue is three, not critical.

Two chosen directions lie in disjoint coordinate pairs, so their moves
commute and give the required receiver `K_(2,2)`.  Deleting both boundaries
gives the common lower hub.  The superincreasing background `a_i=2^i`
makes the rooted background aperiodic and distinguishes different merged
sites after quotienting.

## 2. Tight-handcuff replay

For one group, the cross diagonal consists of group states `10` and `01`;
the other diagonal consists of `00` and `11`.  Therefore every edge in

\[
 0000-1000-1100-0100-0000
\]

and

\[
 0000-0010-0011-0001-0000
\]

is exactly one job's `B`-diagonal.

The displayed graph has eight labelled edges and seven vertices.  It is a
tight handcuff, so its endpoint-list deficiency is

\[
                              8-7=1.
\]

At a shared displayed vertex, incident jobs use different two-direction
groups.  Their receiver-square boundary edges are therefore distinct.
Opposite faces have different fixed contexts, and the two four-cycles use
disjoint direction groups.  Hence no boundary edge is reused.  Deleted-edge
hub colours are also distinct by the marked background and context, so the
sixteen passive parent petal edges have distinct endpoints.

One private active petal at each double-deleted hub makes the local fan
state `one active + one fixed passive pair`.  The active split blocks can be
chosen mutually disjoint inside an untouched, sufficiently large
residue-five macro part.  This validates the no-incoming-sidecar scope.

For `U=emptyset`, both `D` and ordinary slack are zero, while every job is
invisible and the endpoint deficiency is one.  The contradiction to the
unrestricted escape inequality is literal and precedes quotient folding.

## 3. Tree-discount replay

For a tree subgraph `F` with `c(F)` nontrivial components,

\[
 |F|-|V(F)\setminus D|=|D\cap V(F)|-c(F).
\]

Thus a touched tree component contributes at most `d_T-1`.  In a
unicyclic component every subgraph has at most as many edges as vertices,
so it contributes at most `d_C`.  Summing proves

\[
 \delta_Q(D)\le |D\cap V(Q)|-\tau_Q(D).
\]

Discarding visible jobs only removes edges and leaves a pseudoforest, so
the stated upper bound remains valid.

## 4. Common-selector replay

On either shore, job-to-endpoint incidence is a transversal matroid.  For
two-element lists, component rank is `min(e,v)`, hence the explicit
bicircular rank formula is correct.

The feasible two-shore job sets are exactly common independent sets of
the two transversal matroids.  Edmonds' formula therefore gives

\[
 \nu=\min_X(r_A(X)+r_B(E\setminus X)).
\]

Replacing each job by the paired copies `e_A,e_B` in the direct-sum
matroid gives an equivalent linear matroid-parity instance.  The generic
incidence matrices represent the transversal matroids because every
nonzero determinant monomial corresponds to an SDR and independent
incidence variables prevent cancellation.  The skew matrix
`RZ(y)R^T` consequently has generic rank `2nu` by the linear
matroid-parity theorem.

The hubwise perfect-petal-pairing constraint is not absorbed by this
two-matroid formula.  Nor is extension through the residual ordinary
sector: that remains the augmented perfect-matching/delta-matroid row.
The theorem files state both scope boundaries explicitly.

## 5. Quotient replay

For an invariant pseudoforest, component orbits reduce to `C/K`.  A finite
odd group acting on a tree fixes a root (edge inversion is impossible),
and the equivariant parent map makes the quotient a tree.  A unicyclic
component has a unique invariant cycle; an odd group acts on it by
rotations, and attached rooted trees remain trees after quotienting.
Therefore an invariant occurrence pseudoforest descends to a quotient
pseudoforest even without semiregularity.

This topological descent does not imply descent of quantitative ordinary
Hall slack, whose orbit weights can still be nonuniform.
