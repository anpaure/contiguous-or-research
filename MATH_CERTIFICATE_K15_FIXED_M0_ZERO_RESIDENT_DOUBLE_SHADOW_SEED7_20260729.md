# `k=15` fixed-`M0` zero-resident double-shadow certificate, seed 7

Date: 2026-07-29  
Status: exact SAT certificate independently decoded and physically replayed.
It is **not** bi-resident and is **not** all-depth complete.

## 1. Frozen inputs and outputs

The exact fixed-matching mapping is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/seed0.mapping.json
SHA-256 2350beb3c4bed89fb56a5a698e124f094ef59da375932511b667dc7483a46bb9.
```

The H100 DIMACS has 2,999 matching variables and 780,733 clauses:

```text
19,498 exact upper-q1/lower-q2 matching clauses
761,235 exact zero-gap clauses
```

Its SHA-256 is

```text
5be210a72ff3bd313a28e1cacbd42ba45f64d531082c7290954c8968573cc8ab.
```

The seed-7 model is retained locally as

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    seed0.dualresident.seed7.out
SHA-256 813cfa6663c6ab4fd381a44f06c373d2706ea4f7f39a22f1af8d7292108cbd77.
```

The decoded 429-row factor and independent audit are

```text
seed0.dualresident.seed7.factor.json
SHA-256 b4f9cd2e4e32220ff96ee6e321db886bfdc691a06110620a9ddce3084a72201e

seed0.dualresident.seed7.independent.audit.json
SHA-256 eedc4401a43f885aceca28d6569b9b14b502c6bf689b3eab59122ac77a287a7c.
```

The independent replay is

```text
scratch/audit_k15_fixed_m0_biresident_model_20260729.py
```

and reconstructs the physical matching, cycles, both cyclic run families,
and all fixed windows without trusting Tseitin or quotient bookkeeping.

## 2. Exact positive statement

The model selects one second-matching edge at every lower and middle
quotient vertex.  Physical expansion gives 6,435 distinct rank-eight middle
states in 26 cyclic components of lengths

\[
3900,345,330,255^3,245^3,75,45,16^{15}.
\]

Every cyclic zero-run of every coordinate has length at least four.  The
zero-run histogram begins

\[
4^{2325},5^{915},6^{750},7^{480},8^{300},9^{345},
\]

and the exact minimum is four.  There are no missed constant-zero traces:
the smallest component has length sixteen.

The following physical target rows are complete:

1. the middle deck;
2. lower `q1`;
3. upper `q1`;
4. lower `q2`.

Thus the precise proved scope is

\[
\boxed{
\text{fixed-}M_0\text{ factor}
+\text{cyclic zero-residence four}
+\text{upper q1}
+\text{lower q2}.}
\]

The four quotient-parallel incidences omitted by the stable mapping cannot
improve this decision problem when positive residence is later imposed: each
forces an autonomous length-three or length-five component with a short
positive run.  No such extra edge is silently used by this certificate.

## 3. Exact negative boundary

This factor is not positive-resident:

\[
\min(\text{one-run})=2,
\qquad
285\text{ one-runs have length }2,
\qquad
570\text{ have length }3.
\]

Hence it has 855 short positive runs and is not bi-resident.

It also has the exact remaining protected-shadow defects

\[
\begin{array}{c|c|c}
\text{row}&\text{physical holes}&\text{quotient holes}\\ \hline
\text{upper q2 fixed window}&45&3\\
\text{lower q3 fixed window}&78&6.
\end{array}
\]

The independent arbitrary-width upper audit has exactly three missing
quotient targets, and the lower-`q3` pipeline audit has six.  Therefore this
is neither the retained all-depth PBBS factor nor a compiler-ready carrier.

## 4. Solver scope

The six sibling zero-only portfolio jobs were stopped after seed 7 reached
SAT; their existing outputs and the shared CNF were preserved.  No UNSAT
claim is made from any stopped run.  The separate corrected bi-residence
models add 20,943 positive-run clauses and remain a different decision
problem.

