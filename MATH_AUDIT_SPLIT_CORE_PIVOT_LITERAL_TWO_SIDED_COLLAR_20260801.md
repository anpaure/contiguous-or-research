# Independent audit: split-core pivot and literal two-sided collar

Date: 2026-08-01  
Object audited:
`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md`  
Verdict: **GO after three proof-safe wording corrections.**

The construction is a genuine source-level construction, not merely an
owner-level path.  For every

\[
 h\ge2,\qquad r-h\ge2,\qquad 2\le |X|\le r-h,
 \qquad k\ge r+3h,
\]

the displayed `4h+1` nonempty source letters have exactly the asserted
depth-`h` row.  The pre-insertion row, arbitrary-width monotone transport,
two immediate palettes, residence ledger, new short-cell ledger, and
label count all check exactly.  The common-cap/compiler conclusion remains
conditional in precisely the way stated in Section 5; no global host,
exterior guard, or regeneration theorem follows from this local audit.

## 1. Exact source factorization

Write the final word as five consecutive pieces

\[
 A^-\;\;\Lambda^*\;\;[X]\;\;P^*\;\;A^+,
\]

of lengths `h,h,1,h,h`.  Here `A^-` is the left seam block,
`Lambda^*` is the lambda block ending in
`C union X_L union {lambda_h}`, `P^*` is the rho block beginning in
`C union X_R union {rho_1}`, and `A^+` is the right seam block.
Consequently the word has length `4h+1` and its depth-`h` row (windows of
`h+1` letters) has length `3h+1`.

The first such window contains

\[
 B-\{x_R\},\ q^-,\ D^-,\ \lambda_1,
\]

and is exactly `L_0`.  Each of the next `h-1` slides loses
`d^-_{t+1}` and gains `lambda_{t+2}`, yielding
`L_1,...,L_{h-1}`.  The following slide loses the left seam letter and
gains `X`; all of `X_R-{x_R}` is retained while `q^-` is replaced by
`x_R`, so the result is `M_0`.  The central `h` slides successively make

\[
 \lambda_{j+1}\longmapsto\rho_{j+1},
\]

and yield `M_1,...,M_h`.  At the right seam `X` leaves and the right seam
letter enters, replacing `x_L` by `q^+`; the remaining slides replace
`rho_{t+1}` by `d^+_{t+1}`.  This gives exactly

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}.
\]

This verifies the claimed `D^h` identity literally.

## 2. Limiting case `h=2` and singleton shores

The empty singleton ranges in the notation cause no degeneracy.  When
`h=2`, `C` may be empty, and
`X_L={x_L}`, `X_R={x_R}`, the word is

\[
 \begin{aligned}
 &(\{x_L,d^-_1\},\{q^-\}),
 (\{\lambda_1\},\{x_L,\lambda_2\}),\{x_L,x_R\},\\
 &(\{x_R,\rho_1\},\{\rho_2\}),
 (\{q^+\},\{x_R,d^+_1\}).
 \end{aligned}
\]

All nine letters are nonempty, and the seven length-three unions are

\[
 L_0,L_1,M_0,M_1,M_2,R_0,R_1.
\]

Thus the edge case specifically requested by the audit is valid.  More
generally, the seam letters remain nonempty even when either shore minus
its distinguished element is empty because they contain `q^-` and `q^+`.

The theorem statement did need to expose the implicit feasibility
hypotheses `r-h>=2` and `k>=r+3h`; these have now been added.

## 3. Pre-insertion row and arbitrary-width transparency

After deleting the central one-letter cell `[X]`, the adjacent letters are

\[
 Q_L=C\cup X_L\cup\{\lambda_h\},\qquad
 Q_R=C\cup X_R\cup\{\rho_1\}.
\]

Their union contains `B=C union X_L union X_R`, hence contains `X`.
Every old interval that crosses the cut contains both `Q_L` and `Q_R`, so
adding `[X]` changes none of its coordinates.  Intervals wholly on either
side transport by the obvious index shift.  This gives an injective
occurrence map from **every** old interval, not only the short or owner
rows, to an equal-valued final interval.  The result therefore holds in an
arbitrary fixed exterior context.

The old crossing windows of `h+1` letters are, in order,

\[
 U_j=B\cup\{\rho_1,\ldots,\rho_{j+1}\}
       \cup\{\lambda_{j+1},\ldots,\lambda_h\}
     =M_j\cup M_{j+1}\quad(0\le j<h).
\]

