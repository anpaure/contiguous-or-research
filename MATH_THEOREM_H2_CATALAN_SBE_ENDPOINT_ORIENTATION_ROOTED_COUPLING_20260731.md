# SBE endpoint orientations and the rooted strict side: exact quantifier order and flip laws

Date: 2026-07-31  
Status: exact fixed-forest reduction, exact one-flip criterion, and exact
rooted-preservation theorem; authenticated small obstruction to a direct
crossing-supermodular orientation theorem.  No all-parameter orientation,
rooted-side, residence, shadow, compiler, or contiguous-OR theorem is
claimed.

## 0. Verdict

For a fixed **undirected** Catalan path forest, coherent path orientation is
only an endpoint Boolean layer.  It does not change either strict occurrence
multigraph, any direct palette label, or any unordered physical occurrence
edge.  It chooses one terminal endpoint of each nontrivial component on the
upper shore and the opposite endpoint on the lower shore.  Consequently the
two SBE conditions form one exact signed Boolean covering system.

This layer precedes the common-basis and rooted-side choices:

\[
 F\quad\longrightarrow\quad \epsilon
 \quad\longrightarrow\quad Q
 \quad\longrightarrow\quad(S^-,S^+).
\tag{0.1}
\]

Here SBE can certify the existence of a direct common basis \(Q\), but it
does not certify that any such \(Q\) has a palette-perfect, capacity-safe
rooted Higgs lift.  Reversing a component after \(Q\) is frozen is literally
safe only when that component contains no edge of \(Q\).  If it contains a
selected edge, both puncture palettes change; no re-selection supported only
inside that path can preserve both old puncture palettes.

The endpoint system is not covered automatically by the standard
crossing-supermodular orientation theorem.  Although the unrounded Hall
defect is supermodular on outer-vertex families, its projection to path
endpoints is not crossing supermodular already on the authenticated \(n=3\)
forest.  Thus an all-parameter argument needs either special Boolean-cut
structure, a different extended formulation, or a direct construction.

## 1. The fixed data and the Boolean data

Let \(F\) be an undirected Catalan path forest on
\(X=\binom{[2n]}n\).  Its components are paths \(P_i\), with endpoints
\(a_i,b_i\); a singleton has \(a_i=b_i\).  Put

\[
 M=\binom{2n}n,\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad C=M-P,\quad R=N-C.
\tag{1.1}
\]

For each shore \(s\in\{-,+\}\), let
\(G^s=(O^s,X)\) be the complete strict direct occurrence graph.  An
occurrence obtained from an undirected child edge \(q=\{u,v\}\) depends on
only

\[
 L_q=u\cap v,\qquad U_q=u\cup v,
\tag{1.2}
\]

the collar coordinate, and the unordered physical edge.  Therefore
\(G^-\), \(G^+\), both palette labels, and the raw physical-edge map are
unchanged when any \(P_i\) is reversed.

Choose a bit \(\epsilon_i\) for every nontrivial path.  With a fixed
reference ordering of its endpoints, write

\[
 z_i^-(0)=a_i,\quad z_i^-(1)=b_i,\qquad
 z_i^+(0)=b_i,\quad z_i^+(1)=a_i.
\tag{1.3}
\]

Singleton endpoints belong to both terminal banks independently of the
dummy bit.  Thus

\[
 Z^s(\epsilon)=\{z_i^s(\epsilon_i):i\},\qquad
 T^s(\epsilon)=X\setminus Z^s(\epsilon).
\tag{1.4}
\]

The upper endpoint map uses the oriented tails and omits the upper terminal;
the lower endpoint map uses the oriented heads and omits the opposite
terminal.  These endpoint maps, their pullback matroids, and the SBE weights
are the orientation-dependent data.

### Proposition 1.1 (exact invariant/change table)

Before \(Q\) is selected, a component reversal:

* preserves \(G^\pm\), every raw direct occurrence, its two palette labels,
  and its unordered physical edge;
* swaps the two terminal candidates in (1.3), hence changes \(T^\pm\), the
  endpoint maps and possibly the two pulled-back strict matroids;
* does not itself select or alter a common basis \(Q\).

After a fixed edge set \(Q\) is supplied, its upper and lower root-anchor
banks

