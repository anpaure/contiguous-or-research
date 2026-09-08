# Pascal transfer of PBBS permanent switching and capped component pressure

Date: 2026-07-30  
Lane: R, pure-mathematics audit of handoff item 1997  
Status: exact conditional transfer theorem, exact deletion counterexample,
and an exact mixed-depth obstruction.  No unconditional all-`k` upper bound
is claimed.

## 0. Verdict

The two completion mechanisms in item 1997 behave differently under an
odd/even Pascal lift.

1. **Permanent-ratio switching is block-stable but not column-deletion
   stable.**  On every unbraided Pascal interior the child candidate graph
   is an exact relabelled parent candidate graph at an adjacent envelope
   depth.  A direct sum preserves all weighted permanent deletion ratios
   sector by sector, and gives ratio one between sectors.  However, isolating
   the interiors requires deleting every interval column whose parent-owner
   footprint crosses a Pascal cut.  Matched-prefix endpoint deletion, which
   is all that item 1997 assumes, does not imply stability under these right
   column deletions.  The uniform injection graph `K_(2,N)` is an exact
   counterexample: one pair ratio is `N/(N-1)` before deleting columns and
   becomes `2` after only two right columns remain.

2. **A two-matching component cube has a stronger bounded-cut transfer.**
   Given explicit parent cubes, omit the targets used by either shore on the
   seam-dependent columns and delete those columns.  Both shores then
   restrict to saturating matchings on the same retained target set.  Keep
   the original parent component bits tied across any fragments created by
   deletion; do **not** independently resample the fragments.  This correlated
   restricted law preserves every surviving transported signature
   probability.  If `c` is the number of chart cuts and `D` is the child
   compiler depth, the fail-closed omission toll is at most

   \[
                 2cD(3D+1)=O(cD^2).                 \tag{0.1}
   \]

   Thus a bounded-cut Pascal chart has an `O(k)` transfer toll when
   `D=Theta(sqrt(k))`.  The theorem requires nonempty promoted collar cores
   and uses the complete mixed-depth interior conflict family.

3. **Standard parent pressure has no automatic termwise mixed-depth
   domination.**
   At child depth `D`, the odd-to-even facet shore is the parent
   depth-`D+1` envelope, but its physical run horizon is still `D`.  A
   positive envelope run of exactly `D+1` positions contributes a child run
   window and contributes no standard depth-`D+1` parent run window.  Thus
   the displayed component has zero standard run contribution but positive
   facet-shore run contribution.  Thus the existing standard-pressure proof
   supplies no termwise charging; a separate aggregate comparison theorem
   or mixed-depth surcharge is required.

4. **The known Pascal lifts do not automatically meet the bounded-cut
   hypotheses.**  The direct common-colour even-to-odd construction has one
   pair of turns per Catalan component.  Substitution of its Catalan-many
   cuts into (0.1) is not `O(k)`.  The protected-braid position bound
   `|R|<=c(D+2)` proves a one-matching Hall interface, but does not by itself
   give either arbitrary-column deletion stability or a component-compatible
   two-shore collar completion.  A rethreaded `O(1)`-cut lift, or a direct
   bound on the full collar/fusion signature pressure, is still required.

Consequently item 1997 does not yet transfer unconditionally from odd to
even dimensions.  The exact positive transfer theorem below shows what is
enough, and the two counterexamples show why the currently proved parent
hypotheses are insufficient.

## 1. Mixed-depth interval candidate graphs

Let `T=(T_i)` be a strict Johnson chronology.  For an envelope depth
`h>=0`, put, away from linear ramps,

\[
 P^{[h]}_p=\bigcap_{a=0}^{h}T_{p-a},\qquad
 F^{[h]}_p=(P^{[h]}_p\setminus P^{[h]}_{p-1})
           \cup(P^{[h]}_p\setminus P^{[h]}_{p+1}).  \tag{1.1}
\]

For an interval `I` of source positions, put

\[
 P^{[h]}(I)=\bigcup_{p\in I}P^{[h]}_p,\qquad
 F^{[h]}(I)=\bigcup_{p\in I}F^{[h]}_p.              \tag{1.2}
\]

