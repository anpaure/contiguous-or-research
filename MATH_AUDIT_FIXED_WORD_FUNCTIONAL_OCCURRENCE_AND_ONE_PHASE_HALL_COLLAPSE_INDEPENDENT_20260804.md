# Independent audit: fixed-word functional occurrence and one-phase Hall collapse

**Date:** 2026-08-04
**Method:** pure symbolic replay; no computation, search, or solver
**Audited file:**
`MATH_THEOREM_FIXED_WORD_FUNCTIONAL_OCCURRENCE_AND_ONE_PHASE_HALL_COLLAPSE_20260804.md`

## Verdict

**PASS after one typesetting repair.**  The missing display terminator after
equation (0.4) was restored.  The mathematical conclusion is exact in the
declared direct-ray fixed-word model.

## 1. Functional-neighbourhood replay

For one fixed literal word and one interval address `C`, the value
`OR_A(C)` is unique.  Therefore `C` has degree at most one in the graph
whose left vertices are distinct Boolean target values.  For a target set
`Z`, its neighbourhood is the disjoint union of the occurrence fibres of
the members of `Z`.  A present target contributes at least one address; an
absent target contributes none.  The maximum Hall deficiency is therefore
attained by the set of absent targets and equals its cardinality.

## 2. Forced-edge replay

Every forced address `C_i` has value `S_i`.  It cannot simultaneously have
the value of a distinct residual target.  Removing forced addresses hence
removes no neighbour of the residual shore.  The forced matching extends
to a maximum matching by choosing one address for every present residual
value, and it extends to a saturating matching exactly when all residual
values occur.

This also verifies the stronger equality

\[
 \delta(A,\Pi)=\delta(A,\varnothing)
 =|L\setminus\operatorname{Deck}_{\le d}(A)|
\]

when every pinned target belongs to `L` and occurs at its forced address.

## 3. No hidden typed multiplicity

The conclusion would not apply to a pre-word candidate graph in which one
address represents several alternative values, nor to a router whose
interior capacities or terminal type are additional resources.  Those are
explicitly excluded by the direct one-phase definition

\[
 (S,C)\in H_A\iff \operatorname{OR}_A(C)=S.
\]

Inside that graph there is no hidden occurrence-state multiplicity: state
is already fixed and target labels are literal values.  Thus the Hall
collapse is not merely sufficient; it is the exact semantics of the model.

## 4. Scope

The result does not choose the word `A`.  All construction difficulty is
now concentrated in producing one global pinned antecedent whose
short-interval OR map covers the target family.  Guard-pruning, Rado, or
flow formulations may remain useful before the word is selected, but they
do not form a second terminal gate afterward.
