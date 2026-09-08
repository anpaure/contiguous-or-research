# Alternative support splits cannot unlock a two-rectangle trade

Date: 2026-09-07. This is an exact finite local reduction for the saved
integral charge-1280 cover of `[4]^6`, not a proof of global optimality.

## 1. Scope and distinction from the archived test

The saved cover has 80 rectangles and input SHA-256
`bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36`.
The archived `Q4_INTEGRAL_SEARCH_AND_EQUALITY_CENSUS_20260906_f7a91.md`,
Section 6, reports all 3160 two-row removals tested for strict improvement
with their **original two support splits**. Those solver calls were not
repeated here.

The new computation permits both replacement rectangles to use arbitrary
nonempty complementary coordinate splits. It first removes the objective
and asks exact incidence feasibility, using the complete 2-SAT reduction
below rather than a chain catalogue or a time-limited solver.

The current cover and archived `q4int_local2_witness_20260906_f7a91.json`
were independently compared after sorting coordinate shores and chain
coordinates: their normalized sets of 80 rows are identical. Thus the
archived original-slot conclusion concerns this same cover.

## 2. Exact two-color incidence reduction

Remove rows `i,j`, and let `K` be the targets not covered by the other 78
rows. Using original multiplicities, this is exactly

\[
K=P_i\cup P_j\cup
\{x\in R_i\cap R_j:\operatorname{mult}(x)=2\},
\]

where `P_i` consists of the globally private targets of row `i`.

Fix two replacement splits `sigma,tau`. For a split `sigma`, put an edge
between targets `x,y in K` when their projections on at least one shore
of `sigma` are incomparable. Denote this incompatibility graph by `B_sigma`.
One rectangle with split `sigma` can contain a point family exactly when
that family is independent in `B_sigma`: its two projections then form
chains, and their Cartesian product is a legal containing rectangle.

Assign each target a Boolean variable `z_x`, with value one meaning that
the target is assigned to the first new rectangle. The incidence problem
is equivalent to the following 2-CNF formula:

\[
\begin{array}{ll}
\neg z_x\lor\neg z_y,&xy\in E(B_\sigma),\\
z_x\lor z_y,&xy\in E(B_\tau).
\end{array}                                          \tag{1}
\]

Necessity follows by assigning each target to either rectangle that covers
it. Sufficiency follows by forming the Cartesian products of the two
projection chains of each color class. Targets covered by both rectangles
cause no difficulty: assign each of them to just one. Empty color classes
are permitted in this feasibility relaxation.

The common graph `B_sigma intersect B_tau` must be bipartite, since every
one of its edges requires different colors. This is only an early rejection
test; every surviving pair is checked against the full formula (1).

The implementation solves (1) by its implication graph. A negative clause
adds `z_x=1 -> z_y=0` and its symmetric implication; a positive clause
adds `z_x=0 -> z_y=1` and its symmetric implication. Strongly connected
components containing both values of one variable give infeasibility;
otherwise the component order gives an assignment. Every returned
assignment is independently checked against every clause before counting
it as feasible.

## 3. Exact dual pruning and complete results

Use the existing nonnegative integer point weights `w(x)` from
`q4int_verify_20260906_f7a91.py`. Their globally verified property is

\[
\sum_{x\in C\times D}w(x)\le12(|C|+|D|)
\]

for every strict chain pair and every split. Therefore any repair of `K`
by any number of new rectangles costs at least

\[
\left\lceil\frac1{12}\sum_{x\in K}w(x)\right\rceil. \tag{2}
\]

The original two-row charge minus (2) has this exact distribution:

| Maximum saving allowed by this lower bound | Removed-row pairs |
|---:|---:|
| 0 | 1425 |
| 1 | 1346 |
| 2 | 277 |
| 3 | 112 |

Thus 1425 pairs cannot improve under any repair and need no incidence
search. For each remaining pair, all 496 unordered pairs of the 31 possible
splits were tested, allowing the two splits to coincide.

| Exact stage | Count |
|---|---:|
| Removed-row residuals tested | 1735 |
| Split-pair tests | 860560 |
| Passed common-graph bipartiteness | 11785 |
| Passed full 2-SAT | 1735 |
| Feasible with the original support pair | 1735 |
| Feasible with any alternative support pair | **0** |

