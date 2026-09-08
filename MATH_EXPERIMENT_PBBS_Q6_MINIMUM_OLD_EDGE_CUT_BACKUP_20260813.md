# Exact finite minimum rematerialization cost for the PBBS `q=6` old-piece cut gate

**Date:** 2026-08-13  
**Method:** exact CP-SAT on `h100` only  
**Status:** finite computational theorem for `5<=m<=10`.  It measures the
smallest number of immediate-upper colours which must receive a new witness
if one cuts old PBBS edges so that every positive run shorter than six is
punctured.  It does not construct the new witnesses, the new seams, or an
asymptotic repair.

## 1. Optimization problem

Let `F_m` be the complement-GK/PBBS owner factor on `[2m+1]`.  Give every
old edge `e` a cut variable `c_e`.  For every positive coordinate-run
collar `C` of length below six impose

\[
                         \sum_{e\in C}c_e\ge1.      \tag{1.1}
\]

For every immediate-upper colour `U`, let `F_U` be its old witness fibre
and give it a backup variable `b_U`.  Impose

\[
                         \sum_{e\in F_U}(1-c_e)+b_U\ge1. \tag{1.2}
\]

Thus `b_U=1` permits all old witnesses of `U` to be cut, on the promise
that a later packet rematerializes `U`.

The objective is lexicographic:

1. minimize `sum_U b_U`;
2. subject to that, minimize `sum_e c_e`.

The implementation uses the single integer objective

\[
 (|E(F_m)|+1)\sum_U b_U+\sum_e c_e.               \tag{1.3}
\]

## 2. Exact optimum

Every displayed solve returned `OPTIMAL`.

\[
\begin{array}{c|r|r|r|r|c}
m&|E(F_m)|&\text{short collars}&\min\#\text{ cuts}
 &\min\#\text{ backups}&\text{backup old-fibre sizes}\\ \hline
5&462&275&81&11&1^{11}\\
6&1,716&845&257&52&1^{52}\\
7&6,435&2,445&835&180&1^{180}\\
8&24,310&6,834&2,605&510&1^{510}\\
9&92,378&18,677&7,844&1,254&1^{1254}\\
10&352,716&50,127&22,789&2,772&1^{2772}
\end{array}                                             \tag{2.1}
\]

For comparison, the proved all-unique gap-nine family contains

\[
                         (2m+1){m+1\choose5}       \tag{2.2}
\]

blocked collars.  One rematerialized colour can free cuts serving several
overlapping collars, so `(2.2)` is not itself a lower bound on the number
of distinct backups.  The optimization in `(1.1)--(1.3)` computes the
joint minimum exactly for the displayed ranks.

For every `m>=5` tested, every optimal backup in `(2.1)` belongs to a
singleton old fibre.  Thus the optimizer never pays for a redundant old
colour: every paid target genuinely loses its unique old witness.

## 3. Interpretation

The finite data prove two useful points.

1. The old-witness-preserving cut face is not merely infeasible because of
   one badly chosen collar.  Even after optimizing cuts globally, many
   distinct upper colours must be rematerialized.
2. The number of necessary colours is much smaller than the raw number of
   blocked collars.  A replacement-enabled proof should therefore optimize
   a **hitting set of punctured fibres**, rather than attach an independent
   packet to every short run.

No asymptotic formula is claimed from the six values in `(2.1)`.  In
particular the target aperture `q=d(2m+1)+1` grows with `m`, whereas this
audit holds `q=6` fixed.  The data neither prove `o(Cat_m)` backups at the
growing deadline nor show that the selected backup colours admit mutually
compatible occurrence packets.

## 4. Frozen artifacts

The optimizer is

`scratch/optimize_pbbs_qsafe_cut_backups_20260813.py`.

It imports the literal factor/collar builder from

`scratch/audit_pbbs_qsafe_cut_capacity_20260813.py`.

The exact JSON certificates for `m=5,...,10` are

`scratch/h100_results/pbbs_qsafe_minbackup_m5q6_20260813.json`

through

`scratch/h100_results/pbbs_qsafe_minbackup_m10q6_20260813.json`.

The solver models and all substantive enumeration ran on `h100`; the Mac
was used only to write the script and inspect the returned JSON summaries.
