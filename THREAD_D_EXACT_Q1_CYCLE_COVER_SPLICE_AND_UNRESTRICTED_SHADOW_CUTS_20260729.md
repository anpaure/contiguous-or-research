# Exact completion of a q1-complete cycle cover by decorated path splicing

Date: 2026-07-29

Status: theorem and scope audit.  This note gives a finite necessary-and-
sufficient completion system relative to a fixed opened path forest and a
literal phase-labelled connector catalogue.  It does not assert that the
current `k=15` joint scaffold is a degree-two cover; it is not.  No search or
solver was run for this note.

## 0. Verdict

There is an exact completion theorem, but it is not a one-seam Hall theorem.
After a degree-two owner-exact cover is opened into paths, the surviving
integral gate consists of four different pieces:

1. port, owner-colour, component-subtour, and voltage equations;
2. a finite cyclic residence transducer, which must allow a forbidden word
   to cross several seams when retained paths are short;
3. finite fixed-window rows for upper `q=1`, lower `q=2,3`, and upper `q=2`;
4. for unrestricted upper `q=3`, the complete family of labelled
   accumulated-union reachability cuts.

Together these conditions are necessary and sufficient.  They can be put in
CP-SAT with `AddCircuit`, reified local words, and lazy reachability cuts.
The upper-`q=3` auxiliary problem is a network once the carrier arcs are
fixed, but the joint orientation/splice master is not thereby totally
unimodular.

Two sharp warnings are part of the theorem boundary.

* Short paths invalidate independent seam collars: a residence defect can
  start at one seam and end at a second seam.
* Unrestricted upper `q=3` is not a three-edge condition.  A frozen strict
  `k=15` carrier contains rank-eleven targets whose shortest witnesses use
  four edges.

## 1. Literal quotient setup

Put

\[
        k=2r-1,
\]

and let rotation by one coordinate be `rho`.  Work in the strict directed
quotient catalogue of physical Johnson arcs on rank-`r` sets.  A directed
dart `a` retains all of the following data:

\[
 X(a)\longrightarrow Y(a)=X(a)-\{d(a)\}+\{b(a)\},
\tag{1.1}
\]

its lower-owner colour

\[
        c(a)=X(a)\cap Y(a),
\tag{1.2}
\]

its upper-first-shadow colour

\[
        u(a)=X(a)\cup Y(a),
\tag{1.3}
\]

its directed quotient-arc identifier `lambda(a)`, and its voltage `alpha(a)`
in `Z_k`.  Parallel quotient darts have different identifiers and are not
identified.  This is essential at composite `k`.

Let `F_0` be a loopless owner-exact degree-two quotient cover: every upper
root has degree two and every lower-owner colour is used once.  Assume also
that every required upper-`q=1` target is represented by an edge of `F_0`.
The cover may have several components.

Choose a nonempty deleted edge set `D^-` meeting every component of `F_0`.
Then

\[
        H=F_0\setminus D^-
\tag{1.4}
\]

is a spanning path forest

\[
        P_1,\ldots,P_s,
\tag{1.5}
\]

where isolated vertices are allowed.  If `F_0` has no loops, then
`s=|D^-|`.  Let `r_c` be the number of retained edges of lower colour `c`;
in the present owner-exact setting it is zero or one.  The freed colours are
exactly those with `r_c=0`.

Every path has two orientations.  Its oriented version `P_i^epsilon` has an
initial history port, a terminal history port, and an internal voltage
`beta_i^epsilon`.  A connector option is a literal phase-labelled dart

\[
 a:(i,\epsilon)\longrightarrow(j,\eta)
\tag{1.6}
\]

from the terminal port of `P_i^epsilon` to the initial port of
`P_j^eta`.  It includes its exact lower colour, delete/insert tokens, phase,
and voltage.  The theorem is relative to the supplied connector catalogue;
an adjacency with the right quotient endpoints but the wrong phase is not a
connector.

### Phase convention

