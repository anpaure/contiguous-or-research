# Cap-two diamond matchings: exact switch obstruction and gap-Hall rebase

Date: 2026-07-31  
Lane: R, Catalan linear matching and connector topology  
Status: exact alternating-switch calculus; explicit smallest obstruction to
universal forward/backward cycle-shift descent; exact gap-Hall and
transparent-hexagon scope; exact cap-two connectivity inside one fixed
middle-levels cycle; exact bounded-polygon linkage/gammoid state. No
all-\(m\) Catalan linear matching theorem is claimed.

## 0. Verdict

Let \(P\) be a perfect matching of the rank-\((m-1)\)/rank-\((m+1)\)
diamond graph and let \(F=\Psi(P)\) be its Johnson lift. Assume
\(\Delta(F)\le 2\). Both adjacent palettes are already exact; the remaining
local topology defects are the cycle components of \(F\).

The two canonical colour-preserving shifts of one cycle do not always open
it. An explicit \(m=3\) perfect matching below has one physical \(C_4\), but
both shifts add two incidences at each of two already occupied opposite
corners and raise both degrees from one to three. A different alternating
square repairs the same matching. Thus this is an obstruction to canonical
whole-cycle descent, not to the full alternating-circuit fibre.

For an arbitrary compound alternating switch, full forestification is
equivalent to three exact requirements:

1. delete an edge from every old cycle;
2. respect every middle-vertex degree-two capacity; and
3. after retained components are contracted, make the inserted-edge
   multigraph acyclic.

Requirement 3 means no new cycle. It means full acyclicity only when
requirement 1 also holds.

Inside one fixed middle-levels Hamilton cycle there is an earlier independent
gate: for a chosen upper occurrence SDR, the cyclic
gap-versus-lower-colour graph must have a perfect matching. Separate
surjectivity of both turn maps does not suffice. The first fixed-cycle
counterexample at \(m=4\) is nevertheless changed by one ordinary
incidence-hexagon toggle into a decorable cycle. That repairing toggle is
not transparent relative to the undecorable source, which has no decoration
to preserve. Starting from the positive repaired cycle, six further
Hamilton-preserving hexagons have common forest decorations and hence are
transparent for suitable supplied states. The recursive sufficient object
is therefore a joint alternating SDR plus a dynamically transparent gluing
tree.

There is also a complete positive connectivity theorem inside one fixed
middle-levels cycle. Its turn-augmentation graph is bipartite, so its
perfect matchings are connected by ordinary alternating circuits. Every
intermediate matching is again a decoration and hence has a cap-two physical
lift. Forest reachability in this fixed fibre is therefore equivalent to
forest existence, which is automatic when \(\operatorname {Cat}_m\) is odd
and otherwise is decided exactly by same-type forced-pair Hall tests. This
does not imply that compatible states exist at all nodes of a recursive
gluing tree.

For a nontransparent Hamilton-safe (2t)-polygon, the common augmented
trace graph has deficiency at most (e+3t) from a parent of deficiency
(e), and at most (e+2t) in the literal simple-circuit turn graph. Repair
is exactly a vertex-disjoint directed augmenting linkage of
that bounded width. The width is finite, but the paths can traverse the
whole graph; a recursive proof must carry their full bounded-adhesion
linkage signature jointly with the gap-forest and socket/voltage states.

## 1. Diamond matchings and cycle rank

Let \(|\Omega|=2m\), and put

\[
 {\cal L}=\binom{\Omega}{m-1},\qquad
 {\cal X}=\binom{\Omega}{m},\qquad
 {\cal U}=\binom{\Omega}{m+1}.
\]

The diamond graph \(B_m\) is bipartite on
\({\cal L}\sqcup{\cal U}\), with \(L\sim U\) iff \(L\subset U\).
For \(e=(L,U)\), where \(U\setminus L=\{a,b\}\), define

\[
                         \psi(e)=\{L+a,L+b\}.          \tag{1.1}
\]

For a finite multigraph \(G\), retaining loops and parallel edges, write

\[
                         \beta(G)=|E(G)|-|V(G)|+c(G), \tag{1.2}
\]

where \(c(G)\) counts connected components, including isolated vertices.
Thus \(\beta(G)=0\) exactly when \(G\) is a forest.

## 2. Exact compound alternating-switch theorem

