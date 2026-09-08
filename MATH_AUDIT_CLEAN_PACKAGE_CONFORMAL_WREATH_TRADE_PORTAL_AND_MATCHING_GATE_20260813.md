# Audit of the clean-package conformal wreath-trade portal theorem

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_CLEAN_PACKAGE_CONFORMAL_WREATH_TRADE_PORTAL_AND_MATCHING_GATE_20260813.md`  
**Source SHA-256:**
`08f5ceda097056576f9ad4015cd0edac8f3a479e4764c8502cbd2079003d8a8d`  
**Method:** independent row-incidence, cyclic-window, Hall, and asymptotic
count audit; no computation or search  
**Verdict:** **PASS after occurrence and scope corrections.**  The theorem
is an exact sufficient portal criterion.  It does not prove that the
required portal matching exists in the canonical MSW atlas.

## 1. Conformal substitution is exact

For each trade `(P_j,N_j)`, support feasibility gives

\[
                         B_mP_j=B_mN_j.
\]

Because the negative rows are distinct rows of one exact factor, the
supports `B_mN_j` are mutually disjoint and avoid every untouched factor
row.  Their equal positive supports have exactly the same properties.
Thus all positive rows are automatically a packing and substitution
preserves the exact middle palette.  Complementation then preserves the
rank-`m+1` owner palette.  This proves Lemma 1.1 and the central-resource
claim without an additional cross-trade Hall system.

Only negative **row** disjointness is needed: equality of signed middle
supports supplies positive support disjointness.  The squarefree packing
hypothesis prevents multiplicity ambiguity within each sign.

## 2. Clean interval indices and halo separation pass

For the pointed oriented row

\[
                         \sigma=(D,C,I,S)
\]

with block sizes `q,m-q,q,m+1-q`, the length-`m` windows starting just
before `D` are

\[
 L_j=C\cup\{d_{j+1},\ldots,d_q\}
        \cup\{i_1,\ldots,i_j\},\qquad0\le j\le q.
\]

Thus `L_(j-1) union L_j=A_j`, where
`A_j=I_sigma(j-1,m+1)`.  Cyclic complementation gives exactly

\[
 \overline{L_j}=A_{m+j+1},\qquad
 \overline{A_j}=I_\sigma(m+j,m).
\]

Hence the antipodal owner arc has common intersection `S`, and the two
collared owner-index blocks are

\[
 [-d,q+d+1],\qquad[m-d,m+q+d+2]\pmod{2m+1}.
\]

The gap in either direction is `m-q-2d-2`, nonnegative under
`m>=3d+2` and `q<=d`.  At equality the far-port owners are distinct and
consecutive; their joining facet is not in either protected block.  The
central and halo claims therefore pass.

The earlier wording treated an unoriented row containing `S` as if it
determined a unique `(D,C,I)` choice.  It need not: the same set may occur
at several starts or in both orientations.  The corrected theorem defines
a portal as a row plus an **oriented pointed occurrence**.  This is the
right object because different occurrences can expose different halo
resources.

## 3. Hall scope is exact

The portal graph assigns at most one task to one trade.  A Hall matching
therefore selects distinct trades.  Since the entire bank has pairwise
disjoint negative row sets, the selected trades apply conformally by
Lemma 1.1.  The witnessing positive row and pointed occurrence supply the
clean package.  Conversely any installation constrained to at most one
task per trade defines such a matching, so Hall is necessary at exactly
that scope.

A positive row may contain several target intervals, but applying its trade
once does not count as several independently protected packages under
Theorem 3.1.  The source now states this convention explicitly.  A stronger
capacitated portal theorem would require a new within-row halo-conflict
calculation.

Lemma 4.1 is the standard greedy transversal bound.  Its per-pair conflict
quantifier is sufficient because, before a task is chosen, each previous
portal forbids at most `Delta` members of that task's list.  It is not
claimed necessary.

## 4. Universal-trade applicability language is proof-safe

The four-row identity `(5.1)--(5.2)` proves a prospective support-feasible
two-for-two trade for every choice of its labels and ordered banks.  It is
applicable to a fixed factor only when its two negative rows occur there.
The theorem uses this distinction correctly.

For the first-aligned `1100/1010` MSW packet, the cited inverse-triple
theorem supplies a row-disjoint family whose negative row pairs are actual
rows of the canonical factor; these are simultaneously applicable.  The
larger `(2m-1)Cat_(m-2)` inverse-triple atlas also consists of applicable
individual trades at the MSW seed, but their negative pairs overlap and
cannot all be applied at once.  A negative-row-disjoint rainbow selection
is genuinely still required.

## 5. Scale calculation passes, with an exact coefficient

A degree-two bank of `B_0` trades has two positive rows per trade and `n`
cyclic starts per row.  Hence the average multiplicity of rank-`s`
pointed portals is

\[
                         \bar d_s={2nB_0\over\binom ns}.
\]

If its negative rows lie in one exact factor, then
`2B_0<=Cat_m=binom(n,m)/n`, which yields `(6.2)`.

For `s=m+1-q` and `q=Theta(sqrt m)`,

\[
 {\binom nm\over\binom ns}
 =\prod_{j=0}^{q-2}{m+1+j\over m-j}
 =\exp(\Theta(q^2/m))=\Theta(1).
\]

For `N_m=(2m-1)Cat_(m-2)`, direct factorial cancellation gives the exact
identity

\[
 {2nN_m\over\binom ns}
 ={m(m+1)\over2(2m-3)}
  {\binom nm\over\binom ns}.
\]

The prefactor is `n/8+O(1)`, so the full overlapping atlas has average
portal occurrence degree `Theta(n)` at the deadline scale.  This is only
an average and says nothing by itself about a named casualty's degree,
negative-row conflicts, or extra-halo codegrees.

## 6. Exact conclusion

The source proves the implication

\[
\boxed{
\begin{gathered}
\text{pointed clean portals in positive sides of applicable trades}\ +\\
\text{a negative-row-disjoint Hall/rainbow selection}
\\ \Longrightarrow\\
\text{simultaneous exact owner/immediate-lower installation}.
\end{gathered}}
\]

It deliberately leaves the concrete MSW portal-degree, negative-row
matching, nonmiddle halo-conflict, global chronology, and deep-deck gates
open.

