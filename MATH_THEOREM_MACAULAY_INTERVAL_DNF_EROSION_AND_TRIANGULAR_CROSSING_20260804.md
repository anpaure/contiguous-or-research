# Macaulay interval erosion and the exact triangular protected-crossing current

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It gives the canonical
two-sided-interval and principal-star decompositions of every initial colex
segment, classifies all overlaps of their lower shadows, and derives an
occurrence-level protected gluing formula.  For the constant-spread
reservoir it proves an exact head--tail erosion inequality.  A safe head
absorbs every Macaulay tail whose weighted aperture credit is nonnegative.
It also identifies the two-level partial-colex family as a sharp crossing
obstruction: its canonical pieces are individually safe, but their union
has a positive literal pivot current which decomposition alone does not
control.

No computation, search, or solver result is used.

## 0. Setting

Put

\[
 n=2m-1,
 \qquad \mathcal L=\binom{[n]}{m-1}.
\]

Let `P` be a protected subgraph of the Middle-Levels incidence graph with
maximum degree at most two, and write

\[
 \mu_P(A)=\sigma(A)-\lambda_P(A).
\]

When the constant-spread reservoir is used, its frozen singleton estimate
is

\[
 \lambda_P(\{X\})\le10,
 \qquad
 \mu_P(\{X\})\ge m-12
 \quad(X\in\mathcal L).
\tag{0.1}
\]

Let `F` be the initial colex segment of the `m`-sets on `[n]` of size

\[
 f=\binom{c_m}{m}+\binom{c_{m-1}}{m-1}
     +\cdots+\binom{c_s}{s},
\tag{0.2}
\]

where

\[
 n\ge c_m>c_{m-1}>\cdots>c_s\ge s\ge1
\tag{0.3}
\]

is the canonical binomial expansion.  Put

\[
 p_j=c_j+1,
 \qquad
 Q_j=\{p_{j+1},\ldots,p_m\},
 \qquad
 \rho_j=c_j-j+1,
 \qquad
 b_j=\binom{c_j}{j}.
\tag{0.4}
\]

All complements below are taken in `[n]`, and

\[
 A=\{[n]\setminus Y:Y\in F\}\subseteq\mathcal L.
\tag{0.5}
\]

## 1. Canonical interval and DNF decompositions

For `s<=j<=m`, define the Macaulay block

\[
 \mathcal B_j
 =\{Q_j\cup H:H\in\binom{[c_j]}j\}.
\tag{1.1}
\]

The fixed set `Q_j` is disjoint from `[c_j]`, because
`p_l=c_l+1>c_j` whenever `l>j`.

Define

\[
 T_j=Q_j\cup[c_j],
 \qquad
 C_j=[n]\setminus T_j,
 \qquad
 S_j=[n]\setminus Q_j,
\tag{1.2}
\]

and the lower-shore Boolean interval

\[
 \mathcal I_j
 =\{X\in\mathcal L:C_j\subseteq X\subseteq S_j\}.
\tag{1.3}
\]

### Theorem 1.1 (Macaulay intervals and star clauses)

One has the disjoint decompositions

\[
 \boxed{
 F=\mathop{\dot\bigcup}_{j=s}^m\mathcal B_j,
 \qquad
 A=\mathop{\dot\bigcup}_{j=s}^m\mathcal I_j,}
\tag{1.4}
\]

with

\[
 |\mathcal B_j|=|\mathcal I_j|=b_j.
\tag{1.5}
\]

The same lower family also has the monotone-DNF representation

\[
 \boxed{
 A=\bigcup_{j=s}^m\mathcal A_{C_j},
 \qquad
 \mathcal A_{C_j}=\{X\in\mathcal L:C_j\subseteq X\}.}
\tag{1.6}
\]

Thus every Macaulay block is a two-sided Boolean interval, while the
entire colex complement is a union of one principal star per binomial
term.

#### Proof

The standard recursive description of colex first takes all `m`-sets in
`[c_m]`, then fixes `p_m=c_m+1` and takes the initial `(m-1)`-segment of
the residual size, and continues.  At rank `j`, the already fixed pivots
are exactly `Q_j`, and the complete next section is
`Q_j+binom([c_j],j)`.  This proves the first decomposition in (1.4).

