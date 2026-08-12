# Exact last-occurrence circuit for fixed-prefix append completion

## Result

For a fixed prefix and `q` appended nonzero masks, append completion has an
exact SAT encoding in terms of the last-occurrence preorder of the `k`
coordinates.  It needs no physical-interval selector variables.

Applied independently to the 774 width-15 survivors of the fixed-102
four-deletion screen at `k=11,q=15`, the encoding returned

```text
UNSAT 774 / 774
SAT       0
UNKNOWN   0
TIMEOUT   0
```

The initial no-proof pass used four local workers and 233.864 seconds wall
time.  A subsequent bounded bulk run generated and independently checked a
binary DRAT proof for every one of the 774 branches.  All 774 verifier logs
end in `s VERIFIED`.

The separately generated production witness-selector queue also returned
status 20 on exactly the same 774 branches.  After canonical sorting, the two
filename/status ledgers are byte-for-byte identical, with common SHA-256

```text
94da9b4d4dd6db274fc1434999e98ce3e2ca0477c7c7b02801ed5eebe0e820b4
```

This closes the 774 branches computationally by a second, substantially
different formula.  It remains a theorem only about the fixed-prefix
four-deletion-plus-15-append neighborhood, not about arbitrary words of
length 476.

## 1. Recency characterization

Let the completed word through endpoint `e` be fixed.  For coordinate `b`,
write

```text
lambda_e(b) = the last position at or before e containing b,
```

with value `-infinity` if `b` has not occurred.  For a nonempty target `T`,
there is an interval ending at `e` whose OR is exactly `T` if and only if

```text
every b in T has occurred, and
min_{b in T} lambda_e(b) > max_{c not in T} lambda_e(c).       (1)
```

Indeed, an interval `[s,e]` has OR `T` precisely when

```text
lambda_e(b) >= s  for b in T,
lambda_e(c) <  s  for c outside T.
```

Such an `s` exists exactly under (1).  The shortest witness starts at

```text
s = min_{b in T} lambda_e(b).
```

Consequently, a witness-length cap `L` is exact if one additionally requires

```text
lambda_e(b) >= e-L+1  for every b in T,                       (2)
```

with the physical start clamped to zero.  Thus the existing all-rank
containment caps can be imposed without enumerating intervals.

## 2. Exact move-to-front recurrence

For distinct coordinates `a,b`, let

```text
R_e(a,b)  <=>  lambda_e(a) > lambda_e(b).
```

If the newly appended mask has bits `x_a,x_b`, then

```text
R_e(a,b) =
    true                 if x_a=1, x_b=0,
    false                if x_b=1,
    R_{e-1}(a,b)         if x_a=x_b=0.
```

The case `x_a=x_b=1` correctly makes the two last occurrences tied.  The
prototype encodes this truth table with four clauses per ordered pair:

```text
(-x_a or  x_b or  R_e)
(-x_b or -R_e)
( x_a or  x_b or -R_{e-1} or  R_e)
( x_a or  x_b or  R_{e-1} or -R_e).
```

At the first appended endpoint, `R_{e-1}` is the constant relation computed
from the retained prefix.

For each missing target `T` and new endpoint `e`, a selection flag implies
all comparisons `R_e(b,c)` with `b in T,c outside T` and all recent-occurrence
conditions (2).  Every target selects one endpoint.  This is satisfiable if
and only if the fixed prefix has a valid `q`-entry append completion.

Soundness follows directly from (1)-(2).  For completeness, take any valid
append word, assign every recurrence variable its actual last-occurrence
comparison, and select one genuine endpoint for each missing target.

## 3. Poset propagation

The exact recency circuit is augmented by three WLOG consequences already
used in the production interval formula:

1. each target selects exactly one endpoint;
2. incomparable missing targets cannot select the same endpoint, because
   suffix ORs at one endpoint form a chain;
3. if the missing-poset width equals `q`, every endpoint selects one member
   of a fixed maximum antichain of size `q`.

These clauses are logically redundant but decisive for propagation.  On the
branch deleting `102,0,1,2`, the version without them remained unresolved
after more than twenty minutes of contended local runtime and was terminated;
the strengthened version returned UNSAT in 1.6 seconds.  The final batch used
the poset clauses throughout.

## 4. Formula and timing ledger

Across all 774 fixed-102 width survivors:

```text
quantity        minimum   median      p90      p99   maximum       mean
missing              24       35       39       41        43     34.751
variables          2175     2340     2400     2430      2460   2336.260
clauses           23469    33864    37594    40293     42620  33616.525
seconds           0.112    1.1035    1.798    2.603     3.119      1.201
```

The archived production witness-selector formulas are larger (the current
q=15 queue begins around 3.4 thousand variables and 277 thousand clauses).
On the same local Kissat binary, the certified deletion-102 q=12 selector CNF
took 6.76 seconds, while the recency-plus-poset formula took 0.25 seconds.
Cross-machine queue timings should not be compared as controlled benchmarks.

The aggregate run is

```text
scratch/k11_length476_four_deletion_fixed102_20260723/recency_batch.out
```

with SHA-256

```text
618e7d89750dabe9310d02f86ed8e07087fe43710f1faa319dfd34b525adf507
```

The canonical recency and witness-CNF status files are

```text
scratch/k11_length476_four_deletion_fixed102_20260723/recency_statuses.txt
scratch/k11_length476_four_deletion_fixed102_20260723/witness_cnf_statuses.txt
```

`cmp` reports no difference; each has the common hash displayed above.

## 5. Representative proof certificates

The minimum missing-family branch deletes `102,0,1,2`:

```text
variables / clauses       2175 / 23469
CNF size                         330 KiB
binary proof parsed bytes      2,349,226
core clauses              13,108 / 23,469
core lemmas               17,791 / 47,433
resolution steps                 540,221
drat-trim verification             0.874 s
result                          s VERIFIED
```

The maximum missing-family branch deletes `102,49,238,263`:

```text
variables / clauses       2460 / 42620
CNF size                         597 KiB
binary proof parsed bytes      2,518,723
core clauses              14,796 / 42,620
core lemmas               19,353 / 55,418
resolution steps                 499,605
drat-trim verification             2.245 s
result                          s VERIFIED
```

The CNFs, proofs, and verifier logs are under

```text
scratch/k11_length476_four_deletion_fixed102_20260723/recency_proof_samples/
```

Their SHA-256 values are:

```text
40d63d44ca05fead0b0bb181ef62851c51065801d64f702a48cfbb77c41e699c  recency_quad_first_poset.cnf
f8dc299f3c29e46a18fdde82e7dc701ab61f46844ec893937a0bf08480333dbf  recency_quad_first_poset.dratb
abcb6c0e1dd6c456a706f609e4a49cc13f41f0395014f63ab4fa8d7620d80e82  recency_quad_first_poset.verify.log
2c3a7caf0ddf9294a224101015705d731c27624df28d17bbf86a07f883f3557d  recency_quad_last_poset.cnf
e1b030134337e90ca67a1aba89ceab18cdae30b8d0dfa8368cf0d7658bbe7e7e  recency_quad_last_poset.dratb
9b49942b5738ff7b8b1f749eb308a289bcbf5af5f870d2ec2b3a0e1ac2cacedc  recency_quad_last_poset.verify.log
```

## 6. Independent equivalence audit

The independent checker

```text
scratch/audit_append_recency_equivalence.py
```

does not import the CNF generator.  It:

- exhaustively compares recency separation and capped direct suffix ORs for
  every nonzero word through length five at k=1,2 and through length four at
  k=3;
- exhaustively checks the four-clause recurrence truth table;
- verifies the batch has exactly the same 774 deletion branches as the
  structural survivor list, with no duplicate or omitted branch;
- recomputes every reported missing count directly from the retained prefix;
- checks every recorded status is UNSAT.
- compares the canonical recency and witness-selector status ledgers byte for
  byte.

Its output is

```text
PASS recurrence_truth_table exhaustive_words_k1_to_k3 batch_branches=774 batch_unsat=774 missing_counts_recomputed=774 independent_encodings_status_bytes_equal=1
```

Current source hashes are

```text
441f2065e5e13c1c8f7fa68c0e4a9c8ec11e71a7aa24b14b3f7c0dea5ac82b80  scratch/append_completion_recency_sat.py
d9eb3fea8a215d7a85399b96ff884cc6e050ec73921143727b71000eed592ebc  scratch/run_append_recency_survivors.py
948104d44519ae7e3693f8ad370f0eb79775d7dccfe977938a643b63d24ab7e1  scratch/audit_append_recency_equivalence.py
```

