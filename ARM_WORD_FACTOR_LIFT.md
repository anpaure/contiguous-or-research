# Lifting a forced-arm word to the edge-minimum factor

## 1. Outcome

Let a graph edge `e=uv` have colour `z=u vee v` and minimum

\[
                         b_e=u\wedge v.
\]

Suppose its edges have been partitioned into trail pieces

\[
 Q=(v_0,e_1,v_1,e_2,\ldots,e_h,v_h)               \tag{1.1}
\]

such that at every internal trail vertex

\[
                         b_{e_j}\vee b_{e_{j+1}}=v_j. \tag{1.2}
\]

This is exactly the distinct-half-edge-label transition condition in the
lexicographic selected-cover graph.

### Theorem 1 (arm-to-factor lift)

Replace each oriented vertex arm

\[
                         v_0,v_1,\ldots,v_h
\]

by the encoded block

\[
             F(Q)=v_0,b_{e_1},b_{e_2},\ldots,b_{e_h},v_h. \tag{1.3}
\]

For any signed linear ordering of the trail pieces, every contiguous
maximum occurring in the concatenated vertex-arm word also occurs in the
concatenation of the corresponding encoded blocks.  If the graph has `M`
edges and `A` trail pieces, the encoded word has length

\[
                         M+2A.                       \tag{1.4}
\]

For the four-box lexicographic graph, first refine the degree-defined forced
arms at every internal degree-two vertex whose two half-edge labels are
equal.  There are exactly `2(m-1)` such vertices,

\[
 (0,m,a,m-1-a),\quad(m,0,a,m-1-a),\qquad1\le a\le m-1. \tag{1.5}
\]

Keep the two child pieces consecutive in their old orientation when they
belong to one upper macro-arm; the duplicated cut vertex preserves every
old vertex-word interval.  This adds only `O(m)` pieces and ensures (1.2)
at every remaining internal transition.  Thus `M=M_m` and `A=O(m^2)`.
Moreover the internal edge-minimum subsequences retain the audited pair-
and triple-window equations.  Consequently, any seam-aware arm ordering
which covers an upper target family lifts automatically to one word of length

\[
                         M_m+O(m^2)                  \tag{1.6}
\]

covering that family together with the three lower layers
`L_(2m-2),L_(2m-1),L_(2m)`, after the existing surface-size literal
repairs.

Thus the Virtual-Seam Excursion Lemma, if proved, already couples to the
lower factor.  No second global pin assignment is needed for this spine.

## 2. One subpath

Consider a vertex subpath

\[
                         v_i,v_{i+1},\ldots,v_j      \tag{2.1}
\]

inside (1.1).  Associate to it the following interval of (1.3):

* start at the literal `v_0` if `i=0`, and otherwise at `b_(e_i)`;
* end at the literal `v_h` if `j=h`, and otherwise at `b_(e_(j+1))`.

Every included edge minimum lies below a vertex in (2.1): the first is
below `v_i`, the last is below `v_j`, and every intermediate minimum lies
below both of its incident subpath vertices.  Hence the encoded interval's
maximum is at most the maximum of (2.1).

Conversely, every internal vertex `v_l` in (2.1) has both
`b_(e_l),b_(e_(l+1))` in the encoded interval, so (1.2) recovers it.
If an endpoint of (2.1) is an endpoint of the whole arm, its literal copy
is present; otherwise the same adjacent-pair equation recovers it.  Thus
the encoded interval has maximum exactly

\[
                         v_i\vee\cdots\vee v_j.     \tag{2.2}
\]

This includes a one-vertex subpath: an internal singleton uses its two
incident minima, while an arm endpoint uses its literal occurrence.

## 3. Intervals crossing virtual seams

An interval in a concatenated vertex-arm word consists of

1. a suffix of its first arm,
2. zero or more complete intervening arms, and
3. a prefix of its last arm.

Apply the construction in Section 2 to the first and last partial arms and
take the complete encoded blocks for every intervening arm.  Because the
encoded blocks occur in the same signed order, these pieces form one
contiguous physical interval.  Equation (2.2), arm by arm, shows that its
maximum is exactly the maximum of the original vertex-word interval.

This argument makes no assumption that a virtual seam joins two graph
edges or repeats the same graph vertex.  Arbitrary signed arm order is
allowed.

## 4. Length and lower-factor preservation

Every graph edge contributes its minimum exactly once, and every trail
piece contributes two literal endpoint vertices.  This proves (1.4).
Additional isolated vertices may be appended literally; in the
lexicographic graph they form only a surface-size family.

Before applying the construction to the lexicographic forced arms, make the
`2(m-1)` equal-label cuts listed in (1.5).  A degree-two equal-label
transition would fail (1.2); after cutting, it becomes two arm endpoints
represented by the duplicated literal vertex.  If its two child pieces are
kept adjacent, the argument of Section 3 shows that all intervals of the
unrefined upper arm word are still preserved.

Inside each resulting encoded block the minima

\[
                         b_{e_1},\ldots,b_{e_h}
\]

remain consecutive.  Therefore all established identities

\[
 b_{e_j}\vee b_{e_{j+1}}=v_j,
 \qquad
 b_{e_{j-1}}\vee b_{e_j}\vee b_{e_{j+1}}=z_j      \tag{4.1}
\]

remain literal physical windows.  Only trail endpoints and cycle cuts are
missed, exactly as in `LEX_THREE_LAYER_FACTOR.md`; their count is
`O(m^2)`.  The exact singleton deficit in rank `2m-2` is also unchanged.
Appending those known repairs proves (1.6).

## 5. Scope

The theorem is a lossless reduction from upper arm ordering to a combined
upper/lower OR word.  It does **not** prove that the required signed arm
order exists, and it does not reach layers below `2m-2` without the
separate growing-band construction.  Its role is to remove a formerly
independent compatibility concern: virtual seams used for upper coverage
do not destroy the lower factor, because literal arm endpoints mediate the
lift at surface cost.