Complementing `Q_j+H` gives

\[
 C_j\cup([c_j]\setminus H),
\]

and these are precisely the rank-`m-1` sets between `C_j` and `S_j`.
This proves the second decomposition and (1.5).

Every interval `I_j` lies in the star of `C_j`, so only the reverse
inclusion in (1.6) needs proof.  If `X` contains `C_j` but is not in
`I_j`, it contains some pivot `p_l in Q_j`, with `l>j`.  Directly from
(1.2),

\[
 C_l\subseteq C_j\cup\{p_l\}.
\tag{1.7}
\]

Indeed, a point in `C_l-C_j` is larger than `c_l` and belongs to `Q_j`;
among `p_(j+1),...,p_l` only `p_l=c_l+1` has this property.  Hence
`C_l subset X`, so `X` belongs to a higher-index star.  Repeating this
step reaches some interval `I_h` (at `h=m` there is no upper cap).
Therefore every point of the star union lies in the disjoint interval
union, proving (1.6). \(\square\)

For `j<l`, the point `p_l` lies in `C_l-C_j`, while `p_j` lies in
`C_j-C_l`; hence the displayed cores are pairwise incomparable.  No claim
that a general shifted family has this canonical colex form is made.

The core of `I_j` has size `m-rho_j`.  Thus, for the constant-spread
reservoir and all sufficiently large `m`, every `I_j` is individually safe:
use the all-two-sided-subcube theorem when `rho_j>=2`, the singleton margin
(0.1) when `rho_j=1`, and the trivial full-shore identity at an empty-core
endpoint.

## 2. The triangular shadow-intersection law

Write `partial B_j` for the `(m-1)`-shadow of the block `B_j`.

### Theorem 2.1 (one internal block and triangular boundary blocks)

For `j<l`,

\[
 \boxed{
 \partial\mathcal B_j\cap\partial\mathcal B_l
 =\left\{
 (Q_j\setminus\{p_l\})\cup H:
 H\in\binom{[c_j]}j
 \right\}.}
\tag{2.1}
\]

At every displayed facet, the degree contributed by `B_j` is one, while
the degree contributed by `B_l` is

\[
 \rho_l=c_l-l+1.
\tag{2.2}
\]

Consequently, every shared facet belongs to exactly two block shadows.
For indices `j<l`, block `l` contributes the unique internal degree
`rho_l`, while block `j` contributes one boundary extension.

#### Proof

A facet of `B_j` is of exactly one of the following two forms:

\[
 Q_j\cup H,quad H\in\binom{[c_j]}{j-1},
\tag{2.3}
\]

or

\[
 (Q_j\setminus\{p_h\})\cup H,quad
 j<h\le m,quad H\in\binom{[c_j]}j.
\tag{2.4}
\]

The first kind has degree `rho_j` in `B_j`; the second has degree one.

Every facet of `B_l` lies in `Q_l union [c_l]`.  A facet of the first kind
in (2.3) contains `p_l=c_l+1`, so it cannot meet `partial B_l`.  A facet
of the second kind still contains `p_l` unless `h=l`; hence `h=l` is
necessary.  In that case

\[
 (Q_j\setminus\{p_l\})\cup H
 =Q_l\cup\{p_{j+1},\ldots,p_{l-1}\}\cup H.
\]

The part following `Q_l` is an `(l-1)`-subset of `[c_l]`, so the facet is
internal to `B_l` and has degree `rho_l`.  This also proves the converse.

It remains to rule out a third block.  A facet in the displayed
intersection contains every pivot `p_h` with `h>j`, except `p_l`, and it
contains neither `p_j` nor `p_l`.  An intermediate or later block `B_h`,
`j<h` and `h\ne l`, has every facet contained in `Q_h union [c_h]`, and
hence no facet of `B_h` contains `p_h`; our displayed facet does contain
`p_h`.  An earlier block `B_i`, `i<j`, has `p_j,p_l in Q_i`, while one of
its facets can omit at most one of these two pivots; our displayed facet
omits both.  Thus no third block shadow contains it. \(\square\)

