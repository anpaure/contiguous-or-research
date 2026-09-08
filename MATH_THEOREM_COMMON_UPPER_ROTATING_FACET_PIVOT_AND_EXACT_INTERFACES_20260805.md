# The common-upper rotating-facet pivot: exact local closure and exact global interfaces

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local pivot theorem, exact lower-compiler closure,
and two sharp interface obstructions (endpoint stutter and upper cap two)

## 0. Verdict

Fix integers `h>=2` and `r>h`.  Let

\[
 |X|=r-h,
 \qquad C=\{c_0,c_1,\ldots,c_h\},
 \qquad X\cap C=\varnothing,
 \qquad R=X\mathbin{\dot\cup}C.                       \tag{0.1}
\]

Thus `|R|=r+1`.  On source positions

\[
              -h,\ldots,-1,0,1,\ldots,h
\]

put

\[
 \begin{aligned}
 A_{-i}&=X\cup\{c_{h-i+1}\} &&(1\le i\le h),\\
 A_0&=X,\\
 A_i&=X\cup\{c_{i-1}\} &&(1\le i\le h).
 \end{aligned}                                         \tag{0.2}
\]

The insertion at `0` is a valid monotone pivot.  Its `h+1` new owner
windows are exactly

\[
                         M_j=R\setminus\{c_j\},
                    \qquad0\le j\le h.                \tag{0.3}
\]

They form a simple rank-`r` Johnson path.  Every old interval OR survives,
the only new strict-lower band cells are the singleton `X` and two complete
nested rays, and the `h-1` old cells which leave the compiler band have
values `M_1,...,M_(h-1)` of rank `r`.  Consequently the existing flat
monotone-pivot theorem gives zero residual lower-compiler deficiency under
its occurrence-release and one-common-cap hypotheses.

This is a genuine positive local construction.  It also has two exact
limitations.

1. All `h` central Johnson edges have the **same** upper-q1 colour `R`.
   For `h>=3` the block is not cap two.  In an even Catalan owner path it
   spends `h-1` units of the total `Cat_r-1` upper-repeat budget, and a bank
   of `Cat_r-1` such pivots is count-impossible.
2. The `h` fixed old letters on either side already unite to the endpoint
   owner.  Hence every flat rank-`r` source extension has an unavoidable
   repeated owner immediately before `M_0` and immediately after `M_h`.
   An internal occurrence therefore costs at least two exceptional depth
   cells.  At physical length `B+1` it can only be used at a linear endpoint
   (or after a genuinely spectrum-changing rethread which removes one of
   these stutters).

The construction is thus **not** a replacement for the balanced
`Cat_r-1` collar bank or for a cap-two Catalan block.  It remains potentially
useful as one endpoint pivot: its local lower compiler is exact, one of the
two forced stutters disappears at a word endpoint, and its `h-1` upper
repeat excess is negligible relative to the Catalan budget.

## 1. Exact owner windows

For `0<=j<=h`, define the length-`(h+1)` interval through the pivot

\[
 J_j=\{-(h-j),\ldots,-1,0,1,\ldots,j\}.              \tag{1.1}
\]

It contains `h-j` old letters on the left, the pivot, and `j` old letters
on the right.  The left active labels in its union are

\[
                         c_{j+1},\ldots,c_h,
\]

and the right active labels are

\[
                         c_0,\ldots,c_{j-1}.
\]

Every letter contains `X`.  Therefore

\[
 \bigcup_{p\in J_j}A_p
 =X\cup\{c_0,\ldots,c_{j-1},c_{j+1},\ldots,c_h\}
 =R\setminus\{c_j\}=M_j.                              \tag{1.2}
\]

In particular every owner has rank `r`, and

\[
                   M_{j+1}=M_j-\{c_{j+1}\}+\{c_j\}.
                                                               \tag{1.3}
\]

The missing active label recovers `j`, so all owners are distinct.  This
proves the owner assertion.

The two immediate palettes are

\[
 \boxed{
   M_j\cap M_{j+1}=R\setminus\{c_j,c_{j+1}\},
   \qquad
   M_j\cup M_{j+1}=R. }
                                                               \tag{1.4}
\]

The lower colours are pairwise distinct.  The upper colour is repeated on
all `h` transitions.

The path is not a Johnson geodesic when `h>=2`: its endpoints `M_0,M_h`
are adjacent, and hence have Johnson distance one.  This is exactly the
overlapping-bank equality case omitted by the false rigidity sentence in
the original sharp-aperture proposal.

## 2. All-width monotone transparency

