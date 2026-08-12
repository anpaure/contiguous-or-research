# Independent audit: odd-host private gain-one hex absorber

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_PCS_ROW2_PRIVATE_GAINONE_HEX_AND_TRANSPARENT_PULL_TREE_20260802.md`  
**Verdict:** PASS for the literal packet identity, fixed-slot canonical
catalogue count,
non-target resource load, and deterministic private-packing inequality;
the theorem's prospective/off-phase and graphic/pull-tree qualifications
are necessary

## 1. Independent algebraic replay

Set `r=m-1`, take a rank-`r` target lower colour `D`, and write its target
upper colour as `V=D+p+q`.  For

```text
b in D,
c outside V,
(a,s)=(p,q) or (q,p),
K=D-b,
```

the audit independently regenerated the six resources in each phase.  It
checked the containments

```text
D_a subset U_acs, U_abs
D_b subset U_abs, U_bcs
D_c subset U_bcs, U_acs
```

and compared the resource multisets.  The on state equals the off state
plus exactly

```text
target lower D,
target upper V,
target owner slots D+p and D+q.
```

No auxiliary lower, upper, or slot resource changes multiplicity.  Hence
the packet preserves all already present lower/upper occurrences and owner
degrees when, and only when, its two off atoms were planted and its two
target owner slots were left free.  It is not a post-hoc `3<->3` move on a
saturated factor.

The audit also checked the endpoint interpretation.  The bookkeeping target
edge `e_b` is absent from the on phase.  Its upper resource is realized by
`f_a`, while its lower and two slot resources are distributed across the
three on atoms.  Thus the identity proves full-upper occurrence supply, but
does not by itself prove that the old named target tail/head survives after
fixing `M_0`.

## 2. Canonical catalogue and load calculation

The odd ground has size `2m-1=2r+1`.  Therefore

```text
#b = r,
#c = (2r+1)-(r+2)=r-1,
#orientations = 2,
```

and, after fixing the canonical auxiliary slot section used in the source
theorem, the catalogue size is exactly

\[
                         2r(r-1)=2(m-1)(m-2).
\]

The independent parameter-recovery calculation gives the following maximum
loads for a fixed non-target resource:

```text
D_a       r-1       D_c       2
U_acs     2         U_bcs     r
X_ac      1         X_as      2(r-1)
X_bc      2r        X_cs      1
```

Thus the exact maximum is `2r=2(m-1)`, attained at the canonical auxiliary
owner/slot of type `X_bc=D+c`.  A noncanonical auxiliary slot has load zero
in this subcatalogue; additional legal slot lifts are not part of this exact
count.  The four target resources are deliberately excluded: all candidates
must contain them.

This count uses the fixed canonical slot section declared in the theorem.
If auxiliary slots were allowed to be chosen afresh per catalogue member,
the phrase “the catalogue” would not define a finite literal family and the
load statement would have no fixed meaning.

## 3. Independent executable audit

The C++ audit uses one canonical slot label per owner mask, matching the
fixed slot section in the theorem.  It

```text
scratch/audit_k_pcs_row2_private_gainone_hex_20260802.cpp
```

reconstructed every canonical packet for `m=3,...,20`.  For every case it
checked:

1. all ranks and six lower--upper containments;
2. all twelve resources are distinct within their types/slot labels;
3. distinct `(b,c,orientation)` triples give distinct packet supports;
4. the catalogue has size `2(m-1)(m-2)`; and
5. the largest load of a non-target resource is exactly `2(m-1)`.

Representative endpoints of the replay were

```text
PASS m=3  candidates=4   max_non_target_load=4
PASS m=9  candidates=112 max_non_target_load=16
PASS m=20 candidates=684 max_non_target_load=38
```

All intermediate dimensions passed.  The audit source SHA-256 is

```text
b909c67e12c6e8fbbf31bb641bdddf0c26aa9af056357a0c05bd24f8fd276da7
```

## 4. Packing constant

For the packet currently selected, the forbidden set contains at most

```text
|B|                       external resources
4(p-1)                    resources of other targets
8(p-1)                    auxiliaries of earlier packets.
```

Hence it has order at most `|B|+12(p-1)`.  Each forbidden resource kills at
most `2r` candidates, while the current catalogue has `2r(r-1)` members.
The strict inequality

\[
                         |B|+12(p-1)<r-1=m-2
\]

therefore leaves at least one candidate at every greedy step.  This proves
the stated constant without an independence or random-overlap assumption.

## 5. Scope audit

The following promotions would be invalid and are not made in the theorem.

* A local on phase is a forest, but replacing off phases in a global forest
  can create a global cycle.  The graphic-ear row remains explicit.
* The catalogue does not put the two off atoms into an arbitrary existing
  factor.  Their prospective planting is the `DOP` gate.
* Target atoms must already be pairwise resource-disjoint.  This includes
  both physical owner slots and is stronger than separate upper/tail Hall.
* A palette-neutral pull auxiliary graph must remain connected and
  tree-coherent after the packet bank is protected.  Raw packet abundance
  proves neither fact.
* The result is asymptotic for an `O(d)` protected/defect bank.  At `m=9`
  it does not authenticate or complete the current `k=17` one-hole or
  22-boundary-ticket trajectory.

Accordingly, the proved implication is exactly

\[
 \text{resource-disjoint target atoms + planted off phases}
 \Longrightarrow
 \text{private, lossless full-upper occurrence repair},
\]

followed by separately stated graphic--Rado and transparent pull-tree rows.
