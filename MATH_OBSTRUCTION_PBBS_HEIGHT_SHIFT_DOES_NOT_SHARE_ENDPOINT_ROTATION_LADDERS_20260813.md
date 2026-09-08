# PBBS height shift does not share the endpoint-rotation ladders

**Date:** 2026-08-13  
**Status:** unconditional obstruction to the direct conjugation argument.  It
does not rule out a new simultaneous multi-seam relative trade.

## 1. The height spine has no translation

Put

\[
 U_h=\{0\}\mathbin{\dot\cup}[h+1,2h]
      \mathbin{\dot\cup}\{2h+2,2h+4,\ldots,2m\}.
\tag{1.1}
\]

Then

\[
 U_{h+1}=U_h-\{h+1\}+\{2h+1\}.
\tag{1.2}
\]

### Proposition 1.1 (exact height-shift obstruction)

Fix `h>=1` with `2h+2<=m`.  There is no coordinate permutation `gamma`
satisfying

\[
 \gamma(U_t)=U_{t+1}
 \qquad
 (t=h,h+1,2h,2h+1).
\tag{1.3}
\]

#### Proof

Apply `gamma` to the ordered difference in the transition
`U_h -> U_(h+1)`.  Equations `(1.2)` and `(1.3)` give

\[
 \gamma(2h+1)=2h+3,
\tag{1.4}
\]

because `2h+1` is inserted at height `h` and `2h+3` is inserted at
height `h+1`.

But `2h+1` is deleted in the transition `U_(2h) -> U_(2h+1)`.
Applying `gamma` to this transition gives

\[
 \gamma(2h+1)=2h+2,
\tag{1.5}
\]

because `2h+2` is deleted in the next transition.  Equations `(1.4)` and
`(1.5)` contradict each other. \(\square\)

For the compound low spine beginning at height four, the first
contradiction is the concrete pair

\[
 \gamma(9)=11\quad\hbox{from the height-4 insertion},
 \qquad
 \gamma(9)=10\quad\hbox{from the height-8 deletion}.
\tag{1.6}
\]

Thus, once the retained range contains the displayed transitions, there
is not even a coordinate relabelling which translates the whole PBBS
height spine by one.

## 2. Consequence for the first-seam endpoint ladder

`MATH_THEOREM_PARITY_TAIL_ENDPOINT_ROTATION_INSTALLS_FIRST_COMPOUND_SEAM_20260813.md`
constructs a relative trade for `C_4-U_5` in one fixed complete
first-aligned MSW factor `F_m`.  An arbitrary coordinate permutation can
send the local Johnson edge `C_4-U_5` to a prescribed edge
`C_h-U_(h+1)`, but it simultaneously sends the host factor to a conjugate
factor `gamma(F_m)`.  This proves an individual theorem in the conjugate
host; it does not put all height trades into the same `F_m`.

Proposition 1.1 rules out the simplest proposed repair: there is no single
height-translation permutation whose powers carry the first seam and its
PBBS surroundings through all low heights.  In particular, conjugation
does not identify the `Theta(m)` colour ladders inside one common factor,
so it gives no reduction from the naive `Theta(md)` colour count.

This is deliberately a narrow conclusion.  The owner-balance equations
for several seams may still admit one new simultaneous endpoint-flow
trade.  Such a trade could pair the old seam endpoints globally and use
shared *vertices*, but a facet colour of the exact factor can be modified
only once.  Its proof therefore requires a genuine multi-source
owner/lower trade in the fixed factor, together with one joint upper-current
certificate; it cannot be obtained by relabelling the one-seam theorem.

The only unconditional size bounds currently supplied by this lane are

\[
 \Omega(d)\le \#\{\hbox{changed colours}\}\le O(md),
\tag{2.1}
\]

where the lower bound is the number of distinct required seam colours and
the upper bound repeats the one-seam ladder.  Achieving `O(m+d)` (or any
other shared bound) remains an explicit simultaneous-trade problem.
