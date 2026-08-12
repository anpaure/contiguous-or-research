# Adjacent necklaces: terminal-fracture cubes partition and absorb every long-run receiver

**Date:** 2026-08-05  
**Method:** a rotation-equivariant terminal normal form and the odd-group
hypercube-quotient theorem; no computation  
**Status:** unconditional.  The former injection of each all-quiet long-run
source into an already matched active phase fibre is unnecessary.  The
source, its receiver, and all simultaneous terminal fractures belong to one
canonically defined cube-quotient fibre, and that entire fibre is perfectly
matched.

## 1. Why the naive full fracture cubes do not partition

Let a positive run be paired from its terminal end, as in the standard
all-quiet convention.  It is tempting to fix an all-quiet necklace and
independently fracture every standard quiet pair

\[
                 (2z+1,1)\longleftrightarrow(2z+2,0).       \tag{1.1}
\]

The resulting tagged states do form a cube.  After forgetting the tags,
however, cubes based at different all-quiet necklaces need not be disjoint.
For example, in odd coordinate length five,

\[
 X=[1,1,1,1,0]
\]

has two standard quiet pairs.  Fracturing both gives

\[
 Y=[2,0,2,0,0].                                      \tag{1.2}
\]

But `Y` is itself all-quiet: both of its positive runs are singletons, so
its own standard-pair cube is the singleton `{Y}`.  Thus `Y` lies in two
naive fibres.  In particular, taking all standard-pair cubes cannot be used
as a matching partition without an additional normal-form rule.

The collision occurs because an internal fracture creates a new positive
run start.  Terminal fractures behave differently: they move a boundary by
one coordinate but preserve every positive-run start.  That gives the
canonical partition below.

## 2. Positive macroblocks and terminal phases

Fix an odd coordinate length `q` and a nonzero boundary composition

\[
                  x=(x_0,\ldots,x_{q-1}),\qquad \min_i x_i=0. \tag{2.1}
\]

Decompose it cyclically into **positive macroblocks**.  A macroblock starts
at a coordinate preceded by zero, contains one maximal positive run, and
then contains the nonempty zero gap preceding the next positive run.

At the end of one macroblock there are two possible terminal phases.  Fix
an integer n>=2.

* The **expanded phase** is

\[
       E(P,n,g)=(P,n-1,1,0^g),\qquad g\ge1,                 \tag{2.2}
\]

  where `P` is any (possibly empty) positive prefix.

* The **collapsed phase** is

\[
       D(P,n,g)=(P,n,0^{g+1}),\qquad g\ge1.                 \tag{2.3}
\]

Both phases have the same coordinate length, the same total chip mass,
the same macroblock start, and the same next macroblock start.  They are
joined by one literal adjacent transfer,

\[
                         E(P,n,g)\longleftrightarrow D(P,n,g). \tag{2.4}
\]

The requirement `g+1>=2` in the collapsed phase is essential.  It ensures
that expanding the first zero does not erase the zero separator and merge
two macroblocks.

For a fixed macroblock the two displayed conditions are mutually exclusive:
an expanded terminal coordinate is one, while a collapsed terminal
coordinate is at least two.  There is at most one applicable terminal
phase at that macroblock.

## 3. Canonical expansion normal form

Given `x`, replace every collapsed terminal phase (2.3) by its expanded
phase (2.2), simultaneously over all macroblocks.  Call the result `N(x)`.

### Lemma 3.1 (well-defined commuting normalization)

The map `N` is well defined on literal cyclic compositions, commutes with
rotation, and is idempotent.  Its local expansions commute.  It preserves
the cyclic set of positive-run starts.

#### Proof

At a collapsed site, one transfers a unit from the terminal coordinate
to the first of at least two following zeroes.  Hence one zero remains
before the next positive-run start.  No positive-run start is created,
deleted, or moved.  Distinct macroblocks have disjoint coordinate support,
so all local expansions commute.

After expansion the local terminal is `(n-1,1,0^g)` and is no longer a
collapsed phase.  Conversely, operations at other macroblocks do not alter
it.  Thus a second normalization does nothing.  Every part of the rule is
defined cyclically from positive runs and zero gaps, so it commutes with
rotation.  \(\square\)

Let `B=N(x)`, and let `I(B)` be the set of macroblocks of `B` ending in an
expanded phase (2.2).  Put `t(B)=|I(B)|`.  For every subset `S` of `I(B)`,
collapse exactly the sites in `S`; denote the result by `B_S`.

### Lemma 3.2 (exact fibre)

For a fixed literal normalized composition `B`,

\[
                  N^{-1}(B)=\{B_S:S\subseteq I(B)\}.           \tag{3.1}
\]

In particular this fibre is the hypercube `Q_(t(B))`, and every cube edge
is one legal adjacent chip transfer.

#### Proof

Collapsing any subset is legal, has disjoint support, leaves at least one
zero in every affected separator, and normalizes back to `B`.  This proves
one inclusion.

Conversely, if `N(x)=B`, normalization changes only collapsed phases and
does so by the inverse of (2.4).  The positive-run starts are preserved by
Lemma 3.1.  Hence every changed macroblock of `x` is obtained by collapsing
the unique expanded terminal site of the corresponding macroblock of `B`.
No other coordinate can differ.  Thus `x=B_S` for a unique subset `S`.
\(\square\)

This also proves that the terminal-fracture cubes do not overlap: their
base is the value of the function `N`.

## 4. Passing to necklace classes

Let `[B]` be a normalized necklace and let `H<=C_q` be its rotational
stabilizer.  The group `H` permutes the set `I(B)` of movable terminal
sites.  Since `q` is odd, `|H|` is odd.

