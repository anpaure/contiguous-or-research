# Atomic opposition pressure and cut duals for common caps

Date: 2026-07-31  
Lane: K, exact conflict hypergraph  
Status: unconditional finite theorems; the required uniform PBBS/Pascal
pressure bound remains open

## 1. Fixed common-cap instance

Let \(\mathcal S\) be the residual lower-target set.  For each
\(S\in\mathcal S\), let \(D_S\) be its nonempty set of retained candidate
incidences.  A vertex \(v\in D_S\) records both its target and its physical
cell.  Unary-illegal candidates have already been removed, frozen cells have
been reserved, and an owner has been imposed at every physical position.

Let \(\mathcal H\) be the clutter consisting of:

1. same-cell pairs;
2. inclusion-minimal middle-bit blocker covers;
3. inclusion-minimal protected-prepin-bit blocker covers; and
4. a selected lower incidence together with an inclusion-minimal blocker
   cover for one of its required bits.

The exact obstruction theorem in
`MATH_THEOREM_K_ALLK_PASCAL_REROOT_OWNER_CONFLICT_COMPILER_20260731.md`
proves that a selection of one vertex from every \(D_S\) is a literal
common-cap compiler if and only if it contains no member of \(\mathcal H\).
Every \(F\in\mathcal H\) uses at most one vertex from a target part and

\[
             2\le |F|\le \rho:=d+1.                 \tag{1.1}
\]

### Proposition 1.1 (exact bounded-rank obstruction)

A target transversal is a literal common-cap compiler if and only if it
contains no member of \(\mathcal H\).  The four conflict ranks listed above
are respectively

\[
                  2,\qquad d+1,\qquad d,\qquad d+1.  \tag{1.2}
\]

#### Proof

Same-cell pairs are exactly failures of cell injectivity.  Owners keep every
physical letter nonempty.  For a fixed middle or protected-prepin bit, the
bit disappears precisely when the selected incidences omitting it cover all
of its envelope hosts.  For a selected lower incidence, the same statement
holds after adjoining that incidence as the anchor.  Every cover contains
an inclusion-minimal cover, so these are all possible failures of the
maximal common cap; conversely, every listed bad set causes its named
failure.

In an inclusion-minimal cover, every member has a private host.  A middle
row has at most \(d+1\) hosts, a protected lower cell at most \(d\), and a
selected-lower conflict consists of its anchor plus at most \(d\) blockers.
This proves (1.2) and the equivalence. \(\square\)

Without owners there is one additional family, the minimal empty-position
intersections, of rank at most
\(\min\{r,d(d+1)/2\}\).  Everything below remains valid for that larger
clutter, but the owner-filtered rank (1.1) is the useful all-dimensional
form.

## 2. The atomic lopsidependency graph

Choose one random candidate \(X_S\in D_S\) independently for every target
part.  For \(F\in\mathcal H\), let

\[
 A_F=\{X_S=v\text{ for every }v\in F\cap D_S\}.       \tag{2.1}
\]

Join \(F\) and \(G\) when, in some common target part, they prescribe
different candidates.  Denote this graph by \(\Gamma_*\).

### Lemma 2.1 (atomic lopsidependency)

The graph \(\Gamma_*\) is a lopsidependency graph for the bad events
\(A_F\).

#### Proof

Fix \(F\).  Every non-neighbour \(G\) is compatible with the atomic
assignments in \(F\): on a shared target part it prescribes the same value.
Condition on all variables outside the parts used by \(F\).  The indicator
that none of a family of such compatible events occurs is a decreasing
Boolean function of the indicators

\[
       1_{\{X_S=F(S)\}},\qquad S\in\operatorname{parts}(F).
\]

Conditioning on \(A_F\) sets all these indicators to one, so it cannot
increase the probability that all compatible events are avoided.  After
averaging over the outside variables,

\[
 \Pr\!\left(A_F\mid\bigcap_{G\in J}\overline{A_G}\right)
 \le \Pr(A_F)
\]

for every set \(J\) of non-neighbours for which the conditional probability
is defined.  This is the lopsided dependency condition. \(\square\)

Events which reuse the **same** candidate are deliberately not adjacent.
Avoiding such a compatible event can only make \(A_F\) less likely.  This is
the gain over the ordinary graph which joins every pair sharing a target
part.

## 3. Exact candidate-pressure criterion

