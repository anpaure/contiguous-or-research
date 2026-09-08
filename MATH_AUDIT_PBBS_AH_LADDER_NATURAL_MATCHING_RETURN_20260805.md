# Audit of the natural-matching return on the PBBS height ladder

**Date:** 2026-08-05  
**Method:** direct cancellation and exchange-triangle replay; no computation  
**Audited file:**
`MATH_OBSTRUCTION_PBBS_AH_LADDER_NATURAL_MATCHING_RETURN_20260805.md`

**Audited SHA-256:**
`294e6433fd04aaeba72b76947d049cfe6a9e3edcd32da863022785980a40275e`

## 0. Verdict

**PASS at stated scope.**  The matching identities and the absence of
three- or four-cycle returns are exact.  No obstruction to a longer
`O(d)` cycle cover is claimed.

## 1. Survivor replay

For

\[
 I_h=1\,0^{h+1}1^{h-1}(01)^{r-h},
\]

the forward prefix first reaches its minimum at coordinate `h+1`; reverse
`01` cancellation reduces the word to `1,0,0` and leaves coordinate `1`.
Thus `p_+(I_h)=h+1` and `p_-(I_h)=1`.

It follows literally that \(f(I_h)=A_h\) and
\(f^{-1}(I_h)=B_h\).  Therefore \(I_hU_h\) is the retained \(M_0\) edge,
while \(I_hU_{h+1}\) forces the \(M_1\) arc
\(B_h\to A_{h+1}\).
The arc is legal because
\(f^2(B_h)=f(I_h)=A_h\ne A_{h+1}\).

## 2. Triangle replay

Intersecting the source and target gives

\[
 K_h=00\,1^h0^{h+1}(10)^{r-h-1}.
\]

The two leading zeros, the Dyck mountain, and the alternating tail expose
exactly the three forward survivors `0,1,2h+2`.  The target adds `1`, but
the source adds `2h+1`.  Hence the source is not one of the three possible
centers of a directed star triangle on `K_h`.

The classified PBBS triangle theorem therefore excludes a directed
triangle containing the forced arc.  The independent no-`C8` theorem
excludes every directed four-cycle.  A directed two-cycle would lift to
an alternating \(C_4\) in the adjacent-rank incidence graph, which is
impossible.  This proves the asserted minimum cycle length five.

## 3. Boundary replay

The forced arcs are pairwise endpoint-disjoint and all avoid the socket
owner `U_2`; the latter retains its natural `M_0` connector edge.  Thus the
endpoint can remain protected in the proposed colouring.

The note correctly stops at the displaced-survivor cycle-cover problem.
A longer cycle may combine several forced arcs, so the local girth result
does not imply superlinear or linear-in-`m` support.
