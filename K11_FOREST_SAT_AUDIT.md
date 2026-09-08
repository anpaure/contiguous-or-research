# Independent audit of the unrestricted `k=11,n=465` forest SAT formula

## Verdict

I independently audited `K11_FOREST_SAT_DESIGN.md` and
`k11_forest_sat.cpp` against the original nonzero problem.  The formulation is
sound and complete:

\[
  \texttt{k11\_forest\_sat.cpp is SAT}
  \quad\Longleftrightarrow\quad
  \nu(11)\le 465.
\]

Together with the proved lower bound `nu(11) >= 465`, a SAT model would prove
`nu(11)=465` (and hence full-problem length `N(11)=466` after inserting one
literal zero).

I found no logical scope loss, off-by-one error, variable collision, or CNF
polarity error.  In particular, the formula does **not** assume a fixed row,
Hamilton path, Johnson adjacency, or a particular endpoint regime.  The
two-coloured forest clauses are redundant consequences of physical interval
containment and therefore cannot remove a genuine solution.

The exact generated inventory, before any solver-internal variables, is

```text
variables = 4,892,622
clauses   = 15,524,818
```

The program reports these totals when run in build-only mode.  The arithmetic
derivation appears in Section 8 below.

## 1. Monotone-band normal form

For either central rank, select one witness for each of the

\[
 M={11\choose5}={11\choose6}=462
\]

targets and sort the witnesses by left endpoint.  Two distinct equal-rank
witnesses cannot share a left endpoint: intervals with the same left endpoint
are nested, so their OR masks would be comparable.  The same argument applies
to right endpoints.  When left endpoints increase, right endpoints must also
increase, because a reversal would again produce containment.

Thus the left and right endpoints are increasing `M`-subsets of the `N=465`
physical positions.  In zero-based indexing their `i`-th elements obey

\[
  i\le \ell_i\le i+3,\qquad i\le r_i\le i+3.
\]

Writing `alpha_i=ell_i-i` and `beta_i=r_i-i` gives exactly the ten states
enumerated in `STATES`.  Strict growth of `ell_i` and `r_i` is equivalent to
nondecreasing `alpha_i` and `beta_i`.  The adjacent-state clauses implement
this condition exactly: they forbid a next state if either coordinate
decreases.  Because exactly one state is selected at every slot, transitivity
then handles all nonadjacent pairs.

There is no missing endpoint state and no out-of-range array access: for the
last slot `i=461`, the largest endpoint is `461+3=464=N-1`.

## 2. Rank-five width-three pruning

This pruning is globally valid and is not a fixed-row assumption.

Choose the 462 rank-six witnesses and put them in monotone-band order.  Each
chosen interval `J_i` lies in `[i,i+3]`.  Every physical interval `[a,b]` of
length at least four has `a<=461` and contains

\[
  J_a\subseteq[a,a+3]\subseteq[a,b].
\]

Its OR therefore has rank at least six.  Consequently **every** interval whose
OR has rank five has length at most three.  In the ten-state band the only
length-four state is `(0,3)`, so the single clause forbidding that state in the
rank-five row is exact.

The rank-six row correctly retains `(0,3)`: its own equal-rank bound is
`N-M+1=4`.

## 3. Conditional central ORs and cardinalities

For selected state `z=(alpha,beta)` and central bit `c`, the generator emits

```text
(-z OR -c OR A[i+alpha] OR ... OR A[i+beta])
(-z OR -A[p] OR c)                  for every p in the interval.
```

Under `z`, these clauses are exactly

\[
 c\leftrightarrow\bigvee_{p=i+\alpha}^{i+\beta}A_{p,b}.
\]

Exactly one state is true, so every central `C[i,b]` is constrained.  The
subset clauses implement exact cardinality correctly:

* all `(rank+1)`-subsets are forbidden from being simultaneously true;
* all `(K-rank+1)`-subsets are forbidden from being simultaneously false.

Hence the lower and upper central values have ranks exactly five and six.

