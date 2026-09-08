# K16 r98 assumption-core boundary, unique-provider collision cut, and r99 portal reduction

Date: 2026-07-29  
Lane: L  
Status: proved solver-free cut and portal theorems; assumption-core extraction remains uncertified

## 1. Exact verdict

The requested assumption-literal model has been made proof-safe at the
model-construction level, but no CP-SAT assumption core was certified before
the two long H100 jobs were terminated.  In particular, there is currently
neither a solver-returned sufficient assumption core nor a deletion-minimal
assumption core artifact.

Two weaker trusted-solver diagnostics do exist on the same frozen model:

1. fixing all 403 source-singleton active q1 guards hard makes the model
   infeasible;
2. a CEGAR pass found a hard infeasible 360-row subset, consisting of all 197
   singleton lower rows and 163 of the 206 singleton upper rows.

The second set is a useful candidate core, but it was not replayed through the
assumption interface, was not minimized conclusively, and has no independently
checked proof log.  It must not be called a certified minimal core.

The main new results are solver-free.

- Every exact internal radius-98 motif cut loses at least 114 source-unique q1
  colours.  Any 98-seam completion would therefore need at least 16 seams that
  simultaneously repair a distinct lost lower colour and a distinct lost
  upper colour.
- In the radius-99 retain-22511 branch the corresponding uniform lower bound is
  14 double repairs; in the delete-22511 branch it is 12.
- This collision count does **not** close the internal radius-98 face.  An
  explicit exact-fibre cut supports 63 distinct double-repair seams in the
  relaxed endpoint-capacity matching problem.  Thus the missing obstruction is
  not the scalar double-repair count; a stronger coloured-b-factor/odd-set or
  higher-order endpoint obstruction would be needed.
- The locked upper colour `(1,1907)` gives a different, exact portal theorem.
  It removes the entire delete-22511 radius-99 grade-two/no-exterior class and
  reduces the remaining delete branch to 14 one-exterior portals or 6,447
  two-exterior pairs.  Exactly

  ```text
  183051365705061937087534858694049983889408
  ```

  motif-hitting cut banks survive, about 3.4672% of the unfiltered delete
  branch.

No global radius-99 no-go, no resident factor, and no Hamilton carrier is
claimed.

## 2. Frozen objects and notation

Let `F` be the selected 858-edge quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`.  The byte
hash is

```text
d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

Its current positive-residence hypergraph has 147 motifs and 390 distinct
source edges.  Write `E` for this 390-edge motif union and

```text
X = F minus E,    |X| = 468.
```

The exact overlap decomposition has 85 independent local components.  The
audited option certificate has hash

```text
0df79758045e816e2c4545cd10f99b908309d63dc3e96a43715b370e446eb66e
```

and the exact radius-99 graded cutspace certificate has hash

```text
b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e.
```

The catalogue digest is

```text
e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3.
```

Every catalogue edge `e` has one lower q1 colour `lambda(e)` and one upper q1
colour `upsilon(e)`.  A colour is *source-unique* when it has exactly one
provider in `F`.  There are 675 source-unique lower colours and 673
source-unique upper colours.  Define

```text
w(e) = 1[lambda(e) is source-unique and e is its provider]
     + 1[upsilon(e) is source-unique and e is its provider].
```

The exact source-edge histogram is

```text
w=0: 32 edges,    w=1: 304 edges,    w=2: 522 edges.
```

For a source cut `D`, put

```text
ell(D) = sum_{e in D} w(e).
```

Because one edge has exactly one lower and one upper colour, `ell(D)` is
exactly the number of source-unique lower and upper colours whose unique
source provider is removed by `D`.

The 433 nonautomatic guarded rows in the compressed internal model are a
different census: 215 lower and 218 upper.  Their source-provider
multiplicities are

```text
lower: 197 singleton, 18 double;
upper: 206 singleton, 12 double.
```

The global source-unique census is used in the loss theorem; the 433-row
census is used in the assumption-core model.  They must not be conflated.

## 3. Exact guarded model and core status

### Theorem 3.1 (guarded-model equivalence)

On the internal radius-98 branch retaining edge 22511, the frozen guarded
model is equivalent to the following problem.

1. Choose exactly one of the certified local options in each of the 85
   overlap components.  There are 262 option variables in total, involving
   267 possible source cut edges, and every complete choice cuts exactly 98
   edges.
2. Add exactly 98 loopless off-source seams whose endpoints lie in the 466
   exposed motif nodes.  There are 7,761 such seams.
3. At every exposed node, equate deleted and added incidence.
4. Enforce any named subset of the 433 active q1 rows by setting its positive
   guard literals to one.

