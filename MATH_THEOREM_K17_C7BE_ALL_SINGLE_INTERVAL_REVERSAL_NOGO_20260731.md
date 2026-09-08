# K17 c7be: every single interval reversal is U-shore infeasible

Date: 2026-07-31  
Status: solver-free composition of two exhaustive rethread censuses  
Scope: fixed c7be parent and one-occurrence-per-q1-colour U shore only

## Theorem

Let \(T=(T_0,\ldots,T_{12869})\) be the authenticated c7be K16 rank-eight
chronology.  Reverse any one contiguous interval of its vertices, including
a prefix, a suffix, an internal interval, the whole word, or a degenerate
interval.  If the resulting chronology is not a Johnson path or loses a
rank-nine adjacent-union colour, it cannot supply the required K17 U shore.
If it passes those two gates, its one-occurrence-per-colour U shore still
cannot cover all old-coordinate targets of ranks at least ten.

### Proof

There are four cases.

1. A degenerate interval leaves the source unchanged.  The exact
   0x0bf5 opposite-choice core already closes it.
2. A proper prefix or suffix reversal has one new seam.  The exhaustive
   one-ended audit finds 126 Johnson-legal rows.  Of these, 104 lose a
   required q1 colour.  All 22 palette-complete rows retain both the 0x0bf5
   and 0x1ce7 opposite-choice cores.
3. A proper internal reversal has two new seams.  The exhaustive incremental
   quotient finds 19,856 Johnson-legal, palette-complete rows.  Of these,
   19,779 retain both cores, 60 retain the 0x0bf5 core, and 17 retain the
   0x1ce7 core.  No row breaks both.  Any Johnson-legal row omitted by this
   quotient is q1-incomplete and already fails the deck identity.
4. Reversing the whole word reverses the raw edge-colour sequence.  Reversing
   all chosen occurrence positions is a bijection on U-shore transversals
   and on their consecutive OR witnesses.  Hence the source opposite-choice
   core persists by reflection.

Every single-interval reversal belongs to one case, proving the claim.
\(\square\)

## Consequence

This is the first complete genuinely rethreaded c7be K17 scout.  The minimal
remaining c7be topology is not another single 2-opt reversal: it must use at
least two independently moved intervals/more than two old cuts, a
split/interleaved or value-changing operation, or a different parent.

The result concerns the U-shore upper deck.  It makes no claim about
unrestricted K17 and does not build a lower Hall or common-Q model for an
upper-infeasible carrier.

## Components

One-ended theorem:

    MATH_THEOREM_K17_C7BE_ONEENDED_RETHREAD_OCCURRENCE_NOGO_20260731.md
    SHA db38182984475b4ec6784378623c1673820eb8177d27691c924affca1070d3ef

Primary one-ended audit:

    scratch/audit_k17_c7be_oneended_rethread_nogo_20260731.py
    SHA 583f4364b2f31b707a6954322e8e2d3d34f38964634fd6b0c514b4ddcfb2d008

    scratch/k17_c7be_oneended_rethread_nogo_20260731.audit.json
    SHA 9bbd1de2dfd4259191608c39679876c6f14cfd62ce84eb5a34f617b00fefe186
    payload fb8a8509f1279a5305b06b00fddfcba91aaec37ba62326c7efa3680ab6ead31c

Independent one-ended audit:

    scratch/audit_k17_c7be_oneended_rethread_independent_20260731.py
    SHA 6a43c9ae4853db4b2c094b23f1954868ddbd1e06caf0ded511dcfad00a45160b

    scratch/k17_c7be_oneended_rethread_independent_20260731.audit.json
    SHA 8ef308623b2fc63c85a78f7abc42d9c03855b0d1b7a0d7a4eb95484f38dc4484
    payload 2a1154ea0f9a4edc14e4620c7657b1457728416f10c063d125b3dc51ddb25556

Internal theorem:

    MATH_THEOREM_K17_C7BE_U_INTERNAL_SINGLE_REVERSAL_OPPOSITE_CORE_NOGO_20260731.md
    SHA 76601c4f8c1fd7aea7ac71a3e1d0edb85bd930ddd5d89d2783509d46b3440816

Internal audit:

    scratch/audit_k17_u_single_reversal_quotient_20260731.py
    SHA 43521afdc3c3ef0afb3e2ae321282a6a1b2098f998c8ec01d114d22ef051229

    scratch/k17_u_single_reversal_quotient_20260731.audit.json
    SHA bc1d4dbc871b30907b277d47817c2b9f74b671d201176da77134cb22ef051229
    payload e44b3421119f8823631ee8cf89ee0bdf529124137129b44dae43ddf4c8f7ab78
