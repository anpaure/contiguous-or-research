# Independent proof audit: endpoint-triangular bounded chains

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_ENDPOINT_TRIANGULAR_BOUNDED_CHAIN_FRACTIONAL_EXACTNESS_20260804.md`

## Verdict

**PASS**, with the scope stated in the theorem.

The endpoint capacity vector, all max-flow cuts, the uniform-cap fractional
minimum, and the perfect-graph integrality-gap example are independently
rederived below.  No computation or finite search is used.

## 1. Endpoint capacities

At right endpoint `j`, a strict-lower witness can use only interval lengths

\[
 1,\ldots,\min(h,j).
\]

Distinct values at fixed endpoint are nested, so the chain capacity is
`c_j=min(h,j)`.  For `n=W+h`, sorting gives

\[
 h^{W+1},h-1,h-2,\ldots,1.
\]

The total is

\[
 h(W+1)+1+\cdots+(h-1)=hW+{h+1\choose2}.
\]

This confirms equations (0.3)--(0.4) and the clipped-vacancy correction.

## 2. Capacity norms and Boolean cuts

For `1<=t<=h`,

\[
 \begin{aligned}
 \sum_j\min(t,c_j)
 &=t(W+1)+\sum_{a=1}^{h-1}\min(t,a)\\
 &=t(W+1)+{t(t-1)\over2}+t(h-t)\\
 &=t(W+h)-{t\choose2}.
 \end{aligned}
\]

The maximum `t`-antichain union in the strict Boolean lower ideal is the
union of its `t` largest ranks.  Each has size at most `W`; hence its size
is at most `tW`, strictly below the displayed capacity norm.  For `t>=h`,
the norm is total capacity and (0.1), together with `h>=d`, proves the total
cut.  Thus no Greene--Kleitman cut was omitted.

## 3. Uniform fractional optimum

Any fractional bounded-chain cover of total mass `q` has `q>=binom(k,s)`
for every rank `s`, and `hq>=Lambda`.  These are the two lower bounds in
(0.5).

For their maximum `q`, the vector

\[
 p_s={\binom{k}{s}\over q}
\]

lies in the uniform-matroid independence polytope because each coordinate
is at most one and its total is at most `h`.  Decomposing it into rank
patterns and applying a uniform permutation flag gives any fixed rank-`s`
target mass

\[
 q p_s/\binom{k}{s}=1.
\]

Thus both inequalities are sharp and (0.5) is exact.

At `h=d`, substituting

\[
 \Lambda=dW+{d+1\choose2}-\sigma
\]

gives `Lambda/d=W+(d+1)/2-sigma/d`; since the largest strict-lower rank is
at most `W`, the fractional reserve is at least `(d-1)/2`.  The theorem
correctly treats this as chain-mass slack, not an integral partition.

## 4. Labelled triangular fractional factor

The rank-slot transportation graph has one edge between every rank and
slot, with edge capacity one, rank demand `binom(k,s)`, and slot capacity
`c_j`.  The max-flow cut for a rank family `R` is exactly

\[
 \sum_{s\in R}{k\choose s}\le\sum_j\min(c_j,|R|).
\]

For fixed `|R|`, the left side is largest on the top ranks, already checked
in Section 2.  Hence the transportation matrix exists.  Each slot row lies
in a uniform-matroid polytope, and uniform flags turn its pattern
decomposition into named-target mass.  This independently confirms
Theorem 4.1.

## 5. Integral-gap example

For `P_(n,h)`, cross-component incomparability forces every bounded chain
to remain inside one component.  The integral count is therefore

\[
 (n-3)+2\left\lceil{h+1\over h}\right\rceil=n+1.
\]

For one long component, the `h+1` subchains obtained by deleting one point,
each weighted `1/h`, cover every point once with mass `(h+1)/h`.  Two such
components use mass `2+2/h<=3`; the remaining `n-3` slots host the singleton
components.  Since `n-h+1>=3`, three full slots are available.

The antichain-union formula

\[
 a_t=n-3+2\min(t,h+1)
\]

is exact.  Substitution verifies all triangular capacity norms, and total
capacity dominates `n+2h-1` for `n>=h+2`.  The incomparability graph is
complete multipartite, hence perfect.  This confirms that the failure is a
cardinality-bounded coloring gap, not ordinary chromatic nonintegrality.

## 6. Scope audit

The theorem proves neither (6.2) nor any OR-word upper bound.  In
particular:

* fractional slot mixtures may reuse no target in expectation while every
  literal choice still collides;
* endpoint chains are not matched to distinct middle owners;
* no left-endpoint chains or shared source-letter countdown is supplied;
* no upper, residence, topology, or common-cap condition is addressed.

The final implication chain is therefore proof-safe.

