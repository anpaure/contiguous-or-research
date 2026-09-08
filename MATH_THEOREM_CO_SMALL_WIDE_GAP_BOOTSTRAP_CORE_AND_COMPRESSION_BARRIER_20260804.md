# Wide forced gaps, optional bootstrap cores, and the exact compression barrier

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  It
strengthens the base-safe q1 construction by forbidding a subexponential
rank window rather than three fixed ranks.  Every residual optional owner
gap then has width at least `d-2`.  Combined with the exact optional-DM
lattice, any positive canonical optional obstruction is forced to be a
three-supported high-aperture bootstrap core with minimum Johnson degree
at least `3(d-4)`.  The note also gives the exact one-exchange formula
which explains why ordinary coordinate compression is not yet available:
it requires threshold-majorization in the occurrence-labelled protected
gap hypergraph.

No computation, search, or solver result is used.

## 0. Setup

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],
 \qquad |K|=m-1,
 \qquad |E|=m,
\]

and the hybrid clipped-resident common-core reservoir.  Assume

\[
 d=d(m)=O(\sqrt m),
 \qquad d\longrightarrow\infty.
\tag{0.1}
\]

Let `P` be its incidence lift, let

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},
 \qquad X=\mathcal L\setminus Z,
\]

and, for an owner `U`, put

\[
 h(U)=|U\cap K|,
 \quad
 G_U=N(U)\cap X,
 \quad
 g_U=|G_U|,
 \quad
 c_U=2-d_P(U).
\tag{0.2}
\]

## 1. A depth-wide forbidden lower bank

Define

\[
 \mathcal F_{<d}
 =\{L\in\mathcal L:L\subset U
       \text{ for some }U\in\mathcal U
       \text{ with }h(U)<d\}.
\tag{1.1}
\]

### Lemma 1.1 (subexponential size)

One has

\[
 \boxed{
 |\mathcal F_{<d}|
 \le m\sum_{h=0}^{d-1}
       \binom{m-1}{h}\binom mh
 =2^{o(m)}.}
\tag{1.2}
\]

#### Proof

An owner with `h` coordinates in `K` has `m-h` coordinates in `E`, so
there are

\[
 \binom{m-1}h\binom m{m-h}
 =\binom{m-1}h\binom mh
\]

such owners.  Each has `m` lower facets.  This proves the first bound.
For `h<=d=O(sqrt m)`, the elementary estimate

\[
 \binom mh\le (em/h)^h
\]

makes the logarithm of the right side `O(d log m)=o(m)`. \(\square\)

### Theorem 1.2 (depth-wide q1 avoidance)

For all sufficiently large `m`, the hybrid constant-spread reservoir may
be selected with all its previously proved properties and with

\[
 \boxed{Z\cap\mathcal F_{<d}\subseteq Z_{\rm top},}
\tag{1.3}
\]

where `Z_top` is the deterministic cyclic-interval top palette.

#### Proof

A lower facet of an owner `U` with `h(U)<d` has external trace of size at
least

\[
 (m-h(U))-1\ge m-d.
\tag{1.4}
\]

Every shortened low noninterval path has exact external trace of size at
most `m-d-1`.  Hence none of its lower colours lies in
`mathcal F_<d`.

Add `mathcal F_<d` to the forbidden lower-resource bank for the high
monotone-geodesic greedy packing.  Lemma 1.1 enlarges that bank by only
`2^{o(m)}` resources.  The frozen high-packing proof already tolerates an
adaptive forbidden bank of size `2^{m+o(m)}` against resource supply
`2^{2m-o(m)}`.  Thus the same union bound remains strictly below one.
All owner, lower-colour, upper-colour, residence, and constant-spread
properties survive. \(\square\)

## 2. Uniform optional-gap aperture

We need one elementary cyclic fact.

### Lemma 2.1 (one-point cyclic completion)

Let `S` be a proper subset of a cyclically ordered `m`-set, with
`2<=|S|<=m-1`.  There are at most two elements `e in S` for which
`S setminus {e}` is a cyclic interval.

#### Proof

Put `H=E setminus S`, which is nonempty.  The complement of a nonempty
proper cyclic interval is a cyclic interval.  Thus `S setminus {e}` is a
cyclic interval exactly when `H union {e}` is one.  If `H` is itself an
interval, only its two cyclic neighbours can be adjoined.  If `H` is not
an interval, at most one coordinate can fill its unique gap and make it
an interval.  Hence there are at most two choices. \(\square\)

### Theorem 2.2 (uniform wide-gap theorem)

The refined reservoir satisfies

\[
 \boxed{g_U\ge d-2\qquad(U\in\mathcal U).}
\tag{2.1}
\]

In particular its forced-bank base condition holds with growing slack.

#### Proof

Fix `U`, put `S=U cap E`, and write `h=h(U)`.

