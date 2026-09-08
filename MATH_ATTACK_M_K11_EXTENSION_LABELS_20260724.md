# Lane M: the \(K_{11}\) extension-label and rank-seven reduction

Date: 2026-07-24

## 1. Verdict

Assume the audited \(K_{11}\) zero-margin package arising from a hypothetical
length-\(465\) word:

1. the selected rank-five and rank-six witnesses admit the common endpoint
   order
   \[
   I_0,\ldots,I_{461},\qquad J_0,\ldots,J_{461};
   \]
2. their colors \(S_j=\operatorname{OR}(I_j)\) and
   \(U_j=\operatorname{OR}(J_j)\) satisfy
   \[
   S_j\subset U_j,
   \]
   and \(S_j\mapsto U_j\) is a perfect inclusion matching between all
   five-subsets and all six-subsets of \([11]\);
3. the rank-five offset schedule has \(c\leq 6\) nonempty blocks, and cutting
   the \(c-1\) state boundaries gives \(c\) alternating middle-level paths.

No contradiction to length \(465\) follows from the presently available
extension-label, endpoint, rank-seven congestion, or coordinate-parity
constraints alone.

The strongest proved finite conclusion is substantially sharper than the
earlier statement that the external extension labels are free:

* every external coordinate degree is exactly determined by the long
  coordinate-zero-runs of the central word;
* the same assertion has an exact joint-run version for every subset of at
  most five coordinates;
* at the abstract middle-level-cover layer, the remaining matching freedom
  is exactly a spanning directed linear forest in an explicitly defined
  \(5\)-in-neighbor digraph on the \(462\) six-sets;
* at least \(319\) of the \(330\) rank-seven colors occur as literal
  width-at-most-four hulls inside that forest;
* at most \(11\) rank-seven colors are missing, while the exact duplicate
  excess lies between \(126\) and \(137\);
* every coordinate belongs to at least \(15\) repeated rank-seven colors;
* all source/root correction and parity terms are confined to the at most
  six path starts and six path roots.

All statements below are integral statements inside the selected literal
interval witnesses. No averaging, fractional matching, relabeling of a
factor, or computational search is used.

## 2. Imported premises and notation

The following are imported, not reproved here.

### Premise P1: ordered middle-level matching

The selected witnesses are indexed so that both their left endpoints and
their right endpoints are in their audited common order. Their colors run
once through
\[
\binom{[11]}5\quad\hbox{and}\quad\binom{[11]}6,
\]
and
\[
M(S_j)=U_j,\qquad S_j\subset U_j
\tag{2.1}
\]
defines a perfect inclusion matching \(M\).

For \(U\in\binom{[11]}6\), write
\[
P(U)=M^{-1}(U),\qquad a(U)=U\setminus P(U).
\tag{2.2}
\]
Thus \(a(U)\) is one coordinate.

For every \(x\in[11]\), exactly \(42\) matching edges have label \(x\):
\[
\#\{U:a(U)=x\}
=\binom{10}{5}-\binom{10}{4}
=252-210
=42.
\tag{2.3}
\]

### Premise P2: at most six alternating paths

After deleting the \(c-1\) transitions between nonempty rank-five offset
blocks, where
\[
1\leq c\leq 6,
\tag{2.4}
\]
the \(924\) middle-level vertices form \(c\) alternating paths. Projecting
onto the six-set vertices gives a spanning linear forest
\[
G_6\subset J(11,6)
\tag{2.5}
\]
with \(c\) path components and exactly
\[
462-c
\tag{2.6}
\]
edges.

Inside a rank-five state block, consecutive selected six-witnesses overlap
through the intervening selected five-witness. Therefore, if \(j\) is not a
state cut, then
\[
K_j=J_j\cup J_{j+1}
\tag{2.7}
\]
is one literal interval, its physical span is at most four, and
\[
\operatorname{OR}(K_j)=U_j\cup U_{j+1}
\tag{2.8}
\]
has rank seven. The corresponding hull-offset schedule is
\[
02^*,\ 03^*,\ 04^*,\ 14^*,\ 24^*
\tag{2.9}
\]
after the state cuts are removed.

### Premise P3: rank-seven endpoint losses

Choose one selected literal witness for every one of the
\(\binom{11}{7}=330\) rank-seven targets. Let \(e_L\) be the number of these
targets whose selected left endpoint is not shared by the rank-six row, and
let \(e_R\) be the analogous right-endpoint count. The audited endpoint
theorem gives
\[
0\leq e_L,e_R\leq 3.
\tag{2.10}
\]

### Lemma 2.1: endpoint-source injectivity

Within either fixed-rank selected row, witnesses of two distinct targets
are incomparable as intervals. Interval containment would imply
containment of their OR masks, and two masks of the same cardinality can
be contained only if they are equal. It follows that the left endpoints
in each row are distinct, the right endpoints are distinct, and both
endpoint orders are the same strict order.

At a left endpoint common to a selected rank-seven witness \(K_Q\) and a
selected rank-six witness \(J_U\), the latter is a proper prefix of the
former. Otherwise \(J_U\) would contain \(K_Q\), forcing the rank-seven
mask \(Q\) into the rank-six mask \(U\). Thus
\[
J_U\subsetneq K_Q,\qquad U\subsetneq Q.
\tag{2.10a}
\]
At a common right endpoint, \(J_U\) is analogously a proper suffix of
\(K_Q\). Consequently the common-left and common-right source maps are
injective, and their source colors are genuine six-facets of their
rank-seven targets.

Premises P1--P3 are the only imported results used in the global rank-seven
argument. The central-window argument also imports the exact central normal
form recorded next.

### Premise P4: central normal form

Let
\[
A_0,A_1,\ldots,A_{m-1}
\tag{2.11}
\]
be the central low-entry segment, and put
\[
C_i=A_i\cup A_{i+1}\cup A_{i+2}
\quad(0\leq i\leq m-3),
\tag{2.12}
\]
\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}
\quad(0\leq i\leq m-4).
\tag{2.13}
\]
There is one exceptional triple
\[
H=C_s,\qquad |H|\in\{3,4\}.
\tag{2.14}
\]
Every other \(C_i\) is a distinct five-set, and all \(T_i\) are distinct
six-sets. With
\[
\mathcal C=\{C_i:i\neq s\},\qquad
\mathcal T=\{T_i:0\leq i\leq m-4\},
\tag{2.15}
\]
both families have size
\[
q=m-3.
\tag{2.16}
\]
The restriction of the ordered matching is
\[
C_i\longmapsto T_i\quad(i<s),
\qquad
C_i\longmapsto T_{i-1}\quad(i>s).
\tag{2.17}
\]

