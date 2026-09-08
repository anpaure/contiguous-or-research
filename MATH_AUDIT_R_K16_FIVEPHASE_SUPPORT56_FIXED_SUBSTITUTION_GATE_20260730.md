# K16 five-phase one-hole basin: support-56 and blocker-40 exact gates

Date: 2026-07-30

Status: exact source-relative finite models and independently checked finite
supports.  The blocker-40 budget-two class is now certified UNSAT by a checked
DRAT proof.  The broader support-56 budget-two run has only unchecked solver
evidence.  No length-12,874 word and no global radius-four no-go are claimed.

## 1. Frozen source

The input is

```text
scratch/k16_fivephase_rex_hole20067.word
SHA-256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5
length 12874
```

An independent ending-OR recurrence visits all literal interval labels and
finds exactly one missing nonzero mask,

```text
20067 = 0x4e63.
```

The maximum number of distinct ending-OR states is 12, and the exact
multiplicity sum is `12874*12875/2`, so no interval mass is omitted.

## 2. Exact Hamming-one provider support

For each bit `b=0,...,15`, the audit enumerates every physical interval whose
OR is `0x4e63 XOR (1<<b)`.  There are 20 such provider intervals in total.
Their physical-position union has exactly 55 elements and agrees literally
with

```text
scratch/root_k16_fivephase_hole20067_hamming1_support55_20260730.positions.txt.
SHA-256 16bf51eb5a7351cbc86346378b68233fdffbf8957811871b40e4ebf6545c7502.
```

This establishes completeness of that file for its stated Hamming-one
meaning.  It does **not** establish that every multi-cell repair of `0x4e63`
must touch that set.

The 55-position set omits position 12873.  This omission is decisive: the
source cell there is `0x287d`, and a complete enumeration of every nonzero
submask replacement capable of installing `0x4e63` at this position finds
exactly 128 rows.  Every one has the sole collateral debt `0x287d`.  Thus the
finite exact search support used below is

```text
E = support55 union {12873},  |E|=56,
scratch/r_k16_fivephase_hole20067_support56_20260730.positions.txt.
SHA-256 b29227147d0d13895212a0e5711d8cc74209378818d8608adaf71d1a8b33d0ab.
```

The independent support/portal checker is

```text
scratch/audit_r_k16_fivephase_hole20067_support56_20260730.py
SHA-256 2e678d63c412f1b735377ec229296d6e321e65cb9df9d4fdf62f734ca849453d
```

and its output is

```text
scratch/r_k16_fivephase_hole20067_support56_20260730.audit.json
SHA-256 0170831cc6eb89879f9b3adf6f58037d4fb64dd44b953ae73d767b7f522dcb83
status PASS_EXACT_SUPPORT_AND_PORTAL_AUDIT.
```

## 3. Exact support-relative CNF theorem

Fix the cells outside `E`.  Let every cell in `E` range independently over
all nonzero 16-bit masks, and require exactly `b` of the 56 values to differ
from the source.

### Theorem 3.1

The CNF emitted by

```text
scratch/k16_dynamic_fixed_substitution_cnf_20260730.cpp
SHA-256 38f933b9d79cc345cb42e902c3338cbfb9b38858fe2e07c97ac95417ae30c0fa
```

is satisfiable if and only if there is a universal length-12,874 word in this
fixed-support, exact-budget-`b` class.

### Proof

Deleting the 56 editable positions partitions the frozen complement into 57
fixed runs.  Every interval either lies wholly inside one fixed run, or its
intersection with the ordered editable positions is a nonempty consecutive
block `[i,j]`.  In the second case its fixed part is exactly:

1. a suffix of the fixed run immediately before position `i`;
2. every intervening fixed run in full; and
3. a prefix of the fixed run immediately after position `j`.

The emitter enumerates precisely the distinct ORs of these fixed parts.  For
a target `t` and a fixed base `a subseteq t`, a witness literal imposes:

* no editable cell in `[i,j]` uses a bit outside `t`; and
* their union supplies every bit in `t` absent from `a`.

These conditions are necessary and sufficient for the corresponding literal
interval to have OR exactly `t`.  Taking their disjunction covers every
interval meeting `E`; targets already witnessed inside fixed runs require no
clause.  Hence all 65,535 target clauses are equivalent to literal
universality.

Each editable cell has a nonzero clause.  Its change variable is equivalent,
in both directions, to the OR of the sixteen source-bit differences.  The
equivalence-complete prefix counter asserts exactly `b` such change variables.
This proves both implications.  QED.

The independent finite logic audit
`scratch/audit_k16_dynamic_fixed_substitution_encoding_logic_20260730.py`
checks the fixed-run decomposition, dominated-need reduction, target
equivalence, change equivalence, and exact cardinality recurrence on all
small test assignments in its declared domain.

## 4. Budget-two preflight

The H100-only emitter was run on one nice'd CPU under a 2 GiB hard
address-space cap.  It did not invoke a SAT solver.  The exact instance has:

```text
editable positions                 56
fixed runs                         57
targets already fixed-covered   65221
repair targets                    314
editable blocks                  1596
fixed interval bases             3010   (maximum 42 per block)
witness terms                   51182   (maximum 163 per target)
variables                       52299
clauses                       1355933
literals                      3253396
CNF size                         20 MiB
map size                        1.3 MiB
emitter peak RSS                3.5 MiB
```

The copied preflight statistics are
`scratch/r_k16_fivephase_support56_b2_20260730.stats.json`, SHA-256
`94a3b30a93e4e854130dd48436375073598a462ba471ca2ce453720ea9596d34`.

Frozen remote hashes are:

```text
CNF   de673c90ed5713263c3d60546ee2c7d9e0607641a3b463b79e1f58804e3f75a6
map   8662d5199352f3023e7e1dbb56769aea1351ebd152926e11a09183d5d0322514
stats 94a3b30a93e4e854130dd48436375073598a462ba471ca2ce453720ea9596d34
```

The budget-three instance has the identical target/witness core; only the
small exact-cardinality counter changes.

## 5. Safe solve and promotion contract for support 56

Because the H100 load was above 90 and the five-phase beam was still active,
the solver launch was deliberately deferred.  The sharper two-portal
blocker-40 instance in Section 6 now has priority over this source-level
support-56 instance.

Any SAT assignment must be decoded by

```text
scratch/decode_verify_k16_dynamic_fixed_substitution_20260730.py
```

with `--full-quadratic`.  That decoder ignores all witness variables,
checks every mapped value and exact change indicator, materializes the
literal word, and visits all `12874*12875/2` intervals.  The repository word
verifier is then a second required replay.  Fresh output paths are mandatory.

An UNSAT result without a checked proof is exact solver evidence only for the
fixed support `E` and stated budget.  It is not a global radius theorem, since
support-56 completeness is proved only for the Hamming-one provider bank plus
the sharp portal site.

## 6. Two fixed portals and the exact blocker-40 radius-four gate

Apply the following two substitutions to the frozen source:

```text
p12873: 0x287d -> 0x4e63,
p6439:  0xa069 -> 0x206d.
```

The first installs the original missing target `0x4e63` and leaves the sole
hole `0x287d`.  The second restores `0x287d` and leaves the sole hole

```text
A = 43129 = 0xa879.
```

The resulting literal word is

```text
scratch/r_k16_fivephase_blocker_a879_state_20260730.word
SHA-256 aee4b0d00670e887e75d642ba186f0c04e8f279b82253c34d8541ae26dd0af70.
```

It is obtained from
`scratch/k16_fivephase_canonical_p12873_4e63_onehole.word`, SHA-256
`813063b9813d956ebc85729aeab180171062ad0f48fb0220cd71defe2180830a`,
by the hash-pinned materializer
`scratch/materialize_r_k16_fivephase_blocker_state_20260730.cpp`, SHA-256
`220c66e0ca88a781f1191cd1b7b4e474153e5a6bf482bb3d066a2101a12a4ed4`.

For each of the sixteen Hamming-one neighbours of `A`, enumerate every
literal provider interval in this blocker state.  There are exactly 17 such
intervals and their physical-position union has size 41.  Position 6439 is
in that union but is already fixed as the second portal.  Position 12873 is
not in the union.  Deleting position 6439 leaves the 40-position catalogue

```text
scratch/r_k16_fivephase_blocker_a879_support40_20260730.positions.txt
SHA-256 54073bb6217ca948e354c651ea1489be71370c3464c5f09748c873aefaae13f0.
```

This is a complete physical support statement for the specified sixteen
neighbour-provider rows.  It is not a theorem that every arbitrary two-edit
repair of `A` must meet this support.

### Theorem 6.1 (exact catalogue-relative radius-four equivalence)

Fix both portal positions above and every position outside the displayed
40-position set.  Let each of the 40 remaining cells range independently over
all nonzero 16-bit masks, and require exactly two to differ from the blocker
state.  The emitted CNF `blocker40_b2.cnf` is satisfiable if and only if the
resulting length-12,874 literal word is universal.

Every satisfying assignment differs from the original source in exactly four
positions: the two fixed portals and the two support-40 substitutions.

### Proof

The fixed portals are absent from the editable set.  Deleting the 40 editable
positions partitions the blocker state into 41 fixed runs.  The interval
decomposition and exact witness argument in Theorem 3.1 therefore apply
verbatim with this blocker state as the source.  The exact-cardinality counter
requires precisely two differences from that state.  Since the support avoids
the two portal positions, these differences are disjoint from the two fixed
source-to-blocker changes.  This proves both claims.  QED.

The exact preflight dimensions are:

```text
editable positions                 40
fixed runs                         41
targets already fixed-covered   65249
repair targets                    286
editable blocks                   820
fixed interval bases             1910   (maximum 44 per block)
witness terms                   24412   (maximum 88 per target)
variables                       25209
clauses                        527940
literals                      1240131
CNF bytes                     7652772
map bytes                      629817
emitter peak RSS                3584 KiB
```