Every non-pruned residual admits exactly one unordered pair of support
splits: the original pair. The computation alone establishes this support
rigidity, not minimum charge within that original pair. Combining it with
the separately reported archived original-slot infeasibility checks would
exclude every strict two-to-two improvement of this cover. The present
standalone certificate deliberately stops at support rigidity; it does not
claim to re-certify those archived cost-optimality solver statuses.

Also, (2) shows that a single two-row repair could never have saved the
nine units needed to reach 1271, even with arbitrarily many replacement
rectangles. Any such improvement must involve more removed rows or a
sequence of changes through different cover banks.

## 4. Reproduction and limits

New files:

- `q4_alternative_split_input_20260907.py`: emits the hash-checked witness
  and the exact dual weights; it does not modify the witness.
- `q4_alternative_split_2sat_20260907.cpp`: constructs all residuals,
  performs the dual pruning, tests all remaining split pairs, and checks
  each feasible assignment against the original incompatibilities.
- `../scripts/verify_q4_alternative_split_certificate_20260907.py`:
  independently reconstructs the literal critical target sets and checks
  the complete streamed certificate described next. It also directly
  compares the normalized current and archived local-two witness rows.

```
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic \
  scratch/q4_alternative_split_2sat_20260907.cpp \
  -o /tmp/q4_alternative_split_2sat_20260907
python3 -B scratch/q4_alternative_split_input_20260907.py | \
  /tmp/q4_alternative_split_2sat_20260907
```

The fresh exhaustive run completed in approximately two seconds. No
optimization solver or solver timeout was involved. No improving witness
was produced, and no old witness or master file was changed.

### Independent verification of every split-pair decision

Run the C++ program with `--certificate` and pipe its output directly into
the Python verifier:

```
python3 -B scratch/q4_alternative_split_input_20260907.py | \
  /tmp/q4_alternative_split_2sat_20260907 --certificate | \
  python3 -B scripts/verify_q4_alternative_split_certificate_20260907.py
```

The Python verifier does not invoke the C++ graph algorithms or trust their
feasibility labels. It checks each of the following against independently
reconstructed point projections:

- 848775 odd cycles in the common incompatibility graph. All their edges
  are incompatible under both proposed splits, so two colors are impossible.
- 10050 pairs of directed implication paths taking a Boolean literal to
  its negation and back. Every implication is checked directly against an
  actual incomparable projected point pair.
- 1735 satisfying assignments. For each assignment, the two shore
  projections of each color class are explicitly checked to be chains.
- All 1425 dual-pruned residuals, all case identifiers in exhaustive order,
  and the equality of the current and archived normalized witness row sets.

The complete independent stream check passed in approximately four seconds.
The potentially large certificate is not stored in the workspace; it is
regenerated and checked in the pipe. This is a standalone certificate of the
new support-rigidity census, while original-slot cost optimality remains the
separate archived result mentioned above.

This does not exclude coordinated trades involving at least three old
rows, nor unrestricted alternative integral covers. The useful general
reduction is that free-split two-product incidence can be decided exactly
by 2-SAT, before any cost optimization.

## 5. Exact dual budget for arbitrary removed-row sets

The private targets give a stronger quantitative guide to larger trades.
For each old row put

\[
c_i=12(|C_i|+|D_i|)-\sum_{x\in P_i}w(x).
\]

Their exact census is

\[
\#\{c_i=0,6,16,19\}=50,4,10,16,
\]

respectively. Moreover, the only positive-weight shared target owner sets
are these eight disjoint pairs of zero-based row indices, each with total
weight 13:

\[
(14,29),(15,28),(26,55),(27,54),
(46,75),(47,74),(60,77),(61,78).
\]

Their sixteen endpoints are exactly the credit-19 rows. In particular,
there are no positive-weight shared targets with three or more owners.

For an arbitrary removed row set `J`, let `n_a(J)` count its credit-`a`
rows and let `e(J)` count fully removed pairs in that matching. The
critical target set consists of the private targets of removed rows and
the shared targets whose complete owner sets lie in `J`. Hence the dual
bound (2) gives the exact available dual-budget formula

\[
\boxed{\text{saving}\le
\left\lfloor\frac{6n_6(J)+16n_{16}(J)+19n_{19}(J)-13e(J)}{12}
\right\rfloor.}                                    \tag{3}
\]

This is valid for any number and support splits of replacement rectangles.
It is an upper bound on savings, not a construction achieving those savings.

The maximum numerator in (3), among all sets of exactly `r` removed rows,
is

