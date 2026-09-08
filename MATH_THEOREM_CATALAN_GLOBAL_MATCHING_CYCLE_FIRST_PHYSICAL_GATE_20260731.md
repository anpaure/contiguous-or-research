# Global quotient matching reduces the physical problem to one coloured unit-voltage cycle

Date: 2026-07-31  
Status: solver-independent equivalence and exact finite formulation; no
all-\(m\) cycle construction

## 1. Quotient objects

Fix \(m\ge2\), and let

\[
 {\cal L}=\binom{\Omega}{m-1},\qquad
 {\cal M}=\binom{\Omega}{m},\qquad
 {\cal U}=\binom{\Omega}{m+1},
\]

where \(|\Omega|=2m\), and put

\[
 K=\operatorname{Cat}_m,\qquad N=mK,\qquad M=(m+1)K.
                                                               \tag{1.1}
\]

Let a cyclic group \(H\cong\mathbb Z_h\) act on \(\Omega\), with its
induced actions free on all three families.  Write bars for
\(H\)-orbits.  Thus

\[
 |\bar{\cal L}|=|\bar{\cal U}|=N/h,\qquad
 |\bar{\cal M}|=M/h.                                   \tag{1.2}
\]

The quotient diamond multigraph \(\bar{\cal B}\) has shores
\(\bar{\cal L},\bar{\cal U}\).  Every occurrence-labelled inclusion
\(L\subset U\) corresponds to the Johnson edge

\[
 \psi(L,U)=
 \{L\cup\{x\},L\cup\{y\}\},\qquad U\setminus L=\{x,y\}. \tag{1.3}
\]

This is an \(H\)-equivariant bijection, so it remains a bijection between
edges of \(\bar{\cal B}\)—that is, \(H\)-edge orbits upstairs—and
occurrence-labelled edges of the quotient Johnson multigraph \(\bar J\).
Parallel quotient records are retained.

By
MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md,
\(\bar{\cal B}\) is balanced regular and therefore has a perfect matching.
The period-three exceptional filters should be read from the restriction
of such a global matching, not prescribed before it.

## 2. The cycle-first equivalence

Let \(\bar C\) be a connected spanning two-regular occurrence submultigraph
of \(\bar J\), using each quotient edge record at most once.  Call this one
spanning occurrence cycle.  A loop contributes two to degree and a
parallel two-cycle is allowed; in the present Boolean parameters
\(|\bar{\cal M}|\ge2\), so a connected spanning \(\bar C\) is loopless.
The physical developed edges must remain distinct.  For every
\(e\in E(\bar C)\), let

\[
 \ell(e)\in\bar{\cal L},\qquad u(e)\in\bar{\cal U}
                                                               \tag{2.1}
\]

be its intersection and union colour orbits.  Define the bipartite
colour-incidence multigraph \(G(\bar C)\) with shores
\(\bar{\cal L},\bar{\cal U}\) and one occurrence edge
\(\ell(e)u(e)\) for every \(e\in E(\bar C)\).

### Theorem 1 (cycle-first common-transversal equivalence)

The following are equivalent.

1. \(G(\bar C)\) has a perfect matching.
2. \(\bar C\) contains an exact quotient common transversal
   \(\bar F\): lower and upper colours are both bijective on \(\bar F\).
3. \(\bar C\) contains a spanning quotient linear forest \(\bar F\) whose
   physical \(H\)-lift is an exact common transversal.

Whenever these conditions hold:

* \(|\bar F|=N/h\);
* \(\bar F\) has exactly \(K/h\) path components, with isolated vertices
  allowed;
* \(\bar D=E(\bar C)\setminus\bar F\) has exactly \(K/h\) edges; and
* after contracting the paths of \(\bar F\), the occurrence edges
  \(\bar D\) form the same one-cycle transition as \(\bar C\).

#### Proof

The correspondence (1.3) identifies a matching edge of
\(G(\bar C)\) with one literal quotient Johnson edge.  A perfect matching
therefore selects one edge for every lower colour and one for every upper
colour, proving \(1\Longleftrightarrow2\).

A spanning cycle has \(M/h\) vertices and edges.  A perfect matching of
the colour-incidence graph selects \(N/h<M/h\) of those cycle edges.
Every proper edge subset of one cycle is a spanning linear forest when
unused vertices are retained as isolated paths.  Hence \(2\Rightarrow3\).
Clean-group freeness makes the lifted colour maps bijective.

Conversely, an exact common transversal contained in \(\bar C\) selects a
perfect matching in \(G(\bar C)\), giving \(3\Rightarrow1\).
Finally,

\[
 |V(\bar C)|-|\bar F|=(M-N)/h=K/h,                    \tag{2.2}
\]