The exported model has exactly 8,457 variables, 1,525 constraints, and 433
positive assumption references.  It contains no top-residence, connectivity,
voltage, or Hamiltonicity constraint, and it excludes the global branch that
deletes 22511 and uses an exterior cut.

#### Proof

Each component option is an exact minimum local transversal of its motif
component, the component supports are disjoint, and their ranks sum to 98.
Thus choosing one option in every component is exactly the certified internal
radius-98 cut fibre.  The source is degree two, so equality of deleted and
added incidence at every vertex is equivalent to degree two after the
exchange.  A q1 row is automatic precisely when it has a fixed source
provider; every provider admitted by the internal 7,761-seam atlas is
represented by a retained cut-variable source edge or an addition variable.
Guarding the resulting provider sum by a positive literal therefore enforces
exactly that row within this atlas.  The byte-frozen proto has the stated
census.  No other predicate occurs in the proto.  ∎

### Proposition 3.2 (what is and is not certified)

The following statuses are exact.

| row family | status | logical force |
|---|---:|---|
| all 433 positive assumptions, 180-second run | `UNKNOWN` | no core |
| all 433 positive assumptions, long run | terminated before verdict | no core |
| 403 singleton-source rows fixed hard | `INFEASIBLE` | trusted CP no-go for this row set |
| 360-row CEGAR hard subset | `HARD_SUBSET_INFEASIBLE` | candidate sufficient row set, not assumption-replayed or minimal |

The 403-row hard run took 42.249106046 solver seconds, 1,278,159 branches and
116,512 conflicts.  The 360-row candidate consists of 197 lower and 163 upper
rows.  Its minimization field is explicitly false and its final assumption
replay field is null.

Consequently the phrase *minimal r98 assumption core* is presently
unsupported.  Under trusted CP semantics the 360 named hard rows are a
sufficient infeasible subsystem of the guard-fixed formulation, but no
proof-logged or deletion-minimal certificate has been obtained.

### Model-hardening changes

`scratch/extract_k16_r98_joint_q1_unsat_core_20260729.py` now:

- pins the source, option-certificate and catalogue hashes;
- verifies the embedded certificate digest and all option/census invariants;
- exports and hashes the actual model bytes;
- records driver, catalogue-module and command provenance;
- uses positive assumptions only;
- accepts a solver core only after an infeasible replay;
- treats every shrink `UNKNOWN` as inconclusive; and
- declares subset-minimality only after every retained row-minus-one problem
  is proved feasible and the final core itself is replayed infeasible.

The separate raw-face script
`scratch/threadD_k16_r98_q1_assumption_core_20260729.py` is not an
assumption-core artifact for this theorem because it addresses a different
390-cut/649-row face and includes dynamic top rows, whereas Theorem 3.1 concerns
the compressed 262-option/433-row top-free face.  Its current implementation
does create the 7,761 addition variables once, clears the negative hard-base
assumptions before installing positive row assumptions, and rejects unknown or
negative returned literals.  Those repairs do not identify its scope with the
compressed model.

## 4. Solver-free minimum unique-loss theorem

For branch `B`, component `i`, and allowed excess grade `j`, let
`O_ij(B)` be its exact finite local option bank and put

```text
m_ij(B) = min_{D in O_ij(B)} sum_{e in D} w(e).
```

### Theorem 4.1 (min-plus factorization)

Fix one of the three audited faces: internal r98, radius-99 retain-22511, or
radius-99 delete-22511.  If the branch has excess budget `b`, then the minimum
source-unique q1 loss is

```text
min  [ sum_i m_{i,j_i}(B) + min_{Y subset X, |Y|=b-sum_i j_i} sum_{e in Y}w(e) ],
```

where the first minimum is over all nonnegative allowed grades with
`sum_i j_i <= b`.

#### Proof

The 85 motif-overlap components have disjoint source-edge supports.  The
graded cutspace theorem says that every motif-hitting cut in a fixed branch
is uniquely the union of one local graded option from each component and the
required number of exterior edges from `X`.  Conversely every such union is
a branch-valid motif-hitting cut.  Since `ell` is additive on disjoint edge
sets, minimizing it separates into the displayed min-plus convolution.  The
local universes have at most twenty edges and the exterior budget is at most
two, so the permanent audit enumerates every local option and every needed
exterior choice exactly, without a solver.  ∎

### Corollary 4.2 (exact values)

The exact terminal ledgers are:

