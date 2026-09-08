# From the incidence-hexagon near-decomposition to a literal tube atlas

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Write

\[
 J=[2s],\qquad {\cal D}={\cal D}_s,\qquad
 B=C_s,\qquad c=C_{s-1},
\]

and

\[
 {\cal L}=\binom Js\setminus\overline{\cal D},
 \qquad {\cal Y}=\binom J{s+1},
 \qquad |{\cal L}|=|{\cal Y}|=sB.
\tag{0.1}
\]

The theorem in
`MATH_THEOREM_INCIDENCE_HEXAGON_NEAR_DECOMPOSITION_AND_COMPLETION_GATE_20260726.md`
packs

\[
                         \left(\frac13-o(1)\right)sB
\tag{0.2}
\]

vertex-disjoint geometric incidence hexagons. A pair-tube atlas covering
all but \(o(B)\) nonendpoint roots needs only

\[
                         2\frac{B-c-o(B)}3
                              =\left(\frac12+o(1)\right)B
\tag{0.3}
\]

hexagons: about \(B/4\) entrance routers and \(B/4\) inverse returns.
Thus the raw geometric count has a factor-\(\Theta(s)\) margin.

That margin does not survive the required projections automatically. This
note identifies the exact reason.

1. A usable router must be **phase-pure**: all three lower states lie in
   one synchronized layer. Vertex coverage controls only the first phase
   moment and gives no lower bound on the number of phase-pure packets.
2. Pair tubes require a second router on the **same transported strand
   triple**. The geometric near-decomposition controls state-vertex
   codegrees, not this transported-support codegree.
3. A tetrahedral closure is a common-neighbour condition in a strand-link
   graph. Again, the geometric state codegrees do not control it.
4. The frozen \(C_{s-1}\) endpoint corridor forces the packing to split
   into two blocks and prescribes \(C_{s-1}\) upper vertices which the
   inside hexagon packing must avoid.
5. Even after these conditions, the residual outgoing Hall system, the
   phasewise downward Hall systems, and identity monodromy of the leftover
   skeleton remain independent.

There is nevertheless a positive local result. Before the forced endpoint
roots are deleted, the root-pure phase-zero owner hypergraph has minimum
degree at least \(\binom s3\), while its owner-pair codegree is at most
\(s-1\). Thus root triangles have cubic local supply and vanishing relative
owner codegree. This bound need not survive an arbitrary choice of the
frozen endpoint set \(R_\infty\); robustly choosing that puncture is one of
the simultaneous packet constraints, together with upper resources,
label degrees, completion, and return support.

The exact combined gate is a repeated-support tube hypergraph. A
positive-density literal atlas follows from a matching in that hypergraph
together with the two Hall systems. The existing six-uniform nibble does
not prove such a matching, because its degree/codegree hypotheses are on
the wrong vertex set.

## 1. Corridor filtering comes before phase packing

Fix

\[
 R_\infty=\{P\in{\cal D}:b_1(P)=2s\},
 \qquad |R_\infty|=c.
\tag{1.1}
\]

Put

\[
\begin{aligned}
 {\cal X}_\infty&=\{X:\{1,2s\}\subset X,\ |X|=s\},\\
 {\cal Y}_\infty&=\{Y:\{1,2s\}\subset Y,\ |Y|=s+1\}.
\end{aligned}
\tag{1.2}
\]

Every extendable outgoing matching satisfies the tight cut

\[
 g({\cal X}_\infty\dot\cup R_\infty)={\cal Y}_\infty.
\tag{1.3}
\]

The \(c\) root edges

\[
                         P\longmapsto P\cup\{2s\}
                         \qquad(P\in R_\infty)
\tag{1.4}
\]

are frozen. Hence the remaining inside matching has shores

\[
 {\cal X}_\infty,qquad
 {\cal Y}_\infty\setminus
       \{P\cup\{2s\}:P\in R_\infty\},
\tag{1.5}
\]

both of size \((s-1)c\). Every switchable hexagon lies wholly inside
(1.3) or wholly outside it.

The unpunctured inside hexagon system still has the full cubic geometric
scale. For \(X\in{\cal X}_\infty\), its inside degree is exactly

\[
                         (s-2)\binom s2.
\tag{1.6}
\]

Indeed the core is \(X-x\) for one of the \(s-2\) nonendpoint elements
\(x\in X\setminus\{1,2s\}\), and the other two petals are any two of the
\(s\) elements outside \(X\). Every such core contains \(1\), so it is
ballot-eligible.

