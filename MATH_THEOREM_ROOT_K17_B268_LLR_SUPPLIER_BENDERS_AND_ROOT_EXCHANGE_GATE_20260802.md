# K17 `b268` LLR supplier Benders and the root-exchange gate

**Date:** 2026-08-02  
**Status:** exact static transfer formulation, exact conditional supplier
Hall oracle, and finite same-table Pareto witnesses.  The current best frozen
supplier witness in this note has `438` transfers and rank `16802/16898`.
It is not a supplier optimum, a protected occurrence-state packing, a common
two-phase ticket state, a chronology, or a K17 word.

## 1. The two chain faces must be kept distinct

Put

\[
 L=\bigcup_{i=1}^6\binom{[17]}i,
 \qquad M=\binom{[17]}7,
 \qquad R=\binom{[17]}8.
\]

Their sizes are `21777,19448,24310`.  On the compressed-normal face, choose
`x_(m,r)` and `y_(l,m/r)` with

\[
\begin{aligned}
 \sum_r x_{mr}&=1 &&(m\in M),\\
 \sum_m x_{mr}+\sum_l y_{lr}&=1 &&(r\in R),\\
 \sum_{v\in M\dot\cup R}y_{lv}&=1 &&(l\in L),\\
 \sum_l y_{lm}&\le1 &&(m\in M).
\end{aligned}                                                    \tag{1.1}
\]

The counts force `16915` `L-M-R` chains, `4862` `L-R` chains, and
`2533` `M-R` chains.  Equivalently, the receiver set is a common basis of
`T_L` and `T_7^* direct-sum U_(16915,M)`.  This is the exact static layer in
which the rank-seven/root bank can change.

The present `b268` transfer lane is a different, histogram-equivalent face.
One transfer

\[
 (l<m<r)+(u<q)\longmapsto(m<r)+(l<u<q),\qquad l\subsetneq u,       \tag{1.2}
\]

creates one `L-L-R` chain and removes one `L-M-R` and one `L-R` chain.  For
`k` row-disjoint transfers the exact type ledger is

\[
 (LLR,LMR,LR,MR)=(k,16915-k,4862-k,2533+k).                       \tag{1.3}
\]

Thus `k>0` is outside the compressed-normal common-basis theorem.  The
rank-seven/root assignment `x` is unchanged by (1.2); roots and their owners
are pointwise fixed.  This lane is a lower/hit-state recoupling inside one
fixed root bank, not a substitute for root-type exchange.

## 2. Exact marginal transfer master

Let `E` be the authenticated `b268` structural catalogue.  An edge names an
old `LR` host `h`, an old `LMR` donor `d`, and the exact two replacement row
states in (1.2).  Let `p_e^0,p_e^1` be the supplied one-edge marginal price
bits.  The search geometry in this note is

\[
 E_\cap=\{e\in E:p_e^0=p_e^1=1\}.                               \tag{2.1}
\]

For `z_e in {0,1}`, the exact row-disjoint master is

\[
 \sum_{e\ni h}z_e\le1,\qquad
 \sum_{e\ni d}z_e\le1.                                         \tag{2.2}
\]

It may be intersected with `sum_e z_e >= k_min`.  Every integral solution
materializes literally by replacing exactly its selected endpoint pairs.
It preserves the full `65535`-target partition, every root and owner, the
histogram `(0,7395,16915)`, and every row excluded from all transfer
endpoints.

For the frozen fixture,

```text
structural edges                         93,234
marginal phase-0 positive                23,342
marginal phase-1 positive                25,173
marginal intersection                    11,893
maximum row-disjoint rank                   464
```

The last rank is an independently replayed maximum matching/minimum vertex
cover equality, not merely the size of a supplied matching.

## 3. Edge-labelled row modes and exact supplier recourse

For each physical row `v`, let `Sigma_v` contain its base state and one
state for every incident selected transfer.  The host state is edge-labelled
because its new first target is the donor's `l`.  Put

