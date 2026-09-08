# A literal biresident screen lattice realizes the two-component common-history `C8`

**Date:** 2026-08-05  
**Method:** explicit source word, blockwise core swaps, and cut-permutation
calculus; no computation or search  
**Status:** unconditional local/prospective theorem.  The abstract
zero-charge `C8` crossover has a literal two-cycle source realization in
which both phases are owner-simple, globally q1-simple, and biresident at
depth `d`.  The packet has `16(d+1)` source/owner positions and embeds as a
protected bank in an exact q1 factor for all sufficiently large central
levels.  Attaching its two old cycles to prescribed large PBBS components,
and protecting arbitrary-width exterior upper witnesses and the typed cap,
remain separate global gates.

## 0. Outcome

The abstract common-history `C8` uses four hinge roles

\[
 X_i\,\mathcal C\,Y_i\qquad(i\in\mathbb Z_4)
\]

with the same ordered length-`d` history `mathcal C`.  The old roles `0,2`
belong to one source component and `1,3` to another.  Cyclically moving the
complete continuation beginning at `Y_(i+1)` after role `i` changes the
next-role permutation from

\[
                         i\longmapsto i+2
\]

to

\[
                         i\longmapsto i+3,
\]

and hence fuses the two components.

The missing local question was whether the four equal histories can be
joined into actual resident source circuits without repeating an owner or
an immediate colour.  A direct common-core return fails: two of its active
screens are disjoint and therefore make a non-Johnson step.  The
construction below inserts two active bridge screens and two shared core
excursions.  Every source occurrence then lies on one residue class modulo
`d+1`; this makes positive runs and zero gaps simultaneously multiples of
`d+1`.

## 1. Coordinates and ordered core partitions

Fix `d>=1` and an owner rank `r`.  Let `B` have rank `r-2`.  Choose
distinct active coordinates

\[
 b,a_0,a_1,a_2,a_3,c_0,c_1,c_2,c_3\notin B.
\tag{1.1}
\]

Choose an ordered partition into blocks of size at least two

\[
                         B=C_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d.       \tag{1.2}
\]

For every `s in {1,2}` and `1<=j<=d`, choose distinct

\[
 x_{s,j}\in C_j
\]

and fresh, mutually distinct coordinates `y_(s,j)` outside `B` and the
active bank (1.1).  Put

\[
 C_j^s=(C_j-\{x_{s,j}\})+\{y_{s,j}\},
 \qquad
 \mathcal C^s=(C_1^s,\ldots,C_d^s),                         \tag{1.3}
\]

and write

\[
                         \mathcal C=(C_1,\ldots,C_d).       \tag{1.4}
\]

A convenient sufficient supply condition is

\[
 |B|\ge2d,
 \qquad
 |[k]\setminus B|\ge2d+9.                                  \tag{1.5}
\]

It permits the preceding partition with `|C_j|>=2` and holds eventually in
the central regime because `d=Theta(sqrt(k))`.
The generous disjointness in (1.5) is used only to make the collision proof
literal; it is not asserted to be sharp.

Define four screen types at each port:

\[
\begin{aligned}
 A_i&=\{b,a_i\},
 &D_i&=\{a_{i-1},a_i\},\\
 P_i&=\{a_i,c_i\},
 &Q_i&=\{c_i,a_{i+2}\}.
\end{aligned}                                               \tag{1.6}
\]

Consecutive screens in

\[
                 A_i,D_i,P_i,Q_i,A_{i+2}                    \tag{1.7}
\]

meet in exactly one coordinate.  All displayed screen sets, over all
ports and types, are distinct.

## 2. The two old source cycles

For `i in Z_4`, define the connector from role `i` to role `i+2` by the
source block

\[
 \boxed{
 A_i,\mathcal C,
 D_i,\mathcal C^1,
 P_i,\mathcal C,
 Q_i,\mathcal C^2.}
\tag{2.1}
\]

The next source letter after (2.1) is `A_(i+2)`, followed by the base
history `mathcal C`.  Concatenate the blocks for `i=0,2` cyclically to form
one source circuit `W_even`, and those for `i=1,3` to form a second circuit
`W_odd`.  Each circuit has length `8(d+1)`, and together they use

\[
                              16(d+1)                       \tag{2.2}
\]

source positions.

Let `D` denote consecutive union, so the owner row is `D^d W`.

### Lemma 2.1 (rank and Johnson law)

Every length-`d+1` source interval in the two circuits has rank `r`, and
successive owner values are distinct Johnson neighbours.

#### Proof

The source word alternates one two-coordinate screen with an ordered
`d`-block core partition.  Consecutive core partitions are either
`mathcal C -> mathcal C^s` or its reverse.  In block `j` they differ by
the one swap

\[
                         x_{s,j}\longleftrightarrow y_{s,j}.
\]

