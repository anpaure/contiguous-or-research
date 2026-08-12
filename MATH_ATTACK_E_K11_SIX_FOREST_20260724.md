# Line E: cyclic synchronization of the \(k=11\) six-forest

## 1. Verdict

This route does **not** contradict the zero-margin templates and therefore
does not prove the contiguous-OR width conjecture.

It does give a stronger exact classification of the spanning rainbow forest
from Section 3.5 of K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md.

1. The five-set forest canonically induces a second spanning forest on all
   six-sets, with the same components.
2. Every transition is an exactly labelled nested flag
   \[
   Q\subset Y,\qquad |Q|=4,\quad |Y|=7,
   \]
   whose three labels in \(Y\setminus Q\) are pairwise distinct.
3. The lower rank-four and augmented rank-seven occurrence vectors are fixed
   coordinatewise:
   \[
   L_x=168+d_x-\tau_x,\qquad
   H_x=294-\mu_x-\alpha_x.
   \]
4. A fixed rank-four color and a fixed rank-seven color each occur at most
   six times; a fixed joint \(4\subset7\) flag occurs at most twice.
5. Both extreme layers have unavoidable collision excess at least
   \(132-c\ge126\), with exact pointwise ledgers.
6. The previously free central/external split of the \(42\) matching labels
   is fixed by the long zero-runs of the physical central word:
   \[
   e_x^{\rm cen}=R_x^{(3)}-\mathbf1_{x\notin H},\qquad
   e_x^{\rm ext}=43-\mathbf1_{x\in H}-R_x^{(3)}.
   \]
7. Aggregate coordinate flow, parity, and congestion cannot contradict the
   survivor. An integral Hall argument realizes all three label margins, and
   the established Middle Levels Theorem supplies actual abstract forests
   satisfying all forest/matching/\(42\)-label axioms.

The remaining obstruction is therefore physical synchronization: one must
couple this abstract two-forest object to the six endpoint-offset blocks and
the central window word. The weakest one-unit-gap numerical replacement
lemma is isolated in Section 12.

No finite search, computation, or web lookup is used below.

## 2. Setup and endpoint notation

Let
\[
X=[11],\qquad
\mathcal V_5=\binom X5,\qquad
\mathcal V_6=\binom X6.
\]

Assume precisely the normal form of source Section 3.5:

* \(F\) is a spanning linear forest on \(\mathcal V_5\);
* it has \(c\le6\) components and
  \[
  |E(F)|=462-c;
  \]
* distinct forest edges have distinct rank-six union colors;
* \(M:\mathcal V_5\to\mathcal V_6\) is the endpoint-ordered perfect
  inclusion matching;
* in each component, every forest edge is owned by its tail under \(M\),
  while the root matching edge is unused as a forest color.

To avoid the source's two uses of “source”, call the initial five-set of an
oriented component its **leaf** and the unmatched matching-source its
**root**. Write one component from leaf to root as
\[
S_0,S_1,\ldots,S_r,\qquad U_i:=M(S_i).
\tag{2.1}
\]
Then
\[
U_i=S_i\cup S_{i+1}\quad(0\le i<r),
\tag{2.2}
\]
whereas \(U_r\) is the unused rank-six color at the root. Across all
components, the \(S_i\)'s enumerate \(\mathcal V_5\) and the \(U_i\)'s
enumerate \(\mathcal V_6\).

Define
\[
a_i:=U_i\setminus S_i,\qquad
b_i:=S_i\setminus S_{i+1}\quad(i<r).
\tag{2.3}
\]
Thus \(a_i\) is the matching label at \(S_i\), and
\[
S_{i+1}=S_i-\{b_i\}+\{a_i\}.
\tag{2.4}
\]

For \(x\in X\), let

* \(d_x\) count roots whose matching label is \(x\);
* \(\alpha_x\) count leaves whose matching label is \(x\);
* \(\sigma_x\) count roots containing \(x\);
* \(\tau_x\) count leaves containing \(x\);
* \(\mu_x\) count unused root colors \(U_r\) containing \(x\).

Then
\[
\mu_x=\sigma_x+d_x,
\tag{2.5}
\]
and
\[
\sum_xd_x=\sum_x\alpha_x=c,\qquad
\sum_x\sigma_x=\sum_x\tau_x=5c,\qquad
\sum_x\mu_x=6c.
\tag{2.6}
\]

A singleton component has no forest transition; its sole five-set is both
leaf and root. All formulas below retain that convention.

## 3. Exact coordinate flow on the five-set paths

### Theorem 3.1 (matching and transition margins)

Every coordinate occurs exactly \(42\) times as a matching label. If \(f_x\)
and \(g_x\) count forest transitions gaining and losing \(x\), respectively,
then
\[
\boxed{f_x=42-d_x}
\tag{3.1}
\]
and
\[
\boxed{g_x=42-\mu_x+\tau_x.}
\tag{3.2}
\]
The componentwise zero-run and one-run counts are
\[
\boxed{
Z_x^{(5)}=42+c-\mu_x,\qquad
O_x^{(5)}=42-d_x+\tau_x.
}
\tag{3.3}
\]

#### Proof

There are \(252\) six-sets containing \(x\), while there are \(210\)
five-sets containing \(x\). A matching edge from a source containing \(x\)
also ends at a six-set containing \(x\). Hence exactly
\[
252-210=42
\]
matching edges add \(x\). Removing the \(d_x\) root edges proves (3.1).

