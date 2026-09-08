# Full-activity affine trace balance and the owner-frame Hall interface

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There is no activity-pattern collision obstruction inside one fixed
tensor-associator shore.

In one local eight-coordinate associator block, the six cycle cells split
into:

* four **main** squares, which flip the two special pair directions and
  retain a fixed reservoir orientation;
* two **reservoir** squares, which flip the two reservoir directions and
  retain a fixed special full/empty configuration.

For either lower or upper shadows, and for any number
\(j\in\{0,1,2\}\) of local directions used, the physical target uniquely
determines which of the six local cycles supplied it. Main and reservoir
targets have different special/reservoir cardinality signatures whenever
either is touched; when neither is touched, they are disjoint middle-owner
sets. Distinct main cycles retain different reservoir tags, and distinct
reservoir cycles retain different special tags.

Consequently, for any fixed shore vector, the \(6^r\) product
\(Q_{2r}\)-cells have pairwise disjoint physical lower-shadow images and
pairwise disjoint physical upper-shadow images, at every common global
depth. If every cell carries an affine conjugate of the recursive
half-depth rainbow factor, then the union is:

1. one exact cycle partition of all \(24^r\) tensor owners;
2. composed of physical isometric \(C_{4r}\)'s;
3. exactly lower- and upper-shadow injective on the entire tensor packet
   through \(q\le r\).

Thus the internal physical collision excess is exactly zero, not merely
\(o(24^r)\), simultaneously over every full/empty/split activity pattern.
The theorem holds for every one of the \(2^r\) associator shore vectors.

There is also an all-pattern affine quotient array. Choose an independent
uniform affine conjugate on each of the \(6^r\) cells. After identifying
the two active cube coordinates in every block with common abstract slots,
all direction/outside-orientation trace loads satisfy, simultaneously for
both signs and all \(q\le r\),

\[
 L_q^\pm(t)
 =(1\pm\varepsilon_r)
 \frac{6^r2^q}{\binom{2r}{q}},
 \qquad
 \varepsilon_r=\left(\frac38\right)^{r/8}.
\]

The total abstract trace discrepancy is

\[
 O(r\varepsilon_r24^r)=o(24^r).
\]

Exact translation completeness cannot extend from the \(4^r\) main cells
to all \(6^r\) cells: \(4^r\nmid6^r\). The random affine array is the
asymptotically exact replacement.

The obstruction appears only when this result is combined with the
dependent owner-frame Hall assignment. The local two-shore ownership
overlap graph is connected. Therefore any exact hybrid cycle cover drawn
from the two shores must take all six old-shore cycles or all six new-shore
cycles. It cannot implement a frame assignment which gives different
owners of the same 24-owner associator support different shores.

Hence the existing dependent Hall theorem and the tensor theorem do not
compose formally:

* Hall supplies an ownerwise frame assignment with \(o(W)\) literal
  deficiency;
* tensor cycles require shore choices constant on connected associator
  owner components.

Coarsening an arbitrary Hall assignment to component-constant shores can
recolour \(\Theta(W)\) owners, so the existing \(o(W)\) quarantine does not
pay for it. The exact remaining theorem is a **component-dependent affine
Hall assignment** whose choices are constant on associator components and
whose matched faces are the actual consecutive cycle traces, while
retaining \(o(W)\) total deficiency. Activity patterns and affine phases
are now closed; this component-granularity Hall/prefix condition is the
surviving interface.

## 1. Local activity signatures

Partition the eight local coordinates into the four special coordinates

\[
 A=\{a,b,c,d\}
\]

and the four reservoir coordinates

\[
 R=\{u,v,w,x\}.
\]

Fix either associator shore. Its four main squares have:

* two active pair directions in \(A\);
* a fixed two-set \(Y\subset R\), one point from each reservoir pair.

Its two reservoir squares have:

* two active pair directions in \(R\);
* a fixed two-set \(Z\subset A\).

On the old shore, \(Z\in\{ab,cd\}\); on the new shore,
\(Z\in\{ac,bd\}\). In either case, the four main-square special
configurations and the two reservoir-square special configurations are
disjoint and together partition \(\binom A2\).

Suppose a global geodesic window uses \(j\in\{0,1,2\}\) of the two local
cube directions.

### Lower signatures

For a main square, the lower target has

\[
 (|T\cap A|,|T\cap R|)=(2-j,2).
\tag{1.1}
\]

