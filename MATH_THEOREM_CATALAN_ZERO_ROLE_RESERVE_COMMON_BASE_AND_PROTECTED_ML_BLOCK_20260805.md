# Catalan zero-role reserve, an exact SCD common-base gate, and a protected Middle-Levels block

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional zero-role inventory, unconditional static
reservation of any `d<=q` roots, an exact Hall/matroid-intersection theorem
for reserving them inside an SCD--Middle-Levels parity matching, and an
unconditional protected two-factor planting theorem when
`2d-2<=q-2`.  Literal forced-prefix support and rooted Hamilton completion
remain correlated open conditions.

## 0. Outcome

Put

\[
 n=2q-1,
 \qquad
 \mathcal L=\binom{[n]}{q-1},
 \qquad
 \mathcal U=\binom{[n]}q,
 \qquad
 W=|\mathcal L|=|\mathcal U|.
\tag{0.1}
\]

Consider a saturated chain partition of the lower collar band

\[
 \mathcal B_d=
 \bigcup_{j=1}^{d-1}\binom{[n]}{q-1-j},
 \qquad 2\le d\le q-1,
\tag{0.2}
\]

all of whose chains end in rank `q-2`.  Add empty roles until there are
`W` roles, one for every prospective rank-`q-1` root.

This note proves the following.

1. The height inventory is forced.  In particular the number of height-zero
   roles is

   \[
    W-\binom{2q-1}{q-2}
    ={2W\over q+1}
    ={1\over q+1}\binom{2q}q
    =\operatorname{Cat}_q.
   \tag{0.3}
   \]

2. For any prescribed root set `P subseteq mathcal L` with `|P|<=q`, all
   nonempty chains can be injected into roots outside `P`, respecting top
   containment.  Hence any `d<=q` consecutive roots of any Middle-Levels
   Hamilton cycle may be declared height zero at the **static role** level.

3. If one also requires those roots to be the central two-element chains of
   an SCD whose central matching is a fixed Hamilton parity `M`, the exact
   condition is one common-base problem for two transversal matroids.  It
   has both an Edmonds min--max formula and one ordinary Hall formulation.
   The two one-sided Hall systems always pass for `|P|<=q`; their mixed
   common-base cuts are the remaining SCD compatibility.

4. A concrete alternating path through `d` lower roots uses only `2d-2`
   Middle-Levels incidences.  The small protected-factor theorem therefore
   embeds it in a spanning two-factor whenever `2d-2<=q-2`.  Thus the
   physical owner/q1 cost of a consecutive zero block is `O(d)` and is
   negligible for `d=Theta(sqrt(q))`.

5. Neither item 2 nor item 4 makes the static chain at a root equal to its
   actual future-intersection flag.  For a fixed factor and chain partition,
   the exact missing condition is local in the top fibres: every chain must
   have one literal forced-prefix provider outside `P`.  The protected
   factor theorem does not prove those nonempty provider sets, nor does it
   give one Hamilton component.

Thus the safe-cut reserve is unconditional in the static and q1-factor
projections.  The surviving obstruction is not the number of empty roles;
it is co-selection of the factor chronology with the forced-prefix
providers (and, if an SCD is retained, the mixed common-base cuts).

## 1. Exact height inventory

Let a role have height `h` when its chain contains ranks

\[
 q-2,q-3,\ldots,q-1-h.
\]

Empty roles have height zero.  For `1<=j<d`, put

\[
                         N_j=\binom{2q-1}{q-1-j}.
\tag{1.1}
\]

### Theorem 1.1 (Catalan zero-role inventory)

Every saturated chain partition of (0.2), after augmentation to `W` roles,
satisfies

\[
                         \#\{u:h(u)\ge j\}=N_j
                         \qquad(1\le j<d).
\tag{1.2}
\]

Consequently

\[
\begin{aligned}
 \#\{u:h(u)=0\}
   &=W-N_1=\operatorname{Cat}_q,\\
 \#\{u:h(u)=j\}
   &=N_j-N_{j+1}\qquad(1\le j<d-1),\\
 \#\{u:h(u)=d-1\}
   &=N_{d-1}.
\end{aligned}
\tag{1.3}
\]

