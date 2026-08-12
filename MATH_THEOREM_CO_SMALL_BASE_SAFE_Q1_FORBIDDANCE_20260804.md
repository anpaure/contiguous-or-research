# A base-safe q1 bank for every co-small forced complement

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical construction.  It
refines the constant-spread common-core reservoir by one polynomial
forbidden lower-colour bank.  In the resulting incidence lift, the forced
protected lower bank never fills a residual-capacity owner clique and can
almost fill an owner clique only when that owner is protected.  Hence the
base row of the co-small harmonic certificate closes exactly.

No computation, search, or solver result is used.

## 0. Setup

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],
 \qquad |K|=m-1,
 \qquad |E|=m,
\]

and the top, low, and high path architecture of the frozen hybrid resident
reservoir.  Assume

\[
 4\le d=O(\sqrt m).
\tag{0.1}
\]

This includes the actual asymptotic deadline regime.

For an owner `U`, write

\[
 h(U)=|U\cap K|.
\]

Define the polynomial lower-resource bank

\[
 \mathcal F_{\le2}
 =\{L\in\mathcal L:L\subset U
       \text{ for some }U\in\mathcal U\text{ with }h(U)\le2\}.
\tag{0.2}
\]

It has size at most

\[
 m\sum_{h=0}^2\binom{m-1}h\binom m{m-h}=O(m^5).
\tag{0.3}
\]

Retain the deterministic cyclic-interval top paths.  Require every
non-top path to avoid `mathcal F_(<=2)` in its immediate lower palette.

## 1. The extra forbiddance is feasible

### Theorem 1.1 (polynomial q1 avoidance)

For all sufficiently large `m`, the constant-spread clipped-resident
reservoir can be chosen with all its previous properties and with

\[
 \boxed{
 Z_P\cap\mathcal F_{\le2}
 \subseteq Z_{\rm top},}
\tag{1.1}
\]

where `Z_P` is the complete protected lower bank and `Z_top` is the lower
palette already used by the deterministic top paths.

#### Proof

Every member of `mathcal F_(<=2)` has external trace of size at least
`m-3`.  Under (0.1), no low noninterval path uses such a trace: its trace
size is at most `m-d-1<=m-5`.  Thus the random low-path choices are
unaffected.

Add `mathcal F_(<=2)` to the forbidden lower-resource bank in the high
monotone-geodesic greedy packing.  Its size is polynomial by (0.3), while
each high target has resource denominators `2^(2m-o(m))`.  The frozen union
bound already tolerates `2^(m+o(m))` forbidden resources, so this
polynomial enlargement leaves its failure probability strictly below one.

The spread-preserving high packing uses the same denominator and allows an
adaptive forbidden owner bank of size `2^(m+o(m))`; retaining the fixed
polynomial lower bank does not affect that argument.  Therefore owner,
lower-colour, and upper-colour disjointness, clipped residence, singleton
spread, and endpoint spread all survive. \(\square\)

## 2. Two lower colours in one owner

### Lemma 2.1 (same-trace adjacency)

On every non-top low sliding path or high monotone geodesic, if two
immediate lower colours of that path are both facets of one owner `U`,
then they are consecutive lower colours and `U` is their intervening path
owner.  In particular,

\[
 \boxed{
 \text{two same-trace protected lower facets of }U
 \Longrightarrow d_P(U)=2.}
\tag{2.1}
\]

#### Proof

For a low sliding path, the `K`-parts of its lower colours are consecutive
intervals of one fixed length `ell=m-|T|-1>=d>=4`.  Two such sets at
starting-distance `s` have union size

\[
 \ell+\min\{s,\ell\}.
\]

An owner with the same external trace has only `ell+1` `K`-coordinates.
Thus two lower colours can fit in that owner only when
`min(s,ell)<=1`, which for distinct starts forces `s=1`.  Their union is
then exactly the intervening owner.

For a high monotone geodesic, write its lower colours as

\[
 L_t=C\cup\{x_{t+2},\ldots,x_{q-1}\}
          \cup\{y_1,\ldots,y_t\}.
\]

The symmetric difference of `L_t,L_s` has size `2|s-t|`.  Two facets of
one owner differ by one exchange, so again `|s-t|=1`, and their union is
the intervening owner.  The two incidence edges are protected, proving
(2.1). \(\square\)

## 3. Forced-bank clique aperture

Let

\[
 Z_P=\{L:d_P(L)=2\},
 \qquad
 z_U=|N(U)\cap Z_P|,
 \qquad
 g_U=m-z_U.
\tag{3.1}
\]

### Theorem 3.1 (base-safe forced q1 bank)

The refined reservoir satisfies

\[
 \boxed{g_U\ge1\qquad(U\in\mathcal U),}
\tag{3.2}
\]

and

\[
 \boxed{g_U=1\Longrightarrow d_P(U)=2.}
\tag{3.3}
\]

Consequently

\[
 \boxed{\Omega_P(Z_P)=0.}
\tag{3.4}
\]

#### Proof

Fix an owner and put `S=U cap E`, `h=|U cap K|`.  Facets obtained by
deleting an external coordinate have pairwise different exact traces
`S-e`, so at most `|S|=m-h` of them can belong to `Z_P`.

Facets obtained by deleting a `K`-coordinate all have exact trace `S`.
There is only one path for that trace.  Two of its lower colours can be
facets of `U` only in the situation of Lemma 2.1; in all cases there are
at most two.  Hence

\[
 z_U\le m-h+2.
\tag{3.5}
\]

If `h>=4`, this gives `z_U<=m-2`.  If `h=3`, equality
`z_U=m-1` requires two same-trace facets, and Lemma 2.1 gives
`d_P(U)=2`; equality `z_U=m` is impossible.

It remains to consider `h<=2`.  By Theorem 1.1, only top-path lower
colours can then contribute.  Top lower colours have cyclic-interval
external traces of lengths `1,...,m-2`.  At `h=0`, the possible traces
`S` and `S-e` have lengths `m` and `m-1`, so none contributes.  At
`h=1,2`, at most one top colour has trace `S`.  Across all deletions `e`,
at most two have trace `S-e`: the complement of `S-e` must be a cyclic
interval of size two or three, and a fixed complement of size one or two
has at most two possible endpoint extensions.  Therefore

\[
 z_U\le3<m-1
\]

for all sufficiently large `m`.

Combining the three ranges proves (3.2)--(3.3).  These are stronger than
the two base conditions in the harmonic gap theorem, so (3.4) follows.
\(\square\)

## 4. Consequence and remaining row

For the refined constant-spread reservoir, the co-small exact criterion
now has no fixed-bank defect.  Every remaining complement is

\[
 C=Z_P\mathbin{\dot\cup}B,
\]

and can fail only through optional gap saturation:

\[
 \Omega_P(Z_P\cup B)>2|B|.
\]

Thus the base case `B=emptyset` is closed constructively.  The sole
co-small row left is to control the optional bank, for example by the
harmonic balance condition `Gamma_P(x)=2` or by a less rigid fractional
allocation of near-clique units.

## 5. Dependencies

| role | file | SHA-256 |
|---|---|---|
| hybrid clipped-resident reservoir and high greedy supply | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| constant-spread low randomization and high adaptive packing | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| co-small harmonic gap certificate | `MATH_THEOREM_CO_SMALL_FORCED_Q1_HARMONIC_GAP_CERTIFICATE_20260804.md` | `4a5d0993d7c3e2eb54198c2b6278670649308f7aeb3dd1de046b18742db0a85a` |
