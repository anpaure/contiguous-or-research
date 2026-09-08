# PBBS rebundling: automatic balance in merge--reorder--split normal form and the nearest-factor exact cover

Date: 2026-07-27

## 1. Setup

Put

\[
 n=2m+1,
 \qquad V=\binom{[n]}m,
 \qquad W=|V|,
 \qquad B=W/n.
\]

A cycle or path family on middle owners is **point-balanced** if every
coordinate occurs equally often among its vertices.  Every PBBS component
and every wreath is point-balanced.  The complete vertex set \(V\) is also
point-balanced, since every coordinate occurs in
\(\binom{n-1}{m-1}\) middle sets.

The finite \(m=4,5\) certificates both use the same architecture: merge
point-balanced PBBS components, reorder a large component, and split off
target wreaths.  The following observation removes all balance bookkeeping
from the first and last phases.

## 2. Automatic-balance lemma

### Lemma 2.1

The disjoint union of point-balanced vertex families is point-balanced.  If
\(A\subseteq V\) is point-balanced, then its complement \(V\setminus A\) is
point-balanced.

#### Proof

Coordinate-incidence vectors add under disjoint union.  A constant vector
plus a constant vector is constant.  For the complement, subtract the
constant incidence vector of \(A\) from the constant incidence vector of
\(V\). \(\square\)

### Corollary 2.2 (pure merges)

Suppose a factor switch replaces several point-balanced components by one
component on their union.  The new component is point-balanced, independently
of the cyclic ordering chosen on that union.

### Corollary 2.3 (target peeling)

Fix a target wreath factor \(G=\{C_1,\ldots,C_B\}\).  Suppose a spanning
2-factor \(H\) consists of some target cycles \(C_i\) and one further cycle
on all remaining owners.  Then every component of \(H\) is point-balanced.

#### Proof

The selected target cycles are point-balanced.  Their union is
point-balanced by Lemma 2.1, hence the set of remaining owners is
point-balanced.  The one residual cycle contains that set exactly. \(\square\)

The corollary is stronger than a local signature test: it allows an arbitrary
ordering of the residual owners.  Balance is inherited from the *vertex set*,
not from the seams.

## 3. Conditional three-phase theorem

### Theorem 3.1

Let \(F\) be a spanning Kneser 2-factor with point-balanced components and
let \(G\) be a wreath factor.  Suppose physical factor-alternating switches
perform the following three phases.

1. **Merge:** each switch only merges current components, until one spanning
   cycle remains.
2. **Reorder:** switches retain one spanning cycle.
3. **Peel:** every state consists of completed cycles of \(G\) plus one cycle
   on the remaining owners, until the state is \(G\).

Then every intermediate component is point-balanced.  If the total number
of removed factor edges over the construction is \(O(B)\), this is a valid
\(O(B)\) balanced rebundling certificate.

#### Proof

Corollary 2.2 handles Phase 1.  The unique spanning cycle in Phase 2 contains
all of \(V\), which is point-balanced.  Corollary 2.3 handles Phase 3.  The
edge-cost assertion is the definition of the rebundling scale. \(\square\)

Thus, inside this normal form, the missing theorem is purely **physical**:
do the required Kneser alternating switches exist with Catalan-scale cost?
No separate centered-signature invariant remains to be checked.

The \(m=5\) certificate is close to this normal form.  It reaches one
462-cycle after 15 switches; its 303 switches have component-count changes

\[
\begin{array}{c|rrrrrr}
\Delta c&-2&-1&0&+1&+2&+3\\ \hline
\#&5&35&203&49&7&4.
\end{array}
\]

The 203 component-neutral switches are the dominant reorder phase.  The path
allows a few mergers after splitting begins, so it is not literally nested
target peeling; the theorem identifies a cleaner sufficient normal form, not
a description of every recorded step.

## 4. Nearest wreath factor as a maximum-weight exact cover