#### Proof

A saturated chain ending in rank `q-2` meets rank `q-1-j` if and only if
its height is at least `j`.  The chains partition that complete rank, which
has `N_j` members, proving (1.2).  Subtract consecutive tails to obtain
(1.3).  Finally

\[
 \binom{2q-1}{q-2}
 ={q-1\over q+1}\binom{2q-1}{q-1},
\]

and

\[
 {2\over q+1}\binom{2q-1}{q-1}
 ={1\over q+1}\binom{2q}q,
\]

which is (0.3).  \(\square\)

The inventory is independent of the chosen chain partition.  In
particular, the safe-cut problem is not short of empty roles: its empty
stock is Catalan-sized.

## 2. Any `q` prescribed roots can be kept empty statically

For every top `S in binom([n],q-2)`, let `C_S` be the unique chain of the
partition ending at `S`.

### Theorem 2.1 (prescribed-empty static role extension)

Let `P subseteq mathcal L` with `|P|<=q`.  There is an injection

\[
 \mu:\binom{[n]}{q-2}\longrightarrow\mathcal L\setminus P
 \quad\text{such that}\quad
 S\subset\mu(S)
\tag{2.1}
\]

for every `S`.  Consequently every `C_S` can be realized as a static flag
prefix at root `mu(S)`, and all remaining roots, including every member of
`P`, receive height zero.

#### Proof

Apply Proposition 1.2A of
`MATH_THEOREM_NESTED_INTERSECTION_BANK_SUPPORTED_CHAIN_EQUIVALENCE_PASCAL_RECURSION_AND_UCYCLE_NOGO_20260804.md`
to the inclusion graph from rank `s=q-2` to rank `s+1=q-1` on `k=2q-1`
points.  Its parameters are

\[
 a=k-s=q+1,
 \qquad
 b=s+1=q-1.
\]

The protected-upper reserve in that theorem is

\[
\begin{aligned}
 \eta_s
 &=\left\lfloor\min\left\{
 q,
 {2((q+1)(q-1)+1)\over q-1}
 \right\}\right\rfloor\\
 &=q.
\end{aligned}
\tag{2.2}
\]

Therefore deletion of any `P` of size at most `q` preserves a matching
saturating the complete rank-`q-2` shore.  This is (2.1).

To realize `C_S` statically, write it as

\[
 S=S_1\supset S_2\supset\cdots\supset S_h.
\]

Inside `R=mu(S)`, use first the singleton `R setminus S`, followed by the
singletons `S_1 setminus S_2,...,S_(h-1) setminus S_h` as the declared
future departures.  Their successive intersections are exactly `C_S`.
Different chains use different roots by injectivity.  Assign height zero to
all unused roots.  \(\square\)

### Corollary 2.2 (static consecutive zero block)

Fix any Hamilton cycle of `ML_q`, orient it, and list its lower vertices in
cyclic order.  Any prescribed block of `d<=q` consecutive lower vertices
can receive height zero while every chain in (0.2) receives a distinct
containing root outside the block.

The upper-rainbow row is automatic at this projection: the Hamilton cycle
visits every rank-`q` upper vertex once.

This corollary is a static role theorem.  Its declared departure list is not
yet asserted to equal the departures forced by the next roots of the fixed
Hamilton cycle.

## 3. Exact SCD extension with prescribed central short chains

The antichain-top SCD--Hamilton theorem chooses an SCD after a Hamilton
parity matching has been chosen, but it does not prescribe which central
matching edges become the two-element SCD chains.  That refinement has an
exact common-base form.

Fix a perfect inclusion matching

\[
                         M:\mathcal L\longrightarrow\mathcal U.
\tag{3.1}
\]

For example, `M` may be one parity matching of a Middle-Levels Hamilton
cycle.  Put

