# Pascal reachable upper tasks: exact star-cover test and the tagged-descendant obstruction

Date: 2026-07-31  
Lane: A, buffered-hex upper guards after Pascal lift  
Status: exact positive subclasses and a dimension-uniform obstruction proved;
the present reachable-state hypotheses do not imply an \(O(d)\) ray cover

## 0. Verdict

The current Pascal identities do **not** imply that the reachable
buffered-hex task set has an \(O(d)\) upper-ray cover.

Two positive facts are exact.

1. A child target with one fully internal protected parent occurrence,
   disjoint from every candidate support at its assigned anchor, has empty
   bad-pair graph.
2. If the exposed tasks have bad-pair graphs whose **union** has vertex-cover
   number \(O(d)\), then the frozen star-cover theorem removes only
   \(O(md)\) choices.

Neither bounded task count nor an \(O(d)\) number of nested target rays
proves the second fact.  The Pascal task/source projection admits a valid
two-tag descendant label whose completed witness state can, under the
explicit last-witness hypotheses below, have a bad graph containing

\[
                             K_{m,m-q+1}.                         \tag{0.1}
\]

For \(2\le q\le d=o(m)\) its vertex-cover number is
\(m-q+1=\Theta(m)\), not \(O(d)\).  Thus even one task label can violate
the desired cover after its omitted occurrence state is completed, unless
it has an occurrence-private old witness or a packet-private replacement
ray.  This is a no-deduction theorem, not a construction of an obstructed
regenerative Pascal state.

The precise live hypothesis is therefore occurrence-level:

> every exposed Pascal descendant must be assigned to an anchor for which
> its last-witness/replacement bad graph participates in one common
> \(O(d)\) star cover.

Tag type, rank, the number of tasks, and the existence of nested seam rays
are insufficient by themselves.

## 1. The actual four-sector anchor

Let

\[
 V=[2m-1],\qquad \Omega=V\cup\{x,y\},
 \qquad P\in\binom V{m-1}.                                      \tag{1.1}
\]

The \(A\)-\(X\) Pascal attachment uses the source incidence

\[
       C_0=P+x\ \subset\ U_0=P+x+y.                              \tag{1.2}
\]

For

\[
       b\in C_0,\qquad c\in\Omega\setminus U_0=V\setminus P,      \tag{1.3}
\]

the standard incidence hexagon is

\[
 C_0,\ U_0,\ U_0-b,\ U_0-b+c,\ C_0-b+c,\ C_0+c.                  \tag{1.4}
\]

Both parameter shores have order \(m\).  The attachment theorem proves that
the central component tasks can be assigned injectively to incidences of
the form (1.2).  It does not impose an arbitrary-width upper guard on the
\(m^2\) circuits at the chosen incidence.

For a target \(Y\), let \(G_Y\) be the bipartite graph on the two parameter
shores whose edge \((b,c)\) means that the corresponding packet cuts every
old \(Y\)-witness and creates no new \(Y\)-interval.  The exact theorem
already frozen in the companion note says that the complete upper bank has

\[
       G_{\rm bad}=\bigcup_YG_Y                                  \tag{1.5}
\]

and rejects at most \(Kmd\) pairs whenever

\[
                         \tau(G_{\rm bad})\le Kd.                 \tag{1.6}
\]

Here \(\tau\) is vertex-cover number, equivalently maximum matching number
by König.

## 2. An admissible tagged descendant label with a conditional linear cover obstruction

Choose

\[
 E\subseteq V\setminus P,\qquad |E|=q-1,\qquad
 Y=P\cup E\cup\{x,y\}.                                            \tag{2.1}
\]

Then \(Y\) has rank \(m+q\).  It is exactly the two-tag child of the parent
target

\[
                            Y_0=P\cup E,                           \tag{2.2}
\]

which has rank \(m+q-2\).  Thus for \(q\ge2\) it is a legitimate Pascal
descendant label, including the case in which \(Y_0\) is a parent middle
target.

### Theorem 2.1 (tagged-descendant no-spill cut)

