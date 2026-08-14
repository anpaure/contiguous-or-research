# Hostile audit: q=3 character-minimal centre-support hole

**Date:** 2026-08-14  
**Source:**
`MATH_OBSTRUCTION_Q3_CHARACTER_MINIMAL_THREE_BY_THREE_NEAR_C_ATOM_HAS_A_CENTRE_SUPPORT_HOLE_20260814.md`  
**Verdict:** PASS after scope and replay corrections

## 1. Three-by-three equality classification

At net mass three, equality in the global supporting-plane bound forces
zero slack coordinate by coordinate.  For `q=3`, target equality gives
`a\in\{-1,2\}` and `b\ge0`; exterior equality gives `a=0,b\ge0`.
The global sums `\sum a=-1`, `\sum b=1` therefore force exactly one target
with `a=2`, three targets with `a=-1`, and exactly one positive long
centre, possibly exterior.  This argument classifies net ledgers and does
not assume that rails in one aggregate centre/period class share an order.

The two positive period-eight rails centred at the distinguished target
give degree at least `16` there.  Each of the three negative rails is
centred elsewhere and contributes at most `q=3`, so the negative degree is
at most `9`, whereas a one-owner difference requires gap one.  This proves
the three-by-three support hole independently of cyclic order and
simplicity.

## 2. Four physical rails with net mass three

One subtle case in the draft needed explicit separation: four physical
rails per shore can have net centre mass three because one aggregate
centre/period unit cancels.  The net equality classification above still
applies, because it depends on net \(\ell^1\) mass six.  The exact point
equation at the distinguished target then needs `t=-5` or `t=-8`, while
four physical rails imply the necessary bound `|t|<=4`.  Thus the
net-mass-three branch is impossible even with one physical aggregate
cancellation.  The patched verifier now checks this branch separately.

## 3. Proposition 4.1 local-cost audit

For shore four the exact local equation is

\[
 8a+9b+3t=h,\qquad |t|\le4.
\]

At a target, `a\equiv-1\pmod3`.  Minimizing `|a|+|b|` gives costs `7,1,3` for
`a=-4,-1,2`; all more distant target values cost at least eight.  At an
exterior coordinate, nonzero `a` is a multiple of three and costs at least
five.  Since the four targets already cost at least four and the total
cost is eight, the only possible `a` profile is `(2,-1,-1,-1)` on the
targets and zero outside.  The remaining `b` mass is three in \(\ell^1\),
with sum one.  The local equation forces `b=-1` at the `a=2` target and
nonnegative `b` elsewhere, of total two.  This is exactly Proposition 4.1.

## 4. Verifier scope

The replay enumerates all local integer triples `(a,b,t)` satisfying the
exact equation and `|t|<=shore`, then takes their Cartesian product.  This
is a relaxation: independent `t_z` values need not come from common toggle
words.  Therefore absence in the enumeration is a valid obstruction and
classification of every relaxed survivor is a valid necessary normal
form; presence would not prove realizability.  Eight exterior slots are
sufficient because a nonzero exterior state costs at least one and the net
\(\ell^1\) mass is at most eight.

## 5. Ten-label four-by-four obstruction

Proposition 4.1 gives `(a,b)=(2,-1)` at `z_0`, so the exact point equation
forces `t_{z_0}=-2`.  On a reduced ground of size ten, every period-nine
rail toggles every label other than its centre.  The two positive long
centres are away from `z_0`, contributing `+2`; the three negative short
rails contribute at least `-3`; and the negative long rail is itself
centred at `z_0` and contributes zero to `t_{z_0}`.  Therefore
`t_{z_0}>=-1`, a contradiction.  This is symbolic, covers all four
placements of the two positive long centres, and subsumes the independent
ten-label CP-SAT infeasibility results.

The H100 replay returns

```text
PASS shore=3 net_mass=3 feasible_relaxed_states=0
PASS shore=4 net_mass=3 feasible_relaxed_states=0
PASS shore=4 net_mass=4 relaxed_states=40 centre_distribution_types=4
```

No cyclic-window realization at four rails is claimed.  With that
one-way scope explicit, PASS.

## 6. Frozen provenance

Source SHA-256: `54d2477fb1b7d90a8ffbaafb05dd603f3c6a6e3c9ebe3edb51b1f3b23a0f243b`  
Verifier: `scratch/verify_q3_near_c_centre_support_hole_20260814.py`  
Verifier SHA-256:
`a8ce9583f1f00ede02f3237db6f808a4e38c977d9b5039849adf9b8e0dcb6a8b`  
H100 output SHA-256:
`11a2d34661a0e028ff8061f7bdf61b1f5a776e498025a3d1c9ddd2fa63f03069`  
Supporting ten-label solver:
`scratch/search_q3_near_c_four_by_four_atom_20260814.py`  
Solver SHA-256:
`9afedd3571f67bc97249b5c3c806c1bee0a35fafe967ac61e7f8ae7a3ed2943c`  
Audit SHA-256 before provenance insertion:
`91dd123eeb36f8b06dc459e379dcb872718bf1c25b8f3ffdb4b2a10c569b07ed`.
