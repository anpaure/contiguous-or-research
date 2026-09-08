# Self-audit: two-sided mandatory-collar desaturation

**Date:** 2026-08-04  
**Method:** independent symbolic replay of the proof; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_AND_ZERO_RANK_LEAKAGE_20260804.md`

## Verdict

**PASS under its explicit maximal-envelope and separation hypotheses.**
The proof really eliminates every rank-`r` short cell and preserves the
same single owner chronology.  It does not bound duplicate lower values.

## 1. Left end

For source position `p<d`, every owner window containing `p` has index in
`[0,p]`.  The departure coordinate `alpha_p` is present in each of those
owners, so `alpha_p in E_p`.

Fix an affected owner `T_i`, `i<d`, and `x in T_i`.

- If the positive run containing this occurrence enters after the left
  boundary at owner `a`, its envelope support begins at `a+d`.  Residence
  (or a right-boundary end) makes `max(i,a+d)` a valid unmodified supplier
  in `[i,i+d]`.
- If that same run crosses the left boundary and also reaches `T_d`, then
  `x in E_d`.
- If that run crosses the left boundary but ends before `T_d`, its departure is
  some `alpha_u`, `u<d`, and the retained singleton at `u` supplies it.

These cases are exhaustive.  Hence the left replacement loses no owner
coordinate.

## 2. Right end

The symmetric replay uses the envelope support `[a+d,b]` of a run starting
at owner `a` and ending internally at owner `b`.

- If the run containing the occurrence ends before the right boundary,
  `min(b,i+d)` is an unmodified
  supplier below source position `W`.
- If that run reaches `T_(W-1)` and begins no later than
  `T_(W-d-1)`, then
  `x in E_(W-1)`.
- If that run reaches the right boundary but begins later, the retained
  arrival singleton at source `a+d` supplies it.

For `p>=W`, every owner window containing `p` sees the arrival coordinate
`beta_(p-d-1)`, so the replacement remains inside `E_p`.

The affected owner sets at the two ends are disjoint when `W>2d`, so the
two arguments compose.

## 3. Leakage localization

A `q`-cell beginning at `j` is contained in exactly the owner windows with
indices

\[
 [\max(0,j+q-1-d),\min(j,W-1)].
\]

For `q<=d`, this interval is a singleton exactly for the first prefix or
last suffix cell.  Every other cell lies in two consecutive distinct
rank-`r` owners, so its value has rank at most `r-1`.

The exceptional prefix and suffix cells consist of `q` consecutive
departure or arrival singletons.  Repetition within `q<=d` transitions
would create an internal positive run shorter than `d+1`; hence the labels
are distinct and each exceptional value has rank exactly `q<r`.  Thus
`R_A=0`.

## 4. Pins and Euler scope

If pin-affected owner windows avoid the first and last `d` owner windows,
the maximal pinned envelope agrees with the unpinned envelope throughout
both collar blocks and their affected owners.  The preceding replacement
therefore leaves every forced fact untouched.

Changing source letters while retaining all owner-window unions leaves one
linear chronology of the same `W` owners.  In trace language it is one
rooted trail; no splice or reset is introduced.  The theorem does not claim
cyclic closure of the modified source word.

The fixed-word reclassification identity then gives
`D^Pi+Q^Pi=D` and `R^Pi=0`, so bounded terminal deficiency is exactly
`D<=sigma+C` on this face.

## 5. Scope exclusions

The argument requires:

- a resident path whose maximal envelopes already realize all owners;
- an opening separated from the complete pin halo; and
- a simple Johnson owner path.

It supplies none of these globally and does not control named-target
collisions.  Therefore it is a genuine removal of the rank-leakage and
Euler-reset terms, not a proof of the remaining one-copy rounding theorem.
