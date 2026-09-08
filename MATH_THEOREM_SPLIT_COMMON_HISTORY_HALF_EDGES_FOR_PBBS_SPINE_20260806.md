# Split common-history half-edges for a stretched PBBS spine

**Date:** 2026-08-06  
**Method:** literal source-interval partition and the bounded-gap antecedent
criterion; no computation or finite search  
**Status:** unconditional local algebra and conditional physical planting.
One nonresident role-zero source edge can be replaced, for all strict-lower
occurrences, by two resident-programmable half-edges separated by a long
detour.  The PBBS role-zero edge admits distinct lower facets after enlarging
its common history core by the root coordinate.  Simultaneous all-height
planting, arbitrary-width upper backups, and the typed cap remain open.

## 1. The abstract split map

Fix a depth `delta`.  Let `H,X,Y` be pairwise arranged so that

\[
 P=H\mathbin{\dot\cup}X,
 \qquad Q=H\mathbin{\dot\cup}Y,
 \qquad |P|=|Q|=R,
\tag{1.1}
\]

and `P,Q` are Johnson adjacent.  Thus `|X|=|Y|=s` and
`|X cap Y|=s-1`.  Let

\[
 H=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_\delta
\tag{1.2}
\]

be an ordered nonempty partition.  The old source fragment is

\[
 \mathcal W=(X,C_1,\ldots,C_\delta,Y).
\tag{1.3}
\]

Choose two further `s`-screens `Z,W` such that

\[
 |X\cap Z|=s-1,
 \qquad |W\cap Y|=s-1,
\tag{1.4}
\]

and form

