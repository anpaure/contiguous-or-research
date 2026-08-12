# Variable-support facet rings and a literal consecutive-size rectangle fusion

**Date:** 2026-08-07  
**Method:** cyclic support intervals and complete-bipartite star trades  
**Status:** theorem.  This gives an owner-once literal facet ring at every
length in a full interval, lifts the consecutive-size owner trade to an exact
state-balanced source trade, and computes its complete proper-target damage.
It does not select a whole-layer star decomposition or make the trade
upper/target transparent.

## 1. Setup

Let the ground set have size

\[
                         n=2r-1,
\]

and let the owner-window length be

\[
                         D=d+1.
\]

Fix an integer

\[
                         D+1\le \ell\le r+1             \tag{1.1}
\]

and put

\[
                         a=\ell-D.
\]

Choose a core `K` and a cyclically ordered private set

\[
 K\cap F=\varnothing,\qquad
 |K|=r-\ell+1,\qquad
 F=(f_t)_{t\in\mathbb Z_\ell},\qquad |F|=\ell .       \tag{1.2}
\]

At phase `t`, use the source letter

\[
 A_t=K\cup\{f_{t-a+1},f_{t-a+2},\ldots,f_t\},        \tag{1.3}
\]

where subscripts are cyclic.  Thus every private coordinate is supported on
exactly `a` consecutive source phases.  Call (1.3) the **support-`a` facet
ring**.

## 2. Every admissible length gives the same saturated rank profile

### Theorem 2.1 (variable-support facet ring)

For every `ell` satisfying (1.1), the source ring (1.3) has all of the
following properties.

1. For every `1<=q<=D`, the union of `q` consecutive source letters is

   \[
   Z_{t,q}=K\cup
       \{f_{t-q-a+2},f_{t-q-a+3},\ldots,f_t\},         \tag{2.1}
   \]

   and hence

   \[
                       |Z_{t,q}|=r-D+q.                \tag{2.2}
   \]

2. The `D`-windows are the `ell` distinct rank-`r` facets

   \[
             O_t=Z_{t,D}=(K\cup F)-\{f_{t+1}\}.       \tag{2.3}
   \]

   In particular, they form a simple Johnson cycle and use every owner in
   this facet block exactly once.

3. At every proper width `1<=q<D`, the `ell` targets `Z_(t,q)` are pairwise
   distinct.  Targets belonging to different widths have different ranks.

4. The source is one literal state-balanced cyclic component.  Its rank
   profile (2.2) is independent of `ell`.

#### Proof

The union of `q` consecutive cyclic intervals of length `a`, whose starts
advance one phase at a time, is one cyclic interval of length `a+q-1`.
For `q<=D`,

\[
                         a+q-1\le a+D-1=\ell-1,
\]

so no private label is counted twice and (2.1) holds.  Using (1.2),

\[
 |Z_{t,q}|=(r-\ell+1)+(a+q-1)=r-D+q,
\]

which proves (2.2).

At `q=D`, the private interval has length `ell-1` and misses precisely
`f_(t+1)`, proving (2.3).  Consecutive owners delete different private
labels from the common `(r+1)`-set `K union F`, so they are Johnson adjacent
and all owners are distinct.

For `q<D`, the private interval in (2.1) has a proper nonzero length less
than `ell`; it therefore recovers its cyclic endpoint `t`.  This proves
same-width injectivity.  Equation (2.2) separates different widths.  Finally,
cyclic translation sends every literal state to its successor, proving state
balance. \(\square\)

### Two boundary cases

* `ell=D+1` gives `a=1`, the usual all-high facet ring with singleton
  private letters.
* `ell=D+2` gives the previously missing consecutive-size facet ring

  \[
                         A_t=K\cup\{f_{t-1},f_t\}.      \tag{2.4}
  \]

  Its owner windows are still all the facets of `K union F`, rather than
  the adjacent-pair-complement cycle produced by the one-pivot primitive
  source.

The immediate-upper union of two consecutive owners is always `K union F`.
Thus a facet ring is deliberately upper-collapsed; Theorem 2.1 is an owner
and lower-profile theorem, not an upper-rainbow theorem.

## 3. Pure pull blocks survive at every compatible length

Choose `J subset K`, `|J|=delta`, and a cyclic low/high schedule

