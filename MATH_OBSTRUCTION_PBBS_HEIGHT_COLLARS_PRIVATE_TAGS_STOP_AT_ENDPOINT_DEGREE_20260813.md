# Global private tags separate collar interiors but cannot fix the PBBS endpoint degree

**Date:** 2026-08-13  
**Status:** correction and sharp obstruction.  A preliminary version of
this note incorrectly inferred a protected two-factor extension after
separating all collar interiors.  The inference is false: the independent
all-five incoming-collar bank has protected degree three at every internal
height-spine owner.  The valid private-tag theorem below applies only to
the interiors.  The complete decision and source-host quantifier are in
`MATH_THEOREM_PBBS_SYNCHRONIZED_COLLAR_PLANTING_DECISION_AND_EXACT_SOURCE_HOST_QUANTIFIER_20260813.md`.

## 1. The valid interior-separation theorem

Use

\[
 n=2r+1,
 \qquad R=r+1,
\]

and high heights `4<=h<H`.  For one height-pentagon screen bank, direct
substitution gives

\[
 G_h=\{h+2,h+3,\ldots,2h\}
       \mathbin{\dot\cup}
       \{2h+4,2h+6,\ldots,2r\}.
\tag{1.1}
\]

Hence every high core contains the common tail

\[
 J_H=\{2H+2,2H+4,\ldots,2r\},
 \qquad |J_H|=r-H.
\tag{1.2}
\]

There are `N=5(H-4)` synchronized incoming collar paths.  Assume

\[
 N\le r-H,
 \qquad N+\delta\le r+1.
\tag{1.3}
\]

Choose distinct global tags

\[
 T=\{g_{h,i}:4\le h<H,\ i\in\mathbb Z_5\}
       \subseteq J_H.
\tag{1.4}
\]

For collar `(h,i)`, choose the deletion set of the tagged common-union
collar lemma so that

\[
 |D_{h,i}|=\delta-2,
 \qquad D_{h,i}\cap T=\{g_{h,i}\},
\tag{1.5}
\]

and order `g_{h,i}` first.  This is possible by `(1.3)`.

Every positive-time collar owner and every internal collar lower colour
then has tag signature

\[
                         T\setminus\{g_{h,i}\}.
\tag{1.6}
\]

All fixed pentagon owners and lower colours contain every tag in `T`.
Thus:

* internal resources on distinct collars are disjoint because they miss
  different tags;
* no internal collar resource collides with a fixed pentagon resource;
* within one collar, simplicity follows from the original sliding-window
  proof; and
* the endpoint is the only possible owner overlap.

This is a deterministic proof of cross-height **interior** separation.  No
random order or local lemma is required.  If `delta<=H`, the convenient
bound

\[
                         6H\le r+20
\tag{1.7}
\]

suffices.  At `H<=2d+1`, `delta=d`, the eventual bound `r>=12d-14`
suffices.

## 2. The endpoint obstruction

For adjacent high heights, the literal PBBS endpoint calculation is

\[
                         P_{h,0}=Q_{h-1,1}=U_h.
\tag{2.1}
\]

After the simultaneous pentagon head shifts, the role-zero return edges
form the height spine

\[
                  \cdots-U_{h-1}-U_h-U_{h+1}-\cdots.
\tag{2.2}
\]

These two distinct protected spine edges already occupy degree two at the
internal owner `U_h`.  The independent incoming role-zero synchronized
collar ends at `P_{h,0}=U_h`; its first internal owner misses the private
tag `g_{h,0}`.  Consequently its endpoint edge is different from both
all-tag spine edges.

### Theorem 2.1 (all-five degree-three obstruction)

The independent all-five incoming-collar bank has protected owner degree
at least three at every internal adjacent-height seam.  It is contained in
no simple spanning two-factor, regardless of how its collar interiors are
chosen.

#### Proof

Equations `(2.1)--(2.2)` give two distinct protected edges incident at
`U_h`.  The role-zero incoming collar gives a third distinct edge by its
missing-tag signature.  A two-factor has owner degree two.  \(\square\)

Thus interior collision-freedom is not the full correlated planting
theorem.  A protected-factor extension theorem cannot repair prescribed
degree three.

## 3. Correct surviving graph face

The endpoint-corrected bank retains incoming collars at roles `1,2,3,4`,
omits the incoming role-zero collar, and places one full-union collar after
the free old head `Q_{h,0}`.  That bank is an incidence path forest after
the same private-tag separation.  It no longer has exact all-five incoming
upper-current cancellation, so it must be augmented with the known
rank-stratified alternative upper witnesses.  At size `O(Hr)` and exposure
`O(H)`, the polynomial protected-forest theorem then gives a simple
directed spanning owner/q1 two-factor for all sufficiently large `r` at
`H=O(sqrt r)`.

This is a graph theorem only.  Long one-tag arms and the separated
short-block lemma show that, **conditional on a resident global owner
trace**, distinct local source pin blocks can be spaced far enough that
their erosion tests decouple.  They do not prove the local safe-emission
containments, biresidence of the unprotected completion, or existence of
the resident trace.

The exact remaining rows are therefore:

\[
\boxed{
\begin{gathered}
\text{resident oriented completion passing every local pinned-erosion test,}\\
\text{zero-gap/clipped-flag absorption on the fixed and unprotected blocks,}\\
\text{occurrence-level typed suffix rank / common-cap routing.}
\end{gathered}}
\]

Missing-tag privacy alone proves none of these three assertions.
