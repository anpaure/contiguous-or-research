# K16 WIDTH45: exact physical point interface and restricted cycle-column master

Date: 2026-07-30  
Lane: R  
Status: proved interface theorems and implemented fail-closed checker; no
integral `C=103` construction is claimed here.

> **Subsequent resolution.**  The checker and physical interface below remain
> authoritative.  Complete safe-cycle enumeration has now excluded all three
> integral count-103 ledgers in this frozen catalogue; see
> `MATH_THEOREM_R_K16_WIDTH45_C103_COMPLETE_SAFE_CYCLE_EXCLUSION_20260730.md`.

## 1. Frozen data and scope

This note concerns only the frozen asymmetric K16 carrier and the WIDTH45 seam
interface authenticated by

* `scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256
  `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`;
* `scratch/k16_width45_provider_path_dual_20260730.audit.json`, SHA-256
  `115ce4dfbcfdbd652c0696f21c6f44b5ed58737f16752fa1e5bd203477c12f4a`;
* `scratch/k16_width45_symmetric_scale4_potential_20260730.audit.json`,
  SHA-256
  `1b7676e70e209dd2437c042e93eb11a853e35da2899452c1200c188b82d42920`.

There are 12,870 ports, 211,604 directed seams, 93 residual targets, and 150
new WIDTH45 endpoint-pair occurrences.  Each new occurrence has split 2 or 3
(75 of each) and exactly three authenticated collateral cut positions.  The
scale-four target weights sum to 408.

Nothing below asserts reverse-edge legality, retained q1 witnesses, survivor
constraints, shadows outside the frozen 93-target bank, connectedness, COMP3,
boundary absorption, or literal-word validity.

## 2. The full fractional occurrence rows

For a directed seam `e=(u,v)`, let `x_e` be its seam mass.  Let

```
d_a = sum_{e leaves a} x_e = sum_{e enters a} x_e
```

be the cut mass at port `a`.  Endpoint capacity is `0 <= d_a <= 1`.  Cyclic
global Sep5 is

```
sum_{j=0}^4 d_{a+j} <= 1
```

at every position of every frozen source component, with indices cyclic in
that component.

For one of the 150 WIDTH45 occurrences, write its three authenticated
collateral cuts as `Z(e)={z1,z2,z3}` and its activator as `w_e`.  The complete
linear occurrence interface is

```
0 <= w_e <= x_e,
w_e + d_z <= 1                 for every z in Z(e),
w_e >= x_e - sum_{z in Z(e)} d_z.
```

These are 150 upper rows, 450 collateral rows, and 150 lower rows.

### Lemma 2.1 (explicit WIDTH45 activation under fractional Sep5)

For every nonnegative balanced capacity-one seam circulation satisfying global
Sep5, the explicit assignment `w_e=x_e` satisfies all of the above rows for
all 150 authenticated occurrences.

### Proof

For a split-2 occurrence, one collateral lies one position before `u` and two
lie one and two positions after `v`.  For split 3, two lie one and two
positions before `u` and one lies one position after `v`.  Thus every
collateral `z` lies with either `u` or `v` in a length-five Sep5 window.
Nonnegativity gives `x_e<=d_u` and balance also gives `x_e<=d_v`.  Hence the
appropriate Sep5 row gives

```
x_e + d_z <= d_u + d_z <= 1
```

or the same inequality with `v`.  With `w_e=x_e`, the upper and collateral
rows follow.  The lower row becomes
`x_e >= x_e-sum_z d_z`, which follows from nonnegativity.  This checks every
row.  QED.

The lemma says that `w=x` is a feasible explicit choice.  It does **not** say
that Sep5 forces `w=x` at a fractional point.  Consequently a fractional
physical replay must either provide all 150 activators or explicitly request
the assignment `w=x` and then verify all 750 rows.  Merely augmenting each
seam's hit list is not an independent replay.

For a binary balanced seam union, a selected seam has `d_u=d_v=1`; Sep5 then
forces every authenticated collateral cut to zero.  In that special case the
Boolean activator is indeed forced to equal the seam selector.

## 3. Exact scale-four physical ledger

Let `a_t` be the authenticated scale-four weight of target `t`, let `p` be the
port potential, and let the raw seam slack be

```
s_e = 4 + p(v)-p(u) - sum_{t in H45(e)} a_t >= 0.
```

Here `H45(e)` includes the new WIDTH45 target attached to `e`, whether or not a
separately supplied fractional activator is smaller than `x_e`.  Let `L_t` be
the *physical* load: base service uses `x_e`, whereas a new WIDTH45 occurrence
uses `w_e`.  Define

```
S_raw = sum_e s_e x_e,
A_loss = sum_{new e} a_{t(e)} (x_e-w_e),
S_eff = S_raw + A_loss.
```

### Theorem 3.1 (physical scale-four identity)

Every balanced exact rational seam circulation satisfies

```
4 sum_e x_e = sum_t a_t L_t + S_eff.
```

### Proof

Multiply the definition of `s_e` by `x_e` and sum.  Endpoint balance cancels
`sum_e x_e(p(v)-p(u))`.  This first yields the raw identity.  Replacing a raw
WIDTH45 contribution `a_t x_e` by its physical contribution `a_t w_e` adds
exactly `a_t(x_e-w_e)` to slack.  Summing these corrections proves the stated
identity.  QED.

At `C=sum_e x_e=103`, target coverage gives

```
(sum_t a_t L_t - 408) + S_eff = 4.
```

Both terms are nonnegative.  In an integral point, activation loss is zero and
target loads are integers.  Since the minimum target price is 3, the only
three integral branches are exactly:

1. no repeated target and total seam slack 4;
2. one repeated price-3 target and total seam slack 1;
3. one repeated price-4 target and total seam slack 0.

This proves the branch trichotomy without a solver.

## 4. Exact cycle decomposition

### Lemma 4.1 (rational cycle decomposition)

Every finite nonnegative rational balanced seam circulation decomposes into a
finite nonnegative rational sum of directed simple cycles.  If every port has
mass at most one, the aggregate cycle-column point also has port capacity at
most one.

### Proof

If positive mass remains, start at the tail of any positive seam and follow
positive outgoing seams.  Balance prevents the walk from getting stuck.
Finiteness yields a repeated vertex; the intervening seams form a directed
simple cycle after taking the first repetition.  Subtract the minimum residual
mass on that cycle.  This preserves nonnegativity and balance and zeros at
least one seam.  Iteration terminates after at most the original support size
many subtractions.  The capacity statement is just summation of the recovered
columns at each port.  QED.

The checker below implements this deterministic subtraction over exact Python
`Fraction` values.  JSON floats are rejected.

## 5. Independent point checker

The fail-closed checker is

`scratch/audit_r_k16_width45_c103_cycle_column_point_20260730.py`.

It accepts one of:

* exact rational `arc_masses` and derives its own simple-cycle decomposition;
* exact rational ordered simple-cycle `columns`; or
* binary `selected_seam_ids`, which it decomposes itself.

For a fractional input, all coefficients must be integers, rational strings,
or `{numerator,denominator}` objects; floats are rejected.  The input must
provide all 150 activators, or declare
`occurrence_activator_policy="w_equals_x"`.  In the latter case the checker
instantiates all 150 values itself and still verifies every occurrence row.

The checker independently rebuilds endpoints, source component positions,
base target hits, the 150 endpoint-pair mappings, their split and collateral
indices, raw scale-four slacks, target loads, and both forms of the scale-four
identity.  It checks all 12,870 cyclic Sep5 rows and exact rational endpoint
balance/capacity.  It can enforce claimed branch A, B, or C separately.

The exact branch-B point
`scratch/k16_width45_c103_branchB_exact_fractional_point_20260730.json`
(SHA-256
`2fd6dec37213daa697b90c239cf9183099f13343dfa6f8fe4c054724e70f726b`)
has now passed this independent replay.  The retrieved audit
`scratch/k16_width45_c103_branchB_exact_fractional_point.independent.v2.audit.json`
has SHA-256
`5595eb7c5463f8e7d414db01c66bc651ab14ccc743b7bad3799a3e0764b0b0cc`
and payload hash
`d2133732e64fccc3d31c4d0787d779a52741dcbd1943db4768f3f4876801c526`.
It verifies 82 exact rational simple-cycle columns on 602 positive seams,
seam mass exactly 103, maximum port mass strictly below one, all 12,870 Sep5
rows, all 150 upper plus 450 collateral plus 150 lower activator rows, all 93
target covers, weighted physical service 411, activation loss zero, and
effective slack one.  An independent exact check of its target loads gives
load one on every non-price-3 target and total excess mass one across the
price-3 targets.  The v2 checker also recognizes and enforces the point's raw
`B_PRICE3_EXCESS_SLACK1` branch claim.  Thus it lies on branch B exactly.

## 6. Audit of the existing branch-B presolve model

The two independent branch-B CP-SAT models use, respectively,

* all 1,681 arcs in cyclic SCCs of the slack-at-most-one graph; and
* the equivalent 7,742 tight arcs plus the 43 slack-one arcs admitting a tight
  directed return.

For an **integral** branch-B solution these reductions are complete.  The sole
slack-one selected seam must belong to a selected directed cycle; removing it
leaves a tight return path.  Every selected tight seam lies on a selected cycle
in the slack-at-most-one admitted graph.  Endpoint balance plus outgoing
capacity one also supplies incoming capacity one.  Binary global Sep5 makes
the 150 new activators equal their seam selectors.  Thus the encodings contain
the correct integral branch-B interface.

Both models return presolve `INFEASIBLE` with zero branches.  These are exact
solver outcomes but not independently checkable proof certificates.  They
must therefore be reported as solver-only evidence.

The pruning is not valid for the unrestricted fractional face: an arc with
integer slack greater than the total budget can carry a sufficiently small
fraction.  The full fractional cycle-eligible graph has 211,469 arcs.  No
fractional no-go may be inferred from the integral admitted banks.

The original restricted-bank floating point had 602 positive seams and
numerical residuals around `10^-14`.  It has now been rationalized and passed
the independent exact replay in Section 5.  Therefore the branch-B continuous
face is rigorously nonempty.  In particular, the integer presolve failure is
an integrality phenomenon, not a linear-dual obstruction.

## 7. Restricted binary cycle-column master

The prepared exact driver is

`scratch/solve_r_k16_width45_c103_restricted_cycle_column_master_20260730.py`.

It accepts a supplied ordered simple-cycle catalogue and branch A, B, or C.
It rebuilds every column from the raw binary, safely removes columns that are
too long, exceed the integral branch slack budget, internally violate Sep5,
or already have impossible target multiplicity, and imposes:

* port capacity one;
* all nonempty cyclic Sep5 conflict rows;
* all 93 exact target-multiplicity rows;
* total selected length 103;
* exact branch slack and weighted service.

A SAT witness is exported as raw seam ids and is not accepted until Section
5's checker passes.  Every output is marked `restricted_column_bank=true` and
`negative_status_is_global_certificate=false`.  An UNSAT result excludes only
the supplied catalogue.  A global binary conclusion needs a separately
audited complete enumeration or an exact column-generation separation proof.

## 8. Strategic conclusion

Within the frozen WIDTH45/global-Sep5 service interface, any 73-cut equality
face is decisively gone: the authenticated scale-four theorem gives the
stronger lower bound `C>=103`.  The exact `C=103` face is not closed:

* integral branch C is eliminated by the audited GF(2) locks;
* integral branch B is solver-infeasible in two independently encoded complete
  admitted-arc models, but lacks a solver-independent proof certificate;
* branch A remains open; and
* branch B has the exact rational 82-cycle provider bank certified in Section
  5, but no integral bank.

Thus WIDTH45 strengthens rather than restores the old 73-cut face, while also
exposing a genuine fractional/integral gap at the new floor.  No literal K16
construction follows from the service interface alone.