For a target family `S` and an interval horizon `a`, define
`G_(h,a)(T;S)` to have left side `S`, right side all interval columns of
length at most `a`, and edge `(S,I)` exactly when

\[
             F^{[h]}(I)\subseteq S\subseteq P^{[h]}(I).            \tag{1.3}
\]

The standard item-1997 graph at depth `D` is `G_(D,D)`.  Mixed graphs are
unavoidable under Pascal: the envelope depth changes by one while the child
physical interval horizon remains `D`.

For pressure statements, write `C_(h,a;D)` for the complete contracted
run/positive-guard conflict family on `G_(h,a)`, with physical positive-run
windows of length `D+1`.  Thus the last parameter is a physical conflict
horizon, not an envelope depth.

All statements have cyclic and linear versions.  A linear ramp is simply
included among the declared collars.

## 2. Exact Pascal interior charts

### Theorem 2.1 (candidate-graph charts)

Fix a child compiler depth `D`.

**Odd to even.**  Let `T` be the odd parent row, let
`I_i=T_i cap T_(i+1)`, and form the two child sectors

\[
                      A_i=T_i,\qquad B_i=\{z\}\cup I_i.            \tag{2.1}
\]

On every unbraided interior, after deleting `z` from the target label on the
second shore, the two child candidate graphs are

\[
                         G_{D,D}(T),\qquad G_{D+1,D}(T),            \tag{2.2}
\]

up to the index shift `i -> i+1` on the second shore.  The no-`z` and
`z`-containing target families are disjoint.  The old part of the singleton
target `{z}` is the empty target and must be supplied separately if it is
not already in the second package.

**Even to odd.**  On a direct common-colour component

\[
 zT_a,\ldots,zT_b,U_{b-1},\ldots,U_a,qquad
 U_i=T_i\cup T_{i+1},                               \tag{2.3}
\]

the `zT` interior is `G_(D,D)(T)`.  The reversed-`U` interior, after the
exact index reversal, has envelope depth `D-1`.  If its child length-`D`
columns are pruned, the retained parent package is exactly

\[
                              G_{D-1,D-1}(T).         \tag{2.4}
\]

This pruning is legitimate only when the displayed parent package already
saturates the required no-`z` target shore.

In each chart, candidate links and alternating components wholly inside an
interior are transported bijectively.  Hence a new external guard bridge
which is not the image of a parent bridge must use a promoted or
seam-crossing column.

#### Proof

The event-stream identities give

\[
 P_D(A)_i=P_D(T)_i,
 \qquad P_D(B)_i=\{z\}\cup P_{D+1}(T)_{i+1},        \tag{2.5}
\]

and

\[
 P_D(zT)_i=\{z\}\cup P_D(T)_i,
 \qquad P_D^{\rm rev,U}(U_i)=P_{D-1}(T)_{i+D}.     \tag{2.6}
\]

These are Theorems 3.1 and 3.2 of
`MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`.
Taking unions over a source interval preserves the same identities.

The mandatory core in (1.1) is a symmetric nearest-neighbour difference
functional of the envelope row.  It therefore commutes with an index shift
and with reversal.  A coordinate constant on a sector belongs to neither
neighbour difference; consequently adjoining or deleting the constant
coordinate `z` gives exactly (1.3) for the old target part.  This proves the
candidate-edge bijections.

An interval link is the assertion that one target has two candidate
columns.  Candidate-edge bijection therefore transports the entire
interior link graph and every alternating component.  QED.

### Remark 2.2 (what the event theorem does not say)

Theorem 2.1 is an interior theorem.  It proves neither:

* that a Pascal turn has a nonempty mandatory core;
* that old-coordinate residence survives that turn;
* that the child mixed pressure `C_(D+1,D;D)` is bounded by the standard
  parent pressure `C_(D+1,D+1;D+1)`; nor
* that a Hall law remains well behaved after seam-dependent right columns
  are deleted.

These are logically separate conditions.

## 3. Direct sums and permanent deletion ratios

For a weighted left-saturating matching graph `H`, let `Z_H` be its matching
partition function.  For a partial matching `Q`, write `H\ominus Q` for
deletion of its endpoints.  Item 1997 uses

