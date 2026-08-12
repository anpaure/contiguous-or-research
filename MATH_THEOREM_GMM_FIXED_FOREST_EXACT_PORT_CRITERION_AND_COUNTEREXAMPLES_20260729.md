# GMM fixed-forest splicing: an exact port criterion and two tightness counterexamples

Date: 2026-07-29

Status: pure mathematics.  This note gives a necessary-and-sufficient
criterion for the **direct-jump specialization** of the two-GMM-forest
construction.  It also gives explicit tight enumerations showing that GMM
tightness alone supplies neither the required lower-colour injection nor
residence.  It does not claim a new contiguous-OR word or an all-parameter
existence theorem.

The point of the note is to separate three logically different questions:

1. which direct B-jumps must be removed for exact lower ownership;
2. whether the resulting A and B ports admit the required containment
   matching; and
3. whether the matched components can be oriented and spliced with the
   required residence.

Only the second question is Hall.  The first and third are genuine extra
conditions, and neither follows from the numerical forest census.

## 1. The two projected tight enumerations

Assume \(m\ge2\), and let

\[
 \Omega=[2m],\qquad
 W=\binom{2m}{m},\qquad
 C=\frac{W}{m+1}=\operatorname{Cat}_m,
\]

and put

\[
 L=\binom{2m}{m+1}=mC,
 \qquad
 U=\binom{2m}{m+2},
 \qquad
 D=L-U=\frac{3m}{m+2}C.
\]

Fix two tight enumerations and contract them as in the GMM two-level
projection theorem.

* The lower enumeration gives a Hamilton cycle \(H_A\) of
  \(J(2m,m)\).  Its marked edge set \(F_A\) has \(L\) edges, one for every
  rank-\((m-1)\) intersection colour.  The remaining direct edges
  \(J_A=E(H_A)\setminus F_A\) have cardinality \(C\).
* The upper enumeration gives a Hamilton cycle \(H_B\) of
  \(J(2m,m+1)\).  Its marked edge set \(F_B\) has \(U\) edges, one for
  every rank-\((m+2)\) union colour.  The remaining direct edges
  \(J_B=E(H_B)\setminus F_B\) have cardinality \(D\).

Deleting \(J_A\) leaves the canonical A path forest.  To obtain the same
number \(C\) of B paths, choose a set

\[
                         R\subseteq J_B,\qquad |R|=C,
\tag{1.1}
\]

and use the B path forest \(H_B-R\).  Equivalently, retain \(D-C\) of the
direct B-jumps.

For an edge \(e\) of \(H_B\), write

\[
                         \lambda(e)=\bigcap e\in\binom\Omega m.
\tag{1.2}
\]

Let \(P_A\) be the multiset of endpoint owners of the deleted A-jumps
\(J_A\), and let \(P_B(R)\) be the multiset of endpoint owners of the
deleted B-jumps \(R\).  The two occurrences at an isolated path vertex are
regarded as distinct port copies.

Finally, let

\[
 \mathcal U_A=\{T\cup T':TT'\in F_A\}
 \subseteq\binom\Omega{m+1},
 \qquad
 Q_A=\binom\Omega{m+1}\setminus\mathcal U_A.
\tag{1.3}
\]

Thus \(Q_A\) is exactly the z-upper deck that the cross edges must repair.

## 2. Exact elimination of the lower-colour condition

For \(t\in\binom\Omega m\), define

\[
 p_t=|\{e\in F_B:\lambda(e)=t\}|,
 \qquad
 j_t=|\{e\in J_B:\lambda(e)=t\}|.
\tag{2.1}
\]

Assume first that the physical owners in \(P_A\) are distinct.  This is
equivalent to saying that no two direct A-jumps are consecutive in the
cycle \(H_A\).  A cross edge incident with the A port \(t\) has lower
colour exactly \(t\).  Hence the cross channel contributes the indicator
of \(P_A\), independently of how its ports are matched on the B side.

### Lemma 2.1 (per-colour deletion equation)

The no-z lower deck is exact after deleting \(R\) if and only if, for every
rank-m target \(t\),

\[
 |\{e\in R:\lambda(e)=t\}|
   =p_t+j_t-\bigl(1-\mathbf1_{t\in P_A}\bigr).
\tag{2.2}
\]