so the forest has \(K/h\) components and its complement has \(K/h\)
edges.  Reading the original cyclic order shows that those complementary
occurrences join the maximal forest runs cyclically. \(\square\)

### Theorem 2 (physical closure)

Orient \(\bar C\) and let \(v(\bar C)\in\mathbb Z_h\) be its total
voltage.  Under literal free development,

\[
 \text{the lift of }\bar C\text{ is Hamiltonian}
 \quad\Longleftrightarrow\quad
 \gcd(h,v(\bar C))=1.                                  \tag{2.3}
\]

Consequently, within the free \(H\)-invariant fibre, a physical Hamilton
cycle together with an \(H\)-invariant exact common transversal is
equivalent to:

\[
 \boxed{\bar C\text{ spanning and one-cycle},\quad
        G(\bar C)\text{ has a perfect matching},\quad
        \gcd(h,v(\bar C))=1.}                          \tag{2.4}
\]

#### Proof

One traversal of \(\bar C\) translates the fibre coordinate by
\(v(\bar C)\).  Its number of lifted cycle components is
\(\gcd(h,v(\bar C))\).  Apply Theorem 1 to the perfect matching
\(\bar F\); its complement is already the required endpoint connector
system. \(\square\)

Theorem 2 is the promised simplification.  There is no separate
filter-extension problem and no filter-to-connector assignment.  Filters
are internal edges of the matching \(\bar F\); connector occurrences are
the \(K/h\) edges of \(\bar C\setminus\bar F\).

## 3. Exceptional filters are automatic

Put

\[
 q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,
\]

and take the maximal clean group \(H=\langle s\rangle\).
If \(q=6a+3\) and \(v_3(q)=1\), the restriction of the perfect matching
\(\bar F\) in Theorem 1 to the exceptional lower and upper quotient banks
has exactly

\[
                         2\operatorname{Cat}_a         \tag{3.1}
\]

edge orbits.  It services every exceptional colour exactly once, uses
distinct opposite-shore colours on each typed physical shore, and has
pairwise-disjoint middle
endpoints.  Each selected clean orbit is one third of a free
full-rotation edge orbit.

No cross-family distinctness is asserted after the auxiliary operation
which complement-identifies the two typed shores.

These statements follow from the global quotient matching theorem cited
in Section 1.  They do not identify any connector in
\(\bar C\setminus\bar F\) with an exceptional colour.  At higher
three-adic order, one exceptional full-rotation colour orbit splits into
\(s/3\) clean-\(H\) colour orbits; phase consolidation into a smallest
number of full-rotation edge orbits is a separate question and is not
claimed here.

## 4. Exact finite formulations

### 4.1 Cycle first

For a fixed candidate \(\bar C\), the only colour gate is Hall:

\[
 |N_{G(\bar C)}(X)|\ge |X|
 \qquad(X\subseteq\bar{\cal L}).                       \tag{4.1}
\]

If \(G(\bar C)\) has maximum degree at most two, it is a disjoint union of
paths and even cycles.  Then (4.1) is equivalent to every path component
having the same number of lower and upper vertices; cycle components are
automatically balanced.  The matching on a balanced path is forced by
leaf peeling.

### 4.2 Joint selector

For an exact joint model, let binary \(z_e\) select each undirected
occurrence-labelled edge record of \(\bar J\), let binary
\(y_{e,+},y_{e,-}\) choose its orientation, and let binary
\(x_e\le z_e\) select the common transversal.  Impose

\[
 y_{e,+}+y_{e,-}=z_e,\qquad
 \sum_{\operatorname{tail}(a)=v}y_a
 =\sum_{\operatorname{head}(a)=v}y_a=1
 \quad(v\in\bar{\cal M}),                              \tag{4.2}
\]

and the directed subtour rows

\[
 \sum_{\substack{\operatorname{tail}(a)\in W\\
                  \operatorname{head}(a)\notin W}}y_a\ge1
 \quad(\varnothing\ne W\subsetneq\bar{\cal M}).        \tag{4.3}
\]

These rows select one consistently oriented occurrence cycle.  The colour
rows are

\[
 \sum_{\ell(e)=L}x_e=1,\qquad
 \sum_{u(e)=U}x_e=1,                                  \tag{4.4}
\]

for all lower and upper quotient colours.  If
\(\delta_a\in\mathbb Z_h\) is the gain of directed arc \(a\), the exact
voltage row for \(h>1\) is

\[
 \sum_a\delta_a y_a
 =ht+\sum_{r\in\mathbb Z_h^\times}r\,b_r,\qquad
 \sum_{r\in\mathbb Z_h^\times}b_r=1,                  \tag{4.5}
\]

