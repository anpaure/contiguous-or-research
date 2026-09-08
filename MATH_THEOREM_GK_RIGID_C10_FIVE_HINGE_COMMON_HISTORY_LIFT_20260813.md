# The rigid GK `C10` is one five-hinge common-history source rethread

**Date:** 2026-08-13  
**Status:** unconditional prospective local/source theorem for `m>=5`; the
protected owner-level q2 conclusion additionally uses `m>=6` and the
audited unchanged PBBS companion edges.  The theorem bypasses
the shared-chord regeneration obstruction of the serial two-`C6` lift.  It
does not plant a global PBBS transversal or prove a common-cap routing.

## 1. Statement

Let `n=2m+1`, and use the ten rank-`m+1` owners `A_i,B_i`, `i in Z_5`,
from
`MATH_THEOREM_GK_RIGID_PALETTE_NEUTRAL_C10_FUSION_20260813.md`.
The old and new hinges are

\[
                  e_i=A_iB_i,
       \qquad     n_i=B_iA_{i-1}.                    \tag{1.1}
\]

Put

\[
                  H=\{m,m+1,\ldots,2m-3\}.          \tag{1.2}
\]

Then `|H|=m-2`, and `H` is contained in every one of the ten owners.
Fix `1<=d<=m-2`, and partition

\[
                  H=C_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}C_d           \tag{1.3}
\]

into nonempty source letters.  Define the three-element screens

\[
                  X_i=A_i\setminus H,
       \qquad     Y_i=B_i\setminus H,                \tag{1.4}
\]

and the five old source fragments

\[
                  W_i=(X_i,C_1,\ldots,C_d,Y_i).       \tag{1.5}
\]

Replace them simultaneously by

\[
                  \widehat W_i
                  =(X_i,C_1,\ldots,C_d,Y_{i+1}).     \tag{1.6}
\]

In an ambient cyclic source carrier, cut immediately before the five tagged
occurrences `Y_i`.  Move the complete residual path beginning at `Y_i` to
the role receiving `Y_i`, as in the cyclic common-history hinge theorem.
This path formulation is also the meaning of arbitrary exterior contexts
below; it remains valid when two displayed hinges lie on the same carrier
component.

### Theorem 1.1 (compound resident decagon converter)

The rethread `(1.5)->(1.6)` has the following properties.

1. Its distinguished owner hinges are exactly the old five edges `e_i`
   and the new five edges `n_i`; there is no intermediate chord occurrence.
2. It preserves the owner multiset and the complete immediate-lower and
   immediate-upper colour multisets.
3. It gives an occurrence-, width-, and value-preserving bijection on every
   interval OR of rank strictly below `m+1`.  Hence every literal source
   derivative row represented by such intervals (q3 and deeper in the
   present selected-PBBS bookkeeping), and every cell-based strict-lower
   compiler assignment, transports exactly.  The selected owner-level q2
   row is the separate assertion in item 6.
4. The complete internal interval deck of the five displayed fragments is
   preserved at every width.
5. On a cyclic source carrier, every nonconstant positive owner run created
   by the packet has length at least `d+1`; the move has zero source-length
   charge.
6. When planted in the odd GK/PBBS owner factor with the five unchanged
   companion edges used in the q2 audit, the move replaces the four
   affected components by two.  For `m>=6`, it also has the independently
   audited zero q2 current of the owner-level `C10`.

Thus the two clean `C6` phases need not be serially resident-lifted.  Their
net `C10` is a single five-hinge common-history move.

## 2. Owner and palette identities

Since every owner in the displayed `C10` has rank `m+1`, `(1.2)--(1.4)`
give

\[
                  A_i=H\cup X_i,
       \qquad     B_i=H\cup Y_i.                    \tag{2.1}
\]

The two length-`d+1` windows wholly contained in `W_i` therefore have
values `A_i,B_i`.  In `\widehat W_i` they have values `A_i,B_(i+1)`.
The latter hinge is `n_(i+1)`, so all five new hinges in `(1.1)` occur
once.

The already proved Boolean identities for the rigid decagon are

