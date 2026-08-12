# Audit of the Q8 carousel: owner splice valid, aggregate seam disposal insufficient

Date: 2026-07-26

## 0. Verdict

The owner-level results of
MATH_THEOREM_Q8_CAROUSEL_PHASE_SPLICE_SPARSE_SEAM_MACRO_20260726.md
are valid:

* the four phasewise shores splice to one neighbour permutation of Q8;
* every component is an isometric C16;
* the predecessor/successor frame labels close cyclically; and
* inserting disjoint payload direction blocks gives literal long
  isometric macrocycles on the declared carrier.

Two scope qualifications are essential.  Raw macrocycle isometry holds for
all \(L\), but an arbitrary payload word is not a two-sided literal decoder.
Without a separate phase-reset certificate, take \(L\) even to preserve the
original seam parity.  Also, the carrier has \(256(L+1)\) owners rather than
the \(2^{8(L+1)}\) owners of a full packet, so it is not yet a CPM option.

The seam-start estimate

\[
 \#\{H\text{-windows meeting a seam}\}\le 16H
\tag{0.1}
\]

is also correct for one maximum-depth window on one macrocycle.

It does **not** imply an o(W) aggregate central-target loss under the
coefficient-one objective. The objective sums every signed depth
1<=q<=H. A seam belongs to q starts at depth q; summing over depths
costs Theta(H^2) per seam. Quarantining all seam-meeting windows gives

\[
 \boxed{
 \text{uncertified signed occurrences}
 \le {H(H+1)\over L+1}\,G}
\tag{0.2}
\]

on carrier owner mass G, up to a harmless factor two if both directed
orientations are separately certified.

Thus this disposal argument needs

\[
 L/H^2\longrightarrow\infty.
\tag{0.3}
\]

In an ambient problem with L=O(m) and the required
H/sqrt(m)->infinity, (0.3) is impossible. The carousel remains a genuine
frame-changing primitive, but a successful recursion must **decode or
reroute almost all seam-crossing windows**; making the seams sparse only on
the scale H/L is insufficient.

This is a no-go for occurrence-by-occurrence quarantine, not a lower bound
of the same size on actual target holes: cross-carrier coverage can recapture
some exceptional targets.

## 1. Exact aggregate count

One macrocycle has length 16(L+1) and contains sixteen seam edges. Fix a
depth q. One cyclic edge lies in exactly q forward windows of q
transitions. Therefore at most 16q starts have a depth-q window meeting
a seam. Each such start has one lower and one upper target, so
pessimistically at most 32q signed target occurrences are uncertified.
Summing gives

\[
 \sum_{q=1}^H32q=16H(H+1)
\tag{1.1}
\]

per macrocycle. If the carriers contain owner mass G, their number of
macrocycles is G/[16(L+1)]. Multiplying proves (0.2).

This is an occurrence upper bound. Actual target holes can be smaller if
other macrocycles cover the uncertified targets. No such global coverage
theorem is presently proved, so (0.2), rather than the maximum-depth start
fraction, is the valid unconditional seam charge.

## 2. Correct surviving use of the carousel

The carousel may still enter a positive proof in either of two ways.

1. Prove a literal seam decoder whose aggregate collision excess over all
   depths is O(H) rather than O(H^2) per macrocycle.
2. Place the macrocycles in a global colored packet matching which covers
   the seam targets from other packets, so that (1.1) is not charged as
   holes.

The owner splice and frame holonomy are useful inputs to both routes. The
simple sparse-seam quarantine is not itself a coefficient-one interface.

Finally, every completed macrocycle has one common positional antipodal
matching: the offset \(4(L+1)\) pairs \(w_t\) with \(w_{t+4}\) and pairs
corresponding payload directions in blocks \(D_t,D_{t+4}\).  This becomes a
statewise bottom-wire obstruction when the payload direction fields
normalize the same phase kernel.  Positional pairing alone does not
constrain an arbitrary payload decoder.
