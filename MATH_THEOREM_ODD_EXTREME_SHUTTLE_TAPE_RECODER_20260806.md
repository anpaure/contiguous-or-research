# Odd current: the reflected record tape has a tagged extreme-shuttle recoder

**Date:** 2026-08-06  
**Method:** an exact connector-code involution, cancellation of a balanced
ternary word, and finite capacity-two token shuttles; no computation or
search  
**Status:** unconditional unlabelled tape-recoding theorem.  The
occurrence-labelled, pairwise-disjoint path-bank conclusion is additionally
conditional on a literal visible-cart encoder for the finite block-crossing
branches; see
`MATH_AUDIT_ODD_EXTREME_SHUTTLE_VISIBLE_CART_20260806.md`.  The theorem
converts every record coordinate away from the active `p_1` interface.  The
one omitted connector is a bounded charge and belongs to the proved
retirement collar.

## 1. The connector code

For a ternary digit `a` put

\[
 B(a)=\beta(a),\qquad G(a)=\gamma(a).
\]

Thus

\[
 C(a):=(B(a),G(a))\in\{00,20,22\},
\tag{1.1}
\]

and the three values encode `a=0,1,2`, respectively.  In the zipper word

\[
 c(B_1),(G_1,B_2),(G_2,B_3),\ldots,
\tag{1.2}
\]

the two coordinates of `C(a_i)` are physically adjacent: `B_i` is the
right coordinate of one scan pair and `G_i` is the left coordinate of the
next scan pair.  The connector blocks `C(a_i)` are pairwise disjoint and
occur consecutively along the physical path.

The reflected target tape has connector code

\[
 C^*(a)=(2-G(a),2-B(a)).
\tag{1.3}
\]

Consequently

\[
                 00\longleftrightarrow22,
                 \qquad20\longmapsto20.
\tag{1.4}
\]

At central mass, `sum_i a_i=m`, and hence

\[
 \#\{i:C(a_i)=00\}=\#\{i:C(a_i)=22\}.
\tag{1.5}
\]

Indeed `sum_i(a_i-1)=#\{a_i=2\}-#\{a_i=0\}=0`.

## 2. Literal tags for an opposite pair

The following two paths use only adjacent unit transfers on four
consecutive capacity-two coordinates:

\[
\begin{aligned}
0022&\to0112\to1012\to1102\to2002\to2011\to2101,\\
2200&\to2110\to1210\to1120\to0220\to0211\to0121.
\end{aligned}
\tag{2.1}
\]

Thus an adjacent `00|22` pair is changed to the visible noncode tags
`21|01`, while `22|00` is changed to `01|21`.  The two orientations retain
the original digits.  Neither `21` nor `01` belongs to the record alphabet
`{00,20,22}`.

The tags finalize by

\[
 2101\to2110\to2200,
 \qquad
 0121\to0112\to0022.
\tag{2.2}
\]

Therefore the composite of (2.1) and (2.2) is exactly the required swap
`00|22 -> 22|00` or `22|00 -> 00|22`, but the middle tagged phase keeps the
old digit labels visible.

Every arrow in (2.1)--(2.2) transfers one unit across one physical path
edge.  Total mass is four throughout.

## 3. Finite block shuttles

We use one elementary fact repeatedly.

### Lemma 3.1 (finite block interchange)

Let `X` and `Y` be two adjacent blocks of fixed lengths in a
capacity-two path.  If the concatenations `XY` and `YX` have the same
length and total mass, and that mass is neither zero nor full capacity,
then there is a simple adjacent-transfer path from `XY` to `YX` supported
on those blocks.

#### Proof

The capacity-two token graph on a path is connected in every fixed
nonextreme mass layer.  One direct proof moves the prefix excess across
successive path edges: if the first coordinate at which the current word
and target word differ has excess, move one unit right until it reaches
the first deficit; if it has a deficit, perform the reverse move.  The
sum of the absolute prefix discrepancies strictly decreases.  Capacity
zero and two cause no obstruction, because an attempted transfer stops at
the first deficit and every intervening coordinate has a unit available
in the required direction.  Iteration reaches the target.  Removing loops
gives a simple path.  \(\square\)

Only a finite list of instances is used below.  The moving block is one of

\[
                    00,22,01,21,
\]

and a stationary tape block is one of

\[
                    20,01,21.
\]

All their concatenations have nonextreme mass.  Two useful literal
instances are

\[
\begin{aligned}
20|22:quad&2022\to2112\to2202\to2211\to2220=22|20,\\
20|00:quad&2000\to1100\to1010\to0110\to0020=00|20.
\end{aligned}
\tag{3.1}
\]

