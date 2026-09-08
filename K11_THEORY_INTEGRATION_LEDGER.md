# `k=11` mathematical-theory integration ledger

## Verdict

> **Corrected 2026-07-23.**  The former v1--v7 onion formulas were not
> exhaustive branch formulas.  Their filtration and named-cell circuits used
> the chain-A identity `y0=462+h1-h6` on chains B/C, which also contain the
> width-zero states `22`/`11`.  Those deployments are retracted as A-biased
> candidate subsearches.  They produced no candidate or certified result.

The current source repairs every A/B/C row under the exact chain selector.
Independent implementation and downstream-composition audits pass, and four
corrected candidate searches are live.  The exact correction is documented
in `K11_RANK5_SINGLETON_BOUNDARY_REPAIR.md`,
`K11_RANK5_ZERO_STATE_DEPENDENCY_BUG_AUDIT.md`, and
`K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md`.

## 1. Present in every deployed branch

The common deployed formula contains:

* the unrestricted interval-OR target constraints;
* exact adjacent rank-four/rank-seven shadow reuse;
* the globally WLOG rank-three shadow compression;
* rank-six witness-width band cuts;
* joint rank-five/rank-six width and endpoint cuts;
* endpoint-alignment cuts;
* coordinate-canonical literal rank-six and oriented boundary reductions;
* the singleton-pool cut;
* exact entry-rank one-hot variables and the strengthened local-density
  pseudo-Boolean inequalities;
* simultaneous physical containment caps;
* the exact six-subcube run-credit inequalities

  ```text
  7a28+5a29+3a30+a31 <= 462,
  6a28+4a29+2a30     <= 369.
  ```

The Type-I job additionally contains the unique endpoint-six-set branch and
the complete rank-filtration suffix architecture:

```text
A[0]=63 is the unique literal six-set,
all suffix ranks are at most five,
n5<=133,
one physical rank-at-most-four suffix component,
delta5=0.
```

The Type-II job contains the complementary complete architecture:

```text
no literal six-set,
all ranks are at most five,
n5<=134,
delta5+kappa5<=2.
```

With the corrected chainwise circuits, the two current branches are
exhaustive at the level of the audited rank-filtration theorem.  This was not
true of the historical v1--v7 binaries.

## 2. Branch-specific integration status

### Type I

The following exact consequences are valid.  Item 1 entered v2; the
rank-at-most-four named-cell family inclusion and its induced
`y2>=96+z` row entered v3:

1. the core-specific run-credit cut

   ```text
   7a28^C+5a29^C+3a30^C+a31^C <= 461;
   ```

2. the 464-position core covers at least 2041 of the 2047 nonzero masks;
3. its at most six missing masks form one nested prefix chain, with at most
   one loss in each rank six through eleven;
4. the exact boundary-pin/complement-rectangle restrictions at the unique
   endpoint interface.

The deployed v4 Type-I guard exposes the canonical part of items 2--3: every
noncanonical rank-seven through rank-ten selected witness avoids position
zero.  That deployed binary used `0/2,531` variables/clauses.  The current
local source compresses the equivalent selector cut to `0/32`: only 22
direct endpoint supersets, four crossed rank-seven endpoint supersets, and
one canonical-target implication for each of six exact-one generic slots are
needed.

After residual lex, the complete 2041-core count and six-loss coupling are
not a further circuit gap: all possible losses already belong to the fixed
chain `63,1087,1599,1855,1983,2047`.  The genuinely unencoded part of item 4
is the boundary-pin/complement-rectangle compatibility.

### Type II

When two physical rank-at-most-four components occur, all four facts below
entered v2.  V3 additionally localizes every selected lower witness to the
theorem-permitted singleton/pair/triple family and adds the conditional
`y2>=95+z` or `96+z` rows:

1. the literal rank-five entries are duplicate-free (the coupled row already
   implies this, but does not expose the branch explicitly);
