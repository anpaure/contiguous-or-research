# Coherent-edge supply, forced-port Hall, and router-resilient Catalan catalogues

Date: 2026-07-31  
Status: exact postrepair decoration-filtered theorem; static coherent ECO
component supply closed in every dimension; exact private-collar,
weighted-hypertree, preservation and missing-rectangle theorems; repaired
project-\(m=5\) private ECO base proved; no all-\(m\) compatible
private-ECO-hypertree theorem

## 0. Rebased verdict

After a debt-carrying repair/rethread packet reaches an accepting prepared
state, the fixed-decoration transparent gluing problem has three live
**selection** rows on the private/aligned face:

1. a simultaneous **component-faithful coherent component tree**, or the
   separately certified ECO hypertree of Section 6;
2. one joint **forced-port residual gap--Hall** extension for the labels
   actually selected; and
3. **router resilience**

   \[
                      c(K_Y)\le |Y|+1               \tag{0.1}
   \]

   after filtering the binary catalogue by that same decoration.  A
   multi-component ECO atom instead uses the explicit simultaneous-route
   hypothesis of Theorem 6.2.

Coherence removes local palette transparency as an independent row.  It
does not remove the correlation between the tree selected by the
graphic--gammoid criterion and the ports which must belong to one
decoration.

This note proves the exact correlated quantifier

\[
  \exists\,\mathcal D\quad\forall\,Y,
  \qquad c(K_Y(\mathcal D))\le |Y|+1,               \tag{0.2}
\]

and not the invalid order in which the decoration may depend on the router
cut.  It also proves the factorwise version of forced-port Hall needed
before the factor is Hamiltonian, a recursive private-router closure, and
the first raw port-capacity obstruction.

On the private face of item 2195, the latter two rows cease to be abstract
optimization problems: literal owner alignment or zero flux closes the
matching, and node-private or certified laminar paths close routing.  The
ECO theorem then closes static coherent incidence.  The remaining supply
problem is the simultaneous private hypertree isolated in Section 6.  The
repair-first order is not merely formal: Theorem 6.8 proves it exactly at
project \(m=5\), the first dimension where raw canonical ECO gluing fails.

Hamilton-to-Hamilton rethreads are preparation moves, not component edges.
Component-splitting moves are likewise excluded from the ordered merge
list.  If either kind is used inside a debt macro, the macro must terminate
first and the coherent merge catalogue must be recomputed at its endpoint.

## 1. Prepared face and typed labels

Fix prepared non-decoration data

\[
                         \mathscr S=(F,N,\mathcal C),                  \tag{1.1}
\]

where:

* \(F\) is the current exact factor and has \(q\) physical components;
* \(N\) is the fixed vertex-capacitated linkage router with sink bank
  \(Z\); and
* \(\mathcal C\) is a finite catalogue of collar labels.

The decoration is chosen by the forced-port Hall row below; it is not fixed
independently in advance.  The phrase **prepared face** means that, for
every decoration admitted as a certificate, the selected labels satisfy the
private/aligned gap, trace, occurrence and prefix-reachability hypotheses of
handoff item 2189.  Equivalently those rows may be reverified after the
forced-port matching is decoded.  They are assumptions here, not
consequences of coherence.

Every label \(t\in\mathcal C\) has:

* one effective component edge \(c_t\) in a multigraph \(K\) on the
  components of \(F\);
* one source \(s_t\) in \(N\); and
* six marked Boolean-incidence ports, three on each shore.

Only labels oriented so that their toggle merges two distinct current
components are admitted to \(\mathcal C\).  Thus every \(c_t\) is a
nonloop effective component edge.

For \(Y\subseteq V(N)\), let

\[
 T_Y=\{t\in\mathcal C:s_t\text{ reaches }Z\text{ in }N-Y\},\qquad
 K_Y=(V(K),\{c_t:t\in T_Y\}).                       \tag{1.2}
\]

An all-six label is **coherent** when its three lower external insertion
labels agree and its three upper external deletion labels agree:

\[
 d_a=d_b=d_c,\qquad e_{ab}=e_{bc}=e_{ca}.           \tag{1.3}
\]

By the coherent-hex theorem, (1.3) is equivalent to fixed-decoration
palette transparency once all six ports are selected; boundary alternation
is automatic.

For \(S\subseteq\mathcal C\), let \(P_A(S)\) and \(P_B(S)\) be the unions
of its forced A-position and B-position port occurrences on the prepared
middle-levels factor.  A positions carry the upper-turn colours and B
positions carry the lower-turn colours.

### Lemma 1.1 (factorwise forced-port Hall)

Write the alternating components of \(F\) as

\[
 C_\alpha=A_{\alpha,0},B_{\alpha,0},A_{\alpha,1},B_{\alpha,1},\ldots
\]

and let both global turn-colour alphabets have size \(P\).  A joint
occurrence decoration containing prescribed ports \(P_A,P_B\) exists if
and only if all of the following hold.

1. The forced upper colours are globally distinct, and so are the forced
   lower colours.
2. There is one global upper-colour transversal
   \(I=\bigsqcup_\alpha I_\alpha\supseteq P_A\).
3. If \(I_\alpha=\varnothing\), then \(P_B\cap C_\alpha=\varnothing\),
   and the prepared state records one of the two residual alternating
   cross-edge phases of that unmarked component.
   If \(I_\alpha\ne\varnothing\), every cyclic gap between consecutive
   points of \(I_\alpha\) contains at most one forced lower port.
4. Delete every gap containing a forced lower port and delete its forced
   lower colour.  In the bipartite graph from all remaining active gaps to
   all remaining lower colours, with adjacency given by occurrence in the
   gap, there is a perfect matching.

If the prepared face requires every component to carry a mark, add the
condition \(I_\alpha\ne\varnothing\) for every \(\alpha\).

#### Proof

In a joint decoration, the selected upper positions form the transversal
\(I\).  On each active component, alternation puts exactly one selected
lower occurrence in each cyclic \(I_\alpha\)-gap.  Hence the forced colours
are distinct, no gap contains two forced lower ports, and the unforced
selected occurrences form the residual matching.  An inactive component
contains no selected lower port and retains its recorded residual phase.

Conversely, select every forced lower port and, in every residual gap, the
occurrence supplied by the perfect matching.  Every active component now
alternates selected upper and lower positions, inactive components receive
no mark and retain their chosen phases, and the two selected palettes are
globally bijective.  This is the required decoration. \(\square\)

The fixed-cycle forced-port theorem is the one-component case.  Lemma 1.1
is needed because the router theorem starts from a multi-component factor.
Equivalently one may apply the fixed-cycle theorem only to the same final
Hamilton endpoint and transport its decoration backwards through the full
prepared cube; mixing a Hall certificate from one endpoint with a router
certificate from another is invalid.

## 2. The exact selected-tree theorem

### Theorem 2.1 (selected coherent tree criterion)

Let \(S\subseteq\mathcal C\) consist of coherent labels.  Under the
prepared hypotheses of Section 1, the labels in \(S\) can be ordered as a
fixed-decoration transparent component-spanning list if and only if all
three conditions below hold.

1. **Component tree.**  The edges \(\{c_t:t\in S\}\) form a spanning tree
   of the \(q\) current components.  In particular \(|S|=q-1\).
2. **Forced-port Hall.**  The ports \(P_A(S),P_B(S)\) satisfy the
   factorwise criterion of Lemma 1.1 for some witness \((I,M)\), and the
   resulting decoration is admitted by the H0--H5 prepared cube of \(S\).
   In particular there exists one global upper transversal \(I\), and only
   after fixing that \(I\) is the one residual gap--lower-colour matching
   \(M\) required.

3. **Selected-tree router resilience.**  If

   \[
     K^S_Y=(V(K),\{c_t:t\in S,\ s_t\text{ reaches }Z\text{ in }N-Y\}),
                                                               \tag{2.1}
   \]

   then

   \[
                         c(K^S_Y)\le |Y|+1
                         \qquad\text{for every }Y\subseteq V(N).       \tag{2.2}
   \]

Whenever these conditions hold, the residual Hall matching in Item 2
constructs one decoration \(\mathcal D_S\) containing every forced port,
and every ordering of the tree \(S\) is executable on the prepared face.

#### Proof

Assume Items 1--3.  Lemma 1.1 applied to Item 2 produces one
joint alternating occurrence SDR \(\mathcal D_S\) containing all ports of
all labels in \(S\).  Coherence (1.3) makes every selected label
\(\mathcal D_S\)-transparent; no additional local palette test remains.

