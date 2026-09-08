# A tight enumeration supplies the balanced residual factor for the `k=15 -> k=17` diamond

Date: 2026-07-31  
Status: unconditional central-factor theorem, using the published tight-enumeration theorem; no `k=17` word or new numerical upper bound is claimed

## 0. Result

The coupled residual path factor left open in Theorem 2.3 of
`MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`
exists for the authenticated two-cycle `k=15` parent.

The proof has three independent pieces.

1. A tight enumeration of the two consecutive levels
   \(\binom{[2r-1]}{r-2}\cup\binom{[2r-1]}{r-1}\) produces a spanning
   path forest on the rank-\((r-1)\) layer whose edge intersections are
   every rank-\((r-2)\) set exactly once.  It has exactly
   \(\operatorname{Cat}_r\) path components.
2. Such a forest can be coupled to a lower-rainbow parent 2-factor by
   orienting its path endpoints.  The coupling is a balanced residual
   \(X\)-to-\(Y\) path factor exactly when each orientation class hits every
   parent cycle.
3. The endpoint-orientation problem contracts to an ordinary multigraph.
   It is feasible exactly when every contracted parent-cycle vertex has
   degree at least two.  For the actual `k=15` parent, whose cycles have
   sizes `6390` and `45`, a coordinate relabelling of the tight-enumeration
   forest has this property by transitivity averaging.

Thus the sealed `AA` cycles in the first `k=17` four-sector factor are not
forced.  They can be replaced, solver free, by exactly `1430` balanced
residual macro paths.  What remains is the occurrence-labelled insertion
of the pure `U` deck, the joint untagged palette, all-width upper service,
residence, and the one common lower compiler.

## 1. The tight-enumeration forest

Put

\[
 \Omega=[2r-1],\qquad
 \mathcal Z=\binom\Omega{r-2},\qquad
 \mathcal C=\binom\Omega{r-1},
\]

and write

\[
 N=|\mathcal Z|,\qquad M=|\mathcal C|,\qquad
 b=M-N=\operatorname{Cat}_r.                         \tag{1.1}
\]

Gregor--Micka--Mutze's tight-enumeration theorem gives a cyclic listing of
all vertices in the two consecutive levels \(\mathcal Z\cup\mathcal C\)
whose total Hamming length is

\[
 |\mathcal Z|+|\mathcal C|+
 \bigl||\mathcal C|-|\mathcal Z|\bigr|=2M.           \tag{1.2}
\]

### Lemma 1.1 (lower-rainbow GMM forest)

Suppress the \(\mathcal Z\)-vertices in a tight enumeration.  The resulting
cyclic order of \(\mathcal C\) is a Hamilton cycle in
\(J(2r-1,r-1)\).  Exactly \(N\) of its edges are mediated by the members of
\(\mathcal Z\), one per member, and the other \(b\) edges are direct
same-level steps.  Deleting the latter \(b\) edges leaves a spanning linear
forest \(G\) with exactly \(b\) components, and

\[
 \{C\cap C':CC'\in E(G)\}=\mathcal Z                 \tag{1.3}
\]

with multiplicity one.

#### Proof

Let \(x\) be the number of consecutive pairs in the cyclic enumeration
which lie on opposite levels.  Every opposite-level step costs at least one
flip and every same-level step costs at least two.  Since a lower-level
vertex has only two neighbours in the cyclic listing, \(x\le2N\).  Hence
the total number of flips is at least

\[
 x+2(M+N-x)=2(M+N)-x\ge2M.                           \tag{1.4}
\]

Equality in (1.2) forces \(x=2N\), every cross-level step to be an
inclusion edge, and every same-level step to have Hamming distance two.
Thus every \(Z\in\mathcal Z\) is flanked by two distinct members of
\(\mathcal C\), whose intersection is exactly \(Z\), while all remaining
adjacencies are Johnson edges inside \(\mathcal C\).  Suppression therefore
gives the stated Hamilton cycle.  It has \(M-N=b\) direct edges.  Deleting
them from one cycle gives a spanning forest of \(b\) paths, with isolated
vertices allowed, and leaves the \(N\) distinct colours (1.3).  \(\square\)

