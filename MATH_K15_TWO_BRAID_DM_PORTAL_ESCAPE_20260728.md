# `k=15`: two-braid escape from the Hall-25 local minimum

## 1. Result

The Hall-25 carrier is an exact one-move local minimum for every resident,
upper-safe `FF/RF/FR/RR` three-cut segment braid.  It is **not** a local
minimum for compositions of two such moves.

Relative to the Hall-25 state, apply

\[
\operatorname{FR}(1512,2458,4103)
\quad\text{and then}\quad
\operatorname{FR}(2664,3491,6201).
\]

The exact score sequence is

\[
                         H25\longrightarrow H25\longrightarrow H24.
\]

The intermediate state is a genuinely neutral portal move, not an identity.
The second move converts that portal into one additional matched lower target.

The same mechanism repeats immediately from Hall 24:

\[
 H24\xrightarrow{\operatorname{FF}(212,3732,4717)}H24
 \xrightarrow{\operatorname{FF}(210,1501,4867)}H23.
\]

It repeats a third time:

\[
 H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23
 \xrightarrow{\operatorname{FR}(740,4051,6137)}H22.
\]

Canonical artifacts:

* `scratch/k15_segment_braid_hall25_portal.json`;
* `scratch/k15_segment_braid_hall24.json`;
* `scratch/k15_segment_braid_hall24_portal.json`;
* `scratch/k15_segment_braid_hall23.json`;
* `scratch/k15_segment_braid_hall23_portal.json`;
* `scratch/k15_segment_braid_hall22.json`;
* `scratch/audit_k15_segment_braid_descent.py`.

## 2. Exact audit

At both the intermediate and final states:

* all `6435` rank-eight masks occur exactly once;
* every consecutive pair is Johnson-adjacent;
* depth-three residence has zero defects;
* maximal erosion is nonempty and satisfies `D^3 A=T`;
* every upper shadow at depths `q=1,...,7` is complete;
* the immediate-lower support still has exactly four holes.

At the Hall-24 state:

\[
\operatorname{defHall}=24,\qquad
z=7,\qquad
(\text{unmatched rank }6,\text{unmatched rank }7)=(5,19).
\]

The seven degree-zero targets remain

\[
2575,5801,13616,13620,17738,21641,29776.
\]

Thus this move pays one unit of the nonzero-degree Hall obstruction; it does
not yet attack the zero-target floor.

The Hall-23 state has the same seven zeros and four immediate-lower holes,
with unmatched-rank profile `(rank 6,rank 7)=(5,18)`.
The Hall-22 state again preserves them and has profile `(5,17)`.

## 3. Dulmage--Mendelsohn mechanism

Let `A25` be the canonical Hall-25 shore of the starting graph.  Independent
full-graph reconstruction gives its exact gap through the two moves as

\[
                         25\longrightarrow22\longrightarrow21.
\]

After the first move, another shore still has gap 25, so the total Hall score
does not change.  The first braid therefore opens a true portal into the old
persistent core while relocating the maximum obstruction.  The second braid
discharges the replacement shore and lowers the global maximum to 24.

More precisely, if `A0,A1,A2` are the canonical DM shores of the starting,
portal, and final graphs, their exact cross-gap matrix is

\[
 \begin{pmatrix}
 25&24&23\\
 22&25&24\\
 21&24&24
 \end{pmatrix}.
\]

In the common-core contraction, the two boundary-rank changes are

\[
                         15\to15,qquad20\to21.
\]

This proves the structural point:

> A neutral braid can be mathematically necessary.  Monotone greedy Hall
> descent is incomplete even inside the same exact three-cut move family.

The `24 -> 24 -> 23` escape is cleaner still: it removes the whole `161/160`
DM component rooted at rank-four mask `20516`, without adding any replacement
DM target.  The neutral braid regroups two cell shores inside that component;
the second braid refines them into two extra usable cells, raising its matching
rank from `160` to `161`.  All masks in the component share core `20516`, and
the optional bits form a small Boolean diamond.  This is the first exact
instance of a reusable **component-root diamond refinement** mechanism.

The `23 -> 23 -> 22` pair discharges the small `2/1` DM circuit
`{4877,4909}`.  Thus the bounded-lookahead mechanism is not limited to the
large rank-four-root components: it can add a transversal-matroid ear to a
small deficient circuit as well.

