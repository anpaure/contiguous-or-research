# Final audit of the \(Q_4\) four-shore composition theorem

Date: 2026-07-26

Audited report:
MATH_ATTACK_K_Q4_FOUR_SHORE_COMPOSITION_AND_TRACE_BOUNDARY_20260726.md.

Method: independent pure-mathematical verification.  No finite search,
solver, computation, or web input is used.

## Verdict

**PASS.**  No substantive correction remains.

The following claims and their stated scopes were checked independently.

1. The four maps \(G_I,G_A,G_B,G_{AB}\) are exact two-\(C_8\) factors,
   \(AB=(1\,3)(2\,4)\) is fixed-point-free on direction labels, the
   common phase is exactly \(\mathbb Z_4\), and no common rooted
   \(\mathbb Z_8\) refinement exists.
2. For an interlaced proper quartet, exactly \(12/16\) row-label charts
   are owner-Latin, but a same-owner \(AB\)-partner exists only for the
   four plane-constant charts.
3. For a nested proper quartet, exactly \(12/16\) charts are owner-Latin
   and every legal chart has the unique partner
   \[
     U'=1+U,\qquad V'(x)=1+V(x+1).
   \]
   The incoming and outgoing same-owner identities both hold.
4. The interlaced plane-constant double atlas has
   \(2^{2^h/32}\) ordered first-factor states.  The nested growing atlas
   has \(12^{2^h/64}\) ordered first-factor states.  Its relative shore
   moves exactly the even directions and fixes exactly the odd directions.
5. The independent one-bit multilayer has exactly \(2^h/16\) component
   bits and changed-tail density \(1/2\).
6. Every proper disjoint quartet slab contains a separator, so
   \(5t\le h\).  Hence at least \(h/5\) directions remain fixed, and at
   least \(1/9\) of cyclic \(d\)-windows contain at least \(d/10\) fixed
   directions.
7. Complementing two noncommuting layer bits cannot give one fixed shore.
   The separate adjacent-chain braid remains exact with
   \(N(1-2^{-r})\) bits, normalized as rate \(1-o(1)\) per syndrome
   cycle, not per cube owner.
8. The fixed-suffix construction obeys
   \[
      B\le LN\,2^{-\dim D_R},\qquad
      \dim D_R\ge\operatorname{rank}(R-I).
   \]
   For a full perfect-matching shore, the stronger obstruction
   \(\mathbf1\in D_R\) prevents a common rooted phase complement.
9. The syndrome-kernel collision is stated only for a globally constant
   shore.  The fixed-wire trace ratio \(2h/2^d\) is stated only for one
   fixed base cyclic order and the aligned affine trace; \(L_0\) unrelated
   base orders multiply the numerator by \(L_0\).  Transfer through the
   arbitrary-\(k\) carrier is correctly conditional on a complete or
   equidense frozen-fibre decomposition with no extra trace-visible datum.
10. The same \(Q_4\) phase colouring cannot support a transverse second
    perfect-matching twist bank; the third matching is covered by
    conjugacy.

## Exact implication boundary

The seed composes literally at linear syndrome-cycle information rate and
admits a positive nested local-\(AB\) double atlas.  It does not
automatically plug into the arbitrary-\(k\) \(Q_2\) carrier, because the
bare cube lacks a common rooted \(\mathbb Z_8\) phase and the required
antipodal pair-clustered fibre has not been constructed.

The local fixed-direction trace argument is removed at the \(AB\) corner.
It is not removed globally by any proved growing atlas.  The remaining
open primitive is an overlapping phase-local partner identity which
changes wire frames while retaining one same-owner opposite and a
completed antipodal carrier interface.
