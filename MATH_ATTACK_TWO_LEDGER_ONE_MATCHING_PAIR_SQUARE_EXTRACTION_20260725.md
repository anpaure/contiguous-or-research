# Two-ledger extraction and the one-matching pair-square gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

There are three distinct statements.

1. A proper coloring with palette excess \(o(D/Q)\) contains one color
   which simultaneously misses \(o(T/Q)\) tags and has \(o(W)\)
   exceptional-target incidence.  This is an exact two-ledger averaging
   theorem; choosing merely a largest color is insufficient.
2. A complete coloring is stronger than necessary.  Any probability law
   on single matchings with the same two expected ledgers contains one
   deterministic matching satisfying both.  Together with the calibrated
   row deficits, that matching is a cyclic-interval near-design with
   \(o(W)\) holes.
3. The raw geodesic pair-square kernel is relevant to constructing such a
   one-column matching.  It detects the undiluted projective-plane cut:
   that cut has normalized squared row energy \(1-o(1)\), whereas the raw
   geodesic rows vanish.  It does not yet prove the matching.  The estimate
   is not inherited by the isolated-pruning fractional point, it is not
   known under the tilted residual laws of a sequential matching process,
   and even ideal \(z^{-2}\) inflation is too weak at residual density
   \(z=1/Q\).

Thus complete color resolution can be replaced by a one-matching theorem,
but the presently proved pair-square estimate does not establish that
theorem.  The exact remaining input is a hereditary weighted pair-square
or transfer-energy estimate through tag residual \(o(1/Q)\), or a
chain-aligned reserve beginning at a substantially larger residual.

## 1. The coefficient-scale setup

Let \(\mathcal T\) be the original tag set, \(|\mathcal T|=T\), and let
\(\mathcal T_g\) be the good tags from the pointwise isolated pruning.
Write \(T_g=|\mathcal T_g|\).  Let \(V_g\) be the nonexceptional protected
targets and \(V_{\rm exc}=V\setminus V_g\).  The corrected pruning gives

\[
 T-T_g=o(T/Q),
 \qquad |V_{\rm exc}|=o(W),
 \tag{1.1}
\]

and a rational fibre point \((x_e)\) satisfying

\[
 \sum_{e\ni U}x_e=1\quad(U\in\mathcal T_g),
 \qquad
 \sum_{e\ni v}x_e\le1+3\delta\quad(v\in V_g),
 \tag{1.2}
\]

where

\[
 \delta=m^{-2/3},
 \qquad Q\delta=o(1).
 \tag{1.3}
\]

The total fractional incidence with exceptional targets is

\[
 I_{\rm exc}
 :=\sum_e x_e b(e)=o(W),
 \qquad
 b(e):=|C(e)\cap V_{\rm exc}|.
 \tag{1.4}
\]

Choose a common denominator \(D\) and put \(m_e=Dx_e\).  Then

\[
 \sum_{e\ni U}m_e=D,
 \qquad
 \sum_{e\ni v}m_e\le(1+3\delta)D,
 \qquad
 \sum_em_eb(e)=DI_{\rm exc}=o(DW).
 \tag{1.5}
\]

Equivalently, the rescaled point

\[
 \widehat x_e={x_e\over1+3\delta}
 \tag{1.6}
\]

is a genuine fractional matching on \(V_g\), and its total tag deficit,
including the discarded tags, is

\[
 \sum_{U\in\mathcal T}
 \left(1-\sum_{e\ni U}\widehat x_e\right)
 ={3\delta\over1+3\delta}T_g+(T-T_g)
 =o(T/Q).
 \tag{1.7}
\]

Every matching below is a matching in the tag and \(V_g\) coordinates.
Exceptional targets are deliberately not conflict vertices; their use is
charged by \(b(e)\).

## 2. Exact two-ledger color extraction

The next theorem is independent of the geodesic structure.

### Theorem 2.1 (two-ledger color extraction)

Let a tag-target multihypergraph have \(T_g\) tags of degree exactly \(D\),
and let its edge-copies have nonnegative costs \(b(e)\).  Suppose it has a
proper coloring with \(C\ge D\) colors.  Put

