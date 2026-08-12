# Theorem AD-H1: joint global q1-primary oracle and fail-closed compiler gate

Date: 2026-08-02

## 1. Result and exact boundary

Fix the normalized K17 `h=1` central factor variables with

```text
M = 383,  D = 255,  B = 511,
218,790 incidence variables y,
875,088 ordinary-pair variables p.
```

There is an executable, model-independent extension which jointly exposes:

1. one licensed linear orientation;
2. one occurrence-labelled primary provider for every rank-ten upper;
3. the ordinary used-root support;
4. a primary forest and its literal `p minus z` residual completion;
5. the two exceptional physical `D` occurrences;
6. the exact downstream residence, all-upper, source, P/U/M Hall--DM, and
   common-cap publication interface.

The extension is fail closed.  Its DIMACS body contains extension clauses
only and has no terminal meaning unless merged with the authenticated exact
`h=1` base CNF.  A complete merged model is accepted only after independent
topology, provider, root, forest, residual-degree, and contracted-rank replay.
Even that acceptance is only a `Q1_ZERO_H1_SCAFFOLD`; it is not a word.

The marker58 all-opening theorem remains a separate frozen interface.  Its
48,620 directed openings cannot be transplanted into `h=1`.  A connected
`h=1` lollipop has exactly two licensed linear Euler chronologies.

## 2. Central factor and the two chronologies

The exact base has 24,310 rank-eight roots and 24,310 rank-nine owners.  It
selects 48,620 incidences.  The missing root `M` has degree one, the duplicate
root `D` has degree three, all other roots have degree two, and every owner
has degree two.  Deleting `M` and `D` leaves 24,308 ordinary diamonds on two
owner paths.  Reinstalling the exceptional seam gives one connected
lollipop.

Let `T` be the selected `D` neighbour on the ordinary component containing
`B`, and let `S_0,S_1` be the other two selected `D` neighbours in increasing
mask order.  Orientation `o` uses

```text
(T,S_o)       as the internal D occurrence,
(B,S_(1-o))   as the closing physical D occurrence.
```

Both are physical provider occurrences.  Only `(T,S_o)` is consecutive in
the opened linear owner chronology; `(B,S_(1-o))` is the cut edge.  Therefore
physical-cycle q1 and opened-literal q1 are distinct predicates and are
reported separately.  Compiler acceptance always uses opened-literal q1.

## 3. Exact primary-provider extension

For every ordinary candidate diamond `e`, introduce `z_e` and enforce

```text
z_e -> p_e.
```

For every one of the 80 possible physical `D` aliases, introduce one mark in
each orientation.  An exceptional mark implies both its exact role alias and
the selected orientation.  There is deliberately no at-most-one constraint
across the two physical occurrences of `D`: the duplicated occurrence may
provide two different upper colours.  Ordinary roots retain distinct-root
support because the base selects exactly one `p` per ordinary root and every
ordinary mark implies that `p`.

For each rank-ten upper `U`, let `Z(U)` be all ordinary provider marks and
`Z_D(o,U)` the exceptional marks licensed in orientation `o`.  The extension
contains one global at-most-one bank and the two opening-guarded rows

```text
not s_o  or  Z(U)  or  Z_D(o,U),      o in {0,1}.
```

Together with exact-one orientation these rows choose exactly one provider
for all 19,448 upper colours in the active orientation.  They are genuine
opening-guarded constraints: failure of one orientation does not exclude the
other.  Sinz chains make every at-most-one bank linear rather than quadratic.

For each ordinary root `q`, `u_q` is linked iff at least one of its 36 marks
is selected.  Neither `M` nor `D` has an ordinary `u` channel.

## 4. Global residual certificate and closed shores

Let `Q0` be the marked physical provider set.  A candidate is acceptable
only if `Q0` is a forest.  Its ordinary marked subset determines the literal
complement `p minus z`.  The independent replay checks, owner by owner,

```text
deg_(p minus z)(T)
  = 2 - 1[T=B] - 1[T is a selected D neighbour]
      - deg_(ordinary Q0)(T),
```

and checks the contracted graphic rank and final two-component ordinary path
cover.  Thus an accepted merged model supplies the complete primal residual
completion.  It does not optimize one deficient shore and then freeze that
local choice.

Equivalently, after a fixed primary support, every owner shore `Y` must obey

```text
2 I_A(Y) + J_A(Y) <= sum_(T in Y) c_T,
```

or, for a linear primary forest,

```text
2 I_A(Y) + J_A(Y) + |boundary_Q0(Y)|
  <= 2 components(Q0[Y]).
```

These are exact Benders separators for a rejected partial master.  They are
redundant after the full literal `p minus z` primal certificate passes.  A
shore row is never promoted from an envelope, a scalar deficit, or a
one-local-shore improvement.

