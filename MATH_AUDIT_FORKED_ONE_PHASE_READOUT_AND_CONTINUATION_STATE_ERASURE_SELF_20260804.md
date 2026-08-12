# Self-audit: forked one-phase readout and continuation-state erasure

**Date:** 2026-08-04  
**Method:** pure quantifier and charge audit; no computation or search  
**Target:**
`MATH_THEOREM_FORKED_ONE_PHASE_READOUT_AND_CONTINUATION_STATE_ERASURE_20260804.md`  
**Target SHA-256:**
`743648ce5b9b6f0bbd782df951b1ea63b15d81981ee62f2b131abe508a09e587`  
**Verdict:** **SELF-GO as an exact conditional reduction.**  Independent
audit is still required before promotion as an authoritative theorem.

## 1. Odd/even indexing

The auxiliary state at index `m` lies in odd dimension `o_m=2m+1`.
Its two readouts cover dimensions `o_m` and `e_m=2m+2`.  As `m` ranges
over every integer from `m_0` onward, these dimensions partition every
integer `k>=2m_0+1`.  Thus the maximum of the odd and even readout charges
is the correct uniform additive constant.  An odd-only readout would leave
all even dimensions uncovered; this is explicitly retained as a caveat.

## 2. Clone-and-fork quantifiers

Theorem 1.1 assumes three separate relations from one immutable
mathematical parent certificate:

\[
 C_m(g_m,g_{m+1}),\qquad
 R_m^o(g_m,w_m^o),\qquad
 R_m^e(g_m,w_m^e).
\]

No conclusion uses a common child variable.  A finite certificate can be
reused as input to independent existential constructions, so the
conjunction of these three statements is sufficient.  This does not assert
that their child resources coexist and does not concatenate any words.

Corollary 1.2 has the correct induction quantifier: left-total continuation
on the selected family permits one successor to be chosen recursively,
while the two readouts are independent existential witnesses at the current
state.

Corollary 1.3 is also exact.  For every requested horizon it assumes a
complete finite path from the fixed base and a cheap terminal leaf.  The
resulting word proves the upper bound only at that requested horizon, which
is all dimensionwise existence requires.  Paths for different horizons do
not have to be compatible.  Merely having arbitrarily long paths without a
cheap leaf at each horizon would not suffice, and the theorem does not claim
otherwise.

## 3. Terminal charge

The terminal branch starts with physical excess `chi`.  Its one-phase
compiler leaves exactly the residual lower deficiency
`delta(A,Pi^epsilon)` and at most `u(T_0)` retained upper defects.  Literal
appending therefore gives the valid upper charge

\[
             \chi+u(T_0)+\delta(A,\Pi^\epsilon).
\]

The upper and strict-lower target families lie on opposite sides of the
middle rank, so summing their cardinality bounds is safe.  Possible overlap
or accidental repair can only lower the true charge.  The `2(d-1)` ray
facts themselves add no positions: they are matched to distinct short
intervals already in the terminal antecedent.  Any actually appended packet
cell or split position remains in `chi`.

The continuation child contributes no term to the terminal word length.
It is a separate certificate used only to prove that later auxiliary inputs
exist.

## 4. Continuation-only quotient

Equation (3.1) is an exact separator hypothesis for the continuation
predicate.  Existentially quantifying the child-local bulk `X` is valid
because the exterior predicate has no `X` argument.  Hence the next
continuation sees only `Y`.

The terminal predicate has no future exterior and is evaluated on an
independent copy.  It therefore needs no analogous separator.  Section 3
correctly distinguishes two semantics:

1. If `Y` is an existential boundary state, continuation and terminal
   branches may rematerialize different parent-interior representatives over
   `Y`.
2. If a recursion consumes one specified literal parent interior, such a
   replacement needs either a rematerialization theorem or left-totality of
   both fork relations on every retained representative.

This qualification prevents the quotient from silently changing the
source parent.

The proposed carried state remains conditional on bounded **literal**
serialization and complete continuation factorization.  A bounded number
of formal history/cap coordinates is not treated as bounded when their
physical dependency closure grows with `d`.

## 5. Scope of state erasure

The theorem erases the phase, packet parameters, ray facts, terminal
antecedent, residual graph/matching and repair family only from the
continuation state.  It does not erase any such occurrence if the
continuation router, topology, residence or cap proof reads it.  The state
ledger in Section 4 correctly moves every shared occurrence back into `Y`
unless it is rematerialized or reset.

Leaf-only packet planting follows from the finite-horizon theorem but is
purely a quantifier reduction.  It does not prove that a terminal leaf has
an upper-complete resident host, a legal packet slot, a global antecedent or
bounded guard-pruned Hall.

## 6. Remaining hypotheses

The theorem leaves all substantive existence rows visible:

* a continuation child with a uniformly bounded complete boundary;
* odd and even terminal forks constructible from the declared parent state;
* in each terminal fork, one initially upper-complete globally resident
  carrier, coherent ring, protected reservoir and legal packet phase;
* one global nonempty antecedent extending the forced rays; and
* bounded residual literal Hall deficiency.

Therefore the theorem proves neither `nu(k)<=B(k)+O(1)` nor exact equality.
It only removes the unnecessary requirement that the terminally compiled
child also regenerate.
