# Protected Ore failures are near-tight upper-shadow cuts

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sharpening of the protected
Ore--Ryser criterion.  It gives an exact shadow-slack identity, classifies
all equality cases, gives an exact protected-degree form of every cut, and
localizes every failed cut both structurally and by cardinality.  Applied
to the common-core witness reservoir, it reduces factor extension to
small or co-small, nearly clique-closed cuts.  It does **not** prove that
the reservoir satisfies those remaining cuts.

## 0. Setting

Fix `m>=2`, and let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},\qquad
 W=|\mathcal L|=|\mathcal U|.
\]

Write `ML_m` for the `m`-regular containment graph between these shores.
Let `P subseteq ML_m` have maximum degree at most two.  For
`A subseteq mathcal L` and `U in mathcal U`, put

\[
 a_U=|N(U)\cap A|,\qquad
 p_U=e_P(U,\mathcal L\setminus A).
\tag{0.1}
\]

The exact protected Ore--Ryser criterion is

\[
 P\text{ extends to a spanning two-factor}
 \quad\Longleftrightarrow\quad
 \lambda_P(A)\le\sigma(A)\quad(A\subseteq\mathcal L),
\tag{0.2}
\]

where

\[
 \sigma(A)=\sum_U\min\{2,a_U\}-2|A|
\tag{0.3}
\]

and

\[
 \lambda_P(A)=
 |\{U:a_U=1,\ p_U=2\}|+
 \sum_{U:a_U\ge2}p_U.
\tag{0.4}
\]

These are the frozen identities from
`MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`.

For the rest of the note, write

\[
 N=N(A)=\{U:a_U>0\},\qquad
 s(A)=|N(A)|-|A|,
\tag{0.5}
\]

and

\[
 b(A)=\sum_{U:2\le a_U\le m-1}(m-a_U).
\tag{0.6}
\]

Regularity gives `s(A)>=0`.

## 1. Exact shadow-slack identity

### Theorem 1.1 (shadow surplus plus clique-closure defect)

For every `A subseteq mathcal L`,

\[
 \boxed{
 (m-1)\sigma(A)=(m-2)s(A)+b(A).}
\tag{1.1}
\]

Consequently,

\[
 \boxed{
 \sigma(A)\ge {m-2\over m-1}
 \bigl(|N(A)|-|A|\bigr).}
\tag{1.2}
\]

For `m>=3`, equality holds in (1.2) if and only if

\[
 \boxed{a_U\in\{0,1,m\}\quad\text{for every }U\in\mathcal U.}
\tag{1.3}
\]

For `m=2`, both sides of (1.2) are zero for every `A`.

#### Proof

Let

\[
 n_j=|\{U:a_U=j\}|,
 \qquad
 M_2=\sum_{j=2}^m n_j.
\]

Then

\[
 |N|=n_1+M_2,
 \qquad
 m|A|=n_1+\sum_{j=2}^m jn_j,
\tag{1.4}
\]

while

\[
 \sigma(A)=n_1+2M_2-2|A|=|N|+M_2-2|A|.
\tag{1.5}
\]

A direct subtraction now gives

\[
\begin{aligned}
 &(m-1)\sigma(A)-(m-2)(|N|-|A|)\\
 &\qquad=|N|+(m-1)M_2-m|A|\\
 &\qquad=\sum_{j=2}^{m-1}(m-j)n_j=b(A).
\end{aligned}
\tag{1.6}
\]

This proves (1.1).  Since `b(A)>=0`, it also proves (1.2).
For `m>=3`, equality is equivalent to `n_j=0` for every
`2<=j<=m-1`, which is exactly (1.3).  When `m=2`, the sum defining
`b(A)` is empty and `m-2=0`. \(\square\)

The exact identity also gives the congruence

\[
 \boxed{b(A)\equiv s(A)\pmod {m-1},}
\tag{1.7}
\]

