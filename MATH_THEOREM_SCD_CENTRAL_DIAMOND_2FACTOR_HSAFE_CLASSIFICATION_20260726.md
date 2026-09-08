# SCD central diamonds: exact two-factor, safety, and reset obstructions

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

Audit note: the decisive spacing, parity, and Hall steps were checked
independently.  The audit exposed and corrected two scope points: the
endpoint \(g^q(X)=G_q(X)\) must be included in rooted flag propagation,
and residual radius \(q-t\) is a stronger hereditary condition rather than
part of ordinary rooted propagation.  Proposition 4.2 is explicitly scoped
to a fixed retained-source choice.

## 0. Verdict

Let \(\mathscr S\) be a symmetric-chain decomposition of
\(2^{[2m]}\), and let \(\mathcal M=\binom{[2m]}m\).  If the chain through
\(X\in\mathcal M\) has positive radius, write its central triple as

\[
 R_X\subset X\subset U_X,
 \qquad |R_X|=m-1,\quad |U_X|=m+1,
\]

and put

\[
 \alpha_X=X\setminus R_X,qquad
 \beta_X=U_X\setminus X,qquad
 g(X)=X-\alpha_X+\beta_X.
 \tag{0.1}
\]

Thus \(g(X)\) is the other middle vertex of the Boolean diamond
\([R_X,U_X]\).  The exact conclusions are as follows.

1. The map \(g\) is only a partial map.  Its domain \(\mathcal A\), the
   positive-radius middle centers, has size

   \[
   N_1=\binom{2m}{m-1},
   \]

   and the radius-zero leave has the exact Catalan size

   \[
   D=W-N_1=\frac{W}{m+1}=\operatorname {Cat}_m,
   \qquad W=\binom{2m}m.
   \tag{0.2}
   \]

2. The central-diamond edges form a two-factor on \(\mathcal A\) if and
   only if \(g\) is a permutation of \(\mathcal A\).  For a general SCD,
   the largest part supported by central-diamond cycles is exactly the
   periodic-point set of \(g\).  Small local degree defect does not control
   the mass in escaping functional orbits.
3. If radius-zero states may supply nonforced reset transitions, the exact
   abstract criterion weakens from permutation to injectivity:

   \[
       g:\mathcal A\longrightarrow\mathcal M
       \text{ extends to a permutation of }\mathcal M
       \quad\Longleftrightarrow\quad g\text{ is injective}.
   \tag{0.3}
   \]

   More generally, with

   \[
       \Delta=N_1-|g(\mathcal A)|,
   \]

   the minimum number of nonforced arcs in an unrestricted permutation
   completion is exactly

   \[
       \boxed{D+\Delta.}
   \tag{0.4}
   \]

   This is not yet a literal Johnson completion; the missing Hall condition
   is stated below.
4. There is a sharp automatic positive fact.  Every two consecutive
   defined central-diamond moves use four distinct coordinates.  Hence all
   directed \(g\)-orbits are two-step Johnson geodesics, and every
   \(g\)-cycle is automatically \(2\)-safe.  The assertion is sharp:
   an explicit SCD of \(B_4\) has the cycle

   \[
       14\longrightarrow12\longrightarrow23\longrightarrow34
       \longrightarrow14,
   \tag{0.5}
   \]

   which is not \(3\)-safe.  This component embeds in a full SCD of
   \(B_{2m}\) for every \(m\ge2\).  Thus no safety theorem beyond depth two
   follows from the SCD axioms alone.
5. There are exact statewise obstructions even at depth one.  If all
   central diamonds form a two-factor, the radius-zero leave must be a
   point \(1\)-design:

   \[
       |\{E\in\mathcal E:x\in E\}|=D/2
       \qquad(x\in[2m]),
   \tag{0.6}
   \]

   where \(\mathcal E=\mathcal M\setminus\mathcal A\).  In particular
   \(D\) must be even.  Since \(\operatorname {Cat}_m\) is odd exactly for
   \(m=2^a-1\), an exact central-diamond two-factor is impossible in all
   those dimensions.
6. A cycle of the central map does not bundle the higher SCD flags.  The
   first additional identity, for \(X\in\mathcal A_2\) with
   \(g(X)\in\mathcal A_1\), is

   \[
       g^2(X)=G_2(X),
   \tag{0.7}
   \]

   where \(G_2(X)\) is the opposite middle corner of the full depth-two
   SCD interval through \(X\).  Automatic \(2\)-safety proves only that
   \(g^2(X)\) is some distance-two middle state, not (0.7).  The complete
   condition is the opposite-corner semigroup law in Section 8.

Consequently the central-diamond lane is neither automatically positive nor
universally impossible.  It has a complete statewise test.  For
\(H=o(m)\), a genuine long \(H\)-safe factor would be sufficient at the
owner level if it had \(o(W/H)\) cycles; the unavoidable Catalan leave is
already \(o(W/H)\).  What remains unproved is an SCD satisfying the
permutation/reset Hall condition, the all-depth label-separation condition,
the \(o(W/H)\) component bound, and the higher-flag semigroup law
simultaneously.

