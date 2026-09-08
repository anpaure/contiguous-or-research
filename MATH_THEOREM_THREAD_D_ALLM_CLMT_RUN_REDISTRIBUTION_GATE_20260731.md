# The all-`m` CLMT run-redistribution gate

Date: 2026-07-31  
Status: exact counting audit and exact finite reduction; no all-`m`
existence theorem

## 0. Verdict

The Catalan seam-run identity is correct, and it has a useful
coordinatewise strengthening.  If a Catalan path forest is closed by
Johnson seams, then for each coordinate `x`

\[
       R_x=\operatorname {Cat}_m-s_x,                 \tag{0.1}
\]

where `R_x` is the number of final cyclic positive `x`-runs and `s_x` is
the number of closing seams whose two endpoints both contain `x`.  More
precisely, the final runs are the weighted connected components of an
explicit **run-atom forest**.  This gives a necessary-and-sufficient
residence test for any fixed forest and connector chronology, not merely an
average.

There is also an exact all-`m` interior-rethread reduction.  The support of
every rethread must hit the closed edge interval of every inherited short
run.  This hitting number is an interval min-max quantity.  Once it is paid,
all new short runs are confined to inserted-edge collars.  Preserving both
immediate palettes is exactly a perfect matching in a deleted-colour
compatibility graph, but degree two, graphic acyclicity, and the collar
conditions remain simultaneous side constraints.  Thus Hall is exact for
the palette row and insufficient for the physical rethread.

For the central threshold `h=d+1=Theta(sqrt(m))`, the per-coordinate run
count has no scalar obstruction once `h <= (m+1)/2`.  The missing theorem is
an integral redistribution theorem in the alternating-diamond exchange
space, followed by a residence-safe connector chronology.  The exact
`m=5` interior rethread proves this can happen in one nontrivial dimension;
it does not prove the uniform statement.

## 1. Setup

Let `Omega` have size `2m` and put

\[
 M={2m\choose m},\qquad N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.                       \tag{1.1}
\]

Let `F` be a spanning path forest in `J(2m,m)` with `N` edges, using every
rank-`m-1` intersection colour and every rank-`m+1` union colour exactly
once.  For a coordinate `x`, the connected components of the induced
forest `F_x` are called the `x`-**run atoms**.  Give an atom `A` weight

\[
                         w(A)=|V(A)|.                \tag{1.2}
\]

The already-frozen seam-run theorem gives exactly `K` run atoms for each
coordinate.

Suppose Johnson seams are added between endpoints of distinct current
physical path components.  For each `x`, let `s_x` count the added seams
whose common rank-`m-1` intersection contains `x`.

## 2. Coordinatewise seam identity

### Theorem 2.1 (coordinatewise refinement)

After any such sequence of seams which leaves a path forest, the number of
`x`-runs is exactly

\[
                              K-s_x.                 \tag{2.1}
\]

If all `K` source components are joined to one Hamilton path and the last
Johnson seam closes that spanning path to one Hamilton cycle, (2.1) remains
true with the closing seam included in `s_x`.

#### Proof

Before joining there are `K` components in `F_x`.  A seam contributes to
`s_x` precisely when both endpoints contain `x`.  In that case it joins
two `x`-run atoms lying in distinct current physical components, hence
reduces their component count by one.  If either endpoint omits `x`, it
does not join two `x`-runs.

For the final cyclic seam, its two endpoint `x`-runs could already agree
only if the entire Hamilton path between the endpoints contained `x`.
The path is spanning, while some rank-`m` set omits `x`, so this is
impossible.  The final common-coordinate seam again performs one merge.
This proves (2.1). \(\square\)

Summing `s_x` over `x` counts `m-1` common coordinates per seam.  With `K`
cyclic seams,

\[
 \sum_x R_x=2mK-(m-1)K=(m+1)K,                     \tag{2.2}
\]

which recovers the global theorem.  The total positive mass of each
coordinate is `M/2`, and total mass is `mM`.

### Corollary 2.2 (the scalar coordinate test is eventually vacuous)

If every final cyclic positive run has length at least `h`, then necessarily

