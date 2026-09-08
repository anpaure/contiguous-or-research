# The single-bulge hinge has an almost-spanning integral base-layer packing

**Date:** 2026-08-07  
**Method:** maximal capacitated star packing in the Boolean incidence graph  
**Status:** theorem, independently audited.  Its scope is the asymptotic
triangular regime; higher target rows remain outside the claim.

## 1. Base stars of a literal hinge ring

Use the odd parameters

\[
 n=2m+1,\qquad s=m-2d,
\]

and let

\[
                         R=3(d-1).
\]

Assume throughout that \(d\ge2\), \(s\ge1\), and
\(n-s+1\ge4d\).  These conditions hold throughout the sufficiently large
triangular regime.

In the length-\(3d\) single-bulge ring of
`MATH_THEOREM_SINGLE_BULGE_TRIANGULAR_RESET_FACTOR_20260807.md`, put

\[
                         P=C_0\setminus H,
 \qquad |P|=s-1.
\]

Exactly \(R\) private phases are low.  If their private labels form
\(L\), then the ring's complete rank-\(s\) target inventory is

\[
                         \{P\cup\{x\}:x\in L\}.       \tag{1.1}
\]

Thus its bottom row is an \(R\)-petal star in the inclusion graph between
the rank-\((s-1)\) and rank-\(s\) layers.

Conversely, every pair

\[
 P\in{[n]\choose s-1},\qquad
 L\subseteq[n]\setminus P,\qquad |L|=R              \tag{1.2}
\]

lifts to a literal single-bulge ring whenever

\[
                         n-s+1\ge4d.                  \tag{1.3}
\]

Indeed, after choosing the \(R\) low labels, (1.3) leaves at least
\(d+3\) coordinates outside \(P\cup L\).  Choose \(d\) of them as the
reset bank \(H\), three more as the high-phase private labels, and arrange
the resulting \(3d\) private labels in the schedule
\(\mathsf L^{d-1}\mathsf H\) repeated three times.  Taking
\(C_0=P\cup H\) gives exactly (1.1), and the cited hinge theorem supplies
the flat owner row, q1 palettes, residence and regeneration.

No disjointness of the auxiliary \(H\) and high-label banks is required
between different rings; only the named targets in (1.1) are being packed
in this theorem.

## 2. A maximal star packing

Put

\[
 \mathcal V={ [n]\choose s},\qquad
 \mathcal C={ [n]\choose s-1},
 \qquad V=|\mathcal V|,\quad C=|\mathcal C|,
\]

and

\[
                         v=n-s+1.                     \tag{2.1}
\]

Every centre \(P\in\mathcal C\) has exactly \(v\) rank-\(s\) supersets,
and every target \(S\in\mathcal V\) contains exactly \(s\) centres.  Hence

\[
                         Cv=Vs.                       \tag{2.2}
\]

Greedily choose a previously unused centre having at least \(R\) unused
rank-\(s\) supersets, reserve any \(R\) of them as one star, and mark those
targets used.  Stop when no such unused centre remains.  Let \(M\) be the
number of selected stars and \(U=MR\) the number of used targets.

### Theorem 2.1 (integral base-layer packing)

The greedy packing satisfies

\[
 \boxed{
 M\ge {C(v-R+1)\over Rs+v-R+1}}
 \tag{2.3}
\]

and therefore

\[
 \boxed{
 {U\over V}
 \ge
 {Rs(v-R+1)\over v(Rs+v-R+1)}.}
 \tag{2.4}
\]

In the triangular regime \(d=\Theta(\sqrt n)\), the right side of (2.4)
is

\[
                         1-O(1/d).                    \tag{2.5}
\]

#### Proof

At termination every unselected centre has at most \(R-1\) unused
supersets, and hence at least \(v-R+1\) used supersets.  Count incidences
\((P,S)\) with \(P\) an unselected centre, \(S\) a used target and
\(P\subset S\).  The centre count gives at least

\[
                         (C-M)(v-R+1)
\]

incidences.  A used rank-\(s\) target has only \(s\) rank-\((s-1)\)
subsets, so the target count gives at most \(Us=MRs\).  Thus

\[
                         (C-M)(v-R+1)\le MRs,
\]

which rearranges to (2.3).  Multiplying by \(R\), dividing by \(V\), and
using (2.2) gives (2.4).

Here \(s,v=\Theta(n)\), \(R=\Theta(d)=\Theta(\sqrt n)\), and
\(Rs\gg v\).  Both factors lost from one in (2.4) are therefore
\(O(R/v)+O(v/(Rs))=O(1/d)\), proving (2.5). \(\square\)

## 3. Capacity relative to the theta deficit

The central local limit gives

\[
                         {V\over W}\longrightarrow e^{-\pi}.
\]

Consequently Theorem 2.1 selects target-disjoint literal hinge rings whose
rank-\(s\) rows contain

\[
                         (e^{-\pi}-o(1))W             \tag{3.1}
\]

endpoints.  This exceeds the required theta reset bank

\[
                         (\theta+o(1))W,
 \qquad \theta=4\sum_{a\ge1}e^{-4\pi a^2},            \tag{3.2}
\]

by more than three orders of magnitude.  In particular, the bottleneck
rank row of the fractional hinge factor rounds integrally with enormous
margin; no growing-uniformity matching theorem is needed for that row.

## 4. Exact remaining scope

The theorem packs only the rank-\(s\) inventories (1.1).  Distinct base
targets do **not** by themselves force the higher hinge targets, saturated
bridge completions, immediate-upper colours, or owners of two rings to be
disjoint.  Those resources may contain more than one selected base target.

Thus the triangular hinge-factor gate is reduced, but not solved.  The
remaining integral selection must extend a theta-sized subfamily of this
base-star packing so that simultaneously:

1. every higher marked and bridge target is unique;
2. owner and upper palettes are compatible with the residual PBBS factor;
3. the ring cycles fuse into boundedly many chronology components; and
4. the terminal compiler remains feasible.

The new conclusion is exact: **base-layer named-target integrality is no
longer an obstruction.**  The obstruction begins strictly in the correlated
higher rows.
