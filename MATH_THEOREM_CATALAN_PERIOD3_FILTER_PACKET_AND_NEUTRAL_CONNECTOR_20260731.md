# Period-three filters admit canonical paired physical packets

Date: 2026-07-31  
Status: solver-free local packet construction, an exact absorbed
path-forest extension criterion, and two sufficient unit-voltage closure
normal forms; the global forest extension and connector selection remain
finite gates

## 1. Parameters and the smaller necklace graph

Put

\[
 q=6a+3=3n,\qquad n=2a+1,\qquad m=3a+2,
\]

and identify the finite coordinates with \(\mathbb Z_q\).  Let
\(K_3=\{0,n,2n\}\), let

\[
 \pi:\mathbb Z_q\longrightarrow\mathbb Z_n
\]

be reduction modulo \(n\), and write \(C_b=\pi^{-1}(b)\).  As in
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`, the exceptional
outer colours are

\[
 L_A=\{\infty\}\cup\pi^{-1}(A),\quad |A|=a,
 \qquad
 U_B=\pi^{-1}(B),\quad |B|=a+1.                 \tag{1.1}
\]

Let \(I_a\) be the bipartite multigraph whose left vertices are translation
orbits of \(a\)-sets in \(\mathbb Z_n\), whose right vertices are translation
orbits of \((a+1)\)-sets, and whose edges are translation orbits of flags
\(A\subset B\).

### Lemma 1 (solver-free necklace pairing)

The graph \(I_a\) is an \((a+1)\)-regular balanced bipartite multigraph on
\(\operatorname{Cat}_a\) vertices on each shore.  In particular it has a
perfect matching.

#### Proof

Translation acts freely on both shores: an \(a\)-set or \((a+1)\)-set fixed
by a nonidentity translation would be a union of cycles of a divisor of
\(n=2a+1\), whereas

\[
 \gcd(a,n)=\gcd(a+1,n)=1.
\]

A flag stabilizer is contained in the stabilizer of its lower member, so
flags are free as well.  Before quotienting, every \(a\)-set has \(a+1\)
extensions and every \((a+1)\)-set has \(a+1\) lower neighbours.  Freeness
preserves these degrees in the orbit multigraph.  The two shores have

\[
 \frac1n\binom na=\frac1n\binom n{a+1}=\operatorname{Cat}_a
\]

vertices.  A regular balanced bipartite multigraph satisfies Hall's
condition and has a perfect matching. \(\square\)

The pairing in Lemma 1 is by an inclusion flag.  Relabelling the upper bank
by complementation is useful for counting, but complement partners do not
give the local Johnson adjacency used below.

Equivalently, put \(C=\mathbb Z_n\setminus B\).  The two shores of \(I_a\)
are then two copies of the \(a\)-set necklaces, and an edge is

\[
 A\cap C=\varnothing,
 \qquad \mathbb Z_n\setminus(A\cup C)=\{b\}.             \tag{1.2}
\]

Thus Lemma 1 supplies a **complement zipper**: it pairs every lower necklace
\([A]\) with one upper-complement necklace \([C]\), with a unique gap
coordinate \(b\).  The zipper condition is disjointness, not the identity
pairing \(C=A\).

This does not create a direct middle-level complement seam.  For every
rank-\(m\) set \(X\subset[2m]\),

\[
 |X\mathbin{\triangle}X^c|=2m,\qquad d_J(X,X^c)=m.     \tag{1.3}
\]

Hence \(X\) and \(X^c\) are never Johnson adjacent for \(m\ge2\).
Reverse-complement symmetry may cancel voltages only after literal seams
have been found; it cannot supply the two hinges of a zipper by itself.
The physical zipper below instead uses the one-coordinate gap \(b\).

## 2. A literal paired-filter packet

Fix a matched physical flag

\[
 A\subset B=A\cup\{b\}.
\]

Write \(T=\pi^{-1}(A)\), and order the three elements of
\(C_b\) as \((c_i,c_j,c_k)\).  Define rank-\(m\) middle vertices

\[
 X_r=\{\infty\}\cup T\cup\{c_r\},
 \qquad
 Y_r=T\cup(C_b\setminus\{c_r\}).                       \tag{2.1}
\]

### Lemma 2 (the filter square)

The four middle vertices

\[
 X_i,X_j,Y_i,Y_j
\]

form the literal Johnson four-cycle

\[
 X_i-X_j-Y_i-Y_j-X_i.                                  \tag{2.2}
\]

Deleting its last edge leaves the path

\[
 R(A,b;i,j,k):=X_i-X_j-Y_i-Y_j.                         \tag{2.3}
\]

Its three edges have lower colours

\[
 \{\infty\}\cup T,qquad T\cup\{c_j\},qquad
 T\cup\{c_k\},                                        \tag{2.4}
\]

and upper colours

\[
 \{\infty\}\cup T\cup\{c_i,c_j\},\qquad
 \{\infty\}\cup T\cup\{c_j,c_k\},\qquad
 T\cup C_b.                                            \tag{2.5}
\]

Thus (2.3) contains exactly one edge with exceptional lower colour \(L_A\),
exactly one edge with exceptional upper colour \(U_B\), and one ordinary
edge joining the two.  The omitted cross edge \(Y_jX_i\) has colours

\[
 T\cup\{c_i\},\qquad
 \{\infty\}\cup T\cup\{c_i,c_k\}.                    \tag{2.6}
\]

#### Proof

Successive pairs in (2.2) differ respectively by

\[
 c_i\leftrightarrow c_j,\quad
 \infty\leftrightarrow c_k,\quad
 c_j\leftrightarrow c_i,\quad
 c_k\leftrightarrow\infty.
\]

They are therefore Johnson adjacent.  Intersections and unions give
(2.4)--(2.6) directly. \(\square\)

### Theorem 3 (collision-free paired filter bank)

Choose a perfect matching of \(I_a\).  Expand every selected flag orbit to
its \(n\) physical flags, and at every flag choose one ordered triple
\((i,j,k)\).  Then the paths (2.3) may be chosen equivariantly under the
maximal clean group \(H\) and have all of the following properties.

1. They are pairwise vertex-disjoint.
2. Their selected Johnson edges have pairwise distinct lower colours and
   pairwise distinct upper colours.
3. Every exceptional lower colour and every exceptional upper colour occurs
   exactly once.
4. On each shore, the bank additionally uses exactly two ordinary colours
   per exceptional colour.

Consequently their union is an exact partial common transversal and a
disjoint union of physical four-vertex paths.

#### Proof

The selected necklace matching expands to a bijection between all physical
\(a\)-sets and all physical \((a+1)\)-sets by inclusion.  Lemma 2 therefore
uses every colour in (1.1) exactly once.

The ordinary lower colours in (2.4) avoid \(\infty\) and have a unique
\(K_3\)-coset occupancy pattern

\[
 3^a1^1;
\]

the full cosets recover \(A\), and the singleton recovers both \(b\) and
the literal point.  The ordinary upper colours in (2.5) contain \(\infty\)
and have the unique finite occupancy pattern

\[
 3^a2^1.
\]

Hence no ordinary colour repeats, either within one path or between paths.
The same occupancy signatures, together with the presence or absence of
\(\infty\), recover every vertex in (2.1), proving vertex-disjointness.

For equivariance, put

\[
 s=3^{v_3(q)},\qquad h=q/s,qquad d=s/3,
 \qquad H=\langle s\rangle\cong\mathbb Z_h.             \tag{2.7}
\]

The \(n=dh\) physical flags in a selected necklace orbit split into \(d\)
free \(H\)-orbits.  Choose an ordered triple at one representative of each
such orbit and translate it by \(H\).  This is consistent after \(h\)
steps because \(hs=q\), and gives the asserted equivariant choice.
\(\square\)

### Exact quotient ledger

Let \(c=\operatorname{Cat}_a\).  The bank of Theorem 3 has

\[
 nc\text{ physical }P_4\text{ paths},qquad
 dc\text{ quotient }P_4\text{ paths}.                  \tag{2.8}
\]

It uses \(3dc\) quotient common-transversal edges and \(4dc\) quotient
middle vertices.  Every quotient path in (2.8) has internal voltage zero:
choose its four representatives from one literal flag; translation by
\(s\) carries the whole path to its next lift.

This resolves the local realization of the
\(\operatorname{Cat}_a\) lower and \(\operatorname{Cat}_a\) upper filters.
When \(v_3(q)>1\), one filter necklace has \(d=3^{v_3(q)-1}\) clean-group
track pieces, exactly as required by the iterated three-phase section.

The final quotient forest, if it exists, has

\[
 p=\frac{\operatorname{Cat}_{3a+2}}h
   =d\,\frac{\operatorname{Cat}_{3a+2}}{2a+1}          \tag{2.9}
\]

path components.  This number is even and satisfies

\[
                         p\ge 2d\operatorname{Cat}_a. \tag{2.10}
\]

For parity, \(\operatorname{Cat}_r\) is odd exactly when \(r+1\) is a
power of two; here \(3a+3\) is divisible by three, while \(h\) is odd.
For the inequality, the Catalan ratio
\(\operatorname{Cat}_{r+1}/\operatorname{Cat}_r
=2(2r+1)/(r+2)\) is at least two for \(r\ge1\), giving
\(\operatorname{Cat}_{3a+2}/\operatorname{Cat}_a
\ge2^{2a+2}\ge2(2a+1)\) for \(a\ge1\);
\(a=0\) is equality.  Thus scalar component capacity is never the
obstruction to accommodating the \(dc\) packet paths.  This count does not
prove the degree, palette, acyclicity, or connector conditions below.
For each track piece there are three choices of the omitted element
\(c_k\), hence \(3^d\) underlying \(H\)-invariant paired sections (and
\(6^d\) ordered path orientations).  The construction deliberately locks
the lower and upper phase choices together inside each square; it does not
claim to realize every independently prescribed pair of filter phases.

### Lemma 4 (packet endpoints cannot self-chain across flags)

Let \(R,R'\) be packet paths belonging to two distinct matched physical
flags.  No endpoint of \(R\) is Johnson adjacent to an endpoint of \(R'\).

#### Proof

An \(X\)-endpoint has \(\infty\) and finite coset occupancy \(3^a1^1\).
If two such vertices were adjacent, changing the set of full cosets would
already contribute at least two points in each direction to their symmetric
difference.  Hence their full-coset sets agree.  The necklace matching gives
only one flag over that physical \(A\), so the endpoints belong to the same
packet.

For two \(Y\)-endpoints of occupancy \(3^a2^1\), adjacency can also swap
which one of two cosets is full and which is partial.  In that case the
union of the full and partial cosets is the same physical
\((a+1)\)-set \(B\) for both endpoints.  The expanded necklace matching
gives only one matched lower neighbour \(A\) of that \(B\), so two distinct
selected packets still cannot occur.  If the full/partial roles do not
swap, the occupancy pattern directly recovers the same flag.

Finally, if an \(X\)-endpoint and a \(Y\)-endpoint are adjacent, deleting
\(\infty\) from the former must leave a subset of the latter.  All \(a\)
full cosets must therefore agree, and the singleton of the \(X\)-endpoint
must lie in the unique partial coset of the \(Y\)-endpoint.  This recovers
the same flag \(A\subset A\cup\{b\}\).  Again the endpoints are from one
packet. \(\square\)

Consequently, if these packets are kept as separate forest components,
their connector cycle needs bulk sockets: packet components cannot be
placed consecutively.  A closure containing \(dc\) separate packet
components then has at least \(dc\) nonpacket components.  This is a
necessary condition only for that separated normal form; an absorbed
extension may attach residual forest edges to packet endpoints first.

## 3. Native-socket complement zipper

For every packet (2.3), call the omitted fourth edge

\[
 z(A,b;i,j,k)=X_iY_j                                  \tag{3.1}
\]

its **native socket**.  The socket and the three-edge packet have the same
ordered endpoints.  Moreover, their gain difference is identically zero:
the union is the literal square (2.2), hence a closed zero-voltage walk.
This statement is gauge independent.

### Theorem 5 (unit-voltage socket subdivision)

Choose the complement zipper and its \(dc\) quotient packet paths as in
Theorem 3.  Suppose there is a directed quotient Johnson cycle
\(\bar C^\circ\) with the following properties.

1. Its vertex set consists of every quotient middle-vertex orbit except the
   two internal orbits \(X_j,Y_i\) of each packet.
2. It contains every native socket \(X_iY_j\), in one of its two
   orientations.  These sockets are pairwise vertex-disjoint.
3. Its total voltage \(v\in\mathbb Z_h\) is a unit.

Simultaneously replace every native socket by the corresponding three-edge
packet path with the same orientation.  The result is a spanning quotient
Johnson cycle \(\bar C\) on all \(M/h\) middle orbits, and its voltage is
still \(v\).  Hence its regular \(H\)-lift is one physical Hamilton cycle.

#### Proof

By Theorem 3 and Lemma 4 the socket endpoints and internal packet vertices
are all distinct.  Replacing a cycle edge by a path with the same endpoints
preserves the one-cycle topology, and doing so on vertex-disjoint sockets
commutes.  Every omitted internal vertex is introduced exactly once, so the
new cycle is spanning.  The old socket and new detour differ by the literal
zero-voltage square (2.2); each replacement therefore changes total voltage
by zero.  The unit-voltage lift theorem now gives one physical cycle.
\(\square\)

### Corollary 6 (exact common-transversal lift on the zipper cycle)

In addition to Theorem 5, suppose the expanded quotient cycle \(\bar C\)
has a set \(\bar F\) of quotient edges such that:

1. all three edges of every filter packet belong to \(\bar F\); and
2. lower and upper colours are each used exactly once by \(\bar F\).

Then the lift of \(\bar F\) is an exact physical common transversal, and it
is a spanning path forest contained in the Hamilton lift of \(\bar C\).

Indeed, clean-group freeness turns the quotient colour condition into the
literal condition.  Also

\[
 |\bar F|=N/h<M/h=|V(\bar C)|,
\]

so a proper edge subset of the single cycle \(\bar C\), with all vertices
retained (isolated vertices allowed as one-vertex paths), is a spanning path
forest.  It has \((M-N)/h=K/h\) quotient components and therefore \(K\)
physical components.

Theorem 5 is the strongest endpoint-preserving form of the construction:
filter insertion itself needs neither a connector search nor a voltage
correction.  Its exact remaining hypotheses are a unit-voltage reduced
cycle containing all prescribed native sockets and an exact post-expansion
colour selector as in Corollary 6.  These hypotheses are not proved in
general.

Socket subdivision is topology- and voltage-neutral, but it is not
palette-neutral: the ordinary socket colours (2.6) disappear and the three
lower/upper colours (2.4)--(2.5) appear.  The residual selector must recover
the omitted ordinary socket colours elsewhere.  This is why the next gate
cannot be dropped.

### Proposition 7 (exact forced-selector reduction)

For a candidate expanded cycle \(\bar C\), form its bipartite
colour-incidence multigraph \(G(\bar C)\): the shores are quotient lower and
upper colour orbits, and every cycle edge \(e\) gives one occurrence edge
\(\ell(e)u(e)\).  Force the \(3dc\) packet edges, delete their incident
colour vertices, and delete every competing occurrence edge incident with a
deleted colour.  Call the residual graph \(G^\circ(\bar C)\).

The selector required by Corollary 6 exists if and only if
\(G^\circ(\bar C)\) has a perfect matching.  If its maximum degree is at
most two, this is equivalent to every path component having equally many
lower and upper vertices; cycle components are automatically balanced.

#### Proof

The packet edges are already a matching on both colour shores by Theorem 3.
Any perfect common transversal containing them must avoid every other edge
at their colour vertices, and its remaining edges must cover every residual
colour vertex once.  This is exactly a perfect matching of
\(G^\circ(\bar C)\), proving the first assertion and its converse.

A bipartite graph of maximum degree two is a disjoint union of paths and
even cycles.  Every even cycle has an alternating perfect matching.  A path
has one precisely when its two shore sizes agree, in which case leaf
peeling forces the matching uniquely. \(\square\)

Thus the complement-zipper route has two literal, independently auditable
gates: a socket-containing unit-voltage cycle on the reduced middle set,
and a residual colour matching.  It does not require a generic Hamilton
search after the reduced cycle is supplied.

## 4. The absorbed forest-extension gate inside the fixed packet face

Put

\[
 K=\operatorname{Cat}_m,\qquad
 M=(m+1)K,\qquad N=mK.
\]

After reserving the packet bank, the exact remaining quotient ledger is

\[
 \begin{array}{c|c}
 \text{object}&\text{remaining count}\\ \hline
 \text{middle vertices not in the packets}&M/h-4dc\\
 \text{common-transversal edge orbits}&N/h-3dc.
 \end{array}                                            \tag{4.1}
\]

The remaining edges must use every unreserved lower and upper colour orbit
once.  They need **not** be vertex-disjoint from the packet bank.  They may
attach to either exposed endpoint of a packet, thereby absorbing that
packet as an internal subpath of a longer forest component.  They may not
touch either internal packet vertex, which already has degree two.

This distinction removes a false one-filter--one-hinge accounting.  A
completed exact transversal has \(K/h\) quotient path components regardless
of how many packet paths it contains.  Its \(K/h\) connector orbits are
indexed by those final components, not by exceptional colours, necklaces,
or packet paths.

There is one immediate local closure cut.  For the packet
\(X_i-X_j-Y_i-Y_j\), the omitted edge

\[
                         o=X_iY_j                       \tag{4.2}
\]

has a lower and an upper colour unused by the three packet edges, but adding
\(o\) closes the four-cycle (2.2).  Hence every forest extension must match
at least one of those two colours elsewhere.  At \(a=0\), these are the only
two unserved colours, so the packet normal form has no forest extension.
This is a scoped base obstruction, not a failure of the Catalan construction
at \(m=2\), which must use a different local matching.

Here is an exact quotient formulation of the remaining gate.  Let
\(\bar V\) be the middle-orbit set, let \(\bar R\) be the prescribed packet
forest, and let \(E^*\) contain every nonloop quotient Johnson edge whose
lower and upper colour orbits are unused by \(\bar R\).  A residual selector
\(x\in\{0,1\}^{E^*}\) extends the packets to a spanning linear forest if
and only if

\[
 \sum_{e:\ell(e)=L}x_e=1,\qquad
 \sum_{e:u(e)=U}x_e=1                                  \tag{4.3}
\]

for every unserved lower orbit \(L\) and upper orbit \(U\),

\[
 \deg_{\bar R}(v)+\sum_{e\ni v}x_e\le2
 \qquad(v\in\bar V),                                    \tag{4.4}
\]

and

\[
 |E(\bar R[S])|+
 \sum_{e\in E^*[S]}x_e\le |S|-1
 \qquad(\varnothing\ne S\subseteq\bar V).              \tag{4.5}
\]

The colour equations make the union an exact common transversal; (4.4)
is exactly the middle degree cap; and (4.5) is exactly the graphic-forest
condition.  The resulting union has \(N/h\) edges on \(M/h\) vertices and
therefore exactly \(K/h\) path components.  In particular, (4.3)--(4.5)
are a literal, auditable finite gate, not an asserted total-unimodular
system.

This formulation is exact only after the packet bank has been fixed.
For the unrestricted existential route it is unnecessarily strong:
MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md
proves that one may choose a global quotient perfect matching first and
read its exceptional filters afterward.  The residual matching extension
then disappears; only the linear-lift and unit-voltage cycle conditions on
the chosen global matching remain.

## 5. General prescribed-filter extension and neutral insertion

The next statement records the general extension criterion before using the
special zipper packets.

### Theorem 8 (prescribed-filter quotient extension)

Let a cyclic group \(H\cong\mathbb Z_h\) act freely on the three Boolean
shores and hence on occurrence-labelled Johnson edges.  Let \(R\) be any
prescribed \(H\)-invariant partial common transversal.  Assume:

1. lower and upper colours are injective on \(R\), and its quotient
   selected-edge graph \(\bar R\) is a vertex-disjoint path forest;
2. an \(H\)-invariant edge set \(F\supseteq R\) is exact on both outer
   palettes and its quotient \(\bar F\) is a spanning linear forest;
   edges of \(F\setminus R\) may attach to endpoints of \(\bar R\);
3. every quotient path of \(\bar F\) is given an ordered pair of endpoints,
   and quotient Johnson connector edges join each positive endpoint to
   exactly one next negative endpoint so that contraction of the paths
   gives one directed cycle; the occurrence-labelled connector orbits are
   pairwise physically distinct, disjoint from \(F\), and no connector
   touches an internal path vertex; and
4. the total gain of that directed quotient cycle generates
   \(\mathbb Z_h\), equivalently it is a unit modulo \(h\).

Then the physical lift of \(F\) is a spanning common-transversal path
forest containing \(R\), and the connector lift is one Hamilton cycle.

#### Proof

The palette hypothesis makes \(F\) an exact common transversal.
The spanning linear-forest hypothesis and clean-group freeness make its
physical lift a spanning path forest containing the prescribed edges.
Since a quotient path is a tree, its gains gauge to zero and its regular
\(H\)-lift is \(h\) disjoint physical paths.
Ordered endpoint preservation makes every restored vertex degree two, and
the contracted quotient is one cycle.  A closed traversal changes the
fibre label by the total gain, so a unit gain has one orbit on
\(\mathbb Z_h\).  The connected 2-regular spanning lift is one Hamilton
cycle. \(\square\)

This theorem applies to arbitrary prescribed filters.  The zipper bank of
Theorem 3 supplies Item 1, including literal internal disjointness, but does
not by itself supply Items 2--4.  In particular, it imposes no map from a
filter edge or packet to a connector.  A prescribed packet may be buried
strictly inside a final path, and only the endpoints of that final path
participate in the connector cycle.

The following neutral-insertion theorem is a useful **separated
specialization**, not a necessary normal form.  It deliberately keeps every
packet as its own component before closure and therefore uses one socket per
quotient packet.  The absorbed extension of Theorem 8 need not do this.

Here a **separated complementary bulk forest** \(\bar F_0\) means an exact
selector for all remaining lower and upper colours whose vertices avoid the
packet bank.  It uses \(M/h-4dc\) vertices and \(N/h-3dc\) edges and,
when it is a spanning forest of that reserved bulk, has \(K/h-dc\)
components.

Assume such a separated complementary bulk forest \(\bar F_0\) exists.
Suppose its path
components have already been joined by quotient Johnson connector edges
into one directed cycle \(\bar C_0\) of voltage
\(v_0\in\mathbb Z_h\), with \(\gcd(v_0,h)=1\).

For a directed quotient edge \(e=uv\), write \(g(e)\) for its gain: chosen
representatives \(\widetilde u\) and \(\rho^{g(e)}\widetilde v\), where
\(\rho(x)=x+s\), are adjacent.  Reverse traversal negates the gain.

### Theorem 9 (neutral filter-packet insertion)

Let \(R_1,\ldots,R_{dc}\) be the quotient packet paths of Theorem 3, with
oriented endpoints \((x_r,y_r)\) and path gain \(r_r\) (canonically
\(r_r=0\)).  Assume there are distinct connector seams

\[
 e_r=p_rq_r\in E(\bar C_0)
\]

and legal quotient Johnson edges \(p_rx_r\), \(y_rq_r\) such that

\[
 g(p_rx_r)+r_r+g(y_rq_r)=g(p_rq_r)\pmod h              \tag{5.1}
\]

for every \(r\).  Replace each seam \(p_rq_r\) by the detour

\[
 p_r-x_r\;R_r\;y_r-q_r.                                \tag{5.2}
\]

Then the resulting quotient graph is one spanning cycle, its common
transversal is the union of the bulk forest and all packet paths, and its
voltage is still \(v_0\).  Its physical \(H\)-lift is therefore one
Hamilton cycle on all \(M\) middle vertices, while every lower and upper
colour is used exactly once by the distinguished common transversal.

#### Proof

The seams are distinct and the packet paths are mutually disjoint and
disjoint from the bulk.  Replacing a cycle edge by a disjoint path preserves
connectedness and degree two, so simultaneous replacements leave one
quotient cycle.  The voltage change at packet \(r\) is

\[
 \delta_r=g(p_rx_r)+r_r+g(y_rq_r)-g(p_rq_r),
\]

which is zero by (5.1).  Hence the total voltage remains \(v_0\).
The packet and bulk palettes partition both outer shores, so their union is
an exact common transversal.  Finally the clean-group action is free and
the voltage-cycle theorem gives \(\gcd(v_0,h)=1\) physical components,
namely one. \(\square\)

### Corollary 10 (phase-preserving Hall criterion)

Gauge \(\bar C_0\) so that all its edge gains vanish except on one protected
seam carrying the unit voltage \(v_0\).  Form a bipartite graph whose left
shore is the \(dc\) packet paths and whose right shore is the remaining
bulk connector seams.  Join a packet to a seam when some orientation of the
packet admits both literal connector edges in the same \(H\)-phase; in this
gauge every term in (5.1) is zero.

If this port graph has a matching saturating the packet shore, then the
construction of Theorem 9 applies.  Equivalently, it is enough that

\[
 |N(\mathcal S)|\ge |\mathcal S|
 \quad\text{for every packet family }\mathcal S.        \tag{5.3}
\]

For \(h=1\), no seam needs protection.  More generally, if neutral
insertions are unavailable, choices with defects \(\delta_r\) are still
sufficient precisely when the selected distinct seams obey

\[
 \gcd\!\left(v_0+\sum_r\delta_r,h\right)=1.             \tag{5.4}
\]

Thus the residual connector problem is a finite labelled matching, not an
unstructured Hamilton search.

## 6. Exact scope, carrier/compiler separation, and the remaining gate

The following statements are proved without a solver.

1. The two exceptional Catalan banks can always be paired by smaller
   necklace inclusion flags.
2. Every paired flag has the literal collision-free \(P_4\) realization
   (2.3).
3. The full paired bank is an \(H\)-invariant partial common transversal
   and a physical path forest, with exact ledger (2.8).
4. An absorbed forest extension satisfying (4.3)--(4.5), followed by an
   arbitrary one-cycle endpoint matching of unit voltage, gives the required
   connected physical lift without any filter--connector correspondence.
5. The native-socket subdivision and the neutral Hall insertion are two
   stronger sufficient normal forms, not necessary conditions.

Within this optional packet face, what is not proved is that, for every
\(a\), the reserved packet bank has an
absorbed extension satisfying (4.3)--(4.5), or that the endpoint connector
records of such an extension contain a one-cycle primitive-voltage
selection.  In the separated specialization, the stronger unproved gate is
the Hall condition (5.3).

These fixed-bank questions are not the general existential gate.  The
cycle-first formulation in
MATH_THEOREM_CATALAN_GLOBAL_MATCHING_CYCLE_FIRST_PHYSICAL_GATE_20260731.md
asks directly for one unit-voltage quotient Johnson cycle whose
colour-incidence graph has a perfect matching; its matching restriction
supplies the exceptional filters automatically.

These are carrier/common-transversal statements only.  No equivariance is
assumed for a later common-cap compiler.  The authenticated K16 optimum
shows why: its carrier is organized as four strict spirals opened by three
Johnson connectors, but its four symmetry defects do not correspond
one-for-one to shortened colour orbits, and its integral compiler strongly
breaks the clean subgroup symmetry.  That anatomy is consistent with
Theorem 8—filters may be internal to the final paths and connectors are
chosen for topology—but it is not claimed to instantiate the packet normal
form above.

Repetition of connector colours is harmless for immediate lower/upper
coverage because the distinguished forest already uses every colour once;
any stronger uniform-outgoing, floor-load, residence, or compiler claim
requires additional literal constraints not asserted here.

The packet identities and orbit ledgers are independently replayed for
small parameters by

```text
python3 scratch/audit_catalan_period3_filter_connector_packets_20260731.py
```
