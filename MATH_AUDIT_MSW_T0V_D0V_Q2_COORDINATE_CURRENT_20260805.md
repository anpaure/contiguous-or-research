# Audit of the `D_0V -> T_0V` q2 coordinate-current obstruction

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_OBSTRUCTION_MSW_T0V_D0V_Q2_COORDINATE_CURRENT_20260805.md`  
**Status:** PASS

## 1. Incidence identity

For an internal owner not containing `c`, the turn contains `c` exactly
when its selected incidence adds `c`.  Endpoint added-`c` incidences must
be removed because endpoints carry no q2 turn.  This gives (1.4).

Counting selected incidences into colours containing `c` splits them into
owners already containing `c` and incidences which add `c`.  This gives
(1.5).  Therefore fixed owner/colour degrees plus fixed endpoint
added-label multiset force every q2 coordinate marginal.

## 2. Prefix sets and donor pairs

Direct reading gives

\[
 T_0\setminus D_0=\{2,9,11\},\qquad
 D_0\setminus T_0=\{3,7,8\}.
\]

For `D_0=101011110101`, the height-zero upsteps are `1,3,5` and the
height-three upsteps are `8,10,12`.  Pairing equal left/right counts gives
the first three pairs below.  The height-one upstep at `6` and height-two
upstep at `7` give the fourth:

\[
 (1,12),(3,10),(5,8),(6,7).
\]

The only downsteps between these positions start at heights one or four,
so the forbidden-corridor condition is satisfied.  Their matching ordinal
counts are `0,1,2,3`.  The eligible height classes contain no further
pair, so these are the four exact canonical preimages.

## 3. Current check

Removing `D_0` and adding `T_0` changes the coordinate marginal by

\[
 +e_2+e_9+e_{11}-e_3-e_7-e_8\ne0.
\]

All other turns being permuted contributes zero.  This contradicts the
endpoint-transparent invariant, exactly as claimed.

Appending a common suffix changes neither set difference nor the prefix
coordinate vector.  Summing over all suffixes multiplies the same nonzero
vector by `Cat_(r-6)`.  Audit verdict: PASS.
