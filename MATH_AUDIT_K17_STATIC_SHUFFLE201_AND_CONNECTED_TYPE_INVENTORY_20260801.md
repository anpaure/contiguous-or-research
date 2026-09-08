# k=17 static shuffle201 factor and connected type-inventory audit

**Date:** 2026-08-01  
**Status:** two independently replayed finite reductions.  Neither is a
`k=17` word and neither proves the missing integral chronology.

## 1. A third exact static lower-flag factor

The randomized rooted-static factor model produced

```text
scratch/k17_rank8_rooted_static_shuffle201_20260801.certificate.tsv
SHA256 d44b60611a3c9e4ba1533a774762fce825d327dcc7536cdcd9c10522404b1ad3
```

The independent decoder and literal factor verifier both pass:

```text
PASS_K17_ROOTED_STATIC_MODEL_DECODE roots=1430 exact_target_orbits=2424
PASS_K17_RANK8_ROOTED_STATIC_CERTIFICATE roots=1430 tight_target_orbits=2424
```

The exact attachment audit gives

```text
legal packet turns                  970
labelled state arcs                7760
packet-support maximum matching     556
zero packet out                     723
zero packet in                      826
```

This is a genuinely different Pareto basin.  It has sixteen fewer dead
tails than the previously best-matching `e973...` factor, but its raw
packet matching is one smaller (`556` rather than `557`).  Consequently it
is neither dominated nor a solution: exact circuit optimization must be
replayed in this factor's own catalogue.

### 1.1 Complete support-at-most-two circuit replay

The complete unary/binary palette-neutral catalogue was then optimized
serially inside this basin.  The frozen selection contains 42 unary and
407 binary root-disjoint circuits, changing 856 of the 1,430 rooted rows.
The exact resource ledger and reconstructed final table both pass an
independent clean-room replay.  The final table is

```text
scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
```

Its literal transition statistics are

```text
legal packet turns                 1855
labelled state arcs               14840
packet-support maximum matching     954
packet Hall deficiency              476
zero packet out                     234
zero packet in                      445
```

This is a large authenticated improvement over every frozen starting
factor and proves that the old 530--557 plateau was basin-local.  It is
still not a chronology.  The owner projections are different relaxations:
the direct replay has 351 zero-in owners, root--owner in/out/both-live
matching values 890/1196/718.  The both-live graph has an exact Hall shore
of size `770 -> 58`, hence deficiency 712; no common root--owner
transversal exists on this terminal table.  Connectivity, voltage, upper
shadows, opening, and compiler rows remain outside this circuit audit.

The correct continuation is serial: regard the `e28a8ee...` table as a new
exact factor, regenerate its primitive unary/support-two catalogue, and
allow circuits overlapping roots changed in the first 449-circuit packet.
The original root-disjoint catalogue cannot express those moves.

That continuation is productive.  Clean re-enumeration and replay gives:

| exact table | packet matching | common root--owner matching | common deficiency |
|---|---:|---:|---:|
| first circuit wave | 954 | 718 | 712 |
| serial round 1, reverse | 1110 | 867 | 563 |
| serial round 2, reverse | 1178 | 936 | 494 |
| serial round 3, reverse | 1206 | 965 | 465 |

The round-two reverse table has SHA
`560d8d86a7728d1b1e6497c00547aafbcc75c8b5e2b52e9f7ff60144bdfe85fe`
in the independent common-live audit.  Its exact Hall shore has
`652 -> 158`.  These are still relaxation scores: no perfect common
transversal exists and therefore no quotient component profile is defined.
They do establish sustained descent of the actual common obstruction under
overlapping serial palette-neutral circuits.

Round three further reaches common matching 965 with Hall shore `654->189`
(deficiency 465).  The diminishing packet-first gains motivate the next
separate basin: price circuits directly against the common DM shore rather
than using packet matching as the primary objective.

That common-first branch gives the strongest terminal table so far.  From
the round-two baseline it selects 168 resource-exact support-at-most-two
circuits on 313 roots and obtains

```text
common root--owner matching  936 -> 1099
packet matching             1178 -> 1156
common Hall shore             365 -> 34
common deficiency                    331
```

The final table SHA is
`4e7a5fa38a661feea83dcc7bb9179e9194130b13a3fad3e810f169ce3e225402`.
Both the circuit selection and the common-live DM matching pass separate
clean-room replays; the latter has payload SHA
`b3fe2b2a286c8e5845c81c57e270d1ac4666126e7072ae7e734818d37ea9f4a6`.
This verifies that the packet and common objectives are genuinely
different, and that optimizing the actual common shore is substantially
better.  It remains a necessary relaxation rather than a cycle cover.

The serial recataloguing effect is structural, not merely a new greedy
order.  Around the first-wave factor there are 2,561 unary and 214,610
indecomposable binary circuits.  Its binary literal columns have **zero**
overlap with the original 213,670-column catalogue, despite 2,155 shared
row endpoints.  Every one of its 351 dead owners is individually
repairable, and all 67 owner demands missed by the union of the earlier
factor basins now have literal witnesses.  Simultaneous resource-exact
selection remains open.

Two further common-first recataloguing rounds have now been independently
replayed.  They optimize the actual common root--owner both-live matching,
not the easier packet projection:

| exact factor | selected circuits | changed roots | packet matching | common matching | exact Hall shore | deficiency |
|---|---:|---:|---:|---:|---:|---:|
| `4e7a5f...` | 168 | 313 | 1156 | 1099 | `365 -> 34` | 331 |
| `4213de...` | 69 | 131 | 1166 | 1132 | `319 -> 21` | 298 |
| `ae88fc...` | 24 | 43 | 1171 | 1141 | `306 -> 17` | 289 |
| `2e9194...` | 2 | 4 | 1172 | 1141 | `309 -> 20` | 289 |

The first common-primary plateau SHA is
`2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb`;
its predecessor `ae88fc...` has the same common deficiency with a slightly
smaller canonical shore.  A fresh complete catalogue at `2e9194...` accepts
no move in the declared deterministic strict sweep.  This is an
order-specific fixed point, not a support-two ceiling.
The selector, literal owner-demand ledger, and common-live DM shore all pass
separate clean-room audits under
`scratch/laneK_k17_commonfirst_serial_20260801/`.  No full common
transversal is claimed: the exact remaining quotient deficiency is 289,
and therefore no cycle cover, component profile, voltage, opening, upper
deck, or compiler consequence follows yet.  The strict improvement across
freshly regenerated catalogues is nevertheless direct evidence that the
support-two move graph has useful serial depth; the sharply diminishing
gains make a synchronized Benders/min-cut objective the next appropriate
finite model.

## 2. Minimal connected type inventory

The earlier anonymous type-cycle inventory had three weak components:
`{D}`, `{E,F}`, and the main component.  It therefore could certify an
exact labelled factor but could never itself support one Hamilton quotient
chronology.

Two legal transportation switches give the minimum connected repair:

\[
(D,D)+(H,H)\mapsto(D,H)+(H,D),
\]
\[
(E,F)+(H,H)\mapsto(E,H)+(H,F).
\]

All nine row and column type margins are unchanged.  The modified rows are

```text
D: D19, H1
E: F19, H1
H: A139, D1, F1, H96
```

and the support is strongly connected.  The exact builder and independent
decoder are

```text
scratch/build_k17_incidence_bimatching_age_skeleton_20260801.cpp
SHA256 43d73fc40ad0399ff2d53fe1e9512a7e1ca4ee6a1a655c8603fb67ba69d3352a

scratch/verify_k17_incidence_bimatching_age_model_20260801.cpp
SHA256 c2bdeb4bd60f2b7f8a51b51460b59243f442709e4c54ff8979ec496109b833f8
```

The connected staged-rank7 CNF has

```text
4,800,796 variables
17,426,826 clauses
CNF SHA256 1b7ae102244972b374277d19fd8f51c9a768eb7c4909a21dee561742a04932b7
map SHA256 d023b93f604031a1430f8b183d22daf1934d26e324413345f47e97ec5e4a0a0d
```

It enforces exact owners, exact roots, literal depth-three age recurrence,
the exact rank-seven lower palette, and the connected type-pair inventory.
It deliberately omits ranks two through six, strict upper shadows,
quotient-cycle connectivity cuts, nonzero voltage, and the physical opening.

The first proof-retaining two-solver portfolio reached its 1,800-second
limits without a verdict.  Kissat was terminated at the wall with no `s`
line; CaDiCaL exited normally at its internal time limit with no SAT/UNSAT
line and only a 2.5-GiB incomplete DRAT prefix.  The exact status is
**UNKNOWN**, not infeasible.

### 2.1 Owner/age-only calibration face

A separate `--owner-only` mode omits every named lower suffix row while
retaining exact D/H owner and root matchings, the complete literal
depth-three age recurrence, and the same connected type inventory.  Its
purpose is diagnostic: SAT would supply a literal aligned chronology seed
and locate the first additional difficulty in named lower colouring; UNSAT
would refute this fixed type inventory before any rank-seven issue.

```text
4,408,690 variables
14,757,588 clauses
CNF SHA256 fdedb447e07c6cb0fc8441b784b633173affc9e0d158934afc6ba418c6a34b6d
map SHA256 d023b93f604031a1430f8b183d22daf1934d26e324413345f47e97ec5e4a0a0d
```

No finite verdict is claimed here.  Even SAT would omit all lower palettes,
connectivity cuts, voltage, upper shadows, opening, and compiler rows.

The first 900-second two-solver calibration is also **UNKNOWN**.  CaDiCaL
reached its internal limit with exit zero and no status line; Kissat reached
the 930-second outer wall with exit 124 and no status line.  Neither outcome
is evidence of infeasibility.  It does show that the flat CNF remains hard
even before named lower colouring, so the circuit/Benders decompositions
are computationally better motivated than longer undifferentiated runs.

## 3. Fractional versus integral scope

The connected inventory has a complete symmetric fractional realization:
uniformly coupling compatible labelled age partitions on every oriented
Johnson edge satisfies all owner/root/lower marginals.  Therefore an exact
UNSAT result would be a one-copy nonnormality theorem, not a scalar or
fractional Hall obstruction.

An important later correction is required here.  The old determinant-two
triangle was mis-typed under a one-based/zero-based conversion: its packets
have types `H,G,G`, so its arcs `H->G,H->G,G->G` all have zero capacity in
the connected inventory.  Exhaustive O3 replay finds **no** strong `C3` in
the connected face.

The fixed inventory nevertheless does not restore balancedness.  It has an
authenticated zero-holonomy clean `C5`, with arc types
`G->H,G->H,H->H,C->H,C->H`.  This `C5` is not a local parity obstruction:
one literal portal atom and two resource-disjoint alternating-cycle atoms
saturate all five selected rows.  The remaining obstruction is simultaneous
portal packing, equivalently a fractionally light odd-cycle transversal,
not the previously claimed determinant-two triangle.