\[
T(r)=\begin{cases}
19r,&0\le r\le8,\\
152+16(r-8),&8\le r\le18,\\
312+6(r-18),&18\le r\le30,\\
384,&30\le r\le80.
\end{cases}                                         \tag{4}
\]

To see this, each matching component offers marginal credits 19 then
`19-13=6`; the ten medium rows offer 16 each, the four remaining positive
rows offer 6 each, and the fifty others offer zero. Taking these marginal
credits in decreasing order respects the prerequisite within every pair
and attains (4).

Consequently one trade reaching the indicated whole-cover charge requires
at least this many removed old rows:

| Desired cover charge | Required saving | Minimum removed rows forced by the dual |
|---:|---:|---:|
| 1271 | 9 | 6 |
| 1260 | 20 | 14 |
| 1248 | 32 | 30 |

This explains why a three-row trade cannot immediately reach the threshold
1271: even its optimal dual allowance is only `floor(57/12)=4`.

For six-row trades, exactly 70112 removed sets pass the necessary
saving-nine threshold. They consist of six credit-19 rows (1792 choices),
five credit-19 rows and one credit-16 row (17920 choices), or four credit-19
rows and two credit-16 rows (50400 choices), in each case containing no
complete matching pair. The counts are

\[
\binom86 2^6,\qquad \binom85 2^5\cdot10,\qquad
\binom84 2^4\binom{10}2.
\]

These are candidate neighborhoods, not feasible replacement certificates.
For example, removing rows `14,15,26,27,46,47` has old charge 84 and
requires a replacement of charge at most 75 to reach 1271. Its available
scaled dual slack above that threshold is only six units.

The independent checker
`../scripts/check_q4_exact_trade_budget_20260907.py` reconstructs all
owners and weights, verifies the matching and credit census, and checks
all 81 values of (4) by an independent exact-cardinality knapsack dynamic
program. All checks pass.

## 6. Three-row private-core pruning: useful but insufficient

For three proposed support splits, intersect their three incompatibility
graphs. Four pairwise adjacent critical targets cannot fit into three
rectangles: every rectangle misses at least one pair, so those targets
require four colors. This gives a direct four-clique certificate without
solving a three-color or SAT problem.

The bounded test `q4_private_core_three_split_cut_20260907.cpp` applied this
criterion separately to the 80 private cores. For each core it tested all
4960 unordered triples of splits omitting that row's original split.
It found four-clique obstructions in 162140 of 396800 cases. Combining
the three relevant private-core cuts for each of the 82160 removed-row
triples still leaves between 125 and 4130 alternative support triples.

Thus these cuts do not make a broad three-row search small enough to
justify an unstructured solver run; no such run was launched. The stronger
actionable consequence is the exact neighborhood budget in Section 5.

## 7. A fresh targeted six-row test

The root subsequently tested the dual-selected set
`J={14,15,26,27,46,47}` using the exact shore-vertex formulation in
`q4int_local_20260906_f7a91.py`, function `repair`. Removing these rows
leaves 184 critical targets and frees charge 84. The tested threshold was
83, allowing **any** strict improvement, not just the 75 required to beat
the current full-cube coefficient in one trade.

| Replacement support slots | Limit / workers / seed | Fresh solver status | Verified new cover |
|---|---|---|---|
| The original six slots | 30 s / 4 / 70907 | `INFEASIBLE` | none |
| Original six, plus one slot for every other split: 33 slots total | 30 s / 4 / 709071 | `UNKNOWN` | none |

The second model permits arbitrary strict chains in every slot, but does
not permit arbitrary multiplicities of newly introduced splits. The first
entry is a solver-reported scoped infeasibility, not an independently
stream-checked proof like Section 4. `UNKNOWN` establishes no lower bound.
Neither entry changes the retained charge 1280. Both runs terminated; no
search was left live and no candidate witness was saved.

For reproduction, load and normalize the current witness without changing
row order, form `kept` and `removed` using `J`, and call
`repair(kept, removed, supports, 30, seed, 4, target=83)`. The original
distinct supports are `(0,1,2),(0,1,4),(0,1,5),(0,3,5)`. In the expanded
model add each nonempty proper split containing coordinate zero once,
except these four already represented splits. OR-Tools was version
9.15.6755. The archived virtual environment had missing Python module
files; the successful imports used the complete cached package directory
`/Users/amir.nuriyev/.cache/uv/archive-v0/H42pBNG6ZbyqSYtvRYOdb/lib/python3.12/site-packages`
first on `sys.path`. The earlier import failures did not start a solver.
