# PBBS versus lexical Middle-Levels Hamiltonization: exact source and transfer audit

Date: 2026-07-26

Method: pure mathematics and local-source audit only. No web search,
computation, or finite search is used.

## 0. Verdict

Put

\[
 n=2r+1,\qquad
 W_r=\binom{2r+1}{r},\qquad
 B_r=\operatorname {Cat}_r=\frac{W_r}{2r+1}.
\tag{0.1}
\]

There are two different cycle factors in play.

1. The Gregor--Mütze--Nummenpalo short proof starts from the
   \(0/1\)-lexical Middle-Levels factor \(F_{\rm lex}\). Its published
   plane-tree connector theorem gives a Hamilton cycle after exactly
   \(p_r-1\le B_r-1\) factor-alternating \(6\)-cycle flips, where \(p_r\)
   is the number of plane trees with \(r\) edges.
2. The canonical periodic-box-ball factor \(F_{\rm PBBS}\) is an odd-graph
   factor, whose bipartite lift is a different Middle-Levels factor.
   Already at \(r=2\), the PBBS lift has two components whereas
   \(F_{\rm lex}\) has one. Thus the slash identification
   \(F_{\rm PBBS}=F_{\rm lex}\), even up to coordinate conjugacy, is false.

Consequently an \(O(B_r)\)-edit Hamilton cycle is a valid imported theorem
starting from \(F_{\rm lex}\), but no local source proves such a
Hamiltonization starting from \(F_{\rm PBBS}\). The audited PBBS
angle-load theorem cannot be transferred to the published lexical
Hamilton cycle without one new connector or histogram-transfer lemma.

There is also a normalization correction. The PBBS angle theorem gives
complete opposite support. If \(s\) compatible hexagon flips were
available from the PBBS lift, they would create at most \(3s\) opposite
holes. The raw repetition count would be

\[
 \frac{2W_r}{r+2}+O(s),
\tag{0.2}
\]

because \(W_r-\binom{2r+1}{r-1}=2W_r/(r+2)\) repetitions are unavoidable.
Thus \(s=O(B_r)\) gives raw repetition \(O(B_r)=o(W_r)\), not
\(O(B_r/r)\). An \(O(B_r/r)\) statement can refer only to the additional
hole/excess term, and would require \(s=O(B_r/r)\).

## 1. What is actually imported for the lexical factor

Let

\[
 G_r=Q_{2r+1}\left[
 \binom{[2r+1]}r\cup\binom{[2r+1]}{r+1}\right].
\]

The vendored source tmp/central/gmlc2.tex records the following exact
interface.

* Lines 625--627 identify the earlier \(\ell=1\) factor as the union of
  the \(0\)- and \(1\)-lexical perfect matchings. The original
  \(r,r-1\) indexing is isomorphic to \(0,1\) by reversing bitstrings.
* Line 686 states, citing Gregor--Mütze--Nummenpalo Proposition 2, that
  its number \(p_r\) of cycles is the number of plane trees with \(r\)
  edges.
* Lines 997--1014 state, citing their Proposition 3, the alternating
  \(6\)-cycle switch and its edge-disjoint/noninterference properties.

The remaining published \(\ell=1\) input is connectivity of the
plane-tree flippability graph. A spanning tree of that graph has
\(p_r-1\) edges; the corresponding compatible hexagons successively merge
the \(p_r\) factor cycles to one Hamilton cycle. Since forgetting the
root maps the \(B_r\) rooted ordered trees onto the plane trees,

\[
                         p_r-1\le B_r-1.             \tag{1.1}
\]

This is an exact constant-one \(O(B_r)\) flip bound.

The local source does not reproduce the \(\ell=1\) connectivity proof:
line 1028 explicitly excludes \(\ell=1\) from its proof and imports the
earlier theorem. Therefore (1.1) is locally verified as the precise
interface to the named Gregor--Mütze--Nummenpalo theorem, but it is not a
self-contained theorem proved in the vendored TeX. It should also not be
attributed merely to the distinct Mütze--Nummenpalo efficient-generation
paper.

## 2. One hexagon changes exactly three projected slots

### Lemma 2.1 (projection stability)