Consequently a lower-exact deletion can exist only if

\[
 p_t\le 1-\mathbf1_{t\in P_A}\le p_t+j_t
 \qquad(t\in\tbinom\Omega m).
\tag{2.3}
\]

When (2.3) holds, the right side of (2.2) is an integer between zero and
\(j_t\), and its sum over all colours is automatically \(C\).

#### Proof

The retained B edges contribute \(p_t+j_t-|R\cap\lambda^{-1}(t)|\)
copies of \(t\).  The cross channel contributes one additional copy if
and only if \(t\in P_A\).  Requiring their sum to be one gives (2.2).
Because only direct edges may be deleted, the right side must lie between
zero and \(j_t\), which is precisely (2.3).

For the final assertion, sum (2.2).  The full B cycle has \(L\) edges and
the desired retained lower support has size \(W-2C\).  Therefore

\[
 \sum_t |R\cap\lambda^{-1}(t)|
 =L-(W-2C)=mC-(m+1)C+2C=C.
\]

This is (1.1). \(\square\)

The inequalities have a particularly transparent form.

* If \(t\in P_A\), then necessarily \(p_t=0\), and **all** direct B-edges
  of colour \(t\) must be deleted.
* If \(t\notin P_A\) and \(p_t=1\), all direct edges of colour \(t\) must
  be deleted.
* If \(t\notin P_A\) and \(p_t=0\), at least one direct edge of colour
  \(t\) must exist and exactly one must be retained.

In particular the protected marked B edges must have pairwise distinct
intersection colours, and none may have a colour in \(P_A\).  This is a
second-rainbow property; it is not part of the tight-enumeration theorem.

## 3. The exact fixed-forest splice criterion

For a chosen \(R\), form the bipartite port graph

\[
 G_R=(P_A,P_B(R);E_R),
 \qquad
 tV\in E_R\quad\Longleftrightarrow\quad t\subset V.
\tag{3.1}
\]

Both shores consist of port copies.  Thus two copies based at one isolated
B owner are distinct right vertices of \(G_R\).

### Theorem 3.1 (necessary and sufficient direct-jump criterion)

There is a two-sector q1-exact spanning 2-factor using

\[
 \{z\}+F_A,\qquad H_B-R,
\]

and cross edges only at their ports if and only if all of the following
hold.

1. The A port owners are distinct.
2. The per-colour equations (2.2) hold.
3. Every missing z-upper target is exposed as a B port:

   \[
                            Q_A\subseteq\operatorname{supp}P_B(R).
   \tag{3.2}
   \]

4. The containment graph satisfies Hall:

   \[
   |N_{G_R}(S)|\ge |S|\qquad(S\subseteq P_A).
   \tag{3.3}
   \]

Every perfect matching certified by (3.3) gives such a 2-factor.  It is a
single Hamilton cycle if and only if the component quotient produced by
that matching is connected.

#### Proof

Deleting \(C\) edges from each Hamilton cycle leaves \(C\) A paths and
\(C\) B paths, with \(2C\) port copies on each shore.  A legal cross
completion is therefore exactly a perfect matching of (3.1).  Hall's
theorem gives (3.3).

