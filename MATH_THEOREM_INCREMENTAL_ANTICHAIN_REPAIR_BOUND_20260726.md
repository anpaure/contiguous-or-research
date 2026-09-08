# Incremental antichain repair bound for literal OR words

Date: 2026-07-26

## Theorem

Let \(Q=(Q_1,\ldots,Q_L)\) and \(R=(R_1,\ldots,R_s)\) be literal
set-valued words, and write \(Q\Vert R\) for their concatenation.  If
\(\mathcal A\) is any antichain of target sets, then

\[
 \boxed{
 \bigl|\mathcal A\cap
   (\operatorname {Cov}(Q\Vert R)\setminus\operatorname {Cov}(Q))
 \bigr|\le s.}
 \tag{1}
\]

In particular, at any fixed Boolean rank, appending \(s\) letters can
repair at most \(s\) targets which were missing from the original word.

The same statement holds when \(R\) is prepended instead of appended.

## Proof

For every newly covered target \(A\in\mathcal A\), choose one witnessing
interval in \(Q\Vert R\).  Since \(A\notin\operatorname {Cov}(Q)\), its
right endpoint lies in the appended block \(R\).  Map \(A\) to that right
endpoint.

All interval unions having one fixed right endpoint are nested as their
left endpoints move left: enlarging the position interval can only add
letters and hence can only enlarge its union.  Therefore two distinct
incomparable targets cannot be mapped to the same endpoint.  Since
\(\mathcal A\) is an antichain, the endpoint map is injective, and there
are only \(s\) endpoints in \(R\).  This proves (1).  Reversing the word
proves the prepended version. \(\square\)

## Consequences for the Gaussian annulus

Let \(Q_m\) be the proved PBBS central word of length \(W+o(W)\), and let
\(R_m\) be an appended continuation of length \(o(W)\).  For every rank
\(r\), if \(Q_m\Vert R_m\) covers the entire rank, then

\[
 \#\left(\binom{[n]}r\setminus\operatorname {Cov}(Q_m)\right)=o(W).
 \tag{2}
\]

Thus an append-only \(o(W)\) Gaussian-annulus bridge is possible only if
the already-paid PBBS word has near-complete coverage at every annulus
rank.  Cross-seam witnesses do not evade this requirement: they still end
at one of the new positions and are counted by (1).

Taking \(Q\) empty and \(\mathcal A=\binom{[2m]}{m-H-1}\) gives the
universal lower bound

\[
 |R|\ge\binom{2m}{m-H-1}.
 \tag{3}
\]

At \(H=A\sqrt m+O(1)\), (3) is

\[
 |R|\ge(e^{-A^2+o(1)})\binom{2m}m,
\]

so no separately appended fixed-Gaussian tail can have length \(o(W)\).

This theorem does not rule out modifying or replacing \(\Theta(W)\) of
the baseline letters in place.  It shows precisely why the remaining
annulus mechanism must be an in-place compiler, a baseline-sharing
construction, or a theorem that the PBBS baseline already has small
per-rank annulus deficiency.