\[
 \mathcal W^-=(X,C_1,\ldots,C_\delta,Z),
 \qquad
 \mathcal W^+=(W,C_1,\ldots,C_\delta,Y).
\tag{1.5}

Their two owner edges are

\[
 (H+X)(H+Z),
 \qquad
 (H+W)(H+Y).
\tag{1.6}

### Theorem 1.1 (exact strict-lower split transport)

There is an occurrence-injective map from every interval of `mathcal W`
whose union has rank strictly below `R` to an interval of one of the two
fragments (1.5), preserving its width and exact union value.

#### Proof

An interval meeting both endpoint screens of (1.3) contains every history
letter and therefore contains `H+X=P`, of rank `R`.  Hence a strict-lower
interval meets at most one endpoint screen.

Map every interval meeting `X` to the identical address in `mathcal W^-`.
It stops before the final screen, so replacing `Y` by `Z` is invisible.
Map every interval meeting `Y` to the identical address in `mathcal W^+`;
the initial screen is invisible.  Map a history-only interval to its first
copy.  The two physical fragments are disjoint, so the map is injective,
and every displayed letter on an image interval is identical to its old
counterpart. \(\square\)

Consequently every matching of strict-lower targets using cells of the old
role-zero fragment transports with zero deletion.  Extra cells in the two
new fragments are harmless.

## 2. Why the full facet is too large a history

Taking `H=P cap Q` would make `s=1`.  Both edges in (1.6) would then have
the same lower facet `H`.  In the owner/lower incidence two-factor this uses
the same lower vertex twice and is forbidden.  Thus a physical split needs

\[
                         |H|\le R-2.
\tag{2.1}
\]

This is the exact reason to retain at least two screen coordinates.

## 3. The PBBS role-zero two-screen core

For the height-spine edge

\[
 U_h\longrightarrow U_{h+1}
   =U_h-\{h+1\}+\{2h+1\},
\tag{3.1}

let `G_h` be the rank-`R-3` pentagon core and put

\[
 H_h=G_h\cup\{0\}.
\tag{3.2}

Then `|H_h|=R-2`, and direct substitution gives

\[
 U_h=H_h\cup\{h+1,2h+2\},
\tag{3.3}
\]

\[
 U_{h+1}=H_h\cup\{2h+1,2h+2\}.
\tag{3.4}

Thus the role-zero edge has the two-screen form of Section 1.  Choose fresh
labels `z_h,w_h` outside the displayed core/screens and put

\[
 Z_h=\{h+1,z_h\},
 \qquad
 W_h=\{2h+1,w_h\}.
\tag{3.5}

The two half-edge lower facets are

\[
 H_h+\{h+1\},
 \qquad
 H_h+\{2h+1\},
\tag{3.6}

and are distinct.  There are `Theta(R)` choices of each fresh screen label;
only `O(sqrt R)` heights are used, so the half-edge owners and facets can be
chosen pairwise fresh before the tagged arms are planted.

The root coordinate in (3.2) is load-bearing.  A collar ending at `U_h`
may insert `0` on its final edge; with history `G_h` this event would be
outside every internal history letter, whereas it lies in `H_h`.

## 4. Direct antecedent pinning for a half-edge

Consider one half-edge `(H+X)(H+Z)` in a longer resident owner trace.  Pin
the source block

\[
 (X,C_1,\ldots,C_\delta,Z)
\tag{4.1}
\]

at positions `0,...,delta+1`.  At internal position `j`, reserve the two
forced event labels

\[
 D_j, I_{j-\delta-1}\in C_j.
\tag{4.2}

At the endpoints reserve

\[
 \{D_0,I_{-\delta-1}\}\subseteq X,
 \qquad
 \{D_{\delta+1},I_0\}\subseteq Z.
\tag{4.3}

Assume the surrounding long segments are chosen so that every displayed
letter lies in its maximal envelope.  This event prescription is possible
prospectively: each adjacent tagged arm has length `Theta(R)`, while only
`O(delta)` named insertions and deletions are prescribed.

### Theorem 4.1 (the `delta+2` pin block is an antecedent)

Replace the maximal antecedent on the positions (4.1) by the displayed
letters and leave it maximal elsewhere.  Under (4.2)--(4.3) and the envelope
premise, the resulting source word still induces the same owner trace.

#### Proof

Use the coordinatewise bounded-gap characterization.  For `g in C_j`, the
new support retains position `j`.  If the maximal carrier continues through
both ends of the block, the two new support gaps have lengths

\[
 j+1,qquad \delta+2-j,
\]

both at most `delta+1`.  If the carrier begins or ends in the block, its
forced endpoint is retained by (4.2), and only the applicable one of these
two gaps remains.

The `s-1` coordinates in `X cap Z` occur at source positions `0` and
`delta+1`, whose distance is exactly `delta+1`.  The unique coordinate in
`X-Z` has its terminal forced carrier position at `0`, and the unique
coordinate in `Z-X` has its initial forced carrier position at
`delta+1`; this is (4.3).  Coordinates outside `H union X union Z` are not
added.  Every maximal carrier is therefore hit with consecutive support
distance at most `delta+1`, so every owner equation survives. \(\square\)

Two split half-blocks at the same height require four reserved forced labels
in each `C_j`.  Since `|H_h|=Theta(R)` and `delta=O(sqrt R)`, an ordered
partition with these reserves exists for all sufficiently large `R`.

## 5. The stretched local path

The two half-edges can be placed as

\[
 U_h\longrightarrow H_h+Z_h
 \quad\leadsto\quad
 H_h+W_h\longrightarrow U_{h+1},
\tag{5.1}

where the middle arrow is two clean one-tag arms joined by a pair-tag
connector.  Its length is at least `2delta+1`.  At an intermediate `U_h`,
choose the coordinate inserted by the entering edge different from the
coordinate deleted by the leaving edge, and the coordinate deleted on
entry different from the coordinate inserted on exit.  Then no coordinate
is present only at `U_h` or absent only there.  The
two-sided aperture theorem schedules every remaining positive and zero
boundary flag through the long pieces.

This gives a literal, resident-programmable replacement for the direct
short spine edge at the local source level.

## 6. Exact remaining scope

### 6.1 A product-antichain upper-shadow bound

The arbitrary-width set-theoretic leave of a stretched edge is also
polynomial under an explicit shield hypothesis.

Let

\[
 A_0\subseteq A_1\subseteq\cdots\subseteq A_L,
 \qquad
 B_0\subseteq B_1\subseteq\cdots\subseteq B_M
\tag{6.1}
\]

be the incoming suffix-union and outgoing prefix-union chains at one cut.
Assume `L,M<=cR`.  This is exactly what remains before the full-union block
in a length-`O(R)` synchronized collar.  Every old one-cut value in the
non-full bank has the form

\[
                         A_u\cup B_v.
\tag{6.2}
\]

### Lemma 6.1 (fixed-rank product antichain)

For any cardinality `t`, the number of **distinct** sets of size `t` in
(6.2) is at most

\[
                         \min\{L,M\}+1=O(R).
\tag{6.3}
\]

#### Proof

Choose one index pair `(u,v)` for each distinct set.  If
`(u,v)<=(u',v')` coordinatewise, then

\[
 A_u\cup B_v\subseteq A_{u'}\cup B_{v'}.
\]

At equal cardinality the two sets are equal, contrary to choosing two
distinct sets.  The chosen pairs therefore form an antichain in the product
of two chains.  The width of an `(L+1)` by `(M+1)` grid is
`min{L,M}+1`. \(\square\)

Suppose now that every stretched role-zero detour has a full-ground shield,
so every interval penetrating beyond its two declared `O(R)` collars has
union `Omega`.  Suppose also that the first nontrivial collar coordinate is
outside the four central screen labels.  Then, apart from the original
rank-`R+1` target `T_h` already handled by the immediate upper backup,
every nontrivial lost value has rank at least `R+2`.

There are only an absolute number of one-cut grids per stretched edge.
For `H` heights, Lemma 6.1 gives the exact proof-safe census

\[
 |\mathcal D_s|\le C H R
 \qquad(2\le s\le R-1)
\tag{6.4}
\]

for an absolute `C`.  When `H=O(sqrt R)`, this is
`O(R^(3/2))` per excess-rank stratum.  The rank-stratified upper-backup
theorem therefore supplies mutually disjoint protected owner paths for all
these values with polynomial size and sub-half exposure.

The hypothesis that the bank is named before the unprotected factor is
completed is load-bearing.  The explicit collars and shields make the
chains in (6.1) protected data; an arbitrary later outgoing arc would not.

## 7. Conditional stretched-role-zero synthesis

Combine:

1. the two half-history edges (Sections 1--5);
2. a tagged long middle detour with the collars/shields of Section 6.1;
3. the two immediate-palette backups from
   `MATH_THEOREM_PBBS_LOW_SPINE_CUT_AND_TWO_PALETTE_BACKUP_20260806.md`;
   and
4. the rank-stratified upper backup paths supplied by (6.4).

### Theorem 7.1 (stretched role-zero protected macro)

For `H=O(sqrt R)` and `delta=O(sqrt R)`, assume the prospective choices are
made so that the named half-edge histories satisfy their forced-envelope
conditions, all declared collars/shields occupy the stated detours, and the
named owner/facet resources are pairwise disjoint except at declared path
attachments.
Then every direct role-zero PBBS spine edge may be replaced by a protected
macro with the following properties:

1. all old strict-lower source occurrences transport injectively with exact
   value and width;
2. the omitted immediate lower and upper colours are restored exactly;
3. every lost arbitrary-width upper target has a protected replacement;
4. the protected owner/lower bank is a path forest with total size
   `R^{O(1)}` and exposure `O(sqrt R)` before the upper backups and at most
   `R/3` after them;
5. the `O(H)` forced macro cores may be chained into one oriented protected
   path, while the upper-backup paths remain unoriented protected
   components; and
6. the long pieces of the forced macro cores admit simultaneous positive-run
   and zero-gap scheduling.

#### Proof

Item 1 is Theorems 1.1 and 4.1.  The immediate palette ledger is the
two-backup theorem.  Lemma 6.1 and the rank-stratified backup theorem give
item 3 and the post-backup exposure in item 4.  Unique one-tag and pair-tag
signatures separate the long pieces, while all-tag immediate-backup
resources are chosen first; hence the union is a protected path forest.
The tagged-chain theorem joins the `O(H)` forced macro cores before the
much larger unoriented upper-backup bank is added.  The two-sided aperture
theorem proves item 6. \(\square\)

The theorem is **prospective**: it gives a mutually compatible protected
macro and proves its local source word once the named event schedules are
embedded.  It does not say that an arbitrary polynomial two-factor
completion inherits the same antecedent or cap state.

## 8. Exact remaining scope

The following rows are not proved by the stretched macro theorem:

1. a proof that the unoriented upper-backup paths and the unprotected cycles
   introduced by factor completion admit one compatible biresident
   antecedent and fuse into the protected source chronology;
2. one occurrence-labelled typed common cap after compensation; and
3. regeneration of the same protected macro interface in the next Pascal
   step.

What is closed is the formerly feared local tradeoff: stretching a short
spine edge need not eject its old lower compiler cells or lose an
unbounded upper bank.  The remaining PBBS obstruction is global
completion/source fusion plus the typed occurrence cap.
