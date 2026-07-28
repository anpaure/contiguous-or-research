# Exact minimal-parent-cover decomposition for the k=15 five-face model

Date: 2026-07-28

Scope: the five canonical directed parent paths

```text
P0 = k15_doubletrans_05_213_hall29.json
P1 = k15_outer2_p1_h30_bridge.json
P2 = k15_trans1113_balanced_hall31.json
P3 = k15_transposition_parent_winner.json
P4 = k15_accumulated_zero_parent_winner.json
```

and the five fixed face-shore inequalities currently used by
`exactdm_5cycle_boundaryupper`.  This note does not claim Hall zero.  It gives
an exact decomposition of that finite search, proof-safe cuts inherited from
the ten pair UNSAT results, and a feasibility homotopy which does not weaken
endpoint or all-shore acceptance.

## 1. Minimal-cover theorem

Let `E_p` be the directed normal-arc set of parent `p`, and let `X` be the
normal-arc set selected by a Hamilton path in `union_p E_p`.  A parent set
`S` covers `X` when

\[
             X\subseteq E_S:=\bigcup_{p\in S}E_p.
\]

### Theorem 1 (lossless face-lattice decomposition)

Every selected path `X` has an inclusion-minimal parent cover `S`.  For such
an `S`,

\[
 X\subseteq E_S,
 \qquad
 X\cap\left(E_p\setminus\bigcup_{q\in S\setminus\{p\}}E_q\right)
 \ne\varnothing\quad(p\in S).                 \tag{1.1}
\]

Conversely, (1.1) says exactly that `S` covers `X` and that no member of `S`
can be deleted from that cover.

#### Proof

Choose an inclusion-minimal cover.  If the second condition failed for some
`p`, every selected arc supplied by `p` would also be supplied by another
member of `S`; hence `S - {p}` would still cover `X`, a contradiction.  The
converse is the same argument reversed.  Every finite cover contains a
minimal subcover.  \(\square\)

All ten two-parent catalogues are already exact UNSAT under a proof-safe
endpoint upper bound.  Hence a **globally Hall-perfect** candidate cannot be
supported by any pair: if it were supported by `{i,j}`, its true
neighbourhoods for the two frozen shores `A_i,A_j` would satisfy the exact
pair model, contradicting that UNSAT result.  Its minimal cover therefore has
size at least three.  Consequently the Hall-perfect search is the union of
exactly

\[
               \binom53+\binom54+\binom55=10+5+1=16       \tag{1.2}
\]

minimal-cover branches.  No Hamilton path and no endpoint choice is lost.

In code, for branch `S`, retain the full five-parent arc table (so every
existing motif file still maps), but add

```python
allowed = frozenset(S)
for pair, lit in zip(arc_pairs, normal_lits):
    if arc_sources[pair].isdisjoint(allowed):
        model.Add(lit == 0)
for p in sorted(allowed):
    witnesses = [
        lit for pair, lit in zip(arc_pairs, normal_lits)
        if p in arc_sources[pair]
        and arc_sources[pair].isdisjoint(allowed - {p})
    ]
    model.AddBoolOr(witnesses)
```

The first family restricts the selected path to `E_S`; the second is the
minimality witness in (1.1).

## 2. Ten entailed pair-escape cuts

For a pair `P={i,j}`, every five-face solution must select an arc outside
`E_i union E_j`.  Hence the following ten inequalities are valid in the
unbranched model:

\[
 \boxed{\quad
   \sum_{e:\,\operatorname{src}(e)\cap\{i,j\}=\varnothing}x_e\ge1
   \quad(0\le i<j<5).
 \quad}                                                   \tag{2.1}
\]

Here `src(e)` is the set of parents supplying directed arc `e`.  The exact
implementation is

```python
from itertools import combinations
for pair in combinations(range(len(parents)), 2):
    pair = frozenset(pair)
    outside = [
        lit for edge, lit in zip(arc_pairs, normal_lits)
        if arc_sources[edge].isdisjoint(pair)
    ]
    model.Add(sum(outside) >= 1)
```

