# Preselected portal forests: the exact topology-first quantifier escape and the pull-host lift gate

Date: 2026-08-01

Status: unconditional abstract extension theorem and sharp scope audit.  This
removes component scattering from the bounded-task topology row **provided**
the selected task portals belong to one static compatible connector host.  No
current theorem lifts the ordered SCD portals into the canonical Mütze pull
host, so this does not prove a protected Hamilton carrier or
`nu(k)=B(k)+O(1)`.

## 0. Outcome

There is a useful quantifier swap which should be made before trying to
preserve portal menus through a long sequence of component contractions.

Suppose the bounded task portals can be selected while the elementary
components are still unmerged.  If their connector edges form a forest in
the **actual static connector host**, then they can be frozen first and
extended to a spanning connector tree afterward.  No menu has to remain
scattered during the subsequent contractions.

The ordered-potential theorem already proves that the selected portal edges
form a forest on the raw SCD-chain graph.  What is not proved is that this
raw graph is the actual connector host used by the topology completion.  In
particular, the canonical Gregor--Mütze--Nummenpalo pull host has:

* vertices equal to cycles of the canonical lexical middle-levels factor;
* edges equal to its canonical flippable-pair hexagons.

The raw SCD-chain forest may acquire loops or parallel edges under the map
to those factor cycles, and a generic ordered Johnson edge need not be a
canonical pull at all.  Thus the new exact missing statement is a
**portal-to-pull lift lemma**, not a component-scattering theorem.

## 1. Forest-first extension

### Theorem 1.1 (graphic basis extension)

Let `H=(V,E)` be a connected multigraph and let `F subseteq E` be a graphic
forest.  Then `H` has a spanning tree `T` with

\[
                         F\subseteq T.                 \tag{1.1}
\]

More generally, if `H` has `c` connected components, every forest `F` in
`H` extends to a maximal spanning forest with exactly `|V|-c` edges.

#### Proof

Contract every edge of `F`.  Because `F` is a forest, contraction loses no
cycle rank.  The quotient `H/F` is connected.  Choose a spanning tree
`T'` of `H/F` and lift its edges to `H`.  Then

\[
                           T=F\cup T'
\]

is connected and has

\[
 |F|+|V(H/F)|-1
 =|F|+(|V|-|F|)-1
 =|V|-1
\]

edges, hence is a spanning tree.  The componentwise statement is the same
argument in every component of `H`. \(\square\)

This is just basis extension in the graphic matroid, but its order of
quantifiers is important here:

\[
 \boxed{
 \text{choose the bounded task forest first, then choose the global merge
 tree around it}. }
                                                        \tag{1.2}
\]

No claim about the later images of the unused menu edges is required.

## 2. Static switch systems

The graph theorem transfers to physical topology when the connector system
is static in the following precise sense.

Let `P` be a base factor with component set `V(H)`.  For each `e in E(H)`,
let `Z_e` be a factor-alternating circuit which joins the two components
named by `e`.  Call the family **tree-compatible** when, for every forest
`J subseteq E(H)`, the symmetric differences along `Z_e`, `e in J`, are
simultaneously legal and the resulting component partition is obtained by
contracting the edges of `J`.

Let `D` be a protected packet bank.  Call `Z_e` **D-transparent** when its
switch preserves all named packet tickets required after topology
completion: owner occurrences, immediate palettes, residence rails,
arbitrary-width witnesses, and the retained terminal compiler cells.
Write `H_D` for the spanning subgraph of `H` consisting of the
`D`-transparent connector edges.

### Theorem 2.1 (preselected-switch completion)

Assume:

1. `H_D` is connected;
2. `{Z_e:e in E(H)}` is tree-compatible;
3. a selected task set `F subseteq E(H_D)` is a forest.

Then there is a spanning tree `T` of `H` containing `F`, and switching the
circuits indexed by `T` gives one spanning component while retaining every
selected task in `D`.

#### Proof

