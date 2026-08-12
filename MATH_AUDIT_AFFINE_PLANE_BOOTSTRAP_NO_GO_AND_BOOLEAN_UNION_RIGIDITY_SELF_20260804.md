# Self-audit: affine-plane bootstrap no-go and Boolean union rigidity

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_AFFINE_PLANE_BOOTSTRAP_NO_GO_AND_BOOLEAN_UNION_RIGIDITY_20260804.md`

No computation or search is used.

## 1. Affine parameters and strict Hall

`AG(2,q)` has `q^2` points, `q(q+1)` lines, point degree `q+1`, line
degree `q`, and one line through each point pair.  Thus its incidence graph
is `C_4`-free.

For `0<=t<=q`, `min(2,t)>=2t/q`.  Summing line intersections of `D`
counts each point `q+1` times and gives

\[
 \sum_\ell\min(2,|D\cap\ell|)
 \ge2(q+1)|D|/q>2|D|.
\]

The strict margin is an integer.  Reducing any one line capacity by one
therefore leaves non-strict Hall.  Bipartite integrality justifies the
matching and robustness conclusions.

At the full bank, each of `q(q+1)` lines contributes two, while the modular
cost is `2q^2`, giving `Psi(B)=2q`.  The same strict-Hall expression is
exactly the objective lost after deleting any nonempty `D`; hence every
proper subset has smaller objective.  The unique-maximizer claim is valid
because the abstract ground set consists only of these `q^2` points.

## 2. Johnson nonembedding

Any two affine points share a line.  Under a containment embedding, their
two distinct rank-`m-1` images therefore have union rank `m` and are
Johnson adjacent.  Hence all point images form a Johnson clique.

The standard clique classification has two cases.  In a top clique, every
pair union is the same rank-`m` owner, so distinct affine lines cannot have
distinct owner images.  In a star clique, an owner contains at most two
members, contradicting line size `q>=3`.  Thus the nonembedding proof uses
the injection of line vertices and is exact.

## 3. Scope

The theorem disproves sufficiency of the abstract local bootstrap package.
It does not construct a positive obstruction in the actual Boolean
middle-level graph and does not disprove factor extension for the protected
reservoir.  On the contrary, it identifies literal-union/Johnson-clique
rigidity as the additional property a closing theorem must use.

**Self-audit verdict:** GO.
