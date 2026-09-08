# Coefficient-accurate extraction from the corrected fractional chunk point

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let \(x\) be the corrected rational protected-chunk point on \(T\) tags.
Assume

\[
 \sum_{e:\tau(e)=U}x_e\leq1,
 \qquad
 \sum_U\left(1-\sum_{e:\tau(e)=U}x_e\right)=\beta T,
 \tag{0.1}
\]

and every protected target has \(x\)-load at most one.  Thus \(\beta\)
is the **average fractional tag deficit**, including both discarded tags
and the common shrinkage used to make all target loads pointwise at most
one.

Clear the denominators by \(D\), so that edge type \(e\) has integral
multiplicity \(m_e=Dx_e\).  If this demand multihypergraph has a rational
fractional edge-colour cover of cost

\[
 C\leq(1+\varepsilon)D,
 \tag{0.2}
\]

then, after one further common rational clearing, it has an integral
matching colour which misses at most

\[
 \boxed{
  {\varepsilon+\beta\over1+\varepsilon}\,T
 }
 \tag{0.3}
\]

tags.  There is no hidden denominator or ceiling loss in (0.3).

If a missed chunk tag can cost at most \(K\leq(2Q+1)g\) literal
protected claims and \(gT=(1+o(1))W\), then the omitted-claim ledger is at
most

\[
 (2Q+1)(1+o(1))
 {\varepsilon+\beta\over1+\varepsilon}W.
 \tag{0.4}
\]

Therefore the full-colour averaging route is coefficient-safe under the
sharp aggregate requirement

\[
 \boxed{\varepsilon+\beta=o(1/Q).}
 \tag{0.5}
\]

The corrected isolated-pruning point supplies \(\beta=o(1/Q)\).  The
remaining unproved fractional-colouring gate is consequently
\(\varepsilon=o(1/Q)\), not merely \(o(1)\).

The relevant matching-cover inequality is weighted by this particular
point \(x\).  An unweighted clique in the support is harmless if its total
\(x\)-mass is small.  In particular, a fixed loose triangle has mass at
most \(3\|x\|_\infty\).  However diffuseness alone does not close the
gate: there is an arbitrarily diffuse three-bundle loose triangle with
tag deficit zero, target loads exactly one, and fractional colour cost
at least \(3/2\).  Projective-plane singleton families give the analogous
larger weighted cut.  Thus one must rule out *weighted overlap-cycle mass*,
not merely heavy individual chunks.

No coefficient-one conclusion is claimed: the required weighted
matching-cover inequality for the actual geodesic point is still open.

## 1. Correct rational clearing

Let \({\cal T}\) be a set of \(T\) tags, \({\cal V}\) the protected
targets, and \({\cal E}\) the finite set of legal chunk types.  Every
\(e\in{\cal E}\) has one tag \(\tau(e)\) and a protected claim set
\(C(e)\subseteq{\cal V}\).

Let \(x_e\in\mathbb Q_{\geq0}\).  Put

\[
 s_U:=\sum_{e:\tau(e)=U}x_e,
 \qquad
 \ell_v:=\sum_{e:v\in C(e)}x_e.
 \tag{1.1}
\]

Assume

\[
 0\leq s_U\leq1,
 \qquad
 \ell_v\leq1,
 \qquad
 \sum_U(1-s_U)=\beta T.
 \tag{1.2}
\]

It follows exactly that

\[
 \sum_e x_e=\sum_Us_U=(1-\beta)T.
 \tag{1.3}
\]

Choose a common denominator \(D\) and put

\[
 m_e=Dx_e\in\mathbb Z_{\geq0}.
 \tag{1.4}
\]

The resulting demand multihypergraph has

\[
 d(U)=Ds_U\leq D,
 \qquad
 d(v)=D\ell_v\leq D,
 \tag{1.5}
\]

and its total number of occurrence edges is

\[
 \boxed{\sum_em_e=D(1-\beta)T.}
 \tag{1.6}
\]