Apply Theorem 1.1 inside `H_D` to obtain `T sup F`.  Tree compatibility says that all
switches in `T` are simultaneously legal and contract the base components
along a spanning tree, hence produce one component.  Since `T subseteq H_D`,
transparency preserves the named task data. \(\square\)

For the canonical lexical factor and canonical flippable-pair hexagons in
the short middle-levels proof, the published noninterference theorem gives
the required tree compatibility.  Consequently, **if** the task portals are
members of that canonical pull family and are transparent, the quantifier
escape is complete: select them first, extend their auxiliary edges to a
spanning tree, and never ask their unused menus to survive a contraction.

### Corollary 2.2 (transparent-cut criterion)

Let `B_D=E(H)-E(H_D)` be the pulls forbidden by the protected bank.  The
forest-first completion works if and only if `F subseteq E(H_D)` and every
nontrivial cut of `H` contains an edge outside `B_D`.  In particular, if
`H` is `kappa`-edge-connected and

\[
                            |B_D|<\kappa,             \tag{2.1}
\]

then every selected forest `F subseteq E(H_D)` extends to a transparent
spanning tree.

This gives a quantitative route to the physical theorem.  If each of `h`
bounded packets forbids at most `beta` canonical pulls, it is enough to
prove

\[
                  \lambda(H)>h\beta.                 \tag{2.2}
\]

No such edge-connectivity/load inequality is currently proved for the
canonical plane-tree host with the full OR/compiler notion of
transparency.

## 3. Consequence for bounded task regeneration

Suppose at one Pascal transition there are at most `h=O(1)` task menus in a
single static connector host `H`.  Select one edge from each menu before
topology completion.  If the selected edges form a forest, Theorem 2.1
absorbs them into the global connector tree at no extra physical seam cost.

For ordered-shift portals on distinct raw rank-`m` tails, the common
coordinate potential proves that **every** transversal is a forest before
contraction.  Therefore, once a portal-to-host lift is available, the
topology row needs no dynamic scattering invariant.  The recursive state
can be reduced to:

1. bounded tasks are born before the child topology is completed;
2. each task has one literal portal in the child's static connector host;
3. the selected host edges are independent; and
4. the remaining tree switches are transparent to the packet tickets.

Fresh menus need only be produced at the next Pascal transition.  They do
not have to remain live after the current transition's tree has been fixed.
This is strictly weaker than maintaining a private-head bank through all
intermediate contractions.

## 4. Why the existing ordered-portal theorem does not yet instantiate it

There are three different graphs which must not be identified.

### 4.1 Raw SCD-chain graph

Every rank-`m` root belongs to a distinct SCD chain.  Hence the ordered
portal theorem works in the graph

\[
 K_{\rm SCD}:
 \quad
 \text{vertices = raw SCD chains, edges = selected Johnson portals}.
                                                        \tag{4.1}
\]

The potential proof gives a forest in `K_SCD`.

### 4.2 Completed-factor component graph

The small protected-factor theorem embeds the literal packet incidence bank
in **some** spanning q1 two-factor.  It does not control which SCD chains
the completion puts on the same factor cycle.  If

\[
 \rho:V(K_{\rm SCD})\longrightarrow
       \{\text{cycles of the completed factor}\}
                                                        \tag{4.2}
\]

is the induced contraction, a raw portal can become a loop, and two raw
portal edges can become parallel.  Graphic independence need not survive
`rho`.

### 4.3 Canonical pull host

Mütze's static host is still more specific: it is the auxiliary plane-tree
graph of the canonical lexical factor, and its edges are canonical
alternating hexagons.  A forward Johnson edge between two SCD roots is not,
merely from that description, one of those hexagons.  Conversely, embedding
the packet path into an arbitrary q1 two-factor does not place it in the
canonical lexical factor.

Thus the current implications stop at

\[
 \begin{aligned}
 &\text{ordered raw portal choices}
      \Longrightarrow\text{forest in }K_{\rm SCD},\\
 &\text{small packet bank}
      \Longrightarrow\text{contained in some q1 two-factor},
 \end{aligned}                                      \tag{4.3}
\]

