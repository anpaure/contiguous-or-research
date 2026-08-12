# Width-two rational multicovers need matching-polytope cuts before edge colouring

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Consider the proposed simultaneous-resolution input after clearing the
denominators of the protected-strip fractional point:

* every tag has degree exactly \(D\);
* every protected target has degree at most \(D+o(D)\);
* every edge is one complete legal chunk and has \(K\) protected claims;
* every pairwise protected intersection has width at most two; and
* the normalized exponential intersection excess is \(m^{o(1)}\) for
  weights up to \(C\log m\).

The numerical and pair-intersection parts of this input do **not** imply an
edge colouring with \((1+o(1))D\) colours.  They do not even imply that the
fractional edge-chromatic number is \((1+o(1))D\).

The obstruction is an exact width-two Shannon triangle.  For arbitrary
growing edge rank \(K\), it has tag degree \(D\), target degree at most
\(D\), and normalized exponential excess only \(O((\log m)^2)=m^{o(1)}\),
but requires at least \(3D/2\) colours.  Normalizing every edge by \(1/D\)
gives a feasible tag-saturating, target-capacity-one rational point, so the
failure is an integral matching-polytope obstruction rather than a failure
of the fractional overload calculation.

Consequently entropy compression or heat-bath rounding cannot start from
the displayed five parameters alone.  The exact additional gate is the
matching-cover inequality

\[
 \sum_{e\in\mathcal E}y_e
 \le (1+o(1))D
     \max_{M\text{ a matching}}\sum_{e\in M}y_e
 \qquad(y\ge0).                                      \tag{0.1}
\]

For the actual protected geodesic catalogue, one must prove (0.1), or a
stronger hereditary version, from chronology or from a new census of
overlap *cycles*.  Width two and the present row-sum exponential moment do
not see this cut.

This note is an obstruction to a black-box rounding theorem from the stated
parameters.  It is not asserted that the constructed abstract chunks occur
as a subcatalogue of the Boolean geodesic catalogue.

## 1. The exact colouring target

Let \(\mathcal T\) be the tags and \(V\) the protected targets.  A cleared
rational multicover is a labelled hypergraph

\[
 \mathcal H=(\mathcal T\mathbin{\dot\cup}V,\mathcal E)
\]

in which an edge has the form

\[
 e=\{\tau(e)\}\mathbin{\dot\cup}C(e),
 \qquad |C(e)|=K.                                    \tag{1.1}
\]

A proper edge colour is a matching: it contains at most one edge over each
tag and at most one edge claiming any protected target.  Hence a proper
edge colouring into \(C\) colours is precisely a decomposition

\[
 \mathcal E=M_1\mathbin{\dot\cup}\cdots
              \mathbin{\dot\cup}M_C                  \tag{1.2}
\]

into matchings.

If every tag has degree \(D\), then every tag occurs in exactly \(D\) of the
colour classes.  Thus, when \(C=(1+\varepsilon)D\), the total number of
tag--colour omissions is exactly

\[
 \sum_{i=1}^{C}|\mathcal T\setminus\tau(M_i)|
 =|\mathcal T|(C-D)=\varepsilon D|\mathcal T|.       \tag{1.3}
\]

In particular, \(C=(1+o(1))D\) would decompose the multicover into
near-factors with total missing-tag mass \(o(D|\mathcal T|)\).

The relevant fractional relaxation is the fractional edge-chromatic
number

\[
 \chi_f'(\mathcal H)
 =\min\left\{
    \sum_{M\in\mathfrak M}x_M:
    x_M\ge0,\ 
    \sum_{M\ni e}x_M\ge1\ (e\in\mathcal E)
           \right\},                                 \tag{1.4}
\]

where \(\mathfrak M\) is the family of all matchings.  Finite-dimensional
linear-programming duality gives

\[
 \boxed{
 \chi_f'(\mathcal H)
 =\max_{y\ge0}
   \left\{
    \sum_{e\in\mathcal E}y_e:
    \sum_{e\in M}y_e\le1\quad(M\in\mathfrak M)
   \right\}.}                                       \tag{1.5}
\]

Equivalently,

