# The Hall-service UNIT-controller replacement graph is acyclic at `k=15`

Date: 2026-07-28

Status: exact finite no-go for pairwise separated single-controller-state
edits using only the 1,602 UNIT pins in the retained Hall-service atlas.
It does not exclude auxiliary UNIT compensation edits; those form directed
cycles in the full controller graph.  Interacting multi-state circuits,
non-UNIT moves, and a new carrier are also outside its scope.

## 1. Restricted move model

Let

\[
 T_0,\ldots,T_{W-1}\in{[15]\choose8},\qquad W=6435,
\]

be the frozen middle chronology, and let

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i
\]

be its maximal erosion controller.  For a flat Hall-service UNIT pin `(p,x)`
from the retained positive-defect atlas, consider only an **isolated
one-state edit**

\[
 P'_p=P_p-\{y\}+\{x\},\qquad P'_j=P_j\quad(j\ne p).
\tag{1.1}
\]

The edit is locally admissible when:

1. `P'_(p-1),P'_p,P'_(p+1)` remains a Johnson path;
2. every affected four-window union has rank eight; and
3. every affected consecutive pair of middle windows remains Johnson-adjacent.

The UNIT property says that among the four middle windows containing `P_p`,
exactly one old state `T_q` omits `x`.

### Lemma 1.1 (one middle replacement)

Every locally admissible edit (1.1) changes exactly that one state:

\[
 T_q\longmapsto T_{q'},\qquad q'\ne q,
\tag{1.2}
\]

and leaves all other middle states fixed.

#### Proof

The four affected unions are recomputed directly.  Adding `x` changes only
the unique one which omitted it.  Rank eight forces the deleted coordinate
`y` to disappear from that union, while the other three unions must retain
`y`; otherwise one of them drops to rank seven.  Hence exactly one union
changes.  Since the old chronology enumerates every rank-eight set, its new
value is `T_(q')` for a unique `q'`.  The edit is nontrivial, so `q'!=q`.
\(\square\)

Thus every locally admissible UNIT edit defines a directed replacement arc

\[
                         q\longrightarrow q'.
\tag{1.3}
\]

## 2. Exact exhaustive census

The retained atlas has 1,602 Hall-service UNIT pin types.  Exhausting every
possible deletion `y in P_p` gives:

\[
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{flat UNIT pins with one locally admissible edit}&1318\\
\text{flat UNIT pins with none}&283\\
\text{left-boundary UNIT pin outside this model}&1\\
\text{locally admissible replacement arcs}&1318\\
\text{vertices in the replacement digraph}&2295.
\end{array}
\]

Every one of the 1,318 admissible pins has exactly one admissible deletion.
Kahn elimination removes all 2,295 vertices.  Therefore:

\[
 \boxed{\text{the retained Hall-service replacement graph is acyclic}.}
\tag{2.1}
\]

Only 14 of the 24 pins in the displayed optimistic Hall-29 incidence
certificate admit even this isolated local edit.  This observation concerns
that witness only; (2.1) concerns all 1,602 pins in the retained service
atlas, not all theoretical controller UNIT pairs.

### 2.1 The ambient graph has cycles

If every theoretical flat unique-omission pair `(p,x)` is admitted, rather
than only pins which currently expose a Hall target, the counts become

\[
\begin{array}{c|r}
\text{theoretical UNIT pairs}&13122\\
\text{locally admissible arcs}&10370\\
\text{replacement vertices}&6359\\
\text{arcs in nontrivial strongly connected components}&3445.
\end{array}
\]

There are seven nontrivial strongly connected components, of sizes

\[
                     2266,5,5,3,3,3,3.
\tag{2.2}
\]

In particular the ambient graph is not acyclic.  The three pairwise
separated operations

\[
\begin{aligned}
 (1058,8,2,1055,3724),\quad
 (3724,2,3,3724,6430),\quad
 (6430,3,8,6430,1055)
\end{aligned}
\tag{2.3}
\]

form a directed 3-cycle; each tuple is `(p,x,y,q,q')`.  Simultaneous direct
recomputation preserves the complete rank-eight deck and every middle
Johnson adjacency.  Auxiliary UNIT edits can therefore close deck circuits.

There is also a pairwise-separated 23-cycle containing retained service pin
`(96,7)`.  It preserves the exact middle deck, but loses five immediate-upper
colours and does not realize the advertised singleton target `1920`: its
forced deletion is coordinate `8`, which that target needs.  This distinction
between **deck compensation** and **physical service** is essential.

## 3. Separated-family no-go

### Theorem 3.1

No nonempty family of pairwise distance-at-least-eight isolated one-state
edits drawn solely from the retained Hall-service UNIT atlas preserves the
exact middle deck.

#### Proof

At separation eight, the affected controller neighborhoods, four-window
blocks, and their Johnson-adjacency tests are disjoint.  Hence every chosen
edit has exactly the independent form (1.2), and its source indices `q` are
distinct.

Initially every middle value occurs exactly once.  After the chosen edits,
the old value `T_q` disappears at every selected source `q`.  Exact deck
preservation therefore requires each disappeared value to be supplied by
exactly one selected replacement.  Equivalently, the chosen arcs must have
indegree and outdegree one on their selected source set, so they are a
nonempty disjoint union of directed cycles.  This contradicts (2.1).
\(\square\)

The same proof works for any separation convention strong enough to make
the local edit supports independent; distance eight is used because it also
separates the depth-three physical collars in the current Hall repair lane.

### Theorem 3.2 (isolated physical service is impossible)

None of the 1,318 locally admissible Hall-service operations retains any of
its advertised target/cell addresses after its forced deletion.

#### Proof

For every operation and every advertised record, replace `P_p` by
`P_p-y+x` and recompute the union of the controller states in that physical
cell.  Exhaustion gives

\[
 S\nsubseteq\bigcup_{j\in I_c}P'_j
\]

in every case.  Thus no pinning `A'_j subseteq P'_j` can realize `S` on that
cell.  The failure is not the originally missing coordinate `x`; the unique
locally legal deletion removes another coordinate required by the target.
\(\square\)

For example, pin `(2237,2)` advertises singleton cell `6308`.  Its only
locally legal deletion is `y=7`, giving controller state `6181`, which no
longer contains target coordinate `7`.

An independent enlarged two-state enumeration reaches the same frontier.
Among all `1,011,150` choices of two distinct theoretical UNIT states at
distance at most seven, with at least one Hall-service pin, `30,442` preserve
the controller Johnson adjacencies and `28,379` retain rank-eight middle
windows, but none is an exact middle-deck circuit.  Therefore a complete
state-replacement repair using a Hall-service edit changes at least three
controller states.  This does not exclude a target-safe local block which
exports deck imbalance to a larger distant compensation circuit.

### Proposition 3.3 (the first target-safe export blocks)

If local deck closure is relaxed but every controller, middle-rank, middle-
adjacency, maximal-erosion, and target-envelope condition is retained, the
same two-state census contains exactly 59 target-safe blocks.  Each exports
two directed deck-replacement arcs.  Exactly three have both exported arcs
routable in the ambient UNIT graph, allowing either the direct or crossed
pairing at the level of unconstrained reachability:

\[
\begin{array}{c|c|c}
\text{controller edits}&\text{exported arcs}&\text{served target}\\ \hline
(3151,12,13),(3152,11,13)&3148\to685,\ 3149\to4452&6308\\
(3266,12,6),(3267,11,6)&3263\to3120,\ 3264\to3121&6308\\
(3268,2,6),(3269,12,6)&3268\to2236,\ 3269\to2237&6308.
\end{array}
\tag{3.1}
\]

Here each edit tuple is `(p,x,y)`.  These are the first exact local blocks
which retain a Hall address while respecting the controller geometry.  They
are not completed circuits: the two closing paths share or approach
controller positions where isolated-edge composition is invalid.  The next
finite gate is therefore a position-conflict two-commodity circulation for
one row of (3.1), followed by the physical pin and upper-shadow audit.

## 4. Consequence for the positive program

The optimistic 24-pin incidence cover cannot be interpreted as 24
independent Hall-service-only local controller repairs.  The full theoretical
UNIT graph contains auxiliary compensation pins and is not acyclic.  Any
successful UNIT repair must therefore use at least one of the following
genuinely collective mechanisms:

1. a target-safe interacting block together with auxiliary UNIT edits outside
   the Hall-service atlas which close its exported deck imbalance;
2. overlapping controller edits whose four-window effects interact;
3. a multi-state alternating circuit which permutes the middle deck as a
   whole;
4. a reordering of the middle chronology rather than point replacement;
5. non-UNIT or mandatory-defect records; or
6. a different carrier/compiler pairing.

This is compatible with the direct degree-two circuit lane: the necessary
move is a closed multi-state deck circuit, not a bank of separated pin
collars.  It also explains why the controller congruence and the named-pin
flow must be enforced at circuit level.

## 5. Reproduction

Run

```text
python3 scratch/audit_k15_unit_pin_isolated_cycle_nogo.py
python3 scratch/audit_k15_full_unit_compensation_cycles.py
python3 scratch/audit_k15_two_state_service_export.py
```

The first script reconstructs all Hall-service UNIT pins from the Hall atlas,
exhausts every deletion, checks every local rank and adjacency condition, and
verifies the complete topological elimination.  The second reconstructs the
full ambient graph, both explicit cycles, the zero physical-service count,
and the upper-colour loss of the 23-cycle.  The third verifies all 1,011,150
two-state choices, the 59 target-safe export blocks, and the three ambient-
reachable rows of (3.1).

The O3 circuit census is

```text
clang++ -O3 -DNDEBUG -std=c++20 \
  scratch/search_k15_full_unit_service_circuits.cpp \
  -o /tmp/search_k15_full_unit_service_circuits
python3 scratch/export_k15_full_unit_service_instance.py |
  /tmp/search_k15_full_unit_service_circuits 2
```

after compiling `scratch/search_k15_full_unit_service_circuits.cpp`.  Its
two-state count was independently reproduced in Python.  All assertions are
scoped to one-coordinate-for-one-coordinate controller replacements; broader
rethreadings remain open.
