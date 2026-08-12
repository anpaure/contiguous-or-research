# Independent-style audit: three-slot Bellman normal form

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_THREE_SLOT_BELLMAN_NORMAL_FORM_AND_SCALAR_GATE_20260804.md`  
**Verdict:** **PASS**, including the scalar theta estimate, the completion
of regime I, and the independently audited regime-II triangle theorem.

## 1. Table constraints

For `(0,x,y,T)`, internal superadditivity gives `y>=2x` and
`T>=x+y`; the remaining inequalities follow from monotonicity.  Comparing
`y/2` with `T/3` therefore gives the complete efficiency dichotomy.

## 2. Regime I recurrence

Under `2T<=3y`, pairs of size-three generators are no better than three
size-two generators.  Pairs of size-one generators are no better than one
size-two generator.  A remaining size-one plus size-three pair is no better
than two size-two generators because `x<=T-y` and `2T<=3y`.

The only odd-capacity residues are consequently one size-one generator or
one size-three generator.  Their offsets relative to `qy` are `x` and
`T-y`, and the latter is larger by `T>=x+y`.  This verifies (1.4).

## 3. Regime II recurrence

Under `3y<=2T`, triples of size-two generators are no better than two
size-three generators, and pairs of size-one generators are no better than
one size-two generator.  Modulo three, residue two is represented by one
size-two generator.  Residue one is represented either by one size-one
generator or, after removing one size-three generator, by two size-two
generators.  These give offsets `x` and `2y-T`, proving (1.8).  The stated
parameter bounds follow directly from `y>=2x` and `3y<=2T`.

## 4. Scalar reduction

In subcritical regime I, `T>=A` and `T<=3y/2` force `y>=2A/3`, while
`z=T-y` lies in `[A-y,y/2]`.  On `[0,A/2]`, the exact logarithmic ratio

\[
 \log{\phi(A+u)\over\phi(A-u)}
 =2\operatorname{arctanh}(u/A)-\pi u/A
\]

is negative, so the transient replacement `K(x)-K(z)` is nonnegative.

On the allowed shift interval, only the zero-period term lies below `A`.
The critical-point calculation is therefore identical to the audited
two-slot calculation and shows that every interior critical point is a
strict maximum.  The endpoint shifts are `A-y` and `y/2`, giving exactly
`mathcal H(y)` and the arithmetic margin `C(y/2)`.

At `y=2A/3`, the two cosets interlace into the `A/3` lattice; at `y=A`
they coincide with two copies of the `A` lattice.  This verifies (2.2).

## 5. Scalar theta-gate audit

For `P=tA`, the two residue classes have exactly four points at or below
`A`: `0,P,A-P,A`.  Expanding those four kernel values gives the four
Gaussian factors at lattice offsets `-1,0,1,2` in (3.2); every omitted
term is in one of the two explicitly displayed negative tails.  Thus the
decomposition has neither a missing head term nor a duplicated tail term.

Poisson summation at `A^2=pi/4` gives the factor two and the dual exponent
`4pi` in (3.4).  Since all omitted lattice terms are positive, replacing
the four-term head by the full theta lattice is in the correct direction.

At `t=2/3`, the first tail begins at `7/3`, with consecutive squared-gap
at least `32/9`, and the second begins at `8/3`, with squared-gap at least
`4`.  Multiplication by `A^2=pi/4` gives the ratios `e^(-8pi/9)` and
`e^(-pi)`.  The rational bounds in (3.6)--(3.8) leave the strict margin

\[
 {1\over28}-{1\over20000}-{1\over36}>0.
\]

Hence Theorem 3.1 is a uniform proof of `H(P)>0` on the whole interval,
not an endpoint interpolation or numerical check.

For `y>=A` in regime I, cancellation in (1.5) leaves `C(y)+K(x)` minus a
tail shifted by `z`.  Since `z>=x`, replacing `z` by `x` only makes that
negative tail larger in magnitude, so it is a valid lower bound.  The
result is exactly the two-slot Bellman sum for `(0,x,y)`, and `2x<=y`
holds.  Thus Theorem 3.2 closes the whole of regime I without extending
the scalar theta estimate outside its stated interval.

## 6. Regime-II boundary reduction

For fixed `x,y`, every positive-period Bellman argument is nondecreasing
in `T`.  On the active branch `z=2y-T`, the first such argument is exactly
`2y` and all later ones increase.  Hence the minimum occurs at
`max(A,3y/2)`.

At `T=3y/2`, the three eventual residues are `0,s,2s`, with `s=y/2`.
The only discrepancy from the arithmetic step-`s` clock is replacement of
its first value `s` by `x`.  The three cases in (4.4)--(4.6) compare the
remaining tail respectively with `C(s)`, `C(A/2)`, or `C(x)`; every
comparison occurs entirely in the increasing part `[A,infinity)` of `K`.

At the other boundary `T=A`, both `x` and
`z=max(x,2y-A)` lie in `[0,A/3]`.  The previously audited decrease of `K`
on `[0,A/2]` makes the transient correction nonnegative.  Thus only the
compact triangle (4.2)--(4.3) remains.

For fixed `y`, the allowed `z` interval is contained in `[0,A/3]`.  The
same logarithmic-derivative calculation used in Section 4 says every
interior critical point of `F_A(z)` is a strict maximum there.  Therefore
the minimum over `z` is bounded below by the minimum of the two
full-interval endpoints `0` and `y/2`, even when the physical lower
endpoint is larger than zero.  These substitutions give the two functions
in (4.7).

## 7. Regime-II triangle theorem

The separate theorem
`MATH_CANDIDATE_PROOF_THREE_SLOT_REGIME_II_TRIANGLE_20260804.md` was
independently replayed line by line.  Its theta-completion identity has the
correct omitted lattice shores; the Poisson factor and dual exponent are
correct; the two-Gaussian envelope has only an interior maximum; and all
rational power certificates follow from
`exp(-pi/36)>229/250`.  Its margins are

\[
 J_1>{397\over20000},
 \qquad J_2>{117\over20000}.
\]

Together with Sections 3--6, this proves every three-slot Bellman table
strictly positive.

## 8. Scope

The note does not prove:

* the Bellman inequality for all finite tables;
* the smooth configuration theorem or an additive OR-word bound.

Its gain is a complete max-plus classification and positivity proof at
`n=3`.  A finite Bellman counterexample, if one exists, has grid size at
least four.
