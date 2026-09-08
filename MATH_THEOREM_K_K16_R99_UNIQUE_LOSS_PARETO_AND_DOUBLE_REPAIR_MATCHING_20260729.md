# The `k=16` radius-99 unique-loss Pareto frontier and double-repair matching tax

Date: 2026-07-29  
Lane: K  
Status: **solver-free exact deletion-side DP; endpoint-feasible matching tax proved; degree/q1 completion remains open**

## 0. Main theorem

Work in the loopless `C_15` quotient catalogue about the audited re-centered
factor `F_1`.  Among its selected edges, exactly 675 are unique providers of
their lower q1 row and exactly 673 are unique providers of their upper q1
row.  Give a selected edge the loss bit

\[
 w(e)=(w_L(e),w_U(e))\in\{0,1\}^2,
\tag{0.1}
\]

where a bit is one precisely when `e` is the unique selected provider in
that palette.

For every radius-99 motif-hitting cut `C`, let

\[
 L_1(C)=\sum_{e\in C}w_L(e),
 \qquad
 U_1(C)=\sum_{e\in C}w_U(e).
\tag{0.2}
\]

These count rows certainly lost by the cut.  They are lower bounds on all
lost rows because a row with several selected providers can also disappear
if all of them are cut.

The exact Pareto frontiers are as follows.

### Retain `22511`

\[
 \boxed{
 \mathcal P_R={(50+j,63-j):0\le j\le13\}.
 }
\tag{0.3}
\]

Thus

\[
 \min_C(L_1+U_1)=113,
 \qquad
 \min_C\max(L_1,U_1)=57.
\tag{0.4}
\]

### Delete and replace `22511`

\[
 \boxed{
 \mathcal P_D={(49+j,62-j):0\le j\le13\}
 \cup\{(64,48)\}.
 }
\tag{0.5}
\]

Hence

\[
 \min_C(L_1+U_1)=111,
 \qquad
 \min_C\max(L_1,U_1)=56.
\tag{0.6}
\]

Any exact 99-seam completion preserving both q1 palettes must therefore
contain at least

\[
 \boxed{14}
\tag{0.7}
\]

seams which simultaneously repair a lost lower and a lost upper row in the
retain branch, and at least

\[
 \boxed{12}
\tag{0.8}
\]

in the delete branch.  The exceptional delete point `(64,48)` requires 13.
These simultaneous seams must form a pairwise label-distinct matching which
coexists inside one endpoint-restoring `b_C`-factor.  This is strictly
stronger than scalar occurrence capacity or a compatibility graph assembled
from mutually incompatible seam choices.

## 1. Exact component DP

The 147 current residence motifs have 390 selected edges and 85
edge-overlap components with pairwise-disjoint supports `E_i`.  The selected
exterior bank

\[
 X=F_1\setminus\bigcup_iE_i
\tag{1.1}
\]

has 468 edges.

The audited radius-99 normal form has two branches.

* In the retain branch, the conditioned local optima sum to 98 and the
  excess budget is one.
* In the delete branch, the ordinary local optima sum to 97, component 5 is
  required to contain `22511`, and the excess budget is two.

For component `i`, grade `g`, and a local hitting set `S`, record

\[
 (g,L_1(S),U_1(S)).
\tag{1.2}
\]

Let `P_i(g)` be the set of loss pairs attainable after the first `i`
components using excess `g`.  The recurrence is the finite Minkowski sum

\[
 P_{i+1}(g)=
 \bigcup_{h=0}^g
 \bigl(P_i(g-h)+Q_{i+1}(h)\bigr),
\tag{1.3}
\]

where `Q_i(h)` is the local loss-pair set at grade `h`.  At fixed excess,
coordinatewise dominated pairs may be discarded: every future component
and exterior cut contributes a nonnegative pair, so a dominated state can
never become Pareto-minimal later.  Finally, use exactly the remaining
budget on distinct edges of `X` and Pareto-prune once more.

This recurrence is exhaustive because the 85 component supports and `X`
are disjoint, and the branch excess equations are exact.  It is not a fit to
the stated answer.  The replay enumerates every local option directly from
the motifs and independently obtains aggregate grade counts

\[
\begin{array}{c|ccc}
 &0&1&2\\ \hline
\text{retain}&262&958&-\\
\text{delete}&261&960&3442.
\end{array}
\tag{1.4}
\]

The dominance-pruned final tables contain 54 and 87 loss pairs before the
last Pareto operation, yielding exactly (0.3) and (0.5).

The selected-source loss-bit histogram is

\[
 (1,1)^{522}(1,0)^{153}(0,1)^{151}(0,0)^{32},
\tag{1.5}
\]

which independently gives the totals 675 and 673.

## 2. The endpoint-feasible double-repair theorem

Fix a radius-99 cut `C`.  Let `b_C(v)=d_C(v)` and let

\[
 \mathcal B(C)=\{A\subseteq E^+:
 |A|=99,\ d_A(v)=b_C(v)\text{ for every }v\}
\tag{2.1}
\]

be its loopless endpoint-restoring seam factors.  Let `Lambda_C` and
`Upsilon_C` be the palette-tagged unique lower and upper rows lost by `C`.

For `A in B(C)`, define `m_C(A)` to be the maximum number of seams in a
subset `M subseteq A` such that

1. every seam of `M` has lower label in `Lambda_C` and upper label in
   `Upsilon_C`;
