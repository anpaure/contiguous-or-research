# Slab Beneš rearrangeability: ideal theorem, literal no-lift, and chronology gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Exact outcome

This note tests the proposed multiscale rearrangeability route based on the
rank-twisted cross-parent \(Q_{R+1}\) slab trade.

The abstract switching theorem is positive. If \(N=2^k\) wires carry
indivisible complete nested-flag bundles and every \(2\times2\) node is an
ideal straight/cross switch, the recursive Beneš network has \(2k-1\)
stages and routes every permutation. Consequently every balanced typed home
assignment is routable after choosing a type-respecting bijection.

The literal slab is not that switch. If

\[
 P_\alpha=\{x_e=\alpha\},\qquad
 Q_\beta=\{x_i=\beta\}
 \qquad(\alpha,\beta\in\{0,1\})
\tag{0.1}
\]

are its old and new packet facets, then

\[
 |P_\alpha\cap Q_\beta|=2^{R-1}
\tag{0.2}
\]

for all four pairs. Its normalized owner-transfer matrix is

\[
 \boxed{\frac12
 \begin{pmatrix}1&1\\1&1\end{pmatrix},}
\tag{0.3}
\]

not the identity or transposition matrix. A slab swaps one home-label bit
with one internal orientation bit; it splits both old packets in half.

There are three stronger literal conclusions.

1. **Persistent-bundle no-go.** Any sequence of slab re-foliations which
   carries every uniquely tagged old packet intact has the same packet
   partition at the end. No nonidentity permutation of owner-attached
   packet bundles is possible.
2. **Sharp chronology toll.** Put \(P=2^{R+1}\). For every
   \(1\le q<R\), every nontrivial slab re-resolution changes the
   owner-rooted lower target at at least \(qP/R\) roots and changes the
   upper target at at least \(qP/R\) roots, regardless of the new
   compiler. A certified synchronized coupling attains both lower bounds
   exactly.
3. **No raw branchwise recursion.** The two slab states terminate in the
   distinct active frames
   \(D\) and \(D-\{i\}+\{e\}\). A transverse next-stage raw slab cannot
   be available for all four independent settings of two predecessor
   nodes. Hence raw slabs do not form a fixed Beneš fabric with one
   independent bit per node.

The abstract balanced nested-flow theorem therefore does not lift by
packet permutation. Its owner flags must instead be grouped directly into
literal \(Q_R\) fibres whose complete tables are certified compiler
columns. Slabs may still be used as correlated re-partitioning variables
in a direct attack on CPCR, but then intermediate flags are discarded and
the Beneš theorem supplies no target-balance implication.

This is a no-go for the proposed automatic conversion, not a no-go for
CPCR.

## 1. Ideal packet-bundle network

An ideal wire carries one indivisible atom

\[
 \mathcal B_x=(\text{packet tag},
   (\mathcal F_{x,q}^-,\mathcal F_{x,q}^+)_{q\le H}).
\tag{1.1}
\]

An ideal switch has the two states

\[
 (A,B)\mapsto(A,B),\qquad (A,B)\mapsto(B,A).
\tag{1.2}
\]

For \(N=2^k\), define \(\mathsf B_k\) recursively. Pair the inputs,
send one member of each pair to each of two copies of
\(\mathsf B_{k-1}\), and use a final paired stage to reach the prescribed
output pairs.

### Theorem 1.1 (ideal Beneš rearrangeability)

The network \(\mathsf B_k\) routes every permutation of its \(N=2^k\)
input bundles. It has exactly

\[
 2k-1\quad\text{stages},
 \qquad
 {N\over2}(2k-1)\quad\text{switches}.
\tag{1.3}
\]

#### Proof

Group the input wires and output wires into pairs. For a requested
permutation \(\pi\), form the bipartite multigraph whose left vertices are
input pairs, whose right vertices are output pairs, and whose edge for
input \(x\) joins its input pair to the output pair containing \(\pi(x)\).
Every vertex has degree two, so every component is an even cycle, with a
doubled edge allowed.

