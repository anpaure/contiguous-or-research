# Return-free rectangle-pruned chunks: the weakest residual gate and a coordinate-star obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Outcome

Use the return-free chunk scale

\[
 g=(1-o(1))H,\qquad
 T_0=(1+o(1)){W\over g},
\tag{0.1}
\]

from Section 8 of
`MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md`.  A chunk is
a monotone geodesic grid

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
              \cup\{b_1,\ldots,b_j\},
\tag{0.2}
\]

with physical columns on the diagonal strip.  Declare two chunks
rectangle-incompatible if their full grids share a compressed
\(s\times s\) product subgrid.

There are three conclusions.

1. The uniform residual-degree and uniform residual-link clauses in PDRC
   are stronger than one bite needs.  The exact one-bite proof uses only:
   almost-everywhere tag viability, an aggregate owner collision energy,
   an aggregate rectangle-conflict energy, and one **reciprocal-slack
   weighted flag-link hazard**.  Theorem 3.1 proves this self-contained.
2. Choose any sufficiently slow \(\omega_m\to\infty\), and put
   \[
    \varepsilon_m={g\over m^{2/3}\omega_m},\qquad
    L_m=(\log m)^2,\qquad
    \alpha_0={\varepsilon_m\over L_mg}
      ={1\over m^{2/3}\omega_mL_m}.
   \]
   If the four quantities remain \(o(1)\) at every residual and
   \[
    \alpha_t={\alpha_0T_0\over|\mathcal A_t|},
   \]
   then \(O(1/\alpha_0)=o(m)\) bites leave only
   \(O(\alpha_0T_0)=o(T_0)\) chunk tags.
   This is the weakest proved conditional iteration in this note; it does
   not ask for multiplicative concentration of every small link.
3. The exact grid-intersection theorem supplies the per-pair bound
   \[
    \chi_q(P,F)\le(s-1)(2q+1).
   \]
   It does **not** propagate the aggregate hazard.  Deleting the single
   lower-depth-one coordinate star
   \[
    Z_1^-(x)=\{S\in\tbinom{[2m]}{m-1}:x\in S\}
   \]
   leaves every tag whose carrier omits \(x\) unchanged, but suppresses
   the degree of every tag whose carrier contains \(x\) by the factor
   \[
    O(H/m).
   \]
   Equivalently, conditioning on survival amplifies the noncore roles of
   \(x\) by \(\Theta(m/H)\).  The deleted star is only
   \((1/2+o(1))\) of one target row.  Rectangle pruning is pairwise and
   does not exclude this aligned accumulation.

Thus the rectangle catalogue gives bounded increments, not hereditary
drift.  A coefficient-one proof must propagate the aggregate hazard (or
an equivalent coordinate-cut discrepancy theorem) through the actual
partial-matching trajectory.

## 1. Residual laws and exact link quantities

Let \(\mathcal A\) be the current active chunk tags and put

\[
 n=|\mathcal A|.
\tag{1.1}
\]

Let \(Z\) record the already forbidden owner and flag targets and, when
rectangles are treated as extra conflicts, the previously selected full
grids.  For a tag \(\tau\), let \(\mathcal P_\tau(Z)\) be the return-free
base chunks above \(\tau\) whose owners avoid the old owner targets, whose
full grids are rectangle-compatible with the old selected grids, and
which admit at least one priority avoiding the old flag targets.  A tag is
**viable** if this family is nonempty.  On every viable tag choose an
arbitrary probability law \(\nu_\tau\) supported on
\(\mathcal P_\tau(Z)\).  The law may, in particular, be proportional to
the exact surviving priority count \(\Pi_Z(P)\).

For \(P\sim\nu_\tau\), write \(O(P)\) for its \(g\) middle owners and
write

\[
 F_{r}^{\epsilon}(P),\qquad
 1\le r\le Q,\quad \epsilon\in\{-,+\},
\tag{1.2}
\]

for its raw signed depth-\(r\) row.  Each such row has one target in each
physical phase column.  Define the owner load

\[
 \mu_X=\sum_{\tau\ {\rm viable}}
       \Pr_{P\sim\nu_\tau}(X\in O(P)).
\tag{1.3}
\]

