# H22 graded `2575/2607` split: exact forced-pair collar min-cut

Date: 2026-07-28

Status: exact necessary-and-sufficient matching criterion, exact H22-zero-six
baseline audit, and executable separation oracle. The active frontier has
since advanced to H21 through a different component; this theorem remains a
reusable H21-to-H20 primitive with updated cell and rank parameters in
`THREAD_D_DM_COMPONENT_COMPRESSION_AND_H21_SPLIT_CURRENT_20260728.md`.

## 0. Result

The depth-zero proposal at cell `5617` is invalid. In the authoritative
H22/six-zero carrier that cell has descriptor

```text
(depth, start, envelope, mandatory, P-run)
= (0, 5617, 2574, 516, (2574)).
```

Coordinate pinning only replaces a controller letter by a subset. It cannot
add the missing coordinate and change `2574` to `2575`. More intrinsically,
an internal native depth-zero cell has rank five, whereas `2575` has rank
six. Thus cell `5617` is not incident with target `2575` and plays no part in
the corrected rank test.

The current deficient component is instead

```text
C = {2575,2607},     D = {17342}.
```

Cell `17342` has depth two, start `4467`, native trace `2607`, mandatory mask
`519`, and controller triple `(2601,2602,2604)`.

The required move is a graded cell split:

1. Create a distinct depth-one native cell `c1` for `2575`.
2. Retain a depth-two native cell `c2` for `2607` (in the fixed-slot test,
   `c2=17342`).
3. Retain the exterior matching capacity after both forced cells have been
   reserved.

On the focal targets, the old column is `(1,1)^T`. The endpoint columns,
ordered `(c1,c2)` and rows `(2575,2607)`, are

```text
[ 1  epsilon ]
[ 0  1 ].
```

Here `epsilon` may be zero or one, depending on the final mandatory mask.
The forced saturating assignment is `2575-c1, 2607-c2`; the local determinant
is one in either case. But that is only the local circuit test. The exact global test deletes
both targets and both reserved cells. The remaining graph must have matching
rank at least `16360`. Equivalently, one ordinary bipartite min-cut must be
at least `16360`.

## 1. Exact baseline

Let `G0` be the compiler graph of
`scratch/k15_segment_braid_hall22_zero6.json`, SHA-256
`bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778`.
The exact counts are

```text
targets = 16383, cells = 19311,
matching rank = 16361, deficiency = 22.
```

Both `2575` and `2607` have the single candidate cell `17342`. The full shore
of that cell is

```text
{519,527,551,559,2567,2575,2599,2607}.
```

Its restriction to the positive DM component is exactly `C`. Full exterior
sharing is therefore real: once `17342` is forced to `2607`, it must not be
counted again in the exterior flow.

Let `L° = L minus C`, and let `B0` be `G0` with the two targets and cell
`17342` deleted. Then

```text
|L°| = 16381, rank(B0) = 16360, deficiency(B0) = 21.
```

The lower bound is the old maximum matching after choosing `2607-17342` and
deleting that edge. A residual matching of size `16361` would combine with
`2607-17342` to contradict the old rank `16361`, proving equality.

The canonical tight alternating shore of `B0` is exactly the old positive DM
left shore with `2575,2607` removed. It has

```text
|S0| = 1004, |N_B0(S0)| = 983,
rank histogram = {4:6, 5:54, 6:272, 7:672}.
```

There is no depth-one native cell with trace `2575` in the current carrier.
So `B0` is an exterior baseline, not already a solution.

## 2. Literal graded predicate

For a controller `P=(P_i)`, a native depth-`q` cell at start `s` has trace

```text
tau_q(s) = union(P_s,...,P_(s+q)).
```

The corrected endpoint must contain distinct cell occurrences `c1,c2` with

```text
depth(c1)=1, tau(c1)=2575;
depth(c2)=2, tau(c2)=2607.
```

In the fixed-slot version, `c2=17342`. This by itself checks only the final
depth/start address. A genuinely transported-occurrence claim must also mark
the old occurrence through the braid and audit its transported profile;
merely finding the same slot, or an unrelated `2607` cell, is weaker.

If “split” is required literally inside one three-position run, then, up to
reversing the run,

```text
P_s union P_(s+1) = 2575,
P_s union P_(s+1) union P_(s+2) = 2607.
```

