# Independent hostile audit: Catalan-scale low-exposure rails need not extend

**Date:** 2026-08-13  
**Audited source:** `MATH_OBSTRUCTION_CATALAN_SCALE_LOW_EXPOSURE_PROTECTED_RAILS_NEED_NOT_EXTEND_20260813.md`  
**Audited SHA-256:** `baa5d99d2e30ace220aba57f069422456653da52f9dbf9abc5bf71e9adec99a1`  
**Verdict:** **PASS**, with the stated asymptotic and scope.

## Checks

1. With a distinguished coordinate \(\infty\), the four shore sizes are
   \[
   |\mathcal U_1|=|\mathcal L_0|=A={2r-2\choose r-1},\qquad
   |\mathcal U_0|=|\mathcal L_1|=B={2r-2\choose r-2},
   \]
   and \(A-B=A/r\).  The \((r,r-1)\)-biregular incidence graph from
   \(\mathcal U_0\) to \(\mathcal L_0\) has a matching saturating
   \(\mathcal U_0\), so the catalogue paths \(U-f(U)-(f(U)+\infty)\)
   are indeed mutually vertex-disjoint.  Their owner, lower, and union
   colours are all distinct.

2. In the complete catalogue every all-occurrence exposure row has load at
   most \(r\).  A lower facet in \(\mathcal L_0\) sees at most \(r-1\)
   zero-side owners plus its possible matched one-side owner; a facet in
   \(\mathcal L_1\) sees at most \(r\) one-side owners.  Injectivity of
   \(f\) gives the corresponding upper-owner bound for the central facets.

3. For a fixed row and colour, the load is a sum of independent weights in
   \(\{0,1,2\}\), has mean at most \(r/\lceil\sqrt r\rceil\le\sqrt r\),
   and Bernstein gives \(\exp(-\Omega(\sqrt r))\) probability of exceeding
   \(8\sqrt r\).  A path variable appears in at most \(2r\) lower-exposure
   rows and \(r\) upper-exposure rows; including the \(t\) colours, a bad
   event has dependency degree at most \(3r^2t\).  The symmetric local
   lemma therefore applies for all sufficiently large \(r\).

4. For the residual lower shore \(\mathcal A=\mathcal L_1\), its entire
   neighbourhood is \(\mathcal U_1\).  Exactly one endpoint of each chosen
   protected path lies there and consumes one of its two factor degrees,
   so the residual capacity is exactly \(2A-N\).  Since
   \[
   \frac{B/t}{2(A-B)}=\frac{r-1}{2t}>1
   \]
   eventually (and the floor is asymptotically harmless), this is strictly
   below \(2B\).  Thus the capacitated Hall cut really forbids every spanning
   two-factor containing the bank.

## Scope

The theorem refutes extension from bank size and exposure bounds alone.  It
does not refute the particular tensorized T2 rails, whose extra cut balance
or conformal trade geometry may still force extension.  Conversely, the
existing \(2^{o(r)}\)-bank theorem cannot be extrapolated to a
Catalan-scale bank from these numerical bounds.
