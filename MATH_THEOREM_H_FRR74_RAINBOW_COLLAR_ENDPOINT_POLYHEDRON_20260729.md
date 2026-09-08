# `FRR(7,4)`: the exact rainbow-collar endpoint polyhedron

Date: 2026-07-29  
Lane: H  
Status: exact formulation and polynomial sufficient subtheorems proved.  No
`FRR(7,4)` rethreading is claimed.

## 0. Verdict

Let `B_0` be the rank-seven turn derivative of the certified `k=15` factor
from
`MATH_THEOREM_K16_BIRESIDENT_COMPLEMENT_DOUBLE_AND_TURN_SELECTOR_20260729.md`.
For a fixed collar-hitting, four-separated cut set `H`, the remaining
reconnection problem has an exact `0-1` configuration formulation:

* choose exactly one new seam of every cut rank-eight union colour;
* use every exposed endpoint exactly once;
* cover every rank-six lower colour whose old providers were all cut; and
* permit only seams satisfying an exact positive-residence collar rule.

After projecting from pair variables `y` to incidence marginals `z`, degree
plus exact upper restoration is a TU bipartite `(1,2)`-matching.  Relative to
the deleted incidences, this marginal system is also a zero-divergence signed
circulation in the rank-seven/rank-eight incidence graph.  The unprojected
`y` equations are not TU.  Residence and lower `q1` are the precise
non-network terms: both depend on the **pair** of incidences chosen at one
upper colour.

A polynomial sufficient theorem survives.  First reserve disjoint seams for
the vanished lower colours.  If every remaining upper colour has a
residence-compatible pair graph which is the base graph of a rank-two
matroid, completion is ordinary two-matroid intersection.  The exact
common-base rank inequalities are necessary and sufficient in this
subclass.  If those local graphs are complete, this specializes to one
capacitated Hall/max-flow test.

This hypothesis is not automatic.  Exact positive collar compatibility can
violate rank-two basis exchange on four ports.  More basically, three
compatible Johnson seams on three endpoints give the minor

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad |\det|=2.                                             \tag{0.1}
\]

Thus the natural configuration class is genuinely non-TU.  Whether this
minor occurs in the particular frozen `B_0` endpoint graphs remains an
instance audit.  The full `FRR(7,4)` integer hull has no proved polynomial
separation oracle.  The result below identifies exactly what an instance
audit would have to prove in order to recover flow or matroid intersection.

## 1. The facet factor, cuts, and ports

Write the components of `B_0` cyclically.  Its edge of rank-eight union
colour `U` is denoted `e_U`; upper perfection makes this edge unique.  For a
rank-six set `R`, let

\[
 \ell_0(R)=|\{e\in E(B_0):c^-(e)=R\}|                         \tag{1.1}
\]

be its old lower load.

Let `h_e in {0,1}` indicate that the old edge `e` is cut.  The `1,425`
length-three positive runs of `B_0` have four-edge closed collars.  Let
`mathcal C` be that collar family.  Every repair must satisfy

\[
 \sum_{e\in C}h_e\ge1\qquad(C\in\mathcal C).                 \tag{1.2}
\]

This note works in the **four-separated cut subclass**.  If
`e_i,e_(i+1),...` are the cyclic edges of one old component, impose

\[
 \sum_{j=0}^{3}h_{e_{i+j}}\le1\qquad(i\text{ cyclic}).        \tag{1.3}
\]

Two consecutive cuts at cyclic edge distance `d` leave a retained path with
`d` vertices.  Hence (1.3) is equivalent to requiring every retained path
to have at least four vertices.  It also implies that no two cut edges share
a vertex, so every exposed vertex has degree deficit exactly one.

Every old edge `e=vw` has two **ports**, one at `v` looking inward along the
retained old path and one at `w` looking inward in the other direction.  A
port `p` records:

* its old edge `e(p)`;
* its rank-seven endpoint state `v(p)`; and
* for every coordinate `x`, the capped inward terminal positive length

  \[
  \lambda_x(p)=
  \begin{cases}
  0,&x\notin v(p),\\
  \min(4,\text{number of consecutive inward states containing }x),
       &x\in v(p).
  \end{cases}                                                \tag{1.4}
  \]

Because (1.3) keeps the next cut at least four vertices away, (1.4) is fixed
local data of the oriented old edge; it does not depend on the other cuts.

## 2. Exact positive-residence compatibility