These are not heuristic diversity constraints.  Their validity for the
desired Hall-perfect candidate follows from the exact pair UNSAT artifacts.
They preserve all endpoint, residence and global-shore semantics.  The
current five-cycle surrogate uses pair-local positive-state files generated
on five chosen cycle faces; those restricted rows are not literally the same
objects as all ten pair models.  Thus (2.1) is a target-valid Hall cut, not a
claim that every non-Hall-perfect path satisfying only the restricted
five-face surrogate must obey it.

### Stronger core cuts (requires full-union shore predicates)

Build the full five-parent graph with the two **globally exact** fixed-shore
predicates for `A_i,A_j`.  Add every literal `not x_e`, for `e` outside that
pair, as a CP-SAT assumption.  This assumption set recreates the proved pair
face.  If
`SufficientAssumptionsForInfeasibility()` returns a core `C`, then

\[
                         \bigvee_{e\in C}x_e             \tag{2.2}
\]

is a proof-safe strengthening of (2.1): even if every non-core outside arc
is left free, forbidding the core arcs is already inconsistent.  Use
`core_minimization_level=2`, then deletion-minimize or recursively split
tail-vertex blocks.  A cardinality ramp

\[
             \sum_{e\notin E_i\cup E_j}x_e\le t          \tag{2.3}
\]

gives a still stronger certified distance cut whenever it is UNSAT:
the full model then entails that the same sum is at least `t+1`.

No assumption-core sizes were present in the current artifacts; the ten
existing runs built the smaller pair graphs directly.  They therefore prove
(2.1) but do not yet provide (2.2).  In particular, do **not** derive (2.2)
by loading a two-parent positive-state list into the full union.  Once a
proper subset of the outside-arc assumptions is released, a Hall-perfect
path may obtain `A_i` or `A_j` neighbours through mixed outside-parent local
words which that list omits.  The resulting core would certify only the
restricted surrogate.  The global successor/zeta or exact centered compiler
predicate is required for a target-valid core or distance cut.

## 3. Exact branch sizes and recommended order

The five-parent union has 23,628 normal arcs.  The ten triple unions are:

| branch `S` | arcs |
|---|---:|
| 0,3,4 | 14,510 |
| 0,1,2 | 15,890 |
| 0,1,4 | 15,909 |
| 0,1,3 | 15,920 |
| 1,2,3 | 16,246 |
| 1,2,4 | 16,370 |
| 0,2,3 | 16,382 |
| 0,2,4 | 16,434 |
| 1,3,4 | 17,593 |
| 2,3,4 | 17,890 |

The quadruple sizes are 19,751 (`0123`), 19,808 (`0124`), 19,823
(`0134`), 20,324 (`0234`), and 21,422 (`1234`).

For fast exclusion, use the increasing-arc order displayed above.  For a
positive hunt, first try the five triples which meet every edge of the
parent 5-cycle (equivalently, whose omitted pair is nonadjacent):

```text
013, 124, 023, 024, 134.
```

Among those, the arc-count order is `013,124,023,024,134`.

The branch command, after adding `--allowed-parent-set` and
`--minimal-parent-cover`, is the existing five-face command with these two
extra flags, for example

```bash
PYTHONPATH=/dev/shm/orlib python3 -u \
  search_k15_directed_parent_union_cpsat.py \
  P0.json P1.json P2.json P3.json P4.json \
  --output exactdm_5cycle_S013.json \
  --hall-bin ./fast_k15_hall_dm \
  --seconds 1800 --workers 16 --rounds 1 \
  --allowed-parent-set 0,1,3 --minimal-parent-cover \
  --hint-parent 0 \
  --exact-fixed-motif-file pair01_block0.exact.tsv \
  --exact-fixed-threshold 1524 \
  --exact-fixed-motif-file pair12_block1.exact.tsv \
  --exact-fixed-threshold 1528 \
  --exact-fixed-motif-file pair23_block2.exact.tsv \
  --exact-fixed-threshold 1529 \
  --exact-fixed-motif-file pair34_block3.exact.tsv \
  --exact-fixed-threshold 1524 \
  --exact-fixed-motif-file pair40_block4.exact.tsv \
  --exact-fixed-threshold 1524 \
  --exact-fixed-boundary-upper
```

