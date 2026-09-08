# The \(L^1\) recast of the cross-profile and packet-union cuts: exact grouped Hall and a linear-hole counterexample

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

The authoritative constant-one objective is

\[
 \mathfrak H
 =\sum_{q\le H,\epsilon,T}(1-L_q^\epsilon(T))_+
 =\sum_{q\le H,\epsilon}
      \#\{T:L_q^\epsilon(T)=0\},
\tag{0.1}
\]

or equivalently the full linear repeat excess

\[
 \mathfrak X
 =\sum_{q,\epsilon}\left[
   \sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)_+\right],
\tag{0.2}
\]

up to the already negligible forced deficit
\(\sum_{q,\epsilon}(N_q-G)_+=o(W)\).

The two cuts in
MATH_THEOREM_OVERLAP_COMPRESSION_CROSS_PROFILE_AND_PACKET_UNION_CUT_20260726.md
have the following exact \(L^1\) status.

1. The mixed-profile \(1/2\)-cut is a statewise linear-hole and
   linear-repeat obstruction for every state supported on its fixed raw
   incidence graph.
2. The frozen-parent touched-axis cut is a statewise linear-hole
   obstruction in the allocation-labelled face graph for every
   within-parent \(Q_R\)-packetization.
3. Neither is presently a physical obstruction after arbitrary legal
   cross-parent \(Q_{R+1}\)-slab trades. A slab can replace a two-packet
   image by another two-packet image and can import \(2^{R+1}\) new
   targets at one signed depth. Repairing either linear cut requires a
   positive-density slab family, but the legal state space permits exactly
   that order of magnitude. The cuts therefore prove a dense-cross-parent
   toll, not impossibility.

The smallest exact \(L^1\) grouped theorem is a near-cover theorem for
whole all-depth option images. For owner-disjoint choice groups \(g\), let
\(I_{g,\omega}\) be the typed target support of one legal option. Then

\[
 \boxed{
 \min_{\omega_g}
   \left|\mathcal V\setminus\bigcup_g I_{g,\omega_g}\right|
 =
 \min_{x\in\prod_g\Delta(\Omega_g)}
   \sum_{v\in\mathcal V}\prod_g(1-p_g(v)),}
\tag{0.3}
\]

where

\[
                         p_g(v)=
 \sum_{\omega}x_{g,\omega}{\bf1}_{\{v\in I_{g,\omega}\}}.
\tag{0.4}
\]

Thus a product law with \(o(W)\) avoidance mass is necessary and
sufficient inside any fixed owner-disjoint grouped catalogue. It is an
exact \(L^1\) statement, not a covariance surrogate.

There is an exact obstruction to replacing (0.3) by ordinary grouped
Hall ranks. Two owner-disjoint groups on four targets have option images

\[
 \{1,2\},\{3,4\}
 \qquad\text{and}\qquad
 \{1,3\},\{2,4\}.
\tag{0.5}
\]

Every subset \(A\) satisfies the natural grouped Hall inequality

\[
                         |A|\le r_1(A)+r_2(A),
\tag{0.6}
\]

and the uniform fractional law gives every target mean load one.
Nevertheless every integral state has exactly one hole and one repeat.
Tensoring gives \(\mathfrak H=\mathfrak X=N/4\).

This counterexample is entirely cross-group: every option image is
injective, and there is no within-packet, common-order, component, or seam
defect. It is an abstract option-incidence model, not a claimed literal
subcatalogue of the diverse-order slab atlas. It proves that the physical
theorem must use either full avoidance/homing information or a genuine
exchange structure on feasible target bundles.

## 1. Exact missing/repeat ledger

Fix one typed colour \(c=(q,\epsilon)\), write \(N=N_q\), and let

\[
                         L(T)\in\mathbb Z_{\ge0},
 \qquad \sum_TL(T)=G.
\tag{1.1}
\]

Put

\[
 H(L)=\sum_T(1-L(T))_+,
 \qquad
 E(L)=\sum_T(L(T)-1)_+.
\tag{1.2}
\]

If \(U=\{T:L(T)>0\}\), then

\[
                         E(L)=G-|U|,
 \qquad
                         H(L)=N-|U|.
\]

Therefore

\[
 \boxed{H(L)=N-G+E(L)}
\tag{1.3}
\]

