# Port matchings and the cross-core triangle gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 J=[2r],\qquad B=\operatorname {Cat}_r,
 \qquad {\cal X}=\binom Jr,\qquad {\cal Y}=\binom J{r+1}.
\tag{0.1}
\]

Then

\[
 |{\cal X}|=(r+1)B,\qquad |{\cal Y}|=rB.
\tag{0.2}
\]

Thus one ordinary matching cannot literally saturate both full shores.
For an oriented exact Dyck-port factor, its outgoing incidence matching is
the bijection

\[
 M:{\cal U}:={\cal X}\setminus\overline{{\cal D}_r}
       \longleftrightarrow {\cal Y},
 \qquad |{\cal U}|=rB,
\tag{0.3}
\]

and this is the meaning of a saturated port matching below.

There is an exact graph and flag reduction.

1. Contract every edge of \(M\).  On the remaining lower labels one
   obtains a simple graph \(Q_M\) with degrees

   \[
   d_{Q_M}(X)=
   \begin{cases}
   2r-1,&X\in{\cal U},\\
   r,&X\in\overline{{\cal D}_r}.
   \end{cases}
   \tag{0.4}
   \]

   The terminal family \(\overline{{\cal D}_r}\) is independent.

2. The triangles of \(Q_M\) are exactly the directed common-core
   triangles of \(M\).  Consequently

   \[
                  \boxed{A(M)={1\over6}\operatorname {tr}A(Q_M)^3.}
   \tag{0.5}
   \]

3. The complementary incidence matching of the port factor becomes a
   spanning linear forest of \(Q_M\): precisely \(B\) disjoint
   length-\(r\) paths, one from each \(P\in{\cal D}_r\) to
   \(\overline P\).

4. There are exactly \(r(r-1)B\) local closing flags, and

   \[
        \boxed{3A(M)=\sum_{X\in{\cal U}}
             \sum_{e\in J\setminus(X\cup\{d_X\})} I(X,e),}
   \tag{0.6}
   \]

   where \(d_X\) is the coordinate inserted by \(M\) at \(X\), and the
   Boolean flag \(I(X,e)\) is defined exactly in Section 4.

Formula (0.6), not the average one-core degree, is the missing cross-core
theorem.  A constant fraction of the flags would give

\[
                         A(M)=\Omega(r^2B).
\tag{0.7}
\]

That scale is stronger than is needed for a quotient-vertex-disjoint
hexagon bank.  Since every state is in at most \(r\) alternating
hexagons, the elementary greedy bound is

\[
                         \nu_6(M)\ge {A(M)\over6r-5}.
\tag{0.8}
\]

Therefore

\[
             \boxed{A(M)=\Omega(rB)\text{ already implies }
                    \nu_6(M)=\Omega(B).}
\tag{0.9}
\]

The larger scale (0.7) is relevant only if a subsequent strand extraction
loses another factor \(r\).

The port degrees, the Dyck/complement path forest, the ballot core count,
and the first two spectral moments do not prove (0.6) has a positive
density.  Section 6 gives triangle-free bipartite graphs with exactly the
same degree sequence and a spanning forest with the same endpoint/path
shape.  Thus no proof using only those data can work.

This is not yet a literal Boolean-incidence counterexample: the abstract
graphs in Section 6 need not be contractions of stars in the Boolean
incidence graph.  Nor is a fully upper-saturating, endpoint-compatible,
triangle-free port factor constructed here.  The literal problem is
reduced to the closure flags (0.6), and remains open at that point.

## 1. The saturated port-matching normal form

Let \(F\) be an exact \({\cal D}_r\)-port factor, oriented from every
Dyck root \(P\) to its complementary terminal \(\overline P\).  Write a
row as

\[
 X_0-Y_0-X_1-Y_1-\cdots-Y_{r-1}-X_r,
 \qquad X_0=P,\quad X_r=\overline P.
\tag{1.1}
\]

Its two incidence matchings are

\[
 M=\{X_tY_t:0\le t<r\},
 \qquad
 N=\{Y_tX_{t+1}:0\le t<r\}.
\tag{1.2}
\]

