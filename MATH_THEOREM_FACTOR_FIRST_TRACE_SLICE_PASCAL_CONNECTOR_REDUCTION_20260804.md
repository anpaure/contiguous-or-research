# Factor first: exact-trace saturating blocks and the Pascal endpoint connector

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction and deterministic
upper-witness construction.  It shows that a factor-first approach does
not need a random factor to discover the exponentially many common-core
upper witnesses: every nonempty proper exact external-trace slice below
the co-singleton slice has a canonical-size path cover with one component
whose union is the required target.  (The empty and full traces are
boundary slices, not members of the common-history damage family.)
Completing all slices to a Middle-Levels factor is
equivalent to one explicitly defined endpoint-connector problem.  The
co-singleton slice is a sharp exception and necessarily uses a cross-trace
excursion.  No endpoint-connector, residence, or common-cap theorem is
claimed here.

> **2026-08-04 correction.**  The minimum-component specialization of the
> endpoint problem in Section 9 is impossible for every `m >= 4`.  Endpoint
> slot conservation forces `2*binom(m-1,q)^2` cross-trace incidences at rank
> `q`; the rank-two minimum forests do not have that capacity.  The exact
> obstruction and the sharp owner-linear path-splitting repair are proved in
> `MATH_OBSTRUCTION_PASCAL_ENDPOINT_FORCED_SQUARE_FLOW_AND_MINIMUM_SLICE_NOGO_20260804.md`.
> Sections 0--8 below remain valid, but Section 9 must be read with
> square-compatible, nonminimum slice forests.

## 0. Setting

Let

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,
 \qquad |E|=m,
\tag{0.1}
\]

and consider the Middle-Levels incidence graph

\[
 \mathrm {ML}_m=
 \left(\binom{[2m-1]}{m-1},\binom{[2m-1]}m\right).
\tag{0.2}
\]

The common-history hinge ring has common upper core `K`; its possible
damaged targets are `K union T` for proper external traces `T subset E`
containing a cyclic hinge edge.  The purpose of this note is to choose the
Middle-Levels factor before choosing separate protected witness paths.

Put `n=m-1`.  For an owner `U` define

\[
 T=U\cap E,\qquad A=K\setminus U.
\]

Then `|T|=|A|+1`, and every owner has the unique form

\[
 u(A,T)=(K\setminus A)\cup T,
 \qquad A\in\binom K{q-1},\quad T\in\binom E q.
\tag{0.3}
\]

For a lower vertex `x`, put

\[
 S=x\cap E,\qquad B=K\setminus x.
\]

Then `|S|=|B|`, and every lower vertex has the unique form

\[
 \ell(B,S)=(K\setminus B)\cup S,
 \qquad B\in\binom Kq,\quad S\in\binom E q.
\tag{0.4}
\]

Thus the owner shore consists of the difference-one pairs `(A,T)`, while
the lower shore consists of the diagonal pairs `(B,S)`.

## 1. Exact two-kind incidence law

### Lemma 1.1

The lower vertex `ell(B,S)` is adjacent to the owner `u(A,T)` if and only
if exactly one of the following holds:

1. **K step:** `T=S` and `B=A+a` for some `a in K setminus A`;
2. **E step:** `A=B` and `T=S+e` for some `e in E setminus S`.

### Proof

Adjacency is literal containment `ell(B,S) subset u(A,T)`.  Since their
ranks differ by one, the owner is obtained by adding either a coordinate
of `K` or a coordinate of `E`.  Adding `a in K` removes `a` from the
missing set and leaves the external trace fixed, giving case 1.  Adding
`e in E` leaves the missing `K`-set fixed and enlarges the external trace,
giving case 2.  The two cases are disjoint and exhaustive. \(\square\)

Fix an exact trace `T in binom(E,q)`.  Its owner slice is

\[
 \mathcal O_T=\{u(A,T):A\in\binom K{q-1}\},
 \qquad v_q:=|\mathcal O_T|=\binom n{q-1}.
\tag{1.1}
\]

The same-trace lower vertices are

\[
 \mathcal L_T=\{\ell(B,T):B\in\binom Kq\},
 \qquad l_q:=|\mathcal L_T|=\binom nq.
\tag{1.2}
\]

A lower vertex `ell(B,T)` used twice inside the slice joins two distinct
facets `A,A' subset B`.  Consequently the same-trace part of `ML_m` is
exactly the incidence subdivision of the two consecutive levels

\[
                    \binom K{q-1},\quad\binom Kq.
\tag{1.3}
\]

## 2. Slice forests and the exact endpoint-completion equivalence

For every trace `T`, choose a linear forest `F_T` on the owner set
`binom(K,q-1)`.  An edge `AA'` is legal only when

\[
 |A\mathbin\triangle A'|=2,
 \qquad B=A\cup A'\in\binom Kq,
\tag{2.1}
\]