Since `2607 = 2575 union {coordinate 5}`, the first two letters lie inside
`2575`, while the third introduces coordinate five. The old triple
`(2601,2602,2604)` cannot itself contain this split: every letter contains
coordinate five and neither adjacent pair has union `2575`.

For two native cells, compatibility between these two pins is automatic with
the final maximal controller word `A=P`, even if their intervals overlap.
That does not certify other exterior pins, seams, residence, or protected
shadows; those remain separate conditions on the same final carrier.

## 3. Forced-circuit contraction theorem

### Theorem 3.1

Let `G-` be a target-to-cell graph with `N` targets, matching rank `n=N-h`,
and a transversal-matroid circuit `C` of size `s`. Let `G+` be a materialized
endpoint. Suppose

```text
Q = {x-c_x : x in C}
```

is a prescribed matching of distinct, physically legal cell occurrences.
Let `E_Q={c_x:x in C}` and `H_Q=G+ minus C minus E_Q`. Then the largest
matching of `G+` constrained to contain all of `Q` is exactly

```text
nu_Q(G+) = s + nu(H_Q).
```

Consequently, `Q` gives a one-unit gain over `G-` if and only if

```text
nu(H_Q) >= n + 1 - s.
```

#### Proof

Delete the `s` forced edges from any matching containing `Q`; what remains is
a matching in `H_Q`. Conversely, any matching in `H_Q` is disjoint from every
endpoint of `Q`, so adjoining `Q` gives a matching in `G+`. This proves both
claims. □

The theorem is reusable for every gap-one DM component. A native atlas on
`C minus {root}` plus a new root ear only specifies `Q`; the global exterior
test is still required.

### Corollary 3.2 (H22 graded split)

For `C={2575,2607}` and `Q={2575-c1,2607-c2}`, the endpoint has a matching of
size at least `16362` containing both graded edges if and only if

```text
nu(H_Q) >= 16360.
```

The graded pair replaces the old one-edge component matching and supplies the
new rank unit. The exterior must preserve `16360`, not `16361`.
This proves deficiency at most `21`; calling the endpoint exactly H21 also
requires a retained gap-21 shore or another matching-rank upper bound.

## 4. The single global min-cut

Build the standard unit-capacity bipartite flow network for `H_Q`:

* source to every target in `L°`, capacity one;
* every residual target-cell incidence, capacity greater than `16381`;
* every residual cell to the sink, capacity one.

Its maximum flow and minimum cut both equal `nu(H_Q)`. Equivalently,

```text
nu(H_Q) = min over S subset L° of
          (|L° minus S| + |N_G+(S) minus {c1,c2}|).
```

Therefore the exact all-shore condition is

```text
|N_G+(S) minus {c1,c2}| >= |S| - 21
for every S subset L°.
```

Both cells must be deleted. The capacity of `c1` is consumed by `2575`, and
the capacity of `c2` is consumed by `2607`. Counting either on an exterior
shore double-counts one occurrence, even when its full profile contains
other exterior targets.

A failed max-flow returns the exact violating shore. Thus one polynomial
min-cut separates the exponential family of Hall rows.

## 5. Exact collar-current signature

For `S subset L°`, define the old exterior cut slack and reserved current by

```text
eta_0(S) = |L° minus S| + |N_B0(S)| - 16360
         = 21 + |N_B0(S)| - |S|,

j_Q(S) = |N_G+(S) minus {c1,c2}| - |N_B0(S)|.
```

Every old slack is nonnegative, and the exact necessary-and-sufficient
signature is

```text
j_Q(S) >= -eta_0(S)    for every S subset L°.
```

A tight old exterior cut may lose no net cell capacity; a cut of slack `r`
may lose at most `r`. In particular, the first exact row is

```text
|N_G+(S0) minus {c1,c2}| >= 983.
```

This row is necessary but not sufficient alone. The min-cut in Section 4
enforces it and every mixed or near-critical shore simultaneously.

Relative to the unreduced H22 graph, put

```text
sigma_22(S) = 22 - (|S| - |N_G0(S)|),
J_Q(S)      = |N_HQ(S)| - |N_G0(S)|.
```

The equivalent signature is

```text
min over S subset L° of (sigma_22(S)+J_Q(S)) >= 1.
```

