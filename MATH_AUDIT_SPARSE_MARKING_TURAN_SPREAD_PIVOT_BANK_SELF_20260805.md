# Self-audit of the sparse-marking Turan spread pivot bank

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_SPARSE_MARKING_TURAN_SPREAD_PIVOT_BANK_20260805.md`  
**Method:** independent symbolic replay; no computation, search, or solver  
**Verdict:** **SELF-GO** at the stated owner-only scope.

## 1. Edge count and forbidden-set loss

An `s`-uniform `Delta`-regular hypergraph on `N` vertices has exactly

\[
                         |E|={N\Delta\over s}.
\]

Deleting every edge incident with `F` deletes at most `|F|Delta` edges,
even when an edge contains several forbidden vertices.  Thus marking each
remaining edge with `q=gamma/(sDelta)` gives

\[
 \mathbb EX\ge {\gamma N\over s^2}
                  -{\gamma|F|\over s}
 ={\gamma N\over s^2}
   \left(1-{s|F|\over N}\right).
\]

The theorem explicitly assumes `s|F|/N=o(1)` and `N/s^2 -> infinity`, so
the Chernoff use is valid.

## 2. Collision ledger

Every intersecting pair of hyperedges is counted at least once by

\[
                         \sum_v{d(v)\choose2}.
\]

Pairs meeting more than one vertex are overcounted, which is safe for the
upper bound.  Hence

\[
 \mathbb EY
 \le q^2N{\Delta\choose2}
 \le {\gamma^2N\over2s^2}.
\]

Markov at threshold `(1+epsilon)` times this displayed upper bound has good
probability at least `epsilon/(1+epsilon)`.  The edge-count and simultaneous
spread events have probability `1-o(1)`, so their intersection with this
constant-probability event is nonempty.

For a graph with `X` vertices and `Y` edges,

\[
 \alpha(G)\ge\sum_x{1\over d(x)+1}
 \ge {X^2\over X+2Y}.
\]

Substitution gives exactly the coefficient

\[
 { (1-\epsilon)^2\gamma
  \over(1-\epsilon)+(1+\epsilon)\gamma}.
\]

An independent set of the intersection graph is precisely an
owner-disjoint hypergraph matching.  No codegree or fixed-uniformity theorem
is hidden in this step.

## 3. Spread tail

For one test set `A`, the weighted marked incidence count is

\[
 Z_A=\sum_e|e\cap A|\xi_e.
\]

Since each vertex of `A` lies in at most `Delta` retained edges,

\[
 \sum_e|e\cap A|\le\Delta|A|.
\]

As `|e cap A|<=s`,

\[
 \sum_e|e\cap A|^2\le s\Delta|A|.
\]

Therefore `EZ_A<=gamma|A|/s`, the variance proxy is at most `gamma|A|`,
and Bernstein at excess `epsilon gamma|A|/s` has exponent

\[
                         \Omega_{\epsilon,\gamma}(|A|/s^2).
\]

The theorem's ratio hypothesis

\[
 {L/s^2\over1+\log|\mathcal A|}\to\infty
\]

is stronger than the exact union-bound requirement and is therefore safe.
The owner union of the final matching is a subset of the marked owner union,
so the same upper bound applies after Turan selection and after taking a
submatching.

## 4. Containment-star asymptotics

For a lower set of size `a`, the rank-`r` containment star has size

\[
                         {k-a\choose r-a}.
\]

Over `a<=r-h-1` this is minimized at `a=r-h-1`, giving

\[
                         L_*={k-r+h+1\choose h+1}.
\]

When `k=2r+O(1)` and `h=Theta(sqrt r)`, elementary binomial bounds give

\[
 \log L_*=\Theta(h\log(r/h))
          =\Theta(\sqrt r\log r).
\]

Thus `L_*/s^2` is itself exponential in `Theta(sqrt r log r)` and dominates
`log(2^k)=O(r)`.  The simultaneous star union bound is valid.

## 5. Catalan constants

At the pivot-gluing depth, `s=d(k)+2` and

\[
                         {s^2\over r}\to{\pi\over4}.
\]

The limiting matching coefficient at `gamma=5` is `5/6`, strictly larger
than `pi/4`.  A sufficiently small fixed `epsilon` retains this strict
inequality, so the even target `W/(r+1)-1` is met eventually.  The odd
target `W/(2r-1)-1` requires only the limiting coefficient `pi/8` and is
also met.

## 6. Scope boundary

The proof controls only rank-`r` owner collisions and owner-containment
stars.  It does not put the `h(h+1)` natural suffix targets of a bridge into
the matching hypergraph.  Consequently it proves neither cross-bridge
suffix-deck disjointness nor compatibility with a completed named lower
forest.  It also fixes the bank before any later MLD sampling; it does not
claim that conditioning an existing MLD law preserves MLD.

Within those boundaries the theorem is exact and unconditional.
