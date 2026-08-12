# Decorated two-factors: exact component catalogue, gap Hall, and odd-residual trace safety

Date: 2026-07-31  
Status: exact correction and factor-level reduction; no all-dimension
decorated factor, residence, deep-shadow, socket, or compiler theorem

## 0. Verdict

Hamiltonicity is not needed for the middle-levels-supported Catalan Linear
Matching implication.  A componentwise decorated spanning two-factor is
enough, but there are **two** forbidden local trace faces, not one:

1. a mixed trace on which every positive zero-run has length two and every
   one-run has odd length; and
2. the wholly marked trace.

The second face was absent from the first snapshot of
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`.
The corrected source now excludes it.

This note gives three exact refinements of the corrected factor theorem.

* It proves the complete local trace trichotomy, including the two cycles
  on a wholly marked component.
* For a fixed factor, it reduces the full componentwise decoration problem
  to a finite multiple-choice two-palette exact-cover system.
* After fixing an upper-turn SDR, it reduces the lower marks exactly to one
  gap-versus-colour Hall matching.  If every marked component has a positive
  odd number of residual positions on each shore, the trace-forest row is
  automatic.
* For an already chosen perfect diamond matching, factor-resolvability is an
  exact bipartite \(b\)-flow problem, rather than a Hamilton-extension
  problem.

Thus the clean sufficient target is

\[
 \boxed{
 \text{spanning two-factor}
 +\text{ upper-turn SDR with positive odd residuals}
 +\text{ one global gap Hall matching}.}
 \tag{0.1}
\]

It implies Catalan Linear Matching, but it does not imply a literal
contiguous-OR word.

## 1. Setup and exact counts

Fix \(m\ge2\), put

\[
 \Omega=[2m-1],\qquad
 Q={2m-1\choose m-1}={2m-1\choose m},
 \qquad
 P={2m-1\choose m-2}={2m-1\choose m+1},
 \tag{1.1}
\]

and

\[
 K=Q-P=\operatorname {Cat}_m.
 \tag{1.2}
\]

Let \(F\) be a spanning two-factor of \({\rm ML}(2m-1)\).  Write one
factor component \(C\) as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1},
 \tag{1.3}
\]

with indices modulo \(q\).  Its turn colours are

\[
 \ell_i=A_i\cap A_{i+1}\in{\Omega\choose m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in{\Omega\choose m+1}.
 \tag{1.4}
\]

A mark at \(A_i\) selects \(u_i\), while a mark at \(B_i\) selects
\(\ell_i\).  On every marked component, “consecutive marks alternate
shores” always includes the cyclic last-to-first pair.

## 2. Exact local trace trichotomy

Encode the marks on \(C\) by a cyclic word \(w\in\{0,1\}^{2q}\).  When
both symbols occur and consecutive marks alternate shores, every positive
zero-run is even and the residual incidence paths have one forced perfect
matching.

### Theorem 2.1 (three local faces)

The physical diamond lift supported by \(C\) has the following exact
topology.

1. If \(w=0^{2q}\), either alternating residual phase gives \(q\)
   disjoint cross edges.
2. If \(w=1^{2q}\), the lift is the disjoint union of two same-rail
   \(q\)-cycles.
3. If both symbols occur, the lift contains a cycle if and only if

   \[
       \text{every positive zero-run has length }2
       \quad\text{and}\quad
       \text{every maximal one-run has odd length}.
       \tag{2.1}
   \]

   In case (2.1) it contains exactly one cycle; otherwise it is a linear
   forest.

#### Proof

In the all-zero case no turn is selected.  Either perfect-matching phase of
the alternating incidence cycle consists of \(q\) factor edges, and every
one lifts to one cross edge between the two physical rails.  These edges
are vertex-disjoint.

In the all-one case every \(A_i\)-turn is selected, so its physical edge is
\(B_{i-1}B_i\).  These \(q\) edges form the \(B\)-rail cycle.  Every
\(B_i\)-turn is also selected, producing
\((\infty+A_i)(\infty+A_{i+1})\), the disjoint \(A\)-rail cycle.  There is
no residual cross edge.

Suppose both symbols occur.  On a block \(0,1^a,0\), the turn chords
transmit a path between the two boundary zeroes exactly when \(a\) is odd.
On a positive zero-run, the forced residual matching transmits between its
two boundaries exactly when that run has length two.  A route therefore
closes around the original factor component exactly under (2.1); then it
is the unique transmitted cycle.  If any block fails to transmit, the
circular route is broken and every physical component is a path. \(\square\)

Consequently a marked component is admissible precisely when it is not
wholly marked and its mixed trace fails (2.1).  An unmarked component is
admissible in either residual phase.

## 3. The all-marked omission is a real obstruction

The missing face first occurs at \(m=3\).  Work on
\(\Omega=\mathbb Z_5\), with all subscripts modulo five.  Define

\[
 A_i=\{i,i+1\},\qquad B_i=\{i,i+1,i+2\},
 \tag{3.1}
\]

and

\[
 D_i=\{2i,2i+2\},\qquad E_i=D_i\cup D_{i+1}.
 \tag{3.2}
\]

Then

\[
 C=(A_0,B_0,A_1,B_1,\ldots,A_4,B_4,A_0)
 \tag{3.3}
\]

and the analogous \(C'=(D_i,E_i)_{i\in\mathbb Z_5}\) are two disjoint
ten-cycles which exhaust all rank-two and rank-three vertices of
\({\rm ML}(5)\).

Mark every occurrence of \(C\) and leave \(C'\) unmarked.  On \(C\),

\[
 \ell_i=\{i+1\},\qquad
 u_i=\Omega\setminus\{i+3\}.
 \tag{3.4}
\]

Thus the two turn palettes are globally bijective and the marked shores
alternate.  The word \(1^{10}\) is not caught by the mixed condition
(2.1), yet Theorem 2.1 gives two physical five-cycles.  The unmarked
component contributes five cross edges.  The lift consequently has two
cycles and seven connected components, rather than
\(\operatorname {Cat}_3=5\) paths.

This example is minimal in \(m\): at \(m=2\), \({\rm ML}(3)\) is one
six-cycle and \(P={3\choose0}=1\), so a globally bijective decoration marks
only one occurrence on each shore and cannot wholly mark the component.

## 4. Correct factor-to-diamond theorem

### Theorem 4.1

Suppose a spanning two-factor \(F\) has marks satisfying:

1. the selected \(A\)-turns enumerate \({\Omega\choose m+1}\) exactly
   once;
2. the selected \(B\)-turns enumerate \({\Omega\choose m-2}\) exactly
   once;
3. selected shore types alternate cyclically on every marked component;
4. no marked component is wholly marked; and
5. every mixed component fails the cycle condition (2.1).

Choose either residual phase on every unmarked component.  Then the
resulting diamonds form a perfect matching between Boolean ranks \(m-1\)
and \(m+1\) on \(\Omega\cup\{\infty\}\), and their Johnson lift is a
spanning linear forest with exactly \(K=\operatorname {Cat}_m\) paths.

#### Proof

The selected turns use every outer-shore colour once by items 1 and 2.
On a marked component, deleting the cyclically alternating marks leaves
even paths, whose residual matching uses every remaining \(A\)- and
\(B\)-occurrence once.  On an unmarked component either phase does the
same.  Hence the diamonds form a perfect matching.

The physical vertex sets belonging to distinct factor components are
disjoint.  Theorem 2.1 and items 4 and 5 show that every local lift is a
linear forest.  The global lift is therefore a linear forest.  It has

\[
 {2m\choose m}\quad\text{vertices},\qquad
 {2m\choose m-1}={2m\choose m}-\operatorname {Cat}_m
 \quad\text{edges}.
 \tag{4.1}
\]

Euler's identity gives exactly \(K\) path components, with isolated
vertices allowed. \(\square\)

This removes factor-component merging, Hamilton voltage, and gluing-tree
topology from the minimal middle-levels-supported implication.

## 5. Exact component catalogue

Fix the two-factor \(F\) and let \({\cal C}(F)\) be its components.  For a
component \(C\), let \(\Sigma_C\) consist of the following local states.

* An unmarked state, with either residual phase and signature
  \((U_\sigma,L_\sigma)=(\varnothing,\varnothing)\).
* Every partially marked, alternating, trace-safe state whose selected turn
  colours are pairwise distinct on each shore.  Its signature is

  \[
  U_\sigma=\{u_i:A_i\text{ is marked}\},\qquad
  L_\sigma=\{\ell_j:B_j\text{ is marked}\}.
  \tag{5.1}
  \]

For central feasibility the two unmarked phases may be quotiented to one
state; retaining the phase bit is useful only for downstream chronology.

### Theorem 5.1 (multiple-choice exact cover)

The fixed factor \(F\) has an admissible componentwise Catalan decoration
if and only if one can choose one state \(\sigma_C\in\Sigma_C\) for every
component such that

\[
 \mathop{\dot\bigcup}_{C\in{\cal C}(F)}U_{\sigma_C}
       ={\Omega\choose m+1},
 \qquad
 \mathop{\dot\bigcup}_{C\in{\cal C}(F)}L_{\sigma_C}
       ={\Omega\choose m-2}.
 \tag{5.2}
\]

Equivalently, the following finite zero-one system is feasible:

\[
 \sum_{\sigma\in\Sigma_C}x_{C,\sigma}=1
 \qquad(C\in{\cal C}(F)),
 \tag{5.3}
\]

\[
 \sum_{C,\sigma:\,u\in U_\sigma}x_{C,\sigma}=1
 \qquad\left(u\in{\Omega\choose m+1}\right),
 \tag{5.4}
\]

\[
 \sum_{C,\sigma:\,\ell\in L_\sigma}x_{C,\sigma}=1
 \qquad\left(\ell\in{\Omega\choose m-2}\right).
 \tag{5.5}
\]

#### Proof

Restricting a global decoration to one component gives a state in
\(\Sigma_C\), and global palette bijectivity is exactly the two disjoint
unions (5.2).  Conversely, the chosen local states are supported on
vertex-disjoint factor components; (5.2) supplies the two global
bijections, while every local residual matching and trace row is already
certified inside \(\Sigma_C\).  Theorem 4.1 applies.  Equations
(5.3)--(5.5) are precisely the incidence formulation of (5.2). \(\square\)

No total-unimodularity claim is made.  The value of the reduction is that
component topology has disappeared: the only coupling is the two exact
palette partitions.

### Corollary 5.2 (exact relational induction with accepting root)

For \({\cal S}\subseteq{\cal C}(F)\), define \({\cal R}({\cal S})\) to be
the set of pairs \((U,L)\) obtained by choosing one local state on every
component of \({\cal S}\), with the chosen upper signatures pairwise
disjoint and the chosen lower signatures pairwise disjoint, and taking
their unions.  For disjoint component sets \({\cal S},{\cal T}\),

\[
 {\cal R}({\cal S}\dot\cup{\cal T})
 =\left\{(U_S\dot\cup U_T,L_S\dot\cup L_T):
 (U_S,L_S)\in{\cal R}({\cal S}),
 (U_T,L_T)\in{\cal R}({\cal T})\right\}.             \tag{5.6}
\]

This join is associative, and the root is accepting exactly when

\[
 \left({\Omega\choose m+1},{\Omega\choose m-2}\right)
       \in{\cal R}({\cal C}(F)).                     \tag{5.7}
\]

Thus any binary decomposition tree of the factor components gives an exact
bottom-up relational induction.  The state in (5.6) is finite but not
claimed to have bounded adhesion or polynomial size.

#### Proof

Equation (5.6) is simply restriction and union of component-local states;
disjointness is the exact no-repeated-colour condition.  Associativity of
disjoint union makes the result independent of the chosen decomposition
tree.  The root condition is exactly (5.2). \(\square\)

## 6. Fixed upper SDR and exact gap Hall

An **upper-turn SDR** is a set \(I\) of \(A\)-occurrences for which

\[
                 A_i\longmapsto u_i
 \tag{6.1}
\]

is a bijection onto \({\Omega\choose m+1}\).  Put
\(I_C=I\cap V(C)\) and \(r_C=|I_C|\).  A component with \(r_C=0\) will be
left wholly unmarked: cyclic last-to-first alternation forbids lower marks
on a component with no upper mark.

For \(r_C>0\), list the selected \(A\)-occurrences cyclically.  Between
each selected \(A_i\) and the next selected \(A_{i'}\), form one oriented
**gap** containing precisely the \(B_j\)-occurrences encountered strictly
after \(A_i\) and strictly before \(A_{i'}\).  The gaps partition the
\(B\)-occurrences of every hit component.  Across all components there are

\[
                         \sum_C r_C=P                         \tag{6.2}
\]

gaps.

When \(r_C=1\), the unique gap is the full cyclic traversal from the one
selected \(A\)-occurrence back to itself and contains every \(B\)-occurrence
of \(C\).

Let \({\cal H}_I\) be the bipartite graph whose left vertices are these
gap occurrences and whose right vertices are the lower colours
\({\Omega\choose m-2}\).  Join a gap \(g\) to \(\ell\) if some
\(B_j\in g\) has \(\ell_j=\ell\).

### Theorem 6.1 (gap-Hall equivalence)

The fixed upper SDR \(I\) extends to globally bijective lower marks which
alternate componentwise with \(I\) if and only if \({\cal H}_I\) has a
perfect matching.  Equivalently,

\[
                         |N(S)|\ge |S|
 \qquad\text{for every set }S\text{ of gaps}.          \tag{6.3}
\]

#### Proof

Between two consecutive selected \(A\)-occurrences, alternation requires
exactly one selected \(B\)-occurrence: zero would make consecutive marked
shores both \(A\), and two would create consecutive selected shores both
\(B\).  Hence any extension chooses one lower colour from every gap, with
all lower colours distinct and complete.  This is a perfect matching of
\({\cal H}_I\).

Conversely, for every matched gap-colour edge choose one witnessing
\(B_j\) in that gap.  Distinct gaps are disjoint and the matching uses each
lower colour once.  The resulting cyclic marked order is
\(A,B,A,B,\ldots\) on every hit component; components missed by \(I\) are
unmarked.  Thus the extension is exact.  Hall's theorem gives (6.3).
\(\square\)

Theorem 6.1 handles palette and residual-matching legality.  The local
trace condition must still be imposed unless the following parity row is
available.

### Corollary 6.2 (block-diagonal palette ownership)

Suppose the two global turn palettes are partitioned into banks
\((U_C,L_C)\) indexed by the factor components, with
\(|U_C|=|L_C|=r_C\).  Banks are both empty on components intended to remain
unmarked.  On each nonempty component choose an upper occurrence SDR for
\(U_C\), and form its local gap graph against only \(L_C\).  If every one
of these local graphs has a perfect matching, the union of their matchings
is exactly one global componentwise alternating two-palette decoration.
If in addition every component is trace-safe, Theorem 4.1 applies.

This is Theorem 6.1 after the right palette has been allocated in advance:
the global Hall graph becomes a disjoint union of component-local Hall
instances.  It is a sufficient design theorem, not a claim that one may
preassign the banks without loss of generality.

## 7. Positive odd residuals make trace safety automatic

For a component with \(q_C\) occurrences on each shore, put

\[
                          z_C=q_C-r_C.                 \tag{7.1}
\]

### Theorem 7.1 (odd-residual sufficient theorem)

Suppose \(I\) is an upper-turn SDR, \({\cal H}_I\) has a perfect matching,
and

\[
              z_C>0\text{ and }z_C\text{ is odd}
 \qquad\text{for every component with }r_C>0.          \tag{7.2}
\]

Then every lower extension supplied by Theorem 6.1 is trace-safe.
Consequently it gives a Catalan linear matching.

#### Proof

On a hit component the extension has \(r_C\) selected occurrences on each
shore, hence \(2r_C\) ones and \(2z_C\) zeroes.  Condition \(z_C>0\)
excludes the wholly marked face.

If the mixed cycle condition (2.1) held, every zero-run would have length
two, so there would be exactly \(z_C\) zero-runs and hence exactly \(z_C\)
one-runs.  Every one-run would be odd.  Their total length would therefore
have the parity of \(z_C\), namely odd, but their total length is
\(2r_C\), which is even.  This contradiction excludes (2.1).  Theorem 4.1
finishes the proof. \(\square\)

This criterion is sufficient, not necessary.  When \(z_C\) is even, a
long zero-run or an even one-run may still make the component safe.

### Corollary 7.2 (path budget and component bound)

For every admissibly decorated factor, the physical lift contributed by
component \(C\) consists of exactly \(z_C=q_C-r_C\) paths, where
\(r_C=0\) on an unmarked component.  Therefore

\[
                    \sum_C z_C=Q-P=K,
 \qquad
                    |{\cal C}(F)|\le K.               \tag{7.3}
\]

#### Proof

The local lift has \(2q_C\) vertices.  It has \(2r_C\) selected turn edges
and \(q_C-r_C=z_C\) residual cross edges, for a total of \(q_C+r_C\)
edges.  Since it is a forest, its component count is
\(2q_C-(q_C+r_C)=z_C\).  Every marked component has \(z_C\ge1\) by the
all-marked exclusion, and every unmarked component has
\(z_C=q_C\ge1\).  Summing gives (7.3). \(\square\)

## 8. Exact factor-extension flow

Let \({\cal M}\) be any perfect matching of the Boolean diamond graph.  Its
**forced middle-levels support** \(\Theta({\cal M})\) is the following
simple subgraph of \({\rm ML}(2m-1)\).

* A cross diamond contributes its one middle-levels edge.
* A same-\(B\)-rail diamond contributes the two edges of its length-two
  middle-levels path through its unique \(A\)-centre.
* A same-\(A\)-rail diamond contributes the two edges of its length-two
  path through its unique \(B\)-centre.

If two selected turns share a factor edge, that edge occurs only once in
\(\Theta\).

### Theorem 8.1 (factor-resolvability is a bipartite flow gate)

The matching \({\cal M}\) has a componentwise decorated spanning-two-factor
representation if and only if \(\Theta({\cal M})\) is contained in a
spanning two-factor of \({\rm ML}(2m-1)\).

Put \(G={\rm ML}(2m-1)\), with bipartition \((\mathcal A,\mathcal B)\), and
assume first that

\[
                     \deg_\Theta(v)\le2\quad(v\in V(G)).        \tag{8.1}
\]

Let

\[
 G'=G-E(\Theta),\qquad b(v)=2-\deg_\Theta(v).                    \tag{8.2}
\]

Then such a spanning two-factor exists if and only if, for every
\(X\subseteq\mathcal A\) and \(Y\subseteq\mathcal B\),

\[
 e_{G'}(X,\mathcal B\setminus Y)+b(Y)\ge b(X).                  \tag{8.3}
\]

When it exists, the completion is integral.  If the physical lift of
\({\cal M}\) is already a forest, every resulting representation satisfies
the corrected componentwise trace conditions automatically.

#### Proof

In any supported representation, every cross diamond is a literal factor
edge and every same-rail diamond is the shortcut of the displayed
length-two factor path, so \(\Theta\) is contained in the factor.

Conversely, suppose a spanning two-factor contains \(\Theta\).  Mark the
centre of every same-rail diamond.  Perfectness of \({\cal M}\) implies
that every unmarked \(A\)- and \(B\)-occurrence belongs to exactly one
cross diamond; these cross edges form a perfect matching of the unmarked
occurrences and lie in \(\Theta\).  The same perfectness makes the
same-\(B\)-rail turns biject all upper colours avoiding \(\infty\), and the
same-\(A\)-rail turns biject all lower colours containing \(\infty\).  On
each factor component the residual matching forces the selected shore types
to alternate cyclically.  Thus the factor and its marks reproduce
\({\cal M}\).

It remains to characterize completion of \(\Theta\).  Select edges
\(H\subseteq E(G')\) with

\[
                         \deg_H(v)=b(v).                         \tag{8.4}
\]

Then \(E(\Theta)\dot\cup H\) is exactly the desired spanning two-factor.
The two total demands agree automatically, since every edge of \(\Theta\)
has one endpoint on each shore.  Build the standard flow network with
source arcs of capacity \(b(a)\) to \(a\in\mathcal A\), unit arcs for
edges of \(G'\), and arcs of capacity \(b(b)\) from
\(b\in\mathcal B\) to the sink.  For a cut whose source side contains
\(X\subseteq\mathcal A\) and \(Y\subseteq\mathcal B\), the max-flow cut
inequality reduces exactly to (8.3).  Max-flow/min-cut proves necessity and
sufficiency, and integral capacities give an integral completion.

Finally, the physical lift reconstructed from the factor is the original
lift of \({\cal M}\).  If it is a forest, Theorem 2.1 rules out both a
wholly marked component and the mixed cycle face. \(\square\)

This replaces the Hamilton-extension/subtour gate by an exact polynomial
cut system.  It does not assert that every Catalan linear matching is
factor-resolvable; the cuts (8.1)--(8.3) can fail.

## 9. The factor-resolvable class is strictly broader than the Hamilton-resolvable class

The two-cycle factor from Section 3 also gives an explicit strictness
witness.  On component \(C=(A_i,B_i)\), select

\[
 I_C=\{0,2\},\qquad J_C=\{0,3\};                                  \tag{9.1}
\]

on component \(C'=(D_i,E_i)\), select

\[
 I_{C'}=J_{C'}=\{0,3,4\}.                                        \tag{9.2}
\]

The upper palettes are complementary banks of sizes two and three, and so
are the lower palettes.  Directly, the two cyclic traces are

\[
 \begin{array}{c|c|c}
 &\text{selected upper labels (missing element)}
 &\text{selected lower singleton labels}\\ \hline
 C&\{3,0\}&\{1,4\}\\
 C'&\{1,2,4\}&\{0,2,3\}.
 \end{array}                                                     \tag{9.3}
\]

Indeed \(u_i=\Omega\setminus\{i+3\}\),
\(\ell_i=\{i+1\}\), while
\(u'_i=\Omega\setminus\{2i+1\}\) and
\(\ell'_i=\{2i+2\}\).  The two cyclic traces are

```text
1100100100
1100001111
```

The first is safe because it has an even one-run; the second is safe because
it has a zero-run of length four.  Hence this is an admissible decorated
two-factor and its lift is a five-path Catalan linear matching.

Nevertheless \(\Theta({\cal M})\) contains every edge of the first factor
component \(C\): its four turn centres supply the edges incident with a
mark, and its three residual two-zero gaps supply the remaining three
factor edges.  Every vertex of \(C\) is therefore already saturated to
degree two inside \(\Theta\).  Any spanning two-factor containing
\(\Theta\) retains \(C\) as a separate component.  No Hamilton cycle can
support this same diamond matching.

Thus factor-resolvable matchings genuinely extend Hamilton-resolvable ones
at the object level.  This does not by itself separate the corresponding
all-dimension existential statements.

## 10. Alternating-circuit reachability and exact scope

Any two spanning two-factors of the same graph have a balanced red-blue
symmetric difference.  Pairing red and blue half-edges decomposes it into
edge-disjoint alternating closed trails.  In the bipartite middle-levels
graph, repeated vertices split these trails into simple alternating even
cycles.  Toggling them successively preserves degree two.  Hence the
existence of a packet from any starting factor to an accepting decorated
factor is equivalent to existence of the accepting factor itself; no
component-merging condition is hidden.

The positive \({\rm ML}(7)\) incidence-hex theorem belongs to a stronger
recursive lane.  For one fixed decoration, a hex transfer is transparent
exactly when the selected local turn-colour multisets agree separately on
the two shores and the retained-fragment boundary mark types alternate
after reconnection.  Its frozen census has 31 alternating hexes, 16
Hamilton outputs, 10 decorable outputs, and 6 outputs sharing a forest
decoration with the source.  This proves that joint transparent transfer is
available, but it is not a hypothesis of Theorems 4.1--8.1.

The hierarchy is therefore

\[
 \text{joint alternating SDR + transparent gluing tree}
 \Longrightarrow
 \text{decorated Hamilton cycle}
 \Longrightarrow
 \text{corrected componentwise decorated two-factor}.
 \tag{10.1}
\]

Separate upper and lower rainbows do not supply either the gap matching or
the correlated trace state.  In the factor-level induction, the exact joint
object is the relation \({\cal R}\) of Corollary 5.2, not two independent
palette flags.

The phrase “weakest target” is scoped to the middle-levels-supported,
factor-resolvable architecture.  An arbitrary Catalan linear diamond
matching need not be supported by any chosen middle-levels two-factor.

Finally, none of the results above supplies strict coordinate residence,
all deeper upper/lower shadows, connector or voltage state, or an integral
common-cap compiler.  Those remain separate requirements for
\(\nu(k)=B(k)\).
