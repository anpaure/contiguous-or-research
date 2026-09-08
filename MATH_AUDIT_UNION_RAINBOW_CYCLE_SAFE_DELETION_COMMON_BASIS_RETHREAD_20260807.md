# Audit of the union-rainbow safe-deletion common-basis reduction

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_UNION_RAINBOW_CYCLE_SAFE_DELETION_COMMON_BASIS_RETHREAD_20260807.md`  
**Method:** exact parameter, Kruskal--Katona, matroid, and endpoint-colour
audit; no finite search  
**Verdict:** `GO`, with the protected-minor capacity correction recorded in
Section 5 below.

## 1. Layer counts and safe rank

For `|Omega|=2m`, put

\[
 W={2m\choose m},\qquad C={W\over m+1},\qquad
 V={2m\choose m-1}=mC.
\]

Also

\[
 \left|{\Omega\choose m-2}\right|
 ={m(m-1)\over m+2}C.
\]

Hence the partition-matroid rank is

\[
 V-\left|{\Omega\choose m-2}\right|
 ={3m\over m+2}C>C\qquad(m>1),
\]

as claimed.  The Gregor--Micka--Mütze optimal cycle through the smaller
shore `binom(Omega,m-1)` visits `V` distinct rank-`m` vertices; suppressing
that shore therefore gives a Hamilton cycle with pairwise-distinct edge
unions.  No further Hamilton claim is used.

## 2. Kruskal--Katona endpoint Hall

Let `O` be the `C` omitted rank-`m` sets.  For every nonempty
`F subseteq O`, write `|F|=binom(x,m)` in the Lovasz real-binomial
parameterization.  Since

\[
 |F|\le C={1\over m+1}{2m\choose m}
      <{2m-1\choose m}qquad(m>1),
\]

one has `x<2m-1`.  Lovasz--Kruskal--Katona gives

\[
 |\partial F|\ge{x\choose m-1}
 ={m\over x-m+1}{x\choose m}>|F|.
\]

Thus `O` has a containment matching into distinct rank-`(m-1)` facets.
Orienting the Hamilton cycle and sending every selected facet to its
outgoing edge is injective.  Composing the two maps gives distinct cycle
edges incident with the corresponding omitted sets.  Therefore the
endpoint transversal matroid has rank exactly `C`.  Lemma 3.1 is correct.

## 3. Common-basis and capacitated-Hall forms

The desired deletion set is a common independent set of size `C` in:

* the partition matroid with colour capacities `mu_a-1`; and
* the endpoint transversal matroid.

Edmonds' min--max therefore gives the displayed two-matroid inequality.
The network

\[
 \mathcal O\longrightarrow E(K)\longrightarrow\mathcal A
 \longrightarrow t
\]

has unit capacities through each edge-node and final capacity `mu_a-1` at
colour `a`.  Its Hall cut for `X subseteq O` is exactly

\[
 \sum_a\min(\mu_a-1,|N_K(X)\cap E_a|)\ge|X|.
\]

Thus Corollary 3.3 neither loses nor adds a constraint.

## 4. Endpoint-colour partition after deletion

Union rainbowness partitions the rank-`m` colours as

\[
 \mathcal U
 =\mathcal O\mathbin{\dot\cup}q(D)
  \mathbin{\dot\cup}q(E(K)\setminus D).
\]

After complementation:

* `q(E(K)\D)` supplies all internal rank-`m` colours;
* `O` supplies one endpoint colour for every deleted edge through the
  transversal matching; and
* `q(D)` supplies the other endpoint colour of every deleted edge.

If `p(e) subset eta(e)`, then `bar(eta(e)) subset bar(p(e))`; and
`bar(q(e))` lies in the complement of either endpoint of `e`.  The three
families are disjoint and have total size `W`, so they assign every lower
vertex exactly once.

Adjacent deleted cycle edges merely create two endpoint occurrences at one
isolated owner.  They still receive different colours because `eta` and
`q` are injective and their images lie in disjoint palettes.  Hence the
literal incidence forest in Section 4 is correct.

## 5. Protected-minor correction

If a prescribed edge set `P` must survive, the deletion ground set is

\[
                         E'=E(K)\setminus P.
\]

Both matroids must be restricted to `E'`.  For colour `a`, write
`n_a=|E'\cap E_a|`.  Its deletion capacity in the restricted network is

\[
                         c_a=\min(\mu_a-1,n_a).
\]

Therefore the protected capacitated-Hall condition is

\[
 \boxed{
 \sum_a\min(c_a,|N_K(\mathcal X)\cap E'\cap E_a|)
 \ge|\mathcal X|\quad(\mathcal X\subseteq\mathcal O).}
\]

Equivalently one may keep the original capacity `mu_a-1`, since the
available-edge count already truncates it; the explicit `c_a` form prevents
mistaking protected occurrences for deletable ones.  If all occurrences of
a colour are protected, its restricted capacity is zero.

With this correction understood, the protected-segment statement is an
exact matroid-minor specialization.  The source makes no claim that the
protected inequality is automatic, so no theorem correction is required.

## 6. Scope

The reduction is conditional on an intersection-surjective union-rainbow
cycle and on the common-basis inequality.  It proves neither condition,
the exterior common-endpoint forest, residence, deeper upper coverage, nor
the literal compiler.  Within that scope, all stated implications audit
correctly.

