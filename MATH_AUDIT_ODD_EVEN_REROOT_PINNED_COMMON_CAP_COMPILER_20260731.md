# Referee audit: odd-to-even reroot, pinned schedule, and common-cap compiler

Date: 2026-07-31  
Audited note: `MATH_THEOREM_ODD_EVEN_REROOT_PINNED_COMMON_CAP_COMPILER_20260731.md`  
Verdict: the K16 corollary is certified, and the common-cap/composition core
and variable-staircase recurrence are sound.  The note is **not** an all-`k`
construction.  An earlier draft of Lemma 4.1 omitted its baseline-exactness
hypothesis; the audited theorem now includes that repair.

## 1. Uniform statements that are proved

The following statements are dimension-free.

1. **Two-shore ownership (Lemma 2.1).**  If the two shore lists are already
   exact enumerations, any interleaving/orientation still enumerates the even
   middle layer exactly.  This says nothing about adjacency, shadows,
   residence, or the existence of the shore lists.
2. **Boundary localization (Lemma 3.1).**  Block reversal preserves the set of
   internal interval ORs; every change is localized to intervals crossing a
   new seam.  This is an audit reduction, not an existence theorem.
3. **Seam-cost identity (Lemma 4.2).**  For complement start/deadline sets,
   the proper-prefix area is exactly
   `sum(X)-sum(Y)`.  It does not count omitted-start boundary cells.
4. **Lower-cell necessity (Section 5).**  A lower-rank witness cannot contain
   a complete middle interval, and distinct lower targets need distinct
   physical cells.
5. **Maximal common cap (Theorem 6.1).**  Conditional on a fixed injective
   target-to-cell assignment, the coordinatewise maximal common cap is a
   realizing word iff its letters are nonempty and all middle/lower OR
   equations hold.
6. **Cartesian-Hall factorization (Theorem 6.2).**  A compiler exists iff a
   Cartesian edge bank contains a matching saturating all lower targets.
   This is exact but existential: constructing the Cartesian bank may be the
   hard part.
7. **Boolean formulation and finite matching-only CEGAR (Section 7).**  The
   `y/q` formulation is sound and complete relative to the retained candidate
   graph.  A negative theorem requires the graph to be complete; a positive
   certificate may use any sound subgraph.
8. **Upper transfer (Lemma 8.1).**  Exact middle rows transfer consecutive-row
   upper witnesses to literal word intervals when the schedule is
   chain-aligned.
9. **Composite construction (Theorem 8.2).**  Its five displayed hypotheses
   imply a universal word; combined with the independent deadline lower bound
   they imply equality.

## 2. Correction applied to Lemma 4.1

The earlier statement of Lemma 4.1 was false.  Equation (4.4) checks only
rows containing the capped position, so it cannot ensure that unchanged rows
were realized by the uncapped maximal envelope.

A counterexample uses positions `0,...,5`, intervals

```
I0=[0,3], I1=[1,4], I2=[2,5]
```

and targets

```
T0={x,a}, T1={x,b}, T2={x,c}.
```

Starts and deadlines are strictly increasing.  The maximal envelope equals
`{x,a}` at 0, `{x,c}` at 5, and `{x}` at every other position.  Cap position
0 to `C=E0`.  Equation (4.4) holds for the only row containing position 0
that needs checking, but row `I1` has OR `{x}`, not `{x,b}`.

The current repaired statement is:

> Assume first that the uncapped maximal envelope realizes every middle row
> (or, equivalently for this one-position change, assume every row not
> containing `p` is exact).  Then the capped envelope realizes all rows iff
> (4.4) holds for every row containing `p`.

Corollary 4.3 now likewise says “cap `C={z}` at `p`”, rather than the
ambiguous “cap `E_p={z}`”, and invokes the repaired lemma.  Theorem 8.2
already assumed the capped envelope exact, so this repair did not affect its
validity or K16.

## 3. K16-only facts

The following are finite statements authenticated for the displayed parent,
reroot, and schedule; none follows uniformly from the preceding lemmas.

1. The K15 parent has a complete rank-eight four-letter deck and a
   three-letter deck consisting of every rank-seven mask plus exactly one
   rank-six exception.
