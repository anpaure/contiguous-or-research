# Exact contiguous-OR formula: systematized understanding after k=15 carrier closure

Date: 2026-07-28

This note distills the proved lower bound, the exact certificates through
`k=14`, the full `k=15` search history, and the finite negative audits into a
single working model.  Its purpose is not to retell the search chronologically.
It separates what is forced, what is a chosen normal form, what the exact
certificates actually teach, and which next searches are mathematically
distinct rather than renamed versions of exhausted neighborhoods.

## 1. Problem and current theorem frontier

For a nonzero set word `A=(A_1,...,A_L)` on `[k]`, let `nu(k)` be the least
length for which every nonempty subset of `[k]` occurs as the union of a
contiguous interval.  Put

```text
r = ceil(k/2),
W = binom(k,r),
Lambda = sum_{j=1}^{r-1} binom(k,j),
d(k) = min {d : d W + binom(d+1,2) >= Lambda},
B(k) = W + d(k).
```

The monotone-deadline theorem proves unconditionally

```text
nu(k) >= B(k).
```

Machine-checkable words meet the bound for every `k<=14`.  Hence

```text
nu(k)=B(k) for 0<=k<=14.
```

For `k=15`, `r=8`, `W=6435`, `d=3`, `Lambda=16383`, and `B(15)=6438`.
No length-6438 word has yet passed the full verifier.

## 2. What the lower bound really forces

For column `i` in the triangular OR array, let `f_i` be the number of initial
cells below rank `r`, and set the deadline `F_i=i+f_i`.  Monotonicity of the
OR array gives `F_{i+1}>=F_i`; distinct middle-layer witnesses have distinct
deadlines.  If `L=W+e`, this implies

```text
f_i <= min(e,L-i+1),
Lambda <= sum_i f_i <= eW + binom(e+1,2).
```

At equality length `L=W+d`, define

```text
sigma = dW + binom(d+1,2) - Lambda.
```

There is an exact loss identity

```text
sigma = Delta_depth + Delta_repeat,
```

where `Delta_depth` is unused deadline capacity and `Delta_repeat` counts
repeated lower-cell occurrences.  This is all the scalar proof forces.

Consequences that are rigorous:

- if `sigma=0` (notably `k=6,9`), the flat middle row and bijective lower band
  are forced;
- for positive `sigma`, only the total two-loss budget is forced.

Consequences that are **not** forced when `sigma>0`:

- a flat middle derivative;
- rank-by-rank grading;
- a Johnson path or cycle;
- a unique boundary flag;
- minimum residence;
- shadow simplicity.

Those are construction properties of the successful normal form, not
corollaries of the lower bound.  This distinction prevents empirical beauty
from being mistaken for a theorem.

For the three relevant positive-slack odd cases:

| k | W | d | Lambda | sigma | sigma/Lambda |
|---:|---:|---:|---:|---:|---:|
| 11 | 462 | 3 | 1023 | 369 | 0.361 |
| 13 | 1716 | 3 | 4095 | 1059 | 0.259 |
| 15 | 6435 | 3 | 16383 | 2928 | 0.179 |

Absolute slack grows, but relative slack shrinks.  This is consistent with
the compiler becoming more selective at `k=15` despite having more raw cells.

## 3. The exact carrier/compiler normal form

The successful constructions choose a rank-`r` chronology

```text
T=(T_0,...,T_{W-1})
```

enumerating the complete middle layer and seek `A` with `D^d A=T`, where
`D` takes adjacent unions.  This factorization exists exactly when every
internal coordinate run in `T` has length at least `d+1`.  The maximal
erosion envelope then supplies all legal physical positions for the lower
compiler.

The construction decomposes into four exact gates:

1. middle permutation / Johnson chronology;
2. depth-`d` residence;
3. every upper shadow `D^q T` is covered;
4. the lower sandwich graph has a matching saturating every lower target.

Gate 4 is not an implementation detail.  For a fixed carrier and hitting
core it is exactly Hall/PCSH.  Missing shadows give zero-candidate targets,
but even after every target has a candidate, competition for named cells may
still cause deficiency.  Therefore neither a scalar hole count nor a
fractional capacity check substitutes for the exact matching.

## 4. Forced path-cover palette algebra

Suppose the middle layer is partitioned into `p` Johnson paths.  Let `R` be
the number of repeated rank-`r-1` edge-colour occurrences and `H` the number
of missing rank-`r-1` colours.  There are `W-p` selected internal edges and
`W` possible colours, so identically

