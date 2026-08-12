# Long MSW quotient intervals: fractional owner saturation and a shallow-shadow Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
 p=2m+1\text{ be prime},\qquad
 W=\binom{p}{m},\qquad T={W\over p},
\tag{0.1}
\]

and project an oriented MSW factor to translation necklaces. Fix an exact
interval length

\[
                         H\ll L\ll p.
\tag{0.2}
\]

On the middle-necklace-transversal core, every cyclic length-\(L\)
MSW interval is a \(2L\)-edge on the split left/right necklace set. The
owner interval hypergraph has a fractional matching of weight

\[
                         T-o(T).
\tag{0.3}
\]

Thus there is no fractional owner Hall obstruction. An almost-spanning
*integral* interval matching remains a genuine growing-rank rounding
problem.

Direct missing-shadow support has a sharper obstruction. Put

\[
 r_q={1\over W}\binom{2m+1}{m-q}
 =\prod_{j=0}^{q-1}{m-j\over m+2+j}.
\tag{0.4}
\]

For every \(Q\le\min\{H,(L+1)/2\}\), the fractional home-bundle deficit
for the two signed quotient target layers of depths \(1,\ldots,Q\) obeys

\[
 \boxed{
 \operatorname {def}_{L,Q}
 \ge
 2T\left[
       {Q^2\over L}-\sum_{q=1}^Q(1-r_q)
     \right]_+.}
\tag{0.5}
\]

Using only the product in (0.4),

\[
 1-r_q\le {q(q+1)\over m},
\tag{0.6}
\]

and hence

\[
 \boxed{
 \operatorname {def}_{L,Q}
 \ge
 2T\left[
 {Q^2\over L}
 -{Q(Q+1)(Q+2)\over3m}
 \right]_+.}
\tag{0.7}
\]

This is a literal Hall certificate. It already applies to fractional
interval packings, assumes perfect target distinctness inside every
interval, and therefore cannot be repaired by a stronger integral owner
matching theorem.

Suppose now that

\[
 H\asymp\sqrt{m\log m},\qquad H\ll L\ll m.
\tag{0.8}
\]

Then \(Q=\lfloor m/L\rfloor\) is admissible, and (0.7) gives

\[
 \boxed{
 \operatorname {def}_{L,Q}
 \ge\left({4\over3}-o(1)\right)
            T{m^2\over L^3}.}
\tag{0.9}
\]

Consequently exact-length open intervals cannot have total signed
quotient missing mass \(o(T)\) unless

\[
                         \boxed{L\gg m^{2/3}.}
\tag{0.10}
\]

In particular every scale

\[
                 H\ll L=O(m^{2/3})
\tag{0.11}
\]

has a positive-density, or larger, direct-shadow Hall obstruction. This
is not CPCR and not a safety/collar estimate: it counts the number of
distinct physical target necklaces which can possibly receive homes.

The obstruction does not rule out the surviving range

\[
                         m^{2/3}\ll L\ll m,
\tag{0.12}
\]

nor a variable-length packing which puts enough mass into much longer or
complete rows. In that range the integral owner matching and the
non-counting target-collision gate remain open.

## 1. The exact-length split-shore interval hypergraph

Let \({\cal R}\) be the \(T\) oriented MSW rows, each with \(p\) physical
arcs. Let \({\cal N}_m\) be the \(T\) middle translation necklaces and
split it into left and right copies

\[
                         V={\cal N}_{m,L}\sqcup{\cal N}_{m,R}.
\tag{1.1}
\]

A cyclic interval

\[
 I=(e_i,e_{i+1},\ldots,e_{i+L-1})
\tag{1.2}
\]

of one row is **admissible** when its \(L\) tail necklaces are distinct
and its \(L\) head necklaces are distinct. Its split owner support is

\[
 E(I)
 =\{[\operatorname {tail}e_j]_L:i\le j<i+L\}
 \cup
  \{[\operatorname {head}e_j]_R:i\le j<i+L\}.
\tag{1.3}
\]

Thus \(|E(I)|=2L\). The exact-length interval hypergraph
\({\cal I}^{=}_L\) has vertex set \(V\) and one edge \(E(I)\) for every
admissible interval. Edges retain their row/start tags even if their
unlabelled supports agree.

A matching in \({\cal I}^{=}_L\) is exactly a family of row intervals
which is pairwise compatible on both quotient necklace shores. Its owner
weight is \(L\) times its number of edges.

Choose the prime coordinate cycle by the middle-rank transversality
theorem. All but at most \(p(p-1)/2\) MSW rows are transversal at the
middle rank. Delete those exceptional rows. Since \(T\) is exponential,
their complete owner mass is \(o(T)\), and every length-\(L\) interval of
a retained row is admissible. Simultaneous target transversality would
make the support bound below an equality inside each row, but the Hall cut
uses only the universal upper bound and does not assume it.

## 2. The owner LP is fractionally saturated

There are \((T-o(T))p\) retained tagged intervals: one for every cyclic
start on every retained row. Give each the value

