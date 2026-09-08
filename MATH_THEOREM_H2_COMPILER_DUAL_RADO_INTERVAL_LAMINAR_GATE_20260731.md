# Compiler dual-Rado under a common interval order

Date: 2026-07-31  
Lane: H2, bulk-compiler normalization/duality  
Status: exact conditional reductions and a literal sharp obstruction  
Scope: monotone-deadline, trace-guarded compiler banks with elementary
one-cell deletion tasks.  No all-dimensional Pascal list construction and
no `B(k)+O(1)` conclusion is claimed.

## 0. Result

Let `H=(T,C)` be a trace-guarded target--cell compiler graph with a
`T`-saturating matching, let `M=M_H^*` be the dual of its cell-side
transversal matroid, and let `L_i subset C` be the candidate cells for
elementary Pascal deletion task `i`.

Four precise statements hold.

1. If the old target neighbourhoods and the deletion lists are intervals in
   **one common order of cells**, the whole dual-Rado system is exactly the
   family of augmented interval-capacity cuts

   ```text
   #{t:N_H(t) subseteq J}+#{i:L_i subseteq J} <= |J|       (0.1)
   ```

   over cell intervals `J`.  Earliest-deadline matching is a constructive
   compiler.
2. If

   ```text
                    r_M(A) >= alpha |A|,                 (0.2)
   ```

   on every union of deletion lists, then for interval lists it is enough to
   check

   ```text
                #{i:L_i subseteq J} <= alpha |J|          (0.3)
   ```

   for every cell interval `J`.  These window cuts imply every Rado cut.
   For a laminar list family, it is enough to check (0.3) only on the
   distinct list sets themselves.
3. Neither monotone deadlines, trace guards, common interval geometry,
   laminar deletion lists, ordinary list Hall, nor full-ground scalar dual
   slack implies (0.1).  A literal four-cell example has one old target and
   three deletion tasks; every task is individually safe, the task lists
   have an ordinary SDR, and the full dual rank is three, but the interval
   `[1,2]` has load `3>2`.  Thus the first forbidden pattern is not a
   crossing pattern at all: it is a repeated interval contained in a
   dual-parallel class.
4. The canonical tail-start staircase does not natively produce elementary
   deletion lists: its deletions are coupled Ferrers ideals.  On one fixed
   compiler matching their exact condition is the depth-row prefix test
   `a_ell<=u_ell`; without an additional mobility braid, dual Rado is the
   wrong native abstraction.

There is also an authenticated *crossing* obstruction in the current K17
Pascal marginal atlas.  Every complete active `AA`, `X`, and `Y` inclusion
shore contains the inclusion-minimal Tucker triangle `M_I(3)`, so the full
Pascal inclusion bank has no common interval order.  This is not yet a
physical deletion-list no-go: the K17 chronology, staircase envelopes, and
elementary casualty lists have not been serialized.  On the already selected
degree-two support, exact cycle cuts delete `5,0,1` incidences on `AA,X,Y`
and make the three marginal banks interval-convex.

The authenticated K16 compiler reinforces the last point.  Its initial
marginal support freezes 14,059 universal assignments, whose cells are
coloops of that compiler transversal matroid and hence loops of its dual.
One further assignment becomes universal after guard filtering and the
first contraction.  The initial 14,059 already show that no positive uniform
density (0.2) can hold on the full bank.  A scalable density argument must
first contract the forced compiler assignments and exclude their dual-loop
cells from every Pascal deletion list.

## 1. Exact compiler specialization of dual rank

Let `r=|T|=nu(H)`.  For `D subseteq C`, the dual rank formula is

```text
 r_M(D)=|D|-r+nu(H-D).                                  (1.1)
```

By the bipartite deficiency formula this is also

```text
 r_M(D)=|D|-max_(X subseteq T)
                  (|X|-|N_H(X)\D|).                    (1.1a)
```

Consequently a Rado row for a task family `K` and

```text
                         U_K=union_(i in K)L_i
```

is equivalently

