# Alternating \(C_6/C_8\) splices, strand permutations, and the exact parity gate

Date: 2026-07-26

Let \(J\) have size \(2r\), and let

\[
 \mathcal X=\binom Jr,\qquad
 \mathcal Y=\binom J{r+1},\qquad
 M(J)=(\mathcal X,\mathcal Y;\subset).
\]

Let \(F\) be a spanning simple \(b\)-factor with degree one at
\(\mathcal D_r\cup\overline{\mathcal D_r}\) and degree two elsewhere,
and assume initially that \(F\) is a path cover.  Write

\[
 \pi_F:\mathcal D_r\longrightarrow\mathcal D_r
\]

for its endpoint monodromy: the path beginning at \(P\) ends at
\(\overline{\pi_F(P)}\).

The preceding four-cycle lane is empty because \(M(J)\) is \(C_4\)-free.
This note gives the exact successor.

1. Every \(C_6\) is a three-petal star.  Every \(C_8\) is either a
   four-petal star or an octahedral square.
2. There is an exact strand-diagram test for any alternating switch,
   including switches which cut one old path more than once.
3. A clean \(C_6\) on three distinct coherently oriented paths acts by a
   \(3\)-cycle.  A clean \(C_8\) on four such paths acts by a \(4\)-cycle.
4. The slogan “\(C_6\) only generates \(A_N\)” is false without the
   distinct-strand hypothesis: a folded \(C_6\) can act as a transposition.
5. A concrete \(r=3\) star \(C_8\) changes endpoint parity while leaving
   every root-incident first edge fixed.
6. Two explicit geometric gates suffice for arbitrary monodromy correction:
   connected clean \(C_6\) support plus one clean \(C_8\), or a connected
   graph of folded-\(C_6\) transposition routers.

All statements below are local graph theorems.  They do not assert that the
canonical Chung--Feller factor contains the required growing router atlas.

## 1. Set classification of \(C_6\) and \(C_8\)

Write a simple cycle as

\[
 X_0-Y_0-X_1-Y_1-\cdots-X_{k-1}-Y_{k-1}-X_0,           \tag{1.1}
\]

where \(Y_i=X_i\cup X_{i+1}\), with indices modulo \(k\).

### Theorem 1.1 (all six-cycles)

Every simple \(C_6\) has the form

\[
\begin{aligned}
 K a&\subset K a b\supset K b
     \subset K b c\supset K c
     \subset K c a\supset K a,                         \tag{1.2}
\end{aligned}
\]

where \(|K|=r-1\) and \(a,b,c\notin K\) are distinct.  Conversely (1.2)
is always a \(C_6\).

#### Proof

The three lower vertices are distinct and pairwise adjacent in the Johnson
graph.  A pairwise adjacent triple of \(r\)-sets either has a common
\((r-1)\)-core, or lies in one common \((r+1)\)-set.  In the second case
all three upper unions in (1.1) are the same vertex, contradicting
simplicity.  The first case is exactly (1.2). \(\square\)

### Theorem 1.2 (all eight-cycles)

Every simple \(C_8\), after cyclic relabelling, is exactly one of the
following two types.

**Star type.**  For an \((r-1)\)-set \(K\) and distinct \(a,b,c,d\notin K\),

\[
 K a,\ K b,\ K c,\ K d,                                \tag{1.3}
\]

with successive upper vertices

\[
 K a b,\ K b c,\ K c d,\ K d a.                        \tag{1.4}
\]

**Octahedral-square type.**  For an \((r-2)\)-set \(K\) and distinct
\(a,b,c,d\notin K\),

\[
 K a b,\ K b c,\ K c d,\ K d a,                        \tag{1.5}
\]

with successive upper vertices

\[
 K a b c,\ K b c d,\ K a c d,\ K a b d.                \tag{1.6}
\]

Conversely, both displays give simple \(C_8\)'s whenever the indicated
sets exist.

#### Proof

Consider the opposite lower vertices \(X_0,X_2\).  Their Johnson distance
is one or two.

If it is two, put \(K=X_0\cap X_2\), so \(|K|=r-2\), and write the two
two-element differences as \(\{a,b\}\) and \(\{c,d\}\).  The common
neighbours \(X_1,X_3\) select one element from each difference.  If they
share either selection, two consecutive upper unions coincide.  Therefore
they use opposite selections, giving (1.5)--(1.6).

If the distance is one, write \(X_0=K a\), \(X_2=K c\) with
\(|K|=r-1\).  A common Johnson neighbour of \(X_0,X_2\) is either of
star form \(Kx\), or is an \(r\)-subset of \(Kac\).  Any neighbour of the
second kind has union \(Kac\) with both \(X_0\) and \(X_2\), so it repeats
an upper vertex of the incidence cycle.  Thus both \(X_1,X_3\) are of
star form.  Simplicity makes their new elements distinct from each other
and from \(a,c\), giving (1.3)--(1.4). \(\square\)