and different edges of `F_T` must have different labels `B`.  Lift that
edge to the two incidences through `ell(B,T)`.  Let

\[
 \mathscr C=\bigsqcup_T\operatorname {Comp}(F_T)
\tag{2.2}
\]

be the family of slice-path components, and let `mathscr R` be the lower
vertices not used by any slice edge.

Every nontrivial path component has its two ordinary endpoint owners.  A
singleton component has two labelled endpoint slots at its unique owner;
the two slots must eventually use two distinct incidence edges.

Construct the **endpoint connector** `Gamma(F)` as follows.  Its left
objects are all endpoint slots of all components, and its right objects
are two capacity copies of every `ell in mathscr R`.  A slot at owner `U`
is eligible for a copy of `ell` precisely when `ell subset U`.  A selection
is called physical when the two slots of one singleton are not both sent
to the same lower vertex.

### Theorem 2.1 (factor-first endpoint equivalence)

The slice forests extend to a spanning two-factor of `ML_m` if and only if
`Gamma(F)` has a physical matching which covers every endpoint slot and
uses both copies of every member of `mathscr R`.

For any such matching, contract every path component of every `F_T` to one
component vertex and every `ell in mathscr R` to one connector vertex.
The resulting bipartite multigraph has degree two at every vertex.  The
completed Middle-Levels factor has exactly the same number of components
as this quotient.  In particular, the factor is one cycle exactly when
the quotient is one alternating Hamilton cycle on

\[
                         \mathscr C\sqcup\mathscr R.
\tag{2.3}
\]

The same statement permits a prescribed cycle partition, for example one
cycle through each old ring hinge before the cyclic hinge rethread.

### Proof

Every selected same-trace lower vertex already has degree two, every
internal owner of a slice path already has degree two, and every endpoint
slot represents exactly one missing incidence at its owner.  Every member
of `mathscr R` still needs exactly two incidences.  Thus the displayed
matching is exactly the residual degree equation on both shores.  The
physical qualification only excludes choosing the same simple incidence
twice at a singleton owner.

After adding those incidences, suppressing each internal path changes no
connectivity.  The quotient has two incident connector edges at every
path component and two at every residual lower vertex.  Hence it is
2-regular, and suppression identifies its cycles bijectively with the
cycles of the completed factor.  The converse is obtained by reading the
residual incidences of any completion. \(\square\)

This is not merely another form of the protected Ore--Ryser inequalities.
The slice edges explicitly saturate part of both shores, and the only
remaining choice is the occurrence-labelled endpoint matching plus its
cycle structure.

## 3. Exact Pascal count and square frontier

Let `b_T` be the number of components of `F_T`, and let `r_T` be the
number of unused same-trace lower vertices.  Since a forest on `v_q`
vertices with `b_T` components has `v_q-b_T` edges,

\[
 r_T=l_q-v_q+b_T.
\tag{3.1}
\]

### Theorem 3.1 (global equality and rank-prefix square)

For every collection of slice forests,

\[
                         |\mathscr R|=|\mathscr C|.
\tag{3.2}
\]

More precisely, let `R_q` and `C_q` be the numbers of residual lower
vertices and components in all traces of size `q`.  With

\[
                         a_q=\binom{m-1}q,
 \qquad a_{-1}=a_m=0,
\]

one has

\[
 \boxed{R_q-C_q=a_q^2-a_{q-1}^2,}
\tag{3.3}
\]

and therefore

\[
 \boxed{
 \sum_{j=0}^q(R_j-C_j)=\binom{m-1}q^2.}
\tag{3.4}
\]

### Proof

There are `binom(m,q)` traces of size `q`.  Equation (3.1) gives

\[
 R_q-C_q=\binom mq(l_q-v_q).
\]

Pascal's identity gives `binom(m,q)=a_q+a_(q-1)`, while
`l_q-v_q=a_q-a_(q-1)`.  Their product is (3.3), and summation telescopes
to (3.4).  At `q=m` the square is zero, proving (3.2). \(\square\)

The square frontier is independent of every choice inside the slices.
It is the exact scalar law an inductive endpoint construction must
respect; it explains why the connector counts close without an error
term.

## 4. Saturating cycles construct the slice blocks

We use the following published result of Gregor--Micka--Mütze: the
subgraph of a Boolean cube induced by any consecutive sequence of levels
has a saturating cycle, i.e. a simple cycle visiting every vertex of its
smaller bipartition class.  Apply it to the two levels in (1.3).

### Theorem 4.1 (minimum-component exact-trace cover)

For every trace `T` of size `q` with

\[
                         2\le q\le m-2,
\tag{4.1}
\]

there is a linear forest `F_T` with

