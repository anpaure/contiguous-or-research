# Audit of the three-row rank-strip LP

## Verdict

The reported numerical identity

\[
             \text{minimum holes}=\sigma
\]

for odd `k=11,13,...,21` is forced by the LP's equality constraints.  It is
not an optimized lower bound, a construction, or evidence that the Boolean
array conjecture is true.

Let `z_(ell,s)` be the normalized number of selected cells of physical
length `ell+1` and OR-rank `s`, and let `h_ell` be the normalized number of
holes in row `ell`, for `ell=0,1,2`.  The model imposes

\[
 \sum_s z_{\ell,s}+h_\ell={n-\ell\over M},\qquad
 \sum_{\ell=0}^2z_{\ell,s}={\binom{k}{s}\over M}.    \tag{1}
\]

Summing the three row equations and subtracting the rank-total equations
gives, for every feasible point,

\[
 \sum_{\ell=0}^2h_\ell
 ={n+(n-1)+(n-2)-\sum_{s=1}^r\binom{k}{s}\over M}
 ={\sigma\over M}.                                  \tag{2}
\]

An exact LP dual certificate puts multiplier `+1` on each row equation,
`-1` on each rank equation, and zero on every inequality.

The right-extension inequalities used by the model are valid coarse
necessary conditions.  In arbitrary depth they have the form

\[
 Z_{\ell,\ge s}\le
 Z_{\ell+t,\ge s+t}+\sum_{j=1}^t h_{\ell+j}+t,       \tag{3}
\]

where the final `t` accounts for right-boundary starts.  They are a
rank-profile projection of the occupied-band/double-chain theorem already
in the handoff.  Exact integer profiles satisfy all displayed inequalities
in every reported `d=3` case, so the computation shows only that this weak
one-sided relaxation remains feasible.

Any useful strengthening must retain at least one of: the physical
locations of the holes, both extension directions, the join recurrence, or
coordinate pin survival.

