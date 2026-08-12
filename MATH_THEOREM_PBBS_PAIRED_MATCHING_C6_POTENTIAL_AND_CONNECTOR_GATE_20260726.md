# PBBS paired matchings: a statewise \(C_6\) potential, loose-triangle fusion, and the parity bridge

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Put

\[
 n=2m+1,\qquad {\cal X}=\binom{[n]}m,\qquad
 {\cal U}=\binom{[n]}{m+1},\qquad
 {\cal L}=\binom{[n]}{m-1},
\]

\[
 W=|{\cal X}|=|{\cal U}|,\qquad
 N=|{\cal L}|={m\over m+2}W,\qquad
 D=W-N={2W\over m+2},\qquad
 B={W\over2m+1}=\operatorname {Cat}_m.                       \tag{0.1}
\]

The canonical PBBS permutation \(f\) is a valid and particularly strong
initial state for the paired-matching problem.

* It gives two edge-disjoint perfect matchings of the middle-level
  incidence graph:

  \[
  M_0(X^c)=f^{-1}(X),\qquad M_1(X^c)=f(X).                    \tag{0.2}
  \]

* Their projected Johnson \(2\)-factor uses every upper color exactly
  once and every lower color at least once.  The lower multiplicities are
  \(1,2,\) or \(3\).
* Its monodromy is \(f^{-2}\), so it has at most \(B\) components.

Thus both color shores are already solved exactly; only Hamiltonicity is
missing.

For a general paired state \(F=M_0\cup M_1\), let

\[
 h(F)=\#\{\text{missing lower colors}\},\qquad
 c(F)=\#\{\text{monodromy cycles}\}.
\]

Every legal alternating switch of \(M_1\) preserves the complete upper
ledger.  A component-transversal alternating \(C_6\) merges three
components into one and changes at most three lower occurrences.  A
Hamilton-safe alternating \(C_8\) can merge two components and changes at
most four lower occurrences.  Consequently

\[
 \boxed{\mathcal P(F)=h(F)+5(c(F)-1)}                         \tag{0.3}
\]

is a strict statewise potential for both moves:

\[
 \Delta\mathcal P\le-7\quad(C_6\text{ three-way merge}),\qquad
 \Delta\mathcal P\le-1\quad(C_8\text{ two-way merge}).        \tag{0.4}
\]

This gives an exact conditional asymptotic construction.

> If the PBBS paired factor has a physically disjoint loose forest of
> legal component-transversal \(C_6\)'s joining all components down to
> one or two, and in the two-component case one legal Hamilton-safe
> \(C_8\), then the resulting Hamilton Johnson cycle has every upper
> union exactly once and misses only \(O(B)=o(W)\) lower intersections.

The \(C_6\)-only route has an unavoidable parity restriction:

\[
                         c(F)\pmod2\quad\text{is invariant}.  \tag{0.5}
\]

For PBBS,

\[
                         c(F_{\rm PBBS})\equiv B\pmod2.       \tag{0.6}
\]

Hence an all-\(C_6\) construction can end in one component only when the
Catalan number \(B\) is odd, equivalently \(m=2^a-1\).  In all other
dimensions a \(C_8\) or another even-length alternating circuit is
mathematically necessary.

The existing switch libraries do not yet prove the required connector
atlas.  The MNW loose \(\alpha\)-tree is certified for its own path-factor
components, not for the natural PBBS matchings (0.2).  The large PBBS clean
\(C_8\) reservoir is certified in the odd-graph factor, not as directed
\(4\)-cycles of the paired-matching exchange digraph.  Transferring either
library requires a new topology-identification theorem.

## 1. PBBS as an exact paired-matching state

Let \(f\) be the canonical PBBS permutation of \({\cal X}\).  Its directed
arcs are odd-graph edges:

\[
                              X\cap f(X)=\varnothing.          \tag{1.1}
\]

Every PBBS orbit has length \(\ell n\) for an integer \(\ell\ge1\), and
the orbit levels satisfy

\[
                              \sum_{\text{orbits}}\ell=B.     \tag{1.2}
\]