```text
 nu(H-U_K) >= r+|K|-|U_K|.                              (1.2)
```

Equivalently, for every old-target family `X`,

```text
             |N_H(X) union U_K| >= |X|+|K|.            (1.3)
```

Thus the compiler dual-Rado gate is literally the augmented Hall system,
not a new independent family of inequalities.

This is the exact robust-matching meaning of the bulk compiler dual.  Trace
guards are logically prior: they make every matching in `H` a literal
common-cap compiler, but they add no rank to `M` and imply no robustness
inequality such as (1.2).

Likewise, a monotone-deadline schedule supplies a line of physical positions
and a complete atlas of contiguous cells.  It does **not** imply that the
sets of cells incident with a lower target, or the cells offered to a
Pascal casualty, are consecutive in any one order of the cell objects.
That common-order convexity is an additional, directly auditable
construction property.

## 2. Exact common-order theorem

Fix an order

```text
                         C_1 < ... < C_m.               (2.1)
```

Call a prepared monotone-deadline compiler **jointly convex** when every old
target neighbourhood `N_H(t)` and every elementary deletion list `L_i` is a
nonempty interval in (2.1).

### Theorem 2.1 (jointly convex prospective compiler)

For a trace-guarded jointly convex bank, the following are equivalent.

1. There are distinct representatives `d_i in L_i` such that `H-D`,
   `D={d_i}`, still has a target-saturating matching.
2. The augmented interval cuts

   ```text
   #{t:N_H(t) subseteq [C_a,C_b]}
    +#{i:L_i subseteq [C_a,C_b]} <= b-a+1              (2.2)
   ```

   hold for every `1<=a<=b<=m`.

When they hold, sort the disjoint union of old targets and deletion tasks by
nondecreasing right endpoint and assign the first unused allowed cell.  The
cells assigned to deletion tasks are discarded; the old-target assignments
form a literal zero-defect common-cap compiler.

#### Proof

Make one augmented bipartite graph whose left shore is `T disjoint union I`,
with the old neighbourhoods and the lists as its incidences.  A matching of
this graph saturating the augmented left shore is exactly a set of distinct
task representatives plus a matching of `H` avoiding them.

Every left neighbourhood is an interval.  For any left subset `X`, its
neighbourhood is a disjoint union of intervals `J_1,...,J_s`.  Because each
left neighbourhood is connected, every member of `X` lies wholly in one
`J_h`.  Applying (2.2) to each component and summing proves Hall.  Necessity
is Hall applied to all rows whose complete neighbourhood lies in one
interval.  The standard earliest-right-endpoint exchange proves the greedy
algorithm.  Trace guarding promotes the retained old matching to an exact
common cap.  `square`

Thus interval convexity does more than simplify the abstract dual matroid:
it replaces all dual-rank calls by literal one-dimensional load cuts.

## 3. Uniform density times list expansion

The preceding exact theorem may be unavailable when the old compiler graph
is not jointly convex.  The proposed uniform-density route nevertheless has
a clean sufficient form.

### Lemma 3.1 (density--expansion product)

Assume that, for some `0<alpha<=1`,

```text
 r_M(A) >= alpha |A|                                   (3.1)
```

for every set `A` which is a union of deletion lists.  If

```text
 |union_(i in K)L_i| >= |K|/alpha                      (3.2)
```

for every task family `K`, then every dual-Rado inequality holds.

#### Proof

For `U_K=union_(i in K)L_i`, combine (3.1) and (3.2):

```text
                       r_M(U_K)>=alpha|U_K|>=|K|.
```

This is the Rado row.  `square`

If (3.1) is strengthened from unions of deletion lists to **every**
`A subseteq C`, it is equivalent to saying that the constant vector
`alpha 1_C` lies in the independent-set polytope of `M`.  If additionally
`alpha=r_M(C)/|C|`, it lies in the base polytope, so this strengthened form
is a uniform fractional dual-base decomposition.  Even the restricted form
used by Lemma 3.1 is substantially stronger than the single scalar row
`r_M(C)>=|I|`.

