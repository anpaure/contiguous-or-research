# Pair-omission rows versus exact Pascal corridors: the transport obstruction

Date: 2026-07-25

This note couples the exact nested Pascal-chain resolution to the fixed
tight path forest of PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md,
Section 5.

The outcome is exact.  The row forest already solves middle ownership,
the outgoing rank-\((m-1)\) flag, residence, and reset cost.  It cannot,
however, carry the zero-loss abstract Pascal resolution: the first
pair-omission phase has more fixed owners than there are possible
same-row upper flags.  The first failure is at rank \(m+1\), and the
stronger radius-one failure is at rank \(m+2\).

The exhibited unavoidable baseline is \(\Theta(W/m)\), hence \(o(W/H)\)
for \(H=O(\sqrt m)\).  The baseline is therefore not a counterexample to
constant one; the actual minimum loss may be larger.  The exact remaining
gate is a row-coherent selection of monotone Pascal paths inside the fixed
row orders.  Marginal Boolean Hall integrality does not prove that
selection.

## 1. Fixed row starts and their forced flags

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},
 \qquad P_1,\ldots,P_m
\]

for the ordered disjoint coordinate pairs used by the first-avoided-pair
extraction, and let \(z\) be the unpaired coordinate.  For phase \(j\),
write

\[
 Q_j=[n]\setminus P_j.
\]

Let \(\Omega_j\) be the selected starts in the exact local factor
\(F_j\) on \(Q_j\), and put

\[
 \Omega=\bigsqcup_{j=1}^m\Omega_j.
\]

Theorem 5.1 of the source gives

\[
 |\Omega|=N_1:=\binom{n}{m-1},
\tag{1.1}
\]

distinct middle owners \(X_\omega\), and a bijection

\[
 \omega\longmapsto L_1(\omega)
\quad\hbox{from }\Omega\hbox{ to }\binom{[n]}{m-1}.
\tag{1.2}
\]

If \(\omega\) is start \(i\) in a cyclic order \(\pi\) of \(Q_j\), define

\[
 L_d(\omega)=I_\pi(i,m-d),\qquad
 U_s(\omega)=I_\pi(i,m+s).
\tag{1.3}
\]

Here \(X_\omega=L_0(\omega)=U_0(\omega)\).  The fixed row order realizes
the literal saturated chain

\[
 L_d(\omega)\subset\cdots\subset L_1(\omega)
 \subset X_\omega\subset U_1(\omega)\subset\cdots
 \subset U_{d+1}(\omega)
\tag{1.4}
\]

whenever \(\omega\) is assigned radius at least \(d\).

Every set in (1.3) is contained in \(Q_j\).  Moreover,
\(L_1(\omega)\) meets every earlier pair \(P_h\), \(h<j\), and avoids
\(P_j\).  Hence every upper flag \(U_s(\omega)\) has the same
first-avoided-pair category \(j\).  This phase residence is an ordering
constraint absent from an abstract symmetric-chain decomposition.

## 2. Canonical transport and the full Pascal corridor

The coupling problem has a finite integral formulation.

### Theorem 2.1 (canonical-column nested transport system)

Restrict every owner to the same-start canonical column (1.3).

Let

\[
 E_0\supseteq E_1\supseteq\cdots\supseteq E_H
\subseteq\Omega
\tag{2.1}
\]

be owner sets.  Assign radius

\[
 \rho(\omega)=\max\{d:\omega\in E_d\}
\]

to \(\omega\in E_0\).  The resulting fixed-row Pascal chains are pairwise
target-disjoint through depth \(H\) if and only if

1. \(U_1\) is injective on \(E_0\);
2. for every \(1\le d\le H\), both \(L_d\) and \(U_{d+1}\) are injective
   on \(E_d\).

In particular, prescribed exact quotas \(M_d\) are realizable by these
canonical columns if and only if such nested sets exist with

\[
 |E_d|=M_d\qquad(0\le d\le H).
\tag{2.2}
\]

#### Proof

Necessity follows because two owners with the same flag target collide in
that Boolean rank.  Conversely, the middle owners are distinct by the
source theorem, and the displayed injectivities make all targets distinct
within every other rank.  Targets in different ranks have different
cardinalities and cannot collide.  Formula (1.4) gives one literal tight
row realization for every retained chain.  Nesting (2.1) is exactly the
condition that every owner receives one initial interval of radii.
\(\square\)

Equivalently, introduce binary variables \(x_{\omega,d}\).  The exact
transport system is

