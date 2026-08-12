# Global degree audit for owner-separated eight-template packets

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

Throughout,

\[
 n=2m,\qquad W=\binom{2m}m,\qquad M=m+H,\qquad
 N_H=\binom{2m}M,
\]

with calibrated \(H\) satisfying \(W/(MN_H)=1+o(1)\), and
\(Q=o(H)\), \(H=o(m)\).

## 0. Outcome

The owner-separated eight-template gadget has no static coefficient-scale
degree or overlap obstruction.

At the middle layer, either sign of the trade uses twelve distinct owners,
but the union of the two signs has fourteen owners, supported on

\[
 K\cup\{u,v,a,b,c,d\},
 \qquad |K|=m-3.
 \tag{0.1}
\]

For the ordered packet hypergraph:

1. every owner has exact robust-packet skeleton degree
   \[
     14(m)_3^2;
   \]
2. two owners at Johnson distance \(\delta\) have codegree zero for
   \(\delta>3\), and normalized codegree \(O(m^{-2\delta})\) for
   \(1\le\delta\le3\);
3. every higher owner overlap is
   \(O(m^{-(\kappa+e)})\) of one-owner degree, where
   \(m-\kappa\) is the common-intersection size and \(m+e\) the union size;
4. fixing another carrier tag removes one free filler choice.  The
   normalized tag and mixed overlaps are \(o(1)\), in fact exponentially
   smaller than any fixed power of \(m\).

Clone every carrier into

\[
 b=\left\lfloor\frac {2M}7\right\rfloor
 \tag{0.2}
\]

three-state block slots.  A robust packet uses four slots and reserves all
fourteen owners which can occur in either sign.  The robust-owner and slot
degrees then agree up to \(1+O(1/M)\).  An explicitly parameterized nibble
therefore gives a static robust matching with

\[
 \left(\frac1{14}-o(1)\right)W
 \tag{0.3}
\]

eight-template packets, covering all but \(o(W)\) robust owner
reservations and all but \(o(W)\) carrier slots.  This exceeds the
\((1/16-o(1))W\) correction-direction scale of the rectangular cube.

There is an essential distinction between a reservation and an occurrence.
After a sign is chosen, only twelve of the fourteen reserved owners occur;
the other two are shadow owners.  Thus a maximal robust matching by itself
would cover only \((6/7+o(1))W\) owners.  It is not a coefficient-one
construction.

At the required correction scale \(g=(1/16-o(1))W\), however, the exact
ledger is

\[
 12g=\left(\frac34-o(1)\right)W
 \quad\hbox{gadget occurrences},\qquad
 W-12g=\left(\frac14+o(1)\right)W
 \quad\hbox{remaining carrier states}.
 \tag{0.4}
\]

The robust union reserves \(14g=(7/8-o(1))W\) owners; its \(2g\) shadow
owners together with the \(W-14g\) unreserved owners form exactly the
\(W-12g\) targets that the remaining carrier states must hit.  Hence the
static packing has enough capacity, but no occurrence slack: every
non-gadget state must be productive up to \(o(W)\).

This is not yet a literal coefficient-one compiler.  A slot represents a
three-state diamond block, and independently matched blocks need not have
the endpoint/source equality required to concatenate them inside one
carrier walk.  Resetting between \(b=\Theta(M)\) blocks per carrier costs
\(\Theta(QM)\) letters per carrier and is fatal.

The exact remaining statement is therefore a **productive square-tube
completion lemma**: order the statically matched blocks so that the unused
quarter of the carrier states both connects successive blocks and hits the
entire complementary owner set with only \(o(W)\) collisions.  No higher
template is forced by the static degree audit.  Moreover, no larger
single-marked Johnson cycle has enough sign-robust capacity: a five-cycle
uses seventeen robust owners per direction.  If the productive tube lemma
is false, the minimal possible higher escape is a ten-template five-cycle
amortizing at least two marked rectangles, not a one-direction cycle.

## 1. The fourteen-owner robust packet

Use the notation of
MATH_AUDIT_PAIRED_DIAMOND_DUPLICATION_AND_EIGHT_TEMPLATE_20260725.md.
At the selected middle block, put

\[
 \Sigma=\{u,v,a,b,c,d\}.
\]

One positive configuration has the following twelve owner triples over the
common \((m-3)\)-set \(K\):

