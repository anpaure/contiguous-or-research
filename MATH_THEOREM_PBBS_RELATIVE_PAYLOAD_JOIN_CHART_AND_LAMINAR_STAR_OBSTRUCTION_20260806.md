# PBBS-relative payloads are interval-join charts: a laminar-star obstruction

**Date:** 2026-08-06  
**Method:** literal interval-union algebra and the mandatory-core payload
criterion; no computation or search  
**Status:** unconditional quantifier correction and structural obstruction.
Freezing the PBBS whole-fan section read-only really removes the owner-side
matching, but it does not turn the remaining payload problem into an ordinary
target-to-interval matching.  Even in one good separated free block there
are inclusion-minimal infeasible target systems of every order up to the
block length plus one, although every proper subsystem is literally
realizable.  The obstruction persists after restricting all targets to the
deep range `d<|S|<t`.  Thus the ideal containment SDR is only the one-shadow
of the required object.  The correct residual object is a growing-rank
factor of interval-join charts.  More sharply, the previously proposed
canonical-lock template of separated length-`d` blocks admits no such factor
asymptotically: the rank-`(t-1)` interval antichain casts a quadratic upset
shadow which leaves less than half the required capacity for the remaining
deep ranks.

## 1. The source-side problem after the PBBS section is frozen

Let `T` be the labelled PBBS owner chronology and let `P` be its maximal
depth-`d` antecedent.  The fixed whole-fan section already carries, as
read-only owner intervals, one intersection witness for every strict-lower
target and the complementary union witness for every proper-upper target.
Consequently a payload filling does not select or consume an owner witness.
It only has to create a distinct ordinary source interval of the prescribed
value.

Fix one good free block

\[
                         G=[a,b],\qquad g=|G|\le d.             \tag{1.1}
\]

At its positions let `F_p` be the mandatory cores and let `C_G` be the
boundary-free common payload core.  Assume the private-marker hypothesis

\[
 U_G=\{\iota_p:p\in G\}\text{ has size }g,
 \qquad F_p\cap U_G=\{\iota_p\}.                              \tag{1.2}
\]

Every owner-invisible filling has the form

\[
                         A_p=F_p\cup H_p,
 \qquad H_p\subseteq C_G.                                    \tag{1.3}
\]

For an interval `I` put

\[
 F(I)=\bigcup_{p\in I}F_p,
 \qquad A(I)=\bigcup_{p\in I}A_p.                            \tag{1.4}
\]

The private markers make the values `A(I)` at distinct intervals distinct,
but they do not make those values independently programmable.

## 2. Complete charts are join homomorphisms

Let `Int(G)` be the nonempty intervals of `G`.

### Theorem 2.1 (complete interval-join chart criterion)

Suppose a named value `Z_I` is prescribed for every `I in Int(G)`.  There
is an owner-invisible filling (1.3) with

\[
                         A(I)=Z_I\qquad(I\in\operatorname{Int}(G))
                                                                    \tag{2.1}
\]

if and only if

\[
 F_p\subseteq Z_{\{p\}}\subseteq F_p\cup C_G
                         \qquad(p\in G),                         \tag{2.2}
\]

and

\[
 \boxed{
 Z_{[u,v]}=\bigcup_{p=u}^{v}Z_{\{p\}}
                         \qquad([u,v]\subseteq G).}              \tag{2.3}
\]

In particular the complete triangular chart, containing
`g(g+1)/2` named targets, has only `g` freely chosen letter values.

#### Proof

If (2.1) holds, its singleton cases give `A_p=Z_{\{p\}}`; (1.3) gives
(2.2), and taking unions of the singleton letters gives (2.3).

Conversely define `A_p=Z_{\{p\}}`.  Condition (2.2) writes it in the
form (1.3), so the short-gap mandatory-core theorem preserves the complete
owner row.  Equation (2.3) gives every equality in (2.1). \(\square\)

There is an equivalent binary formulation.  For every coordinate `x`, the
map

\[
 I\longmapsto {\bf1}_{\{x\in Z_I\}}                            \tag{2.4}
\]

must be the hitting function of one point set `E_x subseteq G`:

\[
 {\bf1}_{\{x\in Z_I\}}={\bf1}_{\{I\cap E_x\ne\varnothing\}}.  \tag{2.5}
\]

