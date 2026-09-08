# A compound low-spine palette path removes the history holonomy

**Date:** 2026-08-13  
**Status:** unconditional low-spine owner/palette path algebra, exact local
residence reduction to long bridge scheduling, and a polynomial cut-load
reduction for the canonical top-`d` compiler cells.  This construction does
not reuse one ordered common history on both halves of every split and is
therefore not subject to the queue-holonomy theorem.  Literal source
planting of the polynomial repair paths and the global deep payload atlas
remain explicit gates.

## 1. The local split resources

Let the owner rank be `R`, the source depth be `d`, and put

\[
                         q=d+1.
\tag{1.1}
\]

For `4<=h<=d`, write the deleted role-zero spine edge as

\[
                         U_hU_{h+1}.
\tag{1.2}
\]

Use the integrated split notation

\[
 H_h=G_h\cup\{0\},\qquad |H_h|=R-2,
\tag{1.3}
\]

\[
 X_h=\{h+1,2h+2\},\quad
 Y_h=\{2h+1,2h+2\},
\tag{1.4}
\]

\[
 Z_h=\{2h+2,z_h\},\quad
 W_h=\{h+1,2h+1\},
\tag{1.5}
\]

and

\[
 B_h=H_h\cup Z_h,\qquad
 C_h=H_h\cup W_h.
\tag{1.6}
\]

Here `z_h` is chosen fresh from every earlier protected owner, lower
facet, and fixed endpoint; at an internal seam require in particular

\[
                         z_h\notin C_{h-1}\cup U_h.
\tag{1.6a}
\]

There are `Theta(R)` eligible exterior labels and only `O(d)` fixed
endpoints, so the choices may be made greedily.  Then

\[
 U_h-B_h,qquad C_h-U_{h+1}
\tag{1.7}
\]

are Johnson edges, the first restores the old lower facet

\[
 U_h\cap B_h=U_h\cap U_{h+1},
\tag{1.8}
\]

and the second restores the old immediate upper value

\[
 C_h\cup U_{h+1}=U_h\cup U_{h+1}.
\tag{1.9}
\]

The individual same-history source lift is not used below.

## 2. Exact consecutive-seam normal form

For an internal low seam `5<=h<=d`, put

\[
                         M_h=H_{h-1}\cap H_h.
\tag{2.1}
\]

The consecutive core differences are

\[
 H_{h-1}\setminus H_h=\{h+1,2h+2\},
 \qquad
 H_h\setminus H_{h-1}=\{2h-1,2h\}.
\tag{2.2}
\]

Since

\[
 W_{h-1}=\{h,2h-1\},
\tag{2.3}
\]

direct substitution gives the three consecutive owners

\[
 \boxed{
 C_{h-1}=M_h\cup\{h,h+1,2h-1,2h+2\},}
\tag{2.4}
\]

\[
 \boxed{
 U_h=M_h\cup\{h+1,2h-1,2h,2h+2\},}
\tag{2.5}
\]

\[
 \boxed{
 B_h=M_h\cup\{2h-1,2h,2h+2,z_h\}.}
\tag{2.6}
\]

The three owners are pairwise consecutive Johnson neighbours in the order

\[
                         C_{h-1}-U_h-B_h.
\tag{2.7}
\]

Across this triple the nonconstant coordinate membership words are

\[
\begin{array}{c|c}
\text{coordinates}&(C_{h-1},U_h,B_h)\\ \hline
h&100\\
h+1&110\\
2h&011\\
z_h&001.
\end{array}
\tag{2.8}
\]

The coordinates `2h-1,2h+2` and every member of `M_h` have word `111`.
In particular neither `010` nor `101` occurs.

### Lemma 2.1 (no internally trapped short flag)

Every nonconstant positive run or zero gap created by the fixed triple
`(2.7)` meets its left or right boundary.  No nonconstant flag is bounded
on both sides strictly inside the triple.

#### Proof

An internally bounded positive singleton would have word `010`; an
internally bounded zero singleton would have word `101`.  Both are absent
from `(2.8)`.  Every other nonconstant word in `(2.8)` reaches one boundary
of the triple. \(\square\)

This is the precise advantage of treating the entire low ladder as one
compound path.  The short three-owner pieces export clipped age profiles;
they do not contain an unrepairable short run.