Suppose the selected packet at (1.2) cuts every protected old occurrence of
\(Y\), and every available replacement interval for \((b,c)\) contains a
\(c\)-bearing atom of (1.4).  Suppose also that no alternative packet-private
interval avoids that atom.  Then

\[
        C_0\times\bigl((V\setminus P)\setminus E\bigr)
              \subseteq E(G_Y).                                  \tag{2.3}
\]

Consequently

\[
 |E(G_Y)|\ge m(m-q+1),\qquad
 \tau(G_Y)\ge m-q+1.                                               \tag{2.4}
\]

#### Proof

Every \(c\)-bearing atom contributes coordinate \(c\) to the accumulated
union.  Since

\[
                  Y\cap(V\setminus P)=E,                           \tag{2.5}
\]

the exact no-spill row forces \(c\in E\).  Hence every \(c\) outside \(E\)
is bad for every one of the \(m\) choices of \(b\), proving (2.3).  The
displayed subgraph is \(K_{m,m-q+1}\), whose matching and vertex-cover
numbers are both \(m-q+1\).  \(\square\)

### Corollary 2.2 (reachability alone is insufficient)

If \(d=o(m)\), then for every fixed \(q\ge2\), and more generally for
\(q\le d\), Theorem 2.1 gives

\[
                         \tau(G_Y)=\Omega(m)\not=O(d).              \tag{2.6}
\]

The conditional schema uses only one task label.  Therefore:

* an absolute bound on the number of reachable tasks does not imply
  star-cover protected rays;
* the hypothetical exposure row \(|{\cal U}|\le4\Phi+b_0\) does not imply
  the star-cover property, even when \(\Phi=O(1)\); and
* a task label being a genuine Pascal descendant does not imply a cylinder
  guard.

The theorem is conditional on the explicit last-witness and forced
\(c\)-bearing-ray hypotheses.  It does not say that every occurrence of the
label (2.1) is obstructed.  A fully internal old witness or a private
replacement interval removes this obstruction.

## 3. What the proved Pascal identity does give

For a Pascal cycle trace, index cyclically and put
\(F_i=C_{i-1}\cap C_i\).  For a rooted Pascal path
\(C_0,\ldots,C_{N-1}\), let \(F_0\) be its declared Pascal root facet and
put \(F_j=C_{j-1}\cap C_j\) for \(1\le j<N\).  For \(s\ge1\), the exact
Pascal identity is

\[
       \bigcup_{j=0}^{s}F_{i+j}
          =\bigcup_{j=0}^{s-1}C_{i+j}.                             \tag{3.1}
\]

Here the indices are cyclic in the cycle case; in the rooted-path case
\(0\le i\) and \(i+s<N\), with the declared root convention used when
\(i=0\).

Thus a fully internal protected parent occurrence produces both child
descendants without loss.

### Proposition 3.1 (internal-occurrence zero graph)

If a child target \(Y\) has one protected occurrence lying wholly in a
transported fragment and disjoint from every candidate packet support in
its assigned list, then

\[
                              E(G_Y)=\varnothing.                   \tag{3.2}
\]

#### Proof

The occurrence is never cut.  It supplies the first alternative in the
exact last-witness theorem for every \((b,c)\).  \(\square\)

This is the correct free part of Pascal upper transport.  Only targets for
which every protected occurrence meets the exposed cut kernel enter the
ray-cover problem.

### Proposition 3.2 (finite exposed-bank reduction)

Let \({\cal U}_{\rm exp}\) be the exposed child targets.  If, for each
\(Y\in{\cal U}_{\rm exp}\), a cover \(Q_Y\) of \(G_Y\) is exhibited and

\[
                         \left|\bigcup_{Y\in{\cal U}_{\rm exp}}Q_Y\right|
                              \le Kd,                              \tag{3.3}
\]

then the complete reachable task bank has the star-cover property and at
most \(Kmd\) packet choices are rejected.

#### Proof

Internal targets have empty graphs by Proposition 3.1.  The union in (3.3)
covers every remaining graph, hence covers (1.5).  Apply (1.6).
\(\square\)

