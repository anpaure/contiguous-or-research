# Protected-strip width-two pruning and the exact surviving dual gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let (g=(1-o(1))H) be the return-free geodesic chunk length and let
(Q=o(H)) be the controlled radius.  We use the truncated regime

\[
 \max_{q\le Q}\lambda_q=m^{o(1)},
 \tag{0.0}
\]

which holds for
(Q^2/m=O(\log\log m+o(\log m))).  The relevant object of one chunk is
its protected diagonal strip


\[
 {cal S}_Q(P)=
 \{G_{t,t}\}\cup
 \{G_{t+q,t},G_{t-q,t}:1\le q\le Q\},
 \tag{0.1}
\]

with the physical phase range understood.  Two corrections are essential.

1. The sparse conflict must be imposed on ({\cal S}_Q(P)), not on the
   entire (g\times g) grid.  A full-grid conflict pays for irrelevant
   ranks as far as (m\pm g), where the target load can be polynomial.
2. A bad tag fibre has physical weight (g), not weight one.

With these corrections, the raw overlap problem closes exactly:

* one may prune every pair whose protected strips share a three-element
  antichain;
* the relative bad degree is (m^{-3+o(1)});
* all but (o(W)) weighted tag/target fibres retain degree
  (m^{5/2-o(1)});
* every surviving protected intersection has width at most two; and
* its complete exponential shape census is summable down to residual
  density (1/\log m).

This still does not prove a matching.  The exact surviving obstruction is
the weighted hitting-set dual over whole tag fibres, followed by joint
integral rounding.

## 1. Protected three-antichain conflict

Join two candidate chunks on distinct tags when their protected strips
share three pairwise incomparable Boolean targets.  Let (A) be the
unpruned degree of a tag fibre and (Delta_3) the maximum conflict degree.

### Theorem 1.1 (protected conflict census)

Uniformly for the calibrated return-free catalogue,

\[
 \boxed{
 {\Delta_3+1\over A}
 \le m^{o(1)}{gQ\over m^4}
 =m^{-3+o(1)}.}
 \tag{1.1}
\]

#### Proof

Fix a path and three protected antichain cells.  In grid coordinates their
successive positive gaps are

\[
 \alpha_1,\alpha_2\ge1,
 \qquad
 \beta_1,\beta_2\ge1.
\]

Conditioned on the first protected target, a competing grid must realize
four disjoint prescribed coordinate blocks.  Since all protected ranks
lie between (m-Q) and (m+Q), the normalized load of the anchor is at
most

\[
 \max_{q\le Q}\lambda_q=m^{o(1)}.
\]

The relative degree for the four gaps is therefore at most

\[
 {m^{o(1)}\over
  \binom{m-g}{\alpha_1,\alpha_2}
  \binom{m-g}{\beta_1,\beta_2}}.
 \tag{1.2}
\]

Summing all positive gaps is (O(m^{-4+o(1)})), dominated by four unit
gaps.  The protected strip has (O(gQ)) possible first cells.  This proves
(1.1). \(\square\)

The use of protected anchors is what permits (g\asymp H).  For the full
grid, ranks near (m\pm g) would introduce an unnecessary factor as large
as (exp(g^2/m)).

## 2. Coefficient-safe balanced pruning

Apply Theorem 1.1 and the weighted independent-pruning theorem in
`RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md` with

\[
 L=Q\log m,
 \qquad
 p={1\over L(\Delta_3+1)}.
 \tag{2.1}
\]

Give every tag fibre weight (g), and every protected target fibre weight
one.  There are (T=(1+o(1))W/g) tags, so their total weight is
((1+o(1))W).  The total target-fibre weight is (O(QW)).

The minimum unpruned fibre degree is ((1-o(1))A).  Hence every good fibre
retains degree at least

\[
 \boxed{
 \mu/4,
 \qquad
 \mu={1\over Lm^{-3+o(1)}}=m^{5/2-o(1)}.}
 \tag{2.2}
\]

The weighted exceptional proportion is

\[
 e^{-\Omega(\mu)}+O(1/L)=O(1/(Q\log m)).
\]

Therefore its total physical ledger is

\[
 O(QW)/(Q\log m)=O(W/\log m)=o(W).
 \tag{2.3}
\]

Fix one pruning outcome attaining this bound.  Its retained catalogue has
no protected three-antichain shared by two paths.

## 3. Exact width-two exponential census

For two retained paths put

\[
 {cal L}={\cal S}_Q(P)\cap{\cal S}_Q(E).
\]

By construction, ({\cal L}) has width at most two.  If
(|{\cal L}|\ge2), form its meet and join in either full grid and put

\[
 t=\left|\bigcup{\cal L}\setminus\bigcap{\cal L}\right|.
 \tag{3.1}
\]