2. Deleting that exception gives the two exact K16 shore lists.
3. The two specific endpoint reversals preserve all old upper witnesses and
   install all six formerly missing upper masks.
4. The three-hole schedule
   `X=(12870,12871,12872)`, `Y=(0,1,6388)` is legal and chain-aligned.
5. Capping position 6389 to `0x8000` leaves all 12,870 middle rows exact.
6. The full lower catalogue has 32,230 cells.  After reserving the singleton,
   it has 26,331 targets, 32,229 cells, and 347,677 incidences.
7. The joint common-cap CNF is SAT.  The fail-closed independent model replay
   reconstructs a word with SHA
   `890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe`;
   direct literal replay covers all 65,535 nonempty masks.
8. The independent lower bound is 12,873.  Therefore `nu(16)=12873`.

The last item needs none of the SAT lineage once the literal word is retained.

## 4. Dependency graph

```text
K15 derivative-deck facts -- Lemma 2.1 --> exact natural K16 ownership
                                                  |
specific endpoint reroots -- Lemma 3.1 + replay --+--> upper-complete T*
                                                  |
schedule DP -- Lemma 4.2 ------------------------> optimal-length schedule
                                                  |
pin search -- corrected Lemma 4.1 --------------> exact capped envelope
                                                  |
catalogue identity (Section 5) ------------------> complete C_full
                                                  |
joint SAT -- Theorem 6.1 / Section 7 ------------> lower + middle word Q
                                                  |
chain alignment + Lemma 8.1 + upper-complete T* -> all upper masks in Q
                                                  |
literal replay ----------------------------------> universal length 12873
                                                  |
deadline lower bound ----------------------------> nu(16)=12873
```

For a uniform odd-to-even induction the corresponding open chain is:

```text
uniform odd source
  -> exact two-shore derivative lists
  -> upper-complete rethread
  -> chain-aligned length-(W+d(k)) pinned schedule
  -> Cartesian lower bank / exact common-cap feasibility
  -> even optimum.
```

The note contains no construction of the first node for every odd `k`, and
no even-to-odd step.  Consequently even a uniform proof of the four K16-style
arrows would not by itself prove the formula for all `k`.

## 5. Minimal missing uniform hypotheses

For equality in every dimension, the truly minimal existence input is:

1. **Odd source theorem.**  For every required odd predecessor, construct a
   source whose adjacent derivative rows give exact even shores after an
   explicitly controlled deletion/replacement operation.  “Controllably many
   exceptions” is insufficient unless their ownership is repaired exactly.
2. **Upper rethread theorem.**  Reorder/orient that shore deck so every upper
   target is the OR of a consecutive middle block.  Boundary localization
   only makes this check finite; it gives no bound or existence guarantee.
3. **Optimal schedule-and-pin theorem.**  At length `W+d(k)`, produce a
   chain-aligned schedule and all required positional caps with nonempty exact
   middle envelope.  Increasing starts/deadlines alone does not imply chain
   alignment.
4. **Uniform Cartesian-Hall/common-cap theorem.**  Produce an injective lower
   assignment satisfying Theorem 6.1, or a Cartesian edge bank satisfying
   Hall, for the complete lower family.  Marginal Hall and scalar area are
   only necessary filters.

For a merely existential theorem, the number of exceptions or reroot seams
need not be bounded; boundedness is an algorithmic/explicit-construction
strengthening, not a logical requirement.

## 6. Counterexamples and scope warnings

1. **Monotone does not imply chain-aligned.**  `I0=[0,0]` and `I1=[2,2]`
   have increasing starts and deadlines, but their union is disconnected.
2. **Marginal Hall does not imply compatibility.**  Let one middle row
   `I={1,2,3}` have target `{a,b}` and envelope `{a,b}` at all positions.
   Give lower target `{a}` only cell `{1,2}` and lower target `{b}` only cell
   `{2,3}`.  The two-edge graph has a perfect matching and each edge is
   individually feasible, but position 2 would have to be both `{a}` and
   `{b}`; its common cap is empty.