Give every candidate \(v\) a positive activity \(t_v\).  For
\(F\in\mathcal H\), put

\[
       x_F=\prod_{v\in F}t_v,\qquad 0<x_F<1.         \tag{3.1}
\]

For \(v\in D_S\), let

\[
 \mathcal O(v)=
 \{G\in\mathcal H:G\cap(D_S\setminus\{v\})\ne\varnothing\}              \tag{3.2}
\]

be the bad sets prescribing an alternative to \(v\) in its target part.
Define its survival factor and opposition pressure by

\[
 \Psi_t(v)=\prod_{G\in\mathcal O(v)}(1-x_G),
 \qquad
 P_t(v)=-\log\Psi_t(v)
       =\sum_{G\in\mathcal O(v)}-\log(1-x_G).         \tag{3.3}
\]

### Theorem 3.1 (atomic opposition-capacity theorem)

If

\[
             \boxed{\quad
             \sum_{v\in D_S}t_v e^{-P_t(v)}\ge1
             \quad}                                  \tag{3.4}
\]

for every target part \(S\), then the common-cap instance has an integral
compiler.

#### Proof

Condition (3.4) permits probabilities \(\mu_S(v)\) satisfying

\[
 \sum_{v\in D_S}\mu_S(v)=1,
 \qquad
 0<\mu_S(v)\le t_v\Psi_t(v).                         \tag{3.5}
\]

For example, normalize the right sides within each target part.  Under the
independent law with marginals \(\mu_S\),

\[
 \Pr(A_F)
 =\prod_{v\in F}\mu_{\sigma(v)}(v)
 \le x_F\prod_{v\in F}\Psi_t(v).                    \tag{3.6}
\]

The union of the sets \(\mathcal O(v)\), \(v\in F\), is exactly the
lopsidependency neighbourhood \(\Gamma_*(F)\).  A neighbour opposing two
members of \(F\) is counted twice on the right of (3.6); because every
factor lies in \((0,1)\), this only decreases that product.  Hence

\[
 \Pr(A_F)
 \le x_F\prod_{G\in\Gamma_*(F)}(1-x_G).              \tag{3.7}
\]

The asymmetric lopsided local lemma gives positive probability of avoiding
every bad event.  By the exact obstruction theorem, the resulting
transversal is a literal common-cap compiler. \(\square\)

This is a finite, candidate-specific theorem.  It allows pressure to vary
inside a target part: many low-pressure candidates can compensate for a few
locked candidates.

### Corollary 3.2 (normalized candidate pressure)

Write \(n_S=|D_S|\), choose \(c>1\) with \(c<\min_S n_S\), and set

\[
 t_v={c\over n_S}\quad(v\in D_S),
 \qquad
 x_F={c^{|F|}\over\prod_{S\in\operatorname{parts}(F)}n_S}.               \tag{3.8}
\]

Then a compiler exists whenever

\[
 {1\over n_S}\sum_{v\in D_S}e^{-P_c(v)}\ge{1\over c}
 \quad\text{for every }S.                             \tag{3.9}
\]

In particular, it is enough that, in each target part, a fraction at least
\(\eta\) of the candidates satisfy

\[
       P_c(v)\le\log(c\eta),
       \qquad \eta>{1\over c}.                        \tag{3.10}
\]

No maximum-pressure hypothesis is needed.

### Corollary 3.3 (eventwise atomic-pressure cut)

Fix any independent candidate law, write

\[
 p_F=\Pr(A_F),\qquad p_*=\max_Fp_F,
\]

and choose \(1<\theta<p_*^{-1}\).  A compiler exists if, for every bad set
\(F\),

\[
 \boxed{\quad
 \sum_{G\in\Gamma_*(F)}-\log(1-\theta p_G)
 \le\log\theta.\quad}                                \tag{3.11}
\]

Indeed, use \(x_F=\theta p_F\) in the asymmetric lopsided local lemma.  The
linearized sufficient form is

\[
 \boxed{\quad
 \sum_{G\in\Gamma_*(F)}p_G
 \le {1-\theta p_*\over\theta}\log\theta.\quad}      \tag{3.12}
\]

