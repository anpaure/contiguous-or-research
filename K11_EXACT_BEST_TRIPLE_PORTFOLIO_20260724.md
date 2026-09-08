# Exact globally ranked three-replacement portfolio for `k=11`

Date: 2026-07-24

## Scope

This is the next launchable exact neighborhood after a completed arbitrary
two-replacement screen of a 476-entry one-hole seed.  The runner accepts either
an effective 476-entry seed or the 477-entry canonical file whose last token is
to be dropped.  It does **not** encode all

\[
\binom{476}{3}=17,861,900
\]

position triples.  It ranks all of them exactly by the number of targets whose
old witnesses are all hit, removes any previously certified case list, and
passes the best requested triples to the already audited fixed-edit SAT
encoding.  For every selected triple, all \(2047^3\) nonzero replacement-value
assignments are represented exactly by the CNF.

Sources:

```text
scratch/k11_select_best_triples_exact.cpp
scratch/audit_k11_select_best_triples_exact.py
scratch/run_k11_best_triple_portfolio.sh
```

## Exact position score

For \(E=\{p<q<r\}\), an old witness interval avoids \(E\) iff it lies wholly
in one of

\[
[0,p-1],\quad[p+1,q-1],\quad[q+1,r-1],\quad[r+1,n-1].
\]

The selector precomputes, for every segment \([a,b]\), the 2,048-bit set
\(C[a,b]\) of OR values realized by intervals wholly inside that segment.
The exact repair family is therefore

\[
\mathcal R(E)=
[2047]\setminus
\bigl(C[0,p-1]\cup C[p+1,q-1]\cup C[q+1,r-1]\cup C[r+1,n-1]\bigr).
\]

The primary score is \(|\mathcal R(E)|\).  The deterministic tie-break is the
sum, over the three positions, of the number of unique old witnesses that the
position meets.  The selector retains the globally smallest requested tuples

```text
(repair size, unique-witness load, p, q, r).
```

This is a strictly broader selection rule than the earlier hole-interval beam:
every one of the 17,861,900 triples is scored before the heap is truncated.

The segment ledgers take about 58 MiB at length 476.  Triple ranking performs
about

\[
32\binom{476}{3}=571,580,800
\]

64-bit merge/popcount iterations and retains only `TOP` heap records.

## Exact value search

For each retained triple, `k11_fixed_edit_neighborhood_cnf.cpp` uses the
consecutive-edit-block lemma.  A changed interval meets one of only six blocks

```text
p, q, r, pq, qr, pqr
```

(the nonconsecutive `pr` category is impossible for a contiguous interval).
For each repair target it retains the inclusion-minimal fixed-base need masks.
The resulting case CNF is satisfiable iff some assignment of three nonzero
11-bit values at the named positions makes the whole word universal.  Values
may equal their old values, so the formula itself searches “at most three.”
The global two-replacement no-go means any satisfying model must in fact alter
all three positions.

SAT is accepted only after the independent quadratic decoder plus both C++
verifiers accept the 476-entry candidate.  In `certify` mode, UNSAT is accepted
only after `drat-trim` exits zero and prints `s VERIFIED`.

## Recommended first launch

For the canonical prefix, use the 1,471 certified radius-three cases as
`EXCLUDE` and request the next 4,096 global triples.  On a host where the
sources and tools are in the same directory, the command is of the form

```bash
scratch/run_k11_best_triple_portfolio.sh \
  best3_next4096 5 k11_completed_477.txt r3.cases \
  search 911 1800 7200 4096 /root/k11_best_triples_20260724
```

Run `search` first for candidate value.  A negative search-only result can be
repeated with a fresh tag and `certify` to produce and check a DRAT proof.
Passing `-` instead of `r3.cases` is valid but needlessly rechecks the already
closed 1,471 sets on the canonical prefix.  For a different 476-entry seed,
pass `-` unless it has its own certified exclusion manifest.

## Expected cost relative to the direct pair solver

The exhaustive direct pair solver checked

```text
113,050 * 2047^2 = 473,703,127,450
```

value pairs in 221 seconds in the independent canonical run.

The certified 1,471-case triple SAT batch had 178,494 variables, 1,623,908
clauses and solved UNSAT in 27 seconds.  Linear size extrapolation for 4,096
triple cases is approximately

```text
variables   497,000
clauses   4,520,000
literals  9,945,000
```

before the exact generator reports the actual values.  The corresponding
nominal Cartesian neighborhood contains

```text
4096 * 2047^3 = 35,132,857,643,008
```

value triples, but the SAT encoding shares their 33 primary bits and OR
constraints rather than visiting those assignments.  Based only on the prior
batch, a search-only solve should be on the order of one to a few minutes;
proof checking can cost several additional minutes.  The all-triple ranking
pass is additional, but is a fixed 571.6-million-word scan rather than a
value-assignment loop.

Thus a 4,096-case exact triple portfolio has roughly the same wall-clock class
as one completed global two-replacement seed screen while examining a much
larger nominal value neighborhood.  Exhausting every position triple remains
out of scope: linear extrapolation would require thousands of such batches.

## Independent audit

The Python oracle shares neither the segment-ledger recurrence nor the C++
heap.  It explicitly lists every old witness, tests every position of every
witness against each triple, independently computes unique-witness loads, and
compares the complete sorted retained list including exclusions.

It exhausts every nonzero 2-bit word of lengths three through five and adds
300 seeded random 3/4-bit words:

```text
PASS cases=651 retained_rows=4028 seed=4123921
```

Source hashes at audit time:

```text
6977582f522cd0e8d50f792b372984b02fef159e0849d4d28c9e5305c8a3b793  scratch/k11_select_best_triples_exact.cpp
8116fc827e136d1bc66b93954dbf8cff7e2b50e25daf88f11e513cbaeca0f0cd  scratch/audit_k11_select_best_triples_exact.py
e5c4767d4c622238d5e6f1fe603feedfcbdc2e3f98a190e1a5ed70d64469d1f4  scratch/run_k11_best_triple_portfolio.sh
```

The runner accepts `CXX_STD` (default `c++20`) so the audited sources can also
be built as `c++2a` on the older GCC 9 RunPod image; this changes only the
compiler spelling, not the selector or CNF logic.

## Status rule

- A verified SAT candidate improves the `k=11` upper bound from 477 to 476.
- A proof-checked UNSAT closes exactly the emitted triples.
- A search-only UNSAT, timeout, or unchecked proof changes no mathematical
  bound.
- Even a fully certified 4,096-case batch is a selected-neighborhood theorem,
  not a global length-476 impossibility proof.

## Certified first production batch

The recommended 4,096-case batch has now completed in `certify` mode on the
Purple RunPod.  The selector exhaustively ranked all

\[
\binom{476}{3}=17,861,900
\]

position triples, excluded the 1,471 already-certified radius-three cases,
and retained the globally best 4,096 remaining triples.  Their repair-family
sizes range from 4 through 13.  The exact combined CNF has

```text
variables       296,491
clauses       1,747,206
literals      3,781,832
repair rows      47,594
```

Kissat returned UNSAT.  `drat-trim` parsed the complete proof, detected the
empty clause, backward-checked a core containing 124,055 of 789,843 lemmas,
and terminated with

```text
s VERIFIED
DRAT_TRIM_EXIT:0
```

Thus all

\[
4096\cdot 2047^3=35,132,857,643,008
\]

replacement-value assignments represented by these selected triples are
formally excluded.  This is disjoint from the previously certified 1,471
position triples but remains a selected neighborhood, so the global bound
`465 <= nu(11) <= 477` is unchanged.

Certificate hashes:

```text
ab1dc514edde0471fc59e867d1444adb0a1f27164de0b4dec629563d44638d2c  cases
a8742e09bf36d7c17f3ef729eb5ad14d633980c23d475406249ea2491e618c83  CNF
2dfafec4d508f4e6dee9e2411a98b946ff48e1f17c21e7d7b2755d26c6113924  map
335e3294a86056baaba5d5a73dd57eea24f6ccd6adc9f9431717d9b130869806  DRAT
3b99e2d9465a98ff6e9179c123535723ea10938ba06f9db9a1652a689281e1bd  drat-trim log
```

## Certified second production batch

The next disjoint 4,096-case block is also formally closed.  Its exclusion
manifest is the exact union of the 1,471 certified radius-three triples and
the first certified ranked block.  The union has 5,567 distinct valid triples
and no overlap between its two inputs.  Its SHA-256 is

```text
f9843aa0e7ce86e5bb90d9248f24eacc2a1fdba4678d119050d70aafae719983
```

The selector again scored all 17,861,900 position triples, excluded precisely
those 5,567 positions, and retained the next 4,096.  Their repair-family sizes
range from 13 through 14.  The formula has

```text
variables       318,485
clauses       1,978,010
literals      4,257,078
repair rows      54,894
```

The search pass and the fresh certificate pass generated byte-identical case,
CNF, and map files.  Kissat returned UNSAT in both passes.  For the certificate
pass, `drat-trim` read the 31,700,531-byte proof, detected the empty clause,
and backward-checked a core containing 114,103 of 795,604 lemmas using 543,487
resolution steps.  It terminated after 1,551.263 seconds with

```text
s VERIFIED
DRAT_TRIM_EXIT:0
```

An additional exact scope audit regenerated the globally best 8,192 triples
after excluding only the radius-three family.  Its ordered output is exactly

```text
first certified 4,096 || second certified 4,096
```

with no duplicate position triple.  The fresh 8,192-row manifest has SHA-256

```text
67d3f3ec7d052978c9f3eabbe0ce555f0a94353cc7746d5162ee7efdfe5f2259
```

and the independent local archive audit reports

```text
PASS exact k=11 globally ranked triple scope
radius3=1471 first_ranked=4096 second_ranked=4096
fresh_top8192 == first_ranked || second_ranked
```

The second batch formally excludes another

\[
4096\cdot 2047^3=35,132,857,643,008
\]

replacement assignments.  Across the two globally ranked batches, the exact
count is 70,265,715,286,016.  Including the disjoint 1,471-case radius-three
family, 9,663 position triples and 82,883,008,643,649 represented assignments
are now certificate-excluded around this canonical length-476 seed.

Second-batch certificate hashes:

```text
679a2955581053985c407c0aac70b309930e7024b26ed0c8e81f630717910fd0  cases
a399f738a6749e93539af450fcd0f75b12f9d7a2342a7f2b514b26925c658649  CNF
60f3bf34ec976352b75b4e0ca643af23956568028eb04bf7ac049c60fb9631f1  map
6eddaf202ded51c68728e87b28b065f082585d7142a909c2cde55bf30a18e2c1  DRAT
f5f3286cde975d96d4606da3df8f1f4844c30b7ce18317e80888b860bacf98bf  drat-trim log
```

The compact manifests, scope ledger, checker log, and generator statistics are
archived under `scratch/k11_best_triple_portfolio_20260724/`.  The executable
scope audit is `scratch/audit_k11_best_triple_production_scope.py`, whose
SHA-256 is

```text
f7d06a6d80031bceef5ee137677f00a3af017140bdb3f8fdaaeea212361e9e7d
```

This remains a selected-neighborhood theorem.  It produces no length-476
candidate and does not change the certified bound
`465 <= nu(11) <= 477`.