because `m-2` is `-1` modulo `m-1`.

### Theorem 1.2 (classification of all equality cuts)

Assume `m>=3`, and put `k=m-1`.  Equality holds in (1.2) if and only if
there are subsets `S_i subseteq [2m-1]`, each of size at least `k`, such
that

\[
 \boxed{
 A=\mathop{\dot\bigcup}_i {S_i\choose k},
 \qquad
 |S_i\cap S_j|\le k-2=m-3\quad(i\ne j).}
\tag{1.8}
\]

The empty union and `S_1=[2m-1]` give `A=emptyset` and
`A=mathcal L`, respectively.

#### Proof

Join two rank-`k` sets when their union has size `k+1=m`; this is the
Johnson graph on `mathcal L`.  An upper vertex `U` indexes the maximal
clique `{U choose k}`.  Condition (1.3) says:

> whenever a Johnson clique contains two members of `A`, it contains all
> of its members.

Take a connected component `C` of the Johnson graph induced by `A`, and
put `S=union_(X in C) X`.  We show that `C={S choose k}`.

Start with one `X in C`.  Suppose that all `k`-subsets of a current support
`S_0` are already in `C`, and that the next vertex on a spanning-tree
exploration is adjacent to one of them.  If it is new, it has the form

\[
 Z=H\cup\{z\},\qquad |H|=k-1,\qquad H\subset S_0,
 \qquad z\notin S_0.
\]

We already know `H union {x} in A` for every `x in S_0\setminus H`.
Together with `H union {z}`, clique closure supplies all `k`-facets of
`H union {x,z}`.  Repeating this switch along the connected Johnson graph
on the `(k-1)`-subsets of `S_0` shows that