All chronology and shadow words below are evaluated in the physical voltage
lift.  If a quotient lap has voltage `v`, its endpoint is `rho^v X_0`, not
the same chosen representative `X_0`.  Equivalently, either expand every
selected dart through all `k` phases or lift a word by its accumulated
voltages and use the `v`-twisted wrap.  Naively joining normalized quotient
representatives at the lap boundary is incorrect.

For noncentral targets, all claims use their actual translation orbits.
They need not have size `k` when `k` is composite.

## 2. The oriented port master

Use orientation literals `o_i^+`, `o_i^-` and connector literals `z_a`.
The raw completion equations are

\[
 o_i^++o_i^-=1,
\tag{2.1}
\]

\[
 \sum_{a\text{ out of }(i,\epsilon)}z_a
 =\sum_{a\text{ into }(i,\epsilon)}z_a
 =o_i^\epsilon,
\tag{2.2}
\]

and the exact owner-current equations

\[
        r_c+\sum_{a:c(a)=c}z_a=1
        \qquad\hbox{for every lower colour }c.
\tag{2.3}
\]

Put

\[
        s_{ij}=\sum_{a:i\to j}z_a.
\]

The selected successor permutation on the paths is one cycle if and only if
the in/out equations hold and

\[
   \sum_{i\in A,\ j\notin A}s_{ij}\ge1
   \qquad
   (\varnothing\ne A\subsetneq[s]).
\tag{2.4}
\]

Thus (2.4) may be replaced by `AddCircuit` on the path components, provided
the API's exclusion self-loops are omitted or forced to zero and every path
node is mandatory.  Parallel connector literals may be passed directly, or
one may use aggregate arc literals `s_ij` exactly reified as their OR.  The
case `s=1`, whose genuine closing connector is a self-seam, must be handled
separately; it is not an optional-node self-loop.

The quotient voltage is

\[
 v\equiv
 \sum_{i,\epsilon}\beta_i^\epsilon o_i^\epsilon
 +\sum_a\alpha(a)z_a\pmod k.
\tag{2.5}
\]

Its physical lift is one cycle exactly when

\[
        \gcd(v,k)=1.
\tag{2.6}
\]

At `k=15`, (2.6) is the eight-value table

\[
        v\in\{1,2,4,7,8,11,13,14\}.
\tag{2.7}
\]

### Lemma 2.1 (raw splice equivalence)

Equations (2.1)--(2.4) are necessary and sufficient for the retained paths
and selected connectors to form one owner-exact spanning quotient cycle.
Adding (2.6) is necessary and sufficient for its equivariant physical lift
to be one Hamilton cycle.

#### Proof

Every internal path vertex already has degree two.  Each nonisolated path
endpoint lacks one incidence; an isolated path vertex lacks two.  Equations
(2.1)--(2.2) supply exactly the missing incoming and outgoing incidences with
one common orientation.  Equation (2.3) restores each deleted owner colour
once and introduces no repeated owner.  After contracting every retained
path, the components of the result are precisely the cycles of `s`; hence
(2.4) is equivalent to one quotient cycle.  Voltage is additive under path
concatenation, and the cyclic lift of voltage `v` has `gcd(v,k)` components.
This proves both assertions.  QED.

Upper-`q=1` completeness is not automatic under the splice, even when the
input cover was complete.  Let `U` denote an actual translation orbit and
let `I_1(U)` be the number of retained internal edge orbits whose union lies
in `U`.  Its exact preservation row is

\[
 I_1(U)+\sum_{a:[u(a)]_\rho=U}z_a\ge1.
\tag{2.8}
\]

Only targets whose every old witness was deleted need a nontrivial row.

## 3. Exact residence and fixed-window shadows

For a physical directed edge word write

\[
 X_{t+1}=X_t-\{d_t\}+\{b_t\}.
\tag{3.1}
\]

Residence at least `d+1` is exactly

\[
        b_i\ne d_{i+t}
        \qquad(1\le t\le d)
\tag{3.2}
\]