For a reservoir square, it has

\[
 (|T\cap A|,|T\cap R|)=(2,2-j).
\tag{1.2}
\]

### Upper signatures

For a main square, the upper target has

\[
 (|T\cap A|,|T\cap R|)=(2+j,2),
\tag{1.3}
\]

while for a reservoir square it has

\[
 (|T\cap A|,|T\cap R|)=(2,2+j).
\tag{1.4}
\]

These four formulas are independent of the selected shore.

## 2. Exact local cell separation

For a local cycle \(C\), let
\(\mathcal I_j^-(C)\) and \(\mathcal I_j^+(C)\) be the sets of physical
lower and upper local targets produced by windows using \(j\) directions
of \(C\).

### Lemma 2.1 (six-cell trace separation)

For either sign, any two distinct local cycles \(C\ne C'\), and arbitrary
\(j,j'\in\{0,1,2\}\),

\[
 \boxed{
 \mathcal I_j^\pm(C)\cap\mathcal I_{j'}^\pm(C')
 =\varnothing.
 }
\tag{2.1}
\]

#### Proof

If both cycles are main squares, they have different fixed reservoir
orientations \(Y\). That \(Y\) is retained in every lower and upper target,
so their images are disjoint.

If both are reservoir squares, they have different fixed special
configurations \(Z\), retained in every target. Again the images are
disjoint.

Suppose one cycle is main and the other reservoir. For lower targets,
(1.1)--(1.2) can agree only if \(j=j'=0\). For upper targets,
(1.3)--(1.4) give the same conclusion. At \(j=j'=0\), the target is the
local middle owner itself. The main and reservoir cycles are disjoint
members of one exact local cycle partition, so these owner sets do not
intersect. \(\square\)

The lemma allows \(j\ne j'\). This is important: two global windows in
different product cells need not use the same number of directions in a
given local block.

## 3. Global separation of every activity pattern

Fix a shore vector

\[
 \varepsilon\in\{0,1\}^r.
\]

Choosing one of the six local cycles in each block gives \(6^r\) disjoint
product cells

\[
 \mathcal Q_{\mathbf C}
 =C_1\square\cdots\square C_r
 \cong Q_{2r}.
\tag{3.1}
\]

The activity pattern records, for every block, whether \(C_i\) is main or
reservoir. It therefore records which local pair frame is split and which
local configuration is frozen full/empty/split data.

### Theorem 3.1 (cross-cell physical trace separation)

Let two physical geodesic windows lie in product cells
\(\mathcal Q_{\mathbf C}\) and \(\mathcal Q_{\mathbf C'}\). If their lower
targets are equal, then

\[
 \mathbf C=\mathbf C'.
\tag{3.2}
\]

The same statement holds for upper targets.

#### Proof

If the cells differ, choose a block \(i\) with \(C_i\ne C_i'\). Restrict
the two alleged equal targets to the eight ground coordinates of block
\(i\). The two restrictions belong to
\(\mathcal I_{j_i}^\pm(C_i)\) and
\(\mathcal I_{j_i'}^\pm(C_i')\) for some
\(j_i,j_i'\in\{0,1,2\}\). Lemma 2.1 says these sets are disjoint, a
contradiction. \(\square\)

Now put \(d=2r\), assume \(d\) is a power of two, and install an arbitrary
affine conjugate of the recursive rainbow factor \(F_d\) on every product
cell.

### Corollary 3.2 (full-activity exact rainbow factor)

For every fixed shore vector, the union of the \(6^r\) cell factors:

1. partitions all \(24^r\) tensor owners exactly;
2. consists of isometric \(C_{4r}\)'s;
3. has injective physical lower-shadow and upper-shadow maps for every
   \(q\le r\).

#### Proof

The local six-cycle factors partition each 24-owner block, so their product
cells partition the tensor support. Every installed \(F_d\)-conjugate is an
exact factor of its cell into isometric \(C_{2d}=C_{4r}\)'s.

Within one cell, recursive rainbowness gives both shadow injectivities
through \(d/2=r\). Between different cells, Theorem 3.1 gives disjoint
physical images. \(\square\)

This closes every main/reservoir, equivalently every local
full/empty/split, activity pattern in one shore.

## 4. An affine quotient array on all \(6^r\) cells

The physical images are already separated. It is still useful to balance
the abstract direction/basepoint traces obtained after each cell's two
directions per block are identified with a common \(d=2r\) slot set.

Independently on every product cell \(c\), choose a uniform affine
automorphism

\[
 g_c(x)=\sigma_cx+a_c\in Q_d\rtimes S_d
\]

and install \(F_d^{g_c}\). Since the base factor is two-sided trace
injective through \(r\), a fixed signed abstract trace is hit at most once
per cell.

For \(t\in\mathcal T_{d,q}\), define its aggregate abstract load
\(L_q^\pm(t)\). By affine transitivity,

\[
 \mathbb E L_q^\pm(t)
 =\lambda_{r,q}:=
 \frac{6^r2^q}{\binom{2r}{q}}.
\tag{4.1}
\]

Moreover,

\[
 \frac{\binom{2r}{q}}{2^q}
 \leq
 \sum_{j=0}^{2r}\binom{2r}{j}2^{-j}
 =\left(\frac94\right)^r,
\]

and therefore

\[
 \boxed{
 \lambda_{r,q}\geq\left(\frac83\right)^r.
 }
\tag{4.2}
\]

### Theorem 4.1 (all-pattern affine trace balance)

For all sufficiently large \(r\), there is a deterministic choice of the
affine conjugates such that, with

\[
 \delta_r=\left(\frac38\right)^{r/8},
\tag{4.3}
\]

one has simultaneously

\[
 \boxed{
 |L_q^\pm(t)-\lambda_{r,q}|
 \leq\delta_r\lambda_{r,q}
 }
\tag{4.4}
\]

for both signs, every \(q\le r\), and every abstract trace
\(t\in\mathcal T_{2r,q}\).

#### Proof

For fixed \(q,\pm,t\), the load is a sum of \(6^r\) independent Bernoulli
variables with mean (4.1). Chernoff gives failure probability at most

\[
 2\exp\left(-\frac{\delta_r^2\lambda_{r,q}}3\right).
\]

By (4.2)--(4.3),

\[
 \delta_r^2\lambda_{r,q}
 \geq
 \left(\frac83\right)^{3r/4}.
\]

The number of signed traces at all depths is at most

\[
 2\cdot3^{2r}=2\cdot9^r.
\]

A union bound is less than one for all sufficiently large \(r\).
\(\square\)

### Corollary 4.2 (full tensor trace discrepancy)

For the array in Theorem 4.1,

\[
\begin{aligned}
 &\sum_{1\le q\le r}\sum_{\pm}
   \sum_{t\in\mathcal T_{2r,q}}
   |L_q^\pm(t)-\lambda_{r,q}|\\
 &\qquad\leq
 2r\delta_r\,6^r2^{2r}
 =2r\delta_r24^r
 =o(24^r).
\end{aligned}
\tag{4.5}
\]

This is the requested all-activity-pattern affine balance.

### Exact translation-completeness obstruction

The main-cell array had exactly \(4^r=2^{2r}\) cells, one for every
translation of \(Q_{2r}\). The full tensor has \(6^r\) cells. Equal use of
all translations would require

\[
 4^r\mid6^r,
\]

which fails for every \(r\ge1\). More generally, a fixed activity pattern
with \(k\) main blocks has \(4^k2^{r-k}=2^{r+k}\) cells, divisible by
\(4^r\) only when \(k=r\). Thus literal translation completeness is unique
to the all-main pattern. Theorem 4.1 is the asymptotically exact
replacement on the full activity space.

## 5. Both associator shores

All arguments above use only:

1. four main squares with distinct retained reservoir tags;
2. two reservoir squares with distinct retained special tags;
3. disjointness of the four main and two reservoir owner sets;
4. two physical pair directions in every local square.

These properties hold on both associator shores. Therefore:

### Theorem 5.1 (two-shore resolution classes)

For every shore vector
\(\varepsilon\in\{0,1\}^r\), there exists an exact full-activity tensor
factor satisfying Corollary 3.2 and the affine balance (4.5).

These are \(2^r\) alternative exact resolution classes on the same
\(24^r\) owner support. The theorem does not assert that different shore
vectors can be mixed ownerwise inside one exact factor.

## 6. Exact shore rigidity

Let \(\mathcal F_0\) and \(\mathcal F_1\) be the two local six-cycle
partitions of the same 24-owner associator support. Form their ownership
overlap graph:

* left vertices are cycles of \(\mathcal F_0\);
* right vertices are cycles of \(\mathcal F_1\);
* every middle owner is an edge joining its two cycle owners.

This bipartite graph is connected.

### Theorem 6.1 (no hybrid local shore factor)

Suppose
\(\mathcal H\subseteq\mathcal F_0\cup\mathcal F_1\) covers every one of
the 24 local owners exactly once. Then

\[
 \boxed{\mathcal H=\mathcal F_0
 \quad\text{or}\quad
 \mathcal H=\mathcal F_1.}
\tag{6.1}
\]

#### Proof

For every cycle vertex \(C\) of the overlap graph, let \(z_C\in\{0,1\}\)
indicate whether \(C\in\mathcal H\). Every owner edge \(LR\) must be
covered exactly once, so

\[
 z_L+z_R=1.
\tag{6.2}
\]

Along a length-two path, (6.2) forces the two vertices on the same shore to
have equal labels. Connectivity therefore makes all left labels equal and
all right labels complementary. The only two solutions select the complete
left shore or the complete right shore. \(\square\)

This is the exact obstruction to applying an ownerwise frame assignment
inside one associator component.

## 7. Interface with dependent owner-frame Hall

The dependent Hall theorem provides one assignment

\[
 A:\binom{[2m]}m\longrightarrow\{\text{allowed pair frames}\}
\]

with total two-sided literal Hall deficiency \(o(W)\). Its rounding and
quota repair operate on individual owners. They do not impose that
\(A\) be constant on a 24-owner associator component.

If two owners in one component are assigned opposite associator shores,
Theorem 6.1 shows that no exact local cycle factor realizes those choices.
This is not repaired by the affine arrays: affine conjugacy changes cycle
orders and phases inside a chosen shore, not the shore incidence equations
(6.2).

### Proposition 7.1 (coarsening can have linear cost)

There are ownerwise shore assignments on a disjoint union of
24-owner associator supports for which every component has 12 owners on
each shore. Any component-constant shore assignment differs on exactly
12 owners per component, hence on one half of all owners.

#### Proof

Choose any 12 owners in every component for shore zero and the other 12
for shore one. A constant choice keeps at most 12 of the prescribed labels.
The components are disjoint, so the costs add. \(\square\)

The proposition does not say that every Hall-good assignment has this
form. It proves that the existing ownerwise theorem cannot be postprocessed
to component constancy using its \(o(W)\) quarantine bound.

## 8. Conditional global consequence and exact remaining theorem

Suppose one could strengthen dependent Hall rounding as follows:

> Assign one admissible shore vector and one tensor packet to each
> connected owner component, rather than assigning frames ownerwise, while
> retaining total lower-plus-upper Hall deficiency \(o(W)\), couple the
> Hall faces to the actual consecutive traces of the affine cell factors,
> and leave only \(o(W/H)\) owners outside the tensor packing.

Then install the exact full-activity affine factors of Theorem 5.1 on the
chosen packets. Internal packet collision excess is zero by Corollary 3.2;
the affine quotient discrepancy sums to \(o(W)\) by (4.5); the Hall
quarantine and omitted owners contribute \(o(W)\). The near
wreath-resolved SCD compiler would then give coefficient one after the
radius census and cycle-cut toll are imposed.

The phrase “couple the Hall faces” is essential. The proved owner-frame
Hall theorem matches targets to arbitrary literal faces after a frame is
frozen. It does not say that those matched faces are the nested consecutive
prefixes of one cycle factor. Affine balance supplies the correct marginal
distribution, but no theorem presently converts that marginal into the
same Hall matching across packets.

The unproved strengthening is therefore:

> **Component-dependent affine Hall theorem.** There is one integral
> mixed-frame tensor assignment, constant on every connected associator
> owner component, together with one affine conjugate on every selected
> tensor cell, such that the actual consecutive physical shadow maps have
> \[
>  \sum_{q\le H}(\kappa_q^-+\kappa_q^+)=o(W),
> \]
> while the frame/type quotas and the Catalan radius census are retained.

Here \(\kappa_q^\pm\) is domain size minus physical shadow-image size at
depth \(q\).

This is strictly stronger than the proved ownerwise dependent Hall theorem.
Theorem 6.1 is the exact reason the ownerwise result cannot simply be
inserted into the tensor construction. There is no remaining
activity-pattern or affine-phase obstruction inside a fixed tensor
resolution class; the open step is the joint component-level
Hall/prefix/packet coupling.
