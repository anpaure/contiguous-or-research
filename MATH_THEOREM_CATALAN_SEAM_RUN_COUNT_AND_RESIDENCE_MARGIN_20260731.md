# Catalan seam run count and the exact residence margin

Date: 2026-07-31  
Status: all-`m` counting theorem; exact `m=5` replay; no uniform run-balancing
construction

## 0. Verdict

The residence problem after a Catalan linear matching has an exact global
ledger.  Before the path components are joined, every coordinate occurs in
exactly `Cat_m` runs.  Every legal Johnson seam which joins two components
merges exactly `m-1` of those runs.  Hence a cyclic joining has average
coordinate-run length exactly `m`.

Since the word construction asks for minimum run length `d+1=O(sqrt(m))`,
there is a linear-factor margin in the aggregate.  The obstruction found at
`m=5`—many length-one and length-two runs—is therefore a distributional
obstruction, not a shortage of total residence mass.  An interior rethread
must redistribute this fixed run budget.

## 1. Catalan linear matching notation

Let

\[
 M={2m\choose m},\qquad N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.
\]

Let `F` be a spanning path forest in `J(2m,m)` with `N` edges whose
rank-`m-1` intersection colours and rank-`m+1` union colours are each used
exactly once.  Such an `F` is the lift of a Catalan linear matching and has
exactly `K` path components.

For a coordinate `x`, let `F_x` be the subgraph induced by the middle sets
which contain `x`.  Its connected components are precisely the maximal
`x`-runs along the path components of `F`, including singleton runs.

## 2. Exact run theorem

### Theorem 2.1

For every coordinate `x`, `F_x` has exactly `K` components.  Consequently
the total number of coordinate runs over all `2m` coordinates is `2mK`.

#### Proof

There are

\[
             |V(F_x)|={2m-1\choose {m-1}}
\]

middle sets containing `x`.  A Johnson edge of `F` lies wholly inside
`F_x` exactly when its intersection colour contains `x`.  Because every
rank-`m-1` intersection colour is used once,

\[
             |E(F_x)|={2m-1\choose {m-2}}.
\]

The induced subgraph is a forest, so its component count is the difference.
The binomial identity

\[
 {2m-1\choose {m-1}}-{2m-1\choose {m-2}}
 ={1\over m+1}{2m\choose m}=K
\]

proves the claim. \(\square\)

### Theorem 2.2 (seam identity)

Suppose `c` Johnson edges are added successively between endpoints of
different current path components, and the result remains a path forest.
Then its total number of coordinate runs is exactly

\[
                         2mK-(m-1)c.                 \tag{2.1}
\]

In particular, joining all `K` components into one Hamilton path gives

\[
                         (m+1)K+m-1                 \tag{2.2}
\]

runs.  Closing that path by one further Johnson edge gives, in the cyclic
sense,

\[
                         (m+1)K.                     \tag{2.3}
\]

#### Proof

A Johnson seam `XY` has `|X intersect Y|=m-1`.  For each coordinate in
`X intersect Y`, the seam joins the boundary run ending at `X` to the
boundary run ending at `Y`; these are distinct because the endpoints lie in
different current components.  Thus exactly `m-1` induced coordinate
components merge.  For the two exchanged coordinates only one endpoint
contains the coordinate, so no run merges.  Summing proves (2.1), and
substitution of `c=K-1` gives (2.2).

For the final cyclic edge, every common-coordinate boundary run at the two
ends merges.  No coordinate occupies every middle vertex, so the two end
runs cannot already be one cyclic all-vertex run.  This gives (2.3).
\(\square\)

### Corollary 2.3 (exact average)

Across all coordinates the total number of one-incidences is

\[
                       mM=m(m+1)K.
\]

Therefore a cyclic Catalan joining has average positive-run length exactly

\[
                       {m(m+1)K\over (m+1)K}=m.      \tag{2.4}
\]

For a Hamilton path the average is

\[
                 {m(m+1)K\over (m+1)K+m-1}=m-o(1). \tag{2.5}
\]

The flat compiler asks for internal run length at least `d+1`, where
`d=Theta(sqrt(m))`.  Thus aggregate run mass exceeds the residence floor by
a factor `Theta(sqrt(m))`.  This is only a capacity statement: (2.4) does
not prevent short runs from coexisting with compensating long runs.

## 3. The exact rethread target

Theorems 2.1--2.2 identify what an interior rethread must do.  It need not
create more residence mass; the mass and total seam credit are already
forced.  It must exchange palette-valid interior edges and seams so that the
fixed total run budget is redistributed from long runs to runs below
`d+1`, while retaining:

1. lower and upper immediate-shadow coverage;
2. a path or cyclic chronology;
3. the deeper flag tower; and
4. enough erosion-envelope incidence for the lower compiler.

A two-diamond alternating `C4` is the smallest exact exchange.  If matched
diamonds `(L1,U1),(L2,U2)` also satisfy `L1 subset U2` and `L2 subset U1`,
replace them by `(L1,U2),(L2,U1)`.  This preserves both immediate palettes.
After deleting the two old Johnson edges, the exchange preserves the
Catalan path-forest state exactly when the two new edges respect degree two
and their contracted attachment multigraph is loopless and acyclic.  Only
runs meeting the four cut ports can change.  Longer alternating circuits
give the corresponding multiport operation.

This is the residence analogue of the transparent-hex and common-core
linkage tests: exact local validity is finite, while uniform existence of a
sequence balancing all short runs remains open.

## 4. `m=5` calibration

For the synchronized repaired `m=5` forest,

\[
 M=252,\quad N=210,\quad K=42.
\]

The audit confirms `42` runs for every coordinate and `420` before joining.
The colour-injective 42-seam cyclic closure has exactly

\[
                        6\cdot42=252
\]

cyclic coordinate runs and average length `5`.  It nevertheless has `76`
runs of length one or two, compensated by longer runs.

The independently verified optimal `k=10` word has a depth-two carrier
which is a Hamilton path through all 252 middle sets.  Its total run count is

\[
                        6\cdot42+4=256,
\]

exactly (2.2), and it has no short **internal** run.  Its four short boundary
runs are legal for the linear erosion.  Hence the required distribution is
actually attainable at this dimension, although not by intact-path
reordering of the synchronized repaired forest.

An exact exploratory `C4/C6` rethread of that forest already reduces its 31
immutable internal defects to one while preserving the complete immediate
palettes and a 42-path forest.  This is evidence that the required move is
an interior palette exchange, not extra mass; it is not an all-`m` proof.

## 5. Scope

The run and seam identities are all-`m` theorems.  The existence of a
residence-balanced rethread, preservation of the deeper tower, and compiler
compatibility remain open.  The `m=5` mixed-circuit search is a candidate generator only
until its output is independently replayed.