For two chunks define the raw common-cell count through depth \(q\) by

\[
 \chi_q(P,F)
 =\sum_{\epsilon\in\{-,+\}}\sum_{r=1}^q
   |F_r^\epsilon(P)\cap F_r^\epsilon(F)|.
\tag{1.4}
\]

This may count several common cells in one phase column.  It therefore
upper-bounds, which is the useful direction, the number of columns of
\(P\) newly blocked by \(F\) through depth \(q\).

Activate tags independently with probability \(\alpha\), and choose
their chunks independently from the laws \(\nu_\tau\).  Conditional on a
fixed active chunk \(P\) above \(\tau\), put

\[
 b_q(P)
 =\alpha\sum_{\upsilon\ne\tau}
   \mathbb E_{F\sim\nu_\upsilon}\chi_q(P,F).
\tag{1.5}
\]

Let \(\mathcal Y\) be the raw flag targets used by the other activated
chunks, before any colliding paths are discarded, and define the monotone
overcount

\[
 C_q(P)=\#\{t:\text{for some }r\le q,\epsilon\in\{-,+\},
                   \ F_r^\epsilon(P,t)\in\mathcal Y\}.
\tag{1.6}
\]

This counts the phase even if it was already blocked by \(Z\).  Therefore

\[
 B_q^{Z\cup\mathcal Y}(P)\le B_q^Z(P)+C_q(P),
\tag{1.7}
\]

and

\[
 \boxed{\mathbb E(C_q(P)\mid P\hbox{ active})\le b_q(P).}
\tag{1.8}
\]

No independence between the individual cells of \(P\) is asserted or
needed.

Let

\[
 B_q^Z(P)=\#\{\hbox{phases first blocked by }Z
                    \hbox{ at depth at most }q\}
\tag{1.9}
\]

and define the old deadline slack

\[
 \sigma_q(P)=\bar d_q^{(g)}-B_q^Z(P)\ge0.
\tag{1.10}
\]

The inequality follows from the definition of
\(\mathcal P_\tau(Z)\).

## 2. The reciprocal-slack residual gate

Partition \([Q]\) into consecutive intervals \(I\).  Denote the right
endpoint of \(I\) by \(q_I\), and put

\[
 \sigma_I(P)=\min_{q\in I}\sigma_q(P).
\tag{2.1}
\]

For the initial calculation one takes the usual dyadic partition in
which \(\Lambda_q\) changes by a factor at most two inside one interval.
There are \(O(\log m)\) such intervals.

Define the reciprocal-slack hazard

\[
 \boxed{
 \mathfrak H_Z(\alpha)
 =\sum_{\tau\ {\rm viable}}
   \mathbb E_{P\sim\nu_\tau}
   \sum_I
   \min\left\{1,
    {b_{q_I}(P)\over \sigma_I(P)+1}\right\}.}
\tag{2.2}
\]

Let \(\mathfrak R_s\) be the expected number of rectangle-incompatible
pairs before activation:

\[
 \mathfrak R_s
 =\sum_{\tau<\upsilon}
   \Pr_{P\sim\nu_\tau,F\sim\nu_\upsilon}
   (P,F\hbox{ share a compressed }s\times s\hbox{ grid}).
\tag{2.3}
\]

If the catalogue has already been globally rectangle-pruned, then
\(\mathfrak R_s=0\).  If rectangles are merely declared additional
conflicts, (2.3) is the exact extra energy which must be controlled.

### Definition 2.1 (RSH: residual sampled-hazard gate)

The residual has RSH with error \(\varepsilon\) at bite probability
\(\alpha\) if

\[
 |\{\tau\in\mathcal A:\tau\hbox{ is not viable}\}|
 \le\varepsilon n,
\tag{2.4}
\]

\[
 \alpha\sum_X\mu_X^2\le\varepsilon n,
\tag{2.5}
\]

\[
 \alpha\mathfrak R_s\le\varepsilon n,
\tag{2.6}
\]

and

\[
 \mathfrak H_Z(\alpha)\le\varepsilon n.
\tag{2.7}
\]

