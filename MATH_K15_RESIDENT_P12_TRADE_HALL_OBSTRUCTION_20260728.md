# k=15 resident-cycle-12 trade: exact carrier obstruction

## Setup

Start with the 17-cycle all-shadow carrier
`scratch/k15_dual_descent_a4_step19.segments.json`.  Replace physical cycle 12
by a residence-three Hamilton path on its 135 middle vertices.  Cutting the
unique owners on physical cycle 1 of every foreign lower-q1 colour turns this
reroute into a palette trade.  Cycle 14 is cut at a minimum residence hitting
set, and every untouched physical cycle is represented by one rotatable,
reversible item.

Two such reroutes were audited:

- `scratch/k15_cycle12_trade.segments.json` (budget 13): 13 owner cuts on
  cycle 1, 14 native lower-q1 holes, and three upper-q1 holes.
- `scratch/k15_cycle12_b14_q1.segments.json` (budget 14): 14 owner cuts on
  cycle 1, 15 native lower-q1 holes, and **zero upper holes at every depth**.

## Item compatibility graph

An item is one residence-safe segment (or one untouched cycle with a chosen
cut and orientation).  Join two items when some allowed orientations have a
residence-safe Johnson seam.  A splice into one word induces a Hamilton path
in this item graph, so every vertex-cut toughness inequality

\[
  c(G-X)\le |X|+1
\]

is necessary.

For both reroutes, let

\[
X=\{\text{items belonging to physical cycles }6,8,9,10,13,15,16\}.
\]

Before any additional splitting, `X` consists of seven items.  Direct exact
enumeration of the residence-safe item graph gives ten components in `G-X`:

1. the cycle-1 trade segments (one component);
2. the remaining carrier core, including the resident cycle-12 path (one
   component);
3. the clean cycle-11 item (one isolated component);
4. seven isolated minimum-residence segments of cycle 14.

Thus

\[
  c(G-X)=10>|X|+1=8.
\]

This proves that the fixed 36-item budget-13 splice and fixed 37-item
budget-14 splice are impossible before imposing any shadow constraints.

## Minimum repair size

Splitting one member of `X` replaces one separator item by two, so `|X|`
increases from 7 to 8 while the same ten components remain after deleting
`X`.  Hence

\[
  10>|X|+1=9,
\]

and **every one-split repair is impossible**.  This subsumes the 1,114
residence-safe split-pair SAT instances that were being considered.

At least two separator cycles must be split.  With two splits, `|X|=9` and
the toughness inequality is tight.  The remaining necessary quotient problem
is an alternating Hamilton path through ten components and nine separator
items.  It is solved exactly before submitting a cut pair to the full
orientation-aware SAT model by
`scratch/search_k15_cycle12_two_split_quotient.py`.

### Cycle 14 cannot be compressed

One possible escape would be to replace the eight residence-safe cycle-14
segments by fewer paths using non-native Johnson edges.  This is impossible.
The exact augmented-dummy SAT model
`scratch/search_k15_cycle_path_cover.py` allows **every** induced Johnson edge
on the 45 vertices of cycle 14 and imposes only depth-three residence.  It
proves path-cover sizes 1 through 7 UNSAT.  Size 8 is SAT, with lengths

\[
6,6,6,6,6,6,6,3.
\]

Certificates are `scratch/k15_cycle14_pathcover_2.json` through
`scratch/k15_cycle14_pathcover_8.json`; the size-one result is
`scratch/k15_cycle14_resident_any.json`.  Hence eight is the global minimum
over all carrier reroutings on those vertices, not merely the minimum number
of cuts in the original cycle.

The minimum cover is not unique.  We enumerated 200 distinct eight-path
covers (`scratch/k15_cycle14_pathcover_8_enum200.json`) and substituted each
into the endpoint-optimized full-orbit cycle-12 carrier.  Every fixed splice
was path-UNSAT.  Their item-edge counts took only the values 350, 354, and 356
(frequencies 68, 53, and 79 respectively).  Thus alternate cycle-14 endpoint
geometry gives a small portal improvement but does not by itself remove the
separator obstruction.

## Upper-shadow portal cost for the budget-13 path

The three missing upper-q1 colours are

\[
10997,\quad 21847,\quad 22442.
\]

All nine middle subsets of each colour lie exclusively on cycles 1 and 12.
Exact portal enumeration shows that each missing colour requires two extra
cuts; the feasible cut-pair counts are respectively 25, 30, and 28, and the
three cut families are disjoint.  Therefore at least six extra portal cuts
are necessary.  The budget-14 path removes this entire layer because it has
zero upper holes at every depth.

## Lower-palette ledger

For the budget-14 path with two separator splits, the final item count is 39.
There are 38 non-cycle-12 cuts and therefore 38 seams.  The reroute replaces
15 native colours by 14 foreign colours, whose 14 native owners are cut on
cycle 1.  Consequently the exact lower-q1 balance is

\[
  15+(38-14)-38=1.
\]

Thus a 39-item braid can in principle leave exactly the single boundary hole
required by the linear compiler.  The open issue is orientation-compatible
Hamiltonization (and then simultaneous q1/q2 upper preservation), not palette
capacity.
