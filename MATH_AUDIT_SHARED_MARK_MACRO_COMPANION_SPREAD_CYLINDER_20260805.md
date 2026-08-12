# Audit: shared-mark macro companion-spread cylinder

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_SHARED_MARK_MACRO_COMPANION_SPREAD_CYLINDER_20260805.md`  
**Method:** symbolic probability and scale audit; no computation

## 1. Partition factor

A prescribed collection whose exact induced partition has `g` macro groups receives exactly `g`
independent common marks, hence mark probability `a^{-g}`.  The cluster
exposure bound contributes `eta^g kappa^(m-g)`.  Relative to the desired
product `(eta/a)^m`, the factor is

\[
                         (a\kappa/\eta)^{m-g}.
\]

A partition with `m-g=c` mergers admits at most `m^{2c}` rooted-star
encodings.  This proves the geometric series in Theorem 1.1.  The encoding
overcounts and is therefore safe.

## 2. Companion scale

At level two, each copy contains the common kernel of rank `r-d+2` and a
private tail of rank `d-2`.  Distinct copies have disjoint tails.  Even after
`h_0-2` tails are forbidden, the next tail orbit has size

\[
                         N_*=\binom{Theta(d^2)-O(d)}{d-2}
                            =\exp(Theta(d\log d)).
\]

The cylinder parameters have scales

\[
 a=Theta(d^2),\qquad eta=Theta(d^{-3}),\qquad
 kappa\le\exp(-Theta(d\log d)).
\]

Therefore for `M=O(d)`,

\[
 M^2a\kappa/\eta
       =\exp(-Theta(d\log d))=o(1).
\]

This is much stronger than required.

## 3. Bank union bound

For one local orbit, the bank intersection has hypergeometric mean
`pN_*`, with `p=O(1/d)`.  Its fixed-relative tail is
`exp(-Omega(pN_*))`.  The logarithm of the crude total number of indexed
local orbits is only `O(k+d log k)=O(d^2)`, while
`pN_*=exp(Theta(d log d))`.  Hence simultaneous survival is valid.

## 4. Scope

The theorem assumes the cluster exposure cylinder `(CE)` for the selected
integral macro packing.  The prospective full orbit and the random-bank
lemma do not imply `(CE)` after adaptive owner exclusions.  In particular,
the theorem does not invoke the coarse same-shore codegree bound as if it
were a selected-factor cylinder.

The result is nevertheless stronger than merely restating `(C2)`: `(CE)`
uses only one-mark macro selection plus a local companion point-mass bound;
the second mark is common inside each physical duplicate macro and is then
generated explicitly.

## 5. Verdict

**PASS, conditional exactly on `(CE)`.**  The probability calculation,
companion-orbit scale, and random-bank preservation are proof-safe.  The
remaining unproved row is the companion-spread integral macro selector.
