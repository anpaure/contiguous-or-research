# AD exact strengthening audit: projected shadows, aggregate chronology, and quotient Hall

Date: 2026-07-29

## 1. Scope and frozen artifacts

This note strengthens the exact `k=15` strict-quotient carrier model without
removing or adding a feasible carrier.  It audits the source

```text
scratch/graded_quotient_pipeline.py
```

at size `75171`, mtime `2026-07-29T02:00:06+0500`, SHA-256

```text
a364a0e48e1f35dc9610436adf3e841f16290b883f12308de04dfce728fa8fda.
```

The concurrent source changes from the previously audited `5d0f0fb2...`
snapshot add base-only search control; they do not change the shadow blocks
audited here.  The resident-seeded exact model therefore still has

```text
46,920 variables, 457,321 constraints.
```

The two fixtures are

```text
scratch/fixtures/k11_equivariant_carrier_repo_v1.json
SHA-256 ae7c71823eb795555e4f81c953f6b1015a1f9767d92a0c8f43c8cc4e6de1355d

scratch/fixtures/k15_residence_hint_explicit_v1.json
SHA-256 4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10.
```

No CP-SAT solver was invoked and no search was run.  The companion
solver-free audit is

```text
scratch/audit_ad_exact_shadow_hall_master_20260729.py.
```

It runs in about two seconds, reconstructs both physical carriers, and
returns `PASS`.  This lane did not edit the shared pipeline.

Throughout, `k=2r-1`, the selected quotient arcs lift to the directed
physical middle carrier, and `d` is the enforced minimum positive residence
minus one.  The application has

\[
 (k,r,d,W,N)=(15,8,3,6435,429).
\]

## 2. Residence projects away every lower deletion token

For a lower target

\[
 S\in\binom{[k]}{r-q},
 \qquad
 \mathcal V_S=\{X\in\tbinom{[k]}r:S\subseteq X\},
\]

the current block uses `q+1` state integers, `q` quotient-arc integers, and
`q` physical deletion-token integers.  The token variables are unnecessary
once the already-eager residence automaton is present.

### Theorem 2.1 (residence-implied lower defect permutation)

Assume the carrier is `d`-resident and `1<=q<=d+1`.  If

\[
 X_0\to X_1\to\cdots\to X_q,
 \qquad X_j\in\mathcal V_S,
\]

is a literal carrier path, then

\[
 \bigcap_{j=0}^qX_j=S.                                  \tag{2.1}
\]

Equivalently, the `q` physical deletion coordinates are automatically a
permutation of the `q`-set `X_0\setminus S`.

#### Proof

Let `alpha_j` be the coordinate deleted on `X_j->X_(j+1)`.  If `alpha_j`
were not in `X_0`, it would have been inserted at an earlier step `h<j`.
Its resulting positive run would have length at most

\[
 j-h\le q-1\le d,
\]

contrary to residence.  Thus every deletion belongs to `X_0`.  A repeated
deletion would require a reinsertion between the two deletions and would
create the same forbidden short positive run.  Hence the deletions are
distinct.  No deletion lies in `S`, because every state contains `S`.
There are exactly `q` distinct deletions and exactly `q` members of
`X_0\setminus S`, so the two sets are equal.  Every initial extra is absent
from some later state, proving (2.1).  QED.

The range `q<=d+1` is exact for this proof: an inserted-then-deleted
coordinate within `q` edges is present for at most `q-1` states.  Only
`q=2,3` is used below.

### Theorem 2.2 (endpoint-projected lower block)

For `2<=q<=d+1`, define the projected tables

\[
 L_S=\{(x_1,a_0):\exists x_0\in\mathcal V_S,
                   x_0\xrightarrow {a_0}x_1\},          \tag{2.2}
\]

\[
 M_S=\{(x,y,a):x\xrightarrow a y, x,y\in\mathcal V_S\},\tag{2.3}
\]

and

\[
 R_S=\{(x_{q-1},a_{q-1}):\exists x_q\in\mathcal V_S,
                   x_{q-1}\xrightarrow {a_{q-1}}x_q\}. \tag{2.4}
\]

Use only the internal physical-state variables

