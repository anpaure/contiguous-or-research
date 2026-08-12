# Independent audit: co-selected reservoir small-cut closure and protected factor

**Date:** 2026-08-04  
**Method:** independent pure-mathematical reconstruction; no finite search or
solver  
**Audited theorem:**
`MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`  
**Audited SHA-256:**
`3b561fadc870fce0f5c19b0989a70506b1d1bfec4d218c07393e41145e12254c`  
**Verdict:** **GO**, in the actual deadline regime
`d=Theta(sqrt(m))`, subject to the cited Chao--Yu partial-shadow theorem.
The conclusion is exactly a spanning two-factor extending the protected bank;
it does not imply connectedness, global cyclic residence, an upper-complete
chronology, or a compiler.

There is one harmless polynomial bookkeeping correction in a dependency: in
the simultaneous lower-star high-tail greedy argument, forbidding every owner
above every critical lower vertex can cost `O(m^3(2^m+H_d))` owner resources,
not the displayed `O(m^2(2^m+H_d))` in the roughest direct count.  After the
additional at-most-`m` path-position factor this is still
`2^{-m+o(m)}`, so none of the existence conclusions or constants used by the
audited theorem changes.

## 1. Exact residual criterion

Let `Z` be the protected lower vertices and `X=L\Z`.  Every protected
lower vertex has protected degree two, every member of `X` has protected
degree zero, and an owner has residual capacity `c_U=2-d_P(U)`.  For
`A subseteq X`, capacitated Hall is exactly

\[
 \kappa(A)=\sum_U\min\{c_U,a_U\}\ge 2|A|.
\]

The local identity

\[
 \kappa(A)-2|A|=\sigma(A)-\lambda_P(A)
\]

holds owner by owner: an unprotected owner contributes `min(2,a_U)`, an
endpoint contributes `min(1,a_U)`, and an internal protected owner contributes
zero.  This verifies that the residual-Hall and protected-Ore languages used
in different sections of the theorem are interchangeable.

Also

\[
 \sum_Uc_U=2|X|.
\]

Indeed `|E(P)|=2|Z|` and the two middle-level shores both have size `W`.
Thus a residual matching saturating every lower demand automatically saturates
all owner capacities; after adding `P`, every vertex on both shores has degree
two.

## 2. Minimality and the `m-21` count

Choose an inclusion-minimal nonempty failed shore `A`.  Integrality gives
`kappa(A)<=2|A|-1`.  Removing `x in A` decreases an owner summand by one
exactly for

\[
 1\le a_U\le c_U.
\]

Since `A\{x}` is safe,

\[
 q_A(x):=\kappa(A)-\kappa(A\setminus\{x\})
 \le (2|A|-1)-2(|A|-1)=1.
\]

The minimality direction in Lemma 1.1 is therefore correct: every selected
lower vertex has at most one loose owner.

Let `H` be the union of the lower facets of the at most `2m` deterministic
top endpoints.  Then `|H|<=2m^2`.  For `x in A\H`, among its exactly `m`
owner neighbours there are at most

* ten internal protected owners, by `ell_P(x)<=10`;
* ten non-top endpoint owners, by `e_P^priv(x)<=10`;
* zero deterministic top endpoints, by `x notin H`; and
* one loose owner, by minimality.

Every other neighbour has `d_P(U)=0`, `c_U=2`, and, since it contains `x`
but is not loose, `a_U>=3`.  Hence it lies in `F`, proving the exact lower
bound

\[
 d_{\mathcal F}(x)\ge m-10-10-1=m-21.
\]

Each member of `F` contributes exactly two to `kappa(A)`, so

\[
 2|\mathcal F|\le\kappa(A)\le2|A|-1,
 \qquad |\mathcal F|\le |A|-1.
\]

No disjointness between the three exceptional owner classes is needed;
subtracting their separate upper bounds only weakens the estimate.

## 3. Bounded-ratio Chao--Yu corollary

The cited Chao--Yu theorem was checked against the source form in
arXiv:2307.15380v3, Theorem `PartialShadow`.  If an `r`-uniform family
`J` has size `binom(y,D)` and every member has at least `D` selected
facets in `C`, then

\[
 |C|\ge\binom y{D-1}.
\]

For nonempty `J` there is a unique `y>=D`.  If
`|C|<=q|J|`, then

\[
 {D\over y-D+1}
 = {\binom y{D-1}\over\binom yD}\le q,
\]

so `y>=D+D/q-1` and

\[
 |J|=\binom yD\ge\binom{D+D/q-1}D.
\]

Thus Lemma 3.1 has the correct direction, parameter translation, and real
binomial top.  Its nonempty hypothesis is necessary and is present in the
audited byte version.

## 4. Exponential contradiction on the nonpolynomial small side

If `a=|A|>=4m^2`, then `a_0=|A\H|>=2m^2` and
`a<=a_0+2m^2<=2a_0`.  Complementation turns `A_0` into an
`m`-uniform family `J` and `F` into an `(m-1)`-uniform family `C`.
The incidence direction reverses correctly:

\[
 x\subset U\quad\Longleftrightarrow\quad U^c\subset x^c.
\]

Every member of `J` has at least `D=m-21` facets in `C`, while

\[
 |C|=|F|\le a-1<2a_0=2|J|.
\]

