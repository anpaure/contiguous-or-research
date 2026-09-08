# Protected width-two multicovers: line-colouring obstruction

Date: 2026-07-25

Pure mathematics only.  No computation, web input, or black-box colouring
theorem is used.

## 0. Verdict

The presently proved properties of the protected width-two-pruned rational
multicover do **not** imply a \((1+o(1))D\) edge-colouring after denominators
are cleared.

There are two logically separate gaps.

1. The fractional-overload theorem bounds only

   \[
    \sum_v(\ell(v)-1)_+=o(W).                        \tag{0.1}
   \]

   It does not give \(\max_v\ell(v)=1+o(1)\).  A single target of load two
   costs only one unit in (0.1), but already forces at least \(2D\) colors.
   This preliminary defect can be repaired by declaring \(o(W)\) highly
   overloaded targets exceptional; that repair does not affect the second
   obstruction.

2. Even granting the stronger pointwise bound \(\ell(v)\le1+o(1)\), tag
   and target capacities are only star-clique inequalities of the line
   graph.  The width-two condition does not make that line graph perfect.
   Three legal return-free geodesic path bundles can meet pairwise in
   three different singleton targets.  Half the mass of each of three tag
   fibres may be put on the corresponding bundle and half on disjoint
   fillers.  This satisfies every tag and target capacity exactly.  After
   denominator clearing, the three bundles contribute a clique of size
   \(3D/2\).  The construction may be atomized to path weights
   \(1/\mu=m^{-5/2+o(1)}\).

Thus fibre switches cannot produce fewer than \(3D/2\) colors in this
legal width-one example.  The obstruction is a loose triangle, not a
large common rectangle.

This does not prove that the particular uniform point produced by the
isolated-pruning theorem has chromatic ratio \(3/2\).  It proves that its
recorded degree, overload, width-two, and chronology properties are
insufficient.  To establish \((1+o(1))D\) coloring for that point one must
add a global packing-cut theorem excluding weighted loose odd systems.

## 1. Clearing denominators and the exact line-graph question

Let \(\mathcal I=\bigcup_U\mathcal I_U\) be the retained protected path
catalogue and let \(x_P\in\mathbb Q_{\ge0}\) satisfy

\[
 \sum_{P\in\mathcal I_U}x_P=1                       \tag{1.1}
\]

for every retained tag \(U\).  Choose a common denominator \(D\) and put

\[
 m_P=Dx_P\in\mathbb Z_{\ge0}.                        \tag{1.2}
\]

Make \(m_P\) labelled copies of the hyperedge consisting of the tag of
\(P\) and all protected targets claimed by \(P\).  Call the resulting
multihypergraph \(\mathcal H_D\).  Its tag degrees are exactly

\[
 d_{\mathcal H_D}(U)=D,                              \tag{1.3}
\]

and its target degrees are

\[
 d_{\mathcal H_D}(v)=D\ell(v),
 \qquad
 \ell(v)=\sum_{P\ni v}x_P.                          \tag{1.4}
\]

Let \(L\) be the conflict graph on path types: two vertices are adjacent
when the paths have the same tag or share a protected target.  An
edge-colouring of \(\mathcal H_D\) is exactly a colouring of the weighted
blow-up of \(L\).

The relevant fractional parameter is

\[
 \chi_f(L,x)
 =\min\left\{
   \sum_{M}y_M:
   y_M\ge0,
   \sum_{M\ni P}y_M\ge x_P\quad(P\in\mathcal I)
  \right\},                                         \tag{1.5}
\]

where \(M\) ranges over independent sets of \(L\), equivalently matchings
of protected paths.

Every tag fibre is a clique of total \(x\)-mass one, so

\[
 \chi_f(L,x)\ge1.                                    \tag{1.6}
\]

Conversely, after allowing an arbitrary further common replication of
the denominator, the rational linear program (1.5) decomposes the copies
into

\[
 (\chi_f(L,x)+o(1))D                                 \tag{1.7}
\]