\[
 x_1,\ldots,x_{q-1}
\]

and the quotient-arc variables

\[
 a_0,\ldots,a_{q-1}.
\]

Impose `L_S`, the `q-2` internal copies of `M_S`, `R_S`, and
`Element(a_j,arc_vars)=1` for every `j`.

Under the residence constraints, this block is feasible if and only if the
selected carrier has a `q`-edge witness for `S`.

#### Proof

Every table row is a retained physical Johnson edge with its exact directed
quotient-arc label.  A selected arc has a unique physical lift entering a
fixed destination and a unique lift leaving a fixed source.  Thus (2.2)--
(2.4), sharing the internal physical states, concatenate to one literal
path in `V_S`.  Theorem 2.1 makes its intersection exactly `S`.
Conversely, any witness supplies every projected row.  QED.

This uses

\[
 2q-1\quad\hbox{variables},\qquad 2q\quad\hbox{constraints}. \tag{2.5}
\]

In particular:

```text
lower q2: 7 variables / 7 constraints -> 3 / 4;
lower q3: 10 variables / 10 constraints -> 5 / 6.
```

Across the 47 lower-q2 and 11 lower-q3 seed rows, the lower shadow part
shrinks from

```text
439 variables / 439 constraints
```

to

```text
196 variables / 254 constraints.
```

The projected tables have exactly `130274` rows and `288226` integer table
entries.  Projection creates no new rows.

## 3. Upper membership is essential, but q2 has a four-variable bow tie

Residence does make the upper insertion tokens pairwise distinct: inserting,
deleting, and reinserting one coordinate within `q<=d+1` edges would create
a short positive run.  It does **not** make every inserted coordinate an
initial hole.  Deleting an old coordinate and reinserting it after a short
zero-run is permitted.

### Counterexample 3.1 (actual resident k11 carrier)

At physical position zero, the passing resident `k=11` fixture contains

```text
X0=63, X1=317, X2=303.
```

All three are rank six and lie in the rank-eight target `U=383`.  Their
union is only `319`, of rank seven.  The insertion tokens are `8,1`, which
are distinct, while

```text
U\X0 = {6,8}.
```

Coordinate 1 was initially present, deleted, and reinserted.  Therefore
dropping the upper initial-defect membership would falsely certify `U=383`
on a genuine globally resident Hamilton carrier.

The resident `k=15` seed has the analogous literal segment

```text
11149 -> 10957 -> 11209,
```

whose union is `11213`, not the containing rank-ten target `11215`.

### Theorem 3.2 (exact q2 bow-tie block)

Fix a lower or upper q2 target.  For each state `x`, let `D(x)` be its
two-element initial defect: `x\S` in lower mode and `U\x` in upper mode.
From the four-column transition table form

\[
 B^-={(x_1,a_0,e):
  \exists,x_0\xrightarrow[a_0]{d}x_1,
  D(x_0)=\{d,e\}\},                                    \tag{3.1}
\]

and

\[
 B^+=\{(x_1,a_1,e):
  \exists,x_1\xrightarrow[a_1]{e}x_2\}.               \tag{3.2}
\]

Use only four integers `x1,a0,a1,e`, the two tables, and the two selected-
arc `Element` constraints.  This block is equivalent to the current q2
token block.

#### Proof

A joined pair of rows supplies a literal predecessor and successor of the
same middle state.  The first transition removes one defect member `d`; the
second removes the other initial defect member `e`.  The deletion-token
theorem gives the lower intersection, while its insertion dual gives the
upper union.  Conversely every token-valid two-edge witness chooses exactly
the other initial defect member as `e` and appears in the join.  QED.

The block uses four variables and four constraints instead of seven and
seven.  Applying it to the 27 upper-q2 seed rows saves 81 variables and 81
constraints.  The audit joined both tables and compared them with every
token-valid q2 path for all 45 q2 target orbits at `k=11` and all 74 seeded
q2 blocks at `k=15`; the sets agree exactly.  The 27 upper tables contain
`38840` rows, `116520` integer entries, and encode `155202` exact joined
paths.

Upper depths at least three retain the unrestricted accumulated-union
reachability separator.  No short-window assumption is introduced.