Keeping all five sources in the command is intentional: the motif edge table
continues to map, while the support constraints define the actual branch.

## 4. The min-slack audit: not a one-line bug

The current source creates

```python
fixed_min_slack = model.NewIntVar(0, W, "fixed_min_slack")
```

at line 1601 and maximizes it.  However every exact row has already imposed

```python
model.Add(sum(weighted_terms) >= threshold)
```

at line 477.  Therefore the nonnegative domain is consistent with the
documented meaning, *surplus among already feasible solutions*.  Merely
changing `[0,W]` to `[-W,W]` does not create a feasibility homotopy: the hard
shore rows still reject every negative-margin carrier.

The useful exact change is a separate `--soft-fixed-thresholds` mode:

1. have each fixed-row builder return its exact/proof-safe score but omit the
   hard `score >= threshold` row in soft mode;
2. create `margin = NewIntVar(-W, W, ...)`;
3. add `margin <= score_i - threshold_i` for all five shores;
4. maximize `margin` (then, at fixed optimum, maximize the sum of the five
   capped scores);
5. save the best path as an arbitrary `--hint-path`, not merely a parent
   index;
6. once `margin >= 0`, rerun with the five hard rows and independently audit
   every endpoint and shore.

This changes only search guidance.  Final acceptance remains the original
hard all-shore model plus the independent Hall auditor.

## 5. A second proof-safe relaxation before the cold model

For face `f`, let `b_i^f` say that the selected arc at order position `i`
belongs to that face's pair union.  A face-positive interior motif has 9, 10,
or 11 arcs in the present exact files.  If the 1-runs of `b^f` have lengths
`ell`, then the number of possible positive interior motifs is at most

\[
 U_f=\sum_{\text{runs }\ell}
       [ (\ell-8)_+ +(\ell-9)_+ +(\ell-10)_+ ].          \tag{5.1}
\]

The endpoint upper budget is at most 36, so every five-face solution obeys

\[
                         U_f+36\ge |A_f|                 \tag{5.2}
\]

for all five faces.  This is a small run-automaton/cardinality relaxation and
contains no target-motif variables.  Solve circuit + (2.1) + (5.2) first;
then add residence; then add the exact shore rows one at a time with the
signed-margin incumbent as a hint.  UNSAT at any relaxation is a valid
no-go; SAT is only a warm start.

## 6. Exactness caveats in the current artifacts

`--exact-fixed-boundary-upper` is a proof-safe endpoint *upper bound*, not an
exact joint collar.  Moreover the five motif files were generated on their
respective two-parent faces.  Thus the current five-cycle model asks for five
face-local neighborhood counts.  It is not the same as evaluating each shore
against every mixed five-parent local word.  Both facts are safe for the
stated restricted five-face UNSAT lane, but any positive checkpoint still
requires the exact literal endpoint audit and the global compiler matching
audit.  The support decomposition above preserves precisely the current
face-local semantics.

For a global-shore model, use the same decomposition but regenerate/refine
each shore predicate on the branch catalogue.  Do not reuse a two-parent
positive-state list as though it exhausted a larger catalogue.

The source should make this distinction impossible to miss.  After mapping
the producer edge table, global-exact mode must assert

```python
producer = {(node_of[a], node_of[b]) for a, b in cpp_edges}
consumer = set(arc_pairs)  # or the branch-active arc set
if producer != consumer:
    raise ValueError("exact motif catalogue differs from consumer catalogue")
```

The existing adaptive-exact consumer already performs this equality check;
`add_exact_fixed_dm_constraint` currently checks only that producer edges are
present.  If the restricted face-local experiment is retained, expose it
under an explicitly named opt-in such as `--restricted-face-score` and never
label its UNSAT result a global Hall no-go.  Likewise, an endpoint maximum
computed on a strict producer subcatalogue is not a global upper bound after
mixed consumer collars are admitted.