at every cyclic position.  In the application `d=3`.  The `t=1` rows follow
already from exact lower-owner colours, but retaining them is harmless and
makes the transducer self-contained.

Enumerate every realizable directed physical edge string `C` in the
path/seam language of the needed bounded length.  Let `L(C)` be the finite
set of orientation and exact connector literals supporting it.  Introduce

\[
        w_C=\bigwedge_{\ell\in L(C)}\ell
\tag{3.3}
\]

by the standard exact reification

\[
 w_C\le\ell\quad(\ell\in L(C)),\qquad
 w_C\ge\sum_{\ell\in L(C)}\ell-|L(C)|+1.
\tag{3.4}
\]

An internal word of a fixed oriented path can instead be folded directly
into the corresponding orientation literal; a word invariant under path
reversal may be recorded as a constant protected witness.

For every residence-hazard string

\[
 C=(e_0,\ldots,e_t),\qquad
 1\le t\le d,\qquad b(e_0)=d(e_t),
\tag{3.5}
\]

impose the no-good

\[
        \sum_{\ell\in L(C)}\ell\le |L(C)|-1.
\tag{3.6}
\]

For required targets impose

\[
 \sum_{C:\ |E(C)|=q,\ \cap V(C)=S}w_C\ge1
       \quad(q=2,3),
\tag{3.7}
\]

for every lower target `S` of rank `r-q`, and

\[
 \sum_{C:\ |E(C)|=2,\ \cup V(C)=U}w_C\ge1
\tag{3.8}
\]

for every upper target `U` of rank `r+2`.  Equation (2.8) is the analogous
one-edge row.

These are exact finite rows, not an independence approximation.  A lower
depth-`q` word can cross as many as `q` seams.  A residence comparison in
(3.5) contains `t+1` edges and can cross as many as `d+1` seams when isolated
or very short path components intervene.

### Equivalent queue formulation

Instead of listing (3.5), put at every path entrance the ordered queue of the
last `d` physical insertion tokens, together with the current phase and the
last three upper states (or, equivalently, the rolling `q=2,3`
intersection/union registers) needed to emit the fixed labels.  Processing
a path dart or a connector rejects if its deletion token occurs in the
queue, then shifts the queue and appends its insertion token.  Each oriented
path is a fixed partial map on these boundary states.  Linking those maps
through the selected connector cycle, with the voltage-twisted wrap, is
equivalent to (3.2)--(3.8).  This is the path-forest version of the residence
queue automaton.

### Lemma 3.1 (safe retained interiors)

For a maximal old coordinate run `R` of length at most `d`, include its two
bracketing transitions and call this closed set `span(R)`.  All retained path
interiors are residence-safe in either orientation if and only if

\[
        D^-\cap\operatorname{span}(R)\ne\varnothing
\tag{3.9}
\]

for every such old run.

#### Proof

If the closed span is retained, its word `0 1^ell 0` remains inside one path;
reversal preserves its run length.  Conversely, after every old short closed
span is hit, a short run wholly inside a retained path would be an unhit old
short run.  Hence every possible new defect crosses an inserted seam and is
listed in (3.5).  QED.

If every retained path has at least `d` internal edges, a distance-at-most-`d`
comparison cannot cross two inserted seams.  In that special case genuine
one-seam residence collars suffice.  No such reduction is valid for shorter
paths.

### Lemma 3.2 (unrestricted upper q2 shortens exactly)

If an interval of rank-`r` Johnson states contained in a rank-`r+2` set `U`
has union `U`, then three consecutive states already have union `U`.

#### Proof

Take a shortest such interval `X_0,...,X_l`.  Minimality gives a coordinate
present only at the left endpoint and another present only at the right
endpoint.  Every interior state is therefore the unique rank-`r` set obtained
from `U` by deleting those two coordinates.  Consecutive carrier states are
distinct, so there is at most one interior state and `l<=2`.  Two adjacent
Johnson states have union rank `r+1`, hence `l=2`.  QED.

