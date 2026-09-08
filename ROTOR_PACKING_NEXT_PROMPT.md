# Research prompt: integral monotone-profile rotor packing

We study universal contiguous-OR words.  The local and fractional parts of
the following route are already proved; do not re-prove them or claim the
final theorem from fractional feasibility.

Let

\[
W={2m\choose m},\quad N_q={2m\choose m-q},\quad
h=\lceil\sqrt{m\log m}\rceil,\quad H=m-h.
\]

A **queue atom** is specified by an injective coordinate queue and a
nonincreasing radius profile

\[
d_0\ge d_1\ge\cdots\ge d_{H-1},\qquad 0\le d_t\le h.
\]

At start (t), it exposes the saturated symmetric chain centered at the
length-(m) queue window, through radius (d_t).  The atom is a genuine MTF
OR word of length at most (H+2h+1), and its exposed masks are pairwise
distinct.  The complete coordinate/profile orbit has an exact fractional
cover of every rank (m-h,ldots,m+h), of total atom mass (W/H).

For an integral atom family (mathcal A), define for each sign
(sigma\in\{-,+\}) and depth (q>0)

\[
T_q^\sigma=\sum_S\mu_q^\sigma(S),\qquad
D_q^\sigma=\sum_S(\mu_q^\sigma(S)-1)_+,
\]

and use one middle-row quantity (T_0,D_0).  The exact missing identity is

\[
M_q^\sigma=N_q+D_q^\sigma-T_q^\sigma.
\]

## Main target

Prove or disprove that there are (W/H+o(W/H)) queue atoms such that

\[
\sum_{q=0}^h\sum_\sigma |T_q^\sigma-N_q|=o(W)
\]

(with the middle row counted once) and

\[
D_0+\sum_{q=1}^h(D_q^-+D_q^+)=o(W).
\]

Either statement is acceptable:

1. an explicit integral construction;
2. a randomized greedy/absorption theorem with all growing-uniformity error
   terms proved;
3. a rigorous obstruction showing that this atom class necessarily has
   (Omega(W)) summed duplicate excess.

If the positive statement holds, concatenating the atom words costs
(W+o(W)); missing band masks cost (o(W)) literally; and the established
width-order two-tail word costs (o(W)).  Therefore it proves

\[
\nu(2m)=W+o(W).
\]

## Required audit discipline

- Do not cite a fixed-uniformity nibble theorem diagonally: an atom exposes
  (Theta(m^{3/2})) band masks.
- Pair codegree (o(D)) alone is insufficient.  The allowed leftover is
  (o(W)) among (Theta(W\sqrt m)) band masks, i.e. relative
  (o(m^{-1/2})).
- Preserve the per-rank quotas.  Atom count plus small duplicate excess does
  not prevent an undersupplied row.
- All queue coordinates must be injective over the full residence horizon.
- Distinguish the shared width-order tail construction from literal tail
  enumeration.
- Report exact small cases.  The first case (m=3,h=1,H=2) has a certified
  zero-duplicate exact packing of ten atoms; reproduce it before trusting a
  general implementation.

Relevant files:

- `MONOTONE_RADIUS_ROTOR_BRAIDS_AUDIT.md`
- `ROTOR_PACKING_SMALL_EXACT.md`
- `GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT.md`
- `TRUNCATED_TAIL_CONSTRUCTION.md`