Alternately colour every component red and blue. Each input and output
pair sees one edge of each colour. Use the first and last stages to send
the red edges through the upper recursive copy and the blue edges through
the lower copy. Each colour class induces a permutation of \(2^{k-1}\)
wires, routable by induction. This proves rearrangeability.

The stage count satisfies \(d_k=d_{k-1}+2\), \(d_1=1\), and the switch
count satisfies \(s_k=2s_{k-1}+N\), \(s_1=1\), giving (1.3). \(\square\)

### Corollary 1.2 (balanced typed bundles)

If input bundle types and output-demand types have equal multiplicities,
then every output demand can be met.

#### Proof

Choose an arbitrary bijection within each type and apply Theorem 1.1.
The whole nested lower/upper tower is part of the type and is never
opened. \(\square\)

### Proposition 1.3 (ideal depth lower bound)

A binary switching network with \(N/2\) switches per stage which routes
all \(N!\) permutations has depth

\[
 d\ge
 \left\lceil {2\log_2(N!)\over N}\right\rceil
 =2\log_2N-2\log_2e+o(1).
\tag{1.4}
\]

#### Proof

A depth-\(d\) network has \(dN/2\) binary switches and hence at most
\(2^{dN/2}\) settings and realized permutations. Compare this with \(N!\) and
use Stirling's formula. \(\square\)

Laminarity does not improve this universal bound. Complete nested bundles
may have identical laminar shapes but retain distinct owner or context
tags, leaving all \(N!\) assignments distinct.

## 2. A slab is a re-foliation, not a bundle switch

Let

\[
 \mathcal S\cong Q_{R+1}
\tag{2.1}
\]

have orientation coordinates \(D\cup\{e\}\), where \(|D|=R\), and fix
\(i\in D\). The old shore freezes \(e\), while the new shore freezes
\(i\). Thus the old and new active frames are

\[
 D^0=D,
 \qquad
 D^1=(D\setminus\{i\})\cup\{e\}.
\tag{2.2}
\]

The four intersections in (0.2) are

\[
 P_\alpha\cap Q_\beta
 =\{x_e=\alpha,\ x_i=\beta\}\cong Q_{R-1},
\tag{2.3}
\]

which proves the half-and-half law.

### Theorem 2.1 (no nontrivial intact-bundle permutation)

Give every initial physical \(Q_R\)-packet a unique tag attached to all
of its owners. Suppose that, after any finite sequence of exact slab
re-resolutions, every final \(Q_R\)-packet is required to carry one old
tag intact. Then every final packet equals the correspondingly tagged
initial packet as an owner set. In particular the final packet partition
is the initial partition setwise.

#### Proof

If a final packet \(Q\) carries tag \(j\) intact, then every owner of
\(Q\) lies in the initial packet \(P_j\). Hence \(Q\subseteq P_j\).
Both sets have cardinality \(2^R\), so \(Q=P_j\). Apply this to every
final packet. \(\square\)

This argument is independent of the number of stages, repeated axes,
the rank-twisted status atlas, and compiler choice. Exact owner
preservation never moves an owner; it only changes its packet home.

### Theorem 2.2 (parallel-foliation transfer kernel)

Let \(Q_S\) have two parallel \(Q_R\)-foliations with active coordinate
sets \(D,D'\subseteq[S]\), \(|D|=|D'|=R\). Put

\[
 t=|D\setminus D'|=|D'\setminus D|.
\tag{2.4}
\]

Every nonempty intersection of an old and a new packet has size

\[
 2^{R-t}.
\tag{2.5}
\]

After ordering packets by their common frozen coordinates, the normalized
owner-transfer matrix is, up to row and column permutations,

\[
 \boxed{
 I_{2^{S-R-t}}\otimes 2^{-t}J_{2^t}.}
\tag{2.6}
\]

It is a permutation matrix if and only if \(t=0\).

#### Proof