## 4. Exact aggregate chronology cuts

Physical coordinate tokens may repeat across different target witnesses.
Indeed the valid `k=11` carrier covers 30 lower-q2 target orbits and 15
lower-q3 target orbits using only 11 coordinates.  A shared coordinate-token
`AllDifferent` is therefore false.

The quotient **arc** columns do admit exact aggregate `AllDifferent` rows.

### Theorem 4.1 (same-depth, same-step arc injection)

Fix a depth `q` and a relative step `j`.  Witness blocks for two distinct
rotation orbits of targets cannot choose the same directed quotient arc at
step `j`.

#### Proof

A selected quotient arc lies on one selected quotient cycle and therefore
fixes its `j` predecessors and `q-j-1` successors.  Its physical lifts are
simultaneous rotations of one literal `q`-edge window.  Their intersection,
or fixed-length union, targets all lie in one rotation orbit.  Equal step-`j`
arc labels would therefore force equal target orbits.  QED.

For the seeded model add:

```text
2 AllDifferent rows across the 47 lower-q2 witnesses;
3 AllDifferent rows across the 11 lower-q3 witnesses;
2 AllDifferent rows across the 27 upper-q2 witnesses.
```

Do not combine different relative steps or different depths.  The same
physical segment may legitimately serve nested shadows at two depths.

The passing `k=11` fixture independently gives injective column sizes
`30,30` at q2 and `15,15,15` at q3.  The resident `k=15` seed gives
`288,288` and `190,190,190` over its already-covered target orbits.

### Theorem 4.2 (cross-depth containment disequalities)

Suppose a q2 witness arc at relative column `i` equals a q3 witness arc at
relative column `j`, with

\[
 j-i\in\{0,1\}.                                         \tag{4.1}
\]

After rotating the physical lifts to align the common edge, the q2 interval
is the prefix or suffix of the q3 interval.  Hence its target contains the
q3 target.  Therefore equality is forbidden whenever no rotation of the q3
target is contained in the q2 target.

Among the `47*11=517` seeded lower target pairs, exactly 29 are compatible
and 488 are incompatible.  The four column pairs satisfying (4.1) give

\[
 4\cdot488=1952                                         \tag{4.2}
\]

implied disequalities.  Given Theorem 4.1 for the q2 columns, they compress
to 44 `AllDifferent` groups: for each q3 target and each of the four column
pairs, group its q3 arc with the incompatible q2 arcs in that q2 column.

These 44 rows are propagation only.  They neither identify witnesses across
depths nor impose a false global token matching.

### Composite stabilizer gauge

The two short lower-q2 deficit targets `3171,5285` have orbit size five and
stabilizer shifts `{0,5,10}`.  Rotating an entire witness by its target
stabilizer preserves the selected quotient-arc labels.  The sole internal
state can therefore be restricted to 12 representatives instead of all 36
states.  This removes 1,296 table rows and 2,592 integer entries without a
variable or constraint.

## 5. Exact equivalent model size

Apply:

1. lower endpoint projection to all 47 q2 and 11 q3 blocks;
2. q2 bow ties to all 27 upper-q2 blocks;
3. the seven same-depth/same-step `AllDifferent` rows;
4. the 44 cross-depth containment groups;
5. the short-target stabilizer gauge; and
6. the unchanged unrestricted-upper reachability boundary.

The exact count becomes

\[
 \boxed{46,596\text{ variables},\qquad457,106\text{ constraints}.} \tag{5.1}
\]

Before the 51 aggregate propagation rows it is

```text
46,596 variables, 457,055 constraints.
```

Omitting the optional 44 cross-depth groups gives `457062` constraints.
The allowed-table integer-entry count falls from `723472` to `402154`, a
reduction of `321318` entries, or 44.4 percent.  All reductions are
existential projections or implied constraints, so (5.1) has exactly the
same feasible selectors as the current model.

The count was derived from source objects and independently checked by the
companion script.  Local OR-Tools is unavailable, so this is not a fresh
`CpModelProto` build count.

## 6. Seed-relative choice cuts that expose contradictions early

