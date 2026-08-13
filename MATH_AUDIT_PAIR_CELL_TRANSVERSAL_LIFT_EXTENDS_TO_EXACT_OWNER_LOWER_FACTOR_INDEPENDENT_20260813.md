# Independent audit: transversal lift extends to an exact owner/lower factor

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** `MATH_THEOREM_PAIR_CELL_TRANSVERSAL_LIFT_EXTENDS_TO_EXACT_OWNER_LOWER_FACTOR_20260813.md`  
**Source SHA-256:** `5316e51d0204d2bb6cc7a12609d61e836ce177a706fed45247e03bdfd17463c7`

This was a proof-level audit.  No local search or solver was used.

## 1. Protected incidence cycle

The lifted owner \(D_t=L_{x_t}\cup L_{x_{t+1}}\) is rank \(r\), and consecutive
lifted owners meet in exactly \(L_{x_t}\).  Distinct cube edges give distinct lifted
owners, so the alternating incidence lift is a simple cycle with

\[
 |Z|=|Y|=2^{r-1},\qquad |E(P)|=2^r.
\]

The two exposure bounds are exact.  A lower facet below a protected owner is either a
transversal, in which case only the two Hamilton edges at that cube vertex are
possible, or it has one double and one empty matched pair, in which case only the two
fillings of the empty pair are possible.  Dually, an owner contains at most two
transversal facets.

For the actual protected cycle and every residual shore \(A\subseteq\mathcal L-Z\),
each protected owner has both protected edges outside \(A\).  Hence its loss is simply
\(\min\{2,a_U\}\), and

\[
 \lambda_P(A)
 =\sum_{U\in Y}\min\{2,a_U\}
 \le e(A,Y)\le2|A|.
\]

This gives a shorter direct verification of Lemma 2.2 and agrees with its more general
charging proof.

## 2. Small shores

The general protected-Ore localization theorem gives

\[
 \min\{|A|,W-|A|\}
 <\frac{r(r-1)}{2r-1}2^r<r2^{r-1}.
\]

After complementing lower facets, \(A\) is an \(r\)-uniform family.  If
\(|A|={x\choose r}<r2^{r-1}\), the entropy base

\[
 \frac{(13/10)^{13/10}}{(3/10)^{3/10}}>2
\]

implies \(x<13r/10\) eventually.  Kruskal--Katona then gives

\[
 |N(A)|/|A|\ge r/(x-r+1)>r/(3r/10+1).
\]

Together with the exact capped-shadow slack inequality, this makes
\(\sigma(A)>2|A|\ge\lambda_P(A)\) for all sufficiently large \(r\).  The direction
and constants in (3.2)--(3.4) are correct.

## 3. Co-small shores

Writing \(X=\mathcal L-Z\) and \(B=X-A\), the co-small alternative indeed gives
\(|B|<r2^{r-1}\).  A positive inclusion-minimal optional core has
\(|Q|>|B^-|\).  Since every owner contains at most two protected lower vertices, its
optional gap is at least \(r-2\); with residual capacity at most two, every owner in
\(Q\) must contain at least \(D=r-3\) members of \(B^-\).  The sharp one-sided
partial-shadow theorem yields

\[
 |B^-|\ge {2D-1\choose D-1}+1
          ={2r-7\choose r-4}+1=2^{2r-o(r)},
\]

contradicting \(|B^-|<r2^{r-1}\).  Thus the co-small argument is also valid.

## 4. Completion and scope

Protected Ore--Ryser and bipartite integral \(b\)-matching now saturate every residual
lower demand and every residual owner capacity.  Because two distinct adjacent
rank-\(r\) owners have a unique rank-\((r-1)\) intersection, projection gives a
simple Johnson two-factor with every lower colour exactly once.

The proof does not control the chronology of the complementary factor, upper support,
source intervals, or fusion.  The protected lift remains a closed saturated component.
The source states all of these limitations explicitly.  Its exact conclusion is that
the top-cell complement balance is not an owner/lower incidence obstruction; the
remaining obstruction is chronological.
