# K17 q1-zero upper closed-shore circulation oracle

## Status

This note proves an exact upper-deck change formula for alternating incidence
circulations and freezes a positive finite `k=17` calibration.

The authenticated input factor covers all `19,412/19,412` required ordinary
non-`D` q1 colours.  Its best opened literal chronology is not q1-complete:
its rank-10-through-rank-13 hole vector is

```text
[22,1533,286,7]
```

and it has `5,586` short positive linear runs.  Ordinary q1 zero and opened
literal rank-10 zero are different gates.

On this factor there is a serial sequence of guard-safe, connected,
degree-preserving alternating circuits which keeps ordinary q1 zero and never
loses any upper target already covered by the selected opening.  The current
independently replayed Pareto checkpoints are

```text
main total-debt lane:  [10,386,4,0]  (400 total)
rank-ten-first lane:   [ 5,394,6,0]  (405 total)
```

from the original `[22,1533,286,7]` (1,848 total), without one upper loss.
Residence is not protected by this lane; the two checkpoints have respectively
`5,552` and `5,523` short positive runs in their best openings.  This is not a
source, compiler, or universal-word result.

## 1. Ordinary q1 is an additive circulation current

Let `Q` be an ordinary rank-eight root.  Write its two selected owners as

\[
Q+a,\qquad Q+b.
\]

If an alternating incidence circulation replaces the selected incidence
`Q--(Q+a)` by `Q--(Q+c)` while retaining `Q--(Q+b)`, its signed ordinary-q1
current is

\[
 [Q+\{b,c\}]-[Q+\{a,b\}].                 \tag{1.1}
\]

Summing (1.1) over the roots of a directed owner circulation gives the exact
change in every ordinary q1 provider multiplicity.  This is why ordinary q1
admits a min-cost-circulation or bounded-q1-debt formulation.

Formula (1.1) does **not** describe the opened exceptional `D` colours or any
deeper upper target.  Those depend on the physical owner chronology.

## 2. Exact fragment identity at every window width

Let

\[
T=(T_1,\ldots,T_n)
\]

be one opened owner chronology.  For a fixed owner-window length `ell`, write

\[
 \mathcal D_\ell(T)
 =\sum_{i=1}^{n-\ell+1}
   \left[\bigcup_{j=i}^{i+\ell-1}T_j\right]             \tag{2.1}
\]

as a formal multiset.

Toggle an alternating incidence circulation, and assume the resulting factor
is again one connected guarded lollipop.  Delete from the old owner word every
projected owner adjacency whose root is changed.  This cuts the word into
maximal fragments

\[
P_1,\ldots,P_s.
\]

The new chronology is another concatenation of these same fragments, with
some fragments possibly reversed.  Let

\[
\mathcal X_\ell(T;P_1,\ldots,P_s)
\]

denote the submultiset of (2.1) consisting of windows that cross at least one
fragment boundary.  Then