When the seam is internal, the two central alternating paths, in their exact
orders, are
\[
C_0,T_0,C_1,T_1,\ldots,C_{s-1},T_{s-1}
\tag{2.18}
\]
and
\[
C_{m-3},T_{m-4},C_{m-4},T_{m-5},
\ldots,C_{s+1},T_s.
\tag{2.19}
\]

## 3. The external extension vector is forced

For \(x\in[11]\), call an interval of consecutive indices an
\(x\)-zero-run if every \(A_i\) on it omits \(x\), and the interval is
maximal with this property. Let
\[
R_x^{(r)}
\tag{3.1}
\]
be the number of \(x\)-zero-runs of length at least \(r\). Put
\[
h_x=\mathbf 1_{\{x\in H\}}.
\tag{3.2}
\]
Let \(t_x\) be the number of matching edges in (2.17) whose unique added
coordinate is \(x\).

### Theorem 3.1: exact central label formula

For every coordinate \(x\),
\[
\boxed{t_x=R_x^{(3)}-1+h_x.}
\tag{3.3}
\]
Consequently the number \(e_x^{\mathrm{ext}}\) of matching edges outside
\(\mathcal C\to\mathcal T\) whose label is \(x\) is
\[
\boxed{
e_x^{\mathrm{ext}}
=42-t_x
=43-R_x^{(3)}-h_x.
}
\tag{3.4}
\]
In particular,
\[
\boxed{1\leq R_x^{(3)}+h_x\leq 43.}
\tag{3.5}
\]

#### Proof

Let \(N_{\ell,x}\) be the number of length-\(\ell\) windows of the
\(A\)-sequence whose union contains \(x\). A zero-run of length \(r\)
contributes
\[
\max(r-\ell+1,0)
\]
windows omitted from \(N_{\ell,x}\). Hence, on passing from length three to
length four, every zero-run of length at least three contributes exactly
one, while the total number of windows drops by one. Thus
\[
N_{4,x}-N_{3,x}=R_x^{(3)}-1.
\tag{3.6}
\]

The target point-incidence minus the ordinary source point-incidence is
\[
\begin{aligned}
\#\{T\in\mathcal T:x\in T\}
&-\#\{C\in\mathcal C:x\in C\}\\
&=N_{4,x}-\bigl(N_{3,x}-h_x\bigr)\\
&=R_x^{(3)}-1+h_x.
\end{aligned}
\tag{3.7}
\]
Every edge of the inclusion matching either contributes zero to this
difference or contributes one precisely when it adds \(x\). Therefore the
left side of (3.7) is \(t_x\), proving (3.3).

Equation (2.3) then gives (3.4). Both \(t_x\) and
\(e_x^{\mathrm{ext}}\) are nonnegative integers, which gives (3.5).
\(\square\)

The sum checks are exact:
\[
\sum_x t_x=m-3,
\qquad
\sum_x e_x^{\mathrm{ext}}=465-m,
\tag{3.8}
\]
and hence
\[
\sum_x\bigl(R_x^{(3)}+h_x\bigr)=m+8.
\tag{3.9}
\]

There is also a literal run-to-label interpretation. If \(x\notin H\),
exactly one long \(x\)-zero-run contains the seam positions
\(s,s+1,s+2\); that run supplies no central matching label, and every other
long run supplies exactly one. If \(x\in H\), no \(x\)-zero-run contains
all three seam positions and every long run supplies exactly one central
label. This is the bijective version of (3.3).

From this point through Corollary 3.4, assume that the seam is an internal
transition seam:
\[
1\leq s\leq m-4.
\tag{3.9a}
\]

### Theorem 3.2: internal-seam restitution

Define the singleton endpoint labels
\[
\alpha=T_0\setminus C_0,\qquad
\beta=T_{m-4}\setminus C_{m-3},
\tag{3.10}
\]
and write
\[
\alpha_x=\mathbf 1_{\{x=\alpha\}},\qquad
\beta_x=\mathbf 1_{\{x=\beta\}},\qquad
\gamma_x=\mathbf 1_{\{x\in T_{s-1}\cap T_s\}}.
\tag{3.11}
\]
Then
\[
\boxed{
R_x^{(3)}+h_x
=R_x^{(4)}+\alpha_x+\beta_x+\gamma_x.
}
\tag{3.12}
\]
Equivalently,
\[
\boxed{
t_x=R_x^{(4)}-1+\alpha_x+\beta_x+\gamma_x,
}
\tag{3.13}
\]
\[
\boxed{
e_x^{\mathrm{ext}}
=43-R_x^{(4)}-\alpha_x-\beta_x-\gamma_x.
}
\tag{3.14}
\]

#### Proof

The difference \(R_x^{(3)}-R_x^{(4)}\) counts the maximal
\(x\)-zero-runs of exact length three.

An exact length-three run at the left endpoint is equivalent to \(x=\alpha\);
the right-endpoint case is equivalent to \(x=\beta\). Suppose an exact
length-three run starts at an internal index \(i\neq s\). Then \(x\notin
C_i\), while the maximality of the run puts \(x\) in both
\(T_{i-1}\) and \(T_i\). Since \(C_i\) is a five-set and both four-windows
are six-sets, this forces
\[
T_{i-1}=C_i\cup\{x\}=T_i,
\]
contrary to the distinctness of the \(T\)'s. Thus an internal exact
length-three run can occur only at \(i=s\).

If \(x\notin H\), the seam run has exact length three precisely when \(x\)
is present on both sides of the seam, which is precisely
\(x\in T_{s-1}\cap T_s\). If \(x\in H\), there is no seam zero-run, but
\(x\) belongs to both \(T_{s-1}\) and \(T_s\); the term \(h_x\) supplies
exactly this correction. Therefore
\[
R_x^{(3)}-R_x^{(4)}+h_x
=\alpha_x+\beta_x+\gamma_x,
\]
which is (3.12). Equations (3.13) and (3.14) follow from Theorem 3.1.
\(\square\)

### Corollary 3.3: exact central deletion ledger

Let \(g_x^{\mathrm{cen}}\) count the central nonmatching edges whose deleted
coordinate is \(x\). Then
\[
\boxed{
g_x^{\mathrm{cen}}
=t_x
-\mathbf 1_{\{x\in T_{s-1}\}}
-\mathbf 1_{\{x\in T_s\}}
+\mathbf 1_{\{x\in C_0\}}
+\mathbf 1_{\{x\in C_{m-3}\}}
\geq0.
}
\tag{3.15}
\]
Moreover,
\[
\sum_xg_x^{\mathrm{cen}}=m-5.
\tag{3.16}
\]

