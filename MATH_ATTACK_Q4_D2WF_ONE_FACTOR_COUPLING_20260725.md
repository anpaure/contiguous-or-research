# Fourth-wave Q: the depth-two wreath-factor gate inside one exact factor

## Coupled pair curvature, survival-packet locking, and factor-scale trade obstructions

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computational experiment was used.

## 0. Outcome and exact scope

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn,
\qquad N_q=\binom n{m-q}.
\]

For an exact middle wreath factor \(F\), let \(\mu_q^F\) be its cyclic
rank-\((m-q)\) interval histogram and let

\[
H_q(F)=N_q-|\operatorname{supp}\mu_q^F|.
\]

The exact remaining theorem is

\[
\tag{D2WF}
\exists F_m\text{ exact with }H_1(F_m)+H_2(F_m)=o(W).
\]

The previously proved intact-cycle conversion says

\[
\tag{0.1}
L_{[m-2,m+2]}
\le W+4B+2H_1(F)+H_2(F).
\]

This report does **not** prove D2WF. It proves a new package of exact
one-factor theorems and exhausts the direct survival-Hall and bounded-trade
routes at their present strength.

The only imported mathematical inputs are: existence of exact middle
wreath factors (frozen in the project brief), the intact depth-two
cycle-to-word inequality (0.1), the already audited survival-packet
equivalence and rank-three threshold rounding, and the already proved
two-old/two-new topology and depth-one nonneutrality of an exact balanced
\(C_8\). All new coupling, curvature, refactor, and edit statements below
are proved here and were independently rederived.

1. The level-one occurrence graph of every exact factor is an Eulerian
   transversal of the middle diamonds. Its isolated vertices are exactly
   the depth-one holes, and its missing intersection colours are exactly
   the depth-two holes.

2. If \(H_1=o(W)\), then after deleting \(o(W)\) selected middle edges,
   every fixed depth-two colour class is a matching on its rank-
   \((m-1)\) ports. Thus a linear depth-two defect, if present, is forced
   to be dispersed across essentially disjoint depth-one ports. This is a
   theorem about every genuine exact factor, not a local propagation
   counterexample.

3. The first two load profiles satisfy an exact pair-curvature identity.
   Two nonnegative \(2B\)-regular pair multigraphs occur, and they are
   coupled much more rigidly than their margins suggest: one is a sum of
   \(B\) Hamilton cycles and the other is the sum of the distance-three
   chord factors of those **same** Hamilton cycles. Explicitly,

   \[
   G_2-2G_1
   =\frac{B(m-1)(m-12)}{(m+2)(m+3)}\mathbf1+A_{m-1}.
   \]

   This is a new exact-factor rejection certificate. It is not a lower
   bound on \(H_1+H_2\).

4. Survival packets give a sharp dichotomy. A hard packet cover by \(k\)
   wreaths implies

   \[
   2H_1+H_2\le3nk.
   \]

   Rank-three rounding therefore makes a fractional cover of mass
   \(o(B)\) sufficient for D2WF and for (0.1). In contrast, every soft
   deletion-plus-violation objective collapses exactly to the original
   overload; deleting rows cannot fill a support hole.

5. If D2WF fails by a fixed positive density, a globally best exact factor
   contains \(\Omega(B)\) pairwise row-disjoint two- or three-wreath
   survival packets. Every such packet is integrally coverage-locked
   against every exact refactorization of its own middle support;
   fractionally, it is either dual-certified optimal or separated by a
   genuine integrality gap. This is an exact-factor invariant obstruction
   forced by failure of D2WF.

6. Depth-\(q\) support is \(2q\)-Lipschitz in Kneser-factor edge-edit
   distance. Hence reducing a linear depth-two defect requires changing
   \(\Omega(W)\) factor edges, equivalently refactoring \(\Omega(B)\)
   wreaths in one shot. A bounded alternating \(C_8\) changes
   \(H_1+H_2\) by at most \(24\), so \(\Omega(W)\) such switches are
   required in the linear-defect regime.

7. The exact quadratic trade potential has a positive-semidefinite
   interaction law. At a one-switch local minimum, a beneficial
   simultaneous packet must have quantitatively negative cross-shadow
   overlap. A pure depth-two repair assembled from exact \(C_8\)'s cannot
   be shadow-disjoint: restoring the depth-one histogram forces a linear
   number of cross-cancellation contacts.

The surviving construction is therefore global. One must either construct
an exact factor already satisfying the coupled pair-curvature stability, or
perform a factor-scale rebundling whose new wreaths explicitly refill the
old core holes. The packet and bounded-switch estimates proved here do not
themselves provide that rebundling.

## 1. Exact notation and the level-one diamond graph

Throughout Sections 1--2 assume \(m\ge3\). All asymptotic applications
later use \(m\ge8\).

Represent each wreath row by an oriented cyclic order

\[
C=(c_0,c_1,\ldots,c_{n-1}),
\]

with indices in \(\mathbb Z_n\), and write \(I_C(j,r)\) for its cyclic
length-\(r\) interval beginning at \(j\). Put

\[
T_j=I_C(j,m),\qquad
L_j=I_C(j+1,m-1),\qquad
K_j=I_C(j+2,m-2).
\tag{1.1}
\]

Thus the \(T_j\)'s, over all rows, partition \(\binom{[n]}m\), while the
\(L_j\)'s and \(K_j\)'s have histograms \(\mu_1\) and \(\mu_2\).

### Theorem 1.1 (exact coloured-diamond encoding)

Let \(\mathcal G_F\) be the graph on \(\binom{[n]}{m-1}\) in which the row
\(C\) contributes the cyclic edges

\[
L_jL_{j+1}\qquad(j\in\mathbb Z_n).
\]

Then:

1. the edge \(L_jL_{j+1}\) has upper colour

   \[
   L_j\cup L_{j+1}=T_{j+1}
   \]

   and lower colour

   \[
   L_j\cap L_{j+1}=K_j;
   \]

2. every middle set is the upper colour of exactly one edge;

3. for every \(L\in\binom{[n]}{m-1}\),

   \[
   \tag{1.2}
   \deg_{\mathcal G_F}(L)=2\mu_1(L);
   \]

4. \(\mathcal G_F\) is Eulerian and is edge-decomposed into the \(B\)
   prescribed row cycles of length \(n\);

5. \(H_1\) is exactly the number of isolated vertices of \(\mathcal G_F\),
   while \(H_2\) is exactly the number of rank-\((m-2)\) labels absent
   among its edge-intersection colours.

#### Proof

The two identities in part 1 follow immediately from (1.1). Exact middle
ownership makes the upper colours \(T_{j+1}\) globally distinct, proving
part 2. Every occurrence of \(L\) in a row has precisely two incident row
edges. Conversely, an incident edge and its row identify that occurrence,
so (1.2) follows. The remaining assertions are now definitions or direct
consequences of (1.2). \(\square\)

This is stronger than an arbitrary Eulerian graph condition. There is one
edge in the middle diamond

\[
\{\{T\setminus\{a\},T\setminus\{b\}\}:a,b\in T,\ a\ne b\}
\]

for every \(T\), and the selected edges must decompose into genuine
wreath-admissible \(n\)-cycles.

## 2. Three-host packets and the port-dispersion theorem

Fix one occurrence \(K=K_j\). Set

\[
a=c_j,\qquad b=c_{j+1},\qquad
c=c_{j+m},\qquad d=c_{j+m+1}.
\]

