# Lower-rainbow path extension: four matroids and the exact K17 Hall gate

Date: 2026-07-31  
Status: exact extension theorem; positive colour/protection-aware K17 provider
matching; its minimal forced-cut completion in the frozen source orientation
is rigorously impossible  
Scope: the lower-\(q_1\) and protected-provider layers.  Staircase deadlines,
the remaining upper witnesses, and the compiler are separate gates.

## 0. Verdict

Let \(F\) be a spanning lower-rainbow Johnson 2-factor on \(N\) owners, and
let \(P\) be prescribed directed provider arcs.  Exact coefficient-one
completion is neither an ordinary matching problem nor a two-matroid
intersection.  It is exactly a target-size common-independent-set problem
for four matroids.  If every matroid has rank at least \(N-1\)—otherwise
infeasibility is immediate—this is equivalently a common-base problem after
truncating all four matroids to rank \(N-1\):

1. at most one selected arc at each tail;
2. at most one selected arc at each head;
3. at most one selected arc of each lower colour; and
4. graphic acyclicity after forgetting orientations.

A common independent set of size \(N-1\) is automatically a directed
Hamilton path and automatically recycles every deleted factor colour except
one.  This is the dependency-clean extension theorem.

Distinct provider tails and heads certify only the first two gates.  The
first frozen K17 assignment has 103 forced colour repeats and cannot extend.
A new exact provider reselection does pass tail, head, colour, protection,
and prescribed-forest tests for all 1,838 deep holes.  However, if one cuts
only the 3,336 source edges forced by those providers, the residual
tail--colour and colour--head matchings have sizes only 926 and 892, against
the required 1,497.  Thus that *minimal cut closure* cannot be completed in
the frozen source orientation.  Within that orientation, additional ejection
cuts or a provider selection coupled to residual Hall are necessary; fragment
reorientation is a third global escape.  This is not a global K17 no-go.

## 1. The one-hole identity

Let the lower-colour palette be \(\mathcal C\), with

\[
                         |\mathcal C|=N,
\]

and suppose \(F\) uses every colour exactly once.  For any spanning directed
path \(Q\), let \(m_Q(c)\) be the number of its arcs of colour \(c\), and put

\[
 H(Q)=|\{c:m_Q(c)=0\}|,
 \qquad
 E(Q)=\sum_c(m_Q(c)-1)^+.
\]

Since \(Q\) has \(N-1\) edges,

\[
 \boxed{H(Q)-E(Q)
   =\sum_{c\in\mathcal C}(1-m_Q(c))=1.}            \tag{1.1}
\]

Thus the desired coefficient-one lower ledger is not merely \(H-E=1\); it
is the sharp case

\[
                         H=1,qquad E=0.             \tag{1.2}
\]

Here and below factor membership is **physical**, not oriented: project every
selected arc to its underlying undirected edge (the graphic matroid forbids
selecting both orientations).  Let \(D\) be the physical edges of \(F\) not used
by \(Q\), and let \(S\) be the selected physical edges outside \(F\).  Since \(F\)
is rainbow,

\[
 |D|=|S|+1.
\]

### Lemma 1.1 (automatic recycling)

The following are equivalent:

1. \(Q\) satisfies (1.2);
2. the seam colours are distinct and
   \(\chi(S)\subseteq\chi(D)\);
3. the seams use exactly all but one of the deleted factor colours.

#### Proof

If a seam has colour \(c\) while the unique factor edge of colour \(c\)
remains, then \(c\) is repeated.  Hence (1.2) implies
\(\chi(S)\subseteq\chi(D)\), and rainbowness makes \(\chi\) injective on
\(S\).  The cardinality equation then leaves exactly one colour of \(D\)
unused.  The converse is immediate. \(\square\)

In particular, if a prescribed set has \(p\) arcs but only \(d\) distinct
colours, then every completion retaining it has

\[
                    E\ge p-d,qquad H\ge p-d+1.     \tag{1.3}
\]

