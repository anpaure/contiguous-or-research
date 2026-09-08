# Thread D: Pascal residual reachability and controlled-debt packet acceptance

Date: 2026-07-31  
Status: pure-mathematical audit and exact finite-boundary theorem.  This
note proves no all-parameter construction and no K17 equality result.

## 0. Verdict

The Pascal determinant split has two exact consequences which must be kept
separate.

1. Two literal **full** canonical parent rails cannot be placed in one
   Catalan linear matching.  Exact palette completion forces enough
   cross-rail edges to create a physical cycle.  This is a no-go for the
   scalar two-full-parent product, not for every boundary-deficient Pascal
   recursion.
2. After an atom $q:T\to H$ is selected and all atoms conflicting with
   its four labels are removed, the residual selection is legal exactly
   when it is acyclic and has no path $H\leadsto T$.  For a packet of
   additions this becomes one exact boundary-reachability test.

Consequently the determinant-side state of a controlled-debt packet is not
a scalar parent value.  It consists of named palette debts, named physical
in/out sockets, and the directed reachability relation on the live
boundary.  This coordinate composes with the item2169 common-core linkage
signature only as a **jointly realizable product**.  Physical reachability
does not imply a simultaneous alternating linkage, and a strict-gammoid
answer does not imply physical acyclicity.

## 1. Independent audit of the two-full-parent obstruction

Distinguish $x,y$ and put

\[
 \Omega=\Omega'\sqcup\{x,y\},\qquad |\Omega'|=2m-2.
\]

Write

\[
 C'=\operatorname {Cat}_{m-1},\qquad
 M'=\binom{2m-2}{m-1}=mC',\qquad
 N'=\binom{2m-2}{m-2}=(m-1)C'.                    \tag{1.1}
\]

A full $x\bar y$ parent occupies $N'$ physical edges on the rail

