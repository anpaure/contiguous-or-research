# Hinge target chains, one-copy owners, and projected Hamilton topology coexist statically

**Date:** 2026-08-07  
**Method:** full-base star packing, one SCD completion, and the
antichain-top Middle Levels owner lift  
**Status:** audited theorem after the designated-occurrence scope correction;
see `MATH_AUDIT_HINGE_TARGET_OWNER_HAMILTON_STATIC_COEXISTENCE_20260807.md`

## 1. Input target bank

Use the odd parameters

\[
                         n=2m+1,
 \qquad                    s=m-2d.
\]

The theorem
`MATH_THEOREM_FULL_BASE_STAR_PACKING_AND_SCD_COMPLETION_20260807.md`
gives an almost-spanning family of distinct rank-\(s\) bases and one fixed
symmetric-chain decomposition which completes every selected base to a
pairwise disjoint saturated chain through rank \(m-1\).

For each selected base, choose one age
\(a\in\{0,1,\ldots,d-1\}\) according to the single-bulge schedule and
retain from its saturated chain precisely the \(d\) ranks

\[
 \begin{cases}
 s,s+1,\ldots,s+a-1,\quad
 t+a,t+a+1,\ldots,m-1,&a>0,\\[2mm]
 t,t+1,\ldots,m-1,&a=0,
 \end{cases}                                             \tag{1.1}
\]

where \(t=m-d\).  Call the resulting nested target chain
\(\mathcal C_u\).  Different \(u\)'s have disjoint target inventories.
Every \(\mathcal C_u\) has a distinct maximum of rank \(m-1\), so the
maxima form an antichain.

Add empty roles until there are exactly

\[
                         W={2m+1\choose m}
\]

roles.

## 2. Lower-shore antichain-top lift

The antichain-top theorem
`MATH_THEOREM_ANTICHAIN_TOP_SCD_HAMILTON_OWNER_LIFT_AND_LITERAL_AGE_GATE_20260802.md`
is stated with the rank-\((m+1)\) shore named as the owner shore.  Its proof
also gives the following lower-shore form.

### Lemma 2.1 (lower-shore form)

For any family of pairwise target-disjoint nested chains whose maxima form
an antichain below rank \(m\), there exist:

1. a Middle Levels Hamilton cycle
   \[
   q_0,T_0,q_1,T_1,\ldots,q_{W-1},T_{W-1},q_0,
   \]
   with \(|q_i|=m\) and \(|T_i|=m+1\);
2. a bijection from the roles to the lower owners \(q_i\); and
3. one static depth-\(d\) source state for every nonempty role,

such that the union of that state's cells is \(q_i\) and all targets of
the assigned chain occur as its prescribed nested suffix unions.

#### Proof

Choose either parity matching of a Middle Levels Hamilton cycle and extend
it to a full SCD by the central-matching extension theorem.  Each antichain
maximum lies in a different SCD chain.  Assign its role to that chain and
use the chain's rank-\(m\) member \(q_i\) as owner.  Empty roles fill the
remaining chains.

For a prescribed target chain
\(P_1\subset\cdots\subset P_h\subset q_i\), partition each difference
\(P_{j+1}\setminus P_j\) into the required source cell and partition the
remaining set \(q_i\setminus P_h\) among the unmarked age cells.  This is
the same gap-partition construction as in the antichain-top theorem and
realizes every prescribed suffix union.  Along the alternating Hamilton
cycle, consecutive lower owners \(q_i,q_{i+1}\) are distinct facets of
\(T_i\), hence differ by one Johnson exchange. \(\square\)

## 3. Static coexistence theorem

### Theorem 3.1

The single-bulge target bank in Section 1 admits a simultaneous realization
with:

1. every selected named lower target assigned to exactly one nonempty role,
   with the designated target inventories of the nonempty roles pairwise
   disjoint;
2. every selected role assigned to a different rank-\(m\) owner;
3. all \(W\) rank-\(m\) owners occurring exactly once; and
4. the owner order forming one Johnson Hamilton cycle.

In particular, no remaining obstruction can be attributed merely to lower
target Hall, owner capacity, owner injectivity, or projected central
Hamiltonicity.

#### Proof

The selected target chains are pairwise disjoint and their maxima are a
rank-\((m-1)\) antichain.  Apply Lemma 2.1, assigning the empty roles to all
unused owners.  This proves uniqueness in the designated selected-role
inventory.  It does not assert that arbitrary later fillings of the empty
roles avoid those targets. \(\square\)

## 4. Exact remaining quantifier

The theorem is **static**.  If the state at role \(i\) is

\[
                         X^i=(X^i_0,\ldots,X^i_d),
\]

one literal cyclic word additionally requires the cellwise shift equations

\[
 \boxed{
 X^{i+1}_{j+1}=X^i_j\setminus X^{i+1}_0
 \qquad(0\le j<d).}                                    \tag{4.1}
\]

The gap partitions used in Lemma 2.1 are independent from role to role and
need not satisfy (4.1).  Conversely, the literal single-bulge rings satisfy
(4.1) inside each ring, but their higher named targets and owners have not
yet been aligned with the global packing of Theorem 3.1.

Therefore the surviving lower/owner theorem is precisely:

> **Literal hinge alignment.** Choose the target packing, SCD completion,
> owner Hamilton cycle and gap partitions in one common fibre satisfying
> (4.1), with only bounded terminal sidecar.

After that, arbitrary-width upper coverage and the terminal compiler still
have to be retained.  The present result does not claim those rows.

Nor does it claim global one-occurrence uniqueness for the selected targets:
uncontrolled suffixes in the empty/background roles may repeat them.  That
avoidance requirement belongs to the literal-alignment/compiler gate.