\[
\boxed{
 \mathcal D_\ell(T')-\mathcal D_\ell(T)
 =\mathcal X_\ell(T';P_1,\ldots,P_s)
  -\mathcal X_\ell(T;P_1,\ldots,P_s).
}                                                        \tag{2.2}
\]

### Proof

Every window wholly contained in one fragment remains a window after the
rethread.  Reversing a fragment reverses the order of the letters in such a
window but does not change their union.  Thus the complete internal multiset
of every fragment occurs with the same multiplicity before and after.  Remove
those common internal multisets from both sides of (2.1); exactly the two
cross-fragment multisets in (2.2) remain.  \(\square\)

If there are `s-1` fragment boundaries, at most

\[
 (s-1)(\ell-1)                                             \tag{2.3}
\]

length-`ell` windows cross an old boundary, and the same bound holds in the
new word.  This bound is useful for fixed widths.  It must not be misread as a
constant bound for the arbitrary-width deck: a low-rank union can persist for
a long physical interval.

## 3. Exact arbitrary-width closed-shore criterion

For an upper target `Z`, let

\[
 \mathcal W_T(Z)=
 \{[i,j]:\bigcup_{h=i}^jT_h=Z\}                           \tag{3.1}
\]

be its literal witness intervals.  Let `K` be the old cut-adjacency set of a
candidate circulation.  Define the passive count

\[
 p_K(Z)=\#\{I\in\mathcal W_T(Z): I\text{ crosses no edge of }K\}. \tag{3.2}
\]

Let `c_K'(Z)` be the number of witnesses for `Z` in the new chronology that
cross at least one new fragment boundary.  Then

\[
\boxed{
 Z\in\operatorname{Deck}(T')
 \iff p_K(Z)+c_K'(Z)>0.
}                                                         \tag{3.3}
\]

Indeed, every new witness either lies wholly inside one old fragment, in
which case it is one of the passive witnesses counted by (3.2), or crosses a
new junction, in which case it is counted by `c_K'`.  The two classes are
disjoint and exhaustive.

Define the cut-closed shore

\[
 R_K(T)=\{Z\in\operatorname{Deck}(T):p_K(Z)=0\}.           \tag{3.4}
\]

The circulation loses no currently covered upper target exactly when

\[
\boxed{
 R_K(T)\subseteq
 \{Z:c_K'(Z)>0\}.
}                                                         \tag{3.5}
\]

It is a strict upper improvement when, in addition, some old hole belongs to
the new cross deck.  This criterion includes the 22 exceptional opened
rank-ten holes; ordinary-q1 provider preservation is imposed separately by
(1.1).

Equation (3.5) is the exact version of the informal rule that an upper target
is lost precisely when every old witness is cut and no new crossing ladder
recreates it.

The same statement protects several openings simultaneously.  If the old
factor has opened words `T^omega` and the rethread induces opened words
`T'^sigma(omega)`, then literal containment of every old deck is equivalent
to imposing (3.5) separately for every `omega`, with the corresponding cut
and new-cross banks.  No aggregate hole-count comparison can replace these
conditions: equal counts may swap a covered target for a hole.  The joint
calibration below uses this two-opening form.

### 3.1 A bounded fragile shore

For a covered upper target `Z`, define its edge-transversal number

\[
 \tau_T(Z)=\min\{|K|:K\text{ meets the interior adjacency set of every }
 I\in\mathcal W_T(Z)\}.                                  \tag{3.6}
\]

Every upper witness has at least two owners, so its interior adjacency set is
a nonempty interval of chronology edges.  The interval transversal theorem
gives the equivalent packing form

\[
 \tau_T(Z)=\max\{t:\mathcal W_T(Z)\text{ contains }t
 \text{ pairwise edge-disjoint witnesses}\}.             \tag{3.7}
\]

If a circulation changes `c` old projected root adjacencies, then

\[
 \tau_T(Z)>c\quad\Longrightarrow\quad p_K(Z)>0.           \tag{3.8}
\]

Indeed, a `c`-element cut cannot meet every witness when the minimum
transversal has size greater than `c`.  Hence the exact closed shore (3.4) is
contained in the bounded fragile shore

\[
 \mathcal F_c(T)=\{Z:\tau_T(Z)\le c\}.                    \tag{3.9}
\]

For a C6 only `F_3(T)` needs an active recreation check; every target with four
edge-disjoint witnesses is passive automatically.  This is stronger than a
raw provider-multiplicity test because several witnesses may all cross the
same chronology edge.  The equality (3.7) follows by the usual earliest-right-
endpoint greedy algorithm for interval stabbing.

## 4. Bounded upper debt

Fix a protected bank `S`.  For a chronology `T` define

\[
 D_S(T)=S\setminus\operatorname{Deck}(T).                 \tag{4.1}
\]

A serial packet has upper-debt width `b` if every prefix stays in the frozen
guarded connected factor class and

\[
 |D_S(T_i)|\le b,                                         \tag{4.2}
\]

and it is accepting if `D_S(T_final)=empty`.  The monotone finite lane below
uses the strongest case `b=0`.

Debt alone is not a Markov state.  Two chronologies with the same missing
target set can have different fragments, passive witness banks, guards, and
future alternating circuits.  A sound bounded-debt search state must retain
the literal factor (or an exact equivalent boundary/fragment state) together
with the debt set.

### Monotone termination

If every accepted move satisfies (3.5) and adds at least one old hole, the
covered-target sets form a strictly increasing chain.  Starting with `H`
upper holes, such a run has at most `H` moves and ends either at zero holes or
at a strict closed-shore local minimum of the chosen actuator catalogue.  It
cannot cycle.  Thus a sampled plateau has a clean escalation order:

1. exhaust the present single-circuit catalogue;
2. enlarge to compound or longer circulations while retaining (3.5);
3. only then permit positive bounded debt (4.2).

## 5. Why the all-upper objective is not min-cost circulation

The q1 current (1.1) is a sum of root-local arc currents.  The deeper current
in (2.2) is different in two ways.

1. Even an interval crossing one new junction depends jointly on a suffix of
   one chosen fragment and a prefix of the next.
2. An interval may cross several new junctions, so its value depends on an
   ordered tuple of circulation arcs and on the induced global rethread.

Therefore no context-free cost on individual circulation arcs reproduces the
general upper objective.  A min-cost circulation is exact only on a specially
separated face where every relevant witness crosses at most one changed
junction and all suffix/prefix states have already been fixed.

The correct general architecture is:

1. a master chooses a guard-safe degree-balanced alternating circulation and
   enforces connected topology;
2. a literal separator reconstructs the two openings, evaluates (3.2)--(3.5),
   and returns every lost protected target;
3. the master receives either a full candidate no-good or a witness
   disjunction requiring one passive or new-cross provider for each violated
   target.

Thus the exact global problem is a **higher-order chronology-state problem
with Benders/CEGAR separation**.  Min-cost circulation remains the correct
inner oracle for ordinary q1 and can propose moves, but it is not the all-upper
oracle.

### 5.1 Residence is a finite junction state

The residence objective is materially easier than the all-upper objective.
Cut the root chronology at the projected adjacencies changed by a circulation.
For each fragment `P` and coordinate `x`, retain the binary boundary signature

```text
(first bit, last bit, prefix-one length, suffix-one length,
 all-one flag, internal short-run count),
```

with the two run lengths clipped at the required residence floor.  The
signature of a concatenation `PQ`, and its exact number of internal short
positive runs, is a deterministic function of the two signatures: only the
suffix run of `P` and prefix run of `Q` can merge.  Reversal merely exchanges
the two boundary fields.  Applying this independently to all coordinates
proves that exact residence change is an additive finite-state junction cost.

Consequently a joint oracle may lexicographically minimize residence after
the literal upper separator accepts a candidate without carrying arbitrary
window history.  The asymmetry is useful:

- ordinary q1 is a root-local additive current;
- residence is a bounded-memory fragment-junction current;
- the complete upper deck remains a genuinely higher-order ordered-fragment
  state and still needs the literal separator (3.3)--(3.5).

### 5.2 A common Lyapunov function

Let `R(T)` be the best linear short-run count and let `H(T)` be the larger
upper-hole count of the two protected openings.  Put

\[
 \Phi(T)=2R(T)+H(T).                                    \tag{5.2}
\]

If a both-opening closed move has residence change `Delta R` and creates at
least `g` new targets in each opening, then

\[
 \Delta\Phi\le 2\Delta R-g.                            \tag{5.3}
\]

Hence the exact acceptance rule `2 Delta R - g < 0` is a strict Lyapunov
descent even when one individual coordinate worsens.  In the larger
bounded-debt vocabulary, the two calibrated change vectors

```text
Q = (Delta R, Delta H) = (-1,+1)
V = (Delta R, Delta H) = (+3,-7)
```

both have `Delta Phi=-1`.  The hard-closed selector used below is stronger:
it forbids the `+1` upper step but uses the same potential to compare the
remaining candidates.  This common potential can cross a residence-first or
upper-first lexicographic plateau while remaining mathematically monotone.

### 5.3 Topology is not a packetwise invariant

Topology is also not additive in the packet supports.  In the joint
calibration, five root-disjoint individually safe child circuits composed to
one connected factor, while a sixth root-disjoint, individually safe and
literally applicable child made the terminal factor have two components.
Thus disjoint incidence support does not imply commuting preservation of the
global lollipop topology.  Connectivity must be replayed on the compound
terminal factor (or encoded in the master); it cannot be certified by summing
per-packet flags.

For a fixed factor, exact separation is cheap.  From each start position,
record only the moments when a previously absent coordinate first appears.
There are at most `k-r` proper upper arrivals per start.  Hence all upper
coverage can be replayed in

\[
 O(k\log k\,W+2^k)                                       \tag{5.1}
\]

time without enumerating all `Theta(W^2)` intervals.

## 6. Finite K17 calibration

### 6.1 Authenticated input

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
  q1zero.independent.model
SHA b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
```

Its best opened metrics are

```text
ordinary necessary non-D q1: 19412/19412
upper holes rank 10..13:      22/1533/286/7
best linear short runs:       5586
```

### 6.2 First strict closed-shore move

The first witness is the rank-seven-core C6

```text
core:       7045
labels:     3,14,6
old edges:  9025,40406,9191
new edges:  9022,40403,9196
```

It preserves all `19,412` ordinary q1 colours and all old opened upper
targets, and changes

```text
[22,1533,286,7] -> [22,1533,285,7].
```

The independent existing pipeline reports

```text
PASS_EXTEND_K17_H1_LAZY_PAIR_MODEL
PASS_K17_H1_COMPLETE_DIMACS_MODEL_REPLAY
  variables=1093878 clauses=7163170 literals=22610292
PASS_K17_H1_EXACT_Q1_CUT
  required=19412 covered=19412 missing=0 cut_literals=0
PASS_H1_GLOBAL_CONNECTED
  short_components=5585 best_linear_res=5587 best_linear_upper=1847
```

The first witness model has SHA

```text
64e0e626e2bc6cfe232395be12cc187b7cb954fc8f83a7141abe994356454e15.
```

### 6.3 Independently replayed chain-800 checkpoint

```text
model SHA
4fea86459eff1b8525d4437a0c0cb9f8d3e72949290d9fc11a91bbca54fe40c5

extended model SHA
a1d1b6b844e50c0a349ef3408ae21b34dd80596f2cc8b90fe3f0d44c8e633889

complete-CNF audit SHA
777306ca8ae7cb641d9dc98522b8fa797d9088679764d593d007e169b4e0c224

exact-q1 cut SHA (empty)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

passive audit SHA
d12cdd99e1922af73a3e1b91cbbe165b18c05cc1a9603ed1fea0924136989e39
```

The replay reports

```text
ordinary q1 provider histogram 0..9:
  [0,15041,3905,438,25,3,0,0,0,0]
upper holes rank 10..13:
  [15,746,46,0]
cyclic short components:
  5560
best linear short runs:
  5561
```

Every step was accepted only after literal clause, degree, boundary,
connectivity, ordinary-q1, and full upper-inclusion replay.  The catalogue was
seeded/random over current-state C6, rank-seven-core star-C8, and octahedral
C8 moves; it is not an exhaustive no-go catalogue at any later state.

### 6.4 Rank-ten-priority branch

A second lane started from `chain1000`, whose hole vector was
`[12,553,17,0]`.  Before performing the full upper replay it required a
candidate circuit to install at least one currently missing opened rank-ten
colour, and it retained the same strict closed-shore test (3.5).  Three C6
moves gave

```text
[12,553,17,0]
 -> [11,553,17,0]
 -> [10,552,17,0]
 -> [9,551,17,0].
```

The last state was independently extended and replayed:

```text
model SHA
9df371b5b5947d6d528293efbea566950fec5f2a42472a94088114992066446d

extended model SHA
8130abba08badf2ff6b5d040602f4fb3a6bfc04016fccdf0e278b93d2fbb692e

complete-CNF audit SHA
777306ca8ae7cb641d9dc98522b8fa797d9088679764d593d007e169b4e0c224

exact-q1 cut SHA (empty)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

passive audit SHA
71a5ec0ac57d727cabc532a4bd144361da1e50dbfdf6cd6e02ed966f93a9795c
```

Its ordinary q1 provider histogram is

```text
[0,15038,3920,423,29,2,0,0,0,0],
```

and its best linear residence debt is `5,543`.  A subsequent 50-million
proposal sample of the same local C6/star-C8/octahedral-C8 family found no
fourth strict rank-ten-gaining move.  This is a sampled local boundary, not an
exhaustive obstruction to a compound or longer alternating circulation.

### 6.5 Later independently replayed Pareto checkpoints

Continuing the total-debt branch gave

```text
round 1170 holes: [10,386,4,0]
model SHA:
d18db004c7840980d2ff980310f53e3b64a13b10f02c64bc994f83b15445d234
passive audit SHA:
43248db27476a5c0ef7c756972978d2f34ec73569a7e4a67c4724ce097704d25
q1 provider histogram:
[0,15044,3904,435,28,1,0,0,0,0]
best linear residence debt: 5552
```

Continuing from the rank-ten-priority checkpoint gave

```text
r10m123 holes: [7,430,9,0]
model SHA:
87f53fa5d238be09d9c93b7e442d849529f28d9a9bab919b6b607d1b8191fc2e
passive audit SHA:
28cecd7def54d77711c1680a4738489c5d8e23326568bce7d8f376178b442f62
q1 provider histogram:
[0,15041,3916,423,30,2,0,0,0,0]
best linear residence debt: 5550
```

Both checkpoints pass the independent 7,163,170-clause complete-model replay,
have an empty ordinary-q1 cut, and replay as one connected guarded lollipop.
They are retained as a Pareto pair because one minimizes total upper debt and
the other has three fewer opened rank-ten holes.

### 6.6 A longer circuit escapes the local rank-ten boundary

At `r10m71`, an exhaustive deduplication of the positive candidates emitted
by the bounded-path full-rank-ten circulation generator left 39 distinct
longer circuits.  Applying the exact separator (3.5) found one strict closed
move of length five:

```text
roots:     5365,1271,3287,1495,5589
old edges: 5745,446,2693,607,6157
new edges: 5743,445,2694,608,6159
```

It fills rank-ten mask `5375` and changes

```text
[8,482,11,0] -> [7,482,11,0]
```

without losing an old upper target.  Its independent replay is

```text
model SHA:
02b9d4b0cecd3ab52562a85359ce690188cf6e0a3fc1e81c49c1235f3a7a7a13
passive audit SHA:
37b3be2d9664805ac9b2162a83ec3368642ffb651b7eb54fd83c963facef44a5
full-CNF replay: PASS
ordinary q1 cut: empty (19412/19412)
connected: true
best linear residence debt: 5548
```

This is a concrete calibration of the escalation theorem: the
50-million-proposal local C6/C8 sample was not a true closed-shore barrier;
one longer alternating circulation crossed it without using positive upper
debt.

Continuing ordinary closed-shore moves from that escaped state reached

```text
longm29 holes: [6,455,9,0]
model SHA:
8be24b0784e5794477b5d796e36ba7253dbb01b667f779960401130bcc054a3d
passive audit SHA:
00c5c931c4939c2cbf9eb66ac1b9c17cf1e8e7f80cca98b5585b74eb0aa926de
q1 provider histogram:
[0,15038,3924,417,31,2,0,0,0,0]
best linear residence debt: 5543
```

This checkpoint also passes the independent complete-CNF, empty-q1-cut, and
connected-lollipop replays.

After further ordinary closed moves, a second longer-circulation catalogue at
`longm88` contained 34 distinct positive candidates.  Exactly one was closed:

```text
roots:     66267,66235,74395,78483,86675,82643
old edges: 116297,116246,132239,141077,156527,147841
new edges: 116291,116251,132244,141083,156523,147836
```

It fills mask `66303` and yields

```text
[5,394,6,0]
model SHA:
c979aef0c35b6753b19ef01a2c865d7c4f214dd9225011c07db4fef26fcec435
passive audit SHA:
944cb3c55aa8cc1352cdec36cdf91bb044c08fbbc77552090e930186eba8814a
best linear residence debt: 5523
```

The independent complete-CNF, empty-q1-cut, and connected-lollipop replays
all pass.  This is the retained rank-ten-first checkpoint.

### 6.7 Fragile-shore census

The interval-packing formula (3.7) was replayed literally.  The histogram
below has bins `tau=0,1,...,8,9+`; holes are excluded from the histogram.

```text
q1-zero input:
[0,20383,9797,4123,1863,953,595,389,233,1042]

main round 1139:
[0,21875,9925,3991,1762,915,602,386,281,1057]

r10m123:
[0,21878,9862,4033,1770,933,577,399,258,1070]
```

Thus a C6 automatically protects about five thousand covered targets by
`tau>3`; the remaining targets still require the cut-specific test (3.5).
The transversal theorem is a real exact reduction, but this census shows that
it is not by itself a small-shore theorem for the present chronology.  The
frozen audit SHAs are respectively

```text
15bb5013fdd6e518ea225417be8d2bd8e52e7f99b80fdc9ffef1aa57bb7eb2fd
68e4176adcdf74d43571f983ee6579950d47cf5508144f62e9d52bedf7cbdd29
c2f08e8545216fee1609bb999a0239ea9a38ba2623f78310684f2a78d4097830
```

### 6.8 Joint calibration in the low-residence component

The upper-only chains above began in the `5,500`-run basin, so by themselves
they did not show that upper repair remains available after the independent
residence descent.  The authenticated `res1980` checkpoint has

```text
ordinary q1:                 19412/19412
upper holes rank 10..13:     [0,1516,269,4]
best linear short runs:      1980
model SHA:
ad031d96fb53155c3671806a6c5294e04852f73814920b70dd5c87e72ad94c82
```

A 20-million-proposal joint envelope enumerated only literal upper-closed
circulations and selected lexicographically by `(upper holes, residence)`.
It contained `3,152` accepted closed candidates.  The winner was the star-C8

```text
core:       33913
labels:     13,1,14,12
old edges:  75418,59038,90856,67103
new edges:  75412,59039,90862,67102
```

and changes

```text
upper holes:  [0,1516,269,4] -> [0,1512,267,3]
best runs:    1980 -> 1983
```

without losing any previously covered upper target.  The independently
replayed frozen endpoint is

```text
model SHA:
833953e576c9e3c40f9f951d09ce74c3a9ff01b90628798048f791eca9c02c8c
independent audit SHA:
cad0b8adef1749f449984e01551237f105769377529f240a3275801d599f4cf9
q1 provider histogram:
[0,15106,3793,478,34,1,0,0,0,0]
```

This proves that strict upper repair is physically available inside the
low-residence component and that one useful move costs only three additional
short runs.  It does not prove a bounded-total-cost route to simultaneous
zero upper holes and zero residence debt; that requires a serial Pareto or
regeneration theorem.

The complete 20-million-proposal Pareto census is stronger.  Its rows are
`(upper gain, accepted count, minimum residence delta)`:

```text
(1,2084,-2)  (2,750,-2)  (3,251,-3)
(4,  46, 0)  (5,  6, 0)  (7,  2,+3)
```

Thus there are strict local moves improving both objectives, and closed
five-target upper gains with no residence cost.

Starting at the independently frozen `res1983` endpoint, a separate literal
descent then applied exactly six octahedral C8 moves.  Every prefix retained
both previous opened upper decks, not merely their cardinalities, and
preserved q1, guards, degrees, and connectedness.  The endpoint is

```text
best linear short runs:      1970
upper holes rank 10..13:     [0,1505,264,3]
model SHA:
959689e441fa3b2689ca3a6ec6bf458d7ab8899ca87183633449dca948c032c3
independent audit SHA:
83f30e0a8d3e38fef8aa4540f10fc1df442e58071e695c747bbd10e0f86df32a
manifest SHA:
e1fff19f7853d0fb3c3f8a0e3fee452bdb469e47c8c5ce7ff7c7f081995abb7f
```

Relative to the original `res1980` checkpoint, this serial path simultaneously
improves residence by `10` and upper debt by `17`.  It is the first frozen
joint-descent calibration; it still does not imply that the two debts admit a
common path all the way to zero.

Two independent 20-million-proposal oracles were then rebased on this
`res1970/1772` state and required aligned literal containment of **both** old
opening decks.

The strict-upper/nonworsening-residence oracle found

```text
best runs:     1970 -> 1969
upper holes:   [0,1505,264,3] -> [0,1503,263,3]
model SHA:
eac2d041b0941fd671255a55ca1bd48452abc0a5da7f1e9274272faeca31c3c2
audit SHA:
be0dddc2266491e9aedfe318996e3cc7934a77ffe30b906c1de5a1f0c19c647e
```

The maximum-residence-drop oracle found

```text
best runs:     1970 -> 1967
upper holes:   [0,1505,264,3] -> [0,1504,264,3]
model SHA:
f56a56a375119c337ed64d94bf22bfcf1ab9d17e144679c0f3d127f89bf43b43
audit SHA:
2834270f36a689fdf05bf39f0b680c6971d41f1ecfa1759f6b7bac2878847ce6
```

The second model is exactly the independently found `joint1967` parent in the
residence lane.  This is a cross-implementation reproduction of the same
strict joint step, rather than two related scalar summaries of different
states.

Subsequent connected batches continued the common descent:

```text
(R,H) = (1967,1771)
     -> (1961,1767)
     -> (1953,1764)
     -> (1948,1761)
     -> (1943,1748).
```

For the last transition, all five child circuits compose to one connected
factor.  Exact comparison against the `1948/1761` parent has zero losses and
thirteen gains in **each** opening.  Thus

```text
Delta Phi = 2*(-5) - 13 = -23.
```

The current fully replayed endpoint is

```text
upper holes rank 10..13: [0,1488,258,2]
artifact root:
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1943_deep1748/
manifest SHA:
2ad380e05f9eb366497537e9a2960ed2d09f45c384bcb9ea2eedf31839a2a93c
model SHA:
4570796ee9a5d084deb3f1e7522a35836c877b0c94797dd85636f61c9a251c2c
passive audit SHA:
a5f9366e9ba4c5ff7875a16914b5f289fd13416a715376d51e3c1f6373e50811
independent audit SHA:
351f663c7d6efcf0b96e0af1b5fbfffd6c248de6df77d30aad9063aa62ffd3bb
batch TSV SHA:
68ec020f0e7446cc55ae7957540fc9fa7ffd20ffd734713bea4f07f4d2a27e85
both-opening comparator audit SHA:
3618a6729b83109f21eef6c833deb24081fc02b948e9719765556fc42f648b06
containment table SHA:
e37cf2e6d66856b4052700119bf9c61486190cca912fe7b3512d8dc500faeb4a
```

This endpoint is a finite joint-carrier record, not a depth-three antecedent
or universal word.

A subsequent connected three-child subset strictly supersedes it:

```text
(R,H):                 (1943,1748) -> (1941,1743)
upper holes 10..13:    [0,1485,256,2]
artifact root:
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1941_deep1743/
manifest SHA:
cd3cfaf4f9e18193f5dccf3cee74311fbad30e09e84b01cf7669b6832aea6509
model SHA:
3254891f26ea96b094350861a8adf512a8fcb0af61c26c7b23da8be49c4f177d
independent audit SHA:
19dae06373bc8c0a8f97a6867f8d7dd75fca0e76eef17ff4dd413761d0705d60
passive audit SHA:
f86ca65893b87903831a140e1b647fa7cabacfcfaf96bb66d6fde002c388a271
both-opening containment audit SHA:
2e18e71ea0fb2b977acea860d7e0f256035e14b46223368c6008270bafaad4ff
containment TSV SHA:
b4554cf2d32b1276d22c7ebcdc127f9105e22d7dcdb11cfb03a13d150425729e
```

It gains five targets in each opening with no loss and has
`Delta Phi=2*(-2)-5=-9`.  This is the current authoritative joint record.

A later four-child subset gives the next authoritative record:

```text
(R,H):                 (1941,1743) -> (1938,1733)
upper holes 10..13:    [0,1478,253,2]
artifact root:
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1938_deep1733/
manifest SHA:
284f2db51bc432b2105396b993dc63bd8d682f775860ea63b05ef84f4ae91d59
model SHA:
fc6be42f7c52fa0d1da4733af10568adc1bb3e6a5b6d580f78920f11c6329d4b
independent audit SHA:
4692e42f1c3e8cc4bd34f42af5c54d9e42cde0198b02f86d5d7447dc2bb09f7e
both-opening containment audit SHA:
c05f835291bfd74f8061212ff9bfb566d847d5b184b938037a6d079098d2ecf9
containment TSV SHA:
49ea683315d9bd09539b4269bb1410969e1ccfa594dcf718af843d39b42af048
```

It gains ten targets in each opening, loses none, and has
`Delta Phi=2*(-3)-10=-16`.  A sibling `1939/1732` endpoint is retained as the
upper-Pareto alternative; the `1938/1733` endpoint minimizes `Phi`.

Continuing through the lower-residence Pareto branch gives the current
authoritative endpoint:

```text
(R,H):                 (1938,1733) -> (1935,1729)
                            -> (1930,1721) -> (1926,1712)
upper holes 10..13:    [0,1469,241,2]
artifact root:
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1926_deep1712/
manifest SHA:
44171fe48b108a2ec3b9bd10ea18daba52ba76b9b269168a3502c0ca6e6ab113
model SHA:
978386dff296a61195781aa23d0b4c85f0c671eb0ac59355a61aaa5e4851fbc3
passive audit SHA:
6aa9977c3ba115ee5d4d3dfb243cb98c1e980074ad9ac77b9b98e05c3f7215e4
independent audit SHA:
97c30214988f735889d89898e9e0c392367ae3285d606db4d643ab0d45fe16a8
both-opening containment audit SHA:
e34ce5e1afd8cbd6aa04fc90ddd4db97069171083167e357960b4867b9a96f59
containment TSV SHA:
c88ccc2ea59f76067785781743adb7bcfbca72242c81ddc2970bfe53b6d20fdf
```

The last batch has `Delta Phi=2*(-4)-9=-17`.  Relative to the first
`res1980/1789` joint checkpoint, the current record improves residence by
`54`, upper debt by `77`, and `Phi` by `185`, always under literal
two-opening containment at the frozen steps.

One further four-child batch gives the latest frozen record:

```text
(R,H):                 (1926,1712) -> (1923,1702)
upper holes 10..13:    [0,1463,237,2]
artifact root:
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1923_deep1702/
manifest-file SHA:
097ec68ba65380d442dcfe4018b673db3854729213847e12f4482707d99fc2ba
model SHA:
7a80fe02517039df87bcf7f88860b1bbf201482952c1317bfbcd6aeb9d435a2c
passive audit SHA:
5e5235733d25d4a127e26880604a92987ac6b265c8eeff0b50fe27838fd91308
independent audit SHA:
40ccf578cfe9cdac77f4e25806966784f65f5b9a3116b56d1953c6b4d717ffbd
batch TSV SHA:
ced90034bca1cc94eec14a99deef850f34ecbb2439942a257656fc1da005ada0
both-opening containment audit SHA:
74fd86d4d9235c0900427219bcce8f0a5568e9e5cdefece6157a934617760092
containment TSV SHA:
5f5d0cc71dd42599489bedcea7277ae38a90e69d0b56aa50df9123784aa06d7b
```

It gains ten targets per opening with no loss and has `Delta Phi=-16`.
From `res1980/1789`, the frozen path has now improved residence by `57`,
upper debt by `87`, and `Phi` by `201`.

Two independently replayed children of this checkpoint improve the joint
frontier again.  The `Phi` record is

```text
(R,H):                 (1923,1702) -> (1921,1694)
model SHA:
353a9e97239666e88f93b3fbf89fdee95240ef1a5099af408b28692f930a6f15
independent audit SHA:
b4395ceb2922b29ff33b00a36f698451f4c75be5e685bdc1af868258841a8747
comparison audit SHA:
08690d72401555e3517941b5ee78a8dec30106f96e156a18a976c8397f6af3a9
opening-zero and opening-one missing-list SHA:
c75a989c2fd1074e3ec5b500b869466ea53971b552811d22fa7bbf6004ae4c0a
```

It repairs eight old holes and loses no previously covered target in either
literal opening.  Thus `Delta Phi=2*(-2)-8=-12`, giving the new value
`Phi=5536`.  A sibling is the strict upper-Pareto record:

```text
(R,H):                 (1923,1702) -> (1922,1693)
model SHA:
bbfc5de584038755114d02acbd09972f0c60e2bb80d02d8343e195d1c4edb95e
independent audit SHA:
7f4777d4547d3e4aa79fb33193124c115d2f0c8d23643ed9a479c474c5603ea8
comparison audit SHA:
f13cb1216493b681fa75ab750ab615cf9008dbcf21e6452e3c7c6af74a9b308b
opening-zero and opening-one missing-list SHA:
8ed6c995ee70f6d560c90e94eb6ac2b85c9a56587564f6399b9dd43501487215
```

It repairs nine holes and loses none in either opening, for
`Delta Phi=2*(-1)-9=-11` and `Phi=5537`.  The common comparison parent has
audit SHA
`e804f2a4bfc4ef29e28e18f185bc3cba0301da4626e41f42a86a6d98567744a5`
and missing-list SHA
`ba721a7d7f76f765d43e07753915de1b224b2b0ffc90c87f2c90339a9e5e4329`.
The exact comparison artifacts are in
`/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/compare_joint1923_candidates_self/`.

The next independent portfolio produces three different terminals with the
same improved potential `Phi=5533`.  Exact self-replay followed by literal
set comparison against the relevant parent gives:

```text
terminal       old-covered losses   old holes repaired   both openings
1921/1691               0                    3                 yes
1920/1693               0                    1                 yes
1922/1689               0                    4                 yes
```

Their audit/missing-list SHA pairs are respectively
`c5e22a1e4289ef8ba2df6ea79a9b676a8076add5fd992134b50297d5b6c70140` /
`33520e59b5ff25a51125bb5255b87fd80998eb4ef61594bdcede22bd0ef6d2cf`,
`fb0fac697de0c5bd3362c4aa599643fb3a4d981a5df0f7ac7eb1a181d855be52` /
`dca4dcb4a11c14fd7474ecad56c995e4467481666073af4a0e4e2917ce2832d7`,
and
`339ce2868d747130f3d32acd124ef9bc7a5b135a1019f0f9555c5f3391008906` /
`29aa027dbac4dffc9bba4bc59deaafcf34b05cb3362490f6904ffe68e03084a4`.
The comparison root is
`/home/amodo/or15/work/root_k17_q1zero_upper_closed_20260802/compare_phi5533_children/`.
Thus `R=1920` and `H=1689` are the current certified Pareto extremes, while
all three terminals tie on the common Lyapunov function.

An immediately tempting scalar improvement to `1943/1744` was rejected by
the literal separator: in each opening it gained five targets but lost one
old target.  Thus the hole count fell by four while deck containment failed.
The frozen rejection has comparator-audit SHA
`23c33952a741a48ef0454047447ecea2344e8053dc04e625e99c341e9f7ded86`
and containment-table SHA
`366e35bebcb742fde0f19e3111e00ca0653a7fdc2975d350bd6960245eda5649`.
This is a concrete reason to retain the exact two-opening separator rather
than accept a numerical `H` cap alone.

### 6.9 Symmetric-difference bridge to the upper-only basin

The exact incidence symmetric difference between the frozen `1943/1748`
joint factor and the upper-only `[8,353,2,0]` factor has `18,504` incidence
edges (`9,252` removals and additions).  Pairing old/new incidences in sorted
order at every physical vertex decomposes it into `1,094` degree-preserving
alternating components:

```text
length 3: 602 components
length 4: 133
length 5:  64
maximum length: 1434
ambiguous local pairing vertices: 1799
```

The decomposition audit has SHA
`0950402a4faa78986851c2a1e23c6d0cb8511d2001571b1807a38315df4fc6ee`;
the component table has SHA
`6bd1143c24794b7d14220bd647bb05a1c5251c17ac4476419f3f5b1fabc652f9`.

Exact singleton replay gives:

```text
components:                    1094
q1/guard/topology replaying:    283
hard both-opening closed:       116
strictly Phi-decreasing:          7
```

The seven negative components are individually only `Delta Phi=-1`, but an
exhaustive `2^7-1` subset audit finds two six-component terminals with
`Delta Phi=-6`.  More strongly, the subset-state DP finds the literal monotone
ordered route

```text
0 -> 32 -> 48 -> 56 -> 58 -> 62 -> 63.
```

Every prefix passes q1, guards and connected topology, contains both previous
opening decks, and strictly lowers `Phi`.  The endpoint gains twelve upper
targets in each opening while increasing residence by three.  The scored
subset SHA is
`eed9a4d3353965923c6e7a7c949bb5ca30263ee90aece64567718bb30dcdfe60`;
the reachable-state and route SHAs are respectively
`e34f2dbdd59db17ef75cc01569a738d7faf6a7c290879d5ba077d26a42e0db33`
and
`1ed9932e1c30c6b812b8222c320845e6564980298af94f70a70481ddbf8dd992`.

This first bridge endpoint is dominated by the newer direct joint records.
Its significance is structural: a large remote factor can be decomposed into
exact alternating transactions, and a compound ordered subset crosses the
single-circuit plateau under the full literal invariants.  It is not evidence
that the complete 1,094-component path is feasible; most components fail an
individual guard, q1, topology, or deck gate.

## 7. Exact scope

Proved mathematically:

- the fixed-width signed fragment identity (2.2);
- the arbitrary-width closed-shore criterion (3.3)--(3.5);
- ordinary q1 is an additive circulation current, while the full upper deck
  is a higher-order rethread state with an exact Benders separator.

Proved computationally for the frozen K17 checkpoint:

- all frozen guards, degree rows, boundary incidences, and connected topology;
- all `19,412` ordinary q1 colours;
- literal upper inclusion at every accepted step;
- upper debt `1,848 -> 400` on the total-debt branch and rank-ten debt
  `22 -> 5` on the retained Pareto branch, with rank 13 completely closed.
- one independently replayed strict upper improvement in the `res1980`
  low-residence component, removing seven holes for residence delta `+3`.
- one independently replayed seven-move serial joint path (the precursor plus
  six octahedral C8 moves) which improves `res1980/1789` to `res1970/1772`.

Not proved:

- that the strict closed-shore chain reaches zero rather than a local minimum;
- residence preservation or repair;
- a depth-three source antecedent;
- lower compilation or a length-`24,313` word;
- `nu(17)=B(17)`.

The immediate next escalation at a strict plateau is not to weaken the
no-loss invariant.  It is to enlarge the master from one C6/C8 to a compound
closed-shore packet or an arbitrary alternating circulation, while applying
the same exact separator (3.5) to every prefix or only to the terminal state,
according to the licensed debt budget.