\[
                 h(K-s_x)\le {M\over2}              \tag{2.3}
\]

for every `x`.  If `h <= (m+1)/2`, this condition holds for every possible
seam-load vector, since `K-s_x <= K` and `M=(m+1)K`.

Thus at the intended `h=Theta(sqrt(m))`, neither the global average nor its
coordinatewise refinement supplies the missing existence theorem.  They
certify capacity only.

## 3. The exact run-atom criterion

Fix the forest `F` and a literal cyclic Johnson closure `C`.  For each
coordinate `x`, form a graph `A_x(F,C)` as follows.

1. Its vertices are the `K` run atoms of `F_x`, with weights (1.2).
2. For every connector seam in `C` whose endpoints contain `x`, join the
   two atoms containing those endpoints.

### Theorem 3.1 (weighted run-atom theorem)

Assume `C` closes `F` into one spanning Hamilton cycle.  Then the graph
`A_x(F,C)` is a forest.  Its connected components are in
weight-preserving bijection with the cyclic positive `x`-runs of the
closed chronology: the length of a final run equals the sum of the atom
weights in its component.  Consequently the closure is `h`-resident if
and only if

\[
       \sum_{A\in Q}w(A)\ge h                       \tag{3.1}
\]

for every connected component `Q` of every `A_x(F,C)`.

#### Proof

Inside a source path, maximal positive blocks are exactly the run atoms.
A connector concatenates two such blocks exactly for its common
coordinates, which is exactly the edge rule defining `A_x(F,C)`.  No other
seam changes `x`-adjacency.  Hence connected atom sets and final runs agree,
and weights add.

A cycle in `A_x(F,C)` would be a cyclic component of the subgraph of the
Hamilton cycle induced by owners containing `x`.  Since the Hamilton cycle
also contains an owner omitting `x`, every induced positive component is a
path, not a cycle.  Thus `A_x(F,C)` is a forest.  Condition (3.1) is now
exactly the minimum-run condition. \(\square\)

### Corollary 3.2 (intact-path obstruction)

Any run atom of weight below `h` which contains no endpoint of its physical
path is isolated in every connector graph `A_x(F,C)`.  Therefore no
permutation, reversal, or socket choice of the intact paths can make the
closure `h`-resident.

This is the conceptual form of the `m=5` obstruction in item 2183.  The new
`m=5` matching in item 2188 escapes it by changing 119 diamond partners:
it changes the run atoms themselves rather than merely joining them.

### Corollary 3.3 (exact connector cut rows)

Let `z_e` be the indicator of a candidate connector seam `e`.  For a fixed
coordinate `x`, and a run-atom set `S`, let `delta_x(S)` consist of those
candidate seams whose two endpoints contain `x` and whose two incident
`x`-atoms lie on opposite sides of `S`.  Then, subject to the endpoint and
topology rows which make the selected seams a literal cyclic closure,
`h`-residence is equivalent to

\[
       \sum_{e\in\delta_x(S)}z_e\ge1
       \quad\text{for every nonempty }S
       \text{ with }\sum_{A\in S}w(A)<h.            \tag{3.2}
\]

#### Proof

If a selected run-atom component has weight below `h`, take its vertex set
as `S`; no selected `x`-edge leaves it, so (3.2) fails.  Conversely, if
(3.2) fails, `S` is a union of selected run-atom components.  Since its
total weight is below `h`, at least one of those components has weight below
`h`.  Theorem 3.1 completes the equivalence. \(\square\)

Thus fixed-forest residence has an exact Benders separator: replay the
selected connector graph, and whenever a light component appears, emit its
row (3.2).  This is a weighted small-component cut system, not a scalar
seam-count constraint.

### Theorem 3.4 (literal linear residence cuts)

Let `Y` be any spanning linear forest on the middle owners.  For a coordinate
`x`, put

\[
 V_x=\{X:x\in X\}.
\]

For nonempty `S subset V_x`, let `i_x(S)` be the number of selected Johnson
edges with both endpoints in `S`, and let `t_x(S)` be the number of selected
edges with one endpoint in `S` and the other endpoint outside `V_x`.  Then
`Y` has no strictly internal positive `x`-run of length below `h` if and only
if

