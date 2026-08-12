# Core-pinned uniform spread and the exact residual factor/host cuts

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional co-selection, protected-factor extension, and
exact host-frontier theorem.  The clipped three-ring upper-witness reservoir
may be chosen with one common core coordinate while retaining all three
constant-spread estimates.  The small-cut and optional co-small theorems
therefore apply in the pinned fibre and give a spanning two-factor containing
the complete bank.  The factor row is closed.  The theorem then identifies
the separate static pull-host inequality.  It does not prove accessibility
in one pull phase, global residence, or ambient upper completeness.

## 0. Setting

Work in the Middle-Levels incidence graph

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m}.
\]

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
\]

and fix a core coordinate `q in K`.  Let `P=P_3(q)` be the incidence lift
of the following core-pinned **hybrid** realization of the clipped-resident
three-ring reservoir.  On every cyclic-interval top path, put `q` last in
the order on `K`; hence `q` is never deleted.  On the three top paths that
contain the ring hinges, retain the prescribed ring-deletion coordinate in
the first position, so those hinges remain the first protected
adjacencies.  On every
noninterval low trace use the pinned shortened path, and use the pinned
high-tail paths for the remaining traces.  Thus every
physical vertex of `P` contains `q`, every lower protected vertex has
degree two, and every owner has protected degree at most two.  Put

\[
 Z_P=\{x\in\mathcal L:d_P(x)=2\}.
\tag{0.1}
\]

The reservoir has

\[
 |E(P)|=O(m2^m).
\tag{0.2}
\]

## 1. Uniform owner-star spread survives core pinning

For a fixed owner `U`, define its forced-facet load

\[
 z_U=|N(U)\cap Z_P|.
\tag{1.1}
\]

### Theorem 1.1 (simultaneous core pin and all three spread caps)

For all sufficiently large `m`, the paths in `P_3(q)` can be selected so
that all the conclusions of the core-pinned reservoir theorem hold and

\[
 \boxed{
 z_U\le9\quad(U\in\mathcal U),\qquad
 \ell_P(x)\le10,\quad e_P^{\rm priv}(x)\le10
       \quad(x\in\mathcal L).}
\tag{1.2}
\]

Here `ell_P(x)=lambda_P({x})`, and `e_P^priv(x)` is the private/high
endpoint exposure used in the constant-spread theorem.  The at most `2m`
deterministic top endpoints remain priced separately.

#### Proof

Every protected lower vertex contains `q`, so the owner-star assertion in
(1.2) is automatic when `q notin U`.  Assume `q in U`, put

\[
 S=U\cap E,\qquad e=|S|.
\]

Keep the deterministic top and hinge choices from the hybrid realization
above.  This is still a genuinely pinned bank: putting `q` last in each
top-path order makes every top owner and immediate palette contain `q`.
For every noninterval low trace `T`, including trace size three, choose the
linear order of `K-{q}` independently and uniformly.

Deleting an external coordinate `a in S` gives the facet `U-{a}` of
trace `T_a=S-{a}`.  When this is a randomized trace, its core-pinned path
has `e-2` immediate lower colours.  The relevant `K-{q}` part is a
uniform subset of size `m-e-1` of an `(m-2)`-set.  Hence

\[
 \Pr(U-\{a\}\in Z_P)
 ={e-2\over {m-2\choose e-1}}.
\tag{1.3}
\]

The events for distinct `a` use distinct trace orders and are independent.
Only

\[
                         4\le e\le m-d-1
\]

enters the randomized range.  The number of owners containing `q` with
external size `e` is

\[
 {m\choose e}{m-2\choose e-1}.
\]

Therefore the expected number of owners receiving three randomized
cross-trace hits is at most

\[
 \Sigma'_m=
 \sum_{e=4}^{m-d-1}
 {m\choose e}{e\choose3}(e-2)^3
 {1\over {m-2\choose e-1}^{2}}.
\tag{1.4}
\]

Using

\[
 {{m\choose e}\over {m-2\choose e-1}}
 ={m(m-1)\over e(m-e)},
\tag{1.5}
\]