Delete the pivot position `0` and call the resulting `2h`-letter line the
old word.  Every old letter contains `X`.  Transport an old interval by an
index shift if it is one-sided and by taking its convex hull if it crosses
the cut.

### Theorem 2.1 (literal all-width transparency)

Every old interval keeps its exact OR under this transport.

#### Proof

A one-sided interval is copied literally.  A crossing interval gains only
the inserted position, whose value is `X`.  Its old union already contains
`X` (indeed every one of its old letters does), so its union is unchanged.
`square`

Thus

\[
                       \operatorname {Deck}(A^-)
             \subseteq\operatorname {Deck}(A^+),       \tag{2.1}
\]

with an explicit witness injection.  Exact width is not preserved for
crossing witnesses: their source length increases by one.

## 3. Exact band exchange and the two rays

For `1<=j<h`, put

\[
 I_j=\{-(h-j),\ldots,-1,1,\ldots,j\}.                \tag{3.1}
\]

These are precisely the old crossing cells of source length `h`.  Directly,

\[
                         \bigcup_{p\in I_j}A_p=M_j.    \tag{3.2}
\]

Their convex hulls have length `h+1`, so they are precisely the old cells
which leave the depth-`h` compiler band.  All have rank `r`.

The genuinely new band cells are

\[
 \begin{aligned}
 X,\qquad
 P_t&=X\cup\{c_{h-t+1},\ldots,c_h\},\\
 S_t&=X\cup\{c_0,\ldots,c_{t-1}\},
                 &&1\le t<h.                         \tag{3.3}
 \end{aligned}

They are the singleton pivot, the left suffix ray, and the right prefix
ray.  Their ranks are

\[
                         |X|=r-h,
 \qquad                 |P_t|=|S_t|=r-h+t<r.          \tag{3.4}
\]

Both nontrivial families are strict nested chains.  They are mutually
disjoint as value families: every `P_t` contains `c_h`, whereas no `S_t`
does.  Thus all `2h-1` cells in (3.3) have distinct values.

This is exactly the general monotone-pivot ledger:

\[
                 h-1\text{ escaped cells},
 \qquad          2h-1\text{ new cells},
 \qquad          \text{net gain }h.                  \tag{3.5}
\]

### Theorem 3.1 (zero residual lower compiler, conditional only on the
standard ambient rows)

Let `mathcal M_0` be a reference matching of the old strict-lower target
shore into source intervals of length at most `h`.  Assume:

1. the singleton task `X` is a new occurrence-labelled target, not already
   saturated by `mathcal M_0`;
2. each target `P_t,S_t` is released from its old matching edge and assigned
   to the correspondingly addressed new ray cell;
3. every other matching edge is transported by the monotone interval map;
4. the displayed word and all exterior owner, cap, pin and guard rows are
   feasible in one simultaneous common-`Q` state.

Then the new strict-lower target shore has a complete matching and its
residual deficiency is zero.

#### Proof

The only old band cells not transported are the `I_j`, whose values have
rank `r` by (3.2).  A strict-lower matching uses none of them.  Hence every
unreleased edge of `mathcal M_0` transports injectively with the same value.
The transport image is disjoint from the complete new-cell family (3.3).
After the stated occurrence-labelled releases, place `X,P_t,S_t` on those
new cells.  Their values and cells are pairwise distinct, so the union is a
matching.  The one-common-`Q` hypothesis makes this literal assignment, the
owner rows, and every exterior row simultaneous rather than merely
marginal. `square`

If `X` was already a target vertex of the old matching, its new singleton
cell is only a redundant occurrence; it cannot be counted as a second new
target.  This is the same target-identity qualification as in the audited
sharp-pivot theorem.

## 4. The exact local cap interval

The owner equalities alone give a transparent componentwise cap description.
Intersect the owner values of all windows containing one source position.
The resulting maximal allowed letters are