For \(X\in{\cal X}\), write \(U_X=X^c\in{\cal U}\), and define (0.2).

### Theorem 1.1 (natural PBBS paired matchings)

The maps in (0.2) are edge-disjoint perfect matchings between
\({\cal U}\) and \({\cal X}\).  Their projected Johnson edge at \(U_X\)
is

\[
                         e_X=\{f^{-1}(X),f(X)\}.               \tag{1.3}
\]

It has upper color

\[
                         f^{-1}(X)\cup f(X)=X^c=U_X           \tag{1.4}
\]

and lower color

\[
                         \chi(X)=f^{-1}(X)\cap f(X).          \tag{1.5}
\]

The upper colors are therefore all distinct, while the PBBS angle theorem
gives

\[
                  1\le|\{X:\chi(X)=L\}|\le3
                                    \quad(L\in{\cal L}).       \tag{1.6}
\]

#### Proof

As \(X\) varies, both \(f^{-1}(X)\) and \(f(X)\) vary bijectively over
\({\cal X}\).  Equation (1.1), applied in both time directions, puts them
inside \(X^c=U_X\), so they are incidence matchings.  They are distinct:
equality would give \(f^2(X)=X\), whereas every PBBS orbit has length at
least \(n\ge5\).

Two distinct \(m\)-subsets of the \((m+1)\)-set \(X^c\) have union
\(X^c\) and intersection of size \(m-1\), proving (1.3)--(1.5).
Equation (1.6) is precisely the audited PBBS depth-one angle theorem.
\(\square\)

Thus PBBS starts with

\[
                         h(F_{\rm PBBS})=0,\qquad
                         M^+(F_{\rm PBBS})=0.                 \tag{1.7}
\]

## 2. PBBS monodromy, component count, and parity

Let \(f_i:{\cal U}\to{\cal X}\) denote the two matching bijections.  The
paired monodromy is

\[
                              \sigma=f_1^{-1}f_0.              \tag{2.1}
\]

### Theorem 2.1 (PBBS monodromy)

\[
                         \sigma(U_X)=U_{f^{-2}(X)}.            \tag{2.2}
\]

An \(f\)-orbit of length \(\ell n\) contributes

\[
                         \gcd(2,\ell n)=\gcd(2,\ell)           \tag{2.3}
\]

cycles to \(\sigma\).  Consequently

\[
                         c(F_{\rm PBBS})
                           =\sum_{\text{orbits}}\gcd(2,\ell)
                           \le B,                              \tag{2.4}
\]

and

\[
                         c(F_{\rm PBBS})\equiv B\pmod2.       \tag{2.5}
\]

#### Proof

For \(Y\in{\cal X}\),

\[
                         f_1^{-1}(Y)=U_{f^{-1}(Y)}.
\]

Substitute \(Y=f^{-1}(X)=f_0(U_X)\) to obtain (2.2).  The number of
cycles of the step-two map on a cyclic orbit of length \(\ell n\) is its
greatest common divisor with two.  Since \(n\) is odd, this is (2.3).
Sum over orbits and use (1.2).  Finally
\(\gcd(2,\ell)\equiv\ell\pmod2\), giving (2.5). \(\square\)

The classical Catalan parity criterion says

\[
                         B\text{ is odd}
                 \quad\Longleftrightarrow\quad m=2^a-1.      \tag{2.6}
\]

## 3. Scalar repeat capacity is not the obstruction

Let \(a_j\) be the number of lower colors of PBBS multiplicity \(j\),
\(j=1,2,3\).  Equations (1.6) and total mass give

\[
 a_1+a_2+a_3=N,\qquad a_1+2a_2+3a_3=W,
\]

so

\[
                              a_2+2a_3=D.                     \tag{3.1}
\]

The number of upper vertices \(U_X\) whose current lower color occurs at
least twice is

\[
 2a_2+3a_3=2D-a_3\ge {3D\over2}.                             \tag{3.2}
\]

Since

\[
                         {D\over B}={2(2m+1)\over m+2}
                                   =4-{6\over m+2},            \tag{3.3}
\]

