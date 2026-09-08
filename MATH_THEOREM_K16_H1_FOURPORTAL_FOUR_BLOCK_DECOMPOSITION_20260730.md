# The K16 H1 four-portal fibre is an exact four-block coverage join

Date: 2026-07-30

## Scope and current verdict

This note concerns only the authenticated length-12873 H1 word with sole hole
`0x2c6d`, with the complement frozen and arbitrary nonzero substitutions
allowed at the thirteen positions

```text
0,1 | 4486,4487,4488,4489 | 6438,6439,6440 |
12869,12870,12871,12872.
```

The original raw Kissat run in

```text
/home/amodo/or15/work/root_k16_h1_fourportal_joint13_raw_20260730_8b4e73
```

reached its 1800-second cap.  It produced neither a SAT model nor an UNSAT
line and ended by SIGTERM at 1799.62 solver seconds.  Its incomplete DRAT is
not a proof.  Its exact status is `UNKNOWN_TIMEOUT`.

No statement below is a global K16 no-go, and no timeout is classified as
UNSAT.

## Exact decomposition theorem

Let `R` be the 55 residual targets not covered by an interval avoiding all
thirteen editable cells.  The independently audited occupancy map proves:

1. every target in `R` contains coordinate 6;
2. any changed interval realizing a target in `R` lies wholly inside one of
   the four displayed collars (the three intervening fixed gaps have ORs
   `0x7fff,0xffff,0xffff`);
3. in a fixed collar, the editable cells used by one witness form a nonempty
   contiguous interval; and
4. there are exactly `3+10+6+10=29` possible collar intervals for each
   target.

For a target `T` and a local interval `I`, write `need(T,I)` for the unique
audited minimal set of bits that the editable cells of `I` must supply after
the fixed prefix/suffix base is included.

> **Four-block coverage theorem.** The arbitrary-value joint13 fibre is SAT
> if and only if every `T in R` can choose one pair `(block,I)` such that,
> after defining
>
> ```text
> value(c) = intersection {T : the chosen interval of T contains c},
> ```
>
> with an empty intersection interpreted as `0xffff`, every bit of
> `need(T,I)` occurs in at least one `value(c)`, `c in I`.

**Proof.** Suppose physical cell values solve the fibre.  For each residual
target choose one realizing changed interval.  At a cell, intersect all
targets whose chosen witnesses cross the cell.  This canonicalization can
only remove bits forbidden by a selected target.  Every bit needed by a
selected witness occurred somewhere in that witness before canonicalization;
all selected targets crossing that occurrence contain the bit, so it remains.
Thus the displayed intersection values also solve the fibre.

Conversely, every intersection value is nonzero because all residual targets
contain coordinate 6.  It is a submask of every selected target crossing its
cell.  The `need` condition supplies precisely the target bits not already
supplied by the fixed base, so the chosen interval OR is exactly the target.
Targets already covered by a fixed-only interval remain covered.  Therefore
the resulting physical word is universal.  QED.

This is a four-way set-union join, not a monolithic 16-bit substitution
problem.  If `C_b(v)` is the subset of residual targets covered by a physical
value tuple `v` in collar `b`, the same theorem can be written

```text
exists v_0,v_1,v_2,v_3:
    C_0(v_0) union C_1(v_1) union C_2(v_2) union C_3(v_3) = R.
```

The canonical values lie in the intersection closure of `R`; this closure has
exactly 216 masks.  Hence the local search dimensions are `216^2`, `216^4`,
`216^3`, and `216^4`, but the two length-four collars admit a pair meet in the
middle.  A fully solver-free exact algorithm is therefore:

1. enumerate local coverage masks for the length-two and length-three
   collars;
2. for each length-four collar, enumerate left-pair and right-pair states,
   adding the four crossing-interval coverages at the join;
3. retain only inclusion-maximal 55-bit coverage masks in a ZDD; and
4. join the four ZDDs with a superset query for the uncovered complement.

This is an exact decision algorithm.  It is prepared as the fallback if the
strong witness CNF does not decide within its resource cap; no heavy local run
has been made.

## Strong explicit-witness CNF

The exact theorem gives a direct finite-domain encoding:

- one choice variable for each of `55*29=1595` target/witness pairs;
- exactly one witness per target;
- one availability variable for each of 13 cells and 15 non-common bits;
- a chosen witness requires each needed bit at some cell in its interval; and
- a chosen witness of a target omitting bit `q` blocks availability of `q` at
  every cell in its interval.

The resulting independently reconstructed formula has:

```text
variables  1790
clauses    55852
literals   121679
```

Clause families are:

```text
choice ALO                    55
choice pairwise AMO        22330
need -> some availability  10301
omitter -> blocked cell    23166
```

Artifacts:

| artifact | SHA-256 |
|---|---|
| builder `scratch/build_k16_h1_fourportal_joint13_witness_cnf_20260730.py` | `2a2db4190e794f13fd0e6dc4da9de537523cca3999271cdd28913829959f7647` |
| fail-closed decoder `scratch/decode_verify_k16_h1_fourportal_joint13_witness_20260730.py` | `bc55596502f7f53eaaf5a303220b5ec205b741712526d2efdf25149352464fe0` |
| independent audit `scratch/audit_k16_h1_fourportal_joint13_witness_cnf_independent_20260730.py` | `2141f02aeb34b62959674c88b9a5000f64de4cc2e968704c42f016f83ad0f127` |
| generated CNF | `f7c7c00592a682b994f6656ddf8f335ab272cd1517fb44a6cbd4e29061e19e47` |
| generated map | `146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a` |
| independent audit JSON | `e2b3f02f40733096327ed90eaa7b8106bcbd2e97e2a7923e60f268209c629279` |

The independent audit rebuilds all 55 one-of-29 rows and every clause from
the previously audited chart ledger, compares the complete clause multiset,
checks that the variable map is bijective, and records status `GO`.

## A certified one-clause-away phase

The decomposition also exposes an unusually sharp structural phase.  Choose
the first literal source witness for each of the 54 targets covered by the H1
word, and choose the singleton at flat cell 1 for the missing target
`0x2c6d`.  Canonical intersection then gives the thirteen values

```text
4879 2069 2849 2449 2069 2261 2869 206d 806d 8c62 8c63 cc61 ce61.
```

This complete assignment satisfies 55,851 of the 55,852 witness-CNF clauses.
Its unique falsified clause is the bit-11 availability requirement for
`0x2c6d` at flat cell 1.  The three selected source witnesses through that
cell whose targets omit bit 11 are `0x246d`, `0x346d`, and `0x766d`.

The phase is generated and checked by
`scratch/build_k16_h1_fourportal_joint13_near_phase_20260730.py`, SHA-256
`c9f8448debf114527054c692c35c2d7e58e2431da05f6c44c4d8d88d8b30bcbb`.
Its 120-variable flip set has SHA-256
`9c19821e729dc13cf2749107b76f8d262ac137524a5383ff7123ac4426102112`.
This does not prove satisfiability; it supplies a principled phase-flipped
fallback if the unhinted bounded run remains unknown.

### Exact bit-11 ejection frontier

Turning on the unique missing bit has a rigid first cascade.  The chosen hole
witness is the singleton at flat cell 1.  Its canonical value is `0x2069`, so
it lacks only bit 11.  Exactly three selected witnesses cross that cell while
omitting bit 11:

```text
0x246d, 0x346d, 0x766d.
```

An exhaustive check of all `27^3=19683` alternative local intervals for
these targets gives 13,393 internally non-self-blocking combinations.  Every
one must eject at least six further incumbent target witnesses.  Equality
occurs in exactly 32 combinations, split equally between only two sets:

```text
{2669,2e69,4879,6879,ce61,ce63}
{4879,6879,806d,a86d,ce61,ce63}.
```

Thus the smallest singleton-flat1 ejection frontier changes ten target
choices: the hole, its three immediate blockers, and one of the two displayed
six-target sets.  This is an exact first-frontier theorem, not an UNSAT claim.
The frozen audit is
`scratch/k16_h1_fourportal_bit11_exact10_20260730/frontier.audit.json`,
SHA-256 `6b22378df906ebb0a59ee3cd50b445f20a7724eb462b57515826d9da73cac5c1`;
its independent enumerator has SHA-256
`cfc586b9b0cbacc562c9859cf17d7e7cf808ccc34db03deaae2d9b1c07f28065`.

