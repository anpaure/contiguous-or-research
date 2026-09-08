# Independent audit of the fixed-prefix rank-antichain endpoint cap

## Verdict

**PASS for the intended zero-free domain `1 <= k < 20`, `q >= 0`.**

The new early contradiction, exact target-by-endpoint flags, endpoint
distinctness clauses, and saturated-endpoint clauses in
`append_completion_sat.cpp` are exact consequences of endpoint geometry:

* if a fixed prefix misses more than `q` masks from one rank layer, no
  `q`-entry append can complete it;
* if it misses exactly `q` masks from one rank layer, every appended right
  endpoint must serve that layer, so the endpoint support clauses lose no
  completion;
* at every rank-feasible branch, two distinct missing masks of one rank cannot
  choose the same appended endpoint, so the per-endpoint at-most-one clauses
  are also lossless.

This includes seam-crossing witnesses and remains true with containment caps
enabled.  The current source also fixes the proof-hook ordering bug: tracing
starts before every option, declaration, and clause, and trace-open failure is
checked.  Its audited SHA-256 is

```text
c5c75460b861bc96a20ffe42daab241d401769ccd4dd771bae0d09e2254136cd
    append_completion_sat.cpp
```

An independent physical-interval enumeration proves that deleting old index
zero is structurally impossible to repair with twelve entries: the shortened
prefix misses thirteen rank-seven masks.  Among all 465 one-entry deletions,
only 82 survive this necessary test, and precisely indices `7,89,196` have
maximum missing-layer size eleven.  The 82 survivors are not claimed
feasible.

## 1. Endpoint theorem

Let `P` be a fixed prefix and append `q` new entries.  Let `T` be a target
absent from `P`.  Every witness for `T` in the completed word must end at a
new position.  Otherwise the interval lies wholly in `P` and already
witnesses `T` there.  This covers both append-only and seam-crossing
intervals.

At one fixed new endpoint `e`, moving the left endpoint left produces a chain

\[
 U([e,e])\subseteq U([e-1,e])\subseteq\cdots .
\]

Distinct masks of one rank are incomparable, so this chain contains at most
one of them.  If the prefix misses `m_r` rank-`r` targets, choosing one
completed-word witness for each injects those targets into the `q` new
endpoints.  Therefore

\[
 m_r\le q.                                                   \tag{1}
\]

When `m_r=q`, this injection is a bijection and every new endpoint is used
once by the rank-`r` layer.  The proof assumes neither singleton append
entries nor append-only witnesses.

For a fixed completed word, possible-endpoint sets belonging to two different
missing rank-`r` targets are disjoint: a shared endpoint would put two
incomparable ORs in one suffix chain.  Thus any choice of one witness per
target in the saturated case necessarily covers all `q` endpoints.

## 2. Exact source correspondence

Lines 92--100 compute the missing family and its rank counts.  Lines 120--126
implement (1) exactly:

```text
missing_by_rank[rank] > q  =>  structural UNSAT.
```

Every target gets an at-least-one support clause and a pairwise at-most-one
family, so it selects exactly one witness.  For each target and endpoint with
at least one candidate, lines 229--243 create a flag `E(T,e)` and add

```text
selector -> E(T,e)             for every selector ending at e,
E(T,e) -> OR(selectors ending at e).
```

Thus `E(T,e)` is exactly the chosen endpoint of target `T`; supports with no
candidates are represented by constant false rather than an unnecessary
variable.  The global exactly-one witness choice also implies that exactly
one endpoint flag is true for each target.

Lines 249--258 add pairwise `AMO` clauses among the flags of equal-rank
targets at one endpoint.  This is exactly the suffix-chain conclusion and is
logically redundant in a complete OR model, but exposes the theorem directly
to propagation.  If `missing_by_rank[rank] == q`, the same loop requires one
flag at every endpoint.  If such a flag support is empty, the empty clause
correctly states that no completion exists.

Every selector in an endpoint support implies exact OR equality:

* a fixed suffix OR containing a target-external bit is rejected;
* selecting the candidate forbids every target-external bit in its appended
  positions;
* selecting it requires every target bit not already supplied by the fixed
  suffix.

