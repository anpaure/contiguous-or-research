# Independent audit: fixed-factor functional digraph, Steiner barrier, and Boolean hexagons

**Date:** 2026-08-03  
**Audited theorem:**
MATH_THEOREM_FIXED_FACTOR_FUNCTIONAL_DIGRAPH_STEINER_PARITY_AND_C6_20260803.md  
**Method:** independent line-by-line combinatorial audit. No computation,
finite search, or solver is used.

## 0. Verdict

**GO after two proof-safe presentation repairs.**

The contraction degrees, local functional upper-colour digraph, two
separate Hall saturations, Steiner equivalence, even-\(m\) divisibility
obstruction, quantitative collision bound, full-hexagon count, and cubic
upper-colour action are all correct at their stated scopes.

The theorem was patched only to:

1. write the complement in the block family unambiguously as
   \([n]\setminus S\) and repair malformed binomial typography in (3.5);
2. state the exact common head in Theorem 3.2 and record the immediate
   global bound
   \(\sum_x\mathcal E_x\ge|\mathcal U|/2\) under balanced loads.

The result does not prove the cap-two second matching or an energy-decreasing
hexagon.

## 1. Contraction and degree audit

The containment graph between ranks \(m-1\) and \(m\) of
\([2m-1]\) is \(m\)-regular on both shores. For a matched middle set \(S\),
write

\[
 F_0^{-1}(S)=S-\{a(S)\}.
\]

The lower vertex \(q=S-\{a(S)\}\) has neighbours \(q+\{x\}\) for
\(x\notin q\). The choice \(x=a(S)\) is the deleted matching edge. Every
other choice is a unique \(b\notin S\), producing the contracted arc

\[
 S\longrightarrow S-\{a(S)\}+\{b\}.
\]

Thus every contracted vertex has outdegree \(m-1\). Deleting a perfect
matching from the balanced \(m\)-regular bipartite graph leaves degree
\(m-1\) on the other shore too, so every contracted vertex also has
indegree \(m-1\).

Fix \(R\in\binom{[n]}{m+1}\), and put \(S_b=R-\{b\}\). The unique
colour-\(R\) arc with tail \(S_b\) has head

\[
 S_b-\{a(S_b)\}+\{b\}=R-\{a(S_b)\}.
\]

Hence its facet-index action is
\(b\mapsto p_R(b)=a(S_b)\). Since the root belongs to \(S_b\), it differs
from \(b\), so the functional digraph is loopless. There is exactly one
outgoing colour-\(R\) arc at every facet; head multiplicities are the
fibres of \(p_R\).

A second perfect matching chooses one outgoing and one incoming contracted
arc at every vertex, exactly a directed cycle cover. Its upper-colour
multiplicity is exactly the number of selected arcs in \(p_R\). This
verifies Theorem 1.1 and Corollary 1.2.

## 2. Separate SDR Hall audit

In the colour-tail graph, an upper colour \(R\) has its \(m+1\) facets as
occurrences, while a middle tail belongs to \(m-1\) upper sets. In the
colour-head occurrence multigraph, \(R\) again has \(m+1\) occurrences,
and a middle head has degree \(m-1\) by the contracted indegree count.

For either graph and any upper-colour family \(X\),

\[
 (m+1)|X|\le (m-1)|N(X)|.
\]

The inequality remains valid with parallel head occurrences because the
right side uses the total occurrence degree available at the neighbour
vertices. It implies \(|N(X)|\ge|X|\), so Hall saturates every upper colour
in each projection.

These two matchings need not use the same arc occurrence. Even a common
one-per-colour partial choice would still have to extend to a full cycle
cover while allocating the remaining \(W-|\mathcal U|\) arcs without
creating multiplicity three. The theorem correctly leaves that correlation
open.

## 3. Steiner equivalence and parity audit

If every \(p_R\) is a permutation, then the roots of the \(m+1\) facets of
every \(R\) are distinct. Two adjacent middle sets are facets of their
unique rank-\(m+1\) union, so this is equivalent to adjacent middle sets
having different roots.

Fix \(x\). A set \(S\) rooted at \(x\) contains \(x\); therefore its
complement \(B=[n]\setminus S\) is an \((m-1)\)-subset of the
\((2m-2)\)-set \([n]\setminus\{x\}\). If two such blocks shared
\(m-2\) points, their complementary middle sets would be adjacent and
would both have root \(x\). Hence no \((m-2)\)-subset occurs in two blocks.

Every upper set \(R\) containing \(x\) has exactly one facet rooted at
\(x\), because its facet roots permute \(R\). Every fixed middle set rooted
at \(x\) lies in \(m-1\) upper sets. Thus

\[
 |\mathcal B_x|
 =\frac{\binom{2m-2}{m}}{m-1}
 =\frac1m\binom{2m-2}{m-1}
 =\operatorname{Cat}_{m-1}.
\]

