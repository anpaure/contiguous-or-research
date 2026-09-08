# Independent audit of `ARM_WORD_FACTOR_LIFT.md`

## 1. Verdict

The arm-to-factor lift is correct.

More precisely, let

\[
Q=(v_0,e_1,v_1,\ldots,e_h,v_h),\qquad h\ge 1,
\]

be an oriented trail piece, put `b_t=b_(e_t)`, and assume

\[
 b_t\le v_{t-1},v_t,
 \qquad b_t\vee b_{t+1}=v_t\quad(1\le t<h).       \tag{1.1}
\]

Then replacing the vertex arm

\[
                     v_0,v_1,\ldots,v_h
\]

by

\[
                     v_0,b_1,\ldots,b_h,v_h       \tag{1.2}
\]

preserves every contiguous maximum, even after arbitrary ordering and
orientation of the trail pieces.  For an edge partition into `A` nonempty
trail pieces and `M` edges, the encoded length is exactly `M+2A`.

The claimed conditional implication is consequently sound: an edge-once
virtual-seam arm order covering an upper family lifts to a single
width-plus-surface word which still has the audited lower factor.

There are four presentation qualifications, none fatal:

1. a negatively oriented arm must reverse **both** its vertex arm and its
   encoded block;
2. the formula `M+2A` treats only nonempty edge pieces; isolated graph
   vertices are appended separately, as the source later says;
3. an ordering that copies edges has length equal to the total edge
   multiplicity plus `2A`, not `M+2A`.  The stated Virtual-Seam Excursion
   Lemma uses an edge partition/refinement and is therefore within scope.
4. the degree-defined forced arms used in the upper excursion document are
   not quite all factorable: exactly `2(m-1)` internal degree-two vertices
   have equal half-edge labels.  They must be added as mandatory cut
   locations before applying the lift.  This is only `O(m)` additional
   cuts and preserves every upper witness, so it does not change the
   conditional asymptotic conclusion.

## 2. Exact interval map inside one arm

Index the encoded block (1.2) by `0,...,h+1`, so that position zero is
`v_0`, position `t` is `b_t` for `1<=t<=h`, and position `h+1` is `v_h`.
For a source subpath

\[
                         v_i,\ldots,v_j,
\]

define

\[
 \alpha(i)=\begin{cases}0,&i=0,\\ i,&i>0,\end{cases}
 \qquad
 \beta(j)=\begin{cases}h+1,&j=h,\\ j+1,&j<h.\end{cases}               \tag{2.1}
\]

The encoded witness is the literal interval

\[
                         [\alpha(i),\beta(j)].       \tag{2.2}
\]

This formula resolves every endpoint case without an implicit convention:

| source subpath | encoded interval |
|---|---|
| whole arm `v_0,...,v_h` | `v_0,b_1,...,b_h,v_h` |
| proper prefix `v_0,...,v_j` | `v_0,b_1,...,b_(j+1)` |
| proper suffix `v_i,...,v_h` | `b_i,...,b_h,v_h` |
| internal interval `v_i,...,v_j` | `b_i,...,b_(j+1)` |
| internal singleton `v_i` | `b_i,b_(i+1)` |
| left endpoint singleton `v_0` | `v_0,b_1` |
| right endpoint singleton `v_h` | `b_h,v_h` |

The last two witnesses have maximum `v_0` and `v_h`, respectively, because
`b_1<=v_0` and `b_h<=v_h`.

### No positive coordinate is lost

Every source vertex in the subpath is recovered inside (2.2):

* `v_0` or `v_h`, when present, occurs literally;
* every other included `v_t` is the maximum `b_t vee b_(t+1)` from (1.1).

Thus the maximum of (2.2) is at least
`v_i vee ... vee v_j`.

### No contaminating coordinate is introduced

Every edge minimum in (2.2) lies below an included source vertex.  At the
left boundary, `b_i<=v_i`; at the right boundary,
`b_(j+1)<=v_j`; and an intermediate `b_t` lies below both incident source
vertices.  Literal block endpoints are themselves source vertices.
Therefore the maximum of (2.2) is at most
`v_i vee ... vee v_j`.

Combining the two inequalities proves the exact equality claimed in
equation (2.2) of the source.

The proof also handles a one-edge trail.  Its encoded block is
`v_0,b_1,v_1`; the two endpoint singletons and the whole edge subpath all
have the required maxima.

## 3. Reversal and arbitrary signed order

For the negative orientation of `Q`, the correct encoded block is