Its three consecutive middle hosts and its two level-one ports are

\[
T_j=K\cup\{a,b\},\quad
T_{j+1}=K\cup\{b,c\},\quad
T_{j+2}=K\cup\{c,d\},
\tag{2.1}
\]

\[
L_j=K\cup\{b\},\qquad L_{j+1}=K\cup\{c\}.
\tag{2.2}
\]

Thus a depth-two occurrence is not merely a selected pair. It carries the
three-vertex path

\[
ab-bc-cd
\tag{2.3}
\]

in the Johnson graph on \(\binom{[n]\setminus K}{2}\).

### Lemma 2.1 (exact three-host packing)

Assume \(m\ge3\). For fixed \(K\), the paths (2.3) belonging to its
distinct occurrences are vertex-disjoint. Globally, every middle set
belongs to exactly three such three-host packets.

#### Proof

If two fixed-\(K\) packets shared a vertex of the two-subset Johnson graph,
then their corresponding lists (2.1) would share a middle host \(T\).
Exact middle ownership places both packet occurrences around the same
unique row occurrence of \(T\). In that row, \(T\) is respectively the
left, central, and right host of exactly three adjacent depth-two
occurrences. Their labels are three distinct cyclic intervals of positive
proper length \(m-2\). Hence at most one of those packets has the fixed
label \(K\), a contradiction. The same description proves that globally
every middle host belongs to exactly three packets. \(\square\)

For \(K\subset L\), let \(d_{K,L}\) be the number of selected edges of
\(\mathcal G_F\) having lower colour \(K\) and incident with port \(L\).

### Theorem 2.2 (exact port identities and dispersion)

Assume \(m\ge3\). For every exact factor,

\[
\tag{2.4}
\sum_{L\supset K}d_{K,L}=2\mu_2(K),
\qquad
\sum_{K\subset L}d_{K,L}=2\mu_1(L).
\]

Every occupied \(L\) is incident with at least two distinct lower colours
\(K\). Consequently

\[
\boxed{
E_{\rm port}(F):=
\sum_{K\subset L}(d_{K,L}-1)_+
\le
2\bigl((W-N_1)+H_1\bigr)
=\frac{4W}{m+2}+2H_1.}
\tag{2.5}
\]

There is a set of at most \(E_{\rm port}(F)\) selected middle edges whose
deletion leaves, for every fixed \(K\), a matching on the ports
\(\{K\cup\{x\}:x\notin K\}\).

#### Proof

Each edge of lower colour \(K\) has two ports, and every edge incident with
\(L\) is counted once, proving (2.4). At one occurrence of \(L_j\), the two
incident edges have lower colours \(K_{j-1}\) and \(K_j\). These are
distinct cyclic intervals. Hence, if \(L\) is occupied, at least two cells
\((K,L)\) are nonzero. Therefore

\[
\sum_{K\subset L}(d_{K,L}-1)_+
=2\mu_1(L)-|\{K:d_{K,L}>0\}|
\le2\mu_1(L)-2.
\]

Summing over the \(N_1-H_1\) occupied labels and using
\(\sum_L\mu_1(L)=W\) gives

\[
E_{\rm port}
\le2W-2(N_1-H_1).
\]

Since \(N_1=mW/(m+2)\), this is (2.5). For every cell with
\(d_{K,L}>1\), choose \(d_{K,L}-1\) of its incident edges for deletion and
take the union of all choices. Its size is at most (2.5), and every
remaining fixed-\(K\) port degree is at most one. \(\square\)

### Corollary 2.3 (linear badness must be port-disjoint)

Suppose \(H_1=o(W)\) but \(H_2\ge\varepsilon W\) along some sequence.
After deleting \(o(W)\) selected middle edges, the fixed-\(K\) owner graphs
are matchings and their total duplicate excess is still

\[
\sum_K(\mu_2(K)-1)_+
\ge \varepsilon W-o(W).
\tag{2.6}
\]

Indeed, before deletion the left side is

\[
W-|\operatorname{supp}\mu_2|
=(W-N_2)+H_2,
\]

and deleting one edge reduces it by at most one. Thus depth-one success
forces a hypothetical linear depth-two obstruction to become dispersed,
not concentrated. A repair mechanism requiring repeated depth-two owners
to meet at a common rank-\((m-1)\) port cannot handle more than \(o(W)\) of
this obstruction.

The conclusion does not bound \(H_2\): a matching on the \(m+3\) ports
over a fixed \(K\) may still contain \(\lfloor(m+3)/2\rfloor\) edges.

## 3. Exact pair curvature and the coupled third-chord invariant

For a row \(C\) and an unordered coordinate pair \(e=\{x,y\}\), let
\(d_C(e)\in\{1,\ldots,m\}\) be the shorter cyclic distance between \(x\)
and \(y\) in \(C\). Define the pair multigraphs

\[
A_d(e)=|\{C\in F:d_C(e)=d\}|.
\tag{3.1}
\]

For \(q=0,1,2\), put

\[
P_q(e)=
\sum_{\substack{S\supset e\\|S|=m-q}}\mu_q(S),
\qquad
G_q(e)=P_q(e)-\binom{n-2}{m-q-2}.
\tag{3.2}
\]

Here \(G_q\) is the pair marginal of \(\mu_q-\mathbf1\), and \(G_0=0\)
by exact middle ownership.

### Theorem 3.1 (coupled Hamilton/third-chord invariant)

Assume \(m\ge4\). There are \(B\) Hamilton cycles \(J_C\) on \([n]\),
one for each row, such that

\[
\tag{3.3}
A_m=\sum_{C\in F}\mathbf1_{E(J_C)}
\]

and

\[
\tag{3.4}
A_{m-1}=\sum_{C\in F}\mathbf1_{E(J_C^{[3]})},
\]

where, for a cyclic enumeration \(h_0,\ldots,h_{n-1}\) of \(J_C\),

\[
E(J_C^{[3]})=\{\{h_i,h_{i+3}\}:i\in\mathbb Z_n\}.
\]

Thus the decompositions in (3.3) and (3.4) use the same row cycles.
Moreover,

\[
\boxed{
G_1=\kappa_1\mathbf1+A_m,
\qquad
\kappa_1=\frac{B(m-4)}{m+2},}
\tag{3.5}
\]

\[
\boxed{
G_2=\kappa_2\mathbf1+2A_m+A_{m-1},
\qquad
\kappa_2=
\frac{3B(m^2-5m-4)}{(m+2)(m+3)},}
\tag{3.6}
\]

and hence

\[
\boxed{
G_2-2G_1
=\gamma_m\mathbf1+A_{m-1},
\qquad
\gamma_m=
\frac{B(m-1)(m-12)}{(m+2)(m+3)}.}
\tag{3.7}
\]

Every \(A_d\) is a nonnegative \(2B\)-regular multigraph with total edge
mass \(W\). The graph \(J_C^{[3]}\) is one Hamilton cycle if
\(3\nmid n\), and is three cycles of length \(n/3\) if \(3\mid n\).
The second case is equivalent to \(m\equiv1\pmod3\).

In particular, for \(m>12\),

\[
G_2(e)-2G_1(e)\ge\gamma_m>0
\qquad(e\in\tbinom{[n]}2),
\tag{3.8}
\]

while at the exact endpoint \(m=12\) the constant \(\gamma_m\) is zero.

The bridge to Section 1 is literal: the diamond edge
\(L_jL_{j+1}\), of lower colour \(K_j\) and upper colour \(T_{j+1}\),
selects the pair