3. **Upstream carrier gates do not force compilation.**  The recorded K9
   protected three-component factor passed its cyclic palette/shadow gates,
   yet all 96,228 openings failed the exact compiler.  Thus the uniform
   common-cap hypothesis cannot be deleted (the positive-slack regime may be
   better, but that is still a theorem to prove).
4. **“Canonical” is matching-relative.**  `A(M)` is canonical after `M` and
   the positional caps are fixed; there is no canonical matching or global
   source word supplied by Theorem 6.1.
5. **K16's constants are not structural constants.**  Three omitted
   starts/deadlines, one exceptional shore entry, two reroot boundaries, and
   one singleton pin are all finite K16 data.  Since `d(k)` grows, none may be
   imported unchanged into an all-`k` induction.

## 7. Referee conclusion

With Lemma 4.1 repaired, the reusable theorem is accepted as an exact
**conditional reduction** and the K16 corollary as a certified finite
theorem.  It must not be advertised as an all-`k` proof.  The hard uniform
content has been isolated rather than eliminated: exact shore production,
upper-safe rethreading, optimal chain-aligned pinning, and simultaneous
Cartesian-Hall/common-cap feasibility, plus an independent construction for
the odd dimensions.

## 8. Variable-staircase and arbitrary-P/Q addendum

Section 11 was audited separately from the K16 certificate.

1. The map from a nondecreasing threshold vector to omitted deadlines is a
   bijection on the tail-start subclass, with inverse
   `a_j=y_j-j+1`.  It is not a normal form for arbitrary P/Q schedules.
2. For arbitrary legal omitted sets `X,Y`, let `c(t)` be the deadline of the
   first owner whose start is at or after `t`, or `L` if there is none.  The
   exact cells beginning at `t` are `[t,u]` with `t<=u<c(t)`.  Consequently

       A = sum(X)-sum(Y),
       B = sum_{x in X}(c(x)-x),
       |C_full| = A+B.

   The first term is selected-start proper-prefix area; the second is the
   literal omitted-start boundary contribution.  An automatic triangular
   credit for arbitrary omitted starts would be unsound.
3. With `Y={y_1<...<y_d}`, the exact loss and surplus invariants are

       ell(X,Y) = sum_{x in X}(L-c(x))
                  + sum_j(y_j-(j-1)),
       |C_full| = d M + binom(d+1,2) - ell(X,Y),
       Omega_k = sigma_k - ell(X,Y).

   Tail starts have `ell=sum_j a_j`.  Pin contraction removes one distinct
   target and one distinct cell per pin, so it preserves this raw scalar
   surplus.  It does not preserve residual incidences or Hall: domains must
   be rebuilt after capping, and multi-cell pin equalities remain guarded.
4. Direct substitution proves the odd/even recurrences for
   `(d_k,sigma_k)`.  The depth changes by at most one: odd-to-even keeps or
   deletes one threshold, and even-to-odd keeps or adds one.
5. The recursive seam prescription is an all-`k` accounting/obligation
   schema, not a closure theorem.  The recurrence supplies only the child
   depth and scalar budget; it transports no chronology, omitted sets, pins,
   upper witnesses, Hall matching, or common cap.

The K16 state has area `32224`, boundary contribution `6`, 32,230 cells and
surplus 5,898; contracting its singleton gives 32,229 cells for 26,331
targets with the same surplus.  The carrier-free K17 forecast has

    (M,Lambda,d,sigma)=(24310,65535,3,7401),
    a=(0,0,7401), X=(24310,24311,24312), Y=(0,1,7403),
    p=7404, A=65529, B=6, |C_full|=65535, Omega=0.

Thus any legal one-cell pin would leave 65,534 residual cells for 65,534
targets; every residual cell would have to be used.  This proves no K17
carrier, pin, upper replay, Hall matching, or common cap.

The deterministic audit checks every transition through `k=1000`, all 1996
small tail-start catalogues, 5,223 legal arbitrary-omission catalogues, 144
one-pivot endpoint cases, and the K15--K17 calibration.  It reports PASS
with the hashes recorded in the audited theorem's certificate-reference
section.