This follows from
\(-\log(1-\theta p_G)\le\theta p_G/(1-\theta p_*)\).
The optimal \(\theta\) in (3.12) satisfies
\(\log\theta+\theta p_*=1\); as \(p_*\to0\), the allowed atomic neighbour
mass tends to \(1/e\).  Taking \(\theta=2\) and \(p_*\le1/4\) recovers the
explicit threshold \(\log2/4\).
For a purely candidatewise check, the left sides of (3.11)--(3.12) may be
replaced by the larger multiplicity sums over
\(v\in F\) and \(G\in\mathcal O(v)\).

## 4. Countable pressure cuts and honest constants

For a candidate \(v\in D_S\), let \(d_j(v)\) be the number of size-\(j\)
bad sets containing \(v\), and let

\[
 D_j(S)=|\{F\in\mathcal H:|F|=j,
                         F\cap D_S\ne\varnothing\}|.
\tag{4.1}
\]

Because a bad set uses at most one candidate from a part,

\[
 \sum_{v\in D_S}d_j(v)=D_j(S),
 \qquad
 |\{G\in\mathcal O(v):|G|=j\}|=D_j(S)-d_j(v).        \tag{4.2}
\]

### Theorem 4.1 (target-part cluster pressure)

Choose arbitrary weights \(b_v>0\), and put

\[
 \mu_F=\prod_{v\in F}b_v,
 \qquad
 B_S=\sum_{v\in D_S}b_v,
 \qquad
 T_S=\sum_{\substack{F\in\mathcal H\\F\cap D_S\ne\varnothing}}\mu_F.
\tag{4.2a}
\]

If

\[
                 \boxed{\quad B_S\ge1+T_S\quad}       \tag{4.2b}
\]

for every target part \(S\), then a common-cap compiler exists.

#### Proof

Use the independent law \(q_v=b_v/B_S\) for \(v\in D_S\).  Then

\[
 \Pr(A_F)={\mu_F\over
               \prod_{S\in\operatorname{parts}(F)}B_S}.
\]

In the ordinary dependency graph, all bad events using a fixed target part
form a clique.  The closed-neighbourhood independent-set polynomial in the
cluster-expansion local lemma is at most

\[
       \prod_{S\in\operatorname{parts}(F)}(1+T_S).
\]

Indeed, an independent family of neighbours uses mutually disjoint target
parts.  Assign each member to one part which it shares with \(F\); the
corresponding monomial occurs in the displayed product.  Condition (4.2b)
therefore gives the cluster-expansion inequality

\[
 \Pr(A_F)\le
 {\mu_F\over
  \prod_{S\in\operatorname{parts}(F)}(1+T_S)}.
\]

The cluster-expansion local lemma and the exact obstruction theorem finish
the proof. \(\square\)

For uniform \(b_v=b\), (4.2b) is the finite cut

\[
 \boxed{\quad
 n_Sb\ge1+\sum_{j=2}^{\rho}D_j(S)b^j
 \quad(S\in\mathcal S).\quad}                        \tag{4.2c}
\]

With \(m=\min_Sn_S\) and \(b=t/m\), \(t>1\), it is enough that

\[
 \sum_{j=2}^{\rho}D_j(S)\left({t\over m}\right)^j
 \le t-1.                                            \tag{4.2d}
\]

For a single arity \(j\), the best normalized density allowed by this
cluster cut is

\[
 \max_{t>1}{t-1\over t^j}
 ={(j-1)^{j-1}\over j^j};                            \tag{4.2e}
\]

the pair-conflict constant is \(1/4\).  This improves the uniform atomic
Jensen constant below, while the candidate-level atomic test can be better
on heterogeneous atlases.  The two criteria are complementary.

Now take a uniform atomic activity \(t_v=a\in(0,1)\).  Theorem 3.1 becomes
the exact finite family of **candidate-pressure cuts**

\[
 \boxed{\quad
 C_S(a):=
 a\sum_{v\in D_S}
       \prod_{j=2}^{\rho}(1-a^j)^{D_j(S)-d_j(v)}
 \ge1\quad}                                          \tag{4.3}
\]

for all target parts \(S\).

Jensen's inequality gives the simpler, weaker sufficient cuts

\[
 \boxed{\quad
 \log(a n_S)\ge
 \left(1-{1\over n_S}\right)
 \sum_{j=2}^{\rho}D_j(S)[-\log(1-a^j)]
 \quad}.                                             \tag{4.4}
\]

Indeed, the exponential is convex and the mean of
\(D_j(S)-d_j(v)\) over \(v\in D_S\) is
\((1-1/n_S)D_j(S)\).