\[
             3i_x(S)+t_x(S)\le 3|S|-2              \tag{3.3}
\]

for every nonempty `S subset V_x` with `|S|<h`.

#### Proof

Let `c_x(S)` count selected edges from `S` to `V_x-S`, and let

\[
 \epsilon_Y(S)=\sum_{v\in S}(2-d_Y(v))
               =2|S|-2i_x(S)-c_x(S)-t_x(S).        \tag{3.4}
\]

Since `Y[V_x]` is a forest, `Y[V_x][S]` has
`kappa=|S|-i_x(S)` components.  The set `S` is exactly one complete
strictly internal `x`-run precisely when

\[
                    \kappa=1,\qquad c_x(S)=0,
                    \qquad\epsilon_Y(S)=0.          \tag{3.5}
\]

Consequently there is no such run on `S` precisely when

\[
                    \kappa+c_x(S)+\epsilon_Y(S)\ge2. \tag{3.6}
\]

Substitution of (3.4) and `kappa=|S|-i_x(S)` into (3.6) gives exactly
(3.3).  If a short internal run exists, take its full vertex set and (3.3)
fails.  Conversely, failure of (3.3) forces all three equalities in (3.5),
so it exposes a short internal run. \(\square\)

The coefficients in (3.3) are literal selected-edge coefficients.  Thus
unlike the run-atom rows (3.2), these cuts may be installed before the
forest or its path components are known.

### Corollary 3.5 (no fractional residence obstruction)

Let

\[
                         D={m+1\choose2}.
\]

Give every edge of the rank-`m-1`/rank-`m+1` diamond inclusion graph weight
`1/D`, and lift it to its physical Johnson edge.  This is the uniform
fractional perfect matching on both immediate palettes.  For `|S|=s<=m`,

\[
 i_x(S)\le {\binom{s}{2}\over D},\qquad
 t_x(S)={ms\over D}={2s\over m+1}.                 \tag{3.7}
\]

Hence, for `m>=2`,

\[
 3i_x(S)+t_x(S)
 \le {3s(s-1)\over m(m+1)}+{2s\over m+1}
 \le 3s-2.                                          \tag{3.8}
\]

The same point gives fractional middle-owner degree
`m^2/D=2m/(m+1)<2`.  Therefore every internal-run residence cut (3.3) with
`h<=m+1`, including `h=Theta(sqrt(m))`, and every degree-two row is
fractionally feasible together with both immediate palette equations.
This is not an integral forest theorem: graphic acyclicity, deep flags and
connector chronology still have to be correlated with one integral
matching.

## 4. All-`m` support min-max for an interior rethread

Let `h >= 2`.  On an oriented source path, an internal positive coordinate
run of length `ell<h` has trace

\[
                         0\,1^{\ell}\,0.             \tag{4.1}
\]

Its **closed span** is the interval of the `ell+1` source edges between the
two displayed zero vertices.  Let `B_h(F)` be the family of all such spans,
on all source paths and coordinates, and let `tau_h(F)` be the minimum
number of source edges meeting every span.

### Theorem 4.1 (run-span min-max)

Every fragment rethread which retains undeleted source fragments intact up
to reversal and eliminates all inherited internal runs of length below `h`
deletes at least

\[
 \tau_h(F)=\max\{|Q|:Q\subseteq B_h(F)
             \text{ consists of pairwise edge-disjoint spans}\}.       \tag{4.2}
\]

Both sides split additively over the source paths and are obtained by the
earliest-right-endpoint greedy algorithm.

#### Proof

If a closed span is uncut, all vertices in (4.1) remain consecutive in one
retained fragment.  Reversal fixes the pattern, so the bad run survives.
Thus every rethread support is a transversal of `B_h(F)`.

On one source path the closed spans are intervals on a line.  The standard
earliest-right-endpoint algorithm simultaneously produces a hitting set
and a family of pairwise disjoint intervals of the same size.  Different
source paths have disjoint edge grounds, so the equality adds over paths.
\(\square\)

### Theorem 4.2 (collar localization after hitting)