The current shadow blocks eventually imply substantial distance from the
resident seed, but CP propagation need not derive that distance early.

### Theorem 6.1 (missing-orbit choice-radius bound)

Let an incumbent quotient Hamilton cycle of length `N` miss `H` distinct
fixed-depth `q` target orbits, where `1<=q<N`.  Every cycle covering all of
them uses at least

\[
 \left\lceil H/q\right\rceil                            \tag{6.1}
\]

undirected quotient choices absent from the incumbent.

#### Proof

A future witness made entirely of old undirected cycle edges is a connected
path in the old 2-regular cycle, possibly traversed in reverse.  It was
therefore already an incumbent interval, and reversal does not change its
intersection or union.  Hence every newly covered missing orbit has a
witness containing a new choice.  One new choice lies in exactly `q`
cyclic q-edge windows and can account for at most `q` missing target orbits.
Double counting proves (6.1).  QED.

For the resident `k=15` seed:

```text
47 lower-q2 holes  -> at least 24 changed choices;
11 lower-q3 holes  -> at least  4 changed choices;
27 upper-q2 holes  -> at least 14 changed choices;
67 upper-q1 holes  -> at least 67 changed choices.
```

Thus the shadow-only aggregate cut is

\[
 \sum_{c\in C_{\rm seed}}c_c\le429-24=405.              \tag{6.2}
\]

In the full current master, the already-eager upper-q1 clauses imply the
stronger right-hand side `362`.  The lower bound 24 remains useful after
moving to a q1-repaired scaffold.  At `k=11` every count is zero, so the cut
is vacuous.

### Per-target novelty clauses

For a seed-missing target `t`, let `E_t` be the undirected choices occurring
on any structurally eligible transition inside its exact state automaton.
Every new witness contains a nonseed choice, hence

\[
 \bigvee_{c\in E_t\setminus C_{\rm seed}}c              \tag{6.3}
\]

is valid.  These are cheap necessary clauses, not replacement witnesses.
Their exact seed sizes are:

```text
lower q2: 78..243 literals across 47 targets;
lower q3: 1050..1215 across 11 targets;
upper q2: 314..352 across 27 targets.
```

The arbitrary upper-q3 target `7807` has 1,841 structurally eligible
nonseed choices.  Its exact reachability boundary is complementary and more
phase-specific, but neither clause dominates the other.

### Projected target-to-arc Hall cuts

Let `F_(t,j)` be the directed arc labels occurring at column `j` on some
complete valid path for target `t`.  Theorem 4.1 projects to

\[
 \sum_{a\in\bigcup_{t\in X}F_{t,j}}y_a\ge |X|           \tag{6.4}
\]

for every target subset `X`.  A unit target-to-arc flow separates these
transversal cuts; raw transition unions give a safe weaker domain if the
complete-path domains have not been pruned by forward/backward DP.

The resident relaxations already match `47/47` at lower q2 and `11/11` at
lower q3.  Thus (6.4) strengthens propagation but does not see the current
holes by itself; successor chronology remains decisive.

### Upper-boundary literal compression

The exact `7807` reachability boundary has 3,425 directed-arc literals.
For 1,541 choices it contains both orientations, so their two-arc disjunction
is exactly the existing choice Boolean.  Only 343 choices contribute one
orientation.  The same clause is therefore

```text
1,541 choice literals + 343 arc literals = 1,884 literals,
```

with no auxiliary variable and no semantic change.

## 7. Exact `331 x 429` Hall compression

The weighted quotient Hall gate is exact only after an equivariant envelope
`P` and one-core `C` are fixed.  At `k=15` its target weights are

\[
 15^{329},\qquad5^1,\qquad3^1,                          \tag{7.1}
\]

and every right block has capacity 15.

### Theorem 7.1 (two ordinary Hall tests)

Weighted Hall is equivalent to two ordinary unit-capacity Hall tests on
`330 x 429` graphs:

1. the 329 full-weight target nodes plus the weight-five node; and
2. the 329 full-weight nodes plus the weight-three node.

These are two independent tests, not two matchings required simultaneously.

#### Proof

A shore with `f` full nodes and short-node indicators `a,b` requires