Over all rows, \(M\) is the bijection (0.3), while

\[
 N:{\cal Y}\longleftrightarrow
              {\cal X}\setminus{\cal D}_r
\tag{1.3}
\]

is another bijection.  Their union is the prescribed collection of
complement geodesics.

For \(X\in{\cal U}\), write

\[
                         m(X)=X+d_X\in{\cal Y},
 \qquad d_X\in J\setminus X.
\tag{1.4}
\]

Every upper state is \(m(X)\) for exactly one \(X\in{\cal U}\).

## 2. The contracted directed graph

Define a directed graph \(R_M\) on \({\cal X}\) by

\[
 X\longrightarrow Z
 \quad\Longleftrightarrow\quad
 X\in{\cal U},\quad Z\ne X,\quad Z\subset m(X).
\tag{2.1}
\]

Thus every matched upper star is oriented away from its matched lower
centre.  Let \(Q_M\) be the underlying undirected graph.

### Proposition 2.1 (exact degrees)

The directed degrees are

\[
 d^+_{R_M}(X)=
 \begin{cases}r,&X\in{\cal U},\\0,&X\notin{\cal U},\end{cases}
 \qquad
 d^-_{R_M}(X)=
 \begin{cases}r-1,&X\in{\cal U},\\r,&X\notin{\cal U}.\end{cases}
\tag{2.2}
\]

There is no directed two-cycle.  Hence (0.4) follows, and

\[
                         |E(Q_M)|=r^2B.
\tag{2.3}
\]

#### Proof

The matched upper state \(m(X)\) has exactly \(r+1\) lower facets, one
of which is \(X\), giving \(r\) outgoing arcs.

Every lower state \(Z\) belongs to exactly \(r\) upper states.  If
\(Z\in{\cal U}\), one of them is \(m(Z)\), whose star is centred at
\(Z\) and contributes no loop; each of the other \(r-1\) upper states
has another centre and contributes one incoming arc.  If \(Z\) is an
unmatched terminal, all \(r\) containing upper states have another
centre.

A two-cycle \(X\leftrightarrow Z\) would require both \(X\) and \(Z\)
to be the matched centre of their unique common upper state \(X\cup Z\),
contrary to upper saturation.  Summing (0.4) gives (2.3). \(\square\)

### Proposition 2.2 (triangles are precisely hexagons)

Every directed triangle of \(R_M\) has the form

\[
 K+a\longrightarrow K+b\longrightarrow K+c
                 \longrightarrow K+a
\tag{2.4}
\]

for one \((r-1)\)-core \(K\).  Conversely every directed common-core
triangle gives one directed triangle of \(R_M\).  Each undirected
triangle of \(Q_M\) has one of the two cyclic orientations.  Therefore
(0.5) holds.

#### Proof

Every arc joins two Johnson-adjacent lower states.  A triangle of the
Johnson graph is of one of two types: its three vertices either share an
\((r-1)\)-core, or they are three facets of one common \((r+1)\)-set
\(Y\).  The second type cannot be a triangle of \(Q_M\), because each of
its three edges would require a different one of those facets to be the
matched centre of the same upper vertex \(Y\).  The first type is exactly
(2.4), and its three matched incidence edges are one cyclic half of the
incidence hexagon.  At a common-core triangle, one lower vertex cannot
point to both of the others: those two arcs would require its unique
matched upper state to be two distinct pairwise unions.  Hence every
vertex has one outgoing edge inside the triangle, so its orientation is
cyclic. \(\square\)

The terminal family is independent in \(Q_M\), because an edge is always
oriented out of a matched centre in \({\cal U}\).

## 3. What the complement endpoint condition becomes

Contract every edge \(X_tY_t\in M\) in (1.1), retaining the lower label
\(X_t\).  The other factor edge \(Y_tX_{t+1}\in N\) becomes the edge

\[
                         X_tX_{t+1}\in E(Q_M).
\tag{3.1}
\]

Indeed, \(X_{t+1}\) is a lower facet of \(Y_t=m(X_t)\) distinct from
\(X_t\).  Consequently the \(N\)-edges give a spanning linear forest

