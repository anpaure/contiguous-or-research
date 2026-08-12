# Tree-contiguous private socket schedules

Date: 2026-07-31  
Status: exact necessary-and-sufficient theorem inside the recursively
contiguous/private-resource socket class; exact primitive-voltage actuator
criterion; no existence theorem for that class in every dimension

## 0. Verdict

The factorial socket state in
`MATH_THEOREM_AD_CATALAN_LEAF_RUN_SOCKET_BOUNDARY_STATE_AND_ROUTING_OBSTRUCTION_20260731.md`
has one exact bounded-interface escape.

Let the finalized physical path components be organized by a rooted binary
refinement of the transparent gluing tree.  Assume that their desired socket
Hamilton cycle is **tree-contiguous**: the components below every proper node
form one cyclic interval.  Cut one declared root connector.  Then every node
contains one directed socket chain, so its complete physical routing state is
one endpoint triple and one gain,

\[
             \bigl((t_x,U_x),h_x,g_x\bigr).                 \tag{0.1}
\]

If, in addition, every internal connector uses a literal edge resource and a
lower colour owned privately by its gluing node, the unbounded used-colour set
can be deleted from the state.  Bottom-up multiplication of (0.1), followed
by one root connector of primitive total voltage, is then necessary and
sufficient **within this class**.

This is compatible with the private-colour attachment path

\[
 [c_1]-g_1-[c_2]-g_2-[c_3]                         \tag{0.2}
\]

from the leaf-peelable transparent-gluing theorem.  The two private systems
remain logically independent: (0.2) controls the gap--colour forest, while
(0.1) controls the physical endpoint cycle.  A proof may carry both at one
node using boundedly many literal labels.  Neither one implies the other.

The result below is the strongest exact locality reduction currently
justified.  Without tree contiguity one subtree can expose arbitrarily many
socket chains.  Without private resource ownership the used lower-colour set
must be retained.  Without the gain residue, primitive voltage can change
under an indistinguishable exterior closure.

## 1. Supplied path records and the recursive interval condition

Let \({\cal C}\) be a supplied physical path forest in a free clean quotient
by \(H\cong\mathbb Z_q\), where \(q=|H|\).  Give each oriented path component \(C\) its
terminal-host record

\[
                   ((t_C,U_C),h_C,g_C),               \tag{1.1}
\]

where \(t_C\) is the entry endpoint of its terminal host, \(U_C\) its host
upper label, \(h_C\) the opposite path endpoint, and \(g_C\) the oriented
gain of the retained path.  Isolated hosts retain both orientation choices.

