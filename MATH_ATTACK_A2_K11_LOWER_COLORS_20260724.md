# Second-wave attack through the rank-four intersection colors

Input:

K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md

Date: 2026-07-24.

This note is purely mathematical.  It uses no search, computation, solver,
or web source.

## 1. Outcome

Let \(F\) be the spanning linear forest in \(J(11,5)\) supplied by the
zero-margin normal form.  It has \(c\le6\) path components, all \(462\)
five-set vertices, and \(462-c\) edges with distinct six-set union colors.
The endpoint construction also supplies a perfect inclusion matching
\[
 \Phi:\binom{[11]}5\longrightarrow\binom{[11]}6
\]
such that, after every component is oriented from its opposite leaf toward
its unused-source root, the union color of the outgoing edge from a
nonroot \(S\) is \(\Phi(S)\).  The root's matched six-set is one of the
\(c\) omitted union colors.

For an oriented edge \(e:S\to S^+\), put
\[
 I_e=S\cap S^+,\qquad
 U_e=S\cup S^+=\Phi(S),\qquad
 P_e=U_e\setminus I_e.
\]
Thus \(|I_e|=4\), \(|P_e|=2\).  The principal new theorem is the following.

### Root-corrected intersection-color theorem

For every four-set \(K\), let
\[
 m_K=\#\{e:I_e=K\}.
\]
Let \(Q_K\) count edges for which
\[
 P_e\subset K\subset U_e;
\]
these are exactly the edges whose union contains \(K\) but neither endpoint
contains \(K\).  Let \(\tau_K\) count opposite leaves containing \(K\), and
let \(\delta_K\) count roots whose unused matching extension lies in \(K\)
and whose root contains the other three elements of \(K\).  Then
\[
 \boxed{m_K=Q_K-7-\tau_K+\delta_K.}               \tag{1.1}
\]
Moreover,
\[
 0\le m_K\le6.                                    \tag{1.2}
\]
Since \(c\le6\),
\[
 \boxed{Q_K\ge m_K+1}                             \tag{1.3}
\]
for every \(K\).  At least
\[
 330-15c\ge240
\]
four-sets have \(\tau_K=\delta_K=0\), and every such set satisfies
\[
 \boxed{Q_K=m_K+7.}                               \tag{1.4}
\]

The intersection-color multihypergraph is point-almost-regular.  If \(d_x\)
counts roots whose unused matching edge adds \(x\), and \(\tau_x\) counts
opposite leaves containing \(x\), then
\[
 \boxed{
 \sum_{K\ni x}m_K=168+d_x-\tau_x,
 \qquad 162\le\sum_{K\ni x}m_K\le174.}            \tag{1.5}
\]
There are exact pair and triple projections as well:
\[
 \boxed{
 \sum_{K\supset\{x,y\}}m_K
   =42+q_{xy}+\delta_{xy}-\tau_{xy},}             \tag{1.6}
\]
where \(q_{xy}\) counts forest edges swapping \(x\) and \(y\), and
\[
 \boxed{
 \sum_{K\supset T}m_K=Q_T+\delta_T-\tau_T
 \quad(|T|=3).}                                   \tag{1.7}
\]

