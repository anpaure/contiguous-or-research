# AD audit: exact K16 second-stage port dual and floor 101

Date: 2026-07-30  
Status: **proved in the frozen source-relative seam catalogue**.  This is a
lower bound, not an existence or optimality claim.

## 1. Frozen scope

The certificate concerns the compact directed seam ledger

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

whose embedded source-factor SHA-256 is

```text
6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

The ledger has 12,870 transition ports and 211,604 directed seams.  Its
fixed service bank consists of 45 lower-q2 defects and 48 upper-q3 defects,
so there are 93 targets in total.  For a seam (e:u\to v), let (H(e)) be
the set of distinct defects supplied by that seam.

Let (x_e\ge0) satisfy the transition-port balance equations

\[
 \sum_{e:\,\operatorname{tail}(e)=v}x_e
 =\sum_{e:\,\operatorname{head}(e)=v}x_e
 \quad(v=0,\ldots,12869),                                      \tag{1.1}
\]

and the 93 additive service rows

\[
 \mu_t:=\sum_{e:\,t\in H(e)}x_e\ge1
 \quad(t\in\mathcal H).                                       \tag{1.2}
\]

Write (C=\sum_e x_e).  The final ceiling uses that (C) is integral for
an integral seam selection.  No q1, separation, reverse-edge, survivor,
residence, component-connectivity, or deeper-shadow row is used.

## 2. Exact composite certificate

The previously audited scale-20 certificate gives nonnegative integer
target weights (w_t), with

\[
                   \sum_{t\in\mathcal H}w_t=1899,              \tag{2.1}
\]

and an integer port potential (phi_v).  The second-stage certificate gives
nonnegative integer prices (A_t) and an integer potential (P_v), with

\[
 \sum_t A_t=735,
 \qquad A_t\in[0,105],
 \qquad P_v\in[-266,154].                                     \tag{2.2}
\]

There are 44 positive (A_t).  The denominator of the second stage is
seven.  Define the composite target weights and potential by

\[
 B_t:=7w_t+A_t,
 \qquad \Phi_v:=7\phi_v+P_v.                                  \tag{2.3}
\]

Thus (B_t\ge0) for every target and

\[
             \sum_{t\in\mathcal H}B_t
             =7\cdot1899+735=14028.                            \tag{2.4}
\]

### Exact all-arc inequality

Every one of the 211,604 directed seams satisfies

\[
 \boxed{\quad
    \sum_{t\in H(e)}B_t
    \le 140+\Phi_{\operatorname{head}(e)}
              -\Phi_{\operatorname{tail}(e)}.
 \quad}                                                        \tag{2.5}
\]

The direct integer replay found minimum slack zero, maximum slack 553, and
34,031 tight arc rows.  Hence (2.5) includes the zero-provider seams; it is
not merely a provider-only check.

## 3. Sign audit and derivation

The base reduced cost is

\[
 \rho(e)=20+\phi_{\operatorname{head}(e)}
             -\phi_{\operatorname{tail}(e)}
             -\sum_{t\in H(e)}w_t\ge0.                         \tag{3.1}
\]

The exact second-stage row is

\[
 \sum_{t\in H(e)}A_t
 +P_{\operatorname{tail}(e)}-P_{\operatorname{head}(e)}
 \le7\rho(e).                                                  \tag{3.2}
\]

This orientation is decisive.  Substituting (3.1) in (3.2), then adding
(7\sum_{t\in H(e)}w_t), gives

\[
 \sum_{t\in H(e)}(7w_t+A_t)
 \le140+(7\phi+P)_{\operatorname{head}(e)}
          -(7\phi+P)_{\operatorname{tail}(e)},
\]

which is exactly (2.5).  The checked integer slack was

\[
 7\rho(e)-\sum_{t\in H(e)}A_t
 -P_{\operatorname{tail}(e)}+P_{\operatorname{head}(e)},       \tag{3.3}
\]

so the implementation and theorem use the same signs.

## 4. The floor-101 theorem

### Theorem 4.1 (weighted service-plus-balance cut)

Every nonnegative (x) satisfying (1.1)--(1.2) obeys

\[
                         140C\ge14028.                          \tag{4.1}
\]

Consequently every integral selection in the frozen catalogue has

\[
                              C\ge101.                          \tag{4.2}
\]

#### Proof

Multiply (2.5) by (x_e\ge0) and sum over all seams.  By (1.1), the
potential contribution telescopes with the audited orientation:

\[
 \sum_e x_e\bigl(\Phi_{\operatorname{head}(e)}
                    -\Phi_{\operatorname{tail}(e)}\bigr)
 =\sum_v\Phi_v(\operatorname{in}_x(v)-\operatorname{out}_x(v))=0.
                                                                    \tag{4.3}
\]

Therefore

\[
 \sum_t B_t\mu_t
 =\sum_e x_e\sum_{t\in H(e)}B_t
 \le140\sum_e x_e=140C.                                      \tag{4.4}
\]

All (B_t) are nonnegative and every (mu_t\ge1), even when a target is
supplied repeatedly.  Hence

\[
 140C\ge\sum_tB_t\mu_t\ge\sum_tB_t=14028.                    \tag{4.5}
\]

This proves the fractional bound

\[
 C\ge\frac{14028}{140}=\frac{501}{5}=100.2.
\]

For integral (C), this is (C\ge101).  QED.

The same calculation in two stages says that (3.2) gives total reduced
cost at least (735/7=105), while the base certificate contributes 1899:

\[
                  20C\ge1899+105=2004.                         \tag{4.6}
\]

Equation (4.5) is preferable because it makes target multiplicity harmless
without any equality-face case split or cycle decomposition.

## 5. Localization of the old 66/67/68 frontier

The staged row-family conclusion is exact:

1. Service/provider incidence alone had the much weaker set-cover floor 56.
2. Adding only transition-port balance already produced the earlier
   scale-20 cut (20C\ge1899), hence (C\ge95).
3. The exact denominator-seven refinement uses **the same two row families**
   and yields the single implied inequality (4.1), hence (C\ge101).

Thus the failure at exact 67 is not caused by q1, residence, separation,
survivor, connectivity, or a hidden physical-master row.  It is already
forced in the relaxation consisting solely of the 93 service inequalities,
nonnegativity, and transition-port balance.  In particular the former
"extra two above 66" is subsumed by a 35-unit gap: every count through 100
is excluded in this frozen catalogue.

This is a compact Farkas consequence, not a claim that its target support is
inclusion-minimal.

## 6. Independent binary replay and provenance

The current exact generator and regenerated certificate are

```text
scratch/audit_k16_second_stage_cycle_dual_exact_20260730.py
  SHA-256 843d36429b14b543660682f7d22488c2c944f273028e5f995805229d4b29b911

