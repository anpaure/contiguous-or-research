# Uniform forced-facet spread eliminates every optional co-small core

**Date:** 2026-08-04  
**Method:** pure mathematics; probabilistic method plus the sharp
partial-shadow theorem; no computation, search, or solver  
**Status:** unconditional asymptotic closure of the optional co-small
factor-extension gate for a simultaneously selected common-core witness
reservoir.  This theorem does not by itself close the separate small-cut,
global-residence, upper-host, or compiler gates.

## 0. Main result

Let `P` be the incidence lift of the hybrid clipped-resident common-core
witness reservoir in `ML_m`.  It can be selected with all previously
proved properties and with the additional uniform forced-facet bound

\[
 \boxed{
 z_U:=|N(U)\cap Z_P|\le9
 \qquad(U\in\tbinom{[2m-1]}m),}
\tag{0.1}
\]

where `Z_P` is the protected lower-q1 palette.

Consequently every owner has optional gap

\[
 g_U=m-z_U\ge m-9.
\tag{0.2}
\]

For this reservoir no positive optional co-small obstruction exists.
Equivalently, every co-small complement containing the forced bank
`Z_P` satisfies the exact residual-capacity Hall inequality.

The proof has two parts.  First, the already-used random trace orders are
chosen to spread protected facets over **owner stars** as well as lower
stars.  Second, the high-tail greedy packing treats a nearly saturated
owner star as another forbidden resource bank.

## 1. Cross-trace hits under one owner

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m.
\]

For every noninterval low trace `T`, the low-path order on `K` is selected
independently and uniformly as in the random trace-spread theorem.

Fix an owner `U`, put

\[
 S=U\cap E,\qquad e=|S|.
\]

Deleting an external coordinate `a in S` gives the lower facet

\[
 L_a=U-\{a\}
\]

of exact external trace `T_a=S-{a}`.  When `T_a` is a randomized low
trace, its size is `q=e-1`, and its path has `q-1=e-2` immediate lower
colours.  Symmetry of the random `K` order gives

\[
 \Pr(L_a\in Z_P)
 ={e-2\over {m-1\choose e-1}}.
\tag{1.1}
\]

The events for different `a` are independent, because the traces
`S-{a}` are distinct and their path orders are independent.

Let `Y_U` count these randomized cross-trace hits.  Only

\[
 4\le e\le m-d
\]

can contribute.  Therefore

\[
 \Pr(Y_U\ge3)
 \le {e\choose3}
 \left({e-2\over {m-1\choose e-1}}\right)^3.
\tag{1.2}
\]

### Lemma 1.1 (simultaneous cross-trace cap)

The random low paths can be chosen so that

\[
 \boxed{Y_U\le2\quad\text{for every owner }U.}
\tag{1.3}
\]

This choice can be made simultaneously with the previously proved lower
star and endpoint-spread bounds.

#### Proof

The number of owners with `|U cap E|=e` is

\[
 {m\choose e}{m-1\choose e-1}.
\]

Summing (1.2) over all owners gives at most

\[
 \begin{aligned}
 \Sigma_m
 &:=\sum_{e=4}^{m-d}
 {m\choose e}{m-1\choose e-1}{e\choose3}
 \left({e-2\over {m-1\choose e-1}}\right)^3\\
 &=\sum_{e=4}^{m-d}
 {m\over e}
 {{e\choose3}(e-2)^3\over {m-1\choose e-1}}.
 \end{aligned}
\tag{1.4}
\]

We claim `Sigma_m=o(1)`.  For each fixed `4<=e<=8`, its summand is
`O(m^{-(e-2)})`.  For `9<=e<=m/4`, unimodality gives

\[
 {m-1\choose e-1}\ge {m-1\choose8},
\]

while the numerator in one summand is `O(m^6)`; the sum over this range
is `O(m^{-1})`.  Finally, for `m/4<e<=m-d`, unimodality gives

\[
 {m-1\choose e-1}
 \ge
 \min\left\{
 {m-1\choose\lfloor m/4\rfloor-1},
 {m-1\choose d}
 \right\}.
\]

The first term is exponential in `m`, and the second is
`m^omega(1)` because `d to infinity`; in particular their minimum is
`omega(m^8)`.  There are at most `m` summands, each with numerator
`O(m^6)`, so this final range is also `o(1)`.  Hence `Sigma_m=o(1)`.

The total bad-event probability used in the existing simultaneous lower
star and endpoint-spread selection is also `o(1)`.  Taking the union of
the two bad-event families still has probability below one.  Thus one
choice satisfies both the old spread bounds and (1.3). \(\square\)

## 2. The pre-high owner load is at most seven

Fix an owner `U` again.

All facets obtained by deleting a `K` coordinate have the same exact
external trace.  The same-trace adjacency theorem implies that at most
two of them lie in the protected lower palette of the top-plus-low bank.

Among facets obtained by deleting an `E` coordinate, at most two have a
cyclic-interval trace when `2<=|S|<=m-1`, by the one-point cyclic
completion lemma.  When `|S|<=3`, there are at most three external
deletions directly.  When `S=E`, the deleted traces have size `m-1`, while
the top lower palette has external-trace sizes at most `m-2`, so the
contribution is zero.  Thus the deterministic top/hinge bank contributes
at most three cross-trace facets in every case.

