# Independent audit: stratified-support phase-clock dilation and the oriented `T_2` certificate

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_STRATIFIED_SUPPORT_PHASE_CLOCK_DILATION_20260813.md`  
**Audited source SHA-256:**
`01e63d5202486d329fafe5003a3e7981d687dc8914ab99a933484488fb318f24`  
**Verdict:** **PASS**, apart from the harmless TeX typo `,quad` in (6.1).

## 1. General theorem

If a lifted interval meets `s` clock blocks, starts at offset `a`, and
ends at offset `b`, its physical width is

\[
 (h+1-a)+(s-2)(h+1)+(b+1)
 =(s-1)(h+1)-a+b+1.
\]

Thus equation (3.6) and the offset condition `a'-b'=a-b` are exact.
For `s=1`, the base value, starting phase, and the same two offsets
determine the clock arc.  For `s=2`, alternating phases determine both
endpoint blocks from the initial phase, and the same offsets determine the
literal union of their two clock pieces.

For `s>=3`, every interval contains at least one strictly intervening
block in full.  Both possible half-clock blocks satisfy

\[
 \bigcup_{t=0}^{h}D_t=U,
 \qquad
 \bigcup_{t=h}^{2h}D_t=U.
\]

The complete intervening block therefore shields both endpoint pieces and
makes phase irrelevant.  The signature in (1.4) is consequently
sufficient at every `h>=2`.  Multiplicity domination is unnecessary for a
support theorem.

The closure qualification is essential and correctly stated.  An interval
crossing a separately attached return has a block list not tested by the
internal path bank.  The theorem applies to such intervals only after the
complete return-augmented closures pass the same stratified signature
test, or after a literal return-transport theorem supplies it.

## 2. `T_2` endpoint orientations

The five new residual paths have endpoint pairs

\[
 F_0F_{11},\quad F_2R_{62},\quad F_1R_0,\quad
 F_{62}R_{11},\quad R_1R_2.
\]

Alternating them with fixed complementary returns `F_xR_x` gives the
cycle

\[
 F_0,F_{11},R_{11},F_{62},R_{62},F_2,R_2,R_1,
 F_1,R_0,F_0.
\]

In the affected-path order `(x_0,x_2,x_1,x_{62},x_{11})`, this is mask
`26`, and reversing the whole cycle gives mask `5`.  These are global
cycle orientations, not five independent post-switch choices.  Before the
switch the five components may be oriented with the same mask, and the
union of old and new owner adjacencies admits the common bipartite phase
map used in the theorem.

## 3. Independent finite certificate

I independently reconstructed all semilength-six canonical paths, toggled
the two literal hexagons, derived the common phase map, applied mask `5`,
and enumerated the signature sets in (1.4).  The exact result was

```text
old stratified signatures = 2382
new stratified signatures = 2404
old minus new             = 0
new minus old             = 22
```

The singleton bank is unchanged.  The oriented two-block bank contains
`792` `(union,start-phase)` signatures on each side.  Each of the five
changed old unions in (6.4) occurs on a new edge with starting phase zero;
all other oriented edges are literal.  The table's five union values and
positions replay exactly.

The `s>=3` row is a finite theorem about the fixed `m=6` base.  Its exact
enumeration proves the stated inclusion; the all-`h` conclusion then
follows symbolically from the full-block shield, rather than by
extrapolating the clock computations through `h=12`.

The surviving open condition is precisely the one stated in the source:
the complementary return and vertical endpoint closures must be added to
the stratified test before any complete odd-wreath cyclic-deck conclusion
is drawn.