2. the two component slacks are exactly `{1,2}`;
3. at least one component has total coordinate union `[11]`;
4. the slack-one component has every adjacent pair equal to a distinct
   rank-five target, and every lower target represented there is literal.

The all-dimensional laminar pin-capacity theorem adds a further family of
coordinate-deficit Hall inequalities and cross-rank deficit-merge budgets.
The first nonredundant coordinate-sensitive specialization is now encoded in
v5.  In the two-component branch, if `D2` is the coordinate deficit of the
slack-two component, then every rank-at-most-four mask meeting `D2` is literal
in the slack-one component.  The guard
`K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1` enforces `|D2|<=2`, the exact
rank vectors for deficits one and two, and

```text
z>=32 => |D2|<=1,
z>=97 => |D2|=0.
```

It adds `11,604/57,705` variables/clauses, for a full Type-II inventory of
`3,657,075/19,601,762`.  The broader all-rank deficit-merge family remains
without a production circuit.

The corrected source now also encodes the reverse orientation under
`K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1`.  If coordinate `b` is absent from the
slack-one component and `o_b` counts its occurrences in the slack-two
component, the circuit enforces

```text
o_b>=59,
h2+h4+h6 <= 3o_b+h1+h3+h5+76.
```

The second row is the chain-independent form of
`3o_b+z+y2>=386`.  The module adds `15,945/96,149`, passes an independent
theorem-to-CNF audit, and gives a strongest corrected Type-II inventory of
`3,676,391/20,175,839`.  One reverse-pin candidate seed is live alongside a
pin-localized control seed.

## 3. Audited theory deliberately not encoded separately

### Type-I boundary facets

The Type-I boundary/core decomposition now supplies a coordinate-sensitive
specialization that is not dominated by the scalar support ledger.  In the
inner peel `P5 || C4 || Q5`, every five-set facet satisfies

```text
#{i in C4 : A_i subseteq R} >= 20.
```

After residual lex fixes the endpoint six-set to `63`, the six facets
`63\{b}` are encoded by `K11_FOREST_TYPE1_FACET_PIN_LOAD=1`.  The guard adds
`8,304/49,788` variables/clauses and, together with the compressed 32-clause
prefix guard and rank-seven width moment, gives the deployed Type-I v7
inventory `3,648,797/20,036,415`.  This completes the first nonredundant
boundary-pin specialization of the Type-I complement rectangles; broader
rectangle families remain unencoded.


Some results do not currently justify another circuit:

* the Rayleigh lower-tail and moment laws are asymptotic interpretations of
  the finite cumulative rank cuts, not independent `k=11` constraints;
* the symmetric one-number projections of simultaneous multirank
  amortization are dominated by existing nested cap/run constraints at
  `k=11`;
* the common-zeta and laminar merge formulations are exact mathematical
  couplings, but encoding their full exponential family without first finding
  a nonredundant finite specialization would add size rather than useful
  propagation.

## 4. Search policy

The historical no-proof onion jobs are terminated or ended incompletely and
must not be cited as exhaustive.  A hypothetical SAT model from one would
still have been independently checkable, but no candidate was produced.
Only the corrected rank-five portfolio in
`K11_ONION_SUBCUBE_DEPLOYMENT_20260723.md` is a current exhaustive-branch
candidate search.  Any candidate must pass both independent interval-OR
verifiers; any UNSAT report still requires a proof-producing rerun and
independent proof checking.

The v3/v4/v5 portfolio has completed former steps 1 and 2, the first
nonredundant named-cell specialization of step 3, the first coordinate-pin
specialization, and the canonical endpoint chain portion of the former Type-I
upper-core target.  The next production
work should, in order:

1. independently audit and deploy the compressed Type-I selector cut, then
   encode a nonredundant specialization of its complement rectangles;
2. specialize the coordinate-deficit part of laminar pin capacity to a small
   set of nonredundant `k=11` cuts;
3. benchmark the v3 coordinate quotient and named-cell family against v2;
4. keep older seeds only as a deliberate formulation-diversity portfolio.

