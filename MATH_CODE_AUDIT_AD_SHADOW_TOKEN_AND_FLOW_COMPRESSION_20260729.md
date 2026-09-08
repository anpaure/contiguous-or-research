# AD code/mathematics audit: shadow tokens, exact scope, and flow compression

Date: 2026-07-29

## 1. Frozen source and scope

This report independently audits the compact lower/upper shadow constraints
in

```text
scratch/graded_quotient_pipeline.py
```

without editing that core file, invoking a solver, or running a search.  The
reported `86`-cut model statistics belong to the snapshot read at
`2026-07-29T00:56:20+0500`, size `62382`, SHA-256

```text
ec0cc8e5f2b427d26b935cd890f207a9fd91f6c74d28b52b1c2afa525972d946.
```

During the audit the shared file changed to size `62555`, mtime
`2026-07-29T01:02:08+0500`, SHA-256

```text
3ad43459b8661feaa1936fe081ae523d422ebe57395e8d5c4c8dc820edb329b8.
```

The latter snapshot implements the defect-token formulation proved below.
The shared file then acquired unrelated cycle-cover, sparse-erosion, and
partial-hint work.  The last snapshot frozen by this audit is size `68960`,
mtime `2026-07-29T01:15:52+0500`, SHA-256

```text
e9aa47eaaf0c7d1194f28c47eb4ebe7f1b646ed90c656a8f6e37a124ef9232ef.
```

Its compact-shadow code is semantically unchanged from `3ad43459...`.
The audit corrections were then incorporated concurrently into the shared
core.  The final implementation snapshot audited here is size `73281`, mtime
`2026-07-29T01:22:43+0500`, SHA-256

```text
5d0f0fb2f0d369b73e914fdb121801229c37885c9364f1616b4ff48776450926.
```

It retains the token block, fails closed on directed-arc nonuniqueness, and
implements the exact unrestricted-upper reachability cut of Section 6.
All quoted old line ranges and the `49,309 / 460,437` reconstruction refer
to the frozen `ec0cc8e...` snapshot.  I made none of these core changes.  An
even earlier live read showed a transient `if b == a: continue` in
`cover_upper_q2`; it had disappeared by the frozen snapshot.  No hash of
that transient state was captured, so no claim about its provenance is made.

## 2. Exact local state-path theorem

Let `k=2r-1` be odd.  Let the selected directed quotient arcs lift to one
directed physical carrier on the rank-`r` masks.  Fix `1 <= q <= r-1`.

For a lower target

\[
 S\in\binom{[k]}{r-q},
\]

put

\[
 \mathcal V^-_S=\{X\in\tbinom{[k]}r:S\subseteq X\}.
\]

For an upper target

\[
 U\in\binom{[k]}{r+q},
\]

put

\[
 \mathcal V^+_U=\{X\in\tbinom Ur\}.
\]

### Theorem 2.1 (fixed-length shadow-state-path equivalence)

For lower mode, the `shadow-state-path` constraint is feasible exactly when
the selected physical carrier contains consecutive states

\[
 X_0\longrightarrow X_1\longrightarrow\cdots\longrightarrow X_q,
 \qquad X_j\in\mathcal V^-_S,
\]

with

\[
 \bigcap_{j=0}^qX_j=S.                                      \tag{2.1}
\]

For upper mode it is feasible exactly when it contains such a `q`-edge path
inside `\mathcal V^+_U` with

\[
 \bigcup_{j=0}^qX_j=U.                                      \tag{2.2}
\]

#### Proof

The state builder in frozen lines 526--588 enumerates precisely the physical
central supersets of `S`, respectively the physical central subsets of `U`.
For every retained non-self-loop directed Johnson edge between two enumerated
states it records the unique directed quotient arc whose rotation orbit
contains that physical edge.  Quotient self-loops are absent because they
cannot lie on a quotient Hamilton circuit with more than one quotient vertex.