Lemma 1.1 contributes at most two randomized low cross-trace facets.
Therefore, before the high-tail paths are selected,

\[
 \boxed{z_U\le2+3+2=7\quad\text{for every owner }U.}
\tag{2.1}
\]

## 3. The high-tail greedy packing preserves a cap of nine

### Lemma 3.1 (one high path adds at most two facets per owner)

The immediate lower colours of one monotone high-tail geodesic contain at
most two facets of any fixed owner.

#### Proof

Write the lower colours of the geodesic as

\[
 L_t=C\cup\{x_{t+2},\ldots,x_{q-1}\}
          \cup\{y_1,\ldots,y_t\}.
\]

Then `|L_t triangle L_s|=2|t-s|`.  Two distinct facets of one owner differ
by exactly one exchange, so they can occur only for `|t-s|=1`.  Three
indices cannot be pairwise consecutive. \(\square\)

At an intermediate greedy stage call an owner **critical** when

\[
 z_U\ge8.
\]

Forbid every lower facet of every critical owner.  The total owner-facet
load is

\[
 \sum_Uz_U=m|Z_P|,
\tag{3.1}
\]

because every rank-`m-1` lower vertex has exactly `m` containing owners.
The reservoir has `|Z_P|=O(m2^m)`, uniformly throughout the greedy
construction.  Hence there are `O(m^2 2^m)` critical owners and at most

\[
 O(m^3 2^m)
\tag{3.2}
\]

new forbidden lower resources.

The symmetric high-tail lower-resource denominator is
`2^(2m-o(m))`.  Multiplying (3.2) by the at most `m` positions of a
candidate path still gives failure probability

\[
 2^{-m+o(m)}<1.
\]

Thus this new bank can be added to all existing resource-collision and
lower-star critical banks.  A legal high path remains at every step.
Critical owners receive no new protected facet; a noncritical owner has
load at most seven and receives at most two by Lemma 3.1.  Induction from
(2.1) proves (0.1).

All previously proved disjointness, complete upper-cone coverage,
clipped residence, lower-star spread, and endpoint-spread properties are
unchanged.

## 4. Sharp partial shadows rule out the optional core

The bound (0.1) immediately gives the forced-bank base condition, because

\[
 g_U=m-z_U\ge m-9\ge2
\]

for all sufficiently large `m`.

Suppose, for contradiction, that the optional residual factor deficiency
is positive.  Let `B^-` be the inclusion-minimal positive optional core
and put

\[
 Q=\{U:a_U>0\},
 \qquad
 a_U=(b_U-(g_U-c_U))_+\in\{1,2\}.
\]

The exact minimal-core ledger gives

\[
 \sum_Ua_U>2|B^-|.
\]

Since `a_U<=2`,

\[
 \boxed{|Q|>|B^-|.}
\tag{4.1}
\]

For every `U in Q`, positivity and `c_U<=2` give

\[
 b_U(B^-)
 \ge g_U-c_U+1
 \ge m-10.
\tag{4.2}
\]

Apply the sharp one-sided partial-shadow theorem to the adjacent-rank
families `(B^-,Q)` with threshold

\[
 D_0=m-10.
\]

The strict imbalance (4.1) gives

\[
 |B^-|
 \ge {2D_0-1\choose D_0-1}+1
 ={2m-21\choose m-11}+1
 =2^{2m-o(m)}.
\tag{4.3}
\]

On the other hand, the near-shadow localization theorem says every
co-small failed complement—and hence its optional part `B^-`—has size

\[
 |B^-|=O(m^2 2^m)=2^{m+o(m)}.
\tag{4.4}
\]

Equations (4.3)--(4.4) contradict each other for all sufficiently large
`m`.  Therefore no positive optional core exists.

By the exact optional-complement/factor equivalence, the protected path
bank extends across every co-small residual cut.  This proves the claimed
optional co-small closure.

### Corollary 4.1 (the exact load threshold is linear, not constant)

The constant nine is much stronger than necessary.  Let a protected bank
with the same co-small cutoff satisfy

\[
 \max_U z_U\le R_m.
\]

Then the same proof gives positive-owner threshold

\[
 D_m=m-R_m-1
\]

and therefore

\[
 |B^-|\ge {2D_m-1\choose D_m-1}+1.
\]

In particular, for every fixed `epsilon>0`, the optional core is already
impossible under

\[
 R_m\le(1/2-\epsilon)m.
\tag{4.5}
\]

Indeed the last binomial coefficient is
`2^(2D_m-o(m))>=2^((1+2epsilon)m-o(m))`, still larger than the
`2^(m+o(m))` co-small cutoff.  Uniform forced-facet spread therefore has
a large robustness margin.

## 5. Exact scope

This theorem closes the optional bootstrap obstruction which survived the
earlier `d-2` gap bound.  Its decisive improvement is not another local
bootstrap estimate: it changes the reservoir selection so that every
owner has only `O(1)` protected facets.  A positive owner would then need
`m-O(1)` optional core facets, and the sharp threshold-shadow theorem
makes that incompatible with the independently proved co-small cutoff.

It does not assert that the protected bank already forms a connected
Hamilton carrier, is globally cyclically resident, has the required
upper occurrence chronology, or satisfies a terminal lower compiler.
Those remain separate gates.

## 6. Dependencies

- `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`
- `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`
- `MATH_THEOREM_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_20260804.md`
- `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md`
- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`
