# Selector-free 4/9/5 chain-minimum model for the frozen RF495 fibre

Date: 2026-07-30  
Lane: AD  
Scope: the complete frozen repeat-free seed5/self `4/9/5` fibre

## 1. Result

The authenticated 4,900-provider exact-one model has an exact formulation
whose only variables are the Boolean coordinates of the three mutable chain
words and their shared interval ORs.  It has no provider selector, witness
selector, target-address variable, output-value variable, ALO, AMO, or Sinz
state.

The full native CP-SAT model has

```text
1,120 Boolean variables;
  920 high-level constraints;
4,900 affine mismatch branches;
76,054 Boolean affine terms in those branches.
```

An independent implementation parsed every emitted proto and reconstructed
every variable and constraint from the frozen maximal-provider table.  The
audit is `PASS`.

## 2. The exact chain/output catalogue

The eighteen mutable word positions split into three consecutive chains:

```text
left4:    mutable ordinals 0..3,   physical positions 0..3;
middle9:  mutable ordinals 4..12,  physical positions 6434..6442;
right5:   mutable ordinals 13..17, physical positions 12868..12872.
```

Their nonempty contiguous intervals number

```text
4*5/2 + 9*10/2 + 5*6/2 = 10 + 45 + 15 = 70.
```

For a chain interval `Q`, let

```text
R_Q = OR_(i in Q) X_i,
```

where the `X_i` are the mutable nonzero 16-bit cells.  A physical interval
shape contributes a fixed halo `F`, so its symbolic output is

```text
O_(Q,F)(X) = F OR R_Q.
```

These are symbolic output functions, not constant masks.  The raw global
shape map contains 395 `(Q,F)` pairs.  Of these, 227 occur in residual-witness
rows.  Taking the unique greatest `F` in every same-`(target,Q)` fibre leaves
exactly 192 output types:

```text
left4    30;
middle9 127;
right5   35.
```

Thus exactly 35 residual-compatible types are removed by same-`Q` dominance;
the other 168 raw global shapes are inactive for the seventy residual
targets.  It would be incorrect to call all 203 nonmaximal-catalogue shapes
dominance removals.

For every residual target `T` and each of the seventy intervals `Q`, the
audited table supplies one greatest physical fixed halo `F(T,Q)`.  There are
4,900 such rows, but only the 192 distinct symbolic functions above.

## 3. Shared interval state

Singleton interval bits alias the corresponding cell bits.  For every
nonsingleton interval `[a,b]` inside one chain and every bit `k`, introduce
`R[a,b,k]` and impose

```text
R[a,b,k] = max(R[a,b-1,k], X[b,k]).
```

On Boolean variables this is exactly OR.  The number of nonsingleton
intervals is

```text
(10-4) + (45-9) + (15-5) = 6 + 36 + 10 = 52.
```

Hence the state ledger is

```text
18*16 = 288 cell bits;
52*16 = 832 nonsingleton interval-OR bits;
total  = 1,120 Boolean variables.
```

Every cell has one 16-literal nonzero constraint.  There are 832 exact
interval recurrences.

## 4. Direct target-coverage constraint

The greatest halo always satisfies `F(T,Q) subseteq T`.  Define the
nonnegative mismatch

```text
M(T,Q)
  = sum_(k notin T) R[Q,k]
    + sum_(k in T minus F(T,Q)) (1-R[Q,k]).
```

### Lemma 4.1

For every residual `T` and chain interval `Q`,

```text
M(T,Q)=0  iff  F(T,Q) OR R_Q = T.
```

#### Proof

Every summand is zero or one.  The first sum vanishes exactly when `R_Q` has
no bit outside `T`.  The second vanishes exactly when `R_Q` contains every
bit of `T` not already supplied by `F(T,Q)`.  Bits of `F(T,Q)` already lie in
`T`.  These conditions are precisely equality of the symbolic physical
output with `T`.  QED.

