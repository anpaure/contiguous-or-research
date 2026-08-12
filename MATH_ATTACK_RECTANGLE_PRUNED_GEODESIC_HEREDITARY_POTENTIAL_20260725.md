# Rectangle-pruned geodesic chunks: hereditary potential audit

Date: 2026-07-25

Pure mathematics only.  No computation, web input, or fixed-rank theorem
is used.

## 0. Verdict

Pairwise rectangle pruning does not supply hereditary priority-deadline
closure for the return-free geodesic chunk catalogue.

The obstruction already occurs at depth one.  For the chunk parameters of
`MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md`, the enlarged
depth-one deadline is exactly

\[
 \boxed{\bar d^{(g)}_1=1.}                            \tag{0.1}
\]

Hence a base path may hide one previously used depth-one target, but two
blocked phase columns make its priority degree zero.

There exist three return-free geodesic grids
\(\mathcal G_0,\mathcal G_1,\mathcal G_2\) such that

\[
 \mathcal G_0\cap\mathcal G_i=\{v_i\}\quad(i=1,2),
 \qquad
 \mathcal G_1\cap\mathcal G_2=\varnothing,           \tag{0.2}
\]

where \(v_1,v_2\) are depth-one targets in distinct phase columns of
\(\mathcal G_0\).  Thus every pairwise intersection has width at most one
and contains no \(2\times2\) product rectangle.  Select priorities on
\(\mathcal G_1,\mathcal G_2\) which claim \(v_1,v_2\).  The resulting
residual has

\[
 B_1(\mathcal G_0)=2>\bar d^{(g)}_1,                 \tag{0.3}
\]

so the base path on \(\mathcal G_0\) has no legal priority.

This is minimal: zero or one blocker is feasible, while two are not.  It
also survives the strongest pruning which forbids every pair of chunks
sharing a nontrivial product rectangle.  The two blockers arrive from two
different earlier chunks and are invisible to a pairwise rectangle test.

The natural exact entropy is the tag partition function

\[
 D_U(Z)=\sum_{P\in\mathcal B(U)}\Pi_Z(P),             \tag{0.4}
\]

where \(\Pi_Z(P)\) is the exact number of legal common priorities.  This
quantity is not closed under tag degrees and one-target row degrees: its
one-step drift contains two-target blocker correlations, and the next
drift contains three-target correlations.  Equivalently, the Hessian of
the partition function is an essential state variable.  Rectangle pruning
does not remove the mixed term in (0.3).

Therefore no martingale based only on current tag degrees, row-target
degrees, and pairwise grid-rectangle exclusion proves \(O(m)\)-bite
propagation.  A possible surviving route is a full exponential blocker
potential or an adaptive dispersal condition controlling blockers from
different selected chunks.  Neither is presently proved.

## 1. Exact depth-one deadline

Let \(T\) be the number of labelled length-\(g\) chunk tags, with

\[
 gT\le W,
 \qquad
 R_1=\binom{2m}{m-1}={m\over m+1}W.                 \tag{1.1}
\]

The raw depth-one claim and defect are

\[
 c^{(g)}_1
 =\min\left\{g,\left\lfloor{R_1\over T}\right\rfloor\right\},
 \qquad
 d^{(g)}_1=g-c^{(g)}_1.                              \tag{1.2}
\]

Since \(T\le W/g\),

\[
 {R_1\over T}
 \ge {gm\over m+1}>g-1.                             \tag{1.3}
\]

Thus \(c^{(g)}_1\ge g-1\) and

\[
 d^{(g)}_1\le1.                                      \tag{1.4}
\]

The enlarged deadline used by the owner-scale bite is

\[
 \bar d^{(g)}_1
 =\min\left\{g,
  \max\left(d^{(g)}_1,
   \left\lceil C_m{g\over m}\Lambda_1\right\rceil
  \right)\right\},                                  \tag{1.5}
\]

