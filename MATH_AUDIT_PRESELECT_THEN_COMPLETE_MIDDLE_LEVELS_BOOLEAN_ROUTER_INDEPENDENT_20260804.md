# Independent audit: preselect-then-complete Middle Levels Boolean router

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_PRESELECT_THEN_COMPLETE_MIDDLE_LEVELS_BOOLEAN_ROUTER_20260804.md`  
**Audited SHA-256:**
`13c3c3baea1e2e667f748ba49fafef297f49d6e8771d09043c96e823f8bb72bc`  
**Verdict:** **GO.**  The theorem is an exact conditional composition of
three valid steps.  No finite search or numerical computation is used.

## 1. Eligible-port Hall calculation

The injected gains are distinct rank-`(m-1)` sets.  Two such sets have at
most one common rank-`m` upper neighbour, since a common neighbour, if it
exists, must be their union.  Thus for a nonempty gain subfamily `X`,
`x=|X|`,

\[
 \left|\bigcup_{i\in X}A_i^0\right|
 \ge xL_0-\binom x2.
\]

Deleting a global forbidden port bank of size `f_0` leaves at least

\[
 xL_0-\binom x2-f_0
\]

ports.  Hall is therefore implied by

\[
 q_0(x)=x(L_0-1)-\binom x2-f_0\ge0.
\]

The quadratic is concave, so its minimum on the integer interval
`1<=x<=p` occurs at an endpoint.  These endpoints are exactly

\[
 f_0\le L_0-1,
 \qquad
 p(L_0-1)-\binom p2-f_0\ge0.
\]

The simple conditions `p<=L_0`, `f_0<=L_0-1` imply the second endpoint
because

\[
 q_0(p)\ge(p-1)\left(L_0-1-{p\over2}\right)\ge0.
\]

For `p=1` the product is zero; for `p>=2`, use `L_0>=p>=2`.  The empty
gain bank is vacuous.  Thus the source handles every small case.

These are exact endpoint conditions for this Bonferroni/concavity proof;
they are sufficient rather than claimed necessary for the underlying
eligible graph.

## 2. Sequential two-coordinate selection

After choosing `mu_0`, remove only `mu_0(i)` from the phase-1 menu of the
same gain `i`.  Every reduced menu has size at least `L_1-1`.  Reapplying
the previous Hall calculation with this lower bound gives endpoints

\[
 f_0\le L_1-2,
 \qquad
 p(L_1-2)-\binom p2-f_0\ge0,
\]

which are exactly `(P1)`.

The resulting `mu_1` is injective on the right shore and satisfies
`mu_1(i)!=mu_0(i)` for every gain.  Hence:

* every injected left vertex has exactly two distinct selected edges;
* every right vertex has at most one edge from each matching and therefore
  total degree at most two; and
* no edge repeats, so the union has exactly `2p` edges.

Thus `Delta(M_0 union M_1)<=2`.  Allowing `mu_1(i)=mu_0(j)` for `i!=j` is
correct and important: it creates permitted right degree two.  Deleting
the entire phase-0 image from every phase-1 menu would be an unjustified
loss of up to `p` choices per gain.

When `L_0=L_1=L`, the simple conditions `p<=L-1`, `f_0<=L-2` imply both
coordinate Hall systems.

## 3. Protected-factor completion

The cited small protected-factor theorem says exactly that a subgraph of
`ML_m` with maximum degree at most two and at most `m-2` edges lies in a
spanning two-factor.  Therefore `(F0)` and `(F01)` are precisely its
hypotheses for the selected bank plus any pre-existing protected bank.

The scalar bounds

\[
 |E(P_*)|+p\le m-2,
 \qquad\text{or}\qquad
 |E(P_*)|+2p\le m-2
\]

are sufficient for edge count, but the degree-two condition must still be
checked against `P_*`.  The source states this explicitly.  With
`P_*` empty, a matching is 1-bounded and the union of the two sequential
matchings is 2-bounded automatically.

The completion theorem is undirected and supplies an arbitrary two-factor.
It does not supply compatible orientations, a component bound, an upper
palette, residence, or compiler state; the source keeps these outside the
conclusion.

## 4. Suffix Hall composition

For one coordinate, selected right vertices are distinct.  Under the
assumed physical lift their Boolean base values are distinct, so their
typed one-step menus have pairwise overlap at most one.  Repeating the
same Hall calculation with menu lower bound `L_suf` and forbidden bank
`f_1` gives exactly

\[
 f_1\le L_{\rm suf}-1,
 \qquad
 p(L_{\rm suf}-1)-\binom p2-f_1\ge0.
\]

For two coordinates, values are distinct inside each selected matching.
Thus across the union every Boolean value has multiplicity at most two.
The repaired grouped Boolean theorem applies with `rho=2`, giving exactly

\[
 f_1\le L_{\rm suf}-2,
 \qquad
 T(L_{\rm suf}-2)-\binom T2-f_1\ge0.
\]

Here `T` counts distinct values among all `2p` occurrence tickets.  The
simple conditions `T,f_1<=L_suf-2` are sufficient by concavity.

This must be one joint Hall instance.  Two separate suffix matchings could
reuse one physical sink or another cross-coordinate capacity and would not
prove the conclusion.

## 5. Literal disjointness and compatibility audit

The route concatenation is proof-safe only because the source assumes all
of the following in one materialized state:

1. every selected abstract incidence has a physical occurrence-labelled
   prefix from an allocated unit source;
2. all selected prefixes, including both coordinate banks, are jointly
   capacity-disjoint and avoid the fixed compensation/protected banks;
3. the physical lift preserves the selected coordinate and terminal type;
4. every retained upper value has one fixed sink occurrence legal for
   every selected ticket whose menu contains that value;
5. distinct values use distinct unit-capacity sink occurrences;
6. the forbidden upper bank removes every collision with a prefix,
   compensation route, or protected bank; and
7. every further physical unit resource on a one-step arc is node-split
   and private.

The Hall injection chooses distinct upper values.  These premises therefore
make the prefix-plus-suffix concatenations pairwise vertex-disjoint and
typed legal.  In the two-coordinate conclusion, allocating two unit source
tickets per logical gain is explicit.

The theorem does not infer nonseparable product compatibility between the
two representatives of one logical gain; such compatibility must be
encoded in the menus or proved separately.

## 6. Central Boolean counts

In `ML_m`, every left rank-`(m-1)` vertex has `m` rank-`m` neighbours.
Every selected rank-`m` port has `m-1` one-coordinate extensions to rank
`m+1` inside `[2m-1]`.  Thus, after at most `c` typed exclusions,

\[
 L_{\rm suf}=m-1-c.
\]

The simple two-coordinate suffix bounds become

\[
 T,f_1\le m-3-c.
\]

If each phase retains at least `L` raw incident ports before the global
bank `F_0`, the simple preselection bounds are

\[
 p\le L-1,
 \qquad f_0\le L-2.
\]

With no additional protected edges, the factor bound is `2p<=m-2`.
Therefore `p,f_0,T,f_1=O(sqrt(m))` and only `O(1)` typed exclusions satisfy
all scalar inequalities for sufficiently large `m`.  This asymptotic
observation does not create any physical occurrence data.

## 7. Scope verdict

The source proves the exact order

\[
 \text{eligible preselection}
 \Longrightarrow
 \text{protected two-factor completion}
 \Longrightarrow
 \text{conditional joint suffix routing}.
\]

It does not prove the injection, menus, and prior protected bank coexist in
a fully guarded carrier; a native/transported phase-1 occurrence exists;
the prefixes or sinks survive the common cap and background compiler; the
completed factor has acceptable topology or upper shadows; the selected
roles admit compatible cycle orientations; or the construction
regenerates.  Consequently it has no standalone implication for
`nu(k)<=B(k)+O(1)`.