Membership conservation from all leaves to all roots gives
\[
f_x-g_x=\sigma_x-\tau_x.
\]
Substitution of (3.1) and \(\mu_x=\sigma_x+d_x\) proves (3.2).

A one-run begins at a leaf containing \(x\), or at a transition gaining
\(x\). A zero-run begins at a leaf omitting \(x\), or at a transition losing
\(x\). Therefore
\[
O_x^{(5)}=\tau_x+f_x,\qquad
Z_x^{(5)}=(c-\tau_x)+g_x,
\]
which is (3.3). \(\square\)

### Theorem 3.2 (pairwise-distinct labels and no internal \(101\))

For every \(0\le i<r\), the coordinates
\[
a_i,\quad b_i,\quad a_{i+1}
\tag{3.4}
\]
are pairwise distinct. Consequently no coordinate-incidence word on a
five-set component contains an internal pattern \(101\); this consequence
uses the displayed assertion for \(0\le i<r-1\).

If \(s\) is the number of singleton components, the total number of
length-one zero-runs over all eleven coordinates is
\[
\boxed{E^{(5),0}_1=2(c-s)+6s=2c+4s.}
\tag{3.5}
\]

#### Proof

The coordinates \(a_i,b_i\) are distinct because one is gained and one is
lost. Also \(a_i\in S_{i+1}\), whereas \(a_{i+1}\notin S_{i+1}\), so
\(a_i\ne a_{i+1}\). If \(b_i=a_{i+1}\), then
\[
U_i=S_{i+1}\cup\{b_i\}
   =S_{i+1}\cup\{a_{i+1}\}
   =U_{i+1},
\]
contrary to injectivity of \(M\).

An internal \(101\) would say that one transition loses \(x\) and the next
gains \(x\), so \(b_i=a_{i+1}=x\). Thus none exists. A nontrivial component
has exactly one boundary length-one zero-run at each end. A singleton
five-set omits six coordinates. Summing gives (3.5). \(\square\)

## 4. The synchronized rank-six forest and exact \(4\subset7\) flags

### Theorem 4.1 (dual rank-six forest)

For every component (2.1), the sequence
\[
U_0,U_1,\ldots,U_r
\tag{4.1}
\]
is a path in \(J(11,6)\). Over all components these paths form a spanning
linear forest \(F_6\) on \(\mathcal V_6\), with the same \(c\) components as
\(F\). Its edges satisfy
\[
U_i\cap U_{i+1}=S_{i+1}.
\tag{4.2}
\]
Thus the \(462-c\) intersection colors of \(F_6\) are exactly the five-sets
other than the \(c\) leaves, each once.

#### Proof

By (2.4),
\[
U_i=S_{i+1}\cup\{b_i\},\qquad
U_{i+1}=S_{i+1}\cup\{a_{i+1}\}.
\]
Theorem 3.2 gives \(b_i\ne a_{i+1}\). Hence the two six-sets are distinct
and have intersection exactly \(S_{i+1}\). Bijection of \(M\) makes the
\(U_i\)'s all \(462\) six-sets, and the intersections are precisely all
nonleaf five-sets. \(\square\)

### Theorem 4.2 (exact labelled flag)

For a forest edge \(S_iS_{i+1}\), put
\[
Q_i:=S_i\cap S_{i+1},\qquad
Y_i:=U_i\cup U_{i+1}.
\tag{4.3}
\]
Then
\[
\begin{aligned}
S_i&=Q_i\sqcup\{b_i\},\\
S_{i+1}&=Q_i\sqcup\{a_i\},\\
U_i&=Q_i\sqcup\{a_i,b_i\},\\
U_{i+1}&=Q_i\sqcup\{a_i,a_{i+1}\},\\
Y_i&=Q_i\sqcup\{a_i,b_i,a_{i+1}\}.
\end{aligned}
\tag{4.4}
\]
In particular,
\[
\boxed{Q_i\subset Y_i,\qquad (|Q_i|,|Y_i|)=(4,7),}
\tag{4.5}
\]
and the three labelled coordinates in \(Y_i\setminus Q_i\) are distinct.

#### Proof

The first four identities follow from (2.2)--(2.4). Theorem 3.2 says that
the three displayed extra coordinates are distinct, and their union gives
the fifth identity. \(\square\)

The final root color \(U_r\), although unused as an \(F\)-edge color, is the
second member of the final pair \(U_{r-1}U_r\). Thus there is exactly one
flag (4.5) per edge of \(F\).

### Corollary 4.3 (complement duality)

Define
\[
\psi(S):=X\setminus M(S),\qquad
M^*(\psi(S)):=X\setminus S.
\tag{4.6}
\]
Then \(M^*\) is a perfect inclusion matching on a second copy of
\(\mathcal V_5\to\mathcal V_6\). An original edge \(S_i\to S_{i+1}\)
becomes
\[
\psi(S_{i+1})\to\psi(S_i).
\]
This complementary-dual construction is involutive when the second
application uses \(M^*\). It swaps roots and leaves and exchanges \(Q_i\)
with the complement of \(Y_i\).

#### Proof