```text
H = p + R.                                      (4.1)
```

This one identity explains the k=15 carrier breakthrough.

- a missing-colour join changes `(p,R,H)` to `(p-1,R,H-1)`;
- a used-colour join changes it to `(p-1,R+1,H)`.

For a depth-three one-path compiler there are two exceptional outer cells.
Thus terminal `H<=2` is necessary, equivalently `R<=1`.  Palette simplicity
was therefore stronger than necessary.  The exact successful seam pattern

```text
missing -> used -> missing
```

gives

```text
(4,0,4) -> (3,0,3) -> (2,1,3) -> (1,1,2).
```

This is a reusable bounded-repeat bridge, not a lucky numerical accident.

## 5. What the exact certificates teach

### k=11

- one cyclic-equivariant carrier;
- residence minimum exactly the required four;
- all shadows complete;
- one safe cut and a nested endpoint flag;
- Hall passes;
- upper-q1 load is the integrality-floor profile `1^198 2^132`.

The lesson is compatibility of residence, complete shadows, boundary, and
Hall—not that upper simplicity is logically necessary.

### k=13

- the exact resident, all-shadow carrier was a two-cycle factor, not a
  Hamilton cycle;
- exhaustive cut-and-join checked 24,960 splices; 1,092 preserved both all
  upper shadows and exact depth-three residence;
- the chosen seam lost one lower-q1 colour and Hall still passed;
- upper-q1 had 78 triple loads, proving CPCR/simple-design behavior is useful
  guidance but not necessary.

The decisive correction was: connectivity inside the hard core was stronger
than the compiler required.  Construct the exact small-component factor first,
then spend the boundary capacity on a safe splice.

### k=14

- the odd-to-even lift needed a six-piece braid;
- every five-piece braid failed for a structural reason: extracting the
  required length-three run deleted two unique upper colours but exposed only
  one repairing endpoint;
- the second cut supplied the second endpoint, and 35/100 calibrated carriers
  then worked.

The lesson is that a higher-order simultaneous splice can be qualitatively
different from every smaller local move.  Exhausting 2/3/4-opt does not make
the next order implausible when the missing resource count itself is four or
more.

### k=15

The exact replayable carrier chain is:

| paths | q1 repeats/holes | q2/q3 holes | invariant status |
|---:|---:|---:|---|
| 4 | 0/4 | 21/5 | residence 0, all upper exact |
| 3 | 0/3 | 21/5 | residence 0, all upper exact |
| 2 | 1/3 | 24/5 | residence 0, all upper exact |
| 1 | 1/2 | 28/5 | residence 0, all upper exact |

Across 99 endpoint rotations, 92 were palette-neutral and only seven changed
one colour.  Thus exact invariant-preserving endpoint routing is abundant;
the used-colour bridge, not generic randomness, crossed the component barrier.

The first clean p1 is

```text
scratch/k15_targetpalette_p1_q28.json
SHA-256 ba96c6f81098ed73f09f861d9e55283d9374e3426604e05eab0e0c2cd5dabffe
```

It closes middle ownership, connectivity, residence, every upper shadow, and
the clean q1 palette.  Its initial lower Hall deficiency was 41 because its
two missing q1 faces were not contained in the two endpoints and seven
rank-six roots had no candidate.  Exact Hall descent subsequently produced

```text
clean q1 (R,H)=(1,2): Hall 31, q2/q3=22/5, outer score one;
bridge q1 (R,H)=(3,4): Hall 30, q2/q3=21/5, both outer faces paid.
```

The authoritative artifacts are

```text
scratch/k15_terminal_palette_h31_outer1.json
SHA-256 b8f688867544cc62cdc86d1d6f2550bcd83e283f24cd6bfede3c2d639ab6219f

scratch/k15_outer2_p1_h30_bridge.json
SHA-256 6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
```

The clean Hall-31 path has seven rank-six zero candidates and one rank-seven
zero.  The Hall-30 bridge has five rank-six zeros and two rank-seven zeros.
Both remain strictly deficient, so neither is a certificate.

The old scalar-Hall lane reached deficiency 33 at palette `(R,H)=(4,5)`;
the current bridge lane reaches 30 at `(3,4)`.  These are not ruled out as
final compiler inputs: the exact sandwich Hall graph, not the number of q1
repeats, is authoritative.  The clean `(1,2)` palette is a particularly
transparent sufficient normal form, not a theorem about every optimum word.
The remaining problem is therefore a coupling problem, not any one of the
gates in isolation.

