# K16 generalized P/Q compiler: exact lower Hall gate and alternative-schedule search

**Date:** 2026-07-31  
**Status:** exact solver-free fixed-schedule no-go; exact search reduction for other P/Q schedules

## 1. Authenticated orders

The intermediate P9/P9 order is

```text
scratch/k16_facet_augmented_area29283_targets_20260731.word
SHA-256 7e47362fbe1535b758f566343b741ed379ae631b24a4b7c0cc73d83f3b477a71
```

with maximizing schedule

\[
 X=\{11838,11839,11840\},\qquad Y=\{331,332,5571\}.
\]

It is useful as provenance, but it is not the current carrier.  It has the
single target-order upper hole `0xef79`, and Section 6 below proves that this
hole has no legal physical pin in that fixed schedule.

The current order is

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43
```

It is obtained from the preceding order by the two inclusive reversals

```text
[5567,11365], then [11,11268].
```

Literal replay proves that it is a permutation of all `12870` rank-eight
masks and that its consecutive-block unions contain every target of ranks
9 through 16.  Its maximum-area realizable three-hole schedule is

\[
 X_0=\{5722,10950,10951\},\qquad Y_0=\{10,12,13\}.
\]

The complete schedule DP gives selected area `27588`, hence at most `27597`
lower cells after including all nine omitted-start cells.  This passes the
scalar requirement `26332`, but the exact Hall gate below does not.

## 2. General P/Q schedule and maximal envelope

Let $T=(T_0,\ldots,T_{W-1})$ be a fixed squarefree rank-eight order,
$W={16\choose8}=12870$, and $L=W+3=12873$.  For three-element sets
$X,Y\subset[0,L)$, write

\[
 P=[0,L)\setminus X=\{p_0<\cdots<p_{W-1}\},\qquad
 Q=[0,L)\setminus Y=\{q_0<\cdots<q_{W-1}\}.
\]

The P/Q schedule assigns row $T_i$ to

\[
 I_i=[p_i,q_i].
\]

It is a depth-three forward schedule when

\[
 0\le q_i-p_i\le3\quad\text{for every }i.                 \tag{2.1}
\]

Define the maximal physical envelope

\[
 E_j=\bigcap_{i:j\in I_i}T_i.                              \tag{2.2}
\]

The schedule is middle-realizable exactly when every $E_j\ne\varnothing$
and

\[
 \bigcup_{j\in I_i}E_j=T_i\quad\text{for every }i.         \tag{2.3}
\]

Indeed every physical realization satisfies $A_j\subseteq E_j$, while
$A_j=E_j$ proves sufficiency.  This is the generalized P/Q envelope; no
flat `sandwich2` identity or uniform $D^3A=T$ is assumed.

For the current schedule, the exact data are

```text
span histogram       0^1931 1^1 2^5227 3^5711
selected area        27588
zero envelopes       0
middle failures      0
envelope ranks       4^3 5^5705 6^5230 7^2 8^1933
chain breaks         0
```

## 3. Exact physical lower cells

Let ${\cal L}=\{S:1\le |S|\le7\}$, so $|{\cal L}|=26332$.

### Proposition 3.1 (P/Q lower-cell inventory)

The complete physical lower-cell inventory of a depth-three P/Q schedule is

\[
 {\cal C}(P,Q)=
 \bigcup_i\{[p_i,p_i+\ell-1]:1\le\ell\le q_i-p_i\}
 \;\cup\!
 \bigcup_{x\in X}\{[x,x+\ell-1]:1\le\ell\le\min(3,L-x)\}. \tag{3.1}
\]

For a selected start $p_i$, an interval reaching $q_i$ contains the
whole scheduled delivery of $T_i$ and therefore has rank at least eight;
precisely its proper prefixes can be lower.  At an omitted start there is no
selected row, so every depth-three prefix remains a possible lower cell.
Conversely every lower occurrence begins at either a selected or omitted
physical start and has length at most three.  This proves (3.1).

For $X_0,Y_0$, (3.1) has

\[
 |{\cal C}|=27588+9=27597.                                \tag{3.2}
\]

## 4. Exact individual-pin criterion

For every scheduled row-bit pair $(i,b)$, define its maximal host set

\[
 H_{i,b}=\{j\in I_i:b\in E_j\}.                            \tag{4.1}
\]

For a cell $C\in{\cal C}$, put

\[
 O_C=\bigcup_{j\in C}E_j,
 \qquad
 M_C=\{b:\text{some }H_{i,b}\subseteq C\}.                \tag{4.2}
\]

### Theorem 4.1 (one lower pin, if and only if)

A lower target $S\in{\cal L}$ can be imposed on $C$, while retaining
all scheduled middle rows, if and only if

\[
 S\subseteq O_C,\qquad M_C\subseteq S,
 \qquad E_j\cap S\ne\varnothing\quad(j\in C).              \tag{4.3}
\]

Necessity is immediate.  For sufficiency, use $E_j\cap S$ on $C$ and
$E_j$ outside $C$.  The first and third conditions make the pinned OR
exactly $S$ with no empty source cell.  If a row bit is absent from $S$,
the second condition leaves one of its hosts outside $C$; all row bits are
therefore still delivered.  This proves the claim.

The criterion contains every literal lower interval and is independent of
any choice of compiler letters.

## 5. The bipartite Hall theorem and the current no-go

Form the bipartite graph

\[
 G_\Sigma=({\cal L},{\cal C};E),\qquad
 S\sim C\iff\text{(4.3) holds}.                            \tag{5.1}
\]

### Theorem 5.1 (fixed-schedule lower Hall obstruction)

Every physical compiler for $\Sigma$ induces a matching saturating
${\cal L}$ in $G_\Sigma$.

Choose one physical witness cell for each lower target.  One cell has one
literal OR and cannot witness two distinct targets, so the chosen cells are
distinct.  Hence Hall is necessary.  In particular, any maximum matching of
size below 26332 is an unconditional no-go for that fixed P/Q schedule.

The exact current graph has

```text
left targets                    26332
right physical cells            27597
incidences                      293968
targets of degree zero            1478
maximum matching                24328
deficiency                       2004
canonical deficient shore       4029 / 2025
```

The last row is a literal Hall certificate:

\[
 |Z|=4029,\qquad |N(Z)|=2025,\qquad |Z|-|N(Z)|=2004.      \tag{5.2}
\]

Thus the maximum-area schedule $X_0,Y_0$ is **compiler-impossible**, even
though it is envelope-realizable, upper-complete, and has scalar capacity
1265 above the lower target count.  Of the deficit, 1478 units are already
singleton no-host rows; a further 526 units come from collisions among
nonempty rows.

If Hall were to pass, it would still not be sufficient.  For an injective
assignment $\phi:{\cal L}\to{\cal C}$, define the common cap

\[
 E_j^\phi=E_j\cap\bigcap_{S:j\in\phi(S)}S.                 \tag{5.3}
\]

That assignment is physically realizable exactly when every cap is nonzero,
all middle row ORs remain $T_i$, and every selected cell OR is its assigned
target.  The maximal capped word $A_j=E_j^\phi$ proves sufficiency.  Hence
Hall is the correct first exact gate, followed by this common-cap gate.

## 6. The old `ef79` debt and its removal

For the intermediate SHA `7e47362f...`, the target order has no consecutive
block with union `0xef79`.  More strongly, the exact arbitrary-width physical
pin test has no legal interval.  For a proposed interval $J$, cap its
envelopes by $U=\mathtt{0xef79}$.  It is individually legal exactly when

1. $E_j\cap U\ne\varnothing$ for every $j\in J$;
2. their union is $U$; and
3. $J$ contains no complete host set $H_{i,b}$ with $b\notin U$.

The exhaustive interval recurrence returns zero legal minima.  Therefore
`ef79` can never be produced by any legal physical interval under that fixed
target order and fixed P9/P9 schedule.  Independently, its lower graph has
matching `25256/26332`, deficiency `1076`, including `890` no-host targets.

The two reversals remove this upper obstruction.  In the current target
order,

```text
rows 11363..11366:
c671, c879, a879, 6d38
```

have union `ef79`.  Their scheduled physical union is positions
`11366..11369`; the generic cap checker also finds legal minimal pins
`[11365,11369]` and `[11366,11369]`.  There are no upper holes of any rank.

## 7. Exact search for another P/Q schedule

The preceding no-go is for one schedule, not for the current target order.
Other $X,Y$ must be screened as follows.

### 7.1 Mandatory staged gate

For every three-hole P/Q schedule:

1. enforce (2.1), the envelope conditions (2.2)--(2.3), and
   $p_{i+1}\le q_i+1$ (`CHAIN`);
2. require the exact cell-count bound
   \[
   \sum_i(q_i-p_i)+\sum_{x\in X}\min(3,L-x)\ge26332;       \tag{7.1}
   \]
3. build (4.1)--(5.1) and reject any degree-zero target;
4. run capacitated or ordinary bipartite matching and reject positive Hall
   deficiency;
5. only after Hall passes, solve the common-cap problem (5.3) and replay all
   65535 masks.

Because the current target order is upper-complete, `CHAIN` transports every
target-order interval witness to a literal physical interval.  A search
which drops `CHAIN` must instead install the complete physical upper-pin
oracle; that larger architecture is not covered here.

The maximum-area row has selected area 27588.  An alternative schedule can
lose at most 1265 cells (when all omitted starts retain three cells), so an
area-maximizing DP alone is not a completeness proof.

### 7.2 Exact event DAG and backward capacity pruning

Scan physical positions as in the schedule DP.  Immediately before position
$j$, retain

\[
 \sigma_j=(x_j,y_j,Q_j),                                  \tag{7.2}
\]

where $x_j,y_j$ count used start/deadline holes and $Q_j$ is the ordered
queue of accumulated ORs of active rows.  A transition chooses whether $j$
is a start hole and/or a deadline hole, intersects the appropriate contiguous
target block, updates every accumulator, and checks an ending row exactly.
This is a finite acyclic state graph and is the same exact envelope recurrence
as the scalar DP.

Compute on this DAG the maximum possible remaining area $A^+(j,\sigma)$.
A history with prefix area $a$ is pruned whenever

\[
 a+A^+(j,\sigma)+\text{remaining omitted-start credit}<26332. \tag{7.3}
\]

Unlike the scalar optimization, histories reaching the same $\sigma$ may
not be merged merely by keeping the largest area: their past Hall graphs can
differ.

### 7.3 Exact Hall profile state

For a lower cell define its neighborhood profile

\[
 \pi(C)=\left(O_C,M_C,\{E_j:j\in C\}\right).              \tag{7.4}
\]

Equation (4.3) shows that two right cells with the same profile have exactly
the same target neighborhood.  They may be contracted to one profile vertex
with integer capacity equal to its multiplicity.  Thus an exact merge key for
the Hall screen is

\[
 (j,\sigma_j,\text{unfinalized depth-three boundary collar},
                    (c_\pi)_\pi).                         \tag{7.5}
\]

It is safe but potentially large.  A cell starting at $s$ is final after
position $s+2d-1=s+5$: by then every row which could place a host in that
cell has ended.  Hence the boundary collar in (7.5) has constant width.

For the current schedule this quotient is only modest: `27597` cells have
`26740` distinct exact neighborhoods.  Profile compression is therefore a
correct representation, not by itself a promised asymptotic collapse.

### 7.4 Sound optimistic Hall pruning

At a partial event-DAG history, keep all finalized right cells exactly.  For
each pending or future physical cell identity $C$, let

\[
 \widehat N(C)=\bigcup_{\text{legal completions of the history}}N_\Sigma(C).
                                                                    \tag{7.6}
\]

Use one optimistic right vertex with neighborhood $\widehat N(C)$.  Every
completion graph is a subgraph of this optimistic graph.  Therefore:

* a target absent even from the optimistic graph gives an exact zero-host
  prune;
* a maximum matching smaller than 26332 in the optimistic graph gives an
  exact Hall prune.

The sets in (7.6) are finite local tables: a depth-three cell depends only on
the current $(x,y)$, the nearby target rows, and the remaining hole events
in its constant-width collar.  They can be generated directly from the event
DAG, without SAT and without assuming that independently possible future
profiles occur simultaneously.  The latter independence is deliberately an
optimistic relaxation, which makes every rejection sound.

### 7.5 Adjacent-hole sensitivity

Move one start or deadline hole by one physical position, preserving a valid
schedule.  The hole-count paths differ at only one position, so exactly one
maximal envelope cell changes.  Any altered row-bit host set belongs to a row
through that position.  Such a row lies between positions \(c-d\) and
\(c+d\).  A length-at-most-\(d\) cell which contains its remaining hosts can
start as early as \(c-2d+1\) or as late as \(c+d\).  On the common universe
of all possible `(start,length)` cells, at most

\[
 3d^2=27                                                   \tag{7.7}

right vertices change.

Consequently the matching number is 27-Lipschitz under an adjacent legal
hole move.  Starting from deficiency 2004, no path in the valid adjacent-move
schedule graph can reach Hall feasibility in fewer than

\[
 \left\lceil2004/27\right\rceil=75                         \tag{7.8}

moves.  This does not rule out a distant schedule; it rules out treating the
current row as a shallow local Hall defect.  Exact dynamic matching and a
zero-host bitset need update only this constant halo after each move.

### 7.6 Exact top-256 schedule census

To test whether another near-maximum-area schedule repairs the defect, retain
the 256 largest-area histories at every full event-DAG state (7.2).  This is
an exact K-best dynamic program, not a beam: after two histories reach the
same complete state, every continuation and every future area increment is
identical, so discarding the 257th prefix cannot remove a top-256 terminal
history.

The exact terminal area histogram is

```text
27588^1 27587^4 27586^11 27585^24
27584^47 27583^83 27582^86.
```

Every one of these schedules passes the envelope recurrence and the scalar
capacity test.  For a proof-safe Hall screen, first retain only the selected-
start proper-prefix cells.  The three omitted starts are then granted nine
completely arbitrary additional right vertices.  Since nine new vertices can
raise a matching number by at most nine, selected deficiency greater than
nine is an unconditional full-schedule rejection, regardless of the omitted
cells' actual neighborhoods.

All 256 schedules fail this stronger optimistic test:

```text
selected Hall deficiency histogram
  2006^6 2007^76 2008^110 2009^51 2010^13