matchings.  Hence the asymptotic colouring question is precisely

\[
 \boxed{\chi_f(L,x)=1+o(1).}                         \tag{1.8}
\]

Target capacities prove (1.8) only when all non-star matching-polytope
cuts are redundant.  Width-two intersections do not give that
redundancy.

## 2. Fibre switches do not change the obstruction

A fibre switch permutes colors among the \(D\) copies above one tag.  It
preserves:

* the weighted point \(x\);
* every target degree;
* the conflict graph \(L\); and
* every independent-set inequality in (1.5).

Thus fibre switches are useful for constructing a colouring after (1.8)
is known, but cannot decrease \(\chi_f(L,x)\).  In particular they cannot
repair an odd-system or clique cut which already exceeds one.

## 3. Legal loose triangles exist in the protected catalogue

### Lemma 3.1 (loose geodesic triangle)

For all sufficiently large \(m\), the return-free protected geodesic
catalogue contains paths \(P_1,P_2,P_3\) on distinct tags and distinct
protected owner targets \(v_{12},v_{23},v_{31}\) such that

\[
 \mathcal S_Q(P_i)\cap\mathcal S_Q(P_j)
 =\{v_{ij}\}\qquad(1\le i<j\le3),                   \tag{3.1}
\]

and there is no target common to all three paths.  Each intersection has
width one.

#### Proof

Put

\[
 s=g-2Q=\ell-1.
 \tag{3.2}
\]

Thus \(s>2Q\) and \(s=o(m)\).  Take pairwise disjoint blocks

\[
 |E_0|=|E_1|=|E_2|=s,
 \qquad |S|=m-2s,
 \tag{3.3}
\]

and define three middle owners

\[
 A=S\dot\cup E_0\dot\cup E_1,
 \quad B=S\dot\cup E_1\dot\cup E_2,
 \quad C=S\dot\cup E_2\dot\cup E_0.
 \tag{3.4}
\]

Their pairwise Johnson distances are all \(s\).  Use the following three
chronological core segments:

\[
  \begin{array}{c|c|c|c}
  \text{path}&\text{time }Q&\text{time }Q+s
     &\text{core exchanges}\\
  \hline
  P_1&A&C&E_1\longrightarrow E_2\\
  P_2&A&B&E_0\longrightarrow E_2\\
  P_3&B&C&E_1\longrightarrow E_0.
 \end{array}
 \tag{3.5}
\]

If \(D=(d_1,\ldots,d_s)\) is the departure order, \(E=(e_1,\ldots,e_s)\)
the arrival order, and \(T\) the persistent block, the owner at core time
\(k\) is exactly

\[
 X_k=T\cup\{d_{k+1},\ldots,d_s\}
          \cup\{e_1,\ldots,e_k\}.
 \tag{3.6}
\]

The three persistent blocks in (3.5) are respectively
\(S\cup E_0,S\cup E_1,S\cup E_2\).  Comparing their three block
coordinates in (3.6) shows, without a count or genericity argument, that

\[
 P_1\cap P_2=\{A\},\qquad
 P_2\cap P_3=\{B\},\qquad
 P_3\cap P_1=\{C\}
 \tag{3.7}
\]

on the owner row.  For example, equality between a \(P_1\)-owner and a
\(P_2\)-owner would require both the \(E_0\)- and \(E_1\)-coordinates to
be full, forcing both times to be zero.

It remains to audit the signed rows.  For \(q\le Q\), away from an end of
the core segment, (3.6) gives the exact identities

\[
 \begin{aligned}
 L_q(k)&=T\cup\{d_{k+q+1},\ldots,d_s\}
                 \cup\{e_1,\ldots,e_k\},\\
 U_q(k)&=T\cup\{d_{k-q+1},\ldots,d_s\}
                 \cup\{e_1,\ldots,e_k\}.
 \end{aligned}
 \tag{3.8}
\]