In particular,

\[
 \left|\partial\mathcal B_j\cap\partial\mathcal B_l\right|=b_j
 \qquad(j<l).
\tag{2.5}
\]

In particular, the pairwise intersections in (2.1) are mutually disjoint
as occurrences: triple block-shadow intersections do not occur.

## 3. Exact occurrence-level protected gluing

Fix a facet `D` belonging to at least two block shadows, let

\[
 J(D)=\{j:D\in\partial\mathcal B_j\},
 \qquad l=\max J(D),
 \qquad h=|J(D)|-1=1,
\tag{3.1}
\]

and let `U=[n]\setminus D` be the corresponding owner.  Put

\[
 d=d_P(U)\in\{0,1,2\}.
\]

When `rho_l>=2`, let `tau_D` be the number of protected selected facets at
`U` which belong to one of the `h` boundary blocks.  When `rho_l=1`, let
`t_D` be the number of all protected selected facets at `U`.

Define

\[
 \chi_P(D)=
 \begin{cases}
  h,&\rho_l\ge2,\ d=0,\\
  h-\tau_D,&\rho_l\ge2,\ d=1,\\
  0,&\rho_l\ge2,\ d=2,\\
  h-1,&\rho_l=1,\ d=0,\\
  h-t_D,&\rho_l=1,\ d=1,\\
  0,&\rho_l=1,\ d=2.
 \end{cases}
\tag{3.2}
\]

Every quantity in (3.2) is nonnegative because `h>=1`.

### Theorem 3.1 (exact triangular crossing current)

For the disjoint interval decomposition (1.4),

\[
 \boxed{
 \mu_P(A)
 =\sum_{j=s}^m\mu_P(\mathcal I_j)
  -\sum_{D:\,|J(D)|\ge2}\chi_P(D).}
\tag{3.3}
\]

Moreover, the complete boundary-occurrence ledger is the exact identity

\[
 \boxed{
 \sum_{D:\,|J(D)|\ge2}h
 =\sum_{j=s}^{m-1}(m-j)b_j.}
\tag{3.4a}
\]

Consequently,

\[
 \boxed{
 0\le\sum_D\chi_P(D)
 \le\sum_{j=s}^{m-1}(m-j)b_j.}
\tag{3.4}
\]

The upper bound is exact when every terminal internal degree is at least
two and `P` has degree zero at every shared owner.  In particular it is
exact for a two-level Macaulay expansion with those degree conditions.

#### Proof

At `D`, the terminal block contributes selected fibre size `rho_l`, while
each of the `h` boundary blocks contributes one selected facet.

First assume `rho_l>=2`.  The separate truncated-shadow contribution is
`2+h`, and the union contribution is two, a scalar loss of `h`.  The
terminal block's protected loss is `d-t_0`, where `t_0` is its number of
protected selected incidences.  Boundary singleton blocks have total loss
zero for `d<=1`, and for `d=2` their total loss is `h-tau_D`.  The union
loss is `d-t_0-tau_D`.  Subtracting gives exactly the first three rows of
(3.2).

If `rho_l=1`, all `h+1` pieces are singleton fibres.  The exact singleton
gluing table gives respectively

\[
 (h+1)-2=h-1,
 \qquad
 (h+1)-1-t_D=h-t_D,
 \qquad
 0
\]

for protected degree zero, one, and two.  This proves the last three rows.
Owners belonging to only one block have identical contributions before
and after gluing.  Summation proves (3.3).

Always `chi_P(D)<=h`.  By Theorem 2.1, every shared facet belongs to a
unique pair `(j,l)`, `j<l`, and pair `(j,l)` contributes exactly `b_j`
facets.  Hence

\[
 \sum_Dh
 =\sum_{s\le j<l\le m}b_j
 =\sum_{j=s}^{m-1}(m-j)b_j,
\]

which proves (3.4a) and (3.4).  Under the stated sharpness hypotheses, the
first row of (3.2) gives `chi_P(D)=h=1` at every shared facet, proving
equality in (3.4). \(\square\)