## 2. Coupling a path forest to the two parent rails

Let \(F\) be a directed lower-rainbow Johnson 2-factor on rank-\(r\)
owners \(T_i\), indexed so that

\[
 C_i=T_i\cap T_{\operatorname{succ}(i)}              \tag{2.1}
\]

enumerates \(\mathcal C\) exactly once.  Regard the vertices of the forest
\(G\) from Lemma 1.1 as these indices \(i\).

Orient every component of \(G\).  Put \(\alpha_i=1\) at its first endpoint
and \(\beta_i=1\) at its last endpoint; put both equal to one at an isolated
vertex.  They vanish elsewhere.  Then

\[
             \deg_G(i)+\alpha_i+\beta_i=2            \tag{2.2}
\]

at every index.

Adjoin new coordinates \(x,y\), set

\[
 A_i=C_i+xy,\qquad X_i=T_i+x,\qquad Y_i=T_i+y,       \tag{2.3}
\]

and form \(R(G,\alpha,\beta)\) from:

* the edges \(A_iA_j\) for \(ij\in E(G)\);
* \(X_iA_i\) if \(\alpha_i=1\), and
  \(X_iX_{\operatorname{succ}(i)}\) otherwise;
* \(A_iY_{\operatorname{succ}(i)}\) if \(\beta_i=1\), and
  \(Y_iY_{\operatorname{succ}(i)}\) otherwise.

The three edge families have the complete lower-colour palettes

\[
 \mathcal Z+xy,\qquad \mathcal C+x,\qquad\mathcal C+y               \tag{2.4}
\]

exactly once.

### Theorem 2.1 (endpoint-coupling criterion)

The graph \(R(G,\alpha,\beta)\) is a spanning path cover by exactly \(b\)
paths, each with one free \(X\)-endpoint and one free \(Y\)-endpoint, if
and only if

\[
 \{i:\alpha_i=1\}\quad\hbox{and}\quad
 \{i:\beta_i=1\}                                    \tag{2.5}
\]

each meet every component of the parent 2-factor \(F\).

#### Proof

Equation (2.2) is the coupled socket equation, so every \(A_i\) has degree
two.  On one directed component of \(F\), replacing the outgoing
\(X_iX_{\operatorname{succ}(i)}\) edge at every \(\alpha\)-index cuts the
\(X\)-cycle into paths.  Each such path has one free \(X\)-endpoint and its
other endpoint attached to the corresponding \(A_i\).  If the component
contains no \(\alpha\)-index, its whole \(X\)-cycle remains sealed.  The
identical statement, with the orientation shifted by one edge, holds on the
\(Y\)-rail and the \(\beta\)-indices.

Every component of \(G\) joins its unique \(\alpha\)-endpoint to its unique
\(\beta\)-endpoint.  Hence, when (2.5) holds, one \(X\)-arm, one component
of \(G\), and one \(Y\)-arm concatenate into one path.  These \(b\) paths
are vertex-disjoint and exhaust all three owner decks.  If (2.5) fails, the
missed parent component survives as a sealed \(X\)- or \(Y\)-cycle, so the
asserted path cover is impossible.  \(\square\)

## 3. The endpoint contraction

Contract every directed cycle of \(F\) to one vertex.  For every component
of \(G\), put one multiedge between the two contracted vertices containing
its two endpoint occurrences.  An isolated component of \(G\) gives a loop.
Call the resulting multigraph \(H(F,G)\).

Orienting a path of \(G\) chooses which endpoint is \(\alpha\) and which is
\(\beta\).  Therefore (2.5) asks for an orientation of \(H(F,G)\) in which
every vertex has positive indegree and positive outdegree; a loop contributes
one to each.

### Lemma 3.1 (exact endpoint-orientation test)