## 4. Why the `Q` variables force permutations

For target mask `S`, `Q[i,S]` implies that all bits of `S` occur in `C_i`.
Because both have the same prescribed rank, this implication already forces
`C_i=S`; explicit negative-bit implications are unnecessary.

A slot cannot support two distinct targets, since their union would contain
more than `rank` bits.  Every one of the `M` targets has at least one supporting
slot, and there are only `M` slots.  Pigeonhole therefore forces exactly one
target per slot and exactly one slot per target.  Multiple support for one
target would require more than `M` occupied slot-target incidences and is
impossible.  Thus the two central rows are permutations without pairwise
all-different clauses.

## 5. Forest strengthening

The source examines every pair of central slots that could share an endpoint.
The range `j in [i-3,i+3]` is exhaustive because both offsets lie in `[0,3]`.

If a rank-five and rank-six interval share a left endpoint, physical
containment permits only

\[
 r_5<r_6,\qquad C^5\subset C^6.
\]

The other ordering would imply that a six-set is contained in a five-set, and
equal right endpoints would give the same physical interval two different
ranks.  The right-endpoint case is dually

\[
 \ell_6<\ell_5,\qquad C^5\subset C^6.
\]

The emitted forbid/inclusion clauses exactly express these consequences.
They are redundant with the conditional physical OR equations and exact
cardinalities, so they are safe propagation clauses.

Internally each endpoint list is strictly increasing, so each colour is a
matching.  Equality matching between two sorted endpoint lists is
order-preserving.  Two order-preserving matchings on the same two ordered
vertex classes cannot form an alternating cycle unless the same pair receives
both colours; that case would be an identical interval and is forbidden as
above.  The induced graph is therefore a spanning linear forest.  Since two
462-subsets of a 465-set intersect in at least 459 elements, each matching has
at least 459 edges and the forest has at most six components.  These properties
are implied rather than separately asserted, which is logically sufficient.

## 6. Direct noncentral witnesses

The threshold encoding is exact:

* `L[p]` is a monotone false-to-true threshold and `L[N-1]` is true;
* `R[p]` is a monotone true-to-false threshold and `R[0]` is true;
* the three clauses per position give `Inside[p] <=> L[p] AND R[p]`;
* `some_inside` makes the interval nonempty;
* `(-Inside[p] OR -Inside[p+bound])` enforces length at most `bound`;
* absent target bits are excluded at every inside position;
* for each present bit, an occurrence variable selects an inside array
  position containing it.

Consequently the selected interval has OR exactly the target.

The implemented bound

\[
 \Lambda(s)=\min\left(N-{11\choose s}+1,
              \min_{r>s}\left(N-{11\choose r}\right)\right)
\]

has the right off-by-one conventions.  The same-rank term is `d+1`, because a
selected equal-rank witness lies inside `[i,i+d]`; the higher-rank term is `d`,
because every interval of length `d+1` already contains a selected higher-rank
witness.  For the direct ranks the values are

```text
rank       1  2  3  4    7    8    9   10   11
Lambda     3  3  3  3  136  301  411  455  465
```

All are positive, so the phase helper never encounters an empty search range.

## 7. Soundness and completeness audit

### Soundness

Read the `465*11` array variables as nonempty masks.  Sections 3--4 give a
physical exact witness for every rank-five and rank-six target.  Section 6
gives one for every other nonzero target.  Hence a SAT model is a universal
nonzero array.

### Completeness

Take any universal array of length 465.

1. It contains no zero entry: deleting a zero preserves all nonzero interval
   ORs and would contradict the proved lower bound 465.
2. Select bounded direct witnesses using the rank-slack theorem.
3. Select one witness per rank-five and rank-six target and sort each family.
   Section 1 gives the represented schedules; Section 2 gives the extra
   rank-five pruning.
4. Set each central value to its physical OR and set the corresponding `Q`.
5. Every forest clause holds by physical containment, as shown in Section 5.

