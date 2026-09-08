# Owner-once upper lifting: sharp K6 counterexample, K7 odd-rainbow no-go, and all-k clean-block bounds

Date: 2026-08-02  
Status: exact theorems, theorem-guided K6 construction, deterministic audit,
and arithmetic audit.  No general solver and no K17 solver were launched.

## 0. Outcome

There is no unconditional monotone upper-shadow theorem from owner-once,
immediate-palette completeness, and optimal positive residence alone.
The smallest possible counterexample is already `k=6,r=3`:

```text
7 11 41 37 21 22 50 35 19 26 56 49 25 13 44 42 14 28 52 38
```

is a simple cyclic Johnson ordering of all twenty rank-three owners.  All
fifteen rank-two intersections and all fifteen rank-four adjacent unions
occur, every positive coordinate run has length at least two, every rank-four
target is covered, but the rank-five target `31={0,1,2,3,4}` is missing.
Here `d(6)=1`, so the residence floor is exactly `d+1=2`.

This is the sharp even complete-with-repeats counterexample.  It is **not** an
odd middle-levels lower-rainbow object: twenty edges cover fifteen lower
facets with five repeated occurrences.

Under the intended odd-carrier interpretation, the smallest test is K7.  It
has the opposite answer.  A Hamilton cycle on all rank-four owners using
every rank-three intersection exactly once cannot cover all rank-five sets
while missing a rank-six set.  The proof is a two-line clean-block/facet
count and does not need residence.

More generally, exact lower-facet usage and depth-`d` residence give two
uniform upper bounds on the number of clean blocks of every target.  Combined
with an exact hole-transversal theorem, they yield a quantitative sufficient
condition under which completeness at rank `m`—in particular `m=r+4`—forces
every higher rank.

## 1. General clean-block notation

Let `F` be a simple Hamilton cycle through every rank-`r` subset of `[k]`
exactly once.  Fix `Y subset [k]`, `|Y|=t>r`.  A vertex is **Y-clean** when it
is contained in `Y`.  Deleting all dirty vertices cuts the Hamilton cycle
into `b_Y` maximal clean path blocks `B`.

Put

\[
              U_B=\bigcup_{u\in B}u,
              \qquad H_B=Y\setminus U_B.                \tag{1.1}
\]

The target `Y` is covered exactly when some `H_B` is empty.  When `Y` is
missing, all `H_B` are nonempty.  Let `tau(H_Y)` be the transversal number of
the hole hypergraph

\[
                         \mathcal H_Y=\{H_B:B\}.          \tag{1.2}
\]

## 2. Exact hole-transversal lifting

### Theorem 2.1 (clean-block shadow/transversal equivalence)

Assume `Y` is missing and let `m<t`.  The following are equivalent:

1. every `m`-subset of `Y` is contained in at least one block union `U_B`;
2. the union of the block `m`-shadows is complete,

   \[
                    \bigcup_B\binom{U_B}{m}=\binom{Y}{m};        \tag{2.1}
   \]

3. `tau(H_Y)>m`.

Consequently, if the carrier's literal interval deck covers every rank-`m`
target and misses `Y`, then

\[
                         \boxed{\tau(\mathcal H_Y)>m}.            \tag{2.2}
\]

#### Proof

An `m`-set `X subset Y` is contained in `U_B` exactly when
`X intersect H_B` is empty.  Thus `X` is absent from every block shadow
exactly when it hits every `H_B`.  There is such an `m`-set if and only if
there is a transversal of size at most `m`, since a smaller transversal can
be extended inside `Y` to size `m`.  This proves the equivalence.

If an interval has union `X`, every owner in the interval is contained in
`X`, hence lies in one Y-clean block, and therefore `X subset U_B`.  Global
rank-`m` completeness implies (2.1), giving (2.2). `QED`

### Corollary 2.2 (factor-specific upper-lifting condition)

Fix `m`.  Suppose that for every `Y` with `m<|Y|<k`, either

* one Y-clean block has union `Y`; or
* the nonempty hole family has transversal number at most `m`.

Then rank-`m` completeness forces every higher proper rank.  Rank `k` is
automatic from the union of the full owner chronology.

This is the exact clean-block expansion condition useful to a regenerative
construction.  It replaces all higher target automata by a bounded hole-
transversal certificate.  A simpler sufficient condition is

\[
                              b_Y\le m,                          \tag{2.3}
\]

because choosing one hole from every block gives a transversal of size at
most `b_Y`.