\[
\begin{aligned}
\mathcal F^+={}&
\{uva,uvc,uvd,uvb\}\\
&\cup\{vab,uac,ucd,ubd\}\\
&\cup\{abc,acd,bcd,abd\}.
\end{aligned}
 \tag{1.1}
\]

The negative configuration has intermediate triples

\[
 \{vac,ucd,ubd,uab\}.
 \tag{1.2}
\]

Thus the robust owner set which must be reserved before the sign is chosen is

\[
\begin{aligned}
\mathcal F={}&
\{uva,uvc,uvd,uvb\}\\
&\cup\{vab,vac,uac,uab,ucd,ubd\}\\
&\cup\{abc,acd,bcd,abd\},
\end{aligned}
 \tag{1.3}
\]

of size fourteen.  Each sign uses the same four sources and four endpoints
and four of the six intermediate owners.

Here, for example, \(uva\) denotes \(\{u,v,a\}\).  In (1.1), the three
displayed lines are respectively the four source, intermediate, and endpoint
owners.

An **ordered skeleton** is a choice of

\[
 K\in\binom{[2m]}{m-3}
\]

and an injection of the six ordered roles

\[
 (u,v,a,b,c,d)
\]

into \([2m]\setminus K\).  The number of ordered skeletons is

\[
 G_{\rm skel}
 =\binom{2m}{m-3}(m+3)_6.
 \tag{1.4}
\]

We keep ordered roles.  This removes irrelevant automorphism divisors and
makes every degree identity exact.

## 2. Exact owner degrees and pair codegrees

### Proposition 2.1 (one-owner degree)

Every middle owner belongs to exactly

\[
 \boxed{d_1=14(m)_3^2}
 \tag{2.1}
\]

ordered skeleton packets.

#### Proof

Coordinate symmetry makes the degree constant.  Double-counting
owner--packet incidences gives

\[
 d_1
 ={14G_{\rm skel}\over\binom{2m}m}.
\]

The exact factorial cancellation is

\[
 {\binom{2m}{m-3}(m+3)_6\over\binom{2m}m}
 =(m)_3^2.
\]

This proves (2.1). \(\square\)

For two middle owners \(X,Y\), write

\[
 \delta=|X-Y|=|Y-X|
\]

for their Johnson distance.  Let

\[
 A_\delta
 =
 \#\{(T,T')\in\mathcal F\times\mathcal F:
       T\ne T',\ |T-T'|=\delta\}.
 \tag{2.2}
\]

The constants are exactly

\[
 \boxed{(A_1,A_2,A_3)=(86,84,12).}
 \tag{2.2a}
\]

Indeed, among the \(\binom{14}2=91\) unordered pairs in \(\mathcal F\),
there are six complementary pairs, hence six pairs at distance three.  The
six triples missing from \(\binom\Sigma3\) induce seven edges of
\(J(6,3)\).  Since \(J(6,3)\) has 90 edges and every missing vertex has
degree nine, the subgraph induced by \(\mathcal F\) has
\(90-(6\cdot9-7)=43\) edges.  Thus 43 pairs have distance one and the
remaining \(91-43-6=42\) have distance two; ordered pairs give (2.2a).

### Proposition 2.2 (exact pair codegree)

If \(\delta>3\), no packet contains both \(X\) and \(Y\).  For
\(1\le\delta\le3\), their ordered-skeleton codegree is

\[
 \boxed{
 d_2(\delta)
 =
 A_\delta\,(\delta!)^2
 (m-\delta)_{3-\delta}^2.}
 \tag{2.3}
\]

Consequently

\[
 {d_2(\delta)\over d_1}=O(m^{-2\delta}).
 \tag{2.4}
\]

#### Proof

Every packet owner is \(K+T\) for a three-role set \(T\), so two owners in
one packet differ in at most three points.