Thus it preserves every interval union which is again an interval.  This
is a semilattice constraint, not a capacity constraint.

## 3. A minimal obstruction on a laminar star

The preceding dependence remains high-order even if the assigned physical
intervals are laminar.

Partition `G` into `q>=2` nonempty consecutive intervals

\[
                         G=J_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}J_q.             \tag{3.1}
\]

Assume `C_G` contains a set `K` and one further point `x`, with

\[
                         K\cap\{x\}=\varnothing.                \tag{3.2}
\]

Prescribe the parent and child targets

\[
 Z_G=K\cup F(G)\cup\{x\},
 \qquad
 Z_j=K\cup F(J_j)\quad(1\le j\le q).                          \tag{3.3}
\]

### Theorem 3.1 (laminar-star obstruction of arbitrary order)

The `q+1` assignments

\[
                         G\mapsto Z_G,
 \qquad J_j\mapsto Z_j                                      \tag{3.4}
\]

are jointly infeasible, but every proper subfamily is realized by one
literal owner-invisible filling of `G`.

Under the private-marker hypothesis (1.2), all the targets in (3.3) are
distinct.  If

\[
 |K|=d+1,
 \qquad |K|+|F(G)|+1<t,                                     \tag{3.5}
\]

then every one of them lies strictly in the deep range

\[
                         d<|Z|<t.                              \tag{3.6}
\]

For a length-`g` good Johnson block, the sufficient eventual central
inequality

\[
                         3d+2<t                               \tag{3.7}
\]

guarantees (3.5) uniformly for `g<=d`.

#### Proof

Suppose all assignments are realized.  Every child target omits `x`, so
the equality `A(J_j)=Z_j` forces `x` to be absent from every letter at
every position of `J_j`.  The children partition `G`, hence `x` is absent
from every letter of `G`.  This contradicts `x in Z_G=A(G)`.

Now remove any one or more assignments.  If the parent is absent, put

\[
                         H_p=K\qquad(p\in G).                   \tag{3.8}
\]

Every remaining child then has value `K union F(J_j)=Z_j`.

If the parent is present, some child, say `J_s`, is absent because the
subfamily is proper.  Choose `p_0 in J_s` and put

\[
 H_{p_0}=K\cup\{x\},
 \qquad H_p=K\quad(p\ne p_0).                                \tag{3.9}
\]

The parent has value `K union F(G) union {x}`.  Every assigned child is
disjoint from `J_s`, so it still has value `K union F(J_j)`.  Equations
(3.8)--(3.9) are allowed payloads because `K union {x} subseteq C_G`.
The mandatory-core theorem preserves the owner row in every case.

Distinct children have different private-marker projections
`{iota_p:p in J_j}`; the parent has their union and also `x`.  This proves
target distinctness.  Finally `K` is disjoint from every mandatory core,
so every target has rank greater than `d`, while

\[
 |Z_G|\le d+1+2g+1\le3d+2<t.                                 \tag{3.10}
\]

Every child is smaller than the parent.  This proves (3.6). \(\square\)

### Corollary 3.2 (unbounded local Helly number)

For every `q<=g`, the relative payload system has an
inclusion-minimal infeasible subsystem of size `q+1`, even when

1. the physical intervals form a laminar family;
2. every target is individually aperture-feasible;
3. every proper subsystem is simultaneously feasible;
4. every target lies above the separately solved subdeadline bank; and
5. all assignments leave the labelled owner chronology unchanged.

Hence no fixed-order local conflict test, pairwise incompatibility graph,
or ordinary target-to-interval Hall matching can characterize the payload
atlas as `d` tends to infinity.

The obstruction is not an owner shortage.  Every target in (3.3) is a
strict-lower set and therefore occurs in the exact ideal containment SDR.
The SDR merely assigns its members to distinct containing owner slots; it
does not enforce the joint identity forced by the partition (3.1).

## 4. Exact laminar form of the coordinate cut

The obstruction above is the only possible form for one coordinate on a
laminar interval family.

Let `L` be a laminar family of intervals in `G`, and fix a payload
coordinate `x in C_G`.
Write `L_x^+` and `L_x^-` for the intervals whose prescribed residual does
and does not contain `x`.

### Proposition 4.1 (laminar negative-cover criterion)

The `x`-equalities are realizable by some point set `E_x subseteq G` if
and only if every positive interval contains a point outside the union of
the negative intervals:

\[
 I\setminus\bigcup_{J\in\mathcal L_x^-}J\ne\varnothing
                         \qquad(I\in\mathcal L_x^+).            \tag{4.1}
\]

Equivalently, no positive node is contained in a negative ancestor and no
collection of maximal negative descendants covers that positive node.

If the children of every internal node partition that node and all leaves
are present, this reduces to the exact recursion

\[
 x\in Z_I
 \quad\Longleftrightarrow\quad
 x\in Z_J\text{ for at least one child }J\text{ of }I.        \tag{4.2}
\]

#### Proof

Every negative interval forbids `E_x` throughout that interval.  Thus
`E_x` must be contained in the complement of their union, and it can hit
every positive interval exactly when (4.1) holds.  For a laminar family,
the negative members meeting a fixed positive interval are either
ancestors or have pairwise disjoint maximal descendants, giving the second
formulation.  When the children partition their parent, (4.1) is precisely
(4.2). \(\square\)

This is a useful positive reduction: a *prepared* laminar target chart is
checked by a tree recursion.  What fails is the inference that an arbitrary
ideal SDR automatically has that recursion.

## 5. The correct global object is a chart factor

Let `G_1,...,G_b` be separated good free blocks.  For a block `G_a`, an
allowed filling `H^(a)` determines the complete labelled deck

\[
 \mathcal D(G_a,H^{(a)})
   =\left\{F(I)\cup\bigcup_{p\in I}H_p^{(a)}:
                   \varnothing\ne I\subseteq G_a\text{ an interval}\right\}.
                                                                    \tag{5.1}
\]

Private markers make (5.1) an injectively addressed family.  Since the
blocks are separated, their payload variables are disjoint.

### Theorem 5.1 (relative payload chart-factor equivalence)

After the PBBS owner section and the canonical locks outside the free bank
have been fixed, a complete deep payload atlas exists if and only if one
can choose one allowed filling in every free block and match every deep
target to a distinct occurrence in the union of the decks (5.1).

Equivalently, before the fillings are chosen, the global selector is a
hypergraph factor whose atoms are feasible partial interval-join charts.
Its atom rank is at most

\[
                         {g+1\choose2}=\Theta(d^2),             \tag{5.2}
\]

not one.  The ordinary ideal containment graph and the target-to-interval
aperture graph are only one-shadows of this chart hypergraph.

#### Proof

Given the fillings, every interval has one literal value.  Distinct
physical interval addresses may be matched to equalities independently
across different blocks, and the read-only PBBS principle supplies the
owner witness without consuming a source address.  This proves the forward
description.

Conversely, a selected feasible chart is, by definition, realized by one
payload filling of its block.  Different blocks use disjoint variables and
separated source positions, so all selected charts compose.  The exact
source matching then gives the atlas.  A length-`g` block has precisely
`binom(g+1,2)` interval addresses. \(\square\)

Theorem 3.1 shows that this hypergraph does not reduce to the matching of
its one-shadow, even on laminar interval atoms.

## 6. Near-optimality forces growing-rank charts

The high-order issue cannot be avoided by using only a bounded number of
targets in each free block.

Use the odd central parameters

\[
 n=2m+1,
 \quad r=m,
 \quad t=m-d,
 \quad W={n\choose m},
 \quad M={n\choose t},
 \quad U=W-M.                                                \tag{6.1}
\]

The depth-sized template has

\[
 b=\left\lfloor{U\over d+1}\right\rfloor
 \quad\text{blocks and}
 \quad C_b=b{d(d+1)\over2}                                  \tag{6.2}
\]

physical interval addresses.  Let

\[
 L_{\rm deep}=\sum_{s=d+1}^{t-1}{n\choose s}.                \tag{6.3}
\]

### Proposition 6.1 (positive-density chart utilization)

At the optimal deadline,

\[
 {L_{\rm deep}\over C_b}
 \longrightarrow
 \theta:={4\Phi(-\sqrt{\pi/2})\over1-e^{-\pi/4}}>0.77.       \tag{6.4}
\]

Consequently an atlas with `O(1)` terminal leave assigns
`Theta(d^2)` targets per free block on average.  In particular no factor
whose chart atoms have uniformly bounded rank can prove the required
near-optimal atlas on this block template.

#### Proof

The central local limit and lower-tail estimates give

