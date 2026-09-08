# Controlled-debt packet composition and an exact four-packet K17 macro

Date: 2026-07-31  
Status: dependency-clean composition theorem and exact finite K17
old-rail instantiation; no full ordered four-transversal or K17 equality claim

## 0. Verdict

The common-exterior packets can be ordered without treating each
intermediate factor as an accepting recursive state.  The exact state across
a packet boundary is not a scalar palette score.  It consists of

1. the named palette defect on the labels still live across the boundary;
2. the common-core alternating-linkage signature of the augmented occurrence
   graph;
3. the open physical in/out sockets and their residual reachability relation;
4. the protected occurrence/flag ledger, named deeper-shadow debt, residence
   collars and private-socket ledger; and
5. at an accepting endpoint only, one fixed decoration and an ordered
   transparent leaf-peelable gluing list.

The packet may contain arbitrarily many bounded-port circuits.  What must be
bounded is the number of simultaneously live labels/sockets and the exposed
linkage debt, not the total number of circuits or the lengths of the
augmenting paths.

On the frozen K17 source, four pairwise support-disjoint packets have an exact
monotone ordering

\[
                     3836,\quad919,\quad705,\quad783.                 \tag{0.1}
\]

Every prefix preserves the exact rank-8 edge palette and the complete
rank-10 edge-union palette, loses no previously supported lower-turn colour,
strictly raises lower-turn support, and strictly raises augmented occurrence
rank.  The ledger is

\[
\begin{array}{c|c|c|c|c}
\text{prefix}&\text{lower holes}&\text{occurrence deficiency}&
\text{correlation excess}&\text{components}\\ \hline
0&3826&4134&308&11\\
3836&3822&4130&308&9\\
+919&3820&4127&307&10\\
+705&3818&4124&306&9\\
+783&3816&4121&305&9.
\end{array}                                                       \tag{0.2}
\]

Thus the compound packet repairs ten lower-turn colours and gains thirteen
units of occurrence rank.  Four repaired colours lie in the exact common
1,297-colour six-bank shell.  This is a genuine improving macro, but it is
still very far from an accepting K17 state.

## 1. Support-disjoint packet composition

Let \(F\) be a Johnson two-factor on an owner set \(V\).  A packet
\(P=(R_P,A_P)\) deletes the factor edges \(R_P\) and inserts \(A_P\), with

\[
                 F_P=(F\setminus R_P)\cup A_P.                       \tag{1.1}
\]

Its physical support \(Z(P)\) is the set of endpoints of the deleted edges.
For the common-exterior packets considered here, every inserted edge also
has both endpoints in \(Z(P)\).  Let \(m_F(c)\) denote the lower-turn
multiplicity of colour \(c\), and put

\[
                 \delta_P(c)=m_{F_P}(c)-m_F(c).                       \tag{1.2}
\]

### Lemma 1.1 (commuting packet law)

If \(P_1,\ldots,P_s\) have pairwise disjoint physical supports, then:

1. all \(s!\) orders are legal and have the same endpoint;
2. every intermediate graph is a Johnson two-factor;
3. the lower-turn multiplicity after a prefix \(I\) is exactly

   \[
                 m_I(c)=m_F(c)+\sum_{i\in I}\delta_{P_i}(c);          \tag{1.3}
   \]

4. every edge-palette multiset preserved by each packet is preserved by
   every prefix.

#### Proof

No vertex is incident with changed edges from two packets.  Hence toggling
one support changes neither the deleted nor inserted edge status on another
support, proving commutation and degree two.  A turn can change only at an
endpoint of a deleted edge, and every such endpoint belongs to exactly one
support.  Therefore the turn deltas add without a cross term.  Edge-palette
multisets add supportwise in the same way. \(\square\)

### Corollary 1.2 (exact palette-prefix test)

An order is old-support preserving exactly when, for every prefix \(I\) and
every colour with \(m_F(c)>0\),

\[
                 m_F(c)+\sum_{i\in I}\delta_{P_i}(c)\ge1.             \tag{1.4}
\]

This is an exact integer test.  Counting gains without the negative
multiplicity terms is not sound.

For a long packet, define the live palette set at a cut to be the nonzero
defect labels which can still be touched by a future circuit.  A label whose
target status is already correct and which no future circuit touches is
retired.  This retirement rule permits packet length to grow while the live
palette state remains bounded, but it does not prove such a bound; uniform
boundedness is an explicit construction hypothesis below.  This is the first
controlled-debt ledger.