The bounded-ratio lemma with `q=2` therefore gives

\[
 a_0\ge\binom{3D/2-1}{D}
      =2^{(c_*+o(1))m},
 \qquad c_*={3\over2}H_2(2/3)>1.
\]

For the same co-selected reservoir, the protected near-shadow theorem and
`|E(P)|=O(m2^m)` give

\[
 \min\{|A|,W-|A|\}=O(m^2 2^m)=2^{m+o(m)}.
\]

The forced-facet theorem applies to this same reservoir, not a separately
chosen one: the low-path bad-event sums are united before choosing the random
orders, and the high-tail greedy step forbids the union of the lower-star,
endpoint, and owner-star critical banks.  Therefore a co-small failed shore is
already excluded.  Any surviving failed shore must be on the small side, so
`a<=2^{m+o(m)}`.  This contradicts the preceding lower bound because
`c_*>1`.

The optional-complement linkage is exact.  For
`B=X\A`,

\[
 \mathcal L\setminus A=Z\mathbin{\dot\cup}B,
 \qquad
 \kappa(A)-2|A|=2|B|-\Omega_P(Z\cup B).
\]

Thus the co-small side in the cardinality dichotomy is exactly the optional
bank closed by the uniform forced-facet argument; there is no switch of cut
convention.

## 5. Pair-priced endpoint loss

For `A subseteq X`, all protected lower neighbours lie in `Z` and hence
outside `A`.  Ownerwise inspection gives

\[
 \lambda_P(A)
 =\sum_{x\in A}\ell_P(x)
  -\sum_{U:d_P(U)=2}(a_U-2)_+ +E_1(A).
\]

Dropping the favourable middle term is valid.  Every counted private
endpoint contains at least two members of `A` and is counted in
`e_P^priv(x)` for each of them, so there are at most `5|A|` such
endpoints.  Every counted deterministic top endpoint contains a pair of
distinct members of `A`.  A pair of distinct `(m-1)`-sets has at most one
common `m`-set owner, so choosing one pair below each top endpoint is
injective.  Its contribution is therefore at most

\[
 \min\{2m,\binom{|A|}{2}\}.
\]

Together with `sum ell_P(x)<=10|A|`, this proves exactly

\[
 \lambda_P(A)\le15|A|+
 \min\{2m,\binom{|A|}{2}\}.
\]

## 6. Kruskal--Katona range and constants

Complementing `A` gives an `a`-member family `J` of `m`-sets, and the
complements of `N(A)` are exactly its lower shadow.  Write
`a=binom(x,m)` with real `x>=m`.  The Lovasz real-binomial form of
Kruskal--Katona gives

\[
 |N(A)|\ge\binom x{m-1}
 =a{m\over x-m+1}.
\]

For sufficiently large `m`, `binom(m+3,3)>4m^2`; hence
`a<4m^2` implies `x<m+3` and

\[
 {|N(A)|\over a}>{m\over4}.
\]

The exact shadow-slack inequality then yields

\[
 \sigma(A)>
 {m-2\over m-1}\left({m\over4}-1\right)a
 ={(m-2)(m-4)\over4(m-1)}a=\beta_m a.
\]

For fixed `2<=a<=8`, `(beta_m-15)a>binom a2` eventually.  For
`a>=9`, `9(beta_m-15)>2m` eventually.  These two ranges therefore give
`sigma(A)>lambda_P(A)`.  A singleton is safe because
`sigma({x})=m-2` and `ell_P(x)<=10`.  This closes every
`1<=a<4m^2` shore.

## 7. Co-selection and exact scope

The four premises used by the final theorem are simultaneously available:

1. the random low orders satisfy both lower-star bounds and the owner-star
   forced-facet bound by one union bound whose total bad probability is
   `o(1)`;
2. the high-tail geodesics are then selected greedily while avoiding all
   critical banks at once;
3. this changes no path lengths, so the global edge count remains
   `O(m2^m)`; and
4. the deterministic top bank still has at most `2m` endpoint owners.

The forced-facet low-order estimate uses
`binom(m-1,d)=omega(m^8)` and hence requires `d to infinity`; the actual
deadline satisfies `d=Theta(sqrt(m))`.  The audited theorem is valid in
that intended regime.  It should not be read as a uniform theorem for fixed
`d` without a separate adjustment of that estimate.

Combining Sections 4 and 6 leaves no failed residual shore.  Capacitated
bipartite Hall then produces the residual integral matching, and the total
capacity equality upgrades it to a spanning two-factor.  Nothing in this
argument joins the factor cycles or supplies any of the later chronology,
residence-at-the-seams, upper-host, or compiler gates.

## 8. Audited dependencies

| role | file | SHA-256 during audit |
|---|---|---|
| lower-star and endpoint spread | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| uniform owner-star forced-facet spread | `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md` | `051c700a605f4820108846f9d5d2d220c01d00adcb0c4a7fec0dcbcfd8b9ffde` |
| protected near-shadow localization | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| optional-complement identity | `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md` | `55da48ce87926da31b0d226c368d75f2f7edd8b76cfb7b746993d6eadc9b625f` |
| sharp partial shadow | `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md` | `90748e697d5dd10eb5b8a5cf35b849da16f73f6b188f6b3f589ec0e6e43e785b` |