The copied statistics are
`scratch/r_k16_fivephase_blocker40_b2_20260730.stats.json`, SHA-256
`910678b1a153028dfa496355f2eece6f9454a2fd8f73ddc26a73673b75d42a9f`.
The frozen remote hashes are

```text
CNF   1306bc47a3f3fdcdadbfb87a201fa48c758b876bf1fae5d95b591c464874f6db
map   e17a374f77d2818497cf76788b47cfb39293548bd6c77ef68cb2bbb5e9a73836
stats 910678b1a153028dfa496355f2eece6f9454a2fd8f73ddc26a73673b75d42a9f
```

The complete fail-closed reproduction and promotion contract is

```text
scratch/r_k16_fivephase_blocker40_b2_20260730.manifest.json
SHA-256 f6be395c0536b7e873a81eac167236df5562a298bb5aeaa13aa065ed46c96dd2.
```

The budget-one continuation is not scheduled: the independently frozen
global sharp-fibre census
`scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json`,
SHA-256
`b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629`,
checks all 128 sharp terminal first edits, all 16 sharp off-tail second edits,
and every third one-cell substitution.  Its 2,048 intermediate states all
have minimum residual debt one and it has zero universal rows.  Thus a
support-40 budget-one solve would duplicate an already stronger exact census.

### Theorem 6.2 (certified support-40 exclusion)

The finite class in Theorem 6.1 is empty.

### Proof

The locally retained instance and proof are

```text
CNF   scratch/r_k16_fivephase_blocker40_b2_20260730.cnf
      SHA-256 1306bc47a3f3fdcdadbfb87a201fa48c758b876bf1fae5d95b591c464874f6db
map   scratch/r_k16_fivephase_blocker40_b2_20260730.map
      SHA-256 e17a374f77d2818497cf76788b47cfb39293548bd6c77ef68cb2bbb5e9a73836
DRAT  scratch/r_k16_fivephase_blocker40_b2_20260730.drat
      SHA-256 f4587e3ac5dd06ebd66e25fb87c03ce9d17d705304bac378f29a61c928367e7b
```

Hash-pinned Kissat returned literal `s UNSATISFIABLE` with exit status 20 in
4.82 seconds, using 32,264 KiB peak RSS.  The independent checker
`drat-trim`, SHA-256
`92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a`,
then checked exactly that CNF/proof pair, exited zero, and printed literal
`s VERIFIED`.  It used 204.933 seconds of verification time and 98,816 KiB
peak RSS.  Its backward core contains 41,372 clauses and 58,689 of 355,425
lemmas, with 13,267,078 resolution steps and 32,946 RAT lemmas.  Thus the CNF
is unsatisfiable.  The exact equivalence in Theorem 6.1 proves the claimed
finite exclusion.  QED.

The self-contained result ledger is

```text
scratch/r_k16_fivephase_blocker40_b2_certified_unsat_20260730.audit.json
SHA-256 d58fb6c9693dddb33067d102ebaa99fa131bb7524d2206c48d92a8d207c2982b.
```

## 7. Sharp proved boundary and next enlargement

Combining the global sharp-fibre radius-three census with Theorem 6.2 gives:

1. no one-cell continuation after the two fixed portals can be universal;
2. no two-cell continuation supported on the Hamming-neighbour catalogue can
   be universal.

The second statement is deliberately catalogue-relative.  It does not show
that every arbitrary two-edit witness for `A` uses support 40.  The next exact
enlargement must enumerate all intervals that can become `A` after at most two
cell substitutions.  Necessarily every unchanged cell of such an interval is
a submask of `A`, so the source interval contains at most two cells carrying
bits outside `A`.  After choosing the `A`-witness edit sites, a second edit may
also lie outside that witness solely to repair collateral debt.  Both cases
must be retained in any complete provider-pair model.

## 8. Support-56 budget-two run is not certified

A separate hash-pinned Kissat run on the broader source-level support-56
instance printed `s UNSATISFIABLE` and emitted a 51,855,952-byte DRAT file,
SHA-256
`eda96cfe6f7a1987a87ca0264da1f9f1199d62c7923f5a6e25efe46289be62df`.
The run took 34.84 seconds and 70,908 KiB peak RSS.  Its first `drat-trim`
attempt was killed by signal 9 after 279.83 CPU seconds.  Both checker output
streams are empty and there is no literal `VERIFIED` line.  Therefore this is
solver evidence only, not a certified theorem.

The fail-closed ledger is

```text
scratch/r_k16_fivephase_support56_b2_uncertified_unsat_20260730.audit.json
SHA-256 9fd2aa2486060c984fe97b3b0ff603371558859f5b9ba060965df283b70a7bfc.
```

No rerun is authorized while the shared host guard fails.  Even a later
certificate would exclude only the frozen support-56 budget-two class, not
arbitrary radius-two repairs of the source.