\[
                 \mathsf L^j\mathsf H,
 \qquad 1\le j\le d,\qquad j+1\mid\ell .              \tag{3.1}
\]

Replace (1.3) by

\[
 A_t=
 \begin{cases}
 (K-J)\cup\{f_{t-a+1},\ldots,f_t\},&t\text{ low},\\
 K\cup\{f_{t-a+1},\ldots,f_t\},&t\text{ high}.
 \end{cases}                                           \tag{3.2}
\]

### Theorem 3.1 (length-free pure pull realization)

The word (3.2) is one state-balanced owner-once facet ring with the same
owner inventory (2.3).  Relative to the all-high profile, its per-phase
proper-window correction is

\[
                         {1\over j+1}S_{\delta,j},       \tag{3.3}
\]

independently of `ell`.  At every proper width all literal target values in
one ring are distinct.

#### Proof

Every low run has length `j<=d=D-1`, so every `D`-window contains a high
phase and restores all of `K`.  The private-label calculation in Theorem 2.1
is unchanged, hence the owners remain (2.3).

A `q`-window loses `J` exactly when it lies wholly in a low run.  In each
period of `j+1` phases this happens `j-q+1` times for `q<=j`, and never for
`q>j`.  This is exactly the staircase tile `S_(delta,j)`, divided by the
period, proving (3.3).  The number of periods `ell/(j+1)` cancels from the
per-phase profile.

For any interval, its intersection with `F` is the cyclic interval in
(2.1).  Its length recovers the source width and its endpoint recovers the
phase.  Thus two different proper source intervals cannot have the same
literal union, whether or not `J` is present. \(\square\)

### Consequence for the fractional pull factor

For a pure type `(delta,j)`, one is no longer restricted to the shortest
multiple of `j+1` above `D+1`.  Every multiple

\[
                 \ell\equiv0\pmod{j+1},
 \qquad D+1\le\ell\le r+1                            \tag{3.4}
\]

has exactly the same normalized staircase contribution.  Thus packet length
is a free integral owner variable at the fractional rank-profile level.
Named-target and upper-palette correlations remain separate.

## 4. Complementation and the literal rectangle trade

Complement rank-`r` owners.  Formula (2.3) becomes the star

\[
                         \{G+f:f\in F\},               \tag{4.1}
\]

where `|G|=r-2`.  By Theorem 2.1, **every** star size
`ell in [D+1,r+1]` has a literal state-balanced depth-`d` realization with
the same saturated proper-rank profile.

Fix an integer `p` with

\[
                         D+1\le p<p+1\le r+1           \tag{4.2}
\]

and assume

\[
                         2p\le r+1.                    \tag{4.3}
\]

Choose disjoint sets

\[
 |S|=r-3,\qquad |A|=p,\qquad |B|=p+1.                 \tag{4.4}
\]

The owner rectangle

\[
             \mathcal X(S;A,B)
                =\{S+\{a,b\}:a\in A,\ b\in B\}       \tag{4.5}
\]

has the two star decompositions

\[
 \begin{aligned}
 \mathcal D_B
   &=\bigl\{\{S+b+a:a\in A\}:b\in B\bigr\},\\
 \mathcal D_A
   &=\bigl\{\{S+a+b:b\in B\}:a\in A\bigr\}.
 \end{aligned}                                         \tag{4.6}
\]

The first consists of `p+1` stars of size `p`; the second consists of `p`
stars of size `p+1`.

### Theorem 4.1 (literal consecutive-size rectangle fusion)

Both decompositions in (4.6) lift to literal state-balanced depth-`d`
source rings.  Replacing `D_B` by `D_A`:

1. preserves the complete owner inventory (4.5) exactly;
2. preserves the total number `p(p+1)` of proper-window occurrences at
   every width and preserves their rank `r-D+q`;
3. preserves literal cyclic state balance componentwise; and
4. reduces the number of source-ring components from `p+1` to `p`.

Hence the complete-bipartite consecutive-size trade is a genuine literal
owner-neutral component-reducing move, not merely an owner-set arithmetic
identity.

#### Proof

