# Audit of the fixed sharp-pivot global-host reduction

**Date:** 2026-08-06  
**Primary note:**  
MATH_THEOREM_FIXED_SHARP_PIVOT_BANK_TWOFACTOR_AND_CATALAN_HOST_GATE_20260806.md  
**Verdict:** PASS for the protected two-factor and exact connector
reduction; NO-GO for an unconditional connected resident carrier.

## 1. Packet and factor counts

A collared depth-\(d\) sharp-pivot path has \(3d\) Johnson transitions.
Each transition lifts to two Middle-Levels incidences, so one packet has
\(6d\) incidences.  For \(H\le31\),

\[
 |E(\mathcal P)|\le6Hd\le186d.
\]

On the direct upper-shore lift the relevant graph is \(ML_{m+1}\), so the
small protected-factor threshold is

\[
 186d\le(m+1)-2=m-1.
\]

This agrees with the corrected top-deadline theorem.  Since
\(d=\Theta(\sqrt m)\), the inequality is eventually true.

Alternating the incidence paths gives exactly \(3d\) edges of each colour
per full packet.  Hence \(f_i\le3Hd\le93d\).  Substitution in the
Hamilton-anchored bound gives

\[
\begin{aligned}
8r(93d)^2&=69192\,rd^2,\\
64r^2(93d)&=5952\,r^2d,\\
10(93d)&=930d.
\end{aligned}
\]

The polynomial component estimate is therefore arithmetically correct.
The associated common coloured edges prevent it from being called a
simple carrier.

## 2. Two incidence orientations must not be conflated

For the original rank-\(m\) path on \([2m+1]\), lifting through its
rank-\((m+1)\) unions gives the balanced graph \(ML_{m+1}\).  A spanning
two-factor there is directly upper-\(q1\)-exact.

The rooted Catalan representative decomposition is naturally applied
after complementing the owner path and lifting through its lower incidence
shore.  This exchanges lower and upper immediate palettes and exchanges
positive-run with zero-gap residence.

Therefore:

* the direct protected two-factor theorem gives zero upper-\(q1\) defect
  but no connectedness;
* the Catalan \((e,s)\) system is an exact complementary rooted-host
  certificate;
* neither statement alone gives one chronology satisfying both residence
  polarities and all downstream source guards.

The primary note records this distinction explicitly.

## 3. Catalan ledger

A forest \(Q_0\) on \(W\) roots representing \(U-e\) distinct upper
colours has

\[
 W-(U-e)=C+e
\]

components.  A free-port forest leaving \(s\) paths therefore uses

\[
 (C+e)-s
\]

connector edges.  This verifies formula (3.2) and the special target
\((e,s)=(O(1),1)\).

The ordered-Hall deficiency is exact only after \(M_0,Q_0\), all forced
paths, and the literal free-port graph have been fixed.  It is not a
selection theorem for \(Q_0\).

## 4. Uniform-marginal scale

For a size-\(f\) matching in an \(r\)-regular simple bipartite graph, let
\(c\) count all edges between its two endpoint shores.  The union of all
incident stars has size \(2rf-c\); deleting the \(f\) protected edges gives

\[
 |D_{\rm star}|=2rf-c-f.
\]

Because \(f\le c\le f^2\), the two bounds in the primary note follow.
When \(f=o(r)\) and the common-basis marginal is \(\Theta(1/r)\), the
expected star-halo intersection is \(\Theta(f)\).

This proves only that the one-point avoidance lemma is insufficient.  It
does not prove that every common basis meets the star halo.

## 5. Obstruction scope

The three-arc example proves failure for one frozen parity matching.
The four-edge example proves failure of the complete protected two-factor
fibre at \(m=3\).  Neither is an asymptotic no-go for a prospectively
selected sharp-pivot bank.

Their valid consequence is the quantifier statement:

\[
\text{small clean protected bank}
\not\Longrightarrow
\text{post-hoc protected Hamilton completion}.
\]

An asymptotic positive theorem may still cochoose the packet labels,
parity matching, Catalan representatives, and connector order.

## 6. Final audit boundary

Unconditional:

1. the at-most-\(31\) path bank embeds in an exact simple spanning
   two-factor;
2. its direct upper-\(q1\) palette is exact;
3. the rooted \((e,s)\) certificate and its counts are exact;
4. fixed literal \(O(d)\) common-basis conflicts are avoidable;
5. full endpoint-star avoidance is not obtained from one-point marginals.

Still open:

1. a protected Hamilton or \(O(1)\)-component completion;
2. a protected common representative forest with ordered port deficiency
   \(O(1)\);
3. elimination of common-edge debt in the anchored completion;
4. global positive residence, zero-gap residence, and clipped-flag
   completion;
5. one source antecedent and the deep interval-OR/common-cap rows.

No all-\(k\), \(B+O(1)\), or connected-carrier claim follows from the
primary note.