The `+1` is the desired Hall-rank gain. It disappears in the `B0` form
because `B0` has already contracted the old one-edge circuit matching.

### Occurrence-capacity form

Materialize the entire braid composition first. Cancel old and new cell
columns only when their full target profiles agree, retaining occurrence
multiplicity. Let `B-` and `B+` be the remaining old and new collar banks
after the old component cell and both final reserved cells have been removed
on their respective sides. Then

```text
j_Q(S) = sum over c in B+ of 1[Gamma+(c) meets S]
       - sum over c in B- of 1[Gamma-(c) meets S].
```

Each cell occurrence meeting `S` contributes one, no matter how many arcs
from that cell enter `S`. Point-degree derivatives and separately added
macro currents do not compute this expression unless overlapping physical
columns have first been composed and cancelled exactly.

## 6. Fixed exterior, rerouted exterior, and compensation flow

There are three different meanings of “retain the exterior.”

1. **Literal old edges.** If a fixed `16360`-edge exterior matching survives
   edge-for-edge and avoids `c1,c2`, adjoining the two forced edges gives
   `16362`. No further min-cut is needed.
2. **Same exterior targets, arbitrary cells.** Those targets must be
   independent in the residual transversal matroid, a Hall test on the
   protected target set.
3. **Only exterior rank retained.** The global min-cut of Section 4 is exact
   and permits all legitimate rerouting.

There is a smaller alternating-path realization of case 3. Let `K` be the
multigraph of full cell columns common to `B0` and `H_Q`, and put

```text
r_K = nu(K),     b = 16360 - r_K.
```

Fix a maximum matching of `K`, and let `kappa` be the maximum number of
vertex-disjoint alternating augmenting paths in `H_Q` from unmatched targets
to free cells. Symmetric difference gives

```text
nu(H_Q)   = r_K + kappa,
nu_Q(G+)  = 16362 - b + kappa.
```

Hence the exact compensation condition is `kappa >= b`. It is `b`, not
`b+1`: saturating the old `2/1` circuit already supplies the extra unit. The
residual network has only `21+b` unmatched target sources.

A **forced-pair-neutral** intermediate, meaning its best matching constrained
to contain the graded pair still has rank `16361`, has `kappa=b-1`; it has
exported exactly one deficit unit into the exterior, and a later splitter
must return that unit. Unconstrained Hall neutrality alone does not imply
this equality.

## 7. Why a component-only cut is unsafe

Take targets `rho,x,z`. Initially let one cell `a` serve both `rho,x` and one
cell `o` serve `z`, so `{rho,x}/{a}` is a `2/1` circuit and the old rank is
two. Replace `o` by a cell `e` serving `rho,z`. Locally, `rho-e,x-a`
saturate the old circuit, but the full three-target set still has only the
two cells `a,e`; the global rank remains two because `z` lost its independent
exterior capacity.

Thus neither the local 2-by-2 matrix, nor unions of old DM components, nor
old slack-zero shores alone are sufficient. The full forced-complement
min-cut is the sharp global certificate.

## 8. Executable audit and remaining gate

`scratch/audit_threadD_h22_graded_split_mincut.py` performs no braid search.
For any materialized candidate carrier it:

* rejects the obsolete depth-zero portal;
* finds depth-one native `2575` cells and the retained depth-two `2607` cell;
* reserves both targets and both cells;
* computes the exact residual matching rank and a violating canonical shore;
* evaluates its old slack plus collar current; and
* emits the violating target shore itself; and
* separately reports whether the chosen old exterior matching survives as
  the same indexed target-cell edges.

The base audit is
`scratch/threadD_h22_graded_split_mincut_base_audit.json`. It confirms the
baseline counts, finds no depth-one native `2575` cell, and therefore reports
no passing forced pair in the present carrier.

The precise surviving construction gate is:

> Find one deck-exact, residence-safe, all-upper-safe carrier braid whose
> final controller contains the native graded pair, whose complete protected
> pin family has one common physical word, and whose reserved exterior
> min-cut is at least `16360`.

The matching part is now completely characterized. What remains is physical
construction of the depth-one native cell together with nonnegative
**slack-plus-current margin** on every cut. The current itself may be negative
on a cut having enough old slack.