## 2. Exact common-core linkage state

Let \(G_i=(L,R;E_i)\) be the fixed-universe augmented occurrence graph after
packet prefix \(i\), with equal shore order \(N\).  For one transition put

\[
                         H_i=G_{i-1}\cap G_i.                         \tag{2.1}
\]

Fix a maximum matching of \(H_i\).  Its exposed vertices, together with the
endpoints of occurrence edges deleted or added at this transition, are the
live alternating boundary.  The linkage signature records which equally
sized boundary subsets can be joined by internally vertex-disjoint
alternating paths in the common core.  Equivalently it is the appropriate
strict-gammoid boundary relation; a scalar matching deficiency is only its
rank projection.

### Theorem 2.1 (common-core acceptance row)

Write

\[
                  \nu(H_i)=N-r_i.                                    \tag{2.2}
\]

If the new columns contain \(\lambda_i\) pairwise vertex-disjoint
augmenting paths relative to a maximum common-core matching, and the
resulting matching is certified maximum in \(G_i\), for example by an
equal-cardinality vertex cover, then

\[
                  \nu(G_i)=N-r_i+\lambda_i,
        \qquad \operatorname{def}(G_i)=r_i-\lambda_i.                 \tag{2.3}
\]

Equivalently, \(\operatorname{def}(G_i)\le q\) exactly when

\[
 |N_{G_i}(X)\setminus N_{H_i}(X)|
 \ge |X|-|N_{H_i}(X)|-q
 \quad\text{for every }X\subseteq L.                                 \tag{2.4}
\]

#### Proof

Augment simultaneously along the disjoint paths.  This gives the lower
bound in (2.3).  The supplied maximum certificate gives the reverse
inequality.  Without it, absence of a deaugmenting component in one
displayed symmetric difference proves only the lower bound.  Formula (2.4)
is Hall's theorem after separating common and new neighbours. \(\square\)

For composition, one must retain the pairing-resolved linkage relation, not
only \(r_i\).  If two chunks have disjoint interiors, their signatures
compose by existentially identifying the same distinct interface terminals;
this is relational composition in the vertex-disjoint path gammoid.  The
result is accepted only when the requested terminal pairing is present.
This avoids the circular instruction “choose a matching which later
extends.”

## 3. Physical deletion/contraction state

The alternating-linkage state does not enforce physical directed
acyclicity.  These are different graphs and must be carried jointly, keyed
by the same selected packet columns.

Delete all physical arcs touched by a macro.  Let \(F^\circ\) be the literal
residual directed forest, and let \(B\) contain every open tail/head socket
and every adhesion vertex.  Export

\[
       R^\circ=\operatorname{Reach}(F^\circ)\cap(B\times B),           \tag{3.1}
\]

together with named in/out degree and palette debts.  If \(A\subseteq
B\times B\) is a proposed set of filling arcs, then

\[
 F^\circ\cup A\text{ is acyclic}
 \quad\Longleftrightarrow\quad
 (B,R^\circ\cup A)\text{ is acyclic}.                                \tag{3.2}
\]

After composing two blocks, take the union of their boundary relations and
glue arcs, reject a directed cycle, and export the transitive closure on the
parent boundary.  For one contracted arc \(T\to H\), (3.2) reduces exactly
to

\[
                              H\not\leadsto T.                         \tag{3.3}
\]

This relation is minimal for an unrestricted glue catalogue: two residuals
which differ only on \(H\leadsto T\) are distinguished by the context which
adds \(T\to H\).

There is an essential delete-first qualification.  Reachability can be
updated compositionally when arcs are **added** to a fixed residual core;
it cannot in general be decremented after deleting an arc from a summarized
transitive relation.  A long repair packet must therefore either delete the
union of all touched old arcs before exporting \(R^\circ\), or recompute the
literal residual reachability after every later deletion.  A scalar or
relation-only deletion update is not exact.

### 3.1 Interval and residence boundary state

For each controlled depth, record the signed change in the literal
union/intersection witness multiplicity of every target touched by a changed
window.  A target with an untouched protected witness is retired; a target
whose last witness is touched remains as a named live debt.  These sparse
vectors compose by addition of the exact changed-window ledgers, just as in
(1.3).  Immediate turn palettes are only their first row and do not determine
the deeper rows.

