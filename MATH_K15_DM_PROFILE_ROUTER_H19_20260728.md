# k=15 DM profile router: exact H20 -> H19 descent

## Scope

This note certifies one carrier/compiler descent.  It does **not** construct a
length-6438 covering word and does **not** prove `nu(15)=6438`.

The frozen chain is

```text
H20  -- RF(180,2764,4210) -->  H20  -- FR(123,722,4710) -->  H19.
```

The exact checker is
[`scratch/audit_k15_h20_h19_profile_router_theorem.py`](scratch/audit_k15_h20_h19_profile_router_theorem.py),
with machine-readable output in
[`scratch/audit_k15_h20_h19_profile_router_theorem.json`](scratch/audit_k15_h20_h19_profile_router_theorem.json).

## Frozen states

| state | file SHA-256 | Hall | matching | zero | DM shores | DM components |
|---|---|---:|---:|---:|---:|---:|
| base | `9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1` | 20 | 16363 | 6 | 677/657 | 20 |
| router | `eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51` | 20 | 16363 | 6 | 677/657 | 19 |
| final | `86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b` | 19 | 16364 | 6 | 516/497 | 18 |

All three middle paths contain all 6435 distinct rank-8 sets, are Johnson
paths, and have no residence defect.  Their lower hole vector is unchanged,

```text
[4,18,11,1,0,0,0],
```

and every audited upper layer `q=1,...,7` is complete.

## The neutral router

Before the router, the DM decomposition has two rooted native bases

```text
root 8217: 161/160,
root 8218: 160/159.
```

The neutral braid joins them into one two-root native forest

```text
core 8216: 321/319,
missing native roots exactly {8217,8218}.
```

Its target shore is the disjoint union of the two old target shores, so the
total gap remains two.  All 18 other components are identical.  At the cell
profile level, 317 of 319 profiles are common; two shores are regrouped into
two different shores.

Crucially, the complete abstract profile of the separate 161/160 component
rooted at 24610 is unchanged.  The router changes its physical chronology,
not its Hall rank or abstract incidence multiset.

## The improving braid and the common-Q certificate

The second braid discharges the complete old component rooted at 24610.  Its
161 targets have a final 162-cell neighbourhood of rank 161.  That
neighbourhood is disjoint from the final DM right shore, and the old DM left
shore is the disjoint union of this 161-target block and the final 516-target
DM left shore.

The local profile surgery is exact:

```text
common profiles: 159
lost:             {26146,26402}
gained:           {26146}
                  {26402}
                  one extra copy of Q={24610,25634}
```

The profile `Q={24610,25634}` already existed once and has multiplicity two
after the braid.  The two physical Q-cells can serve its two targets
independently.  One explicit restricted matching uses

```text
24610 -> cell 1212
25634 -> cell 4713
26146 -> cell 11150
26402 -> cell 17586.
```

Thus the old paired shore splits into two singleton shores while a second
copy of the common Q is created.  This raises the contracted boundary rank
from 20 to 21 and the global matching from 16363 to 16364.

## Structural reading

The successful neutral move is not another DM-compression move.  It leaves
the total DM shore sizes at 677/657, merges two gap-one bases into a gap-two
forest, and changes the physical chronology while preserving the abstract
24610 component profile.  The next braid then creates a duplicate common-Q
cell and obtains a genuine local rank gain.

This is different from the audited H20 double-compression lane: those neutral
moves reduced DM shore sizes, but the scanned top-compression descendants did
not expose an H19 move.  Compression remains a useful heuristic, but this
certificate shows that **profile routing/physical realizability is an
independent search coordinate**.