Thus the clauses enforce the same suffix-chain incompatibility as the proof,
even though no explicit cross-target at-most-one clauses are needed.

## 3. Seam quotient and containment caps

Every seam-crossing interval is a suffix of `P` followed by append prefix
`[0,e]`.  The old part matters only through its suffix OR.  Lines 136--142
scan suffix lengths in increasing order and retain the shortest suffix for
each distinct OR value.

Replacing a longer suffix by that shortest same-OR suffix preserves the
target and can only shorten the physical interval.  Hence the quotient loses
no completion with caps off or on.

The containment theorem bounds every target witness.  Therefore a feasible
completion retains a capped witness for every missing target.  In a saturated
rank layer, that witness still ends at the only endpoint available to that
target.  Containment pruning and endpoint saturation therefore compose
without an additional assumption.

For the original `k=11,q=12` prefix, the source's independent literal-stream
summary is identical with containment caps disabled and enabled:

```text
used variables=1338  declared upper bound=2550
clauses=71020        literal calls=242178
candidates=1050      endpoint flags=156
endpoint AMO clauses=792
hash1=871c60a667837349
hash2=98419efafa7558f0
```

The clause delta over the pre-flag formula is exactly

```text
1050 selector-to-flag implications
+156 flag-to-selector reverse clauses
+792 endpoint distinctness clauses
=1998 clauses.
```

The twelve saturated endpoint supports existed before and are now written in
terms of equivalent flags.  The unused part of the declaration is harmless:
it reserves the unpruned maximum candidate and flag pool, while fixed-OR
checks omit many selectors.

## 4. Nonzero and boundary cases

The executable intentionally addresses the nonzero problem.

* Mask zero is not included in `missing`, and fixed-prefix entries must be
  nonzero.
* The original full problem is recovered by prepending one zero.
* Forbidding zero append entries is WLOG even at a nonminimal exact `q`:
  delete every zero, preserving positive interval ORs after compression, then
  restore the requested length with arbitrary nonzero padding at the end.
* For `q=0`, a missing target triggers structural UNSAT; a universal prefix
  returns an empty append.
* An empty fixed prefix is allowed and simply has no seam candidates.

The CLI assumes `1 <= k < 20` and `q >= 0`; it does not validate those
conditions.  Its padding value `1` is invalid for degenerate `k=0`.  This is
an out-of-scope qualification, not an error in the current `k=11` runs.  The
all-`k` constructor must continue to handle `k=0` separately.

## 5. Proof-hook audit

CaDiCaL proof tracing must be active before the formula is constructed.  The
current source calls `trace_proof` immediately after constructing `Solver`,
before `set`, `declare_more_variables`, or any `add`, and checks its Boolean
return value.

The audit-only API double

```text
scratch/append_rank_cap_proof_stub/cadical.hpp
```

records operation order.  A normal proof request reports

```text
trace_requested=1 trace_first=1 operations=242314 clauses=71020.
```

A simulated open failure reports

```text
could not open proof trace ...
trace_requested=1 trace_first=1 operations=0 clauses=0
```

and the executable exits with status 2.  Moving the hook changes no formula:
the post-fix literal stream is byte-identical to the pre-move summary above.

Structural theorem exits occur before solver construction and deliberately do
not emit DRAT; their certificate is the independently checked rank profile
and theorem (1).

## 6. Original `k=11,q=12` regression

Independent exhaustive interval enumeration of
`k11_upper549_natural_array.txt` gives

```text
length=465, missing=13, rank7=12, rank8=1.
```

The new structural test accepts this branch, and the saturated rank-seven
layer legitimately activates all twelve endpoint supports.  The stored
append still completes the prefix, and every one of its twelve new endpoints
serves a missing rank-seven target.

As a source-level regression, the current 2,550-variable/71,020-clause DIMACS
was generated with a clause-streaming API double and solved by Kissat.  A
fresh model decoded to

```text
604 1860 1730 1251 1170 670 956 251 941 493 1468 1946
```

and both independent verifiers accept the resulting length-477 word:

```text
exhaustive: length=477 covered=2047 required=2047
suffix OR:  length=477 covered=2047/2047 missing=0
```