Let \(m=\min_Sn_S\), put \(a=t/m\), where \(1<t<m\), and use

\[
 -\log(1-a^j)\le {a^j\over1-a^j}
                 \le {a^j\over1-a^2}.               \tag{4.5}
\]

The following completely explicit inequalities imply (4.4):

\[
 \boxed{\quad
 \sum_{j=2}^{\rho}D_j(S)\left({t\over m}\right)^j
 \le
 \left(1-{t^2\over m^2}\right)\log t
 \quad(S\in\mathcal S).\quad}                       \tag{4.6}
\]

Thus a genuine asymptotic closure theorem is available: along any sequence
with \(m\to\infty\), if for some fixed \(t>1\),

\[
 \limsup\ \sup_S
 \sum_{j=2}^{\rho}{D_j(S)t^j\over m^j}<\log t,       \tag{4.7}
\]

then all sufficiently large instances have common caps.  This remains true
when \(\rho=d+1\) grows, provided the displayed sum is uniform.

If only arity \(j\) is present, the largest asymptotic density allowed by
this Jensen bound as \(m\to\infty\) is

\[
       \max_{t>1}{\log t\over t^j}={1\over je},
       \qquad t=e^{1/j}.                              \tag{4.8}
\]

For pair conflicts the honest normalized threshold of this Jensen reduction
is therefore \(1/(2e)\), not an unspecified positive constant.  The
candidate-level cut (4.3) can be strictly better than (4.6), since it
retains the distribution of \(d_j(v)\); the cluster cut (4.2c) has the
larger uniform pair threshold \(1/4\).

## 5. Why a generic LLL or nibble still does not close all \(k\)

Take \(n\) target parts

\[
       D_i=\{(i,c):c\in[m]\},
\]

and make two candidates conflict precisely when they use the same cell
\(c\).  This is a rank-two conflict clutter with every part of size \(m\).
For \(n=m+1\), no transversal exists by the pigeonhole principle.  Hence
bounded rank, bounded depth, and growing lists do not imply any LLL or
nibble conclusion.

Even the feasible case \(n=m\) lies outside the uniform independent-choice
pressure range.  It has

\[
       D_2(i)=m(m-1),
\]

so its normalized density tends to one, four times even the stronger
cluster threshold \(1/4\).  Nevertheless any permutation of the cells is a
transversal.
This is a precise diagnostic: the cell-matching part should be extracted
deterministically, or sampled from a negatively dependent matching law,
rather than paid for by an independent-choice LLL.

For Boolean/Johnson carriers, owner orientation proves only
\(\rho\le d+1\).  It does not prove (3.9), (4.3), or (4.7).  An asymptotic
nibble must supply one of the following genuinely new inputs:

- a positive density of candidates with bounded atomic opposition pressure;
- a normalized conflict profile satisfying (4.2d) or (4.7); or
- a negatively dependent law which removes the deterministic cell-matching
  conflicts before the cap conflicts are exposed.

Without such a dispersion theorem, generic LLL numerics do not close the
coefficient-one conjecture.

## 6. Exact finite cutwise alternatives

### 6.1 Integral minimal-conflict system

Introduce \(y_v\in\{0,1\}\).  The following system is feasible if and only
if a common-cap compiler exists:

\[
 \sum_{v\in D_S}y_v=1                         \quad(S\in\mathcal S),
                                                               \tag{6.1}
\]

\[
 \sum_{v:\operatorname{cell}(v)=C}y_v\le1     \quad(C\text{ a cell}),
                                                               \tag{6.2}
\]

\[
 \sum_{v\in F}y_v\le |F|-1                   \quad(F\in\mathcal H
                                                    \text{ noncell}).
                                                               \tag{6.3}
\]

Under owners every noncell cut has width at most \(d+1\).  Separation is
literal: build the maximal cap of an integral assignment; a missing middle,
prepin, or selected-lower bit yields an inclusion-minimal violated cut.  In
the unoriented extension, an empty letter yields the additional minimal
empty-position cut.  Since there are finitely many assignments, cut
generation ends with a compiler or a finite infeasibility certificate.

### 6.2 Fractional cut dual

Let \(\mathcal R\) contain every cell row, with support the candidates using
that cell and right side \(b_R=1\), and every noncell row \(F\), with
\(b_F=|F|-1\).  For weights \(z_R\ge0\), put