The two equality sets factor into three nested two-target portal pairs.  Both
use the first-collar pair `{4879,6879}` with intervals `[0,0] subset [0,1]`
and the last-collar pair `{ce61,ce63}` with intervals
`[11,12] subset [9,12]`.  The remaining pair is either the second-collar
pair `{2669,2e69}`, `[3,5] subset [2,5]`, or the third-collar pair
`{806d,a86d}`, `[8,8] subset [6,8]`.  Safe gaps make these three local costs
additive; only assignment of the ten free targets to collars remains coupled.

Two exact restricted CNFs freeze the other 45 target choices and force the
hole to singleton flat 1.  They have base-CNF hashes
`2317ed07edd39f6a881c6220328aa2b479354637c1df6d75e90ea40267aaa994`
and `f75560ae8afc840b68cdced52f7903923b91573c7f41c5e30d5deb683b77f2f8`.
The independent slice audit is
`scratch/k16_h1_fourportal_bit11_exact10_20260730/independent.audit.json`,
SHA-256 `a0bcbe687c60aeedceccfe21c260528989223cc091676cdbf5123a4eb8d5e27b`.
The fail-closed physical decoder has SHA-256
`f85b509b45af7ef3ccf29d55b226b1eb70739625d9cefd6408184dc85eec02fe`.
Any SAT result must pass this decoder and a complete 65,535-target replay.

In fact, neither restricted SAT run is needed.  A solver-free local DP freezes
the other 45 choices, enumerates every feasible subset of the ten free targets
inside each collar, and then performs the exact four-way disjoint-partition
join.  Its local family sizes and maximum target capacities are:

| slice | collar family sizes | collar maxima | sum |
|---|---|---|---:|
| second-collar pair | `100,7,1,12` | `5,2,0,2` | 9 |
| third-collar pair | `94,1,7,12` | `5,0,2,2` | 9 |

Both must assign ten free targets, but each has total additive capacity at
most nine.  The exact partition join is empty in both cases.  Therefore both
minimum-six-ejection slices are UNSAT by a separator theorem, without a SAT
solver or a DRAT proof.  The complete enumerated-family audit is
`scratch/k16_h1_fourportal_bit11_exact10_20260730/separator_dp.audit.json`,
SHA-256 `a428ed55afd53bd8479c950878453506e72be3b753545322da20bdfcb534c867`;
the audit program has SHA-256
`71ef974a3ade5f1c342a54a304e3740e8f4dba5fa60e77caf42861fabe2657c7`.

Consequently a completion using the singleton-flat1 hole witness must eject
at least seven external target choices, hence change at least eleven target
witness choices in total, or leave the minimum frontier in some other way.
This remains a statement about the rooted near phase, not unrestricted fibre
UNSAT.

The same exact method has now been carried through external radii seven,
eight, and nine.  Candidate generation is complete because every completion
must contain one of the Pareto blocker states.  The census is:

| external choices | total changed witness choices | candidate sets | capacity UNSAT | empty-join UNSAT |
|---:|---:|---:|---:|---:|
| 6 | 10 | 2 | 2 | 0 |
| 7 | 11 | 90 | 90 | 0 |
| 8 | 12 | 1,990 | 1,987 | 3 |
| 9 | 13 | 28,813 | 28,674 | 139 |

All 30,895 candidate joins are empty.  The exact radius-13 audit is
`scratch/k16_h1_fourportal_bit11_exact10_20260730/radius13.audit.json`,
SHA-256 `86eec82212188b24b0ae5ec28b953f104e4e33750e09c19d6b2147113af824c6`;
its payload hash is
`52a71be36d642cc2c229041e192a95b18204ec213c8eb8bb838dd33360dcfc9f`.

Thus the singleton-flat1 branch has no completion within 13 changed
target-witness choices of the certified phase.  This is **not** impossibility
of flat1 in the thirteen-cell support: witness choices are auxiliary and many
can change while only thirteen physical cells are edited.  The unrestricted
conditioned CNF below is the correct test of that stronger claim.

