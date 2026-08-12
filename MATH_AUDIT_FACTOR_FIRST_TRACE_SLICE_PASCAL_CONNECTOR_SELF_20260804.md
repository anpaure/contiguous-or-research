# Self-audit: factor-first trace slices and Pascal endpoint connector

**Date:** 2026-08-04  
**Status:** proof audit of
`MATH_THEOREM_FACTOR_FIRST_TRACE_SLICE_PASCAL_CONNECTOR_REDUCTION_20260804.md`.
No computation or finite search was used.

## 1. Coordinate dictionary

For an owner `u(A,T)`,

\[
 |u(A,T)|=(m-1-|A|)+|T|=m
\]

exactly when `|T|=|A|+1`.  For a lower vertex `ell(B,S)`,

\[
 |\ell(B,S)|=(m-1-|B|)+|S|=m-1
\]

exactly when `|S|=|B|`.  Adding a coordinate changes either
`B=A+a,T=S` or `A=B,T=S+e`; there is no third case.  PASS.

## 2. Slice and global counts

For one trace of size `q`, owner and same-trace lower counts are

\[
 v_q=\binom{m-1}{q-1},\qquad l_q=\binom{m-1}q.
\]

A `b_T`-component forest uses `v_q-b_T` distinct lower labels, leaving
`r_T=l_q-v_q+b_T`.  Hence `r_T-b_T=l_q-v_q`.

Writing `a_q=binom(m-1,q)`, Pascal gives

\[
 \binom mq(l_q-v_q)
 =(a_q+a_{q-1})(a_q-a_{q-1})
 =a_q^2-a_{q-1}^2.
\]

This includes the boundary slices `q=0` and `q=m`: their differences are
`+1` and `-1`, so the global sum is zero.  PASS.

## 3. Endpoint completion

Every forest edge consumes one lower vertex twice.  Every internal owner
has degree two.  The residual demands are one at each ordinary path
endpoint, two at each singleton, and two at every unused lower vertex.
Because the numbers of components and residual lowers agree, total demand
also agrees.  A physical full matching is therefore necessary and
sufficient.  Suppression preserves connectivity and cycle count.  PASS.

## 4. Saturating-block cases

If `v_q<=l_q`, the smaller shore is the owner shore.  Deleting one
projected edge from the saturating cycle gives one path on all owners,
with `v_q-1` labels.  Counts: `b=1`, `r=l-v+1`.

If `v_q>l_q`, the smaller shore is the label shore.  The saturating cycle
uses every label and `l_q` owners.  Any outside owner has at least one
incident label.  Replacing one cycle incidence at that label by the
outside-owner incidence opens the cycle into a path with all `l_q` labels
and `l_q+1` owners.  The remaining owners are singletons.  Counts:

\[
 b=1+v-(l+1)=v-l,\qquad r=0.
\]

The replacement cannot collide with a cycle owner because the chosen
owner was outside the cycle.  PASS.

For the union claim in the first case, all `(q-1)`-sets occur and have
empty total intersection.  In the second case, for every `x in K` choose
a visited `q`-label omitting `x`; an incident owner index also omits `x`,
so its complementary actual owner contains `x`.  The restriction
`q<=m-2=|K|-1` is exactly what permits that label.  PASS.

## 5. Sharp exceptional slice

At `q=m-1`, owner indices are co-singletons of `K`, so actual owner
`K`-parts are singletons.  The unique same-trace lower label is `K` and can
join only two owners.  Thus a same-trace component covers at most two
`K` coordinates.  For `m>=4`, this is strictly smaller than `|K|=m-1`.
PASS.

## 6. Ring dictionary

Substitution gives

\[
 u(\varnothing,\{a_i\})=K+a_i=L_i,
\]

\[
 \ell(\{b\},\{a_i\})=(K-b)+a_i=I_i,
\]

and the two E-step children are exactly

\[
 (K-b)+a_{i-1}+a_i=R_i,
 \quad (K-b)+a_i+a_{i+1}=R_{i+1}.
\]

Thus the rethread changes one eligible child at the same connector and no
slice edge.  PASS.

## 7. Scope checks

The theorem does **not** assert:

1. that the endpoint connector has the required matching or cycle
   partition;
2. that arbitrary prescribed endpoint pairs lie on the saturating blocks;
3. global or clipped residence of the large slice blocks;
4. compatibility with one common cap;
5. that the pre-rethread factor is Hamiltonian or that the hinges already
   lie on the required distinct components.

The random-measure lemma assumes a sequential **lower** conditional bound;
it does not infer one from an ordinary upper-spread hypothesis.  PASS.

## 8. Verdict

The coordinate reduction, count identities, slice-witness construction,
co-singleton obstruction, ring interpretation, and conditional
probability lemma are internally proved.  The Pascal endpoint-cycle
theorem is correctly left open.  **SELF-GO within stated scope.**