Frozen lines 1252--1275 use the same transition table at each of the `q`
steps and require its recorded quotient arc variable to equal one.  Adjacent
table rows share the literal physical state variable, so these are physically
composable edges, not merely compatible quotient endpoints.  Since the
selected lift is functional, they are consecutive carrier edges.

In lower mode every state already contains `S`; frozen lines 1276--1297 say
that every coordinate outside `S` is absent from at least one state.  This is
equivalent to (2.1).  In upper mode every state is already a subset of `U`;
lines 1281--1301 say every coordinate of `U` is present in at least one
state.  This is equivalent to (2.2).  Conversely, a physical witness assigns
its literal states and unique directed quotient arcs and satisfies every
table, `Element`, and coordinate clause.  QED.

No independent phase variable is missing: the state domain consists of
physical masks, hence includes phase.  Simultaneously rotating every state
leaves the quotient arc label unchanged.  Since `gcd(k,r)=1`, the central
rotation action is free and the oriented arc normalization is unique.

### Exact generic table sizes

Before strict quotient self-loop rows are removed,

\[
 \begin{array}{c|c|c}
 &\text{states}&\text{directed transition rows}\\ \hline
 \text{lower }q&
 \binom{r+q-1}{q}&
 \binom{r+q-1}{q}\,q(r-1)\\[2mm]
 \text{upper }q&
 \binom{r+q}{q}&
 \binom{r+q}{q}\,rq.
 \end{array}                                                \tag{2.3}
\]

Indeed a lower state chooses its `q` extras from `r+q-1` coordinates, then
a preserving Johnson step deletes one of those `q` extras and inserts one of
the `r-1` absent coordinates.  An upper state is an `r`-subset of an
`(r+q)`-set; a preserving step deletes one of `r` present and inserts one of
`q` absent coordinates.

Thus the local construction is a valid polynomial-size encoding for every
fixed `q`.  This statement is about an exact `q`-edge witness.  Section 3
separates that local statement from unrestricted upper intervals.

## 3. The upper semantic boundary

The lower checker at frozen lines 383--391 asks for exactly `q+1`
consecutive states, so Theorem 2.1 matches it exactly.

The upper checker at lines 393--407 instead accepts the union of an interval
of any length.  A local `q`-edge witness is always sufficient, but need not
be necessary.

### Theorem 3.1 (upper q2 shortening)

If a Johnson path of rank-`r` subsets of an `(r+2)`-set `U` has union `U`,
then three consecutive states already have union `U`.

#### Proof

Choose a shortest subinterval `X_0,...,X_l` with union `U`.  Minimality gives
a coordinate `x` occurring only at the left endpoint within this interval
and a coordinate `y` occurring only at the right endpoint.  Every interior
state is therefore an `r`-subset of `U\{x,y}`, an `r`-set, so every interior
state equals `U\{x,y}`.  Consecutive carrier states are distinct.  Hence
there is at most one interior state and `l<=2`.  Two adjacent rank-`r`
Johnson neighbours have union rank `r+1`, so `l=2`.  QED.

Therefore upper q2 local state paths are exact cuts for the arbitrary-length
`upper_missing` semantics.

### Proposition 3.2 (upper q3 and all q>=3 do not shorten)

For every `q>=3` and `r>=q+1`, there is a Johnson path of rank-`r` subsets
of an `(r+q)`-set whose full union is the target but no `q+1` consecutive
states have that union.

#### Proof by an explicit family

Choose a common set `C` of size `r-2` and active symbols

\[
 1,2,3,\ldots,q+2.
\]

Use the active pairs

\[
 \{1,2\},\{2,3\},\{2,4\},\ldots,\{2,q+1\},
 \{3,q+1\},\{3,q+2\},                                  \tag{3.1}
\]

and adjoin `C` to every pair.  Consecutive states are Johnson neighbours.
Their full union is `C \cup \{1,\ldots,q+2\}`, of rank `r+q`.  Every window
ending before the last state misses `q+2`; the only `q+1`-state window ending
at the last state starts after the first state and misses `1`.  QED.