## 3. The compound degree-two palette path

Delete `U_hU_{h+1}` for all `4<=h<=d`.  Omit every independent incoming
role-zero collar.  Use

\[
 U_4-B_4\leadsto C_4-U_5-B_5\leadsto C_5-U_6-
 \cdots-B_d\leadsto C_d-U_{d+1}.
\tag{3.1}
\]

For every `h`, join `B_h` to `C_h` by two long one-tag arms and a pair-tag
connector, with each arm of length at least `q` and the middle connector
of length at least `2q-1`.  Give different bridges different missing-tag
signatures and choose their far endpoints pairwise sufficiently distant.

### Theorem 3.1 (compound low-spine protected path)

Prospectively, all resources in `(3.1)` and its long bridges can be chosen
so that:

1. the complete bank is one simple owner/lower-incidence path;
2. every deleted immediate lower and upper value is restored by `(1.8)`
   and `(1.9)`;
3. all internal positive and zero flags can be scheduled with length at
   least `q`; and
4. only the two exterior endpoints export clipped flags.

The bank has `O(dR)` incidences and exposure `O(d)` on each middle-level
shore.

#### Proof

At every shared owner `U_h`, exactly two protected edges occur: the terminal
half-edge `C_(h-1)U_h` and the initial half-edge `U_hB_h`.  There is no
separate role-zero collar, so the old degree-three obstruction is absent.
The fixed endpoint resources are distinct by the split-resource collision
lemma; private missing-tag signatures separate all positive-time bridge
interiors.  Thus the bank is one simple path.

Equations `(1.8)--(1.9)` give the palette claims.  Lemma 2.1 says that every
flag created on an internal three-owner seam is clipped to an adjacent long
bridge.  The unit clipped-age inequalities hold at every Johnson boundary.
Apply the exit-arm release schedule, entrance-arm deadline schedule, and
the two-sided interval-Hall theorem on the pair-tag connector.  The arm and
connector length bounds provide the required aperture and leave flags only
at the two ends of the whole chain.

There are `d-3=O(d)` fixed seam blocks and bridges, each of length `O(R)`.
The clean one-tag arm theorem gives `O(1)` exposure per bridge on a fixed
resource star, and summing the bridges gives `O(d)`. \(\square\)

The word “prospectively” retains the usual exact hypothesis: the endpoint
event labels and missing tags must be chosen with their declared clipped
ages before the bridge orders are fixed.  The theorem schedules those
profiles; it does not assert that an arbitrary later completion has the
same profiles.

## 4. Compatibility with the retained high spine

Retain the direct role-zero spine from `U_(d+1)` upward.  For a coordinate
`x_j=2j+1`, its direct-spine positive run is

\[
                         U_{j+1},\ldots,U_{2j}
\tag{4.1}
\]

of length `j`.  If both boundary transitions of `(4.1)` lie in the retained
high spine, then `j>=d+1=q`, so the run is resident.  If one boundary lies
inside the replaced low block, the run is clipped to the final long bridge
of `(3.1)` and is handled by its boundary scheduler.

Here the last assertion is literal at the splice, rather than an appeal to
an unspecified continuation.  From

\[
 H_d=\{0\}\mathbin{\dot\cup}\{d+2,\ldots,2d\}
     \mathbin{\dot\cup}\{2d+4,2d+6,\ldots,2R-2\}
\tag{4.2}
\]

and `C_d=H_d\cup\{d+1,2d+1\}`, every odd coordinate `x_j` which is
present at `U_(d+1)` and whose insertion lies in the replaced block is
also present at `C_d`.  Explicitly, the former condition is

\[
             \left\lceil{d+1\over2}\right\rceil\le j\le d.
\tag{4.3}
\]

Thus its high-spine tail is not born at the unprotected splice: it already
meets the right endpoint of the final scheduled bridge.  When `d` is even,
the one additional coordinate `x_(d/2)=d+1` lies in `C_d` but not in
`U_(d+1)`; its run ends at the splice and is likewise clipped into that
bridge.  These are all odd-coordinate boundary cases.

