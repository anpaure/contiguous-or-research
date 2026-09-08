# Independent audit of `exact_or_sat_direct.cpp`

## 1. Scope and verdict

Audited source:

```text
file:   exact_or_sat_direct.cpp
lines:  236
bytes:  9552
SHA-256:
ad6c1f2853ac6f03161a7778525c518607c4544b9942ecd595312ae23a8b03b3
```

The audit target is the invocation `k=11,n=465`.  In that scope the formula is
**sound and complete for the unrestricted nonzero problem**:

> The formula is satisfiable if and only if there is a length-465 array of
> nonzero 11-bit masks whose nonempty contiguous-subarray ORs contain every
> nonzero 11-bit mask.

In particular, the formula does **not** assume a fixed derivative row, a
Hamilton path, grading by window length, a prescribed endpoint schedule, or
the existing seed's combinatorial structure.  The seed affects solver
polarities only.

Consequences, using the proved lower bound `nu(11) >= 465`:

* a SAT model, after independent OR verification, proves `nu(11)=465` and
  hence proves `N(11)=466` for the original problem including zero;
* a genuine refutation of this formula proves `nu(11)>=466` globally, not
  merely failure of the fixed-row ansatz.

There is one important certification caveat.  The current program invokes
CaDiCaL in process but does not request a DRAT or LRAT trace.  Thus a printed
`UNSAT` is logically about the unrestricted problem, but the log alone is not
an independently checkable impossibility certificate.  A theorem-grade UNSAT
claim still requires proof tracing and independent proof checking.

## 2. Array and interval variables

Let `A[p,b]` be the variable returned by `A(position,bit)` on lines 65--74.
The clause

```text
A[p,0] OR ... OR A[p,10]
```

forces every array entry to be nonzero.

For each nonzero target mask `S`, the code creates three length-`n` unary
vectors `L`, `R`, and `M`.

### Lemma 1: `L` and `R` select one interval

The clauses on lines 116--123 imply

```text
L = 0 ... 0 1 ... 1,
R = 1 ... 1 0 ... 0.
```

Indeed, `L[n-1]` is true and `L[p] -> L[p+1]`; similarly, `R[0]` is true and
`R[p+1] -> R[p]`.  Therefore there are unique indices

```text
ell = min {p : L[p]=1},
rho = max {p : R[p]=1}.
```

The three clauses on lines 126--128 are exactly

```text
M[p] <-> (L[p] AND R[p]).
```

The long disjunction on line 131 requires at least one `M[p]`, and hence
`ell<=rho`.  Consequently

```text
M[p]=1  iff  ell<=p<=rho.
```

Thus every target receives exactly one nonempty contiguous witness interval.
Choosing only one witness is without loss of generality: every universal
array has at least one witness from which to choose.

### Lemma 2: the length clauses are exact

For a positive bound `B<n`, lines 133--135 add

```text
not M[p] OR not M[p+B]
```

for every legal `p`.  Since the true `M` positions form one interval, these
clauses hold exactly when its length is at most `B`.  If `B<=0`, the empty
clause correctly makes the instance unsatisfiable.

## 3. Exact target OR clauses

For a bit `b` absent from target `S`, lines 137--140 add

```text
M[p] -> not A[p,b]
```

at every position.  Hence no outside bit occurs in the chosen interval.

For a bit `b` present in `S`, the occurrence variables `H[b,p]` satisfy

```text
H[b,p] -> M[p],
H[b,p] -> A[p,b],
OR_p H[b,p].
```

Therefore at least one interval position contains `b`.  Combining the
positive- and negative-bit clauses gives

```text
OR_{p=ell}^rho A[p] = S
```

exactly.  The reverse implications `M[p] AND A[p,b] -> H[b,p]` are unnecessary:
the `H` variables are existential occurrence certificates, not definitions.

Conversely, given a real witness interval, set `L`, `R`, and `M` to that
interval and choose one actual occurrence for each target bit as its true
`H`.  All clauses are then satisfied.  Thus this part of the encoding is both
sound and complete.

## 4. Audit of `safe_bound`

For rank `r`, the code uses

```text
B(r) = min(n-C(k,r)+1, min_{q>r}(n-C(k,q))),
```

clipped to `[0,n]`.  This is a globally valid witness bound.

### Lemma 3: same-rank bound