\[
 \boxed{
 \chi_f'(\mathcal H)
 =\sup_{y\ge0,\ y\ne0}
 {\sum_e y_e\over
  \max_{M\in\mathfrak M}\sum_{e\in M}y_e}.}        \tag{1.6}
\]

Indeed, for fixed nonzero \(y\), divide it by the denominator in (1.6)
to obtain a feasible vector in (1.5); conversely every feasible vector in
(1.5) has denominator at most one.  Therefore (0.1) is equivalent to

\[
 \chi_f'(\mathcal H)\le(1+o(1))D.                   \tag{1.7}
\]

It is a necessary gate even before one asks for an integral or list edge
colouring.

## 2. Exact width-two Shannon multicover

Fix an even integer \(D\ge2\), put \(r=D/2\), and fix any integer
\(K\ge2\).  Make three tags

\[
 \tau_{ab},\qquad \tau_{bc},\qquad \tau_{ca}.        \tag{2.1}
\]

For each \(j\in\{0,1\}\), make a disjoint core triple

\[
 a_j,b_j,c_j.                                        \tag{2.2}
\]

For every \(j\), every type \(xy\in\{ab,bc,ca\}\), and every
\(i\in[r]\), make one edge

\[
 e_{j,xy,i}=\{\tau_{xy}\}\mathbin{\dot\cup}
              \{x_j,y_j\}\mathbin{\dot\cup}P_{j,xy,i},
 \qquad |P_{j,xy,i}|=K-2,                            \tag{2.3}
\]

where all private sets \(P_{j,xy,i}\) are mutually disjoint and avoid the
six core targets.  Thus each tag carries \(r\) edges in each of the two
copies and has degree \(2r=D\).

If the protected targets are required to carry a poset, take
\(a_j<b_j<c_j\) in each copy and insert all private targets anywhere in a
total extension.
Then every protected intersection has poset width one.  If the three core
targets are instead placed in one Boolean rank, the maximum intersection
width is two.  Only the latter upper bound will be used.

### Theorem 2.1 (all stated local parameters, but a \(3/2\) gap)

The hypergraph above has the following properties.

1. Every tag has degree exactly \(D\).
2. Every protected target has degree at most \(D\).
3. Every edge has exactly \(K\) protected claims.
4. Every pair of protected claim sets intersects in at most two targets,
   hence has width at most two.
5. With
   \[
    \Psi_w(e):={1\over D}\sum_{f\ne e}
       \left(
       w^{|C(e)\cap C(f)|}-1
       -(w-1)|C(e)\cap C(f)|
       \right),                                     \tag{2.4}
   \]
   one has, uniformly over all edges,
   \[
    \boxed{\Psi_w(e)\le {1\over2}(w-1)^2.}          \tag{2.5}
   \]
   If the sum is restricted to edges on tags different from that of
   \(e\), as in the actual protected-strip census, its value is exactly
   zero.
6. The weights \(x_e=1/D\) saturate every tag and load every protected
   target by at most one.
