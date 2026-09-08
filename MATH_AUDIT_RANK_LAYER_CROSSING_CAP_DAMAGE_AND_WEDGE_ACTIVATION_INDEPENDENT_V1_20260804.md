# Independent audit of rank-layer crossing cap damage and wedge activation

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited theorem:** `MATH_THEOREM_RANK_LAYER_CROSSING_CAP_DAMAGE_AND_WEDGE_ACTIVATION_20260804.md`  
**Audited theorem SHA-256:** `46eae57429e3f2939b2032b3fe44783e3a5643af6c53eb7faf53d4fd89fd33eb`  
**Author audit SHA-256:** `e1882e2792d28c4420ee681dbb5e7fec9a079c17ba116cab793153f3d573c98b`

## Verdict

**GO at the theorem's stated raw-endpoint-face and bounded-layer-crossing
scope.**  The final version correctly repairs the two scope points raised
during audit: it clamps the lower owner count before evaluating the wedge
polynomial, and it requires strict rank increase on counted capacities (not
merely a nondecreasing ambient-rank path).

## Independent replay

### 1. Endpoint counts

The compensation linkage contains (q) vertex-disjoint paths and each path
uses at most \(\lambda_m\) counted owner capacities and
\(\lambda_{m+1}\) counted q1-terminal capacities.  Its complete union
therefore occupies at most

\[
  \lambda_m q\quad\hbox{and}\quad \lambda_{m+1}q
\]

distinct capacities in those two layers.  Since a fixed lower turn has
exactly (m) owner neighbours, at least (m-\lambda_mq) owner sides
survive.  The global terminal count is also a valid (possibly loose) upper
bound on the unavailable terminal values in any one source's menu.

The raw-face assumptions are essential and are stated: sources survive,
all direct branches are present and typed, distinct Boolean values use
distinct selected capacities, and unpriced branch-local resources are
avoided.  Thus a surviving owner/terminal pair is genuinely star-active,
not merely present in a projected graph.  The rows

\[
 \lambda_mq\le m-p,
 \qquad
 \lambda_{m+1}q\le m-p-1
\]

give exactly (a_i\ge p) and (t_i\le m-p-1), so the cited endpoint-only
active-wedge theorem applies.

### 2. Rank-layer specialization

If the counted capacity vertices along a path have strictly increasing
Boolean rank, that path visits each counted rank at most once.  Hence
\(\lambda_m,\lambda_{m+1}\le1\).  Contracting same-rank transport is sound
only when the contracted plateau contains no counted owner or q1-terminal
capacity; the theorem now says this explicitly.  Plain rank
nondecrease would not imply the conclusion.

### 3. Hidden-capacity losses

Let (h_i) count supported wedge terminals whose entire active branch menu
is killed by hidden deletions.  Removing terminal holes and then those
fully killed wedge values gives the safe lower bound

\[
 |W_i^c|\ge B_{a_i}(m)-t_i-h_i.
\]

Since a real owner count cannot be negative, monotonicity of (B_a(m))
must be used with

\[
 \bar a=\max\{0,m-\lambda_mq\};
\]

the final theorem does so.  If a hidden resource kills many terminal
values, its charge is the number of killed values, not one unit per path.
Possible overlap between the (t_i) and (h_i) books can only make the
displayed subtraction more conservative.

### 4. Regenerative invariant and obstruction

`RLE(p)` restates the exact local hypotheses required by the endpoint
theorem: source survival, at least (p) simultaneous active owner sides,
at most (m-p-1) unavailable supported terminal values after all hidden
losses, and completion-stable value-faithful occurrence maps.  It therefore
implies one zero-defect protected-wedge router.

The theorem does **not** derive `RLE(p)` from path count alone.  One path
may snake through arbitrarily many same-rank counted capacities, so (q=1)
does not bound either layer footprint.  The remaining all-dimensional
premise is correctly left as bounded-crossing/rank-monotone linkage
selection or direct residual full-port expansion.

## Scope boundary

This theorem is an exact implication from a raw typed endpoint face and a
bounded complete compensation footprint.  It does not construct that face,
prove a rank-monotone compensation linkage for the present parent, or prove
regeneration across Pascal lifts.  No all-(k) upper bound follows from this
lemma alone.
