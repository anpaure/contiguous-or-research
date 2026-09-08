# The k15 quota-first rainbow forest: exact split, four-matroid boundary, and off-bank gate

Date: 2026-07-29

Status: theorem-level audit and strict reduction.  The numerical
\(335+94\) split is exact.  The relative path-forest completion theorem is
exact after a forest has been fixed.  A full rainbow forest is not
constructed.  This note proves why ordinary matroid intersection and all
separate Hall marginals do not prove it, constructs an acyclic
Hall-extendible rainbow bank from the saved \(426+3\) factor, and isolates
the first two exact physical obstructions: its forced length-two component
and a sixteen-provider off-bank residence toll.

All arguments are mathematical or use counts already independently audited
in the cited frozen notes.  No search or solver is used here.

## 1. Parameters and the fixed-first-matching chart

Let

\[
 k=15,\qquad r=8,\qquad
 W=\binom{15}{8}=6435,\qquad N=W/15=429.
\tag{1.1}
\]

The cyclic action is free on ranks seven and eight, because a nontrivial
period on \(\mathbb Z_{15}\) has cycles of length three, five, or fifteen,
whereas neither seven nor eight is divisible by three or five.  Thus each
of the lower and middle quotient shores has \(429\) vertices.

For rank nine, Burnside gives

\[
\left|\binom{\mathbb Z_{15}}9/C_{15}\right|
 =\frac{\binom{15}9+2\binom53}{15}=335.
\tag{1.2}
\]

Indeed, only the two rotations of order three fix rank-nine sets; each
fixes \(\binom53=10\) of them.  Consequently the \(335\) upper colours
consist of \(333\) free orbits and two orbits of size five.

Fix a phase-labelled perfect matching \(P\) from the rank-seven shore to
the rank-eight shore and write \(X_R=P(R)\).  Every residual incidence from
\(R\) distinct from its selected incidence \(R X_R\), with phase-labelled
parallel incidences retained, becomes a directed owner arc

\[
 a:X_R\longrightarrow Y.
\tag{1.3}
\]

It has upper colour \(\upsilon(a)=[X_R\cup Y]\), transported deletion and
insertion ports, and voltage \(\omega(a)\in\mathbb Z_{15}\).  The residual
bipartite multigraph is seven-regular on both shores.  The phase-labelled
incidences are distinct, but \(Y\) may equal \(X_R\) as an unphased quotient
vertex; such an arc is a quotient loop and is dependent in
\(\mathcal M_{\rm gr}\).

## 2. The exact four-matroid formulation

Let \(\mathcal A\) be the phase-labelled residual arc set.  On this same
ground set define:

1. \(\mathcal M_{\rm out}\), the partition matroid with capacity one for
   every tail;
2. \(\mathcal M_{\rm in}\), the partition matroid with capacity one for
   every head;
3. \(\mathcal M_{\rm col}\), the partition matroid with capacity one for
   every upper colour;
4. \(\mathcal M_{\rm gr}\), the graphic cycle matroid of the underlying
   undirected owner multigraph.

Loops are dependent in \(\mathcal M_{\rm gr}\), and phase-labelled parallel
arcs are retained; two parallel undirected edges form a graphic circuit.

### Theorem 2.1 (four-matroid rainbow-forest characterization)

A set \(M\subseteq\mathcal A\) of size \(335\) is an upper-rainbow directed
path forest if and only if it is independent in all four matroids above.
In that event it has exactly

\[
429-335=94
\tag{2.1}
\]

directed path components, counting isolated vertices.

#### Proof

Independence in the two shore partition matroids says that every vertex has
outdegree at most one and indegree at most one.  Graphic independence
excludes undirected cycles and loops.  Every nontrivial component is
therefore an undirected path.  Its orientation is consistent: an internal
sink would have indegree two and an internal source would have outdegree
two.  Thus every component is a directed path.

Colour independence and \(|M|=335\), the number of upper colours, say that
every colour occurs exactly once.  Conversely every upper-rainbow directed
path forest plainly satisfies the four independence conditions.  Finally a
forest on \(429\) vertices with \(335\) edges has \(429-335=94\)
components.  \(\square\)