\[
 x_{\omega,d+1}\le x_{\omega,d},\qquad
 \sum_\omega x_{\omega,d}=M_d,
\tag{2.3}
\]

\[
 \sum_{\omega:U_1(\omega)=Y}x_{\omega,0}\le1,
\tag{2.4}
\]

and, for \(d\ge1\),

\[
 \sum_{\omega:L_d(\omega)=S}x_{\omega,d}\le1,
 \qquad
 \sum_{\omega:U_{d+1}(\omega)=T}x_{\omega,d}\le1.
\tag{2.5}
\]

At one fixed depth, (2.5) asks for a matching in the bipartite graph whose
edge indexed by \(\omega\) joins \(L_d(\omega)\) to \(U_{d+1}(\omega)\).
The same owner edges must be nested across all depths.  This is the exact
condition for the canonical same-start columns.  A full Pascal corridor
also permits left/right endpoint choices and is treated below.

For a zero-loss continuation of the source's exact lower coverage one
would have

\[
 E_1=\Omega,\qquad |E_d|=\binom{n}{m-d}
\quad(d\ge1).
\tag{2.6}
\]

Then \(L_d\) and \(U_{d+1}\) would both be bijections onto their symmetric
Boolean ranks.

The row order makes the lower transport especially rigid.  Write one
oriented component's exact outgoing lower colors as

\[
 \cdots,S_{i-2},S_{i-1},S_i,\cdots .
\]

### Lemma 2.2 (canonical ordered-intersection map)

At every position whose preceding \(d-1\) colors lie in the same component,

\[
 \boxed{
 L_d(\omega_i)=\bigcap_{h=0}^{d-1}S_{i-h}.}
\tag{2.7}
\]

In particular,

\[
 L_2(\omega_i)=S_i\cap S_{i-1}.
\tag{2.8}
\]

On the opposite side of the same coordinate order,

\[
 \boxed{
 U_{d+1}(\omega_i)=\bigcup_{h=0}^{d+2}S_{i+h}.}
\tag{2.9}
\]

Only \(O(dJ)\) owner positions over the whole forest can depend on
endpoint collars at depth \(d\).

#### Proof

In its local cyclic coordinate order,

\[
 S_{i-h}=I_\pi(i-h,m-1).
\]

The common interval of the \(d\) displayed windows starts at \(i\) and
ends at \(i+m-d-1\), hence is \(I_\pi(i,m-d)=L_d(\omega_i)\).
The union of the \(d+3\) windows in (2.9) starts at \(i\) and ends at
\(i+m+d\), hence is \(I_\pi(i,m+d+1)=U_{d+1}(\omega_i)\).
Only the first \(d-1\) relevant positions of each cut component lack all
displayed predecessors, and only \(O(d)\) positions at the opposite end
lack all displayed successors. \(\square\)

Thus, if an abstract deletion flow is transported to the fixed paths via
the canonical columns, then, away from \(O(dJ)\) endpoints, its
depth-\(d\) target for \(S_i\) is the ordered intersection (2.7).  For
example, if

\[
 r_d(T)=|\{i:L_d(\omega_i)=T\}|,
\tag{2.10}
\]

then an injective depth-\(d\) selection must discard at least

\[
 \sum_T(r_d(T)-1)_+
\tag{2.11}
\]

of these fixed occurrences.  The unrestricted \(O(m^{-2})\) atom
codegree does not bound the multiplicities (2.10): fixing the path has
conditioned on one
ordered Johnson neighbor at essentially every lower color.

### The full row-coherent corridor

For an owner \(\omega=(j,\pi,i)\), the complete interval corridor through
\(X_\omega=I_\pi(i,m)\) has lower choices

\[
 L_{d,a}(\omega)=I_\pi(i+a,m-d)
 \qquad(0\le a\le d)
\tag{2.12}
\]

and upper choices

\[
 U_{s,b}(\omega)=I_\pi(i-b,m+s)
 \qquad(0\le b\le s).
\tag{2.13}
\]

A row-coherent lower path is a sequence

\[
 a_0=0,\qquad a_{d+1}-a_d\in\{0,1\},
\tag{2.14}
\]

and an upper path is a sequence

\[
 b_0=0,\qquad b_{s+1}-b_s\in\{0,1\}.
\tag{2.15}
\]

These conditions say exactly that each next interval is obtained by
deleting, or adding, one endpoint.

### Theorem 2.3 (exact full-corridor transport)