The two stages are cleanly separated in this example.  The neutral first
braid performs a Boolean packet rotation inside the unrelated large component
rooted at `24610`, without changing that component's rank.  Its purpose is to
reroute the global chronology.  The improving second braid makes no cell-shore
change at root `24610`; remotely, it replaces the single shared shore
`{4877,4909}` by the two singleton shores `{4877}` and `{4909}`.  Hence the
repeatable architecture is

\[
\boxed{\text{neutral legality router}\quad+\quad
       \text{local DM-circuit splitter}.}
\]

This is stronger than requiring the router and discharged component to be the
same: the neutral exchange group can potentially position a splitter for any
remaining circuit.

### Circuit-ear lemma

Let a positive DM component have target shore `L`, physical-cell shore `R`,
`|L|=|R|+1`, and suppose `L` is a circuit of the compiler transversal
matroid—equivalently, `L-{x}` is matchable into `R` for every `x in L`.
If an exchange retains all cells of `R` and creates one new cell adjacent to
some `x in L`, then the component becomes perfectly matchable: match `x` to
the new cell and use the matching of `L-{x}` into `R`.

This elementary ear lemma explains why one genuinely new independent cell is
enough.  A braid generally deletes cells as well as adding them, so its neutral
first stage is a basis rotation which arranges that the improving stage's
deletions are replaceable.  The Hall-24-to-23 pair is exactly such a
rotation followed by a one-cell ear extension.

Consequently a general Shadow--Braid descent theorem must work on the graph of
DM shores (or allow bounded lookahead), rather than demanding an improving
outgoing edge at every carrier.

## 4. Separate Pareto escape

There is also an independently audited two-braid path

\[
(25,7)\to(26,6)\to(25,6)
\]

for the lexicographic pair `(Hall deficiency, zero-candidate targets)`:

\[
\operatorname{FR}(2396,4635,5353),qquad
\operatorname{FF}(2125,4140,6201).
\]

It gives target `2575` its first physical candidate and retains it after the
Hall score is restored.  Its artifacts are

* `scratch/k15_segment_braid_hall26_zero6.json`;
* `scratch/k15_segment_braid_hall25_zero6.json`.

This second escape is complementary to Hall 24: the Hall-24 branch reduces
matching deficiency while retaining seven zeros; the Pareto branch reduces
the zero floor while retaining Hall 25.  A successful continuation should
combine these two effects.

That combination is now achieved at Hall 22.  From the Hall-22/seven-zero
state,

\[
(22,7)\xrightarrow{\operatorname{FF}(882,2606,3222)}(23,6)
\xrightarrow{\operatorname{RF}(1500,4943,6184)}(22,6).
\]

The first move is the unique one-braid Pareto bridge reducing the zero count;
the second is the unique return to Hall 22 with six zeros in its exhaustive
neighbourhood.  The resulting canonical artifact is
`scratch/k15_segment_braid_hall22_zero6.json`.  Thus Hall descent and
zero-target descent are no longer separate branches.

In DM form, the former isolated `1/0` zero component `{2575}` becomes the
`2/1` circuit `{2575,2607}`.  Therefore the zero repair has an exact two-stage
normal form:

\[
\boxed{\text{first-cell creator: }1/0\to2/1
       \quad\text{followed by}\quad
       \text{circuit splitter: }2/1\to0.}
\]

The first stage removes the degree-zero obstruction without yet changing
Hall deficiency.  A legal splitter of the new shared cell would simultaneously
produce Hall 21 and retain six zeros.

Its canonical DM shore has sizes `1006/984`.  All `984` right cells have
pairwise distinct native traces, every native trace is an adjacent target in
that shore, and the one maximal erosion word realizes all of them
simultaneously.  Therefore the literal common-`Q_x` gap on the critical shore
is exactly `22`, equal to Hall deficiency.  This is verified independently by
`scratch/audit_k15_dm_native_current.py`.  It does not yet lift an arbitrary
global maximum matching outside the critical shore.

## 5. Remaining caveat

Hall 22 is an outer target/cell matching statement for maximal erosion, not a
length-6438 word.  The cumulative endpoint audit realizes 1146 simultaneous
pins on the former 1168-target H24 critical shore, missing exactly the 22
current roots, but it is not a global 16361-pin matching lift.  Hall must
reach zero and the selected exterior pins must satisfy the same common-`Q_x`
criterion.  Neither condition is yet proved.  The exact regenerative
groupoid theorem and the two-colour H22 port classification are in
`THREAD_D_H22_NEUTRAL_ROUTER_CIRCUIT_SPLITTER_THEOREM_20260728.md`.
