# Audit of the two-sided depth-one pseudofactor and complement-fusion note

Date: 2026-07-26

Audited file:
MATH_THEOREM_TWO_SIDED_Q1_PSEUDOFACTOR_AND_COMPLEMENT_FUSION_OBSTRUCTION_20260726.md.

Method: pure mathematics only.

## 0. Verdict

The following parts pass:

1. both even- and odd-ground cloned-hypergraph degree and codegree tables;
2. the short-cycle conflict counts and their fixed-\(L\) use;
3. the diagonal passage, cycle-breaking cost, and forest/component ledger;
4. the corrected physically-simple endpoint criterion for a specified
   spanning forest;
5. the complement inclusion--exclusion theorem;
6. the three-level GMM opposite-colour defect identity; and
7. the first-global-minimum GJM collision injection and its asymptotic
   \(1/4\) ratio.

The unconditional pseudofactor conclusion is sound, subject to the
explicitly imported Delcourt--Postle fixed-uniformity conflict-free matching
theorem:

\[
 e(F_m)=W-o(W),\qquad c(F_m)=o(W),
\]

and both depth-one colour maps are injective.  The diagonal argument gives
no rate stronger than \(o(W)\).

One substantive scope correction was required and has been applied.
Hamiltonizing all \(W\) owners is a sufficient endpoint gate, but is not
equivalent to constructing the requested cycle on \(W-o(W)\) owners.  The
latter may discard components of total mass \(o(W)\); conversely, an
almost-spanning cycle does not automatically absorb its omitted owners while
retaining almost all its edges.  Section 0 and the final gate statement have
therefore been narrowed.  The earlier duplicated “Proposition 3.1” heading
has also been removed.

## 1. Even-ground cloned hypergraph

For a lower colour \(S\), there are
\(\binom{m+1}{2}\) possible upper colours and four clone assignments.
The same count holds dually for an upper colour.  Hence

\[
 d(S)=d(U)=4\binom{m+1}{2}=2m(m+1).
\]

A fixed middle clone \(X^i\) has \(m^2\) projected Johnson neighbours and
two choices for the clone of the other endpoint, so

\[
 d(X^i)=2m^2.
\]

The nonzero pair codegrees are

\[
 4,\qquad 2m,\qquad 2m,\qquad 1
\]

for lower--upper, lower--clone, upper--clone, and adjacent-clone pairs.
Thus

\[
 D=\Delta=2m(m+1),\qquad
 \delta/\Delta=m/(m+1),\qquad
 \Delta_2=2m=o(D).
\]

A hypergraph matching projects to a simple Johnson graph of maximum degree
two: the two labelled clones of a middle owner can each occur at most once.
The colour vertices make both edge-colour projections injective.  Two
different lifts of one projected edge cannot both be selected because they
share its lower and upper colour vertices.

All formulas (1.3)--(1.5) pass.

## 2. Odd-ground cloned hypergraph

For \(J(2m+1,m)\), the lower, upper, and clone degrees are respectively

\[
 4\binom{m+2}{2}=2(m+1)(m+2),
\]

\[
 4\binom{m+1}{2}=2m(m+1),
\]

and

\[
 2m(m+1).
\]

The first formula chooses two new coordinates outside an \((m-1)\)-set.
The second chooses the two deleted coordinates from an \((m+1)\)-set.
The third is twice the Johnson degree \(m(m+1)\).

The maximum pair codegree is \(2(m+1)\), obtained from a compatible
lower-colour/clone pair.  Hence, with

\[
 D=2(m+1)(m+2),
\]

the minimum-to-maximum degree ratio is \(m/(m+2)=1-o(1)\), and
\(\Delta_2/D=o(1)\).

Every hyperedge contains one lower colour, so

\[
 |E(\mathcal H_m)|
 =D\binom{2m+1}{m-1}.
\]

Therefore

\[
 |E(\mathcal H_m)|/D
 =N^-=\binom{2m+1}{m-1}
 =\frac{m}{m+2}W^+
 =W^+-O(W^+/m).
\]

The fixed-\(L\) conflict counts use Johnson degree \(m(m+1)=\Theta(D)\)
and are unchanged in scale.  Thus Corollary 1.2 and its two target-hole
counts pass.

## 3. Short-cycle conflicts and the external theorem

Fix a lifted edge in a projected \(i\)-cycle.  After orienting it, the next
\(i-2\) projected continuation steps may be chosen freely and the closing
step is forced.  With Johnson degree \(Q=\Theta(D)\), this gives

\[
 \Delta_i=O_L(Q^{i-2})=O_L(D^{i-2}).
\]

