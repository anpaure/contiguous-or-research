# Authenticated k=15 octahedral AA/BB global-curvature descent

Date: 2026-07-30

## 1. Scope and source

This audit starts from the authenticated all-depth-complete `k=15` factor
used by

```text
scratch/audit_k11_k13_k15_aa_octahedral_c6_20260730.py
```

and uses only literal four-label octahedral `C6` switches on the two Pascal
shores `AA` and `BB`.  Every accepted state is replayed as a physical
2-factor and checked for

1. degree two at every middle owner;
2. every lower and upper shadow at depths `q=1,...,7`;
3. no positive coordinate run shorter than four; and
4. the exact negative run histogram and the exact negative `phi_5`.

The search does **not** alter the owner set, add arbitrary Johnson edges, or
relax any shadow condition.

## 2. The frozen nine-BB state

The first nine compatible BB atoms from the authenticated audit reproduce
exactly

```text
physical component sizes = 3930,1467,461,461,71,45
positive phi_5          = 1427
negative phi_5          = 5738
short positive runs     = 0
short negative runs     = 1996
all lower/upper shadows = complete
```

The deterministic replay is

```text
scratch/reproduce_k15_octahedral_bb9_plateau_20260730.py
scratch/k15_octahedral_bb9_plateau_20260730.audit.json
```

## 3. Why the earlier recensus stopped prematurely

The original atom audit first required improvement of the *split-coordinate
path-length proxy* and only then performed a global physical replay.  That
proxy is sufficient for finding some useful atoms, but is not the global
negative-run objective.  A split-neutral or split-worsening atom may still
shorten negative runs of other coordinates after the physical components are
rethreaded.

The corrected engine therefore enumerates every currently selected literal
octahedral `C6`, physically applies it, and scores the actual global run
histogram before filtering.  At the frozen BB9 state this exposes 63 globally
safe improving single atoms even though the split-proxy recensus had exposed
none.

## 4. Complete BB pair census and dynamic descent

On the frozen BB9 state there are 440 currently available literal BB atoms.
A complete census tested all 96,269 pairs with disjoint changed-edge support.
Among them,

```text
3,457 pairs are all-depth-complete, positive-resident, and improving.
```

The best pair reduces

```text
short negative runs 1996 -> 1990
negative phi_5      5738 -> 5732.
```

After this pair, dynamically re-enumerating the catalogue after every move
and taking the exact steepest safe single atom accepts 51 further BB moves,
reaching

```text
short negative runs = 1937
negative phi_5      = 5638.
```

The corresponding artifacts are

```text
scratch/k15_octahedral_bb9_compound_pair_census_20260730.audit.json
scratch/k15_octahedral_bb9_compound_pair_best_20260730.cycles.txt
scratch/k15_octahedral_dynamic_greedy_descent_20260730.audit.json
scratch/k15_octahedral_dynamic_greedy_descent_20260730.cycles.txt
```

## 5. Two-shore AA/BB descent

Adding the AA shore is decisive.  Starting from the BB state above, exact
steepest descent over the union of the dynamic AA and BB catalogues accepts
74 more moves and reaches

```text
physical component sizes = 5695,478,217,45
short positive runs      = 0
short negative runs      = 1849
positive phi_5           = 1478
negative phi_5           = 5488
all lower/upper shadows  = complete.
```

Running the same AA/BB greedy rule directly from BB9 reaches the identical
short-gap floor 1849 (and negative `phi_5=5489`), so the floor is not an
artifact of the preliminary BB-only route.

At this state a complete two-shore commuting-pair census has the following
exact funnel:

```text
available atoms                         938
compatible disjoint-support pairs   438854
lexicographically improving pairs     88155
also positive-resident                 3475
also all-depth-complete                    0
```

Thus 1849 is a genuine local minimum for **single atoms and commuting pairs
available at that state**.  It is not a no-go for dynamic triples or for a
neutral walk.

## 6. Crossing the 1849 pair plateau

An invariant-preserving anneal was then run on the same dynamic catalogue.
Every accepted state still passed all physical shadow and positive-residence
checks.  The anneal takes safe neutral or mildly worsening moves, thereby
changing the available catalogue, and then resumes descent.  Seed 13 reached
1841 short negative runs; a final exact greedy harvest reduced its negative
`phi_5` to 5484 without changing the short count:

```text
physical component sizes = 5695,263,214,185,45,33
short positive runs      = 0
short negative runs      = 1841
positive phi_5           = 1475
negative phi_5           = 5484
all lower/upper shadows  = complete.
```

Artifacts:

```text
scratch/k15_octahedral_AABB_greedy_descent_20260730.audit.json
scratch/k15_octahedral_AABB_greedy_descent_20260730.cycles.txt
scratch/k15_octahedral_AABB_pair_plateau_20260730.audit.json
scratch/k15_octahedral_AABB_anneal_seed13_20260730.audit.json
scratch/k15_octahedral_AABB_anneal_seed13_20260730.cycles.txt
scratch/k15_octahedral_AABB_harvest1841_20260730.audit.json
scratch/k15_octahedral_AABB_harvest1841_20260730.cycles.txt
```

The search/replay engine is

```text
scratch/search_k15_octahedral_bb_compound_pairs_20260730.cpp
```

and was compiled with `g++ -O3 -march=native -std=c++20` and run on the H100
host CPU.  The final cycle files were independently replayed with the Python
shadow and residence auditors.

## 7. Exact unique-shadow accounting

There is a local exact formulation behind the replay.  Let `F` be a physical
2-factor, let `E_-` be the three edges removed by one octahedral switch, and
let `E_+` be the three inserted edges.  For a target mask `S` and depth `q`,
write `mu_q^F(S)` for its number of cyclic-window occurrences.  Every window
not traversing a changed edge survives unchanged.  Hence