Apply the router-resilience theorem to the restricted catalogue \(S\).
Because its component graph is already a tree, (2.2) says exactly that this
tree is independent in the linkage gammoid.  Thus its \(q-1\) sources have
one simultaneous vertex-disjoint linkage to the sink bank.  The prepared
private/aligned hypotheses and item 2189 then imply that every ordering of
the tree joins two actual current components at each step, preserves
\(\mathcal D_S\), preserves the carried leaf-peelable gap matching and
trace state, and respects prefix reachability.

Conversely, an executable component-spanning list has \(q-1\) effective
merge edges and no split, so those edges form a component tree.  Its fixed
decoration restricts to an upper transversal \(I\) and exactly one selected
lower occurrence in each \(I\)-gap.  Removing the forced gaps and colours
leaves the residual perfect matching, proving Item 2.  The simultaneously
routed list is a gammoid-independent spanning tree; the router-resilience
criterion applied to its restricted ground gives (2.2).  The assertion
about every ordering uses the full H0--H5 subset-cube hypotheses:
root-only coherence or singleton checks would not suffice. \(\square\)

## 3. The exact decoration-filtered catalogue theorem

Let \(\mathfrak D\) be the set of joint occurrence decorations produced by
Lemma 1.1 which also satisfy the prepared entrance conditions.  For
\(\mathcal D\in\mathfrak D\), define

\[
 \mathcal C(\mathcal D)=
 \{t\in\mathcal C:t\text{ is coherent, all six ports of }t
       \text{ lie in }\mathcal D,\text{ and its frozen signature is }
       \mathcal D\text{-compatible}\}.                              \tag{3.1}
\]

The H0--H5 superposition hypotheses are required on every component-forest
subset of \(\mathcal C(\mathcal D)\).  Put

\[
 K_Y(\mathcal D)=
 \bigl(V(K),\{c_t:t\in\mathcal C(\mathcal D),\
             s_t\leadsto Z\text{ in }N-Y\}\bigr).                  \tag{3.2}
\]

### Theorem 3.1 (single-decoration router criterion)

Under the prepared hypotheses, the following are equivalent.

1. There are one joint decoration \(\mathcal D\) and an ordered
   fixed-\(\mathcal D\) transparent component-spanning merge list whose
   label set lies in \(\mathcal C(\mathcal D)\).
2. There is one \(\mathcal D\in\mathfrak D\) such that

   \[
      c(K_Y(\mathcal D))\le |Y|+1
      \qquad\text{for every }Y\subseteq V(N).                       \tag{3.3}
   \]

3. There are one upper transversal \(I\) satisfying the componentwise
   conditions of Lemma 1.1 and one residual perfect matching \(M\), giving
   \(\mathcal D=\mathcal D(I,M)\), such that for every router deletion
   \(Y\) and every partition \(\Pi\) of the factor components,

   \[
   |Y|+
   \bigl|\{t\in\mathcal C(\mathcal D):
        c_t\in\delta_K(\Pi),\ s_t\leadsto Z\text{ in }N-Y\}\bigr|
       \ge |\Pi|-1.                                                  \tag{3.4}
   \]

4. There are a coherent component tree \(S\subseteq\mathcal C\) and a
   factorwise Hall witness producing \(\mathcal D\in\mathfrak D\), with
   \(S\subseteq\mathcal C(\mathcal D)\), such that the sources of \(S\)
   admit one simultaneous vertex-disjoint linkage.

#### Proof

Suppose Item 1 holds, and let \(S\) be its label set.  The selected labels
form a component tree and their router sources have simultaneous
vertex-disjoint paths.  Deleting \(Y\) destroys at most \(|Y|\) of those
paths.  The surviving selected tree therefore has at most \(|Y|+1\)
components.  It is a subgraph of \(K_Y(\mathcal D)\), proving (3.3).

Conversely, fix the single decoration in Item 2.  The router-resilience
theorem applied to the already filtered ground set
\(\mathcal C(\mathcal D)\) supplies a common graphic--gammoid spanning
tree.  Every one of its labels is coherent and has all six ports in this
same \(\mathcal D\).  The coherent-hex theorem gives fixed-decoration
transparency, and item 2189 executes every ordering of the tree.

The equivalence of (3.3) and (3.4) is the partition form of the
graphic--gammoid criterion: the component-count lemma of the router theorem
collapses all partitions precisely to (3.3).  Lemma 1.1 identifies every
admissible \(\mathcal D\) with one global \(I\) followed by one residual
matching \(M\).  Finally, Item 4 gives Item 1 by Theorem 2.1, and any list
from Item 1 supplies the tree and linkage of Item 4. \(\square\)

The quantifier order in (3.3) is load-bearing:

\[
          \boxed{\exists\,\mathcal D\ \forall\,Y,\Pi}             \tag{3.5}
\]

is required.  Neither \(\forall Y,\Pi\,\exists\mathcal D_{Y,\Pi}\) nor
the conjunction “some Hall tree exists and some router tree exists” is
sufficient.  The same decoration must filter the catalogue before every
router cut is tested.

### Corollary 3.2 (catalogue-wide sufficient certificate)

If one decoration contains every port of a coherent catalogue and the full
catalogue satisfies \(c(K_Y)\le |Y|+1\) for every \(Y\), then an executable
merge list exists.

#### Proof

For that decoration, \(\mathcal C(\mathcal D)=\mathcal C\).  Apply Theorem
3.1. \(\square\)

This deliberately strong corollary is the only safe decoupling of Hall and
router selection used here.

## 4. Constructive private-router closure

### Theorem 4.1 (private-tree Pascal closure)

Suppose a parent stage has child component blocks
\(Q_1,\ldots,Q_r\), one common decoration \(\mathcal D\), and the following
data.

1. In each child block, a \(\mathcal D\)-compatible coherent catalogue is
   router-resilient in an internal router \(N_i\).
2. A tree on the \(r\) child blocks is represented by coherent
   \(\mathcal D\)-compatible bridge labels.
3. Every bridge label has a fixed router path; these paths are pairwise
   vertex-disjoint and disjoint from all internal router banks \(N_i\).
4. The child and bridge labels together satisfy the H0--H5 product
   hypotheses.  In particular all their forced ports are certified by the
   one decoration \(\mathcal D\), not by separate child decorations.

Then the union catalogue is router-resilient and the parent has an
executable fixed-\(\mathcal D\) transparent component-spanning list.

#### Proof

Let \(Y_i=Y\cap V(N_i)\), and let \(Y_0\) be the remainder.  The surviving
catalogue in child \(i\) has at most \(|Y_i|+1\) components.  Let \(b\) be
the number of fixed bridge paths hit by \(Y_0\).  Path privacy gives
\(b\le |Y_0|\).  At least \(r-1-b\) edges of the bridge tree survive, and
each joins two pieces lying in different child blocks.  Hence

\[
\begin{aligned}
c(K_Y(\mathcal D))
 &\le \sum_{i=1}^r (|Y_i|+1)-(r-1-b)\\
 &\le |Y|+1.
\end{aligned}                                                       \tag{4.1}
\]

Theorem 3.1 applies. \(\square\)

### Theorem 4.2 (finite terminal-mode tree grammar)

Fix a rooted scaffold tree on the factor components.  At each vertex
\(v\), let \(\Sigma_v\) be a finite family of zero-debt terminal rethread
modes; these modes have no component rank.  For an edge \(vw\), let
\(H_{vw}(\sigma,\tau)\) be the literal coherent all-six merge options
available in terminal modes \(\sigma,\tau\).  Assume different scaffold
edges have product-private supports, fixed router paths, and forced
gap--colour tubes whose positions and colours are disjoint across edges.
Terminal modes export one compatible base matching and upper-transversal
state; every forced tube is owner-aligned on the leaf-forest face or has
zero matching flux for that base matching.  After the forced tubes are
removed, the residual gap graph is the direct sum of the child residual
graphs.  Every other prepared guard is part of the terminal mode.

Define bottom-up

\[
 A_v=\{\sigma\in\Sigma_v:\text{ for every child }w\text{ there are }
       \tau\in A_w\text{ and }h\in H_{vw}(\sigma,\tau)\}.            \tag{4.2}
\]

On this product face, a common decoration and coherent spanning merge list
exist if and only if \(A_{\rm root}\ne\varnothing\).

#### Proof