\[
T_{j+1}\setminus K_j=\{c_{j+1},c_{j+m}\},
\]

whose cyclic distance is \(m-1\). Thus \(A_{m-1}\) is exactly the
selected-pair multigraph of the coloured-diamond graph.

#### Proof

For one row, its distance-\(m\) graph has edges

\[
\{\{c_i,c_{i+m}\}:i\in\mathbb Z_n\}.
\]

Since \(\gcd(2m+1,m)=1\), this is a Hamilton cycle. Enumerate it by
\(h_t=c_{tm}\). The congruence

\[
3m\equiv m-1\pmod{2m+1}
\tag{3.9}
\]

shows that \(\{h_t,h_{t+3}\}\) is precisely a distance-\((m-1)\) edge in
the original cyclic order. This proves the coupled decompositions and the
component count \(\gcd(n,3)\).

Now fix \(e\), and abbreviate \(d=d_C(e)\). A cyclic \(k\)-interval with
\(k\le m\) contains \(e\) exactly

\[
(k-d)_+
\tag{3.10}
\]

times: no such interval can contain the longer arc between the two points.
Exact middle ownership gives

\[
P_0(e)=C_0:=\binom{n-2}{m-2}.
\]

For every \(1\le d\le m\),

\[
(m-1-d)_+=(m-d)-1+\mathbf1_{\{d=m\}},
\tag{3.11}
\]

\[
(m-2-d)_+=(m-d)-2
+2\mathbf1_{\{d=m\}}+\mathbf1_{\{d=m-1\}}.
\tag{3.12}
\]

Summing over the \(B\) rows gives

\[
P_1=C_0-B+A_m,
\qquad
P_2=C_0-2B+2A_m+A_{m-1}.
\tag{3.13}
\]

Set

\[
C_1=\binom{n-2}{m-3},\qquad
C_2=\binom{n-2}{m-4}.
\]

The exact ratios are

\[
C_0=\frac{B(m-1)}2,
\qquad
\frac{C_1}{C_0}=\frac{m-2}{m+2},
\qquad
\frac{C_2}{C_0}
=\frac{(m-2)(m-3)}{(m+2)(m+3)}.
\tag{3.14}
\]

Subtracting \(C_1\) and \(C_2\) from (3.13), followed by direct
simplification with (3.14), gives (3.5) and (3.6). Finally,

\[
\kappa_2-2\kappa_1
=\frac{B(m-1)(m-12)}{(m+2)(m+3)},
\]

which proves (3.7). In one cyclic order every point has exactly two
partners at each shorter distance \(d\); hence every \(A_d\) is
\(2B\)-regular. Each row contributes \(n\) such edges, so the total mass is
\(nB=W\). \(\square\)

### 3.1 All-depth curvature

The same calculation gives a useful exact extension. Extend (3.2) through
\(0\le q\le m-1\), using the convention
\(\binom{N}{-1}=0\). For \(0\le q\le m-1\), let

\[
C_q=\binom{n-2}{m-q-2}.
\]

Then

\[
\tag{3.15}
P_q=C_0-qB+
\sum_{s=0}^{q-1}(q-s)A_{m-s},
\]

and, for \(1\le q\le m-2\),

\[
\boxed{
G_{q+1}-2G_q+G_{q-1}
=(2C_q-C_{q-1}-C_{q+1})\mathbf1+A_{m-q}.}
\tag{3.16}
\]

Indeed, if \(d=m-t\), then

\[
(m-q-d)_+
=(m-d)-q+
\sum_{s=0}^{q-1}(q-s)\mathbf1_{\{d=m-s\}},
\]

which proves (3.15); taking a discrete second difference proves (3.16).
Thus the long-distance pair graphs are the exact nonnegative curvature
terms of the entire lower cycle tower.

### 3.2 A robust necessary stability consequence

Let \(r_q=m-q\), \(\lambda_q=W/N_q\), and let

\[
\overline A=\frac{W}{\binom n2}=\frac Bm
\tag{3.17}
\]

be the mean edge multiplicity of every \(A_d\). For a signed pair weight
\(y=(y_e)\), put

\[
Y_r(S)=\sum_{e\in\binom S2}y_e.
\]

Subtracting the uniform pair margins from (3.5) and (3.7) gives the exact
identities

\[
\tag{3.18}
\sum_e y_e(A_m(e)-\overline A)
=\sum_{|S|=r_1}Y_{r_1}(S)(\mu_1(S)-\lambda_1),
\]

\[
\tag{3.19}
\sum_e y_e(A_{m-1}(e)-\overline A)
=\sum_{|S|=r_2}Y_{r_2}(S)(\mu_2(S)-\lambda_2)
-2\sum_{|S|=r_1}Y_{r_1}(S)(\mu_1(S)-\lambda_1).
\]

If \(\max_{|S|=r_1,r_2}|Y_{|S|}(S)|\le1\), then

\[
\left|\sum_e y_e(A_m(e)-\overline A)\right|
\le2((W-N_1)+H_1),
\tag{3.20}
\]

\[
\left|\sum_e y_e(A_{m-1}(e)-\overline A)\right|
\le2((W-N_2)+H_2)+4((W-N_1)+H_1).
\tag{3.21}
\]

To see the constants, for an integer histogram \(\mu\) of total \(W\),

\[
\|\mu-\lambda\mathbf1\|_1
\le \|\mu-\mathbf1\|_1+(\lambda-1)N
=2((W-N)+H).
\tag{3.22}
\]

Therefore D2WF would force both coupled long-distance graphs to be
\(o(W)\)-close to uniform in this Boolean pair-sum dual norm. This is a
necessary stability theorem, not a construction: the norm is too weak by
itself to recover the rowwise Hamilton decomposition or exact middle
ownership.

### 3.3 Exact obstruction scope

The pair identities impose additional constraints beyond the displayed
total and point margins.
Any proposed depth-one/depth-two load pair coming from one exact factor
must admit **one common** collection of Hamilton cycles satisfying

\[
G_1-\kappa_1\mathbf1=\sum_C\mathbf1_{E(J_C)},
\]

\[
G_2-2G_1-\gamma_m\mathbf1
=\sum_C\mathbf1_{E(J_C^{[3]})}.
\]

They do not imply \(H_1+H_2=\Omega(W)\), and they are not sufficient for
factor realizability: they do not assert that the middle intervals attached
to the row cycles partition \(\binom{[n]}m\).

