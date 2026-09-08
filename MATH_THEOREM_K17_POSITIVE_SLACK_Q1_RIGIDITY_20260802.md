# K17 positive staircase slack does not buy a large lower-q1 defect

**Date:** 2026-08-02  
**Status:** unconditional obstruction induced by the rank-nine witness
intervals of any hypothetical length-`B(17)` word.  Chain alignment and a
pre-existing Johnson carrier are not assumed.  The result does not construct
a K17 word.

## 0. Verdict

Put

\[
 W=\binom{17}{9}=24310,
 \qquad L=W+3=24313.
\]

An arbitrary-start/deadline schedule can have as many as `7401` extra lower
cells.  That scalar surplus does **not** permit a rank-nine Johnson owner
path to omit `7401` immediate-lower colours.

For every legal arbitrary-start/deadline schedule which can cover the
rank-eight layer, all but at most `6` rank-eight targets must be consecutive
owner intersections.  Equivalently, if

\[
 T_0,T_1,\ldots,T_{W-1}
\]

is the order of one selected witness interval for every rank-nine target,
then at least `W-6` consecutive pairs are Johnson edges and their
intersections are distinct:

\[
 \boxed{
 \left|\{T_{i-1}\cap T_i:1\le i<W\}\right|
 \ge W-6=24304.}
\tag{0.1}
\]

For the maximum-surplus schedule

\[
 I_i=[i,i+3],
\tag{0.2}
\]

the sharper bound is `W-4=24306`.

Thus positive staircase slack relaxes the **occurrence** bijection (cells
may duplicate or have rank at least nine), but it does not provide a broad
escape from lower-q1 rainbowness.  A resident Hamilton owner path outside
the current exact-q1 factor class is useful only if it is already
q1-rainbow up to a constant-size exceptional bank.

## 1. Lower cells are grouped by physical left endpoint

Choose one witnessing interval for each of the `W` rank-nine targets.  Two
such intervals cannot contain one another: containment would make their OR
values nested, while two distinct rank-nine sets are incomparable.  Ordering
the witnesses by left endpoint therefore also orders them strictly by right
endpoint.  Write them as

\[
 I_i=[s_i,q_i],\qquad 0\le i<W,
\]

where starts and deadlines are strictly increasing.  Write the three
omitted starts and deadlines as

\[
 x_j=\alpha_j+j-1,
 \qquad y_j=\tau_j+j-1,
 \qquad 1\le j\le3,
\]

using the usual nondecreasing threshold vectors.  Legality is

\[
 \tau_j\le\alpha_j.
\tag{1.1}
\]

No chain-alignment hypothesis is used below.

Every interval whose OR has rank at most eight avoids containing an owner
interval.  For a fixed physical left endpoint `p`, all such intervals form
one nested chain.  Therefore one left-endpoint chain contains at most one
**distinct** rank-eight value.  Since there are `W` rank-eight targets, a
universal word necessarily has

\[
 N_1\ge W,
\tag{1.2}
\]

where `N_1` is the number of nonempty atlas chains.

For `d=3`, the exact staircase count rewrites (1.2) as

\[
 \left|\bigcup_{j=1}^3[\tau_j,\alpha_j)\right|\ge W-3.
\tag{1.3}
\]

This is the rank-eight part of the rank-chain condition; it uses no Hall or
compiler assumption.

## 2. Clean selected starts can deliver only q1 colours

Call a selected start `s_i`, with `1\le i<W`, **clean** when

\[
 q_i=q_{i-1}+1,
 \qquad s_i\le q_{i-1}.
\tag{2.1}
\]

The first condition says that no deadline hole lies between the two rows;
the second says that the rows genuinely overlap rather than merely abut.

### Lemma 2.1 (clean-chain containment and forced Johnson edge)

Every lower cell beginning at a clean selected start `s_i` is contained in

\[
 I_{i-1}\cap I_i=[s_i,q_{i-1}].
\tag{2.2}
\]

Consequently, if its literal OR is a rank-eight target `S`, then

\[
 S=T_{i-1}\cap T_i.
\tag{2.3}
\]

In particular, `T_{i-1}` and `T_i` are Johnson-adjacent.

#### Proof

The first owner start at or after `s_i` is `s_i` itself.  Hence the maximal
lower interval with that left endpoint ends at `q_i-1`.  Under (2.1),

\[
 [s_i,q_i-1]=[s_i,q_{i-1}]=I_{i-1}\cap I_i.
\]

Every shorter cell in the same chain is contained in this overlap.  Every
physical letter in the overlap is subordinate to both owner caps, so its
OR `S` is contained in `T_{i-1}\cap T_i`.  The two selected owner values
are distinct rank-nine sets, so their intersection has rank at most eight.
Since it contains the rank-eight set `S`, it equals `S`.  Equality of the
intersection rank to eight is exactly Johnson adjacency.  \(\square\)

This lemma is cap-independent: shrinking the maximal envelope can destroy
an occurrence, but cannot turn a clean chain into a different rank-eight
colour.

## 3. There are at most six exceptional chains

Put