The same block comparison rules out every lower--lower equality between
two paths.  It rules out every upper--upper equality except the following
three boundary comparisons:

\[
 \begin{array}{c|c}
  (P_1,P_2) & \text{the first \(q\) arrivals in their two orders on }E_2,\\
  (P_1,P_3) & \text{the last \(q\) departures in their two orders on }E_1,\\
  (P_2,P_3) & \text{the last \(q\) departures of \(P_2\) on \(E_0\)
               versus the first \(q\) arrivals of \(P_3\) on \(E_0\).
 \end{array}
 \tag{3.9}
\]

Choose the two \(E_2\) arrival orders and the two \(E_1\) departure
orders to be different cyclic shifts.  Distinct cyclic shifts of an
\(s\)-term order have different proper prefix sets and different proper
suffix sets.  Choose the last \(Q\) terms of the \(P_2\) departure order
on \(E_0\) disjoint from the first \(Q\) terms of the \(P_3\) arrival
order; this is possible because \(s>2Q\).  Hence none of the comparisons
in (3.9) is an equality.

Finally prepend and append \(Q\) exchanges to each core, using mutually
disjoint exterior labels.  In the prefix, arrive through a private
\(Q\)-subset of \(S\); in the suffix, depart through another private
\(Q\)-subset of \(S\).  The six subsets may be disjoint because
\(|S|=m-2s\gg Q\).  A protected upper flag which crosses the first core
boundary contains a private prepended departure label.  A protected lower
flag which crosses the second boundary omits the corresponding private
suffix subset.  Thus the boundary extensions create no equality omitted
from (3.8)--(3.9).

Each full path now has \(g\) distinct departures and \(g\) distinct
arrivals.  Its union has size \(m+g\le m+H\), so it lies in a carrier;
pad to size \(m+H\), and use three distinct labelled carrier-copy tags.
Proposition 3.1 of the geodesic catalogue then realizes each sequence as
a legal radius-\(Q\) return-free rotor path.  Equations (3.7)--(3.9) give
(3.1), with

\[
 v_{12}=A,\qquad v_{23}=B,\qquad v_{31}=C.
 \tag{3.10}
\]

\(\square\)

The construction uses only singleton intersections, so it survives the
three-antichain pruning and every stronger rule which merely forbids a
shared nontrivial product rectangle.

There are also legal filler cores \(F_i\) on the tag of \(P_i\) whose
protected targets avoid the three triangle strips and the earlier filler
cores.  Indeed,
for a fixed rank-\(r\) target in a carrier, transitivity bounds the fraction
of geodesic supports claiming it by

\[
 {\ell\over\binom{m+H}{r}}.
 \tag{3.11}
\]

At each sequential choice there are only \(O(gQ)\) forbidden targets, and
\(r\in[m-Q,m+Q]\).  The union bound from (3.11) is \(o(1)\), so a filler
exists in the same carrier-copy fibre.  This also supplies a literal
finite-avoidance proof instead of an appeal to genericity.

The core orders themselves give arbitrarily fine atomization, without
counting hidden rotor decorations or unclaimed future-buffer states.  Keep
all the boundary pieces used in (3.9) fixed.  On each path there remains
an exchange order with only its first or its last \(Q\) positions fixed,
and hence at least

\[
 (s-Q)!
 \tag{3.12}
\]

different simple protected supports.  The block comparison leading to
(3.9) depends only on the fixed boundary pieces, so it holds for every
pair of variants.  In the calibrated regime,
\((s-Q)!>m^{5/2-o(1)}\).

## 4. A capacity-perfect multicover needing \(3D/2\) colors

The six-path version puts

\[
 x_{P_i}=x_{F_i}={1\over2}\qquad(i=1,2,3).          \tag{4.1}
\]

Every tag has total weight one.  Each shared target \(v_{ij}\) has load

\[
 x_{P_i}+x_{P_j}=1,                                  \tag{4.2}
\]

and every other target has load at most \(1/2\).  Thus this rational
multicover has zero target overload and maximum target load one.  All
paths are legal rotor paths, and every cross-tag intersection has width at
most one.

Nevertheless \(P_1,P_2,P_3\) form a triangle in the line graph.  Any
independent set contains at most one of them, so summing their three
covering inequalities in (1.5) gives

\[
 \chi_f(L,x)\ge {3\over2}.                           \tag{4.3}
\]

Equivalently, take \(D\) even.  There are \(D/2\) copies of each \(P_i\).
Copies of one type meet through their common tag, and copies of different
types meet through \(v_{ij}\).  Hence all \(3D/2\) copies form one clique:

\[
 \boxed{\chi'(\mathcal H_D)\ge3D/2.}                 \tag{4.4}
\]

No fibre switch changes this clique.

More pertinently, let \(\mu\) be any even integer with
\(\mu\le (s-Q)!\), in particular

\[
 \mu=m^{5/2-o(1)}.
 \tag{4.5}
\]

Above tag \(i\), take \(\mu/2\) distinct core-order variants
\(\mathcal P_i\) of the triangle core \(P_i\), and \(\mu/2\) legal filler
paths \(\mathcal F_i\).  (Here “variants” means the visible core-order
variants of (3.12), not buffer decoration.)  Give every path weight
\(1/\mu\).
All paths in \(\mathcal P_1\cup\mathcal P_2\) share \(A\), all paths in
\(\mathcal P_2\cup\mathcal P_3\) share \(B\), and all paths in
\(\mathcal P_3\cup\mathcal P_1\) share \(C\).  Apart from those anchors,
different triangle bundles have disjoint protected targets.

The full triangle bundles expose only
\(O(\mu gQ)=m^{O(1)}\) targets.  Applying (3.11) to that whole forbidden
set, and then sequentially to the earlier filler families, chooses
\(\mu/2\) fillers on each tag so that fillers on different tags meet
neither each other nor a triangle bundle.  Intersections inside one tag
are harmless: their total filler mass is only \(1/2\).  The forbidden
fraction is still \(o(1)\), since the denominator in (3.11) is
exponential in \(m\).

Every anchor therefore has load one.  Every other target is confined to
one triangle bundle or to one tag's filler family, whose total mass is
\(1/2\).  Thus this atomized multicover still has zero overload and
maximum target load one.  If \(D\) is divisible by \(\mu\), the copies
belonging to the three triangle bundles form a clique of cardinality

\[
 {3\mu\over2}{D\over\mu}={3D\over2}.
 \tag{4.6}
\]

Hence neither diffuse atoms of the isolated-pruning scale nor polynomial
fibre entropy removes the obstruction.

## 5. The general packing-cut obstruction

For every path subfamily \(\mathcal F\), let \(\nu(\mathcal F)\) be the
maximum number of pairwise nonconflicting paths in \(\mathcal F\).  Every
colour contains at most \(\nu(\mathcal F)\) members of \(\mathcal F\).
Therefore a necessary condition for \((1+\epsilon)D\) colors is

\[
 \boxed{
 x(\mathcal F)
 \le(1+\epsilon)\nu(\mathcal F)
 \qquad\hbox{for every }\mathcal F.}                 \tag{5.1}
\]

For a pairwise-intersecting family, \(\nu(\mathcal F)=1\), so (5.1)
reduces to the non-star clique inequality

\[
 x(\mathcal F)\le1+\epsilon.                        \tag{5.2}
\]

The triangle in Section 4 has \(x(\mathcal F)=3/2\).

Tag and target capacities imply only the special cases in which
\(\mathcal F\) is covered by one tag or one target.  For an arbitrary
rank-\(K\) protected system, take a maximal matching in \(\mathcal F\).
The union of its tag and target vertices has size at most
\((K+1)\nu(\mathcal F)\) and meets every edge of \(\mathcal F\).  Vertex
capacities consequently give only

\[
 x(\mathcal F)\le(K+1)\nu(\mathcal F),              \tag{5.3}
\]

which is the wrong factor.  Linear set systems, in which every two edges
meet in at most one target, already exhibit this gap.  Therefore the
statement that protected intersections are unions of at most two chains
does not improve (5.3) by itself.

## 6. What the isolated-pruning point still needs

The particular point constructed in
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md` is much more
diffuse than the six-path presentation (4.1): each retained path above a
good tag has weight roughly

\[
 \tau={1\over\mu}=m^{-5/2+o(1)},                     \tag{6.1}
\]

whereas \(K=m^{1+o(1)}\).  One fixed loose triangle in that point has only
\(O(\tau)\) mass and is harmless.  Section 4 shows, however, that the same
atom size is compatible with a mass-\(3/2\) loose-triangle bundle.  The
protected width-two exponential census is rooted at one path and counts
nonlinear overlap shapes; singleton intersections contribute zero after
the linear term is subtracted.  It therefore does not bound
\(x(\mathcal F)/\nu(\mathcal F)\) for a whole subfamily.

Define the packing-cut excess

\[
 \Omega(x)
 =\sup_{\mathcal F}
  \left({x(\mathcal F)\over\nu(\mathcal F)}-1\right)_+.
 \tag{6.2}
\]

Then

\[
 \boxed{
 (1+o(1))D\hbox{-colourability requires }\Omega(x)=o(1).} \tag{6.3}
\]

This unweighted excess is only a necessary diagnostic.  The exact weighted
excess is

\[
 \Omega_*(x)
 =\sup_{y\ge0}
  \left(
   {\sum_Px_Py_P\over
    \max_{M\text{ matching}}\sum_{P\in M}y_P}-1
  \right)_+
 =\chi_f(L,x)-1.
 \tag{6.4}
\]

Consequently near-\(D\) colourability after rational replication is
equivalent to \(\Omega_*(x)=o(1)\), not merely to \(\Omega(x)=o(1)\).

The present pruning and fractional-overload results prove neither (6.3)
nor the stronger weighted identity \(\Omega_*(x)=o(1)\).

There is also the preliminary maximum-degree requirement

\[
 \max_v\ell(v)=1+o(1),                               \tag{6.5}
\]

which is stronger than the aggregate overload estimate (0.1).

## 7. Explicit unconditional colouring bounds

Assume for this paragraph that every protected path claims at most \(K\)
targets and that all tag and target degrees are at most \(\Delta\).  An
edge has at most

\[
 (K+1)(\Delta-1)                                    \tag{7.1}
\]

neighbours in the line graph, counting a neighbour once for each shared
vertex only enlarging the value.  Greedy colouring therefore gives

\[
 \boxed{
 \Delta\le\chi'(\mathcal H)
 \le (K+1)(\Delta-1)+1.}                            \tag{7.2}
\]

The lower end cannot be improved to \((1+o(1))\Delta\) from width two
alone, by (4.4).  A colour nibble would need, in addition to the existing
shape census, a quantitative packing-cut hypothesis such as

\[
 x(\mathcal F)\le(1+\epsilon_K)\nu(\mathcal F)
 \quad\hbox{for all }\mathcal F,
 \qquad \epsilon_K=o(1),                             \tag{7.3}
\]

plus pointwise degree concentration.  Condition (7.3) is not a consequence
of any currently proved \(K\)-dependent overlap bound.

## 8. Final status

The line-colouring route has an exact new gate:

\[
 \boxed{\chi_f(L,x)=1+o(1),}                         \tag{8.1}
\]

or equivalently the weighted matching inequalities in (6.4).  The
protected width-two and legal-rotor properties do not imply this gate.  A
legal loose triangle gives a coefficient \(3/2\) counterexample even with
zero target overload.

For the particular diffuse isolated-pruning point, (8.1) remains open; it
is neither proved nor disproved by the legal triangle bundle.  Thus no
\((1+o(1))D\) coloring theorem, and hence no coefficient-one extraction,
currently follows from the protected rational multicover.
