# The equivariant one-core gate at k=15: runs, ports, and weighted Hall

Date: 2026-07-29

Status: exact structural characterization and sufficient compiler theorem.
Equivariant one-cores always exist and admit an explicit run-wise
construction.  The note identifies the exact Hall-safe sparse normal form,
the exact forced-port obstruction, and an exact adaptive matching-with-
conflicts formulation.  It does not prove that every strict carrier passing
residence, lower q=2, and upper coverage has a successful compiler.

## 1. Scope and conventions

Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad h=r-d=5,
\]
\[
 W={15\choose8}=6435,\qquad N=W/15=429.
\tag{1.1}
\]

All sequences in Sections 1--7 are cyclic, indexed by
\(\mathbb Z_W\).  The derivative is Boolean OR dilation:

\[
                       (DX)_i=X_i\cup X_{i+1}.
\tag{1.2}
\]

It is not an intersection, a down-shadow, or a symmetric difference.

Let \(T\) be a cyclic rank-eight Johnson Hamilton carrier satisfying

\[
                       T_{i+N}=\rho^vT_i,
\qquad v\in\mathbb Z_{15}^{\times},
\tag{1.3}
\]

where \(\rho(x)=x+1\).  Assume cyclic three-residence.  Its maximal
backward erosion is

\[
                 P_i=T_i\cap T_{i-1}\cap T_{i-2}\cap T_{i-3}.
\tag{1.4}
\]

Then

\[
\begin{array}{c|c}
\text{row}&\text{rank}\\ \hline
P&5\\
DP&6\\
D^2P&7\\
D^3P=T&8.
\end{array}
\tag{1.5}
\]

The fixed lower carrier requirements are rank-six coverage by \(DP\) and
the rank-seven rainbow row \(D^2P\).  Rank-five coverage by \(P\) is not
assumed below.  It is tested on the literal output side of Hall.

Upper coverage does not enter the one-core proofs.  It remains a separate
carrier/cut obligation.

## 2. Exact coordinate-run characterization

For a coordinate \(x\), write

\[
 p_i(x)=\mathbf 1_{\{x\in P_i\}},
\qquad
 c_i(x)=\mathbf 1_{\{x\in C_i\}}.
\tag{2.1}
\]

### Theorem 2.1 (cyclic one-core theorem)

A cyclic sequence \(C\) satisfies

\[
                         C_i\subseteq P_i,\qquad DC=DP
\tag{2.2}
\]

if and only if, for every \(i\) and \(x\),

\[
 c_i(x)\le p_i(x),
\qquad
 c_i(x)\vee c_{i+1}(x)
   =p_i(x)\vee p_{i+1}(x).
\tag{2.3}
\]

Equivalently, let \([a,b]\) be a proper cyclic positive run of the
\(x\)-trace of \(P\).  Then

\[
                         c_a(x)=c_b(x)=1,
\tag{2.4}
\]

and no two consecutive positions of \([a,b]\) both have \(c(x)=0\).
Thus the omitted positions form an arbitrary independent set in the
interior \(\{a+1,\ldots,b-1\}\).

The core \(C\) itself is allowed to have empty point letters.  It is a
protecting lower bound, not the final literal word; Section 7 proves
nonemptiness of the emitted word \(A\).

#### Proof

Equality in (2.2) is coordinatewise exactly (2.3).  On an edge outside the
support of \(p(x)\), both sides vanish.  The boundary edge
\((a-1,a)\) contains \(x\) in \(DP\), but \(a-1\) is forbidden in \(C\);
hence \(a\) is selected.  Similarly \(b\) is selected.  Each internal run
edge must have a selected endpoint, which is exactly the prohibition of
two adjacent omissions.  Conversely, these conditions cover every cyclic
edge on which \(DP\) contains \(x\).  \(\square\)

No coordinate has all-one support in the present application.  If one
coordinate belonged to every \(P_i\), (1.3) and the unit voltage would make
every coordinate belong to every \(P_i\), contradicting \(|P_i|=5\).

### Corollary 2.2 (all run counts)

For a proper run of length \(\ell\), a feasible one-core pattern having
exactly \(s\) selected positions exists in

\[
                         {\binom{s-1}{\ell-s}}
\tag{2.5}
\]

ways.  Consequently the total number of run patterns is the Fibonacci
number \(F_\ell\), with \(F_1=F_2=1\), and