\[
                         v_h,b_h,b_{h-1},\ldots,b_1,v_0.              \tag{3.1}
\]

It is the reversal of (1.2), and is also exactly the construction applied
to the reversed trail.  Equation (1.1) is symmetric, so the proof of
Section 2 applies verbatim.

This convention is implicit in the phrase "corresponding encoded blocks"
in the source.  It should be made explicit in any theorem statement that
uses "signed ordering": reversing only the source arm but not its encoded
block would not be the claimed interval-by-interval lift.

No compatibility between successive signs is needed.

## 4. Exact audit of cross-seam intervals

Consider a source interval crossing at least one seam.  It has a unique
decomposition into

1. a suffix `v_i,...,v_h` of the first oriented arm;
2. complete intervening oriented arms; and
3. a prefix `w_0,...,w_j` of the final oriented arm.

Map the suffix to `b_i,...,b_h,v_h` (or the whole first block if `i=0`),
map every intervening arm to its complete encoded block, and map the prefix
to `w_0,c_1,...,c_(j+1)` (or the whole final block if `j` is its last
index).

These pieces form one contiguous encoded interval: the suffix reaches the
last physical position of its block, every intervening block is taken in
full, and the prefix begins at the first physical position of its block.
There is no omitted or inserted position at a seam.

By Section 2, each partial or complete encoded arm has exactly the same
maximum as its source portion.  Taking the maximum over the consecutive
pieces proves equality for the whole crossing interval.

In particular:

* adjacent arms may end and begin at different graph vertices;
* they may share a graph vertex or repeat the same literal value;
* an interval may start or stop on either seam endpoint;
* cycle cuts, where the two arm endpoints can be two occurrences of the
  same graph vertex, cause no exception.

If the source interval stays inside one arm, Section 2 applies directly;
it should not be decomposed as both a suffix and a prefix of that same arm.

## 5. Length accounting

If piece `a` contains `h_a>=1` edges, then its encoded block has
`h_a+2` entries.  Since the pieces partition the edge set,

\[
 \sum_{a=1}^A(h_a+2)=\sum_a h_a+2A=M+2A.           \tag{5.1}
\]

Reversal changes no count.  Cutting one transition cycle creates one open
piece with two occurrences of its cut vertex and still obeys (5.1).
Refining an existing piece at one additional cut increases `A` by one and
adds exactly two endpoint literals relative to the edge-minimum count, so
`O(m^2)` refinements retain `M_m+O(m^2)` length.

An isolated graph vertex is not a nonempty edge piece.  Appending each such
vertex once costs the size of the isolated family; in the lexicographic
graph that family lies on the surface and is `O(m^2)`.

If an auxiliary construction repeats an edge, (5.1) remains true with `M`
replaced by the number of edge occurrences.  This is outside the edge-once
Virtual-Seam Excursion Lemma but is relevant when comparing the theorem
with bounded-copy variants.

## 6. Preservation of the lower factor

Inside every encoded block the sequence

\[
                         b_1,b_2,\ldots,b_h
\]

is physically consecutive and has exactly its original orientation (or
its exact reversal).  Hence every established pair window

\[
                         b_j\vee b_{j+1}=v_j        \tag{6.1}

\]

and every established triple window

\[
                 b_{j-1}\vee b_j\vee b_{j+1}=z_j  \tag{6.2}

\]

survives unchanged.  Inserting endpoint literals only before and after the
entire minimum subsequence cannot split an internal pair or triple.

The lift is actually stronger at trail boundaries than Section 4 of the
source records:

* a trail endpoint vertex is represented literally;
* the colour of every trail-boundary edge is represented by applying the
  interval map of Section 2 to its two endpoint vertices.

For example, the first edge colour `v_0 vee v_1` is the maximum of
`v_0,b_1,b_2` when `h>1`, and of the whole block
`v_0,b_1,v_1` when `h=1`.  The last edge is symmetric.  Thus the old
rank-`2m-1` endpoint and rank-`2m` boundary repairs from the bare minimum
word are conservative and may be omitted after this lift.  Appending them
anyway is harmless and still costs only `O(m^2)`.

The exact bottom image is unchanged because each edge minimum still occurs
once as a singleton.  For the four-box lexicographic graph the only missing
rank-`2m-2` points are the audited `m(m-1)` surface family, which may be
appended literally.

### 6.1 Compatibility with the degree-defined forced arms

This point is implicit but must not be skipped.  The upper excursion notes
define forced arms by cutting at vertices of graph degree different from
two.  A degree-two vertex need not have two distinct half-edge labels.

