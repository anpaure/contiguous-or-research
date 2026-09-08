# AD audit: K16 split-pair hybrid-lattice artifact

Date: 2026-07-30  
Status: **PASS for the stated canonical occurrence-pairing lattices; five
high-cycle lattices remain unenumerated; no solver-free residence certificate
is present in the package**

Subsequent result: the five high-cycle lattices are now closed by the
polynomial run-implication certificate independently audited in
`THREAD_AD_K16_SPLITPAIR_HYBRID_RUN_IMPLICATIONS_INDEPENDENT_AUDIT_20260730.md`.
References below to an open/conditional high-cycle claim describe only the
older exhaustive package audited here.

## 1. Frozen scope

The audited remote package is

```text
/home/amodo/or15/work/root_k16_splitpair_hybrid_lattice_20260730
```

and the locally visible source is

```text
scratch/search_k16_splitpair_hybrid_lattice_20260730.cpp
```

The eight input rows have length 12,873 and IDs

```text
151 155 162 178 229 231 233 282.
```

They have the same multiset: the 12,870 rank-eight masks occur once, except
`4e71`, `cc63`, and `ce61`, which occur twice.  The common adjacent repeat
pairs are at zero-based positions

```text
6320/6321 = 4e71,
12869/12870 = cc63,
12871/12872 = ce61.
```

The executable uses the canonical increasing-occurrence pairing.  For these
eight frozen endpoints, that canonical cycle lattice is in fact WLOG among
all pointwise choices `q_p in {A_p,B_p}` that preserve the target multiset;
the proof is in Section 2.  It is not WLOG for operations which introduce a
third row value or do not preserve the multiset.

## 2. Exact construction and proof of multiset preservation

For inputs `A,B`, let

```text
src[position of the j-th occurrence of x in B]
    = position of the j-th occurrence of x in A.
```

Equality of the two multiplicity vectors makes `src` a permutation of all
12,873 positions.  Moreover

\[
 B_p=A_{\operatorname{src}(p)}.                    \tag{2.1}
\]

On each nontrivial cycle of `src`, the program chooses either all `A` values
or all `B` values.  Choosing `B` on a whole cycle merely cyclically permutes
the `A` values on that cycle by (2.1).  Therefore every one of the `2^c`
cycle selections has exactly the original target multiset.  Fixed points
need no selector because they cannot change the value.

Conversely, let `s_p` record whether a pointwise hybrid takes `B_p` rather
than `A_p`.  Every mask except the three displayed duplicates occurs exactly
once in each endpoint.  For such a unique mask `x`, multiset preservation
gives

\[
1-s_{p_A(x)}+s_{p_B(x)}=1,
\]

so `s_(p_A(x))=s_(p_B(x))`.  Since
`src(p_B(x))=p_A(x)`, these equalities force `s` to be constant around each
nontrivial canonical cycle.  The three duplicate masks occur at the same
fixed positions in both endpoints, where `A_p=B_p`; changing their pairing
can add only value-inert position cycles.  Therefore the canonical `2^c`
lattice is complete for every frozen-catalogue pointwise `A/B` hybrid that
preserves the multiset.

The fixed-duplicate hypothesis is essential to that WLOG conclusion.  For
generic sources

```text
A = (x,x,y,y),    B = (y,y,x,x),
```

the order pairing has cycles `(1 3)` and `(2 4)` (using one-based
positions), while changing positions `{1,4}` is also multiset-preserving and
is not a union of those two cycles.  Here the duplicate values move between
the endpoints, unlike the frozen K16 catalogue.  Thus the counterexample is
a generic-source warning, not a caveat to the actual eight-endpoint result.

## 3. Geometry and upper replay audit

For a candidate row `q`, the code reconstructs the falling depth

\[
d_i\in\{3,2,1,0\}
\]

by decrementing after each adjacent equal pair.  It rejects a fourth repeat,
a final positive depth, or a suffix for which `i+d_i` is out of range.  It
then forms the maximal erosion

\[
 E_c=\bigcap_{i:\ i\le c\le i+d_i}q_i              \tag{3.1}
\]

and accepts precisely when every `E_c` is nonempty and

\[
 q_i=\bigcup_{c=i}^{i+d_i}E_c                       \tag{3.2}
\]

for every row.  This is the exact nonempty depth-three erosion test used in
this split-pair fibre.

