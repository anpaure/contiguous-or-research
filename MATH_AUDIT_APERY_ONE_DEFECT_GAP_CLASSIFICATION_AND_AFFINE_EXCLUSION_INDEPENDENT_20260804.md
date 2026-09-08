# Independent audit: one-defect cyclic Apéry classification and exclusion

**Date:** 2026-08-04  
**Status:** **PASS after three scope corrections.**  This is a
pure-mathematical audit; no finite search or numerical sign experiment was
used.

## 1. Frozen source

The audited source is

`MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md`

with SHA-256

`9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e`.

The source was corrected during this audit in three places:

1. the classification is stated for `h>=3`; for `h=2` the designation of
   a common versus exceptional gap is not unique;
2. the genuine long-wrap endpoint satisfies the strict inequality
   `a<A/(h+1)`;
3. the final branch-C conclusion distinguishes a nonpositive formal clock
   from a positive formal clock overturned by the finite shoulder.

The current bytes pass all checks below.

## 2. Cyclic classification

From cyclic superadditivity,

\[
s_j\ge s_{j-1}+s_1\quad(2\le j<h),
\qquad
P\ge s_{h-1}+s_1,
\]

so every cyclic gap is at least `gamma_1`.  This immediately gives the
correct sign of an exceptional first or wrap gap.

For an internal exceptional gap at `2<=j<=h-1`, write

\[
\gamma_j=a+\delta,
\qquad
P=ha+\delta,
\qquad
s_r=ra+\delta\,\mathbf 1_{r\ge j}.
\]

If `j<=h/2`, both `s_j` and `s_(h-j)` contain `delta`, and the carry at
sum `h` gives

\[
ha+2\delta\le P=ha+\delta.
\]

If `j>h/2`, then `0<2j-h<j`; the carry at `j+j` gives

\[
2ja+2\delta
\le P+s_{2j-h}
=ha+\delta+(2j-h)a
=2ja+\delta.
\]

In either case `delta<=0`, whereas minimum-gap monotonicity gives
`delta>=0`.  Thus no genuine internal lone defect exists.  The two cases
also cover the boundary `2j=h` without an indexing exception.

The restriction `h>=3` is necessary for the word **exactly** in the
classification.  If `h=2` and `gamma_1<gamma_2`, the same two-gap word can
be called short-first by taking the common value to be `gamma_2`, or
long-wrap by taking it to be `gamma_1`.  The source now removes this
nonuniqueness and cites the complete three-slot theorem for the associated
exact-first-carry clock.

## 3. Affine identity and parameter domain

On the short-first face, with `beta=a-t`,

\[
s_r=ra-\beta\quad(1\le r<h),
\qquad P=ha-\beta.
\]

For `m=qh+r`, the cases `r=0` and `r>0` give respectively

\[
qP=am-\beta q,
\qquad
qP+s_r=am-\beta(q+1).
\]

Since `ceil(m/h)` is `q` in the first case and `q+1` in the second, this
proves the exact clock identity

\[
W_m=am-\beta\left\lceil {m\over h}\right\rceil.
\]

At the exact first carry,

\[
A=P+t=(ha-\beta)+(a-\beta)=(h+1)a-2\beta.
\]

Putting `n=h+1`, the required affine domain follows without an endpoint
loss:

\[
A-(n-2)\beta
=(h+1)a-(h+1)\beta
=(h+1)(a-\beta)>0.
\]

Hence `0<beta<A/(n-2)`, exactly the open domain of the audited all-grid
affine theorem.  The uniform endpoint `beta=0` is separately covered by
reciprocal-ceiling positivity.

## 4. Long-wrap clock and endpoint-period comparison

On the long-wrap face,

\[
s_r=ra,
\qquad P=ha+\delta.
\]

Again splitting `m=qh+r` gives

\[
W_m=am+\delta\left\lfloor {m\over h}\right\rfloor
\]

for both `r=0` and `r>0`.

Under the exact first carry `P+a=A`, one has

\[
\delta=A-(h+1)a>0,
\qquad
P=A-a,
\qquad
a<{A\over h+1}.
\]

The displayed augmented table

\[
(0,a,2a,\ldots,(h-1)a,A-a,A)
\]

is the prefix of the same Bellman clock through capacity `h+1`; the last
entry is inert because its value equals `W_(h+1)`.  For
`m=(h+1)q+i`, `0<=i<=h`, using `q` endpoint generators and the size-`i`
generator yields

\[
W_m\ge qA+c_i.
\]

At `q=0` equality holds.  At `q>=1` both values lie on the increasing
Gaussian tail, so summing by residues proves exactly

\[
\Phi(W)\ge
C+\sum_{i=1}^{h-1}F(ia)+F(A-a).
\]

There is no missing residue, reversal of the kernel inequality, or
finite-head loss in this comparison.

If `(h-1)a<=A/2`, every term `F(ia)` with `2<=i<=h-1` is positive, while
the remaining pair obeys

\[
F(a)+F(A-a)>-1/20000.
\]

Together with `C>43/1000`, this gives the stated strict positive margin.
Combining failure of this sufficient condition with the genuine
long-wrap inequality gives the precise open interval

\[
h\ge4,
\qquad
{A\over2(h-1)}<a<{A\over h+1}.
\]

For `h=3` the two bounds meet at `A/4`, and the strict upper bound makes
the interval empty.  The source therefore correctly closes `h=3` and
does not accidentally retain a boundary point.

## 5. Exact branch-C logic

The parent trichotomy supplies

\[
\Phi(V)=\Phi(W)+\mathcal H(V,W).
\]

Thus positivity of a uniform or short-first **formal** clock does not by
itself exclude a nonpositive original clock: a finite negative shoulder
may overturn it.  The corrected source now makes the exhaustive disjoint
split:

1. `Phi(W)>0`, forcing
   `mathcal H(V,W)<=-Phi(W)<0`;
2. `Phi(W)<=0` with a one-defect word, forcing the unresolved near-uniform
   long-wrap interval;
3. `Phi(W)<=0` with no value shared by all but at most one gap.

This is the precise consequence.  The boxed long-wrap/multidefect
narrowing applies only to the nonpositive formal-clock branch.  In the
actual minimal branch, `N=n=g+1` and `n>=6`, so `g=n-1>=5`; the standalone
`h=2` convention issue cannot re-enter this corollary.

Threshold overshoot, a later crossing, and elimination of the finite
shoulder remain explicitly outside scope.

## 6. Dependency check

All dependency hashes printed in the frozen source agree with current
bytes.  In particular, the audit checked the all-grid affine theorem and
audit, reciprocal-ceiling theorem and audit, threshold reflection/compact
train theorem and audit, sharp threshold ceiling-margin theorem and audit,
the complete three-slot theorem and audit, and the parent Apéry trichotomy
and audit.

## 7. Verdict

The corrected theorem is **GO**.

It proves a complete one-defect classification for `h>=3`, closes the
short-first exact-first-carry face by the affine theorem, closes a broad
long-wrap range by a literal endpoint-period comparison, and narrows a
nonpositive formal exact-first-carry clock to the strict interval above or
to a genuinely multidefect gap word.  It does not prove positivity in the
remaining long-wrap interval and does not eliminate the original clock's
finite-shoulder alternative.