## 1. The exact central map and census

Let \(\rho(X)\) be the radius of the SCD chain whose unique middle member is
\(X\), and define

\[
 \mathcal A_q=\{X\in\mathcal M:\rho(X)\ge q\},
 \qquad \mathcal A=\mathcal A_1,
 \qquad \mathcal E=\mathcal M\setminus\mathcal A.
 \tag{1.1}
\]

### Lemma 1.1 (rank bijections)

For every \(q\le m\), the depth-\(q\) lower and upper members of the chain
through \(X\) give bijections

\[
 \mathcal A_q\longrightarrow\binom{[2m]}{m-q},
 \qquad
 \mathcal A_q\longrightarrow\binom{[2m]}{m+q}.
 \tag{1.2}
\]

In particular,

\[
 |\mathcal A_q|=N_q:=\binom{2m}{m-q},
 \qquad |\mathcal E|=W-N_1=D.
 \tag{1.3}
\]

#### Proof

Every rank-\((m-q)\) set belongs to a unique SCD chain.  Symmetry of that
chain forces it to reach rank \(m+q\) and to have a unique middle member.
This constructs the inverse of the lower map.  The upper assertion is the
same argument, or follows by symmetry.  Equation (1.3) follows, and

\[
 W-N_1
 =\binom{2m}m-\binom{2m}{m-1}
 =\frac1{m+1}\binom{2m}m.
\]

\(\square\)

For \(X\in\mathcal A\), define \(R_X,U_X,\alpha_X,\beta_X,g(X)\) as in
(0.1).  The maps \(X\mapsto R_X\) and \(X\mapsto U_X\) are the two
bijections in (1.2) at \(q=1\).

## 2. Exact local structure of a central-diamond fibre

Let \(\mathcal D_{\mathscr S}\) be the directed graph on \(\mathcal M\)
with the arc \(X\to g(X)\) for every \(X\in\mathcal A\).

### Lemma 2.1 (simple edges and no reversals)

The \(N_1\) undirected edges \(\{X,g(X)\}\), \(X\in\mathcal A\), are
distinct.  There are no loops and no reverse pairs:

\[
 g(X)\ne X,
 \qquad
 \text{there are no }X,Y\in\mathcal A
 \text{ with }g(X)=Y, g(Y)=X.
 \tag{2.1}
\]

#### Proof

The endpoints of a Johnson edge determine their intersection and union.
For the edge owned by \(X\), these are \(R_X\) and \(U_X\).  If two SCD
centers owned the same edge, they would have the same rank-\((m-1)\)
predecessor and the same rank-\((m+1)\) successor, contradicting the
uniqueness of a chain member.  A loop is impossible because
\(\alpha_X\ne\beta_X\).  A reverse pair would make both \(X\) and \(Y\)
the central member above \(X\cap Y\), again impossible. \(\square\)

### Lemma 2.2 (each incoming fibre is a matching)

Fix \(Y\in\mathcal M\).  Every \(X\in g^{-1}(Y)\) determines a pair

\[
 (a_X,b_X)=(X\setminus Y,\;Y\setminus X)
       \in Y^c\times Y.
 \tag{2.2}
\]

The pairs (2.2) form a matching between \(Y^c\) and \(Y\).  Consequently

\[
                         |g^{-1}(Y)|\le m.
 \tag{2.3}
\]

#### Proof

For the preimage \(X=Y-b_X+a_X\),

\[
 R_X=Y-b_X,
 \qquad U_X=Y+a_X.
 \tag{2.4}
\]

Two preimages sharing \(b_X\) would share their lower SCD member, and two
sharing \(a_X\) would share their upper SCD member.  Both are impossible by
Lemma 1.1. \(\square\)

### Corollary 2.3 (exact middle degree)

For every \(Y\in\mathcal M\),

\[
 \deg_{\mathcal D_{\mathscr S}}(Y)
 =\mathbf 1_{Y\in\mathcal A}+|g^{-1}(Y)|.
 \tag{2.5}
\]

There is no double-counting in (2.5), by the no-reversal assertion in
Lemma 2.1.

## 3. Two-factors and the exact cyclic core

### Theorem 3.1 (central-diamond two-factor criterion)

The following are equivalent.

1. All central-diamond edges form a two-factor on \(\mathcal A\), with
   every vertex of \(\mathcal E\) isolated.
2. \(g(\mathcal A)=\mathcal A\) and
   \(g:\mathcal A\to\mathcal A\) is a permutation.
3. Every vertex of \(\mathcal A\) has indegree one and every vertex of
   \(\mathcal E\) has indegree zero.

When these conditions hold, the components are the directed cycles of
\(g\).

#### Proof

By (2.5), degree two on \(\mathcal A\) and degree zero on \(\mathcal E\)
is precisely condition 3.  Since every member of \(\mathcal A\) has one
outgoing arc and \(|\mathcal A|<\infty\), condition 3 is equivalent to
condition 2.  A finite permutation decomposes into directed cycles.
\(\square\)