\[
 B_j\cap A_{j-1}=A_{j-1}\cap B_{j-1},
 \qquad
 B_j\cup A_{j-1}=A_j\cup B_j.                     \tag{2.2}
\]

With `j=i+1`, these say that the lower colour on `A_iB_(i+1)` is the
old colour on `A_iB_i`, while its upper colour is the old colour on
`A_(i+1)B_(i+1)`.  Hence lower colours are fixed rolewise and upper
colours are cyclically permuted.  This proves items 1--2.

## 3. Exact lower occurrence transport

Cut the affected cyclic source carrier immediately before every displayed
`Y_i`.  The cuts give five disjoint tagged residual paths, including two
paths from the one old component cut twice.  Each path begins with one
`Y_i`; the rethread permutes these complete paths.  Equivalently, each
changed seam has the local form

\[
          P_iX_iC_1\cdots C_d\mid Y_jQ_j,           \tag{3.1}
\]

and the complete path `Y_jQ_j` is moved with its head.

An interval which crosses a changed seam and extends left far enough to
meet `X_i` contains all the history letters `C_1,...,C_d`.  Its value
therefore contains

\[
                  H\cup X_i=A_i,                    \tag{3.2}
\]

which already has owner rank `m+1`.  Consequently, a strict-lower interval
crossing a changed seam uses only a suffix of the common history followed
by a prefix of `Y_jQ_j`.  Map it to the old seam preceding that same path:
the suffix of the common history is literal and `Y_jQ_j` is the same tagged
path, so width and OR value are unchanged.  A strict-lower interval cannot
cross two changed seams, because between two successive cuts it traverses
a complete terminal `X_hC_1\cdots C_d` and hence contains the owner `A_h`.

Intervals not crossing a cut remain at their literal positions inside a
residual path.  The seam map and the path-internal identity map are inverted
by the reverse rethread, and therefore form an occurrence bijection.  This
proves item 3 even for arbitrary compatible contexts and for the old
component containing two protected hinges.

In a depth-`d` antecedent, the literal lower source-derivative cells are
such source intervals.  Transporting the chosen occurrence of each
cell-based compiler target through the bijection preserves its value and
distinctness.  External phase, socket, cap, or route tickets are not
asserted to be functions of this bijection.

## 4. Complete internal deck and residence

Inside a displayed fragment, widths at most `d` cannot meet both screens,
so the argument of Section 3 gives exact deck invariance.  Width `d+1` is
the owner row, already handled in Section 2.  At width `d+2`, each old
fragment has the single value

\[
                  A_i\cup B_i,
\]

whereas the corresponding new fragment has value

\[
                  A_i\cup B_{i+1}=A_{i+1}\cup B_{i+1}.
                                                               \tag{4.1}
\]

Thus the full-fragment values are cyclically permuted as well.  These are
all possible internal widths, proving item 4.

On a cyclic source word, each occurrence of a source coordinate belongs to
`d+1` consecutive owner windows.  It therefore creates a positive trace run
of length `d+1`; overlaps between occurrences can only merge positive runs.
The rethread merely permutes complete source screen/context blocks, so it
adds and removes no source positions.  This proves item 5.  No minimum
zero-gap assertion is made here.

## 5. Topology, q2, and exact scope

At owner level `(1.6)` is exactly the audited rigid `C10`.  Its exposed-port
return permutation turns the four affected old components into two.  If
the prospective source packet is planted while retaining the unchanged
PBBS companion edge at every affected owner, then for `m>=6` the independent
q2 audit shows zero q2 multiset current for the net move.  The source lift
changes neither calculation because it realizes the net move directly
rather than passing through the cancelling chord.  This proves item 6 at
its stated conditional planting scope.

The theorem supplies a prospective protected packet, not a claim that the
unchanged canonical PBBS chronology already contains `(1.5)`.  It also
protects every internal upper occurrence but does not automatically protect
an old exterior fan interval crossing a screen.  The remaining global task
is therefore to plant a collision-free family of these direct five-hinge
packets (and other needed packets) on a transversal of short PBBS runs,
while assigning fresh internal witnesses to the upper colours whose old
collars must be cut.