Thus (3.8) is also exact for the unrestricted upper-`q=2` semantics.

## 4. Unrestricted upper q3: the exact cut family

Fixed three-edge rows are not necessary at upper `q=3`.  Fix instead an
upper target

\[
        U\in\binom{[k]}{r+3}.
\]

Build the accumulated-union automaton with nodes

\[
 (J,X),\qquad X\in\binom Ur,\qquad X\subseteq J\subseteq U.
\tag{4.1}
\]

Every `(X,X)` is a source and every `(U,X)` is accepting.  For every literal
physical Johnson edge `X->Y` inside `U`, add

\[
       (J,X)\longrightarrow(J\cup Y,Y),
\tag{4.2}
\]

labelled by its directed quotient-arc variable `y_lambda`.  The variables
`y_lambda` are linked exactly to the chosen path orientations and connector
literals.  A retained path selects one direction of each of its internal
arcs; a selected connector activates its literal dart.  Parallel quotient
arcs remain distinct.  Concretely, one may impose the exact Boolean identity

\[
 y_\lambda=
 \bigvee_{(i,\epsilon):\ \lambda\in P_i^\epsilon}o_i^\epsilon
 \ \vee\!
 \bigvee_{a:\ \lambda(a)=\lambda}z_a,
\tag{4.2a}
\]

with the port and owner equations ruling out incompatible simultaneous
realizations.

For a node set `R` containing every source and no accepting node, let

\[
 B_U(R)=
 \{\lambda:\hbox{a transition labelled }\lambda
       \hbox{ leaves }R\}_{\rm distinct}.
\tag{4.3}
\]

The exact labelled boundary row is

\[
        \boxed{\ \sum_{\lambda\in B_U(R)}y_\lambda\ge1\ }.
\tag{4.4}
\]

Repeated labels are counted once.  If `B_U(R)` is empty, (4.4) is the
correct infeasibility row.

### Theorem 4.1 (upper-q3 reachability and cuts)

For an integral one-in/one-out orientation of a degree-two selection, the
following are equivalent.

1. One physical directed lift component contains a consecutive interval of
   states lying inside `U` whose union is `U`.
2. The open accumulated-union automaton has a source-to-accepting path.
3. Every row (4.4) holds.

The equivalence remains true before the directed connector cycle cover is
spliced into one component; it does not require the subtour rows (2.4).

#### Proof

A carrier interval lifts through (4.2), and its first coordinate is exactly
its running union.  Conversely, consecutive automaton transitions share the
literal physical state.  The selected degree-two orientation has one
outgoing edge there, so the projection of an open automaton path is a
contiguous path in one selected component.  It accepts exactly when its
union is `U`.  An automaton walk may formally traverse a selected component
more than once.  A second full lap sees no state not seen on the first and
cannot enlarge the union, so every accepting walk shortens to a based cyclic
interval of at most one lap.

Every accepting path crosses the boundary of each `R`, proving that (2)
implies (3).  If no accepting node is reachable, take `R` to be the set of
nodes reachable from all sources.  No label in `B_U(R)` is selected, so
(4.4) is violated.  This proves the converse.  QED.

For a lazy CP-SAT implementation, evaluate reachability at an integer master
solution.  If the target is uncovered, the reachable set gives one violated
row (4.4).  Repeating this is exact because the integer master space and the
cut family are finite; no polynomial bound on the number of rounds is
claimed.  Alternatively, add one unit of conditional network flow.  The
auxiliary node-arc matrix is totally unimodular after the binary carrier arcs
are fixed.  This conditional fact is not total unimodularity of the combined
master.

### Segment compression

The same predicate can be evaluated directly on the opened paths.  For an
oriented path `P=(X_0,...,X_l)`, store all internal interval unions inside
`U`, all prefix and suffix unions inside `U`, and, when every state of `P`
lies in `U`, its total union.  Reversal preserves internal and total unions
and exchanges prefixes with suffixes.

Every seam-crossing witness has the unique form