More generally, a prescribed \(j\)-edge submatching which can occur in a
simple cycle projects to \(s\ge1\) disjoint paths.  The \(i-j\) new edges
fill \(s\) nonempty gaps between fixed endpoints.  A gap of length \(t\)
has at most \(Q^{t-1}\) completions, so

\[
 O_L(Q^{i-j-s})\le O_L(D^{i-j-1}).
\]

If the prescribed projection has the wrong degree pattern or already
contains a proper cycle, the extension count is zero.  Clone multiplicity
is \(O_L(1)\).  Thus (1.6)--(1.7) pass.

There are no size-two projected-cycle conflicts.  Under the
Delcourt--Postle terminology imported and audited in
ASYMPTOTIC_MATCHING.md, the two additional conflict 2-degree conditions
therefore vanish.

The proof is not self-contained: it uses the published Delcourt--Postle
small-codegree corollary in precisely the form recorded in
ASYMPTOTIC_MATCHING.md.  Given that form, the application is correct.  For
example, with \(\beta=1/3\),

\[
 O(m)\le D^{2/3},\qquad
 O_L(D^{i-2})\le \alpha D^{i-1}\log D,\qquad
 O_L(D^{i-j-1})\le D^{i-j-1/3}
\]

for every fixed \(L\) and all sufficiently large \(m\).  Fixed uniformity
is used before, not after, the diagonal passage.

The note should continue to identify this theorem as its sole external
matching black box.  It would be an overclaim to present Theorem 1.1 as an
elementary internal proof.

## 4. Diagonal passage and component ledger

The projection has maximum degree two, so its cycles are vertex-disjoint.
Girth greater than \(L\) implies that deleting one edge from every cycle
costs at most

\[
 W/(L+1).
\]

For every fixed integer \(t\), choose a threshold after which the
fixed-\(L=t\) matching error is at most \(W/t\), and let \(L(m)\) be the
largest eligible \(t\).  Then \(L(m)\to\infty\), and both matching loss and
cycle-breaking loss are \(o(W)\).  No theorem with growing conflict
uniformity is being invoked.

After unused owners are added as isolated vertices, the graph is a spanning
forest on \(W\) vertices.  Therefore

\[
 c(F_m)=W-e(F_m)=o(W)
\]

exactly.  Concatenating its path lists creates exactly one seam per
component, including the cyclic closing seam.  This proves no
\(o(W/m)\) component rate, so the warning against arbitrary geodesic seam
repair is correct.

## 5. Endpoint criterion

The current physically-simple version of Proposition 3.1 is correct.  A
Hamilton extension gives one connector at every path port.  After paths are
contracted, the connectors form a connected 2-regular multigraph.
Conversely, expanding such a quotient through the retained paths gives a
connected 2-regular simple graph on all owners.

The two qualifications newly present in the theorem are necessary:

* with one path component, its two distinct endpoints may be joined by a
  same-component closing edge, represented by a quotient loop;
* two isolated owners each have two formal ports, so the port matching must
  not use their one underlying Johnson edge twice.

For two components the quotient may be a two-edge multicycle, but its two
physical connector edges must be distinct.  The “physically simple”
condition enforces this.

Deleting \(d\) forest edges increases the component count by exactly \(d\);
that ledger passes.

### Remaining scope correction

This proposition is necessary and sufficient for a Hamilton extension of
that specified spanning forest.  It is stronger than the exact
almost-spanning target.

For a cycle on \(W-o(W)\) owners, it suffices to find, after \(o(W)\)
deletions, a subcollection of path components covering \(W-o(W)\) owners
whose ports admit a connected matching.  Components of total size \(o(W)\)
may be discarded.  Conversely, a cycle already constructed on \(W-o(W)\)
owners need not admit an edge-preserving absorption of all omitted owners.

Hence full endpoint Hamiltonization implies the desired target, but the two
forms in Section 6 are not equivalent without an additional robust
absorption theorem.

## 6. Complement fusion

Theorem 4.1 passes exactly.  Inside \(E(C)\),

\[
\begin{aligned}
 |C\cap P\cap cP|
 &\ge |C\cap P|+|C\cap cP|-|C|\\
 &\ge 2N-a-b-W\\
 &=W-2K-a-b.
\end{aligned}
\]

Only \(|E(C)|\le W\) is used.  Since \(K=W/(m+1)=o(W)\), retaining
\(N-o(W)\) edges from both one-sided cores forces \(W-o(W)\) common
edges.

If \(P\) is lower-rainbow, the common edges inherit distinct lower colours
from \(P\).  They also lie in \(cP\), whose upper colours are distinct by
De Morgan duality.  Thus the common subgraph is two-sided rainbow.
Reversal leaves the edge set unchanged, and a fixed coordinate conjugate
obeys the identical inclusion--exclusion estimate.