\[
 \mathcal A=\binom{[n]}{q-2},
 \qquad
 \mathcal Z=\binom{[n]}{q+1},
 \qquad
 a=|\mathcal A|=|\mathcal Z|.
\tag{3.2}
\]

Define two transversal matroids on ground set `mathcal L`.

* For `E subseteq mathcal L`, let `r_-(E)` be the maximum matching size in
  the inclusion graph `mathcal A -- E`.
* Let `r_+(E)` be the maximum matching size in the graph joining
  `R in E` to `Z in mathcal Z` when `M(R) subset Z`.

Both full matroids have rank `a`.

### Theorem 3.1 (prescribed-short SCD common-base theorem)

For `P subseteq mathcal L`, the following are equivalent.

1. There is a full symmetric-chain decomposition of `B_n` whose central
   matching is `M` and in which every central edge `R<M(R)`, `R in P`, is
   a two-element SCD chain.
2. The restrictions of the two transversal matroids to
   `E_0=mathcal L setminus P` have a common base of size `a`.
3. For every `A subseteq E_0`,

   \[
    \boxed{
    r_-(A)+r_+(E_0\setminus A)\ge a.}
   \tag{3.3}
   \]

4. The bipartite graph `H_(M,P)` below has a perfect matching.  Its shores
   are

   \[
    \mathcal A\mathbin{\dot\cup}E_0^-
    \quad\text{and}\quad
    \mathcal Z\mathbin{\dot\cup}E_0^+,
   \tag{3.4}
   \]

   with edges

   \[
   \begin{array}{lll}
    S-R^+&\text{when}&S\subset R,\\
    R^--Z&\text{when}&M(R)\subset Z,\\
    R^--R^+&&.
   \end{array}
   \tag{3.5}
   \]

Equivalently, item 4 is the exact Hall family

\[
 \boxed{
 |N_-(X)\cup B|+|N_+(B)|\ge |X|+|B|
 }
\tag{3.6}
\]

for every `X subseteq mathcal A` and `B subseteq E_0`, where

\[
\begin{aligned}
 N_-(X)&=\{R\in E_0:\exists S\in X, S\subset R\},\\
 N_+(B)&=\{Z\in\mathcal Z:\exists R\in B, M(R)\subset Z\}.
\end{aligned}
\tag{3.7}
\]

#### Proof

Items 2 and 3 are equivalent by Edmonds' matroid-intersection min--max
theorem.

Suppose item 2 holds, with common base `E`.  Choose a perfect matching from
`mathcal A` to `E` and a perfect matching from `M(E)` to `mathcal Z`.  For
each `R in E` these make one symmetric four-rank chain

\[
                         S_R<R<M(R)<Z_R.
\tag{3.8}
\]

For `R notin E`, retain the central two-element chain

\[
                         R<M(R).
\tag{3.9}
\]

Equations (3.8)--(3.9) partition all four central ranks.  Their endpoints
are rank-symmetric because

\[
 (q-2)+(q+1)=n,
 \qquad
 (q-1)+q=n.
\]

The outward induction in the central-matching extension theorem now
extends this symmetric central-band decomposition to a full SCD while
preserving all its internal adjacencies.  Since `E subseteq E_0`, every
member of `P` has the short form (3.9).  This proves item 1.

Conversely, in a full SCD let `E` be the central lower roots whose chain
also meets rank `q-2`.  Every rank-`q-2` set has a distinct successor in
`E`, and symmetry gives every `M(R)`, `R in E`, a distinct rank-`q+1`
successor.  Hence `E` is a common base.  A root in `P` is short, so
`E subseteq E_0`.  This proves item 2.

For items 2 and 4, observe that a perfect matching in `H_(M,P)` uses the
same set `E` of roots on the two outer comparisons.  Indeed, if `R^+` is
matched from `mathcal A`, then `R^-` cannot use its identity and must be
matched to `mathcal Z`; the converse is identical.  The remaining roots
use their identities.  Thus a perfect matching is precisely two outer
matchings on one common base `E`.  Finally, a left set of `H_(M,P)` has the
form `X dotcup B^-`; its right neighbourhood is the disjoint union

