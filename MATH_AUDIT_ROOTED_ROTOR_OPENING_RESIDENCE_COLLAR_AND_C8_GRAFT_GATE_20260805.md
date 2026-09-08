# Audit of rooted rotor opening and residence collars

**Date:** 2026-08-05  
**Method:** independent run-fragment, geodesic, and scope replay; no
computation or search  
**Audited theorem:**
`MATH_THEOREM_ROOTED_ROTOR_OPENING_RESIDENCE_COLLAR_AND_C8_GRAFT_GATE_20260805.md`

## 0. Verdict

**PASS at stated scope.**  A rotor cut necessarily exposes length-one
positive and zero fragments, so no constant-width universally safe opening
exists at growing depth.  A `d`-owner safe-coordinate geodesic collar is
both necessary and sufficient for the rotor-clipped fragments.  It exports,
rather than silently solves, one nested external state interface.

## 1. Fragment replay

At the cut `T_(2m-2)|T_0`, coordinate `z_a`, `0<=a<=m-2`, has positive
endpoint fragments `a+1` and `m-1-a`.  The absent coordinates have the
complementary zero fragments.  This gives exactly the four vulnerable banks
in (1.4)--(1.5).  Coordinate `z_0` forces `d` preceding present states, so
the collar-length lower bound is literal.

## 2. Collar replay

Condition `m>=2d+1` gives at least `d` safe coordinates both inside and
outside the endpoint owner after the vulnerable banks are removed.  The
displayed collar is a monotone geodesic replacing one safe outside
coordinate by one safe inside coordinate at every step.  Its owners and
both q1 palettes are simple.

All left vulnerable-present coordinates remain present and all
vulnerable-absent coordinates remain absent through `d` positions.  The
right calculation is the reversal.  New collar transitions produce only
the explicitly listed nested `(u_i,v_i)` boundary state; the theorem does
not claim that an arbitrary PBBS body realizes it.

## 3. Factor and C8 scope

A fixed number of geodesic shield/collar segments has `O(m)` protected
size and constant star/facet exposure, so the fixed-exposure protected-Ore
proof applies prospectively.  It is unrooted: it does not select named PBBS
endpoints or one source chronology.

Once rooted body-state realization is supplied, the full-union theorem,
residence collars, and adaptive `C8` phase theorem compose exactly as
stated.  The localized upper backup and typed common-cap/lower-compiler rows
remain explicit hypotheses.

