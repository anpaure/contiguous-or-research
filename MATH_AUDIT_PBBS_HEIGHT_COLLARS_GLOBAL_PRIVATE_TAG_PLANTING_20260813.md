# Hostile audit of global private-tag planting for synchronized PBBS height collars

**Date:** 2026-08-13  
**Audited file:**
`MATH_THEOREM_PBBS_HEIGHT_COLLARS_GLOBAL_PRIVATE_TAG_PLANTING_20260813.md`  
**Audited SHA256:**
`e1cb69065220b01e4f017d5a3d69addedecf89da83b869876fa50ae81e5c0544`  
**Verdict:** **FAIL at the claimed all-five path-forest and factor-extension
conclusions.**  The common-tail formula, parameter inequalities, and
missing-tag separation of collar interiors are correct.  They do not remove
the forced adjacent-height endpoint overlap.  The audited file incorrectly
asserts that the pentagon endpoints are pairwise distinct across heights.

## 1. The exact counteridentity

Use the audited high-pentagon notation

\[
 P_{h,i}=[2r+1]\setminus g(Z_h^i),\qquad
 Q_{h,i}=[2r+1]\setminus Z_h^i.                    \tag{1.1}
\]

For every adjacent high height,

\[
                 g(Z_h^0)=Z_{h-1}^1.               \tag{1.2}
\]

Taking complements gives

\[
                 \boxed{P_{h,0}=Q_{h-1,1}=U_h.}    \tag{1.3}
\]

This is the binding endpoint identity proved in
`MATH_AUDIT_PBBS_TAGGED_COLLAR_ENDPOINT_OVERLAP_AND_RANK_STRATIFIED_BACKUP_20260806.md`.
It is not contradicted by disjointness of the exchange states `Z_h^i`:
the two endpoint families are obtained through different maps, `g` and the
identity.  Separate injectivity of those maps does not make their images
disjoint from each other.

After simultaneous head shifts, the role-zero rethread edges form the
height spine

\[
                 \cdots-U_{h-1}-U_h-U_{h+1}-\cdots.\tag{1.4}
\]

Those two spine edges already occupy both factor degrees at `U_h`.  The
claimed incoming role-zero collar ends at `P_(h,0)=U_h`.  Its next owner
misses its private tag, whereas both spine neighbours contain the entire tag
bank, so its incident edge is distinct from both spine edges.  Thus the
protected degree at `U_h` is three.

Consequently:

* item 1 of Theorem 0.1 is false;
* the union is not an incidence path forest;
* the polynomial protected-forest theorem is inapplicable; and
* the spanning two-factor conclusion in Section 4 does not follow.

No probability estimate or alternative choice of the deletion sets
`D_(h,i)` changes (1.3).

## 2. What survives the audit

The literal core calculation

\[
 G_h=\{h+2,\ldots,2h\}\mathbin{\dot\cup}
     \{2h+4,2h+6,\ldots,2r\}                      \tag{2.1}
\]

is correct, as are

\[
 J_H=\{2H+2,2H+4,\ldots,2r\}\subseteq G_h,
 \qquad |J_H|=r-H.                                  \tag{2.2}
\]

Writing `N=5(H-4)`, the two inequalities

\[
 N\le r-H,\qquad N+\delta\le r+1                 \tag{2.3}
\]

do permit distinct global tags and deletion sets of size `delta-2` which
contain exactly the private tag.  For every positive-time collar owner and
every collar lower colour, the tag trace is exactly

\[
                         T\setminus\{g_{h,i}\}.    \tag{2.4}
\]

Therefore collar **interiors** on different paths are mutually distinct and
avoid every all-tag pentagon resource.  Within-path simplicity remains the
audited sliding-window theorem.  These are useful unconditional conclusions.

The convenient implication `6H<=r+20` is also arithmetically correct when
`delta<=H`, and the eventual deadline estimate is valid.  These inequalities
control tag supply only; they do not control endpoint degree.

## 3. Correct scope

The proof can be retained after replacing its main conclusion by:

> The global tag bank makes all positive-time synchronized-collar owners
> and all collar lower colours resource-disjoint from one another and from
> the fixed pentagon bank.  The endpoint identity (1.3) remains, so an
> all-five incidence path forest requires a fused adjacent-height collar or
> a replacement of one spine incidence.

The already audited endpoint-corrected construction—four incoming collars
and one outgoing role-zero collar at each high height—does yield a protected
path forest and may be extended after adding its rank-stratified upper
backups.  It no longer has literal zero complete exterior current; its
alternative witness bank pays that residual current.

The two direct ways to recover the all-five current theorem are still:

1. a shared collar that reuses a spine edge while retaining the common
   cumulative-union profile; or
2. an alternating physical lift of the minimal three-edge zero-seam repair
   ear, creating a positive-length intercut arc to which a full collar can
   attach.

Neither is supplied by the audited file.

