# Exact relative-bit-permutation CSP: the next `k=13`, length-1,851 lane

Date: 2026-07-24

## Verdict

The highest-leverage next candidate lane is not another small edit around the
two current one-hole words.  It is the complete **relative 12-bit permutation
family** of the one-interface lift, with the deletion pair free.

The new encoding represents all `12!` relative coordinate maps symbolically
with only a `12 x 12` permutation matrix.  A first production portfolio takes
the first 5,000 individually feasible deletion pairs with the fewest exact
internal holes in each lifted orientation (or every feasible pair if there are
fewer).  If both lists have 5,000 rows, it searches

```text
2 * 5,000 * 12! = 4,790,016,000,000
```

distinct `(orientation, deletion pair, relative bit map)` architectures.  The
preparation ledger prints the exact retained count before solving, so the
scope is never inferred from the requested limit.  No computation is launched
in this note.  The runner is disk- and RAM-bounded and independently verifies
every SAT result.

This scope is disjoint from the completed arbitrary-two-edit searches around
the identity-derived one-hole seeds: a nonidentity relative map changes most
of the 924 retained lifted entries coherently.  It is also structurally wider
than the 2,000 tested anchor triples.

## 1. Candidate architecture

Let `B=(B_0,...,B_925)` be the exact nonzero `k=12` word.  Let `pi` be an
arbitrary coordinate permutation of the 12 old bits, let `O` be either `B` or
its reversal, and choose `0 <= a < b < 926`.  The candidate is

\[
 B\ \Vert\ (2^{12})\ \Vert\
 \bigl(2^{12}\vee\pi(O_i):i\ne a,b\bigr).
\]

Its length is exactly

\[
926+1+(926-2)=1851.
\]

The first block already covers every nonzero target omitting the new bit.  It
remains only to decide whether all 4,096 residues of targets containing the
new bit occur.

## 2. Exact profile reduction

For a fixed oriented deletion pair, put

* `R_ab = (0,O_0,...,omit O_a,...,omit O_b,...,O_925)`;
* `I_ab` = all interval ORs of `R_ab`;
* `P_ab` = the distinct prefix OR chain of `R_ab`;
* `S` = the distinct suffix OR chain of the unchanged lower word `B`;
* `H_ab = [0,4095] minus I_ab`.

Internal lifted intervals give exactly `pi(I_ab)`.  Intervals crossing the
one lower/lifted interface give exactly

\[
 \{s\vee\pi(p):s\in S,\ p\in P_{ab}\}.
\]

Consequently the candidate is universal if and only if, for every
`h in H_ab`, there are `s in S` and `p in P_ab` with

\[
s\vee\pi(p)=\pi(h).                                      \tag{2.1}
\]

The prefix ORs form an inclusion chain.  Let `p_h` be the largest prefix
contained in `h`.  If (2.1) holds for any smaller prefix, it also holds for
`p_h`.  Thus each hole needs only the undominated providers indexed by the
eight suffix values.  For a fixed suffix, (2.1) is equivalent to

\[
 \pi(h\setminus p_h)\subseteq s\subseteq\pi(h).          \tag{2.2}
\]

This equivalence is the core compression.  It replaces an exhaustive
`12!` loop and repeated interval enumeration by a small permutation CSP.

An individual provider is possible for some permutation exactly when

\[
 |h\setminus p_h|\le |s|\le |h|.                         \tag{2.3}
\]

The profile scanner uses (2.3) as an exact necessary filter and ranks
surviving pairs first by `|H_ab|`.  Ranking is heuristic only; the subsequent
SAT formula is exact.

## 3. Exact CNF

`scratch/k13_relative_bitperm_exact_cnf.cpp` uses:

* 144 variables `X[i,j]` for `pi(i)=j`;
* exact-one constraints on every row and column;
* one exactly-selected deletion pair from the supplied manifest;
* one provider selector for each surviving `(pair,hole,suffix)`.

A provider for `(h,p_h,s)` implies

* for every `i in h minus p_h`, `pi(i)` lies in `s`;
* for every `j in s`, the preimage of `j` lies in `h`.

Under the permutation constraints these clauses are exactly (2.2).  Every
hole has a pair-gated disjunction of its providers.  Therefore

```text
CNF SAT
iff one listed deletion pair and one of all 12! bit permutations
    produce a universal 1,851-entry word.
```

The same 144 mapping variables are safely shared by all manifest pairs because
exactly one pair selector is true.  Provider selectors imply their pair
selector, so unselected pairs impose no mapping constraint.

## 4. Audits completed without a production search

The reduction audit
`scratch/audit_k13_relative_bitperm_reduction.py` exhausts every permutation
through five bits on random small words and checks:

1. all-prefix crossing equality versus the maximal-prefix reduction;
2. the setwise condition (2.2);
3. full direct residue coverage versus coverage of all internal holes.