The unique boundary hole cannot pay for even one repeated seam colour.

## 2. The orientation-free four-matroid theorem

Let \(G\) be the allowed directed-arc catalogue.  It contains both
orientations of every factor edge and whichever directed Johnson seams are
admissible at the lower-\(q_1\) layer.  Opposite orientations of one physical
edge are distinct parallel elements.  On ground set \(G\), define:

* \(M_{\rm out}\): the partition matroid with capacity one at each tail;
* \(M_{\rm in}\): the partition matroid with capacity one at each head;
* \(M_{\rm col}\): the partition matroid with capacity one in each
  rank-\((r-1)\) colour class; and
* \(M_{\rm gr}\): the graphic matroid of the underlying undirected
  multigraph.

### Theorem 2.1 (provider-retaining rainbow path extension)

For a prescribed directed provider set \(P\subseteq G\), the following are
equivalent.

1. There is a spanning directed path \(Q\supseteq P\) using \(N-1\)
   pairwise-distinct lower colours.
2. The four matroids have a common independent set \(Q\supseteq P\) of
   cardinality \(N-1\).
3. \(P\) is independent in all four matroids and the four contractions
   \(M_i/P\) have a common independent set of size \(N-1-|P|\).

When these conditions hold, the components of the physical intersection
\(F\cap Q\), with their selected directions, are exactly the cuts and oriented
fragments; the selected physical edges outside \(F\) give their unique order.
Lemma 1.1 then proves exact colour recycling with one boundary hole.

#### Proof

A path as in (1) plainly satisfies all four independence conditions.
Conversely, graphic independence and \(N-1\) selected arcs on \(N\) vertices
give a spanning tree.  Tail and head capacities make its undirected maximum
degree at most two, so the tree is a path.  At an internal path vertex the
two incident arcs cannot both enter or both leave; hence the orientation is
consistent from one end to the other.  Colour independence gives \(N-1\)
distinct colours.  This proves (1)\(\Leftrightarrow\)(2).  The contraction
identity proves (2)\(\Leftrightarrow\)(3), and Lemma 1.1 gives the final
ledger statement. \(\square\)

The theorem removes cut and orientation choices as independent mysteries:
they are recovered from the target-size common independent set.  It does
**not** turn the problem
into ordinary matroid intersection.  Four-matroid target-size common
independence has no Edmonds two-matroid min--max theorem.

If a provider's advertised upper witness needs directed factor edges in a
protected suffix, prefix, or collar, include all those directed factor edges
in the prescribed set together with the provider seam.  Theorem 2.1 then
retains the witness whenever this enlarged set is common-independent.  When
the witness itself is still a choice, use the guarded variables (3.6); that
OR-of-spans layer is an additional side constraint, not a fifth matroid.

## 3. Exact fixed-orientation equations

For a computation in one oriented factor, write \(s(u)\) for the source
successor and

\[
                       \lambda(u)=u\cap s(u).
\]

The lower-rainbow property makes \(\lambda\) a bijection from source-edge
tails to colours.  For a seam \(a=(u,v)\), define

\[
 \alpha(a)=u,qquad
 \beta(a)=s^{-1}(v),qquad
 \gamma(a)=\lambda^{-1}(u\cap v).                  \tag{3.1}
\]

Let \(c_i\) say that source edge \(i\to s(i)\) is cut, \(x_a\) select a
seam, and \(t_i,h_i,z_i\) mark respectively the terminal cut, initial cut,
and omitted-colour cut.  The exact three ledgers are

\[
 \sum_{a:\alpha(a)=i}x_a=c_i-t_i,                 \tag{3.2}
\]

\[
 \sum_{a:\beta(a)=i}x_a=c_i-h_i,                  \tag{3.3}
\]

\[
 \sum_{a:\gamma(a)=i}x_a=c_i-z_i,                 \tag{3.4}
\]

with

\[
 t_i,h_i,z_i\le c_i,qquad
 \sum_i t_i=\sum_i h_i=\sum_i z_i=1.              \tag{3.5}
\]