## 6. Hall anatomy at k=15

For a depth-three p1 carrier:

- row-2/rank-7 envelopes are the q1 lower colours;
- row-1/rank-6 envelopes are the q2 lower colours;
- row-0/rank-5 envelopes are the q3 lower colours;
- two exceptional outer cells can absorb at most two missing q1 faces.

Hence the clean sufficient target is

```text
outer endpoints pay the two q1 holes,
q2 holes = 0,
q3 holes = 0.
```

It is stronger than necessary, but it removes every known zero-candidate
root before cell competition is considered.

The empirical Hall descent is consistent with this anatomy:

```text
65 -> 64 -> 63 -> 62 -> 61 -> 59 -> 37 -> 36 -> 35 -> 34 -> 33.
```

The major drop `59 -> 37` came from transferring a low-q2 carrier, not from a
generic Hall-local move.  The persistent named rank-six masks, rather than
the total q2 count alone, predict which rotations matter.  Future scoring
must therefore retain:

```text
(terminal palette, outer-face assignment, named q2 roots, exact DM/Hall,
 q2 total, q3 total).
```

No projection of this tuple to one scalar has yet remained monotone.

The exact Dulmage--Mendelsohn witness of the Hall-30 carrier is much larger
than its seven zero-candidate masks:

```text
reachable targets A = 1,528
reachable cells N(A) = 1,498
|A|-|N(A)| = 30
rank histogram of A: 4:9, 5:82, 6:413, 7:1024
cell-depth histogram of N(A): 0:81, 1:395, 2:1022.
```

Thus "fill the seven zeros" is necessary but not a complete objective.  The
reusable exact certificate is

```text
scratch/audit_k15_hall_dm_witness.py
scratch/k15_outer2_p1_h30_bridge.dm_witness.json
```

For a component-order model this witness yields a Benders cut.  Compiler cell
slots partition into fixed internal slots, selected seam-crossing slots, and
the two selected endpoint collars.  Every Hall-zero chronology must satisfy

```text
|N_fixed(A)| + sum(selected seam/endpoint slots adjacent to A) >= |A|.
```

Iterating chronology SAT, exact Hall witness extraction, and this necessary
weighted cut is strictly stronger than blocking one failed chronology or
maximizing the number of named roots.

In the first terminal-palette Hall-37 path, all six rank-six zero-candidate
targets

```text
5397, 8869, 10794, 17738, 21588, 21672
```

are cyclic shifts of the single canonical mask `2709`.  The persistent defect
is therefore one broken `Z_15` orbit, not six unrelated local accidents.  This
suggests orbit-aware scoring and, more importantly, makes a rank-six mixed seam
a targeted resource rather than generic non-Johnson damage.

## 7. Exact local closures

The following neighborhoods are exhausted, not merely sampled:

- every strict internal 2-opt from Hall-33: no improvement;
- the palette-relevant internal 2-opt tree through depth four: state counts
  `320,203,80,0`, no Hall below 33 and no terminal palette repair;
- two independent repeats-3 p1 states: about 12.9 million sparse 3-opt triples
  each, no hole `4 -> 3` transition even before residence/upper checks;
- targeted separated 4-opt on the duplicate colours: no repeat `<=1` state;
- clean p3 one-cut/four-segment reconnections: no Johnson routing;
- clean p2 direct one-cut and targeted two-cut terminal splices: no valid route.
- root-conditioned fixed-endpoint 3-opt on both the clean Hall-37 and bridge
  Hall-31 carriers: about 0.75 million indexed reconnections per source; the
  clean source has one upper/residence-valid result but worsens Hall to 39,
  while the bridge source has none even at q1 repeat four.

These results close only those move classes.  They positively identify Posa
endpoint routing, higher-order simultaneous splices, and cross-seed component
trades as the nonredundant geometries.

## 8. The 89-component crossover theorem

The Hall-33 path and clean p1 share 6,348 of 6,434 edges.  Their union has
6,520 edges but only 6,433 q1 colours:

```text
6346 colours occur on one union edge,
87 colours occur on two union edges.
```

