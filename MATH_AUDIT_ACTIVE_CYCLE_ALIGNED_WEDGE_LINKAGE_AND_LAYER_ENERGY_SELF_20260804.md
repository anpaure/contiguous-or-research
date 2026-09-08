# Self-audit: active cycle-aligned wedge linkage and layer energy

**Date:** 2026-08-04  
**Method:** symbolic proof replay only; no computation or search  
**Target:**
`MATH_THEOREM_ACTIVE_CYCLE_ALIGNED_WEDGE_LINKAGE_AND_LAYER_ENERGY_20260804.md`  
**Target SHA-256:**
`427fbd30f4208b81d56218e199fb050a7d1bda5463a7a1dba49a0b8ca242e01d`  
**Verdict:** **GO under the explicit selection-stable active-menu and
protected-factor premises.**

## 1. Sequential forbidden count

At stage `i`, each earlier owner star contributes at most one old owner
coordinate, so `|F_i|<=i-1`.  All current wedge edges incident with those
coordinates form a union of at most `i-1` vertex stars and have size at
most `B_(i-1)(m)`.

The terminal assignments introduced at any earlier source form a subset of
one Hamilton cycle.  Its intersection with the current terminal cloud has
size at most two, including the adjacent-source case.  Hence the complete
earlier assigned bank deletes at most `2(i-1)` current edges.  The strict
menu row leaves an active edge outside both forbidden sets.

Both endpoints of that edge are new relative to the entire earlier owner
star union, not merely relative to the previously selected wedges.  Its
terminal is absent from the complete earlier assignment bank.  Every menu
element carries a distinguished completion- and orientation-stable active
owner side; labelling that side as `a_i` before the cycle construction is
essential and is explicit.

## 2. Forcing the chosen edge into a Hamilton cycle

After deleting the earlier assigned terminal edges, the residual graph has

\[
 \delta(G_i)\ge m-2i+1.
\]

The range `i<=p<=floor((m+1)/4)` gives

\[
 m-2i+1\ge(m+1)/2.
\]

Ore's Hamilton-connected theorem therefore gives a Hamilton path between
the two endpoints of the chosen active edge.  Adding that edge closes the
path into a Hamilton cycle containing it.  Orienting the cycle from the
prelabelled active endpoint `a_i` to `b_i` makes this edge the outgoing
assignment at `a_i`.

Because `a_i` is a new owner, the bounded-turn assignment rule applies and
forces

\[
 \phi(L_i+a_i)=L_i+a_i+b_i=Z_i.
\]

The cycle avoids every earlier assigned terminal; outgoing edges within
one oriented cycle are distinct.  Thus the global full-port assignment
remains injective, and its stagewise assigned set remains cycle-supported
for the next overlap calculation.

## 3. Wedge packing and occurrence materialization

New endpoints at each stage give global distinctness of all selected owner
values.  Injectivity of `phi` gives distinctness of the selected `Z_i`.
The selected wedge bank therefore has lower degree two and upper degree one.
Degree compatibility with `P_*` plus the separate edge budget invokes the
small protected-factor theorem.

At a selected lower turn, its two protected incidences exhaust factor
degree two, so the factor q1 value is exactly `Z_i`.  The occurrence and
turn-diamond theorems produce the literal active branch.  Distinct owners
also make selected turns nonconsecutive, so the selected branches coexist.

The last conclusion uses the theorem's selection-stable premise: the
distinguished branch certificate is stable under the unprotected factor
completion and its orientation, and any nonendpoint collision or tail
conflict has already been removed from the menus or is private.  Endpoint
distinctness alone is not used to infer phase compatibility or
arbitrary-tail privacy.

## 4. Layer-energy threshold

The extra requirement that the active edge avoid the earlier assignment
bank costs at most `2(p-1)` beyond the exact wedge-conflict threshold.  Thus
the inactive allowance is

\[
 T_*={m-p+1\choose2}-2(p-1).
\]

The owner-heavy/terminal-heavy split with this `T_*` is identical to the
audited layer-energy argument.  For `p=O(sqrt(m))` and
`R=floor(m/2)+1`, the residual denominator remains at least `m^2/4`
eventually.  Therefore `I=O(m),J=O(m^2)` leaves only the displayed constant
number of exceptional sources.

After those sources are removed, the retained family has a no-larger
Hamilton-cycle/menu threshold.  The protected-factor edge budget must be
checked using the retained count, as the theorem states.

## 5. Scope

The theorem closes the quantifier correlation among an already active
wedge, its forced Hamilton-cycle linkage assignment, and its factor q1
occurrence.  It does not establish the activity menus, type/phase state,
linear owner area, hidden-hole pricing, product cap, or regeneration.

No mathematical correction was found.