\[
 \hbox{suffix of its first segment} ;
 \hbox{zero or more whole segments} ;
 \hbox{prefix of its last segment}.
\tag{4.5}
\]

Tracking the accumulated set `J` in (4.5) gives a labelled component
automaton with states `(i,epsilon,t,J)`, where `t in Z_k` records the physical
phase.  At `q=3` there are at most eight possible `J` above a fixed terminal
rank-`r` state.  Hence, with the quotient-scale `s` of (1.5), the direct
bound is `16ks+2`; obtaining `16s+2` would require an additional proved
orbit-normalized phase compression in which the target is transported too.

The macro activation rules are literal.  A source-to-suffix arc of
`P_i^epsilon` is activated by `o_i^epsilon`.  A transfer through the next
whole segment and an acceptance through its terminal prefix are activated by
the fully oriented connector literal `z_(i epsilon,j eta)`.  A whole-segment
transfer exists only if every state of that physical oriented segment lies
in `U`; an internal witness is handled separately as an already-satisfied
target.  With these rules the automaton handles reversal, cyclic wrap,
isolated paths, and intervals crossing arbitrarily many seams.  Applying the
same labelled-cut theorem gives cuts in the orientation and connector
literals directly.  The physical-arc form (4.1)--(4.4) is usually safer
because it reuses the existing `y_lambda` interface and cannot lose a phase
condition during compression.

## 5. Exact completion theorem

Let `T_2^-`, `T_3^-`, `T_2^+`, and `T_3^+` be any required families of
lower/upper targets; for full completion take all actual target orbits in the
corresponding ranks.

### Theorem 5.1 (decorated q1-cover completion)

Relative to the fixed cut forest `H` and literal connector catalogue, there
exists an orientation and splice whose quotient is one cycle and whose
physical lift is

* owner-exact and one physical Hamilton cycle;
* upper-`q=1` complete;
* resident for at least `d+1` states;
* complete on `T_2^-`, `T_3^-`, `T_2^+`; and
* unrestricted-upper complete on `T_3^+`

if and only if there are integral `o,z,y,w` satisfying all of the following:

1. the orientation, port, and owner equations (2.1)--(2.3);
2. the subtour family (2.4), or the mandatory-node `AddCircuit` formulation
   qualified after (2.4);
3. the unit-voltage condition (2.5)--(2.6), with the physical twisted wrap;
4. the exact directed-arc linkage (4.2a) and every support-conjunction
   reification (3.3)--(3.4);
5. the upper-`q=1` rows (2.8);
6. the residence no-goods (3.6);
7. the lower-`q=2,3` and upper-`q=2` rows (3.7)--(3.8); and
8. every upper-`q=3` labelled reachability cut (4.4).

#### Proof

Given a completed carrier, its traversal orients every retained path and
selects one literal connector at every pair of consecutive ports.  Lemma 2.1
gives conditions 1--3.  Its actual arcs and local words give the exact
linkages in condition 4.  Every bounded physical word has exactly its support
conjunction (3.3), so upper `q=1`, residence, lower `q=2,3`, and upper `q=2`
give conditions 5--7.  Theorem 4.1 gives condition 8.

Conversely, Lemma 2.1 turns conditions 1--3 into one owner-exact quotient
cycle with one physical lift.  Condition 4 binds every decoration variable
to that literal carrier.  Conditions 5--7 are exact enumerations of all
relevant bounded physical words and therefore give the stated residence and
fixed-window support.  By Theorem 4.1, condition 8 supplies an unrestricted
interval for every required upper-`q=3` target.  No other property is used.
QED.

The theorem is also an exact preservation theorem.  A target with a retained
internal witness may be deleted from the active rows; a target whose every
old witness meets `D^-` remains active and must receive a boundary or
reordered-segment witness.

## 6. Sharp failures of more local criteria

### 6.1 Two seams can create one residence defect

The minimal mechanism is already a three-edge word with tokens