Thus an abstract Johnson interval need not shorten at any `q>=3`.  This
alone does not prove that every such path embeds in the restricted strict
equivariant Hamilton-carrier class.  The frozen strict-carrier example below
does prove the actual model mismatch at q3.  Consequently the former upper-
q3 short-path row is a positive-sound search strengthening, not a generic
validity-preserving cut for arbitrary upper coverage.  A positive solution
is still valid because
the final `upper_missing` audit is independent.  UNSAT after installing an
upper-q3 short-path cut applies only to the strengthened model.  The generic
“upper dual is exact at every q” statement is correct only after “upper
shadow” is defined to mean an exact `q`-edge witness.

There is no abstract Johnson-path length bound depending only on `q`: for
q3, take
`U=V\cup\{x,y\}` with `|V|=r+1`, make `x` private to the first state and
`y` private to the last, and traverse arbitrarily many distinct `r`-subsets
of `V` between them.  The interior Johnson graph `J(r+1,r)` is complete, so
the unique full-union interval in this simple path can have order `r` edges.
No strict-equivariant Hamilton extension of this whole family is asserted.

The obstruction occurs inside the frozen strict carrier itself.  The
voltage-one cycle reconstructed from

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

has physical-cycle SHA-256
`b6c231aa269791db4a5457f5dc32d25f0017495418d17984236357ae6f9e0bda`.
At cyclic position 102 it contains

```text
30264, 29242, 29214, 29230, 23086.
```

These five rank-eight states are all contained in the rank-eleven mask
`32318`, their union is `32318`, and its canonical representative is `4031`.
The two four-state unions are only `30270` and `31294`, both of rank ten.
An independent whole-cycle scan proves that target orbits `4031`, `7675`,
and `12155` each have minimum upper witness length four edges, with no
three-edge witness.  Each minimum is attained at the fifteen equivariant
translates.  Thus the semantic mismatch is present in a genuine selected
strict Hamilton lift, not merely an abstract Johnson graph.

There is nevertheless a useful rank-dependent bound.

### Theorem 3.3 (shortest unrestricted upper-witness bound)

Let `H_0,...,H_l` be the q-element hole sets of a shortest carrier interval
whose union is a proper rank-`r+q` target.  For `q>=2`,

\[
 q\le l\le \binom{r+q-2}{q-2}+1.                    \tag{3.2}
\]

#### Proof

Each Johnson step can remove at most one coordinate from the running hole
intersection, so at least `q` edges are necessary.  By shortestness,
`intersection(H_0,...,H_{l-1})` and `intersection(H_1,...,H_l)` are both
nonempty.  Choose `a` in the first and `b` in the second.  Empty total
intersection gives `a notin H_l`, `b notin H_0`, and `a!=b`.  Every interior
hole set `H_1,...,H_{l-1}` therefore contains `{a,b}`.  The physical carrier
is Hamilton and the target is proper, so these interior states, hence their
hole sets, are distinct.  There are only `binom(r+q-2,q-2)` q-sets containing
`{a,b}`.  Hence `l-1` is at most that number.  QED.

For q2 this forces `l=2`, recovering Theorem 3.1.  For k15 upper q3 it gives
the proved safe finite horizon `3<=l<=10`, rather than the false horizon
three or the much looser 164-edge all-state bound.  No sharpness claim is
made for the upper endpoint when `q>=3`.

## 4. Exact defect-token compression at every fixed q

The coordinate-history matrix in the frozen implementation is unnecessary
for the local fixed-length problem.  Importantly, an endpoint-distance test
is **not** equivalent: a coordinate can be deleted and later reinserted.
For example the extra pairs

\[
 \{a,b\}\to\{b,c\}\to\{c,a\}
\]

have empty three-way intersection but overlapping endpoints.  The correct
certificate records transition tokens.

### Theorem 4.1 (lower distinct-deletion certificate)

