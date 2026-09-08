# Exact protected Ore ledger for two-sided Boolean subcubes

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical identity, reduction, and
quantitative sufficient theorem.  It
computes the exact truncated-shadow slack, clique-closure defect, and
protected loss for every two-sided Boolean interval on the lower
Middle-Levels shore.  These families interpolate between the already
closed complete-support families and principal up-stars.  It also closes
an explicit two-boundary range for the constant-spread reservoir.  No
assertion that every such positive-defect family is safe is made here.

## 0. Setting

Put

\[
 n=2m-1,\qquad k=m-1,
 \qquad \mathcal L={{[n]}\choose k},
 \qquad \mathcal U={{[n]}\choose m}.
\]

Let `P subseteq ML_m` have maximum degree at most two.  Choose sets

\[
                         C\subseteq S\subseteq[n],
\]

with

\[
 0\le c:=|C|\le m-2,
 \qquad s:=|S|\ge m-1.
\]

Write

\[
 u=n-s,
 \qquad r=k-c=m-1-c,
 \qquad v=s-c.
\tag{0.1}
\]

The associated two-sided subcube on the lower shore is

\[
 \mathcal A(C,S)
 =\{L\in\mathcal L:C\subseteq L\subseteq S\}.
\tag{0.2}
\]

It has order

\[
                         a=|\mathcal A(C,S)|={v\choose r}.
\tag{0.3}
\]

The endpoint `C=emptyset` is the complete-support family
`binom(S,m-1)`.  The endpoint `S=[n]` is the principal up-star of `C`.

## 1. Exact owner fibres

### Lemma 1.1

For an owner `U in mathcal U`, the number

\[
 a_U=|\{L\in\mathcal A(C,S):L\subset U\}|
\]

is nonzero in exactly two cases:

1. if `C subseteq U subseteq S`, then
   \[
                            a_U=m-c=r+1;
   \tag{1.1}
   \]
2. if `U=F union {z}` for a unique `F in mathcal A(C,S)` and
   `z notin S`, then `a_U=1`.

All other owners have `a_U=0`.  Consequently

\[
 |N(\mathcal A(C,S))|
 ={v\choose {r+1}}+u{v\choose r}.
\tag{1.2}
\]

#### Proof

Any selected facet contains `C` and lies in `S`, so an owner meeting the
family contains `C` and has at most one coordinate outside `S`.  If it has
none, deleting any of its `m-c=r+1` coordinates outside `C` gives a
selected facet, while deleting a coordinate of `C` does not.  If it has
one outside coordinate `z`, only deletion of `z` gives a selected facet.
This proves both cases and the count. \(\square\)

## 2. Exact shadow slack and positive defect

### Theorem 2.1

The protected Ore capacity of the two-sided subcube is

\[
 \boxed{
 \sigma(\mathcal A(C,S))
 =2{v\choose {r+1}}+(u-2){v\choose r}.}
\tag{2.1}
\]

Equivalently,

\[
 \boxed{
 {\sigma(\mathcal A(C,S))\over|\mathcal A(C,S)|}
 =u-2+{2(m-u)\over m-c}.}
\tag{2.2}
\]

Its clique-closure defect is

\[
 \boxed{
 b(\mathcal A(C,S))
 =c{v\choose {r+1}}.}
\tag{2.3}
\]

#### Proof

Since `r+1=m-c>=2`, every internal owner in Lemma 1.1 contributes two to
the truncated shadow and every outside owner contributes one.  Hence

\[
 S_2=2{v\choose {r+1}}+u{v\choose r}.
\]

Subtracting `2a` proves (2.1).  The binomial ratio is

\[
 {{v\choose {r+1}}\over {v\choose r}}
 ={v-r\over r+1}={m-u\over m-c},
\]

which proves (2.2).

An internal owner has fibre size `m-c`.  It contributes
`m-(m-c)=c` to `b` when `c>0`; for `c=0` that contribution is zero as
well.  The outside owners have fibre size one and do not enter `b`.
This proves (2.3). \(\square\)

The endpoint checks are exact.  If `c=0`, (2.2) becomes

