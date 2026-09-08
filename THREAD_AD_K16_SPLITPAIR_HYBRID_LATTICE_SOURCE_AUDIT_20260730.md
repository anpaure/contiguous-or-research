# K16 splitpair occurrence-labelled hybrid lattice: source and scope audit

Date: 2026-07-30  
Lane: AD  
Status: **the fixed-labelled switching theorem and all 23 completed
`c<=16` pair runs are valid; no nontrivial middle-exact hybrid occurs in
those lattices.  Five `c>=21` pairs remain unrun.  The C++ source is not a
fail-closed generic unlabelled theorem without the catalogue-specific repeat
hypothesis proved below.**

## 1. Frozen source and catalogue

Audited source:

`scratch/search_k16_splitpair_hybrid_lattice_20260730.cpp`

SHA-256:

`4fcb1182f8f0c7f7843e33aa779a1777d4f91d35d2e3eee01d97b98a32c0608c`.

It passes

```text
clang++ -std=c++20 -O0 -Wall -Wextra -Wpedantic -fsyntax-only
```

without a diagnostic.

The summary has eleven exact/upper rows, with IDs

```text
151, 152, 155, 156, 162, 178, 229, 231, 233, 234, 282.
```

Exact file hashing gives `151=152`, `155=156`, and `233=234`.  After these
three literal duplicates are collapsed, the declared eight distinct endpoint
IDs are

```text
151, 155, 162, 178, 229, 231, 233, 282.
```

They are therefore a complete set of distinct rows of
`scratch/ad_k16_bad2_splitpair_exact_20260730/summary.tsv` having
`bad=zero=0` and an empty unrestricted-upper-hole field.  The summary is
bound by `manifest.sha256`; the summary SHA-256 recorded there is

`296aaa105dea851d95e5e4e59bb586215b2053aeb777e966e3d18c8a158f26fd`.

The `manifest.sha256` file itself has SHA-256

`32cfd1aa1a126d489238192b6b1a353edce5fa4814bab060b1119b219501eba6`.

The endpoint files have hashes

| ID | SHA-256 |
|---:|---|
| 151 | `a509899b9e331b4c0743b2a814707ea2d899586b35b9aba38605d31ea718b6a3` |
| 155 | `059600a7098beb9c01df1fa36ea973a7d1111591d71ae5e609a2aac6a2d07b4f` |
| 162 | `ad58f4f4f0039e44d811842dfaa65399f81a56f763fa0e4853102331fe80dac4` |
| 178 | `e0b2d3f0d5b68dfb699a36cc771d7412c6ddae2a9a4e57de02fd96276349e9e6` |
| 229 | `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974` |
| 231 | `6dc7a62f632814e09a74b265d2b33737d5a3923cdf4ee71a796b4e149200c78d` |
| 233 | `ab6e72cf98a32efe9b66567ff1908239d291f1488d7d1e21c8d630566c66ef7d` |
| 282 | `e9dfecd67bf34bbc93ae54179d43e942f802e2ea28198d0024dd8c76da07e0f3` |

An independent read-only replay of every endpoint gives, in every case:

```text
length                         12873
rank-eight rows                12873
flat positions                 6320,12869,12871
dynamic capacity               32063
middle replay errors           0
zero maximal envelopes         0
unrestricted upper holes       0
distinct mask multiplicities   12867 once, 3 twice
```

The three doubled values are identically located in all eight endpoints:

```text
4e71 at 6320,6321
cc63 at 12869,12870
ce61 at 12871,12872.
```

Thus every rank-eight mask occurs once, with exactly these three extra flat
copies.

## 2. Exact occurrence-labelled switching theorem

Let `A=(A_i)` and `B=(B_i)` be equal-length words with the same mask
multiset.  For each mask, list its positions increasingly in `A` and in `B`
and match the j-th occurrences.  This defines the permutation `sigma` used
by the program:

\[
B_i=A_{\sigma(i)}.
\tag{2.1}
\]

For a set `S` of physical positions, form

\[
H_i(S)=\begin{cases}B_i,&i\in S,\\A_i,&i\notin S.\end{cases}
\tag{2.2}
\]

Label every occurrence by its position in `A`.  The labels used by (2.2)
are the values of

\[
f_S(i)=\begin{cases}\sigma(i),&i\in S,\\i,&i\notin S.\end{cases}
\tag{2.3}
\]

### Theorem 2.1

`f_S` is a permutation if and only if `S` is a union of nontrivial cycles of
`sigma`, up to irrelevant fixed points.  Consequently the source enumerates
all and only the `2^c` occurrence-labelled hybrids, where `c` is the number
of nontrivial cycles.

### Proof

If a cycle is wholly selected, (2.3) rotates its labels by `sigma`; if it is
unselected, (2.3) is the identity.  Disjoint cycle choices therefore give a
permutation.