Let `X_0->...->X_q` be a Johnson path in `\mathcal V^-_S`, and let `d_j` be
the physical coordinate deleted on step `j`.  Then

\[
 \bigcap_{j=0}^qX_j=S
\]

if and only if the `d_j` are pairwise distinct and every `d_j` belongs to
`X_0\S`.

#### Proof

The initial state has exactly `q` extras `X_0\S`.  Such an extra survives
the full intersection exactly when it is never deleted.  There are exactly
`q` transition deletions.  Hence all initial extras are deleted at least
once exactly when the `q` deleted coordinates are distinct members of the
q-set `X_0\S`.  QED.

### Theorem 4.2 (upper distinct-insertion certificate)

Let `X_0->...->X_q` be a Johnson path in `\mathcal V^+_U`, and let `a_j` be
the physical coordinate inserted on step `j`.  Then

\[
 \bigcup_{j=0}^qX_j=U
\]

if and only if the `a_j` are pairwise distinct and every `a_j` belongs to
`U\X_0`.

#### Proof

The initial state misses exactly the `q` coordinates of `U\X_0`.  The union
acquires a missing coordinate precisely when some transition inserts it.
There are exactly `q` insertions, so all missing coordinates enter exactly
when the insertion tokens are distinct members of that q-set.  QED.

### CP-SAT formulation

Augment each transition row to

```text
(source state, target state, selected quotient arc, physical defect token),
```

where the token is the physical deleted coordinate in lower mode and the
physical inserted coordinate in upper mode.  Add `q` token variables, one
`AllDifferent`, and for each token one allowed-pair table with `state_0`
saying that the token belongs to the initial defect set.

This uses

\[
 (q+1)+q+q=3q+1                                      \tag{4.1}
\]

auxiliary integer variables per target and `3q+1` high-level constraints.
For q2/q3, a one-table alternative lists

```text
(state_0, token_1, ..., token_q)
```

for every permutation of the state's q-element defect.  It has
`n q!` rows and reduces the high-level constraint count to `2q+1`, while
using the same variables.  The `AllDifferent` version avoids factorial
growth and is preferable for arbitrary fixed q.

The token must be computed in the physical frame from
`source & ~target` or `target & ~source`.  The normalized source/target-frame
coordinates stored in the quotient `arc_data` tuple cannot be copied without
phase conversion.

## 5. Exact reconstruction of the 86-cut model counts

At `k=15`, `r=8`, `d=3`, the frozen base model has:

```text
directed arc Booleans                 23,996
choice Booleans                       11,998
voltage/total integers                     2
age Booleans                  429*8*3 = 10,296
------------------------------------------------
base variables                         46,292
```

Its base constraints are exactly

```text
circuit                                      1
choice MaxEquality + AtMostOne          23,996
one choice per lower orbit                  429
voltage equality/modulo/domain                3
age implications/clauses     23,996*(1+7*2+3)=431,928
upper-q1 orbit clauses                     335
---------------------------------------------------
base constraints                        456,692
```

The seed mix is

```text
47 lower q2, 11 lower q3, 27 upper q2, 1 upper q3.
```

In the frozen coordinate-history encoding, a cut uses `2q+1` state/arc
integers plus `(q+1)c` membership Booleans, where `c=r+q-1` below and
`c=r+q` above.  It has `2q+c(q+2)` constraints.  Therefore the four kinds
contribute

```text
                         vars/cut   constraints/cut
lower q2                    32             40
lower q3                    47             56
upper q2                    35             44
upper q3                    51             61
```

and hence

\[
 47(32)+11(47)+27(35)+51=3017,
\]

\[
 47(40)+11(56)+27(44)+61=3745.
\]

Adding the base gives exactly

```text
49,309 variables, 460,437 constraints.
```

Thus the reported figures are independently reproduced from the source,
not from a solver log.

The token/`AllDifferent` formulation instead adds

\[
 74\cdot7+12\cdot10=638
\]

variables and the same number of high-level constraints.  Its exact total
is therefore

```text
46,930 variables, 457,330 constraints.
```