scratch/k16_second_stage_cycle_dual_exact_20260730.audit.json
  SHA-256 1a36ce80af98b5db58ce55a4401e9ccba8bea1f12fd0af2ee73e0a932fdbe285
  payload 2f39d037582e16f36234a6bd0b9292f6073188d2ea70fc171187e13a5e348426
```

The generator imports the established catalogue parser, so it is not by
itself a parser-independent audit.  A separate standard-library verifier
imports neither that parser nor either generator.  It reads the compact
binary format directly, authenticates the binary and both input
certificates, checks all 211,604 arc rows in integers, checks the composite
row independently, and verifies the telescoping signs and final arithmetic:

```text
scratch/threadB_verify_k16_second_stage_cycle_dual_floor101_20260730.py
  SHA-256 53dfa7fb529eeda7b22a24eeaf07c469306117584cf5495c8526e373ecde38bc

scratch/threadB_k16_second_stage_cycle_dual_floor101_20260730.audit.json
  SHA-256 e095fe41f900c186298c055c5bab517e414f94f2647392c4006c2aab8d140c12
  payload ca641a3639ec5e09b95aa1788b2d86b727f1d9946539beb765e26ed7a20cfe92
  status  GO_EXACT_RAW_REPLAY_AND_TELESCOPING_VERIFIED
```

The AD verifier prepared specifically for this audit gives a third direct
binary replay with the same row census and arithmetic:

```text
scratch/audit_ad_k16_second_stage_cycle_dual_floor101_direct_binary_20260730.py
  SHA-256 b7b0d41547210962ad5372c61384e7e2f0d66b02c9ecc056e06549f25645d574

scratch/ad_k16_second_stage_cycle_dual_floor101_direct_binary_20260730.audit.json
  SHA-256 216d5a4d09d1da110fc1744600f55f6f6021ed9a32f0f5002035b0776d0b86cb
  payload 0e388f40b2502f6213ee9dbc5932d21af1bd27952a82c542b319b664300f5853
  status  PASS_INDEPENDENT_DIRECT_BINARY_FLOOR101
```

That independent replay pins the older exact-certificate file

```text
scratch/k16_second_stage_cycle_dual_exact_floor101_20260730.audit.json
SHA-256 15816ff538bfcc5005782f8eaa7395293d529bfd35ba38b0cd11a0d8467069a4
```

whose recorded generator SHA is `23c81c...`, rather than the current source
SHA above.  This is a provenance-hygiene defect in that older file, not a
mathematical defect: direct comparison shows that its target-price vector,
port-potential vector, reduced-cost histogram, and exact-slack histogram are
identical to the regenerated current certificate.  The regenerated file
correctly records the current generator SHA, and the independent raw replay
authenticates and checks the same integer certificate row by row.

The predecessor five-target partition certificate is frozen at

```text
scratch/audit_ad_k16_four_target_cycle_partition_20260730.py
  SHA-256 421ded9f8d0130873f0cd84335888f9a19a2e2b076e97847d584dd727567085c

scratch/ad_k16_five_target_39791_36343_cycle_partition_20260730.audit.json
  SHA-256 7bd7b9a688dc7d6eee7196331f2c1604271ee4a2433facdd8627bb6b1d7c7b91
  payload bb10bb399f746d07f78f3b85a60a94f550627d68befb22d98e64a1f8c808e0aa
```

It proves the earlier floor 99 in the same ledger.  The all-arc composite
dual above is stronger and supersedes it.

## 7. Sharp boundary

What is proved is

\[
 C\ge101
\]

for endpoint-balanced integral selections covering the 93 fixed defects in
the SHA-`832ddd` source-relative direction-coherent q<=3/upper-width-four
catalogue.

What is **not** proved is feasibility at 101, optimality of 101, a no-go for
the broader WIDTH45 catalogue, or a no-go for reverse seams, interacting
multi-cut windows, arbitrary compound rethreads, another source factor, or
unrestricted K16.  Any such enlargement needs a fresh all-arc replay.
