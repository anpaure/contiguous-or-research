# Protected Ore deficiency is componentwise on the Johnson shore

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It proves that the
protected Ore--Ryser inequalities split exactly over the connected
components induced by a lower-shore family in the Johnson graph.  Hence a
failed cut always has a connected failed component.  It also gives a
finite connected-set entropy bound and specializes the zero-clique-defect
classification to one complete uniform layer on one support.  It does not
prove that the remaining connected cuts are safe.

## 0. Setting

Fix `m>=3`, and put

\[
 \mathcal L={{[2m-1]}\choose {m-1}},\qquad
 \mathcal U={{[2m-1]}\choose m}.
\]

Let `ML_m` be the incidence graph between these shores, and let `P` be a
protected subgraph of maximum degree at most two.  For
`A subseteq mathcal L`, retain the frozen notation

\[
 a_U=|N_{ML_m}(U)\cap A|,
 \qquad
 p_U=e_P(U,\mathcal L\setminus A),
\]

\[
 \sigma(A)=\sum_U\min\{2,a_U\}-2|A|,
\]

and

\[
 \lambda_P(A)
 =|\{U:a_U=1,\ p_U=2\}|+
   \sum_{U:a_U\ge2}p_U.
\tag{0.1}
\]

The protected bank extends to a spanning two-factor exactly when
`lambda_P(A)<=sigma(A)` for every `A`.

Let `J` be the Johnson graph on `mathcal L`: two lower vertices are
adjacent exactly when their intersection has rank `m-2`, or equivalently
when they are two facets of one owner `U in mathcal U`.  Its degree is

\[
                         \Delta=m(m-1).
\tag{0.2}
\]

## 1. Exact component decomposition

### Theorem 1.1

Let

\[
                         A=A_1\mathbin{\dot\cup}\cdots
                           \mathbin{\dot\cup}A_c
\tag{1.1}
\]

be the connected-component decomposition of the induced graph `J[A]`.
Then the upper shadows `N(A_i)` are pairwise disjoint, and

\[
 \boxed{
 \sigma(A)=\sum_{i=1}^c\sigma(A_i),
 \qquad
 \lambda_P(A)=\sum_{i=1}^c\lambda_P(A_i).}
\tag{1.2}
\]

The shadow surplus

\[
 s(A)=|N(A)|-|A|
\]

and the clique-closure defect

\[
 b(A)=\sum_{U:2\le a_U\le m-1}(m-a_U)
\]

split in the same way.

#### Proof

All lower facets of one owner `U` are pairwise adjacent in `J`.  Hence, if
`U` contains a member of `A_i` and a member of `A_j`, then those two lower
vertices are adjacent and `i=j`.  Thus the upper shadows `N(A_i)` are
pairwise disjoint.

Fix `U in N(A_i)`.  No lower facet of `U` belongs to any other `A_j`.
Consequently the number of its selected facets is the same whether it is
computed relative to `A` or relative to `A_i`.  More explicitly,

\[
 \mathcal L\setminus A_i=(\mathcal L\setminus A)
 \mathbin{\dot\cup}\bigcup_{j\ne i}A_j,
\]

but `U` has no neighbour in any `A_j`, `j\ne i`.  Hence

\[
 e_P(U,\mathcal L\setminus A_i)
 =e_P(U,\mathcal L\setminus A),
\]

which is the required equality of the two complement-defined values
`p_U`.  Owners outside `N(A_i)` have `a_U=0` and contribute zero to both
local functionals regardless of `p_U`.  Therefore the local summand of
both `sigma` and `lambda_P` belongs wholly to component `i`.
Summing over the disjoint upper shadows proves (1.2).  Cardinalities and
the defining local summands of `s` and `b` give their asserted
decompositions. \(\square\)

### Corollary 1.2 (connected-cut sufficiency)

The following are equivalent:

1. `P` extends to a spanning two-factor of `ML_m`;
2. `lambda_P(A)<=sigma(A)` for every Johnson-connected
   `A subseteq mathcal L`.

In particular, every failed cut contains a Johnson-connected component
which is itself failed.

#### Proof

