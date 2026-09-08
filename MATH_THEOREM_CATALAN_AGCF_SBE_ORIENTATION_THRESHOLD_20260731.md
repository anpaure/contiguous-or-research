# Antipodal-geodesic fillers and the SBE orientation threshold

Date: 2026-07-31  
Status: complete finite census at `n=3,4`; exact all-parameter target
isolated; no all-parameter SBE theorem is claimed.

## 0. Result

An antipodal-geodesic Catalan forest (AGCF) is the strongest known residence
filler: every component is a length-`n` complement geodesic and has no
internal coordinate run.  It is therefore natural to ask whether the same
object can also be the SBE structural parent.

The answer is sharply thresholded in the known cases.

\[
\begin{array}{c|c|c|c|c}
 n&\text{fixture}&\text{half-point violations}&
 \text{both-SBE orientations}&\text{all orientations}\\ \hline
 3&\text{AGCF}&(2,2)&0&32\\
 4&\text{independent AGCF}&(0,0)&15010&16384\\
 4&\text{recursive AGCF}&(0,0)&628&16384.
\end{array}                                                \tag{0.1}
\]

Thus endpoint antipodality does **not** make SBE or fractional half-SBE
automatic: the authenticated `n=3` AGCF is a counterexample.  Nor does it
make every orientation valid at `n=4`.  What it does provide is strong
positive evidence for the exact threshold target:

> **AGCF--SBE threshold conjecture.**  For every `n>=4`, there is an AGCF
> whose half-endpoint point is SBE on both shores and whose two rounded
> endpoint systems have a common coherent orientation.

Both independently constructed parameter-four AGCFs satisfy this target,
despite having very different numbers of feasible orientations.

If the conjecture is proved simultaneously with all-parameter AGCF
existence, one forest can supply both universal residence and balanced
strict common-basis marginals.  It would collapse the present distinction
between the structural parent and the independent filler.  It would not by
itself choose physical direct representatives or prove the complete DERF
graphic row.

## 1. Exact antipodal orientation form

Let the AGCF paths have endpoint pairs

\[
                         \{A_j,\overline{A_j}\},qquad
                         j=1,\ldots,\operatorname{Cat}_n.       \tag{1.1}
\]

Every coherent orientation chooses one member of each pair as the upper
terminal and the other as the lower terminal.  Thus the SBE gauge is a
complement-transversal problem on the endpoint bank.  All internal vertices
have forest degree two and every endpoint has degree one, so the
half-endpoint criterion from
`MATH_THEOREM_CATALAN_SBE_ORIENTATION_AND_FOUR_SECTOR_GATE_20260731.md`
specializes to

\[
                  n\kappa+(n+1)|S\cap E|\ge2|S|,       \tag{1.2}
\]

where `E` is the full AGCF endpoint set.

For a fixed AGCF, define the two supermodular raw endpoint demands
`Psi^-,Psi^+` by maximizing the SBE closure deficit over internal middle
vertices.  The integral gate is exactly to choose a complement transversal
`Z` satisfying

\[
 |Z\cap A|\ge\left\lceil{\Psi^-(A)\over C}\right\rceil,
 \qquad
 |(E\setminus Z)\cap A|
 \ge\left\lceil{\Psi^+(A)\over C}\right\rceil          \tag{1.3}
\]

for every endpoint family `A` (with negative demands truncated at zero).

Equations (1.2)--(1.3) are the exact two statements an all-parameter proof
must establish.  Antipodality supplies the complement pairing but does not
remove the ceiling obstruction: (1.2) itself fails by two on both shores at
`n=3`, and no orientation satisfies (1.3).

## 2. Parameter-four evidence

The independent exact-cover AGCF has `15,010` simultaneous solutions of
(1.3), or `91.6%` of all coherent orientations.  The recursively split AGCF
has only `628`, or `3.8%`.  In particular:

* feasibility is reproduced in two independent AGCF architectures;
* robustness under arbitrary orientation is false in both;
* a fixed numerical endpoint convention is not structural—the independent
  witness accepts its stored direction, while the recursive witness first
  succeeds at a nonzero orientation mask; and
* the useful theorem must be existential and globally correlated, not a
  coordinatewise endpoint rule.

This is consistent with the newborn-buffer formulation: an AGCF gives an
ideal residence bank, but its terminal orientation must still be selected
against the two global occurrence-cut systems before `Q` and the direct
representatives are frozen.

## 3. Audit

The exact census is replayed by

```text
scratch/audit_catalan_agcf_sbe_orientation_n3_n4_20260731.py
scratch/catalan_agcf_sbe_orientation_n3_n4_20260731.audit.json
```

with SHA-256 hashes

```text
67a0792660670f9dd8013f58b053235b24ce53a3d59ab129e2e67105c468e91f
5d280529f939432d29dfc4ab4ab0d7cdd7119fb4426000c2403a71fb2e65f830
```

and canonical payload hash

```text
5ecb3f415e8940364d4078516f185b42a044bd0ddb2a8c5f57e5d16d940b57bd
```

The script authenticates the three named fillers, verifies path lengths and
complementary endpoints, recomputes both half-point min-cuts, and exhausts
all coherent orientations.  Its scope is finite; it neither enumerates all
AGCFs nor proves the threshold conjecture.
