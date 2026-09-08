# Independent audit: hole spectrum and boundary-moment hierarchy

## Verdict

**PASS**, with `d>=1` and the standard convention that out-of-range binomial
coefficients vanish.  The exact hole spectrum is bookkeeping; the substantive
new theorem is the synthesis of run geometry, cover-edge gradients, and
dimension projection.

## Checked identities

Let `B` be the interval band of lengths at most `d`, let one distinguished
short witness be selected for every nonempty mask of rank below `r`, and let
`H` be the `sigma` remaining band cells.  For every coordinate set `Q`,

\[
F_Q=\sum_{s=1}^{r-1}\binom{k-|Q|}{s}+h_Q,
\qquad
h_Q=\sum_{T\subseteq[k]\setminus Q}c_T,
\]

where `c_T` counts holes whose OR is `T`.  Boolean Möbius inversion recovers
the nonnegative integer vector `(c_T)` of total mass `sigma`.  This is exact,
with multiplicity.

Projecting every entry to `Q` and deleting empty projections preserves every
target contained in `Q`, so

\[
z_Q\le n-\nu(|Q|).
\]

For zero-run lengths `g_j`, put

\[
F_Q=\sum_j f_d(g_j),\qquad
\Lambda_Q=\sum_j\min(g_j,d-1).
\]

The pointwise identity/inequality gives

\[
F_Q+\frac d2\Lambda_Q\le d z_Q.
\]

The band cover graph has

\[
E_{n,d}=(d-1)(2n-d)
\]

edges and maximum degree four, hence at least
`max(E_(n,d)-4 sigma,0)` selected-selected edges.

## Boundary gradient

For a selected cover edge `I proper-subset J`, its two labels are distinct
lower masks.  If their ranks are `s<t`, then `s<=r-2` and `t<=r-1`.  Its
weight

\[
\binom{k-s}{q}-\binom{k-t}{q}
\]

counts exactly the `q`-sets that avoid the smaller label but meet the larger
one.  A zero run supplies at most `min(g,d-1)` crossings at each boundary, so

\[
G_q\le2\sum_{|Q|=q}\Lambda_Q.
\]

Consequently the coefficient in the weighted theorem is indeed `d/4`:

\[
dZ_q\ge R_q+H_q+\frac d4G_q.
\]

The displayed explicit gradient direction is also correct:

\[
\binom{k-s}{q}-\binom{k-t}{q}
=\sum_{u=s}^{t-1}\binom{k-u-1}{q-1}
\ge\binom{k-r+1}{q-1}.
\]

Combining this with projection and then replacing `nu(q)` by its proved lower
bound `B(q)` is logically valid, though weaker than using the exact value.

## First moment and limitation

At `q=1`,

\[
R_1=\sum_{s=1}^{r-1}(k-s)\binom{k}{s},\quad
H_1=\sum_{I\in H}(k-|U(I)|),\quad
G_1\ge\max(E_{n,d}-4\sigma,0).
\]

No positive lower bound on `H_1` follows without extra information: a hole
may have full OR.  The explicit scalar corollary was mechanically evaluated
at every maximizing rank for `B(k)`, `k<20`; it has no violation and therefore
does not improve any current exact lower bound by itself.  The exact
Möbius/run constraints remain potentially stronger than their average.