Let \(P,P'\) be perfect matchings of \(B_m\). Their symmetric difference is
a vertex-disjoint union of \(P\)-alternating even circuits. Put

\[
 A=\Psi(P\setminus P'),\qquad
 B=\Psi(P'\setminus P),\qquad
 F_0=\Psi(P)-A.                                      \tag{2.1}
\]

Contract every connected component of \(F_0\) and retain one multiedge for
every edge of \(B\). Call the result \(\Gamma(P,P')\); an inserted edge
whose ends lie in one retained component becomes a loop.

### Theorem 2.1 (degree and cycle-rank identities)

For every middle vertex \(x\),

\[
 d_{\Psi(P')}(x)=d_{F_0}(x)+d_B(x),                  \tag{2.2}
\]

and

\[
 \boxed{\beta(\Psi(P'))=\beta(F_0)+\beta(\Gamma(P,P')).} \tag{2.3}
\]

Consequently, when \(\Delta(\Psi(P))\le 2\), the new lift is a spanning
linear forest if and only if:

1. \(A\) meets every cycle component of \(\Psi(P)\);
2. \(d_{F_0}(x)+d_B(x)\le 2\) for every \(x\in{\cal X}\); and
3. \(\Gamma(P,P')\) is a forest, with no loop or parallel two-cycle.

Both adjacent palettes remain exact automatically.

#### Proof

Equation (2.2) is the literal deletion/addition identity. Components of
\(F_0+B\) are in bijection with components of \(\Gamma\), so

\[
\begin{aligned}
 \beta(F_0+B)
 &=|E(F_0)|+|B|-|V(F_0)|+c(\Gamma)\\
 &=\bigl(|E(F_0)|-|V(F_0)|+c(F_0)\bigr)
   +\bigl(|B|-c(F_0)+c(\Gamma)\bigr),
\end{aligned}
\]

which is (2.3). In a cap-two graph, deleting from every cycle component is
equivalent to \(F_0\) being a forest. The three conditions now follow from
(2.2)--(2.3). Finally, \(P'\) is a perfect matching on the same two shores,
so both typed colour maps remain bijective. \(\square\)

### Corollary 2.2 (exact global obstruction and scope)

For a fixed cap-two matching \(P\), failure of forestification by one
arbitrary compound switch is exactly:

> every \(P\)-alternating even subgraph which cuts all old cycles violates a
> middle capacity row or creates a circuit after retained components are
> contracted.

If one arbitrary compound switch is allowed with no restriction on
intermediate states, the assertion that every matching can be switched to a
forest is equivalent to the Catalan Linear Matching assertion itself. Given
one forest matching \(Q\), toggle all components of \(P\triangle Q\).
The stronger statement that every component of the cap-two reconfiguration
graph contains a forest matching remains open.

## 3. Forward/backward shifts and the descent ledger

Let \(C=X_0X_1\cdots X_{r-1}X_0\) be a cycle component of
\(F=\Psi(P)\). Write

\[
 L_i=X_i\cap X_{i+1},\qquad
 U_i=X_i\cup X_{i+1}\quad(i\bmod r).                 \tag{3.1}
\]

The forward and backward matchings replace the diamonds on \(C\) by

\[
                 (L_i,U_{i+1})\qquad\hbox{or}\qquad(L_i,U_{i-1}), \tag{3.2}
\]

respectively. These are containments because
\(L_i\subset X_{i+1}\subset U_{i+1}\) forward and
\(L_i\subset X_i\subset U_{i-1}\) backward. They retain every lower colour
and cyclically permute the same upper colours.

Delete \(E(C)\), put \(F_0=F-E(C)\), and let \(B_C^\varepsilon\) be the
new Johnson edges for sign \(\varepsilon\in\{+,-\}\). Let
\(\Gamma_C^\varepsilon\) be their multigraph after components of \(F_0\)
are contracted.

### Theorem 3.1 (one-cycle shift criterion)

The sign \(\varepsilon\) remains cap-two exactly when

\[
 d_{F_0}(x)+d_{B_C^\varepsilon}(x)\le 2
 \qquad(x\in{\cal X}).                               \tag{3.3}
\]

If (3.3) holds and \(c_{\rm cyc}(F)\) is the number of old cycle
components, then

\[
 \beta(F_0+B_C^\varepsilon)
   =c_{\rm cyc}(F)-1+\beta(\Gamma_C^\varepsilon).     \tag{3.4}
\]

Therefore:

- no new cycle is created exactly when \(\Gamma_C^\varepsilon\) is acyclic;
- under that condition the old cycle count drops by exactly one; and
- the output is a full forest exactly when \(C\) was the only old cycle.

Checking only the shifted edges is insufficient: retained paths must first
be contracted.

#### Proof

Apply Theorem 2.1. Since \(C\) is one entire component,
\(\beta(F_0)=c_{\rm cyc}(F)-1\). \(\square\)

### Theorem 3.2 (simultaneous sign-shift master)

Choose any family \({\cal D}\) of old cycle components and one sign for each.
Delete all their old edges and let \(S\) be the union of their middle
vertices. Every new shifted edge has one distinguished anchor in \(S\) and
one auxiliary endpoint; each \(x\in S\) anchors exactly one edge. Let
\(a(x)\) count auxiliary occurrences at physical vertex \(x\).

The simultaneous shift is cap-two exactly when

\[
 a(x)\le 2-d_{F_0}(x)-{\bf1}_{x\in S}
 \qquad(x\in{\cal X}).                               \tag{3.5}
\]

Orient each new edge from its anchor to its auxiliary component. Its
attachment multigraph is acyclic exactly when

\[
 \#\{e:\operatorname{anchor}(e),\operatorname{aux}(e)\in Q\}
       \le |Q|-1
 \qquad(\varnothing\ne Q\subseteq S).                \tag{3.6}
\]

If \({\cal D}\) contains all old cycles, (3.5)--(3.6) are necessary and
sufficient for a forest. If it contains only some, they certify no new
cycle and reduce old cycle rank by \(|{\cal D}|\), while untouched cycles
remain.

#### Proof

Equation (3.5) is (2.2), with one anchor incidence at every member of \(S\).
After contraction, vertices outside \(S\) have outdegree zero and vertices
inside \(S\) have outdegree one. In a finite digraph of outdegree at most
one, an undirected circuit exists exactly when there is a directed circuit;
an outside sink cannot lie on it. The graphic inequalities on arcs internal
to \(S\) are exactly (3.6). Apply (2.3). \(\square\)

A matching is canonical-shift locked if every old cycle and both signs fail
(3.3) or contracted acyclicity. This is the exact obstruction to even the
first monotone whole-cycle step.

## 4. Exact \(C_4\) opposite-corner obstruction

Let \(S\in\binom{\Omega}{m-2}\), and let \(a,b,c,d\notin S\) be distinct.
Set

\[
\begin{aligned}
 X_0&=S+a+c,&X_1&=S+b+c,\\
 X_2&=S+b+d,&X_3&=S+a+d,
\end{aligned}                                        \tag{4.1}
\]

and

\[
                         Y_0=S+c+d,\qquad Y_1=S+a+b. \tag{4.2}
\]

### Theorem 4.1 (private opposite corners are exact)

Suppose \(X_0X_1X_2X_3X_0\) is a cycle component of a cap-two perfect
diamond matching, and put \(F_0=F-E(C)\). Both its forward and backward
shifts use \(Y_0\) twice and \(Y_1\) twice. Consequently either shift is
cap-two if and only if

\[
                         d_{F_0}(Y_0)=d_{F_0}(Y_1)=0. \tag{4.3}
\]

When (4.3) holds, either shifted edge set is two disjoint two-edge paths and
is safe. If either opposite corner has one retained edge, both signs fail.

#### Proof

In cyclic order the forward edges are

\[
 X_1Y_0,\quad X_2Y_1,\quad X_3Y_0,\quad X_0Y_1.       \tag{4.4}
\]

The backward edges use the same auxiliary corners with the other adjacent
anchors. Thus each \(Y_j\) receives two incidences. The cycle vertices have
no retained incidence after deletion. This proves (4.3), and (4.4) proves
acyclicity when both corners are isolated. \(\square\)

## 5. A literal smallest shift-locked matching

Take \(m=3\), \(\Omega=\{1,2,3,4,5,6\}\), and match:

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
L&12&13&14&15&16&23&24&25&26&34&35&36&45&46&56\\ \hline
U&1234&1235&1245&1345&1236&2346&2456&1256&1246&1346&
2345&1356&3456&1456&2356.
\end{array}                                           \tag{5.1}
\]

Every containment is literal. Complements of the upper sets are

\[
56,46,36,26,45,15,13,34,35,25,16,24,12,23,14,
\]

which enumerate every pair; hence (5.1) is a perfect matching. Its lift has
the one cycle

\[
                         123-124-145-135-123          \tag{5.2}
\]

and the five path components

\[
\begin{gathered}
245-246-126-136-356-256-125,\qquad 234-236,\\
134-346,\qquad235-345-456-146,\qquad156.              \tag{5.3}
\end{gathered}
\]

Thus the lift is cap-two. In (4.1) take

\[
 S=\{1\},\qquad(a,b,c,d)=(3,4,2,5).
\]

The opposite corners are \(Y_0=125\), \(Y_1=134\), and

\[
                         d_{F_0}(125)=d_{F_0}(134)=1. \tag{5.4}
\]

Theorem 4.1 proves that both canonical shifts raise both degrees to three.

This is not a full-fibre obstruction. The alternating square

\[
 (12,1234),(13,1235)\longmapsto(12,1235),(13,1234)   \tag{5.5}
\]

replaces \(123-124,123-135\) by \(123-125,123-134\). The resulting five
paths are

\[
\begin{gathered}
245-246-126-136-356-256-125-123-134-346,\\
234-236,\qquad235-345-456-146,\qquad124-145-135,
\qquad156.                                            \tag{5.6}
\end{gathered}
\]

For \(m=2\), perfect matchings of
\(B_2=K_{4,4}\setminus\{(i,i)\}\) are derangements. A 4-cycle derangement
lifts to two paths. A product of two transpositions lifts to one \(C_4\)
whose two opposite corners are the two isolated middle vertices, so either
sign opens it. Thus \(m=3\) is the smallest locked dimension.

## 6. Middle-levels support: gap Hall and transparent gluing

Fix a Hamilton cycle of \({\rm ML}(2m-1)\):

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.                \tag{6.1}
\]

Its turn colours are

\[
 \ell_i=A_i\cap A_{i+1},\qquad u_i=B_{i-1}\cup B_i.  \tag{6.2}
\]

Choose one occurrence \(I\) of every upper turn colour. The selected
\(A\)-positions cut the cyclic \(B\)-positions into gaps. Join a gap \(G\)
to lower colour \(L\) when some \(j\in G\) has \(\ell_j=L\).

### Theorem 6.1 (gap-Hall gate)

The upper SDR \(I\) extends to alternating bijective upper/lower turn
representatives if and only if the gap-versus-lower-colour graph has a
perfect matching; equivalently,

\[
 \left|\{\ell_j:j\in\bigcup_{G\in{\cal S}}G\}\right|
       \ge |{\cal S}|                                  \tag{6.3}
\]

for every family \({\cal S}\) of \(I\)-gaps.

#### Proof

Alternation requires exactly one selected \(B\)-position in each gap, and
lower bijectivity requires their colours to be distinct. This is precisely
the stated perfect matching; (6.3) is Hall. \(\square\)

Separate surjectivity of \((u_i)\) and \((\ell_i)\) does not imply (6.3).
MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md
gives an \({\rm ML}(7)\) Hamilton cycle for which all \(12{,}288\) upper
SDRs fail, with best gap matching \(20/21\). This is a fixed-cycle failure,
not \(m=4\) nonexistence.

A shifted decorated matching need not remain supported on the same
middle-levels cycle. It does so exactly when every shifted diamond lies in
that cycle's same-rail-turn/cross-edge support. Conditional on this support
test, the resulting perfect matching uniquely reconstructs its decoration
and passes gap Hall. Outside it, no fixed-trace claim is valid.

Arbitrary Catalan linear matchings are not assumed middle-levels-resolvable:
the \(m=3\) forest in
MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md
has a forced middle-levels support of degree three.

### Theorem 6.2 (transparent hexagon transfer)

Let a standard incidence-hexagon toggle replace one alternating three-edge
matching of a middle-levels cycle by the other, and suppose both sides are
Hamiltonian. A fixed decoration survives if and only if:

1. the selected local turn-colour multisets agree before and after,
   separately on the two shores; and
2. after the three retained fragments are reconnected, the last marked shore
   type on each fragment is opposite to the first marked type on the next.

If a binary-trace breaker outside the six ports remains protected, both
physical diamond lifts are linear forests.

#### Proof

Only turn colours at the six ports change. The old selected palettes were
bijective, so they remain bijective exactly when their two typed local
multisets are restored. Marks already alternate inside each retained path,
including after reversal; only the three new boundaries can fail. A retained
trace breaker excludes the unique binary cycle face on both sides.
\(\square\)

MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
uses one ordinary incidence hexagon to turn the failed \(m=4\) cycle into
an explicit decorable cycle with \(\operatorname{Cat}_4=14\) paths. The
repair itself is not transparent: its source has no decoration. Starting
from the repaired positive cycle, 31 alternating hexagons are available;
16 outputs remain Hamiltonian, 10 are decorable, and 6 share a common
forest decoration with the positive source. Those six are the transparent
local atoms.

Relative to a supplied decorated state, every Hamilton-preserving hexagon
has an exact trichotomy. It is **transparent** when the same occurrences pass
Theorem 6.2; **repairable** when the new turn-augmentation graph has a perfect
matching, obtainable after deleting at most six invalid old matching edges
and making at most six Berge augmentations; and **Hall-blocked** otherwise.
A repaired matching may still lie on the exceptional physical cycle face,
so forest parity must be tested separately.

Thus the recursive sufficient object is a joint alternating SDR plus a
transparent gluing tree: preserve the two local palette multisets and three
boundary types at every gluing hexagon, merge all components, and retain a
trace breaker. An arbitrary frozen SDR and an arbitrary published gluing
tree are both too weak.

### Theorem 6.3 (exact cap-two connectivity in one fixed cycle)

Let \(H_C\) be the turn-augmentation graph of the fixed middle-levels cycle
\(C\). Let \(M,M^*\) be any two perfect matchings of \(H_C\). There is a
sequence

\[
                     M=M_0,M_1,\ldots,M_t=M^*        \tag{6.4}
\]

in which \(M_i\triangle M_{i+1}\) is one alternating even circuit of
\(H_C\). Every \(M_i\) is a perfect matching, hence every corresponding
diamond matching preserves both outer palettes and has a cap-two physical
lift supported by \(C\).

Consequently, from any supplied decoration of \(C\), a physical path-forest
decoration is reachable by such protected compound switches if and only if
one exists. Put \(K=\operatorname {Cat}_m\). More explicitly:

1. if \(K\) is odd, every decoration is already a path forest;
2. if \(K\) is even, a path-forest decoration exists if and only if the
   forced-pair graph \(H_C[p,q]\) is perfect-matchable for some two distinct
   same-type residual cycle edges \(c_p,c_q\).

Thus, in the even case, the exact fixed-fibre obstruction is a Hall
deficiency in every \(H_C[p,q]\). This is an exact obstruction to all
compound transitions whose endpoints remain in the same fixed-cycle
decoration fibre; it is not an obstruction to first changing the
middle-levels cycle by a hexagon.

#### Proof

The symmetric difference of two perfect matchings of a bipartite graph is a
vertex-disjoint union of alternating even circuits. Toggle these circuits
one at a time. This proves (6.4), and every intermediate set is again a
perfect matching of \(H_C\). The turn-augmentation equivalence reconstructs
from it a decoration of the same \(C\), while the binary-trace equivalence
says that its physical lift is cap-two and has at most the exceptional one
cycle.

If \(K\) is odd, the residual-edge types cannot alternate cyclically, so
every decoration is a forest. If \(K\) is even, the residual-edge parity
criterion says that a decoration is a forest exactly when two consecutive
residual edges have the same type. Forcing such a pair and forbidding
residual edges on the open arc between them gives precisely
\(H_C[p,q]\); hence ordinary perfect-matching Hall is necessary and
sufficient. \(\square\)

The word *protected* in this theorem has a deliberately narrow scope: the
fixed cycle support, both adjacent palettes, and cap-two topology survive.
It does not assert preservation of a separately selected deeper-shadow,
residence, socket, or compiler witness bank. Nor does it decompose an
\(H_C\)-circuit into primitive diamond hexagons while keeping every
intermediate primitive toggle cap-two; the whole translated difference is
one permitted compound switch.

### Corollary 6.4 (exact recursive compatibility gate)

For a prescribed sequence of Hamilton-preserving hexagon toggles, let the
state at each stage be a forest perfect matching of its turn-augmentation
graph. Join two consecutive state sets by the transparent relation of
Theorem 6.2, or by the repair relation obtained by deleting the at most six
lost matching edges and applying at most six Berge augmentations in the new
turn-augmentation graph. A decorated forest survives the whole sequence if
and only if this layered relation has a path from an initial state to a final
state.

For a recursively supplied gluing tree the identical statement is the usual
bottom-up tree constraint recursion: a state at a parent survives exactly
when it has a compatible surviving state in every child subtree. Therefore
nonemptiness of every individual hexagon relation is not sufficient; a
branch vertex can demand incompatible representatives. The all-\(m\)
existence gate is precisely nonemptiness of the root state after this joint
pruning. Transparent edges are the diagonal, zero-repair part of this
relation.

When intermediate nodes are two-factors rather than Hamilton cycles, replace
\(H_C\) by the componentwise turn-augmentation graph with global saturation
of both colour shores, impose boundary alternation on every new factor
cycle, and retain one physical forest-parity/breaker condition per component.
Every hexagon condition is evaluated at the moment that toggle is applied.
This componentwise extension is formal; existence of accepting states is
not asserted.

Here a node state means the full occurrence-labelled matching, global colour
saturation data, and per-component trace state. Boundary bits alone do not
make sibling subproblems independent: their palette choices can still
collide globally.

If the recursion additionally demands a leaf-peelable gap matching, every
edge relation must also pass the separate delete--contract--insert test on
the gap--colour graph: the new attachment multigraph must be loopless and
acyclic. Transparency alone does not imply this row; the repaired \(m=4\)
census contains a transparent toggle for which exactly \(72\) of \(144\)
common decorations fail it.

#### Proof

The path statement is induction on the toggle sequence. A transparent edge
keeps the same selected occurrences; a repair edge is exact by Berge
augmentation and the turn-augmentation equivalence, after which the forest
parity test is imposed. The tree statement follows by induction from the
leaves: existential choices in child subtrees are conditionally independent
once the occurrence-labelled parent state is fixed. \(\square\)

### Theorem 6.5 (simultaneous guarded transparent cube)

Let \({\mathfrak F}_0\) be a middle-levels two-factor with one fixed global
decoration \(D=(D_-,D_+)\). Let
\(Z_1,\ldots,Z_s\) be pairwise vertex-disjoint alternating incidence
hexagons. Write \(N_i^0\) for the three edges of \(Z_i\) used by
\({\mathfrak F}_0\), and \(N_i^1\) for the other three.

Delete all \(N_i^0\). Assume that the remaining factor edges form path
atoms, that every original factor component is cut, and that every atom
contains at least one selected occurrence of \(D\). For a formal endpoint
\(p\) of an atom \(A\), let \(\epsilon(A,p)\in\{-,+\}\) be the shore type
of the first selected occurrence met while traversing \(A\) inward from
\(p\). For \(S\subseteq[s]\), put

\[
 {\mathfrak F}_S={\mathfrak F}_0
              \mathbin\triangle\bigtriangleup_{i\in S} Z_i. 
                                                               \tag{6.5}
\]

Then the same selected occurrence sets \(D\) decorate every
\({\mathfrak F}_S\) if and only if, for every \(i\):

1. toggling \(Z_i\), computed in the base factor (equivalently in any state
   of the other disjoint toggles), preserves the selected local turn-colour
   multiset separately on the two shores; and
2. every new seam \(xy\in N_i^1\), with endpoint \(x\) on atom \(A_x\)
   and endpoint \(y\) on atom \(A_y\), satisfies

\[
                    \epsilon(A_x,x)\ne\epsilon(A_y,y).          \tag{6.6}
\]

Thus, under the nonempty-atom guard, transparency composes over the full
Boolean cube of disjoint toggles, not merely along one selected order.

#### Proof

Pairwise vertex-disjointness makes all turn-colour changes additive and
confines the change from \(Z_i\) to its six positions. Hence the two global
turn palettes survive every subset of toggles exactly when the two local
multisets survive each toggle separately.

Inside every retained atom the marked shore types still alternate, even if
that atom is traversed in reverse. Because every atom has a mark, the two
marks consecutive across a seam are exactly the inward first marks recorded
at its two formal endpoints. Old seams are compatible because \(D\)
decorates \({\mathfrak F}_0\); every possible new seam is compatible exactly
under (6.6). This proves sufficiency for every subset \(S\). Necessity follows
by applying the asserted decoration property to \(S=\{i\}\) for each
\(i\). \(\square\)

Let \(P_{\rm at}\) pair the two formal ports of every path atom, and let

\[
 N_S=\bigcup_{i\in S}N_i^1\ \cup
     \bigcup_{i\notin S}N_i^0.                       \tag{6.7}
\]

The factor topology is the independent exact row

\[
 \#\operatorname {comp}({\mathfrak F}_S)
   =\#\operatorname {cycles}(P_{\rm at}\cup N_S).   \tag{6.8}
\]

Indeed, alternating between an atom pairing and a seam pairing traces one
factor component, and every component arises once. Thus a final gluing plan
is connected exactly when this transition system has one cycle; demanding
that each individual toggle reduce the component count is a stronger,
unnecessary monotonicity condition.

In a free \(H\cong\mathbb Z_h\) quotient, if the quotient transition cycles
have voltages \(V_1,\ldots,V_t\), their physical development has

\[
                         \sum_{r=1}^t\gcd(h,V_r)      \tag{6.9}
\]

components. Hence quotient Hamiltonicity additionally requires one
transition cycle and primitive voltage. Neither follows from transparency.
Physical linearity of the decorated diamond lift is also separate: its
residual cycle-edge types must escape cyclic alternation. A chain of four
consecutive unmarked positions lying wholly inside one retained atom is a
simple cube-stable sufficient breaker.

### Corollary 6.6 (exact static gluing existence gate)

For a supplied disjoint-hex plan, let \({\cal T}_i\) be the set of full
occurrence-labelled decorations satisfying the two local conditions of
Theorem 6.5 at \(Z_i\), and let \({\cal G}_{\rm at}\) be the set of
decorations which select at least one occurrence in every retained atom. A
simultaneous transparent construction exists exactly when

\[
 D\in \operatorname {PM}(H_{{\mathfrak F}_0})
       \cap{\cal G}_{\rm at}
       \cap\bigcap_{i=1}^s{\cal T}_i                 \tag{6.10}
\]

for some \(D\) which also passes the chosen final transition-cycle,
voltage, and physical-parity rows. Here
\(H_{{\mathfrak F}_0}\) is the componentwise turn-augmentation graph with
global saturation of both colour shores.

Individual nonempty intersections
\(\operatorname {PM}(H_{{\mathfrak F}_0})\cap{\cal G}_{\rm at}
\cap{\cal T}_i\) do not suffice:
two incident gluing constraints may support disjoint sets of central
decorations. This is the minimal branching obstruction, and no Helly theorem
for these perfect-matching faces is known. A useful sufficient special case
is an affine binary interface on a tree,

\[
                         e_v=e_u\oplus\sigma_{uv},    \tag{6.11}
\]

because all such equations have a solution, unique after the root bit is
fixed. The unresolved all-\(m\) task is to produce enough literal hexagons
whose full occurrence constraints have this or another globally compatible
form.

### Corollary 6.7 (literal transparent gluing tree)

Under Theorem 6.5, form the bipartite incidence multigraph \({\cal I}\) whose
left vertices are the components of \({\mathfrak F}_0\), whose right
vertices are the hexagons \(Z_i\), and whose three edges at \(Z_i\) record
the three base-factor edges \(N_i^0\) and the components containing them.
If \({\cal I}\) is a connected tree, then toggling all \(Z_i\) turns
\({\mathfrak F}_0\) into one Hamilton cycle while preserving \(D\).

If, in addition, one retained atom contains four consecutive unmarked
positions, the diamond lift of the final decoration is a spanning
\(\operatorname {Cat}_m\)-path forest with both adjacent palettes exact.

#### Proof

Root \({\cal I}\) at a component vertex and process hexagon vertices from
the leaves toward the root. A processed hexagon has one parent component
branch and two child component branches. They are distinct, since a repeated
branch would make a cycle in \({\cal I}\). Its three old edges are still
present, because the hexagons are vertex-disjoint. Removing them opens three
cycles into paths, and the other alternating matching of the incidence
hexagon joins those paths into one cycle. Thus each toggle reduces the
component count by two. A tree with \(s\) hexagon vertices of degree three
has \(2s+1\) component vertices, so the final count is one. Theorem 6.5
preserves \(D\) throughout. The retained four-zero trace lies inside an atom
and is untouched; it excludes the unique physical cycle face. \(\square\)

### Theorem 6.8 (bounded polygon damage gives bounded linkage width)

Let \({\cal G},{\cal G}'\) be the old and new balanced augmented trace
graphs, of shore size \(N\), for a Hamilton-safe alternating
\(2t\)-circuit, and put

\[
                         H={\cal G}\cap{\cal G}'.     \tag{6.12}
\]

Let \(M_{\rm old}\) be a maximum matching of \({\cal G}\), of size
\(N-e\). A \(2t\)-circuit deletes at most \(t\) old cycle-incidence edges,
\(t\) old upper-turn occurrence edges and \(t\) old lower-turn occurrence
edges. Therefore, with

\[
 \ell=|M_{\rm old}\setminus E(H)|,\qquad
 \widehat M=M_{\rm old}\cap E(H),\qquad
 s=N-|\widehat M|=e+\ell,                            \tag{6.13}
\]

one has

\[
              \ell\le3t,\qquad s\le e+3t,\qquad
              r:=N-\nu(H)\le s.                      \tag{6.14}
\]

For a literal simple alternating circuit in the turn-augmentation graph,
there is a sharper position-cap bound:

\[
                         \ell\le2t,\qquad r\le s\le e+2t.
\]

Indeed every deleted augmented edge is incident with one of the \(2t\)
switched position vertices, while the deleted physical-incidence edges form
a matching on those positions. This refinement also holds for a
vertex-disjoint union of circuits when \(2t\) denotes the total number of
distinct switched positions. The safe \(3t\) bound remains the correct
stated scope for a more abstract supplied rewrite which may delete augmented
edges not chargeable to that position set.

Orient every edge of \({\cal G}'\setminus\widehat M\) from the left shore
to the right shore and every edge of \(\widehat M\) from right to left.
Then \({\cal G}'\) has a perfect matching if and only if this digraph
contains \(s\) pairwise vertex-disjoint directed augmenting paths covering
all vertices exposed by \(\widehat M\). Equivalently, after replacing
\(\widehat M\) by a maximum matching of \(H\), exactly \(r\) such paths are
required.

In particular a polygon from a decorated parent has linkage width at most
\(3t\), and a polygon from deficiency \(e\) has width at most \(e+3t\).

#### Proof

The three types of removed augmented edges give \(\ell\le3t\), and
(6.13)--(6.14) follow immediately. For any matching \(M\), a directed
path from an exposed left vertex to an exposed right vertex is exactly an
\(M\)-augmenting path. Toggling \(s\) disjoint such paths makes
\(\widehat M\) perfect. Conversely, the symmetric difference of
\(\widehat M\) with any perfect matching of \({\cal G}'\) consists of
alternating cycles and exactly \(s\) vertex-disjoint augmenting paths
covering its exposed vertices. The maximum-common-matching formulation is
the same argument with \(r=N-\nu(H)\). \(\square\)

For completeness, the position refinement follows by letting \(a\) be the
number of deleted physical-incidence edges selected by \(M_{\rm old}\).
They occupy \(2a\) switched positions. Every other deleted selected edge is
a turn-occurrence edge at a distinct unused switched position, so

\[
               \ell\le a+(2t-2a)=2t-a\le2t.
\]

For one hexagon, \(t=3\), this recovers the earlier exact width-six bound.

### Proposition 6.9 (bounded width is not collar locality)

For every \(n\ge1\), let

\[
 L=\{x_0,\ldots,x_n\},\qquad R=\{y_0,\ldots,y_n\},
\]

and let \(H_n\) have the matching

\[
 M_n=\{x_i y_i:1\le i\le n\}
\]

together with the chain edges \(x_{i-1}y_i\) for \(1\le i\le n\).
The matching \(M_n\) has deficiency one and exposes \(x_0,y_0\).
The old graph \(G_n=H_n+\{x_0y_0\}\) is perfect. Replacing that one edge by
\(x_ny_0\) gives another perfect graph \(G'_n\), but relative to the common
matching \(M_n\) its unique augmenting path is

\[
 x_0,y_1,x_1,y_2,\ldots,y_n,x_n,y_0,                 \tag{6.15}
\]

of length \(2n+1\). Hence linkage width one and one new edge can force an
arbitrarily long global rerouting.

This is an abstract bipartite matching example, not a claimed
middle-levels fixture. It proves the exact logical warning: (6.14) bounds
the number of exposed pairs and linkage strands, but by itself bounds
neither path length, distance from the polygon, nor the number of remote
occurrence choices changed.

### Corollary 6.10 (exact combined recursive gluing/socket state)

For one polygon, choose a maximum matching \(M\) of \(H\), let
\(S,T\) be its exposed left and right vertices, and put

\[
 A=E({\cal G}')\setminus E(H),\qquad
 B=S\cup T\cup V(A).                                 \tag{6.16}
\]

The information-complete interface is the full alternating linkage relation
\({\cal L}_H(B)\): all oriented, internally vertex-disjoint path systems in
the common graph whose endpoints lie in \(B\). The new graph is perfect
exactly when one member of this relation, together with the new \(A\)-edges,
forms \(r\) disjoint \(S\)-to-\(T\) augmenting paths. Pairwise terminal
reachability is insufficient because different paths may share a global
bottleneck.

Since \(|A|\le3t\), the safe bound (6.14) gives

\[
                  |B|\le 2e+12t.
\]

For the literal simple-circuit position refinement this improves to
\(|B|\le2e+10t\). These are behavioral-boundary bounds, not bounds on the
vertices inspected while computing \({\cal L}_H(B)\).

For blocks glued along a tree of adhesions of size at most \(b\), record the
oriented linkage signature of
MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md:
every realizable collection of vertex-disjoint alternating path fragments
whose endpoints are exposed terminals or adhesion vertices, including their
orientations and boundary usage. Child signatures compose exactly by joining
compatible fragments and rejecting repeated boundary use, internal directed
cycles and illegal source/sink orientation. For bounded \(b\) this is a
finite tree-DP state (with the bounded exposed-terminal set understood); it
is the gammoid layer of the recursion.

More explicitly, if \(r\) exposed pairs meet a block, the number of named
terminals is at most

\[
 p=b+2r+2|A|\le b+2e+12t
\]

in the safe form, and at most \(b+2e+10t\) under the literal position
refinement. If every new \(A\)-edge has already been assigned wholly inside
one block, its internal endpoints may be omitted from the adhesion
signature, giving the smaller \(b+2r\) parameter. A safe crude bound on
oriented endpoint-pairing patterns is

\[
                         4^p p!=2^{O(p\log p)}.       \tag{6.17}
\]

The state stores the realized subset of these patterns. The composition
theorem is exact, but computing the entire prescribed-pairing profile is not
claimed to be one ordinary max-flow call; the paths may still require a
global gammoid/linkage calculation.

It must be carried alongside, not substituted for, the other exact rows.
If \({\cal P}\) is the selected complete linkage, the repaired matching

\[
             M'=M\mathbin\triangle
                    \bigtriangleup_{P\in{\cal P}}E(P)             \tag{6.18}
\]

must simultaneously satisfy:

1. the full occurrence-labelled decoration and atom-boundary state;
2. physical forest parity, or the full graphic forest test outside the
   fixed-cycle subclass;
3. the leaf-peelable gap-forest connectivity partition when that stronger
   state is required;
4. the atom-transition component condition and the endpoint-socket
   relation;
5. primitive quotient voltage; and
6. the protected deeper-shadow, residence and compiler rows.

These are joint conditions on the same \(M'\), polygon and physical
occurrences. Separate feasibility of the linkage, gap-forest and socket
rows does not imply a common choice. A nontransparent linkage can change
selected occurrences far from the polygon, so the old atom marks, trace
breaker, gap graph and socket endpoints must be recomputed unless they were
explicitly protected against every path in the signature.

A fixed-decoration transparent polygon bypasses this repair search: its old
decoration is already a valid output state. The linkage layer is needed for
repairable, representative-changing polygons and for deficient intermediate
nodes.

Thus bounded polygons now have an exact finite linkage layer whenever the
recursive architecture has bounded adhesion. What remains open is
nonemptiness, for every \(m\), of the full joint state containing this
gammoid layer together with the gap-graphic, topology, voltage and compiler
layers.

## 7. Connector consequence and remaining gate

Once a switch produces a spanning \(K=\operatorname{Cat}_m\)-path forest,
the endpoint connector theorem applies even if the forest is no longer
middle-levels-resolvable. A literal endpoint-saturating connector family
gives one Hamilton cycle exactly when its contracted transition is one
cycle; in the clean quotient its total voltage must be a unit. Distinct
lower and upper connector colours give the corresponding cap-two profiles.
Private sockets, deeper witnesses, residence and the compiler remain
separate.

Equivalently, the cycle-first route seeks a spanning occurrence cycle whose
colour-incidence graph has a perfect matching. The selected matching edges
are then automatically a linear forest and the complementary cycle edges
are its connectors. In the fixed-middle-levels subclass, gap Hall precedes
the binary trace and transparent-gluing topology tests.

The proved boundary is:

- universal canonical whole-cycle shift descent is false, by (5.1)--(5.4);
- a specified compound switch is exact under Theorem 2.1;
- arbitrary one-step compound forestification is equivalent to the open
  Catalan Linear Matching existence theorem;
- within a fixed middle-levels cycle, cap-two matching connectivity and
  forest reachability are exact by Theorem 6.3;
- pairwise disjoint transparent hexagons compose exactly under the guarded
  common-decoration intersection (6.10), with topology given by (6.8);
- a connected component--hexagon incidence tree is an exact sufficient
  Hamilton gluing architecture by Corollary 6.7;
- every bounded \(2t\)-polygon has an augmenting-linkage layer of width at
  most \(e+3t\) in the general edge-count form and at most \(e+2t\) for the
  literal simple-circuit turn graph; it composes exactly over bounded
  adhesions, but its paths can be global;
- cap-two reconfiguration outside that fixed support, an all-\(m\) accepting
  joint transparent-gluing state, protected deeper witnesses, connectors
  and compilation remain open.

No retracted \(W/2\) Greene--Kleitman bound is used. The corrected standard
GK retained-edge count is

\[
                 m\operatorname{Cat}_m-\Delta_m,
\]

with
\(\Delta_m/(m\operatorname{Cat}_m)\to0.356895867892\ldots\), as proved in
MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md.