For a general SCD put

\[
 \operatorname {Per}(g)
 =\{X\in\mathcal A:g^j(X)=X\text{ for some }j\ge1\}.
 \tag{3.1}
\]

### Theorem 3.2 (statewise cyclic-core obstruction)

The vertices lying in any undirected cycle made only of central-diamond
edges are exactly \(\operatorname {Per}(g)\).  Hence the maximal owner set
covered by such cycles is \(\operatorname {Per}(g)\), and an owner leave
of \(o(W/H)\) requires

\[
                W-|\operatorname {Per}(g)|=o(W/H).
 \tag{3.2}
\]

#### Proof

Every periodic orbit is a directed cycle.  Conversely, let \(C\) be an
undirected cycle of length \(L\) in the central-diamond graph.  Its \(L\)
edges have \(L\) distinct owners, each owner has at most one outgoing edge,
and every owner must be a vertex of \(C\).  Therefore every vertex of
\(C\) owns exactly one edge of \(C\).  The induced orientation has
outdegree and indegree one at every vertex, so \(C\) is a directed periodic
orbit. \(\square\)

This is stronger than a local degree estimate.  One functional component
may be a path through \(\Theta(W)\) states ending outside \(\mathcal A\).
It then has only one missing indegree and one terminal state, but contributes
no vertex to \(\operatorname {Per}(g)\).

### Corollary 3.3 (exact functional-component census)

If \(c(g)\) is the number of periodic orbits, then the undirected central-
diamond graph is a pseudoforest and has exactly

\[
                         D+c(g)
 \tag{3.3}
\]

weak components.

#### Proof

Every weak component of a functional graph contains at most one directed
cycle.  The underlying graph has \(W\) vertices, \(N_1\) distinct edges,
and total cyclomatic number \(c(g)\).  Its number of components is therefore

\[
 W-N_1+c(g)=D+c(g).
\]

\(\square\)

## 4. Exact reset completion and its literal Hall cut

Define the collision excess

\[
 \Delta=N_1-|g(\mathcal A)|
 =\sum_{Y\in\mathcal M}(|g^{-1}(Y)|-1)_+.
 \tag{4.1}
\]

### Theorem 4.1 (unrestricted permutation completion)

There is a permutation \(P\) of \(\mathcal M\) satisfying

\[
                         P(X)=g(X)\qquad(X\in\mathcal A)
 \tag{4.2}
\]

if and only if \(g\) is injective.  If collided forced arcs may be
discarded, the maximum number of central-diamond arcs retained by a
permutation is \(|g(\mathcal A)|=N_1-\Delta\), and the minimum number of
nonforced arcs is

\[
                         W-(N_1-\Delta)=D+\Delta.
 \tag{4.3}
\]

#### Proof

A restriction of a permutation is injective.  Conversely, if \(g\) is
injective, choose any bijection

\[
 \mathcal M\setminus\mathcal A
       \longrightarrow \mathcal M\setminus g(\mathcal A)
\]

and adjoin it to \(g\).  For the second assertion, at most one preimage of
each \(Y\in g(\mathcal A)\) can retain its forced arc.  Choosing one such
preimage for every image retains \(N_1-\Delta\) arcs, after which the two
unmatched shores have the same size and may be bijected arbitrarily.
\(\square\)

If \(g\) is injective, its forced graph is a disjoint union of directed
cycles, directed paths, and isolated radius-zero states.  Counting starts
and sinks with isolated states counted in both roles gives exactly \(D\)
of each.  Thus \(D\) abstract resets suffice.  They need not be Johnson
edges, and Theorem 4.1 makes no literal-word claim.

Here is the exact missing depth-one condition.  Select one source over each
image and let \(S\subseteq\mathcal A\) be the selected source family.  Put

\[
 L_0=\mathcal M\setminus S,
 \qquad R_0=\mathcal M\setminus g(S).
 \tag{4.4}
\]

Let \(B_J(S)\) be the bipartite graph with shores \(L_0,R_0\), joining
\(X\in L_0\) to \(Y\in R_0\) exactly when \(|X\mathbin\triangle Y|=2\).

### Proposition 4.2 (literal one-edge reset Hall criterion)

The retained central arcs extend to a permutation all of whose nonforced
arcs are Johnson edges if and only if

\[
 |N_{B_J(S)}(T)|\ge |T|
                  \qquad\text{for every }T\subseteq L_0.
 \tag{4.5}
\]

#### Proof

The missing arcs of a permutation are exactly a perfect matching from
\(L_0\) to \(R_0\).  Requiring each to be a Johnson edge restricts that
matching to \(B_J(S)\).  Hall's theorem gives (4.5). \(\square\)