Because the generic theorem does not make the sole seeded upper-q3
short-window row a necessary constraint for unrestricted upper coverage,
the presently proved validity-preserving subset of the compact rows has 85
targets and adds only

\[
 74\cdot7+11\cdot10=628
\]

variables and high-level constraints.  Its totals are

```text
46,920 variables, 457,320 constraints.
```

The final `5d0f0fb2...` source uses one unrestricted accumulated-union
boundary clause, rather than an upper-q3 token block, for the remaining
seed target.  It therefore has the exact current seeded total

```text
46,920 variables, 457,321 constraints.
```

The one clause has 3,425 directed-arc literals for this seed and target.
This count is for the first separated boundary; later CEGAR rounds may add
further boundaries.  A whole-selector no-good would likewise add one
constraint and no variable, but Section 6 explains why the two cuts are not
generally comparable.

The q2/q3 permutation-table variant retains `46,930` variables and adds only

\[
 74\cdot5+12\cdot7=454
\]

constraints, for a total of

```text
46,930 variables, 457,146 constraints.
```

These are model-construction counts; no claim is made that fewer high-level
constraints always means faster CP-SAT presolve.

## 6. Exact unrestricted-upper accumulated-union network

For q>=3, fixing the local token formulation does not repair the semantic
gap in Section 3.  There is, however, an exact network extended formulation
whose auxiliary flow can be continuous once the carrier arc variables are
binary.

Fix an upper target `U`.  Construct automaton nodes

\[
 (J,X),\qquad X\in\binom Ur,\quad X\subseteq J\subseteq U.  \tag{6.1}
\]

The interpretation is that `X` is the current carrier state and `J` is the
union accumulated since the chosen start.  Add a supersource arc to every
`(X,X)` and a sink arc from every `(U,X)`.  For every retained physical
Johnson edge `e:X->Y` inside `U`, and every node `(J,X)`, add

\[
 (J,X)\longrightarrow(J\cup Y,Y)                    \tag{6.2}
\]

labelled by the directed quotient arc `alpha(e)`.  Give this automaton edge
capacity zero when the carrier variable `y_{alpha(e)}` is zero and capacity
one when it is one.  Require one unit of source-to-sink flow.

### Theorem 6.1 (accumulated-union flow equivalence)

For binary selected carrier arcs, this network has a feasible unit flow if
and only if the physical carrier contains a contiguous interval lying in
`\binom Ur` whose union is `U`.

#### Proof

A carrier interval lifts uniquely through (6.2), starting at `(X_0,X_0)`;
its first coordinate records precisely its running union, so it reaches a
sink exactly when the interval union is `U`.

Conversely, a feasible network flow decomposes into source-to-sink paths and
cycles.  At least one source-to-sink path exists.  Every transition on it
has a selected physical carrier edge.  Consecutive automaton transitions
share the literal physical state, and the selected lift has one outgoing
edge at each state, so its physical projection is a contiguous carrier
interval.  Reaching `(U,X)` certifies that its accumulated union is `U`.
QED.

For fixed binary carrier variables, zero-capacity transitions can be
deleted and the remaining auxiliary system is an ordinary directed
unit-flow network.  Its node-arc matrix is totally unimodular, so the
auxiliary flow variables may be continuous.  This is conditional
integrality; it is not a claim that adjoining the carrier circuit and all
activation columns produces one globally TU matrix.

The number of automaton nodes is exactly

\[
 \sum_{t=0}^q
 \binom{r+q}{q-t}\binom{r+t}{t}
 =2^q\binom{r+q}{q}.                                  \tag{6.3}
\]

The identity follows from

\[
 \binom{r+q}{q-t}\binom{r+t}{t}
 =\binom{r+q}{q}\binom qt.
\]

Before quotient self-loop omission, the nonterminal transition count is

\[
 rq\binom{r+q}{q}(2^q-1).                              \tag{6.4}
\]

