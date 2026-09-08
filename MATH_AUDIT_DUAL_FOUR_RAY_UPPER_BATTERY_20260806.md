# Independent symbolic audit of the saturated dual four-ray battery

**Date:** 2026-08-06  
**Verdict:** PASS for the dual-ray identity, all four signs, cancellation of
the four rank-`m+1` pivot currents, common-shield isolation, and the
`8m+5` bi-battery count.  The native-plus-battery conclusion remains
conditional on cross-native occurrence isolation exactly as stated in the
corrected theorem.

## 1. One port

With `Q_p` of size `p=m-2`,

\[
 R=\Omega\setminus(Q_p\cup\{a,d\}),\qquad
 C=R\setminus\{w\},
\]

has `|C|=m`.  The pivot states `C+d,C+a` therefore have rank `m+1`.
For the word

\[
                 \{a,d\},P,\{w\},q_p,\ldots,q_1,\{a,d\},
\]

every changed interval avoids the shields and starts at `P`.  The
pivot-only current under `(C+d)->(C+a)` is

\[
                              [C+a]-[C+d].
\]

After adjoining `w,q_p,...,q_(j+1)`, the two values are exactly

\[
 \Omega\setminus(Q_j+a),\qquad
 \Omega\setminus(Q_j+d).
\]

This verifies the complement direction and the reverse index.  Those
values have rank `2m-j`, with minimum `m+2`.

## 2. Four-port signs and anchors

The required current `-bar(D)` has directions

\[
 \begin{array}{c|cccc}
 \text{rail}&Y^+&Y^-&X^+&X^-\\ \hline
 \text{complement direction}&a-d&d-a&a-d&d-a.
 \end{array}
\]

Thus `Y^+,X^+` use `(C+a)->(C+d)` and `Y^-,X^-` use the reverse.  For the
two `Y` rails, choosing anchors `y_1,y_(p+1)` leaves the same core

\[
                              C_Y=X+b+c.
\]

For both `X` rails, choosing anchor `b` leaves

\[
                              C_X=Y+c.
\]

The two equal-core opposite-direction pairs cancel their pivot-only
currents literally.  The remaining strict-upper terms are precisely
`-bar(D)`.

## 3. Shield and count audit

The shield `{a,d}` contains the symmetric difference of every pair of
pivot states, so it is sufficient even though it does not contain their
common core.  Any interval meeting two ports contains their shared shield
and is invariant.  This proves there are no two-sided or cross-port terms.

In the eight-port lower-plus-upper battery there are

* `8p` rail singleton positions;
* four additional upper-anchor positions;
* eight pivots; and
* nine shared shields.

The total is

\[
                         8p+4+8+9=8m+5.
\]

Every upper pivot has rank `m+1`; no rank-`m+2` letter is used.

## 4. Composition boundary

The battery shields isolate battery pivots from each other and from a fixed
exterior.  They do not automatically identify the changed intervals of a
native cyclic factor trade with the linear battery occurrences.  Nor do
they prove that an interval spanning a changed native occurrence and the
battery block has invariant union.

Therefore the exact unconditional conclusion is the physical current of
the eight-port battery block itself.  Native cancellation is literal only
under the theorem's additional capacity-separation and cross-region
shield/coinstantiation hypotheses.  This scope is necessary and is stated
correctly in the final theorem.