the summand in (1.4) is

\[
 {m(m-1)\over e(m-e)}
 {{e\choose3}(e-2)^3\over {m-2\choose e-1}}.
\tag{1.6}
\]

For fixed `e>=4` this is `O(m^(2-e))`.  For
`9<=e<=m/4`, the denominator is at least `{m-2 choose 8}` while the
remaining numerator is `O(m^6)`, so the total of that range is `O(1/m)`.
For `m/4<e<=m-d-1`, unimodality gives the denominator at least

\[
 \min\left\{
 {m-2\choose\lfloor m/4\rfloor-1},
 {m-2\choose d}
 \right\}=\omega(m^8),
\]

while the numerator in (1.6), summed over at most `m` indices, is
`O(m^8/d)`.  This range is also `o(1)`.  Consequently

\[
                              \Sigma'_m=o(1).
\tag{1.7}
\]

There is therefore a simultaneous choice with at most two randomized
cross-trace facets under every owner.

We next replay the two lower-star estimates in the pinned sample space.
If `q notin x`, a pinned owner over `x` can only be `x+q`; owner simplicity
makes its total private contribution at most one.  Assume `q in x` and put

\[
 S=x\cap E,\qquad D=(K-\{q\})\setminus x,
 \qquad |S|=|D|=s.
\]

Besides the possible own trace, a random path can meet the star of `x`
only for a trace `S+z`.  Its required `(K-{q})`-part is the fixed set
`(K-{q})-D`, and the pinned fixed-trace marginal gives

\[
 \mu_\ell(s)\le
 {(m-s)(s+1)\over {m-2\choose s}},
 \qquad
 \mu_e(s)\le
 {2(m-s)\over {m-2\choose s}}.
\tag{1.8}
\]

One path contributes at most one unit to either load.  The random range is
`2<=s<=m-d-3`.  Put `B_s={m-2 choose s}`.  The number of lower vertices
containing `q` with external size `s` is

\[
 N_s={m\choose s}B_s.
\]

For either load, the exponential-moment tail at six and (1.8) give a total
bad-event probability bounded by

\[
 \sum_{s=2}^{m-d-3}
 {m\choose s}B_s
 \left({e(m-s)(s+1)\over6B_s}\right)^6=o(1).
\tag{1.9}
\]

Indeed

\[
 {{m\choose s}\over B_s}
 ={m(m-1)\over(m-s)(m-s-1)}.
\]

For fixed `s>=2` the summand in (1.9) is `O(m^(6-4s))`.
For `4<=s<=m/2`, the exact ratio displayed above and
`B_s>={m-2 choose4}` make each summand `O(m^-4)`.  For
`m/2<s<=m-d-3`, unimodality gives
`B_s>={m-2 choose d+1}=m^omega(1)`, which dominates the polynomial
numerator uniformly over the at most `m` remaining indices.  Splitting off
`s=2,3` proves (1.9).

The bad-event sum in (1.9) and the owner-star bad-event sum (1.7) are both
`o(1)`.  Their union is therefore below one, so the same choice of all low
trace orders satisfies both kinds of spread.

Thus the random low contribution to both star loads is at most five
simultaneously at every lower vertex.  The possible own trace costs at
most one.  The same deterministic cyclic deletion/addition lemma prices
the pinned top/hinge bank by at most four singleton units.  (For a lower
vertex avoiding `q`, owner simplicity already gave the stronger bound
one.)  Hence before the high tail

\[
                         \ell_P(x),e_P^{\rm priv}(x)\le10.
\tag{1.10}
\]

Facets obtained by deleting a coordinate of `K-{q}` all have one exact
external trace, so the same-trace adjacency argument contributes at most
two.  Deleting `q` cannot contribute because every protected lower vertex
contains `q`.  The deterministic top/hinge bank contributes at
most three external-deletion facets, exactly as in the unpinned spread
theorem.  Before the high tail is packed,

\[
                              z_U\le2+2+3=7.
\tag{1.11}
\]

One monotone high-tail path contributes at most two facets under one owner.
During the greedy packing call an owner critical at load eight and forbid
all of its facets.  Since every protected lower vertex belongs to exactly
`m` owner stars,

