# Audit: the PBBS portal-tree walk is not a literal OR compiler

Date: 2026-07-26

## Verdict

The portal-tree construction in
`MATH_THEOREM_PBBS_PORTAL_TREE_ANNULUS_LOCAL_CHRONOLOGY_20260726.md`
proves a useful chronology theorem:

\[
 |\mathscr W_H|=W+O(H\operatorname {Cat}_m),
\]

and every directed PBBS window of length at most \(H\) occurs as a
consecutive subwalk.  Consequently every required lower intersection and
upper union occurs as the intersection or union of a consecutive block of
middle states.

It does **not** prove a literal contiguous-OR word of that length.  The
claimed passage from chronology length to coefficient-one word length is
missing and is exactly the already-audited short-residence factorization
gate.

## 1. Why chronology is insufficient

A Johnson walk is a sequence of middle sets

\[
 X_0,X_1,\ldots,X_{L-1}.
\]

Using these states themselves as word letters realizes consecutive
**unions**, but it cannot realize a proper lower intersection: every
nonempty OR contains at least one whole rank-\(m\) letter and therefore
has rank at least \(m\).

The standard transformed letters

\[
 A_i=\bigcap_{j=0}^{H}X_{i+j}
\]

satisfy the needed identities

\[
 X_i=\bigcup_{j=i}^{i+H}A_j
\]

only under the delay-\(H\) safety condition: no coordinate may leave and
return inside the relevant window.  An arbitrary Johnson walk does not
have this property.  The portal construction makes the problem worse at
its repair excursions: \(P_vP_v^{-1}\) immediately retraces every exchange,
so the changed coordinates leave and return within a short interval.

Thus the presence of a PBBS window as a consecutive subwalk certifies the
set identities

\[
 \bigcap X_i=S,\qquad \bigcup X_i=U,
\]

but supplies no literal set-valued letters whose contiguous OR is \(S\).

## 2. What remains true

The following statements from the portal note survive.

1. The component-tree Euler walk has length
   \(W+2(c_m-1)\).
2. Adding one radius-\(H\) forward/backward excursion per portal makes
   every directed PBBS window through depth \(H\) consecutive at total
   chronology length \(W+O(Hc_m)\).
3. Since \(c_m\le\operatorname {Cat}_m\), this chronology overhead is
   \(o(W)\) throughout every fixed Gaussian window.

This is a useful state-sequence theorem and may serve as an input to a new
factorization.  It does not close the annulus.

## 3. Corrected frontier

To obtain a literal word one must still do one of the following.

* Prove delay-\(H\) safety after a different component splice.
* Factor the unsafe portal excursions with total additional cost \(o(W)\).
* Use an in-place dominance/baseline replacement whose crossing windows
  realize the lost lower targets.

The existing dominance-staircase compiler charges unsafe short residence
through \(\nu_H(P_m)\), leading again to the open fixed-window gate

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)
 =o_A(\operatorname {Cat}_m\sqrt m).
\]

Therefore the sentence in the portal note claiming that the Gaussian
annulus gate is closed for coefficient-one word length must be retracted;
only the Johnson-chronology version is proved.