Such an orientation exists if and only if

\[
                     \delta(H(F,G))\ge2,             \tag{3.1}
\]

where loops count twice toward undirected degree.

#### Proof

Degree zero or one plainly cannot supply both an incoming and an outgoing
edge.  Conversely, every finite undirected multigraph has a balanced
orientation with \(|d^+(v)-d^-(v)|\le1\) at every vertex: pair its odd-degree
vertices by adding auxiliary edges, orient Euler circuits in the resulting
even components, and then delete the auxiliary edges.  Under (3.1), the
smaller of \(d^+(v),d^-(v)\) is at least one.  Loops already contribute one
in each direction.  \(\square\)

Combining Theorem 2.1 and Lemma 3.1 reduces the coupled residual-factor gate
to the literal endpoint count

\[
 \boxed{\text{every parent cycle contains at least two endpoint occurrences
 of }G.}                                              \tag{3.2}
\]

In particular, if \(F\) is Hamiltonian, every GMM forest works without any
further condition.

## 4. The authenticated `k=15` parent

For `k=15`,

\[
 r=8,\qquad M=\binom{15}{7}=6435,\qquad
 N=\binom{15}{6}=5005,\qquad b=1430.                 \tag{4.1}
\]

The authenticated parent factor has two cycles of lengths `6390` and `45`.
Let \(S\subset\mathcal C\) be the 45 lower colours on the small cycle.
Take any GMM forest \(G_0\), and count its endpoints with multiplicity, so
an isolated vertex counts twice.  There are exactly

\[
                            2b=2860                  \tag{4.2}
\]

endpoint occurrences.  For a uniformly random coordinate permutation
\(\pi\in S_{15}\), transitivity on \(\mathcal C\) gives

\[
 \mathbb E_\pi\,|\pi(E(G_0))\cap S|
 =\frac{2b|S|}{M}
 =\frac{2860\cdot45}{6435}=20.                       \tag{4.3}
\]

Consequently some relabelling has at least 20 endpoint occurrences on the
small parent cycle.  A vertex contributes at most two endpoint occurrences,
so that cycle receives at most 90 and the large cycle receives at least
\(2860-90=2770\).  Both contracted degrees are therefore at least two.
Lemma 3.1 orients the GMM paths, and Theorem 2.1 produces a balanced residual
path factor with exactly `1430` \(X\)-to-\(Y\) macros.

### Corollary 4.1

The balanced residual path-factor hypothesis in Theorem 2.4 of the
dimension-uniform Shadow--Braid note holds for the authenticated `k=15`
parent.  It requires neither the sealed cap-two `AA` factor of the first
`k=17` construction nor a SAT search.

This does **not** yet satisfy the endpoint-compatible closure theorem.  One
still needs a rainbow path cover of the pure \(U\)-deck, occurrence-labelled
port/direct-seam containment, joint injection of the untagged lower palette,
all pure and tagged upper witnesses, a legal residence schedule, and the
global common-cap compiler.  Thus the certified numerical interval for
\(\nu(17)\) is unchanged.

## 5. Reusable target

For a general odd parent, the GMM forest removes the existence of the
rank-lowered `AA` path forest from the recurrence.  The only extra central
condition is (3.2).  Hence the owner-level regenerative state may be reduced
from an arbitrary coupled cap-two factor to:

1. a lower-rainbow, upper-complete parent 2-factor \(F\);
2. one relabelled GMM endpoint multiset meeting every component of \(F\) at
   least twice; and
3. the endpoint-compatible pure-\(U\) insertion and palette matching of
   Theorem 2.4.

The first finite `k=17` gate in this list is now item 3, not the residual
`AA/X/Y` path factor.

## 6. Pure-`U` insertion is exactly a second tight enumeration

There is a useful exact reformulation of item 3.  Put

\[
 \mathcal T=\binom\Omega r,\qquad
 \mathcal U=\binom\Omega{r+1},
 \qquad |\mathcal T|=M,\quad |\mathcal U|=N=M-b.      \tag{6.1}
\]

