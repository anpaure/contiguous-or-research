# Quaternary Integral Search and Complete Equality Census

Date: 2026-09-06. New scratch files only, suffix `f7a91`.

## 1. Result and Scope

**The requested integral gate was not closed.** No integral cover of charge
below 1280 was found. The rigorous finite bounds remain

\[
                 1248 \le M_{\rm int}(4,6) \le 1280.
\]

In particular, this work proves **no improvement** to the user's current valid
global coefficient `1.1807038038...`. The finite 1280 template itself transfers
to the older, weaker coefficient `(5/4) beta_7 = 1.1882294403...`.

The useful new results and artifacts are:

- A complete enumeration of **166,661 dual-tight chain-pair symmetry types**
  for the exact `c52e9` dual, not just its 14 positive fractional types.
- Their complete **7,464 distinct point-orbit census vectors**.
- An exact optimal-dual-face direction excluding **1,881** of those census
  types from any integral cover of cost exactly 1248.
- An independently checked **balanced-only fractional cover of cost 1248**:
  every shore has three coordinates. Thus the fractional improvement does
  not require `2+4` splits. This is explicitly **not** an integral cover.
- An expanded, symmetry-free **162,142-column** integer feasibility test of
  the actual threshold 1260, with all 4096 targets and a dual-waste constraint.
  Its fresh terminal status was `UNKNOWN`, with no feasible witness.
- A literal, independently checked 80-rectangle witness of cost 1280,
  retained by the enlarged integer search.

No fractional-to-integral rounding premise is used. No existing project file
was edited. Master/index integration is left to the parent.

## 2. Explicit Integral Witness and Independent Check

The final incumbent is stored in

`q4int_final1280_witness_20260906_f7a91.json`.

It contains, for every rectangle, the actual coordinate lists `left`, `right`
and the complete ascending vertex lists `C`, `D`. There are no implicit
fractional multiplicities or solver variable references.

The separate standard-library verifier
`q4int_verify_20260906_f7a91.py` does not import the search, fractional-cover,
or tube-construction code. It checks coordinate partitions, integer vertex
coordinates, strict comparability, every one of the 4096 Cartesian targets,
and the sum of chain lengths. Its final result is:

| Quantity | Exact Value |
|---|---:|
| Principal charge | 1280 |
| Rectangles | 80 |
| Targets covered | 4096 |
| Total occurrence volume | 5120 |
| Excess | 1024 |
| Targets of multiplicity 1 | 3456 |
| Targets of multiplicity 2 | 512 |
| Targets of multiplicity 5 | 128 |
| Twelve times total rectangle dual slack | 280 |
| Twelve times dual-weighted overlap | 104 |

The witness SHA-256 is

```text
bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36
```

Recheck from the workspace root:

```sh
python3 -B scratch/q4int_verify_20260906_f7a91.py \
  scratch/q4int_final1280_witness_20260906_f7a91.json
```

The unchanged `qary_dual_verify_20260906_c52e9.cpp` was separately rebuilt and
run. Its exhaustive integer-arithmetic check again established the universal
lower bound 1248 over **every split and every strict chain**, including
nonsaturated chains. This old exact certificate, rather than a MIP bound,
is the lower-bound premise above.

## 3. Complete Equality Shapes

Let `w(x)=12 y(x)` be the nonnegative integer dual weights from `c52e9`.
For a fixed left chain `C`, put

\[
               g(z)=\sum_{x\in C}w(x,z)-12.
\]

If `C x D` is tight, then `sum_(z in D) g(z)=12|C|`. No selected right
vertex can have `g(z)<0`: deleting that vertex would produce a violation of
the already verified universal dual inequality. Therefore all tight right
chains can be enumerated using only nonnegative vertices.

`q4int_shapes_20260906_f7a91.cpp` enumerates every left chain, identifies its
representative under internal coordinate permutations and simultaneous
reflection, and computes the maximum suffix weight at every right vertex.
It then follows **all** comparable successors attaining the required suffix
value, including every optional zero-weight vertex. This enumerates distinct
strict right chains, not just saturated paths with duplicate skipped-node
representations.

Finally, each pair is canonicalized under independent coordinate permutations
within its shores, simultaneous reflection, and shore exchange when balanced.
Developing these representatives under all six-coordinate permutations
recovers every coordinate split.

| Split | All Left Chains | Canonical Left Chains | Tight Left Representatives | Tight Right Chains Before Right Quotient | Pair Shapes |
|---|---:|---:|---:|---:|---:|
| `1+5` | 15 | 9 | 0 | 0 | 0 |
| `2+4` | 1007 | 275 | 16 | 868056 | 25275 |
| `3+3` | 257295 | 21799 | 1101 | 1735134 | 141386 |
| Total | | | | | 166661 |

The generated file is `q4int_tight_shapes_20260906_f7a91.txt`. Each line is

```text
r  length(C)  base4_ids(C)...  length(D)  base4_ids(D)...
```