The scope statement is correct: this obstructs retention-based sparse
splicing only, not a construction using mostly new edges.

## 7. Three-level GMM defect identity

On ground \([2m+1]\), write

\[
 W=\binom{2m+1}{m},\qquad
 N^-=\binom{2m+1}{m-1}.
\]

In the three-level graph, the middle shore has size \(W\) and the outer
shore has size \(W+N^-\).  A saturating cycle therefore uses every middle
owner \(X_i\) and \(W\) distinct outer witnesses \(Y_i\).  Consecutive
middle owners are Johnson adjacent.  Let \(Z_i\) be the opposite colour of
that edge.

The present signed target support is exactly

\[
 Y\cup\operatorname{supp}(Z).
\]

Since \(|Y|=W\),

\[
\begin{aligned}
 M^-+M^+
 &=(W+N^-)-|Y\cup\operatorname{supp}(Z)|\\
 &=N^--|\operatorname{supp}(Z)\setminus Y|.
\end{aligned}
\]

Thus formula (5.1d) passes after replacing its locally ambiguous \(N\) by
\(N^-\).  The required estimate is exactly

\[
 |\operatorname{supp}(Z)\setminus Y|=N^--o(W).
\]

The global \(N\) introduced for even ground should not be reused here
without redefinition.

## 8. GJM first-minimum collision family

Let \(y\) have length \(2m-1\), weight \(m-2\), and endpoint height \(-3\).
Write \(y=A0B\) at the zero step which first attains the global minimum
\(h\).  Then \(A\) ends at \(h+1\), no earlier zero ends at \(h\), and
the suffix \(B\), started at height \(h\), never falls below \(h\).

For

\[
 x=A010B,
\]

the first and third displayed zeros start at height \(h+1\).  No zero
starts lower, and these are the two leftmost zeros on that lowest row.
Because equal-height down-steps are scanned right-to-left, they are the last
two down-steps in lexical order.

For

\[
 x'=A001B,
\]

the second displayed zero starts at height \(h\) and is the unique zero on
that lower row.  The first displayed zero is the leftmost zero on the row
above, so these are again the last two lexical down-steps.  Consequently

\[
 \psi(x)=A111B=\psi(x').
\]

The selected lexical positions are intrinsic.  They distinguish the
distance-two \(010\) case from the adjacent \(001\) case, locate the
three-bit block, and recover \(y\) by contracting that block back to one
zero.  Hence different \(y\)'s give disjoint domain pairs.

If several disjoint pairs lie in one fibre, a fibre of size \(s\) contains
at most \(\lfloor s/2\rfloor\) such pairs while contributing \(s-1\) to
duplicate excess.  Therefore disjointness alone is enough; their common
images need not be distinct.

There are \(\binom{2m-1}{m-2}\) choices of \(y\), and

\[
 \frac{\binom{2m-1}{m-2}}{\binom{2m+1}{m}}
 =\frac{m-1}{2(2m+1)}
 =\frac14+O(m^{-1}).
\]

Thus Theorem 5.1 and its \(1/4-o(1)\) lower bound pass.  Deleting one
retained forest edge decreases duplicate excess by at most one, while
adding connector edges cannot remove a collision among retained edges.
The linear rerouting conclusion follows.

This theorem depends on the imported description of the GJM lexical map:
the contracted upper colour is obtained by flipping the last two down-steps
in the stated row scan, and the published six-cycle joins leave the lower
lexical forest unchanged.  Those source-interface facts were separately
audited in
MATH_OBSTRUCTION_THREE_LEVEL_OPPOSITE_COLOR_AND_GJM_LINEAR_COLLISIONS_20260726.md
and GJM_FOUR_LEVEL_AUDIT.md.  Given them, the collision proof is complete.

## 9. Repairs applied to the theorem note

1. “The exact remaining gate is endpoint-compatible Hamiltonization” was
   replaced by:

   > A sufficient remaining gate for this pseudofactor route is endpoint
   > Hamiltonization.  The exact almost-spanning gate allows discarding
   > components of total owner mass \(o(W)\).

2. The claim that the two final bullets are equivalent was removed.  Full
   endpoint Hamiltonization implies the desired almost-spanning cycle; the
   converse needs an additional absorption theorem.

3. Equations (5.1d)--(5.1e) now use \(N^-\), not the even-ground \(N\).

4. The duplicated Proposition 3.1 heading was removed.

5. The frontier-priority wording “strongest unconditional object currently
   available” was replaced by the theorem-safe “the following unconditional
   object is available.”