\[
       \min s=\left\lfloor{\ell\over2}\right\rfloor+1.
\tag{2.6}
\]

If \(\ell\) is odd, the minimum pattern is uniquely

\[
                         101\cdots01.
\tag{2.7}
\]

If \(\ell=2u\), there are exactly \(u\) minimum patterns.  Each has one
adjacent \(11\) pair, and its location can be any of

\[
                    (1,2),(3,4),\ldots,(2u-1,2u).
\tag{2.8}
\]

#### Proof

There are \(\ell-s\) omitted vertices.  They form a nonadjacent subset of
the \(\ell-2\) interior vertices.  The standard gap count gives

\[
 {\binom{(\ell-2)-(\ell-s)+1}{\ell-s}}
 ={\binom{s-1}{\ell-s}}.
\]

Summing gives the Fibonacci recurrence.  Maximizing the omitted independent
set gives (2.6), and substitution in (2.5) gives (2.7)--(2.8).
\(\square\)

### Hall-safe sparse normal form

Minimum incidence is an explicit useful subclass, but it is not without
loss for Hall: different minimum phases are incomparable, and a
nonminimum cover may omit a position that every chosen minimum phase keeps.

The exact without-loss sparse class is inclusion-minimal.

### Proposition 2.3 (inclusion-minimal normal form)

On each proper run, an inclusion-minimal one-core word is characterized by

\[
 \text{first and last symbols are \(1\), and neither \(00\) nor \(111\)
 occurs.}
\tag{2.9}
\]