Every star in `D_B` has size `p` and every star in `D_A` has size `p+1`.
Conditions (4.2)--(4.3) make both lengths admissible in Theorem 2.1 and make
the labelled rectangle fit on `[n]`.  Apply Theorem 2.1 separately to every
star.  Equation (4.6) proves exact owner equality.  A length-`ell` ring has
`ell` occurrences at each proper width, so both shores have
`p(p+1)` occurrences.  Their ranks agree by (2.2), and state balance follows
ring by ring.  The component counts are displayed in (4.6). \(\square\)

This is an owner-factor fusion actuator.  It does not assert that arbitrary
preselected cycles can be placed into one rectangle, nor that the output is
one global cycle.

## 5. Exact target-damage boundary of the rectangle

The trade in Theorem 4.1 is not lower- or upper-transparent.  The failure is
complete and can be computed exactly.

Put

\[
 C=[n]-(S\cup A\cup B),\qquad |C|=r-2p+1,              \tag{5.1}
\]

and choose arbitrary cyclic orders on `A` and `B`.  Write

\[
                         a_0=p-D.                       \tag{5.2}
\]

At proper width `1<=q<D`, the `D_B` shore emits exactly the targets

\[
 C\cup(B-\{b\})\cup I_A,
 \qquad b\in B,quad
 I_A\text{ a cyclic }(a_0+q-1)\text{-interval of }A,  \tag{5.3}
\]

whereas the `D_A` shore emits exactly

\[
 C\cup(A-\{a\})\cup I_B,
 \qquad a\in A,quad
 I_B\text{ a cyclic }(a_0+q)\text{-interval of }B.    \tag{5.4}
\]

### Theorem 5.1 (complete proper-target turnover)

For every `1<=q<D`:

1. each family (5.3) and (5.4) has exactly `p(p+1)` distinct targets;
2. the two families are disjoint; hence
3. the rectangle switch has proper-target symmetric difference exactly

   \[
                              2p(p+1)                   \tag{5.5}
   \]

   at that width.

The immediate-upper inventories are also disjointly polarized:

\[
 \begin{array}{c|c}
 \mathcal D_B & p\text{ copies of }[n]-(S+b),\quad b\in B,\\
 \mathcal D_A & (p+1)\text{ copies of }[n]-(S+a),\quad a\in A.
 \end{array}                                           \tag{5.6}
\]

#### Proof

For (5.3), intersection with `B` recovers the unique missing label `b`, and
intersection with `A` recovers the proper cyclic interval `I_A`.  Hence all
targets are distinct.  The same argument applies to (5.4).

A target in (5.3) contains exactly `a_0+q-1` elements of `A` and `p`
elements of `B`.  A target in (5.4) contains `p-1` elements of `A` and
`a_0+q` elements of `B`.  Equality would force

\[
                  a_0+q-1=p-1,
 \qquad           a_0+q=p,
\]

and hence `q=D`, contrary to `q<D`.  Thus the two proper-target families are
disjoint, proving (5.5).

Consecutive owners in one facet ring have union equal to its common
rank-`(r+1)` facet set.  For the star centred at `S+b` this set is
`[n]-(S+b)` and occurs once per owner, hence `p` times.  The other shore is
identical with `a` and `p+1`, proving (5.6).  The two named upper families
are disjoint because `A` and `B` are disjoint. \(\square\)

Therefore Theorem 4.1 can be used safely only when the affected lower and
upper occurrences are uncommitted, are rerouted jointly, or are compiled
only after the serial fusion.  It is not a transparent post-processing move.

## 6. What this changes and what remains open

The owner-side packet catalogue is substantially larger than the previously
used fixed-length block hypergraph:

* every star length `ell in [D+1,r+1]` is literal and owner-once;
* all lengths have the identical saturated proper-rank vector;
* every pure pull type may choose any compatible multiple (3.4); and
* consecutive star sizes have an exact literal component-reducing rectangle
  trade.

Thus scalar owner divisibility and literal realization of the
consecutive-size trade are no longer independent gates.

Still open are:

1. an integral whole-layer orientation into stars of admissible lengths,
   jointly with the required pull-type histogram;
2. named-target-simple selection of those rings;
3. upper-palette compensation for (5.6); and
4. a sequence of admissible rectangles that reduces all packet cycles to
   `O(1)` components without accumulating terminal target deficiency.

The exact new fusion target is consequently a **decorated rectangle
circulation**: combine component-reducing trades so their signed target
families (5.3)--(5.4) and upper currents (5.6) cancel globally.
