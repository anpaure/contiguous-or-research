# Closed \(C_6\) router tubes for BFE

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Let

\[
 J=[2s],\qquad {\cal D}={\cal D}_s,\qquad
 B=C_s,\qquad c=C_{s-1}.
\]

Fix the forced endpoint-root set

\[
 R_\infty=\{P\in{\cal D}:b_1(P)=2s\},
 \qquad |R_\infty|=c.
\tag{0.1}
\]

The tight endpoint corridor from
`MATH_THEOREM_BFE_HEXAGON_OUTGOING_COMPLETION_20260726.md`
freezes the edges

\[
                         P\longmapsto P\cup\{2s\}
                         \qquad(P\in R_\infty).
\tag{0.2}
\]

The remaining phase-zero owners are

\[
                         V_0={\cal D}\setminus R_\infty,
 \qquad |V_0|=B-c.
\tag{0.3}
\]

This note proves five facts about packing those owners by incidence
hexagons.

1. **Orientation cannot balance the scalar quota.** A phase-zero
   \(C_6\) has the same insertion-label multiset in both orientations.
   The Catalan histogram must therefore be encoded in the choice of its
   three petal labels, before any router orientation is chosen.
2. **There is an exact packet hypergraph.** A phase-zero near-factor is a
   matching of six-resource packets—three roots and three upper states—
   with prescribed degrees on the petal labels. It has an exact mod-three
   omitted-owner ledger.
3. **Pair and triple cancellation are classified.** Two 3-cycle routers
   cancel only on the same strand triple with opposite orientation. Three
   cancel either by repeating one 3-cycle three times or by the
   four-strand tetrahedral relation displayed in Theorem 4.1.
4. **Immediate cancellation is impossible.** The three strands leaving a
   \(C_6\) cannot form another outgoing \(C_6\) in the next phase. An
   inverse router must occur at least two phases later.
5. **Return-router Hall is exact.** After prepacking a vertex-disjoint
   internal router bank, pair-tube completion is an ordinary bipartite
   matching problem. Its Hall cut is necessary and sufficient. Triple
   tubes have the analogous demand-two Hall condition.

A matched pair or triple of returning routers is a **closed router tube**.
Jointly toggling all routers in such a tube has identity total monodromy.
Inside an already layered exact ownership ledger, the resulting complete
paths again join every root to its own complement in exactly \(s\) Johnson
steps. Hence the joint tube is a literal fixed-exterior geodesic trade and
its crossing-collar ownership is automatic: it uses the same complete
\(X/Y\) vertex sets as the original factor. The individual nonidentity
router remains only an abstract open ledger.

No unconditional growing packing is proved. The exact remaining problem
is now smaller: a petal-degree packet near-factor satisfying the Catalan
quotas, together with a return-router Hall matching of order about
\((B-c)/3\), and an identity-monodromy leftover skeleton. The
ballot-forced bank guarantees only \(\Theta(B/s)\) uncoloured cycles, so
its present count alone is a factor \(s\) too weak to certify the required
return matching.

## 1. The endpoint cut removes \(2s\) from every phase-zero router

An incidence hexagon is specified by an \((s-1)\)-set \(K\) and three
distinct petals \(a,b,c\notin K\). Its lower and upper shores are

\[
\begin{aligned}
 X(K;a,b,c)&=\{K+a,K+b,K+c\},\\
 Y(K;a,b,c)&=\{K+a+b,K+b+c,K+c+a\}.
\end{aligned}
\tag{1.1}
\]

Suppose all three lower vertices are phase-zero Dyck roots outside
\(R_\infty\). Every Dyck root contains \(1\) and omits \(2s\). Since
three distinct extensions of \(K\) contain \(1\), necessarily \(1\in K\).
Since every extension omits \(2s\),

\[
                         2s\notin K\cup\{a,b,c\}.
\tag{1.2}
\]

Thus all three upper vertices omit \(2s\), and the packet lies wholly
outside the saturated \(\{1,2s\}\)-corridor. Conversely, no phase-zero
switchable packet can meet \(R_\infty\), by the tight-cut lemma. Therefore
the frozen endpoint roots and the phase-zero \(C_6\) packets are completely
separated.

## 2. A \(C_6\) orientation preserves the first-label histogram

The two alternating halves of (1.1) may be written

\[
\begin{array}{lll}
 K+a\to K+a+b,&K+b\to K+b+c,&K+c\to K+c+a,
\end{array}
\tag{2.1}
\]

and

\[
\begin{array}{lll}
 K+a\to K+c+a,&K+b\to K+a+b,&K+c\to K+b+c.
\end{array}
\tag{2.2}
\]