Since \(S\subset M(S)\),
\[
X\setminus M(S)\subset X\setminus S,
\]
and the two ranks are five and six. Bijection follows from bijection of
\(M\). Equation (4.2) and complementation give the dual edge direction and
\[
\psi(S_i)\cap\psi(S_{i+1})=X\setminus Y_i.
\]
On applying the construction again,
\[
X\setminus M^*(\psi(S))=X\setminus(X\setminus S)=S,
\]
so the dualization, rather than necessarily the map \(\psi\) under the
original \(M\), is involutive.
\(\square\)

## 5. Exact point margins on the two extreme layers

Let \(L_x\) be the number, with multiplicity, of \(Q_i\)'s containing \(x\),
and let \(H_x\) be the number, with multiplicity, of \(Y_i\)'s containing
\(x\).

### Theorem 5.1 (lower and upper point laws)

For every \(x\in X\),
\[
\boxed{L_x=168+d_x-\tau_x}
\tag{5.1}
\]
and
\[
\boxed{H_x=294-\mu_x-\alpha_x.}
\tag{5.2}
\]
Equivalently, the ordered partition
\[
X=Q_i\sqcup(X\setminus Y_i)\sqcup(Y_i\setminus Q_i)
\tag{5.3}
\]
of type \((4,4,3)\) has coordinate degrees
\[
\begin{aligned}
\deg_Q(x)&=168+d_x-\tau_x,\\
\deg_{X\setminus Y}(x)&=168-c+\mu_x+\alpha_x,\\
\deg_{Y\setminus Q}(x)&=126-\mu_x-d_x+\tau_x-\alpha_x.
\end{aligned}
\tag{5.4}
\]

#### Proof

The sources of the \(462-c\) forest transitions are all five-sets except
the roots. Their total \(x\)-incidence is \(210-\sigma_x\). Exactly \(g_x\)
of those transitions delete \(x\). Hence
\[
L_x=210-\sigma_x-g_x=168+d_x-\tau_x.
\]

By (4.4), \(Y_i\) is the disjoint union of \(S_{i+1}\), the loss label
\(b_i\), and the next matching label \(a_{i+1}\). The nonleaf targets have
total \(x\)-incidence \(210-\tau_x\); loss labels contribute \(g_x\); and
matching labels on nonleaves contribute \(42-\alpha_x\). Therefore
\[
H_x=(210-\tau_x)+g_x+(42-\alpha_x)
    =294-\mu_x-\alpha_x.
\]
The other two lines of (5.4) are \((462-c)-H_x\) and \(H_x-L_x\).
\(\square\)

The sum checks are
\[
\sum_xL_x=4(462-c),\qquad
\sum_xH_x=7(462-c).
\tag{5.5}
\]

### Corollary 5.2 (run table on the six-set forest)

The zero- and one-run counts of \(x\) on the \(U\)-paths are
\[
\boxed{
Z_x^{(6)}=42+c-\mu_x-\alpha_x,\qquad
O_x^{(6)}=42+\tau_x.
}
\tag{5.6}
\]

#### Proof

The first six-set \(U_0=S_0\sqcup\{a_0\}\) contains \(x\) on exactly
\(\tau_x+\alpha_x\) components. The \(U\)-transitions gain the next labels
\(a_{i+1}\), so they gain \(x\) \(42-\alpha_x\) times. This gives the
one-run formula. They lose the \(b_i\)'s, so
\[
Z_x^{(6)}=(c-\tau_x-\alpha_x)+g_x,
\]
which is the zero-run formula. \(\square\)

Every middle-level parity equation on either layer therefore closes as an
endpoint conservation identity.

## 6. Exact congestion classification

For \(Q\in\binom X4\) and \(Y\in\binom X7\), define
\[
\lambda_Q:=\#\{i:Q_i=Q\},\qquad
\kappa_Y:=\#\{i:Y_i=Y\}.
\]

### Theorem 6.1 (multiplicity six and joint multiplicity two)

For every \(Q,Y\),
\[
\boxed{\lambda_Q\le6,\qquad \kappa_Y\le6.}
\tag{6.1}
\]
A fixed joint flag \(Q\subset Y\) occurs at most twice.

If \(p_Q\) is the number of nontrivial components of the \(Q\)-colored
subgraph, and \(p_Y\) is the analogous number for \(Y\) in \(F_6\), then
\[
\boxed{\lambda_Q+p_Q\le7,\qquad\kappa_Y+p_Y\le7.}
\tag{6.2}
\]

#### Proof

The five-set supersets of \(Q\) are the seven petals
\[
Q\cup\{z\},\qquad z\in X\setminus Q.
\]
The \(Q\)-colored edges form a subgraph of the linear forest \(F\), hence a
linear forest on seven vertices. It has at most six edges. If it has
\(p_Q\) nontrivial components and \(\lambda_Q\) edges, it uses
\(\lambda_Q+p_Q\le7\) vertices.

Dually, the six-set facets of \(Y\) are its seven six-subsets. Edges of
\(F_6\) having union \(Y\) form a linear forest on those facets.

For a fixed pair \(Q\subset Y\), the possible lower endpoints are the three
petals
\[
Q\cup\{z\},\qquad z\in Y\setminus Q.
\]
All possible edges form a triangle. Acyclicity permits at most two.
\(\square\)

### Theorem 6.2 (local deficit/cut identity)

