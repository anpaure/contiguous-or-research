# Independent proof audit: three-pairing residence cover and selector gate

**Date:** 2026-08-04
**Audited file:**
`MATH_THEOREM_THREE_PAIRING_RESIDENCE_COVER_AND_SELECTOR_GATE_20260804.md`

## 1. Distribution audit

For a fixed middle owner `T`, a pairing with `m` cross-edges is obtained by

* choosing `m` points in `T` and `m` in its complement;
* bijecting the two chosen sets; and
* internally pairing the two remaining sets.

The count is

\[
 \binom rm^2m!((r-m)-1)!!^2,
\]

and division by `(2r-1)!!` gives the displayed law.  The parity restriction
`m congruent to r mod 2` is necessary and sufficient.  Direct cancellation
gives

\[
                 p_{m+2}/p_m=(r-m)^2/((m+1)(m+2)).
\]

For even `r`, `p_0=binom(r,r/2)/binom(2r,r)`.  For odd `r`, direct
substitution verifies

\[
                 p_1(r)=r^2p_0(r-1)/(2r-1).
\]

The polynomial prefactor in (1.4) is deliberately loose but valid.  The
tail estimate therefore has exponent

\[
                 -r\log2+O(M\log r).
\]

## 2. Union-bound audit

For three independent frames, a fixed owner is uncovered with probability
`p_{r,M}^3`.  There are `binom(2r,r)<=4^r` owners.  Multiplication gives

\[
 4^r\bigl(4(r+1)^{3/2}(M+1)r^M2^{-r}\bigr)^3
 =64(r+1)^{9/2}(M+1)^3r^{3M}2^{-r}.
\]

For `M=O(sqrt(r)+log r)`, its logarithm is `-Theta(r)`.  Thus the
three-frame cover is exact for all sufficiently large `r`, not merely an
almost-cover.

For `q` frames and a demand of at least `h` good frames, failure means at
least `s=q-h+1` bad frames.  The union bound has leading exponential
`2^{(2-s)r}`.  Hence `s>=3` is the clean threshold of this argument:
three frames give one good choice, four give two, and in general `h+2`
frames give `h` good choices.

## 3. Residence audit

The good threshold is

\[
                 m\ge L+\lceil3\log_2r\rceil.
\]

Since `m<=r`, the cube Gray-code guarantee
`m-3log_2m` is at least `L`.  A cube bit toggles the two members of one
physical pair simultaneously, so same-bit separation is exactly physical
coordinate-transition separation.  Constant pairs create no internal
transition.  Therefore every installed good-cell cycle is `L`-resident.

No claim is made about transitions between different cells; none have yet
been selected.

## 4. Selector audit

The symmetric bipartite occurrence graph records both orientations of
every available physical edge.  A perfect matching is a global successor
permutation, but without the collar row it can contain a two-cycle and is
not yet a simple 2-factor.  Along a selected directed cycle, two transitions
at edge-distance less than `L` may not share a physical coordinate.  This
is exactly (4.1), and it automatically excludes antiparallel use of one
physical edge when `L>=2`.  Hence Proposition 4.1 is an exact equivalence,
not merely a sufficient orientation restriction.

The narrower graph `B^to` records one prechosen orientation of each good
cycle.  Hall (4.3) is necessary and sufficient only for a directed
permutation cover in that restricted arc set; the theorem does not confuse
that statement with residence.

The all-perfect-pairings corollary closes precisely this ordinary Hall row.
For each owner `T`, transitivity of `S_(2r)` shows that the number `a(T)` of
pairings with `X_P(T)>=M` is one constant `a`; a cross-shore perfect
matching gives `a>0` when `M<=r`.  Each good oriented cell cycle contributes
one outgoing and one incoming occurrence at `T`.  Hence the full successor
occurrence bipartite multigraph is `a`-regular and has a perfect matching.
Parallel arcs must remain occurrence-labelled in this count.  The selected
matching may switch frames, violate (4.1), or form a directed two-cycle, so
the corollary gives no resident simple factor.

Selecting whole cell cycles avoids all new seams.  The equations (4.4)
are then precisely the requirement that the selected cells partition the
owner set.

## 5. Obstruction audit

Two triangles meeting in one vertex have no spanning 2-factor.  Duplicating
each triangle gives four partial factors and makes every noncentral vertex
belong to two domains while the shared vertex belongs to four.  Thus even
the strengthened four-frame conclusion “at least two good choices per
owner” does not imply Hall or a 2-factor.

This is an abstract factor obstruction.  It does not assert that these five
vertices are themselves a complete pair-cell instance.  Its exact scope is
to rule out any deduction based only on domain coverage or domain
multiplicity.  A positive theorem must use the actual intersection and
successor geometry of random pair cells.

## 6. Scope verdict

The theorem validly proves:

* three pairings cover every middle owner by a good high-dimensional cube
  cell for all sufficiently large `r`;
* `h+2` pairings give at least `h` good frames per owner;
* all perfect pairings together have an ordinary successor perfect
  matching, hence a directed spanning permutation cover;
* constant active-frame multiplicity gives a topological perfect-matching
  selector; and
* variable multiplicity, even bounded below by two, is insufficient in
  general.

It does **not** prove:

* Hall for the actual three random good-cell factors;
* the collar constraints for a Hall selector;
* one Hamilton component;
* immediate or higher upper palettes; or
* a lower compiler.

The exact next residence object is therefore a collar-compatible perfect
matching in the successor occurrence graph, or a run-transparent splice
theorem strong enough to replace it.