and, equivalently,

\[
 \boxed{
 H(L)=(N-G)_+
      +\bigl(E(L)-(G-N)_+\bigr).}
\tag{1.4}
\]

Every legal state has the same \(G\), so every legal exchange satisfies

\[
                         \Delta H=\Delta E.
\tag{1.5}
\]

The equality uses the complete linear overload mass. It is false for a
capped repeat statistic.

## 2. The mixed-profile cut in the \(L^1\) ledger

Recall the exact construction. Let \(K\ge2\),

\[
                         M=2(K-1),\qquad p=2K.
\tag{2.1}
\]

There are \(p\) target profiles

\[
 L_i=\{(i,a):1\le a\le M\}\mathbin{\dot\cup}\{z_i\}.
\tag{2.2}
\]

The ordinary vertex \((i,a)\) has the \(K\) common neighbors
\((a,1),\ldots,(a,K)\) in

\[
                         U=[M]\times[K],
 \qquad |U|=KM,
\tag{2.3}
\]

while the portal \(z_i\) has a private \(K\)-set \(V_i\).
Every raw subfamily inside one \(L_i\) expands exactly by \(K\), and the
full profile-constant weighted Hall inequality holds.

Let

\[
                         \mathcal A=
 \{(i,a):1\le i\le2K,\ 1\le a\le M\}.
\tag{2.4}
\]

Then

\[
                         |\mathcal A|=2KM,
 \qquad
                         |N(\mathcal A)|=KM.
\tag{2.5}
\]

### Proposition 2.1 (exact \(L^1\) deficit of the mixed-profile cut)

Every target-to-source assignment supported on this fixed incidence graph
leaves at least

\[
                         |\mathcal A|-|N(\mathcal A)|
                         =KM
\tag{2.6}
\]

vertices of \(\mathcal A\) uncovered. This is a \(1/2\)-fraction of
\(\mathcal A\) and a positive fraction of the whole target shore.

If occurrence mass is normalized to equal target mass, then every such
state also has at least \(KM\) repeat units. If a normalization with
\(G>N\) is desired, append state-independent occurrences on already
covered targets; both \(E\) and \(G-N\) increase by the same amount, so
the repeat excess \(E-(G-N)\) remains at least \(KM\).

#### Proof

At most one target can be assigned to each source in \(N(\mathcal A)\).
Thus at most \(KM\) of the \(2KM\) targets in \(\mathcal A\) are covered,
proving (2.6). The repeat statements follow from (1.4). \(\square\)

### Why legal slabs remove the conclusion

Proposition 2.1 is statewise only while the target--source incidence graph
is fixed. A cross-parent slab trade changes two whole packet images and
therefore adds target incidences not represented in (2.2)--(2.3). The
abstract common reservoir \(U\) is not known to be invariant under those
trades.

For one signed depth, write \(s=2^R\). One slab option has target image
of size \(2s\). Against a background load \(B_t\), replacing option
\(a_0\) by \(a\) changes the hole count by

\[
 H(B_t+\Gamma_{t,a})-H(B_t+\Gamma_{t,a_0})
 =|Z_t\cap I_{t,a_0}|-|Z_t\cap I_{t,a}|,
\tag{2.7}
\]

where \(Z_t=\{T:B_t(T)=0\}\). Consequently one slab can reduce the
hole count by at most \(2s\).

Thus repairing a deficit \(D\) at one signed depth requires at least

\[
                         {D\over2s}
\tag{2.8}
\]

cross-cut slab changes. For \(D=\Theta(W)\), this is
\(\Omega(W/2^R)\) slabs, a positive fraction of the available
owner-disjoint slab scale. The legal state permits that scale.
Equation (2.8) is therefore a dense-slab toll, not a contradiction.

## 3. The frozen-parent touched-axis cut in the \(L^1\) ledger

Inside one frozen owner cell \(Q_S\), the earlier probabilistic
construction gives a set \(X_0\), \(|X_0|=(1-o(1))2^S\), and injective
signed cell-face targets \(F^\epsilon(x,D_x)\) such that every
within-cell coordinate \(Q_R\)-packetization satisfies

