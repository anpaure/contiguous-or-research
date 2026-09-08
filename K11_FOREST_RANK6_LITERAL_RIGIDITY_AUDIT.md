# Independent audit of rank-six literal rigidity at `k=11,n=465`

## Verdict

**PASS.**  The three array-level conclusions in
`K11_FOREST_RANK6_LITERAL_RIGIDITY.md` are valid:

1. at most one distinct rank-six mask occurs literally;
2. every occurrence of that mask is at physical position 0 or 464;
3. the two endpoints cannot both be rank-six entries.

It follows that there is at most one literal rank-six occurrence.  Reversal
and coordinate permutation then give the stated existence normal form:

```text
no rank-six literal anywhere,
or A[0]=63 and no other rank-six literal.
```

The complete mismatch-clause inventory is exactly 214,829 clauses and zero
variables.  I found no counterexample based on repeated occurrences of the
same mask, deliberate witness reselection, or endpoint deletion/reindexing.

The important scope qualification is also correctly stated in the source
note: canonical-left is a satisfiability-preserving symmetry representative,
not a coordinate-labelled necessary condition on an already oriented array.

## 1. Frozen material inspected

```text
082029ee18af016b4cda7564533280b9c60985980bf9abb6b5f756b890b2535e
    K11_FOREST_RANK6_LITERAL_RIGIDITY.md

1172c55d5ab21f829af8263cb5cc13e65dec0179c5a50159ed3c1b064ba21c81
    k11_forest_sat.cpp

7d7f63f5deaaae29d933897ae71748c75ff24a6b46b2d74c51d388d4709e35cc
    scratch/verify_k11_rank6_boundary_entry_implementation.cpp
```

The proof depends on two previously proved statements, each quantified over
**every independently chosen** rank-five/rank-six witness family:

* the upper singleton count satisfies `x0<=1`;
* the upper width-three count satisfies `x3>=93` (indeed the stronger
  `x3>=93+2*x0` is available).

It also uses the unrestricted monotone-band normal form for 462 selected
equal-rank intervals in 465 positions.

## 2. Audit of the witness-reselection quantifier

### Two distinct literal masks

Suppose distinct six-sets `S` and `T` occur at positions `p` and `q`.  Choose
`[p,p]` as the selected witness for target `S` and `[q,q]` as the selected
witness for target `T`.  Select one arbitrary witness for each remaining
rank-six target and independently for each rank-five target.

This is a legitimate selected family.  Any two selected intervals for
distinct equal-rank targets are automatically nonnested: containment of
physical intervals would imply containment of their OR masks, impossible for
two different masks of the same cardinality.  Thus no extra compatibility
choice is hidden in the word "arbitrarily."

The deliberately selected family has at least two singleton targets, so
`x0>=2`, contradicting the universally quantified theorem `x0<=1`.  Hence all
literal rank-six entries, if any, have one common mask `C`.

### Repeated occurrences of the same mask

Repeated occurrences do not evade the next step.  Fix **one particular**
occurrence `A[p]=C`, select `[p,p]` for target `C`, and select all other target
witnesses afresh.  The upper family then has `x0=1`; a second occurrence of
`C` is irrelevant because only one witness is selected for target `C`.

No other selected rank-six target can be forced to use position `p`.  Any
interval containing `p` has OR containing `C`; if that OR is another six-set
`T`, then `C subseteq T` and equal cardinality imply `T=C`.  Thus deliberate
reselection creates no obstruction in the remaining target choices.

Most importantly, the `x0<=1`, width-three, and band theorems apply again to
this newly selected family.  The argument may therefore be repeated
separately for every occurrence.  It does **not** need all repeated
occurrences of `C` to be selected simultaneously.

This closes the main quantifier issue.

## 3. Boundary localization

Sort the deliberately selected rank-six intervals by left endpoint and write

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad 0\le\alpha_i\le\beta_i\le3,
\]

with both offset sequences nondecreasing.  Since `x3>=93`, state `03` occurs.
A width-zero state has the form `aa`.  In a coordinatewise monotone sequence,
a width-zero state coexisting with `03` must be

```text
00 before 03, or 33 after 03.
```

States `11` and `22` are incomparable with `03` and therefore cannot occur in
the same monotone schedule.

Because `x0<=1` and the chosen occurrence supplies one singleton, the width-
zero block has exactly one member.  A sole `00` must be slot `i=0`, giving
`[0,0]`; a sole `33` must be slot `i=461`, giving

\[
 [461+3,461+3]=[464,464].
\]

Thus the deliberately chosen physical position is in `{0,464}`.  Applying
the argument separately to every occurrence rules out every interior repeat
of `C`.

I found no dependence here on a fixed derivative row, connected forest, or
Johnson adjacency.

## 4. Audit of the two-boundary contradiction

Assume both endpoint entries have rank six.  Section 2 already shows that
they have the same mask, although equality is not actually needed for the
following avoidance argument.

An interval whose OR has rank at most five cannot contain either endpoint:
its OR would contain a six-set.  Therefore every target of ranks one through
five has a witness wholly inside

```text
A[1],...,A[463].
```

Deleting the two endpoints and subtracting one from every surviving physical
index preserves contiguity and every relevant OR.  This explicitly resolves
the possible endpoint-shift concern.

