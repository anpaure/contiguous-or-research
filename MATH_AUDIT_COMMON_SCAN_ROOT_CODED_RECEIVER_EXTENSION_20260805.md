# Audit: common-scan receiver extension and the root-code bridge

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_COMMON_SCAN_ROOT_CODED_RECEIVER_EXTENSION_AND_ODD_CURRENT_OBSTRUCTION_20260805.md`  
**Method:** literal local-row replay, macro-residue replay, quotient-scope
check, and rooted-path parity; no computation  
**Verdict:** PASS after replacing an unsupported transplant of the old
odd hook marker bank by an explicit even-coordinate odd-mass
capacity-two code.  The common-scan deletion theorem is unconditional.
Finite reset-colour avoidance is proved by background co-selection once
the displayed composition inequality holds.  The odd wrap-current row
remains open exactly as stated.

## 1. Simultaneous scan containment

For an edge supported on pair `p_i`, both endpoints have identical local
states at every other coordinate pair.  If all earlier pairs are quiet,
the scan reaches `p_i`; there the chosen local row exchanges exactly the
two endpoints.  Hence every edge satisfying the triangular prefix
condition belongs to the same scan involution.

When all prescribed edges use one pair put first, no condition on their
contexts remains.  This proves the one-row common-base theorem.  Removing
the endpoints of contained matching edges leaves the remaining edges of
the scan matching, so all augmented receiver Hall cuts are automatically
satisfied.  The same argument applies to a co-designed incoming/outgoing
socket edge.

## 2. Exact correction to the old root-code bridge

The earlier protected marker theorem is native to a hook angle torus of
vacancy length `2h-1`, which is odd.  Its formula

\[
 u_H={\bf1}+\sum_{j\in H}(e_j-e_{j+1})
\]

does not by itself produce an even-coordinate odd-mass capacity-two
sector.  Therefore it cannot alone justify invoking the even scan
theorem.  Fixed marker weight does align the formal workspace sides, but
parity is a separate gate.

The revised theorem supplies the missing object directly.  Two active
coordinate pairs independently take states `12` or `21`, so their four
choices form a literal square.  A third pair fixed at `10` makes the
total mass odd.  Fixed-weight code pairs `00/22` distinguish the square
contexts without changing total mass.  Every selected side is the same
`12-21` edge on the first active pair.  Thus the even common-scan theorem
applies literally.

The macro residues of `12` are `(5,0)` and those of `21` are `(0,5)`.
Deleting the active boundary gives residue five in both cases, hence the
square sides have ordinary critical parent colours.  The construction is
therefore a genuine paired-receiver square, not an arbitrary token
square.

## 3. Quotient check

For fixed background `a`, the necklace quotient group is `Stab(a)`.
Taking `a=(A,0,...,0)` with `A>0` makes that group trivial, so the labelled
scan matching is already a quotient matching.  The equal-sum family
`(A-f,f,0,...)`, `A>2q`, gives independent aperiodic sectors.

This separation is exact for vertices.  It is not automatically exact
for deleted-cut hub colours, because merging coordinates can identify
parent colours arising from different child backgrounds.

The finite-avoidance correction is exact.  For a fixed boundary and a
fixed rooted forbidden parent word, inverse merge consists only of
splitting one entry and has at most `A+1` choices.  Multiplying by child
boundaries, target rotations, and finitely many forbidden colours gives
the stated linear bound.  Proper-period backgrounds have at most the
displayed lower-degree composition count.  Since all bad families are
strictly smaller than the full degree-`n-1` composition family for
`n>=4`, a large-mass aperiodic background avoids every reset colour on
every scan edge.

## 4. Odd check

After one root boundary is cut, every nonwrap edge crosses the path
parity shores and the exact imbalance is

\[
 \Delta_{m,R}=[z^{R-1}](1+z^2+z^4)^m.
\]

A prescribed nonwrap edge removes one vertex from each shore and changes
no imbalance.  A wrap edge changes it by at most two, and one socket by
at most one.  Therefore a fixed bank of `q` receiver edges cannot leave a
nonwrap-completable residue when `Delta_(m,R)>2q+1`.  This validates the
odd obstruction and shows precisely why the even common scan does not
settle the actual hook family.

## 5. Proof-safe frontier

Closed:

1. a fixed finite even receiver bank may be co-designed as one parallel
   local row;
2. all its edges lie in one explicit perfect matching;
3. deletion gives an exact residual matching, eliminating every even
   proper-cut calculation for that bank; and
4. the construction descends on aperiodic backgrounds.

Open:

1. small/zero-background periodic cases not covered by finite avoidance;
2. the macroscopic odd wrap/circulation-ear current; and
3. regeneration of the chosen rooted sectors across levels.