\[
 B=\sum_e m_eb(e).
 \tag{2.1}
\]

For every \(0<\theta<1\), some color class \(M\) satisfies

\[
 \boxed{
 T_g-|M|
 \le {T_g(C-D)\over\theta C},}
 \tag{2.2}
\]

and

\[
 \boxed{
 \sum_{e\in M}b(e)
 \le {B\over(1-\theta)C}.}
 \tag{2.3}
\]

In particular, \(\theta=1/2\) loses only a factor two in both ledgers.

#### Proof

For a color \(c\), let \(r_c\) be the number of missed tags and let

\[
 h_c=\sum_{e\text{ of color }c}b(e).
\]

The \(D\) copies through any one tag receive \(D\) different colors.
Consequently

\[
 \sum_{c=1}^C r_c=T_g(C-D).
 \tag{2.4}
\]

Every edge-copy occurs in exactly one color, so

\[
 \sum_{c=1}^C h_c=B.
 \tag{2.5}
\]

Let \(\bar r=T_g(C-D)/C\) and \(\bar h=B/C\).  If both are positive, the
average over colors of

\[
 \theta{r_c\over\bar r}
 +(1-\theta){h_c\over\bar h}
 \tag{2.6}
\]

is one.  Some color makes (2.6) at most one, and each nonnegative summand
then gives (2.2)--(2.3).  If either average is zero, its corresponding
variable vanishes for every color, and the same proof applies to the other
variable. \(\square\)

### Corollary 2.2 (coefficient-one color scale)

In the protected catalogue, assume

\[
 C-D=o(D/Q).
 \tag{2.7}
\]

Then Theorem 2.1 and (1.5) give one color \(M\) for which

\[
 T-|M|=o(T/Q),
 \qquad
 \sum_{e\in M}b(e)=o(W).
 \tag{2.8}
\]

#### Proof

Take \(\theta=1/2\).  Equation (2.2) is \(o(T/Q)\), and (2.3) is
\(o(DW)/C=o(W)\).  Add the \(T-T_g=o(T/Q)\) exceptional tags. \(\square\)

This proves precisely why a \((1+o(1))D\) coloring is insufficient.  The
relative palette excess must be \(o(1/Q)\), unless a separate reserve
repairs the omitted tag rows.

## 3. Complete coloring is unnecessary

The same averaging works directly for one randomized matching.

### Theorem 3.1 (two-ledger one-matching extraction)

Let \(\mathbf M\) be any random matching in the tag and \(V_g\)
coordinates.  Put

\[
 R(\mathbf M)=T_g-|\mathbf M|,
 \qquad
 H(\mathbf M)=\sum_{e\in\mathbf M}b(e).
 \tag{3.1}
\]

If

\[
 \mathbb ER(\mathbf M)=a,
 \qquad
 \mathbb EH(\mathbf M)=h,
 \tag{3.2}
\]

then for every \(0<\theta<1\) there is one outcome \(M\) such that

\[
 \boxed{R(M)\le a/\theta,}
 \qquad
 \boxed{H(M)\le h/(1-\theta).}
 \tag{3.3}
\]

Hence expectations

\[
 a=o(T/Q),
 \qquad h=o(W)
 \tag{3.4}
\]

already give a deterministic coefficient-one matching.

#### Proof

Average

\[
 \theta R(\mathbf M)/a+(1-\theta)H(\mathbf M)/h
\]

and argue exactly as in Theorem 2.1, with the zero cases treated
separately. \(\square\)

Thus a full palette resolution is only one way to manufacture the law
\(\mathbf M\).  A sequential geodesic nibble or random-priority greedy
process may target (3.4) directly.  The fractional point \(\widehat x\)
is not itself such a law: decomposing it into large integral matchings is
exactly the matching-integrality problem, and the projective example shows
that vertex capacities alone do not perform this decomposition.

## 4. From the two ledgers to a cyclic-interval near-design

Let the protected target strata be \(V_i\), and suppose every legal chunk
claims exactly \(k_i\) targets in stratum \(i\).  Put

\[
 K=\sum_i k_i.
 \tag{4.1}
\]