In the reindexed 463-position word choose one witness for each of the 462
rank-five masks.  Equal-rank nonnesting makes both endpoint lists strictly
increasing.  They are 462-subsets of a 463-position universe, so their `i`th
members satisfy

\[
 i\le l_i\le r_i\le i+1,
 \qquad 0\le i\le461.                            \tag{1}
\]

Now let `[a,b]` be any interior interval of length at least two.  Necessarily
`a<=461`, and (1) puts the selected rank-five interval `I_a` inside
`[a,a+1] subseteq [a,b]`.  Hence the OR of `[a,b]` contains a five-set and has
rank at least five.

Every target of ranks one through four must consequently occur as a singleton
entry.  There are

\[
 {11\choose1}+{11\choose2}+{11\choose3}+{11\choose4}
 =561
\]

distinct such targets but only 463 singleton positions.  One position has
one fixed OR value, so this is impossible.

The contradiction is unaffected by duplicate array values, zeros, or the
fact that witnesses were chosen after deletion.  In particular, no hidden
claim that the original selected endpoints remain numerically unchanged is
being used; the band theorem is reapplied to the reindexed interior family.

## 5. Reversal and coordinate WLOG

With at most one occurrence established:

* if it is at position 464, reversal moves it to position 0;
* if its mask is the six-set `C`, a permutation of the eleven coordinates
  maps `C` to `{0,1,2,3,4,5}`, decimal 63;
* if no rank-six literal occurs, every rank-six-forbidding mismatch clause is
  already satisfied.

Reversal preserves the family of contiguous intervals, while a coordinate
permutation commutes with OR and bijects all target masks.  Therefore the
normal form preserves existence.

As usual, this symmetry break must be composed only with hard constraints
that are invariant under the same action or whose auxiliary witnesses can be
rebuilt after applying the action.  In the inspected solver, seeds affect
phases only; the exact target families and the guarded structural cuts are
coordinate-equivariant and are necessary for every rebuilt witness family.
No independent hard left/right orientation break was found.  A future such
break would require a new joint-stabilizer audit.

## 6. Exact CNF inventory

There are

\[
 {11\choose6}=462
\]

rank-six masks.  The canonical-left gate forbids:

* at position 0, the 461 masks other than 63;
* at each of positions 1 through 464, all 462 rank-six masks.

Thus its exact clause count is

\[
 461+464\cdot462
 =461+214368
 =\boxed{214829}.                                \tag{2}
\]

Each clause is one eleven-literal mismatch clause and introduces no variable.
The corresponding literal-occurrence count is

\[
 214829\cdot11=2363119.                           \tag{3}
\]

The already implemented coordinate-canonical gate contributes

\[
 465\cdot461=214365
\]

of these clauses.  The additional canonical-left delta is exactly the 464
clauses forbidding mask 63 at positions 1 through 464.  The two clause
families are disjoint in `(position,mask)` space.

The current source reflects this distinction correctly:

```text
canonical gate alone:              214365 clauses
boundary delta with canonical on:      464 clauses
combined canonical-left total:     214829 clauses
```

With the canonical option off, the standalone boundary option emits
`463*462=213906` coordinate-labelled necessary clauses forbidding rank-six
entries only at positions 1 through 463.  It deliberately leaves both
physical endpoints available; this standalone branch is sound but is not by
itself the complete canonical-left normal form.

## 7. Counterexample attempts

| attempted escape | result |
|---|---|
| two different literal six-sets | reselect both singleton witnesses, contradicting `x0<=1` |
| repeated interior copies of one six-set | reselect each copy separately; every chosen copy localizes to a boundary |
| same six-set at both endpoints | the 463-position interior would need 561 distinct lower singleton values |
| deletion changes witness endpoints | reindex and reapply the equal-rank band theorem; no old numeric index is reused |
| sole occurrence at the right endpoint | reversal gives the canonical-left representative |
| no literal rank-six entry | all canonical-left mismatch clauses remain satisfied |
| sole noncanonical mask | coordinate permutation maps it to 63 |

None yields a counterexample.

## 8. Mechanical cross-check

The supplied checker was compiled independently with GNU C++ 15 and `-O3`:

```text
/opt/homebrew/bin/g++-15 -O3 -std=c++20 -Wall -Wextra -pedantic \
  scratch/verify_k11_rank6_boundary_entry_implementation.cpp \
  -o /tmp/verify_k11_rank6_boundary_entry
/tmp/verify_k11_rank6_boundary_entry
```

Observed output:

```text
small_boundary_gate=PASS
small_canonical_interaction=PASS
k11_boundary_plain_variables=0 clauses=213906 literals=2352966
k11_boundary_with_canonical_variables=0 clauses=464 literals=5104
duplicate_interaction_clauses=0
```

The small test exhausts every local value/position interaction.  The proof in
Sections 2--6, rather than the finite checker, establishes the full theorem.

## Final assessment

The theorem and the 214,829-clause complete canonical-left inventory pass.
Repeated same-mask occurrences and endpoint deletion do not expose a logical
gap.  The only material caution is categorical: the 214,829 clauses are the
**combined total** of the coordinate-canonical gate and its 464-clause
left-boundary refinement, not an additional 214,829-clause delta on top of
the old gate.
