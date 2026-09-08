# K17 remaining-5054 fail-closed materialization and deep-guard pipeline

Date: 2026-08-02  
Lane: AD  
Status: exact inventory, exact cut-liability prefilter, and fail-closed
post-SAT materialization/audit pipeline proved and implemented.  No q1 SAT
solve was launched, and no q1-SAT chronology is asserted.

## 1. Exact live shell

The authoritative local semantic screen contains 169,426 jointly zero-265
clean Hamming-two banks.  Of these, 164,323 contain an authenticated persistent
q1 core and are rejected.  The conservative rebuild class has 5,103 rows.
Exactly 49 are the dirty-central anchors 13 through 19, seven per anchor; all
49 have separately frozen exact-q1 UNSAT certificates.  Therefore the
remaining clean-anchor shell is exactly

\[
                         5103-49=5054.                 \tag{1.1}
\]

It is selected by the literal predicate

```text
classification == EXACT_BUILD and anchor <= 12
```

in the semantic filter, joined to the complete clean-row table by
`(job,anchor)`.  The per-anchor counts are

```text
0:288  1:380  2:380  3:380  4:380  5:431  6:322
7:354  8:386  9:380  10:380  11:469  12:524.
```

All 5,054 job IDs and complete two-recut bank keys are distinct.  `EXACT_BUILD`
means only that the frozen semantic-core library did not reject the bank.  It
does **not** mean q1 feasible, materialized, connected, resident, upper
complete, or compiler feasible.

The frozen extraction and prefilter output is

```text
scratch/ad_k17_q1_survivor_pipeline_regression_20260802/remaining5054.tsv
```

with 5,054 data rows.

## 2. Exact two-new-cut liability prefilter

Let the round02 internal piece deck be \(I(C_0)\), and let a row replace two
selected cuts by two new cuts \(d_1,d_2\):

\[
 C_1=(C_0\setminus\{c_1,c_2\})\cup\{d_1,d_2\}.       \tag{2.1}
\]

For a cut edge \(d\), let \(X_d\) be the product of the two nested
suffix/prefix accumulated-union rays at that edge.  Each ray has at most nine
states, so \(|X_d|\le81\).  At rank \(9+q\), it has at most \((q+1)^2\)
states.

### Theorem 2.1 (sound prefilter)

\[
 I(C_0)\setminus I(C_1)\subseteq X_{d_1}\cup X_{d_2}. \tag{2.2}
\]

Consequently the total universal bound is 162, and the rank-11 through
rank-17 bounds are

\[
                    18,32,50,72,98,128,162.           \tag{2.3}
\]

#### Proof

Removing \(c_1,c_2\) can only join old pieces, hence cannot destroy an old
internal witness.  Any old-internal witness destroyed by (2.1) crosses
\(d_1\) or \(d_2\).  Cutting there writes the witness as an old suffix followed
by an old prefix, so its union is in the corresponding ray product.  The ray
state bounds give (2.3).  QED

The deterministic replay reconstructs the literal factor cycles and all
20,477 candidate edges, then computes \(X_{d_1}\cup X_{d_2}\) for each of the
5,054 rows.  The exact finite maxima over ranks 11 through 17 are

```text
rank                 11  12  13  14  15  16  17
maximum union size    4   6   7   9  11  11   1
maximum total over ranks 11..17: 48.
```

There are 2,048 distinct new-cut IDs evaluated among these rows.  The observed
48 improves the generic 162 ceiling on this frozen face, but it is still only
a liability superset.  A nonempty row is **not** rejected: selected q1 seams
may redeliver any or all of these masks.  Thus the output field
`general_hard_reject` is zero for every row.  A hard prefilter becomes sound
only after either (i) a target is declared strict-internal-retention, or (ii)
even the complete orientation-expanded seam reachability supergraph has no
witness for it.

## 3. Exact SAT-to-chronology interface