\[
 \rho_H(e,f)=
 {Z_H Z_{H\ominus\{e,f\}}\over
  Z_{H\ominus e}Z_{H\ominus f}}.                   \tag{3.1}
\]

### Lemma 3.1 (exact block-sum transfer)

Let `H=H_1 disjoint_union ... disjoint_union H_t`, with product edge
weights.  Endpoint-delete an arbitrary partial matching in every block.
Then

\[
 \rho_H(e,f)=
 \begin{cases}
   \rho_{H_i}(e,f),&e,f\in H_i,\\
   1,&e\in H_i,\ f\in H_j,\ i\ne j.
 \end{cases}                                         \tag{3.2}
\]

If block `i` has the direct pair bound

\[
                  \rho_{H_i}(e,f)\le1+{\gamma_i\over h_i},        \tag{3.3}
\]

then at child horizon `D` the direct sum has the item-1997 form with

\[
                   \gamma_*=D\max_i{\gamma_i\over h_i}.           \tag{3.4}
\]

In particular, common constants `gamma_i<=gamma` give

\[
 \gamma_*\le\gamma
 \quad\hbox{for odd-to-even depths }D,D+1,           \tag{3.5}
\]

whereas the even-to-odd depths `D,D-1` give

\[
 \gamma_*\le\gamma {D\over D-1}\le2\gamma
 \quad(D\ge2).                                      \tag{3.6}
\]

The corresponding all-arity cylinder constant is `exp(gamma_*/2)`.

#### Proof

Partition functions multiply over a disjoint union, before and after every
endpoint deletion.  Cancelling the factors gives (3.2).  Equations
(3.4)--(3.6) are algebra.  The item-1997 prefix multiplication then gives
the displayed cylinder constant.  QED.

### Definition 3.2 (the deletion-stable switching hypothesis actually needed)

Call a family of weighted candidate graphs **right-hereditary at horizon
`D`** if the bound (3.3), or its external-switch double-counting
certificate, remains valid after:

1. arbitrary omission of target parts;
2. arbitrary deletion of interval columns and their incident candidates;
3. every subsequent compatible endpoint-prefix contraction;

whenever the residual graph still has a left-saturating matching.

This is stronger than the endpoint-prefix hypothesis in item 1997.

### Theorem 3.3 (conditional permanent transfer)

Take either Pascal chart in Theorem 2.1.  Delete every column whose chart
dependency footprint crosses a declared collar, and prune the reversed
union length-`D` columns as in (2.4).  If each transported parent package is
right-hereditary, the residual child block sum satisfies the item-1997 pair
bound with `gamma_*` in (3.4).  Cross-sector pairs have zero same-component
error mass.

#### Proof

Right heredity permits exactly the target and right-column deletions used to
form the safe interiors.  Theorem 2.1 identifies each residual sector with
the corresponding parent residual graph.  Apply Lemma 3.1.  QED.

On the even-to-odd depth-`D-1` shore, a child conflict can have `D+1`
edges, so the sequential proof can condition `D-1` earlier edges before its
last pair.  The standard depth-`D-1` parent application only needs prefixes
through size `D-2`.  Thus even apart from right-column deletion, the child
requires one additional prefix level.  Definition 3.2 deliberately includes
it; the ordinary same-depth parent theorem does not.

## 4. Prefix stability does not imply right heredity

### Proposition 4.1 (explicit injection counterexample)

Let `H_N=K_(2,N)`, give every edge weight one, and use the uniform law on
left-saturating matchings.  Let

\[
                   e=(u_1,v_1),\qquad f=(u_2,v_2).                 \tag{4.1}
\]

Then

\[
 \Pr(e)=\Pr(f)={1\over N},\qquad
 \Pr(e,f)={1\over N(N-1)},                         \tag{4.2}
\]

so

\[
                         \rho_{H_N}(e,f)={N\over N-1}.             \tag{4.3}
\]

After deleting the right columns `v_3,...,v_N`, the residual graph is
`K_(2,2)` and

\[
                  \Pr(e)=\Pr(f)=\Pr(e,f)={1\over2},\qquad
                  \rho_{K_{2,2}}(e,f)=2.            \tag{4.4}
\]

