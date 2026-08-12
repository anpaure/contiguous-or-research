# Audit of the one-prefix prism boundary defect

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_MNW_ONE_PREFIX_PRISM_EXACT_BOUNDARY_DEFECT_20260807.md`  
**Verdict:** PASS.

## 1. Prefix separation

Every mirror-gamma cycle vertex is `1 revcomp(y) 1`; every
`alpha(1100)` cycle vertex starts with `1 1100`.  Hence neither tuple
touches a first-bit-zero incidence.  The natural `01` boundary is retained.

**Result:** PASS.

## 2. Destination-owner ledger

At `O_3=1011001001`, direct mirror images of the old other neighbour and
new gamma neighbour are `1011011001=10E` and `1011001101=10Q^-`.

At `O_1=1010001101`, the retained mate is `1010101101=10E`; gamma removes
`1011001101=10Q^+` and installs `1110001101`.  The required
`1010001111=10Q^-` is absent.

**Result:** PASS.

## 3. Leaf-root check

`O_1` belongs to the wrapped path root `1111010000`.  Its old root
`11101000` is gamma-only in the standard `F_4` star.  The new
`alpha(1100)` connector meets the wrapped block at `1110011000`; all later
connector prefix forms differ.  Thus no selected recursive tuple supplies a
second mark on the relevant root.

**Result:** PASS.

## 4. Spare providers

The second inverse providers for complement targets `45` and `28` are
centred at `11100001` and `00111010`.  Their positive-context copies differ
from all six lower centres changed by the two first-stage tuples.

This proves noninteraction with the relay pair only; the theorem correctly
retains a global avoidance condition for other recursive tuples.

**Result:** PASS within scope.

**Overall verdict:** PASS.  The unmodified recursive relay tree fails the
prepared-prism phase at the explicit leaf incidence (5.2).
