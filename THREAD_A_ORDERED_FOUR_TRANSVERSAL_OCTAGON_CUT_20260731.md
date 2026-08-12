# The first alternating-cycle palette trap for ordered four-transversals

Date: 2026-07-31  
Status: exact algebraic and local-rounding theorems.  This note does not
prove the Catalan Linear Matching Theorem.  It identifies the first possible
palette obstruction inside a simple half-integral tail--head cycle and gives
an exact two-parent switching criterion.

## 1. Ordered atoms

Let \(|\Omega|=2m\), and write

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1}.
\]

An **ordered diamond atom** is a quadruple

\[
 e=(L,U;T,H),                                      \tag{1.1}
\]

where \(L\subset U\), \(|U\setminus L|=2\), and \(T,H\) are the two
rank-\(m\) sets strictly between \(L\) and \(U\), in one of their two
orders.  Put

\[
 \lambda(e)=L,\quad \upsilon(e)=U,\quad
 \tau(e)=T,\quad \eta(e)=H.                        \tag{1.2}
\]

An integral ordered four-transversal is a set of atoms using every lower
and every upper colour once, every tail and every head at most once, and
whose underlying Johnson edges form a forest.  This is the ordered form of
the Catalan Linear Matching assertion.

If

\[
 d=\binom{m+1}{2},
\]

then the ordered uniform point is

\[
                         y_e={1\over 2d}.             \tag{1.3}
\]

Every lower and upper row has load one.  A fixed middle set is the tail of
\(m^2\) ordered atoms and the head of \(m^2\) ordered atoms, so each of its
two directed loads is

\[
 {m^2\over 2d}={m\over m+1}<1.                      \tag{1.4}
\]

