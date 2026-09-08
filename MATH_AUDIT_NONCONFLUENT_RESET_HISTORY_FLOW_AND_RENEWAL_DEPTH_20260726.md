# Nonconfluent reset histories: the exact configuration flow and a renewal-depth obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Decision

Put

\[
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},\qquad
 M=m+H,
\tag{0.1}
\]

and work at

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 L=m-3H+1,
\tag{0.2}
\]

with

\[
 {LN_H\over W}=1-o(1).
\tag{0.3}
\]

The deletion-robust nonmechanical common-core atlas supplies a dense
state alphabet, literal parent arcs, and a whole-state fractional
capacity point. This note determines what renewal can and cannot add.

There are three conclusions.

1. The exact nonconfluent object is not an ordinary circulation after
   physical tops with different histories are identified. It is a
   configuration LP whose columns are complete integral schedules on
   unfolded history components. An integral column choice gives one
   state per physical top. Merging histories inside a usual network
   either chooses several states for one top or enforces restriction
   confluence.
2. The target rows destroy network integrality even before asymptotics.
   Three literal common-core paths contain a physical middle-rank
   incidence minor of determinant two. Thus no total-unimodularity or
   bare circulation argument can round the fractional atlas.
3. More decisively, renewal every \(D=O(H)\) levels cannot work if
   different renewal components are rounded independently, even when
   arbitrary dependence is allowed inside each component. A component
   has at most \(4^D\) physical roots, whereas a marginal-preserving
   product rounding with vanishing middle defect requires coupling at
   least

   \[
      (1-o(1)){\binom MH\over L}
   \tag{0.4}
   \]

   roots. For \(D=O(H)\), the expected middle holes and repeat excess
   are both at least

   \[
      (e^{-1}-o(1))W.
   \tag{0.5}
   \]

The necessary renewal depth for a bounded-branching independent
architecture is

\[
 \boxed{
 D\ge {1-o(1)\over\log4}\log{\binom MH\over L}
   =\left({1\over2\log2}+o(1)\right)H\log{m\over H}.}
\tag{0.6}
\]

This is \(\Theta(H\log m)\), not \(\Theta(H)\).

Therefore the proposed \(\Theta(H)\)-renewal recursion does not yield an
integral coefficient-one selection through local or product rounding.
The only surviving version must correlate at least
\(\binom MH/L=\exp(\Theta(H\log(m/H)))\) roots across many renewal
components. Such a global configuration rounding is precisely the
unresolved one-state-per-top promotion-path packing problem; renewal has
not reduced it to network flow.

## 1. The unfolded history object

Consider a band of \(D\) standard Boolean suspensions. At step \(j\),
adjoin a new coordinate pair

\[
 E_j=\{a_j,b_j\}.
\tag{1.1}
\]

Let \(V_0\) be the coordinate set at the bottom of the band and

\[
 V_j=V_0\mathbin{\dot\cup}E_1\mathbin{\dot\cup}\cdots
          \mathbin{\dot\cup}E_j.
\tag{1.2}
\]

A history remembers, at every step, which coordinates of \(E_j\) lie
in the current top, which parent deletion is used, the current ordered
common-core state, and whether the edge is inherited or is a reset.
The state transition is literal deletion of the prescribed labels. For
the front-tail inherited arc, every old signed trace obeys

\[
 T^+_{j+1,\ell}=T_{j,\ell}\cup\{x\}.
\tag{1.3}
\]

The safety index decreases by at most one per inserted or deleted
coordinate.

If histories are unfolded, the local marginal variables have the usual
form

\[
 z_{h,\pi}\ge0,\qquad
 f_{h,\pi;h',\pi'}\ge0,
\tag{1.4}
\]

where \(h'\) extends \(h\) by one step and \(\pi'\) deletes to \(\pi\).
On a history tree the equations

