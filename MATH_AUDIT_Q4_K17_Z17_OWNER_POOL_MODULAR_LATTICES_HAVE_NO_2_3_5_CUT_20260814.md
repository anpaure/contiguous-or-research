# Audit: the frozen `Z_17` owner pools have no mod-2, mod-3, or mod-5 cut

**Date:** 2026-08-14
**Status:** exact finite, pool-specific lattice audit.  This removes three
small-prime explanations for the current search difficulty; it does not
prove an integral exact cover.

## 1. Systems audited

Let `A` be the `1430`-row owner-orbit incidence matrix of a frozen finite
column pool, and let `1` be its all-one owner target.  Three literal H100
maps were audited:

```text
/dev/shm/q4z17_group100k.map.json
100,000 period-10 columns
SHA-256 ab00a2c7c9f3e76772dd40215672a6190a09f626b721f59569757656bd79104d

/dev/shm/q4z17_mixed100k.map.json
50,000 period-10 + 50,000 period-11 columns
SHA-256 087a010484418ac5ca004d485c3fb4ac1c37f7f457bf12ba9cbc32c62eef8d35

/dev/shm/q4z17_atomclosed.map.json
159,999 period-10/11 columns, including 10,000 correlated atom groups
SHA-256 a7d050a5eb63f14d69d6ecb403d014dce3c24ac250c481250015e9445bb8d93c
```

For each mixed pool the augmented matrix

\[
 \widetilde A=\begin{pmatrix}A\\r_{11}\end{pmatrix}             \tag{1.1}
\]

was also audited, where `r_11` is one on a period-eleven column and zero
on a period-ten column.  Its target on scalar face `t` is `(1,10t)` for
every `0<=t<=13`.

## 2. Exact ranks and consistency

The period-ten group-closed pool has

\[
\begin{array}{c|ccc}
p&2&3&5\\ \hline
\operatorname{rank}_{\mathbb F_p}A&1429&1430&1429\\
1\in\operatorname{col}_{\mathbb F_p}A&\text{yes}&\text{yes}&\text{yes}.
\end{array}                                                       \tag{2.1}
\]

The two mixed pools each have full owner-row rank over all three fields:

\[
             \operatorname{rank}_{\mathbb F_p}A=1430,
             \qquad p\in\{2,3,5\}.                              \tag{2.2}
\]

For each of those pools, the augmented ranks are

\[
\begin{array}{c|ccc}
p&2&3&5\\ \hline
\operatorname{rank}_{\mathbb F_p}\widetilde A&1430&1431&1430.
\end{array}                                                       \tag{2.3}
\]

Every one of the fourteen targets `(1,10t)`, `0<=t<=13`, belongs to the
corresponding augmented column space for each `p in {2,3,5}`.

These ranks are exact, not lower estimates.  For period ten, the all-one
left row annihilates every column modulo 2 and 5 because every column has
weight ten; hence 1429 is the maximum possible rank in `(2.1)`.  In the
mixed augmented system, modulo 2 or 5 the forced left relation is

\[
       \sum_{v=1}^{1430}\widetilde A_{v,*}
             -11\widetilde A_{1431,*}=0,                         \tag{2.4}
\]

so rank 1430 is maximal.  The mod-3 matrices attain literal full row
rank.  Exact modular elimination reaches these bounds, then directly
reduces each target.

## 3. Consequence and boundary

The UNKNOWN SAT/CP behavior of these pools is not explained by a parity
cut, a mod-3 cut, a mod-5 cut, or by the exact period-count congruence on
any scalar face.  In particular, adding the explicit q4 common-reserve
atom columns removes no such obstruction because the unaugmented mixed
pool was already full-row-rank over all three fields.

This is deliberately not an integer-semigroup theorem.  Higher-prime,
nonnegative, Hall, support, or chronology obstructions may remain, and
column-space consistency supplies no exact-cover certificate.

## 4. H100 artifacts

```text
scratch/audit_q4_k17_z17_pool_modular_lattice_20260814.py
SHA-256 fac0962f2f4beacdf84378e8baf12b98eedbe689c42cba254977dbde1e333b19

scratch/audit_q4_k17_z17_group100k_modular_20260814.h100.out
SHA-256 47fc7e2acbf36de0b40f3bfb512c2982f8450c9d61649f0b0bf08dd1366d803d

scratch/audit_q4_k17_z17_mixed100k_modular_20260814.h100.out
SHA-256 458a3f49f680e98868861af342709f03e40efafe1d2381bccca973b20e1a3ed7

scratch/audit_q4_k17_z17_atomclosed_modular_20260814.h100.out
SHA-256 20cd8e9206d6d5cfdf022c4e84da2d3dc8a083ef07bde1ed52c9a279f79760c3
```

Pool generators, for provenance:

```text
scratch/solve_q4_k17_z17_quotient_exact_cover_sat_20260814.py
SHA-256 2247a3fac76f7a49169b34d01f26c6d73a664b5efcd6162267a2ffb7a197a560

scratch/solve_q4_k17_z17_quotient_mixed_sat_20260814.py
SHA-256 3edc5e7f1096f8085d892da76134570413317bcabdc174dc43361e3198ee83e0

scratch/solve_q4_k17_z17_quotient_atom_closed_sat_20260814.py
SHA-256 3675d7d50c63abaa855b8479dbed7a413adbbdef6603df46a48990e792608e6f
```

All enumeration, elimination, replay, and hashing ran through SSH on H100.
The local Mac was used only for reading, editing, transfer, and Git.