The calibrated floor, capped-row, and deadline ledgers give

\[
 \Delta_{\rm cal}
 :=\sum_i\bigl(|V_i|-k_iT\bigr)=o(W),
 \tag{4.2}
\]

with the summands interpreted after including the already recorded scalar
deletions.  In particular they are nonnegative capacity deficits in the
calibrated system.  Also

\[
 K=O(gQ),
 \qquad gT=(1+o(1))W.
 \tag{4.3}
\]

### Theorem 4.1 (near-design ledger)

Suppose \(M\) is a matching in the tag and \(V_g\) coordinates and

\[
 T-|M|=r,
 \qquad
 h=\sum_{e\in M}|C(e)\cap V_{\rm exc}|.
 \tag{4.4}
\]

Then the total number of uncovered protected targets is at most

\[
 \boxed{
 \Delta_{\rm cal}+Kr+h.}
 \tag{4.5}
\]

There are no repeated nonexceptional targets.  Consequently, if

\[
 r=o(T/Q),
 \qquad h=o(W),
 \tag{4.6}
\]

the chosen legal geodesic chunks form a cyclic-interval near-design with
\(o(W)\) holes across all protected ranks.

#### Proof

Because \(M\) is a matching on \(V_g\), its number of distinct covered
good targets is exactly

\[
 \sum_{e\in M}|C(e)\cap V_g|=K|M|-h.
 \tag{4.7}
\]

The total protected target count is \(KT+\Delta_{\rm cal}\).  Ignoring
any exceptional targets which happen to be covered only decreases the
number credited as covered.  Hence the number of holes is at most

\[
 KT+\Delta_{\rm cal}-(K|M|-h)
 =\Delta_{\rm cal}+Kr+h,
\]

proving (4.5).  Under (4.6),

\[
 Kr=O(gQ)o(T/Q)=o(gT)=o(W).
\]

Every selected edge is a literal geodesic chunk, so its protected flags
are the prescribed consecutive intersection/union cyclic intervals.  This
proves the last assertion. \(\square\)

The theorem concerns the near-design itself.  Concatenating its chunks
into one literal word still uses the separately audited reset/bridge
ledger.

## 5. What the pair-square kernel sees

For a fractional path measure \(x\), define target loads and pair loads by

\[
 \ell(u)=\sum_{e\ni u}x_e,
 \qquad
 c(u,v)=\sum_{e\supseteq\{u,v\}}x_e,
 \tag{5.1}
\]

and define the symmetrically normalized off-diagonal kernel

\[
 \mathcal K_x(u,v)
 ={c(u,v)\over\sqrt{\ell(u)\ell(v)}}.
 \tag{5.2}
\]

The kernel is invariant under multiplying every edge weight by one common
positive scalar.  Thus the pointwise-pruned point may be replaced here by
the genuine fractional matching \(\widehat x\) from (1.6).

This kernel sees the arrangement of singleton edge intersections which is
invisible to

\[
 w^{|e\cap f|}-1-(w-1)|e\cap f|.
\]

### Proposition 5.1 (projective energy is order one)

For the projective construction with \(R\) disjoint planes of order
\(q\), line size \(k=q+1\), and uniform edge weight \(1/R\), every
projective target \(u\) satisfies

\[
 \boxed{
 \sum_{v\ne u}\mathcal K_x(u,v)^2
 =1-{1\over k}.}
 \tag{5.3}
\]

#### Proof

The load of every projective point is \(k/R\).  Any two different points
in its plane lie on one common line, so their pair load is \(1/R\).  Thus

\[
 \mathcal K_x(u,v)=1/k
\]

for the \(q^2+q=k^2-k\) other points in that plane, and it is zero for
points in the other planes.  Summing the squares gives (5.3). \(\square\)

There is also a scale-sensitive version.  Suppose every line support in
the same \(R\)-plane system has fractional mass \(a\), possibly inside a
larger fractional point, and all target loads are at most one.  Give weight
one to the projective supports and zero to all other supports.  Their
weighted matching-cut ratio is at least

\[
 \gamma={aRN\over R}=aN.
 \tag{5.4}
\]