PBBS initially has at least \((6-o(1))B\) removable occurrences whose
individual removal does not create a lower hole.  A complete three-way
fusion needs at most \(3B/2\) negative occurrences.  Hence scalar repeat
capacity is more than sufficient.

This does not prove that safe occurrences assemble into legal
component-transversal alternating cycles.  It separates the remaining
topological incidence problem from a nonexistent repeat shortage.

## 4. Legal alternating circuits

Fix any edge-disjoint paired state \(M_0,M_1\) and use the legal exchange
digraph from the paired-matching theorem:

\[
 V\longrightarrow U
\quad\Longleftrightarrow\quad
 f_1(V)\subset U,\quad V\ne U,\quad f_1(V)\ne f_0(U).          \tag{4.1}
\]

It is \((m-1)\)-in/out-regular and has no directed \(2\)-cycles.  A
directed \(r\)-cycle

\[
                         U_0\to U_1\to\cdots
                              \to U_{r-1}\to U_0              \tag{4.2}
\]

replaces \(M_1\) by

\[
                         f_1'(U_i)=f_1(U_{i-1}).               \tag{4.3}
\]

With

\[
 \tau=(U_0\,U_1\,\cdots\,U_{r-1}),\qquad
 \sigma=f_1^{-1}f_0,
\]

the exact derivatives are

\[
                              \sigma'=\tau\sigma,              \tag{4.4}
\]

\[
 \ell'-\ell
 =\sum_{i=0}^{r-1}
   \left(
    e_{\,f_0(U_i)\cap f_1(U_{i-1})}
    -e_{\,f_0(U_i)\cap f_1(U_i)}
   \right).                                                   \tag{4.5}
\]

Every such switch keeps both shores perfectly matched.  Therefore