\[
                         x_I={1\over pL}.
\tag{2.1}
\]

### Theorem 2.1 (fractional owner near-factor)

The vector (2.1) is a fractional matching of \({\cal I}^{=}_L\), and its
total owner weight is \(T-o(T)\).

#### Proof

Fix a left necklace. It contains \(p\) physical middle owners. Each
owner is the tail of one retained row arc unless its row was deleted, and
one row arc lies in exactly \(L\) cyclic length-\(L\) intervals. Hence the
number of retained interval incidences at the vertex is at most \(pL\).
Its fractional load under (2.1) is at most one. The right-shore argument
is identical, using the \(p\) physical predecessors of the necklace.

The objective is

\[
 \sum_I Lx_I
 =(T-o(T))p\,{L\over pL}
 =T-o(T).
\]

Thus (2.1) is feasible and has the asserted weight. \(\square\)

The uniform split-vertex cover \(y_v=1/2\) has value \(T\), so Theorem
2.1 is asymptotically optimal. Therefore ordinary fractional Hall,
degree regularity, and the owner matching polytope cannot decide the
integral near-factor question.

## 3. Quotient target supports of one interval

For each \(q\le H\) and sign \(\epsilon\in\{-,+\}\), let
\({\cal T}_{q}^{\epsilon}\) be the translation necklaces of the relevant
rank-\((m-q)\) lower targets and complementary upper targets. Both typed
layers have size

\[
 |{\cal T}_{q}^{\epsilon}|
 ={1\over p}\binom{2m+1}{m-q}
 =Tr_q.
\tag{3.1}
\]

The translation lift of one certified quotient start supplies all \(p\)
physical phases of its target necklace. Thus covering one token of
\({\cal T}_{q}^{\epsilon}\) is exactly the quotient form of covering that
entire physical target orbit.

An open interval of \(L\) consecutive odd arcs contains at most

\[
                         L-2q+1
\tag{3.2}
\]

starts of a \(q\)-step every-second Johnson window. Let
\(J_{I,q}^{\epsilon}\) be the literal quotient target support of those
windows. Whether or not target transversality holds,

\[
                         |J_{I,q}^{\epsilon}|
 \le L-2q+1.
\tag{3.3}
\]

On a row which is also target-necklace transversal at depth \(q\),
equality holds before cross-interval collisions. The inequality is all
that is needed for the Hall cut.

Put

\[
 {\cal T}_{\le Q}
 =\bigsqcup_{q=1}^Q
   ({\cal T}_{q}^{-}\sqcup{\cal T}_{q}^{+}),
 \qquad
 J_I=\bigsqcup_{q=1}^Q
   (J_{I,q}^{-}\sqcup J_{I,q}^{+}).
\tag{3.4}
\]

Then

\[
 |J_I|\le2\sum_{q=1}^Q(L-2q+1)
 =2(QL-Q^2).
\tag{3.5}
\]

## 4. The exact home-bundle Hall dual

For every interval \(I\) and bundle \(B\subseteq J_I\), introduce
\(x_{I,B}\ge0\). The fractional target-home LP is

\[
\begin{aligned}
 \operatorname {cov}_{L,Q}=\max\quad&
       \sum_{I,B}|B|x_{I,B},\\
 \sum_{I\ni v,B}x_{I,B}&\le1 &&(v\in V),\\
 \sum_{I,B:t\in B}x_{I,B}&\le1 &&(t\in{\cal T}_{\le Q}),\\
 x_{I,B}&\ge0.
\end{aligned}
\tag{4.1}
\]

The first constraints are exactly pairwise quotient-necklace
compatibility. The second assign at most one interval home to each target;
nonhome collisions are allowed.

Put

\[
 \operatorname {def}_{L,Q}
 =|{\cal T}_{\le Q}|-\operatorname {cov}_{L,Q}.
\tag{4.1a}
\]

Dual variables \(y_v,z_t\ge0\) give

\[
 \operatorname {cov}_{L,Q}
 =\min\left\{
   \sum_vy_v+\sum_tz_t:
   \sum_{v\in E(I)}y_v+\sum_{t\in B}z_t\ge|B|
   \ \forall I,B
          \right\}.
\tag{4.2}
\]

For fixed \(I\), the strongest bundle contains the targets with \(z_t<1\).
Clipping \(z_t\) to \([0,1]\) and putting \(w_t=1-z_t\) yields the exact
weighted Hall form

\[
 \boxed{
 \operatorname {def}_{L,Q}
 =\max_{0\le w\le1}
 \left[\sum_tw_t-\tau_L(w)\right],}
\tag{4.3}
\]

where

\[
 \tau_L(w)
 =\min_{y\ge0}\left\{
   \sum_vy_v:
   \sum_{v\in E(I)}y_v
      \ge\sum_{t\in J_I}w_t
   \quad\forall I
                  \right\}.
\tag{4.4}
\]

Every integral interval matching and literal target homing is a feasible
integral point of (4.1). Hence any positive value in (4.3) is a genuine
physical missing-shadow obstruction, not merely a failure of a rounding
method.

