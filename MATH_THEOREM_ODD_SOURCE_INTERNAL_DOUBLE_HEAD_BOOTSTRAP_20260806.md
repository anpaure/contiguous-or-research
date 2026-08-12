# Odd source-internal double-head bootstrap

**Date:** 2026-08-06  
**Method:** literal connector rewrites and reversible marked corridors; no
search or computation  
**Status:** unconditional local initialization and retirement identities,
but **not** an unconditional moving-cart theorem.  The source-selected berth
is adaptive.  If both heads leave it, two different sources can collide.
Thus this note removes the scalar battery but does not yet remove the need for
a persistent berth marker (or an anchored single-head transport).  If the
first connector is extreme, one opposite extreme also remains outside the
bulk cancellation.

## 1. Alphabet

Use the connector alphabet

\[
 A=00,\qquad B=20,\qquad C=22,
\]

the marked neutral block

\[
 M=11,
\]

and the visible-cart head

\[
 H=02.
\]

Complement interchanges `A,C` and fixes `B`.  The source connector word is
balanced:

\[
                         \#A=\#C.
\tag{1.1}
\]

The first connector, which meets the active `p_1` clock, is left outside the
construction below.  Call the remaining connector word the **work suffix**.

## 2. Literal local paths

All arrows below move one unit across one edge of the four-coordinate path.
First, a `C` moves left through one `B` and records the crossed block as `M`:

\[
 20|22:\quad
 2022\to2112\to2202\to2211=22|11.
\tag{2.1}
\]

An adjacent oriented opposite pair creates the double head:

\[
 00|22:\quad
 0022\to0112\to0202=02|02.
\tag{2.2}
\]

For retirement, the double head first becomes the complemented oriented pair:

\[
 \begin{aligned}
 02|02:
 0202&\to1102\to2002\to2011\\
     &\to2101\to2110\to2200=22|00.
 \end{aligned}
\tag{2.3}
\]

The right `A` then moves right through one marked neutral block while restoring
the literal `B`:

\[
 \begin{aligned}
 00|11:
 0011&\to0101\to1001\to1010\\
     &\to1100\to2000=20|00.
 \end{aligned}
\tag{2.4}
\]

Finally, two adjacent neutral source blocks may create the head without a
mass battery:

\[
 20|20:\quad
 2020\to1120\to0220\to0211\to0202=02|02.
\tag{2.5}
\]

The reverse of (2.5) restores `B|B`, which is already its complemented value.

None of the strict interiors of (2.1)--(2.5) contains `H|H`.  Thus the head is
created only at the declared endpoint and destroyed immediately on retirement.

## 3. The oriented-pair bootstrap

Assume that the work suffix contains both `A` and `C`.  Choose the orientation
of the complement pair so that its first non-`B` block is `A`.  In the initial
run of `A` blocks, take its final `A`; let the next non-`B` block be the first
following `C`.  The intervening blocks are all `B`, so the selected segment is

\[
                         A B^s C
\tag{3.1}
\]

for one uniquely determined `s>=0`.

Repeatedly apply (2.1), from right to left.  This gives

\[
                         A B^s C
             \leadsto   A C M^s.
\tag{3.2}
\]

Apply (2.2) to its first two blocks:

\[
                         A B^s C
             \leadsto   H H M^s.
\tag{3.3}
\]

The two source extremes removed in (3.3) have fixed ordered type `A,C`; the
length of the adjacent `M` corridor is exactly `s`.  Hence no nine-valued
record and no mass-offset battery is needed.

At the end of the bulk complement pass, apply (2.3) and then apply (2.4)
successively from left to right:

\[
 \begin{aligned}
 H H M^s&\leadsto C A M^s\\
         &\leadsto C B^s A.
 \end{aligned}
\tag{3.4}
\]

The last word is exactly the connectorwise complement of (3.1).

### Proposition 3.1 (zero-battery stationary-head bootstrap)

For every work suffix containing both extremes, (3.2)--(3.4) install and
retire the protected double head with zero external mass transfer.  The
selected source segment and the stage are recoverable at every macro
checkpoint **while the double head remains at its selected berth**.

#### Proof

The setup and teardown identities were proved literally above.  At the setup
endpoint the unique double head locates the selected segment, while the
adjacent maximal `M` corridor records `s`; replacing it by `A B^s C` recovers
the source segment.  Outside the segment the source tape is untouched.  During
teardown, the unique active `A` immediately before the remaining suffix of
`M` blocks records how many restorations in (2.4) have occurred.  This proves
the stationary statement.  It deliberately makes no claim after both heads
have moved away from the adaptive berth.  \(\square\)

### Proposition 3.2 (adaptive-berth collision)

The stationary statement cannot be upgraded merely by invoking ordinary
double-head transport.  The balanced oriented sources

\[
                         ACB,\qquad BAC
\tag{3.5}
\]

bootstrap respectively to

\[
                         HHB,\qquad BHH.
\tag{3.6}
\]

If the first source moves both heads one block to the right by literal block
transport, it reaches `BHH`, exactly the second source's bootstrap checkpoint.
Common `B` padding gives the same collision in every larger size.  Therefore a
persistent origin head, an injectively marked head trail, or a fixed-coordinate
seed is load-bearing.

## 4. The neutral-pair exception

Suppose the work suffix does not contain both extremes.  By (1.1), apart from
the all-`B` fixed source, this can happen only when the full connector word has
one `A` and one `C`, one of them is the omitted first connector, and the work
suffix contains the other extreme together with `m-2` copies of `B`.

For `m>=5`, a linear word of length `m-1` containing one exceptional block and
at least three copies of `B` has two adjacent `B` blocks.  Choose the first
such pair and apply (2.5).  Its reverse retirement restores the same two
blocks.  The fixed all-`B` source is its own complement and need not enter the
counterflow.

### Corollary 4.1

For every nonfixed central source and every `m>=5`, the work suffix itself
supplies a zero-battery **stationary** double head.  A moving visible cart
still requires the persistent-origin repair identified in Proposition 3.2.

## 5. Exact residual at the first connector

Delete the first connector from a balanced word.  If it is `B`, the work
suffix is balanced and the internal cancellation plus Theorem 3.1 complements
the entire connector tape.  If it is `A` or `C`, the work suffix has exactly
one unmatched connector of the opposite type.  After all internal pairs and
the head berth have been retired, the only unfinished operation is therefore

\[
                         A\mid C\longmapsto C\mid A
       \quad\hbox{or}\quad
                         C\mid A\longmapsto A\mid C,
\tag{5.1}
\]

where the first block denotes the omitted first-connector value and the second
is the one deterministically located remote residual.  The two blocks have
equal total mass before and after (5.1).

Conditional on a persistent-origin repair, the visible cart can bring the
remote residual to the terminal collar without losing its occurrence label.
What is not proved in this note is that repair, nor a directed literal handoff
which changes the active first connector at the same time.  The latter
operation touches the `p_1` clock itself, so it is not an ordinary work edge
covered by the fixed-clock lifting theorem.

Thus the mass-offset part of the old finite collar lemma `DH` has been
eliminated, but its occurrence-label role has not.  The exact odd residue is
an anchored-head transport plus the single two-orientation first-connector
exchange (5.1), together with the already proved aperture/root retirement
collar.
