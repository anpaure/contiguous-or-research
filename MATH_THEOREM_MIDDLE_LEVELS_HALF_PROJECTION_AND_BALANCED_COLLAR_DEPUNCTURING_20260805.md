# Middle-levels half projection and exact balanced-collar depuncturing

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional unpunctured upper-exact Catalan forest theorem and
an exact equivalence for the fixed balanced-collar puncture.  The theorem
does not prove that a middle-levels Hamilton cycle can be chosen with the
required Catalan-scale bank of protected initial pivot stems.  That protected
vertical-spacing statement is the remaining owner/upper-q1 gate.

## 0. Outcome

Put `k=2r`, let `Omega` be a `2r`-set, and write

\[
 \mathcal X={\Omega\choose r},\qquad
 \mathcal U={\Omega\choose r+1},
\]

\[
 W=|\mathcal X|={2r\choose r},\qquad
 U=|\mathcal U|={2r\choose r+1},\qquad
 C=W-U={W\over r+1}=\operatorname {Cat}_r.       \tag{0.1}
\]

There are two results.

1. Every Hamilton cycle of the middle-levels graph on
   `Omega dot union {z}` canonically projects to a spanning `C`-path forest
   on `mathcal X` whose edge unions enumerate `mathcal U` exactly once.
   Thus the **unpunctured upper-exact Catalan forest exists in every
   dimension**, with no matching, absorber, or asymptotic theorem.
2. For the balanced collars in
   `MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`,
   the punctured prescribed-end forest is exactly equivalent to an
   unpunctured upper-exact Catalan forest in which the `C-1` pivot stems are
   prescribed initial path segments, the declared `P_j` are terminal
   endpoints, and the formal collar arcs have the declared acyclic component
   order.  Deleting those initial stems performs the puncture; restoring
   them, but not the repeated left seams, is the inverse operation.

The second result is the useful quantifier change.  The fixed puncture does
not require a new type of upper/owner rounding theorem.  One concrete route
is a protected version of the already unconditional middle-levels
projection.  Such a protected projection is sufficient, not asserted to be
necessary: a collar-adapted forest need not lift back to a middle-levels
Hamilton cycle.

## 1. The one-coordinate decomposition of the middle-levels graph

Let

\[
 G=\operatorname {ML}(2r+1)
\]

be the containment graph between the rank-`r` and rank-`r+1` subsets of
`Omega dot union {z}`.  Split its four vertex sectors as

\[
\begin{array}{c|c|c}
 &z\notin X&z\in X\\ \hline
 |X|=r&A=\mathcal X&B=z+{\Omega\choose r-1}\\
 |X|=r+1&C_+=\mathcal U&D=z+\mathcal X.
\end{array}                                                    \tag{1.1}
\]

There are exactly three edge sectors:

\[
       A-C_+,qquad B-D,qquad
       V_z=\{X-(z+X):X\in\mathcal X\}.              \tag{1.2}
\]

The third sector is a perfect matching, called the **vertical `z`-matching**.
There are no `B-C_+` edges.  Every vertex of `C_+` has all its neighbours
in `A`, and every vertex of `B` has all its neighbours in `D`.

## 2. Every middle-levels Hamilton cycle contains an upper-exact Catalan
forest

Fix any Hamilton cycle `H` of `G`.  Such a cycle exists by the Middle
Levels Theorem.  For every `R in mathcal U`, the vertex `R in C_+` has two
neighbours in `H`, both rank-`r` facets of `R`; call them `T_R,H_R`.  Put

\[
                    e_R=T_RH_R\in E(J(2r,r))          \tag{2.1}
\]

and

\[
                    F_z(H)=\{e_R:R\in\mathcal U\}.    \tag{2.2}
\]

### Theorem 2.1 (middle-levels half-projection theorem)

For every Hamilton cycle `H` of `ML(2r+1)`, `F_z(H)` is a spanning linear
forest on `mathcal X` with exactly `C=Cat_r` path components.  Moreover

\[
                 e_R\longmapsto T_R\cup H_R=R        \tag{2.3}
\]

is a bijection from `E(F_z(H))` to `mathcal U`.

The endpoints of `F_z(H)` are exactly the owners `X in mathcal X` for
which the vertical edge `X-(z+X)` belongs to `H`.  Consequently `H` uses
exactly

\[
                            2C                       \tag{2.4}
\]

vertical `z`-edges.

#### Proof