For residence, each open fragment exports, for every coordinate, its first
and last bit and its initial/terminal positive-run lengths capped at the
required threshold.  It also exports every already internal short-run
violation.  Gluing two fragments either keeps the two boundary runs separate
or merges them by capped addition, according to their boundary bits.  An
internal short run can never be repaired by later endpoint gluing.  Thus the
composition is exact on a declared bounded collection of live fragments,
even though the fragment interiors and the packet itself may be long.  The
literal collar description has size `O(mb)` for boundary size `b`; a
uniform finite alphabet additionally requires a proved quotient of coordinate
and target identities.

## 4. A dependency-clean controlled-debt macro theorem

At a packet cut the exact exported state is the correlated tuple

\[
 \Sigma=(d^{\rm pal},\Gamma^{\rm aug},R^{\rm phys},
          d^{\rm sh},C^{\rm run},\Pi^{\rm comp},{\cal P}).             \tag{4.1}
\]

Here \(d^{\rm pal}\) is the named palette/degree defect, \(\Gamma^{\rm
aug}\) the pairing-resolved alternating-linkage signature, \(R^{\rm phys}\)
the strict boundary reachability relation, \(d^{\rm sh}\) the named
all-depth changed-witness debt, \(C^{\rm run}\) the capped coordinate-run
collars plus internal violations, \(\Pi^{\rm comp}\) the current physical
component/attachment forest, and \({\cal P}\) the occurrence-labelled
private ports and ownership guards.  These coordinates are correlated: the
state space contains only tuples realized by one literal set of packet
columns, not the Cartesian product of their separate projections.

Composition adds the signed defect ledgers, composes \(\Gamma^{\rm aug}\)
through distinct shared terminals, and—over a frozen delete-first physical
core—takes transitive closure of \(R^{\rm phys}\) after rejecting cycles.
If a later chunk deletes an old arc, its literal residual relation is first
recomputed.  The remaining coordinates use the exact changed-window and
capped-run updates of Section 3.1, update the attachment forest, and
intersect the surviving private guards.  This is the promised finite
composition law.

### Theorem 4.1 (conditional repair-and-glue theorem)

Suppose a recursive step supplies the following literal data.

1. **Boundary-deficient input.**  Residual rail forests, not two complete
   parent solutions, with named palette/degree debts, bounded boundary
   \(B\), and the exact reachability relation (3.1).
2. **Ordered repair packet.**  A finite ordered list of bounded-port
   circuits.  Its length may grow.  At every cut, the live palette labels,
   physical sockets and exposed alternating terminals have size at most a
   declared bound \(b\).  The sparse palette update uses (1.3), and the
   physical and occurrence states use (3.2) and Theorem 2.1.
3. **Accepting endpoint decoration.**  At the packet endpoint, both turn
   palettes have their required values and the augmented occurrence graph
   has an explicitly certified perfect matching \(D\), including every
   declared protected port.
4. **Fixed-decoration transparent gluing list.**  There is an ordered list
   of literal owner-preserving, degree/capacity-legal incidence hexagons.
   Three tests are certified separately at every step: (a) the physical
   component update remains linear and performs the advertised merge;
   (b) the selected local lower and upper turn-colour multisets agree
   separately before and after the toggle and the retained-fragment boundary
   mark types alternate, so the same fixed decoration \(D\) survives; and
   (c) the occurrence-labelled gap attachment remains acyclic and admits
   the advertised private leaf peeling.
5. **Private/physical guards.**  Every declared private occurrence and
   socket survives, each physical reachability update passes (3.2), and
   leaf peeling of the fixed decorated gap graph removes the complete
   advertised forest.  If all-depth support or residence is advertised,
   the exact changed-window and capped-run compositions of Section 3.1 must
   also end with zero debt; endpoint data alone are not sufficient.

Then the packet endpoint followed by that ordered list is a valid decorated
linear-forest macro with the advertised boundary state.  If the list spans
the component forest, it gives the advertised connected closure.

Intermediate repair states need not have complete palettes or a perfect
decoration.  Only the packet endpoint and subsequent fixed-decoration
transparent states are accepting.

#### Proof