\[
 A_Q^- =\{U_q:q\in Q\},\qquad A_Q^+=\{L_q:q\in Q\}
\tag{1.5}
\]

are orientation invariant, as are the root stars, physical degree caps and
the ambient raw graphic matroids.  In contrast, the puncture palettes

\[
 D_Q^-(\epsilon)=X\setminus\{t_\epsilon(q):q\in Q\},\qquad
 D_Q^+(\epsilon)=X\setminus\{h_\epsilon(q):q\in Q\}
\tag{1.6}
\]

and hence the allowed palette restrictions of the rooted Higgs rows can
change.  The lower quotient/permutation row can change as well because its
tail/head boundary labels change.

#### Proof

Intersection, union and an unordered edge are symmetric in the two child
endpoints, proving the invariant assertions.  Coherent path reversal swaps
tails with heads and the omitted endpoints, proving (1.3)--(1.4).  Formula
(1.5) again uses symmetric edge colours, whereas (1.6) uses ordered
endpoints.  The strict occurrence restriction and the lower boundary copies
are defined from those ordered endpoint images. \(\square\)

## 2. Exact Boolean endpoint cuts

For \(A\subseteq O^s\), put \(B^s(A)=N_{G^s}(A)\).  Give an endpoint-image
middle vertex scaled weight \(R\), and a terminal scaled weight \(N\).  Since
\(N-R=C\), define the scaled slack

\[
 \sigma^s_\epsilon(A)
 =R|B^s(A)|+C|B^s(A)\cap Z^s(\epsilon)|-N|A|.
\tag{2.1}
\]

### Theorem 2.1 (signed Boolean cut system)

The orientation \(\epsilon\) is SBE on shore \(s\) if and only if

\[
 |B^s(A)\cap Z^s(\epsilon)|\ge
 \theta^s(A):=
 \max\left\{0,
 \left\lceil{N|A|-R|B^s(A)|\over C}\right\rceil\right\}
\tag{2.2}
\]

for every \(A\subseteq O^s\).  After the fixed singleton contribution is
removed, every row is an affine Boolean inequality whose coefficient on
\(\epsilon_i\) lies in \(\{-1,0,1\}\).  The two-shore condition is the union
of the upper rows and the lower rows under the opposite choice (1.3).

#### Proof

The weighted Hall inequality is exactly
\(N|A|\le R|B\setminus Z|+N|B\cap Z|\), which rearranges to (2.1).  The
left side of (2.2) is integral, so division by \(C\) and rounding is exact.
For component \(i\), replacing \(a_i\) by \(b_i\) changes its contribution
by
\({\bf1}_{b_i\in B}-{\bf1}_{a_i\in B}\in\{-1,0,1\}\).  The lower choice is
opposite by (1.3). \(\square\)

### Corollary 2.2 (single-cut orientation bounds)

For one row with neighbourhood \(B\), let \(u(B)\) be the number of path
components having at least one endpoint in \(B\), and let \(\ell(B)\) be
the number having both endpoints in \(B\), with singletons counted in both.
Then:

* if \(\theta(A)>u(B)\), this row obstructs every orientation;
* if \(\theta(A)\le\ell(B)\), this row holds for every orientation.

These tests are exact for one row but not sufficient for the simultaneous
two-shore system, because different rows may demand opposite choices.

### Theorem 2.3 (exact one-path flip test)

Fix \(\epsilon\) and a nontrivial component \(j\).  For each row define

\[
 \delta_j^s(A)=
 {\bf1}_{z_j^s(1-\epsilon_j)\in B^s(A)}-
 {\bf1}_{z_j^s(\epsilon_j)\in B^s(A)}.
\tag{2.3}
\]

Flipping exactly \(j\) makes both shores SBE if and only if, on both shores,

\[
\begin{array}{c|c}
\delta_j^s(A)&\text{necessary and sufficient old-slack bound}\\ \hline
+1&\sigma^s_\epsilon(A)\ge-C,\\
0 &\sigma^s_\epsilon(A)\ge0,\\
-1&\sigma^s_\epsilon(A)\ge C
\end{array}
\tag{2.4}
\]

for every outer family \(A\).