\[
       (d_0,b_0)=(a,x),\qquad
       (d_1,b_1)=(c,g),\qquad
       (d_2,b_2)=(x,f),
\tag{6.1a}
\]

where `a,c,f,g,x` are otherwise distinct.  Choose the initial Johnson state
to contain `a,c` and omit `x,f,g`; then all three transitions are literal.
The first and third edges may be connector seams separated by the one-edge
path in the middle.  The first seam passes against a safe continuation that
does not delete `x`, and the third passes against a safe history in which
`x` was inserted more than `d` steps earlier.  Selecting them together gives

\[
        b_0=x=d_2,
\]

a delay-two residence defect.  Thus pre-eligibility of each seam against its
old collar does not compose across a short intervening path.

A closed version which simultaneously retains distinct local owner and
first-shadow colours is the Johnson chronology

\[
        12,\ 23,\ 34,\ 14,\ 12
\tag{6.1}
\]

which has transition tokens

\[
 (d_i,b_i)=(1,3),(2,4),(3,1),(4,2).
\tag{6.2}
\]

Every immediate check `b_i != d_(i+1)` passes.  Its four edge intersections
are distinct, and its four edge unions are the four different three-subsets
of `[4]`.  Nevertheless

\[
        b_0=d_2,
        \qquad b_1=d_3,
\tag{6.3}
\]

so residence four fails.  Cutting the four edges into isolated path vertices
makes (6.3) a literal multi-seam failure.  Fixed spectator coordinates embed
the same word in larger Johnson graphs.  This is a local chronology gadget,
not a claim that the four displayed states span a full central layer.

Thus endpoint equations, owner colours, upper `q=1`, connectivity, and
independent immediate seam tests do not imply residence.  The `d`-step queue
or all forbidden chains (3.5) are necessary unless path lengths separate the
seams.

### 6.2 Upper q3 can require four edges in a strict carrier

The audited strict `k=15` residence carrier contains the five consecutive
rank-eight states

```text
30264, 29242, 29214, 29230, 23086.
```

Their union is the rank-eleven mask

```text
32318
```

with canonical orbit representative `4031`.  The first and last four-state
unions are `30270` and `31294`, both of rank ten.  A whole-cycle audit proves
that orbit `4031` has no three-edge witness anywhere and has minimum witness
length four.  The same is true of orbits `7675` and `12155`.

Therefore a three-edge upper-`q=3` collar rejects a genuine valid strict
carrier.  Cutting the four displayed transitions into segment boundaries
and then reinserting those same four transitions as selected seams realizes
the witness as a correlated four-seam interval.

The proved general finite horizon at `k=15` is ten edges,

\[
 \ell\le {r+q-2\choose q-2}+1={9\choose1}+1=10,
\tag{6.4}
\]

but the accumulated-union reachability formulation is exact without
choosing a horizon.

## 7. k15 calibration and present scope

For `k=15`, `r=8`, the central quotient has `429` upper roots and `429`
lower-owner colours.  The strict catalogue has `11,998` undirected choices
and `23,996` directed arc variables.  The target-orbit counts are

| gate | target orbits |
|---|---:|
| upper `q=1` | 335 |
| lower `q=2` | 335 |
| lower `q=3` | 201 |
| upper `q=2` | 201 |
| upper `q=3` | 91 |

If one edge is opened in each of `s` cover components, there are `s` paths
and `s` freed colours.  A fixed lower colour has at most `28` undirected,
hence `56` directed, Johnson choices, so before port filtering there are at
most `56s` connector literals.  Add one orientation bit per path, the
port/colour rows, mandatory-node `AddCircuit` (with the `s=1` case handled
separately), the voltage table, and the decorated rows of Theorem 5.1.

For one upper-`q=3` target, (4.1) has exactly

\[
        2^3{11\choose3}=1320
\tag{7.1}
\]

nodes and, before strict self-loop omission,

\[
        8\cdot3{11\choose3}(2^3-1)=27720
\tag{7.2}
\]