Their reverses move the output extreme back to the right.  Lemma 3.1
supplies the equally finite tag crossings.

The ordered types of the two blocks form a fixed finite alphabet.  To turn
these unlabelled paths into a simultaneous path bank, one needs a literal
visible cart which writes that ordered type, remains readable throughout the
chosen simple path, and restores the ordinary delimiter afterward.  Scalar
reachability of the required delimiter masses follows from the `p_1` mass
ladder, but that does not by itself prove occurrence-labelled setup and
teardown paths.  The precise finite condition is stated in
`MATH_AUDIT_ODD_EXTREME_SHUTTLE_VISIBLE_CART_20260806.md`.

## 4. Cancellation and shuttling

Ignore the `20` blocks and read `00` as a minus sign and `22` as a plus
sign.  By (1.5) the sign word is balanced.  Repeatedly choose two unlike
signs which are adjacent among the still unprocessed signs.  Such a pair
exists unless no signs remain.

For one chosen pair, move the right extreme block left across every block
between it and its mate.  An unprocessed intervening block is `20`; a
processed block is one of the visible tags `01,21`.  Lemma 3.1 moves the
extreme past each such block.  Apply (2.1) when the opposite extremes
become adjacent.  Then move the right tag back to the original right-hand
position by reversing the same sequence of block interchanges.  Every
intervening block is restored literally.  The two processed positions now
carry `21,01` or `01,21`, so they remain visible and retain their original
digits.

Remove those positions from the unprocessed sign word and repeat.  At the
end every extreme position is tagged and every digit-one position is the
unchanged code `20`.

Now run the same cancellation pairs once more.  Shuttle the right tag to
its mate, apply (2.2), and shuttle the resulting right target block back.
After the last pair, every connector block is exactly `C^*(a_i)` and all
intermediate blocks have been restored.

### Theorem 4.1 (conditional tagged extreme-shuttle recoder)

Assume the visible-cart condition from
`MATH_AUDIT_ODD_EXTREME_SHUTTLE_VISIBLE_CART_20260806.md` for every finite
tagging, shuttling, return, and finalization branch used below.

On the connector tape disjoint from the active `p_1` pair, the preceding
algorithm gives a prescribed tail-token path

\[
               (C(a_i))_{i\ge2}\leadsto(C^*(a_i))_{i\ge2}
\tag{4.1}
\]

for every central ternary source.  At every intermediate state the source
and stage are recoverable.  Consequently the paths for distinct sources
are pairwise vertex-disjoint after their lift through the fixed `p_1`
shadow clock.

#### Proof

At a macrostep boundary, each block is exactly one of the following:

* an unprocessed literal source code;
* the fixed code `20`;
* a visible oriented tag which records its source extreme; or
* a finalized target code whose source is recovered by the involution
  (1.4).

The moving delimiter identifies the unique active shuttle and the current
cancellation pair.  The deterministic leftmost cancellation rule is then
reversible.  During one finite block interchange, the delimiter records
the ordered block type and the simple path has no repeated local state, so
the microstep is also recovered.

Equivalently, delete the active blocks from two putatively colliding tape
states.  Equality of all remaining source/target/tag blocks recovers all
other ternary digits.  Since both source words have sum `m`, the remaining
active digit or opposite pair is forced as well.  The delimiter then
forces the same branch and microstep.  Thus the source-to-current-state map
is injective at every local time.

Every shuttle move is a physical transfer on coordinates disjoint from
`p_1`.  The shadow-clock phase-compilation theorem lifts it to a directed
two-arc path in the fixed phase-zero contraction.  Its tagged
time-expansion lemma converts the injectivity just proved into pairwise
vertex-disjointness of the whole source bank.  \(\square\)

## 5. The omitted `p_1` connector

The connector `C(a_1)` meets the active `p_1` clock and is intentionally
not touched in Theorem 4.1.  Removing one digit from a balanced word leaves
extreme imbalance at most one.  In the shuttle description this is exactly
one unpaired `00` or `22`, hence at most four units of bounded mass debt.

The proved shadow-clock mass router changes the masses of the two work
components and the clock among one, two, and three by repeated unit
transfers.  It therefore carries this single omitted charge.  The finite
aperture-retirement collar then writes the required `p_1`/boundary
predecessor and reaches the exact target endpoint.

Thus the record tape itself has no growing *unlabelled* serialization
obstruction.  In an application one must still install the bounded
visible-cart interface, identify the input reflected record chain and output
target record chain with the connector coordinates in (1.2), and invoke the
already audited retirement hypotheses.  No new macroscopic path packing,
comparator network, or unbounded scratch bank is required, but the bounded
cart is load-bearing for pairwise disjointness.