This extends the array assignment to every CNF variable.  No central
Hamiltonicity, Johnson adjacency, fixed-window derivative, or chosen forest
component structure is required.

## 8. Independent exact inventory

The array contributes `465*11=5,115` variables.  The 1,123 direct targets
contribute

\[
 \sum_{s\in\{1,2,3,4,7,8,9,10,11\}}
 {11\choose s}\,465(3+s)=4,441,215.
\]

Each central layer contributes

```text
states       462*10  =   4,620
value bits   462*11  =   5,082
Q variables  462^2   = 213,444
total                  223,146
```

so the grand total is

```text
5,115 + 4,441,215 + 2*223,146 = 4,892,622 variables.
```

For clauses, the independent category totals are

```text
array nonzero                         465
direct witnesses              11,634,947
rank-five central layer        1,607,298
rank-six central layer         1,820,280
central schedule monotonicity     46,100
central target occurrence            924
forest propagation                414,804
                                   -------
total                           15,524,818
```

The forest loop encounters 46,092 possible shared-left state pairs and the
same number of shared-right pairs.  In each colour, 29,961 pairs are forbidden
and 16,131 legal pairs emit eleven inclusion clauses.  This gives

\[
 2(29,961)+22(16,131)=414,804.
\]

## 9. Operational caveats, not logical defects

* `forest_cases_LR` counts possible state-pair cases, not edges selected in the
  eventual model.  This affects only interpretation of the diagnostic.
* The input seed controls solver phases only.  A bad seed cannot remove models.
* The program writes the SAT array but does not itself perform the independent
  suffix-OR and exhaustive checks.  Any claimed certificate must still be run
  through both project verifiers and archived with its SAT model/log.
* Build with C++20, because the source uses `std::popcount`.

These caveats do not alter the SAT iff theorem.

## 10. Independent build-only check

The audited source was also compiled independently with GCC in C++20 mode
against CaDiCaL and run in build-only mode on a RunPod (not on the local Mac).
Using `k11_phase465.txt` only for phase initialization, it printed

```text
variables=4892622 clauses=15524818 direct_targets=1123
exact_direct_phase=1072/1123 exact_central_phase=0,1
forest_cases_LR=46092,46092
BUILD_ONLY
```

This exactly matches the independent arithmetic above.  The phase counts are
not logical constraints and do not affect completeness.

Audited source hashes at the time of this check:

```text
1e0e296be7ec73bb930e23d474b3dfd0f867bdc1617d24ce7ee19bc3c731c33d  K11_FOREST_SAT_DESIGN.md
fe25299907e8a4bf641f6034d9fa268a85cf4c91bfb1c7cdc8a37ca49e933496  k11_forest_sat.cpp
```

These hashes include the subsequent optional proof/CNF archival hooks audited
below.

## 11. Audit of the proof and DIMACS hooks

The optional operational amendment does not change the formula.

* `K11_FOREST_PROOF` calls `trace_proof(path)` after options/variable
  declaration but before either clause helper is used.  CaDiCaL requires proof
  tracing to begin in its `CONFIGURING` state, before the first `add`, `dimacs`,
  or `solve`; this ordering is correct.  A failure to open the trace terminates
  with exit code 6 rather than silently running without a proof.
* `K11_FOREST_DIMACS` calls `write_dimacs(path, variable_total)` after all
  clauses and before either build-only return or `solve`.  The second argument
  is CaDiCaL's documented lower bound for the DIMACS header's maximum external
  variable, so all 4,892,622 declared external variables are retained even if
  some happened not to occur.  A write error terminates with exit code 7.
* Both variables are optional and empty values are ignored.  With neither set,
  control flow and every added clause are identical to the audited version.
* The real-CaDiCaL rebuild still reports exactly 4,892,622 variables and
  15,524,818 clauses, confirming that the amendment added no CNF clauses or
  auxiliary variables.

For an archival run, the proof path, DIMACS path, seed path, and output path
should of course be distinct.  This is an operational precondition rather
than a CNF-scope issue.