Suppose first that `h<d`.  By Theorem 1.2, only top-path lower colours can
be protected facets of `U`.  A facet obtained by deleting a `K`
coordinate has exact external trace `S`; the simple top palette contains
at most one such lower colour.  A facet obtained by deleting
`e in S` has trace `S setminus {e}`.  Lemma 2.1 allows at most two such
top colours.  At `h=0`, the possible trace sizes are `m` and `m-1`, while
top lower colours have trace sizes at most `m-2`, so there are none.
Thus in every case

\[
 |N(U)\cap Z|\le3,
 \qquad
 g_U\ge m-3\ge d-2
\tag{2.2}
\]

for all sufficiently large `m`.

Now suppose `h>=d`.  Deleting an external coordinate gives a different
trace `S-e`, so at most `m-h` such facets can be protected.  All facets
obtained by deleting a `K` coordinate have trace `S`.  Exact trace assigns
them to one path, and the same-trace adjacency lemma allows at most two
of them.  Hence

\[
 |N(U)\cap Z|\le m-h+2,
 \qquad
 g_U\ge h-2\ge d-2.
\]

This proves (2.1). \(\square\)

## 3. The threshold hypergraph of an optional obstruction

For `B subseteq X`, put

\[
 b_U(B)=|B\cap G_U|,
 \qquad
 s_U=g_U-c_U,
\]

and define

\[
 \Psi(B)=
 \sum_U(b_U(B)-s_U)_+-2|B|.
\tag{3.1}
\]

The exact optional-complement theorem identifies `max Psi` with the full
residual factor deficiency.  Let `B^-` and `B^+` be respectively the
unique inclusion-minimal and inclusion-maximal maximizers of `Psi`.

Call an owner **overflowing at `x in B`** when

\[
 x\in G_U,
 \qquad b_U(B)\ge s_U+1,
\tag{3.2}
\]

and **threshold-ready at `y notin B`** when

\[
 y\in G_U,
 \qquad b_U(B)\ge s_U.
\tag{3.3}
\]

### Theorem 3.1 (three-supported wide-gap core)

If the residual deficiency is positive, every `x in B^-` belongs to at
least three overflowing owners.  Moreover,

\[
 \boxed{
 d_{J(2m-1,m-1)[B^-]}(x)\ge3(d-4)
 \qquad(x\in B^-).}
\tag{3.4}
\]

Consequently

\[
 \boxed{|B^-|\ge3d-11.}
\tag{3.5}
\]

At the opposite extremum, every `y in X setminus B^+` belongs to at most
one threshold-ready owner.  Equivalently, `B^+` is closed under the rule

> insert every optional lower vertex which sees two threshold-ready owner
> gaps.

#### Proof

The optional-DM one-point identities give at least three overflowing
owners through each member of `B^-`, and at most one threshold-ready
owner through each vertex outside `B^+`.

Fix `x in B^-` and one of its overflowing owners `U`.  Since `c_U<=2`,

\[
 b_U(B^-)
 \ge g_U-c_U+1
 \ge g_U-1.
\]

Besides `x`, this supplies at least `g_U-2>=d-4` members of `B^-` which
are other facets of `U`; each is a Johnson neighbour of `x`.  For fixed
`x`, different owners over `x` produce disjoint sets of Johnson
neighbours, because the owner containing an adjacent pair `x,y` is
uniquely `x union y`.  Three overflowing owners and Theorem 2.2 therefore
give (3.4).  The minimum-degree bound implies (3.5).  The closure statement
is just the maximal-bank threshold condition in words. \(\square\)

Thus a remaining positive optional obstruction is not an arbitrary small
family.  It is a growing-aperture, internally dense bootstrap core in the
optional Johnson graph, together with its two-threshold closed hull.

There is a more geometric version which interfaces directly with the
already-closed two-sided-subcube class.

### Corollary 3.2 (trihedral subcube bouquet at every core vertex)

For every `x in B^-`, there are three distinct owners
`U_1,U_2,U_3 superset x` and three two-sided Boolean intervals

\[
 \mathcal Q_i
 =\{L\in\mathcal L:C_i\subseteq L\subseteq U_i\}
 \subseteq B^-
\tag{3.6}
\]

such that

\[
 \boxed{|\mathcal Q_i|\ge d-3,}
\tag{3.7}
\]

every `mathcal Q_i` contains `x`, and

\[
 \boxed{\mathcal Q_i\cap\mathcal Q_j=\{x\}
 \qquad(i\ne j).}
\tag{3.8}
\]

#### Proof

Choose three overflowing owners through `x`.  For one such owner `U`, let

\[
 R_U=\{a\in U:U\setminus\{a\}\in B^-\cap G_U\},
 \qquad C_U=U\setminus R_U.
\]

Then