This is weaker than PDRC in three ways.  Degrees need not be equal among
viable tags, no individual pair link must follow a product trajectory,
and paths with small slack are allowed provided their reciprocal-slack
weighted collision mass is negligible in aggregate.

RSH is not asserted to be logically necessary.  It is the weakest
explicit collection of residual inequalities used by the proof below:
removing any one of (2.4)--(2.7) leaves one of its four deletion ledgers
uncontrolled.

## 3. A self-contained one-bite and \(O(m)\)-bite theorem

### Theorem 3.1 (one bite under RSH)

Suppose the current residual has RSH with error \(\varepsilon=o(1)\), and
\(0<\alpha\le1/2\).  Then there is a family of

\[
 \boxed{(1-O(\varepsilon))\alpha n}
\tag{3.1}
\]

new chunks such that:

1. their owners are mutually disjoint;
2. no two selected full grids share a compressed \(s\times s\) subgrid;
3. every selected chunk has a priority which avoids all old forbidden
   targets; and
4. all newly claimed signed flags are mutually distinct through depth
   \(Q\).

#### Proof

Do not activate the nonviable tags.  Activate every viable tag with
probability \(\alpha\), independently, and sample its chunk from
\(\nu_\tau\).  The expected number of activated chunks is at least

\[
 \alpha(1-\varepsilon)n.
\tag{3.2}
\]

The expected number of activated owner-collision pairs is at most

\[
 {\alpha^2\over2}\sum_X\mu_X^2.
\tag{3.3}
\]

Deleting both endpoints of every such pair therefore costs in expectation
at most

\[
 \alpha^2\sum_X\mu_X^2\le\varepsilon\alpha n.
\tag{3.4}
\]

Similarly, deleting both endpoints of every rectangle-incompatible pair
costs in expectation at most

\[
 2\alpha^2\mathfrak R_s\le2\varepsilon\alpha n.
\tag{3.5}
\]

Fix an activated chunk \(P\).  If a new deadline violation occurs at some
\(q\in I\), then, because \(C_q(P)\) is nondecreasing in \(q\),

\[
 C_{q_I}(P)\ge C_q(P)\ge\sigma_q(P)+1
                         \ge\sigma_I(P)+1.
\tag{3.6}
\]

Markov's inequality and (1.8) give

\[
 \Pr(P\hbox{ becomes deadline-bad}\mid P\hbox{ active})
 \le
 \sum_I\min\left\{1,
 {b_{q_I}(P)\over\sigma_I(P)+1}\right\}.
\tag{3.7}
\]

After averaging over tags and chunks, (2.7) shows that the expected number
of activated deadline-bad chunks is at most

\[
 \alpha\mathfrak H_Z(\alpha)\le\varepsilon\alpha n.
\tag{3.8}
\]

Delete them.  Deleting chunks can only remove owner, rectangle, and flag
collisions.

For every remaining chunk,

\[
 B_q^Z(P)+C_q(P)\le\bar d_q^{(g)}qquad(q\le Q).
\tag{3.9}
\]

The exact deadline Hall theorem supplies a priority avoiding all old
blockers and every new duplicated raw target.  If a raw target is used by
two remaining chunks, then each of its phase columns was counted as newly
blocked at that depth, so neither occurrence is claimed by the supplied
priorities.  The newly claimed targets are therefore mutually distinct.

Subtracting (3.4), (3.5), and (3.8) from (3.2), and choosing an outcome at
least as good as its expectation, proves (3.1). \(\square\)

### Corollary 3.2 (conditional \(o(m)\)-bite completion)

Suppose RSH holds with one uniform \(\eta_m=o(1)\) after every
chosen bite while

\[
 n_t\ge 2\alpha_0T_0.
\tag{3.10}
\]

At time \(t\), take

\[
 \alpha_t={\alpha_0T_0\over n_t}\le{1\over2}.
\tag{3.11}
\]

Then after at most

\[
 {1\over(1-O(\eta_m))\alpha_0}
 =O(m^{2/3}\omega_m\log^2m)=o(m)
\tag{3.12}
\]

bites, only

\[
 O(\alpha_0T_0)=o(T_0)
\tag{3.13}
\]

