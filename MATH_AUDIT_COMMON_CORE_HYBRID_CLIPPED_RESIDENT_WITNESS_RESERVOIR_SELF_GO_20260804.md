# Self-audit: hybrid clipped-resident common-core reservoir

**Date:** 2026-08-04  
**Verdict:** `GO_SELF`.  The construction and every asymptotic estimate
were independently replayed from the set definitions.  No search,
sampling, or finite enumeration is used.

## 1. Audited theorem

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `1e0a55e6e86e1c557aecc97c78e277fba027ea9ca4768c6f835eee42bd7d345b` |

## 2. Exhaustion of traces

Every damage trace has size at least two and is proper.  Cyclic intervals
are handled by the existing top paths.  A noninterval trace is assigned to
exactly one of:

* the harmless two-owner case `q=2`;
* the low range `3<=q<=m-d-1`;
* the high range `q>=m-d`.

Thus there is no missing integer size between the low and high banks.

## 3. Low-path replay

For `h=m-q`, the final window endpoint is

\[
 (q-1)+(h-1)=m-2=|K|-1,
\]

so the windows in the theorem do not wrap.  Every owner has size
`q+h=m`, consecutive owners exchange exactly one `K`-coordinate, and the
lower and upper ranks are `m-1` and `m+1`.

The union of the `q` windows has length

\[
 h+q-1=m-1=|K|,
\]

so the path union is the required target.  A coordinate `k_s` occurs for
indices

\[
 [s-h+1,s]\cap[0,q-1].
\]

If this run is internal, neither truncation is active and its length is
exactly `h=m-q>=d+1`.  This proves the clipped-residence row.  Exact
external trace distinguishes different private paths and separates them
from the cyclic-interval top paths in all three resource ranks.

## 4. High-geodesic replay

For `q=m-h`,

\[
 |Z|=2m-h-1,
 \qquad |C|=h+1,
 \qquad |X|=|Y|=q-1
\]

is an exact partition because

\[
 h+1+2(q-1)=2m-h-1.
\]

Every displayed owner has rank

\[
 h+1+(q-1-t)+t=m.
\]

The path length is `q-1`, exactly the Johnson distance between its
endpoints, and the endpoint union is all of `Z`.  Core coordinates are
constant; `X` coordinates occur only in initial runs and `Y` coordinates
only in terminal runs.  Hence no internal positive run exists.

The owner at time `t` has exactly `t` `Y`-coordinates.  Lower and upper
colours on edge `t` have respectively `t` and `t+1` `Y`-coordinates.
Thus all three resource lists are simple.  Full coordinate symmetry makes
each position uniform in its corresponding rank, proving the exact hit
probabilities

\[
 q/{N\choose m},
 \qquad (q-1)/{N\choose m-1},
 \qquad (q-1)/{N\choose m+1}.
\]

## 5. Entropy and union-bound replay

For `p=r/N`, the integer `r` is a binomial mode because

\[
 (N+1)p=r+r/N\in(r,r+1).
\]

Hence its probability is at least `1/(N+1)`, giving the type lower bound.
For `r in {m-1,m,m+1}`,

\[
 \left|{r\over N}-{1\over2}\right|
 \le {h+3\over2N}.
\]

The elementary relative-entropy bound on `|t|<=1/4` gives the stated
uniform estimate

\[
 B_m\ge{1\over2m}
 2^{2m-d-1-3(d+3)^2/(2(2m-d-1))}
 =2^{2m-o(m)}.
\]

Also

\[
 H_d\le(d+1)(em/d)^d=2^{o(m)}
\]

for `d=O(sqrt m)`.  Before any greedy step, each forbidden resource bank
has size at most `4m(2^m+H_d)`.  Therefore the failure probability is at
most

\[
 {12m^2(2^m+H_d)\over B_m}=2^{-m+o(m)}<1.
\]

The estimate is uniform over the current target and all previous choices,
so sequential conditioning is legitimate: the probabilistic method is
reapplied at each deterministic greedy step.

## 6. Scope

The conclusion is a pairwise owner/lower/upper-disjoint, internally
clipped-resident witness reservoir.  Endpoint collars, global cyclic
residence, weighted Ore--Ryser extension, component placement, and the
common cap are not inferred.

**Final self-audit verdict:** `GO_SELF`.