## Active bounded run

After the raw core-31 run ended, one materially different proof-retaining
Kissat run of the explicit-witness formula was launched on core 31 under

```text
/home/amodo/or15/work/root_k16_h1_fourportal_joint13_witness_20260730_f7c7c005
```

with seed 1731, a 1800-second wall cap, an 8-GiB address-space cap, and all
artifacts under `/home`.  It also reached the cap: exit 124 at 1799.91 solver
seconds, no SAT/UNSAT line, hence `UNKNOWN_TIMEOUT` and no claim.

The exact unrestricted flat1 condition adds only unit 467 to the witness CNF;
after the certified phase transform this is unit `-467`.  It has no witness
radius or edit-cardinality restriction.  Its original and transformed hashes
are

```text
08aa410fcc959fdd0a0ea7ce27d9ce92903148226c53f0884d09b92194a77b06
37ca680bf8d3197f5b0fd12fb002dca68ff259046166c125936396668d5ac119
```

and its independent audit has SHA-256
`8dbfbb418355db5e6c3b568bce9a37cde2a235af6e056eb617ddf1ce81a1359a`.
A single proof-retaining conditioned run was run under

```text
/home/amodo/or15/work/root_k16_h1_fourportal_joint13_flat1_20260730_8dbfbb41
```

on core 31.  It reached its wall cap with exit 124, no SAT model, and no
completed UNSAT proof.  Its final status is therefore `UNKNOWN_TIMEOUT`; the
partial DRAT file carries no mathematical claim.

## All 29 conditioned hole-witness branches

The four-collar decomposition also supports a solver-free census across every
possible local witness for the sole hole `0x2c6d`.  For each of the 29
contiguous intervals, the audit first reconstructs the complete inclusion-
minimal set of incumbent target choices that must be freed merely to supply
the hole.  It then tests every changed-target set at that minimum Pareto
radius by exact collar-local family enumeration and a disjoint four-way join.

All 29 minimum-radius branches fail by the stronger additive-capacity test;
none reaches the nontrivial partition join.  The minimum external radii, in
witness-index order, are

```text
2,0,3,12,9,6,2,12,9,5,11,7,11,7,4,
2,7,5,7,9,6,6,2,6,6,2,6,2,2.
```

The aggregate audit is
`scratch/k16_h1_fourportal_allh_minfrontier_20260730.audit.json`, SHA-256
`e221662ea9ba7a7eaa056a271e92e43f1b6d55c4223eb570e821d4dea6d54a80`;
its branch-ledger hash is
`754aeeff34de7bea6fa6ed148a29cd6ef3715374a167cf7685f90af83f71c8a4`.
The fail-closed aggregate checker has SHA-256
`604e0a6941f2e15cf418a7abe69ff0d425002922b14aff8a15e98278ca590078`.

This does **not** prove any conditioned branch UNSAT: it only proves that the
first Pareto ejection layer is locally too small.  The exact branch-radius
enumerator, SHA-256
`cbcca11983e306b7dec27fb0391449304871da6dc8d7b22547329352abb86372`,
is now growing the cheapest branches beyond their minimum frontier.  Its
radius counts changed target-witness choices relative to the frozen phase,
not physical edits.

For the particularly cheap witness `[2,5]` (index 6), one rooted cascade has
minimum supply frontier `{0xce61,0xce63}` after freeing its two immediate
blockers `{0x2669,0x2e69}`.  A separately frozen exact audit for that rooted
cascade has already excluded all 22,101 candidate changed-target sets through
five further external choices (eight changed target-witness choices total),
all by additive local capacity:
`scratch/k16_h1_fourportal_h6_radius5_20260730.audit.json`, SHA-256
`e11e30fa47e924e7cfd86cb0653cf73e736b3cfac6390a7d5494fe4f7cc7aade`.

The generic conditioned audit for witness `[0,0]` (index 0) is deeper.  It
enumerates every H-only Pareto-frontier superset through six external changes,
or seven changed target-witness choices including the hole.  At the last
radius, 270,387 of 270,725 candidates fail additive capacity and the remaining
338 have an empty exact four-way join.  The frozen audit is
`scratch/k16_h1_fourportal_h00_radius6_20260730.audit.json`, SHA-256
`59a31a152aa4a892255871c8215ffee191a222918833bc1210a939e546dfc6c1`;
its payload hash is
`3a009c958554c61cd903b94c713f87912b552f72fee941d7102bcda98233c913`.

