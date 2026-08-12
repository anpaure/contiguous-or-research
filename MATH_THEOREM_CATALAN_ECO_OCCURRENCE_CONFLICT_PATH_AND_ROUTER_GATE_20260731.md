# ECO occurrence conflicts are paths; router privacy is one local ownership gate

Date: 2026-07-31  
Status: exact all-dimension occurrence-support theorem; exact conditional
private-router reduction; exact first scope obstructions; no claim that the
required local router channels exist for every ECO atom

## 0. Verdict

Work in the fixed coordinate rotation with common external labels
\((d,e)=(2n,0)\).  For a Dyck word

\[
                         D=1u0v\in {\cal D}_{n-1},
\]

write \(Z(D)\) for the coherent ECO hexagon of the coherent-supply theorem.
Its six occurrence-labelled ports are

\[
 V(D)=\{\,1upv0:p\in\mathcal P\,\},\qquad
 \mathcal P=\{100,010,001,110,011,101\}.            \tag{0.1}
\]

The complete physical-overlap graph of this fixed-rotation family is
elementary.
Two distinct atoms overlap if and only if, for Dyck words \(s,t\), their
parents are

\[
             D_L=1s100t,\qquad D_R=1s010t.           \tag{0.2}
\]

They then share exactly the old factor edge on

\[
             1s10010t0,qquad 1s10110t0.             \tag{0.3}
\]

Consequently the atom-conflict graph is a disjoint union of paths.  For
\(n\ge3\) it has exactly \(\operatorname{Cat}_{n-2}\) edges (and for
\(n=2\) it has none).  A canonical bipartition is

\[
 \eta(D)=\#\{\hbox{initial primitive components `10' of }v\}\pmod2. \tag{0.4}
\]

Thus every one-parity ECO bank has **pairwise disjoint literal six-port
supports**.  More generally, the whole ECO occurrence-privacy problem is a
one-dimensional ownership problem on path components: orient each shared
old edge to one of its two incident atoms and test only whether each atom can
realize its local channels after the at-most-two unowned old edges are
removed.

This is the exact gain from ECO leaf-insertion genealogy.  It is not yet a
router theorem.  The coherent-supply theorem specifies the physical atoms
and their component hyperedges, but it does not specify a source-to-sink
linkage in the fixed occurrence router.  The same ECO genealogy is compatible
with either dedicated local paths or a shared unit bottleneck.  Hence neither
node-private routes nor the weaker laminar-cut condition follows from
genealogy alone.

There is also a grouped-rank warning.  From \(n=5\) onward an ECO atom may
meet three distinct factor components.  Such an atom carries two component
rank units.  To enter the one-source-per-unit graphic--gammoid theorem it
must export two independently routable unit channels (or retain a grouped
two-source state).  Treating the whole three-component toggle as one source
silently loses one rank unit.

## 1. Exact support intersection

Let

\[
 \mathcal P_-=\{100,010,001\},\qquad
 \mathcal P_+=\{110,011,101\}.                     \tag{1.1}
\]

The two parts are respectively the lower and upper ports of one ECO atom.

### Lemma 1.1 (three-letter overlap equation)