| face | local excess | exterior cuts | minimum `ell(D)` | number attaining that case minimum |
|---|---:|---:|---:|---:|
| r98 retain 22511 | 0 | 0 | 114 | 219122084616339456 |
| r99 retain 22511 | 0 | 1 | 114 | 4382441692326789120 |
| r99 retain 22511 | 1 | 0 | 113 | 438244169232678912 |
| r99 delete 22511 | 0 | 2 | 112 | 20816598038552248320 |
| r99 delete 22511 | 1 | 1 | 111 | 4382441692326789120 |
| r99 delete 22511 | 2 | 0 | 111 | 1095610423081697280 |

Thus the uniform minima are respectively 114, 113 and 111.

## 5. The double-repair Hall cut

### Lemma 5.1 (two-palette collision demand)

Let a radius-`r` cut destroy `l` source-unique lower colours and `u`
source-unique upper colours.  Every q1-complete `r`-seam repair contains at
least

```text
l + u - r
```

seams that simultaneously provide a destroyed lower colour and a destroyed
upper colour.  These seams contain a matching of that size between distinct
lost lower and distinct lost upper colours.

#### Proof

For every lost lower colour choose one selected replacement seam that provides
it, and do the same for every lost upper colour.  Within either palette these
chosen seam sets are injective because one seam has only one colour in that
palette.  They are two subsets of the same `r` selected seams, of sizes `l`
and `u`.  Their intersection therefore has size at least `l+u-r`.  Every seam
in the intersection represents one distinct lower and one distinct upper
colour, so the intersecting seams form the claimed colour-pair matching.  ∎

For a fixed cut `D`, define its *endpoint-capacitated colour-pair packing*
`nu_pair(D)` as the largest set `Z` of allowed off-source seams such that:

1. every seam in `Z` provides one lower and one upper colour uniquely lost by
   `D`;
2. no two seams in `Z` use the same lost lower colour or the same lost upper
   colour; and
3. at every quotient node `v`, the number of incidences from `Z` is at most
   `deg_D(v)`.

Every degree-balanced q1-complete repair induces such a packing.  Lemma 5.1
therefore gives the exact checkable necessary inequality

```text
nu_pair(D) >= ell(D)-r.                                      (5.1)
```

This is the promised colour-pair/endpoint Hall cut.  Failure of (5.1) for one
cut excludes that cut; failure for every cut in a fibre excludes the fibre.
Satisfaction of (5.1) is only a relaxation because it does not assign the
remaining seams or enforce all degree and q1 equations simultaneously.

### Corollary 5.2 (frozen demands)

Combining Lemma 5.1 with Corollary 4.2 gives:

```text
internal r98:               at least 114 - 98 = 16 double repairs;
r99 retain, uniformly:      at least 113 - 99 = 14 double repairs;
r99 delete, uniformly:      at least 111 - 99 = 12 double repairs.
```

The r99 subcases retain sharper values: the retain grade-zero plus one-exterior
class needs at least 15, and the delete grade-zero plus two-exterior class
needs at least 13.

### Proposition 5.3 (this cut does not close r98)

The r98 double-repair endpoint relaxation has an explicit feasible witness
with:

```text
98 exact-fibre source cuts,
157 source-unique colour losses,
63 distinct lower/upper double-repair seams,
63 distinct lost lower colours,
63 distinct lost upper colours,
and seam incidence no larger than cut incidence at every endpoint.
```

The solver-free verifier checks all 147 motifs, all 85 selected local options,
both colour matchings, and every endpoint capacity.  It intentionally does
not impose full addition-degree equality or the remaining q1 rows.

For this displayed cut, (5.1) asks for `157-98=59` seams and the witness gives
63.  Hence even the cut-specific demand is met in the relaxation, while the
uniform demand 16 is much smaller still.  This particular Hall layer cannot
prove r98 infeasible.  A separate floating GLOP diagnostic reports a feasible
8,024-variable, 1,597-row relaxation with 533 fractional variables, but it
stores neither the primal vector nor a payload digest, and its proto was not
constraint-diffed against the 1,525-row guarded model.  It therefore suggests,
but does not certify, ordinary LP feasibility.  No rigorous scalar/Farkas cut
has been found.  A complete human-readable no-go may require an integral
coloured-b-matching odd-set inequality, or an equivalent higher-order
endpoint/monodromy certificate stable under all 7,761 seams.

## 6. Exact radius-99 graded candidate theorem

Let `e_* = 22511`.

### Theorem 6.1 (retain branch)

Every radius-99 motif-hitting cut retaining `e_*` satisfies

```text
sum_i j_i + |D intersect X| = 1.
```

Consequently it is exactly one of:

1. one grade-zero option from every component, together with one of the 468
   exterior source cuts; or