Prescribed arcs have \(x_a=1\).  A protected witness \(w\) for a deep target
has a variable \(y_w\) with

\[
 y_w\le x_{a(w)},qquad
 y_w\le1-c_e\quad(e\in R(w)),qquad
 \sum_{w\in\mathcal W(Z)}y_w\ge1,                \tag{3.6}
\]

where \(R(w)\) is its complete suffix/prefix and run-collar edge set.

Equations (3.2)--(3.5) give one directed path plus possible directed cycles.
Requiring the graph consisting of uncut source edges and selected seams to
be acyclic is necessary and sufficient to remove those cycles.  Equivalently
one may use exact subtour cuts, or integer order variables on the physical
owners.  Thus (3.2)--(3.6) plus acyclicity are an exact fixed-orientation
form of Theorem 2.1 with protected witnesses.

This fixed-orientation model must not be misused as a one-bit orientation
choice per source cycle.  Once several edges of a cycle are cut, its
surviving fragments may be oriented independently.  Theorem 2.1 handles
that general case directly; alternatively the fragment-orientation states
must be enumerated explicitly.

## 4. Fixed cuts: three-dimensional matching plus connectivity

Fix a cut set \(K\), the fragment orientations, and the three boundary
omissions.  Deleting \(K\) produces \(|K|\) directed source segments, provided
every source cycle is cut.  Every candidate seam determines three slots:

1. its exit segment;
2. its entry segment; and
3. the unique cut edge carrying its lower colour.

After removing the terminal, initial, and hole slots, exact degree and
colour restitution are precisely a perfect matching in this three-partite,
three-uniform seam hypergraph.  The selected segment links must additionally
be independent in the graphic matroid.  With \(|K|-1\) links, graphic
independence makes them a spanning tree; the two degree partitions make it
a directed Hamilton path.

Hence fixed-cut completion is a target-size common-independent-set problem
for tail, head, colour, and graphic matroids.  Dropping connectivity still
leaves three partition matroids, i.e. a three-dimensional matching problem.
The *generic* three-partite incidence class admits the minor

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad |\det|=2,                                  \tag{4.1}
\]

by taking two columns sharing a tail row, two sharing a head row, and two
sharing a colour row.  This particular triangle is **not** physically
realizable by Johnson seams.  Indeed, if seams \(e_1,e_2\) share a tail \(T\),
\(e_1,e_3\) share a head \(H\), and \(e_2,e_3\) share a lower colour \(C\), then

\[
 C\subseteq T\cap H=\chi(e_1),
\]

and equality follows from their common rank, contradicting the required
zero in the colour row of \(e_1\).  Therefore (4.1) is only a warning about
the unrestricted three-index formulation; it is not a non-TU certificate
for the literal Johnson catalogue.  No physical determinant-two minor is
claimed here.

One useful necessary family follows from the four ranks.  For every
partition of the candidate ground set

\[
 A=A_T\mathbin{\dot\cup}A_H\mathbin{\dot\cup}
   A_C\mathbin{\dot\cup}A_G,
\]

a common independent set of size \(q\) requires

\[
 r_T(A_T)+r_H(A_H)+r_C(A_C)+r_G(A_G)\ge q.         \tag{4.2}
\]

For four matroids these inequalities are not sufficient in general.  A
proof which promotes (4.2), separate endpoint Hall, or a fractional point
to an integral path without another hypothesis is circular.

## 5. Two positive extension criteria

### Theorem 5.1 (exact coloured connectivity projection)

Suppose \(P\) is a prescribed rainbow undirected forest.  Contract its
components, delete its used colours, and retain every residual allowed
coloured edge.  Then \(P\) extends to a rainbow spanning tree if and only if,
for every partition \(\Pi\) of the contracted vertex set,

\[
 \boxed{
 |\{\text{unused colours on edges crossing }\Pi\}|
      \ge |\Pi|-1.}                                \tag{5.1}
\]

