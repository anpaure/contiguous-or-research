# Odd APH: the OC18 origin code turns an adaptive atom into a mobile double cart

**Date:** 2026-08-06  
**Method:** a bounded origin aperture, explicit capacity-two code layers, and
copy-before-erase; no computation or search  
**Status:** unconditional local origin-code theorem and mobile-cart
reduction.  It closes the unbounded-address defect which a remote auxiliary
code would not close.  The fixed-row directed-lift audit now passes, so the
APH consequence in Section 7 is unconditional relative to its cited proved
package inputs.

## 1. Why the code must live at the cart origin

A finite code at an unrelated auxiliary atom remembers its own type but not
the unbounded physical address of the atom from which `H|H` departed.  The
old `ACB/BAC` collision may then be tensored with the remote code.  Therefore
the code below is written in a bounded collar of the **same** atom which
creates the cart.

Retain

\[
 A=00,\quad B=20,\quad C=22,\quad H=02,\quad M=11.
\]

The early four-state theorem records the atom type and, on an `AB^sC`
source, distinguishes private-gap from raw transport before any head moves.

## 2. A bounded origin aperture always exists

Bootstrap one deterministically selected ordinary atom.  Its endpoint is one
of

\[
            HHM^s,\qquad M^sHH,\qquad HH.             \tag{2.1}
\]

The first two words are the two transition orientations; the last is the
neutral `BB` atom.

An **origin aperture** is an ordered pair of noncart blocks in a fixed
neighbourhood of (2.1) whose combined mass is strictly between zero and
eight.

### Lemma 2.1 (origin-aperture lemma)

Let the reserved-collar word have length at least fourteen and imbalance at
most three.  One can select the ordinary atom so that after its bootstrap it
has an origin aperture.  The two aperture blocks can be brought to the same
side of the still-stationary `H|H` by a bounded sequence in which one head is
literal at every nontrivial block transposition.

#### Proof

If a selected transition gap has length at least two, use its first two
`M`-blocks.  Their total mass is four.

If the gap has length one, use its `M` together with the nearest nonhead raw
block.  Their total mass is two, four, or six.  If the raw block lies on the
opposite side of `H|H`, move it through the cart one head at a time; the other
head is a literal sentinel.

Suppose the gap has length zero.  If the immediate outer blocks on the two
sides of the heads have nonextreme combined mass, use them and move the right
one left through the cart.  Otherwise those two outer blocks have the same
extreme sign.  In the reduced binary word this means that the selected
transition is adjacent to a singleton run.  Choose the other edge of that
singleton run.  Its outer blocks have opposite signs unless the whole
non-`B` word has one minority letter.  In the latter case imbalance at most
three bounds the number of extreme blocks by five.  Since the full word has
length at least fourteen, a `B`-run supplies a block of mass two within a
bounded number of extreme blocks; pair it with its nearest nonhead block.

Finally suppose no transition is used.  Then all extremes have one sign and
there are at most three of them.  Length at least fourteen gives at least
eleven copies of `B` in at most four runs.  Some run has length at least
three.  Choose two adjacent `B`'s for the atom and use a third `B` together
with its nearest nonhead neighbour as the aperture.  Again the total mass is
two, four, or six.

In every case the aperture lies in the atom gap, immediately outside the
atom, or across at most the bounded singleton extreme bank just described.
Before the cart leaves, the early register and one stationary head give the
audited raw-interval decoder for bringing the two blocks to the origin.
Each final crossing through `H|H` is performed as two adjacent block swaps,
holding the other head fixed.  \(\square\)

The boundedness in the proof is absolute; no distance depending on \(m\) is
hidden in the aperture.

## 3. The code layers

For \(j\in\{0,\ldots,8\}\), let

\[
 V_j=\{x\in\{0,1,2\}^4:\;x_1+x_2+x_3+x_4=j\},       \tag{3.1}
\]

with edges given by one adjacent unit transfer.  This is the state graph of
two capacity-two blocks of total mass \(j\).  Every nonextreme layer is
connected by the prefix-discrepancy algorithm.

The only layer containing the double head is \(V_4\), where

\[
                              HH=0202.
\]

### Lemma 3.1 (`OC18` connectivity)

The graph \(V_4-\{0202\}\) is connected and has eighteen vertices.

#### Proof

The mass-four layer has coefficient

\[
                          [z^4](1+z+z^2)^4=19.
\]

The three neighbours of `0202` are

\[
                    1102,\qquad 0112,\qquad 0211.
\]

The first and third reach `1111` directly without using `0202`.  The middle
one has the avoiding path

\[
                    0112\to1012\to1021\to1111.
\]

Since the full layer is connected and all neighbours of the deleted vertex
remain in one component, deleting that vertex leaves the graph connected.
\(\square\)

For masses two, four, and six, three convenient source-indexed path triples
are:

\[
\begin{array}{c|ccc}
AB&0020&0011&0002\\
BA&2000&1100&0200
\end{array}                                         \tag{3.2}
\]

along the displayed left-to-right paths;

\[
\begin{array}{c|ccc}
AC&0022&0112&1012\\
CA&2200&2110&1210\\
BB&2020&2011&2002
\end{array}                                         \tag{3.3}
\]

and

\[
\begin{array}{c|ccc}
BC&2022&1122&0222\\
CB&2220&2211&2121.
\end{array}                                         \tag{3.4}
\]