Choose one witness interval for each of the `m=C(k,r)` rank-`r` masks and sort
them by left endpoint.  Two selected intervals cannot contain one another:
interval containment implies OR-mask containment, and two distinct equal-rank
masks are incomparable.  Their left endpoints and right endpoints are
therefore both strictly increasing.

For the `i`-th interval in zero-based order,

```text
left_i >= i,
right_i <= n-m+i.
```

Its length is at most `n-m+1`.  Hence every universal array admits selected
rank-`r` witnesses satisfying the first term of `B(r)`.

### Lemma 4: higher-rank bound

Fix a higher rank `q>r`, put `m=C(k,q)` and `d=n-m`, and select its `m`
nonnesting witness intervals.  The inequalities above give

```text
I_i subseteq [i,i+d].
```

Every physical interval `J=[a,b]` of length at least `d+1` has `a<m` and
contains `[a,a+d]`, hence contains `I_a`.  Its OR therefore has rank at least
`q`.  An interval representing a rank-`r` mask cannot do that, so every such
witness has length at most `d=n-C(k,q)`.

Taking the minimum over all higher ranks proves the second term of `B(r)`.
This argument applies to every unrestricted universal array; it is not a
fixed-row assumption.

For `k=11,n=465`, the audited bounds are:

| rank | targets | maximum witness length | length clauses per target |
|---:|---:|---:|---:|
| 1 | 11 | 3 | 462 |
| 2 | 55 | 3 | 462 |
| 3 | 165 | 3 | 462 |
| 4 | 330 | 3 | 462 |
| 5 | 462 | 3 | 462 |
| 6 | 462 | 4 | 461 |
| 7 | 330 | 136 | 329 |
| 8 | 165 | 301 | 164 |
| 9 | 55 | 411 | 54 |
| 10 | 11 | 455 | 10 |
| 11 | 1 | 465 | 0 |

The rank-five bound of three is valid because every four-position interval
already contains one of the 462 selected rank-six witnesses.

## 5. Rank-five/rank-six endpoint auxiliaries

The source materializes starts and ends only for the two 462-element central
layers.

### Lemma 5: transition variables are exact

For `p=0`, lines 199--200 encode

```text
start[0] <-> L[0].
```

For `p>0`, lines 202--204 encode

```text
start[p] <-> (L[p] AND not L[p-1]).
```

The end clauses on lines 206--212 dually encode

```text
end[n-1] <-> R[n-1],
end[p]   <-> (R[p] AND not R[p+1])  for p<n-1.
```

Because `L` and `R` are thresholds, every target has exactly one true start
and one true end.

### Lemma 6: the sequential at-most-one encoding is correct

For literals `x_0,...,x_{m-1}`, `at_most_one` introduces prefix variables.
If `x_i` is true, its prefix variable is true and truth propagates through all
later prefixes; any later true `x_j` then contradicts either an internal
conflict clause or the final conflict clause.  Conversely, whenever at most
one `x_i` is true, assigning each prefix to

```text
OR(x_0,...,x_i)
```

satisfies all clauses.  Thus the encoding is equisatisfiable with an exact
at-most-one condition.

### Lemma 7: endpoint distinctness loses no solutions

Suppose two distinct equal-rank target witnesses share a left endpoint.  One
of their intervals contains the other.  Their OR masks are therefore
comparable.  Equal cardinality makes comparable masks equal, contradicting
that the targets are distinct.  The same argument applies to a shared right
endpoint.

Hence starts and ends are necessarily distinct inside each rank layer.  The
auxiliary constraints merely expose an implication already present in every
valid array.  They impose no relation between the rank-five and rank-six
layers and no Hamilton, fixed-row, or fixed-regime condition.

## 6. Nonzero entries are without loss of generality

For the nonzero-mask problem, delete every zero entry.  Within any nonzero
witness interval, the surviving entries remain contiguous in the compressed
array and have the same OR.  Thus zero entries never improve the minimum.

More generally, if deletion produces a universal nonzero array shorter than
`n`, append arbitrary nonzero entries until its length is exactly `n`; all old
witnesses remain.  Therefore enforcing every one of the 465 entries nonzero
does not change the length-at-most-465 decision problem.

This generator is for `nu(11)`, not directly for the version that must also
represent zero.  A literal zero must be prepended to a SAT output to obtain
the original full array, giving total length 466.

## 7. Full soundness and completeness theorem

### Soundness

Read a satisfying assignment's `A[p,b]` values as the array.  Every entry is
nonzero.  For every one of the 2047 nonzero targets, Lemmas 1--2 give a legal
nonempty bounded interval and Section 3 proves that its OR equals the target.
Therefore the output array is universal for all nonzero masks.

