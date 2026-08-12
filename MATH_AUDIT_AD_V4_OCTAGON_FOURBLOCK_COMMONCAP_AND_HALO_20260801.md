# The V4 four-octagon move avoids the split valley, but is not owner-simple

Date: 2026-08-01  
Lane: AD, common-cap and physical-halo audit  
Status: exact all-depth owner/common-cap theorem, with a sharp owner-multiplicity
obstruction.  Width-graded OR-support identities are independently replayed
through depth 24; no all-depth proof of that secondary source-deck identity is
claimed here.

## 0. Verdict

Let

\[
 \alpha=(01)(23),\qquad \beta=(03)(12),\qquad
 \gamma=\alpha\beta=(02)(13),
\]

and place four relabelled sharp octagon blocks in the order

\[
                 1,\ \beta,\ \alpha,\ \gamma .          \tag{0.1}
\]

The proposed simultaneous phase move is

\[
                         0110\longrightarrow1001.        \tag{0.2}
\]

It genuinely evades the universal single-split valley: all four replaced
source blocks have equal length, so no source index is shifted.  However,
the **naked concatenation** is not a rank-\(r\) source.  At each of its three
seams it has exactly \(d\) rank-\(r+2\) windows; in total it has

\[
              3d\text{ bad-rank windows},\qquad
              3(d+1)\text{ non-Johnson consecutive pairs}.       \tag{0.3}
\]

There is an exact positive repair.  Work first at owner level and put one
intersection screen between every two blocks.  The resulting two words are
resident rank-\(r\) Johnson walks of common length \(32d+95\), have equal
owner multisets and equal immediate lower/upper palette multisets, and their
maximal erosions are nonempty exact sources of common length \(33d+95\).
The first and last \(d+2\) source positions agree literally.  The free
positionwise unions give one common-cap family for (0.2), and no deadline
jump occurs.

This still is not a physical owner-tight packet.  The four relabellings in
(0.1) preserve the same eight active octagon owners.  Consequently the
screened word has only

\[
                         8d+26                           \tag{0.4}
\]

distinct owners among \(32d+95\) occurrences, with maximum multiplicity
five.  Thus four coordinated replacement is a valid common-cap resident
**walk** and a valid prepared-slot relation, but it is not a literal simple
carrier unless an additional owner-disjoint/tagged embedding is supplied.

This is the sharp distinction requested by the single-split obstruction:

\[
\boxed{
\begin{array}{c}
\text{equal-length V4 replacement + three screens avoids the valley;}\\
\text{the untagged V4 stabilization fails owner simplicity.}
\end{array}}
                                                               \tag{0.5}
\]

## 1. Why the naked source has a ridge

Suppress the fixed core and write \(F=\{f_0,\ldots,f_{d+1}\}\).  Every
sharp octagon source has length \(9d+23\).  Concatenating four such sources
therefore introduces no positional mismatch between the two sides of
(0.2).

Let \(V\) be the last active two-set of one relabelled block and \(W\) the
first active two-set of the next.  At all three seams in (0.1),

\[
                         |V\cap W|=1.                    \tag{1.1}
\]

Nevertheless a crossing source window also sees the two different endpoint
coatom omissions.  For each of the \(d\) strict crossing addresses, its
union contains three active labels and all \(d+2\) fillers.  Since
\(r=d+3\) in the core-suppressed normalization, its rank is

\[
                         3+(d+2)=r+2.                    \tag{1.2}
\]

The two boundary transitions adjacent to this ridge add one further bad
Johnson pair per seam, giving \(d+1\) rather than \(d\).  Summing over the
three seams proves (0.3).  This is the exact dual of the one-letter split
valley: coordinated equal-length replacement removes the index defect, but
unprepared concatenation produces a rank-high seam.

## 2. One intersection screen closes each seam

For adjacent active endpoints \(V,W\) from (1.1), insert

\[
                         I(V,W)=K\cup(V\cap W)\cup F.     \tag{2.1}
\]

The terminal owner of the left coatom block is