Regard each of the `b` residual paths from Theorem 2.1 as one oriented
**macro** `P`, with a rank-`r` input port \(\ell(P)\) and output port
\(h(P)\).  These are the projections of its free `X` and `Y` endpoints.
For the equivalence below impose the additional **Johnson-port** condition

\[
              |\ell(P)\mathbin\triangle h(P)|=2
              \qquad\hbox{for every macro }P.        \tag{6.2}
\]

This condition is not a consequence of Theorem 2.1.  Without it the macro
cycle below is still a valid owner/colour object, but expanding one macro to
its two port labels need not be a tight enumeration.
An adjacency has a rank-`r` colour as follows:

* two adjacent `U`-owners have colour their intersection;
* a `U`-owner adjacent to a macro uses the relevant contained port;
* two adjacent macros are legal exactly when the output port of the first
  equals the input port of the second, and that common set is their colour.

### Theorem 6.1 (Johnson-port macro/tight-enumeration equivalence)

The following are equivalent.

1. The Johnson-port condition (6.2) holds, and the complete `U`-deck and the
   `b` oriented macros admit one cyclic order
   in which every declared adjacency is legal and the adjacency colours are
   a bijection onto \(\mathcal T\).
2. The two consecutive levels \(\mathcal T\cup\mathcal U\) admit a tight
   enumeration whose `b` direct same-\(\mathcal T\)-level transitions can be
   put in bijection with the macros, preserving the two ordered endpoints.

Under this equivalence, deleting any one adjacency opens the cycle and loses
exactly its one rank-`r` colour.  This gives the scalar one-hole linear
lower-`q1` ledger.  A macro--macro adjacency need not exist: direct
same-level transitions in a tight enumeration may all be isolated.  If the
later compiler requires the specific direct-gap boundary type of Theorem
2.4, that adjacency must be imposed separately; opening a macro--`U` or
`U`--`U` adjacency has different endpoint types.

#### Proof

Start with a tight enumeration of \(\mathcal T\cup\mathcal U\).  The equality
argument from Lemma 1.1, now on the complementary pair of levels, shows that
every `U`-vertex is flanked by `T`-vertices through inclusion edges, while
there are exactly

\[
                         M-N=b                       \tag{6.3}
\]

direct `T`--`T` transitions, each a Johnson step.  Replace every directed
`T`--`T` transition by its assigned macro and suppress the remaining
`T`-vertices.  A run

\[
 U,T_0,T_1,\ldots,T_s,U'
\]

becomes a run of `s` macros: the end labels are legal containment ports and
each internal label is a legal macro--macro seam.  A subword `U,T,U'`
becomes the Johnson edge `UU'` of colour `T`.  Since every `T`-vertex occurs
once in the tight enumeration, every rank-`r` adjacency colour occurs once
in the substituted cycle.

Conversely, expand every macro into its ordered pair
\(\ell(P),h(P)\).  At a macro--macro seam identify the equal output/input
label; at a `U` port insert its contained label; and between two adjacent
`U`-owners insert their rank-`r` intersection.  Colour bijectivity says that
this expansion lists every member of \(\mathcal T\) exactly once, while the
owner cycle already lists every member of \(\mathcal U\) once.  All
cross-level steps are inclusions and every same-level step is a Johnson
step.  It therefore has total Hamming length

\[
 2N+2(M-N)=2M
 =|\mathcal T|+|\mathcal U|+
  \bigl||\mathcal T|-|\mathcal U|\bigr|,             \tag{6.4}
\]

so it is a tight enumeration.  The two operations are inverse.  Opening any
adjacency removes exactly the corresponding colour and no owner. \(\square\)

### Corollary 6.2 (a coupled-tight sufficient subclass)

For the authenticated `k=15 -> k=17` branch, suppose in addition that the
GMM residual forest and its endpoint orientation can be chosen so that all
`1430` resulting macros satisfy (6.2).  Then middle ownership and the full
child lower-`q1` palette reduce to one **coupled pair of tight
enumerations**:

1. the lower tight enumeration from Lemma 1.1 supplies and endpoint-orients
   the `1430` residual macros; and
2. an upper tight enumeration must realize those `1430` ordered macro port
   pairs as its direct transitions.

The two tight enumerations exist separately by the published theorem.  Their
required endpoint correlation is the whole remaining owner/`q1` gate **in
this Johnson-port subclass**.  It must not be replaced by two independent
applications of tight enumeration: the direct-transition deck is part of
the data.

For unrestricted residual macros, (6.2) is an additional nontrivial gate.
Failure of (6.2) does not obstruct an endpoint-compatible child cycle: a
long macro may legitimately connect two nonadjacent port labels through its
internal owners.  Such a cycle simply has no expansion to an ordinary tight
enumeration.  Consequently Corollary 6.2 is a sharp sufficient reduction,
not an equivalence for every solution of Theorem 2.4.

Even after Corollary 6.2, all-width upper service, residence, and the common
lower compiler remain separate Shadow--Braid obligations.

## 7. The unrestricted macro gate is one integral `b`-flow

The Johnson-port hypothesis is unnecessary if one works directly with the
macros.  Assume that every macro has two distinct port colours and that the
input-port colours are pairwise distinct, as are the output-port colours.
For \(T\in\mathcal T\), let

\[
 m_T=|\{P:T\in\{\ell(P),h(P)\}\}|\in\{0,1,2\},
 \qquad d_T=2-m_T.                                   \tag{7.1}
\]

Form the balanced bipartite incidence graph \(\mathcal B_{\cal P}\).  Its
left shore is

\[
                     \mathcal U\mathbin{\dot\cup}{\cal P},             \tag{7.2}
\]

where \({\cal P}\) is the `b`-element macro set, and its right shore is
\(\mathcal T\).  Join `U` to every \(T\subset U\), and join a macro only to
its two port colours.

### Theorem 7.1 (exact unoriented macro `b`-flow reduction)

There is a spanning two-factor of \(\mathcal B_{\cal P}\) if and only if
the ordinary incidence graph between \(\mathcal U\) and \(\mathcal T\)
contains an integral subgraph satisfying

\[
              \deg(U)=2\quad(U\in\mathcal U),
 \qquad       \deg(T)=d_T\quad(T\in\mathcal T).      \tag{7.3}
\]

Equivalently, for every family \({\cal S}\subseteq\mathcal U\),

\[
 \boxed{
  2|{\cal S}|\le
  \sum_{T\in\mathcal T}
       \min\bigl(d_T,\,|\{U\in{\cal S}:T\subset U\}|\bigr).
 }                                                     \tag{7.4}
\]

If each residual macro path may be traversed in either direction, any
connected solution is a cyclic macro/`U` owner order with every rank-`r`
colour exactly once.  An arbitrary solution is a disjoint union of such
coloured cycles; connectivity is then the only remaining owner/`q1`
topological condition.

If macro directions are frozen in advance (for example, every macro is
required to run from its `X` endpoint to its `Y` endpoint), one must add the
**macro-coherence** condition that every cycle of the two-factor traverses
all of its macros in their prescribed direction, after possibly reversing
the whole cycle.  The scalar flow (7.4) does not imply this directed
condition.

#### Proof

Every macro vertex has graph degree two, so a spanning two-factor must use
both of its port incidences.  The colour vertex `T` has residual degree
\(2-m_T=d_T\), while every `U` vertex still needs degree two.  This proves
the equivalence with (7.3).  The totals agree:

\[
 \sum_Td_T=2M-2b=2N=2|\mathcal U|.                  \tag{7.5}
\]

To characterize (7.3), use the integral network with source-to-`U`
capacity two, unit-capacity containment arcs `U`--`T`, and `T`-to-sink
capacity \(d_T\).  The max-flow/min-cut condition, minimized separately at
each `T`, is exactly (7.4); integrality is automatic.  A full flow saturates
every `T` capacity by (7.5).