chunk tags remain.

#### Proof

By Theorem 3.1, every successful bite selects at least

\[
 (1-O(\eta_m))\alpha_0T_0
\]

new tags, independent of the current value of \(n_t\).  Sum this constant
decrement until (3.10) fails. \(\square\)

Since \(gT_0=(1-o(1))W\), the middle-owner cost of the final leave is

\[
 g\,O(\alpha_0T_0)=O(\alpha_0W)=o(W).
\tag{3.14}
\]

Thus RSH is quantitatively sufficient for the coefficient-one owner and
all-row ledger, modulo the already recorded reset, remainder, and
deadline-modification terms.

## 4. What exact rectangle pruning proves

The intersection of two full geodesic grids is a sublattice of each
product of two chains.  If it has width \(w\), closure under meet and join
produces a compressed \(w\times w\) subgrid.  Therefore, for a
rectangle-compatible pair,

\[
 \operatorname{width}(\mathcal G(P)\cap\mathcal G(F))\le s-1.
\tag{4.1}
\]

Restrict to the \(2q+1\) Boolean ranks from \(m-q\) through \(m+q\).
Every chain contains at most one set of each rank.  Dilworth's theorem
gives

\[
 |\mathcal G(P)\cap\mathcal G(F)\cap
   \{|S|\in[m-q,m+q]\}|
 \le(s-1)(2q+1).
\tag{4.2}
\]

The cells counted by \(\chi_q(P,F)\) are a subfamily of the left side.
Hence

\[
 \boxed{\chi_q(P,F)\le(s-1)(2q+1).}
\tag{4.3}
\]

This is exactly the bounded-increment statement needed by any later
Freedman or stopped-energy proof.  It also explains why long shared chains
are harmless in one pair while wide shared rectangles are dangerous.

However, (4.3) does not bound the sum in (1.5).  Many different chunks may
meet \(P\) in different width-one chains or in different isolated cells.
Their union may block all \(g\) phase columns.  In abstract grid language
this is sharp: the shifted diagonal

\[
 \{G_{t+1,t}:0\le t<g\}
\tag{4.4}
\]

contains one lower-depth-one cell in every column and contains no
\(2\times2\) product rectangle.  Thus a union of isolated
rectangle-compatible intersections can have

\[
 B_1(P)=g
\tag{4.5}
\]

even though every individual intersection has width one.  Rectangle
pruning controls jumps of the hazard, not its accumulated drift.

### Proposition 4.1 (minimal two-source failure)

For all sufficiently large \(m\), there are three return-free grids
\(\mathcal G_0,\mathcal G_1,\mathcal G_2\) and two depth-one cells
\(v_1,v_2\) in distinct columns of \(\mathcal G_0\) such that

\[
 \mathcal G_0\cap\mathcal G_i=\{v_i\}\quad(i=1,2),
 \qquad
 \mathcal G_1\cap\mathcal G_2=\varnothing.
\tag{4.6}
\]

The grids \(\mathcal G_1,\mathcal G_2\) can be assigned priorities which
claim \(v_1,v_2\).  After selecting them, the base path on
\(\mathcal G_0\) has

\[
 B_1(\mathcal G_0)=2>\bar d_1^{(g)}=1
\tag{4.7}
\]

and therefore has zero residual priority degree, although every pair in
(4.6) is rectangle-compatible even for \(s=2\).

#### Proof

The singleton-grid perturbation lemma in
MATH_ATTACK_RECTANGLE_PRUNED_GEODESIC_HEREDITARY_POTENTIAL_20260725.md
applies because \(g=o(m^{2/3})\).  Apply it to two distinct nonboundary
depth-one cells of \(\mathcal G_0\), obtaining (4.6).  Exactly \(g-1\)
phase columns of a chunk may claim depth one, so choose priorities on
\(\mathcal G_i\) which claim \(v_i\).  The exact return-free deadline is
\(\bar d_1^{(g)}=1\), proving (4.7). \(\square\)

This is an actual two-chunk partial-matching residual, not merely an
abstract deletion pattern.  It kills only one prescribed base path, so it
does not by itself violate the aggregate RSH gate.  It does prove that no
pathwise hereditary-slack theorem can follow from pairwise rectangle
pruning.

