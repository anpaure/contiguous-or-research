# Hostile audit: q4 k17 fixed-lower mixed-C4 projection and L3 lift kernel

**Date:** 2026-08-14

**Verdict:** **PASS** at the explicitly projected/lattice scope.

## 1. Audited source

```text
MATH_REDUCTION_Q4_K17_FIXED_LOWER_MIXED_C4_ACTION_AND_L3_LIFT_KERNEL_GATE_20260814.md
sha256 ea51ae8818702eb704080cbbceead147d00a8f619fc5e04f1cbd4e795a989755
```

## 2. Algebra checks

A mixed unit `C4` changes the rank-eight lower ledger by `e_A-e_B` for
adjacent `A,B`.  Modulo two on fixed reflection bracelets, the three cases
are exactly a fixed-fixed edge, a singleton when exactly one endpoint is
fixed, and zero when neither is fixed.  Literal reflection pairing doubles
every fixed endpoint and therefore has zero fixed action.  These statements
do not use occurrence in a chosen factor.

For cut edges `a--b,c--d`, the four old length-two paths through the cuts
and the four new paths after reconnecting `a--d,c--b` give precisely the
eight signed rank-seven terms in source formula `(3.2)`.  The four flanking
owners are necessary data.  Hence the matrix `C_7` and kernel `Lambda_F`
are correctly factor-dependent; the source does not infer L3 preservation
from the abstract lower-current graph.

For non-literal lift pairs, `E(u)=E(v)` is the right orientation condition.
Then `u+reflection(v)` covers `E` and `reflection(E)` once each.  Relative
to `u+reflection(u)`, its ticket changes are exactly the reflected
differences in `(4.3)`.  Equality of only the ten reduced rows would not be
enough, and the source explicitly retains this boundary.

## 3. Finite graph and minimum audit

The H100 verifier independently builds all 1,430 rank-eight translation
orbits.  It finds 70 fixed bracelets and reconstructs every quotient
Johnson neighbor.  Removing eight zero-current quotient loops leaves 32
fixed-fixed edges with components

```text
                            C16 + C16 + 38 K1.
```

Their binary incidence rank is `15+15=30`.  Every fixed vertex has between
52 and 72 nonfixed neighbors, so singleton fixed projections exist at all
70 vertices and the unrestricted projected rank is 70.

The frozen all-eight quotient-self lower catalogue covers sixteen fixed
vertices.  Direct replay gives 30 deficient isolates and twelve deficient
vertices on each 16-cycle.  The verifier exhausts all `2^16` fixed-edge
subsets per cycle, charging one additional move for each residual singleton.
Both minima are eight, so the projected lower bound and projection-only
witness cost are exactly `30+8+8=46`.

This does not claim that the singleton moves' nonfixed currents cancel, or
that 46 occurrence-compatible switches can be packed.  The source labels
46 as a projection minimum throughout.

## 4. Replay

```text
scratch/verify_q4_k17_fixed_lower_mixed_c4_projection_and_lift_kernel_20260814.py
sha256 d94555683993c0bae82210a6494ca63162c5445d7afd5f21389226ff4fa56d2a

scratch/verify_q4_k17_fixed_lower_mixed_c4_projection_and_lift_kernel_20260814.h100.out
sha256 ec428eb3e86c084711dfa4a3638a171899e6e83e9dc0a34746fd8478333a0d07
status PASS
```

The final H100 replay was byte-identical to the frozen output.  No owner
cover, switch packing, or lower/L3 feasibility claim is made.