For \(Y\in{\cal Y}_\infty\), its inside degree is exactly

\[
                         (s-1)\binom{s-1}2.
\tag{1.7}
\]

Choose the two removed nonendpoint petals from
\(Y\setminus\{1,2s\}\), then choose the third petal outside \(Y\).

Thus the corridor does not create a raw cubic-degree deficit. The exact
difficulty is the prescribed puncture in (1.5): the full near-decomposition
theorem does not say that its matching can leave exactly those \(c\) upper
vertices unused. This is a genuine constrained-matching cut, not a scalar
capacity issue.

Already at the outgoing-edge level the inside block must satisfy

\[
 |N(A)\cap({\cal Y}_\infty\setminus Y(R_\infty))|\ge|A|
 \qquad(A\subseteq{\cal X}_\infty),
\tag{1.8}
\]

where \(Y(R_\infty)=\{P\cup\{2s\}:P\in R_\infty\}\). Failure of (1.8)
is the exact frozen-corridor Hall obstruction.

## 2. Phase purity is a third-order moment

Let

\[
                         {\cal L}=L_0\dot\cup\cdots\dot\cup L_{s-1},
 \qquad |L_t|=B,
\tag{2.1}
\]

be synchronized lower layers, with \(L_0={\cal D}\). For a geometric
hexagon \(e\), let

\[
                         n_t(e)=|X(e)\cap L_t|.
\tag{2.2}
\]

A hexagon is usable as a phase-\(t\) router precisely when
\(n_t(e)=3\). For a geometric matching \({\cal M}\), the number of such
routers is

\[
                         R_t({\cal M})
                              =\sum_{e\in{\cal M}}\binom{n_t(e)}3.
\tag{2.3}
\]

By contrast, near-perfect lower-shore coverage gives only

\[
                         \sum_{e\in{\cal M}}n_t(e)=B-o(B).
\tag{2.4}
\]

### Proposition 2.1 (phase-moment gap)

Equation (2.4) implies no positive lower bound on (2.3). In particular,
the full near-decomposition theorem does not imply even one phase-zero
router.

#### Proof

The integers \(n_t(e)\) lie in \(\{0,1,2,3\}\). A sum of
\(B-o(B)\) in (2.4) can be realized with every nonzero term equal to one,
while then every summand in (2.3) is zero. The near-decomposition theorem
records vertex coverage and has no further phase statistic. \(\square\)

This is a logical nonimplication, not a proof that the particular
incidence hypergraph lacks a phase-pure matching. The next section shows
that the phase-zero restriction in fact retains large local degree.

## 3. Exact phase-star degrees

For any layer \(L_t\) and \((s-1)\)-core \(K\), put

\[
                         d_t(K)=|\{a\notin K:K+a\in L_t\}|.
\tag{3.1}
\]

Let \({\cal R}_t\) be the 3-uniform hypergraph on \(L_t\) whose edges are
the lower shores of ballot-eligible phase-pure hexagons.

### Proposition 3.1 (exact owner degree and codegree)

For \(X\in L_t\),

\[
 d_{{\cal R}_t}(X)
   =\sum_{\substack{K\subset X,\ |K|=s-1\\K\ \mathrm{eligible}}}
        \binom{d_t(K)-1}{2}.
\tag{3.2}
\]