\[
 P=X_0-X_1-\cdots-X_r=\overline P,
 \qquad P\in{\cal D}_r,
\tag{3.2}
\]

of \(Q_M\).  It has \(B\) components, every component has \(r\) edges,
and it covers all \((r+1)B\) vertices.

Thus the full complement endpoint structure visible after contraction is
not merely a scalar degree condition: \(Q_M\) contains the labelled
spanning linkage (3.2).  But it is still only a spanning forest inside
\(Q_M\); the other \(r-1\) outgoing and \(r-2\) or \(r-1\) incoming
edges at a typical vertex are not determined by (3.2).

Call a directed arc of \(R_M\) **blocked** when its underlying edge
belongs to the forest (3.2).  In the uncontracted factor this says that
the proposed opposite half-edge of the incidence cycle is already the
selected \(N\)-edge.  There are exactly

\[
                              rB
\tag{3.3}
\]

blocked arcs, one for every upper state.

### Proposition 3.1 (one blocker per triangle)

A directed common-core triangle contains at most one blocked arc.  A
fixed blocked arc belongs to at most one directed triangle.  Consequently
the number \(A_F(M)\) of triangles which are genuinely alternating
against the full factor \(F=M\cup N\) satisfies

\[
                         \boxed{A_F(M)\ge A(M)-rB.}
\tag{3.4}
\]

#### Proof

If two consecutive arcs

\[
 K+a\longrightarrow K+b\longrightarrow K+c
\]

were blocked, these would be two successive lower-state transitions on
one oriented factor row.  The first transition deletes \(a\) and inserts
\(b\); the second immediately deletes the newly inserted \(b\) and
inserts \(c\).  This backtracks one coordinate and is impossible on a
geodesic from a set to its complement.  Any two edges of a triangle are
consecutive cyclically, proving the first assertion.

Once a directed arc in one core is fixed, the outdegree-one rule at its
head determines the third vertex of a possible directed triangle, so the
arc is in at most one.  Charge every spoiled triangle to its unique
blocked arc and use (3.3). \(\square\)

Thus the stronger target \(A(M)=\Omega(r^2B)\) would automatically leave
\(\Omega(r^2B)\) full-factor alternating hexagons after every blocker is
discarded.  At the weaker natural quotient scale \(A(M)=\Theta(rB)\),
the blocker budget can still destroy the entire supply.

## 4. The exact cross-core closure flag

Fix \(X\in{\cal U}\), and put \(d=d_X\).  For every

\[
                         e\in J\setminus(X\cup\{d\}),
\tag{4.1}
\]

the upper state \(X+e\) has a unique matched centre.  It is not \(X\),
because \(X\) is already matched to \(X+d\).  Hence there is a unique
\(a_e(X)\in X\) such that

\[
 C_e(X):=X-a_e(X)+e\in{\cal U},
 \qquad m(C_e(X))=X+e.
\tag{4.2}
\]

In \(R_M\) this is the incoming arc

\[
                         C_e(X)\longrightarrow X.
\tag{4.3}
\]

The unique outneighbor of \(X\) which is Johnson-adjacent to \(C_e(X)\)
is

\[
                         W_e(X)=X-a_e(X)+d.
\tag{4.4}
\]

Their union is

\[
 V_e(X)=X-a_e(X)+d+e.
\tag{4.5}
\]

Define the closing flag

\[
 I(X,e)=
 \mathbf 1_{\{W_e(X)\in{\cal U},\ m(W_e(X))=V_e(X)\}}.
\tag{4.6}
\]

### Theorem 4.1 (exact flag identity)

Equation (0.6) holds.

#### Proof

The two forced arcs (4.3) and

\[
                         X\longrightarrow W_e(X)
\]

close to a directed triangle exactly when the upper state (4.5) is
matched from \(W_e(X)\), which is precisely (4.6).  Conversely, at a
specified middle vertex \(X\) of a directed triangle, its incoming edge
uses one upper state \(X+e\), its outgoing edge uses the distinct matched
upper state \(X+d_X\), and the preceding reconstruction is unique.
Every directed triangle has three choices of its middle vertex. \(\square\)

