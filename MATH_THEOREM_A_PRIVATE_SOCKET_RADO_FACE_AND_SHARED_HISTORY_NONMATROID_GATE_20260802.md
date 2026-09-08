# Private socket Rado faces and the shared-history nonmatroid gate

**Date:** 2026-08-02  
**Lane:** A, central common-base/reset integrality  
**Status:** exact sufficient matroid theorem, a smallest abstract
two-port obstruction, and a literal obstruction in the authenticated K17
relaxed-nine socket catalogue.  This note does **not** prove or disprove
matroidality of the family of short banks which extend to a complete
canonical K17 cycle cover.  It does not prove residence, upper coverage,
topology, a source word, or a compiler.

## 0. Verdict

The cotransversal outer matroid

\[
                         M_{\rm short}=(M/\mathcal F)^*
\]

from the bottom-token theorem has an exact matroid partner only after a
real privacy theorem is supplied.

If every accepted socket is represented by one ticket object, different
ticket objects have disjoint complete literal footprints, and selecting a
short row merely matches that row injectively to one compatible ticket,
then the socket-feasible short sets form a transversal matroid.  More
generally, if all residual ticket conflicts form one matroid (in particular
a laminar matroid), the induced short-set system is a Rado matroid.  Edmonds'
matroid-intersection criterion with `M_short` is then exact for a common
independent set of the required size.  Equivalently, truncate the Rado
matroid to that size and ask for a common basis; the untruncated Rado
matroid need not have the same rank as `M_short`.

The real common-state socket system does not have this form automatically.
A socket consumes a predecessor port and a successor port and, when a long
role is used on both sides, requires the same flag.  Two crossing capacity
partitions already destroy matroid exchange.  This is not only an abstract
warning: the frozen round-47 relaxed-nine K17 catalogue contains three
shorts with unique literal sockets for which

\[
             I=\{4183\},\qquad J=\{4218,4250\}
\]

are each socket-packable, while neither `I+4218` nor `I+4250` is.  Thus the
hereditary partial shared-socket packing system violates matroid
augmentation on the smallest possible number of ground elements.

Finally, the frozen Boolean `C6`, `C8`, and `C10` bottom-relay actuators do
not select a new short bank.  Their alternating circuits use real bottom
tokens only and use the same physical slot palette in both phases, so the
dummy-matched slot set—and hence the basis of `M_short`—is unchanged.  A
whole protected actuator can become **one** ticket only after a separate
literal theorem exports one private short socket from it.  The existing
resource identities do not prove that export.

## 1. The exact private-ticket theorem

Let `E` be a set of candidate short hard slots and let `T` be a set of
completed socket tickets.  A ticket is completed only when its owner,
address, predecessor/successor histories, cap/reset state and every
protected resource have already been fixed and replayed.  Let

\[
                         G\subseteq E\times T                 \tag{1.1}
\]

be the literal compatibility graph.

Call the bank **private** when the full resources belonging to distinct
ticket objects are disjoint.  In particular, after the edge `(e,t)` is
chosen there is no remaining constraint coupling `t` to a second chosen
ticket.  A short set `S` is ticket-feasible when it can be matched
injectively into `T` through (1.1).

### Theorem 1.1 (private tickets give the required transversal matroid)

The ticket-feasible subsets of `E` are the independent sets of the
transversal matroid presented by `G`.  If every accepted table requires
exactly `r` short slots, then its private socket-complete short sets are
exactly the bases of the rank-`r` truncation of this matroid (provided its
rank is at least `r`).

Consequently, when `r=1748`, transversal rank below `1748` is immediately
infeasible.  Otherwise let `M_sock` denote the rank-`1748` truncation of
this transversal matroid (the identity operation when its rank is exactly
`1748`).  A short set which is both outer feasible and private-socket
complete exists if and only if

\[
 r_{M_{\rm short}}(X)+
 r_{M_{\rm sock}}(E-X)\ge1748
 \qquad(X\subseteq E).                              \tag{1.2}
\]

#### Proof

The first statement is the defining matching representation of a
transversal matroid.  Privacy says that an injective ticket assignment is
already a simultaneous literal assignment; there are no omitted shared
rows.  Truncation is a matroid operation and makes precisely the feasible
`r`-sets its bases.  Equation (1.2) is Edmonds' common-base theorem applied
to that truncation.  \(\square\)

Privacy is stronger than pairwise distinct ticket names.  Two tickets with
different names but the same predecessor role, successor role, history
cell, cap coordinate or protected occurrence are not private.