Condition (4.8) in the source theorem is sufficient, but it also protects
zero-runs.  `FRR(7,4)` needs positive residence only, so the exact rule is
strictly weaker.

### Lemma 2.1 (exact positive seam rule)

Let `p,q` be distinct active ports whose endpoint states are Johnson
adjacent.  The new seam `v(p)v(q)` creates no positive run of length below
four at that seam if and only if, for every coordinate `x`,

\[
\begin{array}{ll}
 \lambda_x(p)+\lambda_x(q)\ge4,
     &x\in v(p)\cap v(q),\\
 \lambda_x(p)\ge4,
     &x\in v(p)\setminus v(q),\\
 \lambda_x(q)\ge4,
     &x\in v(q)\setminus v(p),\\
 \text{no condition},
     &x\notin v(p)\cup v(q).
\end{array}                                                   \tag{2.1}
\]

Call such a port pair **positive-compatible**.

#### Proof

If `x` is present at both seam endpoints lying on different retained paths,
the seam joins two disjoint inward terminal positive runs, whose total
length is the first line of (2.1).  The same is true for the two ends of one
retained path unless `x` is constant one on that whole path.  In the latter
case the path itself has at least four vertices, both capped lengths equal
four, and the run is automatically safe; no equality with their sum is
needed.  If `x` is present at exactly one endpoint, that side's terminal run
ends before reaching the other endpoint and has precisely the length in the
second or third line.  If it is absent at both endpoints, the seam contains
no positive `x`-run.  These cases are exhaustive, and failure of a stated
inequality literally exhibits the corresponding maximal short positive
run.  QED.

### Lemma 2.2 (local-to-global collar criterion)

Assume (1.2) and (1.3).  A reconnection of all ports is positive-resident at
depth four if and only if every new seam is positive-compatible.

#### Proof

An old positive run meeting no new seam is safe: every old short run has a
cut in its closed collar by (1.2).  A run meeting exactly one seam is safe
exactly by Lemma 2.1.  A new run meeting at least two seams contains an
entire intermediate retained path on which its coordinate is constant one;
that path has at least four vertices by (1.3).  Conversely, a seam violating
(2.1) produces the short run described in Lemma 2.1.  QED.

The retained-path hypothesis also ensures every newly formed factor
component has at least four vertices.  Uncut old components of `B_0` already
have length at least four.

## 3. Exact simultaneous cut-and-reconnection system

Let `mathcal A` be the set of unordered pairs `{p,q}` of ports such that

1. `v(p)` and `v(q)` are distinct Johnson-adjacent rank-seven states; and
2. `{p,q}` satisfies (2.1).

Introduce `m_pq in {0,1}` for `{p,q} in mathcal A`.  The following system is
static and exact in the four-separated cut subclass:

\[
 \sum_{q:\{p,q\}\in\mathcal A}m_{pq}=h_{e(p)}
       \qquad\text{for every port }p,                           \tag{3.1}
\]

\[
 \sum_{\substack{\{p,q\}\in\mathcal A\\
                   v(p)\cup v(q)=U}}m_{pq}=h_{e_U}
       \qquad\left(U\in\binom{[15]}8\right),                  \tag{3.2}
\]

\[
 \ell_0(R)
 -\sum_{e:c^-(e)=R}h_e
 +\sum_{\substack{\{p,q\}\in\mathcal A\\
                   v(p)\cap v(q)=R}}m_{pq}\ge1
       \qquad\left(R\in\binom{[15]}6\right).                 \tag{3.3}
\]

These are imposed together with (1.2), (1.3), and binary bounds.

### Theorem 3.1 (exact separated-cut polyhedron)

Integral solutions of (1.2), (1.3), and (3.1)--(3.3) are in bijection with
four-separated collar rethreadings of `B_0` which

* preserve degree two;
* restore every cut upper `q1` colour exactly once;
* retain complete lower `q1` support; and
* have positive residence and component length at least four.

#### Proof

Equation (3.1) activates the two ports of every cut edge and matches every
active port once; inactive ports cannot be used.  Because (1.3) makes the
active endpoint states distinct, the selected seams form a simple matching
which restores degree two.

The old factor is upper-perfect.  If `e_U` is retained, (3.2) forbids a new
edge of colour `U`; if it is cut, (3.2) inserts exactly one.  Thus the upper
palette is restored with its old exact loads.  Equation (3.3) is precisely
the signed lower-load ledger after old edges are cut and new seams inserted.
It asks only for support at least one; restoring every old lower
multiplicity would be an unnecessary stronger condition.