where \(C_m=(\log m)^2\), \(\Lambda_1=\lambda_1=(m+1)/m\), and
\(g=(1-o(1))H=m^{1/2+o(1)}\).  Therefore

\[
 0<C_m{g\over m}\Lambda_1=o(1),                     \tag{1.6}
\]

so its ceiling is one.  Equations (1.4)--(1.6) prove (0.1).

The deadline Hall theorem now gives the exact dichotomy

\[
 \Pi_Z(P)>0\iff B_1(P;Z)\le1
 \quad\hbox{at depth one}.                           \tag{1.7}
\]

When no deeper target is blocked, the depth-one contribution is especially
transparent.  With no blocked phase, all \(g!\) priority orders are legal.
With one blocked phase, that phase must occupy the unique height-zero
slot, so exactly \((g-1)!\) priorities remain.  With two blocked phases,
none remain:

\[
 \Pi_1(B_1)=
 \begin{cases}
  g!,&B_1=0,\\
  (g-1)!,&B_1=1,\\
  0,&B_1\ge2.
 \end{cases}                                         \tag{1.8}
\]

Thus the second blocker creates a jump of \(\log\Pi\) to \(-\infty\).
No bounded-increment martingale for pathwise log-priority degree is
possible.

## 2. The exact partition function and its unclosed drift

For a forbidden target family \(Z\), the priority degree of a base path is

\[
 \Pi_Z(P)
 =(g-B_Q(P))!
  \prod_{q=1}^Q
  { (\bar d_q-B_{q-1}(P))!
   \over
    (\bar d_q-B_q(P))!},                             \tag{2.1}
\]

provided every prefix inequality \(B_q(P)\le\bar d_q\) holds, and is zero
otherwise.  The exact residual tag degree is

\[
 \boxed{D_U(Z)=\sum_{P\in\mathcal B(U)}\Pi_Z(P).}    \tag{2.2}
\]

This is the correct entropy partition function.  The priority scheduler
above tag \(U\) is precisely the Gibbs law

\[
 \Pr_Z(P)={\Pi_Z(P)\over D_U(Z)},                    \tag{2.3}
\]

followed by a uniform legal priority conditional on \(P\).

For a depth-one target \(v\), let \(I_v(P)\) be the indicator that the raw
grid of \(P\) uses \(v\), and put

\[
 B_1(P;Z)=\sum_{v\in Z^-_1\cup Z^+_1}I_v(P).         \tag{2.4}
\]

The first row-target marginals control only sums of \(I_v(P)\).  But after
adding two targets \(v,w\), the killed path mass contains

\[
 \boxed{
 C_U(v,w;Z)
 =\sum_{P\in\mathcal B(U)}
   \Pi_Z(P)I_v(P)I_w(P)
   \mathbf1_{\{B_1(P;Z)=0\}}.}                      \tag{2.5}
\]

This is a mixed second derivative, or susceptibility, of the blocker
generating polynomial.  It is not determined by

\[
 D_U(Z),\qquad
 \sum_P\Pi_Z(P)I_v(P),\qquad
 \sum_P\Pi_Z(P)I_w(P).                              \tag{2.6}
\]

The second-blocker term (2.5) is exactly what turns the two factors
\(g!\to(g-1)!\) into \((g-1)!\to0\).  After another bite, the drift of
\(C_U(v,w;Z)\) contains the triple term

\[
 \sum_P\Pi_Z(P)I_v(P)I_w(P)I_x(P),                  \tag{2.7}
\]

and so on.  Hence neither tag degrees nor all one-target row degrees form
a closed martingale state.

An exact closed object is the full multivariate polynomial

\[
 \mathscr F_U(\mathbf y)
 =\sum_{P\in\mathcal B(U)}
   \Pi_\varnothing(P)
   \prod_v y_v^{I_v(P)},                             \tag{2.8}
\]

