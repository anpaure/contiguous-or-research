# Thread D: disjoint K16 subgroup portfolio

Date: 2026-07-30

## Result

The period-three subgroup rows admit an exact **disjoint** 63-case split.  The
executable sequential driver is

```text
scratch/threadD_k16_q23_disjoint_portfolio_20260730.py
```

and the exact joint-history solver now accepts

```text
--preinstall-q23-disjoint-branch PATTERN_A<node>
```

in `scratch/solve_even_two_rail_joint_history_kissat_20260730.py`.

This is a global source-independent restriction.  It contains no source
carrier, edit radius, hint, prescribed seam, or source-relative transition.

## Canonical-witness partition theorem

Let `A_m` mean that the selected carrier contains a q2 provider of the
singular target 37449 whose middle A-node is `m`.  The frozen geometry audit
proves that the possible `m` are exactly

```text
380,384,395,406,378,381,383,396,405.
```

The order puts the four 80-provider nodes before the five 120-provider nodes.
Let `C_m` mean that the selected carrier contains an `AAAB` provider of the
singular q3 target 4681 whose first A-middle is `m`.  Its first two edges are
the corresponding q2 provider, so `C_m` implies `A_m`.  Finally, for each
non-AAAB one-block shore pattern let `P_p` mean that a provider with pattern
`p` occurs, ordered as

```text
ABBB, BBAA, AABB, BAAA, BBBA, BBBB.
```

Every carrier satisfying the two singular rows has some `A_m`.  Its q3
provider either gives some `C_m`, or gives one of the six `P_p`.  Assign it as
follows:

1. If any `C_m` occurs, use the first such `m`.
2. Otherwise use the first occurring `P_p` and independently the first
   occurring `A_m`.

This assigns exactly one of nine AAAB cases or one of `6*9=54` remaining
cases.  Existence proves exhaustivity.  The first-witness rule proves pairwise
disjointness.

The earlier 9-by-7 positive restrictions were exhaustive but could overlap
when a carrier contained several providers.  They must not be described as a
disjoint proof partition.  The new flag adds the missing negative clauses.

## Exact CNF realization

For a provider path `e_1,...,e_q`, occurrence is the conjunction of its
selected option literals.  Its nonoccurrence is therefore the single exact
clause

```text
not x[e_1] or ... or not x[e_q].
```

An AAAB branch fixes its positive `C_m` row and adds one such clause for every
earlier `C`.  A non-AAAB branch fixes positive rows `P_p` and `A_m`, forbids
every AAAB path, every earlier non-AAAB pattern path, and every earlier q2
middle path.  Thus the implementation is exactly the canonical rule above;
there is no relaxation or chosen-witness ambiguity.  The existing factored
positive DNF remains exact.

The frozen inputs are:

```text
k16_subgroup_shadow_geometry_20260730.audit.json
  d4887f9bdd15a479c965448ad208d250d87279be9891d30c6cdf92b2c5ac1f4a
k16_joint_q23_preinstall_size_20260730.audit.json
  7b585784ac2cde11d8dc40f1c67041b0ae14ccb123e49fa93a5c81fdd3a4c024
k16_subgroup_cluster_portfolio_20260730.audit.json
  d763a3dcb059a6f573aae6e55b568c703a5ac92dabb58079d8671b5cc427f71d
```

## Sequential and promotion semantics

The driver:

- refuses `run` off H100;
- requires an explicit unbranched-pilot artifact whose status contains
  `UNKNOWN` or `UNSAT`;
- uses a lock and a `pgrep -af` conflict census before every branch, including
  old `--preinstall-q2-subgroup-middle-node` jobs;
- launches one branch process at a time under address-space, CPU, wall, round,
  and per-round caps;
- always passes `--deep-cegar`;
- sends a deep PASS directly to the fail-closed all-cut bridge
  `scratch/threadD_k16_joint_history_comp3_bridge_20260730.py`;
- lets that bridge independently rematerialize the quotient and physical
  carrier, construct the exact arbitrary-upper cut-survival atlas, and account
  for every surviving cut edge in both orientations;
- runs one-worker COMP3 under a separate finite `RLIMIT_AS`, CPU, wall,
  per-state, total-time, state-count, and CEGAR-batch cap;
- accepts a decoded K16 word only after the bridge's independent D3 and literal
  65,535-mask replay, including the required source letter `{z}=32768`.

An atlas-level cut rejection is exact: every cyclic interval witness of at
least one upper target crosses that edge.  Lower q2/q3 fixed-window losses are
diagnostic and remain available to the integrated compiler/boundary model.
If a state is UNKNOWN, or the state/time budget leaves any surviving state
untested, promotion remains explicit UNKNOWN; it is not an all-cut rejection.

Kissat is invoked without proof logging.  Consequently `UNSAT_NO_PROOF` is
kept as diagnostic data and counts as zero proved branches.  Even 63 such
statuses leave the portfolio result `UNKNOWN_BRANCH_PORTFOLIO`.

## Lightweight regression

```text
python3 scratch/test_threadD_k16_q23_disjoint_portfolio_20260730.py -v
```

The ten tests verify the frozen Cartesian atlas, canonical disjoint
classification, absence of source-relative command flags, fail-closed pilot
gating, direct all-cut K8/K10 replay, and the one-call promotion contract into
the all-cut bridge.  They also verify the three exact any-unit middle orbits,
the production successor ledgers for all three orbit representatives, and
replay all four strengthened collar summaries.  The bridge's separate
four-test suite checks its exact
cut theorem against all 504 oriented K10 linearizations and independently
replays the retained 1,023-mask word.
The construction/regression audit itself launched no H100 job.  Runtime
execution and its per-branch proof status are recorded separately in
`THREAD_D_K16_Q23_AAAB_FIRST_PORTFOLIO_RESULT_20260730.md`.

## Any-unit quotient and common collar cut

`THREAD_D_K16_ANY_UNIT_VOLTAGE_SUBGROUP_ORBIT_AUDIT_20260730.md` gives the
exact symmetry reduction of the nine middles to three multiplier orbits.  It
reduces the 63 existential formulas to 21 orbit formulas only when quotient
voltage is allowed in all of \(U(15)\), or when the exact stabilizer-residue
representatives are retained.  It is not a deletion of cases from the old
fixed-voltage-one slice.  The executable enforces this scope through
`--preinstall-q23-orbit-branch` and the voltage flags.

For the four 80-prefix AAAB formulas, the exact next-collar audit is
`THREAD_D_K16_AAAB_COLLAR_COLOUR_ORDER_FLOW_20260730.md`.  It installs 22,400
compact one-step colour/order/history implications per formula and proves
their option-level multiplier covariance.  All 89,600 collars nevertheless
pass marginal Hall, and the endpoint-coupled flow for the full set of 427
uncovered colours has value 428.  Proper colour subsets were not exhausted.
Thus this is a common propagation cut and a sharp localization of the next
gate, not a branch UNSAT result.
