# Exact unrestricted `k=11,n=465` forest/band SAT design

## Status

This note gives an exact SAT formulation for the original array problem at
`k=11,n=465`.  It is **not** restricted to a fixed derivative row.  The
implementation is `k11_forest_sat.cpp`.

The first implementation deliberately retains the already-audited direct
witness encoding away from ranks five and six.  Its purpose is to remove the
largest avoidable part of `exact_or_sat_direct.cpp` while keeping the proof of
exactness short.  The central two layers are represented in the globally
necessary monotone-band/two-coloured-forest normal form.

## 1. WLOG central coordinates

Put

\[
 n=465,\qquad M={11\choose5}={11\choose6}=462,\qquad d=n-M=3.
\]

In each central rank `s in {5,6}`, choose one witnessing interval for every
`s`-set and sort the intervals by increasing left endpoint.  Equal-rank
incomparability makes both endpoint lists strictly increasing.  Consequently

\[
 I^s_i=[i+\alpha^s_i,i+\beta^s_i],\qquad 0\le i<M,
\]

where

\[
 0\le\alpha^s_0\le\cdots\le\alpha^s_{M-1}\le3,
 \quad
 0\le\beta^s_0\le\cdots\le\beta^s_{M-1}\le3,
 \quad \alpha^s_i\le\beta^s_i.
\]

Thus every slot has one of only ten states `(alpha,beta)`.  This is a theorem
about every possible length-465 solution, not a fixed-row ansatz.
Moreover, the rank-six layer gives the exact witness-length bound three for
every rank-five mask, so the single width-three state `(0,3)` may be forbidden
in the rank-five schedule.  Rank-six slots retain all ten states.

For every slot introduce eleven bits `C[s,i,b]`, intended to be the OR of its
chosen interval.  Conditional four-cell clauses make

\[
 C^s_i=\bigvee_{p=i+\alpha_i^s}^{i+\beta_i^s}A_p.
\]

Cardinality clauses force `|C^s_i|=s`.  Finally introduce `Q[s,i,S]` for every
slot and every rank-`s` mask.  The clauses

\[
 Q[s,i,S]\Longrightarrow b\in C^s_i\quad(b\in S),
 \qquad \bigvee_iQ[s,i,S]
\]

are sufficient.  Since `C^s_i` has rank exactly `s`, `Q[s,i,S]` implies
`C^s_i=S`.  A slot cannot support two distinct `Q` variables.  There are `M`
targets and `M` slots, so the target clauses automatically make the row a
permutation; no quadratic pairwise all-different clauses are needed.

## 2. The two-coloured forest is present explicitly

The two sorted endpoint schedules define two matchings between the rank-five
and rank-six slots:

* an `L` edge when `i+alpha^5_i=j+alpha^6_j`;
* an `R` edge when `i+beta^5_i=j+beta^6_j`.

Each endpoint list omits only three of 465 positions, so each matching has at
least 459 edges.  For every possible schedule-state pair producing an `L`
edge, the generator requires the rank-five interval to end strictly earlier
than the rank-six interval and adds

\[
 C^5_i\subset C^6_j.
\]

For an `R` edge it analogously requires the rank-six interval to start
strictly earlier and adds the same inclusion.  These clauses are redundant
with the physical interval OR equations, but expose the forest to unit
propagation before array labels settle.

Each colour is a matching, no pair can receive both colours, and alternating
cycles are impossible by strict endpoint growth.  Hence the materialized
graph is exactly the proved spanning linear forest with at most six
components.  No Hamilton-path assumption has been introduced.

## 3. Noncentral masks

For every target of rank other than five or six, the first generator keeps the
sound and complete unary endpoint encoding from `exact_or_sat_direct.cpp`.
Its witness length is bounded by

\[
 \Lambda(s)=\min\left(n-{11\choose s}+1,
                   \min_{r>s}(n-{11\choose r})\right).
\]

