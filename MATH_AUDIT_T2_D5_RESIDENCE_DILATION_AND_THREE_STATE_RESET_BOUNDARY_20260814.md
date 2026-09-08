# Independent hostile audit of the D5 residence dilation and three-state reset boundary

**Date:** 2026-08-14  
**Audited note:**
`MATH_THEOREM_T2_D5_RESIDENCE_DILATION_SUCCESSOR_TAG_NOGO_AND_THREE_STATE_RESET_GATE_20260814.md`  
**Audited note SHA-256:**
`f2ff0703e4946cff79b852750c732e2bd81d7c8f0132885f7bc57f5daaece246`  
**Verdict:** **PASS** for the static residence construction, defect
provenance, two-history and variable-successor-tag no-go, and exact
three-state reduction.  **No dynamic residence repair has been constructed.**

## 1. Scope controls

The audit separates four logically different assertions.

1. The frozen D5 toggle creates most of its final bad collars.
2. The already-fused output cycle can be recoded as a resident cycle.
3. Two natural ways to make that recoding common to both switch states are
   impossible.
4. A three-state certificate reduces the next construction to three reset
   interfaces.

Only item 2 is a construction.  Item 4 is conditional.  The aggregate audit
explicitly checks

```text
static_is_dynamic_switch_lift        false
three_state_reset_cell_constructed   false.
```

This prevents the principal possible overclaim.

## 2. Static clock algebra

For a base edge `T_i T_(i+1)`, the three expanded owners are

```text
T_i     + p_c     + q_c
T_(i+1) + p_c     + q_c
T_(i+1) + p_(1-c) + q_c,
```

followed by `T_(i+1)+p_(1-c)+q_(1-c)`.  The three edge supports are therefore
the base exchange, `{p0,p1}`, and `{q0,q1}`.  Consecutive supports are
disjoint.  Every immediate-upper transition spans two adjacent lower
supports, and adjacent such transitions use three pairwise disjoint support
pools.  The lower and upper q=2 claims follow without assuming that the base
output was resident.

The exact H100 replay checks the literal depth-two derivative, all 37,260
owners, Johnson adjacency, lower support separation, and immediate-upper
support separation.  It finds lower run minima `(3,3)` and upper minima
`(4,2)`.  The sharp upper zero witness is fresh coordinate 23, namely `p0`.
Thus the value two really is a clock-anchor effect.

The replay also finds repeated immediate-lower tickets.  The theorem records
this failure and does not promote the construction to a complete strict-lower
palette repair.

## 3. Provenance audit

The before/after event sets are compared literally, rather than estimating
collisions only near marked seams.  The resulting identities are

```text
upper: 84 old, 244 new-state, 36 retained, 208 new, 48 resolved
lower: 126 old, 240 new-state, 75 retained, 165 new, 51 resolved.
```

The category sums close:

```text
upper 36 + 203 + 5 = 244
lower 75 + 164 + 1 = 240.
```

External-role multiplicities are reconstructed from the exact factor maps,
not inferred from circuit lengths.

## 4. Two-history obstruction

The old component census contains only odd cycles, of lengths 23 and 115.
This alone excludes an alternating two-state tag on every old closure.

The additional XOR obstruction is local and stronger than the parity count:
two rows of `edge_index=3` share the same component and trade variables but
require opposite XOR values.  Hence even an open-arc phase assignment cannot
make that selected circuit use one common phase.

## 5. Alphabet-independent successor-tag obstruction

For fixed cycle orientations, successor-tag feasibility is the quotient
condition

```text
old head = new head in the tag quotient
tail != old head in the tag quotient.
```

Fourteen Boolean tag bits are not a restrictive alphabet because there are
only 12,420 owners and `2^14>12420`.  If the equality quotient were loopless,
one could give every quotient class a private 14-bit name.  UNSAT therefore
means that some required inequality becomes a loop for every orientation.

The hostile verifier does not trust the SAT conclusion.  It reads the two
extracted cores, tries all old-component orientations, contracts the selected
head equalities by union-find, and checks for a required loop.  It obtains:

| final direction | equations | old components | orientation masks | masks with a loop |
|---|---:|---:|---:|---:|
| forward | 86 | 4 | 16 | 16 |
| reverse | 96 | 5 | 32 | 32 |

It then deletes each equation in turn.  Every one of the 86 and 96 deletions
has a loop-free orientation, independently verifying inclusion minimality.

The no-go is model-specific.  It assumes one orientation per old cycle and a
block whose terminal tag is literally the successor tag.  It does not exclude
a multi-lane box carrying both possible successor ports in one fixed bank.

## 6. Three-state certificate

The independent replay rebuilds both suppressed factors and obtains 12,897
edges in their union.  It checks every edge against the stored 12,420-entry
three-colouring.  Since an old length-23 cycle is an odd-cycle lower bound,
the verified upper bound is sharp:

```text
chi(F- union F+) = 3.
```

It independently reconstructs all 477 tail/old-head/new-head triples.  Their
counts sum to 477; 265 have equal head states, while all 212 unequal cases use
all three states.  Therefore the reduction to three unoriented tail-keyed
reset types is exact.

This coloring alone is not a source lift.  To obtain one cycle it still needs
a switchbox whose pass and swap states use the same physical resource bank,
whose terminal collars are resident, and whose q2 currents are safe.  The
three external owners of role multiplicity four are an explicit coalescence
test, not disposable duplicates.

## 7. `K3` and thirteen-port challenges

The state graph `J(3,2)=K3` is not itself q=2 resident: consecutive triangle
edges have intersecting coordinate supports.  A proposed `K3 x Q_s` repair
must interpose payload moves and prove that every terminal routing traverses
the same bank.  Such a construction could settle the graph/owner residence
layer; it would still require the palette/current audit.

The thirteen-port native MSW theorem is inapplicable for two independent
reasons:

1. its finite hypothesis at `d=2` is `n>=39`, while this D5 instance has
   ground size 23; and
2. it applies to canonical highest-valley packet parents with same-start
   direct histories, not to the selected cross-suffix alternating circuits.

The theorem may become a host tool after a reset template exists, but it is
not that template.

## 8. Frozen replay

The aggregate H100 audit is

```text
scratch/audit_t2_suffix_d5_residence_reset_boundary_20260814.py
```

with source/output SHA-256

```text
3dc2598081ec097d1c64ea72c9ac96f26eb4d8d1e06ab93132fd9f155ae692a2
2252786824f0353a7b6056a004f04f95948b64c76724fde779a82d83d6fba2fb.
```

Its verdict is:

```text
new upper/lower collision events       208 / 165
static four-clock residence            PASS
two-history common phase               UNSAT
unrestricted variable successor tag    UNSAT
old/new union chromatic number          3
nontrivial selected resets              212
three-state reset cell constructed      false.
```

All compilers, SAT calls, enumerations, verifier replays, and hashes used in
this audit ran only on H100.