Equations (1.2), (1.3), and the definition of `mathcal A` give positive
residence by Lemma 2.2 and component length by the retained-path argument.
Every physical rethreading in this subclass defines the unique corresponding
`h,m` vector and satisfies the same ledgers, proving the converse.  QED.

This is an exact `0-1` formulation, not an assertion that its linear
relaxation is integral.

## 4. The fixed-cut endpoint configuration polytope

Fix a cut set `H` satisfying (1.2) and (1.3).  Let `P_H` be its `2|H|`
active ports and let

\[
 \mathcal U_H=\{U:e_U\in H\}.                                 \tag{4.1}
\]

For `U in mathcal U_H`, define the residence-compatible pair graph

\[
 K_U=\bigl\{\{p,q\}\subset P_H:
 v(p)\cup v(q)=U\text{ and }\{p,q\}\text{ satisfies (2.1)}\bigr\}. \tag{4.2}
\]

The cut upper colours are distinct because `B_0` is upper-perfect.  Put

\[
 \ell_H(R)=\ell_0(R)-|\{e\in H:c^-(e)=R\}|,
 \qquad
 \mathcal D_H=\{R:\ell_H(R)=0\}.                              \tag{4.3}
\]

For every `{p,q} in K_U`, introduce `y_(U,pq) in {0,1}`.  Then:

\[
 \sum_{\{p,q\}\in K_U}y_{U,pq}=1
       \qquad(U\in\mathcal U_H),                              \tag{4.4}
\]

\[
 \sum_{\substack{U,\{p,q\}\in K_U\\s\in\{p,q\}}}
 y_{U,pq}=1
       \qquad(s\in P_H),                                     \tag{4.5}
\]

\[
 \ell_H(R)+
 \sum_{\substack{U,\{p,q\}\in K_U\\
                   v(p)\cap v(q)=R}}y_{U,pq}\ge1
       \qquad\left(R\in\binom{[15]}6\right).                \tag{4.6}
\]

### Corollary 4.1 (exact fixed-`H` gate)

The binary system (4.4)--(4.6) is feasible if and only if `H` has a valid
rainbow-collar rethreading in the separated-cut architecture.

Only rows indexed by `mathcal D_H` are nontrivial in (4.6).  A fixed upper
colour `U` and fixed lower colour `R subset U` determine at most one seam:
if `U\setminus R={a,b}`, its endpoints must be `U-a` and `U-b`.

## 5. What is flow, and what is not

For a configuration vector `y`, define its incidence marginals

\[
 z_{U,p}=\sum_{q:\{p,q\}\in K_U}y_{U,pq}.                     \tag{5.1}
\]

If pair compatibility and lower colours are temporarily forgotten, the
exact marginal system is

\[
 \sum_{p:v(p)\subset U}z_{U,p}=2\quad(U\in\mathcal U_H),
 \qquad
 \sum_{U:v(p)\subset U}z_{U,p}=1\quad(p\in P_H),              \tag{5.2}
\]

with `0<=z<=1`.  This is a bipartite `(2,1)`-factor and is TU.

### Proposition 5.1 (the marginal Hall theorem)

The compatibility-free system (5.2) is feasible if and only if

\[
 |N(\mathcal S)|\ge2|\mathcal S|
       \qquad(\mathcal S\subseteq\mathcal U_H),               \tag{5.3}
\]

where `N(mathcal S)` is the set of exposed ports whose endpoint state is a
facet of at least one colour in `mathcal S`.

#### Proof

Split every upper colour into two identical unit-demand copies and give each
port capacity one.  The usual capacitated Hall theorem gives (5.3), and a
max-flow realizes the incidences.  Conversely any realization uses two
distinct ports for every colour and hence supplies the inequality.  QED.

Let `z^0` be the old incidence vector of the cut edges.  Both `z` and `z^0`
have degree two at every cut upper colour and the same total incidence at
every rank-seven endpoint.  Orient new incidences from upper colours to
endpoints and old incidences in the reverse direction.  Then `z-z^0` is a
zero-divergence integral circulation in the bipartite middle-levels
incidence graph and decomposes into alternating even circuits.

This proves that degree plus exact upper restoration is both a bipartite
matching and a signed circulation.  It does **not** solve (4.4)--(4.6): a
marginal `z` can select two incidences at `U` which are not an edge of
`K_U`, and the lower colour is a function of that selected pair.

