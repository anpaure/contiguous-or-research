# Helly packing for protected geodesic strips and the exact nonlinear defect

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web input, or
fixed-rank coloring theorem is used.

## 0. Outcome

Let \(\mathcal H\) be the cleared rational multicover of retained
return-free protected strips.  Write

\[
 D=m^{5/2-o(1)}
\tag{0.1}
\]

for its tag degree and target-degree scale.  If \(P\) is a protected path,
write \(C(P)\) for its claimed target set and put

\[
 K=\max_P|C(P)|.
\tag{0.2}
\]

The bounded-displacement/geodesic coordinates give the exact bound

\[
 K\le g+2gQ=(2Q+1)g=m^{1+o(1)},
\qquad
 K^2=o(D).
\tag{0.3}
\]

This note proves the following defect-Helly theorem.  For every pairwise
target-intersecting family \(\mathcal F\) of distinct-tag protected paths,
let

\[
 \omega(\mathcal F)
 =\max_v|\{P\in\mathcal F:v\in C(P)\}|
\tag{0.4}
\]

be its largest target clique.  Let \(\tau_2(\mathcal F)\) be the minimum
number of paths which must be deleted so that every two remaining paths
share at most one target.  Then

\[
 \boxed{
 |\mathcal F|
 \le \tau_2(\mathcal F)
    +\max\{\omega(\mathcal F),K^2-K+1\}.}
\tag{0.5}
\]

Consequently:

1. Every target-linear projective-plane-type family has size at most
   \(K^2-K+1=o(D)\), unless it is a target star.
2. Since every target clique has size at most \(D+o(D)\), any family with
   \(|\mathcal F|\ge(1+\delta)D\), for fixed \(\delta>0\), must satisfy
   \[
    \tau_2(\mathcal F)=\Omega(D).
   \tag{0.6}
   \]
   Thus a color-scale obstruction in the actual catalogue cannot be a
   projective plane carried only by singleton intersections.  It must
   contain a linear-sized nonlinear core.
3. Strict Helly is false even for literal return-free strips.  Three
   protected geodesics can form a Johnson triangle: each pair shares a
   different middle owner, while the common lower facet is hidden in the
   unique depth-one zero column.  Hence the coefficient of the target
   clique in (0.5) cannot be replaced by an exact Helly assertion.

Equation (0.5) resolves the new projective-plane check at the coefficient
scale.  It does not prove the desired edge coloring.  The protected
width-two exponential moment is an average and does not imply
\(\tau_2(\mathcal F)=o(D)\) for every adversarial intersecting family.
The exact remaining clique gate is therefore a nonlinear-core packing
theorem, not another singleton-codegree estimate.

## 1. Exact protected rank from the geodesic coordinates

A return-free grid has the form

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
    \cup\{b_1,\ldots,b_j\}.
\tag{1.1}
\]

At physical phase \(t\), its owner and signed flags are

\[
 X_t=G_{t,t},\qquad
 L_q(t)=G_{t+q,t},\qquad
 U_q(t)=G_{t-q,t}.
\tag{1.2}
\]

The bounded-displacement gap construction is exactly rainbow in every
signed protected row.  Hence all target occurrences within one claimed
row are distinct.

Let \(c_q(P)\) be the number of phase columns of \(P\) whose priority
height is at least \(q\).  Every owner is claimed, and a height-\(q\)
column claims one lower and one upper target at depth \(q\).  Therefore

\[
 \boxed{
 |C(P)|=g+2\sum_{q=1}^Q c_q(P).}
\tag{1.3}
\]

In particular,

\[
 |C(P)|\le(2Q+1)g.
\tag{1.4}
\]

At the calibrated scales

\[
 g=(1-o(1))H=m^{1/2+o(1)},\qquad
 Q=m^{1/2+o(1)},
\tag{1.5}
\]

so (0.3) follows.  The balanced protected-three-antichain pruning retains
degree

