# Lane K: the PBBS plane-tree action, rerooting no-go, and the exact saddle charge left open

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, or web
search is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad \tau=\phi^2.
\]

Under the ordinary contour bijection between Dyck words and rooted ordered
plane trees, \(\tau\) is **not** a rerooting.  It is an exact
first-deepest-sector cut and graft.  If

\[
 D=P\,1\,R\,0\,S                                      \tag{0.1}
\]

is the canonical first-maximum decomposition, then

\[
 \boxed{\tau D=S\,1\,P\,0\,R.}                       \tag{0.2}
\]

Here the marked one enters the first deepest leaf, the displayed zero is
the first subsequent return to the root, and \(S\) is the contour of the
root branches strictly after the branch containing that leaf.  Thus the
two-step spatial displacement is

\[
 \boxed{-(|S|+1)=-(2|E(S)|+1)\pmod N.}               \tag{0.3}
\]

An odd omitted-label return of gap \(2s+1<N\) is therefore the exact
plane-tree sector equation

\[
 \boxed{
 \sum_{h=0}^{s-1}(2|E(S_h)|+1)
   =\alpha(T_s)+aN,
 \qquad \alpha(T_s)=|P_s|+1,
 }                                                     \tag{0.4}
\]

where \(T_h=T(\tau^hD)\), \(\alpha(T_h)\) is the contour time of the
first arrival at the first deepest leaf, and \(a\ge0\).  The return is
consecutive precisely when the corresponding congruence fails at every
earlier odd time.  Equation (0.4), not a repeated edge in one fixed tree,
is the literal tree interpretation of a short return.

There are two rigorous obstructions to the proposed rerooting charge.

1. Already on the defect-one core
   \(E_d=(10)^{d-2}1100\), \(d\ge3\), the trees of \(E_d\) and
   \(\tau E_d=1(10)^{d-1}0\) have different unrooted degree multisets.
   They are respectively a broom and a star.  Hence no charge transported
   by ordinary rerooting of the standard contour tree can be \(\tau\)-
   invariant.

2. The central gap-seven Pascal fibre rules out even a uniform local
   charge to the **full** edge or corner set of the fixed reduced core.
   For \(2d-1=r/2+O(1)\), there is a long-cycle edge-disjoint family over
   this one reduced passage with normalized mass

   \[
    \frac{|\mathcal P|}{P_r(E_d)}\ge\frac1{18}-o(1). \tag{0.5}
   \]

   Consequently every assignment of these intervals to the \(d\) core
   edges has some edge of load at least

   \[
    \left(\frac1{18}-o(1)\right)\frac{P_r(E_d)}d,    \tag{0.6}
   \]

   and every assignment to the \(2d\) core corners has some corner of
   load at least

   \[
    \left(\frac1{36}-o(1)\right)\frac{P_r(E_d)}d.    \tag{0.7}
   \]

Thus a per-core \(o(P_r(E)/d)\) tree-edge or tree-corner congestion
theorem is false.  The obstruction is local, not global: this particular
core fibre has only \(\exp((\log2+o(1))r)=o(B_r/N)\) mass.  A viable charge
may still allow such rare cores to be exceptional and prove an aggregate
Pascal-weighted estimate across the critical saddle.

The exact necessary saddle statement is sharpened below.  If
\((\mathrm{RP}_A)\) holds, then bounded-slot predecessor passages must
have vanishing two-dimensional Gaussian-weighted density throughout the
Pascal saddle.  This is the precise surviving boundary for any nonlocal
unrooted-tree/corner charge.

## 1. The exact plane-tree action of \(\tau\)

Let \(T(D)\) be the rooted ordered plane tree whose contour word is the
Dyck word \(D\), with one denoting traversal away from the root and zero
traversal toward the root.  Let \(H\) be the height of \(T(D)\), and let
\(v\) be the first vertex at depth \(H\) reached by the contour.  It is a
leaf.  Mark the up-step entering \(v\).  Starting after that step, mark the
first down-step which returns the contour to the root.  This gives the
unique factorization (0.1).

The suffix \(S\) is a Dyck word.  In tree language it is the ordered forest
of root branches lying strictly after the first root branch which contains
a deepest leaf.  If that suffix forest has \(j\) edges, then

\[
 |S|=2j.                                               \tag{1.1}
\]

### Theorem 1.1 (first-deepest-sector transport)

For every nonempty Dyck word \(D\),

\[
 \tau D=S1P0R.                                        \tag{1.2}
\]