### Completeness

Take any universal array of length at most 465, delete zeros, and append
nonzero entries if necessary to reach length 465.  For every target choose a
witness satisfying `safe_bound`, which exists by Lemmas 3--4.  Set its
threshold, membership, and occurrence variables as in Sections 2--3.  The
rank-five and rank-six starts and ends are distinct by Lemma 7, so their
transition variables and sequential-counter auxiliaries can be assigned by
Lemmas 5--6.  This extends the array to a satisfying assignment.

Thus formula satisfiability is exactly the unrestricted existence question.

## 8. Independent size accounting

The reported counts were reproduced algebraically from the source.

### Variables before endpoint materialization

There are `465*11=5,115` array-bit variables.  Every target contributes
`465*(3+rank(target))` threshold/membership/occurrence variables.  Since

```text
sum_{nonzero S subseteq [11]} |S| = 11*2^10 = 11,264,
```

the total is

```text
5,115 + 465*(3*2,047 + 11,264) = 8,098,440.
```

### Endpoint variables

Starts and ends contribute

```text
2 layers * 462 targets * 465 positions * 2 endpoints = 859,320.
```

There are

```text
2 layers * 465 positions * 2 endpoint kinds = 1,860
```

at-most-one groups.  A 462-literal group uses 461 prefix variables, giving

```text
1,860*461 = 857,460.
```

Hence the actual highest variable identifier is

```text
8,098,440 + 859,320 + 857,460 = 9,815,220.
```

The two-million-variable reservation leaves 283,220 identifiers of margin.

### Clauses

The array, interval, and exact-OR clauses before length pruning total
`20,481,216`.  The rank table in Section 4 contributes 824,318 length clauses,
giving

```text
21,305,534
```

clauses before endpoint materialization.

For one target and one endpoint kind, the transition definitions use

```text
2 + 3*(465-1) = 1,394
```

clauses.  Across 924 central targets and two endpoint kinds this is
`2,576,112` clauses.

The sequential encoding uses `3*462-4=1,382` clauses per group, hence

```text
1,860*1,382 = 2,570,520.
```

The final count is therefore

```text
21,305,534 + 2,576,112 + 2,570,520 = 26,452,166,
```

exactly matching the remote build report.

## 9. Operational caveats and certification protocol

1. The seed array is used only in calls to `solver.phase` and in phase-quality
   counters.  It contributes no logical clause.  A poor or out-of-range seed
   can hurt search quality but cannot remove or create satisfying arrays.
2. The program checks only the seed's length, not its value range, and it does
   not check whether the output file opened successfully.  These are CLI
   robustness issues, not defects in the `k=11,n=465` formula.
3. The special endpoint materialization is intentionally hard-coded to
   `k=11` and ranks five and six.  The certification in this report should not
   be extrapolated to arbitrary command-line parameters without a separate
   audit of input ranges and arithmetic overflow.
4. A SAT output should be checked by an independent exhaustive or suffix-OR
   verifier before being promoted as a construction.  Such verification is
   cheap compared with the SAT run and removes dependence on model extraction.
5. For an UNSAT theorem, run a proof-producing version of the same clauses,
   save the exact CNF/source hash and solver command, and independently verify
   the DRAT/LRAT certificate.  Without this step, `UNSAT` is a solver result,
   not a portable mathematical certificate.

## 10. Final audit classification

| Component | Verdict |
|---|---|
| Unary endpoint/interval encoding | Sound and complete |
| Exact OR encoding | Sound and complete |
| `safe_bound` pruning | Globally valid and completeness-preserving |
| Rank-5/rank-6 endpoint auxiliaries | Exact and mathematically redundant |
| Sequential at-most-one clauses | Sound and complete |
| Nonzero-entry constraint | Without loss of generality for `nu(11)` |
| Reported variable counts | Reproduced exactly |
| Reported clause count | Reproduced exactly |
| SAT model implication | Globally valid after independent output check |
| Formula-UNSAT implication | Globally valid |
| Current plain CaDiCaL `UNSAT` log | Not independently certified without proof trace |

**Overall verdict:** `exact_or_sat_direct.cpp` is an exact, globally
unrestricted `k=11,n=465` decision encoding.  No mathematical restriction was
found that would make a SAT result or a proof-checked UNSAT result apply only
to a narrower construction family.