\[
 \#\{x\in X_0:D_x\subseteq R(P_x)\}
 \le2\alpha2^S,
 \qquad
 \alpha={\binom Rq\over\binom Sq}=o(1).
\tag{3.1}
\]

### Proposition 3.1 (exact frozen-parent \(L^1\) deficit)

In the allocation-labelled selected-axis graph of the frozen parent,
every within-parent \(Q_R\)-packetization leaves at least

\[
                         (1-o(1)-2\alpha)2^S
                         =(1-o(1))2^S
\tag{3.2}
\]

of those face targets uncovered.

#### Proof

A labelled face \(F(x,D_x)\) has a selected neighbor exactly when
\(D_x\subseteq R(P_x)\). If one face vertex \(y\) belongs to a packet
whose support contains \(D_x\), that coordinate packet contains the whole
face and hence \(x\); it is therefore \(P_x\). Equation (3.1) bounds all
covered faces. \(\square\)

### Why cross-parent slabs remove the conclusion

A legal \(Q_{R+1}\)-slab trade creates final packets crossing the original
parent boundary. Such packets are not parts of a \(Q_R\)-tiling of the
frozen \(Q_S\) in Proposition 3.1. Moreover the physical target problem
forgets the allocation/cell label, so the same literal target may be
rerouted through a different middle extension.

Even if the labels were retained, filling the
\(\Theta(2^S)\) holes of (3.2) needs only
\(\Omega(2^{S-R})\) slabs by (2.8), which is the natural number of
owner-disjoint \(Q_{R+1}\)'s at that scale. Hence the counting cut is
again compatible with a positive-density cross-parent recoupling.

No invariant presently shows that all legal slab states preserve the
mixed-profile reservoir \(U\) or the frozen-parent face labels.
Accordingly neither earlier cut proves a statewise \(\Omega(W)\)
physical hole lower bound in the enlarged legal state space.

## 4. Exact cross-parent grouped \(L^1\) theorem

Let

\[
 \mathcal V
 =\mathop{\dot\bigcup}_{q\le H,\epsilon}
     \mathcal T_q^\epsilon
\tag{4.1}
\]

be the typed all-depth target universe. Choose an owner-disjoint
collection of compound choice groups \(\mathcal G\). A group may be one
untraded packet, one \(Q_{R+1}\)-slab, or a larger owner-disjoint compound
whose legal internal choices are coupled. Its option set is
\(\Omega_g\). One option \(\omega\in\Omega_g\) has the whole typed support

\[
                         I_{g,\omega}\subseteq\mathcal V.
\tag{4.2}
\]

All signed depths occur in the same option; no depthwise splitting is
allowed.

For a deterministic state \(\boldsymbol\omega=(\omega_g)_g\), put

\[
 H(\boldsymbol\omega)
 =\left|\mathcal V\setminus
       \bigcup_{g\in\mathcal G}I_{g,\omega_g}\right|.
\tag{4.3}
\]

For product distributions \(x_g\in\Delta(\Omega_g)\), put

\[
 p_g(v)=\sum_{\omega\in\Omega_g}
            x_{g,\omega}{\bf1}_{\{v\in I_{g,\omega}\}},
\tag{4.4}
\]

and

\[
                         \Psi(x)
 =\sum_{v\in\mathcal V}\prod_{g\in\mathcal G}(1-p_g(v)).
\tag{4.5}
\]

### Theorem 4.1 (exact grouped avoidance theorem)

\[
 \boxed{
 \min_{\boldsymbol\omega}H(\boldsymbol\omega)
 =\min_{x\in\prod_g\Delta(\Omega_g)}\Psi(x).}
\tag{4.6}
\]

Moreover this common value equals

\[
 |\mathcal V|-
 \max\left\{
   \sum_g|B_g|:
   B_g\subseteq I_{g,\omega_g}\text{ for some }\omega_g,\ 
   B_g\cap B_h=\varnothing\ (g\ne h)
 \right\}.
\tag{4.7}
\]

#### Proof

Sample the group options independently according to \(x\). A typed target
\(v\) is missed exactly when every group misses it, an event of
probability \(\prod_g(1-p_g(v))\). Therefore

\[
                         \Psi(x)=
 \mathbb E_xH(\boldsymbol\omega).
\tag{4.8}
\]