\[
 K\cup V\cup(F-\{f_{d+1}\}),
\]

and the initial owner of the right coatom block is

\[
 K\cup W\cup(F-\{f_0\}).
\]

The first edge into (2.1) exchanges \(V-W\) for \(f_{d+1}\); the second
exchanges \(f_0\) for \(W-V\).  Both are Johnson edges and every displayed
owner has rank \(r\).  This proves owner legality at all three joins.

The screen is independent of the phase bit of either incident block because
both octagon phases have the same first and last active owner.  Hence the
same three screens serve both sides of (0.2).

### Residence

Every coordinate-exclusive active run entering a seam already occupies the
whole terminal coatom block, and every new exclusive active run occupies the
whole initial coatom block.  Their lengths are \(d+2\).  A filler \(f_t\)
is omitted once on each side.  The tail after its left omission, the screen,
and the head before its right omission have total length

\[
                       (d+1-t)+1+t=d+2.                 \tag{2.2}
\]

Thus no seam creates a positive run shorter than \(d+1\).  The internal
tensor theorem handles all other runs, so both screened walks are resident.
Their clipped boundary signatures agree.

## 3. Exact source halos, deadline and common cap

Take maximal depth-\(d\) erosion of each screened owner walk.  Maximal erosion
is nonempty because every \(d+1\)-owner interval inside a tensor block is
nonempty, and across a seam it contains \(V\cap W\) as well as at least one
filler.  Dilation reconstructs the owner walks exactly.

The first coatom block and last coatom block are phase-common for \(d+2\)
owner positions.  Therefore the two eroded words have literal common source
halos of length

\[
                              d+2                       \tag{3.1}
\]

on both ends.  Around each internal screen the same argument gives a
phase-common seam neighborhood.  Since the move is equal-length, every old
depth-\(d\) address retains width \(d+1\); the one-position deadline jump of
a binary split never occurs.

At each source position define

\[
                       P_p=E_p^{0110}\cup E_p^{1001}.    \tag{3.2}
\]

Both source words lie pointwise below \(P\), and both dilate to their stated
owner words.  Thus (3.2) is an exact free common-cap certificate.  As usual,
it does not imply compatibility with an independently prescribed parent cap;
that requires the screened-maximal intersection test.

## 4. Palette and OR-interface audit

Every single octagon phase pair has equal immediate lower and upper palette
multisets.  Relabelling preserves this equality, and the three inserted
screens are the same on both sides.  Hence the complete screened walks have
equal lower and upper palette multisets.

The light replay gives the following stronger source facts for every
\(1\le d\le24\).

1. The two maximal erosions have identical width-graded interval-OR
   **supports**.
2. Their graded occurrence multiplicities are not equal: after cancellation
   exactly \(d+4\) occurrences remain in each direction.
3. Their prefix supports and suffix supports each differ by one value in
   each direction.
4. The left guard \(\{a_0,a_1\}\) and right guard
   \(\{a_0,a_3\}\) make the prefix and suffix profiles pointwise equal and
   preserve equality of the complete width-graded support.

Item 1 is not promoted here to an all-depth theorem merely from a depth-24
replay.  More importantly, the two guards are OR screens, not automatically
legal internal source positions; their owner/deadline embedding remains a
separate boundary problem.

## 5. The exact owner-multiplicity obstruction

The set of active octagon owners is

\[
 \{\{z,a_i\}:0\le i<4\}\cup
 \{\{a_i,a_{i+1}\}:0\le i<4\}.                         \tag{5.1}
\]

The Klein four group generated by \(\alpha,\beta\) preserves (5.1).  Hence
all four relabelled tensor blocks have the same owner set.  Direct counting
in the screened word gives the multiplicity histogram

\[
        4^{,8d+19},\qquad 1^4,\qquad 5^3.               \tag{5.2}
\]

It has \(8d+26\) distinct owners and \(32d+95\) occurrences, as asserted in
(0.4).  This is an all-depth structural calculation, not a finite-search
observation.

Therefore the construction is directly usable only in either of the
following two scopes.