Consequently target coverage is the single native constraint

```text
min_Q M(T,Q) = 0.
```

There is one such `MinEquality` for each of the seventy residual targets.
The full constraint ledger is therefore

```text
18  nonzero BoolOr constraints;
832 exact interval LinMax constraints;
70  target MinEquality constraints;
---
920 high-level constraints.
```

Across the seventy minima there are exactly 4,900 affine branches and 76,054
nonconstant Boolean terms.  OR-Tools 9.15 serializes each minimum as a
`LinMax` over the negated mismatches; the independent proto audit verified
all coefficients and offsets exactly.

## 5. Equisatisfiability theorem

### Theorem 5.1

The selector-free chain-minimum model and the authenticated 4,900-provider
exact-one CNF have the same projection onto the 288 mutable cell bits.
Therefore either is satisfiable exactly when the frozen seed5/self RF495
fibre contains a literal universal word of length 12,873, importing the
already authenticated exact-one/host-completeness theorem for the final
universal-word equivalence.

#### Proof

Suppose first that the chain model is satisfied.  For every residual target
`T`, choose a `Q` with `M(T,Q)=0`.  By Lemma 4.1 the authenticated greatest
physical row `(T,Q,F(T,Q))` has literal OR exactly `T`.  Select its exact-one
provider variable and set the corresponding Sinz prefix state.  This can be
done independently for all seventy targets: set the complete 69-bit Sinz
prefix vector to zero before the chosen selector and one from it onward.
Thus every clause of the 4,900-row model is satisfied.

Conversely, take a satisfying exact-one assignment.  Its selected row for
`T` has some `(Q,F(T,Q))`.  The provider implications say exactly that no
outside bit occurs in `R_Q` and every bit in `T minus F(T,Q)` occurs.  Thus
`M(T,Q)=0`, and the target minimum is zero.

Finally, the existing unique-greatest same-`(T,Q)` theorem maps any literal
raw witness `(T,Q,F)` to `F(T,Q)`: from

```text
F OR R_Q = T,
F subseteq F(T,Q) subseteq T,
```

it follows that `F(T,Q) OR R_Q=T`.  Hence neither maximalization nor selector
elimination loses a literal completion.  QED.

## 6. Exact lead-pinned faces and queue

For the authenticated incumbent cells, the sixty-seven currently covered
residual targets have a unique **serving chain** and split as follows:

```text
left4:    14;
middle9:  37;
right5:   16;
holes:    {0x18e7,0x3de7,0x9e20}.
```

This is not a unique-host claim: the sixty-seven targets have seventy-five
incumbent interval hosts in total.

When chains outside an active face are pinned to the incumbent, a target is
deleted from the face model exactly when a pinned output already equals it.
All remaining pinned branches are positive and may be removed.  After
substituting every inactive-chain cell by its authenticated incumbent value,
this gives the following standalone protos with exactly the same projection
on the active-chain cells:

| Queue | Active face | Required targets | Active Q | Bool vars | Constraints | Mismatch branches | Affine terms |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | left4 | 17 | 10 | 160 | 117 | 170 | 2,500 |
| 2 | right5 | 19 | 15 | 240 | 184 | 285 | 4,275 |
| 3 | middle9 | 40 | 45 | 720 | 625 | 1,800 | 27,707 |
| 4 | left4 + right5 | 33 | 25 | 400 | 298 | 825 | 12,695 |
| 5 | left4 + middle9 | 54 | 55 | 880 | 739 | 2,970 | 45,669 |
| 6 | middle9 + right5 | 56 | 60 | 960 | 806 | 3,360 | 52,172 |
| 7 | full | 70 | 70 | 1,120 | 920 | 4,900 | 76,054 |

The frozen queue order is exactly the requested one: left, right, middle,
then the two-chain faces in increasing active-cell count `LR, LM, MR`.  The
full model is last in the reusable queue because it is logically equivalent
to the already-live exact-one solve.  No **proper incumbent-pinned face**
solve has been launched.  The separately
authorized full-model run is recorded in Section 8.