This is four-matroid intersection, not ordinary two-matroid intersection.
Moreover the condition that every component have at least three arcs is
not hereditary, and hence is not itself a matroid independence condition.
The transported residence constraints are forbidden path windows of sizes
two, three, and four; they need not satisfy circuit elimination either.

### Proposition 2.2 (smallest C4-free rainbow obstruction)

Let the directed support be the three-edge path

\[
 b:r\longrightarrow q,\qquad
 a:p\longrightarrow q,\qquad
 c:p\longrightarrow s
\tag{2.2}
\]

on four distinct vertices.

First colour \(a,b,c\) by \(A,B,C\), respectively.  The colour family
\(\{A\}\) is realizable, and \(\{B,C\}\) is realizable by \(\{b,c\}\), but
neither \(\{A,B\}\) nor \(\{A,C\}\) is realizable.  Thus the hereditary
system of simultaneously matchable colour sets violates augmentation.
Its projected rank also violates submodularity:

\[
\rho(AB)=\rho(AC)=\rho(A)=1,\qquad \rho(ABC)=2,
\]

so

\[
\rho(AB)+\rho(AC)=2<3=\rho(ABC)+\rho(A).
\tag{2.3}
\]

If instead both arms \(b,c\) have colour \(B\) and the centre \(a\) has
colour \(A\), then

\[
\nu(E(S))\ge |S|\qquad(S\subseteq\{A,B\}),
\tag{2.4}
\]

but no rainbow \(A,B\)-matching exists: the only two-edge matching is
\(\{b,c\}\), which is monochromatic.

#### Proof

Every assertion follows by listing the three possible one-edge matchings
and the unique two-edge matching \(\{b,c\}\).  The support is a tree, so the
failure does not use a four-cycle or any graphic-cycle obstruction.
It is edge-minimal for (2.4): with at most two provider edges, the
two-colour inequality for \(S=\{A,B\}\) forces two disjoint edges, and the
singleton inequalities force both colours to occur, so those two edges are
already a rainbow matching.
\(\square\)

Thus even the most obvious matching-rank Hall inequalities do not capture
the joint tail-head-colour choice.  Ordinary matroid parity handles the
uncoloured tail-head pair.  Adding a colour token makes each arc a
three-object block, and adding graphic acyclicity makes the natural
encoding a four-object problem; standard two-element matroid parity does
not apply.

### Proposition 2.3 (extendibility is not a matroid)

For a bipartite graph \(G\), let

\[
\mathcal E(G)=\{I:I\text{ is contained in a perfect matching of }G\}.
\]

Even when \(G\) is a six-cycle, \(\mathcal E(G)\) need not be a matroid.

#### Proof

Write the two perfect matchings of the six-cycle as

\[
Q_0=\{l_1r_1,l_2r_2,l_3r_3\},\qquad
Q_1=\{l_1r_2,l_2r_3,l_3r_1\}.
\]

Let

\[
I=\{l_1r_1\},\qquad J=\{l_1r_2,l_3r_1\}.
\]

The sets \(I,J\) extend to \(Q_0,Q_1\), respectively.  Neither edge of
\(J\) can augment \(I\), because one shares \(l_1\) and the other shares
\(r_1\).  Exchange fails.  \(\square\)

Consequently the residual \(94\)-edge completion cannot be incorporated as
one further matroid in Theorem 2.1.

## 3. All ordinary colour-family marginals pass

The preceding obstruction is genuinely joint.  It is not caused by a
deficient union of provider rows in the unpruned physical quotient.

### Theorem 3.1 (provider-family matching lower bound)

Let \(\mathcal S\) contain \(f\) free upper orbits and
\(s\in\{0,1,2\}\) short upper orbits.  In the unpruned seven-regular
residual graph,

\[
|E(\mathcal S)|=9f+3s,\qquad \Delta(E(\mathcal S))\le7.
\tag{3.1}
\]

Hence

\[
\nu(E(\mathcal S))
\ge \left\lceil\frac{9f+3s}{7}\right\rceil
\ge f+s,
\tag{3.2}
\]

apart from the formal case \(f=0,s=2\).  That case also has matching number
at least two.  Therefore every colour-family matching-rank inequality, and
in particular each separate colour-to-tail and colour-to-head Hall
inequality, holds.

#### Proof

