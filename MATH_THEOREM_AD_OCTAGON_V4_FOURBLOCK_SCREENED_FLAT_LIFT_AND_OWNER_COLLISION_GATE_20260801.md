# The V4 four-octagon relation has a screened flat lift, but not a simple owner factor

Date: 2026-08-01  
Lane: AD, follow-up to the internal-ray split-valley obstruction  
Status: exact flat/nonflat owner classification for the `0110 -> 1001`
four-block relation.  Exterior OR context and collision-free ambient embedding
remain open.

## 0. Outcome

The four-block relation in
`scratch/explore_h2_four_relabelled_octagon_20260801.py` is genuinely outside
the single-letter split obstruction.  It replaces four equal-length sharp
source blocks by four equal-length blocks; it inserts no source position and
does not force the decomposition-independent `d`-letter valleys of a split
`Q_p -> Z,T`.

However, concatenating the four sharp sources literally is **not** a flat
owner construction.  At each of its three raw seams, all `d` crossing
depth-`d` windows have rank `r+2`, not `r`.  Thus the raw relation is an
equal-length OR-source identity only.

There is an exact flat repair.  Work at the owner level.  Between each pair
of consecutive coatom blocks insert one phase-common rank-`r` screen owner,
then take the maximal depth-`d` erosion of the whole screened owner word.
For the two ordered V4 frames which have both the concatenated graded-deck
identity and three active-Johnson seams:

* every choice of intersection/union screen at the three seams gives a
  rank-`r` Johnson walk;
* the walk is depth-`d` resident;
* old and new owner multisets and both immediate q1 palette multisets agree;
* global maximal erosion is nonempty and exact;
* a 32-address global sharp thinning reconstructs both walks exactly;
* the two sharp sources have the same length and a pointwise common cap;
* every seam has a common maximal-erosion halo of `d+5` positions.

The construction is nevertheless not yet a literal owner factor.  In the
untagged V4 model its `4L+3` owner positions realize only `L+3` distinct owner
sets.  Almost every owner occurs four times.  A collision-free ambient
tagging or four-occurrence embedding is therefore an additional theorem,
and arbitrary tags are not known to preserve the exterior OR identity.

## 1. Why the split-valley lemma does not apply

The single-split theorem starts with one source word and changes its length:

\[
                  Q_p\longmapsto Z,T,qquad Z\cup T=Q_p. \tag{1.1}
\]

The index shift forces `d` windows containing both pieces but only `d-1`
other source letters.  Those are the rank-deficient windows.

In the V4 relation let `S_e` be the sharp octagon source in phase `e`, and
let

\[
 (g_0,g_1,g_2,g_3)=(1,\beta,\alpha,\alpha\beta).        \tag{1.2}
\]

The replacement is

\[
 g_0S_0\mid g_1S_1\mid g_2S_1\mid g_3S_0
 \quad\longleftrightarrow\quad
 g_0S_1\mid g_1S_0\mid g_2S_0\mid g_3S_1.              \tag{1.3}
\]

Both sides have four blocks of the same length.  No old block is refined,
no contraction map is asserted, and source positions do not shift.  Hence
Theorem 1.2 of the split-valley note has no hypothesis here.

For any equal-length source replacement `A -> B` in fixed exterior halos,
the exact flat condition is simply the sliding-window condition

\[
 U_i=\bigcup_{q=i}^{i+d}\widetilde Q_q,qquad
 |U_i|=r,qquad
 |U_i-U_{i+1}|=|U_{i+1}-U_i|=1                         \tag{1.4}
\]

for every affected start `i`.  Exact positionwise owner preservation is the
stronger condition that every `U_i` equal its old counterpart.  Equal source
length or equality of an internal interval deck does not imply (1.4).

## 2. The raw concatenation is uniformly off-rank

Put

\[
                  L=8d+23,qquad N=L+d=9d+23.           \tag{2.1}
\]

Each sharp source block has length `N` and dilates internally to `L`
rank-`r` owners.  Consider a raw seam between a left block ending in the
coatom block `B(V)` and a right block beginning in `B(W)`.  For the viable V4
frames, `V,W` are adjacent active 2-sets.  Every depth-`d` source window
crossing that raw seam contains active union `V union W` and the full filler
bank `Phi`.  Therefore its rank is

\[
 |K|+|V\cup W|+|\Phi|
   =(r-d-3)+3+(d+2)=r+2.                                \tag{2.2}
\]

There are exactly `d` such windows at each seam and three seams.  Thus the
raw source has `3d` rank-`r+2` rows.  It cannot be the inverse of a flat
rank-`r` chronology, despite being equal-length and despite the four-block
graded-deck relation.

## 3. Exact one-screen seam criterion

The last owner in `B(V)` and first owner in `B(W)` are

\[
 P=K\cup V\cup(\Phi-\{f_{d+1}\}),\qquad
 Q=K\cup W\cup(\Phi-\{f_0\}).                           \tag{3.1}
\]

### Theorem 3.1 (coatom one-screen criterion)

Assume `V,W` are distinct active 2-sets.  There is a rank-`r` owner adjacent
in the Johnson graph to both `P` and `Q` if and only if