There is also a purely numerical shadow-capacity certificate:

\[
                 \sum_B\binom{|U_B|}{m}<\binom{t}{m}             \tag{2.4}
\]

implies that some rank-`m` target inside `Y` is absent unless `Y` itself is
already covered.

### Corollary 2.3 (one-rank lift)

If rank `t-1` is complete but a `t`-set `Y` is missing, then `tau(H_Y)=t`.
Equivalently, for every `y in Y` there is a distinct clean block with

\[
                             H_B=\{y\},\qquad U_B=Y-\{y\}.       \tag{2.5}
\]

In particular `b_Y>=t`.

#### Proof

Theorem 2.1 gives `tau>t-1`, while no hypergraph on `t` vertices has
transversal number greater than `t`.  A nonempty-set hypergraph has
transversal number `t` exactly when it contains every singleton edge: the
proper set `Y-{y}` fails to hit some edge only when that edge is `{y}`.
`QED`

## 3. Bounds supplied by the owner-once carrier

Assume now that `k=2r-1` and the lower q1 palette is occurrence-exact: the
`W=binom(k,r)=binom(k,r-1)` Hamilton edges use every rank-`r-1` facet exactly
once.

### Theorem 3.1 (exact-facet clean-block bound)

For every proper `t`-set `Y`,

\[
 b_Y\le \binom{t}{r-1}-\binom{t}{r}
     =\frac{k-t}{r}\binom{t}{r-1}.                       \tag{3.1}
\]

#### Proof

There are `binom(t,r)` clean owners.  Their `b_Y` path blocks contain
`binom(t,r)-b_Y` internal clean-clean edges and exactly `2b_Y` boundary
edges.  The intersection facet of every one of these edges lies inside `Y`.
Thus at least

\[
                         \binom{t}{r}+b_Y                 \tag{3.2}
\]

selected facets lie in `Y`.  Exact lower-facet usage permits only
`binom(t,r-1)` such facets.  Rearranging proves (3.1).  Dirty-dirty edges
whose facet also lies in `Y` only strengthen the inequality. `QED`

### Theorem 3.2 (residence clean-block bound)

If every positive coordinate run has length at least `d+1`, then

\[
              b_Y\le
              \left\lfloor\frac{W-\binom{t}{r}}{d+1}\right\rfloor.  \tag{3.3}
\]

#### Proof

Clean and dirty blocks alternate, so there are `b_Y` dirty blocks containing
the `W-binom(t,r)` dirty owners.  At the first owner of a dirty block, an
outside-Y coordinate is inserted.  Its positive run has at least `d+1`
owners, all still dirty.  Hence every dirty block has length at least `d+1`.
Summing their lengths gives (3.3). `QED`

### Corollary 3.3 (uniform numeric lifting criterion)

Let a lower-rainbow, depth-`d` owner Hamilton cycle cover every rank-`m`
target.  If for every `t=m+1,...,k-1`,

\[
 \min\left\{
     \binom{t}{r-1}-\binom{t}{r},
     \left\lfloor\frac{W-\binom{t}{r}}{d+1}\right\rfloor
 \right\}\le m,                                           \tag{3.4}
\]

then all higher ranks are covered.

For the Regenerative Shadow--Braid target, set `m=r+4`.  Condition (3.4) is
an all-k sufficient theorem; when its scalar bound is too weak, the exact
factor-specific replacement is the transversal condition of Corollary 2.2.

## 4. The sharp even K6 counterexample

For `k=6,r=3`,

\[
 W=20,\qquad \Lambda=\binom61+\binom62=21,
 \qquad d(6)=1.                                           \tag{4.1}
\]

Consider the cycle

\[
 (7,11,41,37,21,22,50,35,19,26,
  56,49,25,13,44,42,14,28,52,38).                         \tag{4.2}
\]

Direct replay proves:

* its twenty masks are exactly all rank-three owners, once each;
* consecutive masks differ by one Johnson swap, cyclically;
* the twenty intersections cover all fifteen rank-two targets;
* the twenty unions cover all fifteen rank-four targets;
* the shortest positive coordinate run has length two;
* the complete cyclic interval deck contains every rank-four target but not
  `Y=31`.

This is the smallest possible dimension: for `k<=5`, after the middle and q1
layers the next upper rank is already the full ground set, which the union of
the complete owner chronology necessarily covers.

### Why the finite search was exact and tiny