This is the graphic-matroid/colour-partition matroid-intersection theorem in
partition form.  It is the exact coloured Hall theorem for connectivity.
It is only necessary for a directed Hamilton path, because the tail and head
partition matroids remain.

### Theorem 5.2 (colour-rectangular degree extension)

Fix the fragments and boundary ports, leaving \(q\) exit ports and \(q\)
entry ports to be saturated.  For every available colour \(c\), suppose its
complete safe seam bank is a rectangle

\[
                         L_c\times R_c.             \tag{5.2}
\]

Delete the colours and exit/entry ports already occupied by prescribed
seams.  On the residual colour set \(C_0\), let \(M_L\) be the transversal matroid
whose independent colour sets can be injected into exit ports through the
banks \(L_c\); define \(M_R\) analogously for entry ports.  In this residual
problem, a rainbow degree-cover extension of size \(q\) exists if and only if

\[
 \max\{|I|:I\in M_L\cap M_R\}\ge q,                \tag{5.3}
\]

or equivalently

\[
 r_L(Z)+r_R(C_0\setminus Z)\ge q
       \qquad(Z\subseteq C_0).                      \tag{5.4}
\]

Given the two transversal matchings, rectangularity pairs the chosen exit
and entry for each colour.  This theorem is exact for the degree layer, not
for connectivity.

There is a noncircular sufficient connectivity certificate.  If selected
seams in two cyclic cover components, or in the distinguished path and one
cyclic component, can be crossed so that the two new seams retain their
respective colours and remain legal, the appropriate crossing preserves all
three partition ledgers and merges the cycle components (or absorbs the
cycle into the path).  A rooted tree of edge-disjoint certified crossings,
applied in its stated order, therefore absorbs every cycle into the
distinguished path while retaining all prescribed arcs.  This *protected
splice-tree* is a finite positive certificate.

When run safety or protected-span exclusions delete individual pairs inside
\(L_c\times R_c\), rectangularity fails and (5.4) is no longer an iff
criterion; the residual problem is genuine three-dimensional matching.

## 6. Sharp obstructions

### 6.1 Endpoint disjointness does not imply colour independence

Fix a rank-\((r-1)\) set \(C\) and four distinct points
\(a,b,d,e\notin C\).
The two Johnson arcs

\[
 C+a\longrightarrow C+b,qquad
 C+d\longrightarrow C+e                            \tag{6.1}
\]

have distinct tails and heads, but both have lower colour \(C\).  Retaining
both forces \(E\ge1\) and \(H\ge2\).

### 6.2 Rainbow degree feasibility does not imply a path

Two prescribed seams can saturate two cut segments in both directions and
form a directed 2-cycle.  Their tails, heads, and colours may all be
distinct.  They violate only the graphic matroid and cannot be repaired
without deleting a prescribed seam.

### 6.3 Independence in all four matroids need not extend

Let \(W\) be a rank-\(r\) owner and choose distinct \(a,b\notin W\).  For
every \(i\in W\), prescribe

\[
 (W\setminus\{i\})+a
   \longrightarrow
 (W\setminus\{i\})+b.                              \tag{6.2}
\]

These \(r\) arcs form a matching, have distinct colours \(W\setminus\{i\}\),
and are a forest.  Thus they are independent in all four matroids.  But they
consume every colour available on an edge incident with \(W\).  No further
rainbow edge can attach \(W\), so no spanning extension exists.  The
two-block partition \(\{\{W\},V\setminus\{W\}\}\) violates (5.1).

This physical Johnson-star example proves that even a prescribed common
independent set needs genuine extension ranks; independence alone is not an
absorption theorem.

## 7. Exact K17 diagnosis