If the root set is nonempty, choose modes and merge options recursively.
The private residual matchings unite to the single global forced-port Hall
matching.  Coherence gives transparency, the scaffold gives the component
tree, and the fixed private paths give router resilience exactly as in
Theorem 4.1.  Conversely, any grammar-conforming list restricts on each
subtree to witnesses in (4.2); induction from the leaves puts its root mode
in \(A_{\rm root}\). \(\square\)

Thus the first empty \(A_v\) is an exact finite bad-subtree certificate.  If
every oriented parent--child relation is parent-total, all \(A_v\) are
nonempty and the induction is automatic.  Cylindrical Pascal lifting
preserves local coherence literally: the core \(H\) is replaced by
\(H\cup P\), while the common external labels and both forced colour
triples lift injectively.  It preserves the full grammar only under the
gap-order and router-embedding hypotheses of Theorem 5.4; a new selected
upper point may otherwise subdivide an owner gap.  Therefore a finite
parent-total family of Pascal node types satisfying the full private product
hypotheses would prove the missing catalogue existence.  Constructing such
a family remains open.

The residual Hall row can also be certified constructively by a
leaf-peelable residual gap graph.  This is stronger than existence of a
perfect matching but stable under a truly private direct-sum recursion.

### Proposition 4.3 (bounded-pressure coherent selector)

On the product-private face of Theorem 4.2, suppose every scaffold-edge
task has a list of at least \(L\) coherent options.  Let \(J\) be the task
interaction graph, and suppose a fixed option forbids at most \(\beta\)
options in any neighbouring task.

1. If \(J\) has a processing order of vertex separation at most \(w\) and
   \(L>w\beta\), a deterministic greedy compatible selector exists.
2. If \(J\) has maximum degree \(\Delta\) and

   \[
          e\,\frac{\beta}{L}(2\Delta-1)\le1,          \tag{4.3}
   \]

   a compatible selector exists by the symmetric local lemma.

The first assertion keeps at most \(w\) earlier option signatures live.  If
one signature exports at most \(p\) boundary objects, the live boundary is
at most \(p(w+1)\), independently of the total packet length.

#### Proof

In a vertex-separation order, at most \(w\) already chosen neighbours can
constrain the current list, and together they forbid at most \(w\beta<L\)
options.  Greedy selection proves Item 1.  For Item 2 choose options
independently and uniformly.  The incompatibility event on one edge has
probability at most \(\beta/L\) and depends on at most
\(2\Delta-2\) other edge events.  The symmetric local lemma gives (4.3).
\(\square\)

This proposition is invalid before the private-tube reduction: generic
residual gap Hall is a global event, not a pairwise conflict which may be
hidden in an interaction graph.

### Proposition 4.4 (forced-port capacity)

Let \(P_m\) be the size of either turn-colour alphabet.  Every selected
coherent tree satisfies

\[
       |P_A(S)|\le P_m,\qquad |P_B(S)|\le P_m.       \tag{4.4}
\]

If the six physical port sets of its labels are pairwise disjoint, then

\[
                         3(q-1)\le P_m.              \tag{4.5}
\]

#### Proof

Lemma 1.1 requires injectivity of both forced-colour maps, so neither shore
can contain more forced ports than its complete turn alphabet.  Under port
disjointness, every one of the \(q-1\) labels contributes three new ports to
each shore, giving (4.5). \(\square\)

For the standard plane-tree component count \(q\le {\rm Cat}_{m-1}\), the
raw disjoint-port inequality is not restrictive from \(m=4\) onward.
Indeed, with \(P_m=\binom{2m-1}{m-2}\),

\[
 \frac{P_m}{{\rm Cat}_{m-1}}
   =\frac{(2m-1)(m-1)}{m+1}\ge3\qquad(m\ge4).        \tag{4.6}
\]

Thus scalar port capacity is not the standard-factor obstruction; the
correlated decoration and residual Hall row may still fail.  For a general
factor with too many components, (4.5) proves that a port-disjoint all-six
catalogue can only be a post-bulk merge mechanism.  Rethread packets may
reduce or reorganize the component state before the fixed catalogue is
formed, but they cannot be counted as missing merge edges.

## 5. The joint private coherent collar

The two new private closures turn Theorem 3.1 from a Hall/router test into
a literal construction invariant.

Fix an upper transversal \(I\), its gap--lower-colour graph \(\Gamma_I\),
and a perfect matching \(M\).  For a coherent merge label \(t\), write
\(F_t\) for its three forced lower port edges.  Call \(t\) an
**\((I,M)\)-private coherent collar** when:

1. \(t\) is a component-faithful nonloop coherent all-six merge;
2. all forced upper ports lie in \(I\), the three edges of \(F_t\) have
   distinct gap and colour endpoints, and \(F_t\subseteq M\);
3. its occurrence transfer has a fixed private source--sink path; and
4. its full physical support, gap attachment, trace and reachability
   signature satisfies H0--H5 on the intended product cube.

For a family of collars, **matching privacy** means their forced matching
edges and private gap-attachment banks are pairwise disjoint.  **Route
privacy** means their occurrence paths are pairwise vertex-disjoint and
avoid all child router banks.  These are different resource statements.

### Lemma 5.1 (matching-seam preservation)

Let \(\Gamma^\circ\) be a core forest with a matching \(M^\circ\).  For every prospective
collar \(t\), let \((B_t^0,M_t^0)\) and \((B_t^1,M_t^1)\) be its two
private rooted forest alternatives.  Suppose different banks meet only the
core, each at a distinct private root \(r_t\), and put

\[
 b_t=\deg_{M_t^0}(r_t)=\deg_{M_t^1}(r_t)\in\{0,1\}.
\]

Require \(\deg_{M^\circ}(r_t)=1-b_t\), and require \(M^\circ\) to cover
every nonroot core vertex.  For both \(\epsilon\in\{0,1\}\), require
\(M_t^\epsilon\) to cover every nonroot vertex of \(B_t^\epsilon\)
exactly once.  For \(U\) a set of already used collars, put

\[
 \Gamma_U=\Gamma^\circ\cup\bigcup_{t\notin U}B_t^0
                         \cup\bigcup_{t\in U}B_t^1,
 \qquad
 M_U=M^\circ\cup\bigcup_{t\notin U}M_t^0
                    \cup\bigcup_{t\in U}M_t^1.                     \tag{5.1}
\]

Then every \(\Gamma_U\) is a forest, \(M_U\) is its unique perfect
matching, and a pending collar with \(F_t\subseteq M_t^0\) remains
owner-aligned after every other bank replacement.

#### Proof

A one-point union of forests is a forest.  Complementary core/bank root
status makes the displayed union cover every root and every private vertex exactly once, so
\(M_U\) is perfect and hence unique.  For pending \(t\), disjointness of
the banks gives \(F_t\subseteq M_t^0\subseteq M_U\). \(\square\)

Equal root status is load-bearing.  The two leaf forests

\[
 \Gamma_0=\{g_1c_1,g_2c_2\},\qquad
 \Gamma_1=\{g_1c_2,g_2c_1\}                        \tag{5.2}
\]

each have a unique perfect matching, but the prospective later port
\(g_2c_2\) is owner-aligned only in \(\Gamma_0\).  Thus root-time owner
alignment plus leaf-peelability of every endpoint does not imply dynamic
preservation.

### Theorem 5.2 (private coherent collar tree)

Let \(S\) be a component-spanning tree of \((I,M)\)-private coherent
collars.  If \(\Gamma_I\) is a forest, the collars have matching privacy
with the matching-seam state of Lemma 5.1, and their occurrence paths have
route privacy, then every ordering of \(S\) is an accepted
fixed-decoration transparent merge list.

#### Proof

A forest has at most one perfect matching.  The leaf-forest owner theorem
therefore says that all forced lower ports extend if and only if
\(F(S)=\bigcup_{t\in S}F_t\subseteq M\), which is built into the collar
definition.  The selected upper ports already lie in \(I\), so
\(\mathcal D(I,M)\) is the one common decoration.

At a prefix \(U\), Lemma 5.1 gives the transported unique matching \(M_U\)
of that same occurrence-labelled decoration and puts every pending
\(F_t\) inside \(M_U\).  Thus owner alignment is preserved dynamically,
not merely checked at the root.

Coherence makes every selected hexagon transparent for that decoration.
The fixed occurrence paths are pairwise vertex-disjoint, so the sources of
the component tree are simultaneously linkable; equivalently, deleting
\(Y\) destroys at most \(|Y|\) selected tree paths and leaves at most
\(|Y|+1\) component pieces.  The H0--H5 product hypotheses now let item
2189 execute every ordering. \(\square\)

### Lemma 5.3 (off-forest zero-flux replacement)