This SAT run is only a regression.  The stored certificate already proves
the upper bound without trusting a solver.

The three one-endpoint-slack deletion branches receive the intended generic
distinctness encoding even though no rank is saturated:

| skip | missing | used vars | clauses | candidates | endpoint flags | endpoint AMO |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 21 | 2,058 | 116,340 | 1,674 | 252 | 780 |
| 89 | 19 | 1,878 | 104,956 | 1,518 | 228 | 732 |
| 196 | 19 | 1,878 | 104,420 | 1,518 | 228 | 768 |

For example, skip 7 has missing-rank multiplicities
`2,3,4,11,1` across ranks 4 through 8.  Per endpoint this gives

\[
 \binom22+\binom32+\binom42+\binom{11}2=65
\]

distinctness clauses, and `12*65=780` in total.  The other two table rows
independently reproduce their corresponding binomial sums.  Enabling
containment caps leaves the complete two-word literal-stream summaries
unchanged for all three branches and for the no-skip regression.

## 7. Deletion-profile audit

The standalone checker enumerates every physical interval after every
deletion and does not reuse the optimized distinct-suffix recurrence.  It
obtains:

| maximum missing count in one rank | deletions |
|---:|---:|
| 11 | 3 |
| 12 | 79 |
| 13 | 144 |
| 14 | 135 |
| 15 | 73 |
| 16 | 29 |
| 17 | 2 |

Therefore exactly `3+79=82` of 465 deletions survive the `<=12` test.  The
three maximum-eleven branches are zero-based indices

```text
7 89 196.
```

Deleting index zero yields

```text
missing=15: rank6=1, rank7=13, rank8=1.
```

The source consequently returns

```text
UNSAT structurally rank=7 missing_layer=13 append_endpoints=12
```

before constructing a SAT formula.  This is a mathematical UNSAT certificate
for that fixed deletion branch, not a solver-status claim.

## 8. Independent checker and hashes

`scratch/audit_append_rank_antichain_cap.cpp` performs:

1. brute-force physical-interval coverage of the original prefix and stored
   completion;
2. direct saturation of all twelve new endpoints;
3. brute-force physical-interval profiles for all 465 deletions;
4. exhaustive enumeration of all nonzero fixed-prefix extensions with
   `1<=k<=3`, prefix and append lengths at most three.

The small check inspected 8,429 universal extensions and 667 saturated
rank-layer instances.  Complete output:

```text
small_exhaustive universal_extensions=8429 saturated_layers=667
k11_base missing=13 rank7=12 rank8=1 endpoint_saturation=12/12
k11_skip0 missing=15 rank6=1 rank7=13 rank8=1 structural_unsat=1
k11_deletions survivors=82/465 max11=7,89,196 histogram=11:3,12:79,13:144,14:135,15:73,16:29,17:2,
PASS
```

Both audit sources compile warning-free under C++20.  SHA-256 inventory:

```text
4126473e752b83dc0cfa79404392f50b9a3a459fb35dfe3581092d71b3134498
    scratch/audit_append_rank_antichain_cap.cpp
6cf35b2b593a545a54a54c25370f5829a87e71a2c47204cc56487bdf2ce0b44f
    scratch/append_rank_cap_proof_stub/cadical.hpp
c508307dcc666b0e5c0b11ff96cb129df82d74d3b34d2d3aec4adf7b861c8ebd
    k11_upper549_natural_array.txt
ba44a89403c6b402fb6c9b48cd8a1274dd716cd56885af710db8f091e8ee6989
    k11_append_12.txt
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b
    k11_completed_477.txt
```

## Final conclusion

The generic rank-antichain endpoint cap, exact endpoint flags, same-rank
endpoint distinctness clauses, and saturated endpoint supports are sound and
complete for fixed-prefix extensions in the intended domain.  They certify
skip zero UNSAT, reduce the 465 deletion portfolio to 82 theorem-surviving
branches, strengthen the three one-endpoint-slack formulas, and preserve the
original satisfiable twelve-entry completion.  They do not prove any of the
82 survivors feasible and do not by themselves change the unrestricted
`k=11` bounds.