Lemma 1.1 and the named defect ledger give the palette statement.  Theorem
2.1 supplies the endpoint decoration without assuming its existence.
Equation (3.2) preserves directed acyclicity.  Each transparent hexagon
preserves the same selected local palette multisets and alternating marks,
so \(D\) remains a decoration.  The contracted attachment-forest test
preserves linearity and the ordered spanning list gives the stated
topology.  Private guards are literal exclusions/ownership checks, so they
survive by hypothesis. \(\square\)

The theorem is conditional but noncircular: each hypothesis is a finite
certificate on the supplied residuals, packet columns, matchings,
reachability relation, and ordered gluing list.  It does not assume a
completed parent or an unspecified future extension.

## 5. Why residence must be a separate regenerated state

The theorem above is central Catalan state, not a compiler theorem.  A
compiler-ready version must additionally provide a literal interior
rethreaded chronology and verify:

1. coordinatewise residence (equivalently the exact erosion-source row);
2. explicit all-depth union/intersection witnesses; and
3. the lower envelope/compiler matching.

These rows cannot be inferred from endpoint sockets.  In the exact repaired
\(m=5\) base, the 42 path interiors contain 31 one-runs of length two,
bounded by zeroes strictly inside 18 paths, with coordinate multiplicities

\[
                         (5,5,2,3,3,3,3,3,3,1).                       \tag{5.1}
\]

At depth \(d=2\), every run must have length at least three.  Reversing or
permuting those intact paths and changing the endpoint socket cannot alter
(5.1), so that particular forest requires an interior rethread.  Item 2188
now supplies a different exact-palette 210-edge/42-path forest with no
internal run below three, obtained by changing 119 matching partners.  Its
unjoined fragments still miss 21 deeper targets.  Thus the central `m=5`
residence row is solved, while endpoint joining, common-decoration and
reachability transport, all-depth coverage, and the compiler remain open.
Every such rethread must still have its palette, occurrence linkage,
physical reachability, all-depth witnesses and residence recomputed;
“all-depth support plus endpoint closure” is not an accepting substitute.

## 6. Why the input must be boundary-deficient

The Pascal determinant split rules out scalar two-full-parent recursion.
Two complete embedded \((m-1)\)-solutions force \(\operatorname{Cat}_m\)
cross edges between their middle rails; the induced edge excess is

\[
                   \operatorname{Cat}_m-2\operatorname{Cat}_{m-1}\ge0,
                                                                         \tag{6.1}
\]

so a cycle is forced.  Thus Theorem 4.1 must start with deficient rails and
carry their named debts.  The same algebra gives the exact atom-contraction
condition (3.3).  Reachability/socket state is therefore forced by the
determinant, rather than optional solver metadata.

## 7. Exact K17 four-packet certificate

The six frozen K17 banks share 1,297 missing lower-turn colours.  Their
largest rank-6-core extension shell has order five, attained at nine cores;
the dual rank-8-cap shell also has order five, attained at two caps.  This is
the sharp localized profile inside the robust shell against which the packet
gains are measured.

Packets (0.1) have pairwise disjoint physical supports.  Their exact
common-core transition table is

\[
\begin{array}{c|c|c|c|c|c}
P&|Z(P)|&|E_{\rm del}^{\rm occ}|&
\operatorname{def}(H)&
\operatorname{rankloss}(G_{\rm old}\to H)&\lambda\\ \hline
3836&10&15&4136&2&6\\
919 &10&15&4131&1&4\\
705 & 8&12&4127&0&3\\
783 & 8&12&4125&1&4.
\end{array}                                                       \tag{7.1}
\]

The vertex lengths of the certified disjoint augmenting components are

\[
\begin{array}{c|c}
3836&4,4,4,4,4,6\\
919 &4,4,8,10\\
705 &4,4,4\\
783 &4,4,4,14.
\end{array}                                                       \tag{7.2}
\]

Thus the incremental physical support is at most ten owners, deletion from
the occurrence graph is at most fifteen edges, common-core rank loss is at
most two, and the exposed augmenting debt is at most six paths.  The path
length can already reach fourteen; bounded debt does not mean bounded path
length.

All 24 packet orders have the same literal endpoint.  The displayed order
has the monotone ledger (0.2).  It gains colours

```text
0x9435 0x949c 0x9515 0x1111d
0x2aac 0xa8aa
0x10ca5 0x118a3
0x1154a 0x11554
```

and loses none.  The first three gains and `0x2aac` lie in the common
1,297-colour shell.