Thus for `N>=D+1` the original ratio has item-1997 parameter at most one,
while the deleted graph requires parameter at least `D`.  No
dimension-independent prefix ratio theorem can be transported through
arbitrary Pascal column excision without Definition 3.2 or a new collar
law.

#### Proof

There are `N(N-1)` ordered injections of the two left vertices.  Exactly
`N-1` use `e`, exactly `N-1` use `f`, and exactly one uses both.  This proves
(4.2)--(4.3).  The two injections of `K_(2,2)` prove (4.4).  QED.

This counterexample does not refute the same-component inequality of item
1997; that inequality is exact.  It refutes the missing monotonicity step
needed to infer a Pascal residual estimate from a parent prefix estimate.

## 5. Exact seam-footprint count

An interval of `a` source positions in an envelope row of depth `h` depends
on a consecutive owner block of length `h+a`.  For one fixed cut, exactly
`h+a-1` starts have a dependency block crossing that cut.  Hence the number
of interval columns of lengths at most `A` whose chart footprint crosses one
cut is at most

\[
 Q(h,A)=\sum_{a=1}^{A}(h+a-1)
       =Ah+{A(A-1)\over2}.                           \tag{5.1}
\]

For the odd-to-even facet shore `(h,A)=(D+1,D)`,

\[
                         Q(D+1,D)={D(3D+1)\over2}.                  \tag{5.2}
\]

This dominates the copied shore count `D(3D-1)/2`.  On the retained
even-to-odd packages, the copied shore again has `D(3D-1)/2`, while the
pruned union shore has

\[
                         Q(D-1,D-1)={(D-1)(3D-4)\over2}.           \tag{5.3}
\]

If a declared cut is incident with two independently charted oriented
pieces, summing the two one-sided counts is fail-closed.  Thus for `c` cuts
the universal two-sided bound is

\[
                         |U|\le cD(3D+1),                           \tag{5.4}
\]

where `U` is the full unsafe interval-column set.  In a single global
backward-envelope orientation only one side reaches across each cut, and
the sharper half of (5.4) applies.

The count is only a column count.  It is not, by itself, a bound on the
capped pressure of a collar hypergraph.

## 6. A component-cube transfer which needs no permanent estimate

Let a two-matching cube be generated by saturating matchings `M^0,M^1` on
one residual target set.  Its symmetric-difference components are chosen
independently and uniformly.

### Lemma 6.1 (universal cylinder constant two)

Every two-matching component cube satisfies, for every shore-consistent
edge set `F`,

\[
                    \Pr(F)\le2^{|F|}\prod_{e\in F}\Pr(e).          \tag{6.1}
\]

Thus `C_0=2` is always a valid item-1997 cylinder constant.

#### Proof

Let `v` be the number of varying edges of `F` and let `q` be the number of
symmetric-difference components used by those edges.  Consistency gives
`Pr(F)=2^{-q}`.  Each varying edge has marginal `1/2`, every fixed edge has
marginal one, and `q<=v`.  Therefore

\[
                 2^{|F|}\prod_e\Pr(e)=2^{|F|-v}\ge1\ge2^{-q}.
\]

QED.

### Theorem 6.2 (safe-column Pascal cube transfer)

Fix one of the Pascal charts of Theorem 2.1 and its complete mixed-depth
interior conflict families.  In each parent sector let
`M_i^0,M_i^1` be two saturating matchings on the same target set.  Transport
them to the child interiors.  First discard any deliberately pruned column
which is unused by both supplied matchings.  Let `U` be the remaining unsafe
seam-footprint column set from Section 5.  Put

\[
 O=\{S:\text{ some }M_i^b\text{ matches }S\text{ to a column in }U,\
                  b\in\{0,1\}\}.                    \tag{6.2}
\]

Then

\[
                              |O|\le2|U|.            \tag{6.3}
\]

After omitting `O` and deleting `U`, both transported shores restrict to
saturating matchings of the same retained child target set.  Suppose in
addition that:

1. the child chronology is deadline-resident, upper-complete, and has the
   required safe linear opening;
2. every collar source position has a certified nonempty core (or its
   complete source-empty conflict family is separately charged);
3. every run/guard conflict using only safe columns is wholly contained in
   one Pascal sector; and
