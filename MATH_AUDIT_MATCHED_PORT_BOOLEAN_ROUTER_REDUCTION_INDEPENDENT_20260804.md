# Independent audit: matched-port Boolean router reduction

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_MATCHED_PORT_BOOLEAN_ROUTER_REDUCTION_20260804.md`  
**Pre-audit SHA-256:**
`8e90e125b9eeade58a554ffa09d0c563ea90bcf902e31b7a94136052ea77d235`  
**Repaired source SHA-256:**
`732d2c8d4c4318a09dceb00435387df719b691aa3d81d9359887dba8af0e6524`  
**Verdict:** **GO after scope/quantifier repairs.**

The abstract Hall arguments were correct.  The source was repaired to make
the positive-degree assumption, matching-selection quantifier, literal
prefix privacy, occurrence/type compatibility, small cases, and precise
Middle-Levels parameter explicit.  A proposed bounded-multiplicity
strengthening was independently verified and added.  No computation is
used.

## 1. Degree-balanced Hall

Assume `h>=1`.  For every `X subseteq G`, all `h|X|` factor incidences
from `X` terminate in `N_B(X)`, while the total degree available there is
at most `h|N_B(X)|`.  Hence

\[
 h|X|\le h|N_B(X)|,
\]

and division by the positive `h` gives Hall.  Thus a saturating matching
`mu:G->P` exists.

This proves only an abstract factor matching.  It does not prove that an
arbitrarily chosen matching has incidence-typed menus or pairwise distinct
Boolean values.  The repaired theorem correctly fixes one matching and
places those properties on that matching as additional hypotheses.  If
only a subset of incidences is eligible, that eligible subgraph needs its
own Hall certificate.

## 2. Distinct selected values: overlap and Hall algebra

For distinct rank-`s` values `p,p'`, an `(s+1)`-set containing both exists
only when `|p union p'|=s+1`, and then it is uniquely `p union p'`.
Therefore any incidence-specific restrictions of their upper shadows
intersect in at most one value.

For `x` selected gains, first-order Bonferroni gives

\[
 \left|\bigcup N_g\right|\ge xL-\binom x2.
\]

After a forbidden bank of size `f`, Hall follows from

\[
 q(x)=x(L-1)-\binom x2-f\ge0.
\]

The quadratic is concave.  Its endpoint checks are

\[
 q(1)=L-1-f\ge0
\]

and, for `p=|G|<=L`,

\[
 q(p)\ge(p-1)\left(L-1-{p\over2}\right)\ge0.
\]

The small cases are sound: an empty gain bank is vacuous; for `p=1` the
last product is zero; for `p>=2`, `L>=p>=2` gives
`L-1-p/2>=L/2-1>=0`.  Thus Lemma 2.2 is correct for every allowed
integer parameter.

## 3. Bounded-multiplicity strengthening

Let selected occurrence tickets be grouped by their rank-`s` Boolean base
value.  Suppose at most `rho` tickets use one value and there are `T`
distinct values.  For a nonempty ticket subfamily `X`, let `t` be the
number of value groups it meets.

Within one active group, the union of the ticket menus has size at least
`L`, because it contains the menu of any one member.  For two different
groups, the two menu unions are subsets of different full upper shadows,
so their intersection has size at most one.  Hence

\[
 \left|\left(\bigcup_{u\in X}N_u\right)\setminus F\right|
 \ge tL-\binom t2-|F|.
\]

The demand of `X` is at most `rho t`.  Hall is therefore implied by

\[
 q_\rho(t):=t(L-\rho)-\binom t2-|F|\ge0
 \qquad(1\le t\le T).
\]

Again this is concave.  Its endpoint conditions are exactly

\[
 |F|\le L-\rho,
 \qquad
 T(L-\rho)-\binom T2-|F|\ge0.
\]

The simpler proposed hypotheses

\[
 T\le L-\rho,
 \qquad |F|\le L-\rho
\]

are sufficient, because the second endpoint is at least

\[
 (T-1)\left(L-\rho-{T\over2}\right)\ge0.
\]

For `T=1` this is zero; for `T>=2`, use `L-rho>=T`.

Thus the strengthening is correct.  If two coordinatewise selected banks
are internally value-distinct, their union has multiplicity at most two.
Taking `rho=2` proves one joint suffix matching whenever