The subsequent v6 portfolio also encodes the audited four-truncated
rank-seven width moment under `K11_FOREST_RANK7_TRUNCATED_WIDTH=1`.  Its exact
rows are `T7>=930` in Type II and `T7>=940` in Type I, at an incremental cost
of `2,954/475,094` and `2,954/475,092` variables/clauses respectively.  This
completes the scalar rank-seven width part of item 1's outer-layer coupling;
the remaining useful target there is named endpoint/target compatibility, not
another profile moment.

No solver result, bound change, or claim of `nu(11)=465` follows from this
ledger.

## 5. Latest exact propagation specializations

Two further unrestricted consequences of the repaired onion architecture are
now implemented behind independent guards.

### Type-II companion orientation

If coordinate `b` is absent from the slack-two component `C2`, then all 176
rank-at-most-four targets containing `b` occur literally in slack-one `C1`,
and the rank-five family gives

```text
#{i in C1:b in A_i}>=176,
|C1|+z>=211.
```

`K11_FOREST_TYPE2_COMPANION_PIN_LOAD=1` reuses the exact C1 occurrence bank
from the reverse module and adds `10,220/71,628`.  Its theorem and
implementation audits pass.  A paired benchmark was favorable at 1,000
conflicts but unfavorable at 5,000, so it remains optional and is not in the
current four-slot portfolio.

### Type-I rank-one/rank-two interaction

Inside the Type-I rank-at-most-four core, nonliteral rank-two targets use
pairwise-disjoint adjacent atom witnesses.  Consequently

```text
n1+2*n2>=110.
```

The guard `K11_FOREST_TYPE1_GLOBAL_PAIR_PROFILE=1` adds `1,864/13,053`.
Independent audit passes.  The paired 5,000-conflict benchmark reduced mean
CPU by 11.6% and propagations by 51.9%; one ridge-only live seed was therefore
replaced by a ridge-plus-global-pair seed, while the facet-only seed remains
for diversity.

The same face analysis proves strict support at least five in every
three-face and the endpoint profile `c1+2*c2>=30`.  Those larger pointwise or
endpoint modules are mathematically audited but deferred until the compact
global row has accumulated longer-run evidence.

The frozen common source is

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
  k11_forest_sat.cpp