All candidates already retain the three common adjacent repeats listed in
Section 1.  Since the multiset contains only three duplicated masks, any
additional adjacent equality makes the reconstructed depth negative.
Consequently every exact hybrid has the fixed endpoint depth schedule.  This
is the key reduction needed by any subsequent solver-free run proof.

For a geometry-exact candidate, `upper_missing` maintains the nested list of
distinct ORs of intervals ending at the current row and marks every mask of
rank greater than eight.  Because this endpoint list is nested under
inclusion, equal ORs are consecutive, so comparison with `n.back()` loses no
distinct value.  Thus `holes=0` is an exact all-upper interval replay.

The program does not check generalized lower Hall, literal compiler owner
matching, or full 65,535-mask coverage.  Those are outside this artifact's
claim.

## 4. Exhaustive 23-pair result

Every listed run exited zero.  In every case the only geometry-exact subsets
are subset `0` and subset `2^c-1`; their emitted rows hash exactly to the two
input endpoints, and both have zero upper holes.  No nonuniform cycle choice
is geometry-exact.

| pair | cycles `c` | subsets | exact subsets |
|---|---:|---:|---|
| 151-155 | 2 | 4 | 0, 3 |
| 151-162 | 1 | 2 | 0, 1 |
| 151-178 | 3 | 8 | 0, 7 |
| 151-229 | 11 | 2,048 | 0, 2,047 |
| 151-231 | 5 | 32 | 0, 31 |
| 151-233 | 2 | 4 | 0, 3 |
| 155-162 | 6 | 64 | 0, 63 |
| 155-178 | 9 | 512 | 0, 511 |
| 155-229 | 13 | 8,192 | 0, 8,191 |
| 155-231 | 4 | 16 | 0, 15 |
| 155-233 | 3 | 8 | 0, 7 |
| 162-178 | 3 | 8 | 0, 7 |
| 162-229 | 15 | 32,768 | 0, 32,767 |
| 162-231 | 3 | 8 | 0, 7 |
| 162-233 | 2 | 4 | 0, 3 |
| 162-282 | 12 | 4,096 | 0, 4,095 |
| 178-229 | 6 | 64 | 0, 63 |
| 178-231 | 4 | 16 | 0, 15 |
| 178-233 | 3 | 8 | 0, 7 |
| 229-231 | 16 | 65,536 | 0, 65,535 |
| 229-233 | 9 | 512 | 0, 511 |
| 229-282 | 11 | 2,048 | 0, 2,047 |
| 231-233 | 4 | 16 | 0, 15 |

An independent lightweight parser rebuilt the occurrence lists, permutation,
and cycle decomposition for all 28 pairs.  Its cycle counts and lengths agree
with all 23 stored `CYCLES` lines.  In particular the largest completed case
is `229-231`, with 16 cycles and all 65,536 subsets traversed.

The 23 exact cycle-length signatures, in the table order above, are

```text
2606,51
2606
2389,718,1664
27,140,140,140,140,140,140,140,140,140,1319
1361,415,415,415,259
2606,201
521,521,521,521,521,51
1548,446,654,447,101,207,207,207,207
1156,136,136,136,136,136,136,136,136,68,134,134,51
1660,53,103,103
891,769,151
2897,1534,339
4,4,4,4,4,4,4,4,4,4,4,4,2,1949,606
1129,1476,259
2605,201
2029,222,118,118,118,280,280,280,280,280,280,278
2611,460,1072,346,128,128
1347,1288,926,463
1336,1336,1352
178,178,178,178,178,178,178,178,178,178,178,178,178,178,88,259
98,98,98,98,98,49,1001,1040,201
760,608,606,606,280,280,280,280,280,280,278
1010,11,124,124
```

## 5. The five unenumerated pairs

The omitted five pairs are exactly the pairs involving carrier 282 that do
not occur in Section 4:

| pair | `c` | exact independently reconstructed cycle lengths |
|---|---:|---|
| 151-282 | 26 | 1054, 110x6, 55, 80x9, 78, 39, 280x6, 278 |
| 155-282 | 23 | 118x5, 116x2, 78, 76x10, 838, 280x4 |
| 178-282 | 24 | 456x2, 1222, 934, 58x3, 56x12, 22x5 |
| 231-282 | 26 | 56, 54x14, 27, 165, 328x2, 276x3, 284, 282x3 |
| 233-282 | 21 | 12x11, 140x5, 10x2, 1677, 141, 140 |