For a four-set \(Q\), put
\[
z_Q:=\sum_{S\supset Q}(2-\deg_FS),
\]
and let \(\delta_Q\) be the number of forest edges with exactly one endpoint
among the seven petals over \(Q\). Then
\[
\boxed{2\lambda_Q+\delta_Q=14-z_Q.}
\tag{6.3}
\]
Moreover,
\[
\sum_Qz_Q=10c,\qquad
\sum_Q\delta_Q=8(462-c).
\tag{6.4}
\]
The identical dual statements hold for seven-set facet families in \(F_6\),
with \(\lambda_Q\) replaced by \(\kappa_Y\).

#### Proof

Degree-summing over the seven petals gives (6.3). The total degree deficit
of \(F\) is
\[
\sum_S(2-\deg_FS)=2c.
\]
Every five-set contains five four-sets, proving \(\sum_Qz_Q=10c\).

For an edge \(ST\), exactly one four-set, \(S\cap T\), lies in both
endpoints. Each endpoint contains five four-sets, so exactly
\(5+5-2=8\) petal families cut the edge. This proves the second identity.
The dual proof is the same: a six-set lies in five seven-sets, and adjacent
six-sets have one common seven-set union. \(\square\)

Summing (6.3) returns only an identity; there is no global cut deficit.

### Theorem 6.3 (exact collision ledgers)

Let \(m_4\) be the number of four-colors with \(\lambda_Q=0\), and let
\(p_x^{(4)}\) count those missing colors containing \(x\). Define
\[
r_x^{(4)}:=\sum_{Q\ni x}(\lambda_Q-1)_+.
\]
Then
\[
\boxed{r_x^{(4)}=48+d_x-\tau_x+p_x^{(4)}}
\tag{6.5}
\]
and
\[
\boxed{\sum_Q(\lambda_Q-1)_+=132-c+m_4.}
\tag{6.6}
\]

Similarly, if \(m_7,p_x^{(7)}\) are the missing rank-seven color count and
its point incidences, then
\[
\boxed{r_x^{(7)}=84-\mu_x-\alpha_x+p_x^{(7)}}
\tag{6.7}
\]
and
\[
\boxed{\sum_Y(\kappa_Y-1)_+=132-c+m_7.}
\tag{6.8}
\]

Every coordinate belongs to at least \(42\) repeated lower occurrences and
at least \(72\) repeated upper occurrences. Each extreme layer has global
collision excess at least
\[
132-c\ge126.
\tag{6.9}
\]

#### Proof

There are \(120\) four-sets containing \(x\), of which
\(120-p_x^{(4)}\) are used distinctly. Thus
\[
r_x^{(4)}
=L_x-(120-p_x^{(4)})
=48+d_x-\tau_x+p_x^{(4)}.
\]
The distinct used four-colors number \(330-m_4\), so
\[
\sum_Q(\lambda_Q-1)_+
=(462-c)-(330-m_4)
=132-c+m_4.
\]
The rank-seven layer has point degree \(210\). The same argument using
(5.2) proves (6.7)--(6.8). Since \(d_x\ge0\),
\(\tau_x,\mu_x,\alpha_x\le c\le6\), the pointwise lower bounds are \(42\)
and \(72\). \(\square\)

These are congestion theorems, not contradictions: multiplicity six leaves
ample capacity.

## 7. The local cyclic selector forced by labelled ownership

### Theorem 7.1 (seven-petal functional digraph)

Fix \(Q\in\binom X4\). For every \(b\in X\setminus Q\), set
\[
S_b:=Q\cup\{b\},\qquad
\phi_Q(b):=M(S_b)\setminus S_b.
\tag{7.1}
\]
Then
\[
D_Q:\ b\longmapsto\phi_Q(b)
\tag{7.2}
\]
is a functional digraph on the seven coordinates of \(X\setminus Q\), with
no loop and no directed two-cycle. Its seven underlying unordered edges are
distinct, so every directed cycle has length at least three.

A rootward forest edge with lower color \(Q\) is exactly a selected arc
\[
b\longmapsto a=\phi_Q(b).
\tag{7.3}
\]
Its upper flag is determined by the length-two successor walk
\[
b\longmapsto a\longmapsto\phi_Q(a),
\tag{7.4}
\]
namely
\[
Y=Q\sqcup\{a,b,\phi_Q(a)\}.
\tag{7.5}
\]

#### Proof

The label \(\phi_Q(b)\) is outside \(S_b\), so it lies in \(X\setminus Q\)
and differs from \(b\). If \(\phi_Q(b)=a\) and \(\phi_Q(a)=b\), then
\[
M(S_b)=Q\cup\{a,b\}=M(S_a),
\]
contradicting injectivity of \(M\). The same argument shows that two
different tails cannot define the same underlying unordered edge.

If \(S_b\to S_a\) has lower intersection \(Q\), its union color is
\(M(S_b)=Q\cup\{a,b\}\), so \(\phi_Q(b)=a\). The next matching label is
\(\phi_Q(a)\), and (4.4) gives (7.5). \(\square\)

This is the exact cyclic synchronization law at one lower color. The forest
selects only \(462-c\) arcs among the \(330\cdot7=2310\) candidate arcs of
all \(D_Q\)'s.

### Corollary 7.2 (lazy extreme-color walks)

Along consecutive flags,
\[
Q_{i+1}=Q_i\quad\Longleftrightarrow\quad b_{i+1}=a_i;
\tag{7.6}
\]
otherwise \(Q_i,Q_{i+1}\) are Johnson-adjacent. Likewise,
\[
Y_{i+1}=Y_i\quad\Longleftrightarrow\quad a_{i+2}=b_i;
\tag{7.7}
\]
otherwise \(Y_i,Y_{i+1}\) are Johnson-adjacent.