Some deterministic state in the support has cost at most this
expectation. Conversely every deterministic state is a product
distribution of delta masses. Taking minima proves (4.6).

For a deterministic state, assign every covered target to one selected
group which covers it. The assigned bundles are disjoint and satisfy the
condition in (4.7), with total size equal to the union. Conversely any
bundles in (4.7) are covered by the witnessing group options. This proves
(4.7). \(\square\)

### Corollary 4.2 (minimal sufficient cross-parent grouped Hall theorem)

It suffices to construct:

1. an owner-disjoint legal compound-group decomposition;
2. one common all-depth option catalogue \(\Omega_g\) per group; and
3. product distributions \(x_g\) for which

\[
                         \Psi(x)=o(W).
\tag{4.9}
\]

Conditional expectation then chooses one integral all-depth legal state
with \(\mathfrak H=o(W)\), and (1.4) gives
\(\mathfrak X=o(W)\).

The theorem is exact for the chosen grouped catalogue. If slab-packing
choices overlap, they must first be placed in one larger choice group or
resolved by a legal owner-disjoint slab packing. Treating incompatible
slabs as independent groups is invalid. The same warning applies to a
rank matching, selector, or frame variable shared by several groups: it
must be frozen before product sampling or absorbed into their common
master group. Owner disjointness alone does not make shared-frame choices
independent.

### Correlated form

For an arbitrary joint distribution \(\mu\) on complete legal states, the
minimal condition is simply

\[
 \boxed{
 \sum_{v\in\mathcal V}
   \Pr_\mu\{v\text{ is uncovered}\}=o(W).}
\tag{4.10}
\]

An averaging argument then selects one state of at most that cost. Formula
(4.5) is the factorized special case of (4.10); a correlated slab
construction may be strictly stronger.

## 5. A natural grouped Hall inequality is not sufficient

For one group define its bundle rank

\[
 r_g(A)=\max_{\omega\in\Omega_g}|A\cap I_{g,\omega}|.
\tag{5.1}
\]

If all of \(A\) can be assigned to legal group bundles, necessarily

\[
                         |A|\le\sum_gr_g(A).
\tag{5.2}
\]

This is the direct grouped analogue of the ordinary Hall cut. It is not
sufficient.

### Theorem 5.1 (alternating two-group linear-hole obstruction)

Let \(\mathcal V=\{1,2,3,4\}\). Give group \(1\) the two options

\[
                         I_{1,0}=\{1,2\},\qquad
                         I_{1,1}=\{3,4\},
\tag{5.3}
\]

and group \(2\) the two options

\[
                         I_{2,0}=\{1,3\},\qquad
                         I_{2,1}=\{2,4\}.
\tag{5.4}
\]

Then:

1. (5.2) holds for every \(A\subseteq\mathcal V\);
2. there is a fractional option law under which every target has mean
   load one;
3. every integral state has exactly one missing target and one repeat
   unit; and
4. every product distribution has expected hole count exactly one.

Tensoring \(n\) disjoint copies gives

\[
                         \mathfrak H=\mathfrak X=n
                         ={|\mathcal V|\over4}
\tag{5.5}
\]

for every integral state, while all grouped rank inequalities and exact
mean-one marginals continue to hold.

#### Proof

View the four targets as a \(2\times2\) array. The options of group \(1\)
are its rows and the options of group \(2\) are its columns. For every
\(A\),

\[
 r_1(A)\ge\left\lceil{|A|\over2}\right\rceil,
 \qquad
 r_2(A)\ge\left\lceil{|A|\over2}\right\rceil,
\]

so (5.2) holds.

Choose each option with probability \(1/2\). Every target lies in one
option of each group, so it has coverage probability \(1/2\) from each
group and mean load one.

Every selected row meets every selected column in exactly one target.
Their union therefore has size three. Since the total occurrence mass is
four, the load vector has one zero, one two, and two ones. Thus
\(H=E=1\).

For arbitrary option probabilities \(x\) and \(y\), the four miss
probabilities are

\[
 (1-x)(1-y),\qquad
 (1-x)y,\qquad
 x(1-y),\qquad
 xy.
\tag{5.6}
\]

Their sum is identically one. Independent tensor copies add their costs
and preserve (5.2) copy by copy. \(\square\)

### Interpretation