#### Proof

Orient both paths (2.18)--(2.19) from their displayed initial five-set to
their terminal six-set. Along a path, matching additions minus nonmatching
deletions equal terminal six-set incidence minus initial five-set incidence.
Summing the two paths coordinatewise gives (3.15). Summing over coordinates
gives
\[
(m-3)-12+10=m-5.
\]
\(\square\)

### Corollary 3.4: the two central root labels

Define
\[
\lambda^-=T_{s-1}\setminus C_{s-1},
\qquad
\lambda^+=T_s\setminus C_{s+1}.
\tag{3.17}
\]
Then
\[
\lambda^-\neq\lambda^+,
\qquad
\lambda^-,\lambda^+\in H\cap T_{s-1}\cap T_s.
\tag{3.18}
\]
In the seam notation of the audited central classification:

* in mode D with seam entries \(\{a\},\{b\},\{c\}\),
  \[
  (\lambda^+,\lambda^-)=(a,c);
  \]
* at a \((3,3)\) seam, \(\lambda^+\) and \(\lambda^-\) are respectively
  the two private seam coordinates on the left and right;
* at an oriented \((2,3)\) seam written
  \(\{x\},\{y\},\{c,d\}\),
  \[
  \lambda^+=x,\qquad
  \lambda^-=\text{the unique element of }\{c,d\}\setminus L,
  \]
  with \(L\) as in that classification.

Thus two distinct coordinates occur as matching labels at central path
roots. In particular, for the global rootward five-set gain count \(F_x\)
defined in Section 7,
\[
F_x\leq41
\tag{3.19}
\]
for at least two distinct coordinates.

The local membership assertions in (3.18) follow directly from
\[
\lambda^-\in
A_{s+2}\setminus(A_{s-1}\cup A_s\cup A_{s+1})
\]
and
\[
\lambda^+\in
A_s\setminus(A_{s+1}\cup A_{s+2}\cup A_{s+3}).
\]
The displayed seam cases show that the two labels are distinct.

## 4. Joint-coordinate extension constraints

The one-coordinate identities have an exact inclusion-exclusion
strengthening.

For a nonempty \(Y\subseteq[11]\), let \(R_Y^{(3)}\) be the number of
maximal runs of at least three consecutive \(A_i\)'s all disjoint from
\(Y\). For \(X\subseteq[11]\), \(1\leq |X|=r\leq5\), put
\[
\Delta_X
=\#\{T\in\mathcal T:X\subseteq T\}
-\#\{C\in\mathcal C:X\subseteq C\}.
\tag{4.1}
\]

### Theorem 4.1: joint zero-run hierarchy

For every \(X\subseteq[11]\) with \(1\leq |X|\leq5\),
\[
\boxed{
\Delta_X
=-1+\mathbf 1_{\{X\subseteq H\}}
+\sum_{\varnothing\neq Y\subseteq X}
(-1)^{|Y|+1}R_Y^{(3)}.
}
\tag{4.2}
\]
In addition,
\[
\boxed{
0\leq\Delta_X\leq
\binom{11-r}{6-r}-\binom{11-r}{5-r}.
}
\tag{4.3}
\]
For \(r=1,2,3,4,5\), the upper bounds are respectively
\[
\boxed{42,\ 42,\ 28,\ 14,\ 5.}
\tag{4.4}
\]

#### Proof

For a length-\(\ell\) window \(W\),
\[
\mathbf 1_{\{X\subseteq\operatorname{OR}(W)\}}
=\sum_{Y\subseteq X}(-1)^{|Y|}
\mathbf 1_{\{\operatorname{OR}(W)\cap Y=\varnothing\}}.
\tag{4.5}
\]
Subtracting the length-three count from the length-four count, the empty
term contributes \(-1\). For a nonempty \(Y\), every \(Y\)-zero-run of
length at least three contributes \(-1\) to the change in the number of
all-\(Y\)-zero windows. Thus the nonempty term contributes
\((-1)^{|Y|+1}R_Y^{(3)}\). Removing \(H\) from the source family adds
\(\mathbf 1_{\{X\subseteq H\}}\), proving (4.2).

Because every central matching edge is an inclusion edge, \(\Delta_X\)
counts exactly the central edges on which containment of \(X\) is newly
created. It is therefore nonnegative. Across the complete perfect matching,
the number of such edges is
\[
\#\{U\in\tbinom{[11]}6:X\subseteq U\}
-\#\{P\in\tbinom{[11]}5:X\subseteq P\},
\]
which is the right side of (4.3). The central edges form a subset of the
complete matching edges, giving the upper bound. Direct evaluation gives
(4.4).
\(\square\)

For example, for two coordinates \(x,y\),
\[
0\leq
R_x^{(3)}+R_y^{(3)}-R_{\{x,y\}}^{(3)}
-1+\mathbf 1_{\{\{x,y\}\subseteq H\}}
\leq42.
\tag{4.6}
\]
Thus the extension choices cannot be treated as independent coordinate
wildcards.

## 5. Residual facet congestion

The central matching also forces many additional central source--target
incidences, whether or not those incidences are selected by the matching.

Put
\[
K=\#\{(C,T)\in\mathcal C\times\mathcal T:C\subset T\},
\qquad
e=462-q=465-m.
\tag{5.1}
\]

### Theorem 5.1: residual-facet lower bound

\[
\boxed{K\geq 6q-5e=11q-2310.}
\tag{5.2}
\]

For an internal seam, the locally forced incidences number \(2q-2\).
Consequently the number \(K_{\mathrm{nonlocal}}\) of all other central
incidences satisfies
\[
\boxed{K_{\mathrm{nonlocal}}\geq9q-2308.}
\tag{5.3}
\]
For an endpoint seam, the corresponding bound is
\[
\boxed{K_{\mathrm{nonlocal}}\geq9q-2309.}
\tag{5.4}
\]

#### Proof

The full rank-five/rank-six inclusion graph is \(6\)-regular on both sides
and has
\[
6\binom{11}{5}=2772
\]
edges. After removing the \(q\) central sources and \(q\) central targets,
the number of edges between the two external families is
\[
2772-6q-6q+K=2772-12q+K.
\tag{5.5}
\]
The external part of the perfect matching has \(e\) edges, so (5.5) is at
least \(e\). This gives
\[
K\geq e-2772+12q=11q-2310=6q-5e.
\]