\[
 x+\binom{\Omega'}{m-1},
\]

and a full $y\bar x$ parent occupies $N'$ edges on the analogous
$y$-rail.  Each rail has $M'$ vertices.

After those two parents have used every lower and upper colour containing
exactly one of $x,y$, exact outer-palette completion forces

\[
 \binom{2m-2}{m-1}-\binom{2m-2}{m-3}
   =\operatorname {Cat}_m=:C                              \tag{1.2}
\]

atoms from a lower colour avoiding $x,y$ to an upper colour containing
both.  Such an atom necessarily has

\[
 U=L\cup\{x,y\},
\]

and its physical edge is $(L+x)(L+y)$.  Hence the graph induced by the two
middle rails has

\[
 |V|=2M',\qquad |E|=2N'+C,
\]

and therefore

\[
 |E|-|V|=C-2C'
 =\frac{2(m-2)}{m+1}C'\ge0.                         \tag{1.3}
\]

A finite forest on $2M'$ nonempty vertices has at most $2M'-1$ edges,
so this induced graph contains a cycle.  The contradiction is orientation
independent.  It proves the following scoped statement.

### Theorem 1.1 (exact scalar two-full-parent no-go)

For \(m\ge3\), no Catalan linear matching contains both canonical full embedded parent
matchings.  If the forced $C$ cross edges are retained, at least

\[
 C-2C'+1                                               \tag{1.4}
\]

parent edges must be omitted before the induced edge count even reaches
the forest bound.

The same edge-count contradiction holds at the formal \(m=2\) boundary,
where \(|E|=|V|\).  The last number is not a lower bound for an arbitrary Pascal braid, since
changing the named palette debts may also change the forced cross bank.
Thus Theorem 1.1 forces boundary-deficient parents but does not rule out a
non-scalar recursion.

## 2. Exact one-atom contraction

Let $D$ be the directed physical graph of a residual atom selection, and
let $q:T\to H$ be a proposed atom.  First delete every residual atom which
shares the lower colour, upper colour, tail, or head of (q).  The remaining
palette and degree constraints are then precisely the constraints with the
four resources used by $q$ removed.

### Lemma 2.1 (contraction criterion)

\[
 D+q\text{ is acyclic}
 \quad\Longleftrightarrow\quad
 D\text{ is acyclic and }H\not\leadsto_D T.          \tag{2.1}
\]

#### Proof

If $D$ has a directed cycle, it remains after adding $q$.  If $D$
contains $H\leadsto T$, that path followed by $T\to H$ is a directed
cycle.  Conversely, every directed cycle in $D+q$ which is not already in
$D$ uses $q$; deleting $q$ from it leaves a directed path
$H\leadsto T$ in $D$.  □

Thus a fixed contraction needs one reachability bit in addition to residual
acyclicity.  It is not represented by the scalar value of the smaller
enumerator.

## 3. Exact composition through a live boundary

Let $D_1,\ldots,D_s$ be acyclic directed fragments.  Their interiors are
pairwise disjoint; every overlap and every endpoint of a new glue arc lies
in a named boundary $B$.  Define

\[
 R_i=\{(u,v)\in B^2:u\leadsto_{D_i}v\},              \tag{3.1}
\]

where reachability uses a nonempty directed path.  Let $A\subseteq B^2$
be the selected glue arcs, and form the boundary quotient

\[
 Q(B)=\bigl(B,A\cup R_1\cup\cdots\cup R_s\bigr).    \tag{3.2}
\]

### Theorem 3.1 (boundary contraction theorem)

The glued directed graph

\[
 D=D_1\cup\cdots\cup D_s\cup A
\]

is acyclic if and only if $Q(B)$ is acyclic.  Moreover its reachability
relation on any retained exterior boundary is the corresponding restriction
of the transitive closure of (Q(B)).

#### Proof

A directed cycle of $Q(B)$ expands every $R_i$-arc to a witnessing path
inside $D_i$, giving a directed closed walk and hence a directed cycle in
$D$.  Conversely, a directed cycle in $D$ cannot lie in one $D_i$.
Compress each maximal subpath lying in one fragment to its boundary
endpoints.  The resulting directed closed walk lies in $Q(B)$, which
therefore contains a directed cycle.  The same expansion/compression proves
the reachability assertion.  □

For one residual core and a bank of new atoms, Theorem 3.1 says simply:

\[
 D^\circ\cup A\text{ is acyclic}
 \quad\Longleftrightarrow\quad
 (B,R^\circ\cup A)\text{ is acyclic}.               \tag{3.3}
\]

This is the batch form of Lemma 2.1.

### Corollary 3.2 (sharpness of the reachability state)

Among residual DAGs with the same other interface data, and for an
unrestricted catalogue of future boundary arcs, the full relation
\(R\subseteq B^2\) is the coarsest universally sufficient acyclicity
signature.  Indeed, if two residual DAGs differ on \(h\leadsto t\) and
the separating arc is socket-compatible, the completion consisting of the
single arc \(t\to h\) rejects the first and accepts the second.

For a restricted glue catalogue one may quotient boundary states which no
allowed continuation distinguishes.  Mere rail counts, component counts,
or socket counts are not sufficient in general.

## 4. The smallest determinant-side rail state

Within a fixed declared completion interface, a boundary-deficient rail
exports

\[
 \mathfrak R(F)=
 \bigl(
   \Delta_{\rm low},\Delta_{\rm up},
   c^+,c^-,
   R_F
 \bigr).                                             \tag{4.1}
\]

Here

* $\Delta_{\rm low},\Delta_{\rm up}$ are the **named** unfilled outer
  palette resources;
* $c^+(v),c^-(v)\in\{0,1\}$ are the named remaining outgoing and incoming
  capacities at live physical sockets; and
* $R_F$ is directed reachability on every socket or adhesion vertex which
  a future atom may use.

A completion is determinant-legal exactly when it fills the prescribed
palette resources once, respects every socket capacity, and passes the
acyclic quotient test of Theorem 3.1.  Identities, not only cardinalities,
are required: changing one named palette or socket changes the legal atom
catalogue, while changing one bit of $R_F$ can change contraction
acceptance by Corollary 3.2.

There is one essential operational qualification.  A summarized
reachability relation supports **addition, gluing, transitive closure, and
forgetting closed boundary vertices**.  It does not support arbitrary later
edge deletion: deleting an edge can destroy an unknown subset of paths, and
that information cannot be recovered from $R_F$ alone.  Therefore a long
switch packet must either

1. freeze a delete-first residual core containing none of the packet's
   variable atoms, and add candidate banks to that core; or
2. recompute the exact reachability signature after every deletion stage.

The support-frozen common-core normal form uses the first, noncircular
option.

## 5. Product with the common-core linkage signature

The relation $R_F$ lives in the directed physical atom graph.  The
item2169 signature lives in the alternating orientation of an augmented
bipartite occurrence graph relative to a fixed common-core matching.  It
records simultaneous vertex-disjoint augmenting path fragments, with named
pairings when pairings matter.

These coordinates are logically independent.

* Pairwise physical reachability is sufficient for the directed-cycle
  question but says nothing about competition between several augmenting
  paths.
* A strict-gammoid linkability answer or even a complete pairing-resolved
  alternating signature says nothing about a physical path
  $H\leadsto T$.

Let $Z$ be a support-frozen packet, $D_Z$ its physical residual core,
$H_Z$ its augmented occurrence core, and $a$ a bundled column choice.
The exact combined boundary table is therefore

\[
 \Sigma_Z=
 \bigl\{
   (a,R,\mathcal L):
   a\text{ realizes physical reachability state }R
   \text{ and alternating linkage state }\mathcal L
 \bigr\}.                                           \tag{5.1}
\]

Composition must join entries arising from the same compatible column
choices.  Taking the Cartesian product of a feasible reachability state and
a separately feasible gammoid state is unsound.  If the live physical
boundary and the exposed matching debt are bounded, (5.1) is a finite
boundary state even when the packet contains a growing number of internal
circuits or its augmenting paths are long.

More explicitly, a physical boundary of order \(b\) has at most
\(2^{b(b-1)}\) directed-relation tables before transitivity and acyclicity
prune them.  If the alternating linkage interface has \(p\) named terminals,
item2169's safe pairing-pattern bound is \(4^p p!\).  Thus, apart from the
named debt labels, a crude joint bound is
\[
                 2^{b(b-1)}\,4^p p!.
\]
This is a width bound, not an assertion that every formally paired state is
jointly realizable.

## 6. Exact acceptance test for a controlled-debt rethread packet

Consider a K17 central packet or the required $m=5$ interior rethread.
Let $Z$ contain every old atom changed anywhere in the macro, delete $Z$
first, and expose every affected fragment endpoint.  Let $A_j$ be the new
atom bank at an intermediate state $j$, and $A_*$ the accepting endpoint
bank.  The packet is exact on the determinant/common-core coordinates when:

1. **named debt:** each $A_j$ obeys its declared temporary palette and
   socket debts, and $A_*$ fills every required debt exactly;
2. **physical contraction:** every state which is required to be physical
   satisfies
   \[
     (B,R_Z\cup A_j)\text{ acyclic};                 \tag{6.1}
   \]
3. **common-core repair:** the endpoint bundled columns admit the required
   pairing-resolved, vertex-disjoint augmenting linkage in $H_Z$, hence
   meet the exact common-core Hall/rank row;
4. **same witness:** conditions 1--3 are realized by one column selection,
   i.e. one entry of the joint table (5.1), not by separately chosen
   witnesses.

For an ordered transparent gluing list, apply (6.1) after every
nontransparent addition and carry the transitive-closure restriction to the
next live boundary.  If only the macro endpoint is an accepting state,
temporary palette or matching debt is allowed, but a claimed intermediate
physical forest must still pass (6.1).

These four rows do **not** imply residence, deeper shadow support, the
erosion/compiler matching, the undirected endpoint-socket topology, or
primitive voltage.  Those remain correlated endpoint conditions.  In
particular item2183's 31 bounded length-two one-runs survive every intact
path permutation, reversal, and socket choice.  Item2188 supplies the
required nontrivial interior rethread at `m=5`: its exact-palette 42-path
forest has no internal run below three.  It still owes 21 deeper targets,
endpoint joining, common-decoration transport and the compiler.  The Pascal
reachability test can certify that a chosen directed realization has
introduced no directed cycle; it neither constructs that realization nor
certifies residence or flags for it.

## 7. Precise surviving gate

The algebraically minimal noncircular recursion object is a
boundary-deficient, delete-first rail packet carrying the joint state

\[
 \boxed{
 (\text{named palette debt},\text{named sockets},
  R_{\rm physical},\mathcal L_{\rm augmented})
 }                                                    \tag{7.1}
\]

together with the independent protected residence, shadow, topology,
voltage, and compiler coordinates required by the application.  Packet
size may grow.  What must remain bounded for a finite-state induction is
the live boundary and unresolved linkage/debt, not the total internal
support.

Theorems 1.1--3.1 prove why both boundary deficiency and reachability are
necessary.  They do not prove that an accepting packet exists for K17 or
uniformly in $m$.
