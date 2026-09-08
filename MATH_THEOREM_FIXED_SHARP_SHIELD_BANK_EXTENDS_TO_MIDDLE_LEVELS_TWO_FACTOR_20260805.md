# A fixed bank of sharp full-union shields extends to a middle-levels two-factor

**Date:** 2026-08-05  
**Method:** orbit avoidance, exact geodesic exposure, protected Ore--Ryser,
and the existing partial-shadow/co-small theorems; no computation or search  
**Status:** unconditional for every fixed number of shields and all
sufficiently large odd central parameters.  In particular, the eight
oriented full-union shields required by the four-arc common-history `C8`
can be planted in one owner/lower-`q1` spanning two-factor.  The theorem
does not connect that factor, construct depth-`d` source antecedents, or
preserve the upper deck and common cap after the `C8` rethread.

## 1. Setting

Work in the balanced middle-levels incidence graph

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},\qquad
 W=|\mathcal L|=|\mathcal U|.
\tag{1.1}
\]

A sharp full-union shield is the owner path from Theorem 3.1 of
`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`.
Thus, for a singleton `K` and disjoint ordered `(m-1)`-sets

\[
 X=(x_1,\ldots,x_{m-1}),\qquad
 Y=(y_1,\ldots,y_{m-1}),
\]

put

\[
 T_j=K\cup\{y_1,\ldots,y_j\}
          \cup\{x_{j+1},\ldots,x_{m-1}\},
 \qquad 0\le j\le m-1.                                    \tag{1.2}
\]

Its transition colour is

\[
 I_j=T_j\cap T_{j+1}
 =K\cup\{y_1,\ldots,y_j\}
       \cup\{x_{j+2},\ldots,x_{m-1}\},
 \qquad0\le j<m-1.                                       \tag{1.3}
\]

The incidence lift of the shield is the alternating path

\[
 T_0,I_0,T_1,I_1,\ldots,I_{m-2},T_{m-1}.                  \tag{1.4}
\]

## 2. Disjoint sharp shields exist

### Lemma 2.1 (fixed-bank orbit avoidance)

For every fixed integer `q`, and all sufficiently large `m`, there are
`q` sharp shields whose owner vertices, lower transition colours, and
upper Johnson-edge colours are separately pairwise disjoint.

#### Proof

Start with the canonical shield (1.2), and apply a uniformly random
coordinate permutation.  The coordinate symmetric group is transitive on
each of the three relevant ranks.  Consequently, for fixed forbidden
families

\[
 F_m\subseteq\mathcal U,\qquad
 F_{m-1}\subseteq\mathcal L,\qquad
 F_{m+1}\subseteq{[2m-1]\choose m+1},
\]

the expected number of collisions is

\[
 {m|F_m|\over W}
 +{(m-1)|F_{m-1}|\over W}
 +{(m-1)|F_{m+1}|\over {2m-1\choose m+1}}.                 \tag{2.1}
\]

After fewer than `q` shields have been selected, all three forbidden
families have size `O_q(m)`.  Both denominators in (2.1) are exponential
in `m`, so (2.1) is less than one for all sufficiently large `m`.  Some
coordinate image has no collision.  Induction selects all `q` shields.
\(\square\)

Only the owner and lower-colour disjointness is needed for factor
extension.  The upper-colour clause is retained because the shields are
intended for the upper-decorated `C8` graft.

## 3. Exact exposure of a geodesic bank

Let `P` be the union of the incidence paths (1.4) for the `q` shields from
Lemma 2.1.  Thus `P` is a vertex-disjoint path forest, every used lower
colour has protected degree two, and every owner has protected degree at
most two.

### Lemma 3.1 (two hits per geodesic)

For one sharp shield:

1. a fixed `x in mathcal L` is contained in at most two shield owners;
2. a fixed `U in mathcal U` contains at most two shield transition
   colours.

Hence a bank of `q` shields has both exposure bounds at most `2q`.

#### Proof

For `i<j`, formula (1.2) gives

\[
                         |T_i\cap T_j|=m-(j-i).              \tag{3.1}
\]

If a rank-`m-1` set lies in both owners, their intersection has rank at
least `m-1`; hence `j-i<=1`.  Three distinct path owners cannot all be
pairwise at distance at most one, proving the first assertion.

Likewise, from (1.3),

\[
                         |I_i\cup I_j|=m-1+(j-i).            \tag{3.2}
\]

