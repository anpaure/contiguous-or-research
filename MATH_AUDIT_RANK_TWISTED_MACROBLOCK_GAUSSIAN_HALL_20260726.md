# Rank-twisted macroblocks: exact compatibility census and the unresolved Gaussian Hall overlap

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Verdict

The owner theorem in
MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md
is correct.  The rank-dependent local status cells are disjoint, their
products partition the middle layer, subdivision of every \(Q_S\) with
\(S\ge r\) gives disjoint physical \(Q_r\) packets, and the leave is

\[
                         2^{m+o(m)}.                  \tag{0.1}
\]

Every retained axis crosses the two halves of one macroblock.  Two scope
qualifications are necessary.

1. A packet has one frozen local-rank vector and therefore one frozen
   product matching.  Frame motion occurs between packets, not during a
   path inside one packet.
2. After a \(Q_S\) cell is subdivided, only the chosen \(r\) axes are
   available.  After a cycle factor is installed, only one chronological
   \(q\)-window is assigned to each owner.  The theorem does not specify
   either choice, so it does not yet determine a literal target Hall
   graph.

The maximal graph obtained by allowing every split source edge can be
analyzed exactly.  Let \(N=d\lfloor m/d\rfloor\) be the number of
nonresidual matched pairs and let \(\rho=2m-2N<2d\).  If \(S(X)\) is the
number of split edges in the rank-selected product matching of a source
\(X\), then

\[
 \boxed{
 \sum_X x^{|X|}y^{S(X)}
 =(1+x)^\rho(1+2xy+x^2)^N.}                           \tag{0.2}
\]

Thus rank twisting changes literal incidences but not the joint
rank/split census.  In the maximal lower depth-\(q\) compatibility graph,
a source \(X\) has degree exactly

\[
                         \binom{S(X)}q,                \tag{0.3}
\]

and the total number of source--target edges is

\[
 \boxed{
 E_q^*
 =2^q\binom Nq\binom{2m-2q}{m-q}.}                    \tag{0.4}
\]

Consequently the average target/source degree ratio is exactly

\[
 \boxed{
 {\overline d_T\over\overline d_X}
 ={W\over N_q},\qquad
 W=\binom{2m}m,\quad N_q=\binom{2m}{m-q}.}             \tag{0.5}
\]

This average surplus is not a Hall theorem.

More sharply, freeze one allocation vector
\(\boldsymbol\ell=(\ell_1,\ldots,\ell_b)\).  Relative to the resulting
source-rank product matching, let a lower target have \(e_j\) empty and
\(u_j\) split edges in block \(j\).  The allocation-resolved
source/target ratio is exactly

\[
 \boxed{
 R_{\boldsymbol\ell}(\mathbf e,\mathbf u)
 =2^q\prod_j
 {\binom{e_j}{\ell_j}\over
  \binom{u_j+\ell_j}{\ell_j}},
 \qquad\sum_j\ell_j=q.}                               \tag{0.6}
\]

This fixed-allocation kernel can be strongly deficient.  For example,
if \(\ell_j=1\) on \(q\) blocks and zero elsewhere, and those blocks have
the exact central statuses \(e_j=d/4,u_j=d/2\), then

\[
 \boxed{
 \log R_{\boldsymbol\ell}
 =q\log{d/2\over d/2+1}
 =-(2+o(1)){q\over d}.}                               \tag{0.7}
\]

At \(q=A\sqrt m\), \(d=\Theta(\log m)\), this tends to
\(-\infty\).  This is a deficit of a decorated allocation slice, not yet
a raw Hall cut.  The rank twist can succeed only because one raw target
can be offered to many different source-rank allocations and therefore
many different product matchings.  The allocation overlap is not a
lower-order detail; it is the only possible repair of (0.7).

The exact raw compatible-source count for a target is given by the
cross-correlation coefficients (5.2) and (5.4) below.  It is an upper envelope
for every selected-axis packet tiling.  No argument presently converts
its large value into Hall expansion, because the same source capacity is
shared by many targets and many allocations.  Thus:

* the deterministic owner gate and cross-half toll are certified;
* potential reachability and total average capacity are certified;
* a fixed allocation is Gaussian-deficient;
* the global allocation-overlap Hall inequality remains open.

## 1. Independent audit of the owner partition

Write one macroblock as

\[
 B=A\mathbin{\dot\cup}C,\qquad |A|=|C|=d.
\]