\[
 h_i=|\{j:\tau_j\le i\}|,
 \qquad g_i=|\{j:\alpha_j\le i\}|.
\]

The lower chain at a selected start `s_i` is nonempty exactly when

\[
 q_i>s_i
 \quad\Longleftrightarrow\quad
 h_i>g_i
 \quad\Longleftrightarrow\quad
 i\in U:=\bigcup_{j=1}^3[\tau_j,\alpha_j).
\tag{3.1}
\]

For `i\ge1`, the overlap size at transition `i` is

\[
 q_{i-1}-s_i+1=h_{i-1}-g_i.
\tag{3.2}
\]

Suppose a selected-start chain is nonempty and `i` is not one of the three
threshold values `\tau_j`.  Membership in `U` then gives
`\tau_j<i<\alpha_j` for some `j`, so (3.2) is positive.  Also no deadline
threshold occurs at `i`, and hence

\[
 q_i-q_{i-1}=1+h_i-h_{i-1}=1.
\tag{3.3}
\]

Thus every nonempty selected-start chain whose row index is not a threshold
is clean.  This statement includes the left boundary: if the chain at
`s_0` is nonempty, then `0\in U`, which forces some `\tau_j=0`.  Therefore
all exceptional **selected-start** chains occur at threshold indices, and
there are at most three of them.

The other physical starts are precisely the three omitted starts.  Whether
or not all of their atlas chains are nonempty, they add at most three more
exceptions.  Hence the total exceptional-chain count is at most

\[
 3+3=6.
\tag{3.4}
\]

### Theorem 3.1 (arbitrary-staircase q1 rigidity)

Assume a nonempty word of length `W+3` covers every rank-nine target and
every rank-eight target.  Choose and order one witness interval for every
rank-nine target as in Section 1.  Then at least `W-6` consecutive witness
pairs are Johnson-adjacent, and their intersections are `W-6` distinct
rank-eight targets.

#### Proof

Every rank-eight target witness belongs to one left-endpoint atlas chain.  A chain
contains at most one distinct rank-eight value.  By Lemma 2.1, every value
in a clean selected-start chain forces a Johnson edge and is its
intersection.  Section 3
leaves at most six other chains.  Hence at most six rank-eight targets
can lie outside the edge-intersection palette.  \(\square\)

The number `6` is sharp for the abstract schedule count (the independent
small-parameter audit in Section 9 attains `2d`), though simultaneous
literal rank-eight service in all exceptional chains is not asserted.  The
exact schedule-specific exceptional count is at most

\[
 3+|\{\tau_j:1\le j\le3\}|\le6.
\tag{3.5}
\]

Since the ordered witness row has only `W-1` consecutive transitions,
Theorem 3.1 also says that at most

\[
 (W-1)-(W-6)=5
\]

transitions can fail to be distinct-colour Johnson steps.  The sixth
exception is the unavoidable linear boundary port.

### Corollary 3.2 (odd-dimensional form)

The same proof with `d` omitted starts and deadlines gives the following.
For odd `k=2r-1`, let `W=\binom{k}{r}`.  If a length-`W+d` word covers the
complete rank-`r` and rank-`(r-1)` layers, order one selected witness for
every rank-`r` target.  Then

\[
 \left|\{T_{i-1}\cap T_i:1\le i<W\}\right|
 \ge W-2d.
\tag{3.6}
\]

Equivalently, at most `2d-1` consecutive witness transitions fail the
distinct-colour Johnson condition.

Indeed, the `d` omitted physical starts give at most `d` exceptional chains.
Among selected starts, every nonempty non-threshold chain is clean by the
same calculation as (3.1)--(3.3), leaving at most the `d` threshold
indices.  These are all possibilities.

For the OR lower bound, `d=Theta(sqrt(k))`.  Thus even in general odd
dimension, scalar staircase slack can relax the forced Johnson/q1 spine by
only `O(sqrt(k))` transitions, not by a positive fraction of the middle
layer.

## 4. Maximum scalar slack gives only four exceptional chains

The zero-loss schedule is

\[
 \alpha=(W,W,W),\qquad \tau=(0,0,0),
\]

so every owner interval is `I_i=[i,i+3]`.  It has

\[
 \Omega=7401
\]

extra lower cells.  Nevertheless, for every physical start
`1\le p\le W-1`, every lower cell beginning at `p` is contained in

\[
 I_{p-1}\cap I_p=[p,p+2].
\]

Only the initial start and the three final omitted starts are exceptional.
Thus

\[
 \boxed{|\text{q1 palette}|\ge W-4.}
\tag{4.1}
\]

This also explains why the tempting rank-only use of `7401` pair cells is
not literal.  Inside a clean chain a rank-eight pair is contained in the
rank-eight owner intersection above it, so it repeats that same q1 colour;
it cannot deliver a missing colour.  The local five-letter obstruction to
two consecutive rank-eight pairs is consistent with, but weaker than, this
global containment statement.

## 5. What positive slack actually changes

Let `\mathcal C` be the complete lower atlas and put

\[
 \Omega=|\mathcal C|-65535.
\]

For a subordinate word `Q`, retain the spectral quantities