An UNSAT proper-face result excludes only that incumbent-pinned face.  It is
not an UNSAT result for the complete RF495 fibre.  A full-model `INFEASIBLE`
response would instead be a complete frozen-fibre CP-SAT solver result, but
without an independently replayable proof certificate.

## 7. Independent implementation audit

The independent auditor does not import the builder and never creates a
solver.  It:

1. pins the exact-one CNF, exact-one map, exact-one independent audit,
   maximal incidence, host audit and incumbent cells;
2. checks all 4,900 maximal TSV rows against the exact-one selector map;
3. reconstructs the seventy contiguous `Q` masks and all 192 symbolic output
   types;
4. verifies `F(T,Q) subseteq T` for every row;
5. reconstructs the exact lead-pinned target reduction for every face;
6. parses all seven binary protos;
7. checks every Boolean variable name and domain;
8. reconstructs every nonzero row and interval recurrence;
9. reconstructs every coefficient and offset in every target minimum;
10. verifies the 4,900-branch/76,054-term full ledger; and
11. AST-checks that the builder contains no solver invocation.

It reports `PASS` with payload

```text
a8fca7fb225c45d7c84c5bf60b4fd642cf0a5e8c3a3b7c2a5f7956175110d548.
```

The full proto has SHA-256

```text
59f46dcac67d8178590ab28ab72e2fd56d2e08b05ba0fa07be1e7767125fdd71.
```

## 8. Execution and proof scope

After the model audit, one full-model CP-SAT run was authorized as materially
different from the live provider-selector solve.  Its fixed policy is:

```text
one CP-SAT worker;
nice level 15;
one pinned CPU;
hard address-space cap 2 GiB;
solver time limit 600 seconds;
no concurrent face portfolio.
```

The frozen immediately-prelaunch memory audit reported 230,169 MiB available
and the preceding filesystem audit reported 426 GiB free on
the `/home` filesystem.  The affinity audit also showed a material caveat:
all sixty-four logical CPUs had zero sampled idle time.  Core 46 was therefore
not free when selected.  The run is an oversubscribed nice-15 job, not a
dedicated-core measurement.  This affects resource provenance and the useful
search time obtainable within 600 wall seconds, but not the model scope or
the recorded solver status.

The solver round-trips the binary proto and requires the same SHA before
search.  On SAT it decodes the first 288 bits into the eighteen cells,
materializes the exact 12,873-word layout, runs an endpoint-frontier literal
replay, and then invokes a separate start-by-start verifier.  Only two
65,535-of-65,535 passes promote SAT.

Native CP-SAT does not emit a DRAT/LRAT certificate for this model.  Therefore
an `INFEASIBLE` response is recorded as a scoped solver result, not as an
independently replayable impossibility proof.  `UNKNOWN`, timeout, memory
failure, or missing output remains `UNKNOWN`.

### Prepared complete-hint fallback

A second, non-launched proto adds a complete state hint from the authenticated
three-hole incumbent.  All 288 cell bits are copied from `lead_score3.cells`,
and all 832 interval-OR hints are recomputed literally.  Its exact audit is:

```text
1,120 of 1,120 variables hinted;
hint values: 579 zero, 541 one;
18/18 nonzero constraints satisfied;
832/832 interval recurrences satisfied;
67/70 target minima satisfied;
violated targets exactly {0x18e7,0x3de7,0x9e20}.
```

Clearing only `solution_hint` recovers the unhinted proto byte-for-byte.  The
hinted proto SHA-256 is

```text
a7523f48e53bb6e056899d479bf4037218733c4e4c0300737c2a4c37e1bab4e7.
```

The fallback wrapper refuses to run before the present unhinted status file
exists, refuses a duplicate solver, and also refuses to run without a fresh
post-run `AUTHORIZED_CPU` supplied explicitly.  It has not been launched.