In particular, one must not substitute the average density

```text
                         alpha_bar=r_M(C)/|C|           (3.2a)
```

for the subset hypothesis (3.1).  The literal example in Section 6 has
`alpha_bar=3/4`, but its two-cell flat has density `1/2`.  The example
refutes average/full-ground density plus ordinary list Hall; it does **not**
refute Lemma 3.1, whose uniform subset hypothesis fails exactly on that
flat.

### Theorem 3.2 (interval-window reduction of expansion)

Suppose every `L_i` is an interval in one cell order.  Then (3.2) holds for
every task family if and only if

```text
                  #{i:L_i subseteq J} <= alpha |J|     (3.3)
```

for every cell interval `J`.

#### Proof

If (3.2) holds, apply it to all tasks whose lists are contained in `J`; their
union is contained in `J`, giving (3.3).

Conversely, fix `K`.  The union of its interval lists has disjoint interval
components `J_1,...,J_s`.  Each selected list is contained in exactly one
component.  If `K_h` is the corresponding task part, then

```text
 |K_h| <= #{i:L_i subseteq J_h} <= alpha|J_h|.
```

Summing yields `|K|<=alpha|U_K|`, which is (3.2).  `square`

Together, Lemma 3.1 and Theorem 3.2 prove a complete family of Rado cuts
from uniform dual density plus one-dimensional list load.

### Corollary 3.3 (laminar-list reduction)

If the distinct deletion-list sets form a laminar family, it is enough to
check

```text
             #{i:L_i subseteq A} <= alpha |A|          (3.4)
```

for each distinct list set `A`.

Indeed, the maximal selected lists in any task family are pairwise disjoint;
apply (3.4) to them and sum.  Conversely, (3.2) immediately implies (3.4).

### Corollary 3.4 (fixed unused-basis route)

Fix a target-saturating compiler matching `M_0`, and let `B` be its unused
cell bank.  Assume every `L_i` is an interval in the ambient cell order and
every `L_i cap B` is nonempty.  Order `B` by the induced ambient order.
Then every `L_i cap B` is an interval in this induced order, and an unchanged
compiler survives whenever

```text
 #{i:empty != L_i cap B subseteq [B_a,B_b]} <= b-a+1   (3.5)
```

for every interval of the ordered unused bank.  This is ordinary interval
Hall into one fixed dual basis.  It is often easier to certify than uniform
dual density and is stronger operationally: no compiler rerouting occurs.

## 4. The native tail-start object is a Ferrers ideal

The canonical monotone-deadline staircase does not natively export
independently movable one-cell tasks.  With depth `d`, write its non-tail
cells as `(i,ell)`, where `0<=i<W` and `1<=ell<=d`.  A nondecreasing
threshold vector

```text
                         0<=a_1<=...<=a_d<=W
```

deletes exactly

```text
                 D(a)={(i,ell):0<=i<a_ell}.            (4.1)
```

Thus the native options are Ferrers order ideals.  At fixed cardinality
they are not matroid bases: already for `d=2,W=4`, the ideals of
`a=(0,4)` and `b=(2,2)` violate basis exchange at `(2,2)`.  Splitting
`D(a)` into elementary Rado lists is therefore unsound unless a separate
physical braid proves independent one-cell mobility.

There is, however, an exact fixed-matching specialization.  For a compiler
matching `M_0`, let `u_ell` be the first start in depth row `ell` used by
`M_0` (or `W` if none).  Then `M_0` avoids the entire ideal `D(a)` if and
only if

```text
                         a_ell<=u_ell   for every ell.   (4.2)
```

This is the native tail-start analogue of Corollary 3.4: it is a row-prefix
test, not an elementary-list Rado theorem.  Trace guards must still be
certified for the final threshold vector because retiming changes the
protected physical intervals.

K16 calibrates the inequality with threshold `(0,0,6386)`, first used
starts `(0,2,6390)`, and residence frontier `(0,0,6384)`.  It does not prove
that this prefix margin regenerates.