together with the analogous variables at every depth and sign.  The
priority degree (2.2) is a deadline-dependent specialization of its entire
coefficient table.  Calling (2.8) an invariant merely restates the full
catalogue; it gives no low-dimensional propagation theorem.

## 3. A minimal rectangle-free cumulative obstruction

Write a return-free geodesic grid as

\[
 G_{i,j}
 =C\cup\{A_{i+1},\ldots,A_g\}
       \cup\{B_1,\ldots,B_j\}.                       \tag{3.1}
\]

Its owner path is \(X_t=G_{t,t}\), with physical flags

\[
 L_q(t)=G_{t+q,t},
 \qquad U_q(t)=G_{t-q,t}.                            \tag{3.2}
\]

### Lemma 3.1 (singleton-grid perturbations)

Fix a grid \(\mathcal G_0\) and finitely many distinct non-boundary cells
\(v_1,\ldots,v_k\).  If \(g=o(m^{2/3})\), then for fixed \(k\) and all
sufficiently large \(m\) there are coordinate images
\(\mathcal G_1,\ldots,\mathcal G_k\) such that

\[
 \mathcal G_0\cap\mathcal G_i=\{v_i\},              \tag{3.3}
\]

and the \(\mathcal G_i\) are pairwise disjoint as families of physical
sets.

#### Proof

Choose \(\sigma_i\) uniformly from the setwise stabilizer of \(v_i\) and
put \(\mathcal G_i=\sigma_i\mathcal G_0\).  For cells \(A,B\), the
probability that \(\sigma_i A=B\) is the reciprocal of the orbit size of
\(A\) under this stabilizer.  If \(A\ne v_i\) omits \(a\) coordinates of
\(v_i\) and uses \(b\) coordinates outside \(v_i\), this orbit size is

\[
 \binom{|v_i|}{a}\binom{2m-|v_i|}{b}.                \tag{3.4}
\]

For each fixed \(a+b=d\), the product grid has only \(O(d+1)\) cells at
that distance and only \(O(d+1)\) compatible target cells.  Summing the
reciprocals in (3.4) over \(d\ge1\) is \(o(1)\); the first term is
\(O(1/m)\), and the polynomial number of cells at growing distance is
dominated by the binomial orbit sizes.  The same estimate holds when one
also forbids equality with any of the previously chosen finitely many
grids.  Hence a choice avoiding every unwanted common cell exists.
\(\square\)

Choose two depth-one cells \(v_1,v_2\) in distinct phase columns of
\(\mathcal G_0\), and apply Lemma 3.1.  The selected owner paths on
\(\mathcal G_1,\mathcal G_2\) have no common physical target or owner.
Choose their priorities so that the phases carrying \(v_1,v_2\) have
height at least one; this is possible because exactly \(g-1\) phases have
depth-one height.

After those two paths are selected, the base path on \(\mathcal G_0\) has
two distinct first-row blocked phases.  Equations (0.1) and (1.7) give

\[
 \Pi_Z(\mathcal G_0)=0.                              \tag{3.5}
\]

Every pairwise grid intersection in this construction has size at most
one.  It contains no product rectangle, compressed or otherwise.  Thus
declaring every shared \(s\times s\) rectangle, even with \(s=2\), an
extra conflict does not prevent (3.5).

The point is cumulative: each old chunk is individually below the
deadline budget of the new chunk, but their blockers add in different
phase columns.

## 4. Chronology over owner-scale bites

One geodesic-grid owner-scale bite uses a \(\Theta(1/m)\) fraction of the
available row targets.  After \(k\) quasirandom bites the used fraction is
on the scale

\[
 f_k\asymp{k\over m}.                                \tag{4.1}
\]

A fresh length-\(g\) raw path then sees first-row blocker count of mean

\[
 \mathbb EB_1\asymp f_kg\asymp {kg\over m}.          \tag{4.2}
\]

Since the admissible count is one, an unaligned quasirandom residual
reaches the depth-one transition already at