### 7.1 Exact deeper-shadow and physical-boundary ledger

The q1-positive macro is **not** all-depth monotone.  An exact cumulative
prefix replay gives

\[
\begin{array}{c|c|c|c|c|c}
\text{prefix}&(N_2,N_3)&\Phi_3=2N_2+N_3&
|V_{\rm short}|&\text{source flags lost}&
\text{contraction cycles}\\ \hline
0&(2025,1221)&5271&7115&0&0\\
3836&(2023,1223)&5269&7115&2&2\\
+919&(2023,1221)&5267&7111&2&4\\
+705&(2023,1223)&5269&7116&7&4\\
+783&(2022,1224)&5268&7116&9&4.
\end{array}                                                       \tag{7.3}
\]

Packet `919` is all-rank support-monotone on either the source or the
`3836` prefix: it gains lower targets in ranks 5, 6, 7 and upper targets in
ranks 11, 12, loses none, lowers \(\Phi_3\) by two and removes four vertices
from the short-run support.  In contrast:

* `3836` destroys the last source witnesses for lower rank-5 target
  `0x08491` and upper rank-11 target `0x1b47d`;
* `705` does not repair either.  It additionally loses upper rank-11
  `0x16caf` and lower rank-6 targets
  `0x10827,0x10887,0x10c0b,0x10ca2`, and raises \(\Phi_3\) by two;
* `783` still repairs neither named `3836` debt.  It additionally loses
  upper rank-12 `0x1975f` and lower rank-6 `0x0170c`; it lowers
  \(\Phi_3\) by one but does not reduce the short-support vertex set.

Thus the final endpoint gains 27 all-rank targets but has nine source-target
losses.  Neither `3836` debt is discharged, \(\Phi_3\) is not monotone, and
short-support size is not monotone.  This is the exact reason the sparse
named deeper-debt and residence-collar coordinates in (4.1) cannot be
omitted.

The delete-first touched physical core is also genuinely
boundary-deficient.  On this literal undirected contraction-matching face,
one packet leaves two cycles; the `3836+919` touched core has ten paths and
cycle path counts `1,1,3,5`, while all four packets give eighteen touched
paths and counts `1,1,3,13`.  The corresponding minimum of four omitted
matching edges/eight exported ports is therefore a necessary interface
count only for this touched-core face.  Untouched source cycles remain, the
full endpoint factor has nine cycles, and these packet switches are not yet
ordered-four-transversal or directed Pascal atoms.  Directed
\(H\not\leadsto T\), complete physical opening, and transparent gluing all
remain unaudited.

The exact prefix audit is

```text
scratch/threadD_k17_four_packet_prefix_residence_deepflags_20260731.audit.json
```

with payload SHA-256
`912e9356507a8a517ac50f9d23dcb5dcb15fb85e0d591ff5c27b1ed0a53cf2a6`.

Reproduce the certificate with

```text
python3 scratch/threadD_audit_k17_commonext_four_packet_macro_20260731.py
python3 scratch/threadD_audit_k17_four_packet_prefix_residence_deepflags_20260731.py
```

The audit independently rebuilds the source factor, applies every prefix,
and for each occurrence graph and common core checks an explicit matching
and an equal-cardinality vertex cover.  Its frozen output is

```text
scratch/threadD_k17_commonext_four_packet_macro_20260731.audit.json
```

## 8. Sharp remaining boundary

This exact macro does **not** close K17.  It covers ten of 3,826 missing
lower-turn colours, ends with occurrence deficiency 4,121, and leaves nine
factor components.  Section 7.1 does audit the cyclic short-run and
all-rank interval ledgers—and shows nine source flags are lost—but it does
not produce a linear residence chronology.  Compiler compatibility,
primitive voltage, private socket transport, directed Pascal reachability,
and the other ordered-four-transversal rails remain uncertified.  Most
importantly, the augmented graph audited here is only the old
A-slot/lower-colour versus B-slot/upper-colour occurrence rail.  It is not
the ordered four-transversal of the authoritative reduction.

What is proved is the needed bridge: a nontrivial compound switch packet can
be ordered with strictly improving lower support and occurrence rank while
its *incremental* common-core debt stays bounded and exactly certified.
The next theorem must extend this bounded-live-debt ordering through enough
packets to reach an accepting endpoint, while jointly carrying the physical
reachability, fixed decoration, all-depth and residence/compiler states.
