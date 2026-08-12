# SUPERSEDED lineage audit: Macaulay interval erosion and triangular crossing

> **DO NOT CITE AS THE FINAL AUDIT.**  This file audited theorem SHA
> `50ef8515...`.  The theorem was subsequently corrected and strengthened.
> The authoritative independent audit is
> `MATH_AUDIT_MACAULAY_INTERVAL_AND_COMMON_ROOT_RUN_INDEPENDENT_GO_20260804.md`,
> SHA `8ebc6da6b34d322b3861383ea2c7adfb11ac741f0224d470687479d16ee09b12`,
> covering final theorem SHAs `77253694...` and `83db1a8e...`.

**Date:** 2026-08-04  
**Method:** independent symbolic audit; pure mathematics, no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md`  
**Audited theorem SHA-256:**
`50ef851599ce14f4075087e5782aa91180d3ed985ba16ac749f53093c77f6e99`  
**Verdict:** **GO**, at the exact scope stated in the theorem.

## 1. Canonical decomposition

For the canonical expansion

\[
 |F|=\sum_{j=s}^m {c_j\choose j},
 \qquad c_m>c_{m-1}>\cdots>c_s,
\]

the usual colex recursion fixes the pivots
`Q_j={p_{j+1},...,p_m}`, with `p_l=c_l+1`, and gives the disjoint blocks

\[
 \mathcal B_j=Q_j+{[c_j]\choose j}.
\]

Complementation gives exactly the lower Boolean intervals

\[
 \mathcal I_j=\{X:C_j\subseteq X\subseteq S_j,\ |X|=m-1\}.
\]

The star-union identity is also exact.  If `X` contains `C_j` but is not
in `I_j`, it contains a pivot `p_l` with `l>j`; direct set subtraction
shows

\[
 C_l\setminus C_j=\{p_l\}.
\]

Hence `C_l subset X`, and iteration reaches a unique interval block.
This proves both displayed decompositions without an unstated nesting
assumption.

## 2. Triangular shadow intersections

A facet of `B_j` is either internal,

\[
 Q_j\cup H,\qquad |H|=j-1,
\]

or is obtained by deleting one pivot `p_h` from `Q_j`.  For `j<l`, a
facet can lie in `partial B_l` only in the second case with `h=l`.
Consequently

\[
 \partial B_j\cap\partial B_l
 =\{(Q_j-\{p_l\})\cup H:H\in{[c_j]\choose j}\}.
\]

The residual `(l-1)`-set lies in `[c_l]`, so its degree in `B_l` is

\[
 c_l-(l-1)=\rho_l.
\]

Thus a multiply represented facet has one unique largest-index internal
block and only boundary occurrences from earlier blocks.  The pairwise
intersection cardinality is exactly `b_j`.  With triple intersections,
the sum of terminal-boundary multiplicities is at most, rather than equal
to, the number of block pairs; the audited theorem states this corrected
inequality explicitly.

## 3. Six-row local current

At a shared owner let the terminal fibre have size `rho_l`, let `h` be
the number of boundary singleton fibres, and let the protected degree be
`d in {0,1,2}`.

If `rho_l>=2`, the scalar loss from gluing is `h`.  Direct substitution
in

\[
 \lambda_P(A)_U=
 \min(2,a_U)-\min(2-p_U,a_U)
\]

gives cancellation `0`, `tau_D`, and `h` at protected degrees `0`, `1`,
and `2`, respectively.  The remaining margin taxes are therefore

\[
 h,\qquad h-\tau_D,\qquad0.
\]

If `rho_l=1`, all `h+1` pieces are singleton fibres.  The same table gives

\[
 h-1,\qquad h-t_D,\qquad0.
\]

These are exactly the six rows in the theorem and are nonnegative.  On
summing over shared owners this proves the occurrence-level gluing
identity.  Since `h<=binom(|J(D)|,2)`, summing the exact pairwise
intersection sizes gives

\[
 \sum_D\chi_P(D)
 \le\sum_{j=s}^{m-1}(m-j){c_j\choose j}.
\]

No no-triple-intersection premise is used for this inequality; that
premise appears only in the theorem's equality statement.

## 4. Head--tail erosion

Treat every residual lower vertex as a singleton block.  The frozen
constant-spread estimate supplies margin at least `m-12` per singleton.
There are `m|R|` residual owner incidences.  At an owner with empty head,
the first residual insertion has zero gluing cost, saving one unit.

For block `j`, precisely

\[
 {c_j\choose j-1}
\]

facets are internal.  By the triangular law these internal-facet sets are
disjoint between residual blocks and meet no higher-index head block.
Therefore the gluing cost is at most

\[
 m|R|-\sum_{j=s}^r{c_j\choose j-1}.
\]

Using

\[
 {c_j\choose j-1}
 ={j\over c_j-j+1}{c_j\choose j}
 ={j\over\rho_j}b_j
\]

gives exactly

\[
 \mu_P(A)\ge\mu_P(A^{\rm head})+
 \sum_{j=s}^r\left({j\over\rho_j}-12\right)b_j.
\]

Thus a safe head plus nonnegative aggregate aperture credit is a valid
sufficient condition.  The termwise condition `rho_j<=j/12` is only a
sufficient specialization, as stated.

## 5. Sharp scope boundary

For a two-level expansion, the shared facets are exactly the second
block.  When the protected bank is empty, every shared owner pays one
unit, so the triangular current equals the full size of that block.  This
correctly disproves zero-cost composition of individually safe intervals;
it does not disprove protected Ore for their union, which is covered by
the separate bounded-DNF theorem.

The theorem does **not** close arbitrary shifted families or initial-colex
tails containing a negative aggregate of broad terms
`rho_j>j/12`.  It also makes no factor-topology, residence, or common-cap
claim.  Those exclusions are explicit and necessary.
