# Audit of the common-core tight-path fusion sufficient theorem

Date: 2026-07-26

Source audited:
`MATH_THEOREM_COMMON_CORE_TIGHT_PATH_FUSION_SUFFICES_20260726.md`.

## 0. Verdict

After one necessary parameter correction and an explicit delayed-atom
compilation, the reduction is valid.  CCTPF is a single self-contained
integral theorem sufficient for

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

The necessary correction is substantive: merely assuming
\(H=(1+o(1))\sqrt{m\log m}\) does not control
\(\Lambda=W/N_H\) to additive \(O(H)\).  The common-core ledger needs the
calibrated crossing hypotheses

\[
L+c_0H\le\Lambda\le m+C_0H.
\]

They hold, for example, for
\(H=\lfloor\sqrt{m\log m}\rfloor\).  This exact condition and the
literal compilation have been patched into the source.

## 1. Why the calibration correction is necessary

The relation

\[
\log {W\over N_H}={H^2\over m}+o(H/m)
\]

at the required local precision shows that a displacement
\(H-\sqrt{m\log m}\) of order \(\sqrt{m/\log m}\) changes
\(\Lambda\) by a constant factor.  Such a displacement is still a
relative \(o(1)\) perturbation of \(H\).  Therefore the unqualified
asymptotic condition permits \(\Lambda\gg m\), in which case
\(LN/W=L/\Lambda\) is bounded away from one and the middle leave is not
\(o(W)\).

For \(H=\lfloor\sqrt{m\log m}\rfloor\), write
\(H=\sqrt{m\log m}+c\), \(-1<c\le0\).  The audited expansion gives

\[
\Lambda=m+2cH+o(H),
\]

and hence

\[
\Lambda-L=(3+2c)H+o(H)=\Theta(H).
\]

Thus fixed positive \(c_0,C_0\) exist and all common-core estimates
apply.

## 2. Literal compilation of one selected path

Fix one top and let \((X_i)\) be its full cyclic row of middle owners.
The core-safe phases form a consecutive segment
\(i_0,\ldots,i_0+L-1\).  Define

\[
B_j=\bigcap_{a=0}^{H}X_{j-a}.
\]

Because the owners are cyclic length-\(m\) intervals in a cyclic
\((m+H)\)-word, every segment of at most \(H\) transitions is a Johnson
geodesic, and every nonconstant positive coordinate run has length
\(m\ge H+1\).  Thus the row satisfies \(G_H+P_H\), and the exact atom
identities are

\[
\bigcap_{t=0}^{q}X_{i+t}
=\bigcup_{j=i+q}^{i+H}B_j,
\qquad
\bigcup_{t=0}^{q}X_{i+t}
=\bigcup_{j=i}^{i+H+q}B_j,
\qquad0\le q\le H.
\]

These are the promotion lower and upper traces, after the common harmless
phase reindexing.  The word

\[
B_{i_0},B_{i_0+1},\ldots,B_{i_0+L-1+2H}
\]

has \(L+2H\) letters and contains every witnessing atom interval for
every one of the \(L\) retained phases through depth \(H\).  Empty atoms
may be deleted because every intended mask is nonempty.  Hence one path
really costs at most \(L+2H\), including both boundary collars.  No seam
letter is needed when path blocks are concatenated.

The compiler may cover traces at phases whose stopping tag is smaller
than the depth.  This only helps.  CCTPF's active traces provide a certified
distinct subset of the covered targets and therefore give an upper bound
on the repair count.

## 3. Exact central ledger

There are \(N=N_H\) tops.  The path blocks cost at most

\[
N(L+2H)=LN+2HN.
\]

CCTPF makes the \(LN\) middle owners distinct.  Appending the other
\(W-LN\) middle masks changes the baseline exactly to

\[
W+2HN.
\]

At each internal signed depth \(1\le q<H\), exactly \(b_qN\) active
traces on either sign are globally distinct.  Thus at most
\(N_q-b_qN\) masks need literal repair on each sign.  Since no phase has
tag \(H\), appending both full boundary layers costs \(2N\).  The total
central length is therefore at most

\[
W+2HN+2N+2\sum_{q=1}^{H-1}(N_q-b_qN).
\]

The audited rank ledger says

\[
(W-LN)+2N+2\sum_{q=1}^{H-1}(N_q-b_qN)
=O(H^{3/2}N)=o(W).
\]

In particular the signed-repair portion alone is \(o(W)\), while

\[
HN=O(HW/m)=o(W).
\]

There is no double-counting of the middle leave: it is absorbed when
\(LN\) is replaced by \(W\), and its appearance in the audited ledger is
used only to upper-bound the remaining nonnegative repair terms.

## 4. Boundary and product-SCD interface

The central compiler and literal repairs cover every rank in
\([m-H,m+H]\).  The two rank-\(m\pm H\) layers each have \(N_H=N\)
targets, so the boundary charge \(2N=o(W)\) is correct.

Take the product-SCD parameter

\[
r=m-H-1.
\]

Its word covers every nonempty set of rank at most \(m-H-1\) or at least
\(m+H+1\).  Thus it meets the central word with neither a gap nor a need
for overlap.  Its exact length satisfies

\[
L_m(m-H-1)le C
\exp\left(-{H^2\over8m}\right)W.
\]

At calibrated height, \(H^2/m=(1+o(1))\log m\), so this is
\(O(m^{-1/8+o(1)}W)=o(W)\).  Concatenating this independent block cannot
destroy any witness already present in the central blocks.

## 5. Parity transfer

The trimmed lift gives exactly

\[
\nu(2m+1)\le2\nu(2m).
\]

Since

\[
\binom{2m+1}{m}={2m+1\over m+1}\binom{2m}{m},
\]

one has

\[
{2\binom{2m}{m}\over\binom{2m+1}{m}}
={2(m+1)\over2m+1}=1+O(1/m).
\]

Therefore a coefficient-one result in all even dimensions transfers to
all odd dimensions with no asymptotic loss.

## 6. Exact surviving sufficient theorem

For the calibrated choice of \(H\), suppose one can choose, for every
rank-\(m+H\) top, one core-safe ordered tail and one nested tag profile
with the prescribed \(b_q\)'s such that the middle active masks and both
signed active trace families are globally injective at every internal
depth.  Then the delayed-atom blocks, literal missing-mask repairs, and
the product-SCD exterior concatenate to a literal word of length
\(W+o(W)\).  The trimmed lift supplies the other parity.

No further completion, absorber, seam theorem, or exterior compatibility
is needed *after* CCTPF.  What remains open is exactly CCTPF itself: the
integral selection of one ordered path and one nested history per top.
