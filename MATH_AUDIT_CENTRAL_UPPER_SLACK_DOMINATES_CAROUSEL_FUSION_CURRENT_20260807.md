# Audit of central upper slack versus carousel fusion current

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_CENTRAL_UPPER_SLACK_DOMINATES_CAROUSEL_FUSION_CURRENT_20260807.md`  
**Verdict:** PASS as an unconditional scalar theorem, conditional on the
stated component-size premise.  It proves only the full-shore capacity
row.  It does not imply any named-target Hall inequality, nor does it show
that a palette-neutral pentagonal packet bank fits in the same scalar
budget.

## 1. Binomial inequalities

For (k=2m,R=m), put

\[
 a_s=\frac{\binom{2m}{m+s}}{\binom{2m}{m}}.
\]

The base value is (a_1=m/(m+1)), and

\[
 \frac{a_s}{a_{s-1}}
 =\frac{m-s+1}{m+s}
 \le \frac{m-s+1}{m-s+2}.
\]

Induction gives (a_s\le(m-s+1)/(m+1)), hence

\[
 W-\binom{2m}{m+s}\ge \frac{s}{m+1}W.
\]

For (k=2m-1,R=m), the analogous ratio is

\[
 \frac{b_s}{b_{s-1}}=\frac{m-s}{m+s},
\]

with (b_1=(m-1)/(m+1)\le(m-1)/m).  This yields

\[
 W-\binom{2m-1}{m+s}\ge \frac{s}{m}W.
\]

Theorem 1.1 is correct over its full stated ranges.

## 2. Component comparison

Under the explicit hypothesis that every component size belongs to

\[
 \{M-2,M-1,M\},\qquad M=k-R+d+1,
\]

and (d\ge2), the minimum size is at least (m+1) in the even case and
at least (m) in the odd case.  Therefore the component count satisfies
the displayed bound (2.2), and substitution into Theorem 1.1 gives

\[
 S_s\ge cs.
\]

This calculation is exact.

**Scope.**  The three-size premise is not a consequence of the general
maximal unified-rail formula alone: a general maximal type has

\[
 N=M-r_0,\qquad0\le r_0<p\le d+1.
\]

The audited theorem properly states the three-size condition as a
hypothesis.  Any later application must prove that its selected component
bank actually has (r_0\le2), or redo the comparison using its true
minimum size.

## 3. Fusion-current indexing

At upper offset (s), the source interval length is

\[
 j=d+1+s.
\]

The unified rank formula gives rank (R+s), and one changed seam deletes
exactly (j-d-1=s) old crossing occurrences while crossing paths meet at
most one seam.  Thus (c) changed seams have scalar current (cs), as
claimed.

For terminal widths, full-period targets and paths meeting several seams,
this calculation is not the relevant literal ledger.  Section 3 explicitly
excludes that range.

## 4. Meaning of the duplicate count

Suppose the pre-fusion rank-(R+s) row is complete and has multiplicity
(\mu_s(T)\ge1) for every named target (T).  Its exact deletable
duplicate capacity is

\[
 b_s(T)=\mu_s(T)-1,
 \qquad
 \sum_T b_s(T)=W-\binom{k}{R+s}=S_s.
\]

Thus (S_s) is an actual duplicate bank only after rank-(R+s)
completeness has been established.  Without completeness it is merely the
excess of occurrence slots over the number of possible names.

Moreover, the equality above is a sum over names.  It does not say that
the names exposed at candidate seams have capacity.  Deleting several
occurrences of one duplicated name is safe only up to
(\mu_s(T)-1), not merely because each occurrence initially belongs to a
name of multiplicity at least two.

The source's final paragraph correctly leaves precisely this
occurrence-labelled selection open.  Subject to these scope statements,
no correction to the scalar theorem is needed.
