# The deleted PBBS role-zero edge has one integrated source-coherent palette split

**Date:** 2026-08-13  
**Status:** unconditional **single-height** set/source theorem and
prospective isolated resident macro.  One split common-history macro
transports every strict-lower occurrence, restores the deleted lower colour
on its first half-edge and the deleted upper colour on its last half-edge,
and admits a long tagged middle detour.  These local macros cannot be
concatenated through `d+1` consecutive literal spine junctions while using
the same ordered history on both halves: the exact shift-holonomy
obstruction is proved in
`MATH_OBSTRUCTION_PBBS_SPLIT_ROLEZERO_COMMON_HISTORY_HOLONOMY_20260813.md`.
Thus no complete high-bank or factor-extension claim is made here.

## 0. Statement

Let

\[
 A=U_h,
 \qquad D=U_{h+1},
 \qquad L_h=A\cap D,
 \qquad T_h=A\cup D                                  \tag{0.1}
\]

be one deleted role-zero PBBS spine edge at height `h`.  There are two
auxiliary rank-`R` owners `B_h,C_h` such that

\[
                         A-B_h\leadsto C_h-D         \tag{0.2}
\]

has all the following properties.

1. `A B_h` and `C_h D` are Johnson edges with distinct lower colours.
2. The first half-edge restores the deleted lower ticket exactly:
   
   \[
                         A\cap B_h=L_h.              \tag{0.3}
   \]
3. The last half-edge restores the deleted upper ticket exactly:
   
   \[
                         C_h\cup D=T_h.              \tag{0.4}
   \]
4. A single common-history split gives an occurrence-injective,
   width- and value-preserving map from every strict-lower source interval
   of the deleted edge to one of the two half-edges.
5. `B_h` and `C_h` may be joined by two long one-tag arms and a pair-tag
   connector so that every internal positive run and zero gap has length
   at least `q=d+1`, while the two half-edge pin blocks are literal
   depth-`d` antecedents under their exact forced-envelope conditions.

Thus one deleted role-zero edge has a source-coherent local replacement
which retains its strict-lower occurrence transport and both immediate
palette targets.  Separate isolated edges `f_h^-`,`f_h^+` are unnecessary
at this one interface.  Simultaneous use at all heights is a separate
problem.

## 1. Exact screens and palettes

Let `G_h` be the common rank-`R-3` core of the height-`h` pentagon and put

\[
                         H_h=G_h\cup\{0\},
 \qquad                  |H_h|=R-2.                 \tag{1.1}
\]

The deleted role-zero endpoints are

\[
 A=H_h\cup X_h,
 \qquad X_h=\{h+1,2h+2\},                           \tag{1.2}
\]

\[
 D=H_h\cup Y_h,
 \qquad Y_h=\{2h+1,2h+2\}.                         \tag{1.3}
\]

Choose one label

\[
 z_h\notin H_h\cup X_h\cup Y_h                    \tag{1.4}
\]

and define

\[
 Z_h=\{2h+2,z_h\},
 \qquad W_h=\{h+1,2h+1\},                          \tag{1.5}
\]

\[
 B_h=H_h\cup Z_h,
 \qquad C_h=H_h\cup W_h.                           \tag{1.6}
\]

Every displayed screen is disjoint from `H_h` and has size two, so all
four owners have rank `R`.  Directly,

\[
 A\cap B_h=H_h\cup\{2h+2\}
           =A\cap D=L_h,                            \tag{1.7}
\]

and

\[
 C_h\cup D
 =H_h\cup\{h+1,2h+1,2h+2\}
 =A\cup D=T_h.                                     \tag{1.8}
\]

The last half-edge lower colour is

\[
 C_h\cap D=H_h\cup\{2h+1\},                       \tag{1.9}
\]

which differs from `(1.7)`.  The first half-edge upper colour is

\[
 A\cup B_h=H_h\cup\{h+1,2h+2,z_h\},               \tag{1.10}
\]

which differs from `(1.8)` because `z_h` is fresh and `2h+1` is absent.
Thus the two half-edges do not repeat either immediate palette.

The choice of `W_h` is load-bearing.  The generic split theorem used a
fresh label on both halves and then needed separate palette-backup edges.
Here

\[
                         W_h=X_h\triangle\{2h+1,2h+2\}
\]

is selected so that the last half-edge itself has union exactly `T_h`.

## 2. Literal strict-lower split transport

Partition the common history into nonempty letters

\[
 H_h=C_1\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}C_d,
 \qquad \mathcal C=(C_1,\ldots,C_d).               \tag{2.1}
\]

The source fragment of the deleted edge is

\[
                         \mathcal W=(X_h,\mathcal C,Y_h).
\tag{2.2}
\]

Replace it by the two disjoint fragments