Conversely, suppose `i` is selected.  Label `sigma(i)` is then used at
position `i`.  If `sigma(i)` were unselected, the same label would also be
used at position `sigma(i)`.  Hence `sigma(i)` is selected.  Iterating around
the cycle selects the whole cycle.  Applying the same argument to the
complement shows that a cycle containing an unselected position is wholly
unselected.  This proves the claim.  The source's loop over all bit masks
`0 <= s < 2^c` is therefore complete; its `c<63` guard makes the unsigned
shift defined, and in the audited scope `c<=16`.  QED.

For subset zero, the materialized word is literally `A`.  When all cycles
are selected, every nonfixed position receives `B_i`; at a fixed position
`B_i=A_{sigma(i)}=A_i`.  Thus the full subset is literally `B`.  Reversing
the ordered pair replaces `sigma` by its inverse, which has the same cycle
supports, so one orientation per unordered endpoint pair is WLOG.

## 3. Unlabelled completeness: exact surviving scope

The generic source comment that the fixed `2^c` lattice is complete from
multiset equality alone is too broad.  With repeated values, a balanced
unlabelled switch can recombine occurrence labels across two cycles.  A
four-position counterexample is

```text
A = a,a,c,b
B = b,c,a,a.
```

Increasing-occurrence matching gives the single cycle `(0,3,1,2)`, but
switching only positions `{0,3}` gives `b,a,c,a`, which has the same multiset
and is neither endpoint.  It is absent from the fixed one-cycle lattice.

The actual eight-endpoint catalogue escapes this counterexample exactly.
Every nondoubled mask is unique.  Every doubled mask has both occurrences at
the same two physical positions in every endpoint, so those positions are
fixed points of `sigma` and `A_i=B_i`.  Any unlabelled multiset-preserving
positionwise `A/B` hybrid can therefore be labelled uniquely off these six
irrelevant fixed positions.  Theorem 2.1 then forces its nontrivial switch
set to be a union of the source cycles.

Hence the source's `2^c` family is also complete for **unlabelled**
multiset-preserving `A/B` hybrids for these authenticated inputs.  This is a
catalogue theorem, not a generic consequence checked by the binary.

## 4. Middle and upper replay

For a candidate target chronology `T`, `geometry` starts at depth three and
decrements immediately after every adjacent equality.  In the authenticated
catalogue all hybrids preserve the three fixed doubled pairs and contain
every other mask once, so their depth schedule is necessarily the common
schedule.

It then computes

\[
P_p=\bigcap_{i\le p\le i+d_i}T_i
\tag{4.1}
\]

and checks both `P_p != 0` and

\[
T_i=\bigvee_{p=i}^{i+d_i}P_p
\tag{4.2}
\]

for every row.  Thus `g.exact` is an exact maximal-envelope middle replay,
not a proxy.

For upper coverage, `upper_missing` maintains the chain of distinct ORs of
all suffixes ending at the current row.  Appending `x` maps the preceding
chain to `x` and `old OR x`; deletion of consecutive duplicates is exact
because the chain is inclusion-monotone.  Marking every resulting mask of
rank greater than eight and comparing against all such masks therefore tests
all literal upper intervals at all upper ranks.

No lower compiler Hall condition is tested by this program.  A positive
output would still require the intended external Hall replay.

## 5. Complete pair decomposition

Independent reconstruction from the local endpoint files gives:

| pair | `c` | nontrivial cycle lengths | status |
|---|---:|---|---|
| 151-155 | 2 | 2606,51 | exhausted |
| 151-162 | 1 | 2606 | exhausted |
| 151-178 | 3 | 2389,718,1664 | exhausted |
| 151-229 | 11 | 27,140x9,1319 | exhausted |
| 151-231 | 5 | 1361,415x3,259 | exhausted |
| 151-233 | 2 | 2606,201 | exhausted |
| 151-282 | 26 | 1054,110x6,55,80x9,78,39,280x6,278 | **not run** |
| 155-162 | 6 | 521x5,51 | exhausted |
| 155-178 | 9 | 1548,446,654,447,101,207x4 | exhausted |
| 155-229 | 13 | 1156,136x8,68,134x2,51 | exhausted |
| 155-231 | 4 | 1660,53,103x2 | exhausted |
| 155-233 | 3 | 891,769,151 | exhausted |
| 155-282 | 23 | 118x5,116x2,78,76x10,838,280x4 | **not run** |
| 162-178 | 3 | 2897,1534,339 | exhausted |
| 162-229 | 15 | 4x12,2,1949,606 | exhausted |
| 162-231 | 3 | 1129,1476,259 | exhausted |
| 162-233 | 2 | 2605,201 | exhausted |
| 162-282 | 12 | 2029,222,118x3,280x6,278 | exhausted |
| 178-229 | 6 | 2611,460,1072,346,128x2 | exhausted |
| 178-231 | 4 | 1347,1288,926,463 | exhausted |
| 178-233 | 3 | 1336,1336,1352 | exhausted |
| 178-282 | 24 | 456x2,1222,934,58x3,56x12,22x5 | **not run** |
| 229-231 | 16 | 178x14,88,259 | exhausted |
| 229-233 | 9 | 98x5,49,1001,1040,201 | exhausted |
| 229-282 | 11 | 760,608,606x2,280x6,278 | exhausted |
| 231-233 | 4 | 1010,11,124x2 | exhausted |
| 231-282 | 26 | 56,54x14,27,165,328x2,276x3,284,282x3 | **not run** |
| 233-282 | 21 | 12x11,140x5,10x2,1677,141,140 | **not run** |