## 5. The actual Pascal crossing pattern

For an `(r-1)`-set `K` and distinct exterior elements `a,b,c`, the complete
rank-`r` to rank-`r+1` inclusion bank contains rows

```text
                         K+a, K+b, K+c
```

and columns

```text
                       K+a+b, K+a+c, K+b+c.
```

Their incidence matrix is

```text
                             110
                             101
                             011,                       (5.1)
```

the Tucker matrix `M_I(3)`.  Making all three row supports intervals would
require all three pairs of columns to be adjacent, while a linear order of
three columns has only two adjacent pairs.  Deleting any one row or column
removes the obstruction, so it is inclusion-minimal.

The authenticated frozen K17 PBBS/Pascal marginal atlas contains such a
triangle on every complete active shore:

```text
 shore   targets   owners   incidences
 AA       5005      5005      35035
 X        5720      5720      41323
 Y        5720      5720      41336.
```

Thus Theorem 2.1 cannot be applied to the **unpruned complete Pascal
inclusion bank** under any owner order.  This is a hereditary structural
obstruction, not a defect of lexicographic, colexicographic, PBBS-sector, or
deadline ordering.

The selected incidence support has degree at most two.  In that case row
convexity is equivalent to having no alternating cyclic component: each
cycle asks a linear order to realize every adjacency of a cyclic order.
The authenticated selected supports have respectively `5,0,1` cyclic
components on `AA,X,Y`; deleting one incidence per cycle is both necessary
and sufficient for marginal intervalization.

These six cycle hits are a precise trace-guard design target.  They do not
yet prove a compiler: the existing K17 object is a lower-`q1` factor, not a
final connected chronology with a legal staircase, capped envelopes, and
elementary deletion tasks.  In particular, the displayed Pascal target
neighbourhoods must not be renamed deletion lists.

## 6. Literal monotone, trace-guarded obstruction

Take four physical positions in order and their singleton cells

```text
                         C={c_1,c_2,c_3,c_4}.
```

Use one middle owner `R={o,x}` on the whole interval, with fixed envelope
`{o,x}` at every position.  There is one residual lower target `S={o}` and
the guarded bank contains exactly

```text
                         S--c_1, S--c_2.               (6.1)
```

Each incidence is individually exact: cap its singleton by `{o}`, retain
`x` at positions 3 and 4, and the middle row still ORs to `{o,x}`.  Point
guard `o`, row guards at position 4, and the vacuous co-selectable edge
guards certify the bank.  The one-row start/deadline schedule is monotone
and chain aligned.

The cell-side transversal matroid has rank one on `{c_1,c_2}`.  Its dual
`M` has

```text
 r_M(C)=3,             r_M({c_1,c_2})=1.              (6.2)
```

Now take three independently movable deletion tasks with lists

```text
 L_1=L_2={c_1,c_2},          L_3={c_3,c_4}.            (6.3)
```

All lists are intervals and the list family is laminar.  It has an ordinary
SDR, for example `(c_1,c_2,c_3)`.  Every single task is compiler-safe, and
the full-family scalar row passes at equality:

```text
 r_M(L_1 union L_2 union L_3)=r_M(C)=3=|I|.            (6.4)
```

But the strict task family `{1,2}` violates Rado:

```text
                  r_M(L_1 union L_2)=1<2.              (6.5)
```

Equivalently, the augmented interval `[c_1,c_2]` contains one old compiler
row and two deletion rows, so its load is three and its capacity is two.

This is minimal in the relevant sense.  After all singleton task rows and
the full-family Rado row have been checked, a missed strict subfamily needs
at least three tasks.  With three tasks, full union rank at least three and
a two-element rank-one obstruction require at least one additional rank-two
outside bank, hence at least four ground elements.  The fixture attains both
bounds.  In particular, crossing intervals are not the first obstacle;
dual parallelism under a repeated interval already suffices.

## 7. Known-certificate calibration and the correct normalization order