with integral \(t\) and binary \(b_r\); for \(h=1\) it is vacuous.
Selected physical edge orbits must be distinct and literal.  This model
has no fixed filter variables: exceptional service is a consequence of
(4.4).

The matching-first alternative selects a perfect matching of
\(\bar{\cal B}\) and adds middle-degree and graphic-forest cuts.  It becomes
equivalent only after adding literal endpoint connectors, one-cycle rows,
physical-orbit distinctness and primitive voltage.  Once a candidate
\(\bar C\) is supplied, the cycle-first form absorbs the degree and graphic
cuts and leaves the bipartite matching test (4.1).

### 4.3 Private physical resources

If the recursive filter architecture requires a protected local socket,
collar, or host for an exceptional matching edge, that remains a separate
literal resource condition.  For each selected exceptional occurrence
\(a\), let \(w_{a,s,\theta}\) choose one compatible phase-labelled private
resource record.  The exact rows are

\[
 \sum_{s,\theta}w_{a,s,\theta}=x_a
 \quad(a\text{ an exceptional candidate occurrence}),\qquad
 \sum_{a,\theta}w_{a,s,\theta}\le1,                   \tag{4.6}
\]

together with compatibility rows forbidding nonexistent
\((a,s,\theta)\) records and capacity one on every physical endpoint,
collar, colour, and guard consumed by the records.  These resources need not be edges of
\(\bar C\setminus\bar F\), and there is no exceptional-colour-to-connector
bijection.  In the paired-\(P_4\) specialization the native socket is an
ordered zero-voltage square subdivision; in a general global matching it
must be certified from the literal atom catalogue.

Thus global quotient Hall removes preassigned exceptional-filter
extension, not the fixed-cycle Hall test (4.1) or private-resource
compatibility.

## 5. Two sharp scope warnings

For any physical global diamond matching \(F\), let \(d_F(v)\) be the
degree of a middle vertex in its Johnson lift and put

\[
 O(F)=\sum_v(d_F(v)-2)_+,\qquad
 D(F)=\sum_v(2-d_F(v))_+.
\]

Since \(\sum_vd_F(v)=2N\),

\[
                         D(F)-O(F)=2(M-N)=2K.          \tag{5.1}
\]

Thus a degree-cap matching has exactly \(2K\) endpoint-deficit units.  If
all degrees are at most two, its graph is a disjoint union of paths and
cycles, and the number of path components is exactly \(M-N=K\);
acyclicity is the sole remaining topology condition.

Nevertheless, a global quotient perfect matching alone need not have a linear
Johnson lift.  The deterministic \(m=8,H=\mathbb Z_5\) matching used by
the finite audit has middle-degree histogram

\[
 0^{805}1^{3890}2^{5860}3^{2000}4^{305}5^{10},        \tag{5.2}
\]

overload \(2640\), and cyclomatic number \(331\).  Thus regular quotient
Hall solves palette extension but not the physical gate.

Second, complementation does not supply a connector:

\[
 d_{J(2m,m)}(X,X^c)=m>1.                              \tag{5.3}
\]

The paired-\(P_4\) construction in
MATH_THEOREM_CATALAN_PERIOD3_FILTER_PACKET_AND_NEUTRAL_CONNECTOR_20260731.md
is an optional stronger face.  Its native socket is a literal Johnson edge
and its square subdivision is voltage-neutral, but neither that packet
face nor one socket per exceptional colour is required by Theorem 2.

## 6. Carrier/compiler separation

Theorems 1--2 concern the middle carrier and its common outer-colour
transversal.  They impose no equivariance on a later common-cap compiler.
The authenticated K16 optimum illustrates the distinction: four strict
spirals are opened and joined by three Johnson connectors; the four
symmetry defects do not correspond one-for-one to shortened colour orbits,
and the final compiler strongly breaks \(H\).

Accordingly the remaining immediate common-transversal theorem is exactly
the existence of a spanning quotient Johnson occurrence cycle satisfying
(2.4).  A recursive physical-filter construction must additionally satisfy
the declared private-resource rows (4.6).  Residence, deeper shadows,
boundary conditions and common-cap compilation remain further literal
gates.  No unrestricted all-\(m\) existence claim is made here.

## 7. Finite replay

Run

    python3 scratch/audit_catalan_global_matching_cycle_first_gate_20260731.py

The audit independently reconstructs the deterministic \(m=8\) quotient
matching and the nonlinearity profile (5.2).  It also replays both kernel
choices of the authenticated \(m=4,\mathbb Z_7\) fixture: in each case a
ten-edge quotient cycle of voltage \(2\) contains an eight-edge
colour-incidence perfect matching, and its physical lift is the
seventy-vertex Hamilton cycle with a fifty-six-edge common transversal.