Every `R in C_+` has no neighbour outside `A`, so its two cycle neighbours
`T_R,H_R` are distinct members of `mathcal X` contained in `R`.  They are
rank `r`, hence differ by one exchange and have union `R`.  This proves
(2.1) and the bijection (2.3).

At an owner `X in A`, the Hamilton cycle uses its unique possible vertical
edge zero or one times.  Its remaining incident cycle edges lie in `A-C_+`.
Therefore

\[
 d_{F_z(H)}(X)=
 2-\mathbf1[,X-(z+X)\in H,]\in\{1,2\}.             \tag{2.5}
\]

In particular `F_z(H)` spans every owner and has maximum degree two.

It has no cycle.  Indeed, if `K` were a cycle component of `F_z(H)`, every
owner of `K` would have degree two in the `A-C_+` restriction, and every
intervening upper vertex already has its two Hamilton-cycle edges inside
that same restriction.  Thus the corresponding alternating cycle in
`A union C_+` would be a whole connected component of `H`.  But `H` also
contains the nonempty sectors `B,D`, contradicting Hamiltonicity.

Finally

\[
 |E(F_z(H))|=|\mathcal U|=U=W-C.                     \tag{2.6}
\]

A spanning forest on `W` vertices with `W-C` edges has exactly `C`
components.  Its degree-one vertices are precisely the owners in (2.5)
using a vertical edge.  Every path has two ends, so their number, and hence
the number of selected vertical edges, is `2C`.  This proves (2.4). `square`

### Corollary 2.2 (the opposite half)

Applying the same argument to the `B-D` restriction and then deleting `z`
gives a second spanning `C`-path forest on `mathcal X` whose edge
**intersections** enumerate `binom(Omega,r-1)` exactly once.

The two forests come from the same Hamilton cycle, but they need not be the
same forest.  Thus Theorem 2.1 closes the upper-only unpunctured row, not the
full Catalan Linear Matching theorem with both immediate palettes on one
edge set.

### Proposition 2.3 (exact run dictionary)

Traverse `H` cyclically and cut at its vertical `z`-edges.  Its maximal
`z`-absent arcs are exactly the alternating lifts of the path components of
`F_z(H)`.  If such an arc contains `ell` vertices of `A`, the corresponding
projected path contains `ell` owners.  There are exactly `C` such arcs and

\[
                         \sum_{i=1}^{C}\ell_i=W.     \tag{2.7}
\]

Thus prescribing a pivot stem as an initial segment of the half-projection
is literally prescribing the beginning of one `z`-absent run immediately
after a vertical crossing.  In particular, a bank of `C-1` length-`s`
initial stems requires `C-1` distinct `z`-absent runs of owner length at
least `s+1`.  The locations of the vertical crossings determine these run
boundaries, but do not by themselves determine the pairing/order of the
components under the later formal collar arcs.

#### Proof

The only edges crossing between `A union C_+` and its complement are the
vertical edges (1.2).  Hence the pieces left after cutting at all such edges
are precisely the maximal arcs in the two halves.  Projecting an
`A-C_+` arc suppresses each intervening `C_+` vertex and retains its `A`
vertices in order, giving one component of (2.2).  The component count and
sum follow from Theorem 2.1. `square`

## 3. Balanced collars and their nonrepeated stems

Now fix `b=C-1` pairwise owner-disjoint balanced collars.  For collar `j`,
write

\[
 P_j,M^j_0,M^j_1,\ldots,M^j_h,N_j                 \tag{3.1}
\]

for its owner path and put `s=h+1`.  Its internal upper colours are

\[
 U^j_i=M^j_{i-1}\cup M^j_i\quad(1\le i\le h),
 \qquad U^j_*=M^j_h\cup N_j.                         \tag{3.2}
\]

The left seam satisfies

\[
                       P_j\cup M^j_0=U^j_1.          \tag{3.3}
\]

Thus the **nonrepeated stem** is

\[
 S_j=M^j_0-M^j_1-\cdots-M^j_h-N_j                  \tag{3.4}
\]

with edge set of order `s`, while the full collar is obtained by adjoining
the left edge `P_jM^j_0`.  The stem colours are

\[
              \mathcal U_j=\{U^j_1,\ldots,U^j_h,U^j_*\},
              \qquad |\mathcal U_j|=s.              \tag{3.5}
\]

Assume the `mathcal U_j` are mutually disjoint.  Put