* Four already owner-disjoint prepared slots carry isomorphic labelled
  octagon blocks and the V4 equation is interpreted slotwise.
* A tagged lift is provided and is independently proved to preserve ranks,
  seam Johnson edges, palettes and the OR relation.

The present untagged four-block word supplies neither condition.  In
particular, common caps and residence do not cure owner repetition.

## 6. Replay

## 6. K2,2 shared edge tags: exact parity obstruction

Consider the proposed four shared tag rails

\[
 t_{02},t_{03},t_{12},t_{13},                           \tag{6.1}
\]

where packet `i` may carry precisely the rails incident with vertex `i` of
`K_(2,2)`.  At one aligned owner address write their binary states as

\[
                        (x_{02},x_{03},x_{12},x_{13}).   \tag{6.2}
\]

Equal owner rank forces the four tag loads

\[
 x_{02}+x_{03},\quad x_{12}+x_{13},\quad
 x_{02}+x_{12},\quad x_{03}+x_{13}                     \tag{6.3}
\]

to agree.  Exhausting the two possible values of each `x` gives exactly

\[
\begin{array}{c|c}
\text{common load}&(x_{02},x_{03},x_{12},x_{13})\\ \hline
0&(0,0,0,0)\\
1&(0,1,1,0),(1,0,0,1)\\
2&(1,1,1,1).
\end{array}                                               \tag{6.4}
\]

This is the sharp staggered-rail parity law.  At load one the active edges
form a perfect matching, so the four packets have only two distinct tag
sets: each chosen edge gives the same singleton tag to both endpoints.
Thus load-one staggering cannot distinguish all four aligned copies.  At
load two every rail is forced on and the packet tags are

\[
\begin{aligned}
T_0&=\{t_{02},t_{03}\},&T_1&=\{t_{12},t_{13}\},\\
T_2&=\{t_{02},t_{12}\},&T_3&=\{t_{03},t_{13}\}.
\end{aligned}                                             \tag{6.5}

These are distinct, but two packets paired along an edge share only the
edge tag and have different second tags.  Therefore an equality of complete
tagged masks across that cancellation pair is impossible wherever both
incident tags are present.  Pointwise block distinction and literal
edge-pair cancellation cannot simultaneously hold in this fixed shared-edge
rail model.

There is a second physical obstruction even if one temporarily ignores the
tagged cancellation.  Order the four blocks along a Hamilton path of
`K_(2,2)`, say `0,2,1,3`.  Adjacent block endpoints differ in three resources:
one active label, one exclusive tag, and one endpoint filler.  A shortest
Johnson connection uses two intermediate owners.  With no additional buffer
tag, each intermediate has the tag set of one endpoint packet and a legal
octagon active/screen state.  Since that packet contains the complete active
octagon owner/screen set, the intermediate duplicates an owner already
inside the packet.  There are exactly six duplicate occurrences, two per
seam.

The replay confirms that the constant load-two construction remains rank
legal, resident, palette-balanced, and freely common-capped.  But its eroded
width-graded source supports differ in exactly

\[
                             11d+8                       \tag{6.6}
\]

values in each direction for every audited `1<=d<=24`.  Thus the tag bank
does not merely leave a boundary mismatch: it destroys the untagged V4
source cancellation throughout a linear family.

The weakest viable replacement must relax at least one premise of this
no-go: use a private buffer tag/state at the seams, allow unequal compensated
tag loads, or prove a non-pointwise occurrence matching that never demands
full tagged-mask equality across a shared edge.  None is supplied here.

## 7. Replay

Run

```text
python3 scratch/audit_ad_v4_octagon_fourblock_commoncap_halo_20260801.py
```

The replay checks depths `1..24`, the naked ridge counts, all owner ranks and
Johnson edges after screening, palette equality, residence, maximal erosion,
literal `d+2` source halos, free common caps, graded support and multiplicity
scope, the two endpoint guards, the exact owner-multiplicity histogram, all
16 shared-edge tag states, and the constant-load-two tagged seam/source
obstructions.
