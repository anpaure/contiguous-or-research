# Audit: coloured spectral fresh-path escape

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_COLOURED_SPECTRAL_FRESH_PATH_ESCAPE_20260806.md`  
**Method:** degree and forbidden-neighbour replay; no computation or search

The Johnson induced-average bound is

\[
 D_0\alpha-t(1-\alpha),\qquad D_0=t(k-t).
\]

Passing to a minimum-degree core loses a factor two.  Condition (2.1) is
exactly the inequality making that minimum degree exceed
`t|H|+dk`.

At the second transition, neighbours inserting a forbidden label number at
most `t|H|`.  Reusing the first insertion as a deletion or the first deletion
as an insertion costs at most `(k-t)+t=k`.  At every later transition, the
standard fresh-event exclusion costs at most `jk<dk`.  Thus the greedy path
exists with the required second mark.

For simultaneous forward and reverse mark restrictions, forward deletion
`a_(d-2)` is reverse insertion two.  At transition `d-2`, forbidding that
deletion costs at most `(k-t)|H_-|`; all reused-label exclusions are still
below `dk`.  The two-checkpoint sufficient condition is valid.

The simplification to (3.2) uses only `t>=k/3`, `t<=k/2`, and the exact
denominator `k-t+1`.  Corollary 3.1 then follows from `d^2<=k`.

The stated scalar limitation is also exact: with `N=Theta(M/d)` selected
paths and fixed-factor cap `L_*=C N/k`, total load bounds the saturated set
only by `k/C`.  Shrinking that bound to `O(k/d)` requires a cap larger than
`L_*` by `Theta(d)`.  No stronger conclusion is smuggled into the local
escape theorem.

**Verdict: PASS.**  The theorem is a local escape result only; its explicit
warning that it does not supply a global balanced packing is necessary.