\[
 \mathcal W^-=(X_h,\mathcal C,Z_h),
 \qquad
 \mathcal W^+=(W_h,\mathcal C,Y_h).                \tag{2.3}
\]

Their owner hinges are precisely `A B_h` and `C_h D`.

### Theorem 2.1 (exact strict-lower occurrence injection)

Every occurrence of every interval in `mathcal W` whose OR has rank below
`R` maps injectively to an interval of `mathcal W^-` or `mathcal W^+` with
the same width and exact OR value.

#### Proof

An interval meeting both screens of `mathcal W` contains all of `H_h` and
`X_h`, hence contains the owner `A` of rank `R`.  A strict-lower interval
therefore meets at most one screen.

Map intervals meeting `X_h` to the identical left address in
`mathcal W^-`; they do not see its terminal screen `Z_h`.  Map intervals
meeting `Y_h` to the identical right address in `mathcal W^+`; they do not
see its initial screen `W_h`.  Map history-only intervals to their first
copy.  The two fragments are physically disjoint, so the map is injective.
Every image uses the same literal source letters and therefore has the same
width and value.  \(\square\)

Consequently every cell-based strict-lower compiler assignment supported
on the deleted role-zero fragment transports with zero deletion.  Combining
this map with the unchanged/common-history maps on roles `1,2,3,4` gives an
occurrence injection for the complete old five-role strict-lower bank.

## 3. Direct source pinning and residence

Give each half-edge its own literal copy of the history `(2.1)`.  In a
longer prospective resident owner trace, pin the two source blocks
`mathcal W^-`,`mathcal W^+`.  At each internal history position reserve
the exact forced event pair; at the screens reserve the terminal/initial
forced labels.  If every displayed letter lies in its maximal source
envelope, the bounded-gap antecedent theorem proves that each length-`d+2`
pin block induces its two declared owners.

Join `B_h` to `C_h` as follows.  Both endpoints initially contain the full
global tag reservoir.  At `B_h`, take an exit whisker deleting a private
tag `a_h`; at `C_h`, take the right-dual entrance whisker deleting a
different private tag `b_h` when read outward from `C_h`.  Continue from
the two one-tag endpoints by shortest one-tag arms of length at least `q`,
choose their far endpoints at Johnson distance at least `2q-1`, and join
those endpoints by the corresponding pair-tag geodesic.  Thus `B_h` and
`C_h` keep their unique half-edge plus one whisker
incidence, while every positive-time arm resource misses one tag and the
connector interior misses the pair.  Missing-tag signatures separate the
long interior from all-tag half-edge owners and from macros at other
heights.

The two-sided interval-Hall scheduling theorem orders every deletion and
insertion on the long arms/connector so that all positive runs and zero
gaps meeting its seams have length at least `q`.  The two half-edge pin
blocks already keep every common coordinate through `d+1` owner windows.
For the screen labels:

* `h+1` is present at the left endpoint `A` and at the right auxiliary
  owner `C_h`; it need not remain present across the entire detour, and its
  deletion/insertion events are scheduled so both resulting runs and the
  intervening zero gap have length at least `q`;
* `2h+1` is present at `C_h` and the final owner `D`;
* `2h+2` is present at `A,B_h,D`; its left/right endpoint age profiles are
  passed to the two-sided scheduler, which either keeps it throughout or
  gives any deletion/reinsertion a gap of length at least `q`;
* `z_h` occurs only on the left auxiliary screen and is given its complete
  positive/zero aperture by the left arm.

The event orders on the arms are chosen against these endpoint clipped-age
profiles.  Therefore none of these coordinates acquires a short internal
run or gap.  Only the two exterior ends of the complete forced chain export
clipped flags, which are handled by the same long-arm chain construction.

This proves the local biresidence assertion prospectively.  It does not
claim that an arbitrary later two-factor completion is resident.

## 4. Prospective cross-height resource planting

The generic fresh-resource proof for the split half-edges applies to
`B_h`: one has `Theta(R)` choices of `z_h`, while only `O(H)` protected
owners/facets have been reserved.  The owner `C_h` is fixed rather than
fresh.  It therefore needs a literal collision audit.

### Lemma 4.1 (fixed terminal half-owner is new)

For high heights `h,h'>=4`, the owner

\[
 C_h=H_h\cup\{h+1,2h+1\}                         \tag{4.1}
\]

is not one of the ten pentagon owners `P_(h',i),Q_(h',i)`.  Its lower
colour

\[
 J_h=H_h\cup\{2h+1\}                              \tag{4.2}
\]

is not an old or new pentagon lower colour.  The pairs `(C_h,J_h)` are
distinct across heights.

#### Proof

At its own height, subtracting `G_h` reduces `C_h` to the active triple
`{0,h+1,2h+1}`.  The five tail screens and five head screens are