Prescribed radius quotas are realizable on the fixed rows by pairwise
target-disjoint Pascal corridors if and only if one can:

1. choose nested active owner sets \(E_0\supseteq\cdots\supseteq E_H\)
   of the prescribed sizes;
2. choose for each active owner monotone paths (2.14)--(2.15), through
   its assigned radius; and
3. make the chosen \(L_{d,a_d}\) targets injective on \(E_d\), the chosen
   \(U_{d+1,b_{d+1}}\) targets injective on \(E_d\), and the chosen
   \(U_{1,b_1}\) targets injective on \(E_0\).

#### Proof

Every interval chain through a fixed middle window has the form
(2.12)--(2.15): at each cover step one deletes or adds its left or right
endpoint.  Target-disjointness is precisely injectivity in each Boolean
rank.  Conversely, the chosen monotone paths are literal intervals in the
given row order, and the rankwise injectivities prevent every possible
same-rank collision. \(\square\)

Already the first upper step has a nontrivial row-restricted Hall system.
Put

\[
 \Gamma^+(\omega)
 =\{I_\pi(i,m+1),\,I_\pi(i-1,m+1)\}.
\tag{2.16}
\]

### Corollary 2.4 (first-upper row Hall condition)

A full-corridor first-upper assignment retaining \(M\) owners exists if
and only if

\[
 \boxed{
 \max_{\mathcal A\subseteq\Omega}
 \bigl(|\mathcal A|-|\Gamma^+(\mathcal A)|\bigr)
 \le|\Omega|-M.}
\tag{2.17}
\]

#### Proof

This is the deficiency form of Hall's theorem in the bipartite graph with
left side \(\Omega\), right side \(\binom{[n]}{m+1}\), and neighborhoods
\(\Gamma^+(\omega)\).  Every matched edge is one of the two literal
same-row cover moves. \(\square\)

At later depths, the choices must remain one monotone path for each row
label.  Independent rankwise Boolean flows can splice two different row
labels at a shared target and therefore do not prove Theorem 2.3.

The first-upper Hall defect has an exact graph formula.  For every selected
owner \(X_i\), put

\[
 Z_i=I_\pi(i,m+1)
\]

and make one edge \(Z_{i-1}Z_i\), labelled by \(X_i\).  Let \(\mathcal H^+\)
be the resulting graph on actual rank-\((m+1)\) targets.

### Proposition 2.5 (exact two-parent first-upper deficiency)

The graph \(\mathcal H^+\) is simple.  If its connected components are
\(C\), then the maximum number of owners receiving distinct physical upper
parents is

\[
 \sum_C\min\{e(C),v(C)\},
\tag{2.18}
\]

and the exact owner deficiency is

\[
 \boxed{\delta^+=\sum_C(e(C)-v(C))_+.}
\tag{2.19}
\]

If the selected starts form \(J\) source-row runs, then

\[
 \delta^+=|E(\mathcal H^+)|-|V(\mathcal H^+)|+T,
\qquad T\le J,
\tag{2.20}
\]

where \(T\) is the number of tree components.

#### Proof

The endpoints of an edge determine its owner:

\[
 Z_{i-1}\cap Z_i=X_i.
\]

Distinct middle owners therefore prevent parallel edges.  Assigning an
owner to one of its two upper parents is exactly matching the edges of
\(\mathcal H^+\) injectively into incident vertices.

In a connected component with \(e\le v\), connectedness gives
\(e\in\{v-1,v\}\).  A tree matches each edge to its child after choosing a
root; a unicyclic component orients its cycle cyclically and its attached
trees away from the cycle.  Thus all \(e\) edges can be assigned.  If
\(e>v\), choose a spanning unicyclic subgraph and assign its \(v\) edges;
no assignment can use more than the \(v\) vertices.  This proves
(2.18)--(2.19).

Every connected component has \(e-v\ge-1\), with equality exactly for a
tree.  Summing gives (2.20).  Each tree component contains at least one
source-row run, so \(T\le J\). \(\square\)

In phase \(1\), every start of every local factor row is selected, hence
every source run is a full cycle.  No component of \(\mathcal H^+\) is a
tree.  With \(A_m=\binom{2m-1}{m-1}\),

\[
 \delta_1^+=A_m-
 |\{I_\pi(i,m+1):\pi\in F_1,\ i\in\mathbb Z_{2m-1}\}|.
\tag{2.21}
\]

Thus allowing both physical parents attains, but cannot exceed, the
canonical support size in phase \(1\).