Proposition 4.2 is for the fixed retained-source choice \(S\).  A literal
completion retaining the maximum \(|g(\mathcal A)|\) forced arcs exists if
and only if at least one choice of one preimage per image satisfies (4.5).
Failure for every maximal choice does not rule out a completion after
discarding further forced arcs.

Ordinary state Hall is still insufficient for \(H\)-safety, because an
allowed seam depends on the last \(H-1\) swaps at its tail and the first
\(H-1\) swaps at its head.  The history-correct version is given in
Section 9.

There is also a coordinate-flux obstruction invisible in the abstract
completion theorem.  For any retained directed central-edge family \(F\),
put

\[
 v_F=\sum_{X\to Y\in F}(\mathbf1_Y-\mathbf1_X)
     =\sum_{X\to g(X)\in F}(e_{\beta_X}-e_{\alpha_X})
     \in\mathbb Z^{[2m]}.
 \tag{4.6}
\]

### Proposition 4.3 (physical seam flux lower bound)

If \(r\) additional directed Johnson edges turn \(F\) into a union of
directed cycles, then

\[
                              r\ge\frac12\|v_F\|_1.
 \tag{4.7}
\]

#### Proof

The sum of \(\mathbf1_Y-\mathbf1_X\) around every directed cycle is zero.
Hence the \(r\) added edge vectors sum to \(-v_F\).  Every directed Johnson
edge vector has \(\ell^1\)-norm two, and the triangle inequality gives
(4.7). \(\square\)

Thus even an injective owner map may need many physical seams when the
forced endpoint flux is large.

### Corollary 4.4 (injective endpoint-leave law)

Assume \(g\) is injective and put

\[
 \mathcal F=\mathcal M\setminus g(\mathcal A),
 \qquad |\mathcal F|=D.
\]

Then, for every coordinate \(x\),

\[
                         d_{\mathcal E}(x)+d_{\mathcal F}(x)=D.
 \tag{4.8}
\]

In particular, retaining every forced edge reduces Proposition 4.2 to a
Johnson matching from the radius-zero tail set \(\mathcal E\) to the
indegree-zero head set \(\mathcal F\).  In the no-reset case
\(g(\mathcal A)=\mathcal A\), one has \(\mathcal F=\mathcal E\), and
(4.8) becomes the point-design law \(d_{\mathcal E}(x)=D/2\).

#### Proof

For one central diamond, the number of its two middle endpoints containing
\(x\) equals

\[
 \mathbf1_{x\in R_X}+\mathbf1_{x\in U_X}.
\]

The first endpoint family is \(\mathcal A=\mathcal M\setminus\mathcal E\)
and, by injectivity, the second is
\(g(\mathcal A)=\mathcal M\setminus\mathcal F\).  Summing endpoint
incidences and using the two rank bijections gives

\[
 2\binom{2m-1}{m-1}-d_{\mathcal E}(x)-d_{\mathcal F}(x)
 =\binom{2m-1}{m-2}+\binom{2m-1}{m}.
\]

The difference of the two sides' binomial baselines is \(D\), proving
(4.8). \(\square\)

## 5. The automatic two-step theorem

For a directed orbit write

\[
 X_{t+1}=g(X_t)=X_t-a_t+b_t,
 \qquad S_t=\{a_t,b_t\}.
 \tag{5.1}
\]

### Theorem 5.1 (incident supports are disjoint)

Any two distinct central-diamond edges incident with the same middle state
have disjoint two-coordinate supports.  In particular, if
\(X_t,X_{t+1}\in\mathcal A\), then

\[
                             S_t\cap S_{t+1}=\varnothing.
 \tag{5.2}
\]

Consequently every two-edge undirected path in the central-diamond graph,
in either orientation, is a Johnson geodesic of length two.

#### Proof

Let two distinct central-diamond edges meet at \(Y\).  Relative to \(Y\),
each support contains one coordinate of \(Y\) and one coordinate outside
\(Y\).  If their supports shared \(c\in Y\), both edges would have lower
colour \(Y-c\), contradicting the lower-rank bijection of Lemma 1.1.  If
they shared \(c\notin Y\), both would have upper colour \(Y+c\),
contradicting the upper-rank bijection.  Thus the supports are disjoint.
Two disjoint swaps change four coordinates, so the endpoints of the
two-edge path have Johnson distance two. \(\square\)

In particular the undirected central-diamond degree of every middle state
is at most \(m\).  For a positive-radius state, (2.5) sharpens to
\(|g^{-1}(Y)|\le m-1\).

This is the strongest universal local safety statement: Section 7 gives an
SCD where \(S_t=S_{t+2}\).

## 6. Exact \(H\)-safety criterion and cycle-length toll

Regard a directed cycle

\[
 C=(X_0,X_1,\ldots,X_{L-1},X_0)
 \tag{6.1}
\]

as periodically indexed.  Call it \(H\)-safe if every segment of
\(q\le H\) consecutive edges is a Johnson geodesic of length \(q\).

### Lemma 6.1 (geodesic support criterion)