Any terminal palette `(R,H)=(1,2)` inside this union must select every
singleton-colour edge, at least one edge from every double-colour pair, and
both edges from exactly one pair.  The forced singleton graph has 89 path
components, so the whole crossover becomes an 89-node connector problem:
choose 88 of 174 connectors subject to vertex capacities, colour-pair quotas,
and connectivity.

The exact SAT/lazy-cut census is complete:

```text
134 connectivity cuts,
1 residence cut,
4 valid Hamilton selections,
then UNSAT.
```

All four have the same missing q1 faces, outer score zero, q2=28, and Hall
deficiencies 41 or 42.  Thus the clean carrier is essentially unique inside
the two-seed union; Hall 33 cannot be inherited by merely recombining their
existing edges.  This is a reusable normal form for future carrier crossover:
contract forced single-colour chains before invoking a global SAT model.

Artifacts:

```text
scratch/k15_union89_crossover.summary.json
scratch/search_k15_union_connector_sat.py
```

### Exact scope of the alternating-component heuristic

For spanning paths `P,Q`, retain their common edge set `K` and let the
connected components of `(E(P)\\E(Q)) union (E(Q)\\E(P))` be `C_i`.  Choosing
the red or blue edges independently on each `C_i` always gives a spanning
graph of maximum degree two, but it need not preserve the endpoint set or be
connected.  If

```text
delta_i = |endpoints(Q) intersect C_i| - |endpoints(P) intersect C_i|,
```

then a switch set `S` has exactly two endpoints only if
`sum_{i in S} delta_i=0`; even then a detached cycle may remain.  The familiar
"even alternating cycles" theorem is therefore applicable only when the two
named degree sequences agree vertex by vertex.

This was checked exactly on the three-component overlay between the Hall-30
bridge and the earlier outer-2 Hall-37 path.  Seven of eight hybrids are
Hamilton paths and have Hall deficiencies

```text
30, 31, 33, 33, 34, 35, 36;
```

the eighth has two endpoints but is disconnected.  All seven valid paths
retain residence zero and complete upper shadows.  Thus the cube is real and
useful, but Hall is visibly non-additive and this entire cube contains no
improvement below 30.  The frozen audit is

```text
scratch/audit_k15_open_overlay_hybrids.py
scratch/k15_h30_h37_c3_hybrids.json
```

Components obtained from different source pairs cannot be freely combined
merely because their changed edges are disjoint: they must be interpreted
relative to one common base, preserve endpoint balance, avoid detached
cycles, retain residence/upper conditions, and then pass exact Hall.  Hence
`edges changed / Hall unit` is not a distance estimate.  The correct reusable
objects are the contracted connector CSP and the component-order SAT,
followed by an exact Hall audit.

## 9. Corrections to repeatedly tempting but false intuitions

1. **Counting/entropy is not a no-go.**  Correlated Johnson constructions
   defeat the independent-depth ledger by an unbounded factor.
2. **Hamiltonicity is not the hard-core requirement.**  Exact small-component
   factors plus boundary-safe splicing solved k=13 and enabled k=15.
3. **Simple q1 palette is not required.**  Equation (4.1) describes the
   Johnson-edge identity cells, but row-zero/one/two cells can also realize
   rank-seven targets.  The exact sandwich Hall test permits any repeat count
   that actually matches; `(R,H)=(1,2)` is a clean sufficient endpoint, not a
   logical cap.
4. **Mean residence does not imply minimum residence.**  Short runs must be
   excluded or repaired explicitly.
5. **A missing-shadow count is not Hall.**  Named-cell competition can remain
   after zero candidates vanish.
6. **Monotone descent is not expected.**  k=13 temporarily traded q1 progress
   for q2 debt; k=15 temporarily trades palette for endpoint/Hall progress.
7. **Positive lower-bound slack does not force the observed normal form.**
   The normal form is justified by successful compilation, not scalar rigidity.
8. **Terminal constraints need not be bridge constraints.**  k=13 required
   temporary q2 debt, and k=15 required temporary palette debt.  Hard-constrain
   residence/upper coverage when their repair lane is absent, but do not
   universally hard-constrain every terminal shadow statistic throughout the
   search.
9. **The upper multiplicity profile is not forced.**  k=11 has only loads one
   and two, while the exact k=13 carrier has 78 triple-loaded upper colours.
   The total excess is forced; its distribution is not.

## 10. Search principles now justified by evidence

### A. Preserve a Pareto state, not a scalar best