\[
 \{z\}\cup H'\in A
 \qquad\left(H'\in{S_0\choose k-1}\right).
\]

Thus all `k`-subsets of `S_0 union {z}` lie in the same component.
Induction proves `C={S choose k}`.

If two distinct component supports met in at least `k` points, their
complete `k`-graphs would share a vertex.  If they met in exactly `k-1`
points, choose that common `(k-1)`-set and one additional point from each
support; the resulting two vertices would be Johnson adjacent.  Hence
distinct supports meet in at most `k-2` points.

Conversely, suppose (1.8) holds.  If an upper clique contains two selected
facets, those facets are Johnson adjacent, so the intersection condition
forces them to belong to the same `S_i`.  Their union lies in `S_i`, and
therefore all `m` facets of that upper vertex belong to `{S_i choose k}`.
Every upper fibre consequently has size `0`, `1`, or `m`, proving equality
by Theorem 1.1. \(\square\)

Thus `b(A)` is an exact **clique-closure defect**: it vanishes precisely on
unions of separated complete Johnson subgraphs.

For an equality cut (1.8), put `t_i=|S_i|`.  Its shadow surplus is also
explicit:

\[
 \boxed{
 s(A)=\sum_i\left[
 {t_i\choose m}+(2m-2-t_i){t_i\choose m-1}
 \right].}
\tag{1.9}
\]

Indeed an upper neighbour of `{S_i choose m-1}` either lies wholly in
`S_i`, or consists of one outside coordinate and `m-1` coordinates of
`S_i`.  Upper shadows belonging to distinct components are disjoint,
because a shared upper vertex would contain one selected facet from each
component, and those facets would be Johnson adjacent.  Subtracting
`|{S_i choose m-1}|` gives (1.9).  Therefore the equality cuts surviving
any bound on `s(A)` are parametrized exactly by a separated support packing
and this one-dimensional binomial budget.

## 2. Exact protected crossing identity

Put `C=mathcal L\setminus A`, and define

\[
 c_P(A)=e_P(N(A),C)
       =\sum_{U:a_U\ge1}p_U,
\tag{2.1}
\]

and

\[
 \rho_P(A)=|\{U:a_U=1,\ p_U\ge1\}|.
\tag{2.2}
\]

For a set of vertices `X` on either shore, write

\[
 D_P(X)=\sum_{x\in X}d_P(x).
\tag{2.3}
\]

### Theorem 2.1 (crossing edges minus one-neighbour rebates)

For every lower cut `A`,

\[
 \boxed{
 \lambda_P(A)=c_P(A)-\rho_P(A).}
\tag{2.4}
\]

Moreover,

\[
 \boxed{
 c_P(A)=D_P(N(A))-D_P(A).}
\tag{2.5}
\]

Consequently `P` extends to a spanning two-factor if and only if, for
every `A subseteq mathcal L`,

\[
 \boxed{
 (m-1)\bigl(c_P(A)-\rho_P(A)\bigr)
 \le (m-2)s(A)+b(A).}
\tag{2.6}
\]

#### Proof

If `a_U=1`, then the contribution of `U` to `c_P-rho_P` is zero when
`p_U=0` or `1`, and is one when `p_U=2`.  If `a_U>=2`, its contribution is
`p_U`.  These are exactly the local terms in (0.4), proving (2.4).

Every protected edge incident with `A` has its upper endpoint in `N(A)`.
Hence subtracting the degree sum on `A` from the degree sum on `N(A)`
leaves exactly the protected edges from `N(A)` to `C`, proving (2.5).
Finally combine (2.4), Theorem 1.1, and (0.2). \(\square\)

The exact identity is sharper than `lambda_P(A)<=|E(P)|`.  Useful
consequences are

\[
\begin{aligned}
 \lambda_P(A)
 &\le c_P(A)\\
 &\le \min\{|E(P)|,D_P(C),D_P(N(A))\}\\
 &\le 2\min\{|C\cap V_{\mathcal L}(P)|,
              |N(A)\cap V_{\mathcal U}(P)|\}.
\end{aligned}
\tag{2.7}
\]

If `c_1` denotes the number of crossing protected edges at owners with
`a_U=1`, and `c_{>=2}` the number at owners with `a_U>=2`, then also

\[
 \boxed{
 \lambda_P(A)\le c_{\ge2}+{c_1\over2}.}
\tag{2.8}
\]

Indeed an `a_U=1` owner contributes only when both of its protected edges
cross, and then two crossing edges buy one unit of protected loss.

## 3. Exact localization of every failed cut

Call `A` **failed** if `lambda_P(A)>sigma(A)`.  Put

\[
 \ell_P(A)=c_P(A)-\rho_P(A)=\lambda_P(A).
\tag{3.1}
\]

### Theorem 3.1 (near-shadow localization)

Assume `m>=3`.  Every failed cut satisfies

\[
 \boxed{
 (m-2)s(A)+b(A)
 \le (m-1)\ell_P(A)-1.}
\tag{3.2}
\]

In particular,

\[
 \boxed{
 s(A)\le
 \left\lfloor{(m-1)\ell_P(A)-b(A)-1\over m-2}\right\rfloor
 =\ell_P(A)+
 \left\lfloor{\ell_P(A)-b(A)-1\over m-2}\right\rfloor,}
\tag{3.3}
\]

and

\[
 \boxed{
 b(A)\le (m-1)\ell_P(A)-1-(m-2)s(A).}
\tag{3.4}
\]

Thus the number of upper vertices with
`2<=a_U<=m-1` is at most the right side of (3.4).

If `e=|E(P)|`, then every failed cut lies in the global region

\[
 \boxed{
 s(A)\le e+\left\lfloor{e-1\over m-2}\right\rfloor,}
\tag{3.5}
\]

and has at most `(m-1)e-1` partially filled upper cliques.

#### Proof

Failure and the exact identities (1.1), (2.4) give

\[
 {(m-2)s+b\over m-1}<\ell_P(A).
\]

All quantities after clearing the denominator are integers, so this is
equivalent to (3.2).  Rearranging proves (3.3)--(3.4).  Every partial upper
clique contributes at least one to `b(A)`.  Finally use
`ell_P(A)<=|E(P)|` and discard `b(A)>=0` to obtain (3.5). \(\square\)

This theorem is an exact fail-closed reduction: cuts outside (3.2) cannot
obstruct extension.

### Corollary 3.2 (small complements are automatically safe)

Every cut with

\[
 |\mathcal L\setminus A|\le m-2
\tag{3.6}
\]

is safe for every `P` of maximum degree at most two.

For every nonempty failed cut one therefore has

\[
 |\mathcal L\setminus A|\ge m-1,
 \qquad s(A)\ge m-1,
 \qquad \ell_P(A)\ge m-1.
\tag{3.7}
\]

#### Proof

Put `C=mathcal L\setminus A` and suppose `|C|<=m-2`.  No upper vertex can
have more than `m-2` lower facets in `C`; hence every upper vertex has at
least two facets in `A`.  Therefore `N(A)=mathcal U` and

\[
 \sigma(A)=2W-2|A|=2|C|.
\]

On the other hand, every term counted by `lambda_P(A)` is paid by a
protected edge ending in `C`, so

\[
 \lambda_P(A)\le D_P(C)\le2|C|.
\]

Thus the cut is safe.  For a nonempty `A` with complement at least `m-1`,
the sharp middle-shadow bound gives `s(A)>=m-1`.  Theorem 1.1 then gives
`sigma(A)>=m-2`; since `lambda_P(A)` is an integer strictly larger than
`sigma(A)` on a failed cut, `ell_P(A)=lambda_P(A)>=m-1`. \(\square\)

### Corollary 3.3 (the first edge-count boundary)

If `|E(P)|<=m-2`, then `P` extends to a spanning two-factor.

If `|E(P)|=m-1` and a failed cut exists, then necessarily

\[
 \boxed{
 \lambda_P(A)=m-1,\qquad
 \sigma(A)=m-2,\qquad
 s(A)=m-1,\qquad b(A)=0.}
\tag{3.8}
\]

In particular the cut must be one of the clique-closed families classified
by Theorem 1.2.

#### Proof

On a failed cut, Corollary 3.2 gives
`lambda_P(A)>=m-1`, while `lambda_P(A)<=|E(P)|`.  This proves the first
claim.  If `|E(P)|=m-1`, then failure forces
`lambda_P(A)=m-1` and `sigma(A)<=m-2`.  Corollary 3.2 gives the reverse
inequality.  Equality in Theorem 1.1 now forces `s=m-1` and `b=0`.
\(\square\)

## 4. Cardinality localization

The preceding reduction controls shadow surplus directly.  It also puts
every failed cut close in cardinality to one of the two trivial cuts.

Let `J=J(2m-1,m-1)` be the Johnson graph on `mathcal L`, and let
`partial_J A` be its undirected edge boundary.  Each Johnson edge has a
unique upper owner, so

\[
 |\partial_J A|=\sum_U a_U(m-a_U).
\tag{4.1}
\]

### Lemma 4.1 (weighted boundary dominates Johnson boundary)

For `m>=4`,

\[
 \boxed{
 \sigma(A)\ge {2\over m(m-1)}|\partial_J A|.}
\tag{4.2}
\]

#### Proof

The local weight in the frozen weighted-boundary formula is

\[
 h_m(1)={m-2\over m},\qquad
 h_m(a)={2(m-a)\over m}\quad(2\le a\le m-1).
\]

For `a=1`, one has

\[
 {m-2\over m}\ge {2\over m(m-1)}(m-1)
\]

exactly when `m>=4`.  For `2<=a<=m-1`,

\[
 {2(m-a)\over m}\ge
 {2\over m(m-1)}a(m-a)
\]

because `a<=m-1`.  Sum these inequalities over `U`. \(\square\)

The Johnson graph has degree `m(m-1)` and Laplacian gap `2m-1`.  One quick
derivation is to let `B` be the inclusion matrix between ranks `m-1` and
`m`.  Then

\[
 BB^T=mI+A_J,
\]

and the standard up--down decomposition of the Boolean lattice gives
eigenvalues `(m-i)^2`, `0<=i<=m-1`, for `BB^T`.  Thus the two largest
adjacency eigenvalues are `m(m-1)` and `(m-1)^2-m`, whose difference is
`2m-1`.  Applying the Laplacian inequality to the indicator of `A` gives

\[
 |\partial_J A|
 \ge (2m-1)|A|\left(1-{|A|\over W}\right).
\tag{4.3}
\]

### Theorem 4.2 (small/co-small localization)

Let `m>=4` and `e=|E(P)|`.  If `A` is failed, then

\[
 \boxed{
 {|A|(W-|A|)\over W}
 <{m(m-1)\over2(2m-1)}\ell_P(A)
 \le {m(m-1)\over2(2m-1)}e.}
\tag{4.4}
\]

Consequently,

\[
 \boxed{
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}\ell_P(A)
 \le {m(m-1)\over2m-1}e.}
\tag{4.5}
\]

