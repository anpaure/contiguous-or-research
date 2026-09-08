# Mixed coatom-screen tensor: an all-depth simple transparent ECO path

Date: 2026-08-01  
Lane: independent `B(k)+O(1)` construction audit  
Status: exact all-`d` simple-path macro theorem.  The all-lower-screen draft
has four repeated vertices, but replacing four prescribed screens by their
upper common neighbours removes every repetition while preserving all
coverage and residence rows.  No unconditional additive-constant upper bound
is claimed: recursive availability, topology, and compiler composition remain.

## 0. Verdict

The coatom-screen construction is algebraically correct, with one necessary
precision correction and one exact repair.

1. Its old and new distinct interval-OR **supports** are equal.  Interval
   multiplicities are not equal.
2. The all-lower-screen draft has four repeated screen occurrences.  At
   transition indices `1,3,5,7` (zero based), use the upper common Johnson
   neighbour instead.  The resulting mixed-screen word is simple.

For every `d>=0` and every target rank
`r>=d+4`, the two tensor words

* have length `12d+35` and constant rank `r`;
* are Johnson-adjacent at every consecutive pair and have the same endpoints;
* have the same physical multiset;
* have identical pointwise prefix/suffix OR signatures;
* have equal distinct internal interval-OR support, of size `12d+68`;
* have identical clipped boundary residence states; and
* have every internal positive run of length at least `d+1`.

This is the first literal lift of the contracted ECO connector that closes
crossing upper transport, internal upper transport, and growing-`d`
residence simultaneously **as a simple Johnson path**.  The remaining work
is no longer a local retained-path construction: one must place these macros
in the recursive topology and fixed compiler-cap fibre with the quadratic
menu and linear conflict code of the selection theorem.

## 1. Active connector data

Use connector row `1` of
`scratch/independent_eco_sixseam_signature_connectors_20260731.audit.json`.
On the active universe

\[
                       \{e,a,b,c,d,\infty\},
\]

the old and new rank-three words are