\[
 D=m^{5/2-o(1)}
\tag{1.6}
\]

in every nonexceptional tag and target fibre.  Thus

\[
 {K^2\over D}=m^{-1/2+o(1)}=o(1).
\tag{1.7}
\]

This numerical separation is specific to the return-free protected
strip.  It is the reason a projective plane of order \(K-1\), although
extremal for abstract linear set systems, is below the required color
scale here.

## 2. Exact defect-Helly theorem

For a family \(\mathcal F\), define its nonlinear-pair graph
\(\mathcal N_2(\mathcal F)\) on vertex set \(\mathcal F\) by

\[
 PE\in E(\mathcal N_2)
 \quad\Longleftrightarrow\quad
 |C(P)\cap C(E)|\ge2.
\tag{2.1}
\]

Let

\[
 \tau_2(\mathcal F)
 =\tau(\mathcal N_2(\mathcal F))
\tag{2.2}
\]

be its minimum vertex-cover number.

### Theorem 2.1 (protected-strip defect Helly)

Every pairwise target-intersecting family \(\mathcal F\) of protected
paths satisfies (0.5).

#### Proof

Delete a minimum vertex cover \(\mathcal Z\) of
\(\mathcal N_2(\mathcal F)\), and put

\[
 \mathcal F_0=\mathcal F\setminus\mathcal Z.
\tag{2.3}
\]

Then

\[
 |\mathcal Z|=\tau_2(\mathcal F),
\tag{2.4}
\]

and \(\mathcal F_0\) remains pairwise target-intersecting, while every two
of its members meet in exactly one target.

Suppose first that all members of \(\mathcal F_0\) contain one target
\(v\).  Then

\[
 |\mathcal F_0|\le\omega(\mathcal F).
\tag{2.5}
\]

Otherwise choose \(A,B\in\mathcal F_0\) and write

\[
 C(A)\cap C(B)=\{x\}.
\tag{2.6}
\]

Because \(\mathcal F_0\) is not a star, choose
\(F\in\mathcal F_0\) with \(x\notin C(F)\).

Every member of \(\mathcal F_0\) containing \(x\) must meet \(F\).  Two
such members cannot meet \(F\) in the same target, since they would then
share that target and \(x\).  Thus at most

\[
 |C(F)|\le K
\tag{2.7}
\]

members contain \(x\).

Every member \(E\) not containing \(x\) determines the ordered pair

\[
 \bigl(C(E)\cap C(A),\,C(E)\cap C(B)\bigr)
 \in
 (C(A)\setminus\{x\})\times(C(B)\setminus\{x\}).
\tag{2.8}
\]

Both entries in (2.8) are singleton targets.  The map is injective:
two members with the same ordered pair would share two targets.  Hence at
most

\[
 (K-1)^2
\tag{2.9}
\]

members avoid \(x\).  Combining (2.7)--(2.9) gives

\[
 |\mathcal F_0|\le K+(K-1)^2=K^2-K+1.
\tag{2.10}
\]

Finally,

\[
 |\mathcal F|
 =|\mathcal Z|+|\mathcal F_0|
 \le\tau_2(\mathcal F)
   +\max\{\omega(\mathcal F),K^2-K+1\},
\]

which is (0.5). \(\square\)

### Corollary 2.2 (projective-plane obstruction is subcritical)

If \(\mathcal F\) is target-linear, then

\[
 |\mathcal F|
 \le\max\{\omega(\mathcal F),K^2-K+1\}.
\tag{2.11}
\]

In the cleared protected multicover,

\[
 \omega(\mathcal F)\le D+o(D),
\tag{2.12}
\]

and \(K^2=o(D)\).  Therefore

\[
 \boxed{|\mathcal F|\le D+o(D).}
\tag{2.13}
\]

If \(\mathcal F\) is not a star, then the stronger bound

