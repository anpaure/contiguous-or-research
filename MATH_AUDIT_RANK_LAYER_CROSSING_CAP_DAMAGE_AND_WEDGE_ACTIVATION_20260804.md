# Audit of rank-layer crossing cap damage and wedge activation

**Date:** 2026-08-04  
**Method:** pure-mathematical replay; no computation, search, or solver  
**Audited theorem:** MATH_THEOREM_RANK_LAYER_CROSSING_CAP_DAMAGE_AND_WEDGE_ACTIVATION_20260804.md  
**Audited SHA-256:** 46eae57429e3f2939b2032b3fe44783e3a5643af6c53eb7faf53d4fd89fd33eb

## Verdict

**GO at the raw endpoint-face and bounded-layer-crossing scope.**

For \(q\) disjoint compensation paths, each visiting at most
\(\lambda_m\) owner capacities and \(\lambda_{m+1}\) q1 terminal
capacities, their union occupies at most

\[
 \lambda_mq,\qquad \lambda_{m+1}q
\]

capacities in the two respective layers.  A lower turn has exactly \(m\)
owner sides, so at least \(m-\lambda_mq\) survive.  Its unavailable terminal
count is at most the global rank-\((m+1)\) usage
\(\lambda_{m+1}q\).

Because the theorem explicitly protects lower sources and excludes
unpriced hidden capacities in its base case, these surviving endpoints are
star-active.  The inequalities

\[
 \lambda_mq\le m-p,\qquad
 \lambda_{m+1}q\le m-p-1
\]

therefore imply the sharp endpoint rows \(a_i\ge p\) and
\(t_i\le m-p-1\).

A path strictly rank-increasing on counted Boolean-capacity vertices visits
each rank at most once, so \(\lambda_m,\lambda_{m+1}\le1\).  Same-rank
private transport may be contracted only when its plateau contains no
additional counted capacity.  Thus \(q=O(\sqrt m)\) satisfies the rows for
large \(m\).

The hidden-capacity correction is sound: after terminal holes are removed,
each additional wedge whose complete active-side menu is killed costs one
unit \(h_i\), giving

\[
 |W_i^c|\ge
 B_{\max\{0,m-\lambda_mq\}}(m)-\lambda_{m+1}q-h_i.
\]

The RLE invariant restates exactly the endpoint theorem's premises,
including source survival, completion stability, and full hidden-capacity
pricing.

Finally, one compensation path may snake through arbitrarily many
rank-\(m\) vertices, so path count alone gives no layer-crossing or RLE
bound.  The theorem correctly leaves rank-monotone/bounded-crossing
selection and regeneration open.