On the physical PBBS skew product, two steps send

\[
 (u,D)\longmapsto
 \bigl(u-(2j+1)\pmod N,\ S1P0R\bigr).                \tag{1.3}
\]

#### Proof

The one-step quotient map is

\[
 \phi(D)=\overline R\,1\,\overline S\,0\,\overline P.
                                                               \tag{1.4}
\]

The displayed one is the first step reaching the maximum of this word:
\(\overline R\) rises from zero to height \(H-1\) without reaching
\(H\), the displayed one reaches \(H\), and the rest never exceeds it.
Applying the same one-step formula again gives

\[
 \phi^2(D)
 =\overline{\,\overline S0\overline P\,}\,0\,
   \overline{\overline R}
 =S1P0R,
\]

which is (1.2).  The two one-step displacements add to

\[
 |P|+1+|R|+1=N-(|S|+1).
\]

Reduction modulo \(N\), together with (1.1), proves (1.3). \(\square\)

The operation (1.2) is a contour-sector cut and graft.  It is not merely a
change of the root: the marked one and displayed zero need not be matched
to one another, and their reordering can change vertex degrees.

## 2. Short returns are accumulated sector equations

For \(D_h=\tau^hD\), write

\[
 D_h=P_h1R_h0S_h,
 \qquad
 j_h=|E(S_h)|,
 \qquad
 \alpha_h=|P_h|+1.                                  \tag{2.1}
\]

The number \(\alpha_h\) is exactly the contour index of the up-step which
first reaches the maximum height of \(T(D_h)\), or equivalently the first
arrival time at its first deepest leaf.

### Theorem 2.1 (tree-sector return criterion)

Assume \(2s+1<N\).  The omitted physical label at \((u,D)\) returns after
\(2s+1\) PBBS steps if and only if, for a unique integer \(a\ge0\),

\[
 \sum_{h=0}^{s-1}(2j_h+1)=\alpha_s+aN.               \tag{2.2}
\]

It is the first return if and only if

\[
 \sum_{h=0}^{t-1}(2j_h+1)\not\equiv\alpha_t\pmod N
 \qquad(0\le t<s).                                  \tag{2.3}
\]

#### Proof

By (1.3), after \(s\) two-step moves the spatial root is

\[
 u-\sum_{h=0}^{s-1}(2j_h+1)\pmod N.
\]

The last odd PBBS move advances it by
\(\delta(D_s)=\alpha_s\).  Equality with the initial root is therefore
equivalent to (2.2) modulo \(N\).  Positivity gives the unique integer
\(a\), and applying the same criterion to every shorter odd prefix gives
(2.3). \(\square\)

The important negative point is literal: (2.2) compares a sum of suffix-
forest sizes in a sequence of generally nonisomorphic trees with one final
contour-arrival time.  It is not, under the standard contour bijection, the
return of a root or an edge inside one unrooted tree.

## 3. Ordinary rerooting is impossible

For \(d\ge2\), put

\[
 E_d=(10)^{d-2}1100.                                 \tag{3.1}
\]

More generally write

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c,
 \qquad a,c\ge0,\ b\ge1.
\]

Direct substitution into the one-step formula gives

\[
 \phi E(a,b,c)=E(b-1,c+1,a).                        \tag{3.2}
\]

Since \(E_d=E(d-2,1,0)\), applying (3.2) twice yields

\[
 \boxed{\tau E_d=E(0,d-1,0)=1(10)^{d-1}0.}          \tag{3.3}
\]

The standard contour tree of \(E_d\) has \(d-2\) leaf children at the
root and one final child which itself has one leaf child.  Its unrooted
degree multiset is

\[
 \{d-1,2,1^{d-1}\}.                                 \tag{3.4}
\]

The standard contour tree of \(1(10)^{d-1}0\) is a star rooted at one of
its leaves.  Its unrooted degree multiset is

\[
 \{d,1^d\}.                                         \tag{3.5}
\]

For every \(d\ge3\), (3.4) and (3.5) differ.  Therefore neither a root
change, a root-corner change, a reflection, nor any composition of these
operations can realize \(\tau\) on the ordinary contour tree.

An explicit all-rank version makes the same degree change before any
pruning.  For \(d\ge3\) and \(r\ge2d-1\), put

\[
 D_{r,d}=(10)^{r-(2d-1)}(1100)^{d-2}111000.          \tag{3.6}
\]

Writing \(a=r-(2d-1)\), two direct first-maximum substitutions give