```text
mu_q^(F')(S) = mu_q^F(S) - d_q(S) + c_q(S),
```

where `d_q(S)` is obtained by enumerating only old radius-`q` windows that
traverse `E_-`, and `c_q(S)` by enumerating only new radius-`q` windows that
traverse `E_+`.  Thus a switch is shadow-safe exactly when

```text
mu_q^F(S) - d_q(S) + c_q(S) >= 1
```

for every lower/upper target and every audited depth.  Targets with
`mu=1,d=1,c=0` are the exact unique-shadow blockers.

For a pack whose changed-edge radius-`q` neighbourhoods are disjoint, these
deltas add literally.  Without that separation, the same identity remains
true after including the interaction windows that traverse more than one
changed edge.  The physical replay used here computes precisely this complete
interaction version.  Therefore the pair and pack funnels below are not
heuristic collision tests; their final shadow verdict is the exact
unique-witness inequality.

## 8. Mixed-coordinate cells

The AA/BB catalogue above treats the distinguished coordinate `z=14` as a
spectator: every switched `C6` lies wholly in the `z=1` or `z=0` shore.  The
full literal octahedral catalogue also contains cells in which `z` is one of
the four varying labels.  These mixed cells contain AA, BB, and cross-shore
edges (or the complementary three-cross-edge resolution).

Adding these cells to the dynamic exact scorer produces another immediate
greedy cascade.  From the 1841 state, 50 safe moves (39 mixed, 6 AA, 5 BB)
reach

```text
physical component sizes = 5285,691,414,45
short positive runs      = 0
short negative runs      = 1802
positive phi_5           = 1494
negative phi_5           = 5412
all lower/upper shadows  = complete.
```

Artifacts:

```text
scratch/k15_octahedral_FULL_greedy1802_20260730.audit.json
scratch/k15_octahedral_FULL_greedy1802_20260730.cycles.txt
```

This shows that the shore filtration is itself a useful description of the
descent: BB moves unlock AA moves, and AA moves unlock mixed-coordinate moves.

A cached-catalogue invariant anneal (the catalogue is rebuilt every 50
accepted/attempted steps; every accepted move is still exactly replayed)
then crosses the 1802 single-move floor.  Four 20,000-step deterministic
seeds were run; the best reached 1779 short gaps.  An exact greedy harvest
then reduced its negative `phi_5` to 5388:

```text
physical component sizes = 3403,1638,466,375,329,150,45,29
short positive runs      = 0
short negative runs      = 1779
positive phi_5           = 1497
negative phi_5           = 5388
all lower/upper shadows  = complete.
```

```text
scratch/k15_octahedral_FULL_anneal1779_20260730.audit.json
scratch/k15_octahedral_FULL_anneal1779_20260730.cycles.txt
scratch/k15_octahedral_FULL_harvest1779_20260730.audit.json
scratch/k15_octahedral_FULL_harvest1779_20260730.cycles.txt
```

The 1779 state is substantially more rigid than the earlier plateaux.  Its
full literal catalogue has 1,293 available atoms.  A complete census of all
834,286 commuting disjoint-support pairs gives

```text
preliminary improving pairs          152223
also positive-resident                 9294
also all-depth-complete                   0.
```

Thus no single atom and no commuting pair available at this state improves
the lexicographic `(short gaps, negative phi_5, positive phi_5)` objective
while retaining the invariants.  Four high-temperature exact safe walks,
30,000 accepted moves each, also found no state below 1779.  This last fact is
empirical rather than exhaustive, but it probes a large part of the
invariant-preserving neutral component.

Fixed-baseline random compound searches add the following negative scope:

```text
pack size       trials     prelim improving   positive-resident   all-depth
3               250000          36632                633              0
4               250000          28745                143              0
5               250000          23127                 29              0
6               250000          18340                  7              0
```

A targeted one-atom repair was then tried after 50,000 random improving base
pairs and base triples.  It tested 731,516 and 149,100 repair atoms,
respectively, and again found no all-depth improving final pack.  These pack
experiments are sampled no-go results, not exhaustive theorems.

Finally, 216 positive-resident improving single atoms and 55 such base pairs
were each followed by a freshly re-enumerated dynamic repair catalogue
(350,169 repair atoms tested in total).  No all-depth improving two/three-step
compound was found.  This closes the most obvious newly-created-atom escape
in the sampled scope, but is still not an exhaustive triple theorem.

```text
scratch/k15_octahedral_FULL_pair_plateau1779_20260730.audit.json
scratch/k15_octahedral_FULL_randompack{3,4,5,6}_1779_20260730.audit.json
scratch/k15_octahedral_FULL_1779_repair{2,3}.audit.json
scratch/k15_octahedral_FULL_1779_dynrepair{1,2}.audit.json
```

## 9. Exact conclusion

The octahedral move lane is not locally dead.  The first apparent plateau was
a proxy-scoring artifact, the BB-only plateau was crossed by exact pairs, and
the genuine two-shore single/pair plateau was crossed by a safe neutral walk.
The authenticated defect count has fallen

```text
2010 -> 1996 -> 1990 -> 1937 -> 1849 -> 1841 -> 1802 -> 1779.
```

This is a strict invariant-preserving descent, but it is not yet a
bi-resident factor: 1779 short negative runs remain.  The next scoped target
is to iterate `neutral walk -> exact greedy harvest -> complete pair census`,
and, if that rate stalls, replace the neutral walk by an exact small-pack LNS
over dynamically created AA/BB atoms.