## 6. A polynomial matroidal Hall theorem

The following is the strongest clean polynomial sufficient theorem obtained
here.

Choose, for every vanished lower colour `R in mathcal D_H`, a **service
portal**

\[
 w_R=(U_R,\{p_R,q_R\}),\qquad
 \{p_R,q_R\}\in K_{U_R},\qquad
 v(p_R)\cap v(q_R)=R,                                         \tag{6.1}
\]

such that all `U_R` are distinct and all service ports are pairwise
disjoint.  Fix these seams, and delete their colours and ports.  Denote the
remaining colour and port sets by `mathcal U'` and `P'`.

For each `U in mathcal U'`, let `I_U={(U,p):p in P', v(p) subset U}` be its
incidence copies and let `mathcal B_U` be the pairs in `K_U` that remain
inside `P'`.

### Theorem 6.1 (matroidal collar completion)

Assume that for every remaining `U`, `mathcal B_U` is the family of bases of
a rank-two matroid `M_U` on `I_U`.  Put

\[
 M=\bigoplus_{U\in\mathcal U'}M_U                              \tag{6.2}
\]

and let `N` be the partition matroid on all remaining incidence copies, with
capacity one for the part indexed by each port `p in P'`.  A completion of
the service portals exists if and only if

\[
 r_M(A)+r_N(E\setminus A)\ge2|\mathcal U'|
       \qquad(A\subseteq E),                                  \tag{6.3}
\]

where `E=bigcup_U I_U`.

Consequently (6.1) plus (6.3) is a polynomially checkable sufficient
certificate for the exact endpoint system (4.4)--(4.6).

#### Proof

A set of `2|mathcal U'|` incidence elements independent in `M` must have
rank two in every summand, so it chooses one allowed pair from every
`mathcal B_U`.  Independence in `N` uses each remaining port at most once;
because `|P'|=2|mathcal U'|`, a full-size common independent set uses every
port exactly once.  It is therefore exactly a compatible completion.

The standard matroid-intersection min-max theorem says that the maximum size
of a common independent set is

\[
 \min_{A\subseteq E}\bigl(r_M(A)+r_N(E\setminus A)\bigr).
\]

This maximum reaches `2|mathcal U'|` exactly under (6.3).  The fixed service
portals already cover every row in `mathcal D_H`; all other lower rows had
positive retained load.  Thus the resulting completion satisfies (4.6).
QED.

### Lemma 6.2 (local recognition)

A nonempty family of allowed two-element subsets is the base family of a
rank-two matroid if and only if, after deleting loop elements, its graph is
complete multipartite.

#### Proof

In a rank-two matroid, two nonloop elements fail to form a base exactly when
they are parallel.  Parallelism is an equivalence relation, and every pair
from distinct classes is a base.  Conversely, the parts of a complete
multipartite graph may be declared parallel classes; pairs crossing parts
are precisely the bases of the resulting rank-two matroid.  QED.

If every `K_U` is complete on its eligible ports, `M_U` is uniform rank two
and Theorem 6.1 collapses to Proposition 5.1 after the service portals are
removed.  More generally, (6.3) is separable by the usual matroid-
intersection/rank-oracle algorithm.

### Corollary 6.3 (elementary rectangular Hall certificate)

After fixing the service portals, suppose one can choose two disjoint port
classes `L_U,R_U` for every remaining colour such that

\[
 L_U\times R_U\subseteq K_U.                                  \tag{6.4}
\]

Create two slots `U^L,U^R` with neighborhoods `L_U,R_U`.  If the resulting
slot-to-port graph satisfies Hall's condition, a perfect matching of its
slots gives a valid completion.  This is a single max-flow/min-cut
certificate and needs no matroid machinery.

## 7. Exact obstructions to the polynomial regimes

### Proposition 7.1 (residence compatibility need not be matroidal)

Fix one rank-eight top
`U={a,b,c,d,e,f,g,h}` and let `p_s` have endpoint state `U-s`.  Assign the
three short terminal lengths at the four ports as follows; every other
present coordinate has terminal length four:

\[
\begin{array}{c|ccc}
 &\lambda=1&\lambda=2&\lambda=3\\ \hline
p_a&c&d&e\\
p_b&e&d&c\\
p_c&b&e&f\\
p_d&f&e&b
\end{array}.                                                   \tag{7.1}
\]

Then `{p_a,p_b}` and `{p_c,p_d}` satisfy (2.1), while `{p_b,p_c}` and
`{p_b,p_d}` fail it.  For the two alleged bases

\[
 B_1=\{p_a,p_b\},\qquad B_2=\{p_c,p_d\},
\]

basis exchange at `p_a` would require one of the two failed pairs.  Each row
of (7.1) is physically realizable by a four-state inward Johnson path: from
the endpoint, successively drop the coordinates in its `1,2,3` columns and
insert three coordinates outside the endpoint.  Thus the positive-residence
transition family is not forced by Johnson chronology to be a rank-two
matroid.  Whether this four-port pattern occurs in the frozen `B_0` endpoint
graphs is an unperformed finite audit, not part of the theorem.

### Proposition 7.2 (smallest natural non-TU minor)

Fix a rank-six set `R` and distinct `a,b,c notin R`.  The three rank-seven
states

\[
 v_a=R+a,\qquad v_b=R+b,\qquad v_c=R+c                         \tag{7.2}
\]

form a Johnson triangle.  If its three seams are compatible, their upper
colours are the three distinct sets `R+a+b`, `R+b+c`, `R+c+a`.  Restricting
the seam columns to the three endpoint rows gives, up to permutations,

\[
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix},
 \qquad \det=2.                                               \tag{7.3}
\]

