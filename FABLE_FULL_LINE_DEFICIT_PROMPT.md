# Fable task: close the remaining full-line edge-deficit regime

Work only on the all-dimensional three-chain-box mathematics.  Do not work on
`k=11`, SAT, certificates, or any finite Boolean instance.  Do not reread the
entire handoff.  The previous 120k-token attempt died before writing files;
start from the new audited reductions below.

## Read exactly these files first

1. `ABSORBED_FLOW_COAREA.md`
2. `FULL_LINE_WEDGE_COVER_SEAL.md`
3. `FULL_LINE_WEDGE_COVER_SEAL_AUDIT.md`
4. `SMALL_DEFICIT_WEDGE_SEAL.md`
5. `SMALL_DEFICIT_WEDGE_SEAL_AUDIT.md`
6. `MULTISCALE_DIRECTION_COUPLING_NEXT.md`, Sections 2, 7, 8, and 9 only
7. `LARGE_DEFECT_DICHOTOMY_NEXT.md`, Theorem B only

Treat every scope statement literally.

## Newly proved starting point

For the bottom dangerous threshold put

\[
\ell=3-\delta,
\qquad \int z\,d\rho\le\delta.
\]

The complete selected-line geometry gives

\[
P+2N\ge3-\sqrt{6\delta},
\qquad
A\le P\le2f-3+\sqrt{6\delta}.
\]

For `C=int_alpha(p+s-1)`,

\[
C\le\min\{4f-6+2\sqrt{6\delta},
           3-2\delta+\sqrt{6\delta}\}.
\]

The exact pointwise gap inequality is

\[
\phi(p,s,z)+(4-s)z\ge p+s-1,
\]

so the complete gap correction is at most `3 delta`.  Consequently

\[
U(1^+)\le {15\over4}
 +{5\over4}\sqrt{6\delta}+{3\over2}\delta.
\]

Thus every full-line process is excluded when

\[
0\le\delta<\delta_0,
\qquad
\delta_0={ (\sqrt{29}-5)^2\over24}
=0.0061813303606\ldots .
\]

The coefficient three in the pointwise gap bound is sharp.  Do not try to
improve it without using geometry or common lifetimes.

## Only remaining target

Resolve physically coherent processes with

\[
\delta\ge\delta_0.
\]

You must retain:

- the same physical plateau, gap, seam, direction, and level identities at
  every threshold;
- additive gap contraction;
- actual complete-line unions, pair intersections, and triple concurrency;
- common absorbed-edge lifetimes;
- the exact nonabsorbed saving functional.

Obtain one of:

### Outcome A

Prove, with an explicit constant, that every such process has some common
continuity threshold `c` with `U(c)<4`.  This would combine with the two new
seals to close the broad marked-process obstruction.

### Outcome B

Construct one genuine full-line, common-lifetime marked process satisfying
all constraints with `U(c)>=4` at every threshold.

### If neither is reached

Give one formally stated minimal missing lemma, after proving every reduction
to it.  It must be strictly narrower than “couple the thresholds.”  Include
an exact near-extremizer or dual obstruction showing sharpness.

## Preferred attack

The separate estimates double-charge the same deficit: missing wedge points
produce the `sqrt(delta)` error, while the physical gaps occupying those
points produce the `3delta` error.  Try to derive a joint weighted wedge-gap
coarea inequality, or show via a coherent counterprocess that no such local
joint charge can suffice.  If local control fails, integrate one common
weight over the actual contraction lifetimes.

## Deliverables

Write only these new files:

1. `fable_general_case/FABLE_FULL_LINE_DEFICIT_RESOLUTION.md`
2. `fable_general_case/FABLE_FULL_LINE_DEFICIT_AUDIT.md`
3. `fable_general_case/FABLE_FULL_LINE_DEFICIT_LEDGER.md`

Do not merely narrate your reasoning.  Write the files before the response
approaches the token ceiling.  Reserve at least 15k output tokens for the
deliverables.