#### Proof

Both \(Q_i,Q_{i+1}\) are facets of \(S_{i+1}\). They coincide exactly when
their deleted coordinates \(a_i,b_{i+1}\) coincide. Both \(Y_i,Y_{i+1}\)
contain \(U_{i+1}\); their extra coordinates are \(b_i,a_{i+2}\).
\(\square\)

## 8. Why coordinate flow and color capacity cannot contradict

Let \(N_{a,b,a'}\) count transitions whose current matching label, loss
label, and next matching label are \(a,b,a'\). It is supported on pairwise
distinct triples, with margins
\[
\sum_{b,a'}N_{a,b,a'}=42-d_a,
\tag{8.1}
\]
\[
\sum_{a,a'}N_{a,b,a'}=42-\mu_b+\tau_b,
\tag{8.2}
\]
\[
\sum_{a,b}N_{a,b,a'}=42-\alpha_{a'}.
\tag{8.3}
\]

### Theorem 8.1 (integral three-margin feasibility)

For every actual endpoint vector satisfying (2.5)--(2.6), the aggregate
margins (8.1)--(8.3) admit a nonnegative integral tensor supported on
pairwise distinct triples.

#### Proof

Put
\[
E=462-c\ge456,\qquad
r_a=42-d_a,\qquad t_{a'}=42-\alpha_{a'}.
\]
First construct a loopless integral matrix \(P_{a,a'}\) with row sums
\(r_a\) and column sums \(t_{a'}\). This is an integral transportation flow
on \(K_{11,11}\) with the diagonal removed; off-diagonal cells have
unbounded integral capacity. A set of at least two row labels sees every
column. For a singleton row \(a\), Hall's only nontrivial condition is
\[
r_a+t_a\le E,
\]
which holds because the left side is at most \(84\), while \(E\ge456\).
Integral Hall gives \(P\).

Regard the \(P\)-entries as \(E\) individual slots \((a,a')\), with
\(a\ne a'\). Assign every slot a loss label \(b\notin\{a,a'\}\), with
demands \(g_b=42-\mu_b+\tau_b\). For one loss label \(b\), at most
\(r_b+t_b\le84\) slots are forbidden, while \(g_b\le48\). For two loss
labels \(b_1,b_2\), only slots with endpoint set
\(\{b_1,b_2\}\) reject both; there are at most \(84\), whereas their
combined demand is at most \(96\). Any set of at least three loss labels
sees every slot, because a slot has only two endpoints. Since
\(E-84\ge372\), all Hall inequalities hold. Integral Hall supplies the
loss-label assignment. \(\square\)

This theorem realizes aggregate coordinate roles, not five-set supports or
their sequential order. It proves that the three labelled margins alone
cannot contradict.

There is equally ample unlabelled flag capacity. The containment graph
between four-sets \(Q\) and seven-sets \(Y\) is \(35\)-regular on
\(330+330\) vertices, hence decomposes into perfect matchings. One perfect
matching together with any \(132-c\) edges of a disjoint second matching
gives \(462-c\) distinct flags, covers every extreme color, and has all
extreme multiplicities at most two. This does not satisfy the sequential
subset constraints, but it rules out arguments based only on layer
capacity, Theorem 6.1, or joint-flag capacity.

## 9. New physical-window coupling: the central share of the \(42\) labels

Return to the central word
\[
A_0,A_1,\ldots,A_{m-1},
\]
with
\[
C_i=A_i\cup A_{i+1}\cup A_{i+2},\qquad
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
\]
and seam triple \(H=C_s\). Let \(R_x^{(3)}\) be the number of zero-runs of
\(x\) in the \(A\)-word having length at least three, and put
\[
h_x:=\mathbf1_{x\in H}.
\]

### Theorem 9.1 (exact central/external split)

The number of central matching edges labelled \(x\) is
\[
\boxed{e_x^{\rm cen}=R_x^{(3)}-(1-h_x).}
\tag{9.1}
\]
Consequently,
\[
\boxed{
e_x^{\rm ext}
=42-e_x^{\rm cen}
=43-h_x-R_x^{(3)}\ge0,
}
\tag{9.2}
\]
and
\[
\boxed{R_x^{(3)}\le43-h_x.}
\tag{9.3}
\]

#### Proof

Before the seam, \(C_i\mapsto T_i\) for \(i<s\). This edge is labelled
\(x\) precisely when \(x\) is absent from
\(A_i,A_{i+1},A_{i+2}\) and present in \(A_{i+3}\): it marks the right end
of a zero-run of length at least three.

After the seam, \(C_i\mapsto T_{i-1}\) for \(i>s\). This edge is labelled
\(x\) precisely when \(x\) is present in \(A_{i-1}\) and absent from
\(A_i,A_{i+1},A_{i+2}\): it marks the left end of a long zero-run.

Every long zero-run is counted once unless it contains all seam positions
\(s,s+1,s+2\). Such a run is unique when it exists, exists exactly when
\(x\notin H\), and is counted by neither side. This proves (9.1). The same
argument covers a boundary seam. Equations (9.2)--(9.3) follow from the
\(42\)-label law and nonnegativity. \(\square\)

The global check is exact. Source equation (4.4) gives
\[
\sum_xR_x^{(3)}=m+8-\rho.
\]
Hence
\[
\sum_xe_x^{\rm cen}
=(m+8-\rho)-(11-\rho)
=m-3,
\]
the number of central ordinary triples, and
\[
\sum_xe_x^{\rm ext}=462-(m-3)=465-m.
\tag{9.4}
\]

### Corollary 9.2 (coordinatewise template equations)

Let \(E_{1,x},E_{2,x}\) count zero-runs of \(x\) of exact lengths one and
two. In the \(n_5=133\) slice, with source equation (7.4),
\[
\boxed{
e_x^{\rm ext}
=\lambda_x+r_x+E_{1,x}+E_{2,x}
-22-2h_x-2i_x.
}
\tag{9.5}
\]
In the \(n_5=132\) modes, using source equation (8.6),
\[
\boxed{
e_x^{\rm ext}
=\lambda_x+r_x+E_{1,x}+E_{2,x}-22
+(\delta_4-1)h_x-\ell_x-k_x-X_x.
}
\tag{9.6}
\]
Thus in the rank-four carrier modes,
\[
e_x^{\rm ext}
=\lambda_x+r_x+E_{1,x}+E_{2,x}-22-2\ell_x-X_x,
\tag{9.7}
\]
while in mode D,
\[
e_x^{\rm ext}
=\lambda_x+r_x+E_{1,x}+E_{2,x}-22-2\ell_x-2h_x.
\tag{9.8}
\]

#### Proof

Since
\[
R_x^{(3)}=Z_x-E_{1,x}-E_{2,x},
\]
equation (9.2) becomes
\[
e_x^{\rm ext}=43-h_x-Z_x+E_{1,x}+E_{2,x}.
\]
Substituting source equations (7.4) and (8.6) gives (9.5)--(9.6). In the
rank-four carrier modes \(k_x=\ell_x,\delta_4=1\); in mode D,
\(k_x=\ell_x+h_x,\delta_4=0,X_x=0\). \(\square\)

These are new necessary coordinatewise restrictions. Present control of
the individual \(E_{1,x},E_{2,x}\) does not make a right-hand side negative.

### Proposition 9.3 (internal-seam roots)

For an internal seam, the two central roots are
\[
C_{s-1},\qquad C_{s+1},
\]
with unused colors
\[
T_{s-1},\qquad T_s.
\]
Their labels
\[
x_L:=T_{s-1}\setminus C_{s-1}\subseteq A_{s+2},\qquad
x_R:=T_s\setminus C_{s+1}\subseteq A_s
\tag{9.9}
\]
are distinct elements of \(H\). Moreover,
\[
|T_{s-1}\cup T_s|=7+\eta,\qquad
|T_{s-1}\cap T_s|=5-\eta.
\tag{9.10}
\]

#### Proof

The central matching rule gives the roots and colors. The first label is
absent from \(C_{s-1}\), hence absent from \(A_s\), while the second lies
in \(A_s\). Both lie in \(H\), so they are distinct. Equation (9.10) is
source equations (3.3)--(3.5). \(\square\)

## 10. Physical localization of synchronized colors

### Proposition 10.1 (central lower and upper colors)

Let \(b\in\{1,2\}\) be the number of nonempty central rank-five components:
\(b=2\) for an internal seam and \(b=1\) for a boundary seam. The central
forest contains
\[
m-3-b
\tag{10.1}
\]
edges.

Except for the one extra low pair in mode C0, every such edge
\(C_iC_{i+1}\) has lower color
\[
C_i\cap C_{i+1}=B_{i+1},
\tag{10.2}
\]
and these ordinary pair colors are pairwise distinct. Thus there are at
least
\[
m-3-b-\mathbf1_{\mathrm{C0}}
\tag{10.3}
\]
pairwise distinct central lower colors. In mode C0 the exceptional
intersection is a rank-four superset of the extra low pair and is not
asserted distinct from the ordinary colors.

The synchronized upper colors on these same edges are exactly the unions
of consecutive central four-windows \(T_i,T_{i+1}\), excluding the seam
jump. Every one is an ordinary rank-seven five-window color. They are not
known to be distinct.

#### Proof

There are \(m-3\) ordinary triple targets split into \(b\) path components,
giving (10.1). A retained adjacency never crosses the deleted seam triple.
Whenever its middle pair is ordinary, source equation (3.8) gives (10.2),
and the ordinary rank-four pair targets are distinct. Only mode C0 has one
further low pair away from the seam.

By Theorem 4.1, the corresponding upper edge joins the two matched
four-windows. For an internal seam the two \(T\)-paths are
\[
T_0,\ldots,T_{s-1}
\quad\text{and}\quad
T_{m-4},\ldots,T_s.
\]
They contain every ordinary \(T_iT_{i+1}\) transition and omit only
\(T_{s-1}T_s\). Source equation (3.2) gives rank seven for all ordinary
unions. The boundary-seam case has one path and no seam transition.
\(\square\)

### Proposition 10.2 (adjacent lower repetitions)

Let \(r_4\) count internal vertices of \(F\) at which the two incident
rank-four intersection colors coincide. Such an equality is equivalent to
one internal coordinate pattern \(010\).

Inside a fixed rank-five offset block of physical window length at least
two, no such pattern is possible. Hence adjacent repeated lower colors can
occur only in the literal states \(00,33\), not in
\[
01,02,13,23.
\tag{10.4}
\]

#### Proof

At an internal vertex \(S_i\), equality of the two lower colors means that
both neighbors omit the same unique coordinate \(x\in S_i\), exactly the
pattern \(010\).

In a fixed offset block, the \(S_i\)'s are ORs of equal-length physical
windows shifted by one. If their length is at least two, the union of the
two flanking physical windows covers the middle physical window. A
coordinate absent from both flanking ORs cannot be present in the middle
OR. States \(01,23\) have length two, states \(02,13\) have length three,
and only \(00,33\) have length one. \(\square\)

This localizes adjacent collisions but does not control separated
reappearances of the same rank-four color.

## 11. Endpoint-root augmentation

The original \(F\) deletes every transition between consecutive nonempty
offset-state blocks. Some peripheral deletions can be restored using an
omitted root matching color.

### Proposition 11.1 (forced peripheral closures)

At a same-side state boundary, suppose the relevant root's unused rank-six
witness interval contains the neighboring leaf's rank-five witness
interval. Adding the edge between those five-sets:

1. uses exactly that previously omitted rank-six color;
2. preserves distinct union colors;
3. joins two path endpoints, preserving linearity and acyclicity; and
4. preserves labelled ownership by \(M\).

When the two displayed states are consecutive nonempty blocks, physical
offsets force containment in these cases:
\[
\begin{array}{c|c}
\text{state boundary}&\text{root rank-six states forcing closure}\\ \hline
00\to01&02,03\\
01\to02&03\\
13\to23&03\\
23\to33&03,13.
\end{array}
\tag{11.1}
\]
Thus a break at one of these four listed boundaries, if it survives all
listed forced closures, must use the minimal root states
\[
01,\quad02,\quad13,\quad23
\tag{11.2}
\]
at the respective boundaries. This is necessary only: a minimal state may
still close accidentally at the OR-set level. If an intermediate block is
empty, two further same-side boundaries can occur: at \(00\to02\), root
state \(03\) forces closure; at \(13\to33\), the later root state \(03\)
forces closure. Other cross-orientation skipped boundaries are not
classified by this proposition.

The central \(02\to13\) break cannot close, because the union of its
adjacent five-set targets is
\[
T_{s-1}\cup T_s
\]
of rank \(7+\eta\), not six.

#### Proof

Two distinct five-sets contained in a six-set have that six-set as their
union. The added edge therefore has the unused root color. It connects two
component endpoints, and the color was previously unused.

For \(00\to01\), the root five-interval is \([j,j]\), while the next leaf
is \([j+1,j+2]\). Root six-interval states \(02,03\) are
\([j,j+2]\), \([j,j+3]\), so both contain the leaf; state \(01\) need not.
The other rows follow by the same offset calculation, with reversed
orientation on the right. The central assertion is (9.10). \(\square\)

## 12. Exact obstruction and weakest one-unit replacement lemma

For each used lower color \(Q\), let \(p_Q\) be its number of nontrivial
colored components, and let \(r_4\) be the adjacent-repeat count from
Proposition 10.2. Then
\[
\sum_Q(\lambda_Q-1)_+
=r_4+\sum_{Q:\lambda_Q>0}(p_Q-1).
\tag{12.1}
\]
Indeed, the \(Q\)-colored components contain \(\lambda_Q\) edges in
\(p_Q\) path pieces. Their adjacent repetitions total \(\lambda_Q-p_Q\);
the remaining \(p_Q-1\) is separated reappearance.

Combining (12.1) with (6.6) gives the exact obstruction
\[
\boxed{
r_4+\sum_{Q:\lambda_Q>0}(p_Q-1)
=132-c+m_4.
}
\tag{12.2}
\]
Proposition 10.2 controls only the first term, by localization. Nothing
presently controls the separated-reappearance term. The dual rank-seven
word has the identical obstruction.

The weakest integer upper bound, with the actual missing-color count
retained, that would finish this route by a one-unit gap is:

> **Unproved physical collision lemma.** In the six-block endpoint-offset
> schedule of a zero-margin survivor,
> \[
> r_4+\sum_{Q:\lambda_Q>0}(p_Q-1)\le131-c+m_4.
> \tag{12.3}
> \]

Equations (12.2) and (12.3) differ by exactly one and therefore contradict.
The exact upper-layer replacement is
\[
\sum_Y(\kappa_Y-1)_+\le131-c+m_7.
\tag{12.4}
\]
Neither estimate is proved. The missing-count-free bounds with right sides
\(131-c\) are stronger uniform sufficient lemmas, but are not the weakest
exact thresholds.

A structural replacement would synchronize the separate physical
rank-four/rank-seven endpoint-shadow forests with the particular dual pair
\(F,F_6\). Mere existence of many selected shadow colors does not imply
that they are the synchronized \(Q_i,Y_i\).

The new coordinate split supplies a second exact finishing point. In the
\(n_5=133\) slice, it would suffice to prove that some coordinate violates
\[
\lambda_x+r_x+E_{1,x}+E_{2,x}
\ge22+2h_x+2i_x,
\tag{12.5}
\]
because (9.5) would give \(e_x^{\rm ext}<0\). Present run localization does
not force such a coordinate.

## 13. Abstract realizability no-go

The preceding obstruction is genuinely physical. The abstract forest,
matching, endpoint orientations, and coordinate-\(42\) laws are consistent.

### External theorem used

The established Middle Levels Theorem states that the inclusion graph on
\(\mathcal V_5\cup\mathcal V_6\) has a Hamilton cycle. It is imported here
and not reproved.

### Proposition 13.1 (abstract models for every \(c\le6\))

For every \(1\le c\le6\), there is an abstract spanning rainbow linear
forest on \(\mathcal V_5\) with \(c\) components, a compatible perfect
inclusion matching, and all abstract \(42\)-label, root/leaf, lower-color,
upper-color, and parity identities of Sections 3--8. Any positive component
sizes summing to \(462\) may be prescribed.

#### Proof

Write a middle-level Hamilton cycle cyclically as
\[
S_0,U_0,S_1,U_1,\ldots,S_{461},U_{461},S_0,
\tag{13.1}
\]
where \(S_i\in\mathcal V_5\), \(U_i\in\mathcal V_6\), with indices modulo
\(462\). Define \(M(S_i)=U_i\). Then \(M\) is a perfect inclusion matching,
and the projected edges
\[
S_iS_{i+1}
\]
form a Hamilton cycle in \(J(11,5)\) with pairwise distinct union colors
\(U_i\).

Delete any \(c\) projected edges. The remainder is a spanning linear forest
with \(c\) components. Orient retained edges \(S_i\to S_{i+1}\). At a
deleted edge \(S_iS_{i+1}\), the preceding component has root \(S_i\), and
\(M(S_i)=U_i\) is its unused root color; \(S_{i+1}\) is the next leaf.
Cuts at arbitrary cyclic gaps prescribe any positive composition of \(462\)
into \(c\) sizes.

The \(42\)-label law follows from the complete middle layers, and every
abstract identity in Sections 3--8 was proved from these axioms. Placing an
already oriented component in forward endpoint order gives a left-oriented
abstract block; placing that same oriented path in reverse endpoint order
gives a right-oriented abstract block. Its ownership arrows are not
reversed with \(M\) fixed. \(\square\)

This proposition does not realize physical offset intervals, the central
\(A\)-word, the seam, or the noncentral ranks of an OR array. It proves the
precise no-go
\[
\boxed{
\text{No contradiction can use only the abstract forest, matching,
abstract left/right endpoint placement, parity, \(42\)-label law,
or layer congestion.}
}
\tag{13.2}
\]

## 14. Adversarial audit

The main claims were independently audited through endpoint parity,
coordinate flow, and rank-seven congestion. The following failure modes are
explicitly excluded.

1. **The root color is included in \(F_6\).** The final
   \(Y_{r-1}=U_{r-1}\cup U_r\) uses the formerly omitted root color.
   Omitting it gives wrong counts and margins.
2. **Occurrence degree is not distinct-color degree.** Equations
   (5.1)--(5.2) count with multiplicity; the missing-support vectors
   \(p_x^{(4)},p_x^{(7)}\) are necessary in (6.5), (6.7).
3. **There is no conclusion \(m_4,m_7\le6\).** The number \(c\le6\) counts
   missing rank-six forest colors, not missing synchronized extreme colors.
4. **Rank-seven colors are not asserted distinct.** Their forced collision
   excess is a conclusion.
5. **A separate endpoint-shadow forest is not automatically \(F_6\).**
   Its selected rank-seven colors cannot be transferred to the \(Y_i\)'s
   without an alignment theorem.
6. **Mode C0 has one lower-color exception.** Its extra low pair gives a
   rank-four superset that need not be an ordinary pair color.
7. **Singletons are both leaves and roots.** They have no \(Q_i,Y_i\), but
   contribute six isolated zero-runs in (3.5).
8. **Endpoint augmentation is sufficient, not necessary.** A minimal root
   state may close accidentally from its actual OR labels.
9. **The Hall tensor is aggregate only.** It does not realize distinct
   five-set supports, sequential paths, or physical intervals.
10. **The Middle Levels Theorem is an imported abstract witness.** It
    defeats an abstract contradiction but constructs no zero-margin OR word.
11. **The seam correction in (9.1) is exact.** A long zero-run is missed
    only when it contains all three seam positions, exactly for
    \(x\notin H\); boundary seams obey the same convention.
12. **No conjecture is proved.** The first unproved theorem needed by this
    route is (12.3), its dual, or an equivalent physical alignment theorem.

## 15. Theorem ledger

| Statement | Status |
|---|---|
| Exact gains, losses, and five-set run table | proved |
| Pairwise-distinct transition labels and no internal \(101\) | proved |
| Synchronized spanning six-set forest \(F_6\) | proved |
| Exact labelled \(4\subset7\) flag | proved |
| Complement duality | proved |
| Lower and upper point laws | proved |
| Multiplicity six and joint multiplicity two | proved |
| Local cut identities and collision ledgers | proved |
| Seven-petal functional successor digraph | proved |
| Integral feasibility of all coordinate tensor margins | proved |
| Exact central label split (9.1)--(9.8) | proved |
| Distinct internal-seam root labels in \(H\) | proved |
| Central lower/upper physical localization | proved, with the C0 exception |
| Peripheral root-state augmentation | proved as a sufficient closure theorem |
| Abstract consistency for every \(c\le6\) | proved from the imported Middle Levels Theorem |
| Physical collision estimate (12.3) or (12.4) | **unproved** |
| Contradiction to the zero-margin templates | **not obtained** |
| Contiguous-OR width conjecture | **not proved by this route** |