There are \(r-1\) choices in (4.1) for every one of the \(rB\) matched
lower states.  Thus the full flag count is

\[
                         r(r-1)B.
\tag{4.7}
\]

The desired cross-core inequalities can now be stated without hidden
constants:

\[
 \begin{array}{ll}
 \text{constant flag closure:}&
 \sum I(X,e)\ge c\,r(r-1)B
 \quad\Longleftrightarrow\quad A(M)=\Omega(r^2B),\\[2mm]
 \text{Catalan packing closure:}&
 \sum I(X,e)\ge c\,rB
 \quad\Longrightarrow\quad \nu_6(M)=\Omega(B).
 \end{array}
\tag{4.8}
\]

The second asks only for closure density \(\Omega(1/r)\), not a constant
closure density.

## 5. What the ballot and cycle identities actually give

For an \((r-1)\)-core \(K\), let \(t_K\) be the number of extensions
\(K+a\) which are terminal ports.  The exact endpoint incidence count is

\[
                         \sum_K t_K=rB
                         =\binom{2r}{r-1}.
\tag{5.1}
\]

The ballot calculation gives exactly

\[
 Z_r={r-1\over r+2}\binom{2r}{r-1}
     ={r(r-1)\over r+2}B
\tag{5.2}
\]

cores with \(t_K=0\).  On each such core the directed matching graph is
a total functional graph on \(r+1\) vertices, with neither loops nor
two-cycles.  Hence it has a cycle of length at least three.

If \(c_\ell(K)\) is the number of its directed \(\ell\)-cycles, the
proved consequence is only

\[
 \sum_{K:t_K=0}\sum_{\ell=3}^{r+1}c_\ell(K)\ge Z_r,
 \qquad
                         A(M)=\sum_Kc_3(K).
\tag{5.3}
\]

The identities (5.1)--(5.3) allow every forced cycle to have length four
or more and hence allow \(A(M)=0\).  The global selected-edge budget

\[
 \sum_K\sum_{\ell\ge3}\ell c_\ell(K)\le r|M|=r^2B
\tag{5.4}
\]

does not improve this: \(Z_r\) cycles of length \(r+1\) fit within the
right side.  The exact blocker count from the second incidence matching
is \(rB\), also large enough to mark one arc in every ballot-forced core.
Thus neither the cycle length moment nor the blocker moment forces
\(c_3(K)>0\).

## 6. The spectral identities and an abstract sharp obstruction

Let \(S=A(Q_M)\).  Propositions 2.1--2.2 give

\[
 \operatorname {tr}S^2=2|E(Q_M)|=2r^2B,
 \qquad
 \operatorname {tr}S^3=6A(M).
\tag{6.1}
\]

Thus all degree calculations fix the second spectral moment, while the
desired theorem is exactly a positive third-moment theorem.  The labelled
path forest (3.2) does not by itself bridge these moments.

The following abstract construction makes that failure literal.

### Proposition 6.1 (triangle-free degree-and-endpoint model)

Fix \(r\ge2\).  For every sufficiently large even integer \(N\), there is
a simple bipartite graph \(Q\) with vertex partition

\[
                         U\mathbin{\dot\cup}T,
 \qquad |U|=rN,\quad |T|=N,
\tag{6.2}
\]

such that

\[
 d_Q(u)=2r-1\ (u\in U),
 \qquad d_Q(t)=r\ (t\in T),
\tag{6.3}
\]

\(T\) is independent, and \(Q\) contains a spanning linear forest of
\(N\) paths of length \(r\), with one prescribed endpoint in \(U\) and
one in \(T\) on every path.  In particular \(Q\) has all graph-level
data (0.4) and (3.2), but

\[
                         \operatorname {tr}A(Q)^3=0.
\tag{6.4}
\]

#### Proof

Split both \(U\) and \(T\) equally between two bipartition classes.  Each
class then has total prescribed degree

\[
 {rN\over2}(2r-1)+{N\over2}r=r^2N.
\tag{6.5}
\]