### Theorem 2.1 (petal-multiset invariance)

At phase zero, both orientations have first-insertion histogram

\[
                              e_a+e_b+e_c.
\tag{2.3}
\]

Consequently no choice of orientations in a fixed phase-zero hexagon
packing changes its aggregate first-edge histogram.

#### Proof

The inserted labels in (2.1) are \(b,c,a\), while those in (2.2) are
\(c,a,b\). Both are the multiset \(\{a,b,c\}\). \(\square\)

This closes the proposed ``orient the massive bank to obtain Catalan
balance'' route. Orientation is available for owner transport and
monodromy, but scalar balance must be built into the packet inventory.

The correct target remains

\[
\begin{aligned}
 q_1&=0,\qquad q_{2s}=c,\\
 q_{2j}+q_{2j+1}&=C_{j-1}C_{s-j},\qquad
 |q_{2j}-q_{2j+1}|\le1\quad(1\le j<s).
\end{aligned}
\tag{2.4}
\]

The \(c\) frozen edges (0.2) supply the entire \(2s\)-coordinate load.
The internal target vector

\[
                         d_x=q_x\qquad(2\le x<2s)
\tag{2.5}
\]

must be the petal-degree vector of the phase-zero packet family, up to the
explicit contribution of leftover roots.

## 3. The exact augmented phase-zero packet hypergraph

For fixed \(R_\infty\), let \({\cal P}_0(R_\infty)\) contain every packet

\[
                         p=(K;\{a,b,c\})
\tag{3.1}
\]

such that all three roots in \(X(p)\) belong to \(V_0\). By Section 1,
its upper support \(Y(p)\) automatically lies outside the endpoint
corridor. Give \(p\) three kinds of resources:

\[
                         X(p),\qquad Y(p),\qquad
                         \lambda(p)=\{a,b,c\}.
\tag{3.2}
\]

For variables \(z_p\in\{0,1\}\), the exact phase-zero packet conditions
are

\[
\begin{aligned}
 \sum_{p:P\in X(p)}z_p&\le1 &&(P\in V_0),\\
 \sum_{p:Y\in Y(p)}z_p&\le1
       &&\left(Y\in\binom J{s+1}\setminus{\cal Y}_\infty\right),\\
 \sum_{p:x\in\lambda(p)}z_p&=d_x^{\rm hex}
       &&(2\le x<2s).
\end{aligned}
\tag{3.3}
\]

If every root of \(V_0\) is covered, replace the first inequalities by
equalities. If a leftover set \(Z\subseteq V_0\) is allowed, equality is
required precisely on \(V_0\setminus Z\), and the leftover outgoing edges
must supply

\[
                         d_x^{\rm left}=q_x-d_x^{\rm hex}.
\tag{3.4}
\]

### Proposition 3.1 (packet equivalence)

An integral solution of (3.3), together with collision-free leftover
edges, is exactly a cut-respecting phase-zero outgoing matching assembled
from vertex-disjoint \(C_6\) packets and the stated leftovers. Its
first-edge histogram is (0.2) plus (3.4) plus the petal degrees in (3.3).

#### Proof

The root rows of (3.3) make the packet lower shores disjoint; the upper
rows make their upper shores disjoint. Either alternating half of every
selected packet is therefore a matching on the same six resources.
Theorem 2.1 gives its label contribution. Conversely, every
vertex-disjoint phase-zero hexagon packing records exactly one variable
\(z_p=1\) for each packet and satisfies (3.3). \(\square\)

The packet system has a useful exact lattice ledger. For
\(S\subseteq J\), let

\[
\begin{aligned}
 I_S&=\sum_{P\in V_0\setminus Z}|P\cap S|,\\
 d^{\rm hex}(S)&=\sum_{x\in S}d_x^{\rm hex}.
\end{aligned}
\tag{3.5}
\]

### Theorem 3.2 (mod-three omitted-owner ledger)

Every packet packing satisfies

\[
 \boxed{
 I_S-d^{\rm hex}(S)
          =3\sum_{p:z_p=1}|K(p)\cap S|.}
\tag{3.6}
\]

In particular,

\[
                         I_S-d^{\rm hex}(S)\ge0,
 \qquad I_S-d^{\rm hex}(S)\equiv0\pmod3.
\tag{3.7}
\]

#### Proof

One packet with core \(K\) and petals \(a,b,c\) contributes

\[
 \sum_{P\in X(p)}|P\cap S|
   =3|K\cap S|+|\{a,b,c\}\cap S|
\tag{3.8}
\]