\[
\begin{array}{c|c|c}
i&X_i=P_i\setminus G_h&Y_i=Q_i\setminus G_h\\ \hline
0&\{0,h+1,2h+2\}&\{0,1,2h+2\}\\
1&\{h+1,2h+1,2h+2\}&\{0,2h+1,2h+2\}\\
2&\{2,h+1,2h+1\}&\{2,2h+1,2h+2\}\\
3&\{0,2,h+1\}&\{0,2,2h+1\}\\
4&\{0,1,h+1\}&\{0,1,2\}.
\end{array}                                            \tag{4.3}
\]

The triple of `C_h` occurs nowhere in `(4.3)`.  Intersecting the relevant
tail/head triples likewise shows that the active pair `{0,2h+1}` of
`J_h` is absent from every old/new lower role.

Across heights, the fixed interval/run profile of `G_h` recovers `h`, as
in the standard pentagon disjointness proof; the same argument with one or
two displayed active labels proves no equality with a different-height
owner/facet.  In particular a putative equality would force the same
length of the initial block `3,...,h` and hence `h=h'`, already excluded by
the table.  The same profile proves `(C_h,J_h)` distinct across heights.
\(\square\)

This proof is symbolic.  A direct exact replay through all heights for
`8<=r<=30` independently found no owner or lower-colour collision; it is
only corroboration.

Choose every `z_h` greedily to avoid the fixed terminal halves and all
previous resources.  Enlarge the global tag bank before making these
choices.  All half-edge endpoints contain every tag; every positive-time
arm/collar owner and lower facet misses its private tag, and every pair-tag
connector misses its unique tag pair.  Therefore the usual tag-signature
argument separates all long interiors after the finite all-tag endpoint
audit above.

## 5. Arbitrary-width upper witnesses

The strict-lower split is exact, and the deleted immediate palettes are
restored by `(1.7)--(1.8)`.  Longer exterior intervals need a shield; this
cannot be inferred from the half-edge algebra alone.

Place a full-ground cumulative-union collar on each declared incoming and
outgoing arm before completing the unprotected factor.  Every interval
penetrating beyond a collar has value `[2r+1]`.  Before saturation, the
incoming suffix unions and outgoing prefix unions are two nested chains of
length `O(R)`.  At a fixed target rank, their product has antichain width
`O(R)`.  Hence the complete lost target bank over `H=O(sqrt R)` heights has

\[
                         |\mathcal D_s|=O(HR)
 \qquad(2\le s\le R-1).                           \tag{5.1}
\]

The rank-stratified backup theorem chooses one mutually resource-disjoint
owner-path witness for every such target, with polynomial total size and a
fixed sub-half exposure margin.  Because the collars/shields are protected
before the factor is completed, the target bank is prospectively fixed;
the later completion cannot change it.

Thus arbitrary-width support has no unbounded unresolved leave at the
graph level.  The new witnesses are upper minors conditional on the final
source antecedent; they do not themselves supply that antecedent or the
typed cap.

## 6. Exact simultaneous boundary

At an interior spine owner one has

\[
                         D_{h-1}=A_h=U_h.
\tag{6.1}
\]

Therefore inserting the present two-ended macros on top of the old
all-five-tail collar forest would give degree three at `U_h`: the role-zero
incoming collar, the terminal half-edge of height `h-1`, and the initial
half-edge of height `h` would all be incident there.  Omitting the separate
role-zero collar reduces the graph degree to two and concatenates the
macros into

\[
 \cdots-C_{h-1}-U_h-B_h\leadsto C_h-U_{h+1}-B_{h+1}-\cdots.
\tag{6.2}
\]

But literal source overlap at these junctions forces the ordered histories
to shift by one block.  After `d+1` junctions the shift requires

\[
                         X_{h+d}=Y_{h-1},
\tag{6.3}
\]

which is false for the explicit PBBS screens.  The cited holonomy note
contains the complete proof.  Long middle arms do not repair this when the
same history is required on both halves of each macro.

Consequently Sections 1--5 prove a local macro and a polynomial
prospective witness census, not a simultaneous protected factor.  A valid
global theorem must either construct a genuine history-changing bridge or
move the strict-lower transport to auxiliary rails so that the input and
output histories of `(6.2)` may differ.  It must then separately prove
joint forced-envelope planting, fusion of unprotected cycles, the typed
cap, and regeneration.

What is removed is precisely the single-height role-zero incompatibility:

\[
\boxed{
\text{one deleted spine edge}
\; + \;
\text{five-role strict-lower transport}
\; + \;
\text{both immediate palettes}
\; + \;
\text{prospectively resident long detour}
\; + \;
\text{polynomial all-width backup}.}
\]
