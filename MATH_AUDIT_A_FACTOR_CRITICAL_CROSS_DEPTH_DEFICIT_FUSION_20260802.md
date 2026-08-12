# Audit of factor-critical cross-depth deficit fusion

**Date:** 2026-08-02  
**Verdict:** PASS for the declared protected module/bridge atlas.  Boolean
module and bridge supply remains a hypothesis.

## Audited artifacts

- `MATH_THEOREM_A_FACTOR_CRITICAL_HINGE_PATH_COVER_AND_CROSS_DEPTH_DEFICIT_FUSION_20260802.md`,
  SHA `36bbb6778288f499e096fd67a2f2827c78140e7570b15fff254ac377a27b24fd`;
- `scratch/audit_a_factor_critical_hinge_path_cover_20260802.py`,
  SHA `798b9b8c077d49dfe75210b6744ed6c66e6166f6975dfe93cdc1ce994d24a957`.

## Exact conclusions

A factor-critical module path omits one root role and one outgoing socket.
A jointly occurrence-compatible bridge consumes the source socket and the
next module's omitted role.  Therefore a spanning path forest on `p` modules
with `c` paths telescopes the `p` local deficit pairs to exactly `c` exposed
root--socket pairs.  A Hamilton path leaves one pair; a Hamilton cycle leaves
none.  This is a bound on live deficit, not on selected support or physical
letter cost: at least `p-c` bridges are necessary.

Under port-complete internal relations and a universally
matching-compatible bridge atlas, balanced one-copy completion is exactly
Hall on the quotient digraph.  After reserving a spanning `c`-path forest,
the exact residual balance bank consists of `2^c` Hall rows.  Connectedness
is separate: a residual perfect matching must induce one cycle.  For fixed
`c`, at most `c!` residual matchings decide this topology row.  If the
reserved physical witnesses themselves are frozen, the stated hereditary
extension property is additionally required.

The weighted indegree row and the `rho+kappa<|Q|/2` row are valid sufficient
conditions.  The latter implies Hall and then permits quotient two-switch
fusion with a fresh simultaneous physical realization after each switch;
it does not assert that unaffected literal occurrences remain fixed.

The four-role predecessor obstruction has the factor-critical path

```text
1 -> 3 -> 0 -> 2.
```

Thus compatible bridges `2_t -> 1_(t+1)` cancel arbitrarily many abstract
copies in one cycle.  This does not contradict the fixed-table
deficit-additivity theorem, because the bridges enlarge the old closed
menus.

## Scope boundaries

Without port completeness or universal matching compatibility, failures of
the projected quotient hypotheses are not impossibility certificates.  One
must solve the full joint occurrence-labelled relation.  A locked
two-switch shore obstructs only that switch basis.  The theorem supplies no
Boolean/Pascal bridge atlas, no arbitrary-width upper bank, and no common
source/cap or compiler.

## Replay

The lightweight verifier returns

```text
PASS
cyclic_couplings=8
residual_digraphs=530
two_switch_covers=74903
```

It checks the boundary/resource ledger, cyclic contraction of the four-role
module, all residual Hall systems through three quotient modules, both
minimal projection obstructions, and the graph-level two-switch implication
through five modules.