\[
 15f+5a+3b\le15|N|.                                    \tag{7.2}
\]

If `a=b=0`, this is `f<=|N|`.  Otherwise

\[
 0<5a+3b\le8<15,
\]

so (7.2) is exactly `f+1<=|N|`.  The two one-short tests contain all
full-only and one-short shores.  A shore containing both shorts follows by
deleting either short: the required integer block count remains `f+1` and
the neighborhood can only shrink.  Conversely weighted Hall implies each
ordinary test.  QED.

This replaces a composite weighted separator by two ordinary matching/DM
separators.  Encoding both matchings statically would duplicate the 329
full nodes and need not be smaller than one flow; its value is cheap lazy
separation and ordinary DM certificates.

At `k=11`, every one of the 21 target orbits has weight 11, so the gate is
one ordinary `21 x 42` Hall test.

### Theorem 7.2 (exact top-rank elimination)

For each rank-`h` target orbit `O`, put

\[
 G_O=\{J:P_J\in O\}.                                    \tag{7.3}
\]

These groups partition the 429 right blocks.  Rank-`h` adjacency is exactly
`G_O`, independent of the core.  If `ell_J` is aggregate lower-rank quotient
flow already using block `J`, the top demand can be completed if and only if

\[
 \sum_{J\in G_O}\ell_J
 \le15|G_O|-w(O)                                        \tag{7.4}
\]

for every top orbit `O`.

#### Proof

A rank-`h` target can occur at `J` only when it equals the rank-`h` envelope
there.  Conversely `C_J<=P_J` makes that incidence always available.  The
groups are disjoint, so after aggregate lower flow is fixed, each top orbit
sees only the total residual capacity in its own group.  Inequality (7.4) is
precisely that capacity condition.  QED.

This is an aggregate quotient-flow projection.  It certifies the existence of
some physical matching through the quotient Hall theorem; it does not promise
to extend a separately prescribed phase-resolved lower matching.

Delete all 201 rank-five target nodes and their exactly 429 incidence arcs.
The reduced conditional-TU network is

```text
lower target -> block J -> group G_(tau(J)) -> sink.
```

For any fixture with `N` right blocks and `E` target-to-block incidences, the
transformation is `E -> E-N`, saving exactly `N` network arcs.  The following
structural counts are fixture/core-specific:

```text
k15: adjacency-flow variables 1772 -> 1343;
     all network arcs          2532 -> 2103.

k11: adjacency-flow variables   77 ->   35;
     all network arcs           140 ->   98.
```

For the resident `k=15` seed specifically, eleven top groups are empty, so
their right sides in (7.4) are negative.  The exact procedure first declares
the already-known lower-q3 infeasibility.  The `1343/2103` figures above are
therefore structural reduced-network counts, not counts of a feasible reduced
seed flow.

Do not reserve one arbitrary top witness block: top demand may need to split
over several blocks to coexist with lower and short-orbit loads.

## 8. Core-independent Hall presolve and the exact conflict layer

A failed Hall test for one sampled core is not a carrier cut; another core
may pass.  There is nevertheless a strongest edgewise all-core relaxation.

Define

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1}).  \tag{8.1}
\]

These are the coordinates at the forced endpoints of their positive runs in
`P`.

### Theorem 8.1 (forced-core union graph)

For the required equivariant one-cores, `N>1`, and voltage `v` invertible
modulo `k`, a phased incidence
`(S,i)` is available for **some** core if and only if

\[
 F_i\subseteq S\subseteq P_i.                           \tag{8.2}
\]

Thus the graph defined by (8.2) is exactly the edgewise union of all
equivariant one-core Hall graphs.  Hall failure in this union graph rejects
every core.

#### Proof

The inclusion is necessary because every vertex cover of a positive support
run contains its two boundary vertices.  For sufficiency, encode an
equivariant core by the coordinate-zero cover trace.  With unit voltage `v`,
omitting coordinate `x` at physical position `i` requests omission at base
position

\[
 b_x=i-Nxv^{-1}\pmod W.                                 \tag{8.3}
\]