to the root-incidence ledger, and its petal-degree contribution is the
last term in (3.8). Sum over the selected packets. \(\square\)

For a singleton \(S=\{x\}\), (3.6) reads

\[
 \#\{P\in V_0\setminus Z:x\in P\}-d_x^{\rm hex}
                         \in3\mathbb Z_{\ge0}.
\tag{3.9}
\]

For \(S=\{1\}\), every covered root contains \(1\) and no packet has
petal \(1\), so

\[
                         |V_0\setminus Z|\equiv0\pmod3.
\tag{3.10}
\]

Thus an exact packet factor requires \(B-c\equiv0\pmod3\). Otherwise it is
impossible, and every omitted-owner repair must satisfy
\(|Z|\equiv B-c\pmod3\); the smallest positive residue repair omits one or
two roots. This is only a residue statement, not an existence proof for
that small omitted set. More generally, (3.6) audits every coordinate
residue after the leftover contributions (3.4) are fixed. These
congruences are necessary, not sufficient: the upper-resource collision
rows in (3.3) remain essential.

## 4. Pair and triple cancellation of 3-cycle routers

The endpoint action of a phase-homogeneous \(C_6\) ledger switch is a
3-cycle on the three transported strand labels.

### Lemma 4.1 (classification of two- and three-router cancellation)

Let \(\alpha,\beta,\gamma\) be nontrivial 3-cycles.

1. \(\alpha\beta=1\) if and only if \(\beta=\alpha^{-1}\); in particular
   their supports coincide.
2. If \(\alpha\beta\gamma=1\), then, up to relabelling and cyclically
   rotating the three factors, exactly one of the following holds:

   \[
                              \alpha=\beta=\gamma=(a\ b\ c),
   \tag{4.1}
   \]

   or, for four distinct labels \(a,b,c,d\),

   \[
             \alpha=(a\ b\ c),\qquad
             \beta=(a\ d\ b),\qquad
             \gamma=(a\ c\ d).
   \tag{4.2}
   \]

   Conversely both displayed patterns have product one.

#### Proof

The first assertion is immediate. For the second,
\(\alpha\beta=\gamma^{-1}\) must be a 3-cycle. Classify two 3-cycles by
the size of the intersection of their supports. Disjoint supports give a
product of two disjoint 3-cycles, while intersection one gives a 5-cycle.

If the supports agree, inverse cycles multiply to the identity and equal
cycles multiply to their inverse. This gives (4.1).

It remains to consider support intersection two. Relabel so that
\(\alpha=(a\ b\ c)\) and the support of \(\beta\) is \(\{a,b,d\}\).
For \(\beta=(a\ b\ d)\), the product is a pair of transpositions. For the
opposite orientation \(\beta=(a\ d\ b)\), direct multiplication gives

\[
                         \alpha\beta=(a\ d\ c),
\]

so \(\gamma=(a\ c\ d)\). This is (4.2), and the displayed calculation
also proves its converse. \(\square\)

Thus pairwise cancellation requires a returning copy on the same strand
triple. Triplewise cancellation permits one additional geometry: three
faces of a four-strand tetrahedron sharing the hub strand \(a\). Arbitrary
unrelated certificates from a large uncoloured bank still do not cancel.

## 5. Closed router tubes

Let an exact factor be synchronized into layers

\[
 L_0={\cal D},L_1,\ldots,L_s=\overline{\cal D}.
\tag{5.1}
\]

An outgoing \(C_6\) in phase \(t\) is **supported on the strand triple**
\(T=\{P_1,P_2,P_3\}\subseteq{\cal D}\) if its three lower states are the
phase-\(t\) states on those three paths.

A **pair tube** consists of two vertex-disjoint, cut-respecting outgoing
hexagons in distinct phases, supported on the same \(T\), whose transported
3-cycles are inverse. A **cyclic triple tube** consists of three such
hexagons on the same \(T\), with equal transported 3-cycles. A
**tetrahedral triple tube** consists of three routers on four strands whose
transported cycles have the normal form (4.2).

### Theorem 5.1 (closed-tube exactness)

Let \({\cal T}\) be a family of pair, cyclic triple, and tetrahedral triple
tubes whose complete underlying strand sets are pairwise disjoint and
whose hexagon vertex sets are pairwise disjoint. Jointly toggle every
router in every tube. Then:

1. every lower and upper ownership resource is still used exactly once;
2. the total endpoint permutation of every tube is the identity;
3. every root still ends at its own complement after exactly \(s\)
   two-step transitions; and