If

\[
 {m(m-1)\over2(2m-1)}\ell_P(A)\le {W\over4},
\]

the sharper quadratic form is

\[
 \min\{|A|,W-|A|\}<
 {W-\sqrt{W^2-
  2m(m-1)\ell_P(A)W/(2m-1)}\over2}.
\tag{4.6}
\]

#### Proof

On a failed cut,

\[
 \sigma(A)<\lambda_P(A)=\ell_P(A)\le e.
\]

Combine this with (4.2)--(4.3) to obtain (4.4).  If
`t=min{|A|,W-|A|}`, then

\[
 {|A|(W-|A|)\over W}={t(W-t)\over W}\ge {t\over2},
\]

which gives (4.5).  Solving the cut-sensitive quadratic inequality gives
(4.6).
\(\square\)

There is also an exact Kruskal--Katona version.  Let `partial_m(a)` be the
minimum lower-shadow size of an `a`-member family of `m`-sets on
`[2m-1]`.  Complementation gives

\[
 s(A)\ge\partial_m(|A|)-|A|.
\tag{4.7}
\]

Thus a failed cut must satisfy

\[
 \boxed{
 \partial_m(|A|)-|A|
 \le e+\left\lfloor{e-1\over m-2}\right\rfloor.}
\tag{4.8}
\]