Distinct coordinates give base positions differing by nonzero multiples of
`N`; since `N>1`, no two are consecutive in the base run graph.  If (8.2)
holds, none is a forced run endpoint.  All requested omissions lie in one
shared base trace and are pairwise nonadjacent.  Set precisely those base
positions to zero (omitted), set every other supported base position to one,
and complete outside the support arbitrarily.  This is one valid vertex
cover, proving sufficiency.  QED.

Passing this graph is not sufficient.  Different individually available
incidences can demand adjacent omissions in one common base run.

Write `u_b=1` when the core omits the coordinate-zero incidence at base
position `b`.  The exact common-core conditions are

\[
 u_b=0\quad\hbox{at forced endpoints},
 \qquad u_b+u_{b+1}\le1                                 \tag{8.4}
\]

on every internal run edge.  A phased incidence `(S,i)` is active exactly
when both

\[
 S\subseteq P_i,
 \qquad
 K(S,i)=\{i-Nxv^{-1}:x\in P_i\setminus S\}
 \subseteq\{b:u_b=1\}.                                  \tag{8.5}
\]

Equations (8.4)--(8.5) are the missing exact conflict layer between edgewise
Hall and one common core.

The current randomized core generator samples only minimum-cardinality
vertex covers, equivalently maximum omission independent sets.  An exact
existence model must allow every path-stable omission set, without loss every
maximal one.  On a run of length five, the singleton middle omission is
maximal but not maximum and can expose incidences unavailable from the unique
maximum two-omission pattern.  Therefore failure of all currently sampled
cores is not an exact no-core certificate.

### Fixed-core Hall cuts

For a fixed core, let `e_(O,J)` be exact adjacency and define

\[
 g_J^X=\bigvee_{O\in X}e_{O,J}.
\]

Hall is exactly

\[
 \sum_Jg_J^X\ge
 \left\lceil\frac{\sum_{O\in X}w(O)}{15}\right\rceil    \tag{8.6}
\]

for every shore `X`.  At an incumbent neighborhood `N_0`, the valid
seed-relative form is

\[
 \sum_{J\notin N_0}g_J^X
 \ge
 \left\lceil\frac{\sum_{O\in X}w(O)}{15}\right\rceil
 -|N_0|.                                                 \tag{8.7}
\]

Here an active quotient incidence `e_(O,J)` must be the OR of explicit phased
witnesses `(S,i)`, each carrying its own set `K(S,i)` from (8.5).  There is no
phase-free set `K(O,J)` in general.  Exact OR reification is essential.  A
weighted flow or the two ordinary matchings of Theorem 7.1 separates these
rows.  Conditional on fixed binary
adjacency, the auxiliary flow is a network and may be continuous.  The
combined carrier/core/activation matrix is not claimed TU.

### Rank-prefix presolve

For fixed `C`, let `B_s={J:|C_J|<=s}`.  Targets of rank at most `s` can use
only these blocks, so Hall implies

\[
 15|B_s|\ge\sum_{t=1}^s\binom{15}{t}.                   \tag{8.8}
\]

At `k=15`:

```text
|B1|>=1, |B2|>=8, |B3|>=39, |B4|>=130.
```

At `k=11`, the corresponding first two bounds are `1,6`.  Full induced
prefix Hall is stronger than these scalar rows.

## 9. Lightweight fixture audit

### Passing k11 carrier

```text
shadow deficits                         0 at every audited depth
actual-core weighted Hall               231 / 231
forced-union Hall                       231 / 231
envelope-union Hall                     231 / 231
actual quotient adjacency edges         77
forced-union edges                      108
envelope-union edges                    198
```

All prefix flows pass: `11/11`, `66/66`, `231/231`.  The q2 and q3 actual
occurrence multiplicities and the same-step injections agree with the
theorems above.  The literal upper counterexample in Section 3 confirms that
only the lower residence projection is safe.

### Resident k15 seed

```text
lower q2 holes                           47 orbits
lower q3 holes                           11 orbits
upper holes by depth                     67,27,1

actual-core weighted Hall                4778 / 4943
forced-union Hall                        4778 / 4943
envelope-union Hall                      4778 / 4943
actual quotient adjacency edges          1772
forced-union edges                        4242
envelope-union edges                      9623
```