All these columns have zero reduced cost for the original dual. This is an
equality catalogue, **not** a complete catalogue for costs 1249 through 1280:
positive-slack rectangles may be useful above equality.

`q4int_census_20260906_f7a91.cpp` collapses the complete catalogue by its actual
44-orbit incidence vector, yielding `q4int_censuses_20260906_f7a91.txt` with
7464 distinct vectors. The orbit is the coordinate-value histogram up to
reversal; the incidence counts actual vertices of `C x D`.

## 4. An Exact Equality-Face Filter

The direction saved in `q4int_face_direction_20260906_f7a91.json` has the
following nonzero entries. All unlisted orbit coordinates are zero.

| Histogram Up to Reversal | Direction `z` |
|---|---:|
| `(0,2,4,0)` | -4 |
| `(0,3,2,1)` | -1 |
| `(0,3,3,0)` | 6 |
| `(0,4,0,2)` | 2 |
| `(0,4,1,1)` | 4 |
| `(0,5,0,1)` | -5 |
| `(1,1,3,1)` | -2 |
| `(1,2,1,2)` | 1 |
| `(1,2,2,1)` | 2 |
| `(2,1,1,2)` | -2 |

The script `q4int_face_20260906_f7a91.py` discovers the direction numerically,
then converts it to the displayed integers and checks **exactly** that

\[
 \sum_O |O|z_O=0,\qquad A z\le0
\]

for all 7464 complete tight census vectors `A`. It also checks `z_O>=0`
where the old dual vanishes. There are 1881 strict inequalities and 5583
equalities. In this particular direction there are no newly positive orbits.

Here is a direct exact proof that the filter is valid for the full problem.
Set

\[
                    y'(x)=y(x)+z(x)/14400.
\]

The perturbation is at most `1/2400` in absolute value. Old positive weights
are at least `1/6`, so all new weights are nonnegative. An old non-tight
rectangle has slack at least `1/12`. Every strict chain on `r` coordinates
has at most `3r+1` vertices, so every six-dimensional chain-pair rectangle
has volume at most 100. The perturbation changes its dual mass by at most
`100/2400=1/24`; hence it remains feasible. An old tight rectangle remains
feasible by `A z<=0`. The total new dual weight is still 1248.

Consequently any cover of cost exactly 1248 must be tight for both duals.
Every old tight census with `A z<0` can be removed from an equality search.
This filter is **not** asserted to exclude those columns for a 1260 cover.

## 5. Balanced-Only Fractional Optimum

`q4int_balanced_fractional_20260906_f7a91.py` supplies 15 explicit `3+3`
chain-pair types and positive weights with denominator 119. Developing each
uniformly under coordinate permutations and simultaneous reflection gives
the integer orbit inequalities

\[
 \sum_j n_j |(C_j\times D_j)\cap O|\ge119|O|,
 \qquad \sum_j n_j(|C_j|+|D_j|)=148512=119\cdot1248.
\]

The checker verifies these inequalities and all chains with exact integers.
The occurrence volume is `638912/119`. Together with the unchanged universal
lower certificate, this proves

\[
              M_{\rm frac}^{\,3+3}(4,6)=1248.
\]

This removes a possible explanation of the failed local repairs: `2+4`
splits are not necessary even fractionally. The certificate also supplies
useful cost-15 balanced shapes absent from the original 14-type support.
It does **not** imply an integral cover or a global Boolean coefficient.

```sh
python3 -B scratch/q4int_balanced_fractional_20260906_f7a91.py
```

The separate integral **census relaxation**, in
`q4int_census_relaxation_20260906_f7a91.json`, also has a cost-1248 solution:
22 census types with integer multiplicities. Positive-dual orbit totals
are exact, and other orbit totals are sufficient. This is only a necessary
relaxation: its coordinate orientations have not been chosen to cover
individual targets. It is deliberately not called an integral grid witness.

## 6. All-Target Integer Search and Cost Accounting

The expanded search uses three sources of columns:

- All developments of the original 14 fractional types.
- New asymmetric all-chain pricing under perturbed exact dual weights:
  independent point noise, point-orbit noise, and baseline-correlated noise.
- Genuine single-vertex insertions, deletions, and replacements in each
  shore of baseline rectangles, paired simultaneously across both shores.

The 15 balanced fractional types were subsequently added. This produced
162142 actual chain-pair columns. The small-shore pricing routine
`q4int_price_20260906_f7a91.cpp` enumerates every left chain on every split
and optimizes the other shore by grid dynamic programming. Returned columns
are actual chain lists. The **sampled master pool** is nevertheless finite
and incomplete; pricing calls do not make a timed-out master search a
full-problem infeasibility proof.

For a genuine cover with multiplicities `h(x)`, the exact accounting identity is

\[
 \sum_j\left(12(|C_j|+|D_j|)-\sum_{x\in C_j\times D_j}w(x)\right)
 +\sum_x w(x)(h(x)-1)=12(M-1248).
\]