For two projective points in one plane the pair load is at least \(a\),
and normalization by target loads at most one can only increase it.  Hence
every projective target row satisfies

\[
 \boxed{
 \sum_{v\ne u}\mathcal K_x(u,v)^2
 \ge(N-1)a^2
 =(1-o(1)){\gamma^2\over N}.}
 \tag{5.5}
\]

Thus an upper row-square bound \(\sigma^2\) gives at best
\(\gamma\le(1+o(1))\sigma\sqrt N\).  A scalar pair-square estimate does
not automatically give the \(1+o(1/Q)\) weighted matching cut.

By contrast, the raw symmetrized geodesic catalogue satisfies

\[
 \sum_{v:|v|=|u|,\ v\ne u}\mathcal K(u,v)^2=O(m^{-2})
 \tag{5.6}
\]

and the factorial rank-gap bounds

\[
 \sum_{v:|v|=|u|+h}\mathcal K(u,v)^2
 \le C(|h|+1)^2|h|!(C/m)^{|h|}.
 \tag{5.7}
\]

In particular its total block \(\ell_2\)-norm sum is
\(O(m^{-1/2})\).  Therefore the actual raw pair-square kernel excludes an
undiluted projective-plane component.  This is genuine information beyond
the protected width-two intersection moment.  On the other hand, using
only the total row-square consequence \(\sigma^2=O(1/m)\) and
\(N\asymp K^2=m^{2+o(1)}\), (5.5) permits \(\gamma=m^{1/2+o(1)}\).
Any sharp exclusion must use the factorial rank-block profile, not merely
its scalar sum.

## 6. Why the raw kernel still does not give the matching

There are three separate gaps.

### 6.1 It is not the kernel of the pointwise-pruned fractional point

Equations (5.6)--(5.7) are proved for the raw symmetrized catalogue,
normalized by its raw target degrees.  The isolated-pruning point uses only

\[
 \mu=m^{11/6-o(1)}
 \tag{6.1}
\]

distinct alternatives per good tag, each with weight