\[
 \tau D_{r,d}
 =1(10)^a(1100)^{d-2}11000.                         \tag{3.7}
\]

The tree of (3.6) has degree multiset

\[
 \{r-d,2^d,1^{r-d}\},                              \tag{3.8}
\]

whereas the tree of (3.7) has degree multiset

\[
 \{r-d+1,2^{d-1},1^{r-d+1}\}.                      \tag{3.9}
\]

Thus these are nonisomorphic throughout this stated range.  The word
(3.6) starts a genuine gap-seven omitted-label return.  This gives a
literal short-return example for which the first \(\tau\)-move is a
shape-changing graft, not a rerooting.

There is one genuine tree-derived orbit invariant: peak deletion
semiconjugates the dynamics,

\[
 \partial\tau D=\tau\partial D.
\]

Hence the iterated pruning-rank profile
\((|\partial^jD|/2)_{j\ge0}\) is constant on a \(\tau\)-orbit.  It does
not identify or transport individual unrooted edges.  Moreover the
gap-seven family in the next section has the common complete reduced chain

\[
 E_d\xrightarrow{\partial}10\xrightarrow{\partial}\varnothing,
\]

so even retaining the entire downstream pruning profile does not remove
the local congestion obstruction.

## 4. The full reduced edge/corner menu still has constant normalized congestion

The one-step inverse-pruning fibre above \(E_d\) has exact capacity

\[
 P_r(E_d)=\binom{r+1}{2d}.                           \tag{4.1}
\]

A parent root above this core starts the gap-seven return exactly when its
final root slot is empty.  The allowed start hyperplane has size

\[
 K_r(E_d,0)=\binom r{2d-1},                          \tag{4.2}
\]

and hence

\[
 \frac{K_r(E_d,0)}{P_r(E_d)}=\frac{2d}{r+1}.        \tag{4.3}
\]

Fix \(H\ge4\) with \(H\log N=o(r)\), and choose \(d=d(r)\) with
\(2d-1=r/2+O(1)\).  Then (4.3) is \(1/2+o(1)\).  At gap seven, a
quotient residence interval contains five
transition edges.  After deleting the \(\exp(o(r))\) starts on short
parent quotient cycles, greedy selection deletes at most nine candidate
starts per selected interval.  It therefore gives an edge-disjoint family
\(\mathcal P\) on long parent cycles satisfying

\[
 |\mathcal P|
 \ge\frac19\bigl(K_r(E_d,0)-\exp(o(r))\bigr),        \tag{4.4}
\]

and consequently

\[
 \frac{|\mathcal P|}{P_r(E_d)}\ge\frac1{18}-o(1).  \tag{4.5}
\]

Every member has the same reduced ordered passage trace, including both
nested child returns.  Thus any charge whose menu is determined by this
trace has constant normalized congestion.

The same conclusion survives when the menu is enlarged to every edge or
corner of the reduced plane tree.  An arbitrary assignment of the members
of \(\mathcal P\) to the \(d\) edges of \(T(E_d)\) has a fibre of size at
least \(|\mathcal P|/d\).  By (4.5), this proves (0.6).  There are exactly
\(2d\) ordinary plane-tree corners, so the same pigeonhole argument proves
(0.7).

This rules out a **uniform local** theorem with \(o(P_r(E)/d)\) load per
core edge or corner.  It does not rule out an aggregate theorem which
allows the core \(E_d\) to be exceptional: (4.2), at this central choice
of \(d\), has exponential rate \(\log2\), whereas
\(B_r/N\) has exponential rate \(\log4\).

Nor does it rule out assigning different parent slot vectors to edges of
their different full parent trees.  Such a charge is no longer a charge
through a fixed reduced unrooted object; it must carry the complete Pascal
slot vector and prove a global weighted budget.

## 5. A necessary two-dimensional Pascal-saddle sparsity theorem

The previous obstruction identifies what a surviving aggregate tree charge
must prove.  The statement can be made exact at the Gaussian Pascal saddle.

For a reduced rank \(d\) and peak count \(k\), let

\[
 \mathcal C_{d,k}=\{E\in\mathcal D_d:\operatorname{pk}(E)=k\},
 \qquad
 \mathsf N(d,k)=\frac1d\binom dk\binom d{k-1}.      \tag{5.1}
\]

Fix \(A,a>0\) and an integer \(z_0\ge0\), and put

\[
 H=A\sqrt r+O(1).                                   \tag{5.2}
\]

For every cell with