\[
                         (N_-(X)\cup B)^+
                         \mathbin{\dot\cup}N_+(B).
\]

Hall's theorem is exactly (3.6).  \(\square\)

### Proposition 3.2 (the two endpoint systems always pass)

If `|P|<=q`, then

\[
                         r_-(E_0)=r_+(E_0)=a.
\tag{3.10}
\]

#### Proof

The first equality is Theorem 2.1.  For the second, complement every
`Z in mathcal Z` and every upper owner `M(R)`.  The incidence
`M(R) subset Z` becomes

\[
                         Z^c\subset M(R)^c,
\]

between ranks `q-2` and `q-1`.  As `R` ranges over `P`, the forbidden sets
`M(R)^c` are `|P|` distinct rank-`q-1` vertices.  Theorem 2.1 applies
again.  \(\square\)

Thus ordinary lower Hall and ordinary upper Hall do not obstruct a
`d<=q` reserve.  What remains in Theorem 3.1 is exactly the mixed family
(3.3), equivalently (3.6).  Neither the antichain-top theorem nor the
ordinary protected-factor theorem proves those mixed cuts after `P` is
fixed.

## 4. The consecutive block costs only `2d-2` protected incidences

### Theorem 4.1 (protected consecutive-root block)

Assume

\[
                         d\le q+1,
 \qquad
                         2d-2\le q-2.
\tag{4.1}
\]

Then `ML_q` has a spanning two-factor containing an alternating path whose
lower shore consists of `d` consecutive vertices.  Those `d` roots may
simultaneously be assigned height zero in the static role system of
Theorem 2.1.

#### Proof

Choose a `(q-2)`-set `K` and distinct labels

\[
                         a_0,a_1,\ldots,a_{d-1}
                         \in[n]\setminus K.
\]

This is possible because the complement of `K` has size `q+1`.  Put

\[
 R_i=K\cup\{a_i\}\in\mathcal L,
 \qquad
 U_i=K\cup\{a_i,a_{i+1}\}\in\mathcal U.
\tag{4.2}
\]

Then

\[
 R_0-U_0-R_1-U_1-\cdots-U_{d-2}-R_{d-1}
\tag{4.3}
\]

is a simple alternating path with `2d-2` incidence edges and maximum degree
two.  By (4.1), the small protected-factor theorem embeds (4.3) in a
spanning two-factor of `ML_q`.  Its component containing (4.3), in one of
its two orientations, has the displayed lower roots consecutively.

Since `d<=q`, Theorem 2.1 assigns all nonempty static roles to roots outside
`P={R_0,...,R_(d-1)}`.  Thus every root in the block has height zero.
\(\square\)

Every spanning Middle-Levels two-factor uses each upper vertex once.  Its
projected lower-root cycles therefore have distinct adjacent unions and are
upper-rainbow globally.  The theorem does not assert one component: the
small protected-factor completion may have as many as `W/3` cycles.

For the coefficient-one deadline `d=Theta(sqrt(q))`, both inequalities in
(4.1) hold for all sufficiently large `q`.  The protected block uses
`O(d)=o(q)` of the available `q-2` edge budget.

### Corollary 4.2 (triangular safe cut at the projected level)

Orient the component from Theorem 4.1 so that the block immediately
precedes a chosen cut.  Every predecessor in the triangular safety window
has height zero, and hence

\[
                         h(c-1-t)=0\le t
                         \qquad(0\le t<d-1).
\tag{4.4}
\]

Thus the cut is triangularly safe for the static height assignment.

## 5. Exact literal forced-prefix compatibility

The preceding results do not turn static departures into the departures
forced by the factor chronology.  This final distinction is exact.

Fix an oriented factor component with lower-root order `(R_i)`.  Put

\[
                         I_{i,j}=\bigcap_{u=0}^jR_{i+u}.
\tag{5.1}
\]