4. the jointly modified rows are literal fixed-exterior complement
   geodesics.

If the original factor satisfies the Catalan entrance quotas, so does the
new one.

#### Proof

An alternating \(C_6\) toggle preserves the outgoing perfect matching on
its six vertices. The downward matching is unchanged. Because every
router is phase-homogeneous, all components still advance from \(L_t\) to
\(L_{t+1}\); no detached cycle or unequal component can appear.

On one pair tube, the two transported endpoint cycles multiply to one. On
one cyclic triple tube, the product is \(\alpha^3=1\). On one tetrahedral
tube, (4.2) gives identity. Disjoint complete strand supports make the tube
actions independent, so every root retains its original terminal
complement. Each path has \(s\) Johnson steps between complementary
\(s\)-sets, whose Johnson distance is \(s\); it is therefore geodesic.

The complete lower and upper vertex sets were unchanged by the toggles.
They are the full crossing-collar ledger: every intermediate state and
colour remains present exactly once. No owner-dependent exterior motion is
being inferred. Finally, Theorem 2.1 shows that a phase-zero toggle
preserves the entrance histogram, while internal toggles do not meet the
entrance layer. \(\square\)

The theorem supplies a genuinely cycle-rich **identity-monodromy** family,
provided the returning routers exist. It avoids the fixed-exterior
obstruction because only the joint closed tube is installed. An individual
open router is not treated as a physical packet.

## 6. An inverse router cannot occur in the next phase

The most tempting tube places its closing router immediately after its
opening router. This is impossible.

### Theorem 6.1 (one-phase return obstruction)

Let an outgoing phase-\(t\) hexagon have upper vertices

\[
                         K+a+b,\quad K+b+c,\quad K+c+a.
\tag{6.1}
\]

Choose arbitrary downward neighbours \(Z_1,Z_2,Z_3\) of these three upper
vertices in phase \(t+1\). The three \(Z_i\)'s cannot be the lower shore of
another incidence \(C_6\).

#### Proof

Suppose \(Z_i=K'+u_i\) for one common \((s-1)\)-core \(K'\). Then

\[
 K'\subseteq Z_1\cap Z_2\cap Z_3
       \subseteq (K+a+b)\cap(K+b+c)\cap(K+c+a)=K.
\tag{6.2}
\]

Both \(K'\) and \(K\) have size \(s-1\), so \(K'=K\). Each \(Z_i\) is
therefore one of \(K+a,K+b,K+c\), the lower vertices of the original
hexagon. But the synchronized layers are disjoint, while the original
lower vertices lie in \(L_t\) and the \(Z_i\)'s lie in \(L_{t+1}\). This
is impossible. \(\square\)

Hence a phase-zero entrance router can close only in phase \(2\) or later.
The cancellation problem genuinely uses a nontrivial intervening collar.

## 7. The return-router Hall theorem

Let \({\cal A}\) be a vertex-disjoint family of phase-zero routers. Their
strand triples are disjoint because their root supports are disjoint. Let
\({\cal B}\) be a prepacked vertex-disjoint family of cut-respecting
internal routers in phases \(2,\ldots,s-1\).

Make a bipartite graph \(H^-({\cal A},{\cal B})\) by joining
\(A\in{\cal A}\) to \(C\in{\cal B}\) when:

1. \(C\) is supported on the same three transported strands as \(A\); and
2. their transported 3-cycles can be oriented inversely.

Similarly, make \(H^+({\cal A},{\cal B})\) using equal orientation rather
than inverse orientation.

### Theorem 7.1 (pair-tube Hall criterion)

Every entrance router in \({\cal A}\) can be closed by a distinct internal
router from \({\cal B}\) into a pair tube if and only if

\[
                         |N^-(S)|\ge|S|
                         \qquad(S\subseteq{\cal A}).
\tag{7.1}
\]

Failure of (7.1) is an exact return-router cut obstruction.

#### Proof

The desired closing assignment is exactly a matching of
\(H^-({\cal A},{\cal B})\) saturating \({\cal A}\). Apply Hall's theorem.
The internal routers were prepacked vertex-disjoint, so no further
resource conflict is hidden in this matching. \(\square\)

### Theorem 7.2 (cyclic-triple-tube Hall criterion)

Every entrance router can be closed by two distinct internal routers into
a cyclic triple tube if and only if

\[
                         |N^+(S)|\ge2|S|
                         \qquad(S\subseteq{\cal A}).
\tag{7.2}
\]

#### Proof

Replace each entrance router by two identical demand clones and apply
Hall. Since the two clones have the same neighbourhood, the complete set
of clone Hall inequalities is equivalent to (7.2). \(\square\)