### Harvested unhinted disposition

The unhinted run terminated normally at the internal limit:

```text
solver status:                  UNKNOWN;
acceptance:                     UNKNOWN_OR_RESOURCE_LIMIT;
solver wall time:               600.003602089 seconds;
conflicts:                      738,575;
branches:                       1,994,038;
Boolean propagations:           99,091,661;
integer propagations:           110,810,696;
restarts:                       2,314;
deterministic time:             59.9981;
peak RSS:                       130,700 KiB;
swaps:                          0;
process exit:                   0.
```

The job received 97% CPU despite the oversubscribed launch.  The loaded model
round-tripped byte-identically to the frozen proto.  There is no candidate
word, no literal replay event, no UNSAT certificate and no theorem-status
change.  A separate harvested-run auditor reports `PASS_SCOPED_UNKNOWN`,
payload

```text
4770373bc19c5b8fb2e5fe3758b9b6b32cde6fd8041ba629f8b04ff046290a6e.
```

The exact result hashes are

```text
full.solve.result.json
  8f78ad06691b446f88d99fc81fffd66cca3ab29f1500c12c3bdc37853cf34dec
full.solve.stdout.log
  4a13fa17b2d1c2a5fa3712c6338c69c3788233e749a43de616bb6e951e4dbfc1
full.solve.resource.log
  73c9aadde569e5822cd59594b931f2f3c7c998561bd06974ba89ebbe72c6faee
full.solve.roundtrip.pb
  59f46dcac67d8178590ab28ab72e2fd56d2e08b05ba0fa07be1e7767125fdd71
full.solve.status
  b7245c215954feb8893055c554e811220da6de93c092f8f9908d4a458e7b5019
```

The complete hinted fallback remains `PREPARED_NOT_LAUNCHED`.

## 9. Frozen model and runtime artifacts

```text
scratch/build_k16_rf495_chain_output_cpsat_20260730.py
scratch/audit_k16_rf495_chain_output_cpsat_20260730.py
scratch/solve_k16_rf495_chain_output_full_20260730.py
scratch/verify_k16_rf495_chain_output_candidate_20260730.py
scratch/run_k16_rf495_chain_output_full_h100_20260730.sh
scratch/audit_k16_rf495_chain_output_full_run_20260730.py
scratch/build_audit_k16_rf495_chain_output_full_lead_hint_20260730.py
scratch/solve_k16_rf495_chain_output_full_lead_hint_20260730.py
scratch/run_k16_rf495_chain_output_full_lead_hint_h100_20260730.sh
scratch/k16_rf495_chain_output_cpsat_20260730/
  MANIFEST.json
  RUNTIME_MANIFEST.json
  chain_output.catalogue.json
  chain_output.blueprint.json
  face_queue.json
  chain_output.independent.audit.json
  chain_output.{left4,right5,middle9,left4_right5,
                left4_middle9,middle9_right5,full}.pb
  chain_output.{face}.stats.json
  chain_output.full.lead_hint.pb
  chain_output.full.lead_hint.stats.json
  chain_output.full.lead_hint.independent.audit.json
  full.solve.result.json
  full.solve.stdout.log
  full.solve.resource.log
  full.solve.roundtrip.pb
  full.solve.status
  full.solve.exit
  full.prelaunch.memory
  full.prelaunch.mpstat
  full.solve.independent.audit.json
```

The package manifest payload is

```text
5be3d942eec02c0799ca86a4c678903bf10a5669eba06c31cdefb36f8ad49a5e.
```

That manifest freezes the model catalogue, protos, face queue and independent
model audit.  Runtime scripts are pinned separately in the remote
`full.prelaunch.sha256` ledger.  The harvested runtime manifest has payload

```text
05c217a84c85ba2c4557329c62c9c27e9cc5c7df91b79105555f0ff9d56044f6.
```
