# Independent audit of `SHIFTED_LINE_SYMMETRIC_BAND.md`

## Verdict

The shifted symmetric-band theorem is correct as stated.  The line ranges,
the exact within-line criterion, the slice-fan dichotomy, the length bound,
and the nonzero boundary cases all check out.  No mathematical correction
is needed.

The result is a genuine two-sided shift of the previously audited direct
line construction: for every `m>=2` and `0<=q<=m-1`, one word of length at
most

\[
 M_m+4q(m+1)(2m+1)
\]

covers every rank from `2m-1-q` through `2m-1+q`.

## 1. Spine and exact line criterion

Put `R=2m-1-q`.  At fixed `(c,d)`, the rank-`R` fibre has

\[
 K=R-c-d,\qquad L=\max(0,K-m),\qquad U=\min(m,K),
\]

and is nonempty exactly when `L<=U`.  These fibres are disjoint and list
every point of `L_R` once.

For an interval with first and last parameters `p<=r`, its maximum is

\[
 (r,K-p,c,d).
\]

Let `|y|=R+s` and keep `y_3=c,y_4=d`.  The endpoints of a possible witness
are forced to be

\[
 p=y_1-s,\qquad r=y_1.
\]

The conditions `L<=p<=r<=U` are equivalent to

\[
 y_1\ge s,\qquad y_2\ge s.
\]

Indeed `p>=0` is `y_1>=s`, `p>=K-m` is automatic from `y_2<=m`,
`r<=m` is automatic from the box, and `r<=K` is exactly `y_2>=s`.
This verifies (2.7), including fibres which meet a coordinate boundary.

Since `q<=m-1`, the base rank satisfies `m<=R<=2m-1`.  Rank numbers of
the symmetric box are unimodal with maximum at `2m`, so

\[
 |L_R|\le M_m.
\]

## 2. Slice-fan coverage

The target band is exactly `R+s` for `0<=s<=2q`.  If the two line
inequalities hold, the preceding interval witnesses the target in the
spine.  Otherwise one of `y_1,y_2` is an integer in

\[
 \{0,1,\ldots,s-1\}\subseteq\{0,1,\ldots,2q-1\}.
\]

The universal three-chain word embedded in that fixed-coordinate slice
therefore witnesses `y`.  This is an internal witness in one appended
block, so neither the ordering of slices nor cross-block maxima matter.

There are at most `2q` relevant values for each of the two fixed
coordinates, hence at most `4q` slice words.  The audited three-chain hook
word has nonzero length `(m+1)(2m+1)-1`.  For a positive fixed coordinate,
the local origin becomes a required nonzero slice target and costs at most
one extra literal; for fixed coordinate zero, the local origin is the
excluded global zero and no extra entry is needed.  Thus

\[
 G_m=(m+1)(2m+1)
\]

is a valid uniform bound per slice, proving the stated total length.

If `2q>m+1`, values `a>m` name empty slices and are simply omitted.  This
does not create a coverage gap: any actual failed coordinate value is at
most `m` and is still among the retained slice indices.  It only makes the
actual word shorter than the displayed upper bound.

## 3. Endpoint and nonzero cases

* For `q=0`, no slice is appended.  Here `s=0`, so every base-layer target
  satisfies the line criterion and the spine alone works.
* For `q=m-1`, the bottom rank is `R=m>0`; the spine entries are therefore
  nonzero.  When `s>m`, the line criterion cannot hold in both coordinates,
  but the failed-coordinate slice argument still applies verbatim.
* In a zero-coordinate slice, use the nonzero three-chain word, so no zero
  entry is introduced.  In a positive-coordinate slice, attaching the
  positive fixed coordinate makes even a local-zero entry globally
  nonzero.
* Concatenating the spine and slice words needs no separator.  All claimed
  witnesses remain wholly inside one block, and extra crossing intervals
  can only add harmless OR values.

Thus the construction is valid in the nonzero-mask problem throughout the
full stated parameter range.

## 4. Asymptotics and scope

The slice cost is

\[
 4q(m+1)(2m+1)=O(qm^2).
\]

Since `M_m=Theta(m^3)`, it is `o(M_m)` exactly under the stated condition
`q=o(m)`.  The proof itself remains valid for every `q<=m-1`; only the
near-width asymptotic conclusion requires sublinear depth.

The note correctly does not infer a full-box theorem.  At linear depth the
independent slice fan costs `Theta(m^3)`, the same order as the central
width.

## 5. Independent finite check

I independently enumerated every point of `[0,m]^4` for `m=2,...,12` and
every `q=0,...,m-1`.  For each case I rebuilt all complete rank-`R`
coordinate-`{1,2}` lines, enumerated every internal interval maximum, and
checked every target in the claimed band.  Each target was either an
actual within-line maximum or had `y_1` or `y_2` in the retained slice
index set.  I also checked that the spine is a duplicate-free enumeration
of `L_R` and that `|L_R|<=M_m`.  All cases passed.