First place the \(N\) disjoint alternating paths.  If \(r\) is odd,
orient half from each side, so every path uses equally many vertices on
the two sides.  If \(r\) is even, put the two endpoints of half the paths
on one side and the endpoints of the other half on the other side.  This
uses exactly \(rN/2\) vertices of \(U\) and \(N/2\) vertices of \(T\)
on each side.

Subtract the forest degrees from (6.3).  First satisfy every residual
terminal demand using only vertices of \(U\) on the opposite side.
There are \((r-1)N/2\) terminal stubs on either side and \(rN/2\)
opposite \(U\)-vertices.  A cyclic assignment gives every terminal
\(r-1\) distinct neighbours, avoids its one forest neighbour, and uses
every \(U\)-vertex at most once.  Make the two assignments symmetrically.
Thus no \(T\)--\(T\) edge is introduced and the remaining demand lies
entirely between \(U_L\) and \(U_R\), with equal totals and maximum
demand at most

\[
                              D=2r-2.
\tag{6.6}
\]

The common remaining total is exact.  The forest uses
\((2r-1)N/2\) units of \(U\)-degree on each side, and the terminal
completion uses a further \((r-1)N/2\).  Hence

\[
 R={rN\over2}(2r-1)-{(2r-1)N\over2}-{(r-1)N\over2}
   =(r-1)^2N.
\tag{6.6a}
\]

We use the following elementary bounded-demand completion fact.  In
\(K_{n,n}\) with a forbidden graph of maximum degree two, any two
nonnegative demand sequences bounded by \(D\), with the same total
\(R\ge2D(D+1)\), have a simple bipartite realization avoiding the
forbidden edges.  To verify it, use the capacitated Hall cut

\[
 a(A)\le e(A,R_0\setminus C)+b(C).
\tag{6.7}
\]

Put \(s=|A|\) and \(t=|R_0\setminus C|\).  If \(t\ge D+2\), then
\(e(A,R_0\setminus C)\ge s(t-2)\ge Ds\ge a(A)\).  If
\(t\le D+1\) and \(s\ge D+2\), then

\[
 e(A,R_0\setminus C)+b(C)
 \ge t(s-2)+R-Dt\ge R\ge a(A).
\]

If both \(s,t\le D+1\), then

\[
 b(C)\ge R-D(D+1)\ge D(D+1)\ge a(A).
\]

These are all cuts, and integral max-flow proves the completion fact.
Apply it to the remaining \(U\)-demands, forbidding the already present
forest edges.  For sufficiently large \(N\), their total exceeds the
displayed threshold by (6.6a).

The completed graph is bipartite, hence triangle-free, while the original
forest remains present, and \(T\) is independent. \(\square\)

Proposition 6.1 is deliberately not claimed to be a Boolean-incidence
construction.  It proves the precise negative statement that degrees,
terminal independence, complement-shaped path coverage, and their
spectral consequences cannot alone imply any positive lower bound on
\(A(M)\).

## 7. Exact remaining theorem

A literal Boolean counterexample must do substantially more than
Proposition 6.1.  Its graph must admit the star orientation (2.1): every
upper \((r+1)\)-set chooses exactly one lower facet as centre, the chosen
centres are exactly \({\cal U}\), and the path forest must use Johnson
edges with the prescribed Dyck/complement labels.  Equivalently, it must
make every flag in (4.6) zero while retaining both incidence matchings.

Conversely, a positive theorem sufficient for a Catalan-size quotient
hexagon bank is exactly

\[
 \boxed{
 \sum_{X\in{\cal U}}
 \sum_{e\in J\setminus(X\cup\{d_X\})}I(X,e)
                         \ge c\,rB.}
\tag{7.1}
\]

The stronger conjecture in the question replaces the right side by
\(c r^2B\).  Nothing in the established port, ballot, degree, blocker,
or spectral identities proves even (7.1).  A proof of (7.1) must use a
new compatibility identity between the three distinct upper centres in
(4.2), (4.5), across different cores.  A disproof must construct an
actual two-matching Dyck/complement path factor for which these closure
flags have total \(o(rB)\), ideally zero.

Finally, even (7.1) is only the quotient-incidence supply theorem.
Equal-phase, old-strand-disjoint extraction and port-monodromy closure are
separate physical gates.
