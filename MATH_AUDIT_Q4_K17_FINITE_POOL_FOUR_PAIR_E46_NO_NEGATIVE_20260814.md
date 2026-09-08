# Independent audit: exact finite-pool q4 k17 E46 four-pair boundary

**Date:** 2026-08-14

**Verdict:** **PASS**.  On the frozen
204,462-reflected-pair instance, no negative replacement of four selected
pairs by four distinct unselected pairs exists at the audited E46 state.
Self lifts remain fixed.  The best tested exchange has value `+8`.

## 1. Audited implementation

The implementation is a direct realization of the frozen complete four-
pair/general-depth exclusion recurrence.

```text
scratch/search_q4_k17_z17_reflection_exact_four_pair_exchange_20260814.py
sha256 46331d5e198113914196bf4dff7964ef9e9223214d7534436524b231e5c44a11
```

For each of the `binom(54,4)=316,251` outgoing faces, it computes the exact
constant `c_R`, every directed score `h_R`, and the first four indexed
score entries.  It applies only the proved face, singleton, pair, and
triple exclusion cuts.  Incoming indices are unselected and distinct, and
the scan uses one canonical increasing order.  Every surviving fourth
candidate restores its three omitted prefix overlaps before the exact
energy sign is taken.  Thus no negative quadruple can be pruned.

## 2. Exact E46 finite-face result

The face cuts retain 975 outgoing faces and 34,451 candidate incidences.
They generate 10,877,124 retained pair prefixes, 14,193,069 retained
triple prefixes, and only 15 literal quadruple tests.  The least exact
delta among these 15 negativity-capable leaves is

```text
remove 21378,189651,194629,199463
add    189699,198396,199861,200077
Delta  +8.                                                     (2.1)
```

The source histogram is `23x0,634x1,23x2`, hence energy 46.

```text
scratch/audit_q4_k17_z17_augmented185k_e46_exact_four_pair_20260814.h100.json
sha256 ddce4f8502f70766f32b2498412f319767bae3fa987c4ad2fa48567366b0f0bf

E46 source state sha256
e208ae02dfcfc596829145ae657bb36b1f8cf6afb843d31dc8d72e9ec1aeff49

finite instance sha256
3b3a666170b2b17a57a5ad11094e6ebbdd759501a9e4ecb50ddee0a9eb455dd2
```

## 3. Independent full replay

The independent audit reconstructs the instance and source loads, scans
all 316,251 outgoing faces, recomputes every exact distinct exclusion,
checks every reported retained prefix and literal quadruple, and verifies
the least tested-leaf value.

```text
scratch/audit_q4_k17_z17_finite_pool_four_pair_exchange_e46_20260814.py
sha256 66c5a1ca0f0b322028bee0bd0e9b5b89949ca679246ab590c46cec0dfc0dd5ac

scratch/audit_q4_k17_z17_finite_pool_four_pair_exchange_e46_20260814.h100.out
sha256 8f151b6ee3ba6b6554d10176f6bc34cebb9a6e15b724613161135de91c9ca818
status PASS
```

## 4. Scope boundary

The no-go is only a four-reflected-pair statement for this finite pool and
fixed self selection.  It does not rule out absent columns, a neutral
pivot followed by descent, a mixed pair/self four-exchange, five-or-more
configurations, changing the fixed matching, or an owner/lower-ticket
exact cover.

All computation, replay, and hashing ran on H100.