The q1 solver is external to this lane.  For one alleged survivor the pipeline
requires the frozen base factor, frozen candidate catalogue and round02 bank,
the frozen 5,054-row table, a complete selected cut bank, full CNF, full seam
and orientation maps, and solver output.  Before reading the CNF it proves that
the supplied bank differs from round02 at exactly two distinct bases and that
this exact old/new delta occurs in one unique row of the 5,054 table.

### Theorem 3.1 (fail-closed materialization)

Suppose the following checks pass.

1. The solver output contains exactly `s SATISFIABLE`, gives a consistent
   total assignment, and that assignment satisfies every clause of the
   complete supplied DIMACS formula.
2. From the literal factor row order, the decoder reconstructs exactly 3,807
   canonical base paths and all 20,477 candidate cuts.  The complete candidate
   TSV agrees row-for-row with this reconstruction.
3. The selected bank chooses 3,805 distinct extra cuts, at most one in each
   base path.  Splitting gives 7,612 nonempty paths and 7,612 distinct cut
   colours.
4. The decoder regenerates every relaxed occurrence-labelled seam in the
   builder's exact order.  Every supplied seam-map row, endpoint orientation,
   lower mask, upper mask and variable number agrees.
5. Exactly one orientation is selected per path; exactly one selected seam
   leaves and enters every path; and exactly one selected seam uses every cut
   colour.

Then the selected successor relation is a permutation of all 7,612 oriented
paths.  Concatenating its cycles gives a unique literal physical chronology
with all 24,310 rank-nine owners exactly once.  The implementation then
requires all 24,310 adjacencies to be Johnson edges, every rank-eight lower
colour exactly once, every rank-ten upper colour at least once, and every
protected incidence from the frozen factor.  Only after these tests does it
atomically emit

```text
component<TAB>position<TAB>closed<TAB>owner.
```

#### Proof

The exact one-out/one-in constraints make the selected path relation a finite
permutation, hence a disjoint union of directed cycles.  The paths partition
the old owner occurrences because they are obtained by cutting and splitting
the exact factor cycles.  Therefore concatenation contains every owner once.
The remaining conclusions are literal mask-histogram checks, not projections
or inferred Hall statements.  QED

This closes defects in the older diagnostic replay: no positive-integer scrape,
default orientation, open path, partial assignment, stale seam map, or q1-hole
output can be promoted.

## 4. Topology and voltage

For a fully materialized physical chronology, topology is exact without a
quotient: count its directed successor cycles.  Under policy `HAMILTON`, the
pipeline requires exactly one closed component.  Under `FACTOR_OK`, it reports
the exact component-size list but permits more than one.

Voltage is not an extra datum of an arbitrary physical chronology.  The
pipeline first tests whether the complete physical edge set is invariant under
the cyclic coordinate rotation of order 17.

* If not invariant, it reports
  `NOT_APPLICABLE_NON_EQUIVARIANT_PHYSICAL`.  This is not a failure: direct
  physical connectivity is definitive.
* If invariant, all rank-nine owner orbits are free.  The implementation keeps
  parallel edge orbits, reconstructs the quotient degree-two multigraph, and
  sums the phase increments on each quotient component.  For component voltage
  \(v\), its lift has \(\gcd(17,v)\) physical components.  The sum of these
  predicted counts is required to equal the independently materialized
  physical component count.

Thus no numeric voltage is guessed from masks on a non-equivariant object, and
an equivariant voltage certificate is cross-checked against physical topology.

## 5. Full deep-guard vector

The emitted chronology is passed to the previously frozen accumulated-union
evaluator.  The new wrapper reports independently:

1. exact spanning/literal/q1 replay;
2. exact physical topology and, when applicable, quotient voltage;
3. exact cyclic depth-three product residence;
4. the complete final interval-union deck at ranks 11 through 17;
5. the complete active old-edge set \(A=E(G)\setminus E(H)\);
6. exact retained-old witnesses and maskwise inclusion in
   \(\bigcup_{e\in A}X_e\), including the bound \(81|A|\);