A segment of \(q\) Johnson swaps with support pairs
\(S_t,\ldots,S_{t+q-1}\) is geodesic of length \(q\) if and only if its
\(2q\) coordinate occurrences are all distinct.

#### Proof

Each swap toggles its two coordinates.  After \(q\) swaps the Johnson
distance between the endpoints is half the number of coordinates toggled
an odd number of times.  This number is \(2q\) exactly when no coordinate
occurs twice.  Any repetition reduces it by at least two. \(\square\)

### Theorem 6.2 (cyclic spacing criterion)

For a directed \(g\)-cycle, the following are equivalent.

1. The cycle is \(H\)-safe.
2. Every \(H\)-term cyclic block \(S_t,\ldots,S_{t+H-1}\) consists of
   pairwise disjoint two-sets.
3. For every ground coordinate, the cyclic gap between two consecutive
   edge positions whose support contains that coordinate is at least
   \(H\).

If \(H\ge2\), every \(H\)-safe cycle has

\[
                              L\ge2H.
 \tag{6.2}
\]

In particular every central-diamond cycle has length at least four.
If equality \(L=2H\) holds, the cycle is exactly a physical
\(C_{2H}\)-strip.

#### Proof

Lemma 6.1 gives the equivalence of 1 and 2.  A pair of occurrences lies in
a common block of at most \(H\) consecutive edges exactly when one of their
two cyclic gaps is less than \(H\), proving equivalence with 3.

Around a closed set-valued walk, every coordinate is inserted as many times
as it is deleted.  Hence every used coordinate occurs in an even positive
number of support pairs.  Choose one used coordinate.  Its cyclic
occurrence gaps, of which there are at least two, are each at least \(H\)
and together sum to \(L\); this proves (6.2).  Theorem 5.1 makes every
central-diamond cycle \(2\)-safe, so
\(L\ge4\).

Suppose now that \(L=2H\).  Every used coordinate occurs at least twice,
and its consecutive occurrence gaps are at least \(H\).  It therefore
occurs exactly twice, at antipodal edge positions.  Membership alternates
at its occurrences, so

\[
 b_t=a_{t+H},\qquad b_{t+H}=a_t.
 \tag{6.3}
\]

The deletion labels \(a_0,\ldots,a_{2H-1}\) are consequently distinct.
Writing \(z_t=a_t\), the recurrence becomes

\[
 X_{t+1}=X_t-z_t+z_{t+H},
\]

and hence

\[
 X_t=K\cup\{z_t,z_{t+1},\ldots,z_{t+H-1}\}
\]

for a fixed \((m-H)\)-set \(K\).  This is precisely the physical-strip
normal form. \(\square\)

The lower bound (6.2) only yields at most \(N_1/(2H)\) components.  This is
\(O(W/H)\), not the \(o(W/H)\) needed for coefficient one.  A long-factor
theorem must still make the average component length \(\omega(H)\).

Let \(\operatorname {Per}_H(g)\) be the union of periodic \(g\)-orbits
satisfying Theorem 6.2, and let \(c_H(g)\) be their number.

### Corollary 6.3 (maximal pure-diamond \(H\)-safe cover)

The unique maximal owner support of an \(H\)-safe cycle cover made only
from the fixed central diamonds is \(\operatorname {Per}_H(g)\).  Its
exact statewise ledger is

\[
 \text{leave}=W-|\operatorname {Per}_H(g)|,
 \qquad
 \text{components}=c_H(g).
 \tag{6.4}
\]

#### Proof

Theorem 3.2 says every pure-diamond cycle is a whole periodic orbit.
Theorem 6.2 decides independently which such orbits are \(H\)-safe.  Their
union is therefore both feasible and maximal. \(\square\)

## 7. Sharpness at depth three

On \([4]=\{1,2,3,4\}\), consider the chains

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24.
\end{array}
\tag{7.1}
\]

They partition \(B_4\) into symmetric saturated chains.  Their four
positive-radius centers have central map

\[
 14\xrightarrow{\{4,2\}}12
 \xrightarrow{\{1,3\}}23
 \xrightarrow{\{2,4\}}34
 \xrightarrow{\{3,1\}}14.
 \tag{7.2}
\]

Thus the component is a central-diamond two-factor and is \(2\)-safe, but
the first and third support pairs coincide.  The three-edge path from
\(14\) to \(34\) has Johnson distance one, not three.  It is not
\(3\)-safe.

### Proposition 7.1 (the counterexample embeds in every even Boolean rank)

For every \(m\ge2\), there is an SCD of \(B_{2m}\) containing a translated
copy of the component (7.2).

#### Proof

Split the ground set as \(Q\sqcup T\), with \(|Q|=4\) and
\(|T|=2m-4\).  Choose an SCD of \(B_T\).  Its number of singleton middle
chains is

\[
 \binom{2m-4}{m-2}-\binom{2m-4}{m-3}>0,
\]

so fix one such chain \(\{K\}\), \(|K|=m-2\).