There is also a complement-dual forest \(F^\vee\).  Every original edge
has a dual rank-four intersection color \(I_e^\vee\) disjoint from \(I_e\).
If
\[
 w_{K,L}=\#\{e:I_e=K,\ I_e^\vee=L\},
\]
then
\[
 \boxed{w_{K,L}=0\text{ for }K\cap L\ne\varnothing,
 \qquad w_{K,L}\le2.}                             \tag{1.8}
\]
The duality produces a new rank-seven congestion law.  If
\[
 R_e=\Phi(S)\cup\Phi(S^+),
\]
then
\[
 \boxed{\#\{e:R_e=R\}\le6}                        \tag{1.9}
\]
for every seven-set \(R\).

For the central physical paths, \(R_e\) is exactly the OR of an ordinary
five-window.  Therefore:

* every ordinary central rank-seven five-window value occurs at most six
  times;
* at least \(38\) distinct rank-seven values occur among those windows; and
* every coordinate occurs in at least \(49\) of the ordinary central
  rank-seven windows in every \(n_5=132\) mode, and at least \(50\) in the
  \(n_5=133\) slice.

The rank-four support is also large.  At \(n_5=133\), at least \(224\)
distinct selected rank-four pair colors occur as forest intersection
colors.  Across all five \(n_5=132\) modes, at least \(222\) distinct
rank-four colors are forced.  Combining this with (1.4), at least \(132\)
forced physical rank-four colors satisfy
\[
 m_K\ge1,\qquad Q_K=m_K+7\ge8.                   \tag{1.10}
\]
The number is at least \(134\) at \(n_5=133\).

No contradiction is obtained.  In fact, the abstract forest and matching
axioms alone cannot be contradictory: the middle-levels Hamilton-cycle
theorem produces examples with every \(1\le c\le6\).  Any contradiction
must use the additional physical central-window coupling, not merely
linearity and distinct union colors.  The new constraints above isolate
the remaining freedom in the swap-pair distribution \(Q_K\), the root
corrections, and the disjoint-color matrix \(w\).

## 2. The rooted forest and its matching

Let \(\Omega=[11]\).  Write the components of \(F\) as
\[
 S_{i,0}\to S_{i,1}\to\cdots\to S_{i,\ell_i},
 \qquad 1\le i\le c,
\]
oriented toward the root \(S_{i,\ell_i}\).  The opposite endpoint
\(S_{i,0}\) is called the initial leaf.  If a component is an isolated
vertex, it is counted once in each endpoint role.

For every five-set \(S\), define its matching extension
\[
 a(S)=\Phi(S)\setminus S.
\]
For a nonroot \(S\), its parent is
\[
 p(S)=S-\{b(S)\}+\{a(S)\}
\]
for a unique loss coordinate \(b(S)\in S\), and
\[
 \Phi(S)=S\cup p(S).
\]
For a root \(R\), the six-set
\[
 O_R=\Phi(R)=R\cup\{a(R)\}
\]
is unused by the forest.  The \(c\) sets \(O_R\) are exactly the omitted
six-set colors.

For a subset \(A\subseteq\Omega\), use the following endpoint data:

* \(\sigma_A\): number of roots containing \(A\);
* \(\tau_A\): number of initial leaves containing \(A\);
* \(\mu_A\): number of omitted colors containing \(A\);
* \(\delta_A\): number of roots \(R\) for which
  \[
  a(R)\in A,\qquad A\setminus\{a(R)\}\subseteq R.
  \]

Since a matched edge adds only one coordinate,
\[
 \boxed{\mu_A=\sigma_A+\delta_A.}                 \tag{2.1}
\]

## 3. A subset-projection identity

For \(A\subseteq\Omega\), \(|A|=t\le4\), define
\[
 D_A=\#\{e:A\subseteq I_e\}
     =\sum_{\substack{K\supseteq A\\|K|=4}}m_K
\]
and
\[
 Q_A=\#\{e:P_e\subseteq A\subseteq U_e\}.
\]
Thus \(Q_A\) counts used union colors containing \(A\) whose selected
forest edge has neither endpoint containing \(A\).  It is zero for
\(|A|\le1\).

Put
\[
 v_t=\binom{11-t}{5-t},\qquad
 u_t=\binom{11-t}{6-t},\qquad
 b_t=2v_t-u_t.
\]

### Theorem 3.1

For every \(A\) of size at most four,
\[
 \boxed{
 D_A=b_t-(\sigma_A+\tau_A)+\mu_A+Q_A
     =b_t-\tau_A+\delta_A+Q_A.}                  \tag{3.1}
\]
The constants are
\[
 (b_0,b_1,b_2,b_3,b_4)=(462,168,42,0,-7).        \tag{3.2}
\]

### Proof

There are \(v_t\) five-set vertices containing \(A\).  Their degree sum in
the path forest is
\[
 2v_t-(\sigma_A+\tau_A).                         \tag{3.3}
\]
An edge whose union contains \(A\) belongs to exactly one of three classes:

1. both endpoints contain \(A\), counted by \(D_A\);
2. exactly one endpoint contains \(A\), say \(N_A\);
3. neither endpoint contains \(A\), counted by \(Q_A\).

Hence
\[
 D_A+N_A+Q_A=u_t-\mu_A.                          \tag{3.4}
\]
On the other hand, the degree sum (3.3) is
\[
 2D_A+N_A=2v_t-(\sigma_A+\tau_A).                \tag{3.5}
\]
Subtracting (3.4) from (3.5), and then using (2.1), gives (3.1).  ∎

The formula is a full root-correction hierarchy, not merely a four-set
identity.  Its negative constant \(b_4=-7\) is the source of the forced
double-swap load in (1.1).

## 4. Exact four-set multiplicities

Fix \(K\in\binom{\Omega}{4}\).  The seven five-set vertices containing
\(K\) are
\[
 \mathcal V_K=\{K\cup\{z\}:z\in\Omega\setminus K\}.
\]
The forest edges induced by \(\mathcal V_K\) are exactly the edges with
intersection color \(K\).  Let \(r_K\) be the number of components,
including isolated vertices, of this induced seven-vertex forest.
Equivalently, \(r_K\) is the number of one-runs of the property
“contains \(K\)” on the \(c\) forest paths.  Therefore
\[
 \boxed{m_K=7-r_K.}                              \tag{4.1}
\]
In particular,
\[
 0\le m_K\le6.                                   \tag{4.2}
\]

Orient the paths toward their roots.  Let \(g_K\) and \(\ell_K\) count
entries into and exits from \(\mathcal V_K\).  Binary path telescoping
gives
\[
 \boxed{
 r_K=g_K+\tau_K=\ell_K+\sigma_K,}                \tag{4.3}
\]
and hence
\[
 g_K-\ell_K=\sigma_K-\tau_K.                    \tag{4.4}
\]
The degree ledger on the seven marked vertices is
\[
 \boxed{
 2m_K+g_K+\ell_K
   =14-\sigma_K-\tau_K.}                         \tag{4.5}
\]
This implies the endpoint-refined cap
\[
 m_K\le
 \min\left(6,
 \left\lfloor\frac{14-\sigma_K-\tau_K}{2}\right\rfloor\right). \tag{4.6}
\]

For comparison with all \(21\) six-sets containing \(K\), let \(X_K\)
count forest edges whose union contains \(K\) and exactly one endpoint
contains \(K\).  Then
\[
 m_K+X_K+Q_K=21-\mu_K,                           \tag{4.7}
\]
while
\[
 2m_K+X_K=14-\sigma_K-\tau_K.                   \tag{4.8}
\]
Eliminating \(X_K\), using (2.1), gives
\[
 \boxed{
 m_K=Q_K-7-\tau_K+\delta_K,}                     \tag{4.9}
\]
equivalently
\[
 \boxed{
 Q_K+r_K=14+\tau_K-\delta_K.}                    \tag{4.10}
\]

There is also a matching-free form:
\[
 \boxed{
 Q_K=7+m_K+\sigma_K+\tau_K-\mu_K.}               \tag{4.11}
\]
Since \(\mu_K\le c\le6\),
\[
 \boxed{
 Q_K\ge m_K+1+\sigma_K+\tau_K.}                  \tag{4.12}
\]
Thus every four-set is covered by at least one forest edge which swaps two
of its coordinates while retaining the other two in the intersection.

The endpoint corrections are sparse:
\[
 \sum_K\tau_K=5c,\qquad
 \sum_K\sigma_K=5c,\qquad
 \sum_K\delta_K=10c,\qquad
 \sum_K\mu_K=15c.                                \tag{4.13}
\]
Consequently at least
\[
 330-15c\ge240                                   \tag{4.14}
\]
four-sets obey
\[
 \tau_K=\delta_K=0,\qquad
 Q_K=m_K+7,\qquad Q_K+r_K=14.                    \tag{4.15}
\]

Every edge contributes:

* one four-set as its intersection;
* six four-sets to the \(Q_K\) class; and
* eight four-sets to the \(X_K\) class.

Therefore the global checks are
\[
\begin{aligned}
 \sum_Km_K&=462-c,\\
 \sum_KQ_K&=6(462-c),\\
 \sum_KX_K&=8(462-c),\\
 \sum_Kr_K&=1848+c.
\end{aligned}                                    \tag{4.16}
\]
All four identities agree with (4.9)--(4.13).

If
\[
 a_j=\#\{K:m_K=j\},
\]
then
\[
 \sum_{j=0}^6a_j=330,\qquad
 \sum_{j=0}^6j\,a_j=462-c.                       \tag{4.17}
\]
These two moments alone leave substantial slack.

### 4.1 Local matching arcs

For \(z\notin K\), put
\[
 S_z=K\cup\{z\},\qquad
 \phi_K(z)=a(S_z).
\]
The seven arcs
\[
 z\longrightarrow\phi_K(z)
\]
have no loops.  They also have no repeated underlying edge: a two-cycle
\(z\leftrightarrow w\) would give
\[
 \Phi(S_z)=K\cup\{z,w\}=\Phi(S_w),
\]
contrary to the bijectivity of \(\Phi\).

Within a \(K\)-run, the outgoing matching arc from every nonterminal vertex
is exactly the next \(K\)-colored forest edge.  At the terminal vertex, the
arc is cut either because that vertex is a root or because its forest edge
exits \(\mathcal V_K\) by deleting one element of \(K\).  Thus every
\(K\)-run has exactly one noninternal matching arc.

The functional graph of \(\phi_K\) has directed cycles of length at least
three, and every such cycle must be cut at a run terminus.  This gives a
structural explanation of \(m_K\le6\), but no smaller universal upper
bound: a single directed cycle may be cut once.

## 5. Point, pair, and triple degrees

### 5.1 Points

For \(x\in\Omega\), define
\[
 D_x=\sum_{K\ni x}m_K.
\]
Let \(d_x\) count roots whose unused matching extension is \(x\).  Since an
omitted six-set containing \(x\) either has a root containing \(x\), or
adds \(x\),
\[
 \mu_x=\sigma_x+d_x.                             \tag{5.1}
\]
The \(t=1\) case of Theorem 3.1 gives
\[
 \boxed{D_x=168+d_x-\tau_x.}                     \tag{5.2}
\]
Thus
\[
 \boxed{162\le D_x\le174.}                       \tag{5.3}
\]
Since every individual four-color has multiplicity at most six, each point
belongs to at least
\[
 \left\lceil\frac{162}{6}\right\rceil=27
\]
distinct intersection colors of positive multiplicity.

Let \(G_x,L_x\) be the numbers of rootward edges gaining and losing \(x\),
respectively.  Every coordinate is the extension label of exactly \(42\)
matching edges.  Removing the \(d_x\) unused root edges gives
\[
 \boxed{G_x=42-d_x.}                              \tag{5.4}
\]
Pathwise endpoint balance gives
\[
 G_x-L_x=\sigma_x-\tau_x,
\]
so, using \(\mu_x=\sigma_x+d_x\),
\[
 \boxed{L_x=42-\mu_x+\tau_x.}                    \tag{5.5}
\]

Let \(p_x\) count forest edges whose swapped pair \(P_e\) contains \(x\).
Degree summation over the \(210\) five-sets containing \(x\) gives
\[
 2D_x+p_x=420-\sigma_x-\tau_x.
\]
Therefore
\[
 \boxed{
 p_x=G_x+L_x
    =84-\sigma_x+\tau_x-2d_x,}                   \tag{5.6}
\]
and
\[
 72\le p_x\le90,\qquad
 p_x\equiv\sigma_x+\tau_x\pmod2.                 \tag{5.7}
\]

The exact number of one-runs of coordinate \(x\) on the \(c\) forest paths
is
\[
 \boxed{210-D_x=42+\tau_x-d_x.}                  \tag{5.8}
\]

### 5.2 Pairs

For an unordered pair \(xy=\{x,y\}\), put
\[
 D_{xy}=\sum_{K\supset xy}m_K
\]
and let \(q_{xy}\) count edges with \(P_e=xy\).  Let \(\delta_{xy}\) count
roots whose unused extension is one of \(x,y\) and whose root contains the
other.  The \(t=2\) case of (3.1) gives
\[
 \boxed{
 D_{xy}=42+q_{xy}+\delta_{xy}-\tau_{xy}.}         \tag{5.9}
\]
Thus
\[
 \boxed{36\le D_{xy}\le83.}                      \tag{5.10}
\]
The lower bound uses \(c\le6\); the upper bound is the forest bound on the
induced subgraph of the \(84\) five-sets containing \(xy\).
In particular, every coordinate pair lies in at least six distinct
intersection colors of positive multiplicity.

The corresponding crossing-edge count is
\[
 84-\sigma_{xy}+\tau_{xy}
   -2\delta_{xy}-2q_{xy}\ge0,                    \tag{5.11}
\]
so
\[
 q_{xy}\le
 42-\delta_{xy}
 +\left\lfloor\frac{\tau_{xy}-\sigma_{xy}}2\right\rfloor. \tag{5.12}
\]

The global checks are
\[
\begin{aligned}
 \sum_{x<y}q_{xy}&=462-c,\\
 \sum_{x<y}\delta_{xy}&=5c,\\
 \sum_{x<y}\tau_{xy}&=10c,\\
 \sum_{x<y}D_{xy}&=6(462-c).
\end{aligned}                                    \tag{5.13}
\]

### 5.3 Triples

For a three-set \(T\), let \(Q_T\) count edges whose swapped pair is a
two-subset of \(T\) and whose intersection contains the third element.
Then
\[
 \boxed{
 D_T:=\sum_{K\supset T}m_K
   =Q_T+\delta_T-\tau_T.}                         \tag{5.14}
\]
The induced forest on the \(28\) five-sets containing \(T\) gives
\[
 0\le D_T\le27.                                  \tag{5.15}
\]
Since a leaf contains ten triples and a root-extension correction contains
ten triples, at least
\[
 165-20c\ge45
\]
triples satisfy \(\tau_T=\delta_T=0\), and hence
\[
 D_T=Q_T.                                        \tag{5.16}
\]

## 6. A separate omitted-color concentration law

For a five-set \(A\), let
\[
 h_A=\#\{O_R:A\subset O_R\},\qquad
 \varepsilon_A=2-\deg_F(A).
\]
The six six-set supersets of \(A\) include \(h_A\) omitted colors and
\(\deg_F(A)\) distinct used colors selected on edges incident with \(A\).
Therefore
\[
 \boxed{h_A\le6-\deg_F(A)=4+\varepsilon_A.}       \tag{6.1}
\]
In particular:

* \(h_A=5\) forces \(A\) to be an endpoint;
* \(h_A=6\) forces \(A\) to be isolated; and
* globally,
  \[
  \boxed{\sum_A(h_A-4)_+\le2c.}                  \tag{6.2}
  \]

This does not contradict \(c\le6\), but it prevents the omitted colors from
concentrating arbitrarily around one five-set.

## 7. Complement duality

Consider one rooted component
\[
 S_0\to S_1\to\cdots\to S_\ell.
\]
Put
\[
 U_i=\Phi(S_i),\qquad V_i=\Omega\setminus U_i.
\]
The matching is a bijection, so the \(V_i\), over all components, run
through every five-set exactly once.

Consecutive six-sets \(U_i,U_{i+1}\) both contain \(S_{i+1}\), are
distinct, and therefore intersect exactly in \(S_{i+1}\).  Hence
\[
 V_\ell\to V_{\ell-1}\to\cdots\to V_0
\]
is a path in \(J(11,5)\).  Over all components these paths form a second
spanning linear forest \(F^\vee\) with \(c\) components and distinct union
colors.  Its perfect inclusion matching is
\[
 \Phi^\vee(V_i)=\Omega\setminus S_i.              \tag{7.1}
\]
Its omitted union colors are the complements of the original initial
leaves.

For an original edge \(e:S\to S^+\), write
\[
 a=S^+\setminus S,\qquad b=S\setminus S^+,\qquad
 \gamma=\Phi(S^+)\setminus S^+.
\]
The coordinates \(a,b,\gamma\) are pairwise distinct.  Indeed,
\(\gamma\notin S^+\), so \(\gamma\ne a\), and \(\gamma=b\) would imply
\(\Phi(S^+)=\Phi(S)\).

Now
\[
 R_e=\Phi(S)\cup\Phi(S^+)
     =I_e\mathbin{\dot\cup}\{a,b,\gamma\}
\]
is a seven-set.  The corresponding dual intersection color is
\[
 I_e^\vee=\Omega\setminus R_e.                   \tag{7.2}
\]
Thus
\[
 I_e\cap I_e^\vee=\varnothing.                   \tag{7.3}
\]

### 7.1 The disjoint-color matrix

Define
\[
 w_{K,L}=\#\{e:I_e=K,\ I_e^\vee=L\}.
\]
Then its row sums are \(m_K\), its column sums are the dual multiplicities
\(m_L^\vee\), and it is supported on disjoint pairs \(K,L\).

For fixed disjoint \(K,L\), the three coordinates in
\[
 G=\Omega\setminus(K\cup L)
\]
give exactly three possible original edges, namely the three sides of the
triangle on
\[
 \{K\cup\{g\}:g\in G\}.
\]
All three cannot lie in the forest.  Therefore
\[
 \boxed{w_{K,L}\le2.}                            \tag{7.4}
\]

If equality holds, the two edges are consecutive along one component.
After relabelling \(G=\{g_0,g_1,g_2\}\), their rooted orientation is
\[
 K\cup\{g_0\}\to K\cup\{g_1\}\to K\cup\{g_2\}.
\]
The matching extensions are
\[
 g_0\mapsto g_1,\qquad
 g_1\mapsto g_2,\qquad
 g_2\mapsto g_0.
\]
Thus \(w_{K,L}=2\) is exactly a local directed three-cycle whose third arc
is cut by a root or an exit.  This explains why the matrix cap two is
sharp but does not force a global cycle.

### 7.2 Dual point degrees and gap triples

Let \(\alpha_x\) count components whose original initial matching extension
is \(x\).  The dual endpoint data are
\[
\begin{aligned}
 \tau_x^\vee&=c-\mu_x,\\
 \sigma_x^\vee&=c-\tau_x-\alpha_x,\\
 d_x^\vee&=\alpha_x,\\
 \mu_x^\vee&=c-\tau_x.
\end{aligned}                                    \tag{7.5}
\]
Applying (5.2) to \(F^\vee\) gives
\[
 \boxed{
 D_x^\vee:=\sum_{L\ni x}m_L^\vee
   =168+\alpha_x-c+\mu_x.}                       \tag{7.6}
\]
In particular,
\[
 162\le D_x^\vee\le174.                          \tag{7.7}
\]

Let \(n_R\) count edges for which \(R_e=R\).  By (7.2),
\[
 n_R=m_{\Omega\setminus R}^\vee,
\]
and therefore
\[
 \boxed{0\le n_R\le6.}                           \tag{7.8}
\]
The exact point degrees are
\[
\boxed{
 \sum_{R\not\ni x}n_R=168+\alpha_x-c+\mu_x,}      \tag{7.9}
\]
\[
\boxed{
 \sum_{R\ni x}n_R=294-\alpha_x-\mu_x.}            \tag{7.10}
\]

Finally, let \(k_x\) count edges for which the three-coordinate gap
\[
 \Omega\setminus(I_e\cup I_e^\vee)
 =\{a,b,\gamma\}
\]
contains \(x\).  Since each edge partitions \(\Omega\) into its two
four-colors and this gap,
\[
 \boxed{
 k_x=126-d_x+\tau_x-\alpha_x-\mu_x,}             \tag{7.11}
\]
and
\[
 \sum_xk_x=3(462-c).                             \tag{7.12}
\]

The congestion bound (7.8) concerns unions of two consecutive matched
six-set colors.  It is not automatically a theorem about arbitrary
physical rank-seven word windows.  The next section explains why it does
become physical on the central blocks.

## 8. Coupling back to the central window path

Let
\[
 C_i=A_i\cup A_{i+1}\cup A_{i+2},
 \qquad
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
\]
and let \(H=C_s\) be the omitted seam triple.  Put
\[
 b_H=\mathbf1_{s>0}+\mathbf1_{s<m-3}\in\{1,2\}.
\]
The selected central rank-five triple vertices split into the possibly
empty left and right sequences
\[
 C_0,\ldots,C_{s-1},
 \qquad
 C_{s+1},\ldots,C_{m-3}.
\]
They contain \(m-3\) vertices and induce
\[
 \boxed{e_{\rm cen}=m-3-b_H}                     \tag{8.1}
\]
forest edges.

On the left, the edge \(C_iC_{i+1}\) is oriented
\[
 C_i\to C_{i+1},
\qquad
 \Phi(C_i)=T_i.
\]
Its next matched color is \(T_{i+1}\), so
\[
 R_e=T_i\cup T_{i+1}.
\]
On the right, \(C_iC_{i+1}\) is oriented in the opposite physical
direction, and
\[
 R_e=T_{i-1}\cup T_i.
\]
In either case \(R_e\) is exactly the OR of the corresponding physical
five-window.

The only missing transition when the seam is internal is
\[
 T_{s-1}\longleftrightarrow T_s,
\]
the seam-centered exceptional five-window.  Thus the \(e_{\rm cen}\) dual
colors correspond exactly to all ordinary central five-windows.

### Theorem 8.1: physical rank-seven congestion

Every ordinary central five-window has rank seven, and every one of its
rank-seven values occurs at most six times:
\[
 \boxed{
 \max_R\#\{\text{ordinary central five-windows with OR }R\}\le6.} \tag{8.2}
\]
Consequently the ordinary central five-windows use at least
\[
 \left\lceil\frac{e_{\rm cen}}6\right\rceil       \tag{8.3}
\]
distinct rank-seven values.

Also, the number of these windows omitting a coordinate \(x\) is at most
\[
 D_x^\vee=168+\alpha_x-c+\mu_x.
\]
Hence the exact endpoint-corrected lower bound is
\[
 \boxed{
 \#\{\text{ordinary central five-windows containing }x\}
 \ge e_{\rm cen}-168-\alpha_x+c-\mu_x.}           \tag{8.4}
\]
Since \(D_x^\vee\le174\), this implies the uniform form
\[
 \boxed{
 \#\{\text{ordinary central five-windows containing }x\}
 \ge e_{\rm cen}-174.}                           \tag{8.5}
\]

For \(n_5=133\),
\[
 m=332-n_4,\qquad n_4\le103,
\]
so \(e_{\rm cen}\ge224\).  Thus at least \(38\) distinct seven-set values
occur, and every coordinate occurs in at least \(50\) ordinary central
five-windows.

For all five \(n_5=132\) modes, the stated \(n_4\)-ranges imply
\[
 e_{\rm cen}\ge223.
\]
Explicitly, A, B, and C1 have \(n_4\le104\), C0 and D have
\(n_4\le105\); these are the inequalities \(\Delta_3\ge0\) in their mode
rows.  Together with
\[
 m=333-n_4\quad\text{in A,C0,D},\qquad
 m=332-n_4\quad\text{in B,C1},
\]
and \(b_H\le2\), they give the displayed lower bound.
Thus at least \(38\) distinct seven-set values occur, and every coordinate
occurs in at least \(49\) ordinary central five-windows.

### 8.1 The forced rank-four support

If a central edge is centered on an ordinary physical pair \(B_j\), then
\[
 C_{j-1}\cap C_j=B_j.
\]
At \(n_5=133\), every one of the \(e_{\rm cen}\) central edges is of this
form, and the \(B_j\) are distinct selected rank-four target values.
Therefore at least \(224\) distinct rank-four colors have positive
intersection multiplicity.

The same holds in modes A, B, C1, and D at \(n_5=132\), with at least
\(223\) distinct colors.  Mode C0 has at most one central edge centered on
its extra low pair; all other central intersections are distinct selected
rank-four pair colors.  Hence C0 still forces at least
\[
 e_{\rm cen}-1\ge222
\]
distinct rank-four colors.

Let
\[
 \mathcal G=\{K:\tau_K=\delta_K=0\}.
\]
By (4.14), \(|\mathcal G|\ge240\).  Intersecting \(\mathcal G\) with the
forced physical color family gives:

* at least \(224+240-330=134\) colors at \(n_5=133\);
* at least \(223+240-330=133\) colors in A, B, C1, D; and
* at least \(222+240-330=132\) colors in C0.

For every one of these colors,
\[
 \boxed{m_K\ge1,\qquad Q_K=m_K+7\ge8.}           \tag{8.6}
\]
This is the strongest direct \(c\le6\) constraint obtained from the
rank-four intersection attack.

### 8.2 Exact \(n_5=133\) external point load

At \(n_5=133\), let \(\lambda_x\) count the distinct literal rank-four
boundary values containing \(x\), and let
\[
 h_x=\mathbf1_{x\in H}.
\]
Among the selected rank-four pair colors, exactly \(b_H\) physical endpoint
pair colors fail to occur as central forest intersections.  Let
\(\varepsilon_x\) be their total incidence at \(x\).  The complete
rank-four layer has point degree \(120\), so the central intersection
colors containing \(x\) number
\[
 120-\lambda_x-h_x-\varepsilon_x.                \tag{8.7}
\]
Subtracting this from the global point degree (5.2) gives the exact external
intersection-color load
\[
 \boxed{
 D_x^{\rm ext}
 =48+\lambda_x+h_x+\varepsilon_x+d_x-\tau_x.}    \tag{8.8}
\]
This is an edge-occurrence count with multiplicity; it is not a count of
distinct external rank-four colors.
In particular,
\[
 D_x^{\rm ext}\ge42.                             \tag{8.9}
\]

The central color family has size
\[
 e_{\rm cen}=329-n_4-b_H,
\]
so the external forest has
\[
 133+n_4+b_H-c
\]
edges.  Only \(n_4+b_H+1\) rank-four colors are absent from the central
family.  Since each has multiplicity at most six, the number of external
occurrences which must repeat an already central color is at least
\[
 \boxed{
 \max\{0,\ 127-5(n_4+b_H)-c\}.}                  \tag{8.10}
\]
If this quantity is positive, at least one fifth of it, rounded up, counts
distinct central colors whose total multiplicity is at least two.

### 8.3 Triple projection of the physical filtration

For a three-set \(T\), let:

* \(\lambda_T\) count literal rank-four boundary values containing \(T\);
* \(h_T=\mathbf1_{T\subset H}\); and
* \(\varepsilon_T\) count the excluded endpoint pair colors containing
  \(T\).

The eight rank-four supersets of \(T\) split among the literal boundary
values, \(H\), the central pair colors, and the excluded endpoint pair
colors.  Therefore the number of forced central intersection colors
containing \(T\) is
\[
 8-\lambda_T-h_T-\varepsilon_T.
\]
Combining this with (5.14) gives the physical swap constraint
\[
 \boxed{
 Q_T+\delta_T-\tau_T
 \ge8-\lambda_T-h_T-\varepsilon_T.}              \tag{8.11}
\]
This is a genuine coupling between the abstract forest swaps and the
rank-four boundary filtration.

For completeness, here is the collision-safe \(n_5=132\) version.  Let
\(\lambda_T\) count the distinct literal rank-four target values containing
\(T\), put
\[
 \delta_4=\mathbf1_{\rho=4},\qquad
 h_T=\mathbf1_{T\subset H},
\]
and let \(\varepsilon_T\) count selected rank-four pair target values whose
physical pair witnesses are excluded at the segment endpoints.  In mode C0
only, put \(\xi=1\) if the extra low pair is internal to a central forest
edge, let \(K_\ast\) be that edge's rank-four intersection, and put
\(\kappa_T=\mathbf1_{T\subset K_\ast}\).  In every other case set
\(\xi=0\).  Counting occurrences, so that a possible collision
\(K_\ast\) coincides with an ordinary central rank-four color is counted
correctly, gives
\[
 \boxed{
 Q_T+\delta_T-\tau_T
 \ge
 8-\lambda_T-\delta_4h_T-\varepsilon_T+\xi\kappa_T.} \tag{8.12}
\]
This is the exact mode-uniform triple coupling.

## 9. Why the attack does not contradict \(c\le6\)

The equations close globally:

* (4.9) sums to
  \[
  462-c=6(462-c)-7\cdot330-5c+10c;
  \]
* the point equations sum to
  \[
  4(462-c);
  \]
* the pair equations sum to
  \[
  6(462-c);
  \]
* the dual row and column sums both equal \(462-c\); and
* the three-coordinate gap counts sum to \(3(462-c)\).

The local lower bound \(Q_K\ge m_K+1\) also has ample total capacity:
\[
 \sum_KQ_K=6(462-c)\ge2736,
\]
whereas the sum of the bare lower bounds is far smaller.  Even the at least
\(132\) physical colors with \(Q_K\ge8\) consume only \(1056\) units.

There is a structural reason no forest-only contradiction can exist.
Invoke, as an external established theorem, the middle-levels
Hamilton-cycle theorem for the bipartite inclusion graph on the five- and
six-subsets of \([11]\).  It is not reproved in this note.  Write such a Hamilton cycle
cyclically as
\[
 S_0,U_0,S_1,U_1,\ldots,S_{461},U_{461},S_0,
\]
where \(U_i\supset S_i,S_{i+1}\).  Define the perfect matching
\[
 \Phi(S_i)=U_i.
\]
Delete any \(c\) of the upper vertices \(U_i\), with \(1\le c\le6\).
Project every remaining two-edge segment
\[
 S_i-U_i-S_{i+1}
\]
to the Johnson edge \(S_iS_{i+1}\).  The result is a spanning linear forest
on all five-sets, with \(c\) components and distinct union colors.  Orient
each projected edge \(S_i\to S_{i+1}\).  Whenever \(U_i\) was deleted,
\(S_i\) is a root and its matched color \(\Phi(S_i)=U_i\) is omitted.
Thus the abstract forest, matching, and root axioms used in Sections 2--7
are realized for every \(1\le c\le6\).

This construction does not assert realization of the zero-margin physical
window template or its endpoint offset states.  It proves only that any
contradiction must use those additional data.  Intersection multiplicity,
point degree, root correction, and union-rainbow linearity alone cannot
finish the problem.

## 10. Adversarial audit

### 10.1 Endpoint tokens

Every component contributes one root token and one opposite-leaf token.  An
isolated component contributes both tokens at the same vertex.  With this
convention, the degree deficit in (3.3) is exact and no singleton component
is lost.

### 10.2 The meaning of \(Q_A\)

For an edge with
\[
 U_e=I_e\mathbin{\dot\cup}P_e,
\]
neither endpoint contains \(A\subseteq U_e\) exactly when both swapped
coordinates lie in \(A\).  Thus the definition
\[
 P_e\subseteq A\subseteq U_e
\]
is equivalent to the third class in (3.4); it neither misses nor
double-counts an edge.

### 10.3 Root/omitted-color pairing

The identity \(\mu_A=\sigma_A+\delta_A\) uses the canonical inclusion
matching \(\Phi\).  It is not a consequence of an arbitrary rainbow forest
without that matching.  The zero-margin endpoint construction supplies
\(\Phi\), and the report never applies the root-corrected formulas without
this hypothesis.

### 10.4 Repeated intersection colors

Distinct union colors do not imply distinct intersection colors.  A fixed
four-set \(K\) can occur six times: the seven vertices \(K\cup\{z\}\) may
form a path.  The cap six, rather than one, is sharp at the local forest
level.

### 10.5 Dual-color multiplicity

For fixed disjoint \(K,L\), exactly three possible edges have that color
pair.  Any two share a vertex and are consecutive; all three form a
triangle and are forbidden.  This proves \(w_{K,L}\le2\), but it does not
prove \(w_{K,L}\le1\).

### 10.6 Physical rank-seven scope

The seven-set congestion theorem (7.8) concerns unions of consecutive
matched six-set colors.  Outside the central blocks these need not be ORs
of one physical word interval.  On the central blocks the canonical
matching is \(C_i\mapsto T_i\) or \(C_i\mapsto T_{i-1}\), so the union is
exactly one physical five-window.  The physical conclusion in Theorem 8.1
is therefore valid only there.

### 10.7 Mode C0

Mode C0 may have one central edge centered at its extra low pair.  Its
rank-four intersection is a four-set, but need not be a new selected
rank-four pair color.  This is why the universal forced-support bound is
\(222\), not \(223\).

### 10.8 The Hamilton-cycle dependency

The forest-only noncontradiction construction invokes the established
middle-levels Hamilton-cycle theorem and does not prove that theorem here.
None of the multiplicity, root-correction, duality, or physical central
constraints depends on that invocation; it is used only to show that the
abstract forest axioms themselves admit models.

## 11. Final theorem ledger and remaining gate

The following are unconditional consequences of the zero-margin forest and
its canonical matching:

1. the exact subset-projection hierarchy (3.1);
2. the multiplicity/run law \(m_K=7-r_K\);
3. the root-corrected law (4.9);
4. \(Q_K\ge m_K+1\) for every four-set and
   \(Q_K=m_K+7\) for at least \(240\) four-sets;
5. the point-almost-regular law (5.2), pair law (5.9), and triple law
   (5.14);
6. the omitted-color concentration law (6.1);
7. the complement-dual forest, disjoint-color matrix cap two, and
   rank-seven congestion bound six;
8. the physical central rank-seven consequences (8.2)--(8.5);
9. at least \(132\) forced physical rank-four colors obey the eight-unit
   double-swap constraint (8.6); and
10. the exact external point load and triple couplings
    (8.8)--(8.12).

No contradiction with \(c\le6\) follows.  The remaining obstruction is now
sharply localized: the abstract identities leave the swap-pair flags
\(P_e\), equivalently the vector \(Q_K\), free enough to absorb every
endpoint correction.  A finishing lemma must couple those swap flags, or
the dual matrix \(w_{K,L}\), to the physical central rank-four path more
strongly than (8.6), (8.11), and (8.12).  Alternatively, it must improve the central
rank-seven congestion bound by using physical overlap beyond the abstract
dual forest.