\[
 \sum_Uz_U=m|Z_P|=O(m^2 2^m).
\]

Simultaneously call a lower vertex critical when either load in (1.10) is
ten.  One monotone high path raises each lower-star load by at most one.
The sum of either load over all lower vertices is at most a polynomial
factor times the number of resources already chosen, so the lower-star
critical bank adds only `2^(m+o(m))` forbidden owner resources.

Thus all three extra forbidden banks have size `2^(m+o(m))`.  The conditioned
core-pinned high-path denominators are `2^(2m-o(m))`, while the number of
high traces is `2^o(m)`.  The usual greedy union bound remains
`2^{-m+o(m)}<1`.  Critical owners receive nothing further and every other
owner receives at most two facets; critical lower stars receive no further
load.  This proves (1.2).  All exclusions used in
the pinned resource-disjoint packing are retained, so its owner, palette,
upper-witness, and clipped-residence conclusions are unchanged. \(\square\)

### Corollary 1.2 (optional co-small closure in the pinned fibre)

For the reservoir of Theorem 1.1 every optional co-small residual factor
cut is safe.

#### Proof

The optional gap at an owner is

\[
                         g_U=m-z_U\ge m-9.
\]

If a positive inclusion-minimal optional core `B^-` existed, the exact
optional-core ledger would produce an owner family `Q` with

\[
 |Q|>|B^-|,
 \qquad b_U(B^-)\ge m-10\quad(U\in Q).
\]

The sharp partial-shadow theorem therefore gives

\[
 |B^-|\ge {2m-21\choose m-11}+1=2^{2m-o(m)}.
\]

The protected near-shadow localization theorem and (0.2) give the
incompatible upper bound

\[
 |B^-|=O(m^2 2^m)=2^{m+o(m)}.
\]

Hence no such core exists. \(\square\)

This corollary is the precise compatibility statement missing from simply
placing the pinned-reservoir theorem beside the unpinned spread theorem.

## 2. All protected-Ore cuts close in the pinned fibre

For `A subseteq mathcal L`, write

\[
 a_U=|N(U)\cap A|,
\]

and let

\[
 \mathcal I_P=\{U:d_P(U)=2\},\qquad
 \mathcal E_P=\{U:d_P(U)=1\}.
\tag{2.1}
\]

The residual demand and capacity are

\[
 r_x=2-d_P(x),\qquad c_U=2-d_P(U).
\]

### Lemma 2.1 (the formerly surviving small-cut inequality)

If `P` has positive factor-extension deficiency, its unique minimal
maximum-deficiency shore `A^-` may be chosen so that

1. `A^- cap Z_P=emptyset`;
2. `A^-` is Johnson-connected;
3. `A^-` lies on the small side,

   \[
   |A^-|=O(m^2 2^m);
   \tag{2.2}
   \]

4. and it violates the single residual-capacity inequality

   \[
   \boxed{
    2|A^-|\le
    \sum_{U\in\mathcal U}
       \min\{2-d_P(U),a_U\}.}
   \tag{SC}
   \]

Equivalently, it satisfies

\[
 \boxed{
 \sum_{U\in\mathcal I_P}\min\{2,a_U\}
 +|\{U\in\mathcal E_P:a_U\ge2\}|
 >\sigma(A^-).}
\tag{2.3}
\]

Conversely, if `(SC)` holds for every Johnson-connected
`A subseteq mathcal L setminus Z_P` in the range (2.2), then `P` extends
to a spanning two-factor.

#### Proof

For an incidence-lift path bank, every protected lower vertex has degree
two and every other lower vertex has degree zero.  The irreducible-shore
theorem says `d_P(x)<=1` for every `x in A^-`; hence
`A^- cap Z_P=emptyset`.  The Johnson-component theorem lets one take a
connected failed component.  The near-shadow cardinality theorem says a
failed component is small or co-small.  Corollary 1.2 excludes the
co-small alternative, proving (2.2).

