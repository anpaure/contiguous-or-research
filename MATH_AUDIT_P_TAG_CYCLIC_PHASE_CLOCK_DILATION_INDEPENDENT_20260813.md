# Independent audit: `p`-tag cyclic phase-clock dilation

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_P_TAG_CYCLIC_PHASE_CLOCK_DILATION_20260813.md`  
**Audited source SHA-256:**
`a5d9c224313ca87e726d34fbca0543dd0d0bbdf07fcf560ab155bf4b094d2fcc`  
**Verdict:** **PASS** for the stated local theorem and conservative support
criterion.  The finite `T_2` support test and host planting remain gates, as
the source says.

## 1. Block, rank, and closure

The displayed block has exactly

\[
 (h+1)+1+h=2h+2
\]

owner occurrences.  Its forward clock edges, tag edge, reverse clock
edges, and final base edge are all literal Johnson edges.  The last owner
of a tag-`a` block and the first owner of its successor both carry
`(p_{a+1},D_0)`; they have different base owners and are joined by exactly
the original base exchange.  Thus no endpoint is duplicated in the
chronology.  A component closes precisely because its base length is zero
modulo `p`, or, jointly, because the common tagging satisfies (1.3) in
both states.

The rank is `|C|+rho+1+h=R`.  Counting all disjoint coordinate pools gives
the equivalent ambient inequality in (2.4).

## 2. Simplicity and residence

The lower/upper profiles

\[
 (\rho,1,h-1)/(\rho,1,h+1),\quad
 (\rho,0,h)/(\rho,2,h),\quad
 (\rho-1,1,h)/(\rho+1,1,h)
\]

separate clock, tag, and base edges.  Within a type, the base occurrence,
literal tag, proper clock interval, or assumed simple base ticket separates
occurrences.  The repeated `D_h` owners have different tags; the repeated
`D_0` anchors have different tags or base owners.  Hence the three claimed
palettes are simple.

A base coordinate is held for a whole block.  Each clock coordinate has
an `h`-long positive arc and an `h`-long zero arc; the repeated antipodal
anchors cannot shorten either.  Tag `p_a` occupies the second half of the
tag-`a-1` block and the first half of the tag-`a` block, a positive run of
`2h+2`; its complementary zero gap has length
`(p-1)(2h+2)`.  The residence claim follows.

## 3. Cyclic interval projection

Work in the periodic universal cover, as the source explicitly does.  A
standard cyclic lifted interval projects to a consecutive based block arc
`I=(v_1,...,v_s)`; after one turn the first and last named occurrence may
coincide.  The literal value is

\[
 C\cup T(I)\cup K_{p,h}(t(v_1),s,a,b),
\]

where `a,b` are its two endpoint offsets.  The last term is determined by
the starting tag, block span, and offsets because every successive block
increments the tag by one and uses the same clock word.  A new arc with
the same conservative signature and the same offsets therefore has both
the same literal union and the same physical width.  This remains true for
the repeated-start-block representation of a one-turn cyclic interval.

Thus `Sigma_p^- subseteq Sigma_p^+` is a sufficient finite all-height
support certificate.  The source deliberately retains the starting tag
at every span; it makes no questionable claim that the tag alphabet is
automatically shielded at span `p` or `p+1`.

## 4. Exact scope

The theorem concerns standard cyclic intervals (at most one base turn),
which is the usual cyclic deck.  It neither certifies the finite `T_2`
signature inclusion nor proves simultaneous embedding in the ambient
factor.  Those limitations are stated correctly.