\[
 {M\over W}\longrightarrow e^{-\pi/4},
 \qquad
 {\sum_{s=1}^{t-1}{n\choose s}\over dW}
       \longrightarrow2\Phi(-\sqrt{\pi/2}).                  \tag{6.5}
\]

The omitted subdeadline mass is

\[
 \sum_{s=1}^{d}{n\choose s}
       =\exp(o(m))=o(dW),                                    \tag{6.6}
\]

so the second limit is unchanged by replacing the numerator with
`L_deep`.  On the other hand, (6.2) gives

\[
 {C_b\over dW}\longrightarrow{1-e^{-\pi/4}\over2}.          \tag{6.7}
\]

Dividing (6.5) by (6.7) proves the equality in (6.4).  The strict numerical
bound follows from the same two-step Mills estimate used in the
depth-block scalar-surplus theorem.  Since each block has at most
`Theta(d^2)` intervals, the average assertion follows. \(\square\)

Balanced-doublet rounding supplies separated free-copy positions and
owner resources, but its edges have only `Theta(d)` literal macro roles.
Proposition 6.1 and Theorem 3.1 show why that rounding cannot, by itself,
export the payload atlas: the labels of the free copies must subsequently
be coupled in `Theta(d^2)`-rank join charts.

## 7. The separated depth-sized block face is actually impossible

There is a stronger obstruction which uses only interval containment.

Let

\[
 \mathcal J_g=\{[u,v]:1\le u\le v\le g\}                     \tag{7.1}
\]

be ordered by set containment.

### Lemma 7.1 (exact upset shadow of an interval antichain)

If `A subseteq J_g` is an antichain of size `a`, then

\[
 \boxed{
 |\uparrow\mathcal A|
 :=|\{J:\exists I\in\mathcal A,\ I\subseteq J\}|
 \ge {a(a+1)\over2}.}                                      \tag{7.2}
\]

Equality is attained by the complete layer of all `a` intervals of length
`g-a+1`.

#### Proof

Map `[u,v]` to

\[
                         (x,y)=(u,g+1-v).                     \tag{7.3}
\]

These are the positive lattice points in the triangle `x+y<=g+1`.
An interval containing `[u,v]` corresponds to a point coordinatewise at
most `(x,y)`.

Order the antichain points so that

\[
                         x_1<\cdots<x_a.                      \tag{7.4}
\]

Incomparability forces

\[
                         y_1>\cdots>y_a.                      \tag{7.5}
\]

Put `x_0=0`.  The union of their southwest rectangles has exact size

\[
                         \sum_{i=1}^{a}(x_i-x_{i-1})y_i.      \tag{7.6}
\]

Now `x_i-x_(i-1)>=1`, and a strictly decreasing positive integer sequence
of length `a` obeys `y_i>=a-i+1`.  Hence (7.6) is at least

\[
                         \sum_{i=1}^{a}(a-i+1)
                         ={a(a+1)\over2}.                     \tag{7.7}
\]

Taking `x_i=i,y_i=a-i+1` gives equality and corresponds exactly to all
intervals of length `g-a+1`. \(\square\)

Now return to the canonical-lock block face.  Assume

1. `A_p=P_p` at every position outside the free bank;
2. the free bank is the disjoint union of `b` blocks of length `d`; and
3. every target of rank below `t` is represented.

The first condition means that every source interval of rank below `t`
is contained in one free block: meeting an outside position would include
the rank-`t` letter `P_p`, and crossing two blocks meets such a position.

### Theorem 7.2 (rank-`t-1` shadow no-go)

Put

\[
 A={n\choose t-1},
 \qquad
 L_- =\sum_{s=d+1}^{t-2}{n\choose s},
 \qquad
 C={d(d+1)\over2}.                                          \tag{7.8}
\]

A necessary condition for the separated block face above is

\[
 \boxed{
 L_-
 \le bC-{A^2\over2b}-{A\over2}.}                            \tag{7.9}
\]

For the odd optimal central parameters and

\[
                         b=\left\lfloor{W-M\over d+1}\right\rfloor,
 \qquad M={n\choose t},                                     \tag{7.10}
\]

inequality (7.9) fails for every sufficiently large `n`.  Consequently
the canonical-lock plus separated depth-`d` payload-block template cannot
carry the complete deep lower atlas, even with arbitrary payload letters
and even before any owner, upper, residence, or opening constraint is
imposed.

