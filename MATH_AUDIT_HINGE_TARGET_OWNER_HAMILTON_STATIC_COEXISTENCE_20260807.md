# Audit of hinge-target / one-copy-owner / Hamilton static coexistence

**Date:** 2026-08-07  
**Audited file:**
`MATH_COROLLARY_HINGE_TARGET_OWNER_HAMILTON_STATIC_COEXISTENCE_20260807.md`  
**Verdict:** PASS after one scope correction.  The static coexistence
argument is valid.  The phrase “every selected named lower target used
exactly once” must mean exactly once in the *designated selected-role
inventory*.  It is not yet proved as a uniqueness statement among every
suffix occurrence of arbitrarily filled empty roles.

## 1. Parameter and cardinality checks

The corollary uses

\[
 n=2m+1,\qquad s=m-2d,
\]

so the Middle Levels graph has shores

\[
 { [n]\choose m}\quad\text{and}\quad{ [n]\choose m+1}
\]

of common size

\[
                         W={2m+1\choose m}.
\]

The full-base/SCD theorem selects at most
\({n\choose s}<W\) chains, so padding by empty roles to exactly \(W\)
roles is legitimate.

For age \(a>0\), profile (1.1) contains

\[
 a+(d-a)=d
\]

strictly nested targets.  For age \(a=0\), it contains the \(d\) ranks
\(t,t+1,\ldots,m-1\).  Every nonempty role therefore has exactly \(d\)
proper suffix targets, and its maximum has rank \(m-1\).  All maxima are
distinct and lie in one rank, hence form an antichain.

## 2. The lower-shore Hamilton lift is valid

Take any Middle Levels Hamilton cycle in the form

\[
 q_0,T_0,q_1,T_1,\ldots,q_{W-1},T_{W-1},q_0,
\tag{2.1}
\]

where \(|q_i|=m\) and \(|T_i|=m+1\).  Choose the parity matching

\[
                         M=\{q_iT_i:i\in\mathbb Z_W\}.
\tag{2.2}
\]

The central-matching extension theorem extends \(M\) to a full SCD of
\(B_n\).  Distinct rank-\((m-1)\) maxima lie in different SCD chains.  The
rank-\(m\) member of the chain containing a prescribed maximum is one of
the \(q_i\), contains that maximum, and is unique.  Assign the role to
that lower owner.

This proves an injective owner assignment.  Empty roles fill the remaining
SCD chains.  Moreover, consecutive lower owners \(q_i,q_{i+1}\) are the
two distinct rank-\(m\) facets of \(T_i\), so

\[
                         |q_i\triangle q_{i+1}|=2.
\]

Thus the cyclic lower-owner order is a simple Johnson Hamilton cycle.
The wrap edge is supplied by \(T_{W-1}\).

No fixed-SCD Hamilton assertion is being smuggled in: the Hamilton cycle
and one parity matching are chosen first, and that matching is then
extended to an SCD.  This is the correct quantifier order.

## 3. Static source-state realization is exact

Let a prescribed role have chain

\[
 P_1\subset P_2\subset\cdots\subset P_d,
 \qquad |P_d|=m-1,
\]

and assigned lower owner \(q\in{[n]\choose m}\), with \(P_d\subset q\).
Define source cells, in suffix order, by the nonempty differences

\[
 P_1,\quad P_2\setminus P_1,\quad\ldots,\quad
 P_d\setminus P_{d-1},\quad q\setminus P_d.
\tag{3.1}
\]

Every difference is nonempty because the prescribed targets are strictly
nested; the last difference is a singleton.  Reversing (3.1) into source
order gives \(d+1\) nonempty cells, union \(q\), and exactly the prescribed
\(d\) proper suffix unions.  Hence every nonempty role has a valid static
depth-\(d\) state.

The construction does not use the intermediate members of the new SCD.
It needs only the fact that the rank-\((m-1)\) maximum and its assigned
rank-\(m\) owner lie in the same chain.  Thus it remains valid even though
the target chains were originally obtained from a different fixed SCD.

## 4. One required wording correction

The selected target chains are pairwise disjoint, so each selected named
target has exactly one **designated** selected-role occurrence.  However,
if the empty roles are later filled by arbitrary static states, their
uncontrolled proper suffix unions could repeat a selected target.

Therefore item 1 of Theorem 3.1 should be read or rewritten as

> every selected named lower target is assigned to exactly one nonempty
> role, and the designated target inventories of the nonempty roles are
> pairwise disjoint.

The stronger literal statement

> every selected target occurs exactly once among all proper suffix cells
> of all \(W\) states

requires an additional avoidance or full compiler theorem and is not
proved by the present argument.

Likewise, the static theorem may assign all \(W\) owner roles without
choosing literal states for the empty roles.  Those roles can certainly be
partitioned into \(d+1\) nonempty cells when \(m\ge d+1\), but doing so
while preserving global target uniqueness is a separate row.

## 5. Exact closed/open ledger

The corollary genuinely closes the simultaneous **static** coexistence of:

1. the designated abstract hinge target chains;
2. distinct rank-\(m\) containing owners;
3. every rank-\(m\) owner exactly once as a role; and
4. one projected Johnson Hamilton order of those owners.

It does not close:

1. the cellwise shift equations
   \[
   X^{i+1}_{j+1}=X^i_j\setminus X^{i+1}_0;
   \]
2. identification with the literal single-bulge ring states;
3. avoidance of selected targets by empty/background roles;
4. arbitrary-width upper coverage; or
5. the terminal common compiler.

Subject to the “designated occurrence” correction, the candidate is
mathematically sound.
