# Independent hostile audit: parity-tail endpoint rotation

**Date:** 2026-08-13  
**Verdict:** **PASS.**  
**Frozen source:** `MATH_THEOREM_PARITY_TAIL_ENDPOINT_ROTATION_INSTALLS_FIRST_COMPOUND_SEAM_20260813.md`  
**Source SHA-256:** `809269c1eb2aec6d46a471eee15285a4b7e7c42c10e28893aaa1950ba3fee0bb`  
**Verifier SHA-256:** `6a10102d94815477dc78e20125a5188e628e81ede400a52c145f59817b90484a`

This audit checked the formulas symbolically and independently replayed the root-local
verifier on H100.  The replay covered every \(10\le m\le40\), and additionally
\(m=41,64,65,100,101\), using deadlines satisfying \(m\ge3d+2\).

## 1. Ladder indexing and endpoint

Write \(m=2s\) or \(2s+1\).  In both cases

\[
 t_m=s-2.
\]

The path has the two initial exchanges, \(t_m-3\) middle exchanges, and one final
exchange, hence exactly \(t_m\) edges.  The moving label progresses

\[
 b_m, b_m+4, b_m+8,\ldots,b_m+4(t_m-3), 2m-2.
\]

Substitution of \(b_m=11\) for even \(m\) and \(13\) for odd \(m\) shows that the
penultimate label is the one required by the displayed old endpoint \(B\).  Direct
cancellation of the exchanges gives \(Q_{t_m}=B\).

For every root in (3.4),

\[
 a_r=2r-4+(m\bmod2),qquad
 c_r=m-2r-6-(m\bmod2).
\]

The range \(2\le r<t_m\) makes both exponents nonnegative.  At its final value
\(r=t_m-1\), one has \(c_r=0\) in both parities.  Thus (3.4) is a literal length-
\(2m\) Dyck root at every endpoint; no negative-power convention is hidden.

The backup family (6.6) uses the same \(a_r,c_r\).  Its special \(a_r=0\) branch
occurs exactly at the even base rung \(r=2\).  In the other branch \(a_r>0\), and
the length identity

\[
 12+2(a_r-1)+8+2c_r+2=2m
\]

is exact.  This verifies the two most fragile index formulas.

## 2. Literal first-aligned membership

For every displayed positive host root, the verifier does all of the following rather
than merely searching the completed factor:

1. checks that the word is Dyck of length \(2m\);
2. checks that its displayed `1100` is the first eligible aligned block at a position
   congruent to zero modulo four;
3. forms its literal `1010` mate;
4. applies the inverse-pair normal form to those two canonical MSW rows; and
5. finds the claimed old coloured edge in exactly one of the two resulting positive
   rows, with the displayed moving endpoint.

For the four unchanged repair rows it verifies that no eligible aligned block exists,
so those rows really remain canonical in the complete first-aligned factor.  Hence the
test is an exact reconstruction of membership in the actual factor, not an ambient-row
or rank-only check.

The two-shell recurrence

\[
 \rho(W_{j+2})=(2M_j+4,2,\rho(W_j)+2,2M_j+3,1)
\]

explains the all-\(m\) induction: increasing a rung adds two shells, translates the
old distinguished window by two, and appends the same terminal labels on the source
and backup sides.  The bounded base roots are precisely the separately displayed
formulas (3.1)--(3.3).  The H100 replay agreed at every tested rung and both parities.

## 3. Colour and owner ledger

The fixed path contributes five colours, the tail ladder contributes \(t_m\), the seam
one, and the repair circuit six.  The exceptional-marker profiles and the changing
tail defect make all of them distinct, giving

\[
 (5+t_m+1)+6=t_m+12.
\]

On the seam trade, the two open-path moving-owner defects are \(-C+A\) and
\(-U+B\), while the seam contributes \(-A-B+C+U\).  They cancel exactly.  The
repair walk is closed.  Stationary endpoints never change degree, so every owner
retains degree two and every changed facet retains its colour once.

## 4. Portal separation

The selected portal rows come from packet pairs whose first aligned block is at bit
zero.  Every changed positive host row here belongs to a different first-aligned
packet, at bit four, eight, or twelve; unchanged repair hosts have no eligible aligned
block.  The complete packet factor partitions rank-\(m\) windows, so distinct factor
rows have disjoint facet decks.  This proves colour-level portal avoidance.

The verifier also constructs the actual selected positive portal rows for every
admissible \((A,q)\) and intersects their facet decks with the changed colours.  It
found zero hits in every replay.  The theorem freezes portal rows at the colour/row
level; it does not claim that unrelated protected owner occurrences outside those rows
are untouched.

## 5. Upper-support backups

For each root in (6.2)--(6.8), the verifier reconstructs the canonical or positive
factor row and finds a literal cyclic window of length \(m+2\) equal to the named old
upper value.  It canonicalizes every changed host row and requires the chosen backup
row not to be among them.  Therefore every net-lost upper target retains at least one
untouched occurrence.

This is exactly what support monotonicity needs.  A target may be the negative current
of more than one changed edge, but the net current first cancels positive terms; one
additional untouched occurrence then guarantees final load at least one, regardless
of its original changed multiplicity.  The verifier checks

\[
 \operatorname{supp}(\mu^-_{\rm net})
 \subseteq\{\text{targets with an untouched displayed backup}\}.
\]

The cancellations quoted in Theorem 6.2 also replay literally.  Thus the conclusion is
old-upper-support preservation, not multiplicity preservation or universal coverage,
as stated.

## 6. Sharing/conjugation scope

The audit sees no proved way to conjugate this first-seam trade across all heights.
The middle tail ladder is suggestive of a reusable trunk: adjacent height seams should
alter only bounded head markers while translating much of the alternating tail.
However, the complete first-aligned MSW factor is not invariant under an arbitrary
coordinate conjugation, and the bit-zero portal bank further breaks that symmetry.
Moreover one open ladder carries only two endpoint defects; installing several seams
requires a branched or telescoping current identity, not independent reuse of the same
colours.

A plausible next target is therefore a multi-terminal endpoint-rotation tree whose
height paths share a parity-tail trunk and whose branch currents cancel before the
upper-backup ledger is applied.  No such shared-trunk theorem follows from the present
single-seam certificate, so the source correctly charges \(\Theta(m)\) colours and
leaves repetition open.