If one rank-`m` owner contains both transition colours, their union has
rank at most `m`; again `j-i<=1`, and at most two such colours occur.
Summing over `q` shields proves the stated bounds. \(\square\)

Declare all `2q` path endpoints to be deterministic top endpoints.  In
the notation of the protected-factor theorems this gives

\[
 \ell_P(x)\le2q,\qquad e_P^{\rm priv}(x)=0,
 \qquad z_U=|N(U)\cap Z|\le2q,                              \tag{3.3}
\]

and there are only `2q` top endpoints.  Also

\[
                         |E(P)|=2q(m-1)=O_q(m).              \tag{3.4}
\]

## 4. Fixed-exposure protected-factor theorem

### Theorem 4.1

For every fixed `q` and all sufficiently large `m`, the forest `P`
extends to a spanning two-factor of the middle-levels incidence graph.

#### Proof

Give each owner residual capacity `c_U=2-d_P(U)`.  Protected Ore--Ryser
says that `P` extends precisely when

\[
 \kappa(A)=\sum_U\min\{c_U,|N(U)\cap A|\}\ge2|A|
 \qquad(A\subseteq\mathcal L\setminus Z).                  \tag{4.1}
\]

First apply the general protected-Ore near-shadow theorem.  Since
`e=|E(P)|=2q(m-1)`, every failed cut `A` satisfies

\[
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}e
 =O_q(m^2).                                                \tag{4.2}
\]

The co-small side is impossible.  Indeed, the exact optional-complement
identity produces from a positive co-small failure an inclusion-minimal
optional core `B^-` and an owner family `Q` with

\[
                         |Q|>|B^-|.
\]

Every owner in `Q` contains at least `D=m-2q-1` members of `B^-`: this is
the general forced-facet calculation, using `z_U<=2q` from (3.3) and
residual owner capacity at most two.  The sharp one-sided partial-shadow
theorem therefore gives

\[
 |B^-|\ge {2D-1\choose D-1}+1=2^{2m-o(m)}.                \tag{4.3}
\]

But `B^-` is contained in the co-small side from (4.2), which has size
`O_q(m^2)`.  This is a contradiction.  This is precisely the generic
argument of Corollary 4.1 in
`MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`,
now with the stronger polynomial cutoff (4.2).

Thus every hypothetical failed cut lies on the small side and has
`a=|A|=O_q(m^2)`.  The exact path-forest loss identity and (3.3) give

\[
 \lambda_P(A)
 \le 2q|A|+\min\left\{2q,{|A|\choose2}\right\}.             \tag{4.4}
\]

For every fixed `q`, (4.2) implies eventually

\[
                         1\le a<{m+3\choose3}.
\]

Kruskal--Katona therefore gives

\[
 \sigma(A)\ge
 { (m-2)(m-4)\over4(m-1)}|A|.                               \tag{4.5}
\]

For fixed `q`, (4.5) is larger than the protected-loss bound for all
sufficiently large `m`; singletons pass separately because
`lambda_P({x})<=2q<m-2=sigma({x})`.  Thus small failed shores do not exist
either.  No failed shore remains, so the residual integral
`b`-matching supplied by (4.1), together with `P`, is a spanning
two-factor. \(\square\)

## 5. The eight-shield corollary

### Corollary 5.1

For all sufficiently large `m`, the eight oriented prefix/suffix sharp
shields required by the four-arc common-history `C8` can be chosen with
disjoint owner, lower-`q1`, and upper-`q1` palettes and embedded in one
spanning owner/lower-`q1` two-factor.

#### Proof

Take `q=8` in Lemma 2.1 and Theorem 4.1. \(\square\)

This closes the **unrooted factor-planting** row for the full-union shield
route.  It does not yet prove that the eight factor paths occur at the
required directed prefix/suffix locations of four long PBBS arcs.  Nor
does it construct source antecedents, join the factor cycles, back up the
remaining `O(m^2)` upper casualties, or preserve the terminal common cap.

## 6. Dependencies and scope

Used:

1. `MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`;
2. `MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`;
3. `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`; and
4. `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`.

Not proved:

1. a directed four-arc placement inside one PBBS chronology;
2. depth-`d` source realization and residence;
3. connectedness of the completed two-factor;
4. simultaneous upper-backup and common-cap compatibility; or
5. any universal-word upper bound.