Every free upper orbit has nine phase-labelled provider arc orbits.  A
short upper orbit has three, each representing the stabilizer orbit of
three literal providers.  This proves the edge count.  The residual graph
has maximum degree seven.  By bipartite edge colouring, its edges split
into at most seven matchings, so the largest matching has size at least the
first term in (3.2).

For \(s\le2\), elementary arithmetic gives the second inequality except at
\((f,s)=(0,2)\).  Consider the two short colours there.  No provider of one
can share a tail with a provider of the other.  Otherwise, after phase
normalization, two distinct \(+5\)-invariant rank-nine sets would share a
rank-eight facet \(X\).  Their intersection would be exactly \(X\), making
\(X\) \(+5\)-invariant, impossible because its size eight is not divisible
by three.  The same argument applies to heads.  Thus any provider of one
short colour is shore-disjoint from any provider of the other, and a
two-edge matching exists.

The tail-neighbour and head-neighbour Hall inequalities also follow
directly from (3.1), since each such vertex meets at most seven provider
edges; the same short-pair argument handles the exception.  \(\square\)

Theorem 3.1 proves that no compression based only on provider-family size,
matching number, or separate shore expansion can settle the rainbow
selection.  Proposition 2.2 identifies the missing three-way correlation.

## 4. What the 335 plus 94 split does and does not prove

### Theorem 4.1 (exact rainbow-Hall split)

Let \(A\subseteq\mathcal A\) be any allowed residual support.  A perfect
matching \(Q\subseteq A\) covering every upper colour exists if and only if
there is a \(335\)-edge partial matching \(M\subseteq A\) such that:

1. \(M\) contains one edge of every upper colour;
2. its tails are distinct on the outgoing shore and its heads are distinct
   on the incoming shore; and
3. after deleting those \(335\) outgoing vertices and those \(335\)
   incoming vertices, the residual \(94\) by \(94\) graph has a perfect
   matching.

#### Proof

From a covering perfect matching choose one provider of every colour.  The
remaining \(94\) edges give the residual completion.  Conversely append a
residual perfect matching to \(M\).  \(\square\)

Thus \(335+94\) is both exact and sufficient for static upper coverage.
It does not by itself imply acyclicity, minimum path length, residence,
one-cycle topology, or unit voltage.

### Theorem 4.2 (exact completion relative to a safe forest)

Let \(M\) be an upper-rainbow path forest with \(94\) components, every
component having at least three arcs.  Assume every transported
depth-three residence comparison internal to a component is safe.

Make a phase-labelled directed connector multigraph \(K_M\) on the
components.  A port from the terminal of \(C\) to the initial of \(D\),
with \(C\ne D\), is retained precisely when every residence comparison
whose arc interval crosses that seam is safe.  Parallel ports are retained.
Then a completion containing \(M\) is an eligible parent if and only if its
\(94\) connectors:

1. form a perfect matching between component terminals and initials;
2. induce one directed \(94\)-cycle on the components; and
3. have unit total voltage after the fixed internal path voltages are
   included.

#### Proof

The unused outgoing vertices are exactly the component terminals and the
unused incoming vertices are exactly the component initials.  A perfect
matching between them completes every owner degree.  Its component
permutation is one cycle exactly when the completed owner permutation is
one \(429\)-cycle.

Because every path has at least three arcs, two connectors are never at
arc-distance at most three.  Hence every new depth-three comparison is
localized at one seam and is exactly one of the tests used to define
\(K_M\).  Upper completeness is already protected by \(M\), and unit
voltage is precisely the condition for the quotient cycle to lift to one
physical cycle.  All implications reverse.  \(\square\)

For one seam with terminal-side arcs

\[
\ldots,c_{L-2},c_{L-1},c_L
\]

and initial-side arcs

\[
d_1,d_2,d_3,\ldots,
\]

there are exactly nine arc pairs to test:

\[
\begin{split}
&\text{connector against the previous three and next three arcs},\\
&(c_L,d_1),\quad(c_L,d_2),\quad(c_{L-1},d_1).
\end{split}
\tag{4.1}
\]

Each pair has the two directed port inequalities, so this is an exact
eighteen-inequality collar.  The length-three hypothesis is sharp for this
one-seam localization.  A length-two component puts its two adjacent
connectors at distance three and requires a joint two-connector test.

