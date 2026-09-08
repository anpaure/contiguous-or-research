# Independent audit: dense Ferrers unit-scale chain-deletion barrier

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_DENSE_FERRERS_UNIT_SCALE_CHAIN_DELETION_BARRIER_20260803.md`  
**Audited theorem SHA-256:**
`791acfa54039b58e70bd7a6ede870e74ff140e4d3b902a0dd32b8760de876f84`  
**Verdict:** **PASS**.  The two non-substantive wording/scope corrections
identified in the first audit pass have been applied to this frozen theorem.

## 1. Complement equivalence

For `k=2r`, adjoining the owner `T` to an anchored strict-lower chain
produces a chain in ranks `1,...,r`.  Complementation reverses inclusion,
fixes rank `r`, and maps those ranks exactly to `r,...,k-1`; the omission of
the empty set on the lower shore is therefore matched by the omission of
`[k]` on the upper shore.  The deleted set is carried bijectively to its
complement.

Conversely, each feasible upper chain contains exactly one middle set.
After complementing and removing that middle set, every remaining member is
a strict subset of the complemented middle owner.  Sizes fall from at most
`d+1` to at most `d`.  This proves both inequalities in
`gamma_d(k)=Gamma_d(k)` with the correct owner indexing.  No endpoint or
orientation error was found.

The scalar bound

\[
  \gamma_d(k)\ge (\Lambda-dW)_+
\]

is the immediate total-capacity bound, and the defining inequality for `d`
indeed gives `(Lambda-dW)_+ <= binom(d+1,2)`.

## 2. Fractional deletion value

The proof of

\[
  \gamma_d^*(k)=(\Lambda-dW)_+
\]

is correct.  The details checked independently are:

1. For the central choice `r=ceil(k/2)`,
   `p_s=binom(k,s)/W` lies in `[0,1]` for every `s<r`, and
   `sum_s p_s=Lambda/W`.
2. A vector `0<=q_s<=p_s` with
   `sum_s q_s=min(d,Lambda/W)` always exists.  Since `q_s<=1` and its total
   is at most `d`, it is in the independence polytope of the rank-`d`
   uniform matroid.  Hence it is the marginal vector of a random set of
   rank indices `R` of size at most `d`.
3. For each owner, initial subsets in a uniform ordering at the ranks in
   `R` form one legitimate anchored chain atom.
4. For a fixed rank-`s` target, the load identity is

   \[
   {\binom{k-s}{r-s}\over\binom r s},q_s
      ={Wq_s\over\binom k s}={q_s\over p_s}\le1.
   \]

5. Summing these target loads gives
   `W sum_s q_s=min(Lambda,dW)`, attaining the obvious atom-capacity upper
   bound.

Thus the fractional construction and its use of random-chain rank indices
are exact, not merely asymptotic.

## 3. Projection of a cyclic factor

For a fixed endpoint `j`, the literal suffix cells satisfy

\[
 Q_{j,1}\subseteq\cdots\subseteq Q_{j,d}\subseteq T_j.
\]

Although some inclusions may be equal, cells assigned to distinct named
Boolean targets necessarily give a strict subchain.  Grouping an injective
cyclic assignment by its endpoint therefore gives `W` disjoint anchored
chains, each of size at most `d`.  Deleting the `c` uncovered targets and
the disjoint boundary-assigned set `B` proves

\[
  \gamma_d(k)\le c+|B|\le c+b_\partial.
\]

The word "other" in Theorem 2.1 is needed here: it makes the `c` omissions
disjoint from `B`.  Under that stated reading, the accounting is exact.

The theorem also correctly labels this implication as one-way.  A static
chain partition does not imply the suffix cocycle or simultaneous literal
interval closure.

## 4. Boundary and asymptotic scales

The linear-versus-cyclic count of short cells is

\[
 \sum_{q=1}^d (W+d-q+1)
   =dW+\binom{d+1}{2}.
\]

Hence the noncyclic triangular boundary bank has at most
`binom(d+1,2)` cells.  Since the standard central-binomial estimate gives
`d=Theta(sqrt(k))`, this is `O(k)=o(W)`.  Therefore `c=o(W)` implies the
claimed necessary static conclusion `gamma_d(k)=o(W)`.

For even `k`,

\[
 |\mathcal U^-|=W+\Lambda=\Theta(\sqrt{k}\,W),
\]

so deletion `o(W)` is indeed relative mass `o(k^{-1/2})`.  This verifies
the stated unit-chain-scale interpretation.

## 5. Literature comparison

The primary statement of Sudakov--Tomon--Wagner, *Uniform chain
decompositions and applications*, Theorem 1.2, gives all but at most a
`k^{-1/8+o(1)}` proportion of the `W` chains length

\[
 s\bigl(1+O(k^{-1/16})\bigr),\qquad s=2^k/W=\Theta(\sqrt{k}),
\]

and Corollary 1.3 says those good chains cover a
`1-k^{-1/8+o(1)}` proportion of the lattice.  Their proof first constructs
upper-half chains and then reflects them, so the comparison with the
upper-half parameter is legitimate.

The resulting certified exceptional-element upper scale is

\[
 2^k k^{-1/8+o(1)}=Wk^{3/8+o(1)},
\]

and the additive good-chain length error is

\[
 \Theta(\sqrt{k})O(k^{-1/16})=O(k^{7/16}).
\]

Neither estimate supplies `o(W)` deletion.  The theorem note correctly
uses this only as a limitation of the published quantitative result, not as
a lower bound against a sharper future construction.

Primary source checked: B. Sudakov, I. Tomon, A. Z. Wagner, *Uniform chain
decompositions and applications*, Random Structures & Algorithms 60
(2022), 261--286, Theorem 1.2 and Corollary 1.3; arXiv:1911.09533.

## 6. Editorial corrections applied

These did not affect any proof or conclusion and are included in the
audited theorem SHA above.

1. **Parity scope in Theorem 1.2.**  The surrounding note has fixed the
   even-dimensional notation `r=k/2`, while Theorem 1.2 says "for every
   `k` (of either parity)."  The proof is valid for odd `k` after explicitly
   setting `r=ceil(k/2)`, `W=binom(k,r)`, and defining `Lambda,d` with that
   `r`.  The theorem now states this explicitly.
2. **One-sided literature estimate.**  Phrases such as "exceptional mass
   of order" may conventionally suggest a two-sided `Theta` assertion.
   The cited theorem certifies an upper exceptional scale.  The theorem
   now uses one-sided language.

The theorem is proof-safe and its main conclusion is supported:

\[
 \boxed{\text{dense named-target rounding with }o(W)\text{ leave already
 requires }\gamma_d(k)=o(W).}
\]
