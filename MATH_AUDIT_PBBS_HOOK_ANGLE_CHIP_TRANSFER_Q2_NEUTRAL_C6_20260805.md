# Self-audit: PBBS hook-angle chip-transfer C6

**Date:** 2026-08-05  
**Object audited:**
`MATH_THEOREM_PBBS_HOOK_ANGLE_CHIP_TRANSFER_Q2_NEUTRAL_C6_20260805.md`  
**Method:** independent symbolic dependency and index audit; no state
enumeration and no solver

## 1. Rank and ground-size audit

The base word `D` has semilength

\[
                         h+(b-1)=m-1.
\]

Thus `000D` has length `3+2(m-1)=2m+1`, contains `m-1` ones, and has
exactly three forward survivors.  Its complement outside the four labels
`a_0,a_1,a_2,c` has size

\[
 (2m+1)-(m-1)-4=m-2,
\]

so all ranks in the clean-C6 normal form are correct.

## 2. PBBS-index audit

Rooting the three middle states obtained from `000D` gives, in the order
`a_0,a_1,a_2`,

\[
                         D10,
                         10D,
                         1D0.
\]

Their common reverse survivor is `c`.  The relation between these states
and the clean-C6 owners is

\[
 P_{i+1}=f^{-1}(Z_i),
 \qquad
 Q_{i+1}=f(Z_i).
\]

Cycling the dummy index recovers exactly the old shores `P_i Q_i`; there
is no orientation reversal hidden in the theorem.

## 3. Two-step inverse audit

Use the exact inverse rule

\[
 0_r(X0_sY)\longmapsto0_s\bar Y1_r\bar X.
\]

For `D=U0_cV` this gives the three `P_i` rows

\[
\begin{array}{c|c}
0&\bar V110\bar U\\
1&\bar V011\bar U\\
2&\bar V101\bar U.
\end{array}
\]

With `U=A1_eB`, their reverse roots are `a_2,e,e`.  A second application
gives

\[
\begin{array}{c|c}
0&U1_cV00\\
1&B1_cV100A\\
2&B1_cV010A.
\end{array}
\]

The maximum heights are respectively `h+1,h,h`.  In every row, the
rightmost maximum during `V` is the image of the rightmost post-`c`
height-`(h-1)` occurrence of `D`.  Its following down-step is the same
coordinate `d`.  The post-`V` maxima are at most `2,1,1`; since `h>=3`
they cannot tie.  Thus the common-deletion claim is index-consistent.

The coordinate `d` is a zero of `D`, is not `c`, and is not active, hence
`d in K`.  Therefore the companion rows `P_i-d` satisfy the hypotheses of
the exact common-deletion q2 theorem.

## 4. Selection audit

The owner actions are `(h,1^b)` and `(h+1,1^(b-1))`.  Their top gaps are
`h-1` and at least `h`.  For `h>=3` both are at least two.  The
spectral-gap theorem therefore covers all six old/companion q1
occurrences.  No inference from action profile to component distinctness
is used for selection.

## 5. Angle-coordinate audit

A hook plane forest has one unique length-`h` spine.  Extra soliton-one
edges must be leaves: a nonleaf extra branch would survive one pruning and
create a second soliton part at least two.  There are two ordered leaf
banks at each of the first `h-1` spine vertices and one at the terminal
spine vertex, totaling `2h-1`.

The equivalent peak-deletion count is exact: one deletion leaves
`1^(h-1)0^(h-1)`, which has `2h-1` gaps.  Reconstruction inserts `b+1`
peaks, one mandatory in the central gap and `b` freely distributed.  Thus
the rooted hook words are genuinely weak compositions of `b` into
`2h-1` parts; this is not inferred merely from equality of two counts.

Prepending/appending `10` adds a virtual-root leaf on the two sides of the
spine tree.  These are the first and last banks of the linear contour
order and hence adjacent in its cyclic closure.  Removing the transferred
leaf recovers the common base vector `y`.  Thus every claimed edge has the
form

\[
                         x\leftrightarrow x-e_j+e_{j+1}.
\]

The identification of cyclic bank vectors with physical hook components
uses exactly the standard action--angle theorem and the already-proved
fact that each hook torus is one PBBS cycle.  The proof does not infer this
only from matching component counts.

## 6. Connectivity and topology-scope audit

On labeled weak compositions, adjacent unit transfers move every chip to
slot zero, proving connectedness.  Quotienting a connected graph by the
cyclic group remains connected.  This proves incidence connectedness only.

Promotion reduces `b` by one and preserves `h+b=m`; after `b` promotions
one reaches the unique mass-zero/single-soliton angle.  Hence the graded
hook quotient is connected.  The audit does not turn that connectedness
into a compatible cut order or loose hypertree.

The theorem correctly separates three cases:

* distinct hook necklaces: a genuine `1+1+1` three-component C6;
* equal hook necklaces: a valid q1/q2 switch with no merger claim;
* `b=1`: the hook sector already has one angle torus.

No simultaneous loose-forest conclusion is drawn.

## 7. Rotation audit

Every owner has trivial rotational stabilizer: a nontrivial period of a
length-`2m+1`, weight-`m` word would have orbit size dividing both `m` and
`2m+1`.  A six-owner support has at most `6^2=36` ordered overlap
relations, each determining at most one rotation.  Thus `2m+1>36` is a
valid sufficient, not necessary, condition for two disjoint copies.

## 8. Verdict

**PASS**, with the following dependency/scope labels explicit:

1. hook necklace coordinates use the standard exact PBBS action--angle
   correspondence;
2. the result is an angle-incidence and individual-lift theorem;
3. global physical packing and all post-q2 compiler gates remain open.