Theorem 1.1 is automatically sound as a sufficient physical subface.  To
turn failure of (1.2) into a no-go for a larger declared socket class, one
must additionally prove **decomposition completeness**: every realization
in that class factors into the ticket modes of (1.1).  Without that reverse
map, the rank cut excludes only the private subatlas.

### Theorem 1.2 (laminar/Rado extension)

Suppose ticket subsets allowed by the residual shared-resource rows are the
independent sets of a matroid `N` on `T`.  Declare `S subset E` feasible
when it can be matched through `G` to an `N`-independent ticket set.  Then
these feasible subsets form the Rado matroid `R(G,N)`, whose rank is

\[
 r_R(X)=\min_{Y\subseteq X}
       \bigl(|X-Y|+r_N(N_G(Y))\bigr).                \tag{1.3}
\]

In particular the conclusion applies when every shared-resource condition
is a capacity row on a laminar family of ticket sets.  It also applies to
the genuinely private case by taking `N` free.

For a required short count `r`, there is a set of size `r` independent in
both `M_short` and `R(G,N)` if and only if

\[
 r_{M_{\rm short}}(X)+r_R(E-X)\ge r
 \qquad(X\subseteq E).                              \tag{1.4}
\]

When both matroids have rank at least `r`, this is equivalently the
common-base criterion for their rank-`r` truncations.  In the application
`r=r_{M_short}(E)=1748`, so only the Rado matroid needs explicit
truncation.  It is not, without an equal-rank hypothesis, a common-base
statement for the untruncated Rado matroid.

#### Proof

This is Rado's matroidal matching theorem and its rank formula.  A laminar
capacity system is a laminar matroid, so it is a valid choice of `N`.
Equation (1.4) is Edmonds' matroid-intersection min--max theorem at target
cardinality `r`; truncation gives the equivalent common-base formulation.
\(\square\)

A useful concrete sufficient condition is that the predecessor and
successor conflict partitions are nested: if every block of one partition
is contained in a block of the other, the stronger capacity-one partition
implies the weaker one.  Crossing predecessor/successor blocks are the
first place where this argument stops.

## 2. The smallest two-port obstruction

Let there be two predecessor ports `p1,p2`, two successor ports `q1,q2`,
and four shorts with unique tickets

\[
 e_{ij}\longmapsto(p_i,q_j),\qquad i,j\in\{1,2\}.    \tag{2.1}
\]

A set is feasible when no predecessor and no successor port repeats.  The
two rank-two feasible sets

\[
 B_0=\{e_{11},e_{22}\},\qquad
 B_1=\{e_{12},e_{21}\}                              \tag{2.2}
\]

violate basis exchange.  Replacing either member of `B0` by either member
of `B1` repeats one of its two ports.  Equivalently, the ticket-side
independence system is the intersection of two crossing partition
matroids, and that intersection is not itself a matroid.

This four-element example is minimal for a basis-exchange failure between
two rank-two bases.  At the independence-augmentation level, three ground
elements already suffice: one edge can meet each member of a disjoint
two-edge matching.

The conclusion is directed.  The first coordinate in (2.1) is the unique
outgoing use of a predecessor long role and the second is the unique
incoming use of a successor long role.  It is therefore the exact abstract
shape of a common-state `long -> short -> long` socket, not an undirected
degree surrogate.

## 3. Literal K17 augmentation counterexample

Use the authenticated round-47 relaxed-nine socket catalogue

```text
round-47 table SHA-256
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
```

and its derived file

```text
scratch/k_rots_k17_joint_1s_20260802/frozen_relaxed9/
  short_reset_triples.tsv
```

with SHA-256

```text
381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97.
```

The catalogue contains `2188` exact five-cell socket records on `1426`
short roles.  The following three shorts have exactly one record each:

\[
\begin{array}{c|ccccc}
\text{short}&\text{predecessor}&\alpha&q&\text{successor}&\beta\\ \hline
4183&11218&3&8&3987&2\\
4218& 3756&3&8&3987&3\\
4250& 3988&0&7&11218&0.
\end{array}                                             \tag{3.1}
\]

Here `alpha` and `beta` are the predecessor and successor long flags and
`q` is the short address.

For this section call a short subset **partially socket-packable** when one
catalogue record can be chosen for every selected short so that predecessor
long roles are distinct, successor long roles are distinct, and any long
role used once on each side has the same flag in both records.  This is
exactly the local degree/state part of the common-socket master.  It is a
hereditary system; no completion of unused long roles is included in the
definition.

### Theorem 3.1 (literal shared-history augmentation failure)