Every \(T_i\) contains its two adjacent triples \(C_i,C_{i+1}\), except
that incidences involving the omitted exceptional triple \(H=C_s\) do not
belong to \(\mathcal C\). An internal seam removes two of the \(2q\) local
incidences; an endpoint seam removes one. Subtracting these local counts
from (5.2) proves (5.3) and (5.4).
\(\square\)

### Corollary 5.2: six-sets with at least four central facets

Let \(N_{\geq4}\) count the \(T\in\mathcal T\) which contain at least four
members of \(\mathcal C\). Then
\[
\boxed{
N_{\geq4}\geq
\max\left(0,
\left\lceil\frac{8q-2310}{3}\right\rceil
\right).
}
\tag{5.6}
\]

Indeed, a six-set has at most six five-facets. If fewer than
\(N_{\geq4}\) targets have at least four central facets, then
\[
K\leq6N_{\geq4}+3(q-N_{\geq4})
=3q+3N_{\geq4}.
\]
Combine this with (5.2).

For orientation, \(q=330\) forces \(N_{\geq4}\geq110\), while \(q=329\)
forces \(N_{\geq4}\geq108\).

## 6. Exact description of the remaining matching freedom

The extension labels do not independently choose the next six-set.
They define a directed graph in which the whole alternating cover must
live.

### Definition 6.1: the matching digraph

Let \(D_M\) be the directed graph on \(\binom{[11]}6\) with the five arcs
entering \(U\)
\[
\boxed{
U-\{a(U)\}+\{z\}\longrightarrow U
\qquad(z\notin U).
}
\tag{6.1}
\]

### Theorem 6.2: exact directed-forest equivalence

The projected six-set paths of the alternating middle-level cover are
exactly a spanning directed linear forest in \(D_M\) with:

* \(c\) starts and \(c\) terminals;
* indegree and outdegree at most one;
* no directed cycle;
* \(462-c\) arcs.

Conversely, every spanning directed linear forest in \(D_M\) with these
properties lifts, using the fixed matching \(M\), to an alternating cover
of all \(462+462\) middle-level vertices.

#### Proof

Orient one alternating component as
\[
P_0,U_0,P_1,U_1,\ldots,P_r,U_r,
\tag{6.2}
\]
where \(P_i=M^{-1}(U_i)\). For \(i\geq1\), the previous six-set \(U_{i-1}\)
and the destination \(U_i\) share \(P_i\). Hence
\[
U_{i-1}=P_i\cup\{z\}
=U_i-\{a(U_i)\}+\{z\}
\]
for a unique \(z\notin U_i\), which is an arc of \(D_M\).
Path disjointness gives the degree conditions and absence of cycles.