If \(\Gamma_I\) is not a forest, owner alignment in Theorem 5.2 may be
replaced, for the matching row only, by pairwise vertex-disjoint blocks
\((G_t,C_t,F_t)\) satisfying

\[
 |G_t|=|C_t|=3,\qquad F_t:G_t\longrightarrow C_t\text{ bijective},
 \qquad M(G_t)=C_t.                                  \tag{5.3}
\]

Then all forced ports lie in one perfect matching.

#### Proof

On each block, replace \(M|_{G_t\cup C_t}\) by \(F_t\).  Both are perfect
matchings of the same six vertices, and disjoint blocks may be replaced
simultaneously. \(\square\)

This lemma closes only the matching row.  It does not make the nonforest
gap topology leaf-peelable; the remaining H3 topology must still be proved.
Equivalently, the general extension is a packing of vertex-disjoint
\(M\)-alternating cycles.

### Theorem 5.4 (fixed-coordinate cylinder preservation)

Let \(P\) be fresh, disjoint from the entire old coordinate ground,
and lift every occurrence and colour by \(X\mapsto X\cup P\).  The lift of
an \((I,M)\)-private coherent collar is private coherent for the lifted
data, provided:

1. the lifted transversal consists exactly of the images of \(I\), so no
   new selected upper point subdivides an old gap;
2. the occurrence router has an injective network embedding and different
   child/router images remain disjoint; and
3. the non-decoration H0--H5 guards are lifted with the collar.

#### Proof

The lift preserves cyclic occurrence order, hence induces a graph
isomorphism

\[
               \Gamma_I\longrightarrow\Gamma_{I^P}.                \tag{5.4}
\]

It sends \(M\) to the lifted matching, unique when \(\Gamma_I\) is a
forest, and sends every forced owner
edge \((g,c)\) to \((g,c\cup P)\).  Thus owner alignment, disjoint private
blocks and zero flux are preserved.  A coherent core
\((H;a,b,c;d,e)\) becomes \((H\cup P;a,b,c;d,e)\), so the common external
labels and both forced colour triples lift injectively.  Finally, the
assumed router-network embedding, rather than set union alone, sends each
route injectively and keeps different route images disjoint. \(\square\)

Consequently cylinder lifting preserves existing private collars.  It does
not create the new bridge collars between Pascal children.  The exact
recursive supply gate is therefore:

> find, at every Pascal node, enough component-faithful coherent bridge
> collars whose forced lower ports use fresh matched owner edges and whose
> occurrence transfers use fresh node-private routes.

Once those bridges exist, Theorems 4.1 and 5.2 close the induction.

Literal boundary order is essential.  Two child systems consisting of the
single matched edges \(u_1c_1\) and \(u_2c_2\) are separately
owner-aligned.  But in the parent cyclic order

\[
                         u_1,c_1,c_2,u_2                            \tag{5.5}
\]

with upper transversal \(\{u_1,u_2\}\), one gap contains both lower
colours and the other is empty, so the parent gap graph has no perfect
matching.  Thus disjoint child cylinders compose only after proving the
literal residual-gap direct sum or inserting an explicit zero-flux boundary
tube.  Their lifted upper-colour images must likewise be globally disjoint
and exhaustive.

### Proposition 5.5 (exact joint-selection obstruction)

For each desired scaffold edge \(e\), let \(\mathcal H_e\) be its candidate
private collars.  Record separately the matching resource set \(B(h)\) and
the router resource set \(R(h)\) of a candidate.  Selecting the private
tree is exactly the colourful packing problem

\[
 h_e\in\mathcal H_e,qquad
 B(h_e)\cap B(h_f)=R(h_e)\cap R(h_f)=\varnothing
 \qquad(e\ne f),                                    \tag{5.6}
\]

together with the declared physical-support conflicts.

Separate matching and route selectors need not combine.  The smallest
one-corner obstruction already has two tasks.  Let the first have only a
candidate with signature \((A,x)\).  Let the second have the three
signatures \((A,x),(A,y),(B,x)\), but not \((B,y)\), where \(A,B\) are
disjoint matching blocks and \(x,y\) are disjoint routes.  Matching
resources alone choose \((A,x),(B,x)\); route resources alone choose
\((A,x),(A,y)\); but every joint pair conflicts.  The absent rectangle
corner \((B,y)\) is exactly the missing physical collar.

Conversely, if every candidate family factors losslessly as

\[
                  \mathcal H_e=\mathcal B_e\times\mathcal R_e       \tag{5.7}
\]

and all compatibility is exactly block disjointness plus route
disjointness, any compatible selector from the \(\mathcal B_e\) and any
compatible selector from the \(\mathcal R_e\) combine coordinatewise.

#### Proof

The two-task obstruction is the displayed case check.  Under (5.7), the
chosen block and route for task \(e\) form an available candidate by
Cartesian closure; the two independent disjointness statements give (5.6).
\(\square\)

Thus colour/gap privacy and occurrence-route privacy are orthogonal, but
their **availability** may be correlated.  The first empty mode set in
Theorem 4.2 is an exact obstruction to that joint availability.  Raw counts
such as \(3(q-1)\le P_m\) and a route packing number at least \(q-1\) are
necessary but not sufficient.  Proving rectangle closure, parent-totality,
or a bounded-pressure selector for literal Pascal bridge collars is the
remaining constructive theorem.

## 6. ECO supply and the private hypertree gate

Use the paper parameter \(n\), so the canonical MMM factor lies in the
middle-levels graph on \(2n+1\) coordinates and its components are indexed
by plane trees with \(n\) edges.

The new coherent-ECO theorem gives two exact facts.

1. A standard MMM label

   \[
                        110u0v\longleftrightarrow101u0v             \tag{6.1}
   \]

   is all-six coherent if and only if \(u=\varnothing\).  The resulting
   standard coherent-label graph is disconnected for every \(n\ge5\).
2. For every Dyck parent \(D=1u0v\), the word

   \[
                              h(D)=1u000v0                         \tag{6.2}
   \]

   gives a coherent incidence hexagon on the three displayed zero
   positions, with common external labels \((d,e)=(2n,0)\); coordinate
   rotations give the other phases.  Every standard MMM pull adjacency is
   co-contained in one such ECO hyperedge already in this fixed rotation.
   Hence its coherent ECO component two-section is connected for every
   \(n\).

Thus coherent static abundance is closed.  The canonical standard-label
arborescence is not a coherent recursion, and the remaining problem is to
select a simultaneous private ECO hypertree.

### Definition 6.1 (component-faithful ECO hypertree)

For an ECO atom \(t\), let \(E_t\) be the set of factor components meeting
its three old matching edges and put \(\rho(t)=|E_t|-1\).  Choose a tree
\(R_t\) on \(E_t\), with every unit edge retaining its atom and unit label.
A selected atom family \(S\) is an ECO hypertree
when:

1. every \(|E_t|\ge2\), and the unit expansion

   \[
                              R=\bigcup_{t\in S}R_t                 \tag{6.3}
   \]

   is a tree on all factor components, with every unit edge retaining its
   atom label;
2. the physical hexagons are pairwise support-disjoint or have a certified
   commuting product cube; and
3. whenever \(t\) is pending, its toggle merges all current component
   blocks meeting \(E_t\) into one and splits no block.

Item 3 is automatic when the three old edges lie on three distinct current
cycles.  If two old edges lie on one cycle it is an additional literal
topology test.

### Theorem 6.1A (exact weighted hypertree cuts and one-anchor order)

For a selected positive-rank atom family \(S\), form its bipartite
component--atom incidence graph

\[
 B(V,S),\qquad vt\in E(B)\Longleftrightarrow v\in E_t.             \tag{6.3a}
\]

Then \(B(V,S)\) is a forest if and only if, for every nonempty
\(A\subseteq V\),

\[
 \boxed{
   \sum_{\substack{t\in S\\E_t\subseteq A}}\rho(t)\le |A|-1.}    \tag{6.3b}
\]

It is a spanning tree if and only if (6.3b) holds and

\[
                 \bigcup_{t\in S}E_t=V,
        \qquad \sum_{t\in S}\rho(t)=|V|-1.                       \tag{6.3c}
\]

Equivalently, after choosing any root component, the atoms admit an order
in which every next atom meets the components exposed so far in exactly one
vertex and introduces all its other support components.  In this case any
choice of a tree \(R_t\) on every \(E_t\) makes
\(\bigcup_tR_t\) a tree.  Conversely, a unit-expanded tree forces the
incidence graph to be a tree.