The first lower step has the same exact form.  For
\(S_i=I_\pi(i,m-1)\), make the edge

\[
 I_\pi(i,m-2)\ I_\pi(i+1,m-2),
\tag{2.22}
\]

labelled by \(S_i\).  This graph is simple because the union of the two
endpoints is \(S_i\), and the selected \(S_i\)'s are distinct.  Therefore
its exact deficiency is again (2.19).  In phase \(1\), complementation
inside \(Q_1\) identifies its vertex support with the upper support in
(2.21), so the two first-step deficiencies agree.

### Corollary 2.6 (evolving incidence-graph form)

At any later one-rank corridor transition, provided the currently active
actual interval targets are distinct, make each current target an edge
between its two same-row endpoint deletions (downward) or endpoint
extensions (upward).  The graph is simple, and its exact one-step Hall
loss is

\[
 \sum_C(e(C)-v(C))_+.
\tag{2.23}
\]

Zero loss at that step is equivalent to every component being a
pseudoforest.  The multidepth problem is to orient the edges at every step
so that the next row-labelled incidence graphs continue to have small
cycle excess.

#### Proof

For a downward step, the two endpoint facets have union equal to the
current target; for an upward step, the two endpoint supersets have
intersection equal to it.  Distinct current targets therefore give
distinct graph edges.  Proposition 2.5 applies verbatim.  The chosen
incident vertex fixes the next interval occurrence and hence its two
row-specific choices at the following step. \(\square\)

## 3. The first phase forbids zero loss

The obstruction is visible without estimating any codegree.

Put

\[
 A_m=\binom{2m-1}{m-1}.
\tag{3.1}
\]

In phase \(1\) there are no earlier pairs to meet, so every
\((m-1)\)-subset of \(Q_1\) is selected.  Therefore

\[
 |\Omega_1|=A_m.
\tag{3.2}
\]

Every fixed upper flag of a phase-one owner is contained in \(Q_1\).

### Theorem 3.1 (full-corridor upper-support obstruction)

For the canonical columns on the fixed rows of Section 5:

\[
 |\Omega_1|-|\{U_1(\omega):\omega\in\Omega_1\}|
 \ge \frac{2}{m+1}A_m
 =\frac{W}{2m+1},
\tag{3.3}
\]

and

\[
 |\Omega_1|-|\{U_2(\omega):\omega\in\Omega_1\}|
 \ge
 \frac{6m}{(m+1)(m+2)}A_m
 =\frac{3m}{(2m+1)(m+2)}W.
\tag{3.4}
\]

Consequently \(U_1\) is not injective on \(\Omega\), \(U_2\) is not
injective on \(\Omega\), and the zero-loss nested transport system
(2.6) has no solution.

More generally, every full-corridor solution of Theorem 2.3 satisfies

\[
 |\Omega_1\setminus E_0|\ge \frac{W}{2m+1},
\qquad
 |\Omega_1\setminus E_1|
 \ge\frac{3m}{(2m+1)(m+2)}W.
\tag{3.4a}
\]

#### Proof

There are only

\[
 \binom{2m-1}{m+1}
 =\binom{2m-1}{m-2}
 =\frac{m-1}{m+1}A_m
\tag{3.5}
\]

possible rank-\((m+1)\) flags contained in \(Q_1\).  This proves the first
inequality.  Likewise there are only

\[
 \binom{2m-1}{m+2}
 =\binom{2m-1}{m-3}
 =\frac{(m-1)(m-2)}{(m+1)(m+2)}A_m
\tag{3.6}
\]

possible rank-\((m+2)\) flags contained in \(Q_1\).  Subtracting (3.6)
from \(A_m\) gives the first expression in (3.4).  Finally

\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)},
\tag{3.7}
\]

which gives the displayed \(W\)-normalizations.  Injectivity on all of
\(\Omega\) would imply injectivity on \(\Omega_1\), contradicting both
bounds.  Every alternative corridor interval through a phase-one owner is
also contained in \(Q_1\), so the same support capacities prove (3.4a).
\(\square\)

The obstruction is independent of how the exact local factor \(F_1\) is
chosen.  It comes from the physical residence of every phase-one row in
the \(2m-1\) coordinates \(Q_1\).  An abstract SCD can send a phase-one
owner to an upper target using either omitted coordinate; the fixed row
order cannot.

The bounds are support bounds and may be strict: repeated upper intervals
inside the available support can force still more deletions.

The same argument gives the full phase transport cuts.  Define