This is often sharper than (4.5), and it is an exact finite restriction on
the possible cut cardinalities through the canonical binomial expansion.

## 5. Exact co-small normal form

The co-small side admits a particularly sharp description.  Put

\[
 C=\mathcal L\setminus A,
 \qquad
 d_U=|N(U)\cap C|=m-a_U.
\]

Define

\[
 \theta(C)=|\{U:d_U=m-1\}|+2|\{U:d_U=m\}|,
\tag{5.1}
\]

\[
 \operatorname{def}_P(C)=2|C|-D_P(C),
\tag{5.2}
\]

and

\[
 R_P(C)=
 \sum_{U:d_U=m}p_U+
 \sum_{U:d_U=m-1}\min\{p_U,1\}.
\tag{5.3}
\]

Here `p_U=e_P(U,C)`.

### Theorem 5.1 (near-complete-clique obstruction)

For every `C subseteq mathcal L`, with `A=mathcal L\setminus C`,

\[
 \boxed{
 \sigma(A)=2|C|-\theta(C),}
\tag{5.4}
\]

and

\[
 \boxed{
 \lambda_P(A)=D_P(C)-R_P(C).}
\tag{5.5}
\]

Therefore the co-small cut fails if and only if

\[
 \boxed{
 \theta(C)>\operatorname{def}_P(C)+R_P(C).}
\tag{5.6}
\]