Thus this is polynomial in `k` for every fixed q and avoids enumerating all
carrier intervals or all shadow paths.  At k15 upper q3 it has `1320` nodes
and `27720` internal transition copies before self-loop omission.  It is
larger than the short four-state CP table, but it has the correct unrestricted
chronology and adds no new binary variables in an MILP implementation.

The same automaton also has an exact zero-auxiliary-variable projection for
the existing integer CEGAR loop.  For an integer selector, open precisely the
automaton transitions whose quotient-arc label is selected and let `R` be
the set reachable from the supersource.  If no accepting state is reachable,
let `B` be the set of distinct quotient-arc labels on transitions leaving
`R`.  Then

\[
                 \sum_{a\in B} y_a\ge1                         \tag{6.5}
\]

is valid and violated by the current selector.  Validity follows because
every accepting path starts in `R` and must cross its boundary; violation
follows because a selected boundary label would have made its destination
reachable.  Repeated separation by ordinary reachability is therefore an
exact combinatorial-Benders implementation with no persistent state, token,
or flow variables.  Such a cut may exclude many additional arc selections,
but it and the current whole-choice no-good live in different projections
and neither generally dominates the other.  The number of rounds is not
bounded here.

The lower fixed-q predicate has the same projection after layering the
automaton by steps `0,...,q` and accepting exactly the empty-defect states at
layer q.

## 7. Composite k15 short target orbits

The relevant target-orbit profiles are

```text
rank 5  (lower q3):  15^200 + 3^1
rank 6  (lower q2):  15^333 + 5^2
rank 10 (upper q2):  15^200 + 3^1
rank 11 (upper q3):  15^91.
```

Direct construction of the state templates gives:

```text
mode/target             orbit  states  nominal rows  retained rows  labels
lower q2, 3171             5      36        504           486        162
lower q2, 5285             5      36        504           486        162
lower q3, 4681             3     120       2520          2480        496
upper q2, 14043            3      45        720           680        136
```

There is no short upper-q3 target orbit.  In each displayed row the target
stabilizer acts freely on central states and transitions; the retained-row
count is stabilizer size times the distinct quotient-arc-label count.

The current 86-cut residence seed contains both short lower-q2 targets
`3171,5285`.  Its 11 lower-q3 misses, 27 upper-q2 misses, and one upper-q3
miss are all full target orbits.  Its short upper-q1 miss is separate from
the compact q2/q3 family.

One existential constraint for a target representative is correct even
when its orbit has size 3 or 5: rotating a witness covers every distinct
target in that orbit.  No factor 15 belongs on this existence row.  Actual
orbit size is required later for weighted Hall demand, which is a different
constraint.

A safe composite symmetry breaker restricts only `state_0` to one
representative under the target stabilizer.  It reduces the possible starts
from `36` to `12` for each short lower-q2 target, from `120` to `24` for the
short lower-q3 target, and from `45` to `9` for the short upper-q2 target.
Every witness has a common stabilizer rotation meeting this condition.
Quotienting every time layer independently is unsafe because it forgets the
relative stabilizer phase and can create a nonphysical concatenation.

## 8. Code-audit findings and proved boundary

1. The frozen `ec0cc8e...`/`3ad43459...` code caught both `KeyError` and
   `ValueError` while describing both as self-loop omission.  Only the former
   is the expected absent catalogue choice; the latter signals failure of
   directed-arc uniqueness.  Final hash `5d0f0fb2...` correctly catches only
   `KeyError` at lines 620--625 and therefore fails closed on nonuniqueness.
2. Final lines 567--637 and 1412--1457 implement the all-fixed-q token
   theorem exactly.  Final lines 639--698 implement the accumulated-union
   reachability separator, and lines 1458--1460 install its boundary directly
   in directed-arc variables.  Seed and dynamic upper depths `q>=3` use that
   exact boundary at lines 1570--1575 and 1660--1665; only upper q2 retains
   the short state-path block.
