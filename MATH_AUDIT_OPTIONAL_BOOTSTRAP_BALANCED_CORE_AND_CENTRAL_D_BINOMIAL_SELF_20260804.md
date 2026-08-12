# Self-audit: balanced Boolean core and central-`D` binomial bound

**Date:** 2026-08-04  
**Method:** line-by-line symbolic replay; no computation, search, solver, or
external result  
**Audited theorem:**
`MATH_THEOREM_OPTIONAL_BOOTSTRAP_BALANCED_CORE_AND_CENTRAL_D_BINOMIAL_20260804.md`

## Verdict

**PASS.**  The coordinate-section induction proves the exact two-parameter
minimum-degree bound, and the asymmetric peeling argument extracts the
required core from one-sided degree plus shore balance.  The strict
optional inequality `|Q|>|B^-|` buys one additional unit in the sum of the
two core degrees.  No step proves the conjectural `2D-1` bound under the
weaker one-sided hypotheses.

## 1. Section induction

Fix an incidence `A_* subset C_*` and let `x=C_*-A_*`.

* In the `x=0` section, a lower set has at most one upper neighbour across
  the split, namely `A union {x}`; an upper set has no lower neighbour in
  the `x=1` lower section.  The internal degrees are therefore at least
  `(a-1,b)`.
* In the `x=1` section, a lower set has no upper neighbour outside the
  section; an upper set has at most one lower facet across the split,
  namely the facet obtained by deleting `x`.  The internal degrees are at
  least `(a,b-1)`.

For `a,b>=2`, the first section is nonempty because `A_*` has another upper
neighbour, and the second is nonempty because `C_*` has another lower
neighbour.  Induction gives

\[
\begin{aligned}
 |A_0|&\ge\binom{a+b-2}{b-1},&
 |A_1|&\ge\binom{a+b-2}{b-2},\\
 |C_0|&\ge\binom{a+b-2}{b},&
 |C_1|&\ge\binom{a+b-2}{b-1}.
\end{aligned}
\]

Pascal's identity gives the claimed two bounds.  The `a=1` and `b=1`
base cases replay directly from one vertex on the opposite shore.

The lifted consecutive layers of an `(a+b-1)`-set have degrees `(a,b)`
and attain equality, so the two-parameter theorem is sharp.

## 2. Peeling replay

Let the two shore sizes be `n<=q` and let `e>=Dq`.  If iterative deletion
at thresholds `(a,b)` with `a+b=D+1` erased the entire graph, charging an
edge at the first deletion of an endpoint would give

\[
 e\le(a-1)n+(b-1)q\le(D-1)q,
\]

a contradiction.  Thus a nonempty `(a,b)` core survives.  Choosing
`b-1=floor(D/2)` and applying the section theorem gives

\[
 |B|\ge\binom D{\lfloor D/2\rfloor}.
\]

If `q>n`, choose `a+b=D+2` with `a>=2`.  Complete deletion would instead
give

\[
\begin{aligned}
 e&\le(a-1)n+(b-1)q\\
  &=Dq-(a-1)(q-n)<Dq,
\end{aligned}
\]

again impossible.  Balancing `b-1` yields

\[
 |B|\ge\binom{D+1}{\lfloor(D+1)/2\rfloor}.
\]

The strictness and the condition `a>=2` are both load-bearing.  With only
`q>=n`, the last strict inequality is unavailable.

## 3. Optional specialization

The wide-gap theorem supplies exactly

\[
 D=d-3,qquad |Q|\ge|B^-|+1,qquad d_{B^-}(U)\ge D.
\]

Therefore the strict peeling corollary applies and gives

\[
 |B^-|\ge
 \binom{d-2}{\lfloor(d-2)/2\rfloor}.
\]

Since `d=Theta(sqrt m)`, this is `2^{Omega(sqrt m)}` and improves the
previous `2^(d-3)/O(d)` by a polynomial factor.

## 4. Sharp-candidate boundary

If both shores had minimum degree `D`, the section theorem with `a=b=D`
would prove

\[
 |B|\ge\binom{2D-1}{D-1}.
\]

The actual assumptions provide right minimum degree `D` and left average
degree at least `D`; the peeling theorem guarantees only a core with degree
sum `D+1`, or `D+2` under strict side imbalance.  No average-to-minimum
upgrade to `(D,D)` is made.  Abstract affine-plane systems show that a
purely graph-theoretic upgrade is impossible, although their failure of
Boolean literal-union rigidity leaves the Boolean threshold-shadow question
open.