#### Proof

Choose one representing interval for every rank-`(t-1)` target.  Within
block `j`, these intervals form an antichain `A_j`: if `I subsetneq J`,
then `A(I) subseteq A(J)`; two distinct equal-rank target values cannot
occur at nested intervals.  Write `a_j=|A_j|`.  Then

\[
                         \sum_{j=1}^{b}a_j=A.                  \tag{7.11}
\]

No interval containing a member of `A_j` can represent a target of rank at
most `t-2`, because its union already contains a rank-`(t-1)` set.  Lemma
7.1 therefore leaves at most

\[
                         C-{a_j(a_j+1)\over2}                 \tag{7.12}
\]

addresses for ranks `d+1,...,t-2` in block `j`.  Summing (7.12) and using
Cauchy--Schwarz,

\[
 \sum_ja_j^2\ge {A^2\over b},                               \tag{7.13}
\]

gives (7.9).

It remains to compare the two sides asymptotically.  Put

\[
                         e_0=e^{-\pi/4}.                      \tag{7.14}
\]

The central local limit gives

\[
 {M\over W}\longrightarrow e_0,
 \qquad {A\over W}\longrightarrow e_0,
 \qquad {b\over W/d}\longrightarrow1-e_0.                  \tag{7.15}
\]

Consequently the right side of (7.9), divided by `dW`, is at most

\[
 {1-e_0\over2}-{e_0^2\over2(1-e_0)}+o(1)
 ={1-2e_0\over2(1-e_0)}+o(1).                               \tag{7.16}
\]

The lower-tail estimate, with the top one layer and the subdeadline bank
removed, gives

\[
 {L_-\over dW}
 \longrightarrow2\Phi(-\sqrt{\pi/2}).                       \tag{7.17}
\]

Finally

\[
 2\Phi(-\sqrt{\pi/2})
 >{1-2e^{-\pi/4}\over2(1-e^{-\pi/4})}.                       \tag{7.18}
\]

For a proof with elementary constants, the standard Mills lower bound
`Phi(-x)>x phi(x)/(1+x^2)` at `x=sqrt(pi/2)` makes the left side larger
than `2e_0/(2+pi)`.  Direct cross-multiplication, using
`9/20<e_0<1/2` and `pi<22/7`, makes this strictly larger than the right
side of (7.18).  Equations (7.16)--(7.18) contradict (7.9) for all large
parameters. \(\square\)

Numerically, only for orientation, the two constants in (7.17) and
(7.16) are approximately `0.210` and `0.081`.  The gap is therefore not a
boundary-order effect.

There is a quantitative version.  Keep all ranks `d+1,...,t-2` inside the
same separated blocks, but let only `A_in` rank-`(t-1)` targets use them.
If

\[
                         {A_{\rm in}\over W}\longrightarrow\alpha,
                                                                    \tag{7.19}
\]

then the same proof forces

\[
 2\Phi(-\sqrt{\pi/2})
 \le {1-e_0\over2}-{\alpha^2\over2(1-e_0)}.                  \tag{7.20}
\]

Thus

\[
 \alpha\le
 \alpha_*:=\sqrt{(1-e_0)^2
       -4(1-e_0)\Phi(-\sqrt{\pi/2})}<0.27.                  \tag{7.21}
\]

Since the complete rank-`(t-1)` layer has asymptotic mass `e_0W>0.45W`,
moving only a polynomial or `o(W)` number of its targets cannot repair the
face.  If all lower deep ranks stay in these blocks, a positive linear
fraction of the rank-`(t-1)` layer must be exported.

### Corollary 7.3 (the fractional chart cone is separated too)

The no-go is not caused by integral rounding.  Give each feasible labelled
chart atom `E` the statistics

\[
 a(E)=\#\{\text{rank-}(t-1)\text{ targets in }E\},
 \qquad
 l(E)=\#\{\text{rank }d+1,\ldots,t-2\text{ targets in }E\}.
                                                                    \tag{7.22}
\]

Every atom obeys

\[
                         l(E)+{a(E)(a(E)+1)\over2}\le C.      \tag{7.23}
\]

Consequently any fractional selection of total chart mass `b`, with total
top load `A` and lower-deep load `L_-`, obeys exactly (7.9).  Hence the
desired binomial named-target vector is outside the fractional interval-
chart cone of the separated block template for all sufficiently large
parameters.

