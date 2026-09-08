# Adversarial audit: K16 radius-three provider and frozen-gap theorem

Date: 2026-07-30  
Lane: R  
Audited source: `MATH_THEOREM_R_K16_RADIUS3_PROVIDER_PARTITION_AND_FROZEN_GAP_COLLARS_20260730.md`

## 1. Verdict

The one/two/three-site partition, the `13,627` positional-support count, the
three frozen-gap profile exhaustion, maximal-context domination, and the
245-value closure normalization are valid in their stated finite scopes.

Two wording corrections were required.

1. The `13,627` triples are potential supports for a final `B` interval that
   contains all three sites.  Before lower-site witnesses are excluded, this
   bank can overlap the one-site and two-site branches; it is not a disjoint
   branch merely from its positional definition.
2. Exact Hamming distance three requires
   `u != W_p`, `v != W_q`, and `w != W_r`.  Omitting these inequalities is
   valid only as a relaxation for a no-go.  The theorem now states this
   explicitly.

The audit also proves a sharper result: all `13,627` all-three-site supports
are impossible.  This closes that branch, but not the one-site-plus-two-edit
or two-site-plus-one-edit branches.

## 2. Provider partition and support count

If a final literal `B=0x2c6d` interval meets one, two, or all three edited
sites, the corresponding branch is forced.  Since the source has no `B`
interval, it cannot meet zero sites.  This is exhaustive and uses one common
physical word.

For an all-three interval with sites `p<q<r`, every unchanged internal cell
except `q` must be a submask of `B`.  Thus the open interval `(p,r)` may
contain at most one source cell with a bit outside `B`; if it contains one,
that cell is forced to be `q`.  The unrestricted scan reproduces

```text
span 2: 12,871
span 3:    629
span 4:    110
span 5:     17
total:  13,627
```

and encounters no longer support.  The zero-bad contribution is independently

```text
315 + 2*41 + 3*7 = 418,
```

leaving `13,209` one-bad supports.  This agrees exactly with the previously
frozen support audit.

## 3. Solver-free all-three obstruction

For a support `S={p,q,r}`, a target is private when every old witness meets
`S`.  Removing the sites splits the word into four components, so privacy is
equivalent to absence from the prefix before `p`, the two open internal
segments, and the suffix after `r`.  Earliest-end/latest-start running-OR
states test the two unbounded components exactly.

For each consecutive edited-site class

```text
{p}, {q}, {r}, {p,q}, {q,r}, {p,q,r},
```

the checker enumerates the distinct ORs `F` of fixed cells in literal
intervals of that class.  A genuine new witness for `T` implies

```text
F subset T subset (F OR B).
```

Allowing this relation independently for every target, allowing zero edited
mass, and ignoring shared-value consistency is a relaxation.  A failure is
therefore a mathematical obstruction.  It excludes `13,620` supports.

Exactly seven supports survive the relaxation; all are consecutive triples:

```text
(1,2,3)
(2686,2687,2688)
(3529,3530,3531)
(3958,3959,3960)
(4486,4487,4488)
(4498,4499,4500)
(5922,5923,5924)
```

For these, exact shared-value consistency reduces to the 255 nonzero
submasks of `B`.  For every ordered pair `(u,v)`, the checker stores the
bitset of admissible `w` values, first enforces an all-three literal `B`
witness, and then intersects the exact six-class witness relation for each
private target.  Short target prefixes of lengths `3,3,6,5,8,6,8`
respectively empty all states.  This is an exact finite OR-state dynamic
program, not SAT and not an independent-value relaxation.

It permits a new value to equal its source value.  Consequently its empty
result is stronger than the desired genuine-three-substitution exclusion.

## 4. Frozen-gap and context audit

Within the architecture

```text
A_5 | G_1 | B_9 | G_2 | C_4,
```

deleting one arbitrary collar slot and then freeing all surviving collar
values gives exactly the ordered-word profiles `(4,9,4)`, `(5,8,4)`, and
`(5,9,3)`.  The deleted source identity is immaterial only because every
remaining slot in that collar is arbitrary; this does not authorize moving
or changing a gap.

Both gaps are fixed, with ORs `0x7fff` and `0xffff`.  Every one of the common
57 residual targets omits a bit present in either complete intervening gap,
so no residual witness crosses a gap.  Each witness lies in one collar plus
an adjacent fixed suffix/prefix.

For a fixed target and local editable interval, allowed left suffix ORs and
right prefix ORs form nested chains.  Their independently longest values
contained in the target are simultaneously realizable, and their OR is the
unique maximum compatible context.  If a smaller base `F` witnesses `T`,
then the maximum `F'` satisfies

```text
F subset F' subset T  =>  F' OR Y = T.
```

Thus keeping one maximal context per target/local interval is iff-exact for
this model.  The statement is not that there is one context globally.

## 5. Closure audit

For the common residual family `R`, replacing a live cell `v` by

```text
N(v) = intersection {T in R : v subset T}
```

preserves every selected residual witness: each replacement grows the cell,
stays inside the witness target, and therefore leaves the aggregate OR equal
to that target.  A dead value occurs in no residual witness and may be sent
to the verified live sentinel `0x0001`.  Targets outside `R` retain witnesses
wholly in fixed gaps.

The normalization is equisatisfiable and has exactly 245 nonzero images.  It
does not preserve Hamming distance from an incumbent and cannot be used in an
exact-edit-count theorem without a separate argument.

## 6. Artifacts and exact boundary

```text
scratch/audit_r_k16_radius3_allthree_overapprox_20260730.py
SHA-256 c6b8561ad7677de6492a15d97f150c6814697dad363b52b856c4d2d582cf932a

scratch/r_k16_radius3_allthree_solverfree_obstruction_20260730.audit.json
SHA-256 51dad15c6e7bbee6b2771906588d4af79130aa0d9bfacb7456b6c8ca3f4121f8

scratch/r_k16_upper12874_delete_radius3_supports_20260730.audit.json
SHA-256 e300b79ad60636d5c4d010d3bd8e66d6538046aed86f87b71357664c28937aba
```

Proved: no all-three-site radius-three completion exists around the frozen
best deletion word.

Still open in the global radius-three fibre: a final `B` witness using one
edited site followed by two cooperating repairs, or using two edited sites
followed by one repair.  The three collar CNFs also remain without a checked
SAT/UNSAT disposition.  Nothing here proves or disproves an arbitrary
length-12,873 word.