\[
                              M^+(F')=M^+(F)=0,                \tag{4.6}
\]

while

\[
                              h(F')-h(F)\le r.                 \tag{4.7}
\]

The inequality is statewise: only the \(r\) removed lower occurrences can
create new holes.

For the PBBS state, (4.1) has a direct center form.  On writing
\(V=U_Z\) and \(U=U_X\), it becomes

\[
 Z\longrightarrow X
\quad\Longleftrightarrow\quad
 f(Z)\cap X=\varnothing,\quad X\notin\{Z,f^2(Z)\}.             \tag{4.8}
\]

Thus the PBBS exchange digraph is the odd-graph neighborhood of \(f(Z)\)
with its two PBBS orbit neighbors deleted.  Formula (4.8) is the exact
test which any proposed PBBS \(\alpha\)- or clean-cycle atlas must pass.

## 5. Component calculus for a legal \(C_6\)

Take \(r=3\), so \(\tau=(U_0\,U_1\,U_2)\).  The change in the number of
cycles of \(\sigma\) depends only on how these three vertices lie in the
old monodromy cycles.

### Theorem 5.1 (three-cycle component law)

1. If \(U_0,U_1,U_2\) lie in three distinct \(\sigma\)-cycles, then

   \[
                              c(\tau\sigma)=c(\sigma)-2.       \tag{5.1}
   \]

2. If they lie in exactly two \(\sigma\)-cycles, then

   \[
                              c(\tau\sigma)=c(\sigma).         \tag{5.2}
   \]

3. If they lie in one \(\sigma\)-cycle, then the component count is
   unchanged when their cyclic order agrees with \(\tau\), and increases
   by two in the opposite cyclic order.

#### Proof

Cut the arcs of \(\sigma\) entering the three marked vertices.  This
creates one path segment per marked point inside each touched cycle.
Left multiplication by \(\tau\) reconnects the three incoming arcs
cyclically.  Three old cycles are joined into one in Case 1.  In Case 2,
one old cycle is cut into two segments and the other into one; cyclic
reconnection again gives two cycles.  In Case 3, the three segments are
rejoined into one or separately closed according to the two cyclic
orders. \(\square\)

In particular every \(C_6\) switch preserves \(c(F)\pmod2\).  This also
follows from the fact that a \(3\)-cycle is even.

### Corollary 5.2 (statewise three-way potential descent)

If a legal \(C_6\) meets three distinct components, then

\[
 \Delta\mathcal P
 =\Delta h+5\Delta c
 \le3-10=-7.                                                \tag{5.3}
\]

If it lies in one component in the Hamilton-safe orientation and strictly
decreases \(h\), then it also strictly decreases \(\mathcal P\).

If the three old lower colors are distinct and each retains another
occurrence after their removal, then the three-way merge preserves exact
lower completeness.

## 6. Loose triangle forests

Let the vertices of \({\cal A}(F)\) be the components of the current
paired factor.  A hyperedge \(\{C_1,C_2,C_3\}\) is a **physical connector
triangle** when there is a legal directed triangle in (4.1) using one
upper vertex from each \(C_i\).

A family of such triangles is called physically disjoint when their six
incidence edges, and in particular their three upper supports, are
vertex-disjoint in the middle-level graph.  This ensures that all switches
remain alternating after any earlier member of the family is toggled.

### Theorem 6.1 (loose-forest fusion)

Suppose \({\cal A}(F)\) contains a physically disjoint loose hyperforest
whose connected blocks contain all \(c=c(F)\) original factor components.
Let the hyperforest have \(q\) connected blocks.  Then its triangles can
be ordered so that every switch meets three distinct current components.
After all switches,

\[
                         c(F')=q,\qquad
                         h(F')\le h(F)+{3(c-q)\over2}.          \tag{6.1}
\]

Every upper color still occurs exactly once.

#### Proof

In a loose \(3\)-uniform tree, the first hyperedge contains three vertices
and every later hyperedge meets the preceding union in one vertex and
introduces two new vertices.  Order each tree from its root edge outward.
At the time an edge is used, its old vertex belongs to the already fused
component and its two new vertices belong to two untouched components.
Physical disjointness leaves its alternating incidences unchanged.
Theorem 5.1 therefore merges those three current components.

A loose tree on \(s\) vertices has \((s-1)/2\) hyperedges.  Summing over
the \(q\) blocks gives \((c-q)/2\) switches.  Equation (4.7) now yields
(6.1), and (4.6) gives the upper statement. \(\square\)

Thus a spanning loose tree, possible only for odd \(c\), gives one
component and at most \(3(c-1)/2\) new lower holes.  For even \(c\), a
two-block spanning loose forest leaves two components and at most
\(3(c-2)/2\) new holes.

## 7. The parity-changing \(C_8\) bridge

Take \(r=4\) in Section 4.  The monodromy multiplier \(\tau\) is a
\(4\)-cycle and is odd, so it can change the parity of \(c(F)\).

### Theorem 7.1 (exact parity bridge)

Suppose a legal directed \(4\)-cycle satisfies

\[
                         c(\tau\sigma)=c(\sigma)-1.            \tag{7.1}
\]

Then

\[
                         \Delta\mathcal P
 \le4-5=-1.                                                   \tag{7.2}
\]

In particular, if \(F\) has two components and \(\tau\sigma\) is one
cycle, the switch is a Hamiltonizing bridge.  It preserves every upper
color and creates at most four lower holes.

#### Proof

Equations (4.6)--(4.7) apply with \(r=4\), while (7.1) gives
\(\Delta c=-1\).  Substitute into (0.3). \(\square\)

There are useful literal sufficient orders for (7.1).

* If one marked vertex \(a\) lies in one \(\sigma\)-cycle, the other
  three \(b,c,d\) lie in the second in cyclic order \(b,c,d\), then
  \(\tau=(a\,b\,c\,d)\) joins the two cycles.
* If \(a,c\) lie in one cycle in cyclic order and \(b,d\) lie in the
  other in cyclic order, the alternating multiplier
  \(\tau=(a\,b\,c\,d)\) again joins them.

Both statements follow by cutting the incoming arcs at the four marked
vertices and tracing the reconnected segments.

## 8. Conditional asymptotic Hamilton theorem

### PBBS connector-atlas hypothesis

For the natural PBBS pair (0.2), require:

1. if \(c\) is odd, a physically disjoint spanning loose tree of legal
   component-transversal directed triangles;
2. if \(c\) is even, a physically disjoint two-block spanning loose
   triangle forest, followed by one legal directed \(4\)-cycle satisfying
   Theorem 7.1 and disjoint from the triangle supports.

### Theorem 8.1 (connector atlas implies asymptotic double rainbow)

Under the PBBS connector-atlas hypothesis, there is a Hamilton cycle of
\(J(2m+1,m)\) for which

\[
                         M^+=0,\qquad
                         M^-\le {3B\over2}+4=o(W).             \tag{8.1}
\]

If every connector removes only lower occurrences which retain another
copy, then \(M^-=0\) as well.

#### Proof

Start from Theorems 1.1--2.1.  If \(c\) is odd, apply Theorem 6.1 with
\(q=1\).  If \(c\) is even, apply it with \(q=2\) and then Theorem 7.1.
There are at most \(B\) initial components, so (6.1) and the four-hole
bridge bound give (8.1).  Every state remains a pair of perfect matchings,
and the final monodromy is one cycle, so Theorem 1.1 of the paired-matching
normal form gives a Johnson Hamilton cycle with exact upper rainbowness.
\(\square\)

This is already coefficient-one at depth one: the defect is Catalan-scale,
not merely \(o(W)\).

## 9. Audit of the existing switch libraries

Two tempting imports must be kept separate.

### 9.1 MNW \(\alpha\)-switches

The MNW \(\alpha\)-support hypergraph has a loose spanning tree and its
alternating \(6\)-cycles are designed to merge three factor components.
However the existing theorem is stated for the MW/MSW path-factor
components.  No audited identity currently identifies those component
vertices with the \(f^{-2}\)-orbits in Theorem 2.1, or verifies that every
negative \(\alpha\)-edge satisfies the PBBS exchange test (4.8).

Therefore the known loose tree does not yet prove the PBBS connector-atlas
hypothesis.  The exact missing transfer is:

\[
 \boxed{
 \begin{array}{c}
 \text{map every selected MNW }\alpha\text{ triangle to a directed}\\
 \text{triangle of (4.8), with its three negative incidences lying}\\
 \text{in the prescribed distinct }f^{-2}\text{-components.}
 \end{array}}                                                \tag{9.1}
\]

Physical disjointness, or a dynamic alternation proof, must also be retained
along the loose-tree order.

### 9.2 The PBBS clean-\(C_8\) reservoir

The proved PBBS reservoir contains

\[
 n(\operatorname {Cat}_{m-1}-2^{m-2})
       =\left({1\over4}-o(1)\right)W
\]

clean alternating \(C_8\)'s in the initial **odd-graph** PBBS factor, with
a vertex-disjoint subfamily of order \(B\).  This does not automatically
give a directed \(4\)-cycle of (4.1).  A centered Johnson edge
\(\{f^{-1}(X),f(X)\}\) depends on both odd-factor neighbors of \(X\);
toggling one odd-factor \(C_8\) changes the centered edges at all touched
vertices.  Its monodromy derivative need not be one \(4\)-cycle.

Thus the exact parity-transfer lemma still missing is:

\[
 \boxed{
 \text{some clean PBBS }C_8\text{ induces a legal paired switch with }
 c(\sigma')=c(\sigma)-1.}                                   \tag{9.2}
\]

The large raw reservoir proves supply, not the topology sign in (9.2).

## 10. Proved boundary

The following statements are now unconditional.

1. PBBS is a valid paired-matching initial state with both color shores
   complete and at most \(B=o(W)\) components.
2. The potential (0.3) is a strict statewise descent for every legal
   three-component \(C_6\) merge and every legal two-component \(C_8\)
   merge.
3. A loose triangle atlas plus one parity bridge gives a Hamilton cycle
   with \(O(B)=o(W)\) lower defects and no upper defects.
4. \(C_6\)-only descent has the parity obstruction (0.5)--(0.6).
5. PBBS has ample scalar repeated-color capacity; only its placement in
   component-transversal legal circuits remains unresolved.

Accordingly the next finite theorem is not another marginal descent
estimate.  It is the topology-identification statement (9.1), followed in
even Catalan parity by the single bridge statement (9.2).