Fix an ordered pattern pair \(T,T'\) at distance \(\delta\).  Their
\(3-\delta\) common roles may be injected into \(X\cap Y\) in

\[
 (m-\delta)_{3-\delta}
\]

ways.  The core \(K\) is then forced.  The two ordered groups of
\(\delta\) differing roles map bijectively to \(X-Y\) and \(Y-X\), giving
\((\delta!)^2\) choices.  The remaining \(3-\delta\) roles map into the
complement of \(X\cup Y\), also of size \(m-\delta\), in
\((m-\delta)_{3-\delta}\) ways.  Summing over the \(A_\delta\) pattern
pairs proves (2.3). \(\square\)

## 3. All higher owner overlaps

Let \(X_1,\ldots,X_s\) be distinct middle owners.  Put

\[
 \left|\bigcap_iX_i\right|=m-\kappa,
 \qquad
 \left|\bigcup_iX_i\right|=m+e.
 \tag{3.1}
\]

### Proposition 3.1 (higher-codegree formula)

A common packet is possible only if

\[
 0\le\kappa\le3,\qquad0\le e\le3,
 \tag{3.2}
\]

and the Venn pattern of the \(X_i\) is isomorphic to that of distinct
members \(T_1,\ldots,T_s\) of \(\mathcal F\).

For every compatible ordered pattern tuple, the number of skeletons is

\[
 \boxed{
 (m-\kappa)_{3-\kappa}
 (m-e)_{3-e}\,\gamma(T_1,\ldots,T_s;X_1,\ldots,X_s),}
 \tag{3.3}
\]

where \(\gamma\le6!\) counts the finitely many role bijections on the
noncommon, nonexternal Venn cells.  Therefore the \(s\)-owner codegree is

\[
 O_s\!\left(m^{6-\kappa-e}\right),
 \tag{3.4}
\]

and, relative to (2.1),

\[
 \boxed{
 {d_s(X_1,\ldots,X_s)\over d_1}
 =O_s(m^{-\kappa-e}).}
 \tag{3.5}
\]

#### Proof

The common core has size \(m-3\).  The common role intersection has size
\(3-\kappa\), and choosing its ordered image inside
\(\cap_iX_i\) gives the first falling factorial in (3.3); the core is then
forced.  The union of the role triples has size \(3+e\), leaving
\(3-e\) unused roles.  Their ordered images lie outside \(\cup_iX_i\) and
give the second falling factorial.  All remaining role images lie in fixed
finite Venn cells and contribute \(\gamma\). \(\square\)

This is the complete higher-overlap classification on the owner side.
The worst nontrivial overlap is a Johnson-neighbor pair and is
\(O(d_1/m^2)\).

## 3A. Marked-target degrees and all target overlaps

The middle owners above must not be confused with the four marked masks in
the rank-isolated rectangle.  Fix a target rank \(r\), put \(n=2m\), and
write its target support over an \((r-3)\)-core \(K_r\) as

\[
 \mathcal R=\{vab,uac,vac,uab\}.
 \tag{3A.1}
\]

The number of ordered target skeletons, including the sixth role \(d\) that
does not occur in \(\mathcal R\), is

\[
 G_{\rm tgt}(r)=\binom n{r-3}(n-r+3)_6.
 \tag{3A.2}
\]

### Proposition 3A.1 (exact target degrees)

Every rank-\(r\) mask has target-support degree

\[
 \boxed{d^{\rm tgt}_1(r)=4(r)_3(n-r)_3.}
 \tag{3A.3}
\]

Among ordered distinct pairs in \(\mathcal R\), eight have Johnson distance
one and four have distance two.  Therefore two rank-\(r\) masks at distance
\(\delta\) have exact target-support codegree

\[
 \boxed{
 d^{\rm tgt}_2(\delta;r)
 =B_\delta(\delta!)^2
 (r-\delta)_{3-\delta}
 (n-r-\delta)_{3-\delta},
 \quad (B_1,B_2)=(8,4),}
 \tag{3A.4}
\]

and codegree zero for \(\delta>2\).  In the central band
\(|r-m|\le Q=o(m)\), its normalized value is \(O(m^{-2\delta})\).

#### Proof

Double-count the four target incidences in (3A.2) and use

\[
 {\binom n{r-3}(n-r+3)_6\over\binom nr}
 =(r)_3(n-r)_3.
\]

For a fixed ordered pattern pair, embed its \(3-\delta\) common roles in the
intersection of the two masks, its two ordered \(\delta\)-role differences
in the two set differences, and the remaining \(3-\delta\) roles outside
their union.  This gives (3A.4). \(\square\)

At the marked middle rank \(r=m\), targets and robust owners live in the
same layer and their mixed degrees are also exact.  Since
\(\mathcal R\subset\mathcal F\), the same-vertex owner--target degree is

\[
 4(m)_3^2.
 \tag{3A.4a}
\]

For ordered pairs \((T,R)\in\mathcal F\times\mathcal R\), \(T\ne R\),
the counts at Johnson distances one, two, and three are

\[
 \boxed{(C_1,C_2,C_3)=(26,24,2).}
 \tag{3A.4b}
\]

Indeed the four target triples have, respectively, within \(\mathcal F\),
distance profiles \((6,6,1),(7,6,0),(6,6,1),(7,6,0)\).  Hence fixed
distinct middle masks \(X,Y\) at distance \(\delta\) have mixed
owner--target skeleton codegree

\[
 \boxed{
 d^{\rm own,tgt}_2(\delta)
 =C_\delta(\delta!)^2(m-\delta)_{3-\delta}^2.}
 \tag{3A.4c}
\]

For completeness, let distinct target masks \(Y_1,\ldots,Y_s\) satisfy

\[
 |\cap_iY_i|=r-\kappa,
 \qquad |\cup_iY_i|=r+e.
\]

A common target skeleton exists only when their Venn pattern is that of
distinct members of \(\mathcal R\), necessarily \(\kappa,e\le2\).  For
each compatible ordered pattern tuple its exact contribution is

\[
 (r-\kappa)_{3-\kappa}
 (n-r-e)_{3-e}\,\gamma_{\rm tgt},
 \qquad \gamma_{\rm tgt}\le6!,
 \tag{3A.5}
\]

so every nontrivial higher target overlap is

\[
 O_s\!\left(
 r^{-\kappa}(n-r)^{-e}d^{\rm tgt}_1(r)
 \right)
 =O_s(m^{-\kappa-e}d^{\rm tgt}_1(r))
 \tag{3A.6}
\]

in the central band.  Completing the chains and carrier tags multiplies all
terms in (3A.3)--(3A.5) by the same coordinate-symmetric extension factor
for that fixed \(r\); hence their normalized overlaps are unchanged.

At \(r=m\), every higher mixed owner--target overlap is obtained from
(3.3) by taking owner patterns from \(\mathcal F\) and marked patterns
from \(\mathcal R\).  This is an exact finite Venn-pattern classification,
not merely a pairwise estimate.

## 4. Chain-extension and carrier factors

Fix an ordered skeleton.  The common saturated chain
\(\mathcal B\) has

\[
 B_{m-3}=K.
\]

Below \(K\), choose the ordered \(Q-1\) increments which are removed to
reach rank \(m-Q-2\).  Above \(K\), the two prescribed adjacent increments
are \(u,v\), followed by \(Q\) further ordered increments outside
\(K\cup\Sigma\).  Hence the exact number of common chain extensions is

\[
 \boxed{
 A_Q=(m-3)_{Q-1}(m-3)_Q.}
 \tag{4.1}
\]

For one of the four carrier roles, the visible source/arrival set has size

\[
 v_0=m+Q+2.
 \tag{4.2}
\]

The union of the four visible sets has size \(v_0+1=m+Q+3\); each role
omits one of \(a,b,c,d\).  Put

\[
 L_1=\binom{m-Q-2}{H-Q-2},
 \qquad
 L_*=\binom{m-Q-3}{H-Q-3}.
 \tag{4.3}
\]

Here \(L_1\) is the number of carriers containing one role's visible set,
and \(L_*\) is the number containing the union of any two or more role
visible sets.

The exact number of ordered **distinct** carrier quadruples is

\[
 \boxed{
 \Lambda_Q
 =
 \sum_{\pi\in\Pi_4}
 \left[
 \prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\,L_{|B|}
 \right],}
 \tag{4.4}
\]

where \(L_{1}=L_1\) and \(L_j=L_*\) for \(j\ge2\).  This is Möbius
inversion on the partition lattice, excluding equality among carrier
roles.  Since \(L_1\to\infty\),

\[
 \Lambda_Q=L_1^4(1-o(1)).
 \tag{4.5}
\]

Every owner degree and higher owner codegree in Sections 2--3 is multiplied
by the same factor

\[
 A_Q\Lambda_Q.
 \tag{4.6}
\]

Thus all normalized owner overlaps are unchanged.

## 5. Carrier/tag and mixed overlaps

The total number of completed ordered packets is

\[
 G=G_{\rm skel}A_Q\Lambda_Q.
 \tag{5.1}
\]

Coordinate symmetry gives the exact one-tag degree

\[
 \boxed{
 d_{\rm tag}={4G\over N_H}.}
 \tag{5.2}
\]

There is a useful exact compatibility condition.  If \(j\) prescribed
carrier tags occupy \(j\) distinct roles of one packet, then their common
intersection must contain the common part of those role-visible sets:

\[
 \boxed{
 \left|\bigcap_{\nu=1}^jU_\nu\right|
 \ge m+Q+3-j,
 \qquad 1\le j\le4.}
 \tag{5.3}
\]

If (5.3) fails, the tag codegree is zero.

There is also an exact formula for every higher tag degree.  For a visible
set \(S\), let

\[
 \mathcal C(S)=\{U\in\tbinom{[2m]}M:S\subset U\}.
\]

For visible sets \(S_i\) indexed by a set \(I\), and a set \(D\) of already
prescribed distinct tags, put

\[
 \Phi_I((S_i);D)
 =\sum_{\pi\in\Pi(I)}
 \prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!
 \left(
 \binom{2m-|\cup_{i\in B}S_i|}{M-|\cup_{i\in B}S_i|}
 -\#\{U\in D:\cup_{i\in B}S_i\subset U\}
 \right).
 \tag{5.3a}
\]

Möbius inversion on equality partitions shows that \(\Phi_I\) is exactly
the number of injective choices \(V_i\in\mathcal C(S_i)\setminus D\).
Let \(\mathscr S_Q\) denote the ordered skeleton-chain objects counted by
\(G_{\rm skel}A_Q\), before carrier choices, and let
\(S_1(\sigma),\ldots,S_4(\sigma)\) be their four visible sets.  For distinct
prescribed tags \(U_1,\ldots,U_j\), their exact completed-packet codegree is

\[
\boxed{
 d_{\rm tag}(U_1,\ldots,U_j)
 =\sum_{\rho:[j]\hookrightarrow[4]}
  \sum_{\sigma\in\mathscr S_Q}
  \prod_{\nu=1}^j
  \mathbf1_{S_{\rho(\nu)}(\sigma)\subset U_\nu}\,
  \Phi_{[4]\setminus\rho([j])}
  ((S_i(\sigma));\{U_1,\ldots,U_j\}).}
 \tag{5.3b}
\]

For \(j=4\), the empty \(\Phi\) is one.  Formula (5.3b), together with
\(|S_i|=m+Q+2\) and \(|\cup_{i\in B}S_i|=m+Q+3\) for \(|B|\ge2\), is the
complete exact higher-overlap formula on the carrier side.

The exact mixed owner/target--tag formula is (5.3b) with the inner sum
restricted by the additional indicators that the prescribed middle owners
belong to \(K(\sigma)+\mathcal F\) and the prescribed rank-\(r\) targets
belong to \(K_r(\sigma)+\mathcal R\).  Thus no independence assumption is
being made between the skeleton and its tags.

Fixing one compatible tag leaves three asymptotically free carrier choices;
fixing \(j\) compatible tags leaves only \(4-j\).  Uniformly over all fixed
compatible tags,

\[
 {d_{\rm tag}^{(j)}\over d_{\rm tag}}
 \le
 m^{O(Q)}L_1^{-(j-1)}
 =o(1)
 \qquad(j\ge2).
 \tag{5.4}
\]

The last equality follows from

\[
 \log L_1=\Theta(H\log(m/H)),
 \qquad Q=o(H).
\]

The same argument treats mixed owner--tag overlaps.  Fixing owner geometry
costs the power \(m^{\kappa+e}\) from (3.5), while each additional carrier
tag costs one factor \(L_1\), up to \(m^{O(Q)}\) choices of visible-chain
positions.  Therefore every nontrivial normalized mixed overlap is \(o(1)\).

The tag hypergraph is locally clustered—compatible carriers have very large
intersection—but its completed-packet codegrees are still negligible
because fixing a tag removes an entire filler choice.

## 6. Balanced carrier slots

A standalone diamond block uses three consecutive state occurrences in
each of four carriers.  Clone every carrier tag into

\[
 b=\left\lfloor{2M\over7}\right\rfloor
\]

formal block slots.  A completed robust packet chooses one slot in each of
its four carrier tags and all fourteen vertices of \(K+\mathcal F\).  The
completed slot-packet count is

\[
 G_b=Gb^4.
\]

The exact owner degree is

\[
 d_{\rm own}
 ={14G_b\over W},
 \tag{6.1}
\]

whereas the exact slot degree is

\[
 d_{\rm slot}
 ={4G_b\over bN_H}.
 \tag{6.2}
\]

Since \(W/(MN_H)=1+o(1)\) and \(7b/(2M)=1+O(1/M)\),

\[
 \boxed{
 {d_{\rm slot}\over d_{\rm own}}
 ={2W\over7bN_H}=1+o(1).}
 \tag{6.3}
\]

Thus the augmented hypergraph is asymptotically regular and \(18\)-uniform
(fourteen robust owners and four slots), and has maximum normalized codegree
\(o(1)\) by Sections 3 and 5.

The slot degrees and all slot overlaps are exact consequences of the tag
formulas.  A fixed slot over tag \(U\) has degree

\[
 d_{\rm slot}(U)=b^3d_{\rm tag}(U),
 \tag{6.4}
\]

and \(j\) fixed slots over distinct tags \(U_1,\ldots,U_j\) have codegree

\[
 b^{4-j}d_{\rm tag}(U_1,\ldots,U_j).
 \tag{6.5}
\]

Two distinct slots over the same physical tag have codegree zero, since one
packet uses a carrier only once.  Owner--slot and target--slot overlaps are
obtained from the corresponding owner--tag and target--tag sums by the same
factor \(b^{4-j}\); hence every nontrivial normalized mixed overlap is
\(o(1)\).

## 7. Audited near-perfect static matching

For completeness, we record the exact rounding input rather than invoking
an unspecified random-packing principle.

### Lemma 7.1 (fixed-uniformity nibble)

Let \(\mathcal H_n\) be \(k\)-uniform hypergraphs, with fixed \(k\), on
\(N_n\) vertices.  Suppose every vertex has degree
\((1+o(1))d_n\), where \(d_n\to\infty\), and every pair codegree is
\(o(d_n)\).  Then \(\mathcal H_n\) has a matching leaving \(o(N_n)\)
vertices uncovered.

#### Proof audit

Write \(d=d_n\), \(\Delta_2\) for the maximum pair codegree, and
\(\rho=\Delta_2/d=o(1)\).  In one round, select every edge independently
with probability \(p=\eta/d\), where \(\eta>0\) is fixed and small, and
retain a selected edge only if no intersecting edge was selected.

For an edge \(e\), the number of other edges meeting it is

\[
 \sum_{x\in e}(d(x)-1)+O_k(\Delta_2)
 =kd(1+o(1)).
\]

Hence

\[
 \Pr(e\hbox{ is retained})
 =p(1-p)^{kd(1+o(1))}
 ={\eta\over d}e^{-k\eta}+o(d^{-1}).
 \tag{7.0}
\]

Retained edges through a fixed vertex are mutually exclusive, so summing
(7.0) over its \((1+o(1))d\) incident edges gives the uniform cover
probability

\[
 \eta e^{-k\eta}+o(1)
 \tag{7.0a}
\]

with no independence assumption.

Delete covered vertices and edges meeting them.  Condition now on a fixed
vertex \(x\) being uncovered; without this conditioning the common event
that \(x\) is covered would create a spurious \(\Theta(d^2)\) variance.
In the conditional second moment of its surviving degree, edge pairs whose
off-\(x\) selected-edge neighborhoods are disjoint cancel.  Pairs with an
off-\(x\) intersection contribute at most \(O_k(d\Delta_2)\), and the
diagonal contributes \(O_k(d)\).  Thus

\[
 \operatorname{Var}(D'(x)\mid x\hbox{ uncovered})
 =O_k(d+d\Delta_2)+o(d^2)=o(d^2).
 \tag{7.0b}
\]

The corresponding expectation is the deterministic survival-density
factor times \(d(x)\), up to \(o(d)\).  Chebyshev followed by averaging over
\(x\) shows that all but \(o(N_n)\) survivor vertices have the predicted
degree.  Delete those anomalous vertices.  Their total incident-edge count
is \(o(N_nd)\); Markov therefore shows that deleting them changes the degree
of all but another \(o(N_n)\) vertices by \(o(d)\).  Delete this second
exceptional set as well.  The same count, with two fixed vertices, preserves
the \(o(d)\) codegree bound on the remaining core.

Iterate \(R\) rounds.  For fixed \(R\), the uncovered density is at most

\[
 (1-\eta e^{-k\eta}+o(1))^R.
\]

For each fixed \(R\), the pruned exceptional sets over all rounds still have
size \(o(N_n)\).  First choose \(R\) so the displayed density is below an
arbitrary \(\varepsilon>0\), then let \(n\to\infty\), and finally take a
diagonal choice \(R=R(n)\to\infty\) slowly enough that every one-round
error remains \(o(1/R)\).  The union of retained edges is a matching and
leaves \(o(N_n)\) vertices. \(\square\)

Applying Lemma 7.1 to the \(18\)-uniform robust-owner--slot hypergraph gives:

### Theorem 7.2 (static eight-template near-factor)

There is a family of pairwise robust-owner-disjoint, slot-disjoint completed
eight-template packets of size

\[
 \boxed{
 \left(\frac1{14}-o(1)\right)W.}
 \tag{7.1}
\]

Its fourteen-owner unions cover all but \(o(W)\) middle owners and it uses
all but \(o(W)\) formal carrier slots.

#### Proof

The augmented vertex count is

\[
 W+bN_H
 =\left(\frac97+o(1)\right)W.
\]

A near-perfect matching therefore has

\[
 {W+bN_H\over18}-o(W)
 =\left(\frac1{14}-o(1)\right)W
\]

edges.  Sections 2--6 verify every hypothesis of Lemma 7.1. \(\square\)

Taking an arbitrary \((1/16-o(1))W\)-edge submatching gives enough static
capacity for the rectangular correction family.  The slack is positive at
the robust-packet level: \(W/14-W/16=W/112\).  It is not occurrence slack;
the exact occurrence ledger is recorded next.

## 8. Exact coefficient ledger and the chronology/interface gate

Theorem 7.2 is not yet a literal word theorem.  First, a robust packet
reserves fourteen possible owners but either sign actually visits only
twelve.  Second, a formal slot says only that one carrier participates in
one three-state block.  If two matched packets use successive slots of the
same carrier, the first packet's two-step endpoint need not equal the next
packet's source state.

Resetting every block would cost

\[
 (2Q+1)bN_H
 =\Theta(QW),
 \tag{8.1}
\]

which is coefficient-fatal.  Even an \(O(Q)\)-update flush connector
between blocks has the same order.

For the required number

\[
 g=\left(\frac1{16}-o(1)\right)W
 \tag{8.2}
\]

of correction directions, the four-carrier packets consume \(4g\) blocks,
hence \(12g=(3/4-o(1))W\) state occurrences.  The carriers contain
\((1+o(1))W\) state positions in total, so exactly

\[
 W-12g=\left(\frac14+o(1)\right)W
 \tag{8.3}
\]

positions remain for all connectors and nongadget motion.  After choosing a
sign in each gadget, exactly the same number of owners remains uncovered:

\[
 \underbrace{2g}_{\text{shadow owners}}
 +\underbrace{(W-14g)}_{\text{outside robust unions}}
 =W-12g.
 \tag{8.4}
\]

Thus there is no hidden positive-density loss, but there is also no hidden
positive-density reserve.  The exact missing statement is:

> **Productive square-tube completion \((\mathrm{PSTUBE}_8)\).**  
> A robust submatching of size \(g=(1/16-o(1))W\) can be signed and ordered
> inside its carriers so that the \(W-12g+o(W)\) remaining carrier-state
> positions form the connecting motion and hit, with \(o(W)\) collisions,
> the \(2g+W-14g=W-12g\) owners omitted by the signed gadget blocks.

The finite connector part of this statement is now solved in
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`.
Two common-departure updates take every complementary-triple endpoint
quartet to a fresh singleton-special source quartet, with one new
owner-simple intermediate per carrier.  This gives exactly four state
occurrences per carrier and one direction per four updates, hence the full
\(W/16\) throughput.  What remains of \((\mathrm{PSTUBE}_8)\) is the
global **committed tube near-factor**: choose whole transported tubes whose
sixteen-owner signed cells cover all but \(o(W)\) owners.  The transport
does not turn an arbitrary static block matching into such a tube factor.

An \(O(1)\)-length connector assertion alone is not enough: a positive
constant number of extra joining states per \(\Theta(W)\) blocks changes the
leading coefficient.  The joining states must be precisely the unused
quarter of the carrier state positions and must be useful, not supplementary.

The local owner geometry explains the difficulty.  A Johnson square cycle
has four source owners with common intersection of size \(m-1\), whereas
its four two-step endpoint owners have common intersection of size \(m-3\).
They cannot be the next square sources in the same normal form.  A
coefficient-one tube must alternate square normal forms or absorb the
reconfiguration inside the next useful block.

## 9. Sharp scale bound for every higher Johnson cycle

The higher-template alternative can be classified at coefficient scale
inside the same single-marked-cycle architecture.

### Theorem 9.1 (single-direction cycle ceiling)

Consider a coherent \(k\)-edge Johnson cycle of arrival diamonds.  Assume
its edge intersections are distinct, its edge unions are distinct, and one
edge is changed by a fresh adjacent chain swap so that the complete
coboundary leaves one nonzero marked rectangle; assume also the standard
disjoint role signatures separating source, intermediate, and endpoint
owners.  Then:

1. either sign has exactly \(3k\) distinct middle-owner occurrences;
2. the union of the two signs has exactly \(3k+2\) owners;
3. a sign-robust, owner-disjoint family of
   \((1/16-o(1))W\) such one-direction gadgets is possible only for
   \(k\le4\);
4. even a sign-committed family at that scale is possible only for
   \(k\le5\).

#### Proof

There are \(k\) common source owners and \(k\) common endpoint owners.
Distinct edge intersections and unions make each of these two lists
owner-simple.  Before perturbation, the positive and negative intermediate
lists are the same \(k\) Johnson-cycle vertices, merely cyclically shifted.

The perturbed edge replaces one old intermediate on each side.  Each new
intermediate contains the fresh swap label \(v\), whereas all \(k\) old
cycle intermediates contain \(u\) and not \(v\).  The two new intermediates
have different edge-role pairs, so they are distinct.  Hence the robust
intermediate union has size \(k+2\), proving

\[
 k+(k+2)+k=3k+2.
 \tag{9.1}
\]

At \(g=(1/16-o(1))W\), robust owner-disjointness requires

\[
 (3k+2)g\le W+o(W),
\]

so \(3k+2\le16\), hence \(k\le4\).  If signs are committed before
packing, the necessary occurrence bound is only \(3kg\le W+o(W)\), which
gives \(k\le5\). \(\square\)

Thus the eight-template square (\(k=4\)) is not merely locally minimal: it
is the **only** sign-robust single-rectangle Johnson-cycle template with
coefficient capacity at the \(W/16\) scale.  A ten-template five-cycle
(\(k=5\)) has seventeen robust owners per direction and misses capacity by
exactly

\[
 {17W\over16}-W={W\over16}.
 \tag{9.2}
\]

Every twelve-template cycle already uses eighteen actual occurrences per
direction and exceeds physical state capacity by \(W/8\).

Consequently, if \((\mathrm{PSTUBE}_8)\) is false, no larger
single-marked Johnson cycle can repair it.  The minimal coefficient-feasible
higher architecture must start with a ten-template five-cycle carrying at
least two marked correction rectangles per transport packet: one marked
direction per five-cycle is forbidden by (9.2), while two directions
introduce at most four fresh intermediates, hence at most
\(2\cdot5+(5+4)=19\) robust owners, or \(19/2<16\) per direction.  This
identifies the minimal possible escape architecture; it
does not prove the required two-mark positivity or target pairing.

## 10. Obstruction and minimal-template conclusion

One sign uses twelve owner occurrences for one correction direction, so the
raw occurrence ceiling is

\[
 {W\over12},
\]

strictly above the required \(W/16\) scale.  Sign-robust separation costs
fourteen reservations per direction and gives the smaller ceiling \(W/14\),
still strictly above \(W/16\).  The balanced robust slot count is
\(b=\lfloor2M/7\rfloor\).

Therefore:

1. there is no owner-degree, tag-degree, codegree, higher-overlap, or static
   packing obstruction to \((1/16-o(1))W\) eight-template packets;
2. there is an exact coefficient-scale interface obstruction to concluding
   coefficient one from that packing alone: two of every fourteen robust
   reservations are shadows, and all remaining \(W/4+o(W)\) carrier states
   must cover the complementary \(W/4+o(W)\) owners;
3. the owner-separated eight-template square is the minimal local template:
   four paths force a source/endpoint duplicate, and a six-path triangle
   forces one side of that duplicate;
4. it is also the only sign-robust single-direction Johnson cycle with
   enough coefficient capacity.  If its productive completion fails, the
   minimal possible higher escape is not a one-direction cycle but a
   ten-template five-cycle amortizing at least two marked corrections.

Thus the exact coefficient-one frontier is no longer a static random-packing
question.  The finite productive connector in Section 8 is now solved; the
frontier is the committed whole-tube owner near-factor described in the
transport note.