Theorem 5.1 is not a within-packet obstruction. Each option is an
injective whole image, and the unique collision in every state lies
between the two owner-disjoint groups. Other signed depths may be
decorated with state-independent private targets, so the same option
choice is common all-depth and the obstruction remains at the displayed
colour.

The theorem is an abstract grouped-incidence counterexample. To make it a
physical constant-one no-go one would have to exhibit these four
intersection identities inside every legal diverse-order/slab
resolution, which is not known and is unlikely to follow from direction
marginals alone. Its role is exact: first moments and the natural rank
cuts do not prove (4.9).

This is complementary to the \(Q_3\) slab trap in
MATH_THEOREM_L1_MISSING_HINGE_COMPOUND_SLAB_EXCHANGE_20260726.md.
The present two-group example proves that even all grouped rank cuts can
hold while every state has linear holes. The \(Q_3\) example proves a
different fact: one-slab descent can be trapped even when a correlated
four-slab exchange reaches zero holes. Together they exclude both a
plain Hall-rank proof and a local-descent proof from the currently
audited slab axioms.

## 6. When a true grouped Hall theorem exists

For group \(g\), let

\[
 \mathcal F_g
 =\{B:B\subseteq I_{g,\omega}
          \text{ for some }\omega\in\Omega_g\}.
\tag{6.1}
\]

This is a hereditary family. Suppose, additionally, that every
\(\mathcal F_g\) is the independent-set family of a matroid \(M_g\) on
\(\mathcal V\), with rank \(r_g\).

### Theorem 6.1 (matroidal grouped Hall)

The maximum number of typed targets coverable by disjoint feasible
bundles is

\[
 \boxed{
 C_{\max}
 =\min_{A\subseteq\mathcal V}
     \left(|\mathcal V\setminus A|+\sum_gr_g(A)\right).}
\tag{6.2}
\]

Consequently the minimum hole count is

\[
 \boxed{
 H_{\min}
 =\max_{A\subseteq\mathcal V}
     \left(|A|-\sum_gr_g(A)\right).}
\tag{6.3}
\]

In particular, the grouped Hall inequalities (5.2) are sufficient when
the bundle systems are matroids.

#### Proof

Let \(B_g\in\mathcal F_g\) be pairwise disjoint and put
\(B=\dot\bigcup_gB_g\). For every \(A\subseteq\mathcal V\),

\[
 |B|
 =|B\setminus A|+\sum_g|B_g\cap A|
 \le|\mathcal V\setminus A|+\sum_gr_g(A).
\tag{6.4}
\]

This proves the upper bound in (6.2).

Choose a decomposition \(B=\dot\bigcup_gB_g\) of maximum size. Build the
exchange digraph on \(\mathcal V\): every unassigned element is a source;
and for \(x\notin B_g\), put an arc \(x\to y\), \(y\in B_g\), whenever

\[
                         B_g-y+x\in\mathcal F_g.
\tag{6.5}
\]

Call \(x\) terminal for \(g\) if \(B_g+x\in\mathcal F_g\). An alternating
source-to-terminal path augments \(B\) by one: along the path, insert the
previous element into the group of the next element, freeing the next,
and finally insert the terminal. The circuit-elimination property of
matroids permits a shortest such path to be performed without destroying
the earlier exchanges. Maximality of \(B\) therefore implies that no such
path exists.

Let \(A\) be the set reachable from the unassigned sources. For every
\(g\), no element of \(A\) is terminal for \(g\). If
\(x\in A\setminus B_g\), its fundamental circuit with respect to \(B_g\)
is contained in

\[
                         (B_g\cap A)\cup\{x\};
\]

otherwise (6.5) would reach a circuit element outside \(A\). Hence
\(B_g\cap A\) spans \(A\) in \(M_g\), and

\[
                         r_g(A)=|B_g\cap A|.
\tag{6.6}
\]

Every unassigned element lies in \(A\), so

\[
 |\mathcal V\setminus A|=|B\setminus A|.
\tag{6.7}
\]

Equations (6.6)--(6.7) give

\[
 |\mathcal V\setminus A|+\sum_gr_g(A)
 =|B\setminus A|+\sum_g|B_g\cap A|
 =|B|.
\]

This proves equality in (6.2); (6.3) follows by subtracting from
\(|\mathcal V|\). \(\square\)