zero-host count range
  1478..1483
```

The best row after nine arbitrary-cell credit is K-best row 90,

```text
X = {5718,10950,10951}
Y = {10,12,14}
selected area              27583
selected matching          24326 / 26332
selected deficiency         2006
deficiency after credit      1997
Hall shore              4029 / 2023.
```

Thus the exact near-area frontier through rank 256 is closed.  This is not a
claim about the remaining (11328629291855246030195-256) realizable
schedules.  It does show that moving among the highest-area endpoint choices
does not address the dominant no-host/Hall geometry; a useful schedule must
be genuinely distant or the target order must be rethreaded again.

## 8. Scope

The fixed-schedule UNSAT is unconditional inside the displayed generalized
P/Q schedule.  It does not exclude a different three-hole schedule for the
same upper-perfect target order, a schedule without `CHAIN` supplied with
separate upper pins, a different target order, or a non-P/Q compiler.

The alternative-schedule algorithm is proof-safe: terminal rejections are
exact, while every optimistic or resource-limited survivor remains open.

## 9. Reproducible artifacts

```text
scratch/audit_threadD_k16_generalized_pq_compiler_hall_20260731.py
  SHA-256 88f1e6b7d58c7220fdfc41678b59b55487e93833fce9ca725db0f8ac48aa7bca

