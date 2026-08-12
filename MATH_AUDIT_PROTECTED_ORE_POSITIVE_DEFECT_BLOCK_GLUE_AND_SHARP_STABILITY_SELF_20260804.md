# Self-audit: protected Ore positive-defect block gluing and sharp stability

**Date:** 2026-08-04  
**Verdict:** **SELF-GO** for the exact metric bounds, counterexamples,
block-gluing identity, and the stated positive-defect reservoir corollary.
The result closes only complete-support block unions and their certified
Hamming neighbourhoods.  It does not close arbitrary positive-defect cuts.

No computation, search, or solver result is used.

## 1. Audited artifact

`MATH_THEOREM_PROTECTED_ORE_POSITIVE_DEFECT_BLOCK_GLUE_AND_SHARP_STABILITY_20260804.md`

SHA-256:
`b414ed2dea6a3cc7365a054cbea7e664069ae5c9d84e1bdff1c80d79e6ae0980`.
This self-audit must not be described as an independent audit.

## 2. Metric upper bound

The two equality families `emptyset` and `mathcal L` give

\[
 d_{\mathfrak E}(A)\le t:=\min(|A|,W-|A|).
\]

The frozen inequalities give

\[
 \sigma(A)\ge {2(2m-1)\over m(m-1)}{t(W-t)\over W}
 \ge {2m-1\over m(m-1)}t.
\]

Therefore the coefficient in Theorem 1.1 is exact as derived.  No
unstated stability theorem is used.

## 3. Principal-star lower bound

Put `k=m-1`.  For a zero-defect support block containing the distinguished
coordinate, let `r=|S|-1` and `x=r-k+2`.  Directly,

\[
\begin{aligned}
 g(S)
 &=2{r\choose k-1}-{r+1\choose k}\\
 &={2k-r-1\over k}{r\choose k-1}\\
 &={x(k+1-x)\over k(k-1)}{r\choose k-2}.
\end{aligned}
\]

Supports in a zero-defect family intersect in at most `k-2`; after deleting
the common distinguished coordinate, their intersections have size at
most `k-3`.  Hence the `(k-2)`-shadows used in the proof are genuinely
disjoint.  Finally,

\[
 {{2k\choose k-2}\over{2k\choose k-1}}={k-1\over k+2},
\]

which yields exactly the coefficient

\[
 {(k+1)^2\over4k(k+2)}.
\]

The principal-star slack `2M/k` is the frozen exact formula.  Thus the
ratio is `Omega(m)`, matching the universal `O(m)` bound in order.

## 4. Two-block counterexample

The supports have intersection `H` of size `k-1` and disjoint external
parts of size `p`.  The only fibres of size between two and `m-1` are

\[
 H\cup\{x,y\},\qquad x\in P_0, y\in Q_0,
\]

and every one has exactly two selected facets.  Hence
`b=(m-2)p^2`.

For the packing step, if no equality support contains a fixed
`z=k-1+p` element set `Z`, then every intersection `Q_i` has size at most
`z-1`, and

\[
 { |Q_i|\choose k}
 ={ |Q_i|-k+1\over k}{ |Q_i|\choose k-1}
 \le {z-k\over k}{ |Q_i|\choose k-1}.
\]

The `(k-1)`-shadows are disjoint, so their sum is at most
`{z choose k-1}`.  The missing fraction is exactly `1/p`.

If an equality family is closer than `B/p`, one support contains each of
`S,T`.  Distinct supports are impossible because `|S cap T|=k-1`; one
common support must be all of `Omega`, making the equality family the full
shore.  The last product ratio has every factor at least
`(2m-1)/m`, so the displayed strict inequality holds already for odd
`m>=5`.  The exponential-versus-polynomial conclusion is therefore
proof-safe.

## 5. Local gluing table

At a cross owner, let `q=a_U`, `d=d_P(U)`, and let `t` be the number of
protected selected facets.  The complete local table is

| `d` | union `lambda` | sum of block `lambda` | union `sigma` minus block sum | margin loss `psi` |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | `2-q` | `q-2` |
| 1 | `1-t` | 0 | `2-q` | `q-1-t` |
| 2 | `2-t` | `q-t` | `2-q` | 0 |

This table proves (3.4)--(3.5) exactly.  In particular, degree-two cross
owners have zero gluing penalty; this is not an inequality or a heuristic.

For two support blocks meeting in `k-1` points, every cross owner has
`q=2`.  The only positive row is therefore `d=1,t=0`, so the total penalty
is at most the number `pq` of cross owners.  Their clique defect is exactly
`(m-2)pq`.

## 6. Reservoir and Hamming scope

The frozen constrained-reservoir theorem supplies the one-support lower
margins (4.1)--(4.2) and the exact `(2m+2)` Hamming Lipschitz constant.
Substitution in the exact two-block identity gives Theorem 4.1 without
any independence or probabilistic assumption.

For `|S|=|T|=m`, one has `p=q=2`, `u=m-1`, and
`{m choose m-1}=m`, yielding exactly (4.5).  Since
`R_m=ceil(6m/log m)+2=o(m)`, the radius in (4.6) is positive and
`Theta(m)` for all sufficiently large `m`.

For the singleton specialization, every nonexceptional singleton has
margin at least

\[
 (m-2)-(R_m+4)=m-R_m-6=D_m,
\]

and every exceptional singleton has nonnegative margin by the exact
common-`G_2` theorem.  Applying the same local gluing table to singleton
blocks proves (4.9)--(4.10).

If there are no full owners and `2<=a_U<=r_0` on every partial owner, then
`ψ_U<=a_U-1<=r_0-1`, while its contribution to `b` is
`m-a_U>=m-r_0`.  Summing gives the coefficient in (4.11).  At `r_0=2`,
every partial owner contributes exactly `m-2` to `b` and at most one to
the singleton gluing penalty, proving (4.12).  The incidence bound
`2n_2<=m|A|` proves the density corollary (4.13).

## 7. Fail-closed scope

The theorem does **not** assert:

1. that every positive-defect cut is close to a complete-block union;
2. that `b` controls Hamming distance;
3. that block gluing controls facets outside the extracted blocks;
4. protected-factor component placement; or
5. endpoint-collar or common-cap compatibility.

The exact remaining object is the non-block erosion residual stated in
Section 5 of the theorem.