#### Proof

Inequality (7.23) is Lemma 7.1 applied inside one chart.  If the chart
weights are `w_E`, sum it with weights and use

\[
 \sum_Ew_Ea(E)^2\ge
 {\left(\sum_Ew_Ea(E)\right)^2\over\sum_Ew_E}
 ={A^2\over b}.                                             \tag{7.24}
\]

This gives (7.9) verbatim.  The asymptotic contradiction is Theorem 7.2.
\(\square\)

### Corollary 7.4 (random-phase cutting cannot transfer the pull clock)

Take any stationary fractional marked-trace circulation with the correct
one-dimensional rank marginals, choose an arbitrary distribution of phase
cuts, and retain only marked intervals lying wholly inside separated
length-`d` blocks whose exterior letters have rank `t`.  If all rank-
`(t-1)` and ranks `d+1,...,t-2` target loads are required to survive, the
cut circulation violates (7.23) after averaging.

Thus the stationary pull-clock theorem does not descend to the old linear
block template by multiplying a length-`ell` mark by the elementary
retention probability `(d-ell+1)/d`.  The loss includes the quadratic
containment shadow of the retained rank-`(t-1)` marks, and that shadow is
already too large at the level of fractional expectations.

#### Proof

Condition on one block word and its retained marked intervals.  Its
rank-`(t-1)` intervals form an antichain, so (7.23) holds pointwise.
Average first over the cut and then over the stationary circulation.
Corollary 7.3 applies to the resulting fractional chart law and gives the
contradiction from Theorem 7.2. \(\square\)

### Corollary 7.5 (required architectural escape)

Any successful PBBS-relative payload construction must violate at least
one hypothesis of Theorem 7.2.  In particular it must do at least one of
the following:

1. realize a positive-density part of the rank-`(t-1)` layer outside the
   separated payload blocks;
2. merge the free positions into substantially longer regions;
3. thin or rethread the rank-`t` separators so lower intervals can cross
   between blocks; or
4. replace the canonical-lock face by a chronology in which the top
   lower row and the deep atlas are compiled jointly.

Thus a positive interval-chart factor on the old depth-sized template is
not merely awaiting a stronger matching theorem: its interval-poset
capacity is false.

## 8. Proof-safe consequence for the all-dimensional programme

The following implications are valid.

1. The fixed PBBS whole-fan section removes every owner-side capacity
   coordinate from the deep payload problem.
2. The exact ideal containment SDR proves that every deep target has ample
   individual containing-owner supply.
3. Separated free copies make different block fillings independent.
4. Within one block, however, target equalities are governed by the
   interval-join identities (2.3), or by the equivalent coordinate cuts.
5. Those identities have inclusion-minimal failures of order growing with
   `d`, even on laminar physical intervals and entirely above the solved
   low-target range.
6. Near-optimal scalar usage forces chart atoms of rank `Theta(d^2)`.

Therefore the remaining proof cannot be an ordinary Hall theorem on
target-to-owner or target-to-interval incidences, nor a bounded local
repair of an arbitrary ideal SDR.  Moreover, on the canonical separated
block face, no chart factor exists at all by Theorem 7.2.  A sufficient
next theorem must first implement one of the architectural escapes in
Corollary 7.5 and then prove one of:

* a **PBBS-relative interval-join chart factor**, selecting the payload
  words and target partition simultaneously; or
* an explicit recursive decomposition of the deep Boolean ideal into
  prepared laminar charts satisfying (4.2), together with an embedding of
  those charts into the separated PBBS free blocks.

This note does not refute either possibility.  It proves the exact
high-order obstruction that either construction must overcome.  It also
does not prove balanced-doublet integral rounding, a resident completion,
an upper-safe opening, or `nu(k)<=B(k)+O(1)`.

## 9. Dependencies

Used as inputs:

* the mandatory-core short-gap theorem and its exact coordinatewise
  payload criterion;
* arbitrary-payload marker recursion in a good free block;
* the fixed PBBS whole-fan read-only principle;
* the exact ideal containment SDR; and
* the standard central local-limit estimates already proved for the
  depth-block template.

No analytic Gram/Bessel estimate, probabilistic rounding theorem,
computation, or finite search is used.