For a wreath \(C\), define its PBBS-retention weight

\[
 h_F(C)=|E(C)\cap E(F)|.
\]

Let \(\mathcal W_m\) be the set of geometric wreaths on \([n]\).  Consider
the integer program

\[
 \begin{aligned}
 \text{maximize}\quad&\sum_{C\in\mathcal W_m}h_F(C)x_C,\\
 \text{subject to}\quad&\sum_{C\ni X}x_C=1
                         &&(X\in V),\\
 &x_C\in\{0,1\} &&(C\in\mathcal W_m).
 \end{aligned}
 \tag{4.1}
\]

### Proposition 4.1

If the optimum of (4.1) is \(R^*(F)\), then the minimum edge distance from
\(F\) to an exact wreath factor is

\[
 \boxed{\tau(F)=W-R^*(F).}
 \tag{4.2}
\]

#### Proof

The equality rows in (4.1) say precisely that the selected wreaths partition
the middle owners, hence form an exact wreath factor \(G\).  Distinct selected
wreaths are vertex-disjoint, so their retained factor edges are distinct and

\[
 \sum_Ch_F(C)x_C=|E(F)\cap E(G)|.
\]

Both 2-factors have \(W\) edges.  Therefore
\(|E(F)\setminus E(G)|=W-|E(F)\cap E(G)|\), and maximizing retention is
equivalent to minimizing edge distance. \(\square\)

The LP relaxation has the explicit dual

\[
 \begin{aligned}
 \text{minimize}\quad&\sum_{X\in V}y_X,\\
 \text{subject to}\quad&\sum_{X\in C}y_X\ge h_F(C)
                          &&(C\in\mathcal W_m),
 \end{aligned}
 \tag{4.3}
\]

with unrestricted \(y_X\) because (4.1) has equality constraints.  A dual
solution of value \(W-cB\) would certify the lower bound
\(\tau(F)\ge cB\); an integer solution of value \(W-O(B)\) would prove the
static Catalan-scale sewing theorem.

This formulation separates two logically different tasks:

1. **static proximity:** prove \(R^*(F_{\rm PBBS})=W-O(B)\);
2. **dynamic routing:** realize a near-optimal factor by physical balanced
   switches, preferably in the normal form of Theorem 3.1.

The original static path-packet theorem is exactly the constructive side of
Task 1.  The finite switch certificates address Task 2.

## 5. Exact finite calibration at \(m=5\)

For \(m=5\), exhaustive enumeration gives the high-overlap wreath census

\[
\begin{array}{c|rrrrr}
h_F(C)&7&8&9&10&11\\ \hline
\#C&20449&2706&374&22&3.
\end{array}
\]

The threshold-8 subcatalogue covers every middle owner 26--132 times, but its
exact-cover instance is UNSAT.  Thus strong local availability does not
resolve the integer rows of (4.1).  This is a genuine small integrality gate,
not a degree shortage.

Verified feasible points currently give

\[
 \tau(F_{\rm PBBS})\le267,
 \tag{5.1}
\]

from `scratch/m5_nearest_pbbs_wreath_seed71.txt`.  The factor used by the
303-switch bridge has distance 306 but better shadow support.  Since
\(B=42\), these are \(6.36B\) and \(7.29B\), respectively.  They are
consistent with a Catalan-scale theorem at \(m=5\), but do not control the
constant as \(m\to\infty\).

## 6. Exact remaining mathematical target

A clean sufficient theorem is now:

> For canonical PBBS, solve (4.1) with value \(W-O(B)\), with a solution
> whose signed Gaussian-depth extraction loss is \(o(W)\); then route from
> PBBS to that solution by \(O(B)\) physical switches in merge--reorder--split
> normal form.

The first clause is the proximity/annulus design problem.  The second is a
Kneser switch-connectivity problem with automatic balance.  Neither is proved
asymptotically here, but the two sources of difficulty are now separated
exactly.