A legal directed connector \(e:C\to C'\) satisfies

\[
                    h_C\cup t_{C'}=U_{C'},            \tag{1.2}
\]

has lower label \(\ell(e)=h_C\cap t_{C'}\), literal edge resource
\(r(e)\), and oriented gain \(\gamma(e)\in\mathbb Z_q\).

Let \(T\) be a rooted binary tree whose leaves are the finalized path
components.  It may refine the transparent gluing tree by inserting binary
comb nodes among components finalized at one polygon.  For a node \(x\), let
\({\cal C}_x\) be its descendant leaves.

### Definition 1.1 (recursive contiguity)

A directed socket Hamilton cycle \(Z\) is \(T\)-contiguous if
\({\cal C}_x\) is a cyclic interval of \(Z\) for every proper node \(x\).
Equivalently, after cutting any connector not internal to a proper root
child, the restriction to every \({\cal C}_x\) is one directed chain.

For a binary node, the two child intervals occur in one of the two orders.
Exactly one connector joins them inside the parent chain.  At the root, the
cut connector is restored after the two child intervals have been merged.

### Definition 1.2 (node-private resources)

For every internal node \(x\), fix catalogues \({\cal E}_x\) of literal
connector records and \({\cal L}_x\) of allowed lower labels.  Fix a separate
root-closing catalogue \({\cal E}_\circ\) and lower-label bank
\({\cal L}_\circ\).  The ownership is private when

\[
 \begin{split}
 r({\cal E}_x)&\cap r({\cal E}_y)=\varnothing,\\
 {\cal L}_x&\cap{\cal L}_y=\varnothing
 \end{split}                                         \tag{1.3}
\]

for distinct owners \(x,y\), including the closing owner \(\circ\), and
every selected connector at \(x\) lies in \({\cal E}_x\) and has lower label
in \({\cal L}_x\).  All catalogues have already excluded retained forest
edges and any private collar resource used elsewhere.

For a binary tree only one internal connector is selected per internal node,
so (1.3) automatically gives literal-edge and connector-lower-colour
injectivity.  This ownership is a sufficient syntactic mechanism.  It is not
claimed necessary when global label sets are carried explicitly.

## 2. The exact bounded endpoint product

A directed chain \(C_1,\ldots,C_s\) has compressed record

\[
 \sigma(C_1,\ldots,C_s)
   =\bigl((t_{C_1},U_{C_1}),h_{C_s},g\bigr),           \tag{2.1}
\]

where \(g\) is the total oriented gain of all retained paths and internal
connectors in the chain.

For child records

\[
 s=((t,U),h,g),\qquad s'=((t',U'),h',g'),             \tag{2.2}
\]

and a connector \(e\in{\cal E}_x\), define

\[
 s\star_e s'=((t,U),h',g+\gamma(e)+g')               \tag{2.3}
\]

exactly when \(e\) joins the literal endpoint \(h\) to \(t'\) and satisfies
\(h\cup t'=U'\).  Both child orders and every child orientation represented
in its state are tested.

### Theorem 2.1 (tree-contiguous private-socket theorem)

Under Definitions 1.1--1.2, the following are equivalent.

1. The supplied path components admit a \(T\)-contiguous directed socket
   Hamilton cycle using one connector owned by every internal node and one
   connector from \({\cal E}_\circ\), with all literal connector resources
   and lower labels distinct, and with primitive total voltage.
2. Bottom-up propagation of the records (2.1) by (2.3) produces a root-chain
   record \(((t,U),h,g)\) and a closing connector
   \(e_\circ:h\to t\) such that
   \[
                   h\cup t=U,qquad
                   \gcd(q,g+\gamma(e_\circ))=1.       \tag{2.4}
   \]

For \(q=1\), the second test in (2.4) is vacuous.  Thus one literal endpoint
triple and one residue per feasible chain are information-complete in this
class; no component permutation, chain-cover partition, or used-colour set
is needed.

#### Proof

Assume 1 and cut the declared root connector.  Recursive contiguity makes
the leaves below every proper node one directed chain.  At a binary internal
node its child blocks are consecutive in one of the two orders, and there is
exactly one cycle connector between them inside the parent chain.  Restricting
the cycle therefore gives the product (2.3) at every node.  The removed edge
is \(e_\circ\).  The occurrence cycle is already one cycle, and the supplied-
forest voltage theorem says that its physical development is Hamiltonian
exactly under (2.4).  Private ownership gives all literal capacities and
lower-colour injectivity without an additional ledger.

Conversely, expand the bottom-up products.  At every node (2.3) concatenates
two vertex-disjoint child chains by one legal connector.  Induction gives one
chain on exactly the descendant leaves, so every node is contiguous.  The
root connector closes the root chain into one quotient occurrence cycle.
Private ownership prevents every literal-resource or lower-label collision,
and (2.4), together with the supplied-forest voltage theorem, makes its lift
one physical Hamilton cycle. \(\square\)

### Corollary 2.2 (one-socket leaf insertion)

It is sufficient to construct the schedule incrementally.  Suppose a rooted
leaf-peelable order adds one child subtree at a time.  At an insertion, a
current chain record \(((t,U),h,g)\), a new child-chain record
\(((t',U'),h',g')\), and one node-private connector \(h\to t'\) produce the
new chain by (2.3).  If each insertion succeeds and the final chain has a
legal primitive closing connector, all socket conditions follow.

Equivalently, when a maintained cycle rather than a chain is used, reserve
one connector as the open socket, delete it, splice the new child chain
through the opening by two private connectors, and designate one of them as
the new open socket.  This is the same chain product with a different cut.

This corollary is a sufficient construction protocol, not a normalization of
an arbitrary socket Hamilton cycle.

## 3. Primitive voltage is a root-local actuator

For a fixed root-chain state \(((t,U),h,g)\), let

\[
 A(t,h)=\{\gamma(e):e\in{\cal E}_\circ, e:h\to t
                    \text{ is legal}\}.              \tag{3.1}
\]

### Lemma 3.1 (exact root voltage condition)

The voltage gate accepts this endpoint state exactly when

\[
              (g+A(t,h))\cap\mathbb Z_q^\times\ne\varnothing. \tag{3.2}
\]

Consequently a root catalogue makes voltage automatic for every possible
interior gain precisely when its gain set is **universally unit-hitting**:

\[
        \forall g\in\mathbb Z_q,\qquad
        (g+A(t,h))\cap\mathbb Z_q^\times\ne\varnothing.        \tag{3.3}
\]

A complete gain fibre \(A(t,h)=\mathbb Z_q\) is sufficient.  If \(q\) is
prime, any two distinct available gains are sufficient.  For composite
\(q\), two distinct gains need not suffice; at \(q=6\), the set
\(A=\{0,1\}\) fails for \(g=2\), since both totals 2 and 3 are nonunits.

#### Proof

All retained paths and the internal socket connectors form one spanning
chain.  Gauge every edge of that chain to gain zero.  The unique remaining
cycle edge then has gain equal to the invariant total
\(g+\gamma(e)\).  The supplied-forest voltage theorem gives (3.2).
Quantifying over \(g\) gives (3.3).  For prime \(q\), the only nonunit is
zero, so two distinct translates cannot both be zero.  The composite
counterexample is immediate. \(\square\)

Thus primitive voltage does not require a global permutation state in the
tree-contiguous class.  One residue, or a root actuator satisfying (3.3), is
exact.

## 4. Compatibility with the private-colour attachment path

The leaf-peelable transparent-gluing theorem has the sufficient local gap
face

\[
 [c_1]-g_1-[c_2]-g_2-[c_3],                         \tag{4.1}
\]

where the first two colour blocks are private to the current transparent
glue, the path meets the retained nonprivate gap core in at most the terminal
block \([c_3]\), and different glue paths have disjoint private blocks.

### Theorem 4.1 (orthogonal private-collar product)

Suppose a transparent gluing tree is supplied with a binary refinement such
that, at every internal node:

1. the selected turn occurrences pass palette and boundary transparency;
2. the changed gap sockets have the private path form (4.1), with the
   required leaf-peeling ownership;
3. the finalized physical components admit one chain product (2.3) using a
   node-private literal connector and lower-label bank; and
4. the gap-private and physical-socket-private resource declarations are
   disjoint, unless a literal shared use has been explicitly capacity-checked.

If the strict trace/run state and protected component guards also compose,
then the node needs only the three gap-owner labels in (4.1), the two child
endpoint records and the output record (2.1), plus its finite run/decoration
state.  At the root, (2.4) is the only remaining socket/voltage test.

#### Proof

The gap attachment is a leaf path and meets the old core once, so successive
deletion of \(c_1,c_2\) leaves a forest attached at \(c_3\).  Induction gives
the balanced leaf-peelable gap graph.  Independently, Theorem 2.1 composes the
physical paths into one socket chain.  The resource declarations make the
two inductions capacity-compatible, while palette/boundary transparency and
the run state preserve their respective gates.  The root connector and
primitive voltage close the physical chain. \(\square\)

The word “orthogonal” is substantive.  In the frozen \(m=4\) standard glue,
the private gap-owner triple is \(\{18,20,24\}\), while one explicit physical
Hamilton closure uses connector lower colours

\[
 \{137,22,56,131,194,14,82,164,208,84,73,97,168,49\}.
\]

The sets are disjoint.  The fixture proves compatibility, not identification,
of the two resources.  More generally, transparency preserves gap-owner
palettes but not the physical path involution: item 2170 gives a literal
toggle which changes one 70-cycle into cycles of orders 46 and 24 while
preserving the socket multiplicity profile.  Therefore (4.1) alone cannot be
used as the physical socket theorem.

There is also no longer a standard-family induction to which this theorem
can simply be appended.  Item 2172 exhausts the unmodified standard \(m=5\)
plane-tree glues: both Hamilton outputs miss three turn colours on each
shore, despite one output retaining two disjoint local all-six private
triples.  Thus local private gap paths and local private socket schedules
must be sought only after a nonstandard palette repair, a changed base
factor, or a joint representative/glue choice.  The present theorem removes
the factorial *routing-state* obstruction once such a local schedule is
supplied; it does not repair the \(m=5\) palette obstruction.

## 5. Sharpness of the locality hypotheses

The three reductions in Theorem 2.1 have different scopes.

1. **Tree contiguity is necessary for a one-chain state.**  Restricting an
   arbitrary final Hamilton cycle to one subtree may produce arbitrarily many
   directed chains.  Their entrance/exit pairing is the socket permutation
   state of the factorial routing obstruction.  One endpoint triple cannot
   encode it.
2. **Private resources are sufficient for deleting the used-label set.**
   Without them, two child realizations may have the same endpoint triple and
   gain but differ on whether a lower colour \(c\) was used internally.  An
   exterior connector of colour \(c\) accepts one and rejects the other.
   Hence any exact triples-only state must obtain this distinction from a
   syntactic ownership rule or retain equivalent used-resource information.
3. **The gain residue is necessary unless a root actuator is supplied.**
   Two chains with the same literal endpoints and different total gains can
   be separated by a fixed closing connector whenever one total is primitive
   and the other is not.  Lemma 3.1 is the exact replacement.

Theorem 2.1 is therefore necessary and sufficient inside the recursively
contiguous class, while Definitions 1.2 and (3.3) are explicit sufficient
mechanisms for compressing its resource and voltage coordinates.  It does
not prove:

* that every transparent Catalan gluing tree admits a recursively contiguous
  socket cycle;
* that its physical connector catalogue contains node-private choices;
* that the standard all-six-marked private gap triple supplies physical
  socket edges; or
* that an accepting tree exists for every \(m\).

Those statements are the exact remaining construction problem on the
physical side.

## 6. Audit scope

`scratch/audit_catalan_tree_contiguous_private_socket_20260731.py` checks the
pure combinatorial claims used above: cutting a cycle gives the recursive
one-chain products on every interval binary tree through seven leaves, the
connector count is \(n-1\) internal plus one closing edge, the prime two-gain
actuator and the composite \(h=6\) counterexample, and the disjointness of the
two frozen \(m=4\) private resource lists.  The audit is not an all-dimension
existence search and does not reconstruct the middle-levels fixture.
