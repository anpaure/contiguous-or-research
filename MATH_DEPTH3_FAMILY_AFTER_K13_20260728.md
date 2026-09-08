# The depth-3 family after the exact k=13 certificate

Let

\[
 r=\lceil k/2\rceil,\qquad W=\binom{k}{r},\qquad
 \Lambda=\sum_{j=1}^{r-1}\binom{k}{j},
\]

and let `d(k)` be the least `d` with

\[
 dW+\binom{d+1}{2}\ge\Lambda.
\]

The exact table is:

| k | d | B=W+d | slack | relative slack |
|---:|---:|---:|---:|---:|
| 11 | 3 | 465 | 369 | 36.07% |
| 12 | 2 | 926 | 266 | 16.78% |
| 13 | 3 | 1719 | 1059 | 25.86% |
| 14 | 2 | 3434 | 392 | 6.05% |
| 15 | 3 | 6438 | 2928 | 17.87% |
| 16 | 3 | 12873 | 12284 | 46.65% |
| 17 | 3 | 24313 | 7401 | 11.29% |
| 18 | 3 | 48623 | 39105 | 36.63% |
| 19 | 3 | 92381 | 14997 | 5.72% |
| 20 | 3 | 184759 | 122365 | 28.33% |
| 21 | 3 | 352719 | 9579 | 0.91% |
| 22 | 3 | 705435 | 371867 | 21.32% |
| 23 | 4 | 1352082 | 1214019 | 28.94% |

Thus, apart from the already-solved `k=12` depth-2 case and the exact
`k=14` depth-2 outlier, every case from 11 through 22 has depth 3.  The
razor-tight future test is `k=21`, not `k=14`.

## What k=11 actually transferred to k=13

The exact `k=13` construction now confirms the following architecture.

1. Search in the cyclic quotient, using one variable for each orbit of
   lower middle-level sets.
2. Enforce the degree-2 condition, complete upper shadows, and depth-3
   residence in the quotient model.
3. Do **not** require quotient Hamiltonicity.  Permit a small exact 2-factor.
4. Lift every nonzero-voltage quotient component to one physical cycle.
5. Cut and cross-splice the few physical cycles into a Hamilton path while
   preserving all upper shadows.
6. Use the one missing lower-q1 colour as the odd-case boundary flag in the
   depth-3 compiler.

For `k=11`, step 3 happened to return one quotient Hamilton cycle.  For
`k=13`, it returned two quotient components of sizes 119 and 13, with
voltages 8 and 6.  One seam completed the optimal word.

This is stronger evidence than a direct `k=13` Hamilton-cycle search would
have supplied: connectivity is not the invariant part of the construction.
Exact shadows, residence, and `O(1)` component count are.

## Two cautions from the exact signatures

- The minimum lower-sequence run length is exactly 3 for both `k=11` and
  `k=13`.  Although the mean run rises from 5 to 6, the construction uses the
  residence boundary exactly.  Residence should remain a hard constraint,
  not merely a soft objective.
- The `k=13` upper-q1 multiplicities are `1^936 2^273 3^78`.  Hence an exact
  solution need not have a simple excess design.  Penalizing triple loads is
  reasonable, but forbidding them would exclude the known optimum.

## Priority implication

The reusable odd-prime target is therefore not necessarily a cyclic
Hamilton `sigma` map.  It is an equivariant, all-shadow-exact, resident
quotient 2-factor with few nonzero-voltage components and a shadow-safe
spanning splice.  The `k=13` certificate proves this formulation is strictly
more flexible while retaining the full lower-bound architecture.