and do **not** imply

\[
 \text{selected canonical pulls forming a forest in the lexical
 plane-tree host}.                                  \tag{4.4}
\]

## 5. Sharp failure at the initial quotient

The obstruction can occur before the first topology merge.

Take four raw SCD vertices `a,b,c,d` and two selected portal edges

\[
                         ac,\qquad bd.               \tag{5.1}
\]

They form a forest.  If the base-factor completion identifies `a` with `b`
and identifies `c` with `d`, their images are two parallel edges.  Their
graphic rank is one, so no spanning tree of the factor-component graph can
contain both.

Even one portal can fail earlier.  Let the actual connector host be the
path

\[
                           A-B-C.                    \tag{5.2}
\]

The ambient Johnson edge `AC` is a one-edge forest, but it is not an edge
of the host and therefore cannot belong to any host spanning tree.

Taking the full Johnson graph as `H` does not by itself repair this point.
A Johnson edge is only an abstract adjacency of owner roots.  A spanning
tree of such adjacencies may branch, whereas direct concatenation of path
components has only endpoint capacity two.  One still needs either a
tree-compatible alternating-circuit realization (as in the canonical pull
family) or an explicit free-port theorem for every selected tree edge.

These examples prove that ambient monotonicity and raw SCD independence do
not suffice.  The earliest possible collapse is the **initial quotient from
raw chains to the chosen base-factor components**, not a late stage of the
merge tree.  Component scattering is solving the wrong problem if that
quotient has not first been controlled.

## 6. Exact missing lemma

The weakest theorem which makes the forest-first reordering rigorous is the
following.

### Portal-to-pull lift lemma

For every fixed bounded bank of prepared ordered-shift or pivot tasks, and
all sufficiently large `m`, there exist:

1. one base factor `P` with a connected static compatible connector host
   `H`;
2. one literal task packet for every task, embedded in `P`;
3. a connected spanning transparent subhost `H_D subseteq H`;
4. one host edge `e_i in E(H_D)` attached to each task packet; and
5. a choice of the `e_i` whose set is a forest in `H_D`.

Theorem 2.1 would extend those edges to the required transparent spanning
tree and complete the topology in the same transition.  In a
canonical-Mütze implementation, item 3 says that the literal portal packet
must be identified with, or carried transparently by, a canonical
flippable-pair hexagon.  In a direct SCD implementation, it is enough to
construct a static compatible connector family whose vertices really are
the raw SCD chains.

The current record proves none of these two physical identifications.  It
does prove the graphic independence needed after either identification is
made.

## 7. Revised frontier

For bounded task banks, the alternatives are now clean.

* **Forest-first route.**  Prove the portal-to-pull lift lemma.  Then select
  portals before topology completion and extend them to the global tree;
  no scattering or private-head regeneration is needed inside that child.
* **Topology-first route.**  If tasks are exposed only after an arbitrary
  factor has already merged raw chains, then the sharp graphic-flat/Rado
  cuts and component-scattering problem remain unavoidable.

The forest-first route is strictly shorter.  Its unresolved content is not
graph theory, but one correlated physical host theorem:

\[
 \boxed{
 \text{bounded task birth before topology}
 +\text{ portal-to-static-host lifting}
 +\text{ switch transparency}. }
                                                        \tag{7.1}
\]

Once (7.1) is supplied, ordinary graphic basis extension completes the
merge tree around the already selected portals.

The subsequent direct-pull audit sharpens the canonical-host option.  A
fixed ordered-shift star meets at most two direct canonical pull labels and
at most eight heads in the complete canonical decorated-rail family.  The
standard labelled plane-tree pull host has edge-connectivity exactly one,
at its unique star bridge.  Therefore neither the linear raw portal degree
nor an `o(m)` bound on forbidden pulls supplies (7.1) by expansion.  Any
canonical implementation must plant literal occurrences and reserve that
bridge explicitly; otherwise a noncanonical redundant connector host is
required.