Take the product of (7.1) with the chosen SCD of \(B_T\).  A product of two
symmetric chains has an SCD: for a grid \([0,p]\times[0,q]\), remove the
saturated boundary chain

\[
 (0,0),(0,1),\ldots,(0,q),(1,q),\ldots,(p,q),
\]

and apply induction to the remaining translated
\([0,p-1]\times[0,q-1]\).  The removed and residual chains are symmetric
about the same total rank.  When one factor is a singleton, this procedure
leaves the other chain unchanged.

Therefore the six products of the chains in (7.1) with \(\{K\}\) occur
unchanged in a full product SCD.  Their four central states are

\[
 K\cup14,\quad K\cup12,\quad K\cup23,\quad K\cup34,
\]

and have exactly the transitions (7.2). \(\square\)

This proposition is a local sharpness result, not a positive-density
obstruction to a different SCD.  For \(m\ge3\) it is an eligible depth-three
central-band obstruction; at \(m=2\) it is only the corresponding metric
failure, since rank \(m-3\) does not exist.

The dependence on the full SCD state is already visible with the same
singleton leave.  Replacing (7.1) by

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset12\subset123\subset1234,\\
 2&\subset&23\subset234,\\
 3&\subset&34\subset134,\\
 4&\subset&14\subset124,\\
 &&13,\\
 &&24
\end{array}
 \tag{7.3}
\]

gives

\[
 12\longrightarrow13\longleftarrow34,
 \qquad
 23\longrightarrow24\longleftarrow14.
 \tag{7.4}
\]

Its periodic core is empty.  The cyclic SCD (7.1) and the colliding SCD
(7.3) have the identical radius-zero family \(\{13,24\}\), which is the
required point design.  Hence even the parity and leave-design conditions
do not decide injectivity or cyclicity.

## 8. Coordinate parity, leave design, and the higher-flag cocycle

For each central diamond form the coordinate-swap edge
\(\{\alpha_X,\beta_X\}\) on the ground set \([2m]\).

### Theorem 8.1 (regular swap ledger)

Every ground coordinate has degree exactly

\[
 \binom{2m-1}{m}-\binom{2m-1}{m-2}
 =\frac1{m+1}\binom{2m}m
 =D
 \tag{8.1}
\]

in the swap multigraph of all central diamonds.

#### Proof

For one flag \(R_X\subset U_X\),

\[
 \mathbf1_{x\in\{\alpha_X,\beta_X\}}
 =\mathbf1_{x\in U_X}-\mathbf1_{x\in R_X}.
\]

The lower and upper maps enumerate their complete ranks once by Lemma 1.1.
Summing gives the first difference in (8.1); the displayed binomial
identity gives \(D\). \(\square\)

### Theorem 8.2 (parity and singleton-leave obstruction)

If all central-diamond edges form a two-factor on \(\mathcal A\), then
\(D\) is even and

\[
 d_{\mathcal E}(x):=|\{E\in\mathcal E:x\in E\}|=D/2
 \qquad(x\in[2m]).
 \tag{8.2}
\]

#### Proof

Orient every middle-state cycle.  A coordinate is inserted as often as it
is deleted around each cycle, so its total number of swap incidences is
even.  Theorem 8.1 makes that number \(D\).

For the stronger statement, each used middle owner has degree two.  For
one diamond, the number of its two middle endpoints containing \(x\) is

\[
 \mathbf1_{x\in R_X}+\mathbf1_{x\in U_X}.
\]

Summing all diamonds gives

\[
 2d_{\mathcal A}(x)
 =\binom{2m-1}{m-2}+\binom{2m-1}{m}.
 \tag{8.3}
\]

Subtract (8.3) from twice the full middle coordinate degree
\(2\binom{2m-1}{m-1}\); the result is \(2d_{\mathcal E}(x)=D\).
\(\square\)

### Corollary 8.3 (infinitely many exact failures)

If \(m=2^a-1\), no exact central-diamond two-factor exists.

#### Proof

Legendre's formula gives