Conversely, for an arc \(U'\to U\), (6.1) says exactly that
\[
P(U)\subset U'\cap U.
\]
Insert \(P(U)\) between \(U'\) and \(U\). At a directed start \(U\), insert
\(P(U)\) before it. Since \(M\) is bijective, every five-set occurs once;
since the directed forest spans the six-sets, every six-set occurs once.
This gives the alternating cover.
\(\square\)

There are exactly
\[
5\cdot462=2310
\tag{6.3}
\]
candidate arcs. In the displayed orientation, \(z\) is the coordinate
deleted on entering \(U\). Every coordinate occurs in this leaving role
on
\[
\binom{10}{6}=210
\tag{6.4}
\]
candidate arcs. The matching label \(a(U)\) is the coordinate gained on
entering \(U\); by (2.3), every coordinate occurs in that role on
\(42\cdot5=210\) candidate arcs. Therefore plain degree counting of the
candidate digraph is perfectly balanced and cannot by itself yield a
contradiction.

The converse in Theorem 6.2 is deliberately an abstract cover statement.
An arbitrary directed forest in \(D_M\) need not respect the prescribed
global endpoint order, the offset-block directions, the central template,
or literal interval realization. A length-\(465\) survivor must choose a
forest which also obeys all those additional constraints.

### Rank-seven form of the same restriction

Fix a seven-set \(Q\). Identify its six-facet \(Q\setminus\{z\}\) with the
missing coordinate \(z\in Q\). If
\[
U=Q\setminus\{z\},
\qquad
a_Q(z)=a(U),
\tag{6.5}
\]
then the only possible \(Q\)-colored predecessor of \(U\) is
\[
Q\setminus\{a_Q(z)\}.
\tag{6.6}
\]
Thus the possible \(Q\)-colored arcs are the prescribed arrows
\[
\boxed{a_Q(z)\longrightarrow z\qquad(z\in Q)}
\tag{6.7}
\]
on the seven missing-coordinate vertices, subject to the global
indegree-one, outdegree-one, and acyclicity constraints. This is the exact
rank-seven witness constraint generated by the extension labels.

## 7. Source, root, deletion, and parity ledgers

Orient every alternating component as in (6.2). Define its matching
addition and nonmatching deletion labels by
\[
\alpha_i=U_i\setminus P_i,
\qquad
\beta_i=U_i\setminus P_{i+1}\quad(0\leq i<r).
\tag{7.1}
\]
Then
\[
U_i\cup U_{i+1}
=P_{i+1}\cup\{\beta_i,\alpha_{i+1}\}.
\tag{7.2}
\]
In particular the two labels on a rank-seven hull edge are exact and
distinct.

For \(x\in[11]\), define:

\[
\pi_x=\#\{\hbox{components with initial matching label }\alpha_0=x\},
\tag{7.3}
\]
\[
\delta_x=\#\{\hbox{components with final matching label }\alpha_r=x\},
\tag{7.4}
\]
\[
\tau_x=\#\{\hbox{initial five-sets }P_0\hbox{ containing }x\},
\tag{7.5}
\]
\[
\sigma_x=\#\{\hbox{final five-sets }P_r\hbox{ containing }x\},
\tag{7.6}
\]
\[
\mu_x=\#\{\hbox{final six-sets }U_r\hbox{ containing }x\}
=\sigma_x+\delta_x.
\tag{7.7}
\]
Also put
\[
\nu_x=\tau_x+\pi_x,
\tag{7.8}
\]
the number of initial six-sets containing \(x\).

The endpoint sums and coordinatewise exclusion are
\[
\sum_x\pi_x=\sum_x\delta_x=c,
\quad
\sum_x\tau_x=\sum_x\sigma_x=5c,
\quad
\sum_x\mu_x=6c,
\tag{7.9}
\]
\[
\pi_x+\tau_x\leq c,
\qquad
\delta_x+\sigma_x=\mu_x\leq c.
\tag{7.10}
\]

Let:

* \(F_x\) count gains of \(x\) along the induced five-set paths
  \(P_i\to P_{i+1}\);
* \(H_x^{(6)}\) count gains of \(x\) along the six-set paths
  \(U_i\to U_{i+1}\);
* \(G_x\) count the nonmatching deletion labels \(\beta_i=x\).

The superscript on \(H_x^{(6)}\) distinguishes this path-gain count from
the seam indicator \(h_x=\mathbf1_{\{x\in H\}}\) used in Sections 3 and
12.

### Theorem 7.1: exact endpoint flow

\[
\boxed{
F_x=42-\delta_x,\qquad
H_x^{(6)}=42-\pi_x,\qquad
G_x=42-\mu_x+\tau_x.
}
\tag{7.11}
\]
Consequently,
\[
\boxed{
F_x-G_x=\sigma_x-\tau_x,
}
\tag{7.12}
\]
\[
\boxed{
H_x^{(6)}-G_x=\mu_x-\nu_x,
}
\tag{7.13}
\]
\[
\boxed{
H_x^{(6)}-F_x=\delta_x-\pi_x.
}
\tag{7.14}
\]

#### Proof

Every matching label occurs \(42\) times. A matching label contributes a
five-path gain unless it is the final label of its component, proving the
first formula. It contributes a six-path gain unless it is the initial
label, proving the second.

Across a full alternating component, matching additions minus nonmatching
deletions equal final-six-set incidence minus initial-five-set incidence.
Summing components gives
\[
42-G_x=\mu_x-\tau_x,
\]
which proves the third formula. Equations (7.12)--(7.14) are algebraic
consequences.
\(\square\)

### Corollary 7.2: parity is supported at starts and roots

\[
\boxed{
F_x\equiv\delta_x,\qquad
H_x^{(6)}\equiv\pi_x,\qquad
G_x\equiv\mu_x+\tau_x\pmod2.
}
\tag{7.15}
\]
The odd supports of \(F\) and \(H^{(6)}\) each have size at most \(c\), and
each of their cardinalities is congruent to \(c\pmod2\).

Indeed, \(42\) is even, while a nonnegative integer vector of total mass
\(c\) has at most \(c\) odd entries and has an odd-support cardinality
congruent to \(c\).

This is the exact source/root parity theorem. It does not force every
coordinate degree to be even: the \(c\) start labels and \(c\) root labels
are the unavoidable correction terms.

## 8. The almost-complete rank-seven hull theorem

For a seven-set \(Q\), let
\[
t_Q=\#\{E\in E(G_6):\hbox{the union of the two endpoints of }E\hbox{ is }Q\}.
\tag{8.1}
\]
Let
\[
z=\#\{Q:t_Q>0\},
\qquad
M_7=330-z.
\tag{8.2}
\]

### Lemma 8.1: fixed-color congestion

For every seven-set \(Q\),
\[
\boxed{0\leq t_Q\leq6.}
\tag{8.3}
\]
Equality can occur only when all seven six-facets of \(Q\) occur in one
path component in a consecutive path order.

#### Proof

The only six-set endpoints of a \(Q\)-colored edge are the seven facets
\(Q\setminus\{x\}\), \(x\in Q\). The \(Q\)-colored edges form a subgraph of
the linear forest \(G_6\) on these seven vertices. A forest on seven
vertices has at most six edges. Equality forces a tree; the ambient degree
bound two makes that tree a path.
\(\square\)

### Lemma 8.2: exact crossed spans

At least
\[
p\geq330-e_L-e_R\geq324
\tag{8.4}
\]
selected rank-seven witnesses share both endpoints with selected rank-six
witnesses.

For each such target \(Q\), let \(J_{a_Q}\) share its left endpoint and
\(J_{b_Q}\) share its right endpoint. Then
\[
\boxed{
a_Q<b_Q,\qquad
J_j\subseteq K_Q\quad(a_Q\leq j\leq b_Q),
\qquad
1\leq b_Q-a_Q\leq6.
}
\tag{8.5}
\]
Every \(U_j\), \(a_Q\leq j\leq b_Q\), is a distinct facet of \(Q\), and
every gap in the span has union color \(Q\).

For distinct crossed targets, the gap sets
\[
\{a_Q,a_Q+1,\ldots,b_Q-1\}
\tag{8.6}
\]
are disjoint. Therefore
\[
\boxed{
\sum_{\text{crossed }Q}(b_Q-a_Q)\leq461.
}
\tag{8.7}
\]
At least
\[
\boxed{2p-461\geq187}
\tag{8.8}
\]
crossed spans have length one.

#### Proof

The endpoint order implies that any \(J_j\) between the common-left and
common-right witnesses lies physically inside \(K_Q\). Its OR is therefore
a six-subset of \(Q\). The \(U_j\)'s are distinct, and \(Q\) has only seven
six-facets, proving the length bound.

If spans for two distinct targets shared a gap \(j\), then both targets
would contain the two distinct six-sets \(U_j,U_{j+1}\). Their union is a
seven-set and therefore determines the target uniquely, a contradiction.
There are \(461\) gaps in the global order, which proves (8.7).

If \(s_1\) spans have length one, then
\[
461\geq s_1+2(p-s_1)=2p-s_1,
\]
which is (8.8).
\(\square\)

### Theorem 8.3: rank-seven support and exact duplicate excess

\[
\boxed{
z\geq331-c-e_L-e_R\geq319,
}
\tag{8.9}
\]
\[
\boxed{
M_7\leq c-1+e_L+e_R\leq11.
}
\tag{8.10}
\]
Thus at least \(319\) of the \(330\) rank-seven targets have simultaneous
literal width-at-most-four witnesses of the form \(J_j\cup J_{j+1}\)
inside the exact alternating forest.

Moreover,
\[
\boxed{
\Delta_7:=\sum_Q(t_Q-1)_+
=462-c-z
=132-c+M_7.
}
\tag{8.11}
\]
In particular,
\[
\boxed{126\leq\Delta_7\leq137.}
\tag{8.12}
\]
At least
\[
\boxed{
\left\lceil\frac{\Delta_7}{5}\right\rceil\geq26
}
\tag{8.13}
\]
rank-seven colors repeat.

#### Proof

Before the \(c-1\) state cuts, every crossed target contributes all gaps of
its nonempty span. Distinct targets have disjoint gap sets. A crossed color
can disappear from \(G_6\) only if every gap in its span is a state cut, so
each disappearing crossed color consumes at least one distinct cut.
Therefore
\[
z\geq p-(c-1)
\geq331-c-e_L-e_R,
\]
which proves (8.9) and (8.10).

The forest has \(462-c\) edges. Subtracting one primary occurrence of each
of its \(z\) colors gives (8.11). Its lower bound follows from \(M_7\geq0\)
and \(c\leq6\); its upper bound follows from
\[
M_7\leq c-1+e_L+e_R\leq c+5.
\]
Finally, Lemma 8.1 says one repeated color contributes at most five to
\(\Delta_7\), proving (8.13).
\(\square\)

### Corollary 8.4: touching crossed spans and rank eight

When the crossed spans are put in order, at least
\[
\boxed{2p-462\geq186}
\tag{8.14}
\]
successive pairs touch at a common six-set vertex.

Indeed, the \(p\) spans occupy at least \(p\) of the \(461\) gaps. Of the
\(p-1\) separations between successive spans, at most \(461-p\) can contain
an unused gap. The remainder touch.

Let \(\mathcal A_L,\mathcal A_R\) be the rank-six source families obtained
from the common left and common right endpoints. Lemma 2.1 makes both
source maps injective, so
\[
|\mathcal A_L\cap\mathcal A_R|
\geq(330-e_L)+(330-e_R)-462
=198-e_L-e_R
\geq192.
\tag{8.15}
\]
Every common source lies below two distinct selected rank-seven targets,
one ending and one beginning at its literal rank-six witness.

More explicitly, form a directed pivot graph \(\mathcal P_7\) on the
\(330\) selected rank-seven targets. If \(U=J_j\) belongs to
\(\mathcal A_L\cap\mathcal A_R\), let \(Q^-\) be the unique target whose
witness shares the right endpoint of \(J_j\), and let \(Q^+\) be the unique
target whose witness shares its left endpoint; insert
\[
Q^-\longrightarrow Q^+.
\tag{8.15a}
\]
The two targets are distinct. Their witnesses have the forms
\([\,\ell,v_j\,]\) and \([\,u_j,r\,]\), overlap exactly in \(J_j\), and
their target intersection is exactly \(U\). Their union is therefore one
literal rank-eight interval.

By Lemma 2.1, every rank-seven target has indegree and outdegree at most one
in \(\mathcal P_7\). Every arc goes forward in the strict common endpoint
order, because \(\ell<u_j\) and \(v_j<r\), so \(\mathcal P_7\) is acyclic.
It is a directed linear forest. For a fixed rank-eight set \(R\), the
\(R\)-colored pivots induce a subforest on the eight rank-seven facets of
\(R\), and hence number at most seven.

Consequently these pivots supply at least
\[
\boxed{
\left\lceil\frac{198-e_L-e_R}{7}\right\rceil\geq28
}
\tag{8.16}
\]
distinct literal rank-eight colors. This is a genuine consequence but is
far below the \(165\) rank-eight targets, so it gives no contradiction.

## 9. Coordinatewise rank-seven congestion

For \(x\in[11]\), let \(Z_x^{(6)}\) be the number of maximal zero-runs of
the coordinate \(x\) along the \(c\) oriented six-set paths. Let
\[
q_x^{(7)}=\sum_{Q\ni x}t_Q
\tag{9.1}
\]
be the number of rank-seven hull occurrences containing \(x\), with
multiplicity. Let \(\chi_x\) be the number of six-path edges on which the
membership of \(x\) changes.

### Theorem 9.1: exact point-degree and change-degree formulas

\[
\boxed{
Z_x^{(6)}=42+c-\pi_x-\mu_x,
}
\tag{9.2}
\]
\[
\boxed{
q_x^{(7)}=294-\pi_x-\mu_x,
}
\tag{9.3}
\]
and hence
\[
\boxed{
294-2c\leq q_x^{(7)}\leq294.
}
\tag{9.4}
\]
Also,
\[
\boxed{
\chi_x=H_x^{(6)}+G_x
=84-\pi_x-\mu_x+\tau_x
=q_x^{(7)}-210+\tau_x,
}
\tag{9.5}
\]
\[
\boxed{
\sum_x\chi_x=924-2c,
\qquad
\chi_x\equiv\pi_x+\mu_x+\tau_x\pmod2.
}
\tag{9.6}
\]

#### Proof

A coordinate-zero-run begins either at a \(1\to0\) deletion or at an
initial six-set omitting \(x\). Equivalently it ends immediately before a
\(0\to1\) gain or at a final six-set omitting \(x\). Using the latter
description and Theorem 7.1 gives
\[
Z_x^{(6)}=H_x^{(6)}+(c-\mu_x)=42+c-\pi_x-\mu_x.
\]

Among all \(462\) six-set vertices, exactly
\[
\binom{10}{6}=210
\]
omit \(x\). In a zero-run with \(r\) vertices, exactly \(r-1\) forest
edges have both endpoints omitting \(x\). Hence the total number of forest
edges whose hull omits \(x\) is \(210-Z_x^{(6)}\). Subtracting from the
\(462-c\) forest edges gives
\[
q_x^{(7)}
=(462-c)-(210-Z_x^{(6)})
=294-\pi_x-\mu_x.
\]
Since \(0\leq\pi_x,\mu_x\leq c\), this proves (9.4).

Membership changes are exactly the \(0\to1\) gains and \(1\to0\)
deletions, so \(\chi_x=H_x^{(6)}+G_x\). Equation (9.5) follows from
(7.11).
Every Johnson edge changes two coordinates, giving
\[
\sum_x\chi_x=2(462-c).
\]
The parity assertion follows from (9.5).
\(\square\)

### Theorem 9.2: signed and positive duplicate congestion

Let
\[
M_x=\#\{Q\ni x:t_Q=0\}.
\tag{9.7}
\]
Then
\[
\boxed{
\sum_{Q\ni x}(t_Q-1)=84-\pi_x-\mu_x,
}
\tag{9.8}
\]
\[
\boxed{
\sum_{Q\ni x}(t_Q-1)_+
=84-\pi_x-\mu_x+M_x,
}
\tag{9.9}
\]
and
\[
\boxed{
\sum_{Q\ni x}(t_Q-1)_+-\chi_x=M_x-\tau_x.
}
\tag{9.10}
\]

Every coordinate lies in at least
\[
\boxed{15}
\tag{9.11}
\]
distinct repeated rank-seven colors.

#### Proof

There are
\[
\binom{10}{6}=210
\]
seven-sets containing \(x\). Therefore (9.8) is (9.3) minus \(210\).
Every missing color contributes \(-1\) to the signed sum and zero to the
positive sum, which proves (9.9). Subtract (9.5) to obtain (9.10).

By (9.9), (7.10), and \(c\leq6\), the positive duplicate incidence at
\(x\) is at least
\[
84-\pi_x-\mu_x\geq84-2c\geq72.
\]
A fixed repeated color contributes at most \(t_Q-1\leq5\), by Lemma 8.1.
Thus at least \(\lceil72/5\rceil=15\) distinct repeated colors contain
\(x\).
\(\square\)

The identities pass two independent global sum checks:
\[
\sum_xq_x^{(7)}
=11\cdot294-\sum_x\pi_x-\sum_x\mu_x
=3234-7c
=7(462-c),
\tag{9.12}
\]
and
\[
\sum_x\chi_x
=11\cdot84-c-6c+5c
=924-2c.
\tag{9.13}
\]
These are respectively the point count of the rank-seven hull multiset and
twice the edge count of \(G_6\).

## 10. Endpoint six-set restrictions

The endpoint exceptions also have exact point-degree consequences.

Let \(\mathcal O_L\) be the complement in \(\binom{[11]}6\) of the
common-left source family \(\mathcal A_L\). Thus
\[
|\mathcal O_L|=462-(330-e_L)=132+e_L.
\tag{10.1}
\]
For \(x\in[11]\), let \(a_x^L\) count common-left rank-seven targets whose
unique source six-set \(U\) satisfies \(Q\setminus U=\{x\}\), and let
\(b_x^L\) count left-exception rank-seven targets containing \(x\).
The uniqueness and the identity \(|\mathcal A_L|=330-e_L\) are supplied
by Lemma 2.1.

### Theorem 10.1: endpoint-complement degree

\[
\boxed{
\deg_{\mathcal O_L}(x)=42+a_x^L+b_x^L.
}
\tag{10.2}
\]
The right-hand analogue is
\[
\boxed{
\deg_{\mathcal O_R}(x)=42+a_x^R+b_x^R.
}
\tag{10.3}
\]

#### Proof

Exactly \(210\) rank-seven targets contain \(x\). Of these,
\(210-b_x^L\) are in the common-left family. Passing from such a target to
its source loses \(x\) on exactly the \(a_x^L\) counted targets, so
\[
\deg_{\mathcal A_L}(x)=210-b_x^L-a_x^L.
\]
All \(252\) six-sets contain \(x\) in total. Taking the complement gives
\[
\deg_{\mathcal O_L}(x)
=252-(210-b_x^L-a_x^L)
=42+a_x^L+b_x^L.
\]
The right side is identical.
\(\square\)

For an internal central seam, the two central initial labels are
\[
\ell_L=T_0\setminus C_0,\qquad
\ell_R=T_{m-4}\setminus C_{m-3},
\tag{10.4}
\]
and the two central root six-sets are \(T_{s-1},T_s\). Splitting the global
start and root corrections into central and external contributions gives
the exact specialization
\[
\boxed{
q_x^{(7)}
=294-\mathbf 1_{\{x=\ell_L\}}
-\mathbf 1_{\{x=\ell_R\}}
-\mathbf 1_{\{x\in T_{s-1}\}}
-\mathbf 1_{\{x\in T_s\}}
-\pi_x^{\mathrm{ext}}
-\mu_x^{\mathrm{ext}}.
}
\tag{10.5}
\]
In particular,
\[
q_x^{(7)}\leq292
\tag{10.6}
\]
for every \(x\in T_{s-1}\cap T_s\), before any further external start/root
loss is counted.

## 11. Central rank-seven specialization

Consider the central five-windows
\[
A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}\cup A_{i+4}.
\tag{11.1}
\]
Let \(\chi_{\mathrm{seam}}=1\) precisely in the internal-seam case in which
the audited seam parameter \(\eta\) is positive, and put
\(\chi_{\mathrm{seam}}=0\) otherwise. The number of central rank-seven
occurrences is
\[
\boxed{N_7=m-4-\chi_{\mathrm{seam}}.}
\tag{11.2}
\]

A fixed seven-set occurs at most six times. To see this without silently
using the post-cut forest at the seam, form the auxiliary graph on the
distinct vertices
\[
T_0,T_1,\ldots,T_{m-4}
\]
using precisely those consecutive transitions \(T_iT_{i+1}\) whose union
has rank seven. At an endpoint seam this is one simple path. At an internal
seam with \(\eta=0\), it is also one simple path and includes the seam
transition \(T_{s-1}T_s\), even though that transition is not an edge of
the post-state-cut matching forest \(G_6\). At an internal seam with
\(\eta>0\), the non-rank-seven seam transition is omitted and the
auxiliary graph is two paths. In every case, the occurrences of a fixed
seven-set form a subforest on its seven six-facets and hence number at most
six. Moreover, the ordinary-transition extension-label pairs on repeated
occurrences are distinct; two equal facet pairs would repeat a six-set
target.

Let \(z_{\mathrm{cen}}\) be the number of distinct central rank-seven
colors. Exact endpoint charging gives
\[
\boxed{z_{\mathrm{cen}}\geq m-135.}
\tag{11.3}
\]
Indeed, let the central segment occupy the global positions
\([L,R]\), so \(m=R-L+1\). Any rank-seven interval wholly inside
\([L,R]\) has length at least five: an interval of length at most four is
contained in one of the rank-six four-windows \(T_i\). It therefore
contains a central five-window. Every such five-window has rank at least
seven; being contained in the rank-seven target of the whole interval, it
must have exactly that target color. Thus a target absent from the central
five-window support cannot have its selected witness wholly inside
\([L,R]\).

Charge every such absent target to a selected left endpoint before \(L\),
if it has one, and otherwise to its selected right endpoint after \(R\).
Lemma 2.1 says selected rank-seven witnesses have distinct left endpoints
and distinct right endpoints. There are only
\[
L+(464-R)=465-m
\]
available external endpoint slots. Hence at most \(465-m\) of the \(330\)
targets are absent, proving (11.3). Consequently,
\[
\boxed{
N_7-z_{\mathrm{cen}}\leq131-\chi_{\mathrm{seam}}.
}
\tag{11.4}
\]

The literal short-witness cap only localizes a boundary-crossing selected
witness. It does not force every centrally absent target to cross a central
boundary: its selected witness may lie wholly in a long external prefix or
suffix. Therefore the valid bound is (11.3), not the previously tempting
but invalid replacement of \(465-m\) by a constant such as \(18\).

## 12. Translation back to the audited zero-margin coordinate ledgers

Retain exactly the symbols
\[
\lambda_x,\ r_x,\ i_x,\ \ell_x,\ X_x
\]
from the mode tables in
K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md and its audit. Define here
\[
a_{1x}=\#\{\text{exact length-one }x\text{-zero-runs}\},
\qquad
a_{2x}=\#\{\text{exact length-two }x\text{-zero-runs}\}.
\tag{12.0}
\]
Substituting Theorem 3.1 into those already audited zero-run totals gives
the following additional necessary inequalities.

In the \(n_5=133\) slice,
\[
\boxed{
e_x^{\mathrm{ext}}
=\lambda_x+r_x+a_{1x}+a_{2x}
-22-2h_x-2i_x
\geq0.
}
\tag{12.1}
\]

For the \(n_5=132\) rank-four-carrier modes A, B, C0, and C1,
\[
\boxed{
e_x^{\mathrm{ext}}
=\lambda_x+r_x+a_{1x}+a_{2x}
-2\ell_x-X_x-22
\geq0.
}
\tag{12.2}
\]

For mode D,
\[
\boxed{
e_x^{\mathrm{ext}}
=\lambda_x+r_x+a_{1x}+a_{2x}
-2\ell_x-2h_x-22
\geq0.
}
\tag{12.3}
\]

These are exact coordinate cuts, not estimates. Their scope is the
corresponding previously classified mode only.

## 13. Why the current constraints do not contradict length \(465\)

The sharpest scalar rank-seven ledger is feasible.

Take the extreme permitted endpoint data
\[
c=6,\qquad e_L=e_R=3,\qquad p=324.
\tag{13.1}
\]
The span budget (8.7) can be met by
\[
187\text{ spans of length }1,\qquad
137\text{ spans of length }2,
\tag{13.2}
\]
because
\[
187+2\cdot137=461.
\]
The forest can have
\[
z=319,\qquad M_7=11,\qquad \Delta_7=137.
\tag{13.3}
\]
Its \(456=462-c\) edges can then have the scalar multiplicity profile
\[
137\text{ colors of multiplicity }2,\qquad
182\text{ colors of multiplicity }1,
\tag{13.4}
\]
with \(11\) missing colors. This respects \(t_Q\leq6\) and gives
\[
2\cdot137+182=456,\qquad137+182=319.
\]

This is only a scalar feasibility certificate; it is not asserted to lift
to a set-labelled matching digraph \(D_M\). It proves, however, that span,
support, and multiplicity counts by themselves cannot produce the desired
contradiction.

Likewise:

* the parity defects in (7.15) can be absorbed by the at most six start
  labels and six root labels;
* the point-degree defects in (9.3) can be absorbed by
  \(\pi_x+\mu_x\);
* the missing-color defects in (9.9) can be absorbed by \(M_x\);
* the central external-degree constraints (3.4), (12.1)--(12.3) presently
  force nonnegativity but have not been shown to force a negative
  coordinate.

Therefore no contradiction is proved.

## 14. Strongest new finite theorem

The results may be compressed into the following conditional theorem.

### Theorem M-K11

Under Premises P1--P4, every hypothetical length-\(465\) survivor induces:

1. an exact external label vector
   \[
   e_x^{\mathrm{ext}}=43-R_x^{(3)}-\mathbf1_{\{x\in H\}};
   \]
2. the joint-run inequalities (4.2)--(4.4) for every
   \(X\subseteq[11]\), \(1\leq|X|\leq5\);
3. the residual-facet bound
   \[
   K\geq11(m-3)-2310;
   \]
4. a spanning directed linear forest of \(D_M\), with \(c\leq6\) paths,
   which is equivalent to the remaining abstract alternating-cover choice
   and must additionally satisfy the literal endpoint and central
   constraints;
5. an exact literal rank-seven hull multiset satisfying
   \[
   319\leq z\leq330,\qquad
   M_7\leq11,\qquad
   126\leq\Delta_7\leq137,\qquad
   t_Q\leq6;
   \]
6. the source/root equations (7.11)--(7.15);
7. for every coordinate \(x\),
   \[
   q_x^{(7)}=294-\pi_x-\mu_x,
   \]
   and
   \[
   \sum_{Q\ni x}(t_Q-1)_+
   =84-\pi_x-\mu_x+M_x,
   \]
   so \(x\) belongs to at least \(15\) repeated rank-seven colors;
8. at least \(28\) distinct literal rank-eight colors arising from
   two-sided rank-six endpoint pivots.

Every item is an integral consequence of the fixed ordered witnesses and
the fixed perfect matching. At the abstract cover layer, the remaining
freedom is the set-compatible directed-forest selection in \(D_M\). A
survivor must in addition realize that forest in the fixed endpoint order,
offset blocks, central template, and literal intervals, together with the
bounded endpoint start/root data. Any further contradiction must use this
joint compatibility. Aggregate extension degrees, aggregate rank-seven
multiplicities, endpoint counts, and coordinate parity have now been
exhausted without contradiction.

## 15. Audit and scope

The decisive identities were checked independently in three ways.

1. **Central incidence audit.** Equation (3.3) is both a window-count
   identity and a matching-incidence identity. Its coordinate sums give
   exactly \(m-3\) central and \(465-m\) external matching edges.

2. **Rank-seven double-count audit.** Equation (9.3) sums to
   \(7(462-c)\), exactly seven point incidences per forest edge. Equation
   (9.5) sums to \(2(462-c)\), exactly two changed coordinates per Johnson
   edge.

3. **Endpoint/cut audit.** Distinct crossed rank-seven targets have
   disjoint gap sets. A color lost from the exact forest consumes a
   distinct state cut, which is why (8.9) loses \(c-1\), not \(c\).
   Endpoint omissions contribute exactly \(e_L+e_R\), with each at most
   three.

The endpoint-source injectivity needed for the rank-eight statement and
Section 10 is proved in Lemma 2.1, rather than being silently included in
Premise P3. The central mode formulas in Section 12 use the symbols and
classifications of the audited zero-margin report and make no claim outside
their stated modes.

No unproved new lemma is used in Theorem M-K11. The unresolved assertion is
not a hidden lemma but the next problem: prove that no perfect matching
\(M\) and no spanning directed linear forest of \(D_M\) can realize all of
the simultaneous central run, residual-facet, endpoint, and rank-seven
constraints above. That incompatibility is presently unproved.