## 7. Audit of the production selector encoding

Independent source inspection of `append_completion_sat.cpp` found no
completeness or soundness defect:

- the suffix-OR dynamic program computes the fixed-prefix missing family;
- one shortest representative per equal fixed-suffix OR is sufficient,
  because every appended contribution and endpoint is identical, and a
  longer equal-OR representative cannot improve a length cap;
- appended-only and cross-seam candidates are exhaustive;
- exact-one witness selection is WLOG;
- endpoint flags are exact disjunctions of their selectors;
- full cross-rank incomparability and saturated-antichain supports are sound;
- the declared-variable upper bound covers all filtered candidates and flags;
- the extracted model is checked again by direct OR enumeration.

The recency circuit is therefore an independent equivalent formulation, not
a repair for a detected bug in the production encoder.

## 8. Boundary of the advance

No new scalar theorem eliminated the width-15 survivors.  Canonical minimum
chain covers are not unique.  In fact, none of the 774 posets has a unique
maximum matching/minimum chain cover.  Testing matched edges by deletion
finds between 4 and 22 forced chain links per survivor.  Their longest forced
path has length three in 304 branches, four in 462 branches, and five in only
8 branches.  Two links,

```text
670 subset 1694
856 subset 1880
```

are forced in every survivor, but they do not obstruct completion by
themselves.  Some canonical covers fail the exact local quotient-chain
Hamilton test, while alternative maximum matchings quickly supply locally
compatible covers for the tested failures.  Hence neither chain-cover
uniqueness nor pairwise MTF compatibility closes the family.

The useful advance is instead an exact dynamic circuit at the first level
beyond width: it encodes the joint evolution of all endpoint chains as one
move-to-front last-occurrence preorder.

## 9. Bulk proof ledger

The fixed-102 four-deletion, q=15 queue completed with

```text
branches                         774
workers                            4
wall seconds                  694.953
verified                          774
failures / timeouts / SAT           0
aggregate CNF bytes       372,918,129
aggregate proof bytes   1,557,319,713
```

Every branch has a CNF, binary DRAT proof, solve log, verifier log, status
file, and per-branch SHA-256 manifest under

```text
scratch/k11_length476_four_deletion_fixed102_20260723/recency_proofs/
```

The batch log SHA-256 is

```text
231190748bda26a5c3f74a1ff5c8ab7a10d1bd3f3209938f9d78333a369af8fc
```

The aggregate 4,644-file manifest has SHA-256

```text
b402baf7f5e032f22969d0b1c2b3f712ad779d84ef2a4ceef44881326adb2e16
```

The same circuit also replaced the pending fixed-102 three-deletion q=14
proof queue:

```text
branches                         158
workers                            4
wall seconds                   45.344
verified                          158
failures / timeouts / SAT           0
aggregate CNF bytes        58,150,617
aggregate proof bytes     214,067,333
batch-log SHA-256
497087026d16bd0c9364ff798ebe3463b5aa1aec2a3da3846ee172ade785103f
aggregate-manifest SHA-256
2e30ea806ccb47fcc48e1e5c231c15424fc4d53f4957460ec6c7bf19a6699b66
```

Those artifacts are under

```text
scratch/k11_length476_three_deletion_screen_20260723/fixed102_recency_proofs/
```

Finally, the primary full four-deletion scan found 16 width survivors outside
the fixed-102 family.  All 16 independently generated recency proofs verify:

```text
workers                             2
wall seconds                   14.724
verified                           16
aggregate CNF bytes         6,829,160
aggregate proof bytes      36,503,829
batch-log SHA-256
3066bc0291c3da6ec6afd27dc5ae31b7767d9804246cd78d3f26048df78a7eaf
aggregate-manifest SHA-256
ada712b40ee72c459710bbf887c481e634de5754987cd94823b94191ce2de2df
```

They are stored in

```text
scratch/k11_length476_four_deletion_full_20260723/non102_recency_proofs/
```

Two runs of the independent full structural enumeration were externally
terminated before their atomic final output.  Therefore the statement that
790 is the complete survivor set continues to cite the primary exhaustive
scan, its byte-identical fixed-102 reproduction, and the direct audit of all
790 reported survivors; no second full-aggregate agreement is claimed.  The
proof status of each of the 790 reported survivors is complete.