The path-length ledger is

\[
\sum_{i=1}^{94}(L_i-3)=335-3\cdot94=53.
\tag{4.2}
\]

In particular at least \(41\) paths have length exactly three.

### Corollary 4.3 (one-back Hall is exact after support pruning)

Relative to a fixed \(M\), an eligible connector cycle exists if and only
if there are:

1. a total order of the \(94\) components;
2. one forced connector \(b\), from the maximum component to the minimum;
3. a pruned safe connector support in which every other connector is
   strictly increasing and self-connectors are absent;
4. a unit \(u\in\mathbb Z_{15}\) and a potential
   \(h:V(K_M)\to\mathbb Z_{15}\) such that
   \[
   v_M(C)+\omega(a)
    =h(D)-h(C)+u\,1_{\{a=b\}}
   \tag{4.3}
   \]
   for every retained connector \(a:C\to D\); and
5. Hall's inequalities in the \(93\) by \(93\) graph obtained by deleting
   the tail of \(b\) only on the outgoing shore and the head of \(b\) only
   on the incoming shore.

#### Proof

For sufficiency, Hall gives the other \(93\) connectors.  Every directed
cycle in their component permutation needs a descending edge.  Only the
cycle containing \(b\) has one, so there is exactly one cycle.  Summing
(4.3) around it telescopes the potential and leaves the unit \(u\).

For necessity, order the components along an eligible connector cycle,
take its closing edge as \(b\), prune the support to the cycle itself, and
define \(h\) by prefix voltage sums.  The residual selected edges witness
Hall.  \(\square\)

This equivalence is relative to a fixed forest and permits support pruning.
It does not manufacture that forest.

## 5. The saved 426 plus 3 factor closes the static part

Let \(Q_0\) be the saved upper-complete second matching whose quotient
components have lengths \(426\) and \(3\).  The audited upper-colour loads
of the three small-component edges are \(1,1,3\).  The load-three colour
also has providers on the large component.

### Theorem 5.1 (old-bank acyclic rainbow completion)

There is a \(335\)-edge upper-rainbow acyclic partial matching
\(M_0\subset Q_0\), and \(Q_0\setminus M_0\) is its exact \(94\)-edge
perfect-matching completion.

#### Proof

For each upper colour choose one \(Q_0\)-provider.  For the load-three
colour on the small component choose a provider on the large component.
The two load-one small-component edges are forced, while the third small
edge is omitted.  Thus \(M_0\) uses two small edges and \(333\) large
edges.

Exactly one edge of the three-cycle and \(93\) edges of the \(426\)-cycle
are omitted.  Each old cycle is therefore broken, so \(M_0\) is a directed
path forest.  Since it is a subset of the perfect matching \(Q_0\), the
omitted \(94\) edges complete it.  \(\square\)

This proves, on the actual saved carrier, simultaneous rainbow choice,
shore injectivity, acyclicity, and residual Hall extendibility.  The
remaining difficulty is geometric.

### Proposition 5.2 (old-bank minimum-length obstruction)

No upper-rainbow subset of \(Q_0\) can be both acyclic and have every path
of length at least three.

#### Proof

Both load-one colours of the small component have unique old-bank
providers, so both corresponding consecutive edges must be selected.  If
the third small edge is also selected, the three-cycle survives.  If it is
not selected, the two forced edges form a path of length two.  \(\square\)

Thus at least one off-\(Q_0\) provider is necessary even before the full
residence audit.

### Proposition 5.3 (sixteen-provider residence toll)

Let \(M\) be any upper-rainbow forest in the same fixed-\(P\) residual
graph, and measure its selected arcs relative to the saved bank \(Q_0\).
If \(M\) is internally safe on all depth-three residence windows, then

\[
|M\setminus Q_0|\ge16.
\tag{5.1}
\]

#### Proof

The independently audited collar certificate in
THREAD_A_K15_426_PLUS_3_MULTISPIRAL_ELIGIBILITY_AND_DENSE_TRADE_OBSTRUCTION_20260729.md
contains eighteen bad quotient collars all of whose possible old cut edges
have globally singleton old-bank upper colours.  Their exact transversal
number is sixteen.

