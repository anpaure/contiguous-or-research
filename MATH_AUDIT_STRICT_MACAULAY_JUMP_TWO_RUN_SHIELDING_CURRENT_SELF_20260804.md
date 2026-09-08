# Self-audit: strict Macaulay jump two-run shielding

**Date:** 2026-08-04  
**Verdict:** **SELF-GO.**  The gated owner table, scalar inclusion--exclusion,
four-current protected identity, and Macaulay root transition have been
rederived below.  The theorem is a reduction of strict-jump gluing, not a
uniform safety proof.

No computation, search, or solver result is used.

## 1. Audited artifact

`MATH_THEOREM_STRICT_MACAULAY_JUMP_TWO_RUN_SHIELDING_CURRENT_20260804.md`

SHA-256:
`8dd7fe2074032e5376a5be55b7769437f90e6bc7b95ffd7482024bef1101ed6b`.

This is an author self-audit, not an independent audit.

## 2. Active-core table

Upper clauses are `R+y`, and lower clauses are `R union G+x`.  With only
one active upper hit their intersection is `R+y`; with multiple hits it is
`R`.  The analogous lower intersections are `R union G+x` and
`R union G`.  If both groups fire, the upper cores omit `G union X` while
the lower cores omit `Y`, so their total intersection is exactly `R`.
Accepted facets delete outside this intersection, proving the fibre table.
The largest core has size at most `m-2`, so every active fibre is at least
two.

## 3. Scalar count

At either rank `q`, the upper family is counted by `Phi_q(R;Y)` and the
lower family by `Phi_q(R union G;X)`.  Their intersection requires the
larger base and a hit in both `X` and `Y`, giving the four-term count
`Phi_q^(2)`.  Since all nonzero owner fibres are two-covered,

\[
 \sigma/2=|N|-|A|,
\]

and rankwise inclusion--exclusion proves (2.5).

## 4. Protected current

At every active owner, root deletions are unselected.  A unique upper hit
adds that `Y` coordinate only when the lower gate is absent.  The extra
root `G` is unselected only when the lower gate acts alone, and a unique
lower hit then adds the corresponding `X` coordinate.  When both gates
fire, the active-core intersection is `R`, so every other deletion is
shielded.  This proves the exact four-current identity.

On a resident path, positions containing a fixed base form one interval,
and each hit coordinate also has one occurrence interval.  Each has at
most two boundary incidences, giving (3.2)--(3.4).  Restricting to an
upper-only or lower-only state can only delete contributions.

## 5. Macaulay jump geometry

For consecutive runs, the lower final pivot is `rho_-+b`; the upper first
pivot is `rho_++b+1`.  Comparing their root complements leaves exactly

\[
 G=[\rho_-+b+1,\rho_++b]
\]

in the lower root but not the upper root.  Its size is
`rho_+-rho_-`.  Lower pivots end before `G`, upper pivots start after it,
and both are disjoint from the common upper root.  Therefore the union of
the two run DNFs is exactly the gated family of Section 0.

## 6. Scope

The theorem proves complete shielding of the aperture-jump coordinates
whenever the upper gate fires.  It does not prove that the scalar slack
pays the four residual currents in every case, and it does not compose
three or more gates.

**SELF-GO** at theorem SHA
`8dd7fe2074032e5376a5be55b7769437f90e6bc7b95ffd7482024bef1101ed6b`.
