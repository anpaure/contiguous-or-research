# Independent audit: forked one-phase readout and continuation-state erasure

**Date:** 2026-08-04  
**Method:** independent pure-mathematical quantifier and charge replay; no
computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_FORKED_ONE_PHASE_READOUT_AND_CONTINUATION_STATE_ERASURE_20260804.md`  
**Audited SHA-256:**
`743648ce5b9b6f0bbd782df951b1ea63b15d81981ee62f2b131abe508a09e587`

## Verdict

**INDEPENDENT GO as an exact conditional reduction.**  Existential cloning,
odd/even indexing, the finite-horizon weakening, terminal charges, and the
two permitted parent-boundary semantics are all correct.  No source
correction was required.  The theorem removes a correlation between
continuation and readout; it supplies neither construction.

## 1. Existential cloning

For one immutable finite certificate `g`, the three assertions

\[
 C_m(g,g'),\qquad R_m^o(g,w^o),\qquad R_m^e(g,w^e)
\]

have independent existential witnesses.  Reusing `g` as input does not
superpose the children, concatenate their words, or require their physical
resources to be disjoint.  It is ordinary logical contraction of a finite
witness.  Thus the proof does not need one child variable satisfying all
three predicates.

In the left-total formulation, one continuation successor may be selected
at each stage, while both readout witnesses are independently selected from
the current state.  Countable recursion constructs the required auxiliary
spine; no compatibility between a readout child and the chosen successor is
used.

## 2. Parity and finite horizons

The indexing

\[
 o_m=2m+1,\qquad e_m=2m+2
\]

partitions every dimension `k>=2m_0+1` into exactly one odd or even
readout.  Both readout relations are therefore necessary for the advertised
all-dimension conclusion, and the maximum of their charges is sufficient.

The finite-horizon corollary has the correct quantifiers.  For each
requested `M`, it assumes a complete path from the same fixed base through
index `M` and cheap readouts only at that leaf.  This proves the two
dimensions `o_M,e_M`.  Repeating the existence argument separately for
each `M` proves the dimensionwise upper bound.  Paths for different
horizons need not be nested or compatible.  The source correctly warns
that arbitrarily long paths without a cheap leaf at every requested
horizon would not suffice.

## 3. Charge ledger

For a terminal branch at dimension `k`, `chi` is its already incurred
physical excess over `B(k)`.  The one-phase terminal theorem leaves at most
`u(T_0)` upper targets and exactly
`delta(A,Pi^epsilon)` residual strict-lower targets.  Literal appending
therefore gives the safe charge

\[
              \chi+u(T_0)+\delta(A,\Pi^\epsilon).
\]

The upper and strict-lower shores are rank-disjoint; accidental repair can
only reduce this upper bound.  The `2(d-1)` forced ray facts use distinct
short intervals already present in the antecedent and add no positions.
Any split, extra packet cell, or other actual physical extension remains in
`chi`.

The continuation child contributes no length to either terminal word,
because it is a separate existence witness.  Terminal repairs are paid
once at the requested leaf and are not propagated to a later dimension.

## 4. Parent interior versus existential boundary

The continuation quotient is valid under the exact factorization

\[
 \mathcal F_m^\to(X,Y,Z)
 \Longleftrightarrow
 \mathcal I_m^\to(X,Y)\wedge\mathcal E_m^\to(Y,Z).
\]

Since the exterior predicate has no `X` argument, any witness to
`Q_m^to(Y)=exists X I_m^to(X,Y)` combines with a valid exterior edge.
No hidden bulk-to-future dependence may remain outside `Y`.

The theorem also correctly distinguishes two source semantics.

1. If `Y` is itself the existential auxiliary certificate, continuation
   and terminal copies may rematerialize different interiors over `Y`.
2. If the recursion consumes one specified literal parent interior, that
   replacement is valid only after a rematerialization theorem, or after
   proving continuation and readout left-total for every retained interior
   representative.

Thus state erasure cannot silently change a literal parent.  Bounded formal
dimension of `Y` is also insufficient: its literal serialization and all
cross-boundary histories, capacities, and occurrence identities must be
uniformly bounded.

## 5. Exact erasure scope

Packet phase, ray pins, the terminal antecedent, residual graph/matching,
and repair data may be erased only from the **continuation** state and only
when no continuation theorem reads them.  A socket, cap occurrence, upper
witness, or reservoir fact used by the continuation branch remains in `Y`
unless it is rematerialized or reset.  Leaf-only packet planting is
therefore a valid quantifier reduction, not a planting theorem.

The result proves neither bounded continuation state nor either bounded
terminal readout.  The forked regenerative guarded extension remains the
exact missing existence statement.