In particular, a co-small cut is automatically safe unless `C` contains
all but at most one facet of some upper vertex.

#### Proof

The regularity identity `sum_U d_U=m|C|` gives the baseline
`sum_U 2d_U/m=2|C|`.  In the weighted-boundary formula for `A`, this
baseline is exact for `0<=d_U<=m-2`.  At `d_U=m-1`, the actual weight is
`h_m(1)=(m-2)/m`, one less than the baseline `2(m-1)/m`.  At `d_U=m`,
the actual weight is zero, two less than the baseline.  This proves (5.4).

The degree sum `D_P(C)=sum_U p_U` is the protected loss at owners with
`d_U<=m-2`, because then `a_U>=2`.  At `d_U=m`, the true loss is zero, so
all `p_U` units are rebated.  At `d_U=m-1`, the true loss is zero for
`p_U=0,1` and one for `p_U=2`; relative to the baseline `p_U`, this rebates
`min{p_U,1}`.  This proves (5.5).  Substituting
`D_P(C)=2|C|-operatorname{def}_P(C)` and comparing (5.4)--(5.5) gives
(5.6). \(\square\)

Equation (5.6) is stronger than a generic size cutoff.  It says that the
only dangerous co-small cuts are built around almost-complete Johnson
cliques, and it prices those cliques against both missing protected degree
and an exact local rebate.

## 6. Consequence for the common-core witness reservoir

Let `P_D` be the reservoir of
`MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md`.
Its frozen size bound is

\[
 e_D=|E(P_D)|<2(m-2)(m+2^m)=o(W/m).
\tag{6.1}
\]

The strengthening from the frozen `o(W)` statement to `o(W/m)` follows
directly from `W asymp 4^m/sqrt m`: after multiplication by `m/W`, the
displayed upper bound is `O(m^(5/2)/2^m)`.

Theorem 4.2 implies that every failed protected Ore cut for this reservoir
must satisfy

\[
 \boxed{
 \min\{|A|,W-|A|\}
 <{2m(m-1)(m-2)\over2m-1}(m+2^m)
 =O(m^2 2^m)=o(W).}
\tag{6.2}
\]

Theorem 3.1 additionally says that such a cut has upper-shadow surplus
`O(e_D)` and only `O(me_D)` partially filled Johnson cliques.  If the
small side is the complement `C`, Theorem 5.1 says that `C` must contain
all but at most one facet of an upper vertex and must violate the exact
degree/rebate inequality (5.6).  If `b(A)=0`, Theorem 1.2 classifies the
cut completely as a union of separated complete Johnson subgraphs.

Thus the all-cut extension problem has been reduced from arbitrary subsets
of the `W`-vertex shore to the following proof-safe residual family:

1. small or co-small cuts of size `O(m^2 2^m)`;
2. upper-shadow surplus `O(m2^m)`;
3. at most `O(m^2 2^m)` partially filled upper cliques;
4. on the co-small side, a near-complete upper-clique core satisfying the
   exact failure inequality (5.6).

This is a genuine asymptotic and structural localization.  It is not by
itself an extension proof.  Singleton cuts already have `b(A)=0`, and the
frozen one-cone counterexample shows that a protected bank can concentrate
on such an equality cut.  A balanced construction of `P_D`, or a direct
verification of (2.6) on the residual family above, is still required.

## 7. Dependencies and scope

The exact protected Ore--Ryser criterion and weighted-boundary formula are
from:

* `MATH_OBSTRUCTION_UPPER_CONE_WITNESS_BANK_PROTECTED_FACTOR_EXTENSION_20260804.md`;
* `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`.

The sharp coarse middle-shadow bound used in Corollary 3.2 is from
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.
The only other standard input is the Johnson spectrum in Section 4.

No claim is made here about residence, component distribution, the common
cap, or the existence of a balanced placement of the common-core reservoir.