3. The target API for `shadow_state_template` checks rank but does not require
   a canonical representative.  That is mathematically safe because its
   states are physical masks, though it can duplicate cache entries.  The
   new upper-boundary API does require canonical representatives, matching
   all current callers.
4. The two older comparison scripts initially became stale when transition
   rows changed from triples to four-tuples.  In the final observed tree,
   `scratch/audit_compact_q3_equivalence.py:20` and
   `scratch/audit_compact_shadow_state_paths.py:21` both unpack the fourth
   token and pass syntax checking.  This lane did not rerun their exhaustive
   enumeration locally.  The solver-free reproducer below supplies the k15
   composite and unrestricted-q3 regressions they lack.
5. The comment at final lines 1666--1667 still says deeper upper shadows use
   a whole-selection no-good, although the immediately preceding code now
   installs an exact reachability boundary.  This is stale prose only, not a
   semantic defect.  Seeded cuts in cycle-cover mode still require a
   Hamilton-cycle hint because lines 1560--1565 call `validate_carrier`;
   this is a mode limitation, not a default-model soundness failure.  Also,
   the special `target == full` return at lines 663--666 is a compiler-level
   convention in disconnected cycle-cover mode, matching
   `factor_upper_missing`; it is not a claim that one component contains a
   full-union interval.  For proper targets the separator is exact within one
   selected component, and for the default Hamilton mode there is no such
   qualification.
6. The solver-free reproducer
   `scratch/audit_ad_shadow_state_paths_20260729.py` runs in under one second
   on the audited machine.  It freezes the live source and fixture hashes,
   checks all four composite short-target tables, reconstructs the exact
   86-cut seed mix, reproduces both model totals, and verifies that the only
   covered rank-eleven seed targets needing more than three edges are
   `4031,7675,12155`, each with minimum four.  It also verifies that the
   exact boundary accepts those three long witnesses, separates missing
   target `7807`, has 3,425 labels, and contains no selected arc.  It returns
   `PASS` on `5d0f0fb2...`; it invokes neither CP-SAT nor a carrier search.
7. No edit to the shared core was made in this lane.  The snapshot chronology
   above is essential: `49,309/460,437` is the original coordinate-history
   model, `46,930/457,330` is the transient all-token 86-row model, and
   `46,920/457,321` is the final exact token-plus-boundary seed model.
8. A separate adversarial proof audit rederived the token equivalences,
   counts, finite horizon, conditional-TU flow, boundary validity, and
   composite orbit tables.  It forced three scope corrections incorporated
   above: the all-q obstruction is only a local Johnson-path theorem beyond
   q3, no general sharpness of the horizon is claimed, and the boundary cut
   does not dominate the whole-choice no-good.

Proved:

* exact local lower and upper q-edge state-path semantics for every fixed q;
* exact equivalence with the pipeline lower rows at all q and with
  unrestricted upper coverage at q2;
* failure of upper minimal-window equivalence for abstract Johnson paths at
  every q>=3, and inside the strict carrier class at q3;
* the rank-dependent finite horizon in Theorem 3.3 and a concrete
  full strict-carrier q3 counterexample;
* an exact all-q defect-token CP compression;
* exact reproduction of `49,309 / 460,437` and exact reduced totals;
* correct handling and weights of every short k15 target orbit relevant to
  q2/q3;
* an exact accumulated-union network with conditional TU auxiliaries for
  unrestricted upper chronology, together with its exact lazy boundary-cut
  projection.

False for general Johnson paths, and already false inside the strict carrier
class at q3:

```text
every arbitrary upper rank-(r+q) interval witness has a q-edge witness
for q>=3.
```

No strict-carrier counterexample family is claimed here for every `q>=4`.

Accordingly, the local q3 strengthening is safe for positive search but not
for unrestricted infeasibility.  Exact alternatives are a candidate-specific
whole-selector no-good or the accumulated-union network above.  Final source
hash `5d0f0fb2...` now uses the latter's lazy reachability-boundary projection,
so its upper-q3 CEGAR again has the unrestricted semantics.