\[
 H_Q=\#\{\text{missing lower targets}\},
\quad
 D_Q=\text{duplicate excess},
\quad
 R_Q=\#\{\text{atlas cells of rank at least nine}\}.
\]

The exact identity remains

\[
 H_Q=D_Q+R_Q-\Omega.
\tag{5.1}
\]

Hence positive slack permits duplicate q1 occurrences, rank-at-least-nine
atlas cells, guard-dead cells paid from `\Omega`, and non-top occurrences of
an already present q1 colour.  Theorem 3.1 shows that it does **not** permit
a large set of absent q1 colours, because the missing colours have no
physical rank-eight chain on which to appear.

The exact lower compiler for a candidate chronology must still provide:

1. a literal occurrence for every rank-eight colour, with at most the
   exceptional bank in (3.5) outside clean overlap chains;
2. all ranks one through seven in the remaining cells;
3. nonempty simultaneous caps which replay every selected owner; and
4. `D_Q+R_Q=\Omega` (equivalently `H_Q=0`).

For upper transfer, chain alignment reduces the requirement to the same
one as in the flat theorem: every rank-ten-through-seventeen target must be
a consecutive union of selected owner rows, together with any explicitly
audited mixed-boundary gap family.  Scalar lower slack proves none of these
upper witnesses.

## 6. Consequence for the 3,807-cut resident-rejoin route

Deleting a `3,807`-edge residence stabbing set from an exact-q1 owner factor
retains `W-3807` distinct q1 colours.  Rejoining the blocks with arbitrary
Johnson seams would therefore leave as many as `3,807` colours missing.
Although

\[
 3807<7401,
\]

Theorem 3.1 shows that scalar slack cannot pay this deficit in any
arbitrary-start rank-nine witness schedule: at least `3,801` of those
colours must be restored by the rejoin (and more under a sharper
schedule-specific count).  The lower-colour partition row in the rejoin
master therefore cannot be discarded merely because the scalar catalogue
has `7401` extra cells.

This does not say that all new seams must use distinct cut colours in one
particular occurrence model.  It says that the **final distinct q1 palette**
must miss at most the constant exceptional bank.

## 7. Why the K16 nonflat certificate is not a counterexample

The exact K16 word uses a genuine mixed-depth facet bridge:

\[
 6386\text{ marked middle targets at depth }2,
 \qquad
 49\text{ marked bridge targets at depth }3.
\]

K16 is even-dimensional.  Its middle layer has size

\[
 \binom{16}{8}=12870,
\]

whereas its immediate lower layer has size only

\[
 \binom{16}{7}=11440.
\]

The equal-size pressure used in Theorem 3.1 is therefore absent: `1430`
middle-start chains need not carry a rank-seven target.  The 49-term bridge
is consistent with that spare population.

For odd K17 the two adjacent central layers both have size `W`.  Changing
derivative depth does not evade the theorem: after any hypothetical word is
built, selecting one witness interval for every rank-nine target recreates
the monotone interval row of Section 1.  A K16-style mixed-depth bridge can
therefore create at most six non-q1 rank-eight deliveries at K17, unless it
also leaves the length-`W+3`/complete-rank-eight hypotheses.

## 8. Scope and relation to the corrected two-zone work

This note does not use the retracted uniform four-window interpretation of
the alternating two-zone prefix.  The corrected live prefix uses triple
owners followed by quadruple owners and remains an occurrence-labelled
upper-rainbow path problem.

The theorem assumes only a length-`W+3` word which covers the complete
rank-nine and rank-eight layers.  Selecting one witness per rank-nine target
automatically creates the monotone interval row.  Johnson adjacency and
chain alignment are conclusions/extra upper structure, not hypotheses.

The result does not force a literal top-cell bijection: positive slack may
move or duplicate occurrences of an already forced q1 colour.  Nor does it
prove ranks one through seven, upper completeness, residence, or the common
cap.  It proves the narrower but global fact needed here: neither an
arbitrary start/deadline choice nor a mixed-depth reinterpretation permits
more than six rank-eight colours outside the forced Johnson spine.

## 9. Independent finite schedule audit

The C++ audit

```text
scratch/audit_k17_positive_slack_q1_rigidity_20260802.cpp
SHA-256 8474e5bebeb936335059b3ef4b869a7ce1b3bbc0499cfc4a52bfd8be8967fab6
```

enumerates every pair of nondecreasing threshold vectors for

```text
1 <= d <= 4,  max(2,d) <= W <= 11.
```

It independently reconstructs starts, deadlines, literal atlas-chain
nonemptiness, selected/omitted starts, and clean-chain status.  It does not
filter on chain alignment.  It checks

\[
 N_1=d+\left|\bigcup_j[\tau_j,\alpha_j)\right|
\]

and the bound `exceptional <= 2d` on every schedule with `N_1>=W`.
The authenticated H100 run checks `784105` such schedules and reports

```text
W=3,...,11 d=3 max_exceptional=6
PASS tested=784105 global_max_exceptional=8
```

The audit is only a finite adversarial check of the schedule arithmetic;
the proof of Theorem 3.1 is the argument above.
