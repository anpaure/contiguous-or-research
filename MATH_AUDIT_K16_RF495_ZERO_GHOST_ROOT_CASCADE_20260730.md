# K16 RF495: zero-ghost frontier, exact `70^3` root atlas, and sharp rehost cascade

Date: 2026-07-30  
Status: **exact, independently replayed, and scoped to the frozen repeat-free
seed5/self `4/9/5` fibre.  The full fibre remains under exact search.**

## 1. Frozen object

The literal layout is

```text
[4 free] + seed5[6:6436] + [9 free]
         + (0x8000 | seed5[7:6432]) + [5 free].
```

The eighteen free positions are

```text
0..3, 6434..6442, 12868..12872.
```

The authenticated incumbent has length `12873`, covers `65532/65535`
nonzero masks, and misses

```text
0x18e7, 0x3de7, 0x9e20.
```

All results below use the complete maximal same-`(target,Q)` provider atlas:
seventy residual targets, seventy contiguous free-position sets `Q`, and
exactly `70*70=4900` maximal providers.

## 2. Zero-ghost middle frontier

The architecture-free deadline theorem says that every universal nonzero
K16 word of length `L=W+e` satisfies

```text
Lambda <= (e-G)(L+G).
```

Here

```text
W=12870, L=12873, e=3, Lambda=26332.
```

Already at `G=1`, the right side is

```text
2*12874 = 25748 < 26332.
```

Hence every universal length-`12873` word has **zero repeated middle
deadlines**.

An independent literal replay of the two fixed bodies gives:

* `12849` first rank-eight deliveries;
* `12849` distinct rank-eight targets;
* zero repeated target deadlines and zero deadline collisions;
* exactly twenty-one missing rank-eight targets;
* one immutable jump row, starting at `6481`, whose cumulative ranks are
  `4,6,7,9` and whose rank-nine crossing is `0x9e65` at `6484`.

The remaining starts form the exact mutable frontier

```text
lead:   0..3                 (4)
middle: 6431..6442          (12)
tail:   12866..12872         (7)
                               --
                               23.
```

Therefore any universal assignment of the free cells must make exactly
twenty-one of these starts deliver the twenty-one missing middle targets and
must leave exactly two mutable failures.  The current three-hole incumbent
has twenty successes and failures at `6434,12871,12872`; its sole missing
middle target is `0x18e7`.

### Endpoint-rook prune

The twenty-one rank-eight target rows each have seventy maximal providers.
Their representative left endpoints form exactly the twenty-three mutable
starts above.  Their representative right endpoints form the twenty-three
positions

```text
0..6, 6434..6444, 12868..12872.
```

Two distinct rank-eight targets cannot use representative intervals with a
common left endpoint: the intervals are nested, while two distinct nested
sets cannot have equal rank.  The same argument applies to a common right
endpoint.  Thus every completion selects twenty-one nonattacking rooks on
this `23 x 23` endpoint board and omits exactly two left and two right
endpoints.

### Singleton-run prune

Every interval realizing `0x8000` lies wholly inside one free block, and each
cell of that interval equals `0x8000`.  If its length is `ell>=2`, the `ell`
starts inside it have identical suffix-OR evolution after the run.  A
rank-eight delivery would therefore repeat one target at one deadline, which
is forbidden by `G=0`; all `ell` starts must fail.  Since only two mutable
failures are available,

```text
length(Q_0x8000) <= 2.
```

At length two this run consumes both failures.  Moreover, every provider for
a target not containing bit `0x8000` is disjoint from this run.

These are sound branch-and-bound rules, not heuristics.

## 3. Exact distinguished-hole root atlas

For every choice of one maximal provider for each hole, the integral
maximal-core equations were evaluated.  For each compatible root, every
literal incumbent host of each of the sixty-seven formerly covered residual
targets was then tested one target at a time.

The complete census is:

```text
raw roots                         343000 = 70^3
compatible roots                 179874
minimum direct displacement           5
minimum-displacement roots             5
distinct displaced sets                3
```

The complete displacement histogram is retained in the audit JSON.  Two
structurally separate implementations agree on every histogram entry:

* optimized C++: `1.5` seconds locally;
* independent Python: full `70^3` replay on one H100 CPU core.

All five sharp roots use file-order provider index `3` for `0x3de7` and `20`
for `0x9e20`.  Their physical meanings are

```text
0x3de7 -> Q=0x0000f, witness 2464, fixed OR 0x3104;
0x9e20 -> Q=0x00060, witness 4307, fixed OR 0.
```

The `0x18e7` file-order provider indices are `62,65,66,68,69`.  The exact
equality-cascade survivors are only `68,69`, namely

```text
Q=0x30000, witness 673;
Q=0x20000, witness 674.
```

The index convention above is **per-target file order**, not sorted-`Q`
order.

## 4. Sharp retained-core cascade

At a sharp root, five formerly covered targets have no surviving incumbent
host.  Relax those five and require every other formerly covered target to
retain one of its literal incumbent hosts.

There are seven multiply hosted targets; the exact retained-host choice
product is small.  Across the five sharp roots:

```text
retained-host choices at direct equality       480
compatible retained bases                        0
```

Relaxing any one additional retained target still gives zero compatible
base.  Relaxing any two additional retained targets also gives zero.

At three additional relaxations, exactly two faces survive: the physical
roots `Q(0x18e7)=0x30000` and `0x20000`, and in both cases the extra relaxed
set is forced to be

```text
{0x18e6, 0x19e6, 0x8000}.
```

Each root has exactly eight compatible retained-incumbent bases.  The eight
targets that would have to be rehosted are therefore

```text
{0x1e20,0x1e64,0x1e74,0x39e6,0x9c63,
 0x18e6,0x19e6,0x8000}.
```

This proves a sharp-root retained-core floor of eight rehosted rows before
their new providers are selected.

## 5. The sharp branch is empty through rehost budget ten

For each of the two physical roots and each of its eight retained bases, all
seventy maximal providers of each of the eight relaxed targets were tested.

The result is stronger than a failed joint DFS: on every one of the sixteen
bases, **each of the eight relaxed targets already has zero provider domain
individually**.  Adding other relaxed providers can only intersect coordinate
caps and add demands, so no later choice can repair this.

Hence the exact sharp rehost-eight face is empty.

Next relax one of the remaining fifty-nine retained targets.  Both physical
roots and all fifty-nine choices were checked.  In all `118` faces, every one
of the original eight rehost targets still has zero individually addable
provider.  Therefore total rehost budget nine is empty as well.

For two additional retained relaxations, all

```text
2 * binom(59,2) = 3422
```

faces were checked.  Exactly one face gives every relaxed target a nonempty
individual domain:

```text
Q(0x18e7)=0x20000;
extra relaxed pair = {0x9b54,0x9b56}.
```

The ten individual domain sizes are

```text
1,1,2,1,1,1,1,1,3,4,
```

so there are only twenty-four naive joint choices.  Exhaustive maximal-core
replay of those choices gives zero joint completions.  Thus the exact sharp
rehost-ten face is also empty.

Within the five minimum-displacement hole roots, at least eleven formerly
covered rows must therefore be rehosted.

## 6. All low-displacement roots cascade

The same retained-incumbent audit was then run on every compatible root of
direct displacement six through ten.

```text
direct displacement 6:   51 roots
direct displacement 7:  157 roots
direct displacement 8:  375 roots
direct displacement 9:  708 roots
direct displacement 10: 1264 roots
```

At direct equality, none of these `2555` roots has even one compatible
retained-incumbent base.

For the fifty-one displacement-six roots, every possible one-extra retained
relaxation was also tested.  Only four roots acquire a retained base, and in
all four the extra target is forced to be `0x8000`.  Each has thirty-two
retained bases, but on every base all seven relaxed targets have zero
individually addable provider.  Thus every displacement-six root needs at
least eight rehosted rows.

Consequently:

```text
d=5 roots:  total rehost floor >= 11;
d=6 roots:  total rehost floor >= 8;
d=7 roots:  total rehost floor >= 8;
d=8 roots:  total rehost floor >= 9;
d=9 roots:  total rehost floor >= 10;
d=10 roots: total rehost floor >= 11;
d>=11:      direct displacement alone >= 11.
```

