# Audit of the protected tight-wreath nonextension certificate

**Date:** 2026-08-13  
**Audited source:**
`MATH_OBSTRUCTION_PROTECTED_TIGHT_WREATH_ROWS_NOT_HEREDITARILY_EXTENDABLE_20260813.md`  
**Source SHA-256:**
`6caf88c82ec11d5d92e0ad4a4e9c3055d50da7796ff85fe984c29d213ad8fff6`  
**Verifier SHA-256:**
`60daf6f8a6f8dc6dc78a77a2a4abbb0bc36ce5dbfa792bb1586986e2ea6f64b7`  
**Method:** direct forced-window and Farkas arithmetic, plus an independent
run of the frozen standard-library verifier on `h100`.  
**Verdict:** **PASS** for Theorem 1.1 and its rational nonextension
certificate.  The `m=4` census remains explicitly finite computational
context, not a theorem dependency.

## 1. Forced and uncovered rows

The cyclic length-three windows of

\[
                         (0,1,2,3,4,5,6)                   \tag{1.1}
\]

are

\[
                         012,123,234,345,456,056,016.      \tag{1.2}
\]

Those of

\[
                         (0,2,5,1,3,6,4)                   \tag{1.3}
\]

are

\[
                         025,125,135,136,346,046,024.      \tag{1.4}
\]

The lists are disjoint.  Removing them from all
`binom(7,3)=35` triples leaves exactly the twenty-one triples in (2.3).
Thus an exact factor containing the two rows would require three further
rows supported entirely on that uncovered set.

## 2. The Farkas sign is correct

The certificate gives four uncovered triples weight `-1`, three weight
`+1`, and all others zero.  Therefore the residual all-ones target has
weight

\[
                              -4+3=-1.                     \tag{2.1}
\]

There are `(7-1)!/2=360` unoriented cyclic rows.  The frozen verifier
canonically roots each at zero, filters for rows disjoint from the fourteen
forced windows, and obtains exactly the twenty rows displayed in
(3.4)--(3.5).  On `h100` it reproduced the score vector

\[
 0,0,0,1,0,0,0,0,0,0,
 1,0,1,1,1,1,1,1,0,0,                                  \tag{2.2}
\]

in the displayed row order.  Every eligible column consequently has
nonnegative certificate weight.

If nonnegative coefficients `lambda_c` fractionally covered every
uncovered triple once, then summing the certificate over columns would
give

\[
 \sum_c\lambda_c y(R(c))\geq0,                            \tag{2.3}
\]

whereas summing over the required residual row loads gives `-1` by (2.1).
This contradiction is valid without any cardinality or integrality
assumption.  The residual face is rationally empty.

## 3. Exact scope

The certificate refutes hereditary extension from arbitrary pairwise
window-disjoint prescribed rows.  It says nothing negative about a
covariant special family of clean-package rows, or about trades which keep
only the genuinely protected arcs and alter the rest of their host rows.

The symmetry-reduced `m=2,3,4` statistics in Section 4 are correctly
labelled computational context.  The human theorem uses only the two
forced lists, the twenty eligible lists, and the Farkas weights audited
above.
