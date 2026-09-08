# Exact r99 branch decomposition for the recentered k16 motif family

Date: 2026-07-29

## Frozen data and scope

Let `F` be the 858-orbit factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json` (SHA-256
`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`).
Its 147 positive short-run motifs have 390 distinct source edges and split,
by edge overlap, into 85 components.  The ordinary component transversal
ranks sum to 97.  In the full-motif boundary atlas, upper colour `(1,1907)`
has selected provider 22511 and no replacement provider.  Forbidding 22511
raises only component 5, on motif IDs 5 and 66, from rank one to rank two:

```text
M5  = {22511,22520}
M66 = {22511,22692,25634}.
```

The safe ranks therefore sum to 98.  This note classifies deletion banks of
size 99.  It does not assert feasibility of the degree, insertion, q1,
dynamic-top, connectivity, or voltage ledgers.

## The minimum-option-plus-extra claim is false

Component 10 already gives a literal counterexample:

```text
M10 = {185,311,2169}
M18 = {2169,5603,9704}.
```

Its unique minimum transversal is `{2169}`, but `{185,5603}` is an
inclusion-minimal transversal of size two.  Thus a size-99 global hitting set
can use `{185,5603}` in this component and minimum transversals elsewhere;
it contains no global minimum-product cut bank.  The same obstruction works
in both the retain-22511 and cut-22511 branches.

Exhaustive componentwise enumeration gives the sharper ledger:

| branch/local level | states | states containing no level-0 option |
|---|---:|---:|
| retain 22511, level 0 | 262 | 0 |
| retain 22511, level 1 | 958 | 304 |
| cut 22511, level 0 | 261 | 0 |
| cut 22511, level 1 | 960 | 304 |
| cut 22511, level 2 | 3442 | 2207 |

The 304 level-one failures occur in 33 of the 85 components.  Hence a model
that selects a minimum local option and then toggles one or two additional
edges is incomplete.

## Exact graded theorem

For an overlap component `C`, let `U_C` be its motif-edge union.  The sets
`U_C` are pairwise disjoint.

### Retain branch

Delete 22511 from `U_5`, and let `r_C^+` be the resulting local transversal
rank.  Then `sum_C r_C^+=98`.  A 99-edge source deletion bank `D` which hits
all motifs and retains 22511 is characterized uniquely by

```text
D = D_out disjoint-union (disjoint-union_C D_C),
```

where `D_out` lies among the 468 source edges outside the motif union,
every `D_C` is a local hitting set of size `r_C^+` or `r_C^++1`, and

```text
|D_out| + sum_C (|D_C|-r_C^+) = 1.
```

Thus an exact multiple-choice model needs the 262 level-zero and 958
level-one local states, one state per component, together with 468 raw
outside-cut bits and the displayed excess equation.  It has 1220 local
state variables.

### Cut branch

Let `r_C` be the ordinary ranks, whose sum is 97, and require the component-5
state to contain 22511.  A 99-edge motif-hitting bank which cuts 22511 is
characterized uniquely by local states of sizes `r_C`, `r_C+1`, or `r_C+2`,
468 raw outside-cut bits, and

```text
|D_out| + sum_C (|D_C|-r_C) = 2.
```

There are respectively 261, 960, and 3442 local states, hence 4663 local
state variables.  The equation permits either one level-two component, two
level-one components, one local excess plus one outside cut, or two outside
cuts, with no missing case.

The proof in both branches is just additivity over the pairwise disjoint
`U_C`: each restriction must have at least its local rank, and the total
excess is one or two.  Conversely every state tuple satisfying the excess
equation hits all 147 motifs and has exactly 99 cuts.  Uniqueness follows
from disjointness of the component edge unions.

## Recommended exact model

The simplest complete r99 model uses raw deletion bits for all 858 source
edges, rather than the graded states:

1. `sum d_e=99` and all 147 motif-hit rows;
2. branch row `d_22511=0` or `d_22511=1`;
3. 26,570 off-source loopless addition bits and `sum a_f=99`;
4. exact incidence balance at all 858 quotient vertices;
5. all 764 lower and 764 upper q1 rows;
6. dynamic top boundary/reach rows and literal positive/complemented-top
   residence CEGAR;
7. no AddCircuit initially; components and voltages are post-audited.

There are 27,428 loopless catalogue edges, with sector census
`11998 AA + 3432 AB + 11998 BB`; consequently the top formulation has
47,992 reach variables.  Before lazy rows, each raw branch has 76,278
variables and 52,244 constraints under the stated direct encoding.  The
graded retain/cut alternatives have roughly 77,108/80,551 variables before
any shared CP-SAT constant variable, so their stronger deletion-side
propagation does not reduce the raw variable count.  The raw 858-bit model
is therefore the preferred primary encoding; the graded products are exact
cross-checks or branching oracles.