Every consecutive pair in each row is one adjacent unit transfer.  For a
fixed column, the row paths are vertex-disjoint.  The tables are not needed
for connectivity; they are a transparent audit that three collar-order
classes fit without using `HH`.

## 4. Writing the origin code

Let `S` be the ordered source aperture from Lemma 2.1 and let
\(j=\operatorname{mass}(S)\in\{2,4,6\}\).  The literal outside source
determines the collar sum, so its ordered collar has at most three order
classes.  Choose three distinct codewords

\[
                       O_{S,0},O_{S,1},O_{S,2}\in V_j, \tag{4.1}
\]

avoiding `HH` when \(j=4\).  Use (3.2)--(3.4) when `S` is one of the raw
pairs displayed there; for the `M`-containing aperture modes use any three
simple paths supplied by the same connected layer.

Hold the source collar and early atom register literal while routing `S` to
the codeword for its collar-order class.  The cart is still at its source
atom.  Thus any projected path intersection is tensored with the unchanged
collar, atom type/orientation, and aperture geometry.  At the endpoint the
codeword itself carries the order class, while its physical position in the
bounded atom collar carries the origin address.

### Theorem 4.1 (persistent-origin mobile-cart theorem)

After writing (4.1), both heads may leave the adaptive atom together as a
mobile `H|H` cart.  Its paths through the raw, tag, corridor, and completed
midpoint alphabets are pairwise source-disjoint.  The cart may later return
to the code, restore `S`, and reverse the atom bootstrap.

#### Proof

At a macro checkpoint the unique bounded origin code gives the original atom
address, aperture mode, and collar-order class.  The early register gives
the transport pass and local branch.  The mobile `H|H` gives its current
address.  Reversing the completed block swaps recovers the source interval.

At a strict cart/block swap, one of the two cart heads remains literal.  The
origin code distinguishes it from any isolated origin `H` which a codeword
may contain, and the branch state gives the crossed endpoint type.  The
chosen simple local path then gives the microstep.  This is exactly the
fixed-berth proof of the double-head theorem with "fixed physical berth"
replaced by the stronger persistent literal origin code.

For return, keep the code literal until the cart is back at the atom.  Before
erasing the code, copy its collar-order class into the protected register;
the code and returned cart still give the atom type and orientation.  Reverse
the code path to `S`, then reverse the atom bootstrap.  Finally the literal
source atom labels retirement of the temporary register copy.  This is
copy-before-erase in both directions.  \(\square\)

## 5. Paying the complete pre-head collar

Remove the zero-charge source atom before choosing the noncrossing
cancellation.  The remaining residual extreme bank still has size at most
three and is disjoint from the origin code.  Together with `(G_1,B_2)` there
are at most four remote increments.

Use the sign ordering of the zipper-split fixed-berth accumulator.  For each
increment, the mobile cart shuttles the remote block to the collar, guards
the bounded fixed-mass conversion, and returns the transformed block to its
labelled address before the next increment.  Unlike the old stationary-only
attempt, the cart crosses both a still-raw later extreme and an already
written `M` literally.  Theorem 4.1 and the protected-island extension give
the occurrence decoder for those crossings.

The collar-order class is already stored in the origin code, so every
intermediate even collar mass may use one deterministic representative.  The
last increment writes the permanent `H|H` at the common collar berth.

## 6. No `HHHH` coexistence is needed

Keep one ordinary nonhead block `D` between the returning temporary cart and
the permanent berth.  Such a block exists: if the source atom has a long
gap, an unused gap block is available; otherwise the bounded atom, two code
positions, and at most four task positions use fewer than the fourteen work
blocks guaranteed by the resource theorem.

On the final collar step hold `D` fixed.  Return the temporary cart to the
origin side, leaving

\[
                              HH|D|HH.                \tag{6.1}
\]

The right pair is the permanent fixed cart.  Return the left pair to its
origin, apply the reverse part of Theorem 4.1, and restore the source atom.
The permanent pair remains literal throughout.  Thus the complete ordinary
tape is raw again while the source-independent fixed cart is already
available.

## 7. Consequence and exact audit boundary

### Theorem 7.1 (odd APH from the origin code)

The Anchored Pre-Head Bootstrap lemma holds for every odd dimension whose
reserved work word has length at least fourteen.  In particular the
asymptotic odd package closes from this row.

#### Proof

The reserved-collar resource theorem supplies the atom.  Lemmas 2.1 and 3.1
and Theorem 4.1 turn it into an occurrence-labelled mobile cart without
touching `p_1`.  Section 5 supplies every protected `G_1` and residual
payment and creates the permanent fixed cart.  Section 6 retires the
temporary source atom without merging the two heads.

Now invoke the fixed-head marked/LIFO recoder, connector beta, and the proved
monotone post-beta accumulator.  Each input is literal and every earlier
temporary change has been restored.  \(\square\)

The final fixed-row audit is
`MATH_AUDIT_ODD_APH_OC18_FIXED_ROW_DIRECTED_LIFT_20260806.md`.  Every OC18
edge, including a reflected bounded support straddling the semantic atom
heads, is a physical work edge after `p_1`.  The shadow-clock theorem lifts
these edges directly, one by one.  No directed conjugacy and no extra local
generator are required.