Both ordinary 330-node tests match `319/330`.  The full deficiency is

\[
 4943-4778=165=11\cdot15.                \tag{9.1}
\]

Its dual shore is exactly the eleven full rank-five target orbits against
zero position orbits: precisely the eleven lower-q3 holes.  Prefix flows
through rank four all pass:

```text
15/15, 120/120, 575/575, 1940/1940.
```

Thus the current Hall dual gives no additional carrier contradiction beyond
the q3 positive-degree rows already present.  This negative audit is
important: a generic cut derived only from one failing sampled core would be
unsound.  The displayed eleven-orbit zero shore is nevertheless
core-independent, because it persists in both the forced-union and envelope
graphs; even the exact forced-union relaxation finds only these known q3
zeros.

## 10. Recommended exact master

For the current seeded carrier search:

1. replace lower token blocks by Theorem 2.2;
2. replace upper-q2 blocks by Theorem 3.2;
3. collect arc variables by `(mode,q,relative_step)` and add the seven rows
   of Theorem 4.1 after deduplicating target keys;
4. add the 44 lower cross-depth groups of Theorem 4.2;
5. gauge the two short lower-q2 targets;
6. compress upper boundaries through whole-choice literals when both
   orientations occur;
7. add the seed-relative novelty clauses and the explicit choice-radius
   lower bound; and
8. keep weighted Hall outside the carrier master until a core is fixed, or
   introduce the exact omission variables (8.4)--(8.5).

The 46,596/457,106 count includes steps 1--5 and the existing upper boundary.
Steps 6--7 reduce literals or add implied rows but no variable.  A lower-q3
or Hall failure must never be replaced by an upper short-window surrogate.

For a fixed carrier/core Hall phase, use the two ordinary separators and
top-rank elimination.  Before selecting a core, use the forced-union graph
only as a necessary all-core screen.  Never turn one sampled-core failure
into a carrier no-good.

## 11. Proved and conditional boundary

Proved:

* exact lower token and endpoint elimination under the existing residence
  automaton;
* exact four-variable q2 bow ties, including unrestricted upper-q2 through
  the already-proved q2 shortening theorem;
* seven same-depth arc injections and 44 cross-depth aggregate groups;
* the exact equivalent 46,596/457,106 model and 44.4-percent table-entry
  reduction;
* seed-relative novelty and choice-radius cuts;
* the two-unweighted-matching form of the composite Hall dual;
* exact top-rank flow elimination;
* the forced-core edgewise union theorem and exact common-core conflict
  layer; and
* all stated k11 and resident-k15 audit figures.

Not proved, and not used:

* that every shadow-valid carrier admits an equivariant one-core passing
  Hall;
* that a deficient sampled core rejects the carrier;
* that the forced-union Hall screen is sufficient for one common core;
* that upper insertion membership follows from positive residence; or
* any upper-q3 short-window reduction.

The sole Hall obstruction visible on the resident seed is the already-known
eleven-orbit q3 zero shore.  The genuine new master gains are therefore
compression and implied chronology/radius propagation, not a new finite
infeasibility certificate.

## 12. Independent adversarial audit

Three independent proof/code audits checked the lower projection and q2
join, aggregate chronology, exact count arithmetic, Hall reduction, and
common-core layer against the frozen source and fixtures.  The following
corrections were applied before this note was frozen:

* the lower endpoint projection is restricted to `q<=d+1`;
* the novelty and unrestricted upper-reachability clauses are incomparable;
* the choice-radius theorem states `q<N`;
* the forced-core theorem states invertibility of the voltage and uses one
  shared omission trace;
* phased Hall activation includes `S subseteq P_i` and has no phase-free
  `K(O,J)`;
* top-rank elimination is explicitly aggregate, fixture-specific in its
  numerical counts, and rejects negative group capacities before building a
  network; and
* the resident seed's zero shore is distinguished from an unsound generic
  sampled-core shore.

After those corrections the auditors reproduced every headline number.  The
companion script now asserts all three frozen hashes, audits all 119 claimed
q2 bow ties, derives rather than merely prints the `723472` current table-entry
count, and checks the upper-q3 novelty split `1907=66+1841`.