## 7. Exact polynomial-size global-shore formulation

There is a direct replacement for positive-pattern enumeration.  It is exact
on an arbitrary mixed-parent catalogue and uses the existential definition
of a neighbour cell in the favourable direction.

Fix a shore `A` and let `C` range over the `3W+6` physical compiler cells.
The selected chronology determines, for every cell, its erosion rows
`Q_p(C)`, envelope `E_C`, and mandatory mask `M_C`.  Introduce

* a Boolean `hit[A,C]`; and
* a target mask `T[A,C]` whose domain is exactly the finite set `A`.

Impose only the reified implication

\[
 \operatorname{hit}_{A,C}\Longrightarrow
 \left[
 M_C\subseteq T_{A,C}\subseteq E_C,
 \quad T_{A,C}\cap Q_p(C)\ne\varnothing\quad(p\in C)
 \right],                                                \tag{7.1}
\]

and the cardinality row

\[
                         \sum_C\operatorname{hit}_{A,C}\ge |A|. \tag{7.2}
\]

### Theorem 7.1 (witness-cell equivalence)

Equations (7.1)--(7.2) are satisfiable if and only if the literal compiler
neighbourhood obeys `|N(A)| >= |A|`.

#### Proof

Every true `hit[A,C]` carries a member of `A` which literally fits the
distinct physical cell `C`; hence (7.2) certifies at least `|A|` distinct
neighbour cells.  Conversely, if `|N(A)| >= |A|`, choose `|A|` neighbour
cells and one fitting shore target in each; set exactly those hit variables
to one.  No reverse implication is needed.  \(\square\)

This is important computationally: the model needs one target witness per
*selected cell*, not one Boolean for every positive 5/6/7-edge path in the
catalogue.  Its size is polynomial in `k,W` and the number of shores and is
independent of the five-parent branching factor.

### Concrete CP-SAT channel

Use the already audited inverse chronology channel:

```python
position = [model.NewIntVar(0, W-1, ...) for v in vertices]
node_at  = [model.NewIntVar(0, W-1, ...) for i in range(W)]
model.AddInverse(position, node_at)
```

Channel selected arcs to consecutive positions.  Decompose the `W` masks
`Y_i = mask[node_at[i]]` once, then compute the erosion bits `Q_i` once.
All five shores share `Y,Q,E,M`.  The interior cells at depth `h` are the
`W-9-h` centered positions; the remaining twelve cells per depth (six at
each end) use the exact nine-vertex boundary formula.  Thus the count is

```text
sum_h (W-9-h) + 2*6*3 = 3W+6,
```

as required.

For a shore target, use

```python
target = model.NewIntVarFromDomain(
    cp_model.Domain.FromValues(sorted(A)), ...
)
target_bits = [model.NewBoolVar(...) for x in range(15)]
model.Add(target == sum((1 << x) * target_bits[x] for x in range(15)))
```

For every coordinate `x`, (7.1) contributes only

```python
model.AddBoolOr([hit.Not(), mandatory[x].Not(), target_bits[x]])
model.AddBoolOr([hit.Not(), target_bits[x].Not(), envelope[x]])
```

For each erosion row `Q_p` in the cell, avoid fifteen product auxiliaries:
choose one coordinate witness `c` in `0..14`, use two `AddElement` lookups
to read `target_bits[c]` and `Q_p[c]`, and imply that both equal one when
`hit` is true.  Endpoint cells use the same witness constraints and the
literal left/right `E,M,Q` values, not `+36` and not an endpoint-only upper
maximum.

For the five canonical shores this is roughly 96,555 cell-hit/target pairs,
not tens of millions of positive mixed-parent states.  It is therefore the
recommended proof-safe exact model inside each minimal-cover branch.  The
final independent Hall audit remains mandatory, because five frozen shores
are necessary cuts but not a complete Hall separation oracle.
