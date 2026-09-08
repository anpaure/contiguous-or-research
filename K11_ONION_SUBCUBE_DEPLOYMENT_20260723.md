# Deployment of exact `k=11` onion/subcube branches — 2026-07-23

## Evidentiary status

The two audited rank-filtration architectures now form an exact case split
for a hypothetical nonzero length-465 word:

* Type II: no literal six-set;
* Type I: one canonical endpoint six-set.

Both were deployed with the exact subcube run-credit circuit.  The four live
solver processes described below are candidate generators only.  At this
snapshot none has emitted `SAT`, `UNSAT`, or a candidate file.  A model must
pass both independent interval-OR verifiers.  An UNSAT conclusion requires a
separate archived proof-producing run and independent proof checking for both
branches.

## Frozen production artifacts

Host:

```text
root@157.157.221.29:27423
directory /root/k11_onion_20260723
```

Hashes:

```text
ab9a3e1cce0325469adbb57d8c39c9a5b660f194c20b9ff6b099497f0ba9c4ea  k11_forest_sat.cpp
928f27fc822374405f39abc34332a7ca283b45d4932ab8659d40ac8f673a5a3b  k11_forest_sat_onion
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd  k11_upper549_natural_array.txt
```

The remote build command was

```text
g++ -O3 -std=c++2a -I/root/cadical/src \
  k11_forest_sat.cpp /root/cadical/build/libcadical.a \
  -lpthread -o k11_forest_sat_onion
```

## Common exact guards

Every deployed process enables

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1
K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_SINGLETON_POOL_CUT=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_LOCAL_DENSITY_PB=1
K11_FOREST_CONTAINMENT_CAPS=1
K11_FOREST_SUBCUBE_DEFICIENCY=1
```

Type II additionally enables

```text
K11_FOREST_RANK6_BRANCH=0
K11_FOREST_RANK_FILTRATION_TYPE2=1
```

and has exact build inventory

```text
variables=3632888 clauses=19446941
```

Type I enables

```text
K11_FOREST_RANK6_BRANCH=1
K11_FOREST_RANK_FILTRATION_TYPE1=1
```

and has exact build inventory

```text
variables=3633096 clauses=19448397
```

The deterministic remote build logs have hashes

```text
1bb1447833f28d8fb35b9ff81b568790f199ed8aaf19e9013aa5c2caa67434b5  type2_build.log
78cc0e4b3d1b03170ae8419dc17a0d44ab811005d92f89e2e863ae6be8119674  type1_build.log
```

## Live portfolio

At `2026-07-23 10:38 UTC`, the host had 124 GiB RAM and 6.9 GiB free disk.
Four no-proof CaDiCaL searches were launched:

| branch | seed | CPU | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II | 120 | 0 | 149764 | `type2_120.log` | `candidate_type2_120.txt` |
| Type II | 122 | 2 | 149765 | `type2_122.log` | `candidate_type2_122.txt` |
| Type I | 121 | 4 | 149766 | `type1_121.log` | `candidate_type1_121.txt` |
| Type I | 123 | 5 | 149767 | `type1_123.log` | `candidate_type1_123.txt` |

The processes were live and consuming CPU at the post-launch snapshot; no
candidate file existed.  These searches intentionally omit proof generation
to avoid filling the 20 GiB overlay.  Any no-proof UNSAT return is only a
signal to schedule one proof-producing branch at a time.

## First poll

At `2026-07-23 10:46:45 UTC`, all four PIDs were still live and consuming
CPU.  The logs contained only the frozen build inventories; no solver had
reported `SAT` or `UNSAT`, and no candidate file existed.  The three local
exact `Q_9` cyclic-interval SCD searches were also still live at this poll.

## Second poll: v1 processes ended without a result

At `2026-07-23 11:38:54 UTC`, PIDs `149764`--`149767` were absent.  All four
candidate paths were still absent, all four stdout files were empty, and the
four stderr logs contained only their original deterministic formula
inventory.  In particular, no log contained `SAT`, `UNSAT`, an exit code, or
another terminal marker.

The cause of termination is not recorded in the artifacts inspected at this
poll.  The v1 searches are therefore classified as
**interrupted/incomplete**, with no mathematical consequence.  They must not
be described as SAT, UNSAT, timed out, or proof attempts.

## Enhanced v2 deployment

The same remote directory now contains a second, stronger frozen source and
binary:

```text
1c3ce629c74aeef7339e2d43bd2f922aaf5b98d24f6a993d2d4f01aea7c63d06
  k11_forest_sat_onion_v2.cpp