## 5. The uniform shallow-depth Hall witness

Take \(w_t=1\) for every typed target in (3.4). Set, on every split owner
vertex,

\[
                         y_v=Q-{Q^2\over L}.
\tag{5.1}
\]

This is nonnegative for \(Q\le L\). Every interval edge has \(2L\)
vertices, so (3.5) gives

\[
 \sum_{v\in E(I)}y_v
 =2LQ-2Q^2
 \ge |J_I|.
\tag{5.2}
\]

Thus (5.1) is feasible in (4.4). Also

\[
 \sum_tw_t=2T\sum_{q=1}^Qr_q,
 \qquad
 \sum_vy_v=2T\left(Q-{Q^2\over L}\right).
\tag{5.3}
\]

Substitution in (4.3) proves (0.5).

For completeness, write

\[
 {m-j\over m+2+j}=1-a_j,
 \qquad
 a_j={2(j+1)\over m+2+j}.
\]

Since \(1-\prod_j(1-a_j)\le\sum_ja_j\),

\[
 1-r_q
 \le\sum_{j=0}^{q-1}{2(j+1)\over m+2+j}
 \le{q(q+1)\over m}.
\tag{5.4}
\]

Summing (5.4) and using

\[
 \sum_{q=1}^Qq(q+1)
 ={Q(Q+1)(Q+2)\over3}
\tag{5.5}
\]

proves (0.7).

### One-depth specialization

Taking weights only on one signed pair of depth-\(q\) layers gives

\[
 \operatorname {def}_{L,q}
 \ge2T\left[
 {2q-1\over L}-(1-r_q)
 \right]_+.
\tag{5.6}
\]

This is the exact comparison between open-boundary loss and the forced
binomial surplus at that depth.

## 6. The calibrated asymptotic obstruction

Assume (0.8) and put

\[
                         Q=\left\lfloor{m\over L}\right\rfloor.
\tag{6.1}
\]

Because \(L\gg H\gg\sqrt m\), one has

\[
 Q\le H,\qquad Q\le L/2,
\tag{6.2}
\]

and the asymptotic below applies whenever \(Q\to\infty\). Equation (0.7)
gives

\[
 {Q^2\over L}
 -{Q(Q+1)(Q+2)\over3m}
 =\left({2\over3}-o(1)\right){m^2\over L^3}.
\tag{6.3}
\]

Multiplying by \(2T\) proves (0.9). If \(L=Cm^{2/3}\) with fixed
\(C>0\), the right side is

\[
                         \left({4\over3C^3}-o(1)\right)T.
\tag{6.4}
\]

If \(H\ll L=o(m^{2/3})\), it is \(\omega(T)\); this is possible because
the objective sums holes across \(Q\to\infty\) typed layers. In either
case the required total \(o(T)\) shadow leave is impossible.

## 7. What the cut does and does not close

The cut is robust in four ways.

1. It applies before integral rounding: even the home-bundle LP has the
   stated deficit.
2. It grants perfect owner compatibility and perfect target distinctness
   inside each interval.
3. It uses only literal target counts, not CPCR, covariance, or endpoint
   degrees.
4. Deleting an \(o(T)\) owner set cannot repair a positive-density value
   in (0.9); it only reduces available interval support.

Its scope is exact.

* The proof concerns open intervals whose lengths are bounded above by
  \(L\). For a catalogue with lengths in \([L,L_{\max}]\), the same proof
  holds with \(L_{\max}\) in the denominators.
* Complete cyclic rows have no open-boundary loss and are not covered by
  this witness.
* When \(L\gg m^{2/3}\), (0.9) is \(o(T)\); the theorem supplies no
  obstruction.
* Even in the surviving range, an owner matching does not imply target
  coverage. The remaining exact test is the full dual (4.3)--(4.4), not
  first moments.

Thus a viable interval construction at calibrated \(H\) must place almost
all useful open-segment mass at scales beyond \(m^{2/3}\), use sufficiently
many complete rows, or recover cross-boundary targets by a separate legal
compiler. Merely taking \(H\ll L\) is not enough.

## 8. Certified boundary

Proved:

1. an asymptotically perfect fractional owner matching on the
   middle-transversal exact-length interval core;
2. the exact target home-bundle Hall dual;
3. the explicit uniform shallow-depth dual witness (0.5);
4. the elementary quantitative bound (0.7); and
5. the calibrated necessary condition \(L\gg m^{2/3}\) for direct
   all-depth support by open exact-length intervals.

Not proved:

1. an integral owner matching of weight \(T-o(T)\) in the surviving
   range \(m^{2/3}\ll L\ll m\);
2. a non-counting Hall obstruction in that range;
3. direct target near-coverage there; or
4. coefficient one.

The new route is therefore partially separated. The owner LP has no
fractional deficit, but the direct-shadow configuration LP has a sharp
shallow-depth deficit through scale \(m^{2/3}\). Above that scale, both
integral owner rounding and literal target expansion remain open.