2. the lower labels in `M` are pairwise distinct; and
3. the upper labels in `M` are pairwise distinct.

Put

\[
 \kappa(C)=\max_{A\in\mathcal B(C)}m_C(A),
\tag{2.2}
\]

with value minus infinity when no endpoint factor exists.

### Theorem 2.1 (double-repair matching tax)

If `C` has a degree-two, both-q1-preserving 99-seam completion, then

\[
 \boxed{
 \kappa(C)\ge L_1(C)+U_1(C)-99.
 }
\tag{2.3}
\]

#### Proof

Let `A` be an actual completion.  For each row in `Lambda_C`, choose one
restoring seam of `A`.  Because one seam has only one lower label, these
witnesses form a set `A_L subseteq A` of size `L_1(C)`.  Similarly the lost
upper rows give `A_U subseteq A` of size `U_1(C)`.  Since `|A|=99`,

\[
 |A_L\cap A_U|
 \ge |A_L|+|A_U|-|A|
 =L_1(C)+U_1(C)-99.
\tag{2.4}
\]

Every seam in the intersection repairs both a lost lower and a lost upper
row.  Injectivity within each witness family makes both label projections
pairwise distinct.  Most importantly, all these seams lie in the same
endpoint-restoring factor `A`; they are not merely individually legal
provider edges.  Thus they form an admissible set in (2.2), proving (2.3).
QED.

Combining (2.3) with (0.4) gives the uniform retain bound 14.  Combining it
with (0.6) gives the uniform delete bound 12; at `(64,48)` it gives 13.

The theorem has a hereditary form.  For any subsets
`Lambda' subseteq Lambda_C` and `Upsilon' subseteq Upsilon_C`, their chosen
witnesses must overlap in at least

\[
 |\Lambda'|+|\Upsilon'|-99
\tag{2.5}
\]

seams of the same endpoint factor.  This supplies endpoint-conditioned
Hall/Benders cuts once a problematic colour subfamily is identified.

## 3. Why ordinary colour matching is weaker

Form the raw compatibility graph between `Lambda_C` and `Upsilon_C` by
joining two rows whenever some off-source seam has those labels.  A full
completion certainly requires a matching of size at least the right-hand
side of (2.3).  But this graph may combine seams which cannot coexist under
the endpoint deficits.  Even restricting each seam to positive-deficit
endpoints is insufficient: the chosen seams may compete for endpoint
capacity or may not extend to a full `b_C`-factor.  The exact invariant is
`kappa(C)`, not the raw matching number.

The audit nevertheless calibrates these relaxations on one lexicographic
cut witnessing every Pareto point.  All 29 canonical cuts have 198 distinct
deficit endpoints, so `b_C(v)=1` on their ports.  For each, an exact
four-way packing was computed among seams with

* distinct lower labels,
* distinct upper labels, and
* four distinct endpoint resources across each pair of chosen seams.

The results are

\[
\begin{array}{c|c|c|c}
 &\text{required}&\text{port-colour matching}&
   \text{unit-endpoint four-way pack}\\ \hline
\text{retain}&14&20\ldots23&19\ldots22\\
\text{delete}&12\text{ (or 13)}&20\ldots23&19\ldots22.
\end{array}
\tag{3.1}
\]

Thus the first colour/positive-port/endpoint-packing tests do **not** exclude
these canonical Pareto witnesses.  The displayed four-way packs are not
claimed to extend to complete 99-edge endpoint factors.  This is a sharp
negative calibration: the remaining obstruction, if any, lies in extension
to one full `b_C`-factor, restoration of nonunique lost rows, top residence,
or their coupling.

## 4. Consequence for the hard-radius programme

Radius 99 is no longer an undifferentiated 76,000-variable question on the
deletion side.  Every candidate factor must first pass one of two exact
branch filters:

\[
 \kappa(C)\ge14
 \quad\text{(retain)},
\tag{4.1}
\]

or

\[
 \kappa(C)\ge12
 \quad\text{(delete)},
\tag{4.2}
\]

with 13 forced at the exceptional Pareto point.  Any endpoint-conditioned
matching upper bound below these thresholds is a solver-free branch
certificate.  Passing them proves neither degree completion nor q1
completion.

The clean next theorem is an extension theorem or obstruction for
`kappa(C)`: characterize which simultaneous repair matchings extend to a
99-edge loopless `b_C`-factor while covering the remaining lower and upper
rows.  A valid algorithm should return endpoint-factor Benders cuts to the
85-component DP rather than collapse back to scalar loss counts.

## 5. Frozen audit

The source and exact radius-99 cutspace certificate are

```
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8

scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json
SHA-256 b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e
```

Independent solver-free replay:

```
scratch/audit_k16_r99_unique_loss_pareto_double_matching_20260729.py
SHA-256 b172835d13063669164348b7443275d67e76abb9aaece999750f963588c36020

scratch/k16_r99_unique_loss_pareto_double_matching_20260729.audit.json
SHA-256 5b069eb052ab126e2e2eeca74c0c79db995c6bd83fc41533e18d16846b6d87d4
```

The replay performs no SAT, CP, ILP, or heuristic search.  It reconstructs
every graded local hitting set, runs the exact nonnegative Pareto recurrence,
replays one explicit cut per frontier point, and performs exact finite
matching/four-way-packing calculations on those canonical witnesses.  It
does not claim a radius-99 factor, top residence, or a new word.