\[
 v_2\binom{2m}m=s_2(m),
 \qquad
 v_2(\operatorname {Cat}_m)=s_2(m)-v_2(m+1),
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
If \(t=v_2(m+1)\), then \(m\) ends in exactly \(t\) ones, so
\(s_2(m)\ge t\), with equality precisely when \(m=2^t-1\).  Thus the
Catalan number is odd exactly in the stated dimensions, contradicting
Theorem 8.2. \(\square\)

The parity obstruction concerns the exact use of every central diamond.
It does not obstruct an asymptotic factor after a small reset or deletion
set.

There is a sharp finite strengthening.  If \(D\) is odd, take any union of
central-diamond cycles and omit the other central edges.  The used swap
degree is even at every coordinate, whereas the full degree is the odd
number \(D\).  Thus the omitted swap graph has odd positive degree at all
\(2m\) coordinates and contains at least \(m\) edges.  The source of every
omitted edge is absent from the cycle support by Theorem 3.2.  Therefore,
whenever \(m=2^a-1\), every pure central-diamond cycle cover satisfies

\[
                         \text{middle leave}\ge D+m.
 \tag{8.3a}
\]

This polynomial strengthening is still asymptotically negligible compared
with \(W\).

Now define the full flags.  For \(X\in\mathcal A_q\), let

\[
 D_q(X)\subset\cdots\subset D_1(X)\subset X
 \subset E_1(X)\subset\cdots\subset E_q(X)
 \tag{8.4}
\]

be its SCD chain segment, and write

\[
 \delta_j(X)=D_{j-1}(X)\setminus D_j(X),
 \qquad
 \eta_j(X)=E_j(X)\setminus E_{j-1}(X).
 \tag{8.5}
\]

Put

\[
 G_q(X)=X-\{\delta_1(X),\ldots,\delta_q(X)\}
          +\{\eta_1(X),\ldots,\eta_q(X)\}.
 \tag{8.6}
\]

Set \(G_0(X)=X\).  Thus \(G_1=g\) on \(\mathcal A\).

### Theorem 8.4 (exact flag-bundling criterion)

Consecutive central-map windows reproduce the SCD flags through depth
\(H\) if and only if, for every \(X\in\mathcal A_q\), \(q\le H\),

\[
 g^t(X)=G_t(X)\quad(0\le t\le q),
 \qquad
 G_t(X)\in\mathcal A_1\quad(0\le t<q),
 \tag{8.7}
\]

or equivalently

\[
 G_t(X)\in\mathcal A_1,
 \qquad g(G_t(X))=G_{t+1}(X)
                    \qquad(0\le t<q).
 \tag{8.8}
\]

In label form, the condition is

\[
 \alpha_{g^tX}=\delta_{t+1}(X),
 \qquad
 \beta_{g^tX}=\eta_{t+1}(X)
                    \qquad(0\le t<q),
 \tag{8.9}
\]

#### Proof

If the successive windows reproduce the chain flag at \(X\), the first
\(t\) swaps must delete precisely
\(\delta_1(X),\ldots,\delta_t(X)\) and insert precisely
\(\eta_1(X),\ldots,\eta_t(X)\).  Their endpoint is therefore \(G_t(X)\),
and the next unique swap gives (8.9).  This proves necessity.

Conversely, (8.8) inductively gives \(g^t(X)=G_t(X)\).  The successive
intersections and unions are then exactly \(D_t(X)\) and \(E_t(X)\), so
the SCD flags are reproduced. \(\square\)

The stronger **hereditary shift-consistency** condition additionally asks

\[
                         G_t(X)\in\mathcal A_{q-t}
                         \qquad(0\le t<q).
 \tag{8.9a}
\]

It ensures that the shifted owner itself carries a residual SCD flag of
the full remaining depth.  Condition (8.9a) is useful in recursive
promotion constructions, but it is strictly stronger than what is needed
to reproduce the one rooted flag at \(X\); it is not silently included in
(8.9).

At depth two, Theorem 5.1 only says that

\[
 g^2(X)=X-\{\alpha_X,\alpha_{gX}\}
           +\{\beta_X,\beta_{gX}\}
\]

is a distance-two state.  The load-bearing extra equations are

\[
 \alpha_{gX}=\delta_2(X),
 \qquad \beta_{gX}=\eta_2(X).
 \tag{8.10}
\]

Thus an SCD partitions all ranks but does not, merely by doing so, bundle
its flags into the cyclic order of \(g\).

There is a weaker exact criterion if only global target coverage, rather
than agreement with the preassigned SCD owner, is required.  Suppose the
selected \(H\)-safe cycle system contains every owner in \(\mathcal A_q\).
On its orbits define

\[
 L_q(X_t)=\bigcap_{j=0}^qX_{t+j},
 \qquad
 U_q(X_t)=\bigcup_{j=0}^qX_{t+j}.
 \tag{8.11}
\]

Safety puts these in ranks \(m-q\) and \(m+q\).  Since
\(|\mathcal A_q|=N_q\), the depth-\(q\) lower and upper target layers are
covered exactly once if and only if the two trace maps

\[
 L_q:\mathcal A_q\to\binom{[2m]}{m-q},
 \qquad
 U_q:\mathcal A_q\to\binom{[2m]}{m+q}
 \tag{8.12}
\]

are injective.  Cardinality then makes them bijective.  The semigroup law
is a local sufficient mechanism for (8.12), but the rank census alone
supplies neither injectivity nor coverage.

## 9. Long \(H\)-safe covers and the stateful seam Hall condition

### Theorem 9.1 (exact no-reset owner criterion)

Suppose \(g\) is a permutation of \(\mathcal A\).  Let \(K_H\) be the
number of its cycles, and suppose every cycle satisfies Theorem 6.2.  Then
the central diamonds form an \(H\)-safe owner cycle cover with

\[
 \text{owner leave}=D,
 \qquad
 \text{components}=K_H.
 \tag{9.1}
\]

It has the required negligible leave and component count exactly when

\[
                         D+K_H=o(W/H).
 \tag{9.2}
\]

For \(H=o(m)\),

\[
 \frac{D}{W/H}=\frac{H}{m+1}=o(1),
 \tag{9.3}
\]

so (9.2) reduces to \(K_H=o(W/H)\).

Theorem 6.2 alone gives only \(K_H\le N_1/(2H)\), which is not enough.

For reset completions, histories must be retained as part of the port
state.  Here is an exact useful version.  Start with vertex-disjoint
directed forced paths \(P_i\), each internally \(H\)-safe and containing at
least \(H-1\) forced edges.  Denote its first and last middle states by
\(s_i,t_i\).  Declare \(i\to j\) **admissible** when

1. \(|t_i\mathbin\triangle s_j|=2\); and
2. after inserting this seam swap between the final \(H-1\) support pairs
   of \(P_i\) and the initial \(H-1\) support pairs of \(P_j\), every block
   of at most \(H\) consecutive support pairs is disjoint.

Let \(B_H\) be the bipartite graph with a left and right copy of the path
index set and edge \(i_Lj_R\) exactly for an admissible seam.

### Proposition 9.2 (stateful one-seam Hall theorem)

The paths \(P_i\) admit a one-Johnson-edge-per-path \(H\)-safe cycle-cover
completion if and only if

\[
 |N_{B_H}(I)|\ge |I|
                     \qquad\text{for every path family }I.
 \tag{9.4}
\]

Under a perfect matching, the number of resulting owner cycles is the
number of cycles of the induced permutation of the path indices.

#### Proof

A completion chooses exactly one successor and one predecessor for every
path, hence is a perfect matching of \(B_H\).  Conversely, a perfect
matching joins the paths into directed cycles.  Since each path has at
least \(H-1\) forced edges, an \(H\)-edge window crosses at most one seam.
Internal windows are safe by hypothesis and seam-crossing windows are safe
by admissibility.  Hall's theorem proves (9.4). \(\square\)

The length hypothesis is substantive.  With shorter pieces, an
\(H\)-window can cross several seams, and pairwise endpoint compatibility
is not sufficient.  One must either group the short pieces first or use a
higher-order configuration graph.  Even (9.4) controls only existence of a
cycle cover; it does not force \(o(W/H)\) cycles.  This is the precise
statewise/global-fusion distinction.

Quantitatively, any compiler which pays \(\Theta(H)\) separately for every
noncentral seam requires

\[
                         \Delta=o(W/H),
 \tag{9.5}
\]

because Theorem 4.1 already forces \(D+\Delta\) noncentral arcs.  For
\(H=o(m)\), the \(D\) term is harmless; collision excess, history Hall, and
component fusion are the real gates for that architecture.  Equation (9.5)
is not a universal lower bound on all literal words: a genuinely global
construction might share the repair of many noncentral arcs.

## 10. Standard SCDs and the precise proved boundary

The standard fixed-priority/BTK SCD fails the central-cycle test maximally.
In the usual parenthesis representation, if the unpaired positions of a
radius-\(d\) middle chain are

\[
 u_1<\cdots<u_{2d},
\]

then the middle pattern on them is \(1^d0^d\).  The alternative central
corner has pattern

\[
                         1^{d-1}010^{d-1},
\]

in which the central \(01\) has become a new matched pair.  Therefore

\[
                         \rho(g(X))=\rho(X)-1.
 \tag{10.1}
\]

Every forced orbit reaches a radius-zero state, and
\(\operatorname {Per}(g)=\varnothing\).  Equivalently, in any globally
fixed star order the sum of the coordinate priorities strictly increases
under every central move, so the directed graph is acyclic.

This rules out using the canonical SCD diamond edges as they stand.  It
does not rule out a nonstandard, context-dependent SCD, nor does acyclicity
alone rule out closure by the \(D\) radius-zero reset states.  Such a reset
closure must still satisfy Theorem 4.1, the literal Hall cut (4.5), the
stateful Hall cut (9.4), and the higher cocycle (8.8).

The complete proved boundary is therefore:

* **Positive, exact:** central-diamond paths are automatically \(2\)-safe;
  the \(B_4\) SCD has an exact central \(C_4\) factor; and injective partial
  maps have an abstract \(D\)-reset permutation completion.
* **Negative, exact:** depth-three safety is not automatic; periodic-orbit
  mass, rather than local degree, is the no-reset cycle resource; exact
  factors require the Catalan leave to be a point design and are impossible
  for \(m=2^a-1\); standard ordered SCDs have empty cyclic core.
* **Still open:** construct a sequence of nonstandard SCDs for which, after
  at most \(o(W/H)\) owner/edge changes, the retained central paths have
  all-depth support spacing, satisfy the stateful seam Hall conditions,
  fuse into \(o(W/H)\) cycles, and obey the flag semigroup law with
  aggregate \(o(W)\) rooted defects.

No constant-one conclusion is asserted without this final common
construction.