This is the exact occurrence-level obstruction omitted by a mere statement
that every interval piece is safe.  Degree-two protected owners cancel the
entire tax; degree-one owners cancel precisely the protected boundary
occurrences; unprotected shared owners pay the full triangular tax.

### Theorem 3.2 (quantitative block-margin reduction)

Put

\[
 \beta_j=
 \begin{cases}
  j-2,&\rho_j=1,\\
  2\left({j\over\rho_j}-1\right),&\rho_j\ge2.
 \end{cases}
\tag{3.5}
\]

Then, for every protected bank of maximum degree at most two,

\[
 \boxed{
 \mu_P(A)
 \ge\sum_{j=s}^m
 \left(\beta_jb_j-\lambda_P(\mathcal I_j)\right).}
\tag{3.6}
\]

For the constant-spread reservoir, when `rho_j>=2`, one may use

\[
 \lambda_P(\mathcal I_j)
 \le\min\left\{|E(P)|,
       \min\{10,m-j\}b_j+2N_{\rho_j}\right\},
\tag{3.7}
\]

where

\[
 N_\rho=H_\rho(m)+m+H_d.
\]

At `rho_j=1`, the block is a singleton and its loss is at most ten.

Consequently every collection of blocks satisfying

\[
 \sum_j\beta_jb_j
 \ge\sum_j\lambda_P(\mathcal I_j)
\tag{3.8}
\]

is safe.  In particular, a block with `2<=rho_j<j` can pay all of its
worst-case triangular attachments whenever

\[
 \boxed{
 2\left({j\over\rho_j}-1\right)b_j\ge |E(P)|.}
\tag{3.9}
\]

Thus, after all blocks certified by (3.9) are removed from the accounting,
the only intrinsic nonpositive block credits occur at

\[
 \boxed{\rho_j\ge j,}
\tag{3.10}
\]

apart from the zero-credit singleton exception `(j,rho_j)=(2,1)`.  The
remaining positive-credit blocks are unresolved only when their
occurrence-level protected loss is too large for the available credit.

#### Proof

The exact scalar margin of one interval block is obtained directly from
its complement `B_j`.  It has `binom(c_j,j-1)` internal facets of degree
`rho_j` and `(m-j)b_j` boundary facets of degree one.  Therefore

\[
 \sigma(\mathcal I_j)=
 \begin{cases}
  (m-2)b_j,&\rho_j=1,\\
 \left(m-j-2+{2j\over\rho_j}\right)b_j,&\rho_j\ge2.
 \end{cases}
\tag{3.11}
\]

By (3.4a), charge exactly `(m-j)b_j` possible triangular crossing units to block
`j`.  Subtracting this charge from (3.11) leaves exactly `beta_jb_j`.
Summing the individual protected losses proves (3.6).

Bound (3.7) is the frozen exact two-sided current estimate, combined with
the trivial global incidence bound `lambda<=|E(P)|`.  The singleton row is
(0.1).  Equations (3.8)--(3.10) are immediate. \(\square\)

The distinction between (3.9) and the later singleton-tail criterion is
important.  Apart from `(j,rho_j)=(2,1)`, whole-block margins need only
`rho_j<j` before protected loss is priced, whereas singleton erosion uses
the stronger aperture
`rho_j<=j/12` but avoids paying one protected bound independently for every
block.

## 4. A head--tail erosion inequality

Fix `r` with `s<=r<m`, and put

\[
 A^{\rm head}=\mathop{\dot\bigcup}_{j=r+1}^m\mathcal I_j,
 \qquad
 R=\mathop{\dot\bigcup}_{j=s}^{r}\mathcal I_j.
\tag{4.1}
\]

We treat the head as one already correlated block and every member of `R`
as a singleton block.

### Lemma 4.1 (one-unit insertion bound)

At an owner containing `q` selected residual singleton facets, the local
margin loss in gluing those singletons to an arbitrary head fibre is at
most `q`.  If the head fibre is empty and `q>=1`, the loss is at most
`q-1`.

#### Proof