The octahedral \(C_8\) is the set geometry underlying the known two-row,
two-cut rectangle.  The star \(C_8\) is a genuinely different geometry.

## 2. The exact strand diagram

Assume (1.1) is \(F\)-alternating, with

\[
 A=\{X_iY_i:0\le i<k\}\subseteq F,\qquad
 B=\{Y_iX_{i+1}:0\le i<k\}\cap F=\varnothing.           \tag{2.1}
\]

The toggled factor is

\[
                         F'=F-A+B.                      \tag{2.2}
\]

Delete \(A\) from the old path cover.  Its components are path segments.
Each segment has two terminals, each terminal being either one of the
\(2k\) exposed cycle vertices or one of the \(2N\) global endpoints.
Let \(\mathscr S_F(C)\) be this terminal-pairing diagram.

### Theorem 2.1 (necessary and sufficient strand test)

The toggle (2.2) is again a root-to-sink path cover if and only if, after
the new pairs \(B\) are added to \(\mathscr S_F(C)\),

1. no component contains zero global endpoints; and
2. every component contains exactly two global endpoints, one in
   \(\mathcal D_r\) and one in \(\overline{\mathcal D_r}\).

When these conditions hold, the pairs of global endpoints in the resulting
components are exactly the new monodromy \(\pi_{F'}\).

#### Proof

Every nonterminal vertex still has degree two and every global endpoint
still has degree one.  Hence every component after the toggle is a path or
a cycle.  A component with no global endpoint is a cycle; a component with
two sources or two sinks violates the prescribed endpoint type.  Conversely
the two stated conditions make every component one root-to-sink path.
Contracting the unchanged path segments proves the final assertion.
\(\square\)

This finite pairing diagram is the complete classification when two or
more selected cycle edges lie on one old path.  Cycle length alone does not
determine the endpoint permutation.

## 3. Clean distinct-strand switches

Orient every old path from its Dyck root to its barred endpoint.  For a
selected edge \(e_i=X_iY_i\), put

\[
 \epsilon_i=
 \begin{cases}
 +,&\text{the path traverses }X_i\to Y_i,\\
 -,&\text{the path traverses }Y_i\to X_i.
 \end{cases}                                             \tag{3.1}
\]

Call the switch **clean** when its \(k\) selected edges lie on \(k\)
distinct path components.

### Theorem 3.1 (clean splice theorem)

For a clean alternating \(C_{2k}\), the toggle is a root-to-sink path
cover if and only if

\[
                         \epsilon_0=\cdots=\epsilon_{k-1}. \tag{3.2}
\]

Let \(P_i\) be the root of the path containing \(X_iY_i\), and let
\(\tau=(P_0\,P_1\,\cdots\,P_{k-1})\).  Then

\[
 \pi_{F'}=
 \begin{cases}
 \pi_F\circ\tau^{-1},&\epsilon_i=+\text{ for all }i,\\
 \pi_F\circ\tau,&\epsilon_i=-\text{ for all }i.
 \end{cases}                                             \tag{3.3}
\]

#### Proof

Removing one selected edge from each of \(k\) distinct paths leaves a root
prefix and a sink suffix for every \(i\).  If \(\epsilon_i=+\), the
\(Y_i\)-side is the suffix side and the \(X_i\)-side is the prefix side;
for \(\epsilon_i=-\), these roles are reversed.

The new edge \(Y_iX_{i+1}\) joins a prefix to a suffix exactly when
\(\epsilon_i=\epsilon_{i+1}\).  If the signs differ, it closes one
root--root component and one sink--sink component somewhere around the
cycle.  Thus (3.2) is necessary and sufficient.

In the plus case, the prefix rooted at \(P_{i+1}\) receives the old suffix
ending at \(\overline{\pi_F(P_i)}\), proving the first line of (3.3).
The minus case joins the prefix at \(P_i\) to the suffix formerly attached
to \(P_{i+1}\), proving the second. \(\square\)

### Corollary 3.2

A clean coherent \(C_6\) acts by a \(3\)-cycle and is even.  A clean
coherent \(C_8\) acts by a \(4\)-cycle and is odd.

Thus a genuine four-strand \(C_8\) does break the parity gate.  However,
this conclusion is false for an arbitrary \(C_8\) with repeated old
strands; the canonical two-row rectangle is an endpoint-inert example.

## 4. Folded \(C_6\)'s can be transpositions

The distinct-strand qualification in Corollary 3.2 is essential.

### Theorem 4.1 (folded transposition)

Consider a \(C_6\) with selected edges \(e_0,e_1,e_2\).  Suppose
\(e_0,e_1\) occur, in this order, on one old path \(A\), while \(e_2\)
occurs on another path \(B\), and suppose

\[
                         (\epsilon_0,\epsilon_1,\epsilon_2)=(+,-,+).
                                                               \tag{4.1}
\]

Write \(L_i,R_i\) for the root and sink sides of the cut \(e_i\).  The
old segments are

\[
\begin{array}{c}
 P_A\leadsto L_0,\quad R_0\leadsto L_1,\quad
 R_1\leadsto\overline{\pi_F(P_A)},\\
 P_B\leadsto L_2,\quad R_2\leadsto\overline{\pi_F(P_B)}.
\end{array}                                               \tag{4.2}
\]

The three new cycle edges pair

\[
                         R_0R_1,\qquad L_1L_2,\qquad R_2L_0. \tag{4.3}
\]

Consequently the two new paths are

\[
 P_A\leadsto\overline{\pi_F(P_B)},\qquad
 P_B\leadsto\overline{\pi_F(P_A)}.                       \tag{4.4}
\]

There is no internal cycle.  The endpoint operation is the transposition
\((P_A\,P_B)\).

Global reversal gives the other sign pattern, and cyclic relabelling gives
the analogous placements.  The exact criterion in every case is Theorem
2.1.  In particular:

\[
 \boxed{\text{\(C_6\)-moves do not have a universal parity invariant.}} \tag{4.5}
\]

They generate only even permutations when every admissible \(C_6\) is
clean, but a supply of folded routers can already generate \(S_N\).

If all three selected edges lie on one old path, any valid toggle leaves
its two global endpoints paired and hence acts trivially on monodromy.
With two cuts on one path, other orders/signs either act trivially or
create an internal cycle or a root--root/sink--sink pair; Theorem 2.1
distinguishes them without ambiguity.

This folded pattern is not merely an abstract strand diagram.  In the
rank-three factor (7.8) of the Hall note, the literal alternating cycle

\[
 \boxed{123-1236-126-1246-124-1234-123}                 \tag{4.6}
\]

has selected edges

\[
                  123-1236,\qquad1246-126,\qquad124-1234. \tag{4.7}
\]

The first two occur, in that order, on \(K_1\) with signs \(+,-\);
the third occurs on \(K_2\) with sign \(+\).  Toggling (4.6) swaps the
old suffixes of the paths rooted at \(123\) and \(124\).  Hence it is an
actual transposition router in \(M([6])\).

It toggles the first root edge on both paths.  Therefore it proves that
unrestricted \(C_6\)-moves have no parity invariant, while simultaneously
showing why parity can reappear after a first-layer freeze: this particular
odd router is then forbidden.

## 5. An explicit odd \(C_8\) with all first root edges fixed

Use the rank-three path cover \(K_1,\ldots,K_5\) displayed in (7.8) of
'MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md'.  It contains the four
selected edges in the alternating star cycle

\[
\boxed{
136-1236-236-2346-346-3456-356-1356-136.}              \tag{5.1}
\]

Indeed the selected edges are

\[
 1236-136,\quad2346-236,\quad3456-346,\quad1356-356,    \tag{5.2}
\]

lying respectively on the four distinct paths rooted at

\[
                         123,\quad124,\quad125,\quad135. \tag{5.3}
\]

All four are traversed from \(\mathcal Y\) to \(\mathcal X\), so Theorem
3.1 applies.  None of the four selected or four inserted edges is incident
with a Dyck root.  Thus every first root edge of the path cover remains
literally unchanged.

The original monodromy is

\[
                         \pi_F=(124\ 134\ 135).          \tag{5.4}
\]

After toggling (5.1), direct tracing gives

\[
\begin{aligned}
123&\longmapsto134,&124&\longmapsto125,&125&\longmapsto124,\\
134&\longmapsto135,&135&\longmapsto123.
\end{aligned}                                             \tag{5.5}
\]

Thus

\[
                         \pi_{F'}=(123\ 134\ 135)(124\ 125), \tag{5.6}
\]

which is odd.  This is a literal witness that an interior \(C_8\) can
change endpoint parity while the root-incident layer is frozen.

The cycle does pass through two first \(Y\)-vertices, so it changes the
second edge of those two paths.  If the prescribed “first layer” includes
the full two-edge prefixes \(P-Y_0-X_1\), rather than only the endpoint
incidences \(P-Y_0\), then those prefixes must also be placed in the
protected edge set.

## 6. Generated groups

Let \(\Omega=\mathcal D_r\), \(|\Omega|=N\).  Consider a switch-stable
atlas of clean coherent \(C_6\)'s.  Let \(\mathcal H_3\) be the
3-uniform hypergraph on \(\Omega\) whose edges are the three root strands
of the available switches.

### Theorem 6.1 (clean \(C_6\) group)

If the connected components of \(\mathcal H_3\) have vertex sets
\(\Omega_1,\ldots,\Omega_s\), then the group generated by the clean
\(C_6\) endpoint operations is

\[
                         \prod_{i=1}^s A_{\Omega_i}.     \tag{6.1}
\]

In particular, connected clean \(C_6\) support generates \(A_N\).

#### Proof

Every generator is a \(3\)-cycle supported inside one hypergraph
component, so the generated group is contained in the right side.
Conversely, the \(3\)-cycles supported on the hyperedges of a connected
3-uniform hypergraph generate the alternating group on its vertices.
One proof adds hyperedges along a connected edge ordering.  An edge
meeting the previous union in two vertices adjoins one new point by a
3-cycle.  An edge meeting it in one vertex adjoins two points; conjugating
its 3-cycle by the alternating group already generated on the old union
produces \((u\,x\,y)\) for every old \(u\), and products of two such
cycles produce 3-cycles containing two old points and one new point.
The base cases are \(A_3\) and \(A_4\).  Induction gives the claim.
\(\square\)

### Corollary 6.2 (two sufficient generation gates)

Each of the following produces the full symmetric group on the root
strands.

1. \(\mathcal H_3\) is connected and the atlas contains one clean coherent
   \(C_8\).  Then \(A_N\) and one odd \(4\)-cycle generate \(S_N\).
2. The graph whose edges are available folded-\(C_6\) transposition routers
   is connected.  Transpositions along a connected graph generate \(S_N\).

Here **switch-stable** means that the indicated router operations and their
inverses remain addressable after preceding router choices.  A sufficient
geometric implementation is a serial collection of disjoint router slabs:
each slab has the same boundary vertices in both states, all protected
prefix edges lie before the first slab, and the two internal \(b\)-factors
of a slab differ by the indicated alternating cycle.  Boundary
permutations then compose in slab order.

### Theorem 6.3 (monodromy correction under an atlas)

Suppose an interior switch-stable atlas avoids a protected edge set
\(E_{\rm prot}\), and its endpoint operations generate \(S_N\).  Then any
degree-feasible path cover in its reconfiguration component can be changed
to complement monodromy

\[
                         \pi=\mathrm{id}                \tag{6.2}
\]

without changing any edge of \(E_{\rm prot}\).

#### Proof

Every switch right-composes \(\pi\) by its router permutation or its
inverse, as in Theorems 3.1 and 4.1.  Since the generated group is \(S_N\),
choose a word equal to \(\pi^{-1}\).  Switch-stability realizes that word.
The final monodromy is \(\pi\pi^{-1}=\mathrm{id}\).  The cycles avoid
\(E_{\rm prot}\), so those edges never change. \(\square\)

Taking \(E_{\rm prot}\) to be the root-incident edges preserves a prescribed
first endpoint-colour layer exactly.  Taking it to contain the full
two-edge prefixes preserves both the first \(Y\)-colour and the first
internal \(X\)-state.

## 7. Exact obstruction when the gates fail

The group statement supplies statewise invariants, rather than merely a
counting obstruction.

* With clean \(C_6\)'s only, each hypergraph component \(\Omega_i\) is
  invariant and the sign of the induced permutation on it is invariant.
* If \(\mathcal H_3\) is connected but there is no odd router (neither a
  clean \(C_8\) nor a folded \(C_6\) transposition), the global coset
  \(\pi_F A_N\) is invariant.  An odd monodromy cannot be corrected.
* The currently proved canonical two-row octahedral \(C_8\)'s are not clean
  four-strand routers: their selected edges lie on two old paths and their
  strand diagrams give the identity endpoint operation.  They therefore do
  not break this parity gate.

The final bullet concerns the presently classified canonical rectangle
atlas, not all alternating \(C_8\)'s that might occur in a canonical
factor.  Finding a growing clean-\(C_8\) atlas, or a connected folded-\(C_6\)
transposition graph, remains a genuine geometric theorem.

## 8. Proved boundary

The following are now exact.

1. The set geometry of every \(C_6\) and \(C_8\) in \(M([2r])\).
2. The necessary-and-sufficient strand test for an arbitrary toggle.
3. The \(3\)-cycle and \(4\)-cycle operations in the clean case.
4. A folded \(C_6\) transposition, refuting an unconditional
   \(C_6\)-parity claim.
5. A literal \(r=3\) clean \(C_8\) which changes parity while preserving
   all first root edges.
6. Two explicit sufficient group-generation gates and the corresponding
   monodromy-correction theorem.

What is not proved is that either gate has a growing canonical realization
with the balanced protected layer required by the constant-one recursion.