\[
 s_{v,0}=1-\sum_{e\ni v}z_e,
 \qquad s_{v,e}=z_e.                                           \tag{3.1}
\]

Let `K_(u,sigma;h,tau)` be the exact complete `6/9/4` supplier predicate for
supplier row `u` and hard-head row `h` in the named physical states.  Its
activation is the exact conjunction

\[
 w_{u\sigma,h\tau}
 =K_{u\sigma,h\tau}s_{u,\sigma}s_{h,\tau}.                     \tag{3.2}
\]

Both upper implications and the lower AND implication are required.  For a
mode-labelled head set `Q` and a supplier identity `u`, define the exact OR

\[
 n_{Q,u}=\bigvee_{h\in Q,\sigma,\tau}w_{u\sigma,h\tau}.         \tag{3.3}
\]

Again the OR is bidirectional.  For requested supplier deficiency at most
`delta`, the exact Hall row is

\[
 \boxed{\sum_{h\in Q}a_h-\sum_u n_{Q,u}\le\delta.}             \tag{3.4}
\]

For a fixed integral `z`, one maximum supplier matching and alternating
reachability return a maximally violated row (3.4).  Rebuilding the Boolean
master with every separated row is a finite exact Benders algorithm for the
supplier projection on (2.2).  The transfer matching and fixed-state
supplier matching are each integral; their state coupling is not claimed
to be TU.

A proof-safe implementation must bind the exact table, ticket ledger, edge
catalogue and both price ledgers; replay unique price-index coverage and
selection membership; require a complete SAT model and replay every clause;
recheck row disjointness and the transfer floor; and accept UNSAT only after
an independent proof run and an explicit `s VERIFIED` DRAT transcript.

## 4. Exact finite Pareto ladder

The authoritative parent is

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

and the selected-ticket row ledger is

```text
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1.
```

The baseline and the fully repriced deterministic descent are

```text
table       transfers    p0    p1   both  either   supplier   deficiency
b268             0      2687  1891  1422   3156     16796        102
common464      464      3119  2274  1864   3529     16767        131
DM descent     437      3097  2252  1838   3511     16801         97
```

The `437` table strictly dominates the parent on every displayed measured
coordinate.  Its supplier graph has `82` zero heads and maximum-deficiency
shore `111/14`.  The zero heads are `66` inherited baseline-zero surviving
`LMR` heads and `16` newly zero surviving `LMR` heads; no selected new `LLR`
head is zero.

Among the free/free marginal-common additions to this table, edge `57336`
is

```text
edge_index  lr_row  lmr_row  new MR bottom/root
57336       18089   16316    82007 / 82135.
```

Adding it gives a row-disjoint `438`-transfer table with exact supplier
projection

```text
rank 16802 / 16898, deficiency 96, zero heads 81, Hall shore 110/14,
graph FNV64 8106c32f061fb057.
```

The resulting type ledger from (1.3) is

\[
 (LLR,LMR,LR,MR)=(438,16477,4424,2971).                        \tag{4.1}
\]

This is the current supplier incumbent in this note.  It has not yet been
fully repriced for the four socket coordinates, so no socket improvement is
assigned to the additional edge.

## 5. Pricing and private-state recourse are separate gates

All `7213` rows named as private shorts, hosts, or endpoint tokens are
unchanged as table rows by every selected transfer above.  This proves a
literal row-footprint invariant.  It does not by itself prove simultaneous
retention of the ticket flags, witnesses, placements, and common state.

An independent audit found that the supplied marginal price witnesses reuse
protected rows:

```text
phase 0 protected witness occurrences             10,243
phase 1 protected witness occurrences             12,678
selected-common464 protected occurrences       227 / 255
selected fixed-host flag mismatches              93 / 106
```

This does not show that safe alternate witnesses do not exist.  It shows
that the supplied witness columns do not certify the stronger private-state
claim.

The `11893`-edge intersection is also marginal.  After materializing all
`464` supplied transfers and repricing the whole table, their new donor-short
rows split as