Each block contains \(m-1\) subsets of size \(m-2\), and

\[
 (m-1)|\mathcal B_x|=\binom{2m-2}{m-2}.
\]

Nonrepetition plus this equality proves that every \((m-2)\)-subset occurs
exactly once: the claimed \(S(m-2,m-1,2m-2)\).

In such a design the number of blocks through an \((m-3)\)-set must be

\[
 \frac{\binom{m+1}{1}}{\binom21}=\frac{m+1}{2}.
\]

This is nonintegral for even \(m\), proving the parity impossibility.

## 4. Quantitative collision audit

Under the balanced root load, put
\[
 N=\binom{2m-2}{m-2},
 \qquad
 d_Q=\#\{B\in\mathcal B_x:Q\subset B\}.
\]

Every block contains \(m-1\) rank-\(m-2\) subsets, so
\(\sum_Qd_Q=N\). For every rank-\(m-3\) set \(P\),
\[
 \sum_{Q\supset P}d_Q
 =2\,\#\{B\in\mathcal B_x:P\subset B\}
\]
is even. There are \(m+1\) possible \(Q\supset P\), an odd number for
even \(m\); hence at least one has \(d_Q\ne1\).

Let \(Z=\#\{Q:d_Q=0\}\) and
\(P_+=\#\{Q:d_Q\ge2\}\). Every bad \(Q\) contains \(m-2\) possible
\(P\)'s, so double counting gives
\[
 Z+P_+\ge\frac{N}{m+1}.
\]

Since \(\sum_Q(d_Q-1)=0\),
\[
 Z=\sum_{d_Q\ge2}(d_Q-1)\ge P_+.
\]
Consequently \(Z\ge N/(2(m+1))\), and
\[
 \mathcal E_x
 =\sum_Q\binom{d_Q}{2}
 \ge\sum_{d_Q\ge2}(d_Q-1)
 =Z.
\]

Two blocks counted at \(Q\) complement to adjacent middle tails with a
unique union \(R\). Both roots are \(x\), and both contracted arcs have
head \(R-\{x\}\). This validates the collision interpretation.

If all \(2m-1\) coordinates have balanced load, summing and using
\[
 \binom{2m-2}{m-2}
 =\frac{m+1}{2m-1}|\mathcal U|
\]
gives \(\sum_x\mathcal E_x\ge|\mathcal U|/2\), so the global
positive-density wording is exact.

## 5. Boolean hexagon audit

Fix \(C\in\binom{[n]}{m-2}\) and
\(A=[n]\setminus C\), so \(|A|=m+1\). At lower vertex \(C+\{a\}\), the
deleted matching edge is exactly
\[
 C+\{a,f_C(a)\}.
\]

For a triple \(\{a,b,c\}\), its two hexagon edges at that lower vertex go
to \(C+\{a,b\}\) and \(C+\{a,c\}\). Both survive precisely when
\(f_C(a)\notin\{b,c\}\). Applying the same test at \(b,c\) proves the
exact full-support criterion.

There are \(\binom{m+1}{3}\) triples. Each of the \(m+1\) directed pointer
edges belongs to \(m-1\) triples. A union bound therefore leaves at least
\[
 \binom{m+1}{3}-(m+1)(m-1)
 =\frac{(m+1)(m-1)(m-6)}6
\]
full supports, positive for \(m\ge7\). Pointer-edge overlaps only improve
this lower bound.

The two alternating perfect matchings of a full Boolean hexagon are exactly
the phases (4.4) and (4.5). For example, the old edge
\((C+a,C+ab)\) has contracted upper colour
\[
 F_0(C+a)\cup(C+ab)=C+ab+f_C(a).
\]
The other five formulas follow identically, proving the two three-element
multisets (4.6)--(4.7). The action is therefore a genuine cubic cyclic
reassignment.

The adjacent-rank Boolean incidence graph has no \(C_4\): two distinct
rank-\(m-1\) sets have at most one common rank-\(m\) superset. Thus \(C_6\)
is indeed the smallest possible nontrivial alternating matching exchange.
Abundance of potential supports does not imply that an incumbent second
matching occupies a phase or that the switch lowers global collision
energy.

## 6. Proof-safe endpoint

The audited implications are

\[
\boxed{
\begin{array}{c}
F_0\text{ fixed}\\
\Downarrow\\
(m-1)\text{-regular contracted digraph with functional colour classes}\\
\Downarrow\\
\text{separate tail/head colour SDRs and cubic local exchanges}.
\end{array}}
\]

The permutation shortcut is impossible for even \(m\), with at least
half an upper-layer's worth of root-labelled collision pairs under balanced
loads. The remaining theorem is still the occurrence-correlated cap-two
cycle-cover theorem; no step in the audited note proves it.
