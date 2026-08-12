# Exact common Farkas certificate excluding every C106 R1 signature

Date: 2026-07-30

## Scope

This theorem concerns only the frozen K16 length-eight source and its
211,604 authenticated directed seams.  It is a theorem about the
balance/service projection used for source-relative rethreading.  It is not a
lower bound for another carrier, an unrestricted move family, or `nu(16)`.

## The R1 common relaxation

At cut count 106 the five-lock normal form satisfies

```text
repeat weight + direct-dual slack = 5.
```

On the `R=1` face, exactly four lock groups repeat one weight-one target and
one lock group spends its unit as seam slack.  Therefore every one of the 405
fixed signatures satisfies the following equations.

1. Every one of the 78 nonlock defects has service exactly one.
2. Total service over the fifteen lock defects is `15+4=19`.
3. Total selected seam mass is 106.
4. Total direct-dual seam slack is one.
5. Endpoint flow is balanced at every port.

The fixed choice of the four repeated lock targets imposes additional rows,
but the five equations above are common to all signatures.  Seam values are
allowed to be arbitrary nonnegative reals.  Port capacity, separation, q1,
reverse-edge, residence, survivor and deeper-shadow rows are all omitted.

## Exact certificate

Let `E_cyc` be the seams whose endpoints lie in one nontrivial strongly
connected component of the raw seam digraph (including a self-loop, if one
existed).  Exact SCC replay gives

```text
|E_cyc| = 211,469,
excluded condensation-DAG seams = 135.
```

A nonnegative balanced circulation gives zero mass to every excluded seam,
so this pruning is exact.

The certificate supplies integers

```text
P_v                 for every port v,
a_t                 for every nonlock defect t,
L                    for total lock service,
kappa                for seam count,
eta                  for direct slack.
```

For a seam `e:u->v`, let `H(e)` be its serviced defect set, let `h_L(e)` be
the number of lock defects in `H(e)`, and let `s(e)` be its exact nonnegative
direct-dual row slack.  Direct raw-binary replay proves, for every
`e in E_cyc`,

```text
P_u - P_v
+ sum_{t in H(e), t nonlock} a_t
+ L*h_L(e) + kappa + eta*s(e) <= 0.                 (1)
```

The maximum left-hand side in (1) is exactly zero.  Exactly 5,106 seams are
tight.  Meanwhile the common R1 right-hand side is

```text
Delta = sum_t a_t + 19*L + 106*kappa + eta
      = 309451086187243526028429093040863660533091962880
      > 0.                                           (2)
```

Suppose a feasible nonnegative balanced R1 flow existed.  Multiply (1) by
its seam masses and sum.  The port-potential terms telescope by balance.
The four common service/count/slack equations make the resulting sum equal
to `Delta` in (2), while (1) makes it nonpositive.  This is a contradiction.

Hence:

> **Theorem.** The full continuous common R1 relaxation is infeasible.
> Consequently none of the 405 fixed C106 R1 signatures has a fractional
> balanced service flow, even before port capacity or any physical row is
> imposed.

## How the exact ray was recovered

Native HiGHS first produced a numerical infeasibility ray using only the rows
listed above.  Its 5,106 tight eligible seams form 309 undirected components
with 223 fundamental cycle equations in 81 non-potential multipliers.  The
exact integer cycle-feature matrix has rank 76 and a five-dimensional
integer nullspace.  The numerical direction was reconstructed inside that
nullspace, so every tight cycle identity remained exact; component gauges
were then chosen integrally and all 211,469 seam columns were replayed over
the integers.

The proof does not rely on the numerical solver: a separate verifier parses
the frozen binary directly and checks the emitted integer inequality and RHS.

## Artifacts

```text
scratch/k16_floor106_r1_full_farkas_exact_20260730.audit.json
SHA-256 7644ac7f4cf8a20bb87be935f9522931740d9c4c729db2b4a96f9d23c8b11bd7
payload 9048eb636bab8a14c38774e60246266eb65a73897455f0c5bb76f83567f8c649

scratch/exactify_k16_floor106_r1_full_farkas_20260730.py
SHA-256 434a88d53e3bf2594af2bb43e8c90f13863e642bbced7b40cceee9d798a0d5d7

scratch/k16_floor106_r1_full_farkas_exact_independent_20260730.audit.json
SHA-256 ad333e4a4217a7ea2610c59b3154ba8602b75680cd71242d7dd85826b314015b
payload c40e318e079630eac785c08365038b9de2b9b4e8b15b48d19bb77a6d59ebfd54

scratch/verify_k16_floor106_r1_full_farkas_exact_independent_20260730.py
SHA-256 5d41ea24b7493c5bc1eedbbc244aba4c7b133014d5bf26269b4cf6efbe4e8d7e
```

## Consequence for construction

The exact C106 atlas now has two closed slack layers:

```text
R=0: all 243 signatures excluded by the earlier exact Farkas theorem;
R=1: all 405 signatures excluded by the common certificate above.
```

Thus the first possible fractional C106 construction face is `R=2`.  This is
stronger than the earlier binary-WLOG truncated R1 census and supersedes its
merely numerical interpretation.