#### Proof

Only one terminal changes, so
\(\sigma^s_{\epsilon\oplus e_j}(A)=
\sigma^s_\epsilon(A)+C\delta_j^s(A)\).  Requiring this to be nonnegative
gives exactly (2.4). \(\square\)

Thus a one-flip repair must hit every violated row in the favorable
direction, no violation may exceed \(C\), and every row that loses its old
terminal must have at least \(C\) units of slack.

## 3. Correct quantifier order and the rooted safe-flip theorem

Let \({\cal A}^-_\epsilon,{\cal A}^+_\epsilon\) be the two strict pulled-back
matroids on the undirected child-edge ground.  If both SBE systems hold,
the constant point lies in both base polytopes, so matroid-intersection
integrality gives a distribution on common \(C\)-bases \(Q\).  The rooted
side theorem then asks, for a chosen \(Q\), for occurrence selections in

\[
 \text{two palette bases}\ \cap\
 \text{one rooted Higgs base}\ \cap\
 \text{physical degree caps},
\tag{3.1}
\]

followed by the separate lower quotient-graphic acyclicity test.

Consequently the proof-safe existential order is

\[
 \exists\epsilon\;[\mathrm{SBE}^-\wedge\mathrm{SBE}^+]
 \quad\Longrightarrow\quad
 \exists Q\in{\cal B}({\cal A}^-_\epsilon)
              \cap{\cal B}({\cal A}^+_\epsilon),
\tag{3.2}
\]

and the full strict target strengthens the right side to

\[
 \exists\epsilon\ \exists Q\ \exists S^-\ \exists S^+
 \quad\text{satisfying (3.1), capacities and lower topology.}
\tag{3.3}
\]

SBE proves only the first two quantifiers.  It supplies additive-cost
averaging over \(Q\), not the nonlinear rooted/cap/topology rows.

### Theorem 3.1 (verbatim rooted preservation under a \(Q\)-free flip)

Suppose \((\epsilon,Q,S^-,S^+)\) is a feasible fixed rooted strict tuple.
If path component \(P_j\) contains no edge of \(Q\), then reversing
\(P_j\) preserves verbatim:

* the common basis \(Q\) and both puncture palettes;
* both anchor banks and root stars;
* both chosen occurrence sets, palette labels, physical degree profiles and
  rooted Higgs ranks; and
* the tail/head-labelled lower quotient graph.

Hence the same tuple remains feasible.  Its SBE slacks change only by the
formula in Theorem 2.3.

#### Proof

The reversal changes endpoint maps only on edges of \(P_j\).  Since none is
in \(Q\), the endpoint images of \(Q\), (1.5), and (1.6) are unchanged.
Proposition 1.1 fixes all raw occurrence and physical data.  No seam boundary
copy belonging to \(Q\) lies in this component, so the lower quotient graph
is unchanged as well. \(\square\)

### Theorem 3.2 (sharp fixed-palette obstruction on a hit path)

Let \(P_j=v_0v_1\cdots v_m\) be oriented forward and suppose
\(I\subseteq\{0,\ldots,m-1\}\) indexes the edges of \(Q\cap E(P_j)\).
After reversing the path while keeping \(Q\), the old and new upper deleted
sets are respectively

\[
 \{v_i:i\in I\},\qquad\{v_{i+1}:i\in I\},
\tag{3.4}
\]