The live state must record at least terminal palette distance, outer geometry,
named q2 roots, DM deficiency, q2 total, q3 total, residence, and upper holes.
Bridge states may worsen one coordinate; deleting them by scalar dominance
recreates every previously observed trap.

### B. Separate bridge and clean-normal-form budgets

Rotations may use `(R,H)=(2,3),(3,4),...`.  If the search is specifically
returning to the clean normal form, its decrementing seam must land at
`(1,2)`.  A Hall-PASS state at a larger repeat count is nevertheless a valid
compiler input and must not be discarded.  Using one budget for both made the
p2 state appear nearly rigid (four rotations); splitting them exposed 23
first moves and the successful chain.

### C. Target named Hall roots

The lower-q2 total is a useful smooth statistic, but the zero-candidate masks
and current DM block determine productive edits.  Score actual escape arcs
from the deficient block before generic q2 improvement.

### D. Escalate move order only after a finite closure

The k=14 six-piece proof and the k=15 local audits together justify moving to
five-plus segment or Posa-chain operations now.  Re-running 2/3/4-opt with new
weights cannot change their exact negative verdicts.

### E. Cross seeds at the contracted colour-component level

Raw edge-union SAT wastes structure.  First force singleton-colour edges,
contract their chains, and solve the residual coloured connector instance.
The completed 89-node census is both a negative result for the current pair
and a template for crossing future inequivalent clean carriers.

### F. Do not hard-code Johnson adjacency at positive slack

The exact compiler requires `D^3 A=T`, not that every consecutive pair of
middle sets intersect in rank seven.  Starting from a simple p3 carrier with
three missing q1 colours, a terminal concatenation may use one missing-colour
Johnson seam and one residence-safe non-Johnson seam.  It then has exactly two
q1 holes but avoids the used-colour bridge.  If the non-Johnson intersection
has rank six—ideally in the deficient orbit `2709`—it converts the spare seam
directly into the resource Hall currently lacks.  This lane follows from the
rigorous positive-slack correction and is strictly larger than every previous
Hamilton-path search.

The first targeted realization is already exact at the carrier level.  From
the Hall-31 bridge, three simultaneous upper-safe and residence-safe rank-six
seams fill roots `17738,21588,21672` and produce a four-path cover with

```text
q1/q2/q3 holes = 10/24/5,
residence = 0,
all upper holes = 0.
```

It is stored in `scratch/k15_h31_fourroot_pathcover.json` (the historical
filename says four-root; the audited object installs three roots).  Its fixed
endpoints do not yet admit a factorable concatenation, so the live operation
is endpoint rotation on this mixed path cover, not another fixed 3-opt.

### G. Segment the best chronology, then reorder globally

Cutting the Hall-30 path at upper-redundant edges gives path components whose
internal residence and complete upper shadows are inherited automatically.
The original order is a feasible point, while arbitrary residence-safe seams
open a global chronology neighborhood.  Exact instances with 46, 64, and 96
components have connected physical seam graphs with no forced leaves.  The
complete free census of the 46-component instance contains 108 Hamilton
chronologies and no Hall value below 30; the 64/96-component spaces are
larger and remain active.

Uniformly spaced cuts expose no seam that directly creates any of the five
rank-six zero candidates of the Hall-30 graph.  Targeted segmentations now
force endpoints whose intersections are

```text
5397, 10794, 17738, 21588, 21672.
```

These are deliberately off-rank compiler cells: a rank-six intersection of
two adjacent middle entries is not a natural q1/q2/q3 shadow statistic.  The
component-order objective must therefore score actual erosion/compiler cells,
not maximize the natural q2/q3 cover.  This is the current largest exact
neighborhood around the best state.

## 11. Immediate k=15 program

1. Continue exact-Hall Posa/DM descent from both the clean Hall-31 and bridge
   Hall-30 states; retain every named-root/DM Pareto state.  Hall zero, not q1
   repeat count, is the stopping rule.
2. Search the Hall-30 targeted 32/46/64/96-component segmentations with hard
   residence/upper clauses and an actual compiler-cell objective for the five
   named rank-six roots.  Exact-Hall audit every chronology.
3. Finish the free 64/96-component censuses, but do not repeat the exhausted
   46-component space or the eight-state Hall30/Hall37 overlay cube.
4. Continue generalized multi-seed contracted unions only when they introduce
   edges outside every already closed union.