\[
 R=\dot\bigcup_{j=1}^{b}\{M^j_0,\ldots,M^j_h\},
 \qquad
 \mathcal U_B=\dot\bigcup_{j=1}^{b}\mathcal U_j.   \tag{3.6}
\]

Then `|R|=|mathcal U_B|=bs`.

## 4. The terminal-stem normal form

Call an oriented upper-exact Catalan forest `F` on all `mathcal X`
**collar-adapted** when:

1. every stem (3.4) occurs in `F` with its displayed orientation;
2. `M^j_0` is the initial endpoint of its component, so (3.4) is literally
   an initial segment;
3. every `P_j` is a terminal endpoint of a component; and
4. after contracting the `C` components of `F`, the formal collar arcs

   \[
                         P_j\longrightarrow M^j_0    \tag{4.1}
   \]

   form a directed spanning path on the component set.

Item 4 implies in particular that the `C-1` stem components are distinct,
the `P_j` use distinct terminal occurrences, and there is no component
loop.

Let

\[
        V_0=\mathcal X\setminus R,
        \qquad \mathcal U_0=\mathcal U\setminus\mathcal U_B.  \tag{4.2}
\]

### Theorem 4.1 (balanced-collar depuncturing equivalence)

The following objects are in canonical bijection.

1. A collar-adapted upper-exact Catalan forest `F` on `mathcal X`.
2. A spanning `C`-component linear forest `F_0` on `V_0` such that
   `e -> union(e)` bijects `E(F_0)` to `mathcal U_0`, with the exposed
   oriented endpoint pairs `(P_j,N_j)`: each `N_j` is an initial endpoint,
   each `P_j` is a terminal endpoint, and the component-level arcs
   `P_j -> N_j` join its `C` components into one directed spanning path.

The maps are

\[
                         F\longmapsto F-R             \tag{4.3}
\]

and

\[
 F_0\longmapsto
 F_0\cup\dot\bigcup_j E(S_j).                       \tag{4.4}
\]

After either construction, adjoining the `C-1` repeated left seams
`P_jM^j_0` gives one Hamilton path on all `W` owners.  It covers every
upper-q1 colour and has exactly `C-1` multiplicity excess, one second copy
of `U^j_1` per collar.

#### Proof

Let `F` be collar-adapted.  In one stem component, the vertices
`M^j_0,...,M^j_h` form the initial `s`-vertex block and the only edge from
that block to its complement is `M^j_hN_j`.  Deleting the block therefore
deletes exactly the `s` stem edges and truncates, rather than splits, its
path component.  It leaves `N_j` as the new initial endpoint.  Since the
stems lie in distinct components, deleting all of `R` preserves exactly
`C` components.

The upper map of `F` is a bijection.  The deleted stem edges carry exactly
the disjoint set `mathcal U_B`, so the remaining edges biject to
`mathcal U_0`.  The terminal endpoints `P_j` survive.  The component path
in Item 4 now says precisely that inserting the full collars joins all
truncated components in one order.  This proves 1 -> 2.

Conversely, start from `F_0`.  At the initial endpoint `N_j`, attach the
new path

\[
                 M^j_0-M^j_1-\cdots-M^j_h-N_j.       \tag{4.5}
\]

It adds `s` new vertices and `s` edges to one existing path component; it
neither merges components nor creates a cycle.  The owner banks are
disjoint, so all attachments may be made simultaneously.  The resulting
forest spans all `W` owners and still has `C` components.  Its upper
palette is the disjoint union

\[
                         \mathcal U_0\dot\cup\mathcal U_B
                         =\mathcal U,                 \tag{4.6}
\]

exactly once.  Every attached stem is an initial segment and the old
terminal endpoints `P_j` remain terminal, so the result is collar-adapted.
This proves 2 -> 1 and that (4.3)--(4.4) are inverse.

Finally insert the left seams.  The component-level arcs form a spanning
path, so the physical result is one Hamilton path.  Equations (3.2)--(3.3)
show that the stem restores every deleted colour once and the left seam
adds exactly one repeat of `U^j_1`.  No other repeat occurs. `square`

### Corollary 4.2 (defect does not amplify under depuncturing)

The equivalence is defect-preserving.  More precisely, suppose an
unpunctured collar-structured forest (satisfying the same stem, endpoint,
and component-order conditions, but not assumed upper-exact) has a set `D`
of missing upper colours and
the same number of repeated occurrences, all outside `mathcal U_B`, while
every colour in `mathcal U_B` occurs exclusively on its declared stem.
Then deleting the stems leaves exactly the same defect `D` on
`mathcal U_0`.  Restoring the collars creates only the forced left-seam
repeats in addition to that unchanged defect.

