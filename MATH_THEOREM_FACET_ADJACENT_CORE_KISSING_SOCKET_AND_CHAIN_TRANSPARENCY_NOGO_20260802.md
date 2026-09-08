# Adjacent-core kissing sockets and the exact chain-transparency obstruction

Date: 2026-08-02  
Status: exact pure-splice classification for the unbuffered alternating
packet.  Johnson adjacency gives one all-width rank-correct open socket,
but no pure splice between distinct cores preserves the protected chain
multiset.  In the fixed-phase reservoir, pure rank-correct splicing also
cannot merge two packet cycles into a cycle.

## 0. Outcome

Fix one support

\[
 A=\{\beta\}\mathbin{\dot\cup}V,
 \qquad V=(z_0,\ldots,z_{L-1}),
\]

and let the alternating packet over a core

\[
 X\in\binom{[k]-A}{c-1}
\]

have source cells

\[
 S_t(X)=
 \begin{cases}
 X\cup\{z_t\},&t\text{ even},\\
 X\cup\{\beta,z_t\},&t\text{ odd}.
 \end{cases}                                             \tag{0.1}
\]

This is the corrected packet of
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`,
where

\[
 q=d+2,\qquad
 L=\begin{cases}q+2,&q\text{ even},\\q+1,&q\text{ odd},\end{cases}
 \qquad L>q.
\]

Assume \(c\ge2\), since for \(c=1\) the core layer has one empty vertex
and there is no connector question.  Let \(X,Y\) be Johnson-adjacent
cores.  Write

\[
 X=K\cup\{a\},\qquad Y=K\cup\{b\},
 \qquad |K|=c-2.                                       \tag{0.2}
\]

There are three different assertions, and only the first is positive.

1. There is an exact all-width **rank-correct** open join.  Cut the two
   packets so that an odd cell carrying the same tag \(z_p\) is the end of
   the first path and the start of the second, and orient the two paths in
   the same cyclic direction.  The seam is an \(H\)-\(H\) kissing socket.
2. This socket is never chain-transparent.  Every mixed window has
   outside-\(A\) trace \(X\cup Y\), whereas every old packet resource has
   trace \(X\) or \(Y\).  Thus none of the new crossing labels transports an
   old protected label.
3. In the fixed support/order/phase reservoir, every all-width rank-correct
   mixed seam is such an \(H\)-\(H\) kissing socket.  Cutting two cycles once
   leaves one \(H\) and one \(P\) endpoint on each path, so at most one of
   the two seams needed for a cyclic fusion can be rank-correct.

Consequently, connectivity of the surviving cores in
\(J(k-|A|,c-1)\) does **not** by itself bridge clustered named-resource
packing to physical transparent fusion.  It gives a supply of prospective
rank-correct open sockets, but exact fusion still needs an ambient duplicate
bank, a source-changing collar, or a multi-core cancellation packet.

## 1. The trace obstruction

Call a splice **pure** when it cuts and reconnects source paths without
changing any source cell.  A new interval is **mixed** when it contains at
least one cell with core \(X\) and at least one cell with core \(Y\).

### Theorem 1.1 (outside-trace obstruction)

For any distinct \(X,Y\subseteq[k]-A\), every mixed union window \(C\)
in a pure splice satisfies

\[
                         C\cap([k]-A)=X\cup Y.          \tag{1.1}
\]

Every union window in the two original packet cycles has outside trace
\(X\) or \(Y\).  Hence no nontrivial pure splice between the two cycles can
preserve the multiset of all affected protected union chains.

#### Proof

Every source cell from the \(X\)-packet contains all of \(X\) and no point
of \(([k]-A)-X\); similarly for \(Y\).  A mixed union therefore has outside
trace exactly \(X\cup Y\), proving (1.1).  An unmixed old window lies wholly
in one packet, so its outside trace is exactly its packet core.  Since
\(X\ne Y\), the three sets \(X,Y,X\cup Y\) are distinct.  Thus every new
mixed window has a label absent from both old packet decks.  Every
nontrivial cross-splice creates a mixed window and deletes an old crossing
window, so equality of the affected chain multisets is impossible.
\(\square\)

The result is stronger than a q1 obstruction: it applies simultaneously to
every union width.  It is also independent of core distance.  Johnson
adjacency repairs the *rank* of a mixed window after one tag repetition; it
cannot repair its literal trace.

### Corollary 1.2 (protected-chain scope)

The sufficient equality criterion in Section 6 of the unbuffered theorem
has no pure adjacent-core connector edge.  A proposed connector can still
be useful under a weaker policy in which the deleted labels have ambient
duplicate providers and the new \(X\cup Y\)-trace labels are admitted
prospectively.  Such a policy is not chain transparency and requires a
separate provider ledger.

## 2. Exact rank equation at one seam

Consider a mixed window containing \(\ell\ge2\) source occurrences.  Let

* \(o\) be the number of tag coordinates appearing on both sides of the
  seam; and
* \(\epsilon=1\) if at least one of the cells is an \(H\)-cell and
  \(\epsilon=0\) otherwise.

Because \(\ell\le q<L\), neither one-sided tag arm repeats a coordinate.
For adjacent cores (0.2), the mixed union has rank

\[
 |X\cup Y|+(\ell-o)+\epsilon
                  =c+\ell-o+\epsilon.                  \tag{2.1}
\]

An ordinary \(\ell\)-window in one packet has rank

\[
             (c-1)+\ell+1=c+\ell.                      \tag{2.2}
\]

Thus the exact rank condition is

\[
                              o=\epsilon.               \tag{2.3}
\]

This is the precise content of the adjacent-core rank observation.

### Theorem 2.1 (fixed-phase port classification)

Assume \(q\ge4\), and use the same cyclic tag order and the same \(P/H\)
phase assignment (0.1) on both cores.  A mixed seam has the correct rank
for every crossing width \(2\le\ell\le q\) if and only if:

1. its two boundary cells carry the same odd tag \(z_p\), hence are both
   \(H\)-cells; and
2. the two oriented paths leave \(z_p\) in opposite tag directions, or
   equivalently the paths have the same cyclic orientation on their two
   sides of the seam.

#### Proof

At width two, (2.3) says either:

* the endpoints are \(P,P\) with distinct tags; or
* beta is present and the endpoint tags agree.

Under the fixed phase assignment, equal tags have equal type and unequal
types cannot have equal tags.  Thus the second case is exactly \(H,H\) at
one odd tag.

The \(P,P\) case already fails at width three.  If the left endpoint is
\(z_p\), extending the left arm by one cell introduces the adjacent odd tag.
For the resulting \(2+1\) window to satisfy (2.3), the right \(P\)-tag would
have to equal that odd tag, contradicting its parity.

It remains to treat \(H,H\) at \(z_p\).  At widths two and three the only
common tag is necessarily \(z_p\).  For the \(2+2\) window, condition
(2.3) says that the next tag on the right must differ from the preceding
tag on the left.  This is exactly the asserted opposite-arm condition.
Once the two arms move away from \(z_p\), their intersection is precisely
\(\{z_p\}\) for every total width at most \(q<L\).  Hence \(o=1\); beta is
present, so \(\epsilon=1\), and (2.3) holds through width \(q\).
\(\square\)

### Corollary 2.2 (literal kissing-path formula)

Choose odd \(p\).  Open the \(X\)-cycle immediately after \(z_p\) and the
\(Y\)-cycle immediately before \(z_p\), and concatenate the resulting paths
at their two \(H(z_p)\) endpoints.  A crossing window using \(u\ge1\) cells
from the left and \(v\ge1\) cells from the right, with
\(u+v=\ell\le q\), is

\[
 K\cup\{a,b,\beta\}\cup
 \{z_{p-u+1},z_{p-u+2},\ldots,z_{p+v-1}\}.             \tag{2.4}
\]

It has \(\ell-1\) tags and rank \(c+\ell\).  For fixed \(\ell\), the
\(\ell-1\) crossing labels are distinct.  All have outside trace
\(X\cup Y\), so (2.4) is a prospective rank-correct socket, not a
transparent return of an old label.

## 3. The fixed-phase topology obstruction

### Theorem 3.1 (no pure two-cycle fusion)

Cut one source edge in each of two fixed-phase packet cycles.  No
reconnection of the four path endpoints into one cycle has correct ranks at
every crossing width \(2\le\ell\le q\).

#### Proof

Every source edge of an alternating packet joins one \(P\)-cell to one
\(H\)-cell.  Hence each opened path has one \(P\) endpoint and one \(H\)
endpoint.  Among the four endpoints there are exactly two of each type.
By Theorem 2.1, a rank-correct mixed seam must join the two \(H\) endpoints
at a common odd tag.  This can account for at most one of the two new seams
of a cyclic reconnection.  The remaining seam contains a \(P\) endpoint and
therefore fails by width three (in fact a mixed \(P/H\) seam fails already
at width two).  Reversing either opened path does not change its endpoint
types, so it does not remove the obstruction. \(\square\)

### Corollary 3.2 (one merge is the pure linear limit)

The kissing construction can join two packet cycles into one path, leaving
the two \(P\) endpoints as the external ends.  This same one-cut operation
cannot then attach a third intact packet by another all-width kissing seam:
both ends of the first joined path are \(P\)-ports.  Thus serial iteration
requires an additional cut/rethread or a different phase state.

This corollary concerns the successive one-cut construction on unchanged
source cells in one fixed phase.  It is not a no-go for arbitrary multi-cut
packets.  A second phase species, a relabelled collar, or a source-changing
commutator may alter the endpoint current; none is supplied by the
clustered-pruning theorem.

## 4. Owner-graph comparison

The rank-\(r\) owners in the \(X\)-packet are

\[
 O_t(X)=X\cup\{\beta\}\cup J_t,                         \tag{4.1}
\]

where \(J_t\subset V\) is a cyclic \((q-1)\)-interval.  Since these
intervals are proper and have distinct starts, for adjacent cores \(X,Y\)

\[
 O_i(X)\sim_J O_j(Y)\quad\Longleftrightarrow\quad i=j. \tag{4.2}
\]

Indeed, the core exchange already contributes the two elements of the
Johnson symmetric difference, so the tag intervals must agree.

The aligned cross edge has lower and upper q1 labels

\[
\begin{aligned}
 O_t(X)\cap O_t(Y)&=K\cup\{\beta\}\cup J_t,\\
 O_t(X)\cup O_t(Y)&=K\cup\{a,b,\beta\}\cup J_t.         \tag{4.3}
\end{aligned}
\]

Their outside traces are respectively \(K\) and \(X\cup Y\), whereas all
old internal q1 labels have trace \(X\) or \(Y\).  Thus an owner-level
Johnson rectangle gives a legitimate topological switch, but it replaces
two lower and two upper labels by four fresh labels.  It is not a palette-
transparent switch and, without a separate erosion lift, is not a source-
chain connector.

## 5. Consequence for cylinder-avoidance connectivity

Deleting cross-bad trace cylinders may leave a giant connected subgraph of
the core Johnson graph.  Such a theorem would be useful, but the graph edge
has only the following unconditional physical meanings here:

* an aligned owner-level Johnson edge with the palette change (4.3); or
* an \(H\)-kissing open source socket with the fresh chain labels (2.4).

Neither is transparent to the packet's protected named deck.  Therefore a
Johnson giant-component theorem alone cannot prove component fusion.  A
complete positive fusion theorem must add at least one of:

1. ambient duplicate providers for every deleted chain label;
2. a prospective selection that leaves the relevant port chains unmarked
   and accounts for their deficits;
3. a source-changing multi-core circuit whose \(K\), \(X\), \(Y\), and
   \(X\cup Y\) trace changes cancel; or
4. a second phase/collar state which changes the endpoint-current
   obstruction of Theorem 3.1.

This is the exact obstruction left between cylinder-avoidance connectivity
and physical fusion.

## 6. Scope

The note does not rule out non-pure rethreading, ambient absorption, or
multi-packet alternating circuits.  It does not address the probability
that a cylinder-pruned Johnson reservoir remains connected.  It proves
that even a spanning tree of surviving Johnson-adjacent cores is not, by
itself, a spanning tree of protected chain-transparent physical sockets.