```

and the benchmark ledger is
`K11_NEW_PIN_PAIR_CUTS_MICROBENCHMARK_20260723.md`.  These are propagation
results only; no exact-value bound changes.

## 6. Fixed-prefix endpoint-chain theorem and certified repair screens

The append-completion side now uses the full endpoint-chain theorem, not
only its fixed-rank projection.  If a fixed prefix is missing a family `M`
and `q` entries are appended, then the selected targets ending at each new
position form an inclusion chain.  Therefore

```text
width(M)<=q.
```

The production append solver computes this width for small repair families,
adds endpoint at-most-one clauses for every incomparable pair across ranks,
and saturates a recovered maximum antichain when `width(M)=q`.  The audited
source SHA-256 is

```text
7e49ea13cd92b42a9a7c2bc7c3116e3b9dd6ca80719111b62d9163fef60368e3
```

with an independently verified original-append regression at
`1338/71164`.

This theorem completely closes two restricted length-476 neighborhoods of
the known 465-entry partial word:

* delete one and append twelve: 464 branches fail width and the sole
  survivor has a checked DRAT refutation;
* delete two and append thirteen: 107,861 branches fail width and all 19
  survivors have checked DRAT refutations.

The complete two-deletion proof archive has SHA-256

```text
828e3eda371978508fdcd0e4589c4770499eb4bef506210c573a4a804d835f36
```

and all nineteen verifier logs end in `s VERIFIED`.  See
`APPEND_MISSING_POSET_WIDTH_THEOREM.md`,
`K11_LENGTH476_SINGLE_DELETION_SCREEN_20260723.md`, and
`K11_LENGTH476_TWO_DELETION_SCREEN_20260723.md`.

The hierarchy has now been extended two complete levels further.

* Delete three and append fourteen: all `16,649,480` deletion triples were
  scanned twice structurally.  Exactly 159 have missing-poset width fourteen;
  158 contain index 102 and the unique exception is `(272,275,276)`.  Every
  one of the 159 exact append formulas has an independently checked UNSAT
  proof.
* Delete four and append fifteen: the primary scan covers all
  `1,923,014,940` quadruples.  Exactly 790 have width fifteen; 774 contain
  index 102 and 16 do not.  A direct quadratic interval audit independently
  checks all 790 survivor families and widths.  All 790 recency formulas have
  `s VERIFIED` proof logs.  Two runs of the second independently written
  all-branch aggregate scanner were externally terminated before their atomic
  final output, so the complete aggregate ledger continues to cite the
  primary exhaustive scan rather than claiming second full-scan agreement.

The fixed-branch recency formula is based on exact last-occurrence order, not
the production interval-selector circuit.  Its theorem, truth-table audit,
batch comparison, and proof inventories are in
`APPEND_RECENCY_CIRCUIT_AUDIT.md`.

At five deletions, literal enumeration would require
`C(465,5)=177,301,977,468` branches.  The new exact variable-deletion formula
represents the entire neighborhood at once.  It has

```text
2,523,666 variables
43,004,593 clauses
131,092,440 literals
```

and includes exact deletion-gated recency, sixteen nonzero append entries,
the rank-1--5 length-14 and rank-6 length-15 caps, and WLOG rank-5/rank-6
endpoint channels.  Independent small-instance enumeration, DIMACS parsing,
map checking, and byte-identical regeneration all pass.  The exact solve is
in progress; no result is claimed yet.  See
`DELETE_APPEND_RECENCY_CNF_AUDIT.md` and
`K11_LENGTH476_FIVE_DELETION_VARIABLE_FORMULA_20260724.md`.

The same endpoint-width theorem now gates the joint deletion/append
heuristic.  It rejected a `2045/2047` candidate whose retained-prefix missing
family had width seventeen.  Extending all 790 certified width-fifteen
four-deletion survivors by every fifth deletion checked 364,190 targeted
branches: 9,225 raw extensions have width sixteen, deduplicating to 2,727
five-deletion sets.  Exact fixed-recency solves for that targeted pool are in
progress.  The pool is not exhaustive for all five-deletion sets.  Missing
families are nonmonotone under restoration because deletion compression can
create cross-gap interval ORs, so even saving every width-sixteen
four-deletion base would not make this extension argument exhaustive.

These are construction-neighborhood exclusions.  They are not cuts on the
unrestricted length-465 onion formula and do not change the global bracket
`465<=nu(11)<=477`.

## 7. Linear-excess triangular endpoint braid: search consequence

The abstract triangular target system now has an ordered orthogonal
left/right endpoint realization in `|T_R|+R-1` positions with bandwidth at
most `2R+1`.  For `R>=2` that particular realization is maximally
nonfactorable: its height-zero witnesses cover the whole endpoint hull, so
the first positive height coordinate has no legal pin.  Insertion-only
padding cannot repair it; endpoint chains must be rerouted or duplicated.

This is an existence theorem in an endpoint relaxation, not a WLOG normal
form for a Boolean `k=11` word.  It therefore supplies no sound additional
SAT clause by itself, and forcing its endpoint schedule would exclude
potential solutions.  Its safe search consequence is strategic: scalar
endpoint scheduling and bandwidth are not the missing obstruction, while
the coordinate-pin modules already present in the Type-I/Type-II searches
probe the genuinely unresolved layer.  The proposed protected-backbone
superposition remains conditional and is not encoded as a cut.  In the
strict triangular/four-box auxiliary problem, allowed-letter spanning and
central-point inventory are additional constraints, so the theorem does not
by itself identify the whole quadratic portal cost with pin cost.

See `TRIANGULAR_ENDPOINT_BRAID_AUDIT.md` and handoff Section 303.
