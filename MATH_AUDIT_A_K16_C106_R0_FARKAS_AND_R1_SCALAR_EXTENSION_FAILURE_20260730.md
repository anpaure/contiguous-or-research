# K16 C106: exact `R=0` Farkas no-go and failure of the scalar `R=1` extension

Date: 2026-07-30  
Status: **proved for the frozen source-relative seam catalogue**

## 1. Scope

This audit reuses the exact no-capacity Farkas certificate for the old
count-105 tight face.  It does not rerun C105 and does not alter the frozen
floor-106 theorem.  The conclusions concern only the authenticated 211,604
direction-coherent seams of the length-eight K16 source.

The first conclusion is a new continuous no-go: all 243 count-106 signatures
with direct slack `R=0` are infeasible even without port capacity.  The second
conclusion is deliberately negative: the same Farkas ray cannot be extended
to `R=1` merely by adding a scalar multiple of the direct-slack equality.
This does not prove that the 405 `R=1` signatures are feasible or infeasible.

## 2. Exact `R=0` reuse

On the integer scale \(10^6\), the frozen ray has

\[
 K=118200,qquad
 (G_1,G_2,G_4)=(-1980879,2162517,1398229),
\]

and nonnegative service multipliers with

\[
                         \sum_t Z_t=132674283.
\]

Its independent raw-stream audit proves that every tight seam lying on a
directed tight cycle has nonnegative combined column.  For the original
right-hand side

\[
 (C,M_1,M_2,M_4)=(105,18,60,18)
\]

the combined value is \(-999963\).

Every C106 `R=0` normal form has

\[
 (C,M_1,M_2,M_4)=(106,20,60,18).
\]

The columns do not change, while the right-hand side changes by

\[
 K+2G_1=118200-3961758=-3843558.
\]

Therefore the new exact value is

\[
 -999963-3843558=\boxed{-4843521}<0.                 \tag{2.1}
\]

Nonnegative total direct slack zero forces every positive-flow seam to be
tight.  Every positive edge of a finite nonnegative balanced flow lies on a
directed cycle, so the frozen nonnegative columns cover the whole face.
Equation (2.1) is therefore a Farkas contradiction for nonnegative real
balanced flows, without capacity.  It excludes all (3^5=243) `R=0`
signatures at once.

## 3. Why one scalar slack multiplier cannot settle `R=1`

For C106 `R=1`, the class totals are

\[
 (C,M_1,M_2,M_4)=(106,19,60,18),
\]

so the unchanged ray has exact base right-hand side

\[
                         B_1=\boxed{-2862642}.          \tag{3.1}
\]

Suppose one adds \(\lambda\sum_e s_ex_e\) to the ray and otherwise keeps its
count, group, and cover multipliers fixed.  Arbitrary changes to the balance
potential are allowed.  On a directed closed walk, every balance potential
telescopes, so its combined cost changes only by \(\lambda\) times its direct
slack.

The frozen audit replays the following 65-seam directed closed walk:

```text
182764 93500 205798 183748 2601 10794 117908 192438
66749 207526 194273 108189 122600 198352 185730 9043
17242 147007 173135 95845 207722 174966 88569 207674
192221 81296 207622 180751 74020 207575 177017 115468
192404 86751 181270 71347 109667 77603 71830 66029
143085 137306 131488 99435 140530 197186 202644 207245
208613 201271 160246 81367 207747 211479 205661 123868
154118 207496 208377 196876 87494 117737 146640 117296
123654
```

Seam `182764` is the unique slack-one portal; the other 64 seams are tight.
Literal endpoint replay verifies closure.  The target-price occurrence census
on the walk is

\[
                         (N_1,N_2,N_4)=(11,39,10),
\]

and hence its cycle-local direct identity is

\[
 2\cdot65=11+2\cdot39+4\cdot10+1.
\]

Its five-lock syndrome is mask `8`, of Hamming weight one.  Thus it even lies
on the equality Hamming shell appropriate to a one-slack cycle.  Its exact
base Farkas cost is

\[
                         \boxed{-3319234}.              \tag{3.2}
\]

For every augmented column system to be nonnegative on closed walks,
(3.2) forces

\[
                         \lambda\ge3319234.             \tag{3.3}
\]

But the augmented right-hand side is \(B_1+\lambda\).  Combining
(3.1)--(3.3) gives

\[
 B_1+\lambda\ge-2862642+3319234
                     =\boxed{456592}>0.                 \tag{3.4}
\]

Hence no scalar slack multiplier, even together with arbitrary balance
reweighting, makes this fixed Farkas ray both column-nonnegative and
strictly negative on the C106 `R=1` right-hand side.

The witness repeats several non-lock targets.  It is therefore not itself a
component of a feasible exact-service C106 solution.  It refutes only this
scalar-ray extension.  A target-refined ray may still prove `R=1`
infeasible.

## 4. Frozen replay

```text
scratch/audit_a_k16_c106_r0_farkas_r1_scalar_failure_20260730.py
  SHA-256 0c76b1556bca4c5f19df33b1f32020ef6256b028cfb41a8db84b077170728143

scratch/a_k16_c106_r0_farkas_r1_scalar_failure_20260730.audit.json
  SHA-256 d1ed93a1bac2c2e0a57b4c9a6ecab7f7417b31a32ee640c453df2c28300aefed
  payload 2622dfca7e1e611588d0b052cb45624b275ae2f4d7b8a5c01269ec0e74bb61aa
```

The checker independently pins and replays:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

The other pinned inputs are:

```text
scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/ad_k16_c105_s0_repeat1x3_farkas_20260730.certificate.json
  SHA-256 3a8f9d1fa506b56ff2ae5d3a4463a647bfbdf4773ea5df961a3483299da2d582

scratch/ad_k16_c105_s0_repeat1x3_farkas_rawstream_20260730.audit.json
  SHA-256 3117bd8d0084337a1e854edd2f1536bea0a81991c5ebc6d1c0df116a012ab1b3
```
