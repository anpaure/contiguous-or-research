# Next exact pair/three-edit portfolio for the 1851-entry `k=13` seeds

Date: 2026-07-24

This note does **not** change the certified `k=13` bound.  It records two
verified local no-go results, an exact exhaustive candidate-search partition
for every remaining two-position replacement, and a separately exact
anchor-three-edit encoding.

## 1. The two certified stars

For the forward one-hole word (SHA-256
`3c1b70651f319b9a8c58adba16308c6be88157d40721271aef4770e1eeb78225`),
the manifest contains all 1,850 pairs incident with position 961.  Its exact
two-arbitrary-value CNF has

```text
80,423 variables
886,887 clauses
38,316 unsafe-target incidences
76,698 provider selectors
```

Kissat returned UNSAT and `drat-trim` independently reported `s VERIFIED`.

```text
CNF   fd627eb80a600a6d3238b77b2c18d2b85218741c81894570c9696183a90f1927
DRAT  7fe2f41cddc408315362e9e56cad0597b7c7759be26fc6bc616587b14f58b1f1
check 026013ab151c3e9a134cfe5e639c2a2a97bb477e729947d0b7f767eedebcbbb0
```

For the reversed one-hole word (SHA-256
`15e15d71856823fda819a4303cb4fb46d45d1f603038f4f30f882dc1b9a63d23`),
the complete position-1470 star has

```text
76,773 variables
842,625 clauses
36,494 unsafe-target incidences
73,048 provider selectors
```

and is also independently DRAT-verified UNSAT.

```text
CNF   856eb04d6325c7dd9283d1a525f92797600a674cb4219c3a4783bded41255ae9
DRAT  5309b3e751f6d8f7685fb1d30da9cb4e63743cad70cdcd07160db9c86e237a04
check e71242de62ba73510acbfcd14ae973e720f0c6557840b98b07b47eb008f2317a
```

These certificates prove only that a successful arbitrary two-edit repair of
the corresponding seed cannot use its certified anchor.

## 2. Why the unique hole does not prune any pair

Let `t` be the seed's unique missing target.  For every pair of distinct
positions `(p,q)`, assigning the new value `t` at `p` makes the singleton
interval `[p,p]` a witness for `t`.  Hence **every** position pair can cover the
unique hole.  Any sound pruning must account for old targets destroyed by the
edits; the missing target alone eliminates no pair.

For an old target `s`, let `W_s` be its family of original witness intervals.
The target needs a new provider after editing `(p,q)` exactly when `{p,q}` hits
every member of `W_s`.  This yields an exact and very cheap collateral profile.

For `p<q`, the pair hits every interval in a family `W` iff

1. no interval of `W` ends before `p`; and
2. `q` belongs to the intersection of all intervals of `W` that start after
   `p`.

The second set is either empty or one integer interval.  Thus all pair hitting
counts are computable using suffix intersections in `O(2^k n+n^2)` after the
original witnesses are enumerated.  This identity was checked against direct
hitting-set enumeration on 200 random small words:

```text
PASS cases=200 weighted_hitting_sets_checked=55137
PASS cases=100 profile_rows=2581
```

The implementation is `scratch/k13_pair_triple_hit_profile.cpp`; its
independent audits are `scratch/audit_k13_hit_profile_logic.py` and
`scratch/audit_k13_hit_profile_binary.py`.

## 3. Exact pair profile

Across all `C(1851,2)=1,712,175` pairs, both seeds have one hole and the
following unsafe-target ranges:

```text
forward:  min 6, max 31, mean 20.43 after deleting the certified star
reverse:  min 6, max 31, mean 20.45 after deleting the certified star
```

The complete forward histogram is:

```text
unsafe  6:3       7:3       8:17       9:86      10:349
       11:914    12:1984   13:5190    14:15180   15:38360
       16:77263  17:125090 18:174962  19:214161  20:231993
       21:225015 22:197253 23:154847  24:109680  25:69672
       26:39353  27:19259  28:8065    29:2703    30:684 31:89
```

The reverse histogram differs by at most about two percent in each bucket and
also has only four pairs at unsafe count 6.  The top forward pairs are

```text
(925,926), (0,926), (0,1850)                         unsafe=6
(1849,1850), (926,1850), (0,925)                    unsafe=7
```

and the top reverse pairs are

```text
(0,1), (925,926), (0,926), (0,927)                  unsafe=6
(926,927), (927,928), (0,925)                       unsafe=7
```

Low unsafe count is a search-priority heuristic, not a feasibility theorem.
The exact CNF still decides all provider compatibility.

Five 5,000-pair ranked manifests for each seed are in
`scratch/k13_pair_ranked_manifests/`.  The first forward block generates

```text
138,661 variables, 1,600,947 clauses, 20 MiB CNF
```

and the first reverse block generates

```text
138,196 variables, 1,592,065 clauses, 20 MiB CNF.
```

They are candidate-first blocks, not an exhaustive proof unless each UNSAT is
retained and independently certified.

## 4. Disk-bounded exhaustive pair partition

After removing one certified anchor star, exactly

\[
\binom{1851}{2}-1850=1,710,325
\]

pairs remain per seed.  Partition them by their unique lower endpoint `p`:

\[
\mathcal P_p=\{(p,q):q>p,\ p,q\ne a\},
\]

where `a=961` forward or `a=1470` reverse.  The sets are disjoint and their
union is exactly every non-anchor pair.  The three-way shard audit reports:

```text
forward anchor 961:  [571021, 569516, 569788]
reverse anchor 1470: [570472, 570235, 569618]
```