\[
 \sum_{\pi'}f_{h,\pi;h',\pi'}=z_{h,\pi},
 \qquad
 \sum_{\pi}f_{h,\pi;h',\pi'}=z_{h',\pi'}
\tag{1.5}
\]

are an exact local marginal description. The tree can be sampled from
root to leaves, so its local polytope is integral in the sense that its
points are convex combinations of complete state assignments to the
unfolded occurrences.

This is not yet one state per *physical* top. The same top \(U\) may be
reached by different histories \(h_1,h_2\). There are only two direct
identifications.

- Keep \((h_1,U)\) and \((h_2,U)\) distinct. Then the history flow may
  assign different states to them, so it has selected more than one
  state for the physical top.
- Identify their state variables. Then every deletion diamond has the
  same induced order at its common endpoint. Iterating the diamonds is
  restriction confluence, which collapses the orders to hereditary
  ambient-order profiles.

A nonconfluent one-state-per-top construction must instead choose one
incoming history for every physical top and discard the other
occurrences. That is a branching-arborescence/configuration decision,
not the conservation law (1.5).

## 2. Exact component-configuration LP

Renew the history at both ends of the band. For an old projection
\(B\subseteq V_0\), let \(\mathcal C_B\) be the collection of physical
tops in the band whose intersection with \(V_0\) is \(B\). Let
\(\Sigma_B\) be the finite set of all legal integral schedules on
\(\mathcal C_B\). A schedule chooses

1. one ordered common-core state for every physical top in
   \(\mathcal C_B\);
2. one incoming parent history whenever that top is inherited;
3. literal deletion-compatible state arcs inside the band; and
4. one nested tag profile on every selected promotion path.

For a target \(Y\) at signed depth \(q\), let

\[
 a_{q,Y}^{\pm}(\sigma)
\tag{2.1}
\]

be its number of occurrences in schedule \(\sigma\). The exact grouped
fractional problem is

\[
 \sum_{\sigma\in\Sigma_B}x_{B,\sigma}=1
 \qquad(B),
\tag{2.2}
\]

\[
 \sum_B\sum_{\sigma\in\Sigma_B}
 a_{q,Y}^{\pm}(\sigma)x_{B,\sigma}\le1
 \qquad(q,Y,\pm),
\tag{2.3}
\]

\[
 x_{B,\sigma}\ge0.
\tag{2.4}
\]

An integral solution chooses one whole schedule in every component and
therefore one state per physical top. This is the precise circulation
replacement. The internal history flow may be used to enumerate or
optimize the columns \(\Sigma_B\), but the global target rows act on
whole schedules.

The reset atlas supplies the local state support and a fractional
whole-state capacity point. It does not assert integrality of
(2.2)--(2.4).

## 3. A literal determinant-two target minor

The failure of ordinary network integrality is physical, not merely a
formal warning.

### Theorem 3.1 (middle-rank triangle minor)

For all sufficiently large \(m\), the literal common-core path catalogue
contains three paths \(P_1,P_2,P_3\) and three distinct middle targets
\(Y_{12},Y_{23},Y_{13}\) whose incidence matrix is

\[
 \begin{array}{c|ccc}
       &P_1&P_2&P_3\\ \hline
 Y_{12}&1&1&0\\
 Y_{23}&0&1&1\\
 Y_{13}&1&0&1
 \end{array}.
\tag{3.1}
\]

Its determinant is \(2\). The three paths may all be chosen from the
deletion-robust nonmechanical reset atlas.

#### Proof

Choose disjoint sets

\[
 |K|=m-H+1,\qquad
 |A_{12}|=|A_{13}|=|A_{23}|=H-1,
\tag{3.2}
\]

and three further labels \(p_1,p_2,p_3\). There is room because their
union has size \(m+2H+1<2m\). Put

\[
 \begin{aligned}
 U_1&=K\mathbin{\dot\cup}A_{12}\mathbin{\dot\cup}A_{13}
          \mathbin{\dot\cup}\{p_1\},\\
 U_2&=K\mathbin{\dot\cup}A_{12}\mathbin{\dot\cup}A_{23}
          \mathbin{\dot\cup}\{p_2\},\\
 U_3&=K\mathbin{\dot\cup}A_{13}\mathbin{\dot\cup}A_{23}
          \mathbin{\dot\cup}\{p_3\}.
 \end{aligned}
\tag{3.3}
\]

Every \(U_i\) has size \(M\). Their pairwise intersections

\[
 Y_{12}=K\cup A_{12},\qquad
 Y_{23}=K\cup A_{23},\qquad
 Y_{13}=K\cup A_{13}
\tag{3.4}
\]

are distinct middle targets.

Choose each \(2H\)-core inside \(K\). In the tail of \(U_1\), place
the \(2H-1\) labels

\[
 A_{13},\ p_1,\ A_{12}
\tag{3.5}
\]

consecutively, beginning at tail position \(H+1\). The first and last
length-\(H\) windows of this displayed segment are respectively

\[
 A_{13}\cup\{p_1\}=U_1\setminus Y_{12},
 \qquad
 A_{12}\cup\{p_1\}=U_1\setminus Y_{13}.
\tag{3.6}
\]

They occur at retained phases \(1\) and \(H\). Thus \(P_1\) contains
\(Y_{12}\) and \(Y_{13}\). Use the analogous tail segments

\[
 A_{23},p_2,A_{12}
 \quad\hbox{and}\quad
 A_{23},p_3,A_{13}
\tag{3.7}
\]

for \(U_2\) and \(U_3\). This gives exactly (3.1); the missing target
in each column is not even contained in that column's top.

The constraints (3.5)--(3.7), the cores, and the two prescribed windows
fix only \(O(H)\) labels or positions. Their conditioning cost is
\(\exp(O(H\log m))=\exp(o(m))\). The edit-ball pruning theorem removes
only \(e^{-\Omega(m)}\) of a central type class, so choose the labels
with central \(P/P^c\)-types and complete all three orders inside the
nonmechanical reset alphabet. \(\square\)

### Corollary 3.2

The whole-path target-incidence matrix is not totally unimodular. In
particular, every direct history-flow formulation which retains one
state/path selection variable per column and appends the target rows
contains this minor. Network-flow integrality of the internal chronology
rows cannot round that target-capacity formulation. No claim is made
that every possible higher-dimensional extended formulation must display
the same minor.

The determinant-two minor is not by itself a positive-density packing
obstruction: the full catalogue contains many alternative columns. It
does prove that an integral theorem needs a genuine global rounding
argument rather than a circulation-integrality slogan.

## 4. Size of a renewal component

### Lemma 4.1 (branching bound)

For a fixed old projection \(B\subseteq V_0\), the number of distinct
physical top sets at the upper end of a \(D\)-step band is at most

\[
 |\mathcal C_B|\le2^{2D}=4^D.
\tag{4.1}
\]

The same bound holds after carrying any fixed number of adjacent top-size
types.

#### Proof

Every upper top with old projection \(B\) is determined by its
intersection with the \(2D\) new coordinates
\(E_1\dot\cup\cdots\dot\cup E_D\). There are at most \(2^{2D}\)
such intersections. Restricting to prescribed top sizes only decreases
the count. Extra type labels do not create new physical top sets.
\(\square\)

Across all intermediate layers the corresponding bound is
\(1+4+\cdots+4^D<4^{D+1}/3\). In the renewal estimate below, \(b\)
counts only critical roots at the upper endpoint, so (4.1) is the
relevant bound.

Multiple deletion histories leading to the same top enlarge the state
catalogue but not the number of roots which can be jointly coordinated
inside one old-projection component. This distinction is essential in
the target-capacity estimate.

## 5. The independent-renewal repeat floor

For a middle target \(X\), the compatible critical tops are

\[
 U=X\mathbin{\dot\cup}J,\qquad J\in\binom{X^c}{H},
\tag{5.1}
\]

so their number is

\[
 R_H=\binom mH.
\tag{5.2}
\]

Under a uniform common-core ordered state, a fixed root selects \(X\)
in its \(L\) retained middle phases with probability

\[
 \varpi_H={L\over\binom MH}.
\tag{5.3}
\]

The deletion-robust pruning changes this by only a factor
\(1+e^{-\Omega(m)}\). Also

\[
 R_H\varpi_H={LN_H\over W}=1-o(1).
\tag{5.4}
\]

For the balanced half used by the reset alphabet, define

\[
 \mathcal X_{\rm cen}
 =\left\{X\in\binom{[2m]}m:
 \left||X\cap P|-{m\over2}\right|\le {m\over20}\right\}.
\tag{5.4a}
\]

Stirling's formula gives
\(|\mathcal X_{\rm cen}|=W-e^{-\Omega(m)}W\). Every critical top
containing a member of \(\mathcal X_{\rm cen}\) has \(P\)-type in
\([2M/5,3M/5]\) for all sufficiently large \(m\). Thus the pruning
estimate and (5.4) hold uniformly on this \(W-o(W)\) target set. The
exponentially small complement will be discarded in the lower bound.

### Theorem 5.1 (product renewal no-go)

Partition the critical roots into renewal components of size at most
\(b\). Inside one component allow an arbitrary joint distribution of
whole legal history schedules. Assume distinct components are
independent and every root has the uniform, or deletion-robust
\(e^{-\Omega(m)}\)-perturbed, common-core marginal. If

\[
 b\varpi_H\le\alpha<1,
\tag{5.5}
\]

then the expected number \(Z\) of missing middle targets satisfies

\[
 \boxed{
 \mathbb EZ\ge
 W\exp\left(-{1+o(1)\over1-\alpha}\right).}
\tag{5.6}
\]

The expected middle repeat excess satisfies

\[
 \boxed{
 \mathbb E E_0\ge
 W\exp\left(-{1+o(1)\over1-\alpha}\right)-o(W).}
\tag{5.7}
\]

#### Proof

Fix \(X\in\mathcal X_{\rm cen}\). In renewal component \(C\), let
\(Y_C\) be the number of
its roots whose selected paths contain \(X\), and put
\(\mu_C=\mathbb EY_C\). Markov's inequality gives

\[
 \Pr(Y_C=0)\ge1-\mu_C.
\tag{5.8}
\]

The marginal hypothesis gives

\[
 0\le\mu_C\le b\varpi_H(1+o(1))\le\alpha+o(1),
 \qquad
 \sum_C\mu_C=1-o(1).
\tag{5.9}
\]

Independence of the components and

\[
 \log(1-x)\ge-{x\over1-\alpha-o(1)}
 \qquad(0\le x\le\alpha+o(1))
\tag{5.10}
\]

give

\[
 \Pr(X\hbox{ is missed})
 \ge\prod_C(1-\mu_C)
 \ge\exp\left(-{1+o(1)\over1-\alpha}\right).
\tag{5.11}
\]

Sum over \(\mathcal X_{\rm cen}\), whose size is \(W-o(W)\), to obtain
(5.6).

Every selection has exactly

\[
 T=LN_H=W-o(W)
\tag{5.12}
\]

middle occurrences, up to the exponentially small quarantined root
shore. If \(Z\) is its number of holes and \(E_0\) its repeat excess,
then the exact occurrence identity is

\[
 T=(W-Z)+E_0,
 \qquad E_0=Z-(W-T).
\tag{5.13}
\]

Take expectations and use \(W-T=o(W)\) to prove (5.7). \(\square\)

### Corollary 5.2 (\(\Theta(H)\) renewal fails)

For old-projection renewal bands of depth \(D=O(H)\), Lemma 4.1 gives

\[
 b\varpi_H\le4^D{L\over\binom MH}=o(1).
\tag{5.14}
\]

Consequently

\[
 \mathbb EZ\ge(e^{-1}-o(1))W,
 \qquad
 \mathbb EE_0\ge(e^{-1}-o(1))W.
\tag{5.15}
\]

No such product-renewal law can be supported on selections with
\(o(W)\) middle repeat excess.

#### Proof

Stirling's formula gives

\[
 \log{1\over\varpi_H}
 =\log\binom MH-\log L
 =H\log{M\over H}+H+O\left({H^2\over M}+\log H\right)-\log L
\tag{5.16}
\]

and hence

\[
 \log{1\over\varpi_H}
 =(1+o(1))H\log{m\over H}.
\tag{5.17}
\]

For \(D=O(H)\), \(D\log4=O(H)=o(H\log(m/H))\), proving (5.14).
Apply Theorem 5.1 with \(\alpha=o(1)\). \(\square\)

### Corollary 5.3 (minimum independent renewal depth)

Vanishing holes under a bounded-branching product-renewal law requires

\[
 4^D\ge(1-o(1)){1\over\varpi_H}
 =(1-o(1)){\binom MH\over L}.
\tag{5.18}
\]

Equivalently,

\[
 D\ge\left({1\over2\log2}+o(1)\right)
       H\log{m\over H}.
\tag{5.19}
\]

At the calibrated height this is

\[
 D\ge\left({1\over4\log2}+o(1)\right)
       \sqrt m\,(\log m)^{3/2}.
\tag{5.20}
\]

Thus the required depth is larger than \(H\) by a factor
\(\Theta(\log m)\).

## 6. Exact scope of the obstruction

Theorem 5.1 allows arbitrary chronology, arbitrary state correlations,
and arbitrary nonmechanical reset choices *inside* one renewal
component. It does not assume that roots inside a component are
independent. The obstruction uses only:

1. the root marginal \(\varpi_H(1+o(1))\);
2. the bound on the number of roots per component; and
3. independence between different renewal components.

The independence hypothesis cannot be silently dropped. A deterministic
global design, or a randomized law with one shared seed, may correlate
many renewal components so that their target sets complement one another.
Likewise a global solution of (2.2)--(2.4) couples all components through
the target rows. The present theorem does not refute such a globally
coupled solution.

It does prove that renewal every \(\Theta(H)\) levels supplies
insufficient *local coupling volume*. To escape, one must do at least one
of the following.

1. Keep histories alive for depth
   \(\Omega(H\log(m/H))\).
2. Group at least \((1-o(1))\binom MH/L\) old projections into one
   renewal component.
3. Retain \(\Theta(H)\) bands but solve one global, nonproduct
   configuration rounding across that many components.

Option 3 is exactly the original integral common-history packing gate.
The reset recursion provides its columns and removes the mechanical
support cut, but does not furnish its rounding theorem.

## 7. Final theorem-grade conclusion

### Theorem 7.1 (nonconfluent renewal decision)

The deletion-robust reset atlas admits an exact unfolded history-flow
formulation and an exact grouped configuration LP. Internal history
flows are integral before physical-top identification and target rows,
but the physical whole-path target matrix contains a determinant-two
middle-rank minor.

For renewal bands of depth \(D=O(H)\), every old-projection component
contains at most \(4^D\) roots. Any rounding law which is independent
between those components, even with arbitrary joint schedules inside
each component, has

\[
 \mathbb E E_0\ge(e^{-1}-o(1))W.
\]

Hence \(\Theta(H)\)-level local renewal cannot produce a one-state-per-top
selection with \(o(W)\) repeat excess. Independent renewal needs depth
at least (5.19). A globally coupled nonconfluent configuration rounding
is not disproved, but it is not a network-flow consequence of the reset
atlas; it remains the exact coefficient-one gate.

## 8. Dependency ledger

This note uses:

- `MATH_THEOREM_COMMON_CORE_NONMECHANICAL_RESET_RECURSION_20260726.md`
  for the deletion-robust state alphabet, projective deletion law,
  front-tail trace identity, and rankwise fractional capacity;
- `MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md` for
  the literal path normal form and the middle occurrence count; and
- `MATH_AUDIT_GLOBAL_RECURSIVE_SCD_TO_PROMOTION_RING_FACTORIZATION_20260726.md`
  for the ambient-order confluence obstruction and the original
  root-coupling scale.

All quantitative estimates used in the renewal no-go are reproved above.
