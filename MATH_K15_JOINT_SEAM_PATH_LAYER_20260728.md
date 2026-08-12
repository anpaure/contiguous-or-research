# k=15: joint seam/cut path-cover layer

## 1. Why the old opening audit was too strong

`scratch/audit_k15_phasefactor_safe_openings.py` chooses one cut in every
factor component and deletes all cyclic windows crossing those cuts.  It then
requires the deleted windows to be redundant **before** any new seam is
installed.  The q2 phase factor has three components for which this fails.
That is not a no-go: a seam contributes one new upper-q1 window, two new
upper-q2 windows, and three new upper-q3 windows, and those new windows may
repay losses at other cuts.

The correct object is therefore a simultaneous cut-and-seam selection.

## 2. Exact physical catalogue

Let `F` be

```
scratch/k15_phasequotient_upperq2_orbit.factor.json
```

on the 5295 middle vertices formerly carried by physical cycles 1 and 12.
Let `P` be their exact old lower-q1 palette.  The joint catalogue consists of

1. the 5295 native edges of `F`; and
2. every Johnson edge joining different `F`-components whose intersection is
   in `P`.

The second family has 49,200 edges, so the full catalogue has 54,495 edges.
The component incidence graph is connected and every physical vertex has a
cross-component seam.

For every catalogue edge `e` introduce a selection literal `x_e`, and for
every lower colour `L in P` a miss literal `z_L`.  Impose

```
sum_{e: lower(e)=L} x_e + z_L = 1                       (2.1)
1 <= sum_{e incident with v} x_e <= 2                  (2.2)
```

and, optionally, `sum_L z_L <= p`.  If `h=sum z_L`, then (2.1) selects
exactly `5295-h` edges.  Equation (2.2) consequently forces exactly `2h`
degree-one vertices.  Once cyclic components are excluded, the selected
graph is therefore a path cover with **exactly h paths**.  Thus every retained
path costs exactly one lower colour; no separate seam-cost heuristic is used.

The implementation is

```
scratch/search_k15_joint_seam_path.py
```

## 3. Exact upper-shadow and residence constraints

The untouched physical cycles are counted first.  Only upper targets absent
from that outside load constrain the replacement:

| depth | critical physical targets |
|---:|---:|
| 1 | 3960 |
| 2 | 2118 |
| 3 | 855 |

Upper q1 is encoded eagerly by edge clauses.  For q2, a witness is a selected
two-edge wedge.  For q3, a witness is a selected simple three-edge path.  A
missing target adds the disjunction of all its witness conjunctions.  These
clauses account for destroyed cut windows and new seam windows jointly.

Depth-three residence is also local.  Every internal coordinate run of length
at most three gives a selected edge motif of size at most four; the motif is
forbidden.  Cyclic components are eliminated lazily by clauses requiring at
least one presently selected cycle edge to be dropped.  For `p=1`, ordinary
subtour cuts instead yield one Hamilton path.

All final claims are re-audited directly from the materialized paths.  The SAT
encoding is only a search accelerator, not the verifier.

## 4. Two useful implementation facts

First, represent native selection by a negative literal and seam selection by
a positive literal.  With Kissat's false initial phase, the known factor is
the starting assignment.  This changed the first solve from minutes to 0.4 s.

Second, connectedness is not required by the compiler.  With no path-count
cap, cutting all base cycles while preserving exact upper q1 produced in 6.3 s
an acyclic cover with 1002 paths.  It had 464 upper-q2 holes, 183 upper-q3
holes, and 579 remaining residence motifs.  Adding the base factor's 15 q3
holes and 1455 native residence clauses produced in 14.8 s an acyclic cover
with 1104 paths, 527 q2 holes, 204 q3 holes, and 467 remaining residence
motifs.

The counts 1002 and 1104 are both below the numerical k=15 slack 1119.  This
does **not** yet prove compiler feasibility: the omitted lower colours still
need the exact Hall audit.  It does show that simultaneous seam/cut routing is
at the correct finite scale, whereas the one-cut-per-component opening audit
was testing the wrong polytope.

## 5. Current exact run

The next lazy round enforces all observed defects simultaneously.  Three
independent exact lazy runs contracted as follows (tuple order is
`paths, q2 holes, q3 holes, residence motifs`):

```
max-1119:       (1016,488,166,520) -> (916,363,114,630)
unbounded:      (1104,527,204,467) -> (962,334,120,554)
                                      -> (867,256, 89,627)
cycles-first:   (1002,464,183,579) -> (962,377,125,573)
                                      -> (872,260, 76,683)
```

The non-monotonic residence count is expected: each round forbids every
currently visible short-run motif, but a new selected path cover exposes new
motifs.  Shadow holes and paths contract strongly.

A 28-model CPU portfolio on two once-strengthened CNFs gave the following
global Pareto representatives:

| branch/model | paths | q2 | q3 | residence | seams |
|---|---:|---:|---:|---:|---:|
| balanced/default_1191900 | 928 | 323 | 119 | 547 | 1851 |
| minpath/default_1192204 | **842** | 343 | 111 | 625 | 2089 |
| balanced/default_1191901 | 917 | 333 | 110 | 577 | 2137 |
| balanced/walk_1191920 | 942 | 341 | **100** | 570 | 2082 |
| balanced/default_1191902 | 969 | 373 | 128 | **530** | 2186 |

The first row minimizes total observed defect (1917) and is the sole branch
continued.  Portfolio strengthening must be cumulative: rebuilding from only
the newest model forgets previously learned lazy clauses.  The implementation
therefore accepts repeatable `--replay-paths` inputs and reconstructs all
earlier cycle, residence, q2, and q3 clauses from their materialized audits.
The cumulative round-2 CNF has 7,227,634 variables and 27,352,088 clauses.

The live success criterion is an acyclic path cover with:

* zero upper holes at q=1,2,3;
* zero depth-three residence motifs; and
* at most 1119 paths, followed by the independent lower compiler/Hall check.

No GPU is used.  Heavy SAT runs are on the CPU of the remote `h100` host.

## 6. Exact-shadow seed and whole-carrier scope

The stronger factor

```
scratch/cf15_combined_r2_23014.factor.json
```

has 25 components on physical cycles 1 and 12 and is cyclically hole-free at
upper q1, q2, and q3.  Its SHA-256 is
`39595058a7cc447453b89de67349ad8f15a8143977a18998143db0a81461deb5`.
It leaves 1,260 residence motifs on the replacement, but physical cycle 14
contributes another 15.  A replacement-only model can therefore never certify
whole-carrier residence zero.

The exact model now supports repeatable `--extra-cycle` arguments.  With
`--extra-cycle 14`, the original 45-cycle is appended as an editable native
component, its lower palette is incorporated exactly, and its contribution is
removed from the outside shadow load.  The correct whole-carrier base has

```
p cnf 1467273 4623935
sha256 e30a17b14b2802a67a1b04146cd3e426ab67d95ddbfd63ee9c89006265444911
```

and starts with 26 cycle-break clauses, all 1,275 known residence clauses,
and zero base upper holes at q1--q3.

The first 16-way CPU portfolio produced eight SAT models before the remaining
siblings were stopped.  The important frontier was:

| model | paths | q2 | q3 | residence | seams |
|---|---:|---:|---:|---:|---:|
| forcefalse_230163 | 672 | 271 | 118 | 593 | 1090 |
| forcefalse_230162 | **638** | **267** | 94 | 671 | 1127 |
| false_230157 | **501** | 270 | **89** | 834 | 1456 |
| forcefalse_230165 | 833 | 393 | 122 | **549** | 1378 |

The total-best and residence-best rows are continued as separate cumulative
branches, because shadow defects and residence expose a real tradeoff.  Their
first strengthened CNFs are respectively

```
A: p cnf 10944933 42185706
   sha256 b587feac07dec9388d445a9c21e8fa9b202ee5857ce78eabc48121852ec3be71
B: p cnf 11447587 44055731
   sha256 3db9ed717e7f8cdede14afba6ea2b8331df8d7fd2a3a7e20ba5828765179a2c0
```

Each branch has eight diversified CPU solvers (default, false phase, initial
walk, and forced-false phase).  The obsolete q2-only seed runs were stopped
after their artifacts were preserved.

## 7. Scope correction: a carrier must be fully linear

A certificate that replaces cycles 1 and 12 (and even cycle 14) but leaves
the other fourteen physical cycles cyclic is **not** yet a compiler carrier.
The first h8-seed joint run found a beautiful 17-path replacement with
residence zero and upper q1--q7 exact, but those paths contained only 5,340
vertices; 1,095 vertices remained implicit in fourteen cycles.  That object
is preserved as a partial certificate, not reported as a k=15 completion.

The implementation now accepts every untouched source cycle through repeated
`--extra-cycle` arguments.  The true full-carrier run makes all 22 base cycles
editable:

```
factor replacement cycles: 7
original cycles made extra: 0,2,3,4,5,6,7,8,9,10,11,13,14,15,16
middle vertices in selected paths: 6435
```

Its h8 factor `scratch/k15_uniform444_h8_exact.factor.json` is independently
exact in both lower and upper shadows q1--q7; replacement residence is zero
and only physical cycle 14 contributes fifteen initial motifs.  Pure cutting
(one cut in every residence-free cycle and eight in cycle 14) is exactly
UNSAT while preserving q1--q7, so cross-component seams are essential.

The full joint base has

```
p cnf 1226748 3673991
sha256 112f9da68f0284a40720606afad11f3bd8c9078665184468f0d14dd9ab763b47
```

and its first two cumulative portfolios contracted the genuine whole-carrier
frontier as follows:

| round/model | paths = lower holes | q2 | q3 | q4--q7 | residence |
|---|---:|---:|---:|---:|---:|
| r0 forcefalse_808243 | 48 | 4 | 2 | 0 | 54 |
| r1 default_809233 | 46 | 1 | 1 | 0 | 38 |
| r2 default_810231 | 60 | 2 | **0** | 0 | **32** |
| r2 forcefalse_810242 | **43** | **1** | 2 | 0 | 44 |
| r2 forcefalse_810244 | **43** | 3 | 2 | 0 | 37 |

Every row above was independently decoded over all 6,435 vertices and audited
through q7.  No final metric-zero row exists yet.  The next cumulative round
uses the q3-zero r2 model as polarity but replays the **union** of all q2/q3
targets and residence motifs exposed by all sixteen r2 SAT models, preventing
simple cycling among sibling defect sets.

## 8. Union strengthening and the connected-carrier lane

The sixteen-model union round is now materialized on the remote CPU host as

```
/dev/shm/k15_joint/strength_h8_fullcarrier_r3_union16.cnf
p cnf 22046912 85645240
sha256 a4707f292fa8281d5ea18c669b0b929f58610699d5f0056cff4b412590f7cf65
```

It contains the union of 1,513 q2 witnesses, 471 q3 witnesses, 5,141
residence cuts, and 26 cycle-break cuts from the bootstrap, r0, r1, and all
sixteen r2 audited path covers.  Four diversified Kissat runs are active on
this 1.9 GB instance.  Each uses about 4.34 GiB RSS; all are CPU-only.

There is also a cleaner compiler-compatible lane that enforces a **single
path** directly rather than first finding a path cover and subsequently
ordering its components.  Its verified base is

```
/dev/shm/k15_joint/k15_joint_h8_fullcarrier_onepath.cnf
p cnf 494144 1463310
sha256 576711ee36899fc4b0ed2357491fc58f928fd7197f5150dcd382b23dba0854b
```

Eight diversified CPU-only Kissat runs are active.  A SAT model here would
already solve the global ordering/connectivity interface; it would still be
decoded and audited over all 6,435 vertices through q7 before being called a
certificate.  No SAT result has been returned yet.

The first union-r3 SAT model, `false_823002`, has now been independently
decoded over all 6,435 vertices.  It is the closest genuine full-carrier seed
so far:

```
paths = lower holes = 33
cycles = 0
upper holes q1,...,q7 = 0,0,0,0,0,0,0
depth-three residence motifs = 13
selected native edges / seams = 6385 / 17
```

Its local preserved audit is
`scratch/k15_h8_fullcarrier_frontier/union16_false_823002.audit.paths.json`
with SHA-256
`5a369a2c8f315793c414d93c729e0d927bd41594ff21939bc597728ed087e6fd`.
This is not yet a certificate: the thirteen residence motifs remain, and the
33 paths still require an exact compiler-compatible ordering (or further
joint merging).  The r4 cumulative instance replays this model on top of the
sixteen-model union, so it adds exactly those thirteen new residence clauses
and no new q2/q3 witness clauses.

An intermediate direct lane enforces at most eight paths.  Its verified base
is

```
p cnf 539154 1553323
sha256 e35ad93b1956ee7ab32cf78e9f02fa87c94e4227df7fb8594fe5272abf2d2d86
```

One iterative driver and seven diversified direct Kissat runs are active.
Unlike the 33-path seed, a residence-safe SAT result here can be passed to the
exact path-ordering program at genuinely small size.  Two CaDiCaL lanes were
also added to the strict one-path base for solver diversity.  Every run in
these lanes is CPU-only.

The generic strict-one-path and eight-path bases did not resolve: eight
Kissat plus two CaDiCaL one-path runs, and eight Kissat eight-path runs, all
reached their time limits with `UNKNOWN` (not `UNSAT`).  The global r4 system
was staged append-only from r3, using the stable raw-edge variable catalogue:

```
p cnf 22046912 85645253
sha256 20b50a36121a265bdff8c35fe0b950f01db76d861c4053d72018767e9ee6853e
```

The thirteen appended clauses were checked directly against the parent SAT
assignment: all thirteen are violated by `false_823002`, as required.  Three
new r4 SAT models nevertheless moved far away from that near solution, with
roughly 920--950 paths, 107--120 q2 holes, 27--34 q3 holes, and 636--661
residence motifs.  Thus the remaining lane must preserve locality around the
33-path/13-motif seed; globally adding its clauses is not enough.

Two small utilities now make subsequent rounds cheap and independently
checkable:

* `scratch/append_k15_residence_cuts.py` derives raw-edge residence clauses
  and appends them to a stable CNF without regenerating tens of millions of
  unchanged clauses;
* `scratch/audit_k15_joint_model_fast.py` independently reconstructs the edge
  catalogue and audits a model through q7 without rebuilding the lazy CNF.

Both were bytecode-compiled before use.  The fast audit reproduces every
metric and component size of the earlier full reconstruction of
`false_823002`.