5. On the first Hall PASS, run the global depth-three compiler, extract the
   length-6438 word, and exhaustively verify all 32,767 nonzero masks with two
   independent verifiers.

## 12. What this says about the all-k conjecture

The exact cases support `nu(k)=B(k)`, but they do not yet reveal one uniform
closed-form construction.  The strongest common architecture is instead:

```text
middle-layer factor/path cover
  -> exact residence and upper shadows
  -> bounded-repeat endpoint routing
  -> named-root Hall repair
  -> deterministic lower compiler.
```

This is more than a search recipe: every arrow has an exact finite theorem or
an independently auditable certificate behind it.  What remains missing for
an all-k proof is a uniform theorem guaranteeing the carrier and the final
Hall repair.  The k=15 search is currently testing the first dimension where
those two guarantees no longer coincide automatically.

## 13. Exact Hall separation and the end of the fixed-segmentation lane

The Hall-30 path has the canonical Dulmage--Mendelsohn witness

```text
|A|=1,528, |N(A)|=1,498, deficiency 30.
```

For a factorable linear carrier `P` and a fixed target family `A`, write
`h_A(P)` for the number of compiler cells adjacent to at least one target in
`A`.  Concatenation satisfies the exact one-sided inequality

```text
h_A(PQ) <= h_A(P) + h_A(Q).                         (13.1)
```

Indeed, partition a compiler cell of `PQ` by whether its start lies in `P` or
`Q`, and map it to the corresponding cell of the isolated component.  Gluing
can only intersect additional middle masks into the maximal erosion, so the
cell envelope shrinks; carrier sets shrink and the mandatory mask can only
grow.  Hence a target accepted after gluing was already accepted by its
isolated image.  The map is injective.  This proves that every seam weight in
the component-order Benders model is nonpositive; the observed sign pattern
was not a numerical coincidence.

Thus a segmentation exposes an isolated capacity `sum_i h_A(P_i)` and every
chosen seam spends some of it.  The first Benders inequality is exactly a
nonnegative travelling-path budget.  An exact CP-SAT separation exhausted
256 independently generated 32/46/64/96-component segmentations: every one
was infeasible after the first Hall-30 cut.  Safe 128- and 160-component
instances also fail the first cut; the 192-component instance can cross it but
only relocates the deficiency to 289 and then 136 before the three-witness
system becomes infeasible.  The 256- and 320-component runs crossed several
witnesses but did not improve Hall 30 within their exact time limits.

The failure can be certified even earlier.  Forced compiler actions consume
component ports.  Contracting them leaves a port graph in which any completed
chronology needs the appropriate perfect/near-perfect matching and one
connected component.  On the richest 64-component instance the port graph has
59 fragments, is disconnected, and has maximum matching 56 where 58 is
required.  A max-weight blossom relaxation that also charges the fixed DM
witness gives the stronger optimistic bound

```text
h_A <= 1,511 < 1,528,
```

so Hall deficiency is at least 17 before SAT.  It simultaneously forces at
least 20, 14, and 2 additional lower holes at depths 1, 2, and 3.  Port-safe
64/96-component instances have since been generated, but their optimistic DM
bounds are still only 1,505--1,513.  Generation must therefore condition on
topology and weighted witness capacity simultaneously.

This closes reordering/reversal of fixed Hall-30 segments as the primary lane.
It does not close new carrier edges or a different source factor.

## 14. Directed relabelling trade cubes: the first genuinely new carrier lane

For a Hamilton path `P`, adjoin a dummy vertex and regard its successor map as
a perfect matching from a source copy of the middle layer to a target copy.
For any coordinate permutation `tau`, the two matchings of `P` and `tau P`
decompose into alternating assignment cycles.  Choosing either parent on each
cycle independently preserves indegree and outdegree one.  A circuit
constraint, the exact depth-three residence clauses, and exact upper-shadow
clauses then select genuine new Hamilton carriers.

This is the rigorous form of the hybrid-cube idea.  Unlike the earlier
undirected path overlay, degree preservation is automatic because the objects
being switched are matching components.  For a transposition of two
coordinates, the Hall-30 source yields 842 nontrivial trade components and the
cube contains many mixed resident, all-upper-exact Hamilton paths.  The first
audited samples have Hall values 30--36: no improvement yet, but this is a
nonempty carrier family strictly outside fixed segmentation/reversal.