3cefbfbd64b44966dc09f63174c32518a56d93d16c48cd2d894896f9c3250773
  k11_forest_sat_onion_v2
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd
  k11_upper549_natural_array.txt
```

The source hash is identical to the current local `k11_forest_sat.cpp`.
The remote compiler reports

```text
g++ (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0.
```

Every v2 process retains all common exact guards listed above.  Relative to
v1, the exact branch-specific additions are:

* Type II: the audited two-component automaton, common coordinate-complete
  component selector, and slack-one adjacent-pair row from
  `K11_RANK_FILTRATION_TYPE2_COMPONENT_ENCODING.md`;
* Type I: the audited 464-position suffix-core proper-target charge
  inequality from `K11_TYPE1_CORE_SUBCUBE_ENCODING.md`.

The local independent checkers were rerun against the frozen source and
reported

```text
type2_component_automaton=PASS
type2_coordinate_selector=PASS
type2_adjacent_pair_support=PASS
type2_variables=9814 clauses=47310 PASS

p_63=32 equivalence gate: PASS
eta(p_63-1)=gamma(p_63)+delta truth table: PASS
adjusted <=461 comparator semantics: PASS
Type-I core inventory: 25 variables, 189 clauses: PASS
production wiring anchors: PASS
```

Their hashes are

```text
d4ccaae6478195777d033d4081c5ff598664a6049907e09902558d68247819b0
  scratch/verify_k11_rank_filtration_type2_components.py
d06bcd3f740b0c1d5878a13391c29302d5007f4b1b181f039f5c96c945c49c6d
  scratch/verify_k11_type1_core_subcube_encoding.py
```

### Exact v2 inventories

Type II has

```text
variables=3640328 clauses=19476694
rank_filtration_type2_variables=9814
rank_filtration_type2_clauses=47310
rank_filtration_type2_component_automaton_clauses=6032
rank_filtration_type2_coordinate_separator_clauses=22789
rank_filtration_type2_slack_one_pair_clauses=932
subcube_deficiency_variables=646781
subcube_deficiency_clauses=4309410
```

Type I has

```text
variables=3633121 clauses=19448586
rank_filtration_type1_variables=2341
rank_filtration_type1_clauses=17354
subcube_deficiency_variables=646806
subcube_deficiency_clauses=4309599
subcube_type1_core_variables=25
subcube_type1_core_clauses=189
```

The deterministic v2 build-log hashes are

```text
7dd62b8ea4ed416c045b4134a016ce84b50769690bd4a07f8ded8b4b7264ce26
  type2_v2_build.log
f5daa184d0a1601cdfc8c17f626f493bda262a6d92abfd6a42a664faca912003
  type1_v2_build.log
```

### Live v2 portfolio

All four processes started at `2026-07-23 11:36:36 UTC`:

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II | 130 | 0 | 150237 | `type2_v2_130.log` | `candidate_type2_v2_130.txt` |
| Type II | 132 | 2 | 150238 | `type2_v2_132.log` | `candidate_type2_v2_132.txt` |
| Type I | 131 | 4 | 150239 | `type1_v2_131.log` | `candidate_type1_v2_131.txt` |
| Type I | 133 | 5 | 150240 | `type1_v2_133.log` | `candidate_type1_v2_133.txt` |

Inspection of `/proc/PID/environ` reproduced the complete expected common
guard set and the appropriate branch/type guard for every PID.  File
descriptor inspection also confirmed that each stdout and stderr stream is
attached to the correspondingly named files above.

At `2026-07-23 11:39:19 UTC`, all four were live and consuming CPU.  Their
resident sets were between 3.68 and 4.35 GiB.  No candidate file existed,
stdout was empty, and each stderr log contained only the exact build
inventory.  Snapshot log hashes were

```text
11592c233f0b41e895b5b616eb33774758009b7397857ac40b9a921425b91a74
  type2_v2_130.log
11592c233f0b41e895b5b616eb33774758009b7397857ac40b9a921425b91a74
  type2_v2_132.log
61ad110b9c6b19a55a173effb8f197a742dc1c9edb7b8971bd08a2ef652793cb
  type1_v2_131.log
61ad110b9c6b19a55a173effb8f197a742dc1c9edb7b8971bd08a2ef652793cb
  type1_v2_133.log
```

The empty stdout files have the standard SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Rose had 6.9 GiB free disk and 87 GiB available memory at this snapshot.

A second read-only liveness poll at `2026-07-23 11:44:10 UTC` again found
all four PIDs live and CPU-bound, with no candidate and no terminal marker.

These are again no-proof candidate generators.  A no-proof UNSAT exit would
remain uncertified and would require a frozen proof-producing rerun.

## Named-cell/coordinate-quotient v3 deployment

The first post-blocker-barrier named-cell theorem was encoded together with
the residual coordinate-column symmetry quotient.  The frozen artifacts are

```text
edc223f436db6e86553cb997eb552301546049582efbb238d2784db56b876d38
  k11_forest_sat_onion_v3.cpp
28ed1d32b23665754017085ce46cec9c5ed86e99c32f8f9ba4566e809097d072
  k11_forest_sat_onion_v3
```

Relative to v2, both branches add

```text
K11_FOREST_NAMED_CELL_HALL=1
K11_FOREST_RESIDUAL_COORD_LEX=1.
```

The named-cell guard chooses all rank-at-most-four witnesses in the
branch-permitted physical family and exposes the derived rank-five triple
rows.  The lex guard sorts coordinate occurrence columns under the residual
`S_11` (Type II) or `S_6 x S_5` (Type I) action.

Exact v3 inventories are

```text
Type II: 3,645,471 variables / 19,544,057 clauses;
Type I:  3,637,539 variables / 19,511,503 clauses.
```

The incremental named-cell inventories are

```text
Type II: 489 variables / 39,453 clauses,
         plus 13 variables / 59 clauses exposing duplicate excess;
Type I:  241 variables / 37,851 clauses.
```

The residual-lex increments are

```text
Type II: 4,641 variables / 27,851 clauses;
Type I:  4,177 variables / 25,066 clauses.
```

Remote build-log hashes are

```text
bd72975460b32c91892265329dafb5b65c4ebee1b98f7b3b27b6274e6d0fa1a7
  type2_v3_build.log
c84a737f39b6e0dd4df2cd088e8d2789343306643fc8f94b56b70aac9580bfcf
  type1_v3_build.log
```

The theorem checker, implementation checker, lex truth-table checker,
syntax build, and both local and remote build-only inventories passed before
launch.

At `2026-07-23 12:11:36 UTC`, two additional no-proof candidate generators
were live:

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II | 171 | 6 | 150769 | `type2_v3_171.log` | `candidate_type2_v3_171.txt` |
| Type I | 173 | 9 | 150770 | `type1_v3_173.log` | `candidate_type1_v3_173.txt` |

Both consumed one full CPU and had resident sets of approximately 3.50 and
4.21 GiB.  No candidate or terminal marker existed.  An initial launch on
CPUs 1 and 3 exited before entering the solver because those CPUs were not in
the container's allowed affinity set; PIDs `150693,150694` therefore carry no
search evidence.

The host subsequently exposed an effective four-CPU quota.  PID `150770`
(the first v3 Type-I attempt on CPU 9) disappeared with only its inventory
line, empty stdout, no candidate, and no terminal marker; it is classified as
interrupted/incomplete.  To keep one old formulation per branch while making
room for both v3 branches, the redundant v2 Type-I PID `150240` was terminated
without a candidate or terminal result.  A replacement v3 Type-I seed was
then launched on its released CPU:

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type I | 175 | 5 | 150905 | `type1_v3_175.log` | `candidate_type1_v3_175.txt` |

At `2026-07-23 12:18:55 UTC`, the live rose portfolio was therefore:

```text
v2 Type II: PIDs 150237,150238 (together one effective CPU),
v2 Type I:  PID 150239,
v3 Type II: PID 150769,
v3 Type I:  PID 150905.
```

All were consuming their allotted CPU; neither v3 candidate path existed.

## Concurrent purple snapshot

At `2026-07-23 11:40:59 UTC`, the six older purple-host `k=11` processes
from `REMOTE_SEARCH_TRIAGE_20260723.md` were still live:

```text
generic branches:                  PIDs 164667, 164668
old-threshold density/caps:        PIDs 170487, 170488
corrected-threshold density/caps:  PIDs 171730, 171729
```

None of their six candidate files was nonempty, and none of their logs had a
SAT/UNSAT/exit marker.  They do not contain the v2 rank-filtration/subcube
circuits and remain only diversity searches.  No `k=14` append solver was
live at this poll.  Purple had 1.4 GiB free disk (94% used); no write or
process intervention was performed.

## Current exact conclusion

No `k=11,n=465` bound changed in any deployment generation.  The v1
portfolio ended incompletely.  The enhanced v2/v3 portfolio, its v4 Type-I
replacement, and six older purple diversity processes have produced no
candidate and no terminal solver result at the timestamps above.

## Type-I canonical-prefix v4 deployment

The exact Type-I prefix-chain consequence was added under
`K11_FOREST_TYPE1_PREFIX_CHAIN=1`.  It adds no variables and exactly 2,531
clauses.  The frozen remote artifacts are

```text
3e4f12d89f16b948e6919572a2bab9f400f7dda57931dc4d33d7840b67399282
  k11_forest_sat_onion_v4.cpp
bb023365bd76f528b4f2dd1376dc29aa523cef8bb2a0e14053fe80f9f6946fee
  k11_forest_sat_onion_v4
```

The real remote build-only inventory is

```text
3,637,539 variables / 19,514,034 clauses,
type1_prefix_chain_clauses=2,531.
```

Its build-log SHA-256 is

```text
0ab5005dbaae52075a975d36bc64b7fa6235fe5b97bb8dd4e51a0b3aa4e7c771
  type1_v4_build.log
```

At `2026-07-23 12:35 UTC`, the weaker v3 Type-I PID `150905` was terminated
without a candidate or terminal marker and replaced on the same affinity by

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type I v4 | 183 | 5 | 151172 | `type1_v4_183.log` | `candidate_type1_v4_183.txt` |

Eight seconds after launch, PID `151172` was live at one full CPU with
approximately 3.97 GiB RSS.  Its candidate did not exist and its log
contained exactly the audited inventory.  This remains a no-proof candidate
generator, not evidence for SAT or UNSAT.

## Type-II coordinate-pin v5 deployment

The first genuinely coordinate-sensitive specialization of the laminar pin
constraints was added under

```text
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1
```

It applies only in the exact Type-II two-component branch.  After orienting
the components by their `{1,2}` slacks, it records the coordinate union of
the slack-two component.  Every rank-at-most-four mask meeting its coordinate
deficit is forced to occur literally in the slack-one component.  In
particular, the circuit enforces the exact conditional rank-count vectors

```text
one missing coordinate: (1,10,45,120),
two missing coordinates: (2,19,81,204),
```

and the threshold consequences

```text
z>=32 => deficit<=1,
z>=97 => deficit=0,
```

where `z` is the number of literal rank-five entries.  The mathematical note,
independent source audit, and exhaustive gate/comparator/inventory checker are
`K11_TWO_COMPONENT_PIN_LOCALIZATION.md`, its audit, and
`scratch/check_k11_two_component_pin_localization.py`.

The frozen remote artifacts are

```text
8ed684b780cd2f4239b7eee76c894e5141e40f4d2ccc2345d53536566e53231e
  k11_forest_sat_onion_v5.cpp
5a62d81b6688ddb99e7d5917edf4307c621c2cac0a43598d8d728a088da94358
  k11_forest_sat_onion_v5
```

The real remote build-only inventory is

```text
3,657,075 variables / 19,601,762 clauses,
two_component_pin_variables=11,604,
two_component_pin_clauses=57,705.
```

The build log has SHA-256

```text
37db58098b185d2def87fca5619a581259567fefff686a08dea4228c5d274704
  type2_v5_build.log
```

Immediately before replacement, v3 Type-II PID `150769` was still live after
approximately 68 CPU minutes.  Its candidate was absent and its log had no
SAT, UNSAT, exit, or terminal marker.  It was terminated as an incomplete
redundant search and replaced on the same affinity by

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II v5 | 191 | 6 | 151652 | `type2_v5_191.log` | `candidate_type2_v5_191.txt` |

At `2026-07-23 13:22:05 UTC`, PID `151652` was live at one full CPU with
approximately 4.49 GiB RSS.  `/proc/151652/environ` reproduced every expected
common, Type-II, named-cell, residual-lex, and pin-localization guard.  Its
stdout/stderr descriptors pointed to the displayed files, its candidate did
not exist, and its log contained exactly the audited formula inventory.  This
is again a no-proof candidate generator only.

## Rank-seven truncated-width v6 deployment

The boundary-resolved rank-five/rank-six/rank-seven theorem proves the
stronger four-truncated moment

```text
sum min(width_7,4) >= 930   (Type II),
sum min(width_7,4) >= 940   (Type I).
```

The second row uses the existing Type-I boundary profile.  Under adjacent-
shadow compression, every inactive rank-seven target is safely assigned its
maximum virtual truncated credit four.  The optional production guard is

```text
K11_FOREST_RANK7_TRUNCATED_WIDTH=1
```

and adds 2,954 variables in either branch, with 475,094 clauses in Type II
and 475,092 in Type I.  Independent audits exhausted 1,300,140 threshold
cases, the 14-clause full-adder truth table, the complete 990-input signed
counter, both ten-bit comparators, invalid prerequisite configurations, and
guard-off identity.  See `K11_THREE_LAYER_WIDTH_ALIGNMENT.md`, its audit,
`K11_RANK7_TRUNCATED_WIDTH_IMPLEMENTATION.md`, its independent audit, and the
two checkers in `scratch/` named there.

The frozen remote artifacts are

```text
31dbc54a87af387287e729f708bd31c9fe573a988d62345b0bc10480470c8eda
  k11_forest_sat_onion_v6.cpp
2a04e6befc171892a6b7a6bf9609e11e07202134ff2b94d75e768f1cea4c6b59
  k11_forest_sat_onion_v6
```

The exact remote build-only inventories are

```text
Type II: 3,660,029 variables / 20,076,856 clauses;
Type I:  3,640,493 variables / 19,989,126 clauses.
```

Their build-log hashes are

```text
dba15a7d0ded6abb5040db79657d30b9cbfae8e166678454577c4f0106d3a823
  type2_v6_build.log
d2d40e0b282bef95d287a7e15ee532a0aef91c5d720c239442579c199ce07d3f
  type1_v6_build.log
```

Before this deployment, Type-I v4 PID `151172` had disappeared after an
incomplete run: its candidate and stdout were absent, and its inventory-only
log had no terminal marker.  The two v2 Type-II jobs, PIDs `150237` and
`150238`, were still live after approximately 63 CPU minutes each, with no
candidate or terminal marker.  They were terminated as the weaker redundant
Type-II formulation.  The surviving v2 Type-I process retains deliberate
formula diversity.

The v6 jobs were launched as

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II v6 | 197 | 0 | 152048 | `type2_v6_197.log` | `candidate_type2_v6_197.txt` |
| Type I v6 | 199 | 5 | 152045 | `type1_v6_199.log` | `candidate_type1_v6_199.txt` |

At `2026-07-23 13:44:03 UTC`, both were live and CPU-bound.  Their environment
and file-descriptor audits reproduced the complete intended branch guards and
the corresponding log/output paths.  Neither candidate existed, both stdout
files were empty, and each log contained exactly its audited inventory.

The balanced live rose portfolio at that snapshot was therefore

```text
Type I v2: PID 150239 (formula-diversity seed),
Type II v5: PID 151652 (pin localization, no width moment),
Type I v6: PID 152045 (canonical prefix plus width moment),
Type II v6: PID 152048 (pin localization plus width moment).
```

All remain no-proof candidate generators.  No bound or solver conclusion
follows from their continued execution.

## Type-I boundary-facet pin-load v7 deployment

The Type-I inner peel has the exact form

```text
P5 || C4 || Q5,
```

where `C4` consists of rank-at-most-four entries.  For every five-set `R`,
the boundary-facet theorem proves

```text
p_R^C = #{i in C4 : A_i subseteq R} >= 20.
```

The proof is coordinate-sensitive: the slack-two core gives a length-three
run cap inside each five-set facet, at most one such run can have length
three, and the thirty nonempty proper subsets of `R` require distinct
singleton/pair cells.  Nineteen support positions provide at most twenty-nine
such cells.  This is not implied by the existing scalar subcube-support
ledger.  The six lex-fixed facets `R=63\{b}`, `0<=b<6`, are encoded under

```text
K11_FOREST_TYPE1_FACET_PIN_LOAD=1.
```

The guard requires the Type-I and subcube-deficiency guards, reuses the
already-defined support set for the fixed six-set `63`, and adds exactly

```text
8,304 variables / 49,788 clauses.
```

The theorem, mathematical audit, implementation note, and source checker are
`K11_TYPE1_BOUNDARY_FACET_PIN_LOAD.md`, its audit,
`K11_TYPE1_FACET_PIN_LOAD_IMPLEMENTATION.md`, and
`scratch/check_k11_type1_facet_pin_load_source.py`.  The source audit also
checks the independently compressed 32-clause Type-I prefix-chain guard.

The frozen remote artifacts are

```text
0d41fbd4cfe3ac075c850b0cfe41cea740608bfa953b53d7ffc40d2a1e3bd6d5
  k11_forest_sat_onion_v7.cpp
c70ca4d61498bea7c9e663e9c16bee1822eae38b9e40bcba577d31d9b9a5d9ed
  k11_forest_sat_onion_v7
2da3500b31e54686c3dce439696f25c1e9035f05ae38a09845d19fdb3f3e8c6e
  type1_v7_build.log
```

The exact Type-I build-only inventory is

```text
3,648,797 variables / 20,036,415 clauses,
type1_prefix_chain_clauses=32,
type1_facet_pin_load_variables=8,304,
type1_facet_pin_load_clauses=49,788.
```

The prior Type-I v6 PID `152045` had no candidate or terminal marker and was
terminated as the superseded same-branch formulation.  The v7 job was
launched as

| branch | seed | affinity | PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type I v7 | 211 | 5 | 152670 | `type1_v7_211.log` | `candidate_type1_v7_211.txt` |

At `2026-07-23 14:29:59 UTC`, PID `152670` began running with PPID 1.  Its
environment reproduced all intended common and Type-I guards, including the
rank-seven truncated-width, compressed prefix-chain, subcube-deficiency, and
facet pin-load guards.  Its stdout/stderr descriptors pointed to the named
files and its log reproduced the exact inventory above.  At the latest health
check the candidate was absent and the log had no SAT, UNSAT, exit, or
terminal marker.

The balanced live portfolio is now

```text
Type I v2: PID 150239 (older formulation-diversity seed),
Type II v5: PID 151652 (pin localization without width moment),
Type II v6: PID 152048 (pin localization plus width moment),
Type I v7: PID 152670 (width, compressed prefix, and facet pin load).
```

All four remain no-proof candidate generators.  Their continued execution
does not change either bound.

## Retraction of the onion search formulas: rank-five zero-state bug

Subsequent source audit found a satisfiability-completeness error in every
Type-I/Type-II onion generation above.  The joint rank-five schedule permits
three maximal chains

```text
A = 00,01,02,12,13,23,33,
B = 00,01,02,12,22,23,33,
C = 00,01,11,12,13,23,33.
```

The filtration and named-cell modules nevertheless used

```text
y0=462+h1-h6,
```

which is correct only on chain A.  Chains B and C have additional
width-zero blocks `22` and `11`:

```text
B: y0=462+h1+h5-h4-h6,
C: y0=462+h1+h3-h2-h6.
```

Reversal interchanges B and C but fixes A, so chain A is not globally WLOG.
The old formulas were strict A-biased subformulas.  Consequently none of the
v1--v7 onion searches was an exhaustive search of its advertised Type-I or
Type-II branch.  A SAT candidate would still have been independently
verifiable, but silence or UNSAT from these formulas would have had no
global consequence.  No SAT candidate or UNSAT certificate was produced.

All remaining affected rose processes were stopped or had already ended
incompletely.  A read-only audit on 2026-07-23 found PIDs

```text
150239, 151652, 152048, 152670, 153361
```

absent, their corresponding candidate files absent or empty, and no SAT or
UNSAT marker in the inspected logs.  These runs are permanently classified
as **interrupted/incomplete**.

The authoritative mathematical and dependency audits are

```text
K11_RANK5_SINGLETON_BOUNDARY_REPAIR.md
K11_RANK5_ZERO_STATE_DEPENDENCY_BUG_AUDIT.md
```

The corrected source encodes the Type-II stability rows

```text
A: n5+h6+s       <= h1+464,
B: n5+h4+h6+s    <= h1+h5+464,
C: n5+h2+h6+s    <= h1+h3+464,
```

and the analogous Type-I equalities with constant `462`, each under the
existing exact-one chain selector.  It also repairs the chain-B/C named-cell
rows and defines the Type-II tightness/duplicate flag from the equality on
the selected corrected row.

The first repaired source has SHA-256

```text
f86e80456f2e17fd87774579d11dd090f70f2451e888537212eb1b9613aca6e2
  k11_forest_sat_rank5repair.cpp
```

and remote binary SHA-256

```text
17bed4d6957eef3346850c3cebf883f0d503ec037ad8e1f6ac30491f63be1f09
  k11_forest_sat_rank5repair
```

Fresh real-CaDiCaL build-only inventories for the strongest repaired
portfolios are

```text
Type I + facet + ridge: 3,669,795 variables / 20,162,593 clauses,
Type II + pin localization: 3,660,446 variables / 20,079,690 clauses.
```

Their build-log SHA-256 values are

```text
f2c0f78f72cd6e4f0c8eab4b4a8c1d8c707974c9c92220574325ac25ec438933
  type1_rank5repair_build.log
aee136184fa567567bd52d38dea83e6a6f60d3aa819439b25282eda1184af362
  type2_rank5repair_build.log
```

These are build validations only.  Corrected solver searches are not listed
as deployed until the independent implementation and downstream-composition
audits finish.

## Corrected rank-five portfolio deployment

Both required independent audits now pass:

```text
K11_RANK5_SINGLETON_BOUNDARY_REPAIR_IMPLEMENTATION_AUDIT.md
K11_RANK5_REPAIR_DOWNSTREAM_AUDIT.md
```

They independently verify all A/B/C arithmetic, active-chain tightness,
duplicate semantics, named-cell B/C rows, full carries, guard behavior, and
the unchanged soundness of the Type-I core/facet/ridge, Type-II component/pin,
and rank-seven modules.  No remaining production A-only assumption was
found.

Four no-proof candidate searches were launched from the corrected frozen
binary:

| branch | seed | CPU | wrapper PID | solver PID | log | candidate |
|---|---:|---:|---:|---:|---|---|
| Type I + facet + ridge | 301 | 9 | 153934 | 153935 | `type1_rank5repair_301.log` | `candidate_type1_rank5repair_301.txt` |
| Type I + facet + ridge | 303 | 12 | 153939 | 153940 | `type1_rank5repair_303.log` | `candidate_type1_rank5repair_303.txt` |
| Type II + pin localization | 302 | 4 | 153941 | 153943 | `type2_rank5repair_302.log` | `candidate_type2_rank5repair_302.txt` |
| Type II + pin localization | 304 | 5 | 153942 | 153944 | `type2_rank5repair_304.log` | `candidate_type2_rank5repair_304.txt` |

The Type-I solvers were moved from busy CPUs 0/2 to distinct cores 9/12
after launch; the table records their current affinities.  All four solver
PIDs were live and CPU-consuming at the health snapshot.  Their exact sorted
guard-environment hashes are

```text
Type I: 7e19e67ccc270cb296cec21e23e180271e68af776031b011075c1d5baa8d6651,
Type II: 1265893cb68f5832d20d2c4724032b0c4b0da1624b6aba8d8a38a0f534b68f05.
```

The paired deterministic inventory-log hashes are

```text
Type I: 5d474527b63e2929de1fe8bce80dadc48faee7cd59370d0b70992241b87f3a82,
Type II: 8bf02ea461516d0ad107b35eb9cc448ea912b850b7610b86a2caf12be2cb0f83.
```

At the initial snapshot every stdout file was empty, every candidate was
absent or empty, and no terminal marker existed.  These are candidate
generators, not proof runs.  A model must pass both independent OR verifiers;
an UNSAT report would still require an archived proof-producing rerun and
independent checking in each branch.

## Reverse pin-load v2 correction and benchmark-guided diversity

The Type-II reverse pin-load theorem was implemented under

```text
K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1
```

after the repaired rank-five prerequisite.  It requires the existing
two-component pin-localization module and, whenever the slack-one component
omits coordinate `b`, enforces

```text
o_b>=59,
h2+h4+h6 <= 3o_b+h1+h3+h5+76,
```

where `o_b` counts occurrences of `b` in the slack-two component.  The
second expression is chain-independent because

```text
y0+y2=462+h1+h3+h5-h2-h4-h6
```

on all three repaired rank-five chains.

Both implementation and independent source audits pass.  The optional
module adds exactly

```text
15,945 variables / 96,149 clauses.
```

The frozen reverse source and remote binary hashes are

```text
3500113db42662e783cb8a4e9d3e247372cad1488f346b8f90b9eb36b55d3e38
  k11_forest_sat_rank5repair_reverse.cpp
4e8fcb98ee268fe8b470b0911cd4262062c0942b7f2d75335298cd8bb555c0aa
  k11_forest_sat_rank5repair_reverse
```

and the real-CaDiCaL build-only result is

```text
3,676,391 variables / 20,175,839 clauses,
build-log SHA-256
e0d720fded3da4bd521398a4f22af5af4fd02dd6e68832966b2a3458750aeecb.
```

After checking that seed 304 had no candidate or terminal marker, its solver
PID `153944` and wrapper `153942` were intentionally retired as incomplete.
They were replaced on CPU 5 by

| branch | seed | wrapper PID | solver PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type II + reverse pin load | 306 | 154995 | 154996 | `type2_reverse_306.log` | `candidate_type2_reverse_306.txt` |

The new process reproduced the exact inventory, had empty stdout and no
candidate, and was live at the initial health check.

A separate 16-run bounded Kissat benchmark compared corrected Type-I facet
versus facet+ridge formulas and Type-II base versus pin-localized formulas at
1,000/5,000 conflicts over two seeds.  All runs returned `UNKNOWN`.

* Ridge improved mean Type-I CPU by 7.7% at 1,000 conflicts but worsened it
  by 4.9% at 5,000 conflicts, with strong seed dependence.
* Type-II pin localization improved mean 5,000-conflict CPU by 13.1% and
  propagation count by 15.3%, with favorable CPU on both seeds.

Accordingly, after confirming seed 303 had no candidate or terminal marker,
Type-I ridge PID `153940` and wrapper `153939` were intentionally retired as
incomplete.  A facet-only diversity seed was launched on CPU 12:

| branch | seed | wrapper PID | solver PID | log | candidate |
|---|---:|---:|---:|---|---|
| Type I + facet, no ridge | 305 | 155091 | 155092 | `type1_facet_305.log` | `candidate_type1_facet_305.txt` |

Its exact inventory is `3,649,035 / 20,038,123`; stdout and candidate were
empty at launch.  The benchmark report and archived raw logs are
`K11_RANK5_REPAIRED_MICROBENCHMARK_20260723.md` and
`scratch/k11_rank5_repaired_microbenchmark_20260723/`.

The resulting four-way portfolio deliberately retains one Type-I ridge,
one Type-I facet-only, one Type-II pin-localized, and one stronger Type-II
reverse-pin formula.  This is formulation diversity, not evidence of SAT or
UNSAT.

## Companion-pin and global-pair update

Two later exact propagation modules were implemented and independently
audited on the common frozen source

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
  k11_forest_sat_newcuts.cpp
bd7c79dd68e82d5045d589be45bd7099afacdd49f7fc10decd9157582b45e392
  k11_forest_sat_newcuts
```

The Type-II companion guard adds the exact conditional rows

```text
b notin OR(C2) => #{i in C1:b in A_i}>=176,
b notin OR(C2) => |C1|+z>=211.
```

It reuses the retained C1 occurrence bank and adds exactly
`10,220/71,628`.  The full reverse-plus-companion build is
`3,686,611/20,247,467`.  Its paired benchmark improved mean CPU by 7.7% at
1,000 conflicts but worsened it by 15.8% at 5,000 conflicts.  It therefore
remains an audited optional module and did not replace either live Type-II
slot.

The Type-I global pair-profile guard encodes

```text
n1+2*n2>=110.
```

It adds exactly `1,864/13,053`.  On the existing facet-plus-ridge stack the
full build is `3,671,659/20,175,646`.  Its paired benchmark improved CPU for
both seeds at both caps; mean 5,000-conflict CPU fell 11.6% and propagations
fell 51.9%.  After checking that the old seed-301 candidate was absent and
its logs contained no terminal marker, solver PID `153935` and wrapper
`153934` were intentionally retired as incomplete.  They were replaced by

| branch | seed | CPU | wrapper PID | solver PID | log | candidate |
|---|---:|---:|---:|---:|---|---|
| Type I + facet + ridge + global pair | 361 | 9 | 157066 | 157067 | `type1_global_361.log` | `candidate_type1_global_361.txt` |

The new process reproduced the exact inventory, had no candidate or terminal
marker, and was CPU-consuming at launch.  The facet-only seed 305 remains
live for diversity.  The theorem notes, implementation audits, benchmark,
and raw logs are

```text
K11_TYPE2_COMPANION_PIN_LOAD.md
K11_TYPE2_COMPANION_PIN_LOAD_IMPLEMENTATION_AUDIT.md
K11_TYPE1_FACE_HIERARCHY_NEXT.md
K11_TYPE1_GLOBAL_PAIR_PROFILE_IMPLEMENTATION_AUDIT.md
K11_NEW_PIN_PAIR_CUTS_MICROBENCHMARK_20260723.md
scratch/k11_newcuts_microbenchmark_20260723/
```

All benchmark runs returned `UNKNOWN`; no mathematical bound changed.  The
four temporary DIMACS files were removed from `/dev/shm` only after their
hashes and all raw logs were archived locally.