Tetrahedral triple tubes do not reduce to (7.2). For an entrance cycle on
\(\{a,b,c\}\), a tetrahedral closure must choose a fourth strand \(d\)
and a compatible ordered pair of internal routers on
\(\{a,b,d\}\) and \(\{a,c,d\}\), with the orientations in (4.2) after a
possible relabelling. Selecting one compatible pair for every entrance
router, subject to internal vertex disjointness, is a three-partite packet
matching problem. The necessary resource cut

\[
 \left|\bigcup_{A\in S}\{\hbox{available internal routers for }A\}\right|
                              \ge2|S|
\tag{7.3}
\]

is not sufficient, because the two routers must occur as one compatible
tetrahedral pair.

These are constructive matching theorems once the two router banks have
been produced. If internal router candidates are not prepacked and can
share vertices, their selection is again a packet hypergraph problem;
ordinary Hall must not be applied before resolving those conflicts.

## 8. Capacity and quota audit

A phase-zero packet near-factor covering all but \(|Z|=o(B)\) nonendpoint
roots has

\[
 |{\cal A}|=\frac{B-c-|Z|}{3}
            =\left(\frac14+o(1)\right)B,
\tag{8.1}
\]

because

\[
                         \frac cB=\frac{s+1}{2(2s-1)}\longrightarrow\frac14.
\tag{8.2}
\]

Thus pair tubes need \((1/4+o(1))B\) disjoint return routers, while cyclic
triple tubes need \((1/2+o(1))B\). A family of strand-disjoint
tetrahedral tubes has at most one phase-zero router per tube, because any
two faces in (4.2) share two strands whereas phase-zero packets have
disjoint root supports. Each such tube therefore uses four strands to
cover only three phase-zero roots. It can cover at most
three-quarters of \(V_0\), leaving at least

\[
                              \frac14|V_0|
\tag{8.3}
\]

roots outside phase-zero packets. Hence strand-disjoint tetrahedral tubes
alone cannot support an \(o(B)\)-leftover entrance near-factor. Avoiding
this loss requires an overlapping global tetrahedral complex, whose
monodromy is no longer a product of independent tubes.

The ballot-forced theorem guarantees only

\[
 \frac{s-1}{(s+1)(s+2)}B
                   =\left(\frac1s+O(s^{-2})\right)B
\tag{8.4}
\]

edge-disjoint uncoloured cycle certificates across all phases. Therefore
that guarantee, without a stronger returning-triple theorem, is smaller
than the pair-tube demand by a factor \(\Theta(s)\). This is not an upper
bound on the available routers; it is an audit showing that the existing
cycle-bank theorem cannot certify (7.1).

There are also two independent quota facts.

1. The orientation variables do not appear in (2.4), by Theorem 2.1.
2. The packet selection and leftover ledger must satisfy every congruence
   (3.6), in addition to the root and upper-resource matching rows (3.3).

Consequently a proof which first constructs an arbitrary near-perfect
hexagon decomposition and only then tries to orient it for Catalan balance
cannot work.

## 9. Exact remaining lemma

The coefficient-one entrance problem is reduced to the following
three-part statement.

> **Closed-tube BFE lemma.** Choose \(R_\infty\subset{\cal D}\) with
> \(|R_\infty|=c\). Construct:
>
> 1. an integral near-factor of the augmented packet system (3.3), with
>    \(|Z|=o(B)\), whose petal degrees plus the explicit leftover edges
>    equal the Catalan target (2.4) and satisfy the omitted-owner ledger
>    (3.6);
> 2. a vertex-disjoint internal return bank satisfying the pair Hall
>    inequalities (7.1), the cyclic-triple inequalities (7.2), or an
>    integral tetrahedral closure-packet matching; and
> 3. a layered leftover \(g/h\) skeleton with identity endpoint matching.
>
> Then Theorem 5.1 installs all matched router tubes jointly, preserves the
> frozen endpoint corridor, and gives an integral exact BFE factor with a
> coefficient-scale identity-monodromy switch family.

The sharp failure certificates are now explicit:

* an augmented-packet matching or residue violation in (3.3) or (3.6);
* a return-router Hall cut (7.1) or (7.2); or
* nonidentity monodromy in the leftover skeleton.

Owner-dependent exterior motion is unnecessary for a closed tube. If a
construction keeps an unmatched nonidentity router, the fixed-exterior
distance obstruction returns, and a valid escape must specify the
ownerwise exterior distance and every mixed crossing-collar state and
colour. No such unmatched-router escape is asserted here.