The meet and join need not themselves be protected cells; they are shared
cells of the two full grids, which is all the counting argument needs.

### Lemma 3.1 (shape and span bounds)

\[
 \boxed{|{\cal L}|\le2(t+1).}
 \tag{3.2}
\]

For a fixed protected strip, the number of possible width-two
intersection shapes of span (t) is at most

\[
 \boxed{8g^2(t+1)16^t.}
 \tag{3.3}
\]

A fixed such shape has raw relative degree at most

\[
 \boxed{
 m^{o(1)}{t+1\over\binom{m-g}{t}}.}
 \tag{3.4}
\]

#### Proof

The Boolean interval from the meet to the join has height (t+1).
Dilworth and width at most two give (3.2).

Write the two coordinate spans as (a,b), with (a+b=t).  There are at
most (g^2(t+1)) bounding boxes.  A width-two family is the union of two
chains.  Each chain lies in a monotone lattice path; counting the path and
a subset of it gives at most (2\cdot4^t) chains and hence at most
(8\cdot16^t) ordered chain pairs, with slack for duplicate
representations.  This proves (3.3).

Every competitor containing the shape contains its meet and join.  Given
one protected anchor, it has at most (t+1) grid displacements producing
the prescribed rank-(t) extension, while the prescribed difference is
one of at least (inom{m-g}{t}) coordinate blocks.  The protected anchor
load is (m^{o(1)}).  This proves (3.4). \(\square\)

For (w\ge1), define

\[
 {mathfrak M}_w(P)
 ={1\over A}\sum_E
 \left(w^{|{\cal S}_Q(P)\cap{\cal S}_Q(E)|}
 -1-(w-1)|{\cal S}_Q(P)\cap{\cal S}_Q(E)|\right).
 \tag{3.5}
\]

### Theorem 3.2 (summable protected width-two hierarchy)

For every fixed (C<\infty), uniformly for (1\le w\le C\log m),

\[
 \boxed{
 \sup_P{\mathfrak M}_w(P)=m^{o(1)}.}
 \tag{3.6}
\]

#### Proof

By Lemma 3.1,

\[
 {\mathfrak M}_w(P)
 \le m^{o(1)}g^2
 \sum_{t=1}^{2g}
 { (t+1)^2 16^t w^{2(t+1)}
  \over\binom{m-g}{t}}.
 \tag{3.7}
\]

The ratio of consecutive summands is

\[
 O\!\left(w^2{g\over m-g}\right)=m^{-1/2+o(1)}.
\]

The \(t=1\) term dominates.  Since \(g^2/m=m^{o(1)}\), (3.6) follows.
\(\square\)

Taking \(w=1/z\) gives a raw moment bound for every formal density

\[
 z\ge1/(C\log m).
 \tag{3.8}
\]

This does **not** by itself authorize an induced-residual nibble down to
that density.  The pruning leaves only
\(\mu=m^{5/2-o(1)}\) distinct alternatives per fibre, whereas a protected
edge has rank \(K=gQ=m^{1+o(1)}\).  At \(z=1/\log m\), the scalar product
degree \(\mu z^K\) tends to zero superpolynomially.  Thus the shape moments
are sufficient but the residual support entropy is not.  Any integral
rounding must either avoid passing to induced residuals or use a
simultaneous multicover/color resolution.

## 4. The precise surviving cut

Let \({\cal I}_U\) be the retained path family above tag \(U\), let \(V\)
be the currently available protected targets, and let \(C(P)\subseteq V\)
be the claims of \(P\).  Among tag-saturating fractional weights

\[
 \sum_{P\in{\cal I}_U}x_P=1,
 \tag{4.1}
\]

the minimum capacity-one target overload has the exact dual

\[
 \boxed{
 \operatorname{Ov}({\cal I})=
 \max_{a\in[0,1]^V}
 \left[
 \sum_U\min_{P\in{\cal I}_U}a(C(P))
 -\sum_{v\in V}a_v
 \right].}
 \tag{4.2}
\]

The pruning theorem controls the coordinate fibres \(a=e_v\), but (4.2)
ranges over every weighted hitting set.  Hence (1.1)--(3.8) do not by
themselves imply small overload after target deletion.

The new exact frontier is consequently:

> **Protected-strip integral resolution theorem.**  Prove uniformly for
> every \(a\in[0,1]^V\) that
> \[
>  \sum_U\min_{P\in{\cal I}_U}a(C(P))
>  \le\sum_va_v+o(W),
> \]
> and round one optimizing fractional point to an integral family while
> preserving its legal geodesic path structure, without requiring
> polynomial support to survive an induced rank-\(K\) residual.

Fractional horizontal successor flow is already carried by the same path
weights: its start mass divided by its state-column mass is \(1/g=o(1/Q)\).
The remaining horizontal issue is therefore part of the same integral
rounding, not a second fractional obstruction.