```text
both / p0-only / p1-only / neither = 429 / 2 / 4 / 29.
```

Therefore a promoted supplier finalist must be fully repriced.  Exact
secondary socket optimization requires final-table DNF recourse or a master
whose complete occurrence tickets imply the selected table states.  Transfer
cardinality is only a search proxy.

## 6. Residual fixed-bank boundary and root exchange

At the `437` table the direct zero-head deletion mechanism is exhausted on
the declared marginal-common face: the exact residual scan finds no legal
addition and no one-edge exchange whose selected donor/right endpoint is
one of the `82` zero heads.  Rank can still improve indirectly when a free
transfer changes supplier-row modes, or by repairing the `29` nonzero heads
in the `111/14` shore.  Edge `57336` is precisely such a positive indirect
move.

If the activated Hall closure proves that no further fixed-bank assignment
meets a requested deficiency, the proof applies only to (2.1)--(2.2).  It
does not obstruct the compressed-normal root-changing face (1.1), a larger
nonmarginal ticket face, or a different owner-phase transport.

The rank-seven fixed-root SCC theorem supplies the independent architectural
reason for retaining that escalation: even after deleting all lower-bottom
constraints, `162` of the old rank-seven zero roles remain unreachable while
the current receiver-root bank is fixed.  Changing root type is ordinary
transversal-matroid basis exchange.  In a common-basis implementation it is
an alternating path that retires one complement root and inserts another,
followed by fresh low and rank-seven representing matchings and guarded
socket/supplier recourse.

On every fixed integral hit/root face, the fundamental circuits are the
alternating even circuits of the corresponding bipartite matching.  The
authenticated prefix `C4` and rank-seven `C6` moves are the smallest such
circuits.  They are proof-safe harvest moves; they are not complete once a
hit state or complement-root basis element must change.

## 7. Frozen artifacts and live lane

The load-bearing local artifacts include

```text
q1 common-parent manifest
  03da5a0fec648efccd4072059364d512a9b2a0b04286cb2bc325dadfff578e5c
q1 DM-descent manifest
  351da2df010afdb672f2ea1de1b80e0e3d41d1223e36f5371eb5c360f2dbde05
437 selected / table / supplier audit
  e9704b820222d93f56bcbf348d202651f2ace1082e1fb65eb6c21fce88d2db25
  b6a51766dd8c7632a79f1f60abea26deced8cc5f40aec952bc8b704a3600c2b6
  2a5a5263c41d5b8fada2b26e8a97a6cccc4ae05ce70a579d71ced8e6dd6ef1e4
438 selected / table / supplier audit
  bbbe3d37474d7e5a2338ce678b76332a08a5b0c610d569c933a70b5970fe52b9
  7206ab1c9f3763aa0cfad7e88516753142d2bbbb858627b45fa3f49dee514655
  109e73ea926a7227e79de92a5623faff5db6ec06a9b1626002f34b786b4f569e
independent marginal/private scope audit manifest
  f965c01fba00cd7db87d1be7e73d3ecec9ffc339d71934f648fa1c53611c6646
```

The unique persistent H100 root is

```text
/home/amodo/or15/work/root_k17_b268_llr_supplier_benders_20260802/
```

The current exact search target is deficiency at most `95`, seeded by edge
`57336` and using all `11893` marginal-common edges with at least `438`
transfers.  A positive table is independently replayable.  A negative result
is promotable only with the hardened model/proof checks in Section 3.

## 8. Exact exclusions

Not proved here:

* optimal supplier rank on the `11893`-edge face;
* simultaneous protected private-ticket states or safe alternate witnesses;
* socket counts for the `438` table;
* one common occurrence-labelled phase state;
* phase-1 carrier-opening transport;
* residual outer matching, chronology, residence, upper/source/compiler
  closure, or a K17 word;
* a global obstruction after changing the rank-seven/root basis; or
* any TU claim for the coupled socket/supplier master.

