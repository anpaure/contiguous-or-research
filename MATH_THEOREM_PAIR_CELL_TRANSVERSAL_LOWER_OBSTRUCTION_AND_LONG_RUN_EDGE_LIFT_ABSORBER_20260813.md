# Pair-cell transversal lower obstruction and a long-run edge-lift absorber

**Date:** 2026-08-13  
**Status:** unconditional exact lower-palette obstruction and unconditional structured
repair component.  The repair is owner- and lower-exact and is `q`-biresident under an
explicit transition-gap hypothesis.  It localizes, but does not yet complete, the
required rethread of the remaining top pair cells.

## 1. The inaccessible lower family

Put

\[
 k=2R-1,qquad p=R-1,qquad
 [k]=\{z\}\mathbin{\dot\cup}\bigdotcup_{i=1}^pP_i,qquad
 P_i=\{a_i,b_i\}.                                       \tag{1.1}
\]

For \(x\in\{0,1\}^p\), define the transversal facet

\[
 L_x=\{a_i:x_i=0\}\cup\{b_i:x_i=1\}.                    \tag{1.2}
\]

It has rank \(p=R-1\), omits the sentinel, and meets every pair in exactly one
coordinate.  There are exactly \(2^p\) such facets.

### Proposition 1.1 (exact inaccessible family)

A rank-\((R-1)\) facet is the intersection of an internal edge of a pair cell if and
only if it has an empty matched pair.  Consequently the facets (1.2) are exactly the
lower colours inaccessible to all internal pair-cell edges.

#### Proof

An internal pair-cell edge flips the selected endpoint of one singleton pair.  Its
two owner endpoints agree everywhere else, and their intersection is empty on the
flipped pair.

Conversely, if a facet \(L\) is empty on \(P_i=\{a_i,b_i\}\), then
\(L\cup\{a_i\}\) and \(L\cup\{b_i\}\) are rank-\(R\) owners in the same pair cell
and form an internal cube edge with intersection \(L\).

If a rank-\(p\) facet has no empty pair, it must omit \(z\) and take exactly one
coordinate from every \(P_i\), hence is one of (1.2).  \(\square\)

### Corollary 1.2

An owner cycle factor using only internal edges of this one pair structure cannot be
an exact lower factor.  It has \(W\) owner edges but only \(W-2^p\) accessible lower
colours, so some lower colours repeat and all \(2^p\) transversal facets are omitted.

This is a global palette obstruction; componentwise simplicity of the cube cycles
does not remove it.

## 2. Edge lift of a cube Hamilton cycle

Let

\[
 x_0,x_1,\ldots,x_{2^p-1},x_{2^p}=x_0                 \tag{2.1}
\]

be a cyclic Hamilton Gray code of \(Q_p\).  Write \(d_t\) for the unique direction
in which \(x_t\) and \(x_{t+1}\) differ, and define the rank-\(R\) owner

\[
                         D_t=L_{x_t}\cup L_{x_{t+1}}.     \tag{2.2}
\]

Thus \(D_t\) is double on \(P_{d_t}\), singleton on every other pair, and omits
\(z\).

### Theorem 2.1 (transversal edge-lift component)

The owners \((D_t)\) are distinct and form a simple Johnson cycle satisfying

\[
                         D_{t-1}\cap D_t=L_{x_t}.          \tag{2.3}
\]

Hence this one component uses every transversal facet exactly once and no other lower
facet.

#### Proof

The map from a cube edge to (2.2) is injective: its unique double pair recovers the
edge direction and its singleton choices recover the two endpoints.  A Hamilton cycle
has no repeated edge, so the \(D_t\) are distinct.

Consecutive directions satisfy \(d_{t-1}\ne d_t\), since otherwise
\(x_{t-1}=x_{t+1}\), contradicting simplicity of the Hamilton cycle.  The two lifted
owners are respectively double on these two distinct pairs and share exactly the
transversal choice \(L_{x_t}\).  This proves (2.3), Johnson adjacency, and exact
transversal lower coverage.  \(\square\)

## 3. Exact residence transfer

Measure cyclic separation between two occurrences of a transition direction by the
number of cube edges from the first occurrence to the second.

### Theorem 3.1 (one-unit gap loss)

If every two cyclically consecutive occurrences of every direction in (2.1) have
separation at least \(q+1\), then the lifted owner cycle \((D_t)\) is
`q`-biresident.

#### Proof

Fix a pair \(P_i=\{a_i,b_i\}\) and two consecutive direction-\(i\) transitions at
indices \(r<s\), with cyclic gap \(g=s-r\).  Between those transitions the cube bit
is constant.  The boundary owners \(D_r,D_s\) contain both \(a_i,b_i\), while the
interior owners \(D_{r+1},\ldots,D_{s-1}\) contain only the coordinate selected by
that constant bit.

Thus one physical coordinate has a positive run of length \(g+1\), and its mate has
a zero run of length \(g-1\).  At the next direction-\(i\) gap their roles reverse.
If every \(g\ge q+1\), all zero runs have length at least \(q\) and all positive
runs have length at least \(q+2\).  The sentinel is constantly absent.  This is
exactly `q`-biresidence.  \(\square\)

In particular the long-run cube theorem supplies such a component whenever

\[
                         p-3\log_2p\ge q+1.               \tag{3.1}
\]

The maximal depth-\((q-1)\) antecedent of this cycle is therefore a literal source
clock, by the standard erosion identity.

## 4. Optimal size and localized disruption

Every transversal facet needs two owner incidences.  Since an owner has degree at
most two in an exact owner/lower factor, any closed subfactor covering all
\(2^p\) transversal facets uses at least \(2^p\) owners.  The lift in Theorem 2.1
uses exactly \(2^p\), so it is cardinality-optimal.

Moreover \(D_t\) lies in the unique dimension-\((p-1)\) pair cell whose doubled pair
is \(P_{d_t}\), whose other pairs are singleton, and whose sentinel is absent.
There are only \(p\) such top cells.  Therefore replacing the internal pair-cell
cycles by the transversal lift disturbs owners only in these \(p\) cells.

The remaining exact gate is concrete.  For each direction \(i\), delete from its top
cube \(Q_{p-1}\) the vertices corresponding to the direction-\(i\) edges used by the
Hamilton code (2.1), and find a `q`-resident factor of the complements, with lower
colours disjoint from (1.2) and from one another.  The present theorem does not assert
that complement factor.

## 5. Upper row

At the transversal \(L_{x_t}\), the immediate-upper value is

\[
 L_{x_t}\cup
 \{\text{the opposite endpoint in }P_{d_{t-1}},
   \text{the opposite endpoint in }P_{d_t}\}.             \tag{5.1}
\]

It is a rank-\((R+1)\) set with two double pairs.  Two such values coincide exactly
when the corresponding Hamilton-cycle turns use the same unordered direction pair
at vertices of the same two-dimensional cube face.  Thus the lifted upper row is
simple precisely under this turn-injectivity condition.  No turn-injectivity or
global upper-cover assertion is made here; repeated upper values may instead be
handled by a separate support-preserving completion.
