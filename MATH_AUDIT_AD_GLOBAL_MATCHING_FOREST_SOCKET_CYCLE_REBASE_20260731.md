# Audit and exact rebase: global quotient matching to a private unit-voltage cycle

Date: 2026-07-31  
Status: independently audited exact equivalences and finite model; no
all-dimension existence theorem

## 0. Verdict

The global-matching-first theorem is sound, with its typed-shore and
three-adic qualifications stated explicitly below.  It removes the
residual-Kneser Hall problem from the **existential** construction: choose a
perfect matching of the complete clean-
\(H\) quotient diamond graph first, and obtain the exceptional filters by
restriction.

The exact remaining carrier gate is equivalent to one coloured
unit-voltage-cycle problem:

> Find a spanning directed occurrence cycle \(C\) in the clean quotient
> Johnson graph, of primitive total voltage, such that the lower--upper
> colour-incidence graph of the occurrences in \(C\) has a perfect matching.

The perfect-matching occurrences are then automatically a spanning linear
forest, and the complementary cycle occurrences are automatically its
endpoint-private closure.  This equivalence is exact for the clean odd group.
It does **not** make packet, collar, guard, residence, or compiler resources
private; those require literal developed-resource records.

No claim from `GK_PROJECTION_COUNTS` or `GK_TWO` that a linear subforest can
retain at most half the original edges is used here.  That bound is false and
is irrelevant to this reduction.

## 1. Objects and multiplicities

Fix \(m\ge2\), let \(|\Omega|=2m\), and put

\[
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal V=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1}.
\]

Write

