# Audit of the positive two-size rail unit-residue absorber

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_POSITIVE_TWO_SIZE_RAIL_UNIT_RESIDUE_ABSORBER_AND_SAFE_ORDER_GATE_20260807.md`  
**Verdict:** PASS for the role/sign ledger, common-width deck
disjointness, maximal-background greedy count, and one-order union-bound
criterion.  The displayed background lower bound is conservative by one,
but correct as stated.

## 1. Role table and sign

For (N_1=M-1), the two roles of (x,y) are core/unused and
unused/core.  Hence

\[
 \omega_{Q_1^+,\ell}-\omega_{Q_1^-,\ell}
 =N_1(e_x-e_y).
\]

For (N_2=M-2), the roles reverse, giving

\[
 \omega_{Q_2^+,\ell}-\omega_{Q_2^-,\ell}
 =-N_2(e_x-e_y).
\]

All other coordinates have identical roles on the two sides: (z) is
toggle in both (N_1) components and unused in both (N_2) components;
(D) is always core; every remaining coordinate is always toggle.  Since
(N_1-N_2=1), equation (2.7) has the correct sign and coefficient.

## 2. Deck disjointness

Within (mathcal A^+), every (Q_1^+) deck value contains (x) and
omits (y), while every (Q_2^+) value contains (y) and omits (x).
The two decks are disjoint at every proper common width.  The same argument
with (x,y) reversed proves disjointness in (mathcal A^-).

Each proper width row of an (N_i)-carousel is simple and has (N_i)
values.  Thus both alternatives contain (N_1+N_2=2M-3) values at every
(1\le\ell<N_2).  In particular the owner rows are genuine matchings.

## 3. Background count

For a fixed maximal core, a uniformly random cyclic order has a specified
(q)-subset as one of its cyclic blocks with probability

\[
 \frac{M}{\binom Mq}.
\]

After (b) carousels, at most (bM) owner blocks are forbidden, so the
union bound is (bM^2/\binom Mq).  Condition (3.3) is therefore correct.

Iterating actually certifies at least

\[
 \left\lfloor\frac{\binom Mq-1}{M^2}\right\rfloor+1
\]

orders if one counts the initial automatically available order.  The
source claims only the same expression without (+1), so its stated lower
bound (3.4) is weaker but valid.

Every background owner contains both (x,y); every absorber owner contains
exactly one.  Thus background/absorber owner disjointness is exact and is
unchanged by internal adjacent transpositions.

## 4. Multi-width order avoidance

For a fixed (ell)-subset (J\subseteq T), the probability that (J)
is a cyclic (ell)-block of a random order is exactly

\[
 \frac{N}{\binom N\ell}.
\]

Summing this over every forbidden (J) and every protected width gives
the left side of (4.1).  If it is below one, a safe order exists.  No
independence assumption is used.  Proposition 4.1 is correct.

This is an existence statement for one safe order, not connectivity of the
safe-order graph; the source preserves that distinction in Sections 5--6.

## 5. Audit boundary

The note proves a positive coherent unit incidence residue and a large
owner-compatible background.  It does not yet prove:

* absorption of an arbitrary named multi-row leave;
* connectivity through safe adjacent-transposition states;
* top-two-rank coverage by the nonmaximal gadget; or
* a global integral carousel factor.

Those exclusions are stated correctly.  No mathematical correction is
required.