Relative to `Y`, there are ten clean and ten dirty owners.  Rank-four
completeness with `Y` missing requires at least five clean blocks by
Corollary 2.3.  Residence floor two permits at most five dirty blocks, so
there are exactly five of each.  Every dirty and clean block therefore has
length two.  Up to rotation the status pattern is forced to

```text
CC DD CC DD CC DD CC DD CC DD.
```

The stabilizer of `Y` is transitive on the first clean Johnson edge, so the
search fixed `7->11` and exhaustively backtracked only the remaining forced
pattern.  It found (4.2) after 4,797 nodes.  The proof of the result is the
separate deterministic replay, not trust in the search.

## 5. The K7 odd-rainbow no-go

Let `k=7,r=4`, and suppose all 35 rank-three intersection facets occur
exactly once.  Fix a six-set `Y`.  It contains

\[
                         \binom64=15                    \tag{5.1}
\]

clean owners and only

\[
                         \binom63=20                    \tag{5.2}
\]

available lower facets.

If every rank-five target is covered but `Y` is missing, Corollary 2.3 forces
at least six Y-clean blocks.  Theorem 3.1 instead gives

\[
                         b_Y\le20-15=5,                 \tag{5.3}
\]

a contradiction.  Therefore no owner-once exact-lower-rainbow K7 carrier can
be rank-five complete while missing rank six.  The statement remains true
without the depth-two residence assumption and without requiring upper q1
multiplicity restrictions beyond rank-five completeness.

K9 is the first odd dimension not decided by this scalar theorem.  For its
immediate `rank6 -> rank7` test, (3.1) gives `b_Y<=14`, while a miss requires
only seven blocks; residence gives the still weaker bound 35.  A K9 search
was therefore not launched: it would be a genuinely new construction
problem, not a justified continuation of the K7 finite case.

## 6. K17 implication and limitation

At K17, `r=9,d=3,m=r+4=13`.  The scalar bounds (3.4) are:

| target rank `t` | exact-facet bound | residence bound | combined |
|---:|---:|---:|---:|
| 14 | 1,001 | 5,577 | 1,001 |
| 15 | 1,430 | 4,826 | 1,430 |
| 16 | 1,430 | 3,217 | 1,430 |

They are far above thirteen, so owner-once, q1 exactness, and residence do
not automatically lift rank 13 to ranks 14--16 by scalar counting.  The
useful general replacement is exact and much sharper: for every missing
candidate `Y`, rank-13 completeness forces

\[
                         \tau(\mathcal H_Y)\ge14.        \tag{6.1}
\]

For rank 14 specifically, every one of the fourteen singleton holes must be
realized by a distinct clean block.  This gives a compact theorem-guided
audit/CEGAR target: search for a 13-element transversal of persistent block
holes.  Finding one certifies that some rank-13 target would be absent;
failure is the exact structural shape a rank-14 miss would require.

This does not prove that an owner-once K17 counterexample exists.  It proves
the smallest counterexample in the even complete-with-repeats class, rules
out the smallest odd exact-rainbow case, and isolates the precise additional
clean-block expansion property needed by a general Shadow--Braid theorem.

## 7. Artifacts

The theorem-guided K6 search and deterministic audit are:

```text
84e0b1a3fed0dc7a4214fe850e681f16353572eadefabffad2aed1264c7eb643
  scratch/search_k6_owner_once_q1_resident_upper_counterexample_20260802.cpp
0e619ab0f6ca60dfc6e0cad16c5b69e583be2b85e708903f2c282d04eb7a3dfe
  scratch/audit_k6_owner_once_q1_resident_upper_counterexample_20260802.cpp
```

The H100 deterministic replay returned

```text
PASS_K6_OWNER_ONCE_Q1_RESIDENT_UPPER_COUNTEREXAMPLE_AUDIT
owners=20 lower_q1_distinct=15 upper_q1_distinct=15
minimum_positive_run=2 rank4_complete=1 missing_rank5=31
```

The all-k arithmetic/K7 no-go audit is

```text
d5b4c2088a044e1c2dbae49549cb07f1dd6db302d668997e3ce78a6cc913a25c
  scratch/audit_owner_once_clean_block_lifting_bounds_20260802.cpp
```

and returned

```text
K7_EXACT_NO_GO required_blocks=6 facet_block_bound=5 residence_floor=3
PASS_OWNER_ONCE_CLEAN_BLOCK_LIFTING_BOUND_AUDIT
```