and the lower sets are swapped.  If \(I\ne\varnothing\), these sets are
different.  More strongly, even if \(Q\) is replaced on this path by a set
\(I'\), preserving **both** old deleted sets would require

\[
 I'+1=I,qquad I'=I+1,
\tag{3.5}
\]

and hence \(I=I'=\varnothing\).

Thus a flip of a \(Q\)-hit component cannot be treated as a local orientation
symmetry of an already frozen rooted lift.  It requires a genuinely new
common basis and/or new side selectors and anchors.

#### Proof

Equality of the two sets in (3.4) would make the selected directed subgraph
of a finite path balanced at every vertex.  A nonempty finite directed
forest has a source and a sink, so this is impossible.  If a new edge-index
set \(I'\) is allowed after reversal, its tails are \(I'+1\) and its heads
are \(I'\).  Equating them to the old tails \(I\) and old heads \(I+1\)
gives (3.5).  A finite integer set invariant under translation by two is
empty. \(\square\)

This is why the endpoint Boolean problem must be solved before selecting
\(Q\), except for the explicitly safe \(Q\)-free flips of Theorem 3.1.

## 4. Why the obvious generalized-polymatroid route does not apply

For one shore, the unrounded outer-family defect

\[
 d(A)=N|A|-R|N_G(A)|
\tag{4.1}
\]

is supermodular in \(A\), since neighbourhood cardinality is submodular.
However, orientation variables live on path endpoints, not on \(O\).  Let
\(E_\partial\) be the nontrivial endpoint bank and remove the fixed singleton
terminal contribution.  For an endpoint set \(S\subseteq E_\partial\), put

\[
 p(S)=\max\{\text{residual }\theta(A):
             N_G(A)\cap E_\partial\subseteq S\}.
\tag{4.2}
\]

Then the selected-terminal orientation system is equivalently
\(x(S)\ge p(S)\) for every \(S\).  Projection through the neighbourhood map,
integer rounding and fixed matching-edge contributions do not preserve
crossing supermodularity.

### Proposition 4.1 (authenticated \(n=3\) crossing violation)

On the authenticated \(n=3\) forest, order the nontrivial endpoints as

\[
 [13,19,28,37,41,49].
\tag{4.3}
\]

For the upper shore take

\[
 A=\{13,19\},\qquad B=\{19,28,37,41,49\};
\tag{4.4}
\]

for the lower shore take

\[
 A=\{13,19\},\qquad B=\{13,28,37,41,49\}.
\tag{4.5}
\]

In both cases the exact projected demands are

\[
 p(A)=1,\quad p(B)=3,\quad p(A\cap B)=0,
 \quad p(A\cup B)=3.
\tag{4.6}
\]

The pairs cross, but

\[
 p(A)+p(B)=4>3=p(A\cap B)+p(A\cup B).
\tag{4.7}
\]

Hence this natural proof-safe projected lower-demand function is not
crossing supermodular.  Subtracting the always-present internal edges of the
endpoint matching to convert selected-head bounds into in-cut bounds also
fails crossing supermodularity (and can only move farther from monotonicity).

This does not prove that no larger extended generalized-polymatroid
formulation exists.  It proves that the direct endpoint projection does not
meet the standard hypothesis.

## 5. Finite authentication and scope

The independent orientation-cube replay verifies that the occurrence banks
are invariant under every path-reversal generator.  On the authenticated
\(n=4\) forest, 7,600 of \(2^{14}\) orientation bitstrings satisfy SBE on
both shores.  Four components are singletons, so these are 475 of 1,024
distinct endpoint states, each represented 16 times.  The stored orientation
has two distinct one-path repairs.  At \(n=3\), zero of 32 bitstrings (zero
of eight distinct endpoint states) satisfy both shores.  Direct common bases
still exist there, so SBE remains sufficient rather than necessary.

The separate endpoint-demand audit verifies every one of the \(2^6\) outer
families on both \(n=3\) shores and checks (4.6)--(4.7).  It says nothing
about alternative parents or all \(n\).

Finally, the independent-rail theorem changes only the guard quantifier:
the structural forest \(F\) supplies this orientation/common-basis/rooted
problem, while an independent same-parameter forest \(G\) may supply the
isolated \(c\)-rail.  Choosing \(G\) does not repair a failed endpoint cut or
a failed rooted structural side.

Exact finite sources used here:

```text
MATH_THEOREM_H2_CATALAN_SBE_ENDPOINT_ORIENTATION_BOOLEAN_CUTS_20260731.md
scratch/audit_h2_catalan_sbe_endpoint_orientation_20260731.py
scratch/h2_catalan_sbe_endpoint_orientation_20260731.audit.json
scratch/independent_audit_catalan_sbe_orientation_cube_20260731.py
scratch/catalan_sbe_orientation_cube_20260731.independent.audit.json
scratch/audit_h2_catalan_sbe_endpoint_demand_n3_20260731.py
scratch/h2_catalan_sbe_endpoint_demand_n3_20260731.audit.json
```