### Why the actual option families need a new theorem

For whole-option images, \(\mathcal F_g\) is a union of power sets of
different images. It need not satisfy matroid exchange. In Theorem 5.1,
the group-\(1\) family contains \(\{1,2\}\) and \(\{3,4\}\), but no
two-set mixing one element from each row. Its maximal feasible bundles
therefore violate basis exchange. The same is true for group \(2\).

Thus Theorem 6.1 does not currently apply to the physical compiler
catalogue. A positive route must prove one of:

1. an asymptotic matroidal or polymatroidal closure after allowing
   compound cross-parent slab exchanges;
2. a direct avoidance/homing construction satisfying (4.9);
3. a correlated legal law satisfying (4.10); or
4. a geometric exclusion of positive-density alternating minors such as
   (5.3)--(5.4).

## 7. A useful homing sufficient condition

The exact product objective admits a simple one-sided sufficient
condition. For every typed target \(v\),

\[
 \prod_g(1-p_g(v))
 \le1-\max_gp_g(v).
\tag{7.1}
\]

Therefore:

### Corollary 7.1 (aggregate home-group theorem)

If one legal owner-disjoint grouped catalogue has product distributions
with

\[
 \boxed{
 \sum_{v\in\mathcal V}
       \left(1-\max_gp_g(v)\right)=o(W),}
\tag{7.2}
\]

then it has one integral common all-depth state satisfying

\[
                         \mathfrak H=\mathfrak X=o(W).
\tag{7.3}
\]

Condition (7.2) is stronger than the exact avoidance condition (4.9), but
it is linear in the targetwise home defects. At a fixed Gaussian depth,
if the total mean load
\(\sum_gp_g(v)\) has a uniform constant upper bound outside \(o(W)\)
targets, a successful product law must in fact have
\(\max_gp_g(v)=1-o(1)\) outside \(o(W)\) targets. Thus (7.2) describes
the required polarization scale.

## 8. Certified boundary

Proved:

1. both earlier counter-cuts are linear \(L^1\) obstructions in their
   fixed incidence spaces;
2. neither is invariant under the full legal cross-parent slab state
   space;
3. repairing a linear one-colour cut requires
   \(\Omega(W/2^R)\) slab changes, which is dense but legally possible;
4. (4.6)--(4.7) give the exact grouped \(L^1\) near-cover theorem;
5. the natural grouped rank Hall inequalities and exact mean-one
   marginals do not suffice, by the tensorable two-group obstruction;
6. matroidal bundle exchange would make grouped Hall exact; and
7. aggregate homing (7.2) is a direct sufficient theorem.

Not proved:

1. that the literal diverse-order/slab option families contain the
   alternating obstruction of Theorem 5.1;
2. that they admit matroidal closure or satisfy aggregate homing;
3. a legal correlated avoidance law with \(o(W)\) cost; or
4. the constant-one theorem.

The exact weaker residual is not covariance. It is a common all-depth
cross-parent grouped near-cover problem. The cuts show why fixed raw Hall
and post-hoc packetization fail; Theorem 5.1 shows why even grouped rank
Hall can fail; and (4.9), (4.10), or the stronger homing condition (7.2)
is the minimal positive target.

## 9. \(H\)-memory endpoint successor

MATH_THEOREM_H_MEMORY_COMPLEMENT_GROUPED_HALL_AND_SLAB_CUT_TEST_20260726.md
adds the chronology rows. It proves that a grouped path selection is a
state-valid owner successor exactly when its total
\((H-1)\)-memory endpoint boundary vanishes, and that complement-paired
options give exact lower/upper target symmetry.

For an endpoint-separated connector catalogue, closure is exactly a
perfect matching on complement orbits; Hall and alternating paths are
therefore exact. For general slab groups, a legal augmentation must be a
union of whole group differences with zero memory boundary. Its \(L^1\)
gain is the new-minus-old union on the common background-zero set.

The successor also tests the mixed-profile \(1/2\)-cut. Slab switches are
zero-boundary memory circuits, so the static cut is not invariant.
However, local Hamming-two reachability and endpoint Hall do not imply
literal target escape; a paired abstract countermodel has identical
endpoint/option data with respectively \(1/2\) holes and zero holes.