Here repetitions such as `110x6` mean six cycles of that length.  These
counts were obtained without enumerating the `2^c` lattices.  There is no
stored endpoint-only result for these pairs.  They remain mathematically
open in this package.

## 6. Exact local residence lemma and the missing certificate

With the fixed depth schedule, define

\[
 J_c=\{j:j\le c\le j+d_j\}.
\]

For a coordinate bit `x`, (3.1)--(3.2) give the exact equivalence

\[
 x\in q_i
 \quad\Longrightarrow\quad
 \exists c\in[i,i+d_i]\quad
 x\in\bigcap_{j\in J_c}q_j.               \tag{6.1}
\]

The reverse containment in (3.2) is automatic because `i` belongs to every
`J_c` used on its right side.  Hence (6.1), for all `i,x`, is an exact local
residence characterization of middle exactness.

For one fixed occurrence-cycle lattice, every row-bit in (6.1) is a constant,
a cycle variable, or its negation.  A solver-free endpoint-only proof would
therefore be supplied by a set of local instances of (6.1) that force
equalities between cycle variables and whose equality graph is connected.
Then all cycle switches are equal, leaving only the two endpoints.  This is
an exact sufficient theorem and applies equally when `c>20`.

The current executable and TSV files do **not** emit the failed `(i,x)`
residence witness, an equality implication, or a connected implication
certificate.  Moreover `result.tsv` is filtered to exact and running-best
rows rather than committing every subset's defect.  Thus the stored census
does not itself prove the stronger sentence “every proper subset creates a
short run,” and it gives no theorem for the five pairs in Section 5.  That
claim must remain conditional until the local implication certificates are
constructed and replayed.

## 7. Provenance and hashes

```text
local/remote source search.cpp
4fcb1182f8f0c7f7843e33aa779a1777d4f91d35d2e3eee01d97b98a32c0608c

remote ELF search (BuildID 4061a161e027e32960deaa31a06645d5c2808797)
fd223cb795b53ae1abcb6b7f2cea2a1ba802d2d2747d9f0702fccd647b55136d

run_batch.sh
37131c859b44106989a9d0caff237af76f243bd965e748798d0b02033be0dcbc

batch.stdout
9f442df99ff9c4af53921d1b2edf2b181e74b27ebae1f4b4daa5a6107e66d755

batch.exit (content `0`)
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
```

Input hashes:

```text
151 a509899b9e331b4c0743b2a814707ea2d899586b35b9aba38605d31ea718b6a3
155 059600a7098beb9c01df1fa36ea973a7d1111591d71ae5e609a2aac6a2d07b4f
162 ad58f4f4f0039e44d811842dfaa65399f81a56f763fa0e4853102331fe80dac4
178 e0b2d3f0d5b68dfb699a36cc771d7412c6ddae2a9a4e57de02fd96276349e9e6
229 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974
231 6dc7a62f632814e09a74b265d2b33737d5a3923cdf4ee71a796b4e149200c78d
233 ab6e72cf98a32efe9b66567ff1908239d291f1488d7d1e21c8d630566c66ef7d
282 e9dfecd67bf34bbc93ae54179d43e942f802e2ea28198d0024dd8c76da07e0f3
```

For the 23 run directories, define the transcript-manifest digest by

```text
for every run_*_* directory, sha256sum stdout result.tsv exit;
sort those hash lines bytewise; sha256sum the resulting stream.
```

Its value is

```text
669c3b966cb9056ad910090f971dade151f956291fa37b94a55a66ed76ee0c01
```

The analogous digest of all 46 emitted endpoint files is

```text
04f0f7bccd43563504a9d83d54cb6a07960c66d3180c57e313cf5265b5a57499
```

Every emitted endpoint file individually hashes to the corresponding input
hash above.

## 8. Provenance caveat

`run_batch.sh` lists only 20 pairs.  The three directories `run_151_229`,
`run_162_229`, and `run_229_231` are valid stored runs with exit zero and
complete local transcripts, but they were added outside that batch script.
Also, the package contains no compiler command, compiler-version log, or
binary/source attestation.  The source hash agrees locally and remotely and
the executable's endpoint outputs reproduce all input hashes, but the binary
cannot be cryptographically derived from the source using the frozen package
alone.  These are provenance gaps, not mathematical counterexamples to the
reviewed code path.