The pattern is compatible with literal four-state Johnson collars: choose a
distinct coordinate `f_s in R` for each port.  At `v_s`, keep its unique
coordinate `s` and the five coordinates of `R\setminus\{f_s\}` through four
inward states, vary the seventh coordinate by Johnson moves, and let `f_s`
enter only at the endpoint.  For two ports, each short common-coordinate
terminal is paired with a terminal of length four, so (2.1) holds.  This
proves that (7.3) is Johnson-native rather than an arbitrary hypergraph
minor.  It is minimal in order, since every `1 x 1` or `2 x 2` zero-one
determinant has absolute value at most one.

Therefore the full configuration matrix class is not generally TU.  This is
a local Johnson-native obstruction, not a claim that the frozen `B_0`
cut-instance contains the three required compatible ports.  It does not
contradict the TU marginal projection (5.2): the latter forgets which two
incidences must form one allowed turn.

The same distinction explains the matroid boundary.  After choosing a
bipartite orientation, endpoint matching is the intersection of the two
endpoint partition constraints; an exact upper rainbow condition supplies
another partition constraint, and lower restoration colours the selected
pairs once more.  Ordinary two-matroid intersection does not cover this
unrestricted system.  Nor is it ordinary matroid parity: alternative pairs
at one upper colour overlap in their incidence elements rather than forming
fixed disjoint parity blocks.  No theorem here rules out every possible
extended gadget formulation.

## 8. Separation and the remaining gate

The rows (1.2), (1.3), and (3.1)--(3.3) have polynomial enumeration, so the
displayed linear relaxation has a trivial polynomial row oracle.  This does
not imply integrality.

For fixed `H`:

* the marginal Hall system has a max-flow/min-cut oracle;
* ordinary matching blossom rows for the union of compatible seam graphs
  have polynomial odd-cut separation, but upper-colour and lower-cover rows
  destroy that matching polytope's integrality in general;
* the locally matroidal, pre-serviced system has the polynomial
  matroid-intersection certificate (6.3); and
* no polynomial separation oracle is proved for the unrestricted integer
  hull (4.4)--(4.6).

Thus the sharp remaining physical `B_0` question is finite and structural:

1. choose a four-separated physical transversal of all `1,425` collars;
2. reserve disjoint portals for the vanished lower colours; and
3. prove that the remaining `K_U` are jointly completable, either by the
   Hall condition (5.3), the matroidal condition (6.3), or a stronger
   non-TU argument.

In the `Z_15`-equivariant sublane, the first step becomes a transversal of
the `95` quotient collar orbits **plus** the physical four-separation rows.
The existing size-`60` quotient witness solves only the bare collar
transversal: it is not four-separated, and the width-three DP that produced
it did not impose (1.3).  Its statement that at least twelve lower-colour
orbits are lost is therefore a necessary bare-transversal frontier, not an
attained minimum for the separated endpoint gate.  It still shows that
lower-colour service is material, but existence and minimum size of an
equivariant four-separated cut remain open.
