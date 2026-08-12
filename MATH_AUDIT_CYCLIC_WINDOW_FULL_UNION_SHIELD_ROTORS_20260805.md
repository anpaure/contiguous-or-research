# Audit of cyclic-window full-union shield rotors

**Date:** 2026-08-05  
**Method:** independent cyclic-window, pin-dilation, and protected-Ore replay;
no computation or search  
**Audited theorem:**
`MATH_THEOREM_CYCLIC_WINDOW_FULL_UNION_SHIELD_ROTORS_20260805.md`

## 0. Verdict

**PASS at stated scope.**  The rotor simultaneously supplies sharp
full-union owner shields, both residence polarities, q1 simplicity, and a
nonempty depth-`d` cyclic source antecedent.  Fixed many disjoint rotor
cycles extend to a spanning two-factor.  Their saturation prevents this
unrooted theorem from attaching them to PBBS bodies.

## 1. Cyclic owner replay

Consecutive length-`m` cyclic windows on `2m-1` coordinates differ by one
exchange.  Their intersections and unions are respectively cyclic windows
of lengths `m-1` and `m+1`; all three lengths are strictly between zero and
`2m-1`, so all three palettes are simple.

The union of `m` successive owner windows spans coordinates from `i` through
`i+2m-2`, exactly the ground set.  One coordinate lies in `m` consecutive
owners and is absent from the other `m-1`.  Thus the positive and zero
residence floors are both at least `d+1` precisely throughout the stated
range `d<=m-2`.

## 2. Source-pin replay

For one desired owner run `[s,e]` of length `m`, pins beginning at `s+d`
and separated by `d+1` give adjacent dilation intervals `[p-d,p]`.  The
terminal pin `e` overlaps the last interval and closes the run exactly.
Thus the coordinatewise depth-`d` dilation equals the rotor trace.

At source position `p`, the coordinate indexed
`a=p+m-1-d` has first pin `s_a+d=p`.  Every source letter is therefore
nonempty.  No claim about an external linear endpoint state is implicit.

## 3. Factor replay

Fixed-bank orbit avoidance is valid because every rotor uses only `O(m)`
vertices from exponential rank layers.  A fixed lower facet lies below at
most two rotor owners, and a fixed owner contains at most two rotor facets;
the bank loads are at most `2q`.

The protected bank has `O_q(m)` edges, so near-shadow localization gives an
`O_q(m^2)` small/co-small cutoff.  The fixed forced-facet load excludes the
co-small optional core.  On the small side there are no path endpoints and
the local owner ledger gives `lambda_P(A)<=sum_(x in A)lambda_P({x})`, hence
`lambda_P(A)<=2q|A|`; Kruskal--Katona supplies linear-in-`m` slack.  This
verifies the rotor-cycle adaptation of the fixed-shield factor theorem.

Every rotor vertex is already protected to degree two.  Hence a containing
two-factor cannot use an external edge at any rotor vertex, and each rotor
remains a separate component.  The rooted opening/graft scope is correctly
left open.
