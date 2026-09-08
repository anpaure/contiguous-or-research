# Verified literal lifts at dimensions 18 and 20

2026-09-08. Two prescribed finite constructions were materialized and
exhaustively checked on h100. No search, alternative order, or shortening
was attempted. Both executions returned PASS and exited.

## Exact lift and its finite proof

For any nonempty universal word `A_1,...,A_N` on [k], and a new
coordinate z, emit

    A_1,...,A_N, {z}, A_1 union {z},...,A_(N-1) union {z}.

The length is exactly 2N. Every old target retains its original witness.
For a target T union {z}, choose an old T witness [i,j]. If j<N,
use the corresponding lifted interval; if j=N, use the old suffix
[i,N] followed by the bridge {z}. The bridge alone realizes {z}.
Thus the word is universal and `nu(k+1)<=2nu(k)` for k>=1.

This is the exact existing construction in `MASTER_HANDOFF.md`,
section 3.9 equation (3.44), around lines 1343–1349, and section 2.2
equation (2.2) with d=0, around lines 404–419. The empty k=0 base is
not an input to this construction.

## Materialized results

| Dimension | Verified input length | Output length | Required targets | Missing | Lower bound | Gap | Percent above lower bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 18 | 24668 | 49336 | 262143 | 0 | 48623 | 713 | 1.466384221459% |
| 20 | 94161 | 188322 | 1048575 | 0 | 184759 | 3563 | 1.928458153595% |

The k18 input was the retained supplied word
`answers/k17_upper24668.word`, SHA-256
`22af061610f9c6cb4708ccca77c8d8008f251a1cc40f92858ca79bf7ad2ffff6`.

The k20 input was the fixed canonical k19 word independently generated
and certified by `exact_b_finite_frontier`, with remote source
`/home/amodo/exact-b-k19-height-adaptive-20260908/k19_height_repaired94161.word`
and SHA-256
`1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224`.

The output bodies are retained as:

* `answers/k18_upper49336.word`, SHA-256
  `cdecac783ee47f183e3a0559f3e1860d07781f4fe4a3c888bccc27b083c45ca3`;
* `answers/k20_upper188322.word`, SHA-256
  `0d42106351f630eda5693e91a246ceb738f0704004a38b803eba8456aeec3874`.

They are one decimal mask per line, with coordinate x represented by
bit x-1. All letters are nonzero.

## Independent verification of every ordinary interval target

The standalone script is
`scratch/verify_exact_trimmed_lift_k18_k20_20260908.py`.
It checks the exact input checksum, dimension, integer encoding and
length; applies the prescribed lift; writes the output; then reads that
serialized output back for the actual verification.

Its first pass computes all distinct suffix ORs at each endpoint,
retaining one literal start/end witness per OR. This is the exact
recurrence `R_j={A_j} union {S union A_j:S in R_(j-1)}`. Deduplicating
identical ORs preserves all future extensions. The suffix targets form
a nested chain, so at most k survive at one endpoint.

The second pass builds a separate OR segment tree directly from the
emitted word. It checks the inclusive endpoint bounds and re-evaluates
every recorded witness. It then confirms that every integer mask from
1 through `2^k-1` is present. All 262143 k18 witnesses and all 1048575
k20 witnesses passed this independent range-OR calculation.

Compact reports are retained at

* `scratch/k18_height_adaptive_20260908/k18_upper49336_verification.json`;
* `scratch/k20_height_adaptive_20260908/k20_upper188322_verification.json`.

No large witness JSON was written. The exact script and word bodies
reproduce the complete check. Both mathematical processes ran in
`/home/amodo/exact-b-k18-k20-exact-lift-20260908/`, each with 120 CPU
seconds, 150 wall seconds and 2 GiB address-space limits.

## Independent lower-bound arithmetic

A separate tiny exact-integer h100 check maximized the handoff's
`binom(k,s)+tau_s` over every rank s for k=18,19,20. It had 2 CPU
seconds, 10 wall seconds and 128 MiB limits, and returned:

| k | Maximizing rank | W | Lower-rank target count | Delay | B(k) |
|---:|---:|---:|---:|---:|---:|
| 18 | 9 | 48620 | 106761 | 3 | 48623 |
| 19 | 10 | 92378 | 262143 | 3 | 92381 |
| 20 | 10 | 184756 | 431909 | 3 | 184759 |

For example the capacities at delay two and three are respectively
97243 and 145866 at k18; 184759 and 277140 at k19; and 369515 and
554274 at k20. Each listed lower-target count lies strictly above the
first and at or below the second. No optimality claim is made for the
new upper bounds.