Every coordinate transition on the monotone height spine occurs at most
once as an insertion and at most once as a deletion in the displayed height
range.  Hence every nonconstant zero segment on a finite retained spine is
either a prefix or suffix, unless both transitions lie in the range; in the
latter case it is the complementary segment to a run `(4.1)` and its two
exterior continuations must be included when testing cyclic zero residence.
Thus the protected high segment creates no analogue of the low internal
positive-run obstruction.  A complete cyclic zero-gap conclusion still
depends on how its two exterior ends are joined and is not asserted solely
from the finite spine.

## 5. Polynomial cut load of the canonical top-`d` compiler

Let

\[
                         p=d-3
\tag{5.1}
\]

be the number of deleted old role-zero edges.  On a fixed old owner cycle,
an interval of `q_0+1` consecutive owners has `q_0` internal edges.  For
one deleted edge there are at most `q_0` cyclic starts whose interval
crosses it.  Therefore the number of selected canonical fan cells of depth
`q_0` which can be destroyed is at most

\[
                         p q_0.
\tag{5.2}
\]

For the top source rows `1<=q_0<=d`, summing `(5.2)` gives

\[
 \boxed{
 |\mathcal D_{\rm top}|
 \le p\sum_{q_0=1}^{d}q_0
 ={(d-3)d(d+1)\over2}=O(d^3).}
\tag{5.3}
\]

This is a proof-safe upper bound before identifying repeated target values
or alternate unaffected old occurrences.  The sharper `O(pd)` estimate
would require proving that the fixed gap section chooses at most one
crossing cell per deleted edge and depth; that correlation is not used
here.

Since `d=Theta(sqrt R)`, the crude bank `(5.3)` has polynomial size
`O(R^(3/2))`.

### Lemma 5.1 (one target has a literal top-row replacement path)

Let `S` be one lost target of rank `R-q_0`, where `1<=q_0<=d`.  Choose
distinct coordinates

\[
 A=\{a_1,\ldots,a_{q_0}\},\qquad
 B=\{b_1,\ldots,b_{q_0}\}
\tag{5.4}
\]

outside `S`, and choose a set `C` disjoint from `S\cup A\cup B` of size
`q_0`.  On a sufficiently large odd ground set this is possible in the
deadline regime after allowing a fixed complement/stabilizer relabelling.
Form a shortest Johnson owner path of `q_0+1` owners whose common
intersection is exactly `S` by successively exchanging the `a_i` for the
`b_i` over a rank-`R` completion of `S`.

Then, in the maximal depth-`d` antecedent of any resident chronology which
contains this owner path consecutively with its full `d`-halo, the row
identity supplies a source interval of width

\[
                         d-q_0+1
\tag{5.5}
\]

and exact OR value `S`.

#### Proof

Take a rank-`q_0` set `A` disjoint from `S` and put
`V_0=S\cup A`, which has rank `R`.  Successively exchange each `a_i` for a
fresh `b_i`; the intersection of the `q_0+1` owners is exactly `S`.
The maximal-antecedent intersection/source-row identity maps a depth-`q_0`
owner intersection to the source interval of width `d-q_0+1`, preserving
the exact value. \(\square\)

The auxiliary set `C` in the statement is not needed for this elementary
owner path; it is useful when one packages the path with complement-paired
whiskers and endpoint facets for simultaneous lower/upper backup.  The
literal construction itself needs only `2q_0` labels outside `S`, available
because

\[
                         (2R-1)-|S|=R+q_0-1\ge2q_0.
\tag{5.6}
\]

### Theorem 5.2 (polynomial compiler-repair reduction)

Every lost canonical top-`d` target has an explicit constant-rank-stratum
family of replacement owner paths as in Lemma 5.1.  If one selects mutually
resource-disjoint copies of those paths, protects their full source halos,
and extends their union with `(3.1)` to one resident owner factor, then all
lost top-`d` compiler cells are restored literally.  The total named target
bank is polynomial by `(5.3)`.

The rank-stratified complement-paired backup theorem provides the required
owner/lower path packing and a simple factor extension at the graph level:
its hypotheses allow `O(R^(3/2))` named targets with the inverse-fan rank
profile, while `(5.3)` is no larger.  What does **not** follow from that
graph theorem is the simultaneous resident source halo around every packed
path.  That is an explicit source-host premise in this reduction.

