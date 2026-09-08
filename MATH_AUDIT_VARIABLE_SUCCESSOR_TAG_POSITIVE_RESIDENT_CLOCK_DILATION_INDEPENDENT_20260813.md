# Independent audit: variable-successor-tag positive-resident clock dilation

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_VARIABLE_SUCCESSOR_TAG_POSITIVE_RESIDENT_CLOCK_DILATION_20260813.md`  
**Audited source SHA-256:**
`3b0c6541b3a8fb5ca8c899d0a7e33b9e6760482799d6b1a72bd462c593a307f3`  
**Verdict:** **PASS.**  The source now includes the load-bearing
fixed-alphabet qualification in Theorem 5.1.

## 1. Joint joins, palettes, and positive runs

For either state and every base edge `v -> w`, condition (1.3) gives

\[
 t^+(v)=t(w).
\]

The last lifted owner of `v` and the first lifted owner of `w` therefore
have the same tag and `D_0`, so their join is exactly the old base Johnson
edge.  This proves simultaneous closure; no additive voltage is needed.

The strict inequality `t(v) != t^+(v)` makes the midpoint a genuine tag
edge and distinguishes its two repeated `D_h` anchors.  Together with
the disjoint base/tag/clock profiles and the assumed simple base palettes,
the ticket profiles (3.1) prove owner, lower, and upper simplicity.

In either two-factor every vertex has exactly one predecessor.  If
`t(v)=a` and `u` is that predecessor, then `t^+(u)=a`.  The second
`h+1` owners of `Gamma(u)` and first `h+1` owners of `Gamma(v)` are
consecutive, giving a tag-`a` positive run of length `2h+2`; additional
same-tag blocks only merge runs.  Base and clock positive-run arguments
are also sound.  No zero-gap conclusion is used.

## 2. Conservative support signature

For a standard cyclic arc, the full sequence of pairs

\[
 ((t(v_1),t^+(v_1)),\ldots,(t(v_s),t^+(v_s)))
\]

together with the two endpoint offsets determines the literal tag and
clock union.  Equal base union, span, full tag word, and offsets therefore
give equal lifted value and physical width.  Theorem 4.1 is correct,
including its at-most-one-turn cyclic scope.

## 3. Fixed-alphabet quotient theorem

The relations (5.4)--(5.5) are exactly the forced tag equalities.  After
forming their quotient `Q`, condition (5.6) says that no required
tag-change edge becomes a loop.  This is necessary, and it is sufficient
when the tag alphabet may be enlarged freely: assign a private tag to
every quotient class.

For the fixed finite set `P` inherited from Section 1, the exact criterion
is

\[
 Q\text{ is loop-free and }\chi(G_Q)\le |P|,
\]

where `G_Q` has the quotient classes as vertices and one conflict edge

\[
 [v]_Q [s^-(v)]_Q
\]

for every owner occurrence `v`.  The final source states both versions
correctly: loop-free is equivalent to existence for **some** finite tag
alphabet, while the prescribed `p`-tag problem is equivalent to
`p`-colourability of this conflict graph.  The private-tag sufficient
bound `p>=|Q|` and the ambient coordinate-room warning are explicit.  The
necessity/sufficiency proof and equality of all matched full tag words are
exact.

## 4. Ambient rank gate for the rank-seven prefix actuator

For `rho=7` and ambient owner rank `R=m+1`,

\[
 |C|=m-h-7.
\]

A lifted base-edge upper value has the form

\[
 C\cup V^{(8)}\cup(\{p_a\}\cup D_0).
\]

Its tag-clock part has exactly `h+1` labels.  Hence it equals the named
target `T_0V` precisely when

\[
 C\mathbin{\dot\cup}\{p_a\}\mathbin{\dot\cup}D_0=U(V),
 \qquad |U(V)|=m-6.
\]

For a 13-coordinate prefix universe and a constant `p=|P|`, all unused
prefix, tag, and clock labels fit outside the target exactly under the
eventual inequality

\[
 m\ge h+p+5.
\]

This is only a local, one-target embedding.  Different suffixes `U(V)`
generally require different macroscopic cores `C_V`; simultaneous copies
therefore need a separate owner/palette-disjoint packing or common-core
theorem.  The local rank calculation does not supply such a tensoring
result.