2. no exterior cut, one grade-one local state in one component, and
   grade-zero states elsewhere.

The 85 grade-zero banks contain 262 local entries in total, and the grade-one
banks contain 958 local entries.  Of the latter, 304 states in 33 components
contain no grade-zero option as a subset.  Therefore the stale normal form
“minimum option plus one extra edge” is incomplete.  The exact number of
distinct motif-hitting cut sets in this branch is

```text
26314269608821534759782407397730255110144.
```

No assumption-core provider halo is presently known to reduce this branch.
A q1-neutral exterior cut can create endpoint capacity and permit a different
integral routing without itself providing a core colour.  A filter based only
on which extra edges provide a core row is therefore unsound unless backed by
a stable integral odd-set certificate.

### Theorem 6.2 (delete branch before q1)

Every radius-99 motif-hitting cut deleting `e_*` satisfies

```text
sum_i j_i + |D intersect X| = 2.
```

Its exact local state totals at excess zero, one and two are 261, 960 and
3,442.  Before imposing q1, the branch contains

```text
5279389441842968292775849118951024130785280
```

distinct motif-hitting cut sets.

Both theorems are immediate from the audited graded cutspace identity: the
ordinary local minimum is 98 in the retain branch and 97 in the delete
branch, while a radius-99 cut must pay exactly the displayed excess outside
the local minima.

## 7. Locked-colour portal theorem

The upper colour `(1,1907)` has source provider `e_*=22511`.  Among its 35
off-source providers:

- none has both endpoints in the 466-node internal atlas;
- 14 cross from that atlas to

  ```text
  P = {97,490,502,546,581,620,623};
  ```

- the remaining 21 have both endpoints in `P`.

Every node of `P` has exactly two incident selected source edges.  Their union
is the 14-edge portal bank

```text
B = {4228,4936,18085,18185,18647,18659,20328,20359,
     21573,21581,22775,22790,22847,22858}.
```

### Theorem 7.1 (portal necessity)

Let `G` be any degree-balanced loopless exchange of `F` that deletes 22511
and preserves upper colour `(1,1907)`.  Its source cut contains an edge of
`B`.

#### Proof

Since 22511 is removed, `G` must select one of the 35 alternative providers.
Every such provider has at least one endpoint `v` in `P`.  It contributes
positive added incidence at `v`.  Deleted and added incidence are equal at
every vertex, so some selected source edge incident with `v` must be cut.
The only two selected source edges incident with `v` are the two recorded in
the portal bank.  Hence the cut meets `B`.  ∎

### Corollary 7.2 (exact necessary delete-branch portal filter)

In the radius-99 delete branch:

1. local excess two with no exterior cut is impossible;
2. local excess one with one exterior cut requires that exterior cut to be
   one of the 14 edges of `B`;
3. local excess zero with two exterior cuts requires the pair to meet `B`, so
   exactly

   ```text
   binom(468,2) - binom(454,2) = 6447
   ```

   exterior pairs survive.

Writing

```text
P0 = 16407450809840089013457044143740026880,
P1 = 5519466452430205944126949649954145042432,
```

for the exact local cut-bank products at excess zero and one, the surviving
count is

```text
6447 P0 + 14 P1
= 183051365705061937087534858694049983889408.
```

This is approximately 3.4672% of the unfiltered delete branch.
Here *surviving* means surviving this necessary portal filter; degree/q1
completion of any survivor remains unproved.

### Corollary 7.3 (scope at global radius 98)

The internal radius-98 option product retains 22511 and is the branch tested
by the joint-q1 model.  The omitted global radius-98 tier deletes 22511 at
ordinary local rank 97 and uses exactly one exterior cut.  The portal theorem
forces that exterior cut into `B`; its exact portal-filter candidate count is
therefore

```text
14 P0 = 229704311337761246188398618012360376320.
```

This is the exact number of motif-hitting cut banks surviving the portal
filter, not the number of degree/q1-feasible repairs.  This tier remains open.
Consequently the proved global statement is still
only that the joint residence/q1 radius is at least 98.  The internal face has
radius at least 99 under trusted CP, but a global radius-99 lower bound would
require closing the 14-portal radius-98 tier.

## 8. `dualrail.py` hardening retained in the handoff

The audited live snapshot
`/Users/amir.nuriyev/Downloads/opusproblem/work/dualrail.py` has SHA-256

```text
b4cec5ee93ecc7e41c68cbb573a59b7a35df0a3f126ff81eaad84cd77cd2ccc2.
```

Its rail subtour cut is now correct:

```text
sum_{e in rail-boundary(S)} (1-c_e)
+ sum_{e in rung-boundary(S)} y_e >= 1.
```