An internally safe forest must omit an old edge in every such collar;
otherwise that entire forbidden window remains internal to one forest
path.  At least sixteen singleton old providers are therefore omitted.
Each lost colour must be represented by an off-\(Q_0\) arc in the rainbow
bank.  \(\square\)

The number sixteen is sharp for the collar-hitting projection.  No
sixteen-arc physical completion is asserted.

## 6. Exact spacing cuts for any fixed covered cycle

The obstruction in Proposition 5.2 has a general interval form.

Let \(Q\) be a directed cycle covering every upper colour.  For each colour
\(U\), let \(E_U\) be its occurrence positions in \(Q\), with
\(|E_U|=l_U\).  Suppose \(M=Q\setminus D\) contains exactly one occurrence
of every colour.

### Theorem 6.1 (quota-spacing normal form)

The following hold.

1. Exact colour quotas are equivalent to
   \[
   |D\cap E_U|=l_U-1\qquad(U\in\mathcal U).
   \tag{6.1}
   \]
2. Every component of \(M\) has at least three arcs if and only if \(D\)
   is a stable set of the third power \(C_{429}^3\).
3. Internal depth-three safety requires \(D\) to meet every unsafe
   radius-three arc window of \(Q\).
4. For every set \(I\) of cycle positions, the necessary cut
   \[
   \sum_U\max(0,|E_U\cap I|-1)
      \le \alpha(C_{429}^3[I])
   \tag{6.2}
   \]
   holds.

#### Proof

Statement 1 is immediate.  Between two consecutive omitted cycle arcs, the
retained component length is at least three exactly when the omitted
positions have cyclic distance at least four, which is statement 2.
Statement 3 is the definition of an internal forbidden window.

For a fixed colour, at most \(l_U-|E_U\cap I|\) required omissions can lie
outside \(I\).  Hence at least
\(\max(0,|E_U\cap I|-1)\) omissions of that colour lie in \(I\).
Summing gives a lower bound on \(|D\cap I|\).  By statement 2 this is a
stable set in \(C_{429}^3[I]\), proving (6.2).  \(\square\)

If \(I\) is a proper interval of \(m\) positions and its complementary gap
has at least three positions, then

\[
\alpha(C_{429}^3[I])=\left\lceil\frac m4\right\rceil.
\tag{6.3}
\]

The smallest abstract failure is four consecutive positions coloured
\(A,A,B,B\).  The left side of (6.2) is two and the right side is one.
This is an exact statewise obstruction to any attempt to obtain the forest
merely by thinning one fixed covered cycle.

## 7. The canonical raw PBBS bank has a forced loop

The preceding saved \(Q_0\) is not the unmodified canonical PBBS second
matching.  The most direct necklace rule for that raw matching fails even
earlier.

Let \(f\) be the canonical PBBS permutation on rank-seven subsets of
\(\mathbb Z_{15}\), and put

\[
M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c.
\tag{7.1}
\]

Fix \(P=M_+\) and try to choose the rainbow bank only from \(M_-\).

### Theorem 7.1 (forced interval-colour quotient loop)

Put

\[
S=\{0,1,\ldots,5\},\quad
A_-=S\cup\{6\},\quad
B=\{7,8,\ldots,13\},\quad
A_+=S\cup\{14\}.
\tag{7.2}
\]

The raw \(M_-\)-arc at lower owner \(B\) is the quotient loop

\[
\{6,\ldots,13\}\longrightarrow\{7,\ldots,14\},
\tag{7.3}
\]

and its upper colour is the free orbit of
\(U=S^c=\{6,\ldots,14\}\).  It is the unique \(M_-\)-provider of that
colour.  Hence every one-provider-per-colour subset of the raw \(M_-\)
bank contains a loop and is not a forest.

#### Proof

Direct evaluation of the nested PBBS successor rule gives

\[
f(A_-)=B,\qquad f(B)=A_+.
\tag{7.4}
\]

Therefore

\[
M_+(B)=A_+^c=\{6,\ldots,13\},\qquad
M_-(B)=A_-^c=\{7,\ldots,14\}.
\]

The two endpoints differ by cyclic shift \(+1\), so they are the same
quotient vertex; their union is \(S^c\).