\[
 |\mathcal F|\le K^2-K+1=o(D)
\tag{2.14}
\]

holds.  Lines of an abstract projective plane attain the
\(K^2-K+1\) term, but that term is too small by
\(m^{1/2-o(1)}\) to obstruct a near-\(D\) coloring of the protected
multicover.

### Corollary 2.3 (every color-scale obstruction is nonlinear)

For an arbitrary pairwise target-intersecting \(\mathcal F\),

\[
 \tau_2(\mathcal F)
 \ge
 |\mathcal F|
 -\max\{\omega(\mathcal F),K^2-K+1\}.
\tag{2.15}
\]

Thus if, for some fixed \(\delta>0\),

\[
 |\mathcal F|\ge(1+\delta)D
\tag{2.16}
\]

and all target degrees are at most \(D+o(D)\), then

\[
 \boxed{\tau_2(\mathcal F)\ge(\delta-o(1))D.}
\tag{2.17}
\]

The projective-plane alternative has disappeared.  A genuinely bad
clique must retain a linear-sized family after every attempt to cover all
multiple-intersection pairs.

Equivalently it contains a linear packing of nonlinear pairs.  The
endpoints of a maximal matching in \(\mathcal N_2(\mathcal F)\) form a
vertex cover, so

\[
 \nu(\mathcal N_2(\mathcal F))
 \ge{\tau_2(\mathcal F)\over2}
 \ge\left({\delta\over2}-o(1)\right)D.
\tag{2.18}
\]

Thus every color-scale nonstar clique contains \(\Omega(D)\)
vertex-disjoint pairs of strips, each pair sharing at least two protected
targets.  This is the exact packing form of the remaining obstruction.

## 3. Relation to the protected width-two census

Define the internal repeated-intersection mass

\[
 R_2(\mathcal F)
 =\sum_{\{P,E\}\subseteq\mathcal F}
   \binom{|C(P)\cap C(E)|}{2}.
\tag{3.1}
\]

Every edge of \(\mathcal N_2(\mathcal F)\) contributes at least one to
(3.1).  Choosing one endpoint from every nonlinear pair gives

\[
 \tau_2(\mathcal F)
 \le |E(\mathcal N_2(\mathcal F))|
 \le R_2(\mathcal F).
\tag{3.2}
\]

Theorem 2.1 therefore also gives the completely numerical form

\[
 \boxed{
 |\mathcal F|
 \le R_2(\mathcal F)
 +\max\{\omega(\mathcal F),K^2-K+1\}.}
\tag{3.3}
\]

After protected three-antichain pruning, every common-target poset has
width at most two.  In the exact geodesic coordinates, if a common shape
has meet \(I\), join \(J\), and span

\[
 t=|J\setminus I|,
\tag{3.4}
\]

then

\[
 |C(P)\cap C(E)|\le2(t+1),
\tag{3.5}
\]

and a fixed span-\(t\) shape has relative degree at most

\[
 m^{o(1)}{t+1\over\binom{m-g}{t}}.
\tag{3.6}
\]

These are the exact bounded-displacement/grid inputs behind the
width-two exponential census.

They do not imply a useful uniform upper bound on
\(\tau_2(\mathcal F)\).  The census controls, for each catalogue edge,
an average over all competitors.  An adversarial pairwise-intersecting
family may concentrate on the exceptional nonlinear competitors.  In
particular, a bound

\[
 {1\over D}\sum_E
 \left(w^{|C(P)\cap C(E)|}
       -1-(w-1)|C(P)\cap C(E)|\right)
 =m^{o(1)}
\tag{3.7}
\]

allows \(\Theta(D)\) nonlinear-pair vertices and does not imply
\(\tau_2=o(D)\).

Equations (2.15)--(2.17) nevertheless give a sharp structural reduction:
the singleton-intersection geometry is finished.  To bound cliques at
the color scale, it is enough to prove