The positive `k=11` bulk compiler is a useful but different Rado
calibration.  Its right-side matroid is the partition matroid on occurrence
blocks `R_Q`, with capacities `mu(Q)-1`.  Cyclic symmetry reduces its exact
system to 63 nonempty orbit-union inequalities, whose minimum margins on
three independent complete-shadow cycles are `2,4,3`.  This proves that a
structured bulk Rado system can close, but it does not prove density or
intervality for `M_H^*` in the prospective Pascal compiler.

There is now also an exact retrospective calibration on every stored optimum
`k<=16`.  If `H_A` retains only literal physical cells, grouped by their
literal lower OR label into disjoint blocks `G_S`, then

```text
 r_(M_(H_A)^*)(D)=|D|-#{S:G_S subseteq D}.             (7.1)
```

After fixing all singleton blocks, every remaining block has size at least
two, so this **literal** dual has sharp uniform density `1/2`; two-fold list
expansion is sufficient.  This is a genuine instance of Lemma 3.1 and a
partition/laminar normal form.  It remains retrospective: no stored optimum
exports the prospective Pascal task lists in the same order, and `H_A` is
not the much larger individually sound K16 guard bank discussed next.

At K16, the authenticated retained compiler bank begins with

```text
 cells       32229
 targets     26331
 incidences 347677
 dual rank    5898.
```

Its fail-closed forced closure finds 14,059 neutral universal assignments
in the initial marginal support and one further universal assignment after
unary guard filtering and the first contraction.  The fixed point has
12,271 targets and 237,467 incidences.

A cell used by every target-saturating matching is a coloop of `M_H`, hence
a loop of `M_H^*`.  Applying this to any of the initial 14,059 cells shows
that the original retained marginal bank has

```text
                  min_(nonempty A) r_M(A)/|A| = 0.     (7.2)
```

despite its large scalar dual rank and its authenticated exact compiler.
So the proposed all-dimensional proof must use the order

```text
 forced common-cap closure
 -> delete dual-loop cells from the Pascal option bank
 -> prove density on the movable residual core
 -> prove interval/laminar list expansion
 -> apply dual Rado.                                   (7.3)
```

The current K16 artifacts do not certify a common cell order for the
remaining target domains and hypothetical Pascal deletion lists, nor do
they certify a positive residual uniform density.  They are positive
compiler witnesses and a negative test of the unnormalized density claim,
not a proof of the bulk gate.

The same caveat applies to the stored `k<=14` optimal words: their explicit
first-occurrence assignments and scalar duplicate excesses certify completed
words, not prospective elementary deletion lists or uniform dual-base
decompositions.  No Rado list conclusion should be imported from them.

## 8. Exact remaining theorem for the O(1) route

A sufficient bulk compiler theorem now has a literal form.  For each
prepared Pascal lift, exhibit either:

1. one jointly convex trace-guarded augmented bank satisfying (2.2); or
2. after forced closure, a movable dual core satisfying (3.1), together
   with elementary option-transparent deletion lists satisfying (3.3) (or
   (3.4) on a laminar family); or
3. one fixed compiler matching whose unused basis satisfies (3.5).

Monotone deadlines provide the physical line on which to seek these
intervals, but do not prove any of the three alternatives.  Coupled
multi-cell Pascal options remain outside this theorem: splitting a coupled
block into elementary lists is unsound unless every cross-product choice is
physically realizable.

## 9. Audit and provenance

The dependency-free audit

```text
python3 scratch/audit_h2_compiler_dual_rado_interval_laminar_gate_20260731.py
```

checks every cell subset in (6.2), every representative tuple in (6.3),
every Rado row, every augmented interval cut, and both literal common-cap
replays.  It also authenticates the K16 forced-closure counts.  The JSON is

```text
scratch/h2_compiler_dual_rado_interval_laminar_gate_20260731.audit.json.
```

The audit deliberately does not infer a Pascal deletion-list catalogue or a
post-closure K16 density bound.