Let \(w,r\) be Dyck words, with \(w\ne\epsilon\), and let
\(p,p'\in\mathcal P\) have the same weight.  If

\[
                          wp=p'r,                    \tag{1.2}
\]

then

\[
 (w,p,p',r)=(10,010,100,10)
 \quad\hbox{or}\quad
 (10,110,101,10).                                   \tag{1.3}
\]

#### Proof

If \(|w|=2\), then \(w=10\), and direct substitution gives exactly (1.3).
Assume \(|w|\ge4\).  The first three letters of \(w\) are then \(p'\).
They cannot be a lower pattern: the only lower pattern which starts in `1'
is `100', whose balance is already negative after three letters, whereas a
prefix of a Dyck word has nonnegative balance.  Hence \(p,p'\) are upper
patterns and the first-three-letter prefix \(p'\) has balance one.  The
remaining suffix of \(w\) therefore has total balance minus one.  But that
whole suffix occurs as an initial segment of \(r\), before the final
three-letter word \(p\).  At its end the running balance of \(r\) is minus
one, contradicting that \(r\) is Dyck.  Thus \(|w|=2\), and the direct
check proves the lemma. \(\square\)

### Theorem 1.2 (ECO support-overlap classification)

For distinct \(D,E\in{\cal D}_{n-1}\),

\[
 V(D)\cap V(E)\ne\varnothing
\]

if and only if \(\{D,E\}=\{1s100t,1s010t\}\) for Dyck \(s,t\).  In that
case the intersection is exactly the two vertices in (0.3), one on each
shore, and those two vertices form an old canonical-factor edge.

#### Proof

Write \(D=1u0v\), \(E=1u'0v'\).  If \(|u|=|u'|\), equality of one port word
forces \(u=u'\), the same central pattern, and \(v=v'\), contrary to
\(D\ne E\).

Assume \(|u|>|u'|\).  Equality of port words makes \(u=u'w\) for a nonempty
Dyck suffix \(w\), and gives

\[
                          wpv=p'v'.                  \tag{1.4}
\]

The two central patterns have the same weight.  Hence, after the first three
letters on the right are removed, the prefix preceding \(v\) has balance
zero.  Since the whole residual and \(v\) are Dyck, that prefix is Dyck.
Lemma 1.1 applies and yields \(w=10\), \(v'=10v\), with exactly the two
pattern pairs in (1.3).  This is (0.2)--(0.3).  The converse follows by
substitution.  Direct application of the canonical factor map to the two
shared words shows that they are matched to each other. \(\square\)

## 2. The conflict graph is a path forest

Orient every conflict

\[
                         1s100t\longrightarrow1s010t.              \tag{2.1}
\]

For \(D=1u0v\), there is at most one outgoing conflict, because it requires
that \(u\) end in the primitive component `10'.  There is at most one
incoming conflict, because it requires that \(v\) begin with `10'.  Along
(2.1), \(|v|\) increases by two.  Thus the directed conflict graph has
indegree and outdegree at most one and no directed cycle.  Its underlying
graph is a disjoint union of paths.

For \(n\ge3\), the edge is determined by an ordered pair of Dyck words \((s,t)\) whose
total semilength is \(n-3\).  Catalan convolution gives

\[
 |E(\mathcal X_n)|=
   \sum_{i=0}^{n-3}\operatorname{Cat}_i
                         \operatorname{Cat}_{n-3-i}
   =\operatorname{Cat}_{n-2}.                        \tag{2.2}
\]

If \(v=(10)^jv_0\) with \(v_0\) empty or not beginning in `10', put
\(\eta(D)=j\pmod2\).  Relation (2.1) changes \(j\) by one, so \(\eta\) is a
proper two-colouring.  We have proved:

### Corollary 2.1 (parity-private physical banks)

For either \(\epsilon\in\{0,1\}\), the literal port sets

\[
                  \{V(D):\eta(D)=\epsilon\}          \tag{2.3}
\]

are pairwise disjoint.

This is physical occurrence privacy, not colour privacy: two distinct
ports may carry the same turn colour.  It is also not automatically linkage
privacy: a route starting at a private port may later traverse a public
router vertex.

### Corollary 2.2 (exact ownership reduction)

For the full fixed-rotation ECO family, orient every edge of the path forest \(\mathcal X_n\)
to one endpoint.  Give the shared old factor edge (0.3) to that endpoint and
delete its two vertices from the other endpoint's bank.  The resulting atom
banks are pairwise disjoint.  Every atom loses vertices on at most two old
factor edges.

Hence a node-private route construction for the full family reduces exactly
to the following local avoidance statement:

> for each atom, realize its required unit occurrence channels after any
> prescribed subset of its at most two genealogy-shared old edges has been
> assigned away.

No global port-conflict packing remains after this local statement.

## 3. From a component hypertree to router resilience

For an ECO atom \(Z\), let \({\cal C}(Z)\) be the set of distinct old factor
components met by its three old matching edges, and put

\[
                         \rho(Z)=|{\cal C}(Z)|-1.     \tag{3.1}
\]

Choose a tree \(R_Z\) on \({\cal C}(Z)\); it has \(\rho(Z)\) unit component
edges.  A selected ECO family is a **unit-expanded component hypertree** if

\[
                         R=\bigcup_ZR_Z               \tag{3.2}
\]

is a tree on all factor components.

### Theorem 3.1 (conditional ECO private-router theorem)

Let \({\cal S}\) be a unit-expanded component hypertree.  Suppose every
unit edge of every \(R_Z\) has a named source-to-sink occurrence path, the
\(\rho(Z)\) paths inside one atom are vertex-disjoint, and paths belonging
to different atoms lie in the pairwise disjoint banks of Corollary 2.1 or
2.2.  Suppose also that these paths avoid all internal child router banks.
Then

\[
                         c(R_Y)\le |Y|+1             \tag{3.3}
\]

for every occurrence-router deletion set \(Y\).  Consequently the router
row of the ordered fixed-decoration theorem is satisfied.

#### Proof

All \(|V(R)|-1\) paths are pairwise vertex-disjoint.  A deletion set \(Y\)
therefore kills at most \(|Y|\) unit edges of the tree \(R\).  Deleting at
most \(|Y|\) edges from a tree leaves at most \(|Y|+1\) components.  Extra
surviving catalogue edges can only lower the component count. \(\square\)

The theorem keeps owner alignment separate.  It does not assert that the
forced gap/colour triples lie in one alternating SDR.

## 4. What genealogy does not prove

### Proposition 4.1 (first data-separation obstruction)

ECO leaf genealogy and even pairwise-disjoint physical port supports do not
imply router resilience.

#### Proof

Take the first component-spanning case with three factor components.  At
\(n=4\) they have canonical representatives

\[
             10101010,qquad10101100,qquad10111000.  \tag{4.1}
\]

The parity-zero atoms \(Z(110100)\) and \(Z(111000)\) have disjoint
six-port supports and join respectively the first--second and
second--third components.  They are therefore a literal ECO component tree.

Keep these same atoms, ports, component edges and owner data in two prepared
routers.  In the first router, give the two sources dedicated internally
disjoint paths to two sinks.  In the second, force both sources through one
unit router vertex \(z\), then to distinct sinks.  The ECO genealogy is
identical in the two preparations.  In the second preparation, deleting
\(z\) kills both tree edges and leaves three components:

\[
                         3>|\{z\}|+1=2.              \tag{4.2}
\]

Thus no conclusion about node-private paths or the laminar-cut inequality
can be derived from genealogy without a realization theorem connecting the
actual occurrence network to the atom banks.  For \(n\le3\) there are at
most two plane-tree components, so a connected unit tree has at most one
edge and this two-source separation is impossible. \(\square\)

### Proposition 4.2 (first grouped-rank obstruction)

At \(n=5\), the atom with parent

\[
                              D=11100010              \tag{4.3}
\]

meets the three distinct plane-tree components represented by

\[
                 1011001100,\qquad1010111000,
                 \qquad1011110000.                  \tag{4.4}
\]

Hence \(\rho(Z(D))=2\).  Any unit expansion of its component effect is a
two-edge tree.  In the one-source-per-unit graphic--gammoid model those two
ground elements require two distinct source elements of joint gammoid rank
two; equivalently, they require two vertex-disjoint paths to two distinct
sinks.  Copying one source twice has gammoid rank one and cannot support the
two component-rank units.  Likewise, if the two nominal routes both use one
unit router vertex, deleting that vertex kills both unit joins, creates
three pieces, and violates (3.3).  The exact options are therefore:

1. export two independently routable unit channels;
2. retain the grouped two-source linkage state; or
3. use only a one-rank component effect of the atom and certify that
   correlated partial operation physically.

This is a rank/interface obstruction, not evidence that the ECO atom itself
is unusable.

## 5. Exact remaining local lemma

The coherent ECO supply theorem and the present note reduce its occurrence
router row to one precise statement:

> **ECO local-channel lemma.**  Choose a component-spanning ECO hypertree
> and orient its path-forest support conflicts.  For every selected atom
> \(Z\), realize \(\rho(Z)\) vertex-disjoint occurrence channels inside its
> owned bank, after the at-most-two unowned old edges are removed, ending at
> distinct local sinks and avoiding all child router banks.

If this lemma holds, Theorem 3.1 proves global router resilience.  If it
fails, the first failing atom together with its two ownership bits is a
finite exact obstruction.  Static coherent connectivity, port disjointness,
and gap/colour owner alignment do not decide this lemma.

Coordinate-rotated copies of the ECO family may be added only after their
cross-rotation occurrence conflicts are recomputed.  The path-forest theorem
does not assert privacy between different rotations.

## 6. Audit

The lightweight audit enumerates all Dyck parents through \(n=9\), verifies
the complete intersection classification, the path-forest degrees, the
edge count \(\operatorname{Cat}_{n-2}\), parity disjointness, the first
shared edge at \(n=3\), and the first three-component atom at \(n=5\):

```text
python3 scratch/audit_catalan_eco_occurrence_conflict_router_20260731.py
```

The audit is combinatorial only.  It does not claim to enumerate or solve
the prepared occurrence router.