Let `R` meet every span in `B_h(F)`, and reconnect the resulting maximal
fragments by arbitrary new edges.  Then every internal positive run of
length below `h` in the new path forest crosses at least one inserted edge.
Hence residence is necessary and sufficient to reject every factor

\[
                         0\,1^{\ell}\,0,
             \qquad 1\le\ell<h,                    \tag{4.3}
\]

whose support crosses an inserted-edge collar.  A collar containing the
last `h+1` vertices on the left and first `h+1` on the right is sufficient;
equivalently one may compose the capped prefix/suffix run monoid.

#### Proof

A bad run wholly inside one retained fragment would be an old bad run whose
closed span contains no deleted edge, contrary to the hitting hypothesis.
Thus it crosses an inserted edge.  Pattern (4.3) has at most `h+1` vertices,
so it lies in the stated collar of any inserted edge it crosses.  Literal
avoidance of all such patterns is plainly sufficient. \(\square\)

## 5. Exact palette-preserving exchange theorem

For a Johnson edge `e`, write

\[
             \lambda(e)=X\cap Y,\qquad
             \upsilon(e)=X\cup Y.                   \tag{5.1}
\]

Let `R` be a prescribed set of simple source edges, required below to be the
actual support `R=F-F'` of the rethread.  Form
the bipartite graph `B_R` with a left and a right copy of `R`, and put an
edge from left `e` to right `f` when

\[
                    \lambda(e)\subset\upsilon(f).   \tag{5.2}
\]

The pair determines a unique physical Johnson edge, denoted `a(e,f)`.

### Theorem 5.1 (all-`m` rethread criterion)

There is a Catalan path forest `F'` which differs from `F` exactly on `R`,
uses the same complete lower and upper immediate palettes, and has no
internal positive run shorter than `h`, if and only if one can select a
perfect matching `sigma` in `B_R`, with no fixed point, such that:

1. `R` hits every span in `B_h(F)`;
2. in
   \[
          F'=(F-R)\cup\{a(e,\sigma(e)):e\in R\},    \tag{5.3}
   \]
   every middle owner has degree at most two;
3. `F'` is acyclic; and
4. every inserted-edge collar satisfies (4.3).

When these conditions hold, `F'` has exactly `K` path components.

#### Proof

Every removed lower colour and every removed upper colour must be restored
once.  A lower/upper pair has a physical lift exactly when (5.2) holds, and
that lift is unique.  Thus palette restitution is exactly a perfect
matching; a fixed point reinserts an allegedly removed edge and contradicts
exact support.

Conditions 2 and 3 say that (5.3) is a linear forest.  It has the same `N`
edges on the same `M` owners as `F`, hence exactly `M-N=K` components.
Theorem 4.1 gives condition 1, and Theorem 4.2 makes condition 4 necessary
and sufficient for internal residence.  Reversing the argument proves
sufficiency. \(\square\)

After Theorem 5.1, a cyclic closure is residence-safe exactly when its
connector run-atom forests satisfy Theorem 3.1.  Thus Theorems 3.1 and 5.1
together are an exact, noncircular reduction of run redistribution to
finite matching, graphic, and weighted-connector data.

## 6. Where Hall stops

For fixed exact support `R`, delete the diagonal pairs and write

\[
                  B_R^-=B_R-\{(e,e):e\in R\}.       \tag{6.1}
\]

Hall's inequalities in `B_R^-` are necessary and sufficient for the
palette matching `sigma`.  Using `B_R` itself would allow a fixed point and
therefore a smaller actual support.  Hall says nothing about the physical
rows 2--4 of Theorem 5.1.  On candidate pairs `(e,f)`, those rows are:

* middle-owner degree capacities;
* independence in the graphic matroid after contracting `F-R`; and
* forbidden collar patterns coupled across the selected physical edges.

This natural master matrix is not uniformly a network/TU matrix.  For
`m>=3`, even before residence, three middle-capacity rows and three available
diamond columns over one fixed lower set can contain

\[
\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},  \tag{6.2}
\]

whose determinant has absolute value two.  This proves non-TU for the
unrestricted matrix class; it does not assert that every fixed support `R`
contains this minor or exhibit an LP integrality gap.  Palette matching,
owner cap two, and graphic independence therefore remain an
integral-correlation problem, not one bipartite matching or one matroid
intersection supplied for free.