Insert the residual facets one at a time.  The first insertion into an
empty fibre merely identifies the singleton with the union and has zero
cost.  For every later insertion, inspect protected degrees `0,1,2`.
If the old fibre has size zero or one, the truncated-shadow increment is
zero and the protected-loss discrepancy is at most one.  If the old fibre
has size at least two, the separate singleton contributes one extra unit
of truncated shadow, while the protected-loss discrepancy is nonnegative
and at most that unit.  Thus every insertion after the first costs at most
one; without an empty head even the first costs at most one. \(\square\)

### Theorem 4.2 (exact Macaulay erosion bound)

For the constant-spread reservoir and all sufficiently large `m`,

\[
 \boxed{
 \mu_P(A)
 \ge\mu_P(A^{\rm head})
 +\sum_{j=s}^{r}
 \left({j\over\rho_j}-12\right)b_j.}
\tag{4.2}
\]

Consequently, if the head is safe and

\[
 \boxed{
 \sum_{j=s}^{r}
 \left({j\over\rho_j}-12\right)b_j\ge0,}
\tag{4.3}
\]

then the entire colex-complement cut `A` is safe.

#### Proof

Every residual lower vertex lies below exactly `m` owners, so the total
number of residual owner incidences is `m|R|`.

For each `j<=r`, the internal facets of `B_j` are

\[
 Q_j\cup H,
 \qquad H\in\binom{[c_j]}{j-1},
\]

and there are `binom(c_j,j-1)` of them.  By Theorem 2.1, such a facet
does not belong to any higher-index block.  In particular the head fibre
is empty there.  Internal-facet sets belonging to different residual
blocks are disjoint, because every shared facet has a unique terminal
internal block.

Apply Lemma 4.1 at every owner.  The crude charge is one per residual
incidence, but at each residual internal facet the empty-head clause saves
one unit.  Thus the total gluing loss is at most

\[
 m|R|-\sum_{j=s}^{r}\binom{c_j}{j-1}.
\tag{4.4}
\]

By (0.1), the sum of the residual singleton margins is at least
`(m-12)|R|`.  Therefore

\[
\begin{aligned}
 \mu_P(A)
 &\ge\mu_P(A^{\rm head})+(m-12)|R|\\
 &\qquad-m|R|+
   \sum_{j=s}^{r}\binom{c_j}{j-1}\\
 &=\mu_P(A^{\rm head})+
   \sum_{j=s}^{r}
   \left({j\over c_j-j+1}-12\right)\binom{c_j}{j},
\end{aligned}
\]

which is (4.2).  Condition (4.3) now proves the consequence. \(\square\)

### Corollary 4.3 (one-interval head)

When the expansion has at least two terms, take `r=m-1`.  The head `I_m`
is a principal star, hence a two-sided
Boolean interval, and is safe for the constant-spread reservoir.  (At the
rank-`m-1` singleton endpoint, use (0.1); the full-shore endpoint is
trivial.)  Therefore

\[
 \boxed{
 \sum_{j=s}^{m-1}
 \left({j\over\rho_j}-12\right)b_j\ge0
 \quad\Longrightarrow\quad
 \mu_P(A)\ge0.}
\tag{4.5}
\]

In particular, a termwise sufficient condition is

\[
 \rho_j\le {j\over12}
 \qquad(s\le j<m).
\tag{4.6}
\]

More generally, Theorem 4.2 can use any head certified safe by a
bounded-DNF theorem, a direct interval theorem, or a stronger correlated
construction.  The erosion proof itself is independent of how that head
was certified.

The aggregate criterion (4.3) is stronger than (4.6): large positive
credit from one near-diagonal Macaulay block may absorb finitely many
small negative terminal terms.

## 5. The sharp two-level obstruction

Take the two-level initial colex family

\[
 \mathcal F_{t,u}
 =\binom{[t]}m\ \dot\cup\
 \left(\{z\}+\binom{[u]}{m-1}\right),
 \qquad z=t+1,
\tag{5.1}
\]

with `m+1<=t<=2m-2` and `m<=u<=t-1`.  Its canonical data are

\[
 c_m=t,qquad c_{m-1}=u,qquad p_m=z.
\]

There are two individually safe interval pieces.  Their shared facets are
exactly