The rank-slack lemma proves that every target has a witness within this bound.
Threshold variables select a nonempty interval.  Negative-bit clauses prevent
contamination, while one occurrence variable for every positive bit selects a
position of that bit inside the interval.

This intentionally conservative choice leaves later compression work local:
the central replacement can be audited independently of a new global pinning
encoding.

## 4. Exactness theorem

### Theorem

`k11_forest_sat.cpp` is satisfiable if and only if a universal nonzero
11-bit array of length 465 exists.

### Soundness

Read the `A[p,b]` variables as an array.  Every entry is constrained nonempty.
For a noncentral target, its direct witness clauses give an interval containing
every target bit and no outside bit.  For a central target `S`, its coverage
clause selects a slot with `Q[s,i,S]`; fixed cardinality then gives
`C[s,i]=S`, and the conditional OR clauses give a physical interval with OR
`S`.  Thus every one of the 2047 nonzero masks occurs.

### Completeness

Take any universal length-465 array.  Choose bounded witnesses for all
noncentral targets using exact rank-slack pruning.  In ranks five and six,
choose one witness per mask, sort each family by left endpoint, and set the
band states to its endpoint offsets.  The interval-slack lemma gives offsets
in `[0,3]`, strict endpoint order gives monotonicity, and the interval ORs give
the central bits.  Set the corresponding `Q` variable for every target.  All
forest clauses hold because intervals sharing one endpoint are nested in the
only rank-compatible direction.  This extends to a satisfying assignment.

## 5. Size

The old direct formula has 8,098,440 primary variables before its endpoint
distinctness auxiliaries.  Of these,

```text
rank 5: 462*465*(3+5) = 1,718,640
rank 6: 462*465*(3+6) = 1,933,470
total:                    3,652,110
```

belong solely to central target witnesses.

The replacement uses approximately

```text
schedule states       2*462*10       =   9,240
central OR bits       2*462*11       =  10,164
slot-mask indicators  2*462*462      = 426,888
```

and no endpoint-distinctness auxiliaries for the central ranks.  The resulting
first formula has exactly **4,892,622 variables and 15,524,818 clauses**,
versus 8,098,440 primary variables and 21,305,534 clauses before the old
endpoint-distinctness auxiliaries.  This is a roughly 39-percent variable
reduction before any compression of the other ranks.  These totals were
reproduced by a remote `-O3` CaDiCaL build-only run; set
`K11_FOREST_BUILD_ONLY=1` to reconstruct the formula without launching the
solver.

For a proof-producing run, set `K11_FOREST_PROOF` before launch.  Proof tracing
is enabled before the first clause is added, as required by CaDiCaL.  Set
`K11_FOREST_DIMACS` as well to archive the corresponding external-variable
CNF; an UNSAT result is not promoted without independently checking that
proof/CNF pair.  A SAT result must likewise pass both project OR verifiers.

## 6. Minimal next reductions

The following are exact but are intentionally left out of the first generator
until the central replacement is independently regression-tested.

1. Encode the proved band inequalities

   ```text
   x0 <= 3,
   2*x0+x1 <= 138,
   sum(width_i) >= 1008,
   x3 >= 93.
   ```

   Because the state sequence is monotone, these should use regime-boundary
   integers rather than a large generic pseudo-Boolean counter.

2. Replace ranks one through four by the shared 1/2/3-window OR strip.  All
   those targets are forced into only 1,392 physical intervals.

3. Replace most rank-seven direct witnesses by the forced unions at common
   endpoints.  At least 324 of 330 rank-seven masks arise this way, so only six
   exceptional witnesses need the generic encoding.  The dual compression
   applies to rank four.

4. Ultimately replace all remaining direct target occurrence variables by the
   exact global pin-survival encoding.  This is the point at which the formula
   becomes an ordered triangular orthogonal-chain-pair problem rather than an
   array-first problem.

The first generator is already globally WLOG.  Items 1--4 are performance
improvements, not repairs to its logical scope.