4. in sector `i`, the capped pressure of the complete mixed-depth conflict
   family under the original parent component-bit law is at most `K_i`.

Then the child correlated restricted-cube law has capped pressure at most

\[
                              \sum_iK_i,             \tag{6.4}
\]

and item 1997 gives

\[
                 \nu(k_{child})
                 \le B(k_{child})+2|U|+\sum_iK_i.   \tag{6.5}
\]

Any pre-existing closure omissions are added to the right side.

#### Proof

A matching uses a right column at most once, so each shore contributes at
most `|U|` targets to (6.2).  Removing `O` removes every edge of either
shore on `U`; the restrictions still saturate every retained target.

Deleting target rows and edges can split a symmetric-difference component.
Choose one unbiased bit for the **original** parent component and use that
same bit on every surviving fragment.  Every bit assignment is the
restriction of an old saturating matching, and therefore saturates the
retained target set.  A surviving conflict under this correlated law was
already a conflict under the parent law with exactly the same signature
probability.  Conflicts containing a deleted edge disappear; independently
resampled hybrid conflicts are not introduced.

By assumptions 2--3, every surviving conflict is the transported image of
one sector conflict.  Orient it by the transported parent orientation.
Target families of different Pascal sectors are disjoint, and
`min(1,a+b)<=min(1,a)+min(1,b)`, proving (6.4).  Apply the general
target-capped alteration theorem, Theorem 6.1 of item 1997, to this
correlated law and append the omitted targets `O` literally.  QED.

Independently resampling the split geometric components is not sound for
this transfer: two opposite-shore fragments which formerly belonged to one
component can become simultaneously selectable and can create a new hybrid
conflict.  The tied-bit law is the exact correction.

### Corollary 6.3 (bounded-cut transfer)

If `D^2=O(k_child)`, the Pascal chart has `c=O(1)` cuts, the intentionally
pruned columns are already absent from the supplied sector matchings, and
`sum_i K_i=O(k_child)`, then

\[
                             \nu(k_{child})\le B(k_{child})+O(k_{child}).
                                                               \tag{6.6}
\]

This is an exact positive Pascal-preservation theorem.  Its substantive
hypothesis is the **mixed-depth** pressure bound in Theorem 6.2(4), not the
standard same-depth parent bound.

## 7. General collar completions and component fusion

Safe-column excision is deliberately wasteful.  A protected Pascal braid
may instead complete both shores through collar ports.  The exact issue is
component fusion.

Let `mathcal P` be the transported parent symmetric-difference components.
Each child symmetric-difference component induces a block of parent
components, with a fixed shore parity on each member.  For a consistent
transported conflict `F`, let

\[
 p(F)=2^{-|\operatorname{supp}_{\mathcal P}(F)|},\qquad
 \delta(F)=|\operatorname{supp}_{\mathcal P}(F)|
            -|\operatorname{blocks}(F)|.            \tag{7.1}
\]

Then its exact probability in the child cube is

\[
                              p_{child}(F)=2^{\delta(F)}p(F).       \tag{7.2}
\]

An inconsistent parity signature has probability zero.

Let `phi_i` be the target-label map from parent sector `i` to the child.
It is injective within one sector, but two sectors may project to the same
old target after deleting the new coordinate.  Put

\[
 \mu=\max_R\left|\{(i,S):S\text{ is transported in sector }i,
                    \ \phi_i(S)\setminus\{z\}=R\}\right|.         \tag{7.3}
\]

For both adjacent-dimension Pascal charts, `mu<=2`.  This multiplicity is
needed when several sector loads are bounded by one undecorated parent
load.  If the sector pressures are kept separately, as in Theorem 6.2, no
multiplicity factor is needed.

### Theorem 7.1 (fusion-aware capped transfer)

Suppose every child conflict which is not transported wholly from one
sector contains an edge whose target belongs to a declared collar target
set `H`.  Orient all such conflicts to such a target.  Orient transported
conflicts by parent orientations.  Then the child capped pressure is at
most

\[
 |H|+
 \sum_S\min\left\{1,
    \sum_{F\to S}2^{\delta(F)}p(F)\right\}.          \tag{7.4}
\]