For distinct \(X,X'\in L_t\), the codegree is zero unless
\(X\cap X'=K\) has size \(s-1\) and is eligible; in that case

\[
                         \lambda_t(X,X')=d_t(K)-2\le s-1.
\tag{3.3}
\]

#### Proof

If \(K=X-x\) is the packet core, the other two lower vertices may be any
two of the remaining \(d_t(K)-1\) extensions in the layer. This gives
(3.2). Two distinct lower vertices determine their common core and leave
only the third extension to choose, giving (3.3). \(\square\)

For the root layer \(L_0={\cal D}\), these degrees have a uniform cubic
lower bound.

### Lemma 3.2 (deleting the \(i\)-th up-step creates at least \(i\) roots)

Let \(P\in{\cal D}\), let \(u_i\) be the position of its \(i\)-th
up-step, and put \(K_i=P\setminus\{u_i\}\). Then

\[
                         d_0(K_i)\ge i.
\tag{3.4}
\]

#### Proof

Changing the up-step at \(u_i\) to a down-step leaves all earlier heights
unchanged and lowers every later height by two. Hence the deficient path
of \(K_i\) is nonnegative before \(u_i\) and never below \(-2\). Let
\(a\) be its first down-step ending below zero. Flipping any down-step at
or before \(a\) to an up-step produces a nonnegative balanced path: the
prefix before the flipped step is nonnegative, while the later suffix is
raised by two from a path bounded below by \(-2\).

The first negative step occurs after \(u_i\). At that time the deficient
prefix has one more down-step than up-step and at least \(i-1\) up-steps.
It therefore contains at least \(i\) down-steps. These give at least \(i\)
distinct Dyck extensions of \(K_i\). \(\square\)

### Corollary 3.3 (cubic phase-zero owner supply)

Every root belongs to at least

\[
 \sum_{i=3}^s\binom{i-1}{2}=\binom s3
\tag{3.5}
\]

root-pure hexagon lower shores, while every root pair has codegree at most
\(s-1\). Thus

\[
 \delta({\cal R}_0)\ge\binom s3,
 \qquad
 \Delta_2({\cal R}_0)\le s-1=o(s^3).
\tag{3.6}
\]

#### Proof

Apply (3.2) to the cores \(K_i\) and use (3.4). Every \(K_i\) with
\(i\ge3\) contains coordinate \(1\). Every extension of \(K_i\) therefore
contains \(1\), whereas every barred Dyck port omits \(1\); hence \(K_i\)
is ballot-eligible. Formula (3.3) gives the codegree. \(\square\)

This is an unpunctured statement. Put

\[
 d_0^{V_0}(K)=|\{a:K+a\in{\cal D}\setminus R_\infty\}|.
\tag{3.6a}
\]

After freezing the endpoint roots, the exact remaining degree of
\(P\in V_0\) is

\[
 d_{{\cal R}_0[V_0]}(P)
   =\sum_{\substack{K\subset P,\ |K|=s-1\\K\ \mathrm{eligible}}}
        \binom{d_0^{V_0}(K)-1}{2}.
\tag{3.6b}
\]

The bound (3.6) gives no lower bound for (3.6b) under an arbitrary
\(c\)-set deletion: all alternative extensions of the useful cores of one
surviving root could lie in \(R_\infty\). Therefore the endpoint-root set
must itself be chosen inside the augmented packet matching so that almost
all surviving roots retain large punctured degree. Treating
\(R_\infty\) as an arbitrary scalar quota is insufficient.

There is a useful weighted regularization. Give every root triangle with
core \(K\) weight

\[
                         \omega_K=\binom{d_0(K)-1}{2}^{-1}.
\tag{3.7}
\]

Its weighted degree at a root is the number of its cores with
\(d_0(K)\ge3\), hence lies between \(s-2\) and \(s\). The weighted
codegree of a root pair with common core \(K\) is

\[
                         (d_0(K)-2)\omega_K
                              ={2\over d_0(K)-1}\le1.
\tag{3.8}
\]

So the owner-only root hypergraph has an almost-regular fractional scale
and vanishing relative weighted codegree. This still does not prove the
augmented packet matching: upper-state collisions and the prescribed
Catalan petal degrees are absent from \({\cal R}_0\).

Those label degrees obey the exact packet lattice. If \(Z\) is the set of
unpacked nonendpoint roots and \(d^{\rm hex}(S)\) is the total petal degree
on \(S\subseteq J\), then every phase-zero packet family satisfies

\[
 \sum_{P\in({\cal D}\setminus R_\infty)\setminus Z}|P\cap S|
       -d^{\rm hex}(S)
 =3\sum_{p}|K(p)\cap S|.
\tag{3.9}
\]

Thus the left side must be nonnegative and divisible by three for every
\(S\). In particular the Catalan target cannot be imposed after the
owner-only nibble; it must be part of the augmented packet matching from
the start, together with the explicit leftover label ledger.

## 4. Repeated transported support is the missing codegree

Complete a geometric outgoing matching and downward matching into
synchronized abstract paths. For a phase-pure, strand-admissible router
\(e\), let

\[
                         \operatorname{supp}(e)
                              \in\binom{{\cal D}}3
\tag{4.1}
\]

be its three transported root-strand labels. For a router family
\({\cal Q}\), put

\[
                         \mu_{\cal Q}(T)
   =|\{e\in{\cal Q}:\operatorname{supp}(e)=T\}|.
\tag{4.2}
\]

The maximum number of support-disjoint inverse pairs which can be formed
inside \({\cal Q}\), before checking orientation, is

\[
                         \sum_T\left\lfloor
                                  {\mu_{\cal Q}(T)\over2}\right\rfloor.
\tag{4.3}
\]

For a fixed strand triple \(T\), there is at most one candidate outgoing
hexagon in each phase: the three lower states determine their common core
and hence the hexagon. The one-phase return obstruction excludes the phase
immediately following an entrance router. Therefore a phase-zero router
has at most \(s-2\) possible same-support return phases.

### Theorem 4.1 (state codegree does not control return codegree)

The degree and pair-codegree estimates of the six-uniform geometric
hypergraph give no lower bound on (4.3). In particular they do not imply
the return-router Hall condition.

#### Proof

The geometric estimates count packets sharing a lower or upper **state**.
Distinct phases on the same strand triple use disjoint states, so their
geometric state codegree is zero. Conversely, two geometric packets with
large state-neighbourhood overlap need not lie on the same three completed
strands. The map from states to transported strand labels depends on the
global \(g/h\) completion and is absent from the six-uniform hypergraph.

It is therefore consistent with all stated geometric degree and codegree
bounds that every usable router has a distinct support \(T\), in which
case every \(\mu_{\cal Q}(T)=1\) and (4.3) is zero. No inequality in the
near-decomposition theorem excludes this support profile. \(\square\)

For a prepacked family of disjoint phase-zero routers, the support triples
are disjoint. Once an internal router bank is also part of one outgoing
perfect matching, a return router can be adjacent to only the unique
entrance router with the same support. Thus the pair-return Hall graph is
a disjoint union of stars, and its Hall condition reduces to the exact
pointwise requirement

\[
 \boxed{
 \text{every selected entrance support }T
 \text{ has an oppositely oriented return router.}}
\tag{4.4}
\]

The full near-decomposition theorem supplies no lower bound for the left
side of (4.4).

## 5. Tetrahedral closure is a strand-link codegree

Let \({\cal S}_{\rm int}\subseteq\binom{{\cal D}}3\) be the support
hypergraph of the available internal routers, retaining orientation tags.
For a strand \(p\in{\cal D}\), define its link graph \(L_p\) on the other
strands by

\[
                         qr\in E(L_p)
       \quad\Longleftrightarrow\quad
                         \{p,q,r\}\in{\cal S}_{\rm int}.
\tag{5.1}
\]

An entrance router on \(\{p,q,r\}\) has a tetrahedral closure with hub
\(p\) exactly when there is a strand \(d\) for which

\[
                         qd,rd\in E(L_p)
\tag{5.2}
\]

with the two orientation tags required by

\[
                         (p\ q\ r)(p\ d\ q)(p\ r\ d)=1.
\tag{5.3}
\]

Thus the tetrahedral supply is the common-neighbour codegree

\[
                         |N_{L_p}(q)\cap N_{L_p}(r)|.
\tag{5.4}
\]

The six-uniform near-decomposition theorem controls none of the link
graphs \(L_p\), because their vertices are completed path strands rather
than geometric states. It therefore gives no lower bound on (5.4).

Moreover, strand-disjoint tetrahedral tubes cannot form a near-perfect
entrance atlas: any two faces of a tetrahedron share two strands, so at
most one is a phase-zero packet. Four strands then support only three
phase-zero owners, leaving at least one quarter of the nonendpoint roots
outside phase-zero packets. A coefficient-one tetrahedral construction
would have to use an overlapping global link complex and audit its
noncommuting total monodromy.

## 6. The two Hall systems remain independent

Let \({\cal M}\) be a cut-respecting, phase-pure packet family, and choose
one alternating half of each packet. Let \(Q\) be the resulting partial
outgoing matching in the incidence graph \(G_s\) between \({\cal L}\) and
\({\cal Y}\). It extends to an outgoing perfect matching if and only if

\[
 |N_{G_s-V(Q)}(A)|\ge|A|
 \qquad(A\subseteq{\cal L}\setminus V(Q)),
\tag{6.1}
\]

where the neighbourhood is taken in the residual incidence graph. This
is the first Hall system.

After an outgoing completion \(g\), put \(U_t=g(L_t)\). A phase-respecting
downward completion exists if and only if

\[
 |N(A)\cap L_{t+1}|\ge|A|
 \qquad(A\subseteq U_t, 0\le t<s).
\tag{6.2}
\]

This is the second Hall system. If it holds, the resulting paths have equal
length, but their endpoint permutation still need not be identity.

The geometric matching theorem proves neither (6.1) nor (6.2). Orienting
or pairing its hexagons does not change their consumed vertex sets, so it
cannot repair a Hall cut caused by those sets. Closed tubes remove the
monodromy of their own router blocks, but they also do not repair a
nonidentity endpoint permutation in the leftover skeleton.

## 7. The combined tube-atlas hypergraph

The exact object needed for a literal pair-tube atlas is not the original
six-uniform hypergraph. Define \({\mathfrak T}_s\) as follows.

A tube packet records:

1. one phase-zero root-pure hexagon outside the endpoint corridor;
2. one phase-\(t\) hexagon, \(2\le t<s\), on the same transported strand
   triple and with inverse orientation;
3. three pairwise disjoint, phase-increasing collar linkages certifying
   that the two hexagons lie on the same transported strands;
4. all lower and upper resources on the two routers and the three collar
   linkages;
5. the three entrance petal labels;
6. the phase and strand-support tags; and
7. the residual outgoing and downward boundary ports needed by the two
   Hall completions.

Two tube packets conflict when any recorded ownership resource, root,
upper state, collar state, label quota slot, or boundary port conflicts. A
matching of \({\mathfrak T}_s\) of size

\[
                         {B-c-o(B)\over3}
                              =\left(\frac14+o(1)\right)B
\tag{7.1}
\]

which meets the Catalan petal degrees and leaves residual graphs satisfying
(6.1)--(6.2) gives a positive-density literal tube atlas, provided the
leftover skeleton has identity endpoint matching.

### Theorem 7.1 (conditional literal atlas compiler)

Such a matching in \({\mathfrak T}_s\), together with an identity
leftover skeleton, produces an exact anchored \({\cal D}_s\)-port factor
with the Catalan entrance quotas and
\((1/4-o(1))B\) pairwise resource-disjoint closed pair tubes.

#### Proof

The phase-zero packet resources give distinct nonendpoint roots and the
prescribed petal degrees. The frozen edges (1.4) supply exactly the forced
\(2s\)-load. The recorded collar linkages make the repeated strand support
literal rather than a post-completion tag. The residual Hall systems
complete the two incidence matchings. Each tube's two transported
3-cycles are inverse, so its total monodromy is identity. The leftover
skeleton is identity by hypothesis. Every resulting row has \(s\) Johnson
steps from a root to its own complement, and is therefore geodesic. Since
the tube packet records every collar resource and the two global matchings
exhaust the residual shores, every crossing-collar state and colour has
load one.
\(\square\)

This theorem uses no owner-dependent exterior motion: only the whole
identity-monodromy tube is installed. An individual open router is not a
physical slab.

The collar data changes the packing regime. A tube whose return occurs in
phase \(t\) contains \(\Theta(t)\) state resources, so
\({\mathfrak T}_s\) has growing rather than fixed uniformity. Two tube
candidates can also share a long forced collar subpath. Therefore the
six-uniform degree/codegree estimate and fixed-uniformity nibble from the
geometric theorem cannot be applied to \({\mathfrak T}_s\). A positive
atlas theorem needs new path-packet codegree bounds after the forced
collars are included.

## 8. Exact codegree/cut obstruction

The near-decomposition theorem for the original geometric hypergraph does
not imply the hypothesis of Theorem 7.1. The missing estimates are exactly:

1. a near-perfect augmented phase-zero packet matching with the Catalan
   label degrees and the corridor puncture (1.5);
2. a positive lower bound on the repeated-support degree

   \[
               \rho(T)=|\{t\in\{2,\ldots,s-1\}:
                   T\text{ supports an inverse phase-}t\text{ router}\}|;
   \tag{8.1}
   \]

3. or, for tetrahedral closure, a positive lower bound on the link
   codegrees (5.4);
4. bounded congestion and codegrees for the three collar linkages which
   realize each support repetition;
5. the residual Hall inequalities (6.1)--(6.2); and
6. identity endpoint matching for the leftover skeleton.

The sharp pair-tube cut is

\[
 \boxed{
   \#\{T\text{ selected at phase zero}:\rho(T)=0\}=o(B).}
\tag{8.2}
\]

For a coefficient-scale atlas the stronger matching version must hold
after resource conflicts, but (8.2) is already necessary. The original
degree \(\Theta(s^3)\) and codegree \(O(s^2)\) census says nothing about
\(\rho(T)\): it is a codegree after quotienting by completed path strands,
not a codegree of geometric state vertices.

Therefore the \((s/3-o(s))B\) geometric packets cannot presently be
oriented or paired into a positive-density literal tube atlas. This is not
a proof that such an atlas does not exist. It is an exact identification
of the missing theorem: a completion-aware repeated-support estimate for
\({\mathfrak T}_s\), simultaneously respecting the endpoint corridor,
Catalan petal degrees, and both residual Hall systems.