For completeness, the audited PBBS first-shadow multiplicity formula for
a rank-six set \(S\) is

\[
\mu(S)=|\operatorname{Fix}(\beta_S\circ\alpha_S)|,
\tag{7.5}
\]

where \(\alpha_S,\beta_S\) are the forward and reverse survivor maps on
admissible one-point extensions.  Here their domains are

\[
U_+(S)=\{12,13,14\},\qquad U_-(S)=\{6,7,8\},
\]

and the same nested-rule evaluation gives

\[
\alpha_S(6)=\alpha_S(7)=\alpha_S(8)=14,\qquad
\beta_S(14)=6.
\tag{7.6}
\]

Thus the fixed-point set is \(\{6\}\) and \(\mu(S)=1\).  Since the orbit of
\(S\) is free, this is also the quotient provider multiplicity.  The
displayed loop is forced.  \(\square\)

Every free upper colour has nine residual providers, so Theorem 7.1 does
not obstruct the full residual graph: the forced raw provider may be
replaced by one of its eight off-\(M_-\) providers.  It refutes only the
canonical rule that chooses all representatives from the raw second PBBS
matching.

## 8. Phase is a connector obstruction, not a forest obstruction

Every voltage assignment on a forest is a coboundary.  Choose an arbitrary
phase at one root of each component and propagate it along the unique
paths; all internal arc voltages can then be gauged to zero.  The
gauge-invariant voltage is carried only by the final connector cycle.

Conversely, phase can kill every connector completion.  If all effective
connector weights in \(K_M\) are a coboundary modulo three, or all are a
coboundary modulo five, then every connector cycle has total voltage zero
in that modulus and cannot be a unit modulo fifteen.  This is a distinct
cut after rainbow selection and residence pruning.

For either size-five upper colour, an internally zero-resident final
matching can select exactly one quotient provider.  One such provider gives
literal load three, while two give load six, exceeding the load-four bound
forced by zero-residence.  Its two missing labels must also be distinct
modulo five; otherwise the three rotated literal provider pairs share
facets.  These are hard finite rows, but Theorem 3.1 shows that they are not
ordinary shore-Hall obstructions.

## 9. Precise proved and unproved boundary

The following statements are unconditional.

1. The \(335+94\) count and Theorem 4.1 are exact and sufficient for static
   upper coverage.
2. Relative to a fixed internally safe minimum-length-three forest,
   Theorem 4.2 and Corollary 4.3 are exact, including all collars, topology,
   and voltage.
3. The rainbow-forest selection is a four-matroid intersection with
   nonmatroidal spacing, residence, and extendibility constraints.
4. All ordinary provider-family matching-rank and separate shore Hall
   inequalities pass in the actual unpruned seven-regular quotient.
5. The saved \(426+3\) factor already supplies an acyclic,
   Hall-extendible, upper-rainbow bank, but its small component forces a
   length-two path.
6. Internal residence forces at least sixteen off-\(Q_0\) providers.
7. Restriction to the raw canonical second PBBS matching is impossible
   because one free upper colour forces a quotient loop.

The smallest remaining positive lemma in this architecture is therefore:

> **OFF16 rainbow-forest lemma.**  In the fixed-\(P\) residual port
> multigraph there is a \(335\)-arc set \(M\) which is independent in
> \(\mathcal M_{\rm out},\mathcal M_{\rm in},\mathcal M_{\rm col}\), and
> \(\mathcal M_{\rm gr}\); whose \(94\) paths all have length at least three
> and are internally depth-three biresident; which necessarily uses at
> least sixteen arcs outside the saved \(Q_0\); and whose exact
> eighteen-inequality connector multigraph satisfies the one-back
> \(93\) by \(93\) Hall and unit-voltage conditions of Corollary 4.3.

This lemma would prove the desired eligible \(k=15\) parent and feed the
already-proved two-parent flag-stabilizer consumer.  It is not proved here.
No physical cut refuting it is known.

The sharp obstruction is not a missing scalar count: it is the joint
integral choice of colours, two shores, forest spacing, transported
residence, residual Hall, and non-coboundary connector voltage.  The
three-edge path in Proposition 2.2 is the smallest abstract witness that
all natural marginal Hall tests can pass while the first three of those
requirements already fail jointly.