In particular, component-compatible collar completion (`delta(F)=0` for
every transported conflict) preserves the sum of the parent capped
pressures and costs at most `|H|`.

#### Proof

Equation (7.2) follows because every child block has one unbiased bit,
whereas the unfused parent cube has one unbiased bit per parent component.
The collar conflicts are supported on targets in `H`; after target capping,
their total contribution is at most `|H|`.  Substitute (7.2) for every
transported conflict and sum the oriented loads.  QED.

If the two sector loads are pullbacks of one parent oriented-load family of
fusion-amplified capped pressure `K_fuse`, then (7.3) gives the coarser
bound

\[
                         |H|+\mu K_{\rm fuse}+K_{\rm scarce},      \tag{7.5}
\]

where `K_scarce` is the capped load on child target layers outside the
transported parent compiler families.  Formula (7.4), not (7.5), is exact
when the sector loads differ.

The fibres and scarce layers are explicit.  In the odd-to-even chart the
child low targets are

\[
 \{S:1\le|S|\le r-1,\ z\notin S\}
 \ \dot\cup
 \{\{z\}\cup R:0\le|R|\le r-2\}.                  \tag{7.6}
\]

Deleting `z` gives fibre two for `1<=|R|<=r-2`, fibre one on the no-`z`
rank-`r-1` layer, and the sole new old-empty target `{z}`.  If the parent
package includes its rank-`r-1` layer, the scarce compiler family is just
`{z}`; declared collar targets are already charged by `|H|` in (7.5).

In the even-to-odd chart the child low targets are

\[
 \{S:1\le|S|\le r,\ z\notin S\}
 \ \dot\cup
 \{\{z\}\cup R:0\le|R|\le r-1\}.                  \tag{7.7}
\]

The common parent compiler range `1<=|R|<=r-1` has fibre at most two.  The
new scarce families are the no-`z` rank-`r` layer and the singleton `{z}`.
The common-colour factor normally owns the rank-`r` layer deterministically,
but that reservation and its collar interactions belong to the forced
background; they are not bounded by the parent pressure theorem.

The protected-braid theorem bounds changed envelope positions and displaced
targets for **one specified matching** by `c(D+2)`.  It does not assert a
common two-shore collar completion, does not bound `delta(F)`, and is stated
in its position-port matching model rather than the complete item-1997
interval-column graph.  Therefore that position count alone does not prove
that either term in (7.4) is `O(k)`.  Formula (7.4), or the safe excision of
Theorem 6.2, is the exact additional audit.

Component fusion cannot be ignored: identifying `t` formerly independent
bits can multiply the probability of a compatible signature by `2^(t-1)`.
The universal cylinder bound of Lemma 6.1 remains true, but using it requires
an independent `O(k)` bound on the full marginal run/guard polynomial with
`C_0=2`.

## 8. The mixed-depth facet obstruction

### Proposition 8.1 (standard run terms do not dominate mixed run terms)

Fix `D>=1`.  Let one coordinate `x` have a positive component of exactly
`D+1` consecutive positions in the depth-`D+1` envelope row.  Assume the
forced negative background is empty on this component and, at every one of
its positions, there is a residual singleton interval candidate in a
distinct target part whose target omits `x`, and every displayed candidate
extends to a positive-weight saturating matching (equivalently, each
displayed marginal `q_x(J_j)` is positive).

At child conflict horizon `D`, these `D+1` singleton columns form one
minimal negative cover of the unique `D+1` window.  Its term in the run
polynomial is

\[
                       \prod_{j=1}^{D+1}q_x(J_j)>0.                \tag{8.1}
\]

At standard parent horizon `D+1`, the same positive component contains no
window of length `D+2`, so its entire contribution to the standard run
polynomial is zero.

Consequently the contribution of this coordinate component to the standard
`(D+1,D+1;D+1)` **run polynomial** is zero while its contribution to the
required mixed `(D+1,D;D)` run polynomial is positive.  Thus there is no
term-by-term or coordinate-component multiplicative domination of the
mixed run polynomial by the standard run polynomial.

#### Proof

The first assertion is exactly the definition of an inclusion-minimal
interval cover of a run window.  The second is the strict inequality between
the component length `D+1` and the standard window length `D+2`.  QED.

