# The open Johnson square is an exact three-return role converter, not a protected two-root circuit

**Date:** 2026-08-01  
**Status:** exact resource and projection audit, exact common-residual
obstruction, and a conditional composition theorem.  No normalized
depth-three lift, resident chronology, or compiler closure is constructed.

**Subsequent rebase.**  The last sentence is a statement about the bare
three-edge square phases only.  The frozen theorem
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`
replaces that detour by the long rail (R_d) and reverses the **entire**
reset-plus-return cycle.  That (4d+2)-root packet is resident, internally
all-depth transparent, and a literal closed three-return lift.  Its exact
functional/global-host interface is recorded in
`MATH_COROLLARY_A_COMPLETE_REVERSAL_PACKET_FUNCTIONAL_CUT_AND_PROTECTED_HOST_INTERFACE_20260801.md`.
The computations below remain the sharp audit of the minimal bare square;
they are not an obstruction to the strengthened packet.

## 0. Verdict

Let

\[
\begin{aligned}
V_0&=K+x+z,&V_1&=K+x+y,\\
V_2&=K+y+w,&V_3&=K+z+w,
\end{aligned}                                               \tag{0.1}
\]

where \(K\) has rank two below the \(V_i\) and \(x,y,z,w\) are pairwise
distinct elements outside \(K\).
Delete \(V_0\to V_1\) from the forward Johnson four-cycle and
\(V_1\to V_0\) from the reverse four-cycle.  The remaining phases are

\[
\begin{aligned}
{\cal Q}^{\to}
 &=\{V_1\to V_2,\ V_2\to V_3,\ V_3\to V_0\},\\
{\cal Q}^{\leftarrow}
 &=\{V_0\to V_3,\ V_3\to V_2,\ V_2\to V_1\}.
\end{aligned}                                               \tag{0.2}
\]

The audit gives four exact conclusions.

1. The two phases have identical lower and upper/owner palettes: the three
   surviving undirected Johnson edges are the same.
2. Their head--owner symmetric difference is one alternating path from
   \(V_0^+\) to \(V_1^+\).
3. Their predecessor symmetric difference is two alternating paths, with
   the two index-parity endpoint pairs.
4. Their only four-resource imbalance is the endpoint role current

   \[
   \operatorname{res}({\cal Q}^{\to})
     -\operatorname{res}({\cal Q}^{\leftarrow})
   =(0_L,0_U,\ e_{V_1}^--e_{V_0}^-,
                  e_{V_0}^+-e_{V_1}^+).                    \tag{0.3}
   \]

Thus the open square has exactly the central projection signature required
to transport the opened reset's one attachment and two predecessor
returns.  Omitting both seam orientations avoids the closed doubleton.

It does **not** supply the protected two-root completion of the normalized
puncture theorem:

* the attachment map changes along a path, whereas that theorem fixes
  \(\vartheta\);
* (0.3) is nonzero, so the square is not a standalone four-resource circuit;
* its normalized \(P/T/z\) deltas depend on the exterior continuation;
* both phases cannot share one identical exact residual unless another
  module contributes the negative of (0.3); and
* each phase contains an internal coordinate run \(0\,1\,1\,0\), ruling out
  a flat residence threshold at least three.

The correct positive interpretation is therefore conditional: the square
is an exact **open role converter**.  If an opened reset or another module
has the opposite endpoint current, the attachment and two predecessor
paths are identified oppositely, and a common residual contraction is
proved, then the combined module is resource balanced.  Fixed-cap,
all-width upper, residence, normalized flag, and compiler compatibility
remain additional gates.

## 1. Exact outer palettes

For the four undirected square edges put

\[
\begin{array}{c|cc}
\text{edge}&\text{lower intersection}&\text{upper union}\\ \hline
V_0V_1&L_0=K+x&U_0=K+x+y+z\\
V_1V_2&L_1=K+y&U_1=K+x+y+w\\
V_2V_3&L_2=K+w&U_2=K+y+z+w\\
V_3V_0&L_3=K+z&U_3=K+x+z+w.
\end{array}                                                \tag{1.1}
\]

Every directed orientation of one edge has its displayed lower and upper
resources.  Hence

\[
\begin{aligned}
\operatorname{low}({\cal Q}^{\to})
 &=\operatorname{low}({\cal Q}^{\leftarrow})
   =\{L_1,L_2,L_3\},\\
\operatorname{up}({\cal Q}^{\to})
 &=\operatorname{up}({\cal Q}^{\leftarrow})
   =\{U_1,U_2,U_3\}.                                      \tag{1.2}
\end{aligned}
\]

All six values in their respective resource roles are distinct.  Both
phases omit exactly the same seam palette pair \((L_0,U_0)\).

The tail and head inventories are

\[
\begin{array}{c|cc}
&\text{tails}&\text{heads}\\ \hline
{\cal Q}^{\to}
 &\{V_1,V_2,V_3\}&\{V_2,V_3,V_0\}\\
{\cal Q}^{\leftarrow}
 &\{V_0,V_3,V_2\}&\{V_3,V_2,V_1\}.
\end{array}                                                \tag{1.3}
\]

Subtracting the two rows gives (0.3).

### Theorem 1.1 (exact open four-resource ledger)

Equations (1.2)--(1.3) are the complete typed-resource difference of the
two open phases.  In particular, there is no lower or owner debt inside the
open square; its whole nonzero boundary is the exchange of \(V_0,V_1\)
between the tail and head roles.

#### Proof

Intersections, unions, tails, and heads are read directly from the six
ordered edges in (0.2).  Each edge pair has the values in (1.1), giving
(1.2); the endpoint roles give (1.3). \(\square\)

## 2. One attachment path and two predecessor paths

Use separate copies \(V_i^-\) and \(V_i^+\) for the tail and head shores.
In the head--owner projection, the two phases are

\[
\begin{aligned}
{\cal A}^{\to}
 &=\{(V_2^+,U_1),(V_3^+,U_2),(V_0^+,U_3)\},\\
{\cal A}^{\leftarrow}
 &=\{(V_3^+,U_3),(V_2^+,U_2),(V_1^+,U_1)\}.
\end{aligned}                                               \tag{2.1}
\]

Their symmetric difference is the single alternating path

\[
 V_0^+-U_3-V_3^+-U_2-V_2^+-U_1-V_1^+.                    \tag{2.2}
\]

In the predecessor tail--head projection,

\[
\begin{aligned}
{\cal P}^{\to}
 &=\{V_1^-V_2^+,\ V_2^-V_3^+,\ V_3^-V_0^+\},\\
{\cal P}^{\leftarrow}
 &=\{V_0^-V_3^+,\ V_3^-V_2^+,\ V_2^-V_1^+\}.
\end{aligned}                                               \tag{2.3}
\]

Their symmetric difference is the disjoint union

\[
\begin{aligned}
 V_1^- - V_2^+ - V_3^- - V_0^+,\\
 V_0^- - V_3^+ - V_2^- - V_1^+.
\end{aligned}                                               \tag{2.4}
\]

### Theorem 2.1 (open three-return signature)

The open square exports precisely one attachment endpoint pair and the two
predecessor-parity endpoint pairs in (2.2)--(2.4).  Closing both phases by
their respective seam orientations turns the relative attachment action
into a four-cycle and the relative predecessor action into two
transpositions, i.e. the \(q=4\) signature

\[
                         (\sigma,\sigma^2).                  \tag{2.5}
\]

#### Proof

Every interior vertex in (2.1) has degree two in the symmetric difference,
and \(V_0^+,V_1^+\) have degree one, proving (2.2).  The degree-two
components of (2.3) are exactly the two paths in (2.4).  Adding the omitted
seam endpoints closes the attachment path as one four-cycle and the two
predecessor paths separately, proving (2.5). \(\square\)

On the open paths no permutation sign is defined; the endpoint paths, not
a closed sign, are the exact invariant.

## 3. The seam doubleton and the identical-residual obstruction

The omitted seam atoms are

\[
\begin{aligned}
s^{\to}&=(L_0,U_0,V_0,V_1),\\
s^{\leftarrow}&=(L_0,U_0,V_1,V_0).
\end{aligned}                                               \tag{3.1}
\]

They are opposite orientations of one Johnson edge and use the same lower
and owner resources.

### Theorem 3.1 (seam doubleton)

The two seam orientations cannot coexist in one four-resource matching.
Adding \(s^{\to}\) closes \({\cal Q}^{\to}\); adding
\(s^{\leftarrow}\) closes \({\cal Q}^{\leftarrow}\).  Attempting both
closures repeats \(L_0,U_0\) and recreates the closed-doubleton obstruction.

The same warning applies to the three open internal edges: the forward and
reverse orientations are alternative whole phases, not atoms which may be
simultaneously selected.  Their simultaneous union repeats
\(L_1,L_2,L_3,U_1,U_2,U_3\).

#### Proof

All statements follow from (1.1), since orientation does not change the
intersection or union of an edge. \(\square\)

There is a second, logically different obstruction.

### Theorem 3.2 (no identical exact residual)

There is no one fixed four-resource residual matching \({\cal R}\),
compatible with both open phases, for which the additive typed inventory
vectors

\[
 \chi_{\cal R}+\operatorname{res}({\cal Q}^{\to}),
 \qquad
 \chi_{\cal R}+\operatorname{res}({\cal Q}^{\leftarrow})   \tag{3.2}
\]

have the same exact tail and head coordinates.

#### Proof

The identical additive residual vector cancels when the two inventory
equations are subtracted.  Equation (0.3) would then have to vanish, but
\(V_0\ne V_1\). \(\square\)

Thus equal outer palettes do not imply a common exact residual.  A common
residual is possible only after an additional phase-dependent module
cancels the endpoint current, or after phase-private resources are
contracted and equality of the resulting residual minors is separately
proved.

## 4. Exact relation to the protected puncture theorem

The protected external-puncture theorem works in one fixed functional graph:
the attachment \(\vartheta\) is fixed, one new tail row becomes an external
neighbour of a Hall shore, and two further row substitutions have resource
deltas summing to the negative anchor delta.

The open square is not such a packet.

1. Equation (2.2) changes the head--owner attachment along a nonempty path.
   It is a compound attachment exchange, not a move inside fixed
   \(\vartheta\).
2. Equation (0.3) is a nonzero tail/head current.  The two predecessor paths
   in (2.4) are projection returns, not two normalized row deltas whose sum
   is a prescribed negative resource vector.
3. A normalized depth-three option at the last internal root uses the next
   exterior departure.  Hence the square alone does not determine a common
   old/new \(P/T/z\) ledger.
4. Cut safety is compound.  Until the square is composed with the opened
   reset and all changed rows are checked against a Hall shore, neither
   \(|A_Y|-|L_Y|>0\) nor the all-cut inequalities follow.

### Corollary 4.1 (protected-two-root verdict)

The open square does not instantiate the protected two-root completion
condition, and it cannot be inserted as one allowed circuit in the fixed
functional graph of that theorem.  What it supplies is the missing
**role-conversion boundary type**: one attachment path and two predecessor
paths with exact lower/owner cancellation.

This is a positive projection result and a negative fixed-\(\vartheta\)
result.  It does not rule out a larger puncture repair in which
\(\vartheta\) is changed along (2.2) and the complete final Hall graph is
recomputed.

## 5. Conditional role-conversion composition

Let \(({\cal P}^{\to},{\cal P}^{\leftarrow})\) be another two-phase open
module, for example an opened reset.  Suppose:

1. its typed resource current is the negative of (0.3):

   \[
   \operatorname{res}({\cal P}^{\to})
    -\operatorname{res}({\cal P}^{\leftarrow})
   =(0_L,0_U,e_{V_0}^--e_{V_1}^-,
                  e_{V_1}^+-e_{V_0}^+);                    \tag{5.1}
   \]

2. its one attachment and two predecessor **full alternating paths** are
   identified oppositely with (2.2)--(2.4), with internal projection
   supports disjoint except at the declared identifications;
3. each combined phase is a literal four-resource matching;
4. after quarantining or contracting the phase-private supports, both
   phases have one identified residual factor; and
5. the combined normalized flags, residence, upper decks, and compiler
   hazards pass their literal tests.

### Theorem 5.1 (conditional open-square role conversion)

Under conditions 1--5,

\[
 {\cal P}^{\to}\cup{\cal Q}^{\to}
 \quad\text{and}\quad
 {\cal P}^{\leftarrow}\cup{\cal Q}^{\leftarrow}             \tag{5.2}
\]

have identical complete four-resource inventories, and their attachment
and predecessor projection differences close.  Consequently the open
square supplies a valid central role conversion inside the declared common
residual contraction.

#### Proof

Equations (0.3) and (5.1) cancel coordinatewise.  Opposite identification
of the three endpoint paths closes every degree-one projection endpoint.
Conditions 3--4 promote the signed inventory identity to two literal
matchings with one common residual.  Condition 5 supplies precisely the
rows not represented in the four-resource projection. \(\square\)

The theorem is deliberately conditional: the square proves the current and
path algebra, not conditions 3--5.

## 6. Flat-residence obstruction

Read either open phase in its directed path order.  For
\({\cal Q}^{\to}\), the vertex order is

\[
                         V_1,V_2,V_3,V_0.                    \tag{6.1}
\]

The active-coordinate traces are

\[
\begin{array}{c|cccc}
 &V_1&V_2&V_3&V_0\\ \hline
x&1&0&0&1\\
y&1&1&0&0\\
z&0&0&1&1\\
w&0&1&1&0.
\end{array}                                                \tag{6.2}
\]

For \({\cal Q}^{\leftarrow}\), in the order
\(V_0,V_3,V_2,V_1\), the \(y,z\) rows exchange, while

\[
                         w:0,1,1,0                           \tag{6.3}
\]

is unchanged.

### Proposition 6.1 (internal length-two run)

Both open phases contain a positive \(w\)-run of length two flanked
internally by zeros.  Exterior continuation cannot lengthen it.  Therefore
the bare square has no flat chronology with minimum positive coordinate
run at least three.

#### Proof

Equations (6.2)--(6.3) place the ones at the two middle vertices and their
immediate flanking zeros at the first and last vertices of the displayed
segment.  Altering letters outside the segment cannot change either
adjacent zero. \(\square\)

A nonflat collar or a larger rethread is consequently necessary even after
the role-conversion current is paired.

## 7. Exact boundary

The open Johnson square does improve the closed q-gon picture:

* it omits the two opposite seam atoms rather than trying to select their
  owner-repeating doubleton;
* it preserves the complete surviving lower and upper palettes;
* it exports exactly the three endpoint paths of an opened reset; and
* it gives the exact opposite-current interface required of a central role
  converter.

It does not close the puncture lane by itself.  The remaining conditions are:

1. a literal common two-phase flag lift, including the exterior departure at
   the last internal root;
2. an opposite-current opened reset or other module;
3. a common residual contraction rather than marginal equality alone;
4. a nonflat residence repair of the internal \(0\,1\,1\,0\) run;
5. arbitrary-width upper and outer occurrence protection;
6. fixed-cap/strict-gammoid compiler compatibility; and
7. final functional Hall replay when the attachment path changes
   \(\vartheta\).

Hence the exact answer is:

> the open square is the correct central three-return role converter, but it
> is not a protected two-root completion and it has an unavoidable endpoint
> residual current plus a flat length-two residence obstruction.