For a fixed chain partition `mathscr C`, let `C_S` be the chain ending at
`S in binom([n],q-2)` and define its provider set outside `P` by

\[
 \mathcal F_{\Phi,P}(C_S)=
 \{i:\ R_i\notin P,
       I_{i,1}=S,
       (I_{i,1},\ldots,I_{i,|C_S|})=C_S\}.
\tag{5.2}
\]

### Theorem 5.1 (exact supported-bank reserve criterion)

The factor supports the chain partition with every root in `P` at height
zero if and only if

\[
                         \mathcal F_{\Phi,P}(C_S)\ne\varnothing
                         \qquad
                         (S\in\tbinom{[n]}{q-2}).
\tag{5.3}
\]

#### Proof

Necessity is immediate.  Conversely choose one root from each provider set.
Provider sets for different tops are disjoint, because a root has only one
first forced value `I_(i,1)`.  Hence all chosen roots are distinct, their
forced prefixes are exactly the chains of `mathscr C`, and no chosen root
lies in `P`.  The supported-band-chain equivalence gives the nested banks.
\(\square\)

At depth one alone, (5.3) reduces to

\[
 \{I_{i,1}:R_i\notin P\}
 \supseteq \binom{[n]}{q-2}.
\tag{5.4}
\]

Theorem 4.1 does not imply (5.4): spanning the two Middle Levels shores
controls the lower roots and their rank-`q` adjacent unions, not their
rank-`q-2` consecutive intersections.  At greater depth it supplies none
of the equalities in (5.2).

If the chain partition is not fixed, the exact condition is the restricted
prefix-cover system

\[
 \sum_{\substack{(i,h):R_i\notin P\\X\in C(i,h)}}x_{i,h}=1
 \qquad(X\in\mathcal B_d),
\tag{5.5}
\]

with binary variables.  As before, no separate root-capacity row is needed,
because two positive prefixes at one root share their top.

## 6. Revised frontier

The safe-cut reserve has three increasingly strong meanings.

1. **Static role reserve:** unconditional for any prescribed `d<=q` roots
   by Theorem 2.1.
2. **Upper-rainbow q1-factor reserve:** unconditional in a spanning
   two-factor when `2d-2<=q-2` by Theorem 4.1.
3. **Literal supported-bank reserve:** equivalent to (5.3), or to (5.5)
   when the chain partition is free.  This is not supplied by the first two
   statements.

If one insists that the Hamilton parity also be the central matching of an
SCD with the reserved roots as its central short chains, Theorem 3.1 adds
the exact mixed common-base cuts (3.3)/(3.6).  The two endpoint Hall rows
already pass, so this is a genuinely correlated condition rather than a
capacity shortage.

The shortest remaining co-selection theorem is therefore:

> Find an upper-rainbow one-component Middle-Levels factor containing the
> protected `d`-root block such that the restricted forced-prefix
> hypergraph (5.5) exactly covers the collar band; if the SCD interface is
> retained, satisfy the common-base cuts (3.3) on the same parity matching.

No existing antichain-top, protected-factor, or Middle Levels Hamilton
theorem proves this combined statement.  In particular:

* the antichain-top theorem realizes chains statically but not as future
  intersections;
* the small protected-factor theorem preserves the block but gives neither
  one component nor the lower intersection decks; and
* ordinary one-sided Hall ignores the common-base and chronology coupling.

Accordingly this note reserves the cut at negligible static/q1 cost but
does not claim a resident supported Hamilton factor or an all-dimensional
coefficient-one construction.

## 7. Dependencies

1. `MATH_THEOREM_NESTED_INTERSECTION_BANK_SUPPORTED_CHAIN_EQUIVALENCE_PASCAL_RECURSION_AND_UCYCLE_NOGO_20260804.md`;
2. `MATH_THEOREM_ANTICHAIN_TOP_SCD_HAMILTON_OWNER_LIFT_AND_LITERAL_AGE_GATE_20260802.md`;
3. `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`;
4. Edmonds' matroid-intersection theorem; and
5. Hall's marriage theorem.