For every local rank \(k\), the matching \(M_k\) is fixed on the entire
rank-\(k\) layer.  Fixing the empty and full statuses on \(M_k\) and
allowing all split-edge orientations gives disjoint orientation cubes
partitioning \(\binom Bk\).  A cube move preserves rank, so it cannot
change \(M_k\).  Different ranks are disjoint.  This proves the local
partition without requiring compatibility between \(M_k\) and
\(M_{k'}\).

Tensoring the local partitions and recording each residual-coordinate
pattern partitions the whole Boolean lattice.  Restriction to rank \(m\)
and subdivision of every \(Q_S\), \(S\ge r\), preserve disjointness.

For the leave estimate fix a complete local-rank vector.  It fixes a
matching with \(N\) edges.  The number of subsets having exactly \(s\)
split edges is

\[
                         2^N\binom Ns.                 \tag{1.1}
\]

Therefore the number with fewer than \(r=o(m)\) split edges is
\(2^{m+o(m)}\).  There are

\[
 (2d+1)^{\lfloor m/d\rfloor}
 =\exp\left(O\left({m\log d\over d}\right)\right)
 =2^{o(m)}                                             \tag{1.2}
\]

rank vectors, and the residual coordinates contribute \(2^{O(d)}\).
Under \(d\to\infty\), \(d=m^{o(1)}\), these factors preserve
\(2^{m+o(m)}\).  The residual factor is subexponential in general and
polynomial only when \(d=O(\log m)\).

Every active edge belongs to one \(M_{j,k}\subseteq A_j\times C_j\).
Thus all selected packet axes cross halves.  The assertion that a
length-\(q\) window uses exactly \(q\) such axes additionally requires
an isometric or return-free compiler and \(q\le r\).

## 2. Three different compatibility graphs

It is important not to identify the following graphs.

### 2.1 Maximal exposed-edge graph

A lower target \(T\) is adjacent to a middle source \(X\) when

* \(T\subset X\);
* \(X\setminus T\) has size \(q\); and
* every element of \(X\setminus T\) is the occupied endpoint of a
  distinct split edge in the product matching selected by the local
  ranks of \(X\).

This graph allows all split edges of the original \(Q_S\) cell.

### 2.2 Selected-axis packet graph

For each product status cell, choose only \(r\) of its \(S\) active
axes and freeze the others.  The target must use axes among this selected
set.  This graph is a subgraph of the maximal graph and depends on the
axis selector.

### 2.3 Literal factor graph

After a cycle factor and direction labeling are installed, every owner
has one directed trace at each sign and depth.  This is a further
subgraph of the selected-axis graph.

The rank-twisted tiling theorem specifies only the owner partition.  It
does not specify the last two graphs.  Therefore an exact literal Hall
ratio cannot be inferred from the tiling theorem alone.  Sections 3--6
analyze the maximal graph and the frozen-frame kernels which every later
selection must respect.

## 3. Exact local incidence kernel

Fix a lower target \(T\) in one macroblock, let

\[
                         t=|T|,\qquad \ell\ge0,
\]

and put \(k=t+\ell\).  The relevant source frame is \(M_k\).  A compatible
source is obtained by choosing \(\ell\) edges of \(M_k\) which are empty
in \(T\), and choosing one of their two endpoints.

Summed over all \(t\)-sets \(T\), the number of compatible pairs is

\[
 \boxed{
 I_d(t,\ell)
 =2^\ell\binom d\ell\binom{2d-2\ell}{t}.}             \tag{3.1}
\]

Indeed choose the \(\ell\) used matching edges, orient their source
endpoints, and choose the \(t\) target elements arbitrarily from the
remaining \(2d-2\ell\) coordinates.

Hence the exact average degrees on the two rank layers are

\[
 \overline d_T(t,\ell)
 ={I_d(t,\ell)\over\binom{2d}t},
\qquad
 \overline d_X(t,\ell)
 ={I_d(t,\ell)\over\binom{2d}{t+\ell}},               \tag{3.2}
\]

and their ratio is

\[
 {\overline d_T(t,\ell)\over\overline d_X(t,\ell)}
 ={\binom{2d}{t+\ell}\over\binom{2d}t}.               \tag{3.3}
\]

This layer-average ratio is not a literal Hall ratio because degrees
inside a layer vary, and different allocation vectors overlap on raw
targets and sources.

There is also an exact status refinement.  Relative to \(M_k\), suppose
a target has \(e\) empty, \(u\) split, and \(f\) full edges.  Completing
\(\ell\) empty edges produces a source with statuses

\[
                         (e-\ell,u+\ell,f).            \tag{3.4}
\]

The target degree inside this profile is

\[
                         2^\ell\binom e\ell,           \tag{3.5}
\]

while the source degree back to the profile is

\[
                         \binom{u+\ell}{\ell}.         \tag{3.6}
\]

Thus the exact source/target family ratio is

\[
 \boxed{
 R_\ell(e,u)
 ={2^\ell\binom e\ell\over\binom{u+\ell}{\ell}}.}     \tag{3.7}
\]

For a global fixed allocation
\(\boldsymbol\ell=(\ell_1,\ldots,\ell_b)\), the product-status ratio is

\[
 \boxed{
 R_{\boldsymbol\ell}(\mathbf e,\mathbf u)
 =2^q\prod_{j=1}^b
   {\binom{e_j}{\ell_j}\over
    \binom{u_j+\ell_j}{\ell_j}},
 \qquad \sum_j\ell_j=q.}                              \tag{3.8}
\]

Equations (3.1)--(3.8) are exact and do not use potential-path
heuristics.

## 4. The rank/split census is unchanged by twisting

For one block and one fixed local rank \(k\), the number of \(k\)-sets
having \(s\) split edges relative to \(M_k\) is independent of the
identity of \(M_k\).  It is the coefficient of \(x^ky^s\) in

\[
                         (1+2xy+x^2)^d.
\]

Although a different matching is used at another rank, summing over the
disjoint rank layers therefore gives the same polynomial.  Tensoring the
blocks and adjoining the residual singleton coordinates proves (0.2).

Extracting coefficients gives the exact middle-source census

\[
 \boxed{
 A_{m,s}
 =2^s\binom Ns
  [x^{m-s}](1+x)^\rho(1+x^2)^{N-s}.}                 \tag{4.1}
\]

In the maximal graph, a source with \(S(X)=s\) chooses any \(q\) of its
split edges, and distinct choices give distinct lower targets.  This
proves (0.3).  Summing (0.3) by differentiating (0.2) in \(y\) yields

\[
\begin{aligned}
 E_q^*
 &= [x^m]\frac1{q!}
    \left.\frac{\partial^q}{\partial y^q}
    (1+x)^\rho(1+2xy+x^2)^N\right|_{y=1}\\
 &=2^q\binom Nq[x^{m-q}](1+x)^{2m-2q}\\
 &=2^q\binom Nq\binom{2m-2q}{m-q},
\end{aligned}                                         \tag{4.2}
\]

which proves (0.4).

Since the two vertex classes have sizes \(W\) and \(N_q\), double
counting (4.2) proves (0.5).  In particular, neither the enormous total
incidence count nor the average surplus \(W/N_q\) proves Hall expansion.

## 5. Exact target-side cross-correlation formula

In one cyclic macroblock write

\[
 x_i(T)=\mathbf1_{\{a_i\in T\}},
 \qquad
 y_i(T)=\mathbf1_{\{c_i\in T\}}.
\]

For shift \(s\), put

\[
 e_s(T)=
 \sum_{i\in\mathbb Z_d}
 (1-x_i(T))(1-y_{i+s}(T)).                            \tag{5.1}
\]

This is the number of empty edges of \(M_s\).  If
\(T_j=T\cap B_j\), \(t_j=|T_j|\), and
\(\boldsymbol\ell\) assigns \(\ell_j\) additions to block \(j\), then
the source frame in that block is \(M_{t_j+\ell_j}\).  Therefore the
number of raw compatible sources of a lower target is exactly

\[
 \boxed{
 C_q^-(T)
 =2^q
 \sum_{\substack{\ell_1+\cdots+\ell_b=q\\\ell_j\ge0}}
 \prod_{j=1}^b
 \binom{e_{t_j+\ell_j}(T_j)}{\ell_j}.}                \tag{5.2}
\]

This is zero in an allocation precisely when
\(\ell_j>e_{t_j+\ell_j}(T_j)\) for some \(j\).

For an upper target \(U\), let

\[
 f_s(U)=
 \sum_{i\in\mathbb Z_d}
 x_i(U)y_{i+s}(U).                                    \tag{5.3}
\]

If \(u_j=|U\cap B_j|\), complementation gives

\[
 \boxed{
 C_q^+(U)
 =2^q
 \sum_{\substack{\ell_1+\cdots+\ell_b=q\\\ell_j\ge0}}
 \prod_{j=1}^b
 \binom{f_{u_j-\ell_j}(U_j)}{\ell_j}.}                \tag{5.4}
\]

These are exact compatible-source counts in the maximal graph.  They
already quotient duplicate paths: a source--target pair uniquely
determines the removed elements and hence \(\boldsymbol\ell\).

The cyclic identities

\[
 \sum_{s\in\mathbb Z_d} f_s(T)
 =|T\cap A|\,|T\cap C|,
\qquad
 \sum_{s\in\mathbb Z_d} e_s(T)
 =(d-|T\cap A|)(d-|T\cap C|)                         \tag{5.5}
\]

show why potential reachability is abundant.  They do not control the
particular allocation-dependent shifts in (5.2), and they give no
source-disjoint matching.

## 6. The fixed-allocation deficit and why it is not a raw cut

Fix an allocation
\(\boldsymbol\ell=(\ell_1,\ldots,\ell_b)\).  In block \(j\), the target
rank \(t_j\) and allocation \(\ell_j\) determine the source rank
\(k_j=t_j+\ell_j\), and hence determine the frame \(M_{j,k_j}\).
Relative to that frame, completing \(\ell_j\) empty target edges changes
the local statuses

\[
 (e_j,u_j,f_j)
 \longmapsto
 (e_j-\ell_j,u_j+\ell_j,f_j).
\]

The target-side degree is
\(2^{\ell_j}\binom{e_j}{\ell_j}\), while the source-side degree is
\(\binom{u_j+\ell_j}{\ell_j}\).  Multiplication over blocks proves
(0.6).

For the collision-free allocation in (0.7), every active block
contributes

\[
 {2e_j\over u_j+1}
 ={d/2\over d/2+1}.
\]

This proves (0.7).  More general allocation profiles retain the exact
product (0.6); collisions and local-rank deviations must not be erased
before taking the product.

It would be incorrect to replace (0.6) by the global fixed-matching
ratio

\[
 {2^q\binom Eq\over\binom{U+q}q}
\]

without recording the allocation.  Choosing which empty edges are
completed changes the local source-rank vector, and in the rank-twisted
atlas that changes the product matching itself.  The global ratio is
valid for one matching fixed independently of all local ranks, but not
for one rank-twisted stratum.

The deficit (0.7) therefore lives on decorated copies
\((T,\boldsymbol\ell)\).  One raw target \(T\) has many possible
allocations in (5.2), and the associated source rank vectors are
different.  Adding the fixed-allocation deficits would count \(T\)
multiple times.  Proving that their source neighborhoods still fail to
expand would yield a raw obstruction; proving that their union expands
would be the desired repair.

## 7. Coarse rank profiles do not settle literal Hall

Let a macro-rank vector be
\(\mathbf t=(t_1,\ldots,t_b)\).  Ignoring matching statuses, its weight is

\[
                         w(\mathbf t)=\prod_j\binom{2d}{t_j}.  \tag{7.1}
\]

The ordinary inclusion graph from rank \(m-q\) to rank \(m\) has target
degree \(\binom{m+q}q\) and source degree \(\binom mq\).  Therefore every
family of targets, and in particular every union of macro-rank fibers,
has ordinary-inclusion neighborhood at least

\[
 {\binom{m+q}q\over\binom mq}|{\cal A}|
 ={W\over N_q}|{\cal A}|.                             \tag{7.2}
\]

Thus the weighted product-of-rank-chains quotient has no capacity
deficit.  But (7.2) counts all inclusions.  The exposed-edge condition
deletes most of them, and the selected-axis and chronological graphs
delete still more.  Hence (7.2) is only a proof that macro-rank occupancy
alone is not the desired obstruction.

## 8. Exact Hall gate left by the audit

For a raw lower-target family
\({\cal A}\subseteq\binom{[2m]}{m-q}\), define

\[
 \Gamma^*({\cal A})
 =\{X: X\text{ is counted in }C_q^-(T)
          \text{ for some }T\in{\cal A}\}.            \tag{8.1}
\]

The maximal compatibility graph satisfies Hall exactly when

\[
                         |\Gamma^*({\cal A})|
 \ge|{\cal A}|\qquad\text{for every }{\cal A}.         \tag{8.2}
\]

Equations (3.8) and (5.2) give a complete finite description of this
inequality.  They show two competing facts:

1. every fixed allocation/status slice can have the strong deficit
   (0.7);
2. one raw target participates in many allocation slices, whose source
   rank vectors and product matchings differ.

The missing theorem is an overlap inequality proving that the union in
(8.1) recovers the fixed-slice deficits without reusing sources.  Neither
the total incidence identity (4.2), the cyclic averages (5.5), nor
potential reachability implies this.

Even a proof of (8.2) would not finish CPM.  For each product status cell
one must additionally specify

* the selected \(r\)-subset of its \(S\) active axes;
* the subdivision orientations; and
* one common compiler direction labeling,

and then prove Hall after these deletions.  Conversely, a violation of
(8.2) would be a decisive obstruction to every such selection.

## 9. Certified boundary

Proved:

1. the owner near-tiling and its \(2^{m+o(m)}\) leave;
2. maximal cross-half density of all retained packet axes;
3. the exact local incidence and profile ratios (3.1)--(3.8);
4. the exact rank/split generating function (0.2);
5. the exact total maximal compatibility mass (0.4);
6. the literal target cross-correlation formulae (5.2), (5.4); and
7. the exact fixed-allocation deficit (0.7).

Not proved:

1. Hall expansion of the allocation-overlap graph (8.2);
2. preservation of that expansion by a deterministic \(r\)-axis
   selector; or
3. simultaneous chronological lower/upper coverage.

The rank twist therefore passes the owner and potential-support audits,
but not yet the source-capacity audit.  Its only possible Gaussian repair
is a genuinely quantitative allocation-overlap theorem.