\[
                            |V\cap W|=1.                 \tag{3.2}
\]

When (3.2) holds there are exactly four common neighbours.  Two are the
standard screens

\[
\begin{aligned}
 I(V,W)&=K\cup(V\cap W)\cup\Phi,\\
 U(V,W)&=K\cup(V\cup W)\cup(\Phi-\{f_0,f_{d+1}\}).
\end{aligned}                                            \tag{3.3}
\]

The other two are the crossed coatom screens obtained by taking one of the
two private active labels and the opposite endpoint filler.

#### Proof

If `|V cap W|=1`, remove the common rank-`r-2` base

\[
 K\cup(V\cap W)\cup(\Phi-\{f_0,f_{d+1}\}).             \tag{3.4}
\]

The two endpoints add disjoint two-sets.  A common rank-`r` Johnson
neighbour chooses one element from each two-set, giving exactly four; (3.3)
are two of them.  If `V,W` are disjoint, `P,Q` have Johnson distance three,
so no vertex can be adjacent to both.  \(\square\)

The exploratory V4 census has ten additive graded-deck frames.  Six satisfy
(3.2) at all three seams.  Three have the stronger concatenated graded-deck
identity, and exactly two of those three satisfy (3.2) everywhere.  They are
the two orders of

\[
 \alpha=(01)(23),\qquad \beta=(03)(12),\qquad
 \alpha\beta=(02)(13).                                  \tag{3.5}
\]

Thus (3.5), up to exchanging `alpha,beta`, is the sharp screened frame within
the audited V4 catalogue.

## 4. Screen first, then erode globally

For either phase pattern in (1.3), concatenate the four **owner** paths and
place one screen from (3.3) at every seam.  The resulting length is

\[
                            4L+3.                        \tag{4.1}
\]

Every owner has rank `r` and every consecutive pair is a Johnson edge by
Theorem 3.1.  Residence is also exact.  Each active coordinate occurring in
a screen attaches to a complete adjacent coatom block of length `d+2`.
For fillers, the only extra absences of `f_0,f_(d+1)` occur at union screens;
the shortest strict positive run is still at least `d+1`.

The endpoint active owners and the screen type depend only on the relabel
slot, not on the local octagon phase.  The immediate lower and upper palettes
at every seam are therefore identical on the two sides of (1.3).  Internal
palettes agree by the octagon tensor theorem.  Hence both complete q1 palette
multisets agree, as do the owner multisets.

Now take maximal erosion of each screened owner word.  Residence makes every
erosion letter nonempty, and the depth-`d` dilation returns the owner word
exactly.  Both sources have length

\[
                      4L+3+d=33d+95.                    \tag{4.2}
\]

The two octagon phases agree on their first and last `d+2` owner positions.
Consequently, if a screen has owner index `s`, then the maximal erosion
letters at

\[
                         s-2\le p\le s+d+2              \tag{4.3}
\]

are identical in the two four-block states.  This is a common source halo of
exactly `d+5` positions around each screen.

The eight phase-changing sharp addresses of one block lie in

\[
                  [d+4,7d+20]\subset[d,L-1].            \tag{4.4}

They are therefore strictly inside their owner block and unaffected by the
screen halos.  Starting from the pointwise intersection of the two global
maximal erosions, retain the appropriate maximal letter at those eight
addresses in each of the four blocks.  The resulting 32-address sharp
sources still dilate exactly to the screened owner words.  Positionwise
union gives an explicit common cap.

Thus maximal erosion, rather than concatenation of four separately eroded
sources, is the correct flat physical lift.  It changes the seam halos on
both sides coherently and avoids the single-split valley.

## 5. The remaining owner-collision obstruction

Flat rank and Johnson legality do not imply a simple owner factor.  In the
untagged V4 relation the double-transposition group preserves the full set of
eight active coatom blocks.  It also enlarges the seven-screen owner set by
only three values.  Hence, for every intersection/union screen choice,

\[
 \#\{\text{owner positions}\}=4L+3,qquad
 \#\{\text{distinct owner sets}\}=L+3.                 \tag{5.1}
\]

The inserted seam screens are already among these `L+3` owner values.  So
the screened construction is an exact resident Johnson **walk** and an exact
balanced exchange relation, but not a simple path/factor.

A positive factor theorem must supply four ambient occurrences whose tags
make all owners distinct while retaining:

1. the active-Johnson seam relation (3.2);
2. the common maximal-erosion halos (4.3);
3. the q1 and prescribed-cap equalities; and
4. the exterior interval-OR relation across differently tagged blocks.

Arbitrary private tags do not automatically preserve item 4.  This is the
sharp remaining embedding gate.

## 6. Replay and scope

Run

```text
python3 scratch/audit_ad_octagon_v4_fourblock_screened_flat_lift_20260801.py --write
```

The replay enumerates the ten V4 additive frames, isolates the two screened
concatenated frames, and checks `5<=d<=24`: raw seam ranks, all eight I/U
screen patterns, rank/Johnson legality, residence, q1 multisets, global
maximal erosion, 32-address sharp reconstruction, common caps, common halos,
and the exact owner-collision count.  It does not claim contextual exterior
OR transparency or construct distinct ambient tags.