\[
                         {u(m-2)\over m},
\]

the complete-support equality-cut slack.  If `u=0`, it becomes

\[
                         {2c\over m-c},
\]

the principal-star slack.

## 3. Exact protected-loss decomposition

Define the internal owner bank

\[
 \mathcal U_{C,S}^{\rm in}
 =\{U\in\mathcal U:C\subseteq U\subseteq S\}
\]

and the outside boundary bank

\[
 \mathcal U_{C,S}^{\rm out}
 =\{F\cup\{z\}:F\in\mathcal A(C,S),\ z\notin S\}.
\]

For an incidence `UL in P`, write `del(U,L)` for the unique coordinate in
`U setminus L`.  Put

\[
 \xi_P(C,S)
 =|\{UL\in E(P):U\in\mathcal U_{C,S}^{\rm in},
                    \ \operatorname{del}(U,L)\in C\}|,
\tag{3.1}
\]

and

\[
 \theta_P(C,S)
 =|\{U=F+z\in\mathcal U_{C,S}^{\rm out}:
          d_P(U)=2,\ UF\notin E(P)\}|.
\tag{3.2}
\]

### Theorem 3.1 (core exits plus support-boundary misses)

For every protected bank `P` of maximum degree at most two,

\[
 \boxed{
 \lambda_P(\mathcal A(C,S))
 =\xi_P(C,S)+\theta_P(C,S).}
\tag{3.3}
\]

#### Proof

An internal owner has at least two selected facets, so its local protected
loss is the number `p_U` of protected incidences to unselected facets.
For `U in mathcal U_(C,S)^in`, a facet `L=U-z` remains inside `S` and
fails to contain `C` exactly when `z in C`.  Summing these incidences gives
`xi_P(C,S)`.

An outside owner has exactly one selected facet `F`.  Its local loss is
one precisely when both protected incidences enter from outside the cut,
equivalently when it has protected degree two and the incidence `UF` is
not protected.  These owners are counted by `theta_P(C,S)`.  All other
owners have no selected facet and contribute zero. \(\square\)

At `S=[n]`, the boundary term vanishes and (3.3) is the principal-star
crossing-current identity.  At `C=emptyset`, the internal term vanishes
and (3.3) is the complete-support boundary-owner identity.

## 4. Path interpretation

Suppose `P` is the incidence lift of a family of simple Johnson owner
paths.  For one path, the owners containing `C` and lying in `S` form some
set of path positions.  Every path edge leaving or entering the owner-star
`{U:C subseteq U}` through deletion of a coordinate of `C` contributes
exactly one unit to `xi_P(C,S)`, provided its inside endpoint also lies in
`S`.

The additional upper restriction does **not** increase this core-exit
current.  This corrects the first draft's misleading split-interval
paragraph.

### Lemma 4.1 (two crossings still suffice for the core current)

Assume that every coordinate has an interval of positive owner occurrences
along each protected path.  Let `mathscr P(C)` be the set of protected
paths containing at least one owner which contains `C`.  Then

\[
 \boxed{
 \xi_P(C,S)\le2|\mathscr P(C)|.}
\tag{4.1}
\]

#### Proof

On one path, the positions whose owners contain all of `C` are an
intersection of intervals, hence one interval `I`.  An incidence counted
by `xi_P(C,S)` lies at an owner in `I` and deletes a coordinate of `C`.
The owner at the other end of that Johnson edge consequently lies outside
`I`.  Thus the edge is one of the at most two boundary edges of `I`.
Requiring the inside owner also to lie in `S` can delete a contribution,
but cannot create another boundary edge of `I`.  Sum over paths.
\(\square\)

For the common-core reservoir, put

\[
 \rho=m-c,
 \qquad H_\rho(m)=\sum_{j=0}^{\rho}{m\choose j}.
\tag{4.2}
\]

The same trace count as in the frozen principal-star proof gives

\[
 |\mathscr P(C)|\le H_\rho(m)+m+H_d,
\tag{4.3}
\]

where `m` counts the top paths and `H_d=2^{o(m)}` bounds the resident high
tail.