The shared union in (3.3) matters.  Charging \(O(d)\) new cover vertices
for each target may be linear in the number of targets and is not a uniform
\(O(d)\) theorem.

## 4. Why nested Pascal rays do not close the cover

The block-reroot theorem proves a useful target-space statement.  If the
unprotected defect tower partitions into \(h=O(d)\) nested depth rays, then
\(h\) suitable seams can in principle supply all their OR labels.

This is not a parameter-space star-cover statement.  One nested ray may
have the graph in (2.3), with cover number \(m-q+1\).  Therefore

\[
 h=O(d)\text{ target rays}
 \quad\not\Longrightarrow\quad
 \tau(G_{\rm bad})=O(d).                                           \tag{4.1}
\]

To make the implication valid one needs, in addition, a **common ray-order
certificate**: every failed required-versus-forbidden first-arrival
comparison across all exposed rays is incident with one global active label
set of order \(O(d)\).  That active set is then the cover in (3.3).

Equivalently, every exposed ray may carry a private replacement-witness
token; packets which threaten it must conflict with that token.  This is the
token form used by the composable buffered-hex theorem.

## 5. Interaction with the private-anchor theorem

The Pascal attachment theorem supplies an injective source-incidence
assignment for the unguarded central component tasks.  The weighted-anchor
audit then shows that injectivity does not control auxiliary one-free roles
or cap tickets.  The upper result here is orthogonal:

* injective anchors remove source-fixed cross-list collisions;
* weighted upper/lower codegrees control ordinary physical token load;
* the star-cover property controls arbitrary-width upper list loss; and
* cap-gammoid cuts control complete compiler tickets.

All four must hold on the same selected anchors.  Passing any three does not
imply the fourth.

## 6. Exact surviving Pascal hypothesis

The strongest unconditional conclusion is negative but sharply scoped:
the current definition of a reachable Pascal task does not force an
\(O(d)\) ray cover.

A sufficient all-dimensional replacement is:

### Pascal exposed-ray star-cover (PERSC)

After choosing the actual private anchor of every nonexceptional child task,

1. every transported target has one anchor-disjoint internal witness;
2. the union bad graph of the remaining exposed descendants has
   vertex-cover number at most \(Kd\);
3. for every exposed target and every parameter pair not incident with the
   chosen global cover, there is an anchor-disjoint old witness or a
   tokenized private replacement ray; and
4. the cover and replacement tokens coexist with the residence, physical
   topology, global token-load and cap-ticket states.

Under PERSC, every task list retains \(m^2-O(md)\) upper-safe circuits.
With the separate \(O(md)\) global conflict-degree and composition
hypotheses, the buffered-hex independent-transversal theorem applies.

No current Pascal/RSB theorem proves Item 2.  The minimal obstruction to
attack is already one task: eliminate the \(K_{m,m-q+1}\) no-spill face of
Theorem 2.1 by exhibiting an internal or packet-private witness, or show
that the actual regenerative state cannot expose such a descendant.

## 7. The per-seam compound collar

The whole-collar proposal is stronger than targetwise repair: one selected
pair \((b,c)\) must restore every old-lost target at one changed seam.
Canonical PBBS extreme rays give an exact test of this proposal.

Fix one side of a seam, with service endpoint
\(u\in\binom{\Omega}{m+1}\), where \(|\Omega|=2m+1\).  Let the actual lost
targets on that side be partitioned into canonical nested extreme rays,
meaning outward geodesic rays whose union rank rises by one on every edge.
Every ray \(\rho\) has one departure key

\[
                         \kappa_\rho\notin u,                       \tag{7.1}
\]

common to all depths in that ray.  Assume, as required by the canonical
endpoint theorem, that these ray lists exhaust the old losses assigned to
this side.  Let the buffered packet expose a Johnson-neighbour menu

\[
              v_{b,c}=u-\{b\}+\{c\},\qquad
              b\in B\subseteq u,\quad
              c\in C=\Omega\setminus u,                              \tag{7.2}
\]

with \(|B|=|C|=m\).  Put