The component-side variables in the CNF only forbid selected ordinary edges
from crossing the proposed two sides.  They do not exclude a detached
monochromatic cycle.  Exact augmented connectivity and the ordinary two-path
forest therefore remain mandatory lazy semantic checks.  A topology failure
must return a factor-semantic connectivity cut; it is never accepted as SAT.

## 5. Joint downstream recourse

For orientation `o`, define `R_o` to mean all of the following on one literal
chronology:

1. opened-literal q1 is zero;
2. every internal positive depth-three run has length at least three;
3. every upper of ranks 10 through 17 occurs as a nonwrapping interval union;
4. the maximal source is exact;
5. the complete strict-lower P/U/M graph is rebuilt;
6. its exact matching and Hall--DM replay pass;
7. the exact common-cap CNF has a verified total SAT model;
8. every selected common-cap provider has literal semantics;
9. the decoded word has the exact depth-three owner derivative;
10. two independently organized exhaustive scans cover all 131,071 nonempty
    K17 masks.

The accepted global semantics is

```text
H_central and (R_0 or R_1).
```

The two orientations are recourse alternatives, not two simultaneously
required compilers.  Literal residence and all upper ranks are evaluated
before source, lower Hall--DM, or common-cap work.  A deficient DM shore may
export the strong row

```text
s_o -> sum_(C outside N(A)) q_(o,A,C) >= |A|-|N(A)|
```

only when every `q` is linked iff the full literal P/U/M candidate predicate.
Otherwise the safe result is the opening-guarded semantic factor cube.

`UNSAT_PROOF` is intentionally nonterminal in the present adapter.  Without
one sealed interface binding the regenerated CNF, assumptions, proof,
checker, and checker result, it becomes `COMMONCAP_UNKNOWN` and supports no
cut.  A word is installed by a no-replace operation only after the total SAT
model, every clause, provider semantics, derivative, and both exhaustive
scans pass.

## 6. Executable dimensions

The global extension contains

```text
base variables                         1,093,878
component/orientation/role/D aliases      24,419
ordinary provider marks                  875,088
orientation-labelled D marks                 160
ordinary used-root channels               24,308
sequential auxiliaries                    855,842
total variables                         2,873,695
extension clauses                       6,112,317
extension literals                     16,537,210
```

The implementation is split deliberately:

```text
scratch/build_ad_k17_h1_joint_global_oracle_20260802.cpp
scratch/verify_ad_k17_h1_joint_global_oracle_20260802.cpp
scratch/audit_ad_k17_h1_q1zero_compiler_adapter_20260802.cpp
scratch/audit_ad_h1_joint_global_oracle_controls_20260802.cpp
```

The builder is model independent.  The verifier accepts either a complete
base assignment or the authenticated signed `y` prefix, in which case it
deterministically reconstructs all `p` channels.  A total extension model,
when supplied, must assign every one of the 2,873,695 merged variables and
pass every extension clause and semantic gate.

## 7. Controls and present K17 frontier

The authenticated K7 positive control has 70 incidences, one augmented
component, two ordinary paths, both licensed D joins, 21/21 q1 coverage, a
21-edge primary forest, and a 12-edge residual complement of contracted rank
12 with two final components.

The frozen deficient K7 selector gives

```text
I=4, J=10, c(Y)=15,
forest endpoint row 25 > 22,
primary Benders row 22 > 19,
residual flow 25/28.
```

All 73 legal same-upper one-support replacements were enumerated.  Forty-nine
improve that incumbent shore, but the best local row is still `20>19` and the
best global flow is `26/28`.  This is a finite control against replacing the
global oracle by optimization of one local shore.

The supplied 26-hole K17 incumbent remains an exact regression input.  It has
26 missing necessary non-D q1 colours, 48 opened-literal holes in each
orientation, 47 cyclic holes in each orientation, and linear profiles

```text
orientation 0: short=5574, upper holes=(48,1534,288,7,0,0,0,0)
orientation 1: short=5574, upper holes=(48,1535,288,7,0,0,0,0).
```

A later independently replayed factor closes the earlier necessary non-D q1
census at `19,412/19,412`.  It does **not** close the literal opening gate:

```text
opened-literal q1 holes: 22 / 22
physical-cycle q1 holes: 21 / 21
short runs:               5586 / 5587
upper holes orientation0: (22,1533,286,7,0,0,0,0)
upper holes orientation1: (22,1534,286,7,0,0,0,0).
```

Consequently the compiler adapter returns `Q1_NOT_ZERO`, emits no common-cap
CNF, and emits no word.  This is the exact integration result, not a search
failure and not a lower bound.

## 8. Conclusion

The all-opening Benders/compiler lane now has a proof-safe `h=1` global
primary extension, independent full semantic replay, exact residual primal
certificate, and fail-closed lower/common-cap publication path.  It is ready
to consume a future factor with zero opened-literal q1 holes.  No current K17
factor reaches literal residence, deeper-upper, source, lower Hall--DM, or
common-cap replay, so no K17 word and no value of `nu(17)` is claimed.