After forgetting orientation, (1.3) is exactly the uniform point of
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`, and
therefore satisfies every graphic inequality.

## 2. Uniformity is an exact barycentre test, not a separating test

### Theorem 2.1 (orbit-barycentre equivalence)

Let \(\mathfrak F_m\) be the family of integral ordered
four-transversals.  Then

\[
 \mathfrak F_m\ne\varnothing
 \quad\Longleftrightarrow\quad
 y^{\rm unif}\in\operatorname {conv}\{1_F:F\in\mathfrak F_m\}. \tag{2.1}
\]

More precisely, the orbit average of any one \(F\in\mathfrak F_m\) under
the full coordinate group \(S_{2m}\) is (1.3).

#### Proof

The group \(S_{2m}\) acts transitively on ordered atoms: a permutation can
send an arbitrary lower set and an ordered pair of outside points to any
other such data.  Every integral four-transversal has

\[
 |\mathcal L|
\]

atoms, whereas the total number of ordered atoms is

\[
 |\mathcal L|\,m(m+1)=|\mathcal L|\,2d.
\]

Consequently every atom has orbit-average incidence \(1/(2d)\).  This
proves the forward implication.  The reverse implication is immediate,
because the convex hull of the empty set is empty. \(\square\)

Thus no coordinate-invariant linear cut can separate the uniform point
from the desired integer hull if the theorem is true.  Additional cuts can
still describe the integer hull, but they will be satisfied by the uniform
point and must control **correlation during rounding**, rather than expose
a fractional capacity deficit.

## 3. A two-parent alternating-circuit rounding theorem

Let \(P_0,P_1\) be perfect matchings of the lower--upper diamond graph.
Fix a total order \(\prec\) on \(\mathcal X\), and orient the physical edge
of every diamond in \(P_0\cup P_1\) from its smaller to its larger endpoint.
The symmetric difference \(P_0\triangle P_1\) is a disjoint union of even
alternating cycles \(C_1,\ldots,C_r\).  A binary variable \(z_i\) chooses
the \(P_0\)-parity or the \(P_1\)-parity on \(C_i\); common edges are
always chosen.

For a candidate atom \(e\in P_0\cup P_1\), let \(s_e\) be the Boolean
literal saying that \(e\) is chosen.  Thus \(s_e\) is true for a common
edge, and is either \(z_i\) or \(\neg z_i\) on \(C_i\).  Form the CNF

\[
 \Phi(P_0,P_1,\prec)=
 \bigwedge_{\substack{e\ne f\\
       \tau(e)=\tau(f)\ \mathrm{or}\ \eta(e)=\eta(f)}}
       (\neg s_e\vee\neg s_f).                       \tag{3.1}
\]

After simplifying constants and repeated literals, (3.1) is a 2-CNF.

### Theorem 3.1 (exact two-parent criterion)

The formula \(\Phi(P_0,P_1,\prec)\) is satisfiable if and only if the
alternating-cycle hull of \(P_0,P_1\) contains a perfect diamond matching
whose \(\prec\)-orientation has injective tail and head maps.  Every such
matching lifts to a spanning linear forest.  Hence satisfiability is a
checkable sufficient condition for an ordered four-transversal.

#### Proof

Choosing one parity independently on every component of
\(P_0\triangle P_1\), together with all common edges, always gives a
perfect lower--upper matching.  Formula (3.1) says exactly that no two
chosen atoms have the same tail or the same head.  This proves the stated
equivalence.

Every chosen arc strictly increases under \(\prec\), so there is no
directed cycle.  Tail and head injectivity give indegree and outdegree at
most one.  If the underlying degree-two graph contained an undirected
cycle, every vertex on it would have one incoming and one outgoing edge,
which would be a directed cycle.  Hence the lift is a linear forest.
\(\square\)

Theorem 3.1 is deliberately a two-parent theorem, not a claim that every
solution lies in such a hull or is monotone for a predetermined order.  It
turns a useful global search target into ordinary implication-graph
reachability: construct two quotient perfect matchings and one order for
which (3.1) has no contradictory strongly connected component.

## 4. Local half-integral circuits of lengths four and six always round

Let

\[
 V_0V_1\cdots V_{2r-1}V_0                         \tag{4.1}
\]

be a simple even cycle in the Johnson graph.  Orient every cycle edge from
its even endpoint to its odd endpoint, and put weight \(1/2\) on every
resulting atom.  The tail and head loads are then exactly one.  Assume also
that every lower and upper colour has total weight at most one.

There are two integral tail--head matchings on (4.1), namely its two
alternating edge sets.

### Lemma 4.1 (colour propagation through a two-edge gap)

Suppose two Johnson edges

\[
 V_iV_{i+1},\qquad V_{i+2}V_{i+3}                 \tag{4.2}
\]

have the same lower colour \(L\).  Then the intervening edge
\(V_{i+1}V_{i+2}\) also has lower colour \(L\).  The dual statement holds
for a repeated upper colour.

#### Proof

All four endpoints in (4.2) contain \(L\).  The adjacent distinct sets
\(V_{i+1},V_{i+2}\) have an intersection of size \(m-1\), and this
intersection contains \(L\), also of size \(m-1\).  Hence their
intersection is \(L\).  Taking unions proves the dual statement. \(\square\)

### Theorem 4.2 (no four- or six-edge parity trap)

If \(r=2\) or \(r=3\), both alternating edge sets in (4.1) have pairwise
distinct lower colours and pairwise distinct upper colours.  In particular
either alternating set is an integral partial ordered four-transversal.

#### Proof

For a four-cycle, two edges in one alternating set are separated by one
edge in either direction.  If they shared a lower colour, Lemma 4.1 would
make at least three (in fact all four) cycle edges have that colour.  Its
half-integral row load would exceed one.  The same argument applies to
upper colours.

For a six-cycle, every pair of edges in one alternating set is separated
by a single intervening edge in one cyclic direction.  Lemma 4.1 again
turns a repeated colour in that alternating set into three occurrences,
of half-integral load \(3/2\), a contradiction.  Thus both palettes are
injective on both alternating sets.  Their physical edges are disjoint
because (4.1) is simple, so they form a matching and hence a forest.
\(\square\)

This is a specifically Boolean/Johnson fact.  The usual abstract
\(2\times2\times2\) parity obstruction cannot occur on four diamond atoms:
the intersection/union labels propagate across the physical square.

### Theorem 4.3 (half-integral cycle rounding is exactly 2-SAT)

Let \(y\) be a half-integral ordered fractional base: all entries lie in
\(\{0,1/2,1\}\), every lower and upper row has load one, and every tail
and head row has load at most one.  Assume:

1. all positive atoms are increasing for one total order on
   \(\mathcal X\);
2. the atoms of weight one have no resource collision; and
3. after removing the weight-one atoms, the tail--head support is a
   disjoint union of simple even cycles, with every remaining edge of
   weight \(1/2\).

Give each support cycle one binary variable choosing one of its two
alternating matchings.  For every pair of half-atoms with a common lower
or a common upper colour, insert the 2-CNF clause forbidding the simultaneous
choice of those two atoms.  Call the resulting formula \(\Psi_y\).

Then \(y\) rounds, within this cycle support, to an ordered
four-transversal if and only if \(\Psi_y\) is satisfiable.

#### Proof

A parity choice on every support cycle selects exactly its half-weighted
mass and automatically uses every tail and every head at most once.  The
clauses of \(\Psi_y\) are exactly the remaining lower- and upper-colour
collisions.  Thus a satisfying assignment selects exactly
\(\sum_e y_e=|\mathcal L|\) atoms while using every lower and upper colour
at most once.  Since there are \(|\mathcal L|=|\mathcal U|\) colours on
each outer shore, both palettes are then used exactly once.  The common
total order excludes directed cycles, and tail/head injectivity turns this
into a physical linear forest as in Theorem 3.1.  Conversely, every
rounding by cycle parities plainly satisfies all the collision clauses.
\(\square\)

Theorem 4.2 says that a four- or six-cycle contributes no unit clause to
\(\Psi_y\): neither of its two parities is internally forbidden.  Different
cycles can still couple through binary clauses.  Section 5 shows that an
octagon can contribute the contradictory pair of unit clauses, killing
both values of one cycle variable.

## 5. The first trap is a literal alternating octagon

The bound in Theorem 4.2 is sharp.  Work at \(m=3\) on \(\Omega=[6]\),
and use concatenation for set notation.  Consider the simple Johnson
octagon

\[
 123,124,246,245,125,126,146,134,123.               \tag{5.1}
\]

Orient each edge from an even-position vertex to an odd-position vertex.
The resulting ordered atoms, with their outer colours, are

\[
\begin{array}{c|c|c|c|c}
i&\tau_i&\eta_i&\lambda_i&\upsilon_i\\ \hline
0&123&124&12&1234\\
1&246&124&24&1246\\
2&246&245&24&2456\\
3&125&245&25&1245\\
4&125&126&12&1256\\
5&146&126&16&1246\\
6&146&134&14&1346\\
7&123&134&13&1234
\end{array}                                          \tag{5.2}
\]

### Theorem 5.1 (alternating-octagon rank cut)

For every integral partial ordered four-transversal \(F\),

\[
                  \sum_{i=0}^7 1_F(e_i)\le3.          \tag{5.3}
\]

On the other hand, the half-integral vector

\[
                         y_{e_i}=1/2                  \tag{5.4}
\]

satisfies every lower, upper, tail and head capacity row, every middle
degree row, and every graphic-forest inequality on its support, while its
left side in (5.3) is four.

#### Proof

The tail--head support in (5.2) is the eight-cycle (5.1), so any four
chosen atoms respecting tail and head capacity must be one of its two
perfect matchings.  The even matching \(\{e_0,e_2,e_4,e_6\}\) repeats
lower colour \(12\).  The odd matching
\(\{e_1,e_3,e_5,e_7\}\) repeats upper colour \(1246\).  Neither is
allowed, proving (5.3).  The three atoms \(e_0,e_2,e_6\) are feasible, so
the rank is exactly three.

For (5.4), every tail and head occurs twice, hence has load one.  The only
repeated lower colours are \(12,24\), and the only repeated upper colours
are \(1234,1246\); each occurs twice and hence has load one.  All other
outer loads are \(1/2\).  Every physical cycle vertex has weighted degree
one.  Finally, for a nonempty vertex set \(S\), the octagon induces at
most \(|S|\) edges, so its half-weight is at most \(|S|/2\le |S|-1\) when
\(|S|\ge2\); for \(|S|=1\) it induces no edge.  These are all the graphic
inequalities. \(\square\)

### Corollary 5.2 (dimension-uniform suspension)

The octagon cut exists literally for every \(m\ge3\).  Partition

\[
 \Omega=C\sqcup A\sqcup R,\qquad |C|=|R|=m-3,\quad |A|=6,    \tag{5.5}
\]

identify \(A\) with \([6]\), and replace every vertex \(V_i\) in (5.1)
by \(C\cup V_i\).  Intersections and unions acquire the same fixed core
\(C\), so the table (5.2), its two opposite-shore parity collisions, and
the rank-three inequality all persist verbatim.  The unused set \(R\)
only completes the ambient ground-set size to \(2m\).

Thus the octagon is not a low-dimensional accident.  It is a suspended
Boolean minor of every ordered four-transversal instance from dimension
three onward.

Inequality (5.3) is the first **simple alternating-cycle
palette-correlation rank cut**.
It is not implied by the hereditary matching/capacity/graphic inequalities
(where outer base equalities are relaxed to capacities during a residual
rounding step).  Theorem 4.2 shows that no simple half-integral physical
cycle on four or six atoms can supply such a cut.

This statement is carefully scoped.  The local half-vector (5.4) is not
claimed to extend to a full fractional base with every outer equality, and
(5.3) does not cut the global uniform point.  Indeed Theorem 2.1 says that
the uniform point must satisfy every valid inequality whenever one global
solution exists.  The octagon instead identifies the first correlation of
this alternating-cycle type that an integral residual/absorption argument
must control.

There are smaller cuts outside this restricted class.  In particular,
`THREAD_A_CATALAN_ORDERED_FOUR_TRANSVERSAL_CONFLICT_ROUNDING_AND_MINIMAL_CUT_20260731.md`
contains a three-atom non-Helly oriented clique and a two-column unoriented
reciprocal-completion cut.  Neither is a half-integral simple tail--head
cycle trap, so there is no conflict with Theorem 4.2 or the scoped
minimality asserted here.

## 6. Consequence for the global quotient lane

The globally chosen quotient perfect matching removes the exceptional
filter-extension Hall problem, but it does not control the four occurrence
roles simultaneously.  Theorems 4.2 and 5.1 sharpen the remaining boundary:

* Boolean squares and six-cycles are automatically safe for half-integral
  palette rounding;
* the first possible simple alternating-cycle failure is an octagon whose two
  parities are killed on opposite outer shores;
* therefore any circuit-rounding proof must either exclude these octagons,
  absorb them into a larger alternating circuit, or add their rank cuts;
* a concrete positive route is Theorem 3.1: find two global quotient
  perfect matchings whose ordered alternating-cycle hull has satisfiable
  collision 2-CNF for some middle order.

The P4 exceptional packets of
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_PACKET_AND_NEUTRAL_CONNECTOR_20260731.md`
lie below the first obstruction size, consistent with their exact local
integrality.  Their completion can nevertheless create octagons through
nonexceptional parent interactions.  Controlling precisely those
opposite-shore parity traps is the smallest additional integral task found
here.

## 7. Audit boundary

All arguments are symbolic.  No finite search and no claim about the
retracted Greene--Kleitman \(W/2\) projection bound is used.  The explicit
octagon is checked directly in (5.2).  The result neither proves nor
refutes the Catalan Linear Matching Theorem; it proves a checkable
two-parent sufficient condition and a support-minimal alternating-cycle
correlation obstruction.