\[
 \{L:C_U\subseteq L\subseteq U,\ |L|=m-1\}
 =\{U-a:a\in R_U\}
 \subseteq B^-.
\]

Its size is `b_U>=g_U-1>=d-3`, and it contains `x`.  Two distinct owners
over `x` intersect exactly in `x`, which already has rank `m-1`; hence
their rank-`m-1` facet families have no other common member.  This proves
(3.6)--(3.8). \(\square\)

Each petal of this bouquet is individually inside the proved safe
two-sided-subcube class.  Therefore a positive obstruction, if it exists,
is necessarily created by the global gluing of these petals, not by any
one local aperture.

The full block irreducibility gives still more than the bouquet.

### Theorem 3.3 (strict internal overflow Hall core)

For the minimal maximizer `B^-`, give owner `U` its current overflow
capacity

\[
 a_U=(b_U(B^-)-(g_U-c_U))_+\in\{0,1,2\}.
\tag{3.9}
\]

Then every nonempty `D subseteq B^-` satisfies

\[
 \boxed{
 \sum_U\min\{a_U,|D\cap G_U|\}>2|D|.}
\tag{3.10}
\]

Consequently the incidence graph between `B^-` and the positive-capacity
owners has an integral `b`-matching of lower degree two and owner degree
at most `a_U`.  This remains true after deleting any one owner-capacity
unit.

Moreover, after discarding zero-capacity owners, this incidence graph is
`C_4`-free, has lower minimum degree at least three, and every positive
owner has at least `d-3` neighbours in `B^-`.

#### Proof

For one owner, put `b=b_U(B^-)`, `s=g_U-c_U`, and
`e=|D cap G_U|`.  Since `0<=e<=b`,

\[
 (b-s)_+-(b-e-s)_+=\min\{e,(b-s)_+\}
 =\min\{e,a_U\}.
\tag{3.11}
\]

Inclusion-minimality of `B^-` says

\[
 \Psi(B^-)>\Psi(B^-\setminus D)
\]

for every nonempty `D`.  Substitute (3.11); the modular term contributes
`2|D|`, proving (3.10).

The left side of (3.10) is exactly the capacitated neighbourhood supply
of `D`.  Bipartite capacitated Hall and integrality give the claimed
`b`-matching.  Since every quantity in (3.10) is integral, its strict
margin is at least one.  Deleting any single capacity unit lowers every
cut supply by at most one, so the matching remains feasible.

The lower minimum degree is Theorem 3.1.  If `a_U>0`, then
`b_U>=g_U-c_U+1>=g_U-1>=d-3`.  Finally two distinct lower vertices have
at most one common rank-`m` owner, namely their union when they are
Johnson adjacent.  Thus the incidence graph has no `4`-cycle. \(\square\)

This is an exact combinatorial normal form for a surviving optional
obstruction: a one-token-robust, redundantly two-matchable, `C_4`-free
bouquet complex.  Proving that the trace-structured forced palette cannot
support such a localized complex would close the co-small gate.

The literal Boolean host already sharpens its minimum possible size.

### Corollary 3.4 (quadratic core and exclusion of counting equality)

Put

\[
 n=|B^-|,
 \qquad D=d-3.
\]

For all sufficiently large `m`,

\[
 \boxed{n\ge D(D-1)+3.}
\tag{3.12}
\]

#### Proof

Let `Q` be the number of owners with `a_U>0`.  Since `B^-` has positive
deficiency,

\[
 \sum_Ua_U=2n+\delta(P)>2n.
\]

Every `a_U<=2`, so

\[
 Q\ge n+1.
\tag{3.13}
\]

Every positive owner contains at least `D` members of `B^-`.  Two lower
vertices have at most one common owner, so counting co-owned unordered
pairs gives

\[
 Q\binom D2
 \le\sum_{U:a_U>0}\binom{b_U}2
 \le\binom n2.
\tag{3.14}
\]

Equations (3.13)--(3.14) imply

\[
 (n+1)D(D-1)\le n(n-1),
\]

and hence `n>=D(D-1)+2`.

It remains to exclude equality.  Suppose

\[
 n=D(D-1)+2.
\]

The two sides of (3.14) then differ by exactly one unordered pair at their
minimum values.  Therefore necessarily:

1. `Q=n+1`;
2. every positive owner has exactly `D` members of `B^-`; and
3. exactly one pair of members of `B^-` is not co-owned.

Delete one endpoint of that exceptional pair.  The remaining `n-1`
lower sets are pairwise Johnson adjacent, so the Johnson clique
classification puts them either in one rank-`m` top or over one common
rank-`m-2` core.

In the top case, every positive owner block contains at least `D-1`
members of this clique.  For `D>=4`, it contains at least three, and any
pair of them has the same literal-union owner.  Thus every positive owner
would be that one top owner, contradicting `Q=n+1`.