\[
 \mathcal U_{j,s}
 =\left\{T\in\binom{Q_j}{m+s}:
 T\cap P_h\ne\varnothing\ \hbox{for every }h<j\right\}.
\tag{3.8}
\]

Because the earlier pairs are disjoint, inclusion--exclusion gives the
exact capacity

\[
 |\mathcal U_{j,s}|
 =\sum_{\ell=0}^{j-1}(-1)^\ell
   \binom{j-1}{\ell}
   \binom{2m-1-2\ell}{m+s}.
\tag{3.9}
\]

### Corollary 3.2 (phase-capacity cuts)

Every feasible nested transport system satisfies

\[
 |E_0\cap\Omega_j|\le|\mathcal U_{j,1}|
\tag{3.10}
\]

and, for \(d\ge1\),

\[
 |E_d\cap\Omega_j|\le|\mathcal U_{j,d+1}|.
\tag{3.11}
\]

#### Proof

Every upper flag of a phase-\(j\) owner lies in the indicated family, and
Theorem 2.3 requires those flags to be distinct. \(\square\)

These are genuine ordering cuts: the abstract Boolean shadow network has
all upper targets available, while the fixed row confines phase \(j\) to
\(\mathcal U_{j,s}\).  The phase-one inequalities (3.3)--(3.4) are their
first two strict instances.

The aggregate category imbalance at the first upper rank is nevertheless
small.

### Proposition 3.3 (first-upper category imbalance is \(O(W/m)\))

Let \(T_j=|\Omega_j|\), and let \(Z_j\) be the number of
rank-\((m+1)\) targets of category \(j\), with an additional category
\(\infty\) for targets meeting every pair.  Then

\[
 \Delta_{\rm cat}:=\sum_j(T_j-Z_j)_+
 \le
 N_1\,\frac{2(2m+1)}{(m+1)(m+2)}
 =O(W/m).
\tag{3.12}
\]

#### Proof

Choose a uniform \(S\in\binom{[n]}{m-1}\), then choose a uniform
two-set \(D\subseteq[n]\setminus S\), and put \(Z=S\cup D\).  The set
\(Z\) is uniform in \(\binom{[n]}{m+1}\), because every \(Z\) has the
same \(\binom{m+1}{2}\) preimages.

If \(\kappa(S)=j\), its category changes only if \(D\) meets \(P_j\).
Conditionally, this has exact probability

\[
 1-\frac{\binom m2}{\binom{m+2}2}
 =\frac{2(2m+1)}{(m+1)(m+2)}.
\tag{3.13}
\]

Hence the total-variation distance between the two category laws is at
most (3.13).  If \(p_j=T_j/N_1\) and \(q_j=Z_j/W\), then for the set of
indices where \(T_j>Z_j\),

\[
 \sum_j(T_j-Z_j)_+
 \le N_1\sum_j(p_j-q_j)_+
 \le N_1\,d_{\rm TV}(p,q),
\]

which proves (3.12). \(\square\)

Even unrestricted Boolean Hall loses only \(O(W/m)\) while preserving
these categories.  Indeed, for a selected category-\(j\) middle owner
\(X\), there are exactly \(m-1\) category-\(j\) rank-\((m+1)\)
supersets inside \(Q_j\), whereas a right target has at most \(m+1\)
selected middle facets.  Thus every left family \(\mathcal A\) has

\[
 |N(\mathcal A)|\ge\frac{m-1}{m+1}|\mathcal A|.
\tag{3.14}
\]

The deficiency form of Hall gives a category-preserving abstract matching
losing at most \(2N_1/(m+1)=O(W/m)\) owners.  Comparing this with
Corollary 2.4 isolates the true first-upper gate: the unrestricted Boolean
graph has \(m-1\) choices per owner, while the fixed row graph has only its
two physical parents.

## 4. Quantitative meaning

The obstruction closes exact zero-loss coupling.  Its proved baseline is
smaller than the constant-one release budget.  If \(H=O(\sqrt m)\), then

\[
 \frac{H}{W}\,
 \frac{3mW}{(2m+1)(m+2)}
 =O(H/m)=o(1).
\tag{4.1}
\]

Thus the mandatory baseline in (3.4) is \(o(W/H)\).  The budget can absorb
that baseline; what is not automatic is that the remaining fixed row
corridors have only \(o(W/H)\) further deficiency.

There is an important constant-one distinction.  The rows themselves are
already literal, so one need not delete an owner merely because its flag
duplicates another flag.  Let