\[
 \boxed{b_T=\max\{1,v_q-l_q\},
 \qquad r_T=\max\{0,l_q-v_q+1\}.}
\tag{4.2}

It has one distinguished nontrivial component `C_T` satisfying

\[
 \bigcup_{u(A,T)\in C_T}u(A,T)=K\cup T.
\tag{4.3}
\]

All other components, when present, are singletons.

For `q=1`, the unique owner `K union T` is itself a distinguished
singleton component and already has union `K union T`.

### Proof

First suppose `v_q<=l_q`.  A saturating cycle visits every rank-`q-1`
set `A` and `v_q` distinct rank-`q` labels.  Delete one label edge from
the projected owner cycle.  The result is a Hamilton path on all `v_q`
owners, using `v_q-1` labels.  This gives `b_T=1` and
`r_T=l_q-v_q+1`.

The intersection of all `(q-1)`-subsets of `K` is empty, so the union of
their complements is `K`.  Hence the path has union `K union T`.

Now suppose `v_q>l_q`.  A saturating cycle visits every rank-`q` label
and `l_q` owner indices.  Choose any owner index `A_*` outside the cycle.
It is incident with at least one rank-`q` label `B` on the cycle.  At `B`,
replace one of the two cycle incidences by `A_* B`.  The cycle becomes one
simple alternating path containing all `l_q` labels and `l_q+1` owner
indices.  Every other owner is retained as a singleton.  Thus all labels
are used, and the number of components is

\[
 1+v_q-(l_q+1)=v_q-l_q.
\]

For each `x in K`, there is a rank-`q` label `B_x` not containing `x`,
because `q<=m-2=|K|-1`.  One of the path owners incident with `B_x` is a
subset of `B_x` and therefore also omits `x`.  Its actual `K`-part
`K setminus A` contains `x`.  Hence the distinguished path again has
`K`-union equal to all of `K`.

The two count formulas now follow from (3.1).  The `q=1` assertion is
literal. \(\square\)

Thus, if the endpoint connector is solved, every target in the
common-history damage family with `|T|<=m-2` is already witnessed
deterministically.  (Those traces are nonempty—in fact they contain a
cyclic hinge edge—so the boundary trace `T=emptyset` is not being claimed
here.)  The number of such targets is exponential, but no probabilistic
union bound is needed.

## 5. The sharp co-singleton exception

### Theorem 5.1 (exact-trace co-singletons cannot work)

Assume `m>=4` and let `|T|=m-1`.  No component using only same-trace lower
vertices can have union `K union T`.

### Proof

Here the owner indices are the `(m-2)`-subsets of `K`, so each actual owner
contains exactly one coordinate of `K`.  There is only one same-trace lower
label, namely `B=K`.  Since that lower vertex has degree two in a factor,
it can join at most two owners.  Every same-trace component therefore has
at most two owners, and its union contains at most two coordinates of
`K`.  Since `|K|=m-1>=3`, it cannot have union `K union T`. \(\square\)

The obstruction is exact rather than asymptotic.  It explains why the
high-tail monotone geodesics in the clipped-resident reservoir genuinely
change external trace: the top co-singleton targets cannot be witnessed
inside their own slices.

There is nevertheless no scalar deficit.  One may use the sole same-trace
lower vertex to join two owners and retain the other `m-3` owners as
singletons, giving `b_T=m-2=v_q-l_q` and `r_T=0`; only the target witness
must come from a cross-trace segment.

## 6. The hinge ring is literally a connector switch

Use the full common-history ring notation

\[
 K=B\cup\{b\},\qquad E=\{a_0,\ldots,a_{m-1}\}.
\]

Its old hinge has

\[
 L_i=K+a_i,qquad
 I_i=(K-b)+a_i,qquad
 R_i=(K-b)+a_{i-1}+a_i.
\tag{6.1}
\]

In the difference-one coordinates these are

\[
 L_i=u(\varnothing,\{a_i\}),
\quad I_i=\ell(\{b\},\{a_i\}),
\quad R_i=u(\{b\},\{a_{i-1},a_i\}).
\tag{6.2}
\]

Thus `I_i` is an unused diagonal lower vertex joining an endpoint in a
one-trace slice to an endpoint in a two-trace slice.  The rethreaded head

\[
 R_{i+1}=u(\{b\},\{a_i,a_{i+1}\})
\tag{6.3}
\]

is another child endpoint of the **same** connector `I_i`.  The cyclic
common-history rethread is therefore exactly a reassignment of one side of
these `m` connector vertices; it changes no slice forest.

For every two-trace slice, Theorem 4.1 is just a Hamilton path on the
singleton indices of `K`.  Its endpoint can be chosen to be `{b}`.
Consequently all `m` old ring hinges can be made eligible in the endpoint
connector without using a protected-factor extension theorem.

## 7. Cross-trace chains suffice for the exceptional targets

Order `E` cyclically and put

\[
 T_{i,q}=\{a_i,a_{i-1},\ldots,a_{i-q+1}\}
 \qquad(1\le q\le m-1).
\tag{7.1}
\]

For fixed `q<m`, the traces `T_(i,q)` are distinct.  Suppose an endpoint
completion traverses, consecutively and without leaving their union, one
distinguished component from each of

\[
 T_{i,1},T_{i,2},\ldots,T_{i,m-2},
\tag{7.2}
\]

and then any component of the co-singleton slice `T_(i,m-1)`.  Then the
expanded factor segment has union

\[
                         K\cup T_{i,m-1}.
\tag{7.3}
\]

Indeed, every component lies inside (7.3), the first distinguished
component already contains all of `K`, and the nested traces introduce all
external coordinates of `T_(i,m-1)`.  Therefore only `m` prescribed
cross-trace component chains are needed to cover the exact-trace exception.
Their first transitions can be the ring hinges (6.2).

This is a sufficient interface, not an assertion that the endpoint graph
always contains the chains.

## 8. Why ordinary spread is not the needed random theorem

Let `mu` be any distribution on factor completions containing the ring,
and let `P_(Z,1),...,P_(Z,s_Z)` be candidate factor paths witnessing a
target `Z`.  The following elementary criterion records the exact kind of
probability estimate that would suffice.

### Lemma 8.1 (sequential lower-thickness criterion)

If, for every `Z` and every `j`,

\[
 \Pr_\mu\!\left(P_{Z,j}\subset F\ \middle|\
 P_{Z,1}\not\subset F,\ldots,P_{Z,j-1}\not\subset F\right)
 \ge p_{Z,j},
\tag{8.1}
\]

then

\[
 \Pr_\mu(Z\text{ has no listed witness})
 \le \exp\!\left(-\sum_jp_{Z,j}\right).
\tag{8.2}
\]

Consequently, if

\[
 \sum_{Z\in\mathcal D}
 \exp\!\left(-\sum_jp_{Z,j}\right)<1,
\tag{8.3}
\]

some completion witnesses every target.

### Proof

Expose the candidate failures in the displayed order.  The conditional
probability of failing candidate `j` is at most `1-p_(Z,j)`.  Multiply and
use `1-x<=e^(-x)`, then union-bound over `Z`. \(\square\)

The usual definition of a spread measure gives **upper** bounds on
cylinder probabilities.  It supplies neither (8.1) nor a lower bound on
the probability of any witness.  Therefore “take a spread random
two-factor and union-bound” is not a proof-safe argument.  One would need
a lower-thickness or Janson-type theorem under the ring conditioning and
under all previous failures.

The deterministic slice construction is stronger for the bulk: it makes
all `|T|<=m-2` failure probabilities identically zero.  Randomness, if used
at all, should be aimed at the endpoint connector, its prescribed `m`
cross-trace chains, residence, and the common cap—not at rediscovering
`Theta(2^m)` separate upper witnesses.

## 9. Exact remaining theorem

The factor-first route is reduced to the following statement.

> **Pascal endpoint-cycle theorem.**  Choose the saturating slice forests
> of Theorem 4.1 (with the co-singleton and full-trace boundary forests),
> their endpoint orientations, and their saturating cycles so that the
> endpoint connector has a physical 2-factor with the desired component
> partition; it contains the `m` hinge connectors and the `m` nested
> chains of Section 7; and the expanded chronology meets the residence and
> common-cap guards.

The scalar part of this theorem is exact by (3.2)--(3.4).  The remaining
content is integral endpoint incidence, topology, residence, and cap
correlation.  In particular, this theorem bypasses the all-cut Ore problem
for a separately frozen `O(m2^m)` witness bank, but does not make the
global correlation disappear.

## 10. Dependencies

| role | file | SHA-256 |
|---|---|---|
| common-history hinge identities and rethread | `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md` | `96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba` |
| clipped-resident cross-trace high-tail construction | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| audited repository interface to the GMM two-level saturating-cycle theorem | `MATH_THEOREM_Q1_RAINBOW_JOHNSON_SATURATING_INTERFACE_20260726.md` | `fbcb016be136c5348aecb67ad8ae281a72d921ca178cf0e6642f74a38459ef6d` |

The GMM dependency is used only for existence of a simple saturating cycle
between two consecutive levels.  No prescribed endpoints, random-cycle
law, residence property, or deeper upper-deck property is imported from
that theorem.

Finally, solving the endpoint matching in Theorem 2.1 would prove a
Middle-Levels two-factor containing the displayed common-core target
witnesses.  It would **not** by itself prove the full arbitrary-upper deck
of a starting carrier, global residence, a common-cap compiler, or an
`O(1)` upper bound for `nu(k)`; those implications still require the
frozen hinge transport and the remaining global guards.