In the common-core star case, one rank-`m` owner contains at most two
members of the clique, plus at most the one deleted exceptional vertex.
Its positive-owner degree is therefore at most three, contradicting
`D>=4`.

Since `d to infinity`, eventually `D>=4`.  Equality is impossible, which
proves (3.12). \(\square\)

The first `+2` bound is sharp for abstract linear incidence systems up to
the one-pair residue.  The extra Boolean unit in (3.12) is the first place
where literal-union Johnson clique rigidity, rather than `C_4`-freeness
alone, enters quantitatively.

## 4. Exact exchange and compression barrier

For `x in B` and `y in X setminus B`, define

\[
 R_B(x)=
 |\{U\supset x:b_U(B)\ge s_U+1\}|,
\tag{4.1}
\]

and

\[
 T_{B-x}(y)=
 |\{U\supset y:b_U(B\setminus\{x\})\ge s_U\}|.
\tag{4.2}
\]

### Theorem 4.1 (exact optional exchange identity)

For `B'=B setminus {x} union {y}`,

\[
 \boxed{
 \Psi(B')-\Psi(B)=T_{B-x}(y)-R_B(x).}
\tag{4.3}
\]

#### Proof

Removing `x` lowers one owner overflow unit exactly in the rows counted by
`R_B(x)` and refunds the modular cost two.  Adding `y` creates one owner
overflow unit exactly in the rows counted by `T_(B-x)(y)` and charges the
modular cost two.  The two modular changes cancel, leaving (4.3).
\(\square\)

### Corollary 4.2 (threshold-majorization is the missing shift lemma)

Let `y` be an elementary downward coordinate shift of `x`.  Replacing
`x` by `y` preserves or improves the optional obstruction exactly when

\[
 \boxed{T_{B-x}(y)\ge R_B(x).}
\tag{4.4}
\]

Hence a compression theorem for optional exchanges in `Psi` is
equivalent to a threshold-majorization theorem for the
occurrence-labelled gap system.
Neither ordinary Boolean shadow compression nor the constant-spread
singleton estimates imply (4.4): they control aggregate protected loss,
whereas the two sides of (4.4) ask which specified owner gaps are within
one unit of saturation.

More precisely, choose a lexicographically minimal maximizer of `Psi` for
a fixed coordinate order.  Every downward inversion `x to y` in that
maximizer satisfies

\[
 \boxed{T_{B-x}(y)<R_B(x).}
\tag{4.5}
\]

Indeed (4.3) cannot be positive at a global maximizer, while equality
would produce a lexicographically smaller maximizer.  Thus any
nonshifted canonical obstruction contains a literal **locked inversion**:
the old vertex has strictly more overflowing owner gaps than its shifted
replacement has threshold-ready gaps.

This is the exact new obstruction to compressing the movable part of the
canonical complement.  It is necessary but not sufficient for routing
the complete complement into an already-closed shifted/colex class: the
forced palette `Z` must also be shift-compatible.  Explicitly,
`C=Z union B` is shifted only if every downward shifted image of a member
of `Z` lies in `Z union B`, in addition to the corresponding condition
for members of `B`.  A forced-palette inversion cannot be repaired by
exchanging its source out of `Z`; its shifted image must be added through
the larger optional DM lattice.  This is the optional-complement form of
the forced-element correction in the residual-DM theorem.

## 5. Sharpened remaining theorem

The optional co-small gate is now reduced to either of two genuinely
structural statements.

1. **No locked inversion plus forced closure:** choose the protected
   reservoir so that every optional downward inversion in a localized
   maximizer satisfies (4.4), and so that all downward images forced by
   `Z` occur in the same maximum-deficiency complement.  Then a
   lexicographically minimal complement is shifted and may be attacked by
   the existing shifted/Macaulay programme.
2. **No localized bootstrap core:** prove that the constant-spread trace
   geometry contains no positive `Psi`-maximizer satisfying simultaneously
   the minimum-degree condition (3.4), the three-overflow support rule,
   and the two-threshold exterior closure rule.

The wide-gap refinement rules out low-aperture optional obstructions, but
does not by itself exclude such a high-aperture core.  In particular no
claim is made that minimum Johnson degree `Omega(d)` forces a bounded DNF,
a subcube, or an initial-colex family.

## 6. Dependencies

| role | file | SHA-256 |
|---|---|---|
| hybrid clipped-resident reservoir | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| constant-spread selection and high adaptive packing | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| base-safe q1 construction and same-trace adjacency | `MATH_THEOREM_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_20260804.md` | `c17615960cf7a9ff551125d72b69849b97181b41e1cd234d8a3b58820d7faf7a` |
| optional charging/factor equivalence and optional-DM lattice | `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md` | `55da48ce87926da31b0d226c368d75f2f7edd8b76cfb7b746993d6eadc9b625f` |
