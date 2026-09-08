# Audit of the RF495 blocker-run and three-port service theorem

**Date:** 2026-07-30  
**Status:** PASS after one adversarial correction; exact source-relative scope

## 1. Scope audited

This audits

```text
THREAD_A_K16_RF495_TRIWINDOW_BLOCKER_RUN_DUAL_AND_SHARP_SERVICE_20260730.md
SHA-256 b419f2a9efbeb1a7b53bc7da953ac2bffdd65bf1dfd852a5bdfd89dbc5c7feb2
```

against the frozen parent, cell ledger, literal word, and the independently
authenticated active-kernel support-three theorem.  No stochastic search,
SAT solve, or new heavy enumeration was run for this audit.

## 2. Frozen-source audit

The parent and cell hashes are

```text
parent  4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
cells   6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

Independent reconstruction gives length `12873` and word hash

```text
9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6.
```

The compressed ending-OR recurrence gives holes

```text
0x18e7, 0x3de7, 0x9e20
```

and maximum live suffix-state count `12`.  The two fixed bodies have ORs
`0x7fff,0xffff`, shortest saturating prefix/suffix lengths `(11,19)` and
`(13,20)`, and leave exactly `70` residual targets.  The literal occurrence
histogram on those targets is `0^3 1^60 2^6 3^1`.  Extension radii 20 and 40
both collapse to exactly `395` full Boolean classes.  Thus the theorem's
locality and catalogue-completeness claims pass independently.  Exactly
`227` classes are legal for at least one of the 70 residual targets; the
remaining 168 are generic but residual-irrelevant.

## 3. Duality audit

For a fixed permitted support `E`, every target outside
`H union D_E` has an unchanged avoiding witness, and every target outside
the 70-row body complement has a fixed-body witness.  Intervals with equal
`(S_E,F_E)` give the same OR under every assignment, so the injectivity and
Hall claims are necessary.

For selected classes, every physical cell value is contained in the
intersection `K_p` of the targets using it.  Replacing the physical values by
the maximal masks `K_p` cannot overshoot any selected target, and the
displayed demand equations are exactly what remains for equality.  Assigning
the maximal masks proves sufficiency.  The bit-blocker reformulation is
equivalent coordinatewise.  This matches the independently proved
arbitrary-collar core gate and the RF495 `U/R` active-kernel criterion.

Corollary 3.2 uses the already frozen support-three recurrence rather than a
new computation.  Its three cited hashes were checked byte-for-byte.  The
state rows are exactly the aggregated form of the blocker equations, so the
conclusion "every full completion changes at least four cells" has the same
source-relative scope as the authenticated theorem.

## 4. Pure service and monotone audits

For `A=0x18e7 subset B=0x3de7`, the extension mask is `0x2500`.  Removing
one candidate port and taking its maximal unchanged `B`-clean component gives
exactly the corridor table in Lemma 4.1: `0x2100`, `0x0400`, or zero.  No row
supplies `0x2500`.

For `C=0x9e20`, the four adjacent fixed boundary cells are

```text
0x3104, 0x0004, 0xb088, 0x8a4a,
```

with nonzero forbidden parts `0x2104,0x0004,0x2088,0x004a`.  Hence a
`C`-witness is window-local.  The only unchanged compatible high carrier is
`0x8000`, and it lacks bit 9.  Therefore one edit is exclusive to `C`, and
the one-port lemma proves the sharp lower bound of three service edits.

The materialized sharp service word has hash

```text
2adc27595d03b4cff964760dbc3c1dc9bfccd922929eeaab2fc0e30764c37143
```

and differs from the source only at positions `0,2,12872`.  Independent
literal replay verifies the three advertised witnesses and exactly the
twelve displayed collateral debts.

For the monotone theorem, the complete window-local old-OR lists contained
in `0x9e20`, `0x8000`, and `0x1e20` are respectively

```text
{[6435,6435]=0x8000, [12872,12872]=0x1e20},
{[6435,6435]=0x8000},
{[12872,12872]=0x1e20}.
```

Monotone additions therefore cannot install `0x9e20` without irrecoverably
losing one of the other two residual targets.  The all-support monotone
no-go passes.

## 5. Adversarial correction

An initially proposed second protected branch claimed that the route

```text
p12871: 0x0a44 -> 0x8000
```

made rehosting `0x1e64` require another edit carrying bit 9.  This inference
is false: changing `p6435` to `0x0020` gives

```text
OR[6433,6435] = 0x0004 OR 0x1e40 OR 0x0020 = 0x1e64.
```

The theorem note was corrected before freezing and now explicitly records
this counterexample.  The central-sentinel branch remains valid: after
`p6434:0x1e40 -> 0x1e20`, no unchanged cell in any accessible clean corridor
both lies below `0x1e40` and supplies bit 9, so a second bit-9 edit is forced.

## 6. Final audit boundary

The audited note proves:

- the exact 70-row/395-class blocker-run completion criterion;
- the authenticated four-change lower bound inside the RF495 fibre;
- a human proof that hole service alone needs three changes;
- a sharp three-change service macro with twelve exact debts; and
- impossibility of every all-addition completion.

It does not decide arbitrary nonmonotone reassignment on four through
eighteen free cells, does not normalize arbitrary length-12,873 words to
RF495, and does not change the bracket

```text
12873 <= nu(16) <= 12874.
```
