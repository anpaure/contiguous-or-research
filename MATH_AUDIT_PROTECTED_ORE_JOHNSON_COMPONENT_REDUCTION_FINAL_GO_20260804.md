# Independent audit: protected-Ore Johnson-component reduction

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PROTECTED_ORE_JOHNSON_COMPONENT_REDUCTION_20260804.md`  
**Audited theorem SHA256:**
`e8d77dc370839a0ee8fe3bb23d47aef6fa51059f65cae5d51dfb17c0b02bbd7c`  
**Method:** independent symbolic proof.  No computation, search, solver, or
remote machine was used.

## Verdict

**GO after three proof-scope corrections made in the audited theorem.**

The exact component additivity, connected-cut equivalence, one-support
classification, and small-side connected-set count are correct.  The
corrections were:

1. a connected `b=0` family is one complete uniform layer
   `{{S}\choose {m-1}}`, not necessarily one graph-theoretic Johnson
   clique;
2. the quoted near-shadow cardinality localization in Corollary 3.2 is
   stated only for `m>=4`, so that hypothesis is now explicit; and
3. the DFS entropy bound applies to small connected cuts, not
   automatically to the small complements of co-small connected cuts.
   The latter are now routed to the exact co-small complement normal form,
   without an unsupported entropy claim.

None of these corrections changes Theorems 1.1 or 3.1.

## 1. Exact owner separation

Let

\[
 A=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_c
\]

be the component decomposition of the induced Johnson graph.  The
`m` lower facets of an upper owner `U` form a clique in the Johnson graph:
two distinct facets intersect in rank `m-2`.  Therefore an owner cannot
meet two distinct `A_i`.  In particular, the upper shadows `N(A_i)` are
pairwise disjoint.

Fix `U in N(A_i)`.  For the full cut and component cut respectively,
write

\[
 p_U^A=e_P(U,\mathcal L\setminus A),\qquad
 p_U^i=e_P(U,\mathcal L\setminus A_i).
\]

The potentially dangerous complement identity is

\[
 \mathcal L\setminus A_i
 = (\mathcal L\setminus A)
   \mathbin{\dot\cup}(A\setminus A_i).
\]

But `U` has no incidence edge at all, protected or otherwise, to
`A\setminus A_i`.  Hence

\[
 \boxed{p_U^i=p_U^A.}
\]

Also `a_U^i=a_U^A`.  Owners outside `N(A_i)` have `a_U^i=0`, so their
local contributions to both `sigma(A_i)` and `lambda_P(A_i)` vanish even
if their complement-defined `p_U^i` is nonzero.  This resolves the only
nonformal issue caused by the complement convention in `p_U`.

## 2. Additivity of all four quantities

Because every owner with positive `a_U` belongs to exactly one component
shadow, and its `a_U,p_U` values agree there, the owner sums split.  The
term `-2|A|` also splits over the disjoint union.  Therefore

\[
 \sigma(A)=\sum_i\sigma(A_i),\qquad
 \lambda_P(A)=\sum_i\lambda_P(A_i).
\]

The disjointness of the upper shadows gives

\[
 |N(A)|=\sum_i|N(A_i)|,qquad |A|=\sum_i|A_i|,
\]

and hence `s(A)=sum_i s(A_i)`.  Finally, the local value

\[
 1_{\{2\le a_U\le m-1\}}(m-a_U)
\]

is zero off the component shadows and unchanged on the unique component
shadow containing `U`.  Thus `b(A)=sum_i b(A_i)` as claimed.

## 3. Connected-cut equivalence

The frozen Ore--Ryser theorem says that extension is equivalent to

\[
 \lambda_P(A)\le\sigma(A)
 \quad\text{for every }A\subseteq\mathcal L.
\]

If the inequality is known for every nonempty Johnson-connected family,
additivity proves it for every nonempty family by summing over its induced
components.  The empty family has both sides zero.  Conversely, checking
all cuts trivially checks the connected cuts.

Equivalently, if

\[
 \sum_i\lambda_P(A_i)>\sum_i\sigma(A_i),
\]

then at least one index has
`lambda_P(A_i)>sigma(A_i)`.  Hence every failed cut has a connected failed
component.  This is exact and does not require `sigma(A_i)>=0`.

## 4. The `b=0` one-support consequence

The frozen equality classification is

\[
 A=\mathop{\dot\bigcup}_j {{S_j}\choose {m-1}},
 \qquad |S_i\cap S_j|\le m-3.
\]

For each nonempty support `S`, the induced graph on
`{{S}\choose {m-1}}` is the Johnson graph `J(|S|,m-1)` and is connected.
Distinct support families have no Johnson edge because their supports
intersect in at most `m-3` points.  Thus these support families are
exactly the induced components, and connectedness leaves exactly one.

Conversely, for `A={{S}\choose {m-1}}`, an owner has `0`, `1`, or all
`m` of its facets in `A`, so `b(A)=0`; and the family is connected whenever
nonempty.  The corrected conclusion is therefore exactly

\[
 \boxed{A={{S}\choose {m-1}}.}
\]

It is a single graph-theoretic clique only when `|S|<=m`; for larger `S`
it is a complete uniform layer on one support.  The theorem now uses the
latter terminology.

## 5. Connected-set DFS entropy

Fix global orders and map a connected `t`-set `A` to:

1. its least vertex;
2. its canonical breadth-first spanning tree; and
3. the full depth-first traversal of that tree, returning to the root.

The traversal is a Johnson-graph walk of length exactly `2(t-1)`, and its
visited-vertex set is exactly `A`.  Therefore the map from `A` to the
encoded walk is injective: equal encoded walks have equal visited sets.
There are at most `|\mathcal L|` roots and at most
`Delta=m(m-1)` choices at each step.  Hence

\[
 C_t\le|\mathcal L|\Delta^{2(t-1)}.
\]

The endpoint `t=1` gives `C_1=|\mathcal L|` and is also covered.

## 6. Interaction with near-shadow localization

For `m>=4`, first replace an arbitrary failed cut by a connected failed
component.  Applying the frozen localization theorem to that component
gives

\[
 \min\{|A|,|\mathcal L\setminus A|\}
 <{m(m-1)\over2m-1}|E(P)|.
\]

There are two different cases.

* If `A` is the small side, Theorem 3.1 gives the advertised connected-set
  entropy bound.
* If `A` is co-small, its small complement need not be Johnson-connected.
  The DFS bound cannot be applied to that complement.  The valid further
  reduction is instead the exact co-small normal form in Theorem 5.1 of
  the frozen dependency: the complement must contain an almost-complete
  owner clique and violate its degree/rebate inequality.

For `b(A)=0`, either side is already covered by the exact one-support
classification.  Thus the corrected corollary combines cleanly with the
near-shadow theorem but makes no false complement-connectivity inference.

## 7. Dependency and scope check

The cited dependency
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` has
SHA256
`c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0`,
matching the theorem's citation.

This result is a cut-family reduction only.  It proves neither the
protected factor extension itself nor residence, arbitrary-width upper
witnesses, component fusion, or the common cap.

## Final verdict

After the three corrections listed above, the protected-Ore
Johnson-component reduction is **GO** for use as a frozen pure-mathematical
dependency.