### Lemma 4.1 (necklace fibre is an odd cube quotient)

The necklace classes whose normalization is `[B]` form exactly the simple
orbit graph

\[
                              Q_{t(B)}/H.             \tag{4.1}
\]

#### Proof

Normalization commutes with rotation.  If `B_S` and `B_T` are rotations of
one another, normalizing shows that this rotation stabilizes `B`; hence it
lies in `H` and sends `S` to `T`.  The converse is immediate.  A one-bit
edge is precisely (2.4).  \(\square\)

The odd-group hypercube-quotient matching theorem now applies.

### Theorem 4.2 (terminal-fracture fibre matching)

Every necklace fibre with `t(B)>=1` has a perfect matching consisting only
of terminal fracture edges (2.4), including fibres with nontrivial cyclic
stabilizer.

#### Proof

By Lemma 4.1 the fibre is `Q_(t(B))/H`, where `H` has odd order.  The
odd-group quotient theorem gives a perfect matching, and every supported
quotient edge is the literal transfer (2.4).  \(\square\)

## 5. Exact absorption of all all-quiet nonsingleton runs

In an all-quiet positive run of length at least two, the last two
coordinates form a standard quiet pair `(2z+1,1)`.  Hence that macroblock
is in the expanded phase (2.2), with `n=2z+2`.

### Corollary 5.1 (long-run companions disappear)

Every all-quiet necklace having at least one positive run of length at
least two lies in a perfectly matched terminal-fracture fibre.  In
particular this includes every former long-run source (run length at least
three), every one-step receiver

\[
              (\ldots,2z+1,1,0^g,\ldots)
       \longmapsto
              (\ldots,2z+2,0^{g+1},\ldots),          \tag{5.1}
\]

and all simultaneous receiver states obtained by fracturing several
terminal quiet pairs.

It also includes the second formerly puncturing family: every odd-mass
long-gap singleton and its marked receiver,

\[
                 (m,0^{g+1})\longleftrightarrow(m-1,1,0^g),
       \qquad m\ge3\text{ odd},\quad g\ge1.           \tag{5.2}
\]

Indeed (5.2) is simply the same terminal bit with n=m.  More generally,
the theorem absorbs this pair for every m>=2, with no parity restriction.

Thus no receiver is deleted from a separately matched active phase fibre:
the entire canonical fracture fibre, including the source and receiver
shores, is matched at once.

#### Proof

The normalized base has at least one expanded terminal site, so `t(B)>=1`.
Apply Theorem 4.2.  The receiver in (5.1) is simply the opposite value of
that terminal bit and has the same normalized base.  \(\square\)

The improvement over the former injective receiver theorem is a quantifier
change.  That theorem selected one source edge and then had to repair the
matching puncture at its endpoint.  Here no endpoint is imported into a
different fibre: a disjoint partition into full fibres is matched first.

## 6. Exact residual normal form

After all `t(B)>=1` fibres are removed, a remaining necklace is normalized
and has no expanded terminal phase.  Equivalently, at every positive
macroblock:

1. if the following zero gap has length at least two, the positive run is
   the singleton `[1]`; and
2. if the positive run has length at least two, its terminal value is not
   one and its following zero gap has length exactly one.

Indeed a gap of length at least two together with terminal value at least
two is a collapsed phase, while a run of length at least two ending in one
is an expanded phase.  These exhaust the alternatives.

In particular an all-quiet residual necklace has **only singleton positive
runs**, and every long-gap singleton of mass at least two is gone as well.
The two unbounded receiver banks have not merely been injected one
codimension deeper; both were absorbed in their full fibres.

This residual description is compatible with the later macroblock/barrier
reduction, but it does not by itself match every non-all-quiet residual
state.

## 7. Relation with full allocation rails

For a *tagged* pair of terminal coordinates with fixed total mass `m`, the
allocations

\[
                       (m-a,a),\qquad 0\le a<m,       \tag{7.1}
\]

form the path `P_m`.  Several tagged terminal pairs form a Cartesian
product of paths.  The odd-group Cartesian-path-quotient theorem gives a
matching of deficiency at most one, perfect as soon as one `m` is even.

The tagging cannot simply be discarded.  An expanded state with at least
two positive terminal coordinates can be interpreted either as an
allocation rail on its last two positive coordinates or, when its zero gap
has length at least two, as the collapsed endpoint of a rail using its last
positive coordinate and first zero.  These choices need not have the same
base.  Equation (1.2) is the smallest full-fracture manifestation of this
overlap.

The two-state terminal phase avoids that ambiguity because its two roles
are intrinsically recognizable:

\[
       (\text{positive},1,0^g)
       \quad\hbox{versus}\quad
       (\text{at least two},0^{g+1}).                 \tag{7.2}
\]

Thus Theorem 4.2 is the collision-free untagged consequence currently
available from the stronger path-product algebra.

## 8. Scope

Proved:

1. naive cubes over every standard quiet pair do not partition untagged
   necklaces;
2. one terminal fracture bit per positive macroblock has a canonical,
   rotation-equivariant normal form;
3. these bits partition all relevant necklaces into odd-group cube
   quotients;
4. every nontrivial fibre is perfectly matched; and
5. every all-quiet nonsingleton-run source, every former long-run receiver,
   and every long-gap singleton/receiver pair are absorbed inside those
   full fibres, with no companion puncture.

Not proved here:

1. a matching of the residual non-all-quiet normal forms from Section 6;
2. radial four-socket flexibility after reserving prescribed boundary
   vertices;
3. PBBS owner/q2-halo compatibility; or
4. any universal-word upper bound.