#### Proof

If the incidence graph is a forest, restrict it to the component vertices
in \(A\) and to atoms supported wholly in \(A\).  A nonempty forest on
those vertices has at most one fewer edge than vertices, which after
subtracting one atom vertex per atom is exactly (6.3b).  Conversely, a
cyclic incidence component with component shore \(A_0\) has at least as
many edges as vertices, giving
\(\sum_{E_t\subseteq A_0}\rho(t)\ge |A_0|\), contrary to (6.3b).
Thus (6.3b) is equivalent to acyclicity.  Under (6.3c), the incidence
forest has one fewer edge than vertices and covers \(V\), so it is
connected.

Root the incidence tree at the chosen component.  Ordering atom vertices
away from the root makes each atom have one previously exposed component
neighbour and all remaining component neighbours new.  Conversely, adding
one atom star at a time under this one-anchor rule preserves a tree.  Finally,
replacing each atom star by a tree on the same neighbours preserves
connectedness and gives exactly \(\sum_t\rho(t)=|V|-1\) unit edges; hence
the unit expansion is a tree.  The converse follows by the same count and
connectedness. \(\square\)

The weighted system is not a matroid when binary and ternary atoms are
mixed.  On components \(\{1,2,3\}\), the ternary atom \(123\) and the
binary family \(\{12,23\}\) are each incidence forests, but neither binary
atom augments the ternary family.  Thus ordinary graphic matroid
intersection does not solve the general selection problem.  In the purely
binary subfamily, (6.3b) is the usual graphic-forest cut system.

### Theorem 6.2 (private ECO hypertree execution)

Let \(S\) be a component-faithful ECO hypertree.  Suppose one upper
transversal \(I\) and base matching \(M\) make every atom owner-aligned,
the forced owner blocks are pairwise disjoint and export the matching-seam
state of Lemma 5.1, and every atom \(t\) exports \(\rho(t)\) named
vertex-disjoint occurrence channels for the unit edges of \(R_t\).  Assume
all these channels are mutually vertex-disjoint, end at distinct sinks,
avoid child router banks, and the remaining grouped product-cube, gap,
trace and reachability guards analogous to H0--H5 hold.  The exported state
must also identify each named channel with its named unit component edge,
so a surviving channel is semantically usable as that unit in the router
rank calculation; merely copying one all-or-none atom source \(\rho(t)\)
times is forbidden.  Then every ordering of \(S\) is a
fixed-decoration transparent component-spanning execution, with the
unit-expanded router state satisfying \(c(R_Y)\le |Y|+1\).

Here \(R_Y\) is the atom-edge-labelled auxiliary graph retaining a unit
edge exactly when its named channel avoids \(Y\).  If the prepared router
offers additional surviving channels, its actual unit graph is a supergraph
of \(R_Y\).

#### Proof

Consider a pending atom \(t\).  If two vertices of \(E_t\) had already
been joined by earlier atoms, the corresponding path in their unit trees,
together with the path between those vertices in \(R_t\), would form a
cycle in \(R\).  Hence the current blocks meeting \(E_t\) are distinct.
Component faithfulness makes the toggle merge them into one.  Induction in
any order follows, and connectedness of \(R\) gives one final component.

Owner alignment and disjoint owner blocks put every forced lower edge in
the same matching \(M\); the selected upper ports lie in \(I\).  Thus one
decoration marks every port.  The matching-seam state applies Lemma 5.1 on
every product-cube prefix, and coherence transports the decoration at every
toggle.
All \(|V(R)|-1\) named unit channels are vertex-disjoint.  Deleting \(Y\)
kills at most \(|Y|\) unit edges of the tree \(R\), proving the displayed
router inequality.  The prepared grouped physical signature executes each
hex once while carrying all \(\rho(t)\) channels, and preserves every
remaining guard. \(\square\)

When every \(|E_t|=2\), this is Theorem 5.2.  A three-component atom carries
two component-rank units and therefore needs two independent channels (or
an exact grouped two-source state).  Copying one source twice has rank one.
This grouped-rank condition is load-bearing even though the physical hex is
toggled only once.

### Theorem 6.2A (atomic weighted router alternative)

Suppose instead that the selected atoms have all-or-none router semantics.
Let \(B(V,S)\) be their incidence tree, and call \(t\) dead under a router
deletion \(Y\) exactly when its complete grouped occurrence transfer is no
longer executable.  Removing the dead atom nodes gives the exact backbone
identity

\[
             c(B_Y)-1=\sum_{t\ {\rm dead\ under}\ Y}\rho(t).       \tag{6.3d}
\]

Consequently this atomic backbone is router-resilient if and only if

\[
       \sum_{t\ {\rm dead\ under}\ Y}\rho(t)\le |Y|
       \qquad\text{for every }Y.                                  \tag{6.3e}
\]

A sufficient private certificate is a family of pairwise-disjoint reserved
router banks \(B_t\subseteq V(N)\) such that

\[
        t\text{ dead under }Y\Longrightarrow |Y\cap B_t|\ge\rho(t).
                                                                    \tag{6.3f}
\]

Under the same owner, matching-seam, physical-cube and component-faithful
hypotheses as Theorem 6.2, (6.3f) may replace its unit-separable channel
hypothesis.

#### Proof

An atom node \(t\) has degree \(|E_t|\) in the incidence tree.  Deleting it
increases the number of component-containing pieces by
\(|E_t|-1=\rho(t)\).  Atom nodes are never adjacent, so these increases add,
proving (6.3d) and hence (6.3e).  Under (6.3f), disjointness of the reserved
banks gives

\[
 \sum_{t\ {\rm dead}}\rho(t)
 \le\sum_{t\ {\rm dead}}|Y\cap B_t|\le |Y|.
\]

The remaining execution proof is that of Theorem 6.2 with the atomic
incidence backbone in place of independently surviving unit edges.
\(\square\)

For \(\rho(t)=2\), one private path gives only unit kill cost and does not
imply (6.3f).  The exact alternative is either two semantically independent
unit channels as in Theorem 6.2 or a grouped atomic failure cut of size at
least two.  Extra live catalogue atoms can reconnect pieces, so (6.3f) is
sufficient rather than necessary for the full catalogue.

### Corollary 6.3 (literal owner mask for ECO atoms)

For an ECO atom \(Z=(H;a,b,c;d,e)\), the leaf-forest owner test is exactly
the following, using the canonical old matching
\(L_aU_{ca},L_bU_{ab},L_cU_{bc}\):

\[
\begin{gathered}
 H+a,\ H+b,\ H+c\in I,\\
 \operatorname{owner}_M(g(H+a+b))=H-e+b,\\
 \operatorname{owner}_M(g(H+b+c))=H-e+c,\\
 \operatorname{owner}_M(g(H+c+a))=H-e+a.            \tag{6.4}
\end{gathered}
\]

After applying (6.4), retain only component-faithful atoms exporting
\(\rho(t)\) independent channels or an exact grouped rank-\(\rho(t)\)
state.  A unit-expanded hypertree closes the postrepair catalogue by
Theorem 6.2 only when its owner blocks and matching seams are pairwise
compatible, its channels are node-private or satisfy the certified weighted
laminar condition, and its physical product cube passes.  Under those
hypotheses no further abstract Hall or router optimization is needed.

### Theorem 6.4 (one path forest controls all local ECO collisions)

Restrict to the fixed-rotation atoms \(D=1u0v\).  The physical-port
collision graph and the two forced-owner-colour collision graphs are the
same graph.  It is the directed path forest with edges

\[
              D=1p100v\longrightarrow D'=1p010v,                   \tag{6.5}
\]

where \(p,v\) are Dyck words of total semilength \(n-3\).  It has exactly
\({\rm Cat}_{n-2}\) edges.  Consequently one independent set in this
single forest simultaneously eliminates all physical-port collisions and
all repeated forced owner colours on both shores.

#### Proof