\[
 k\asymp {m\over g}=o(m),                            \tag{4.3}
\]

long before the required \(\Theta(m)\) bites.  The exact priority weight
does favor zero-block paths: at depth one, a one-block path has only a
\(1/g\) fraction of the zero-block priority multiplicity.  But this tilt
does not itself prove that every tag retains comparable zero-block mass or
that every unused target retains comparable weighted degree.  Those are
precisely the mixed correlations in (2.5)--(2.7).

Rectangle pruning controls a large contribution from one earlier grid.
It does not control the sum of singleton contributions from
\(\Theta(k)\) different earlier grids.  Therefore the pruning is not an
invariant over the chronology (4.1)--(4.3).

## 5. A stronger deterministic bad residual

There is also a simple tag-shadow obstruction showing why global row
density cannot control every tag.  Fix a carrier \(U\) and forbid every
lower depth-one target contained in it:

\[
 Z^-_1(U)=\binom U{m-1}.                             \tag{5.1}
\]

Every geodesic chunk on \(U\) has all of its lower depth-one targets in
\(Z^-_1(U)\), so

\[
 D_U(Z^-_1(U))=0.                                    \tag{5.2}
\]

Nevertheless the forbidden fraction of the global row is

\[
 {\binom M{m-1}\over\binom{2m}{m-1}}=o(1)            \tag{5.3}
\]

indeed exponentially small.  Thus no potential based only on global row
entropy or density can imply uniform tag-degree lower bounds.

Equation (5.1) is a deterministic residual, not a claim that the random
scheduler typically creates this entire shadow.  Its role is to identify
the additional discrepancy statement a martingale proof would need: used
targets must remain dispersed relative to every carrier shadow, not merely
uniform in total count.

## 6. What an adequate potential would have to control

A plausible strong potential is an exponential blocker moment under the
current Gibbs law:

\[
 \mathcal H_t
 =\sum_U
   \mathbb E_{P\sim\Pr_{Z_t,U}}
   \exp\left\{
      \sum_{q=1}^Q\theta_q
      {B_q(P;Z_t)\over\bar d_q^{(g)}+1}
   \right\}.                                        \tag{6.1}
\]

To imply PDRC, one would need a stopped supermartingale estimate for
\(\mathcal H_t\), simultaneous lower bounds on every \(D_U(Z_t)\), and
the analogous tilted degree bound for every unused row target.

The one-step increment of (6.1) is not determined by current tag and
target degrees.  Expanding it produces exactly the mixed terms
(2.5)--(2.7).  A sufficient extra hypothesis would be a **multi-source
dispersal condition**: for every grid \(P\), depth \(q\), and family of
previously selected chunks, the number of distinct phase columns of \(P\)
hit by singleton intersections from that family must have exponential
tails at the scale \(\bar d_q^{(g)}\).

Pairwise rectangle exclusion is only the one-source part of this
condition.  The minimal residual (0.2)--(0.3) violates its two-source part.

## 7. Final status

The following statements are exact.

1. The priority partition function (2.2) is the correct entropy object.
2. Its drift is not closed by tag and one-target row degrees; mixed blocker
   susceptibilities are essential.
3. The modified depth-one deadline is exactly one.
4. Two rectangle-free singleton blockers from two earlier chunks are the
   minimal pathwise bad residual.
5. Quasirandom accumulation reaches this obstruction after
   \(\Theta(m/g)=o(m)\) owner-scale bites.
6. A vanishing global row shadow can annihilate one tag, so a uniform
   tag-degree theorem additionally needs carrier-shadow discrepancy.

Thus hereditary propagation is not proved for the rectangle-pruned
catalogue.  The next valid theorem must control a full multi-source
blocker potential such as (6.1), or impose an equivalent adaptive
dispersal rule.  Until then neither the \(O(m)\)-bite common matching nor
coefficient one follows.