On a set disjoint from `Z_P`, every lower residual demand equals two and
no protected edge has its lower endpoint in `A`.  Therefore

\[
 r(A)=2|A|,
 \qquad
 \kappa_P(A)=
 \sum_U\min\{2-d_P(U),a_U\}.
\]

The exact residual Hall theorem is `r(A)<=kappa_P(A)`, which is `(SC)`.
Subtracting this capacity from the unprotected capacity
`sum_U min(2,a_U)` gives one unit precisely when
`U in mathcal E_P` and `a_U>=2`, and gives `min(2,a_U)` when
`U in mathcal I_P`.  This proves (2.3).

If a factor extension failed while every displayed connected small cut
passed, its minimal failed component would contradict the preceding
reduction. \(\square\)

The forced-facet bound `z_U<=9` closes the co-small optional problem because
a positive optional owner would need almost every facet.  By itself it does
not bound the two terms in (2.3) for an arbitrary small positive-defect
family.  The other two spread estimates in Theorem 1.1 do.

### Theorem 2.2 (pinned protected-factor extension)

For all sufficiently large `m`, the core-pinned co-selected reservoir `P`
satisfies `(SC)` on every residual shore and therefore extends to a
spanning two-factor of `ML_m`.

#### Proof

The co-selected small-cut theorem uses exactly four construction facts:

1. `ell_P(x)<=10` for every lower vertex;
2. `e_P^priv(x)<=10` for every lower vertex;
3. at most `2m` deterministic top endpoints; and
4. `z_U<=9` for every owner, through the optional co-small theorem.

Theorem 1.1 supplies all four facts for the same pinned reservoir.
Corollary 1.2 closes the co-small branch.  The small-cut theorem then
excludes every shore in (2.2): above `4m^2`, minimality plus the two
spread-ten bounds and the sharp partial-shadow theorem contradict the
`2^(m+o(m))` localization; below `4m^2`, the pair-priced endpoint bound and
Kruskal--Katona dominate the protected loss.  Hence no shore from Lemma
2.1 exists.  The residual capacitated Hall theorem supplies the integral
completion. \(\square\)

The factor supplied here may have many cycles.  Theorem 2.2 is not a
phase-cover or chronology theorem.

## 3. The exact static pull-host cut is different

Now use the complement-conjugate canonical pull system and the opposite
coordinate-half spanning pull tree `R_q^0` from the coordinate-wall theorem.
Let `g` be the coherent three-ring pull and let `D` be the pinned
reservoir together with the ring stubs and every protected edge required
in one fixed phase.  Fix a pairwise-support-disjoint, tree-compatible pull
host `H` on the same factor-component vertex set which contains
`R_q^0 union {g}`.  Every physical vertex of every pull in `R_q^0` avoids
`q`.  Let

* `A_D` be the forced-on pull labels needed to install `D`; and
* `B_D` be the forced-off labels whose opposite phases would delete or
  contradict an edge of `D`.

Accessibility and phase consistency mean that these sets are defined and
disjoint and that no required edge asks for two incompatible local phases.
Put

\[
                              J=A_D\cup\{g\}.
\tag{3.1}
\]

### Theorem 3.1 (exact coordinate-wall phase-cover cut)

Once accessibility and phase consistency hold, the pinned bank has a
last-ring Hamilton completion by the opposite-half tree if and only if
`J` is a graphic forest.  Equivalently, after loops are excluded,

\[
 \boxed{
 |J\cap E_H(X)|\le |X|-1
 \quad\text{for every }X\subseteq V(H),\ |X|\ge2.}
\tag{PH}
\]

Here `E_H(X)` retains parallel occurrence-labelled pull edges.

#### Proof

Necessity is the ordinary graphic-matroid independence criterion.  For
sufficiency, contract the components of `J`.  The opposite-half pull tree
`R_q^0` is connected after contraction, so a subset of it extends `J` to a
spanning tree.  Since `D` and the complete ring state lie in the `q=1`
half, no label of `R_q^0` belongs to the forced-off bank `B_D`.  Every
completing pull lies wholly in the `q=0` half,
whereas every protected bank and ring edge lies in the `q=1` half.  Hence
the completion touches no protected edge.  Holding out `g` leaves the
required pre-ring factor and toggling `g` gives the Hamilton factor.  This
is exactly the coordinate-wall basis-extension argument. \(\square\)