\[
 \begin{aligned}
 K_0&=X,\\
 K_{-i}&=X\cup\{c_{h-i+1},\ldots,c_h\},\\
 K_i&=X\cup\{c_0,\ldots,c_{i-1}\},
                    &&1\le i\le h.                   \tag{4.1}
 \end{aligned}

The literal letters (0.2) satisfy

\[
                         X\subseteq A_p\subseteq K_p. \tag{4.2}
\]

The componentwise maximal word `K` still realizes every owner `M_j` and
every ray value in (3.3).  Thus local cap feasibility is exact and does not
require the source letters to remain singleton active extensions.  Exterior
rows can only shrink the caps (4.1), and must be included in the same
maximal-word test.

This cap statement does not cure either obstruction below: those depend on
the owner values and on the fixed old source union, both unchanged by
maximalization.

## 5. Exact residence interface

In the central owner trace `M_0,...,M_h`, every member of `X` has one run of
length `h+1`.  For an active label `c_i`, the unique absent owner is `M_i`.
Its positive runs are therefore

\[
 \begin{array}{c|cc}
 &\text{left run}&\text{right run}\\ \hline
 c_i&i&h-i.
 \end{array}                                           \tag{5.1}

Empty runs at `i=0,h` are ignored.  Consequently an internal occurrence
with positive residence floor `h+1` needs exactly

\[
 \begin{aligned}
 &h+1-i\text{ consecutive containing owners immediately on the left}
                    &&(1\le i\le h),\\
 &i+1\text{ consecutive containing owners immediately on the right}
                    &&(0\le i<h).                     \tag{5.2}
 \end{aligned}

These requirements are nested triangular halos.  They are also sufficient
for the displayed active-label runs.  They do not certify the residence of
halo filler labels or prevent another short run elsewhere in the ambient
trace.

For example, at the abstract owner level one may choose `x in X`, fresh
`q^-,q^+`, and fresh filler banks `d^-_1,...,d^-_(h-1)` and
`d^+_1,...,d^+_(h-1)`.  Put

\[
 X^-=(X-x)+q^-,\qquad X^+=(X-x)+q^+                  \tag{5.3}
\]

and, with `a=1` nearest the pivot,

\[
 \begin{aligned}
 L_a&=X^-\cup\{c_1,\ldots,c_{h+1-a}\}
              \cup\{d^-_1,\ldots,d^-_{a-1}\},\\
 R_a&=X^+\cup\{c_{a-1},\ldots,c_{h-1}\}
              \cup\{d^+_1,\ldots,d^+_{a-1}\}.
                                                        \tag{5.4}
 \end{aligned}

Then

\[
 L_h,\ldots,L_1,M_0,\ldots,M_h,R_1,\ldots,R_h        \tag{5.5}
\]

is an abstract simple rank-`r` Johnson path, and every `c_i`-run in (5.1)
is extended to length exactly `h+1`.  This uses only

\[
                         r+2h+1                       \tag{5.6}
\]

distinct coordinate labels.  The `q` and filler runs touch the exterior
boundaries and remain clipped.

However, (5.5) is only an owner-level halo.  It is **not** a literal
extension of the fixed source block (0.2).  The next theorem is the exact
reason.

If the architecture requires bi-residence (both one-runs and zero-runs of
length at least `h+1`), the pivot is impossible even abstractly: every
`c_i` has the one-owner zero gap `M_i`.  The construction is compatible only
with the ordinary positive-run residence condition, plus the halo/clipping
interface just stated.

## 6. Forced endpoint stutters in every literal flat extension

The union of all `h` old source letters on the left is

\[
             \bigcup_{i=1}^h A_{-i}
                    =X\cup\{c_1,\ldots,c_h\}=M_0,     \tag{6.1}
\]

and symmetrically

\[
             \bigcup_{i=1}^h A_i
                    =X\cup\{c_0,\ldots,c_{h-1}\}=M_h.\tag{6.2}
\]

### Theorem 6.1 (two-sided literal stutter obstruction)

Adjoin any source letter immediately before the displayed block.  The
length-`(h+1)` window immediately preceding `J_0` has union containing
`M_0`.  If it is required to have rank `r`, its union is exactly `M_0` and
therefore repeats the first pivot owner.  If its rank is not `r`, it is a
nonowner depth cell.  The symmetric assertion holds immediately after
`J_h`, with `M_h`.

Thus an internal literal embedding has at least two exceptional depth cells
relative to a simple flat rank-`r` owner chronology.

#### Proof

The predecessor window contains all `h` letters in (6.1), plus one exterior
letter.  Its union therefore contains the rank-`r` set `M_0`.  A rank-`r`
superset of `M_0` equals `M_0`; otherwise the window has rank above `r`.
The proof on the right is identical using (6.2). `square`

### Corollary 6.2 (exact physical-length interface)

At length `B=W+h`, there are exactly `W` depth-`(h+1)` windows, so every one
must be a distinct owner.  At length `B+1`, there are `W+1` such windows, so
at most one can be a repeat/nonowner if all `W` owners are to occur.
Theorem 6.1 therefore excludes an internal use of this fixed source block
at `B+1`.

Placing the block at one global endpoint removes one of the two adjacent
windows.  The remaining forced stutter can then be the unique `+1` depth
cell.  Alternatively, a nonlocal rethread must change one endpoint source
state; an abstract owner halo such as (5.5) is not enough.

This is the same strict-stutter interface already isolated for the sharp
pivot.  The common-upper specialization does not remove it.

## 7. Exact Catalan cap-compression interface

The central owner path has `h` edges, all coloured by `R`.  Smoothing it to
the single Johnson edge

\[
                            M_0M_h                       \tag{7.1}
\]

is set-theoretically legal because `M_0` and `M_h` are distinct facets of
`R`.  It deletes the internal owners

\[
                          M_1,\ldots,M_{h-1}             \tag{7.2}
\]

and replaces the `h` lower colours in (1.4) by the single lower colour

\[
                          R\setminus\{c_0,c_h\}.         \tag{7.3}
\]

Thus this is an exact `h-to-1` upper block compression, but it is not free:
the `h-1` owners and their lower occurrences in (7.2) must be rehomed.

The integrality-floor Catalan theorem allows only singleton and two-edge
upper blocks.  Therefore:

### Theorem 7.1 (cap-two incompatibility)

For `h>=3`, the common-upper pivot is not a cap-two block and cannot occur
inside the cap-two Catalan cycle without changing that theorem's load
profile.

More generally, in the even middle layer put

\[
 W={2r\choose r},\qquad U={2r\choose r+1},
 \qquad C=W-U=\operatorname {Cat}_r.                  \tag{7.4}
\]

An upper-complete Hamilton owner **path** has `W-1` transitions and total
upper-q1 multiplicity excess exactly

\[
                             W-1-U=C-1.                \tag{7.5}
\]

Hence `H` disjoint common-upper pivot blocks force

\[
                             H(h-1)\le C-1.            \tag{7.6}
\]

In particular a bank of `C-1` such blocks is impossible for every `h>=3`.

#### Proof

One block uses `h` occurrences of one represented upper target, contributing
`h-1` multiplicity excess.  These excesses add over distinct physical
blocks, even if two blocks use the same target (which only increases the
excess).  Equation (7.5) is the difference between the total transition
count and the number of required upper colours. `square`

The balanced collar theorem needs each `h`-edge stem, together with its
seams, to deliver `h+1` distinct upper targets and only one repeat.  The
common-upper stem delivers one distinct target and `h-1` repeats before its
seams are counted.  It therefore cannot replace a balanced collar in the
`C-1`-component depuncturing construction.

For one fixed pivot, (7.6) has enormous slack because `h=Theta(sqrt r)` and
`C` is exponential.  A non-cap-two endpoint architecture may therefore use
the block, but it must explicitly rehome the compressed owners (7.2) and
pay/absorb the one forced endpoint stutter from Corollary 6.2.

## 8. Relation to the audited sharp pivot

At the owner level, set

\[
 Q=X,\qquad \lambda_i=c_i,qquad \rho_i=c_{i-1}
                     \quad(1\le i\le h).              \tag{8.1}
\]

Then the general sharp-aperture formula becomes exactly (0.3).  The two
moving banks overlap in

\[
                  \{c_1,\ldots,c_{h-1}\}.             \tag{8.2}
\]

The independent sharp-pivot audit proved that an equality-case owner path
is geodesic exactly when the deletion and insertion banks are disjoint.
Thus the common-upper construction is not a new equality normal form; it is
the maximally overlapping rotating-facet specialization.  Adding `X` to
all of the otherwise singleton old source letters leaves the owner and ray
unions unchanged, while making the local cap interval (4.1) particularly
transparent.

Compared with the disjoint-bank sharp pivot, it uses fewer coordinate labels
and has the same exact lower compiler.  The price is precisely what the
disjointness bought there: geodesicity, distinct upper-q1 colours, and
one-sided active-label residence.  The two constructions are therefore
consistent, not contradictory.

## 9. Proof-safe conclusion

Unconditionally closed here:

* exact owner windows `M_j=R-c_j`;
* simple Johnson adjacency and exact q1 ledgers;
* literal preservation of the complete old OR deck;
* exact escaped-cell/singleton/two-ray band ledger;
* zero residual lower compilation under the standard occurrence and
  one-common-cap hypotheses;
* exact local componentwise cap intervals;
* exact positive-residence halo demand;
* the two forced literal endpoint stutters; and
* the exact upper-repeat/cap-compression budget.

The fatal conclusion for the current Catalan collar programme is:

\[
 \boxed{
   \text{the common-upper pivot cannot be the }C-1\text{ protected stem
   bank, and it cannot be embedded internally at }B+1.}
                                                               \tag{9.1}
\]

The surviving use is narrower but concrete: one endpoint pivot in a
non-cap-two construction, with the remaining stutter as the unique `+1`
cell and with an explicit owner-rehoming mechanism for any later smoothing.