Files:

* `scratch/build_k13_lower_endpoint_manifest.py`;
* `scratch/run_k13_all_pair_partition_worker.sh`;
* `scratch/audit_k13_all_pair_partition.py`.

The worker regenerates one lower-endpoint CNF at a time, overwrites its
temporary CNF/map/log, and retains only a resume ledger unless SAT is found.
A SAT result is decoded and checked by the independent quadratic verifier.
Search-only UNSAT rows are explicitly labelled `UNSAT_UNCERTIFIED`; they do
not change a certified mathematical bound.

At `p=0` there are at most 1,849 pairs, so the largest live formula is about
the size of the already solved 11 MiB star formula.  The average cell has about
925 pairs.  This is a complete candidate search at bounded disk, not by itself
an UNSAT certificate for all 1.71 million pairs.

## 5. Exact anchor-three-edit lane

The certified pair-star failures motivate a three-edit neighborhood containing
the old one-hole anchor and two additional positions.  For sorted edited
positions `a<b<c`, a contiguous interval can contain exactly one of these six
nonempty consecutive subsets:

\[
\{a\},\{b\},\{c\},\{a,b\},\{b,c\},\{a,b,c\}.
\]

For each type the unchanged base ORs are the exact cross-product of at most
three monotone OR chains.  The CNF has 39 primary value bits, exactly one
triple selector, and one Tseitin selector per undominated provider.  It is SAT
iff some manifest triple with three arbitrary nonzero values repairs the word.

The implementation and audits are:

* `scratch/k13_exact_triple_neighborhood_cnf.cpp`;
* `scratch/decode_verify_k13_triple_neighborhood.py`;
* `scratch/run_k13_exact_triple_neighborhood.sh`;
* `scratch/audit_k13_triple_neighborhood_logic.py`;
* `scratch/audit_k13_triple_cnf_end_to_end.py`.

Audits:

```text
provider identity: PASS words=24 assignments=164640 target_checks=1152480
CNF vs brute force: PASS cases=80 sat=65 unsat=15
```

For a fixed anchor, a target is unsafe for `{anchor,p,q}` exactly when `{p,q}`
hits the subfamily of its witnesses avoiding the anchor.  The same profiler is
therefore exact for ranking anchor triples.  Across all
`C(1850,2)=1,710,325` choices:

```text
forward anchor 961:  unsafe range 16..41
reverse anchor 1470: unsafe range 14..40
```

The top 1,000 anchor triples per orientation are stored in four exact 250-row
manifests under `scratch/k13_anchor_triple_manifests/`.  Exact generated sizes
for the first blocks are:

```text
forward 250 triples: 17,170 variables, 219,387 clauses, 2.6 MiB
reverse 250 triples: 16,764 variables, 217,126 clauses, 2.5 MiB
```

No production triple block has yet been solved or certified in this note.

## 6. Recommended order

1. Run the disjoint lower-endpoint pair partition on available cores.  Any SAT
   candidate immediately receives two independent direct checks.
2. In parallel or after an early no-hit prefix, run the ranked 5,000-pair
   blocks if early-candidate latency matters more than duplicate computation.
3. If the complete pair search has no hit, run the four 250-triple anchor
   blocks in increasing unsafe-count order for each orientation.
4. Retain DRAT only for deliberately selected manifests.  Search-only UNSAT is
   useful operational evidence but must not be promoted to a lower bound.

The certified finite table is unchanged throughout.

## 7. Completed production candidate searches

The disk-bounded pair partition was subsequently completed for both one-hole
seeds.  Every cell returned solver exit 20 and no SAT candidate was emitted:

```text
forward: 1,849 lower-endpoint cells, 1,710,325 non-anchor pairs
reverse: 1,849 lower-endpoint cells, 1,710,325 non-anchor pairs
status in every row: UNSAT_UNCERTIFIED
```

Together with the two checked anchor-star proofs, the search has examined
every unordered pair of edited positions for each seed.  The non-anchor rows
were deliberately run without proof traces, so this is a complete exact-SAT
candidate search but is **not** promoted to a mathematical UNSAT certificate.
The immutable ledger hashes are

```text
forward shard 0  216b8f8946ce5e2d6b24dd3135180e8b7a8e0c00b6de103ad4765e7bf8252a1b
forward shard 1  e0eba07180901433234b72b9f80d94844088413719ae9e7698f436846e38b313
forward shard 2  9e8fa26f892c8fce22263ad79cf2b35b3e719490d4ac46c4cb83f7f7b20707ea
reverse shard 0  aa6335de64cb5e4b759913ed239a06cc9f1cb13fb2a29a9be452a6016c950c06
reverse shard 1  83cf30d6b26eb5c40dc1d49507dff5afd94ced4fe4668e6c4c8c144847f99152
```

The eight ranked anchor-triple blocks were also searched: four blocks of 250
triples forward and four reversed, for 2,000 distinct three-position
neighborhoods in total.  All eight returned `UNSAT_UNCERTIFIED`; no candidate
was found.  Independent production replay rechecked the seed/manifest/formula
hash chain and the exact encoding audits.  Operational details and the
hash-locked replay wrapper are in
`K13_ANCHOR_TRIPLE_PRODUCTION_AUDIT_20260724.md` and
`scratch/run_k13_anchor_triple_portfolio.sh`.

These completed searches leave the certified upper bound unchanged.  They
motivate either a wider anchor-triple portfolio, three edits avoiding the old
anchor, or a different 1,851-entry architecture.