\[
 \left|d-\frac r2\right|\le a\sqrt r,
 \qquad
 \left|k-\frac r6\right|\le a\sqrt r,              \tag{5.3}
\]

let \(\eta_r(d,k)\) be the fraction of \(E\in\mathcal C_{d,k}\)
for which there is a predecessor-passage time

\[
 g\le2H-1
\]

whose prescribed final slot satisfies \(z_E(g)\le z_0\).  Put

\[
 u_{d,k}=\frac{k-r/6}{\sqrt r},
 \qquad
 v_d=\frac{d-r/2}{\sqrt r},
\]

and

\[
 Q(u,v)=81u^2-18uv+33v^2.                           \tag{5.4}
\]

### Theorem 5.1 (saddle-passage sparsity is necessary for \(\mathrm{RP}_A\))

If

\[
 \overline\nu_H=o(B_r/N),                           \tag{5.5}
\]

then, for every fixed \(a,z_0\),

\[
 \boxed{
 \frac1{\sqrt r}
 \sum_{\substack{|d-r/2|\le a\sqrt r\\
                   |k-r/6|\le a\sqrt r}}
 \eta_r(d,k)
 \exp\!\left[-\frac{Q(u_{d,k},v_d)}8\right]
 \longrightarrow0.}
                                                               \tag{5.6}
\]

More quantitatively, the proof gives the pointwise asymptotic inequality

\[
 \frac{r\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A\,4^{z_0}}+o(1)\right)
 \frac1{\sqrt r}
 \sum_{(d,k)\ \text{ in }(5.3)}
 \eta_r(d,k)e^{-Q(u_{d,k},v_d)/8}-o(1).             \tag{5.7}
\]

#### Proof

The exact outer mass above the cell \((d,k)\) is

\[
 \mathsf M_r(d,k)
 =\mathsf N(d,k)\binom{r+d-k}{2d}.                  \tag{5.8}
\]

Uniformly in the bounded saddle window (5.3), Stirling's formula gives

\[
 \frac{\mathsf M_r(d,k)}{B_r}
 =\frac{9\sqrt2}{2\pi r}
   e^{-Q(u_{d,k},v_d)/8}(1+o(1)).                   \tag{5.9}
\]

For each qualifying core choose one qualifying passage.  Different cores
have disjoint inverse fibres.  If its prescribed slot is \(z\le z_0\),
then uniformly in the same saddle window

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 \ge\left(\frac34+o(1)\right)4^{-z_0}.              \tag{5.10}
\]

Therefore the chosen passages have at least

\[
 \left(\frac34+o(1)\right)4^{-z_0}
 \sum_{(d,k)\ \text{ in }(5.3)}
 \eta_r(d,k)\mathsf M_r(d,k)                       \tag{5.11}
\]

distinct outer start roots.  Remove the
\(Z_H=\exp(o(r))\) roots on short outer quotient cycles.  All remaining
intervals have at most \(H+1\) edges.  On directed cycles, an interval of
this length conflicts only with starts at at most \(H\) preceding and
\(H\) following edges.  Greedy selection therefore retains at least a
\((2H+1)^{-1}\) fraction of the starts.

Substitute (5.9) into (5.11), divide by
\(2H+1=(2A+o(1))\sqrt r\), and note that the
short-cycle term is negligible compared with every saddle cell.  The
result is (5.7).  Assertion (5.6) follows from (5.5), since
\(N=(2+o(1))r\). \(\square\)

The sum in (5.6) ranges over \(\Theta(r)\) saddle cells.  Thus a positive
passage fraction in a positive fraction of the saddle cells is far too
large; even total weighted passage density of order \(\sqrt r\) is the
critical boundary.  This is strictly stronger than a rank-only or one-
curve density requirement.

The bounded-slot layers can be retained simultaneously.  For an integer
\(z\ge0\), let \(\eta_r(d,k;z)\) be the fraction of cores in
\(\mathcal C_{d,k}\) admitting a predecessor passage
\(g\le2H-1\) with exact prescribed slot \(z_E(g)=z\).  A fixed core has
at most one such passage for each \(z\): two distinct next-return times
cannot prescribe the same parent start hyperplane.  Put

\[
 L_r=\lceil3\log r\rceil
\]

and

\[
 \mathcal S_r^*(a)=
 \frac1{\sqrt r}
 \sum_{\substack{|d-r/2|\le a\sqrt r\\
                  |k-r/6|\le a\sqrt r}}
 e^{-Q(u_{d,k},v_d)/8}
 \sum_{z=0}^{L_r}4^{-z}\eta_r(d,k;z).               \tag{5.12}
\]