For the corrected isolated-pruning point, if \({\cal T}'\) is the good
tag set and every good tag has mass \(\rho\), then

\[
 \beta
 ={T-|{\cal T}'|\over T}
  +{|{\cal T}'|\over T}(1-\rho).
 \tag{1.7}
\]

Hence

\[
 T-|{\cal T}'|=o(T/Q),\qquad1-\rho=o(1/Q)
 \tag{1.8}
\]

imply \(\beta=o(1/Q)\) with no uniformity assumption on the exceptional
tags.

## 2. Exact scaled factorization and extraction

Let \(\mathfrak M\) be the family of matchings of the underlying
tag--target hypergraph.  A fractional edge-colour cover of the integral
demand \(m=(m_e)\) is a family of rational numbers
\(\lambda_M\geq0\) satisfying

\[
 \sum_{M\ni e}\lambda_M\geq m_e
 \qquad(e\in{\cal E}).
 \tag{2.1}
\]

Its cost is

\[
 C=\sum_{M\in\mathfrak M}\lambda_M.
 \tag{2.2}
\]

### Theorem 2.1 (coefficient-accurate colour extraction)

Under (1.2), suppose (2.1) has rational cost

\[
 C\leq(1+\varepsilon)D,
 \qquad \varepsilon\geq0.
 \tag{2.3}
\]

There is an integer \(L\geq1\) such that the \(L\)-fold demand has an
integral proper edge-colouring, and one of its colours meets at least

\[
 \boxed{{1-\beta\over1+\varepsilon}T}
 \tag{2.4}
\]

distinct tags.  Consequently it misses at most the quantity in (0.3).

#### Proof

Choose \(L\) clearing all denominators of the \(\lambda_M\).  Create
\(L\lambda_M\) colour slots of matching type \(M\).

For a fixed edge type \(e\), at least

\[
 \sum_{M\ni e}L\lambda_M\geq Lm_e
\]

slots contain \(e\).  Assign its \(Lm_e\) labelled occurrence copies
injectively to any \(Lm_e\) such slots and delete \(e\) from all surplus
slots.  Do this separately for every edge type.  Deletion preserves the
matching property, so the result is an exact integral colouring of every
occurrence copy.

By (1.6), the number of coloured occurrences is

\[
 LD(1-\beta)T.
\]

The number of colour slots is \(LC\).  Hence some slot has at least their
average number

\[
 {LD(1-\beta)T\over LC}
 \geq{1-\beta\over1+\varepsilon}T
\]

of edges.  A matching uses at most one edge on a tag, so these edges meet
the same number of distinct tags.  Subtracting from \(T\) gives

\[
 T-{1-\beta\over1+\varepsilon}T
 ={\varepsilon+\beta\over1+\varepsilon}T.
\]

This proves both assertions. \(\square\)

The proof actually gives, for arbitrary positive cost \(C\), the exact
bound

\[
 T-|M|\leq
 \left(1-{D(1-\beta)\over C}\right)T.
 \tag{2.5}
\]

Thus (0.3) is not an asymptotic expansion; it is the literal average.

## 3. Exact coefficient ledger

Assume one tag represents a chunk of \(g\) physical middle owners and at
most \(K\) protected claims, where

\[
 gT=(1+o(1))W,
 \qquad
 K\leq(2Q+1)g.
 \tag{3.1}
\]

Put

\[
 r={\varepsilon+\beta\over1+\varepsilon}T.
 \tag{3.2}
\]

The missed middle-owner mass is bounded by

\[
 gr
 ={\varepsilon+\beta\over1+\varepsilon}(1+o(1))W,
 \tag{3.3}
\]

while literal repair of every protected claim on every missed tag is
bounded by

\[
\begin{aligned}
 Kr
 &\leq(2Q+1)g
       {\varepsilon+\beta\over1+\varepsilon}T\\
 &= (2Q+1)(1+o(1))
       {\varepsilon+\beta\over1+\varepsilon}W.
\end{aligned}
 \tag{3.4}
\]

Thus (0.5) makes both quantities \(o(W)\).  Conversely, from only the
worst-case per-tag repair bound \(K=\Theta(Qg)\), averaging cannot certify
an \(o(W)\) repair unless

\[
 Q{\varepsilon+\beta\over1+\varepsilon}=o(1).
 \tag{3.5}
\]

Since \(\varepsilon\geq0\), condition (3.5) is equivalent to (0.5).
This is a requirement of the coefficient-accurate *aggregate extraction
argument*; a separate structured reserve theorem could conceivably repair
a larger leave more cheaply.

The start/reset cost for at most \(T\) selected chunks is still

\[
 O(QT)=O(QW/g)=o(W)
 \tag{3.6}
\]

under the audited assumption \(Q=o(g)\).

## 4. The exact weighted matching-cover gate for \(x\)

Define the normalized fractional edge-colour cost of the rational point by

\[
 \chi_f'(x)
 :=\min\left\{
   \sum_{M\in\mathfrak M}\theta_M:
   \theta_M\geq0,\quad
   \sum_{M\ni e}\theta_M\geq x_e
   \ (e\in{\cal E})
 \right\}.
 \tag{4.1}
\]

Scaling gives exactly

\[
 \chi_f'(m)=D\chi_f'(x).
 \tag{4.2}
\]

### Proposition 4.1 (point-specific weighted dual)

\[
 \boxed{
 \chi_f'(x)
 =\sup_{\substack{y\geq0\\y\ne0}}
 {\sum_ex_ey_e\over
  \max_{M\in\mathfrak M}\sum_{e\in M}y_e}.}
 \tag{4.3}
\]

Consequently the exact remaining fractional gate is

\[
 \boxed{
 \sum_ex_ey_e
 \leq\bigl(1+o(1/Q)\bigr)
       \max_{M\in\mathfrak M}\sum_{e\in M}y_e
 \quad(y\geq0).}
 \tag{4.4}
\]

#### Proof

The dual of (4.1) maximizes \(\sum_ex_ey_e\) subject to

\[
 y_e\geq0,
 \qquad
 \sum_{e\in M}y_e\leq1
 \quad(M\in\mathfrak M).
\]

Finite-dimensional linear-programming duality applies.  Normalizing an
arbitrary nonzero \(y\) by
\(\max_M\sum_{e\in M}y_e\) gives (4.3), and (4.4) is precisely
\(\chi_f'(x)\leq1+o(1/Q)\). \(\square\)

The tag and target capacity inequalities in (1.2) verify (4.4) only for
dual weights supported on incidence stars.  They say nothing about a
general matching-polytope dual vector.

## 5. Finite loose triangles are harmless only because their mass is small

Call \(F\subseteq{\cal E}\) intersecting if every matching contains at
most one member of \(F\).  Equivalently, all pairs of edges in \(F\)
intersect.

### Lemma 5.1 (weighted intersecting-family cut)

For every intersecting \(F\),

\[
 \boxed{\chi_f'(x)\geq x(F):=\sum_{e\in F}x_e.}
 \tag{5.1}
\]

Moreover every dual vector supported on \(F\) has quotient in (4.3) at
most \(x(F)\).

#### Proof

Take \(y_e=1\) on \(F\) and zero elsewhere.  Its matching denominator is
one, proving (5.1).  Conversely, for arbitrary \(y\) supported on \(F\),
the denominator is \(\max_{e\in F}y_e\).  Hence

\[
 {\sum_{e\in F}x_ey_e\over\max_{e\in F}y_e}
 \leq\sum_{e\in F}x_e=x(F).
\]

\(\square\)

If \(F\) contains at most \(b\) support edges and
\(\|x\|_\infty\leq\eta\), then

\[
 x(F)\leq b\eta.
 \tag{5.2}
\]

More strongly, for an arbitrary dual vector \(y\geq0\), not necessarily
supported on \(F\), write

\[
 A(y):=\max_{M\in\mathfrak M}\sum_{e\in M}y_e.
\]

Since every singleton edge is itself a matching,
\(A(y)\geq\max_e y_e\).  Therefore

\[
 \boxed{
 {\sum_{e\in F}x_ey_e\over A(y)}
 \leq b\eta.}
 \tag{5.3}
\]

Thus a fixed family contributes at most \(b\eta\) additively to **every**
weighted matching cut, even when coupled to a large dual carrier outside
\(F\).

Thus a single three-edge loose triangle has total mass at most \(3\eta\).
When \(\eta=o(1/Q)\), it cannot by itself violate (4.4).  Clearing
denominators does not change this conclusion: its total occurrence
multiplicity is \(Dx(F)\), and the normalizing colour scale is \(D\).

For the corrected uniform good-tag point,
\(\eta\leq(1+o(1))/\mu\).  In the audited pointwise pruning choice,
\(\mu=m^{11/6-o(1)}\) and \(Q=m^{1/2+o(1)}\), so
\(\eta=o(1/Q)\).  Hence every bounded collection
of loose triangles is coefficient-negligible by (5.3).  A number of
support paths growing on the scale \(1/\eta\) can still carry constant
dual mass, as the next theorem shows.

This is the precise sense in which a **finite** loose triangle is harmless
for a diffuse point.  It does not justify ignoring a large family with the
same overlap pattern.

## 6. An arbitrarily diffuse weighted loose-triangle obstruction

### Theorem 6.1 (diffuseness does not imply the weighted cut)

For every \(K\geq2\) and every \(\eta>0\), there is a rational abstract
chunk-incidence point \(x\) such that

1. \(\|x\|_\infty\leq\eta\);
2. every tag has load exactly one, so \(\beta=0\);
3. every target has load at most one;
4. every two protected claim sets intersect in at most two targets; but
5. \(\chi_f'(x)\geq3/2\).

The construction may be replicated on arbitrarily many tags while
preserving all five assertions.

#### Proof

Choose \(r\) so that

\[
 {1\over2r}\leq\eta.
\]

Use three tags \(\tau_{ab},\tau_{bc},\tau_{ca}\) and three core targets
\(a,b,c\).  Above \(\tau_{ab}\), take \(r\) distinct core chunks claiming
\(\{a,b\}\), and \(r\) filler chunks with mutually private claims.  Give
each of these \(2r\) chunks weight \(1/(2r)\).  Construct the analogous
families above \(\tau_{bc}\) and \(\tau_{ca}\), using core pairs
\(\{b,c\}\) and \(\{c,a\}\).  Pad every chunk to exactly \(K\) protected
claims by private targets.

Every tag has \(2r\) chunks of weight \(1/(2r)\), hence load one.  Target
\(a\) has load \(1/2+1/2=1\), and similarly for \(b,c\); private targets
have load \(1/(2r)\).  Protected intersections have size zero, one, or
two.

Let \(F\) be the union of the \(3r\) core chunks.  It is intersecting:
chunks above one core tag share its two core targets, while chunks above
different core tags share the appropriate one of \(a,b,c\).  Its total
weight is

\[
 x(F)=3r\cdot{1\over2r}={3\over2}.
\]

Lemma 5.1 gives \(\chi_f'(x)\geq3/2\).  Disjoint replication gives any
desired number of blocks and tags; putting the same dual weight on every
block preserves the quotient \(3/2\). \(\square\)

After clearing any denominator \(D\) divisible by \(2r\), this example
has tag degree exactly \(D\), core target degree exactly \(D\), and
fractional edge-colour cost at least \(3D/2\).  Thus no atom-size or
entropy argument can replace the weighted cycle cut.

## 7. Singleton/projective-plane cuts at the corrected point

Let \(F\) be the line family of a projective plane of order \(q\).  It has

\[
 |F|=q^2+q+1,
 \qquad
 |L|=q+1,
\]

and is intersecting through singleton line intersections.  For arbitrary
weights on its lines, Lemma 5.1 says that its exact contribution is

\[
 x(F)=\sum_{L\in F}x_L.
 \tag{7.1}
\]

If one assigns

\[
 x_L={1\over q+1}
 \tag{7.2}
\]

to every line, every projective point has load one, but

\[
 x(F)={q^2+q+1\over q+1}
 =q+{1\over q+1}.
 \tag{7.3}
\]

Attaching one tag to each line and filling its remaining tag mass with
private chunks makes every tag load one without changing (7.3).  Pairwise
core intersections are singletons, so every centered nonlinear overlap
moment between distinct lines is zero.  As \(q\to\infty\), the line atoms
in (7.2) tend to zero, yet the weighted obstruction grows.  The filler
mass may be split among arbitrarily many private chunks, so it creates no
heavy atom either.

More generally, an atom bound \(\|x\|_\infty\leq\eta\) gives only

\[
 x(F)\leq(q^2+q+1)\eta.
 \tag{7.4}
\]

It rules out this particular cut at the coefficient-accurate scale only
if the right side is at most \(1+o(1/Q)\), not merely if it is \(o(K)\)
or \(m^{o(1)}\).  In the actual catalogue, chronology or a first-order
weighted singleton-intersection theorem must supply that conclusion.

## 8. What the new one-star expansion excludes

The chronology-specific theorem in
`MATH_ATTACK_FIRST_ORDER_PROTECTED_STRIP_INTERSECTING_EXPANSION_20260725.md`
proves, after the same isolated pruning, that

\[
 { |\Gamma'_v(E)|\over d'(v)}
 \leq8\varepsilon_1,
 \qquad
 \varepsilon_1=m^{-1/2+o(1)},
 \tag{8.1}
\]

for every good target \(v\) and retained strip \(E\) not containing
\(v\).  Here \(\Gamma'_v(E)\) consists of retained paths which contain
\(v\) and intersect \(E\).

For the corrected point,

\[
 x_P={\rho\over A'_{\tau(P)}},
 \qquad
 (1-\delta)\mu\leq A'_U\leq(1+\delta)\mu.
 \tag{8.2}
\]

Consequently (8.1) has the pointwise weighted consequence

\[
\begin{aligned}
 x(\Gamma'_v(E))
 &\leq {\rho\over(1-\delta)\mu}
          |\Gamma'_v(E)|\\
 &\leq8\varepsilon_1{1+\delta\over1-\delta}
       x(\{P:v\in C(P)\})\\
 &\leq(8+o(1))\varepsilon_1.
\end{aligned}
 \tag{8.3}
\]

Put \(\delta_1=(8+o(1))\varepsilon_1\).  Thus the saturated versions of
the two canonical diffuse obstructions above cannot literally occur
inside the audited point.

* In the three-bundle construction, take \(v=a\) and any \(bc\)-core
  path \(E\).  Every \(ab\)- or \(ca\)-core path contains \(a\) and
  intersects \(E\), so the left side of (8.3) is one, contradicting
  \(\varepsilon_1=o(1)\).
* In a point-saturated projective plane, take a point \(v\) and a line
  \(E\) not through it.  Every supported line through \(v\) meets \(E\),
  again making the left side one.

For the three-bundle pattern this gives a complete quantitative exclusion.
If the three side masses are \(a,b,c\), applying (8.3) with an external
edge on each of the other sides gives

\[
 a+c\leq\delta_1,qquad
 a+b\leq\delta_1,qquad
 b+c\leq\delta_1.
\]

Hence its total intersecting mass is at most

\[
 \boxed{a+b+c\leq\frac32\delta_1=o(1),}
 \tag{8.4}
\]

so it cannot raise the fractional colour cost above the star baseline.

For a projective plane the remaining accounting is weaker.  Put
\(k=q+1\), \(N=q^2+q+1=k^2-k+1\), and let \(s_v\) be the total line weight
through point \(v\).  If all lines are supported, (8.3) gives
\(s_v\leq\delta_1\).  Since every line contains \(k\) points,

\[
 kx(F)=\sum_vs_v\leq N\delta_1.
\]

Together with the atom bound \(x_L\leq\eta\), this yields only

\[
 \boxed{
 x(F)\leq
 \min\left\{N\eta,{N\over k}\delta_1\right\}.}
 \tag{8.5}
\]

At the corrected pointwise scales

\[
 \eta=m^{-11/6+o(1)},qquad
 k\leq K=m^{1+o(1)},qquad
 \delta_1=m^{-1/2+o(1)},
\]

the two terms in (8.5) can be as large as

\[
 m^{1/6+o(1)}quad\hbox{and}\quad m^{1/2+o(1)},
\]

respectively.  Thus the one-star theorem excludes a saturated plane but
does not, by itself, exclude a low-weight projective-plane matching cut
of mass greater than one.  An actual embedding of such a plane in the
geodesic catalogue is not proved; (8.5) identifies the quantitative
singleton-design gap that remains.

This is a genuine use of the geodesic chronology, and it removes these
specific saturated singleton designs.  It does **not** prove (4.4): a
general weighted dual obstruction may be distributed around a strong odd
Berge cycle or a higher matching-polytope facet without one external edge
hitting a near-saturated target star.  The exact remaining task is to
upgrade the one-star bound (8.3) to the full weighted matching-cover
inequality.

## 9. Exact proved and conditional boundary

### Proved

1. The corrected tag deficit is exactly the scalar \(\beta\) in (1.2),
   and rational clearing preserves total mass as (1.6).
2. A fractional colour cover of cost \((1+\varepsilon)D\) yields, after
   common clearing, one colour missing at most (0.3) tags.
3. The literal protected-claim ledger forces
   \(\varepsilon+\beta=o(1/Q)\) in the aggregate extraction route.
4. The exact remaining fractional condition is the point-specific
   weighted matching inequality (4.4).
5. A fixed loose triangle is harmless when its total \(x\)-mass is small,
   but arbitrarily diffuse loose-triangle bundles and projective-plane
   singleton designs can violate (4.4) by a constant or larger factor.

### Still unproved

For the actual corrected geodesic point, prove

\[
 \chi_f'(x)\leq1+o(1/Q),
\]

or directly construct a protected matching missing \(o(T/Q)\) tags.
Neither target capacities, atom diffuseness, width-two intersections, nor
the centered exponential moment proves this statement.

No coefficient-one conclusion is made.