Necessity is immediate.  Conversely, apply Theorem 1.1 to the component
decomposition of an arbitrary cut and add the valid component
inequalities.  If their sum fails, at least one summand fails. \(\square\)

This is stronger than merely taking a connected component of the
protected bank.  Connectivity is measured in the complete Johnson host
on the selected lower shore.

## 2. Connected equality cuts have one support

The frozen near-shadow theorem classifies `b(A)=0` cuts as

\[
 A=\mathop{\dot\bigcup}_j {{S_j}\choose {m-1}},
 \qquad |S_i\cap S_j|\le m-3\quad(i\ne j).
\tag{2.1}
\]

### Corollary 2.1

If `A` is Johnson-connected and `b(A)=0`, then for one support `S`

\[
                         \boxed{A={{S}\choose {m-1}}.}
\tag{2.2}
\]

Conversely every family in (2.2) is Johnson-connected when it is nonempty.

#### Proof

The separate families in (2.1) have no Johnson edge between them, by the
intersection bound.  Connectivity leaves exactly one nonempty support.
The Johnson graph on all `(m-1)`-subsets of one `S` is connected. \(\square\)

Thus, after Corollary 1.2, checking every zero-clique-defect cut requires
only the one-support families (2.2), not arbitrary separated unions.
The phrase *one support* is essential: unless `|S|<=m`, the graph induced
by `{{S}\choose {m-1}}` is a Johnson graph rather than a single complete
graph clique.

## 3. Connected-cut entropy

### Theorem 3.1

For every `t>=1`, the number `C_t` of Johnson-connected `t`-element
families `A subseteq mathcal L` satisfies

\[
 \boxed{
 C_t\le |\mathcal L|\,\Delta^{,2(t-1)}
 ={{2m-1}\choose {m-1}}
   \bigl(m(m-1)\bigr)^{2(t-1)}.}
\tag{3.1}
\]

#### Proof

Fix once and for all an order on the vertices and incident edges of `J`.
For a connected set `A`, choose its least vertex as root, its canonical
breadth-first spanning tree using those orders, and the canonical
depth-first traversal of that tree.  The traversal is a walk of length
`2(t-1)` in `J` and visits exactly the vertices of `A`.  Hence distinct
sets give different visited-vertex sets, so counting all possible roots
and all walks is an upper bound.  There are `|mathcal L|` roots and at most
`Delta` choices at every step, proving (3.1). \(\square\)

The deliberately crude square on `Delta` avoids importing any external
connected-set counting lemma.  Any sharper lattice-animal estimate may
replace (3.1) later.

### Corollary 3.2 (small-side entropy and the co-small split)

Assume `m>=4`, and let `e=|E(P)|`.  By the frozen near-shadow
localization theorem, if `P`
does not extend, then it has a Johnson-connected failed cut `A` satisfying

\[
 \min\{|A|,|\mathcal L\setminus A|\}
 <{m(m-1)\over2m-1},e.
\tag{3.2}
\]

On the small side, candidate connected sets of order `t` have logarithmic
entropy at most

\[
 \log|\mathcal L|+2(t-1)\log(m(m-1)).
\tag{3.3}
\]

Every connected zero-clique-defect candidate is already reduced to one
support `S` by Corollary 2.1.  Therefore a probabilistic cut-thinness proof
for the common-core reservoir needs concentration only against:

1. one-support complete uniform-layer families `{{S}\choose {m-1}}`;
2. small connected positive-`b` families of the entropy (3.3); and
3. co-small connected positive-`b` cuts, handled through the exact
   near-complete-clique complement normal form in Theorem 5.1 of the
   frozen near-shadow theorem.

No copy of (3.3) is asserted for the complement of a co-small connected
cut: `A` being Johnson-connected does not imply that
`\mathcal L\setminus A` is connected.  Without further structure the
trivial count for complements of size `t` is `{{|\mathcal L|}\choose t}`.

This corollary is a reduction, not the missing concentration theorem.

## 4. Dependencies and scope

The only inputs are the exact protected Ore--Ryser identities and the
near-shadow cardinality localization in
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`, final
SHA
`c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0`.

No assertion about residence, upper witnesses, component fusion, or the
common cap is made here.