The exact ECO word comparison shows that equality is possible only between
the role-b port of \(D\) and the role-a port of \(D'\).  Unique Dyck
factorization gives (6.5); the same equality controls the corresponding
owner words on both shores.  The move shortens the first child forest and
has at most one predecessor and successor, so the graph is an acyclic graph
of maximum degree two.  Catalan convolution counts its edges by the pairs
\((p,v)\), giving \({\rm Cat}_{n-2}\).  Every path forest has an
independent set meeting alternating vertices of each path. \(\square\)

This theorem closes the local collision packing, not the owner problem.
Distinct forced faces need not extend to a complete upper transversal, and
an independent set need not retain a spanning component hypertree.

### Corollary 6.5 (exact local-channel reduction)

Orient each edge of the collision path forest to the atom which owns its
shared old factor edge, and remove that edge's two port vertices from the
other atom's **port set**.  The resulting residual port sets are pairwise
disjoint, and every atom loses vertices on at most two old factor edges.
Assume in addition that this port ownership extends to reserved occurrence-
router vertex sets

\[
                   B_t\subseteq V(N),\qquad B_t\cap B_s=\varnothing
                   \quad(t\ne s),                                  \tag{6.6a}
\]

and that every channel assigned to \(t\) lies wholly inside \(B_t\).
Under this additional network-private hypothesis, the entire node-private
routing row reduces to the local statement:

> after any prescribed subset of those at most two shared edges is assigned
> away, atom \(t\) supplies \(\rho(t)\) vertex-disjoint unit occurrence
> channels inside its residual owned bank, to distinct local sinks and
> avoiding every child router bank.

If this local statement holds for the selected hypertree, all channels are
globally disjoint and Theorem 6.2 closes routing.

#### Proof

Every atom has at most one predecessor and one successor in the path
forest.  Assigning each shared edge to one endpoint removes all cross-bank
**port** overlap and removes at most two edges from one atom.  Hypothesis
(6.6a), not the port theorem alone, puts the local channels in disjoint
router banks.  Their union is therefore globally vertex-disjoint.
\(\square\)

Genealogy proves neither (6.6a) nor the displayed local statement: two
disjoint residual port sets can still be embedded in a prepared occurrence
router through one public bottleneck.  Thus Corollary 6.5 is a conditional
reduction after a literal router-bank export, not a consequence of the ECO
collision census by itself.

### Proposition 6.6 (why connected two-section is insufficient)

The hypergraph with edges \(\{1,2,3\}\) and \(\{1,2,4\}\) has connected
two-section, but both edges are needed to span four vertices and their
incidence graph contains the cycle

\[
                  1-E_1-2-E_2-1.                                  \tag{6.6}
\]

Both hyperedges have rank two, so any unit expansion has four edges on four
vertices and cannot be a tree.  Thus it has neither a spanning
incidence-tree subfamily nor a unit-expanded hypertree.  Likewise, owner
masking may delete every ECO atom crossing some component cut, and route
privacy may make all surviving crossing atoms mutually incompatible.

#### Proof

Deleting either displayed hyperedge isolates vertex \(3\) or \(4\), while
keeping both gives (6.6).  The two latter assertions are obtained by
intersecting the static ECO bank with the owner predicate (6.4) and then
with the route/physical conflict system. \(\square\)

This is a scoped obstruction to the unit-expanded hypertree architecture, not a
no-go to a more general ordered hypergraph braid.  The authoritative finite
ECO audit finds pairwise vertex-disjoint coherent hypertrees whose combined
switch is Hamiltonian for \(3\le n\le7\); it does not certify owner
alignment or routes and is not an all-\(n\) proof.

### Theorem 6.7 (raw canonical ECO recursion fails first at project \(m=5\))

For paper parameter \(n=4\), the canonical factor has three components and
45 physical ECO atoms.  Every minimal topology-safe ECO Hamiltonization
uses two reducing atoms.  Across all 648 legal ordered sequences, hence 324
distinct endpoints, the two atoms already have disjoint six-port sets and
disjoint forced faces on both shores.  Nevertheless every endpoint has
only 81 of the required 84 turn colours on each shore, missing

\[
 \{219,365,438\}\quad\text{and}\quad\{73,146,292\}.                 \tag{6.7}
\]

Therefore no upper transversal exists, before a gap forest or owner
alignment can be formed.

#### Proof

This is the exhaustive literal theorem of
MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md.
Its replay constructs the canonical factor, all ECO atoms, every legal
two-step component reduction and both endpoint turn palettes.  The two
missing triples in (6.7) are complementary period-three rotation orbits.
\(\square\)

The conclusion is deliberately architecture-specific: it closes the
unrepaired canonical minimal-ECO recursion, not a preliminary neutral
packet, a repaired factor, a longer braid, or a nonforest owner exchange.

### Theorem 6.8 (repair-first ECO integration is exact at project \(m=5\))

At project \(m=5\) (paper parameter \(n=4\)), apply the authenticated
synchronized three-\(C_{10}\) repair and remove the two old standard glues.
The resulting pre-glue factor has two components of orders \(120\) and
\(132\), one transported \(84+84\) occurrence decoration, a forest gap
graph with a unique perfect matching \(M\), and a forest binary trace.

All five fixed-rotation ECO atoms retain their three old factor edges, are
vertex-disjoint from the repair packet, meet both components, and toggle the
factor to one Hamilton cycle.  Exactly the four parents

\[
                 110100,\qquad110010,\qquad101100,\qquad101010   \tag{6.7a}
\]

have all six ports in the transported decoration and satisfy the pointwise
owner equations (6.4).  Toggling any of them preserves the same two
palettes, forest gap graph, unique matching, and trace forest.  The atom
\(101100\) is isolated in the fixed-rotation support-conflict graph and
recovers a known standard repaired endpoint.  The atom \(110100\) gives a
second witness whose Hamilton endpoint lies outside the four-state
two-standard-glue cube.

Hence the repaired endpoint contains a literal collision-free,
owner-aligned, component-faithful one-atom ECO hypertree.  This finite
toggle is unconditional; no abstract router theorem is needed to verify
its executed endpoint.

#### Proof

The literal reconstruction and independent replay in
MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md
give the component orders, decoration, unique matching, trace, all five
support-disjoint component merges, the four owner-aligned rows in (6.7a),
and the endpoint separation.  With two factor components, one binary ECO
atom has incidence graph consisting of two component vertices joined
through one atom vertex, hence is an incidence tree and satisfies
Theorem 6.1A with total rank one.  Direct endpoint replay proves the
decoration-preservation assertion. \(\square\)

The theorem supplies the first obstructed finite base for the prescribed
order.  It does not produce a uniform repair packet, a recursive private
router bank, a rank-two atom channel, residence/deeper-shadow preservation,
or the compiler.

### Theorem 6.9 (state-expanded path-backbone compiler)

Fix a repaired factor whose components have an order
\[
                         v_0,v_1,\ldots,v_N.                       \tag{6.7b}
\]
For every cut \(i\), let \(\Sigma_i\) be a finite set of literal boundary
states.  A state records every object which may still interact with the
unprocessed suffix: the occurrence-labelled matching transfer, exposed
owner pins, router terminals and ownership state, and any residence,
shadow, socket/voltage or compiler boundary data in scope.

An allowed labelled transition \(t\) has endpoints
\[
                     (a_t,\sigma_t^-)\longrightarrow
                     (b_t,\sigma_t^+),\qquad b_t-a_t\in\{1,2\},  \tag{6.7c}
\]
and carries one binary or ternary ECO atom whose component support is the
consecutive block
\(\{v_{a_t},\ldots,v_{b_t}\}\).  Require:

1. the atom is a literal component-faithful coherent merge on that block,
   all its ports are owner-aligned in the exported decoration, and its local
   transition from \(\sigma_t^-\) to \(\sigma_t^+\) is exact;
2. equality of consecutive boundary states is a sufficient gluing rule:
   internal resource banks of distinct transitions are pairwise disjoint
   and avoid every still-unprocessed bank, every pending atom remains
   available, and every cross-cut obligation is represented in the common
   state; and
3. its router export is either unit-separable of rank \(b_t-a_t\), or is
   atomic with a private bank of kill cost at least \(b_t-a_t\).  All unit
   channel banks and atomic banks used on one accepted path are mutually
   disjoint.

Make the acyclic state graph \(\mathcal A\) with vertices
\((i,\sigma)\), \(\sigma\in\Sigma_i\), and one arc (6.7c) for every
allowed transition.  Then the following are equivalent.

1. There is an accepted repair-exported **left-to-right interval-tiling**
   ECO execution from a declared initial state \((0,\sigma_{\rm in})\) to
   some \((N,\sigma_{\rm out})\) in a declared accepting set; its successive
   tile intervals partition all component-path edges.
2. The graph \(\mathcal A\) contains such a directed source--accepting path.
3. The corresponding source--accepting unit-flow system is feasible.

Moreover, the flow polytope is integral.  Every integral path tiles every
component-path edge exactly once, preserves the complete carried boundary
state by induction, and satisfies router resilience under Item 3.

#### Proof

Project an arc (6.7c) to the interval of component-path edges
\(\{a_t+1,\ldots,b_t\}\).  A directed source--sink path in
\(\mathcal A\) has consecutive endpoints and therefore partitions
\(\{1,\ldots,N\}\) into intervals of lengths one and two.  The ordinary-tree
tiling theorem makes its atom incidence graph a tree.  Component
faithfulness executes the tiles in path order.  Exact equality of boundary
states and Item 2 give, inductively, the one transported decoration and all
declared RSB/compiler guards.

Conversely, read the successive cut states of any accepted path-backbone
execution.  Each executed tile is one allowed arc, so these states form a
directed source--accepting path in \(\mathcal A\).  Equivalence with the
unit-flow system and integrality follow from the incidence matrix of a
directed acyclic graph.  Finally, replace each unit-separable atom node by
its labelled unit tree and retain every all-or-none atom as an incidence
node.  This hybrid backbone is a tree.  Under deletion \(Y\), its component
excess is
\[
 \#\{\text{killed unit channels}\}
   +\sum_{t\ {\rm dead\ atomic}}\rho(t).
\]
Disjoint unit channels charge the first term injectively to their unit
banks; (6.3f) charges the second term to the mutually disjoint atomic banks.
Cross-disjointness in Item 3 bounds the sum by \(|Y|\), proving router
resilience even when the path mixes the two semantics. \(\square\)

The theorem gives an exact finite cutwise test.  Put
\[
 R_0=\{\sigma_{\rm in}\},\qquad
 R_j=\{\tau:\exists\,i\in\{j-2,j-1\},\
       \sigma\in R_i,\ (i,\sigma)\to(j,\tau)\in E(\mathcal A)\}.  \tag{6.7d}
\]
Indices outside \(\{0,\ldots,N\}\) are omitted.  Then an execution exists
exactly when \(R_N\) meets the accepting set.
This is stronger than the bare path-TU statement: owner, local-channel and
downstream boundary compatibility are incorporated before the flow is
solved, so no fractional or separately existential witnesses are combined.

It also gives a literal Pascal concatenation rule.  If two child path
transducers are accepting and a private bridge transition joins one
reachable left exit state to one co-reachable right entrance state, their
concatenation is accepting.  Its live width is at most
\[
             \max\{w_{\rm left},w_{\rm bridge},w_{\rm right}\}.
\]
If the bridge uses the same declared boundary alphabet, fits the child
width, and exports no additional persistent resource, this equals the child
maximum.  Requiring this bridge relation to be parent-total is a convenient
strong recursive invariant, but the exact condition is only nonempty
intersection of the reachable and co-reachable boundary-state sets.

This path-backbone face is not without loss of generality.  On
\(K_{1,3}\), the three ternary tiles covering the three pairs of arms have
matrix
\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
 \qquad\det=2,                                                     \tag{6.7e}
\]
whose unique fractional cover is \((1/2,1/2,1/2)\) and which has no
integral cover.  Thus the first branch already needs an additional integral
choice or a rethread which linearizes the component backbone.  The common
ECO collision path is a path on atom labels, not the component path
(6.7b), and does not supply this linearization.  This is an obstruction
only to the displayed three-ternary-tile exact-cover matrix and to naive
branching TU.  Additional binary or other tiles, a different ordinary
backbone, or a non-ECO braid may restore integrality.