The `q_0=1` row is already restored locally by `(1.8)` and need not be sent
to the backup theorem.  For `q_0>=3`, put `s=q_0-1`.  Then

\[
                         |S|=R-s-1,
\]

so the paired whiskered-geodesic theorem applies to the complementary
rank-`(R+s)` upper target and returns an intersection path for `S`.  The
case `q_0=2` corresponds to `s=1`, outside the stated range of that theorem.
It is covered directly by the following small-stratum lemma.

### Lemma 5.3 (the rank-`(R-2)` bank packs directly)

Let `\mathcal S_2` be the multiset of lost depth-two targets.  Then

\[
                         |\mathcal S_2|\le 2p=O(d).
\tag{5.7}
\]

Against any already fixed `O(d)` endpoint-resource bank, one can choose,
for every occurrence of `S\in\mathcal S_2`, four distinct labels
`a,b,c,e` outside `S` so that the paths

\[
 S\cup\{a,b\}\;--\;S\cup\{b,c\}\;--\;S\cup\{c,e\}
\tag{5.8}
\]

are mutually disjoint in all their named owner, lower-facet, and
upper-union resources.  Each path has common intersection exactly `S`.

#### Proof

The outside set has size

\[
                 (2R-1)-(R-2)=R+1.
\tag{5.9}
\]

For a fixed `S`, a forbidden lower facet can exclude at most one candidate
label `x` through the equality `S\cup\{x\}=L`; a forbidden owner can
exclude at most one candidate two-set; and a forbidden upper union can
exclude at most one candidate three-set.  At the moment a path is chosen,
the fixed endpoint bank and the previously chosen paths contain only
`O(d)` named resources.  Since `d=o(R)`, choose successively distinct
`b,c,a,e` outside the resulting `O(d)` forbidden singletons, pairs, and
triples.  This also works for repeated occurrences of the same target.

The two consecutive intersections in `(5.8)` are `S\cup\{b\}` and
`S\cup\{c\}`, its two unions are `S\cup\{a,b,c\}` and
`S\cup\{b,c,e\}`, and the intersection of all three owners is `S`.
The greedy exclusions therefore give precisely the claimed resource
disjointness and target identity. \(\square\)

Choose this `O(d)` bank before routing the long bridges in `(3.1)`; the
clean-arm avoidance lemma can then treat it as part of the protected
forbidden bank.  Consequently the graph-level path packing in Theorem 5.2
is complete for every `1<=q_0<=d`.  As before, converting these graph paths
into literal source cells still requires their simultaneous resident
halos; Lemma 5.3 does not silently supply those halos.

## 6. Deep compiler cells and exact global boundary

For `q_0>d`, the old owner-intersection address never gave a local source
cell: forced-pair separation shows that its entire owner interval and
forward `d`-collar are source-ineligible.  Those targets already require a
global remote payload atlas in any PBBS proof.  The compound low-spine
construction introduces only a polynomial protected exclusion bank into
that pre-existing selection problem.  A proof must choose the remote atlas
relative to this exclusion bank; it cannot claim that deep cells transport
automatically.

Combining the proved and conditional parts gives the exact frontier.

Proved here:

1. one simple degree-two compound low-spine palette path;
2. exact restoration of every deleted immediate lower and upper value;
3. absence of an internally trapped short flag at every low seam;
4. prospective biresidence after the established long-bridge scheduler;
5. compatibility of internally bounded positive runs on the retained high
   spine; and
6. a polynomial `O(d^3)` cut load for the canonical top-`d` compiler cells,
   with an explicit owner-intersection replacement for each target.

Still required:

1. simultaneous forced-envelope planting of the packed replacement paths;
2. selection of the global deep remote payload atlas relative to this
   polynomial bank;
3. zero-gap closure after the high-spine exterior ends are joined;
4. a resident antecedent on unprotected factor-completion components and
   palette-safe fusion;
5. arbitrary-width upper protection/opening beyond the named paired bank;
   and
6. the final regenerative/typed interface.

The principal structural conclusion is

\[
 \boxed{
 \text{full strict-lower deck transport is unnecessary at the bad spine:}
 \quad
 \text{replace the low owner path and repair only its polynomial selected
 compiler cut load}.}
\]

This avoids both the same-history holonomy and the adjacent full-context
cache overlap.