The proposition does not assert that the full standard run-plus-guard
pressure is zero, nor does it rule out a separate aggregate charging
inequality between the two complete polynomials.  Such an inequality is
precisely the missing mixed-depth comparison theorem.

The example is compatible with nonempty source cores by placing a different
mandatory coordinate in each singleton source cell.  The coordinate `x` is
constant across the displayed envelope component and hence need not belong
to any mandatory difference core.  Thus this is not an artifact of allowing
empty source cells.

On the even-to-odd reversed-union shore, after pruning the extra length-`D`
columns, the child run window is one position longer than the standard
depth-`D-1` parent run window.  Covering a longer window covers each shorter
subwindow, so a conflict-free standard parent assignment remains run-safe.
For alteration pressure, however, a quantitative target-oriented charging
map must still be stated; raw conflict counts need not be monotone.

## 9. Link-return and guard-bridge scope

Within a flat unbraided chart, Theorem 2.1 transports the interval-link
graph exactly.  In particular:

* every child alternating bridge supported on safe interior columns is a
  parent alternating bridge at the displayed adjacent depth;
* deleting safe/interior columns cannot create a link; and
* all genuinely new link entropy lies in promoted or chart-crossing collar
  columns.

More precisely, Theorem 6.1 of
`MATH_THEOREM_R_ALLK_PBBS_PREFIX_SWITCHING_SOCKET_OBSTRUCTION_AND_RETURN_GATE_20260730.md`
says that two distinct columns in one flat return-free hull have no common
candidate target.  Equations (2.5)--(2.6) identify the child erosion row
with the corresponding parent erosion row, up to a shift, reversal and a
constant `z`.  Therefore flatness and return-freeness are preserved exactly
on each unbraided interior, and the return-free link theorem transfers with
no loss.  Equivalently, a nontrivial safe-interior child link pulls back to
an actual parent erosion-coordinate return in the convex hull of its two
columns.

This yields no new collar bridge supply, because promoted/crossing columns
are precisely where the flat-hull identification does not apply.  The
owner-level facet/union lifetime shifts do not alter this conclusion; at
the compiler level the stronger envelope identities (2.5)--(2.6) are the
relevant statement.

Thus Pascal recursion cannot manufacture the `Omega(D)` deletion-stable
external guard bridges demanded by item 1997 from interior algebra alone.
It can only transport an already proved parent supply; every additional
bridge must be certified in the collar atlas.

## 10. Exact odd/even implication boundary

The following implication is proved.

> For every sufficiently large child dimension, suppose there is a
> residence-safe, upper-complete Pascal chart with child deadline depth `D`,
> `c=O(1)` declared cuts, certified nonempty collar cores, and adjacent-depth
> parent sector cubes whose complete **mixed-depth** capped pressure sums to
> `O(k_child)`.  Suppose any deliberately pruned union columns are unused by
> those sector cubes.  Then the child has a literal compiler of length
> `B(k_child)+O(k_child)`.

The proof is Theorem 6.2 plus (5.4), together with the exact owner/shadow and
linear-opening hypotheses of the protected Pascal braid theorem.

None of the following is proved by the present PBBS/Pascal literature:

1. right-hereditary external switching in the mixed graphs of Theorem 2.1;
2. `O(k)` pressure for the odd-to-even mixed facet family
   `C_(D+1,D;D)`;
3. a component-compatible two-shore collar completion, or the fusion bound
   (7.4), for a general protected braid;
4. an all-`k` Pascal chronology with `O(1)` cuts and the required residence,
   all-depth shadow and linear-opening conditions.

The direct common-colour even-to-odd lift has Catalan-many components and
therefore does not satisfy the bounded-cut premise by its known topology.
This observation is a failure of the transfer proof, not a lower bound on
every possible rethreading of that lift.

The sharp next Pascal theorem is consequently one of:

* prove right-hereditary switching and the mixed facet pressure bound, then
  use Theorem 3.3;
* construct explicit adjacent-depth two-matching cubes and apply safe-column
  excision from Theorem 6.2; or
* prove a protected collar target set and fusion-weighted estimate satisfying
  (7.4) with total `O(k)`.

No negative association, finite SAT result, or computational enumeration is
used anywhere in this report.