Every path-internal vertex already has degree two and every path port has
degree one.  Adding a perfect port matching makes every middle owner have
degree two, so the result is a spanning 2-factor.  Lemma 2.1 proves exact
no-z lower ownership.  The A marked edges already give the z-containing
lower deck exactly once.  The marked B edges already cover every no-z
upper target.  An A edge supplies z-upper colour \(z+(T\cup T')\), while a
cross edge ending at \(V\) supplies z-upper colour \(z+V\).  Thus (3.2) is
exactly the remaining upper-cover condition.

Conversely, any restricted completion uses every port once and hence is a
perfect matching of (3.1).  Its exact lower deck forces distinct A labels
and (2.2), and its z-upper cover forces (3.2).  Finally, a finite 2-regular
graph is one cycle exactly when it is connected. \(\square\)

This theorem replaces a simultaneous edge-colour statement by one
per-colour equality followed by one honest Hall condition.  It is also
sharp: none of conditions 1--4 follows from the cardinalities alone.

### Corollary 3.2 (the upper-hole edge-cover test)

For \(V\in Q_A\), let \(I_J(V)\) be the set of direct B-jumps incident
with the corresponding physical B owner.  Condition (3.2) is exactly

\[
                      R\cap I_J(V)\ne\varnothing
                      \qquad(V\in Q_A).
\tag{3.4}
\]

If the marked B forest has no singleton component, every eligible B port
owner is incident with a unique direct jump.  Let \(R_Q\) be the set of
direct jumps thereby forced by \(Q_A\).  Put

\[
 r_t=p_t+j_t-\bigl(1-\mathbf1_{t\in P_A}\bigr).
\]

Then (2.2) and (3.2) have a common solution \(R\) if and only if

\[
 Q_A\text{ consists of eligible port owners},
 \qquad
 |R_Q\cap\lambda^{-1}(t)|\le r_t\le j_t
 \quad\text{for every }t.
\tag{3.5}
\]

#### Proof

Equation (3.4) is the definition of becoming an endpoint after deleting
direct jumps.  Without singleton components, a port owner lies on exactly
one direct jump, so every member of \(Q_A\) forces that jump.  Necessity of
(3.5) is immediate.  Conversely, after taking all forced jumps, add
arbitrary jumps of colour \(t\) until exactly \(r_t\) have been selected.
The upper bounds in (3.5) make this possible independently in every colour
class.  Lemma 2.1 shows that the resulting set has total size \(C\). \(\square\)

Thus, before Hall is even asked, the fixed construction has an exact
partition-quota/edge-cover test.

## 4. Hall is critical, not supplied by density

The containment graph between the full rank-m and rank-\((m+1)\) levels is
biregular.  A fixed rank-m set has \(m\) supersets and
\(|\binom\Omega{m+1}|=L=mC\).  Therefore, for arbitrary fixed port sets of
size \(2C\) and a uniformly random relabelling \(\pi\) of the B shore,

\[
 \Pr[t\subseteq\pi(V)]=\frac{m}{L}=\frac1C,
\]

and hence

\[
 \mathbb E_\pi |E(P_A,\pi P_B)|
   =\frac{(2C)^2}{C}=4C.
\tag{4.1}
\]

The expected degree is exactly two.  There is no density margin from which
a generic Hall theorem could follow.

There is, however, a useful deterministic certificate.

### Lemma 4.1 (balanced-degree Hall certificate)

If an integer \(s\ge1\) satisfies

\[
 \deg_{G_R}(t)\ge s\quad(t\in P_A),
 \qquad
 \deg_{G_R}(V)\le s\quad(V\in P_B(R)),
\tag{4.2}
\]

then \(G_R\) has a perfect matching.

#### Proof

For every \(S\subseteq P_A\),

\[
 s|S|\le e(S,N(S))\le s|N(S)|.
\]

Hence \(|N(S)|\ge|S|\), and Hall applies. \(\square\)

The natural critical case is \(s=2\).  In that case equality throughout
makes the port graph a union of even cycles, and either alternating edge
class is a perfect matching.

Counts alone do not imply even the absence of isolated ports.  For
\(m=3\), let

\[
 P_A=\{012,013,014,015,023,024,025,034,035,045\}
\]

and

\[
 P_B=\{0134,0135,0145,0234,0235,0245,0345,1234,1235,1245\}.
\]

Both have the required size \(2C=10\), but the port \(012\) has no
neighbour in \(P_B\).  This example is only a count-level counterexample;
it is not asserted to arise from a pair of tight enumerations.

## 5. Tightness itself can violate the protected lower rainbow

Before giving the counterexample, it is useful to record that the desired
two-colour edge decks have no **static** Hall obstruction.  Their missing
property is owner-degree/chronology compatibility.

### Proposition 5.1 (static doubly-rainbow decks exist)

There exist edge sets with the following properties.

1. An AA edge set of size \(L\) in \(J(2m,m)\) whose intersection colours
   are all rank-\((m-1)\) sets and whose union colours are all
   rank-\((m+1)\) sets, each exactly once.
2. A BB edge set of size \(U\) in \(J(2m,m+1)\) whose union colours are
   all rank-\((m+2)\) sets exactly once and whose rank-m intersection
   colours are pairwise distinct.

#### Proof

For (1), consider the containment graph between ranks \(m-1\) and \(m+1\).
Its shores have the same size \(L\), and it is regular of degree
\(\binom{m+1}{2}\).  Hence it has a perfect matching.  A matched pair
\(X\subset V\), with \(V\setminus X=\{a,b\}\), defines the unique Johnson
edge

\[
                         (X+a)(X+b).
\]

Its intersection is \(X\) and its union is \(V\).  The perfect matching
therefore gives the first edge set.

For (2), use the containment graph with left shore
\(\binom\Omega{m+2}\) and right shore \(\binom\Omega m\).  A left vertex
has degree \(\binom{m+2}{2}\), while a right vertex has degree
\(\binom m2\).  For every family \(\mathcal S\) on the left, edge counting
gives

\[
 \binom{m+2}{2}|\mathcal S|
 \le \binom m2|N(\mathcal S)|,
\]

so \(|N(\mathcal S)|\ge|\mathcal S|\).  Hall gives an injection
\(V\mapsto t\subset V\).  Writing \(V\setminus t=\{a,b\}\), take the edge

\[
                         (t+a)(t+b)
\]

of \(J(2m,m+1)\).  It has intersection \(t\) and union \(V\), proving the
second claim. \(\square\)

The proposition does **not** bound the degree of a middle owner in the
selected edge set.  Turning either deck into a spanning linear forest, and
coupling the two forests through ports, is precisely the additional
problem.  In particular, the counterexample below refutes an implication
from arbitrary GMM tightness, not the existence of a suitably designed
second-rainbow forest.

The next example *does* come from a valid tight enumeration.

Take \(m=3\), \(\Omega=\{0,1,2,3,4,5\}\), and identify a rank-four B
owner with the complementary pair: \(B_{ab}=\Omega\setminus\{a,b\}\).
The following is a Hamilton cycle of \(J(6,2)\), hence also of
\(J(6,4)\):

\[
 02,01,12,13,03,23,24,04,14,34,35,05,15,45,25.
\tag{5.1}
\]

Mark the six cycle edges

\[
 02\!-\!01,\quad 01\!-\!12,\quad 23\!-\!24,\quad
 13\!-\!03,\quad 24\!-\!04,\quad 35\!-\!05.
\tag{5.2}
\]

Their common pair-coordinates are respectively \(0,1,2,3,4,5\).  Insert
the rank-five set \(\Omega\setminus\{c\}\) between the endpoints of the
edge with common coordinate \(c\).  This lists all fifteen rank-four sets
and all six rank-five sets exactly once.  Every inserted transition has
Hamming length one and every remaining direct transition has length two,
so the cyclic length is

\[
                         2\cdot15=30
   =(15+6)+(15-6).
\]

It is therefore a tight enumeration of levels four and five.

However, the first two marked B edges have the same intersection colour:

\[
 B_{02}\cap B_{01}
 =\{3,4,5\}
 =B_{01}\cap B_{12}.
\tag{5.3}
\]

Thus \(p_{345}=2\), contradicting (2.3) for every possible A port set.
No choice of direct-jump deletions, path orientations, or cross matching
can make this particular pair-of-forests construction lower-exact.

This proves that the missing protected lower rainbow is not a technical
consequence omitted from the proof of GMM tightness.  A coupled theorem
must select a special tight enumeration.

## 6. Tightness itself can violate residence and port distinctness

There is an even smaller example.  Take \(m=2\), \(\Omega=\{0,1,2,3\}\),
and the Hamilton cycle

\[
                         01,02,12,13,23,03
\tag{6.1}
\]

of \(J(4,2)\).  Mark its first four edges.  Their intersection colours are
\(0,2,1,3\), exactly the rank-one deck.  Insert those four singletons
between the corresponding owners.  The resulting enumeration lists all
six rank-two and all four rank-one sets, and has length

\[
                         4\cdot2+2\cdot2=12
   =(6+4)+(6-4).
\]

Hence it is tight.

The two unmarked direct edges are \(23-03\) and \(03-01\).  Deleting them
leaves one five-vertex marked path and the isolated vertex \(03\).  Thus:

* the A component sizes are \(5,1\), so every residence requirement at
  least two fails; and
* the owner \(03\) occurs twice in the A port multiset, so exact no-z lower
  ownership is already impossible.

For a general lower tight enumeration, the A component sizes sum to \(W\)
over \(C\) components, so their average is exactly

\[
                              \frac WC=m+1.
\tag{6.2}
\]

The required depth in the contiguous-OR application is much smaller than
this average, but the example shows that tightness supplies no minimum-gap
statement.  Reversing or reorienting a component cannot change its size.

## 7. Exact residence interface after the port matching

The distinguished coordinate is simple: its runs are precisely the A
components.  Thus its residence is equivalent to a lower bound on every A
component size.

The old coordinates have a separate exact boundary condition.  The
following elementary form is useful because it shows precisely what path
orientation can and cannot repair.

### Proposition 7.1 (boundary-fragment residence criterion)

Fix a coordinate \(x\) and a collection of vertex-disjoint owner paths.
For each oriented path record:

* every maximal internal x-run which meets neither endpoint;
* every maximal boundary x-run, its length, and which of the two path
  ports it meets.  In particular, an all-one path contributes one boundary
  run incident with both ports, not two copies of the same run.

After the paths are joined by external Johnson edges, the final maximal
x-runs are exactly:

1. the unchanged internal runs; and
2. sums of the boundary-run lengths in the connected components obtained
   by joining two boundary-run nodes precisely when the corresponding
   external edge has \(x\) in both endpoint owners.

Consequently residence at least \(h\) holds if and only if every run in
this list has length at least \(h\).

#### Proof

Write the membership of \(x\) along every path as a binary word, and make
one node for each maximal 1-run that touches a path port.  Label that node
by its length and by the one or two ports it touches.  An internal 1-run
cannot meet an external edge and is unchanged.  At a join, the incident
boundary runs concatenate exactly when both endpoint bits are one;
otherwise the join contains a 0 on at least one side and no 1-run crosses
it.  Hence the maximal 1-runs in the glued word are exactly the internal
runs and the connected components of this boundary-run graph.  Summing
node lengths once in each component proves the statement, including the
all-one-path case. \(\square\)

Reorienting a path only swaps the port incidences of its boundary runs.  It
does not alter an internal short run, any colour multiset, the port owners,
the upper-hole set, or the Hall graph.  Thus orientation is relevant only
after conditions (2.2), (3.2), and (3.3) have been met.

For fixed residence threshold \(h\), Proposition 7.1 is a finite capped
state problem: replace every boundary length by \(\min(h,\ell)\).  This is
an exact automaton interface, not a probabilistic estimate.

## 8. The remaining all-parameter theorem, stated without hidden steps

The fixed two-forest route would be completed by a **coupled tight
enumeration theorem** producing \(H_A,H_B\) and a deletion set
\(R\subseteq J_B\) for which:

1. the direct A-jumps are nonconsecutive and separated far enough for the
   distinguished-coordinate residence;
2. the exact colour quotas (2.2) are feasible;
3. the forced upper-hole edge cover (3.2) is feasible;
4. the induced port graph satisfies the exact Hall cuts (3.3); and
5. some perfect matching and path orientation satisfy Proposition 7.1
   for every old coordinate, as well as the deeper compiler constraints.

The explicit examples in Sections 5 and 6 show that items 1 and 2 cannot
be removed or inferred from GMM tightness.  Section 4 shows that item 4 is
critical: under unrelated relabelling the mean port degree is exactly two,
not a growing quantity.

Therefore the smallest exact inequality **after** compatible forests and
the forced B-jump deletion have been chosen is Hall's condition (3.3).
Before that stage there is a strictly earlier, pointwise obstruction:

\[
                         p_t\le 1-\mathbf1_{t\in P_A}
                         \qquad\text{for every }t,
\tag{8.1}
\]

together with the corresponding direct-edge supply in (2.3).  The
dimension-six tight enumeration (5.1)--(5.3) violates (8.1) outright.

This is the exact stopping point of the two-independent-GMM-forests
argument.  Any positive theorem must correlate the choice of the two tight
enumerations; path orientation alone cannot supply that correlation.