Let `I={4183}` and `J={4218,4250}`.  Both `I` and `J` admit a simultaneous
partial common-state socket packing, but for every `e in J`, `I+e` does
not.  Hence the hereditary partial socket-packing system of this literal
catalogue is not a matroid.

#### Proof

The singleton `I` is feasible.  The two records for `4218` and `4250` use
the four distinct long roles

\[
                  3756,3987,3988,11218,
\]

so `J` is feasible.

The shorts `4183` and `4218` both use long `3987` as successor.  Selecting
both violates successor indegree one.  The shorts `4183` and `4250` use
long `11218` on opposite sides.  That is allowed only if one common long
state is selected, but their required flags are respectively `3` and `0`.
Thus this pair is also infeasible.  Since all three socket menus are
singletons, no alternative record repairs either conflict.  This is exactly
the failure of the matroid augmentation axiom.  \(\square\)

This is an exact statement about the partial socket layer in the optimistic
relaxed-nine model.  It is **not** a canonical `4/3/2` address certificate,
and it does not assert that either partial packing extends to a complete
cycle cover.  Conversely, adding the remaining direct-arc and topology rows
cannot justify treating the raw socket layer as a matroid; a separate global
matroid theorem would still be needed.

## 4. Why the Boolean actuator is not yet `M_sock`

In the augmented bottom matching, the short bank `S` is precisely the set
of hard slots matched to dummy bottom tokens.  The frozen hub `C6`, hub
`C8`, and saturated `B5` `C10` bottom-relay actuators have two phases with

* the same real-bottom palette;
* the same physical fixed-suffix slot palette; and
* no dummy token on their alternating circuit.

### Proposition 4.1 (short-basis invariance)

Every composition of the currently proved `C6/C8/C10` bottom-relay
actuators fixes `S` pointwise.  It acts inside the fibre over one basis of
`M_short`; it does not exchange bases of `M_short` and by itself cannot
present `M_sock` on candidate short slots.

#### Proof

The short slots are exactly the right vertices incident with selected dummy
edges.  A matching circuit containing only real-bottom edges changes no
dummy edge, hence changes no short slot.  The claim is preserved under
composition.  \(\square\)

The `C8` fibre aperture does not contradict Proposition 4.1.  It is the
one interval missing from a saturated five-diamond resource fibre.  Both
`C8` phases still have the same four lower, upper, tail and head palettes,
so this omitted interval is not automatically a movable dummy-matched hard
slot or a literal common-state socket.

The correct conditional use is narrower.  Contract a complete actuator
module to one ticket object only after proving that:

1. the whole module has one designated exported short aperture;
2. every other owner, bottom, suffix, history and protected resource is
   internal to the module;
3. distinct module copies have disjoint internal footprints; and
4. each compatible `(short,module)` choice has a literal replayed state.

Then Theorem 1.1 applies to the contracted modules.  Circuit minimality
forbids treating the three, four or five individual diamonds of a primitive
`C6`, `C8` or `C10` as independent tickets: a proper nonempty subset is not
resource neutral.  The entire circuit is one compound ticket.

The existing Boolean trade notes prove the internal four-resource identity
but explicitly leave common state/history planting open.  Therefore they
supply candidate compound ticket **footprints**, not a proved
`M_sock` representation.

## 5. Exact remaining construction row

There are two proof-safe ways forward.

* **Private/Rado route.**  Build completed actuator modules with one exported
  socket each and prove that their remaining shared-resource constraints
  are free, laminar, or otherwise matroidal.  Then use (1.2), or the
  corresponding size-`1748` common-independent-set criterion with the Rado
  matroid (equivalently, common bases after rank-`1748` truncation).
* **Shared-state route.**  Keep the predecessor and successor port rows as a
  two-matching/three-uniform hypergraph problem and use exact Hall/Benders
  separation.  Do not label this system `M_sock` without a new theorem.

A short-set-changing actuator must contain a dummy-inclusive alternating
bottom-matching circuit (or an equivalent compound relay through a free
receiver).  The current real-only `C6/C8/C10` atlas cannot supply that row.
The next local target is therefore a resource-neutral dummy-inclusive
relay ticket whose two phases move one dummy edge and whose complete
history footprint is private or laminar.

## 6. Independent audit

The finite statements above are replayed by

```text
scratch/a_shared_socket_nonmatroid_20260802/
  audit_a_shared_socket_nonmatroid_20260802.py
  audit.json
```

The auditor checks the universal two-port basis-exchange obstruction, binds
the authenticated socket catalogue, verifies that all three literal menus
in (3.1) are singletons, and checks the exact degree/flag compatibility
relations used in Theorem 3.1.