\[
 \Phi_q(\omega)=I_{\pi_\omega}(i_\omega,m+q),
 \qquad
 s_q=|\Phi_q(\Omega)|
\tag{4.2}
\]

for every signed depth carried by the paths.

### Proposition 4.1 (weaker support criterion for constant one)

If, on the required window,

\[
 \sum_q\left(\binom{n}{m+q}-s_q\right)=o(W),
\tag{4.3}
\]

then the fixed path forest, followed by literal one-mask repairs, gives a
word of length \(W+o(W)\) on that window.

#### Proof

The source forest has \(N_1=W-O(W/m)\) distinct middle owners and
\(J=o(W/H)\) components.  Its literal cost is

\[
 N_1+(2H+1)J+O(1)=W+o(W).
\]

It already represents every target in every image \(\Phi_q(\Omega)\).
Append each missing target once.  Equation (4.3) says that the total
repair cost is \(o(W)\). \(\square\)

Thus Theorem 2.3 is the exact answer to the requested *zero-loss nested
Pascal coupling*; Theorem 2.1 is its canonical-column specialization.
Both are stronger than necessary for constant one.
For the fixed literal rows, a sufficient constant-one statement is the
support bound (4.3), equivalently an \(o(W)\) total overload-excess bound
for their canonical flag maps.

For the canonical paths in the source, even the endpoint collars remain in
\(Q_j\), so Theorem 3.1 applies literally.  If one permits new collars
using the omitted coordinates, one has changed the fixed flag system.
Only \(O(d)\) owners per path component can have their depth-\(d\) flags
changed in this way; arranging those changes is an additional endpoint
transport problem, not a consequence of the abstract SCD flow.

The fixed-row analogue of the exact Boolean packing theorem is:

> Find row-coherent monotone paths satisfying Theorem 2.3 in the
> first-avoided-pair forest, with
> \[
> |\Omega\setminus E_0|=o(W/H),
> \qquad
> \sum_{d=1}^H\left(\binom{n}{m-d}-|E_d|\right)=o(W).
> \]

The symmetric orbit multicover's \(O(m^{-2})\) same-rank codegree does not
prove this statement.  It is an average before selecting the local factors
and the first-avoided starts.  Theorem 3.1 shows concretely that after this
conditioning a fixed phase can already have a deterministic
\(\Theta(W/m)\) support deficit.

## 5. Proved/conditional boundary

The following statements are now unconditional.

1. The Section 5 rows give \(N_1\) distinct middle owners, exact
   rank-\((m-1)\) coverage, literal depth-\(H\) residence, and
   \(J=O(W\log^2m/m)=o(W/H)\) components for \(H=O(\sqrt m)\).
2. The simultaneous physical flag problem on those rows is exactly the
   row-coherent monotone-path system of Theorem 2.3; (2.3)--(2.5) is the
   canonical-column specialization.
3. Exact zero-loss coupling is impossible, already in phase \(1\), by
   (3.3)--(3.4).
4. The exhibited unavoidable baseline is
   \(\Theta(W/m)=o(W/H)\).  This baseline is not fatal, but no matching
   upper bound on the full deficiency is proved.
5. Because the fixed rows are already literal, the weaker support
   criterion (4.3), rather than an exact nested matching, is sufficient
   for constant one.

The exact-corridor gate is a row-coherent monotone-path packing with
\(o(W/H)\) owner loss and \(o(W)\) summed rank deficit, subject already to
the \(\Theta(W/m)\) lower bound.  A strictly weaker sufficient
constant-one criterion is (4.3).  Proving only marginal Boolean shadow
inequalities, or applying the
unrestricted \(O(m^{-2})\) overlap estimate after conditioning, establishes
neither statement.

## 6. Adversarial audit

1. The phase-one count is exact: \(\kappa(S)=1\) imposes no condition
   other than \(S\subseteq Q_1\).
2. The upper-support counts do not assume equidistribution or randomness
   of \(F_1\); they hold for every choice of the local exact factor.
3. Equation (3.4) is a lower bound on required deletions, not a claim that
   this many deletions suffice.
4. The proved baseline is not fatal:
   \(\Theta(W/m)=o(W/H)\) for \(H=O(\sqrt m)\).  It is not an upper bound
   on the actual loss.
5. The theorem concerns the fixed row orders with canonical cyclic collars
   requested here.  Arbitrary endpoint recoding would require a separate
   physical Hall theorem and is not silently included.