\[
 \boxed{\tau_2(\mathcal F)=o(D)}
\tag{3.8}
\]

for every pairwise target-intersecting family.  This is a nonlinear-core
packing theorem.  It is strictly stronger than the present averaged
width-two moment and strictly weaker than demanding that the whole
catalogue be target-linear.

## 4. Strict Helly fails in the actual geodesic orbit

The additive nonlinear defect in (0.5) is not an artifact.  Literal
protected geodesics already contain a three-cycle with no common target.

Choose

\[
 R\in\binom{[2m]}{m-1}
\tag{4.1}
\]

and distinct coordinates \(x_1,x_2,x_3\notin R\).  Put

\[
 X_i=R\cup\{x_i\}\qquad(i=1,2,3).
\tag{4.2}
\]

The three Johnson edges

\[
 X_1X_2,\qquad X_2X_3,\qquad X_3X_1
\tag{4.3}
\]

can each be placed at an interior physical phase and extended in both
directions to a return-free length-\(g\) geodesic.  Prescribe
\(x_i\) as the departure and \(x_j\) as the arrival at the displayed
exchange.  For the earlier transitions choose disjoint forward arrivals
inside \(X_i\) and their departures outside \(X_i\); for the later
transitions choose disjoint departures from the unused part of \(X_i\)
and arrivals outside \(X_i\).  Taking all departure and arrival
coordinates distinct gives one global monotone \(a/b\)-ordering.  This is
possible because \(g=o(m)\).

The common lower facet of all three prescribed transitions is \(R\).
For return-free chunks,

\[
 \bar d_1^{(g)}=1.
\tag{4.4}
\]

Assign the unique depth-one zero-height phase of each chunk to its
prescribed transition.  Then none of the three path-edges claims \(R\),
while every path-edge still claims all of its middle owners.  Consequently
the three claimed target sets meet cyclically in

\[
 X_1,\qquad X_2,\qquad X_3,
\tag{4.5}
\]

with no common owner target.

The remaining extensions can be chosen so that no additional target is
common to all three.  Indeed, choose their unused departure and arrival
coordinates from pairwise disjoint auxiliary pools.  Outside the forced
sets in (4.2)--(4.3), every claimed target then contains an auxiliary
membership atom absent from at least one of the other two grids.

Thus the actual protected-strip intersection graph contains a triangle
which is not a target star.  Pairwise target intersection has Helly
number greater than two.  This example has constant size and is harmless
at scale \(D\), but it shows why Theorem 2.1 must have a nonstar error
term.

## 5. Exact status of the coloring route

The projective-plane concern and the coloring theorem are now separated.

1. A projective-plane-like family whose pairs meet in different singleton
   targets has at most
   \[
    K^2-K+1=o(D)
   \]
   members.  It cannot force more than \(D+o(D)\) colors.
2. Any pairwise-intersecting family larger than one target clique by
   \(\delta D\) has a nonlinear-pair vertex-cover number at least
   \((\delta-o(1))D\).
3. The current protected width-two moment does not rule out such a
   nonlinear core.  Max codegree does not do so either, because the core
   may distribute its repeated intersections among many target pairs.

Therefore the exact next theorem for Gate A of the multicover coloring
route is:

> **Nonlinear-core packing theorem.**  In the balanced
> protected-three-antichain-pruned geodesic catalogue, every pairwise
> target-intersecting family satisfies
> \[
>  \tau_2(\mathcal F)=o(D).
> \]

If this holds, Theorem 2.1 gives clique number \(D+o(D)\).  A weighted
matching-cover theorem and the growing-rank integral coloring step are
still additionally required; small cliques alone do not imply a
near-\(D\) coloring.

No projective-plane-scale family inside the literal protected geodesic
catalogue is constructed here.  The theorem proves that even if a
target-linear one exists, it is subcritical by the factor
\(m^{1/2-o(1)}\).  The unresolved obstruction is necessarily nonlinear.