\[
       q_z(v)=\sum_{R\ni v}z_R.                       \tag{6.4}
\]

### Theorem 6.1 (exact fractional cut criterion)

The relaxation of (6.1)--(6.3) to \(y_v\ge0\) is feasible if and only if

\[
 \boxed{\quad
 \sum_{S\in\mathcal S}\min_{v\in D_S}q_z(v)
 \le \sum_{R\in\mathcal R}z_Rb_R
 \quad\text{for every }z\ge0.\quad}                  \tag{6.5}
\]

#### Proof

For a point in the product of the target simplices, the minimum of the
weighted row load is

\[
 \min_y\sum_vq_z(v)y_v
   =\sum_S\min_{v\in D_S}q_z(v).                     \tag{6.6}
\]

Thus (6.5) is necessary by summing the row inequalities with weights \(z\).
Conversely, if the image of the product of simplices under the row-incidence
map misses the down-set \(b-\mathbb R^{\mathcal R}_{\ge0}\), a separating
hyperplane can be chosen with a nonnegative normal \(z\); it gives the
strict reverse of (6.5). \(\square\)

A strict reverse inequality in (6.5) is therefore a solver-free Farkas
obstruction.  Absence of such an obstruction proves only fractional
feasibility.  More generally, take binary target parts on any odd cycle and
forbid the two equal-value pairs on every cycle edge.  Assigning weight
\(1/2\) to every candidate satisfies every pair cut, but an integral
transversal would be a two-colouring of an odd cycle and does not exist.
Every proper path subinstance is satisfiable, so minimal integral
obstruction support is unbounded even for rank-two conflict clutters.

### Corollary 6.2 (the exact TU route)

If the matrix consisting of the target-part rows in (6.1), the aggregate
cell rows in (6.2), and the noncell conflict rows in (6.3) is totally
unimodular, then (6.5) is necessary and sufficient for an integral
common-cap compiler.

#### Proof

All right sides are integral.  Total unimodularity makes every nonempty
fractional relaxation have an integral vertex; the target-part equalities
and nonnegativity make that vertex a zero-one transversal.  Theorem 6.1
characterizes nonemptiness of the relaxation. \(\square\)

The odd-cycle family shows that total unimodularity cannot follow from
rank two, and hence cannot follow from the owner rank bound alone.  A TU
proof after orbit lifting must use additional Pascal/laminar structure.

### 6.3 Integral Hall kernels

There is a useful deterministic sufficient alternative.  Suppose one can
retain a candidate kernel \(K\) such that

1. \(K\) contains no noncell bad set from \(\mathcal H\); and
2. in the bipartite target-cell graph induced by \(K\), every target
   subfamily \(A\) satisfies
   \[
       |N_K(A)|\ge |A|.                              \tag{6.7}
   \]

Then Hall's theorem gives a cell-injective target transversal inside
\(K\).  Condition 1 excludes every remaining cap conflict, so this
transversal is a common-cap compiler.

More generally, let \(\mathcal N\) be a matroid on the candidates such that
every \(\mathcal N\)-independent set is cell-injective and
\(\mathcal H\)-free.  Rado's transversal theorem gives a compiler whenever

\[
 r_{\mathcal N}\!\left(\bigcup_{S\in A}D_S\right)\ge|A|
 \quad\text{for every }A\subseteq\mathcal S.          \tag{6.8}
\]

Equations (6.7)--(6.8) are the clean cutwise route when atomic pressure is
too large.  They require a carrier-specific conflict-free kernel or
laminar resource representation; neither follows from bounded rank alone.

## 7. Exact all-dimensional gate

The conflict-hypergraph lane is now reduced to either of two concrete
statements for a PBBS/Pascal atlas after forced edges and owners:

1. prove the atomic or cluster pressure cuts (3.4) or (4.2b), or more
   restrictively one of the explicit sufficient forms (3.9), (4.2c),
   (4.3), or (4.6); or
2. construct a conflict-free Hall/Rado kernel satisfying (6.7) or (6.8).

Either statement composes with the proved Pascal-reroot compiler theorem to
give the desired upper bound at the scheduled length.  The exact integral
system (6.1)--(6.3) remains the finite fallback.  No claim is made that the
authenticated \(k=16\) matching lies in the independent-choice LLL regime;
\(k=16\) is already solved and is used only to authenticate the common-cap
semantics.