It reports

```text
PASS cases=120 assignments=4560 hole_checks=92476 dominance_checks=244420
```

Both C++ sources compile warning-free under
`-Wall -Wextra -Wpedantic`.  As a production regression, the already-audited
endpoint pair `(0,925)` generates:

```text
forward:  holes=4 providers=5 variables=414 clauses=842
reverse:  holes=4 providers=6 variables=415 clauses=845
```

Kissat returns UNSAT immediately for both formulas, agreeing with the
independent all-`12!` endpoint ceiling theorem.  This regression is not being
promoted as a new proof; it checks the new pipeline against a previously
proved case.

The model decoder independently rebuilds the 1,851 entries and enumerates all
contiguous ORs.  The production wrapper then invokes the separate
`verify_or_array` binary and accepts a candidate only if both checks cover all
8,191 nonzero targets.

## 5. Bounded first production portfolio

The recommended first pass is:

1. scan all `C(926,2)=428,275` deletion pairs once in each orientation;
2. retain the top 5,000 individually feasible pairs by exact internal-hole
   count;
3. split them into 20 blocks of 250 pairs;
4. solve the blocks in search mode, stopping at the first doubly verified SAT
   word.

The profile scan holds about 428,275 small records (well below 32 MiB) and
writes only the requested ranked rows.  Each SAT block has one permutation
matrix and only the hole/provider clauses of 250 pairs.  The endpoint
regression is 10 KiB.  Exact block sizes are printed before solving; the
runner refuses a block exceeding either 256 MiB CNF or 10 million clauses.
Kissat is additionally placed under a 4 GiB virtual-memory limit when
`prlimit` is available.  Search-mode UNSAT deletes the CNF, map, and model
after hashing them, so accumulated disk is bounded by compact logs and stats.

The block solve time cannot be asserted before the ranked profile exists.
Based on the endpoint formula and the completed 250-row anchor-triple formulas,
the expected solve unit is seconds, not hours; the all-pair profile scan is
expected to dominate preparation.  Any block whose generated stats violate
that expectation is automatically stopped and split rather than allowed to
pressure the shared host.

A lightweight nonproduction sizing check on 250 uniformly sampled deletion
pairs generated in `0.03` seconds:

```text
variables=4,218  clauses=50,070  CNF=1.3 MiB
holes=3,905      providers=3,311
```

Kissat rejected that block immediately.  It contained individually impossible
pairs and is not part of the ranked portfolio; its only purpose is to confirm
that 250-pair blocks are comfortably below the resource guardrails.  The exact
ranked block stats remain the authoritative production estimate.

### RunPod preparation (do not run locally)

Copy the eight files named in Section 7 and the 926-entry base word to one
RunPod work directory.  For each orientation:

```bash
./prepare_k13_relative_bitperm_portfolio.sh \
  /root/k13_relperm/k12_optimal_nonzero.txt \
  /root/k13_relperm/portfolio forward 0 5000 250 5

./prepare_k13_relative_bitperm_portfolio.sh \
  /root/k13_relperm/k12_optimal_nonzero.txt \
  /root/k13_relperm/portfolio reversed 1 5000 250 6
```

Compile the exact generator warning-free:

```bash
g++ -O3 -std=c++20 -Wall -Wextra -Wpedantic \
  k13_relative_bitperm_exact_cnf.cpp \
  -o k13_relative_bitperm_exact_cnf
```

Then run one sequential portfolio per free CPU:

```bash
export K13_RELPERM_WORK=/root/k13_relperm/results
export K13_RELPERM_GENERATOR=/root/k13_relperm/k13_relative_bitperm_exact_cnf
export K13_RELPERM_DECODER=/root/k13_relperm/decode_verify_k13_relative_bitperm.py
export K13_RELPERM_RUNNER=/root/k13_relperm/run_k13_relative_bitperm_block.sh
export VERIFY_OR_ARRAY=/root/verify_or_array

./run_k13_relative_bitperm_portfolio.sh \
  forward 5 /root/k13_relperm/k12_optimal_nonzero.txt \
  /root/k13_relperm/portfolio/forward.manifests 0 search 131300 1800

./run_k13_relative_bitperm_portfolio.sh \
  reversed 6 /root/k13_relperm/k12_optimal_nonzero.txt \
  /root/k13_relperm/portfolio/reversed.manifests 1 search 141300 1800
```

These commands are a launch recipe only.  No remote job was launched while
preparing this result.

## 6. Why this precedes more three-edit work

The completed exact candidate searches already cover every arbitrary
two-position edit of both fixed one-hole seeds, and the top 2,000 triples that
contain their old anchors.  Extending anchor triples is a valid but incremental
lane.  Three edits avoiding the anchor have

\[
\binom{1851}{3}=1,055,270,525
\]

position triples before values are considered, and the current exact triple
encoding has no comparably strong global symmetry compression.