```text
old: Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab
new: Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

Call them `V^0=(V^0_0,...,V^0_11)` and
`V^1=(V^1_0,...,V^1_11)`.  The contracted audit proves

\[
 \{V^0_j\}_j=\{V^1_j\}_j,\qquad
 \Sigma_\vee(V^0)=\Sigma_\vee(V^1),\qquad
 \mathcal I_\vee(V^0)=\mathcal I_\vee(V^1),              \tag{1.1}
\]

where the last equality is equality of distinct interval-union supports.
The common support in (1.1) has `25` values.

The eleven consecutive intersections have the same counter in both phases:

\[
 \{3^2,5^2,9^2,40^2,17,34,36\}.                        \tag{1.2}
\]

Here masks are decimal on the six active coordinates.  Thus there are eleven
screen occurrences, seven screen colours, and exactly four extra
occurrences.

## 2. Construction

Put

\[
 n=d+2,qquad F=\{f_0,\ldots,f_{n-1}\},qquad
 C_i=F\setminus\{f_i\}.                                  \tag{2.1}
\]

Take a fixed set `K`, disjoint from the active and filler coordinates, of
size

\[
                            |K|=r-d-4.                    \tag{2.2}
\]

For an active owner `V`, define its coatom block

\[
 B(V)=\bigl(K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}\bigr). \tag{2.3}
\]

Between consecutive active owners insert the full-filler screen

\[
 S(V,W)=K\cup(V\cap W)\cup F.                            \tag{2.4}
\]

For `epsilon in {0,1}`, the expanded word is

\[
 \widetilde V^\epsilon=
 B(V^\epsilon_0),S(V^\epsilon_0,V^\epsilon_1),
 B(V^\epsilon_1),\ldots,
 S(V^\epsilon_{10},V^\epsilon_{11}),B(V^\epsilon_{11}). \tag{2.5}
\]

## 3. Rank, adjacency, endpoints, and physical multiset

Every block letter has rank

\[
               (r-d-4)+3+(n-1)=r,                       \tag{3.1}
\]

and every screen has rank

\[
               (r-d-4)+2+n=r.                           \tag{3.2}
\]

Consecutive coatoms `C_i,C_(i+1)` exchange `f_i` and `f_(i+1)`, so adjacent
letters inside a block are Johnson-adjacent.  If `V,W` are consecutive
active owners, they exchange one active coordinate.  The last letter of
`B(V)` and `S(V,W)` exchange that departing active coordinate with the
missing filler; `S(V,W)` and the first letter of `B(W)` make the reverse
exchange with the entering active coordinate.  Hence every consecutive pair
in (2.5) is Johnson-adjacent.

The length is

\[
                       12n+11=12d+35.                    \tag{3.3}
\]

The first and last active owners agree in the two phases, and the coatom
order is fixed, so the physical endpoints agree.  Equation (1.1) gives the
same multiset of block letters; (1.2) gives the same multiset of screens.
Therefore the complete physical multisets agree.

## 4. Exact prefix/suffix transparency

At a corresponding position inside block `j`, the old/new active prefix
unions are equal by (1.1).  The fixed core and filler coatom are identical.
At a screen, `V_j intersect V_(j+1)` is already contained in the active
prefix through `V_j`, while the screen completes the same full filler `F` in
both phases.  Hence every prefix OR agrees pointwise.  The suffix proof is
the reverse argument: the screen intersection is contained in the next
active owner.  Thus

\[
              \Sigma_\vee(\widetilde V^0)
               =\Sigma_\vee(\widetilde V^1).             \tag{4.1}
\]

This is the strongest crossing-interval interface; compressed prefix/suffix
deck equality follows immediately.

## 5. Exact internal OR-support decomposition

Every singleton interval in a block has value

\[
                        K\cup V\cup C_i.                  \tag{5.1}
\]

Every singleton screen has value

\[
                        K\cup I\cup F,qquad I=V\cap W.   \tag{5.2}
\]

Every other interval contains either two different coatoms or a screen, so
its filler union is all of `F`.  After suppressing `K union F`, its active
union is exactly the union of a nonempty contiguous interval of the active
word.  Conversely every active interval union is realized with full filler:
use the corresponding expanded block range, and for a one-owner interval
use two letters in that owner's block (`n>=2`).  Therefore

\[
\begin{aligned}
 \mathcal I_\vee(\widetilde V^\epsilon)
  ={}&\{K\cup V\cup C_i:V\in\mathcal V,\ 0\le i<n\}\\
   &\cup\{K\cup I\cup F:I\in\mathcal S\}\\
   &\cup\{K\cup F\cup U:U\in\mathcal I_\vee(V^\epsilon)\}, \tag{5.3}
\end{aligned}
\]

where `mathcal V` is the common twelve-owner set and `mathcal S` is the
common seven-colour screen set.  The three families in (5.3) are disjoint:
the first misses one filler, the second has active rank two, and the third
has active rank at least three.  Equations (1.1)--(1.2) prove exact old/new
support equality and the count

\[
                       12n+7+25=12d+56.                  \tag{5.4}
\]

This is not multiplicity equality.  Direct endpoint counting gives exactly

\[
                         5(n+1)^2=5(d+3)^2               \tag{5.5}
\]

unmatched interval occurrences in each direction.  Coverage uses support,
so (5.5) is harmless for the upper bank, but it must not be silently stated
as a multiset identity.

## 6. All-depth residence and boundary state

A fixed-core coordinate is present throughout.  An active-coordinate run of
`ell>=1` active owners becomes

\[
                         \ell n+(\ell-1)=\ell(d+3)-1      \tag{6.1}
\]

consecutive occurrences: every containing block contributes `n`, and every
internal screen contributes one.  Its minimum is `n=d+2`.

For a filler coordinate `f_i`, each block has exactly one zero, at the
`i`-th coatom, and every screen contains `f_i`.  Between successive zeros
there are

\[
                         (n-1-i)+1+i=n=d+2               \tag{6.2}
\]

ones.  Thus every internal positive run in either expanded phase has length
at least `d+2`, strictly above the required `d+1`.

The first and last active blocks are identical old/new.  Active coordinates
present there already contribute `n>=d+1` and hence have the same saturated
clipped record; absent coordinates give zero.  Each filler has the same
prefix length `i` and suffix length `n-1-i`, and the core is saturated.
Therefore the complete clipped old/new boundary states agree.  Any one
exterior that completes the short filler boundary runs works for both phases.

## 7. The exact four-duplicate obstruction

All `12n` block letters are distinct: equality determines the active owner
and the omitted filler.  No block letter equals a screen, since a block
misses one filler and a screen contains all of `F`.

The screen counter (1.2), however, has four colours of multiplicity two.
Consequently

\[
 \begin{aligned}
  \#\text{occurrences}&=12n+11,\\
  \#\text{distinct physical sets}&=12n+7,\\
  \#\text{duplicate occurrences}&=4.                    \tag{7.1}
 \end{aligned}
\]

Thus the all-lower version (2.5) is only a Johnson-adjacent walk.  The next
section gives an exact splitter with no extra positions.

## 8. Mixed screens remove all four repetitions

Index the eleven transitions by `j=0,...,10` and put

\[
 {cal U}=\{1,3,5,7\},\qquad
 {cal L}=\{0,2,4,6,8,9,10\}.                              \tag{8.1}
\]

At a lower transition use (2.4).  At an upper transition use the other
common Johnson neighbour

\[
 S^+(V,W)=K\cup(V\cup W)\cup
             \bigl(F\setminus\{f_0,f_{n-1}\}\bigr).       \tag{8.2}
\]

Equation (8.2) has rank `r`.  Relative to the last letter
`K union V union C_(n-1)` of the left block, it removes `f_0` and adds the
entering active coordinate.  Relative to the first letter
`K union W union C_0` of the right block, it removes the departing active
coordinate and adds `f_(n-1)`.  Hence both incident pairs are Johnson edges.

The selected lower active colours are, in the old and new phases respectively,

```text
old: 24 09 28 22 03 11 05
new: 22 09 28 24 05 11 03,
```

and the selected upper active colours are

```text
old: 2d 39 2e 2b
new: 2b 39 2e 2d.
```

Thus both phases use the same seven distinct lower colours and the same four
distinct upper colours.  Their filler profiles are respectively `F` and
`F-{f_0,f_(n-1)}`, while every block letter misses exactly one filler.
Consequently all `12n+11` physical sets are distinct and the old/new physical
sets agree as a set, not merely as a multiset.

### 8.1 External signatures

At a lower screen the proof of Section 4 is unchanged.  At an upper screen,
the active contribution is `V_j union V_(j+1)`.  The prefix through that
screen is therefore the original active prefix through `j+1`, which agrees
old/new by (1.1); the suffix is the original suffix from `j`, which also
agrees.  The filler profile at corresponding positions is identical.
Hence the mixed words retain pointwise prefix/suffix OR equality.

### 8.2 Internal deck

The exact mixed internal support is the disjoint union of four common
families:

\[
\begin{array}{ll}
 K\cup V\cup C_i,
   & V\in{cal V},\ 0\le i<n;\\[2mm]
 K\cup I\cup F,
   & I\in{cal S}^-;\\[2mm]
 K\cup U\cup R,
   & U\in{cal S}^+,\quad
     R\in\{F-\{f_0,f_{n-1}\},F-\{f_0\},F-\{f_{n-1}\}\};\\[2mm]
 K\cup F\cup Q,
   & Q\in\mathcal I_\vee(V^\epsilon).
\end{array}                                                   \tag{8.3}
\]

Indeed, an upper screen alone gives the first `R` in its row; joining it to
the left final coatom or right initial coatom gives the other two.  Every
other nonsingleton interval contains full `F` and collapses to one contiguous
active interval union exactly as in Section 5.  The common palettes displayed
above and (1.1) prove equality.  The four families are separated by filler
profile and active rank, so the support size is

\[
                          12n+7+3\cdot4+25=12d+68.        \tag{8.4}
\]

### 8.3 Residence

Active-coordinate runs still contain at least one whole block, hence at
least `n=d+2` positions.  A filler `f_i` with `0<i<n-1` occurs in every
screen and retains the length-`n` calculation (6.2).  At an upper screen,
`f_0` and `f_(n-1)` are absent.  This can shorten their adjacent positive run
only to

\[
                              n-1=d+1,                   \tag{8.5}
\]

which is exactly legal.  The first and last blocks are unchanged, so the
clipped boundary-state proof also survives.

We have therefore proved:

> **Mixed coatom-screen theorem.**  For every `d>=0` and `r>=d+4`, the two
> row-1 ECO phases admit length-`12d+35` simple rank-`r` Johnson paths with
> the same endpoints and physical set, identical pointwise prefix/suffix OR
> signatures, equal distinct internal interval-OR support, equal clipped
> boundary states, and minimum internal positive-run length `d+1`.

This theorem closes the local retained-path macro.  It does not by itself
prove that a quadratic atlas of such macros is simultaneously available in
one recursive forest/common-cap fibre.

The choice (8.1) is not isolated.  Exhausting the `2^11` lower/upper screen
patterns finds exactly `16` for which the lower palettes agree and are simple
and the upper palettes agree and are simple.  Each gives the same symbolic
transport and residence proof.

### 8.4 Support, topology, and the remaining selection rows

The slot has exactly `12d+35=O(d)` physical vertices.  More strongly, its two
phases are simple Hamilton paths on the **same** vertex set with the same
ordered boundary pair.  Therefore any family of vertex-disjoint prepared
slots forms a subset-closed topology cube: switching an arbitrary subset
preserves the global path/forest topology and physical owner set.  This
closes U4 of the quadratic-list theorem once disjoint placements are given;
it is not merely pairwise topology safety.

Consequently U1--U4 are now explicit on each labelled coatom-screen slot.
If a reachable anchor supplies `m^2` labelled active connectors and the
remaining physical/compiler failures have vertex-cover number at most `Kd`,
then the theorem of the companion macro note leaves

\[
                              m^2-Kmd                         \tag{8.6}
\]

eligible slots.  Since each slot exports `O(d)` physical/conflict tokens,
external token load `O(m)` gives `O(md)` cross-list conflict exactly as
before.  What is **not** proved here is that the actual recursive forest
exposes those `m^2` labelled embeddings with one fixed unused compiler basis
and the required token-load code.  U5 and global availability, rather than
deck, residence, or local topology, are now the sharp missing rows.

### 8.5 Planting into the original all-six ECO atom

The tensor can retain the literal original owners and attachment endpoints.
Let the suppressed common core of the full all-six atom be

\[
                              G=H\setminus\{e\},\qquad |G|=r-3. \tag{8.7}
\]

Choose `F_0 subset G` with `|F_0|=d+1`, put `K=G-F_0`, and choose one fresh
coordinate `p` outside the active atom.  Set

\[
                    F=F_0\cup\{p\}.                       \tag{8.8}
\]

The coatom missing `p` satisfies

\[
                    K\cup V\cup(F\setminus\{p\})=G\cup V, \tag{8.9}
\]

so every block contains its original full owner exactly once.  Order the
fillers as `(g_0,...,g_d,p)` in blocks two through twelve.  In the first
block use the missing-filler order

\[
                    C_p,C_{g_1},\ldots,C_{g_d},C_{g_0},      \tag{8.10}
\]

and make transition `0` an upper screen with filler part `F-{p,g_0}`.
Then the first and last tensor vertices are exactly the original first and
last owners.  The block set and the lower/upper screen filler families are
unchanged.  For the deck row, an interval meeting two screens crosses a
complete coatom block and fills `F`; every non-full-`F` exception therefore
uses one block cell, or one screen with at most one adjacent boundary
coatom.  These exceptions are determined by the common selected active
screen colours, so the pointwise signature/deck proof remains valid even for
the two schedules containing consecutive upper screens.

Residence also survives (8.10).  Coordinate `p` has exactly `n-1=d+1`
positive cells before the transition-zero upper screen.  Coordinate `g_0`
has consecutive zeros at the last first-block coatom, the upper screen and
the first next-block coatom.  All subsequent filler gaps have the original
lower bound `n-1=d+1`.  Hence the planted tensor has the same `d+1` floor
and equal boundary states.

For a fixed full atom, if `P` fresh coordinates are permitted, this gives at
least

\[
                    4P{r-3\choose d+1}                    \tag{8.11}
\]

labelled planted tensors before quotienting symmetries.  Exactly four of the
sixteen owner-simple patterns pass both immediate palettes with the endpoint
rotation (8.10); their upper-screen sets are

```text
{0,2,4,6,8,10},
{0,2,3,4,6,8,10},
{0,2,4,5,6,8,10},
{0,2,3,4,5,6,8,10}.
```

The previously written order `C_p,C_g0,...,C_gd` with transition zero lower
fails lower-q1 equality for all eight claimed schedules.  Its factor eight
is only a U1--U4 slot count when the immediate palettes are omitted.

Varying the two remaining active labels still gives a quadratic inventory
of **distinct candidate-dependent planted slots**, but not a menu within one
fixed incumbent slot.  A fixed old word recovers the ordered active labels;
distinct choices differ in at least three full coatom blocks.  Therefore a
global task theorem needs an actual planted-slot bank and a task-to-slot
matching, rather than treating relabellings as post-hoc alternatives at one
anchor.

Equation (8.11) is a local planted-slot count, not a global packing theorem
and not a fixed-incumbent menu.  To use
it in the repaired ECO forest one must ensure:

1. the `12d+35` tensor vertices are already owned by, or exchanged into, the
   prepared slot rather than appended to the word length;
2. fixed block vertices shared by alternatives are private to that task
   anchor (or exported as conflict tokens);
3. selected tensors at different anchors have disjoint physical interiors;
   and
4. the same trace-guarded unused compiler basis survives.

The endpoint condition is now exact and free: it is inherited from the
original all-six atom.  Physical owner availability/private-halo packing and
U5 are the remaining planting conditions.

There is an exact token form of the first condition.  Remove the twelve
planted original owners from a tensor and call the remaining

\[
                         (12d+35)-12=12d+23              \tag{8.12}
\]

rank-`r` sets its **new-owner interior**.  Vertex-disjoint source slots are
simultaneously plantable precisely when their new-owner interiors are
pairwise disjoint and avoid every protected owner outside the slots (or when
an explicitly certified owner exchange supplies the collisions).  This
condition is phase-independent because both tensor phases use the same set.
Thus these `12d+23` owner names form a complete physical conflict-token row.
If any token appears in at most `lambda` choices of another task list, the
owner contribution to pairwise conflict is at most

\[
                            (12d+23)\lambda.             \tag{8.13}
\]

The desired `lambda=O(m)` is exactly the remaining private-anchor/load
statement; it would give `O(md)` without another upper-shadow calculation.

## 9. Frozen audit

The dependency-free replay is

```text
scratch/audit_independent_eco_coatom_screen_tensor_20260801.py
  a190d6a3c3bb07cb47eb9ca81802af8b965cfd58591e621bd049a37cd8833ed9
scratch/independent_eco_coatom_screen_tensor_20260801.audit.json
  09ce392df51a47dee9f09566b3650a8b323ef350b61a5a5dc705afb75b402621
```

It instantiates `d=0,...,12` and separately verifies every symbolic ledger
used above.  It reports

```text
PASS_ECO_MIXED_COATOM_SCREEN_TENSOR_SIMPLE_PATH
```

Its canonical payload SHA-256 is
`515c4607c2aaad9eb644a848f5ecb47aab35751060becba1bff6001e6b244d3e`.

Dependencies:

* `MATH_THEOREM_INDEPENDENT_ECO_SIXSEAM_SIGNATURE_CONNECTOR_AND_FRAGMENT_LIFT_20260731.md`;
* `MATH_THEOREM_COMPRESSED_PREFIX_SUFFIX_DECK_TRANSPARENCY_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_UNION_TRANSPARENT_RESIDENT_ECO_MACRO_SELECTION_20260731.md`.