There is a useful fixed-forest special case.  If no physical path component
is all-one in any coordinate, then a final positive run crosses at most one
connector seam.  For fixed path orientations, label a directed endpoint
seam `P->Q` safe when, coordinate by coordinate,

* a `1->0` seam leaves the suffix run of `P` of length at least `h`;
* a `0->1` seam leaves the prefix run of `Q` of length at least `h`; and
* a `1->1` seam has suffix-plus-prefix length at least `h`.

Assuming all internal runs are already safe, a cyclic ordering is resident
if and only if every chosen arc is safe.  A safe cycle cover is then exactly
a bipartite perfect matching and has a Hall characterization; requiring one
cycle still adds the usual subtour/connectedness row.  Components which are
all-one in some coordinate require the full associative run-state or the
run-atom criterion of Theorem 3.1, because a run may cross several seams.

## 7. Consequences for the current recursive target

The correct uniform object is not a bounded number of alternating switches.
The exact `m=5` rethread changes 119 partners and its alternating-cycle
half-lengths range from 2 through 9.  What can remain bounded is the live
interface:

1. exposed short-run spans not yet hit;
2. unmatched lower/upper palette ports;
3. residual owner capacities and the contracted graphic partition;
4. capped coordinate prefix/suffix run states; and
5. connector run-atom debts of weight below `h`.

A controlled-debt packet may use a growing number of internal alternating
circuits provided those five boundary ledgers stay bounded and terminate at
zero.  Only after that terminal state is reached may a fixed-decoration
transparent gluing list be frozen.  Freezing the decoration before the
interior rethread is impossible in general because one lower/upper colour
pair determines its Johnson edge uniquely.

For `m=5`, the residence-clean matching proves that the interior part of
this target is attainable.  Exact endpoint replay now finds fourteen
endpoint-locked components (and, more locally, one component with two dead
pair-safe sockets), so no ordering/reversal with endpoint-only Johnson seams
can make that fixed 42-path forest resident.  Its 21 deeper-target debts are
therefore downstream of an empty fixed-body connector face.  The next
interior rethread must control exposed run rays as well as internal runs.
No all-`m` supply theorem, deep-flag preservation theorem, or compiler
theorem follows from the run average or from Theorem 5.1.

## 8. Audit scope

The exact identities audited here are those in

```text
MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md
```

with frozen SHA-256 values

```text
e1e0ddae1289a91d6912e07e0b1e1ca7f2728eb1640e7f3c6e08b18d48e96d48
dcb9b98e02580202f6dc94eaa4c3c009afe1c0638feab48a31bdf9f3e6c9d82e
```

The `m=5` finite certificate remains independently replayed by

```text
scratch/audit_catalan_m5_residence_rethread_c4c6_20260731.py
scratch/catalan_m5_residence_rethread_c4c6_20260731.audit.json
```

with SHA-256 values

```text
a68afdee13ac848475c92103ea0722ac645ff8753ee7f3f1d339c7a92d8bb3f6
809482ac99912194526ff30628ebbfe77c0493f8ed7d1062b67e433fec989151
```

The frozen JSON's `canonical_payload_sha256` predates JSON-roundtrip
canonicalization of integer histogram keys.  Its whole-file SHA above is
authoritative; replaying the payload field requires restoring those histogram
keys to integers before sorted serialization.

Only the final `m=5` matching and its symmetric-difference cycle profile are
used here.  No accepted `C4/C6` move trace is frozen, so no claim about
physical linearity at every intermediate search move is imported.

The fixed-body endpoint obstruction is independently replayed by

```text
MATH_THEOREM_AD_RESIDENCE_REDISTRIBUTION_AUTOMATON_AND_M5_ENDPOINT_LOCK_20260731.md
scratch/audit_ad_m5_residence_clean_triple_endpoint_obstruction_20260731.py
scratch/ad_m5_residence_clean_triple_endpoint_obstruction_20260731.audit.json
```

No search, asymptotic existence claim, or compiler claim is made in this
note.