\[
 H\in\binom{[u]}{m-1}.
\tag{5.2}
\]

Let `U_H=[n]\setminus H`, and let

\[
 X_H=[n]\setminus(\{z\}\cup H)
\]

be the selected lower facet belonging to the second block.  Define

\[
 \Theta_P(t,u)
 =|\{H:d_P(U_H)=0\}|
  +|\{H:d_P(U_H)=1,\ U_HX_H\notin E(P)\}|.
\tag{5.3}
\]

### Corollary 5.1 (literal pivot-current identity)

One has the exact identity

\[
 \boxed{
 \mu_P(A)
 =\mu_P(\mathcal I_m)+\mu_P(\mathcal I_{m-1})
  -\Theta_P(t,u).}
\tag{5.4}
\]

In particular, for the empty protected bank,

\[
 \Theta_{\varnothing}(t,u)
 =\binom u{m-1},
\tag{5.5}
\]

the entire size of the second Macaulay block.

#### Proof

Here every shared owner has one boundary facet from the second block and
terminal internal degree

\[
 \rho_m=t-m+1\ge2
\]

from the first block.  Thus `h=1` in the first three rows of (3.2).  The
tax is one at degree zero, one at degree one unless the second-block facet
is protected, and zero at degree two.  Summing gives (5.3)--(5.4), and
(5.5) is immediate. \(\square\)

This is a sharp counterexample to the hoped **zero-cost** interval
decomposition: even with no residual at all, two safe interval pieces can
carry a gluing tax equal to a macroscopic block.  It is not a counterexample
to protected Ore itself.  Rather, (5.3) is the exact occurrence-level
crossing current which a full theorem must cancel or pay.  A bounded-DNF
theorem can close this two-clause family globally; interval safeness alone
cannot.

## 6. Consequences and exact frontier

The new unconditional conclusions are:

1. every initial colex segment has a canonical disjoint decomposition into
   two-sided Boolean intervals and, simultaneously, a principal-star DNF;
2. every cross-block shadow occurrence is oriented from one boundary block
   to one unique terminal internal block;
3. the protected gluing current is exactly (3.2), with every shared facet
   belonging to exactly two blocks and with complete cancellation at
   protected degree two;
4. a safe head plus a Macaulay tail satisfying the weighted aperture
   inequality (4.3) is safe; and
5. broad terms `rho_j>j/12` are the only terms which can contribute
   negatively to the singleton-erosion certificate, while the block-margin
   reduction has intrinsic nonpositive credit only at `rho_j>=j` and the
   exceptional zero-credit singleton `(j,rho_j)=(2,1)`.

This does **not** finish the shifted-family classification.  Coordinate
compression proves that a capped-shadow minimizer may be shifted, but a
general shifted family need not be an initial colex segment.  Even inside
colex, a long tail of broad terms may make (4.3) negative, and positive
block credit may be smaller than its protected occurrence loss.  Such a
tail requires either a larger correlated DNF theorem, direct control of
the triangular current (3.2), or a separate near-complete-support
stability argument.

Thus the exact remaining lemma is no longer an unspecified erosion
statement.  It is:

> control the degree-zero/one pivot current of broad Macaulay blocks, or
> show that every long broad block run belongs to a bounded-width DNF or
> a certified stability neighbourhood.

No claim about component placement, residence, or the common cap is made.

## 7. Dependencies

| role | file | SHA-256 |
|---|---|---|
| capped-shadow compression and partial-colex obstruction | `MATH_THEOREM_CAPPED_LOWER_SHADOW_COMPRESSION_AND_PARTIAL_COLEX_OBSTRUCTION_20260804.md` | `6e138117e2310bcc8087d3cc67cb07bd1702f0674b1ac1369298205b4fc1610f` |
| all two-sided Boolean intervals pass | `MATH_THEOREM_CONSTANT_SPREAD_ALL_TWO_SIDED_SUBCUBES_ORE_COMPLETE_20260804.md` | `c1bcfa900291760974c167c2c02248c65291d28beaf3ef8e66c095a2301f4817` |
| constant-spread singleton margin | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
