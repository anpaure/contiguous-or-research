# Independent audit: architecture-free endpoint chains and unit-scale vacancy

**Date:** 2026-08-03  
**Audited source:**
`MATH_THEOREM_ARCHITECTURE_FREE_ENDPOINT_CHAIN_UNIT_SLACK_20260803.md`  
**Source SHA-256:**
`bcf51c38498b65d02d7c4a8ab2cb784155df24b6a6e7fbf7c6869c2b4962290b`

## Verdict

**GO.**  The theorem and its stated scope are correct.  No mathematical
correction is required.

## Checks

### 1. Noncontainment and endpoint order

Two selected intervals representing distinct rank-`r` targets cannot contain
one another: containment of intervals implies containment of their OR values,
whereas two distinct sets of the same rank are incomparable.  Equal left
endpoints would therefore force containment, so the left endpoints are
distinct.  After sorting by left endpoint, a nonincreasing pair of right
endpoints would again force containment.  Hence both endpoint sequences are
strictly increasing.

For a strictly increasing `W`-tuple in `[W+e]`, its `t`-th entry lies in
`[t,t+e]`.  Thus equation (1.1) is exact for both endpoint sequences.

### 2. Long-window lemma

If `J=[a,b]` has length at least `e+1`, then `b>=a+e`.  Since
`b<=W+e`, this forces `a<=W`, so the selected middle interval indexed by
`t=a` exists.  Equation (1.1) gives

\[
 a\le a_a\le b_a\le a+e\le b,
\]

and therefore `I_a` is contained in `J`.  The conclusion that every such
window has OR-rank at least `r` follows immediately.

### 3. Literal endpoint-chain partition

Every strict-lower witness interval has length at most `e`.  At a fixed right
endpoint, its possible starts are the at most `e` clipped positions
`j-e+1,...,j`; their OR values are nested as the start moves left.  Choosing
one witness per named lower target therefore gives a genuine partition into
`n` possibly empty inclusion chains, each of cardinality at most `e`, and
each represented literally at its named endpoint.

### 4. Vacancy inequalities

With `e=d+C`, the available endpoint slots are exactly

\[
 e(W+e)=(d+C)(W+d+C),
\]

so equation (0.2) is correct.  The defining inequality for `d` gives

\[
 dW-\Lambda\ge-{d+1\choose2},
\]

and minimality at `d-1` gives, for `d>=1`,

\[
 dW-\Lambda<W-{d\choose2}.
\]

The `d=0` case satisfies the displayed bounds directly.  Substitution into
(0.2) yields

\[
 0\le V_C<(C+1)W+O_C(d^2)=(C+1)W+O_C(k),
\]

and division by `W+d+C` gives (0.5) for fixed integer `C>=0`.

### 5. Scope

The theorem is purely necessary and static.  Its explicit exclusions of
owner anchoring, a common sliding suffix cocycle, residence, upper coverage,
topology, common cap, and regeneration are all necessary.  In particular,
the result does not furnish an upper construction or imply
`nu(k)<=B(k)+O(1)`.