Therefore **every completion anywhere in the full frozen seed5/self fibre
must rehost at least eight formerly covered residual targets.**  This is a
global statement about the frozen fibre, unlike the sharper budget-eleven
statement for the five minimum-displacement roots.

## 7. Scope and current decision state

Proved here:

1. the zero-ghost `23 -> 21` mutable middle frontier;
2. the `21`-rook endpoint condition;
3. the singleton `0x8000` length-two prune;
4. the full `70^3` distinguished-hole root census;
5. direct displacement minimum five;
6. the sharp retained-core forced triple;
7. emptiness of the exact sharp rehost-eight and rehost-nine faces;
8. the unique individually live rehost-ten pair face and its joint no-go;
9. direct-equality emptiness for all displacement-six through ten roots;
10. the global frozen-fibre rehost floor eight.

Not proved here:

* UNSAT of all `179874` compatible roots;
* SAT of any nonsharp root;
* impossibility of a different parent/opening or collar layout;
* `nu(16)=12874`.

The global bracket remains

```text
12873 <= nu(16) <= 12874.
```

## 8. Artifacts

```text
scratch/audit_k16_rf495_fixed_deadline_frontier_20260730.py
scratch/k16_triwindow_rf495_repeatfree_frozen_atlas_20260730/
  fixed_deadline_frontier.independent.audit.json

scratch/audit_k16_rf495_distinguished_hole_root_atlas_20260730.cpp
scratch/audit_k16_rf495_distinguished_hole_root_atlas_20260730.py
scratch/k16_triwindow_rf495_repeatfree_frozen_atlas_20260730/
  distinguished_hole_root_atlas.cpp.audit.json
  distinguished_hole_root_atlas.independent.audit.json
  distinguished_hole_root_atlas.sharp.tsv

scratch/search_k16_rf495_sharp8_exact_20260730.cpp
scratch/audit_k16_rf495_sharp8_nogo_20260730.py
scratch/k16_triwindow_rf495_repeatfree_frozen_atlas_20260730/
  sharp8_nogo.independent.audit.json
  sharp_pair_blocker.cpp.audit.json
  sharp_pair_blocker.candidates.tsv
```

The displacement-six/seven and displacement-eight/ten ranking audits are
produced by modes `low67-audit` and `low10-audit` of
`scratch/search_k16_rf495_sharp8_exact_20260730.cpp`; their H100 reports and
rankings are retained under
`/home/amodo/or15/work/root_rf495_low67_repairability_20260730/`.

### Solver-ready global rehost cut

The global floor in Section 6 is also frozen as an exact strengthening of the
original 18-cell DIMACS model:

```text
scratch/build_k16_rf495_rehost8_cut_20260730.py
scratch/audit_k16_rf495_rehost8_cut_20260730.py
scratch/k16_triwindow_rf495_rehost8_cut_20260730/
  model.rehost8.cnf
  rehost8.map.json
  rehost8.manifest.json
  rehost8.independent.audit.json
```

There are sixty-seven rehost selectors, one for each **formerly covered**
residual target.  The three incumbent holes

```text
0x18e7, 0x3de7, 0x9e20
```

are excluded from the count.  For a target with incumbent physical witness
variables `w_1,...,w_s`, including the six double-hosted and one triple-hosted
targets, the selector has the exact semantics

```text
r_t <=> not(w_1 or ... or w_s).
```

An exact Tseitin dynamic counter enforces `sum_t r_t >= 8`.  The strengthening
adds `679` variables and `2363` clauses, producing `7048` variables and
`207920` clauses.  The independent auditor remaps all seventy-five physical
incumbent rows to exact `(target,shape)` witness variables, verifies the
unchanged base-CNF prefix and every appended clause, exhaustively truth-tables
the selector semantics for multiplicities one, two, and three, truth-tables
the counter recurrence, and calibrates the threshold on all `2^12` input
patterns.

This cut is sound only in the frozen repeat-free seed5/self `4/9/5` fibre.  It
does not constrain a different parent, opening, braid, or collar layout.