\[
 x_e={1\over A'_U}
 ={m^{-11/6+o(1)}}.
 \tag{6.2}
\]

For any two good targets \(u,v\) in one retained path,

\[
 c(u,v)\ge x_e,
 \qquad
 \mathcal K_x(u,v)^2
 \ge {x_e^2\over(1+3\delta)^2}
 =m^{-11/3+o(1)}.
 \tag{6.3}
\]

For a fixed rank gap \(|h|=4\), the raw bound (5.7) is \(O(m^{-4})\).
Thus (5.7) cannot be inherited unchanged by the pruned point whenever a
retained chunk contains such a good target pair.  More generally, the
polynomial atom weight imposes a pair-square floor absent from the raw
catalogue.  A weighted pair-square theorem for the selected pruning outcome
must be proved separately; the raw formula cannot simply be rescaled.

Accordingly, the viable interpretation of the pair-square route is to run
the one-column process in the original high-entropy catalogue and impose
bad-intersection quarantine dynamically.  It is not a consequence of
scaling the polynomial-support isolated-pruning point.

### 6.2 One matching still creates a tilted residual law

Avoiding complete coloring removes palettes, but it does not remove
conditioning.  In a sequential matching process, accepted chunks delete
targets and quarantine competing paths.  The remaining distribution in a
tag fibre can concentrate on a rare correlated subcatalogue.

The exact weighted square at step \(t\) is

\[
 J_t(F)
 =\sum_{P,P'\in F}p_{t,F}(P)p_{t,F}(P')K_t(P,P'),
 \tag{6.4}
\]

where \(p_{t,F}\) is the current tilted path law and \(K_t(P,P')\) is the
common-killer kernel.  This is the Efron--Stein variance term for one
column.  The raw pair-square estimate corresponds only to the initial
uniform law.  No proved inequality currently dominates (6.4) for all
later \(p_{t,F}\).

Sequential quarantine eliminates simultaneous bad-pair alterations, but
not (6.4).  With exact relative fibre losses \(I_{s,F}\), the surviving
martingale gate is

\[
 \boxed{
 \sum_F\operatorname{wt}(F)
 \mathbb E\sum_s I_{s,F}^2=o(W\zeta^2),}
 \tag{6.5}
\]

for the tolerance \(\zeta\) used to declare exceptional fibres.  This is
the one-matching, rather than full-color, form of the hereditary
pair-square problem.

### 6.3 The proved depth is far above \(1/Q\)

Even granting the ideal residual inflation

\[
 \mathfrak T_z(u)\le {Cg\over mz^2},
 \tag{6.6}
\]

the existing calculation is summable at \(z=1/\log m\), but at the
coefficient-one stopping scale it gives

\[
 \mathfrak T_{1/Q}(u)
 \le {CgQ^2\over m}
 =m^{1/2+o(1)},
 \tag{6.7}
\]

not \(o(1)\).  Also

\[
 {T\over\log m}\gg {T\over Q}.
 \tag{6.8}
\]

Thus stopping where the current kernel is controlled leaves far too many
tags for the no-reserve ledger.  A chain-aligned completion theorem could
bridge this gap; none is presently supplied by the pair-square estimate.

## 7. The exact one-column theorem still needed

The complete edge-color target can now be replaced by the following
strictly weaker statement.

### Geodesic two-ledger matching theorem

There is a probability law on sequentially quarantined legal geodesic
matchings \(\mathbf M\) such that

\[
 \boxed{
 \mathbb E(T_g-|\mathbf M|)=o(T/Q),}
 \tag{7.1}
\]

and

\[
 \boxed{
 \mathbb E\sum_{e\in\mathbf M}
 |C(e)\cap V_{\rm exc}|=o(W).}
 \tag{7.2}
\]

By Theorems 3.1 and 4.1, this theorem alone produces a deterministic
cyclic-interval near-design with \(o(W)\) holes.  It makes no demand for a
resolution of all path copies into colors.

A sufficient proof package is:

1. the correct common mean drift through residual tag density
   \(\eta=o(1/Q)\);
2. the weighted sequential transfer-energy bound (6.5), equivalently a
   hereditary form of (6.4), with total exceptional fibre ledger \(o(W)\);
3. expected exceptional-target cost (7.2); and
4. dynamic quarantine cost \(o(W)\).

The raw pair-square formula supplies the time-zero covariance input to
item 2 and rules out the natural undiluted projective plane.  It does not
prove the hereditary estimate or the required stopping depth.  That is the
sharp present obstruction to replacing full color resolution by one large
matching.

## 8. Whole Latin tube absorption and the owner leave

The two-update Latin transport can be incorporated after the matching, but
it does not manufacture the matching assumed in Theorem 4.1.  The exact
whole-tube statement is proved in
`MATH_ATTACK_WHOLE_LATIN_TUBE_MATCHING_AND_OMITTED_OWNER_LEDGER_20260725.md`.
For \(t\) selected four-carrier tubes its owner leave is exactly

\[
 W-4Mt;
\]

if all but \(r\) calibrated carrier tags are used, this is

\[
 (W-MN_H)+Mr.
\]

Latin cell switches preserve every coordinate marginal, so the omitted
owner family must additionally have degrees

\[
 d_a(\mathcal L)=W/2-\Gamma_a.
\]

A port-rooted rectangle matching then absorbs the complete owner defect
without changing any tube endpoint.  The missing global input is the
hereditary Hall theorem which assigns the required rectangles to distinct
port-stable cells.  Thus the tube construction closes chronology and the
exact leave ledger, but it does not bypass the geodesic one-matching theorem
or its hereditary transfer-energy gate.

Moreover, the current transported one-braid tube has only

\[
 O(W/Q+WQ/M)=o(W)
\]

owner-active cells: during a \(\Theta(Q)\)-cell collar sweep the moving
adjacent swap meets a middle-owner-sensitive cut only \(O(1)\) times.
Consequently its Latin signs can absorb only a defect with positive mass of
this order.  The \((1/16-o(1))W\) count is a flag-direction count over all
ranks, not a linear-capacity middle-owner absorber.  Any global theorem must
therefore construct the whole-tube prepacking already at absorption-scale
owner error before the rooted Hall assignment is invoked.