The fixed source is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
SHA-256 3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e
```

It consists of 11 cycles on all 24,310 rank-nine owners.  Its 24,310 factor
edges use the entire rank-eight palette once, its upper-\(q_1\) palette is
complete, and it has 1,838 deeper holes, of ranks

\[
                         11^{1496}12^{329}13^{13}.   \tag{7.1}
\]

The independent replay recomputes all arbitrary-width cyclic unions from
the components, rather than trusting this census: it finds 39,388 witnessed
upper masks, all 19,448 rank-ten masks, and exactly the 1,838 holes in
(7.1).

### 7.1 The first endpoint assignment is unusable

The first simultaneous certificate assigns one individually run-(1/2)-safe
Johnson provider to every hole with 1,838 distinct tails and 1,838 distinct
heads.  Nevertheless its seam-colour histogram is

\[
                         1^{1634}2^{99}3^2.          \tag{7.2}
\]

It has only 1,735 distinct colours and therefore forces \(E\ge103\),
\(H\ge104\).  For example colour `05fa` occurs on both

```text
target 0fdfa: 085fa -> 00dfa
target 107fb: 005fb -> 105fa.
```

Its 1,838 arcs force 3,497 source cuts.  Only 684 of its selected distinct
seam colours are among those cut colours; the literal partial ledger is

\[
                         H=2813,\quad E=1154.       \tag{7.3}
\]

Moreover 762 local collars meet another forced cut, and only 1,075 targets
retain a fully protected advertised witness.  This freezes a literal K17
counterexample to “distinct tails and heads imply extendibility.”  It closes
only that saved assignment.

### 7.2 Colour/protection-aware provider reselection succeeds

The already-running H100 lane was strengthened by the colour partition,
the requirement that every selected seam colour have its source edge cut by
a selected endpoint, and simultaneous protected-span exclusions.  It
finished `OPTIMAL` in 52.51 seconds and selected all 1,838 providers.  An
independent replay proves:

* all targets, tails, heads, and seam colours are distinct;
* all 1,838 seam-colour source edges lie in the forced cut set;
* the 6,800 protected source-edge tails are disjoint from that cut set;
* all advertised suffix/prefix/collar witnesses replay literally; and
* the 1,838 provider seams together with all 6,800 directed protected factor
  edges form an 8,638-edge common-independent set in all four matroids.

Thus the target/tail/head/colour/protection selection gate is genuinely
positive.  The frozen result's free-text `scope` field is stale and says that
protected spans were not imposed.  Its authoritative Boolean fields
`matching_recycle_lower=true` and `matching_protected_spans=true`, together
with the independent replay, prove the selected-span exclusions.  They do
not prove preservation of every pre-existing arbitrary-upper witness, a
completed path cover, the staircase, or the compiler.

### 7.3 Its minimal forced-cut closure is impossible in the frozen orientation

Let \(A\) be the 1,838 provider tails and let
\(B=s^{-1}(\{\text{provider heads}\})\).  The exact overlap is 340, so the
minimal endpoint-forced cut set is

\[
 K=A\cup B,qquad |K|=3336.                         \tag{7.4}
\]

The prescribed seams use 1,838 distinct colours, all sourced in \(K\).  The
partial lower ledger is therefore

\[
                         H=1498,qquad E=0.          \tag{7.5}
\]

On the 3,336 cut segments in the frozen source orientation, the provider
arcs form 1,498 directed paths and
no quotient cycle.  However one separate original three-vertex source cycle
receives no cut at all, already requiring an additional cut.

Even if connectivity and every safety filter are discarded, the fixed set
\(K\) fails the residual degree/colour Hall gate.  There remain 1,498 exit
slots, 1,498 entry slots, and 1,498 unused cut colours; exactly 1,497 return
seams are required.  In the **full Johnson graph**, the tail--colour
projection has only 1,414 incidences and maximum matching 926, while the
colour--head projection has only 1,399 incidences and maximum matching 892.
Its zero-row counts are

\[
\begin{array}{c|r}
\text{tail with no remaining colour}&465\\
\text{colour with no remaining tail}&464\\
\text{colour with no remaining head}&478\\
\text{head with no remaining colour}&494.
\end{array}                                         \tag{7.6}
\]

Since local safety can only delete these incidences, no ordering or subtour
choice can complete this minimal \(K\) **while retaining that frozen source
orientation**.  This is a strict fixed-cut, fixed-orientation theorem.  It
already has a literal Hall witness: 465 residual exits have no admissible
remaining colour, whereas only one exit may be the terminal boundary; the
maximum-matching computations sharpen this from 1,033 to 926 usable
tail--colour pairs (and to 892 on the colour--head side).  The theorem
does not exclude reversing surviving factor fragments, enlarging \(K\), or
reselecting providers.  A new cut simultaneously creates an exit, an entry,
and a recyclable colour, which is exactly the ejection-chain closure absent
from the provider-only matching.

## 8. The surviving uniform gate

The strongest exact next statement is now:

> Select providers and an enlarged cut closure simultaneously so that the
> protected rows survive, the three exact ledgers (3.2)--(3.4) hold, the
> coloured partition cuts (5.1) and tail/head ranks pass, and the selected
> common independent set reaches size \(N-1\).

For K17, this means adding cut/ejection variables to the positive 1,838-row
provider model, not merely solving another endpoint matching.  For all \(k\),
the missing induction lemma is a protected four-matroid target-size
extension theorem with enough physical Johnson-star expansion to defeat the
obstruction (6.2).  No such uniform theorem is proved here, and no all-\(k\)
claim is made.

## 9. Reproducible artifacts

First endpoint assignment and its independent nonextension audit:

```text
scratch/k17_fragment_endpoint_matching_20260731.result.json
  SHA-256 4edd549b5e12d398223b1b8ae0fbb6d49ac161238389cc969d7e1285e395d6d7