Each has rank `r+1`.  All noncrossing owner windows remain the `L` and `R`
blocks, establishing the stated pre-insertion row exactly.

## 4. Immediate palettes

All owners have rank `r`, and every transition exchanges one label.  For
clarity, the lower and upper colours split into five disjoint signature
classes:

1. left-internal colours contain `q^-`; their moving `D^-` boundary makes
   them mutually distinct;
2. the left seam has lower colour `(B-{x_R}) union Lambda` and upper colour
   `B union {q^-} union Lambda`; unlike every left-internal upper colour it
   contains no `D^-` label;
3. central colours have the usual distinct rho-prefix/lambda-suffix
   signatures and contain the full base `B` but no seam label;
4. the right seam is the analogous pair based on
   `(B-{x_L}) union P` and `q^+`;
5. right-internal colours contain `q^+` and are separated by their moving
   `D^+` boundary.

Freshness of the displayed external labels separates these classes.  This
also works unchanged for `h=2`.  Hence both q1 palettes are injective.

## 5. Residence

The exact run ledger in the owner word is:

\[
 \begin{array}{c|c}
 \text{coordinate}&\text{run}\ \\ \hline
 \lambda_j&L_{j-1},\ldots,L_{h-1},M_0,\ldots,M_{j-1}\\
 \rho_j&M_j,\ldots,M_h,R_0,\ldots,R_{j-1}
 \end{array}
\]

and each of these runs has length `(h-j+1)+j=h+1`.
Every coordinate in `C`, `X_L-{x_L}`, or `X_R-{x_R}` persists through the
whole block.  The `x_L` run goes from the left endpoint through `M_h`, and
the `x_R` run goes from `M_0` through the right endpoint; both have length
`2h+1`.  Only the `D^-,q^-` runs clipped at the left endpoint and the
`D^+,q^+` runs clipped at the right endpoint can be shorter than `h+1`.
Thus all internal runs satisfy residence, while exactly the named endpoint
flags require exterior continuation.

This is an owner-run statement backed by the literal source factorization
in Section 1, so there is no remaining local antecedent assumption.

## 6. New short cells and compiler scope

Among final intervals of at most `h` letters, the intervals outside the
old transport image must contain `[X]` and lie wholly on only one side of
the cut (or consist of `[X]` alone).  They are exactly

\[
 [X],\qquad
 B\cup\{\lambda_{h-i+1},\ldots,\lambda_h\},\qquad
 B\cup\{\rho_1,\ldots,\rho_i\},\quad1\le i<h.
\]

The `h-1` old crossing intervals of exactly `h` letters are the values
`M_1,...,M_{h-1}`.  They have rank `r`, so no strict-lower target can have
used them in the reference matching.  All shorter old crossing intervals
remain within the short band after insertion and transport with the same
value.

Therefore the local compiler operation is exact **provided** the ambient
flat monotone-pivot hypotheses hold: the reference occurrence matching
omits the new task `X`, the actual old occurrences of all `2h-2` ray-target
vertices are released, the displayed new occurrences pass the same caps
and guards, and the operation lives in one common maximal-word ledger.
The construction itself does not prove those global occurrence/cap facts.

The original note called `[X]` a “singleton task.”  Since the theorem
requires `|X|>=2`, this was semantically misleading: it is a one-letter
cell whose set-value is `X`, not a singleton subset.  The wording has now
been corrected.

## 7. Ground count and final scope

There are `r-h` labels in `B`, `2h` labels in the lambda/rho banks, two seam
labels, and `2(h-1)` labels in the two `D` banks.  Hence the exact label
count is

\[
 (r-h)+2h+2+2(h-1)=r+3h.
\]

No label can be identified without a new collision analysis, so the stated
construction requires `k>=r+3h`.  The audit proves only this local packet.
It does not prove a global upper-exact Hamilton host, exterior completion of
the clipped flags, common-cap admissibility, or bounded regeneration.  The
case `|X|=1` is genuinely outside this split-core construction.

## Audit conclusion

After making the following corrections, the theorem is proof-safe:

- expose `r-h>=2` and `k>=r+3h` in the hypotheses;
- distinguish the one-letter cell `[X]` from a singleton-valued target;
- make the nonemptiness explanation cover every source letter, including
  the singleton-shore limit.

No algebraic or combinatorial counterexample was found.  The factorization
is exact for all stated parameters, including `h=2`, and all global claims
remain explicitly conditional.