Thus an `O(1)`-defect protected unpunctured theorem gives an `O(1)`-defect
punctured theorem.  The Catalan number of punctures causes no multiplication
of the residual defect.

## 5. Endpoint roles turn the protected problem into one forward matching

There is a useful exact formulation of the remaining protected theorem.
Orient every component of a collar-adapted forest.  Let

\[
 \mathcal S=\{M^j_0:1\le j\le C-1\}\cup\{a_*\},
 \qquad
 \mathcal T=\{P_j:1\le j\le C-1\}\cup\{z_*\},       \tag{5.1}
\]

where `a_*` is the unique component initial endpoint not entered by a
collar and `z_*` is the unique terminal endpoint not used by a collar.
The tail and head role copies have respective active sets

\[
                  \mathcal X_{\rm tail}\setminus\mathcal T,
       \qquad     \mathcal X_{\rm head}\setminus\mathcal S.   \tag{5.2}
\]

Both have order

\[
                         W-C=U.                     \tag{5.3}
\]

For an oriented Johnson edge `T -> H`, retain the atom

\[
                         (T\cup H,T,H).              \tag{5.4}
\]

### Theorem 5.1 (endpoint-saturation/forward-host criterion)

Fix the collar stems and the two endpoint banks (5.1).  A collar-adapted
upper-exact forest exists if and only if there is a matching of order `U`
in the three-partite atom system (5.4) which

1. saturates `mathcal U`, the active tail bank, and the active head bank;
2. contains all oriented stem atoms; and
3. after adjoining the fixed formal arcs `P_j -> M^j_0`, has no directed
   cycle.

Moreover, if there is one strict potential `phi` satisfying

\[
 \phi(T)<\phi(H)\quad\hbox{for every allowed selected atom},
 \qquad
 \phi(P_j)<\phi(M^j_0)\quad(1\le j<C),              \tag{5.5}
\]

then Item 3 is automatic.  On that forward face, the remaining owner/q1
problem is a single protected perfect matching in a balanced three-partite
hypergraph; no separate graphic or endpoint-pairing condition remains.

#### Proof

In any matching saturating the three parts, every owner outside
`mathcal T` occurs once as a tail and no owner of `mathcal T` does; dually,
every owner outside `mathcal S` occurs once as a head and no owner of
`mathcal S` does.  Hence the selected directed graph is a disjoint union of
exactly `C` directed source-to-terminal paths and some directed cycles.
The stem containment makes its named paths begin as prescribed.

Adjoining the `C-1` formal collar arcs consumes all but one source and all
but one terminal occurrence.  Every vertex then has indegree and outdegree
one except the unique global source `a_*` and sink `z_*`.  Such a graph is
one spanning directed path plus zero or more directed cycles.  It is one
spanning path exactly when the cycles are absent.  Removing the formal arcs
recovers the collar-adapted forest and its component order.  This proves the
equivalence.

Under (5.5), every selected and formal arc strictly increases `phi`, so no
directed cycle exists. `square`

## 6. Exact new frontier

Theorem 2.1 shows that the unprotected upper-exact forest is not open: it is
an immediate corollary of the Middle Levels Theorem.  Theorem 4.1 shows that
the fixed balanced-collar puncture is not an independent rounding problem:
it is terminal-stem deletion from an unpunctured forest.

Within the middle-levels route, the remaining central theorem can therefore
be stated without punctured language.

> **Protected half-projection theorem.**  There is a Hamilton cycle of
> `ML(2r+1)` and a distinguished coordinate `z` such that the `z`-free
> half-projection contains the `C-1` prescribed pivot stems as initial
> component segments, with the prescribed terminal bank and component
> order.  In particular, its vertical `z`-crossings occur at the declared
> initial and terminal stem boundaries; that crossing condition alone does
> not encode the required component order.

This protected half-projection is a clean sufficient theorem, not an exact
converse to Theorem 4.1.  For the full word construction it must still be intersected
with residence, deeper upper witnesses, and named lower flags.  Nothing
here asserts those later rows.  But at owner/upper-q1 level, it removes the
unpunctured existence and the puncture accounting completely; only the
protected placement inside a middle-levels Hamilton cycle remains on this
route.