Let \(F\) be a spanning \(2\)-factor of \(G_r\), and let \(Z\cong C_6\)
be factor-alternating. Put \(F'=F\mathbin\triangle Z\). After suppressing
the rank-\((r+1)\) shore, the projected Johnson factors differ in exactly
three edge slots: three old Johnson edges are replaced by three new ones.
In particular their projected-edge symmetric difference has size at most
six.

The opposite triple-union colour changes at most three rank-\(r\)
vertices. Hence the \(L^1\) distance between the two opposite-colour
histograms is at most six, and the number of new holes is at most three.

#### Proof

An alternating hexagon contains three factor edges and three nonfactor
edges. At each of its three upper vertices, symmetric difference replaces
one of the two incident factor edges by the other hexagon edge. Suppressing
that upper vertex therefore replaces its projected Johnson edge, and no
other upper slot changes. This proves the first assertion.

The same argument on the lower shore shows that precisely the three lower
vertices of \(Z\) can acquire a different ordered pair of adjacent upper
neighbours. Their pair union, equivalently the triple union of consecutive
lower states, is the opposite colour. Replacing three occurrences has
histogram \(L^1\)-cost at most six and can delete at most three formerly
present labels. \(\square\)

For any ordered compatible family of \(s\) flips, the triangle inequality
therefore gives at most \(3s\) changed opposite-colour occurrences and at
most \(3s\) new holes.

## 3. The PBBS lift and its complete opposite support

Let \(f\) be the PBBS permutation of
\(\binom{[2r+1]}r\). Its Middle-Levels lift joins a lower copy of \(A\)
to the upper copies

\[
                         f(A)^c,\qquad f^{-1}(A)^c.
\tag{3.1}
\]

After suppressing the upper shore, the two projected neighbours of \(A\)
are \(f^{-2}(A)\) and \(f^2(A)\). The opposite triple-union colour centred
at \(A\) has complement

\[
 \bigl(f^{-2}(A)\cup A\cup f^2(A)\bigr)^c
   =f^{-1}(A)\cap f(A).                              \tag{3.2}
\]

Indeed, the two upper neighbours in (3.1) have union
\([2r+1]\setminus(f^{-1}(A)\cap f(A))\), and this is also the union of the
three consecutive lower states.

Thus the opposite-colour histogram of the PBBS lift is exactly, after
complementation, the audited PBBS angle histogram. In particular every
rank-\((r-1)\) target occurs. If an ordered compatible family of \(s\)
hexagon flips Hamiltonized this same lift, Lemma 2.1 would give

\[
 h_{\rm opp}\le3s,                                  \tag{3.3}
\]

where \(h_{\rm opp}\) is the number of missing opposite targets.
Consequently the raw repetition count of the Hamilton output would be

\[
\begin{aligned}
 \beta_r
 &=W_r-\left(\binom{2r+1}{r-1}-h_{\rm opp}\right)\\
 &=\frac{2W_r}{r+2}+h_{\rm opp}
 \le\frac{2W_r}{r+2}+3s.                            \tag{3.4}
\end{aligned}
\]

For \(s=O(B_r)\), this is \(O(B_r)=o(W_r)\). This is already enough for
the little-oh Middle-Levels base condition appearing in the audited
Pascal reduction. It does not give raw \(\beta_r=O(B_r/r)\), because the
first term of (3.4) is \(\Theta(B_r)\).

## 4. Exact nonidentity at \(r=2\)

On \([5]\), direct cyclic-parenthesis reduction gives the two PBBS orbits

\[
 (12,34,15,23,45),\qquad
 (13,24,35,14,25).                                  \tag{4.1}
\]

Both have odd length five. Their bipartite double covers are therefore
two \(10\)-cycles in \(G_2\). Equivalently, the suppressed-shore
monodromy \(f^{-2}\) has two components.

By the Gregor--Mütze--Nummenpalo component classification, the
\(0/1\)-lexical factor has one component for each plane tree with two
edges. There is only one such plane tree, so \(F_{\rm lex}\) is one
\(20\)-cycle.

Component count is invariant under coordinate permutations and shore
exchange. Hence

\[
                         F_{\rm PBBS}\not\cong F_{\rm lex}
\tag{4.2}
\]

even in the first nontrivial dimension. The published lexical hexagons
are alternating relative to \(F_{\rm lex}\); (4.2) gives no reason for
them to be alternating relative to the PBBS lift.

## 5. The exact missing connector lemma

The minimum PBBS theorem which would justify the proposed transfer is:

### PBBS compatible-hexagon merge-tree lemma

For every \(r\), there are hexagons

\[
                         Z_1,\ldots,Z_s\subseteq G_r,
\qquad s\le C B_r,                                  \tag{5.1}
\]

such that, with \(F_0\) the PBBS lift and

\[
                         F_j=F_{j-1}\mathbin\triangle Z_j,
\tag{5.2}
\]

each \(Z_j\) is alternating with respect to the current factor
\(F_{j-1}\), each switch is a pure component merge, and \(F_s\) is one
Hamilton cycle.

The stronger rate \(s=O(B_r/r)\) would give additional opposite defect
\(O(B_r/r)\) by (3.3). The rate \(s=O(B_r)\) already gives
\(\beta_r=o(W_r)\) by (3.4).

No workspace theorem proves (5.1)--(5.2). The GMN connected auxiliary
graph is tied to the lexical factor. The existing PBBS \(C_6\) theorem
switches one fixed matching, has a different three-component/parity
topology, and explicitly leaves transfer to full-factor connectors open.

## 6. Audited boundary

The sharp conclusions are therefore:

1. **Verified imported theorem:** \(F_{\rm lex}\) is Hamiltonized by
   exactly \(p_r-1\le B_r-1\) alternating hexagons.
2. **Verified edit constant:** one such hexagon changes three projected
   edge slots and at most three opposite-colour occurrences.
3. **Refuted identification:** \(F_{\rm PBBS}\) is not the lexical factor.
4. **Invalid inference:** the PBBS angle-load theorem cannot be attached
   to the published lexical Hamilton cycle without a new theorem.
5. **Minimum open statement:** the PBBS compatible-hexagon merge-tree
   lemma (5.1)--(5.2), or alternatively a direct theorem that the lexical
   factor already has the same complete opposite support as PBBS.