A length-`d+1` window contains exactly one screen.  In every core block it
contains exactly one of the old or new block versions, never both.  Its
core union therefore has rank `r-2`, and the disjoint screen raises the
rank to `r`.

When the start passes a screen, the owner swaps the one noncommon active
coordinate of two consecutive screens in (1.7).  At every other step it
swaps `x_(s,j)` for `y_(s,j)` or conversely.  Hence every owner step is
a loopless Johnson edge.  Strict change at every step also proves adjacent
distinctness.  `square`

### Lemma 2.2 (global owner and q1 simplicity)

Across both old source circuits, all `16(d+1)` owners are distinct.  Their
rank-`(r-1)` lower colours and rank-`(r+1)` upper colours are also pairwise
distinct.

#### Proof

Every owner has an active trace equal to one screen in (1.6), because no
active coordinate occurs in a core block.  Distinct screens therefore
separate owners belonging to different screen runs.  Within one screen
run, the prefix of its `y` bank determines the transition stage,
so those owners are distinct as well.

On a core-swap edge, the lower and upper colours contain exactly two active
coordinates.  Their prefix/suffix profile, their unique active screen, and
the bank index `s` recover the edge.  On a screen-swap edge, the lower colour
contains exactly one active coordinate and the upper colour exactly three,
so neither can collide with a core-swap colour.

It remains only to compare screen-swap edges with one another.  The old
hinge `A_i D_i` has base core `B` and common active coordinate `a_i`.
The edge `D_i P_i` has the changed core from bank `1`, the edge
`P_i Q_i` has base core and common coordinate `c_i`, and `Q_i A_(i+2)` has
the changed core from bank `2`.  Thus the common active coordinate
together with the base/changed-core bank recovers the edge.  The same data
and its three-coordinate active union recover every upper colour.  Private
`c_i` labels and the active `a_i` profiles separate different ports.
`square`

Consequently the old owner graph consists of exactly two simple q1-rainbow
cycles.

## 3. The common-history rethread

At role `i`, the selected literal fragment is

\[
                         A_i,\mathcal C,D_i.          \tag{3.1}
\]

All four roles therefore have the same ordered history `mathcal C`.  Cut
after that history and attach to role `i` the complete continuation which
formerly began at `D_(i+1)`.

The old hinge owners are

\[
 L_i=B+A_i=B+b+a_i,
 \qquad
 R_i=B+D_i=B+a_{i-1}+a_i.                            \tag{3.2}
\]

The new hinge at role `i` is `L_i R_(i+1)`.  Its lower colour is

\[
                         L_i\cap R_{i+1}=B+a_i,       \tag{3.3}
\]

the same as the old lower colour at role `i`, while its upper colour is

\[
                         L_i\cup R_{i+1}
                              =B+b+a_i+a_{i+1},       \tag{3.4}
\]

the old upper colour at role `i+1`.

### Theorem 3.1 (literal two-component `C8` collar)

The rethread above:

1. turns the two old source/owner cycles into one cycle;
2. preserves the complete owner multiset;
3. preserves every lower-q1 colour pointwise and cyclically permutes the
   four changed upper-q1 colours;
4. preserves all other q1 resources literally;
5. preserves the occurrence-labelled multiset of every source interval of
   width at most `d+1`;
6. transports every strict-lower interval occurrence and every matching on
   those occurrences; and
7. adds and deletes no source or owner position.

Both phases remain owner-simple and globally q1-simple.

#### Proof

In the old state, the complete continuation beginning at `D_i` reaches
the next selected role `i+2`; hence the old next-role permutation is

\[
                         \sigma=(0\ 2)(1\ 3).        \tag{3.5}
\]

The head assignment is `tau=(0 1 2 3)`.  Therefore the new next-role
permutation is

\[
                         \tau\sigma=(0\ 3\ 2\ 1),   \tag{3.6}
\]

one cycle.  Equations (3.2)--(3.4) are exactly the common-history `C8`
owner/q1 identity.  Every connector edge is carried with its complete
continuation and is unchanged.

All four cuts lie at the same literal order-`d` de Bruijn vertex.  Euler
reassembly at one vertex gives an occurrence bijection for source subwords
of width at most `d+1`.  Every owner window has rank `r`, so an interval
whose union has rank below `r` has width at most `d`; the same bijection
therefore transports the entire strict-lower deck and any
occurrence-labelled matching on it.  Position count is unchanged.

Lemma 2.2 proves simplicity before the move.  The only new edges are the
four hinges.  Their lower resources are the same occurrences and their
upper resources are permuted by (3.4), so simplicity also holds afterward.
`square`

## 4. Exact biresidence

### Theorem 4.1 (positive and zero runs are multiples of `d+1`)

In both the old and new owner phases, every nonconstant positive run and
every nonconstant zero gap of every coordinate has length divisible by
`d+1`.  In particular both phases satisfy the positive- and zero-residence
floor `d+1`.

#### Proof