Both terms are nonnegative. Thus the target 1260 allows at most 144 units
of scaled rectangle slack plus weighted overlap, whereas the baseline uses
`280+104=384`. The direct 1260 CP model includes a redundant Boolean overlap
ledger derived from this identity, in addition to actual target coverage and
the full cost constraint. This is a simultaneous coverage-and-cost search,
not independent orbit rounding.

### Final Fresh Runs

| Test | Actual Master Scope | Limit | Fresh Status | Verified Integral Cost |
|---|---|---:|---|---:|
| Exact 1248 | 75200 raw columns, 65560 retained after equality filtering, no symmetry restriction, all 4096 targets | 300 s | `UNKNOWN` | None |
| Improve 1280 | 162142 raw columns; 100336 bundles under the baseline involution; 2048 target orbits | 300 s | `FEASIBLE` | 1280 |
| Direct 1260 | 162142 columns, no symmetry restriction, all 4096 targets, explicit overlap ledger | 240 s | `UNKNOWN` | None |

The final 1280 search's involution is coordinate permutation
`(5,3,2,1,4,0)` followed by simultaneous value reflection. Each bundle is
expanded to its literal rectangles before the independent witness check.

Fresh records, including `verified_cost: null` for unsuccessful runs, are:

- `q4int_final1248_witness_20260906_f7a91.json.status.json`
- `q4int_final1280_witness_20260906_f7a91.json.status.json`
- `q4int_direct1260_witness_20260906_f7a91.json.status.json`

**A solver can print `objective=1260` on an `UNKNOWN` feasibility run without
having any feasible incumbent. That printed number is not an upper bound.**
No 1248 or 1260 witness JSON was generated by these unsuccessful runs.

Earlier, smaller CP runs tested 1248 with the baseline involution and 1260
with cyclic groups of orders three and five. All timed out without a witness.
A 58661-column, involution-restricted optimization retained the baseline.

Two larger HiGHS attempts were terminated before producing a final status.
The retained log `q4int_highs_mutation_run_20260906_f7a91.log` reaches the
root search of a 145603-column model and reports only the supplied 1280
start. These interrupted runs yield **no** infeasibility, optimality, or
improvement claim. No solver process was intentionally left running.

### Local Formulations

`q4int_local_20260906_f7a91.py` selects shore vertices directly. Incomparable
vertices cannot share a chain, each uncovered target must be assigned to
some rectangle, and the objective is the number of selected shore vertices.
For fixed support slots, this includes every chain, rather than a path pool.
Restricting vertices to projections of residual targets loses no optimum:
other vertices can be deleted without harming the repair.

All 3160 two-rectangle removals were tested with their two original support
splits retained; CP reported every strict improvement infeasible. This is
strictly scoped to those two support slots, not all alternative split pairs.
Random eight-rectangle repairs made 34 calls: 15 returned `INFEASIBLE` and
19 `UNKNOWN`, with no improvement.

The asymmetric column-generation experiment with 16 removed rectangles
generated a 25016-column residual pool. Its restricted MIP proved the old
residual charge 264 optimal. Pricing had **not** converged, so this is not
an all-column local lower certificate. A 48-rectangle experiment was
terminated during column generation, likewise without a complete certificate.

## 7. Reproduction and Files

The standard-library witness and fractional checkers above do not require
any solver. The exact shape and census programs require a C++17 compiler.

```sh
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic \
  scratch/q4int_shapes_20260906_f7a91.cpp \
  -o /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_shapes_f7a91
/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_shapes_f7a91 \
  scratch/q4int_tight_shapes_20260906_f7a91.txt
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic \
  scratch/q4int_census_20260906_f7a91.cpp \
  -o /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_census_f7a91
/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_census_f7a91 \
  scratch/q4int_tight_shapes_20260906_f7a91.txt \
  scratch/q4int_censuses_20260906_f7a91.txt
```

The search environment is isolated at
`/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_f7a91`.
It has CPython 3.12.11, OR-Tools 9.15.6755, HiGHS 1.15.1, NumPy and SciPy.
The generated 58661-column initial expanded pool is
`q4int_expanded_pool_20260906_f7a91.json`; the larger pool is deterministically
reconstructed from it by the mutation and balanced-seed flags.

The direct threshold experiment can be rerun with:

```sh
/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/q4int_f7a91/bin/python -B \
  scratch/q4int_expanded_20260906_f7a91.py \
  --pool-input scratch/q4int_expanded_pool_20260906_f7a91.json \
  --output scratch/q4int_direct1260_witness_20260906_f7a91.json \
  --balanced-seeds --mutations --overlap-ledger \
  --seconds 240 --threads 8 --target 1260 --symmetry none --seed 1260
```

Only explicit feasible solutions passing the independent integer checker
are saved as witness JSON. Failed search results and necessary relaxations
are kept separate. The finite gate `M_int(4,6)<=1260` remains unresolved.