The exact new all-\(m\) lemma is therefore sharply constructive:

> after the controlled repair, export a component path and a bounded-width
> state graph \(\mathcal A\) satisfying Items 1--3 and (6.7d), with the
> accepted terminal state carrying the downstream RSB/compiler interface.

The repaired \(m=5\) singleton is the one-arc base for the central
component/owner and compiled rank-one channel coordinates.  No accepting
downstream RSB/compiler state has been exported for it.  Neither the raw ECO
supply nor the current Pascal recursion proves the full export for all
\(m\).

### Theorem 6.10 (central decoration may be postponed until after gluing)

For the middle-levels-resolvable **central CLMT** only, let Stage A be any
pairwise-disjoint strict ECO incidence hypertree which Hamiltonizes the
starting factor.  No coherence, turn decoration, forced owner matching, or
occurrence router is required during this explicit gluing stage.

Let Stage B be the assertion that some Hamilton cycle of
\({\rm ML}(2m-1)\) has one joint alternating upper/lower turn SDR and lies
on the binary-trace forest face.  Then Stage A followed by a finite
alternating-circuit packet produces a central Catalan linear matching.
Indeed, the packet exists from **any** Stage-A Hamilton cycle if and only if
Stage B holds.

#### Proof

Strict component faithfulness and the incidence-tree rank identity make the
disjoint ECO toggles reduce the factor to one degree-two component.  For any
Stage-A Hamilton cycle \(C_0\) and terminal decorated Hamilton cycle \(C_*\),
the red/blue graph \(C_0\mathbin\triangle C_*\) has equal red and blue degree
at every vertex.  It decomposes into edge-disjoint alternating circuits.
Toggling them successively preserves degree two and reaches \(C_*\);
intermediate factors need not be Hamiltonian or decorated.  The
decorated-middle-levels theorem, including its binary-trace alternative,
lifts \(C_*\) to the Catalan linear matching.  The reverse implication
reads the terminal cycle. \(\square\)

Thus the weakest exact missing theorem in this central sufficient route is

\[
 \boxed{\operatorname{DHC}(m):
 \text{ some ML}(2m-1)\text{ Hamilton cycle has a joint alternating SDR}
 \text{ on the forest trace face}.}                  \tag{6.7f}
\]

It is not enough that the two turn maps are separately surjective.  The
audited \({\rm ML}(7)\) counterexample has both rainbows but all
\(12{,}288\) upper SDRs fail gap Hall; one incidence-hex toggle repairs it.
Around the repaired positive cycle, the exact census is 31 alternating
hexes, 16 Hamilton outputs, 10 decorable outputs, and six Hamilton toggles
whose source/output pair admits at least one common forest-side decoration.
The fixed-decoration transparent criterion—equality of the two local
selected turn multisets plus alternation of retained boundary mark
types—is needed only when the repair-first route insists on transporting
the same decoration.

At project \(m=5\), Stage A is literal: the disjoint fixed-rotation atoms
\(101010\) and \(101100\) Hamiltonize the canonical component profile
\(36+72+144\).  Stage B is the authenticated three-\(C_{10}\) packet,
whose terminal Hamilton cycle has complete \(84+84\) palettes, a unique
gap-forest matching, and a forest trace.  The ECO and \(C_{10}\) supports
are disjoint, so the finite packet also commutes, although this commutation
is not used by the general implication.

Theorem 6.10 is weaker than the private-collar architecture on the gluing
coordinate and stronger in what it asks of the terminal packet: the latter
must construct the decoration after all glues.  It does not preserve
residence, deeper shadows, sockets/voltage or compiler state.  It also does
not assert that every abstract CLMT is middle-levels-resolvable.  For the
full contiguous-OR problem, either Stage B must be strengthened to an
RSB/compiler-compatible terminal theorem or the repair-first preservation
route remains necessary.

The repair-first private-collar order is

\[
 \boxed{
 \text{controlled repair/rethread}
 \longrightarrow\text{ collision-free ECO hypertree}
 \longrightarrow\text{ owner-aligned residual matching}
 \longrightarrow\text{ private/laminar occurrence routing}.}       \tag{6.8}
\]

For central existence alone, Theorem 6.10 permits the weaker order

\[
 \boxed{\text{raw strict Hamiltonization}
        \longrightarrow\text{ terminal joint-decoration repair}.} \tag{6.9}
\]

The exact remaining supply statement is now:

> after a controlled zero-debt repair, choose a collision-free,
> component-faithful ECO family satisfying the weighted cuts
> (6.3b)--(6.3c); then produce one leaf-peelable
> \((I,M)\) satisfying (6.4) and the matching-seam state of Lemma 5.1,
> followed on the same physical atoms by either semantically independent
> unit channels or atomic private failure cuts satisfying (6.3f).

Equivalently, in the finite grammar of Theorem 4.2, the ECO bridge relation
must be parent-total after the owner, topology and route masks.  The first
empty mode set is the exact architecture-specific obstruction.  Static
coherent-edge abundance is no longer the open row.  The local router
condition for a fixed atom/ownership state is the integral vertex-split
max-flow test of the exported local-channel theorem; the missing work is to
construct that network export recursively, not to infer it from the Dyck
word.

## 7. Rethread and merge certificates are different types

For a factor-safe local switch \(t\), put