The next exact optimization is to express `h_A` for a fixed DM witness as a
sum of bounded local-pattern indicators on the trade bits, maximize it inside
CP-SAT, and then iterate exact DM cuts.  All 105 coordinate transpositions are
being screened before escalating to three-parent assignment catalogues.

That pricing step is now implemented in
`scratch/fast_k15_relabel_fixed_patterns.cpp`.  It enumerates the exact local
10/11/12-vertex compiler motifs in native code, aggregates 1.34 million path
prefixes into about 59,000 Boolean patterns, and reduces construction time
from over a minute in Python to about eight seconds.  In the `(0 1)` cube it
finds a mixed resident/all-upper Hamilton path with

```text
h_A = 1,581,
```

an 83-cell improvement over the Hall-30 source and 53 above the required
1,528.  Its full Hall deficiency is 50 because a new DM block forms; thus the
old witness is decisively escapable but one-witness optimization is not enough.
The frozen carrier is `scratch/k15_trans01_fixed1581_hall50.json`.

The same cutting-plane idea now works at generation time for segmentations.
After conditioning on the three witnesses that killed the first gain
portfolio, a new 256-instance portfolio contains candidates with simultaneous
optimistic margins such as `[30,19,18]`.  Conditioning on nine accumulated
witnesses still leaves multiple candidates positive on every individual
witness (best minimum margin 19).  Exact chronology models must preload the
same witness family; otherwise they merely relocate into a block that the
generator had already budgeted for.  The active loop is therefore

```text
exact DM witness -> native multi-resource generation -> joint CP-SAT cuts
                 -> new exact DM witness.
```

One remaining implementation subtlety in the trade cube is endpoint pricing.
The current native objective is exact on bounded interior cells.  A scalar
allowance for the at most 36 boundary cells gives a necessary but non-exact
cut; allowance zero is sufficient but can exclude endpoint-paid solutions.
The next native revision must enumerate the left/right dummy-path collars as
Boolean patterns, making every accumulated trade-cube Hall inequality exact.

### First global descent: Hall 30 to Hall 29

The targeted double-transposition cube for `(0 5)(2 13)` has now produced the
first carrier that improves the *full* matching, not merely a chosen witness:

```text
scratch/k15_doubletrans_05_213_hall29.json
SHA-256 5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c
```
It selects 683 assignment-trade components and has

```text
residence defects             0
upper holes q=1,...,7         0
lower q1 holes/repeats        4 / 3
lower q2 holes                21
lower q3 holes                4
compiler matching             16,354 / 16,383
Hall deficiency              29
zero-candidate targets         7.
```

Python and native C++ audits agree.  Its canonical DM block has
`1,524-1,495=29`; only 579 of its 1,524 targets lie in the old Hall-30 block.
The new chronology differs from Hall 30 in 5,531 of 6,434 directed edges, so
this is exactly the global reorganization that exhaustive 2/3/4-opt searches
could not reach.  The certificate and independent reports are indexed by
`scratch/k15_doubletrans_05_213_hall29.summary.json`.

Hall 29 is the new authoritative finite frontier.  It is not yet a
length-6,438 OR word; the compiler still requires deficiency zero.

### Exact boundary pricing closes the winning two-parent cube at Hall zero

The relabel objective now includes the exact 18 left-boundary and 18
right-boundary compiler cells; no scalar endpoint allowance remains.  Starting
from the Hall-29 carrier, optimization against its canonical DM family finds
the complement-side seven-trade carrier with neighbourhood 1,795, but its
exact audit creates a new block of size `1,524-1,495=29`.  Adding both exact
full-boundary inequalities makes the complete 691-variable resident,
all-upper-exact Hamilton cube infeasible.

Thus Hall zero does not occur anywhere in the directed two-parent cube between
Hall 30 and its `(0 5)(2 13)` relabelling.  This is an exact finite no-go for
that cube, not a timeout.  It does not rule out Hall 28 or a better carrier in
a richer parent catalogue.  The frozen summary is

```text
scratch/h29cube_exact_benders8.json
SHA-256 eb429f9d083c2ce49fcaeb1eb058b3c16f0c43718d9fece25a2efd57dff7c66f
```

The exhaustive subcube consisting only of the eight components omitted by the
Hall-29 solution has 22 valid non-parent settings; every one has Hall 29 or
30.  Hence the 26 changed successor sources form a cooperative improvement
gadget with a Hall-29 plateau, not a hidden Hall-28 local move.
