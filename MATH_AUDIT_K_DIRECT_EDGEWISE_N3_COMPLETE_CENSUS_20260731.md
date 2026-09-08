# Independent audit: direct-edgewise \(n=3\) complete census

Date: 2026-07-31  
Verdict: **GO**, with all discovered corrections incorporated in the theorem at SHA-256

    0b0533fe423a18e0b0b9ba879f37cf35a47b9148daf2ccf501a1da2510610cbd.

Audited theorem:

    MATH_THEOREM_K_DIRECT_EDGEWISE_N3_COMPLETE_CENSUS_AND_MATCHING_LOSS_RANK_20260731.md

## 1. Mathematical replay

The exact identities

\[
r_{\mathcal A_F^{\rm dir}}(S)=|S|-\kappa_F^-(S),
\qquad
r_{\mathcal B_F^{\rm dir}}(S)=|S|-\kappa_F^+(S)
\]

follow directly from dual transversal rank and Hall deficiency. Edmonds' formula then gives the common-basis criterion

\[
\kappa_F^-(S)+\kappa_F^+(E\setminus S)\le N-C
\quad(S\subseteq E).
\]

The uniform-vector criterion, the \(n=3\) co-singleton collapse, and the path-sensitive inequality

\[
(n+2)\kappa_F^-(S)+2g\le(n-2)|S|+\iota^-(S)
\]

were rederived independently. No algebraic or domain defect remains.

The theorem correctly says that the direct pullbacks have rank at most \(C\), not automatically rank \(C\). Rank \(C\) is part of the terminal-bank matching condition.

## 2. Exhaustive agreement

Two independently written complete enumerators agree on:

* \(458{,}544\) undirected forests;
* \(9{,}549{,}888\) coherent orientations;
* \(7{,}136{,}784\) orientations with a direct common basis;
* \(1{,}242{,}576\) upper-uniform and \(1{,}242{,}576\) lower-uniform orientations;
* \(364{,}176\) both-uniform orientations;
* the complete sixteen-bin common-basis-count histogram.

The cross-audit independently parses the full density-pair histogram and proves:

\[
\min \text{ individual density}=\frac23,\qquad
\max \text{ simultaneous minimum density}=\frac{14}{15},
\]

with \(3{,}600\) orientations at the pair \((2/3,2/3)\).

The two literal sharp cuts replay as:

\[
0x3e\to\{0x1a,0x1c,0x26\},\quad S=\{5,9,11\},
\]

and

\[
0x01\to\{0x0d,0x13,0x23\},\quad S=\{5,6,11\}.
\]

In both cases the deleted neighbour bank gives deficiency one, while an explicit matching covers the remaining five outer vertices, so the rank is exactly two.

## 3. Physical replay and corrected parallel-cell semantics

Both exhaustive producers rediscover the same both-uniform physical support. The corrected independent source explicitly deduplicates two occurrence labels only when they have:

1. the same direct middle/outer cell; and
2. the same undirected physical edge.

It aborts on any other collision. The corrected exhaustive run retained assertions and reproduced every aggregate.

One independent consumer, applied separately to both producer encodings, verifies on each shore all \(2^{15}\) rank inequalities and all fifteen co-singleton bases. It also reconstructs:

\[
\Delta=2,\quad\beta=0
\]

for the child forest and for the complete uncontracted 50-vertex variable physical support. Contracting fixed forest fragments preserves cycle rank, so the contracted graphic condition follows.

The result proves existence of at least one both-uniform literal joint physical direct extension. It does not count all physically extendable both-uniform orientations.

## 4. Frozen audit artifacts

    scratch/audit_catalan_direct_edgewise_n3_two_censuses_20260731.py
      SHA-256 df1a2c05389944c6454d7035d7889926a0ad6b2764e38731385732445bc30c98
    scratch/catalan_direct_edgewise_n3_two_censuses_20260731.crossaudit.v2.json
      SHA-256 41058a94bd9d5261db585b3507b09dbff4468aacf97b9cd1bb4a387c3e41b0a8
    scratch/audit_catalan_direct_edgewise_n3_uniform_physical_witness_20260731.py
      SHA-256 cb524c1c3a483453e79a30e551886132142d4af7f4dec53bed51e7964589cd57
    scratch/catalan_direct_edgewise_n3_uniform_physical_witness_20260731.replay.json
      SHA-256 7ffbf20ebb2f720eef71655b3f58d4f2da2d25f579ddce5754813eb456669c53
    scratch/catalan_direct_edgewise_n3_uniform_physical_witness_20260731.independent.v2.replay.json
      SHA-256 a115261a24654efee3edceeaed803e1c6e78874e412fc414384c7bb79d6036c5

No exhaustive computation was run on the local machine.