In the four-box lexicographic graph, the degree-two equal-label vertices
are exactly

\[
 (0,m,a,m-1-a),\qquad (m,0,a,m-1-a),
 \qquad 1\le a\le m-1.                              \tag{6.3}
\]

There are `2(m-1)` of them.  At a vertex in the first family both labels
are coordinate 2, and at a vertex in the second family both labels are
coordinate 1.  Hence (6.1) fails if an unrefined forced arm passes through
one of these vertices.  The remaining equal-label cases have degree one or
three and are already cut by the degree kernel.

Cut every forced arm additionally at (6.3).  All internal vertices of the
refined arms now have distinct labels, and the number of new pieces grows
by at most `2(m-1)`.  If an upper ordering was first obtained for the
unrefined arms, keep the two children of each new cut consecutive and in
their inherited orientation.  The refined vertex word differs only by an
extra adjacent copy `v,v` of the cut vertex.  Any old interval crossing the
cut may include the duplicate without changing its maximum; intervals on
one side are unchanged.  Therefore every old upper witness survives.

This supplies the missing bridge between the degree-arm Virtual-Seam
formulation and hypothesis (1.1) of the factor lift, at surface cost.

## 7. Nonzero entries and isolated cases

In the application `m>=2`:

* every minimum `b_e` has rank `2m-2>=2`;
* every endpoint literal has rank `2m-1`;
* every literal repair has positive rank.

Hence the constructed word is nonzero.  The generic interval-preservation
lemma itself does not require positivity, but the nonzero conclusion in
the four-box application does.

An isolated vertex has no incident minimum from which it could be
reconstructed.  Appending it literally is therefore both necessary for
this particular encoding and sufficient.  Its addition cannot destroy an
existing witness.

## 8. Conditional coupling to upper coverage

Let `W_V` be a concatenation of the oriented vertex arms, and let `W_F` be
the concatenation of their corresponding encoded blocks.  Sections 2--4
prove the set inclusion

\[
 \{\bigvee I:I\text{ a contiguous interval of }W_V\}
 \subseteq
 \{\bigvee J:J\text{ a contiguous interval of }W_F\}.               \tag{8.1}
\]

Therefore every upper target certified by a seam-crossing interval in
`W_V` has a concrete seam-crossing interval in `W_F` with exactly the same
maximum.  Independently, Section 6 supplies the three lower layers, up to
surface repairs.  Since all entries of `W_F` are explicit minima or endpoint
vertices, this coupling needs no SAT labeling, envelope choice, or second
pin-survival argument.

The implication is conditional only on the existence of the required
upper arm order.  It does not prove the Virtual-Seam Excursion Lemma, and it
does not cover layers below `2m-2`.

When that upper order is phrased for the original degree-defined forced
arms, the mandatory refinement in Section 6.1 must be performed before
forming `W_F`.

## 9. Finite adversarial check

As an independent diagnostic, I reconstructed the lexicographic graph and
the distinct-label transition decomposition for every `m=2,...,8`.  For
each `m`, ten independently seeded random permutations and orientations of
all trail pieces were tested.  I enumerated every contiguous maximum of
the concatenated vertex-arm word and every contiguous maximum of the
encoded word.  In all 70 signed orders, every former value occurred in the
latter word.

The tested trail counts were respectively

\[
                         10,17,26,37,50,65,82,
\]

and included one-edge pieces, open endpoints, cycle cuts, unrelated seam
vertices, and both orientations.  This is not used as proof; the exact map
(2.1)--(2.2) is the proof.

## 10. Final ledger

| Claim | Audit result |
|---|---|
| exact subpath mapping | proved, including all endpoint cases |
| arbitrary virtual seams | proved |
| arbitrary signed order | proved once reversal convention is explicit |
| encoded length `M+2A` | proved for nonempty edge pieces |
| pair/triple lower windows | preserved literally |
| trail-boundary lower values | stronger than claimed: recovered by the lift |
| compatibility with degree-defined forced arms | valid after `2(m-1)` mandatory cuts |
| isolated vertices | require and admit surface-size literal repair |
| nonzero four-box word | proved for `m>=2` |
| coupling to any upper arm coverage | proved conditionally |
| existence of the all-upper arm order | not claimed and remains open |

The abstract source theorem is therefore suitable for the proved ledger.
Its four-box corollary is suitable after explicitly inserting the
equal-label cuts of Section 6.1, together with the orientation and
edge-partition qualifications stated above.
