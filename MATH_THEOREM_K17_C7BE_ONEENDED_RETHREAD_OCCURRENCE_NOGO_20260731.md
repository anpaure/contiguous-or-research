# K17 c7be one-ended rethreads retain both opposite-choice cores

Date: 2026-07-31  
Status: solver-free exhaustive no-go for one-ended reversals  
Scope: authenticated c7be K16 parent only; no unrestricted K17 claim

## 1. Result

Let

\[
T=(T_0,\ldots,T_{12869})
\]

be the authenticated c7be rank-eight chronology of SHA

    c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.

Consider every nontrivial prefix or suffix reversal,

\[
\operatorname{rev}(T_0,\ldots,T_r)\Vert
  (T_{r+1},\ldots,T_{12869})                              \tag{1.1}
\]

and

\[
(T_0,\ldots,T_{\ell-1})\Vert
  \operatorname{rev}(T_\ell,\ldots,T_{12869}).            \tag{1.2}
\]

Require the sole new boundary edge to be Johnson-legal.  There are exactly
63 legal prefix rows and 63 legal suffix rows.

Of these 126 genuinely rethreaded parent chronologies:

- 104 lose one required rank-nine adjacent-union colour;
- 22 retain the complete rank-nine palette;
- 12 of those 22 also retain every K16 arbitrary-upper target; and
- all 22 palette-complete rows retain both exact opposite-choice cores.

Consequently no one-ended reversal of this parent produces a feasible
one-occurrence-per-colour U shore.  The next c7be-derived topology needs at
least two old cuts, a value/domain-changing operation, or a different source.

## 2. Exhaustive seam reduction

A prefix reversal preserves every internal undirected edge and changes only

\[
(T_r,T_{r+1})\longrightarrow(T_0,T_{r+1}).                \tag{2.1}
\]

A suffix reversal similarly changes only

\[
(T_{\ell-1},T_\ell)\longrightarrow
  (T_{\ell-1},T_{12869}).                                 \tag{2.2}
\]

Thus the new chronology is a Johnson path exactly when the displayed new
edge differs in two coordinates.  Each endpoint has 64 Johnson neighbours;
removing the trivial unchanged boundary leaves 63 nontrivial candidates on
each side.

Only one adjacent-union occurrence is removed and one is added.  The complete
rank-nine palette therefore survives exactly when the removed colour has a
second occurrence or equals the added colour.  Literal multiplicity replay
leaves 10 prefix and 12 suffix rows.  No heuristic filter is used.

## 3. Exact occurrence core

For a palette-complete rethread, let \(c_i=T_i\cup T_{i+1}\) be its raw
rank-nine edge-colour sequence.  The U shore chooses one occurrence of each
distinct colour and orders the choices by raw position.

For a target \(S\), a raw interval \(I\) supports some consecutive selected
U witness exactly when:

1. no blocker colour \(c\not\subseteq S\) has its whole occurrence domain
   trapped in \(I\); and
2. the union of compatible colours with an occurrence in \(I\) is \(S\).

The choices are independent across colours, so these conditions are
necessary and sufficient.  Moreover \(I\) forces colour \(c\) to occurrence
\(p\) exactly when it contains no other occurrence of \(c\) and the other
compatible colours fail to cover \(S\).

The audit enumerates every such interval for four targets on all 22 rows.
In every row:

- targets 0x1bf5 and 0x0ff5 force distinct occurrences of colour 0x0bf5;
- independently, targets 0x1def and 0x3de7 force distinct occurrences of
  colour 0x1ce7.

Since the U transversal selects each colour exactly once, either pair is a
contradiction.  A one-ended reversal can move the occurrence positions, but
it never removes the forced opposition.

## 4. Other gates and scope

The arbitrary-width spectrum is rebuilt literally for every
palette-complete parent and first-occurrence U word.  Twelve parents retain
all old upper targets; all twelve still fail the occurrence core.  Across
the 22 rows, the smallest first-occurrence U-upper deficit is 215.

The canonical tail-start run frontier is also rebuilt for the raw K17
concatenation.  Its smallest sum is 40,703, far above K17 slack 7,401.
This is corroboration only: the occurrence core already proves the U-shore
no-go independently of a schedule.

The theorem closes exactly one prefix or suffix reversal.  It does not close
an internal two-ended reversal, a multiblock rethread, a value-changing
operation, a different source, or unrestricted K17.  Lower Hall and common-Q
are not built for rows already impossible on their upper shore.

## 5. Frozen audit

    scratch/audit_k17_c7be_oneended_rethread_nogo_20260731.py
    SHA 583f4364b2f31b707a6954322e8e2d3d34f38964634fd6b0c514b4ddcfb2d008

    scratch/k17_c7be_oneended_rethread_nogo_20260731.audit.json
    SHA 9bbd1de2dfd4259191608c39679876c6f14cfd62ce84eb5a34f617b00fefe186
    payload fb8a8509f1279a5305b06b00fddfcba91aaec37ba62326c7efa3680ab6ead31c

The JSON stores all 22 palette-complete rows, their rethreaded-word hashes,
upper deficits, both core certificates, and run frontiers.  It also hashes a
compact digest over all 126 legal rows.  A second implementation independently
reproduces the 126/22/12 census and both cores:

    scratch/audit_k17_c7be_oneended_rethread_independent_20260731.py
    SHA 6a43c9ae4853db4b2c094b23f1954868ddbd1e06caf0ded511dcfad00a45160b

    scratch/k17_c7be_oneended_rethread_independent_20260731.audit.json
    SHA 8ef308623b2fc63c85a78f7abc42d9c03855b0d1b7a0d7a4eb95484f38dc4484
    payload 2a1154ea0f9a4edc14e4620c7657b1457728416f10c063d125b3dc51ddb25556