scratch/threadD_k16_uppercomplete27597_three_hole_schedule_dp_20260731.audit.json
  SHA-256 1ea8b93d84b616cf63751ba46cd55ac1ac73ecb835aef1b6edf5c565770a5b77
  payload 65762c8b0deff2df664d5321bccc057678711a51e42bc9561fd8300a94238313

scratch/threadD_k16_uppercomplete27597_pq_compiler_hall_20260731.audit.json
  SHA-256 6919bf664e195805d93c02a4050eb1fa51fa38b27ed93f3f6585d8cbb3954c3a
  payload 03c38753ad9f4eb4b4cd2d2e86d67f6986c0f22ada1511ef4458c520797c61f0

scratch/threadD_k16_area29283_pq_compiler_hall_20260731.audit.json
  SHA-256 eaf8a7c12389f2b4ae66ef6c69f18844ff65087a54d32bcf2ac22e27ba8250eb
  payload bae256ae1bbe7ecd2c6fdbc4f550cb815e6e98f1fb5dd1164dcca834ecf73356

scratch/threadD_k16_uppercomplete_pq_kbest_20260731.py
  SHA-256 abb94950ccf7fafc72c0bab5e9c78c1aa503224295b499f01d2550dfb4bf35d7

scratch/threadD_k16_uppercomplete_pq_kbest_hall_screen_20260731.py
  SHA-256 66484fcaaa8f38078e8107994a44267bc086e0480be132c098c4dd3e481213cd

scratch/threadD_k16_uppercomplete_pq_kbest256_20260731.json
  SHA-256 c5aec9fedb240c3b709cb921ca16e29844ec94f98857bf70136648479d94500b
  payload e9762486083901d6322e7e011c1ee1c0fcd6c58f7fdb5c7ce1c69cb914f09632

scratch/threadD_k16_uppercomplete_pq_kbest256_hall_20260731.json
  SHA-256 6f7f4fc61fd5bc0af09a75dc046c484b89ec86ae2531b2db42ec161346198aef
  payload c6f28aae5d51720ffe3c7a83ea4faf2e97d37342c46ff85836deb7adfb4a96a8
```

The checker imports no solver.  Each full K16 Hall audit used one local
process, about five seconds, and under 100 MB resident memory.