Reinsert the two forced incidences of every macro.  All vertices then have
degree two.  On an alternating component, suppressing a colour vertex
between two `U` vertices gives their Johnson edge, between a `U` and a macro
gives the corresponding containment port, and between two macros gives a
legal equality seam.  Every right-shore colour occurs once as a vertex and
hence once in the suppressed cycle.  Therefore one component is precisely
an unoriented cyclic owner order, while several components are the sole
unoriented topological defect.  Traversing a macro backward simply reverses
its already valid physical path.  Under a fixed-orientation convention the
additional coherence condition stated above is necessary and sufficient.
\(\square\)

### Corollary 7.2 (the smallest current `k=17` owner gate)

After the GMM endpoint-oriented construction, the remaining unrestricted
owner/lower-`q1` question is no longer a simultaneous palette search.  It is:

1. choose the GMM relabelling and endpoint orientations so all macro ports
   are distinct in their own type and \(\ell(P)\ne h(P)\);
2. verify the explicit cut inequalities (7.4); and
3. choose an integral flow whose completed two-factor is connected, or can
   be opened and spliced within the available boundary budget; and
4. if a common macro direction is required by the later braid, enforce
   macro coherence on the selected component(s).

This formulation is strictly more general than the coupled-tight subclass
of Section 6.  It also shows where correlation still enters: (7.4) depends
on the *joint* multiplicity vector \((m_T)\), not merely on the two separate
port-set cardinalities.

## 8. Only full and one-missing stars can obstruct the flow

The cut system (7.4) has a much smaller complementary form.  For
\({\cal Q}\subseteq\mathcal U\), put

\[
 q_T({\cal Q})=|\{U\in{\cal Q}:T\subset U\}|.
\]

Every rank-`r` set has exactly \(r-1\) supersets in \(\mathcal U\).  Define

\[
\begin{aligned}
 F_0({\cal Q})&=\{T:m_T=0,\ q_T({\cal Q})=r-1\},\\
 F_1({\cal Q})&=\{T:m_T=1,\ q_T({\cal Q})=r-1\},\\
 A_0({\cal Q})&=\{T:m_T=0,\ q_T({\cal Q})=r-2\}.
\end{aligned}                                         \tag{8.1}
\]

### Proposition 8.1 (full-star cut criterion)

The macro `b`-flow exists if and only if, for every
\({\cal Q}\subseteq\mathcal U\),

\[
 \boxed{
  2|F_0({\cal Q})|+|F_1({\cal Q})|+|A_0({\cal Q})|
  \le2|{\cal Q}|.
 }                                                     \tag{8.2}
\]

Thus no rank-`r` colour with two or more missing supersets can occur in a
minimal capacity obstruction.  The only witnesses are port-weighted full
stars and unported stars missing exactly one member.

#### Proof

Take \({\cal S}=\mathcal U\setminus{\cal Q}\) in (7.4).  Since
\(a_T=|\{U\in{\cal S}:T\subset U\}|=r-1-q_T({\cal Q})\) and
\(\sum_Td_T=2|\mathcal U|\), the cut is equivalent to

\[
       \sum_T(d_T-a_T)_+\le2|{\cal Q}|.              \tag{8.3}
\]

For \(d_T=2\), the summand is two on a full star, one on a star missing one
member, and zero otherwise.  For \(d_T=1\), it is one only on a full star.
For \(d_T=0\), it always vanishes.  Substituting \(d_T=2-m_T\) gives
(8.2). \(\square\)

Proposition 8.1 is the natural target for a relabelling or discrepancy
argument: the port multiplicities need only hit the deep interiors of
families of upper sets.  It is also a fail-fast exact audit for a proposed
GMM endpoint system; enumerating arbitrary subsets on the original side of
(7.4) is unnecessary if the full- and one-missing-star families can be
generated directly.