internal transition copies.  Instantiating all `91` orbit representatives
would give `120,120` nodes and at most `2,522,520` internal transitions, plus
`30,030` source/sink incidences.  Lazy separation keeps none as persistent
solver variables.  The first frozen cut for the seed-missing target `7807`
has `3,425` distinct directed-arc literals.

There is not yet an authoritative degree-two upper-`q=1`-complete `k=15`
cover near the joint scaffold to which Theorem 5.1 can be applied.  The
69-change joint selector has degree histogram

```text
0:4, 1:71, 2:283, 3:64, 4:6, 5:1,
```

with `79` shortage and `79` excess units, so it is at least `40` further
choice replacements from degree two.  It is upper-`q=1` and lower-`q=3`
positive only at the relaxed choice-witness level.  Relative to the resident
seed, the same relaxed choice-witness audit also hits `21/47` old
lower-`q=2` misses, `23/27` old upper-`q=2` misses, and the unique old
upper-`q=3` miss; `26` lower-`q=2` and four upper-`q=2` misses remain before
degree, orientation, and residence are restored.

Independently, the checked DRAT certificate proves that a degree-two
upper-`q=1`-complete selector cannot lie at distance `67` from the resident
seed; distance `68` is merely the first admissible shell, not a proved
feasible shell.  The small unindexed scaffold-radius `INFEASIBLE` JSON files
do not carry proof logs and are not used to strengthen either bound.

Hence the exact surviving finite task is:

> first obtain an owner-exact upper-`q=1` degree-two cover (or solve for it
> jointly), then choose its cuts, path orientations, and literal connectors
> satisfying Theorem 5.1.  Upper `q=3` must be separated by (4.4); neither a
> three-edge collar nor a componentwise shadow score is a valid substitute.

## 8. What is and is not closed

Proved here:

* an iff port/owner/subtour/voltage theorem for a fixed opened cover;
* an iff multi-seam residence and fixed-shadow formulation;
* exact shortening of unrestricted upper `q=2`;
* an iff unrestricted upper-`q=3` labelled-cut theorem;
* a finite, directly embeddable CP-SAT/CEGAR system; and
* sharp counterexamples to pairwise seam safety and three-edge upper `q=3`.

Not proved here:

* existence of the initial `k=15` degree-two q1-complete cover;
* existence of a splice satisfying the finite system;
* a polynomial bound on the number of lazy cuts;
* total unimodularity of the combined master; or
* the later one-core Hall, physical owner matching, upper-safe cut, and
  literal compiler gates.

The precise gain over the preceding decorated-forest theorem is that every
remaining chronology condition is now exact: short components are handled
by the cyclic queue, and unrestricted upper `q=3` is handled by a complete
reachability cut family rather than by an unsupported local shadow row.

## 9. Dependencies audited

The inputs used, with no new computational claim, are:

* `THREAD_D_STRICT_EQUIVARIANT_COMPACT_SHADOW_CIRCUIT_EXISTENCE_20260729.md`
  for the decorated forest/queue reduction;
* `MATH_THEOREM_DECORATED_MMM_ALTERNATING_SWITCH_AND_K15_SUPPORT_OBSTRUCTION_20260729.md`
  for the exact retained-segment, residence-span, and shadow ledgers;
* `MATH_CODE_AUDIT_AD_SHADOW_TOKEN_AND_FLOW_COMPRESSION_20260729.md`
  for the corrected unrestricted upper automaton, cut projection, counts,
  and strict `q=3` counterexample;
* `MATH_AUDIT_K15_JOINT_SHADOW_REPAIR_20260729.md` for the joint-scaffold
  scope and degree shortage; and
* `MATH_THEOREM_K15_RESIDENT_SHADOW_STATE_SWITCH_AND_RADIUS67_FLOW_OBSTRUCTION_20260729.md`
  together with `MATH_CERTIFICATE_K15_RADIUS67_DRAT_20260729.md` for the
  certified distance-67 obstruction.