Index source positions modulo `d+1`, taking screens at residue zero and
the `j`th core block at residue `j`.  Active coordinates occur only in
screens.  Every coordinate of a base or changed core block occurs only in
one fixed block index.  Hence all source occurrences of any fixed
coordinate lie in one residue class modulo `d+1`, before and after the
rethread.

An occurrence at source position `p` is present in exactly the `d+1`
owner windows whose starts lie from `p-d` through `p`.  Consecutive source
occurrences of a coordinate are separated by `t(d+1)` for an integer
`t>=1`.  If `t=1`, their owner arcs meet and form one longer positive run.
If `t>=2`, the intervening zero gap has length

\[
                  t(d+1)-(d+1)=(t-1)(d+1).          \tag{4.1}
\]

Thus every positive component and every nonempty zero component has length
a positive multiple of `d+1`.  `square`

This closes zero-gap residence as well as the positive residence supplied
abstractly by common-history reassembly.

## 5. A polynomial internal upper-damage bank

The local theorem is not all-width transparent, but its complete internal
damage set is much smaller than the ambient upper cone suggests.

### Corollary 5.1 (internal casualties are `O(d^2)` and start at rank `r+2`)

Let `D_up` be the set of targets which occur as cyclic owner-interval
unions in the old two collar cycles but have no cyclic owner-interval
witness in the fused collar cycle.  Then

\[
 |D_{\rm up}|\le 128(d+1)^2,                                \tag{5.1}
\]

and every member of `D_up` has rank at least `r+2`.

#### Proof

Each old cycle has length `L=8(d+1)`.  It has at most `L^2`
occurrence-labelled nonempty cyclic intervals, so the union of the two old
decks has at most `2L^2=128(d+1)^2` values.  This proves the cardinality
bound without any multiplicity assumption.

The common-history theorem transports every interval of source width at
most `d+1`.  Every untransported value contains one old rank-`(r+1)` hinge
union `U_i`.  If its rank is `r+1`, it equals `U_i`; but the four hinge
upper colours are merely permuted by (3.4), so `U_i` still has a new q1
witness.  Hence an actual casualty has rank at least `r+2`.  `square`

Thus a bank of at most `128(d+1)^2=O(k)` protected alternative occurrences
would make the **isolated cyclic collar deck** upper-safe.  This does not
bound values of longer intervals created after the collar is opened and
grafted into external PBBS bodies; those intervals can carry arbitrary
exterior coordinates and remain the separate cone/interface in Section 7.

## 6. Protected q1-factor planting

Each owner edge corresponds to two consecutive incidences in the
middle-level containment graph.  The old collar therefore occupies

\[
                         32(d+1)                    \tag{6.1}

protected incidence edges and has maximum protected degree two.  The
fixed-`H` collar extension theorem consequently gives the following.

### Corollary 6.1 (prospective owner/q1 host)

Specialize the owner rank to `r=m` on a `[2m-1]` ground set.  At that
central level, if

\[
                         32(d+1)\le m-2,             \tag{6.2}

then the complete old two-cycle collar extends to an exact spanning q1
two-factor.  Switching the collar to its new phase leaves a valid exact q1
two-factor and reduces its component count by one.

The collar cycles are saturated components of that extension.  This
corollary does **not** attach them to two prescribed pre-existing PBBS
components.  Such an attachment needs an open protected endpoint-pairing
or grafting theorem.

## 7. Remaining interfaces

The construction removes three local uncertainties from the abstract
`C8` frontier:

* the four equal histories are simultaneously literal;
* all intermediate owners and immediate colours are collision-free; and
* zero-gap residence is automatic, not an additional collar condition.

It does not prove the all-dimensional upper bound.  The remaining global
interfaces are now precise.

1. **Protected grafting.**  Open the two old collar cycles and graft their
   four sockets into two named large PBBS components while retaining the
   same cut permutation.  The unrooted q1-factor extension does not choose
   these endpoint pairings.
2. **Arbitrary-width upper witnesses.**  Common-history transport is exact
   through source width `d+1`, but longer intervals crossing a changed
   hinge still need a protected witness bank or a monotone whole-component
   theorem.
3. **Typed common cap and opening.**  The terminal literal target-to-cell
   routes and a quiet linear opening must coexist with the grafted collar.

Thus the local endpoint replacement demanded by the rigid-PBBS
common-history no-go now exists explicitly.  What remains is no longer a
source-factorization problem; it is the correlated global grafting and
upper/cap protection problem.

## 8. Dependencies

The abstract crossover and short-deck transport are in

`MATH_THEOREM_TWO_COMPONENT_COMMON_HISTORY_C8_CROSSOVER_AND_MINIMALITY_20260805.md`

and

`MATH_THEOREM_COMMON_DEBRUIJN_VERTEX_SHORT_DECK_FUSION_20260805.md`.

The protected q1-factor extension used in Corollary 6.1 is in

`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.