## Exact 29-way conditioning of the composed formula

The independently audited 469-variable proxy/supply-code CNF admits a much
cleaner exhaustive split.  Target `0x2c6d` owns five binary code variables
`81,82,83,84,85`.  Its valid actions are exactly codes 0 through 28, while
the parent CNF already contains the three clauses excluding codes 29, 30,
and 31.  Appending the five code-unit clauses for each valid code therefore
gives 29 pairwise-disjoint branches whose union is exactly the parent model
set.

All 29 original and phase-flipped branch CNFs, maps, and flip files are under
`scratch/ad_k16_h1_joint13_29way_20260730/`.  The manifest has SHA-256
`5a9aa58e9407ebb12d2652f1baa2b02359f7204920d0aa4419fae9a67d2d5456`
and payload hash
`3bc249346bd800ab6c5059cdf9490745c9d726631935e51d91816b27faa52c20`.
The independent clause-for-clause and phase audit has SHA-256
`54079694caaf8a8e94a52d6d9c6d2e28738f3a4980e74e29ff2679eb291fa85d`,
status `GO_EXACT_DISJOINT_EXHAUSTIVE_PREPARED_NOT_RUN`, payload hash
`86bed586a3c56a82d5e47862065b31eccc8d09ee952c8b0d6fafa363c1f4c8e5`,
and branch-ledger hash
`d748de986065ec234842baf71839c37c96ada8da9e8981d18f942a1a701c251c`.
The builder and independent auditor have SHA-256 values
`85b5d7506b19520f23771035726865ee7e4dbe031107e55e3315b90baf8f5151`
and
`1cc7705458a138b4d637d03c65f71708200fb363d5b2c263dbf3692cd2c9f6c2`.

For each branch the deterministic phase keeps the 54 incumbent action codes,
substitutes that branch's hole action, intersects active targets at every
editable cell, and sets the supply variables from those canonical values.
The numbers of parent clauses violated by these complete phases are

```text
6,4,1,2,1,1,3,2,2,4,3,5,6,2,1,
3,2,4,4,3,8,12,17,2,7,12,6,12,4.
```

Thus branches 2, 4, 5, and 14 are each literally one clause away.  They were
launched as disjoint proof-retaining formulas, not as duplicate seeds of the
same CNF.  Exact branches 4, 5, and 14 have returned solver UNSAT and passed
independent `drat-trim` verification against their respective phase-flipped
branch CNFs.  Their proof and checker-output SHA-256 pairs are

```text
branch  4  c0eaff9af15ff1bd6b95464b1e7f729866bd5009a4627071813fe41799c89223
           6a987d4c2a6bf80be90b13dd60c4b9e6b967658bb4089fb00a33cbcfb22461ee
branch  5  58dff95a03c110aad9d2a883c4cf7e0c6f6fa4e4310af9c373e75ec6f392da6c
           dc8d2cdd9f690f309b40d97b1e4adcbc9377fb5b2a42c68fc6157b82ae13754b
branch 14  043c404661b4aedfe280a6788058224fe552613ff07cd9b35c410b869db33471
           68cec634131d796f5776460663c9ccb2012cc094436ea46135b52c34bebdb060
```

These are rigorous theorems only for conditioned actions 4, 5, and 14.
Branch 2 reached its bounded solver cap with exit 0 and status `s UNKNOWN`, so
it remains open.  The first four near-two-clause branches were then launched;
branch 8 has likewise returned `UNSAT_DRAT_VERIFIED`, with proof SHA-256
`8659d12113b5b573534e6c8eff5ce5b442f18fda9120439a87ee50b3b21ca187`
and checker-output SHA-256
`4aa5673b03c48c5c6673f3b7ffa4ac063582456d0e25b6cfdc95948363bd1bd5`.
No conclusion about the full 29-way union follows until every branch is
decided; all timeout/unknown branches remain explicitly open.