### Corollary 5.2 (all low-slot layers at once)

For \(H=A\sqrt r+O(1)\), the following pointwise asymptotic inequality
holds:

\[
 \boxed{
 \frac{r\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A}+o(1)\right)
 \mathcal S_r^*(a)-o(1).}                           \tag{5.13}
\]

In particular, \(\mathrm{RP}_A\) forces

\[
 \boxed{\mathcal S_r^*(a)\longrightarrow0}
                                                               \tag{5.14}
\]

for every fixed \(a\).

#### Proof

For fixed \(E\), the start hyperplanes belonging to different exact slot
values \(z\) are disjoint.  Hence all qualifying pairs \((E,z)\) may be
counted simultaneously before greedy packing.  Uniformly in the saddle
tube and for \(0\le z\le L_r=O(\log r)\), the exact product formula for
the Pascal ratio gives

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\left(\frac34+o(1)\right)4^{-z},                 \tag{5.15}
\]

because the logarithmic relative error in the product is
\(O(z/\sqrt r+z^2/r)=o(1)\), uniformly in this range.  Substitute
(5.15) and the cell asymptotic (5.9), sum over \(z\), remove the same
\(Z_H=\exp(o(r))\) short-cycle starts once, and apply the same
\((2H+1)^{-1}\) variable-length greedy bound.  This gives (5.13), and
(5.14) follows as in Theorem 5.1. \(\square\)

Corollary 5.2 is the sharpest density consequence currently forced by the
Pascal saddle and the universal interval greedy bound.  It still is only
necessary: it does not supply an upper bound for an arbitrary packing.

## 6. Exact surviving boundary for a tree/orbit charge

The preceding results leave one route logically open, but make its required
content precise.

* It cannot use the ordinary unrooted contour tree as a \(\tau\)-orbit
  invariant: Section 3 disproves invariance before any asymptotics.
* It cannot factor through one reduced passage or a bounded collection of
  its nested child returns: (4.5) gives constant normalized congestion.
* It cannot have uniform \(o(P_r(E)/d)\) congestion even after opening all
  reduced core edges or corners: (0.6)--(0.7) are sharp local obstructions.
* It may use the full parent slot vector and allow rare cores such as
  \(E_d\) to carry constant local load.  It must then prove an aggregate
  Pascal-weighted dispersion or orbit-overlap theorem across the two-
  dimensional saddle, at least strong enough to force (5.6) for every
  bounded slot layer.

The latest capacitated pruning reduction further shows that, up to
\(o(B_r/N)\) start roots, only

\[
 d\ge r/4,
 \qquad
 z_E(g)\le3\log r+O(1)                              \tag{6.1}
\]

remains.  Hence the honest positive target is a high-rank, low-predecessor-
multiplicity, slot-sensitive orbit charge.  No standard-tree rerooting
invariant or local edge/corner menu supplies it.

## 7. Audit and scope

1. Equations (1.2)--(1.3) are ordinary integer/word identities; no
   probabilistic or completion assumption is used.
2. Equation (2.2) is valid for \(2s+1<N\).  This contains
   \(H=A\sqrt r\) for each fixed \(A\) and all sufficiently large \(r\).
3. The degree multisets (3.4), (3.5), (3.8), and (3.9) count all vertices
   and all degrees, so the nonisomorphism claim is unrooted and does not
   depend on the root corner.
4. The constant \(1/18\) is exactly the product of the limiting retained
   fibre fraction \(1/2\) and the rigorous five-edge greedy factor \(1/9\).
5. The corner bound uses the exact identity that an \(d\)-edge plane tree
   has \(2d\) corners.
6. Theorem 5.1 is a necessary consequence of \((\mathrm{RP}_A)\), not a
   proof of it.  It concerns actual predecessor passages and exact Pascal
   lifts, not merely available fibre capacity.
7. The report does not rule out an exotic derived unrooted object unrelated
   to the standard contour tree.  To be useful, such an object must retain
   full slot-vector/orbit information and prove the aggregate saddle
   dispersion demanded by (5.6); naming a \(\tau\)-orbit itself as an
   unrooted object is only a restatement of the original packing problem.

The precise proved boundary is therefore negative but substantive: the
natural rerooting/orbit invariant does not exist, and every local
tree-edge/corner normalization fails at constant density.  The only
surviving version is a genuinely aggregate Pascal-saddle orbit theorem.