The earlier use of `c_e` made incumbent subtour rows vacuous.  The following
gates remain mandatory.

1. Input middle-deck, Johnson-cycle, q1, union-completeness and two-sided
   residence checks must fail closed; Python `assert` is not proof-safe under
   `python -O`.
2. The scalar row `b>=2` does not force an internal four-state B ear.  An exact
   mark `z_i` must imply

   ```text
   cB[i-1]=cB[i+3]=1,
   cB[i]=cB[i+1]=cB[i+2]=0,
   ```

   with zero endpoint flags at the two ear ends and `sum_i z_i>=1`.
3. A current PASS certifies at most a middle-deck-exact Johnson path, both q1
   palettes and positive internal residence.  The field called `cycle` is a
   path.  Arbitrary-width upper coverage, `COMP3`/lower coverage, and literal
   replay of all 65,535 nonempty masks are not checked.
4. The correct interim label is
   `CARRIER_Q1_RESIDENCE_PASS_NO_COMP3`, not `MASTER PASS`.
5. `INFEASIBLE`, `UNKNOWN`, `MODEL_INVALID`, and CEGAR-budget exhaustion must
   remain distinct statuses.

Accordingly `dualrail.py` supplies no evidence for the r98/r99 theorems above.

## 9. Permanent artifacts

The mathematical replay is local and solver-free:

```text
scratch/audit_k16_r98_r99_unique_q1_double_repair_20260729.py
  SHA e3f5ada896648448ccfe3a8867e13eaafba6890e760dcf36b355db8db8357bb9

scratch/k16_r98_unique_q1_double_repair_dp_20260729.json
  SHA f4be8118be2d89cc71d5641aaadd21b82a501bbf7ab9020afb168a70c098d4b5

scratch/k16_r99_retain_unique_q1_double_repair_dp_20260729.json
  SHA 607ff8d3cb302639db42c84e385d22870361af142386aced805d408c85aedf4c

scratch/k16_r99_delete_unique_q1_double_repair_dp_20260729.json
  SHA ee3b22f2c3e073fbb91cb472b249cf582bda9f5abfc61d3ce237341d87ac721a
  embedded payload SHA 7e007acbf5fb635ca62b3e0bdcdb82e57e2deaa0961cae21cf872e79e7814735
```

The guarded-model and trusted-CP diagnostics are:

```text
scratch/k16_r98_joint_q1_guarded_full_20260729.model.pb
  SHA c720ecec4f8216b5157dbbc1bd8768867c17b8930978f590221eb1b2c5a549d9

scratch/k16_r98_unique_rows_hard_20260729.json
  SHA 98655de470fc60a5d0eefb21fa52cc4ff88d26e6babafc2b7a63ad6c32f4177b

scratch/k16_r98_unique_q1_cegar_candidate_20260729.json
  SHA 36e90cf33f08c331760a7b6fb4d86e1b521e7e8cb95e79daa3f5e70093c37706
```

The relaxed 63-double witness and its solver-free replay are:

```text
scratch/k16_r98_unique_q1_double_repair_capacity_20260729.json
  SHA 855ae0012d7776847dd1bf698c5b861529e4360ba764528cc12ae966e98cf9e5

scratch/audit_k16_r98_double_repair_capacity_witness_20260729.py
  SHA 52ee5cffd211ca17b3fbfcf52cae3e6aee3dc45908fc9cc19cf58a519501fcc3

scratch/k16_r98_unique_q1_double_repair_capacity_20260729.audit.json
  SHA 9ed279eb135e618bc55cc5d4345bff3461437d26835051f580cad625b63a9849

scratch/extract_k16_r98_joint_q1_unsat_core_20260729.py
  SHA e96d8294c8f145bd98c80ac65fd5e32d1d6886a8fd3b698ab701225cb8ff3002
```

## 10. Sharp remaining boundary

The exact positive result is a solver-free, branch-complete unique-loss and
portal reduction.  The exact negative boundary is equally important:

- no sufficient CP assumption core was returned before termination;
- no deletion-minimal row core is certified;
- no rigorous ordinary LP/Farkas Hall cut has been found; the current GLOP
  transcript is only a non-replayable floating diagnostic;
- the double-repair matching demand is not capacity-obstructed; and
- the retain-22511 radius-99 branch has no proved provider-halo reduction.

The next mathematical gate is a stable integral coloured-b-factor odd-set
certificate for the internal option fibre, or a constructive completion that
shows the trusted CP no-go was relying on a narrower modelling assumption.
For global radius 98, the separate exact gate is the 14-edge locked-colour
portal tier of Corollary 7.3.