The failure is also algebraically unclosed.  At depth one the priority
weights are
\[
 g!,\quad (g-1)!,\quad 0
\]
for zero, one, and at least two blocked columns.  If \(I_v(P)\) records
that the raw grid of \(P\) uses \(v\), the second-blocker drift contains
\[
 C_U(v,w;Z)
 =\sum_P\Pi_Z(P)I_v(P)I_w(P)
   \mathbf1_{\{B_1(P;Z)=0\}}.
\tag{4.8}
\]
This mixed susceptibility is not determined by tag degrees and the two
one-target degrees.  Its next drift contains the corresponding triple
term.  Thus (4.3) bounds each summand geometrically but does not close the
martingale state; RSH deliberately retains the required multi-source
average in (2.2).

## 5. The empty residual passes the nonrectangle part of RSH

At \(Z=\varnothing\), take the symmetric uniform chunk law.  Every owner
has load

\[
 \mu_X={gT_0\over W}=1-o(1).
\tag{5.1}
\]

Consequently, for

\[
 \varepsilon_m={g\over m^{2/3}\omega_m},\qquad
 L_m=(\log m)^2,\qquad
 \alpha_0={\varepsilon_m\over L_mg},
\tag{5.2}
\]

one has

\[
 {\alpha_0\sum_X\mu_X^2\over T_0}
 =O(\alpha_0g)
 =O(\varepsilon_m/L_m)=o(1).
\tag{5.3}
\]

Likewise a raw signed depth-\(r\) target has load

\[
 (1+o(1))\lambda_r.
\tag{5.4}
\]

Therefore, uniformly in \(P\),

\[
 b_q(P)\le(2+o(1))\alpha_0 g\Lambda_q
 ={(2+o(1))\varepsilon_m\over L_m}\Lambda_q.
\tag{5.5}
\]

The enlarged chunk deadline satisfies

\[
 \bar d_q^{(g)}\ge
 \min\left\{g,
  \left\lceil\varepsilon_m\Lambda_q\right\rceil
 \right\}.
\tag{5.6}
\]

On the dyadic \(\Lambda\)-partition, (5.5)--(5.6) give a hazard per tag at
most

\[
 O\left({\log m\over L_m}\right)=o(1).
\tag{5.7}
\]

Thus (2.5) and (2.7) hold initially.  If a globally rectangle-compatible
subcatalogue with the same symmetric marginal laws is supplied, then
(2.6) is zero as well.  If rectangles are only extra conflicts, the
degree estimate for \(\mathfrak R_s\) remains a separate static theorem;
the product-grid width lemma alone does not estimate its frequency.

The balanced-pruning theorem in
RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md shows that a bound
\[
 {\Delta_{\square(s)}+1\over d}
 =o\left({1\over Q^2\log m}\right)
\]
would produce a rectangle-free subcatalogue with only \(o(W)\) weighted
exceptional fibres.  Conditional on that still-missing rectangle census,
it supplies (2.4) and makes (2.6) zero at time zero.  Fibre lower bounds
alone do not imply the owner \(L^2\) energy (2.5) or the
reciprocal-slack hazard (2.7); those must still be checked for the pruned
marginal laws.

More generally, at active density \(u=n/T_0\), an ideally uniform
residual has target loads reduced by \(u\).  With the constant-throughput
bite

\[
 \alpha={\alpha_0\over u},
\tag{5.8}
\]

the product \(\alpha u=\alpha_0\) is unchanged.  Hence the numerical
owner and reciprocal-slack ledgers remain exactly at the initial scale.
The missing statement is not numerical; it is propagation of this
uniformity against aligned residuals.

## 6. A sharp coordinate-star residual amplification

Fix a coordinate \(x\in[2m]\), and forbid precisely the lower
depth-one star

\[
 Z_1^-(x)
 =\{S\in\tbinom{[2m]}{m-1}:x\in S\}.
\tag{6.1}
\]

Its density in that row is

\[
 {|Z_1^-(x)|\over\binom{2m}{m-1}}
 ={m-1\over2m}={1\over2}+o(1).
\tag{6.2}
\]