\[
 T\le L-2,
 \qquad |F|\le L-2.
\]

This conclusion is valid only for one shared Hall instance.  Separate
coordinatewise matchings do not control cross-coordinate sink collisions.

## 4. Literal occurrence and type quantifiers

The literal concatenation is valid under the repaired hypotheses:

1. the complete prefix family is fixed in one cap/guard/phase state;
2. prefix interiors are physically private, with only the named common
   starts and terminal port gates allowed before matching;
3. the selected matching leaves one prefix per claim and distinct physical
   terminal ports, so the retained prefixes are mutually disjoint;
4. all prefixes already avoid the fixed compensation and protected
   capacity banks;
5. for each retained upper value `Y`, one physical occurrence `r(Y)` is
   fixed and is legal for every selected incidence/ticket whose menu
   contains `Y`;
6. distinct upper values use distinct physical sink occurrences;
7. `F` removes every retained occurrence colliding with a selected prefix,
   compensation route, or protected bank; and
8. after node splitting every physical unit resource, the one-step arcs
   have no unpriced shared interior.

The Boolean Hall matching chooses distinct upper values, hence distinct
sink occurrences.  Concatenation with the selected prefixes is therefore
pairwise vertex-disjoint and typed legal.

For the grouped/two-coordinate version, every occurrence ticket also needs
its own allocated unit source capacity, and the prefixes must be private
jointly across coordinates.  The one Hall instance controls shared suffix
capacity; it does not establish an additional nonseparable compatibility
relation between the two representatives of one logical ticket unless that
relation is encoded in the menus.

## 5. Middle-Levels specialization

A rank-`m` port in a `(2m+1)`-element ground set has exactly `m+1`
one-coordinate upper extensions.  If at most `c` are typed-forbidden, then

\[
 L=m+1-c.
\]

For a nonempty bank `0<=c<=m` makes `L>=1`.  The distinct-value theorem
therefore requires

\[
 |G|\le m+1-c,
 \qquad |F|\le m-c.
\]

In the convention where `ML_q` uses ranks `q-1,q` of `[2q-1]`, this is the
lower shore of `ML_(m+1)`, not `ML_m`; the repaired source records this
parameter shift.  For multiplicity `rho`, the simple grouped conditions
become

\[
 T\le m+1-c-\rho,
 \qquad |F|\le m+1-c-\rho.
\]

At `rho=2` these are `T,|F|<=m-1-c`.

The abstract small protected-factor theorem supplies the degree-balanced
factor only after an explicit injection of logical gains into its shore.
It does not supply the physical port identification, the menu-rich
matching, occurrence addresses, or joint typed sink bank.  The source no
longer suggests otherwise.

## 6. Relation to prior router theorems

The pair-overlap/concavity calculation for distinct selected values is the
existing small-port Boolean theorem applied to `Q=mu(G)`.  It is not a new
Boolean-shadow theorem.  The genuine reduction is the order of
quantifiers:

\[
 \text{choose one factor port per gain first, then route only those ports.}
\]

This strictly weakens full-port gammoid rank.  A witness is a left-degree-2
factor in which every gain has one good degree-one port and one bad
degree-one port.  Give the good ports distinct Boolean menus satisfying the
theorem and make every bad port a suffix-gammoid loop.  The good ports form
a saturating matching and route all gains, while the full port set is
dependent because it contains the loops.

The bounded-multiplicity theorem is an additional grouped extension of the
prior distinct-port statement.  Neither result replaces the exact
factor-restricted Rado theorem for arbitrary multi-step networks, unpriced
duplicates, or shared interiors.

## 7. Scope verdict

The repaired source proves a conditional but unconditional-in-its-
hypotheses router theorem.  It does **not** construct:

* a menu-rich saturating matching when only some factor incidences qualify;
* literal prefixes or physical Boolean port occurrences;
* the common cap/guard/phase state;
* joint source/prefix capacity across two occurrence coordinates;
* nonseparable product compatibility not encoded in the menus; or
* regeneration, a universal OR word, or `nu(k)<=B(k)+O(1)`.

Within those stated boundaries, the degree Hall, Boolean Hall, grouped
strengthening, literal concatenation, and Middle-Levels specialization are
all valid.