scratch/threadD_audit_k17_fragment_endpoint_colour_closure_20260731.py
  SHA-256 d69fb241892894cb4acfd701239b5b215b1d2234f852f7a038186bf2d7796376
scratch/threadD_k17_fragment_endpoint_colour_closure_20260731.audit.json
  SHA-256 c8bdaf7585158e1a34be471700755d0c6d63b2243c7294632071f146df44170e
  payload 86e6310af4eb59be81fc96899cb1dcec57843a02a1e6cfeafeb4079164258172
```

Colour/protection-aware matching and fixed-minimal-cut audit:

```text
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/producer.py
  SHA-256 0cb6c05fb71284e4805aca31ca52527c04e3880654939d8070bfce7e2479feaa
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/producer.result.json
  SHA-256 3db9e5fc4a6bd9ab467e895de70a75c60376fff016661b6a18ec006900ab5d8a
  payload 7871e3bc87c519089136e0e4ee3668ffcebbac6d83796edc150beeba41c14169
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/producer.run.log
  SHA-256 c8ebffb8703592057dc0d23061a491594bbcb1401deefbd0fc4a6b0a879361a5
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/producer.preflight.json
  SHA-256 45f5b236e07fecf6d3d02b89a173a9f8ebbe0de8738d51ff3687a53f59e66fe0
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/METADATA_CORRECTION.md
  corrects only the frozen result's stale free-text scope; the result bytes
  remain unchanged
  SHA-256 c15f3ed2a238fc52a9795d97e15570d06990b4501db45bcc1e64aa60f66f49c5
scratch/threadD_audit_k17_recycle_protected_extension_gate_20260731.py
  SHA-256 91bff072d9a8b1d387a5b7b6d121ac6583f3d3f7c2d6a4f1751055e8a8306c12
scratch/threadD_k17_endpoint_matching_recycle_protected_20260731/independent.audit.json
  SHA-256 a21708146e26d9c88a6a42b8b35fe9c91c75eba7e61799242a44bdae71c335c8
  payload f057331d421005c886b8c2eca3a48c448805194f5b98d70ef1ae70ff4b4341a0
```

The two independent audits run locally in under one second each and remain
below 60 MB maximum resident memory.  No second heavy provider search was
launched.
