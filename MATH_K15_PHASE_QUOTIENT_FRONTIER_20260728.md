# k=15 phase-quotient frontier (2026-07-28)

## Carrier block

The phase search rewires physical cycles 1 and 12 of
`scratch/k15_dual_descent_a4_step19.segments.json`.  Their union has 5,295
rank-8 vertices, 353 free `Z_15` vertex orbits, and 353 free lower-colour
orbits.  The full induced exact-lower catalogue contains 7,609 edge orbits.

The other fifteen physical cycles are held fixed.  Consequently a selected
quotient factor must cover only the upper targets not already supplied by
those cycles.

## Exact positive results

1. Exact lower plus every critical upper-q1 target is feasible.
2. Exact lower plus every critical upper-q1 and upper-q2 target is feasible.
   The compressed model has 276,048 variables and 845,714 clauses and solved
   in 139.15 seconds.  Its full-carrier audit is
   `scratch/k15_phasequotient_upperq2_orbit.audit.json`:

   - upper holes q1 = 0;
   - upper holes q2 = 0;
   - upper holes q3 = 15 (one rotation orbit);
   - upper holes q >= 4 = 0.

   This proves that the invariant edge-orbit catalogue has enough
   multidepth capacity; the q1-only success was not a false positive.

3. Residence is independently feasible far beyond the two explicit
   rectangles.  The eager depth-one model remains SAT after more than 900
   lazy depth-two/three cuts.  The eager depth-two model also produced a SAT
   first round and is continuing with depth-three cuts.

The unresolved finite problem is the intersection:

```text
exact old lower palette
+ upper q1/q2/q3 coverage
+ depth-three residence
```

Connectivity is intentionally absent.  The depth-three compiler has 1,119
units of scalar slack, so a moderate number of components can be opened and
handled by a separate safe-cut selection.

## Exact local no-go

The two explicit rectangle templates cut the C1 edge orbits based at indices
444 and 5049.  There are three further phase-complete missing-colour witness
orbits based at 580, 1480, and 4698.  The script
`scratch/search_k15_double_template_braid.py` audits arbitrary subsets of
these five C1 cut orbits together with the P12 foreign cut orbit.

For every one of the 31 nonempty subsets, the following system has no
nontrivial solution:

- use only resident Johnson seams between the exposed endpoints;
- restore every removed lower colour exactly once;
- cover every upper-q1 target lost by the cuts.

Equivalently, after requiring even one non-original seam, SAT returns UNSAT.
Without that requirement, the only feasible selection restores the native C1
and P12 components.  Adding upper q2/q3 does not change the verdict.

Thus no mixture of the five known phase rectangles, and no higher-order
endpoint matching on their exposed ports, can solve k=15.  A successful
factor must alter internal C1/P12 chronology, exactly as the 7,609-orbit
quotient model permits.

## Required next verification

Once the combined model is SAT:

1. audit cyclic residence and all upper depths on the full 6,435-vertex
   carrier;
2. choose one safe opening per component without creating upper q1/q2/q3
   holes;
3. run the exact depth-three lower Hall/compiler;
4. materialize and independently verify the length-6,438 OR word.

