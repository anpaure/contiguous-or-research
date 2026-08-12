# Independent audit: functional partner codegree for the twisted `C6` pump

**Date:** 2026-08-02  
**Scope:** finite replay and proof audit of
`MATH_THEOREM_K_TWISTED_C6_FUNCTIONAL_PARTNER_CODEGREE_AND_COMPONENT_ESCAPE_20260802.md`.
No residual factor or ambient chronology is solved.

## 1. Independent replay

The script
`scratch/audit_k_twisted_c6_functional_partner_20260802.py` independently
constructs every Cartesian option through one target for `4<=r<=12` and
checks:

1. all six displayed transitions are Johnson edges;
2. old/new lower, upper, tail and head inventories agree exactly;
3. cyclically deranged role maps have full displayed marginal supply and
   zero mutual pair;
4. the corresponding old role atoms have separately distinct tails and
   heads and separately distinct lower and upper resources, so none of the
   four local matching rows exposes the obstruction;
5. identity role maps attain the maximum `r-2` mutual pairs;
6. after restricting to those mutual pairs, every non-target typed resource
   belongs to only one option, though it may occur once in each phase of
   that same option; and
7. arbitrary endpoint phase potentials give zero old/new signed charge.

The injectivity in item 6 also verifies Theorem 3.3: `t` mutual options
give `2t` vertex/facet-disjoint projected paths and hence exactly `4t`
incidence edges of maximum degree two.

Retained output:

```text
PASS functional C6 partner audit r_cases=9 derangement_min=2 max_mutual=r-2 charge=zero
```

## 2. Proof audit

The functional normal form is exact. For fixed `b`, all first-role options
leave the same owner `A_b`, so an oriented factor chooses at most one `c`.
For fixed `c`, all second-role options enter the same owner `D_c`, so it
chooses at most one `b`. Hence simultaneous options are the mutual
two-cycles of the two partial maps and form a matching.

The `4d` history bound is correctly conditional. Two variable-label tests
on the `b` shore and two on the `c` shore each expose a common set of at
most `d` labels. A matching loses at most one option per exposed label.
If collars vary with the option, the union can have linear size and the
bound is invalid; the theorem states this explicitly.

The component criterion is also exact: the three old components are the
pump component and the components containing the two partner edges. An
A-targeted fusion therefore needs exactly one partner on A's component and
the other on neither A nor the pump. Component-size bounds do not imply
this off-diagonal condition.

Finally, zero charge follows only after selecting one coherent physical
hex. Its old/new tail multisets and head multisets agree, so endpoint phase
potentials cancel. A quotient marginal lacking its phase/lift field is not
covered.

## 3. Verdict

**PASS within stated scope.** The theorem proves a sharp conditional
asymptotic result and identifies three independent missing rows:

* positive mutual functional codegree;
* a positive A-component escape fraction; and
* a common-envelope or otherwise bounded-load history bank.

It does not prove any of those rows for an arbitrary owner/`q1` factor.
The cited hex-free near-factor obstruction is used only to reject generic
near-perfect/high-girth reasoning; its even-band scope is not transferred
to the present odd host.