The 23 pairs with `c<=16` contain exactly 115,974 labelled subsets.  The
remote records report exactly two middle-exact and two upper-complete rows
per pair.  These are the two endpoints, leaving all 115,928 nonendpoint
subsets middle-inexact.

The five omitted pairs have cycle counts `26,23,24,26,21`; there is no pair
with `17<=c<=20`.  They remain UNKNOWN and are not covered by the no-go.

## 6. Remote artifact audit

Read-only inspection used

`/home/amodo/or15/work/root_k16_splitpair_hybrid_lattice_20260730`.

The remote source hash equals the local source hash.  The remote binary hash
is

`fd223cb795b53ae1abcb6b7f2cea2a1ba802d2d2747d9f0702fccd647b55136d`.

All eight remote endpoint hashes equal the local hashes in Section 1.  For
every one of the 23 completed run directories:

1. `exit` contains zero;
2. `stderr` is empty;
3. `stdout` reports `total=2^c exact=2 upper=2`;
4. `result.tsv` has exactly a header and two endpoint rows;
5. exactly two output files exist;
6. `pass_0.targets` hashes to endpoint `A` and `pass_1.targets` hashes to
   endpoint `B`.

The current `run_batch.sh` hash is

`37131c859b44106989a9d0caff237af76f243bd965e748798d0b02033be0dcbc`.

It lists only twenty pairs.  The completed directories `run_151_229`,
`run_162_229`, and `run_229_231` are additional runs and are not covered by
that batch script or its aggregate stdout.  Their individual outputs have
the same source-consistent form and endpoint-hash checks, but the package has
no frozen compiler command/build log cryptographically tying the binary hash
to the source hash.  Thus the mathematical/source audit is exact, while the
remote execution provenance is source-consistent rather than fully
reproducible from a frozen build manifest.

## 7. Fail-closed audit and corrections

The positive and negative mathematical conclusions above survive, but the
generic executable has the following scope defects:

1. It does not check input hashes, length 12,873, rank-eight rows, parent
   middle exactness, parent upper completeness, or the fixed-repeat
   hypothesis needed for unlabelled completeness.  These were established
   externally for the eight files only.
2. Invalid depth schedules and depth overruns return `exact=false` with
   `bad=zero=0`.  Therefore `bestbad=0` and a table row with zero bad/zero can
   be diagnostically false even though it cannot increment `exact` or emit a
   pass.  This does not occur in the authenticated catalogue because the
   repeat positions are fixed.
3. The table has no explicit `exact` column, and nonexact rows do not receive
   upper replay; their default `holes=0` must not be read as upper complete.
4. Output and table streams are not checked after open/write, output paths
   are not required fresh, and stale `pass_*` files are not rejected.
5. The exit status is zero whenever any upper pass exists.  Since both
   endpoints are guaranteed passes, exit zero does **not** mean a new hybrid
   was found.  The decisive record is `exact=2 upper=2` plus endpoint hashes.
6. The current runner is not itself a manifest of all 23 completed runs, and
   the binary/source build relation is not frozen.

These are provenance and generic-scope defects, not false positives in the
23 audited results: every emitted file was independently identified as an
authenticated endpoint, and the exact counter proves there was no other
middle-exact member.

## 8. Exact conclusion

For each of the 23 unordered endpoint pairs whose occurrence permutation has
at most sixteen nontrivial cycles, every positionwise `A/B` hybrid preserving
the complete target multiset belongs to the enumerated fixed-labelled cube.
Among its 115,974 members across all pairs, the only middle-exact members are
the 46 endpoint occurrences, all upper complete.  No nontrivial hybrid from
these cubes can advance the compiler/Hall problem.

Nothing here excludes a hybrid for one of the five `c>=21` pairs, a mixture
of three or more endpoints, a hybrid that does not choose positionwise
between one fixed pair, or a construction that changes the target multiset.
