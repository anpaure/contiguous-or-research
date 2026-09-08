# The shortest rotating-hole rail collapses the internal cut triangle but exports six exterior ladders

Date: 2026-08-01  
Lane: K, fixed-defect regenerative collars  
Status: exact local theorem and sharp scope boundary.  The shortest rail has
zero internal upper-target loss when its return edge is opened.  For widths
at most the residence depth its exterior interface is six nested ladders.
This gives a constant number of *ladder certificates*, not a constant number
of ordinary target occurrences.  Arbitrary longer windows additionally see
a two-sided `Z`-grid.  No Pascal host theorem or `B(k)+O(1)` conclusion is
claimed.

## 1. Setup

Fix `d>=2` and use the shortest rotating-hole rail of
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`
at residence depth `h=d`.  Thus

\[
 Z=L\cup\{a,d_0,y\},\qquad
 V_i=Z\setminus\{z_i,z_{i+1}\},
\]

where cyclically

\[
 (z_0,z_1,z_2,z_3,\ldots,z_{d+2})
   =(a,y,d_0,x_0,\ldots,x_{d-1}).
\]

Write

\[
 E=V_0,qquad F=V_1,qquad
 R=(V_1,V_2,\ldots,V_{d+2},V_0).
\tag{1.1}
\]

The linear rail has `d+3` vertices.  The old packet uses the return edge
`EF`, while the plus packet opens that edge and retains the linear rail.
Put

\[
 U=E\cup F=Z\setminus\{y\}.
\tag{1.2}
\]

The packet vertex `A=U-b` satisfies

\[
 A\cup F=U.
\tag{1.3}
\]

For a word of middle owners, a depth-`q` upper cell means the union of
`q+1` consecutive owners.

## 2. The internal triangular collateral is exactly zero

### Theorem 2.1 (cut-triangle collapse)

Open the old rail cycle at `EF`.  Then every upper target supplied by an
old cyclic interval is still supplied by the plus packet and the opened
rail.

More precisely:

1. at depth one the deleted edge has upper colour `U`, and the plus edge
   `AF` has the same upper colour;
2. for every `2<=q<=d`, the `q` old cyclic `(q+1)`-windows crossing `EF`
   all have union `Z`; and
3. after opening, the linear rail has exactly

   \[
                         d+3-q
   \tag{2.1}
   \]

   internal `(q+1)`-windows, every one of union `Z`.  In particular there
   are at least three such surviving witnesses.

Thus the occurrence triangle has size `d(d+1)/2`, but its target loss is
zero.  This is the point at which the shortest rail differs from the
strict long wreath rail, whose cut windows were pairwise distinct.

#### Proof

Three consecutive cyclic rail vertices have missing-pair intersection

\[
 \{z_i,z_{i+1}\}\cap\{z_{i+1},z_{i+2}\}
 \cap\{z_{i+2},z_{i+3}\}=\varnothing.
\]

Their union is therefore `Z`; every longer cyclic interval also has union
`Z`.  A cyclic `(q+1)`-window crosses one specified edge in exactly `q`
ways.  This proves item 2.  A linear word of length `d+3` has
`d+3-(q+1)+1=d+3-q` windows of length `q+1`, and the same three-window
argument proves item 3.  Finally (1.2)--(1.3) prove item 1.  \(\square\)

The theorem concerns upper-target support.  It does not alter the
one-cell-star fan/crossing equations for a source antecedent.  In
particular it does not, by itself, repair the lower common-cap triangular
obstruction in
`MATH_THEOREM_K_ONE_CELL_TYPED_STAR_TRIANGULAR_COLLAR_GATE_20260801.md`.

### Proposition 2.2 (a generic Pascal cut still loses its whole triangle)

Theorem 2.1 is special to opening the rail's own return edge `EF`.  It does
not say that inserting `R` at an arbitrary Pascal-child cut preserves that
cut's old windows.

Indeed, let an old child word have a cut `X|Y`, and let `S_i` and `P_j` be
the unions of the nearest `i` owners on the left and the nearest `j`
owners on the right.  Its depth-`q` crossing occurrences are exactly

\[
             C_{q,i}=S_i\cup P_{q+1-i},
             \qquad 1\le i\le q.                       \tag{2.2}
\]

Insert the `d+3`-vertex rail between the two sides.  For `q<=d`, no new
`(q+1)`-window reaches both old sides.  Hence all `q` occurrences in (2.2)
are destroyed, for a total of

\[
                         \sum_{q=1}^{d}q={d(d+1)\over2} \tag{2.3}
\]

destroyed occurrences.  A target among them is repaid exactly when it has
an unaffected old witness or occurs in the new local spectrum: the six
boundary ladders of Theorem 3.1, the internal value `Z` at `q>=2`, and the
immediate packet/rail palette at `q=1`.

Equivalently, if `W_0(T)` is the old witness set, `C` is the occurrence
triangle (2.2), and `N` is the new local spectrum, the exact hole set is

\[
 \mathcal H_{\le d}
   =\{T:W_0(T)\ne\varnothing, W_0(T)\subseteq C, T\notin N\}. \tag{2.4}
\]

Thus the shortest rail collapses the triangle only on a **prepared
saturated cut**.  Its own `EF` cut is such a cut because its depth-one
target is `U` and every deeper target is `Z`; Theorem 2.1 supplies both.
For a generic Pascal cut the sets in (2.2) may all be distinct, and the
full triangular return debt remains possible.

#### Proof

A contiguous window meeting both old sides after insertion must traverse
the entire rail.  Its length is at least `d+3` even when the rail endpoints
are identified with the two old boundary owners (and is `d+5` when both
exterior owners remain separate).  A protected window has length at most
`d+1`.  Therefore none of (2.2) transports.
Formula (2.4) is the last-witness criterion, and Theorem 2.1 proves the
special `EF` assertion.  \(\square\)

## 3. Exact short-window exterior ledger

Attach `R` between a left exterior owner word and a right exterior owner
word.  Let

\[
 S_j=\text{union of the last }j\text{ left exterior owners},\qquad
 P_j=\text{union of the first }j\text{ right exterior owners}.
\tag{3.1}
\]

The rail prefix unions are

\[
 p_1=F,\qquad p_2=Z\setminus\{d_0\},\qquad p_t=Z\quad(t\ge3),
\tag{3.2}
\]

and its suffix unions are

\[
 r_1=E,\qquad r_2=Z\setminus\{a\},\qquad r_t=Z\quad(t\ge3).
\tag{3.3}
\]

### Theorem 3.1 (six-ladder boundary normal form)

For all protected depths `1<=q<=d`, no `(q+1)`-window meets both exterior
boundaries of `R`.  The complete left-crossing target set, over all such
depths, is contained in the three nested ladders

\[
\begin{aligned}
 \mathcal L_1&=\{S_j\cup F:1\le j\le d\},\\
 \mathcal L_2&=\{S_j\cup(Z\setminus\{d_0\}):1\le j\le d-1\},\\
 \mathcal L_3&=\{S_j\cup Z:1\le j\le d-2\}.
\end{aligned}
\tag{3.4}
\]

The complete right-crossing target set is contained in

\[
\begin{aligned}
 \mathcal R_1&=\{E\cup P_j:1\le j\le d\},\\
 \mathcal R_2&=\{(Z\setminus\{a\})\cup P_j:1\le j\le d-1\},\\
 \mathcal R_3&=\{Z\cup P_j:1\le j\le d-2\}.
\end{aligned}
\tag{3.5}
\]

At a fixed depth `q`, the `q` left-crossing windows consist exactly of

\[
 S_q\cup F,qquad
 S_{q-1}\cup(Z\setminus\{d_0\})\ (q\ge2),\qquad
 S_j\cup Z\ (1\le j\le q-2),
\tag{3.6}
\]

and the reflected formula holds on the right.

Consequently a fixed bank of `H` rails has upper interface arity at most
`6H` in the following exact sense: one complete last-witness ladder
certificate for each family in (3.4)--(3.5) certifies every exterior
window of depth at most `d`.

#### Proof

The rail has `d+3` vertices, whereas a protected window has at most `d+1`,
so it cannot cross both rail boundaries.  A left-crossing `(q+1)`-window
uses `j>=1` exterior owners and `t>=1` rail owners with `j+t=q+1`.
Substitute (3.2).  The cases `t=1`, `t=2`, and `t>=3` give (3.6).
Taking the union over `q<=d` gives (3.4).  Reversal gives (3.5).
Nestedness follows from `S_j subseteq S_(j+1)` and
`P_j subseteq P_(j+1)`.  The last-witness assertion is then just the exact
cut criterion: every changed short exterior interval belongs to one of the
six displayed families, while Theorem 2.1 handles every internal one.
\(\square\)

A **complete ladder certificate** means that every target in the ladder
which would otherwise lose its last witness has a jointly valid surviving
or recreated occurrence.  It is not one occurrence at the top of the
ladder.

## 4. Constant ordinary tickets are false

### Proposition 4.1 (linear physical-ticket lower bound)

The three-state prefix theorem alone does not imply that `O(1)` ordinary
target occurrences repair one rail uniformly in `d`.  Even the first
ladder in (3.4) may contain `d` distinct rank-correct targets along a
q1-rainbow Johnson exterior path.

#### Proof

Choose an `(m-2)`-set `C` and distinct coordinates
`e_0,e_1,\ldots,e_(d+1)` outside `C`.  Put

\[
 X_i=C\cup\{e_i,e_{i+1}\}\qquad(0\le i\le d),
\tag{4.1}
\]

and identify `F=X_0`.  Attach the exterior path in the order

\[
 X_d,X_{d-1},\ldots,X_1,F.
\]

Consecutive owners are Johnson adjacent and their lower colours are the
distinct sets `C+e_i`.  The last-`j` exterior union before `F` is

\[
 S_j=C\cup\{e_1,e_2,\ldots,e_{j+1}\},
\]

so

\[
 S_j\cup F=C\cup\{e_0,e_1,\ldots,e_{j+1}\}
\tag{4.2}
\]

has rank `m+j` and is strictly increasing for `1<=j<=d`.  These are `d`
different upper targets at their correct depths.  If they are last
witnesses at the attachment, each needs its own physical replacement.
Nothing in the rotating-hole rail theorem supplies those replacements.
\(\square\)

The example is a local Johnson/q1-rainbow obstruction to an automatic
inference.  A specially constructed Pascal child may of course provide a
second witness for every member of (4.2); that is precisely the complete
ladder-ticket hypothesis.

## 5. Long windows and the two-sided `Z`-grid

The six-ladder theorem is exact for widths `q<=d`.  For arbitrary widths,
an interval may contain the whole rail and exterior owners on both sides.
Its value is exactly

\[
                         S_j\cup Z\cup P_k.
\tag{5.1}
\]

Thus the full upper interface consists of:

1. the internal rail deck;
2. the six one-sided ladders (3.4)--(3.5); and
3. the two-sided grid (5.1).

The grid may have quadratically many distinct proper masks when the left
and right exterior paths introduce disjoint coordinates.  Hence six ray
certificates do not imply arbitrary-width transparency.  A uniform
all-width attachment theorem must additionally provide one of the
following exact rows:

* a complete last-witness certificate for the entire `Z`-grid;
* a full-OR separator making every relevant member of (5.1) equal to the
  already harmless top target; or
* a dominance theorem showing every proper member of (5.1) has an
  unaffected witness elsewhere.

This is not a scalar count.  It is the exact remaining exterior upper row.

## 6. Consequence for a fixed regenerative bank

For fixed `H`, **when each rail is carried through its prepared saturated
`EF` actuator rather than inserted at an unrelated child cut**, the shortest
rail has the following proved upper-state ledger.

* Internal cut collateral: zero targets.
* Immediate palette collateral: zero, by the ternary packet identity.
* Short exterior interface: at most `6H` complete ladder certificates.
* Arbitrary-width exterior interface: additionally `H` two-sided
  `Z`-grid certificates (or `H` full-OR/dominance replacements).

This does bypass the *upper-target* triangle of the older long rail.  It
does not prove bounded ordinary ticket count, does not solve the
one-cell-star lower/common-cap triangle, and does not show that a Pascal
child exports the six ladders or the `Z`-grid certificates.  The weakest
remaining host hypothesis is exactly their occurrence-level last-witness
realization together with terminal residence and common-cap replay.
At an unrelated Pascal cut, Proposition 2.2 adds the old
`d(d+1)/2`-occurrence triangle to this ledger; there is then no bounded
interface theorem without an independent cut-saturation/return hypothesis.