\[
                 \Delta\kappa(t)=\kappa(F_t)-\kappa(F),              \tag{7.1}
\]

where \(F_t\) is its endpoint factor.

* A **binary merge certificate** has \(\Delta\kappa=-1\), is oriented
  between two distinct prepared components, and may contribute an edge to
  \(K\).
* A **faithful ECO hypermerge** meeting \(r\) current blocks has
  \(\Delta\kappa=-(r-1)\) and may contribute one atom to the incidence
  hypertree of Theorem 6.2.  It is not one rank-one edge of \(K\).
* A **rethread certificate** has \(\Delta\kappa=0\).  It may alter the
  chronology, decoration, sockets or the later merge catalogue, but it is
  not a component-tree edge.
* A **split certificate** has \(\Delta\kappa=+1\) and cannot occur in the
  ordered component-reducing list.

### Lemma 7.1 (stage separation)

Let a debt-carrying packet of rethreads and/or split--merge circuits end at
an accepting prepared state \(\mathscr S\).  If the packet changes
\(F,N\), or the admissible decoration face, any coherent merge labels to be
used later must be recomputed at \(\mathscr S\).  Concatenating the accepted packet with a
catalogue certified by Theorem 2.1 or 3.1 is valid.  Counting a neutral
rethread or an uncompensated split as an edge of the later component tree
is invalid.

#### Proof

The router-resilience and forced-port theorems are statements about one
fixed prepared factor, admissible-decoration face and linkage network.  A switch with
\(\Delta\kappa=0\) supplies no decrease in the component partition, while a
switch with \(\Delta\kappa=+1\) moves it in the wrong direction.  Their
only legitimate recursive use is inside the preceding packet, whose final
state becomes the new ground on which \(K\), \(N\), coherence and forced
ports are evaluated.  Once that packet is accepted, Theorem 2.1 supplies a
later binary merge list, or Theorem 6.2 supplies a prepared ECO hypertree
execution.  Ordinary concatenation proves the positive statement.
\(\square\)

## 8. Exact finite calibration

The repaired positive \({\rm ML}(7)\) cycle has six shared-decoration
transparent Hamilton-to-Hamilton rethreads.  Four lie on the all-six
coherent face and two are all-zero-marked.  They calibrate local coherence
and decoration transport, but \(\Delta\kappa=0\), so none is evidence for
coherent component-edge supply.

All fifteen component-splitting toggles of that repaired cycle have zero
common componentwise decorations.  The independent replay also finds zero
palette-compatible common decorations, although the frozen scope JSON
records only the former count.  They cannot be reversed into a
fixed-decoration merge certificate without first preparing a different
decorated split endpoint.

The separate standard-factor fixture of handoff item 2171 supplies the
genuine positive \(m=4\) component merge with a common leaf-peelable
decoration and private attachment path.  It is the correct merge base.
These fixtures prove different coordinates and must not be combined into a
single fictitious certificate.

The coherent-ECO theorem independently supplies a connected component
two-section in every dimension and pairwise-disjoint Hamiltonizing
hypertrees through \(n=7\).  Those finite hypertrees have not been audited
for the owner mask or occurrence routes, so they do not replace the item
2171 private merge calibration.

The raw canonical project-\(m=5\) census is the sharp negative calibration:
all 648 minimal ECO sequences already pass port and forced-face
disjointness, yet every endpoint misses the same period-three three-colour
orbit on each shore.  The failure is global palette preparation, not local
collision packing.

Theorem 6.8 is the matching positive calibration.  After the synchronized
three-\(C_{10}\) preparation, the pre-glue state has two components and one
unique owner forest.  All five fixed-rotation ECO atoms survive, and four
are simultaneously all-six marked and pointwise owner-aligned.  Either the
isolated standard atom \(101100\) or the nonstandard atom \(110100\)
Hamiltonizes while preserving the accepting decoration.  Thus
\[
 \text{repair}\longrightarrow\text{private owner-aligned ECO glue}
\]
is exact at the first raw-obstructed dimension.  This closes neither the
uniform repair export nor the recursive occurrence-channel row.  The
separate exported-state audit does verify a literal rank-one route
\(s_{g1}\to z_{g1}\) for the repaired atom \(g1=Z(101100)\); this is a
finite singleton channel, not an all-\(m\) local-channel construction and
not evidence for the first rank-two atom.

## 9. Exact all-\(m\) catalogue target

There are now two different targets.

For the weakest middle-levels-resolvable **central** route, the exact
missing theorem is DHC(\(m\)) from (6.7f).  An undecorated Hamilton cycle is
already known, and Theorem 6.10 makes alternating-circuit realization
automatic once a terminal decorated Hamilton exists.  A raw disjoint ECO
hypertree or the path-backbone bank is therefore an optional canonical
Hamiltonization scaffold, not an additional logical gate for bare central
existence.  Separate turn rainbows do not imply DHC: joint gap Hall and the
binary-trace forest condition remain essential.

For the stronger repair-first route, or whenever downstream RSB/compiler
data must survive gluing, static coherent component incidence is no longer
missing but the exact postrepair lemma is:

> output one prepared leaf-peelable state \((F,I,M)\) for which the
> owner-masked ECO catalogue contains a component-faithful family satisfying
> the exact weighted hypertree cuts (6.3b)--(6.3c); its private matching
> banks export one common matching-seam state, its physical atoms form one
> commuting cube, and its occurrence transfers admit either unit-separable
> channels or atomic private failure cuts of weight \(\rho(t)\).

Theorem 4.2 turns this into a finite recursive target: zero-debt terminal
modes with parent-total ECO bridge relations after the owner, topology,
matching-seam and route masks.  Proposition 5.5 shows the sharp first
failure: Hall and route projections may each accept while one literal
rectangle corner is absent.  A sufficient local recursion theorem would be
conditional rectangle closure on one and the same terminal-mode assignment,
preserved by the fully isomorphic Pascal cylinder lift of Theorem 5.4.
The first empty bottom-up mode set is a finite architecture-specific
obstruction.  Theorem 6.1A supplies an independent exact topology
certificate: the first violated weighted cut is a literal incidence-cycle
obstruction.  The repaired project-\(m=5\) theorem supplies one positive
base mode, but no rule propagating it through every Pascal node.

On the strongest integral subclass, Theorem 6.9 replaces the mixed
hypertree master by one state-expanded path-flow.  Its exact missing input
is not another matching theorem: a repair must export the component path,
the literal owner/channel transitions, and one reachable accepting RSB
state.  A Pascal node composes when its child reachable/co-reachable state
sets meet one private bridge transition.  The determinant-two
\(K_{1,3}\) fixture proves that this path-backbone export cannot be assumed
for a general branching component tree.

Residence, deeper shadows, socket/voltage, and the common-\(Q\) compiler
remain separate entrance requirements and must be encoded in the terminal
modes if the grammar is used.  DHC by itself supplies none of them.  No
all-\(m\) decorated Hamilton theorem, owner-aligned/private-route ECO
hypertree, residence/deeper-shadow connector, compiler, or coefficient-one
theorem is claimed.

## 10. Authoritative inputs

This note uses the exact statements frozen in handoff items 2192 and 2195
and the subsequent coherent-ECO supply theorem:

* MATH_THEOREM_CATALAN_TRANSPARENT_ROUTER_RESILIENCE_CRITERION_20260731.md;
* MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md;
* MATH_THEOREM_CATALAN_FORCED_PORT_GAP_HALL_20260731.md;
* MATH_THEOREM_CATALAN_LEAF_FOREST_FORCED_PORT_OWNER_ALIGNMENT_20260731.md;
* MATH_THEOREM_CATALAN_PRIVATE_TREE_AUTOMATIC_HALL_AND_ROUTER_20260731.md;
* MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md;
* MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md;
* MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md;
* MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md;
* MATH_THEOREM_CATALAN_ECO_LOCAL_CHANNEL_EXPORTED_STATE_AND_FIRST_OBSTRUCTIONS_20260731.md;
* THREAD_A_CATALAN_ECO_PRIVATE_HYPERTREE_WEIGHTED_FOREST_CUTS_20260731.md;
* MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md;
* MATH_AUDIT_AD_ECO_COMPONENT_TREE_TILING_AND_BRANCH_OBSTRUCTION_20260731.md;
* MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md;
* MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md;
* MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md;
* MATH_THEOREM_K_RAW_ECO_HAMILTON_THEN_DECORATE_SEPARATION_20260731.md;
* the independently replayed repaired-\({\rm ML}(7)\) scope census.

The component-merging positive fixture is the separate item 2171 package.