Every one-core \(C\) contains an inclusion-minimal one-core \(C'\).
Moreover, for the containment candidate graph

\[
              S\sim_C i
   \quad\Longleftrightarrow\quad C_i\subseteq S\subseteq P_i,
\tag{2.10}
\]

one has \(G_C\subseteq G_{C'}\).  Thus any matching that works for \(C\)
also works for \(C'\).  If \(C\) is equivariant, \(C'\) may be chosen
equivariant.

#### Proof

The condition \(00\) is forbidden by Theorem 2.1.  An internal selected
vertex is removable exactly when both of its run neighbours are selected,
which is the pattern \(111\).  The endpoints are never removable because
of the two boundary edges.  Repeatedly delete removable internal vertices.
This gives \(C'\subseteq C\), and decreasing the lower containment bound
can only add candidate edges.  In the equivariant case, perform the thinning
on the coordinate-zero run traces and transport the chosen subsets by
\(\gamma\).  Since the original core is equivariant, the transported core
remains a subset of it.  \(\square\)

This proposition, rather than cardinal-minimum covers, is the exact
Hall-safe meaning of sparse.

### Warning: a depth-three core need not be a one-core

On \(\mathbb Z_5\), take one coordinate trace

\[
                       p=(1,1,1,1,0),\qquad
                       c=(1,0,0,1,0).
\tag{2.11}
\]

Then \(c\le p\) and already \(D^2c=D^2p\), hence also
\(D^3c=D^3p\), but

\[
                       Dc=(1,0,1,1,1)\ne(1,1,1,1,1)=Dp.
\tag{2.12}
\]

The two consecutive interior omissions are the exact failure.  A sparse
depth-three core from a multirow construction cannot be substituted for a
one-core without checking (2.3).

## 3. Equivariance and the exact k=15 sparsity ledger

Define the incidence action

\[
                         \gamma(i,x)=(i+N,x+v).
\tag{3.1}
\]

It is free and has order \(15\).

### Theorem 3.1 (equivariant transport)

Choose any valid one-core trace \(c_i(0)\) for coordinate \(0\).  If
\(x=tv\pmod {15}\), define

\[
                         c_j(x)=c_{j-tN}(0).
\tag{3.2}
\]

Then \(C\) is well-defined,

\[
                         C_{i+N}=\rho^vC_i,
\qquad C\subseteq P,\qquad DC=DP.
\tag{3.3}
\]

Conversely, every equivariant one-core is obtained this way.

#### Proof

Since \(v\) is a unit, \(t\) is unique modulo \(15\).  After fifteen
translations the coordinate and position both return, because \(15N=W\).
The support traces and every cyclic edge equation in (2.3) are transported
by \(\gamma\).  Conversely, equivariance determines every coordinate trace
from coordinate \(0\).  \(\square\)

Thus an equivariant core always exists: choose run patterns for coordinate
\(0\), then translate them.

### Proposition 3.2 (exact incidence-minimum ledger)

The coordinate-zero trace of \(P\) has exactly \(N\) positive runs and
exactly \(5N\) supported positions.  Let \(o\) be the number of those run
lengths that are odd.  Every incidence-minimum equivariant one-core has

\[
                 \sum_{i=0}^{W-1}|C_i|
                    ={15((5+2)N-o)\over2},
\tag{3.4}
\]

and average point rank

\[
             {1\over W}\sum_i|C_i|
                  ={7\over2}-{o\over2N}.
\tag{3.5}
\]

Here

\[
                         1\le o\le N,\qquad o\equiv5N\pmod2.
\tag{3.6}
\]

In particular, at \(N=429\),

\[
                  3\le {1\over W}\sum_i|C_i|
                    \le {7\over2}-{1\over858}<3.5.
\tag{3.7}
\]

#### Proof

Every Johnson transition starts one coordinate run, so there are \(W\)
coordinate runs in total.  Erosion preserves them because every carrier run
has length at least four.  Equivariance is transitive on coordinates, hence
there are \(W/15=N\) runs per coordinate.

The row \(P\) has rank five at every position, and equivariance again makes
the coordinate frequencies equal.  Thus coordinate \(0\) occurs \(5W/15
=5N\) times.  Summing (2.6) over its \(N\) runs gives

\[
 \sum_R\left(\left\lfloor{|R|\over2}\right\rfloor+1\right)
 ={5N+2N-o\over2}.
\]

Transport multiplies this by \(15\), proving (3.4)--(3.5).  Parity of the
sum of run lengths gives (3.6), and (3.7) follows.  \(\square\)

This is a real sparsity floor: a one-core remains roughly half-dense on each
coordinate run.  It is nevertheless much sparser than \(P\), whose point
rank is five.

### Quotient-column form

Let \(R_0=\{i:0\in P_i\}\), and let \(Q_0\subseteq R_0\) be the selected
coordinate-zero trace.  For \(j\in\mathbb Z_N\), put

\[
 q_j=\bigl|Q_0\cap\{j,j+N,\ldots,j+14N\}\bigr|.
\tag{3.8}
\]

Then

\[
                         |C_{j+tN}|=q_j
\quad(t\in\mathbb Z_{15}),
\tag{3.9}
\]

and each corresponding \(P\)-column contains exactly five coordinate-zero
support positions.  Hence \(0\le q_j\le5\), and for a minimum core

\[
                         \sum_{j=0}^{N-1}q_j={7N-o\over2}.
\tag{3.10}
\]

The even-run phase choices in (2.8) are precisely the finite choices that
alter this quotient load profile in the incidence-minimum subclass.

### Weighted run construction

Let \(a_{i,x}\ge0\) be any \(\gamma\)-invariant incidence penalties.
Minimizing

\[
                         \sum_{i,x}a_{i,x}c_i(x)
\tag{3.11}
\]

over equivariant one-cores reduces, on the coordinate-zero trace, to a
weighted vertex cover on each proper support run with both endpoints forced.
Each remaining graph is a path, so its LP is integral and an exact minimum
is given by the usual path dynamic program or an \(s\)-\(t\) cut.

This gives a rigorous way to respond to additive Hall-dual penalties.
It does not make the full Hall expansion functional additive.

## 4. Forced ports and exact target-orbit eligibility

Since consecutive \(P\)-sets have rank five and union rank six, \(P\) is
itself a cyclic Johnson chronology.  Define

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1}).
\tag{4.1}
\]

The two displayed singleton differences may coincide, so

\[
                         |F_i|\in\{1,2\}.
\tag{4.2}
\]

### Lemma 4.1 (forced-port lemma)

Every one-core satisfies

\[
                         F_i\subseteq C_i.
\tag{4.3}
\]

For a fixed physical position \(i\) and nonempty target \(S\), there exists
some one-core with

\[
                         C_i\subseteq S\subseteq P_i
\tag{4.4}
\]

if and only if

\[
                         F_i\subseteq S\subseteq P_i.
\tag{4.5}
\]

#### Proof

If \(x\in P_i\setminus P_{i-1}\), the edge \((i-1,i)\) forces
\(x\in C_i\); similarly for \(P_i\setminus P_{i+1}\).  This proves
(4.3) and necessity.

For sufficiency, prescribe \(c_i(x)=0\) for
\(x\in P_i\setminus S\).  Condition (4.5) says that every such occurrence
is internal to its coordinate run.  These prescribed omissions concern
different coordinates, so they create no same-coordinate adjacent pair.
Select every remaining supported occurrence.  Theorem 2.1 gives a one-core and
(4.4).  \(\square\)

### Corollary 4.2 (orbitwise version)

Assume \(N>1\).  If (4.5) holds, there is an equivariant one-core satisfying

\[
                 C_{i+tN}\subseteq\rho^{tv}S
                    \subseteq P_{i+tN}
\quad(t\in\mathbb Z_{15}).
\tag{4.6}
\]

It may be chosen inclusion-minimal.

#### Proof

Translate all prescribed omissions in the proof of Lemma 4.1 by
\(\gamma\).  For any fixed coordinate, the prescribed positions are
separated by \(N>1\), hence are nonadjacent; equivariance transports the
interior condition.  Complete to a one-core, then thin it equivariantly by
Proposition 2.3.  \(\square\)

### Corollary 4.3 (sharp singleton gate)

A singleton target orbit has positive degree for some equivariant one-core
if and only if

\[
                         |F_i|=1
\tag{4.7}
\]

for some \(i\).  This is equivalent to a one-vertex coordinate run in
\(P\), and hence to a length-four coordinate run in \(T\).

If every \(|F_i|=2\), all fifteen singleton targets have degree zero for
every one-core.  Thus residence, lower q=2, and upper coverage do not by
themselves settle the graded compiler: a minimum-length carrier run is an
exact additional port requirement, detected inside the compiler gate.

## 5. Exact adaptive-core assignment theorem

Fix distinct physical positions \(i_a\) and distinct nonempty targets
\(S_a\) with

\[
                         S_a\subseteq P_{i_a}.
\tag{5.1}
\]

For each coordinate define the mandatory omission set

\[
                 Z_x=\{i_a:x\in P_{i_a}\setminus S_a\}.
\tag{5.2}
\]

### Theorem 5.1 (adaptive one-core criterion)

There exists a one-core \(C\) satisfying

\[
                         C_{i_a}\subseteq S_a
\quad\text{for every }a
\tag{5.3}
\]

if and only if, on every proper \(P_x\)-run,

1. \(Z_x\) avoids both run endpoints; and
2. \(Z_x\) contains no two adjacent positions.

When these conditions hold, one may take

\[
 c_i(x)=
 \begin{cases}
 0,&i\in Z_x,\\
 p_i(x),&i\notin Z_x.
 \end{cases}
\tag{5.4}
\]

It may then be thinned to an inclusion-minimal one-core.

#### Proof

Any core satisfying (5.3) must omit every incidence in (5.2), so necessity
is Theorem 2.1.  Under the two stated conditions, (5.4) selects both run
endpoints and leaves no internal edge with two omitted endpoints.  Hence it
is a one-core.  Proposition 2.3 supplies the thinning.  \(\square\)

Define the spiral orbit closure of mandatory zero incidences by

\[
 \overline Z
  =\{\gamma^t(i_a,x):a,\ x\in P_{i_a}\setminus S_a,\
                         t\in\mathbb Z_{15}\}.
\tag{5.5}
\]

### Theorem 5.2 (equivariant adaptive criterion)

There exists an equivariant one-core satisfying (5.3) if and only if, for
every coordinate, its section of \(\overline Z\)

1. avoids every endpoint of every proper support run; and
2. contains no adjacent pair.

#### Proof

The zero set of an equivariant core is \(\gamma\)-invariant.  Thus it must
contain (5.5), and necessity follows from Theorem 2.1.  Conversely, delete
exactly the incidences in (5.5) from \(P\).  The result is equivariant and
passes the run criterion, so it is a one-core.  At every assigned position
it is contained in the assigned target.  \(\square\)

### Matching-with-conflicts reformulation

Call an assignment edge \((S,i)\) port-legal when

\[
                         F_i\subseteq S\subseteq P_i.
\tag{5.6}
\]

Two port-legal assignment edges conflict if the union of their
orbit-closed mandatory omissions contains two adjacent positions for some
coordinate.  At \(N=429>1\), one port-legal edge does not conflict with
itself: its same-coordinate orbit copies are \(N\)-separated.

Theorem 5.2 gives the following exact statement.

### Corollary 5.3 (no higher-order core obstruction)

There is a target-saturating assignment protected by an equivariant
one-core if and only if there is a target-position matching using only
port-legal edges and containing no conflicting pair.

Endpoint failure is unary; adjacent omission is pairwise.  No higher-order
run obstruction remains.

This is an exact alternative to fixing \(C\) before matching.  It is not
ordinary Hall, because the pair conflicts couple assignment edges.

The no-higher-order statement is scoped exactly to
\(C\subseteq P,\ DC=DP\).  It does not include pointwise nonemptiness or
prescribed ranks of \(C\), point quotas, or other cross-coordinate
capacities.  Several compatible coordinate omissions may jointly empty a
core letter.  That is harmless here because the emitted source letter is a
nonempty assigned target or the rank-five envelope \(P_i\).

## 6. Fixed-core weighted quotient Hall

Fix an equivariant one-core \(C\).  Let

\[
 \mathcal S_{\le5}=\{S\subseteq[15]:1\le|S|\le5\}
\tag{6.1}
\]

and form the physical bipartite graph

\[
 S\sim i
 \quad\Longleftrightarrow\quad
 C_i\subseteq S\subseteq P_i.
\tag{6.2}
\]

Let \(O\) range over rotation orbits of targets and let \(J\) range over the
\(N=429\) free position orbits.  Give \(O\) demand

\[
                         w(O)=|O|
\tag{6.3}
\]

and every \(J\) capacity \(15\).  Join \(O\) to \(J\) when at least one
physical edge (6.2) joins their members.

The exact target-orbit profile is

\[
\begin{array}{c|c}
\text{rank}&\text{orbit sizes}\\ \hline
1&15^1\\
2&15^7\\
3&15^{30},5^1\\
4&15^{91}\\
5&15^{200},3^1.
\end{array}
\tag{6.3a}
\]

Thus the weighted network has \(331\) target-orbit vertices and \(429\)
position-orbit vertices.

### Theorem 6.1 (weighted quotient-flow certificate)

The physical graph has a matching saturating all \(4943\) targets if and
only if there are integers \(f_{O,J}\ge0\) satisfying

\[
 \sum_J f_{O,J}=w(O)
\quad(O),
\tag{6.4}
\]
\[
 \sum_O f_{O,J}\le15
\quad(J),
\tag{6.5}
\]
\[
 f_{O,J}=0
\quad\text{when }O\not\sim J.
\tag{6.6}
\]

Equivalently, for every family \(\mathcal X\) of target orbits,

\[
                 \sum_{O\in\mathcal X}w(O)
                    \le15\,|N_{\rm quot}(\mathcal X)|.
\tag{6.7}
\]

#### Proof

The integral flow conditions are equivalent to weighted Hall on the
quotient.  It remains to justify that quotient Hall is exact physically.

For a physical target family \(A\), put

\[
                         \delta(A)=|A|-|N(A)|.
\]

This deficiency is supermodular.  If Hall fails, take a
maximum-deficiency family and repeatedly union it with all of its rotations.
Supermodularity preserves maximum deficiency, producing an invariant
deficient family.  Its target size is the sum of orbit weights and its
neighborhood is a union of full free position orbits, each of size fifteen.
This violates (6.7).  The converse is immediate.  Integral max flow gives
(6.4)--(6.6).  \(\square\)

The quotient flow is an existential Hall certificate.  An arbitrary
integer matrix \(f_{O,J}\) need not admit a direct phase-by-phase lift.
After quotient Hall is proved, one may recover an actual assignment by an
ordinary physical bipartite matching.

Short target orbits retain their physical weights.  At \(k=15\), the unique
short rank-three orbit has weight five and the unique short rank-five orbit
has weight three.  A final matching generally breaks rotation symmetry; an
equivariant final matching is neither needed nor generally possible.

### Necessary rank-threshold screen

For a fixed core put

\[
 b_s(C)=|\{J:|C_i|\le s\text{ on the position orbit }J\}|.
\tag{6.8}
\]

All targets of rank at most \(s\) can use only these orbits.  Thus weighted
Hall implies

\[
                         15b_s(C)\ge\sum_{t=1}^s{15\choose t}.
\tag{6.9}
\]

Explicitly,

\[
\begin{array}{c|c|c}
s&\sum_{t=1}^s{15\choose t}&\text{required }b_s\\ \hline
1&15&1\\
2&120&8\\
3&575&39\\
4&1940&130.
\end{array}
\tag{6.10}
\]

These four inequalities are useful early obstructions, but they are not
sufficient: target labels must also be contained in the corresponding
envelopes, and multi-orbit Hall cuts may remain.

## 7. Composition into the graded compiler

Assume either

1. a fixed equivariant one-core passes Theorem 6.1; or
2. a complete conflict-free adaptive assignment is supplied by
   Corollary 5.3.

Set \(A_i=S\) at every assigned position and \(A_i=P_i\) at every unassigned
position.  In either case there is a protecting one-core with

\[
                         C\subseteq A\subseteq P.
\tag{7.1}
\]

Therefore

\[
                  DP=DC\subseteq DA\subseteq DP,
\]

so

\[
                         DA=DP,\qquad
                         D^2A=D^2P,\qquad
                         D^3A=T.
\tag{7.2}
\]

Applying further derivatives gives

\[
                         D^{3+q}A=D^qT
\quad(q\ge0).
\tag{7.3}
\]

Hence every cyclic upper target supplied by the assumed carrier chronology
is inherited by the compiler.

Every source letter is nonempty: assigned letters are nonempty targets, and
unassigned letters are rank-five sets \(P_i\).  Hence this is a literal
cyclic graded compiler.

## 8. Rank five is an output-side Hall gate, not an eager carrier hypothesis

If \(|S|=5\), then

\[
 C_i\subseteq S\subseteq P_i,\qquad |P_i|=5
\]

forces

\[
                              S=P_i.
\tag{8.1}
\]

Thus a missing rank-five value is a zero-degree Hall target for every
possible core.  Rank-five coverage has been relocated into the compiler
matching; it has not been assumed and it has not disappeared.

In particular, this condition is immutable for a fixed carrier: changing
the one-core cannot create a missing value of \(P\).  Calling rank five
output means that Hall tests and certifies this carrier-determined condition,
not that the compiler repairs it.

In any successful matching, the

\[
                         {15\choose5}=3003
\tag{8.2}
\]

rank-five targets occupy 3003 distinct positions, one target occurrence per
position.  Their assigned letters equal \(P_i\), so they impose no mandatory
core omissions or conflicts.  Deleting those matched edges leaves exactly

\[
             4943-3003=1940
\tag{8.3}
\]

targets of ranks one through four for

\[
             6435-3003=3432
\tag{8.4}
\]

remaining positions.

Consequently lower q=3 is an output/zero-degree and position-capacity test.
It is not part of the one-core construction.  A carrier with a missing
rank-five value fails Hall at that output target, regardless of how its core
is chosen.

## 9. Exact proved boundary

The following points are now proved.

1. Sparse equivariant one-cores exist for every strict resident carrier and
   are constructed run by run.
2. Incidence-minimum cores have the exact ledger (3.4)--(3.7).
3. Within the equivariant-core subclass, Hall existence may be restricted
   without loss to inclusion-minimal run words avoiding \(00\) and \(111\).
4. The forced ports \(F_i\) give exact unary target-orbit eligibility.
5. A singleton orbit is possible exactly when the controller has a
   one-vertex run, equivalently when the carrier has a length-four run.
6. After port legality, the adaptive equivariant-core obstruction for
   \(C\subseteq P,\ DC=DP\) is exactly pairwise adjacent omission; no
   higher-order run obstruction exists within that scope.
7. For a fixed core, the weighted quotient flow (6.4)--(6.6) is an exact
   Hall certificate.
8. Rank-five/lower-q=3 coverage is compiler output, not an eager carrier
   hypothesis.

What is not proved is that the stated carrier hypotheses force either the
weighted flow or a conflict-free complete assignment.  They do not even
force the singleton port (4.7).  Nor is equivariance without loss for an
arbitrary successful core: the theorem only preserves equivariance when
thinning a core that was equivariant already.  Within the equivariant graded
route, the smallest remaining constructive hypothesis is therefore one of
the following equivalent-style certificates:

1. an inclusion-minimal equivariant run core plus a \(4943\)-unit quotient
   flow; or
2. a target-saturating port matching whose orbit-closed omission sets have
   no conflicting pair.

For a linear final word, the cyclic theorem should be applied first and the
usual three-letter prefix appended.  Boundary support runs have different
endpoint rules if one starts directly in the linear model.