The now-closed inequalities `(SC)` and the still-open inequality `(PH)`
live on different objects.  `(SC)` is a residual-capacity cut on subsets
of the Middle-Levels lower shore.  `(PH)` is a graphic-rank cut on
components of one fixed pull factor.  The arbitrary factor supplied by
Theorem 2.2 need not lie in the fixed pull orbit, and the opposite-half
pull tree cannot be applied until accessibility, phase consistency, and
`(PH)` have been verified in that same host.

Thus the currently proved theorems do **not** compose as

\[
 \text{protected Ore completion}
 \Longrightarrow
 \text{opposite-half pull completion}.
\]

The missing quantifier is “the same factor state.”

## 4. Residence and upper completeness remain literal invariance rows

Let `F_J` be the factor state after the forced labels `J` are installed
and before the opposite-half completion pulls are toggled.

### Proposition 4.1 (the coordinate wall freezes the pinned run system)

The completing opposite-half pulls change no factor edge incident with a
vertex containing `q`.  Hence they preserve the entire induced `q=1`
path system of `F_J`, including all maximal positive `q`-run lengths.
Consequently a globally `d`-resident completion is possible by this route
only if every nonboundary positive `q`-run in `F_J` already has length at
least `d+1`.

#### Proof

Every edge of every completing pull has both endpoints in the `q=0`
half.  No edge incident with the `q=1` half is inserted or deleted.
Maximal positive `q`-runs are determined by precisely those unchanged
edges. \(\square\)

The constituent witness paths are clipped resident, but this does not
settle how their endpoint runs are joined in `F_J`.  This is the exact
remaining pinned-coordinate residence row.  For coordinates other than
`q`, even this wall invariance is unavailable unless a separate typed
state invariant is proved.

Likewise, the protected reservoir witnesses every target in the three-ring
damage family, but its all-width theorem assumes that the ambient carrier
was already upper-complete.  A pull which is physically disjoint from the
protected bank may still reorder remote occurrence intervals.  Therefore
the remaining upper-host premise is literally

\[
 \boxed{
 \text{one phase state }F_J\text{ is upper-complete outside the protected
 damage family, and every opposite-half completion pull preserves those
 selected witnesses}.}
\tag{UH}
\]

Vertex separation alone does not imply `(UH)`.

## 5. Exact frontier

The compatible pinned reservoir now has:

1. complete all-width witnesses for the three-ring damage cone;
2. clipped internal residence;
3. pairwise simple owners and immediate palettes;
4. uniform owner-star forced load `z_U<=9`; and
5. no optional co-small protected-factor obstruction; and
6. an unconditional spanning protected two-factor completion.

The remaining **fixed pull-orbit host** theorem is exactly the conjunction
of:

\[
 \boxed{
 \text{accessibility/phase consistency}+(PH)+
 \text{endpoint residence}+(UH).}
\]

All residual protected-Ore cuts are now closed.  Once `(PH)` holds in the
fixed host, the opposite-half pull tree makes every residual cographic
connectivity cut automatic.  Neither protected factor existence nor
uniform forced-facet spread proves that this factor lies in the chosen pull
orbit, or proves the accessibility/phase condition or the upper-witness
invariance condition.

## 6. Dependencies

- `MATH_THEOREM_CORE_PINNED_THREE_RING_RESERVOIR_AND_COORDINATE_WALL_PULL_COMPLETION_20260804.md`
- `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md`
- `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`
- `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md`
- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_JOHNSON_COMPONENT_REDUCTION_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md`
- `MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`
- `MATH_THEOREM_THREE_RING_CLIPPED_UPPER_CONE_RESERVOIR_AND_ALLWIDTH_TRANSPARENCY_20260804.md`
- `MATH_THEOREM_FORCED_PULL_PHASE_LAST_RING_BASIS_AND_CONJUGATION_NOGO_20260804.md`