For later use, if \(F,F'\) are exact factors, subtracting their identities
gives

\[
\Delta G_1=\Delta A_m,
\qquad
\Delta G_2-2\Delta G_1=\Delta A_{m-1}.
\tag{3.23}
\]

Both signed pair graphs on the right have zero degree at every coordinate,
because every \(A_d\) is \(2B\)-regular. Their positive and negative edge
multisets therefore decompose into alternating even closed trails. This is
a necessary packetization condition for an exact trade. It is not
sufficient: the positive and negative Hamilton rows and their third-chord
factors must still be coupled as in (3.3)--(3.4), and exact middle
ownership must still hold.

## 4. Survival packets: the hard theorem and the exact soft no-go

Assume henceforth \(m\ge8\). Then

\[
1<\frac W{N_1}=\frac{m+2}{m}<2,
\qquad
1<\frac W{N_2}
=\frac{(m+2)(m+3)}{m(m-1)}<2.
\tag{4.1}
\]

Thus the balanced quotas at depths one and two have values in \(\{1,2\}\).
Fix arbitrary quota functions

\[
\beta_q:\binom{[n]}{m-q}\longrightarrow\{1,2\},
\qquad
\sum_S\beta_q(S)=W.
\tag{4.2}
\]

For a target \((q,S)\), let \(\mathcal O_{q,S}\) be the set of wreath rows
that own \(S\). A row owns a fixed target at most once. Its survival packets
are all subsets

\[
P\subseteq\mathcal O_{q,S},
\qquad |P|=\beta_q(S)+1.
\tag{4.3}
\]

Let \(\mathcal P(F,\beta)\) be the union of these packet families over
\(q=1,2\). It has rank at most three. Write \(\theta\), \(\tau\), and
\(\nu\) for its fractional vertex-cover number, integral vertex-cover
number, and matching number, respectively.

For \(X\subseteq F\), put \(k=|X|\), let

\[
\eta_q^X=\mu_q^{F\setminus X},
\]

and define its remaining upper violation

\[
V_q(X)=\sum_S(\eta_q^X(S)-\beta_q(S))_+.
\tag{4.4}
\]

### Theorem 4.1 (weighted Hall ledger)

For arbitrary nonnegative weights \(w_1,w_2\), every deletion
\(X\subseteq F\) satisfies

\[
\boxed{
\sum_{q=1}^2w_qH_q(F)
\le nk(w_1+w_2)+\sum_{q=1}^2w_qV_q(X).}
\tag{4.5}
\]

Moreover,

\[
\boxed{
\min_{X\subseteq F}
\left[n|X|(w_1+w_2)+\sum_qw_qV_q(X)\right]
=\sum_qw_qV_q(\varnothing).}
\tag{4.6}
\]

The same equality holds for fractional deletions \(x_C\in[0,1]\), with
\(|X|\) replaced by \(\sum_Cx_C\) and with the residual loads reduced by
the corresponding owner weights.

#### Proof

At depth \(q\), the residual total is \(W-nk\), while the quota total is
\(W\). Therefore

\[
\sum_S(\beta_q(S)-\eta_q^X(S))_+
=nk+V_q(X).
\tag{4.7}
\]

Every original hole has \(\eta_q^X(S)=0\) and \(\beta_q(S)\ge1\), so it
contributes at least one to the left side of (4.7). This proves (4.5).

Deleting one row removes exactly \(n\) occurrences at each depth. Hence it
can decrease \(V_q\) by at most \(n\), and in general

\[
V_q(X)\ge V_q(\varnothing)-nk.
\tag{4.8}
\]

After weighting and summing, (4.8) says that every expression minimized in
(4.6) is at least its value at \(X=\varnothing\), where equality is
attained. The positive-part function is one-Lipschitz, so the identical
argument proves the fractional assertion. \(\square\)

For the literalization weights \((w_1,w_2)=(2,1)\), (4.5)--(4.6) become

\[
\tag{4.9}
2H_1+H_2\le3nk+2V_1(X)+V_2(X),
\]

\[
\tag{4.10}
\min_X\{3n|X|+2V_1(X)+V_2(X)\}
=2V_1(\varnothing)+V_2(\varnothing).
\]

Thus a soft Hall deletion with residual penalties gives no improvement over
the original weighted upper-quota violation. Optimizing the balanced quota
separately at each depth makes \(V_q(\varnothing)\) the ordinary nearest
balanced overload \(O_q(F)\). Equation (4.10) is an exact no-go for the
soft-deletion architecture, not a claim that \(H_q=O_q\) exactly.
The previously audited depth-two identity gives

\[
H_q\le O_q\le H_q+(W-N_q)
=H_q+O(W/m)
\qquad(q=1,2),
\tag{4.10a}
\]

so soft Hall merely repackages the same asymptotic support gate.

### Corollary 4.2 (hard cover, fractional sufficiency, and packet matching)

A set \(X\) is an integral packet cover if and only if

\[
\eta_q^X(S)\le\beta_q(S)
\qquad(q=1,2; S).
\tag{4.11}
\]

For every such cover of size \(k\),

\[
\boxed{
H_1+H_2\le2nk,
\qquad
2H_1+H_2\le3nk.}
\tag{4.12}
\]

Since the packet rank is at most three, threshold rounding and a maximal
matching give

\[
\tag{4.13}
\tau\le3\theta,
\qquad
\tau\le3\nu.
\]

Consequently

\[
\boxed{
H_1+H_2\le6n\theta,
\qquad
2H_1+H_2\le9n\theta,}
\tag{4.14}
\]

and

\[
\boxed{
H_1+H_2\le6n\nu,
\qquad
2H_1+H_2\le9n\nu.}
\tag{4.15}
\]

In particular, the exact fractional condition

\[
\tag{FH2, sufficient}
\theta(F,\beta)=o(B)
\]

implies D2WF and, by (0.1),

\[
L_{[m-2,m+2]}
\le W+4B+9n\theta=W+o(W).
\tag{4.16}
\]

Conversely, if \(H_1+H_2\ge\varepsilon W\), then for every balanced quota
system

\[
\theta\ge\frac{\varepsilon B}{6},
\qquad
\nu\ge\frac{\varepsilon B}{6}.
\tag{4.17}
\]

Thus a bad actual factor contains a linear matching of pairwise
wreath-disjoint two- or three-row survival packets.

#### Proof

Condition (4.11) is precisely the survival-packet equivalence: more than
\(\beta_q(S)\) surviving owners exist exactly when some
\((\beta_q(S)+1)\)-subset survives. For a hard cover \(V_q(X)=0\), so
(4.12) follows from (4.5). Thresholding a fractional cover at \(1/3\)
gives the first inequality in (4.13). The union of the vertices of any
maximal matching is a vertex cover and has size at most \(3\nu\), proving
the second. The remaining statements follow from (0.1) and
\(W=nB\). \(\square\)

The condition (FH2) is a sufficient gate. No converse inside exact factors
has been proved. In particular, it must not be called equivalent to D2WF.

### Lemma 4.3 (deletion monotonicity)

For every row subfamily \(X\subseteq F\),

\[
\tag{4.18}
H_q(F\setminus X)\ge H_q(F).
\]

This is immediate because deletion only shrinks support. Therefore the hard
cover is a certificate and an extractor; it is not itself a repair of a bad
factor. Any Hall use intended to transform a given bad factor into a better
exact factor must replace the deleted middle support by new genuine
wreaths.

## 5. The exact internal-refactor Hall problem

Let \(X\subseteq F\), put

\[
U=\bigcup_{C\in X}\{I_C(j,m):j\in\mathbb Z_n\},
\qquad G=F\setminus X,
\tag{5.1}
\]

and let the tagged core-hole set be

\[
Z=\{(q,S):q\in\{1,2\},\ \mu_q^G(S)=0\}.
\tag{5.2}
\]

Let \(\mathfrak W(U)\) be the family of all genuine wreaths whose entire
middle support is contained in \(U\). An internal refactorization of \(U\)
is a subfamily \(Y\subseteq\mathfrak W(U)\) whose middle supports partition
\(U\). Then \(F'=G\cup Y\) is again an exact factor.

### Lemma 5.1 (exact refill identity)

For every internal refactorization \(Y\),

\[
\boxed{
H_q(G\cup Y)-H_q(F)
=|\operatorname{supp}\mu_q^X\cap Z_q|
-|\operatorname{supp}\mu_q^Y\cap Z_q|,}
\tag{5.3}
\]

where \(Z_q=\{S:(q,S)\in Z\}\).

#### Proof

Every target outside \(Z_q\) is already covered by \(G\) and remains
covered. The holes of \(G\cup Y\) are precisely
\(Z_q\setminus\operatorname{supp}\mu_q^Y\), while those of
\(F=G\cup X\) are
\(Z_q\setminus\operatorname{supp}\mu_q^X\). Subtracting their cardinalities
gives (5.3). \(\square\)

This identity exhibits the missing operation: the new rows must cover more
of the **core holes** than the old rows did. Merely capping surviving owner
loads cannot do so.

Since each of \(X\) and \(Y\) has \(nk\) colour occurrences at each depth,
(5.3) also gives the universal row-refactor Lipschitz bounds

\[
\boxed{
|H_q(G\cup Y)-H_q(F)|\le nk,}
\tag{5.3b}
\]

\[
\boxed{
|[H_1+H_2](G\cup Y)-[H_1+H_2](F)|\le2nk,}
\tag{5.3c}
\]

and

\[
|[2H_1+H_2](G\cup Y)-[2H_1+H_2](F)|\le3nk.
\tag{5.3d}
\]

### Lemma 5.1b (pair-distance conservation under internal refactoring)

Let \(X\) and \(Y\) be two factorizations of the same middle support \(U\)
into \(k\) wreaths. Then, for every coordinate pair \(e=\{a,b\}\),

\[
\boxed{
\sum_{C\in X}d_C(e)=\sum_{C\in Y}d_C(e).}
\tag{5.3e}
\]

Indeed, one row \(C\) has exactly \(m-d_C(e)\) middle intervals
containing both points of \(e\). Counting the sets in \(U\) that contain
\(e\) gives both

\[
km-\sum_{C\in X}d_C(e)
\quad\text{and}\quad
km-\sum_{C\in Y}d_C(e),
\]

which proves the identity. Thus even a two- or three-wreath Hall packet
cannot be rebundled arbitrarily: every exact alternative preserves its
entire pair-distance sum matrix. This condition is necessary, not
sufficient.

### 5.1 Exact coloured refactor LP and its Hall dual

Give a tag \(a=(q,S)\in Z\) weight \(w_a=w_q\ge0\). For
\(C\in\mathfrak W(U)\), write \(M(C)\) for its \(n\) middle sets and
\(\operatorname{col}_Z(C)\) for the tags in \(Z\) covered by its depth-one
or depth-two intervals. The integral maximum refill is the optimum of

\[
\begin{aligned}
\text{maximize }&\sum_{a\in Z}w_a z_a,\\
\text{subject to }&
\sum_{C:X_0\in M(C)}y_C=1 &&(X_0\in U),\\
&z_a\le\sum_{C:a\in\operatorname{col}_Z(C)}y_C &&(a\in Z),\\
&y_C\in\{0,1\},\qquad 0\le z_a\le1.
\end{aligned}
\tag{5.4}
\]

The middle equalities say exactly that the selected wreaths partition
\(U\). Replacing \(y_C\in\{0,1\}\) by \(y_C\ge0\) gives a fractional
optimum. Equivalently, the
minimum uncovered weight in the fractional relaxation has the dual

\[
\boxed{
\delta_{\rm frac}^w(U,Z)=
\max\left\{
\sum_{a\in Z}p_a-\sum_{X_0\in U}\alpha_{X_0}:
\begin{array}{l}
0\le p_a\le w_a,\\[2mm]
\displaystyle
\sum_{X_0\in M(C)}\alpha_{X_0}
\ge
\sum_{a\in Z\cap\operatorname{col}_Z(C)}p_a
\quad(C\in\mathfrak W(U))
\end{array}
\right\},}
\tag{5.5}
\]

where the middle prices \(\alpha_{X_0}\) are free in sign. Finite linear
programming duality proves (5.5). The true integral minimum uncovered
weight \(\delta_{\rm int}^w(U,Z)\) obeys

\[
\tag{5.6}
\delta_{\rm frac}^w(U,Z)\le\delta_{\rm int}^w(U,Z).
\]

Equivalently, if \(\Phi_{\rm old}\) is the old rows' covered weight and
\(\Phi_{\rm int},\Phi_{\rm frac}\) are the integral and fractional maximum
coverage values, then

\[
\Phi_{\rm old}\le\Phi_{\rm int}\le\Phi_{\rm frac},
\qquad
\delta_*^w=\sum_{a\in Z}w_a-\Phi_*.
\tag{5.6a}
\]

The dual says that middle-set prices must dominate the total rewarded
core-hole coverage on every candidate wreath. Ordinary deletion-packet Hall
does not impose the middle partition equalities in (5.4), and therefore
does not solve this coloured refactor problem.

### Theorem 5.2 (locked-packet obstruction at a global minimizer)

Fix nonnegative weights \(w_1,w_2\), and let \(F_*\) minimize

\[
D_w(F)=w_1H_1(F)+w_2H_2(F)
\]

over all exact factors in the given dimension. For every
\(X\subseteq F_*\), the old row family \(X\) is an integral optimum of
(5.4), and

\[
\tag{5.7}
\delta_{\rm int}^w(U,Z)=D_w(F_*).
\]

In particular, take \(w_1=w_2=1\). If, for some \(\varepsilon>0\),

\[
H_1(F_*)+H_2(F_*)\ge\varepsilon W,
\tag{5.8}
\]

then for every balanced quota system there are at least
\(\varepsilon B/6\) pairwise row-disjoint survival packets of size two or
three. For each such packet \(P\), exactly one of the following two
obstruction descriptions applies:

1. \(\Phi_{\rm frac}(U_P,Z_P)=\Phi_{\rm old}(U_P,Z_P)\), and the dual
   (5.5) supplies an exact middle-price/colour-reward Hall certificate for
   the packet's optimality;

2. \(\Phi_{\rm frac}(U_P,Z_P)>\Phi_{\rm old}(U_P,Z_P)
   =\Phi_{\rm int}(U_P,Z_P)\), so the induced
   coloured wreath-factor polytope on its \(2n\) or \(3n\) middle vertices
   has a genuine integrality gap.

Equivalently, each packet is either certified fractionally or obstructed
integrally; in both cases no exact internal refactor covers more of its
core holes than the old packet.

#### Proof

If an internal refactorization \(Y\) of any \(U\) improved the weighted
coverage in (5.3), then \((F_*\setminus X)\cup Y\) would have smaller
\(D_w\), contradicting global minimality. Hence the old \(X\) is optimal,
and its uncovered core holes are exactly the holes of \(F_*\), proving
(5.7). Under (5.8), Corollary 4.2 supplies the matching of at least
\(\varepsilon B/6\) packets. On each induced finite LP, either equality or
strict inequality holds in (5.6); equality has a dual optimizer by finite
LP duality. \(\square\)

Tags in \(Z_P\) uncovered by every candidate wreath add the same harmless
constant to both uncovered-defect optima. They may be discarded before
reading the first alternative as a local Hall certificate; the relative
coverage formulation above already removes this constant.

If D2WF is false, then along an infinite subsequence there is some
\(\varepsilon>0\) for which every exact factor satisfies (5.8). Theorem
5.2 then gives a positive-density family of disjoint locked packets in an
actual minimizing factor. This is the promised exact-factor obstruction.
It is conditional only in the logically appropriate sense that it describes
what failure of D2WF must look like; none of its structural conclusions is
an abstract non-factor example.

## 6. Exact-factor edit distance forces factor-scale repair

There are two natural edge metrics. Let \(k_K(F,F')\) be the number of old
Kneser-factor edges absent from \(F'\), and let \(k_J(F,F')\) be the number
of old transitions absent from the corresponding reindexed Johnson cycles.
The two metrics must not be confused.

### Theorem 6.1 (radius-colour edit theorem)

For every two exact factors \(F,F'\) and every \(1\le q<m\),

\[
\boxed{
|H_q(F)-H_q(F')|
\le qk_J(F,F')
\le2qk_K(F,F').}
\tag{6.1}
\]

Consequently,

\[
\boxed{
|[H_1+H_2](F)-[H_1+H_2](F')|
\le6k_K(F,F'),}
\tag{6.2}
\]

\[
\boxed{
|[2H_1+H_2](F)-[2H_1+H_2](F')|
\le8k_K(F,F').}
\tag{6.3}
\]

#### Proof

Orient a Kneser wreath and let \(\sigma\) be its successor. Its reindexed
Johnson successor is

\[
\rho=\sigma^2,
\]

which is again an \(n\)-cycle because \(n\) is odd. With a harmless shift
of the starting vertex, a lower depth-\(q\) colour has the form

\[
Y\cap\rho Y\cap\cdots\cap\rho^qY.
\tag{6.4}
\]

It therefore depends on a \(q\)-edge Johnson segment, equivalently a
\(2q\)-edge Kneser segment. A removed Johnson transition lies in exactly
\(q\) such cyclic windows. Every window containing no removed transition
is the same path in both degree-two factors and contributes the same
colour. Hence at most \(qk_J\) colour occurrences move. Replacing one
occurrence changes support size by at most one, proving the first bound.

A derived Johnson edge \(XZ\) has the unique intermediate Kneser vertex

\[
[n]\setminus(X\cup Z).
\]

Thus a removed Kneser edge destroys at most its two incident derived
Johnson transitions, and \(k_J\le2k_K\). Equations (6.2)--(6.3) follow by
weighting (6.1). \(\square\)

### Corollary 6.2 (one-shot rebundling scale)

If \(F'\) is obtained by replacing \(s\) old wreaths by \(s\) new wreaths
on the same middle support, then

\[
k_K(F,F')\le sn.
\tag{6.5}
\]

Therefore, if

\[
H_1(F)+H_2(F)\ge\varepsilon W,
\qquad
H_1(F')+H_2(F')=o(W),
\]

then

\[
\boxed{
s\ge(\varepsilon/2-o(1))B.}
\tag{6.6}
\]

Indeed, this sharper row count follows from (5.3c). Independently,
Theorem 6.1 gives the factor-edge lower bound

\[
k_K(F,F')\ge(\varepsilon/6-o(1))W.
\tag{6.6a}
\]

Thus refactoring \(o(B)\) Hall-selected rows cannot repair a linear defect
in one shot. Such a small refactor is useful only after one has already
reached \(o(W)\) defect, or as one stage of a trajectory whose aggregate
edit mass is factor-scale.

### Corollary 6.3 (balanced \(C_8\) constants)

A balanced alternating \(C_8\) removes four pairwise vertex-disjoint old
Kneser edges. Each removes two distinct reindexed Johnson transitions, so

\[
k_K=4,\qquad k_J=8.
\]

Hence one such switch satisfies

\[
\boxed{
|\Delta H_1|\le8,
\qquad |\Delta H_2|\le16,
\qquad |\Delta(H_1+H_2)|\le24,}
\tag{6.7}
\]

and

\[
|\Delta(2H_1+H_2)|\le32.
\tag{6.8}
\]

Thus lowering \(H_1+H_2\) by \(\varepsilon W\) along a sequence of
balanced \(C_8\)'s requires at least \(\varepsilon W/24\) switches. The
survival-packet scale is \(\Theta(B)\), whereas the bounded-switch scale is
\(\Theta(W)=\Theta(nB)\). Consequently one bounded switch per disjoint
matched packet is quantitatively impossible. If all required switches are
charged to the \(\Theta(B)\) matched packets, the average charge is
\(\Omega(n)\) switches per charged packet; otherwise a different
mesoscopic rebundling resource must be supplied.

## 7. Exact alternating-trade energy and cross-shadow coupling

For \(q=1,2\), define

\[
Q_q(F)=\frac12\sum_S
(\mu_q^F(S)-1)(\mu_q^F(S)-2),
\qquad
\Psi(F)=Q_1(F)+Q_2(F).
\tag{7.1}
\]

If \(a_{q,j}=|\{S:\mu_q(S)=j\}|\), then

\[
\boxed{
Q_q=H_q+
\sum_{j\ge3}\binom{j-1}{2}a_{q,j}.}
\tag{7.2}
\]

Thus \(\Psi=o(W)\) is sufficient for D2WF, but is not equivalent to it
without a separate upper-load bound. If all loads are at most two, then
\(Q_q=H_q\) exactly.

### Theorem 7.1 (exact quadratic interaction law)

Let an exact trade \(F\to F'\) have depth increments

\[
\delta_q=\mu_q^{F'}-\mu_q^F.
\]

Then

\[
\boxed{
Q_q(F')-Q_q(F)
=\langle\mu_q^F,\delta_q\rangle
+\frac12\|\delta_q\|_2^2.}
\tag{7.3}
\]

Suppose legal moves from the same base factor have increments
\(\delta^1,\ldots,\delta^t\), and suppose their simultaneous endpoint is
legal and has increment \(\sum_i\delta^i\). With the direct-sum inner
product over depths one and two,

\[
\boxed{
\Delta\Psi\!\left(\sum_i\delta^i\right)
=\sum_i\Delta\Psi(\delta^i)
+\sum_{i<j}\langle\delta^i,\delta^j\rangle.}
\tag{7.4}
\]

#### Proof

The polynomial in (7.1) is

\[
f(x)=\tfrac12x^2-\tfrac32x+1.
\]

Every histogram increment has total zero. Expanding
\(f(\mu+\delta)-f(\mu)\) and summing therefore cancels the linear
\(-3\delta/2\) term and gives (7.3). Expanding the squared norm of a sum
gives (7.4). Identity (7.2) follows by evaluating \(f(j)\) at nonnegative
integers. \(\square\)

### Corollary 7.2 (negative-overlap necessity)

At a \(\Psi\)-local minimum for a legal move family, every improving legal
simultaneous packet must have

\[
\sum_{i<j}\langle\delta^i,\delta^j\rangle<0.
\tag{7.5}
\]

If the moves are balanced \(C_8\)'s, their two-old/two-new topology gives
\(|\delta_{i,q}(S)|\le2\): one row owns a fixed cyclic target at most once,
so each sign of the increment has target multiplicity at most two. An
improvement of size \(D\) therefore requires
at least \(D/4\) pair-target incidences on which two moves have opposite
signs. Shadow-disjoint or sign-conformal switch packets cannot escape a
local minimum.

The following purely integral cancellation form is independent of the
choice of convex potential. The proved no-neutral-\(C_8\) theorem says that
every exact balanced \(C_8\) has nonzero depth-one increment. For a sequence
of \(t\) such switches, join two switches when their depth-one increments
have opposite signs on some common target. If the final depth-one
histogram equals the initial one, this graph has no isolated vertex and
hence at least \(\lceil t/2\rceil\) edges. More generally, if the final
depth-one \(\ell^1\)-drift is \(\eta\), it has at least

\[
\tag{7.6}
\frac t2-\frac\eta4
\]

edges. Indeed, an isolated nonzero integral zero-sum increment contributes
at least two uncancelled units to the final \(\ell^1\)-drift. Thus a
depth-one-neutral, depth-two-productive alternating trade is intrinsically
mesoscopic and cross-coupled.

### 7.1 One transposition component cube is exactly solvable, but not enough

Fix a coordinate transposition \(\tau\). Overlay the row ownership of
\(F\) and \(\tau F\), and let \(K\) range over its connected components.
Choosing the left or right rows independently in every component gives an
exact factor \(F_s\), indexed by signs \(s_K\in\{\pm1\}\): each middle
set is an overlay edge, and choosing either entire shore of its connected
component covers that edge's middle label exactly once. Let

\[
a_{K,q}=\text{the depth-}q\text{ histogram of the left rows in }K,
\qquad
\delta_{K,q}=(\tau-I)a_{K,q},
\]

and put \(d_K=(\delta_{K,1},\delta_{K,2})\). Then

\[
\mu_{F_s,q}
=g_q+\frac12\sum_Ks_K\delta_{K,q},
\qquad
g_q=\frac{\mu_{F,q}+\tau\mu_{F,q}}2.
\tag{7.7}
\]

The vector \(g_q\) is \(\tau\)-invariant and every \(\delta_{K,q}\) is
\(\tau\)-anti-invariant, so they are orthogonal. Consequently

\[
\boxed{
\Psi(F_s)=C_{F,\tau}
+\frac18\left\|\sum_Ks_Kd_K\right\|_2^2.}
\tag{7.8}
\]

For completeness, the component pairing used here is exact. Every row
\(C\) shares a middle set with \(\tau C\): each transposed coordinate lies
in exactly \(m\) of the row's \(n\) middle intervals, so their total
incidence is \(2m=n-1\); hence some interval contains both or neither and
is fixed by \(\tau\). The ownership overlay therefore connects \(C\) to
\(\tau C\) in the same component. The right-row histogram of a component
is \(\tau a_{K,q}\), proving (7.7). Since the invariant and
anti-invariant subspaces of a transposition are orthogonal, the cross term
in the squared norm vanishes. The linear terms of (7.1) are constant on
histograms of total \(W\), which proves (7.8).

This is an exact zero-field positive-semidefinite sign problem inside the
exact-factor fibre. If

\[
R_\tau=\sum_K\|d_K\|_2^2,
\qquad
D_\tau=\left\|\sum_Kd_K\right\|_2^2,
\]

random signs give expected energy
\(C_{F,\tau}+R_\tau/8\), so \(D_\tau>R_\tau\) guarantees strict exact
descent from the original endpoint. More sharply, if
\(v_s=\sum_Ks_Kd_K\), flipping component \(K\) changes \(\Psi\) by

\[
\tag{7.9}
\frac12\bigl(\|d_K\|_2^2-s_K\langle v_s,d_K\rangle\bigr),
\]

and every component-cube local minimum satisfies

\[
\tag{7.10}
\|v_s\|_2^2\le R_\tau.
\]

Indeed, flipping \(s_K\) replaces \(v_s\) by
\(v_s-2s_Kd_K\), proving (7.9). Summing (7.9) over \(K\) gives
\((R_\tau-\|v_s\|_2^2)/2\), proving (7.10).

However, the cube preserves every target-orbit total:

\[
\mu_{F_s,q}(S)+\mu_{F_s,q}(\tau S)
=\mu_{F,q}(S)+\mu_{F,q}(\tau S).
\tag{7.11}
\]

It fixes \(\mu_q(S)\) itself when \(\tau S=S\). Hence every cube vertex
has the exact hole floor

\[
\boxed{
H_q(F_s)\ge
\sum_{\tau S=S}\mathbf1_{\{\mu_q(S)=0\}}
+\sum_{\{S,\tau S\}}
(2-\mu_q(S)-\mu_q(\tau S))_+.}
\tag{7.12}
\]

For an arbitrary actual hole family \(\mathcal H\subseteq\binom{[n]}r\),
the average number of transposition-fixed holes is exactly

\[
\frac1{\binom n2}\sum_\tau
|\mathcal H\cap\operatorname{Fix}(\tau)|
=p_{n,r}|\mathcal H|,
\tag{7.13}
\]

where

\[
p_{n,r}
=\frac{r(r-1)+(n-r)(n-r-1)}{n(n-1)}
=\frac12+O(1/n)
\tag{7.14}
\]

at the central ranks. Formula (7.13) is obtained by counting, for each
\(S\), the transpositions wholly inside \(S\) or wholly outside \(S\).
Thus a single fixed transposition cube has a large immutable orbit sector
on average. This does not obstruct an adaptive sequence of different
transpositions.

## 8. Combined theorem and the exact remaining construction gate

The preceding results combine into the following alternative.

### Theorem 8.1 (fourth-wave one-factor alternative)

For \(m\ge8\), every exact factor \(F\) satisfies all of the following.

1. **Positive Hall certificate.** If some balanced two-depth quota system
   has fractional survival-packet cover mass \(\theta=o(B)\), then

   \[
   H_1(F)+H_2(F)=o(W)
   \]

   and the intact-cycle word has length

   \[
   L_{[m-2,m+2]}\le W+4B+9n\theta=W+o(W).
   \]

2. **Soft Hall obstruction.** For every balanced quota system, weighted
   deletion with residual violation has the exact value (4.6). It cannot
   improve the original weighted overload. Within this deletion architecture,
   a genuine repair would have to add an explicit internal refactorization
   that covers new core holes.

3. **Factor-scale obstruction.** If \(H_1(F)+H_2(F)\ge\varepsilon W\), no
   one-shot refactorization of \(o(B)\) rows can produce a factor with
   \(o(W)\) defect. It must replace at least
   \((\varepsilon/2-o(1))B\) rows and differ on at least
   \((\varepsilon/6-o(1))W\) old Kneser edges.

4. **Bounded-trade obstruction.** A balanced \(C_8\)-trajectory lowering
   the defect by \(\varepsilon W\) has \(\Omega(W)\) switches. If it keeps
   \(\|\mu_{1,\mathrm{final}}-\mu_{1,\mathrm{initial}}\|_1=o(W)\), all but
   \(o(W)\) of those switches must participate in cross-shadow cancellation
   contacts.

5. **Coupled invariant.** Every intermediate and endpoint exact factor
   must satisfy the diamond-port theorem, the Hamilton/third-chord
   pair-curvature identities, and the pair-distance conservation law on
   every internally refactored support.

If D2WF fails by positive density, a global minimizer additionally has the
locked-packet structure of Theorem 5.2. Thus failure cannot be blamed on
generic bounded-rank set-cover rounding: it must be witnessed inside a
positive-density family of genuine coloured wreath-refactor problems.

#### Proof

Part 1 is Corollary 4.2. Part 2 is Theorem 4.1 with Lemma 5.1. Part 3
uses (5.3c) for the row count and Theorem 6.1 for the edge count. Part 4
is Corollaries 6.3 and 7.2. Part 5 is Theorems 1.1--3.1 with Lemma 5.1b.
The final assertion is Theorem 5.2. \(\square\)

### The remaining exact lemma (unproved)

The analysis isolates the following quantitative statement. It is **not
proved** here.

> **Coloured internal-refactor escape \(\mathrm{CIR2}_\varepsilon\)
> (unproved).** Fix \(\varepsilon>0\). For all sufficiently large \(m\),
> let \(F\) be any exact factor with
> \(H_1(F)+H_2(F)\ge\varepsilon W\). For some balanced two-depth quota
> system, take a maximum matching \(P_1,\ldots,P_\nu\) in its survival-
> packet hypergraph. There is a nonempty subcollection
> \(I\subseteq[\nu]\), with
> \(X=\bigcup_{i\in I}P_i\), and a genuine wreath factorization \(Y\) of
> the same middle support as \(X\), such that
> \[
> H_1((F\setminus X)\cup Y)+H_2((F\setminus X)\cup Y)
> <H_1(F)+H_2(F).
> \]

If \(\mathrm{CIR2}_\varepsilon\) holds for every fixed
\(\varepsilon>0\), then D2WF follows. Indeed, a global minimizer with
defect at least \(\varepsilon W\) would contradict the asserted strict
escape; hence the minimum normalized defect is below every fixed
\(\varepsilon\) for all sufficiently large \(m\).

A one-shot escape from a linear-defect factor necessarily uses
\(\Omega(B)\) rows if its endpoint has \(o(W)\) defect, by (6.6). A
bounded-packet implementation can only work through many coupled stages
with \(\Omega(W)\) aggregate seam edits. Fractional feasibility of (5.4)
is insufficient unless its integral gap and the resulting exact
\(C_n\)-component lengths are controlled.

The symmetric difference of an old and new internal factorization is an
even alternating-cycle bundle in the Kneser graph. Toggling the whole
bundle gives the new exact factor, but an individual alternating cycle need
not preserve the requirement that every component have length \(n\).
Therefore ordinary alternating-cycle decomposition does not prove CIR2.

## 9. Independent audit of the decisive steps

The decisive statements were rederived independently after the first proof.
The audit classifications are as follows.

### 9.1 Valid

1. **Diamond indexing.** With the definitions (1.1), the edge
   \(L_jL_{j+1}\) has union \(T_{j+1}\) and intersection \(K_j\).
   Equation (1.2), the isolated-vertex identity for \(H_1\), and the
   edge-colour identity for \(H_2\) are exact.

2. **Port constant.** The audit recomputed

   \[
   E_{\rm port}
   \le2W-2(N_1-H_1)
   =\frac{4W}{m+2}+2H_1.
   \]

   The use of at least two distinct incident \(K\)-colours at every
   occupied port is valid.

3. **Pair coefficients.** Independent binomial simplification recovered
   exactly

   \[
   \kappa_1=\frac{B(m-4)}{m+2},
   \quad
   \kappa_2=\frac{3B(m^2-5m-4)}{(m+2)(m+3)},
   \quad
   \gamma_m=\frac{B(m-1)(m-12)}{(m+2)(m+3)}.
   \]

   The sign endpoint is exact: \(\gamma_{12}=0\), and positivity begins at
   \(m=13\). The congruence \(3m\equiv m-1\pmod n\), the Hamilton case
   \(3\nmid n\), and the three-cycle case \(3\mid n\) all pass.

4. **Kneser/Johnson factor two.** The audit explicitly distinguished the
   two metrics. A depth-\(q\) colour uses \(q\) reindexed Johnson edges but
   \(2q\) Kneser edges. Thus (6.1), the \(6k_K\) and \(8k_K\) constants,
   and the \(8,16,24\) balanced-\(C_8\) constants are valid.
   Independently, (5.3) gives the row-refactor constants
   \(nk,2nk,3nk\), and hence the \((\varepsilon/2-o(1))B\) row lower
   bound in (6.6).

5. **Hall directions.** The audit checked

   \[
   H_1+H_2\le2n\tau\le6n\theta,
   \qquad
   2H_1+H_2\le3n\tau\le9n\theta.
   \]

   It also checked the exact integral and fractional soft-collapse identity
   (4.6). The variables \(\alpha\) in (5.5) are correctly free, and the
   signs in the refactor dual are correct.

6. **Quadratic interaction.** The zero-total condition removes the linear
   term in (7.3), and the coefficient of every cross inner product in
   (7.4) is exactly one. The audit also confirmed that \(\Psi=o(W)\) is
   sufficient but not equivalent to D2WF without an upper-load cap.

### 9.2 Corrected during audit

1. An early draft blurred Kneser edge edits with reindexed Johnson
   transition edits. The final statement (6.1) records both metrics and the
   necessary factor two.

2. An early formulation called the \(o(B)\) fractional packet condition
   strictly stronger than D2WF. The final report says only
   **sufficient, with no converse proved inside exact factors**. An
   abstract owner-system separation would not establish strictness in the
   exact-factor class.

3. The local Hall obstruction was initially phrased using absolute defect,
   which includes core holes that no local candidate can cover. The final
   coverage formulation \(\Phi_{\rm old},\Phi_{\rm int},\Phi_{\rm frac}\)
   removes this harmless constant before classifying a dual certificate or
   integrality gap.

4. An early description called a locked packet factorization-rigid. The
   proved statement is coverage optimality, not uniqueness: fractionally
   it is either dual-certified or separated by an integrality gap.

5. The targetwise bound \(|\delta_{i,q}(S)|\le2\) for a balanced \(C_8\)
   is now justified explicitly by its two-old/two-new topology and binary
   ownership within each row; it is not inferred from an \(\ell^1\) shadow
   bound.

### 9.3 Unsupported and not used as conclusions

1. No theorem here constructs a factor satisfying D2WF.

2. No theorem shows that the coupled pair-curvature invariant forces a
   positive support defect. It is a necessary rejection certificate only.

3. No theorem gives an integral productive solution of the coloured
   refactor LP (5.4), or proves that its alternating-cycle bundle preserves
   \(C_n\)-component lengths one cycle at a time.

4. No theorem shows that a sequence of different transposition component
   cubes cannot reach D2WF. The immutable floor (7.12) is for one fixed
   transposition cube.

5. No signed-lattice or point-margin example is promoted to an actual
   \(0/1\) exact factor. Packing and exact completion remain decisive.

## 10. Final verdict

The attempted positive routes stop at two exact, now sharply delimited
gates:

\[
\boxed{\text{construct }\theta(F,\beta)=o(B)}
\]

for the hard survival-packet certificate, or

\[
\boxed{\text{prove }\mathrm{CIR2}_\varepsilon
\text{ for every fixed }\varepsilon>0.}
\]

The first is sufficient; no exact-factor converse is known. The second is
the honest iterative trade formulation: it must refill core holes, preserve
the middle partition, obey every pair-distance sum, and realize the
Hamilton/third-chord profiles through the same wreath rows.

The new obstruction is exact. If D2WF fails at positive density, then a
best actual factor contains linearly many disjoint locked survival packets,
each blocked by a finite Hall certificate or a genuine integral gap, while
an endpoint with sublinear defect requires factor-scale rewiring. For
balanced-\(C_8\) trajectories whose final depth-one histogram has
\(o(W)\) \(\ell^1\)-drift from its start, the switches must additionally
have linear cross-shadow cancellation. This
does not settle D2WF, but it rules out soft/uncoupled Hall repair and every
balanced-\(C_8\) conversion that uses \(o(W)\) switches; in the
regime of final depth-one \(\ell^1\)-drift \(o(W)\), it also forces
linearly many cross-shadow contacts inside one exact factor.