\[
                         K=\{\kappa_\rho:\rho\text{ active}\}.       \tag{7.3}
\]

### Theorem 7.1 (canonical compound-collar obstruction)

Under canonical extreme-ray endpoint reuse, one pair \((b,c)\) repairs the
entire one-sided compound collar if and only if

\[
                              K\subseteq\{c\}.                      \tag{7.4}
\]

Consequently:

1. if \(K=\{\kappa\}\), the safe pairs are exactly
   \(B\times\{\kappa\}\), while
   \[
       G_{\rm collar}=K_{m,m-1},\quad
       |E(G_{\rm collar})|=m(m-1),\quad
       \tau(G_{\rm collar})=m-1;                                  \tag{7.5}
   \]
2. if \(|K|\ge2\), no pair is safe and
   \[
       G_{\rm collar}=K_{m,m},\qquad \tau(G_{\rm collar})=m.       \tag{7.6}
   \]

Additional upper guards can only enlarge these bad graphs.

#### Proof

The exact PBBS endpoint-replacement theorem says that every target in ray
\(\rho\) is restored precisely when \(\kappa_\rho\in v_{b,c}\).  The key is
absent from \(u\), and (7.2) adds exactly the one coordinate \(c\).
Therefore \(\kappa_\rho\in v_{b,c}\) iff \(c=\kappa_\rho\).  All rays are
restored precisely when every member of \(K\) equals \(c\), which is (7.4).
The two graph calculations and their König cover numbers are immediate.
\(\square\)

### Corollary 7.2 (nested size \(O(d)\) has the wrong polarity)

Even one nonempty nested ray, containing any number up to \(O(d)\) of
all-depth target labels, rejects \(m(m-1)=\Theta(m^2)\) pairs in the
canonical menu.  It leaves one **safe** \(c\)-star rather than a union of
\(O(d)\) **bad** stars.  Hence

\[
 \text{one changed seam with }O(d)\text{ nested losses}
 \quad\not\Longrightarrow\quad
 \tau(G_{\rm collar})=O(d).                                      \tag{7.7}
\]

If the two sides of the seam have independent nonempty canonical collars,
each side must pass its own key condition.  Failure on either side already
gives the lower bound (7.5), so a two-sided or three-rail packet cannot
improve this conclusion merely by carrying other rails which create no
noncanonical replacement witness.

This is an exact no-go for the standard one-insertion endpoint reuse.  It is
not a no-go for noncanonical seam intervals: a deeper crossing interval may
restore a ray even when the foreign endpoint omits its key.

### Theorem 7.3 (key-preloaded buffered collar)

There is an exact favorable-polarity sufficient condition.  Suppose a
noncanonical buffered rail offers endpoints

\[
              v_{b,c}=u^+-\{b\}+\{c\},\qquad K\subseteq u^+,        \tag{7.8}
\]

and every ray is restored whenever its key remains in \(v_{b,c}\), with all
no-spill/no-deficit and other protected-target rows already guaranteed by
private witnesses.  Then every bad pair has \(b\in K\), so

\[
 G_{\rm collar}\subseteq(K\cap B)\times C,\qquad
 \tau(G_{\rm collar})\le |K|,\qquad
 |E(G_{\rm collar})|\le m|K|.                                    \tag{7.9}
\]

Thus \(|K|=O(d)\) gives the desired \(O(d)\) star cover and \(O(md)\)
loss.

#### Proof

The only way (7.8) can lose a preloaded key is to choose that key as the
deleted coordinate \(b\).  The remaining asserted rows make key retention
sufficient.  Therefore the displayed \(b\)-stars cover every bad pair.
\(\square\)

Theorem 7.3 gives a favorable-polarity sufficient whole-collar theorem:
construct a literal buffer rail which preloads all live seam keys, or provide
noncanonical/private replacement intervals with the same favorable
bad-star polarity.  The canonical Pascal/PBBS endpoint has the opposite
polarity because every departure key is absent from \(u\).  No current
three-rail construction proves this preload while preserving physical
degree, the full old upper bank, residence, topology and common cap.