7. actual final losses and actual final holes.

Two positive notions are deliberately separated:

* `PASS_RETAINED_GUARDS_WITH_INTRINSIC_HOLES` means no reference-covered mask
  was lost and the requested topology policy passed, but reference holes
  remain;
* `PASS_ALLWIDTH_DEEP_GUARDS` additionally means zero actual holes at every
  rank 11 through 17 and the requested topology policy passes.

An open chronology, missing q1 row, short run, lost old witness, failed
topology policy, malformed file, or partial model never receives the full
PASS.  The pipeline publishes through a temporary directory and emits
`ERROR_FAIL_CLOSED` at the first structural failure.

## 6. Implementation and regressions

The implementation consists of:

```text
scratch/verify_ad_k17_q1_dimacs_model_20260802.cpp
scratch/materialize_ad_k17_q1_model_chronology_20260802.cpp
scratch/audit_ad_k17_q1_survivor_full_guards_20260802.cpp
scratch/run_ad_k17_q1_survivor_full_guard_pipeline_20260802.sh
scratch/build_ad_k17_remaining5054_crossdeck_prefilter_20260802.py
scratch/verify_ad_k17_bank_in_remaining5054_20260802.py
```

Frozen source hashes are, in the same order except with the membership checker
last,

```text
f3d623b4f150fdeb3d73725a99612e67a86931cbbd439c008a44bde77e111c28
7cdd4e0a31df093e211924d74fc5e3331d24bab7b38ea6ff88fec02c413f062c
ba423074976a3adfb6ae9369838f0caacf4625fa6e01045763becacc55e91379
2204867aa416fe9c46cc47df734e7ccd48a6dc31b1ca18438e5399272f51b432
4e82d78323e2b8154aa260a78c36b741c61365f55d889e87f8a9ea0c221a1e2a
e54cb26ec6a97ac13cb3861cd3f5959ce7dd1a7952bf1a3b0529fcb508741e0f
```

The regression directory is

```text
scratch/ad_k17_q1_survivor_pipeline_regression_20260802/
```

Its manifest SHA is
`1176e5bb4d1adec277be5f182ec3dde00dd270a5f1ab06a5a2a0d91da5a50b74`.

Deterministic tests establish:

* a tiny total multiline SAT model passes complete CNF replay;
* a false tiny model fails on its first unsatisfied clause;
* nonnumeric garbage in either a model line or the DIMACS body fails closed;
* the materialized job-14 bank is uniquely recovered as clean anchor 0 with
  key `1:18,540:2842` in the frozen 5,054 rows;
* the authenticated round02 UNSAT output cannot be materialized and produces
  no chronology;
* the frozen factor replays as seven components, 5,783 bad D3 runs and 1,806
  rank-11-through-17 holes, so it is rejected;
* protected C6 row 144 replays as five components, three active old edges,
  5,780 bad runs, zero old-witness losses and 1,803 actual holes, so it is
  rejected;
* both physical factors are non-equivariant and therefore correctly report
  voltage as not applicable rather than inventing a number;
* the target TSV has exactly 21,778 data rows plus its header.

No positive Hamming-two SAT chronology exists in the shared artifacts at the
time of this note.  Therefore the materializer's positive K17 branch is proved
by exact reconstruction checks but awaits its first real SAT survivor as a
positive regression.  The pipeline does not claim q1 feasibility for any of
the 5,054 rows.

## 7. Exact remaining boundary

This work closes the post-SAT ambiguity: any future q1 survivor can be turned
immediately into a hashable physical chronology and either accepted or rejected
by topology, voltage scope, D3 residence, ranks 11--17 and cross-deck guards.

It does not solve any of the 5,054 q1 instances.  Even
`PASS_ALLWIDTH_DEEP_GUARDS` would still leave source-word realization,
terminal lower compiler/common-cap matching, opening convention where needed,
and the final literal contiguous-OR verification as separate gates.
