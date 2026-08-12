# Independent audit of the RF495 middle9 endpoint-Hall obstruction

Date: 2026-07-30  
Status: `GO`, solver-free, for the middle9-only incumbent-pinned face.

## Scope

The authenticated repeat-free seed5/self RF495 collar has mutable-chain
lengths `4/9/5`.  This note fixes the left four and right five cells to the
three-hole lead and permits arbitrary nonzero values only at physical
positions

```text
6434,6435,6436,6437,6438,6439,6440,6441,6442.
```

It proves this middle9 face infeasible.  It does not decide either two-chain
face, the unrestricted RF495 fibre, any other parent/layout, or unrestricted
K16 equality.

## The physical ten-target core

The core is

```text
18e7, 1c67, 1f54, 9867, 98e6,
99c6, 9c63, 9e54, 9e64, b986.
```

All ten masks have rank eight, so they are pairwise incomparable.  Exact
replay of the complete physical literal-interval table gives:

```text
core literal intervals:       812
middle-supported intervals:   558
outer-supported intervals:    254
outer intervals valid at pins:  0
```

For every core target, the set of right endpoints of all middle-supported
physical intervals is exactly

```text
{6434,6435,6436,6437,6438,6439,6440,6441,6442}.
```

## Hall theorem

In any completion, every core target must therefore be realized by a
middle-supported physical interval.  Map each target to the right endpoint
of its realizing interval.  This map is injective: two full physical
intervals with the same right endpoint are nested, so their complete literal
OR masks are comparable by inclusion.  Two distinct rank-eight core masks
are incomparable and cannot share that endpoint.

The required injection has ten sources and nine endpoints.  Equivalently,
the endpoint bipartite graph has maximum matching size nine and Hall
deficiency one.  Deleting any one core target restores a matching of size
nine, so the displayed obstruction is inclusion-minimal.

It is also cardinality-minimal among endpoint-Hall obstructions in this
face.  Reconstructing all forty middle-mandatory targets gives the endpoint
neighborhood-size histogram

```text
9:32, 10:2, 11:2, 12:3, 15:1.
```

Every nonempty target family therefore has at least nine neighboring
endpoints; a Hall-deficient family must contain at least ten targets.  The
core meets that lower bound.

## Plateau/end-point audit

The physical catalogue has `6,089` potential literal intervals but only
`6,081` semantic `(target,Q,fixed-OR)` representatives.  The audit uses the
uncollapsed `6,089` rows and reconstructs every row's support, fixed halo,
and incumbent full OR directly from the 12,873-cell word.

The eight extra plateau rows belong to three semantic keys, all for target
`0xbbde`.  No plateau key intersects the ten-target core.  Within the core,
the physical and semantic tables both have 812 rows and identical endpoint
sets.  Thus quotienting the eight global plateau duplicates cannot hide a
new core endpoint.

The fixed halos cause no exception to the nesting proof: the compared
objects are the complete physical intervals, not just their mutable
supports.  Their full literal ORs are the target masks themselves.

## Frozen independent artifacts

```text
scratch/audit_k16_rf495_middle9_endpoint_hall_independent_20260730.py
  SHA-256 2d60074e99df8d23ad125b86901274cf2d56223c3c4dfd53fa6d730f500b56cf

scratch/k16_rf495_middle9_endpoint_hall_independent_20260730/
  middle9_endpoint_hall.independent.audit.json
    SHA-256 fd84183cf9f4ba76157a1e963dc06a02ebc9a874ffbebfef0be356ab0a277d31
    payload 6c6c6c69f54985b7b67538356f4f9f81f050f1065fcb41b6826358248bba87e8
  middle9_endpoint_hall.core.tsv
    SHA-256 81a03340ee0784f89b7c54f086a19f515ae3ced2b202e9cf3231c3d56e1dd2ba
```

Pinned inputs include the full potential-literal table SHA-256
`c8f7381486c0412f9f3d34a724d6bbfdc60c210fbf1a2bb2aaa647fad3f0e6dc`
and lead-word SHA-256
`9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6`.
No solver was invoked.
