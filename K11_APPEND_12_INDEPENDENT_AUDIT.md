# Independent audit of the fixed-prefix 12-entry `k=11` append

## Verdict

**PASS**, with the scope qualifications below.

The 465-entry word

```text
k11_upper549_natural_array.txt
```

misses exactly thirteen nonzero 11-bit masks: twelve masks of rank seven and
one mask of rank eight.  Appending the twelve entries in

```text
k11_append_12.txt
```

gives the 477-entry word `k11_completed_477.txt`, which covers all 2,047
nonzero masks.  The append length 12 is minimal among all extensions of this
**fixed 465-entry prefix**.  Consequently the files prove

```text
nu(11) <= 477,
N(11) <= 478.
```

They do not prove that 477 is the unrestricted optimum.  Combining this audit
with the separately proved rank-slack lower bound gives the current interval

```text
465 <= nu(11) <= 477,
466 <= N(11) <= 478.
```

The validity of the upper bound does not depend on trusting the SAT solver:
the emitted append, its explicit witnesses, and complete coverage are all
directly checkable.

## 1. Data and assembly checks

The input files contain respectively 465, 12, and 477 valid nonzero 11-bit
masks.  After normalizing whitespace, the first 465 entries of
`k11_completed_477.txt` are byte-for-byte the prefix, and its last 12 entries
are byte-for-byte `k11_append_12.txt`.

The append is

```text
243 1216 774 956 941 1468 607 1694 1946 1763 1884 493
```

Independent exhaustive interval enumeration of the prefix gives

```text
length=465 covered=2034 required=2047
missing: 251 493 607 941 956 958 1267 1468 1694 1763 1884 1946 1990
```

The same missing set is returned by an independently compiled implementation
of the distinct-suffix-OR recurrence.  Direct popcounts give rank eight for
958 and rank seven for each of the other twelve masks.

For the completed word, the two independent checks give

```text
exhaustive: length=477 covered=2047 required=2047
suffix OR:  length=477 covered=2047/2047 missing=0
```

The regenerated logs are byte-identical to the stored
`k11_completed_477_exhaustive.log` and `k11_completed_477_suffix.log`.

## 2. Explicit witness audit

All indices below are zero-based.  Regenerating the shortest witness for each
of the thirteen formerly missing targets reproduces
`k11_append_12_witnesses.txt` exactly:

| target | rank | interval | check |
|---:|---:|---:|---|
| 251 | 7 | `[464,465]` | `11 OR 243 = 251` |
| 493 | 7 | `[476,476]` | literal |
| 607 | 7 | `[471,471]` | literal |
| 941 | 7 | `[469,469]` | literal |
| 956 | 7 | `[468,468]` | literal |
| 958 | 8 | `[467,468]` | `774 OR 956 = 958` |
| 1267 | 7 | `[465,466]` | `243 OR 1216 = 1267` |
| 1468 | 7 | `[470,470]` | literal |
| 1694 | 7 | `[472,472]` | literal |
| 1763 | 7 | `[474,474]` | literal |
| 1884 | 7 | `[475,475]` | literal |
| 1946 | 7 | `[473,473]` | literal |
| 1990 | 7 | `[466,467]` | `1216 OR 774 = 1990` |

Thus the twelve rank-seven targets are supplied one per new right endpoint,
and the rank-eight target is supplied without another entry.

`completion_witness_certificate.cpp` is correct for these files.  It
enumerates all intervals, stops extending an interval only after an outside
bit makes equality impossible, and reports a shortest witness.  Its
`cross-seam` label is based only on the left endpoint being before 465; that
is safe here because every requested target was absent from the prefix.  The
documentation should explicitly say that the listed indices are zero-based.

## 3. Minimality for the fixed prefix

Let an arbitrary extension of the fixed prefix have `q` new positions.  Each
of the twelve missing rank-seven masks needs a witnessing interval ending at
a new position: an interval ending inside the old prefix would already have
represented it there.

For one fixed right endpoint, the ORs of suffixes ending there form a chain
under inclusion.  Two distinct rank-seven masks are incomparable, so that
chain contains at most one of the twelve targets.  Hence twelve targets need
twelve distinct new right endpoints and

```text
q >= 12.
```

The displayed extension has `q=12`, so it is shortest for this prefix.  This
argument allows arbitrary appended masks and arbitrary seam-crossing
intervals; it is not restricted to the SAT ansatz.

The related claim about a completion word that must stand alone is also
sound.  If twelve positions covered all twelve rank-seven targets, equality
in the antichain interval argument forces their witnesses to be the twelve
singleton positions.  Of those twelve masks only 956 is contained in 958,
and 956 alone is not 958.  Therefore no interval of that twelve-entry literal
word can have OR 958, so a standalone completion requires thirteen entries.

Neither statement rules out a different universal 11-bit word of length less
than 477; fixed-prefix minimality is strictly weaker than global optimality.

## 4. SAT encoding audit

For the used instance (`k=11`, append length 12, no skipped prefix entry),
`append_completion_sat.cpp` is sound and complete for fixed-prefix extensions
of minimum length.

The bit variables `X(position,bit)` describe the twelve appended entries.
Every possible witness for a missing target is represented in one of two
forms:

1. every appended-only interval `[start,end]`; or
2. every cross-seam interval, represented by the OR of its old-prefix suffix
   and the appended prefix `[0,end]`.

Collapsing old suffixes with the same OR loses no information.  For a selected
witness variable, the clauses forbid every target-external bit throughout the
appended part and require every target bit not already supplied by the fixed
suffix.  Therefore the selected interval OR is exactly the target.  Conversely,
every real witness of either form activates a candidate satisfying those
clauses.

The support clause chooses a witness for every missing target.  Pairwise
at-most-one selector clauses are without loss of generality, since one may
retain any one real witness.  The extra rank-seven endpoint clauses are also
without loss here: there are twelve missing incomparable rank-seven targets
and twelve new endpoints, and no endpoint can witness two of them.  Therefore
any length-12 completion necessarily uses every new endpoint for exactly one
rank-seven target.

The source forbids zero append entries.  This is without loss in this
particular minimum-length instance: deleting a zero from a purported
12-entry extension preserves all nonzero interval ORs and would contradict
the proved lower bound of 12.  As a generic exact-length decision procedure
for nonminimal `q`, that restriction would need this qualification; it does
not affect the result audited here.

The explicit append itself certifies satisfiability of the current formula.
Set the bit variables from its twelve masks, select the thirteen witnesses in
the table, and set every other selector false.  The rank-seven endpoint order
is

```text
251, 1267, 1990, 956, 941, 1468,
607, 1694, 1946, 1763, 1884, 493.
```

Every formula family is then satisfied.  No SAT model, DRAT proof, or solver
log is required for the constructive upper-bound certificate.  Solver output
alone would not prove an UNSAT claim, but no UNSAT claim is being made here.

## 5. Independent verifier audit

`verify_or_array.cpp` exhaustively enumerates every physical interval and is
correct on the audited valid inputs.  `verify_or_suffix.cpp` uses the standard
recurrence

```text
new suffix ORs = {x} union {old OR x : old in previous suffix ORs},
```

deduplicates the resulting values, and is an independent complete coverage
check.  Both accept the 477-entry word.

## 6. SHA-256 inventory

```text
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd  k11_upper549_natural_array.txt
ba44a89403c6b402fb6c9b48cd8a1274dd716cd56885af710db8f091e8ee6989  k11_append_12.txt
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
099ec7dbe7f706f84645592faa17bd9f436d4cbaff9c8cda7b0031ae1e023012  k11_append_12_witnesses.txt
852247ff77a69219b63eabdf83edce3411a999473e95414ec6f650aaa3e934b2  append_completion_sat.cpp
22978c314e158f1256524264402ed83553e6c34eaf758ca612a14d733e6d7456  completion_witness_certificate.cpp
2ef221f819cc6df5eea81aebcb194a1ff76bf0229c47333b3caa367c01df80c4  verify_or_array.cpp
7bd7892532882e31c828e750c1ec960029f0571cd11584b897240c2a051fdbaa  verify_or_suffix.cpp
ae2aa7d6fd67da00ce33452f19fa9375b7189a3812f885080bc38641ec0c8a23  k11_completed_477_exhaustive.log
cb2c0650d53926e3327d36c1a50cec8e8783194349ce309aa9ae9f955b76d741  k11_completed_477_suffix.log
```

The source hash identifies the current source, which contains later optional
`APPEND_SKIP_INDEX`, DIMACS, and proof-trace support.  The direct certificate
above verifies the 12-entry no-skip case independently of how the original
solver process was launched.

## 7. Stale-document and artifact audit

The following current-status references predate this improvement and should
be updated:

- `PARTIAL_COMPLETION_FOREST.md`, section 4, still reports the old 478-entry
  `k=11` completion and lists hashes for `k11_completed_best.txt` and
  `k11_completion_best.txt`.
- `K11_INTEGRATED_SEARCH.md` still states `nu(11)<=478` and `N(11)<=479`.
- `MATHEMATICAL_HANDOFF.md` still contains the old 479 full-array upper bound,
  the old 478 nonzero completion, and the corresponding generated-length
  table entries.
- `k11_completed_best.txt` and `k11_completion_best.txt` still name the old
  478/13-entry certificate.  They are valid historical artifacts but the
  suffix `best` is now misleading.
- `PARTIAL_COMPLETION_FOREST_AUDIT.md` correctly audits the earlier
  478-entry forest/literal completion, but it is superseded as the current
  `k=11` upper-bound audit and should be labeled historical if retained.

`PARTIAL_COMPLETION_FOREST.md`, section 2, already states the new 477-entry
result correctly.  `construct_or_array.cpp` already references
`k11_completed_477.inc`, but generator-wide rebuilding and verification are
outside the scope of this certificate audit.

## Final conclusion

The new append is a fully checkable and genuine one-entry improvement:

```text
fixed prefix:             465 entries, 13 masks missing
shortest append:           12 entries
completed nonzero word:   477 entries, all 2,047 masks covered
```

All mathematical, data, witness, coverage, and used-instance SAT-encoding
claims pass.  The only findings are scope qualifications and stale references
to the superseded 478-entry completion.