For a lower vertex `F`, write `ell_P(F)=lambda_P({F})`.

### Lemma 4.2 (the support boundary is paid by singleton load)

For every protected bank,

\[
 \boxed{
 \theta_P(C,S)\le
 \sum_{F\in\mathcal A(C,S)}\min\{\ell_P(F),u\}.}
\tag{4.4}
\]

#### Proof

Every owner counted by `theta_P(C,S)` has the unique selected facet `F`,
has protected degree two, and does not protect `UF`.  It therefore
contributes one to the singleton loss `ell_P(F)`.  Distinct outside owners
give distinct singleton-loss occurrences.  For each fixed `F` there are
only `u` outside owners, proving the additional truncation. \(\square\)

Now choose the alternative-random common-core reservoir of
`MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`.
For this one bank, the frozen simultaneous estimate is

\[
 \ell_P(F)\le R_0=10
 \qquad(F\in\mathcal L).
\tag{4.5}
\]

### Theorem 4.3 (explicit two-boundary safe region)

For the constant-spread reservoir,

\[
 \boxed{
 \lambda_P(\mathcal A(C,S))
 \le \min\{R_0,u\}{v\choose r}
 +2\bigl(H_{m-c}(m)+m+H_d\bigr).}
\tag{4.6}
\]

Consequently the two-sided subcube is safe whenever

\[
 \boxed{
 u-2+{2(m-u)\over m-c}
 \ge \min\{R_0,u\}+
 {2\bigl(H_{m-c}(m)+m+H_d\bigr)\over {v\choose r}}.}
\tag{4.7}
\]

In particular, the simpler conditions

\[
 \boxed{
 u\ge13,
 \qquad
 {v\choose r}\ge2\bigl(H_{m-c}(m)+m+H_d\bigr)}
\tag{4.8}
\]

are sufficient.

There is a useful complementary near-full range.  If `u<=10` and `c>u`,
then (4.7) is equivalent to the sufficient inequality

\[
 \boxed{
 {v\choose r}(c-u)
 \ge (m-c)\bigl(H_{m-c}(m)+m+H_d\bigr).}
\tag{4.9}
\]

#### Proof

Combine Theorem 3.1, Lemmas 4.1--4.2, the path count (4.3), and the
singleton cap (4.5).  This proves (4.6).  Divide the exact slack (2.2) by
`a={v choose r}` to obtain (4.7).  Under (4.8), its left side is at least
`u-2>=11`, while its right side is at most `10+1`.

When `u<=10`, subtracting `u` from the scalar part of (4.7) gives

\[
 -2+{2(m-u)\over m-c}={2(c-u)\over m-c}.
\]

Clearing the positive denominators gives (4.9). \(\square\)

## 5. Exact remaining two-boundary theorem

For the **single alternative-random constant-spread reservoir** used in
Theorem 4.3, both endpoint cases of (3.3) are already closed:

1. `C=emptyset` by its zero-defect complete-support theorem;
2. `S=[n]` by its principal up-star theorem.

The earlier constrained common-`G_2` theorem is a different reservoir and
must not be mixed with the alternative-random principal-star result.

The canonical positive-defect interpolation is therefore the following
explicit statement:

> choose the resident trace paths so that, simultaneously for every
> `C subseteq S`, the core-exit current `xi_P(C,S)` plus the saturated
> outside boundary `theta_P(C,S)` is at most the exact scalar (2.1).

This is a two-boundary current inequality, not an unspecified protected
Ore cut.  Proving it for every subcube would still not by itself classify
all lower families as subcubes; an isoperimetric stability theorem is
needed to pass from arbitrary positive-`b` cuts to these canonical
families.

## 6. Frozen dependencies and scope

The protected Ore definitions and endpoint theorems are frozen in:

| role | file | SHA-256 |
|---|---|---|
| exact weighted Ore identity | `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md` | `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891` |
| one-bank constant spread, complete-support and principal-star closure | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |

No all-subcube factor-extension, arbitrary-family stability,
component-placement, residence-collar, or common-cap conclusion is asserted
here.
