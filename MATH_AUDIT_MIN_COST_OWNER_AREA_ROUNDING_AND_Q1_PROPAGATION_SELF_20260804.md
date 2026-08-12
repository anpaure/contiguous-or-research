# Self-audit: min-cost owner-area rounding and q1 propagation

**Date:** 2026-08-04  
**Method:** exact flow and incidence replay; no computation or search  
**Target:**
`MATH_THEOREM_MIN_COST_OWNER_AREA_ROUNDING_AND_Q1_PROPAGATION_20260804.md`  
**Target SHA-256:**
`2659c8e6080b4d4fbc123e312e047e7ca3ad08aa7feed9444855f7bc94d21b24`  
**Verdict:** **GO under the stated one-network fractional-current
premise.**

## 1. Integrality and cost

Node splitting turns every physical vertex capacity into an integral arc
capacity.  Adding `q` unit source arcs and unit sink arcs gives an ordinary
single-commodity min-cost max-flow instance with integral capacities and
demands.  Its feasible polytope is integral.

The supplied fractional value-`q` flow proves that the min-cost optimum is
at most `L`.  An integral optimum has integer cost, hence cost at most
`floor(L)`.  Removing nonnegative-cost flow cycles preserves value and does
not increase cost.  Because all internal node capacities and all terminal
arcs are one, the resulting path decomposition consists of `q` mutually
vertex-disjoint paths to distinct sinks and saturates all `q` claim starts.

Every used owner occurrence crosses its cost-one split arc exactly once.
Thus integral cost equals the number of used owner occurrences.  Boolean
value projection can only coalesce occurrences, so the distinct-value count
is no larger.

## 2. Terminal projection

Every nonexceptional used rank-`m+1` terminal value contains a used
rank-`m` owner value along a selected Boolean containment edge.  One owner
value has exactly `m-1` such supersets in a `2m-1` element ground set.
The union bound therefore gives

\[
 |D_Z|\le(m-1)|D_U|+e
 \le(m-1)\lfloor L\rfloor+e.
\]

No path order, pathwise length, or monotonicity is used.  Terminal nodes on
remote/non-Boolean portions of the network are correctly charged to the
exception bank.

## 3. Regular-factor fractional current

Sending `1/h` along each of the `hq` complete incidence paths is feasible
only under the explicitly imported privacy/congestion hypotheses.  Its
owner cost is linear in arc load:

\[
 {1\over h}\sum_{gp}\ell_{gp}.
\]

Shared owner arcs do not invalidate this identity; their loads add, and
feasibility already enforces capacity at most one.  If the average owner
count is at most `ell`, the displayed sum is at most `q ell`.

The min-cost theorem may choose a different integral linkage from the
displayed paths.  This is allowed and is exactly why only aggregate
fractional owner current, rather than a pathwise bound, is required.

## 4. Regenerative use and guardrails

An integral background with owner area `O(m)` and terminal-only/hidden
exceptions `O(m^2)` satisfies the audited active-wedge layer-energy rows.
The active cycle-aligned theorem then correlates surviving activity,
Boolean linkage and factor q1 occurrence.

The following are not inferred:

1. existence of the fractional current in the current Pascal child;
2. compatibility of separately constructed coordinate flows;
3. terminal typing or phase compatibility not encoded in the network;
4. a quadratic bound on terminal-only exceptions; or
5. nonaccumulating regeneration.

All shared physical capacities must be present in the one node-split
network before applying min-cost integrality.  Averaging currents from
different cap states would be invalid and is explicitly excluded.

## 5. Conclusion

The theorem is mathematically sound.  It removes the integral owner-area
rounding obstruction: any one-state fractional compensation current with
aggregate owner load `O(m)` has an integral private realization with
linear owner footprint and, modulo priced exceptions, quadratic q1
footprint.  Fractional existence and regeneration remain the exact open
rows.
