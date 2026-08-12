# Independent audit of the fixed-head trace-tree criterion

**Date:** 2026-08-02  
**Verdict:** PASS, with the scope qualifications recorded below.

## 1. Balance reduction

For a fixed owner-labelled marked suffix table, role \(i\) has fixed head

\[
                         h_i=(A_{i,1},\ldots,A_{i,d})
\]

and legal leading letters

\[
 \varnothing\ne B\subseteq T_i,\qquad
 T_i\setminus U_i\subseteq B,\quad U_i=\bigcup_tA_{i,t}.
\]

Therefore every option has the same owner \(T_i\) and the same proper
suffix payload. If \(a(v)\) is the multiplicity of \(v\) among the fixed
heads, selected indegree at \(v\) is always \(a(v)\). Balance is exactly
the equation

\[
                         \#\{\text{selected tails }v\}=a(v).
\]

Thus the role-to-tail capacitated Hall system in Theorem 2.1 is exact and
its matrix is bipartite/TU. Tail states with \(a(v)=0\) must be deleted;
allowing them as positive-capacity sinks would be a false relaxation.

## 2. Connected criterion

Necessity of Theorem 3.1 follows by taking a weak spanning tree from any
connected balanced selected support. Its edges use distinct selected
roles and at most the available tail multiplicities. Removing them leaves
the actual residual selection, which witnesses Hall with exact demands
\(a-b_R\).

For sufficiency, the residual Hall matching fills every demand
\(a-b_R\). Adding the skeleton gives tail multiplicity \(a\), hence exact
balance, and its projected tree forces weak connectedness. A balanced
weakly connected finite digraph is Eulerian.

The following details are essential and are correctly stated in the
theorem.

* Residual roles used by the skeleton are deleted.
* The quantities \(a-b_R\) are equality demands, not upper bounds.
* Loops may occur in the residual selection but cannot serve a spanning
  tree.
* Parallel labelled roles are harmless.
* A protected option must be contracted first and its used tail demand
  decremented.

## 3. Payload scope

Changing only the leading letter preserves:

1. the full owner, by \(B\cup U_i=T_i\); and
2. every proper suffix union and therefore every marked lower target.

It does not automatically preserve an upper or exterior interval crossing,
residence at an external cut, or a common-cap/compiler cell whose legality
depends on \(B\). Such conditions must be included as structural zeros in
the role-to-tail graph. The theorem is exact after those deletions, but it
does not prove that the guarded graph still satisfies Hall.

## 4. Relation to the pull clock

The stationary pull-clock circulation is upstream of the fixed table. It
does not itself provide one role per owner or one literal occurrence per
named target, so applying Theorem 2.1 directly to the symmetric fractional
point would be a quantifier error.

The proof-safe implication is

\[
 \text{static owner/target-exact marked table}
 +\text{ Hall-safe trace tree}
 \Longrightarrow
 \text{one rooted label-exact Euler chronology}.             \tag{4.1}
\]

The reverse implication also holds by extracting the table and a spanning
tree from the chronology. Hence the triangular rooted spine-tree lemma is
the exact minimal lower-side statement exposed by this reduction. No
upper-bound claim follows until that lemma and the later upper/residence/
compiler rows are proved.