### Proposition 6.1 (coordinate-star degree split)

Let \(D_U(\varnothing)\) be the initial decorated degree above a chunk
tag with carrier \(U\), and let \(D_U(Z_1^-(x))\) be its residual degree.
For the symmetric return-free geodesic catalogue,

\[
 x\notin U
 \quad\Longrightarrow\quad
 D_U(Z_1^-(x))=D_U(\varnothing),
\tag{6.3}
\]

whereas

\[
 x\in U
 \quad\Longrightarrow\quad
 {D_U(Z_1^-(x))\over D_U(\varnothing)}
 \le {H+g\over M}=O(H/m)=o(1).
\tag{6.4}
\]

#### Proof

If \(x\notin U\), every grid cell is a subset of \(U\), so no lower flag
belongs to (6.1).  This proves (6.3).

Suppose \(x\in U\).  In the ordered partition

\[
 U=C\ \dot\cup\ A\ \dot\cup\ B\ \dot\cup\ R,
\qquad |C|=m-g,\quad |A|=|B|=g,\quad |R|=H-g,
\tag{6.5}
\]

the symmetric catalogue puts \(x\) in \(C\) on exactly the fraction

\[
 {|C|\over|U|}={m-g\over M}
\tag{6.6}
\]

of its base chunks.  If \(x\in C\), then every physical lower-depth-one
flag

\[
 L_1(t)=G_{t+1,t}
\tag{6.7}
\]

contains \(x\).  Hence

\[
 B_1^{Z_1^-(x)}(P)=g.
\tag{6.8}
\]

On the other hand,

\[
 \boxed{\bar d_1^{(g)}=1.}
\tag{6.9}
\]

Indeed, \(T_0\le W/g\) and
\[
 R_1={m\over m+1}W
\]
give \(R_1/T_0>g-1\), so \(d_1^{(g)}\le1\).  Moreover
\[
 0<\varepsilon_m\Lambda_1=o(1),
\]
so the enlarged integer floor is one.  Thus no priority of a base chunk
with \(x\in C\) survives.  Discarding all
such chunks leaves at most the complementary fraction

\[
 1-{m-g\over M}={H+g\over M},
\]

which proves (6.4). \(\square\)

Conditioning a surviving chunk above a carrier containing \(x\) therefore
forces \(x\) into \(A\cup B\cup R\).  Its probability of a noncore role
has risen from

\[
 {H+g\over M}=\Theta(H/m)
\]

to one.  The exact residual amplification factor is

\[
 \boxed{\Theta(m/H).}
\tag{6.10}
\]

This example does not claim that the coordinate star is already known to
be the used-target set of an actual partial matching.  It proves the
logically necessary point: static grid intersections, row cardinalities,
and pairwise rectangle pruning do not imply a hereditary degree or link
theorem.  A proof for the actual random trajectory must add a martingale
which rules out coordinate-cut concentration such as (6.1).

The example is also invisible to the pairwise rectangle bound.  The
forbidden object is a union of isolated row targets contributed over many
earlier choices; no one earlier grid need share a wide rectangle with the
current grid.

## 7. Correct coefficient-one frontier

The return-free rescaling and rectangle geometry improve the dynamic
problem in two concrete ways:

* the bite can have constant throughput \(\Theta(\alpha_0T_0)\), giving
  an \(O(1/\alpha_0)=o(m)\)-round ledger; and
* rectangle pruning bounds every pairwise flag-link increment by (4.3).

The exact remaining theorem is now smaller than PDRC:

> Along the actual constant-throughput partial-matching process, choose
> residual laws \(\nu_\tau\) for which the four RSH quantities
> (2.4)--(2.7) are \(o(1)\) uniformly until only
> \(O(\alpha_0T_0)\) tags remain.

Theorem 3.1 and Corollary 3.2 then give the common owner/flag matching and
the coefficient-one ledger.  The static geodesic hierarchy and the
rectangle width lemma verify only the initial scale and bounded
increments.  Propositions 4.1 and 6.1 show sharply why a new
multi-source/coordinate-cut or aggregate-hazard martingale is
indispensable.