An old fibre and a new fibre are simultaneously free precisely on
\(D\cap D'\), which has size \(R-t\). If their fixed coordinates agree
on the common inactive set, their intersection is therefore a
\(Q_{R-t}\); otherwise it is empty.

The common inactive set has size \(S-R-t\). For each fixed value on it,
there are \(2^t\) old and \(2^t\) new fibres, and every pair intersects
in \(2^{R-t}\) of the \(2^R\) owners of an old fibre. This is exactly
(2.6). \(\square\)

Thus a multistage uniform frame change has an endpoint dyadic mixing
kernel determined only by its initial and final frames. Intermediate
slabs do not turn that kernel into an arbitrary permutation.

## 3. Sharp owner-rooted chronology obstruction

Fix canonical orientations of the old and new isometric
\(C_{2R}\)-factors on the two shores. For a root \(x\in\mathcal S\), let

\[
 T_{0,q}^\pm(x),\qquad T_{1,q}^\pm(x)
\tag{3.1}
\]

be the old and new lower/upper literal targets of the directed
length-\(q\) windows.

### Theorem 3.1 (universal sharp \(q/R\) flag rewrite)

For every \(1\le q<R\), every new isometric factor on the
\(i\)-frozen shore satisfies

\[
 \boxed{
 |\{x:T_{0,q}^-(x)\ne T_{1,q}^-(x)\}|
 \ge {q\over R}2^{R+1},}
\tag{3.2}
\]

and

\[
 \boxed{
 |\{x:T_{0,q}^+(x)\ne T_{1,q}^+(x)\}|
 \ge {q\over R}2^{R+1}.}
\tag{3.3}

Both constants are best possible, simultaneously at every \(q<R\), at
the cubical factor level. They are attained by certified compiler
conjugates whenever the source compiler is certified through the stated
depths.

#### Proof of the lower bounds

Every old component has direction word \(\pi\pi\), so it uses direction
\(i\) at two antipodal edges. For each oriented \(i\)-edge tail, exactly
\(q\) rooted length-\(q\) windows contain that edge. Since \(q<R\), the
two predecessor intervals are disjoint. The slab has

\[
 {2^{R+1}\over2R}
\tag{3.4}
\]

components, so exactly

\[
 2q{2^{R+1}\over2R}
 ={q\over R}2^{R+1}
\tag{3.5}
\]

old rooted windows use \(i\).

On such an old window, both endpoints of the physical pair \(i\) occur
among the middle vertices. Therefore its lower intersection contains
neither endpoint of \(i\), while its upper union contains both endpoints.
Every new packet freezes \(i\), so every new window contains the same one
endpoint of \(i\) at all its vertices. Its lower intersection and upper
union each contain exactly that one endpoint. Hence neither signed old
target can equal the corresponding new target at any root counted in
(3.5). This proves (3.2)--(3.3). \(\square\)

#### Sharp synchronized construction

Let \(\tau\) toggle the two orientation bits \(i,e\), and let \(\phi\)
transpose the physical pairs \(i,e\). Install any certified oriented
compiler factor \(F\) on the facet \(e=0\), and install \(\tau F\) on
\(e=1\). Their union \(F_0\) is \(\tau\)-invariant. Put

\[
 F_1=\phi F_0.
\tag{3.6}
\]

Then \(F_1\) lies in the two \(i\)-facets, and each restriction is a
physical affine/coordinate conjugate of \(F\).

For every slab vertex \(x\), either \(\phi x=x\) or \(\phi x=\tau x\).
The old outgoing direction is \(\tau\)-invariant, and consequently the
new outgoing direction at \(x\) is the old one unless it is \(i\), in
which case it is \(e\). The two rooted paths therefore agree until an
old \(i\)-tail is met, and agree for the whole length \(q\) outside the
predecessor set counted in (3.5). On that predecessor set the signed
targets differ by the preceding status argument. Thus equality holds in
(3.2)--(3.3).

This construction also gives, for either sign, image indicators
\(\Gamma_0,\Gamma_1\) satisfying

\[
 |\operatorname{supp}\Gamma_1\setminus
       \operatorname{supp}\Gamma_0|
 =|\operatorname{supp}\Gamma_0\setminus
       \operatorname{supp}\Gamma_1|
 \le {q\over R}2^{R+1},
\tag{3.7}
\]

and

\[
 \|\Gamma_1-\Gamma_0\|_1
 \le {2q\over R}2^{R+1}.
\tag{3.8}
\]

Cross-root coincidences can make (3.7) strict; the rootwise mismatch
equalities are the sharp statement.

### Corollary 3.2 (persistent complete flags cannot glue)

Suppose the old owner-rooted flag table includes even the depth-one
lower and upper compiler flags. No nontrivial slab state can glue the
two old half-cube restrictions into legal new packets while preserving
that table owner by owner.

#### Proof

Theorem 3.1 with \(q=1\) forces a mismatch on \(2^{R+1}/R>0\) owners in
each sign, for every new compiler. \(\square\)

Thus the local flag-gluing condition in a conditional physical Beneš
theorem is not merely unproved for arbitrary complete flags. It is false
for every nontrivial raw slab when the flags are required to persist.

## 4. All-depth rewrite toll

For one nontrivial slab of owner mass \(P_a=2^{R_a+1}\), Theorem 3.1
gives the exact universal lower bound

\[
 \sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
 |\{x:T_{0,q}^\epsilon(x)\ne T_{1,q}^\epsilon(x)\}|
 \ge {H(H+1)\over R_a}P_a,
\tag{4.1}
\]

provided \(H<R_a\).

Consequently, if one stage uses owner-disjoint nontrivial slabs of common
dimension \(R\) and total switched owner mass \(T\), its persistent-flag
rewrite toll is at least

\[
 \boxed{{H(H+1)\over R}T.}
\tag{4.2}
\]

At the CPCR scale

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\to\infty,
 \qquad H=o(R),\qquad R=o(m),
\tag{4.3}
\]

one has

\[
 {H^2\over R}={m\omega(m)^2\over R}\longrightarrow\infty.
\tag{4.4}
\]

Therefore a stage which nontrivially re-resolves \(\Omega(W)\) owners
cannot transport a prescribed common all-depth flag table with an
\(o(W)\) aggregate mismatch budget.

This is a statement about lifting a fixed abstract flag table. It is not
a lower bound on the final CPCR energy after compilers are discarded and
freshly selected, because later choices may construct a different
balanced table rather than transport the old one.

## 5. Raw slabs do not form an independent-bit Beneš recursion

A raw slab node \(v\) has terminal active frame

\[
 D_v^0=D_v,
 \qquad
 D_v^1=D_v-\{i_v\}+\{e_v\},
 \qquad D_v^0\ne D_v^1.
\tag{5.1}
\]

Both output packets of one state share that frame. A subsequent raw slab
may pair two packets only when their active \(R\)-sets are equal.

### Theorem 5.1 (branchwise frame incompatibility)

Suppose a fixed second-stage switch pairs an output of predecessor node
\(v\) with an output of a different predecessor node \(w\). If this
second-stage slab is required to exist for all four independent first-stage
settings \((a,b)\in\{0,1\}^2\), then both predecessor nodes are trivial:

\[
 D_v^0=D_v^1=D_w^0=D_w^1.
\tag{5.2}
\]

In particular, two nontrivial raw slab nodes cannot feed a fixed
transverse next-stage slab with branchwise independent settings.

#### Proof

Slab compatibility of the paired inputs requires

\[
 D_v^a=D_w^b
\tag{5.3}
\]

for all four pairs \((a,b)\). Fixing \(b=0\) and comparing \(a=0,1\)
gives \(D_v^0=D_v^1\). Fixing \(a=0\) similarly gives
\(D_w^0=D_w^1\), and (5.2) follows. \(\square\)

The alternatives are exact and narrow:

1. correlate predecessor bits, so the configuration space is not a
   Cartesian switch cube;
2. make the interconnection adaptive to earlier choices; or
3. replace every logical node by a frame-restoring compound gadget whose
   two terminal states have the same frame.

The first alternative abandons the Cartesian independent-switch
interpretation, though a correlated code on a fixed topology is not ruled
out. The second makes the interconnection adaptive and thus abandons the
fixed topology. The third
cannot be a home switch on the same \(Q_{R+1}\) support. Indeed, a common
terminal active \(R\)-frame determines the unique inactive coordinate and
hence the unique unordered pair of \(Q_R\) facets. Restoring the frame
restores the packet-home partition. Any surviving logical bit is therefore
compiler/ordered-port holonomy on the same packets, not a permutation of
packet homes. Such a compound has zero net direction boundary but may
retain a nontrivial compiler context and literal target residue.

## 6. Repeated-axis and frame chronology

Along one packet-frame path write

\[
 D_{t+1}=D_t-\{i_t\}+\{e_t\}.
\tag{6.1}
\]

Then exactly

\[
 \boxed{
 \mathbf1_{D_d}-\mathbf1_{D_0}
 =\sum_{t=0}^{d-1}(e_{e_t}-e_{i_t}).}
\tag{6.2}
\]

Pure cubical legality is equivalent to every partial sum in (6.2) being a
zero-one vector of coordinate sum \(R\). Thus a coordinate cannot be
removed while inactive or inserted while active. Its insertion and
removal events must alternate, with the first event determined by its
initial membership.

### Corollary 6.1 (closed nontrivial routes repeat axes)

If \(D_d=D_0\) and the route is nontrivial, every coordinate used by the
route has equal positive insertion and removal counts and hence occurs in
at least two exchanges.

Aggregate frame closure therefore cannot avoid repeated physical axes.
It also does not prove compiler closure. An ordered isometric compiler
state consists of an ordered active frame, phases, and frozen endpoint
orientations. A closed set-valued frame walk can return with a nonidentity
permutation or affine holonomy of this data.

For one packet-frame path of fixed dimension \(R\), the direction-support
derivative telescopes as

\[
 z_q^{(1)}=qg_R(\mathbf1_{D_d}-\mathbf1_{D_0}),
 \qquad g_R={2^R\over R}.
\tag{6.3}
\]

For a synchronized aggregate two-packet slab chain the coefficient is
twice this:

\[
 z_q^{(2)}=2qg_R(\mathbf1_{D_d}-\mathbf1_{D_0}).
\tag{6.3a}
\]

A closed route has zero direction residue, but (6.3)--(6.3a) see neither
the ordered compiler holonomy nor the literal target derivative.
Repeated-axis closure is therefore necessary and not sufficient. In a
general network whose packet mates change, the correct statement is the
sum of the one-packet telescopes with packet multiplicity.

Rank-twisted physical legality is stronger still: every exchange must be
a current Hamming-two parent-status move with a common active set on its
two input facets, and every stage must use owner-disjoint slabs.

### Lemma 6.2 (matching-frame transposition)

Write one current cross-half matching as a bijection

\[
 \mu:A\longrightarrow C.
\tag{6.4}
\]

Choose distinct \(a,b\in A\), remove the two matching edges

\[
 \{a,\mu(a)\},\qquad \{b,\mu(b)\},
\tag{6.5}
\]

and activate the cross edge \(e=\{a,\mu(b)\}\). The unique perfect
matching which agrees with \(\mu\) elsewhere and contains \(e\) is

\[
 \mu'=\mu\circ(a\ b),
\tag{6.6}
\]

whose other changed edge is \(e^*=\{b,\mu(a)\}\).

#### Proof

After \(a\) is matched to \(\mu(b)\), the only unmatched vertices among
the four displayed coordinates are \(b\) and \(\mu(a)\), so they must be
paired. This is exactly (6.6). \(\square\)

Thus a path state is not only its active set. It includes the current
matching, frozen orientations, and compiler context. A closed active-set
walk must also close the ordered product of matching transpositions. The
original cyclic rank-dependent matching atlas is not automatically closed
under these updates.

### Theorem 6.3 (directed ordered-port gluing criterion)

Cut every old compiler cycle at its two \(i\)-edges. Each resulting
oriented path has a record

\[
 (a,b;w),
\tag{6.7}
\]

where it runs from \(a\) to \(b\) and \(w\) is the ordered word of the
remaining \(R-1\) distinct directions. Keep all these path edges and
permit only \(e\)-edges between the two old \(e\)-facets. The two halves
glue to an oriented isometric factor in one new \(i\)-facet if and only if
their records can be paired as

\[
 \boxed{
 (a,b;w)\longleftrightarrow(b+e,a+e;w).}
\tag{6.8}
\]

For undirected factorhood one may simultaneously reverse both paired
records, equivalently reverse the whole new cycle. Independent reversal of
only one retained path is not allowed. For a prescribed oriented flag
table, (6.8) itself is required.

#### Proof

The only possible retained-edge cycle through the first path is

\[
 a\mathrel{\xrightarrow{w}}b
 \mathrel{\xrightarrow{e}}b+e
 \mathrel{\xrightarrow{w'}}a+e
 \mathrel{\xrightarrow{e}}a.
\tag{6.9}
\]

Its direction word is \(w,e,w',e\). Period \(R\) is necessary and
sufficient for an isometric \(C_{2R}\), so \(w'=w\). This is (6.8), and
pairing every record covers every owner exactly once. \(\square\)

The criterion is nonvacuous. If the compiler on one old facet is \(F\),
install the translate which toggles \(i\) and \(e\) on the other facet.
Its ordered half-path records are the partners in (6.8), giving the
synchronized sharp construction of Theorem 3.1. Around a multistage
switch graph, however, the ordered products of these translations must lie
in the stabilizer of the requested compiler table \(f\). For pure
translations on a fixed frame this requires

\[
 \bigoplus_a(e_a+i_a)
 \in\operatorname{Stab}_{\rm trans}(f).
\tag{6.10}
\]

It reduces to zero only when the translation stabilizer is trivial (in
particular when literal owner labels are fixed pointwise). Moving frames
require the corresponding conjugated product. This is the compiler-context
cocycle left invisible by (6.2)--(6.3).

### Lemma 6.4 (exact repeated-cut exposure)

Open \(k\ge1\) distinct direction seams of one doubled-permutation cycle.
If the cyclic gaps of unopened directions in one half-word are
\(g_1,\ldots,g_k\), so that \(\sum_jg_j=R-k\), then the number of rooted
length-\(q\) windows avoiding every opened seam is exactly

\[
 2\sum_{j=1}^k(g_j-q+1)_+.
\tag{6.11}
\]

Consequently at least

\[
 \boxed{2\min\{R,k+q-1\}}
\tag{6.12}
\]

roots have exposed chronology.

#### Proof

A window avoids the seams precisely when its \(q\) consecutive letters
fit in one unopened gap, giving (6.11) in the two identical half-words.
Since

\[
 (u-q+1)_++(v-q+1)_+\le(u+v-q+1)_+,
\]

the right side of (6.11) is at most
\(2(R-k-q+1)_+\). Subtract from \(2R\). \(\square\)

This is an exposure count, not an unconditional final mismatch count.
Correlated removal and reactivation can close seams, in which case the
ordered-port holonomy, rather than the historical number of cuts, decides
the final literal table.

## 7. A balanced laminar home assignment outside every slab network

The obstruction is not limited to already grouped packet atoms. Even a
perfectly balanced one-level laminar owner assignment need not have
physical packet fibres.

Fix one orientation cube \(Q_{R+1}\) with bits
\(x_1,\ldots,x_{R+1}\), and prescribe the two homes

\[
 H_b=\{x:x_1\oplus x_2=b\},
 \qquad b\in\{0,1\}.
\tag{7.1}
\]

Each home has exactly \(2^R\) owners. Nevertheless neither is a physical
\(Q_R\)-packet.

### Theorem 7.1 (parity-home obstruction)

No exact tiling of \(Q_{R+1}\) by two physical coordinate-disjoint
\(Q_R\)-packets realizes the two homes in (7.1). Consequently no finite
slab sequence supported on this fixed carrier and ending in two
\(Q_R\)-packets inside it realizes this balanced home assignment.

#### Proof

A physical \(Q_R\)-packet is connected in the orientation-cube graph.
Inside \(H_b\), an edge in direction \(1\) or \(2\) leaves the parity
class, while the remaining directions preserve both \(x_1\) and
\(x_2\). Thus \(H_b\) is the disjoint union of two
\(Q_{R-1}\)-components and is disconnected. It cannot be a physical
\(Q_R\). Every final part of a slab re-resolution supported on this
carrier is still a physical \(Q_R\) inside it, proving the last claim.
\(\square\)

Assume the fixed exterior contains at least \(H\) coordinates present in
every owner and at least \(H\) coordinates absent from every owner. (This
is automatic in the CPCR parameter range inside a typical cylinder.) This
can be made a locally integral, collision-free nested-flag example. Choose
common
selected exterior coordinates \(d_1,\ldots,d_H\) and common absent
exterior coordinates \(a_1,\ldots,a_H\). At every owner \(X\), prescribe

\[
 X_q^-=X\setminus\{d_1,\ldots,d_q\},
 \qquad
 X_q^+=X\cup\{a_1,\ldots,a_q\}.
\tag{7.2}
\]

These are literal nested flags, and their target maps are injective on
the local cylinder at every depth. Append the exactly balanced home bit
\(x_1\oplus x_2\). The two home multiplicities are equal, but Theorem 7.1
prevents grouping the owners into the two requested physical packets.

This is a balanced one-level home assignment decorated with valid nested
flags, equivalently a local \(0/1\) partial flow. It disproves automatic
cubical grouping from laminarity plus equal home counts. It is not a
complete globally floor/ceiling-balanced nested resolution, and the home
bit is not part of the Boolean-lattice circulation theorem. The abstract
nested-flow theorem itself supplies no cubical-home assignment.

## 8. The restricted positive result: coordinate re-foliation

There is one exact multistage statement which slabs do realize.

### Theorem 8.1 (minimal re-foliation between parallel frames)

In a pure orientation cube \(Q_S\), let \(D,D'\) be active \(R\)-sets
and put \(t=|D\setminus D'|\). The parallel \(D\)-foliation can be changed
to the parallel \(D'\)-foliation by exactly \(t\) stages of owner-disjoint
\(Q_{R+1}\) slab resolutions. No fewer uniform one-axis-exchange stages
can suffice.

#### Proof

Pair the coordinates of \(D\setminus D'\) bijectively with those of
\(D'\setminus D\). At one stage, for a pair \((i,e)\), pair every two
current packets which agree on all inactive coordinates except \(e\).
Each pair has union \(Q_{R+1}\) with active coordinates
\(D_t\cup\{e\}\). Re-resolve every such slab along \(i\). The slabs are
owner-disjoint and the new global active set is
\(D_t-\{i\}+\{e\}\). Repeating for all \(t\) pairs reaches \(D'\).

Each slab stage changes the active set by Johnson distance at most one,
whereas \(d_J(D,D')=t\). Hence \(t\) stages are necessary. \(\square\)

Theorem 8.1 changes coordinate roles and packet homes. It does not route
the old bundles; its endpoint owner-transfer matrix is (2.6). It also
ignores rank-twisted parent admissibility. A literal use in the global
atlas must separately construct every required cross-parent Hamming-two
slab bank.

## 9. Exact connection to the balanced nested-flow theorem and CPCR

The abstract Boolean-lattice circulation theorem produces integral
owner-rooted nested lower and upper flags with floor/ceiling-balanced
loads. It does not produce physical packet homes or compiler cycles.

For a physical packet \(Q\), let \(\mathscr C(Q)\) be the catalogue of
complete owner-resolved, all-depth, two-sign flag tables supplied by the
certified compiler conjugates on \(Q\). A prescribed abstract table
\(f=(f_X)_X\) is literalizable after slab re-partitioning if and only if
there is a slab-reachable physical \(Q_R\)-tiling \(\mathcal Q\) such
that

\[
 \boxed{f|_Q\in\mathscr C(Q)\qquad(Q\in\mathcal Q).}
\tag{9.1}
\]

Equation (9.1) is the exact cubical grouping/home condition. Ideal Beneš
routing does not imply it:

* Theorem 2.1 rules out nontrivial permutation of already grouped
  owner-attached bundles.
* Theorem 7.1 rules out some balanced splittable home tables on a fixed
  carrier before compiler constraints are even imposed.
* Corollary 3.2 rules out transporting a fixed complete compiler table
  through a nontrivial raw slab.

There are therefore two logically different uses of slabs.

1. **Transport interpretation.** Keep the abstract flags attached to
   owners through every stage. This is the proposed Beneš lift, and it is
   impossible for every nontrivial raw switch by Theorem 3.1.
2. **Configuration interpretation.** Use slabs only to reach a final
   packet tiling, discard all intermediate compiler flags, and install a
   fresh compiler in every final packet. This remains legal and may be
   useful for CPCR, but it is a direct common all-depth floor-covariance
   problem. The ideal routing theorem contributes no flag-realizability
   statement.

CPCR asks for one final legal resolution state with

\[
 \sum_{q\le H}\sum_{\epsilon=\pm}\sum_T
 (L_q^\epsilon(T)-c_q)(L_q^\epsilon(T)-c_q-1)=o(W).
\tag{9.2}
\]

Nothing proved here refutes (9.2). The report proves that a positive CPCR
construction cannot be obtained merely by routing the already-known
abstract balanced nested flow through a raw-slab Beneš network.

## 10. Independently audited boundary

The decisive obstruction has four independent proofs or checks.

1. **Owner intersections:** the four old/new facet intersections give the
   rank-one kernel (0.3).
2. **Cardinality:** a final packet carrying one old tag intact must equal
   that old packet.
3. **Literal status:** an old window using removed axis \(i\) has
   lower/upper statuses \(0/2\) on that pair, while every new window has
   status \(1\).
4. **Frame branching:** two nontrivial predecessor bits cannot feed a
   fixed transverse slab for all four settings.

Proved:

* exact ideal Beneš rearrangeability and its stage count;
* the ideal information-theoretic depth lower bound;
* the exact slab transfer kernel and its general parallel-foliation form;
* impossibility of every nontrivial intact owner-bundle permutation;
* the sharp universal \(q/R\) rootwise flag-rewrite theorem;
* the all-depth rewrite toll;
* failure of a fixed independent-bit raw-slab recursion at the second
  transverse stage;
* the repeated-axis/frame-closure law;
* an explicit balanced laminar parity-home obstruction; and
* the minimal positive re-foliation theorem for two parallel frames.

Not proved or claimed:

* that every physically groupable nested table is slab-reachable;
* connectivity of the general \(Q_R\)-subcube-tiling flip graph;
* a frame-restoring compound switch with two useful terminal states;
* rank-twisted availability of the global banks in Theorem 8.1;
* all-depth compiler holonomy cancellation in a compound network; or
* CPCR.

The exact surviving network problem is not a Beneš permutation theorem.
It is to construct a correlated, frame-restoring family of slab
re-partitionings whose **final** compiler columns satisfy CPCR. Any such
family must be analyzed through its cubical grouping, pathwise frame
holonomy, repeated-axis chronology, and physical target loads.