\[
 K=\operatorname{Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 M=|\mathcal V|=(m+1)K=N+K.                 \tag{1.1}
\]

The diamond graph \(\mathcal B_m\) is the bipartite graph on
\(\mathcal L\sqcup\mathcal U\) with \(L\sim U\) iff \(L\subset U\).
It is balanced and

\[
 \Delta=\binom{m+1}{2}                                  \tag{1.2}
\]

regular.  Every diamond \(L\subset U\), with
\(U\setminus L=\{a,b\}\), is in bijection with the literal Johnson edge

\[
 \psi(L,U)=\{L\cup\{a\},L\cup\{b\}\}.                 \tag{1.3}
\]

Let \(H\cong\mathbb Z_h\) be the clean subgroup from the three-primary
reduction.  Thus \(h\) is odd, and \(H\) acts freely on all three displayed
ranks.  Bars denote \(H\)-orbits.  An edge of the quotient is an
**occurrence-labelled edge orbit**.  Every carrier record is one distinct
\(H\)-orbit of physical Johnson edges, and different selected carrier records
must have disjoint physical developments.  Parallel carrier orbits are
retained when they have different physical middle edges or voltage.  Collar,
socket, and guard alternatives on one carrier orbit are linked refinement
records, not additional carrier edges.

## 2. Audit of the global matching theorem

### Theorem 2.1 (regular quotient matching)

The quotient multigraph \(\mathcal B_m/H\), with edge-orbit multiplicity,
is balanced and \(\Delta\)-regular.  Hence it has a perfect matching, and the
full \(H\)-development of that matching is an \(H\)-invariant physical
perfect matching of \(\mathcal B_m\).

#### Proof

An element stabilizing a diamond edge fixes its lower and upper endpoints,
because the action preserves the two shores.  Vertex freeness therefore
forces the edge stabilizer to be trivial.  Each edge orbit has size \(h\) and
contributes exactly one incidence at every physical vertex in each of its two
endpoint orbits.  Thus every quotient vertex has degree \(\Delta\), counted
with multiplicity.

For a set \(X\) of lower quotient vertices, incidence counting gives

\[
 \Delta|X|\le \Delta|N(X)|.
\]

Hall gives a quotient perfect matching.  Developing each selected edge orbit
covers every physical vertex of each selected endpoint orbit once, so the
lift is a physical perfect matching. \(\square\)

Multiplicity is essential in this proof.  Collapsing parallel quotient
records need not preserve regularity and is not a valid model reduction.

### Theorem 2.2 (automatic minimal filters, exact scope)

Suppose

\[
 q=2m-1=6a+3,qquad v_3(q)=1,qquad h=q/3=2a+1.
\]

The restriction of any quotient perfect matching from Theorem 2.1 to the
exceptional lower and upper banks consists of exactly

\[
 2\operatorname{Cat}_a                                  \tag{2.1}
\]

clean-\(H\) edge orbits.  It services every exceptional colour once, is
already globally extended, and has pairwise-distinct physical middle
endpoints.  Each selected orbit is exactly one of the three \(H\)-phases in
its free full-\(\mathbb Z_q\) edge orbit.

#### Audit proof

An exceptional colour is

\[
 E_A=\{\infty\}\cup\pi^{-1}(A),qquad
 A\in\binom{\mathbb Z_{2a+1}}a.
\]

There are

\[
 \frac1{2a+1}\binom{2a+1}{a}=\operatorname{Cat}_a
\]

exceptional \(H\)-vertex orbits on each typed shore.  Two exceptional
vertices cannot form a diamond: after complement-identifying the upper
shore, both contain \(\infty\), so they are not disjoint.  The matching
therefore uses one distinct edge orbit for each of the two exceptional
banks, proving (2.1).

A full rotation edge orbit is free and splits into three clean phases.  All
three phases meet the same exceptional colour orbit.  Selecting a second
phase would rematch every exceptional physical colour, so exactly one phase
is selected.

Two different exceptional lower sets differ in at least one whole
three-point coset, hence have symmetric difference at least six.  Two
rank-\((m-1)\) subsets of one rank-\(m\) set have symmetric difference two.
Thus two lower-filter diamonds cannot share a middle endpoint.
Complementation proves the upper case.  A lower-filter middle endpoint
contains \(\infty\), while an upper-filter middle endpoint does not, so the
two families do not collide. \(\square\)

There are three necessary qualifications.

1. Opposite colours are distinct on each **typed physical shore**.  After
   identifying the two shores by complementation, the same auxiliary Kneser
   label may occur once in each family.
2. The count (2.1) and one-third statement require \(v_3(q)=1\).  If
   \(s=3^{v_3(q)}>3\), this period-three bank alone splits into
   \(2(s/3)\operatorname{Cat}_a\) clean-\(H\) vertex/edge orbits.  No total
   higher-adic exceptional-bank count is claimed here.
3. The sharp \(2\operatorname{Cat}_a\) number is the forced exceptional-bank
   contribution.  It is not a statement that the completed matching has no
   other partially occupied full-rotation edge orbit.

## 3. Exact forest-lift criterion

Let \(Q\) be a quotient perfect matching, and let \(\bar F(Q)\) be the
occurrence-labelled quotient multigraph on \(\bar{\mathcal V}\) obtained by
applying (1.3).  A loop has incidence multiplicity two.

### Theorem 3.1 (quotient forest iff physical forest)

The physical \(H\)-development of \(Q\) is a spanning linear forest if and
only if

\[
 \deg_{\bar F(Q)}(v)\le2
       \qquad(v\in\bar{\mathcal V})                     \tag{3.1}
\]

and \(\bar F(Q)\) is graphic-acyclic, including the exclusion of loops and
parallel-edge two-cycles.

Equivalently, for matching variables \(x_e\), these are

\[
 \sum_e\iota_v(e)x_e\le2
       \qquad(v\in\bar{\mathcal V})                    \tag{3.2}
\]

and

\[
 \sum_{e:\,p(e),q(e)\in W}x_e\le |W|-1
       \qquad(\varnothing\ne W\subseteq\bar{\mathcal V}). \tag{3.3}
\]

Every such quotient forest has exactly \(K/h\) path components, with
isolated quotient vertices allowed, and its physical lift has exactly
\(K\) paths.

#### Proof

Because \(h\) is odd, an edge orbit cannot invert its two middle endpoints.
Thus the middle lift is an ordinary regular voltage development.  Voltages
on a quotient tree gauge to zero, so a quotient tree develops into \(h\)
disjoint physical trees.  Conversely, the development of any quotient cycle
is a finite two-regular graph on its lifted cycle edges and therefore
contains physical cycles, whether its total voltage is zero or nonzero.
This proves the iff statement.

A quotient perfect matching has \(N/h\) edges on \(M/h\) middle vertices.
For a forest, Euler's identity gives

\[
 \frac Mh-\frac Nh=\frac Kh                            \tag{3.4}
\]

components.  Each quotient tree has \(h\) physical lifts, yielding \(K\)
physical paths. \(\square\)

Oddness is substantive.  For an even group, an endpoint-inverting quotient
loop can develop to a matching rather than a cycle.  This caveat does not
affect the three-primary clean group, whose order divides the odd number
\(2m-1\).

### Corollary 3.2 (exact five-matroid boundary)

Take two orientations of every loopless quotient diamond occurrence.  On
this directed ground set impose:

1. capacity one at every lower colour orbit;
2. capacity one at every upper colour orbit;
3. capacity one at every middle tail;
4. capacity one at every middle head; and
5. the graphic matroid of the underlying quotient middle multigraph, with
   all distinct records having the same unordered middle endpoints parallel,
   and in particular with the two orientations of one record parallel.

A common independent set of size \(N/h\) is exactly a two-sided-rainbow
spanning quotient path forest.  Indeed the size makes the two colour
capacities exact; tail/head capacity makes each graphic-tree component a
coherently oriented path; and the graphic matroid gives acyclicity.
Conversely, orient every path consistently.

This is a five-matroid characterization, not an ordinary two-matroid
intersection theorem and not a consequence of the total unimodularity of
the outer matching equations.

## 4. Exact closure and voltage

Orient the \(c=K/h\) quotient paths as

\[
 P_i:a_i^-\rightsquigarrow a_i^+.
\]

A singleton path has two formal incidence ports at its one vertex.  A socket
record is an occurrence-labelled directed Johnson edge

\[
 s:a_i^+\longrightarrow a_j^-                         \tag{4.1}
\]

with its literal phase, gain, and complete developed physical resource
multiset.

### Theorem 4.1 (private endpoint closure)

A socket set \(S\) closes the forest into one occurrence-private quotient
cycle if and only if:

1. every positive path port has exactly one outgoing socket;
2. every negative path port has exactly one incoming socket;
3. the developed edge occurrences are distinct and disjoint from the
   forest; and
4. the induced permutation of the \(c\) path components is one cycle.

Then \(|S|=c\).  If \(\lambda_i\) is the oriented gain of \(P_i\) and
\(\gamma_s\) is the gain of socket \(s\), the gauge-invariant total voltage
is

\[
 v=\sum_i\lambda_i+\sum_{s\in S}\gamma_s\pmod h.       \tag{4.2}
\]

The physical development has exactly \(\gcd(h,v)\) cycles and is Hamiltonian
if and only if

\[
 \gcd(h,v)=1.                                           \tag{4.3}
\]

#### Proof

The first two conditions make every quotient middle vertex degree two after
closure.  The third forbids repeated literal edges.  Contracting every path
turns the fourth condition into one directed component cycle, so the quotient
union is connected and two-regular.  One quotient traversal changes the
fibre coordinate by (4.2); its action on \(\mathbb Z_h\) has
\(\gcd(h,v)\) orbits. \(\square\)

Deleting one **physical phase occurrence** of one closure socket opens the
Hamilton cycle into one physical spanning path.  Deleting the complete
socket orbit leaves \(h\) physical paths when \(h>1\).

The word "private" in Theorem 4.1 concerns middle edge and endpoint
occurrences.  It does not automatically cover packet, collar, guard, host,
or compiler resources.  If a non-clean rank appears in such a resource, one
quotient record can even self-collide under its own development.  Therefore
each refined socket record must list the complete developed resource
**multiset**, must be rejected if it internally exceeds a capacity, and must
participate in exact aggregate physical-capacity rows.  An enable bit not
linked to an actually selected or reserved occurrence is unsound.

## 5. Cycle-first equivalence

Here a spanning occurrence-labelled quotient cycle means a connected
two-regular occurrence multigraph, with loops counted twice and every
underlying carrier edge-orbit record used at most once.  Its selected
physical developments are required to be pairwise disjoint.  For such a
cycle \(C\), let \(G(C)\) be
the bipartite multigraph whose shores are
\(\bar{\mathcal L},\bar{\mathcal U}\) and whose edge corresponding to a
cycle occurrence \(e\) joins its lower and upper colour orbits
\(\ell(e),u(e)\).

### Theorem 5.1 (global matching plus closure iff coloured cycle)

The following are equivalent.

1. There is a global quotient perfect matching whose physical lift is a
   spanning linear forest and which has a Johnson-edge/endpoint-private
   unit-voltage closure.
2. There is a spanning directed quotient Johnson occurrence cycle \(C\)
   satisfying
   \[
    \gcd(h,v(C))=1                                      \tag{5.1}
   \]
   such that \(G(C)\) has a perfect matching.

Under this equivalence the perfect matching of \(G(C)\) is the global
diamond matching \(Q\), and

\[
 E(C)\setminus Q                                       \tag{5.2}
\]

is its \(K/h\)-edge endpoint-private closure.  This equivalence does not
assert privacy of any extra packet, collar, guard, host, or compiler resource.

#### Proof

Assume (1) and adjoin the private closure edges to the matching forest.  By
Theorem 4.1 the result is one spanning quotient occurrence cycle of unit
voltage.  The selected forest uses every lower and upper colour once, so its
occurrences form a perfect matching in \(G(C)\).

Conversely, let \(Q\) be a perfect matching in \(G(C)\).  It has \(N/h\)
edges, whereas \(C\) has \(M/h>N/h\) edges.  Every proper edge subset of one
cycle is a spanning linear forest when unused vertices are retained as
isolated paths.  It has \(M/h-N/h=K/h\) components.  Reading the cyclic order
shows that the complementary occurrences (5.2) use every component's two
ports once and form one cycle after contraction.  The unit-voltage condition
then gives one physical Hamilton cycle. \(\square\)

This theorem commutes the matching and topology quantifiers without
returning to "prescribe filters, then extend."  The exceptional filters are
still read from the restriction of \(Q\).

### Corollary 5.2 (fixed-cycle Hall criterion)

For a fixed unit-voltage spanning quotient cycle \(C\), the whole outer
palette and forest gate is exactly

\[
 |N_{G(C)}(X)|\ge |X|
       \qquad(X\subseteq\bar{\mathcal L}).              \tag{5.3}
\]

Parallel occurrence edges remain distinct choices, but—as always—Hall's
neighbour set counts vertices, not edge multiplicity.

## 6. Compact exact joint model

For every undirected occurrence-labelled quotient Johnson record \(e\),
introduce direction bits \(z_e^+,z_e^-\) and a transversal bit \(x_e\).  Put
\(z_e=z_e^++z_e^-\), and impose

\[
 z_e^++z_e^-\le1,qquad x_e\le z_e.                    \tag{6.1}
\]

At every quotient middle vertex impose one incoming and one outgoing
\(z\)-arc, together with the directed subtour rows

\[
 \sum_{\substack{(e,\varepsilon):\\
          \operatorname{tail}(e^\varepsilon)\in W,\\
          \operatorname{head}(e^\varepsilon)\notin W}}
        z_e^\varepsilon
 \ge1
 \quad(\varnothing\ne W\subsetneq\bar{\mathcal V}).    \tag{6.2}
\]

For every quotient outer colour impose

\[
 \sum_{\ell(e)=L}x_e=1,qquad
 \sum_{u(e)=U}x_e=1.                                   \tag{6.3}
\]

Fix one representative of every quotient middle orbit.  If \(g(e)\) is the
gain in the positive orientation relative to those representatives, reversal
has gain \(-g(e)\).  Impose for \(h>1\)

\[
 \sum_e g(e)(z_e^+-z_e^-)
  =ht+\sum_{r\in\mathbb Z_h^\times}r\eta_r,qquad
 \sum_{r\in\mathbb Z_h^\times}\eta_r=1,              \tag{6.4}
\]

where \(t\in\mathbb Z\) and the \(\eta_r\) are binary.  For \(h=1\), omit
(6.4), or explicitly adopt the trivial-generator convention.

Equations (6.1)--(6.2) choose one directed quotient cycle; (6.3) chooses a
perfect colour-incidence matching inside it; and (6.4) makes its lift
connected.  Since \(x\) is a proper subset of the one cycle, separate middle
degree and graphic cuts are unnecessary in this cycle-first model.  The
closure selector is simply

\[
 y_e=z_e-x_e.                                           \tag{6.5}
\]

Every literal physical occurrence and developed private resource also has
its exact capacity row.  A quotient-level resource coefficient is the sum of
its physical multiplicities in the selected orbit-complete record, not an
orbit average.  Packet/collar refinements are additional linked selectors;
they are not free variables and are not implied by (6.5).

## 7. Why regularity alone cannot finish the gate

Already for \(m=2\), on
\(\Omega=\{\infty,0,1,2\}\), the four diamond edges whose middle edges are

\[
 \infty0-\infty1,qquad
 12-02,qquad
 \infty0-02,qquad
 \infty1-12                                             \tag{7.1}
\]

use every lower and upper colour exactly once.  Thus they are a global
diamond perfect matching.  Their physical middle graph is a \(C_4\) plus
the isolated vertices \(01\) and \(\infty2\), not a linear forest.

More generally, the standard BTK two-rank perfect matching has a middle
vertex of degree \(m\) for every \(m\ge3\), as proved in
`MATH_THEOREM_CATALAN_ABSTRACT_COLOUR_FOREST_AND_PHYSICAL_LIFT_GATE_20260731.md`.
Hence quotient regularity, marginal balance, determinant information, and
an arbitrary perfect matching do not control the physical lift.

This obstruction is exact but does not prove nonexistence of a forest-good
matching.  It shows why the selection inside the perfect-matching polytope is
the genuine remaining theorem.

## 8. Proved boundary and next exact lemma

Proved here:

1. global-first matching removes the exceptional residual-Hall gate;
2. the physical forest condition is exactly degree cap plus quotient graphic
   acyclicity;
3. private endpoint closure is exactly a one-cycle component permutation;
4. connected physical development is exactly primitive total voltage;
5. the entire carrier gate is exactly the coloured-cycle equivalence of
   Theorem 5.1; and
6. compiler symmetry is unnecessary and must not be imposed.

Not proved:

1. existence, for every \(m\), of a unit-voltage spanning quotient cycle
   satisfying the fixed-cycle Hall inequalities (5.3);
2. private packet/collar/guard resources for the inherited exceptional
   matching edges;
3. residence, deeper shadows, boundary chronology, or a common-cap literal
   compiler.

Thus the sharp all-dimension carrier lemma is:

> For the maximal clean subgroup \(H\), construct one unit-voltage spanning
> quotient Johnson occurrence cycle \(C\) for which \(G(C)\) has a perfect
> matching, together with any separately required literal private-resource
> refinements.

The authenticated K16 anatomy supports symmetry on a carrier scaffold only:
its three \(\mathbb Z_5\) sectors are interlaced across four spirals, and its
compiler is asymmetric.  It does not prove the all-dimension lemma.

## 9. Audited sources

Hashes are recorded at the final freeze of this note.

* `MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`
* `MATH_REDUCTION_GLOBAL_QUOTIENT_MATCHING_PHYSICAL_FOREST_SOCKET_VOLTAGE_20260731.md`
* `MATH_THEOREM_CATALAN_GLOBAL_MATCHING_CYCLE_FIRST_PHYSICAL_GATE_20260731.md`
* `MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`
* `MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`
* `MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md`