In contrast, the relative-permutation CSP changes almost the entire lifted
half yet compresses every one of the `12!` coherent relabelings into 144
primary variables.  If both feasible lists reach the requested 5,000 rows,
the first 10,000-pair portfolio represents 4.79 trillion complete
architectures.  It is therefore the sharper first attempt.

If this lane has no hit, the next order is:

1. extend the ranked relative-permutation manifests from 5,000 to 25,000 pairs;
2. partition all 428,275 pairs by lower endpoint for a disk-bounded exhaustive
   candidate search (the complete two-orientation family is
   `410,288,820,480,000` architectures);
3. only then spend comparable compute on non-anchor triples;
4. if both fail, change the interface architecture itself: move the singleton
   into a two-portal seam or split the lifted block into two coherently
   permuted pieces.  That is a genuinely new length-1,851 architecture rather
   than another local repair.

## 7. Files and hashes

```text
8f18d7176ecacc9283b4937a72d9e3c0d2392135f5f6e01a5d9b31d29d087651  scratch/k13_relative_bitperm_profile.cpp
67b88a8f934ee654f1e1f11695d993ec48d559220848cff4a41541a33bb9d13b  scratch/k13_relative_bitperm_exact_cnf.cpp
f71864608bb5d8995854db6d63b2739b4c7615df7d939f3cc5b31e9a1a2ed687  scratch/decode_verify_k13_relative_bitperm.py
3fe7c1f058dcdab2e90d9a9e60437fd4ae2ec7c3d1909c3996bf2e42e9f14734  scratch/build_k13_relative_bitperm_manifests.py
b8d89c49c8f230a758250f59c5ec2bac34413b604bb9ab348a3213990f63356e  scratch/run_k13_relative_bitperm_block.sh
85f51d1c99b94a8aa7214f353d73bd377d6aa7162fc859940719bb0691181f1e  scratch/run_k13_relative_bitperm_portfolio.sh
df0e16c8a5a4997e9b51783423564bc45ad18da67a6ded6b9ffe0a8c053a0652  scratch/prepare_k13_relative_bitperm_portfolio.sh
6dc6fcf70b6b257b8babf3e177653616e0b96fbf26e81f27f5d3dd7291ca6b5a  scratch/audit_k13_relative_bitperm_reduction.py
```

The base word used by this architecture has SHA-256

```text
75754f3184c649d9d25b1705140d5627cf50c2b85e3a6dcabdd585dcf94a62da
```

and exactly 926 entries.

## 8. First RunPod production result

The complete individually feasible part of the requested top-5,000 profile
was run on Purple RunPod in both orientations.  The exact profiler found only
1,318 individually feasible deletion pairs per orientation, rather than
5,000.  Each list was split into five blocks of 250 and one block of 68.
All 12 blocks returned search-mode UNSAT and no candidate was produced.

Thus the candidate search covered

```text
2 * 1,318 * 12! = 1,262,648,217,600
```

coherent `(orientation, deletion pair, relative permutation)` architectures.
The formulas were small: the largest block had 6,259 variables and 80,214
clauses.  The durable ledger hashes are

```text
27a44ad12271e38697219a9625d2ceb4b06dd7cd0fa62462495a0c06e60f8fab  forward.ledger
99139d9f4161d70785955b6156118029aa648524dfc964edc17005a6c6f29f99  reversed.ledger
```

The ranked-profile hashes are

```text
7ee09326c2c45f81260f0f15ec350acb6f62df5ffe2509f56eda9ee3d15b7588  forward.ranked.tsv
534d99011f32a2d794bf22b425f9f16fbf444eb2b0c6326b620beeac147ac840  reversed.ranked.tsv
```

The same twelve blocks were then rerun in certification mode.  Every Kissat
run returned status 20, every `drat-trim` check returned zero and printed
`s VERIFIED`, and a separate audit regenerated both complete profiles and all
36 CNF/map/stats artifacts byte-for-byte.  The exact partition is

```text
exact necessary infeasibility filter:
  2 * (428275 - 1318) * 12! = 409,026,172,262,400

twelve DRAT-certified feasible-pair CNFs:
  2 * 1318 * 12! = 1,262,648,217,600

total architecture excluded:
  410,288,820,480,000
```

Thus this now formally excludes the entire specified one-interface relative-
permutation architecture, not just the retained candidate portfolio.  It does
not exclude other length-1,851 words, so the finite `k=13` bound is unchanged.

Independent certificate audit:

```text
fc36f456672648693ed02404dfe6e71c66c67beafd45751440d9ae3c0aade058  K13_RELATIVE_BITPERM_FULL_CERTIFICATE_AUDIT_20260724.md
2437aa1d9032bb7922263ee1138002469cb7456bd0fe5bc0393425ccfb8b722a  scratch/audit_k13_relative_bitperm_full_certificate.py
```