7. Nevertheless
   \[
    \boxed{
      \chi_f'(\mathcal H)\ge {3D\over2},\qquad
      \chi'(\mathcal H)\ge {3D\over2}.}             \tag{2.6}
   \]

#### Proof

The tag-degree assertion follows from the last sentence before the theorem.
For example, \(a_j\) occurs in the \(r\) edges of types \(ab\) and \(ca\)
inside copy \(j\), hence has degree \(2r=D\).  The same calculation holds
for every core target, while every private target has degree one.  This
proves the second assertion, and the third is built into (2.3).

Two edges of the same type and copy share exactly the corresponding two
core targets; importantly, they also have the **same tag**.  Edges of
different types in the same copy have different tags and share the unique
core target common to those types.  Edges in different copies have
disjoint protected claims.  This proves the fourth assertion.

For \(s=0,1\),

\[
 w^s-1-(w-1)s=0,                                    \tag{2.7}
\]

whereas for \(s=2\),

\[
 w^2-1-2(w-1)=(w-1)^2.                              \tag{2.8}
\]

Thus an edge receives a nonzero contribution in (2.4) only from the other
\(r-1\) edges of its own type and copy.  Consequently

\[
 \Psi_w(e)\le {r-1\over D}(w-1)^2
 <{1\over2}(w-1)^2,                                 \tag{2.9}
\]

which is (2.5).

Every one of those \(r-1\) double intersections lies inside the same tag
fibre.  Across different tags, an intersection has size zero or one, so
every summand in the distinct-tag centred census is zero.  This proves the
additional assertion in Part 5.

At a tag, the normalized total weight is \(D/D=1\).  At a core target it
is also \(D/D=1\), and at a private target it is \(1/D\).  This proves the
sixth assertion.

Finally fix either copy \(j\), and let

\[
 \mathcal Q_j:=\{e_{j,xy,i}:xy\in\{ab,bc,ca\},\ i\in[r]\}. \tag{2.10}
\]

Any two members of \(\mathcal Q_j\) conflict: equal types already share
their tag, while different types share a core target.  Hence a matching
contains at most one member of \(\mathcal Q_j\).  Put \(y_e=1\) on
\(\mathcal Q_j\) and zero otherwise.  Then

\[
 \max_{M\in\mathfrak M}\sum_{e\in M}y_e\le1,
 \qquad
 \sum_e y_e=|\mathcal Q_j|=3r={3D\over2}.            \tag{2.11}
\]

Equation (1.6) gives the fractional lower bound in (2.6), and
\(\chi'\ge\chi_f'\) gives the integral lower bound. \(\square\)

### Corollary 2.2 (the obstruction survives the intended growth regime)

Let \(D=D_m\) be any even sequence tending to infinity and let
\(K=K_m\ge2\) be arbitrary.  In particular one may choose the denominator
scale so that

\[
 K=m^{1+o(1)},\qquad {K^2\over D}\longrightarrow0.  \tag{2.12}
\]

Thus even the non-intrinsic relation \(K^2=o(D)\) does not remove the
construction.

For every fixed \(C\), uniformly for \(1\le w\le C\log m\), the examples
of Theorem 2.1 obey

\[
 \sup_e\Psi_w(e)=O((\log m)^2)=m^{o(1)},             \tag{2.13}
\]

while

\[
 {\chi'(\mathcal H)\over D}\ge{3\over2}.           \tag{2.14}
\]

The number of protected targets used is exactly

\[
 6+6r(K-2)=6+3D(K-2).                                \tag{2.15}
\]

Thus no hidden restriction on the relative growth of \(K\) and \(D\) is
being used.

#### Proof

Only (2.13) and (2.15) remain to check.  Equation (2.13) follows at once
from (2.5).  There are six core targets and \(6r(K-2)\) private targets,
which gives (2.15). \(\square\)

## 3. Why the present exponential moment misses the obstruction

The subtraction

\[
 w^{s}-1-(w-1)s                                    \tag{3.1}
\]

is exactly zero at \(s=0,1\).  This is appropriate for controlling the
nonlinear part of a deletion second moment, but an edge-colouring conflict
already occurs at \(s=1\).  In the construction above, the complete
conflict among different core bundles is carried entirely by singleton
intersections and is therefore invisible in \(\Psi_w\).  The remaining
double intersections lie inside single tag fibres and contribute only
\(O((w-1)^2)\) even under the stronger all-tag convention.  Under the
actual distinct-tag convention they are omitted and the centred moment is
identically zero.

Even replacing (3.1) by \(w^s-1\) would not by itself give the proposed
conclusion under an \(m^{o(1)}\) upper bound.  For a core edge the normalized
linear intersection mass is

\[
 {1\over D}\sum_{f\ne e}|C(e)\cap C(f)|
 ={2(r-1)+2r\over D}=2-{2\over D},                  \tag{3.2}
\]

a bounded quantity.  Thus constant normalized pair-conflict mass is
compatible with a constant integrality gap.  A near-\(D\) colouring needs
global matching expansion, not merely a subpolynomial pair moment.

## 4. The exact new cut

For any subfamily \(\mathcal A\subseteq\mathcal E\), let
\(\nu(\mathcal A)\) be its matching number.  A decomposition into \(C\)
matchings necessarily satisfies

\[
 \boxed{|\mathcal A|\le C\,\nu(\mathcal A)
        \qquad(\mathcal A\subseteq\mathcal E).}      \tag{4.1}
\]

Indeed, every one of the \(C\) colour classes contains at most
\(\nu(\mathcal A)\) members of \(\mathcal A\).  For the Shannon family
\(\mathcal Q\), (4.1) says

\[
 {3D\over2}\le C.                                   \tag{4.2}
\]

The indicator cuts (4.1) are necessary but the weighted version (0.1) is
the exact fractional statement.  For a rank-two multigraph it specializes
to the usual odd-set obstruction: if \(S\) is an odd set of target
vertices, every matching uses at most \((|S|-1)/2\) edges internal to
\(S\), so

\[
 |E(S)|\le C{|S|-1\over2}.                           \tag{4.3}
\]

The example is (4.3) with \(S=\{a,b,c\}\).

For the actual width-two-pruned chunk multicover, the next theorem must
therefore include at least one of the following genuinely stronger inputs.

1. Prove the full weighted matching-cover bound (0.1).
2. Prove a structural theorem reducing every dual vector in (1.6) to
   target stars plus an \(o(D)\) error; target-degree bounds would then
   suffice.
3. Establish a hereditary census of overlap cycles which, in particular,
   rules out every positive-density Shannon triangle and all higher
   matching-polytope analogues.

Only after this fractional gate is proved is it meaningful to ask whether
entropy compression or heat-bath dynamics rounds the fractional matching
cover into \((1+o(1))D\) integral colours when \(K\) grows.  The present
tag degrees, target degrees, width-two intersections, and
\(m^{o(1)}\) exponential moment do not reach that gate.

## 5. Correction: the shape bound does not exclude the triangle

The previous version of this report asserted a uniform all-pair codegree
\(m^{-1+o(1)}D\) after pruning.  That assertion was false and is retracted.
There were two independent errors:

1. it used the older pruning degree \(m^{5/2-o(1)}\), whereas the corrected
   pointwise tuning has smaller degree \(m^{11/6-o(1)}\); and
2. it treated the shape census as an all-tag codegree bound, although the
   conflict graph and the moment (11.5) sum only over **distinct tags**.

The exact corrected calculation follows.

### 5.1 Correct pointwise tuning and failed union bound

Section 2.1 of
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md` uses

\[
 \delta_{\rm pr}=m^{-2/3},\qquad
 L=Qm^{2/3}\log m,\qquad
 \mu=pA=m^{11/6-o(1)}.                              \tag{5.1}
\]

For a fixed positive-span protected pair, the raw distinct-tag shape bound
has relative size

\[
 \delta_{\rm sh}=m^{-1+o(1)}.                       \tag{5.2}
\]

Thus its marked distinct-tag count has mean at most

\[
 \lambda=\mu\delta_{\rm sh}=m^{5/6+o(1)}.           \tag{5.3}
\]

Chernoff at twice the mean gives only

\[
 \Pr(Y>2\lambda)\le \exp(-m^{5/6+o(1)}).            \tag{5.4}
\]

But the protected target universe has \(|V|=\exp(\Theta(m))\), so there
are \(\exp(\Theta(m))\) target pairs.  Since \(m^{5/6}=o(m)\), (5.4)
does **not** support a union bound.  In particular, the former conclusion
\(4m^{-1+o(1)}D\) was not proved.

There is a weaker statement which the same calculation does prove.

### Proposition 5.1 (one-heavy-tag pair bound)

For every protected target pair \(s=\{u,v\}\) which occurs in the raw
catalogue, choose one occurrence and denote its tag by \(\tau(s)\).  The
pointwise isolated pruning may be chosen so that, simultaneously for every
pair,

\[
 \sum_{P:\ s\subset C(P),\ \operatorname{tag}(P)\ne\tau(s)}x_P
 \le m^{-5/6+o(1)}.                                 \tag{5.5a}
\]

No \(o(1)\) bound is asserted for the contribution from \(\tau(s)\); it
can be as large as the whole tag mass one.

#### Proof

For a fixed pair \(s\), the positive-span shape bound applied to its chosen
anchor says that the number of raw candidates on tags other than
\(\tau(s)\) which contain \(s\) is at most
\(A\delta_{\rm sh}\).  Their marked count \(Y_s\) is therefore binomial
with mean at most \(\lambda\) from (5.3).

Take \(h=m\).  The standard binomial estimate gives

\[
 \Pr(Y_s\ge h)
 \le\left({e\lambda\over h}\right)^h
 =\exp\left[-(1/6-o(1))m\log m\right].              \tag{5.5}
\]

This does beat \(|V|^2=\exp(O(m))\).  Since a good tag denominator is at
least \((1-\delta_{\rm pr})\mu\), it yields at most the weaker uniform
distinct-tag rational load

\[
 {m\over(1-\delta_{\rm pr})\mu}
 =m^{-5/6+o(1)}.                                    \tag{5.6}
\]

Isolated deletion only reduces \(Y_s\), so (5.6) proves (5.5a).  The
probability that (5.5a) fails for some pair is \(o(1)\).  Intersecting this
event with the positive-probability pointwise-pruning ledger, with an
irrelevant absolute enlargement of its exceptional constants, gives one
simultaneous outcome.  After clearing denominators, (5.5a) is
\(m^{-5/6+o(1)}D\) outside the anchor tag. \(\square\)

### 5.2 Same-tag double bundles versus cross-tag singleton conflicts

The distinction is literal in Section 2.  For each \(j\), the \(r=D/2\)
edges claiming \(\{a_j,b_j\}\) all lie over the single tag
\(\tau_{ab}\).  Likewise \(\{b_j,c_j\}\) is confined to \(\tau_{bc}\)
and \(\{c_j,a_j\}\) to \(\tau_{ca}\).  Therefore the repeated
two-target intersections are same-tag intersections and are absent from
the distinct-tag shape sum.

Across different tags the only intersections are

\[
 \{b_j\},\qquad \{c_j\},\qquad \{a_j\},             \tag{5.7}
\]

one for each pair of types in copy \(j\).  Every such intersection is a
singleton, so both the centred moment and every distinct-tag pair-codegree
are exactly zero.  Nevertheless the tag cliques together with these three
families of singleton conflicts make the \(3D/2\) edges of one copy
pairwise conflicting.

Thus the doubled triangle is fully compatible with:

* the distinct-tag width-two condition;
* the distinct-tag shape-by-shape positive-span bound;
* the corrected estimate (5.6); and
* zero distinct-tag nonlinear exponential excess.

It remains an abstract incidence construction rather than a proved literal
geodesic subcatalogue, but the current shape census does not exclude it.

### 5.3 Denominator inflation gives no rescue

The common denominator \(D\) may be enlarged arbitrarily, so a condition
such as \(K^2=o(D)\) is not intrinsic.  If a distinct retained path has
weight about \(1/\mu\), then after clearing denominators its multiplicity
is about \(D/\mu\).  The scale-invariant quantity is therefore

\[
 {K^2(D/\mu)\over D}={K^2\over\mu}.                 \tag{5.8}
\]

At the corrected protected scale,

\[
 K=m^{1+o(1)},\qquad \mu=m^{11/6-o(1)},
 \qquad {K^2\over\mu}=m^{1/6+o(1)}\longrightarrow\infty. \tag{5.9}
\]

Hence neither denominator inflation nor the corrected support degree
numerically rules out singleton-intersection matching cuts.  The full
weighted inequality (0.1), proved from actual rotor chronology, remains
the exact fractional gate.

## 6. Proved and unproved boundary

Proved here:

* the exact matching-cover LP dual for the desired decomposition;
* an explicit rational capacity-feasible multicover satisfying all the
  stated degree, rank, width, and exponential-moment scales;
* a sharp \(3D/2\) fractional and integral colour lower bound; and
* validity of the obstruction for arbitrary growing \(K\) and arbitrary
  denominator scale \(D\);
* failure of the former \(m^{-1+o(1)}D\) all-pair union bound at the
  corrected \(\mu=m^{11/6-o(1)}\) tuning; and
* the weaker valid distinct-tag estimate \(m^{-5/6+o(1)}D\), together with
  a proof that it does not exclude the doubled triangle.

Not proved here:

* realization of the Shannon construction by literal Boolean geodesic
  chunks;
* failure or validity of (0.1) in the actual pruned catalogue; or
* an edge-colouring theorem once (0.1) and suitable hereditary versions
  are added.

The exact surviving positive lane is therefore to prove (0.1) for the
actual rational chunk multicover using its chronology.  A proof based only
on the currently recorded pair-intersection parameters is impossible.
