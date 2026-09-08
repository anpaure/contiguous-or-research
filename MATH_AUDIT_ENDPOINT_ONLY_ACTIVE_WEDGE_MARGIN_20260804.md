# Audit of the endpoint-only active-wedge margin

**Date:** 2026-08-04  
**Method:** pure-mathematical replay; no computation, search, or solver  
**Audited theorem:** MATH_THEOREM_ENDPOINT_ONLY_ACTIVE_WEDGE_MARGIN_20260804.md  
**Audited SHA-256:** 1c443748c354042951c485cf52289b7db5bf349c3b75151ef73b8978d1e13093

## Verdict

**GO at the stated endpoint-factorized fixed-state scope.**

For a source with \(a\) star-active owner sides, unsupported wedges are
exactly the \({m-a\choose2}\) pairs using two inactive sides.  Removing
\(t\) distinct supported terminal pairs therefore leaves exactly

\[
 {m\choose2}-{m-a\choose2}-t=B_a(m)-t
\]

active wedges.

The exact protected-wedge packing theorem needs a strict menu floor above
\(B_{p-1}(m)\).  Since

\[
 B_p(m)-B_{p-1}(m)=m-p,
\]

the rows

\[
 a\ge p,\qquad t\le m-p-1
\]

leave at least \(B_{p-1}(m)+1\) active candidates.  The selected
owner/terminal ledger then makes any chosen active side private.

Sharpness is correct.  With \(a=p-1,t=0\), the menu has exactly the
blockable size \(B_{p-1}\).  With \(a=p\), forbidding the \(m-p\) new edges
introduced by the \(p\)-th active star again leaves exactly
\(B_{p-1}\).

The theorem explicitly assumes universal star activity apart from the
listed terminal holes.  Ordinary gammoid nonloops, marginal activation in
different states, and factor occurrence names alone do not imply that
premise.
