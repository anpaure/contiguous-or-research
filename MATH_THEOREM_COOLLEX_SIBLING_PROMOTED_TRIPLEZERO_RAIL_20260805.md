# Cool-lex sibling paths lift to monotone promoted triple-zero rails

**Date:** 2026-08-05  
**Method:** binary-necklace and rooted PBBS phase algebra; no search  
**Status:** unconditional as an incidence/order statement.  It identifies
the exact overlap of consecutive leaf-plucking packets, but does not prove
that their overlapping q2 identities compose.

## 1. One adjacent child edge and its promoted port

Encode a hook-angle necklace by a binary necklace with one zero per vacancy
slot and one one per leaf.  An adjacent child edge has rooted form

\[
                         A01B\longleftrightarrow A10B.
\tag{1.1}
\]

Deleting the transferred leaf leaves the displayed old vacancy zero.
Promotion inserts two new empty vacancy slots at that cut.  Hence the
marked promoted parent is exactly

\[
                              A000B,
\tag{1.2}
\]

with the inserted adjacent zero pair marked inside the displayed
triple-zero block.  Deleting the mark recovers (1.1), so this is the binary
form of the marked-port bijection.

## 2. The exact sibling port rail

At a cool-lex recursive call write

\[
                         r=0^s1^t\gamma.
\]

Its sibling-root path is

\[
                         r-r_{t-1}-r_{t-2}-\cdots-r_j,
\]

where

\[
 r_i=0^{s-1}1^{t-i}0,1^i\gamma.
\]

Applying (1.2) to the successive path edges gives, in the same order,

\[
 p_a=0^{s-1}1^a000,1^{t-1-a}\gamma,
       \qquad 0\le a\le t-j-1.
\tag{2.1}
\]

Thus the marked triple-zero port moves monotonically through the one-run.
Consecutive ports satisfy

\[
 A0001B
 \longleftrightarrow A0010B
 \longleftrightarrow A0100B
 \longleftrightarrow A1000B,
\tag{2.2}
\]

three legal adjacent chip transfers in the promoted hook-angle graph.
In particular, the cool-lex order is not an arbitrary order on promoted
ports: every sibling family embeds canonically as every third vertex of a
monotone promoted-angle rail.

## 3. Exact overlap on an intermediate child

Consider two consecutive child transfers with the same base angle `y`, at
consecutive cuts.  Their common child is represented once with the added
leaf immediately before the root cut and once with it immediately after
the preceding root cut.  The two cuts are consecutive vacancy phases.

For a hook of height `h`, the rooted PBBS factor successor is `g=f^2` and
acts on the `q=2h-1` vacancy slots by one cyclic step:

\[
                   2(1-h)=1-q\equiv1\pmod q.
\tag{3.1}
\]

Therefore the two tail occurrences on the common child are consecutive
factor states, say `S` and `gS`.  The first packet changes the old factor
edge

\[
                              S\longrightarrow gS,
\tag{3.2}
\]

whereas the second packet changes

\[
                              gS\longrightarrow g^2S.
\tag{3.3}
\]

They do **not** use the same changed old edge.  However, (3.2) is exactly
the incoming companion edge at the tail `gS` in the second packet's q2
identity.  Hence consecutive packets have one canonical directed-edge
halo overlap.

## 4. Consequence and remaining gate

Equations (2.1)--(2.2) give a positive recursive order structure on the
promoted side, and (3.2)--(3.3) identify the only forced child-side overlap
along a sibling path.  This is stronger than marked-port injectivity and
is the appropriate input to a recursive contour calculation.

It is not yet a compound q2-neutral circuit.  The single-C6 common-deletion
proof treats its incoming companion as unchanged; in the chain above that
edge is changed by the preceding packet.  To telescope the chain one must
compute the combined q2 turn multiset (including the possibly different
common deletion pivots at successive cuts).  Neither pairwise disjointness
nor the isolated-C6 theorem supplies that identity.

Thus the exact live positive gate is:

> prove a compound q2 identity for the monotone sibling rail, then compare
> the induced promoted rail contour with the recursive cool-lex plane-tree
> contour.

No global packing or `nu(k)<=B(k)+O(1)` conclusion is asserted here.
